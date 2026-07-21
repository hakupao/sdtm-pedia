# P0 Writer MD — 原子化 prompt v1.9.4

> Version: v1.9.4 (2026-05-11, post P2 B-03c rounds 10-12 CLOSED + ★ §F-1 descriptive-title H3 motif 7th cumulative case (3 distinct H3 title pattern types validated) + §2.4 multi-slice atom_id 续号 3rd production trigger STRONGLY VALIDATED + §F-2 de-figure-naive formula 2 consecutive FIGURE-heavy rounds sustained + §2.6 FIGURE-heavy 20-block single-round NEW peak validated)
> Cut trigger: v1.9.4 candidate stack **MET 3 rounds sustained** (post rounds 10+11+12 all at ≥10 cut planning trigger threshold; 7 actionable candidates consolidated into 4 NEW G-rules).
> 基于 v1.9.3 (2026-05-07) + B-03c rounds 10-12 evidence (`evidence/checkpoints/` + `multi_session/P2_B-03c_round_{10,11,12}_kickoff.md` + `_progress.json` `b_03c_round_{10,11,12}_details`)
> 角色: Writer MD (原子化), 独立 subagent, 与 Reviewer/Matcher 不同 subagent_type
> v1.9.4 变更 over v1.9.3: 4 NEW G-rules — §G-1 HIGH §F-1 Extension descriptive-title H3 title-agnostic explicit codification (7 cumulative cases milestone; 3 distinct title pattern types validated: Example N / References / descriptive) + §G-2 HIGH §2.4 multi-slice atom_id 续号 first-class codification (3rd production trigger STRONGLY VALIDATED) + §G-3 INFO→STANDARD §F-2 de-figure-naive formula promote to STANDARD recipe (2 consecutive FIGURE-heavy rounds 11+12 sustained) + §G-4 INFO §2.6 FIGURE-heavy domain estimate adjustment (20-block single-round NEW peak validated). **Backward compatible** with v1.9.3 atoms (rounds 10-12 production atoms 794 cumulative post v1.9.3 cut byte-exact preserved: round 10 = 182 + round 11 = 208 + round 12 = 404).

## 角色硬约束 (v1.7/v1.8/v1.9/v1.9.1/v1.9.2/v1.9.3 carry-forward unchanged)

参 `archive/v1.7_final_2026-04-30/P0_writer_md_v1.7.md` §角色硬约束 全文.
参 `archive/v1.9_final_2026-05-05/P0_writer_md_v1.9.md` §C-1..C-8 全文.
参 `archive/v1.9.1_final_2026-05-06/P0_writer_md_v1.9.1.md` §D-1..D-8 全文.
参 `archive/v1.9.2_final_2026-05-07/P0_writer_md_v1.9.2.md` §E-1..E-6 全文.
参 `archive/v1.9.3_final_2026-05-11/P0_writer_md_v1.9.3.md` §F-1..F-3 全文 (§F-1 §2.11 Plan B sub-namespace + §F-2 atoms/line ratio band + §F-3 kickoff estimate nested-list calibration).

═══════════════════════════════════════════════════════════════════
## v1.9.4 NEW PATCHES (G-1..G-4, B-03c rounds 10-12 evidence-driven)
═══════════════════════════════════════════════════════════════════

### §G-1 §F-1 Extension — descriptive-title H3 title-agnostic explicit codification (HIGH — 7 cumulative cases milestone, 3 distinct title pattern types validated)

**Background**: v1.9.3 §F-1 established §2.11 Plan B (sib_idx-based namespace for numberless H2 with H3 children) as title-agnostic. v1.9.3 explicit case coverage included `### Example N` (PC/ex round 07) and `### References` (RS/ex round 09). Round 12 batch_127 TE/ex L48 added a **NEW motif**: descriptive-title H3 titles `### Granularity of Trial Elements` / `### Distinguishing Elements, Study Cells, and Epochs` / `### Transitions Between Elements`. These are neither `### Example N` patterns nor `### References` — they are arbitrary descriptive-title H3s.

