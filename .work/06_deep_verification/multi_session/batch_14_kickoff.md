# Batch 14 Kickoff (Multi-Session Parallel — Session C)

> 你是 multi-session parallel 实验的 **session C (batch 14)**.
> 同时还有 session B (batch 13) + session D (batch 15) 在其他终端跑.
> 你只负责 p.131-140, 不动 root 文件 / audit_matrix / _progress.json.

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 (并行 4 文件)
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (full)
2. `.work/06_deep_verification/audit_matrix.md` (READ-ONLY)
3. `.work/06_deep_verification/evidence/checkpoints/P1_batch_12_report.md` (上批 lessons)
4. `.work/06_deep_verification/subagent_prompts/v1.3_patch_candidates.md`

读完报告: 当前 pages_done=120 / atoms_done=3200 / batches_done=12 / findings=35 / Rule D=21. 你将贡献 batch 14.

═══════════════════════════════════════════════════════════════════
## STEP 1 — TOC Ground Truth (从 PDF p.4 提取, 直接用)
═══════════════════════════════════════════════════════════════════

⚠️ Batch 14 是 **chapter-level transition batch** (§6.1 → §6.2). R12 transition discipline 高压.

| § | Title | Pages | Heading Level | Sibling Index |
|---|---|---|---|---|
| §6.1.6 | Substance Use (SU) | p.129-132 (p.129-130 batch 13 已处理, **p.131-132 batch 14 SCOPE 起头**) | L3 sib=6 under §6.1 | (heading 在 p.129 batch 13, batch 14 仅 SU tail content) |
| **§6.2** | **MODELS FOR EVENTS DOMAINS** | **p.133 (chapter heading)** | **L2 sib=2 under §6** (新 chapter) | **batch 14 SCOPE NEW** |
| **§6.2.1** | **Adverse Events (AE)** | **p.133-142 (p.133-140 batch 14 SCOPE)** | **L3 sib=1 under §6.2** | **batch 14 SCOPE 中-末** |
| §6.2.2 | Biospecimen Events (BE) | p.143 | L3 sib=2 under §6.2 | (batch 15 处理) |

### parent_section 规则 (R5 anchor):
- p.131-132 atoms → `§6.1.6 [Substance Use (SU)]` (SU tail content)
- p.133 atoms (3 区: SU last bit if any + §6.2 chapter heading + §6.2.1 AE start):
  - SU tail if any → `§6.1.6 [Substance Use (SU)]`
  - §6.2 heading 自己 → `§6 [Domain Models Based on the General Observation Classes]`
  - §6.2.1 heading 自己 → `§6.2 [MODELS FOR EVENTS DOMAINS]`
  - AE Description/Overview/Spec/Assumptions content → `§6.2.1 [Adverse Events (AE)]`
- p.134-140 atoms → `§6.2.1 [Adverse Events (AE)]` (除 sub-headings 自己)

### Sub-headings convention (depth +1):
- §6.1.6 sub: L4 sib=1/2/3/4 (SU – Description/Overview / Specification / Assumptions / Examples) — heading 在 batch 13, batch 14 仅 sub content
- §6.2.1 sub: L4 sib=1/2/3/4 (AE – Description/Overview / Specification / Assumptions / Examples)

### Cross-Batch Sibling Continuity Pre-Context (R15 NEW)

⚠️ Prepend 到两个 writer prompt: "Prior batches HEADING continuity:
- §6.1 [Models for Interventions Domains] = L2 sib=1 under §6 (handled in earlier batches)
- §6.1.1 [AG] L3 sib=1 / §6.1.2 [CM] L3 sib=2 / §6.1.3 [Exposure Domains] L3 sib=3 / §6.1.4 [ML] L3 sib=4 / §6.1.5 [PR] L3 sib=5 / §6.1.6 [SU] L3 sib=6 (batch 13 setting sib=4/5/6, your batch 14 处理 SU tail content not heading)
- §6.2 [MODELS FOR EVENTS DOMAINS] = L2 sib=2 under §6 (NEW in batch 14, sib continuity from §6.1 sib=1)
- §6.2.1 [Adverse Events (AE)] = L3 sib=1 under §6.2 (NEW)
- (Examples N sibling continuity inside §6.2.1 if AE Examples present 起头 sib=1 — independent of §6.1.3.3 Examples sequence which ended sib=8)"

═══════════════════════════════════════════════════════════════════
## STEP 2 — Dispatch Strategy (Option C parallel, alternation)
═══════════════════════════════════════════════════════════════════

Per alternation (batch 13 = writer+executor, batch 14 切换):

