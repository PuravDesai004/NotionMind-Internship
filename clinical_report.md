# Clinical Insights Report

Generated: July 24, 2026 at 14:44


## Executive Summary

Across 2,000 patients in three programs (Peptides, Testosterone, Weight Loss), retention ranges from 71.6% to 77.96%. Testosterone is the highest-risk program, combining the largest enrollment (729 patients), lowest retention (71.6%), and highest churn (28.4%, flagged as anomalous). Peptides also exceeds the 25% churn risk threshold (25.04%, flagged) despite its short average duration. Weight Loss is the strongest performer, with the highest retention (77.96%) and churn (22.04%) within normal range. A consistent, cross-program pattern is that mid-stage treatment is the dominant drop-off window, accounting for roughly 52-56% of churned patients in every program. No statistical outliers in treatment duration were detected in any program, indicating churn is driven by timing/rate patterns rather than isolated extreme cases.


## Program Performance Analysis

The dataset covers 2000 patients across three programs: Peptides, Testosterone, and Weight Loss. Weight Loss has the best retention (77.96%) and lowest churn (22.04%), while Testosterone has the weakest performance with the lowest retention (71.6%) and highest churn (28.4%), despite having the largest enrollment (729 patients) and longest average treatment duration (28.01 weeks). Peptides sits in the middle but has a churn rate (25.04%) that also exceeds the 25% risk threshold. Across all three programs, most drop-offs happen in the mid-stage of treatment rather than early or late stage.

**Priority Programs**

* Testosterone: High priority
  - Lowest retention rate at 71.6%
  - Highest churn rate at 28.4%, flagged as 'High churn detected' by anomaly detection
  - Largest enrollment (729 patients), meaning the churn impacts the most patients in absolute terms (207 churned)
  - Highest late-stage drop-off count (38 patients), suggesting patients are leaving even after longer commitment
  - Highest mid-stage drop-off count (107 patients)
* Peptides: Medium priority
  - Churn rate of 25.04% is just above the 25% risk threshold and flagged as 'High churn detected'
  - Shortest average treatment duration (10.22 weeks), which combined with churn may indicate early program design issues
  - Mid-stage drop-off (83 patients) is the majority of its 149 churned patients
* Weight Loss: Low priority
  - Best retention rate (77.96%) and churn rate (22.04%) not flagged as anomalous
  - Still shows mid-stage drop-off concentration (78 of 149 churned) worth monitoring

**Key Patterns**

* Mid-stage drop-off is the dominant churn point across all programs
  Evidence: Mid-stage patient drop-off counts are highest in every program: Peptides (83 of 149 churned), Testosterone (107 of 207 churned), Weight Loss (78 of 149 churned) -- all higher than early-stage or late-stage drop-offs.
* Longer average treatment duration correlates with higher churn and more late-stage drop-off
  Evidence: Testosterone has the longest average duration (28.01 weeks) and highest churn (28.4%) and also the most late-stage drop-offs (38 patients), compared to Peptides (10.22 weeks, 25.04% churn, 14 late-stage) and Weight Loss (16.14 weeks, 22.04% churn, 27 late-stage).
* Weight Loss shows the most balanced and healthiest retention profile
  Evidence: Highest retention rate (77.96%), lowest churn rate (22.04%, not flagged), and relatively even spread of drop-offs across stages compared to other programs.


## Patient Segmentation Analysis

The dataset covers 2,000 patients across three program types: Peptides (595 patients), Testosterone (729 patients), and Weight Loss (676 patients). Retention rates range from 71.6% to 77.96%. Two of the three programs (Peptides and Testosterone) show churn rates above the 25% risk threshold, while Weight Loss remains within normal churn levels. Across all programs, mid-stage drop-off is the most common point of patient loss, making it the dominant segmentation pattern in the data.

**Patient Segments Identified**

* Mid-stage drop-off is the most common churn point across all program types
  Peptides: 83 mid-stage vs 52 early / 14 late drop-offs. Testosterone: 107 mid-stage vs 62 early / 38 late. Weight Loss: 78 mid-stage vs 44 early / 27 late. In every program, mid-stage losses outnumber early and late stage combined.
