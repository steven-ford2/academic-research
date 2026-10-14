# Dissertation forensic research audit — Experiments 2 and 3

**Status:** required work plan, not completed independent verification.

## Inputs to inventory
- Original raw and cleaned data; analysis scripts, statistical project files, data dictionaries.
- Experimental design documents, consent/IRB and relevant research data rights.
- Video tracking reconstruction code, calibration/reference samples and error logs.
- Exact scoring of ASQ, SMEQ, SUS, USE-Lite, measurement timing, task identifiers and per-interface aggregation.
- Previously disseminated abstracts, conference proceedings, working papers and coauthor agreements.

## Experiment 2 critical threats
The dissertation describes reconstruction of mouse positions from screen video after coordinate recording failure. Inferred click counts are based on page/interface transitions. Independently examine cursor detection false positives, missed positions, interpolation, frame sampling and differential error by interface/usability condition. Treat 'inferred clicks' as a proxy, not a validated physical click count.

## Experiment 3 critical threats
Appendix B describes strong correlation (approximately r=.94) between fixation count and task time. Test incremental validity versus simple task-duration baseline, fixation rate (subject to conceptual and statistical scrutiny), and non-eye measures. Evaluate collinearity and avoid unsupported causal or cognitive specificity claims.

## Reanalysis protocol
1. Define unit of observation for each outcome, especially post-test instrument scores.
2. Recreate variable transformations, contrast coding, exclusions, model formulas and random effects.
3. Independently reproduce coefficients, CIs, p-values, marginal/conditional R-squared and AIC where meaningful.
4. Investigate convergence problems and justify alternative model structures.
5. Address repeated measures, task/site effects, multiplicity, ceiling/floor effects, missingness and outcome distributions.
6. Run relevant diagnostics and sensitivity checks.
7. For predictive language, use participant-grouped and (if intended) site-grouped cross-validation, using proper preprocessing isolation within folds and baseline comparisons.
8. Quantify uncertainty, calibration and practical importance, not only statistical significance.
9. Preserve every null/contradictory result. Produce provenance-linked figures/tables and a discrepancy register.

## Claims requiring careful distinction
- Marker association vs validated new-subject prediction.
- Usability perception vs objective interface quality.
- Time-on-task vs fixation burden as potential overlapping indicators.
- In-sample model fit vs transfer to previously unseen interface/domain.

## Gate
No journal-ready manuscript or strong predictive-validity claim until source inputs, independent analysis and peer critique are documented.
