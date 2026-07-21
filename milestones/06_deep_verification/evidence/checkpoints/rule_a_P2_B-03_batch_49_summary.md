# Rule A audit — P2 B-03 batch_49 (FA/examples.md)

> Audit date: 2026-05-06
> Reviewer subagent_type: pr-review-toolkit:code-reviewer (round 04 per-batch default per kickoff §3)
> Writer subagent_type: general-purpose (per atom extracted_by) — Rule D 隔离 ≠ reviewer ✓
> Source: `knowledge_base/domains/FA/examples.md` (244 lines)
> Writer output: `evidence/checkpoints/P2_B-03_batch_49_md_atoms.jsonl` (159 atoms)
> Prompt version: P0_writer_md_v1.9.1 / P0_reviewer_v1.9.1

## §1 Sample plan executed

| # | Category | atom_id | Rationale |
|---|---|---|---|
| 1 | boundary | md_dmFA_ex_a001 | H1 file root sib=1 (universal lock) |
| 2 | boundary | md_dmFA_ex_a002 | first H2 §FA.1 (sib=1) |
| 3 | boundary | md_dmFA_ex_a003 | first SENTENCE under §FA.1 (parent_section transition) |
| 4 | boundary | md_dmFA_ex_a037 | H2 §FA.2 (sib=2) |
| 5 | boundary | md_dmFA_ex_a065 | H2 §FA.3 (sib=3) |
| 6 | boundary | md_dmFA_ex_a082 | H2 §FA.4 (sib=4) |
| 7 | boundary | md_dmFA_ex_a104 | H2 §FA.5 (sib=5) |
| 8 | boundary | md_dmFA_ex_a131 | H2 §FA.6 (sib=6) |
| 9 | boundary | md_dmFA_ex_a159 | last atom (TABLE_ROW L244) |
| 10 | stratified | md_dmFA_ex_a006 | TABLE_HEADER L11-12 Hook A1 span=1 verify |
| 11 | stratified | md_dmFA_ex_a142 | TABLE_ROW L217 cell preservation verify |
| 12 | stratified | md_dmFA_ex_a134 | LIST_ITEM sib_idx null (round 03 lock) verify |
| 13 | stratified | md_dmFA_ex_a136 | L205 italic `*Note:...*` — SENTENCE (Hook D-NOTE-BQ negative) verify |
| 14 | stratified | md_dmFA_ex_a013 | L25 bold-caption `**Rows 1, 6, 11:**` — SENTENCE (§R-D5 accept) verify |

Total verdicts: **14** (8 boundary + 6 stratified — exceeded prompt minimum 8+5=13 by adding one more boundary at first SENTENCE under H2 boundary).

## §2 Verdict roll-up

| Verdict | Count | Atoms |
|---|---|---|
| PASS | **14/14** | all |
| FAIL | 0 | — |

**PASS rate: 14/14 = 100.0%**

## §3 Round invariants (5)

| # | Invariant | Result | Detail |
|---|---|---|---|
| 1 | atom_id collision | **PASS** | 159/159 unique IDs |
| 2 | Hook C-8 file prefix `knowledge_base/` | **PASS** | 159/159 atoms have `knowledge_base/domains/FA/examples.md` |
| 3 | H3a sub-namespace | **N/A** | 0 H3 atoms (round 04 source 12 files grep 实证 0 H3 — expected behaviour) |
| 4 | TABLE_HEADER Hook A1 span=1 | **PASS** | 15/15 TABLE_HEADER atoms satisfy `line_end - line_start == 1` (v1.9 standard 2-row header+alignment) |
| 5 | extracted_by consistency | **PASS** | 159/159 = `{prompt_version: P0_writer_md_v1.9.1, subagent_type: general-purpose, ts: 2026-05-06T08:00:00Z}` |

**Invariants: 5/5 PASS** (invariant 3 N/A since 0 H3 atoms in batch — expectation met).

## §4 Atom-type distribution

| Type | Count | Expected (kickoff) | Match? |
|---|---|---|---|
| HEADING (H1+H2) | 7 | 1 + 6 = 7 | ✓ |
| TABLE_HEADER | 15 | 15 | ✓ |
| TABLE_ROW | 76 | 76 | ✓ |
| LIST_ITEM | 2 | 2 | ✓ |
| SENTENCE | 59 | 59 | ✓ |
| FIGURE | 0 | 0 (round 04 expected) | ✓ |
| NOTE | 0 | 0 (no blockquote `> **Note:**`) | ✓ |
| **Total** | **159** | **159** | ✓ |

## §5 H2 boundary line verification

Kickoff §2 noted 6 H2 at lines `3 / 57 / 99 / 127 / 162 / 197 sib=1..6`. Verified byte-exact via source:

