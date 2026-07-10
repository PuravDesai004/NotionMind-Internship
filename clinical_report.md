# Clinical Insights Report

Generated: July 10, 2026 at 14:05


## Executive Summary

Across 300 patients in three programs (Peptides: 91, Testosterone: 112, Weight Loss: 97), overall retention averages ~74%, ranging from 71.43% (Testosterone) to 77.32% (Weight Loss). Testosterone is the highest-risk program: it has the largest enrollment, the lowest retention (71.43%), the highest churn count (32 patients, 28.57%), the longest and most variable treatment duration (mean 28.22 weeks, IQR 14-46), and the highest mid-stage drop-off (14 patients). Peptides is a medium-risk program with high churn (26.37%, 24 patients) concentrated heavily in the early stage (16 of 24 drop-offs) despite the shortest average treatment duration (10.31 weeks). Weight Loss is the strongest performer, with the highest retention (77.32%), lowest churn (22.68%), and no anomaly flags. No statistical duration outliers were found in any program, and no program shows late-stage attrition -- all churn occurs in early or mid treatment stages.


## Program Performance Analysis

The dataset contains 300 patients across three programs: Peptides (91 patients), Testosterone (112 patients), and Weight Loss (97 patients). Overall retention across programs ranges from about 71% to 77%, with Testosterone showing the lowest retention and Weight Loss the highest. Treatment duration varies significantly, from an average of 10.31 weeks for Peptides to 28.22 weeks for Testosterone.

**Priority Programs**

* Testosterone: High priority
  - Lowest retention rate at 71.43%
  - Highest churn count at 32 patients (28.57% churn)
  - Largest enrollment (112 patients), meaning churn affects the most people in absolute terms
  - Longest average treatment duration (28.22 weeks), which may contribute to more opportunities for drop-off
* Peptides: Medium priority
  - Churn rate of 26.37% is close to Testosterone's and above the 25% mark
  - Shortest average treatment duration (10.31 weeks) paired with a relatively high churn count (24 patients)
* Weight Loss: Low priority
  - Highest retention rate at 77.32%
  - Lowest churn rate at 22.68%
  - Moderate treatment duration (16.47 weeks) with a comparatively stable outcome

**Key Patterns**

* Weight Loss has the highest retention rate and the lowest churn rate among all programs
  Evidence: Weight Loss retention rate is 77.32% (75 active out of 97 patients), with only 22 churned patients (22.68% churn)
* Testosterone has the largest patient base but the weakest retention rate
  Evidence: Testosterone has 112 patients (the most of any program) but only 71.43% retention, with 32 patients churned (28.57% churn)
* Treatment duration is strongly tied to program type, with Testosterone requiring much longer average treatment than the other two programs
  Evidence: Average treatment duration: Peptides 10.31 weeks, Weight Loss 16.47 weeks, Testosterone 28.22 weeks
* Peptides has the shortest average treatment duration but a churn rate close to Testosterone's
  Evidence: Peptides average duration is 10.31 weeks (shortest) yet churn is 26.37% (24 of 91 patients), higher than Weight Loss's 22.68%


## Patient Segmentation Analysis

Across 300 patients in three programs (Peptides, Testosterone, Weight Loss), retention rates range from 71.4% to 77.3%. Testosterone and Peptides both show high churn (flagged above 25% threshold), while Weight Loss has the strongest retention and normal churn levels. All programs show drop-off concentrated in early and mid stages, with no late-stage drop-off recorded in any segment.

**Patient Segments Identified**

* Early-stage drop-off dominates across all programs
  Peptides: 16 early vs 8 mid drop-offs; Testosterone: 18 early vs 14 mid; Weight Loss: 11 early vs 11 mid. No late-stage drop-offs recorded in any program.
* Testosterone has the longest average treatment duration but also the highest churn count
  Testosterone average duration is 28.22 weeks (highest of all programs) with 32 churned patients (28.57% churn rate), compared to Peptides (10.31 weeks, 24 churned) and Weight Loss (16.47 weeks, 22 churned).
* Weight Loss shows the most balanced drop-off timing and best retention
  Weight Loss has equal early (11) and mid (11) drop-offs, a 77.32% retention rate, and a churn rate of 22.68%, the only program not flagged for high churn.