* Longer average treatment duration correlates with higher churn
  Testosterone has the longest average duration (28.01 weeks) and the highest churn rate (28.4%). Peptides has the shortest duration (10.22 weeks) but still a high churn rate (25.04%), while Weight Loss (16.14 weeks average) has the lowest churn (22.04%).
* Weight Loss shows the most balanced retention profile
  Weight Loss has the highest retention rate (77.96%), the lowest churn rate (22.04%, not flagged), and the most even distribution of drop-off across early/mid/late stages relative to its patient count.


## Retention and Drop-Off Analysis

Across the three programs (Peptides, Testosterone, Weight Loss) covering 2000 patients, retention rates range from 71.6% to 77.96%, with an average retention of about 74.8%. Mid-stage drop-off is the dominant exit point in every program, suggesting patients most commonly disengage after starting treatment but before completing it, rather than immediately or right at the end.

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

Across the three programs (Peptides, Testosterone, Weight Loss) covering 2,000 patients, no statistically extreme short-duration outliers were detected using the IQR method for any program. However, two of the three programs exceed the 25% churn rate risk threshold: Testosterone (28.4%) and Peptides (25.04%). Weight Loss remains under the threshold at 22.04% but is close enough to warrant monitoring.

**Risk Factors Identified**

* Churn rate above 25% threshold
  Frequency: 2 of 3 programs (67%)
  Affected programs: Testosterone, Peptides
* Mid-stage patient drop-off concentration
  Frequency: 3 of 3 programs (100%)
  Affected programs: Peptides, Testosterone, Weight Loss

**Key Concerns**

* Testosterone and Peptides both exceed the 25% churn threshold, indicating a retention risk affecting the majority of patients enrolled in these two programs (1,324 of 2,000 total patients, or 66.2%)
* Mid-stage drop-off is the dominant pattern in all three programs, suggesting patients are most likely to disengage partway through treatment rather than at the very start or end
* Testosterone has the longest average treatment duration (28.01 weeks) and also the highest churn rate, which together may compound retention challenges over a longer commitment period


## Top Priority Recommendations

* Prioritize Testosterone for intervention: investigate causes of its highest churn rate (28.4%), largest absolute churned population (207 patients), and elevated late-stage attrition despite long treatment duration.
* Investigate and address the mid-stage drop-off window across all programs, since it is the dominant and consistent churn point (52-56% of drop-offs in every program) -- likely the single highest-leverage fix available.
* Monitor and address Peptides' churn rate (25.04%), which narrowly exceeds the risk threshold, with particular focus on its early-to-mid treatment window where drop-off concentrates.
* Use Weight Loss's retention model (77.96% retention, balanced drop-off distribution) as a benchmark or reference design when evaluating retention strategies for the other two programs.
* Continue monitoring treatment duration data even though no outliers were detected, since Testosterone's long duration (28 weeks) and wide variability (Q1 17 - Q3 40 weeks) may still be an underlying contributor to late-stage churn worth deeper investigation.


## Cross-Cutting Insights

* Mid-stage drop-off is the single most consistent finding across all four reports and all three programs (accounting for ~52-56% of churned patients in each), pointing to a shared operational risk period independent of program type or duration.
* Testosterone's combination of largest enrollment, longest duration, lowest retention, and flagged high churn appears consistently across program performance, segmentation, retention, and anomaly reports, confirming it as the top-priority program.
* Longer average treatment duration (most pronounced in Testosterone) correlates with greater late-stage attrition, suggesting that extended commitment periods carry compounding retention risk over time.
* Peptides presents a paradox: despite the shortest program duration, it has a high relative concentration of mid-stage drop-off and a churn rate just above the risk threshold, suggesting early-to-mid engagement issues rather than long-duration fatigue.
* No treatment-duration outliers were found in any program (consistent across retention and anomaly reports), reinforcing that churn is a rate/timing phenomenon rather than driven by isolated extreme cases.


---

Report generated by Multi-Agent Healthcare Analytics System on 2026-07-24 14:44:31