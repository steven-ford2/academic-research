"""Verify local source-manifest shape, NOT the external PDF's checksum/content."""
import json
from pathlib import Path

path = Path("projects/digital-biomarkers-usability/SOURCE_MANIFEST.json")
record = json.loads(path.read_text(encoding="utf-8"))
assert record["source_id"] == "ford-2025-dissertation"
assert record["public_url"].startswith("https://stars.library.ucf.edu/")
assert record["data_availability"] == "not_in_repository"
print("Manifest structure verified; scientific source content not verified.")
