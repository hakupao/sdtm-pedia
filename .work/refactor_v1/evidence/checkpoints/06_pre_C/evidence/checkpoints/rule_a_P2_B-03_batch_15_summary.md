# Rule A Audit — P2 B-03c batch_15 (AG/assumptions.md)

> Reviewer subagent_type: `pr-review-toolkit:code-reviewer` (peer-alternative pool per v1.9.1 §R-D8; ≠ writer subagent_type `general-purpose`, Rule D PASS)
> Audit ts: 2026-05-05
> Source: `knowledge_base/domains/AG/assumptions.md` (1–25 lines, 1 H1 + 5 numbered top-level items + 14 sub-letter items)
> Writer output: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_15_md_atoms.jsonl` (20 atoms; HEADING=1 + LIST_ITEM=19)
> Sample size: 11 verdicts (8 boundary + 3 stratified)
> Reviewer prompt version: `P0_reviewer_v1.9.1` (26 hooks)

## Sample composition

| Sample role | atom_id | atom_type | parent_section | line_range |
|---|---|---|---|---|
| boundary_first_h1_root | a001 | HEADING | §AG [AG — Assumptions] | 1 |
| boundary_first_numbered_top_level_1 | a002 | LIST_ITEM | §AG [AG — Assumptions] | 3 |
| boundary_first_sub_letter_a | a003 | LIST_ITEM | §AG [AG — Assumptions] | 4 |
| mid_sub_letter_c_under_item_1 | a005 | LIST_ITEM | §AG [AG — Assumptions] | 6 |
| boundary_short_caption_numbered_2 | a007 | LIST_ITEM | §AG [AG — Assumptions] | 9 |
| mid_short_caption_numbered_3 | a010 | LIST_ITEM | §AG [AG — Assumptions] | 13 |
| mid_sub_letter_a_under_item_4 | a015 | LIST_ITEM | §AG [AG — Assumptions] | 19 |
| boundary_last_numbered_top_level_5 | a018 | LIST_ITEM | §AG [AG — Assumptions] | 23 |
| stratified_sub_letter_a_under_item_5_with_dashdash_var | a019 | LIST_ITEM | §AG [AG — Assumptions] | 24 |
| boundary_last_atom_eof_sub_letter_b | a020 | LIST_ITEM | §AG [AG — Assumptions] | 25 |
| stratified_short_sub_letter_b_under_item_3 | a012 | LIST_ITEM | §AG [AG — Assumptions] | 15 |

Note: small 20-atom file → boundary set heavily overlaps stratified candidates; sample selection prioritizes 5 distinct numbered top-level items + diverse sub-letter positions (a/b/c) + mix of long/short verbatim + dashdash-variable bearing atoms. Per kickoff §"Sample selection (8 boundary + 3 stratified = 11 atoms; small file, may overlap)" — overlap is canonical.

## Per-atom verdicts

| atom_id | verdict | severity |
|---|---|---|
| a001 | PASS | INFO |
| a002 | PASS | INFO |
| a003 | PASS | INFO |
| a005 | PASS | INFO |
| a007 | PASS | INFO |
| a010 | PASS | INFO |
| a012 | PASS | INFO |
| a015 | PASS | INFO |
| a018 | PASS | INFO |
| a019 | PASS | INFO |
| a020 | PASS | INFO |

**Strict PASS rate**: 11/11 = **100%**.

## File structure & atom-count legitimacy

Source `knowledge_base/domains/AG/assumptions.md` is 25 lines total. Independent reviewer count via `wc -l` confirms 25.

| Source line | Content type |
|---|---|
| L1 | `# AG — Assumptions` (H1) |
| L2, L8, L12, L17, L22 | blank separators |
| L3, L9, L13, L18, L23 | top-level numbered items 1–5 |
| L4–L7 | sub-letters a/b/c/d under #1 (4 items) |
| L10–L11 | sub-letters a/b under #2 (2 items) |
| L14–L16 | sub-letters a/b/c under #3 (3 items) |
| L19–L21 | sub-letters a/b/c under #4 (3 items) |
| L24–L25 | sub-letters a/b under #5 (2 items) |

Atom totals: 1 H1 + 5 numbered + (4+2+3+3+2)=14 sub-letter LIST_ITEMs = **20 atoms**. Writer's 20-atom output is exact-coverage. No fragment dropped, no fabricated additions.

## §D-D8 / CM-pilot chapter root inherit verification (§R-D4)

File contains exactly 1 H1 (`# AG — Assumptions` at L1) and **0 H2/H3** subheadings. Per kickoff §4 + reviewer §R-D4 codification: when no subsections exist, all children atoms inherit chapter root `§AG [AG — Assumptions]`. 

