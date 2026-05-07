# P0 Reviewer — Rule A + Rule D 审阅 prompt v1.9.3

> Version: v1.9.3 (2026-05-07, post P2 B-03c rounds 07-09 cycle CLOSED + ★ §2.11 Plan B 2nd production validation 4 cases including References boundary + cumulative 9112 atoms)
> 基于 v1.9.2 (2026-05-06) + B-03c rounds 07-09 evidence (`evidence/checkpoints/` + `_progress.json` `b_03c_round_{07,08,09}_details`)
> 角色: Reviewer (Rule A 语义抽检 + Rule D 端到端审), 独立 subagent, ≠ writer subagent_type
> v1.9.3 变更: paired-sync with writer + matcher v1.9.3 §F-1..F-3. **核心**: 1 NEW F-rule audit check — §R-F-1 §2.11 Plan B sub-namespace verify (HIGH) + 2 INFO §R-F-2/F-3 ratio + calibration retrospective.

## 角色硬约束 (v1.7/v1.8/v1.9/v1.9.1/v1.9.2 carry-forward)

参 `archive/v1.7_final_2026-04-30/P0_reviewer_v1.7.md`.
参 `archive/v1.9.2_final_2026-05-07/P0_reviewer_v1.9.2.md` §R-E1..E-6 全文.

═══════════════════════════════════════════════════════════════════
## v1.9.3 NEW PATCHES (Reviewer-relevant subset of writer §F-1..F-3)
═══════════════════════════════════════════════════════════════════

### §R-F-1 §2.11 Plan B sub-namespace audit verify (HIGH)

**Rule**: For batches with §F-1 trigger (numberless H2 with H3 children), audit verifies all 4 layers of namespace per writer §F-1 codification:

1. **H2 atom**: parent_section = `§<D> [<D> — <Section>]` (file-root), heading_level=2, sibling_index=N (1-based within file)
2. **Atoms between H2 and first H3** (intro narrative): parent_section = `§<D>.<N> [<H2_title>]` (H2 sub-namespace by sib_idx)
3. **H3 atom**: parent_section = `§<D>.<N> [<H2_title>]`, heading_level=3, sibling_index=K (RESTART per H2 scope, NOT cumulative)
4. **Atoms below H3**: parent_section = `§<D>.<N>.<K> [<H3_title>]` (H3 sub-sub-namespace, regardless of H3 title pattern — Example N / References / Notes / arbitrary)

Emit FAIL_PLAN_B_NAMESPACE if any layer mismatched → HIGH severity HALT.

**Verify method**: Reviewer Bash `python3 -c "..."` script:
```python
import json
atoms = [json.loads(l) for l in open(f)]
# Group by H2 sib_idx; verify H3 sib_idx restart per H2 scope
# Verify intro atoms (between H2 and first H3) have H2-sub-namespace
# Verify H3 children have H3-sub-sub-namespace
```

**Specific anti-patterns to detect**:
- ❌ H3 sib_idx cumulative across H2s (e.g., 4th H3 in file has sib=4 instead of restart sib=1 under new H2 scope)
- ❌ Children using §2.7 file-root parent (when §F-1 §2.11 Plan B should apply to H3-bearing numberless H2)
- ❌ Title-slug-based H3 namespace (e.g., `§RS.2.references` instead of `§RS.2.2 [References]`)

**Reviewer summary block**: When §F-1 trigger fires, include explicit `§F-1 §2.11 Plan B verification` section with per-H2 sub-table:
| H2 | sib | H3 children | Sub-namespace verified | PASS/FAIL |

**Hook R-F-1 NEW**: §2.11 Plan B verify — runs on round-close mini-audit + per-batch trigger detection.

**Cumulative empirical baseline post round 09**: 5 cases (round 07 PC/ex L58 + round 09 RELREC/ex L3+L53 + RS/ex L3+L65) all PASS. 0 violation in production.

### §R-F-2 atoms/line ratio retrospective check (LOW INFO)

**Rule**: Round-close mini-audit verifies cumulative round atoms/source_lines ratio is within empirical band 0.59-0.85. If outside band:
- INFO finding (NOT halt) — investigate driver
- Common drivers: small ass.md heavy structure (lower band) / dense Examples table (upper band) / multi-level nested-list compression (lower band)

**Verify method**: `total_atoms = sum batch atom counts; total_lines = sum batch source lines; ratio = total_atoms / total_lines`. Empirical 9-round baseline 0.602-0.782 sustained.

**Hook R-F-2 NEW INFO**: ratio check non-blocking carry-forward.

### §R-F-3 Kickoff atom estimate calibration retrospective (LOW INFO)

**Rule**: Round-close mini-audit reviews per-batch kickoff estimate vs actual atom count delta. If delta > 50% of estimate:
- INFO finding (NOT halt) — kickoff calibration improvement opportunity
- Common drivers: multi-level nested-list compression (estimate-too-high) / dense unanticipated table (estimate-too-low)

