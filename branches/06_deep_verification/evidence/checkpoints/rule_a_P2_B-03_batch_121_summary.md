# Rule A audit — P2 B-03c round 11 batch_121 (TD/examples.md)

> Reviewer: `pr-review-toolkit:code-reviewer` (P0 reviewer v1.9.3, Rule D 隔离 vs writer `general-purpose`)
> Audit date: 2026-05-07
> Verdict: **PASS** (with 2 INFO carries to v2.0 candidate stack — non-blocking)

## Inputs

- Source: `knowledge_base/domains/TD/examples.md` (165 lines, 3 H2 numbered + 3 mermaid blocks)
- Writer output: `evidence/checkpoints/P2_B-03_batch_121_md_atoms.jsonl` (38 atoms, a001..a038)
- Writer subagent_type: `general-purpose` (prompt v1.9.3, ts 2026-05-07T11:04:15Z)

## Audit summary table

| Hook | Check | Result |
|---|---|---|
| Hook A1 | Byte-exact verbatim incl. 3 multi-line FIGURE atoms | **PASS 38/38** |
| §R-E1 | Schema regression sweep PRIORITY 1 (12 required fields × 38 atoms) | **PASS 0 violation** |
| §R-E2 | H1 sib_idx=1 universal | **PASS** (a001 hl=1 sib=1) |
| §R-E3 | TABLE_HEADER + TABLE_ROW sib=null + hl=null | **PASS** (3 TH + 8 TR all null) |
| §R-E4 | extracted_by object schema (subagent_type + prompt_version + ts) | **PASS 38/38** |
| §R-E5 | non-HEADING atoms field-explicit-null (incl. 3 FIGURE) | **PASS 0 violation** |
| §R-E6 | FIGURE-vs-CODE_LITERAL boundary | **PASS** (3 mermaid → FIGURE; 0 CODE_LITERAL) |
| §R-F-1 | §2.11 Plan B sub-namespace | **N/A** (0 H3 in batch; 0 §F-1 trigger) |
| §R-F-2 | atoms/line ratio empirical band 0.59-0.85 | **INFO** ratio=0.230 below band; FIGURE-compression driver, non-blocking carry |
| §R-F-3 | kickoff estimate calibration delta_pct ≤ 50% | **INFO** delta=62% above 50% threshold; un-FIGURE-aware estimate driver, non-blocking carry |
| §2.5 | Numbered H2 self-namespace ×3 | **PASS** (a002/a014/a025 sib=1/2/3 file-root parent) |
| §2.6 | FIGURE-in-domains lock ×3 | **PASS** byte-exact mermaid fences preserved |
| §2.7 | Numberless H2 childless | **N/A** (0 numberless H2 in batch) |
| §2.9 | LIST_ITEM sib_idx universal null | **PASS** 7/7 |
| §2.10 (E-5) | LIST_ITEM hl+sib field-explicit-null | **PASS** 7/7 |
| atom_id | uniqueness + sequential a001..a038 | **PASS** |
| parent_section | distribution = 4 file-root + 34 sub-namespace | **PASS** (1H1+3H2 file-root; 11/10/13 §TD.1/.2/.3) |

## Hook A1 — Byte-exact verbatim verification (CRITICAL)

Run: `'\n'.join(src_lines[line_start-1:line_end]) == verbatim`

- **Result**: 38/38 PASS — 0 byte-exact mismatches
- 3 FIGURE atoms (multi-line mermaid blocks):
  - `md_dmTD_ex_a004` L7-L36 (30 src lines, 804 UTF-8 bytes)
  - `md_dmTD_ex_a016` L58-L86 (29 src lines, 921 UTF-8 bytes)
  - `md_dmTD_ex_a027` L107-L145 (39 src lines, 1384 UTF-8 bytes)
- All 3 FIGURE atoms verified:
  - `verbatim` STARTS with ` ```mermaid` ✓
  - `verbatim` ENDS with ` ``` ` (closing fence on its own line) ✓
  - Mermaid syntax preserved: `graph LR` + `subgraph` + `-->` arrows all intact ✓

