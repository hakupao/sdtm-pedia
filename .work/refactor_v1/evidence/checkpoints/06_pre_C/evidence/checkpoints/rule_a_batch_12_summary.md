# Rule A Audit — Batch 12 Summary
<!-- scope: p.111-120 §6.1.3.3 Exposure/Exposure as Collected Examples -->
<!-- reviewer: oh-my-claudecode:debugger (independent audit, slot #21) -->
<!-- seed: 20260465 | date: 2026-04-25 -->

## Top-Line Results

| Metric | Value |
|--------|-------|
| Total sampled | 10 |
| PASS | 8 |
| PARTIAL | 1 |
| FAIL | 1 |
| Weighted PASS rate | (8×1.0 + 1×0.5 + 1×0.0) / 10 = **85%** |
| **Final Verdict** | **CONDITIONAL_PASS** (≥80% but <90%) |

## Per-Atom Verdict Table

| atom_id | page | atom_type | verdict | severity | key finding |
|---------|------|-----------|---------|----------|-------------|
| ig34_p0111_a006 | 111 | TABLE_HEADER | PASS | null | 5-column Exposure CRF header exact match |
| ig34_p0112_a021 | 112 | TABLE_ROW | PASS | null | Vertical CRF row "Volume Given (mL) \| 5" exact match |
| ig34_p0113_a019 | 113 | TABLE_ROW | PASS | null | ec.xpt Row 5 Example 3 — 16 columns exact match |
| ig34_p0114_a022 | 114 | HEADING | PASS | null | "Subject ABC5003" L5 sib=null per convention |
| ig34_p0115_a017 | 115 | TABLE_ROW | PASS | null | ex.xpt Row 3 Example 5 — 19 columns exact match |
| ig34_p0116_a011 | 116 | TABLE_ROW | PARTIAL | LOW | ECTRT cell-wrap: "BOTTLE" may be "BOTTLE\n2" (R10 ambiguity) |
| ig34_p0117_a004 | 117 | HEADING | PASS | null | "Example 7" L5 sib=7 correct |
| ig34_p0118_a036 | 118 | TABLE_ROW | FAIL | HIGH | Page attribution error: ex.xpt Row 2 is on p.119, not p.118 |
| ig34_p0119_a005 | 119 | HEADING | PASS | null | "Example 8" L5 sib=8 correct |
| ig34_p0120_a014 | 120 | TABLE_ROW | PASS | null | ex.xpt Row 2 Example 8 — 16 columns exact match |

## Findings Detail

### F-12-01 — FAIL | HIGH | ig34_p0118_a036 — Page Attribution Error

**Atom**: `ig34_p0118_a036`, TABLE_ROW, table_ref="ex.xpt"

**Finding**: The atom's `page` field is set to `118`, but the ex.xpt table for Example 7 physically begins on **page 119**. Page 118 contains only:
- A transposed CRF table (Visit 1/2/3 columns)
- The ec.xpt table (6 rows: ABC123-0201 rows 1-6)
- Explanatory text ending with "Row 2: Shows the subject's second dose."

Page 119 starts with the `ex.xpt` label and two data rows. Row 2 of that ex.xpt matches the atom verbatim exactly:
`ABC123 | EX | ABC123-0201 | 2 | 20090220T1100 | V2 | DRUG Z | 2.6 | mg/kg | SOLUTION | CONTINUOUS | INTRAVENOUS | Injection site reaction | 2 | VISIT | TREATMENT | 2009-02-20 | 2009-02-20 | 8 | 8`

**Dimensions affected**: page metadata (HIGH — breaks source traceability)
**Content correctness**: verbatim, parent_section, atom_type all correct

**Recommended scope-sweep**: Check all atoms from batch 12 with page=118 that reference ex.xpt or appear at high atom_index_on_page (>30) — they may belong to page 119. Specifically audit whether the ex.xpt table for Example 7 was systematically mis-attributed to p.118 across all its atoms.

---

### F-12-02 — PARTIAL | LOW | ig34_p0116_a011 — R10 Cell-Wrap Ambiguity in ECTRT

**Atom**: `ig34_p0116_a011`, TABLE_ROW, table_ref="ec.xpt"

**Finding**: The ec.xpt table on page 116 contains 22 rows for subjects 56789001 (rows 1-12) and 56789003 (rows 13-22). The ECTRT column shows alternating values that appear to be "BOTTLE" with a line-wrapped bottle number (1 or 2). For Row 2 (the sampled atom), the ECTRT value is captured as just `BOTTLE`, but the CRF context (page 115 bottom: CRF for Subject 56789001 shows Period 1 with Bottle 1 and Bottle 2) suggests the actual ECTRT may be `BOTTLE 1` or `BOTTLE 2` with the number being a cell-wrap artifact.

The alternating dosage form (CAPSULE / TABLET, COATED for odd/even rows) further supports the hypothesis that odd rows = Bottle 1 and even rows = Bottle 2.

**R10 relevance**: Cell-wrap artifact `\n2` dropped, resulting in `BOTTLE` instead of `BOTTLE\n2`.

**Severity**: LOW — ambiguous from PDF rendering; the "2" below BOTTLE in ECTRT column may be a visual rendering artifact rather than a true cell value.

**Recommended scope-sweep**: Review all ec.xpt atoms from pages 115-116 (Example 6) where ECTRT appears as bare `BOTTLE` — check whether bottle number suffixes were dropped across the full table.

---

## Spot-Check Observations (Outside Sample — R6/R8/R10/R11/Heading Convention)

### OBS-12-01 — R6 Codelist Literal Check
- Pages 111-120 contain EXDOSFRM values: `TABLET`, `TABLET, COATED`, `CAPSULE`, `SOLUTION`. No codelist references with `(UNIT)` / `(ROUTE)` / `(FREQ)` pattern found in these pages — not applicable to this batch scope (codelist parenthetical notation appears in spec sections, not example dataset tables).
- EXDOSU values observed: `mg`, `mg/kg`, `mL` — all lowercase/mixed as per PDF, no codelist substitution artifacts detected.

### OBS-12-02 — R8 Empty Cell `| |` Check
- The ec.xpt table on page 118 (Example 7) Row 6 shows ECOCCUR="N" with null ECDOSE and null ECDOSU. These empty cells should be captured as `| |`. The sampled atom (p0118_a036) is from the ex.xpt table not ec.xpt, so this specific row was not sampled — but any atoms for ec.xpt Row 6 on p.118 should be checked for proper `| |` handling.
- Page 113 ec.xpt Row 4 (ECOCCUR=N) has empty ECDOSE and ECDOSU — similarly requires `| |` for those cells.

### OBS-12-03 — R11 Trailing Empty Cell / Column Count Check
- The ec.xpt table on page 116 has 21 columns; atom ig34_p0116_a011 uses bounding-pipe format and presents 21 values — column count preserved. Consistent with R11.
- The ex.xpt on page 119 (Example 7) has columns including EXADJ — atom ig34_p0118_a036 includes "Injection site reaction" for EXADJ correctly. No trailing empty cell collapse detected in sampled atoms.

### OBS-12-04 — R10 Cell-Wrap Artifacts
- Page 115 ex.xpt EXLNKID column shows values like `20120101-20120108-AM` and `20120101-20120108-PM` — these are long strings that could wrap. Atom ig34_p0115_a017 captures `20120201-20120208-AM` correctly without truncation.
- Page 116 ec.xpt ECSTDTC and ECENDTC columns show ISO datetime values like `2002-07-01T07:30` — these appear in two-line cells (date on top, time on second line). The atom ig34_p0116_a011 captures `2002-07-01T07:30` as a single value — correctly reassembled.
- **Potential systematic issue** (OBS-12-04a): The ECTRT "BOTTLE" values in the page 116 ec.xpt may all be affected by the same cell-wrap drop (bottle number on second line dropped). Recommend full-table sweep of Example 6 ec.xpt atoms.

### OBS-12-05 — Heading Level / Sibling Index Continuity
- Page 111: §6.1.3.3 heading (bold, L4 sib=3) confirmed.
- Page 111: "Example 1" (L5 sib=1), page 112: "Example 2" (L5 sib=2), page 113: "Example 3" (L5 sib=3), page 114: "Example 4" + "Example 5" (L5 sib=4, 5), page 115: "Example 6" (L5 sib=6), page 117: "Example 7" (L5 sib=7), page 119: "Example 8" (L5 sib=8).
- Atoms 7 (sib=7) and 9 (sib=8) correctly reflect continuous sibling numbering. No continuity break detected.
- "Subject ABC5001/ABC5002/ABC5003" on page 114 — all bold L5 sib=null. Atom 4 (Subject ABC5003) correctly has sib=null.

### OBS-12-06 — Page Boundary Attribution Risk (Extending F-12-01)
- Example 7 spans pages 117 (text description), 118 (CRF + ec.xpt), and 119 (ex.xpt + vs.xpt + relrec.xpt + Example 8 start). The transition from p.118 to p.119 mid-example creates a boundary condition where the ex.xpt table header lands on p.119 but its content might be attributed to p.118 by an atomizer.
- **Systematic risk**: If the writer agent atomized the ex.xpt table from the visual context of p.118 (where the ec.xpt discussion ends) without correctly tracking the page break, ALL ex.xpt atoms for Example 7 may be tagged page=118 instead of page=119.
- Recommended: Check all atoms with page=118 and atom_type in {TABLE_HEADER, TABLE_ROW} where DOMAIN=EX — if any are present, they are likely mis-attributed.

## Final Verdict

**CONDITIONAL_PASS** — Weighted PASS rate 85% (≥80%, <90%)

- 1 FAIL (HIGH): Page attribution error for ex.xpt table crossing p.118/p.119 boundary (F-12-01)
- 1 PARTIAL (LOW): R10 cell-wrap ambiguity for ECTRT "BOTTLE" vs "BOTTLE\n2" in Example 6 ec.xpt (F-12-02)
- 8 PASS: atom_type, verbatim, parent_section, heading dimensions all correct

**Blocking action required before batch 12 promotion**: Sweep all batch 12 atoms where page=118 and DOMAIN=EX; correct page attribution to 119. Also sweep Example 6 ec.xpt ECTRT values for cell-wrap completeness.
