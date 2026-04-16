# SDTM Knowledge Base Project

## Project Overview

SDTM (Study Data Tabulation Model) knowledge base built from CDISC standard source files (PDF + xlsx).
293 Markdown files covering 63 domains, terminology, model concepts, and implementation guide chapters.

## Session Startup

Every new session, **before doing any work**, read these files in order:

1. `.work/MANIFEST.md` — file layout, change chains, quick reference table
2. `.work/meta/worklog.md` — work log with recovery guide
3. `.work/03_verification/issues_found.md` — open issues
4. `.work/meta/retrospective.md` § 4 — four prevention rules (must follow when doing any AI-assisted content work)

Then summarize to the user: current status, open issues, and suggested next step.

## Change Chains

This project uses a change-chain system to prevent forgotten updates.
When modifying any `.work/` file, check its `<!-- chain: X -->` header for related files that must also be updated.
Full chain definitions are in `.work/MANIFEST.md`.

## Key Paths

| What | Where |
|------|-------|
| Knowledge base output | `knowledge_base/` |
| Source files (PDF/xlsx) | `source/` |
| Work artifacts | `.work/` (phase-numbered dirs) |
| Project docs | `docs/` |
| Page index (authoritative) | `.work/02_indexing/page_index.json` |
| Verification plan | `.work/03_verification/plan.md` |
| Retrospective & rules | `.work/meta/retrospective.md` |
| Follow-up risk plan | `.work/03_verification/followup_plan.md` |
| TODO (Phase 6) | `.work/04_optimization/retrieval_optimization.md` |
| Phase 7 设计文档 | `docs/DESIGN_RAG_KG.md` |
| Phase 7 session 记录 | `.work/05_rag_kg/session_2026-04-16_design.md` |

## Conventions

- Knowledge base content is in English (extracted from English PDF sources)
- Work logs, plans, and meta docs are in Chinese
- File status fields use format: `> 状态: **已完成** (date)` or `> 状态: 描述`
- When completing a task, follow Chain B (work log → progress.json → docs/PROGRESS.md)
