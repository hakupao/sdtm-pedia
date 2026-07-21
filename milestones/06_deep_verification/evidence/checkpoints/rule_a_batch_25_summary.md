# Rule A Batch 25 Audit Summary (slot #34 feature-dev:code-architect, AUDIT-mode pivot 15th)

## Sample Parameters
- Sample size: n=10 atoms
- Pages: p.241–p.250
- Seed: 20260530
- Stratification: 4 TABLE_ROW + 3 HEADING + 2 LIST_ITEM + 1 CODE_LITERAL

## Per-Atom Verdict Table

| atom_id            | page | atom_type    | verdict | atom_type | verbatim | parent_section | heading_fields |
|--------------------|------|-------------|---------|-----------|----------|----------------|----------------|
| ig34_p0241_a023    | 241  | HEADING      | PASS    | PASS      | PASS     | PASS           | PASS           |
| ig34_p0242_a010    | 242  | TABLE_ROW    | PASS    | PASS      | PASS     | PASS           | N/A            |
| ig34_p0243_a009    | 243  | TABLE_ROW    | PASS    | PASS      | PASS     | PASS           | N/A            |
| ig34_p0244_a010    | 244  | TABLE_ROW    | PASS    | PASS      | PASS     | PASS           | N/A            |
| ig34_p0245_a012    | 245  | LIST_ITEM    | PASS    | PASS      | PASS     | PASS           | N/A            |
| ig34_p0246_a008    | 246  | LIST_ITEM    | PASS    | PASS      | PASS     | PASS           | N/A            |
| ig34_p0247_a019    | 247  | CODE_LITERAL | PASS    | PASS      | PASS     | PASS           | N/A            |
| ig34_p0248_a023    | 248  | HEADING      | PASS    | PASS      | PASS     | PASS           | PASS           |
| ig34_p0249_a001    | 249  | HEADING      | PASS    | PASS      | PASS     | PASS           | PASS           |
| ig34_p0250_a012    | 250  | TABLE_ROW    | PASS    | PASS      | PASS     | PASS           | N/A            |

## Weighted Score Breakdown

| Metric       | Count |
|--------------|-------|
| n_PASS       | 10    |
| n_PARTIAL    | 0     |
| n_FAIL       | 0     |
| weighted_pct | 100%  |

Score: (10 × 1.0 + 0 × 0.5 + 0 × 0.0) / 10 × 100 = **100.0%**
Threshold: ≥90% — **EXCEEDED**

## 4-Dimension Breakdown

| Dimension       | PASS | PARTIAL | FAIL | N/A |
|-----------------|------|---------|------|-----|
| atom_type       | 10   | 0       | 0    | 0   |
| verbatim        | 10   | 0       | 0    | 0   |
| parent_section  | 10   | 0       | 0    | 0   |
| heading_fields  | 3    | 0       | 0    | 7   |

(heading_fields N/A for 7 non-HEADING atoms; all 3 HEADING atoms PASS)

## Special Checks: NEW6.b + NEW Round-4 Deep-Nesting Precedent

### NEW6.b: L4 HEADING Self-Parent Prohibition

**§6.3.5.6 LB HEADING (ig34_p0241_a023, p.241):**
- Assigned parent_section: `§6.3.5 Specimen-based Findings Domains`
- Verdict: COMPLIANT — parent is the L3 group container, NOT self-parent (§6.3.5.6)
- NEW6.b check: PASS

**§6.3.5.7 Microbiology Domains HEADING (ig34_p0248_a023, p.248):**
- Assigned parent_section: `§6.3.5 Specimen-based Findings Domains`
- Verdict: COMPLIANT — parent is the L3 group container, NOT self-parent (§6.3.5.7)
- NEW6.b check: PASS

### NEW Round-4 Deep-Nesting Precedent: L5 MB HEADING Parent

The sample does NOT contain the §6.3.5.7.1 Microbiology Specimen (MB) L5 SECTION HEADING atom (which would be on p.248 and would require parent = `§6.3.5.7 Microbiology Domains`). The atom ig34_p0249_a001 is "MB – Specification" (L6 sub-heading within §6.3.5.7.1), whose parent = `§6.3.5.7.1 Microbiology Specimen (MB)` is correctly assigned and does NOT conflict with the NEW round-4 precedent (which targets the L5 section heading, not L6 sub-headings within the section).

Round-4 precedent application: NOT directly tested in this sample (L5 §6.3.5.7.1 HEADING not in sample); no precedent violation observed.

(Note from main session: §6.3.5.7.1 MB L5 HEADING atom is `ig34_p0248_a025` with parent_section=`§6.3.5.7 Microbiology Domains` per programmatic NEW6.b sweep — round-4 NEW deep-nesting precedent VERIFIED outside Rule A 1/page sample.)

## Findings

**No FAIL or PARTIAL findings.** All 10 atoms across all 4 dimensions verified PASS.

Notable observations (informational, not findings):
1. Both NEW6.b-critical HEADING atoms (§6.3.5.6 LB p.241 + §6.3.5.7 Microbiology Domains p.248) correctly use L3 group container as parent — no self-parent error.
2. The stratification of 4 TABLE_ROW atoms across 3 different PDF pages (242/243/244/250) spanning both LB and MB spec tables provides good coverage of verbatim column accuracy.
3. CODE_LITERAL "lb.xpt" (p.247) correctly placed within LB parent; consistent with prior batch precedents for dataset filename labels.
4. L6 heading "MB – Specification" (p.249) sib=2 consistent with L6 heading sequence: MB–Description/Overview (sib=1, p.248) → MB–Specification (sib=2, p.249).

## Final Verdict

**PASS_AT_THRESHOLD**

Weighted score: 100.0% — exceeds ≥90% threshold with 10 percentage points margin.
All 10 atoms PASS across all 4 audit dimensions.
Both NEW6.b L4 self-parent checks (§6.3.5.6 LB + §6.3.5.7 Microbiology Domains) confirmed COMPLIANT.
No verbatim character deviations, atom_type misclassifications, parent_section errors, or heading_fields errors detected.
