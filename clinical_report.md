# Clinical Insights Report

Generated: July 16, 2026 at 15:43


## Executive Summary

Across 2000 patients in three programs (Peptides: 595, Testosterone: 729, Weight Loss: 676), average retention is roughly 74.8%. Weight Loss is the strongest performer (77.96% retention, 22.04% churn, within normal range), while Testosterone is the highest-risk program (71.6% retention, 28.4% churn, longest average duration at 28.01 weeks). Peptides sits in between but still trips the high-churn flag (25.04%, just above the 25% threshold) despite having the shortest average duration (10.22 weeks). All four analyses independently converge on the same core finding: mid-stage drop-off is the dominant exit point in every program, accounting for over half of all churned patients. No treatment-duration outliers were detected in any program by any analysis, and all four reports confirm the full dataset was analyzed with no excluded or failed programs.


## Program Performance Analysis

The dataset contains 2000 patients across three programs: Peptides (595), Testosterone (729), and Weight Loss (676). Weight Loss has the best retention (77.96%) and lowest churn (22.04%), while Testosterone has the worst retention (71.6%) and highest churn (28.4%). Peptides sits in the middle with 74.96% retention but still shows a flagged high churn rate of 25.04%. All three programs show their heaviest patient drop-off occurring in the mid-stage of treatment. No treatment-duration outliers were detected in any program.

**Priority Programs**

* Testosterone: High priority
  - Highest churn rate at 28.4%, flagged as high churn
  - Lowest retention rate at 71.6%
  - Largest patient volume (729) meaning churn affects the most patients (207 churned)
  - Longest average treatment duration (28.01 weeks), increasing exposure window for drop-off
  - Highest late-stage drop-off count (38) among all programs, suggesting attrition persists even deep into treatment
* Peptides: Medium priority
  - Churn rate of 25.04% flagged as high, just above threshold
  - Largest share of churned patients occurring mid-stage (83 of 149, ~56%)
  - Shortest average treatment duration (10.22 weeks), possibly indicating early disengagement
* Weight Loss: Low priority
  - Best retention rate at 77.96% and lowest churn at 22.04%, not flagged as high risk
  - Still shows mid-stage drop-off concentration (78 of 149 churned, ~52%) worth monitoring

**Key Patterns**

* Mid-stage drop-off is the dominant churn point across all programs
  Evidence: Peptides: 83 of 149 churned patients (56%) left mid-stage; Testosterone: 107 of 207 (52%); Weight Loss: 78 of 149 (52%). In every program, mid-stage losses outnumber early and late-stage losses combined or nearly so.
* Longer average treatment duration correlates with higher churn
  Evidence: Testosterone has the longest average duration (28.01 weeks) and the highest churn rate (28.4%), while Peptides has the shortest duration (10.22 weeks) with lower churn (25.04%), though Weight Loss (16.14 weeks avg) has the lowest churn (22.04%) of all, so the relationship is not perfectly linear.
* Two of three programs exceed the 25% churn risk threshold
  Evidence: Peptides (25.04%) and Testosterone (28.4%) are both flagged for high churn; only Weight Loss (22.04%) falls under the threshold.


## Patient Segmentation Analysis

The dataset covers 2000 patients across three programs: Peptides (595), Testosterone (729), and Weight Loss (676). Retention rates range from 71.6% (Testosterone) to 77.96% (Weight Loss). Both Peptides and Testosterone show high churn rates that exceed the 25% risk threshold, while Weight Loss remains within normal churn levels. Mid-stage drop-off is the dominant pattern across all three programs.

**Patient Segments Identified**

* Mid-stage drop-off is the most common exit point across all programs
  Peptides: 83 of 149 churned patients (55.7%) left mid-stage vs 52 early and 14 late. Testosterone: 107 of 207 (51.7%) left mid-stage vs 62 early and 38 late. Weight Loss: 78 of 149 (52.3%) left mid-stage vs 44 early and 27 late.
* Longer average treatment duration correlates with higher churn rate
  Testosterone has the longest average duration (28.01 weeks) and the highest churn rate (28.4%). Peptides has the shortest duration (10.22 weeks) but still shows elevated churn (25.04%). Weight Loss sits in between (16.14 weeks) with the lowest churn (22.04%).
* Weight Loss shows the most balanced retention profile
  Highest retention rate (77.96%) and the only program not flagged for high churn (22.04%, below the 25% threshold).


