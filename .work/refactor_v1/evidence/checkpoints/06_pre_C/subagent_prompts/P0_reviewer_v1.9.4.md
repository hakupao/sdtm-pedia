# P0 Reviewer — Rule A + Rule D 审阅 prompt v1.9.4

> Version: v1.9.4 (2026-05-11, post P2 B-03c rounds 10-12 cycle CLOSED + ★ §F-1 descriptive-title H3 7th cumulative case + §2.4 multi-slice 续号 3rd production STRONGLY VALIDATED + §F-2 de-figure-naive 2-round sustained + §2.6 FIGURE-heavy 20-block NEW peak + cumulative 9906 atoms post round 12)
> 基于 v1.9.3 (2026-05-07) + B-03c rounds 10-12 evidence (`evidence/checkpoints/` + `_progress.json` `b_03c_round_{10,11,12}_details`)
> 角色: Reviewer (Rule A 语义抽检 + Rule D 端到端审), 独立 subagent, ≠ writer subagent_type
> v1.9.4 变更: paired-sync with writer + matcher v1.9.4 §G-1..G-4. **核心**: 3 NEW G-rule audit checks — §R-G-1 §F-1 descriptive-title H3 title-agnostic verify (HIGH) + §R-G-2 §2.4 multi-slice atom_id 续号 cross-slice verify (HIGH) + §R-G-3 §F-2 de-figure-naive ratio STANDARD computation + §R-G-4 INFO FIGURE-heavy estimate adjustment retrospective.

## 角色硬约束 (v1.7/v1.8/v1.9/v1.9.1/v1.9.2/v1.9.3 carry-forward)

参 `archive/v1.7_final_2026-04-30/P0_reviewer_v1.7.md`.
参 `archive/v1.9.2_final_2026-05-07/P0_reviewer_v1.9.2.md` §R-E1..E-6 全文.
参 `archive/v1.9.3_final_2026-05-11/P0_reviewer_v1.9.3.md` §R-F-1..F-3 全文 (§R-F-1 §2.11 Plan B 4-layer verify + §R-F-2 atoms/line ratio retrospective + §R-F-3 kickoff estimate calibration).

═══════════════════════════════════════════════════════════════════
## v1.9.4 NEW PATCHES (Reviewer-relevant subset of writer §G-1..G-4)
═══════════════════════════════════════════════════════════════════

### §R-G-1 §F-1 descriptive-title H3 title-agnostic audit verify (HIGH)

**Rule**: For batches with §F-1 trigger (numberless H2 with H3 children) containing descriptive-title H3s (i.e., neither `### Example N` nor `### References` pattern), audit verifies namespace shape `§<D>.<N>.<K> [<literal full H3 title>]` per writer §G-1 codification.

Three validated H3 title pattern types (writer §G-1):

| H3 title pattern | Example | Namespace shape |
|------------------|---------|------------------|
| `### Example N` | `### Example 1` | `§<D>.<N>.<K>` |
| `### References` | `### References` | `§<D>.<N>.<K> [References]` |
| **Descriptive arbitrary** | `### Granularity of Trial Elements` | `§<D>.<N>.<K> [<descriptive full title>]` |

All three pattern types MUST use identical sib_idx-based namespace shape with **literal full H3 title** in brackets.

**Emit FAIL_PLAN_B_NAMESPACE_DESCRIPTIVE_TITLE** if any of the following found → HIGH severity HALT:
- Title-slug-based namespace (e.g., `§TE.4.granularity` instead of `§TE.4.1 [Granularity of Trial Elements]`)
- Title-abbreviated bracket (e.g., `§TE.4.1 [Granularity]` instead of `§TE.4.1 [Granularity of Trial Elements]`)
- Title-translated/summarized bracket (e.g., `§TE.4.1 [TE Granularity Section]` instead of literal title)

**Verify method**: Reviewer Bash `python3 -c "..."` script:
```python
import json, re
atoms = [json.loads(l) for l in open(f)]
# Identify H3 atoms (heading_level=3)
# For each H3, verify parent_section format: r'§<D>\.<N>\.<K> \[<literal_h3_title>\]'
# Confirm bracket content matches H3's source line literal title (no slug, no abbrev)
```

**Specific anti-patterns to detect**:
- ❌ Bracket content slugified (any `[<title_slug>]` like underscored lowercase)
- ❌ Bracket content truncated to first N chars (any descriptive title with length-cap suspicious)
- ❌ Bracket content translated/summarized (compare bracket literal to source H3 title line)

