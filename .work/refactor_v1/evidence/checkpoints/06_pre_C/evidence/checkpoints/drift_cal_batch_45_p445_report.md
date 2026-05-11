# Drift Cal Batch 45 p.445 Report — 11th Cumulative + 1ST INAUGURAL v1.7 N21 BASELINE LIVE-FIRE — NEW class divergence (CANONICAL-FORM DELIMITER GRANULARITY, NOT VALUE HALLUCINATION)

- **Date**: 2026-04-29
- **Round**: 11 (multi-session, session C, batch 45) — **1st round running v1.7 baseline post v1.7 cut 2026-04-29 commit `6d19992`**
- **Target page**: p.445 — `Appendix A: CDISC SDS Team` L2 (sib=1 under §10 [APPENDICES] L1) contributor table continuation; ~70 individuals total spanning p.444+p.445 with mid-table TABLE_HEADER `Name | Company` repeat
- **Content type**: appendix narrative + N18.d VERBATIM-CRITICAL identifier (general identifier name+company TABLE_ROW)
- **Drift cal carrier**: 11th cumulative (post round 10 batch 42 = 10th cumulative = 6th writer-direction VALUE HALLUCINATION recurrence on `examples_narrative_spec_table` → v1.7 TRIGGER ESCALATION)
- **N14 STRONGLY VALIDATED 5th live-fire** (round 7 batch 33 1st + round 8 batch 36 2nd + round 9 batch 39 3rd + round 10 batch 42 4th + **round 11 batch 45 5th**)
- **v1.7 N21 baseline**: 1st INAUGURAL live-fire of N21 baseline drift cal validation
- **VERDICT**: 🟡 **GRANULARITY-DIVERGENCE FAIL BOTH NUMERIC THRESHOLDS but NOT VALUE HALLUCINATION** — v1.7 N21 production-side EFFECTIVE; writer rerun shows NEW class of writer-direction divergence (canonical-form delimiter granularity); halt NOT triggered per v1.7 N21 design (production atoms executor-clean, no executor-direction motif surfaced)

## §1 Method (v1.6 N14 NEW EXECUTOR-VARIANT alternation pattern, v1.7 N21 baseline)

