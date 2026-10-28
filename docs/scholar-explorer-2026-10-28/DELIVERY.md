# Delivery and verification — 2026-10-28

- Public website: https://zbchen16.github.io/rlhf-statistics-atlas/
- Public repository: https://github.com/zbchen16/rlhf-statistics-atlas
- Released source: 81d3d63ab50b4da9444801e6dc8f445bf6c4ace0
- Actions: https://github.com/zbchen16/rlhf-statistics-atlas/actions/runs/40623345119 — verify and deploy both success.
- Separate work branch: codex/scholar-three-directions. Prior stable branch retained.

40 selected papers: RLHF/preference/RLVR 16; LLM unlearning 12; watermark/general text detection 12. All 11 requested scholars covered; coauthored works count once in the collection. Scholar-specific counts and representative reading are on the scholar page and in docs/SELECTED_PAPERS_REPORT.md.

PASS: primary title/author-to-scholar associations; source/CSV/embedded data consistency; all 58 legacy IDs retained, with 55 archive records. Source analysis is abstract-level and labelled accordingly.

PASS: 17 independent browser checks locally and on the public URL, including scholar and combined filtering, author search, six-part details, bookmarks/read/notes persistence, archived note editing, comparison, exports, reading routes/opportunities, mobile layout and zero JavaScript runtime errors. Test storage was isolated from the user's real browser.

PASS: public HTML, papers.json, scholars.json and papers_archive.json each returned HTTP 200 and matched tested local bytes. Public repository visibility independently verified.

Limits: selected bibliography, not complete publication lists; full-text proofs/experimental figures not systematically audited. Some acceptance states are author-reported, publisher access sometimes blocked, and the RLHF survey venue is inconsistent across author websites. These limitations appear in individual records. Watermark robustness depends on mechanism/edit assumptions, and generic detection is not unconditional provenance proof.

No user login or authorization step remains. No unrelated project, active kernel or user browser session was modified.
