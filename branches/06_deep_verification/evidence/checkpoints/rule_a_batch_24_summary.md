# Rule A Audit — Batch 24 Summary
**Reviewer slot**: #33 `oh-my-claudecode:scientist` (omc 7th burn, 14th AUDIT pivot)
**Pages audited**: p.231–240 (IS domain §6.3.5.5, IS-Assumptions + IS-Examples)
**Audit date**: 2026-04-26
**Sample file**: `rule_a_batch_24_sample.jsonl`
**Prompt version**: P0_writer_pdf_v1.2 (+ optionE_rerun suffix for p.236–240 atoms)

---

## Summary Statistics

| Verdict | Count | Weight |
|---------|-------|--------|
| PASS    | 9     | 9.0    |
| PARTIAL | 0     | 0.0    |
| FAIL    | 1     | 0.0    |
| **Total** | **10** | **9.0** |

**Weighted% = 9.0 / 10 × 100 = 90.0%**

Threshold: ≥90%. **Status: AT THRESHOLD (90.0% — borderline PASS)**

---

## Per-Atom Results

| atom_id | page | atom_type | verdict | dim:type | dim:verbatim | dim:parent | dim:heading |
|---------|------|-----------|---------|----------|--------------|------------|-------------|
| ig34_p0231_a017 | 231 | HEADING | PASS | OK | OK | OK | OK |
| ig34_p0232_a001 | 232 | LIST_ITEM | PASS | OK | OK | OK | N/A |
| ig34_p0233_a002 | 233 | HEADING | PASS | OK | OK | OK | OK |
| ig34_p0234_a022 | 234 | TABLE_ROW | PASS | OK | OK | OK | N/A |
| ig34_p0235_a001 | 235 | TABLE_ROW | PASS | OK | OK | OK | N/A |
| ig34_p0236_a014 | 236 | TABLE_ROW | PASS | OK | OK | OK | N/A |
| ig34_p0237_a012 | 237 | TABLE_ROW | PASS | OK | OK | OK | N/A |
| ig34_p0238_a004 | 238 | TABLE_HEADER | **FAIL** | OK | **MAJOR** | OK | N/A |
| ig34_p0239_a003 | 239 | TABLE_ROW | PASS | OK | OK | OK | N/A |
| ig34_p0240_a001 | 240 | HEADING | PASS | OK | OK | OK | OK |

---

## FAIL / PARTIAL Detail

### FAIL: ig34_p0238_a004 (p.238, TABLE_HEADER)

**Dimension failed**: verbatim (MAJOR — R10 strict)

**Finding**: The TABLE_HEADER atom for the Example 7 table (cytokine-secreting cells, ELISPOT assay) on p.238 is missing the `NHOID` column. The PDF ground truth header reads:

```
| Row | STUDYID | DOMAIN | USUBJID | NHOID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISMSCBCE | ISTSTCND | ISCNDAGT | ISCAT | ISSCAT | ISORRES | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
```

The atom verbatim reads:
```
| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISMSCBCE | ISTSTCND | ISCNDAGT | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
```

Two discrepancies:
1. **NHOID absent**: Column `NHOID` (Non-host Organism Identifier, position 5 in PDF) is completely missing from atom verbatim.
2. **ISORRESU spurious**: Atom includes `ISORRESU` (between ISORRES and ISSTRESC) which is NOT present in the PDF Example 7 table header. Example 7 uses ISMSCBCE/ISTSTCND/ISCNDAGT columns instead of the ADA-test column layout.

These two errors partially compensate each other numerically (both 23-column count) but represent distinct column-identity failures. The Option-E rerun on this batch did NOT repair this specific atom (ig34_p0238_a004, which has standard `P0_writer_pdf_v1.2_optionE_rerun` suffix but the error persists).

**Impact**: TABLE_HEADER errors propagate to downstream matcher — if NHOID is absent from header, column-to-field mapping for the Example 7 dataset will be off for all rows referencing this header.

