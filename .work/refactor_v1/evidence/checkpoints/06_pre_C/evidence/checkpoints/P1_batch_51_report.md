# P1 Batch 51 Report — Round 13 Session C — sv20 p.40-49

- **Date**: 2026-04-30 (Round 13, multi-session, session C, batch 51)
- **Round**: 13 = 3rd round running v1.7 baseline post round 12 2nd cumulative EFFECTIVE 2026-04-30 commit `ba1ae12`
- **v1.7 vs v1.8 baseline note**: round 13 dispatched with **v1.7 baseline** per `_progress.json` recovery_hint explicit decision rule: "round 13 dispatched BEFORE v1.8 cut commit completes runs v1.7 baseline; round 14+ dispatched AFTER v1.8 cut commit runs v1.8 baseline (per round 11/12 mid-prompt-swap precedent: kickoff §10 NEVER DO list — no mid-round prompt swap)". v1.8 prompts (active 2026-04-30 with 5 NEW patches N24-N28) are deliberately NOT used in this round 13 batch dispatch. Round 14+ batches will adopt v1.8.
- **Page range**: sv20 p.40-49 (10 pages), divided 51a (p.40-44) + 51b (p.45-49) per kickoff §3.1/§3.2 sub-batch protocol.
- **Content type**: HEAVY `mixed_structural_transition` (1 L2 NEW §3.2 + 4 L3 NEW §3.2.1/§3.2.2/§3.2.3/§3.2.3.x children + 4 L4 NEW §3.2.3.1/2/3/4 transitions across 10 pages — DENSE) + sv20 model-level abstract narrative + 12-col Demographics + Comments + various §3.2.3.x spec tables.
- **Atom production**: 51a 65 atoms + 51b 85 atoms = **150 atoms total**. Single-dispatch pattern N6 STRONGLY VALIDATED (4th cumulative live-fire post round 12 batch 49 3rd).
- **Drift cal target**: sv20 p.45 (13th cumulative drift cal in P1; 7th N14 strict-alternation live-fire; 3rd v1.7 N21 baseline cumulative; 2nd in sv20 PDF source).

## §1 Sub-batch Distribution

| Sub-batch | Page range | Atoms | Sections covered | Active heading terminal |
|---|---|---|---|---|
| 51a | sv20 p.40-44 | 65 | §3.2 L2 NEW + §3.2.1 Demographics L3 NEW + §3.2.2 Comments L3 NEW | §3.2.2 [Comments] |
| 51b | sv20 p.45-49 | 85 | §3.2.3 Subject Summary Domains L3 NEW + §3.2.3.1/2/3/4 L4 NEW chain | §3.2.3.4 [Subject Disease Milestones] |

Per-page atom counts (executor self-claim): p.40=18 / p.41=7 / p.42=13 / p.43=11 / p.44=16 / p.45=16 / p.46=19 / p.47=17 / p.48=18 / p.49=15.

## §2 Executor Self-Validation Summary

- **Hook 19 PDF-cross-verify N=10**: 10/10 spot-check sample atoms PASS per executor self-claim
- **Hook 15 pipe-count consistency (N5)**: 11 pipes cross-row consistent in baseline TABLE_ROWs (minimal-delimiter form within batch)
- **Hook 18 SENTENCE-paragraph-concat WARN**: 0 multi-sentence concats detected
- **9-enum schema sweep**: 0 invalid atom_types (all atoms in HEADING/SENTENCE/TABLE_HEADER/TABLE_ROW per executor)
- **Header/footer leak**: 0 sv20 furniture atoms emitted
- **atom_id collisions**: 0
- **Cross-batch HEADING sibling continuity**: §3.2 children sib=1 (Demographics) → sib=2 (Comments) → sib=3 (Subject Summary Domains) consistent; §3.2.3 children sib=1..4 consistent
- **Hook 20 parent_section granularity refinement**: applied per N11 chapter-short-bracket form on all 10 unique parent sections

**Executor DONE echo**: `EXECUTOR_BATCH_51_DONE atoms_51a=65 atoms_51b=85 total=150 failures=0 repair_cycles=0 hook18_warn_count=0 hook19_pdf_cross_verify=10/10 sv20_header_footer_leaks=0 schema_errors=0 active_heading_terminal=§3.2.3.4 [Subject Disease Milestones]`

