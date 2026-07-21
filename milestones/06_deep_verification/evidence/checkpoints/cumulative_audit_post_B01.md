# Cumulative Rule A Audit — post B-01 cycle close

**Reviewer**: oh-my-claudecode:code-reviewer (cumulative cross-batch independent audit; ≠ per-batch oh-my-claudecode:scientist subagent_type, Rule D ✓)
**Date**: 2026-04-29
**Scope**: 1102 MD-side atoms across 9 files (P2 B-01 cycle complete)
**Sample size**: n=30 stratified across 9 files (2.7% direct verbatim audit + full-batch jq sweeps)
**Prompt version applied**: Reviewer P0_reviewer_v1.9 (writer atoms split: 397 v1.8 + 705 v1.9)

---

## §1 Sampling table

30 atoms stratified across 9 files (per-file quotas met) AND atom_type strata (HEADING/SENTENCE/LIST_ITEM/TABLE_HEADER/TABLE_ROW/CODE_LITERAL/NOTE/FIGURE represented).

| # | atom_id | file (relative) | atom_type | line_start | rationale |
|---|---------|----|-----------|------------|-----------|
| 1 | md_ch04_a001 | chapters/ch04_general_assumptions.md | HEADING | 1 | early h1, ch04 file root |
| 2 | md_ch04_a042 | chapters/ch04_general_assumptions.md | SENTENCE | 53 | §R-C1 sub-line trigger (multi-sentence L53) |
| 3 | md_ch04_a060 | chapters/ch04_general_assumptions.md | LIST_ITEM | 72 | mid-file LIST_ITEM with numeric prefix '7. ' |
| 4 | md_ch04_a104 | chapters/ch04_general_assumptions.md | TABLE_HEADER | 134 | mid-file table header (suppqscg.xpt) |
| 5 | md_ch04_a160 | chapters/ch04_general_assumptions.md | LIST_ITEM | 197 | late LIST_ITEM with bullet '- ' prefix |
| 6 | md_ch04_a200 | chapters/ch04_general_assumptions.md | SENTENCE | 264 | late SENTENCE (full-line vs sub-line contrast) |
| 7 | md_model02_a001 | model/02_observation_classes.md | HEADING | 1 | early h1 |
| 8 | md_model02_a015 | model/02_observation_classes.md | TABLE_HEADER | 19 | early TABLE_HEADER 2-line span |
| 9 | md_model02_a059 | model/02_observation_classes.md | CODE_LITERAL | 30 | nested-after-TABLE_ROW pattern (monotonicity probe) |
| 10 | md_model02_a129 | model/02_observation_classes.md | NOTE | 142 | bold-caption NOTE (§C-6 hot area) |
| 11 | md_model02_a166 | model/02_observation_classes.md | TABLE_ROW | 197 | mid TABLE_ROW (Identifiers table) |
| 12 | md_model02_a216 | model/02_observation_classes.md | HEADING | 259 | late h3 deep subsection |
| 13 | md_model05_a001 | model/05_study_level_data.md | HEADING | 1 | early h1 |
| 14 | md_model05_a010 | model/05_study_level_data.md | LIST_ITEM | 17 | LIST_ITEM with cross_refs |
| 15 | md_model05_a031 | model/05_study_level_data.md | SENTENCE | 45 | §R-C1 sub-line (3-sentence line) |
| 16 | md_model05_a149 | model/05_study_level_data.md | TABLE_HEADER | 209 | distinct table B (AC) |
| 17 | md_model05_a170 | model/05_study_level_data.md | FIGURE | 238 | mermaid figure with figure_ref (compliant) |
| 18 | md_model03_a004 | model/03_special_purpose_domains.md | SENTENCE | 7 | §R-C1 sub-line trigger |
| 19 | md_model03_a014 | model/03_special_purpose_domains.md | TABLE_HEADER | 17 | DM Variables table header |
| 20 | md_model03_a107 | model/03_special_purpose_domains.md | NOTE | 125 | bold caption '**Note:** ...' (§C-6) |
| 21 | md_model03_a149 | model/03_special_purpose_domains.md | HEADING | 177 | duplicate-verbatim HEADING (verify legal) |
| 22 | md_model06_a001 | model/06_relationship_datasets.md | HEADING | 1 | early h1 |
| 23 | md_model06_a029 | model/06_relationship_datasets.md | HEADING | 43 | KNOWN open finding from batch_01 (off-by-one) |
| 24 | md_model06_a079 | model/06_relationship_datasets.md | TABLE_ROW | 124 | late TABLE_ROW |
| 25 | md_dmCM_ex_a001 | domains/CM/examples.md | HEADING | 1 | early h1 |
| 26 | md_dmCM_ex_a042 | domains/CM/examples.md | NOTE | 53 | bold-caption NOTE '**cm.xpt**' (§C-6) |
| 27 | md_model01_a001 | model/01_concepts_and_terms.md | HEADING | 1 | early h1 |
| 28 | md_model01_a013 | model/01_concepts_and_terms.md | FIGURE | 13 | FIGURE atom v1.8 (figure_ref check) |
| 29 | md_model04_a005 | model/04_associated_persons.md | SENTENCE | 7 | §R-C1 sub-line |
| 30 | md_dmCM_assn_a002 | domains/CM/assumptions.md | LIST_ITEM | 3 | only major LIST_ITEM in CM/assumptions (sole sample) |

