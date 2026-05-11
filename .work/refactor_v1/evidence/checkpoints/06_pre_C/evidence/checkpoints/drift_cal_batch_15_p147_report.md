# Drift Calibration Report — batch 15 p.147 (Multi-Session Parallel)

> Date: 2026-04-25
> Trigger: every-3-batches cadence (last cal batch 12 p.118) + cumulative atoms ≥300 since p.118 (双触发 mandatory per kickoff)
> Target: p.147 §6.2.2 [Biospecimen Events (BE)] Examples — densest page in 15b (39 atoms baseline, mid-BE Examples spec/cross-domain table cluster: be.xpt continuation header + 4 rows + suppbe.xpt + 6 rows + bs.xpt + 7 rows + relspec.xpt + 6 rows)
> Strategy: 2-way (writer 15b baseline 39 atoms + Option C oh-my-claudecode:executor independent rerun 38 atoms)
> Outcome: **Strict count 97.4% (38/39) PASS @ ≥80% threshold; verbatim hash overlap 41% LOW → drove deep root-cause analysis revealing systemic writer 15b corruption across p.146-148 → escalated to Option E full-page replace × 3 + Option H sibling/References fix × 3**

---

## Metrics

| 指标 | 12b… wait, 15b writer (baseline) | executor (rerun) |
|---|---|---|
| Atoms | 39 | 38 |
| atom_type dist | TABLE_HEADER 4 / TABLE_ROW 23 / SENTENCE 3 / LIST_ITEM 6 / CODE_LITERAL 3 | TABLE_HEADER 3 / TABLE_ROW 23 / SENTENCE 9 / CODE_LITERAL 3 |
| Strict count match | 38/39 = **97.4%** | — |
| Verbatim hash set overlap | 16 / 39 = **41%** | 16 / 38 = **42%** |
| Threshold | ≥80% strict | strict PASS / verbatim LOW |
| Tiebreaker | NOT triggered | (root cause definitive — writer-family multi-bug pattern matching O-P1-12 / O-P1-23 / O-P1-34) |

## Root cause analysis (R1-R6)

### (R1) HIGH STUDIID typo across 8 atoms in 15b file (NOT just p.147) — Option E scope

PDF ground truth says `STUDYID` (standard CDISC variable name). Writer 15b wrote `STUDIID` (missing Y, extra I) consistently across all TABLE_HEADER and 1 TABLE_ROW atoms in 15b.

| atom_id | Field | 15b (corrupted) | PDF | Severity |
|---|---|---|---|---|
| ig34_p0146_a001 | bs.xpt header col 2 | `STUDIID` | `STUDYID` | HIGH typo |
| ig34_p0146_a010 | relrec.xpt header col 2 | `STUDIID` | `STUDYID` | HIGH typo |
| ig34_p0147_a001 | be.xpt cont header col 2 | `STUDIID` | `STUDYID` | HIGH typo |
| ig34_p0147_a010 | suppbe header col 2 | `STUDIID` | `STUDYID` | HIGH typo |
| ig34_p0147_a022 | bs.xpt header col 2 | `STUDIID` | `STUDYID` | HIGH typo |
| ig34_p0147_a033 | relspec header col 2 | `STUDIID` | `STUDYID` | HIGH typo |
| ig34_p0148_a003 | relrec header col 2 | `STUDIID` | `STUDYID` | HIGH typo |
| ig34_p0148_a016 | ce.xpt Row 1 col 1 | `STUDIID` | `STUDYID` | HIGH typo |

**Pattern**: Same writer-family hallucination as O-P1-23 batch 09 DSDTC + O-P1-34 batch 12 ECNKID/ECPSTRGUI. Drift cal value-add 超 Rule A 第 5 次 — Rule A 10-atom sample only had a chance at 1-2 of these in stratified design; drift cal full-page 2-way captured all 8.

### (R2) HIGH supple.xpt → suppbe.xpt typo (1 atom)

PDF p.147 clearly shows `suppbe.xpt` (the SUPPBE supplemental qualifier dataset for BE domain — standard SDTM naming). Writer 15b wrote `supple.xpt` (cross-confused with SUPPL prefix or partial typo).

- ig34_p0147_a009 CODE_LITERAL: `supple.xpt` → `suppbe.xpt` (HIGH typo)

