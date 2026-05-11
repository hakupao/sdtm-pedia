# P1 Batch 24 Report (Session C, Round 4)

> Status: **completed**
> Date: 2026-04-26
> Scope: ig34 p.231-240, §6.3.5.5 IS body (IS-Specification body / IS-Assumptions / IS-Examples 1-11 / IS tail)
> Sub-batches: 24a oh-my-claudecode:executor p.231-235 (118 atoms) + 24b oh-my-claudecode:writer p.236-240 (post Option E 90 atoms; pre Option E 113)
> Total atoms: **208** (raw 24a 118 + 24b post Option E 90)
> Failures: 0
> Repair cycles: **2** (Option H R15 Examples sib renumber + Option E p.236-240 wholesale executor rerun)

## Sub-batch summary

| Sub-batch | Subagent | Pages | Atoms | Status |
|---|---|---|---|---|
| 24a | oh-my-claudecode:executor | p.231-235 | 118 | DONE 0 failures, 0 sub-batch repair |
| 24b raw | oh-my-claudecode:writer | p.236-240 | 113 | DONE 0 failures (raw); writer-family wide-TABLE_HEADER corruption caught by NEW8 |
| 24b post Option H | (Option H sib renumber) | — | 113 | Examples 6-11 sib=1-6 → sib=6-11 (R15 cross-batch continuity fix) |
| 24b post Option E | (Option E executor rerun) | p.236-240 | 90 | Wholesale rerun, 23 atom net drop (mostly duplicate-hallucinated TABLE_HEADER cols removed) |

## Per-page density

| Page | Atoms | Status |
|---|---|---|
| 231 | 19 | OK |
| 232 | 14 | DENSITY ALARM ↓ FALSE POSITIVE (list-only page, O-P1-73) |
| 233 | 32 | OK (drift cal target page) |
| 234 | 23 | OK |
| 235 | 30 | OK |
| 236 | 16 | OK (post Option E) |
| 237 | 18 | OK (post Option E) |
| 238 | 15 | OK (post Option E, 1 residual TABLE_HEADER column-set issue O-P1-74) |
| 239 | 16 | OK (post Option E) |
| 240 | 25 | OK (post Option E) |

## Atom type breakdown

| Type | Count |
|---|---|
| TABLE_ROW | 70 |
| SENTENCE | 57 |
| LIST_ITEM | 45 |
| HEADING | 13 |
| CODE_LITERAL | 10 |
| TABLE_HEADER | 10 |
| NOTE | 3 |
| **Total** | **208** |

## HEADING chain (NEW7 L5/L6/L7 deep-nesting)

| Page | Level | Sib | Verbatim |
|---|---|---|---|
| 231 | L5 | 3 | IS – Assumptions |
| 233 | L5 | 4 | IS – Examples |
| 233 | L6 | 1 | Example 1 |
| 233 | L6 | 2 | Example 2 |
| 234 | L6 | 3 | Example 3 |
| 235 | L6 | 4 | Example 4 |
| 235 | L6 | 5 | Example 5 |
| 237 | L6 | 6 | Example 6 (post Option H R15 fix from sib=1) |
| 237 | L6 | 7 | Example 7 (post Option H R15 fix from sib=2) |
| 238 | L6 | 8 | Example 8 (post Option H R15 fix from sib=3) |
| 239 | L6 | 9 | Example 9 (post Option H R15 fix from sib=4) |
| 240 | L6 | 10 | Example 10 (post Option H R15 fix from sib=5) |
| 240 | L6 | 11 | Example 11 (post Option H R15 fix from sib=6) |

## Drift Cal NEW1 dual-threshold (MANDATORY batch 24, target p.233)

| Metric | Value | Verdict |
|---|---|---|
| Strict count | 94.1% (32 baseline / 34 rerun) | PASS |
| Verbatim hash overlap | 41.2% | FAIL |
| **Overall** | strict PASS + verbatim FAIL | **FAIL** |

DIRECTION REVERSED 8th precedent (writer rerun semantic-drifted vs executor baseline). Drift cal value-add 9th precedent. NEW1 STRONGLY VALIDATED 4th time (round 1+2+3+4).

Full report: `drift_cal_batch_24_p233_report.md`.

## Rule A audit (slot #33 oh-my-claudecode:scientist, AUDIT pivot 14th, omc-family 7th burn)

| Metric | Value |
|---|---|
| Sample size | 10 atoms (1/page p.231-240) |
| Stratification | 5 TABLE_ROW + 3 HEADING + 1 LIST_ITEM + 1 TABLE_HEADER |
| Seed | 20260525 |
| Raw PASS | 9 |
| Raw PARTIAL | 0 |
| Raw FAIL | 1 (ig34_p0238_a004 TABLE_HEADER column-set error) |
| **Raw weighted%** | **90.0%** |
| Verdict | **PASS_AT_THRESHOLD** |

TOC anchor n=150 cumulative / 15 consecutive batches / 4 families (1 family pool COMPLETED post round 3 + omc-family 7th burn round 4 + feature-dev family 3rd burn pool COMPLETED post round 4 batch 25).

## Findings (O-P1-71..74 reserved range, G-MS-13 PASS)

- **O-P1-71 HIGH**: writer-family wide-TABLE_HEADER systemic corruption (8th batch P1 cumulative; joins O-P1-23/34/36/37/38/50/63); Option E wholesale rerun applied
- **O-P1-72 MEDIUM**: drift cal NEW1 verbatim FAIL writer-family SENTENCE/LIST_ITEM paraphrase drift; DIRECTION REVERSED 8th precedent + drift cal value-add 9th precedent + NEW8.b SENTENCE-trigram extension v1.4 candidate
- **O-P1-73 LOW**: G-MS-12 density alarm p.232 FALSE POSITIVE (list-only page 14 atoms <15 floor); G-MS-12.a content-type-aware density floor sub-rule v1.4 candidate (3rd FALSE POSITIVE precedent)
- **O-P1-74 INFO**: Rule A residual p.238 a004 TABLE_HEADER NHOID-missing/ISORRESU-spurious column-set error; reconciler-deferred manual repair candidate; NEW8.c TABLE_HEADER column-set validation v1.4 candidate

