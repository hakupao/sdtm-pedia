# Rule A Audit Summary — batch_95 RELREC/examples.md (§2.11 Plan B 2nd production validation)

> Round: P2 B-03c round 09 batch_95
> Baseline: v1.9.2 (3rd round post-cut)
> Reviewer: general-purpose subagent (Rule D isolation from writer)
> Date: 2026-05-07

## 1. Scope

- **Source**: `knowledge_base/domains/RELREC/examples.md` (66 lines)
- **Writer output**: `P2_B-03_batch_95_md_atoms.jsonl` (40 atoms)
- **Atoms total**: 40
- **Atoms audited**: 11 (8 boundary + 3 stratified)

## 2. Audit Sample

| # | atom_id | role | line(s) | atom_type | hl | sib | parent_section |
|---|---------|------|---------|-----------|----|----|---------------|
| 1 | a001 | boundary (round-start, H1) | 1 | HEADING | 1 | 1 | §RELREC [RELREC — Examples] |
| 2 | a002 | boundary (H2 #1) | 3 | HEADING | 2 | 1 | §RELREC [RELREC — Examples] |
| 3 | a003 | boundary (H3 L5) | 5 | HEADING | 3 | 1 | §RELREC.1 [Peer Record Examples] |
| 4 | a004 | stratified (SENTENCE) | 7 | SENTENCE | null | null | §RELREC.1.1 [Example 1] |
| 5 | a008 | stratified (TABLE_HEADER) | 15-16 | TABLE_HEADER | null | null | §RELREC.1.1 [Example 1] |
| 6 | a015 | boundary (H3 L24) | 24 | HEADING | 3 | 2 | §RELREC.1 [Peer Record Examples] |
| 7 | a024 | boundary (H3 L38) | 38 | HEADING | 3 | 3 | §RELREC.1 [Peer Record Examples] |
| 8 | a029 | stratified (TABLE_ROW) | 47 | TABLE_ROW | null | null | §RELREC.1.3 [Example 3] |
| 9 | a033 | boundary (H2 #2) | 53 | HEADING | 2 | 2 | §RELREC [RELREC — Examples] |
| 10 | a034 | boundary (H3 L55, RESTART) | 55 | HEADING | 3 | 1 | §RELREC.2 [Dataset Relationship Example] |
| 11 | a040 | boundary (round-end) | 66 | SENTENCE | null | null | §RELREC.2.1 [Example 1] |

## 3. Verdict

- **PASS**: 11/11
- **FAIL**: 0/11
- **Pass rate**: 100.0%
- **Halt**: no

## 4. Per-Check Matrix

| Check | Atoms tested | PASS | FAIL | Notes |
|-------|--------------|------|------|-------|
| Schema 12/12 fields exact names | 11 | 11 | 0 | All present, exact spelling |
| §E-1 schema regression sweep (no `verbatim_text`/`H1`/`H2`) | 40 (all atoms) | 40 | 0 | grep `verbatim_text`=0, `H1`/`H2` atom_type=0 |
| §E-2 H1: a001 hl=1 sib=1 | 1 | 1 | 0 | a001 ✓ |
| §E-3 TABLE_HEADER sib=null universal | 4 (all THs) | 4 | 0 | grep TABLE_HEADER=4, all sib=null |
| §E-4 extracted_by object form | 11 | 11 | 0 | object {subagent_type, prompt_version, ts} |
| §E-5 non-HEADING explicit-null hl + sib literal | 4 (a004/a008/a029/a040) | 4 | 0 | All literal `null` |
| Verbatim byte-exact | 11 | 11 | 0 | All match source line ranges byte-exact |
| §2.11 Plan B sub-namespace | 11 | 11 | 0 | See §5 |
| TABLE_HEADER 2-row span (Hook A1) | 1 (a008) + 3 others spot | 4 | 0 | line_end-line_start=1 for all 4 THs |
| atom_id sequence a001-a040 contiguous | 40 | 40 | 0 | a001…a040 verified |

## 5. §2.11 Plan B Sub-Namespace Verification (CRITICAL — 2nd Production Validation)

| H2 | line | sib | H3 children count | H3 sib_idx range | Sub-namespace |
|----|------|----|-------------------|------------------|----------------|
| L3 ## Peer Record Examples | 3 | 1 | 3 (L5/L24/L38) | 1, 2, 3 | §RELREC.1.{1,2,3} |
| L53 ## Dataset Relationship Example | 53 | 2 | 1 (L55) | 1 (RESTART) | §RELREC.2.1 |

**Mapping verification** (per round 09 kickoff §2.11 contract):

| Atom | Source line | Expected parent_section | Actual parent_section | Match |
|------|-------------|-------------------------|------------------------|-------|
| a002 H2 sib=1 | L3 | §RELREC [RELREC — Examples] (file-root) | §RELREC [RELREC — Examples] | ✓ |
| a003 H3 sib=1 | L5 | §RELREC.1 [Peer Record Examples] | §RELREC.1 [Peer Record Examples] | ✓ |
| a004 child of L5 | L7 | §RELREC.1.1 [Example 1] | §RELREC.1.1 [Example 1] | ✓ |
| a015 H3 sib=2 | L24 | §RELREC.1 [Peer Record Examples] | §RELREC.1 [Peer Record Examples] | ✓ |
| a024 H3 sib=3 | L38 | §RELREC.1 [Peer Record Examples] | §RELREC.1 [Peer Record Examples] | ✓ |
| a029 child of L38 | L47 | §RELREC.1.3 [Example 3] | §RELREC.1.3 [Example 3] | ✓ |
| a033 H2 sib=2 | L53 | §RELREC [RELREC — Examples] (file-root) | §RELREC [RELREC — Examples] | ✓ |
| **a034 H3 sib=1 (RESTART)** | **L55** | **§RELREC.2 sib=1 (NOT 4)** | **§RELREC.2 sib=1** | **✓ CRITICAL** |
| a040 child of L55 | L66 | §RELREC.2.1 [Example 1] | §RELREC.2.1 [Example 1] | ✓ |

**Critical finding**: L55 H3 sibling_index=**1** (RESTART under new H2 scope), NOT 4 (cumulative across H2). This confirms §2.11 Plan B sub-namespace is correctly scoped to per-H2 restart, not file-cumulative. **Plan B 2nd production validation: PASS.**

## 6. §0.5 Grep Cross-Verification

| Metric | Expected | Actual | Match |
|--------|----------|--------|-------|
| File line count (`wc -l`) | 66 | 66 | ✓ |
| `## ` H2 count | 2 | 2 | ✓ |
| `### ` H3 count | 4 | 4 | ✓ |
| Atoms total (`wc -l` jsonl) | 40 | 40 | ✓ |
| Atoms with `verbatim_text` (forbidden) | 0 | 0 | ✓ §E-1 |
| Atoms with `atom_type":"H1"` (forbidden) | 0 | 0 | ✓ §E-1 |
| Atoms with `atom_type":"H2"` (forbidden) | 0 | 0 | ✓ §E-1 |
| TABLE_HEADER atoms | 4 | 4 | ✓ |
| TABLE_HEADER atoms with `sibling_index":null` | 4 | 4 | ✓ §E-3 |

## 7. Findings

None. Zero findings across 11 audited atoms and 40-atom batch-wide grep sweep.

## 8. Notes for §2.11 Plan B 2nd Production Validation

This is the **2nd production validation** of §2.11 Plan B sub-namespace mechanics (1st was round 07 batch on PC). The RELREC/examples.md case is structurally tighter:
- 2 H2 sections (Peer Record Examples + Dataset Relationship Example), each with their own H3 series
- L55 H3 sib_idx=1 RESTART correctly demonstrates per-H2-scope sibling indexing (NOT file-cumulative)
- 4 sub-namespace branches exercised: §RELREC.1.{1,2,3} + §RELREC.2.1
- All 4 mapping cases pass byte-exact + structural

**v1.9.2 baseline 3rd round**: Plan B mechanics stable across two distinct file structures (PC subsections + RELREC dual-H2). No prompt-cut trigger detected for this batch.

## 9. Final Verdict

`RULE_A_BATCH_95: PASS raw=11/11 pct=100.0% halt=no`
