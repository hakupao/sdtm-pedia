# Round 11 batch_114 attempt 1 — Failure post-mortem

> 创建: 2026-05-07
> 触发: pr-review-toolkit:code-reviewer HALT report — HIGH severity verbatim byte-exact regression
> 处理: re-dispatch with reinforced Hook A1 prompt (per round 06 batch_72 4-schema-regression precedent)

## 输入

- Source file: `knowledge_base/domains/SU/assumptions.md` (20 lines, 0 H2, multi-level nested-list 5 numbered + 9 sub-bullets)
- Writer subagent_type: `general-purpose`
- Prompt: P0_writer_md_v1.9.3.md + per-batch dispatch (round 11 batch_114 first dispatch attempt)

## 产物

15 atoms (a001..a015) at `evidence/failures/round_11_batch_114_attempt_1_writer_general_purpose_verbatim_leading_ws_strip_2026-05-07.jsonl`

## 技术判定 (Reviewer + 主 session 独立 grep verify)

- 9 / 15 atoms (60%) 违反 Hook A1 byte-exact verbatim — 删除了 indented sub-bullet 的 3-space leading whitespace
- 受影响 atom_id: a003 / a004 / a006 / a007 / a008 / a010 / a011 / a013 / a014 (全部 a./b./c. 级 sub-bullets)
- 主 session 独立 verify (`python3 ... json.loads`):
  - Source L4/L5/L8/L9/L10/L13/L14/L17/L18 全有 3-space leading whitespace
  - Writer 输出全部 leading whitespace stripped
- 对照基线: 195 prior production atoms 在 md_atoms.jsonl (round 01-10) 全 preserve indented sub-bullet 3-space leading whitespace (sample md_ch04_a228..a230 / md_dmAE_assn_a004/a005 etc.) — batch_114 是唯一 regression batch

## 业务判定

- HIGH severity per kickoff §4 halt #2 (Rule A audit < 90% PASS = 6/15 = 40%) + #3 (schema sweep — verbatim 不算 schema 但 byte-exact 是 v1.7+ Hook A1/22 硬约束)
- HALT 触发 — 不能进 batch_115
- Roll back md_atoms.jsonl 已恢复 9294 baseline (git restore)

## 下一 attempt 输入

- Re-dispatch writer (NEW general-purpose instance OR escalate to oh-my-claudecode:executor if available) with **reinforced Hook A1 verbatim mandate**:
  - 显式说明 "preserve ALL leading whitespace including 3-space indented sub-bullet prefix"
  - 显式 anti-pattern: "❌ verbatim 不能 trim/strip leading whitespace"
  - 显式 precedent reference: "md_ch04_a228..a230 / md_dmAE_assn_a004..a005 verbatim 全 starts with '   ' (3 spaces)"
  - 要求 writer 在 self-validate 前先 byte-cmp 抽样 verbatim vs source line bytes
- Reviewer attempt 1 PASS items (preserve, NOT re-run):
  - Schema 12-field structure ✓
  - atom_id sequential ✓
  - parent_section file-root consistency ✓
  - LIST_ITEM Hook A3 full-prefix (`a.`/`b.` 后 prefix preserved) ✓
  - §F-2 ratio 0.750 in band ✓
  - §F-3 estimate +57.9% INFO carry ✓
- Reviewer 提醒 batch_116 SUPPQUAL/ass + batch_118 SV/ass 同 risk (need verify their nested structure and apply reinforced prompt to all subsequent batches in round 11)

## v2.0 candidate stack (post round 11 close 时合并)

- **C-R11-01 NEW**: Hook A1 verbatim leading-whitespace strip regression mode — v2.0 codify Hook A1 显式 anti-pattern "indented sub-bullet 3-space leading whitespace strip" + 显式 precedent atoms (md_ch04_a228..a230) in writer prompt §C / §D / §E section. Severity: HIGH (per round 11 batch_114 1st in-flight regression in B-03c since round 06 batch_72 schema regression). Carry to v1.9.4 candidate stack — likely 1st cut driver if recurs in round 12.