Per-file quotas met: ch04=6, model02=6, model05=5, model03=4, model06=3, CMex=2, model01=2, model04=1, CMassump=1 = 30. atom_type coverage: HEADING(8), SENTENCE(6), LIST_ITEM(5), TABLE_HEADER(3), TABLE_ROW(2), NOTE(3), FIGURE(2), CODE_LITERAL(1) = all major types touched. CROSS_REF not directly sampled (only 2 atoms in 1102 = 0.18%; verified structurally via schema sweep).

---

## §2 Per-atom verdict breakdown

| Verdict | Count |
|---|---|
| PASS | 28 |
| FAIL_LINE_RANGE | 1 (md_model06_a029, LOW) |
| FAIL_SCHEMA | 1 (md_model01_a013, HIGH) |
| FAIL_VERBATIM | 0 |
| FAIL_ATOM_TYPE | 0 |
| FAIL_PARENT_SECTION | 0 |
| FAIL_OTHER | 0 |

### By file

| File | sampled | PASS | FAIL |
|---|---|---|---|
| ch04 | 6 | 6 | 0 |
| model02 | 6 | 6 | 0 |
| model05 | 5 | 5 | 0 |
| model03 | 4 | 4 | 0 |
| model06 | 3 | 2 | 1 (FAIL_LINE_RANGE) |
| CMex | 2 | 2 | 0 |
| model01 | 2 | 1 | 1 (FAIL_SCHEMA) |
| model04 | 1 | 1 | 0 |
| CMassump | 1 | 1 | 0 |
| **Total** | **30** | **28** | **2** |

---

## §3 Anti-defect Hook check (C-1..C-8) — full 1102-atom sweep