## Retention and Drop-Off Analysis

Across the 3 programs analyzed (Peptides, Testosterone, Weight Loss) covering 2000 patients, retention rates range from 71.6% to 77.96%, giving an average retention of roughly 74.8%. Mid-stage drop-off is the dominant pattern in every program, meaning most patients who leave treatment do so after starting but before reaching the later stages. Testosterone stands out as the program needing the most attention due to its lower retention rate, longest treatment duration, and highest churn rate.

**Treatment Duration Trends**

* Peptides
  Mean: 10.22 weeks, Median: 10.0 weeks, Q1: 7.0 weeks, Q3: 15.0 weeks
* Testosterone
  Mean: 28.01 weeks, Median: 28.0 weeks, Q1: 17.0 weeks, Q3: 40.0 weeks
* Weight Loss
  Mean: 16.14 weeks, Median: 17.0 weeks, Q1: 10.75 weeks, Q3: 23.0 weeks

**Drop-Off Timing by Stage**

* Peptides
  Early stage: 52 patients, Mid stage: 83 patients, Late stage: 14 patients
* Testosterone
  Early stage: 62 patients, Mid stage: 107 patients, Late stage: 38 patients
* Weight Loss
  Early stage: 44 patients, Mid stage: 78 patients, Late stage: 27 patients


## Anomalies and Risk Factors

Anomaly detection covered all 3 programs (Peptides, Testosterone, Weight Loss) across 2000 patient records with no failed/excluded programs. No treatment-duration outliers were found using the IQR method in any program. However, two programs - Testosterone (28.4% churn) and Peptides (25.04% churn) - exceed the 25% churn risk threshold, while Weight Loss (22.04% churn) remains within normal range.

**Risk Factors Identified**

* Churn rate exceeding 25% threshold
  Frequency: 2 of 3 programs (67%)
  Affected programs: Testosterone, Peptides

**Key Concerns**

* Testosterone program has the highest churn rate (28.4%) among all programs, exceeding the risk threshold and warranting closer review of program design or engagement.
* Peptides program churn (25.04%) is only marginally over the threshold but still flagged, suggesting it should be monitored to prevent further increase.
* No treatment duration outliers were detected in any program, indicating that duration extremes are not currently a contributing risk factor in this dataset.
* Weight Loss remains the most stable program based on churn and retention metrics, with no anomalies flagged.


## Top Priority Recommendations

* Prioritize Testosterone for intervention: investigate drivers of its high churn (28.4%), low retention (71.6%), and long treatment duration (28.01 weeks), including its notably high late-stage drop-off (38 patients)
* Design a targeted mid-stage retention intervention applicable across all three programs, since mid-stage drop-off is the single largest and most consistent churn driver (>50% of churned patients in every program)
* Monitor Peptides closely as a medium-priority program: its churn rate (25.04%) is only marginally above the risk threshold and could be addressed early to prevent escalation, especially given its early-to-mid engagement issues despite short overall duration
* Maintain but continue light monitoring of Weight Loss, the most stable program (77.96% retention, 22.04% churn, no anomalies), while still watching its mid-stage drop-off concentration (78 patients)
* Duration-based outlier detection (IQR method) is not currently a useful risk signal (0 outliers across all programs, negative thresholds); consider refining or deprioritizing this method in favor of churn-rate and drop-off-stage monitoring


## Cross-Cutting Insights

* All four independent analyses (performance, segmentation, retention, anomaly detection) converge on identical figures and conclusions, indicating high confidence in the findings with no material discrepancies to resolve
* Mid-stage drop-off is a cross-program vulnerability independent of program type or treatment duration -- it appears as the top pattern in every report, linking the performance, segmentation, and retention findings
* Testosterone consistently appears as the top-priority/highest-risk program across all four analyses, driven by a compounding combination of highest enrollment (729), longest duration (28.01 weeks), highest churn (28.4%), lowest retention (71.6%), and highest late-stage drop-off (38 patients)
* The churn-threshold anomaly flags (Peptides, Testosterone) directly explain the segmentation and performance rankings that place these two programs in 'Medium' and 'High' attention tiers, while Weight Loss's clean anomaly profile aligns with its 'Low' priority ranking across all reports


---

Report generated by Multi-Agent Healthcare Analytics System on 2026-07-16 15:43:38