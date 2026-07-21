# Rule A Audit Summary — P2 B-03c Round 01 batch_20 (BS/examples.md)

> Audit date: 2026-05-05
> Reviewer: `pr-review-toolkit:code-reviewer` (Rule D distinct from writer `general-purpose`)
> Reviewer prompt: `P0_reviewer_v1.9.1`
> Source: `knowledge_base/domains/BS/examples.md` (20 lines, 2,224 bytes)
> Writer output: `evidence/checkpoints/P2_B-03_batch_20_md_atoms.jsonl` (16 atoms)
> Verdicts: `evidence/checkpoints/rule_a_P2_B-03_batch_20_verdicts.jsonl`

## Sample Strategy

Per kickoff §0 audit spec — **full file audit (16 atoms / 16 atoms = 100% sample)**, exceeds 11-atom minimum (8 boundary + 3 stratified). Full coverage justified for small-file batch (20-line source).

| Class | Count | Atoms |
|---|---|---|
| Boundary H1 | 1 | a001 |
| Boundary H2 (sib=1) | 1 | a002 |
| Boundary TABLE_HEADER (L15-16) | 1 | a012 |
| Boundary TABLE_ROW × 4 | 4 | a013-a016 |
| Boundary bold-caption (filename) | 1 | a011 |
| Stratified bold-caption SENTENCE | 3 | a006, a008, a010 |
| Stratified narrative SENTENCE (sub-line) | 5 | a003, a004, a005, a007, a009 |
| **Total** | **16** | **a001-a016** |

## Verdict Distribution

| Verdict | Count | Atoms |
|---|---|---|
| PASS | 16 | all |
| CONDITIONAL_PASS | 0 | — |
| FAIL | 0 | — |

**PASS rate**: 16/16 = **100%** (gate ≥ 90% ✓).

## Check-by-check Results

### 1. verbatim byte-exact (16/16 PASS)

All atom verbatim fields independently grep/awk-verified against source via Bash:
- L1 `# BS — Examples` em-dash hex `e2 80 94` preserved (a001)
- L3 `## Example 1` (a002)
- L5 split into 3 grammatically-self-contained sentences (a003-a005)
- L7 split into bold-caption + tail (a006, a007)
- L9 split into bold-caption + tail (a008, a009)
- L11 single bold-caption sentence (a010)
- L13 `**bs.xpt**` hex `2a 2a 62 73 2e 78 70 74 2a 2a` (a011)
- L15-16 TABLE_HEADER 2-row span, both rows 198 bytes (a012)
- L17-L20 TABLE_ROW × 4, each 21-field byte-exact (a013-a016)

### 2. atom_type per v1.9.1 (16/16 PASS)

- HEADING × 2 (a001 H1, a002 H2): correct.
- SENTENCE × 9 (a003-a011): includes 4 bold-caption SENTENCE (a006/a008/a010/a011) accepted per §R-D5 (Rows/Row/filename ≠ Note/Exception literal — canonical SENTENCE retention).
- TABLE_HEADER × 1 (a012): 2-row span line_end - line_start = 1 = v1.9 standard per §R-D6.
- TABLE_ROW × 4 (a013-a016): each single-line.

**Note**: a011 `**bs.xpt**` is unusual — bold filename label functioning as a table caption marker. Reviewer accepts as SENTENCE per §R-D5 bold-caption rule (matches `**[Caption Label]:**` family even without trailing colon — bold filename treated as inline caption to following table). Not NOTE (no Note/Exception text), not HEADING (no `#` prefix). Canonical.

### 3. parent_section per CM pilot self-reference (16/16 PASS)

- a001 H1 self-reference: `§BS [BS — Examples]` — matches CM pilot precedent `§CM [CM — Assumptions]`. Kickoff §2.2 lock confirmed.
- a002 H2 self-reference: `§BS.1 [Example 1]` — matches CM pilot H2 self-reference `§CM.1 [Example 1]`. Per CM pilot, H2 atom's parent_section = its OWN sub-namespace (self-reference convention).
- a003-a016 children of H2: `§BS.1 [Example 1]` per kickoff §2.2 — all 14 children correctly inherit single H2 parent.

### 4. HEADING meta (Hook A2 pattern + sib_index) (2/2 PASS)

- a001: `^# ` matches; heading_level=1; sibling_index=1 (sole H1 in file).
- a002: `^## ` matches; heading_level=2; sibling_index=1 (sole H2 in file).

### 5. TABLE_HEADER 2-row span (Hook A1) (1/1 PASS)

a012: line_start=15, line_end=16, diff=1 = v1.9 baseline 2-row standard (header + alignment). Both rows present in verbatim with embedded `\n` separator. Hook A1 PASS.

Style classification: **0 v1.8 pilot 1-row legacy / 1 v1.9 standard 2-row** (consistent with B-02 chapters/ era + B-03+ domains/ standard).

