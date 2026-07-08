# Clinical Insights Report

Generated: July 04, 2026 at 12:01


## Executive Summary

Analysis of 300 patients across three programs (Peptides n=91, Testosterone n=112, Weight Loss n=97) shows retention ranging from 71.43% to 77.32% (average ~74.1%). Testosterone is the weakest performer and highest priority, combining the highest churn rate (28.57%), lowest retention (71.43%), largest patient population, and the longest and most variable treatment duration. Peptides is a secondary concern with churn at 26.37% and the shortest, most front-loaded drop-off pattern. Weight Loss is the strongest program (77.32% retention, 22.68% churn) with no flags. All programs show drop-off concentrated in early/mid stages with zero late-stage churn, and no statistically significant duration outliers were detected via IQR analysis in any program.


## Program Performance Analysis

Across 300 patients in three programs, Weight Loss has the best retention (77.32%), followed by Peptides (73.63%), and Testosterone has the weakest retention (71.43%) despite having the largest enrollment (112 patients) and the longest average treatment duration (28.22 weeks).

**Priority Programs**

* Testosterone: High priority
  - Lowest retention rate at 71.43%
  - Highest churn rate at 28.57% (32 of 112 patients churned)
  - Largest patient population (112), so churn impacts the most people in absolute terms
  - Longest average treatment duration (28.22 weeks), which may be linked to higher drop-off
* Peptides: Medium priority
  - Second-highest churn rate at 26.37% (24 of 91 patients)
  - Shortest average treatment duration (10.31 weeks), which is notably lower than the other two programs and worth monitoring
* Weight Loss: Low priority
  - Highest retention rate (77.32%) and lowest churn rate (22.68%) among the three programs
  - No immediate performance concerns based on current data

**Key Patterns**

* Longer average treatment duration is associated with higher churn
  Evidence: Testosterone has the longest average duration (28.22 weeks) and the highest churn rate (28.57%), while Peptides has the shortest duration (10.31 weeks) and a lower churn rate (26.37%).
* Weight Loss shows the most balanced performance
  Evidence: Weight Loss has a mid-range duration (16.47 weeks), the lowest churn rate (22.68%), and the highest retention rate (77.32%) among the three programs.
* All programs have retention rates within a fairly narrow band
  Evidence: Retention rates range from 71.43% to 77.32%, a spread of under 6 percentage points, meaning no program is catastrophically underperforming but Testosterone consistently trails the others.


## Patient Segmentation Analysis

The dataset covers 300 patients across three programs: Peptides (91 patients), Testosterone (112 patients), and Weight Loss (97 patients). Retention rates range from 71.43% to 77.32%, with Testosterone and Peptides both flagged for high churn (over the 25% threshold), while Weight Loss remains within normal churn levels. No late-stage drop-offs were recorded in any program, meaning all observed attrition happens in the early or mid stages of treatment.

**Patient Segments Identified**

* All programs show early or mid-stage drop-off only, with zero late-stage churn recorded
  Peptides: 16 early / 8 mid / 0 late; Testosterone: 18 early / 14 mid / 0 late; Weight Loss: 11 early / 11 mid / 0 late
* Peptides has the shortest average treatment duration and the most front-loaded drop-off (early stage roughly double mid stage)
  Average duration 10.31 weeks; 16 early-stage drop-offs vs 8 mid-stage
* Testosterone has the longest average treatment duration but also the highest churn rate and largest volume of both early and mid-stage drop-offs
  Average duration 28.22 weeks; churn rate 28.57%; 18 early + 14 mid-stage drop-offs (32 total churned)
* Weight Loss shows the most balanced drop-off distribution and best retention performance
  Retention rate 77.32%; churn rate 22.68% (not flagged); 11 early and 11 mid-stage drop-offs evenly split


## Retention and Drop-Off Analysis

Across the three programs (Peptides, Testosterone, Weight Loss), retention rates range from 71.43% to 77.32%, with an average retention rate of about 74.1%. All programs show drop-offs concentrated in early and mid-stage treatment, with zero late-stage drop-offs recorded in any program, meaning patients who make it past the mid-point tend to stay through completion.


## Anomalies and Risk Factors

Anomaly detection was run across 300 patient records spanning three programs: Peptides, Testosterone, and Weight Loss. No statistically abnormal treatment duration outliers were found in any program using the IQR method. However, two programs (Peptides and Testosterone) exceed the 25% churn rate risk threshold, while Weight Loss remains within normal churn levels.

**Risk Factors Identified**

* High churn rate above 25% threshold
  Frequency: 2 of 3 programs (66.7%)
  Affected programs: Peptides, Testosterone
* Treatment duration outliers
  Frequency: 0 of 3 programs (0%) - not observed in current data
  Affected programs: 

**Key Concerns**

* Testosterone has the highest churn rate at 28.57%, exceeding the risk threshold and warranting close monitoring.
* Peptides also exceeds the churn risk threshold at 26.37%, indicating retention challenges alongside Testosterone.
* No program shows treatment duration outliers, suggesting the churn issue is not linked to unusually short treatment lengths based on this analysis alone.


## Top Priority Recommendations

* Prioritize intervention in the Testosterone program given its combination of highest churn (28.57%), lowest retention (71.43%), largest patient base (112), and widest duration variability — the greatest absolute and relative impact.
* Implement early-stage engagement initiatives (e.g., onboarding check-ins, early follow-up) across all programs, with emphasis on Peptides and Testosterone where early drop-off is most concentrated.
* Investigate the specific drivers of Peptides' early attrition despite its short program length, to determine if onboarding or expectation-setting issues are causing rapid disengagement.
* Examine Testosterone's wide treatment duration spread (14–46 weeks) to identify whether inconsistent care pathways or patient journeys contribute to churn, and standardize where appropriate.
* Use Weight Loss's balanced drop-off distribution and strong retention (77.32%) as a benchmark model to inform improvements in the other two programs.
* Since no late-stage churn occurs in any program, focus retention resources on the early-to-mid stage transition point rather than late-stage retention efforts.


## Cross-Cutting Insights

* Testosterone is flagged as the highest-risk program across every analysis (performance, segmentation, retention, anomaly) — the combination of largest enrollment, highest churn, lowest retention, and widest duration variability makes it the clear top priority.
* Early-stage drop-off is a cross-program vulnerability, but it is most severe in the two flagged high-churn programs (Peptides and Testosterone), suggesting the start of treatment is the critical intervention window.
* Peptides presents a paradox: despite having the shortest average treatment duration, it still exceeds the churn threshold, with early-stage drop-off nearly double mid-stage — suggesting disengagement happens very soon after enrollment rather than being duration-driven.
* The absence of late-stage churn across all programs, combined with concentrated early/mid drop-off, indicates retention efforts should focus on the first half of the treatment journey rather than the tail end.
* Testosterone's long average duration combined with high churn (rather than short duration driving churn, as seen in Peptides) suggests different underlying drivers per program, despite both exceeding the same churn threshold.


---

Report generated by Multi-Agent Healthcare Analytics System on 2026-07-04 12:01:23