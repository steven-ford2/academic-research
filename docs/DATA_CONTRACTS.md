# Data and provenance contracts

## Literature sources
`source_id` stable; `doi` optional but syntax-checked; `title`, `authors`, `year`, `venue`, `version`, `retrieval_utc`, `access_rights`, `pdf_sha256` if lawfully possessed. Never treat a metadata-only record as a read full text.

## Claims
JSON array of objects: `id` (unique), `claim`, `verification_status` in [unverified, located, checked, disputed, retracted], `sources[]` with `document_id`, `locator`, `verification_method`. Additional fields: `extraction_note`, `contradictory_source_ids`, `checked_by`, `checked_at`, `statistical_reproduction_id`.

## Journal profiles
YAML fields: `journal`, `article_type`, `official_instructions_url`, `ai_policy_url`, `status`, `last_verified_utc`. Article-specific limits and editorial information must record official source locators and date of verification; NEVER silently adopt an old policy.

## Statistical projects
`analysis_id`, `raw_sha256`, `derived_sha256`, `code_commit`, `environment_lockfile`, `random_seed`, `unit_of_analysis`, `estimand`, `missingness`, `exclusions`, `model_formula`, `fit_diagnostics`, `validation_split_rule`, `outputs[]`, `review_status`.

## Submission artifacts
`target`, `article_type`, `policy_snapshot`, `manuscript_version`, `tables/figures`, `reference_audit`, `author_approvals`, `data_sharing_approval`, `release_gate_status`.

Do not persist PII or credentials in any of these files.