| sib_idx | atom_id | source line | verbatim |
|---|---|---|---|
| 1 | a002 | L3 | `## Example 1` ✓ |
| 2 | a037 | L57 | `## Example 2` ✓ |
| 3 | a065 | L99 | `## Example 3` ✓ |
| 4 | a082 | L127 | `## Example 4` ✓ |
| 5 | a104 | L162 | `## Example 5` ✓ |
| 6 | a131 | L197 | `## Example 6` ✓ |

All 6/6 H2 line offsets and sib_idx PASS.

## §6 Special checks

### §6.1 a001 H1 sib_idx=1 (universal precedent)
Verified per round 01-04 sustained lock. Sampled past batches batch_25/42/43/44 all show H1 sib=1. Atom a001 sib=1 = canonical. PASS.

(Note: kickoff §2.7 example showed `sibling_index: null` for the H1 line in the FT/ass illustration. That is documentation drift — actual round 01-04 H1 atoms uniformly use sib=1. This is a kickoff §2.7 doc-snippet drift, NOT a writer atom defect. Writer correctly followed established convention. INFO-level only; recommend orchestrator note for kickoff §2.7 doc cleanup before batch_50 dispatch.)

### §6.2 All under-Ex atoms parent_section = `§FA.N [Example N]`
Verified atoms a003-a036 all parent=`§FA.1 [Example 1]`; a038-a064 all `§FA.2`; a066-a081 all `§FA.3`; a083-a103 all `§FA.4`; a105-a130 all `§FA.5`; a132-a159 all `§FA.6`. PASS.

### §6.3 L205 italic `*Note:...*` → SENTENCE (Hook D-NOTE-BQ negative)
Source L205 = italic single-asterisk pair `*Note: ... Interventions.*` (NOT blockquote `> **Note:** `). Per Hook D-NOTE-BQ in v1.9.1 §R-D2: only blockquote-prefix bold-Note triggers atom_type=NOTE. Writer correctly emitted atom_type=SENTENCE for a136. PASS.

### §6.4 0 FIGURE atoms (round 04 §2.6 lock)
Verified: 0/159 atoms have atom_type=FIGURE. Matches kickoff §0.5 row 14 grep claim of 0 mermaid in 12 round 04 source files. PASS.

### §6.5 LIST_ITEM sib_idx null (round 03 lock)
Verified: 2/2 LIST_ITEM atoms (a134, a135 at L202/L203 under §FA.6) have `sibling_index: null`. Round 03 lock enforced. PASS.

### §6.6 Bold-caption SENTENCE accept (§R-D5)
Source contains many `**Rows N, M:**` and `**Row N:**` captions (L25, L26, L105, L106, L131, L132, L133, L134, L158, L160, L170-175, L222, L224). Writer treated all as SENTENCE (not HEADING / not NOTE) per §R-D5. Sampled a013 (L25 first occurrence) verified PASS. PASS.

## §7 Kickoff drift verification (Hook R24 / §R-D1)

No `kickoff_doc_drift_detected` flag in batch report. Kickoff §0.5 numeric claims line-up with reviewer-side independent grep:
- 244 source lines ✓ (`wc -l knowledge_base/domains/FA/examples.md` = 244)
- 6 H2 at L3/57/99/127/162/197 ✓ (verified byte-exact)
- 0 mermaid blocks in source ✓ (no FIGURE atoms produced)
- atom count 159 within est range 122-207 ✓

No kickoff drift detected affecting writer atoms.

Minor INFO note (§6.1): kickoff §2.7 illustrative JSONC example shows H1 file root with `sibling_index: null`; the actual round 01-04 enforced lock is H1 sib=1. The example is a documentation excerpt for the §2.7 numberless H2 case in FT/ass and contains an inconsistency with the H1 row inside it. Writer batch_49 correctly used sib=1, so no atom defect. Recommend orchestrator clarify §2.7 example before batch_50 (FT/ass §2.7 first-time application) dispatches.

## §8 Findings summary

- HIGH severity: **0**
- MEDIUM severity: **0**
- LOW severity: **0**
- INFO: **1** (kickoff §2.7 example H1 sib_idx illustrative drift — not writer-attributable; orchestrator-side doc clean before batch_50)

## §9 Final verdict

- Per-batch Rule A audit: **14/14 = 100.0% PASS** (≥ 90% gate threshold)
- 5/5 round invariants PASS (invariant 3 N/A: 0 H3 atoms — expected)
- 0 HIGH/MEDIUM/LOW findings
- 1 INFO routed to orchestrator (kickoff §2.7 doc drift, not writer-attributable)

**Batch 49 Rule A audit: PASS**

---

BATCH_49_RULE_A PASS rate=100.0% invariants=5/5 findings=[INFO:kickoff_§2.7_example_H1_sib_idx_drift_routed_to_orchestrator_not_writer_attributable]
