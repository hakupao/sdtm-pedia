# Rule A Audit — P2 B-03c batch_14 (AE/examples.md)

> Reviewer subagent_type: `pr-review-toolkit:code-reviewer` (peer-alternative pool per v1.9.1 §R-D8; ≠ writer subagent_type `general-purpose`, Rule D PASS)
> Audit ts: 2026-05-05
> Source: `knowledge_base/domains/AE/examples.md` (1–97 lines, 6 Examples)
> Writer output: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_14_md_atoms.jsonl` (97 atoms)
> Sample size: 11 verdicts (8 boundary + 3 stratified)
> Reviewer prompt version: `P0_reviewer_v1.9.1` (26 hooks)

## Sample composition

| Sample role | atom_id | atom_type | parent_section | line_range |
|---|---|---|---|---|
| boundary_first_h1_root | a001 | HEADING | §AE [AE — Examples] | 1 |
| boundary_h2_self_reference_pilot_drift_caught | a002 | HEADING | §AE.1 [Example 1] | 3 |
| boundary_bold_caption_xpt | a015 | SENTENCE | §AE.1 [Example 1] | 11 |
| boundary_table_header_middle_ex1 | a016 | TABLE_HEADER | §AE.1 [Example 1] | 13-14 |
| boundary_bold_caption_rows | a027 | SENTENCE | §AE.2 [Example 2] | 23 |
| boundary_table_header_ex3 | a046 | TABLE_HEADER | §AE.3 [Example 3] | 43-44 |
| boundary_h2_sib_chain_ex4 | a049 | HEADING | §AE.4 [Example 4] | 48 |
| boundary_table_row_middle | a058 | TABLE_ROW | §AE.4 [Example 4] | 63 |
| stratified_sub_line_narrative_l71 | a070 | SENTENCE | §AE.5 [Example 5] | 71 |
| stratified_table_row_ex5 | a081 | TABLE_ROW | §AE.5 [Example 5] | 82 |
| stratified_h2_ex6_sib_chain_check | a082 | HEADING | §AE.6 [Example 6] | 84 |

## Per-atom verdicts

| atom_id | verdict | severity |
|---|---|---|
| a001 | PASS | INFO |
| a002 | PASS | INFO |
| a015 | PASS | INFO |
| a016 | PASS | INFO |
| a027 | PASS | INFO |
| a046 | PASS | INFO |
| a049 | PASS | INFO |
| a058 | PASS | INFO |
| a070 | PASS | INFO |
| a081 | PASS | INFO |
| a082 | PASS | INFO |

**Strict PASS rate**: 11/11 = **100%**.

## §C-1 sub-line atomization legitimacy verification

Writer reported 97 atoms vs estimate 70-90 (above midpoint, within halt #8 [35,135]). Driver: §C-1 sub-line atomization on narrative-heavy lines.

Independent reviewer count of sub-line atoms per source line:

| Source line | Atom count | Writer kickoff claim | Verdict |
|---|---|---|---|
| L5 (Example 1 narrative) | 5 | 5 sentences | PASS |
| L21 (Example 2 narrative) | 6 | 6 sentences | PASS |
| L37 (Example 3 narrative) | 7 | 7 sentences | PASS |
| L71 (Example 5 narrative) | 9 | 9 sentences | PASS |

All sub-line atoms have `line_start == line_end == <line>` (correct per §C-1). Each atom captures one distinct sentence; no fragmenting wrong, no duplicate. Hook R22 (sub-line SENTENCE multi-atom on same line_range NOT ERROR/MISPLACED) confirmed clean.

**Sub-line atomization driver legitimate** — NOT a finding. The 97-atom count is a faithful consequence of source narrative density; the writer's §C-1 application is byte-exact and per-sentence canonical.

## H2 self-reference convention verification (CM pilot inheritance)

Per kickoff §2 + CM pilot precedent, all 6 H2 atoms in this batch use SELF-reference parent_section:

| atom_id | source line | verbatim | parent_section | sib_index | Verdict |
|---|---|---|---|---|---|
| a002 | L3 | `## Example 1` | §AE.1 [Example 1] | 1 | self ✓ |
| a020 | L19 | `## Example 2` | §AE.2 [Example 2] | 2 | self ✓ |
| a035 | L35 | `## Example 3` | §AE.3 [Example 3] | 3 | self ✓ |
| a049 | L48 | `## Example 4` | §AE.4 [Example 4] | 4 | self ✓ |
| a063 | L69 | `## Example 5` | §AE.5 [Example 5] | 5 | self ✓ |
| a082 | L84 | `## Example 6` | §AE.6 [Example 6] | 6 | self ✓ |

