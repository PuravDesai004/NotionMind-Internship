# Clinical Insights Report

Generated: July 31, 2026 at 14:12


## Executive Summary

Across 200 patients in three telehealth programs, overall retention is 73.5% (147 active, 53 churned). Peptides is the strongest performer (79.41% retention, 20.59% churn, not flagged), while Testosterone (67.74% retention, 32.26% churn) and Weight Loss (72.86% retention, 27.14% churn) both exceed the 25% churn-risk threshold and are flagged as high churn. Churn in Testosterone and Weight Loss is concentrated in the mid-treatment stage (and early stage for Weight Loss), unlike Peptides where drop-off skews early. No treatment-duration outliers were found in any program, indicating that churn timing and program-specific dynamics -- not unusually short treatment lengths -- drive the performance gap. Testosterone is the top-priority program, followed by Weight Loss, with Peptides serving as a low-risk baseline.


## Program Performance Analysis

Across 200 patients in three programs (Peptides, Testosterone, Weight Loss), retention varies notably. Peptides shows the strongest retention (79.41%), while Testosterone has the weakest (67.74%) and the highest churn rate (32.26%). Two of the three programs (Testosterone and Weight Loss) exceed the 25% churn risk threshold, making them priority areas for attention.

**Priority Programs**

* Testosterone: High priority
  - Highest churn rate at 32.26%, flagged as anomalous by the risk threshold check
  - Lowest retention rate among all programs at 67.74%
  - Largest share of mid-stage drop-offs (9 of 20 churned patients, 45%), suggesting patients are leaving partway through treatment rather than at the start or end
* Weight Loss: Medium priority
  - Churn rate of 27.14% exceeds the 25% risk threshold and is flagged
  - Largest enrollment (70 patients) combined with elevated churn means more patients affected in absolute terms (19 churned)
  - Drop-offs spread across early (8) and mid (9) stages, indicating retention issues begin fairly early in treatment
* Peptides: Low priority
  - Highest retention rate (79.41%) and lowest churn (20.59%), not flagged by anomaly detection
  - Drop-offs are more spread out with early stage being most common (7 of 14), a less concerning pattern than mid-stage concentration

**Key Patterns**

* Peptides has the best retention and lowest churn, with drop-offs concentrated early rather than mid-treatment.
  Evidence: Peptides: 79.41% retention, 20.59% churn (not flagged), 7 early-stage vs 3 mid-stage vs 4 late-stage drop-offs.
* Testosterone and Weight Loss both show churn rates above the 25% risk threshold, flagged as 'High churn detected'.
  Evidence: Testosterone: 32.26% churn (flagged). Weight Loss: 27.14% churn (flagged).
* Mid-stage drop-off is disproportionately common in Testosterone and Weight Loss compared to Peptides.
  Evidence: Testosterone: 9 of 20 dropped patients left mid-stage (45%). Weight Loss: 9 of 19 dropped patients left mid-stage (47%). Peptides: only 3 of 14 (21%) left mid-stage.
* Average treatment duration is fairly similar across programs (21.8 to 24.1 weeks), so duration length alone does not explain the churn differences.
  Evidence: Peptides: 21.82 weeks avg. Testosterone: 22.65 weeks avg. Weight Loss: 24.09 weeks avg.


## Patient Segmentation Analysis

The dataset covers 200 patients across three programs: Peptides (68 patients), Weight Loss (70 patients), and Testosterone (62 patients). Retention varies clearly by program, with Peptides retaining patients best (79.41%) and Testosterone retaining patients worst (67.74%). Two of the three programs, Testosterone and Weight Loss, have churn rates that exceed the 25% risk threshold, indicating broader retention concerns beyond a single program.

**Patient Segments Identified**

* Peptides has the strongest retention profile and lowest churn, with drop-off concentrated in the early stage of treatment.
  79.41% retention rate, 20.59% churn (not flagged), 68 patients with average duration 21.82 weeks. Drop-off breakdown: 7 early, 3 mid, 4 late stage patients out of 14 churned.
* Testosterone has the weakest retention profile, with churn concentrated in the mid-stage of treatment.
  67.74% retention rate (lowest of all programs), 32.26% churn (flagged as high), 62 patients. Drop-off breakdown: 5 early, 9 mid, 6 late stage patients out of 20 churned -- mid-stage is the largest group.
