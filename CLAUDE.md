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

## 06 Deep Verification Multi-Session History (rounds 1-13 closed; round 14 closing in flight)

**Round 1-13 closed cumulative state** (post round 13 reconciler `ae06326`): 12194 atoms / 519 pages / 52 batches / 115 findings / 47 AUDIT-mode pivots / 11 active families with 4 EXHAUSTED [vercel + plugin-dev + feature-dev + pr-review-toolkit] / ~19.5-20h wall savings vs serial / 0 quality regression / 0 cross-round Rule D collision / **ig34 fully atomized 461/461 = 100%** / **sv20 58/74 = 78.4%** (p.50 SKIP → v1.8 backfill candidate) / **P1 closure trajectory 519/535 = 97.0% / 16 pages residual / round 14 estimated to P1 CLOSURE milestone**.

**Per-round digest** (all reconcilers committed):

- Round 1-3 (batches 13-22): foundational baseline; reconcilers `6d173b1` / `d6bc41c` / `eb51567`.
- Round 4-6 (batches 23-31, 2026-04-26→27): 3 family pools EXHAUSTED + general-purpose / pr-review-toolkit / superpowers inaugural.
- Round 7 (batches 32-34 `1af10c5`): G-MS-4 1st LIVE-FIRE; v1.4 cut COMPLETED.
- Round 8 (batches 35-37 `eda792b`): drift cal p.357 4th cumulative VH → v1.5 cut #48 codex INAUGURAL.
- Round 9 (batches 38-40 `856fc21`): drift cal p.382 5th cumulative VH + §7 L1 NEW + Explore INAUGURAL → v1.6 cut `5e2b953` #52 codex 2nd burn.
- Round 10 (batches 41-43 `c545618`): drift cal p.412 **6th cumulative VH** → HALT_BATCH_42 + v1.7 trigger + omc 12× + N6 SendMessage NEW PRECEDENT → v1.7 cut COMPLETED #56 codex 3rd burn.
- Round 11 (batches 44-46 `dd67cee`): v1.7 1st INAUGURAL EFFECTIVE + drift cal p.445 NEW class canonical-form drift NOT VH + N6 single-dispatch NEW PRECEDENT.
- Round 12 (batches 47-49 `ba1ae12`): **ig34 fully atomized 461/461** + cross-PDF boundary 1st cumulative + drift cal sv20 p.15 MULTI-MOTIF SIMULTANEOUS 3 axes (Axis 1+2+3 writer-direction artifact-only BY DESIGN) + omc 14× critic D-MS-7.
- **Round 13** (batches 50-52 `ae06326`): v1.7 3rd round running EFFECTIVE + **FIRST executor-direction motif observable** (O-P1-177 Axis 4 + O-P1-181 N26 + Axis 2 executor-direction; MEDIUM not v1.8 trigger ESCALATION; v1.9 candidate stack) + drift cal sv20 p.45 GRANULARITY_DIVERGENCE_MULTI_AXIS_BIDIRECTIONAL **NO Axis 1 VH first in 13 cumulative drift cals** + counter-intuitive writer SUPERIOR to executor on page boundary first observed + omc 15× architect D-MS-7 (6 successive sister chain) + codex 6-burn + Plan 3-burn + slot collision resolved (#63→#64 + #64→#65 + #65→#66 per v1.8 cut took #63 in parallel).

**v1.8 baseline ACTIVE since 2026-04-30** (`0d6efb4`): 4 prompts P0_writer_pdf/md/matcher/reviewer_v1.8.md (5 NEW patches N24-N28 multi-axis motif taxonomy + cross-PDF §3.5 sweep + page-boundary Hook 21 + L1/L2 parent_section conventions; Rule D roster 56→63 + 36-item fix matrix A-AJ + Self-Validate hooks 20→21). v1.7 archived `archive/v1.7_final_2026-04-30/`. Round 13 used v1.7 (dispatched BEFORE v1.8 cut commit per no-mid-round-prompt-swap); **round 14 adopts v1.8 baseline** (1st INAUGURAL live-fire).

**Round 14 closing prep notes**:
- Page range: **single closing batch 53 covers sv20 p.60-74** (15 pages residual) — Option A per round 13 retro §6 (P1 closure proximity + pages < 2-batch threshold + simpler closure; deviation from 10-page convention justified). Drift cal SKIP this round (cumulative atoms post-sv20-p.45 ≥600 dual-threshold not met by single-batch end).
- Pre-allocated reviewer slot: **#67** (NOT cumulative #1-#66).
- Finding ID range pre-allocation: O-P1-189..194 (6 IDs reserved for closing batch).
- v1.8 N21 production-side prevention layer + N24 multi-axis taxonomy + N25 cross-PDF sweep N/A (sv20-only) + N26 Hook 21 page-boundary detection + N27/N28 parent_section conventions all ACTIVE for round 14.
- **P1 CLOSURE milestone trigger** at sv20 p.74 = 535/535 = 100% (assuming Option (a) p.50 SKIP held; if v1.8 backfills sv20 p.50 separately, full closure includes 1 backfill batch).
- O-P1-185 sv20 p.50 backfill DEFERRED to v1.8 cut session OR round 14 prep (separate single-page batch ~10-20 atoms covering §4 [ASSOCIATED PERSONS DATA] L1 NEW chapter).

**Routing rule** (round 14): `batch 53 开始任务` → `multi_session/batch_53_kickoff.md`, `reconciler 开始任务` → `reconciler_kickoff_round14.md`. Master guide `multi_session/MULTI_SESSION_PROTOCOL.md` + 13 retro files MULTI_SESSION_RETRO.md + MULTI_SESSION_RETRO_ROUND_2..13.md + 13 sibling_continuity_sweep_reports preserved as historical reference.

**Preserved historical artifacts**: `MULTI_SESSION_PROTOCOL.md` + 13 retro files round 1-13 + halt_state files (batch 32/36/42/51 G-MS-4 LIVE-FIRE; batch 51 reclassified NO HALT) + drift cal reports (rounds 1-13 = 13/13 carrier success) + v1_5/6/7/8_cut_reviewer_reports + 13 sibling_continuity_sweep_reports.

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
| **06 Deep Verification 旁枝入口** | **`.work/06_deep_verification/PLAN.md`** v0.6 — 字面级 PDF→KB 深审. **v1.8 prompts active 2026-04-30** (`subagent_prompts/P0_writer_pdf/md/matcher/reviewer_v1.8.md`): 5 NEW patches N24-N28 (multi-axis writer-direction motif taxonomy + cross-PDF §3.5 sweep + page-boundary Hook 21 + L1/L2 parent_section conventions) + 2 NEW STRONGLY VALIDATED status promotions (§0.5 reconciler sweep + N6 single-dispatch) + Rule D roster 56→63 + 36-item fix matrix A-AJ + Self-Validate hooks 20→21. v1.8 cut reviewer #63 codex:codex-rescue 5th burn extension PASS 36/36 SAFE_FOR_DAISY_ACK (`evidence/checkpoints/v1_8_cut_reviewer_report.md` + `v1_8_cut_reviewer_verdicts.jsonl`). v1.7 archived `archive/v1.7_final_2026-04-30/`; earlier archives `archive/v1.{1,2,3,4,5,6}_final_*/`. P1 cumulative state + per-round details = see "06 Deep Verification Multi-Session History" section above. Sub-plan `plans/P1_pdf_atomization.md` v1.0 ack'd. Schema frozen `schema/atom_schema.json` + `ledger_schema.json` (JSON Schema 2020-12, 9-enum atom_type + forward 9 verdict + reverse 5 verdict). |
| Phase 6.5 AI 平台部署 | `ai_platforms/` (总览 + 三平台子目录) |
| **Phase 6.5 通用部署范本 + 锁步看板** | `ai_platforms/_template/README.md` (10 维度规范, ChatGPT/Gemini upstream spec) + `ai_platforms/SYNC_BOARD.md` (双平台 Phase 0-5 锁步 gate; session 启动若涉及两平台必读). |
| **Phase 6.5 smoke v4 题库 + 跨 4 平台 retro** | `ai_platforms/SMOKE_V4.md` (1019 行, 17 题 v4.0 + AHP × 3) + `ai_platforms/retrospectives/` (R1/R2/PHASE5/PHASE5_28TH_REVIEWER + V5C plan); 跨 4 平台 PHASE5 v1.0 FINAL Daisy 认可 ✅ 4 平台 final state Claude 17/17 + ChatGPT 16.5/17 + Gemini R2 16/17 + NotebookLM 15/17. |
| **Phase 6.5 ChatGPT GPTs + Gemini Gems** | `ai_platforms/{chatgpt_gpt,gemini_gems}/` — ChatGPT v2.2 LIVE 8,777 bytes + Gemini v7.1 LIVE 29,836 bytes (post-V5C Q10 MINOR fix); current/system_prompt.md + dev/ + docs/. |
| **Phase 6.5 NotebookLM** | `ai_platforms/notebooklm/` (current/ + docs/ + dev/ + archive/) — Phase 4 + Phase 5 retro COMPLETE 2026-04-24 Daisy 认可; v2 架构 1 notebook × 42 sources; smoke v4 R1 15/17 (88.2%) strict PASS + AHP × 3 全 PASS+ 最强 in-KB-only; current Custom mode 8,925 chars (89.25% of 10K cap); 平台独立 retro `notebooklm/docs/RETROSPECTIVE.md` v1.0 FINAL. |
| **Phase 6.5 Claude Projects** | `ai_platforms/claude_projects/` (current/ + docs/ + dev/ + archive/) — v2 finalized 24/24 PASS capacity 77%; uploads 19 / 1.29M tokens; current/UPLOAD_TUTORIAL.md 10 章节; docs/ contains PLAN_V2 + RETROSPECTIVE_V2 + rag_decay_curve + phase7_handoff + capacity_research; design `docs/superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md`. |
| **🟢 Phase 6.5 Release v1.0 (公司发布版)** | `ai_platforms/release/v1.0/` — 27 docs + 4 平台 self_deploy bundle (26M total) ✅ 2026-04-27 v1.0 + v1.1 polish; tag `v1.0-company-release`; plan + retro `.work/07_release/{PLAN.md,RETROSPECTIVE.md}` Rule C 三段; D-RELEASE-1 Phase B runtime pivot omc-teams→Agent (1h idle→7min); Rule A omc:verifier N=3 抽检 0 drift / 0 fabrication. |
| **07 Website Phases 6/7/8 (closed)** | `.work/07_website/phase{6,7,8}/PLAN.md` + 3 handoffs at `.work/meta/website_phase{6→7,7→8,8→9}_handoff_*.md` (Rule C retros + R/G/D/C namespaces). Phase 6 Multi-dim Comparison + Phase 7 Pre-Public-Release Bundle + Phase 8 Search (Pagefind 1.5.2 17 artifacts in dist/pagefind/). Production: `https://sdtm-pedia.pages.dev/`. Reviewer reports: `phase{6,7,8}/evidence/checkpoints/phase_{N}_reviewer_report.md` (~450 lines each). Metrics post Phase 8: tsc 0 / vitest 34/34 / e2e 7/7 / build 31 HTML pages + Pagefind index. Phase 9 entry = master plan §"Phase 8 — Downloads Pipeline" (`docs/superpowers/plans/2026-04-27-sdtm-release-website.md`). |

## AI 平台双平台并行部署 (锁步规则)

涉及 **ChatGPT GPTs** (`ai_platforms/chatgpt_gpt/`) 或 **Gemini Gems** (`ai_platforms/gemini_gems/`) 任一方时, 遵守锁步规则:

1. **Session 启动自动动作**: 若用户首次提到两平台任一方, 主 session 必须先读 `ai_platforms/SYNC_BOARD.md` + 两份 `dev/evidence/_progress.json`, 报告当前锁步 Phase + 允许的下一动作, **再开工**.
2. **Gate 机制**: Phase 0-5 (启动/调研/PLAN/落地/审查/收束), 任一 Phase N 两边未都 PASS, **两边都不能进 Phase N+1**. 主 session 派发 Phase N+1 subagent 前强制校验.
3. **PASS 四条** (规则 D 强制): evidence 存在 / writer 产物合规 / 独立 reviewer subagent PASS (不同 subagent_type) / 用户口头 ack.
4. **偏离处理**: 若两平台 Phase 偏离 >1 格, 先同步慢的那边, 再推快的. **严禁跑通一边再补另一边** (会丢失 cross-pollination).
5. **并行派发模式**: 每 Phase 内用 2 个 subagent 并行 (各平台一个), 主 session 做 cross-review + 更新 `_template/` 缺陷.
6. **状态写回**: 每步操作完, 双写更新两处: 对应平台 `_progress.json` + `SYNC_BOARD.md` Phase 矩阵格.

Claude Projects 已完成, **不**参与本锁步 — 仅作为方法论参考 (`ai_platforms/claude_projects/docs/RETROSPECTIVE_V2.md`).

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
