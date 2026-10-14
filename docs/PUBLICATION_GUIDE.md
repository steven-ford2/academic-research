# Publication and collaboration guide

Remote repository: https://github.com/steven-ford2/academic-research
Visibility: **public by temporary owner direction (2026-10-14)**. Switch to private before including any nonpublic material.

## Local install
```bash
git clone https://github.com/steven-ford2/academic-research.git
cd academic-research
python -m venv .venv
python -m pip install -e '.[dev]'
pytest -q
researchos status
```

## Source of truth
GitHub records code, configs, literature metadata, evidence ledgers, protocols and *approved* public-facing artifacts. Restrict participant data and research instruments separately.

## Codex
Connect this repository to Codex and open a narrow issue. Instruct Codex to follow AGENTS.md and work on a branch with tests and review artifacts. Merge only after scientific and engineering verification.

## Final release
Use the journal/funder's official instructions, verify their recency, obtain coauthor and institutional approvals, and block actual submission until all source/evidence/results checks and independent scientific review have been completed.
