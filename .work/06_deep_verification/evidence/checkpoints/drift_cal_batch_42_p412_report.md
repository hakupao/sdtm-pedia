# Drift Cal Batch 42 p.412 Report — 10th Cumulative + 6TH WRITER-DIRECTION VALUE HALLUCINATION RECURRENCE = v1.7 TRIGGER

- **Date**: 2026-04-29
- **Round**: 10 (multi-session, session C, batch 42)
- **Target page**: p.412 (§7.3.2 TD – Examples L4 + Example 1 L5 + figure + 3 LIST_ITEM bullets + td.xpt CODE_LITERAL + TABLE_HEADER + 3 TABLE_ROW)
- **Content type**: `examples_narrative_spec_table` (per v1.6 N18.a binding) + `mixed_structural_transition` adjacency
- **Drift cal carrier**: 10th cumulative (post round 9 batch 39 = 9th cumulative = 5th writer-direction VALUE HALLUCINATION recurrence on `mixed_structural_transition`)
- **N14 STRONGLY VALIDATED 4th live-fire** (round 7 batch 33 1st + round 8 batch 36 2nd + round 9 batch 39 3rd + round 10 batch 42 4th)
- **VERDICT**: 🔴 **CATASTROPHIC FAIL BOTH THRESHOLDS** + **6TH CUMULATIVE WRITER-DIRECTION VALUE HALLUCINATION RECURRENCE DETECTED** = v1.7 TRIGGER ESCALATION (deprecate writer-family entirely from P1 atomization)

## §1 Method (v1.6 N14 NEW EXECUTOR-VARIANT alternation pattern)

Per v1.6 N18 EXTENDED scope, writer-family is BANNED for ALL content in batch 42 (sub-rules a/b/d/e all triggered). Production atomization for both 42a + 42b dispatched executor-only (PDF-clean).

For drift cal direction-attribution validation, kickoff §3.3 codifies v1.6 NEW EXECUTOR-VARIANT alternation: baseline = `oh-my-claudecode:executor` (same as 42a production), rerun = `oh-my-claudecode:writer` (writer-family) for direction-attribution purpose ONLY. **Rerun atoms NOT merged to root regardless of verdict** (artifact preserved at `drift_cal_p412_writer_rerun.jsonl`).

| Baseline | Rerun |
|---|---|
| executor (42a production atoms p.412) | writer (drift_cal_p412_writer_rerun.jsonl) |

Pre-extraction: writer rerun agent did NOT read 42a output (independent reproduction confirmed via Agent prompt + DO NOT TOUCH section).

## §2 Dual-Threshold Metrics (v1.6 carry-forward NEW1)

| Metric | Value | Threshold | Verdict |
|---|---|---|---|
| Baseline atoms (42a p.412) | 17 | — | — |
| Writer rerun atoms (p.412) | 24 | — | — |
| Verbatim hash intersection | 6 | — | — |
| Verbatim hash union | 35 | — | — |
| **Strict count overlap** (\|intersection\|/max) | **25.0%** (6/24) | ≥80% | **🔴 FAIL** |
| **Verbatim hash Jaccard** (\|inter\|/\|union\|) | **17.1%** (6/35) | ≥80% | **🔴 FAIL** |

**Both thresholds FAIL**: YES → **DRIFT CAL VERDICT: CATASTROPHIC FAIL** (both-threshold halt-condition per kickoff §5.2 / §6 dual-<80% halt clause).

This is the LOWEST verbatim Jaccard recorded in P1 cumulative (round 5 batch 27 p.270 had 6.7% strict but here both metrics fail simultaneously — first time both metrics fail since round 1 of NEW1 codification).

## §3 Atom-by-Atom Divergence Analysis

PDF p.412 ground truth verified by main session via `Read source/SDTMIG v3.4 (no header footer).pdf p.411-420` pre-dispatch.

### §3.1 Granularity-only divergences (NOT VALUE HALLUCINATION)

Writer split content differently — soft atomicity rather than fabrication:

- Writer emitted 4 SENTENCE atoms (a001-a004) for the bottom-of-p.411 LIST_ITEM continuation that executor merged into LIST_ITEM atoms a001-a002.
- Writer split the figure caption SENTENCE into multiple atoms (a009-a012) where executor combined narrative SENTENCEs.
- Writer treated the schedule narrative bullets as inline SENTENCE+NOTE+SENTENCE+LIST_ITEM stream (a013-a019) where executor cleanly emitted as 3 LIST_ITEM bullets.

These are atom_type granularity differences. Content per se PDF-acceptable in both. Net effect: writer 24 vs executor 17 (writer over-split by 7).

### §3.2 ⚠️ HIGH VALUE HALLUCINATION — TABLE_HEADER ig34_p0412_a021 (writer-only)

