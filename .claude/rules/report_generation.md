---
paths:
  - "report_generator.py"
---

# Report Generation Rules

When modifying report generation code in this file:

1. Output format is markdown only.
2. Executive summary comes first, before all other sections.
3. Section order is fixed: Executive Summary, Program Performance, Patient Segmentation, Retention Analysis, Anomalies and Risk Factors, Recommendations, Cross-Cutting Insights.
4. Every number in the report comes directly from the JSON inputs. No new calculations or estimates.
5. Language is plain English with zero technical jargon. A clinic director with no data background must be able to read and understand it.
6. Recommendations are specific and actionable, not generic advice.
7. File writes use encoding="utf-8" to avoid Windows encoding errors.