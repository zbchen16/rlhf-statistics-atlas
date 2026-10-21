#!/usr/bin/env python3
"""Regenerate public/data/papers.csv and embedded PAPERS in public/index.html.

Canonical bibliography is public/data/papers.json. No third-party dependencies.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "public/data/papers.json"
HTML = ROOT / "public/index.html"
CSV = ROOT / "public/data/papers.csv"


def main() -> None:
    papers = json.loads(DATA.read_text(encoding="utf-8"))
    if not isinstance(papers, list) or not papers:
        raise ValueError("papers.json must be a nonempty JSON list")
    if not all(isinstance(p, dict) for p in papers):
        raise ValueError("all paper records must be JSON objects")
    fields = list(papers[0])
    if not all(list(row) == fields for row in papers):
        raise ValueError("record fields/order must match for clean CSV export")
    with CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(papers)
    source = HTML.read_text(encoding="utf-8")
    # Do not allow an inserted record to prematurely close the HTML script element.
    serialized = json.dumps(papers, ensure_ascii=False, indent=2).replace("<", "\\u003c")
    pattern = r"(?<=const PAPERS = )\[[\s\S]*?\](?=;\nconst DIRECTIONS = )"
    updated, n = re.subn(pattern, lambda _m: serialized, source)
    if n != 1:
        raise ValueError(f"Expected one PAPERS declaration before ROUTE, got {n}; aborting")
    HTML.write_text(updated, encoding="utf-8")
    print(f"Synced {len(papers)} paper entries into HTML and CSV")


if __name__ == "__main__":
    main()
