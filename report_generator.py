from datetime import datetime

def generate_clinical_report(coordinator_synthesis_output, subagent_results):

    synthesis = coordinator_synthesis_output

    report = []
    report.append("# Clinical Insights Report")
    report.append("")
    report.append(f"Generated: {datetime.now().strftime('%B %d, %Y at %H:%M')}")
    report.append("")
    report.append("")

    report.append("## Executive Summary")
    report.append("")
    if "executive_summary" in synthesis:
        report.append(synthesis["executive_summary"])
    report.append("")
    report.append("")

    report.append("## Program Performance Analysis")
    report.append("")
    perf = subagent_results.get("program_performance", {})
    if isinstance(perf, dict):
        if "overall_summary" in perf:
            report.append(perf["overall_summary"])
            report.append("")
        if "high_attention_programs" in perf:
            report.append("**Priority Programs**")
            report.append("")
            for prog in perf.get("high_attention_programs", []):
                report.append(f"* {prog.get('program', 'Unknown')}: {prog.get('priority', 'Medium')} priority")
                for reason in prog.get("reasons", []):
                    report.append(f"  - {reason}")
            report.append("")
        if "program_patterns" in perf:
            report.append("**Key Patterns**")
            report.append("")
            for pattern in perf.get("program_patterns", []):
                report.append(f"* {pattern.get('pattern', 'Unknown pattern')}")
                report.append(f"  Evidence: {pattern.get('evidence', 'No evidence provided')}")
            report.append("")
    report.append("")

    report.append("## Patient Segmentation Analysis")
    report.append("")
    segment = subagent_results.get("patient_segmentation", {})
    if isinstance(segment, dict):
        if "overall_summary" in segment:
            report.append(segment["overall_summary"])
            report.append("")
        if "program_patterns" in segment:
            report.append("**Patient Segments Identified**")
            report.append("")
            for pattern in segment.get("program_patterns", []):
                report.append(f"* {pattern.get('pattern', 'Unknown segment')}")
                report.append(f"  {pattern.get('evidence', '')}")
            report.append("")
    report.append("")

    report.append("## Retention and Drop-Off Analysis")
    report.append("")
    retention = subagent_results.get("retention_analysis", {})
    if isinstance(retention, dict):
        if "overall_summary" in retention:
            report.append(retention["overall_summary"])
            report.append("")

        duration_data = retention.get("duration_and_dropoff_by_program", {})
        if isinstance(duration_data, dict) and duration_data:
            report.append("**Treatment Duration Trends**")
            report.append("")
            for program, stats in duration_data.items():
                if isinstance(stats, dict):
                    trends = stats.get("duration_trends", {})
                    report.append(f"* {program}")
                    report.append(
                        f"  Mean: {trends.get('mean_weeks', 'N/A')} weeks, "
                        f"Median: {trends.get('median_weeks', 'N/A')} weeks, "
                        f"Q1: {trends.get('q1_weeks', 'N/A')} weeks, "
                        f"Q3: {trends.get('q3_weeks', 'N/A')} weeks"
                    )
            report.append("")
            report.append("**Drop-Off Timing by Stage**")
            report.append("")
            for program, stats in duration_data.items():
                if isinstance(stats, dict):
                    counts = stats.get("drop_off_points", {})
                    report.append(f"* {program}")
                    early = counts.get("early_stage_patients", 0)
                    mid = counts.get("mid_stage_patients", 0)
                    late = counts.get("late_stage_patients", 0)
                    report.append(f"  Early stage: {early} patients, Mid stage: {mid} patients, Late stage: {late} patients")
            report.append("")
    report.append("")

    report.append("## Anomalies and Risk Factors")
    report.append("")
    anomalies = subagent_results.get("anomaly_detection", {})
    if isinstance(anomalies, dict):
        if "overall_summary" in anomalies:
            report.append(anomalies["overall_summary"])
            report.append("")
        if "common_risk_factors" in anomalies:
            report.append("**Risk Factors Identified**")
            report.append("")
            for risk in anomalies.get("common_risk_factors", []):
                report.append(f"* {risk.get('factor', 'Unknown risk')}")
                report.append(f"  Frequency: {risk.get('frequency', 'Unknown')}")
                report.append(f"  Affected programs: {', '.join(risk.get('affected_programs', []))}")
            report.append("")
        if "key_concerns" in anomalies:
            report.append("**Key Concerns**")
            report.append("")
            for concern in anomalies.get("key_concerns", []):
                report.append(f"* {concern}")
            report.append("")
    report.append("")

    report.append("## Top Priority Recommendations")
    report.append("")
    if "top_priority_recommendations" in synthesis:
        for rec in synthesis.get("top_priority_recommendations", []):
            report.append(f"* {rec}")
        report.append("")
    report.append("")

    report.append("## Cross-Cutting Insights")
    report.append("")
    if "cross_cutting_insights" in synthesis:
        for insight in synthesis.get("cross_cutting_insights", []):
            report.append(f"* {insight}")
    report.append("")

    report.append("")
    report.append("---")
    report.append("")
    report.append(f"Report generated by Multi-Agent Healthcare Analytics System on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    return "\n".join(report)


def save_report_to_file(report_text, filename="clinical_report.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_text)
    return filename


def _escape_html(text):
    if text is None:
        return ""
    text = str(text)
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    return text


def generate_html_report(coordinator_synthesis_output, subagent_results):

    synthesis = coordinator_synthesis_output
    generated_at = datetime.now().strftime('%B %d, %Y at %H:%M')

    parts = []

    parts.append(f"<div class='wordmark'><span class='wm-light'>NOTIO</span><span class='wm-dark'>NMIND</span><sup>&reg;</sup></div>")
    parts.append(f"<h1>Clinical Insights Report</h1>")
    parts.append(f"<p class='meta'>Generated {generated_at}</p>")

    parts.append("<h2>Executive Summary</h2>")
    parts.append(f"<p>{_escape_html(synthesis.get('executive_summary', ''))}</p>")

    perf = subagent_results.get("program_performance", {})
    if isinstance(perf, dict):
        parts.append("<h2>Program Performance Analysis</h2>")
        parts.append(f"<p>{_escape_html(perf.get('overall_summary', ''))}</p>")
        if perf.get("high_attention_programs"):
            parts.append("<h3>Priority Programs</h3>")
            parts.append("<ul>")
            for prog in perf.get("high_attention_programs", []):
                parts.append(f"<li><strong>{_escape_html(prog.get('program', 'Unknown'))}</strong>: {_escape_html(prog.get('priority', 'Medium'))} priority")
                reasons = prog.get("reasons", [])
                if reasons:
                    parts.append("<ul>")
                    for reason in reasons:
                        parts.append(f"<li>{_escape_html(reason)}</li>")
                    parts.append("</ul>")
                parts.append("</li>")
            parts.append("</ul>")
        if perf.get("program_patterns"):
            parts.append("<h3>Key Patterns</h3>")
            parts.append("<ul>")
            for pattern in perf.get("program_patterns", []):
                parts.append(f"<li>{_escape_html(pattern.get('pattern', ''))} &mdash; {_escape_html(pattern.get('evidence', ''))}</li>")
            parts.append("</ul>")

    segment = subagent_results.get("patient_segmentation", {})
    if isinstance(segment, dict):
        parts.append("<h2>Patient Segmentation Analysis</h2>")
        parts.append(f"<p>{_escape_html(segment.get('overall_summary', ''))}</p>")
        if segment.get("program_patterns"):
            parts.append("<h3>Patient Segments Identified</h3>")
            parts.append("<ul>")
            for pattern in segment.get("program_patterns", []):
                parts.append(f"<li>{_escape_html(pattern.get('pattern', ''))} &mdash; {_escape_html(pattern.get('evidence', ''))}</li>")
            parts.append("</ul>")

    retention = subagent_results.get("retention_analysis", {})
    if isinstance(retention, dict):
        parts.append("<h2>Retention and Drop-Off Analysis</h2>")
        parts.append(f"<p>{_escape_html(retention.get('overall_summary', ''))}</p>")
        duration_data = retention.get("duration_and_dropoff_by_program", {})
        if isinstance(duration_data, dict) and duration_data:
            parts.append("<h3>Treatment Duration Trends</h3>")
            parts.append("<ul>")
            for program, stats in duration_data.items():
                if isinstance(stats, dict):
                    trends = stats.get("duration_trends", {})
                    parts.append(
                        f"<li><strong>{_escape_html(program)}</strong>: "
                        f"Mean {_escape_html(trends.get('mean_weeks', 'N/A'))} weeks, "
                        f"Median {_escape_html(trends.get('median_weeks', 'N/A'))} weeks, "
                        f"Q1 {_escape_html(trends.get('q1_weeks', 'N/A'))} weeks, "
                        f"Q3 {_escape_html(trends.get('q3_weeks', 'N/A'))} weeks</li>"
                    )
            parts.append("</ul>")
            parts.append("<h3>Drop-Off Timing by Stage</h3>")
            parts.append("<ul>")
            for program, stats in duration_data.items():
                if isinstance(stats, dict):
                    counts = stats.get("drop_off_points", {})
                    parts.append(
                        f"<li><strong>{_escape_html(program)}</strong>: "
                        f"Early {_escape_html(counts.get('early_stage_patients', 0))}, "
                        f"Mid {_escape_html(counts.get('mid_stage_patients', 0))}, "
                        f"Late {_escape_html(counts.get('late_stage_patients', 0))}</li>"
                    )
            parts.append("</ul>")

    anomalies = subagent_results.get("anomaly_detection", {})
    if isinstance(anomalies, dict):
        parts.append("<h2>Anomalies and Risk Factors</h2>")
        parts.append(f"<p>{_escape_html(anomalies.get('overall_summary', ''))}</p>")
        if anomalies.get("common_risk_factors"):
            parts.append("<h3>Risk Factors Identified</h3>")
            parts.append("<ul>")
            for risk in anomalies.get("common_risk_factors", []):
                affected = ", ".join(risk.get("affected_programs", []))
                parts.append(f"<li>{_escape_html(risk.get('factor', ''))} &mdash; Frequency: {_escape_html(risk.get('frequency', ''))}, Affected: {_escape_html(affected)}</li>")
            parts.append("</ul>")
        if anomalies.get("key_concerns"):
            parts.append("<h3>Key Concerns</h3>")
            parts.append("<ul>")
            for concern in anomalies.get("key_concerns", []):
                parts.append(f"<li>{_escape_html(concern)}</li>")
            parts.append("</ul>")

    if synthesis.get("top_priority_recommendations"):
        parts.append("<h2>Top Priority Recommendations</h2>")
        parts.append("<ol>")
        for rec in synthesis.get("top_priority_recommendations", []):
            parts.append(f"<li>{_escape_html(rec)}</li>")
        parts.append("</ol>")

    if synthesis.get("cross_cutting_insights"):
        parts.append("<h2>Cross-Cutting Insights</h2>")
        parts.append("<ul>")
        for insight in synthesis.get("cross_cutting_insights", []):
            parts.append(f"<li>{_escape_html(insight)}</li>")
        parts.append("</ul>")

    parts.append(f"<hr><p class='meta'>Report generated by Multi-Agent Healthcare Analytics System &middot; {generated_at}</p>")

    body = "\n".join(parts)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Clinical Insights Report</title>
<style>
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1a1d29;
    max-width: 720px;
    margin: 40px auto;
    padding: 0 20px;
    line-height: 1.6;
  }}
  .wordmark {{
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 0.02em;
    margin-bottom: 18px;
  }}
  .wm-light {{ color: #2f80ed; }}
  .wm-dark {{ color: #16337a; }}
  h1 {{
    color: #16337a;
    border-bottom: 2px solid #2f80ed;
    padding-bottom: 10px;
  }}
  h2 {{
    color: #16337a;
    margin-top: 32px;
  }}
  h3 {{
    color: #0f766e;
    margin-top: 20px;
  }}
  p, li {{
    color: #1a1d29;
  }}
  .meta {{
    color: #5a6072;
    font-size: 14px;
  }}
  hr {{
    border: none;
    border-top: 1px solid #ddd;
    margin-top: 32px;
  }}
</style>
</head>
<body>
{body}
</body>
</html>"""

    return html


def save_html_report_to_file(html_text, filename="clinical_report.html"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_text)
    return filename