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


def _badge_html(priority):
    p = str(priority).strip().lower()
    if p == "high":
        color = "#b91c1c"
        bg = "#fde8e8"
    elif p == "low":
        color = "#166534"
        bg = "#e6f7ec"
    else:
        color = "#92400e"
        bg = "#fef3d9"
    label = _escape_html(priority) if priority else "Medium"
    return f"<span class='badge' style='color:{color};background:{bg};'>{label}</span>"


def _bar_chart_svg(labels, values, color, max_value=None, width=600, height=220, value_suffix=""):
    if not labels:
        return ""

    if max_value is None:
        max_value = max(values) if values else 1
    if max_value <= 0:
        max_value = 1

    top_pad = 28
    bottom_pad = 28
    plot_h = height - top_pad - bottom_pad

    n = len(labels)
    slot_w = width / n
    bar_w = slot_w * 0.6

    bars = []
    for i in range(n):
        label = labels[i]
        value = values[i]
        bar_h = (value / max_value) * plot_h
        x = i * slot_w + (slot_w - bar_w) / 2
        y = top_pad + (plot_h - bar_h)

        bars.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" fill="{color}" rx="4"></rect>')
        bars.append(f'<text x="{x + bar_w / 2:.1f}" y="{y - 6:.1f}" text-anchor="middle" font-size="12" font-weight="700" fill="#1a1d29">{value:g}{value_suffix}</text>')
        bars.append(f'<text x="{x + bar_w / 2:.1f}" y="{height - 8:.1f}" text-anchor="middle" font-size="12" fill="#5a6072">{_escape_html(label)}</text>')

    baseline_y = top_pad + plot_h

    svg = (
        f'<svg viewBox="0 0 {width} {height}" width="100%" height="{height}" role="img" '
        f'aria-label="Bar chart">'
        f'<line x1="0" y1="{baseline_y:.1f}" x2="{width}" y2="{baseline_y:.1f}" stroke="#e2e4ea" stroke-width="1"></line>'
        f'{"".join(bars)}'
        f'</svg>'
    )
    return svg


def _stacked_bar_chart_svg(labels, series, width=600, height=240):
    if not labels:
        return ""

    totals = [sum(values[i] for _, _, values in series) for i in range(len(labels))]
    max_total = max(totals) if totals else 1
    if max_total <= 0:
        max_total = 1

    top_pad = 20
    bottom_pad = 28
    legend_h = 24
    plot_h = height - top_pad - bottom_pad - legend_h

    n = len(labels)
    slot_w = width / n
    bar_w = slot_w * 0.6

    bars = []
    for i in range(n):
        label = labels[i]
        x = i * slot_w + (slot_w - bar_w) / 2
        cursor_y = top_pad + plot_h

        for name, color, values in series:
            v = values[i]
            seg_h = (v / max_total) * plot_h
            if seg_h > 0:
                y = cursor_y - seg_h
                bars.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{seg_h:.1f}" fill="{color}"></rect>')
                if seg_h > 14:
                    bars.append(f'<text x="{x + bar_w / 2:.1f}" y="{y + seg_h / 2 + 4:.1f}" text-anchor="middle" font-size="11" fill="#ffffff">{v:g}</text>')
                cursor_y = y

        bars.append(f'<text x="{x + bar_w / 2:.1f}" y="{top_pad + plot_h + 20:.1f}" text-anchor="middle" font-size="12" fill="#5a6072">{_escape_html(label)}</text>')

    baseline_y = top_pad + plot_h

    legend_items = []
    lx = 0
    ly = height - legend_h + 10
    for name, color, _ in series:
        legend_items.append(f'<rect x="{lx}" y="{ly - 10}" width="10" height="10" fill="{color}"></rect>')
        legend_items.append(f'<text x="{lx + 14}" y="{ly - 1}" font-size="11" fill="#5a6072">{_escape_html(name)}</text>')
        lx += 14 + len(name) * 6 + 24

    svg = (
        f'<svg viewBox="0 0 {width} {height}" width="100%" height="{height}" role="img" '
        f'aria-label="Stacked bar chart">'
        f'<line x1="0" y1="{baseline_y:.1f}" x2="{width}" y2="{baseline_y:.1f}" stroke="#e2e4ea" stroke-width="1"></line>'
        f'{"".join(bars)}'
        f'{"".join(legend_items)}'
        f'</svg>'
    )
    return svg


def generate_html_report(coordinator_synthesis_output, subagent_results):

    synthesis = coordinator_synthesis_output
    generated_at = datetime.now().strftime('%B %d, %Y at %H:%M')

    retention = subagent_results.get("retention_analysis", {})
    duration_data = retention.get("duration_and_dropoff_by_program", {}) if isinstance(retention, dict) else {}

    chart_programs = []
    chart_retention = []
    chart_early = []
    chart_mid = []
    chart_late = []
    if isinstance(duration_data, dict):
        for program, stats in duration_data.items():
            if isinstance(stats, dict):
                chart_programs.append(program)
                chart_retention.append(stats.get("retention_rate_percent", 0))
                counts = stats.get("drop_off_points", {})
                chart_early.append(counts.get("early_stage_patients", 0))
                chart_mid.append(counts.get("mid_stage_patients", 0))
                chart_late.append(counts.get("late_stage_patients", 0))

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
                badge = _badge_html(prog.get('priority', 'Medium'))
                parts.append(f"<li><strong>{_escape_html(prog.get('program', 'Unknown'))}</strong> {badge}")
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

    if isinstance(retention, dict):
        parts.append("<h2>Retention and Drop-Off Analysis</h2>")
        parts.append(f"<p>{_escape_html(retention.get('overall_summary', ''))}</p>")

        if chart_programs:
            retention_svg = _bar_chart_svg(chart_programs, chart_retention, "#0887FF", max_value=100, value_suffix="%")
            dropoff_svg = _stacked_bar_chart_svg(chart_programs, [
                ("Early Stage", "#0887FF", chart_early),
                ("Mid Stage", "#103FB8", chart_mid),
                ("Late Stage", "#0f766e", chart_late),
            ])
            parts.append("<h3>Retention Rate by Program</h3>")
            parts.append(f"<div class='chart'>{retention_svg}</div>")
            parts.append("<h3>Drop-Off Stage by Program</h3>")
            parts.append(f"<div class='chart'>{dropoff_svg}</div>")

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
  .wm-light {{ color: #0887FF; }}
  .wm-dark {{ color: #103FB8; }}
  h1 {{
    color: #103FB8;
    border-bottom: 2px solid #0887FF;
    padding-bottom: 10px;
  }}
  h2 {{
    color: #103FB8;
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
  .badge {{
    display: inline-block;
    font-size: 12px;
    font-weight: 700;
    padding: 2px 10px;
    border-radius: 999px;
    margin-left: 6px;
  }}
  .chart {{
    margin: 12px 0 24px;
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