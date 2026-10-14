from datetime import date

from researchos.journals import audit_profile


def test_unverified_profile_fails(tmp_path):
    p = tmp_path / "journal.yaml"
    p.write_text("journal: Example\nstatus: unverified\n")
    assert audit_profile(p)

def test_verified_recent_profile_passes(tmp_path):
    p = tmp_path / "journal.yaml"
    p.write_text("\n".join([
        "journal: Example", "article_type: Research", "status: verified",
        "official_instructions_url: https://example.org/authors",
        "ai_policy_url: https://example.org/ai",
        f"last_verified_utc: '{date.today().isoformat()}'",
    ]))
    assert audit_profile(p) == []
