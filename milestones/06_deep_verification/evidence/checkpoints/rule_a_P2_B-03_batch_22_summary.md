# Rule A Audit — P2 B-03c Round 01 batch_22

> Source: `knowledge_base/domains/CE/examples.md` (1–165 lines)
> Writer atoms: `evidence/checkpoints/P2_B-03_batch_22_md_atoms.jsonl` (126 atoms)
> Reviewer: `pr-review-toolkit:code-reviewer` (Rule D peer-alternative pool, distinct from writer `general-purpose`)
> Audit ts: 2026-05-05
> Prompt: `subagent_prompts/P0_reviewer_v1.9.1.md`
> **Status: this is the LAST batch of Round 01 — round close mini-audit follows separately.**

## Sample composition (11 atoms total)

**Boundary 8**:
- a001 — H1 first atom (file root)
- a002 — H2 Example 1, sib=1
- a021 — H2 Example 2, sib=2
- a126 — last atom (TABLE_ROW relrec.xpt L165)
- a079 — TABLE_HEADER (Example 3, mh.xpt L99-100)
- a008 — TABLE_ROW (Example 1 CRF Rash row L13, **different example** than TABLE_HEADER pick)
- a015 — bold-caption SENTENCE `**ce.xpt**` (L22 table-title style)
- a012 — bold-caption SENTENCE `**Rows 1-3:**` (L18 Row-style)

**Stratified 3** (CM pilot H2 self-reference + Ex 3 multi-table complexity stress):
- a045 — narrative SENTENCE sub-line containing `Section 4.2.7.3` cross-ref (L54)
- a124 — TABLE_ROW relrec.xpt Ex3 (different table than a008 + a094)
- a053 — H2 Example 3, sib=3 (different H2 than boundary a021 Ex2)

## Atom totals (writer DONE manifest)

| atom_type    | count | check |
|--------------|-------|-------|
| HEADING      | 4     | ✓ (1 H1 + 3 H2) |
| SENTENCE     | 66    | ✓ |
| TABLE_HEADER | 11    | ✓ matches writer report (Ex1=1, Ex2=2, Ex3 has 7 incl crf+mh+suppmh+ce+suppce+pr+relrec, plus reuse of Ex2 ce.xpt = 1 extra; counted = 11) |
| TABLE_ROW    | 45    | ✓ |
| **TOTAL**    | **126** | ✓ matches writer DONE |

## Check results

### 1. verbatim byte-exact (Rule B)
**11/11 PASS**. All sample atoms byte-exact match source lines. Spot-checked via `awk` line read + `xxd` hex dump for bold-caption atoms (a015 `**ce.xpt**`, a012 `**Rows 1-3:**`).

### 2. atom_type per v1.9.1
**11/11 PASS**. HEADING / SENTENCE / TABLE_HEADER / TABLE_ROW types correctly assigned. No NOTE/Exception in source (no `> **Note:**` blockquote prefix), so D-2 hook not triggered. No FIGURE atoms (no `![...](...)`/figure_ref needed).

### 3. parent_section convention (CM pilot kickoff §2.2 lock)
- L1 H1 → `§CE [CE — Examples]` ✓ (a001 self-reference)
- L3 H2 + Ex 1 children → `§CE.1 [Example 1]` ✓ (a002 self-reference; a003-a020 children inherit)
- L31 H2 + Ex 2 children → `§CE.2 [Example 2]` ✓ (a021 self-reference; a022-a052 children inherit)
- L66 H2 + Ex 3 children → `§CE.3 [Example 3]` ✓ (a053 self-reference; a054-a126 children inherit)

Continuity verified by spot-checking parent_section transitions L20→L31 (a020→a021 Ex1→Ex2), L29→L31, L65→L66 (a052→a053 Ex2→Ex3). All correct.

### 4. HEADING meta (h_lvl + sib)
- a001: h_lvl=1, sib=1 ✓
- a002: h_lvl=2, sib=1 ✓ (Example 1 first H2)
- a021: h_lvl=2, sib=2 ✓ (Example 2 second H2 positional)
- a053: h_lvl=2, sib=3 ✓ (Example 3 third H2 positional)

**4/4 HEADING atoms PASS**.

### 5. TABLE_HEADER 2-row span (Hook A1)
**11/11 PASS** systematic-compliance verified across full batch (not just sample):

| atom_id | line_start | line_end | diff |
|---|---|---|---|
| a007 | 11 | 12 | 1 ✓ |
| a016 | 24 | 25 | 1 ✓ |
| a028 | 41 | 42 | 1 ✓ |
| a047 | 58 | 59 | 1 ✓ |
| a057 | 72 | 73 | 1 ✓ |
| a079 | 99 | 100 | 1 ✓ |
| a084 | 108 | 109 | 1 ✓ |
| a093 | 121 | 122 | 1 ✓ |
| a099 | 131 | 132 | 1 ✓ |
| a113 | 146 | 147 | 1 ✓ |
| a122 | 160 | 161 | 1 ✓ |

