#!/usr/bin/env python3
"""Lightweight static acceptance checks without altering the site or its data."""
from __future__ import annotations

import csv
import json
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "public/index.html"
JSON = ROOT / "public/data/papers.json"
CSV = ROOT / "public/data/papers.csv"
REQUIRED = ("id", "title", "year", "venue", "topic", "stat", "rank", "url", "insight", "question", "angle", "effort", "keywords", "memo")


def verify() -> None:
    html = HTML.read_text(encoding="utf-8")
    papers = json.loads(JSON.read_text(encoding="utf-8"))
    assert isinstance(papers, list) and papers, "non-empty papers.json required"
    assert len(papers) == len({p["id"] for p in papers}), "paper IDs must be unique"
    assert len(papers) == len({p["title"] for p in papers}), "paper titles must be unique"
    assert all(tuple(p) == REQUIRED for p in papers), "missing or extra paper fields"
    assert all(isinstance(p["year"], int) and p["year"] >= 2020 for p in papers), "invalid years"
    assert all(p["rank"] in ("A", "B", "C", "S") for p in papers), "invalid priority"
    assert all(urlparse(p["url"]).scheme == "https" and urlparse(p["url"]).netloc for p in papers), "invalid URL format"
    matches = re.findall(r"const PAPERS = (\[[\s\S]*?\]);\nconst ROUTE = ", html)
    assert len(matches) == 1, "embedded HTML paper array not found exactly once"
    embedded = json.loads(matches[0])
    assert embedded == papers, "HTML data is stale; run python scripts/sync_papers.py"
    with CSV.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        assert tuple(reader.fieldnames or ()) == REQUIRED, "CSV headers differ"
        rows = list(reader)
    assert len(rows) == len(papers), "CSV record count differs"
    for idx, (record, row) in enumerate(zip(papers, rows), 1):
        assert all(str(record[k]) == row[k] for k in REQUIRED), f"CSV mismatch at row {idx}"
    assert '<html lang="zh-CN">' in html, "expected Chinese language metadata"
    assert 'id="papers"' in html and 'id="search"' in html, "core UI missing"
    assert '<script>' in html and '</script>' in html, "static JavaScript missing"
    assert (ROOT/'public/.nojekyll').exists(), "expected .nojekyll marker"
    print(f"PASS: {len(papers)} papers, {sum(p['rank']=='A' for p in papers)} A-priority, CSV/HTML snapshot synced")
    print("NOTE: This is a consistency check, not independent verification of every citation or remote deployment.")


if __name__ == '__main__':
    verify()
