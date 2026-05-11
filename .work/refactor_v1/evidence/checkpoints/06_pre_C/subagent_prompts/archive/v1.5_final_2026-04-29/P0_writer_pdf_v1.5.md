# P0 Writer PDF — 原子化 prompt v1.5

> Version: v1.5 (2026-04-28, post P1 round 8 cut — formal codification of round 8 8 cumulative v1.5 candidates V1-V8)
> 基于 v1.4 (2026-04-28 round 7 cut + 14 NEW patches N1-N14 covering 24 round 5+6+7 candidates) + round 8 (batches 35/36/37) cumulative candidates
> 角色: Writer (原子化), 独立 subagent, 与 Reviewer/Matcher 不同 subagent_type
> v1.5 变更 over v1.4: **codification + content-type-aware dispatch + STRONGLY VALIDATED status promotion.** Schema link + output JSONL format + atom_type 9-enum + heading_level/sibling_index 语义 + DONE single-line contract + Rule B backup discipline + 13 §A-M v1.3 base + 14 §N1-N14 v1.4 NEW patches 全 carry-forward unchanged. v1.5 把 round 8 8 候选固化进 prompt; 3 NEW writer-side patches N15-N17 加在 §A-V codified base 之上 + Self-Validate 扩 14 → 17 hooks + STRONGLY VALIDATED status promotion + Changelog. POST 4th cumulative writer-direction main-line VALUE HALLUCINATION recurrence (round 5 O-P1-85 + round 6 O-P1-103 + round 7 O-P1-109 + round 8 batch 36) ESCALATED to writer-family ban for Examples-narrative + spec-table content type (per N16).

## 角色硬约束 (v1.4 carry-forward unchanged)

参 `archive/v1.4_final_2026-04-28/P0_writer_pdf_v1.4.md` §角色硬约束 全文.

## 派发 subagent_type (v1.5 NEW16 content-type-aware dispatch)

**v1.4 carry-forward**: `oh-my-claudecode:executor` 或 `oh-my-claudecode:writer` 家族 (action-oriented, 带 Write tool). 禁用 `Explore` / `oh-my-claudecode:explore` / `feature-dev:code-explorer` (search-oriented 家族).

**🔴 v1.5 NEW16 content-type-aware dispatch (post 4 cumulative writer-direction VALUE HALLUCINATION recurrences round 5+6+7+8)**:

主 session dispatch MUST cross-check **content type** of target page(s) BEFORE selecting writer-family:

| Content type | Recommended subagent_type | Justification |
|---|---|---|
| **Examples-narrative + spec-table** (TR Example 3 type tables / dense .xpt continuation pages / raw data tables with 24+ pipe-count columns / cross-dataset Examples with relrec.xpt) | **`oh-my-claudecode:executor` MANDATORY** (writer-family BANNED) | 4 cumulative writer-direction VALUE HALLUCINATION recurrences round 5+6+7+8 main-line on this content type; executor-family produces clean output (round 8 batch 36 Option H bulk repair via executor rerun proved 129-atom clean replacement for 127 corrupt 36b writer atoms) |
| **SENTENCE-paragraph + LIST_ITEM-heavy** (chapter intro / domain Description/Overview L4 / Common Assumptions block) | `oh-my-claudecode:writer` 或 executor (free choice, both validated) | No systematic family-direction motif; either family acceptable |
| **Mixed structural transition pages** (R12 transition zones / chapter NEW transitions / L3-leaf-pattern L4 chain start) | `oh-my-claudecode:executor` PREFERRED (boundary discipline) | round 8 batch 37 §6.4 chapter NEW + 4 L3 sub-section transitions = 11 NEW HEADING transitions in single 10-page batch — executor produced 100% PASS first-attempt with 0 amplification baseline |

**v1.4 alternation rule (N14 STRONGLY VALIDATED post 2nd live-fire)** carry-forward unchanged: drift cal rerun MUST 用 alternation table baseline writer ↔ rerun executor or vice versa. NOT same family.

**Drift cal cadence (v1.5 reaffirmed)**: every-3-batches mandatory (cumulative atoms post-last-cal ≥600 also triggers). Drift cal alternation methodology STRONGLY VALIDATED post round 7 batch 33 1st live-fire + round 8 batch 36 2nd live-fire EFFECTIVE.

## 输入 (v1.4 carry-forward + v1.5 N16 NEW field)

