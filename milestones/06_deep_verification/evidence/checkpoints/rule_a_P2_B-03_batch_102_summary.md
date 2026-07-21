# Rule A Audit — P2 B-03c batch_102 (round 09)

**Source**: `knowledge_base/domains/SE/assumptions.md` (30 lines)
**Writer output**: `P2_B-03_batch_102_md_atoms.jsonl` (17 atoms)
**Baseline**: v1.9.2 (3rd sustained round)
**Parent variant**: 0 H2 file → file-root parent (`§SE [SE — Assumptions]`) for all atoms

## Source structure cross-verification (grep)

| Metric | Expected | Actual | Status |
|--------|----------|--------|--------|
| `wc -l` | 30 | 30 | ✓ |
| `^# ` (H1) | 1 | 1 | ✓ |
| `^## ` (H2) | 0 | 0 | ✓ |
| `^### ` (H3) | 0 | 0 | ✓ |
| L28/L29/L30 leading indent | 4-space | 4-space (verified `[____a...] [____b...] [____c...]`) | ✓ |

## Sampling (8 boundary + 3 stratified = 11)

| atom_id | line | class | atom_type |
|---------|------|-------|-----------|
| a001 | L1 | boundary H1 | HEADING |
| a002 | L3 | stratified SENTENCE | SENTENCE |
| a004 | L7 | boundary mid LIST_ITEM | LIST_ITEM |
| a005 | L9 | stratified LIST_ITEM | LIST_ITEM |
| a008 | L15 | boundary mid LIST_ITEM | LIST_ITEM |
| a010 | L19 | boundary mid LIST_ITEM | LIST_ITEM |
| a012 | L23 | stratified LIST_ITEM | LIST_ITEM |
| a013 | L25 | stratified LIST_ITEM | LIST_ITEM |
| a015 | L28 | boundary sub-bullet a | LIST_ITEM |
| a016 | L29 | boundary sub-bullet b | LIST_ITEM |
| a017 | L30 | boundary sub-bullet c (last) | LIST_ITEM |

## Per-atom checks

All 11 sampled atoms passed every check:

1. **Schema 12/12 fields EXACT**: all 17 atoms have keys `[atom_id, atom_type, cross_refs, extracted_by, figure_ref, file, heading_level, line_end, line_start, parent_section, sibling_index, verbatim]` — verified by full-file scan, not just sample
2. **§E-1 schema regression sweep**: PASS (no extra/missing keys; all expected types)
3. **§E-2 H1 hl=1 sib=1**: PASS (a001 has `heading_level=1, sibling_index=1`)
4. **§E-3 N/A**: no H2 in this file
5. **§E-4 extracted_by object**: PASS (all 17 atoms have object `{subagent_type, prompt_version, ts}`, not stringified)
6. **§E-5 non-HEADING explicit hl=null sib=null literal**: PASS (verified for all 16 non-HEADING atoms)
7. **Verbatim byte-exact**: PASS for all 11 sampled atoms — including critical 4-space leading indent on sub-bullets a/b/c (L28-L30) which is the highest-risk regression vector for this batch
8. **parent_section uniformity**: PASS — all 17 atoms = `§SE [SE — Assumptions]` (file-root, no H2 ancestry)
9. **atom_type discipline**: a001=HEADING, a002=SENTENCE, a003=SENTENCE, a004-a017=LIST_ITEM — matches source markdown structure
10. **atom_id sequence contiguous**: a001..a017 (no gaps, no duplicates)

## Key observations

- **Sub-bullet indent fidelity**: The three sub-bullets at L28/L29/L30 each carry exactly 4 leading space characters; the writer preserved this byte-exact in `verbatim` for a015/a016/a017. This is the highest-risk vector for §E-1 / verbatim regression on this file shape and it passed cleanly.
- **Literal `--` token preservation**: SDTM convention placeholders (`--SEQ`, `--STDTC`, `--GRPID`, `--REFID`, `--SPID`, `--DTC`, `--DY`, `--DUR`, `--TPT`, `--TPTNUM`, `--ELTM`, `--TPTREF`, `--RFTDTC`) all preserved as literal double-dash in verbatim, no markdown em-dash transformation.
- **Em-dash in title**: `# SE — Assumptions` uses U+2014 em-dash; preserved byte-exact in a001 verbatim.
- **No SENTENCE/LIST_ITEM mistype**: numbered items 1-11 correctly typed as LIST_ITEM (a004-a014); sub-bullets a/b/c correctly typed as LIST_ITEM (a015-a017); paragraph-level prose correctly typed as SENTENCE (a002-a003).

## Sample audit ratio

- Raw: 11/11 PASS = **100%**
- Halt triggers (§E-1 regression, verbatim sub-bullet indent loss): **none triggered**

## Verdict

```
RULE_A_BATCH_102: PASS raw=11/11 pct=100% halt=no
```
