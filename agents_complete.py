from anthropic import Anthropic
from dotenv import load_dotenv
import pandas as pd
import os
import json
import concurrent.futures
import time
# Report generation lives in a separate file so the analysis and coordination
# code here never has to know anything about markdown or HTML formatting.
# This split is also what lets the two Claude Code rule files scope to
# genuinely different files instead of both firing on every edit.
from report_generator import generate_clinical_report, save_report_to_file, generate_html_report, save_html_report_to_file

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=api_key)
model = "claude-sonnet-5"

# Loaded once at import time. Every analysis function below reads this same
# dataframe rather than being passed a fresh copy, so all four subagents and
# the tool layer are working against identical data within a single run.
df = pd.read_csv(r"telehealth.csv")

# ---------------------------------------------------------------------------
# ANALYSIS FUNCTIONS
# These do the actual math against the dataframe. Each one is called by the
# tool dispatcher (run_tool) further down, never directly by a subagent.
# ---------------------------------------------------------------------------

def get_df_info():
    temp_df = df.copy()
    temp_df.fillna("N/A", inplace=True)
    return {
        "columns": temp_df.columns.tolist(),
        "rows": len(temp_df),
        "data_types": temp_df.dtypes.astype(str).to_dict(),
        "top_5_rows": temp_df.head().to_dict(orient="records"),
    }

def run_cohort_analysis(df):
    # These two dicts are the whole reason this function can't be taken down
    # by one bad program. Every program that computes successfully lands in
    # result. Every program that throws an exception lands in
    # failed_programs instead, and the loop just continues to the next one.
    result = {}
    failed_programs = {}
    for program, group in df.groupby("program_type"):
        try:
            total_patients = len(group)
            active_patients = (
                group["retention_status"].astype(str).str.lower().isin(["active", "completed"]).sum()
            )
            churned_patients = total_patients - active_patients
            retention_rate = round((active_patients / total_patients) * 100, 2)

            result[program] = {
                "number_of_patients": total_patients,
                "average_treatment_duration_weeks": round(group["treatment_duration_weeks"].mean(), 2),
                "active_patients": int(active_patients),
                "churned_patients": int(churned_patients),
                "retention_rate_percent": retention_rate,
            }
        except Exception as e:
            failed_programs[program] = str(e)
    # Always returns this same two-key shape, even if every program failed.
    # Nothing downstream has to check whether "data" exists before reading it.
    return {"data": result, "failed_programs": failed_programs}

def run_outcome_analysis(df):
    # Same per-program isolation pattern as run_cohort_analysis above.
    result = {}
    failed_programs = {}
    for program, group in df.groupby("program_type"):
        try:
            retention_rate = round(
                (group["retention_status"].astype(str).str.lower().isin(["active", "completed"]).sum() / len(group)) * 100, 2
            )
            duration_q1 = round(group["treatment_duration_weeks"].quantile(0.25), 2)
            duration_median = round(group["treatment_duration_weeks"].quantile(0.5), 2)
            duration_q3 = round(group["treatment_duration_weeks"].quantile(0.75), 2)
            duration_mean = round(group["treatment_duration_weeks"].mean(), 2)

            churned = group[group["retention_status"].astype(str).str.lower().eq("dropped off")]

            early_dropoff = len(churned[churned["treatment_duration_weeks"] <= duration_q1])
            mid_dropoff = len(churned[(churned["treatment_duration_weeks"] > duration_q1) &
                                    (churned["treatment_duration_weeks"] <= duration_q3)])
            late_dropoff = len(churned[churned["treatment_duration_weeks"] > duration_q3])

            result[program] = {
                "retention_rate_percent": retention_rate,
                "duration_trends": {
                    "mean_weeks": duration_mean,
                    "median_weeks": duration_median,
                    "q1_weeks": duration_q1,
                    "q3_weeks": duration_q3,
                },
                "drop_off_points": {
                    "early_stage_patients": int(early_dropoff),
                    "mid_stage_patients": int(mid_dropoff),
                    "late_stage_patients": int(late_dropoff),
                }
            }
        except Exception as e:
            failed_programs[program] = str(e)
    return {"data": result, "failed_programs": failed_programs}

