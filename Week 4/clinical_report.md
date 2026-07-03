# Clinical Insights Report

Generated: July 03, 2026 at 15:51


## Executive Summary

Across 300 patients in three programs, the clinic's overall churn rate is approximately 26%, marginally above the 25% risk threshold. Testosterone (112 patients) is the highest-priority program with the lowest retention rate (71.43%), the highest absolute churn count (32 patients), and a churn rate of 28.57% flagged by anomaly detection. Peptides (91 patients) is a secondary concern with a flagged churn rate of 26.37% and the shortest average treatment duration (10.31 weeks). Weight Loss (97 patients) is the strongest performer at 77.32% retention and is the only program below the risk threshold. Universally, churn is concentrated in the early and mid stages of treatment — no late-stage drop-offs were recorded in any program — making the early-to-mid treatment window the most critical retention period clinic-wide.


## Program Performance Analysis

The dataset contains 300 patients across 3 programs: Peptides (91 patients), Testosterone (112 patients), and Weight Loss (97 patients). Each record includes treatment duration in weeks, retention status (Active, Completed, or Churned), and drop-off reason. Across all programs, 78 out of 300 patients churned, yielding an overall churn rate of approximately 26%. Retention rates range from 71.43% to 77.32%, indicating moderate but uneven retention performance across programs.

**Priority Programs**

* Testosterone: High priority
  - Lowest retention rate at 71.43% across all programs
  - Highest absolute churn count with 32 patients lost
  - Churn rate of 28.57% exceeds the 25% risk threshold
  - Largest enrolled program (112 patients), meaning churn has the greatest overall impact
* Peptides: Medium priority
  - Churn rate of 26.37% marginally exceeds the 25% risk threshold
  - Shortest average treatment duration at 10.31 weeks, suggesting patients may be disengaging early
  - 24 churned patients out of 91 enrolled
* Weight Loss: Low priority
  - Best retention rate at 77.32%
  - Lowest churn count at 22 patients
  - Churn rate of 22.68% remains below the 25% risk threshold

**Key Patterns**

* Testosterone has the highest enrollment but the lowest retention rate
  Evidence: Testosterone enrolled 112 patients (37.3% of total), yet holds the lowest retention rate at 71.43% with 32 churned patients — the highest absolute churn count across all programs.
* Weight Loss leads in retention despite mid-tier enrollment
  Evidence: Weight Loss enrolled 97 patients and achieved the highest retention rate at 77.32%, with only 22 churned patients — the lowest churn count of all three programs.
* Peptides has the shortest average treatment duration by a wide margin
  Evidence: Peptides averages only 10.31 weeks of treatment, compared to 16.47 weeks for Weight Loss and 28.22 weeks for Testosterone — less than half the duration of Weight Loss and less than 37% of Testosterone's average.
* Testosterone has significantly longer average treatment duration than other programs
  Evidence: Testosterone's average treatment duration is 28.22 weeks, which is 1.71x longer than Weight Loss (16.47 weeks) and 2.74x longer than Peptides (10.31 weeks).


## Patient Segmentation Analysis

The dataset contains 300 patients across 3 program types: Peptides (91 patients), Testosterone (112 patients), and Weight Loss (97 patients). Overall retention across all programs averages approximately 74%, with churn ranging from 22.68% to 28.57%. No late-stage drop-offs were recorded in any program. Early-stage drop-off is the dominant churn pattern across all three segments. Two of three programs (Peptides and Testosterone) have been statistically flagged for high churn rates exceeding the 25% threshold.

**Patient Segments Identified**

* Early-stage drop-off is the dominant churn pattern across all programs
  Peptides: 16 early vs. 8 mid drop-offs. Testosterone: 18 early vs. 14 mid drop-offs. Weight Loss: 11 early vs. 11 mid drop-offs. No program recorded any late-stage drop-offs.
* No late-stage churn exists in any program
  All three programs returned 0 late-stage drop-off patients, meaning patients who stay past the mid-stage tend to complete or remain active.
* Testosterone has the widest treatment duration spread, indicating high variability in patient engagement length
  Testosterone Q1 is 14 weeks and Q3 is 46 weeks — a 32-week interquartile range. By comparison, Peptides IQR is 11 weeks (Q1: 5, Q3: 16) and Weight Loss IQR is 17 weeks (Q1: 9, Q3: 26).
