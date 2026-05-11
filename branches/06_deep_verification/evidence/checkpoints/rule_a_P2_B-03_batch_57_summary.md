# Rule A audit — P2 B-03c round 04 batch_57 (IE/examples.md) — FINAL batch of round 04

> Reviewer: pr-review-toolkit:code-reviewer (peer-alternative per v1.9.1 §D-8 reviewer pool; round 04 default per-batch reviewer; 13/13 sustained)
> Writer: general-purpose+P0_writer_md_v1.9.1
> Source: knowledge_base/domains/IE/examples.md (18L)
> Atoms: 11 (1 H1 + 1 H2 + 4 SENTENCE + 1 TABLE_HEADER + 4 TABLE_ROW); est range 9-15; halt low <4 / halt high >22 (within bounds)
> Sample: 11/11 = 100% full coverage (small file <30 atoms per kickoff §5; 0 stratified, all atoms = boundary/anomaly)
> Round 04 reviewer prompt: P0_reviewer_v1.9.1 (26 hooks)

## Verdict matrix

| # | atom_id | type | h_lvl | sib | line | byte_exact | verdict |
|---|---------|------|-------|-----|------|------------|---------|
| 1 | md_dmIE_ex_a001 | HEADING | 1 | 1 | L1 | ✓ | PASS |
| 2 | md_dmIE_ex_a002 | HEADING | 2 | 1 | L3 | ✓ | PASS |
| 3 | md_dmIE_ex_a003 | SENTENCE | null | null | L5 | ✓ | PASS |
| 4 | md_dmIE_ex_a004 | SENTENCE | null | null | L7 | ✓ | PASS |
| 5 | md_dmIE_ex_a005 | SENTENCE | null | null | L9 | ✓ | PASS |
| 6 | md_dmIE_ex_a006 | SENTENCE | null | null | L11 | ✓ | PASS |
| 7 | md_dmIE_ex_a007 | TABLE_HEADER | null | null | L13-14 | ✓ | PASS |
| 8 | md_dmIE_ex_a008 | TABLE_ROW | null | null | L15 | ✓ | PASS |
| 9 | md_dmIE_ex_a009 | TABLE_ROW | null | null | L16 | ✓ | PASS |
| 10 | md_dmIE_ex_a010 | TABLE_ROW | null | null | L17 | ✓ | PASS |
| 11 | md_dmIE_ex_a011 | TABLE_ROW | null | null | L18 | ✓ | PASS |

**PASS rate**: 11/11 = **100%**

## Round invariants check (5/5)

| # | Invariant | Result |
|---|-----------|--------|
| 1 | a001 HEADING h_lvl=1 sib=1 (file root H1) | ✓ PASS |
| 2 | a002 HEADING h_lvl=2 sib=1 at L3 (only H2 in file; pre-H2 carve: H2 atom itself parent=file root) | ✓ PASS |
| 3 | Pre-H2 atoms (a001-a002) parent_section=`§IE [IE — Examples]` (file root) | ✓ PASS (2/2) |
| 4 | Under-H2 atoms (a003-a011) parent_section=`§IE.1 [Example 1]` | ✓ PASS (9/9) |
| 5 | TABLE_HEADER (a007) sib=null + line_end-line_start=1 (v1.9 standard 2-row, NOT pilot legacy — B-03 domain outside ch04 a001-a218) | ✓ PASS |

**Invariants**: 5/5 PASS.

## Cross_refs verification (0 inline section refs)

Source IE/examples.md contains **0 inline `Section X.Y.Z` references** (verified via grep). All 11 atoms have `cross_refs=[]` correctly.

## Hook checks (v1.9.1 reviewer hooks 1-26)