**Recommendation**: Targeted Option-E rerun on p.238 specifically for atom a004 (TABLE_HEADER). The corresponding TABLE_ROW atoms for Example 7 (p.237 rows) should be checked separately for NHOID inclusion — atom ig34_p0237_a012 on p.237 correctly omits NHOID from the Example 6 table (different example, no NHOID). The p.238 Example 7 TABLE_ROW atoms (not sampled here) may also be affected.

---

## Cross-Batch Sibling Continuity Verification (IS L5/L6 Chain)

Per spec (G-MS-11.b + NEW7):

| Heading | Expected L/sib | Atom claimed | Status |
|---------|---------------|--------------|--------|
| IS – Assumptions | L5 sib=3 | L5 sib=3 (ig34_p0231_a017) | MATCH |
| IS – Examples | L5 sib=4 | (not in sample, carried from batch 23) | N/A |
| Example 1 | L6 sib=1 | L6 sib=1 (ig34_p0233_a002) | MATCH |
| Example 10 | L6 sib=10 | L6 sib=10 (ig34_p0240_a001) | MATCH |

The L5→L6 chain is intact for sampled atoms. IS-Assumptions (L5 sib=3) correctly precedes IS-Examples section. Example 1 and Example 10 sibling indices are consistent with a monotonically incrementing series from 1 to (at least) 10. No sibling inversion or gap detected in sampled atoms.

**IS-Examples heading (L5 sib=4)**: Not in this sample but was in batch 23. The IS-Examples heading appears on p.233 ("IS – Examples"), and batch 24 opens on p.231 mid-IS-Assumptions section. The handoff from batch 23 is structurally correct per p.231 content (still IS-Assumptions).

---

## NEW6 Parent Section Consistency Check

All 10 atoms claim `parent_section = "§6.3.5.5 Immunogenicity Specimen Assessments (IS)"`.

PDF verification: Pages 231–240 are entirely within §6.3.5.5 IS domain — no chapter or sub-domain transitions. The IS-Examples section (starting p.233) and all 10+ examples through p.240 remain under §6.3.5.5.

**Result**: NEW6 parent_section consistency = CLEAN (10/10 atoms correct).

---

## NEW8 Variable Name Char-Drift Survey

Post-Option-E rerun atoms (p.236–240 suffix `_optionE_rerun`) surveyed for variable name character drift:

| Variable | Atom spelling | PDF spelling | Status |
|----------|--------------|--------------|--------|
| MBIGGAB | MBIGGAB | MBIGGAB | OK |
| MBNAB | MBNAB | MBNAB | OK |
| ABSCCL | ABSCCL | ABSCCL | OK |
| ISMSCBCE | ISMSCBCE | ISMSCBCE | OK |
| ISTSTCND | ISTSTCND | ISTSTCND | OK |
| ISCNDAGT | ISCNDAGT | ISCNDAGT | OK |
| NHOID | (absent in ig34_p0238_a004 header) | NHOID | MISSING (FAIL case) |
| ADA_BAB | ADA_BAB | ADA_BAB | OK |
| ELECTROCHEMILUMINESCENCE IMMUNOASSAY | exact | exact | OK |
| MICRONEUTRALIZATION ASSAY | exact | exact | OK |

**Result**: No character-swap or adjacent-letter drift detected in any variable name. The only issue is structural (column omission), not character-level drift. NEW8 n-gram cross-check: clean for all sampled variable names.

---

## Overall Assessment

- **Weighted score**: 90.0% (AT THRESHOLD — meets ≥90% requirement exactly)
- **FAIL count**: 1 (ig34_p0238_a004 TABLE_HEADER, NHOID column missing + spurious ISORRESU)
- **Root cause**: Option-E rerun on p.238 did not fix the TABLE_HEADER atom. The writer appears to have correctly captured the Example 7 row data but misidentified the column schema for this specific example's header.
- **Action required**: Targeted repair of ig34_p0238_a004. Verify corresponding Example 7 TABLE_ROW atoms (not in sample) for NHOID field presence. Consider whether p.237 also contains Example 7 table rows that need NHOID.
- **All other dimensions**: atom_type (10/10), parent_section (10/10), heading_fields (3/3 HEADING atoms) all CLEAN.