**Reviewer summary block**: When §G-1 trigger fires (descriptive-title H3 present), include explicit `§G-1 descriptive-title H3 verification` section:
| H2 | H3 title | Pattern type | Namespace shape | Literal title preserved | PASS/FAIL |

**Hook R-G-1 NEW**: §F-1 descriptive-title H3 title-agnostic verify — runs on round-close mini-audit + per-batch trigger detection. HALT 优先级 ≥ §R-F-1.

**Cumulative empirical baseline post round 12**: 7 cumulative cases × 3 distinct title pattern types validated (Example N + References + Descriptive). 0 violation in production.

### §R-G-2 §2.4 multi-slice atom_id 续号 cross-slice audit verify (HIGH)

**Rule**: For multi-slice batches (slice B/C of a §2.4 split source file), audit verifies cross-slice atom_id continuation per writer §G-2 codification:

1. **atom_id suffix continuation**: First atom in slice B/C MUST have suffix = (last atom suffix in prior slice) + 1. NOT `a001` reset.
2. **sib_idx continuation within same H2 scope**: If slice boundary falls mid-H2 scope, first atom in next slice within same scope MUST continue cumulative sib_idx (NOT reset to 1).
3. **No atom_id collision**: grep cross-slice atom_id list, verify zero overlap.

**Emit FAIL_MULTI_SLICE_CONTINUATION** if any check fails → HIGH severity HALT (would cause atom_id collision / file-scope namespace duplicate post-merge).

**Verify method**: Reviewer Bash script:
```python
import json
prior = [json.loads(l) for l in open(prior_slice_path)]
curr = [json.loads(l) for l in open(curr_batch_path)]

# Check 1: atom_id continuation
prior_last_suffix = int(prior[-1]['atom_id'].split('_a')[-1])
curr_first_suffix = int(curr[0]['atom_id'].split('_a')[-1])
assert curr_first_suffix == prior_last_suffix + 1, \
    f"FAIL multi-slice atom_id: prior last=a{prior_last_suffix}, curr first=a{curr_first_suffix}"

# Check 2: No atom_id collision
prior_ids = {a['atom_id'].split('_a')[-1] for a in prior}
curr_ids = {a['atom_id'].split('_a')[-1] for a in curr}
overlap = prior_ids & curr_ids
assert not overlap, f"FAIL atom_id collision: {overlap}"

# Check 3: sib_idx continuation (if same H2 scope continues into curr)
# Compare prior[-1]['parent_section'] H2-scope vs curr[0]['parent_section']
# If same H2 scope: assert curr[0]['sibling_index'] > prior[-1]['sibling_index']
```

**Specific anti-patterns to detect**:
- ❌ atom_id reset to `a001` at start of slice B/C
- ❌ sib_idx reset to 1 when same H2 scope spans the slice boundary
- ❌ atom_id list shows gap (e.g., a113 then a115, skipping a114) — should be perfect sequential
- ❌ Hard-coded slice marker in atom_id (e.g., `<batch>_sliceB_a001` form)

**Reviewer summary block**: When §G-2 trigger fires (multi-slice slice B/C), include explicit `§G-2 multi-slice 续号 verification`:
| Slice | First atom_id | Prior last | sib_idx continuation | atom_id collision | PASS/FAIL |

**Hook R-G-2 NEW**: §2.4 multi-slice atom_id 续号 cross-slice verify — runs on round-close mini-audit when multi-slice batches present. HALT 优先级 HIGH.

**Cumulative empirical baseline post round 12**: 3 cumulative production triggers (round 03 + B-02 + round 12 TA/ex 3-slice). 0 violation; all 3 PASS file-scope atom_id continuity post-merge.

### §R-G-3 §F-2 de-figure-naive ratio STANDARD recipe (STANDARD)

**Rule**: §F-2 atoms/line ratio band — PROMOTED from INFO (v1.9.3) to STANDARD (v1.9.4). When N_fig ≥ 1 (FIGURE atoms present in batch/round), reviewer MUST compute de-figure-naive ratio per writer §G-3 formula:

```
de_figure_ratio = N_atoms / (total_source_lines − Σfig_span + N_fig)
```

Reviewer round-close mini-audit verifies cumulative round **de-figure** ratio (not naive) is within empirical band 0.59-0.85 when round has any FIGURE atoms. If outside band → INFO finding (NOT halt) — investigate driver.

**When to apply (reviewer decision table)**:

| Condition | Ratio used |
|-----------|------------|
| `N_fig == 0` across round | naive ratio (apply band) |
| `N_fig ≥ 1` across round | **de-figure ratio (STANDARD; apply band)** |

