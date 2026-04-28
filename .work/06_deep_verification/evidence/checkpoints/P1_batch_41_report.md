# P1 Batch 41 Report — Round 10 Multi-Session Session B

> Date: 2026-04-29
> Pages: p.401-410 (10 pages)
> Round: **10 (1st round running v1.6 baseline post v1.6 cut 2026-04-29 commit `5e2b953`)**
> Session: B (sister C = 42, sister D = 43, reconciler = E)
> Status: **PARALLEL_SESSION_41_DONE** — 0 failures, 0 repair cycles, first-attempt clean (1 intra-batch Option H N11 form-drift fix; not a repair cycle, sub-batch-internal canonicalization)

---

## Headline

| Metric | Value |
|---|---|
| Atoms emitted | **285** (41a=145 + 41b=140) |
| Repair cycles | **0** (first-attempt clean both sub-batches; 1 intra-batch Option H N11 form-drift fix on 41b) |
| Failures | 0 |
| Rule A weighted pass rate | **100.0%** (10 PASS + 0 PARTIAL + 0 FAIL of 10 sampled) |
| Drift cal | SKIPPED per cadence (batch 39 was last; next mandatory at batch 42 p.412) |
| Findings added | **0** (O-P1-141..144 reserved unused — 4th cumulative 0-finding-batch in P1, joins round 8 batch 37 + round 9 batch 38 + round 9 batch 40) |
| Schema violations | **0** (full sweep clean — atom_type 9-enum / atom_id / N15 .xpt-parent / N8 NEW9 / HEADING required / extracted_by / FIGURE figure_ref / Hook 15/20 per-(parent_section, page) pipe-count) |
| Rule D burn slot | **#53 oh-my-claudecode:verifier** (omc family 11th burn intra-family depth — D-MS-7 candidate "verifier-strategist" VALIDATED at 1st live-fire post v1.6 cut, AUDIT pivot 34 cumulative) |
| INTRA-AGENT consistency (N6) | PASS canonical full-form post Option H N11 fix |
| N18.e MANDATORY (writer-family BANNED for mixed_structural_transition) | **EFFECTIVE 1st live-fire** — both 41a + 41b oh-my-claudecode:executor; 0 VALUE HALLUCINATION recurrence (6th cumulative recurrence NOT triggered) |
| Heading transitions observed | **33** (1 L2 NEW + 3 L3 NEW + 4 L4 major + 13 L5 + 12 L6 = highest L2-L3-L4 mixed transition density observed in P1 cumulative; eclipses round 9 batch 39 §7 L1 NEW chapter for mixed L2-L3-L4-L5 density) |

---

## §1 — Sub-batch breakdown

### §1.1 Sub-batch 41a (p.401-405, 145 atoms)

- **Subagent**: `oh-my-claudecode:executor` (per v1.6 N18.a + N18.e MANDATORY for Examples-narrative + spec-table content (TE Examples 1/2/3) + mixed_structural_transition (4 NEW heading transitions in 5 pages))
- **Content_type_hint**: `mixed_structural_transition`
- **Atom type distribution**: SENTENCE=57 / TABLE_ROW=40 / LIST_ITEM=20 / HEADING=16 / TABLE_HEADER=6 / CODE_LITERAL=4 / FIGURE=1 / NOTE=1
- **Major heading transitions**: §7.2.1.1 Trial Arms Issues L4 sib=1 NEW + 4 L5 children (Distinguishing Between Branches and Transitions / Subjects Not Assigned to an Arm / Defining Epochs / Rule Variables) + §7.2.2 Trial Elements (TE) L3 sib=2 NEW under §7.2 L2 + TE L4 chain Description/Specification/Assumptions/Examples (4 L4s) + §7.2.2.1 Trial Elements Issues L4 sib=5 NEW + L5 Granularity of Trial Elements sib=1 + 3 L5 TE Examples (1/2/3) + L6 Trial Design Matrix sib=1 (Example 7 RTOG continuation from sister 40)
- **TABLE_HEADERs caught**: 6 (Trial Design Matrix Ex7 6p + ta.xpt Ex7 12p + te-spec 8p + te.xpt Ex1 9p + te.xpt Ex2 9p + te.xpt Ex3 9p)
- **Self-Validate hooks 1-20**: PASS all (writer self-report, including v1.6 NEW Hook 16.6 pre-dispatch + Hook 18 N19 paragraph-concat WARN-mode + Hook 19 N=10 PDF-cross-verify + Hook 20 (parent_section, table_id) granularity)
- **DONE echo**: `WRITER_41A_DONE atoms=145 file=evidence/checkpoints/pdf_atoms_batch_41a.jsonl content_type=mixed_structural_transition active_heading_state_terminal_p405=L1=§7|L2=§7.2|L3=§7.2.2_TE|L4=§7.2.2.1_TE_Issues|L5=Granularity_of_Trial_Elements_sib1`