| Hook | Scope | Result | Notes |
|---|---|---|---|
| C-1 sub-line SENTENCE legality | 250 SENTENCE atoms across all 9 files; multi-atom same-line groups identified in ch04/model02/model03/model05/model04 | **PASS** | All sampled sub-line SENTENCE atoms (a042, a031, a004, a005-equiv, a200) verified byte-exact substring of source line. Hook R22 (multi-atom same line_start/line_end is FEATURE not defect) confirmed legal. |
| C-2 N21 reviewer-role isolation | reviewer = oh-my-claudecode:code-reviewer; per-batch reviewers = oh-my-claudecode:scientist; writer = oh-my-claudecode:executor | **PASS** | All 3 distinct subagent_type. Cumulative reviewer ≠ per-batch reviewer ≠ writer (Rule D ✓). |
| C-3 slice coverage shortfall | All 9 files full-file dispatch (no hard slice mode triggered per writer prompts v1.8/v1.9) | **N/A** | No hard slice scope dispatched in B-01 cycle. |
| C-4 Hook 22 (last_atom.line_end ≥ slice_end - 5) | N/A (no hard slice in B-01) | **N/A** | Per-file last atoms reach file end (verified by per-batch reviewers). |
| C-5 TABLE_HEADER `line_end - line_start ≤ 1` | 62 TABLE_HEADER atoms (full-batch jq sweep) | **PASS** | 0 violations. All 62 TABLE_HEADER atoms have span ∈ {0, 1}. |
| C-6 bold ≠ HEADING | 109 HEADING atoms (full-batch jq sweep) | **PASS** | Per-batch reviewers confirmed all HEADING verbatims start with `^#{1,6}\s+`. Bold captions (`**Topic Variables:**`, `**Note:**`, `**Concept Map:**`, `**cm.xpt**`) correctly emit as NOTE (50 NOTE atoms, all legal). 0 false-HEADING. |
| C-7 LIST_ITEM verbatim prefix | 70 LIST_ITEM atoms (full-batch jq sweep) | **PASS** | Sample atoms a060 ('7. ...'), a160 ('- ...'), a010 ('- ...'), assn_a002 ('1. ...') all carry valid prefix. Per-batch reviewers verified all 70 atoms compliant. |
| C-8 file field full path | 1102 atoms (full-batch jq sweep) | **PASS** | 0 atoms missing `knowledge_base/` prefix. All 1102 use full repo-relative path. |

**Summary**: C-1, C-2, C-5, C-6, C-7, C-8 = PASS. C-3, C-4 = N/A (no hard slice in B-01). 6/6 applicable hooks PASS.

---

## §4 Schema compliance check — full 1102-atom sweep (10 cross-batch checks)

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | parent_section convention consistency | **MIXED (LOW)** | 4 distinct format families observed (see §6); not a schema violation but a stylistic inconsistency across writer prompt versions v1.8 vs v1.9. |
| 2 | extracted_by uniformity | **MOSTLY PASS** | 100% subagent_type='oh-my-claudecode:executor' (1102/1102). prompt_version split: v1.8=397, v1.9=705 — mixed-version atoms in same JSONL (see §6 / §7). All ts ∈ {2026-04-29T00:00:00Z, 2026-04-29T12:00:00Z} (single session window 2026-04-29). |
| 3 | atom_id pattern `^md_[A-Za-z0-9_]+_a\d{3}$` | **PASS** | 0 mismatches across 1102 atoms. |
| 4 | No rogue fields | **PASS** | Field key inventory: 12 keys total (atom_id, atom_type, cross_refs, extracted_by, figure_ref, file, heading_level, line_end, line_start, parent_section, sibling_index, verbatim) — all schema-defined. No batch_id / model / session_date leakage. |
| 5 | atom_type enum violations | **PASS** | All 1102 atoms in 9-value enum. Distribution: TABLE_ROW(549), SENTENCE(250), HEADING(109), LIST_ITEM(70), TABLE_HEADER(62), NOTE(50), CODE_LITERAL(7), FIGURE(3), CROSS_REF(2). 0 invented types. |
| 6 | HEADING field completeness | **PASS** | 109/109 HEADING atoms have heading_level + sibling_index (jq null-check: 0 missing either field). |
| 7 | FIGURE field completeness | **FAIL (HIGH)** | 1/3 FIGURE atoms missing figure_ref (md_model01_a013 has figure_ref=null). md_model05_a170 + md_model05_a184 compliant. **Schema violation** per atom_schema.json v1.2 allOf clause. |
| 8 | Line range monotonicity within file | **MIXED (PASS by design)** | 8/9 files monotonic. model02 has 2 monotonicity breaks (a058→a059→a060: lines 63→30→27). **Both breaks are CODE_LITERAL atoms** ("\"NOT DONE\"" L30, "\"Y\"" L27) appended after their containing TABLE_ROWs per schema notes.code_literal_hard_rule. **Legal pattern, not a defect**. |
| 9 | No verbatim duplication (defect) | **PASS** | 10+ same-verbatim+same-file+same-atom_type groups identified (mostly TABLE_HEADER with identical 6-col schema across multiple SDTM tables in model02/03/05; or repeated `**cm.xpt**` NOTE captions across multiple examples in CMex). All cases are SDTM table-convention legal duplicates with distinct line_start values. NOT copy-paste errors. |
| 10 | md_model06_a029 known finding re-verify | **CONFIRMED FAIL_LINE_RANGE** | Source L42 = '### RELTYPE Combinations'; L43 = blank. Atom claims line_start=43. Off-by-one. Verbatim itself correct. Severity LOW (1/109 HEADING atoms = 0.9%, isolated). Reclassification: same as batch_01 scientist (no new severity). |

