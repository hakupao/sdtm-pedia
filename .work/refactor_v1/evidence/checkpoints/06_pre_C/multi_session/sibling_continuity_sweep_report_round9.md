# Sibling Continuity Sweep Report — Round 9 Reconciler (post v1.5 cut, batches 38/39/40)

> Date: 2026-04-29
> Reconciler session: E (post B+C+D PARALLEL_SESSION_NN_DONE)
> Scope: cross-batch sibling continuity sweep §3 of `reconciler_kickoff_round9.md`
> Inputs: 6 sub-batch jsonl files (38a + 38b + 39a + 39b + 40a + 40b) covering p.371-400, 604 atoms total
> Verdict: PASS post Option H bulk fix (1 reconciler-side fix on cross-session canonical-form drift)

## §1 — Headline

| Sweep dimension | Pre-fix | Post-fix | Verdict |
|---|---|---|---|
| Total atoms scanned | 604 | 604 | — |
| 9-enum atom_type violations | 0 | 0 | PASS |
| atom_id pattern `^ig34_p\d{4}_a\d{3}$` violations | 0 | 0 | PASS |
| Duplicate atom_ids | 0 | 0 | PASS |
| Page coverage p.371-400 | 30 pages contiguous | 30 pages contiguous | PASS |
| **N15 .xpt-parent FORBID** violations | 0 | 0 | **PASS 1st INAUGURAL live-fire EFFECTIVE** |
| **N8 NEW9 L2 short-bracket FORBID** non-L3-HEADING violations | 0 | 0 | **PASS 2nd cumulative live-fire EFFECTIVE** |
| **N11 L1 chapter-short-bracket extension** L2 children parent | 2 atoms | 2 atoms | PASS 1st live-fire EFFECTIVE (§7.1 + §7.2 L2 children parent=`§7 [TRIAL DESIGN MODEL DATASETS]`) |
| **N6 INTRA-AGENT consistency cross-session** L6 + descendants canonical form | **37-atom drift detected in 39b** | 0 violations | **Option H bulk fix applied** |
| Pre-merge backup created | yes (`pdf_atoms.jsonl.pre-multi-38-40.bak`) | — | Rule B PASS |

## §2 — Cross-Batch Heading Chain Validation

### §2.1 §6.4 chapter L3 chain (closure batch 37→38)

| Sib | Verbatim | Source batch | Page |
|---|---|---|---|
| sib=1 | When to Use FA | batch 37 | p.361 |
| sib=2 | Naming | batch 37 | p.363 |
| sib=3 | Variables Unique | batch 37 | p.364 |
| sib=4 | FA | batch 37 | p.364 |
| sib=5 | **Skin Response (SR)** NEW | **batch 38** (p.375) | p.375 |
| — | (chapter §6.4 closes; §7 NEW chapter at p.382 batch 39) | — | — |

### §2.2 §6.4.4 FA L5 chain Examples (closure cross-batch 37→38)

| Sib | Verbatim | Source batch | Page |
|---|---|---|---|
| sib=1 | Example 1 | batch 37 | p.367-369 |
| sib=2 | Example 2 | batch 37 | p.369-370 |
| sib=3 | Example 3 | **batch 38** | p.371 |
| sib=4 | Example 4 | **batch 38** | p.372 |
| sib=5 | Example 5 | **batch 38** | p.373 |
| sib=6 | Example 6 | **batch 38** | p.374 |

Cross-batch INTRA-AGENT consistency: parent_section canonical 'FA – Examples' short-form preserved across batch 37 + batch 38 first-attempt (Branch A executor → executor across rounds; N6 consistency PASS).

### §2.3 §6.4.4 FA L6 caption-as-HEADING NEW round-9 precedent

| Sib | Verbatim | Source batch | Page |
|---|---|---|---|
| sib=1 | Rheumatoid Arthritis History | batch 38 | p.371 |
| sib=2 | Prespecified Adverse Events of Clinical Interest | batch 38 | p.372 |

First L6 textual-heading atoms in P1 cumulative for FA – Examples (caption-as-L6-HEADING for CRF table titles within Example 3 + Example 4 narratives; distinct from L3-group-container Examples-at-L6 pattern).

