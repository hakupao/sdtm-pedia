# P0 Writer MD — 原子化 prompt v1.6

> Version: v1.6 (2026-04-29, post P1 round 9 cut, paired sync with `P0_writer_pdf_v1.6.md`)
> 基于 v1.5 (round 8 cut, 3 NEW patches N15-N17 + STRONGLY VALIDATED status N14 + G-MS-4) + round 9 cumulative
> 角色: Writer MD (原子化), 独立 subagent, 与 Reviewer/Matcher 不同 subagent_type
> v1.6 变更 over v1.5: **EMERGENCY-CRITICAL N16 scope ESCALATION (sync with PDF N18) + SENTENCE-paragraph-concat Hook 18 + writer pre-DONE PDF-cross-verify expansion + Self-Validate hooks 15→18.**

## 角色硬约束 (v1.5 carry-forward unchanged)

参 `archive/v1.5_final_2026-04-29/P0_writer_md_v1.5.md` §角色硬约束 全文.

## 派发 subagent_type (v1.6 N18 EXTENDED writer-family ban scope — sync with PDF writer)

主 session dispatch MUST cross-check **content type** + **content patterns** of target md file BEFORE selecting writer-family per N18 EXTENDED scope:

| Content type / Pattern | Recommended subagent_type | Justification |
|---|---|---|
| **Examples-narrative + spec-table dense** (carry-forward N16) | `oh-my-claudecode:executor` MANDATORY (writer-family BANNED) | round 5+6+7+8 4 cumulative recurrences |
| **MD with URLs (regex `https?://`) or DOI references** (NEW v1.6 N18.b) | `oh-my-claudecode:executor` MANDATORY | round 9 batch 39 URL `.org → .ch` fabrication motif applies to MD as PDF |
| **MD with paragraphs ≥500 chars in single SENTENCE** (NEW v1.6 N18.c) | `oh-my-claudecode:executor` MANDATORY | long-cell / paragraph-concat motif |
| **MD with citation, identifier, or VERBATIM-CRITICAL fact** (NEW v1.6 N18.d) | `oh-my-claudecode:executor` MANDATORY | generalization clause |
| **MD with structural transitions (chapter NEW + L3-leaf-pattern L4 chain start)** (NEW v1.6 N18.e — was PREFERRED) | `oh-my-claudecode:executor` MANDATORY | mixed_structural_transition recurrence proof |
| **SENTENCE-paragraph + LIST_ITEM-heavy** (no URLs/long/citations/transitions) | `oh-my-claudecode:writer` 或 executor (free choice) | No systematic family-direction motif |

**Effect**: v1.6 reduces MD writer-family permissible content to plain narrative ONLY (no URLs / no long-cells / no transitions / no Examples).

## 输入 (v1.5 carry-forward + v1.6 NEW)

参 v1.5 §输入. v1.6 NEW input field: `n18_url_atoms_count` / `n18_long_cell_atoms_count` (sync with PDF writer per N18).

═══════════════════════════════════════════════════════════════════
## CODIFIED R-RULES + NEW (v1.5 carry-forward §A-N17 FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.5_final_2026-04-29/P0_writer_md_v1.5.md` for full §A-M v1.3 base + §N1-N9 v1.4 patches + §N15-N17 v1.5 patches.

═══════════════════════════════════════════════════════════════════
## v1.6 NEW PATCHES (sync with PDF writer N18-N20)
═══════════════════════════════════════════════════════════════════

### §N18 EMERGENCY-CRITICAL writer-family ban EXTENDED scope (sync with PDF N18)

`parent_section` 值 + content patterns MUST be cross-checked pre-dispatch. MD files with URL/DOI/long-paragraph/citation/structural-transition content MUST use executor-family.

**Self-Validate hook (NEW Hook 16.6 pre-dispatch — sync with PDF)**: pre-dispatch hook check per N18 EXTENDED scope. Halt-on-violation.

### §N19 SENTENCE-paragraph-concat detection Hook 18 (sync with PDF N19)

MD writer pre-DONE Hook 18 NEW — for each MD-codified SENTENCE atom, regex search `\.\s+[A-Z]` inside verbatim. WARN-mode (no halt). Same writer prompt narrative-chapter exemplar as PDF writer §N19.

### §N20 Writer pre-DONE PDF-cross-verify expansion (sync with PDF N20)

MD writer pre-DONE expansion:
- Sample N=3 → N=10 random atoms per sub-batch
- **Mandatory cross-check** for atoms with URLs/DOIs/citations regardless of sample — **halt-on-violation per any URL/DOI/citation discrepancy with MD source**
- **Long-paragraph TABLE_ROW** (≥500 chars cell content) mandatory cross-check — **halt-on-violation per content drift with MD source**

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks final list (v1.6 = 18 hooks)
═══════════════════════════════════════════════════════════════════

1-12 (v1.4 base): MD writer base hooks
12.5 (v1.5 per N15): .xpt-parent FORBID assert
13-15 (v1.5 per N17): cross-row pipe-count + USUBJID format + multi-axis spot-check N=3
**15.5 / 16 (v1.6 NEW per N18 + N19 + N20)**: pre-dispatch EXTENDED scope assert / SENTENCE-paragraph-concat WARN / PDF-cross-verify N=3→N=10 + mandatory URL/DOI/citation
**17 (v1.6 NEW per OBS-4)**: Hook 13 (parent_section, table_id) granularity refinement (MD tables)
**18 (v1.6 NEW)**: cross-MD-file content type consistency check pre-DONE

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.6 sync with PDF writer)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: STRONGLY VALIDATED post 3rd live-fire (round 7 batch 33 + round 8 batch 36 + round 9 batch 39)
- **G-MS-4 halt fallback**: STRONGLY VALIDATED post 2nd live-fire (round 7 batch 32 + round 8 batch 36) carry-forward
- **N9 + N10 leaf-pattern codifications**: CROSS-LEAF-DOMAIN VALIDATED post 3rd live-fire (FA + SR + TA)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.4 | 2026-04-28 | post P1 round 7 cut: 9 NEW patches N1-N9 |
| v1.5 | 2026-04-28 | post P1 round 8 cut: 3 NEW patches N15-N17 sync + STRONGLY VALIDATED N14 + G-MS-4 |
| **v1.6** | **2026-04-29** | **post P1 round 9 cut EMERGENCY-CRITICAL**: 3 NEW patches N18-N20 sync with PDF writer covering 5 round 9 v1.6 candidates (writer-family ban EXTENDED scope + SENTENCE-paragraph-concat Hook 18 + PDF-cross-verify expansion); Self-Validate hooks 15→18; STATUS PROMOTIONS N14 STRONGLY VALIDATED post 3rd live-fire + N9+N10 CROSS-LEAF-DOMAIN VALIDATED; v1.5 archived. NOT behavior change — MD writer task structure / DONE format 全 carry-forward unchanged. |
