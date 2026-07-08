# Clinical Insights Report

Generated: July 08, 2026 at 14:12


## Executive Summary

Across 300 patients in three programs, Weight Loss is the strongest performer (77.32% retention, 22.68% churn, within normal range), while Testosterone and Peptides both exceed the 25% churn risk threshold (28.57% and 26.37% respectively). Testosterone is the highest-priority concern: it has the largest enrollment (112 patients), the lowest retention (71.43%), the longest and most variable treatment duration (mean 28.22 weeks, IQR 14-46), and the most churned patients (32). Peptides is a medium-priority concern, combining high churn with the shortest average treatment duration (10.31 weeks), suggesting early disengagement. A consistent pattern across all programs is that drop-off is concentrated in early and mid-stage treatment, with zero late-stage drop-offs recorded, and no statistical treatment-duration outliers were found anywhere -- churn rate, not duration extremes, is the primary risk signal.


## Program Performance Analysis

Across 300 patients in three programs, Weight Loss has the strongest retention (77.32%) and normal churn levels, while Testosterone and Peptides both show churn rates above the 25% risk threshold. Testosterone has the largest enrollment (112 patients) and the longest average treatment duration (28.22 weeks), but also the lowest retention rate (71.43%). No treatment-duration outliers were found in any program, and drop-offs across all three programs are concentrated in the early and mid stages, with zero late-stage drop-offs recorded.

**Priority Programs**

* Testosterone: High priority
  - Lowest retention rate at 71.43%
  - Highest churn rate at 28.57%, flagged as high churn
  - Largest patient enrollment (112), so churn affects the most patients (32 churned)
  - Longest average treatment duration (28.22 weeks) yet still lowest retention
  - Highest mid-stage drop-off count (14 patients)
* Peptides: Medium priority
  - Churn rate of 26.37% flagged as high churn
  - Shortest average treatment duration (10.31 weeks)
  - Heaviest concentration of early-stage drop-off relative to program size (16 of 24 churned patients left early)
* Weight Loss: Low priority
  - Highest retention rate (77.32%)
  - Churn rate of 22.68% is within normal range (not flagged)
  - Drop-off is evenly split between early and mid stage (11 vs 11), showing no strong concentration pattern

**Key Patterns**

* Early-stage drop-off dominates over mid and late stage across all programs
  Evidence: Peptides: 16 early vs 8 mid vs 0 late; Testosterone: 18 early vs 14 mid vs 0 late; Weight Loss: 11 early vs 11 mid vs 0 late
* Longer average treatment duration correlates with lower retention
  Evidence: Testosterone has the longest average duration (28.22 weeks) and the lowest retention rate (71.43%), while Weight Loss has a mid-length duration (16.47 weeks) and the highest retention (77.32%)
* Two of three programs exceed the 25% churn risk threshold
  Evidence: Peptides churn rate 26.37% (flagged), Testosterone churn rate 28.57% (flagged), Weight Loss churn rate 22.68% (not flagged)


## Patient Segmentation Analysis

The dataset contains 300 patients across three programs: Peptides (91), Testosterone (112), and Weight Loss (97). All three show early-stage drop-off as the dominant churn pattern, with no late-stage drop-offs recorded anywhere. Testosterone has the weakest retention profile of the three, while Weight Loss performs best overall.

**Patient Segments Identified**

* Early-stage drop-off dominates across all programs
  Peptides: 16 early vs 8 mid-stage drop-offs (0 late); Testosterone: 18 early vs 14 mid-stage (0 late); Weight Loss: 11 early vs 11 mid-stage (0 late). No program recorded any late-stage churn.
* Testosterone has the longest average treatment duration but also the highest churn
  Testosterone averages 28.22 weeks (median 25.5) versus Peptides at 10.31 weeks and Weight Loss at 16.47 weeks, yet Testosterone has the highest churn rate at 28.57%.
* Weight Loss shows the most balanced drop-off timing and best retention
  Weight Loss has an even split of early (11) and mid-stage (11) drop-offs and the highest retention rate at 77.32%, with churn at 22.68% (below the 25% risk threshold).
* Peptides has the shortest treatment duration alongside elevated churn
  Peptides averages just 10.31 weeks (Q1: 5, Q3: 16) and carries a 26.37% churn rate, exceeding the 25% risk threshold.


## Retention and Drop-Off Analysis

Across the three programs (Peptides, Testosterone, Weight Loss), retention rates are fairly close, ranging from 71.43% to 77.32%. Weight Loss has the highest retention (77.32%), followed by Peptides (73.63%) and Testosterone (71.43%). Drop-offs across all programs occur mainly in the early and mid stages of treatment, with no late-stage drop-offs recorded in any program.

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

Anomaly detection across 300 patient records in 3 programs (Peptides, Testosterone, Weight Loss) found no statistically abnormal treatment duration outliers using the IQR method. However, two programs exceed the 25% churn rate risk threshold: Testosterone (28.57%) and Peptides (26.37%). Weight Loss remains within normal churn levels (22.68%).

**Risk Factors Identified**

* Churn rate exceeding 25% risk threshold
  Frequency: 2 out of 3 programs (66.7%)
  Affected programs: Testosterone, Peptides

**Key Concerns**

* Testosterone has the highest churn rate (28.57%) among all programs, flagged as a risk
* Peptides also exceeds the churn risk threshold at 26.37%
* No abnormal treatment duration outliers were detected in any program, suggesting churn is the primary anomaly driver rather than unusually short treatments


## Top Priority Recommendations

* Prioritize Testosterone for intervention: investigate causes of early/mid-stage drop-off (32 of 112 patients churned) and evaluate whether the wide duration variability (14-46 weeks) reflects inconsistent care pathways that could be standardized
* Address Peptides' early disengagement: since patients churn quickly (average duration only 10.31 weeks, 16 of 24 churned patients leaving early), focus retention efforts on the first few weeks of enrollment
* Apply Weight Loss's balanced drop-off pattern and normal churn (22.68%) as a benchmark model when redesigning early-stage engagement strategies for Testosterone and Peptides
* Concentrate retention resources on early-to-mid stage treatment across all programs, since zero late-stage drop-offs indicate that patients who reach later stages are essentially retained
* Since no treatment-duration outliers exist, avoid resource allocation toward individual-outlier case review and instead focus on systemic, program-level churn-rate reduction strategies for Testosterone and Peptides


## Cross-Cutting Insights

* All four reports independently converge on the same core finding: Testosterone is the highest-risk program (lowest retention, highest churn, largest affected population) and Weight Loss is the lowest-risk, best-performing program -- consistent across performance, segmentation, retention, and anomaly analyses
* The early-stage drop-off pattern identified in performance and segmentation reports is explained in detail by the retention analysis, which shows Peptides and Testosterone patients leaving disproportionately early (16/8 and 18/14 early/mid splits) while Weight Loss remains balanced
* Testosterone's long average duration (28.22 weeks) combined with its wide IQR spread (14-46 weeks) and highest churn suggests that longer, less standardized treatment timelines do not translate into better retention -- a pattern flagged separately in performance (duration-retention correlation) and retention (duration variability) reports
* The absence of late-stage drop-off across all programs and all four analyses reinforces that intervention should target the early-to-mid treatment window rather than program completion stages


---

Report generated by Multi-Agent Healthcare Analytics System on 2026-07-08 14:12:59