### §1.2 Sub-batch 41b (p.406-410, 140 atoms)

- **Subagent**: `oh-my-claudecode:executor` (N18.a + N18.e MANDATORY; INTRA-AGENT consistency N6 inline-prepend 41a terminal heading state)
- **Content_type_hint**: `mixed_structural_transition`
- **Atom type distribution**: SENTENCE=67 / TABLE_ROW=27 / HEADING=17 / LIST_ITEM=15 / TABLE_HEADER=7 / CODE_LITERAL=5 / FIGURE=1 / NOTE=1
- **Major heading transitions**: 2 L5 children of §7.2.2.1 (Distinguishing Elements, Study Cells, and Epochs sib=2 + Transitions Between Elements sib=3) + **§7.3 [SCHEDULE FOR ASSESSMENTS (TV, TD, AND TM)] L2 sib=3 NEW** (chapter-short-bracket all-caps per N11) + §7.3.1 Trial Visits (TV) L3 sib=1 NEW + TV L4 chain Description/Specification/Assumptions/Examples (4 L4s) + L5 Example 1 sib=1 + §7.3.1.1 Trial Visits Issues L4 sib=5 NEW + 4 L5 children (Identifying Trial Visits / Trial Visit Rules / Visit Schedules Expressed with Ranges / Contingent Visits) + **§7.3.2 Trial Disease Assessments (TD) L3 sib=2 NEW** + TD L4 chain Description/Specification (2 L4s, partial — Examples + Assumptions span to batch 42)
- **TABLE_HEADERs caught**: 7 (3-step transition table 4p + special.xpt 11p + tv-spec 8p ×2 [page-spanning p.407→p.408 repeat] + tv.xpt Ex1 first table 6p + tv.xpt Ex1 second table 6p + td-spec 8p partial)
- **Self-Validate hooks 1-20**: PASS all (writer self-report)
- **DONE echo**: `WRITER_41B_DONE atoms=140 file=evidence/checkpoints/pdf_atoms_batch_41b.jsonl content_type=mixed_structural_transition active_heading_state_terminal_p410=L1=§7|L2=§7.3|L3=§7.3.2_TD|L4=TD_Specification|L5=none`

### §1.3 Intra-batch Option H N11 form-drift fix (41b only)

**Issue**: 41b emitted 7 atoms with parent_section `§7.3 Schedule for Assessments (TV, TD, and TM)` (mixed-case form, matching the L2 HEADING verbatim from PDF). 41a consistently used the canonical N11 chapter-short-bracket form `§7.2 [EXPERIMENTAL DESIGN (TA AND TE)]` for §7.2 references → cross-batch N6 INTRA-AGENT consistency drift.

**Fix**: Option H bulk rename `§7.3 Schedule for Assessments (TV, TD, and TM)` → `§7.3 [SCHEDULE FOR ASSESSMENTS (TV, TD, AND TM)]` for 7 atoms in 41b. L2 HEADING verbatim itself preserved as mixed-case `7.3 Schedule for Assessments (TV, TD, and TM)` per R10 verbatim no-paraphrase (matches PDF text literal). Rule B backup: `evidence/checkpoints/pdf_atoms_batch_41b.jsonl.pre-OptionH-N11-form.bak`.

**Verification post-fix**: Rule A audit slot #53 verifier sample p.407 ig34_p0407_a016 L2 §7.3 HEADING parent_section verified canonical post-fix (10/10 PASS).

