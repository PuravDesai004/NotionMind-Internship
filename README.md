# Multi Agent Healthcare Analytics System

An AI system that turns a raw telehealth CSV into a clinic ready report. Point it at patient data and it produces a prioritized, plain English summary of program performance, patient risk, and retention patterns, with zero human input needed once it starts running.

Built during a five week internship at Notionmind.

## What it does

The system reads a CSV of telehealth patient records and produces two finished reports:

- `clinical_report.md`, a markdown report
- `clinical_report.html`, a branded HTML report with two inline charts

Both reports contain the same content: an executive summary, a breakdown by program performance, patient segmentation, retention patterns, and anomaly detection, followed by ranked recommendations and cross cutting insights that connect findings across all four areas.

The target reader is a clinic director with no data science background. The reports use plain language, call out real numbers with context, and avoid technical jargon entirely.

## How it works, briefly

The system runs in three layers.

Four subagents analyze the dataset in parallel, each one responsible for a single dimension, program performance, patient segmentation, retention, or anomaly detection. Each subagent calls a shared set of analysis tools to get real numbers rather than being given the dataset directly.

A coordinator agent then reads all four subagents' findings and merges them into one unified report. It does not run any new analysis of its own, it only combines, resolves conflicts, and ranks recommendations.

A report generator, which is plain Python with no AI calls at all, turns the coordinator's output into the two finished report files.

See `TECHNICAL_WRITEUP.md` for the full reasoning behind this design and the testing that shaped it.

## Requirements

- Python 3.10 or later
- An Anthropic API key

Install dependencies:

```
pip install anthropic pandas python-dotenv
```

## Setup

1. Place your dataset as `telehealth.csv` in the same folder as the script. The dataset must contain these exact columns: `patient_id`, `program_type`, `start_date`, `treatment_duration_weeks`, `retention_status`, `drop_off_reason`. See Known Limitations below for why this matters.

2. Create a `.env` file in the same folder containing your API key:

```
ANTHROPIC_API_KEY=your_actual_api_key_here
```

## Running it

```
python agents_complete.py
```

The pipeline runs fully non interactively, no prompts or input required once it starts. A full run takes roughly 20 seconds and prints progress for each step as it completes. When it finishes, `clinical_report.md` and `clinical_report.html` will be in the same folder.

## File structure

```
agents_complete.py                   the pipeline: tools, subagents, coordinator, error handling
report_generator.py                  markdown and HTML report builders, inline SVG charts
telehealth.csv                       input dataset
.env                                 API key, not committed to version control
clinical_report.md                   generated output
clinical_report.html                 generated output
TECHNICAL_WRITEUP.md                 architecture decisions and testing history
```

## Component responsibilities

### `agents_complete.py`

This is the whole pipeline in one file.

**Analysis functions** (`get_df_info`, `run_cohort_analysis`, `run_outcome_analysis`, `flag_anomalies`) do the actual math against the dataframe using pandas. Each one processes one program at a time and isolates failures per program, so one corrupted program's data does not stop the other programs from computing correctly in the same run.

**Chunking** (`chunk_dict_by_size`, `_prepare_analysis_response`) splits large per-program results into smaller pieces so no single tool response is too big for the model to handle in one go. Tested against a synthetic 40 program dataset with no data lost across chunks.

**Error handling** (`_classify_error`, `run_tool_safe`) wraps every tool call in a consistent envelope. On failure it reports a category, whether retrying is worth it, and retries once with a short pause before giving up for good.

**`subagent_runner`** runs a single subagent through the full tool calling loop until it returns a final structured report.

**`coordinator_synthesis`** takes all four subagent reports and produces the unified summary.

**The `if __name__ == "__main__":` block** at the bottom is what actually executes the pipeline: runs all four subagents in parallel, synthesizes the results, and generates both report files.

### `report_generator.py`

Pure formatting layer. Takes the coordinator's JSON and the four subagents' JSON as input and produces the two output files. Makes no API calls, never touches the dataframe, never calls a tool. `generate_html_report` also builds the two charts as inline SVG generated directly in Python, so the HTML report has no external dependencies and renders identically whether it is opened online, offline, or as an email attachment.

## Known limitations

The four analysis tools currently expect exact column names (`program_type`, `treatment_duration_weeks`, `retention_status`). A dataset with the same kind of information under different column headers will fail. This was a deliberate tradeoff made to move quickly against a known dataset shape, not an oversight. The planned fix is to use `get_df_info`'s column list to map whatever column names actually exist to the roles the analysis functions need, before running any analysis.

## License

Internal project, built for Notionmind.