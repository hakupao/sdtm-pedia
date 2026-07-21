# Rule A audit — P2 B-03c batch_122 (TA/assumptions.md)

> Round: 12 | Batch: 122 | Source: `knowledge_base/domains/TA/assumptions.md` (29L) | Atoms: 16
> Reviewer prompt: `P0_reviewer_v1.9.3` | Subagent family: pivot from writer (independent Rule D)
> Timestamp: 2026-05-07

## §0 Sample selection method

- **N = 16 (full cohort, exhaustive audit)** — per round 11 small-batch precedent (≤25 atoms): `N = total atoms`, no random sampling needed because exhaustive run is cheaper than seed bookkeeping
- Selection seed: N/A (exhaustive)
- Audit script: in-line `python3` byte-exact compare of each atom's `verbatim` field against `knowledge_base/domains/TA/assumptions.md` lines `[line_start, line_end]` (rstrip `\n` only); plus 12-field schema sweep + parent_section literal compare + hook checks

## §1 Per-dimension PASS rate (16 atoms)

| Dimension | PASS | Total | Rate |
|---|---|---|---|
| Verbatim (byte-exact vs source line span) | 16 | 16 | 100.00% |
| Schema (12 fields + 9-enum + §2.9 + §E-5) | 16 | 16 | 100.00% |
| parent_section (§TA [TA — Assumptions] file-root) | 16 | 16 | 100.00% |
| Hooks (§E-1/E-2/E-4/E-5/§2.9/Hook D-NOTE-BQ N/A) | 16 | 16 | 100.00% |

## §2 Weighted overall PASS rate

- **Weighted dim PASS rate**: (16+16+16+16) / (4 × 16) × 100 = **100.00%**
- **Per-atom overall PASS**: 16 / 16 = **100.00%**
- Round 12 §4 halt #2 threshold (≥ 90%): **PASS** (100% well above floor)

## §3 Findings

- **HIGH severity**: 0
- **MED severity**: 0
- **LOW INFO**: 1 (see §4)

No atom-id collisions (writer report grep-verified 0 prior `md_dmTA_assn_a*` in master).
No schema regression. No 9-enum violation. No `extracted_by` shape violation.
No §2.9 LIST_ITEM `sib_idx` non-null (all 14 LIST_ITEM atoms have `sibling_index: null` explicit).
No §E-2 H1 `sib_idx` violation (a001 = 1).
No §E-5 non-HEADING field-explicit-null violation (a002..a016 all have `heading_level: null` AND `sibling_index: null` explicitly written).

## §4 §F-2 ratio observation (LOW INFO)

- **Ratio**: 16 / 29 = **0.552**
- **Empirical band v1.9.3**: 0.59-0.85 (9-round baseline 0.602-0.782 sustained)
- **Out-of-band**: yes, just below lower bound (-0.038 from 0.59)
- **Halt-band check**: round 12 kickoff §4 halt #8 specifies <50% halt — 0.552 is **above 0.500 floor**, **NOT a halt**, INFO-only
- **Driver classification**: source-structure driven, NOT extraction issue
  - File is small (29 lines) with 12 numbered top-level narrative LIST_ITEMs (each typically 1-4 sentences kept atomic per LIST_ITEM convention) + 2 sub-items 10.a/10.b
  - Each numbered item spans 1 source line (no multi-line wrap), so atom count cannot exceed line count
  - Blank lines between items inflate denominator: 12 blank lines + 1 H1 + 1 intro + 12 numbered + 1 sub-bullet header (10:) + 2 sub-items = 29L vs 16 atoms (blank lines are non-atomized scaffolding)
  - Pattern matches band-lower-tail expectation per round 08 INFO-R08-01 codification (small-ass.md heavy structure) and is consistent with QS/ass batch_90 0.286 territory pattern (milder here because TA/ass has 14 LIST_ITEMs vs QS heavy compression)
- **Verdict**: **INFO acceptable**, source-structure driver verified by line inventory; no extraction issue; carry-forward to round-close mini-audit per §R-F-2 non-blocking

## §5 §F-3 kickoff estimate calibration (LOW INFO, sub-threshold)

- Kickoff §0.5 row 24 estimate: 9-15 atoms (mid = 12)
- Actual: 16
- delta_pct vs upper bound: (16 - 15) / 15 × 100 = **+6.7%** (well below 50% threshold)
- delta_pct vs mid: (16 - 12) / 12 × 100 = **+33.3%** (still below 50% threshold)
- **No carry-forward INFO needed** per §R-F-3 (calibration well within tolerance band)

## §6 §F-1 §2.11 Plan B verification

- §F-1 trigger: **N/A** (0 numberless H2 in 29L source; pure file-root scope)
- No 4-layer namespace audit needed
- Backward compat: SUSTAINED (no regression flag — file is single-section H1-only)

## §7 v1.9.3 §F-1 backward compat sweep

- v1.9.2 archived rules ALL carry-forward verified PASS in this batch (Hook 22c 12-field; Hook E-2-1 H1 sib=1; Hook E-3-2 TABLE_HEADER N/A; Hook E-4-3 extracted_by object; Hook E-5 non-HEADING null explicit)
- §2.11 Plan B regression: 0 (out-of-scope; no H2)
- §2.7 Plan A regression: 0 (out-of-scope; no H2)
- 10th sustained validation cycle for `extracted_by` object schema (post v1.9.2 cut)

## §8 Cross-check writer self-report (P2_B-03_batch_122_report.md)

- Writer atoms-total claim 16: VERIFIED (byte-exact wc -l of JSONL)
- Writer atom_type distribution claim (1 H + 1 SENT + 14 LI): VERIFIED
- Writer §F-2 ratio claim 0.552: VERIFIED
- Writer §F-3 calibration claim +6.7%: VERIFIED
- Writer Hook A4 cross_ref claim (a002 captures §5.2/§5.3): VERIFIED (a002.cross_refs = ["§5.2","§5.3"])
- Writer schema-sweep claim PASS_12_12: VERIFIED (16/16 atoms have all 12 fields explicit)
- 0 contradiction between writer report and reviewer audit

## §9 DONE marker

`REVIEWER_122_DONE pass_rate=100.00%_16_of_16 dim_verbatim=16/16 dim_schema=16/16 dim_parent_section=16/16 dim_hooks=16/16 findings_HIGH=0 findings_MED=0 findings_LOW=1`
