# Rule A Audit Summary — P2 B-03 batch_89

> 状态: **PASS** (2026-05-06)
> Reviewer subagent_type: `pr-review-toolkit:code-reviewer`
> Prompt baseline: `P0_reviewer_v1.9.2`

## Audit scope

- **Source**: `knowledge_base/domains/PR/examples.md` (58 lines, 3 numbered H2 §PR.1/.2/.3, 0 H3, 0 mermaid, 5 tables)
- **Atoms file**: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_89_md_atoms.jsonl` (34 atoms)
- **Mode**: 8 boundary + 3 stratified = 11 atom audit (≥30 atoms threshold per round 08 kickoff §5)
- **Atoms layout**: 4 HEADING (a001 H1 + a002/a011/a028 H2) + 11 SENTENCE + 5 TABLE_HEADER + 14 TABLE_ROW = 34

## Per-atom verdicts (11 audited)

| Atom | Line | Type | Role | Verdict |
|------|------|------|------|---------|
| md_dmPR_ex_a001 | L1 | HEADING | 1st atom, H1 root | **PASS** |
| md_dmPR_ex_a002 | L3 | HEADING | H2 boundary 1/3 | **PASS** |
| md_dmPR_ex_a003 | L5 | SENTENCE | First child of H2 a002 | **PASS** |
| md_dmPR_ex_a004 | L7 | SENTENCE | Bold-caption stratified | **PASS** |
| md_dmPR_ex_a005 | L9-L10 | TABLE_HEADER | Stratified | **PASS** |
| md_dmPR_ex_a006 | L11 | TABLE_ROW | Stratified | **PASS** |
| md_dmPR_ex_a011 | L17 | HEADING | H2 boundary 2/3 | **PASS** |
| md_dmPR_ex_a012 | L19 | SENTENCE | First child of H2 a011 | **PASS** |
| md_dmPR_ex_a028 | L48 | HEADING | H2 boundary 3/3 | **PASS** |
| md_dmPR_ex_a029 | L50 | SENTENCE | First child of H2 a028 | **PASS** |
| md_dmPR_ex_a034 | L58 | TABLE_ROW | Last atom | **PASS** |

**Pass rate: 11/11 audited = 100% (≥90% gate ✓)**

## Findings

- **HIGH**: 0
- **MED**: 0
- **LOW**: 0

No findings.

## v1.9.2 paired-sync hook results

### §R-E1 PRIORITY 1 schema regression sweep — **PASS (0 regression across all 34 atoms)**

Verified across all 34 atoms via Python schema sweep:
- Field name `verbatim` (NOT `verbatim_text`) — ✓ all 34 (grep `"verbatim_text"` count = 0)
- Field `line_start` / `line_end` present as int — ✓ all 34
- Field `figure_ref` present (null value) — ✓ all 34 (grep `"figure_ref":null` count = 34)
- `atom_type` ∈ canonical 9 enum {HEADING, LIST_ITEM, SENTENCE, TABLE_HEADER, TABLE_ROW, FIGURE, NOTE, CODE_LITERAL, CROSS_REF} — ✓ all 34 (4 HEADING + 11 SENTENCE + 5 TABLE_HEADER + 14 TABLE_ROW; no "H1"/"List"/etc bad values)
- 12-key exact set {atom_id, file, line_start, line_end, parent_section, atom_type, verbatim, heading_level, sibling_index, figure_ref, cross_refs, extracted_by} — ✓ all 34 (no extra, no missing)

### §R-E2 — R-2.8-1 H1 hl/sib — **PASS**

a001: heading_level=1, sibling_index=1 ✓ (H1 root universal).

### §R-E3 — R-2.8-2 TABLE_HEADER — **PASS (5/5)**

All 5 TABLE_HEADER atoms (a005 L9-L10, a015 L25-L26, a019 L33-L34, a025 L43-L44, a031 L54-L55) carry:
- `sibling_index=null` ✓
- `line_end - line_start = 1` (2-line span: header row + separator row) ✓
- `verbatim` newline-joined byte-exact with source ✓ (verified on a005 stratified sample)

### §R-E4 — R-2.8-3 extracted_by codification — **PASS**

All 34 atoms carry `extracted_by` object form with `subagent_type: "general-purpose"`, `prompt_version: "P0_writer_md_v1.9.2"`, `ts: "2026-05-06T14:14:35Z"` ✓ (NOT string; grep `"prompt_version":"P0_writer_md_v1.9.2"` count = 34).

### §R-E5 — MED-01 non-HEADING explicit-null — **PASS**

30 non-HEADING atoms (34 total - 4 HEADING) all carry `"heading_level":null,"sibling_index":null` as explicit JSON literal byte-strings.
- Grep `"heading_level":null,"sibling_index":null` count = **30** ✓ (matches 30 non-HEADING expectation exactly).

### §R-E6 — FIGURE/CODE_LITERAL boundary — **N/A**

0 mermaid blocks, 0 fenced code blocks in this file (kickoff §0.5 row confirmed).

## Round 08 §2.5 numbered H2 self-namespace lock validation — **PASS (3/3 cases)**

Plan B sub-namespace first production validation post-cut. All 3 H2 cases verified:

| Case | H2 Atom | H2 Line | H2 parent | H2 sib | Children Range | Children parent |
|------|---------|---------|-----------|--------|----------------|-----------------|
| 1 | a002 (`## Example 1`) | L3 | `§PR [PR — Examples]` ✓ | 1 ✓ | L5-L15 (a003-a010, 8 atoms) | `§PR.1 [Example 1]` ✓ |
| 2 | a011 (`## Example 2`) | L17 | `§PR [PR — Examples]` ✓ | 2 ✓ | L19-L46 (a012-a027, 16 atoms) | `§PR.2 [Example 2]` ✓ |
| 3 | a028 (`## Example 3`) | L48 | `§PR [PR — Examples]` ✓ | 3 ✓ | L50-L58 (a029-a034, 6 atoms) | `§PR.3 [Example 3]` ✓ |