### §2.4 §6.4.5 SR L3-leaf domain inaugural (full L4 chain + L5 Examples)

| Level / sib | Verbatim | Source batch | Page |
|---|---|---|---|
| L3 sib=5 | §6.4.5 Skin Response (SR) NEW (parent=`§6.4 [FINDINGS ABOUT EVENTS OR INTERVENTIONS]` short-bracket per N11) | batch 38 | p.375 |
| L4 sib=1 | SR – Description/Overview | batch 38 | p.375 |
| L4 sib=2 | SR – Specification | batch 38 | p.376 |
| L4 sib=3 | SR – Assumptions | batch 38 | p.377 |
| L4 sib=4 | SR – Examples | batch 38 | p.378 |
| L5 sib=1 | Example 1 (Johnson grass IgE) | batch 38 | p.378 |
| L5 sib=2 | Example 2 (Dog Epi IgG) | batch 38 | p.378 |
| L5 sib=3 | Example 3 (Tuberculin PPD) | batch 38 | p.380 |

N9 L3-leaf-pattern L4 chain Description/Specification/Assumptions/Examples 2nd cumulative live-fire EFFECTIVE (FA + SR both leaf-pattern; CROSS-LEAF-DOMAIN VALIDATED). N10 L3-leaf Examples-at-L5 distinction 2nd cumulative live-fire EFFECTIVE.

### §2.5 §6.4.5 SR Examples table tail (cross-batch 38→39 head)

| Page | Atoms | Source batch | Note |
|---|---|---|---|
| p.381 | 5 (TABLE_ROW + SENTENCE) | **batch 39 (39a head)** | SR Example 3 Tuberculin PPD continuation table tail; parent='SR – Examples' canonical short-form preserved cross-session B→C |

### §2.6 §7 [TRIAL DESIGN MODEL DATASETS] L1 NEW chapter (FIRST L1 transition in P1 cumulative)

| Level / sib | Verbatim | Source batch | Page |
|---|---|---|---|
| **L1 sib=7 NEW** | **§7 Trial Design Model Datasets** (parent=`(SDTMIG v3.4)` document root) | **batch 39 (39a)** | **p.382** |
| L2 sib=1 | §7.1 Introduction to Trial Design Model Datasets (parent=`§7 [TRIAL DESIGN MODEL DATASETS]` N11 L1 chapter-short-bracket extension 1st live-fire) | batch 39 | p.382 |
| L3 sib=1 | §7.1.1 Purpose of the Trial Design Model | batch 39 | p.382 |
| L3 sib=2 | §7.1.2 Definitions of Trial Design Concepts | batch 39 | p.382 |
| L3 sib=3 | §7.1.3 Current and Future Contents of the Trial Design Model | batch 39 | p.383 |
| L2 sib=2 | §7.2 Experimental Design (TA and TE) (parent=`§7 [TRIAL DESIGN MODEL DATASETS]`) | batch 39 | p.384 |
| L3 sib=1 | §7.2.1 Trial Arms (TA) | batch 39 | p.384 |

**FIRST L1 CHAPTER TRANSITION IN P1 CUMULATIVE since project start.** N11 chapter-short-bracket extension to L1 = 1st live-fire EFFECTIVE post v1.4 codification.

### §2.7 §7.2.1 TA L4 leaf-pattern chain (cross-batch 39→40 continuation)

| L4 sib | Verbatim | Source batch | Page |
|---|---|---|---|
| sib=1 | TA – Description/Overview | batch 39 (39a) | p.384 |
| sib=2 | TA – Specification | batch 39 (39a) | p.384 |
| sib=3 | TA – Assumptions | batch 39 (39a) | p.385 |
| sib=4 | TA – Examples | batch 39 (39b) | p.386 |

N9 L3-leaf-pattern L4 chain 3rd cumulative live-fire EFFECTIVE (FA + SR + TA = 3 leaf-domains validated).

### §2.8 §7.2.1 TA L5 Examples chain (cross-batch 39→40 head + 40 deep-interior)

