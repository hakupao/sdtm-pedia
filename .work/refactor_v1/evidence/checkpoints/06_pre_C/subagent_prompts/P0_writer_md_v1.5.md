# P0 Writer MD — 原子化 prompt v1.5

> Version: v1.5 (2026-04-28, post P1 round 8 cut, paired sync with `P0_writer_pdf_v1.5.md`)
> 基于 v1.4 (round 7 cut, 9 NEW patches N1-N9 covering 24 round 5+6+7 candidates) + round 8 cumulative
> 角色: Writer MD (原子化), 独立 subagent, 与 Reviewer/Matcher 不同 subagent_type
> v1.5 变更 over v1.4: **codification + STRONGLY VALIDATED status promotion + Self-Validate hooks 12→15.**

## 角色硬约束 (v1.4 carry-forward unchanged)

参 `archive/v1.4_final_2026-04-28/P0_writer_md_v1.4.md` §角色硬约束 全文.

## 派发 subagent_type (v1.5 NEW16 content-type-aware dispatch — sync with PDF writer)

主 session dispatch MUST cross-check **content type** of target md file BEFORE selecting writer-family per N16:

| Content type | Recommended subagent_type | Justification |
|---|---|---|
| **Examples-narrative + spec-table dense** (md files with TR Example 3 / .xpt continuation tables / 24+ pipe-count rows) | **`oh-my-claudecode:executor` MANDATORY** (writer-family BANNED per PDF N16 sync) | 4 cumulative writer-direction VALUE HALLUCINATION recurrences round 5+6+7+8 main-line; same family-direction motif applies to MD as PDF |
| **SENTENCE-paragraph + LIST_ITEM-heavy** | `oh-my-claudecode:writer` 或 executor (free choice) | No systematic family-direction motif on this content type |
| **Mixed structural transition** (chapter intro + L3 sub-section transitions) | `oh-my-claudecode:executor` PREFERRED | round 8 batch 37 boundary discipline 100% PASS first-attempt precedent |

## 输入 (v1.4 carry-forward + v1.5 N16 NEW field)

参 v1.4 §输入. v1.5 NEW input field: `content_type_hint` (sync with PDF writer per N16).

═══════════════════════════════════════════════════════════════════
## CODIFIED R-RULES + NEW (v1.4 carry-forward §A-V FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.4_final_2026-04-28/P0_writer_md_v1.4.md` for full §A-M v1.3 base + §N1-N9 v1.4 NEW patches.

═══════════════════════════════════════════════════════════════════
## v1.5 NEW PATCHES (sync with PDF writer N15-N17)
═══════════════════════════════════════════════════════════════════

### §N15 .xpt-parent / table_caption FORBID rule (sync with PDF N15)

`parent_section` 值 MUST NOT match pattern `^[a-z]+\.xpt$`. Same canonical replacement form table as PDF writer §N15.

**Self-Validate hook (NEW Hook 12.5)**: pre-DONE regex assert `assert not re.match(r"^[a-z]+\.xpt$", a["parent_section"])` halt-on-violation.

### §N16 Writer-family ban for Examples-narrative + spec-table content type (sync with PDF N16)

主 session dispatch must cross-check content type pre-dispatch (per §派发 subagent_type table). MD files with Examples-narrative + spec-table content type MUST use executor-family.

### §N17 Post-extraction VALIDATION pass — Self-Validate hooks 12→15 extension (sync with PDF N17)

MD writer pre-DONE Self-Validate hooks expand 12→15 with 3 NEW hooks:
- **Hook 13 (NEW)**: cross-row TABLE_ROW pipe-count consistency check (md tables)
- **Hook 14 (NEW)**: cross-row USUBJID format consistency
- **Hook 15 (NEW)**: multi-axis value-cell spot-check sample N=3 random rows + cross-verify against md source

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (sync with PDF writer per V5)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: STRONGLY VALIDATED post 2nd live-fire (round 7 batch 33 + round 8 batch 36)
- **G-MS-4 halt fallback**: STRONGLY VALIDATED post 2nd live-fire (round 7 batch 32 + round 8 batch 36)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.4 | 2026-04-28 | post P1 round 7 cut: 9 NEW patches N1-N9 covering 24 round 5+6+7 candidates; Self-Validate hooks 8→12 |
| **v1.5** | **2026-04-28** | **post P1 round 8 cut**: 3 NEW patches N15-N17 sync with PDF writer N15-N17 covering 8 round 8 v1.5 candidates V1-V8 (.xpt-parent FORBID + writer-family ban Examples-narrative + spec-table + post-extraction VALIDATION pass Self-Validate hooks 12→15); STATUS PROMOTIONS N14 + G-MS-4 STRONGLY VALIDATED post 2nd live-fire; G-MS-12.b boundary-region density alarm threshold; v1.4 archived. NOT behavior change — MD writer task structure / DONE format / atom_type 9-enum / heading semantic 全 carry-forward unchanged. |