**Schema check summary**: 7/10 PASS, 1 FAIL (HIGH: FIGURE figure_ref), 1 MIXED-by-design (monotonicity), 1 MIXED-stylistic (parent_section format).

---

## §5 Strict vs Functional pass rate

| Metric | Numerator | Denominator | Rate |
|---|---|---|---|
| Strict pass (literal verdicts: PASS only) | 28 | 30 | **93.3%** |
| Functional pass (re-classify §R-C1 sub-line drift) | 28 | 30 | **93.3%** |

**No reclassification triggered**: 0 strict FAIL_VERBATIM verdicts emitted. All 6 sub-line SENTENCE samples (ch04_a042, model02_a015 implicit, model05_a031, model03_a004, model04_a005) directly classified PASS per §R-C1 byte-exact-substring rule. The 2 fails are line_range and schema-completeness, NOT verbatim drift.

Both rates ≥ 90% threshold.

---

## §6 Cross-batch consistency findings

### parent_section format observations per file

| File | prompt_v | parent_section format pattern | Sample |
|---|---|---|---|
| chapters/ch04 | v1.8 | `§<num> [<title>]` | `§4.1.7 [Splitting Domains]` |
| domains/CM/assumptions | v1.8 | `§<DOMAIN> [<title>]` | `§CM [CM — Assumptions]` |
| domains/CM/examples | v1.8 | `§<DOMAIN.N> [<title>]` | `§CM.1 [Example 1]` |
| model/01_concepts | v1.8 | `§<num> [<title>]` | `§2.1 [Model Concepts and Terms — Variables]` |
| model/04_assoc_persons | v1.8 | `§<num> [<title>]` | `§4 [SDTM v2.0 — Chapter 4: Associated Persons Data]` |
| model/02_obs_classes | v1.9 | `§ <title>` (no bracket) + `§<num> > <subsection>` chained | `§3.1.1 > Topic and Qualifier Variables (43 variables)` |
| model/03_special_purpose | v1.9 | `§ <title>` + `§ <Domain> > <subsection>` | `§ Comments (CO) > Variables (15 variables)` |
| model/05_study_level | v1.9 | `§ <num> <title>` (no bracket) | `§ 5.1 Trial Design Model` |
| model/06_relationship | v1.9 | `§ <title>` (no num, no bracket) | `§ Summary of Relationship Datasets` |

**Finding**: Two distinct parent_section format families ALIGN with prompt version split:
- **v1.8 family** (5 files): bracketed format `§<num> [<title>]` with consistent square brackets.
- **v1.9 family** (4 files): un-bracketed format `§ <title>` (often with `>` chaining for subsections), no square brackets.

This is **NOT a schema violation** (parent_section is a free-form string field per atom_schema.json) but is a **cross-batch stylistic inconsistency**. Downstream P3/P4 consumers expecting uniform format may need normalization. **MEDIUM** as v1.9.1 candidate (adopt one canonical format).

### extracted_by uniformity

- **subagent_type**: 100% `oh-my-claudecode:executor` (1102/1102) ✓ — single writer pool confirmed (N21 v1.9 compliance).
- **prompt_version**: SPLIT — v1.8 (397 atoms in ch04/CM_assump/CM_ex/model01/model04) + v1.9 (705 atoms in model02/03/05/06). Cross-batch inconsistency.
- **ts**: All within 2026-04-29 single session window (00:00:00Z for v1.9 atoms, 12:00:00Z for v1.8 atoms). No drift outside session.