**Note**: executor self-validation = detection-not-prevention; round 9-12 cumulative = 4 confirmations writer/executor self-claim trust profile UNRELIABLE. Codex Rule A independent verification surfaced 2 motifs the executor self-validation MISSED (N26 + heading_text), demonstrating Rule A independent audit value-add.

## §3 Drift Cal Outcome (sv20 p.45, 13th cumulative)

- **Method**: v1.6 NEW EXECUTOR-VARIANT alternation pattern under v1.7 N21 §派发 `drift_cal_alternation_artifact` exception. Baseline = executor (51b p.45 subset, 16 atoms). Rerun = writer (drift_cal_sv20_p045_writer_rerun.jsonl, 16 atoms).
- **Numeric metrics**: strict count overlap 50.0% (8/16) FAIL <80%; verbatim hash Jaccard 33.3% (8/24) FAIL <80%.
- **Multi-axis classification (per v1.8 N24 codification reference)**:
  - Axis 1 (VERBATIM cell-value fab): NONE detected (writer rerun preserves byte-exact cell content)
  - Axis 2 (canonical-form delimiter granularity): YES, **REVERSED DIRECTION** from round 12 batch 48 (this round: executor=minimal, writer=full pipes; round 12: executor=full, writer=minimal). Cross-family Axis 2 cumulative: 2 writer + 1 executor = 3.
  - Axis 3 (schema-field enum fab): NONE detected
  - **NEW Axis 4** (parent_section casing/suffix variation): YES, bidirectional (1st cumulative)
  - **N26** (page-boundary off-by-one): YES at executor-direction, **2 atoms in batch 51** (sv20_p0043_a011 + sv20_p0045_a001) — ≥2/batch ≥ N26 v1.8 promotion threshold
  - TABLE_HEADER continuation-page emission divergence (NEW class)
- **Verdict**: 🟡 **GRANULARITY_DIVERGENCE_MULTI_AXIS_BIDIRECTIONAL** — content-preserving multi-axis drift; NO HALT per kickoff §5.2 v1.7 N21 strict halt clause (N26 + Axis 2 are NOT Hook 19 value fab nor schema sweep failure; heading_text schema is non-violation per schema reality).
- **Counter-intuitive direction-attribution finding**: writer rerun page-boundary handling SUPERIOR to executor on this batch (writer correctly started p.45 atoms at row 9; executor mis-attributed row 8 IDVAR to p.45). FIRST observed instance in P1 cumulative where writer-direction handling outperforms executor-direction on a specific axis. NUANCE in v1.7 N21 "executor-only for production" policy.

Full drift cal analysis: `evidence/checkpoints/drift_cal_batch_51_sv20_p045_report.md` (12 sections, 230+ lines).

## §4 Rule A Audit Slot #64 codex:codex-rescue (5th burn extension AUDIT pivot 45th cumulative)

- **Sample**: 10 atoms, stratified 1/page sv20 p.40-49, seed=20260602
- **Verdicts**: verbatim 9/10 PASS (1 FAIL halt-grade) / atom_type 10/10 PASS / parent_section 10/10 PASS / schema 7/10 PASS (3 FAIL — see disposition)
- **Weighted PASS%**: **90.0%** (36/40) ≥ 80% threshold
- **Halt-grade verbatim FAIL**: 1 atom (sv20_p0043_a011) — N26 page-boundary off-by-one motif at executor-direction; codex's strict rubric flagged page-local non-byte-exact as verbatim FAIL
- **Schema FAIL on 3 sample atoms** (extrapolated 14/150 batch-wide via codex scan): codex strict rubric flagged `heading_text` field as undeclared. **Main-session resolution**: schema does NOT set `additionalProperties: false`, so heading_text IS allowed per JSON Schema 2020-12 default semantics. Codex's interpretation was strict-prompt-rubric false positive. **Production atoms schema-valid per actual schema spec.**
- **Codex DONE echo**: `RULE_A_BATCH_51_DONE sample_n=10 weighted_pass_pct=90.0% verbatim_pass=9/10 atom_type_pass=10/10 parent_section_pass=10/10 schema_pass=7/10 halt_grade_fails=1 findings=O-P1-181,O-P1-182`
- **Codex's HALT verdict**: stricter than kickoff §5.2 v1.7 N21 halt clause; main session interprets per kickoff (N26 = page-attribution NOT value fab; heading_text = non-violation per schema reality) → **NO HALT** at main session disposition.

Codex Rule A files: `rule_a_batch_51_sample.jsonl` + `rule_a_batch_51_verdicts.jsonl` + `rule_a_batch_51_summary.md`.