参 v1.4 §输入 全文. v1.5 NEW input field:
- `content_type_hint` (**v1.5 NEW per N16**): one of `examples_narrative_spec_table` | `sentence_paragraph_list_heavy` | `mixed_structural_transition` | `unknown`. Main session MUST set this per page-region content cross-check pre-dispatch. Used to validate subagent_type selection per N16 dispatch table.

## 任务流程 (v1.4 carry-forward + v1.5 N17 NEW step)

参 v1.4 §任务流程 6 steps. v1.5 NEW step 7:
7. **(v1.5 NEW per N17)** Pre-DONE post-extraction VALIDATION pass — embedded Self-Validate hooks 14→17 extension:
   - **Hook 15 (NEW)**: regex pipe-count consistency for ALL TABLE_ROW atoms within same parent_section: `verbatim.count('|') == TABLE_HEADER.count('|')` for matching parent (cross-row pipe-count DRIFT halt-on-violation per N5 v1.4 carry-forward strengthened)
   - **Hook 16 (NEW)**: cross-row USUBJID format consistency (regex `^[A-Z0-9-]+$` or per-domain pattern) — flag any USUBJID that differs from prior row's USUBJID format mid-table
   - **Hook 17 (NEW)**: multi-axis value-cell spot-check sample N=3 random TABLE_ROWs from current sub-batch + PDF-cross-verify atom_id, USUBJID, key-data-cell value matches PDF (DETECT 4th cumulative writer-direction VALUE HALLUCINATION recurrence pattern)

═══════════════════════════════════════════════════════════════════
## CODIFIED R-RULES + NEW (v1.4 carry-forward §A-V, FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.4_final_2026-04-28/P0_writer_pdf_v1.4.md` for full §A-V text:
- §A R1-R15 (15 累 R-rules) — v1.3 base + v1.4 N5/N13 hardening
- §B O-P1-26 outer-pipe convention
- §C NEW1 dual-threshold drift cal — **v1.5 STRONGLY VALIDATED 8× round 1-8** (round 8 p.357 NEW1 8th time CATASTROPHIC FAIL writer-direction VALUE HALLUCINATION 4th cumulative recurrence)
- §D NEW2 Cyrillic homoglyph extension — v1.4 N2 11+ chars (К М Н В У + base 7)
- §E NEW3 Option E rerun convention
- §F NEW6/NEW6.b dual-form L4 self-parent NEVER — v1.4 carry-forward
- §G NEW7 L4-L7 chain + L6 PROCEDURAL SUB-BATCH HANDOFF — v1.4 N6 ALL L6 sub-headings + INTRA-AGENT consistency
- §H NEW7 L4 group-container branch — v1.4 carry-forward
- §I NEW8 oracle expansion canonical SUPPQUAL — v1.4 N1
- §J NEW8.b SENTENCE-trigram — v1.4 N4
- §K NEW8.c TABLE_HEADER column-set — v1.4 carry-forward
- §L G-MS-12 density alarm + 12.a content-type-aware floor — v1.4 N12 LIST_ITEM-heavy floor 8
- §M G-MS-13 cross-validation table — v1.4 carry-forward
- §N1-N14 v1.4 NEW patches — full text in archive

═══════════════════════════════════════════════════════════════════
## v1.5 NEW PATCHES (N15-N17, codifying 8 round 8 v1.5 candidates V1-V8)
═══════════════════════════════════════════════════════════════════

### §N15 .xpt-parent / table_caption FORBID rule (per V2 + retroactive sweep)

**Source**: round 8 batch 36 O-P1-122 MEDIUM AMBIGUOUS reviewer slot #46 Plan flagged 27 .xpt-as-parent_section atoms (8 tu.xpt + 8 tr.xpt + 6 relrec.xpt + 5 vs.xpt) AMBIGUOUS-lean-OVERRIDE (discipline-extension reading favored). + reconciler retroactive sweep 9 historical p.133 batch 13 NEW9 violations.

**Rule**: `parent_section` 值 MUST NOT match pattern `^[a-z]+\.xpt$` (.xpt filename used as parent_section). Same as N8 NEW9 L2 short-bracket FORBID for non-L3-HEADING — `parent_section` 值 MUST be a SECTION DESCRIPTOR not a FILE CAPTION.

**Canonical replacement form** (writer-side guidance):

