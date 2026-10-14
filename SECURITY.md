# Research data governance

**Public-repository phase authorized 2026-10-14.** This is temporary. Change repository visibility to private before introducing nonpublic manuscripts or analyses.

Do not commit:
- Participant-level raw/derived data, recordings, gaze logs, identifiers, consent forms or IRB-limited materials without an explicit approved release determination.
- Employer, proprietary, ITAR, EAR, export-controlled, CUI, classified, defense program, or contractual information.
- API keys, tokens, secrets, unlicensed copyrighted full-text collections, author email correspondence, or unapproved drafts.
- Research data containing identifiers in comments, notebooks, figures, logs, metadata, or file names.

Use approved storage with access controls; commit only redacted manifests, public protocols, synthetic fixtures, hashes, analysis code and permissible publication outputs. Public dissertation reference: https://stars.library.ucf.edu/etd2024/445/. Never treat Git history deletion as adequate remediation after accidental disclosure.

Prohibit auto-publishing from AI agents. Require investigator authorization before public release. Scan diffs and history for secrets, PII, and unusual binary assets.
