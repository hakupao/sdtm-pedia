# P6 T5 — Non-Prose Ledger Update Report

**Date**: 2026-05-12T08:17:42Z
**Script**: scripts/p6_t5_update_nonprose.py
**Backup**: coverage_ledger.jsonl.p6_t5_pre.bak

---

## Update Summary

| Action | Count |
|--------|-------|
| HEADING → EQUIVALENT (found in KB) | 61 |
| HEADING → INTENTIONAL_EXCLUDE (structural) | 15 |
| CROSS_REF → INTENTIONAL_EXCLUDE | 9 |
| TABLE_ROW/TABLE_HEADER/CODE_LITERAL → EQUIVALENT | 210 |
| FIGURE skipped (deferred) | 9 |
| Total EQUIVALENT added | 271 |
| Total INTENTIONAL_EXCLUDE added | 24 |
| Total atoms updated | 295 |

## Post-Update Coverage Statistics

| Metric | Value |
|--------|-------|
| Total PDF atoms | 12487 |
| INTENTIONAL_EXCLUDE | 2087 |
| Adjusted denominator | 10400 |
| Covered (EXACT+EQUIV+PARTIAL+MISPLACED) | 10298 |
| MISSING | 9 |
| ERROR | 93 |
| **Coverage rate** | **99.02%** |
| 99% gate MISSING+ERROR target | ≤ 120 |
| Current MISSING+ERROR | 102 |
| **Gate G1** | PASS ✅ |

## Verdict Distribution

| Verdict | Count |
|---------|-------|
| EQUIVALENT | 4235 |
| EXACT | 3748 |
| INTENTIONAL_EXCLUDE | 2087 |
| PARTIAL | 2039 |
| MISPLACED | 276 |
| ERROR | 93 |
| MISSING | 9 |

## Remaining MISSING (9 atoms)

All remaining MISSING are FIGURE atoms (GF dataset tables + TA trial design
diagrams) — deferred for manual review.

| Atom ID | Section |
|---------|---------|
| `ig34_p0225_a004` | §6.3.5.4 Genomics Findings (GF) |
| `ig34_p0225_a017` | §6.3.5.4 Genomics Findings (GF) |
| `ig34_p0387_a011` | §7.2.1 Trial Arms (TA) – Example 1 |
| `ig34_p0388_a001` | §7.2.1 Trial Arms (TA) – Example 1 |
| `ig34_p0388_a003` | §7.2.1 Trial Arms (TA) – Example 1 |
| `ig34_p0388_a005` | §7.2.1 Trial Arms (TA) – Example 1 |
| `ig34_p0397_a005` | §7.2.1 Trial Arms (TA) – Example 5 |
| `ig34_p0398_a012` | §7.2.1 Trial Arms (TA) – Example 6 |
| `ig34_p0409_a007` | §7.3.1 Trial Visits (TV) – Example 1 |

## New IE Entries (24 atoms)

### Structural Chapter Headings (15)

| Atom ID | Reason |
|---------|--------|
| `ig34_p0256_a009` | Section heading for MB examples sub-section; content distributed across MB/examp |
| `ig34_p0285_a006` | High-level chapter grouping heading §6.3.7; no direct KB file (domains covered i |
| `ig34_p0353_a005` | Section heading for TR/TU examples; content in domain examples files |
| `ig34_p0361_a012` | §6.4.1 chapter-level intro heading; FA/SR domain files cover the content |
| `ig34_p0363_a010` | §6.4.2 chapter-level naming heading; FA/SR domain files cover the content |
| `ig34_p0364_a010` | §6.4.3 chapter-level variables heading; FA/SR domain files cover the content |
| `ig34_p0375_a024` | §6.4.5 SR section heading; SR domain content in SR/assumptions.md |
| `ig34_p0382_a002` | §7.1 Trial Design Model intro heading; content split across TA/TE/TV/TD/TM/TI/TS |
| `ig34_p0382_a003` | §7.1.1 Purpose heading; introductory content in TA/assumptions.md preamble |
| `ig34_p0382_a015` | §7.1.2 Definitions heading; definitions distributed across trial design domain f |
| `ig34_p0384_a015` | §7.2 Experimental Design grouping heading; content in TA and TE domain files |
| `ig34_p0407_a010` | §7.3 Schedule for Assessments grouping heading; content in TV/TD/TM domain files |
| `ig34_p0415_a025` | §7.4 Trial Eligibility grouping heading; content in TI and TS domain files |
| `ig34_p0416_a002` | TI Proposed Removal sub-heading; content covered under TI/assumptions.md PE-alig |
| `ig34_p0425_a026` | §7.5 How to Model heading; content in TI/assumptions.md steps 1-12 |

### Cross-Reference Navigation (9)

All 9 CROSS_REF atoms: "See Section X" navigation pointers — not substantive content.

| Atom ID |
|---------|
| `ig34_p0012_a002` |
| `ig34_p0012_a023` |
| `ig34_p0037_a003` |
| `ig34_p0042_a016` |
| `ig34_p0043_a007` |
| `ig34_p0055_a004` |
| `ig34_p0275_a014` |
| `ig34_p0275_a015` |
| `ig34_p0275_a023` |
