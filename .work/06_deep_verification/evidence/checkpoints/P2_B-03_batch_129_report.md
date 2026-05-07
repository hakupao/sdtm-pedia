# P2 B-03c Batch 129 Writer Report — TI/examples.md

> Round: 12 (B-03c)
> Source: `knowledge_base/domains/TI/examples.md` (20L, 1 numbered H2 §2.5)
> Atom prefix: `md_dmTI_ex_a`
> Prompt version: `P0_writer_md_v1.9.3`
> Subagent: `general-purpose`
> Timestamp: 2026-05-07T15:00:00Z

## Source structure (grep-verified)

- 20 lines total (`wc -l`)
- 1 H1 (L1 `# TI — Examples`)
- 1 H2 numbered (L3 `## Example 1`) — §2.5 lock
- 0 H3 / 0 H4
- 0 mermaid blocks
- 1 markdown table (L13-20: header L13 + sep L14 + 6 rows L15-20)
- 1 bold standalone label `**ti.xpt**` (L11) — Hook D-NOTE-BQ → SENTENCE per MB/ex precedent

## Atom counts

- **Total: 13** (within [4, 18] band)
- Type distribution:
  - HEADING: 2 (H1 + H2)
  - SENTENCE: 4 (3 narrative + 1 `**ti.xpt**` bold label)
  - TABLE_HEADER: 1 (header + sep, line_start=13/line_end=14)
  - TABLE_ROW: 6 (rows 1-6)
- Range: `md_dmTI_ex_a001` .. `md_dmTI_ex_a013`
- Atoms/line ratio: 13/20 = **0.650** (within §F-2 empirical band 0.59-0.85)

## Parent_section assignment

- `§TI [TI — Examples]` (file-root): a001 (H1), a002 (H2 numbered §2.5)
- `§TI.1 [Example 1]`: a003-a013 (intro narrative + bold label + table)

## Hooks self-validate (v1.9.3)

| Hook | Status | Evidence |
|---|---|---|
| §E-1 dispatch JSON template | PASS | extracted_by complete on all 13 atoms |
| §E-2 R-2.8-1 H1 sib_idx=1 universal | PASS | a001 H1 sib_idx=1 |
| §E-3 R-2.8-2 TABLE_HEADER sib_idx=null | PASS | a007 sib_idx=null |
| §E-4 R-2.8-3 extracted_by object | PASS | subagent_type+prompt_version+ts all present |
| §E-5 MED-01 non-HEADING field-explicit-null | PASS | 11/11 non-HEADING atoms have heading_level=null AND sibling_index=null |
| §2.5 numbered H2 sib_idx=1 | PASS | a002 `## Example 1` sib_idx=1 (file-root parent) |
| §2.9 LIST_ITEM null | N/A | 0 LIST_ITEM in batch |
| Hook D-NOTE-BQ | PASS | a006 `**ti.xpt**` SENTENCE (MB/ex L20 `**relrec.xpt**` precedent) |
| §F-1 §2.11 Plan B trigger | NOT TRIGGERED | 0 H3 children in only numberless-relevant scope; H2 is numbered (`Example 1`) → §2.5 lock, not §F-1 |
| §F-2 atoms/line ratio | PASS | 0.650 within band 0.59-0.85 |

**Schema sweep**: PASS 12/12 (8 required fields × all atoms + HEADING heading_level/sibling_index conditional + non-HEADING explicit-null + extracted_by sub-fields).

## Output files

1. Append: `.work/06_deep_verification/md_atoms.jsonl` (9880 → 9893 lines, +13)
2. Backup: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_129_md_atoms.jsonl` (13 lines)
3. Report: this file

## Failures / repair cycles

- Failures: 0
- Repair cycles: 0
- Halts: 0

## DONE

`PARALLEL_SESSION_129_DONE atoms=13 failures=0 repair_cycles=0 schema_sweep=PASS_12_12 hooks=PASS_v1.9.3 atom_id_range=md_dmTI_ex_a001..a013`
