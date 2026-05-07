# Rule A Audit Summary — P2 B-03c Round 10 batch_108 (SM/assumptions.md)

> Date: 2026-05-07
> Reviewer prompt: `subagent_prompts/P0_reviewer_v1.9.3.md` (35 hooks)
> Source: `knowledge_base/domains/SM/assumptions.md` (13 lines, 0 H2, file-root)
> Atoms: `evidence/checkpoints/P2_B-03_batch_108_md_atoms.jsonl` (10 atoms claimed)
> Round 10 context: v1.9.3 1st production validation round (post commit 6990c54); 0 §2.11 Plan B trigger expected; §F-1 backward compat verification.

## Verdict

**PASS — 10/10 atoms PASS (100%); 0 HIGH severity finding; 0 schema regression; 0 atom_id collision.**

## Per-check matrix

| # | Check | Result |
|---|---|---|
| 1 | atom_id sequential a001..a010 (10 atoms, 0 collision) | ✓ PASS |
| 2 | file path `knowledge_base/domains/SM/assumptions.md` (10/10) | ✓ PASS |
| 3 | parent_section `§SM [SM — Assumptions]` ALL 10 atoms (file-root, 0 H2) | ✓ PASS |
| 4 | line ranges within [1, 13] | ✓ PASS |
| 5 | atom_type ∈ 9 valid types (HEADING ×1 + LIST_ITEM ×9) | ✓ PASS |
| 6 | verbatim byte-exact (incl indented sub-items L6/L7/L10/L11/L12/L13 3-space preserved) | ✓ PASS 10/10 |
| 7 | §E-2 a001 H1 hl=1 sib=1 (R-2.8-1) | ✓ PASS |
| 8 | §E-5 LIST_ITEM hl=null AND sib=null EXPLICIT (9 atoms) | ✓ PASS 9/9 |
| 9 | §E-4 extracted_by object schema (subagent_type/prompt_version/ts) | ✓ PASS 10/10 |
| 10 | prompt_version = `P0_writer_md_v1.9.3` | ✓ PASS 10/10 |
| 11 | 12 fields per atom (no missing/extra) | ✓ PASS 10/10 |
| 12 | §F-3 nested-list: 3 parent items + 6 sub-items = 9 LIST_ITEM (NOT compressed) | ✓ PASS |
| 13 | cross_refs a002 ["TM"] verified TM mentioned in L3 source ("TM dataset") | ✓ PASS |

## §R-E1 Schema regression sweep PRIORITY 1

✓ PASS — 0 schema regression. All 10 atoms preserve 12-field schema. R-2.8-1 (H1 hl=1 sib=1) ✓; R-2.8-2 N/A (no TABLE_HEADER); R-2.8-3 (extracted_by object) ✓; MED-01 (LIST_ITEM hl+sib explicit null) ✓.

## §R-F-1 §2.11 Plan B sub-namespace verification (HIGH)

**N/A trigger — 0 §F-1 trigger.** Source has 0 H2 (file-root only). Backward compat verification: file-root namespace pattern preserved (10/10 atoms `§SM [SM — Assumptions]`), consistent with round 04 §2.7 lock + round 08 0-trigger pattern. Round 10 §F-1 backward compat 1st production validation — PASS.

## §R-F-2 atoms/line ratio retrospective (INFO non-blocking)

ratio = 10/13 = **0.769** — IN BAND (empirical 0.59-0.85). Mid-upper range for ass.md with 3-level nested LIST (1 simple parent + 2 parent-with-children @ 2/4 sub-items respectively). Non-blocking.

## §R-F-3 Kickoff atom estimate calibration (INFO non-blocking)

Kickoff §0.5 row 25 / §1 row 5: est=7-11 (mid 9), actual=10. delta_pct = abs(10-9)/9 × 100 = **11.1%** — well within 50% threshold. Non-blocking. Estimate well-calibrated for small ass.md with nested-list.

## Spot-check 2 atoms (independent re-verify)

**a002 (L3 parent 1 — most-content atom)**: verbatim re-read from source L3 byte-by-byte; matches `"1. Disease milestones are observations or activities whose timings are of interest in the study. The types of disease milestones are defined at the study level in the TM dataset. The purpose of the SM dataset is to provide a summary timeline of the milestones for a particular subject."` exactly. cross_refs ["TM"] ← `TM dataset` substring verified at L3 char ~165. parent_section file-root correct. hl=null sib=null explicit. ✓ PASS.

**a007 (L10 sub-item a under parent 3 — indented sub-item with nested quote)**: verbatim re-read from source L10 byte-by-byte; matches `"   a. The start date/time of the disease milestone is the critical date/time, and must be populated. If the disease milestone is an event, then the meaning of \"start date\" for the event may need to be defined."` exactly (3-space indent + escaped double-quotes preserved in JSON). parent_section file-root §SM correct (§F-3 nested-list expanded NOT compressed). ✓ PASS.

## file-root namespace verification (all 10 atoms)

10/10 atoms parent_section = `§SM [SM — Assumptions]` — consistent with §2.7 file-root convention for 0-H2 ass.md (round 04 lock sustained). 0 H2 in source (grep verified §0.5 row 16). 0 §F-1 trigger.

## §F-3 nested-list correct count

3 parent items (L3, L5, L9 — items 1/2/3) + 6 sub-items (L6/L7 a/b under item 2 + L10/L11/L12/L13 a/b/c/d under item 3) = **9 LIST_ITEM atoms**. Each sub-item is a separate atom (NOT compressed into parent). ✓ §F-3 lock correctly applied.

## cross_refs sanity

- a002: ["TM"] — TM dataset reference at L3 verified ✓
- a006 (L9): [] — SMSTDTC/SMENDTC/SMSTDY/SMENDY are SM self-domain variables, NOT cross-domain refs (correctly excluded) ✓
- All other 8 atoms: [] — no cross-domain refs in source content ✓

## HIGH findings

**NONE.** 0 HIGH severity findings. 0 schema regression. 0 atom_id collision.

## §F-2 INFO

Cumulative round 10 ratio band tracker (post batch_108): batches 104-108 atoms 6+11+13+22+10 = 62; lines 11+47+21+38+13 = 130; sub-ratio = 0.477. Note: batch_108 individual ratio 0.769 in band; cumulative round-level needs all 10 batches before §F-2 round-close mini-audit fires per v1.9.3 §R-F-2 rule.

## Halt status

**No halt triggered.** PASS rate 100% (≥ 90% threshold). 0 HIGH severity. 0 schema regression. 0 collision. Round 10 may proceed to batch_109 (SM/examples.md) per dispatch order.