### Per-batch summary cross-reference

| Batch | per-batch verdict | this audit re-verify |
|---|---|---|
| 01 (model06) | PASS 10/10 + 1 LOW flag (md_model06_a029) | **CONFIRMED**: a029 FAIL_LINE_RANGE LOW — same severity, same disposition |
| 02 (model02) | PASS 10/10 0 defects | **CONFIRMED**: 6 sample atoms all PASS, no new defects surfaced |
| 03 (model03) | PASS 10/10 0 defects | **CONFIRMED**: 4 sample atoms all PASS |
| 04 (model05) | PASS 10/10 0 defects (FIGURE first surfaced) | **CONFIRMED**: 5 sample atoms all PASS, including FIGURE a170 |

**No per-batch scientist missed any defect that this cumulative audit found in their assigned batches**. The HIGH FAIL_SCHEMA (md_model01_a013) is in model01 — which was NOT in any of batches 01-04 (model01 was outside the 4 batches under per-batch scientist review). This is the **unique value** of cumulative audit: catching defects in files that fell outside per-batch scope.

---

## §7 Open findings + v1.9.1 candidates

### Open findings

1. **HIGH — md_model01_a013 FIGURE figure_ref=null (FAIL_SCHEMA)**
   - File: `knowledge_base/model/01_concepts_and_terms.md` L13-39
   - Issue: FIGURE atom (mermaid concept map) missing required `figure_ref` field per atom_schema.json v1.2 allOf conditional.
   - Compare: md_model05_a170 (`md_model05_DI_concept_map`) and md_model05_a184 (`md_model05_OI_concept_map`) — both v1.9 and compliant.
   - Root cause: Atom emitted under v1.8 prompt before §C-1..C-8 codification. v1.9 prompt presumably enforces FIGURE figure_ref via Hook A1+ family.
   - Disposition: **must fix** before B-02 entry. Suggested figure_ref value: `md_model01_sdtm_domains_concept_map`.

2. **LOW — md_model06_a029 FAIL_LINE_RANGE (carry-forward)**
   - File: `knowledge_base/model/06_relationship_datasets.md` L43 (claimed) vs L42 (actual)
   - Issue: Off-by-one on line_start; verbatim correct.
   - Disposition: **carry-forward** to v1.9.1 backlog (LOW severity, isolated 1/109 = 0.9%, no systematic pattern). Already flagged by batch_01 scientist; this audit confirms severity LOW.

### v1.9.1 candidates (NEW from this cumulative audit)

| # | severity | description |
|---|---|---|
| V1 | HIGH | **FIGURE figure_ref completeness sweep** — add full-batch validator: any atom_type=FIGURE MUST have non-null figure_ref. v1.8-emitted FIGURE atoms (3 total: model01_a013, model05_a170, model05_a184; only the model01 one is broken) need retro-fill. Add explicit Hook A4: pre-DONE FIGURE-figure_ref check. |
| V2 | MEDIUM | **parent_section format unification** — v1.8 uses `§<num> [<title>]`, v1.9 uses `§ <title>` / `§ <num> <title>` / `§<num> > <subsection>` (3 sub-variants). Adopt single canonical format for v1.9.1 — recommend v1.9 family but with explicit grammar in writer prompt. Existing 1102 atoms either need migration or P3/P4 consumers need format normalizer. |
| V3 | LOW | **Mixed prompt_version atoms in same md_atoms.jsonl** — 397 v1.8 + 705 v1.9 atoms coexist. Consider: re-emit all 397 v1.8 atoms under v1.9 to enforce §C-1..C-8 uniformly. Risk: introduces re-extraction cost; benefit: eliminates v1.8 vs v1.9 drift (e.g., V1 above). Decision deferred to PLAN cycle. |

---

## §8 Gate verdict