All 6 H2 atoms consistently apply CM pilot convention. Writer correctly Rule-B'd over any orchestrator-side prompt drift. sib_index is positional (1..6) per source order. **All children atoms inside `## Example N` blocks correctly inherit `§AE.N [Example N]`** (spot-checked across all 6 example blocks).

## Kickoff drift verification (§R-D1)

Per dispatch prompt: "main session dispatch prompt had a drift the writer caught via Rule B" — H2 self-reference convention.

**Reviewer independent verification**: writer atoms a002/a020/a035/a049/a063/a082 all apply `§AE.<N> [Example <N>]` self-reference (NOT escalate to `§AE [AE — Examples]` file root). This matches CM pilot precedent and source-byte-exact intent. Writer Rule-B compliance confirmed; no HIGH severity defect.

Per Hook R24, kickoff drift instances route to orchestrator-level batch report — NOT writer FAIL.

## TABLE_HEADER 2-row span (Hook A1) classification

All 6 TABLE_HEADER atoms in this batch:

| atom_id | line_range | delta | style |
|---|---|---|---|
| a016 | 13-14 | 1 | v1.9 standard 2-row |
| a031 | 29-30 | 1 | v1.9 standard 2-row |
| a046 | 43-44 | 1 | v1.9 standard 2-row |
| a056 | 60-61 | 1 | v1.9 standard 2-row |
| a079 | 79-80 | 1 | v1.9 standard 2-row |
| a095 | 94-95 | 1 | v1.9 standard 2-row |

**6/6 v1.9 standard 2-row + 0 v1.8 pilot 1-row legacy; 0 FAIL_LINE_RANGE post-classification.** AE/examples.md is outside ch04 pilot range so no legacy expected — confirmed.

## §D-5 bold-caption SENTENCE compliance (§R-D5)

12-13 bold-caption SENTENCE atoms in batch (Rows N-M / Row N / ae.xpt). Sample includes 2 (a015 `**ae.xpt**` + a027 `**Rows 1-2:** Show...`). Both:
- atom_type=SENTENCE (NOT NOTE — caption text is `ae.xpt` / `Rows`, neither is `Note` or `Exception` literal — strict §R-D5 carve-out)
- bold markers `**` preserved verbatim byte-exact
- For caption + narrative continuation on same line (a027), full line emitted as one atom (NOT split caption from narrative)

**Pattern compliance: 100% sample.** Spot-check on a052/a053/a054/a073/a075/a087/a090 (bold-caption SENTENCEs): all consistent.

## Rule D 隔离 verification

- Writer subagent_type: `general-purpose`
- Reviewer subagent_type: `pr-review-toolkit:code-reviewer`
- ≠ writer (peer-alternative pool per v1.9.1 §R-D8 SUSTAINED status)
- **Rule D PASS**

## Verdict

- **Strict PASS rate**: 11/11 = 100%
- **HIGH severity findings**: 0
- **MEDIUM severity findings**: 0
- **LOW severity findings**: 0
- **Sub-line atomization driver**: legitimate (NOT a finding)
- **PASS gate**: ≥90% strict PASS achieved → **PASS**

---

RULE_A_VERDICT: PASS
