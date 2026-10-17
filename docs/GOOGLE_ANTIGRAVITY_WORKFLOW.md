# VS Code and Google Antigravity workflow (October 2026)

## Why Antigravity instead of the old Gemini CLI
Google ended Google-sign-in access for **consumer** Gemini CLI and Gemini Code Assist in June 2026. Google AI Pro subscribers should now use Antigravity IDE, its VS Code extension or the `agy` CLI. Official references:
- https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals
- https://antigravity.google/docs/ide/extensions/vscode/
- https://antigravity.google/docs/cli/install/
- https://antigravity.google/docs/cli/subagents
- https://antigravity.google/docs/plans

## Workstation installation (Windows PowerShell)
1. Install VS Code, Git, Python 3.11+, R, Quarto and any agreed R packages in their usual supported installers.
2. Open VS Code Extensions (`Ctrl+Shift+X`), install **Google Antigravity** (publisher Google), and sign in with your existing Google AI Pro account. Install Codex separately and sign in with ChatGPT.
3. Clone into a local folder **outside OneDrive-synced directories** if feasible:
   ```powershell
   New-Item -ItemType Directory -Force C:\\dev
   cd C:\\dev
   git clone https://github.com/steven-ford2/academic-research.git
   cd academic-research
   code .
   py -3.11 -m venv .venv
   .\\.venv\\Scripts\\Activate.ps1
   python -m pip install -e '.[dev]'
   pytest -q
   ```
4. VS Code Antigravity extension automatically installs the local CLI backend. Or install independently via the official installer after inspecting it, then launch `agy`:
   ```powershell
   irm https://antigravity.google/cli/install.ps1 | iex
   agy
   ```
5. In CLI, use `/agents` to inspect workspace subagents, `/usage` to see model quotas and `/credits` to inspect credit consumption. Set automatic AI-credit overages to **Never** until deliberate spending is approved.

## Project-scoped agents
Agents defined under `.agents/agents/<agent-name>/agent.md` are automatically discovered. This repository provides:
- `literature-triage` (Flash; read-only): work on already acquired and licensed source metadata/notes.
- `citation-auditor` (Pro; read-only): claim-to-source mismatch reporting, not certification.
- `journal-intelligence` (Flash; read-only): examine *already retrieved* official policy snapshots.
- `methods-skeptic` (Pro; read-only): methodological critical review, not independent statistical reproduction.
- `repository-maintainer` (Flash; sandbox): bounded documentation, schemas, deterministic utilities and tests; no merging or research claims.

The root `AGENTS.md` is continuously active in Antigravity and Codex. Avoid duplicate `GEMINI.md` rules unless necessary. Some review agents do not have web tools: have the parent retrieve/verify sources, then delegate analysis of files. Restrict tool access by using known Antigravity tool names; never permit arbitrary self-modification.

## Multi-model handoff
1. Start from GitHub issue and create a short, testable task brief.
2. Assign literature/data inventory, docs and boilerplate to Antigravity Flash; route hard reasoning to its Pro agent as appropriate.
3. Save audit-ready outputs (source IDs, exact locators, test logs, changed files) in a feature branch.
4. Reserve Codex for complex statistical implementation, model diagnostics, architecture/integration or high-difficulty debugging. Independent R/statistical verification and investigator review remain mandatory.
5. Run Python/R checks and GitHub CI; review source traceability and scientific claims separately.
6. Merge a reviewed PR and update the issue; never let two agents modify the same uncommitted workspace concurrently.

## Privacy
Antigravity consumer terms permit use of interactions for product improvement subject to controls; assess data collection settings before use. Public repository currently holds **no participant datasets**. Do not provide raw or sensitive research data, unpublished manuscripts, employer/controlled information, or unlicensed PDFs to external agents until rights, permitted storage, product privacy, and institutional approvals are established.

## Suggested first Antigravity task
> Read AGENTS.md and docs/issues/02-literature.md. Audit the current literature/evidence schema and propose a deterministic DOI metadata normalization and deduplication implementation with synthetic fixtures. Work only in a feature branch. Do not make scientific claims, acquire restricted full texts, overwrite original data, or mark evidence verified. Include passing tests and unresolved issues in a PR.

## Relevant source docs
- Antigravity rules (AGENTS.md supported): https://antigravity.google/docs/rules/
- Agent definition syntax and tools: https://antigravity.google/docs/cli/subagents
- VS Code extension: https://antigravity.google/docs/ide/extensions/vscode/
- Quotas and credit overages: https://antigravity.google/docs/plans