Style classification: **11 v1.9 standard 2-row + 0 v1.8 pilot 1-row legacy** (domains/, all v1.9.1 baseline). 0 FAIL_LINE_RANGE.

### 6. §D-5 bold-caption preserved verbatim
**Sample 2/2 PASS** (a015 `**ce.xpt**`, a012 `**Rows 1-3:**`).
Spot-checked broader pattern: writer reported ~12 bold-captions (7 xpt-style + 4 row-style + `**CRF: ...**`). Sample confirmed bold markers `**` byte-exact preserved on both ends. Atom_type=SENTENCE not NOTE per §D-5 carve-out (caption text is not "Note"/"Exception").

### 7. §C-1 sub-line atomization legitimate
**PASS**. Verified at L33 (Ex2 narrative split into 3 SENTENCE atoms a022/a023/a024 byte-exact reassemble), L48 (split into 4 a033/a034/a035/a036), L50/L52/L54 (Ex2 Row 3/4/5 narratives split correctly), L93/L95 (Ex3 Row 1/Row 2 narratives split correctly with bold-caption preserved in first sub-atom).

### 8. cross_refs §D-7.3 placement
**a045 PASS**. L54 has 3 sub-line atoms (a043 + a044 + a045). Only a045 carries `cross_refs: ["Section 4.2.7.3"]` — the sub-line atom containing the cross-ref text. Peers a043 ("**Row 5:**...") and a044 ("Because this event was not prespecified...") have empty cross_refs `[]`, per §D-7.3 + §D-7.5 (cross_refs assign to specific sub-line atom, not all peers).

### 9. extracted_by field
**126/126 PASS** (full-batch grep verified):
- subagent_type: `general-purpose`
- prompt_version: `P0_writer_md_v1.9.1`

### Kickoff drift verification (per §R-D1)
Round 01 kickoff (`P2_B-03c_round_01_kickoff.md` §0.5) reports 13/13 grep checksum byte-exact verified pre-dispatch. Writer atoms align with kickoff numeric claims:
- atom_id prefix `md_dmCE_ex_a` ✓ (matches kickoff §2.1 lock)
- parent_section format `§CE [CE — Examples]` + `§CE.<n> [Example <n>]` ✓ (matches kickoff §2.2 lock)
- atom count 126 ∈ kickoff-estimated range [120, 160] ✓ (within halt #8 [0.5×120, 1.5×160] = [60, 240])

No `kickoff_doc_drift_detected` flag from writer side. Reviewer independent grep verify: source L1 = `# CE — Examples` ✓, L165 = `| 4 | ABC | PR | | PRSPID | | MANY | 2 |` ✓.

## Verdict tally

| Sample atom | Verdict |
|---|---|
| a001 boundary H1 | PASS |
| a002 boundary H2 Ex1 sib1 | PASS |
| a021 boundary H2 Ex2 sib2 | PASS |
| a126 boundary last atom | PASS |
| a079 boundary TABLE_HEADER Ex3 | PASS |
| a008 boundary TABLE_ROW Ex1 | PASS |
| a015 boundary bold-caption `**ce.xpt**` | PASS |
| a012 boundary bold-caption `**Rows 1-3:**` | PASS |
| a045 stratified sub-line + cross_refs | PASS |
| a124 stratified diff-table TABLE_ROW relrec.xpt | PASS |
| a053 stratified diff-H2 Ex3 sib3 | PASS |

**Per-atom rate: 11/11 = 100% PASS** (gate threshold ≥90%).

## Findings

**0 HIGH severity**, **0 MEDIUM**, **0 LOW NEW**.

Per §R-D1 kickoff drift: kickoff §0.5 verified pre-dispatch, no drift detected, no atom-vs-source mismatch found in audit sample. Writer correctly applied:
- §D-5 bold-caption SENTENCE (NOT HEADING, NOT NOTE) for `**ce.xpt**` / `**Rows N:**` / `**Row N:**` / `**CRF: ...**` patterns
- §C-1 sub-line atomization for multi-sentence narrative lines (L5/L33/L48/L50/L52/L54/L85-95/L115-117 etc.)
- §D-7.3 + §D-7.5 cross_refs placement on specific sub-atom (a045 only, not a043/a044)
- §D-7.6 trailing-narrative parent attachment (Ex3 trailing narratives L137-156 inherit §CE.3 closest H2 parent, NOT escalate to chapter root §CE)
- CM pilot kickoff §2.2 H1/H2 self-reference convention

## Round 01 close audit context

This is **batch_22 = LAST batch of Round 01** (5 domains × 2 files = 10 batches batch_13..22). Per round 01 kickoff §6, **round close mini-audit (10-atom stratified across 5 domains × 2 files)** follows separately, dispatched to a Rule D-distinct reviewer. This per-batch Rule A audit feeds into round 01 cycle gate decision.

---

**RULE_A_VERDICT: PASS**
