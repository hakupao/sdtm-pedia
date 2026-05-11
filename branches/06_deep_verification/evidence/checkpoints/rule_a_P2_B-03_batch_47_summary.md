# Rule A Audit Summary — P2 B-03c batch_47

> Reviewer: pr-review-toolkit:code-reviewer (AUDIT mode, NOT code-review)
> Writer subagent_type: general-purpose (Rule D isolation upheld — reviewer ≠ writer)
> Prompt version: P0_reviewer_v1.9.1
> Audit date: 2026-05-06
> Source: `knowledge_base/domains/EX/examples.md` lines **233-434** (Ex6..Ex8, slice part 2 of 2)
> Writer output: `P2_B-03_batch_47_md_atoms.jsonl` — **133 atoms** (atom_id `md_dmEX_ex_a145..a277`)
> Estimate range: 101-172 → actual 133 (mid-band, ratio 0.658 atoms/line)

---

## 1. Sample plan executed

**13 verdicts** = 8 boundary + 5 stratified (per kickoff §2.4 cross-batch slice + bold-caption SENTENCE D-codified anomaly density).

| # | atom_id | role | type |
|---|---|---|---|
| 1 | a145 | boundary | HEADING (Ex6, slice first atom) |
| 2 | a146 | boundary | SENTENCE (post-H2 first) |
| 3 | a147 | boundary | SENTENCE (bold-caption **CRF:**) |
| 4 | a200 | boundary | HEADING (Ex7) |
| 5 | a201 | boundary | SENTENCE (post-H2 Ex7 first, long) |
| 6 | a252 | boundary | HEADING (Ex8) |
| 7 | a276 | boundary | TABLE_ROW (penultimate) |
| 8 | a277 | boundary | TABLE_ROW (last, L434 upper bound) |
| 9 | a149 | stratified | TABLE_HEADER (Ex6) |
| 10 | a256 | stratified | TABLE_ROW (Ex8 short CRF row) |
| 11 | a202 | stratified | LIST_ITEM (Ex7, sib=null lock) |
| 12 | a230 | stratified | SENTENCE (bold-caption **Row 1:**) |
| 13 | a161 | stratified | SENTENCE (bold-caption **Rows 1-12:**) |

---

## 2. Verdict roll-up

**13 / 13 PASS** (100% strict PASS, weighted 100%).

0 FAIL, 0 CONDITIONAL_PASS, 0 HIGH/MEDIUM/LOW findings.

---

## 3. Round invariants (5 / 5 PASS)

| # | Invariant | Result |
|---|---|---|
| 1 | atom_id collision check within batch | **PASS** — 0 dupe across 133 atoms; sequence contiguous a145..a277 (0 gaps) |
| 2 | Hook C-8 file prefix universal `knowledge_base/` | **PASS** — 133/133 atoms |
| 3 | H3a sub-namespace convention | **N/A** — 0 H3 in slice (kickoff §0.5 row 11 confirmed 8 H2 only at L5/59/109/148/165/233/307/389) |
| 4 | TABLE_HEADER Hook A1 span=1 | **PASS** — 13/13 TABLE_HEADER atoms have `line_end - line_start == 1` (v1.9 standard 2-row, no v1.8 pilot legacy in B-03) |
| 5 | extracted_by consistency | **PASS** — all 133 atoms `subagent_type=general-purpose` + `prompt_version=P0_writer_md_v1.9.1` |

---

## 4. Round 03 carry-forward locks (3 / 3 PASS applicable)

| Lock | Result |
|---|---|
| LIST_ITEM sib_idx=null (round 03 lock) | **PASS** — all 3 LIST_ITEM atoms (a202/a203/a204) `sibling_index=null` |
| §2.4 multi-batch slice cross-batch atom_id 续号 (round 03 lock) | **PASS** — batch_46 last `md_dmEX_ex_a144` (TABLE_ROW L231 parent §EX.5) → batch_47 first `md_dmEX_ex_a145` (HEADING L233 parent §EX file root, sib=6 continuing H2 chain Ex5=5→Ex6=6); 144+1=145 ✓; H2 boundary at L232\|233 clean (a144 ≤ L231 < L232 ≤ blank ≤ L233 = a145) |
| §2.6 FIGURE-in-domains lock | **PASS** — 0 FIGURE atoms (kickoff §0.5 row 14 grep confirmed 0 mermaid) |
| §2.7 numberless H2 in assumptions.md | **N/A** — applicable only to FT/ass batch_50 |

---

## 5. atom_type distribution observed vs kickoff expected

