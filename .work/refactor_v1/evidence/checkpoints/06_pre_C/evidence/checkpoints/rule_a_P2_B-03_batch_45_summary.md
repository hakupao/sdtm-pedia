# Rule A audit — P2 B-03 batch_45 (EX/assumptions.md)

> Reviewer subagent: pr-review-toolkit:code-reviewer (Rule D 隔离 ≠ writer subagent_type general-purpose)
> Reviewer prompt: P0_reviewer_v1.9.1 (26 hooks; v1.7 18 + v1.9 2 + v1.9.1 6)
> Audit timestamp: 2026-05-06
> Source: knowledge_base/domains/EX/assumptions.md (33L)
> Writer output: P2_B-03_batch_45_md_atoms.jsonl (27 atoms = 1 HEADING + 26 LIST_ITEM)

## Sample plan

- **Plan**: 8 boundary + 3 stratified = **11 verdicts** per v1.9.1 §R-Stratified-Sampling per-batch standard.
- **Boundary atoms (8)**: a001 (file H1), a002 / a003 (start), a013 / a014 (mid — boundary between item 1.d.ii Roman numeral list end + item 2 numbered top-level start), a025 / a026 / a027 (end).
- **Stratified atoms (3)**: a005 (sub-bullet w/ trailing-colon intro `include the following:` — Hook D-NOTE-BQ negative pattern verify), a015 (codelist literals `ASPIRIN`/`100MG TABLET`/`PLACEBO`/`EXTRT` w/ JSON-escaped double-quotes), a020 (longest text density — L24 multi-sentence narrative ~1140 chars w/ JSON-escaped `"start visit"`/`"end visit"`).
- **Coverage**: 11/27 = 40.7% sampled; non-sampled atoms a004, a006-a012, a016-a019, a021-a024 are homogeneous LIST_ITEM single-line copies and inherit pattern from boundary verdicts.

## Per-atom verdicts (11/11 PASS)

| atom_id | line | role | verdict |
|---|---|---|---|
| a001 | L1 | file H1 boundary | PASS |
| a002 | L3 | start (1. top-level) | PASS |
| a003 | L4 | start (sub-bullet a.) | PASS |
| a005 | L6 | stratified (trailing-colon intro) | PASS |
| a013 | L14 | mid (deepest indent ii.) | PASS |
| a014 | L16 | mid (numbered top-level 2.) | PASS |
| a015 | L17 | stratified (codelist literals) | PASS |
| a020 | L24 | stratified (longest text density) | PASS |
| a025 | L31 | end (codelist --DOSTOT) | PASS |
| a026 | L32 | end (cross-domain refs EC/EX) | PASS |
| a027 | L33 | end (codelist --PRESP, --OCCUR, --STAT, --REASND) | PASS |

**Per-atom PASS rate**: **11/11 = 100.0%** (gate ≥90% PASS).

### Check breakdown per atom (a..h all PASS for all 11)

- (a) atom_id format & sequence: a001..a027 strict +1 increment, no gaps, prefix `md_dmEX_assn_a` matches kickoff §1 row 1.
- (b) atom_type correct: H1 = HEADING; numbered/lettered/Roman list items all = LIST_ITEM per §R-D7.2 (ordered list `^N\.\s+` canonical). No SENTENCE/NOTE/HEADING-misclassified items.
- (c) verbatim byte-exact: all 11 sampled lines match source byte-exact (including 3-space + 6-space indents on sub-bullets a-d / Roman numerals i-v, double-quoted ASPIRIN/PLACEBO codelist literals, hyphenated `--PRESP/--OCCUR/--STAT/--REASND` qualifier prefixes; JSON-escaped quotes preserve source).
- (d) line_start/line_end: all 11 ≡ source line; line_start == line_end (single-line atoms; no multi-line span in this file).
- (e) parent_section: all 11 = `§EX [EX — Assumptions]` (file root, no H2 in source per `grep '^## ' EX/assumptions.md` → 0 matches; no sub-namespace expected).
- (f) sibling_index: H1 = null (file root self-ref canonical); all 26 LIST_ITEM = null per round 03 lock.
- (g) heading_level: H1 = 1; all 26 LIST_ITEM = null (correct).
- (h) file: all 11 = `knowledge_base/domains/EX/assumptions.md` (Hook C-8 universal).

## Round invariants check (5 applicable to batch_45)

| # | Invariant | Result | Evidence |
|---|---|---|---|
| 1 | atom_id collision check within batch | **PASS** | `grep -oE '"atom_id":"md_dmEX_assn_a[0-9]+"' \| sort -u \| wc -l` = 27 (= total atoms 27, 0 dupes) |
| 2 | Hook C-8 file prefix universal | **PASS** | `grep -c 'knowledge_base/' batch_45.jsonl` = 27/27 |
| 3 | H3a sub-namespace convention | **N/A** | EX/assumptions.md contains 0 H3 (`grep '^### ' EX/assumptions.md` → 0). Round 04 §0.5 row 19 expectation. |
| 4 | TABLE_HEADER Hook A1 span=1 | **N/A** | 0 TABLE atoms in EX/assumptions.md (`grep -c '"atom_type":"TABLE_HEADER"' batch_45.jsonl` = 0). |
| 5 | extracted_by consistency | **PASS** | All 27 atoms `subagent_type=general-purpose` + `prompt_version=P0_writer_md_v1.9.1`. |

