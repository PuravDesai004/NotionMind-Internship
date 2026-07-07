# Clinical Insights Report

Generated: July 07, 2026 at 14:15


## Executive Summary

Across 300 patients in three programs (Peptides, Testosterone, Weight Loss), overall retention averages roughly 74%, ranging from 71.43% (Testosterone) to 77.32% (Weight Loss). Testosterone and Peptides both exceed the 25% churn-risk threshold (28.57% and 26.37% respectively) and are flagged as high-churn programs, while Weight Loss remains within normal limits (22.68% churn). All patient loss across all three programs occurs in early or mid-stage treatment, with zero late-stage drop-offs and no statistical duration outliers detected anywhere. Testosterone is the top-priority program due to its combination of lowest retention, highest churn, and largest raw churned count (32 patients), despite having the longest average treatment duration (28.22 weeks). Peptides is a secondary concern, driven by rapid early-stage attrition (67% of its churn) within a short average treatment span (10.31 weeks).


## Program Performance Analysis

Across 300 patients in three programs (Peptides, Testosterone, Weight Loss), retention rates range from 71.43% to 77.32%. Weight Loss has the best retention and lowest churn, while Testosterone and Peptides both show churn rates above the 25% risk threshold and are flagged as high-churn programs. All programs show drop-off concentrated in early and mid-stage treatment, with no late-stage drop-off recorded anywhere.

**Priority Programs**

* Testosterone: High priority
  - Highest churn rate at 28.57%, flagged as high churn
  - Longest average treatment duration at 28.22 weeks, which may contribute to fatigue or disengagement
  - Largest number of mid-stage drop-offs (14 patients), second only to early-stage (18 patients)
  - Lowest retention rate among the three programs at 71.43%
* Peptides: Medium priority
  - Second-highest churn rate at 26.37%, flagged as high churn
  - Early-stage drop-off is heavily concentrated (16 of 24 churned patients, 66.7%), suggesting early engagement issues
  - Shortest average treatment duration at 10.31 weeks
* Weight Loss: Low priority
  - Highest retention rate at 77.32% and lowest churn rate at 22.68%, within normal range
  - No anomalies flagged for this program
  - Still shows early and mid-stage drop-off in equal measure (11 each), worth monitoring but not urgent

**Key Patterns**

* Early-stage drop-off is the most common exit point across all programs, with no late-stage drop-offs recorded.
  Evidence: Peptides: 16 early vs 8 mid vs 0 late; Testosterone: 18 early vs 14 mid vs 0 late; Weight Loss: 11 early vs 11 mid vs 0 late (equal split).
* Longer average treatment duration correlates with higher churn.
  Evidence: Testosterone has the longest average duration (28.22 weeks) and the highest churn rate (28.57%), while Peptides has the shortest duration (10.31 weeks) but still a high churn rate (26.37%), suggesting duration alone doesn't fully explain churn.
* Weight Loss shows the most balanced drop-off pattern and lowest churn.
  Evidence: Weight Loss has an even split between early (11) and mid-stage (11) drop-offs and the lowest churn rate at 22.68%, which is below the 25% risk threshold.


## Patient Segmentation Analysis

Across 300 patients in three programs (Peptides: 91, Testosterone: 112, Weight Loss: 97), Weight Loss shows the strongest retention (77.32%) while Testosterone shows the weakest (71.43%) and the highest churn rate (28.57%). Two of the three programs (Peptides and Testosterone) exceed the 25% churn risk threshold, while Weight Loss remains within normal churn levels. Drop-off in all programs is concentrated in early and mid-stage treatment, with zero late-stage drop-offs recorded anywhere in the dataset.

**Patient Segments Identified**

* Early-stage drop-off dominates in Peptides
  16 of 24 churned Peptides patients (about 67%) left in the early stage versus 8 in mid-stage; average duration is only 10.31 weeks, the shortest of all programs.