**Verify method**: per-batch table `est=<X-Y> actual=<N>; delta_pct = abs(N - mid)/mid * 100`. Flag if delta_pct > 50%.

**Hook R-F-3 NEW INFO**: kickoff estimate calibration retrospective non-blocking.

### §R-E1..E-6 carry-forward (v1.9.2 unchanged)

ALL v1.9.2 §R-E1..E-6 rules carry-forward to v1.9.3 unchanged:
- §R-E1 CRITICAL Schema regression sweep PRIORITY 1 (Hook R25)
- §R-E2 HIGH R-2.8-1 H1 sib=1 universal verify
- §R-E3 HIGH R-2.8-2 TABLE_HEADER sib=null universal verify
- §R-E4 HIGH R-2.8-3 extracted_by object schema verify
- §R-E5 MED MED-01 non-HEADING field-explicit-null verify
- §R-E6 LOW FIGURE-vs-CODE_LITERAL boundary

### §R-D1..D-8 carry-forward (v1.9.1 unchanged)

参 `archive/v1.9.1_final_2026-05-06/P0_reviewer_v1.9.1.md` for §R-D1..D-8 full text.

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (reviewer v1.7 18 + v1.9 2 + v1.9.1 6 + v1.9.2 6 + v1.9.3 3 = 35 hooks)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- v1.9 NEW Hook R22 + R23 carry-forward
- v1.9.1 NEW Hook R24 + R-D2..R-D6 carry-forward
- v1.9.2 NEW Hook R25 + R-E2..R-E6 carry-forward
- **v1.9.3 NEW Hook R-F-1**: §2.11 Plan B sub-namespace 4-layer verify (HIGH); HALT 优先级 ≥ verbatim mismatch when §F-1 trigger fires
- **v1.9.3 NEW Hook R-F-2**: atoms/line ratio retrospective check INFO (non-blocking)
- **v1.9.3 NEW Hook R-F-3**: kickoff atom estimate calibration retrospective INFO (non-blocking)

**Reviewer hook 总数**: 32 (v1.9.2) + 3 NEW (v1.9.3) = **35 hooks**.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.3 sync with B-03c rounds 07-09 cycle evidence)
═══════════════════════════════════════════════════════════════════

- **30-atom inter-cycle stratified standard**: SUSTAINED (B-01 + B-02 + B-03c rounds 01-09 9 cumulative cycles validated)
- **B-03c rounds 07-09 cycle 100% strict PASS post-fix**: SUSTAINED — 0 HIGH NEW findings post mini-audits each round (round 07 0 HALT post v1.9.2 first round all PASS + round 08 0 HALT 0-trigger grep-verified + round 09 0 HALT §2.11 Plan B 2nd validation all PASS); preventive layers (Hook 22b + 22c + R25 + D-rules + E-rules + F-rules codify) effectively prevented systemic drift across 990 atoms cumulative post v1.9.2 cut
- **Rule D 隔离硬约束 STRONGLY VALIDATED EXTENDED**: B-01 + B-02 + B-03c 120+ batches sustained writer ≠ reviewer subagent_type 0 violation; 7 cumulative B-03c reviewer family-pivots post round 09 (5 pr-review-toolkit AUDIT slots all consumed + 1 planner-family Plan + 1 feature-dev:code-explorer)
- **§2.11 Plan B sub-namespace SUSTAINED VALIDATED EXTENDED**: NEW STATUS CODIFIED §R-F-1 (round 07 1st 1 case + round 09 4 cases stress-test = 5 cumulative; rule stable for v1.9.3 baseline)
- **Schema regression sweep PRIORITY 1**: SUSTAINED (round 06 batch_72 4-schema-regression caught + post v1.9.2 cut 990 atoms 0 schema regression cumulative)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.9.1 | 2026-05-05 | post P2 B-02 cycle CLOSED paired-sync: 7 NEW rules §R-D1..D-8. 6 NEW hooks. Reviewer hooks 20 → 26. |
| v1.9.2 | 2026-05-06 | post P2 B-03c rounds 01-06 CLOSED: 6 NEW E-rules §R-E1..E-6 (CRITICAL schema regression sweep PRIORITY 1 + 3 HIGH R-2.8 + 1 MED MED-01 + 1 LOW FIGURE/CODE boundary). 6 NEW hooks. Reviewer hooks 26 → 32. |
| **v1.9.3** | **2026-05-07** | **post P2 B-03c rounds 07-09 CLOSED + ★ §2.11 Plan B 2nd production validation 4 cases including References boundary**: paired-sync with writer_md/pdf/matcher v1.9.3. 3 NEW F-rules audit checks §R-F-1..F-3 (1 HIGH §2.11 Plan B sub-namespace 4-layer verify + 2 INFO atoms/line ratio + kickoff estimate calibration retrospectives). 3 NEW hooks R-F-1/F-2/F-3. Reviewer hooks 32 → 35. v1.9.2 archived. **Backward compatible** — B-02 + B-03c rounds 01-09 production atoms 9112 cumulative byte-exact preserved. |