| L5 sib | Verbatim | Source batch | Page |
|---|---|---|---|
| sib=1 | Example 1 | batch 39 (39b) | p.387 |
| sib=2 | Example 2 | batch 39 (39b) | p.389 |
| sib=3 | Example 3 | batch 40 (40a) | p.392 |
| sib=4 | Example 4 | batch 40 (40a) | p.394 |
| sib=5 | Example 5 | batch 40 (40b) | p.397 |
| sib=6 | Example 6 | batch 40 (40b) | p.398 |
| sib=7 | Example 7 | batch 40 (40b) | p.399 |

N10 L3-leaf Examples-at-L5 distinction 3rd cumulative live-fire EFFECTIVE.

### §2.9 §7.2.1 TA L6 Trial Design Matrix sib=1 RESTART per Example chain (cross-session continuity)

| L6 sib=1 (RESTART per Example) | parent (post Option H fix) | Source batch | Page |
|---|---|---|---|
| Trial Design Matrix | `§7.2.1 Trial Arms (TA) – Example 1` | batch 39 (39b) | p.389 |
| Trial Design Matrix | `§7.2.1 Trial Arms (TA) – Example 2` | batch 40 (40a) | p.391 |
| Trial Design Matrix | `§7.2.1 Trial Arms (TA) – Example 3` | batch 40 (40a) | p.393 |
| Trial Design Matrix | `§7.2.1 Trial Arms (TA) – Example 4` | batch 40 (40b) | p.396 |
| Trial Design Matrix | `§7.2.1 Trial Arms (TA) – Example 5` | batch 40 (40b) | p.397 |
| Trial Design Matrix | `§7.2.1 Trial Arms (TA) – Example 6` | batch 40 (40b) | p.398 |

L6 'Trial Design Matrix' sib=1 RESTART discipline EFFECTIVE — 2nd cumulative live-fire of N10 leaf-pattern Examples-at-L5 + L6 sub-heading sib=1 RESTART per Example (round 8 batch 36 1st + round 9 batch 40 2nd live-fire = STRONGLY VALIDATED candidate post 2nd live-fire).

## §3 — Reconciler-Side Option H Bulk Fix (cross-session canonical-form drift in 39b)

### §3.1 Detection

Initial sweep of 6 sub-batch jsonl files surfaced cross-session canonical-form drift:
- **39b** (session C, p.387-390) emits 37 atoms with parent_section short-form `§7.2.1 TA – Example 1/2`
- **40a + 40b** (session D, p.391-400) consistently emit full-form `§7.2.1 Trial Arms (TA) – Example N`
- 39b's own L5 chain head atoms (Example 1+2 sib=1+2 + L4 atoms) use full-form `§7.2.1 Trial Arms (TA) – Examples`

**Internal 39b inconsistency**: L5 chain uses full-form, but L6 + descendants under L6 use short-form. The 30 atoms under L6 'Trial Design Matrix' Example 1 + 7 atoms under Example 2 (mostly child SENTENCE/FIGURE/TABLE_HEADER/TABLE_ROW/CODE_LITERAL/HEADING types) were affected.

### §3.2 Decision

Apply Option H bulk fix per kickoff §3 instructions: "Apply Option H any cross-batch sib gap / canonical-form drift / NEW9 violation / N15 .xpt-parent violation / N16 dispatch violation."

The full-form is the dominant convention (matches L4 chain `§7.2.1 Trial Arms (TA)` parent canonical full-form + L5 'Examples' parent + 40a/b convention). Fix changes 37 short-form atoms in 39b → full-form to align with cross-session convention.

This is a 1st reconciler-side cross-session canonical-form drift fix in P1 cumulative — extends round 7 batch 34 O-P1-115 LOW intra-batch sub-batch L4 canonical drift precedent to cross-session L6+descendants scope post v1.5 cut N16 same-family content-type-bound dispatch first-batch.

### §3.3 Fix execution

