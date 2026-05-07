# Rule A audit summary — P2 B-03c round 11 batch_118 (SV/assumptions.md)

> Reviewer: `pr-review-toolkit:code-reviewer` (P0 reviewer v1.9.3, 35 hooks)
> Writer: `general-purpose` (P0 writer_md v1.9.3) — Rule D 隔离 satisfied (≠ reviewer subagent_type)
> Audit timestamp: 2026-05-07
> Source: `knowledge_base/domains/SV/assumptions.md` (43 lines)
> Atoms: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_118_md_atoms.jsonl` (27 atoms a001..a027)

---

## Verdict: **PASS** (35/35 hooks PASS, 0 HIGH severity findings)

---

## §0 Numeric checksum

| Item | Value |
|---|---|
| Source lines | 43 |
| Atoms produced | 27 |
| atoms/line ratio | 27/43 = **0.6279** |
| atom_type tally | 1 HEADING + 26 LIST_ITEM (0 SENTENCE) |
| H3 in source | 0 (§F-1 §2.11 Plan B N/A) |
| atom_id range | md_dmSV_assn_a001..a027 (sequential, unique) |
| parent_section | 27/27 file-root `§SV [SV — Assumptions]` |

---

## §1 Hook A1 byte-exact verbatim — PASS (27/27)

```python
src = open('knowledge_base/domains/SV/assumptions.md').read().splitlines(keepends=False)
for a in atoms:
    expected = '\n'.join(src[a['line_start']-1:a['line_end']])
    assert a['verbatim'] == expected
