# Codex first implementation sprint

Use this document to hand a bounded, auditable wave of work to Codex. The repository exists and its initial foundation GitHub Actions workflow passed on 2026-10-14. **Green CI does not verify science.**

## Recommended setup

1. Clone `https://github.com/steven-ford2/academic-research`.
2. Install Python >= 3.10 and package with `pip install -e '.[dev]'`.
3. Run `pytest -q` and `researchos status`.
4. Work in new branches with pull requests; maintain all acceptance evidence.
5. Do not fetch original participant datasets or unpublished manuscripts into the current public repository.
6. If work requires restricted source material, stop and request a private approved storage path and access review.

## Paste this request into Codex

> Work on the `academic-research` repository and follow `AGENTS.md` without exceptions.
>
> **Mission:** Complete the next verifiable increment of the ResearchOS platform, prioritizing scientific validity over feature count. Begin with `docs/issues/01-foundation.md`, `docs/issues/02-literature.md`, and `docs/issues/03-statistics.md`. Do not claim those work packages are complete unless all acceptance criteria and negative controls are demonstrated.
>
> **First pass:** inventory the repository, run tests, identify unimplemented requirements and quality defects, and write a short implementation design in `docs/`. Prefer simple composable modules over an opaque multi-agent system.
>
> **Implement:** structured schema validation for evidence and manuscript claim provenance; deterministic bibliographic normalization and DOI deduplication with synthetic fixtures; a documented research search-log schema; a reproducible R analysis project template with codebook, dataset checksum checks, environment lockfile pattern, and target-aware grouped cross-validation demonstrations. Implement only functions that can be correctly tested in this sprint.
>
> **Validation:** build positive and adversarial tests (fabricated or mismatched citations, duplicate DOIs, missing locators, repeated-measures data leakage, invalid journal profile dates, accidental restricted-file additions). Preserve deliberately failing scientific release gates while ensuring foundation CI passes.
>
> **Documentation:** update roadmap and status with exact implemented and nonimplemented functionality, current assumptions, decisions requiring PI approval, security implications, tests executed, and residual risks. Do not invent research results, current journal policies or scientific evidence.
>
> **Deliver:** one or more reviewed pull requests with test commands and output, a reproducible demo on synthetic data, and a concise prioritized next-sprint plan. Never publish new data, submit a manuscript or generate grant scientific prose without investigator authorization.

## After the first sprint

The investigator should review the PR with specific attention to statistical dependence, model assumptions, false-positive verification flags, external API rights, and security. Then move to the original dissertation data inventory in issue #4 only after deciding on approved private storage and author permissions.

Use the [issue tracker](https://github.com/steven-ford2/academic-research/issues) as the progress ledger, not chat history.
