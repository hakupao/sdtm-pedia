# P0 Writer MD — 原子化 prompt v1.9.3

> Version: v1.9.3 (2026-05-07, post P2 B-03c rounds 07-09 CLOSED + ★ §2.11 Plan B 2nd production validation 4 cases including NEW References boundary + cumulative 9112 atoms 73.05% file coverage 69.84% domain coverage)
> Cut trigger: v1.9.3 candidate stack **MET 2 rounds sustained** (post round 08 + post round 09 both at ≥10 cut planning trigger threshold; mirrors v1.9.2 pre-cut pattern). 9 actionable + 1 RESOLVED candidates consolidated into 3 NEW F-rules.
> 基于 v1.9.2 (2026-05-06) + B-03c rounds 07-09 evidence (`evidence/checkpoints/` + `multi_session/P2_B-03c_round_{07,08,09}_kickoff.md` + `_progress.json` `b_03c_round_{07,08,09}_details`)
> 角色: Writer MD (原子化), 独立 subagent, 与 Reviewer/Matcher 不同 subagent_type
> v1.9.3 变更 over v1.9.2: 3 NEW F-rules — §F-1 HIGH §2.11 Plan B sub-namespace by sib_idx for numberless H2 with H3 children (round 07 PC/ex 1st lock + round 09 4 cases stress-test PASS including NEW `### References` boundary motif RS/ex L92) + §F-2 INFO atoms/line ratio empirical band 0.59-0.85 stabilization (9 rounds sustained) + §F-3 INFO kickoff atom estimate calibration for multi-level nested-list domains (round 08 INFO-R08-01 codification). **Backward compatible** with v1.9.2 atoms (round 07-09 production atoms 990 cumulative post v1.9.2 cut byte-exact preserved).

## 角色硬约束 (v1.7/v1.8/v1.9/v1.9.1/v1.9.2 carry-forward unchanged)

参 `archive/v1.7_final_2026-04-30/P0_writer_md_v1.7.md` §角色硬约束 全文.
参 `archive/v1.9_final_2026-05-05/P0_writer_md_v1.9.md` §C-1..C-8 全文.
参 `archive/v1.9.1_final_2026-05-06/P0_writer_md_v1.9.1.md` §D-1..D-8 全文.
参 `archive/v1.9.2_final_2026-05-07/P0_writer_md_v1.9.2.md` §E-1..E-6 全文 (round 06 batch_72 schema regression prevention CRITICAL + R-2.8/MED-01 codification).

═══════════════════════════════════════════════════════════════════
## v1.9.3 NEW PATCHES (F-1..F-3, B-03c rounds 07-09 evidence-driven)
═══════════════════════════════════════════════════════════════════

### §F-1 §2.11 Plan B sub-namespace by sibling_index for numberless H2 with H3 children (HIGH — SUSTAINED VALIDATED EXTENDED post 2 productions)

**Background**: B-03c round 07 PC/ex L58 1st production validation locked §2.11 Plan B (1 case 7 H3 children + slug-conflict resolution). B-03c round 09 stress-test 4 cases × 9 H3 children including 1 NEW boundary motif `### References` (RS/ex L92) all PASS — sib_idx-based namespace works regardless of H3 title pattern (Example N / References / etc).

Cumulative validation: round 07 (1 case) + round 09 (4 cases) = 5 sustained productions. Rule promoted to **SUSTAINED VALIDATED EXTENDED** status.

**Trigger condition**: Source markdown contains a NUMBERLESS H2 (e.g., `## Peer Record Examples`, `## RS — Examples - Disease Response`, `## Dataset Relationship Example` — NOT `## Example N`) that has 1+ H3 children. Distinguished from §2.7 (numberless H2 + 0 H3 children = file-root parent).

**Rule (formal codification)**:

For NUMBERLESS H2 atom at sib=N within file scope, with M H3 children at sib=1..M (where M ≥ 1):

