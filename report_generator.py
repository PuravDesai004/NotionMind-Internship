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
        if "duration_trends" in retention:
            report.append("**Treatment Duration Trends**")
            report.append("")
            trends = retention.get("duration_trends", {})
            for program, stats in trends.items():
                if isinstance(stats, dict):
                    report.append(f"* {program}")
                    report.append(f"  Mean: {stats.get('mean_weeks', 'N/A')} weeks, Median: {stats.get('median_weeks', 'N/A')} weeks")
            report.append("")
        if "drop_off_points" in retention:
            report.append("**Drop-Off Timing by Stage**")
            report.append("")
            dropoff = retention.get("drop_off_points", {})
            for program, counts in dropoff.items():
                if isinstance(counts, dict):
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