# Batch 19 Kickoff (Multi-Session Parallel — Session D, Round 2 batches 17/18/19)

> 你是 multi-session parallel 实验 round 2 的 **session D (batch 19)**.
> 同时还有 session B (batch 17) + session C (batch 18) 在其他终端跑.
> 你只负责 p.181-190, 不动 root 文件 / audit_matrix / _progress.json.
>
> ⚠️ **batch 19 含 2 chapter-internal transitions**: p.183 (DA→DD) + p.185 (DD→EG). R12 transition discipline 高压.
> ⚠️ **batch 19 是 §6.3 Findings 章首个真正多 domain batch** — DA tail (p.181-182) + 完整 DD (p.183-184, 2 页 mini-domain) + EG 起头 (p.185-190 partial, EG ends p.192). 5 domains touched if include DA continuation.
> Round 2 实验 — 吸收 round 1 (batches 13-15) MULTI_SESSION_RETRO.md G-MS-4 (halt fallback) + G-MS-7 (finding ID range pre-allocation) 两条缺口修.
> **注**: batch 16 已由 single-session resume 完成 (commit `7447ec0` 2026-04-25, 298 atoms / Rule A 100% effective post Option H × 2 / 2 findings O-P1-40 LOW + O-P1-41 MEDIUM). Round 2 重定义为 batches 17/18/19.

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 (并行 6 文件)
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (round 1 master 协议, 你 round 2 沿用)
2. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO.md` (round 1 retro 三段式, 重点 §2 G-MS-4 + G-MS-7)
3. `.work/06_deep_verification/audit_matrix.md` (READ-ONLY)
4. `.work/06_deep_verification/evidence/checkpoints/P1_batch_15_report.md` (上批 lessons + drift cal value-add 5th 案例)
5. `.work/06_deep_verification/evidence/checkpoints/P1_batch_16_report.md` (single-session resume + Option H × 2 + 2 v1.3 NEW6/NEW7 candidates 灯塔)
6. `.work/06_deep_verification/subagent_prompts/v1.3_patch_candidates.md` (cumulative R-rules + NEW1-NEW7 — NEW6 parent_section canonical format pin + NEW7 level-4 sub-section deterministic sib chain 必须应用)

读完报告: 当前 pages_done=160 / atoms_done=4175 / batches_done=16 / findings=41 / Rule D=25 (post batch 16 single-session resume). 你将贡献 batch 19.

═══════════════════════════════════════════════════════════════════
## STEP 1 — TOC Ground Truth (PDF p.4-5 + page_index.json verified, 直接用)
═══════════════════════════════════════════════════════════════════

⚠️ Batch 19 含 **2 chapter-internal transitions** (DA→DD at p.183 + DD→EG at p.185). 此外 p.181 是 DA Specification table tail (从 batch 18 p.180 续过来), 注意 R15 cross-batch sib continuity.

| § | Title | Pages (PDF p.4 TOC verified) | Heading Level | Sibling Index |
|---|---|---|---|---|
| §6.3.1 | Product Accountability (DA) | p.180-182 (p.181-182 batch 19 SCOPE 起头, p.180 batch 18 已设 sib) | L3 sib=1 under §6.3 | (heading 在 p.180 batch 18, batch 19 仅 DA Assumptions/Examples tail) |
| **§6.3.2** | **Death Details (DD)** | **p.183-184 (完整 mini-domain 2 页)** | **L3 sib=2 under §6.3** | **batch 19 SCOPE NEW** |
| **§6.3.3** | **ECG Test Results (EG)** | **p.185-192 (p.185-190 batch 19 SCOPE 末 + 6 页, 留 p.191-192 给 batch 20)** | **L3 sib=3 under §6.3** | **batch 19 SCOPE NEW** |
| §6.3.4 | Inclusion/Exclusion Criteria Not Met (IE) | p.193 onward | L3 sib=4 under §6.3 | (out of batch 19 scope) |

### parent_section 规则 (R5 anchor, NEW6 canonical full-form pin):

- p.181-182 atoms → `§6.3.1 Product Accountability (DA)` (DA – Assumptions + DA – Examples 1/2/3 tail)
- p.183 atoms (transition page DA→DD, **R12 critical**):
  - DA last bit if any (DA Examples table tail) → `§6.3.1 Product Accountability (DA)`
  - §6.3.2 heading 自己 → `§6.3 [MODELS FOR FINDINGS DOMAINS]`
  - DD Description/Overview/Specification 起头 → `§6.3.2 Death Details (DD)`
- p.184 atoms → `§6.3.2 Death Details (DD)` (DD Assumptions + DD Examples)
- p.185 atoms (transition page DD→EG, **R12 critical**):
  - DD last bit (dd.xpt + ds.xpt + relrec.xpt cross-domain Example 2 tail) → `§6.3.2 Death Details (DD)`
  - §6.3.3 heading 自己 → `§6.3 [MODELS FOR FINDINGS DOMAINS]`
  - EG Description/Overview/Specification 起头 → `§6.3.3 ECG Test Results (EG)`
- p.186-190 atoms → `§6.3.3 ECG Test Results (EG)` (EG Specification table 大量 spec rows)

### Sub-headings convention (depth +1, NEW7 deterministic chain pin):

- §6.3.1 sub: L4 sib=1/2/3/4 (DA – Description/Overview / Specification / Assumptions / Examples) — heading 部分在 batch 18, batch 19 仅 DA Assumptions+Examples tail (sib=3 + sib=4)
- §6.3.2 sub: L4 sib=1/2/3/4 (DD – Description/Overview / Specification / Assumptions / Examples) — **全在 batch 19 NEW**
- §6.3.3 sub: L4 sib=1/2 (EG – Description/Overview / Specification) — batch 19 仅 EG 起头 2 sub-sections (Assumptions+Examples 留 batch 20)

⚠️ **NEW7 pinned chain**: Description=1 / Specification=2 / Assumptions=3 / Examples=4 deterministic — DO NOT mid-page-emergence sib assignment (collision risk per batch 16 O-P1-41 lesson).

### Cross-Batch Sibling Continuity Pre-Context (R15)

⚠️ Prepend 到两个 writer prompt: "Prior batches HEADING continuity (post batch 16 single-session resume CONFIRMED + sister batches 17 + 18 in concurrent run):
- §6.2 [MODELS FOR EVENTS DOMAINS] = L2 sib=2 under §6 (set in batch 14)
- §6.2.1-§6.2.7 chain set across batches 14-18 (你不动 §6.2.x atoms, only confirm continuity post-merge by reconciler)
- §6.3 [MODELS FOR FINDINGS DOMAINS] = L2 sib=3 under §6 (NEW in batch 18 if p.180 chapter-level transition confirmed; **若 batch 18 sister determined chapter-internal §6.2.8 instead, halt + report — batch 19 R15 depends on §6.3 chapter heading existence**)
- §6.3.1 [DA] = L3 sib=1 under §6.3 (NEW in batch 18, your batch 19 处理 DA Assumptions+Examples tail content not heading)
- §6.3.2 [DD] = L3 sib=2 under §6.3 (NEW in batch 19, sib continuity from §6.3.1 sib=1)
- §6.3.3 [EG] = L3 sib=3 under §6.3 (NEW in batch 19, sib continuity from §6.3.2 sib=2)
- L4 sub-section chain per NEW7 v1.3 candidate: each domain Description=1 / Specification=2 / Assumptions=3 / Examples=4 deterministic.
- DD Examples N + EG Examples N (level-5 if any) RESTART per domain — independent across domains.
- parent_section canonical format pin (per NEW6 from batch 16 O-P1-40 lesson): use `§N.N.N Title (CODE)` form (e.g. `§6.3.2 Death Details (DD)`) — DO NOT use `[Title]` short-bracket form."

═══════════════════════════════════════════════════════════════════
## STEP 2 — Dispatch Strategy (Option C parallel, alternation)
═══════════════════════════════════════════════════════════════════

Per alternation (batch 18 = writer+executor, batch 19 = 奇 → executor-led):

- **19a = `oh-my-claudecode:executor` × p.181-185** (executor 家族 R12 transition 验, p.183 DA→DD + p.185 DD→EG)
- **19b = `oh-my-claudecode:writer` × p.186-190** (writer 家族 EG Specification dense table 验, R10 verbatim accuracy + NEW2 char-level self-validation 重点 — 防 writer 14b/15b cluster 复发)

并行派. R12 transition critical for p.183 (DA→DD) + p.185 (DD→EG). 完整 self-contained prompt 同 batch 17/18 协议.

### R12 Transition Discipline (HIGH PRESSURE for p.183 + p.185)

⚠️ **2 transition pages 必须 PDF cross-check by main session pre-Rule-A** (类 batch 14 p.133 / batch 15 p.143/p.148 / batch 16 p.155 / batch 17 p.167 (sister) / batch 18 p.171/p.178/p.180 (sister) precedents):

1. **p.183 DA→DD**: DA last bit (Examples table tail) + §6.3.2 heading L3 sib=2 + DD Description/Overview/Specification 起头 — 期望 atom count >= 8 (DD spec table 含 ~12 variables)
2. **p.185 DD→EG**: DD last bit (dd.xpt + ds.xpt + relrec.xpt cross-domain Example 2 tail) + §6.3.3 heading L3 sib=3 + EG Description/Overview/Specification 起头 — 期望 atom count >= 12 (cross-domain table tail dense + EG spec table 起头)

writer/executor 必须 atomize 全部 physical content top-to-bottom 不漏 transition tail. **9 prior R12 transition clean precedents** (batch 14 p.133 / 15 p.143 / 15 p.148 / 16 p.155 / 17 p.167 sister / 18 p.171 sister / 18 p.178 sister / 18 p.180 sister) — 不能复发 batch 11 p.103 under-extraction 类 O-P1-28.

⚠️ **NEW2 critical for 19b writer-family** (R10 verbatim accuracy + spec-table char-level self-validation): EG Specification table p.185-190 含 ~25-30 variables (EGTESTCD/EGTEST/EGCAT/EGSCAT/EGORRES/EGORRESU/EGSTRESC/EGSTRESN/EGSTRESU/EGSTAT/EGREASND/etc), 每个 variable + Core column + CT column 必须 char-level verify pre-DONE — 防止 writer 14b AERLPRT/AELLT cluster + writer 15b STUDIID×8 + supple→suppbe 复发.

═══════════════════════════════════════════════════════════════════
## STEP 3 — Schema Validation (post-DONE, before Rule A)
═══════════════════════════════════════════════════════════════════

同 batch 17/18. 额外检 2 transition pages (p.183 + p.185) R12 验证:
- 各 transition page atom count sanity-check
- parent_section partition 区分清楚 (DA tail vs §6.3.2 heading vs DD content; DD tail vs §6.3.3 heading vs EG content)
- §6.3.2 sib=2 / §6.3.3 sib=3 sib chain correctness
- L4 sub-section chain per NEW7 deterministic (DD: Description=1/Specification=2/Assumptions=3/Examples=4 + EG: Description=1/Specification=2)

═══════════════════════════════════════════════════════════════════
## STEP 4 — Drift Cal: NOT triggered batch 19
═══════════════════════════════════════════════════════════════════

跳过. Last mandatory drift cal 在 batch 18 (sister) p.<TBD by sister> per cadence. Next mandatory = batch 21. Ad-hoc 触发条件同 batch 17. **19b writer-family 高警戒** (writer-family 5/5 batches drift cal value-add 命中 typo/under-extraction cluster 历史 — O-P1-12 batch 03 / O-P1-23 batch 09 / O-P1-34 batch 12 / batch 13 O-P1-37 / batch 14 O-P1-36 / batch 15 O-P1-36+37+38), 主 session 务必 PDF cross-check 19b dense EG spec table pages (p.186-190).

═══════════════════════════════════════════════════════════════════
## STEP 5 — Rule A Audit (slot #28 = oh-my-claudecode:qa-tester AUDIT-mode)
═══════════════════════════════════════════════════════════════════

预分配 reviewer (Rule D unique, **HARDCODED 不可改, round 2 partition**, 9th AUDIT pivot, omc family 3rd burn post #21 debugger + #23 designer): `oh-my-claudecode:qa-tester`

派发 prompt 显式 "Mode: AUDIT for SDTMIG v3.4 PDF atomization quality, NOT QA testing. NOT tmux session management. NOT interactive CLI testing. You are an INDEPENDENT REVIEWER for PDF atomization quality. Do NOT run interactive tests, do NOT use tmux, do NOT manage CLI sessions. The 'tests' you perform are independent literal-verification audits — verify each atom's atom_type / verbatim / parent_section / heading_level+sibling_index against the PDF ground truth + 17 cumulative R-rules + 7 v1.3 NEW candidates (NEW1-NEW7). Output verdicts JSONL + summary md to designated paths." (类 prior AUDIT pivot pattern; **9th AUDIT-mode pivot, omc family 3rd burn**, qa-tester semantic close to AUDIT — "QA testing" 的核心是质量验证, AUDIT pivot 仅限定 review 对象 from interactive CLI testing → PDF atom quality, **has Write tool natively** so no Bash heredoc adaptation needed).

### Sample build (Bash + Python):
- Seed = 20260500
- 10 atoms 1/page stratified (p.181-190)
- Atom_type 优先: TABLE_ROW × 5 (R10/R11/O-P1-26/NEW2 spec table char verify — DD spec + EG spec dense rows) + HEADING × 3 (R12 transition validation §6.3.2 sib=2 + §6.3.3 sib=3 + L4 sub-section chain per NEW7 deterministic verify) + SENTENCE × 1 (DA Assumptions narrative) + CODE_LITERAL × 1 (dd.xpt + eg.xpt strict CODE_LITERAL classification per NEW4)
- 输出 `rule_a_batch_19_sample.jsonl`
- **NEW7 critical sample target**: 至少 1 HEADING 验证 §6.3.2 DD L4 sub-section chain (Description=1/Specification=2/Assumptions=3/Examples=4 deterministic) — 防止 batch 16 O-P1-41 sib chain off-by-one 复发
- **NEW6 critical sample target**: 至少 1 atom 横跨 §6.3.1→§6.3.2 transition page p.183 验证 parent_section 用 canonical full form `§6.3.2 Death Details (DD)` 而非 `[DD]` 短括号 — 防止 batch 16 O-P1-40 format split 复发

### Reviewer prompt (类 batch 17/18 prior reviewer prompts) 含:
- 4-dimension verdict (atom_type / verbatim / parent_section / heading_level+sibling_index)
- TOC ground truth prepend (§6.3.1 / §6.3.2 / §6.3.3 anchors)
- 17 R-rules embedded (R1-R15 cumulative + O-P1-26 + NEW1-NEW7 candidates) + R12 transition discipline 强调 (2 transition pages)
- Output: `rule_a_batch_19_verdicts.jsonl` + `rule_a_batch_19_summary.md`
- Final message: `RULE_A_DONE pass=N partial=N fail=N weighted=X.XX`
- Threshold ≥90% weighted → PASS; ≥80% <90% → CONDITIONAL_PASS; <80% → FAIL halt + report 等 reconciler 决定 (per round 2 G-MS-4 halt fallback)

═══════════════════════════════════════════════════════════════════
## STEP 6 — Repair (if any finding)
═══════════════════════════════════════════════════════════════════

同 batch 17/18. 注意 chapter-internal transitions p.183 + p.185 易出 R12 violation, 主 session 务必 PDF cross-check p.182/p.183 + p.184/p.185 4 页确认 transition tail 完整 + new domain Description 起头不漏.

⚠️ Round 2 G-MS-5 NEW3 Option E rerun outer-pipe + null-key requirement 必须 inline 到 rerun prompt — 防 batch 14 91-atom bulk Option H 修工作复发.

⚠️ NEW7 sib chain repair: 若 Rule A 揭 §6.3.2 DD 或 §6.3.3 EG 的 L4 sub-section chain off-by-one (类 batch 16 O-P1-41), 直接 Option H inline fix sib_index per deterministic Description=1/Specification=2/Assumptions=3/Examples=4.

═══════════════════════════════════════════════════════════════════
## STEP 7 — Sub-progress + Batch Report
═══════════════════════════════════════════════════════════════════

写 `.work/06_deep_verification/evidence/checkpoints/_progress_batch_19.json` (schema 同 batch 17/18, batch_id=19, session_id="D", round=2, reviewer_slot=28, reviewer_type="oh-my-claudecode:qa-tester", reviewer_audit_pivot_index=9, reviewer_family_first_burn=false, reviewer_family_name="oh-my-claudecode" (3rd burn post #21+#23), finding_id_range_allocated="O-P1-50..53", chapter_internal_transitions=["p.183_DA_to_DD", "p.185_DD_to_EG"]).

写 `.work/06_deep_verification/evidence/checkpoints/P1_batch_19_report.md` (类 batch 17/18 report 结构).

═══════════════════════════════════════════════════════════════════
## STEP 8 — Final Message
═══════════════════════════════════════════════════════════════════

```
PARALLEL_SESSION_19_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list of O-P1-50..53>
```

═══════════════════════════════════════════════════════════════════
## Round 2 Protocol Upgrade — G-MS-7 Finding ID Range Pre-allocation
═══════════════════════════════════════════════════════════════════

Round 1 缺口 G-MS-7: 各 session 用相同 O-P1-NN 累加 ID 易冲突. Round 2 修:

- Batch 16 (DONE single-session, used IDs O-P1-40 LOW + O-P1-41 MEDIUM, 2 of 4 reserved actually used; 42/43 freed for compression).
- Batch 17 (sister): 预留 IDs O-P1-42..45.
- Batch 18 (sister): 预留 IDs O-P1-46..49.
- **Batch 19 (你)**: 预留 IDs **O-P1-50..53** (4 IDs reserved). 若你新 finding > 4, 用 IDs O-P1-50a/50b/50c suffix 子序列.
- Reconciler: 预留 IDs O-P1-54+ for cross-batch / cross-session findings (e.g. R15 sibling continuity sweep / chapter-level §6.3 boundary 决议 / cross-session reviewer slot uniqueness audit).

按预分配 ID 写 `findings_added` 数组 + batch report. **不要** 用 round 1 sister-collision ID 模式 (O-P1-36..39 通用).

═══════════════════════════════════════════════════════════════════
## Round 2 Protocol Upgrade — G-MS-4 Halt Fallback Decision Tree
═══════════════════════════════════════════════════════════════════

Round 1 缺口 G-MS-4: sub-session halt 时 reconciler 决策树未 spec. Round 2 修:

任一 halt condition 触发, **session 必须**:

1. **不要** 删除 partial work — 留所有 batch file / progress / sample / verdicts (Rule B 强制)
2. 写 `.work/06_deep_verification/multi_session/halt_state_batch_19.md` 含 halt_reason / partial_state / incomplete_steps / recommended_fallback / evidence_paths
3. echo 单行 (替代 PARALLEL_SESSION_19_DONE):
   ```
   PARALLEL_SESSION_19_HALT reason=<text> partial_atoms=<N> partial_pages=<list> recommended_fallback=<a|b|c>
   ```
   - (a) reconciler retry 全 batch
   - (b) reconciler defer 本 batch + merge sister batches only
   - (c) reconciler abort experiment
4. 不要 等 reconciler — 直接 exit. Reconciler 读 halt_state 决策.

═══════════════════════════════════════════════════════════════════
## Halt Conditions (per protocol, round 2 augmented)
═══════════════════════════════════════════════════════════════════

任一触发则 halt + 写 halt_state per G-MS-4:
- writer failure rate >15% in batch
- Rule A raw <70%
- ctx 用量 >80%
- 预分配 reviewer `oh-my-claudecode:qa-tester` 不可派发 — Round 2: **不要** fallback 自选
- §6.3 chapter heading 状态依赖 sister batch 18 — 若 batch 18 confirms p.180 chapter-internal §6.2.8 instead of chapter-level §6.3 NEW, your sib assumption (§6.3.1 sib=1 / §6.3.2 sib=2 / §6.3.3 sib=3 under §6.3) 不成立 → halt + 报告 reconciler 决定 (类 round 2 G-MS-4 fallback)
- 任何尝试触动 root pdf_atoms.jsonl / audit_matrix.md / _progress.json 的 code path → halt 立即

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- 写 root pdf_atoms.jsonl / audit_matrix.md / _progress.json
- Self-pick reviewer slot (用 #28 oh-my-claudecode:qa-tester hardcoded)
- Touch sister batch (17/18) files
- Skip TOC anchor / R-rules / R14 / R12 transition (2 pages!) / NEW2 char-level self-validation / NEW3 outer-pipe rerun / NEW6 parent_section canonical / NEW7 deterministic L4 chain
- 私自决定 §6.3 chapter heading 是否存在 — **必须** depend on batch 18 sister determination + halt if uncertain
- Use round 1 ID reuse pattern — **必须** 用 round 2 G-MS-7 O-P1-50..53
- Run git commit / push

开干. 第一步 STEP 0 并行 6-file Read.
