# Clinical Insights Report

Generated: July 16, 2026 at 12:07


## Executive Summary

Across 300 patients in three programs, Weight Loss is the strongest performer (77.32% retention, 22.68% churn, within normal range), while Testosterone (28.57% churn, 71.43% retention) and Peptides (26.37% churn, 73.63% retention) both exceed the 25% churn risk threshold. All four analyses agree that drop-off is concentrated in early and mid treatment stages, with zero late-stage attrition recorded in any program. No duration outliers were found via IQR analysis, indicating churn rate itself—not unusual treatment length—is the primary risk signal. Testosterone is the top-priority program due to its combination of largest enrollment (112 patients), highest churn, and longest average duration (28.22 weeks); Peptides is a medium priority due to high churn despite its short duration (10.31 weeks).


## Program Performance Analysis

The dataset covers 300 patients across three programs: Testosterone (112 patients), Weight Loss (97 patients), and Peptides (91 patients). Weight Loss has the best retention (77.32%) and normal churn levels, while Testosterone and Peptides both show high churn rates that exceed the 25% risk threshold. Early-stage drop-off is the dominant timing pattern across all three programs, and no late-stage drop-offs were recorded anywhere in the dataset. No failed or excluded programs were reported by any tool.

**Priority Programs**

* Testosterone: High priority
  - Largest enrollment (112 patients), so issues affect the most people
  - Highest churn rate at 28.57%, flagged as high churn
  - Longest average treatment duration (28.22 weeks), with a wide spread (Q1: 14 weeks, Q3: 46 weeks)
  - Highest raw count of early-stage churned patients (18) and mid-stage churned patients (14)
* Peptides: Medium priority
  - Second-highest churn rate at 26.37%, flagged as high churn
  - Shortest average treatment duration (10.31 weeks), meaning patients drop off relatively quickly
  - Early-stage drop-off (16 patients) is double the mid-stage drop-off (8 patients), suggesting patients leave very soon after starting
* Weight Loss: Low priority
  - Best retention rate at 77.32%
  - Churn rate of 22.68% is within normal range (not flagged)
  - Drop-off is evenly split between early and mid stage (11 each), showing no concentrated risk point

**Key Patterns**

* Early-stage drop-off dominates churn in every program
  Evidence: Peptides: 16 early-stage vs 8 mid-stage churned patients; Testosterone: 18 early vs 14 mid; Weight Loss: 11 early vs 11 mid. Zero late-stage drop-offs recorded across all programs.
* Longer average treatment duration correlates with higher churn
  Evidence: Testosterone has the longest average duration (28.22 weeks) and the highest churn rate (28.57%), while Weight Loss has a mid-length duration (16.47 weeks) with the lowest churn (22.68%).
* Peptides has the shortest treatment duration but still high churn
  Evidence: Peptides averages only 10.31 weeks (median 11.0) yet has a 26.37% churn rate, flagged as high despite the short program length.


## Patient Segmentation Analysis

Across 300 patients in three programs (Peptides, Testosterone, Weight Loss), retention rates range from 71.4% to 77.3%. Testosterone and Peptides both show high churn (over 25%), while Weight Loss remains within normal churn range. Drop-off in all three programs happens almost entirely in the early and mid stages of treatment, with zero late-stage drop-offs recorded anywhere.

**Patient Segments Identified**

* Early-stage drop-off dominates across all programs
  Peptides: 16 early vs 8 mid drop-offs; Testosterone: 18 early vs 14 mid; Weight Loss: 11 early vs 11 mid. No late-stage drop-offs recorded in any program.
* Longer average program duration correlates with more mid-stage drop-off
  Testosterone has the longest average duration (28.22 weeks) and the highest mid-stage drop-off count (14), compared to Peptides' shortest duration (10.31 weeks) and lowest mid-stage drop-off (8).
* Weight Loss shows the most balanced and stable retention profile
  Weight Loss has the highest retention rate (77.32%), lowest churn (22.68%, not flagged), and equal early/mid drop-off split (11/11), unlike the other two programs where early-stage loss outweighs mid-stage.


## Retention and Drop-Off Analysis

Across the three programs analyzed (Peptides, Testosterone, Weight Loss), the average retention rate is approximately 74.1%. Weight Loss has the highest retention (77.32%), followed by Peptides (73.63%), while Testosterone has the lowest (71.43%). No program shows any late-stage drop-off patients, meaning all recorded drop-offs happen in the early or mid stages of treatment.

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

Anomaly detection was run across 300 patient records spanning three programs (Peptides, Testosterone, Weight Loss). No treatment duration outliers were found in any program using the IQR method, but two of the three programs exceed the 25% churn rate risk threshold: Testosterone (28.57%) and Peptides (26.37%). Weight Loss (22.68%) remains under the threshold and is considered normal.

**Risk Factors Identified**

* High churn rate (above 25% threshold)
  Frequency: 2 out of 3 programs (66.7%)
  Affected programs: Testosterone, Peptides

**Key Concerns**

* Testosterone and Peptides both exceed the 25% churn risk threshold, indicating retention issues in these two programs.
* No treatment duration outliers were found in any program, suggesting churn (not unusually short or long treatment durations) is the primary risk signal.
* Weight Loss churn (22.68%) is close to the 25% threshold and could shift into flagged territory if trends worsen.


## Top Priority Recommendations

* Prioritize retention interventions for Testosterone given its combination of largest patient base (112), highest churn rate (28.57%), longest treatment duration, and highest early+mid drop-off counts
* Investigate root causes of rapid early-stage disengagement in Peptides, where patients churn quickly (avg. 10.31 weeks) at a high rate (26.37%), despite the program's short length
* Focus retention efforts specifically on the early treatment stage across all three programs, since this is the dominant and consistent drop-off point with no late-stage attrition observed
* Monitor Weight Loss's churn rate (22.68%) proactively, as it is the closest normal-range program to the 25% risk threshold and could shift into flagged status
* Since no duration-based statistical outliers exist, deprioritize duration-focused interventions in favor of addressing churn drivers directly (e.g., early patient engagement/onboarding)


## Cross-Cutting Insights

* All four reports independently converge on identical core metrics (churn/retention rates, duration, drop-off counts), reinforcing confidence in the findings with no material discrepancies to resolve
* Early-stage drop-off is the universal risk driver across all programs and all analyses, with zero late-stage attrition recorded — this pattern connects the program performance, segmentation, retention, and anomaly findings
* Testosterone consistently emerges as highest priority across every report: largest population, highest churn, longest duration, and highest anomaly severity all align on this single program
* Peptides presents a distinct paradox flagged consistently across reports: high churn despite the shortest treatment duration, suggesting patients disengage rapidly rather than gradually
* Weight Loss's balanced early/mid drop-off split (unlike the skewed patterns in Testosterone and Peptides) aligns with its status as the only program under the churn risk threshold


---

Report generated by Multi-Agent Healthcare Analytics System on 2026-07-16 12:07:57