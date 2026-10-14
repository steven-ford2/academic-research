"""Minimal tracked-file safety check; not a security audit."""
from pathlib import Path
import subprocess
import sys

EXT = {".edf", ".asc", ".mp4", ".mov", ".avi", ".sqlite", ".duckdb", ".parquet"}
PATHS = ("/data/raw/", "/data/derived/", "/restricted/", "/private/")


def main():
    result = subprocess.run(["git", "ls-files", "-z"], capture_output=True, check=True)
    names = result.stdout.decode().split("\x00")
    bad = []
    for name in names:
        if not name:
            continue
        path = Path(name)
        if path.suffix.lower() in EXT or any(s in "/" + name for s in PATHS):
            bad.append(name)
        if path.name == ".env" or (path.name.startswith(".env.") and path.name != ".env.example"):
            bad.append(name)
    if bad:
        print("Forbidden tracked files:", *sorted(set(bad)), sep="\n")
        return 1
    print("Tracked-file screening passed; human review remains required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