**Verify method**: Reviewer aggregates per-batch checkpoints:
```python
import json, glob
total_atoms = 0
total_lines = 0
total_fig_span = 0
total_n_fig = 0
for cp in glob.glob("evidence/checkpoints/batch_*.json"):
    data = json.load(open(cp))
    total_atoms += data['atom_count']
    total_lines += data['source_lines']
    total_fig_span += data.get('fig_span_sum', 0)
    total_n_fig += data.get('n_fig', 0)
if total_n_fig >= 1:
    adjusted = total_lines - total_fig_span + total_n_fig
    defigure_ratio = total_atoms / adjusted
    # Apply band 0.59 <= defigure_ratio <= 0.85
else:
    naive_ratio = total_atoms / total_lines
```

**Empirical baseline rounds 11+12** (2 consecutive FIGURE-heavy rounds):
- Round 11: naive 0.479 (outside band, misleads) vs de-figure **0.698 in band**
- Round 12: naive 0.443 (outside band, misleads) vs de-figure **0.714 in band**

**Hook R-G-3 NEW STANDARD (replaces Hook R-F-2 INFO)**: de-figure ratio retrospective check — STANDARD when N_fig ≥ 1; carry-forward INFO non-blocking only when ratio is OUTSIDE band post de-figure adjustment.

### §R-G-4 §2.6 FIGURE-heavy domain estimate adjustment retrospective (INFO)

**Rule**: Round-close mini-audit for domains with ≥10 FIGURE atoms (FIGURE-heavy threshold per writer §G-4) — confirm adjusted-lines estimate was used in kickoff:

```
adjusted_lines = total_lines − Σfig_span + N_fig
mid_estimate = adjusted_lines × 0.73
```

If kickoff used naive estimate (`total_lines × 0.73`) and naive overstated actual by >50%, INFO carry-forward note (kickoff calibration improvement opportunity for future FIGURE-heavy domains).

**Verify method**: Compare kickoff §X estimate (text-extracted) vs actual atom count. If kickoff used naive AND `naive_estimate / actual > 1.5` AND `N_fig ≥ 10` → INFO finding.

**Empirical TA/ex worked example (round 12)**:
- naive: 911 × 0.73 = 665 atoms estimate
- adjusted: 566 × 0.73 = 413 atoms estimate
- actual: 404 atoms (98% of adjusted mid; 61% of naive mid — naive overstates by 64%)

**FIGURE build-script defensive recipe (C-R12-07)**: Reviewer post-DONE sweeps mermaid atom bodies for double-newline patterns (`\n\n` between mermaid lines that should be `\n` only). If detected, INFO finding pointing to build-script trailing-newline issue.

**Hook R-G-4 NEW INFO**: FIGURE-heavy estimate adjustment retrospective + mermaid double-newline sweep — both non-blocking INFO carry-forward.

### §R-F-1..F-3 carry-forward (v1.9.3 unchanged)

ALL v1.9.3 §R-F-1..F-3 rules carry-forward to v1.9.4 unchanged (extended by §R-G-1..G-4 above; §R-F-1 explicitly extended by §R-G-1 descriptive-title; §R-F-2 promoted to STANDARD §R-G-3):
- §R-F-1 HIGH §2.11 Plan B 4-layer namespace verify — extended by §R-G-1 (descriptive-title H3)
- §R-F-2 INFO atoms/line ratio retrospective — **PROMOTED to STANDARD §R-G-3 de-figure recipe**
- §R-F-3 INFO Kickoff atom estimate calibration retrospective — unchanged

### §R-E1..E-6 carry-forward (v1.9.2 unchanged)

参 `archive/v1.9.2_final_2026-05-07/P0_reviewer_v1.9.2.md` for §R-E1..E-6 full text.

### §R-D1..D-8 carry-forward (v1.9.1 unchanged)