* Weight Loss is the only program with an even split between early and mid-stage drop-offs
  Weight Loss recorded exactly 11 early-stage and 11 mid-stage churned patients, unlike Peptides and Testosterone where early-stage churn significantly outnumbers mid-stage churn.


## Retention and Drop-Off Analysis

The dataset contains 300 patient records across 3 programs — Peptides, Testosterone, and Weight Loss — with 6 fields tracking patient ID, program type, start date, treatment duration in weeks, retention status, and drop-off reason. Overall retention rates range from 71.43% to 77.32% across all programs, indicating that roughly 1 in 4 patients across the clinic does not complete or remain active in treatment. Notably, no program recorded any late-stage drop-offs, meaning all churn occurs in the early or mid stages of treatment.


## Anomalies and Risk Factors

The dataset contains 300 patient records across 3 programs: Peptides, Testosterone, and Weight Loss. Each record includes treatment duration in weeks, retention status, and drop-off reason. Anomaly detection focused on two dimensions: statistically abnormal treatment durations (IQR method) and churn rates exceeding the 25% risk threshold. No short-duration outliers were detected in any program. However, 2 out of 3 programs — Peptides and Testosterone — exceeded the 25% churn rate threshold and were flagged for high churn.

**Risk Factors Identified**

* Churn rate exceeding the 25% risk threshold
  Frequency: 2 out of 3 programs flagged (66.7%)
  Affected programs: Peptides, Testosterone
* Absence of short-duration outliers across all programs
  Frequency: 0 out of 3 programs flagged for duration outliers (0%)
  Affected programs: 

**Key Concerns**

* 2 out of 3 programs (Peptides and Testosterone) have churn rates above the 25% risk threshold, indicating a systemic retention issue across the majority of programs
* Testosterone has the highest churn rate at 28.57%, making it the most at-risk program in the dataset
* Peptides churn at 26.37%, only marginally above the threshold but still flagged — any further increase would deepen the risk level
* While no short-duration outliers were detected, the negative IQR thresholds (e.g., -34.0 weeks for Testosterone) suggest high variability in treatment duration, which may warrant further timing analysis
* Weight Loss is the only program not flagged, but at 22.68% churn it is approaching the threshold and should be monitored


## Top Priority Recommendations

* Implement targeted early-stage retention interventions for Testosterone immediately — given its combination of highest enrollment, highest churn rate (28.57%), highest absolute churn (32 patients), and highest mid-stage drop-off count (14), it represents the greatest total retention impact opportunity.
* Investigate and address front-loaded drop-off in Peptides: with 66.7% of churned patients leaving at the early stage and a Q1 duration of just 5 weeks (vs. 10.31 week average), the first 5 weeks of the Peptides program are the highest-risk window requiring immediate engagement support.
* Develop a clinic-wide early-stage engagement protocol, since 57.7% of all churn occurs at the early stage across all three programs and no late-stage churn exists — resources concentrated in the early-to-mid treatment window will have the broadest impact.
* Monitor Weight Loss for mid-stage attrition: while it is the best-performing program overall, its unique equal split of early and mid-stage drop-offs (11 each) indicates sustained churn pressure through mid-treatment that differs from other programs and could worsen without attention.
* Investigate the structural drivers of Testosterone's extreme duration variability (IQR of 32 weeks) to determine whether inconsistent patient engagement length is a cause or consequence of its high churn rate, and use findings to improve retention forecasting for that program.


## Cross-Cutting Insights

* Testosterone is flagged consistently across all four analyses — highest churn rate, highest absolute churn, highest mid-stage drop-off count, widest duration variability, and formally flagged by anomaly detection — making it the single highest-priority program by every available metric.
* Peptides' short average treatment duration (10.31 weeks) and high early-stage churn proportion (66.7%) are structurally linked: patients are leaving quickly and predominantly before mid-treatment, a pattern confirmed by both segmentation and retention analyses.
* The universal absence of late-stage churn across all programs — identified independently by segmentation, retention, and performance analyses — suggests that surviving past mid-treatment is a strong predictor of completion or continued activity, making early-to-mid intervention the highest-leverage retention window.
* Weight Loss's equal early/mid churn split (flagged in both segmentation and retention analyses) distinguishes it from the other two programs and suggests a different underlying attrition dynamic that may require a different intervention approach than the front-loaded strategies needed for Peptides and Testosterone.


---

Report generated by Multi-Agent Healthcare Analytics System on 2026-07-03 15:51:24