Reviewer independent verification: all 19 LIST_ITEM atoms have `parent_section == "§AG [AG — Assumptions]"` consistently. Spot-check across all 19 atoms confirms zero deviation. **No `parent_section_should_be_subsection` finding** — D8 numberless chapter root inherit applies (here strengthened: not even an `## Overview` H2 — pure single-H1 root file).

## §D-7.2 Axis 5 LIST_ITEM canonical compliance

Atom_type=LIST_ITEM applied uniformly to:
- Top-level numbered `^N\. ` (5 atoms: a002, a007, a010, a014, a018)
- Sub-letter `^   [a-z]\. ` (3-space indent, 14 atoms: a003-a006, a008-a009, a011-a013, a015-a017, a019-a020)

Sample includes 3 numbered top-level (a002/a007/a018) + 7 sub-letter (a003/a005/a012/a015/a019/a020 + boundary first/last sub-letters). All conform to canonical Axis 5 LIST_ITEM. Note a007 (`2. Examples and structure`) is a short header-like phrase but correctly emitted as LIST_ITEM (not HEADING), since source line lacks `^#{1,6}` prefix and per Axis 5 ordered-list rule.

## Verbatim byte-exact verification (Hex-dump independent verify)

Reviewer Bash `od -c` cross-verified prefix bytes for sample atoms:
- L1: `# A G   —** **   A s s u m p t i o n s \n` — em-dash U+2014 (3-byte UTF-8 `e2 80 94`) preserved
- L3: `1 .   P u r p o s e   o f   t h e   d o m a i n :` — leading `1. ` byte-exact
- L4: `        a .   T h e   C o n c o m i t a n t` — 3 leading spaces (`0x20` x3) preserved
- L11: `        b .   T h e   s t r u c t u r e` — 3 leading spaces preserved
- L19: `        a .   A G P R E S P` — 3 leading spaces + `a.` preserved
- L24: `        a .   H o w e v e r ,   - - I N D C` — double-dash variable prefix `--` preserved
- L25: `        b .   T h e   v a r i a b l e s   - - D O S T O T` — `--DOSTOT` and trailing line preserved

**0 byte-exact mismatches** in sample. Apostrophes (`sponsor's`) and embedded quoted strings (`"Y"`, `"N"`, `"NOT DONE"`, `"ALBUTEROL"`) all preserved.

## TABLE_HEADER 2-row span (Hook A1) classification

**N/A** — AG/assumptions.md contains 0 tables (verified by grep on `^|` and `---|---`). 0 TABLE_HEADER, 0 TABLE_ROW atoms expected and produced. **0 FAIL_LINE_RANGE possible.**

## §D-5 bold-caption SENTENCE / NOTE-BQ status (§R-D2 / §R-D5)

**N/A for this file**:
- 0 `**Note:**` / `**Exception:**` / `> **Note:**` patterns (no NOTE atoms expected)
- 0 `**Bold-caption**` patterns outside Note/Exception (no SENTENCE bold-caption atoms expected)
- 0 FIGURE references (figure_ref=null verified across all 20 atoms)

## Kickoff drift verification (§R-D1)

Per kickoff prompt: file is small (20 atoms), single-H1, no tables, no NOTEs, no FIGUREs — minimal anomaly surface. 

**Reviewer independent verification**: writer atoms parent_section assignment matches kickoff §"parent_section: ALL atoms = `§AG [AG — Assumptions]` (file root self-reference; only 1 H1, no H2/H3 — root inherit per §D-D8 / CM pilot)" exactly. No drift detected. Per Hook R24, no kickoff drift to route.

## sib_index / heading_level meta (HEADING atom only)

a001 (only HEADING):
- heading_level=1 ✓ (matches `^# ` source)
- sibling_index=1 ✓ (only H1 in file, positional first)
- All LIST_ITEM atoms have heading_level=null + sibling_index=null per writer schema (LIST_ITEM does not carry heading_level/sib_index — confirmed canonical).

## Rule D 隔离 verification

- Writer subagent_type: `general-purpose`
- Reviewer subagent_type: `pr-review-toolkit:code-reviewer`
- ≠ writer (peer-alternative pool per v1.9.1 §R-D8 SUSTAINED status; B-02 + B-03c sustained empirical PASS)
- **Rule D PASS**

## Verdict

- **Strict PASS rate**: 11/11 = 100%
- **HIGH severity findings**: 0
- **MEDIUM severity findings**: 0
- **LOW severity findings**: 0
- **File coverage**: 20/20 atoms emitted, exact-coverage with source
- **PASS gate**: ≥90% strict PASS achieved → **PASS**

---

RULE_A_VERDICT: PASS
