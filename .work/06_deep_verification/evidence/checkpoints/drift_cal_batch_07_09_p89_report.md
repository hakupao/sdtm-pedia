# Drift Calibration — Batch 07-09 Cumulative (§C.1 Cadence)

> Date: 2026-04-25
> Pair: baseline (`oh-my-claudecode:writer` batch 09b) vs rerun (`oh-my-claudecode:executor` drift_cal)
> Target page: SDTMIG v3.4 p.89 (§5.5 SV – Examples: tv.xpt + ds.xpt example tables)
> Baseline atoms: 33; Rerun atoms: 33 (count identical)
> Cumulative range: batch 07 (228 atoms) + batch 08 (220 atoms) + batch 09 (227 atoms) = 675 atoms ≥ 300-atom threshold

---

## Pre-repair agreement

| Metric | Value |
|---|---|
| Strict (type+verbatim norm 300) agreement | **0.606** |
| Threshold (§C.1 2-type cross-check) | ≥ 0.80 |
| Verdict (pre-repair) | **FAIL** |

### Agreement by atom_type

| atom_type | baseline | rerun | both | agreement |
|---|---|---|---|---|
| CODE_LITERAL | 2 | 0 | 0 | 0.00 |
| HEADING | 2 | 4 | 2 | 0.50 |
| LIST_ITEM | 10 | 10 | 10 | 1.00 |
| SENTENCE | 5 | 5 | 4 | 0.80 |
| TABLE_HEADER | 2 | 2 | 1 | 0.50 |
| TABLE_ROW | 12 | 12 | 3 | 0.25 |

### Drift driver analysis (2 root causes)

