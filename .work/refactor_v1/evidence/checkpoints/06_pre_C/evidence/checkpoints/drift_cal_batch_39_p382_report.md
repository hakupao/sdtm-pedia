# Drift Cal Batch 39 p.382 Report — 9th Cumulative + N14 STRONGLY VALIDATED 3rd Live-Fire

- **Date**: 2026-04-29
- **Round**: 9 (multi-session, session C, batch 39)
- **Target page**: p.382 (§7 TRIAL DESIGN MODEL DATASETS L1 NEW chapter — first L1 transition in P1 cumulative)
- **Content type**: `mixed_structural_transition` (per v1.5 N16 dispatch table)
- **Drift cal carrier**: 9th cumulative (post round 8 batch 36 = 8th cumulative writer-direction VALUE HALLUCINATION 4th cumulative recurrence)
- **N14 STRONGLY VALIDATED 3rd live-fire** (round 7 batch 33 1st + round 8 batch 36 2nd + round 9 batch 39 3rd)

## §1 Method

**Baseline subagent**: `oh-my-claudecode:executor` (batch 39a, 22 atoms p.382)
**Rerun subagent**: `oh-my-claudecode:writer` (drift cal, 22 atoms p.382)

Per v1.4 N14 STRONGLY VALIDATED post 2nd live-fire alternation table:
| Baseline | Rerun |
|---|---|
| executor | writer |

Per v1.5 N16 EMERGENCY-CRITICAL dispatch: writer acceptable for `mixed_structural_transition` (free choice; N16 ban applies only to `examples_narrative_spec_table` content). Writer rerun N16-compliant.

Pre-extraction: rerun agent did NOT read baseline output (independent reproduction).

## §2 Dual-Threshold Metrics

| Metric | Value | Threshold | Verdict |
|---|---|---|---|
| Strict count overlap | **100.0%** (22/22) | ≥80% | **PASS** |
| Verbatim hash Jaccard | **69.2%** (18/26 union) | ≥80% | **FAIL** |
| Verbatim intersection / max | 81.8% (18/22) | ≥80% (not formal threshold) | borderline |

**Both thresholds pass**: NO → **DRIFT CAL VERDICT: FAIL** (single-threshold FAIL, not both → NOT halt-condition per kickoff §5 / §6 dual-<80% halt clause).

## §3 Atom-by-Atom Divergence (4 of 22 = 18.2% divergent)

PDF p.382 ground truth verified by main session via `Read source/SDTMIG v3.4 (no header footer).pdf p.382` post-drift-cal.

### Atom 1: ig34_p0382_a001 (HEADING) — R10 whitespace drift (MINOR)
- **Baseline**: `"7  Trial Design Model Datasets"` (2 spaces between "7" and "Trial")
- **Rerun**:    `"7 Trial Design Model Datasets"` (1 space)
- **PDF ground truth**: shows wide whitespace between "7" and "Trial" — likely tab character rendered as multiple spaces; either 1-space or 2-space form is borderline-acceptable per R10 verbatim, but baseline preserved wider-form.
- **Classification**: R10 whitespace drift (MINOR — not VALUE HALLUCINATION; semantic content identical)
- **Disposition**: writer-side R10 normalization tendency; 39a baseline preferred for ledger merge.

### Atom 2: ig34_p0382_a004 (SENTENCE) — URL VALUE HALLUCINATION ⚠️ HIGH
- **Baseline**: `"...available at http://www.ich.org/products/guidelines/), Section 9.1..."`
- **Rerun**:    `"...available at http://www.ich.ch/products/guidelines/), Section 9.1..."`
- **PDF ground truth**: confirms `http://www.ich.org/products/guidelines/` (`.org`, NOT `.ch`)
- **Classification**: **URL VALUE HALLUCINATION** — writer fabricated `.ch` (Switzerland country-code TLD) where PDF has canonical `.org`. ICH is the International Council for Harmonisation; its actual domain is `ich.org`. The `.ch` substitution is plausibly motivated by ICH's Geneva headquarters but is NOT verbatim and is FACTUALLY WRONG.
- **Disposition**: rerun is HALLUCINATED, baseline is PDF-correct. v1.5 N17 Hook 17 multi-axis spot-check N=3 should have caught this if the random sample included a004 — but writer self-claim "17/17 hooks PASS" suggests Hook 17 did NOT catch it (either sample missed or hook is procedural-not-evidential).

