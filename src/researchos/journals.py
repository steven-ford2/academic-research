"""Journal metadata recency and human verification, not source truth."""
from datetime import date
from pathlib import Path
import yaml


def audit_profile(path, max_age_days=90):
    path = Path(path)
    try:
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return [f"{path}: cannot load: {exc}"]
    if not isinstance(record, dict):
        return [f"{path}: profile must be mapping"]
    issues = []
    for key in ("journal", "article_type", "official_instructions_url",
                "ai_policy_url", "last_verified_utc"):
        if not record.get(key):
            issues.append(f"{path}: missing {key}")
    if record.get("status") != "verified":
        issues.append(f"{path}: human verification pending")
    for key in ("official_instructions_url", "ai_policy_url"):
        if record.get(key) and not str(record[key]).startswith("https://"):
            issues.append(f"{path}: invalid {key}")
    if record.get("last_verified_utc"):
        try:
            age = (date.today() - date.fromisoformat(str(record["last_verified_utc"]))).days
            if not 0 <= age <= max_age_days:
                issues.append(f"{path}: out-of-date verification")
        except ValueError:
            issues.append(f"{path}: bad verification date")
    return issues
