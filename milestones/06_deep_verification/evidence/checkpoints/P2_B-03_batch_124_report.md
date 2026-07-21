# P2 B-03c Round 12 — batch_124 Writer Report

> Source: `knowledge_base/domains/TA/examples.md` slice B (L344-L605, 262L)
> Scope: §2.4 multi-batch slice 2/3 — Examples 4/5/6 + 8 mermaid FIGURE blocks
> Prompt version: P0_writer_md_v1.9.3
> Subagent: general-purpose
> Timestamp: 2026-05-07T16:00:00Z

## §0 Source line range

| Item | Value |
|---|---|
| Slice | B (2/3 of TA/ex multi-batch) |
| Line range | 344–605 (262 lines) |
| Examples | Example 4 (L344-465) + Example 5 (L466-533) + Example 6 (L534-605) |
| FIGURE blocks | 8 mermaid (E4 ×4 / E5 ×2 / E6 ×2) |
| Slice A predecessor | batch_123 atoms a001..a113 line_end 342 (gap L343 blank) |
| Slice C successor | batch_125 L606+ Examples 7+ |

## §1 Atom type distribution

| atom_type | Count |
|---|---|
| HEADING | 3 (## Example 4/5/6) |
| SENTENCE | 27 (intro narrative + **bold** sub-captions) |
| FIGURE | **8** (mermaid blocks byte-exact) |
| TABLE_HEADER | 6 (Trial Design Matrix ×3 + ta.xpt ×3) |
| TABLE_ROW | 60 (Trial Design Matrix 2+2+2 + ta.xpt 20+16+18) |
| **Total** | **104** |

Halt threshold [55, 240]: actual 104 → OK (mid-range).

## §2 Sample atom_id list

| Position | atom_id | atom_type | Line | Note |
|---|---|---|---|---|
| First | md_dmTA_ex_a114 | HEADING | 344 | ## Example 4 (sib=4) |
| E4 narrative | md_dmTA_ex_a115 | SENTENCE | 346 | Intro sentence 1 |
| E4 figure 1 | md_dmTA_ex_a120 | FIGURE | 352-360 | Study Schema |
| E4 figure 4 | md_dmTA_ex_a128 | FIGURE | 416-432 | Blinded View |
| E5 H2 | md_dmTA_ex_a155 | HEADING | 466 | ## Example 5 (sib=5) |
| E5 figure 1 | md_dmTA_ex_a160 | FIGURE | 472-484 | Study Schema |
| E6 H2 | md_dmTA_ex_a185 | HEADING | 534 | ## Example 6 (sib=6) |
| E6 figure 2 | md_dmTA_ex_a193 | FIGURE | 558-574 | Retrospective View |
| Last | md_dmTA_ex_a217 | TABLE_ROW | 604 | EX6 ta.xpt row 18 |

## §3 Schema sweep — PASS_12_12

| # | Check | Result |
|---|---|---|
| 1 | 12-field set (atom_id/file/line_start/line_end/parent_section/atom_type/verbatim/heading_level/sibling_index/figure_ref/cross_refs/extracted_by) | PASS |
| 2 | atom_id pattern `^md_[A-Za-z0-9_]+_a\d{3,}$` | PASS |
| 3 | atom_id uniqueness within batch | PASS (104/104) |
| 4 | atom_id collision against master (post-batch_123 9631) | PASS (0 collision pre-append) |
| 5 | atom_type ∈ 9-value enum | PASS |
| 6 | line_start/line_end ∈ [344, 605] | PASS |
| 7 | line_end ≥ line_start | PASS |
| 8 | extracted_by object {subagent_type, prompt_version, ts} | PASS |
| 9 | HEADING required heading_level + sibling_index | PASS (3/3) |
| 10 | parent_section namespace correct (§TA file-root for H2; §TA.4/5/6 for content) | PASS |
| 11 | non-HEADING heading_level=null + sibling_index=null (§E-5 MED-01) | PASS |
| 12 | TABLE_HEADER sibling_index=null universal (§E-3 R-2.8-2) | PASS (6/6) |

Final result: **PASS_12_12**.

## §4 Hook compliance (v1.9.3 = 30 hooks effective)

| Hook | Check | Result |
|---|---|---|
| v1.7 H1-H18 | atom_type enum / FIGURE convention / sentence-not-paragraph / heading-caption / etc. | PASS |
| v1.9 Hook 22 + A1/A2/A3/A4 | dispatch JSON template + LIST_ITEM full-prefix + null-discipline | PASS / N/A LIST_ITEM (none in slice B) |
| v1.9.1 Hook 22b + D-NOTE-BQ + D-D8 | grep verify count / no NOTE/blockquote in slice / no D-D8 trigger | PASS |
| v1.9.2 Hook 22c | dispatch reference working atom (md_dmRELSPEC_assn_a001 anchored) | PASS |
| v1.9.2 E-2-1 R-2.8-1 | H1 sib_idx=1 universal — N/A (no H1 in slice B) | N/A |
| v1.9.2 E-3-2 R-2.8-2 | TABLE_HEADER sib_idx=null universal | PASS (6/6) |
| v1.9.2 E-4-3 R-2.8-3 | extracted_by object schema | PASS |
| v1.9.2 E-5 MED-01 | non-HEADING field-explicit-null | PASS (101/101 non-HEADING) |
| v1.9.2 E-6 | FIGURE-vs-CODE_LITERAL boundary (mermaid → FIGURE) | PASS (8/8) |
| **v1.9.3 Hook F-1** | §2.11 Plan B sub-namespace — N/A (no NUMBERLESS H2 with H3 children in slice B; all H2 are NUMBERED `## Example N`) | N/A |
| **v1.9.3 Hook F-2** | atoms/line ratio retrospective | REPORTED (de-fig 0.7324 IN BAND) |
| Hook F-3 | N/A writer-side | N/A |

Overall: **PASS_v1.9.3**.

## §5 §2.6 FIGURE byte-exact verification

All 8 mermaid blocks verified byte-exact against source `knowledge_base/domains/TA/examples.md`:

| atom_id | Lines | Bytes | Header | Tail | Result |
|---|---|---|---|---|---|
| md_dmTA_ex_a120 | 352–360 | 320 | ` ```mermaid ` | ` ``` ` | PASS |
| md_dmTA_ex_a122 | 364–380 | 400 | ` ```mermaid ` | ` ``` ` | PASS |
| md_dmTA_ex_a126 | 388–412 | 722 | ` ```mermaid ` | ` ``` ` | PASS |
| md_dmTA_ex_a128 | 416–432 | 447 | ` ```mermaid ` | ` ``` ` | PASS |
| md_dmTA_ex_a160 | 472–484 | 529 | ` ```mermaid ` | ` ``` ` | PASS |
| md_dmTA_ex_a162 | 488–504 | 399 | ` ```mermaid ` | ` ``` ` | PASS |
| md_dmTA_ex_a191 | 542–554 | 529 | ` ```mermaid ` | ` ``` ` | PASS |
| md_dmTA_ex_a193 | 558–574 | 439 | ` ```mermaid ` | ` ``` ` | PASS |

Total FIGURE bytes preserved: **3,785 bytes** (no truncation, no escaping drift).

**Build script defect caught + fixed mid-execution**: Initial pass produced doubled-newline FIGURE verbatim (8/16/24-byte excess due to `f.readlines()` keeping `\n` then `"\n".join(...)` doubling). Caught by §5 byte-exact verifier (all 8 figures FAILED byte-exact pre-fix). Rolled back master append, fixed `block()` helper (`line.rstrip("\n")` before join), rebuilt, re-verified — all 8 PASS post-fix. Master state clean (no orphan / no duplicate).

## §6 §2.4 cross-slice 续号 verification

| Check | Expected | Actual | Result |
|---|---|---|---|
| First atom_id (slice B start) | md_dmTA_ex_a114 (NOT a001) | md_dmTA_ex_a114 | PASS |
| Last atom_id | a217 (within [a168, a273] estimate band per kickoff) | md_dmTA_ex_a217 | PASS |
| Slice A intact in master | 113 atoms a001..a113 unchanged | 113/113 verified | PASS |
| TA/ex atom_id space contiguous | a001..a217 = 217 IDs no gaps | min=1 max=217 count=217 contiguous=True | PASS |
| H2 sib_idx 4/5/6 (NOT 1/2/3 restart) | E4=4, E5=5, E6=6 (continuing slice A 1/2/3) | a114=4, a155=5, a185=6 | PASS |
| H2 verbatim | `## Example 4`, `## Example 5`, `## Example 6` | matched | PASS |
| H2 parent_section | `§TA [TA — Examples]` (file-root) | matched | PASS |

§2.4 cross-slice atom_id 续号 lock: **PASS**.
§2.5 numbered H2 self-namespace continuation lock: **PASS**.

## §F-2 atoms/line ratio (de-figure formula)

```
slice_lines = 605 - 344 + 1 = 262
sum_fig_span = sum(end - start + 1 for each FIGURE) = 9 + 17 + 25 + 17 + 13 + 17 + 13 + 17 = 128
N_fig = 8
de_fig_lines = slice_lines - sum_fig_span + N_fig = 262 - 128 + 8 = 142
atoms = 104
```

| Ratio | Value | §F-2 band [0.59, 0.85] |
|---|---|---|
| Naive (atoms / slice_lines) | 104/262 = **0.3969** | OUT OF BAND (low — figures dominate slice) |
| **De-figure (atoms / de_fig_lines)** | 104/142 = **0.7324** | **IN BAND** |

The de-figure ratio is the reviewer-codified proper formula (batch_123 reviewer pin). 0.7324 sits squarely in the upper-mid empirical band, consistent with TA examples.md being LIST_ITEM-light + dense table content (TABLE_ROW heavy: 60/104 = 57.7% of atoms).

## §7 Single-line DONE

```
PARALLEL_SESSION_124_DONE atoms=104 failures=0 repair_cycles=1 schema_sweep=PASS_12_12 hooks=PASS_v1.9.3 atom_id_range=md_dmTA_ex_a114..a217 figure_count=8 cross_slice_续号=PASS
```

Note: `repair_cycles=1` reflects the in-session FIGURE byte-exact build-script fix (rolled back + rebuilt + re-verified all green; final state clean).
