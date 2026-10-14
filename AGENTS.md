# Codex / AI agent operating instructions

Applies across the entire Academic Research repository. Read README.md, docs/ARCHITECTURE.md, docs/QUALITY_GATES.md, docs/IMPLEMENTATION_STATUS.md, and the project protocol before changes.

## Core contract
- Treat correctness and provenance as hard release blockers, not aesthetics.
- Preserve raw sources. Transform into reproducible derived products with hashes, scripts, logs, and versioned decisions.
- Distinguish confirmed empirical findings, source statements, speculation, and proposed research.
- Never fabricate quotations, citations, DOI, effect sizes, journal policies, editors, or reviewer identities.
- Never call in-sample AIC superiority proof of out-of-sample predictive accuracy.
- For repeated measures, verify the outcome's actual observation unit; prevent participant, task, or interface leakage in cross-validation.
- Run independent statistical diagnostics, baseline comparisons, sensitivity checks, and validation appropriate for each estimand.
- Review source content directly before declaring that a citation supports a claim.
- Do not infer permission for unrestricted AI writing from the availability of AI tools. Respect journal/funder policies; research interpretation and scientific authorship belong to the investigator.
- Document all adverse and null findings, sensitivity failures, and material limitations; do not optimize toward significance.
- Never push raw participant data, unpublished manuscripts, restricted materials, credentials, proprietary employer information, CUI or export-controlled material to this public repository or any unapproved AI service.

## Workflow
1. Identify the governing research protocol, ethical constraints, and desired acceptance tests.
2. Propose the smallest auditable change, implement it on a dedicated branch, and preserve provenance.
3. Write or update unit tests, data quality checks, and documentation.
4. Run tests and include the actual command/result or honestly record that execution was not possible.
5. Open a reviewable PR with scientific assumptions, decisions requested from PI, risks, and blockers.
6. Do not submit manuscripts, grants, register protocols, upload restricted datasets, or represent human approval without explicit authority.

## Scientific release gates
- verified sources and claim-level citation support
- reproduced, checked numerical results and complete analytical provenance
- documented uncertainty, confounds, sensitivity analyses and negative evidence
- independent expert review of consequential methodology and conclusions
- current journal/funder policies and author approval

## First study
Ford (2025) Experiment 2 reconstructed mouse trajectories from recorded videos after logging failure; its inferred clicks are a navigation proxy. Experiment 3 reports fixation count strongly correlated with task time (approximately r=.94). Independently audit both before asserting marker specificity or predictive generalizability.

Never describe CI passing as scientific peer review.