All 4 finding IDs ∈ O-P1-71..74 reserved range = G-MS-13 self-validation PASS.

## Round 4 compliance

| Rule | Status |
|---|---|
| G-MS-4 halt fallback decision tree | NOT triggered (no unrecoverable halt; live-fire still NOT tested 4th round; recommend round 5 live-fire OR accept spec-only validation) |
| G-MS-7 finding ID range pre-allocation | PASS (no mis-allocation; §0 cross-validation table effective) |
| G-MS-11 NEW6 dual-form codification | EFFECTIVE 0 violations / 208 atoms |
| G-MS-11.b L4 self-parent extension | N/A (no L4 transitions in batch 24) |
| G-MS-12 density alarm | TRIGGERED p.232 → main-session FALSE POSITIVE adjudicated (3rd precedent) |
| G-MS-13 self-validation gate (round 3 NEW) | PASS — preventive check confirmed all finding IDs ∈ reserved range |
| NEW1 dual-threshold drift cal | STRONGLY VALIDATED 4th time (round 1+2+3+4) |
| NEW7 L4-L7 chain | L5 IS-Description/Specification/Assumptions/Examples + L6 Examples 1-11 contiguous post Option H |
| NEW8 substring n-gram cross-check | EFFECTIVE caught 6+ wide-TABLE_HEADER drifts pre Option E; 0 real flag post Option E |

## v1.4 candidates added round 4 (3 new)

1. **NEW8.b SENTENCE-trigram extension**: extend NEW8 substring n-gram cross-check to whole-SENTENCE trigram comparison vs baseline (currently NEW8 only catches `[A-Z]{3,}` variable name char-swap; needs to catch SENTENCE/LIST_ITEM paraphrase drift caught by drift cal NEW1 verbatim FAIL)
2. **NEW8.c TABLE_HEADER column-set validation**: extend NEW8 to verify TABLE_HEADER column SET (not just individual variable spell) matches expected canonical column set per PDF + per CDISC IS spec (caught Rule A p.238 a004 NHOID-missing residual gap)
3. **G-MS-12.a content-type-aware density floor sub-rule**: list-only pages floor=8 (not 15); spec-table pages floor=15 (current); transition pages floor=8 R12 (3rd FALSE POSITIVE precedent demands threshold relaxation for pure-list content)

## Files written (session C independent scope)

```
evidence/checkpoints/pdf_atoms_batch_24a.jsonl                                    (118 atoms)
evidence/checkpoints/pdf_atoms_batch_24b.jsonl                                    (90 atoms post Option E + Option H)
evidence/checkpoints/pdf_atoms_batch_24b.jsonl.pre-OptionH-R15-Examples.bak       (113 atoms pre Option H)
evidence/checkpoints/pdf_atoms_batch_24b.jsonl.pre-OptionE-p236-240.bak           (113 atoms pre Option E)
evidence/checkpoints/option_e_rerun_p236_240.jsonl                                (90 atoms Option E rerun)
evidence/checkpoints/drift_cal_p233_writer_rerun.jsonl                            (34 atoms drift cal writer rerun)
evidence/checkpoints/drift_cal_batch_24_p233_report.md                            (NEW1 dual-threshold report)
evidence/checkpoints/_progress_batch_24.json                                      (sub-progress + round_4_compliance)
evidence/checkpoints/P1_batch_24_report.md                                        (this file)
evidence/checkpoints/rule_a_batch_24_sample.jsonl                                 (10 atoms stratified)
evidence/checkpoints/rule_a_batch_24_verdicts.jsonl                               (10 verdicts per-atom 4-dim)
evidence/checkpoints/rule_a_batch_24_summary.md                                   (Rule A summary 125 lines)
```

## Files NOT touched (留给 reconciler)

- root `pdf_atoms.jsonl` / `audit_matrix.md` / `_progress.json`
- `subagent_prompts/*` / `schema/*` / `PLAN.md` / `plans/*` / `CLAUDE.md` / MEMORY
- sister batch files `pdf_atoms_batch_23*` / `pdf_atoms_batch_25*`

## Reconciler action items

1. Merge `pdf_atoms_batch_24a.jsonl` + `pdf_atoms_batch_24b.jsonl` to root `pdf_atoms.jsonl` (5502 + 208 = 5710 atoms expected post merge)
2. Update root `_progress.json` with batch 24 row + 4 findings O-P1-71..74
3. Update `audit_matrix.md`:
   - P1 Batch Roster row (batch 24 / 208 atoms / Option H + Option E 2 cycles / Rule A 90% AT-threshold)
   - P1 Drift cal row (batch 24 / p.233 / NEW1 dual strict 94.1% PASS verbatim 41.2% FAIL DIRECTION REVERSED 8th)
   - P1 Rule A row (batch 24 / slot #33 oh-my-claudecode:scientist / AUDIT pivot 14th / 90% AT-threshold)
   - Rule D Roster narrative update (slot #33 + AUDIT pivot 14th + omc-family 7th burn)
   - n cumulative 150 / 15 consecutive batches conclusion
4. Manual repair candidate: ig34_p0238_a004 TABLE_HEADER NHOID-missing/ISORRESU-spurious column-set (low priority, reconciler-deferred per O-P1-74 INFO)
