# Project Context: Multi-Agent Healthcare Analytics System

## Overview

This project implements a two-layer multi-agent system that analyzes telehealth patient data. A coordinator agent delegates analysis to four specialized subagents, which call data processing tools and return structured findings. The coordinator synthesizes all findings into a unified report, which is converted to a clinical markdown report for clinic leadership.

## Dataset

telehealth.csv contains patient records tracking programs, enrollment, treatment progression, and retention outcomes. The system is dataset-agnostic and works with any telehealth data that tracks patient journeys across programs.

## Architecture

Layer 1: Four Specialized Subagents

Each subagent analyzes one dimension:

program_performance: Program-level metrics, rankings, and comparisons
patient_segmentation: Patient grouping, segment characteristics, risk identification
retention_analysis: Treatment duration, drop-off timing, retention trends
anomaly_detection: Statistical outliers, risk thresholds, anomalies

Each subagent calls available analysis tools and returns structured JSON findings. All four run in parallel.

Layer 2: Coordinator Agent

Synthesizes all four subagent outputs into one unified report. Resolves conflicts, identifies cross-cutting themes, prioritizes recommendations.

Layer 3: Report Generator

Converts JSON findings to markdown format for clinic leadership. Produces clinical_report.md with plain language and no technical jargon.

## Code Organization

### Data Processing Files

When modifying tools or analysis functions:

1. All tools return structured JSON only. No exceptions that crash the pipeline. Errors are wrapped in JSON.

2. Tools are pure functions: given the same input, they return identical output. Temperature is 0 for all LLM calls.

3. All numeric calculations include error handling. No assumptions about data format or completeness.

4. Tool outputs are wrapped in tool_result blocks before passing to Claude. Raw data never passes directly.

5. Tool descriptions must be unambiguous. Each tool clearly states what it returns and what it does NOT return.

### Report Generation Files

When modifying report generation code:

1. Output format is markdown only. No HTML, PDF, or mixed formats.

2. Executive summary appears first, before all other sections. This is the most important section for clinic leadership.

3. Report sections are fixed and consistent: Overview, Program Analysis, Patient Segments, Retention Analysis, Anomalies, Recommendations, Cross-Cutting Insights.

4. All numbers come directly from JSON outputs. No calculations, estimates, or inferences. Every number is accompanied by what it means in plain language.

5. Language is plain English, zero technical jargon. Target: clinic director with no data science background can read and understand in under 10 minutes.

6. Recommendations are specific and actionable. Not: improve retention. Instead: implement specific intervention for specific program to address specific problem.

7. Timestamps use readable format: Month Day, Year at HH:MM. Not ISO 8601.

### Subagent System Prompts

When modifying subagent prompts:

1. All subagents share base system prompt defining role and guardrails. This never changes.

2. Each subagent receives base prompt plus dimension-specific task prompt. Tasks are specific and non-overlapping.

3. Subagent prompts explicitly state which tools to call and in what order. Without this, subagents may skip data-gathering steps.

4. Output schema is specified in task prompt. Subagents must know exact JSON structure expected.

5. Nothing is assumed. If it is not in the prompt, the subagent does not know about it.

### Coordinator Synthesis

When modifying coordinator:

1. Coordinator does NOT perform new analysis. It only synthesizes, merges, and prioritizes.

2. Conflicts between subagents are resolved by preferring the more conservative, data-supported figure.

3. Cross-cutting themes are identified: patterns appearing across multiple subagents.

4. Recommendations are deduplicated: similar actions suggested by different subagents are merged.

5. Output is valid JSON with temperature 0. Output structure is fixed and consistent.

## Execution Instructions

### Non-Interactive Execution (Production Mode)

This is standard execution for automation.

Command:

claude-code run -p agents_complete_with_report.py

The -p flag means production mode. Claude Code reads this CLAUDE.md file, executes the pipeline non-interactively from start to finish, and generates clinical_report.md.

Expected duration: 60 to 120 seconds depending on API latency.

### Interactive Execution (Development)

For debugging and testing:

python agents_complete_with_report.py

Same output as production mode but allows detailed console inspection.

### Output Files

Pipeline generates:

clinical_report.md: Professional markdown report in project folder

Console output shows progress through three steps:
- Step 1: Four subagents running in parallel
- Step 2: Coordinator synthesis
- Step 3: Report generation

## Project Rules Summary

RULES FOR DATA PROCESSING:
- Tools return JSON only
- All calculations are error-handled
- Outputs are deterministic
- Tools never receive raw message content
- Errors are wrapped in JSON structures

RULES FOR REPORT GENERATION:
- Markdown format only
- Executive summary first
- Fixed section order and structure
- All numbers from JSON only
- Plain English, zero jargon
- Specific, actionable recommendations

RULES FOR EXECUTION:
- Non-interactive mode is standard
- No human input prompts mid-run
- Temperature 0 for determinism
- All subagents run in parallel
- Coordinator runs after subagents complete
- Report generator runs after synthesis

## Important Notes

Do not modify execution flow to add interactive elements. System is designed for batch processing.

Do not add new tools without updating descriptions and maintaining JSON output standard.

Do not change report section order or structure without reviewing impact on readability.

Do not pass raw data to Claude. Always wrap in tool_result blocks.

All tool outputs are wrapped in structured JSON before being passed to Claude via tool_result blocks. Claude never sees raw dataframe content. This isolation is critical for security and data integrity.

The system has been tested with multiple failure scenarios and documented in COMPLETE_BREAKING_EXERCISE_DOCUMENTATION.md.