* Weight Loss has moderate retention but churn is roughly evenly split between early and mid-stage drop-off.
  72.86% retention rate, 27.14% churn (flagged as high), 70 patients, average duration 24.09 weeks (highest average duration among programs). Drop-off breakdown: 8 early, 9 mid, 2 late stage patients out of 19 churned.


## Retention and Drop-Off Analysis

Across all 3 programs (200 patients total: Peptides 68, Testosterone 62, Weight Loss 70), the overall retention rate is 73.5% (147 active out of 200 patients), with 53 patients having dropped off. Peptides has the best retention (79.41%), Weight Loss is in the middle (72.86%), and Testosterone has the weakest retention (67.74%) and the highest churn rate (32.26%).

**Treatment Duration Trends**

* Peptides
  Mean: 21.82 weeks, Median: 20.5 weeks, Q1: 11.75 weeks, Q3: 32.0 weeks
* Testosterone
  Mean: 22.65 weeks, Median: 19.0 weeks, Q1: 13.0 weeks, Q3: 32.75 weeks
* Weight Loss
  Mean: 24.09 weeks, Median: 26.0 weeks, Q1: 15.0 weeks, Q3: 33.0 weeks

**Drop-Off Timing by Stage**

* Peptides
  Early stage: 7 patients, Mid stage: 3 patients, Late stage: 4 patients
* Testosterone
  Early stage: 5 patients, Mid stage: 9 patients, Late stage: 6 patients
* Weight Loss
  Early stage: 8 patients, Mid stage: 9 patients, Late stage: 2 patients


## Anomalies and Risk Factors

Across the 3 telehealth programs (200 patients total), no program shows statistically abnormal treatment duration outliers using the IQR method. However, 2 of the 3 programs exceed the 25% churn rate risk threshold, making high churn the primary anomaly in this dataset.

**Risk Factors Identified**

* Churn rate above 25% threshold
  Frequency: 2 of 3 programs (66.7%)
  Affected programs: Testosterone, Weight Loss

**Key Concerns**

* Testosterone program has both the highest churn rate (32.26%) and lowest retention rate (67.74%), making it the top priority for attention.
* Weight Loss program also exceeds the churn risk threshold (27.14%) and has the highest raw count of churned patients (19).
* No program shows abnormal treatment duration patterns, meaning the anomaly concern is isolated to churn/retention rather than how long patients stay when they are in a program.


## Top Priority Recommendations

* Prioritize Testosterone for intervention: investigate causes of mid-stage disengagement (weeks/sessions where the 9-of-20 mid-stage drop-offs cluster) and pilot targeted retention outreach at that point in treatment.
* Address Weight Loss churn (27.14%, 19 patients) with early-to-mid stage check-ins, given its large patient volume and drop-off pattern concentrated before the late stage despite longer average treatment duration.
* Use Peptides' early-stage drop-off pattern and low overall churn as a benchmark/model for onboarding practices that could be adapted to the other two programs.
* Since no treatment-duration outliers exist, focus retention efforts on stage-of-treatment triggers (mid-stage check-ins, milestone engagement) rather than adjusting overall program length.
* Establish ongoing monitoring of the 25% churn threshold flag for Testosterone and Weight Loss to track whether interventions reduce churn over time.


## Cross-Cutting Insights

* The two programs flagged for high churn (Testosterone, Weight Loss) both show mid-stage drop-off as the largest or tied-largest attrition point, a pattern absent in the low-risk Peptides program (early-stage dominant) -- linking the segmentation, retention, and anomaly findings to a shared mid-treatment risk window.
* Similar average treatment durations (21.8-24.1 weeks) across all programs, combined with zero duration outliers, confirm that churn differences stem from when patients drop off within treatment rather than how long programs run.
* Weight Loss's large patient base (70) combined with flagged high churn means it has the highest absolute number of churned patients (19), even though Testosterone has the higher churn rate -- both scale and rate matter for prioritization.
* All four reports consistently rank programs identically (Peptides low-risk, Weight Loss medium-risk, Testosterone high-risk), giving high confidence in these findings; the only minor figure discrepancy is Weight Loss retention cited as both 72.86% (segmentation, retention, anomaly reports) -- used here as the confirmed, conservative figure.


---

Report generated by Multi-Agent Healthcare Analytics System on 2026-07-31 14:12:08