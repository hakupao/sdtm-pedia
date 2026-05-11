# P0 Matcher — PDF↔MD 原子双向匹配 prompt v1.5

> Version: v1.5 (2026-04-28, post P1 round 8 cut)
> 基于 v1.4 (round 7 cut, 8+5 verdict carry-forward + 4 NEW v1.4 discrepancy markers) + round 8 cumulative
> 角色: Matcher (双向 PDF↔MD 匹配 + discrepancy 分类), 独立 subagent, 与 Writer/Reviewer 不同 subagent_type
> v1.5 变更 over v1.4: **1 NEW discrepancy marker `[NEW7_xpt_parent_caption_violation]` + STRONGLY VALIDATED status promotion (N14 + G-MS-4) — codification only.** Schema link + verdict 8+5 enum + bidirectional match contract 全 carry-forward unchanged.

## 角色硬约束 (v1.4 carry-forward unchanged)

参 `archive/v1.4_final_2026-04-28/P0_matcher_v1.4.md` §角色硬约束 全文.

## 派发 subagent_type (v1.4 carry-forward unchanged)

参 v1.4 §派发. v1.5 reaffirmed: matcher 与 writer/reviewer 不同 subagent_type per Rule D writer/reviewer/matcher isolation.

═══════════════════════════════════════════════════════════════════
## CODIFIED VERDICT ENUM + DISCREPANCY MARKERS (v1.4 carry-forward FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.4_final_2026-04-28/P0_matcher_v1.4.md` for:
- v1.2 base 8+5 verdict enum (forward 9 / reverse 5)
- v1.3 NEW discrepancy markers
- v1.4 NEW discrepancy markers (4 markers covering round 5+6+7 candidates):
  - `[NEW8.d_value_hallucination]` — TABLE_ROW value-cell hallucination (writer-direction VALUE HALLUCINATION 3rd cumulative recurrence main-line)
  - `[NEW9_L2_short_bracket_parent_skip]` — L2 short-bracket parent on non-L3-HEADING (28-atom motif round 7 O-P1-113)
  - `[NEW7_L6_canonical_form_violation]` — L6 textual heading canonical form violation
  - `[NEW2_extended_homoglyph]` — Cyrillic К М Н В У expansion 11+ chars

═══════════════════════════════════════════════════════════════════
## v1.5 NEW DISCREPANCY MARKER (1 NEW per V2)
═══════════════════════════════════════════════════════════════════

### `[NEW7_xpt_parent_caption_violation]` — sync with PDF/MD writer N15 retroactive sweep

**Trigger**: PDF atom OR MD atom with `parent_section` matching pattern `^[a-z]+\.xpt$` (.xpt filename used as parent_section instead of canonical SECTION DESCRIPTOR).

**Severity**: MEDIUM — discipline regression motif, not strict atom_type/verbatim violation.

**Detection regex**: `re.match(r"^[a-z]+\.xpt$", parent_section)`.

**Source**: round 8 batch 36 O-P1-122 reviewer slot #46 Plan AMBIGUOUS-lean-OVERRIDE = 27 atoms (8 tu.xpt + 8 tr.xpt + 6 relrec.xpt + 5 vs.xpt) + reconciler-side retroactive sweep 8 historical p.133 batch 13 NEW9 violations cumulative scope 35 atoms cumulative round 1+8 P1.

**Resolution**: writer-side N15 codification + reconciler-side retroactive Option H bulk fix at v1.5 cut session (this session).

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (per V5, sync with all 4 prompts)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: graduate from "1st-live-fire-EFFECTIVE" → **"STRONGLY VALIDATED post 2nd live-fire"** — production-ready protocol; matcher-side discrepancy detection assumes alternation methodology baseline writer ↔ rerun executor (or vice versa) cleanly disentangles writer-direction signal from intra-family non-determinism
- **G-MS-4 halt fallback**: graduate from "1st-live-fire-EFFECTIVE" → **"STRONGLY VALIDATED post 2nd live-fire"** — production-ready protocol

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.2 | 2026-04-24 | P0 Pilot 收官 frozen 8+5 verdict enum |
| v1.3 | 2026-04-27 | post P1 round 4 cut: 4 NEW discrepancy markers covering round 1-4 candidates |
| v1.4 | 2026-04-28 | post P1 round 7 cut: 4 NEW discrepancy markers covering round 5+6+7 candidates |
| **v1.5** | **2026-04-28** | **post P1 round 8 cut**: 1 NEW discrepancy marker `[NEW7_xpt_parent_caption_violation]` covering round 8 V2 candidate (.xpt-as-parent_section discipline regression 35-atom cumulative retroactive sweep batch 36 + p.133 batch 13); STATUS PROMOTIONS N14 + G-MS-4 STRONGLY VALIDATED post 2nd live-fire; v1.4 archived. NOT behavior change — verdict enum / bidirectional match contract / Rule D isolation 全 carry-forward unchanged. |
