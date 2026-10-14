"""Validate evidence record structure, not scholarly correctness."""
import json
from pathlib import Path

STATES = {"unverified", "located", "checked", "disputed", "retracted"}


def audit_claims(path):
    try:
        records = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"Cannot read evidence ledger: {exc}"]
    if not isinstance(records, list) or not records:
        return ["Expected a nonempty list of evidence records"]
    problems = []
    seen = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            problems.append(f"{index}: record must be object")
            continue
        key = record.get("id")
        if not isinstance(key, str) or not key.strip() or key in seen:
            problems.append(f"{index}: missing or repeated ID")
        seen.add(key)
        if not isinstance(record.get("claim"), str) or not record["claim"].strip():
            problems.append(f"{key}: missing claim text")
        state = record.get("verification_status")
        if state not in STATES:
            problems.append(f"{key}: invalid verification state")
        if state == "checked":
            sources = record.get("sources")
            if not isinstance(sources, list) or not sources:
                problems.append(f"{key}: checked claim without sources")
            else:
                for source in sources:
                    if not isinstance(source, dict) or not all(
                        source.get(k) for k in ("document_id", "locator", "verification_method")
                    ):
                        problems.append(f"{key}: source locator or method missing")
    return problems


def release_blockers(path):
    problems = audit_claims(path)
    if problems:
        return problems
    records = json.loads(Path(path).read_text(encoding="utf-8"))
    return [f"{x['id']}: not independently checked" for x in records
            if x["verification_status"] != "checked"]
