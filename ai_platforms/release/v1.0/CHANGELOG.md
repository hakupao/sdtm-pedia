---
lang: en
slug: changelog
order: 60
title: "Changelog"
---

# CHANGELOG — SDTM AI Knowledge Base Release

## v1.0 — 2026-04-27 (Company Release)

**First public release for company-internal use.**

### Added
- 4-platform LIVE deployments: Claude Projects v2.6 / ChatGPT GPTs v2.2 / Gemini Gems v7.1 / NotebookLM (Custom mode instructions 8,925 chars)
- Trilingual user documentation (zh / en / ja): top README, USER_GUIDE, self_deploy/README, 4 × UPLOAD_TUTORIAL
- 10-question DEMO pack with multilingual prompts
- KNOWN_LIMITATIONS reference (en)
- 17-question smoke test framework v4.0 with 3 anti-hallucination probes (AHP)
- Per-platform decision tree ("which platform for what")

### Quality baselines (17-question evaluation, R1+R2)
- Claude Projects: 17/17 (100%) — all PASS
- ChatGPT GPTs: 16.5/17 (97%) — post v2.2 Q1 GFINHERT spelling fix
- Gemini Gems: 16/17 (94%) — post v7.1 Q10 SUPP-- Core anchor; R2 dual-gate PASS
- NotebookLM: 15/17 (88%) — Q11/Q12 supplemental topics PUNT (correct), Q9 safety-correct PUNT

### Methodology references
- 4 prevention rules (Rules A/B/C/D) governing all AI-assisted content work
- 28-slot independent reviewer chain (Rule D) across 17-question evaluation + V5C regression
- Per-platform Phase 0-5 lifecycle with sign-off (PHASE5_RETROSPECTIVE.md)

### Source Knowledge Base
- 295 Markdown files derived from CDISC SDTMIG v3.4 + CDISC CT (NCI EVS) + SDTM v2.0 model
- 63 SDTM domains (full spec + assumptions + examples per domain)
- ~2,400K total tokens across all source files

### Release artifacts
- `./` (this folder) — self-contained release: public-facing docs + per-platform deploy bundles under `self_deploy/{claude,chatgpt,gemini,notebooklm}/`, each with `system_prompt.md` (or `instructions.md`) + `uploads/` + trilingual `tutorial.{zh,en,ja}.md`
- git tag: `v1.0-company-release` (created at Phase E end)

### Known limitations
See `KNOWN_LIMITATIONS.en.md` for full list (L1-L3 cross-platform + L4 per-platform).

---

## Pre-release (work history, abbreviated)

- 2026-04-23 to 2026-04-24: Phase 5 sign-off across 4 platforms (28th independent reviewer ack-ready)
- 2026-04-24: Gemini v7.1 LIVE (post Q10 PASS+) + ChatGPT v2.2 LIVE (post Q1 PASS)
- 2026-04-22: smoke v4.0 question battery design (3 + 14 + 3 = 20 evaluation files per platform)
- 2026-04-21: NotebookLM v2 architecture pivot (3-notebook → 1-notebook × 42 sources)
- 2026-04-20: Claude Projects v2.6 final (24/24 PASS, 1.29M tokens / 77% capacity)
- 2026-04-18 onwards: 4-platform parallel deployment program kickoff

Full development history (28-slot Rule D reviewer chain, R1/R2/PHASE5/V5C retrospectives, per-platform retros) is maintained internally and available from Bojiang Zhang on request.
