# P2 Pilot Rule A Verdicts — Attempt 2 Summary

> Date: 2026-04-29
> Reviewer: oh-my-claudecode:scientist (Rule A independent reviewer)
> Input: `p2_pilot_md_atoms_combined_v2.jsonl` (397 atoms, executor-only)
> Sample: 30 atoms deterministic stratified

---

## 1. Sample Method

Deterministic stratified sampling across all 5 source files and all atom_types present.

**File distribution** (proportional to atom count):
| File | Atoms | In sample |
|------|-------|-----------|
| chapters/ch04_general_assumptions.md | 218 | 14 |
| knowledge_base/domains/CM/examples.md | 77 | 8 |
| knowledge_base/model/01_concepts_and_terms.md | 72 | 5 |
| knowledge_base/model/04_associated_persons.md | 24 | 3 |
| knowledge_base/domains/CM/assumptions.md | 6 | 0 (absorbed into type quotas) |

**Type distribution** (evenly spaced within each type bucket, sorted by file+line):
| Type | Target | Sampled |
|------|--------|---------|
| HEADING | 5 | 5 |
| SENTENCE | 8 | 8 |
| LIST_ITEM | 5 | 5 |
| TABLE_ROW | 5 | 5 |
| TABLE_HEADER | 3 | 3 |
| NOTE | 2 | 2 |
| CODE_LITERAL | 1 | 1 |
| FIGURE | 1 | 1 |
| CROSS_REF | 0 (none exist in dataset) | 0 |
| **Total** | **30** | **30** |

---

## 2. Per-type Verdict Distribution

| Verdict | Count |
|---------|-------|
| PASS | 24 |
| FAIL_VERBATIM | 6 |
| FAIL_ATOM_TYPE | 0 |
| FAIL_LINE_RANGE | 0 |
| FAIL_PARENT_SECTION | 0 |
| FAIL_SCHEMA | 0 |
| PARTIAL | 0 |

**PASS rate: 24/30 = 80.0%**

Breakdown by type:
| Type | Sampled | PASS | FAIL |
|------|---------|------|------|
| HEADING | 5 | 5 | 0 |
| SENTENCE | 8 | 2 | 6 (all FAIL_VERBATIM) |
| LIST_ITEM | 5 | 5 | 0 |
| TABLE_ROW | 5 | 5 | 0 |
| TABLE_HEADER | 3 | 3 | 0 |
| NOTE | 2 | 2 | 0 |
| CODE_LITERAL | 1 | 1 | 0 |
| FIGURE | 1 | 1 | 0 |

---

## 3. Anti-Defect Spot-Check Results (3 Attempt-1 Known Failure Classes)

| Defect Class | Attempt 1 Count | Attempt 2 Count | Status |
|---|---|---|---|
| TABLE_HEADER `line_end` overflow | 13/13 (100%) | **0/3 (0%)** | FIXED |
| Bold `**foo**` fabricated as HEADING | 14 atoms | **0/5 (0%)** | FIXED |
| LIST_ITEM verbatim truncated / prefix stripped | systematic | **0/5 (0%)** | FIXED |

All 3 Attempt-1 anti-defects are fully resolved in Attempt 2. No regressions on these 3 classes.

---

## 4. New Defect Discovered in Attempt 2

### F-P2P-DEFECT-004: SENTENCE Sub-Sentence Extraction (NEW, HIGH)

**Symptom:** When a source file paragraph contains multiple sentences on a single line (as rendered in markdown), the executor splits the paragraph into individual sub-sentence SENTENCE atoms. Each atom has `line_start == line_end` correctly pointing to the paragraph's line, but `verbatim` captures only one sentence from the line rather than the full line content.

**Impact:** 6/8 SENTENCE atoms in sample failed (75% failure rate for SENTENCE type).

**Systematic measurement** (all SENTENCE atoms in dataset):
| File | Total SENTENCE | Full-line match | Sub-sentence only | Hallucinated |
|------|---|---|---|---|
| ch04_general_assumptions.md | 95 | 38 (40%) | 57 (60%) | 0 |
| 01_concepts_and_terms.md | 35 | 4 (11%) | 31 (89%) | 0 |
| 04_associated_persons.md | 6 | 1 (17%) | 5 (83%) | 0 |
| CM/examples.md | 34 | 13 (38%) | 21 (62%) | 0 |
| **Total SENTENCE** | **170** | **56 (33%)** | **114 (67%)** | **0** |

**Root cause:** The executor correctly applies the PLAN §3 rule "1 sentence = 1 SENTENCE atom" for multi-sentence paragraphs, but the MD source lines store entire paragraphs as single lines (common markdown wrap behavior). The executor's sentence-splitting is semantically reasonable but violates the `verbatim = byte-exact match to source at line_start..line_end` requirement: the verbatim must be the full content at those line numbers, not a sub-string.

**Scope:** Affects ~67% of all SENTENCE atoms (114/170). This is a systematic defect in the executor's MD atomization approach for multi-sentence paragraph lines.