### 6. §D-5 bold-caption preserved (4/4 PASS)

| Atom | Caption | bold marker preservation |
|---|---|---|
| a006 | `**Rows 1-2:**` | `**` open + close byte-exact |
| a008 | `**Row 3:**` | `**` open + close byte-exact |
| a010 | `**Row 4:**` | `**` open + close byte-exact |
| a011 | `**bs.xpt**` | `**` open + close byte-exact |

All four bold markers preserved. None misclassified as NOTE (correct per §R-D5 — Row/Rows/filename ≠ Note/Exception literal).

### 7. §C-1 sub-line atomization legitimate (5/5 PASS)

| Source line | Atom count | Atoms | Legitimate? |
|---|---|---|---|
| L5 | 3 | a003, a004, a005 | YES — 3 grammatically distinct sentences (`This example shows...` + `The data collected focus...` + `It has been shown...`). |
| L7 | 2 | a006, a007 | YES — bold-caption sentence + tail explanation sentence. |
| L9 | 2 | a008, a009 | YES — bold-caption sentence + tail rationale sentence. |
| L11 | 1 | a010 | N/A — single coherent sentence with bold-caption prefix. |
| L13 | 1 | a011 | N/A — single bold-caption marker. |

Sub-line splits respect sentence boundaries (period + space). No fragments mid-sentence. Per §R-C1 and §C-1, sub-line SENTENCE atomization with same line_range is canonical, NOT FAIL_VERBATIM.

### 8. extracted_by (16/16 PASS)

All 16 atoms list:
- `subagent_type: general-purpose` ✓ (per kickoff §3 Writer pool, §D-8 peer-alternative)
- `prompt_version: P0_writer_md_v1.9.1` ✓ (round 01 baseline prompt)
- `ts: 2026-05-05T22:55:00Z` ✓ (uniform per-batch timestamp)

## Kickoff drift verification (per §R-D1 / Hook R24)

Independent grep verification of kickoff §0.5 numeric claims relevant to batch_20:

| Claim | Verify command | Match |
|---|---|---|
| BS/examples.md = 20 lines | `wc -l` source | ✓ 20 |
| BS/examples.md atoms expected ~16-20 | actual 16 atoms | ✓ in [16, 20] range |
| atom_id prefix `md_dmBS_ex_aNNN` | first/last atom_id check | ✓ a001..a016 |
| parent_section root `§BS [BS — Examples]` | a001 parent_section | ✓ |
| parent_section H2 `§BS.<N> [Example N]` | a002 parent_section | ✓ `§BS.1 [Example 1]` |

**No kickoff drift detected.** Writer atoms align with source AND kickoff numeric claims. INFO log only.

## Hook coverage checked

- Hook A1 (TABLE_HEADER 2-row): ✓ a012
- Hook A2 (HEADING `^#{1,6}\s+`): ✓ a001, a002
- Hook 22b (kickoff §0.5 grep checksum trust): ✓ kickoff §0.5 13/13 verified, writer trusted boundaries
- Hook D-NOTE-BQ (D-2): N/A (no blockquote NOTE in source)
- Hook D-D8 (D-4 numberless `## Overview` chapter root inherit): N/A (no `## Overview` in source)
- Hook A4 (FIGURE figure_ref non-null): N/A (no FIGURE atoms)
- Hook C-8 (file field `knowledge_base/` prefix): ✓ all 16 atoms
- Hook R-D5 (bold-caption SENTENCE accept): ✓ a006/a008/a010/a011 not faulted
- Hook R-D6 (TABLE_HEADER style classification): ✓ 1 v1.9 standard 2-row

## Defect findings

**None.** No HIGH / MEDIUM / LOW severity findings. No anomalies, no carry-forward candidates, no codification candidates.

## Stratified-sampling anomaly inclusion (per v1.9.1 §R-Stratified-Sampling)

Sampled 4 bold-caption SENTENCE instances (D-5 codified anomaly type) — all verified byte-exact preservation + canonical pattern adherence. ≥1 anomaly instance requirement met.

No NOTE-BQ / D5 dual-constraint / D8 chapter-root / mixed sib chain instances in this batch (none expected for examples.md domain file).

## Rule D verification

- Writer subagent_type: `general-purpose` ✓ (peer-alternative per §D-8)
- Reviewer subagent_type: `pr-review-toolkit:code-reviewer` ✓ (peer-alternative per §D-8)
- Distinct subagent_type: ✓ (general-purpose ≠ pr-review-toolkit:code-reviewer)
- Rule D 隔离硬约束 satisfied.

## Final verdict

**16/16 atoms PASS = 100%**, exceeds 90% PASS gate. 0 defects across 8-check matrix (verbatim / atom_type / parent_section / heading_meta / line_range / table_header_2row / bold_caption_preserve / extracted_by). Full-file audit yields no findings, no kickoff drift detected, Rule D 隔离 satisfied.

---

RULE_A_VERDICT: PASS
