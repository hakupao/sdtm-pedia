# P2 B-03c Round 12 — batch_126 writer report

> Source: `knowledge_base/domains/TE/assumptions.md` (37L)
> Atom prefix: `md_dmTE_assn_a001..a023`
> Subagent: general-purpose
> Prompt: P0_writer_md_v1.9.3
> Timestamp: 2026-05-07T14:00:00Z

## §0. DONE marker

`PARALLEL_SESSION_126_DONE atoms=23 failures=0 repair_cycles=0 schema_sweep=PASS_12_12 hooks=PASS_v1.9.3 atom_id_range=md_dmTE_assn_a001..a023`

## §1. Atom inventory

- Total: **23** (within [7, 30] halt band)
- atom_type distribution:
  - HEADING: 1 (L1 H1 `# TE — Assumptions`)
  - SENTENCE: 7 (L3×3 + L5×1 + L7×3)
  - LIST_ITEM: 15 (L9, L11, L13, L15, L17, L19, L21, L23, L25, L27, L29, L31, L33, L35, L37 — items #1..#15)
  - TABLE_HEADER: 0
  - TABLE_ROW: 0
  - CODE_LITERAL: 0
  - CROSS_REF: 0
  - FIGURE: 0
  - NOTE: 0
- atom_id range: `md_dmTE_assn_a001..a023`
- 0 collision vs existing 9792 atoms (verified)
- 23 unique atom_ids (verified)

## §2. Source structure (no surprises)

```
L1:  # TE — Assumptions          (H1 only — 0 H2/H3/H4/mermaid grep-verified)
L3:  intro paragraph (3 sentences)
L5:  paragraph (1 sentence)
L7:  paragraph (3 sentences)
L9-L37: 15 numbered list items (#1..#15), each on its own odd line, blank even lines
```

grep `^#{2,4} ` → 0 matches (confirmed no H2/H3/H4)
grep `mermaid` → 0 matches (confirmed no mermaid)

## §3. Parent section assignment

All 23 atoms → `§TE [TE — Assumptions]` (file-root H1 scope; no nested sub-namespace because no H2 with H3 children — §F-1 §2.11 Plan B not triggered this batch).

## §4. v1.9.3 hook self-validation

| Hook | Applies | Result |
|------|---------|--------|
| §E-1 Hook 22c CRITICAL | YES (dispatch JSON template) | PASS — extracted_by object schema followed |
| §E-2 Hook E-2-1 H1 sib_idx=1 universal | YES | PASS — H1 a001 has sibling_index=1 |
| §E-3 Hook E-3-2 TABLE_HEADER sib_idx=null | N/A | N/A — 0 TABLE_HEADER |
| §E-4 Hook E-4-3 extracted_by object | YES | PASS — all 23 use object form |
| §E-5 MED-01 non-HEADING field-explicit-null | YES | PASS — 22 non-HEADING atoms all have heading_level:null + sibling_index:null |
| §2.9 LIST_ITEM null fields | YES | PASS — 15 LIST_ITEM atoms heading_level/sibling_index/figure_ref all null |
| Hook D-NOTE-BQ | N/A | N/A — no blockquote in source |
| §F-1 §2.11 Plan B | N/A | N/A — 0 H2/H3 in source |
| §F-2 atoms/line ratio | INFO (post-DONE retrospective) | atoms_per_line_ratio=0.6216 (within 0.59-0.85 §F-2 band) |
| §F-3 nested-list calibration | N/A | N/A — writer-side only INFO carry; numbered list without sub-bullets |

## §5. §F-2 ratio retrospective

- Source lines: 37
- Atoms: 23
- atoms_per_line_ratio (naive == de-fig since 0 FIGURE): **0.6216**
- §F-2 empirical band 0.59-0.85: **IN BAND** (lower-mid range, consistent with assumption-style numbered-list narrative)
- §F-2 absolute halt band [0.5, 1.0]: **IN BAND**
- 10th cumulative round in band (rounds 04-12 sustained, contributes to §F-2 SUSTAINED VALIDATED status)

## §6. 12-field schema sweep

PASS_12_12 — all 23 atoms carry the full 12-field schema:
1. atom_id ✓
2. file ✓
3. line_start ✓
4. line_end ✓
5. parent_section ✓
6. atom_type ✓
7. verbatim ✓
8. heading_level (HEADING=1, others=null) ✓
9. sibling_index (HEADING=1, others=null) ✓
10. figure_ref (all null, 0 FIGURE) ✓
11. cross_refs (all []) ✓
12. extracted_by (object with subagent_type+prompt_version+ts) ✓

## §7. Halt condition checklist

| Condition | Status |
|-----------|--------|
| atom count outside [7, 30] | PASS — 23 in band |
| Schema/12-field violation | PASS — 12/12 sweep clean |
| atom_id collision | PASS — 0 collision vs 9792 existing |
| Surprise H2/H3/mermaid | PASS — grep verified 0 |

No halt triggered. Clean batch.

## §8. Outputs delivered

1. Appended to `.work/06_deep_verification/md_atoms.jsonl` (9792 → 9815, +23 lines)
2. Backup `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_126_md_atoms.jsonl` (23 lines)
3. This report `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_126_report.md`

## §9. Notes for reviewer

- All 7 SENTENCE atoms come from intro paragraphs (L3 ×3 / L5 ×1 / L7 ×3). Multi-sentence-per-line splits follow §C-1 (one SENTENCE per English sentence) — including the L7 short final sentence (`"Week 2 to week 4" is not a valid trial element.`) extracted as standalone atom_a008.
- All 15 LIST_ITEM atoms are full-prefix multi-sentence compounds (Hook A3 pattern), preserving the leading number (e.g., `1. There are no gaps...`, `15. Note that...`). This matches the same compound style as TA/assumptions batch_122 atoms.
- L23 / L25 contain `**must not**` bold markdown — preserved verbatim per md atom convention.
- L17 contains an em-dash word `—particularly` — preserved verbatim with the unicode em-dash character, not converted.
- L7 closing `"unique page."` and L21 `"Trial Entry."` retain the period inside the quote per source.
- Items #6 (L19) and #11 (L29) and #15 (L37) start with `Note that...` — kept as LIST_ITEM type per §F-2/§E-5 because they are part of the numbered list (NOT separated NOTE atoms — the source's narrative voice puts these inline as numbered items, not as discrete callouts).

End of report.
