"""Minimal ResearchOS command-line interface."""
import argparse
import json
import re
import sys
from pathlib import Path

from .evidence import audit_claims, release_blockers
from .journals import audit_profile


def create_project(title, kind, root):
    slug = re.sub("-+", "-", re.sub("[^a-z0-9]+", "-", title.lower())).strip("-")
    if not slug:
        raise ValueError("Title required")
    folder = Path(root) / slug
    if folder.exists():
        raise FileExistsError(f"Already exists: {folder}")
    for section in ("protocol", "analysis", "manuscript", "figures", "reviews", "data"):
        (folder / section).mkdir(parents=True, exist_ok=True)
    (folder / "README.md").write_text(
        f"# {title}\n\nType: {kind}\nStatus: not approved\n", encoding="utf-8")
    (folder / "protocol" / "research_charter.md").write_text(
        "# Research charter\n\n- Question: [PI required]\n"
        "- Estimands: [PI required]\n- Design: [PI required]\n"
        "- Ethical review: [pending]\n", encoding="utf-8")
    (folder / "data" / "README.md").write_text(
        "Keep participant data in approved restricted storage.\n", encoding="utf-8")
    return folder


def main(argv=None):
    parser = argparse.ArgumentParser(prog="researchos")
    commands = parser.add_subparsers(dest="cmd", required=True)
    commands.add_parser("status")
    ev = commands.add_parser("audit-evidence")
    ev.add_argument("file")
    ev.add_argument("--release", action="store_true")
    jr = commands.add_parser("audit-journals")
    jr.add_argument("directory")
    jr.add_argument("--max-age-days", type=int, default=90)
    project = commands.add_parser("init-project")
    project.add_argument("title")
    project.add_argument("--type", required=True, choices=[
        "empirical", "review", "meta-analysis", "grant", "experiment"])
    project.add_argument("--root", default="projects")
    a = parser.parse_args(argv)
    if a.cmd == "status":
        print(json.dumps({"status": "alpha", "available": [
            "project scaffolding", "evidence ledger structure audit",
            "journal metadata audit"], "not_available": [
            "verified literature search", "statistical reanalysis",
            "manuscript and grant generation"]}, indent=2))
        return 0
    if a.cmd == "init-project":
        try:
            print("Created", create_project(a.title, a.type, a.root))
            return 0
        except (ValueError, OSError) as exc:
            print(exc, file=sys.stderr)
            return 2
    if a.cmd == "audit-evidence":
        issues = release_blockers(a.file) if a.release else audit_claims(a.file)
    else:
        profiles = list(Path(a.directory).glob("*.yaml"))
        issues = ["No journal profiles found"] if not profiles else [
            problem for p in profiles
            for problem in audit_profile(p, max_age_days=a.max_age_days)]
    for issue in issues:
        print("BLOCKER:", issue)
    if not issues:
        print("Structural validation only; scientific truth not checked.")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