def flag_anomalies(df):
    # Same per program isolation pattern again. Three functions, three
    # different calculations, one shared reliability pattern.
    result = {}
    failed_programs = {}
    for program, group in df.groupby("program_type"):
        try:
            q1 = group["treatment_duration_weeks"].quantile(0.25)
            q3 = group["treatment_duration_weeks"].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - (1.5 * iqr)

            short_duration_outliers = group[group["treatment_duration_weeks"] < lower_bound]
            short_duration_count = len(short_duration_outliers)

            churned = group[group["retention_status"].astype(str).str.lower().eq("dropped off")]
            churn_rate = round((len(churned) / len(group)) * 100, 2)

            abnormal_churn = churn_rate > 25.0

            result[program] = {
                "short_duration_outliers": {
                    "count": int(short_duration_count),
                    "threshold_weeks": round(lower_bound, 2),
                    "affected_patients_percent": round((short_duration_count / len(group)) * 100, 2),
                    "flagged": short_duration_count > 0,
                },
                "abnormal_drop_off_clusters": {
                    "churn_rate_percent": churn_rate,
                    "flagged": abnormal_churn,
                    "interpretation": "High churn detected" if abnormal_churn else "Normal churn levels"
                }
            }
        except Exception as e:
            failed_programs[program] = str(e)
    return {"data": result, "failed_programs": failed_programs}


def chunk_dict_by_size(data, max_chars=6000):
    """
    Splits a dict's top-level items into a list of smaller dicts, keeping
    each chunk's JSON-serialized size under max_chars. This exists so a
    tool whose per program output could grow large (many programs, wide
    per program payloads) never returns a single blob big enough to blow
    out the context window in one shot.
    """
    chunks = []
    current_chunk = {}
    current_size = 2  # accounts for the {} braces in the eventual JSON

    for key, value in data.items():
        item_size = len(json.dumps({key: value}, default=str))
        # Close the current chunk and start a new one the moment adding
        # this item would push it over the limit. The item that triggered
        # the overflow becomes the first item in the next chunk.
        if current_chunk and current_size + item_size > max_chars:
            chunks.append(current_chunk)
            current_chunk = {}
            current_size = 2
        current_chunk[key] = value
        current_size += item_size

    if current_chunk or not chunks:
        chunks.append(current_chunk)

    return chunks


def _prepare_analysis_response(raw, tool_input, max_chars=6000):
    # This is the bridge between a raw analysis function's output and what
    # actually gets sent back to the model: chunked, indexed, and carrying
    # has_more so the model knows whether to ask for another chunk.
    tool_input = tool_input or {}
    requested_index = int(tool_input.get("chunk_index", 0))

    chunks = chunk_dict_by_size(raw["data"], max_chars=max_chars)
    chunk_index = max(0, min(requested_index, len(chunks) - 1))  # clamp, never index out of range

    return {
        "data": chunks[chunk_index],
        "chunk_index": chunk_index,
        "total_chunks": len(chunks),
        "has_more": chunk_index < len(chunks) - 1,
        "failed_programs": raw["failed_programs"],
    }


def _classify_error(exc):
    """
    Turns a raw exception into (category, isRetryable). Message content is
    checked first because a generic Python exception type (ValueError,
    RuntimeError, etc.) can represent very different real-world failures --
    a malformed value in the dataset is not retryable, but a message that
    reads like a transient connection/timeout issue is worth one retry.
    """
    message = str(exc)
    lowered = message.lower()

    if isinstance(exc, ValueError) and lowered.startswith("unknown tool"):
        return "unknown_tool", False

    if any(keyword in lowered for keyword in ["connection", "timeout", "temporarily", "unavailable", "network"]):
        return "transient_error", True

    if isinstance(exc, (ConnectionError, TimeoutError, OSError)):
        return "transient_error", True

    if isinstance(exc, (KeyError, TypeError, ValueError)):
        return "data_error", False

    return "unexpected_error", True


def run_tool(tool_name, tool_input):
    # Plain dispatcher, no error handling here on purpose -- that's what
    # run_tool_safe below is for. This function is allowed to raise.
    tool_input = tool_input or {}
    if tool_name == "get_df_info":
        return {"data": get_df_info()}
    elif tool_name == "run_cohort_analysis":
        return _prepare_analysis_response(run_cohort_analysis(df), tool_input)
    elif tool_name == "run_outcome_analysis":
        return _prepare_analysis_response(run_outcome_analysis(df), tool_input)
    elif tool_name == "flag_anomalies":
        return _prepare_analysis_response(flag_anomalies(df), tool_input)
    raise ValueError(f"Unknown tool: {tool_name}")