* Longer treatment duration but still high churn in Testosterone
  Testosterone has the longest average treatment duration (28.22 weeks, median 25.5) yet the highest churn rate (28.57%) and highest raw churn count (32 patients), split fairly evenly between early (18) and mid-stage (14) drop-off.
* Balanced drop-off timing with best overall retention in Weight Loss
  Weight Loss shows an even split between early (11) and mid-stage (11) drop-offs, with the highest retention rate (77.32%) and a churn rate (22.68%) that is not flagged as anomalous.
* No late-stage drop-off in any program
  All three programs report 0 late-stage drop-off patients, meaning patients who stay past the early/mid stages tend to complete or remain active rather than churn late.


## Retention and Drop-Off Analysis

Across 300 patients in three programs (Peptides, Testosterone, Weight Loss), retention rates range from 71.4% to 77.3%, averaging about 74.1%. Drop-off happens almost entirely in the early and mid stages of treatment across all programs, with no late-stage drop-offs recorded anywhere in the dataset.

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

Anomaly detection was run across 300 patient records spanning three programs (Peptides, Testosterone, Weight Loss). No statistical outliers were found in treatment duration using the IQR method for any program. However, two programs exceeded the 25% churn rate risk threshold: Testosterone (28.57%) and Peptides (26.37%). Weight Loss remained within normal churn levels at 22.68%.

**Risk Factors Identified**

* Churn rate above 25% threshold
  Frequency: 2 of 3 programs flagged (66.7%)
  Affected programs: Testosterone, Peptides
* Absence of duration outliers
  Frequency: 3 of 3 programs (100%) show no flagged duration anomalies
  Affected programs: Peptides, Testosterone, Weight Loss

**Key Concerns**

* Testosterone has the highest churn rate (28.57%) among all programs, exceeding the risk threshold.
* Peptides also exceeds the 25% churn threshold at 26.37%, indicating a shared retention challenge with Testosterone.
* Two out of three programs (66.7%) are flagged for high churn, suggesting churn may be a broader pattern rather than isolated to one program.
* No duration-based anomalies were found in any program, so the primary risk driver identified in this analysis is churn rate, not treatment length irregularities.


## Top Priority Recommendations

* Prioritize retention intervention for Testosterone: investigate drivers of disengagement given its highest churn (28.57%), lowest retention (71.43%), and largest churned count (32 patients) despite the longest treatment duration.
* Strengthen early-stage engagement for Peptides: since 67% of churned patients leave early within a short 10.31-week average duration, focus on onboarding and early check-ins to reduce the 26.37% churn rate.
* Target retention efforts on the early-to-mid treatment window across all programs, since no late-stage drop-off occurs anywhere — this is where interventions will have the most measurable impact.
* Maintain current approach for Weight Loss (77.32% retention, 22.68% churn, no anomalies) with routine monitoring only, and consider studying its balanced drop-off pattern as a model for the other two programs.
* Treat churn rate, rather than treatment duration, as the primary risk metric going forward, since no program showed duration-based statistical outliers.


## Cross-Cutting Insights

* All four analyses independently converge on the same two flagged programs (Testosterone, Peptides) for high churn, and the same unflagged program (Weight Loss) — confirming consistency across performance, segmentation, retention, and anomaly perspectives.
* The universal absence of late-stage drop-off (confirmed in all four reports) reframes the retention problem as an early/mid-stage engagement issue rather than a long-term attrition issue.
* Testosterone's paradox — longest treatment duration yet highest churn and largest raw churned count (32 patients) — appears consistently across performance, segmentation, and retention reports, suggesting duration itself is not protective against disengagement.
* Peptides' short duration (10.31 weeks) paired with a 67% early-stage churn concentration links directly to onboarding/early-engagement risk, a theme repeated in performance, segmentation, and retention analyses.
* No program shows duration-based anomalies (per anomaly detection), reinforcing that churn rate — not irregular treatment length — is the dataset's central risk signal.


---

Report generated by Multi-Agent Healthcare Analytics System on 2026-07-07 14:15:46