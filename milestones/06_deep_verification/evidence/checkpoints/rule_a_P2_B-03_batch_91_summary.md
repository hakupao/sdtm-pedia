# Rule A Audit Summary — P2 B-03 batch_91

> 状态: **PASS** (2026-05-06)
> Reviewer subagent_type: `pr-review-toolkit:code-reviewer`
> Prompt baseline: `P0_reviewer_v1.9.2`

## Audit scope

- **Source**: `knowledge_base/domains/QS/examples.md` (24 lines, 1 numbered H2 §QS.1, 0 H3, 0 mermaid, 1 table)
- **Atoms file**: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_91_md_atoms.jsonl`
- **Mode**: Full audit (17/17 atoms — <30 atoms threshold per round 08 kickoff §5)
- **Atoms layout**: 1 H1 (a001) + 1 H2 (a003) + 4 SENTENCE (a002, a004, a005, a006) + 1 TABLE_HEADER (a007) + 10 TABLE_ROW (a008-a017)

## Per-atom verdicts

| Atom | Line | Type | Verdict |
|------|------|------|---------|
| md_dmQS_ex_a001 | L1 | HEADING | **PASS** |
| md_dmQS_ex_a002 | L3 | SENTENCE | **PASS** |
| md_dmQS_ex_a003 | L5 | HEADING | **PASS** |
| md_dmQS_ex_a004 | L7 | SENTENCE | **PASS** |
| md_dmQS_ex_a005 | L9 | SENTENCE | **PASS** |
| md_dmQS_ex_a006 | L11 | SENTENCE | **PASS** |
| md_dmQS_ex_a007 | L13-14 | TABLE_HEADER | **PASS** |
| md_dmQS_ex_a008 | L15 | TABLE_ROW | **PASS** |
| md_dmQS_ex_a009 | L16 | TABLE_ROW | **PASS** |
| md_dmQS_ex_a010 | L17 | TABLE_ROW | **PASS** |
| md_dmQS_ex_a011 | L18 | TABLE_ROW | **PASS** |
| md_dmQS_ex_a012 | L19 | TABLE_ROW | **PASS** |
| md_dmQS_ex_a013 | L20 | TABLE_ROW | **PASS** |
| md_dmQS_ex_a014 | L21 | TABLE_ROW | **PASS** |
| md_dmQS_ex_a015 | L22 | TABLE_ROW | **PASS** |
| md_dmQS_ex_a016 | L23 | TABLE_ROW | **PASS** |
| md_dmQS_ex_a017 | L24 | TABLE_ROW | **PASS** |

**Pass rate: 17/17 = 100%**

## Findings

- **HIGH**: 0
- **MED**: 0
- **LOW**: 0

No findings.

## v1.9.2 paired-sync hook results

### §R-E1 PRIORITY 1 schema regression sweep — **PASS (0 regression)**

Explicitly verified across all 17 atoms:
- Field name `verbatim` (NOT `verbatim_text`) — ✓ all 17
- Field `line_start` present as int — ✓ all 17
- Field `line_end` present as int — ✓ all 17
- Field `figure_ref` present (null value) — ✓ all 17
- `atom_type` value ∈ canonical 9 enum {HEADING, LIST_ITEM, SENTENCE, TABLE_HEADER, TABLE_ROW, FIGURE, NOTE, CODE_LITERAL, CROSS_REF} — ✓ all 17 (2 HEADING + 4 SENTENCE + 1 TABLE_HEADER + 10 TABLE_ROW; no "H1"/"H2"/"Header"/etc bad values)
- 12-key exact set {atom_id, file, line_start, line_end, parent_section, atom_type, verbatim, heading_level, sibling_index, figure_ref, cross_refs, extracted_by} — ✓ all 17 (no extra, no missing)

### §R-E2 — R-2.8-1 H1/H2 hl/sib — **PASS**

- a001 (H1): heading_level=1, sibling_index=1 ✓ (H1 root universal)
- a003 (H2 numbered §QS.1): heading_level=2, sibling_index=1 ✓ (only H2 in file)

### §R-E3 — R-2.8-2 TABLE_HEADER — **PASS**

a007: line_start=13, line_end=14, line_end-line_start=1 ✓ (2-row span: header row + separator row joined by `\n`).
a007: heading_level=null, sibling_index=null ✓.

### §R-E4 — R-2.8-3 extracted_by codification — **PASS**

All 17 atoms carry `extracted_by` object form with `subagent_type: "general-purpose"`, `prompt_version: "P0_writer_md_v1.9.2"`, `ts: "2026-05-06T00:00:00Z"` ✓ (NOT string).

### §R-E5 — MED-01 non-HEADING explicit-null — **PASS**

15 non-HEADING atoms (a002, a004-a017) all carry `"heading_level":null,"sibling_index":null` as explicit JSON literal byte-strings (verified by raw line inspection, not omitted from object).

### §R-E6 — FIGURE/CODE_LITERAL boundary — **N/A**

0 mermaid blocks, 0 fenced code blocks in this file.

## Round 08 §2.5 numbered H2 self-namespace lock VALIDATE — **PASS**

QS/examples.md is the **first production validation** of §2.5 numbered H2 sub-namespace lock (Plan B). Three-tier verification:

| Tier | Atom range | Expected parent_section | Actual | Result |
|------|-----------|-------------------------|--------|--------|
| Pre-H2 (file-root) | a002 (L3) | `§QS [QS — Examples]` | `§QS [QS — Examples]` | ✓ PASS |
| H2 atom itself | a003 (L5, the H2) | `§QS [QS — Examples]` (parent=file-root, NOT self) | `§QS [QS — Examples]` | ✓ PASS |
| Post-H2 children | a004-a017 (L7-24) | `§QS.1 [Example 1]` | `§QS.1 [Example 1]` (all 14) | ✓ PASS |

**§2.5 lock validation: PASS** — Plan B sub-namespace correctly applied; H2 atom does NOT self-reference, all subsequent SENTENCE/TABLE_HEADER/TABLE_ROW children correctly nest under §QS.1.

## §D-5 bold-caption SENTENCE retention — **PASS**

Round 07/08 §D-5 hook (bold-only short lines kept as SENTENCE, not promoted to NOTE):

| Atom | Line | Verbatim | atom_type | Result |
|------|------|----------|-----------|--------|
| a004 | L7 | `**Satisfaction With Life Scale (SWLS)**` | SENTENCE | ✓ (NOT NOTE) |
| a006 | L11 | `**qs.xpt**` | SENTENCE | ✓ (NOT NOTE) |

Both bold-caption lines correctly retained as SENTENCE per §D-5.

## Per-atom byte-exact verbatim check

All 17 atoms verbatim joined byte-exact with source `[line_start, line_end]` slice:

- a001 L1 `# QS — Examples`: ✓
- a002 L3 (CDISC publishes... single-line sentence with embedded URL): ✓
- a003 L5 `## Example 1`: ✓
- a004 L7 `**Satisfaction With Life Scale (SWLS)**`: ✓
- a005 L9 `The example represents the items from the SWLS instrument.`: ✓
- a006 L11 `**qs.xpt**`: ✓
- a007 L13-14 (header row + separator joined by `\n`): ✓ multi-line newline-join byte-exact
- a008 L15 (Row 1, USUBJID CDISC01.100008, SWLS0101): ✓
- a009 L16 (Row 2, SWLS0102): ✓
- a010 L17 (Row 3, SWLS0103): ✓
- a011 L18 (Row 4, SWLS0104): ✓
- a012 L19 (Row 5, SWLS0105): ✓
- a013 L20 (Row 6, USUBJID CDISC01.100014, SWLS0101): ✓
- a014 L21 (Row 7, SWLS0102): ✓
- a015 L22 (Row 8, SWLS0103): ✓
- a016 L23 (Row 9, SWLS0104): ✓
- a017 L24 (Row 10, SWLS0105): ✓

## Other checks

- **file prefix**: All 17 atoms start with `knowledge_base/` ✓
- **figure_ref**: All 17 atoms = null ✓ (no figures in source)
- **cross_refs**: All 17 atoms = `[]` ✓ (a002 contains a bare URL `https://www.cdisc.org/standards/foundational/qrs` per round 06 batch_70 ML/assn precedent — bare URL not requiring cross_ref entry; no `(see Section X)` patterns triggered)
- **atom_id monotonic**: a001..a017 sequential, no gaps ✓
- **12-field schema**: All 17 atoms carry full set ✓

## Gate decision

**PASS** — orchestrator may append batch_91 atoms to root `md_atoms.jsonl` and proceed to batch_92.

- ≥90% atoms PASS gate: 17/17 = 100% ✓
- 0 §R-E1 PRIORITY 1 regression ✓
- 0 HIGH severity finding ✓
- §2.5 numbered H2 sub-namespace lock validation: PASS ✓ (first production validation)
- §D-5 bold-caption SENTENCE retention: PASS ✓
