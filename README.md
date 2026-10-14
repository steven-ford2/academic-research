# Academic Research / ResearchOS

**Status: foundational engineering scaffold (alpha); not a validated scientific production system.**

This is a provenance-first research workspace for empirical manuscripts, evidence synthesis, systematic reviews and meta-analysis, grant planning, journal intelligence, and future PsychoPy/Unity experiments. The first validation project is Ford (2025), *Digital Biomarkers of Usability*, with a proposed manuscript integrating Experiments 2 and 3.

> **Temporary public repository:** owner explicitly authorized proceeding publicly on 2026-10-14. Change GitHub visibility to **Private** before adding unpublished manuscripts, research participant data, proprietary work, or other nonpublic material. The public dissertation is referenced at https://stars.library.ucf.edu/etd2024/445/.

## Scientific operating rules

- No invented citations, source quotations, estimates, results, ethics approvals, editor identities, or journal/funder policies.
- Claims require verifiable original sources and precise locators; numerical claims require a reproducible derivation.
- Treat all agent outputs as unverified until source checked or independently computed.
- Distinguish hypotheses from results, and internal fit from prospective prediction.
- No participant-level, IRB-restricted, employer, export-controlled, CUI, classified, credential, or otherwise confidential files in this public repository.
- Journal/funder-specific AI rules control manuscript and grant text; PI retains scientific authorship and release authority.
- Passing continuous integration is not scientific certification.

## Start here

- [Codex instructions](AGENTS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Scientific quality gates](docs/QUALITY_GATES.md)
- [Implementation roadmap](docs/ROADMAP.md)
- [Implementation status](docs/IMPLEMENTATION_STATUS.md)
- [Dissertation project](projects/digital-biomarkers-usability/README.md)

## Planned command line

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
researchos status
pytest -q
```

The implemented core is deliberately small and conservative. It does **not** yet perform live academic database harvesting, independent study reanalysis, or manuscript/grant generation.