### Atom 3: ig34_p0382_a017 (SENTENCE) — WORD DELETION VALUE HALLUCINATION ⚠️ HIGH
- **Baseline**: `"See the CDISC Glossary (...) for more complete definitions of clinical trial and objective."`
- **Rerun**:    `"See the CDISC Glossary (...) for more complete definitions of trial and objective."`
- **PDF ground truth**: confirms `"definitions of clinical trial and objective"` (with "clinical")
- **Classification**: **WORD DELETION VALUE HALLUCINATION** — writer dropped "clinical" word.
- **Disposition**: rerun is HALLUCINATED. Hook 17 spot-check did NOT catch.

### Atom 4: ig34_p0382_a022 (TABLE_ROW Study cell) — TEXT TRUNCATION + REORDER VALUE HALLUCINATION ⚠️ HIGH
- **Baseline length**: 1032 chars
- **Rerun length**: 758 chars (271-char shorter, ~26% truncation)
- **First divergence at char 406**: baseline `"...associated with the epoch has an associated treatment strategy..."` vs rerun `"...associated with the treatment epoch, 1 for each arm..."` (text REORDERED + DROPPED middle content about "associated treatment strategy" + truncated tail)
- **PDF ground truth**: full Study cell Definition cell paragraph (~1030 chars) describing study cells, treatment strategy, 3-arm parallel trial example, and chemotherapy/cycle complex example. **BASELINE matches PDF, RERUN truncated and reordered**.
- **Classification**: **TEXT TRUNCATION + REORDER VALUE HALLUCINATION** — most severe writer-direction motif in this drift cal (~26% of cell content fabricated/dropped).
- **Disposition**: rerun is SEVERELY HALLUCINATED. Hook 17 spot-check did NOT catch.

## §4 Cumulative Writer-Direction Main-Line VALUE HALLUCINATION Tracking

| Round | Batch | Drift cal page | Content type | Recurrence # | Motif |
|---|---|---|---|---|---|
| 5 | 28 | p.270 | examples_narrative_spec_table | 1st | TABLE_ROW VALUE HALLUCINATION (O-P1-85) |
| 6 | 31 | p.293 | examples_narrative_spec_table | 2nd | TABLE_ROW VALUE HALLUCINATION (O-P1-103) |
| 7 | 34 | p.325 | examples_narrative_spec_table | 3rd | TABLE_ROW VALUE HALLUCINATION (O-P1-109) |
| 8 | 36 | p.357 | examples_narrative_spec_table | 4th | TABLE_ROW VALUE HALLUCINATION (round 8 batch 36 → halt → Option H bulk repair) → triggered v1.5 N16 codification |
| **9** | **39** | **p.382** | **mixed_structural_transition** ⚠️ | **5th** | **URL + WORD DELETION + TEXT TRUNCATION VALUE HALLUCINATION (3 atoms)** |

**5th cumulative recurrence achieved**. CRITICALLY: this 5th occurrence is on **mixed_structural_transition** content type where N16 PERMITS writer-family (free choice). Writer was dispatched per N16 permission, NOT in violation of N16. The motif extends BEYOND Examples-narrative+spec-table content type to general structural+sentence content.

**Direction**: REVERSED — baseline (executor) is PDF-correct; rerun (writer) is the hallucinated side. DIRECTION REVERSED 12th cumulative occurrence.
**Value-add**: drift cal caught what Rule A 10-atom sample missed (Rule A sample drew from 39a baseline = PDF-correct; would not detect rerun hallucination). 13th value-add precedent.

## §5 N16 Escalation Decision

Per kickoff §6 + v1.5 N16 EMERGENCY-CRITICAL:
> if 5th cumulative writer-direction main-line VALUE HALLUCINATION recurrence detected DESPITE N16 dispatch ban, ESCALATE per v1.5 N16 escalation clause (mandatory writer-family ban for ALL TABLE_ROW-heavy content type)

**Nuance**: this 5th recurrence is NOT "DESPITE N16 dispatch ban" — writer was permitted by N16 for mixed_structural_transition. So the strict condition is not met. BUT the SUBSTANCE is more severe: writer-direction VALUE HALLUCINATION extends to content types N16 currently permits.

**Recommendation: v1.6 N16.b extension (NEW writer-side patch)** — broaden writer-family ban beyond Examples-narrative+spec-table to ANY content with embedded URLs, citations, or paragraph-prose ≥500 chars. Specifically:

**v1.6 N16.b draft** (for v1.6 cut session, drafted now):
> "Writer-family BANNED for any of: (a) Examples-narrative + spec-table content type [carry-forward N16 v1.5]; (b) SENTENCE atoms containing URLs (regex `https?://`) or DOI references; (c) TABLE_ROW atoms with cell content ≥500 chars; (d) any content where verbatim drift could fabricate identifier/citation values. Executor-family MANDATORY for these. Round 9 batch 39 5th cumulative writer-direction recurrence proves N16 v1.5 scope insufficient — VALUE HALLUCINATION extends to mixed_structural_transition content."

