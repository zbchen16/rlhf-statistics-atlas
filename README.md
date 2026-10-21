# Statistics × LLM Alignment Research Explorer

**Public site:** https://zbchen16.github.io/rlhf-statistics-atlas/

A static, Chinese-language curated reading site for statistics researchers. The main collection contains **30 papers**: **15** RLHF & Preference Alignment, **9** Other Alignment Methods, and **6** Machine Unlearning. It favors representative research questions over a large bibliography. See [selection and evidence report](docs/SELECTED_PAPERS_REPORT.md).

## Use

Open `public/index.html` directly or serve `public/` with `python3 -m http.server 8000 --directory public`. The four sections are Overview, Paper Explorer, Research Opportunities and Reading Roadmap. Search, direction/venue/year/type filters, bookmarks, read status, notes, comparisons and export work in the browser. Personal state stays in the current browser's `localStorage`; it is not uploaded or synchronized.

## Maintain the bibliography

`public/data/papers.json` is the **sole canonical selected-paper source**. Edit it, then run:

```bash
python3 scripts/sync_papers.py
python3 scripts/verify_site.py
```

The sync script regenerates the embedded offline-capable HTML data and `public/data/papers.csv`. `public/data/papers_archive.json` preserves the 28 excluded records from the original 41-paper collection. Old IDs were kept for selected papers; if an archived paper returns, restore its original ID so existing local notes reattach. Do not reuse an old ID for a different paper. Roadmap and opportunity references in `public/index.html` are editorial and need separate review when papers change.

## Evidence limits

Publication metadata and six-part summaries were checked against official proceedings and abstracts where accessible. Full-text theorem assumptions, proof details, and numeric experiment results were **not systematically audited**; each paper has a `verification` field. The Constitutional AI entry is labeled as an arXiv preprint. Research opportunities are hypotheses for further reading, not verified literature gaps. The site does not claim that its LLM unlearning papers prove certified deletion. Venue names are not individual paper quality grades.

## Deployment

`.github/workflows/pages.yml` verifies source consistency and deploys `public/` after a push to `main`. GitHub Pages is configured to use GitHub Actions. Confirm the latest Actions run and public URL after each release. The public repository has no backend, login, paid service or API key.
