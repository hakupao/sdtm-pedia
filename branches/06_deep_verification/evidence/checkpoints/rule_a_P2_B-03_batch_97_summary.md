# Rule A Review — P2 B-03c batch_97 (RP/examples.md)

> **Reviewer**: independent subagent (general-purpose), Rule D isolation from writer
> **Round**: P2 B-03c round 09 (v1.9.2 baseline 3rd sustained round)
> **Source**: `knowledge_base/domains/RP/examples.md` (31 lines)
> **Writer output**: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_97_md_atoms.jsonl` (26 atoms)
> **Date**: 2026-05-07

## 1. Cross-verify (grep/wc evidence)

| Metric | Expected | Actual | Status |
|---|---|---|---|
| Source `wc -l` | 31 | 31 | PASS |
| Source `grep -c '^## '` | 1 | 1 | PASS (`## Example 1` at L3) |
| Source `grep -c '^### '` | 0 | 0 | PASS |
| Source `grep -c '^# '` | 1 | 1 | PASS (`# RP — Examples` at L1) |
| Atom count | 26 | 26 | PASS |
| atom_id sequence | a001-a026 contiguous | a001-a026 contiguous | PASS |

**Atom composition** (writer output structural breakdown):
- 1 × HEADING (hl=1) → a001 (L1 `# RP — Examples`)
- 1 × HEADING (hl=2) → a002 (L3 `## Example 1`)
- 2 × SENTENCE → a003 (L5 narrative), a004 (L7 `**rp.xpt**`)
- 1 × TABLE_HEADER → a005 (L9-10, 2-row span)
- 21 × TABLE_ROW → a006-a026 (L11-L31, 21 data rows for 2 subjects: P0001 rows 1-11 + P0002 rows 12-21)
- **Total = 26 ✓**

## 2. Sample roster (8 boundary + 3 stratified = 11)

| # | atom_id | line | type | role |
|---|---|---|---|---|
| 1 | a001 | L1 | HEADING hl=1 | boundary: H1 first line |
| 2 | a002 | L3 | HEADING hl=2 | boundary: H2 numbered (§2.5 trigger) |
| 3 | a003 | L5 | SENTENCE | boundary: first content right after H2 |
| 4 | a005 | L9-10 | TABLE_HEADER | boundary: 2-row span Hook A1 |
| 5 | a006 | L11 | TABLE_ROW | boundary: first TABLE_ROW |
| 6 | a015 | L20 | TABLE_ROW | boundary: random mid-table (subject P0001 row 10) |
| 7 | a020 | L25 | TABLE_ROW | boundary: random mid-table (subject P0002 row 15) |
| 8 | a026 | L31 | TABLE_ROW | boundary: last TABLE_ROW |
| 9 | a004 | L7 | SENTENCE | stratified: bold-marker SENTENCE |
| 10 | a013 | L18 | TABLE_ROW | stratified: visit transition row |
| 11 | a022 | L27 | TABLE_ROW | stratified: TABLE_ROW (replaces TABLE_HEADER stratified slot — only 1 TABLE_HEADER exists in source) |

> **Note on stratified plan**: prompt suggested "1 TABLE_HEADER (already in boundary, replace with another)" — source only contains 1 TABLE_HEADER, so the slot was reassigned to an additional TABLE_ROW (a022) per prompt's "replace" intent.

## 3. Per-check matrix

| Check | Rule | Pass | Fail | Notes |
|---|---|---|---|---|
| Schema 12/12 fields exact | §E-1 baseline | 11/11 | 0 | All atoms carry exactly the 12 required fields |
| §E-1 schema regression sweep | hl/sib/figure_ref/cross_refs explicit | 11/11 | 0 | All non-HEADING explicit `null` literals present |
| §E-2 H1 hl=1 sib=1 | a001 | 1/1 | 0 | a001: hl=1 sib=1 ✓ |
| §E-3 TABLE_HEADER sib=null | a005 | 1/1 | 0 | a005 sib=null ✓ |
| §E-4 extracted_by object form | all | 11/11 | 0 | Object with subagent_type/prompt_version/ts |
| §E-5 non-HEADING hl=null sib=null | a003-a026 | 9/9 | 0 | Sampled non-HEADING atoms all explicit null |
| Verbatim byte-exact | source diff | 11/11 | 0 | All sampled verbatim strings match source byte-by-byte |
| §2.5 numbered H2 self-namespace | parent_section routing | 11/11 | 0 | a001+a002 parent=§RP[RP — Examples]; a003-a026 parent=§RP.1[Example 1] ✓ |
| Hook A1 TABLE_HEADER 2-row span | line_end-line_start=1 | 1/1 | 0 | a005 L9-10 (delta=1) ✓ |
| atom_id sequence contiguous | a001-a026 | 1/1 | 0 | No gaps, no duplicates |

**Sampled pass rate: 11/11 = 100%**

## 4. §2.5 sub-namespace deep-check (CRITICAL)

The §2.5 rule for v1.9.2 baseline: numbered H2 sections create sub-namespace where children's `parent_section` = `§RP.1 [Example 1]`, while the H2 atom itself parents to its grandparent `§RP [RP — Examples]`.

| atom | line | parent_section | expected | verdict |
|---|---|---|---|---|
| a001 (H1) | L1 | `§RP [RP — Examples]` | `§RP [RP — Examples]` | PASS |
| a002 (H2 numbered) | L3 | `§RP [RP — Examples]` | `§RP [RP — Examples]` (H2 self-parent) | PASS |
| a003-a026 (descendants) | L5-L31 | `§RP.1 [Example 1]` | `§RP.1 [Example 1]` (sub-namespace) | PASS (24/24) |

Spot-checked all 26 atoms — boundary at L3→L5 transition correctly flips from `§RP [RP — Examples]` to `§RP.1 [Example 1]`. **Zero §2.5 violations.**

## 5. Findings

**No findings.** All 11 sampled atoms PASS all 10 checks. Cross-verification (grep/wc) matches structural expectations. §2.5 sub-namespace boundary correctly applied. Hook A1 2-row TABLE_HEADER span correct. Verbatim byte-exact across all sampled atoms.

## 6. Halt evaluation

| Halt trigger | Condition | Triggered? |
|---|---|---|
| §E-1 regression | any schema field missing/wrong | NO |
| Verbatim mismatch | byte diff vs source | NO |
| §2.5 sub-namespace error | wrong parent_section assignment | NO |
| TABLE_HEADER sib≠null | a005 violation | NO |
| Pass rate <90% | sample PASS / 11 < 0.9 | NO (100%) |

**No halt. No findings.**

---

RULE_A_BATCH_97: PASS raw=11/11 pct=100% halt=no
