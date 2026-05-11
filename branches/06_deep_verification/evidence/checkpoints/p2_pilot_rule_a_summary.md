# P2 Pilot — Rule A Scientist Verdict Summary

> Reviewer slot: `oh-my-claudecode:scientist` (P2 内 Rule A slot #1, independent of writer pool)
> Date: 2026-04-29
> Input: `p2_pilot_md_atoms_combined.jsonl` (383 atoms, 5 files)
> Output: `p2_pilot_rule_a_verdicts.jsonl` (30 sampled atoms)

---

## 1. Sampling Method (Deterministic; Reproducible)

**Method**: Deterministic stratified sampling within each `atom_type` stratum.

1. Group atoms by `atom_type`.
2. Within each stratum, sort by `(file_priority_index, atom_id)` where file order = `[model/01, model/04, chapters/ch04, domains/CM/assumptions, domains/CM/examples]`.
3. Pick `N` atoms at evenly-spaced indices: `indices = [int(i * total/N) for i in range(N)]`.
4. No randomness — fully reproducible given same combined JSONL input.

**File coverage**: All 5 pilot files represented in the sample. Writer A (executor) atoms: model/01, model/04, CM/assumptions. Writer B (writer) atoms: ch04, CM/examples.

---

## 2. Per-Type Sampling Distribution

| atom_type | Pool | Sampled | Files Covered |
|---|---|---|---|
| HEADING | 49 | 5 | model/01, model/04, ch04, CM/examples |
| SENTENCE | 166 | 8 | model/01, ch04, CM/examples |
| LIST_ITEM | 54 | 5 | model/01, model/04, ch04, CM/assumptions |
| TABLE_ROW | 90 | 5 | model/01, model/04, ch04, CM/examples |
| TABLE_HEADER | 16 | 3 | model/01, ch04 |
| NOTE | 3 | 1 | model/01 |
| CODE_LITERAL | 3 | 1 | ch04 |
| FIGURE | 1 | 1 | model/01 |
| CROSS_REF | 1 | 1 | ch04 |
| **Total** | **383** | **30** | — |

---

## 3. Verdict Breakdown

| Verdict | Count | % |
|---|---|---|
| PASS | 19 | 63.3% |
| PARTIAL (minor, not blocking) | 6 | 20.0% |
| FAIL_VERBATIM | 2 | 6.7% |
| FAIL_LINE_RANGE | 2 | 6.7% |
| FAIL_ATOM_TYPE | 1 | 3.3% |
| **Total** | **30** | **100%** |

**PASS rate: 19/30 = 63.3%**
**PASS + PARTIAL rate: 25/30 = 83.3%**

Both rates are below the ≥90% gate threshold.

---

## 4. Top 5 Systematic Findings

### Finding 1 — TABLE_HEADER line_end spans entire table (Writer B, 13/13 = 100%)

**Severity: BLOCKING**

All 13 TABLE_HEADER atoms produced by `oh-my-claudecode:writer` (ch04 + CM/examples) set `line_end` to the last row of the *entire table* rather than the header + separator rows (lines N and N+1).

- Example: `md_ch04_a086` claims lines 93–102 (10 lines) but verbatim contains only 2 lines (header + separator). The data rows (lines 95–102) are separately and correctly atomized as TABLE_ROW atoms.
- Effect: `line_end` for every Writer-B TABLE_HEADER overlaps with the TABLE_ROW atoms that follow it — causing line-range collisions in any downstream line-based lookup.
- All 3 TABLE_HEADER atoms from `oh-my-claudecode:executor` (model/01 and model/04) are correct (single-line range = 1).
- **13 affected atoms**: `md_ch04_a033`, `a074`, `a086`, `a096`, `a104`, `a117`, `a121`, `a133`; `md_dmCM_ex_a013`, `a028`, `a045`, `a059`, `a080`.

### Finding 2 — Bold-text labels misclassified as HEADING (Writer B, 14 atoms)

**Severity: BLOCKING**

14 atoms across ch04 and CM/examples use `atom_type=HEADING` for lines beginning with `**Bold text**` (markdown bold, not `#` heading syntax). These are dataset-label captions (e.g., `**relrec.xpt**`, `**Dataset for Clinical Global Impressions — qscg.xpt**`, `**cm.xpt**`).

- HEADING requires markdown `#`/`##`/`###`/`####` prefix by definition.
- `heading_level` is fabricated (e.g., level 4 for non-`#` text).
- Should be `SENTENCE` (table caption) or `NOTE`.
- All 14 are Writer B (`oh-my-claudecode:writer`) atoms; executor produces zero such errors.
- **14 affected atoms**: `md_ch04_a073`, `a085`, `a095`, `a103`, `a115`, `a116`, `a120`, `a132`, `a152`; `md_dmCM_ex_a012`, `a027`, `a044`, `a058`, `a079`.

### Finding 3 — LIST_ITEM verbatim truncated to first sentence only (Writer B, systematic)

**Severity: BLOCKING**

Multi-sentence list items in ch04 have verbatim truncated to the first sentence only, silently discarding subsequent sentences. Also: numbered/bulleted prefixes (`- `, `10. `) are stripped from verbatim.

- `md_ch04_a052` (line 61): verbatim = "A domain based on a general observation class may be split according to values in --CAT." — missing "When a domain is split on --CAT, --CAT must not be null." Also `line_end=62` is wrong (points to a *different* list item on line 62).
- `md_ch04_a078` (line 83): verbatim = first sentence of item 10 only, missing "For additional examples, see the Metadata Submission Guideline…"
- By contrast, `md_dmCM_assn_a004` (Writer A / executor) captures the full 6-sentence sub-item on line 6 correctly.
- Pattern is Writer B only; Writer A (executor) has no LIST_ITEM verbatim truncation.

### Finding 4 — T2' ch04 slicing shortfall: lines 215–300 unatomized (F-P2P-001 CONFIRMED)

**Severity: BLOCKING** (scope gap, not a verbatim error)

The T2' task contracted lines 1–300 of `chapters/ch04_general_assumptions.md`. The combined JSONL contains ch04 atoms only up to `line_start=214` / `line_end=214`. Section `§4.2 General Variable Assumptions` (starting at line 216) and subsections §4.2.1–§4.2.6 (lines 218–300) are entirely absent — approximately 49 non-empty lines yielding ~30–50 missing atoms.

Atoms within lines 1–214 are otherwise present and verbatim-correct (modulo findings 1–3 above).

### Finding 5 — §4.1 [OVERVIEW] for unnumbered section in model/04 (F-P2P-002 CONFIRMED + §CM.0 convention)

**Severity: PARTIAL** (convention issue, not blocking individually)

- **F-P2P-002**: `model/04_associated_persons.md` has an unnumbered `## Overview` at line 5. All atoms from this file use `parent_section = §4.1 [OVERVIEW]`, fabricating the `.1` sub-number. Per N27, §N.M form requires a numbered source heading. Internally consistent across the file, but non-canonical.
- **F-P2P-003 §CM.0 indexing**: CM/examples uses 0-indexed sub-numbers (`§CM.0 [Example 1]` … `§CM.4 [Example 5]`) for unnumbered `## Example N` headings. Section 0 is not a valid CDISC section number. The downstream P4a matcher will need an explicit convention declaration to handle this correctly.

---

## 5. Priors Verdict

| Prior | Status | Finding |
|---|---|---|
| **F-P2P-001** ch04 slicing | **CONFIRMED — BLOCKING** | Max line covered = 214. §4.2 (lines 216–300) absent. ~30–50 atoms missing. |
| **F-P2P-002** §4.1 [OVERVIEW] | **CONFIRMED — PARTIAL** | Internally consistent but §4.1 is interpolated for unnumbered heading. Tolerable if documented as accepted convention; recommend decision in pilot report. |
| **F-P2P-003** §CM parent_section | **CONFIRMED — PARTIAL** | §CM [ASSUMPTIONS] and §CM [CM — Examples] are acceptable domain-code conventions. §CM.0 [Example 1] (0-indexed) is non-standard; recommend §CM.1 or §CM [Example 1] instead. Convention decision required before P2 production. |

---

## 6. Writer-Type Attribution

| Defect | Writer A (executor) | Writer B (writer) |
|---|---|---|
| TABLE_HEADER line_end overflow | 0/3 (0%) | 13/13 (100%) |
| Bold-text-as-HEADING | 0 atoms | 14 atoms |
| LIST_ITEM verbatim truncation | 0 atoms | ≥2 atoms in sample |
| LIST_ITEM prefix stripped | 0 | ≥2 atoms in sample |

All three blocking defect classes are **Writer B (oh-my-claudecode:writer) only**. Writer A (executor) produces clean atoms across all sampled checks.

---

## 7. Gate Verdict

**GATE: FAIL**

| Criterion | Threshold | Actual | Result |
|---|---|---|---|
| PASS rate | ≥90% (≥27/30) | 19/30 = 63.3% | **FAIL** |
| PASS+PARTIAL rate | ≥90% | 25/30 = 83.3% | **FAIL** |

Gate fails on both strict and lenient criteria. The 5 FAIL verdicts represent systematic, repeatable defect patterns (not isolated errors) affecting 100% of Writer B TABLE_HEADER atoms, a majority of bold-label atoms, and multiple LIST_ITEM atoms.

**Halt recommendation**: P2 production dispatch should be halted until Writer B prompt defects are resolved. Specifically:

1. **v1.9 prompt fix required** for `oh-my-claudecode:writer`: TABLE_HEADER `line_end` must be set to the separator row only (header+separator = 2 lines max); bold-text labels (`**...**`) must NOT be classed as HEADING; LIST_ITEM verbatim must include full bullet text (all sentences); bullet/number prefix (`- `, `N. `) must be retained in verbatim.
2. **T2' ch04 rerun required**: lines 215–300 must be atomized (new slice T2'b) to close the scope gap.
3. **Convention decisions required before production**: F-P2P-002 (unnumbered section numbering) and F-P2P-003 (§CM.0 vs §CM.1 indexing) must be decided and codified in the v1.9 prompt.

---

*Report generated 2026-04-29 by `oh-my-claudecode:scientist` (Rule A Reviewer, P2 pilot, independent of writer pool).*
*Evidence: `p2_pilot_rule_a_verdicts.jsonl` (30 records)*