## Retention and Drop-Off Analysis

Across all three programs (Peptides, Testosterone, Weight Loss), the average retention rate is about 74.1%, meaning roughly 1 in 4 patients drop off before finishing treatment. None of the programs show any late-stage drop-off, indicating that when patients leave, it happens in the early or middle parts of their treatment journey rather than near the end.

**Treatment Duration Trends**

* Peptides
  Mean: 10.31 weeks, Median: 11.0 weeks, Q1: 5.0 weeks, Q3: 16.0 weeks
* Testosterone
  Mean: 28.22 weeks, Median: 25.5 weeks, Q1: 14.0 weeks, Q3: 46.0 weeks
* Weight Loss
  Mean: 16.47 weeks, Median: 17.0 weeks, Q1: 9.0 weeks, Q3: 26.0 weeks

**Drop-Off Timing by Stage**

* Peptides
  Early stage: 16 patients, Mid stage: 8 patients, Late stage: 0 patients
* Testosterone
  Early stage: 18 patients, Mid stage: 14 patients, Late stage: 0 patients
* Weight Loss
  Early stage: 11 patients, Mid stage: 11 patients, Late stage: 0 patients


## Anomalies and Risk Factors

Across 300 patients in three programs (Peptides, Testosterone, Weight Loss), no statistically abnormal treatment duration outliers were detected using the IQR method. However, two programs - Testosterone and Peptides - exceed the 25% churn rate risk threshold, indicating retention concerns rather than duration concerns.

**Risk Factors Identified**

* Churn rate exceeding 25% threshold
  Frequency: 2 of 3 programs flagged (66.7%)
  Affected programs: Peptides, Testosterone

**Key Concerns**

* Testosterone has the highest churn rate (28.57%), the most severe anomaly flagged in the dataset
* Peptides also exceeds the churn risk threshold at 26.37%, close behind Testosterone
* No program shows statistically abnormal treatment duration outliers, so risk is concentrated in retention/churn rather than duration extremes
* Two out of three programs (66.7%) are flagged for high churn, suggesting a broader retention issue rather than an isolated program problem


## Top Priority Recommendations

* Prioritize Testosterone for intervention: investigate drivers of its high churn (28.57%, 32 patients) and long/variable treatment duration (mean 28.22 weeks, range 14-46 weeks), with particular focus on reducing mid-stage drop-off (14 patients)
* Address early-stage disengagement in Peptides: 16 of 24 churned patients drop off early despite the program's short average duration (10.31 weeks), suggesting a need for stronger onboarding or early check-ins
* Focus retention interventions on early and mid treatment stages across all programs, since no program shows late-stage attrition -- resources are better spent before patients reach later stages
* Use Weight Loss's balanced drop-off pattern and strong retention (77.32%) as a benchmark model to inform engagement strategies for the other two programs
* Conduct further timing-based and root-cause analysis (e.g., reasons for drop-off, patient feedback) for Testosterone and Peptides, since current anomaly detection found no duration outliers, meaning the churn issue is behavioral/retention-based rather than a duration extreme


## Cross-Cutting Insights

* The high-churn flag for Testosterone and Peptides is consistent across program performance, segmentation, retention, and anomaly reports, confirming it is a robust, high-confidence finding rather than an artifact of one analysis method
* Testosterone's combination of longest average duration (28.22 weeks), widest duration variability (14-46 weeks), and highest churn count suggests that longer, less standardized treatment courses may correlate with greater drop-off risk
* Peptides' short average duration (10.31 weeks) paired with heavy early-stage drop-off (16 of 24 churned patients) suggests patients are disengaging very early in a program that is already brief, pointing to a possible onboarding/early-engagement gap rather than fatigue over a long course
* The universal absence of late-stage drop-off across all programs and all four analyses indicates that patients who progress past the early/mid stages reliably complete treatment, so intervention value is highest if focused on the early-to-mid window
* Weight Loss's balanced drop-off timing, lowest churn, and lack of any anomaly flags consistently position it as the lowest-risk, best-performing program across every analytical lens


---

Report generated by Multi-Agent Healthcare Analytics System on 2026-07-10 14:05:03