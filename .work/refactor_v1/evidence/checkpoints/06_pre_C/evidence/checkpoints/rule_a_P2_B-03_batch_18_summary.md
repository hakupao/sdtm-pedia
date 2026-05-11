# Rule A audit — P2 B-03c round 01 batch_18 (BE/examples.md)

> Audit run: 2026-05-05
> Reviewer: `pr-review-toolkit:code-reviewer`
> Writer: `general-purpose` (prompt_version `P0_writer_md_v1.9.1`)
> Rule D 隔离: PASS (writer subagent_type ≠ reviewer subagent_type)
> Source: `knowledge_base/domains/BE/examples.md` (161 lines)
> Writer output: `evidence/checkpoints/P2_B-03_batch_18_md_atoms.jsonl` (121 atoms)
> Sample size: 11 (8 boundary + 3 stratified)

## §1 Sample composition (per kickoff §1 + §R-Stratified-Sampling)

| # | atom_id | class | role | verdict |
|---|---|---|---|---|
| 1 | md_dmBE_ex_a001 | boundary | H1 file root (first atom) | PASS |
| 2 | md_dmBE_ex_a002 | boundary | H2 Example 1 (sib=1, L3) | PASS |
| 3 | md_dmBE_ex_a046 | boundary | H2 Example 2 (sib=2, L60) | PASS |
| 4 | md_dmBE_ex_a121 | boundary | last atom (LIST_ITEM L161) | PASS |
| 5 | md_dmBE_ex_a015 | boundary | TABLE_HEADER mid (be.xpt L17-18) | PASS |
| 6 | md_dmBE_ex_a070 | boundary | TABLE_ROW varied (Example 2 row 8 L89) | PASS |
| 7 | md_dmBE_ex_a014 | boundary | bold-caption SENTENCE `**be.xpt**` (L15) | PASS |
| 8 | md_dmBE_ex_a050 | boundary | bold-caption SENTENCE `**Row 1:**` Example 2 (L64) | PASS |
| 9 | md_dmBE_ex_a004 | stratified | narrative sub-line SENTENCE (L7 of 3 sub-atoms) | PASS |
| 10 | md_dmBE_ex_a120 | stratified | LIST_ITEM numbered reference (L160) | PASS |
| 11 | md_dmBE_ex_a079 | stratified | TABLE_HEADER different-table (suppbe.xpt Example 2 L101-102) | PASS |

**PASS rate: 11/11 = 100%** (gate ≥ 90% / 10/11)

## §2 Check matrix coverage

| Check | Description | Coverage |
|---|---|---|
| 1 | verbatim byte-exact (preserves `**`, `|`, quotes, `—`) | 11/11 PASS (verified via Python `==` against source `split('\n')`) |
| 2 | atom_type correctness per v1.9.1 | 11/11 PASS (HEADING / SENTENCE / TABLE_HEADER / TABLE_ROW / LIST_ITEM all canonical) |
| 3 | parent_section convention | 11/11 PASS (CM pilot SELF precedent inherited correctly: H1→`§BE [BE — Examples]`, H2 children→`§BE.<index> [Example N]`) |
| 4 | HEADING meta (h_lvl, sib_index) | 3/3 HEADING atoms PASS (a001 lvl=1 sib=1; a002 lvl=2 sib=1; a046 lvl=2 sib=2) |
| 5 | TABLE_HEADER 2-row span (Hook A1) | 9/9 TABLE_HEADER atoms in batch are v1.9 standard 2-row (line_end-line_start==1); 2 sampled (a015, a079) PASS |
| 6 | §D-5 bold-caption SENTENCE | 2 sampled (a014 `**be.xpt**`, a050 `**Row 1:**`) PASS — bold-prefix preserved byte-exact, atom_type=SENTENCE per §R-D5 |
| 7 | §C-1 sub-line atomization legitimate | a004 (L7 first of 3) PASS — verified a004+a005+a006 verbatims joined byte-exact reconstruct source L7 (240 chars); line_start==line_end on all sub-line atoms |
| 8 | extracted_by metadata | 11/11 PASS (`subagent_type`=`general-purpose`, `prompt_version`=`P0_writer_md_v1.9.1`) |

## §3 CM pilot SELF parent_section precedent — verification

Reviewer cross-checked CM pilot atoms in `md_atoms.jsonl` to confirm convention inheritance:

| CM pilot atom | Pattern | BE batch_18 atom | Pattern | Match |
|---|---|---|---|---|
| `md_dmCM_ex_a001` (H1 root) | `§CM [CM — Examples]` | `md_dmBE_ex_a001` (H1 root) | `§BE [BE — Examples]` | ✓ identical SELF format |
| `md_dmCM_ex_a002` (H2 Example 1 sib=1) | `§CM.1 [Example 1]` | `md_dmBE_ex_a002` (H2 Example 1 sib=1) | `§BE.1 [Example 1]` | ✓ identical SELF subsection |
| `md_dmCM_ex_a022` (H2 Example 2 sib=2) | `§CM.2 [Example 2]` | `md_dmBE_ex_a046` (H2 Example 2 sib=2) | `§BE.2 [Example 2]` | ✓ identical |

Confirmed: kickoff §2.2 convention lock honored. atom_id prefix `md_dmBE_ex_aNNN` also matches kickoff §2.1 (CM pilot inherit).

## §4 Schema + structural integrity (independent grep)

- All 121 atoms include 12 required schema fields (no missing keys)
- All `file` fields = `knowledge_base/domains/BE/examples.md` (Hook C-8 PASS)
- All `figure_ref` = null (no figures in BE/examples.md — Hook A4 N/A)
- All non-HEADING atoms have `heading_level`=null AND `sibling_index`=null (no leakage)
- atom_id sequential `md_dmBE_ex_a001..a121` no gap no collision
- 13 lines have multi-atom sub-line splits (L7=3, L9=2, L11=2, L13=3, L31=5, L45=2, L62=3, L66=3, L70=2, L74=2, L95=2, L97=2, L130=2) — all SENTENCE only, all `line_start==line_end` (Hook R22 sustained)
- Atom counts: HEADING=3 / SENTENCE=59 / TABLE_HEADER=9 / TABLE_ROW=48 / LIST_ITEM=2 = 121 ✓ matches writer report

## §5 Kickoff drift verification (per §R-D1 + Hook R24)

- Kickoff §1 estimated atoms for batch_18: ~120-160. Actual: 121 — within range ✓
- Kickoff §0.5 numeric claims for batch_18: source 161L → reviewer `wc -l` confirms 161 source lines ✓
- No `kickoff_doc_drift_detected` flag from writer for this batch
- No kickoff-vs-source drift detected by reviewer

## §6 Anomaly instances examined (per §R-Stratified-Sampling v1.9.1+)

| Anomaly type | Instance count | Sample audited | Verdict |
|---|---|---|---|
| §D-5 bold-caption SENTENCE | ~17 instances (table titles + Row N captions) | a014 + a050 | PASS — atom_type=SENTENCE canonical |
| §C-1 sub-line SENTENCE atomization | 13 multi-atom lines | a004 (L7) | PASS — joined verbatim reconstructs source byte-exact |
| §D-7.2 LIST_ITEM ordered list | 2 instances (References L160-161) | a120 + a121 | PASS — atom_type=LIST_ITEM canonical |
| TABLE_HEADER 2-row v1.9 standard | 9 instances | a015 + a079 | PASS — all 2-row span (no v1.8 pilot legacy expected outside ch04) |

No NOTE blockquote (§D-2) atoms present — file has no `> **Note:**` / `> **Exception:**` source content.
No D5 dual-constraint h_lvl divergence — only H1 + H2 numbered SELF pattern, no nested H3+.
No D8 numberless `## Overview` — file uses `## Example N` numbered H2.
No FIGURE atoms — file has no figure references.

## §7 Findings

**HIGH severity findings**: 0
**MEDIUM severity findings**: 0
**LOW severity findings**: 0
**INFO**: Writer reported "7 instances" for `**filename.xpt**` table-title bold-captions; reviewer counted 9 such atoms (a014, a021, a031, a040, a061, a078, a090, a102, a111). Minor count undercount in writer's free-text description but **no atom-level defect** — all 9 atoms exist in JSONL with correct atom_type=SENTENCE and byte-exact verbatim. Routes to orchestrator (Hook R24) as kickoff/report-level note, NOT writer FAIL.

## §8 Verdict

- 11/11 = 100% strict PASS, exceeds gate threshold ≥ 90% (10/11)
- 0 HIGH / 0 MEDIUM / 0 LOW findings
- v1.9.1 codified anomalies (§D-5 bold-caption, §C-1 sub-line, §D-7.2 LIST_ITEM, TABLE_HEADER 2-row) all canonical
- CM pilot SELF parent_section convention sustained in first BE/examples.md batch
- Rule D 隔离 PASS (writer=`general-purpose` ≠ reviewer=`pr-review-toolkit:code-reviewer`)

---

RULE_A_VERDICT: PASS