**Effective applicable invariants**: 3/3 PASS (collision / Hook C-8 / extracted_by); 2/5 N/A by source structure (no H3, no TABLE).

## Round 03 carry-forward locks (applicable subset)

- **LIST_ITEM sib_idx=null lock**: all 26 LIST_ITEM atoms `sibling_index:null` confirmed (total `sibling_index:null` count = 27 = 1 HEADING H1 + 26 LIST_ITEM, 100%). **PASS**.
- **§2.4 multi-batch slice**: not applicable (single-batch single-file). **N/A**.
- **§2.6 FIGURE-in-domains lock**: 0 FIGURE atoms in batch_45 output (`grep -c '"atom_type":"FIGURE"' batch_45.jsonl` = 0; matches kickoff §0.5 row 14 grep 0 mermaid). **PASS**.
- **§2.7 numberless H2 in assumptions.md**: not applicable to batch_45 (EX/assumptions.md contains 0 H2; this lock applies at batch_50 FT/assumptions.md only). **N/A**.

## Coverage check (atom-vs-source line accounting)

- Source: 33 lines; non-blank content lines = 27 (lines 1, 3-14, 16-18, 20-21, 23-25, 27, 29-33).
- Writer atoms: 27 (1 H1 + 26 LIST_ITEM); each atom line_start=line_end, mapping 1:1 to a non-blank source line.
- Skipped lines = 6 (lines 2, 15, 19, 22, 26, 28) — all verified blank lines (separator gaps between numbered top-level items 1-6 + post-H1 + final-section pre-29). Correct atom-creation behavior (no blank-line atoms expected per writer convention).
- Atoms/line ratio = 27/33 = **0.818** (within round 04 §0.5 expectation 0.5-0.85; falls at upper range due to assumptions.md being almost entirely list content).

## Anti-flag / D-codified pattern accept

- a005 trailing-colon intro `... include the following:` is **NOT** a NOTE caption (no `**Note:**` / `**Exception:**` literal) — Hook D-NOTE-BQ negative case correctly classified as LIST_ITEM (per §R-D2 strict-NOTE carve-out). No reviewer flag.
- a002 / a014 / a017 / a019 / a022 / a023 numbered top-level items `^N\.\s+` correctly classified LIST_ITEM (NOT HEADING) per §R-D7.2 Axis 5 anti-flag accept. No reviewer flag.
- a020 / a015 multi-quote JSON-escaped strings correctly preserved byte-exact; no escape-doubling defect.

## Kickoff drift verification (per §R-D1)

- Kickoff §0.5 row 9 estimated atoms 17-28 for batch_45; actual 27 = within band (max).
- Kickoff §1 row 1 atom_id prefix `md_dmEX_assn_a` + parent_section `§EX [EX — Assumptions]` = matches writer output exactly.
- Kickoff §0.5 row 6 EX listed in domains/ alphabetical Round 04 first; correct.
- No kickoff drift flag for batch_45.

## Findings

**Findings**: 0 HIGH / 0 MEDIUM / 0 LOW.

No defects, no anomaly instances requiring D-codified accept-handling, no reviewer-noted style ambiguity. Output strictly conforms to:
- Schema v1.2.1 atom shape
- v1.9.1 writer prompt convention
- Round 03 LIST_ITEM sib_idx=null lock
- Round 04 §0.5 numeric estimates (atoms within 17-28 band)

## Final gate verdict

| Gate | Threshold | Actual | Result |
|---|---|---|---|
| Per-atom PASS rate | ≥90% | 100.0% (11/11) | PASS |
| Applicable invariants | All PASS | 3/3 PASS (2 N/A by structure) | PASS |
| Round 03 LIST_ITEM lock | All `sib_idx=null` | 26/26 LIST_ITEM null + 1 HEADING null | PASS |
| FIGURE in domains | 0 expected | 0 actual | PASS |
| atom_id collision | 0 | 0 | PASS |
| Hook C-8 file prefix | 27/27 | 27/27 | PASS |
| extracted_by consistency | uniform | uniform | PASS |
| atom count band | [17, 28] | 27 | PASS |

### **Final gate: PASS**

batch_45 is gate-cleared for round 04 cumulative inclusion. atom_id `md_dmEX_assn_a027` is the last batch_45 atom; batch_46 (EX/examples.md L1-232 sliced part 1) starts fresh `md_dmEX_ex_a001` per round 04 §2.5 (跨 file 不续号; only intra-file slicing per §2.4 maintains continuity).

---

*Audit complete 2026-05-06; reviewer Rule D 隔离 enforced (writer general-purpose ≠ reviewer pr-review-toolkit:code-reviewer); 11-atom Rule A sample 100% PASS; 5-of-5 round invariants PASS or N/A; 0 findings; gate PASS.*