| Source pattern | Wrong (FORBID) | Correct (canonical) |
|---|---|---|
| TU Example 3 dataset | `tu.xpt` | `§6.3.12.3 Example 3 - TU Dataset` (descriptive form) OR `§6.3.12.3 Tumor Identification/Tumor Results Examples` (most-specific section ancestor) |
| TR Example 3 dataset | `tr.xpt` | `§6.3.12.3 Example 3 - TR Dataset` (descriptive form) OR `§6.3.12.3 Tumor Identification/Tumor Results Examples` |
| RELREC dataset for Example 3 | `relrec.xpt` | `§6.3.12.3 Example 3 - RELREC Dataset` (descriptive form) OR `§6.3.12.3 Tumor Identification/Tumor Results Examples` |
| VS Example 1 dataset | `vs.xpt` | `§6.3.13 VS – Examples` (most-specific section ancestor — VS is L3-leaf single-domain so canonical L4 Examples ancestor used) |

**Self-Validate hook (NEW Hook 14.5)**: pre-DONE regex assert `assert not re.match(r"^[a-z]+\.xpt$", a["parent_section"]) for a in atoms` halt-on-violation. If violation found: re-emit with canonical replacement form per table above.

**Implementation impact**: writer-side N15 hook prevents future occurrences. **Retroactive sweep**: 27 batch 36 atoms + 8 historical p.133 atoms = 35 atoms cumulative round 1+8 P1 reconciler-side Option H bulk fix at v1.5 cut session (this session).

### §N16 Writer-family ban for Examples-narrative + spec-table content type (per V3 ESCALATION)

**Source**: 4 cumulative writer-direction main-line VALUE HALLUCINATION recurrences post round 5+6+7+8 (O-P1-85 + O-P1-103 + O-P1-109 + round 8 batch 36 = 4 cumulative). v1.4 N3 NEW8.d EMERGENCY-CRITICAL halt-on-violation EFFECTIVE end-to-end (caught + repaired + verified within v1.4 framework) but underlying motif RECURS — hooks are detection-layer not prevention-layer.

**Rule**: 主 session dispatch MUST cross-check content type pre-dispatch (per §派发 subagent_type table). For **Examples-narrative + spec-table content type**:
- Writer-family MANDATORY-BANNED (oh-my-claudecode:writer NOT permitted)
- Executor-family MANDATORY (oh-my-claudecode:executor required)
- Rationale: round 8 batch 36 Option H bulk repair via executor rerun on p.356/358/359/360 demonstrated executor produces clean output for this content type (129-atom clean replacement for 127 corrupt 36b writer atoms = N=4 cumulative writer-direction recurrence)

**Halt threshold for 5th recurrence**: if drift cal subsequent batch reveals 5th cumulative writer-direction main-line VALUE HALLUCINATION recurrence DESPITE N16 content-type-aware dispatch, ESCALATE to mandatory writer-family ban for ALL TABLE_ROW-heavy content type (not just Examples-narrative + spec-table).

**Self-Validate hook (NEW Hook 16.5)**: pre-dispatch hook check `if content_type_hint == "examples_narrative_spec_table": assert subagent_type == "oh-my-claudecode:executor"` else halt + "N16 violation: writer-family banned for Examples-narrative + spec-table content type per 4 cumulative writer-direction VALUE HALLUCINATION recurrences round 5+6+7+8".

### §N17 Post-extraction VALIDATION pass — Self-Validate hooks 14→17 extension (per V4)

**Source**: round 8 G-MS-NEW-8-5 — N3 hooks detection-not-prevention; v1.4 N3/N5 catch failures at drift cal pre-DONE hook only every 3-4 batches; needs per-batch pre-DONE validation at every batch.

**Rule**: writer pre-DONE Self-Validate hooks expand 14→17 with 3 NEW hooks (light implementation, no new tooling — embedded in writer prompt as spec checklist):
- **Hook 15 (NEW)**: cross-row TABLE_ROW pipe-count consistency check (described in §任务流程 step 7 above)
- **Hook 16 (NEW)**: cross-row USUBJID format consistency (described in step 7)
- **Hook 17 (NEW)**: multi-axis value-cell spot-check sample N=3 (described in step 7)

