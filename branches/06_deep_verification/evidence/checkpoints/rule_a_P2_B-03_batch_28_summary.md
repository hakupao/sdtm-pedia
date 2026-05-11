# Rule A Audit Summary — P2 B-03c round 02 batch_28

> Reviewer: pr-review-toolkit:code-reviewer (Rule D distinct from writer general-purpose ✓)
> Source: `knowledge_base/domains/CV/examples.md` (32 lines)
> Atoms: 22 (3 HEADING + 4 SENTENCE + 2 TABLE_HEADER + 13 TABLE_ROW)
> Sampling: 8 boundary + 3 stratified = 11 verdicts
> Date: 2026-05-06

## Count

- **Atoms produced**: 22
- **Sampled**: 11 (boundary 8 = a001/a002/a003/a004/a005/a011/a014/a022; stratified 3 = a008/a012/a018)
- **Sample-size compliance**: 22 ∈ [11, 44] ✓ (per v1.9.1 §R-Stratified-Sampling per-batch 11-16 verdict rows)
- **Audit ratio**: 11/22 = 50%

## PASS rate

- **Strict PASS**: 11/11 = **100%**
- **HIGH findings**: 0
- **MEDIUM findings**: 0
- **LOW findings**: 0

## Findings

### Boundary atoms (8 sampled)

| atom_id | sample_class | verdict | key check |
|---|---|---|---|
| a001 | boundary (H1 file head) | PASS | em-dash UTF-8 e2 80 94 byte-exact via od -c; root self-ref §CV |
| a002 | boundary (1st H2) | PASS | h_lvl=2 sib=1 canonical; parent §CV chapter root |
| a003 | boundary (Ex1 narrative w/ cross_refs) | PASS | cross_refs=["rows 1 to 3"] inline-verified §D-7.3 |
| a004 | boundary (`**cv.xpt**` D-5 bold-caption) | PASS | atom_type=SENTENCE per §R-D5 — NOT HEADING/NOTE |
| a005 | boundary (TABLE_HEADER Ex1, Hook A1) | PASS | line_end-line_start=1 v1.9 standard 2-row; 15 cols |
| a011 | boundary (Ex1→Ex2 H2 transition) | PASS | h_lvl=2 sib=2 canonical; parent §CV chapter root |
| a014 | boundary (TABLE_HEADER Ex2, Hook A1) | PASS | line_end-line_start=1 v1.9 standard 2-row; 18 cols |
| a022 | boundary (last TABLE_ROW EOF) | PASS | line 32 EOF correct; sequential a001..a022 verified |

### Stratified atoms (3 sampled)

| atom_id | sample_class | verdict | key check |
|---|---|---|---|
| a008 | stratified (mid Ex1 TABLE_ROW) | PASS | pipe-delimited 15-col row byte-exact; STANFADC class A |
| a012 | stratified (Ex2 narrative SENTENCE) | PASS | atom_type=SENTENCE; cross_refs=[] (no inline ref) |
| a018 | stratified (mid Ex2 TABLE_ROW) | PASS | pipe-delimited 18-col row byte-exact; comma preserved |

## Hook A1 (TABLE_HEADER style)

11 atoms sampled. 2 TABLE_HEADER instances:
- a005 (Ex1, lines 9-10): line_end-line_start = **1** → v1.9 standard 2-row ✓
- a014 (Ex2, lines 23-24): line_end-line_start = **1** → v1.9 standard 2-row ✓

**Style classification**: 2/2 v1.9 standard 2-row + 0/2 v1.8 pilot 1-row legacy. Both atoms B-03 domains (CV/examples.md, NOT ch04 a001-a218 pilot range), so v1.9 standard mandatory per §R-D6 — both compliant. **0 FAIL_LINE_RANGE** post-classification.

## §R-D5 bold-caption SENTENCE adherence

a004 (`**cv.xpt**` line 7) audited: caption pattern `^\*\*[a-z]+\.[a-z]+\*\*$` matches D-5 bold-caption canonical. Reviewer **accepts** atom_type=SENTENCE (not HEADING / not NOTE since text is `cv.xpt` filename ≠ `Note`/`Exception`). a013 (`**cv.xpt**` line 21) not in stratified sample but verified parallel by a004 byte-exact identity (od -c confirmed both lines 7 and 21 are `* * c v . x p t * *`).

## Kickoff drift verification (§R-D1)

No `kickoff_doc_drift_detected` flag in current batch. Reviewer independently verified:
- File 32 lines: matches kickoff §2.2 numeric claim (`32 lines`) ✓
- 22 atoms produced: matches kickoff atom estimate ✓
- §R-D1: writer atoms align with source byte-exact + kickoff. **No drift detected**.

## Schema field compliance

- atom_id sequential a001..a022 (no gaps) ✓
- HEADING (a001/a002/a011): heading_level + sibling_index populated; non-HEADING null ✓
- parent_section namespace: a001/a002/a011 → §CV chapter root; a003-a010 → §CV.1; a012-a022 → §CV.2 ✓
- cross_refs: only a003 has `["rows 1 to 3"]`; all others `[]` ✓
- figure_ref: all null (no figure references in CV/examples.md) ✓
- extracted_by.prompt_version: P0_writer_md_v1.9.1 ✓
- extracted_by.subagent_type: general-purpose (Rule D distinct from reviewer pr-review-toolkit:code-reviewer) ✓

## Gate

- **Rule A audit**: GREEN (11/11 = 100% strict PASS)
- **Rule D isolation**: GREEN (writer general-purpose ≠ reviewer pr-review-toolkit:code-reviewer)
- **Hook A1 (TABLE_HEADER)**: GREEN (2/2 v1.9 standard 2-row, 0 pilot legacy)
- **§R-D5 bold-caption SENTENCE**: GREEN (a004 + a013 D-5 canonical accepted)
- **§R-D1 kickoff drift**: GREEN (no drift, source = atoms = kickoff)

## Halt-trigger

- 22 atoms ∈ [11, 44] per-batch sampling band ✓ (no need to escalate to multi-batch cumulative audit)
- 0 HIGH/MEDIUM/LOW findings → no halt

## Paths

- Verdicts JSONL: `/Users/bojiangzhang/MyProject/SDTM-compare/.work/06_deep_verification/evidence/checkpoints/rule_a_P2_B-03_batch_28_verdicts.jsonl`
- Summary MD (this file): `/Users/bojiangzhang/MyProject/SDTM-compare/.work/06_deep_verification/evidence/checkpoints/rule_a_P2_B-03_batch_28_summary.md`
- Source: `/Users/bojiangzhang/MyProject/SDTM-compare/knowledge_base/domains/CV/examples.md`
- Writer atoms: `/Users/bojiangzhang/MyProject/SDTM-compare/.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_28_md_atoms.jsonl`

## DONE

**Verdict**: batch_28 Rule A audit **PASS** (11/11 = 100% strict; 0 HIGH/MEDIUM/LOW). Proceed to next batch.