1. Pre-fix backup: `cp evidence/checkpoints/pdf_atoms_batch_39b.jsonl evidence/checkpoints/pdf_atoms_batch_39b.jsonl.pre-OptionH-form-drift.bak` ✓
2. Python bulk replace: `§7.2.1 TA – Example 1` → `§7.2.1 Trial Arms (TA) – Example 1` (30 atoms) + `§7.2.1 TA – Example 2` → `§7.2.1 Trial Arms (TA) – Example 2` (7 atoms) = 37 total atoms fixed
3. Post-fix sweep: 0 short-form residual + 59 full-form usages (37 fixed + 14 L5 Examples already full-form + 7 L4 Assumptions already full-form + 1 L4 baseline already full-form = 59/59 atoms in 39b consistent) ✓
4. Line count preserved: 59 atoms before + after fix ✓

### §3.4 Affected atom IDs (37 total)

| atom_id | atom_type | pre-fix parent | post-fix parent |
|---|---|---|---|
| ig34_p0387_a007..a012 (6 atoms) | SENTENCE / FIGURE | `§7.2.1 TA – Example 1` | `§7.2.1 Trial Arms (TA) – Example 1` |
| ig34_p0388_a001..a005 (5 atoms) | FIGURE / SENTENCE | `§7.2.1 TA – Example 1` | `§7.2.1 Trial Arms (TA) – Example 1` |
| ig34_p0389_a001..a019 (19 atoms) | SENTENCE / HEADING (L6 Trial Design Matrix sib=1) / TABLE_HEADER / TABLE_ROW / CODE_LITERAL | `§7.2.1 TA – Example 1` | `§7.2.1 Trial Arms (TA) – Example 1` |
| ig34_p0389_a021..a022 (2 atoms) | SENTENCE / FIGURE | `§7.2.1 TA – Example 2` | `§7.2.1 Trial Arms (TA) – Example 2` |
| ig34_p0390_a001..a005 (5 atoms) | SENTENCE / FIGURE | `§7.2.1 TA – Example 2` | `§7.2.1 Trial Arms (TA) – Example 2` |

## §4 — N15 / N16 / N17 v1.5 Compliance Summary

### §4.1 N15 .xpt-parent FORBID

- **Status**: 1st cumulative INAUGURAL live-fire EFFECTIVE
- **Coverage**: 604 atoms across 6 sub-batches scanned
- **Violations**: 0
- **.xpt CODE_LITERAL atoms catalogued** (all parented to L4 textual heading ancestor canonical, NOT to .xpt filename):
  - Batch 38 (FA + SR domains): mh.xpt, suppmh.xpt, faae.xpt, ae.xpt, face.xpt, relrec.xpt, sr.xpt, ex.xpt, ag.xpt
  - Batch 39 + 40 (TA domain): ta.xpt (referenced repeatedly across 7 Examples)
- **Evidence**: regex `^[a-z]+\.xpt$` 0 matches on parent_section field

### §4.2 N16 writer-family ban for examples_narrative_spec_table

- **Status**: 1st cumulative INAUGURAL live-fire EFFECTIVE for SAME content type; 5th cumulative writer-direction recurrence on NEW content type (mixed_structural_transition) where N16 PERMITS = scope INSUFFICIENT
- **Per-sub-batch dispatch verification**:
  - 38a (p.371-375 FA Examples 3-6 + §6.4.5 SR L3 NEW): content_type=examples_narrative_spec_table → executor MANDATORY → executor dispatched ✓
  - 38b (p.376-380 SR Spec table + Assumptions + Examples + cross-domain xpt tables): content_type=examples_narrative_spec_table → executor MANDATORY → executor dispatched ✓
  - 39a (p.381-385 §7 L1 + L2 + L3 NEW transitions): content_type=mixed_structural_transition → writer PERMISSIBLE / executor PREFERRED → executor dispatched ✓
  - 39b (p.386-390 TA Examples 1+2): content_type=examples_narrative_spec_table → executor MANDATORY → executor dispatched ✓
  - 40a (p.391-395 TA Examples 2-4): content_type=examples_narrative_spec_table → executor MANDATORY → executor dispatched ✓
  - 40b (p.396-400 TA Examples 4-7): content_type=examples_narrative_spec_table → executor MANDATORY → executor dispatched ✓
- **Drift cal batch 39 p.382** (mixed_structural_transition): writer rerun PERMISSIBLE per N16 free-choice → writer dispatched → **5th cumulative writer-direction VALUE HALLUCINATION recurrence detected** (URL .org→.ch + word `clinical` deletion + TABLE_ROW Study cell ~26% drift). N16 v1.5 ban scope INSUFFICIENT proof → v1.6 N16.b EMERGENCY-CRITICAL ESCALATION candidate filed.

