# Rule A Audit Summary — P2 B-03c Round 04 batch_46

> Audit run: 2026-05-06
> Reviewer subagent_type: `pr-review-toolkit:code-reviewer` (round 04 per-batch reviewer per kickoff §3)
> Reviewer prompt: `subagent_prompts/P0_reviewer_v1.9.1.md`
> Writer subagent_type: `general-purpose` (per atoms `extracted_by`)
> Rule D 隔离: writer ≠ reviewer subagent_type ✓

---

## Batch context

| Field | Value |
|---|---|
| Batch | batch_46 (sliced part 1 of 2 — round 03 §2.4 carry-forward second application) |
| Source | `knowledge_base/domains/EX/examples.md` lines 1-232 (Ex1..Ex5) |
| Writer output | `evidence/checkpoints/P2_B-03_batch_46_md_atoms.jsonl` |
| Atom count actual | **144** atoms |
| Atom count estimated | 116-197 (§4 halt band [58, 296]) |
| atom_id range | `md_dmEX_ex_a001`..`md_dmEX_ex_a144` (a145 reserved for batch_47 first atom) |
| Atoms/line ratio | 144/232 = 0.621 (mid-range vs round 04 expected 0.5-0.85) |
| atom_type distribution | 6 HEADING (1 H1 + 5 H2) / 18 TABLE_HEADER / 69 TABLE_ROW / 7 LIST_ITEM / 44 SENTENCE / 0 FIGURE / 0 NOTE / 0 CODE_LITERAL |

---

## Sample plan executed

**18 verdicts** (8 boundary + 10 stratified, exceeds v1.9.1 §B-2 minimum 11):

### Boundary atoms (8)
| atom_id | role | line | type |
|---|---|---|---|
| a001 | first H1 file root | 1 | HEADING |
| a002 | inline Note SENTENCE (Hook D-NOTE-BQ negative) | 3 | SENTENCE |
| a003 | first H2 Ex1 | 5 | HEADING |
| a034 | H2 Ex2 boundary | 59 | HEADING |
| a067 | H2 Ex3 boundary | 109 | HEADING |
| a093 | H2 Ex4 boundary | 148 | HEADING |
| a104 | H2 Ex5 boundary | 165 | HEADING |
| a144 | last atom (slice boundary) | 231 | TABLE_ROW |

### Stratified atoms (10)
| atom_id | role | line | type |
|---|---|---|---|
| a004 | long SENTENCE (325 ch, density check) | 7 | SENTENCE |
| a007 | TABLE_HEADER v1.9 standard 2-row | 13-14 | TABLE_HEADER |
| a033 | last atom of §EX.1 (cross-Example transition) | 57 | TABLE_ROW |
| a040 | TABLE_ROW with trailing empty cell (R12 lock) | 69 | TABLE_ROW |
| a066 | last atom of §EX.2 (cross-Example transition) | 107 | TABLE_ROW |
| a069 | LIST_ITEM with sib_idx=null (R03 lock) | 113 | LIST_ITEM |
| a092 | last atom of §EX.3 (cross-Example transition) | 146 | TABLE_ROW |
| a103 | last atom of §EX.4 (cross-Example transition) | 163 | TABLE_ROW |
| a142 | TABLE_HEADER relrec Ex5 v1.9 standard 2-row | 228-229 | TABLE_HEADER |
| a143 | penultimate atom relrec | 230 | TABLE_ROW |

---

## PASS rate

**18 / 18 = 100% PASS** (weighted, all atoms full PASS — 0 HIGH, 0 MEDIUM, 0 LOW findings).

---

## 5 round invariants (kickoff §6 carry-forward)

