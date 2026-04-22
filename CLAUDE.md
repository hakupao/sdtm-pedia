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
| **Phase 6.5 通用部署范本** | **`ai_platforms/_template/README.md`** — 10 维度规范 (README + APPLY_CHECKLIST + 00 platform_profile + 01 directory_structure + 02 workflow + 03 research + 04 plan + 05 solution + 06 review + 07 agent_dispatch + 08 evidence + 09 closure), 抽象自 Claude v2 方法论, ChatGPT/Gemini 及未来平台的 upstream spec |
| **Phase 6.5 双平台锁步看板 (强制读)** | **`ai_platforms/SYNC_BOARD.md`** — ChatGPT GPTs + Gemini Gems 并行部署 Phase 0-5 锁步 gate; session 启动若涉及两平台任一方, 第一件事读本文件定位当前 Phase |
| **Phase 6.5 smoke v4 唯一入口 (3 合 1, 2026-04-22)** | **`ai_platforms/SMOKE_V4.md`** — 1019 行, 路径 B bundled: §1 R1 执行 Plan (4 平台跑题顺序 + 前置 + 手顺 + 阈值 + 评分 + R1→R2 gate) + §2 17 题题库 v4.0 (Q1-Q10 4 平台共用 + Q11-Q14 ChatGPT 专属 + **AHP1-3 anti-hallucination probe 4 平台共用**) + §3 跨平台对比矩阵骨架 (4 列 × 17 行, R1 跑完填). 替代 smoke_v3_questions_draft.md + SMOKE_V4_R1_EXECUTION_PLAN.md + cross_platform_compare_v4.md (3 源合并). **Step 1-5 完成 (audit 11th slot + v4 bundled patch + AHP×3 + 3 平台 v3 SUPERSEDED + P3.8 reviewer 12th slot)**, Step 6 R1 pending. 历史归档 `ai_platforms/archive/smoke_history/` (5 份: SMOKE_QUESTIONS_V2 + N5_3_QUESTIONS_DESIGN + SMOKE_V4_DESIGN_HANDOFF + smoke_v3_audit_notes + PHASE4_PLAN) |
| Phase 6.5 smoke v2 10 题 (archived) | `ai_platforms/archive/smoke_history/SMOKE_QUESTIONS_V2.md` — **SUPERSEDED** by v3 (then v4.0 2026-04-22); 4 业务维度 10 题 (场景 3 + 规则 3 + 映射 2 + 鉴别 2), 保留作历史 trace |
| Phase 6.5 Gemini C 方案 (Node 4 架构) | `ai_platforms/gemini_gems/docs/PLAN_V2_C.md` — 舍弃 terminology 重整 4 文件为业务问答优化 (01 导航 + 02 spec+assumptions + 03 examples + 04 业务弹药包) |
| Phase 6.5 ChatGPT batch 2 规划 | `ai_platforms/chatgpt_gpt/docs/PLAN_BATCH2.md` — 维持原策略保留 terminology, 新增 5 文件 (05 assumptions + 06 examples + 07/08/09 terminology 高频/问卷补充/低频 3 档) |
| **Phase 6.5 ChatGPT GPTs 入口** | **`ai_platforms/chatgpt_gpt/README.md`** — 待开始 (范本就绪 2026-04-20), Tier 2 / 2 批到位 / 20 文件硬限 / 可 GPT Store 发布; Phase 0 初稿见 `chatgpt_gpt/docs/platform_profile.md`; 进度见 `chatgpt_gpt/dev/evidence/_progress.json` |
| **Phase 6.5 Gemini Gems 入口** | **`ai_platforms/gemini_gems/README.md`** — 待开始 (范本就绪 2026-04-20), Tier 1-2 / 1 批全上 / 1M 窗口 / 仅个人; Phase 0 初稿见 `gemini_gems/docs/platform_profile.md`; 进度见 `gemini_gems/dev/evidence/_progress.json` |
| **Phase 6.5 NotebookLM 入口** | **`ai_platforms/notebooklm/README.md`** — Phase 3 **P3.8 执行 9/10 strict PASS (2026-04-22 PM, smoke v3 Q1-Q10, cowork 代跑 sanity 3/3 + Q1-Q10 9/10, Q9 Pinnacle 21 PUNT 作架构限制 in-KB-only safety-correct 非能力 FAIL)** + **主 session 独立复判暴露 smoke v3.1 Q10 (b) 判据基于错前提** (SUPPTS 在 SDTMIG v3.4 不存在, TS 属 Trial Design 用 TSVAL1-n 内部派生) + **用户 meta insight → smoke v3 → v4 升级决策** (加 3 类 AHP Anti-Hallucination Probe 测纠错能力, 4 平台 R1 baseline → R2 system prompt 迭代); **PLAN v2.1 → v2.2 (2026-04-22 PM, P3.8 题库 smoke v2.1 → smoke v3 Q1-Q10 对齐 ChatGPT+Gemini N5.3)**; v2.1 决策全保留 (P3.5/P3.6/P3.7 ICEBOX); 异步 lane 不参与 SYNC_BOARD; v2 架构 **1 notebook × ≤50 sources + 3 档分享切换** (pivot from v1 3 notebook); **下一步新 session**: smoke v4 设计审计 + Q10 (b) patch + 加 AHP × 3 + 4 平台 R1, 详见 `ai_platforms/archive/smoke_history/SMOKE_V4_DESIGN_HANDOFF.md`; P3.8 reviewer (Rule D 11th subagent_type) 未派挂新 session |
| **Phase 6.5 NotebookLM v2.2 PLAN** | **`ai_platforms/notebooklm/docs/PLAN.md`** — v2.2 修订 2026-04-22 PM (v2.1 基础上: P3.8 题库 smoke v2.1 → **smoke v3 Q1-Q10** 对齐 ChatGPT+Gemini N5.3 Full A/B Generalization Probe; 题源 `ai_platforms/SMOKE_V4.md §2` v3.1 Q1-Q10; PASS 阈值保 ≥9/10 (~90%) 不降; 维度: v2 = 04 预设 baseline, v3 = generalization probe 测 v3.4 新域/域边界/Timing/CT/Pinnacle/SUPP; §6 P3.8 Task 完整重写 + §7 A/B 矩阵重写 + Sanity 前置 3 题 + v3.4 新域 FAIL 作 P10 (d) 新归因路径; 9 处更新; v2.1 原 ICEBOX 决策全保留) — **v2.1 2026-04-22**: P3.5/P3.6/P3.7 Studio 三件套挪 ICEBOX post-project optional; 第 9 种 subagent_type (architect) CONDITIONAL_PASS 84% → PASS; 第 10 种 subagent_type (scientist) P3.4.5 CONDITIONAL_PASS 8.5/10 Q1 红线双锚闭合 |
| **Phase 6.5 NotebookLM 架构 pivot 记录** | **`ai_platforms/notebooklm/archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md`** — v1 (3 notebook) → v2 (1 notebook × ≤50) pivot 完整证据链 + 被舍弃决策 D1-D10 + 保留资产 A-F; v1 Q7 "Mode A/B 叙事合成伪约束" 教训作 _template 补丁 #10a/10b.1/10b.2 |
| **Phase 6.5 NotebookLM 执行进度** | **`ai_platforms/notebooklm/dev/evidence/_progress.json`** — Phase A 全 PASS + P3.1 merge + P3.2 Web UI 上传 + P3.3 Custom mode + H3 VERIFIED + F-1 初 CLOSED + P3.4 indexing smoke 10/10 + P3.4.5 Q1 红线语义级 8.5/10 + **P3.8 完成 (2026-04-22 PM, smoke v3 Q1-Q10 9/10 strict PASS, p3_8_completion 块 8 字段含 sanity_preflight_3q 3/3 / per_question_verdicts_cowork 10 题逐题 / main_session_independent_review_findings 5 条 (Q1 bookkeeping MINOR + Q3 BECAT vs BETERM 判据过窄 MEDIUM + **Q10 (b) 判据前提错 HIGH** SUPPTS 不存在 / Q9 PUNT 架构限制 Phase 4 Scoping / Rule D 11th reviewer gap) / user_meta_insight smoke v3 缺纠错维度 / decision_smoke_v4_design_plan 7 步 / handoff_docs_new_session / rule_a_b_c_d_e 合规)**; **v2.2 2026-04-22 PM**: ab_matrix_plan_v2 题库 v2.1→v3 Q1-Q10 重写 (standard_questions_source 切换 + question_type_distribution_v3 六维度 + pass_threshold_unchanged + sanity_preflight_3q + p3_8_carry_over_absorbed v3.4 新域 P10 (d)); **next_action 重定向 smoke_v4_design_session** 新 session 审计/patch/加 AHP/4 平台 R1/R2 迭代; **10-subagent_type Rule D 链 cumulative** (11th slot 挂新 session 合并派 P3.8 reviewer + smoke v4 审计) |
| **Phase 6.5 NotebookLM P3.2 手顺 + 执行 log** | **`ai_platforms/notebooklm/dev/checkpoints/CHECKPOINT_P3.2_HANDOFF.md`** (250 行手顺, 融合 PLAN §6 P3.2 + A5' 小样 + MANIFEST 42 清单 + Rule B 回退 + 明示 scope) + **`ai_platforms/notebooklm/dev/evidence/p3_2_upload_log.md`** (执行 log, notebook URL + 42/42 indexed + 5-tile metadata 对照表 + Chat STUDYID [1][2] citation 证据 + 用户偏离透明记录) |
| **Phase 6.5 NotebookLM P3.3 evidence** | **`ai_platforms/notebooklm/dev/evidence/chat_mode_toggle_test.md`** — 210 行; 3 组问答 AESER Core controlled comparison (Custom / Learning Guide / Custom 回切) + H3 三档切换 VERIFIED PASS (UI per-chat-session 可动态切, 非 notebook 锁定) + Q-REV-1 CLOSED + F-1 UI 表格渲染初 CLOSED log (WebFetch 官方 help answer/16179559 + minimal table test 分支 a 命中 UI 真表格) — **注: F-1 于 2026-04-22 P3.4.5 真实漂移 8/10 打脸后重开 F-1-recurring, 本文件 CLOSED 判断属极端 case 外推**; F-2 同题非幂等挪 P3.8 吸收 |
| **Phase 6.5 NotebookLM P3.4.5 evidence (Rule A 正本, Q1 红线语义级自证)** | **`ai_platforms/notebooklm/dev/evidence/phase3_task_P3.4.5_req_semantic_audit.md`** (306 行 evidence + Step 5 scientist reviewer 完整填 + 用户仲裁 + Exit) + **`p3_4_5_prompt_log.md`** (566 行 HC-4 raw prompt + raw answer 全文 dump, 10 题 + 2 HC-3 补题, 每题 inline citation count + F-1 漂移 + 主判分) + **`p3_4_5_sampling_log.md`** (86 行, base seed 20260422 + 8 层递 seed + 10 变量约束校验) — CONDITIONAL_PASS 8.5/10, 语义 10/10 顶阈值 + citation 7/10, scientist 终审 + 用户仲裁 A, HC-3 bucket 38 头段 PASS (CDR [38_ct_questionnaires_part1_22.md]×3) / 尾段 INCONCLUSIVE (MMSE FT 归属事件), F-3 citation T2 题型偏向 Reviewer 新发现 |
| **Phase 6.5 NotebookLM P3.8 evidence (smoke v3 Q1-Q10 跨平台对比基线)** | **`ai_platforms/notebooklm/dev/checkpoints/CHECKPOINT_P3.8_HANDOFF.md`** (213 行手顺, 6 Steps: 题库 + 阈值 / notebook 状态不动 / sanity 3 题 / Q1-Q10 逐题 / 落档 / 回报) + **`dev/evidence/smoke_v3_results.md`** (cowork self-score 9/10 strict PASS + 逐题 verdict table + 总分 + carry-over 观察 + 主结论) + **`dev/evidence/smoke_v3_answers/`** (11 文件: Q1-Q10_answer.md + sanity_questions.md, DOM 回读原文) — 主 session 独立复判 5 findings (Q1 bookkeeping MINOR / Q3 BETERM vs BECAT MEDIUM / **Q10 (b) 判据前提错 HIGH SUPPTS 不存在** / Q9 PUNT 架构限制 Phase 4 Scoping / Rule D 11th reviewer gap); Q1-Q3 v3.4 新域 3/3 PASS; Q4-Q5 域边界 2/2 PASS; Q6-Q8 Timing+CT 3/3 PASS; Q9 FAIL (in-KB-only safety-correct); Q10 PASS+ (NotebookLM 正确纠错 SUPPTS 前提错, 反衬判据 bug) |
| **Phase 6.5 smoke v4 设计 handoff (新 session 入口)** | **`ai_platforms/archive/smoke_history/SMOKE_V4_DESIGN_HANDOFF.md`** — 9 段自足可独立启动: (0) 当前状态已完成/待执行 / (1) Q10 (b) 关键 finding 修订方向 (SUPPTS 不存在 → PASS 必识别 TSVAL1-n 替代) / (2) Step 1 审计 Task 校验 matrix 6 维度 + agent 派发 (建议第 11 种 subagent_type `oh-my-claudecode:document-specialist` opus background read-only + WebFetch) / (3) Step 2-4 Patch Plan 含 Q10 (b) new 题干/判据 draft + AHP1/2/3 完整 draft (variable/cross-domain/deprecated-version trap) / (4) Step 5 v3 SUPERSEDED 策略 (3 平台已跑结果标记) / (5) Step 6 4 平台 R1 顺序+阈值+评分矩阵 / (6) Step 7 R2 改 prompt 典型 pattern / (7) Rule D chain 10 种已烧 + 11th slot 候选 / (8) 相关路径速查 / (9) 执行前 checklist — 用户 meta insight "smoke v3 缺给错前提能否纠错维度, 用户常问错前提希望纠错非幻觉" 驱动 |
| **Phase 6.5 NotebookLM Req 全集** | **`ai_platforms/notebooklm/dev/evidence/req_vars_full_set.md`** — 176 独立 Req 变量 (9 通用 + 167 领域专属), Q1 零丢失审计基线 |
| **Phase 6.5 NotebookLM 42 bucket 配置** | **`ai_platforms/notebooklm/dev/scripts/bucket_config.json`** + **`current/uploads/MANIFEST.md`** — 295 md → 42 bucket concept cluster (63/63 domains + 176/176 Req ∅ gap), 8 slot headroom; bucket 02/42 加 `_auto_source` 字段由 merge_sources.py 特殊派发 |
| **Phase 6.5 NotebookLM 42 uploads md (P3.2 上传产物)** | **`ai_platforms/notebooklm/current/uploads/*.md`** × 42 — merge_sources.py 合成, 总 1,582,085 words, 最大 bucket 302K < 500K/source cap, 0 over-cap 0 missing; 每文件顶部含 NotebookLM source metadata header 便于 citation 反查 |
| **Phase 6.5 NotebookLM Chat Custom mode** | **`ai_platforms/notebooklm/current/instructions.md`** — 9,011 chars = 90% of 10K cap (11% headroom); 13 behavior rules + SDTM 锚点 (AESER=Exp 非 Req / LBNRIND 全写 / NY C66742 / ISO 8601 / C-code 字面 / Day 1 无 Day 0 / RELREC+RELSPEC+RELSUB 三件套 / SUPP-- 结构); authoritative layer 优先级 spec > ch04 > CT > assumptions > examples |
| **Phase 6.5 Claude 入口 (reorg 后)** | **`ai_platforms/claude_projects/README.md`** — 新结构导航入口, 指向 current/docs/dev/archive 四层 |
| **Phase 6.5 Claude 部署教程 (用户视角)** | **`ai_platforms/claude_projects/current/UPLOAD_TUTORIAL.md`** — 10 章节完整制作教程 (前置 / 建 Project / System Prompt / 上传 / Smoke Test / 回归 / 排错 / 升降级 / 团队 / 后续), 已去版本化 |
| Phase 6.5 Claude 当前可部署 (发布版) | `ai_platforms/claude_projects/current/` (uploads/ 19 文件 + system_prompt.md + upload_manifest.md + UPLOAD_TUTORIAL.md + README.md, 1.29M tokens, capacity 77%) |
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