**Tally**: 30 sub-namespace child atoms (parent matches `§PR\.[123] \[`) + 4 root-parent atoms (a001 H1 + 3 H2 atoms with parent `§PR [PR — Examples]`) = 34 ✓.

H2 transitions clean: writer correctly switches parent_section namespace immediately after each H2 boundary atom; no leakage of children to root parent or wrong sub-namespace.

## §D-5 bold-caption SENTENCE retention — **PASS (5/5)**

Source has 5 bold-caption lines (`^\*\*[a-z]+\.xpt\*\*$` regex, kickoff said ~7 — actual count 5):
- L7 `**pr.xpt**` → a004 SENTENCE ✓
- L23 `**pr.xpt**` → a014 SENTENCE ✓
- L31 `**eg.xpt**` → a018 SENTENCE ✓
- L41 `**relrec.xpt**` → a024 SENTENCE ✓
- L52 `**pr.xpt**` → a030 SENTENCE ✓

0 NOTE misclassifications. §D-5 retention rule fully honored.

## cross_refs canonical shape — **PASS (2/2)**

2 atoms carry cross_refs entries (both reference identical Section 4.2.4):
- a003 L5: `[{"section":"Section 4.2.4","title":"Text Case in Submitted Data"}]` ✓
- a029 L50: `[{"section":"Section 4.2.4","title":"Text Case in Submitted Data"}]` ✓

Both match batch_88 a004 precedent canonical shape `{section, title}` exactly.

## Per-atom byte-exact verbatim check (11 audited)

All 11 audited atoms verbatim joined byte-exact with source `[line_start, line_end]` slice (verified by Python source-slice + JSON-decoded-verbatim equality):

- a001 L1 (H1 single-line): ✓
- a002 L3 (H2 single-line): ✓
- a003 L5 (long SENTENCE with cross_ref): ✓
- a004 L7 (bold-caption SENTENCE): ✓
- a005 L9-L10 (TABLE_HEADER 2-line newline-join): ✓
- a006 L11 (TABLE_ROW): ✓
- a011 L17 (H2): ✓
- a012 L19 (SENTENCE): ✓
- a028 L48 (H2): ✓
- a029 L50 (long SENTENCE with cross_ref): ✓
- a034 L58 (last TABLE_ROW): ✓

## Other checks

- **file prefix**: All 34 atoms start with `knowledge_base/` ✓ (grep count = 34)
- **figure_ref**: All 34 atoms = null ✓
- **12-field schema**: All 34 atoms carry full set ✓
- **line_start/line_end int type**: All 34 atoms int ✓
- **canonical atom_type**: All 34 ∈ enum-9 ✓
- **No NOTE atoms**: 0 NOTE in batch (consistent with §D-5 bold-caption retention as SENTENCE)

## Gate decision

**PASS** — orchestrator may append batch_89 atoms to root `md_atoms.jsonl` and proceed to batch_90.

- ≥90% atoms PASS gate: 11/11 = 100% ✓
- 0 §R-E1 PRIORITY 1 regression ✓
- 0 HIGH severity finding ✓
- §2.5 numbered H2 sub-namespace lock validation: 3/3 cases PASS ✓ (Plan B first production validation post-cut SUCCESS)
