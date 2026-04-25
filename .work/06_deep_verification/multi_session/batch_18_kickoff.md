# Batch 18 Kickoff (Multi-Session Parallel — Session C, Round 2 batches 17/18/19)

> 你是 multi-session parallel 实验 round 2 的 **session C (batch 18)**.
> 同时还有 session B (batch 17) + session D (batch 19) 在其他终端跑.
> 你只负责 p.171-180, 不动 root 文件 / audit_matrix / _progress.json.
>
> ⚠️ **batch 18 包含 mandatory drift cal** (per cadence "every 3 batches" since p.147 batch 15 + cumulative atoms post-p.147 ≥300 双触发, **batch 18 仍是 round 2 mandatory drift cal target** because batch 16 single-session=298 atoms + batch 17 ~250-300 atoms = cumulative ~550-600 ≥300, batch 18 every-3-batches 自 batch 15).
> ⚠️ **batch 18 是 P1 至今 transition 最密的 batch** — p.171 (HO→MH) + p.178 (MH→DV) + 可能 p.180 (DV→DA, 同时可能为 §6.2→§6.3 chapter-level boundary). R12 transition discipline 极高压.
> Round 2 实验 — 吸收 round 1 (batches 13-15) MULTI_SESSION_RETRO.md G-MS-4 + G-MS-7 两条缺口修.
> **注**: batch 16 已由 single-session resume 完成 (commit `7447ec0` 2026-04-25, 298 atoms / Rule A 100% effective post Option H × 2 / 2 findings O-P1-40 LOW + O-P1-41 MEDIUM). Round 2 重定义为 batches 17/18/19 (而非 round 1 prep 时计划的 16/17/18).

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 (并行 6 文件)
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (round 1 master 协议, 你 round 2 沿用)
2. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO.md` (round 1 retro 三段式, 重点 §2 G-MS-4 + G-MS-7)
3. `.work/06_deep_verification/audit_matrix.md` (READ-ONLY)
4. `.work/06_deep_verification/evidence/checkpoints/P1_batch_15_report.md` (上批 lessons + drift cal value-add 5th 案例)
5. `.work/06_deep_verification/evidence/checkpoints/drift_cal_batch_15_p147_report.md` (drift cal precedent — 你将做类似分析 + 应用 NEW1 dual-threshold)
6. `.work/06_deep_verification/subagent_prompts/v1.3_patch_candidates.md` (cumulative R-rules + NEW1-NEW5 — NEW1 dual-threshold 必须应用)

读完报告: 当前 pages_done=160 / atoms_done=4175 / batches_done=16 / findings=41 / Rule D=25 (post batch 16 single-session resume). 你将贡献 batch 18 + drift cal.

═══════════════════════════════════════════════════════════════════
## STEP 1 — TOC Ground Truth (PDF p.4 + page_index.json verified, 直接用)
═══════════════════════════════════════════════════════════════════

⚠️ Batch 18 含 **3 个 transition** (P1 至今 transition 最密):
- p.171: §6.2.5 HO → §6.2.6 MH (chapter-internal)
- p.178: §6.2.6 MH → §6.2.7 DV (chapter-internal)
- p.180: §6.2.7 DV → §6.2.8 DA OR **§6.2 → §6.3 chapter-level boundary** (DA = "Drug Accountability" 历史属 §6.3 Findings; **必须 PDF cross-check p.180 起头 chapter heading 实际 layout** — 若 PDF 显示 "§6.3 MODELS FOR FINDINGS DOMAINS" + "§6.3.1 Drug Accountability (DA)" 起头, 则为 chapter-level transition L2 sib=3; 若仅显示 "§6.2.8 Drug Accountability (DA)", 则为 chapter-internal sib=8)

| § | Title | Pages (page_index.json) | Heading Level | Sibling Index |
|---|---|---|---|---|
| §6.2.5 | Healthcare Encounters (HO) | p.167-171 (p.171 batch 18 SCOPE 起头, p.167-170 batch 17 已处理) | L3 sib=5 under §6.2 | (heading 在 p.167 batch 17, batch 18 仅 HO tail content) |
| **§6.2.6** | **Medical History (MH)** | **p.171-178 (p.171-178 batch 18 SCOPE 中)** | **L3 sib=6 under §6.2** | **batch 18 SCOPE NEW** |
| **§6.2.7** | **Protocol Deviations (DV)** | **p.178-179 (p.178-179 batch 18 SCOPE 末)** | **L3 sib=7 under §6.2** | **batch 18 SCOPE NEW** |
| **§6.2.8 OR §6.3.1** | **Drug Accountability (DA)** | **p.180-182 (p.180 batch 18 SCOPE 末)** | **L3 sib=8 under §6.2 OR L3 sib=1 under §6.3** ⚠️ TBD by PDF | **batch 18 SCOPE NEW (1 page only)** |

### parent_section 规则 (R5 anchor):
- p.171 atoms (transition page, **R12 critical**):
  - HO last bit if any → `§6.2.5 [Healthcare Encounters (HO)]`
  - §6.2.6 heading 自己 → `§6.2 [MODELS FOR EVENTS DOMAINS]`
  - MH Description/Overview/Spec content → `§6.2.6 [Medical History (MH)]`
- p.172-177 atoms → `§6.2.6 [Medical History (MH)]` (除 sub-headings 自己)
- p.178 atoms (transition page, **R12 critical**):
  - MH last bit if any → `§6.2.6 [Medical History (MH)]`
  - §6.2.7 heading 自己 → `§6.2 [MODELS FOR EVENTS DOMAINS]`
  - DV Description/Overview/Spec content → `§6.2.7 [Protocol Deviations (DV)]`
- p.179 atoms → `§6.2.7 [Protocol Deviations (DV)]` (DV is 1-2 page domain only — DV spec p.178-179, examples p.179)
- p.180 atoms (transition page, **R12 critical** — possibly chapter-level):
  - DV last bit if any → `§6.2.7 [Protocol Deviations (DV)]`
  - **若 chapter-level**: §6.3 heading 自己 → `§6 [Domain Models Based on the General Observation Classes]` + §6.3.1 heading 自己 → `§6.3 [MODELS FOR FINDINGS DOMAINS]`
  - **若 chapter-internal**: §6.2.8 heading 自己 → `§6.2 [MODELS FOR EVENTS DOMAINS]`
  - DA Description/Overview/Spec content → `§6.2.8 OR §6.3.1 [Drug Accountability (DA)]`

### Sub-headings convention (depth +1):
- §6.2.5 sub: L4 sib=1/2/3/4 (HO – Description/Overview / Specification / Assumptions / Examples 若有) — heading 在 batch 17, batch 18 仅 HO tail
- §6.2.6 sub: L4 sib=1/2/3/4 (MH – Description/Overview / Specification / Assumptions / Examples 若有)
- §6.2.7 sub: L4 sib=1/2/3/4 (DV – Description/Overview / Specification / Assumptions / Examples 若有)
- §6.2.8 OR §6.3.1 sub: L4 sib=1/2/3/4 (DA – Description/Overview / Specification / Assumptions / Examples 若有)

### Cross-Batch Sibling Continuity Pre-Context (R15)

⚠️ Prepend 到两个 writer prompt: "Prior batches HEADING continuity (post batch 16 single-session resume CONFIRMED + Option H × 2 + sister batch 17 in concurrent run):
- §6.2 [MODELS FOR EVENTS DOMAINS] = L2 sib=2 under §6 (set in batch 14)
- §6.2.1 [AE] L3 sib=1 / §6.2.2 [BE] L3 sib=2 / §6.2.3 [CE] L3 sib=3 / §6.2.4 [DS] L3 sib=4 ✅ (batch 16 confirmed) / §6.2.5 [HO] L3 sib=5 (batch 17 setting sib=5 in concurrent session, your batch 18 处理 HO tail content not heading — **若 sister batch 17 not yet committed**, accept sib=5 as expected per R15 protocol; reconciler 串行 merge will resolve)
- §6.2.6 [MH] = L3 sib=6 under §6.2 (NEW in batch 18)
- §6.2.7 [DV] = L3 sib=7 under §6.2 (NEW in batch 18)
- §6.2.8 OR §6.3.1 [DA] = TBD by PDF cross-check on p.180 (chapter-internal sib=8 OR chapter-level §6.3 NEW L2 sib=3 + §6.3.1 sib=1) (NEW in batch 18)
- L4 sub-section chain per NEW7 v1.3 candidate (PINNED post batch 16 O-P1-41 lesson): each domain Description=1 / Specification=2 / Assumptions=3 / Examples=4 deterministic — DO NOT mid-page-emergence sib assignment (collision risk).
- MH/DV/DA Examples N sibling sequences (level-5 if any) RESTART per domain — Examples in MH/DV/DA are unrelated to HO Examples sequence.
- parent_section canonical format pin (per NEW6 from batch 16 O-P1-40 lesson): use `§N.N.N Title (CODE)` form, e.g. `§6.2.6 Medical History (MH)` and `§6.2.7 Protocol Deviations (DV)` — DO NOT use `[Title]` short-bracket form."

═══════════════════════════════════════════════════════════════════
## STEP 2 — Dispatch Strategy (Option C parallel, alternation)
═══════════════════════════════════════════════════════════════════

Per alternation (batch 17 = executor+writer, batch 18 切换):

- **18a = `oh-my-claudecode:writer` × p.171-175** (writer 家族 R12 transition 验, p.171 HO→MH; R10 verbatim accuracy + NEW2 char-level self-validation 重点)
- **18b = `oh-my-claudecode:executor` × p.176-180** (executor 家族 R12 transition 验, p.178 MH→DV + p.180 DV→DA possible chapter-level)

并行派. R12 transition critical for p.171 (HO→MH) + p.178 (MH→DV) + p.180 (DV→DA possible chapter-level). 完整 self-contained prompt 同 batch 16/17 协议.

### R12 Transition Discipline (HIGHEST PRESSURE in P1 — 3 transitions in single batch)

⚠️ **3 transition pages 必须 PDF cross-check by main session pre-Rule-A** (类 batch 14 p.133 / batch 15 p.143/p.148 / batch 16 p.155 / batch 17 p.167 precedent — 7 prior R12 chapter-internal transition CLEAN; **batch 18 是首个 single batch 含 3 transitions 测试**):

1. **p.171 HO→MH**: HO last bit + §6.2.6 heading + MH Description 起头 — 期望 atom count >= 8
2. **p.178 MH→DV**: MH last bit + §6.2.7 heading + DV Description 起头 — 期望 atom count >= 6 (DV 是小 domain)
3. **p.180 DV→DA**: DV last bit + (§6.3 chapter heading L2 sib=3 if applicable) + §6.2.8/§6.3.1 heading + DA Description 起头 — 期望 atom count >= 8 (chapter-level transition 区间多)

writer/executor 必须 atomize 全部 physical content top-to-bottom 不漏 transition tail (类 batch 11 §6.1.2→§6.1.3 + batch 12 §6.1.3.3→§6.1.4 hint + batch 13 §6.1.5→§6.1.6 + batch 14 §6.1.6→§6.2/§6.2.1 chapter-level + batch 15 §6.2.1→§6.2.2 + §6.2.2→§6.2.3 + batch 16 §6.2.3→§6.2.4 + batch 17 §6.2.4→§6.2.5 — 8 prior R12 transition clean precedents 不能复发 batch 11 p.103 under-extraction 类 O-P1-28).

═══════════════════════════════════════════════════════════════════
## STEP 3 — Schema Validation (post-DONE, before drift cal + Rule A)
═══════════════════════════════════════════════════════════════════

同 batch 16/17. 额外检 3 transition pages (p.171 + p.178 + p.180) R12 验证:
- 各 transition page atom count sanity-check
- parent_section partition 区分清楚
- §6.2.6 sib=6 / §6.2.7 sib=7 / §6.2.8 OR §6.3.1 sib chain correctness
- 若 p.180 chapter-level: 验 §6.3 chapter HEADING L2 sib=3 + §6.3.1 sub L3 sib=1 同时存在 (3-zone partition 类 batch 14 p.133)

═══════════════════════════════════════════════════════════════════
## STEP 4 — Drift Cal: **MANDATORY** (cumulative 自 p.147 ≥300 + every-3-batches)
═══════════════════════════════════════════════════════════════════

⚠️ 你 MUST 触发 drift cal. 流程 (类 batch 15 p.147 precedent + NEW1 dual-threshold mandatory):

### Step 4.1: 选 target page
候选 (按 dense TABLE_ROW value-add 排序):
- **p.180** (DA start, 可能 chapter-level transition + spec table 高密) — **推荐 1st choice** (transition + density 双 value-add)
- **p.178** (DV start, 1-page domain spec table 高密) — 2nd choice
- **p.171** (MH start, spec table 高密) — 3rd choice
- **p.176-177** (MH spec table dense pages) — 4th choice
- **任一** spec table dense 页 (18a 或 18b atomized 后看哪页 atom count >= 30)

主 session 在 schema validation 后选定 1 页 (理想 1 页 atom count ~30-50, dense TABLE_ROW + spec table 含 transition 价值 加分).

### Step 4.2: 派 executor 单页 rerun
对应 baseline 的另一 agent type (若 baseline page 在 18a writer → 派 executor; 若在 18b executor → 派 writer for tiebreaker, 类 batch 12 p.118 precedent).

输出 `drift_cal_p<XXX>_<rerun-type>_rerun.jsonl`.

### Step 4.3: 比对 (**NEW1 dual-threshold mandatory**)
**双 threshold 必须 BOTH PASS** (per NEW1 v1.3 candidate, batch 15 p.147 lesson absorbed):
- (a) Strict count match ≥80%
- (b) Verbatim hash set overlap ≥80%

任一 < 80% → 触发深 root cause analysis (NOT 仅记 strict PASS 然后 ignore verbatim divergence — batch 15 p.147 案例: strict 97.4% PASS 但 verbatim 41% 揭 4 HIGH bugs).

实现:
```python
strict = abs(len(rerun) - len(baseline)) / max(len(rerun), len(baseline)) <= 0.20
verbatim_overlap = len(set(a['verbatim_hash'] for a in baseline) & set(a['verbatim_hash'] for a in rerun)) / max(len(baseline), len(rerun))
verbatim = verbatim_overlap >= 0.80
```

报告 **two thresholds** + 4-dim verdict (atom_type / verbatim / parent_section / heading_level).

### Step 4.4: 根因分析 + 决策 (类 batch 15 p.147)
若任一 FAIL <80%:
- (a) Reproducibility noise (类 O-P1-09 batch 03 QS sparse-cell) → tiebreaker `general-purpose` 第 3 派 + 2/3 majority
- (b) Writer family bug (类 O-P1-12 / O-P1-23 / O-P1-34 / batch 13 O-P1-37 / batch 14 O-P1-36 / batch 15 O-P1-36..38 数据腐败) → root-cause 定位 + Option H 类 inline 修
- (c) Convention drift (类 O-P1-33 CRF cell-splitting / O-P1-26 outer-pipe) → defer v1.3 INFO finding
- (d) Page-shift / duplication (类 O-P1-35 batch 12 p.119 / batch 14 p.137 / batch 15 p.146) → Option E full-page rerun wholesale replace + apply NEW3 outer-pipe + null-key requirement to rerun prompt

### Step 4.5: 写报告 `drift_cal_batch_18_p<XXX>_report.md`
含 strict + verbatim 双 threshold 数值 + 根因 + action + 4-dim verdict.

═══════════════════════════════════════════════════════════════════
## STEP 5 — Rule A Audit (slot #27 = plugin-dev:agent-creator AUDIT-mode)
═══════════════════════════════════════════════════════════════════

预分配 reviewer (Rule D unique, **HARDCODED 不可改, round 2 partition**, **post batch-16 slot rebalance — vercel:ai-architect 已分给 batch 17 #26**): `plugin-dev:agent-creator`

派发 prompt 显式 "Mode: AUDIT for SDTMIG v3.4 PDF atomization quality, NOT agent creation. You are an INDEPENDENT REVIEWER for PDF atomization quality. Do NOT generate agent configurations, do NOT touch plugin agent files, do NOT scaffold new agents. The 'agents' you review are JSONL atom records — verify each atom's atom_type / verbatim / parent_section / heading_level+sibling_index against the PDF ground truth + 17 cumulative R-rules + 7 v1.3 NEW candidates (NEW1-NEW7). Output verdicts JSONL + summary md to designated paths." (类 prior AUDIT pivot pattern; **8th AUDIT-mode pivot, plugin-dev family 2nd burn post slot #25 plugin-validator**, agent-creator new 子 type extending plugin-dev pool, **has Write tool natively** so no Bash heredoc adaptation needed).

### Sample build:
- Seed = 20260495
- 10 atoms 1/page stratified (p.171-180)
- Atom_type 优先: TABLE_ROW × 5 (R8/R11 验) + HEADING × 4 (R12 transition validation §6.2.6/§6.2.7/§6.2.8 OR §6.3.1 起头 sib=6/7/8|1 + 可能 §6.3 chapter L2 sib=3) + CODE_LITERAL × 1 (若有 mh.xpt/dv.xpt/da.xpt) + 若 spare slot SENTENCE
- 输出 `rule_a_batch_18_sample.jsonl`

### Reviewer prompt 含 4-dim verdict + TOC ground truth (§6.2.5/§6.2.6/§6.2.7/§6.2.8 OR §6.3.1 anchors) + 15 R-rules + R12 transition discipline 强调 (3 transition pages p.171 + p.178 + p.180).

═══════════════════════════════════════════════════════════════════
## STEP 6 — Repair (if any)
═══════════════════════════════════════════════════════════════════

同 batch 16/17. 注意 batch 18 含 drift cal + 3 transition pages, repair cycles 可能比 batch 16/17 多 (类 batch 15 6 cycles NEW P1 MAX precedent; batch 18 估计 4-7 cycles).

⚠️ Round 2 G-MS-5 NEW3 Option E rerun outer-pipe + null-key requirement 必须 inline 到 rerun prompt — 防 batch 14 91-atom bulk Option H 修工作复发.

═══════════════════════════════════════════════════════════════════
## STEP 7 — Sub-progress + Batch Report
═══════════════════════════════════════════════════════════════════

写 `_progress_batch_18.json` (schema 同 batch 17/19, batch_id=18, session_id="C", round=2, reviewer_slot=27, reviewer_type="plugin-dev:agent-creator", reviewer_audit_pivot_index=8, reviewer_family_first_burn=false, reviewer_family_name="plugin-dev" (2nd burn post #25), drift_cal_triggered=true, drift_cal_page=<XXX>, drift_cal_strict_match=<float>, drift_cal_verbatim_overlap=<float>, drift_cal_dual_threshold_verdict="PASS|FAIL", drift_cal_root_cause="<text>", drift_cal_action="Option H/E/tiebreaker/INFO defer", finding_id_range_allocated="O-P1-46..49", chapter_transition_p180="chapter-internal §6.2.8|chapter-level §6.3 NEW").

写 `P1_batch_18_report.md` (含 drift cal 段落 + NEW1 dual-threshold 数值 + 3 transition pages PDF cross-check 段, 类 batch 15 报告结构).

═══════════════════════════════════════════════════════════════════
## STEP 8 — Final Message
═══════════════════════════════════════════════════════════════════

```
PARALLEL_SESSION_18_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered_p<XXX>_strict=<float>%_verbatim=<float>%_action=<text> findings_added=<list of O-P1-48..51> chapter_transition_p180=<chapter-internal|chapter-level>
```

═══════════════════════════════════════════════════════════════════
## Round 2 Protocol Upgrade — G-MS-7 Finding ID Range Pre-allocation
═══════════════════════════════════════════════════════════════════

Round 1 缺口 G-MS-7: 各 session 用相同 O-P1-NN 累加 ID 易冲突. Round 2 修:

- Batch 16 (DONE single-session, used IDs O-P1-40 LOW + O-P1-41 MEDIUM, 2 of 4 reserved actually used; 42/43 freed for compression).
- Batch 17 (sister): 预留 IDs O-P1-42..45.
- **Batch 18 (你)**: 预留 IDs **O-P1-46..49** (4 IDs reserved, compressed forward post batch 16 actual usage). 若你新 finding > 4, 用 IDs O-P1-46a/46b/46c suffix 子序列.
- Batch 19 (sister): 预留 IDs O-P1-50..53.
- Reconciler: 预留 IDs O-P1-54+ for cross-batch / cross-session findings (e.g. R15 sibling continuity sweep / chapter-level §6.3 boundary 决议 / cross-session reviewer slot uniqueness audit).

按预分配 ID 写 `findings_added` 数组 + batch report. **不要** 用 round 1 sister-collision ID 模式 (O-P1-36..39 通用).

═══════════════════════════════════════════════════════════════════
## Round 2 Protocol Upgrade — G-MS-4 Halt Fallback Decision Tree
═══════════════════════════════════════════════════════════════════

Round 1 缺口 G-MS-4: sub-session halt 时 reconciler 决策树未 spec. Round 2 修:

任一 halt condition 触发, **session 必须**:

1. **不要** 删除 partial work — 留所有 batch file / progress / sample / verdicts (Rule B 强制) + drift cal partial outputs (rerun.jsonl + 中间分析)
2. 写 `.work/06_deep_verification/multi_session/halt_state_batch_18.md` 含 halt_reason / partial_state / incomplete_steps (注明 drift cal 是否完成 + dual-threshold 数值若有) / recommended_fallback / evidence_paths
3. echo 单行 (替代 PARALLEL_SESSION_18_DONE):
   ```
   PARALLEL_SESSION_18_HALT reason=<text> partial_atoms=<N> partial_pages=<list> drift_cal_state=<not_run|partial|completed_failed_dual> recommended_fallback=<a|b|c|d>
   ```
   - (a) reconciler retry 全 batch
   - (b) reconciler defer 本 batch + merge sister batches only
   - (c) reconciler abort experiment
   - (d) reconciler 仅完成 drift cal (若 batch atoms 完成 + drift cal halt 中段)
4. 不要 等 reconciler — 直接 exit. Reconciler 读 halt_state 决策.

═══════════════════════════════════════════════════════════════════
## Halt Conditions (per protocol, round 2 augmented)
═══════════════════════════════════════════════════════════════════

任一触发则 halt + 写 halt_state per G-MS-4:
- writer failure rate >15% in batch
- Rule A raw <70%
- ctx 用量 >80% (batch 18 是 P1 至今最复杂 batch — 3 transitions + drift cal mandatory + 可能 chapter-level §6.3 boundary, 估计 ctx 用量较 batch 15 65min/heaviest precedent 更高)
- 预分配 reviewer `plugin-dev:agent-creator` 不可派发 — Round 2: **不要** fallback 自选
- drift cal dual-threshold 双 FAIL 且 root cause 不可定位 (e.g. tiebreaker 与 baseline + rerun 都不一致 — 三方分歧) — halt + 报告 user
- 任何尝试触动 root pdf_atoms.jsonl / audit_matrix.md / _progress.json 的 code path → halt 立即

═══════════════════════════════════════════════════════════════════
## NEVER DO (同 batch 16/17)
═══════════════════════════════════════════════════════════════════

- 写 root pdf_atoms.jsonl / audit_matrix.md / _progress.json
- Self-pick reviewer slot (用 #27 plugin-dev:agent-creator hardcoded)
- Touch sister batch (17/19) files
- Skip TOC anchor / R-rules / R14 / R12 transition (3 pages!) / drift cal mandatory + NEW1 dual-threshold / NEW2 char-level self-validation / NEW3 outer-pipe rerun
- 私自决定 p.180 chapter-level vs chapter-internal — **必须** PDF cross-check + 记 finding (O-P1-48..51 范围)
- Use round 1 ID reuse pattern — **必须** 用 round 2 G-MS-7 O-P1-46..49
- Run git commit / push

开干. 第一步 STEP 0 并行 6-file Read.
