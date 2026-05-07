# Rule A + Rule D Audit — P2 B-03c Round 11 batch_119 (SV/examples.md)

> Reviewer: `pr-review-toolkit:code-reviewer` (per-batch reviewer per kickoff §3 dispatch table step 12)
> Writer: `general-purpose` (≠ reviewer subagent_type — Rule D PASS)
> Prompt: `subagent_prompts/P0_reviewer_v1.9.3.md` (35 hooks)
> Audit timestamp: 2026-05-07
> Source: `knowledge_base/domains/SV/examples.md` (95 lines)
> Atoms file: `evidence/checkpoints/P2_B-03_batch_119_md_atoms.jsonl` (61 atoms a001..a061)

---

## Verdict: **PASS**

35/35 hooks PASS, 0 HIGH severity findings, 0 MED findings, 1 INFO carry-forward (§F-3 calibration delta 52.5% just above ±50% threshold — kickoff estimate range 30-50 mid 40 vs actual 61, driver = SENTENCE-heavy narrative density 27 SENTENCE atoms beyond pure table content).

---

## Audit summary

| Check | Result |
|---|---|
| Hook A1 byte-exact verbatim (61 atoms) | **PASS** 61/61 |
| §R-E1 12-field schema regression sweep | **PASS** 0 violations |
| §R-E2 H1 sib_idx=1 universal (a001) | **PASS** 1/1 |
| §R-E3 TABLE_HEADER sib=null + R-2.8-2 TABLE_ROW sib=null + hl=null | **PASS** 32/32 (3 TH + 29 TR) |
| §R-E4 extracted_by object schema (subagent_type/prompt_version/ts) | **PASS** 61/61 |
| §R-E5 non-HEADING field-explicit-null (heading_level + sibling_index) | **PASS** 59/59 non-HEADING |
| §R-E6 FIGURE-vs-CODE_LITERAL boundary | **N/A** 0 FIGURE atoms (0 mermaid in source — kickoff §0.5 row 17 verified) |
| §R-F-1 §2.11 Plan B sub-namespace 4-layer verify | **N/A** 0 H3 children (no §F-1 trigger; only 1 numbered H2 §2.5 self-namespace) |
| §R-F-2 atoms/line ratio 0.642 in band 0.59-0.85 | **PASS** within band (10th sustained validation cycle) |
| §R-F-3 kickoff atom estimate calibration | **INFO** delta 52.5% just above ±50% threshold (carry-forward; non-blocking) |
| §2.5 numbered H2 self-namespace (×1: `## Example 1`) | **PASS** verified below |
| atom_id uniqueness + sequential a001..a061 | **PASS** |
| parent_section consistency | **PASS** 2 distinct values (file-root + §SV.1) |
| Source coverage (non-blank lines) | **PASS** 64/64 non-blank lines covered, 31 blank lines uncovered (expected) |
| Line range overlap check | **PASS** 0 overlaps |
| Halt range [<15, >75] | **PASS** actual=61 within range |
| Rule D writer ≠ reviewer subagent_type | **PASS** writer=`general-purpose`, reviewer=`pr-review-toolkit:code-reviewer` |

---

## §2.5 numbered H2 ×1 sub-namespace verification

| Atom | Type | Line | parent_section | hl | sib | Verbatim |
|---|---|---|---|---|---|---|
| a001 | HEADING | L1 | `§SV [SV — Examples]` (file-root) | 1 | 1 | `# SV — Examples` |
| a002 | HEADING | L3 | `§SV [SV — Examples]` (file-root) | 2 | 1 | `## Example 1` |
| a003..a061 | non-HEADING | L5-95 | `§SV.1 [Example 1]` (H2 self-namespace) | null | null | (59 atoms) |

**§2.5 namespace bookkeeping**:
- H2 atom (a002) parent = file-root `§SV [SV — Examples]` ✓
- H2 atom (a002) sib_idx = 1 (first H2 in file) ✓
- 59 children (a003..a061) parent = `§SV.1 [Example 1]` (numbered H2 self-namespace by sib_idx 1) ✓
- 0 atoms with deviant parent_section ✓

---

## Rule A Semantic Sampling (15 atoms ≥10 required)

