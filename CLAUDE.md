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
| Phase 6.5 AI 平台部署 | `ai_platforms/` (总览 + 三平台子目录) |
| Phase 6.5 Claude 压缩计划 | `ai_platforms/claude_projects/PLAN.md` (方案 B, 实测 192,036 tokens, 含 §7 Claude Code 执行手册) |
| Phase 6.5 Claude 上传教程 | `ai_platforms/claude_projects/UPLOAD_TUTORIAL.md` (Step 13-14 手工操作手册 + T1-T8 测试矩阵) |
| Phase 6.5 Claude 压缩脚本 | `ai_platforms/claude_projects/scripts/` (11 个 Python 脚本, build_all.py 一键重建) |
| Phase 6.5 Claude 压缩产物 | `ai_platforms/claude_projects/output/` (11 个 .md 上传文件 + upload_manifest.md) |
| Phase 6.5 Claude 执行进度 | `ai_platforms/claude_projects/output/_progress.json` (Step 1-12 completed, 等 step13 用户上传) |
| Phase 6.5 Claude Evidence | `ai_platforms/claude_projects/output/evidence/` (trace.jsonl + 12 份 step_NN_*.md + checkpoints/ + subagent_prompts/ + failures/) |
| Phase 6.5 Claude Retrospective | `ai_platforms/claude_projects/RETROSPECTIVE.md` (Step 1-12 复盘: R1-R5 保留 / G1-G4 缺口 / 四条规则 A/B/C/D 已固化到全局 CLAUDE.md) |

## Session Wrap-up (收尾)

When the user says **"收尾"**, **"wrap up"**, or **"提交收尾"**, execute the following checklist automatically:

1. **Review** what was done this session (read git diff + new files)
2. **Update index files** — always update these 3 (+ CLAUDE.md if new key paths):
   - `.work/MANIFEST.md` — plan map, directory structure, phase mapping, quick reference
   - `.work/meta/worklog.md` — execution phase table + append work record entry
   - `docs/PROGRESS.md` — progress board status
   - `CLAUDE.md` Key Paths table (only if new key paths were created)
3. **Check Change Chains** — if knowledge_base/ changed → Chain D; if plans changed → Chain E
4. **Commit + push** — single commit with descriptive message, push to main
5. **Report** — one-line summary of what was committed

Do NOT ask for confirmation on each step — just execute the full checklist and report at the end.

## Conventions

- Knowledge base content is in English (extracted from English PDF sources)
- Work logs, plans, and meta docs are in Chinese
- File status fields use format: `> 状态: **已完成** (date)` or `> 状态: 描述`
- When completing a task, follow Chain B (work log → progress.json → docs/PROGRESS.md)