Per v1.7 N21 PRIMARY EMERGENCY-CRITICAL writer-family complete deprecation, writer-family is BANNED for ALL P1 production atomization across ALL content types. Production atomization for both 45a + 45b dispatched executor-only (PDF-clean per Rule A 100.0% PASS slot #58 + schema sweep 0 errors).

For drift cal direction-attribution validation, kickoff §3.3 sustains v1.6 NEW EXECUTOR-VARIANT alternation pattern under v1.7 N21 §派发 `drift_cal_alternation_artifact` exception: baseline = `oh-my-claudecode:executor` (same as 45a production), rerun = `oh-my-claudecode:writer` (writer-family) for direction-attribution purpose ONLY. **Rerun atoms NOT merged to root regardless of verdict** (artifact preserved at `drift_cal_p445_writer_rerun.jsonl`).

| Baseline | Rerun |
|---|---|
| executor (45a production atoms p.445 subset, 40 atoms) | writer (drift_cal_p445_writer_rerun.jsonl, 40 atoms) |

Pre-extraction: writer rerun agent independent reproduction confirmed via Agent prompt INDEPENDENCE REQUIREMENT (rerun agent did NOT read 45a output; PDF-only source).

## §2 Dual-Threshold Metrics (NEW1 dual-threshold)

| Metric | Value | Threshold | Verdict |
|---|---|---|---|
| Baseline atoms (45a executor p.445) | 40 | — | — |
| Writer rerun atoms (p.445) | 40 | — | — |
| Verbatim hash intersection | 0 | — | — |
| Verbatim hash union | 80 | — | — |
| **Strict count overlap** (\|inter\|/max) | **0.0%** (0/40) | ≥80% | **🔴 FAIL** |
| **Verbatim hash Jaccard** (\|inter\|/\|union\|) | **0.0%** (0/80) | ≥80% | **🔴 FAIL** |

**Both thresholds FAIL by NUMERIC measure**: YES.

**HOWEVER**: see §3 — the divergence is **CANONICAL-FORM DELIMITER GRANULARITY only** (writer drops leading/trailing pipes from TABLE_ROW canonicalization), NOT VALUE HALLUCINATION. Every name + company semantic content is PDF-byte-exact on both sides. This is a **NEW class of writer-direction divergence** not seen rounds 5-10.

## §3 Atom-by-Atom Divergence Analysis

PDF p.445 ground truth verified by main session via `pdftotext -f 445 -l 445 -layout` pre-dispatch. Sample comparison (5 of 40 representative pairs):

| atom_id | Baseline (45a executor) | Rerun (writer) | Semantic content | Divergence type |
|---|---|---|---|---|
| a001 (TABLE_HEADER) | `\| Name \| Company \|` | `Name \| Company` | Name + Company columns | Delimiter-only |
| a002 (TABLE_ROW) | `\| Gbenga Ogunsulire \| Regeneron \|` | `Gbenga Ogunsulire \| Regeneron` | "Gbenga Ogunsulire" + "Regeneron" | Delimiter-only |
| a003 (TABLE_ROW) | `\| Debra O'Neill \| Merck & Co. \|` | `Debra O'Neill \| Merck & Co.` | "Debra O'Neill" + "Merck & Co." | Delimiter-only |
| a029 (TABLE_ROW) | `\| Anita Umesh \| \|` | `Anita Umesh` | "Anita Umesh" + (empty company) | Delimiter-only + empty-cell encoding loss |
| a040 (TABLE_ROW) | `\| Craig Zwickl \| Transendix LLC \|` | `Craig Zwickl \| Transendix LLC` | "Craig Zwickl" + "Transendix LLC" | Delimiter-only |

### §3.1 NOT VALUE HALLUCINATION

This is the **first cumulative drift cal in P1 where writer rerun divergence is content-preserving**:
- Every contributor name (~70 names) is PDF-byte-exact on both sides.
- Every company is PDF-byte-exact on both sides.
- No fabricated names (contrast round 5 USUBJID/PCREFID INVENTED + round 10 TDDESC/TDANCVRF INVENTED columns).
- No digit deletion (contrast round 10 P9W→P1W + P11W→P1W).
- No truncation (contrast round 9 Study cell ~26% TRUNCATION+REORDER).
- No column reordering or fabricated extra columns.

### §3.2 NEW class of writer-direction divergence — CANONICAL-FORM DELIMITER GRANULARITY

The systematic difference is delimiter convention:
- **Executor (baseline)**: emits TABLE_ROW with leading + trailing pipes per N5 standard markdown table form `| cell1 | cell2 |`.
- **Writer (rerun)**: emits TABLE_ROW WITHOUT leading + trailing pipes `cell1 | cell2`.

This produces a 100% verbatim hash mismatch despite 100% semantic content equivalence. The writer canonicalization style is internally consistent (all 40 rerun atoms use the same no-leading-trailing-pipe convention) but diverges from the executor's canonical N5 form.

### §3.3 Granularity divergence — empty-cell encoding loss (single instance)

For contributor row a029 ("Anita Umesh" with no company column shown in PDF):
- Baseline: `| Anita Umesh | |` (encodes empty cell explicitly per N3 NEW8.d whole-row + N5 pipe-count consistency)
- Rerun: `Anita Umesh` (drops empty cell delimiter; loses cell-count info)

Information loss in rerun (1 atom of 40, 2.5%): empty cell collapsed. Still NOT VALUE HALLUCINATION (no fabricated content), but slight ambiguity reduction in rerun's representation.

## §4 11TH CUMULATIVE DRIFT CAL + Cumulative writer-direction recurrence tracking

| Round | Batch | Drift cal page | Content type | Recurrence # | Motif |
|---|---|---|---|---|---|
| 5 | 28 | p.270 | examples_narrative_spec_table | 1st | TABLE_ROW VALUE HALLUCINATION (USUBJID/PCREFID/PCTESTCD INVENTED IDs) (O-P1-85) |
| 6 | 31 | p.293 | examples_narrative_spec_table | 2nd | TABLE_ROW VALUE HALLUCINATION (O-P1-103) |
| 7 | 34 | p.325 | examples_narrative_spec_table | 3rd | TABLE_ROW VALUE HALLUCINATION (O-P1-109) |
| 8 | 36 | p.357 | examples_narrative_spec_table | 4th | TABLE_ROW VALUE HALLUCINATION → halt → Option H bulk repair → triggered v1.5 N16 codification |
| 9 | 39 | p.382 | mixed_structural_transition | 5th | URL .org→.ch + word `clinical` deletion + TABLE_ROW Study cell ~26% TRUNCATION+REORDER (O-P1-134) → triggered v1.6 N18 EXTENDED scope codification |
| 10 | 42 | p.412 | examples_narrative_spec_table | 6th | TABLE_HEADER FABRICATION + TABLE_ROW VALUE FABRICATION (O-P1-145) → triggered v1.7 N21 COMPLETE BAN codification |
| **11** | **45** | **p.445** | **appendix narrative + N18.d VERBATIM-CRITICAL identifier** ⚠️ | **NOT a 7th** | **CANONICAL-FORM DELIMITER GRANULARITY divergence (NEW CLASS)** — content-preserving (every name+company byte-exact); NOT VALUE HALLUCINATION; NOT counted as 7th cumulative writer-direction VALUE HALLUCINATION recurrence |

**Critical finding for v1.7 N21 baseline 1st INAUGURAL drift cal validation**:
- Under v1.7 N21 design, "7th cumulative writer-direction VALUE HALLUCINATION recurrence is impossible by construction" since writer is NOT used in production. Round 11 batch 45 drift cal CONFIRMS this — production atoms (45a+45b executor-only) are clean (Rule A 100.0% PASS + schema sweep 0 errors).
- The writer rerun did NOT exhibit the rounds 5-10 cumulative VALUE HALLUCINATION motif. The divergence is canonical-form delimiter only.
- This may reflect content-type sensitivity: rounds 5-10 cumulative recurrences were on `examples_narrative_spec_table` (5 of 6) + `mixed_structural_transition` (1 of 6). Round 11 batch 45 p.445 is `appendix narrative + N18.d VERBATIM-CRITICAL identifier (contributor name+company)` — a content type writer-family had NOT been observed to fabricate on. Hypothesis: writer-family fabrication motif is **content-type-conditional**, with simple identifier+identifier 2-column tables (Appendix A name+company) staying PDF-correct, but spec-table-with-CDISC-Notes-column or domain-Examples tables triggering fabrication.
- Alternative hypothesis: writer canonicalization style drift (no-leading-trailing-pipe convention) is a separate motif from VALUE HALLUCINATION.
- Both hypotheses are consistent with v1.7 N21 baseline production-side discipline (executor-only) being EFFECTIVE.

**Direction**: REVERSED — baseline (executor) is PDF-correct + canonical N5 form; rerun (writer) is PDF-correct semantic content but non-canonical delimiter form. **DIRECTION REVERSED 14th cumulative occurrence (writer-side divergence) but FIRST INSTANCE of content-preserving divergence**.
**Value-add**: drift cal caught what Rule A 10-atom sample missed (Rule A sample drew from 45a executor baseline = PDF-correct; would not detect rerun delimiter form drift). **15th value-add precedent.**

## §5 v1.7 N21 baseline halt analysis (per kickoff §0.4 + §5.2-5.3 + §6)

Per kickoff §5.3 expected outcomes under v1.7 N21 baseline:

> **Most likely**: production 45a + 45b executor-clean per v1.7 N21 prevention layer; writer rerun continues to fabricate examples_narrative_spec_table or mixed_structural_transition content = EXPECTED validation of N21 ban scope; halt NOT triggered for writer-direction recurrence (artifact NOT merged); **DOCUMENT in `drift_cal_batch_45_p445_report.md`** that 7th-recurrence at writer-direction is CONTROLLED by N21 ban (NOT v1.7 halt threshold).
> **Less likely but possible**: executor-direction motif surfaces in 45a or 45b production atoms = **NEW class of failure** not seen rounds 5-10; halt-on-violation per Hook 19 + ESCALATE to v1.8 trigger candidate.

**Actual outcome**: Neither expected scenario exactly. Production 45a + 45b executor-clean as expected. Writer rerun divergence is NEW CLASS — canonical-form delimiter granularity, NOT VALUE HALLUCINATION. This is a third path not anticipated in kickoff §5.3.

**Halt analysis**:
- Drift cal both-thresholds halt (legacy v1.6 carry-forward N1): NUMERIC values fail thresholds (strict 0% AND verbatim Jaccard 0% both <80%) BUT the divergence is content-preserving canonical-form drift, NOT VALUE HALLUCINATION. The threshold's design intent (catch VALUE HALLUCINATION via verbatim mismatch) is not violated. **Disposition**: numeric-threshold trip is technical-not-substantive; halt NOT escalated.
- N3 NEW8.d "5th cumulative recurrence" halt clause (legacy carry-forward): NOT triggered (not a writer-direction VALUE HALLUCINATION recurrence; this is a NEW class).
- v1.7 N21 NEW halt clause (executor-direction motif in baseline): NOT triggered (production 45a + 45b executor-clean per Rule A 100.0% PASS + schema sweep 0 errors).
- **Decision**: NO HALT. Continue to STEP 6 evidence write + STEP 7 DONE echo.

**Important nuance**: production atoms 45a + 45b (312 atoms total, executor-only, PDF-clean per schema sweep + Rule A 100.0%) are NOT affected. Drift cal rerun atoms NOT merged to root regardless. The numeric threshold trip is a technical artifact of the writer rerun's non-canonical delimiter convention; it does not reflect content fidelity issues.

## §6 v1.7 N21 baseline 1st INAUGURAL live-fire VALIDATION

Round 11 batch 45 drift cal = **1st INAUGURAL live-fire of v1.7 N21 baseline drift cal validation**:

1. **N21 ban scope validation (production-side)**: PROVEN EFFECTIVE — production 45a (139 atoms) + 45b (173 atoms) = 312 atoms total, executor-only, schema-clean (0 errors), Rule A 100.0% PASS slot #58 Plan AUDIT-mode pivot. v1.7 N21 production-side prevention layer working as designed.
2. **N21 ban scope validation (artifact-side via EXECUTOR-VARIANT alternation)**: PROVEN EFFECTIVE BUT WITH NUANCE — writer rerun did NOT exhibit rounds 5-10 cumulative VALUE HALLUCINATION motif on this content type (appendix narrative + N18.d VERBATIM-CRITICAL identifier). Instead exhibited NEW class divergence (canonical-form delimiter granularity). This validates that N21 COMPLETE BAN was the correct escalation level — under partial bans (N16 + N18), writer would have been used for production on this content type and the canonical-form drift would have shipped to root atoms; under N21 COMPLETE BAN, executor canonicalization is enforced for production.
3. **N14 STRONGLY VALIDATED status sustained 5th live-fire**: Round 7 batch 33 1st + round 8 batch 36 2nd + round 9 batch 39 3rd + round 10 batch 42 4th + **round 11 batch 45 5th** = STRONGLY VALIDATED status sustained at 5 cumulative live-fires.
4. **EXECUTOR-VARIANT alternation pattern under v1.7 N21**: continues to deliver direction-attribution capability (writer-side divergence detected and characterized as NEW class). Pattern remains production-ready.

## §7 Findings Filed

- **No new findings raised** (no Rule A blockers; no halt triggered; production atoms clean).
- **OBS-A LOW** (informational, from Rule A): `ig34_p0444_a018` page_region heuristic borderline call — leave to reconciler post-fix queue.
- **OBS-B INFORMATIONAL (NEW v1.7 N21 baseline drift cal observation)**: Writer-family canonical-form delimiter granularity divergence (no-leading-trailing-pipe convention) on contributor table content type. Not a Rule A blocker, not a halt trigger, but a NEW class of writer-direction divergence to track in v1.8 candidate stack:
  - Hypothesis A (content-type-conditional fabrication): writer-family fabricates on `examples_narrative_spec_table` + `mixed_structural_transition` but stays content-correct on `appendix narrative + N18.d VERBATIM-CRITICAL identifier` simple 2-column tables.
  - Hypothesis B (canonical-form drift independent of fabrication): writer-family table-row canonicalization drifts toward minimal-delimiter convention regardless of content type. Round 5-10 fabrication motif may have masked this delimiter drift previously.
  - Round 12+ test: drift cal on simple 2-column glossary or fragment table from Appendix B/D batch (round 11 batch 46 territory) would discriminate hypotheses.

(O-P1-157..160 reserved unused — no new findings warranting an O-P1-NN finding ID.)

## §8 Disposition for Batch 45 Closure

- **45a (139 atoms p.441-445)**: KEEP. Executor-emitted, schema sweep PASS 0 errors, Rule A audit PASS 100.0% slot #58 Plan, Hook 19 N20 PDF-cross-verify URL exact (https://www.cdisc.org/standards/foundational/medical-devices-sdtmig/ verified in §9.1).
- **45b (173 atoms p.446-450)**: KEEP. Executor-emitted, schema sweep PASS 0 errors, Hook 19 N20 PDF-cross-verify URLs exact (https://www.cdisc.org/standards/terminology/controlled-terminology + https://www.cancer.gov/research/resources/terminology/cdisc verified in Appendix C).
- **drift_cal_p445_writer_rerun.jsonl (40 atoms)**: PRESERVE as drift cal artifact (NOT merged to root pdf_atoms.jsonl); reference for v1.8 candidate stack hypothesis testing.
- **Rule B backup**: not needed — 45a/45b atoms not modified post-drift-cal.
- **OBS-A page_region fix**: defer to reconciler scope per kickoff §8.

## §9 N14 STRONGLY VALIDATED Status Sustained (5th Live-Fire)

Round 7 batch 33 1st + round 8 batch 36 2nd + round 9 batch 39 3rd + round 10 batch 42 4th + **round 11 batch 45 5th** = STRONGLY VALIDATED status sustained at 5 cumulative live-fires of N14 strict alternation methodology. v1.6 NEW EXECUTOR-VARIANT alternation pattern (kickoff §3.3) under v1.7 N21 baseline successfully attributing direction (REVERSED — writer-side canonical-form drift via baseline-PDF cross-check + rerun-PDF cross-check). N14 production-ready alternation methodology validated for cumulative 5 live-fires across content-type variation.

## §10 Rule 合规

- **Rule A**: 10-atom audit slot #58 Plan (single-agent family 2nd burn extension after #46 INAUGURAL round 8) PASS 100.0% (separate gate, complementary to drift cal)
- **Rule B**: not invoked (no Option H needed; 45a/45b baselines PDF-correct; rerun NOT merged)
- **Rule C**: drift cal report (this file) + Rule A summary + P1_batch_45_report.md (STEP 7) + reconciler-stage round 11 retro pending
- **Rule D**: writer rerun (`oh-my-claudecode:writer`) ≠ executor baseline (`oh-my-claudecode:executor`) per N14 alternation; main session attribution INDEPENDENT of writer self-claim (writer claimed "all 20 hooks PASS" in WRITER_DRIFT_CAL_P445_DONE echo and the canonical-form drift was caught by main-session post-rerun Python comparison, not by writer self-Validate hooks; this is consistent with round 9-10 cumulative observation that writer self-Validate hooks 17/20 are detection-not-prevention; v1.7 N20 carry-forward Hook 19 N=10 sample insufficient to catch delimiter-style divergence).
- **Rule E**: OBS-B INFORMATIONAL (canonical-form delimiter granularity NEW class) filed for v1.8 candidate stack.

## §11 v1.8 Candidate Stack (post round 11 batch 45)

Non-blocking observations queued to v1.8 candidate stack:

1. **OBS-B (INFORMATIONAL, NEW class)**: Writer-family canonical-form delimiter granularity divergence — characterize content-type-conditional vs canonical-form-drift hypotheses via round 12+ drift cal on simple 2-column tables (glossary/fragment).
2. **OBS-A (LOW, page_region heuristic refinement)**: borderline page_region attribution for L1 chapter NEW transitions; v1.8 candidate to refine page_region heuristic OR codify "L1 chapter NEW transition page_region = `middle`" convention.
3. **Carry-forward v1.7 cut F2 LOW**: N22/AD "executor self-claim trust profile" wording placement refinement (functional but could be cleaner).
4. **Round 11+ executor-direction motif watch (v1.7 N21 §N21 last paragraph)**: under N21 design, 7th-recurrence writer-direction impossible. Round 11+ watch for executor-direction NEW motif. Round 11 batch 45 confirms NO executor-direction motif on appendix narrative + N18.d VERBATIM-CRITICAL identifier content type. Continue watch round 12+ on different content types.
5. **Hook 19 N20 detection-not-prevention 3rd cumulative confirmation**: Round 9 batch 39 1st + round 10 batch 42 2nd + round 11 batch 45 3rd = writer self-Validate hooks 17/20 detection-not-prevention status sustained at 3 cumulative confirmations (this round = canonical-form drift not caught by writer self-claim "all hooks PASS"). v1.7 N23 codified "RENDERED MOOT by N21 since executor doesn't exhibit motif" — round 11 batch 45 EXPANDS the "writer self-claim untrustworthy" finding from VALUE HALLUCINATION to canonical-form drift, but consequence (use executor for production) remains correct.

---

**Drift Cal Verdict**: 🟡 **GRANULARITY-DIVERGENCE FAIL BOTH NUMERIC THRESHOLDS but NOT VALUE HALLUCINATION** — production atoms 45a + 45b executor-clean preserved. v1.7 N21 PRODUCTION-SIDE EFFECTIVE. NEW class of writer-direction divergence (canonical-form delimiter granularity) characterized. NO HALT. Continue to STEP 6/7 closure.