**Halt analysis**:
- Drift cal both-thresholds halt: NO (strict 100% PASS)
- N3 NEW8.d "5th cumulative recurrence" halt clause from kickoff §5: AMBIGUOUS — N3 specifically targets TABLE_ROW whole-row VALUE; here only 1 of 3 hallucinations is TABLE_ROW (a022 truncation, not whole-row identifier swap). Liberal reading triggers halt; strict reading does not.
- Decision: **NOT halt**. 39a/39b root atoms (145 cumulative) are executor-clean per schema sweep + Rule A audit + this drift cal validation (39a baseline atoms are PDF-correct; only writer rerun is hallucinated). Continuing to STEP 7 with finding filed.

## §6 Findings Filed

- **O-P1-133 MEDIUM** (from Rule A) — SENTENCE-paragraph-concat motif on §7 narrative pages (4/10 sample atoms PARTIAL on verbatim granularity); v1.6 candidate item Z; recurrence-watch round 10
- **O-P1-134 HIGH** (from this drift cal) — 5th cumulative writer-direction VALUE HALLUCINATION recurrence on mixed_structural_transition content type (URL fabrication + word deletion + text truncation/reorder); v1.6 EMERGENCY ESCALATION candidate N16.b broadening writer-family ban scope; ESCALATE BEFORE round 10 batch 42 next mandatory drift cal

## §7 Disposition for batch 39 Closure

- **39a baseline (22 atoms p.382)**: KEEP. Executor-emitted, PDF-verified correct via main session post-drift-cal cross-check.
- **39a/39b full output (145 atoms total)**: KEEP. Schema sweep PASS, Rule A 90% PASS, executor-only (no writer rerun atoms merged).
- **drift_cal_p382_writer_rerun.jsonl (22 atoms)**: PRESERVE as drift cal artifact (NOT merged to root pdf_atoms.jsonl); reference for v1.6 cut session.
- **Rule B backup**: not needed — 39a/39b atoms not modified post-drift-cal.

## §8 N14 STRONGLY VALIDATED Status Sustained

Round 7 batch 33 1st + round 8 batch 36 2nd live-fire = STRONGLY VALIDATED post 2nd live-fire (codified in v1.5 P0_writer_pdf §STATUS PROMOTIONS). Round 9 batch 39 = 3rd live-fire of the **methodology** (executor↔writer alternation enables direction-attribution; here REVERSED direction = writer-side hallucination, attributed correctly). N14 STRONGLY VALIDATED status sustained → production-ready alternation methodology validated for cumulative 3 live-fires.

## §9 Rule 合规

- **Rule A**: Rule A 10-atom audit slot #50 omc:planner PASS 90% (separate gate, complementary to drift cal)
- **Rule B**: not invoked (no Option H needed; 39a baseline PDF-correct)
- **Rule C**: drift cal report + retro embedded in P1_batch_39_report.md (STEP 7)
- **Rule D**: writer rerun ≠ executor baseline (different subagent_type per N14 alternation); main session attribution INDEPENDENT of writer self-claim (writer claimed "17/17 hooks PASS" but PDF cross-check disproved 3 atoms — Rule D writer/reviewer isolation upheld writer-direction skepticism)
- **Rule E**: O-P1-134 HIGH + v1.6 N16.b ESCALATION candidate filed for v1.6 cut session

## §10 v1.6 Candidate Stack (post round 9 batch 39)

1. **N16.b** (EMERGENCY-CRITICAL post 5th cumulative recurrence): writer-family ban broadening — see §5 draft
2. **Item Z** (MEDIUM, from Rule A finding O-P1-133): SENTENCE-paragraph-concat detection hook + writer prompt narrative-chapter exemplar
3. **OBS-1/2/3** (carry-forward from v1.5 cut codex audit): reviewer item W grep tightening + sweep count source-of-truth normalization + slot ordinal vs cumulative total derivation
4. **OBS-4** (NEW from STEP 4 schema sweep): N17 Hook 15 strict reading "same parent_section → same pipe-count" fails when one Example has multiple tables (Trial Design Matrix 5-pipe + ta.xpt 12-pipe both parent="§7.2.1 TA – Example 1"); refine hook to (parent_section, table_id) granularity
5. **OBS-5** (NEW from drift cal): writer self-Validate hooks 17 are detection-not-prevention; need pre-DONE PDF-cross-verify sample expanded from N=3 to N=10 OR mandatory cross-check for atoms with URLs/citations

---

**Drift Cal Verdict**: FAIL (single-threshold) + 5th cumulative writer-direction VALUE HALLUCINATION recurrence + v1.6 N16.b ESCALATION candidate filed. NOT halt. Batch 39 atoms (executor-clean) PROCEED to STEP 7.