## §5 Findings Filed (4 IDs O-P1-181..184; 4 used + 0 reserved unused)

- **O-P1-181 MEDIUM** (RECONCILED drift cal + Rule A unified): N26 page-boundary off-by-one motif at executor-direction, **≥2/batch** (sv20_p0043_a011 row 37 DMDTC + sv20_p0045_a001 row 8 IDVAR). 2nd cumulative N26 motif at executor-direction (round 12 batch 49 1st cumulative). Exceeds N26 v1.8 ≤1/batch WARN threshold = halt-on-violation under strict v1.8 codification. Recommend Option H page-label correction at reconciler stage for both atoms. v1.9 candidate stack: promote N26 from WARN-mode to halt-on-violation (≥2/batch empirical evidence threshold).
- **O-P1-182 LOW** (codex Rule A, MAIN-SESSION RECLASSIFIED non-violation): codex flagged 14/150 batch atoms with `heading_text` extra field as schema FAIL. Main session reclassification: schema does NOT close additional properties (additionalProperties default = allow). `heading_text` is permitted per actual schema spec. Codex strict-prompt-rubric false positive. Recommend v1.9 schema clarification: explicitly declare `heading_text` as optional HEADING property in atom_schema OR mark schema as `additionalProperties: false` for strict closure (with corresponding writer protocol update).
- **O-P1-183 LOW** (drift cal): NEW Axis 4 parent_section casing/suffix variation (round 13 batch 51 1st cumulative cross-direction). Title-case vs UPPERCASE casing + domain-code suffix presence/absence. Recommend v1.9 codification: extend N27 to L2/L3/L4 parent_section convention.
- **O-P1-184 LOW** (drift cal): TABLE_HEADER continuation-page emission convention divergence (round 13 batch 51 1st cumulative). Recommend v1.9 codification: design single canonical form for multi-page TABLE_HEADER convention.

(All 4 reserved IDs O-P1-181..184 used.)

## §6 Halt Analysis

Per kickoff §5.2 v1.7 N21 strict halt clause: HALT only if executor-direction motif surfaces in baseline via Hook 19 PDF-cross-verify (value fab) OR schema sweep failure.

- N26 motif (≥2/batch): NOT Hook 19 (page-attribution, not value fab) AND schema sweep on production atoms = 0 errors per executor self-claim → kickoff §5.2 HALT NOT triggered.
- Codex strict rubric `heading_text`: NOT a real schema sweep failure (schema allows additional properties per default).
- Drift cal numeric trip (50.0%/33.3% both <80%): legacy v1.6 carry-forward halt clause; superseded by multi-axis taxonomy classification under v1.7 N21 baseline (round 11+12 precedent: numeric trip with multi-axis classification → no halt for content-preserving drift).
- Codex Rule A weighted PASS 90.0% ≥ 80% threshold: PASS.

**Main session HALT disposition**: NO HALT. Continue to STEP 7 DONE echo with comprehensive findings + escalation to v1.9 candidate stack.

## §7 v1.9 Candidate Stack Update (post round 13 batch 51)

1. **N26 promotion to halt-on-violation** (per ≥2/batch empirical evidence round 13 batch 51): codify N26 as halt-grade when batch contains ≥2 page-boundary off-by-one atoms.
2. **Per-family cumulative count tracking** (Axis 2 BIDIRECTIONAL evidence round 13 batch 51): refine v1.8 N24 multi-axis taxonomy to track writer-direction AND executor-direction cumulative counts independently.
3. **NEW Axis 4** (parent_section casing/suffix variation): codify as Axis 4 of multi-axis taxonomy with single canonical form mandate for L2/L3/L4 (extending N27 from L1-only to L2-L4).
4. **NEW Axis 5 candidate** (page-boundary off-by-one motif integration): include N26 in multi-axis taxonomy as Axis 5 for unified per-family per-axis cumulative tracking.
5. **TABLE_HEADER continuation-page emission convention** (O-P1-184): codify single canonical form (executor convention "once per logical table" recommended; preserves atom-count parsimony).
6. **Schema clarification on heading_text** (O-P1-182): either explicitly declare heading_text in atom_schema HEADING properties OR set additionalProperties: false (with writer protocol update). Resolve prompt-vs-schema ambiguity.
7. **Hook 21 backport recommendation** (executor-direction page-boundary detection): even under v1.7 baseline (where Hook 21 is NOT yet active), N26 motif is observable. Round 14+ batches under v1.8 baseline will benefit from Hook 21 pre-DONE detection. Round 13 batch 51 evidence supports Hook 21 v1.8 codification value.