| Type | Observed | Expected per kickoff | Status |
|---|---|---|---|
| HEADING | 3 (all H2 sib=6,7,8) | 3 H2 (Ex6/Ex7/Ex8) | ✓ exact |
| TABLE_HEADER | 13 | (kickoff stated 13) | ✓ exact |
| TABLE_ROW | 74 | not stated explicitly | — observed |
| LIST_ITEM | 3 | (kickoff stated 3) | ✓ exact |
| SENTENCE | 40 | (kickoff stated 40) | ✓ exact |
| FIGURE | 0 | 0 (per §2.6) | ✓ |
| NOTE | 0 | 0 (no `> **Note:**` blockquote in slice) | ✓ |
| CODE_LITERAL | 0 | — | ✓ |

Total 133 atoms = 3+13+74+3+40 ✓.

---

## 6. parent_section transitions (PASS)

Independently verified all 133 atoms:
- a145 (H2 Ex6) parent = `§EX [EX — Examples]` (file root) ✓
- a146..a199 parent = `§EX.6 [Example 6]` ✓ (54 atoms)
- a200 (H2 Ex7) parent = `§EX [EX — Examples]` (file root) ✓
- a201..a251 parent = `§EX.7 [Example 7]` ✓ (51 atoms)
- a252 (H2 Ex8) parent = `§EX [EX — Examples]` (file root) ✓
- a253..a277 parent = `§EX.8 [Example 8]` ✓ (25 atoms)

Zero misattribution across H2 boundaries. Each H2 atom itself inherits file root (per §2.5 spec); children inherit H2 self-namespace.

---

## 7. Line range bounds (PASS)

- `min(line_start) = 233` — exact slice lower bound ✓
- `max(line_end) = 434` — exact slice upper bound ✓
- 0 atoms outside [233, 434].

---

## 8. v1.9.1 D-codified anomaly handling

§R-D5 (bold-caption SENTENCE accept, MEDIUM): writer correctly classified as SENTENCE (not HEADING / not NOTE):
- a147 `**CRF:**`
- a148 `**Subject 56789001**`
- a154 `**Subject 56789003**`
- a161 `**Rows 1-12:** ...`
- a162 `**Rows 13-24:** ...`
- a230 `**Row 1:** ...` etc.

All non-Note/Exception bold captions per regex `^\*\*[A-Z][^*]+(:|\.)\*\*` correctly stay as SENTENCE. Reviewer accept per §R-D5.

§R-D6 (TABLE_HEADER style): All 13 TABLE_HEADER atoms use v1.9 standard 2-row (`line_end - line_start == 1`); 0 v1.8 pilot legacy 1-row (correct — B-03 domains/ scope).

---

## 9. Kickoff drift verification (§R-D1)

Independent grep confirmed kickoff §0.5 row 11 claim: EX/examples.md H2 boundaries at lines 5, 59, 109, 148, 165, 233, 307, 389. Writer's H2 atoms at L233 (Ex6 sib=6), L307 (Ex7 sib=7), L389 (Ex8 sib=8) align byte-exact with source. **No kickoff drift detected; no writer fabrication.**

---

## 10. Cross-batch atom_id continuity (§2.4 lock — round 04 second application)

Verified manually:

```
batch_46 tail: md_dmEX_ex_a144  type=TABLE_ROW  L231  parent=§EX.5 [Example 5]
                                                       verbatim="| 2 | ABC | EX | | EXLNKID | | ONE | 1 |"
batch_47 head: md_dmEX_ex_a145  type=HEADING    L233  parent=§EX [EX — Examples]
                                                       sib=6  h_lvl=2  verbatim="## Example 6"
```

Boundary clean:
- atom_id: 144 + 1 = 145 ✓
- Source line: a144 line_end=231 < blank L232 < a145 line_start=233 ✓
- H2 sib chain: batch_46 sib=1..5 (Ex1..Ex5) → batch_47 sib=6,7,8 (Ex6..Ex8) ✓ (file-level, contiguous)
- parent_section: Ex5 boundary atom (TABLE_ROW under §EX.5) → Ex6 H2 atom (file root) ✓

§2.4 lock fully validated for slice part 2.

---

## 11. Findings

**None.** 0 HIGH / 0 MEDIUM / 0 LOW. All atoms strict PASS.

---

## 12. Verdict

```
BATCH_47_RULE_A PASS rate=100% invariants=5/5 findings=[]
```

Round 04 rolling: batch_45 PASS + batch_46 PASS + batch_47 PASS (slice fully closed). EX domain Rule A complete; ready for batch_48 (FA/ass) dispatch.