**Writer rerun a021 verbatim**: `ROW | STUDYID | STUDYID | ARMCD | TDSEQ | TDDESC | TDSTOFF | TDANCVRF | TDEVALU1 | TDEVALU2 | TDEVALU3 | TDEVALU4 | TDNU...`

**PDF actual** (verified by main-session read): `Row | STUDYID | DOMAIN | TDORDER | TDANCVAR | TDSTOFF | TDTGTPAI | TDMINPAI | TDMAXPAI | TDNUMRPT`

**Executor baseline a014**: `| Row | STUDYID | DOMAIN | TDORDER | TDANCVAR | TDSTOFF | TDTGTPAI | TDMINPAI | TDMAXPAI | TDNUMRPT |` ✓ BYTE-EXACT to PDF.

**Hallucination breakdown**:
- `STUDYID` DUPLICATED (twice in writer header, once in PDF)
- `ARMCD` — NOT IN PDF (writer fabricated; ARMCD is a TA-domain variable, not TD)
- `TDSEQ` — NOT IN PDF (no such variable exists in TD spec on p.411)
- `TDDESC` — NOT IN PDF (writer fabricated; no such TD variable exists)
- `TDANCVRF` — NOT IN PDF (writer fabricated; actual variable is `TDANCVAR`)
- `TDEVALU1`, `TDEVALU2`, `TDEVALU3`, `TDEVALU4` — NOT IN PDF (writer fabricated; no such TD variables exist)
- `DOMAIN`, `TDORDER`, `TDANCVAR`, `TDTGTPAI`, `TDMINPAI`, `TDMAXPAI`, `TDNUMRPT` — MISSING from writer header (all in PDF)

**Classification**: 🔴 **TABLE_HEADER FABRICATION VALUE HALLUCINATION** — writer pulled column names from training-data templates of OTHER trial design domains (TA / generic CRF tables) instead of reading PDF verbatim. Same training-data-template motif as round 5+6+7+8+9 cumulative recurrences but extends to NEW MODE (TABLE_HEADER column-name fabrication, not just TABLE_ROW value drift).

**Disposition**: writer rerun is HALLUCINATED. Executor baseline matches PDF.

### §3.3 ⚠️ HIGH VALUE HALLUCINATION — TABLE_ROW ig34_p0412_a022/a023/a024 (writer-only)

Writer rerun TABLE_ROW values fabricated to match the fabricated TABLE_HEADER column count:

**a022** (Row 1):
- Writer: `1 | ABC123 | TD | 1 | ANCH1DT | P0D | P8W | P53D | P1W | | | | 6`
- PDF: `1 | ABC123 | TD | 1 | ANCH1DT | P0D | P8W | P53D | P9W | 6`
- Hallucinations: `P9W` → `P1W` (digit deletion); 3 EXTRA empty pipe pairs `| | | | 6` not in PDF; pipe count 14 vs PDF 11

**a023** (Row 2):
- Writer: `2 | ABC123 | TD | 2 | ANCH1DT | P48W | P12W | P1W | | | | 4`
- PDF: `2 | ABC123 | TD | 2 | ANCH1DT | P48W | P12W | P11W | P13W | 4`
- Hallucinations: `P11W` → `P1W` (digit deletion); `P13W` cell DROPPED; 4 EXTRA empty pipes; pipe count 13 vs PDF 11

**a024** (Row 3):
- Writer: `3 | ABC123 | TD | 3 | ANCH1DT | P96W | P24W | P23W | P25W | | | 12`
- PDF: `3 | ABC123 | TD | 3 | ANCH1DT | P96W | P24W | P23W | P25W | 12`
- Hallucinations: 3 EXTRA empty pipe cells; pipe count 13 vs PDF 11

**Executor baseline a015/a016/a017**: BYTE-EXACT to PDF (verified main-session).

**Classification**: 🔴 **TABLE_ROW VALUE HALLUCINATION** — exactly the round 5-9 cumulative motif (writer fabricates cell values from training-data templates instead of reading PDF verbatim). Compounded by fabricated TABLE_HEADER column count creating cascading column-misalignment.

## §4 6TH CUMULATIVE WRITER-DIRECTION VALUE HALLUCINATION RECURRENCE TRACKING

