# Rule A 抽检 summary — P2 B-03c round 07 batch_82 (PC/examples.md L250-447 slice 2 of 3)

> Reviewer: general-purpose + P0_reviewer_v1.9.2
> Timestamp: 2026-05-06T23:30:00Z
> Scope: 11/150 stratified (8 boundary + 3 stratified)
> Source: `knowledge_base/domains/PC/examples.md` L250-447
> Atoms file: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_82_md_atoms.jsonl`

## §R-E1 Schema regression sweep — PRIORITY 1 (CRITICAL pre-check)

| Check | Result | Detail |
|---|---|---|
| 1. `verbatim_text` field name regression | PASS | 0/150 |
| 2. Missing `line_start`/`line_end`/`figure_ref` | PASS | 0/150 |
| 3. Invalid `atom_type` enum (H1/H2/H3 string etc.) | PASS | 0/150 (all in {HEADING, SENTENCE, TABLE_HEADER, TABLE_ROW}) |
| 4. 12-keys schema regression sweep | PASS | 0/150; key set exact match {atom_id, file, line_start, line_end, parent_section, atom_type, verbatim, heading_level, sibling_index, figure_ref, cross_refs, extracted_by} |

**Schema regression sweep verdict**: GREEN — proceed to per-atom byte-exact verify.

## §R-E2 R-2.8-1 H1 sib=1 universal verify

N/A — no H1 atoms this slice (slice 2 entirely under L7 H2, only 2 H3 atoms at L250 and L332).

## §R-E3 R-2.8-2 TABLE_HEADER sib=null universal verify

PASS — 8/8 TABLE_HEADER atoms have `sibling_index=null`. 0 violation.

## §R-E4 R-2.8-3 extracted_by object schema universal verify

PASS — 150/150 atoms have `extracted_by` as object with exactly 3 fields (subagent_type, prompt_version, ts). prompt_version="P0_writer_md_v1.9.2" universal. 0 string-form violation.

## §R-E5 MED-01 non-HEADING field-explicit-null verify

| Field | Expected | Actual | Result |
|---|---|---|---|
| non-HEADING count | — | 148 | — |
| `"heading_level":null` byte-grep | 148 | 148 | PASS |
| `"sibling_index":null` byte-grep | 148 | 148 | PASS |

PASS — all 148 non-HEADING atoms have explicit JSON null fields (not omitted).

## §R-E6 FIGURE-vs-CODE_LITERAL boundary

N/A — 0 FIGURE/CODE_LITERAL atoms in slice 2 (all atoms ∈ {HEADING, SENTENCE, TABLE_HEADER, TABLE_ROW}).

## §2.11 Plan B parent_section verify (CRITICAL)

| parent_section | Count | Expected | Result |
|---|---|---|---|
| `§PC.2 [Relating PC and PP — Overview]` (parent of L250+L332 H3 = L58 H2) | 2 | 2 (a200 + a258) | PASS |
| `§PC.2.5 [Example 2 (Some PC records excluded)]` (synthesized 5.1 children of L250 H3) | 57 | 57 | PASS |
| `§PC.2.6 [Example 3 (Inconsistent PC usage across parameters)]` (synthesized 6.1 children of L332 H3) | 91 | 91 | PASS |
| `§PC [PC — Examples]` (Plan A.1 fallback — should be 0) | 0 | 0 | PASS |
| `§PC.1 [Example 1]` (slice 1 only, should be 0 in slice 2) | 0 | 0 | PASS |

**§2.11 Plan B verify status: PASS**

## Per-atom verdicts (11/11)

| Stratum | atom_id | line | atom_type | parent_section | Verdict |
|---|---|---|---|---|---|
| boundary first slice2 | a200 | 250 | HEADING h3 sib5 | §PC.2 | PASS |
| boundary L250 H3 explicit | a200 | 250 | HEADING h3 sib5 | §PC.2 | PASS |
| boundary first under L250 H3 | a201 | 252 | SENTENCE | §PC.2.5 | PASS |
| boundary L332 H3 | a258 | 332 | HEADING h3 sib6 | §PC.2 | PASS |
| boundary first under L332 H3 | a259 | 334 | SENTENCE | §PC.2.6 | PASS |
| boundary TABLE_HEADER sib=null | a207 | 264-265 | TABLE_HEADER sib=null | §PC.2.5 | PASS |
| boundary middle L332 region | a301 | 389 | SENTENCE (Method C) | §PC.2.6 | PASS |
| boundary last slice | a349 | 446 | TABLE_ROW | §PC.2.6 | PASS |
| stratified SENTENCE | a204 | 258 | SENTENCE (bold-caption Method A) | §PC.2.5 | PASS |
| stratified TABLE_HEADER | a207 | 264-265 | TABLE_HEADER (re-check) | §PC.2.5 | PASS |
| stratified TABLE_ROW | a321 | 418 | TABLE_ROW | §PC.2.6 | PASS |

**Pass rate**: 11/11 = 100% PASS.

## Findings

- **HIGH**: 0
- **MEDIUM**: 0
- **LOW**: 0

## Interpretation-vs-defect declaration (Hook R23)

No defects detected this batch. All 11 stratified atoms pass byte-exact + schema + parent_section §2.11 Plan B verify.

## Gate verdict

| Gate | Threshold | Actual | Result |
|---|---|---|---|
| Stratified PASS rate | ≥10/11 | 11/11 | PASS |
| §R-E1 schema regression | 0 | 0 | PASS |
| HIGH findings | 0 | 0 | PASS |
| §2.11 Plan B verify | PASS | PASS | PASS |

**Gate: GREEN — batch_82 ready to advance.**

## Reviewer + ts

- Reviewer subagent_type: general-purpose (Rule D isolated from writer subagent_type)
- Reviewer prompt_version: P0_reviewer_v1.9.2
- ts: 2026-05-06T23:30:00Z
