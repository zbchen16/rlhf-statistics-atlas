# Progress

2026-10-28: Read task/skills, inspected clean repository, created codex/scholar-three-directions from stable codex/selected-research-explorer. Baseline scripts/verify_site.py PASS (30 main, 28 archive). No other project changed.

2026-10-28: Verified 11 scholar identities against primary homepages and 46 candidate arXiv author/title/abstract records. Selected 40 (16 RLHF, 12 unlearning, 12 detection); six further candidates retained in the report. Three old main IDs remain selected, 55 archived; all 58 legacy IDs retained. Added scholar navigation, author search/filtering, publication evidence, archive note editing, revised roadmap/opportunities, and retained grayscale design.

Verification: scripts/verify_site.py PASS; Node script syntax PASS; git diff --check PASS. 17 Playwright behavior checks PASS in an isolated project-local browser, including persistence/archived notes/exports/mobile/zero runtime errors. Desktop, scholar map and mobile screenshots visually inspected. Chromium and temporary files are project-local and ignored; no active user browser or kernel touched. Initial bundled-browser launch failed because Chromium was absent; installed the test browser only under this project and reran successfully.

Publication-source HTTP checks recorded separately: 31 successful endpoints, five blocked endpoints (403); blocked publisher pages remain linked and claims use accessible primary arXiv records plus documented publication metadata. No full-text theorem audit or paper experiment reproduction was performed.

Next: publish tested branch to existing public repository, verify Actions and live data/HTTP, and run the interaction checks against the public project subpath.