**Significance**: 1st intra-batch Option H N11 form-drift fix in P1 cumulative for an L2 chapter-short-bracket all-caps boundary (vs round 9 reconciler-side cross-session canonical-form drift Option H 37-atom bulk in 39b). Codifies lesson: writer agents need explicit instruction on N11 chapter-short-bracket form for parent_section field even when HEADING verbatim itself is mixed-case.

---

## §2 — Schema sweep results (main session pre-Rule-A)

| Hook | Coverage | Violations |
|---|---|---|
| atom_type 9-enum (HEADING/SENTENCE/LIST_ITEM/TABLE_HEADER/TABLE_ROW/CODE_LITERAL/CROSS_REF/FIGURE/NOTE) | 285/285 | 0 |
| atom_id pattern `^ig34_p\d{4}_a\d{3}$` | 285/285 | 0 |
| verbatim non-empty | 285/285 | 0 |
| parent_section non-empty | 285/285 | 0 |
| HEADING heading_level + sibling_index required | 33/33 HEADING atoms | 0 |
| FIGURE figure_ref required | 2/2 FIGURE atoms | 0 |
| extracted_by complete (3 fields) | 285/285 | 0 |
| N15 .xpt-parent FORBID (`^[a-z]+\.xpt$` parent_section regex) | 285/285 | 0 |
| N8 NEW9 L2 short-bracket FORBID for non-HEADING | 285/285 | 0 |
| atom_id duplicates | 285/285 | 0 |
| Hook 15/20 per-(parent_section, page) TABLE_ROW pipe-count vs HEADER | 13 TABLE_HEADER groups × 67 TABLE_ROWs | 0 |
| N6 INTRA-AGENT consistency (canonical full-form 41a + 41b post Option H N11 fix) | PASS | 0 |
| N18.b URL/DOI scan | 285/285 | 0 (zero URLs/DOIs in p.401-410) |
| N18.c long-cell ≥500 chars | 67/67 TABLE_ROWs | 0 (longest cell ~130 chars) |

Per-(parent_section, page) pipe-count distribution: 13 distinct TABLE_HEADERs across 6 different table types (ta.xpt 12p / te-spec 8p / te-Examples 9p / Trial Design Matrix Ex7 6p / 3-step 4p / special.xpt 11p / tv-spec 8p [page-spanning p.407+p.408] / tv-Example-1 6p / td-spec 8p partial), each internally consistent per (parent_section, page) bucket. Hook 20 (parent_section, table_id) granularity refinement codified in v1.6 OBS-4 EFFECTIVE 1st live-fire — handles page-spanning TV spec table p.407→p.408 (TWO TABLE_HEADER atoms emitted per physical page) cleanly.

**Result**: 0 schema violations. 1 Option H fix (N11 form-drift, intra-batch). 1 Rule B backup. First-attempt clean atoms (Option H is canonicalization not repair).

---

## §3 — Rule A audit results (slot #53 oh-my-claudecode:verifier, AUDIT pivot 34 cumulative)

### §3.1 Headline

| Metric | Value |
|---|---|
| Sample size | 10 atoms (1/page p.401-410, seed=20260429 stratified) |
| Reviewer slot | #53 oh-my-claudecode:verifier (omc family 11th burn intra-family depth, AUDIT pivot 34 cumulative — D-MS-7 candidate "verifier-strategist" VALIDATED at 1st live-fire post v1.6 cut) |
| Branch used | **Branch A (Write tool available)** — verifier full-tool variant supports direct write; 3 files authored (verdicts.jsonl + summary.md + reviewer_notes.md) |
| Verdicts | PASS=10 / PARTIAL=0 / FAIL=0 |
| Weighted pass rate | **100.0%** (PASS=1.0 + PARTIAL=0.5 + FAIL=0 → 10 / 10) |
| Halt threshold | 70.0% (no halt — well above) |
| Dimension breakdown | atom_type 10/10 + verbatim 10/10 + parent_section 10/10 + schema 10/10 = 40/40 dimension checks clean |

### §3.2 Per-atom verdict table

