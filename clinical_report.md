# Clinical Insights Report

Generated: July 10, 2026 at 13:18


## Executive Summary

Analysis of 300 patients across three programs (Peptides, Testosterone, Weight Loss) shows an overall retention rate of ~74%. Weight Loss is the strongest program (77.32% retention, 22.68% churn, no flagged anomalies). Testosterone is the highest-risk program: largest enrollment (112 patients), lowest retention (71.43%), highest churn (28.57%), and the longest, most variable treatment duration (mean 28.22 weeks). Peptides also exceeds the 25% churn risk threshold (26.37%) with drop-off heavily concentrated in the early stage. Across all programs, early-stage drop-off is the dominant attrition pattern, no late-stage drop-off was recorded, and no treatment-duration outliers were detected by any method — churn rate, not duration, is the primary risk driver in this dataset.


## Program Performance Analysis

Across 300 patients in three programs (Peptides, Testosterone, Weight Loss), Weight Loss has the best retention (77.32%) and lowest churn (22.68%), while Testosterone has the largest enrollment (112 patients) but the weakest retention (71.43%) and highest churn (28.57%). Peptides also shows high churn (26.37%) despite having the shortest average treatment duration (10.31 weeks). No program shows late-stage drop-off, meaning all recorded churn happens in early or mid treatment stages.

**Priority Programs**

* Testosterone: High priority
  - Highest churn rate at 28.57%, flagged as high churn
  - Lowest retention rate at 71.43%
  - Largest enrollment (112 patients), so churn affects the most people in absolute terms (32 churned)
  - Longest average treatment duration (28.22 weeks), yet still highest drop-off
* Peptides: Medium priority
  - Churn rate of 26.37% flagged as high
  - Shortest average treatment duration (10.31 weeks)
  - Early-stage drop-off (16 patients) is twice the mid-stage drop-off (8 patients), suggesting patients leave sooner than in other programs
* Weight Loss: Low priority
  - Best retention rate at 77.32%
  - Churn rate of 22.68% is below the risk threshold and not flagged
  - Balanced drop-off pattern between early and mid stages

**Key Patterns**

* Testosterone has by far the longest average treatment duration and the largest patient base, but also the highest churn rate.
  Evidence: Average duration 28.22 weeks vs 16.47 (Weight Loss) and 10.31 (Peptides); churn rate 28.57% vs 22.68% and 26.37%.
* All three programs show zero late-stage drop-off; churn is concentrated in early and mid treatment stages only.
  Evidence: Late_stage_patients = 0 for Peptides, Testosterone, and Weight Loss in outcome analysis.
* Peptides has the shortest treatment duration and its drop-off is heavily weighted toward the early stage.
  Evidence: Mean duration 10.31 weeks; early-stage drop-off (16 patients) is double mid-stage drop-off (8 patients).
* Weight Loss shows the most balanced drop-off distribution and the healthiest overall retention profile.
  Evidence: Retention rate 77.32% (highest), churn rate 22.68% (only program not flagged), early (11) and mid (11) drop-offs are equal.


## Patient Segmentation Analysis

Across 300 patients in three programs (Peptides, Testosterone, Weight Loss), retention ranges from 71% to 77%. Testosterone has the largest patient base (112) and the highest churn rate (28.57%), while Weight Loss shows the strongest retention (77.32%) and no flagged anomalies. Early-stage drop-off dominates in all programs, with no late-stage drop-offs recorded anywhere.

**Patient Segments Identified**

* Early-stage drop-off is the dominant churn pattern across all programs
  Peptides: 16 early vs 8 mid-stage drop-offs; Testosterone: 18 early vs 14 mid-stage; Weight Loss: 11 early vs 11 mid-stage. No program recorded any late-stage drop-offs.
* Longer average treatment duration does not guarantee better retention
  Testosterone has the longest average duration (28.22 weeks) but the lowest retention rate (71.43%) and highest churn (28.57%), while Peptides has the shortest duration (10.31 weeks) yet slightly better retention (73.63%).
* Weight Loss shows the most balanced and stable retention profile
  Highest retention rate (77.32%), lowest churn (22.68%), and equal early/mid drop-off split (11 vs 11), with no anomaly flags raised.


## Retention and Drop-Off Analysis

Across all 300 patients in the dataset, the overall retention rate is approximately 74% (222 retained out of 300), with roughly 78 patients dropping off across the three programs. Peptides shows 73.63% retention, Testosterone 71.43%, and Weight Loss 77.32%, making Weight Loss the strongest performer and Testosterone the weakest.

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

Anomaly detection was run across 300 patient records spanning 3 programs (Peptides, Testosterone, Weight Loss). No statistically abnormal treatment duration outliers were found in any program using the IQR method. However, 2 of the 3 programs exceed the 25% churn rate risk threshold: Testosterone (28.57%) and Peptides (26.37%). Weight Loss is within normal churn levels at 22.68%.

**Risk Factors Identified**

* Churn rate above 25% threshold
  Frequency: 2 out of 3 programs (66.7%)
  Affected programs: Testosterone, Peptides

**Key Concerns**

* Testosterone has the highest churn rate (28.57%) of all programs and is flagged as high risk.
* Peptides also exceeds the churn risk threshold at 26.37%.
* 2 out of 3 programs (66.7%) exceed the defined 25% churn risk threshold, suggesting churn is a widespread issue rather than isolated to one program.
* No treatment duration outliers were found in any program, so duration is not currently a contributing anomaly factor.


## Top Priority Recommendations

* Prioritize retention intervention for Testosterone: largest enrollment (112) combined with highest churn (28.57%) and lowest retention (71.43%) means it has the greatest absolute number of at-risk patients (32 churned)
* Target early-stage patient engagement across all programs, since early-stage drop-off is the most common and consistent exit point (Peptides 16, Testosterone 18, Weight Loss 11)
* Investigate mid-stage retention specifically for Testosterone and Weight Loss, where mid-stage drop-off nearly equals early-stage drop-off, indicating risk does not end after program start
* Review Peptides' early program experience (first ~10 weeks), since two-thirds of its churn occurs early despite the shortest average duration
* Examine causes of Testosterone's highly variable treatment duration (14–46 week spread) to understand whether inconsistent engagement structure contributes to its high churn
* Use Weight Loss's balanced drop-off and strong retention as a model/benchmark for improving the other two programs, since it shows no anomalies and the most even risk distribution


## Cross-Cutting Insights

* All four analyses independently converge on the same risk ranking: Testosterone (high) > Peptides (medium) > Weight Loss (low), driven primarily by churn rate rather than duration anomalies
* Early-stage drop-off is a universal pattern across all programs and all analyses, suggesting the first phase of treatment is the most common and consistent point of patient loss
* Testosterone's paradox — longest average duration combined with highest churn and notable mid-stage drop-off — indicates that even patients who stay longer are not more likely to retain, and attrition risk extends well past the early stage in this program
* Peptides' short duration paired with heavy early-stage concentration of drop-off (67%) suggests an early program experience issue distinct from Testosterone's more spread-out attrition pattern
* Absence of any duration outliers across all programs and methods reinforces that churn rate, not unusual treatment length, is the dataset's central risk signal


---

Report generated by Multi-Agent Healthcare Analytics System on 2026-07-10 13:18:52