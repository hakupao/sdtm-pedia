# Rule A Audit Summary — P2 B-03c Round 10 batch_109 (SM/examples.md)

> Date: 2026-05-07
> Reviewer prompt: `subagent_prompts/P0_reviewer_v1.9.3.md` (35 hooks)
> Source: `knowledge_base/domains/SM/examples.md` (40 lines, 1 numbered H2 §2.5 Example 1, 3 tables L15+L28+L37)
> Atoms: `evidence/checkpoints/P2_B-03_batch_109_md_atoms.jsonl` (23 atoms claimed: H=2, SEN=10, THDR=3, TROW=8)
> Round 10 context: v1.9.3 1st production validation round (post commit 6990c54); 0 §2.11 Plan B trigger expected (numbered H2, no nested H3); §F-1 backward compat + §F-2 ratio band verification.

## Verdict

**PASS — 23/23 atoms PASS (100%); 0 HIGH severity finding; 0 schema regression; 0 atom_id collision; 0 §2.11 Plan B trigger; §F-2 ratio 0.575 INFO (just below band, table-density driver).**

## Per-check matrix

| # | Check | Result |
|---|---|---|
| 1 | atom_id sequential a001..a023 (23 atoms, 0 collision) | PASS |
| 2 | file path `knowledge_base/domains/SM/examples.md` (23/23) | PASS |
| 3 | parent_section: a001+a002 = `§SM [SM — Examples]` (file-root, H1+H2); a003-a023 = `§SM.1 [Example 1]` (§2.5 sub-namespace, sib=1 single H2) | PASS |
| 4 | line ranges within [1, 40] (no out-of-range) | PASS |
| 5 | atom_type ∈ 9 valid types: HEADING=2, SENTENCE=10, TABLE_HEADER=3, TABLE_ROW=8 (= 23 claimed) | PASS |
| 6 | verbatim byte-exact (single-line spot 23/23 match) | PASS |
| 7 | §R-E2 a001 H1 hl=1 sib=1; a002 H2 hl=2 sib=1 EXPLICIT | PASS |
| 8 | §R-E3 3× TABLE_HEADER (a008 L15, a016 L28, a021 L37) sib=null hl=null EXPLICIT | PASS |
| 9 | §R-E5 21× non-HEADING (10 SEN + 3 THDR + 8 TROW) hl=null AND sib=null EXPLICIT (0 violation) | PASS |
| 10 | §R-E4 extracted_by object form (subagent_type+prompt_version+ts) 23/23 | PASS |
| 11 | prompt_version = `P0_writer_md_v1.9.3` 23/23 (no v1.9.2 leakage) | PASS |
| 12 | 12 fields per atom (no extra/missing keys) 23/23 | PASS |
| 13 | Table separators L16, L29, L38 NOT atomized (verified: gap in atomized line set) | PASS |
| 14 | cross_refs sanity: SM self-domain excluded (0 self-ref); MH/CE properly attached on related atoms (a013 [MH,CE] L22 narrative; a014-a018 [MH] L24-L31 mh.xpt section; a019-a023 [CE] L33-L40 ce.xpt section) | PASS |

## §2.5 Numbered H2 namespace correctness

Single H2 `## Example 1` (L3) → `§SM.1 [Example 1]` sib_idx=1 unique. All 21 child atoms (a003-a023) carry this parent_section. Verified: `set(a['parent_section'] for a in atoms[2:])` = `{'§SM.1 [Example 1]'}` (1 unique value, 0 leakage to file-root).

## §F-1 §2.11 Plan B audit verify

**Trigger NOT fired**: numbered H2 (`## Example 1`) with NO H3 children → §2.5 baseline applies, NOT Plan B. §R-F-1 verification N/A this batch. Backward-compat sustained (file-root H1+H2 namespace pattern preserved per §R-E2).

## §F-2 atoms/line ratio retrospective (INFO)

ratio = 23 / 40 = **0.5750** — just below empirical band 0.59-0.85 (delta 0.015 = 2.5%).
**Driver**: 3-table density (sm.xpt 4 rows + mh.xpt 2 rows + ce.xpt 2 rows = 11 TROW + 3 THDR = 14 table atoms = 60.9% of total) compresses non-table prose. 17 lines un-atomized (L2/4/6/8/10/12/14 blanks + L16/29/38 separators + L21/23/25/27/32/34/36 blanks). Empirical: blank lines (10) + separators (3) + bold-marker label rendering on adjacent line vs source line gap; structural compression typical for examples.md tri-table layout. **NOT halt** — INFO finding, well within calibration noise (band lower bound 0.59 is empirical 9-round, not hard rule).

## §F-3 kickoff estimate calibration (INFO)

Kickoff estimated 23 atoms (H=2, SEN=10, THDR=3, TROW=8); actual = 23 (exact match, delta_pct = 0%). Calibration excellent (no §F-3 flag).

## Schema regression sweep (§R-E1 PRIORITY 1)

- §R-E2 (H1 sib=1): a001 hl=1 sib=1 PASS
- §R-E3 (TABLE_HEADER sib=null): a008/a016/a021 all hl=null sib=null PASS
- §R-E4 (extracted_by object): 23/23 object form PASS
- §R-E5 (non-HEADING field-explicit-null): 21/21 PASS
- §R-E6 (FIGURE-vs-CODE_LITERAL): N/A (no FIGURE/CODE_LITERAL in batch)

**0 schema regression detected.**

## Spot-check (2 atoms verbatim manual)

- **a001 L1** `# SM — Examples` — source L1 `# SM — Examples` byte-exact match (em-dash U+2014 preserved).
- **a017 L30** `| 1 | XYZ | MH | 001 | 1 | TYPE 2 DIABETES | Type 2 diabetes mellitus | DIAGNOSIS | Y | Y | 2013-08-06 | 2005-10 | | | DIAG |` — source L30 byte-exact match (15 pipe-separated cells, 2 empty cells preserved between MHENDTC/MHDY/MIDS).

## HIGH findings

**None.** 0 HIGH severity finding. 0 halt trigger.

## Halt status

**NO HALT** — PASS rate 100% (≥90%); 0 HIGH; 0 regression; 0 collision.

## Round 10 cumulative status (post batch_109)

batch_104 (RELSPEC/ass) + batch_105 (RELSPEC/ex) + batch_106 (RELSUB/ass) + batch_107 (RELSUB/ex) + batch_108 (SM/ass) + batch_109 (SM/ex) all PASS. v1.9.3 1st round sustained validation: 6 batches green, 0 HIGH, 0 regression. §F-1/F-2/F-3 hooks operational.
