# P0 Matcher — PDF→MD + MD→PDF 匹配 prompt v1.9.3

> Version: v1.9.3 (2026-05-07, post P2 B-03c rounds 07-09 cycle CLOSED + ★ §2.11 Plan B 2nd production validation 4 cases including References boundary + cumulative 9112 atoms paired-sync)
> 基于 v1.9.2 (2026-05-06) + B-03c rounds 07-09 evidence
> 角色: Matcher (P4a 正向 + P5 反向), 独立 subagent
> v1.9.3 变更: paired-sync with writer + reviewer v1.9.3 §F-1..F-3. **核心**: 1 NEW F-rule anti-flag — matcher 不应 emit `schema_drift` 或 `namespace_inconsistent` for canonical §2.11 Plan B sib_idx-based sub-namespaces (`§<D>.<N>` H2-sub + `§<D>.<N>.<K>` H3-sub-sub including References-style title arbitrariness).

## 角色硬约束 (v1.7/v1.8/v1.9/v1.9.1/v1.9.2 carry-forward)

参 `archive/v1.7_final_2026-04-30/P0_matcher_v1.7.md`.
参 `archive/v1.9.2_final_2026-05-07/P0_matcher_v1.9.2.md` §M-E1..E-6 全文.

═══════════════════════════════════════════════════════════════════
## v1.9.3 NEW PATCHES (Matcher-relevant subset of writer §F-1..F-3)
═══════════════════════════════════════════════════════════════════

### §M-F-1 §2.11 Plan B sub-namespace canonical accept (HIGH)

**Rule**: 当 atom parent_section 形如 `§<D>.<N> [<H2_title>]` (H2-sub-namespace where N is H2 sib_idx) 或 `§<D>.<N>.<K> [<H3_title>]` (H3-sub-sub-namespace where K is H3 sib_idx within H2 scope), matcher 接受为 canonical. v1.9.3 baseline §F-1 codified §2.11 Plan B for numberless H2 with H3 children.

Matcher **不**应 emit:
- `namespace_inconsistent_with_h2_title` — sib_idx-based namespace `§<D>.<N>` is canonical even if H2 title varies (e.g., `§RELREC.2 [Dataset Relationship Example]` is canonical, NOT `§RELREC.dataset_relationship` title-slug form)
- `h3_sib_idx_should_be_cumulative` — H3 sib_idx restarts per H2 scope (e.g., RS/ex L69 H3 sib=1 RESTART under L65 H2 sib=2, NOT cumulative 4 from earlier L7/L26/L46 H3s under L3 H2)
- `references_style_h3_unexpected_namespace` — `### References` H3 → `§<D>.<N>.<K> [References]` sib_idx-based; sib_idx-based namespace is canonical regardless of H3 title pattern (Example N / References / Notes / arbitrary)

**PDF↔MD 跨格式**: PDF-side atoms use page-anchored absolute section identifiers (`§6.x.y [Section title]`), NOT sib_idx-based. Matcher accepts cross-format namespace divergence as canonical: PDF parent_section ≠ MD §F-1 parent_section is EXPECTED for §F-1 trigger atoms; primary cross-format match key remains atom verbatim + page/line range.

**Empirical baseline post round 09**: 5 cumulative cases × 5 H2 + 16 H3 + 60+ content atoms across round 07 (PC/ex L58: 1 H2 + 7 H3) + round 09 (4 H2 + 9 H3 including References boundary). 0 violation in matcher cross-format matching.

### §M-F-2 atoms/line ratio band — N/A matcher (writer-side INFO)

§F-2 atoms/line ratio band is INFO codification for writer-side / orchestrator-side estimate calibration. Matcher does NOT use ratio for cross-format matching (matcher uses verbatim + line/page range as primary keys).

### §M-F-3 Multi-level nested-list calibration — N/A matcher (orchestrator-side process)

§F-3 is kickoff orchestrator process rule. Matcher unchanged.

### §M-E1..E-6 carry-forward (v1.9.2 unchanged)

ALL v1.9.2 §M-E1..E-6 rules carry-forward to v1.9.3 unchanged:
- §M-E1 Schema regression sweep N/A matcher (delegated to reviewer §R-E1)
- §M-E2 R-2.8-1 H1 sib=1 universal 接受 (HIGH)
- §M-E3 R-2.8-2 TABLE_HEADER sib=null universal 接受 (HIGH)
- §M-E4 R-2.8-3 extracted_by object schema 接受 (HIGH)
- §M-E5 MED-01 non-HEADING field-explicit-null 接受 (MEDIUM)
- §M-E6 FIGURE-vs-CODE_LITERAL boundary disambiguation 接受 (LOW)

### §M-D1..D-8 carry-forward (v1.9.1 unchanged)

参 `archive/v1.9.1_final_2026-05-06/P0_matcher_v1.9.1.md` for §M-D1..D-8 full text.

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks (matcher v1.7 18 + v1.9 1 + v1.9.1 5 + v1.9.2 5 + v1.9.3 1 = 30 hooks)
═══════════════════════════════════════════════════════════════════

- v1.7 hooks 1-18 carry-forward
- v1.9 NEW Hook M22 carry-forward (sub-line tolerance)
- v1.9.1 NEW Hooks M-D2/M-D4/M-D5/M-D6/M-D7.1 carry-forward
- v1.9.2 NEW Hooks M-E2..M-E6 carry-forward
- **v1.9.3 NEW Hook M-F-1**: §2.11 Plan B sub-namespace canonical accept — sib_idx-based namespace `§<D>.<N>` H2-sub + `§<D>.<N>.<K>` H3-sub-sub canonical regardless of H3 title pattern (Example N / References / Notes / arbitrary)

**Matcher hook 总数**: 29 (v1.9.2) + 1 NEW (v1.9.3) = **30 hooks**.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.9.3 sync)
═══════════════════════════════════════════════════════════════════

- **§2.11 Plan B sub-namespace cross-format matching**: NEW STATUS CODIFIED — matcher accepts MD-side §F-1 hierarchy as canonical; PDF-side absolute section identifier as canonical for cross-format match.
- **References-style H3 title-arbitrariness acceptance**: NEW STATUS — matcher accepts `### References` / `### Notes` / etc as sib_idx-based H3 namespace (round 09 RS/ex L92 1st live-fire).
- **v1.9.3 era atoms (post 2026-05-07 cut)**: NEW STATUS — atoms with prompt_version=`P0_writer_md_v1.9.3` distinguishable from v1.9.2/v1.9.1 era; matcher 跨 era round-comparison 时识别 era 差异预期.

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.9.1 | 2026-05-05 | post P2 B-02 cycle CLOSED paired-sync: 6 NEW anti-flag rules §M-D2..D-7. 5 NEW hooks. Matcher hooks 19 → 24. |
| v1.9.2 | 2026-05-06 | post P2 B-03c rounds 01-06 CLOSED: 5 NEW anti-flag rules §M-E2..E-6. 5 NEW hooks. Matcher hooks 24 → 29. |
| **v1.9.3** | **2026-05-07** | **post P2 B-03c rounds 07-09 CLOSED + ★ §2.11 Plan B 2nd production validation 4 cases**: paired-sync with writer_md/pdf/reviewer v1.9.3. 1 NEW anti-flag rule §M-F-1 (§2.11 Plan B sub-namespace canonical accept including References-style H3 title-arbitrariness). 1 NEW hook M-F-1. Matcher hooks 29 → 30. v1.9.2 archived. **Backward compatible** — accepts v1.8 pilot + v1.9 baseline + v1.9.1 + v1.9.2 + v1.9.3 codified atoms uniformly. |
