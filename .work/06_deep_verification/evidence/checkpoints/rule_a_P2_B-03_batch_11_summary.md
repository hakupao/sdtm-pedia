# Rule A Audit Summary — P2 B-03 batch_11

> Reviewer: pr-review-toolkit:code-reviewer (peer-alternative pool, per writer §D-8)
> Writer subagent: general-purpose (P0_writer_md_v1.9.1)
> Rule D 隔离: VALIDATED — reviewer subagent_type ≠ writer subagent_type
> Date: 2026-05-05
> Slice: VARIABLE_INDEX.md L1412-1670 (slice 6/7 of 7-slice cut for VARIABLE_INDEX)

## Sample composition

- **6 boundary** atoms (slice-first H3 a1281 / RELSUB sib=42 H3 / RS large-table H3 / SUPPQUAL `[domain name]` literal H3 / SV slice-last H3 / a1500 slice-last TABLE_ROW)
- **4 stratified** atoms (RELREC small-table TR / SR TABLE_HEADER 2-row / RS large-table TR / SUPPQUAL TR)

Total: **10 verdicts**, all **PASS**. Gate ≥90%: **PASS at 100%**.

## Audit dimensions — full result

| Dimension | Verdict |
|---|---|
| verbatim byte-exact (10/10 samples + spot-check on `[domain name]` literal hex `5b 64 6f 6d 61 69 6e 20 6e 61 6d 65 5d`) | PASS |
| atom_type canonical (HEADING/TABLE_HEADER/TABLE_ROW only — 0 SENTENCE/LIST_ITEM/NOTE/FIGURE/CODE_LITERAL) | PASS |
| parent_section uniform `§ 二、领域专属变量（仅 1 个域，共 1499 个），按域分组` (220/220 atoms — 0 deviation) | PASS |
| atom_id sequential a1281..a1500 (4-digit padded, 0 gaps, total 220) | PASS |
| sib chain 40..52 contiguous (13 H3 = 13 sib_index distinct values, RELREC..SV) | PASS |
| TABLE_HEADER v1.9 standard 2-row (line_end - line_start == 1) — all 13 TABLE_HEADER atoms | PASS |
| Cross-slice continuity batch_10 a1280 sib=39 → batch_11 a1281 sib=40 | PASS |

## Per-domain TABLE_ROW counts (independent grep verify)

Writer's claim: RELREC2 / RELSPEC4 / RELSUB3 / RP28 / RS38 / SC16 / SE6 / SM5 / SR31 / SS14 / SU32 / SUPPQUAL5 / SV10 = 194.

Reviewer independent count (Python parse of writer JSONL → group by H3 line_start range):

| Domain | sib | TH | TR | Match? |
|---|---|---|---|---|
| RELREC | 40 | 1 | 2 | ✓ |
| RELSPEC | 41 | 1 | 4 | ✓ |
| RELSUB | 42 | 1 | 3 | ✓ |
| RP | 43 | 1 | 28 | ✓ |
| RS | 44 | 1 | 38 | ✓ |
| SC | 45 | 1 | 16 | ✓ |
| SE | 46 | 1 | 6 | ✓ |
| SM | 47 | 1 | 5 | ✓ |
| SR | 48 | 1 | 31 | ✓ |
| SS | 49 | 1 | 14 | ✓ |
| SU | 50 | 1 | 32 | ✓ |
| SUPPQUAL | 51 | 1 | 5 | ✓ |
| SV | 52 | 1 | 10 | ✓ |
| **Total** | | **13** | **194** | ✓ |

Sum = 13 H3 + 13 TH + 194 TR = **220 atoms**, matches writer report.

## Atom type distribution

```
13  HEADING        (h_lvl=3, sib 40..52 RELREC..SV)
13  TABLE_HEADER   (line_end - line_start == 1, v1.9 standard 2-row, all per-domain)
194 TABLE_ROW
---
220 total
```

0 SENTENCE / 0 LIST_ITEM / 0 NOTE / 0 FIGURE / 0 CODE_LITERAL — fully canonical for VARIABLE_INDEX index-table content type.

## Kickoff drift verification (§R-D1)

Reviewer independent grep verify against `knowledge_base/VARIABLE_INDEX.md`:

- Kickoff §0.5 claim row 2: 13 H3 at L1412/1419/1428/1436/1469/1512/1533/1544/1554/1590/1609/1646/1656 — **verified ✓** (all 13 H3 atoms in writer JSONL match these line numbers exactly).
- Kickoff §0.5 claim row 4: 13 tables — **verified ✓** (13 TABLE_HEADER atoms; 1-to-1 H3↔table correspondence).
- Kickoff §0.5 claim row 5: L1669 = SVUPDES TABLE_ROW (last atom) — **verified ✓** (a1500 verbatim byte-exact).
- Kickoff §0.5 claim row 6: atom_id 起 = `md_varindex_a1281` — **verified ✓**.

**No kickoff doc drift detected** for this batch. Writer atoms align with both source and kickoff.

## §R-D6 TABLE_HEADER style classification (mandatory declaration)

13 TABLE_HEADER atoms sampled (all in batch). 100% v1.9 standard 2-row. 0 v1.8 pilot 1-row legacy (expected — VARIABLE_INDEX is post-pilot ≥ a219). 0 FAIL_LINE_RANGE.

## Codified-anomaly stratified samples (§R-Stratified-Sampling v1.9.1)

This batch contained **1 D-codified canonical pattern instance**: SUPPQUAL H3 (a1482, L1646) with literal bracket `[domain name]` — Rule B requires byte-exact preservation (not interpreted as a variable substitution placeholder). Reviewer hex-dump verified preservation (sample #4). **PASS.**

No D7 NOTE-BQ, D5 dual-constraint, D8 chapter-root, bold-caption SENTENCE, or mixed sib chain instances in this slice (expected — slice is 100% index-table content).

## Self-validate hooks (subset relevant to this batch)

| Hook | Check | Result |
|---|---|---|
| v1.7 H1 | atom_type ∈ canonical set | PASS (HEADING/TABLE_HEADER/TABLE_ROW only) |
| v1.7 H2 | verbatim byte-exact | PASS (10/10 sampled + spot SUPPQUAL bracket) |
| v1.7 H3 | parent_section coherent | PASS (220/220 uniform) |
| v1.7 H6 | sib chain contiguous | PASS (40..52, 13 distinct) |
| v1.7 H8 | atom_id sequential | PASS (a1281..a1500, 0 gaps) |
| v1.9 R23 | defect-class concentration explicit | N/A (0 defects) |
| v1.9.1 R24 | kickoff drift routing | PASS (no drift detected; atoms = source byte-exact) |
| v1.9.1 R-D6 | TABLE_HEADER style declaration | PASS (13/13 v1.9 standard 2-row, declared) |

## Verdict

**PASS — 10/10 = 100%** strict PASS. **0 HIGH / 0 MEDIUM / 0 LOW** findings.

Gate ≥90%: cleared decisively.

Slice 6/7 closes; slice 7 (L1671-end) ready for kickoff.
