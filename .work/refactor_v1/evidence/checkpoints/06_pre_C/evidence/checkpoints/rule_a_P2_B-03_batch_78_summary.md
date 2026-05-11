# Rule A Audit Summary — P2 B-03c round 06 batch_78 (OI/assumptions.md)

> Reviewer: pr-review-toolkit:code-reviewer
> Writer: general-purpose (P0_writer_md_v1.9.1)
> Rule D 隔离: PASS (writer general-purpose ≠ reviewer pr-review-toolkit:code-reviewer)
> Date: 2026-05-06
> Reviewer prompt: P0_reviewer_v1.9.1
> Source: knowledge_base/domains/OI/assumptions.md (22 lines)
> Atoms: 15 (md_dmOI_assn_a001..a015)

## Verdict: **PASS** (15/15 sampled = 100% strict PASS)

## Sampling

Total sampled: **15 atoms (full coverage)** — small batch (atoms ≤ 20) audited in entirety per Rule A best practice.

### Full coverage roster

| atom_id | line | atom_type | sample_class |
|---|---|---|---|
| a001 | 1 | HEADING | full_coverage_HEADING_H1 |
| a002 | 3 | SENTENCE | full_coverage_SENTENCE_pre_list_intro |
| a003 | 5 | SENTENCE | full_coverage_SENTENCE_pre_list_intro |
| a004 | 7 | LIST_ITEM | full_coverage_LIST_ITEM_top_numbered (#1) |
| a005 | 9 | LIST_ITEM | full_coverage_LIST_ITEM_top_numbered (#2) |
| a006 | 10 | LIST_ITEM | full_coverage_LIST_ITEM_sub_letter (2.a) |
| a007 | 11 | LIST_ITEM | full_coverage_LIST_ITEM_sub_letter (2.b) |
| a008 | 12 | LIST_ITEM | full_coverage_LIST_ITEM_sub_roman (2.b.i) |
| a009 | 13 | LIST_ITEM | full_coverage_LIST_ITEM_sub_roman (2.b.ii) |
| a010 | 15 | LIST_ITEM | full_coverage_LIST_ITEM_top_numbered (#3) |
| a011 | 17 | LIST_ITEM | full_coverage_LIST_ITEM_top_numbered (#4) |
| a012 | 18 | LIST_ITEM | full_coverage_LIST_ITEM_sub_letter (4.a) |
| a013 | 19 | LIST_ITEM | full_coverage_LIST_ITEM_sub_letter (4.b) |
| a014 | 20 | LIST_ITEM | full_coverage_LIST_ITEM_sub_letter (4.c) |
| a015 | 22 | LIST_ITEM | full_coverage_LIST_ITEM_top_numbered (#5) |

## Schema regression check (priority)

- 12-key schema: **15/15 PASS** (atom_id, file, line_start, line_end, parent_section, atom_type, verbatim, heading_level, sibling_index, figure_ref, cross_refs, extracted_by)
- atom_type enum (HEADING/SENTENCE/LIST_ITEM): **PASS** (no out-of-enum values; no TABLE_HEADER/TABLE_ROW/NOTE in batch)
- No H1/H2 strings in atom_type field: **PASS**
- All 12 keys present in every atom: **PASS** (no missing fields)

## Atom_type breakdown (15 atoms)

| Type | Count | Lines |
|---|---|---|
| HEADING | 1 | 1 (1 H1) |
| SENTENCE | 2 | 3, 5 (pre-list narrative intros) |
| LIST_ITEM | 12 | 7, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20, 22 |

### LIST_ITEM hierarchy detail

- **Top-level numbered (5)**: a004 (#1, L7), a005 (#2, L9), a010 (#3, L15), a011 (#4, L17), a015 (#5, L22)
- **Sub-letter 4-space indent (5)**: a006 (2.a, L10), a007 (2.b, L11), a012 (4.a, L18), a013 (4.b, L19), a014 (4.c, L20)
- **Sub-roman 8-space indent (2)**: a008 (2.b.i, L12), a009 (2.b.ii, L13)

## Invariants (all green)

- **R-2.8-1 H1 sib=1**: PASS (a001 sib=1)
- **R-2.8-3 extracted_by object**: PASS (15/15 with subagent_type+prompt_version+ts)
- **Hook C-8 file prefix**: PASS (md_dmOI_assn_*)
- **LIST_ITEM/SENTENCE heading_level=null AND sibling_index=null EXPLICIT JSON**: PASS (14/14 non-heading atoms)
- **parent_section uniform**: PASS (15/15 = `§OI [OI — Assumptions]`)
- **figure_ref**: PASS (15/15 = null)
- **cross_refs**: PASS (15/15 = []); HCV is virus name not domain code; NHOID/OIPARMCD/OIPARM/OIVAL/OISEQ are internal OI variables (R-D7.3 — no cross-domain reference present)
- **Coverage**: 15/15 non-blank source lines covered (zero missing, zero overlaps); 22 source lines − 7 blank lines (L2/L4/L6/L8/L14/L16/L21) = 15 content lines == 15 atoms
- **atom_id sequential**: PASS (a001..a015 contiguous)
- **Indent byte-exact preservation**: PASS — verified via xxd hex-dump for L10/L11/L18/L19/L20 (4-space `2020 2020`) and L12/L13 (8-space `2020 2020 2020 2020`)
- **Special character preservation**: PASS — em-dash U+2014 (L1 title), curly quotes around `"species."` (L5), `"species"` (L18), `"H77"` and `"HCV1a-H77"` (L13)

## Per-atom audit (15 verdicts)

All 15 atoms (full coverage): **verbatim byte-exact match** vs source, line_range correct, parent_section correct, sib_index correct, h_lvl correct, cross_refs correct, schema 12-key present.

See verdicts JSONL: `rule_a_P2_B-03_batch_78_verdicts.jsonl`.

## Kickoff drift verification (R-D1)

Reviewer independently `wc -l` on source: **22 lines** (matches kickoff claim). JSONL contains exactly **15 atoms** (matches kickoff claim 15 atoms). Density 15/22 = **0.682** matches kickoff. **No kickoff drift detected.**

## D-codified anomaly instances

- §R-D2 NOTE blockquote-prefix: **N/A** (no NOTE atoms in batch)
- §R-D3 D5 markdown-uniform numbered Heading dual-constraint: **N/A** (single H1, no numbered headings)
- §R-D4 D8 numberless `## Overview` chapter root inherit: **N/A** (no Overview structure; pre-list SENTENCE intros (a002/a003) inherit chapter root H1 `§OI [OI — Assumptions]` directly per natural file structure since no H2 exists)
- §R-D5 bold-caption SENTENCE: **N/A** (no bold-caption atoms; SENTENCE atoms a002/a003 are plain narrative)
- §R-D6 TABLE_HEADER pilot legacy 1-row: **N/A** (no TABLE atoms)
- §R-D7.2 Axis 5 numbered LIST_ITEM: **PASS** (12/12 LIST_ITEM atoms — top-level `^N\.\s+`, sub-letter `^\s{4}[a-z]\.\s+`, sub-roman `^\s{8}[ivx]+\.\s+` — all canonical LIST_ITEM)

## Audit matrix row (pre-formatted)

```
| batch_78 | 2026-05-06 | OI/assumptions.md | 22 | 15 | 0.682 | 1H + 2 SENTENCE + 12 LIST_ITEM | general-purpose | pr-review-toolkit:code-reviewer | 15/15=100% | schema_12key+R2.8-1+R2.8-3+HookC-8+coverage15/15+indent_byte_exact | 0 HIGH/MEDIUM/LOW | PASS |
```

## Findings

**0 HIGH / 0 MEDIUM / 0 LOW.**

Batch_78 is the small companion of round 06 (15 atoms, 22 source lines, density 0.682). File is a clean Assumptions document with single H1, two pre-list narrative SENTENCE intros, and a 5-item top-level numbered list (some with sub-letter and sub-roman nested items). All indent levels (4-space sub-letter, 8-space sub-roman) preserved byte-exact via xxd verification. All quotes (curly U+201C/U+201D around "species" / "H77" / "HCV1a-H77") and em-dash (U+2014 in title) preserved byte-exact. SENTENCE atoms a002/a003 correctly inherit chapter root parent_section since no H2 structure exists in this short file (canonical for short single-section domain assumption files).

## Halt check

- PASS rate ≥ 90%: **100% — no halt**
- HIGH severity: **0 — no halt**
- R-2.8 violation: **0 — no halt**
- MED-01 (LIST_ITEM/SENTENCE non-null sib/h_lvl): **0 — no halt**
- Schema regression: **0 — no halt**

## Verdict

**PASS** — batch_78 is GREEN. Continue round 06 dispatch.