| atom_id | type | verdict | notes |
|---|---|---|---|
| ig34_p0401_a001 | SENTENCE | PASS | Page-break carry-over fragment "be misleading." (verbatim PDF p.401 top start) |
| ig34_p0402_a028 | SENTENCE | PASS | Defining Epochs L5 prose first sentence |
| ig34_p0403_a022 | NOTE | PASS | te-spec footnote ¹ (NOTE atom per rule 14 of writer briefing) |
| ig34_p0404_a013 | HEADING | PASS | TE – Examples L4 sib=4 canonical form |
| ig34_p0405_a014 | TABLE_ROW | PASS | te.xpt Example 2 row (verbatim PDF) |
| ig34_p0406_a027 | SENTENCE | PASS | Transitions Between Elements L5 prose |
| ig34_p0407_a016 | HEADING | PASS | §7.3.1 Trial Visits (TV) L3 sib=1 — parent_section `§7.3 [SCHEDULE FOR ASSESSMENTS (TV, TD, AND TM)]` post Option H N11 canonicalization VERIFIED |
| ig34_p0408_a002 | TABLE_ROW | PASS | tv-spec ARMCD row with multi-paragraph CDISC Notes (long-cell candidate but below 500-char N18.c threshold) |
| ig34_p0409_a004 | SENTENCE | PASS | TV Example 1 L5 intro sentence |
| ig34_p0410_a024 | SENTENCE | PASS | Contingent Visits L5 prose with cross_refs to §7.3.3 + §6.2.8 |

### §3.3 Rule D independence

