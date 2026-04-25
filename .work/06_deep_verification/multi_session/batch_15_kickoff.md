# Batch 15 Kickoff (Multi-Session Parallel — Session D)

> 你是 multi-session parallel 实验的 **session D (batch 15)**.
> 同时还有 session B (batch 13) + session C (batch 14) 在其他终端跑.
> 你只负责 p.141-150, 不动 root 文件 / audit_matrix / _progress.json.
>
> ⚠️ **batch 15 包含 mandatory drift cal** (per cadence "every 3 batches" + cumulative ≥300 双触发).

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 (并行 4 文件)
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (full)
2. `.work/06_deep_verification/audit_matrix.md` (READ-ONLY)
3. `.work/06_deep_verification/evidence/checkpoints/P1_batch_12_report.md` (上批 lessons + 看 drift cal pattern p.118 examples)
4. `.work/06_deep_verification/evidence/checkpoints/drift_cal_batch_10_12_p118_report.md` (drift cal precedent — 你将做类似分析)

读完报告: 当前 pages_done=120 / atoms_done=3200 / batches_done=12 / findings=35 / Rule D=21. 你将贡献 batch 15 + drift cal.

═══════════════════════════════════════════════════════════════════
## STEP 1 — TOC Ground Truth (从 PDF p.4 提取, 直接用)
═══════════════════════════════════════════════════════════════════

| § | Title | Pages | Heading Level | Sibling Index |
|---|---|---|---|---|
| §6.2.1 | Adverse Events (AE) | p.133-142 (p.141-142 batch 15 SCOPE 起头) | L3 sib=1 under §6.2 | (heading 在 p.133 batch 14, batch 15 仅 AE tail content) |
| **§6.2.2** | **Biospecimen Events (BE)** | **p.143-147 (batch 15 SCOPE 中)** | **L3 sib=2 under §6.2** | **batch 15 SCOPE NEW** |
| **§6.2.3** | **Clinical Events (CE)** | **p.148-154 (p.148-150 batch 15 SCOPE 末)** | **L3 sib=3 under §6.2** | **batch 15 SCOPE 末** |
| §6.2.4 | Disposition (DS) | p.155 | L3 sib=4 under §6.2 | (batch 16 处理) |

### parent_section 规则 (R5 anchor):
- p.141-142 atoms → `§6.2.1 [Adverse Events (AE)]` (AE tail content)
- p.143 atoms (transition page possibility):
  - AE last bit if any → `§6.2.1 [Adverse Events (AE)]`
  - §6.2.2 heading 自己 → `§6.2 [MODELS FOR EVENTS DOMAINS]`
  - BE Description/Overview/Spec content → `§6.2.2 [Biospecimen Events (BE)]`
- p.144-147 atoms → `§6.2.2 [Biospecimen Events (BE)]`
- p.148 atoms (transition):
  - BE last bit if any → `§6.2.2 [Biospecimen Events (BE)]`
  - §6.2.3 heading 自己 → `§6.2 [MODELS FOR EVENTS DOMAINS]`
  - CE Description/Overview content → `§6.2.3 [Clinical Events (CE)]`
- p.149-150 atoms → `§6.2.3 [Clinical Events (CE)]`

### Sub-headings convention (depth +1):
- §6.2.1 sub: L4 sib=1/2/3/4 (AE – Description/Overview / Specification / Assumptions / Examples) — heading 在 batch 14, batch 15 仅 AE tail
- §6.2.2 sub: L4 sib=1/2/3/4 (BE – Description/Overview / Specification / Assumptions / Examples 若有)
- §6.2.3 sub: L4 sib=1/2/3/4 (CE – Description/Overview / Specification / Assumptions)

### Cross-Batch Sibling Continuity Pre-Context (R15 NEW)

⚠️ Prepend: "Prior batches sibling continuity:
- §6.2 [MODELS FOR EVENTS DOMAINS] = L2 sib=2 under §6 (set in batch 14 p.133)
- §6.2.1 [Adverse Events (AE)] = L3 sib=1 under §6.2 (set in batch 14 p.133)
- §6.2.2 [BE] = L3 sib=2 under §6.2 (NEW in batch 15)
- §6.2.3 [CE] = L3 sib=3 under §6.2 (NEW)
- AE/BE/CE Examples N sibling sequences (if any) RESTART per domain — Examples in BE/CE are unrelated to AE Examples."

═══════════════════════════════════════════════════════════════════
## STEP 2 — Dispatch Strategy (Option C parallel, alternation)
═══════════════════════════════════════════════════════════════════

Per alternation (batch 14 = executor+writer, batch 15 切换):

- **15a = `oh-my-claudecode:writer` × p.141-145**
- **15b = `oh-my-claudecode:executor` × p.146-150**

并行派. R12 transition critical for p.143 (§6.2.1 → §6.2.2) + p.148 (§6.2.2 → §6.2.3).

═══════════════════════════════════════════════════════════════════
## STEP 3 — Schema Validation
═══════════════════════════════════════════════════════════════════

同 batch 13. 额外注意 2 个 transition page (p.143 + p.148) R12 验证.

