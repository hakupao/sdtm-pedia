# Rule A Audit Summary — P2 B-03c batch_100

## Scope

- **Batch**: P2 B-03c round 09 batch_100 (v1.9.2 baseline 3rd round)
- **Source**: `knowledge_base/domains/SC/assumptions.md` (7 lines)
- **Writer output**: `P2_B-03_batch_100_md_atoms.jsonl` (4 atoms)
- **Audit method**: FULL audit (all 4 atoms — small batch, no stratified sampling)

## Source structural facts (grep-verified)

| Metric | Value |
|--------|-------|
| Total lines (`wc -l`) | 7 |
| H1 count (`grep -c '^# '`) | 1 |
| H2 count (`grep -c '^## '`) | 0 |
| H3 count (`grep -c '^### '`) | 0 |

Confirmed: file-root scope, no H2 sub-sections. All 4 atoms share `parent_section = "§SC [SC — Assumptions]"`.

## Per-atom verdicts

| atom_id | line | atom_type | hl/sib | verdict |
|---------|------|-----------|--------|---------|
| md_dmSC_assn_a001 | 1 | HEADING | 1/1 | PASS |
| md_dmSC_assn_a002 | 3 | LIST_ITEM | null/null | PASS |
| md_dmSC_assn_a003 | 5 | LIST_ITEM | null/null | PASS |
| md_dmSC_assn_a004 | 7 | LIST_ITEM | null/null | PASS |

## Per-check matrix

| Check | a001 | a002 | a003 | a004 |
|-------|------|------|------|------|
| 1. Schema 12/12 fields | PASS | PASS | PASS | PASS |
| 2. §E-1 regression sweep | PASS | PASS | PASS | PASS |
| 3. §E-2 H1 hl=1 sib=1 | PASS | NA | NA | NA |
| 4. §E-3 | NA | NA | NA | NA |
| 5. §E-4 extracted_by object | PASS | PASS | PASS | PASS |
| 6. §E-5 non-HEADING null literal | NA | PASS | PASS | PASS |
| 7. Verbatim byte-exact | PASS | PASS | PASS | PASS |
| 8. parent_section §SC [SC — Assumptions] | PASS | PASS | PASS | PASS |
| 9. atom_type correct | PASS | PASS | PASS | PASS |
| 10. atom_id sequence a001-a004 contiguous | PASS | PASS | PASS | PASS |

## Notable observations

- a004 contains 22 SDTM dashed qualifiers (`--MODIFY` through `--SEV`); all hyphens preserved verbatim.
- a003 URL `https://www.cdisc.org/standards/terminology/controlled-terminology` preserved without truncation.
- a002 em-dash in heading title (`SC — Assumptions`, U+2014) byte-exact.
- All non-HEADING atoms use explicit `"heading_level":null,"sibling_index":null` per §E-5 (no field omission).
- `extracted_by` is object form with subagent_type / prompt_version `P0_writer_md_v1.9.2` / ts (§E-4 compliant).

## Aggregate

- raw: 4/4 PASS
- pct: 100%
- halt: no

RULE_A_BATCH_100: PASS raw=4/4 pct=100% halt=no
