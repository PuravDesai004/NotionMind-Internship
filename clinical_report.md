# Clinical Insights Report

Generated: July 11, 2026 at 13:25


## Executive Summary

Across 300 patients in three programs, overall retention averages ~74%. Weight Loss is the strongest and most stable program (77.32% retention, 22.68% churn, within normal range). Testosterone and Peptides both exceed the 25% churn risk threshold (28.57% and 26.37% respectively) and are flagged as high-churn programs by all four analyses. Testosterone is the top-priority program due to its combination of highest churn rate, largest patient base (112, 32 churned), and longest average treatment duration (28.22 weeks). Across all programs, drop-off is concentrated in early and mid treatment stages, with zero late-stage attrition recorded anywhere - suggesting the early-to-mid window is where retention interventions would have the most impact. No statistical outliers in treatment duration were found in any program, indicating churn is not linked to unusually short or long treatment lengths.


## Program Performance Analysis

The dataset covers 300 patients across three programs: Peptides (91 patients), Testosterone (112 patients), and Weight Loss (97 patients). Weight Loss has the best retention (77.32%) and normal churn levels, while Peptides and Testosterone both show high churn rates that exceed the 25% risk threshold. Testosterone has the longest average treatment duration (28.22 weeks) and the highest churn rate (28.57%), making it the program needing the most attention.

**Priority Programs**

* Testosterone: High priority
  - Lowest retention rate (71.43%) among all programs
  - Highest churn rate (28.57%), flagged as high churn
  - Largest patient base (112) meaning highest absolute number of churned patients (32)
  - Longest average treatment duration (28.22 weeks), which may correlate with drop-off risk
  - 18 early-stage and 14 mid-stage drop-offs, the highest raw drop-off counts across programs
* Peptides: Medium priority
  - Churn rate of 26.37% flagged as high, exceeding the 25% threshold
  - 24 patients churned out of 91, with drop-off concentrated early (16 early vs 8 mid)
* Weight Loss: Low priority
  - Highest retention rate (77.32%) and churn rate (22.68%) within normal levels, not flagged as anomalous

**Key Patterns**

* Longer average treatment duration is associated with higher churn
  Evidence: Testosterone has the longest average duration (28.22 weeks) and the highest churn rate (28.57%), while Peptides has the shortest duration (10.31 weeks) but still shows high churn (26.37%), suggesting duration alone isn't the only driver.
* Early-stage drop-off is the most common exit point across all programs
  Evidence: Peptides: 16 early-stage vs 8 mid-stage drop-offs. Testosterone: 18 early-stage vs 14 mid-stage. Weight Loss: 11 early vs 11 mid (evenly split). No program shows late-stage drop-off.
* Weight Loss stands out as the most stable program
  Evidence: Highest retention rate (77.32%), lowest churn rate (22.68%), and the only program not flagged for high churn.


## Patient Segmentation Analysis

Across 300 patients in three programs (Peptides, Testosterone, Weight Loss), retention rates range from 71.43% to 77.32%. Testosterone and Peptides both show churn rates above the 25% risk threshold, while Weight Loss remains just under it. Drop-off in all three programs is concentrated in early and mid stages, with no late-stage attrition recorded anywhere.

**Patient Segments Identified**

* Early-stage drop-off dominates over mid-stage drop-off
  Peptides: 16 early vs 8 mid drop-offs (67% of churned patients leave early). Testosterone: 18 early vs 14 mid. Weight Loss: 11 early vs 11 mid (evenly split). No program shows late-stage churn.
* Shorter average treatment duration correlates with heavier early-stage churn
  Peptides has the shortest average duration (10.31 weeks) and the most early-skewed drop-off ratio (67% early). Testosterone has the longest duration (28.22 weeks) but still has 18 early-stage drop-offs, the highest raw count of any program.
* Higher churn rate paired with larger patient volume increases total attrition impact
  Testosterone has the most patients (112) and the highest churn rate (28.57%), producing the largest absolute churned group (32 patients) among all programs.


## Retention and Drop-Off Analysis

Across the three programs (Peptides, Testosterone, Weight Loss), average retention sits at about 74.1%, meaning roughly 1 in 4 patients drop off before finishing treatment. Retention ranges from 71.43% (Testosterone) to 77.32% (Weight Loss). Drop-offs across all programs happen almost exclusively in the early and mid stages of treatment, with zero late-stage drop-offs recorded in any program - suggesting patients who make it past the mid-point tend to stay through completion.

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

Anomaly detection across 300 patient records in 3 programs found no statistical outliers in treatment duration, but 2 of the 3 programs (Peptides and Testosterone) exceed the 25% churn rate risk threshold.

**Risk Factors Identified**

* Churn rate exceeding 25% threshold
  Frequency: 2 of 3 programs (66.7%)
  Affected programs: Peptides, Testosterone

**Key Concerns**

* Testosterone and Peptides programs both exceed the 25% churn rate risk threshold, indicating a pattern of high patient drop-off in these two programs
* No treatment duration outliers were detected in any program, so the churn issue does not appear linked to unusually short or long treatment lengths based on this data alone
* Weight Loss is the only program currently within normal churn levels


## Top Priority Recommendations

* Prioritize retention interventions for Testosterone: it has the highest churn rate (28.57%), largest patient base, and greatest absolute number of churned patients (32) - the biggest opportunity for impact
* Investigate and address early-stage onboarding/engagement issues across all programs, since early-stage drop-off is the dominant exit point (especially pronounced in Peptides at 67% and Testosterone at 56%), while no late-stage drop-off occurs
* Apply targeted retention efforts specifically to Peptides given its short average treatment duration (10.31 weeks) paired with high churn (26.37%), suggesting patients disengage very quickly after starting
* Use Weight Loss's even early/mid drop-off distribution and normal churn levels as a benchmark model - examine what retention practices in this program could be adapted for Peptides and Testosterone
* Continue monitoring treatment duration even though no statistical outliers were found, since duration alone does not explain churn (Peptides has short duration with high churn; Testosterone has long duration with high churn) - other factors likely drive attrition


## Cross-Cutting Insights

* The high-churn flag on Testosterone and Peptides is consistently confirmed across program performance, segmentation, retention, and anomaly detection analyses - a robust, cross-validated finding
* Early-stage drop-off concentration (seen in segmentation and retention analyses) directly explains why Peptides and Testosterone rank as high-priority in program performance despite differing treatment durations (10.31 vs 28.22 weeks) - duration alone does not drive churn
* Weight Loss's uniquely even early/mid drop-off split (vs. early-skewed patterns elsewhere) aligns with its status as the only program with normal churn and no anomaly flags, reinforcing its relative stability
* Testosterone's combination of largest patient volume, longest duration, and highest churn rate compounds its risk profile, making it an outlier in absolute impact even though no duration-based statistical anomaly was detected


---

Report generated by Multi-Agent Healthcare Analytics System on 2026-07-11 13:25:31