- **14a = `oh-my-claudecode:executor` × p.131-135**
- **14b = `oh-my-claudecode:writer` × p.136-140**

并行派 (单 message 双 Agent tool call). 完整 self-contained prompt 同 batch 13 协议, 但 TOC anchor 段换为 batch 14.

### R12 Transition Discipline (HIGH PRESSURE for p.133)

⚠️ p.133 含 **3 个区** (R12 critical):
1. §6.1.6 SU tail content (若有, 跨 p.132/p.133 boundary)
2. §6.2 [MODELS FOR EVENTS DOMAINS] chapter HEADING (L2 sib=2)
3. §6.2.1 [Adverse Events (AE)] sub-section HEADING (L3 sib=1) + AE Description/Overview/Specification 起头

writer 必须 atomize 全部 physical content top-to-bottom 不漏 SU tail (类 batch 11 p.103 §6.1.2→§6.1.3 transition under-extraction O-P1-28 教训, 不复发).

═══════════════════════════════════════════════════════════════════
## STEP 3 — Schema Validation (post-DONE, before Rule A)
═══════════════════════════════════════════════════════════════════

同 batch 13. 额外检 R12 transition page p.133:
- atom count >= 10 (transition page, dense)
- 含 §6.2 heading L2 sib=2 + §6.2.1 heading L3 sib=1
- parent_section 区分清楚 SU tail vs §6.2 chapter vs §6.2.1 AE

═══════════════════════════════════════════════════════════════════
## STEP 4 — Drift Cal: NOT triggered batch 14
═══════════════════════════════════════════════════════════════════

跳过 (next mandatory batch 15 session D). Ad-hoc 触发条件同 batch 13 (e.g. 若 AE Examples spec table 高密 + page-shift 怀疑).

═══════════════════════════════════════════════════════════════════
## STEP 5 — Rule A Audit (slot #23 = oh-my-claudecode:designer AUDIT-mode)
═══════════════════════════════════════════════════════════════════

预分配 reviewer (Rule D unique, 不可改): `oh-my-claudecode:designer`

派发 prompt 显式 "Mode: AUDIT, NOT design or UI work. You are an INDEPENDENT REVIEWER for PDF atomization quality. Do NOT design, do NOT touch code, do NOT propose UI changes." (AUDIT-mode pivot 4th, omc-family 第 2 个 AUDIT pivot post #21 debugger).

### Sample build:
- Seed = 20260475
- 10 atoms 1/page stratified (p.131-140)
- Atom_type 优先: TABLE_ROW × 5-6 + HEADING × 2-3 (R12 transition validation §6.2 chapter L2 + §6.2.1 L3 sib=1) + 其他 1-2
- 输出 `rule_a_batch_14_sample.jsonl`

### Reviewer prompt (同 batch 13 #22 结构) 含 4-dimension verdict + TOC ground truth (§6.1.6 / §6.2 / §6.2.1 anchors) + 15 R-rules + R12 transition discipline 强调.

═══════════════════════════════════════════════════════════════════
## STEP 6 — Repair (if any finding)
═══════════════════════════════════════════════════════════════════

同 batch 13. 注意 chapter-level transition p.133 易出 R12 violation (类 batch 11 §6.1.2→§6.1.3 + batch 12 §6.1.3.3→§6.1.4 边界), 主 session 务必 PDF cross-check p.131/p.132/p.133 三页确认 SU tail 完整.

═══════════════════════════════════════════════════════════════════
## STEP 7 — Sub-progress + Batch Report
═══════════════════════════════════════════════════════════════════

写 `.work/06_deep_verification/evidence/checkpoints/_progress_batch_14.json` (schema 同 batch 13, batch_id=14, session_id="C", reviewer_slot=23, reviewer_type="oh-my-claudecode:designer").

写 `.work/06_deep_verification/evidence/checkpoints/P1_batch_14_report.md`.

═══════════════════════════════════════════════════════════════════
## STEP 8 — Final Message
═══════════════════════════════════════════════════════════════════

```
PARALLEL_SESSION_14_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list>
```

═══════════════════════════════════════════════════════════════════
## NEVER DO (同 batch 13)
═══════════════════════════════════════════════════════════════════

- 写 root pdf_atoms.jsonl / audit_matrix.md / _progress.json
- Self-pick reviewer slot (用 #23 oh-my-claudecode:designer hardcoded)
- Touch sister batch (13/15) files
- Skip TOC anchor / R-rules / R14
- Skip R12 transition discipline check on p.133
- Run git commit / push

开干. 第一步 STEP 0 并行 4-file Read.
