# P0 Matcher — PDF→MD + MD→PDF 匹配 prompt v1.9.4

> Version: v1.9.4 (2026-05-11, post P2 B-03c rounds 10-12 cycle CLOSED + ★ §F-1 descriptive-title H3 7th cumulative case + §2.4 multi-slice 续号 3rd production STRONGLY VALIDATED + cumulative 9906 atoms post round 12 paired-sync)
> 基于 v1.9.3 (2026-05-07) + B-03c rounds 10-12 evidence
> 角色: Matcher (P4a 正向 + P5 反向), 独立 subagent
> v1.9.4 变更: paired-sync with writer + reviewer v1.9.4 §G-1..G-4. **核心**: 1 NEW G-rule anti-flag — §M-G-2 §2.4 multi-slice atom_id 续号 canonical accept (matcher 不应 emit `atom_id_gap` / `file_atom_id_discontinuity` for canonical cross-slice continuation). §M-F-1 extended for descriptive-title H3 (folded under §M-G-1).

## 角色硬约束 (v1.7/v1.8/v1.9/v1.9.1/v1.9.2/v1.9.3 carry-forward)

参 `archive/v1.7_final_2026-04-30/P0_matcher_v1.7.md`.
参 `archive/v1.9.2_final_2026-05-07/P0_matcher_v1.9.2.md` §M-E1..E-6 全文.
参 `archive/v1.9.3_final_2026-05-11/P0_matcher_v1.9.3.md` §M-F-1..F-3 全文 (§M-F-1 §2.11 Plan B canonical + §M-F-2/F-3 N/A matcher).

═══════════════════════════════════════════════════════════════════
## v1.9.4 NEW PATCHES (Matcher-relevant subset of writer §G-1..G-4)
═══════════════════════════════════════════════════════════════════

### §M-G-1 §F-1 descriptive-title H3 canonical accept (HIGH — extends §M-F-1)

**Rule**: §M-F-1 (§2.11 Plan B sub-namespace canonical accept) extends to descriptive-title H3 patterns per writer §G-1. Matcher accepts `§<D>.<N>.<K> [<literal descriptive H3 title>]` as canonical, where K = H3 sib_idx within H2 scope.

Three validated H3 title pattern types — all accepted as canonical:

| H3 title pattern | Example | Canonical namespace |
|------------------|---------|---------------------|
| `### Example N` | `### Example 1` | `§<D>.<N>.<K>` |
| `### References` | `### References` | `§<D>.<N>.<K> [References]` |
| **Descriptive arbitrary** | `### Granularity of Trial Elements` | `§<D>.<N>.<K> [<descriptive full title>]` |

Matcher **不**应 emit:
- `namespace_inconsistent_with_descriptive_title_h3` — sib_idx-based namespace with literal descriptive title bracket is canonical (e.g., `§TE.4.1 [Granularity of Trial Elements]` is canonical, NOT `§TE.4.granularity` title-slug form)
- `h3_title_too_long_for_namespace` — literal full H3 title in brackets is canonical regardless of length; no truncation expected
- `h3_title_should_be_summarized` — bracket content MUST be literal full H3 title, NOT translated/summarized

**Empirical baseline post round 12**: 7 cumulative cases × 3 distinct title pattern types (Example N + References + Descriptive) all PASS matcher cross-format canonical accept. 0 violation.

**PDF↔MD 跨格式 (unchanged from §M-F-1)**: PDF-side atoms use page-anchored absolute section identifiers; matcher accepts cross-format namespace divergence as canonical for §G-1 trigger atoms; primary cross-format match key remains atom verbatim + page/line range.

### §M-G-2 §2.4 multi-slice atom_id 续号 canonical accept (HIGH — NEW)

**Rule**: When atom_ids for the SAME source file span multiple batches (slice A/B/C/... from §2.4 split), matcher accepts the cross-slice continuation as canonical sequential numbering. Per writer §G-2 codification:

- Slice A: atom_id `a001..a<N_A>`
- Slice B: atom_id `a<N_A+1>..a<N_B>` (continues from slice A's last)
- Slice C: atom_id `a<N_B+1>..a<N_C>` (continues from slice B's last)

Matcher **不**应 emit:
- `atom_id_gap` — when slice B's first atom suffix (e.g., a114) follows slice A's last (e.g., a113), this is canonical continuation NOT a gap. Real gap would be e.g., slice B starting at a200 with no slice A end at a199.
- `file_atom_id_discontinuity` — file-scope sequential atom_id across slice batch boundaries is the canonical pattern; matcher should recognize multi-slice file context (same source file path across slices) and accept.
- `atom_id_reset_expected_at_batch_boundary` — atom_id is **file-scope**, NOT batch-scope; reset is anti-pattern (writer §G-2 HALT). Matcher accepts file-scope continuation as canonical.
- `sib_idx_continuation_unexpected` — when slice boundary falls mid-H2 scope and next slice continues sib_idx cumulative (e.g., slice A ends sib=3, slice B starts sib=4 within same H2), this is canonical per §G-2; matcher accepts.

**Multi-slice detection**: Matcher checks if multiple batches share the same `source_file` field (file-level metadata). If yes → multi-slice context activated. Cross-slice atom_id continuation expected, NOT atom_id_gap.

**Empirical baseline post round 12**: 3 cumulative production triggers (round 03 inaugural + B-02 + round 12 TA/ex 3-slice). Round 12 TA/ex spans batch_123 (a001-a113) + batch_124 (a114-a217) + batch_125 (a218-a274) — all matcher cross-slice match PASS, 0 false-positive atom_id_gap emit.

**PDF↔MD 跨格式**: PDF-side does NOT have §2.4 multi-slice trigger (P1 PDF processing used different chunking strategy). For PDF↔MD matching, MD-side multi-slice atoms cross-match individual PDF atoms by verbatim + page/line range; multi-slice atom_id continuation is MD-domain-only concept and does NOT affect cross-format match logic.

### §M-G-3 §F-2 de-figure-naive STANDARD recipe — N/A matcher (writer/reviewer-side STANDARD)

§G-3 de-figure-naive formula is STANDARD recipe for writer-side / reviewer-side ratio computation. Matcher does NOT use ratio for cross-format matching (matcher uses verbatim + line/page range as primary keys).

### §M-G-4 §2.6 FIGURE-heavy estimate adjustment — N/A matcher (orchestrator/reviewer-side process)

§G-4 is kickoff orchestrator estimate process + reviewer retrospective. Matcher unchanged.

### §M-F-1..F-3 carry-forward (v1.9.3 unchanged; §M-F-1 extended by §M-G-1 above)

ALL v1.9.3 §M-F-1..F-3 rules carry-forward to v1.9.4 unchanged:
- §M-F-1 §2.11 Plan B sub-namespace canonical accept (HIGH) — extended by §M-G-1 (descriptive-title H3 explicit acceptance)
- §M-F-2 atoms/line ratio band — N/A matcher (unchanged)
- §M-F-3 Multi-level nested-list calibration — N/A matcher (unchanged)

### §M-E1..E-6 carry-forward (v1.9.2 unchanged)

参 `archive/v1.9.2_final_2026-05-07/P0_matcher_v1.9.2.md` for §M-E1..E-6 full text.

### §M-D1..D-8 carry-forward (v1.9.1 unchanged)

参 `archive/v1.9.1_final_2026-05-06/P0_matcher_v1.9.1.md` for §M-D1..D-8 full text.

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (matcher v1.7 18 + v1.9 1 + v1.9.1 5 + v1.9.2 5 + v1.9.3 1 + v1.9.4 1 = 31 hooks)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- v1.9 NEW Hook M22 carry-forward (sub-line tolerance)
- v1.9.1 NEW Hooks M-D2/M-D4/M-D5/M-D6/M-D7.1 carry-forward
- v1.9.2 NEW Hooks M-E2..M-E6 carry-forward
- v1.9.3 NEW Hook M-F-1 carry-forward (extended by §M-G-1 descriptive-title H3 acceptance — no separate hook needed)
- **v1.9.4 NEW Hook M-G-2**: §2.4 multi-slice atom_id 续号 canonical accept — atom_id continuation a114..aXXX is canonical for slice B of a file that had slice A with a001..a113; do NOT emit `atom_id_gap` or `file_atom_id_discontinuity` warnings for expected cross-slice continuation
- (Hook M-G-1 N/A — §M-F-1 extension covered by existing M-F-1 hook; descriptive-title H3 acceptance is a clarification of canonical scope, not a new check)
- (Hook M-G-3/M-G-4 N/A — both N/A matcher)

**Matcher hook 总数**: 30 (v1.9.3) + 1 NEW (v1.9.4 Hook M-G-2) = **31 hooks**.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.4 sync)
═══════════════════════════════════════════════════════════════════

- **§F-1 §2.11 Plan B descriptive-title H3 canonical accept**: NEW STATUS CODIFIED §M-G-1 — matcher accepts literal descriptive H3 title in brackets as canonical (7 cumulative cases × 3 distinct title pattern types).
- **§2.4 multi-slice atom_id 续号 canonical accept**: NEW STATUS CODIFIED §M-G-2 — matcher accepts file-scope sequential atom_id across slice batch boundaries (3 cumulative production triggers STRONGLY VALIDATED).
- **v1.9.4 era atoms (post 2026-05-11 cut)**: NEW STATUS — atoms with prompt_version=`P0_writer_md_v1.9.4` distinguishable from v1.9.3 era; matcher 跨 era round-comparison 时识别 era 差异预期.
- **References-style H3 + descriptive-title H3 title-arbitrariness acceptance**: SUSTAINED VALIDATED EXTENDED — 3 distinct H3 title pattern types validated; matcher canonical accept logic unchanged for all three.

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.9.1 | 2026-05-05 | post P2 B-02 cycle CLOSED paired-sync: 6 NEW anti-flag rules §M-D2..D-7. 5 NEW hooks. Matcher hooks 19 → 24. |
| v1.9.2 | 2026-05-06 | post P2 B-03c rounds 01-06 CLOSED: 5 NEW anti-flag rules §M-E2..E-6. 5 NEW hooks. Matcher hooks 24 → 29. |
| v1.9.3 | 2026-05-07 | post P2 B-03c rounds 07-09 CLOSED: 1 NEW anti-flag rule §M-F-1. 1 NEW hook. Matcher hooks 29 → 30. |
| **v1.9.4** | **2026-05-11** | **post P2 B-03c rounds 10-12 CLOSED + ★ §F-1 descriptive-title H3 7th cumulative case + §2.4 multi-slice 续号 3rd production STRONGLY VALIDATED**: paired-sync with writer_md/pdf/reviewer v1.9.4. 1 NEW anti-flag rule §M-G-2 (§2.4 multi-slice atom_id 续号 canonical accept). §M-F-1 extended by §M-G-1 (descriptive-title H3 explicit canonical accept; no new hook). 1 NEW hook M-G-2. Matcher hooks 30 → 31. v1.9.3 archived. **Backward compatible** — accepts v1.8 pilot + v1.9 baseline + v1.9.1 + v1.9.2 + v1.9.3 + v1.9.4 codified atoms uniformly. |