参 `archive/v1.9.1_final_2026-05-06/P0_reviewer_v1.9.1.md` for §R-D1..D-8 full text.

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (reviewer v1.7 18 + v1.9 2 + v1.9.1 6 + v1.9.2 6 + v1.9.3 3 + v1.9.4 3 = 38 hooks)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- v1.9 NEW Hook R22 + R23 carry-forward
- v1.9.1 NEW Hook R24 + R-D2..R-D6 carry-forward
- v1.9.2 NEW Hook R25 + R-E2..R-E6 carry-forward
- v1.9.3 NEW Hook R-F-1 + R-F-2 + R-F-3 carry-forward (Hook R-F-2 promoted to Hook R-G-3 STANDARD recipe)
- **v1.9.4 NEW Hook R-G-1**: §F-1 descriptive-title H3 title-agnostic verify (HIGH); HALT 优先级 ≥ §R-F-1 when §G-1 trigger fires
- **v1.9.4 NEW Hook R-G-2**: §2.4 multi-slice atom_id 续号 cross-slice verify (HIGH); HALT 优先级 HIGH when multi-slice slice B/C present
- **v1.9.4 NEW Hook R-G-3**: §F-2 de-figure-naive ratio STANDARD recipe (replaces R-F-2 INFO when N_fig ≥ 1; INFO only when outside band post de-figure adjustment)
- (Hook R-G-4 N/A explicit — folded as INFO sub-check within R-G-3 + post-DONE mermaid double-newline sweep)

**Reviewer hook 总数**: 35 (v1.9.3) + 3 NEW (v1.9.4) = **38 hooks**.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.4 sync with B-03c rounds 10-12 cycle evidence)
═══════════════════════════════════════════════════════════════════

- **30-atom inter-cycle stratified standard**: SUSTAINED (B-01 + B-02 + B-03c rounds 01-12 12 cumulative cycles validated)
- **B-03c rounds 10-12 cycle 100% strict PASS post-fix**: SUSTAINED — 0 HIGH NEW findings post mini-audits each round (round 10 first under v1.9.3 0 HALT + round 11 0 HALT FIGURE-introduction round + round 12 0 HALT FIGURE-heavy 20-block peak); preventive layers (Hook 22b + 22c + R25 + D-rules + E-rules + F-rules + G-rules codify) effectively prevented systemic drift across 794 atoms cumulative post v1.9.3 cut
- **Rule D 隔离硬约束 STRONGLY VALIDATED EXTENDED**: B-01 + B-02 + B-03c 138+ batches sustained writer ≠ reviewer subagent_type 0 violation
- **§F-1 §2.11 Plan B descriptive-title H3 title-agnostic**: NEW STATUS CODIFIED §R-G-1 (7 cumulative cases × 3 distinct title pattern types validated; rule stable for v1.9.4 baseline)
- **§2.4 multi-slice atom_id 续号**: NEW STATUS CODIFIED §R-G-2 — promoted from implicit to first-class formal codification (3 cumulative production triggers STRONGLY VALIDATED)
- **§F-2 → §G-3 de-figure-naive STANDARD recipe**: PROMOTED from INFO to STANDARD (2 consecutive FIGURE-heavy rounds 11+12 sustained)
- **§2.6 FIGURE-heavy estimate adjustment**: NEW STATUS CODIFIED §R-G-4 INFO retrospective (20-block NEW peak validated; build-script defensive recipe C-R12-07 codified)
- **Schema regression sweep PRIORITY 1**: SUSTAINED (round 06 batch_72 4-schema-regression caught + post v1.9.3 cut 794 atoms 0 schema regression cumulative)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.9.1 | 2026-05-05 | post P2 B-02 cycle CLOSED paired-sync: 7 NEW rules §R-D1..D-8. 6 NEW hooks. Reviewer hooks 20 → 26. |
| v1.9.2 | 2026-05-06 | post P2 B-03c rounds 01-06 CLOSED: 6 NEW E-rules §R-E1..E-6. 6 NEW hooks. Reviewer hooks 26 → 32. |
| v1.9.3 | 2026-05-07 | post P2 B-03c rounds 07-09 CLOSED: 3 NEW F-rules audit checks §R-F-1..F-3. 3 NEW hooks. Reviewer hooks 32 → 35. |
| **v1.9.4** | **2026-05-11** | **post P2 B-03c rounds 10-12 CLOSED + ★ §F-1 descriptive-title H3 7th cumulative case (3 distinct title pattern types) + §2.4 multi-slice 续号 3rd production STRONGLY VALIDATED + §F-2 → §G-3 de-figure-naive STANDARD recipe + §2.6 FIGURE-heavy 20-block NEW peak**: paired-sync with writer_md/pdf/matcher v1.9.4. 3 NEW G-rule audit checks §R-G-1..G-3 (2 HIGH §R-G-1 descriptive-title H3 + §R-G-2 multi-slice 续号 + 1 STANDARD §R-G-3 de-figure-naive promote, with embedded §R-G-4 INFO FIGURE-heavy retrospective). 3 NEW hooks R-G-1/G-2/G-3. Reviewer hooks 35 → 38. v1.9.3 archived. **Backward compatible** — B-02 + B-03c rounds 01-12 production atoms 9906 cumulative byte-exact preserved. |