def run_tool_safe(tool_name, tool_input, max_retries=1):
    """
    Wraps run_tool with structured error handling and one retry. Every
    call returns a consistent envelope so the model can reason about it:
      success -> {"success": True, "data": ..., ...chunk metadata...}
      failure -> {"success": False, "error_category", "isRetryable", "message"}
    A retry only happens once, and only when the classified error is
    marked retryable -- a permanently broken tool fails the same way
    twice and returns the structured failure rather than looping forever.
    A short pause happens before the retry, since transient errors are
    usually network or timeout issues that need a moment to clear rather
    than something an instant retry would catch. Partial per-program
    results are not lost when a tool call fails outright -- that case is
    handled separately, by the failed_programs field on the success path,
    where individual programs can fail without taking down the whole call.
    """
    attempt = 0
    while True:
        try:
            # This is the actual call. Everything else in this function
            # exists to decide what to do if this line raises.
            result = run_tool(tool_name, tool_input)
            return {"success": True, **result}
        except Exception as e:
            category, retryable = _classify_error(e)
            if retryable and attempt < max_retries:
                attempt += 1
                time.sleep(1)  # brief pause before the one allowed retry
                continue
            # Either not retryable, or already used up the retry budget.
            # Return the failure as data instead of letting the exception
            # propagate, so the caller always gets a dict back, never a crash.
            return {
                "success": False,
                "error_category": category,
                "isRetryable": retryable,
                "message": str(e),
            }

# ---------------------------------------------------------------------------
# TOOL SCHEMA
# This is the array actually sent to the Claude API via the tools parameter.
# The API reads name, description, and input_schema to decide which tool to
# call and what arguments to pass. Every description below follows the same
# pattern on purpose: what it returns, what it does not, and which other
# tool to use instead. That pattern is the direct result of testing that
# found ambiguous questions caused the model to call two tools at once
# before the descriptions were tightened this way.
# ---------------------------------------------------------------------------
tools = [
    {
        "name": "get_df_info",
        "description": "Returns raw dataset structure: column names, data types, row count, and sample rows. Use this only to inspect what data exists before running any analysis. Provides no statistics, comparisons, trends, or risk flags.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "run_cohort_analysis",
        "description": "Returns a point-in-time snapshot per program for side-by-side comparison: patient counts and retention percentage. Use for ranking or comparing programs against each other, including ranking by churn or retention. Does not analyze drop-off timing or flag statistical risk. For timing use run_outcome_analysis, for risk thresholds use flag_anomalies. Response may be split across multiple chunks if the number of programs is large -- check has_more and call again with an incremented chunk_index to retrieve the rest.",
        "input_schema": {
            "type": "object",
            "properties": {
                "chunk_index": {
                    "type": "integer",
                    "description": "Which chunk of results to retrieve, starting at 0. Only needed if a previous call to this tool returned has_more: true."
                }
            },
            "required": []
        }
    },
    {
        "name": "run_outcome_analysis",
        "description": "Returns time-based behavior per program: how treatment length is distributed, and which stage (early, mid, late) churned patients left at. Use for understanding when or at what point in treatment patients drop off. Does not rank programs against each other or flag statistical risk. For ranking use run_cohort_analysis, for risk thresholds use flag_anomalies. Response may be split across multiple chunks if the number of programs is large -- check has_more and call again with an incremented chunk_index to retrieve the rest.",
        "input_schema": {
            "type": "object",
            "properties": {
                "chunk_index": {
                    "type": "integer",
                    "description": "Which chunk of results to retrieve, starting at 0. Only needed if a previous call to this tool returned has_more: true."
                }
            },
            "required": []
        }
    },
    {
        "name": "flag_anomalies",
        "description": "Returns statistical risk flags per program: treatment durations that are extreme outliers (IQR method) and churn rates exceeding a 25% threshold. Use for risk detection or exception flagging, not raw counts or timing. Does not provide patient counts or drop-off timing. For counts use run_cohort_analysis, for timing use run_outcome_analysis. Response may be split across multiple chunks if the number of programs is large -- check has_more and call again with an incremented chunk_index to retrieve the rest.",
        "input_schema": {
            "type": "object",
            "properties": {
                "chunk_index": {
                    "type": "integer",
                    "description": "Which chunk of results to retrieve, starting at 0. Only needed if a previous call to this tool returned has_more: true."
                }
            },
            "required": []
        }
    }
]