**Self-Validate hooks final list (v1.5 = 17 hooks)**:
1-9 (P0 v1.1 base): atom_id format / atom_type 9-enum / verbatim non-empty / parent_section non-empty / heading fields / page-region / cross-refs valid / extracted_by required / output_file JSONL strict
10-14 (v1.4 base): R10 verbatim no-paraphrase / R14 wc -l / N3 NEW8.d whole-row VALUE check / N5 TABLE_ROW pipe-count / N6 INTRA-AGENT consistency
14.5 (v1.5 NEW per N15): .xpt-parent FORBID assert
15-17 (v1.5 NEW per N17): cross-row TABLE_ROW pipe-count + USUBJID format + multi-axis value-cell spot-check N=3
16.5 (v1.5 NEW per N16): content-type-aware dispatch assert (pre-dispatch, not pre-DONE)

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.5 per V5)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: graduate from "1st-live-fire-EFFECTIVE" → **"STRONGLY VALIDATED post 2nd live-fire"** (round 7 batch 33 1st + round 8 batch 36 2nd) — production-ready protocol
- **G-MS-4 halt fallback**: graduate from "1st-live-fire-EFFECTIVE" → **"STRONGLY VALIDATED post 2nd live-fire"** (round 7 batch 32 1st + round 8 batch 36 2nd) — production-ready protocol; future rounds 9+ should treat as production-ready (no further validation needed)

═══════════════════════════════════════════════════════════════════
## G-MS-12.b boundary-region density alarm threshold (v1.5 per V6)
═══════════════════════════════════════════════════════════════════

**Source**: round 8 G-MS-NEW-8-6 — QUADRUPLE structural transition single batch (round 7 batch 34 + round 8 batch 36) is normal protocol cadence at boundary regions.

**Rule extension**: G-MS-12.a content-type-aware floor extended with **G-MS-12.b boundary-region floor**:
- If sub-batch contains **4+ structural transitions** (HEADING transitions cumulative L2 chapter / L3 sub-section / L4 sub-section / L5 sub-section / L6 sub-heading) within 10-page span:
  - Per-page floor = 8 (not 15) for ALL pages in sub-batch
  - Sub-batch total floor = 80 (not 100)
- Examples: round 7 batch 34 QUADRUPLE pattern + round 8 batch 36 QUADRUPLE + round 8 batch 37 §6.4 chapter NEW + 4 L3 sub-section transitions = 11 NEW HEADING transitions

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1 | 2026-04-24 | initial P0 Pilot prompt |
| v1.2 | 2026-04-24 | post-P0 收官: schema frozen + 6-item fix matrix |
| v1.3 | 2026-04-27 | post P1 round 4 cut: 13 items A-M codified (R1-R15 + O-P1-26 + NEW1-NEW8 + NEW6/NEW6.b L4 self-parent + NEW7 L4-L7 chain + NEW7 L6 procedural sub-batch handoff template + NEW7 L4 group-container branch + NEW8.b/c + G-MS-12/12.a/13) |
| v1.4 | 2026-04-28 | post P1 round 7 cut EMERGENCY-CRITICAL: 14 NEW writer-side patches N1-N14 covering 24 round 5+6+7 candidates; Self-Validate hooks 9→14 |
| **v1.5** | **2026-04-28** | **post P1 round 8 cut**: (a) 3 NEW writer-side patches N15-N17 covering 8 round 8 v1.5 candidates V1-V8: N15 .xpt-parent / table_caption FORBID rule + retroactive sweep 35 atoms / N16 writer-family ban for Examples-narrative + spec-table content type post 4 cumulative writer-direction VALUE HALLUCINATION recurrences round 5+6+7+8 / N17 per-batch pre-DONE post-extraction VALIDATION pass Self-Validate hooks 14→17 (cross-row pipe-count + USUBJID format + multi-axis value-cell spot-check N=3); (b) STATUS PROMOTIONS N14 strict alternation methodology + G-MS-4 halt fallback graduate from "1st-live-fire-EFFECTIVE" → "STRONGLY VALIDATED post 2nd live-fire" production-ready protocols; (c) G-MS-12.b boundary-region density alarm threshold (4+ transitions in 10-page span = per-page floor 8 / sub-batch floor 80); (d) §派发 subagent_type table content-type-aware dispatch (Examples-narrative + spec-table → executor MANDATORY; SENTENCE-paragraph + LIST_ITEM-heavy → free; mixed structural transition → executor PREFERRED); (e) NEW input field `content_type_hint` per N16 main-session pre-dispatch cross-check; (f) v1.4 archived `archive/v1.4_final_2026-04-28/`. NOT behavior change — writer task structure (Step 1-7) / DONE format / atom_type 9-enum / heading semantic 全 carry-forward unchanged. |
