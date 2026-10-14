import json
from researchos.evidence import audit_claims, release_blockers


def test_checked_claim_needs_source_locator(tmp_path):
    p = tmp_path / "claims.json"
    p.write_text(json.dumps([{"id": "1", "claim": "C", "verification_status": "checked",
                              "sources": [{"document_id": "x", "verification_method": "primary_fulltext"}]}]))
    assert audit_claims(p)


def test_unverified_claim_blocks_release(tmp_path):
    p = tmp_path / "claims.json"
    p.write_text(json.dumps([{"id": "1", "claim": "C", "verification_status": "unverified"}]))
    assert audit_claims(p) == []
    assert release_blockers(p)


def test_checked_claim_valid_structure(tmp_path):
    p = tmp_path / "claims.json"
    p.write_text(json.dumps([{"id": "1", "claim": "C", "verification_status": "checked",
                              "sources": [{"document_id": "x", "locator": "Table 1",
                                           "verification_method": "primary_fulltext"}]}]))
    assert release_blockers(p) == []