system_prompt = """<role>

You are a healthcare data analyst for a telehealth clinic.

Your task is to use the available tools to analyze patient retention and treatment outcome data, and identify patterns, trends, risk factors, and anomalies across programs.

You are NOT a doctor.

You must only analyze the data returned by the tools and summarize observations.

Do not make assumptions beyond the data provided. Do not add anything on your own.

</role>

<job>

What you can do:

- Use the available tools to inspect dataset structure, compare programs, analyze treatment timing, and detect statistical anomalies
- Identify retention and treatment-related trends
- Surface common risk factors related to program design (duration, drop-off timing, churn)
- Calculate counts, percentages, averages, and frequencies using tool outputs
- Flag anomalies and outliers using flag_anomalies
- Highlight programs that may require the most attention based on the data
- Summarize findings in plain English

What you cannot do:

- No diagnosis
- No treatment suggestions
- No medical advice
- No referrals
- No clinical recommendations
- No assumptions about missing information
- No information that is not present in the tool outputs

</job>

<analysis_rules>

- Use only the information returned by the tools
- Call the tools needed to gather sufficient data before answering
- If a tool result is missing or empty, mention it instead of making assumptions
- Use the counts and percentages already provided in tool outputs directly
- Compare programs against each other when identifying patterns and anomalies
- Flag unusually high or low values (e.g., high churn, short duration outliers)
- Highlight programs that stand out from the others
- Explain observations in simple and clear language. No medical jargon.

Every tool response is wrapped in an envelope. Read it before using the data:
- If success is false, the tool call failed. error_category and message explain why, and isRetryable indicates whether it is worth trying again later. Do not fabricate the data that tool would have returned -- note the limitation in your findings instead.
- If the response includes has_more: true, you have not seen all the data yet. Call the same tool again with chunk_index increased by 1 (starting at 0) and keep going until has_more is false, so no program is missed.
- If the response includes a non-empty failed_programs object, those specific programs could not be analyzed by that tool even though the call itself succeeded. Mention this limitation for those specific programs rather than silently omitting them or guessing their numbers.

Prioritize programs based on:
- Retention rate
- Churn rate
- Treatment duration trends
- Drop-off timing (early, mid, late stage)
- Flagged anomalies

</analysis_rules>

<definitions>

Risk Factor:

- A characteristic associated with poorer retention outcomes in the dataset.
- Examples include high churn rate, short average treatment duration, or concentrated mid-stage drop-off.

Anomaly:

- Statistically unusual treatment durations (outliers)
- Churn rates exceeding the defined risk threshold
- Patterns noticeably different from the group average

</definitions>

<output_structure>

Return ONLY the JSON object. No preamble, no explanation, no markdown. Start with { and end with }.

- Return ONLY valid JSON.
- No markdown.
- No code blocks.
- No text outside the JSON response.
- No preamble or explanation.
- Use plain English.
- Use numbers and percentages whenever possible.
- Keep explanations concise but informative.

</output_structure>

<important_notes>

- Do not diagnose any condition.
- Do not suggest treatments.
- Do not provide medical advice.
- Do not recommend medications, tests, or referrals.
- Focus only on what the tool outputs show.
- Support observations with numbers and evidence from the tool outputs whenever possible.

</important_notes>"""

output_schema = """
{
  "overall_summary": "",
  "program_patterns": [
    {
      "pattern": "",
      "evidence": "",
      "affected_programs": []
    }
  ],
  "common_risk_factors": [
    {
      "factor": "",
      "frequency": "",
      "affected_programs": []
    }
  ],
  "high_attention_programs": [
    {
      "program": "",
      "priority": "High | Medium | Low",
      "reasons": []
    }
  ],
  "anomalies": [
    {
      "program": "",
      "observation": ""
    }
  ],
  "key_concerns": [],
  "final_summary": ""
}"""