**Contrast with Attempt 1:** Attempt 1 writer had 3 defects; Attempt 2 executor eliminated all 3 but introduced this new defect class specifically in SENTENCE atomization.

---

## 5. Comparison: Attempt 1 vs Attempt 2

| Dimension | Attempt 1 (writer) | Attempt 2 (executor) |
|---|---|---|
| PASS rate | 19/30 = 63.3% | 24/30 = 80.0% |
| TABLE_HEADER overflow | 13/13 defective | 0 defects |
| Bold-as-HEADING | 14 atoms defective | 0 defects |
| LIST_ITEM truncation/prefix-strip | systematic | 0 defects |
| SENTENCE sub-sentence extraction | not sampled | 6/8 defective (new) |
| Slice coverage T2' | 71% (stopped early) | 100% (line_end=300) |
| Atom_type coverage | 9/9 | 8/9 (CROSS_REF absent) |
| Fabricated verbatim | some | 0 |

**Improvement:** +16.7 pp PASS rate. All Attempt-1 defects resolved.
**Regression:** New SENTENCE sub-sentence extraction defect is systematic and HIGH severity.

---

## 6. F-P2P-002 and F-P2P-003 Assessment (Attempt 2)

**F-P2P-002 (§4.1 [OVERVIEW] invented numbering):**
Attempt 2 RESOLVED. model/04 now uses `§4 [SDTM v2.0 — Chapter 4: Associated Persons Data]` for the top-level section (unnumbered `## Overview` is no longer forced into a invented `§4.1` sub-number). All model/04 atoms share a single consistent parent_section.
Verdict: **ACCEPTABLE** (issue fixed in Attempt 2).

**F-P2P-003 (§CM.0 0-indexed):**
Attempt 2 RESOLVED. CM/examples.md now uses `§CM.1`–`§CM.5` (1-indexed), and CM/assumptions.md uses `§CM [CM — Assumptions]` as the top-level. No 0-indexed entries found.
Verdict: **ACCEPTABLE** (issue fixed in Attempt 2).

---

## 7. Top Findings

1. **[HIGH — NEW DEFECT] F-P2P-DEFECT-004 SENTENCE sub-sentence extraction is systematic**: 114/170 SENTENCE atoms (67%) have verbatim that is a sub-string of the source line rather than the full line content. Line pointers are correct; verbatim is wrong. This alone drives the 80% PASS rate (below the 90% gate).

2. **[FIXED] All 3 Attempt-1 anti-defects eliminated**: TABLE_HEADER overflow (0/3), bold-as-HEADING (0/5), LIST_ITEM truncation (0/5) — executor completely resolves these.

3. **[INFO] Non-SENTENCE types are near-perfect**: HEADING, LIST_ITEM, TABLE_ROW, TABLE_HEADER, NOTE, CODE_LITERAL, FIGURE all PASS 100% in sample. The defect is exclusively in SENTENCE atomization of multi-sentence markdown paragraphs.

4. **[INFO] T2' slice coverage PASS**: Last atom `md_ch04_a218` has line_end=300, meeting the ≥295 gate.

5. **[INFO] 8/9 atom_types**: CROSS_REF absent from entire dataset (no cross-reference atoms were found/emitted). This is a minor gap — may be inherent to the source files processed.

---

## 8. Gate Verdict

| Condition | Result |
|---|---|
| PASS rate ≥ 90% | **FAIL** (80.0%) |
| T2' last atom line_end ≥ 295 | PASS (300) |
| Anti-defect: TABLE_HEADER overflow = 0 | PASS |
| Anti-defect: bold-as-HEADING = 0 | PASS |
| Anti-defect: LIST_ITEM truncation = 0 | PASS |
| F-P2P-002 resolved | PASS |
| F-P2P-003 resolved | PASS |

**Overall Gate: FAIL** (PASS rate 80% < 90% threshold)

**Root cause for FAIL:** Single new defect class F-P2P-DEFECT-004 (SENTENCE sub-sentence extraction) affects 6/8 SENTENCE atoms in sample. Fixing this requires redefining the verbatim convention for SENTENCE atoms from multi-sentence paragraphs: either (a) each SENTENCE atom verbatim = the full source line with `line_start == line_end` for all sentences in that paragraph (sub-sentence atoms omit `verbatim` uniqueness), or (b) SENTENCE atoms spanning a multi-sentence paragraph must have verbatim = full line content (one atom per physical line, not per logical sentence).

**Recommendation for Attempt 3:** Clarify prompt: for multi-sentence paragraphs stored as a single line in markdown, each SENTENCE atom must have verbatim = the full paragraph line text. Sentence splitting is acceptable for atom_id and parent_section, but verbatim must be the complete physical line. Alternative: move to character-offset-based verbatim for sub-sentence granularity. The line-based schema as currently defined cannot support sub-sentence verbatim fidelity.