**Key fact**: §TE.4.1 [Granularity of Trial Elements] / §TE.4.2 [Distinguishing Elements, Study Cells, and Epochs] / §TE.4.3 [Transitions Between Elements] — all sib_idx-based namespace. Round 12 mini-audit 10/10 PASS including these atoms.

**Cumulative cases post round 12**: 7 total
- round 07 PC/ex L58 (1 case Example N pattern)
- round 09 RELREC/ex L3+L53 + RS/ex L3+L65 (4 cases mix of Example N + References)
- round 12 TA/ex L694 (5th case Example N pattern)
- round 12 TE/ex L48 (6th case + 7th case via 3 descriptive-title H3 children — counts as cumulative milestone for descriptive-title motif)

**Status**: SUSTAINED VALIDATED EXTENDED (7 cumulative cases, **3 distinct H3 title pattern types validated**: Example N / References / descriptive).

**Rule (formal codification — extends §F-1)**:

§F-1 §2.11 Plan B sub-namespace is **strictly sib_idx-based**, NOT title-based. The H3 title pattern is irrelevant to namespace shape. Three validated pattern types post round 12:

| H3 title pattern | Round | Example | Namespace shape |
|------------------|-------|---------|------------------|
| `### Example N` | 07 PC/ex L58, 12 TA/ex L694 | `### Example 1` | `§<D>.<N>.<K>` |
| `### References` | 09 RS/ex L92 | `### References` | `§<D>.<N>.<K> [References]` |
| **Descriptive arbitrary** | **12 TE/ex L48** | `### Granularity of Trial Elements` | `§<D>.<N>.<K> [<descriptive title>]` |

All three pattern types use the SAME namespace shape `§<D>.<N>.<K> [<H3 literal title>]` where K = H3 sib_idx within H2 scope.

**Anti-pattern (HALT)**:
- ❌ Assuming §F-1 only applies to `### Example N` or `### References` H3 titles — title-agnostic means ANY H3 title uses sib_idx-based namespace
- ❌ For descriptive-title H3s, attempting to slugify or summarize the title into the namespace (e.g., `§TE.4.granularity` or `§TE.4.gran_trial_elem` for `### Granularity of Trial Elements`); §G-1 mandates literal title in brackets `§TE.4.1 [Granularity of Trial Elements]`
- ❌ For long descriptive H3 titles, attempting to truncate or abbreviate in the bracket content; v1.9.4 mandates **literal full H3 title** in brackets (regardless of length)

**Pre-DONE Hook G-1 (NEW)**: Writer self-validate, for each H3 atom under §F-1 trigger:
1. Identify H3 title pattern type (Example N / References / Descriptive).
2. If **Descriptive**, verify bracket content is **literal full H3 title** (no truncation, no slugification).
3. Verify K = H3 sib_idx within H2 scope (NOT cumulative across H2s, NOT based on title sort order).
4. Confirm three title pattern types acceptance — writer behavior identical for all three.

Writer DONE report MUST include `section_F_1_title_patterns: PASS (X/X H3 atoms verified; pattern types: <Example N count> + <References count> + <Descriptive count>)` confirmation when §F-1 trigger fires with mixed or descriptive H3 titles.

**Reviewer rule (paired-sync §R-G-1)**: When auditing §F-1 trigger batch with descriptive-title H3s, emit FAIL_PLAN_B_NAMESPACE_DESCRIPTIVE_TITLE if title-based slugification or truncation found (e.g., `§TE.4.granularity` instead of `§TE.4.1 [Granularity of Trial Elements]`).

**Cumulative empirical baseline post round 12**: 7 cases × 7 H3-bearing numberless H2 + 19+ H3 children + 70+ content atoms across rounds 07/09/12. 3 distinct H3 title pattern types validated. 0 violation.

**B-03c round 13+ entry**: All kickoffs with numberless H2 with descriptive-title H3 children MUST include §G-1 dispatch instruction reminder ("descriptive-title H3 uses literal full title in brackets; namespace remains sib_idx-based").

### §G-2 §2.4 multi-slice atom_id 续号 first-class codification (HIGH — STRONGLY VALIDATED, 3 cumulative production triggers)