retention_output_schema = """
{
  "overall_summary": "",
  "program_patterns": [
    {
      "pattern": "",
      "evidence": "",
      "affected_programs": []
    }
  ],
  "common_risk_factors": [
    {
      "factor": "",
      "frequency": "",
      "affected_programs": []
    }
  ],
  "high_attention_programs": [
    {
      "program": "",
      "priority": "High | Medium | Low",
      "reasons": []
    }
  ],
  "anomalies": [
    {
      "program": "",
      "observation": ""
    }
  ],
  "key_concerns": [],
  "final_summary": "",
  "duration_and_dropoff_by_program": {
    "<program_name>": {
      "retention_rate_percent": 0,
      "duration_trends": {
        "mean_weeks": 0,
        "median_weeks": 0,
        "q1_weeks": 0,
        "q3_weeks": 0
      },
      "drop_off_points": {
        "early_stage_patients": 0,
        "mid_stage_patients": 0,
        "late_stage_patients": 0
      }
    }
  }
}"""

subagent_prompts = {
    "program_performance": """<dimension>PROGRAM PERFORMANCE</dimension>

Call get_df_info first to confirm dataset structure, then call run_cohort_analysis
to compare programs side-by-side.

Analyze:
1. Enrollment volume per program
2. Completion rate, active rate, and drop-off rate per program
3. Average treatment duration per program
4. Ranking of programs from best to worst performing
5. Which program needs the most attention and why

Return this exact JSON structure:
""" + output_schema,

    "patient_segmentation": """<dimension>PATIENT SEGMENTATION</dimension>

Call get_df_info first to confirm dataset structure, then call run_cohort_analysis
and run_outcome_analysis to understand how patients group by program and duration.

Analyze:
1. Segment patients by program_type -- size and retention profile of each segment
2. Segment patients by treatment stage (early/mid/late drop-off timing)
3. Which segment is highest-risk (most likely to drop off)
4. Which segment is highest-value (most likely to retain)

Return this exact JSON structure:
""" + output_schema,

    "retention_analysis": """<dimension>RETENTION PATTERNS</dimension>

Call get_df_info first to confirm dataset structure, then call run_outcome_analysis
to understand timing and depth of drop-off across programs.

Analyze:
1. Overall retention rate across all programs
2. When in treatment (early/mid/late stage) most drop-offs occur, per program
3. Duration trends (mean, median, Q1, Q3) per program
4. Which program has the most concerning retention timing pattern

In addition to your narrative findings above, you must also populate
duration_and_dropoff_by_program in the JSON output below. The per-program
numbers from run_outcome_analysis live inside the tool response's data field.
If the response has has_more: true, call run_outcome_analysis again with an
incremented chunk_index and keep going until has_more is false, combining
every chunk's programs together. For every program you receive, copy its
retention_rate_percent, duration_trends, and drop_off_points fields into
duration_and_dropoff_by_program exactly as the tool returned them -- do not
summarize or round differently. If a program appears in the tool's
failed_programs field, leave it out of duration_and_dropoff_by_program rather
than inventing numbers for it, and mention the gap in key_concerns instead.
This field carries the tool's raw structured findings forward so downstream
report generation never needs to call the tool again or touch the dataset
directly.

Return this exact JSON structure:
""" + retention_output_schema,

    "anomaly_detection": """<dimension>ANOMALY DETECTION</dimension>

Call get_df_info first to confirm dataset structure, then call flag_anomalies
to detect statistical outliers and abnormal churn rates.

Analyze:
1. Which programs have statistically abnormal treatment duration outliers (IQR method)
2. Which programs exceed the 25% churn rate risk threshold
3. Severity ranking of all flagged anomalies (High/Medium/Low)
4. Recommended next step for each flagged anomaly

Return this exact JSON structure:
""" + output_schema
}