- **Hook C-8 file prefix**: ✓ all 11 atoms `knowledge_base/` prefix
- **Hook A4 FIGURE figure_ref**: ✓ N/A (0 FIGURE atoms — round 04 §0.5 row 14 grep verified 0 mermaid in scope)
- **Hook D-NOTE-BQ (D-2)**: ✓ N/A (0 NOTE atoms; no `> **Note:**` blockquote in source)
- **Hook D-D8 numberless H2 (D-4)**: ✓ N/A (a002 is `## Example 1` numbered H2, sub-namespace `§IE.1 [Example 1]` correctly created; D-D8 numberless rule does not apply)
- **Hook A1 TABLE_HEADER**: ✓ a007 line_end-line_start=1 (v1.9 standard 2-row); explicit style classification: 1 v1.9 standard 2-row TABLE_HEADER + 0 v1.8 pilot 1-row legacy
- **Hook D-D7.2 LIST_ITEM ordered**: ✓ N/A (0 LIST_ITEM atoms in this file)
- **Hook D-D7.3 cross_refs field**: ✓ N/A (0 inline section refs; all cross_refs=[])
- **Hook 22b kickoff drift**: ✓ kickoff §0.5 20/20 PASS at write time; atom count 11 within est [9-15] and halt bounds [<4, >22]; atoms vs source byte-exact (no writer fabrication)
- **Hook R22 sub-line SENTENCE**: ✓ N/A (no sub-line atom split)
- **Hook R-D5 bold-caption SENTENCE**: ✓ a004 (`**Rows 1-2:**`), a005 (`**Rows 3-4:**`), a006 (`**ie.xpt**`) — 3 bold-caption SENTENCE atoms canonical per R-D5 (non-Note/Exception caption pattern; matches `^\*\*[A-Z][^*]+\*\*` and filename variant); correctly NOT classified as HEADING or NOTE
- **Hook R-D6 TABLE_HEADER style**: ✓ 1 v1.9 standard 2-row + 0 v1.8 pilot 1-row legacy; 0 FAIL_LINE_RANGE post-classification
- **extracted_by consistency**: ✓ all 11 atoms = `general-purpose+P0_writer_md_v1.9.1` ts=`2026-05-06T19:00:00Z`

## Kickoff drift verification (per Hook R24 / R-D1)

Kickoff §0.5 row 6 (IE in 6 domains) + row 7 (12 source files) + row 9 (IE/ex 18L bucket <50) + row 16 (batch_57 sequence) verified at kickoff write time. atom count actual=11 within est range [9-15] and halt bounds [<4, >22]. **No kickoff doc drift detected for batch_57**. Writer atoms vs source 100% byte-exact = no Rule B violation. Independent grep of source confirms 18L + 1 H1 + 1 H2 + table starts L13.

## Findings

**HIGH**: 0
**MEDIUM**: 0
**LOW**: 0
**INFO**: 0

No defects detected. batch_57 is canonical examples.md pattern with single example: file-root H1 + numbered H2 (`## Example 1`) creating `§IE.1 [Example 1]` sub-namespace + 4 SENTENCE atoms (1 narrative + 2 `**Rows N-N:**` bold-caption + 1 `**ie.xpt**` filename) + 1 TABLE_HEADER (16-column ie.xpt table) + 4 TABLE_ROW. Pre-H2 carve correctly applied (a001 H1 + a002 H2 itself parent=file root; under-H2 a003-a011 parent=§IE.1).

## Round 04 batch summary context

batch_57 = **FINAL batch of round 04** (13 batches total batch_45..57 covering 6 domains EX/FA/FT/GF/HO/IE × 2 files = 12 source files = 13 batches with EX/ex sliced). Post batch_57 → trigger round 04 mini-audit per kickoff §6.

## Verdict

**BATCH_57_RULE_A PASS rate=100% invariants=5/5 findings=none**

---

*Audit executed 2026-05-06 round 04 batch_57 IE/examples.md (FINAL batch of round 04). Source 18L → 11 atoms (1 H1 + 1 H2 + 4 SENTENCE + 1 TABLE_HEADER + 4 TABLE_ROW); 11/11 byte-exact PASS; 5/5 round invariants PASS; 0 findings. Round 04 ready for mini-audit gate.*