**Background**: §2.4 (large file slicing) has been a locked rule since round 03 inaugural trigger. Atom_id continuation across batch slices was implicit but never explicitly codified as a formal rule. Round 12 TA/ex 3-slice provided the 3rd cumulative production trigger:
- round 03 (inaugural production trigger)
- v1.9.3 cut B-02 validation (2nd trigger)
- round 12 TA/ex 3-slice (3rd trigger STRONGLY VALIDATED)

**Key evidence — TA/ex 710L → 3 slices**:
- Slice A (batch_123): atom_id a001..a113, sib_idx 1/2/3 (Examples 1-3 H3s)
- Slice B (batch_124): atom_id **a114**..a217, sib_idx 4/5/6 (Examples 4-6 H3s) — NOT reset to a001
- Slice C (batch_125): atom_id **a218**..a274, sib_idx 7+8 (Ex7 + Trial Arms Issues) — NOT reset to a001

**Cross-slice 续号 rule (formal codification)**:

For a source file split into N slices (slice A, B, C, ..., N) via §2.4:

1. **atom_id continuation**: atom_id suffix is **file-scope sequential**, NOT batch-scope reset
   - Slice A first atom: `<batch_A>_a001`
   - Slice B first atom: `<batch_B>_a<N_A+1>` where N_A = last atom suffix in slice A
   - Slice C first atom: `<batch_C>_a<N_B+1>` where N_B = last atom suffix in slice B
   - Generally: Slice K first atom suffix = (Σ atoms in slices A..K-1) + 1

2. **sib_idx continuation**: sib_idx is **file-scope cumulative within H2 scope**, NOT slice-scope reset
   - If slice A ends mid-H2 scope at sib_idx=3 (e.g., 3 H3 children written), slice B continues from sib_idx=4 within SAME H2 scope
   - If slice B starts a new H2 scope, sib_idx restarts to 1 within that new H2 scope (per §F-1 §2.11 Plan B normal restart at H2 boundary)
   - For numberless H2 sib_idx (file-scope), continues cumulative across slices

3. **prompt_version stamping**: All slices share the same prompt_version (file-level metadata); atom_id continuation is the disambiguator