synthesis_prompt = """You are the Coordinator Agent. You did NOT analyze any data yourself.
Four independent subagents already completed their analyses and returned structured findings.
Your job is strictly synthesis.

Instructions:
1. MERGE: Combine all four reports into one unified view. Do not repeat the same finding
   under multiple sections -- place it where it fits best and reference it elsewhere.
2. RESOLVE: If two subagents report conflicting numbers or conclusions about the same
   program, note the discrepancy and use the more conservative (data-supported) figure.
3. CONNECT: Identify cross-cutting themes -- e.g., a segment flagged in segmentation that
   also appears in anomaly detection, or a retention pattern that explains a performance ranking.
4. PRIORITIZE: Produce a single, deduplicated list of recommendations ranked by impact,
   drawing from all four reports. Do not repeat recommendations that say the same thing
   in different words.
5. KEEP IT SHORT: Each highlight array should have 3-5 bullets max, not exhaustive lists.

Do not add new analysis, new numbers, or new observations that are not in the subagent reports.
Do not diagnose conditions, suggest treatments, or provide medical advice.

Return ONLY valid JSON. No markdown, no code blocks, no preamble, no text outside the JSON.

{
  "executive_summary": "...",
  "program_performance_highlights": ["...", "..."],
  "patient_segmentation_highlights": ["...", "..."],
  "retention_highlights": ["...", "..."],
  "anomaly_highlights": ["...", "..."],
  "cross_cutting_insights": ["...", "..."],
  "top_priority_recommendations": ["...", "..."]
}"""

def subagent_runner(dimension_name, dimension_addition):
    """
    Runs one subagent through a full tool-calling conversation until it
    returns its final structured report. Called once per dimension
    (program_performance, patient_segmentation, retention_analysis,
    anomaly_detection), and the four calls happen in parallel via the
    ThreadPoolExecutor at the bottom of this file, not inside this function.
    This function itself is single-threaded and has no idea the other
    three subagents exist.
    """
    # Every subagent gets the same core guardrails, plus its own specific
    # task appended. dimension_addition is where the four subagents actually
    # differ from each other.
    system = f"{system_prompt}\n\n{dimension_addition}"

    messages = [
        {"role": "user", "content": f"Begin your analysis for: {dimension_name}"}
    ]

    # This loop is what makes the subagent "agentic" rather than a single
    # API call. It keeps going, sending the growing conversation back to
    # Claude, until Claude stops asking for tools and returns a final answer.
    # This is also the loop that transparently absorbs chunked tool
    # responses -- if a tool comes back with has_more: true, the model just
    # asks for the next chunk as another tool call, and this same loop
    # handles it with no special-case code required.
    while True:
        response = client.messages.create(
            model=model,
            max_tokens=8000,
            system=system,
            tools=tools,
            messages=messages
        )

        # stop_reason other than "tool_use" means Claude is done calling
        # tools and has produced its final text response.
        if response.stop_reason != "tool_use":
            final_text = ""
            for block in response.content:
                # Deliberately checking hasattr(block, 'text') rather than
                # assuming response.content[0] is text. Claude's responses
                # can include ThinkingBlock objects that have no .text
                # attribute, and indexing straight into [0] crashed here
                # before this loop was written this way.
                if hasattr(block, 'text'):
                    final_text += block.text

            # Claude sometimes wraps JSON in markdown code fences even when
            # told not to. Strip them defensively rather than trusting the
            # instruction alone.
            final_text = final_text.replace("```json", "").replace("```", "").strip()
            json_start = final_text.find('{')
            if json_start != -1:
                final_text = final_text[json_start:]

            try:
                return json.loads(final_text)
            except json.JSONDecodeError:
                # Return a structured error dict instead of letting the
                # exception propagate, so one subagent's bad output can't
                # crash the whole parallel run. The coordinator later has to
                # cope with this shape same as any other subagent result.
                return {"error": "Failed to parse response", "raw": final_text[:500]}

        # Claude wants to call one or more tools. Its own response, tool
        # calls included, has to be appended back into the conversation
        # before we can reply with the results, or the API will reject the
        # next call as missing context.
        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                # run_tool_safe, not run_tool directly. This is where the
                # error classification and one-retry logic actually gets
                # invoked, once per tool call the model makes.
                envelope = run_tool_safe(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,  # ties this result to the specific call it answers
                    "content": json.dumps(envelope, default=str),
                    "is_error": not envelope["success"]
                })

        # All tool results go back as one new user turn, and the while loop
        # repeats. Claude sees the results and either calls more tools
        # (another chunk, a different tool) or produces its final answer.
        messages.append({"role": "user", "content": tool_results})