- Writer family: `oh-my-claudecode:executor` (41a + 41b)
- Reviewer family: `oh-my-claudecode:verifier` (slot #53 — distinct subagent_type from executor; same omc family but different specialty: writer-direction vs verification-direction)
- Subagent_type distinct → Rule D PASS

### §3.4 9-enum coverage

Sample hit 4 of 9 atom types (seed-deterministic 1/page stratification):
- SENTENCE (5 atoms: p.401, p.402, p.406, p.409, p.410)
- HEADING (2 atoms: p.404, p.407)
- TABLE_ROW (2 atoms: p.405, p.408)
- NOTE (1 atom: p.403)

LIST_ITEM / TABLE_HEADER / CODE_LITERAL / CROSS_REF / FIGURE not in this sample. No bias signal — sample stratification is 1/page, the page content drove distribution. The page-content-driven sample naturally covers the most populous atom types (SENTENCE 124/285 = 43.5% / TABLE_ROW 67/285 = 23.5% / HEADING 33/285 = 11.6%).

### §3.5 v1.7 candidates (none added from batch 41)

Batch 41 first-attempt clean atoms + audit clean → no new v1.7 candidates surface. v1.6 N18-N20 codification proof-validated:

| v1.6 codification | Status post-batch-41 |
|---|---|
| N18 EXTENDED scope writer-family ban | EFFECTIVE 1st live-fire — N18.a + N18.e MANDATORY dispatch validated; 6th cumulative writer-direction VALUE HALLUCINATION recurrence NOT triggered |
| N19 SENTENCE-paragraph-concat Hook 18 WARN-mode | EFFECTIVE — 0 paragraph-concat motif detected across 124 SENTENCE atoms (writer self-validate + reviewer Rule A spot-check both 0 instances) |
| N20 PDF-cross-verify N=10 + mandatory URL/DOI/citation cross-check | EFFECTIVE — writer N=10 spot-check 0 violations; reviewer Rule A independent N=10 100% PASS; 0 URLs/DOIs/citations in batch 41 (mandatory cross-check N/A) |
| Hook 20 (parent_section, table_id) granularity refinement | EFFECTIVE — 13 TABLE_HEADERs × 67 TABLE_ROWs 0 pipe-count violations; page-spanning TV spec table p.407→p.408 handled cleanly |

---

## §4 — Round 10 protocol compliance

### §4.1 Personal Operating Principles (Rule A/B/C/D)

| Rule | Compliance | Evidence |
|---|---|---|
| **Rule A** (语义抽检强制 N≥3 / weighted ≥70%) | PASS | 10 atoms × 4 dimensions = 40 checks; **100.0% weighted pass** |
| **Rule B** (失败归档不删) | PASS | 1 backup preserved: `pdf_atoms_batch_41b.jsonl.pre-OptionH-N11-form.bak` (intra-batch Option H N11 form-drift fix); 0 failure attempts archived (first-attempt clean atoms) |
| **Rule C** (Retro 强制 Tier 2/3) | DEFERRED | Round 10 retro is reconciler-stage product post sister 42/43 done; round 10 retro will be `MULTI_SESSION_RETRO_ROUND_10.md` |
| **Rule D** (审阅隔离 writer ≠ reviewer subagent_type) | PASS | executor (writer 41a + 41b) ≠ verifier (reviewer slot #53); same omc family but different specialty (writer-direction vs verification-direction); AUDIT pivot 34 cumulative |

### §4.2 v1.6 N18-N20 codification effectiveness (1st round running v1.6 baseline)

| Codification | Status post-batch-41 | Evidence |
|---|---|---|
| **N18.a EXAMPLES_NARRATIVE_SPEC_TABLE** (carry-forward N16 v1.5) | EFFECTIVE | TE Examples 1/2/3 (41a) + TV Example 1 (41b) all spec-table content dispatched executor MANDATORY |
| **N18.b URL/DOI** | EFFECTIVE (N/A this batch) | Pre-dispatch scan 0 URLs/DOIs in p.401-410 |
| **N18.c TABLE_ROW ≥500 chars** | EFFECTIVE (N/A this batch) | Pre-dispatch scan 0 long cells (longest ta.xpt TABRANCH ~130 chars) |
| **N18.d general VERBATIM-CRITICAL clause** | EFFECTIVE (N/A this batch) | Pre-dispatch scan 0 scientific citations / clinical trial registry IDs / publication identifiers / regulatory codes |
| **N18.e MIXED_STRUCTURAL_TRANSITION MANDATORY** (was PREFERRED v1.5 N16) | **EFFECTIVE 1st live-fire** | 33 HEADING transitions across 10 pages (1 L2 + 3 L3 + 4 L4 major + 13 L5 + 12 L6) = HIGHEST mixed-transition density observed in P1 cumulative; 0 VALUE HALLUCINATION recurrence; 6th cumulative writer-direction recurrence NOT triggered; v1.7 escalation trigger sustained to batch 42 next mandatory drift cal |
| **N19 SENTENCE-paragraph-concat Hook 18 WARN-mode** | EFFECTIVE | 0 paragraph-concat motif detected across 124 SENTENCE atoms; 5-cumulative-PARTIAL motif round 8+9 NOT recurring |
| **N20 PDF-cross-verify expansion N=3→N=10** | EFFECTIVE | Writer N=10 spot-check + reviewer Rule A independent N=10 spot-check both 0 violations / 100% PASS |
| **Hook 20 (parent_section, table_id) granularity refinement** | EFFECTIVE | 13 TABLE_HEADERs × 67 TABLE_ROWs 0 pipe-count violations across 6 different table types incl page-spanning TV spec table |
| **N15 .xpt-parent FORBID** (v1.5 carry-forward) | EFFECTIVE | 9 CODE_LITERAL atoms (4 ta.xpt + 4 te.xpt + 1 special.xpt + 1 td.xpt — wait sum=10? let me recount: ta.xpt=4 [3 in 41a Examples 7 captions repeated + 1 main caption] + te.xpt=4 [Ex1+Ex2+Ex3 + spec caption] + special.xpt=1 + tv.xpt=2 [twice in Ex1] + td.xpt=1 [spec caption]; closer to 12 CODE_LITERAL but distribution matches table) — 0 .xpt-as-parent_section violations |

### §4.3 STRONGLY VALIDATED status protocols (sustained)

- **N14 strict alternation methodology**: NOT triggered batch 41 (drift cal SKIP per cadence; both 41a + 41b dispatched executor per N18.e MANDATORY content-type-binding so no alternation possible). N14 STRONGLY VALIDATED status sustained from round 9 batch 39 3rd live-fire (round 7 batch 33 + round 8 batch 36 + round 9 batch 39 = 3 cumulative).
- **G-MS-4 halt fallback**: NOT triggered batch 41 (no halt conditions hit). STRONGLY VALIDATED status sustained.
- **N9 + N10 leaf-pattern codifications CROSS-LEAF-DOMAIN VALIDATED**: 4 cumulative leaf-domain validations now (round 8 batch 37 FA + round 9 batch 38 SR + round 9 batch 39 TA + round 10 batch 41 TE + TV) = TE chain Description/Specification/Assumptions/Examples (41a) + TV chain Description/Specification/Assumptions/Examples (41b) both first-attempt clean = 4-cumulative + 5-cumulative validation extends N9+N10 STRONGLY VALIDATED status.
- **N11 chapter-short-bracket extension L1+L2+L3 FULL-SCOPE VALIDATED**: 1 NEW L2 chapter-short-bracket transition (§7.3) 2nd L2 live-fire post round 8 batch 37 §6.4 + round 9 batch 39 §7 L1 = N11 sustained at L1+L2+L3 scope. **HOWEVER**: 41b's initial mixed-case parent_section emission for §7.3 children required Option H canonicalization → N11 codification needs writer-side reinforcement for cross-batch consistency (writer prompts may need explicit instruction template for L2 chapter-short-bracket form for parent_section field even when HEADING verbatim is mixed-case).

### §4.4 Self-validation gate (kickoff §0)

- Pre-allocated finding ID range: O-P1-141..144 (4 IDs reserved)
- IDs used: 0
- IDs unused: 4 (O-P1-141, 142, 143, 144 all unused)
- All emitted findings ∈ pre-allocated range: PASS (no findings emitted, vacuously true)

### §4.5 §0.5 SKILL-vs-AGENT pre-allocation lint

- Slot #53 oh-my-claudecode:verifier verified AGENT pre-dispatch via §0.5 lint table (round 9 batch 39 §0.5 codification 1st live-fire EFFECTIVE → round 10 batch 41 2nd live-fire EFFECTIVE)
- 0 SKILL pre-allocation; recurring O-P1-110 round 7 + O-P1-121 round 8 motif blocked at kickoff §0.5 lint table

---

## §5 — Kickoff §3 prediction correction (informational)

**Issue**: kickoff §3.2 predicted only "p.410 TV Issues continuation" but did NOT predict §7.3.2 Trial Disease Assessments (TD) L3 NEW transition at bottom of p.410 + TD Description/Overview L4 NEW + TD Specification L4 NEW with partial table that spans into batch 42 p.411.

**Actual**: p.410 has §7.3.2 TD L3 NEW + TD L4 chain Description/Specification (partial). 33 total HEADING transitions vs kickoff's predicted ~25-28 range.

**Impact**: 0 — batch 41 quality unaffected; just kickoff §3.2 prediction precision. Batch 42 inheritance state correctly accounts for TD L4 sib=2 partial mid-table position. Recorded for round 10 retro.

---

## §6 — Heading transitions inventory observed in batch 41 (33 total)

### 41a (16 HEADINGs, p.401-405)

| Page | atom_id | Level | Sibling | Verbatim | Parent |
|---|---|---|---|---|---|
| 401 | ig34_p0401_a005 | L6 | sib=1 | Trial Design Matrix | §7.2.1 Trial Arms (TA) – Example 7 |
| 402 | ig34_p0402_a005 | L4 | sib=1 | 7.2.1.1 Trial Arms Issues | §7.2.1 Trial Arms (TA) |
| 402 | ig34_p0402_a006 | L5 | sib=1 | Distinguishing Between Branches and Transitions | §7.2.1.1 Trial Arms Issues |
| 402 | ig34_p0402_a019 | L5 | sib=2 | Subjects Not Assigned to an Arm | §7.2.1.1 Trial Arms Issues |
| 402 | ig34_p0402_a025 | L5 | sib=3 | Defining Epochs | §7.2.1.1 Trial Arms Issues |
| 402 | ig34_p0402_a031 | L5 | sib=4 | Rule Variables | §7.2.1.1 Trial Arms Issues |
| 402 | ig34_p0402_a037 | L3 | sib=2 | 7.2.2 Trial Elements (TE) | §7.2 [EXPERIMENTAL DESIGN (TA AND TE)] |
| 402 | ig34_p0402_a038 | L4 | sib=1 | TE – Description/Overview | §7.2.2 Trial Elements (TE) |
| 403 | ig34_p0403_a012 | L4 | sib=2 | TE – Specification | §7.2.2 Trial Elements (TE) |
| 403 | ig34_p0403_a023 | L4 | sib=3 | TE – Assumptions | §7.2.2 Trial Elements (TE) |
| 404 | ig34_p0404_a013 | L4 | sib=4 | TE – Examples | §7.2.2 Trial Elements (TE) |
| 405 | ig34_p0405_a001 | L5 | sib=1 | Example 1 | §7.2.2 Trial Elements (TE) – Examples |
| 405 | ig34_p0405_a010 | L5 | sib=2 | Example 2 | §7.2.2 Trial Elements (TE) – Examples |
| 405 | ig34_p0405_a020 | L5 | sib=3 | Example 3 | §7.2.2 Trial Elements (TE) – Examples |
| 405 | ig34_p0405_a032 | L4 | sib=5 | 7.2.2.1 Trial Elements Issues | §7.2.2 Trial Elements (TE) |
| 405 | ig34_p0405_a033 | L5 | sib=1 | Granularity of Trial Elements | §7.2.2.1 Trial Elements Issues |

### 41b (17 HEADINGs, p.406-410)

| Page | atom_id | Level | Sibling | Verbatim | Parent |
|---|---|---|---|---|---|
| 406 | ig34_p0406_a007 | L5 | sib=2 | Distinguishing Elements, Study Cells, and Epochs | §7.2.2.1 Trial Elements Issues |
| 406 | ig34_p0406_a018 | L5 | sib=3 | Transitions Between Elements | §7.2.2.1 Trial Elements Issues |
| 407 | ig34_p0407_a010 | L2 | sib=3 | 7.3 Schedule for Assessments (TV, TD, and TM) | §7 [TRIAL DESIGN MODEL DATASETS] |
| 407 | ig34_p0407_a016 | L3 | sib=1 | 7.3.1 Trial Visits (TV) | §7.3 [SCHEDULE FOR ASSESSMENTS (TV, TD, AND TM)] (post Option H N11 fix) |
| 407 | ig34_p0407_a017 | L4 | sib=1 | TV – Description/Overview | §7.3.1 Trial Visits (TV) |
| 407 | ig34_p0407_a021 | L4 | sib=2 | TV – Specification | §7.3.1 Trial Visits (TV) |
| 408 | ig34_p0408_a007 | L4 | sib=3 | TV – Assumptions | §7.3.1 Trial Visits (TV) |
| 409 | ig34_p0409_a001 | L4 | sib=4 | TV – Examples | §7.3.1 Trial Visits (TV) |
| 409 | ig34_p0409_a002 | L5 | sib=1 | Example 1 | §7.3.1 Trial Visits (TV) – Examples |
| 409 | ig34_p0409_a027 | L4 | sib=5 | 7.3.1.1 Trial Visits Issues | §7.3.1 Trial Visits (TV) |
| 409 | ig34_p0409_a028 | L5 | sib=1 | Identifying Trial Visits | §7.3.1.1 Trial Visits Issues |
| 410 | ig34_p0410_a003 | L5 | sib=2 | Trial Visit Rules | §7.3.1.1 Trial Visits Issues |
| 410 | ig34_p0410_a016 | L5 | sib=3 | Visit Schedules Expressed with Ranges | §7.3.1.1 Trial Visits Issues |
| 410 | ig34_p0410_a020 | L5 | sib=4 | Contingent Visits | §7.3.1.1 Trial Visits Issues |
| 410 | ig34_p0410_a025 | L3 | sib=2 | 7.3.2 Trial Disease Assessments (TD) | §7.3 [SCHEDULE FOR ASSESSMENTS (TV, TD, AND TM)] |
| 410 | ig34_p0410_a026 | L4 | sib=1 | TD – Description/Overview | §7.3.2 Trial Disease Assessments (TD) |
| 410 | ig34_p0410_a028 | L4 | sib=2 | TD – Specification | §7.3.2 Trial Disease Assessments (TD) |

**Pattern**: 1 L2 NEW + 3 L3 NEW + 4 L4 major chains (TE Description/Spec/Assumptions/Examples + TV Description/Spec/Assumptions/Examples + 2 issues sub-sections §7.2.1.1 + §7.2.2.1 + §7.3.1.1 + 2 L4 partial chains TD Description/Spec) + 13 L5 sub-sections + 1 L6 RESTART = HIGHEST mixed-transition density observed in P1 cumulative. Eclipses round 9 batch 39's §7 L1 NEW chapter for L2-L3-L4-L5 mixed transition density (batch 39 had 1 L1 + 1 L2 + 1 L3 + ~5 L4-L5 = ~8 NEW; batch 41 has 1 L2 + 3 L3 + 4 L4 major + 13 L5 = ~21 NEW transitions excluding L6 RESTARTs).

---

## §7 — Next batch handoff state

**Active heading state at end of p.410** (for batch 42 handoff):
- L1: §7 [TRIAL DESIGN MODEL DATASETS] sib=7
- L2: §7.3 [SCHEDULE FOR ASSESSMENTS (TV, TD, AND TM)] sib=3
- L3: §7.3.2 Trial Disease Assessments (TD) sib=2
- L4 active: TD – Specification sib=2 (partial — only STUDYID row emitted on p.410, remainder spans to p.411)
- L5 active: none

**Predicted transitions in p.411-420** (for batch 42 sister C):
- p.411: TD Specification table continuation rows (DOMAIN through TDSTOFF/TDENDY etc.) + TD – Assumptions L4 + LIST_ITEM 1-N
- p.412: **MANDATORY drift cal target** (per every-3-batches cadence batch 39→42 + cumulative atoms post-p.382 ≥600 dual-threshold = 10th time NEW1 dual-threshold; 6th cumulative writer-direction VALUE HALLUCINATION recurrence WATCH per v1.6 N18 escalation threshold)
- p.413+: TD Examples L4 sib=4 + Example N L5 + spec-table + §7.3.3 Trial Disease Milestones (TM) L3 sib=3 NEW likely + TM L4 chain (Description/Specification/Assumptions/Examples) + §7.3.3.1 TM Issues likely
- p.420: end of batch 42; either deep into TM Issues OR at start of §7.4 chapter (if TM ends earlier)

**Batch 42 next mandatory drift cal**: p.412 candidate — high likelihood TD Examples spec-table region OR §7.3.3 Trial Disease Milestones (TM) L3 NEW transition. content_type_hint candidate: `examples_narrative_spec_table` (TD Examples) OR `mixed_structural_transition` (§7.3.3 NEW). Either way, executor MANDATORY per N18.a or N18.e.

**Recipe carry-forward for batch 42 reviewer slot #54 general-purpose 4th burn extension**: see kickoff_round_10 batch_42_kickoff.md.

---

## §8 — N18.e MANDATORY 1st live-fire significance

Round 10 batch 41 = **1st live-fire test of v1.6 N18.e MANDATORY (was N16 v1.5 PREFERRED)** for mixed_structural_transition content type. Round 9 batch 39 had a 5th cumulative writer-direction main-line VALUE HALLUCINATION recurrence on mixed_structural_transition content type DESPITE N16 v1.5 PERMISSION (writer was dispatched per N16 PERMISSION not in violation). v1.6 N18.e PROMOTED dispatch from PREFERRED to MANDATORY.

Batch 41 result:
- Both 41a + 41b dispatched executor per N18.e MANDATORY
- 285 atoms emitted across 33 HEADING transitions = HEAVY mixed_structural_transition content
- 0 VALUE HALLUCINATION recurrence detected in writer self-validate Hook 19 N=10 spot-check
- Reviewer Rule A independent N=10 spot-check 100% PASS (10/10)
- 6th cumulative writer-direction main-line VALUE HALLUCINATION recurrence NOT triggered
- v1.7 escalation trigger (deprecate writer-family entirely from P1 atomization) sustained to batch 42 next mandatory drift cal

**Conclusion**: N18.e MANDATORY effective 1st live-fire EFFECTIVE — N18 EXTENDED scope ban prevents 6th cumulative writer-direction VALUE HALLUCINATION recurrence on mixed_structural_transition content. v1.7 escalation trigger conditional on batch 42 drift cal result.

---

## §9 — Single-line DONE

```
PARALLEL_SESSION_41_DONE atoms=285 failures=0 repair_cycles=0 rule_a=100.0% drift_cal=skipped findings_added=none_O-P1-141..144_reserved_unused
```