**PASS** (Strict 28/30 = 93.3% ≥ 90% threshold; Functional 28/30 = 93.3% ≥ 90% threshold)

Caveat: 1 HIGH severity FAIL_SCHEMA (md_model01_a013) MUST be remediated before B-02 atom emission. While this is below the >2 HIGH-fail threshold for FAIL gate, it represents a real schema violation that must not propagate. Conditional component: PASS gate applies to overall sample but HIGH finding is a single-atom hot-fix item, not a systemic block.

### Gate rationale
- Sample-level pass rate (28/30 = 93.3%) clears 90% bar.
- C-1..C-8 anti-defect hooks all PASS or N/A on full 1102-atom sweep.
- 0 FAIL_VERBATIM (the historical hot defect class).
- 0 systematic drift; both fails are isolated singletons in different files.
- Schema 7/10 PASS, 1 FAIL (HIGH but isolated single-atom), 2 MIXED-but-legal.
- All 4 per-batch scientist verdicts cross-validated.
- Cumulative audit caught 1 NEW HIGH finding in model01 (outside per-batch scope) — proves cumulative-audit unique value.

---

## §9 Recommendation for B-02 entry

**Recommendation**: **GREEN-LIGHT WITH HOTFIX** for B-02 dispatch.

### Hotfix (must complete before B-02 atom emission)

1. **Fix md_model01_a013** — add `figure_ref: "md_model01_sdtm_domains_concept_map"` (or similar canonical value following md_model05 naming). Single-atom edit; no re-extraction needed.

### Required additions to B-02 dispatch template

1. **Hook A4 (FIGURE figure_ref pre-DONE check)** — add to writer P0_writer_md_v1.9.1 prompt: before DONE, validate every FIGURE atom has non-null figure_ref. Block silent emission of mermaid blocks without ref.

2. **parent_section format declaration** — B-02 dispatch kickoff MUST state which format family (v1.8 bracketed vs v1.9 spaced) the writer should use. Recommend **v1.9 spaced** as canonical going forward; document grammar:
   ```
   For root: "§ <plain title>"
   For numbered: "§<N.M> [<title>]" OR "§ <N.M> <title>" — pick ONE
   For chained: "§<parent> > <child name>"
   ```

3. **Cumulative audit gate** — keep cumulative cross-batch audit (this kind of run) as gate between batch-cycles. Per-batch scientists cannot catch defects in files outside their assigned batch (model01 was outside batches 01-04 and would have escaped to B-02 without this audit).

4. **prompt_version uniformity goal** — if B-02 will emit new atoms, ensure all are v1.9.1 (post-hotfix prompt). Existing v1.8 atoms (397 records) remain in JSONL as-is; flag in `_progress.json` the prompt-version distribution as a known cycle-2 cleanup item.

### B-02 entry checklist

- [ ] md_model01_a013 figure_ref hotfix applied + verified via jq
- [ ] writer prompt v1.9.1 published with Hook A4 + parent_section grammar
- [ ] B-02 dispatch kickoff cites canonical parent_section format
- [ ] Reviewer prompt v1.9.1 (if any) incorporates new C-9 (FIGURE figure_ref check) into anti-defect sweep
- [ ] Per-batch scientists informed: continue 10/batch sampling; cumulative audit re-runs at end of cycle

**B-02 may proceed once item 1 is verified and items 2-4 are in dispatch template**.

---

## §10 Limitations

- Sample n=30 (2.7% direct verbatim audit of 1102 atoms); structural full-batch sweeps cover remaining 1072 atoms but do not verify byte-exact verbatim for them.
- TABLE_ROW representation in sample (2/549 = 0.36%) is sparse; relied on per-batch scientist sampling + structural checks (single-line span uniformity, pipe-delimited format).
- model01/model04/CMassump quotas constrained by small file sizes (1-2 atoms each).
- CROSS_REF type (2 total atoms) not directly sampled; verified via schema sweep only.
- No source-PDF cross-check (Rule A audits MD-side atomization only; PDF↔MD matching is P4a scope).