═══════════════════════════════════════════════════════════════════
## STEP 4 — Drift Cal: **MANDATORY** (cumulative ≥300 自 p.118 + every-3-batches)
═══════════════════════════════════════════════════════════════════

⚠️ 你 MUST 触发 drift cal. 流程 (类 batch 12 p.118 precedent):

### Step 4.1: 选 target page
候选 (按 dense TABLE_ROW value-add 排序):
- **p.143** (BE start, 可能 spec table 高密) — 推荐 1st choice
- **p.148** (CE start, 可能 spec table 高密) — 2nd choice
- **p.150** (CE Examples 若有) — 3rd choice
- **任一** spec table dense 页 (15a 或 15b atomized 后看哪页 atom count >= 30)

主 session 在 schema validation 后选定 1 页 (理想 1 页 atom count ~30-50, dense TABLE_ROW + spec table).

### Step 4.2: 派 executor 单页 rerun
对应 baseline 的另一 agent type (若 baseline page 在 15a writer → 派 executor; 若在 15b executor → 派 writer).

输出 `drift_cal_p<XXX>_<rerun-type>_rerun.jsonl`.

### Step 4.3: 比对
- Strict count match
- atom_type distribution
- Verbatim hash
- Threshold ≥80%

### Step 4.4: 根因分析 + 决策
若 FAIL <80%:
- (a) Reproducibility noise (类 O-P1-09 batch 03 QS sparse-cell) → tiebreaker `general-purpose` 第 3 派 + 2/3 majority
- (b) Writer family bug (类 O-P1-12 / O-P1-23 / O-P1-34 数据腐败) → root-cause 定位 + Option H 4-atom 类 inline 修
- (c) Convention drift (类 O-P1-33 CRF cell-splitting) → defer v1.3 INFO finding
- (d) Page-shift / duplication (类 O-P1-35 batch 12 p.119) → Option E full-page rerun wholesale replace

### Step 4.5: 写报告 `drift_cal_batch_13_15_p<XXX>_report.md`
(注: prefix `13_15` 表示 last cal batch (12) + current batch range — wait, last cal was batch 12, current is batch 15, so prefix should be `12_15` 或就用 single batch number 简洁: `drift_cal_batch_15_p<XXX>_report.md`)

文件名简化推荐: `drift_cal_batch_15_p<XXX>_report.md`.

═══════════════════════════════════════════════════════════════════
## STEP 5 — Rule A Audit (slot #24 = vercel:deployment-expert AUDIT-mode)
═══════════════════════════════════════════════════════════════════

预分配 reviewer (Rule D unique, 不可改): `vercel:deployment-expert`

派发 prompt 显式 "Mode: AUDIT, NOT deployment or DevOps. You are an INDEPENDENT REVIEWER for PDF atomization quality. Do NOT touch deployment, do NOT analyze CI/CD, do NOT propose infra changes." (AUDIT-mode pivot 5th, vercel-family 第 2 个 AUDIT pivot post #22).

### Sample build:
- Seed = 20260480
- 10 atoms 1/page stratified (p.141-150)
- Atom_type 优先: TABLE_ROW × 5 (R8/R11 验) + HEADING × 3 (R12 transition validation §6.2.2 / §6.2.3 起头 sib=2/3) + CODE_LITERAL × 1 (若有 ae.xpt/be.xpt/ce.xpt) + 1 其他
- 输出 `rule_a_batch_15_sample.jsonl`

### Reviewer prompt 含 4-dim verdict + TOC ground truth (§6.2.1/§6.2.2/§6.2.3 anchors) + 15 R-rules + R12 transition discipline 强调 (2 transition pages p.143 + p.148).

═══════════════════════════════════════════════════════════════════
## STEP 6 — Repair (if any)
═══════════════════════════════════════════════════════════════════

同 batch 13. 注意 batch 15 含 drift cal + 2 transition pages, repair cycles 可能比 batch 13/14 多.

═══════════════════════════════════════════════════════════════════
## STEP 7 — Sub-progress + Batch Report
═══════════════════════════════════════════════════════════════════

写 `_progress_batch_15.json` (schema 同 batch 13, batch_id=15, session_id="D", reviewer_slot=24, reviewer_type="vercel:deployment-expert", drift_cal_triggered=true, drift_cal_page=<XXX>, drift_cal_match_rate=<float>, drift_cal_root_cause="<text>", drift_cal_action="Option H/E/tiebreaker/INFO defer").

写 `P1_batch_15_report.md` (含 drift cal 段落, 类 batch 12 报告结构).

═══════════════════════════════════════════════════════════════════
## STEP 8 — Final Message
═══════════════════════════════════════════════════════════════════

```
PARALLEL_SESSION_15_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered_p<XXX>_match=<float>%_action=<text> findings_added=<list>
```

═══════════════════════════════════════════════════════════════════
## NEVER DO (同 batch 13)
═══════════════════════════════════════════════════════════════════

- 写 root pdf_atoms.jsonl / audit_matrix.md / _progress.json
- Self-pick reviewer slot (用 #24 vercel:deployment-expert hardcoded)
- Touch sister batch (13/14) files
- Skip TOC anchor / R-rules / R14 / R12 transition / drift cal mandatory
- Run git commit / push

开干. 第一步 STEP 0 并行 4-file Read.
