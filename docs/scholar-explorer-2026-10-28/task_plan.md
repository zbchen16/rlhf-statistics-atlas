# Scholar Research Explorer — 2026-10-28

Owner: coordinator. Branch: codex/scholar-three-directions.

Goal: curate relevant papers by the 11 scholars in the supplied screenshot into the existing black/white static explorer and publish the tested result to the existing public GitHub Pages site.

Scope: RLHF (priority), LLM Unlearning, Watermark & AI Text Detection (especially after paraphrase/editing). Verify identities, titles/authors, identifiers, publication status and abstract-level claims. Keep empirical claims attributed and research suggestions hypothetical. No claimed theorem-proof audit. No quantity padding or exhaustive-publication claim.

Constraints: project-only edits, preserve old IDs/localStorage records and archive removed records; papers.json canonical, CSV/HTML generated; preserve stable prior branch, no force push, no framework/backend. Retain existing simple black/white UI and reading functions.

Phases:
1. [done] Inspect project/Git and baseline data check (30 papers, 28 archive).
2. [done] Verify scholar identities and primary-source bibliography.
3. [done] Add scholar navigation, replace three directions/content, archive prior selections safely.
4. [done] Verify data and browser interactions; review source/claims.
5. [done] Publish and verify Actions/public HTTP; report limitations.

Complete: source consistency, 17 local and 17 public browser checks, GitHub Actions verify/deploy, and live byte comparisons passed.