```

Result: **0 mismatches across 27 atoms**.

### Indented sub-bullet preservation verify (writer DONE explicit claim)

| L# | atom | indent | byte-exact |
|---|---|---|---|
| L10 | a006 | 3-space `   a.` | PASS |
| L11 | a007 | 3-space `   b.` | PASS |
| L12 | a008 | 3-space `   c.` | PASS |
| L13 | a009 | 3-space `   d.` | PASS |
| L36 | a021 | 4-space `    a.` | PASS |
| L37 | a022 | 4-space `    b.` | PASS |
| L38 | a023 | 4-space `    c.` | PASS |
| L39 | a024 | 4-space `    d.` | PASS |
| L40 | a025 | 4-space `    e.` | PASS |
| L41 | a026 | 4-space `    f.` | PASS |

10/10 indented sub-bullets byte-exact preserved. Writer DONE claim **verified**.

**Note**: Source uses 3-space indent for L10-L13 (under list item 4) and 4-space indent for L36-L41 (under list item 15). Inconsistent indent in source is preserved verbatim — correct Rule B behavior.

---

## §2 v1.9.3 §R-E1..E-6 + §R-F-1..F-3 checks

### §R-E1 CRITICAL Schema regression sweep — PASS

All 27 atoms have exactly the 12 required fields (atom_id, file, line_start, line_end, parent_section, atom_type, verbatim, heading_level, sibling_index, figure_ref, cross_refs, extracted_by). 0 missing keys, 0 extra keys.

### §R-E2 HIGH H1 sib=1 universal — PASS

`md_dmSV_assn_a001`: heading_level=1, sibling_index=1. ✓

### §R-E3 HIGH TABLE_HEADER sib=null — N/A (0 TABLE_HEADER atoms in batch_118)

### §R-E4 HIGH extracted_by object schema — PASS (27/27)

All extracted_by are dicts with `subagent_type` + `prompt_version` + `ts`. Values consistent: `general-purpose` / `P0_writer_md_v1.9.3` / `2026-05-07T13:30:00Z`.

### §R-E5 MED non-HEADING field-explicit-null — PASS (26/26)

All 26 LIST_ITEM atoms have explicit `"heading_level": null, "sibling_index": null` (NOT omitted). ✓

### §R-E6 LOW FIGURE-vs-CODE_LITERAL boundary — N/A (0 FIGURE/0 CODE_LITERAL in batch_118)

### §R-F-1 §2.11 Plan B sub-namespace 4-layer verify — N/A

Source has 0 H3 (grep verified). No §F-1 trigger fires. **Backward compat**: prior production cases (round 07 PC/ex L58, round 09 RELREC/ex L3+L53 + RS/ex L3+L65) unaffected by batch_118 (different files, no edits to those atoms).

### §R-F-2 INFO atoms/line ratio band check — PASS

ratio = 27/43 = **0.6279**, within empirical band 0.59-0.85 (lower-mid edge, consistent with kickoff §0.5 row 23 forecast of "lower-edge bias due 4 ass.md compression"). 10th sustained validation in flight (§F-2 INFO non-blocking).

### §R-F-3 INFO kickoff atom estimate calibration — PASS within threshold

est range 17-22 (mid 19.5); actual 27; delta_pct = |27 − 19.5|/19.5 × 100 = **38.5%** (within ±50% threshold). INFO finding: kickoff slightly under-estimated due to indented sub-bullet expansion (10 sub-bullets produced 10 atoms each, contributing ~37% of total atoms). Non-blocking; calibration carry-forward note for future ass.md with nested numbered+lettered lists.

---

## §3 atom_type semantic consistency — PASS (27/27)

Writer report flag: "narrative paragraphs in numbered-list-only ass.md sometimes get classified as LIST_ITEM if they're top-level numbered items". Audit verified:

- All 16 top-level numbered items (`1.` through `16.`) classified as LIST_ITEM — **CORRECT** (markdown semantics: ordered list items ARE LIST_ITEMs regardless of paragraph length; e.g., a010 is a 414-char narrative paragraph that is still syntactically a numbered list item).
- All 10 lettered sub-bullets (`a.` through `f.`) classified as LIST_ITEM — **CORRECT**.
- 1 H1 heading classified as HEADING — **CORRECT**.

**No atom_type misclassification found**. Note: SV/ass.md is structurally a single ordered list with sub-bullets, so 0 SENTENCE atoms is expected and correct.

---

## §4 Rule A 12-sample semantic audit — 12/12 PASS (100%)

Sample indices (random seed 118): 0, 3, 5, 9, 10, 11, 15, 19, 20, 22, 23, 25.

| # | atom_id | type | L# | parent | byte-exact | semantic |
|---|---|---|---|---|---|---|
| 1 | a001 | HEADING | L1 | §SV [SV — Assumptions] | PASS | PASS |
| 4 | a004 | LIST_ITEM | L7 | §SV [...] | PASS | PASS |
| 6 | a006 | LIST_ITEM | L10 (3-sp indent) | §SV [...] | PASS | PASS |
| 10 | a010 | LIST_ITEM | L15 | §SV [...] | PASS | PASS |
| 11 | a011 | LIST_ITEM | L17 | §SV [...] | PASS | PASS (xref Section 4.4.5) |
| 12 | a012 | LIST_ITEM | L19 | §SV [...] | PASS | PASS (xref Section 4.2.8.3) |
| 16 | a016 | LIST_ITEM | L27 | §SV [...] | PASS | PASS |
| 20 | a020 | LIST_ITEM | L35 | §SV [...] | PASS | PASS |
| 21 | a021 | LIST_ITEM | L36 (4-sp indent) | §SV [...] | PASS | PASS |
| 23 | a023 | LIST_ITEM | L38 (4-sp indent) | §SV [...] | PASS | PASS |
| 24 | a024 | LIST_ITEM | L39 (4-sp indent) | §SV [...] | PASS | PASS |
| 26 | a026 | LIST_ITEM | L41 (4-sp indent) | §SV [...] | PASS | PASS |

12-sample pass rate: **100%** (12/12).

---

## §5 cross_refs verification — PASS (3/3 detected = 3/3 declared)

Detected `Section X.Y.Z` references in verbatim and verified against `cross_refs` field:

| atom_id | L# | detected sections | declared cross_refs | match |
|---|---|---|---|---|
| a002 | L3 | Section 7.3.1 | ["Section 7.3.1"] | PASS |
| a009 | L13 | Section 4.5.7 | ["Section 4.5.7"] | PASS |
| a011 | L17 | Section 4.4.5 | ["Section 4.4.5"] | PASS |
| a012 | L19 | Section 4.2.8.3 | ["Section 4.2.8.3"] | PASS |
| a022 | L37 | (none — only "Event and Intervention Domains") | [] | PASS |

5 atoms with explicit `Section N.M` patterns; 4 declare cross_refs, 1 (a022) correctly has empty cross_refs (no Section reference). **Convention**: only `Section X.Y[.Z]` patterns populate cross_refs; informal domain references (e.g., "Event and Intervention Domains") do not. Consistent with batch_114/117 precedent.

---

## §6 atom_id uniqueness + sequential — PASS

- 27 unique atom_ids (0 collisions)
- Sequential a001..a027 (no gaps)
- prefix `md_dmSV_assn_a` consistent

---

## §7 parent_section consistency — PASS (27/27)

All 27 atoms have parent_section = `§SV [SV — Assumptions]` (file-root). 0 H2/H3 in source → no sub-namespace triggers. Consistent with kickoff §0.5 row 16.

---

## §8 source line coverage — PASS

- 27/27 covered lines (every source non-blank line has exactly 1 atom)
- 0 uncovered non-blank lines
- 16 blank lines (separator) correctly skipped

---

## §9 Hook tally

| Hook category | Count | Status |
|---|---|---|
| v1.7 hooks 1-18 | 18 | PASS |
| v1.9 R22+R23 | 2 | PASS |
| v1.9.1 R24 + R-D2..D6 | 6 | PASS |
| v1.9.2 R25 + R-E2..E-6 | 6 | PASS |
| v1.9.3 R-F-1..F-3 | 3 | PASS (R-F-1 N/A; R-F-2 0.628 in band; R-F-3 38.5% within) |
| **Total** | **35** | **35/35 PASS** |

---

## §10 HIGH severity findings: 0

No HALT triggered. batch_118 is **clean** for round 11 close.

---

## DONE report

```
batch_118 reviewer DONE
- audit verdict: PASS
- Rule A sample size + pass rate: 12 samples, 100% PASS (12/12)
- Hook A1 byte-exact: PASS — L10-L13 (3-sp) + L36-L41 (4-sp) indented sub-bullets verbatim verified
- §R-E1..E-6 + §R-D rules: PASS
- §R-F-1 N/A (0 H3); §R-F-2 0.628 in band (0.59-0.85, lower-mid); §R-F-3 +38.5% within ±50%
- atom_type tally: 1 HEADING + 26 LIST_ITEM = 27 verified (0 misclassification; numbered list items in narrative ass.md correctly LIST_ITEM)
- atom_id uniqueness + sequential: PASS (a001..a027)
- parent_section consistency: 27/27 file-root §SV [SV — Assumptions]
- cross_refs: 4 declared (Section 7.3.1, 4.5.7, 4.4.5, 4.2.8.3) all detected; 0 mismatch
- source coverage: 27/27 non-blank lines covered, 0 gaps
- 35/35 hooks PASS
- HIGH severity findings: 0
```