| Round | Batch | Drift cal page | Content type | Recurrence # | Motif |
|---|---|---|---|---|---|
| 5 | 28 | p.270 | examples_narrative_spec_table | 1st | TABLE_ROW VALUE HALLUCINATION (USUBJID/PCREFID/PCTESTCD INVENTED IDs) (O-P1-85) |
| 6 | 31 | p.293 | examples_narrative_spec_table | 2nd | TABLE_ROW VALUE HALLUCINATION (O-P1-103) |
| 7 | 34 | p.325 | examples_narrative_spec_table | 3rd | TABLE_ROW VALUE HALLUCINATION (O-P1-109) |
| 8 | 36 | p.357 | examples_narrative_spec_table | 4th | TABLE_ROW VALUE HALLUCINATION → halt → Option H bulk repair via executor rerun (round 8 batch 36) → triggered v1.5 N16 codification |
| 9 | 39 | p.382 | mixed_structural_transition | 5th | URL .org→.ch + word `clinical` deletion + TABLE_ROW Study cell ~26% TRUNCATION+REORDER (O-P1-134) → triggered v1.6 N18 EXTENDED scope codification |
| **10** | **42** | **p.412** | **examples_narrative_spec_table** ⚠️ | **6th** | **TABLE_HEADER FABRICATION** (TDDESC/TDANCVRF/TDEVALU1-4/STUDYID-duplicate/ARMCD/TDSEQ INVENTED columns) **+ TABLE_ROW VALUE FABRICATION** (P9W→P1W + P11W→P1W + P13W cell DROPPED) → **v1.7 TRIGGER ESCALATION**: deprecate writer-family entirely from P1 atomization |

**6th cumulative recurrence achieved**. CRITICALLY: this 6th occurrence is on **examples_narrative_spec_table** content type where v1.6 N18 EXPLICITLY BANS writer-family (sub-rule a). The drift cal rerun was dispatched per v1.6 NEW EXECUTOR-VARIANT alternation pattern (kickoff §3.3) for direction-attribution validation purpose — and the recurrence was DETECTED as expected (writer-direction VALUE HALLUCINATION CONFIRMED at content type N18 BANS).

**Direction**: REVERSED — baseline (executor) is PDF-correct; rerun (writer) is the hallucinated side. **DIRECTION REVERSED 13th cumulative occurrence.**
**Value-add**: drift cal caught what Rule A 10-atom sample missed (Rule A sample drew from 42a executor baseline = PDF-correct; would not detect rerun hallucination). **14th value-add precedent.**

## §5 v1.7 Trigger Decision Per Kickoff §0.4 + §5.3

Per kickoff §0.4 + §5.3 + v1.6 P0_writer_pdf §N18 last paragraph:

> "Halt threshold for 6th cumulative recurrence: deprecate writer-family entirely from P1 atomization (v1.7 candidate trigger)."

> "if drift cal p.412 reveals 6th cumulative recurrence DESPITE v1.6 N18 EXTENDED scope dispatch... ESCALATE to v1.7 trigger = deprecate writer-family entirely from P1 atomization. Action: write `halt_state_batch_42.md` + 4 resume options + halt signal `HALT_BATCH_42 reason=6th_writer_direction_recurrence_v1.7_trigger`."

**Test of N18 EXTENDED scope EFFECTIVENESS**: writer-direction VALUE HALLUCINATION on content type N18 BANS = N18 ban scope is JUSTIFIED (writer hallucinates exactly as designed-against). N18 is working as a prevention layer for production dispatch (production 42a + 42b correctly used executor-only and is PDF-clean per Rule A 95.0% PASS + schema sweep 0 violations + Hook 19 N20 URL cross-verify PDF-exact).

**v1.7 trigger ESCALATED**: v1.7 cut session must deprecate writer-family entirely from P1 atomization (writer-family becomes INELIGIBLE for ANY production atomization across ALL content types post v1.7 cut).

## §6 Halt Action Per Kickoff §6 + §0.4

**Halt analysis**:
- Drift cal both-thresholds halt: ✅ YES (strict 25.0% AND verbatim Jaccard 17.1% both <80%)
- N3 NEW8.d "5th cumulative recurrence" halt clause: ✅ YES (6th cumulative recurrence on TABLE_ROW + TABLE_HEADER VALUE)
- v1.6 N18 6th-recurrence halt threshold: ✅ YES (6th cumulative writer-direction VALUE HALLUCINATION on N18-banned content type)
- **Decision: HALT** (write `halt_state_batch_42.md` + emit `HALT_BATCH_42 reason=6th_writer_direction_recurrence_v1.7_trigger`)