def coordinator_synthesis(results):
    """
    Runs once, after all four subagents have finished. Unlike
    subagent_runner, this is a single API call with no tools attached and
    no loop -- the coordinator does no analysis of its own and never touches
    the dataframe. Its only job is reading the four subagents' JSON reports
    and producing one merged, prioritized summary.
    """
    # The four subagent reports, however they turned out, get serialized as
    # one JSON blob and handed to the coordinator as-is. If one subagent's
    # report is an error dict instead of real findings, the coordinator
    # still receives it and has to work with what's there -- there is no
    # validation step here that filters or fixes subagent output first.
    combined_input = json.dumps(results, indent=2, default=str)

    try:
        response = client.messages.create(
            model=model,
            max_tokens=8000,
            system=synthesis_prompt,
            messages=[
                {"role": "user", "content": f"Here are the four subagent reports:\n\n{combined_input}"}
            ]
        )
    except Exception as e:
        # If the API call itself fails outright, this is the only place
        # in the whole pipeline that can catch it, since nothing calls
        # coordinator_synthesis inside a try block. Without this, a failed
        # synthesis call would crash the entire script after all four
        # subagents had already completed successfully.
        return {"error": "Synthesis API call failed", "details": str(e)}

    # Same defensive text extraction as subagent_runner: only concatenate
    # blocks that actually have a .text attribute, in case a ThinkingBlock
    # shows up here too.
    raw_text = ""
    for block in response.content:
        if hasattr(block, 'text'):
            raw_text += block.text

    raw_text = raw_text.replace("```json", "").replace("```", "").strip()
    json_start = raw_text.find('{')
    if json_start != -1:
        raw_text = raw_text[json_start:]

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError as e:
        print(f"Synthesis JSON Parse Error: {e}")
        # Same pattern as subagent_runner's parse failure: return a
        # structured error dict rather than raising, so the pipeline can
        # still finish and the report generator gets something to work
        # with, even if that something is an explanation of what went wrong.
        return {"error": "Failed to parse synthesis", "raw": raw_text[:1000]}


# ---------------------------------------------------------------------------
# EXECUTION
# Everything below only runs when this file is executed directly (python
# agents_complete.py), not when it's imported. This is what
# makes it possible to import this module elsewhere, for testing or
# otherwise, without accidentally triggering a real pipeline run and
# spending real API calls.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 80)
    print("STEP 1: Running 4 Subagents in PARALLEL (ThreadPoolExecutor)")
    print("=" * 80)

    # This is the actual moment parallel execution happens. All four
    # subagent_runner calls get submitted to the thread pool essentially
    # at once, rather than one waiting for the previous one to finish.
    # Confirmed directly by testing: running these sequentially instead
    # produced identical output but took about four times as long.
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            dimension: executor.submit(subagent_runner, dimension, addition)
            for dimension, addition in subagent_prompts.items()
        }

        results = {}
        for dimension, future in futures.items():
            print(f"  Waiting for {dimension}...")
            # .result() blocks until this specific subagent is done. Since
            # all four were already submitted above, this loop is just
            # collecting results as they finish, not waiting for them to
            # start.
            results[dimension] = future.result()
            print(f"  {dimension} done")

    print("\nAll 4 subagents completed\n")

    print("=" * 80)
    print("STEP 1 OUTPUT - Raw Subagent Results (preview)")
    print("=" * 80)

    for dimension, result in results.items():
        print(f"\n{dimension.upper()}:")
        print(json.dumps(result, indent=2)[:500])

    print("\n" + "=" * 80)
    print("STEP 2: Coordinator Synthesizing Final Report")
    print("=" * 80)

    # Coordinator only runs after every subagent has returned, since it
    # needs all four reports at once. It receives results exactly as the
    # subagents produced it, error dicts and all.
    final_report = coordinator_synthesis(results)

    print("\nSynthesis complete\n")
    print("=" * 80)
    print("FINAL REPORT")
    print("=" * 80)
    print(json.dumps(final_report, indent=2))

    print("\n" + "=" * 80)
    print("STEP 3: Generating Clinical Report")
    print("=" * 80)

    # From here down, no more API calls happen. Both report functions are
    # pure formatting, reading final_report and results and producing text.
    clinical_report = generate_clinical_report(final_report, results)

    output_filename = save_report_to_file(clinical_report)

    print(f"\nClinical report saved to: {output_filename}")

    html_report = generate_html_report(final_report, results)

    html_output_filename = save_html_report_to_file(html_report)

    print(f"HTML clinical report saved to: {html_output_filename}")


    print("\n" + "=" * 80)
    print("Complete Pipeline Finished Successfully")
    print("=" * 80)