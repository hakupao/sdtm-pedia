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
| Phase 6.5 Claude 容量调研 | `ai_platforms/claude_projects/capacity_research.md` (Step 14 后修订: 200K 假设错, RAG 自动扩 10x, 实际容量 ~3-4M, 详见 PLAN §8 postscript) |
| Phase 6.5 Claude v2 设计 | `docs/superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md` (中庸 5 批 / ~50% 容量 / 16-18 文件 / RAG 衰减曲线) |
| Phase 6.5 Claude v2 计划 | `ai_platforms/claude_projects/PLAN_V2.md` (1852 行, 8 阶段 ~30 Tasks, subagent-driven, 5 hard checkpoints) |
| Phase 6.5 Claude v2 plan pointer | `docs/superpowers/plans/2026-04-18-phase6.5-claude-v2-expansion.md` (superpowers skill 约定, 指向 PLAN_V2.md) |
| Phase 6.5 Claude v2 启动提示词 | `ai_platforms/claude_projects/V2_SESSION_STARTER.md` (新 session 复制粘贴用, 含预授权 + 约束) |
| Phase 6.5 Claude v2 执行进度 | `ai_platforms/claude_projects/output_v2/evidence_v2/_progress.json` (hot path: 4 checkpoints_acked v2.1-v2.4 + g1_output + session_handoff, pending=G2) |
| Phase 6.5 Claude v2 产物 | `ai_platforms/claude_projects/output_v2/` (批 1-4 完成: 14 实体 / 719,241 tokens / capacity 43% / 0 衰减; v2.5 待 G2) |
| Phase 6.5 Claude v2 脚本 | `ai_platforms/claude_projects/scripts_v2/` (6 个: rebuild_chapters/extract_examples_data/extract_terminology_terms/score_domains/score_codelists/build_v2_stage) |
| Phase 6.5 Claude v2 Evidence | `ai_platforms/claude_projects/output_v2/evidence_v2/` (trace.jsonl + _progress.json + subagent_prompts/ 含 G2_executor.md + checkpoints/ + failures/) |
| Phase 6.5 Claude v2 A/B 报告 | `ai_platforms/claude_projects/output_v2/STAGE_V2.{1,2,3,4}_AB_REPORT.md` (4 批 A/B 测试报告, Cowork 填, v2.4 经 Rule D 独立 reviewer 复核) |
| Phase 6.5 Claude v2 Cowork handoff | `ai_platforms/claude_projects/output_v2/CHECKPOINT_V2.{1,2,3,4}_HANDOFF.md` (4 批 Cowork 自动执行手册) |
| Phase 6.5 Claude v2 RAG 衰减曲线 | `ai_platforms/claude_projects/output_v2/rag_decay_curve.md` (5 数据点 v1→v2.4 + 3 段跨批观察 含 T3 二阶正向激活, Phase 7 核心输入) |
| Phase 6.5 Claude v2 测试矩阵 | `ai_platforms/claude_projects/output_v2/test_results_v2.md` (T1-T22 + T-core-reb/T-supp-reb 完整矩阵 + v2.1-v2.6 stage 汇总) |
| Phase 6.5 Claude v2 终态复盘 | `ai_platforms/claude_projects/RETROSPECTIVE_V2.md` (Rule C 产物, 7 章 R1-R8 保留 + G1-G5 缺口 + 5 决策 + Rule E 候选, 过 Rule D 独立复核 PASS, 2026-04-20) |
| Phase 6.5 Claude v2 Phase 7 交接 | `ai_platforms/claude_projects/output_v2/phase7_handoff.md` (6 actionable insight + 5 Q 未解 + 5 步待办, Phase 7 启动前必读, 2026-04-20) |
| Phase 6.5 Claude v2 RAG 曲线终态 | `ai_platforms/claude_projects/output_v2/rag_decay_curve.md` (7 数据点 v1→v2.6 + 4 段跨批观察 + 结论 + 6 Phase 7 actionable, 拐点 ≥77% 未触) |
| Phase 6.5 Claude v2 v2.6 A/B 报告 | `ai_platforms/claude_projects/output_v2/STAGE_V2.6_AB_REPORT.md` (终态 24/24 PASS, T1-T20 持平 + T21/T22 tail + 2 优先级验证全通过, capacity 77%) |
| Phase 6.5 Claude v2 H1 独立复核 | `ai_platforms/claude_projects/output_v2/evidence_v2/H1_reviewer.md` (code-reviewer subagent CONDITIONAL_PASS→PASS, 2 MEDIUM + 3 LOW 数据偏离已修正) |

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