| # | Invariant | Result | Evidence |
|---|---|---|---|
| 1 | atom_id collision check within batch | **PASS** 0 collision | python3 dedupe verified `len(set(ids))==144` |
| 2 | Hook C-8 file prefix universal `knowledge_base/` | **PASS** 144/144 | tally `files: {'knowledge_base/domains/EX/examples.md': 144}` |
| 3 | H3a sub-namespace convention | **N/A PASS** 0 H3 atoms | source L1-232 grep `^### ` = 0; expected per kickoff §0.5 row 14-style scope |
| 4 | TABLE_HEADER Hook A1 v1.9 2-row standard (line_end-line_start=1) | **PASS** 18/18 | `Counter({1: 18})` for all TABLE_HEADER atoms |
| 5 | extracted_by consistency (subagent_type=general-purpose, prompt_version=P0_writer_md_v1.9.1) | **PASS** 144/144 | tally `extracted: {('general-purpose','P0_writer_md_v1.9.1'): 144}` |

**5/5 invariants PASS.**

---

## Round 03 carry-forward locks

| Lock | Result | Evidence |
|---|---|---|
| LIST_ITEM sib_idx=null | **PASS** 7/7 | a069..a072, a083..a085 全 sib_idx=null |
| §2.4 multi-batch slice — atom_id starts a001 | **PASS** | first atom a001, last atom a144 (slice part 1 contract met; batch_47 will continue from a145) |
| §2.4 multi-batch slice — last line_end ≤ 232 | **PASS** | a144 line_end=231 ≤ 232 ✓ |
| §2.6 FIGURE-in-domains | **PASS** 0 FIGURE | atom_type tally has 0 FIGURE entry |
| §2.7 numberless H2 in assumptions.md | **N/A** | batch_46 is examples.md (not assumptions.md); §2.7 first applies in batch_50 FT/ass |

---

## Hook D-NOTE-BQ negative case (kickoff §0.5 row 13) — verified

a002 verbatim L3 source `Note: Examples for EX and EC are shared in Section 6.1.3.3 of the SDTMIG. See also [EC Examples](../EC/examples.md).`

- Source has **no `>` blockquote prefix** (inline plain text starting `Note:` not `> **Note:**`)
- Per v1.9.1 §R-D2 / Hook D-NOTE-BQ: blockquote-prefix `> **Note:** ` triggers atom_type=NOTE; inline non-blockquote = SENTENCE
- Writer atom_type = **SENTENCE** ✓ (correct per Hook negative case)
- cross_refs `["Section 6.1.3.3", "EC/examples.md"]` populated per §R-D7.3 ✓

---

## Cross-Example parent_section transition verified

5 transitions checked (a033→a034, a066→a067, a092→a093, a103→a104; plus initial a001/a002→a003):

- All H2 atoms (a003/a034/a067/a093/a104) have parent_section=`§EX [EX — Examples]` (root, attaching H2 to file-root parent)
- All children of each H2 (e.g. a004 first child of Ex1) have parent_section=`§EX.N [Example N]` self-namespace
- a002 (pre-H2 inline Note SENTENCE) parent_section=`§EX [EX — Examples]` root (correct for pre-first-H2 prefatory)
- Last atoms of each Ex (a033/a066/a092/a103/a144) have parent_section=`§EX.N [Example N]` (still in their respective Example's sub-namespace before next H2)

**0 parent_section transition errors.**

---

## Kickoff drift verification (per v1.9.1 §R-D1)

- batch report: no kickoff_doc_drift_detected flag; kickoff §0.5 20/20 PASS
- writer atoms vs source byte-exact: 18/18 sampled PASS
- No drift fault attributable to writer; INFO no-op.

---

## Findings

**HIGH severity**: 0
**MEDIUM severity**: 0
**LOW severity**: 0

No issues identified. Per v1.9.1 §R-Stratified-Sampling D-codified anomaly check: a002 inline Note SENTENCE properly handled (D-NOTE-BQ negative case canonical, NOT NOTE atom_type). All round 03 carry-forward locks honored.

---

## Final gate verdict

**BATCH_46 RULE A — PASS** (weighted 100%, 5/5 invariants, 0 findings)

Continue autonomous run to batch_47 (EX/examples.md slice part 2, L233-434, atom_id continues from a145).