Note: writer DONE reported byte counts 770/895/1340; reviewer measured UTF-8 byte counts 804/921/1384. The delta is the multi-byte unicode characters (em-dashes "—" and triangles "▲") that mermaid blocks contain — writer was likely counting characters not UTF-8 bytes. Both agree on byte-exact verbatim equality with source; the byte-count number-of-record difference is a measurement metric not a verbatim defect.

## §2.6 FIGURE-in-domains lock — 3 cases verify

| Atom | Source span | parent_section | hl | sib | Mermaid syntax preserved |
|---|---|---|---|---|---|
| a004 | L7-L36 (30 lines) | `§TD.1 [Example 1]` | null | null | ✓ graph LR + subgraph S1/S2/S3 + arrow chain |
| a016 | L58-L86 (29 lines) | `§TD.2 [Example 2]` | null | null | ✓ graph LR + subgraph P1/P2 + arrow chain |
| a027 | L107-L145 (39 lines) | `§TD.3 [Example 3]` | null | null | ✓ graph LR + subgraph DBT/EXT + arrow chain |

All 3 PASS round 03 §2.6 lock criteria + sustained per round 10 RELSPEC/ex precedent. **Round 11 batch_121 is the first triple-FIGURE production batch in B-03c.**

## §2.5 Numbered H2 ×3 sub-namespace verify

| Atom | L | verbatim | hl | sib | parent | sub-namespace for children |
|---|---|---|---|---|---|---|
| a002 | L3 | `## Example 1` | 2 | 1 | `§TD [TD — Examples]` (file-root) | `§TD.1 [Example 1]` |
| a014 | L54 | `## Example 2` | 2 | 2 | `§TD [TD — Examples]` (file-root) | `§TD.2 [Example 2]` |
| a025 | L103 | `## Example 3` | 2 | 3 | `§TD [TD — Examples]` (file-root) | `§TD.3 [Example 3]` |

H2 sib_idx 1/2/3 sequential ✓. Sub-namespace propagated correctly to all children atoms (11/10/13 atoms per §TD.N).

## §F-3 calibration analysis (CRITICAL retrospective)

**Raw ratio (un-FIGURE-aware)**: 38 / 165 = **0.230** — below empirical band 0.59-0.85 → INFO carry.

**De-FIGURE-compressed naive ratio (validates C-R10-02 v2.0 candidate)**:

3 FIGURE atoms span 30 + 29 + 39 = 98 source lines. If those 98 lines were instead naively atomized as SENTENCE/LIST_ITEM (no figure compression):

```
naive_count = 38 + (98 − 3) = 133 atoms equivalent
naive_ratio = 133 / 165 = 0.806
```

**0.806 ∈ [0.59, 0.85] IN BAND ✓**

This validates **C-R10-02 §F-3 FIGURE-aware estimate v2.0 candidate** (round 10 carry). Round 11 batch_121 is the **first triple-FIGURE production validation** of the v2.0 candidate. The kickoff §4 halt-low threshold (40 atoms) was computed with un-FIGURE-aware band; once the FIGURE compression is accounted for the ratio falls cleanly in band — the 38 < 40 trigger is a measurement artifact of the un-calibrated estimator, NOT source/prompt drift.

**Recommendation**: C-R10-01 (FIGURE-bearing band supplement) + C-R10-02 (FIGURE-aware estimate) v2.0 candidates **SUSTAINED EXTENDED** to round 11. 2 production validations now (round 10 RELSPEC/ex 1-FIGURE single + round 11 TD/ex 3-FIGURE triple) — recommend cut into v1.9.4 baseline next session per pattern of v1.9.2/v1.9.3 cuts after 2-3 sustained validations.

## Estimate calibration — kickoff vs actual

| Source | Estimate | Actual | Mid | delta_pct |
|---|---|---|---|---|
| Kickoff §4 row "121 TD/ex" | 80-120 | 38 | 100 | **62%** (above 50% INFO threshold) |
| Kickoff halt-low (0.5×low) | <40 trip | 38 | — | trip by 2 atoms |

