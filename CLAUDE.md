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
| **Phase 6.5 Claude 入口 (reorg 后)** | **`ai_platforms/claude_projects/README.md`** — 新结构导航入口, 指向 current/docs/dev/archive 四层 |
| Phase 6.5 Claude 当前可部署 (v2.6) | `ai_platforms/claude_projects/current/` (uploads/ 19 文件 + system_prompt.md + upload_manifest.md, 1.29M tokens, capacity 77%) |
| Phase 6.5 Claude 方法论文档 | `ai_platforms/claude_projects/docs/` (PLAN_V2.md + RETROSPECTIVE_V2.md + rag_decay_curve.md + phase7_handoff.md + capacity_research.md) |
| Phase 6.5 Claude v2 RAG 衰减曲线 | `ai_platforms/claude_projects/docs/rag_decay_curve.md` (7 数据点 v1→v2.6 + 4 段跨批观察 + 结论 + 6 Phase 7 actionable, 拐点 ≥77% 未触) |
| Phase 6.5 Claude v2 Phase 7 交接 | `ai_platforms/claude_projects/docs/phase7_handoff.md` (6 actionable insight + 5 Q 未解 + 5 步待办, Phase 7 启动前必读) |
| Phase 6.5 Claude v2 终态复盘 | `ai_platforms/claude_projects/docs/RETROSPECTIVE_V2.md` (Rule C 产物, 7 章 R1-R8 保留 + G1-G5 缺口 + 5 决策 + Rule E 候选, 过 Rule D 独立复核 PASS) |
| Phase 6.5 Claude v2 计划 | `ai_platforms/claude_projects/docs/PLAN_V2.md` (1852 行, 8 阶段 ~30 Tasks; 内部路径引用反映 reorg 前状态, 见文件头部 post-reorg note) |
| Phase 6.5 Claude 容量调研 | `ai_platforms/claude_projects/docs/capacity_research.md` (200K 假设错, RAG 自动扩 10x, 实际容量 ~3-4M) |
| Phase 6.5 Claude 开发过程产物 (冷区) | `ai_platforms/claude_projects/dev/` (scripts/ 6 脚本 + evidence/ 49 份 + ab_reports/ 5 + checkpoints/ 6 + test_results.md; 路径引用保留 reorg 前语境, 见 dev/README.md 映射表) |
| Phase 6.5 Claude v2 v2.6 A/B 报告 | `ai_platforms/claude_projects/dev/ab_reports/STAGE_V2.6_AB_REPORT.md` (终态 24/24 PASS, capacity 77%) |
| Phase 6.5 Claude v2 执行进度 (历史) | `ai_platforms/claude_projects/dev/evidence/_progress.json` (status=completed, 5 checkpoints_acked v2.1-v2.4 + v2.6, phase_final_metrics 快照) |
| Phase 6.5 Claude v2 H1 独立复核 | `ai_platforms/claude_projects/dev/evidence/H1_reviewer.md` (code-reviewer subagent CONDITIONAL_PASS→PASS, 2 MEDIUM + 3 LOW 数据偏离已修正) |
| Phase 6.5 Claude 历史归档 (v1 冻结) | `ai_platforms/claude_projects/archive/` (RETROSPECTIVE.md 顶层 + v1/{docs,scripts,uploads} 全冻结) |
| Phase 6.5 Claude v1 复盘 | `ai_platforms/claude_projects/archive/RETROSPECTIVE.md` (v1 Step 1-12 复盘: R1-R5 保留 / G1-G4 缺口 / 四条规则 A/B/C/D 已固化到全局 CLAUDE.md) |
| Phase 6.5 Claude v2 设计 | `docs/superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md` (中庸 5 批 / ~50% 容量 / 16-18 文件 / RAG 衰减曲线) |
| Phase 6.5 Claude v2 plan pointer | `docs/superpowers/plans/2026-04-18-phase6.5-claude-v2-expansion.md` (superpowers skill 约定, 指向 docs/PLAN_V2.md) |

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