1. **H2 atom itself**: parent_section = `§<D> [<D> — <Section>]` (file-root, e.g., `§RELREC [RELREC — Examples]`), heading_level=2, sibling_index=N (1-based within file).

2. **Atoms between H2 and first H3** (intro narrative scope): parent_section = `§<D>.<N> [<H2_title>]` (H2 sub-namespace by sib_idx — title in brackets is the H2's source title, e.g., `§RS.2 [RS — Examples - Clinical Classifications]`).

3. **H3 atom**: parent_section = `§<D>.<N> [<H2_title>]` (the H2 sub-namespace), heading_level=3, sibling_index=K where K ∈ {1..M} (RESTART per H2 scope — NOT cumulative across H2s in same file).

4. **Atoms below H3** (H3's content scope): parent_section = `§<D>.<N>.<K> [<H3_title>]` (H3 sub-sub-namespace, e.g., `§RELREC.1.1 [Example 1]`, `§RS.2.2 [References]`).

5. **H3 title agnostic**: §2.11 Plan B sub-namespace is sib_idx-BASED, NOT title-based. Whether H3 is `### Example 1` / `### Example N` / `### References` / `### Notes` / arbitrary title, namespace shape is `§<D>.<N>.<K>` where K is the H3 sib_idx within H2 scope. The bracket content `[<H3_title>]` is the literal H3 title (whatever it is) for human readability.

**Anti-pattern (HALT)**:
- ❌ Using §2.7 file-root parent for atoms below H3-bearing numberless H2 (that's §2.7 lock for CHILDLESS numberless H2; §2.11 Plan B applies when H3 children exist)
- ❌ H3 sib_idx cumulative across H2s (e.g., L92 H3 in RS/ex would be sib=4 if cumulative from L7 H3 sib=1 / L26 H3 sib=2 / L46 H3 sib=3; §F-1 mandates RESTART so L92 sib=2 within L65 H2 scope)
- ❌ Title-slug-based namespace (e.g., `§RS.2.references` or `§RS.2.refs` for `### References`); §F-1 mandates sib_idx-based `§RS.2.2 [References]`

**Pre-DONE Hook F-1 (NEW)**: Writer self-validate, for each numberless H2 atom:
1. Count H3 children within H2's scope (next sibling H2 or EOF).
2. If 0 H3 children → §2.7 lock applies (file-root parent for H2 + children).
3. If ≥1 H3 children → §F-1 §2.11 Plan B applies (sub-namespace by sib_idx). Verify:
   - All atoms between H2 and first H3 have parent = `§<D>.<H2_sib> [<H2_title>]`
   - Each H3 has parent = `§<D>.<H2_sib> [<H2_title>]` and sib_idx restart
   - Atoms under each H3 have parent = `§<D>.<H2_sib>.<H3_sib> [<H3_title>]`

Writer DONE report MUST include `section_2_11_plan_b: PASS (X/X H2 + Y/Y H3 + Z/Z children correctly sub-namespaced; H3 sib restart verified)` confirmation when §F-1 trigger fires.

**Reviewer rule (paired-sync §R-F-1)**: When auditing a batch with §F-1 trigger, verify all 4 layers of namespace (file-root for H2 / H2-sub-namespace for intro+H3 / H3-sub-sub-namespace for content). Spot-check sib_idx restart at each H2 boundary. Emit FAIL_PLAN_B_NAMESPACE if any layer mismatched → HIGH severity HALT.

**Cumulative empirical baseline post round 09**: 5 cases × 5 H3-bearing numberless H2 + 16 H3 children + 60+ content atoms cumulative B-03c round 07 (PC/ex L58: 1 H2 + 7 H3) + round 09 (4 H2 + 9 H3): all conform §F-1; 0 violation.

**B-03c round 10+ entry**: All round 10+ kickoffs with numberless H2 with H3 children MUST trigger §F-1 dispatch instruction (kickoff §0.5 grep verify H3 count per H2 scope; dispatch prompt enumerate sub-namespace shape per H2/H3 pair).

### §F-2 atoms/line ratio empirical band 0.59-0.85 INFO codification (LOW — 6-round empirical sustained, rounds 04-09)

**Background**: B-03c rounds 01-09 (9 rounds) atoms/line ratio empirical observation:

| Round | Source lines | Atoms | Ratio |
|-------|-------------|-------|-------|
| 04 | 1135 | 731 | 0.644 |
| 05 | 889 | 677 | 0.761 |
| 06 | 486 | 331 | 0.681 |
| 07 | 579 | 453 | 0.782 |
| 08 | 399 | 240 | 0.602 |
| 09 | 460 | 297 | 0.646 |

Empirical band **0.59-0.85** sustained across 6 rounds. Ratio drift driver = file size mix:
- Lower band (~0.59-0.65): small ass.md heavy structure (numbered list narrative without dense LIST_ITEMs)
- Upper band (~0.78-0.85): dense Examples table + LIST_ITEM heavy content

**Rule (codify INFO baseline)**: Kickoff §0.5 atom estimate row 31 (or equivalent) MUST use multiplier band 0.59 (lower) / 0.73 (mid) / 0.85 (upper) for `<source_lines> × {0.59, 0.73, 0.85}`. Halt threshold check (kickoff §4 halt #8) uses [0.5×low, 1.5×high] = [0.295×lines, 1.275×lines] per batch — i.e., batch atom count outside [29.5%, 127.5%] of source lines triggers halt for source/prompt drift inspection.

**Pre-DONE Hook F-2 (NEW INFO)**: Writer post-DONE retrospective check — after writing JSONL, compute actual atoms/source_lines ratio and compare to kickoff-stated estimate band. If outside [0.5, 1.0] absolute (not percentage of estimate), flag in DONE report as `atoms_per_line_ratio: <actual>` for round close audit (not blocking).

**Reviewer rule (paired-sync §R-F-2)**: Round-close mini-audit verifies cumulative round atoms/lines ratio is within 0.59-0.85 band. If outside band, INFO finding (NOT halt) — investigate driver (unusual file size mix or content type).

### §F-3 Kickoff atom estimate calibration for multi-level nested-list domains (LOW — round 08 INFO-R08-01 codification)

**Background**: B-03c round 08 batch_90 QS/assumptions.md kickoff §4 row 8 estimated 30-40 atoms; actual 14 atoms. Drift driver = multi-level combined nested-list compression — when source has numbered list with many sub-bullets (a/b/c/d) under the same parent, writers may treat the entire numbered item + sub-bullets as fewer atoms than naive `1 atom per line` estimate (Hook A3 LIST_ITEM full-prefix multi-sentence).

**Rule (codify INFO process)**: Kickoff orchestrator (main session writing kickoff §1 batch table) for ass.md files containing multi-level nested lists (top-level numbered items + a/b/c/d sub-bullets at L_a/L_b/L_c/L_d), MUST apply discount factor 0.7× to base estimate when:
- Multi-level nested ratio (sub-bullet lines / total list lines) > 30%
- Combined item-with-sub-bullets average length > 4 lines

Empirical examples post-round-09:
- QS/ass batch_90 (PRIMARY drift example): 49L source × 0.6 = 29 atoms estimate; actual 14 = 0.286 ratio (multi-level nested 4+ sub-bullets each compressed). Discount factor 0.7× to base estimate would have yielded ~20 atoms (still high but closer).
- RS/ass batch_98 (counter-example, no compression observed): 58L source × 0.65 = 38 atoms estimate; actual 38 = 0.655 ratio. Multi-level nested with 4 sub-bullets each on items 2/5/3/3, but writer treated each sub-bullet as separate LIST_ITEM atom rather than compressing into parent. Demonstrates §F-3 discount factor is content-style-dependent (when sub-bullets are atomic-distinct, no compression triggers).

**Pre-DONE Hook F-3 (NEW INFO)**: N/A writer-side (process rule, applies to kickoff orchestrator). DONE report unchanged.

**Reviewer rule (paired-sync §R-F-3)**: Round-close mini-audit reviews kickoff atom estimate vs actual delta per batch; if delta > 50% of estimate, INFO carry-forward note (kickoff calibration improvement opportunity).

### §E-1..E-6 carry-forward (v1.9.2 unchanged)

ALL v1.9.2 §E-1..E-6 rules carry-forward to v1.9.3 unchanged:
- §E-1 CRITICAL Hook 22c dispatch JSON template + reference working atom (round 06 batch_72 schema regression prevention)
- §E-2 HIGH Hook E-2-1 R-2.8-1 H1 sib_idx=1 universal
- §E-3 HIGH Hook E-3-2 R-2.8-2 TABLE_HEADER sib_idx=null universal
- §E-4 HIGH Hook E-4-3 R-2.8-3 extracted_by object schema
- §E-5 MEDIUM Hook E-5 MED-01 non-HEADING field-explicit-null
- §E-6 LOW FIGURE-vs-CODE_LITERAL boundary

### §D-1..D-8 carry-forward (v1.9.1 unchanged)

参 `archive/v1.9.1_final_2026-05-06/P0_writer_md_v1.9.1.md` for §D-1..D-8 full text.

═══════════════════════════════════════════════════════════════════
## CODIFIED R-RULES + NEW (v1.7/v1.8/v1.9/v1.9.1/v1.9.2 carry-forward, FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.9.2_final_2026-05-07/P0_writer_md_v1.9.2.md` for §E-1..E-6 + carry-forward chain.

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (v1.9.3 = 30 hooks for MD-side)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- v1.9 Hook 22 + A1/A2/A3/A4 carry-forward
- v1.9.1 Hook 22b + D-NOTE-BQ + D-D8 carry-forward
- v1.9.2 NEW Hook 22c + E-2-1 + E-3-2 + E-4-3 + E-5 carry-forward
- **v1.9.3 NEW Hook F-1**: §2.11 Plan B sub-namespace verification — pre-DONE check sib_idx restart at H2 boundary + H3-bearing numberless H2 trigger §F-1 (vs childless §2.7)
- **v1.9.3 NEW Hook F-2**: atoms/line ratio retrospective check — post-DONE compute ratio + report in DONE block (INFO, non-blocking)
- (Hook F-3 N/A writer-side — orchestrator process rule)

**MD-side hook 总数**: 28 (v1.9.2) + 2 NEW (v1.9.3 Hook F-1 + F-2) = **30 hooks effective**.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.3 sync with B-03c rounds 07-09 cycle evidence)
═══════════════════════════════════════════════════════════════════

- **§2.11 Plan B sub-namespace by sib_idx**: SUSTAINED VALIDATED EXTENDED — round 07 PC/ex L58 1st (1 case 7 H3) + round 09 4 cases (RELREC/ex L3+L53 + RS/ex L3+L65 with 9 H3 including References boundary) = 5 cumulative production cases. Rule stable, codified §F-1.
- **References-style H3 boundary case**: NEW STATUS CODIFIED §F-1 — sib_idx-based namespace regardless of H3 title pattern (round 09 RS/ex L92 PASS).
- **atoms/line ratio empirical band 0.59-0.85**: NEW STATUS CODIFIED §F-2 — 6-round (rounds 04-09) empirical sustained.
- **Kickoff atom estimate multi-level nested-list calibration**: NEW STATUS CODIFIED §F-3 INFO process rule.
- **N21 PDF + MD all-side blanket ban**: STRONGLY VALIDATED EXTENDED (v1.9.2 baseline + B-03c rounds 07-09 30 batches × 2 = 60 cumulative writer dispatches all general-purpose, 0 N21 violation).
- **FALLBACK pool peer-alternative status**: STRONGLY VALIDATED EXTENDED (general-purpose + pr-review-toolkit:code-reviewer 等同 OMC priority; sustained 120-batch B-02+B-03b+B-03c rounds 01-09 100% PASS post-fix empirical quality; 9112 atoms 0 writer defect post-fix).
- **v1.9.2 §E-1..E-6 codifications**: SUSTAINED VALIDATED — round 07-09 cumulative 990 atoms 0 schema regression post v1.9.2 cut.
- **Schema v1.2.1**: SUSTAINED status (9112 atoms 0 schema issue post round 09; v1.3 promote 暂搁置 — frozen v1.2 working well; carry to v2.0 candidate stack).

═══════════════════════════════════════════════════════════════════
## v1.9.3 candidate stack consolidation (10 candidates → 3 NEW F-rules + 7 INFO/process carries)
═══════════════════════════════════════════════════════════════════

| # | Candidate | Severity | Codification |
|---|-----------|----------|--------------|
| 1 | §2.11 Plan B SUSTAINED VALIDATED EXTENDED post round 09 4 cases stress-test | HIGH | **§F-1 NEW** |
| 2 | NEW References boundary motif (RS/ex L92 sib_idx-based namespace) | HIGH | **§F-1 NEW (folded)** |
| 3 | atoms/line ratio empirical band 0.59-0.85 9-round sustained | LOW | **§F-2 NEW INFO** |
| 4 | INFO-R08-01 kickoff atom estimate multi-level nested-list calibration | LOW | **§F-3 NEW INFO process** |
| 5 | INFO-R07-01 §E-5 verification grep whitespace-tolerance | INFO | INFO carry, no rule (already covered §E-5) |
| 6 | INFO-R07-02 atoms/line ratio uptick driver | INFO | folded into §F-2 |
| 7 | INFO-R08-02 sample size note per-batch byte-sweep gap | INFO | INFO process, no rule (current sampling cadence sustained) |
| 8 | INFO-R08-03 §2.11 Plan B not stress-tested in round 08 | INFO | **RESOLVED post round 09** |
| 9 | INFO-R06-01 batch kickoff dispatch prompt count drift | INFO | INFO process, no rule (Hook 22b already covers) |
| 10 | B-04 source curation pass + schema v1.3 promote eval | LOW | carry to v2.0 candidate stack (defer) |

**Net**: 10 candidates → 3 NEW F-rules (1 HIGH §F-1 + 2 INFO §F-2/F-3) + 7 INFO/process carries.

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.9 | 2026-04-29 | post P2 Pilot 2-attempt cycle: 8 NEW patches C-1..C-8. N21 全 ban writer-family 扩到 MD-side. |
| v1.9.1 | 2026-05-05 | post P2 B-02 cycle CLOSED + cumulative audit GREEN-LIGHT 30/30=100%: 8 NEW D-rules consolidating 19 candidate stack. 3 NEW hooks. MD-side hooks 22 → 25. |
| v1.9.2 | 2026-05-06 | post P2 B-03c rounds 01-06 CLOSED + ★ 跨 50% domain coverage milestone: 6 NEW E-rules consolidating 10 candidate stack (1 CRITICAL §E-1 + 3 HIGH R-2.8-1/2/3 + 1 MED MED-01 + 1 LOW FIGURE/CODE boundary). 5 NEW hooks. MD-side hooks 25 → 28. |
| **v1.9.3** | **2026-05-07** | **post P2 B-03c rounds 07-09 CLOSED + ★ §2.11 Plan B 2nd production validation 4 cases including NEW References boundary + cumulative 9112 atoms 73.05% file coverage**: 3 NEW F-rules consolidating 10-candidate stack (1 HIGH §F-1 §2.11 Plan B SUSTAINED VALIDATED EXTENDED codification + 2 INFO §F-2/F-3 atoms/line ratio band + nested-list calibration). 2 NEW hooks (Hook F-1 + F-2). MD-side hooks 28 → 30. v1.9.2 archived `archive/v1.9.2_final_2026-05-07/`. **Backward compatible** — round 07-09 production atoms 990 cumulative byte-exact preserved. |
