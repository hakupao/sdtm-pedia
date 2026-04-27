# .work/ MANIFEST — 文件清单与变更链

> **AI 工作入口文件** — 每次新 session 开始时先读此文件，了解文件布局和更新规则。
> 最后更新: 2026-04-27 (**07 Release v1.0 闭环 + v1.1 polish 闭环 + post-v1.1 self_deploy reorg 闭环 (4 平台 deploy 资产 bundle 入 release/v1.0/self_deploy/<p>/, ~30min, release 296K→26M, colleague 拿 release/ 即可独立部署不需访问 ai_platforms/<p>/current/, R-RELEASE-9 release 包自包含原则启示)** — v1.0 24 文件三语 release 包 1h45m 完成; v1.1 polish 30min (R5 8 项 polish 全 resolved + GLOSSARY.{zh,en,ja}.md 新增 3 文件 = 27 文件) — USER_GUIDE.zh §1 jargon split / pacing 统一 / instructions size 9011→8925 unit-aligned / 内部 codename 全清 (P3.x / smoke v4 R1 / H3 VERIFIED / AHP × 3 / Rule A-D) / Q-D 编号说明 + chatgpt+gemini §6 Q1-Q10→D0-D9 / NotebookLM §0 number wall 解构 / R-RELEASE-8 启示 polish 应作 release 标配 phase 非 deferred. v1.0 详情: Phase B runtime pivot omc-teams tmux 1h idle (3 panes 卡 Bypass Permissions) → Agent 7min (D-RELEASE-1); Phase D 5 reviewer (pr:code-reviewer en + omc:critic ja 敬体 + feature-dev cross-platform + omc:verifier DEMO + omc:critic 二轮 readability) + Rule A omc:verifier N=3 抽检 (15 段 0 numerical drift / 0 SDTM term drift / 0 fabrication) + 22 fix edits applied (MAJOR ×2 cross-language link suffix + MINOR×6 footer 公司发布版/Company Release/社内公開版 + MINOR×6 USER_GUIDE.ja terminology unify + MINOR×3 ja claude polish + MINOR×3 notebooklm orphan path + MINOR×1 DEMO D7 AESCAN + Rule A MINOR×2); R5 readability 8 项 polish 留 v1.1 (USER_GUIDE.zh §1 jargon / pacing / instructions size 单位 / 内部 codename / Q1-Q10 vs D0-D9 编号统一); retro `.work/07_release/RETROSPECTIVE.md` Rule C 三段 R-RELEASE-1..7 retain / G-RELEASE-1..6 gap / D-RELEASE-1..7 decision + Rule A/B/C/D/E 合规 + Rule E 候选回灌 ~/.claude/CLAUDE.md (omc-team→Agent pivot decision tree + HARD-STOP DIRECTIVE 模板 + Rule A 抽检 N=3 mandatory in translation tasks); git tag v1.0-company-release; 删除 3 worker one-shot kickoff (留 PLAN+RETROSPECTIVE); CLAUDE.md routing block removed. **历史 2026-04-27 (06 旁枝 round 5)**: **06 Deep Verification P1 round 5 reconciler closure (用户在另一终端跑) + round 6 batches 29/30/31 kickoff prep with TBD fill-in** — root 6146→7092 atoms / pages 250→280 / batches 25→28 / +946 atoms 3 batches; reconciler-side O-P1-92 NEW7 L6 cross-batch drift 3rd recurrence; 13 new findings O-P1-80..92 + 5 v1.4 candidates accumulated; NEW7 L6 INTRA-batch EFFECTIVE 1st live-fire 0 recurrence vs CROSS-batch INSUFFICIENT 3× cumulative → round 6 kickoff CROSS-batch handoff codification mandatory; NEW1 5th CATASTROPHIC FAIL p.270 strict 71.1% verbatim 6.7% LOWEST EVER first FAIL after 4× PASS; NEW6.b 6× streak; general-purpose family AUDIT pivot recipe family-agnostic VALIDATED 18th; 4 round 6 kickoffs ready (batch_29/30/31 + reconciler_kickoff_round6) 双阶段 skeleton+TBD-fill 完成 (46 TBD-RECONCILER 占位全清); reviewer slots #38 pr-review-toolkit:code-reviewer + #39 superpowers:code-reviewer (drift cal carrier 6th time) + #40 pr-review-toolkit:silent-failure-hunter = 2 NEW family first burn + 1 intra-family depth burn; CLAUDE.md routing rule 切到 round 6 + 删 v1.3 cut 路由 + Background context 全段更新). **历史 2026-04-27 (v1.3 cut)**: **06 Deep Verification v1.3 prompt formal cut COMPLETED** — 4 v1.3 prompts written `P0_writer_pdf/P0_writer_md/P0_matcher/P0_reviewer` codifying 13 items A-M (R1-R15 + O-P1-26 + NEW1-NEW8 + NEW6/NEW6.b L4 self-parent + NEW7 L4-L7 chain + NEW7 L6 procedural sub-batch handoff template + NEW7 L4 group-container branch + NEW8.b/c + G-MS-12/12.a/13); Rule D reviewer slot #35 `oh-my-claudecode:critic` AUDIT verdict PASS 13/13 (1 non-blocking changelog precision fix applied); v1.2 archived to `subagent_prompts/archive/v1.2_final_2026-04-27/`; batch 26+ kickoff §2 references switched to v1.3; inline-prepend overhead RETIRED (~5-7 hours total savings across P1 closure 30+ batches remaining); v1.3 cut DEFERRED 4 prior rounds resolved). **历史 2026-04-26 (**06 Deep Verification P1 batch 23-25 multi-session round 4 + reconciler + round 5 batches 26/27/28 kickoff prepped** — round 4 (23/24/25, +644 atoms 226+208+210) 3 终端物理并行 + 1 reconciler 串行收尾 = post-round-4 cumulative **6146 atoms / 250 页 (45.5% of 535) / 25 batches / 1 dropout (Rule B archived) / 39 repair cycles across 14 batches**; **Round 5 prep**: 4 kickoffs written (batch_26/27/28_kickoff.md + reconciler_kickoff_round5.md), CLAUDE.md routing rule 切到 round 5, reviewer slots #35-#37 pre-allocated (omc:analyst + omc:architect + general-purpose NEW family first burn), drift cal MANDATORY batch 27, finding ID range O-P1-80..91, NEW7 L6 procedural sub-batch handoff codified mandatory (round 3+4 RECURRENCE = formal mandatory). **Round 4 highlights**: reconciler-side Option H 4-atom NEW7 L6 LB-Examples sub-batch context drift fix (O-P1-79 LOW = 2nd recurrence of round 3 O-P1-68 motif) + drift cal batch 24 p.233 NEW1 dual-threshold STRONGLY VALIDATED 4th time (strict 94.1% PASS / verbatim 41.2% FAIL = DIRECTION REVERSED 8th + value-add 9th precedent) + NEW6.b L4 self-parent EFFECTIVE proactively 3× (IS/LB/Microbiology Domains first-attempt correct) + NEW round-4 L5 RESTART under L4 group-container precedent §6.3.5.7.1 MB (O-P1-75 INFO) + writer-family wide-TABLE_HEADER 8th batch corruption batch 24 Option E wholesale rerun + 3 family pools EXHAUSTED post round 4 (vercel + plugin-dev + feature-dev). MULTI_SESSION_RETRO_ROUND_4.md 26180 bytes (12 R-MS retain + 6 G-MS gap + 7 D-MS decision). v1.3 cut TRIPLE-RECOMMENDED + ULTRA-CRITICAL 4th time deferred per Rule D = EMERGENCY-CRITICAL escalation BEFORE batch 27 next mandatory drift cal. **历史 2026-04-26 (round 2+3 之前)**: round 2 (17/18/19) + round 3 (20/21/22) +1327 atoms cumulative 5502 atoms / 220 pages / 22 batches / 36 repair cycles; round 3 reconciler 0 batch-jsonl fixes + 1 metadata renumber (batch 21 finding IDs O-P1-63/64/65 → O-P1-59/60/61 — sub-session mis-read kickoff allocation O-P1-59..62 wrote O-P1-63..66 colliding with batch 22 reserved range = G-MS-13 NEW gap surfaced); **12 AUDIT-mode pivots cross-family 累 (#20-#31)** all 0 FP / 0 inverted; **TOC anchor methodology firmly locked at 14 consecutive batches n=140 cumulative anchored audit 0 FP / 0 inversion across vercel/pr-review-toolkit/oh-my-claudecode/plugin-dev 4 families with 2 family pools COMPLETED post round 3 (vercel 3/3 + plugin-dev 3/3) + omc-family burned 5×**; **drift cal batch 18 p.180 + batch 21 p.205 NEW1 dual-threshold STRONGLY VALIDATED 2× (round 2+3) — 7th drift cal value-add 超 Rule A precedent + DIRECTION REVERSED 6th-7th + 1-atom CPSCMRKS character-swap caught batch 21 + 7-atom DALNKID multi-motif caught batch 18**; **NEW7 deep-nesting L7 sub-example precedent established round 3** (Example 1a/1b L7 sib=1, 2 under Example 1 L6 sib=1 batch 21); **G-MS-11 NEW6 dual-form fix EFFECTIVE round 3** (0 violations batch 20 230 atoms vs round 2 batch 18 5 violations + 1 violation batch 22 GF L4 self-parent inline-fixed); **G-MS-12 density alarm 2× validated round 3** (batch 20 p.192 FALSE POSITIVE + batch 21 p.208 TRUE POSITIVE → Option E rerun 10→23 atoms +130%); **writer-family wide-TABLE_ROW corruption 7th batch P1 cumulative** (batch 22 first Option-E-resistant case p.214 a014 column-shift 2-cycle); ~50% wall savings 3 rounds running with 0 quality regression; **v1.3 prompt formal cut DOUBLE-RECOMMENDED** (3rd time deferred per Rule D writer/reviewer isolation, evidence DOUBLE-saturated post round 3 + 2 NEW round 3 candidates NEW7 L7 codification + NEW8 substring n-gram cross-check vs canonical CDISC variable list catches CPSCMRKS adjacent-letter swap that NEW2 single-character iteration misses); `multi_session/MULTI_SESSION_RETRO_ROUND_3.md` Rule C 强制 8 段 + 11 R-MS retain + 8 G-MS gap + 6 D-MS decision 写完. **历史 2026-04-25**: P1 batch 13-15 multi-session round 1 +677 atoms (cumulative **3877 atoms / 150 页 / 15 batches / 27 repair cycles across 8 batches**; **5 AUDIT-mode pivots cross-family 累 (#20 pr / #21 omc-debugger / #22 vercel-perf-1st / #23 omc-designer / #24 vercel-deploy-2nd)** all 0 FP / 0 inverted; **TOC anchor methodology firmly locked at 7 consecutive batches n=70 cumulative anchored audit 0 FP / 0 inversion across vercel/pr-review-toolkit/oh-my-claudecode 3 families**; **drift cal batch 15 p.147 strict 97.4% PASS / verbatim 41% LOW root caused writer 15b multi-page systemic STUDIID×8 + supple→suppbe + bs.xpt swap + relspec REFID + relrec corruption + p.146 18-atom under-extraction → Option E ×3 + Option H ×3 = 6 repair cycles NEW P1 SINGLE-BATCH MAX**; **R15 cross-batch sibling continuity sweep PASS 0 fixes** (sub-sessions correctly applied R15 from kickoff context); ~50% wall savings vs serial baseline (~75 vs ~150 min) with 0 quality regression / 0 protocol violation / 0 cross-session Rule D collision; **v1.3 prompt formal cut RECOMMENDED** (R10 ≥4 / R11 ≥3 / R12 ≥4 / R14 ≥4 / R15 ≥4 / O-P1-26 ≥5 batches evidence threshold met) **execution deferred to dedicated v1.3 cut session per Rule D writer/reviewer isolation** + 5 NEW v1.3 candidates (NEW1 drift cal dual-threshold / NEW2 writer spec-table self-validation / NEW3 Option E rerun outer-pipe+null-key / NEW4 dataset filename HEADING-vs-CODE_LITERAL codification / NEW5 R12 chapter-level transition strengthening); `multi_session/MULTI_SESSION_RETRO.md` 写完 (Rule C 强制 8 段). **历史 2026-04-25 凌晨**: P1 batch 02-03 + 30-page milestone gate PASS via Option 2' — 三 ack 决策落档 (PLAN v0.5 / P1 sub-plan v1.0 / spec Option A), batch 02 [writer] 323 atoms **9/9 atom_type 单批覆盖首次** + CODE_LITERAL 63 首批浮现, batch 03 [executor] 269 atoms Ch.3 narrative-heavy; cumulative **918 atoms / 30 页 / 3 batches**; 30-page milestone: **Rule A 30-atom 独审 100% PASS** (slot #12 superpowers:code-reviewer 首烧) **but Drift 3-way FAIL** (strict exec↔writer 67.5% / tiebreaker general-purpose 37.5% / 3-way unanimous 19.2%, QS sparse-cell TABLE_ROW verbatim reproducibility, **非 prompt 语义 drift 是 PDF table OCR 固有 lossy parse**); **O-P1-07 resolved X'** (document-specialist 无 Write tool → 2-type alternation only, writer_pool 降 2, writer_banned 扩 7); **O-P1-09 MEDIUM drift sparse-cell** 挂 defer P1 末; MIXED gate 决策 **Option 2'** (加密 Rule A cadence 30-page → per-batch 10-atom ≥90% 作 reproducibility safety net, v1.3 prompt 规则 defer); Rule D 烧 12/16; 下 session 从 `_progress.json.recovery_hint` 开跑 batch 04 writer × p.31-40. **历史 2026-04-24 深夜**: 06 Deep Verification P0 Pilot PASS + v1.2 schema frozen + P1 batch 1 (326 atoms). **历史 2026-04-24 晚**: Phase 6.5 **NotebookLM async lane Phase 5 SIGN-OFF 闭环** ✅: retro v1.0 FINAL + UPLOAD_TUTORIAL v1.0 + 4 索引同步 + reviewer 10 findings 全修; Daisy 认可; 详见 worklog `2026-04-24 Phase 6.5 NotebookLM async lane Phase 5 SIGN-OFF` 段. **历史 2026-04-22 PM**: Phase 6.5 **NotebookLM P3.8 执行 9/10 PASS + v4 升级路径决策**: P3.8 10 SMOKE v3 Q1-Q10 A/B 经 cowork Chrome MCP 代跑, sanity 3/3 + Q1-Q10 **9/10 strict PASS (90%)**, Q9 Pinnacle 21 PUNT (NotebookLM in-KB-only 架构限制 safety-correct 但 generalization 能力 short, Phase 4 拟重分类 'platform N/A'); **主 session 独立复判暴露 v3.1 题库 Q10 (b) 判据基于错前提** — SUPPTS 在 SDTMIG v3.4 不存在 (TS 属 Trial Design 不用 SUPPQUAL, 长 TSVAL 内部派生 TSVAL1-n), NotebookLM 纠错前提作 PASS+ 但讽刺的是沿错判据答反被奖励; **用户 meta insight**: smoke v3 当前只测'给正确前提答对', 缺'给错前提能否纠错'维度, 用户常问错前提希望模型纠错而非幻觉; **决策 smoke v3 → v4 升级路径** (新 session 执行): (1) 审计 smoke_v3_questions_draft.md v3.1 Q1-Q14 前提真实性 Rule A 扩张到题库设计 (派第 11 种 subagent_type oh-my-claudecode:document-specialist background); (2) 强制修 Q10 (b) + 其他发现的前提错; (3) 新增 AHP × 3 (variable trap + cross-domain trap + deprecated-version trap) → smoke v4.0; (4) v3 历史结果标 SUPERSEDED 不回溯重评分; (5) 4 平台 (Claude / ChatGPT / Gemini / NotebookLM) 跑 smoke v4 R1 baseline; (6) R1 FAIL 改 system prompts (尤其 anti-hallucination 锚点 ChatGPT/Gemini) → R2 retest; 详见 ai_platforms/SMOKE_V4_DESIGN_HANDOFF.md; NotebookLM PLAN v2.1 → v2.2 (P3.8 题库 smoke v2.1 → smoke v3 Q1-Q10, 跨平台同期可比); _progress.json 加 p3_8_completion 块 findings 1-5 + user_meta_insight + decision_smoke_v4_design_plan; P3.8 reviewer (Rule D gap) 挂新 session 并派)

---

## 变更链 (Change Chains)

当你修改了某个文件，**必须沿链检查并更新所有关联文件**。
每个链有一个触发条件和一条更新路径。

---

### Chain A: 验证进度链

**触发**: 验证步骤完成、发现问题、步骤状态变更

```
03_verification/plan.md              ← 更新步骤状态
  ↓
03_verification/results/step*.md     ← 添加详细验证结果
  ↓
03_verification/issues_found.md      ← 汇总问题（如有）
  ↓
meta/findings.md                     ← 全局质量问题记录
  ↓
meta/worklog.md                      ← 记录工作内容
  ↓
progress.json                        ← 更新程序化进度
  ↓
../docs/PROGRESS.md                       ← 更新面向读者的进度看板
```

---

### Chain B: 工作日志链

**触发**: 任何阶段性工作完成

```
meta/worklog.md                      ← 记录做了什么
  ↓
progress.json                        ← 更新状态字段
  ↓
../docs/PROGRESS.md                       ← 更新看板
```

---

### Chain C: 新阶段启动链

**触发**: 开始新的工作阶段（如 Phase 6 优化）

```
0N_xxx/ (新目录)                     ← 创建工作文件
  ↓
meta/worklog.md                      ← 记录启动
  ↓
../docs/PROGRESS.md                       ← 更新看板
  ↓
MANIFEST.md (本文件)                  ← 注册新目录和文件
```

---

### Chain D: 溯源链

**触发**: knowledge_base/ 内容变更

```
knowledge_base/ 文件变更
  ↓
meta/mapping.md                      ← 更新源文件→产出映射（如有新源）
  ↓
../docs/TRACEABILITY.md                   ← 更新溯源矩阵
  ↓
meta/worklog.md                      ← 记录变更
```

---

### Chain E: 方案变更链

**触发**: 项目方案/架构调整

```
00_planning/*.md                     ← 修改方案文档
  ↓
meta/worklog.md                      ← 记录决策变更
  ↓
../docs/PROGRESS.md                       ← 如影响阶段则更新
  ↓
../README.md / ../README_CN.md       ← 如影响项目描述则更新
```

---

## 计划导航 (Plan Map)

所有计划/TODO 文件的从属关系、状态和执行顺序。新 session 开始时先看这里，决定该做什么。

```
03_verification/plan.md ──── Phase 5 验证主计划 ──── [已完成]
│
├─→ Step 0~3.6 ······························ [已完成]
│
├─→ repair_plan.md ── Issue 2 修复 ·········· [已完成/归档]
│   │  派生原因: Step 3-4/3-5 执行中发现内容空洞
│   │
│   └─→ followup_plan.md ── 残余风险排查 ··· [已完成]
│        内容: M1~M5 五项抽查任务
│
└─→ Step 4 汇总报告 ························ [已完成]
     产出: results/step4_summary_report.md

04_optimization/retrieval_optimization.md ── Phase 6 检索优化 ── [P0-P2 已完成, P3→Phase 7]
     内容: P0~P3 四项优化任务（ROUTING.md、反向索引等）
     前置: Phase 5 完成后再开始

ai_platforms/ ── Phase 6.5 AI 平台部署 ── [Claude v1 完成 (9/9 PASS); Claude v2 终态 v2.6 完成 (24/24 A/B PASS, 0 衰减, capacity 77%); 2026-04-20 Reorg 重组到 current/docs/dev/archive; 2026-04-20 晚 ai_platforms/_template/ 范本抽象 + ChatGPT/Gemini 骨架升级]
     总览: ai_platforms/README.md
     三平台路线: chatgpt_gpt/ROADMAP.md, claude_projects/ROADMAP.md, gemini_gems/ROADMAP.md
     **通用部署范本**: ai_platforms/_template/ — 10 维度规范 (README + APPLY_CHECKLIST + 00-09) 抽象自 claude v2 方法论, ChatGPT/Gemini 及未来新平台的 upstream spec
     **Claude 新结构入口**: claude_projects/README.md (指向 current/docs/dev/archive 四层)
     Claude 当前可部署 (发布版): claude_projects/current/ (uploads/ 19 文件 + system_prompt.md + upload_manifest.md + UPLOAD_TUTORIAL.md 用户部署教程 + README.md 发布版总览)
     Claude 方法论文档: claude_projects/docs/ (PLAN_V2 + RETROSPECTIVE_V2 + rag_decay_curve + phase7_handoff + capacity_research)
       - PLAN_V2.md (1852 行, 8 阶段 ~30 任务, 内部路径引用为 reorg 前语境, 见文件头 post-reorg note)
       - RETROSPECTIVE_V2.md (7 章复盘, 过 Rule D 独立复核 CONDITIONAL_PASS→PASS)
       - rag_decay_curve.md (7 数据点 v1→v2.6 + 4 段观察 + 结论 + 6 条 Phase 7 actionable)
       - phase7_handoff.md (6 条 actionable + 5 未解问题 + 5 步待办)
       - capacity_research.md (v1 Step 14 后 200K 假设修正)
     Claude 开发过程 (冷区): claude_projects/dev/ (reorg 前为 scripts_v2+output_v2/evidence_v2; 内部路径引用保留历史语境, 见 dev/README.md 映射表)
       - scripts/ 6 Python 脚本 (rebuild_chapters + extract_examples_data + extract_terminology_terms + score_domains + score_codelists + build_v2_stage)
       - evidence/ (trace.jsonl + _progress.json + _phase_summary.md + H1_reviewer.md + subagent_prompts/ 14 + checkpoints/ + failures/ + rag_decay_observations/)
       - ab_reports/ STAGE_V2.{1,2,3,4,6}_AB_REPORT.md (v2.5 被 v2.6 合并 skipped)
       - checkpoints/ CHECKPOINT_V2.{1..6}_HANDOFF.md
       - test_results.md (T1-T22 + 2 优先级验证完整矩阵)
     Claude 历史归档 (冻结): claude_projects/archive/
       - RETROSPECTIVE.md (v1 三段式 + 四条规则已固化全局 CLAUDE.md)
       - v1/docs/ (PLAN.md + UPLOAD_TUTORIAL.md + claude_project_instructions.md + claude_project_setup.md + V2_SESSION_STARTER.md 过渡产物)
       - v1/scripts/ (11 Python 脚本, build_all.py 一键重建)
       - v1/uploads/ (11 上传文件 + evidence/ + _progress.json + capacity_check.md + test_results.md + BASELINE_README.md)
     ChatGPT GPTs: chatgpt_gpt/ ── [待开始 (范本就绪 2026-04-20), Tier 2, 预计 2 批到位]
       - 入口: README.md + ROADMAP.md (按范本升级, P11-P13 含 20 文件硬限 + TableAware 分段约束)
       - Phase 0 填空: docs/platform_profile.md (A-K 10 组字段, Phase 1 调研待补)
       - 四层占位: current/ + dev/ + archive/ (启动后填)
     Gemini Gems: gemini_gems/ ── [待开始 (范本就绪 2026-04-20), Tier 1-2, 预计 1 批全上]
       - 入口: README.md + ROADMAP.md (按范本升级, P11-P12 单批到位 + 末尾召回验证)
       - Phase 0 填空: docs/platform_profile.md (A-K 10 组字段, 3 问简化调研预告)
       - 四层占位: current/ + dev/ + archive/ (启动后填)
     Claude 实际产出构成 (v2.6 终态 19 文件):
       - 00-08: v2.1 chapters byte-exact expand (重建 v1 结构)
       - 09: examples 高频 28 域 (v2.2, 112,697 tokens)
       - 10: examples 其余 35 域 (v2.3, 48,897 tokens) — 63 域 examples 全覆盖
       - 11a/11b/11c: terminology top 200 按 subdir 拆 (v2.4, 351,752 tokens)
       - 12a/12b/12c: terminology mid rank 201-500 按 subdir 拆 (v2.5, 377,939 tokens)
       - 13a/13c: terminology tail 用户优先级重平衡 (v2.6, 188,981 tokens; 6 giants Deferred stub, 13b by design 不存在)
     Claude v2 设计文档: docs/superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md
     Claude v2 plan pointer: docs/superpowers/plans/2026-04-18-phase6.5-claude-v2-expansion.md (skill 约定)
     前置: Phase 6 P0-P2 完成（已满足）

05_rag_kg/ ── Phase 7 RAG + 知识图谱 + 数据集校验 ── [设计完成/待实施]
     设计文档: docs/DESIGN_RAG_KG.md
     session 记录: 05_rag_kg/session_2026-04-16_design.md
     前置: Phase 6 P0-P2 完成（已满足）
```

**下一步执行顺序建议**:
1. ~~`followup_plan.md` M1~M5 抽查（验证收尾）~~ ✅ 已完成
2. ~~`plan.md` Step 4 汇总报告（验证关门）~~ ✅ 已完成
3. ~~`retrieval_optimization.md` P0~P2（检索优化）~~ ✅ 已完成
4. `ai_platforms/` Phase 6.5 三平台部署 ← **当前位置**
5. `docs/DESIGN_RAG_KG.md` Phase 7 实施

---

## 目录结构

```
.work/
├── MANIFEST.md              ← 本文件（入口 + 链路图）
├── progress.json            ← 程序化进度追踪（脚本读写）
│
├── 00_planning/             ← Phase 0: 分析与方案设计
│   ├── source_relationship.md    源文件关系梳理
│   └── restructure_plan.md       知识库重构方案（核心方案文档）
│
├── 01_generation/           ← Phase 1: xlsx 自动生成
│   └── scripts/
│       ├── generate_spec.py       spec.md 生成脚本
│       ├── generate_terminology.py 术语文件生成脚本
│       └── validate_spec.py       spec.md 校验脚本
│
├── 02_indexing/             ← Phase 2: PDF 页码索引
│   ├── page_index.json           权威页码索引（63 域，全部 verified）
│   └── page_index_old.json       旧版备份
│
├── 03_verification/         ← Phase 5: 全量验证
│   ├── plan.md                   验证计划与进度总表
│   ├── issues_found.md           问题汇总
│   ├── followup_plan.md          后续排查计划（残余风险与盲区）
│   ├── repair_plan.md            Issue 2 修复计划（写/审分离流程）
│   ├── results/                  验证结果（按步骤编号）
│   │   ├── step1_assumptions.md
│   │   ├── step2_examples_summary.md
│   │   ├── step2_examples_detail.md
│   │   ├── step3_1_model_small.md
│   │   ├── step3_2_model_rest.md
│   │   ├── step3_3_chapters_small.md
│   │   ├── step3_4_ch04.md
│   │   ├── step3_5_ch08_ch10.md
│   │   └── step4_summary_report.md
│   ├── scans/                    图像溯源扫描
│   │   ├── ig_chapters.md
│   │   ├── ig_domains_d1~d4.md
│   │   ├── v20.md
│   │   └── image_inventory.md
│   └── rescan/                   重新扫描与问题调查
│       ├── a1~a7.md
│       ├── diff.md
│       └── issue1_investigation.md
│
├── 04_optimization/         ← Phase 6: 检索精度优化（P0-P2 已完成）
│   ├── retrieval_optimization.md  P0~P3 优化任务清单与执行结果
│   ├── p1_cross_reference_plan.md P1 交叉引用执行计划
│   ├── p2_variable_index_plan.md  P2 变量反向索引执行计划
│   └── scripts/
│       ├── generate_variable_index.py   P2 脚本（生成 VARIABLE_INDEX.md）
│       └── generate_cross_references.py P1 脚本（生成 Cross References 段）
│
├── 05_rag_kg/               ← Phase 7: RAG + 知识图谱 + 数据集校验
│   └── session_2026-04-16_design.md  设计讨论 session 记录（需求/方案/场景模拟/决策）
│
└── meta/                    ← 贯穿全程的元信息
    ├── worklog.md                 工作日志（中断恢复入口）
    ├── retrospective.md           阶段性反思（Issue 根因 + 四条预防规则）⚑ 必读
    ├── mapping.md                 源文件→产出文件映射
    ├── findings.md                质量问题全局记录
    └── user_actions.md            用户操作指南
```

## Phase 编号映射

| .work/ 目录 | 项目 Phase | 说明 |
|-------------|-----------|------|
| `00_planning/` | Phase 0 | 分析与方案设计 |
| `01_generation/` | Phase 1 | xlsx 自动生成 spec.md + terminology |
| `02_indexing/` | Phase 2 | PDF 页码索引 |
| *(无 .work/ 目录)* | Phase 3-4 | PDF 提取，产出直接写入 knowledge_base/ |
| `03_verification/` | Phase 5 | 全量验证 |
| `04_optimization/` | Phase 6 | 检索精度优化 (P0-P2 已完成) |
| *(根目录 `ai_platforms/`)* | Phase 6.5 | AI 平台部署 (进行中) |
| `05_rag_kg/` | Phase 7 | RAG + 知识图谱 + 数据集校验 (设计完成) |

## 快速参考

| 要做什么 | 先读 |
|---------|------|
| 恢复中断的工作 | `meta/worklog.md` → `progress.json` |
| 了解完整方案 | `00_planning/restructure_plan.md` |
| 查看验证状态 | `03_verification/plan.md` |
| 查 domain 页码 | `02_indexing/page_index.json` |
| 查源文件→产出映射 | `meta/mapping.md` |
| 查质量问题 | `meta/findings.md` |
| 查后续 TODO | `04_optimization/retrieval_optimization.md` |
| **Phase 6.5 AI 平台部署** | **`../ai_platforms/README.md`** — 三平台部署总览与路线图 |
| **Phase 6.5 通用部署范本** | **`../ai_platforms/_template/README.md`** — 10 维度规范 (README + APPLY_CHECKLIST + 00-09) 抽象自 Claude v2 方法论 (2026-04-20) |
| **Phase 6.5 ChatGPT GPTs 入口** | **`../ai_platforms/chatgpt_gpt/README.md`** — 待开始 (范本就绪), Tier 2 / 2 批到位 / 20 文件硬限 / 可 GPT Store 发布 |
| **Phase 6.5 Gemini Gems 入口** | **`../ai_platforms/gemini_gems/README.md`** — 待开始 (范本就绪), Tier 1-2 / 1 批全上 / 1M 窗口 / 仅个人 |
| **Phase 6.5 Claude 入口 (reorg 后)** | **`../ai_platforms/claude_projects/README.md`** — 新结构 current/docs/dev/archive 导航 (2026-04-20) |
| **Phase 6.5 Claude 部署教程** | **`../ai_platforms/claude_projects/current/UPLOAD_TUTORIAL.md`** — 发布版完整制作教程 (10 章节, 去版本化, 用户视角) |
| **Phase 6.5 Claude 当前可部署 (发布版)** | **`../ai_platforms/claude_projects/current/`** — 19 上传 + system_prompt + upload_manifest + UPLOAD_TUTORIAL + README |
| **Phase 6.5 Claude v1 复盘** | **`../ai_platforms/claude_projects/archive/RETROSPECTIVE.md`** — v1 Step 1-12 三段式 + 四条规则 A/B/C/D 固化 (2026-04-18) |
| **Phase 6.5 Claude v1 压缩计划** (archive) | **`../ai_platforms/claude_projects/archive/v1/docs/PLAN.md`** — v1 方案 B 详细落地计划 + §7 执行手册 |
| **Phase 6.5 Claude v1 上传教程** (archive) | **`../ai_platforms/claude_projects/archive/v1/docs/UPLOAD_TUTORIAL.md`** — v1 Step 13-14 手动操作 + T1-T8 测试 |
| **Phase 6.5 Claude 容量调研** | **`../ai_platforms/claude_projects/docs/capacity_research.md`** — 200K 假设错, paid 套餐 RAG 自动扩 10x, 实际容量 ~3-4M |
| **Phase 6.5 Claude v2 设计** | **`../docs/superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md`** — 中庸 5 批 / ~50% 容量 / 16-18 文件 / RAG 衰减曲线 (2026-04-18) |
| **Phase 6.5 Claude v2 计划** | **`../ai_platforms/claude_projects/docs/PLAN_V2.md`** — 1852 行 / 8 阶段 / ~30 Tasks (内部路径 reorg 前语境) |
| **Phase 6.5 Claude v2 执行进度** | **`../ai_platforms/claude_projects/dev/evidence/_progress.json`** — status=completed, 5 checkpoints_acked (v2.1-v2.4 + v2.6), phase_final_metrics 快照 |
| **Phase 6.5 Claude v2 RAG 衰减曲线** | **`../ai_platforms/claude_projects/docs/rag_decay_curve.md`** — 7 数据点 + 4 段跨批观察 + 结论 + 6 条 Phase 7 actionable |
| **Phase 6.5 Claude v2 Phase 7 交接** | **`../ai_platforms/claude_projects/docs/phase7_handoff.md`** — 6 条 actionable + 5 问题 Q1-Q5 + 实施前 5 步待办 |
| **Phase 6.5 Claude v2 复盘** | **`../ai_platforms/claude_projects/docs/RETROSPECTIVE_V2.md`** — Rule C 强制产物, 7 章, 过 Rule D 独立复核 |
| **Phase 6.5 Claude v2 A/B 报告** | **`../ai_platforms/claude_projects/dev/ab_reports/STAGE_V2.{1,2,3,4,6}_AB_REPORT.md`** — 5 批 A/B 报告 (v2.5 合并 skipped), v2.6 终态 24/24 PASS |
| **Phase 6.5 Claude v2 测试矩阵** | **`../ai_platforms/claude_projects/dev/test_results.md`** — T1-T22 + T-core-reb/T-supp-reb + v2.1-v2.6 stage 汇总 |
| **Phase 6.5 Claude v2 H1 独立复核** | **`../ai_platforms/claude_projects/dev/evidence/H1_reviewer.md`** — RETROSPECTIVE_V2 过 code-reviewer CONDITIONAL_PASS → PASS evidence |
| **Phase 6.5 Claude v2 开发过程 (冷区)** | **`../ai_platforms/claude_projects/dev/`** — scripts/ + evidence/ + ab_reports/ + checkpoints/ + test_results.md (reorg 前路径映射见 dev/README.md) |
| **Phase 7 设计文档** | **`../docs/DESIGN_RAG_KG.md`** — RAG + 知识图谱 + 数据集校验 |
| Phase 7 session 记录 | `05_rag_kg/session_2026-04-16_design.md` |
| **Phase 6.5 NotebookLM 入口** | **`../ai_platforms/notebooklm/README.md`** — **Phase 4 COMPLETE (2026-04-23) + Phase 5 retro DRAFT (2026-04-24)**: smoke v4 R1 **15/17 (88.2%) strict PASS** + **AHP × 3 全 PASS+ 最强** (in-KB-only 天然反虚构, 并列 Claude) + P3.8 reviewer 12th slot PASS + P3.9 三档切换 PASS (5 PASS + 1 PARTIAL Public≠gallery 新发现 + 1 SKIP 接受残余风险); 异步 lane 不参与 SYNC_BOARD; 跨 4 retro `PHASE5_RETROSPECTIVE.md` **v1.0 FINAL 2026-04-24 Daisy 认可 ✅**; 本平台独立 `docs/RETROSPECTIVE.md` **v1.0 FINAL 2026-04-24 Daisy 认可 ✅** + `current/UPLOAD_TUTORIAL.md` v1.0 同批产出 (10 章节 276 行) |
| **Phase 6.5 NotebookLM 平台独立 retro** | **`../ai_platforms/notebooklm/docs/RETROSPECTIVE.md`** — Rule C 强制产物 **v1.0 FINAL 2026-04-24 Daisy 认可 ✅**, 508 行, 三段式 (§1 保留 R-NBL-1-8 + §2 缺口 G-NBL-1-6 + §3 决策 D-NBL-1-6 含 v1→v2 pivot 作关键案例) + §4 _template 补丁 (4 吸收 10a/10b.1/10b.2/15 + 4 新候选 16-19) + §5 跨 4 retro 呼应 + §6 Rule A/B/C/D/E 合规 (含 category error 承认) + §7 下一步 + §8 版本 (v0.1→v0.2→v1.0 FINAL) + Appendix A evidence 速查 + Appendix B 元反思 (含 9,011 chars 错的 self-catch 实证); writer = 主 session, reviewer = `oh-my-claudecode:critic` CONDITIONAL_PASS 8.0 → 10 findings 全修升 v0.2 → Daisy ack 升 v1.0 FINAL; `reviewer_notes` @ `dev/evidence/phase5_retrospective_reviewer.md` |
| **Phase 6.5 NotebookLM UPLOAD_TUTORIAL** | **`../ai_platforms/notebooklm/current/UPLOAD_TUTORIAL.md`** v1.0 FINAL 2026-04-24 — 276 行, 10 章节 + 附录 (§0 前置 Pro tier / §1 新建 notebook / §2 Chat Custom mode 8,925 chars / §3 42 sources 上传 + silent fail 防线 / §4 等 indexing / §5 Smoke 3 题 sanity / §6 完整回归 smoke v4 R1 17 题 / §7 3 档分享切换 Public≠gallery 新发现 / §8 排错手册 8 症状映射 / §9 升降级扩容 / §10 后续路径 + ICEBOX + 文档索引 + 附自查清单) |
| **Phase 6.5 NotebookLM smoke v4 R1 结果** | **`../ai_platforms/notebooklm/dev/evidence/smoke_v4_results.md`** + **`smoke_v4_answers/`** (17 答案文件: Q1-Q14 + AHP1-3 + sanity × 3) — 15/17 strict PASS (88.2%) 远超 71% 阈; 6 PASS + 8 PASS+ + 2 PARTIAL (Q11/Q12 supplemental PUNT) + 1 FAIL (Q9 Pinnacle 21 safety-correct 架构限制) |
| **Phase 6.5 NotebookLM P3.9 三档切换演练** | **`../ai_platforms/notebooklm/dev/evidence/share_level_toggle_drill.md`** v1.0 FINAL (2026-04-23) — 6 子步 (a-f) × 5 PASS + 1 PARTIAL (c) + 1 SKIP (f); 新发现 **Public ≠ auto gallery 广播** (画廊是 curated Featured); H3 hypothesis VERIFIED + 深化 |
| **Phase 6.5 NotebookLM P3.8 reviewer (12th slot)** | **`../ai_platforms/notebooklm/dev/evidence/p3_8_reviewer_notes.md`** — feature-dev:code-reviewer 独立复核 9/10 strict PASS 闭合; 5 findings 评级 4/5 正确 (Finding 2 建议 MEDIUM→MINOR) + 2 遗漏 findings (Q3 LEVEL / Q8 (c) Q10 之外 premise-correction 第二例); Rule D chain cumulative 12 种 |
| **Phase 6.5 NotebookLM P3.2 手顺 + 执行 log** | **`../ai_platforms/notebooklm/dev/checkpoints/CHECKPOINT_P3.2_HANDOFF.md`** (手顺) + **`../ai_platforms/notebooklm/dev/evidence/p3_2_upload_log.md`** (执行 log, 5-tile 速览 + Chat STUDYID sanity + source count 三处交叉锁 42 全 PASS, 主 session Chrome MCP 复核) |
| **Phase 6.5 NotebookLM P3.3 evidence** | **`../ai_platforms/notebooklm/dev/evidence/chat_mode_toggle_test.md`** (210 行) — 3 组问答 (AESER Core × Custom/Learning Guide/Custom controlled comparison) + H3 VERIFIED PASS + Q-REV-1 CLOSED + F-1 闭合 log (WebFetch 官方 help 证 UI 支持表格, minimal table test 分支 a UI 真表格渲染) + F-2 同题非幂等观察 (挪 P3.8 A/B 评分吸收) |
| **Phase 6.5 NotebookLM v2 PLAN** | **`../ai_platforms/notebooklm/docs/PLAN.md`** — 610 行 v2 (Q1 双锚 A4 结构+P3.4.5 语义); 第 9 种 subagent_type architect PASS 后全 findings 闭合 |
| **Phase 6.5 NotebookLM 架构 pivot 记录** | **`../ai_platforms/notebooklm/archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md`** — v1→v2 pivot 证据链 + 被舍弃决策 D1-D10 + 保留资产 A-F + _template 补丁 #10a/10b.1/10b.2 |
| **Phase 6.5 NotebookLM Phase A evidence** | **`../ai_platforms/notebooklm/dev/evidence/`** — pre_upload_audit + req_vars_full_set (176 独立 Req) + source_mapping + req_vars_coverage_audit (∅ gap PASS) + phase_a_webui_small_sample + phase2_v2_reviewer |
| **Phase 6.5 NotebookLM 42 bucket config** | **`../ai_platforms/notebooklm/dev/scripts/bucket_config.json`** + **`../ai_platforms/notebooklm/current/uploads/MANIFEST.md`** — 295 md → 42 bucket concept cluster (63/63 domains + 176/176 Req ∅ gap) |
| **AI 工作质量规则** | **`meta/retrospective.md`** ⚑ 四条预防规则必须遵守 |
| 查残余风险排查计划 | `03_verification/followup_plan.md` |
