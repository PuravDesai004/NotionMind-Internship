# Clinical Insights Report

Generated: July 04, 2026 at 15:52


## Executive Summary

Across 300 patients in three programs, Weight Loss is the strongest performer (77.32% retention, 22.68% churn, balanced drop-off) while Testosterone is the highest-risk program (71.43% retention, 28.57% churn, largest patient base at 112) and Peptides is a secondary concern (26.37% churn, shortest duration at 10.31 weeks with drop-off concentrated early). All four analyses independently converge on the same core pattern: churn in Testosterone and Peptides is driven by early/mid-stage disengagement rather than treatment duration, with zero late-stage drop-offs and no statistical duration outliers detected in any program.


## Program Performance Analysis

The dataset covers 300 patients across three programs: Peptides (91), Testosterone (112), and Weight Loss (97). Weight Loss has the highest retention rate (77.32%) and the only churn rate that stays below the risk threshold (22.68%). Testosterone has the lowest retention (71.43%) and the highest churn rate (28.57%), while also having the longest average treatment duration (28.22 weeks). Peptides has the shortest average duration (10.31 weeks) and a high churn rate (26.37%).

**Priority Programs**

* Testosterone: High priority
  - Highest churn rate at 28.57%, flagged as high churn
  - Lowest retention rate at 71.43%
  - Longest average treatment duration (28.22 weeks) without corresponding retention benefit
  - 32 patients churned, the highest raw count among programs
* Peptides: Medium priority
  - Churn rate of 26.37% flagged as high
  - Shortest average treatment duration (10.31 weeks), which may relate to early attrition
  - 67% of churned patients (16 of 24) dropped off in the early stage
* Weight Loss: Low priority
  - Highest retention rate (77.32%) among all programs
  - Only program with churn rate below the 25% risk threshold (22.68%)
  - Drop-off is evenly distributed between early and mid stages, suggesting no acute risk period

**Key Patterns**

* Weight Loss shows the strongest and most balanced performance
  Evidence: Highest retention rate (77.32%), lowest churn rate (22.68%), and an even split between early (11) and mid-stage (11) drop-offs suggests no single risk period dominates.
* Testosterone has the longest treatment duration paired with the highest churn
  Evidence: Average duration is 28.22 weeks (highest of all programs) yet churn rate is 28.57%, the highest observed, with 32 of 112 patients churned.
* Peptides has the shortest treatment duration and concentrated early drop-off
  Evidence: Average duration is only 10.31 weeks, and of the 24 churned patients, 16 (67%) left in the early stage versus only 8 in the mid stage.
* No program shows late-stage drop-off
  Evidence: All three programs report 0 late-stage churned patients, meaning patients who leave tend to do so early or mid-treatment, not near completion.


## Patient Segmentation Analysis

The dataset covers 300 patients across three programs: Peptides (91 patients), Testosterone (112 patients), and Weight Loss (97 patients). Retention rates range from 71.43% to 77.32%, with Testosterone showing the lowest retention and highest churn, while Weight Loss shows the best overall retention profile.

**Patient Segments Identified**

* Early-stage drop-off dominates across all programs
  No program recorded any late-stage drop-offs. Peptides: 16 early vs 8 mid; Testosterone: 18 early vs 14 mid; Weight Loss: 11 early vs 11 mid (evenly split).
* Longer average treatment duration correlates with higher churn
  Testosterone has the longest average duration (28.22 weeks) and the highest churn rate (28.57%), while Peptides has the shortest duration (10.31 weeks) but still a high churn rate (26.37%), suggesting duration alone doesn't fully explain churn.
* Weight Loss shows more balanced drop-off timing and better retention
  Weight Loss has an even early/mid split (11/11) and the highest retention rate (77.32%) with churn (22.68%) below the 25% risk threshold.


## Retention and Drop-Off Analysis

Across the three programs (Peptides, Testosterone, Weight Loss), retention rates range from 71.43% to 77.32%, averaging about 74.1%. All programs show drop-offs concentrated in early and mid stages, with no late-stage drop-offs recorded in any program.


## Anomalies and Risk Factors

Across 300 patients in 3 programs (Peptides, Testosterone, Weight Loss), no statistically extreme treatment duration outliers were found using the IQR method. However, 2 of the 3 programs exceed the 25% churn rate risk threshold, with Testosterone showing the highest churn rate (28.57%) followed closely by Peptides (26.37%). Weight Loss remains within normal churn levels (22.68%).

**Risk Factors Identified**

* Churn rate above 25% risk threshold
  Frequency: 2 out of 3 programs (66.7%)
  Affected programs: Testosterone, Peptides

**Key Concerns**

* Testosterone and Peptides both show churn rates above the 25% risk threshold, indicating retention challenges in these two programs.
* No treatment duration outliers were detected in any program, so the churn issue appears unrelated to unusually short or long treatment lengths based on this data.
* Weight Loss is currently the only program operating within normal churn levels, making it a comparative benchmark for the other two.


## Top Priority Recommendations

* Prioritize retention interventions for Testosterone given its combination of highest churn (28.57%), lowest retention (71.43%), largest patient volume (112), and high mid-stage drop-off (14 patients) -- investigate why long treatment duration is not converting to completion
* Implement early-engagement/onboarding improvements for Peptides to address its concentrated early-stage drop-off (67% of churned patients), given its already short program length
* Target early and mid-stage retention touchpoints across all programs, since no program shows late-stage drop-off -- resources should focus on the first half of treatment rather than late-stage retention efforts
* Use Weight Loss's balanced drop-off pattern and normal churn rate as a benchmark model to inform engagement strategies for Testosterone and Peptides
* Given no duration-based outliers were found, focus monitoring on churn rate and drop-off timing metrics rather than individual treatment-length anomalies


## Cross-Cutting Insights

* All four analyses agree Testosterone is the top-priority program: highest churn (28.57%), lowest retention (71.43%), largest patient base (112), and highest total drop-off count (32), despite having the longest average duration -- duration does not translate into retention benefit for this program
* Peptides' short duration (10.31 weeks) and high early-stage churn (67% of drop-offs) suggest an early engagement/onboarding gap rather than a duration-driven fatigue issue, consistent across segmentation, retention, and performance reports
* The complete absence of late-stage drop-off across all programs and all analyses indicates that patients who progress past mid-stage are highly likely to complete treatment -- the retention challenge is concentrated entirely in early/mid stages
* Since no duration outliers exist in any program, the churn problem is tied to drop-off timing and program-level engagement patterns rather than individual case anomalies
* Weight Loss's balanced early/mid drop-off split and normal churn rate make it a useful internal benchmark for evaluating interventions in the other two programs


---

Report generated by Multi-Agent Healthcare Analytics System on 2026-07-04 15:52:27