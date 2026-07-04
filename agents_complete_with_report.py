from anthropic import Anthropic
from dotenv import load_dotenv
import pandas as pd
import os
import json
import concurrent.futures
from report_generator import generate_clinical_report, save_report_to_file

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=api_key)
model = "claude-sonnet-5"

df = pd.read_csv(r"telehealth.csv")

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
    result = {}
    for program, group in df.groupby("program_type"):
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
    return result

def run_outcome_analysis(df):
    result = {}
    for program, group in df.groupby("program_type"):
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
    return result

def flag_anomalies(df):
    result = {}
    for program, group in df.groupby("program_type"):
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
    return result

def run_tool(tool_name, tool_input):
    if tool_name == "get_df_info":
        return get_df_info()
    elif tool_name == "run_cohort_analysis":
        return run_cohort_analysis(df)
    elif tool_name == "run_outcome_analysis":
        return run_outcome_analysis(df)
    elif tool_name == "flag_anomalies":
        return flag_anomalies(df)
    raise ValueError(f"Unknown tool: {tool_name}")

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
        "description": "Returns a point-in-time snapshot per program for side-by-side comparison: patient counts and retention percentage. Use for ranking or comparing programs against each other, including ranking by churn or retention. Does not analyze drop-off timing or flag statistical risk. For timing use run_outcome_analysis, for risk thresholds use flag_anomalies.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "run_outcome_analysis",
        "description": "Returns time-based behavior per program: how treatment length is distributed, and which stage (early, mid, late) churned patients left at. Use for understanding when or at what point in treatment patients drop off. Does not rank programs against each other or flag statistical risk. For ranking use run_cohort_analysis, for risk thresholds use flag_anomalies.",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "flag_anomalies",
        "description": "Returns statistical risk flags per program: treatment durations that are extreme outliers (IQR method) and churn rates exceeding a 25% threshold. Use for risk detection or exception flagging, not raw counts or timing. Does not provide patient counts or drop-off timing. For counts use run_cohort_analysis, for timing use run_outcome_analysis.",
        "input_schema": {
            "type": "object",
            "properties": {},
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

Return this exact JSON structure:
""" + output_schema,

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
    system = f"{system_prompt}\n\n{dimension_addition}"

    messages = [
        {"role": "user", "content": f"Begin your analysis for: {dimension_name}"}
    ]

    while True:
        response = client.messages.create(
            model=model,
            max_tokens=8000,
            system=system,
            tools=tools,
            messages=messages
        )

        if response.stop_reason != "tool_use":
            final_text = ""
            for block in response.content:
                if hasattr(block, 'text'):
                    final_text += block.text

            final_text = final_text.replace("```json", "").replace("```", "").strip()
            json_start = final_text.find('{')
            if json_start != -1:
                final_text = final_text[json_start:]

            try:
                return json.loads(final_text)
            except json.JSONDecodeError:
                return {"error": "Failed to parse response", "raw": final_text[:500]}

        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                try:
                    result = run_tool(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps(result, default=str)
                    })
                except Exception as e:
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps({"error": str(e)}),
                        "is_error": True
                    })

        messages.append({"role": "user", "content": tool_results})

def coordinator_synthesis(results):
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
        return {"error": "Synthesis API call failed", "details": str(e)}

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
        return {"error": "Failed to parse synthesis", "raw": raw_text[:1000]}

print("=" * 80)
print("STEP 1: Running 4 Subagents in PARALLEL (ThreadPoolExecutor)")
print("=" * 80)

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    futures = {
        dimension: executor.submit(subagent_runner, dimension, addition)
        for dimension, addition in subagent_prompts.items()
    }

    results = {}
    for dimension, future in futures.items():
        print(f"  Waiting for {dimension}...")
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

final_report = coordinator_synthesis(results)

print("\nSynthesis complete\n")
print("=" * 80)
print("FINAL REPORT")
print("=" * 80)
print(json.dumps(final_report, indent=2))

print("\n" + "=" * 80)
print("STEP 3: Generating Clinical Report")
print("=" * 80)

clinical_report = generate_clinical_report(final_report, results)

output_filename = save_report_to_file(clinical_report)

print(f"\nClinical report saved to: {output_filename}")

print("\n" + "=" * 80)
print("Complete Pipeline Finished Successfully")
print("=" * 80)