# Empirical statistical pipeline

## Intended stages
Data governance → manifest/checksum → data dictionary and instrument scoring → frozen transformation → estimands → original-model reproduction → diagnostics → independent sensitivity analysis → grouped cross-validation where prediction is claimed → reproducible tables and plots → independent scientific signoff.

Preferred stack: R (lme4, ordinal, glmmTMB, DHARMa, emmeans, marginaleffects, performance), renv/targets; Python (pandas, numpy, scipy, statsmodels, scikit-learn) as appropriate.

Always establish measurement units, sampling designs, cluster/dependency structures, missingness, hypotheses and exclusion rules. Comparisons between models must respect valid likelihood contexts; AIC does not show generalization. Preserve null results.

**Status:** documented target; no original dissertation reanalysis has been run.