Stratified random sample seeded `random.seed(119)`:
- 2 HEADING (a001 H1, a002 H2 — exhaustive)
- 3 TABLE_HEADER (a010, a027, a046 — exhaustive: tv.xpt header, ds.xpt header, sv.xpt header)
- 5 SENTENCE (a008, a021, a036, a042, a044 — random)
- 5 TABLE_ROW (a014, a033, a050, a054, a057 — random)

| atom_id | Type | Lines | Semantic match | Notes |
|---|---|---|---|---|
| a001 | HEADING | L1 | ✓ | H1 file root |
| a002 | HEADING | L3 | ✓ | H2 numbered §2.5 |
| a010 | TABLE_HEADER | L19-20 | ✓ | tv.xpt header (2-line spanning) |
| a027 | TABLE_HEADER | L46-47 | ✓ | ds.xpt header (2-line spanning) |
| a046 | TABLE_HEADER | L79-80 | ✓ | sv.xpt header (2-line spanning) |
| a008 | SENTENCE | L15 | ✓ | Row 8 follow-up visit description |
| a021 | SENTENCE | L34 | ✓ | Row 2 screen failure description |
| a036 | SENTENCE | L59 | ✓ | Rows 2-3 normal completion |
| a042 | SENTENCE | L71 | ✓ | Row 13 WEEK 2 not occur due to clinic closure |
| a044 | SENTENCE | L75 | ✓ | Row 15 follow-up visit on study day 26 |
| a014 | TABLE_ROW | L24 | ✓ | tv.xpt row 4 WEEK 2 |
| a033 | TABLE_ROW | L53 | ✓ | ds.xpt row 6 WITHDRAWAL BY SUBJECT |
| a050 | TABLE_ROW | L84 | ✓ | sv.xpt row 4 SUBJECT LACKED TRANSPORTATION |
| a054 | TABLE_ROW | L88 | ✓ | sv.xpt row 8 WEEK 8 IN PERSON |
| a057 | TABLE_ROW | L91 | ✓ | sv.xpt row 11 DAY 1 IN PERSON |

**Rule A semantic pass rate: 15/15 = 100.0%** (≥90% threshold MET; 0 HIGH severity findings)

Cross_refs note: 0 `Section X.Y` patterns in source (grep `Section\s+\d+(?:\.\d+)*` returns 0 matches); 0 atoms with non-empty cross_refs — semantically appropriate (this is a domain examples file with no IG section back-references).

---

## §F-2 / §F-3 retrospectives (INFO carry-forward)

### §F-2 atoms/line ratio (10th sustained validation expected post-round-11)

batch_119 ratio = 61/95 = **0.642** — squarely within empirical band 0.59-0.85 (mid 0.72; round 04-10 baseline 0.602-0.782). No driver flag; SENTENCE+TABLE_ROW balanced atomization typical of Examples files with multiple xpt tables interspersed with row-by-row narrative.

### §F-3 kickoff estimate calibration

| Metric | Value |
|---|---|
| Kickoff §1 row 6 est range | 30-50 |
| Kickoff §0.5 row 23 round-mid heuristic | 0.73 × 95 = ~69 |
| Actual atoms | 61 |
| Mid (40) vs actual delta | 52.5% (just above ±50% threshold) |
| Driver | SENTENCE-heavy narrative (27 atoms, 44% of total) — kickoff §1 row 6 noted "35 table_rows" but undercounted SENTENCE coverage of multi-paragraph row-by-row exposition |
| Recommendation | INFO carry-forward; calibration improvement opportunity for Examples files with high narrative density (similar pattern: TD/ex L94 inflate noted). Not blocking. |

---

## Hook tally

35/35 v1.9.3 reviewer hooks PASS:
- v1.7 hooks 1-18: PASS
- v1.9 R22+R23: PASS
- v1.9.1 R24+R-D2..R-D6: PASS
- v1.9.2 R25+R-E2..R-E6: PASS
- v1.9.3 R-F-1 (N/A no trigger), R-F-2 (PASS in band), R-F-3 (INFO above threshold non-blocking)

---

## Final verdict

**PASS** — 0 HIGH severity, 0 MED, 1 INFO carry-forward (§F-3 calibration). Proceed to next batch (batch_120 TD/ass).
