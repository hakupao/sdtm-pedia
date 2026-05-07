# Rule A Audit — P2 B-03c Round 11 batch_116 SUPPQUAL/assumptions.md

> Reviewer: `pr-review-toolkit:code-reviewer` (Rule D PASS — writer = `general-purpose`)
> Prompt version: `P0_reviewer_v1.9.3.md` (35 hooks)
> Audit date: 2026-05-07
> Verdict: **PASS**

## Inputs

- Source: `knowledge_base/domains/SUPPQUAL/assumptions.md` (26 lines, 15 non-blank)
- Atoms: `evidence/checkpoints/P2_B-03_batch_116_md_atoms.jsonl` (15 atoms a001..a015)
- Writer: `general-purpose` (peer-alternative pool, B-02 + round 01-10 sustained streak)

## Atom-type breakdown

| atom_type | count |
|---|---|
| HEADING | 3 (1 H1 L1 + 2 H2 L15+L19) |
| SENTENCE | 8 (L3, L5, L7, L9, L11, L13, L17, L21) |
| LIST_ITEM | 4 (L23, L24, L25, L26) |
| **Total** | **15** |

## Hook-by-hook results (35 reviewer hooks)

### CRITICAL — Hook A1 byte-exact verbatim (15/15 single-line atoms)

PASS — every `verbatim` field is byte-exact equal to the corresponding source line. 0 multi-line atoms in this batch.

### CRITICAL — §R-E1 schema regression sweep (PRIORITY 1)

PASS — all 15 atoms carry the canonical 12-field schema in exact order:
`atom_id, file, line_start, line_end, parent_section, atom_type, verbatim, heading_level, sibling_index, figure_ref, cross_refs, extracted_by`. 0 missing field, 0 extra field, 0 reorder.

### HIGH — §R-E2 H1 sib_idx=1 universal

PASS — a001 H1 hl=1 sib=1 (1/1).

### HIGH — §R-E3 TABLE_HEADER sib_idx=null

N/A — 0 TABLE_HEADER atoms in this batch.

### HIGH — §R-E4 extracted_by object schema

PASS — all 15 atoms `extracted_by` is object with `subagent_type=general-purpose`, `prompt_version=P0_writer_md_v1.9.3`, `ts=2026-05-07T12:30:00Z`.

### HIGH — §R-F-1 §2.11 Plan B sub-namespace 4-layer verify

N/A trigger PASS — 0 H3 atoms in source (kickoff §0.5 row 21 grep verified) → §F-1 trigger condition (numberless H2 with H3 children) does NOT fire. §2.7 round 04 lock applies instead (numberless H2 childless → file-root parent inherit, see below).

### HIGH — §2.7 round 04 lock 2 cases verify (numberless childless H2 → file-root parent inherit)

PASS — both H2 atoms and all their descendants resolve to file-root `§SUPPQUAL [SUPPQUAL — Assumptions]`:

| H2 | line | sib | parent_section | children resolved file-root |
|---|---|---|---|---|
| `## Submitting Supplemental Qualifiers in Separate Datasets` (a008) | L15 | 1 | `§SUPPQUAL [SUPPQUAL — Assumptions]` | a009 (L17 SENTENCE) → file-root ✓ |
| `## When Not to Use Supplemental Qualifiers` (a010) | L19 | 2 | `§SUPPQUAL [SUPPQUAL — Assumptions]` | a011 (L21 SENTENCE) + a012-a015 (L23-L26 LIST_ITEM) → all file-root ✓ |

All 6 children inherit file-root parent (NOT `§SUPPQUAL.1` or `§SUPPQUAL.2` sub-namespace) per §2.7 round 04 lock. 0 atoms carry sub-namespace parent. Cumulative §2.7 lock cases post round 11 batch_116: 4 (FT/ass round 04 + PP/ex L106 round 08 + QS/ass L5 round 08 + SUPPQUAL/ass L15 + L19 round 11 = 5 H2 cases).

### MED — §R-E5 non-HEADING field-explicit-null