### (R3) HIGH bs.xpt Row 3+4 BSTESTCD swap (2 atoms on p.147)

PDF p.147 bs.xpt Row 3 = VOLUME (Volume) / Row 4 = RIN (RNA Integrity Number) per "Rows 3-4 show volume and purity (integrity) of RNA sample" narrative. Writer 15b SWAPPED Row 3 ↔ Row 4 BSTESTCD/BSTEST/BSCAT data.

### (R4) HIGH relspec.xpt Row 5 REFID hallucination (1 atom on p.147)

PDF Row 5 REFID = `298R1-1R2`. Writer 15b wrote `298R1-1R1` (duplicate of Row 4's REFID). Same writer-family hallucination pattern.

### (R5) HIGH p.146 systemic under-extraction (writer 15b: 14 atoms vs executor: 32 atoms)

Writer 15b dropped:
- BS Example 1 narrative description (`The Device Identifiers (DI) dataset...`)
- relrec.xpt section (CODE_LITERAL + TABLE_HEADER + 4 TABLE_ROW)
- Example 2 HEADING + intro SENTENCE
- 6 LIST_ITEMs describing rows 1-6 of be.xpt Example 2 narrative
- be.xpt Example 2 CODE_LITERAL + TABLE_HEADER + 6 TABLE_ROW

Net: 18 atoms missed by writer 15b on p.146. Same pattern as O-P1-12 batch 06 writer page misattribution + under-extraction. Option E executor rerun (32 atoms) wholesale replaced writer 15b's 14 atoms.

### (R6) HIGH p.147/p.148 TABLE_HEADER cross-domain corruption + relrec.xpt Row 1+2 hallucination

- Writer 15b p.147 a001 be.xpt continuation TABLE_HEADER: incorrectly mixed BS columns into BE header (`BETESTEDCD | BETEST | BSCAT | BSORRES | BSORRESN |...` — these BS-prefixed columns don't belong in be.xpt). PDF actual columns: `BEREFID | BETERM | BEDECOD | BEPARTY | BEPRTYID | BECAT | VISITNUM | BEDTC | BESTDTC | BEENDTC`.
- Writer 15b p.148 a004 relrec.xpt Row 1: `1 | 3441271 | BE | MU-298 | BESEQ | 1 | MANY | 1` — should be `1 | 3441271 | BE | (empty USUBJID) | BEREFID | (empty IDVARVAL) | MANY | 1`. Hallucinated USUBJID + wrong IDVAR + wrong IDVARVAL.
- Writer 15b p.148 a005 relrec.xpt Row 2: similarly corrupted (RDOMAIN should be BS not BE; IDVAR should be BSREFID not BESEQ).
- Writer 15b p.147 a010/a022/a033 TABLE_HEADER drift: BSTESTEDCD (extra "ED"), BETESTEDCD (extra "ED"), QORHC (should be QORIG) — multiple column-name mutations.

## Repair scope applied

| # | Type | Pages | Atoms | Action |
|---|---|---|---|---|
| 1 | Option E p.146 wholesale replace | 14 → 32 atoms | -14, +32 net +18 | Executor rerun (`drift_cal_p146_executor_rerun.jsonl` 32 atoms PDF-verified). Backup pre-fix `pdf_atoms_batch_15b.jsonl.pre-OptionE-p146-148-OptionH-p147.bak`. |
| 2 | Option E p.147 wholesale replace + 1 manual leading TABLE_HEADER add | 39 → 39 atoms | -39, +38 (executor) +1 (manual be.xpt cont header per PDF) | Executor rerun (`drift_cal_p147_executor_rerun.jsonl` 38 atoms) + main_session manual `\| Row \| STUDYID \| DOMAIN \| USUBJID \| SPDEVID \| BESEQ \| BEREFID \| BETERM \| BEDECOD \| BEPARTY \| BEPRTYID \| BECAT \| VISITNUM \| BEDTC \| BESTDTC \| BEENDTC \|`. Note: executor missed the be.xpt continuation header which DOES exist on p.147 top per PDF. Convention drift LIST_ITEM→SENTENCE for "Row N:" descriptions accepted (LOW INFO defer v1.3). |
| 3 | Option E p.148 wholesale replace + schema normalize | 25 → 29 atoms | -25, +29 net +4 | Executor rerun (`drift_cal_p148_executor_rerun.jsonl` 29 atoms — schema bug `content`/`subagent_type` flat fields normalized to `verbatim`/`extracted_by` nested). Captures References HEADING + 2 LIST_ITEM citation entries (Tsui & Cerkovnik) that writer 15b dropped. Correct STUDYID + correct relrec rows 1/2 (empty USUBJID + BEREFID/BSREFID IDVAR). |
| 4 | Option H R15 cross-batch sibling continuity Example 1+2 | 2 atoms | 0 net | (a) `ig34_p0145_a004` "Example 1" SENTENCE → HEADING L5 sib=1 (15a writer originally tagged as SENTENCE; per BE-Examples L4 sib=4 convention, Examples are L5 children sib=1,2,...). (b) `ig34_p0146_a016` "Example 2" L4 sib=1 → L5 sib=2. Note: 15a Option H also required (originally clean batch needed sub-heading lift). |
| 5 | Option H References sib (per Rule A M-1) | 1 atom | 0 net | `ig34_p0148_a010` "References" L4 sib=null → L4 sib=5 (peer of BE-Description/Overview/Specification/Assumptions/Examples). Per Rule A reviewer slot #24 vercel:deployment-expert AUDIT-mode finding M-1: References should continue the §6.2.2 sub-heading sib chain since it appears as a peer-level sub-heading after BE-Examples. |
| 6 | Outer-pipe normalization | 90+ TABLE_HEADER/TABLE_ROW atoms | 0 net | Executor rerun TABLE_HEADER/TABLE_ROW atoms originally lacked outer `\| ... \|` pipes (executor convention); main session normalized to writer-family outer-pipe convention via post-processing (`normalize_outer_pipes`) for batch 15b internal consistency. O-P1-26 INFO defer v1.3 reaffirmed. |

## Tiebreaker decision: NOT TRIGGERED ✓

Per drift cal precedent (O-P1-12 batch 06 / O-P1-23 batch 09 / O-P1-34 batch 12), tiebreaker is required when FAIL root cause cannot be conclusively identified. Here:
- HIGH typos (STUDIID, supple, BSTESTEDCD, QORHC, BETESTEDCD): definitively root-caused to writer-family hallucination (executor + PDF agree as ground truth)
- HIGH data corruption (bs.xpt Row 3-4 swap, relspec REFID, relrec rows 1-2): same root cause
- HIGH under-extraction (p.146 14 vs 32): writer family page-shift / under-extraction, established Option E precedent
- Convention drift (LIST_ITEM vs SENTENCE, outer-pipe inconsistency, tab vs space): non-data interpretive choice; INFO defer v1.3

Therefore tiebreaker would not add information. Skip tiebreaker, apply Option E + Option H, document.

## Findings added

| ID | Severity | Summary |
|---|---|---|
| O-P1-36 | HIGH | Writer 15b STUDIID typo across 8 atoms (p.146 ×2 + p.147 ×4 + p.148 ×2) — systemic mis-spelling of standard CDISC variable name `STUDYID`. Same writer-family hallucination pattern as O-P1-23 (DSDTC) + O-P1-34 (ECNKID/ECPSTRGUI). 8 atoms repaired via Option E wholesale replace × 3 pages. |
| O-P1-37 | HIGH | Writer 15b suppbe.xpt → supple.xpt typo (1 atom p.147 a009). PDF ground truth `suppbe.xpt` (standard SUPPBE supplemental qualifier dataset for BE domain). Repaired via Option E p.147 wholesale replace. |
| O-P1-38 | HIGH | Writer 15b dense-table data corruption cluster on p.147 + p.148: (a) bs.xpt Row 3+4 BSTESTCD/BSTEST/BSCAT swap (Row 3 should be VOLUME, Row 4 should be RIN per PDF "Rows 3-4 show volume and purity"); (b) relspec.xpt Row 5 REFID hallucination (`298R1-1R1` duplicate of Row 4 vs PDF `298R1-1R2`); (c) relrec.xpt Rows 1+2 full-row data corruption (hallucinated USUBJID `MU-298` + wrong IDVAR `BESEQ`/wrong IDVARVAL `1` vs PDF empty USUBJID + `BEREFID`/`BSREFID` + empty IDVARVAL); (d) TABLE_HEADER cross-domain pollution (be.xpt header had BS-prefixed columns mixed in) + column-name typos (BSTESTEDCD/BETESTEDCD with extra ED, QORHC instead of QORIG). All repaired via Option E p.146/p.147/p.148 wholesale replace + 1 manual leading TABLE_HEADER add for p.147. |
| O-P1-39 | LOW | Cross-batch sibling continuity for "Example N" sub-headings under "BE – Examples" (L4 sib=4): writer 15a originally tagged "Example 1" on p.145 as SENTENCE (not HEADING); executor rerun on p.146 tagged "Example 2" as HEADING L4 sib=1 (wrong level + wrong sib continuation). Per batch 12 §6.1.3.3 Examples N L5 sib=1-N convention, batch 15 Examples N should also be L5 sib=1-N. 2 atoms inline Option H fix (Example 1 → L5 sib=1, Example 2 → L5 sib=2). Recommend v1.3 prompt: writer prompt to provide depth+1 convention from parent for sub-headings of numbered series; OR main session post-merge always sweeps cross-batch sibling continuity (already R15 NEW). |

## Cumulative drift cal track

| Run | Page | A | B | strict match | verbatim overlap | Root cause | Action |
|---|---|---|---|---|---|---|---|
| 30-page (batch 03) | p.25 | executor | writer | 67.5% / 37.5% / 37.5% (3-way) | — | QS sparse-cell PDF parse noise (O-P1-09) | continue + Rule A 加密 per-batch |
| 300-atom (batch 06) | p.60 | writer 06b | executor rerun | 17.6% strict | — | writer 06b page misattribution + CO under-extract (O-P1-12) | Option E rerun promoted to primary |
| 300-atom (batch 09) | p.89 | writer 09b | executor rerun | 60.6% pre-fix / 69.7% post-fix | — | writer 09b 3 DS row data hallucination + CT spec drift (O-P1-23) | Option H bulk fix using executor verbatim |
| 300-atom (batch 12) | p.118 | writer 12b | executor rerun | 48% strict | — | writer 12b 4-atom ec.xpt corruption (O-P1-34) + convention drift (O-P1-33 non-blocking) | 4-atom Option H targeted; convention defer v1.3 |
| **300-atom (batch 15)** | **p.147** | **writer 15b** | **executor rerun** | **97.4% strict / 41% verbatim overlap** | **41-42%** | **writer 15b multi-page systemic corruption: STUDIID×8 (O-P1-36) + supple→suppbe (O-P1-37) + bs/relrec/relspec data corruption + TABLE_HEADER cross-domain pollution (O-P1-38) + p.146 18-atom under-extraction** | **Option E p.146/p.147/p.148 wholesale replace × 3 + 1 manual leading TABLE_HEADER + 3 Option H (Example 1/2 sib continuity + References sib) — 6 repair cycles single batch NEW P1 MAX (vs batch 12's 5)** |

**Pattern stable across 5 drift cal runs**: writer family exhibits dense-table-row hallucination + under-extraction on every drift cal trigger; executor family does not. Root cause appears systemic to writer family's handling of dense spec/data tables. Confidence: writer-family bug class fully characterized.

**Strict-vs-verbatim divergence NEW lesson**: strict count 97.4% PASS hides 59% verbatim divergence due to systemic typos. Recommend v1.3: drift cal threshold should ALSO check verbatim hash overlap ≥80% (not just strict count) — if either fails, investigate. Add as `recommend_v1.3_drift_cal_dual_threshold`.

## Cross-reference

- O-P1-23 (batch 09): same writer-family DS hallucination pattern — drift cal value-add over Rule A precedent
- O-P1-12 (batch 06): writer page misattribution / under-extraction — Option E "rerun replaces baseline" precedent
- O-P1-34 (batch 12): writer ec.xpt 4-atom data corruption — same column-name + datetime hallucination pattern
- O-P1-26 (batch 10 INFO): TABLE_ROW pipe-format inconsistency — REAFFIRMED in batch 15 (executor no-outer-pipe vs writer outer-pipe convention drift)
- O-P1-32 (batch 12): cross-batch sibling_index continuity gap — REAFFIRMED in batch 15 (Example 1/2 sib + References sib)
