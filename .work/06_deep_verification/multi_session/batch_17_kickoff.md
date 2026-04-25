# Batch 17 Kickoff (Multi-Session Parallel — Session C, Round 2)

> 你是 multi-session parallel 实验 round 2 的 **session C (batch 17)**.
> 同时还有 session B (batch 16) + session D (batch 18) 在其他终端跑.
> 你只负责 p.161-170, 不动 root 文件 / audit_matrix / _progress.json.
> Round 2 实验 — 吸收 round 1 (batches 13-15) MULTI_SESSION_RETRO.md G-MS-4 (halt fallback) + G-MS-7 (finding ID range pre-allocation) 两条缺口修.

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 (并行 5 文件)
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (round 1 master 协议, 你 round 2 沿用)
2. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO.md` (round 1 retro 三段式, 重点 §2 G-MS-4 + G-MS-7 你必须修的两条缺口)
3. `.work/06_deep_verification/audit_matrix.md` (READ-ONLY)
4. `.work/06_deep_verification/evidence/checkpoints/P1_batch_15_report.md` (上批 lessons + drift cal value-add 5th 案例)
5. `.work/06_deep_verification/subagent_prompts/v1.3_patch_candidates.md` (cumulative R-rules + NEW1-NEW5)

读完报告: 当前 pages_done=150 / atoms_done=3877 / batches_done=15 / findings=39 / Rule D=24. 你将贡献 batch 17.

═══════════════════════════════════════════════════════════════════
## STEP 1 — TOC Ground Truth (PDF p.4 + page_index.json verified, 直接用)
═══════════════════════════════════════════════════════════════════

⚠️ Batch 17 含 **1 chapter-internal transition** (§6.2.4 DS → §6.2.5 HO at p.167). DS 是 P1 至今最大单 domain (12 页 p.155-167), 你处理其中 7 页 + HO 起头 4 页中 3 页. R12 transition discipline 高压.

| § | Title | Pages (page_index.json) | Heading Level | Sibling Index |
|---|---|---|---|---|
| §6.2.4 | Disposition (DS) | p.155-167 (p.161-167 batch 17 SCOPE 中末, p.155-160 batch 16 已处理) | L3 sib=4 under §6.2 | (heading 在 p.155 batch 16, batch 17 仅 DS middle/tail content) |
| **§6.2.5** | **Healthcare Encounters (HO)** | **p.167-171 (p.167-170 batch 17 SCOPE 末)** | **L3 sib=5 under §6.2** | **batch 17 SCOPE NEW** |
| §6.2.6 | Medical History (MH) | p.171-178 | L3 sib=6 under §6.2 | (batch 18 处理) |

### parent_section 规则 (R5 anchor):
- p.161-166 atoms → `§6.2.4 [Disposition (DS)]` (DS middle content + DS Examples N if any)
- p.167 atoms (transition page possibility, **R12 critical**):
  - DS last bit if any → `§6.2.4 [Disposition (DS)]`
  - §6.2.5 heading 自己 → `§6.2 [MODELS FOR EVENTS DOMAINS]`
  - HO Description/Overview/Spec content → `§6.2.5 [Healthcare Encounters (HO)]`
- p.168-170 atoms → `§6.2.5 [Healthcare Encounters (HO)]` (除 sub-headings 自己)

### Sub-headings convention (depth +1):
- §6.2.4 sub: L4 sib=1/2/3/4(/5) (DS – Description/Overview / Specification / Assumptions / Examples / References 若有) — heading 在 batch 16, batch 17 仅 DS middle/tail content
- §6.2.5 sub: L4 sib=1/2/3/4 (HO – Description/Overview / Specification / Assumptions / Examples 若有)

### Cross-Batch Sibling Continuity Pre-Context (R15 NEW)

⚠️ Prepend 到两个 writer prompt: "Prior batches HEADING continuity (post round-1 reconciler merge + batch 16 round 2):
- §6.2 [MODELS FOR EVENTS DOMAINS] = L2 sib=2 under §6 (set in batch 14)
- §6.2.1 [AE] L3 sib=1 / §6.2.2 [BE] L3 sib=2 / §6.2.3 [CE] L3 sib=3 / §6.2.4 [DS] L3 sib=4 (batch 16 setting sib=4, your batch 17 处理 DS middle/tail content not heading)
- §6.2.5 [HO] = L3 sib=5 under §6.2 (NEW in batch 17, sib continuity from §6.2.4 sib=4)
- DS Examples N sibling continues batch 16's chain if any continuation; otherwise RESTART per HO domain at sib=1 within §6.2.5 — Examples in HO unrelated to DS Examples sequence."

═══════════════════════════════════════════════════════════════════
## STEP 2 — Dispatch Strategy (Option C parallel, alternation)
═══════════════════════════════════════════════════════════════════

Per O-P1-13 default + alternation pattern (batch 16 = writer+executor, batch 17 切换):

- **17a = `oh-my-claudecode:executor` × p.161-165**
- **17b = `oh-my-claudecode:writer` × p.166-170** (writer 家族 R12 transition 验, p.167 DS→HO)

并行派. 完整 self-contained prompt 同 batch 16 协议, 但 TOC anchor 段换为 batch 17.

### R12 Transition Discipline (HIGH PRESSURE for p.167)

⚠️ p.167 含 **2-3 个区** (R12 critical):
1. §6.2.4 DS tail content (若有, 跨 p.166/p.167 boundary — DS Examples N 收尾或 References 收尾)
2. §6.2.5 [Healthcare Encounters (HO)] sub-section HEADING (L3 sib=5) + HO Description/Overview/Specification 起头

writer 必须 atomize 全部 physical content top-to-bottom 不漏 DS tail (类 batch 14 p.133 + batch 15 p.143/p.148 + batch 16 p.155 chapter-internal transition CLEAN precedent — NEW5 R12 strengthening 已 v1.3 candidate). 17b writer-family 重点 R10 verbatim accuracy + NEW2 spec-table char-level self-validation (writer 14b 5 typos cluster + writer 15b STUDIID×8 + supple→suppbe + bs.xpt swap + relspec REFID + relrec corruption lessons absorbed).

═══════════════════════════════════════════════════════════════════
## STEP 3 — Schema Validation (post-DONE, before Rule A)
═══════════════════════════════════════════════════════════════════

同 batch 16. 额外检 R12 transition page p.167:
- atom count >= 8 (transition page, dense)
- 含 §6.2.5 heading L3 sib=5
- parent_section 区分清楚 DS tail vs §6.2.5 heading vs HO sub-content

═══════════════════════════════════════════════════════════════════
## STEP 4 — Drift Cal: NOT triggered batch 17
═══════════════════════════════════════════════════════════════════

跳过 (next mandatory batch 18 session D). Ad-hoc 触发条件同 batch 16. **17b writer-family 高警戒** (writer-family 5/5 batches drift cal value-add 命中 typo/under-extraction cluster — O-P1-12 batch 03 / O-P1-23 batch 09 / O-P1-34 batch 12 / batch 13 O-P1-37 / batch 14 O-P1-36 / batch 15 O-P1-36+37+38), 主 session 务必 PDF cross-check 17b dense pages.

═══════════════════════════════════════════════════════════════════
## STEP 5 — Rule A Audit (slot #26 = superpowers:code-reviewer AUDIT-mode)
═══════════════════════════════════════════════════════════════════

预分配 reviewer (Rule D unique, **HARDCODED 不可改, round 2 partition**): `superpowers:code-reviewer`

派发 prompt 显式 "Mode: AUDIT for SDTMIG v3.4 PDF atomization quality, NOT source code review. You are an INDEPENDENT REVIEWER for PDF atomization quality. Do NOT review source code, do NOT touch implementation files. The 'code' you review is JSONL atom records — verify each atom's atom_type / verbatim / parent_section / heading_level+sibling_index against the PDF ground truth + 15 cumulative R-rules. Output verdicts JSONL + summary md to designated paths." (类 prior AUDIT pivot pattern; **7th AUDIT-mode pivot, superpowers family FIRST burn**; superpowers:code-reviewer 自然是 reviewer 角色, AUDIT pivot 仅限定 review 对象 from source code → PDF atom quality).

### Sample build (Bash + Python):
- Seed = 20260490
- 10 atoms 1/page stratified (p.161-170)
- Atom_type 优先: TABLE_ROW × 5-6 (R11 trailing empty + R8 empty cell + DS/HO spec table 验证) + HEADING × 2-3 (R12 transition validation §6.2.5 sib=5 起头 + DS sub-heading consistency) + 其他 1-2
- 输出 `rule_a_batch_17_sample.jsonl`

### Reviewer prompt (类 batch 13-16 prior reviewer prompts) 含:
- 4-dimension verdict (atom_type / verbatim / parent_section / heading_level+sibling_index)
- TOC ground truth prepend (§6.2.4 / §6.2.5 anchors)
- 15 R-rules embedded (R1-R15 cumulative)
- Output: `rule_a_batch_17_verdicts.jsonl` + `rule_a_batch_17_summary.md`
- Final message: `RULE_A_DONE pass=N partial=N fail=N weighted=X.XX`
- Threshold ≥90% weighted → PASS; ≥80% <90% → CONDITIONAL_PASS; <80% → FAIL halt + report 等 reconciler 决定 (per round 2 G-MS-4 halt fallback)

═══════════════════════════════════════════════════════════════════
## STEP 6 — Repair (if any finding)
═══════════════════════════════════════════════════════════════════

同 batch 16. 注意 chapter-internal transition p.167 易出 R12 violation (类 batch 11 §6.1.2→§6.1.3 + batch 12 §6.1.3.3→§6.1.4 hint + batch 13 §6.1.5→§6.1.6 + batch 14 §6.1.6→§6.2/§6.2.1 + batch 15 §6.2.1→§6.2.2 + batch 16 §6.2.3→§6.2.4 边界), 主 session 务必 PDF cross-check p.166/p.167 两页确认 DS tail 完整 + HO Description 起头不漏.

⚠️ Round 2 G-MS-5 Option E rerun outer-pipe + null-key requirement (NEW3) — 防止 batch 14 91-atom bulk Option H 修工作复发.

═══════════════════════════════════════════════════════════════════
## STEP 7 — Sub-progress + Batch Report
═══════════════════════════════════════════════════════════════════

写 `.work/06_deep_verification/evidence/checkpoints/_progress_batch_17.json` (schema 同 batch 16, batch_id=17, session_id="C", round=2, reviewer_slot=26, reviewer_type="superpowers:code-reviewer", reviewer_audit_pivot_index=7, reviewer_family_first_burn=true, reviewer_family_name="superpowers", finding_id_range_allocated="O-P1-44..47").

写 `.work/06_deep_verification/evidence/checkpoints/P1_batch_17_report.md` (类 batch 13-16 report 结构).

═══════════════════════════════════════════════════════════════════
## STEP 8 — Final Message
═══════════════════════════════════════════════════════════════════

```
PARALLEL_SESSION_17_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list of O-P1-44..47>
```

═══════════════════════════════════════════════════════════════════
## Round 2 Protocol Upgrade — G-MS-7 Finding ID Range Pre-allocation
═══════════════════════════════════════════════════════════════════

Round 1 缺口 G-MS-7: 各 session 用相同 O-P1-NN 累加 ID 易冲突. Round 2 修:

- Batch 16 (sister): 预留 IDs O-P1-40..43.
- **Batch 17 (你)**: 预留 IDs **O-P1-44..47** (4 IDs reserved). 若你新 finding > 4, 用 IDs O-P1-44a/44b/44c suffix 子序列.
- Batch 18 (sister): 预留 IDs O-P1-48..51.
- Reconciler: 预留 IDs O-P1-52+ for cross-batch / cross-session findings.

按预分配 ID 写 `findings_added` 数组 + batch report. **不要** 用 round 1 sister-collision ID 模式 (O-P1-36..39 通用).

═══════════════════════════════════════════════════════════════════
## Round 2 Protocol Upgrade — G-MS-4 Halt Fallback Decision Tree
═══════════════════════════════════════════════════════════════════

Round 1 缺口 G-MS-4: sub-session halt 时 reconciler 决策树未 spec. Round 2 修:

任一 halt condition 触发, **session 必须**:

1. **不要** 删除 partial work — 留所有 batch file / progress / sample / verdicts (Rule B 强制)
2. 写 `.work/06_deep_verification/multi_session/halt_state_batch_17.md` 含 halt_reason / partial_state / incomplete_steps / recommended_fallback / evidence_paths
3. echo 单行 (替代 PARALLEL_SESSION_17_DONE):
   ```
   PARALLEL_SESSION_17_HALT reason=<text> partial_atoms=<N> partial_pages=<list> recommended_fallback=<a|b|c>
   ```
4. 不要 等 reconciler — 直接 exit. Reconciler 读 halt_state 决策.

═══════════════════════════════════════════════════════════════════
## Halt Conditions (per protocol, round 2 augmented)
═══════════════════════════════════════════════════════════════════

任一触发则 halt + 写 halt_state per G-MS-4:
- writer failure rate >15% in batch
- Rule A raw <70%
- ctx 用量 >80%
- 预分配 reviewer `superpowers:code-reviewer` 不可派发 — Round 2: **不要** fallback 自选
- 任何尝试触动 root pdf_atoms.jsonl / audit_matrix.md / _progress.json 的 code path → halt 立即

═══════════════════════════════════════════════════════════════════
## NEVER DO (同 batch 16)
═══════════════════════════════════════════════════════════════════

- 写 root pdf_atoms.jsonl / audit_matrix.md / _progress.json
- Self-pick reviewer slot (用 #26 superpowers:code-reviewer hardcoded)
- Touch sister batch (16/18) files
- Skip TOC anchor / R-rules / R14 / R12 transition / NEW2 char-level self-validation / NEW3 outer-pipe rerun
- Use round 1 ID reuse pattern — **必须** 用 round 2 G-MS-7 O-P1-44..47
- Run git commit / push

开干. 第一步 STEP 0 并行 5-file Read.