PASS — all 12 non-HEADING atoms carry explicit `"heading_level": null, "sibling_index": null` (NOT omitted). 0 violation.

### LOW — §R-E6 FIGURE-vs-CODE_LITERAL boundary

N/A — 0 FIGURE/CODE_LITERAL atoms in this batch.

### INFO — §R-F-2 atoms/line ratio retrospective

INFO carry-forward — ratio = 15/26 = **0.5769**, just **0.0131 below** the 0.59 lower band. Carry-forward as **C-R11-02 candidate** (small assumptions.md narrative-paragraph compression + 2 numberless H2 + 4 LIST_ITEM compression). Round 10 had similar lower-edge ratio 0.591 (RELSPEC..SS); v1.9.3 §F-2 INFO non-blocking per definition. Round 11 round-close mini-audit will aggregate cumulative round ratio.

### INFO — §R-F-3 kickoff atom estimate calibration

PASS — kickoff §0.5 row 23 + §1 estimate 10-14 (mid 12); actual 15. Delta = |15-12|/12 = **25.0%**, well within ±50% threshold. No INFO finding triggered.

### CRITICAL — atom_id uniqueness + sequential

PASS — 15/15 unique; sequential a001..a015 with prefix `md_dmSUPPQUAL_assn_`.

### HIGH — parent_section consistency

PASS — all 15 atoms carry `§SUPPQUAL [SUPPQUAL — Assumptions]` (file-root). 0 atoms carry sub-namespace. Verified above under §2.7 lock.

### HIGH — Rule D writer ≠ reviewer

PASS — writer = `general-purpose`, reviewer = `pr-review-toolkit:code-reviewer`. Distinct subagent_type, distinct family.

### Coverage check

PASS — 15/15 source non-blank lines covered. 0 uncovered non-blank line.

## Rule A semantic spot-check (15/15 — full census on small batch)

| atom_id | line | type | semantic | cross_refs |
|---|---|---|---|---|
| a001 | L1 | HEADING | PASS | none |
| a002 | L3 | SENTENCE | PASS | `Section 8.4.2` ✓ |
| a003 | L5 | SENTENCE | PASS | `Section 4.1.8` + `Appendix C1` ✓ |
| a004 | L7 | SENTENCE | PASS | none |
| a005 | L9 | SENTENCE | PASS | none |
| a006 | L11 | SENTENCE | PASS | none |
| a007 | L13 | SENTENCE | PASS | none |
| a008 | L15 | HEADING (H2 sib=1) | PASS | none |
| a009 | L17 | SENTENCE | PASS | `Section 4.1.7` ✓ |
| a010 | L19 | HEADING (H2 sib=2) | PASS | none |
| a011 | L21 | SENTENCE | PASS | none |
| a012 | L23 | LIST_ITEM | PASS | none |
| a013 | L24 | LIST_ITEM | PASS | `Section 4.5.5` ✓ |
| a014 | L25 | LIST_ITEM | PASS | none |
| a015 | L26 | LIST_ITEM | PASS | none |

**Rule A pass rate: 15/15 = 100%** (full-census on a 15-atom batch — exceeds 10-sample minimum).

## Findings

- **HIGH severity: 0**
- **MED severity: 0**
- **LOW severity: 0**
- **INFO carries: 1** (§R-F-2 ratio 0.5769 just below 0.59 lower band → C-R11-02 candidate to aggregate at round 11 round-close)

## Verdict

**PASS** — 35/35 hooks PASS; Rule A 15/15 = 100%; Hook A1 byte-exact 15/15; §R-E1 schema regression 0; §2.7 round 04 lock 2 cases verified (a008 L15 sib=1 + a010 L19 sib=2 file-root + 6 child atoms all file-root inherit, 0 sub-namespace); §R-F-1 §2.11 Plan B N/A trigger PASS; §R-F-2 INFO ratio carry-forward (non-blocking); §R-F-3 estimate delta 25% within ±50% threshold; atom_id uniqueness + sequential PASS; parent_section consistency PASS; Rule D writer≠reviewer PASS.