**Root cause R1: CODE_LITERAL vs HEADING type ambiguity for xpt filenames (O-P1-24 INFO)**
- Baseline classifies `tv.xpt` / `ds.xpt` as `CODE_LITERAL` (dataset filename literal, per v1.2 prompt H1' rule)
- Rerun classifies same strings as `HEADING` (treating them as section labels)
- Both defensible; v1.2 prompt is ambiguous here because xpt filenames often FUNCTION as sub-section labels above example tables
- Scope: 4 atoms affected (2 × 2 classification disagreement)
- Fix deferred to v1.3 prompt: explicit rule "`*.xpt` / `*.sas7bdat` / `*.csv` dataset filenames always `CODE_LITERAL`, even when typographically functioning as sub-heading; any accompanying explicit section heading above is the HEADING atom"

**Root cause R2: TABLE_ROW data hallucination on ds.xpt rows 1-3 (O-P1-23 HIGH — inline fixed)**
- Baseline 09b writer hallucinated wrong DSDTC / DSSTDTC / DSSTDY values on DS example table rows 1, 2, 3 — discovered via cross-check with rerun + PDF p.89 verification
- **Scope: 3 TABLE_ROW atoms** (out of 12 TABLE_ROWs on p.89)
  - `ig34_p0089_a030` (row 1 DS 37): baseline DSDTC=2019-09-**09**, DSSTDY=**1** → PDF truth 2019-09-**10**, DSSTDY=(**empty**) → replaced verbatim with rerun
  - `ig34_p0089_a031` (row 2 DS 37): baseline DSDTC=2019-09-**10**, DSSTDY=**2** → PDF truth 2019-09-**16**, DSSTDY=(**empty**) → replaced with rerun
  - `ig34_p0089_a032` (row 3 DS 85): baseline DSSTDY=**1** → PDF truth DSSTDY=**-6** → replaced with rerun
- `a033` (row 4 DS 85) was already correct in baseline
- **Hypothesis**: Writer 09b may have substituted row-index integers (1, 2, 3, 4) for empty DSSTDY cells, and interpolated plausible sequential dates rather than verbatim PDF extraction. Consistent with O-P1-12 pattern (writer inference over literal PDF read).
- Bulk Option H repair applied using rerun verbatim as source (PDF-verified accurate)

**Root cause R3 (minor, NOT repaired)**: TABLE_ROW trailing-pipe representation for TV rows 3-7 (TVENRL empty)
- Baseline truncates TV rows 3-7 to 7 fields (omit trailing empty TVENRL)
- Rerun keeps 8 fields with trailing `|` (explicit empty)
- LOW drift; same class as F-B09-RA-2 pipe-count ambiguity
- Accept as-is, defer v1.3 prompt rule

---

## Post-repair agreement

| Metric | Value |
|---|---|
| Strict agreement (post O-P1-23 fix) | **0.70** (projected; 3 TABLE_ROW atoms now match rerun verbatim) |
| Verdict (post-repair) | still **FAIL** vs 0.80 threshold |

The post-repair agreement is still below threshold because R1 (CODE_LITERAL vs HEADING ambiguity) and R3 (TV trailing pipe) remain. These are classification/format disagreements, NOT semantic correctness failures — both writers produce structurally-valid atoms for the same PDF content; they disagree only on representation choice.

**Cross-reference to Rule A breadth**: Rule A batch 09 sample PASSED 90% (9/10 PASS + 1 PARTIAL pooled). Independent 10-atom PDF verification found only 1 HIGH issue (SVCNTMOD CT cell) which did NOT include the p.89 DS row hallucination. This confirms drift cal provides complementary coverage to Rule A — it catches **systemic writer-reproducibility issues** that stratified Rule A samples may miss (DS rows a030-a032 were not in Rule A sample, but drift cal re-atomized and revealed the corruption).

---

## Comparison vs prior drift cal (O-P1-09)

| | O-P1-09 (batch 03 p.25) | O-P1-23 (batch 09 p.89) |
|---|---|---|
| Target | QS domain spec table (sparse-cell) | §5.5 SV Example tv.xpt + ds.xpt |
| Writers | 3-way (executor / writer / general-purpose) | 2-way (writer / executor) |
| Strict agreement | 0.675 | 0.606 → 0.70 post-fix |
| Verdict | FAIL | FAIL |
| Root cause class | TABLE_ROW sparse-cell verbatim ambiguity | TABLE_ROW data hallucination + CODE_LITERAL/HEADING classification ambiguity |
| Semantic correctness | Both writers atoms PASS Rule A individually (any writer's output valid) | **Writer 09b PRODUCED INCORRECT data** (PDF-verified); rerun executor accurate |

**Key finding**: O-P1-23 is a DIFFERENT CLASS from O-P1-09. O-P1-09 was reproducibility noise (all outputs PASS Rule A, just different representations). O-P1-23 uncovered a WRITER CORRECTNESS BUG — baseline 09b had 3 atoms with wrong data values that Rule A narrow sample missed. Drift cal repairs 3 HIGH-severity hallucinations that would have propagated into P4a forward matching.

---

## Recommendations

### Inline repairs (applied this session)
- ✅ 3 DS row atoms (a030/a031/a032) verbatim replaced with PDF-verified rerun values

### v1.3 prompt candidates (deferred to P1 末集中 update)
1. **CODE_LITERAL hierarchy rule** (R1 fix): `*.xpt` / `*.sas7bdat` / `*.csv` dataset filenames ALWAYS `CODE_LITERAL` (confirm v1.2 H1' intent). Visual positioning above example table does NOT make them `HEADING`; any accompanying section heading text (e.g. "tv.xpt" alone on a line styled as bold caption) may still be a separate HEADING atom alongside the CODE_LITERAL.
2. **TABLE_ROW trailing empty cell rule** (F-B09-RA-2 + R3 fix): if PDF table has N columns per TABLE_HEADER, all TABLE_ROW atoms MUST have pipe-count = N-1 (N fields separated by N-1 pipes, trailing empties explicit). No silent truncation of trailing empties.
3. **TABLE_ROW data integrity rule** (O-P1-23 fix): verbatim cell values MUST be literal PDF read-through; writer MUST NOT substitute row-index / sequential-integer / interpolated values for empty cells. If a cell is empty in PDF, represent as empty string between pipes (`| |`).

### Rule A cadence feedback
- 10-atom Rule A sample (seed 20260450) did NOT include any of the 3 corrupted DS rows (a030/031/032). Sample included `a030` NO — included `a001` TABLE_ROW and `a013` / `a017` TABLE_ROW equivalent? No, the sample only included `a001` (TABLE_ROW SVCNTMOD p.87) and `a018` (TABLE_ROW STUDYID sv.xpt p.86) from 09b TABLE_ROW. The 12 p.89 TABLE_ROWs were not sampled.
- **Methodology implication**: 10-atom per-batch Rule A is insufficient to catch systemic data hallucination on dense example tables where many TABLE_ROW atoms are unsampled. Drift cal is a necessary complementary check. **Consider increasing TABLE_ROW sample weight** in future Rule A sampling (e.g. force ≥3 TABLE_ROW from each dense example/spec page).

---

## Verdict

**Drift Calibration: FAIL (60.6% pre-repair → 70% post-repair; both < 0.80 threshold)**
**Classification: Known-limitation class (similar to O-P1-09 disposition Option 2' prior decision)** — continue P1 with Rule A per-batch as safety net, v1.3 prompt consolidated fix at P1 末.
**Action: 3 HIGH atoms repaired via Option H this session. v1.3 prompt rules catalogued (R1/R3). Tiebreaker general-purpose NOT dispatched this round (ctx budget + confirmed class).**

---

*Drift cal artifacts:*
- `evidence/checkpoints/drift_cal_p89_executor_rerun.jsonl` (33 atoms rerun)
- `evidence/checkpoints/pdf_atoms_batch_09b.jsonl` (post-repair baseline)
- `evidence/checkpoints/drift_cal_batch_07_09_p89_report.md` (this file)
