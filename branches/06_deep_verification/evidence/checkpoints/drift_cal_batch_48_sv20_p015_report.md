# Drift Cal Batch 48 sv20 p.15 Report — 12th Cumulative + 2ND v1.7 N21 BASELINE LIVE-FIRE + 1ST IN sv20 PDF — MULTI-MOTIF (VALUE HALLUCINATION 7TH CUMULATIVE + CANONICAL-FORM DRIFT 2ND + ENUM FABRICATION NEW CLASS)

- **Date**: 2026-04-30
- **Round**: 12 (multi-session, session C, batch 48) — **2nd round running v1.7 baseline post round 11 1st INAUGURAL EFFECTIVE 2026-04-30 commit `dd67cee`**
- **Target page**: sv20 p.15 — §3.1.2 The Events Observation Class L3 NEW chapter-start (sib=2 under §3.1) + L4 sub-heading "Events—Topic and Qualifier Variables—One Record per Event" + 12-column spec table (TABLE_HEADER + rows 1-8: --TERM through --HLT)
- **Content type**: `mixed_structural_transition` chapter-start + 12-column spec table model-level narrative content (CRITICAL: DIFFERENT content profile from round 11 batch 45 appendix-table — discriminator for H_A vs H_B per round 11 G-MS-NEW-11-1)
- **Drift cal carrier**: 12th cumulative (post round 11 batch 45 = 11th cumulative = NEW class canonical-form delimiter granularity content-preserving NOT VALUE HALLUCINATION; cumulative writer-direction VALUE HALLUCINATION count was 6 entering round 12)
- **N14 STRONGLY VALIDATED 6th live-fire** (round 7 batch 33 1st + round 8 batch 36 2nd + round 9 batch 39 3rd + round 10 batch 42 4th + round 11 batch 45 5th + **round 12 batch 48 6th**)
- **v1.7 N21 baseline 2nd cumulative live-fire** (1st INAUGURAL was round 11 batch 45) + **1st cumulative drift cal in sv20 PDF source (Pool 2)** vs all 11 prior in ig34 PDF
- **VERDICT**: 🔴 **CATASTROPHIC FAIL BOTH NUMERIC THRESHOLDS + MULTI-MOTIF SIMULTANEOUS** — v1.7 N21 production-side EFFECTIVE; writer rerun shows 3 simultaneous distinct motifs co-occurring: (1) VALUE HALLUCINATION (rounds 5-10 motif type) = **7TH CUMULATIVE WRITER-DIRECTION VALUE HALLUCINATION RECURRENCE** at writer-direction in artifact direction only; (2) CANONICAL-FORM DELIMITER GRANULARITY DRIFT (round 11 NEW class motif) **2ND CUMULATIVE** on different content type; (3) **NEW round 12 motif: atom_type ENUM FABRICATION** (`SECTION_HEADING` not in 9-enum) — **3RD DISTINCT WRITER-DIRECTION MOTIF CLASS**. Halt NOT triggered per v1.7 N21 design (writer-direction recurrence in artifact-only direction = BY DESIGN per §派发 `drift_cal_alternation_artifact` exception; production atoms 48a + 48b executor-clean per Rule A 100.0% PASS slot #61 codex:codex-rescue + schema 0 errors).

## §1 Method (v1.6 N14 NEW EXECUTOR-VARIANT alternation pattern, v1.7 N21 baseline 2nd cumulative)

Per v1.7 N21 PRIMARY EMERGENCY-CRITICAL writer-family complete deprecation, writer-family is BANNED for ALL P1 production atomization across ALL content types. Production atomization for both 48a + 48b dispatched executor-only via single-dispatch pattern (round 11 batch 46 NEW PRECEDENT carry-forward; agent ID `a6b579a3ab318f1e0`); production 150 atoms total (48a 92 + 48b 58) PDF-clean per Rule A 100.0% PASS slot #61 codex:codex-rescue + schema sweep 0 errors + 0 sv20 header/footer leak.

For drift cal direction-attribution validation, kickoff §3.3 sustains v1.6 NEW EXECUTOR-VARIANT alternation pattern under v1.7 N21 §派发 `drift_cal_alternation_artifact` exception: baseline = `oh-my-claudecode:executor` (same as 48b production p.15 subset, 15 atoms), rerun = `oh-my-claudecode:writer` (writer-family, agent ID `ada01604b94988674`) for direction-attribution purpose ONLY. **Rerun atoms NOT merged to root regardless of verdict** (artifact preserved at `evidence/checkpoints/drift_cal_sv20_p015_writer_rerun.jsonl`, 11 atoms).

| Baseline | Rerun |
|---|---|
| executor (48b production atoms p.15 subset, 15 atoms) | writer (drift_cal_sv20_p015_writer_rerun.jsonl, 11 atoms) |

Pre-extraction independence: writer rerun agent independence requirement enforced via Agent prompt explicit DO-NOT-READ pdf_atoms_batch_48*.jsonl directive; rerun read PDF source only.

## §2 Dual-Threshold Metrics (NEW1 dual-threshold)

| Metric | Value | Threshold | Verdict |
|---|---|---|---|
| Baseline atoms (48b executor p.15) | 15 | — | — |
| Writer rerun atoms (p.15) | 11 | — | — |
| Verbatim hash intersection | 2 | — | — |
| Verbatim hash union | 24 | — | — |
| **Strict count overlap** (\|inter\|/max) | **13.3%** (2/15) | ≥80% | **🔴 FAIL** |
| **Verbatim hash Jaccard** (\|inter\|/\|union\|) | **8.3%** (2/24) | ≥80% | **🔴 FAIL** |

**Both thresholds FAIL by NUMERIC measure**: YES → matches kickoff §5.2 legacy `both-thresholds halt` numeric trip. **HOWEVER**: see §3 + §5 — writer-direction VALUE HALLUCINATION (rounds 5-10 motif type) co-occurs with canonical-form delimiter granularity drift (round 11 NEW class motif type) AND with NEW round 12 motif atom_type ENUM FABRICATION. Each motif independently triggers numeric mismatch; their compound effect drives the catastrophic verbatim hash Jaccard 8.3%.

Strict count overlap (2/15 = 13.3%) tracks cleanly to: writer emitted only the 2 HEADING atoms with verbatim text matching executor (`3.1.2 The Events Observation Class` + `Events—Topic and Qualifier Variables—One Record per Event`) — but writer encoded those 2 atoms with `atom_type=SECTION_HEADING` (NOT 9-enum). Verbatim hash matches because hash is computed on `verbatim` field only.

Verbatim hash Jaccard 8.3% (2/24) = LOWEST verbatim Jaccard recorded in P1 cumulative across 12 drift cals (TIES round 11 batch 45 0.0% LOWEST; round 10 batch 42 17.1%; previous LOWEST exclusive of zeros was round 5 batch 28 6.7% strict).

## §3 Atom-by-Atom Divergence Analysis

PDF p.15 ground truth verified by main session via `pdftotext -layout -f 10 -l 19` (rule_a_batch_48_pdf_groundtruth.txt) + Read pages=10-19 visual inspection pre-dispatch.

### §3.1 ⚠️ HIGH WRITER-DIRECTION VALUE HALLUCINATION (7th cumulative recurrence at writer-direction in artifact direction; rounds 5-10 motif type)

**Row 1 --TERM** (sv20_p0015_a004 writer):
- Writer verbatim: `1 | --TERM | Reported Term | Char | | Topic | | | C825/1 | The collected name for an event observation. | The verbatim or prespecified name of the event. | RESPONSE*: "NON-MEDICAL REASON"`
- Executor baseline (sv20_p0015_a008): `| 1 | --TERM | Reported Term | Char | | Topic | | | C82571 | The collected name for an event observation. | The verbatim or prespecified name of the event. | |`
- PDF actual (groundtruth lines 312-315): C-code `C82571` / Examples cell BLANK
- **Hallucinations**:
  - C-code `C82571` → `C825/1` (digit `7` deleted, `/` inserted = digit-deletion + non-alphanumeric character fabrication; identical motif class to round 10 batch 42 p.412 P9W→P1W digit deletion)
  - Examples cell `RESPONSE*: "NON-MEDICAL REASON"` FABRICATED — this string is the Examples cell of row 39 `--ADJ` (Reason for Dose Adjustment) in the **Interventions Observation Class** spec table (different table, different page p.14-15 boundary). Writer cross-contaminated row 1 of Events table with Examples cell of row 39 of Interventions table = TABLE_ROW value cross-table cell migration motif (analogous to round 10 batch 42 ARMCD/TDSEQ/TDDESC TABLE_HEADER fabrication motif at TABLE_ROW Examples-cell scope).

**Row 2 --MODIFY** (sv20_p0015_a005 writer):
- Writer verbatim: `2 | --MODIFY | Modified Reported Term | Char | | Synonym Qualifier | --TERM | | C170908 | An alteration to a collected value for coding. | If the modified text is required for coding purposes, then the modified text is recorded in this variable. | RESPONSE: "NAUSEA"`
- Executor baseline (sv20_p0015_a009): `| 2 | --MODIFY | Modified Reported Term | Char | | Synonym Qualifier | --TERM | | C170998 | A value which represents an alteration to a collected value for coding purposes. | If the value for --TERM is modified for coding purposes, then the modified text is placed here. | |`
- PDF actual: C-code `C170998` / Definition `A value which represents an alteration to a collected value for coding purposes.` / Notes `If the value for --TERM is modified for coding purposes, then the modified text is placed here.` / Examples BLANK
- **Hallucinations**:
  - C-code `C170998` → `C170908` (digit fabrication 998→908; mid-string digit substitution)
  - Definition paraphrased: writer dropped `A value which represents` + truncated `coding purposes` → `coding`
  - Notes paraphrased: writer rewrote `If the value for --TERM is modified for coding purposes, then the modified text is placed here.` → `If the modified text is required for coding purposes, then the modified text is recorded in this variable.` (semantic drift: PDF says `placed here`, writer says `recorded in this variable`)
  - Examples cell `RESPONSE: "NAUSEA"` FABRICATED — PDF row 2 Examples cell is BLANK

**Row 5 --DECOD** (sv20_p0015_a008 writer):
- Writer verbatim Definition cell: `Standardized or codified name assigned to the description of an event or intervention.`
- Executor baseline + PDF actual: `Standardized or dictionary-derived text for the description of an event or intervention.`
- **Hallucination**: `dictionary-derived text` → `codified name assigned` (synonym substitution paraphrase = R10 violation; semantically related but byte-non-exact)

**Row 6 --EVDTYP** (sv20_p0015_a009 writer):
- Writer verbatim: `6 | --EVDTYP | Medical History Event Date Type | Char | | Variable Qualifier | --STDC; --EVTDC; only | MH domain only | | Specifies the aspect of the medical history event by which events are grouped. MH/MHDTC and/or the MHENDTC is defined. | "DIAGNOSIS"; "SYMPTOM ONSET"; "DISEASE RELAPSE"`
- Executor baseline + PDF actual: `| 6 | --EVDTYP | Medical History Event Date Type | Char | | Variable Qualifier | --STDTC; --ENDTC | MH domain only | | Specifies the aspect of the medical condition or event by which MHSTDTC and/or the MHENDTC is defined. | | "DIAGNOSIS", "SYMPTOM ONSET", "DISEASE RELAPSE" |`
- **Hallucinations**:
  - Variable(s) Qualified: `--STDTC; --ENDTC` → `--STDC; --EVTDC; only` (3 distinct VARIABLE NAME FABRICATIONS in single cell — `--STDC` is not a CDISC SDTM variable; `--EVTDC` is not a CDISC SDTM variable; trailing `; only` is leakage from neighboring `Usage Restrictions` cell `MH domain only`)
  - Definition mangled completely: `Specifies the aspect of the medical condition or event by which MHSTDTC and/or the MHENDTC is defined.` → `Specifies the aspect of the medical history event by which events are grouped. MH/MHDTC and/or the MHENDTC is defined.` (writer fabricated phrase `events are grouped` not in PDF; truncated `MHSTDTC` → `MH/MHDTC` corruption with backslash invented)
  - Examples format drift: `"DIAGNOSIS", "SYMPTOM ONSET", "DISEASE RELAPSE"` (comma-separated per PDF) → `"DIAGNOSIS"; "SYMPTOM ONSET"; "DISEASE RELAPSE"` (semicolon-separated)

**Row 8 --HLT** (sv20_p0015_a011 writer):
- Writer verbatim Definition cell: `The High Level Term in the primary hierarchy assigned to the event from MedDRA.`
- Executor baseline + PDF actual: `The high-level term from the primary hierarchy assigned to the event from MedDRA.`
- **Hallucinations**:
  - Capitalization drift: `high-level term` → `High Level Term` (proper-noun fabrication; PDF uses lowercase `high-level term` per definition style)
  - Hyphen drift: `high-level` → `High Level` (hyphen deleted)
  - Word substitution: `from the primary hierarchy` → `in the primary hierarchy`

### §3.2 CANONICAL-FORM DELIMITER GRANULARITY DRIFT (round 11 NEW class motif RECURRENCE — 2nd cumulative)

The systematic difference in delimiter convention extends across ALL writer rerun TABLE_HEADER + TABLE_ROW atoms (writer rows 3/4/7 are pure canonical-form-only divergence with no value content drift; rows 1/2/5/6/8 compound canonical-form drift atop value hallucinations):

- **Executor (baseline) — N5 standard markdown table form**: `| cell | cell | cell |` with leading + trailing pipes and single space around each pipe. Empty cells encoded as `| |` preserving N5 pipe-count consistency.
- **Writer (rerun) — minimal-delimiter form**: `cell | cell | cell` with NO leading + trailing pipes. Empty cells variably handled (sometimes `| |` preserved, sometimes pipes elided).

**Round 11 batch 45 p.445 motif RECURRENCE on different content type confirmed**: round 11 surfaced this motif on `appendix narrative + N18.d VERBATIM-CRITICAL identifier` simple 2-column contributor table; round 12 batch 48 surfaces the SAME motif on `mixed_structural_transition` chapter-start 12-column spec table content type. **2nd cumulative recurrence on a structurally distinct content type validates Hypothesis B (canonical-form drift INDEPENDENT of content type) per round 11 G-MS-NEW-11-1**.

### §3.3 NEW round 12 motif: atom_type ENUM FABRICATION (3rd distinct writer-direction motif class — schema-violating)

Writer emitted 2 atoms with atom_type=`SECTION_HEADING`, NOT in atom_schema.v1.2 9-enum (HEADING / SENTENCE / LIST_ITEM / TABLE_HEADER / TABLE_ROW / CODE_LITERAL / CROSS_REF / FIGURE / NOTE):

| atom_id | atom_type (FABRICATED) | Should be | verbatim |
|---|---|---|---|
| sv20_p0015_a001 | `SECTION_HEADING` ❌ | `HEADING` | `3.1.2 The Events Observation Class` |
| sv20_p0015_a002 | `SECTION_HEADING` ❌ | `HEADING` | `Events—Topic and Qualifier Variables—One Record per Event` |

**Schema sweep CATCHES**: post-rerun schema validation surfaces 2 `invalid atom_type=SECTION_HEADING` errors on writer rerun artifact. Schema sweep on production 48a + 48b atoms = 0 errors (executor adheres to 9-enum).

**Distinctness from prior motif classes**:
- VALUE HALLUCINATION (rounds 5-10 motif type) operates on `verbatim` field content (digit deletion / column fabrication / value invention)
- Canonical-form delimiter granularity (round 11 NEW class) operates on TABLE_ROW pipe-encoding convention
- atom_type ENUM FABRICATION (round 12 NEW class) operates on `atom_type` schema field — fabricates an enum value not in the frozen 9-enum

**Hypothesis on atom_type ENUM FABRICATION mechanism**: writer-family is pulling from training-data templates of common heading-class enum names (e.g. CommonMark `SECTION_HEADING`, HTML `h1`/`section` semantics, generic markdown / docs schema vocabulary). The 9-enum is a project-frozen v1.2 atom schema specifically tuned for SDTM atomization; training-data templates for generic document atomization use different vocabularies. This is structurally identical to the round 5-10 TABLE_HEADER column-name fabrication motif (writer pulls from training-data templates of generic CRF tables instead of reading PDF verbatim) — **same training-data-template motif extends from `verbatim` field cell-value fabrication to `atom_type` enum-field fabrication**.

### §3.4 Hash intersection breakdown

The 2 atoms in verbatim-hash intersection = the 2 HEADING atoms with byte-exact `verbatim` text match:
- `3.1.2 The Events Observation Class` (executor sv20_p0015_a005 HEADING ↔ writer sv20_p0015_a001 SECTION_HEADING)
- `Events—Topic and Qualifier Variables—One Record per Event` (executor sv20_p0015_a006 HEADING ↔ writer sv20_p0015_a002 SECTION_HEADING)

Both pairs share verbatim hash but diverge on atom_type (HEADING vs fabricated SECTION_HEADING). If atom_type were also part of the hash composition (it is NOT per current drift cal hash methodology — verbatim-only), the intersection would drop to 0.

## §4 12TH CUMULATIVE DRIFT CAL + Cumulative writer-direction recurrence tracking

| Round | Batch | Drift cal page | Content type | Recurrence # | Motif |
|---|---|---|---|---|---|
| 5 | 28 | p.270 | examples_narrative_spec_table | 1st | TABLE_ROW VALUE HALLUCINATION (USUBJID/PCREFID/PCTESTCD INVENTED IDs) (O-P1-85) |
| 6 | 31 | p.293 | examples_narrative_spec_table | 2nd | TABLE_ROW VALUE HALLUCINATION (O-P1-103) |
| 7 | 34 | p.325 | examples_narrative_spec_table | 3rd | TABLE_ROW VALUE HALLUCINATION (O-P1-109) |
| 8 | 36 | p.357 | examples_narrative_spec_table | 4th | TABLE_ROW VALUE HALLUCINATION → halt → Option H bulk repair → triggered v1.5 N16 codification |
| 9 | 39 | p.382 | mixed_structural_transition | 5th | URL .org→.ch + word `clinical` deletion + TABLE_ROW Study cell ~26% TRUNCATION+REORDER (O-P1-134) → triggered v1.6 N18 EXTENDED scope codification |
| 10 | 42 | p.412 | examples_narrative_spec_table | 6th | TABLE_HEADER FABRICATION (NEW MODE) + TABLE_ROW VALUE FABRICATION (O-P1-145) → triggered v1.7 N21 COMPLETE BAN codification |
| 11 | 45 | p.445 | appendix narrative + N18.d VERBATIM-CRITICAL identifier | NOT counted | CANONICAL-FORM DELIMITER GRANULARITY divergence (NEW class round 11) — content-preserving NOT VALUE HALLUCINATION; cumulative count REMAINED at 6 per D-MS-NEW-11-1 |
| **12** | **48** | **sv20 p.15** | **mixed_structural_transition chapter-start + 12-col spec table** | **🔴 7TH CUMULATIVE WRITER-DIRECTION VALUE HALLUCINATION RECURRENCE (artifact direction)** | **MULTI-MOTIF**: VALUE HALLUCINATION (rounds 5-10 type — C-code digit fabrication on rows 1/2 + Definition paraphrase on rows 5/6/8 + Variable(s) Qualified mangling on row 6 + Examples cell cross-table contamination on rows 1/2 — 5 of 8 spec-table rows affected) **+** CANONICAL-FORM DELIMITER GRANULARITY DRIFT (round 11 NEW class motif **2nd cumulative recurrence on different content type confirming H_B**) **+** NEW round 12 motif: **atom_type ENUM FABRICATION** (`SECTION_HEADING` not in 9-enum on 2 of 11 atoms = **3rd distinct writer-direction motif class**) |

**7th cumulative writer-direction VALUE HALLUCINATION recurrence at writer-direction in artifact direction**: cumulative count GOES TO 7 (was 6 entering round 12 per round 11 D-MS-NEW-11-1; round 11 NEW class did not count). Round 12 recurrence is on `mixed_structural_transition + 12-col spec table` content type that v1.6 N18 EXTENDED scope sub-rules a/d/e ALL EXPLICITLY BANNED (writer NOT eligible under v1.6) — round 12 confirms writer-direction VALUE HALLUCINATION motif PERSISTS on banned content types in artifact direction even under v1.7 N21 production-side COMPLETE BAN. **Validates v1.7 N21 was correct escalation level** — under partial bans (N16 + N18) writer would have been used for production on this content type prior to N16/N18 codification, and the value hallucinations would have shipped to root atoms; under N21 COMPLETE BAN, executor canonicalization is enforced for production (production 150 atoms 0 hallucinations per Rule A 100.0% PASS slot #61).

**Direction**: REVERSED — baseline (executor) is PDF-correct + canonical N5 form + 9-enum schema-conformant; rerun (writer) compounds VALUE HALLUCINATION + canonical-form drift + atom_type ENUM FABRICATION. **DIRECTION REVERSED 15th cumulative occurrence (writer-side divergence) + 1st instance of compounded triple-motif divergence**.
**Value-add**: drift cal caught what Rule A 10-atom sample missed (Rule A sample drew from 48b executor baseline = PDF-correct; would not detect rerun multi-motif divergence). **16th value-add precedent.**

## §5 v1.7 N21 baseline 2nd cumulative live-fire halt analysis (per kickoff §0.4 + §5.2-5.3 + §6)

Per kickoff §5.3 expected outcomes under v1.7 N21 baseline:

> **Most likely (per round 11 NEW class precedent)**: production 48a + 48b executor-clean per v1.7 N21 prevention layer; writer rerun exhibits some divergence — outcome classification per H_A vs H_B hypothesis testing per round 11 G-MS-NEW-11-1; halt NOT triggered for writer-direction recurrence regardless of motif type (artifact NOT merged); **DOCUMENT in `drift_cal_batch_48_sv20_p015_report.md`** the divergence motif classification (VALUE HALLUCINATION vs canonical-form drift vs NEW class) + H_A vs H_B hypothesis discrimination outcome
> **Less likely but possible**: executor-direction motif surfaces in 48a or 48b production atoms = NEW class of failure not seen rounds 5-11; halt-on-violation per Hook 19 + ESCALATE to v1.8 trigger candidate (executor-family hardening — out-of-scope for v1.7 N21 by design)
> **NEW round 12 possibility**: sv20 PDF source introduces NEW divergence motif unique to model-level abstract content; codify in v1.8 candidate stack

**Actual outcome**: All three scenarios PARTIALLY realized simultaneously in compound:
- Production 48a + 48b executor-clean as expected (Most-likely scenario realized for production-side)
- Writer rerun divergence is MULTI-MOTIF: (a) VALUE HALLUCINATION (rounds 5-10 type) AT writer-direction in artifact direction (Most-likely scenario expanded to 7th cumulative recurrence); (b) CANONICAL-FORM DELIMITER GRANULARITY DRIFT (round 11 NEW class motif RECURRENCE on different content type — discriminator for H_B); (c) NEW round 12 motif: atom_type ENUM FABRICATION as 3rd distinct motif class (NEW round 12 possibility realized)
- Executor-direction motif NOT surfacing (less-likely scenario NOT realized — production atoms PDF-clean)

**Halt analysis**:
- Drift cal both-thresholds halt (legacy v1.6 carry-forward N1): NUMERIC values fail thresholds (strict 13.3% AND verbatim Jaccard 8.3% both <80%). **Disposition**: numeric trip is REAL (compound multi-motif drift) — but halt clause was always evaluated against motif-type classification per kickoff §5.2.
- N3 NEW8.d "7th cumulative recurrence" halt clause: **TRIGGERED** as 7th cumulative writer-direction VALUE HALLUCINATION recurrence at writer-direction in **artifact direction only**. Per kickoff §5.2 + v1.7 §N21 last paragraph: under N21 design, "7th cumulative writer-direction recurrence is impossible by construction" was specifically scoped to PRODUCTION direction (writer NOT used in production). Per §派发 `drift_cal_alternation_artifact` exception, writer IS still used in artifact direction for direction-attribution validation. Round 12 batch 48 = first instance where writer-direction VALUE HALLUCINATION motif RECURS in artifact direction at the 7th cumulative position. **Disposition**: artifact-direction recurrence is BY DESIGN under §派发 exception; production-side prevention layer EFFECTIVE; halt NOT triggered.
- v1.7 N21 NEW halt clause (executor-direction motif in baseline): NOT triggered (production 48a + 48b executor-clean per Rule A 100.0% PASS + schema sweep 0 errors).
- **Decision**: NO HALT. Continue to STEP 6 evidence write + STEP 7 DONE echo. Document exhaustively in this report + escalate v1.8 candidate stack.

**Important nuance**: production atoms 48a + 48b (150 atoms total, executor-only, PDF-clean per schema sweep + Rule A 100.0% slot #61 codex:codex-rescue codex-family 4th burn) are NOT affected. Drift cal rerun atoms (11 atoms) NOT merged to root regardless. The numeric threshold trip is REAL compound multi-motif drift but contained to artifact direction.

## §6 v1.7 N21 baseline 2nd cumulative live-fire VALIDATION

Round 12 batch 48 drift cal = **2nd cumulative live-fire of v1.7 N21 baseline drift cal validation** (1st INAUGURAL was round 11 batch 45):

1. **N21 ban scope validation (production-side)**: PROVEN EFFECTIVE 2nd cumulative — production 48a (92 atoms) + 48b (58 atoms) = 150 atoms total, executor-only, schema-clean (0 errors), Rule A 100.0% PASS slot #61 codex:codex-rescue AUDIT-mode pivot 42nd cumulative. v1.7 N21 production-side prevention layer working as designed at 2 cumulative live-fires.
2. **N21 ban scope validation (artifact-side via EXECUTOR-VARIANT alternation)**: PROVEN EFFECTIVE WITH EXTENSIVE NUANCE — writer rerun exhibited THREE distinct motif classes simultaneously (VALUE HALLUCINATION + canonical-form drift + NEW atom_type ENUM FABRICATION). All three motifs indicate writer-direction divergence; production atoms unaffected (artifact NOT merged). **Validates v1.7 N21 COMPLETE BAN was correct escalation level at 2 cumulative live-fires** — under partial bans (N16 v1.5 + N18 v1.6) writer would have been used for production on this content type and value hallucinations + canonical-form drift would have shipped to root atoms; under N21 COMPLETE BAN, executor canonicalization is enforced for production.
3. **N14 STRONGLY VALIDATED status sustained 6th live-fire**: Round 7 batch 33 1st + round 8 batch 36 2nd + round 9 batch 39 3rd + round 10 batch 42 4th + round 11 batch 45 5th + **round 12 batch 48 6th** = STRONGLY VALIDATED status sustained at 6 cumulative live-fires.
4. **EXECUTOR-VARIANT alternation pattern under v1.7 N21**: continues to deliver direction-attribution capability at multi-motif granularity (3 distinct writer-direction motif classes characterized in single drift cal). Pattern remains production-ready.

## §7 H_A vs H_B hypothesis discrimination outcome (per round 11 G-MS-NEW-11-1)

Round 11 retro G-MS-NEW-11-1 surfaced two competing hypotheses for writer-direction divergence motif character:

- **H_A (content-type-conditional fabrication)**: writer-family fabricates VALUE HALLUCINATION on `examples_narrative_spec_table` + `mixed_structural_transition` (rounds 5-10 motif) but stays content-correct on `appendix narrative + N18.d VERBATIM-CRITICAL identifier` simple 2-column tables (round 11 batch 45 NEW class). Round 12 batch 48 sv20 p.15 = `mixed_structural_transition + 12-col spec table` content profile = H_A predicts VALUE HALLUCINATION fabrication.
- **H_B (canonical-form drift independent of fabrication)**: writer-family table-row canonicalization drifts toward minimal-delimiter convention regardless of content type; round 5-10 fabrication motif may have masked this delimiter drift previously. Round 12 batch 48 sv20 p.15 prediction: same canonical-form delimiter drift if H_B true regardless of content type.

**Round 12 batch 48 outcome — BOTH HYPOTHESES SIMULTANEOUSLY CONFIRMED**:

- ✅ **H_A confirmed**: VALUE HALLUCINATION fabrication observed on `mixed_structural_transition + 12-col spec table` content type (rows 1/2/5/6/8 of writer rerun spec table). The fabrication motif persists exactly as round 5-10 cumulative pattern (digit deletion in C-codes / Definition paraphrase / Variable(s) Qualified cell mangling / Examples cell cross-table contamination).
- ✅ **H_B confirmed**: canonical-form delimiter granularity drift observed on this 12-col spec table content type (ALL writer rerun TABLE_HEADER + TABLE_ROW atoms drop leading + trailing pipes vs executor canonical N5 form). The motif is the SAME canonical-form drift seen on round 11 batch 45 contributor table (different content type) → drift IS independent of content type.
- 🆕 **NEW Round 12 motif (3rd hypothesis space)**: **atom_type ENUM FABRICATION** — writer fabricates schema-field enum values not in frozen 9-enum (`SECTION_HEADING` for 2 HEADING atoms). This is a SCHEMA-FIELD-LEVEL motif distinct from both VERBATIM-content-level (H_A) and TABLE-row-canonical-form-level (H_B). Generalizes the training-data-template fabrication motif from `verbatim` field cell-value fabrication to `atom_type` enum-field fabrication.

**Conclusion**: H_A and H_B are NOT mutually exclusive — they describe distinct independent writer-direction divergence axes that CO-OCCUR in same drift cal output. Round 12 batch 48 reveals writer-direction motifs are MULTI-AXIS:
- Axis 1 (VERBATIM content fabrication / H_A): triggers selectively on `examples_narrative_spec_table` + `mixed_structural_transition` content types; rounds 5-10 + round 12 = 7 cumulative confirmations
- Axis 2 (canonical-form delimiter granularity / H_B): triggers independent of content type; round 11 + round 12 = 2 cumulative confirmations
- Axis 3 (schema-field enum fabrication / NEW round 12): triggers selectively on HEADING atoms; round 12 = 1st confirmation; v1.8 candidate to monitor

**v1.8 codification candidate**: codify multi-axis writer-direction motif taxonomy formally; each axis has independent cumulative count + trigger-condition + escalation threshold. Round 12 batch 48 = 1st live-fire of multi-axis motif co-occurrence hypothesis.

## §8 Findings Filed

- **No new O-P1-NN finding raised** (no Rule A blockers; no halt triggered; production atoms clean per Rule A 100.0% PASS slot #61 codex:codex-rescue + schema sweep 0 errors + 0 sv20 header/footer leak).
- **OBS-A LOW** (informational): 7th cumulative writer-direction VALUE HALLUCINATION recurrence at writer-direction in artifact-only direction. Under v1.7 N21 design (writer NOT used in production), recurrence in artifact-only is BY DESIGN per §派发 exception. Documents continued effectiveness of v1.7 N21 COMPLETE BAN scope (production prevention layer).
- **OBS-B INFORMATIONAL** (NEW round 12 motif candidate for v1.8 candidate stack): **atom_type ENUM FABRICATION** as 3rd distinct writer-direction motif class. `SECTION_HEADING` is NOT in atom_schema.v1.2 9-enum. Schema sweep on writer rerun artifact catches 2 invalid-enum errors; production atoms unaffected. Generalizes training-data-template fabrication motif from VERBATIM cell-value fabrication to atom_type enum-field fabrication. v1.8 candidate stack: codify NEW Hook 16.X writer-side schema field-level template-fabrication detection (analogous to Hook 19 PDF-cross-verify but for schema field values rather than verbatim text) — deferred to v1.8 cut session if executor-family ever exhibits motif.
- **OBS-C INFORMATIONAL** (multi-axis writer-direction motif taxonomy): H_A + H_B BOTH confirmed simultaneously in round 12 batch 48 indicates writer-direction motifs are MULTI-AXIS not single-axis. v1.8 candidate to formally codify motif-axis taxonomy.

(O-P1-169..172 reserved unused — no new findings warranting an O-P1-NN finding ID.)

## §9 Disposition for Batch 48 Closure

- **48a (92 atoms sv20 p.10-14)**: KEEP. Executor-emitted, schema sweep PASS 0 errors, Rule A audit included in slot #61 sample (atoms p.10-14 sampled), Hook 19 N20 PDF-cross-verify URL/DOI/identifier exact (no URLs in this sub-batch; CDISC-internal CROSS_REF "Model Concepts and Terms – Variables" + "Implementation Advice for this Model" + "Special-purpose Domains" verified vs PDF visible).
- **48b (58 atoms sv20 p.15-19)**: KEEP. Executor-emitted, schema sweep PASS 0 errors, Rule A audit included in slot #61 sample (atoms p.15-19 sampled, 5 atoms 1/page).
- **drift_cal_sv20_p015_writer_rerun.jsonl (11 atoms)**: PRESERVE as drift cal artifact (NOT merged to root pdf_atoms.jsonl); reference for v1.8 candidate stack multi-axis motif taxonomy hypothesis testing + atom_type ENUM FABRICATION 1st evidence repository.
- **Rule B backup**: not needed — 48a/48b atoms not modified post-drift-cal.
- **OBS-A/B/C**: defer to v1.8 candidate stack per §11.

## §10 N14 STRONGLY VALIDATED Status Sustained (6th Live-Fire)

Round 7 batch 33 1st + round 8 batch 36 2nd + round 9 batch 39 3rd + round 10 batch 42 4th + round 11 batch 45 5th + **round 12 batch 48 6th** = STRONGLY VALIDATED status sustained at 6 cumulative live-fires of N14 strict alternation methodology. v1.6 NEW EXECUTOR-VARIANT alternation pattern (kickoff §3.3) under v1.7 N21 baseline 2nd cumulative live-fire successfully attributing direction (REVERSED — writer-side multi-motif divergence via baseline-PDF cross-check + rerun-PDF cross-check) at multi-axis granularity. N14 production-ready alternation methodology validated for cumulative 6 live-fires across content-type variation + cross-PDF source variation (round 12 = 1st in sv20 PDF source).

## §11 Rule 合规

- **Rule A**: 10-atom audit slot #61 codex:codex-rescue (codex-family 4th burn extension; AUDIT pivot 42nd cumulative) PASS 100.0% (separate gate, complementary to drift cal); 4-dimension verdict 10/10 PASS / 0 PARTIAL / 0 FAIL; threshold ≥80% met ✅
- **Rule B**: not invoked (no Option H needed; 48a/48b baselines PDF-correct; rerun NOT merged); drift_cal_sv20_p015_writer_rerun.jsonl preserved as artifact + multi-motif evidence per §派发 `drift_cal_alternation_artifact` exception
- **Rule C**: drift cal report (this file) + Rule A summary (rule_a_batch_48_summary.md) + verdicts (rule_a_batch_48_verdicts.jsonl) + sample (rule_a_batch_48_sample.jsonl) + PDF ground truth (rule_a_batch_48_pdf_groundtruth.txt) + P1_batch_48_report.md (STEP 7) + reconciler-stage round 12 retro pending
- **Rule D**: writer rerun (`oh-my-claudecode:writer`) ≠ executor baseline (`oh-my-claudecode:executor`) per N14 alternation; Rule A reviewer slot #61 (`codex:codex-rescue`) is external runtime / different model — strongest Rule D isolation profile (codex-family 4-burn intra-family depth scale VALIDATED post round 12 batch 48 cumulative #48+#52+#56+#61); main session attribution INDEPENDENT of writer self-claim (writer rerun self-claimed "All v1.7 self-validate hooks passed" in WRITER_DRIFT_CAL_SV20_P015_DONE echo despite the actual schema-validation errors on atom_type field — round 9 batch 39 + round 10 batch 42 + round 11 batch 45 + round 12 batch 48 = **4 cumulative confirmations** that writer self-Validate hooks 17/20 are detection-not-prevention; writer self-claim trust profile UNRELIABLE confirmed at 4 cumulative live-fires; v1.7 N23 codified "RENDERED MOOT by N21 since executor doesn't exhibit motif" — round 12 batch 48 EXPANDS the "writer self-claim untrustworthy" finding to atom_type ENUM FABRICATION axis, but consequence (use executor for production) remains correct).
- **Rule E**: OBS-A LOW + OBS-B INFORMATIONAL (atom_type ENUM FABRICATION NEW class) + OBS-C INFORMATIONAL (multi-axis motif taxonomy) filed for v1.8 candidate stack.

## §12 v1.8 Candidate Stack (post round 12 batch 48 — significantly expanded)

Non-blocking observations + candidate codifications queued to v1.8 candidate stack:

1. **OBS-A (LOW)**: 7th cumulative writer-direction VALUE HALLUCINATION recurrence at writer-direction in artifact-only direction. Confirms v1.7 N21 production-side prevention layer is correct escalation level; writer-direction motif persists in artifact direction even when banned for production. Cumulative writer-direction VALUE HALLUCINATION count GOES TO 7. v1.8 codification candidate: refresh recurrence-tracking table to include round 12 entry; sustain v1.7 N21 ban scope (no escalation needed per N21 design that artifact-direction recurrence is by-design under §派发 exception).
2. **OBS-B (INFORMATIONAL, NEW class)**: **atom_type ENUM FABRICATION** as 3rd distinct writer-direction motif class. Schema sweep on writer rerun artifact catches 2 invalid-enum errors (`SECTION_HEADING` not in 9-enum). Generalizes training-data-template fabrication motif from VERBATIM cell-value fabrication to atom_type enum-field fabrication. **v1.8 codification candidate**: explicitly track schema-field-level enum-fabrication motif as Axis 3 of multi-axis writer-direction motif taxonomy; if executor-family ever exhibits this motif → NEW v1.8 trigger candidate (executor-family hardening).
3. **OBS-C (INFORMATIONAL, multi-axis)**: H_A + H_B BOTH simultaneously confirmed in round 12 batch 48 (with NEW round 12 Axis 3 surfaced) indicates writer-direction motifs are MULTI-AXIS not single-axis. v1.8 codification candidate: formal multi-axis motif taxonomy with independent cumulative counts + trigger conditions + escalation thresholds per axis (Axis 1 VERBATIM cell-value fabrication / Axis 2 canonical-form delimiter granularity / Axis 3 schema-field enum fabrication / future axes if surfaced).
4. **OBS-D (INFORMATIONAL, writer self-claim untrustworthy 4th cumulative)**: writer rerun self-Validate hooks 17/20 self-claimed "all hooks PASS" despite schema-violating atom_type=SECTION_HEADING + multi-motif divergence; round 9+10+11+12 = **4 cumulative confirmations** writer self-claim trust profile UNRELIABLE. v1.8 codification candidate: extend Hook 19 N=10 PDF-cross-verify scope to schema-field-level cross-validation (currently only cell-value-level); v1.8 may codify Hook X for schema-conformance pre-DONE-emit halt-on-violation for writer-family if writer ever permitted in any future scope.
5. **Round 12+ executor-direction motif watch (v1.7 §N21 last paragraph sustained)**: round 12 batch 48 confirms NO executor-direction motif on `mixed_structural_transition + 12-col spec table` content type (Rule A 100.0% + schema 0 errors). Continue watch round 13+ on different content types (sv20 §3.1.3 Findings Observation Class anticipated batch 49 / sv20 §4 Special-purpose Domains anticipated round 13).
6. **CROSS-PDF source variation (round 12 NEW)**: round 12 batch 48 = 1st cumulative drift cal in sv20 PDF source (vs all 11 prior in ig34). Multi-axis writer-direction motifs surfaced in both PDF sources — H_B canonical-form drift confirmed independent of PDF source AND content type.
7. **Carry-forward v1.7 cut F2 LOW** (round 11 carry-forward): N22/AD wording placement refinement.
8. **Carry-forward N11 scope clarification for Appendix-style L2 containers** (round 11 G-MS-NEW-11-3 + O-P1-161 NON_BLOCKING_OBS_FORM-1).
9. **Carry-forward kickoff §3 TOC predictions auto-derive from PDF script** (G-MS-NEW-10-3 motif STRONGLY VALIDATED post 3 cumulative live-fires).

---

**Drift Cal Verdict**: 🔴 **CATASTROPHIC FAIL BOTH NUMERIC THRESHOLDS + MULTI-MOTIF SIMULTANEOUS** (strict 13.3% AND verbatim Jaccard 8.3% both <80%; **3 distinct writer-direction motif classes co-occurring in single drift cal**: VALUE HALLUCINATION 7th cumulative + canonical-form drift 2nd cumulative + atom_type ENUM FABRICATION NEW round 12 class) — **production atoms 48a + 48b executor-clean preserved**. v1.7 N21 PRODUCTION-SIDE EFFECTIVE 2nd cumulative live-fire. Multi-axis writer-direction motif taxonomy surfaced as v1.8 candidate. NO HALT (artifact-direction recurrence by-design under v1.7 N21 §派发 exception; production direction clean). Continue to STEP 6/7 closure.
