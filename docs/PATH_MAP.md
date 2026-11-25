# Path Map — old → new

> 2026-11-25 layout reorganization (R2). `milestones/` was dissolved; contents moved with `git mv` (history preserved, `git log --follow` works).

## Moves

| Old path | New path |
|----------|----------|
| `milestones/release/` | `releases/` |
| `milestones/06_deep_verification/` | `archive/deep_verification/` |
| `milestones/ai_platforms/` | `archive/ai_platforms/` |
| `milestones/jp_delivery/` | `archive/jp_delivery/` |
| `milestones/archive/` | `archive/legacy/` |

Earlier layouts, for reading older documents:

| Era | Old path | Current path |
|-----|----------|--------------|
| before 2026-07-21 (restructure v3) | `branches/06_deep_verification/`, `.work/06_deep_verification/` | `archive/deep_verification/` |
| before 2026-07-21 | `branches/jp_delivery/` | `archive/jp_delivery/` |
| before 2026-07-21 | top-level `ai_platforms/` | `archive/ai_platforms/` |
| before 2026-07-21 | top-level `release/` | `releases/` |
| before 2026-07-21 | top-level `archive/` | `archive/legacy/` |

## RAG / KG service

Everything RAG-related (`sdtm-rag/`, `milestones/07_rag_kg/`, `.work/05_rag_kg/`, `docs/DESIGN_RAG_KG.md`, etc.)
moved to the separate public repository [hakupao/sdtm-rag](https://github.com/hakupao/sdtm-rag), which pins
this repo's `knowledge_base/` as a git submodule.

## What was and was not rewritten

- **Rewritten**: build/content paths (`web/src/content.config.ts`, `web/scripts/build-bundles.sh`,
  `tools/build_release.sh`, `archive/jp_delivery/scripts/build_zip.sh`); every relative Markdown link that
  pointed into a moved directory; bare path mentions in live docs (README*, CLAUDE.md, METHODOLOGY.md,
  docs/PROGRESS.md, .work/MANIFEST.md, .work/AGENT_GUIDE.md, web/README.md, web/RELEASE.md).
- **Left as is (historical record)**: prose inside `archive/`, `.work/` phase directories, and the executed
  plans/specs under `docs/superpowers/`. Paths there describe the layout at the time they were written; use the
  tables above to translate.

## Link-check baseline

`python3 tools/check_links.py` reports **18,728** broken relative links at this reorganization, all pre-existing
and unchanged by it. Almost all are in the bundled knowledge-base copies under `releases/*/self_deploy/` and
`archive/ai_platforms/*/current/` (links that only resolve inside the original `knowledge_base/` tree), plus
`archive/legacy/old_knowledge_base_v0/`. The count should not go up.