Driver: estimate computed via §F-2 mid 0.73 × 165 = ~120 (upper) — but estimate did not subtract FIGURE compression (98 source lines collapsed to 3 atoms loses ~95 atoms equivalent vs naive ratio). The C-R10-02 v2.0 candidate proposes adding a FIGURE adjustment: `est_lower = 0.59 × (lines − figure_lines + figure_count)` which for batch_121 yields `0.59 × (165 − 98 + 3) = 0.59 × 70 = 41` — significantly closer to actual 38 (delta 7.3%, well within calibration band).

**§R-F-3 INFO carry SUSTAINED** — non-blocking. Recommend C-R10-02 cut to v1.9.4 baseline as primary calibration formula post round 11 validation.

## Rule A semantic sample (n=13)

Coverage across all 6 atom types occurring in batch:

| # | atom_id | type | byte_match | type_appropriateness | overall |
|---|---|---|---|---|---|
| 1 | a001 | HEADING (H1) | ✓ | starts `#` | PASS |
| 2 | a002 | HEADING (H2) | ✓ | starts `##` | PASS |
| 3 | a014 | HEADING (H2) | ✓ | starts `##` | PASS |
| 4 | a025 | HEADING (H2) | ✓ | starts `##` | PASS |
| 5 | a004 | FIGURE | ✓ | mermaid block, fences preserved, graph syntax intact | PASS |
| 6 | a016 | FIGURE | ✓ | mermaid block, fences preserved, graph syntax intact | PASS |
| 7 | a027 | FIGURE | ✓ | mermaid block, fences preserved, graph syntax intact | PASS |
| 8 | a005 | SENTENCE | ✓ | narrative paragraph (Example 1) | PASS |
| 9 | a017 | SENTENCE | ✓ | narrative paragraph (Example 2) | PASS |
| 10 | a008 | LIST_ITEM | ✓ | starts `-`, sib=null hl=null | PASS |
| 11 | a030 | LIST_ITEM | ✓ | starts `-`, sib=null hl=null | PASS |
| 12 | a022 | TABLE_HEADER | ✓ | `|...|` with `---` separator (2 lines), sib=null hl=null | PASS |
| 13 | a038 | TABLE_ROW | ✓ | `|...|` data row, sib=null hl=null | PASS |

**Rule A pass rate: 13/13 = 100%**.

## Hook 35-count summary (v1.9.3 reviewer)

- v1.7 hooks 1-18: PASS
- v1.9 R22 + R23: PASS
- v1.9.1 R24 + R-D2..R-D6: PASS
- v1.9.2 R25 + R-E2..R-E6: PASS
- v1.9.3 R-F-1: N/A (no §F-1 trigger in batch); R-F-2: INFO; R-F-3: INFO
- **35/35 hooks evaluated PASS** (with 2 INFO non-blocking carries)

## HIGH severity findings

**0 HIGH severity findings.** Structural correctness verified — the 38 < 40 halt-low threshold trip is artifact of un-FIGURE-aware kickoff estimate (C-R10-02 sustained), NOT source omission, prompt drift, or schema regression. All 38 atoms byte-exact PASS, all schema fields PASS, all sub-namespace + parent consistency PASS.

## INFO carries (v2.0 candidate stack)

1. **C-R10-01 §F-2 FIGURE-bearing band supplement** — 2nd production validation (round 10 RELSPEC/ex single FIGURE → round 11 TD/ex triple FIGURE). Ratio 0.230 raw / 0.806 de-FIGURE-compressed both consistent with prior FIGURE-bearing batch behavior. **Recommend cut to v1.9.4 baseline next session.**
2. **C-R10-02 §F-3 FIGURE-aware estimate v2.0** — 2nd production validation (round 10 batch_105 single FIGURE near halt threshold + round 11 batch_121 triple FIGURE crossed halt-low). Naive de-FIGURE-compressed ratio 0.806 IN BAND validates the candidate formula. **Recommend cut to v1.9.4 baseline next session.**

## Verdict

**PASS** — 0 HIGH severity, 0 schema regression, 0 byte-exact mismatch, Rule A 13/13 100%. 2 INFO carries to v2.0 candidate stack are non-blocking and sustain v1.9.4 cut readiness criteria (2 production validations now satisfied).