### §4.3 N17 cross-row consistency hooks (Self-Validate hooks 14→17)

- **Status**: 1st cumulative INAUGURAL live-fire EFFECTIVE (writer self-claim layer)
- **Hook 15 cross-row TABLE_ROW pipe-count consistency**: writer self-report PASS for all 6 sub-batches (caveat: N17 OBS-4 v1.6 candidate identified — strict reading "same parent_section → same pipe-count" fails when one Example has multiple tables; refine to (parent_section, table_id) granularity)
- **Hook 16 cross-row USUBJID format consistency**: writer self-report PASS for all 6 sub-batches
- **Hook 17 multi-axis value-cell spot-check N=3**: writer self-report PASS for all 6 sub-batches (caveat: drift cal batch 39 p.382 disproved 3 atoms = Hook 17 detection-not-prevention; OBS-5 v1.6 candidate — expand sample N=3→N=10 OR mandatory cross-check for atoms with URLs/citations)

## §5 — Pre-Merge Backup + Sequential Merge

- **Pre-merge backup**: `.work/06_deep_verification/pdf_atoms.jsonl.pre-multi-38-40.bak` (9224 atoms baseline preserved per Rule B mandatory pre-merge)
- **Merge order**: 38a (129) → 38b (126) → 39a (86) → 39b (59 post Option H) → 40a (72) → 40b (132) = 604 atoms appended sequentially
- **Post-merge validation**:
  - Total atoms: 9224 + 604 = **9828** ✓
  - JSON parse: **9828/9828 valid, 0 errors** ✓
  - atom_id uniqueness: **0 duplicates** ✓
  - Page coverage: **1-400 contiguous, 0 missing, 0 extra** ✓

## §6 — Cumulative Sweep Counts (round 1-9)

| Sweep | Round 9 sweep contribution | Cumulative sweep total |
|---|---|---|
| Atoms scanned | 604 | 9828 |
| Pages covered | 30 | 400 |
| TOC anchor cumulative | n=30 (3 batches × 10 pages) | n=320 across 32 consecutive batches |
| Family pools sustained | +Explore INAUGURAL (10th family pool inaugural) | 11 active families post round 9 |
| AUDIT pivots cumulative | +3 (#49 + #50 + #51) | 32 |
| Reconciler-side Option H fixes | 1 (37 atoms canonical-form drift in 39b) | 1st reconciler-side cross-session canonical-form drift fix in P1 cumulative |
| Per-batch Option H fixes | 1 (NOTE→SENTENCE in batch 38) | 52 cumulative repair cycles across 22 batches |

## §7 — Verdict + Disposition

**Sweep verdict**: PASS post Option H bulk fix.

- 6 sub-batch jsonl files merged into root `pdf_atoms.jsonl` (9224 → 9828 atoms; 0 collision / 0 schema err / pages 1-400 unique / atom_id unique).
- 1 reconciler-side Option H bulk fix applied (37 atoms canonical-form drift in 39b; Rule B backup preserved).
- 0 INTRA-AGENT consistency violations remaining post-fix.
- 0 NEW9 violations / 0 N15 violations / 0 N16 dispatch violations / 0 N17 cross-row pipe-count or USUBJID violations.
- N11 chapter-short-bracket extension to L1 1st live-fire EFFECTIVE post v1.4 codification.
- N9 L3-leaf-pattern L4 chain + N10 L3-leaf Examples-at-L5 distinction 3rd cumulative live-fire EFFECTIVE (FA + SR + TA = 3 leaf-domains validated).

**Disposition**: Round 9 closure proceed to STEP 5 (audit_matrix.md update) + STEP 6 (_progress.json update) + STEP 7 (round 9 retro) + STEP 8 (commit + push) per kickoff §4-§8.

---

*Reconciler-side post-merge sweep complete 2026-04-29. v1.6 cut session candidacy STRONGLY RECOMMENDED before round 10 batch 42 next mandatory drift cal.*