**Anti-pattern (HALT)**:
- ❌ Resetting atom_id suffix to `a001` at start of each slice (= atom_id collision / duplicate within same file's namespace post-merge)
- ❌ Resetting sib_idx to 1 at slice boundary when still within same H2 scope (= sib_idx duplicate within scope)
- ❌ Reordering atoms across slice boundaries in a way that breaks line-monotonic source ordering (slice boundaries are line-monotonic by design)
- ❌ Hard-coding slice index into atom_id (e.g., `<batch>_sliceB_a001`) — file-scope sequential numbering is canonical

**Pre-DONE Hook G-2 (NEW)**: Writer self-validate, before DONE if multi-slice slice B/C:
1. Read kickoff §X to identify which slice this batch is (A/B/C).
2. If slice B/C: read prior slice's `atoms.jsonl` (path provided in kickoff) and verify:
   - First atom_id suffix in current batch = (last atom_id suffix in prior slice) + 1
   - If continuing same H2 scope: first sib_idx in current batch = (last sib_idx in prior slice within H2) + 1
3. Confirm no atom_id collision with prior slices (grep prior slice atom_id list, verify zero overlap).
4. If slice A (first slice): standard `a001` start, no continuation check needed.

Writer DONE report MUST include `multi_slice_continuation: PASS (slice <K>; first atom_id a<N+1> continues from prior slice last a<N>; sib_idx continuation verified)` confirmation when §G-2 trigger fires (i.e., this is slice B/C of a multi-slice file).

**Reviewer rule (paired-sync §R-G-2)**: For multi-slice batches, reviewer cross-checks slice boundaries — verify first atom of slice B/C has correct continuation ID (NOT a001 reset). Bash script:
```python
import json
prior = [json.loads(l) for l in open(prior_slice_path)]
curr = [json.loads(l) for l in open(curr_batch_path)]
prior_last_suffix = int(prior[-1]['atom_id'].split('_a')[-1])
curr_first_suffix = int(curr[0]['atom_id'].split('_a')[-1])
assert curr_first_suffix == prior_last_suffix + 1, f"FAIL multi-slice atom_id continuation: prior={prior_last_suffix} curr={curr_first_suffix}"
```

**Matcher rule (paired-sync §M-G-2)**: Matcher accepts multi-slice atom_id continuation as canonical — does NOT emit `atom_id_gap` or `file_atom_id_discontinuity` warnings for expected cross-slice continuation (e.g., slice A ends a113, slice B starts a114 = canonical, NOT a gap).

**Cumulative empirical baseline post round 12**: 3 cumulative production triggers (round 03 + v1.9.3 cut B-02 + round 12 TA/ex 3-slice). All 3 PASS file-scope atom_id continuity + sib_idx continuity post-merge.

### §G-3 §F-2 de-figure-naive formula promote to STANDARD recipe (STANDARD — 2 consecutive FIGURE-heavy rounds 11+12 sustained)

**Background**: v1.9.3 §F-2 codified the atoms/line empirical band 0.59-0.85 as INFO. Round 11 introduced the de-figure-naive formula (0.698 in-band vs naive 0.479 outside band when FIGURE atoms present). Round 12 confirmed (0.714 in-band vs naive 0.443 outside band). 2 consecutive FIGURE-heavy rounds with de-figure-naive formula correctly identifying in-band behavior = promote from INFO to STANDARD recipe.

**Standard formula (formal codification)**:

```
de_figure_ratio = N_atoms / (total_source_lines − Σfig_span + N_fig)
```

Where:
- `N_atoms` = total atom count in batch
- `total_source_lines` = total source MD lines in batch
- `Σfig_span` = sum of all FIGURE block line spans (from opening ` ```mermaid ` to closing ` ``` ` inclusive)
- `N_fig` = number of FIGURE atoms in batch (each mermaid block = 1 FIGURE atom)

**Logic**: The subtraction `−Σfig_span` removes the mermaid source lines (which collapse to 1 atom each, not per-line atoms). Adding back `+N_fig` accounts for the 1 atom that each mermaid block becomes.

**When to apply (decision table)**:

| Condition | Method |
|-----------|--------|
| `N_fig == 0` | Use naive ratio: `N_atoms / total_source_lines` (apply 0.59-0.85 band) |
| `N_fig ≥ 1` | **MUST use de-figure-naive ratio** (apply 0.59-0.85 band to de-figure ratio) |
| `N_fig ≥ 1 and naive_ratio < 0.59` and `Σfig_span > ~30 lines` | Confirm de-figure ratio in band — naive will mislead as "below band" |
| de-figure ratio OUTSIDE 0.59-0.85 band | INFO finding (NOT halt) — investigate unusual content driver |

**Empirical baseline rounds 11+12**:
- Round 11: naive 0.479 (outside band) vs de-figure 0.698 (in band) — 3 FIGURE atoms
- Round 12: naive 0.443 (outside band) vs de-figure 0.714 (in band) — 20 FIGURE atoms TA/ex

**Pre-DONE Hook G-3 (NEW STANDARD, replaces Hook F-2 INFO)**: Writer post-DONE retrospective check — compute BOTH ratios and report:
- If `N_fig == 0`: report `atoms_per_line_ratio: <naive>` (single value).
- If `N_fig ≥ 1`: report `atoms_per_line_ratio_naive: <naive> | atoms_per_line_ratio_defigure: <defigure> (STANDARD)` — both values, with de-figure marked STANDARD.
- Flag if de-figure ratio outside [0.59, 0.85] for INFO retrospective inspection.

**Reviewer rule (paired-sync §R-G-3)**: Round-close mini-audit computes de-figure ratio when FIGURE count ≥ 1 across the round. Verify cumulative round de-figure ratio is within 0.59-0.85 band. If outside, INFO finding (NOT halt) — investigate driver.

**Status**: §F-2 atoms/line ratio band — PROMOTED from INFO (v1.9.3) to **STANDARD** (v1.9.4) with explicit de-figure recipe.

### §G-4 §2.6 FIGURE-heavy domain estimate adjustment (INFO — 20-block single-round NEW peak validated)

**Background**: §2.6 (FIGURE-in-domains byte-exact copy) was first codified in v1.9.1. Round 12 set a single-round NEW peak: **20 FIGURE atoms from TA/ex** (vs round 11's 3, a **6.67× scale-up**). All 20 byte-exact PASS. This validates §2.6 at FIGURE-heavy domain scale.

**Estimate adjustment for FIGURE-heavy files (formal codification)**:

When a source file has ≥10 mermaid blocks (FIGURE-heavy threshold), naive estimate (`source_lines × {0.59, 0.73, 0.85}` from §F-2) widely **overstates** atom count. Use adjusted-lines estimate:

```
adjusted_lines = total_lines − Σfig_span + N_fig
```

(Same adjustment as §G-3 de-figure formula; reference §G-3 for definitions.)

Then apply 0.59-0.85 band to `adjusted_lines`:
- Low estimate: `adjusted_lines × 0.59`
- Mid estimate: `adjusted_lines × 0.73`
- High estimate: `adjusted_lines × 0.85`

**Empirical TA/ex worked example (round 12)**:
- Total lines: 911
- Σfig_span: 365 (sum of 20 mermaid block spans)
- N_fig: 20
- adjusted_lines = 911 − 365 + 20 = **566**
- mid estimate: 566 × 0.73 = **413 atoms**
- actual atom count: **404 atoms** (98% of mid estimate — well within band)
- naive estimate would be: 911 × 0.73 = 665 atoms (overstates by 64%)

**Trigger threshold**: ≥10 FIGURE atoms per domain source file (single-file aggregate; multi-batch slicing of same file counts cumulative).

**When to apply**:
- Pre-kickoff: orchestrator estimates atom count from source file — apply adjustment if ≥10 mermaid blocks detected
- Post-DONE: writer retrospective ratio uses §G-3 de-figure formula (matches estimate adjustment)
- Round-close: reviewer verifies de-figure ratio in band (paired-sync §R-G-4)

**FIGURE build-script defensive recipe (C-R12-07 incident)**:

Round 12 batch_124 incident: `block()` helper had trailing `\n` in mermaid body lines, resulting in atom body having **double-newlines** between mermaid lines. Symptom: byte-exact verification failed on mermaid atoms.

**Fix**: When generating FIGURE atoms programmatically:
```python
# WRONG: body = "\n".join(line for line in mermaid_lines)  # if lines already have trailing \n
# RIGHT:
body = "\n".join(line.rstrip("\n") for line in mermaid_lines)
```

Apply `line.rstrip("\n")` to each line before joining with `\n` separator. This prevents double-newline duplication.

**Pre-DONE Hook G-4 (NEW INFO, orchestrator-process)**: N/A writer-side direct hook (process rule applies to kickoff orchestrator + post-DONE retrospective via §G-3). DONE report unchanged from §G-3.

**Reviewer rule (paired-sync §R-G-4)**: INFO check for domains with ≥10 FIGURE atoms — confirm adjusted-lines estimate was used in kickoff. If naive estimate used (overstated by >50%), INFO carry-forward note (kickoff calibration improvement).

**Cumulative empirical baseline post round 12**: 1 cumulative production trigger (round 12 TA/ex 20 FIGURE; round 11 3 FIGURE was below threshold). All 20 mermaid atoms byte-exact PASS. §2.6 validated at FIGURE-heavy domain scale. Build-script defensive note codified.

### §F-1..F-3 carry-forward (v1.9.3 unchanged)

ALL v1.9.3 §F-1..F-3 rules carry-forward to v1.9.4 unchanged (extended by §G-1..G-4 above; §F-1 explicitly extended by §G-1, §F-2 promoted to STANDARD by §G-3):
- §F-1 HIGH §2.11 Plan B sub-namespace by sib_idx for numberless H2 with H3 children — extended by §G-1 (descriptive-title H3 codification)
- §F-2 INFO atoms/line ratio band 0.59-0.85 — **PROMOTED to STANDARD by §G-3** (de-figure-naive formula)
- §F-3 INFO Kickoff atom estimate calibration for multi-level nested-list domains — unchanged

### §E-1..E-6 carry-forward (v1.9.2 unchanged)

参 `archive/v1.9.2_final_2026-05-07/P0_writer_md_v1.9.2.md` for §E-1..E-6 full text.

### §D-1..D-8 carry-forward (v1.9.1 unchanged)

参 `archive/v1.9.1_final_2026-05-06/P0_writer_md_v1.9.1.md` for §D-1..D-8 full text.

═══════════════════════════════════════════════════════════════════
## CODIFIED R-RULES + NEW (v1.7/v1.8/v1.9/v1.9.1/v1.9.2/v1.9.3 carry-forward, FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.9.3_final_2026-05-11/P0_writer_md_v1.9.3.md` for §F-1..F-3 + carry-forward chain.

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (v1.9.4 = 33 hooks for MD-side)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- v1.9 Hook 22 + A1/A2/A3/A4 carry-forward
- v1.9.1 Hook 22b + D-NOTE-BQ + D-D8 carry-forward
- v1.9.2 NEW Hook 22c + E-2-1 + E-3-2 + E-4-3 + E-5 carry-forward
- v1.9.3 NEW Hook F-1 + F-2 carry-forward (Hook F-2 promoted to Hook G-3 STANDARD recipe)
- **v1.9.4 NEW Hook G-1**: §F-1 descriptive-title H3 title-agnostic verify — pre-DONE check literal full title in brackets (no slug, no truncate); confirm 3 title pattern types (Example N / References / Descriptive) handled identically
- **v1.9.4 NEW Hook G-2**: §2.4 multi-slice atom_id 续号 verify — pre-DONE check first atom_id suffix continues from prior slice's last suffix (NOT a001 reset); sib_idx file-scope cumulative verify when same H2 scope crosses slices
- **v1.9.4 NEW Hook G-3**: §F-2 de-figure-naive ratio STANDARD recipe — post-DONE compute both naive + de-figure ratios when N_fig ≥ 1; report de-figure as STANDARD (replaces Hook F-2 INFO)
- (Hook G-4 N/A writer-side — orchestrator process rule for FIGURE-heavy estimate adjustment)

**MD-side hook 总数**: 30 (v1.9.3) + 3 NEW (v1.9.4 Hook G-1 + G-2 + G-3) = **33 hooks effective**.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.4 sync with B-03c rounds 10-12 cycle evidence)
═══════════════════════════════════════════════════════════════════

- **§F-1 §2.11 Plan B title-agnostic 3 distinct H3 title pattern types**: NEW STATUS CODIFIED §G-1 — Example N + References + Descriptive all sib_idx-based namespace; 7 cumulative cases milestone (round 07 + round 09 + round 12).
- **§2.4 multi-slice atom_id 续号**: SUSTAINED VALIDATED EXTENDED — promoted from implicit to first-class codified §G-2 (3 cumulative production triggers: round 03 + B-02 + round 12 TA/ex 3-slice).
- **§F-2 atoms/line ratio band**: PROMOTED from INFO (v1.9.3) to **STANDARD** (v1.9.4) §G-3 with explicit de-figure-naive recipe (2 consecutive FIGURE-heavy rounds 11+12 sustained).
- **§2.6 FIGURE-heavy domain estimate adjustment**: NEW STATUS CODIFIED §G-4 INFO — 20-block single-round NEW peak validated (TA/ex round 12); FIGURE build-script defensive recipe codified (C-R12-07).
- **N21 PDF + MD all-side blanket ban**: STRONGLY VALIDATED EXTENDED (v1.9.3 baseline + B-03c rounds 10-12 18 batches × 2 = 36 cumulative writer dispatches all general-purpose, 0 N21 violation).
- **FALLBACK pool peer-alternative status**: STRONGLY VALIDATED EXTENDED (general-purpose + pr-review-toolkit:code-reviewer 等同 OMC priority; sustained 138+ batch B-02+B-03b+B-03c rounds 01-12 100% PASS post-fix empirical quality).
- **v1.9.3 §F-1..F-3 codifications**: SUSTAINED VALIDATED — round 10-12 cumulative 794 atoms 0 §F-1/F-2/F-3 violation post v1.9.3 cut.
- **Schema v1.2.1**: SUSTAINED status (post round 12 0 schema regression; v1.3 promote 暂搁置 carry to v2.0 candidate stack).

═══════════════════════════════════════════════════════════════════
## v1.9.4 candidate stack consolidation (7 actionable candidates → 4 NEW G-rules)
═══════════════════════════════════════════════════════════════════

| # | Candidate | Severity | Codification |
|---|-----------|----------|--------------|
| 1 | §F-1 descriptive-title H3 7th cumulative case (3 distinct title pattern types) | HIGH | **§G-1 NEW** |
| 2 | §2.4 multi-slice atom_id 续号 3rd production trigger (TA/ex 3-slice round 12) | HIGH | **§G-2 NEW** |
| 3 | §F-2 de-figure-naive formula 2 consecutive FIGURE-heavy rounds (11+12) sustained | STANDARD | **§G-3 NEW (PROMOTE)** |
| 4 | §2.6 FIGURE-heavy 20-block single-round NEW peak validated (TA/ex round 12) | INFO | **§G-4 NEW** |
| 5 | C-R12-07 FIGURE build-script trailing-newline defensive recipe | INFO | folded into §G-4 |
| 6 | C-R12-05 FIGURE-heavy estimate adjustment empirical formula | INFO | folded into §G-4 |
| 7 | C-R12-06 small-file naive estimate edge case | INFO | superseded by §G-4 (general FIGURE adjustment covers small-file case) |

**Net**: 7 candidates → 4 NEW G-rules (2 HIGH §G-1/G-2 + 1 STANDARD §G-3 + 1 INFO §G-4 with embedded sub-recipes).

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.9 | 2026-04-29 | post P2 Pilot 2-attempt cycle: 8 NEW patches C-1..C-8. N21 全 ban writer-family 扩到 MD-side. |
| v1.9.1 | 2026-05-05 | post P2 B-02 cycle CLOSED + cumulative audit GREEN-LIGHT 30/30=100%: 8 NEW D-rules consolidating 19 candidate stack. 3 NEW hooks. MD-side hooks 22 → 25. |
| v1.9.2 | 2026-05-06 | post P2 B-03c rounds 01-06 CLOSED + ★ 跨 50% domain coverage milestone: 6 NEW E-rules consolidating 10 candidate stack. 5 NEW hooks. MD-side hooks 25 → 28. |
| v1.9.3 | 2026-05-07 | post P2 B-03c rounds 07-09 CLOSED + ★ §2.11 Plan B 2nd production validation 4 cases including References boundary: 3 NEW F-rules consolidating 10-candidate stack. 2 NEW hooks. MD-side hooks 28 → 30. |
| **v1.9.4** | **2026-05-11** | **post P2 B-03c rounds 10-12 CLOSED + ★ §F-1 descriptive-title H3 7th cumulative case (3 distinct title pattern types) + §2.4 multi-slice 续号 3rd production STRONGLY VALIDATED + §F-2 de-figure-naive 2-round sustained + §2.6 FIGURE-heavy 20-block NEW peak**: 4 NEW G-rules consolidating 7-candidate stack (2 HIGH §G-1 descriptive-title H3 + §G-2 multi-slice 续号 + 1 STANDARD §G-3 de-figure-naive PROMOTE + 1 INFO §G-4 FIGURE-heavy estimate + build-script defensive). 3 NEW hooks (Hook G-1 + G-2 + G-3). MD-side hooks 30 → 33. v1.9.3 archived `archive/v1.9.3_final_2026-05-11/`. **Backward compatible** — rounds 10-12 production atoms 794 cumulative (182+208+404) byte-exact preserved. |