**Important nuance**: production atoms 42a + 42b (217 atoms, executor-only, PDF-clean per schema sweep + Rule A + Hook 19 N20 cross-verify) are NOT affected by halt — drift cal rerun atoms NOT merged to root regardless. The halt is for v1.7 trigger ESCALATION to user (Option B/C/D applicable; Option A doesn't apply since no root atoms hallucinated).

## §7 Findings Filed

- **O-P1-145 HIGH** (from this drift cal) — **6TH cumulative writer-direction VALUE HALLUCINATION recurrence** on examples_narrative_spec_table content type DESPITE v1.6 N18 EXTENDED scope dispatch (writer was dispatched per v1.6 NEW EXECUTOR-VARIANT alternation pattern §3.3 for direction-attribution validation purpose; not in production scope; production-side N18 ban EFFECTIVE — production atoms executor-clean; rerun atoms NOT merged); v1.7 TRIGGER ESCALATION = deprecate writer-family entirely from P1 atomization

(O-P1-146..148 reserved unused unless additional findings surface from Rule A audit)

## §8 Disposition for Batch 42 Closure

- **42a (87 atoms p.411-415)**: KEEP. Executor-emitted, schema sweep PASS, Rule A audit PASS 95.0%, Hook 19 N20 PDF-cross-verify URL+identifier exact (incl. p.418 TS Assumption 5+8 URLs verified; p.420 TS Example 1 controlled-term identifiers verified).
- **42b (130 atoms p.416-420)**: KEEP. Executor-emitted, schema sweep PASS, Rule A audit included.
- **drift_cal_p412_writer_rerun.jsonl (24 atoms)**: PRESERVE as drift cal artifact (NOT merged to root pdf_atoms.jsonl); reference for v1.7 cut session.
- **Rule B backup**: not needed — 42a/42b atoms not modified post-drift-cal.

## §9 N14 STRONGLY VALIDATED Status Sustained (4th Live-Fire)

Round 7 batch 33 1st + round 8 batch 36 2nd + round 9 batch 39 3rd + round 10 batch 42 4th = STRONGLY VALIDATED status sustained at 4 cumulative live-fires of methodology. v1.6 NEW EXECUTOR-VARIANT alternation pattern (kickoff §3.3) is N14 4th live-fire successfully attributing direction (REVERSED — writer-side hallucination via baseline-PDF cross-check + rerun-PDF cross-check). N14 production-ready alternation methodology validated for cumulative 4 live-fires across content-type-binding constraint.

## §10 Rule 合规

- **Rule A**: 10-atom audit slot #54 general-purpose 4-burn extension PASS 95.0% (separate gate, complementary to drift cal)
- **Rule B**: not invoked (no Option H needed; 42a baseline PDF-correct; rerun NOT merged)
- **Rule C**: drift cal report + halt_state file + retro embedded in P1_batch_42_report.md (STEP 7) + reconciler-stage round 10 retro
- **Rule D**: writer rerun ≠ executor baseline (different subagent_type per N14 alternation); main session attribution INDEPENDENT of writer self-claim (writer claimed "all 20 hooks PASS" in WRITER_DRIFT_CAL_P412_DONE echo but PDF cross-check disproved 5+ hallucinated atoms = continued detection-not-prevention motif round 9 batch 39 + round 10 batch 42 = 2 cumulative confirmation that writer self-Validate hooks 17/20 are detection-not-prevention even with v1.6 N20 N=10 expansion + mandatory URL/DOI/citation + identifier cross-check; v1.7 may need further hardening)
- **Rule E**: O-P1-145 HIGH + v1.7 trigger ESCALATION filed for v1.7 cut session

## §11 v1.7 Candidate Stack (post round 10 batch 42)

1. **v1.7 PRIMARY: writer-family deprecation entirely from P1 atomization** (per N18 6th-recurrence halt threshold; this is THE v1.7 trigger; writer-family becomes INELIGIBLE for any production atomization across ALL content types — replaces N16 + N18 partial bans with complete ban).
2. **N19 Hook 18 promotion candidate**: round 9 + round 10 cumulative 5+ PARTIAL atoms on SENTENCE-paragraph-concat motif may justify promoting Hook 18 from WARN-mode to halt-on-violation (round 9 D-MS-NEW-9-2 candidate held over).
3. **N20 Hook 19 detection-not-prevention escalation REINFORCED**: round 9 batch 39 + round 10 batch 42 both = 2 cumulative writer self-claim "all hooks PASS" disproven by main-session PDF cross-check; N20 sample expansion to N=10 + mandatory URL/DOI/citation cross-check insufficient to catch TABLE_HEADER fabrication or cell-value drift; v1.7 may need either (a) full-table cross-verify mandatory for ALL TABLE_HEADER+TABLE_ROW atoms (no sample, full population) OR (b) writer-family deprecation makes Hook 19 irrelevant (since executor doesn't exhibit motif).

---

**Drift Cal Verdict**: 🔴 CATASTROPHIC FAIL BOTH THRESHOLDS + 6TH CUMULATIVE WRITER-DIRECTION VALUE HALLUCINATION RECURRENCE = v1.7 TRIGGER ESCALATION. Production atoms 42a + 42b executor-clean preserved. Halt signal `HALT_BATCH_42 reason=6th_writer_direction_recurrence_v1.7_trigger` per G-MS-4 STRONGLY VALIDATED protocol.
