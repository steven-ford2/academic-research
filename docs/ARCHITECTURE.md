# ResearchOS architecture specification

## Mission
Build a reusable research engineering platform for empirical papers, narrative and systematic reviews, meta-analyses, grant applications, journal intelligence, and eventually PsychoPy/Unity experiments. Scientific inference remains investigator-led. **This document defines a target architecture, not a claim that every component is implemented.**

## Shared layers
1. **Portfolio/control plane:** research charters, decisions, approvals, status, dated project handoffs.
2. **Literature acquisition:** OpenAlex/Crossref/Semantic Scholar and licensed discipline databases, Zotero/BibTeX, DOI validation, full-text permissions, citations and retractions, reproducible search logs.
3. **Evidence knowledge:** canonical identifiers, source/version hashes, locators, claim/evidence links, contradictory findings, study designs and effect estimates.
4. **Empirical/statistical:** immutable raw data, derived parquet artifacts with manifests, R/renv/targets and Python, estimands, diagnostics, multilevel inference, grouped validation, power, sensitivity.
5. **Output builders:** Quarto manuscript/supplementary materials, publisher-specific requirements, reproducible tables, figures, references, checklists.
6. **Review/meta-analysis:** predeclared protocol, independent eligibility screening, double-checked extraction, bias assessment, dependent-effect modeling, PRISMA.
7. **Grant intelligence:** opportunity/funder database, aims, feasibility, resources, timelines, risks, sponsor policy and human approvals.
8. **Experiment design:** protocol-to-code, PsychoPy/Unity XR, calibration/timing/event logging, simulation tests and instrument integrity.
9. **Quality & security:** source verification, independent analysis, targeted adversarial peer review, policy snapshots, hard fail-closed release gates.

## Boundaries
- GitHub hosts code, redacted public evidence records, docs and approved releases.
- Zotero maintains authoritative reference metadata and authorized PDFs.
- Approved data vault stores actual restricted material; manifests carry checksums and access instructions.
- No assertion that automatic citation or manuscript output is scientifically verified.
- ChatGPT Work may coordinate legitimate tasks; Codex handles reproducible code/build/test. External connectors require access review.

## Workflow
Charter → search and provenance → evidence synthesis → methods/estimands → reproducible execution → scientific argument → journal/grant fit → independent review → PI-approved release.

## Required provenance fields
`source_id`, `identifier`, `title`, `source_type`, `version`, `license/access`, `source_locator`, `extraction_method`, `verified_by`, `verified_utc`, `verification_status`.

## Non-negotiable scientific distinctions
Association ≠ causation; statistical significance ≠ predictive value; AIC/likelihood support ≠ external validation; high fit with random intercepts ≠ generalization to new participants/interfaces; metadata verification ≠ claim-content verification.