## §8 N6 Single-Dispatch Pattern Status (4th cumulative live-fire)

Round 11 batch 46 NEW PRECEDENT 1st + round 12 batch 48 2nd + round 12 batch 49 3rd + **round 13 batch 51 4th** = N6 single-dispatch pattern at **4 cumulative live-fires**. Status STRONGLY VALIDATED sustained (v1.8 codification at 3 cumulative live-fires; round 13 extends to 4 cumulative).

## §9 Rule Compliance

- **Rule A**: 10-atom audit slot #64 codex-family 5th burn extension (AUDIT pivot 45th cumulative) PASS 90.0% weighted; 4-dimension verdict 36/40 weighted PASS; 1 halt-grade verbatim FAIL (codex-strict rubric N26 motif on sv20_p0043_a011); main session disposition reclassified per kickoff §5.2 strict reading + schema reality.
- **Rule B**: 51a/51b atoms preserved as-emitted; Option H page-label correction RECOMMENDED for sv20_p0043_a011 + sv20_p0045_a001 at reconciler stage per N26 motif WARN-mode "logs to evidence; recommends Option H".
- **Rule C**: P1 batch report (this file) + drift cal report + Rule A summary + verdicts + sample + writer rerun artifact + executor self-claim DONE echo + codex DONE echo all preserved as evidence; reconciler-stage round 13 retro pending.
- **Rule D**: writer rerun (`oh-my-claudecode:writer`) ≠ executor baseline (`oh-my-claudecode:executor`) per N14 alternation; Rule A reviewer slot #64 (`codex:codex-rescue` 5th burn) is external runtime / different model — strongest Rule D isolation profile (codex-family 5-burn intra-family depth scale CANDIDATE VALIDATION post round 13 batch 51); main session disposition INDEPENDENT of writer/executor self-claims (5 cumulative confirmations writer/executor self-claim trust profile UNRELIABLE for direction-attribution-grade verdicts; main session PDF cross-check + codex Rule A independent verdict are authoritative).
- **Rule E**: O-P1-181 MEDIUM + O-P1-182/183/184 LOW filed for v1.9 candidate stack.

## §10 N14 STRONGLY VALIDATED Status Sustained 7th Live-Fire

Round 7 batch 33 1st + round 8 batch 36 2nd + round 9 batch 39 3rd + round 10 batch 42 4th + round 11 batch 45 5th + round 12 batch 48 6th + **round 13 batch 51 7th** = STRONGLY VALIDATED status sustained at 7 cumulative live-fires. v1.6 NEW EXECUTOR-VARIANT alternation pattern under v1.7 N21 baseline 3rd cumulative live-fire successfully attributing direction at multi-axis multi-direction granularity (round 13 = first executor-direction-dominant outcome).

## §11 v1.7 N21 Baseline 3rd Cumulative Live-Fire Validation

- **Production-side**: 51a + 51b 150 atoms executor-only per N21 (writer-family deprecated for production) — 3rd cumulative live-fire EFFECTIVE
- **Cumulative under v1.7 N21 post round 13 batch 51**: 1314 atoms cumulative executor-only, 0 writer-family contamination across 14 sub-batches
- **NEW round 13 finding**: executor-direction motifs observable (N26 + Axis 2 reversal). Executor-family is not infallible — has unique vulnerabilities (page-boundary off-by-one). v1.9 candidate stack: codify executor-direction motif tracking parallel to writer-direction motif tracking.

---

**P1 Batch 51 Closure**: 150 atoms (51a 65 + 51b 85), Rule A weighted PASS 90.0%, drift cal 13th cumulative GRANULARITY_DIVERGENCE_MULTI_AXIS_BIDIRECTIONAL (no Axis 1 fab; first executor-direction-dominant drift cal in P1 cumulative), N26 motif ≥2/batch executor-direction MEDIUM finding O-P1-181 (Option H recommendation deferred to reconciler), 4 findings filed O-P1-181..184 (1 MEDIUM + 3 LOW), v1.7 N21 production-side 3rd cumulative live-fire EFFECTIVE, N14 STRONGLY VALIDATED 7th live-fire, N6 single-dispatch 4th live-fire. NO HALT. Closure ready for reconciler stage round 13.
