# P1 Batch 25 Report — ig34 p.241-250 (multi-session round 4 session D)

> Session D parallel run (multi-session round 4), 2026-04-26.
> Scope: §6.3.5.6 Laboratory Test Results (LB) NEW + §6.3.5.7 Microbiology Domains group NEW (DOUBLE sub-domain transition).

## Final outcome

**PARALLEL_SESSION_25_DONE atoms=210 failures=0 repair_cycles=0 rule_a=100% drift_cal=skipped findings_added=O-P1-75**

## Section coverage

| Page | Section | New atoms | Transition |
|------|---------|----------:|------------|
| 241  | §6.3.5.6 LB L4 NEW + LB-Description L5 head | 25 | §6.3.5.5 IS → §6.3.5.6 LB sub-domain transition |
| 242  | LB-Specification L5 + LB spec table | 22 | — |
| 243  | LB spec table cont (LBSTNRHI etc) | 18 | — |
| 244  | LB spec table cont (LBCLSIG etc) | 20 | — |
| 245  | LB Assumptions list (numbered items) | 15 | — |
| 246  | LB Examples (Rows 2-3 alkaline phosphatase) | 15 | — |
| 247  | LB Examples cont + lb.xpt CODE_LITERAL | 22 | — |
| 248  | LB Example 4+5 tail + §6.3.5.7 Microbiology Domains L4 NEW + §6.3.5.7.1 MB L5 NEW + MB-Description L6 head | 27 | §6.3.5.6 LB → §6.3.5.7 Microbiology Domains group container transition |
| 249  | MB-Specification L6 + mb.xpt CODE_LITERAL + MB spec table head | 21 | — |
| 250  | MB spec table cont (MBDIR/MBMETHOD/MBLOBXFL etc) | 25 | — |

Total: **210 atoms** (sub-batch 25a=100, sub-batch 25b=110).

## Atom type breakdown (cumulative across 25a + 25b)

| atom_type | count |
|-----------|------:|
| TABLE_ROW | 132 |
| LIST_ITEM | 32 |
| SENTENCE  | 16 |
| CODE_LITERAL | 10 |
| TABLE_HEADER | 10 |
| HEADING   | 9 |
| NOTE      | 1 |
| **Total** | **210** |

## Schema validation

| Check | Result |
|-------|--------|
| JSON parse errors | 0 |
| BAD atom_type (non-9-enum) | 0 |
| BAD atom_id format | 0 |
| Frame tags (`</content>`, `<output>`) in verbatim | 0 |
| Within-batch dup atom_ids | 0 |
| Cross-batch collision vs root pdf_atoms.jsonl (5502 atoms) | 0 |

## NEW6.b L4 self-parent sweep (round-3 batch-22 O-P1-64 lesson codified)

| Atom | parent_section assigned | Verdict |
|------|-------------------------|---------|
| ig34_p0241_a023 §6.3.5.6 LB L4 HEADING | `§6.3.5 Specimen-based Findings Domains` | PASS (NOT self-parent) |
| ig34_p0248_a023 §6.3.5.7 Microbiology Domains L4 HEADING | `§6.3.5 Specimen-based Findings Domains` | PASS (NOT self-parent) |

**Result**: 0 violations. Round-3 lesson successfully codified into round-4 kickoff prepend → no recurrence in DOUBLE-transition batch.

## NEW7 deep-nesting + round-4 L5 RESTART precedent

§6.3.5.7 Microbiology Domains is a **group container** (plural "Domains" — similar to §6.3.5 itself but at L4 level). Internal sub-domain §6.3.5.7.1 MB therefore **RESTARTS at L5 sib=1** under §6.3.5.7 (parent='§6.3.5.7 Microbiology Domains' L4 group canonical). MB own internal sub-sections then RESTART at L6:

| Atom | level | sib | parent_section | Verdict |
|------|-------|-----|----------------|---------|
| ig34_p0248_a025 §6.3.5.7.1 MB L5 HEADING | 5 | 1 | `§6.3.5.7 Microbiology Domains` | PASS (NEW round-4 precedent verified) |
| ig34_p0248_a026 MB-Description L6 HEADING | 6 | 1 | `§6.3.5.7.1 Microbiology Specimen (MB)` | PASS |
| ig34_p0249_a001 MB-Specification L6 HEADING | 6 | 2 | `§6.3.5.7.1 Microbiology Specimen (MB)` | PASS |

This **NEW** structural pattern is recorded as **O-P1-75 INFO finding** for v1.4 codification.

## R12 DOUBLE-transition discipline

| Transition | Page | Atoms | Threshold | Verdict |
|------------|------|------:|----------:|---------|
| §6.3.5.5 IS → §6.3.5.6 LB | p.241 | 25 | ≥8 | PASS |
| §6.3.5.6 LB → §6.3.5.7 Microbiology Domains | p.248 | 27 | ≥8 | PASS |

3-zone partition confirmed on both transitions (prior-section tail / new-section L4 HEADING + intro / new-section L5+ chain head).

## R15 cross-batch sibling continuity

- §6.3.5.6 LB L4 sib=6 (batch 25 NEW) — contiguous from §6.3.5.5 IS L4 sib=5 (batch 23 sister NEW)
- §6.3.5.7 Microbiology Domains L4 sib=7 (batch 25 NEW) — contiguous from §6.3.5.6 LB L4 sib=6 (within batch 25)

Reconciler will validate full cross-session R15 chain post-merge.

## Density alarm check (G-MS-12 round 2+3 spec)

- Lowest per-page atoms: **p.245=15 + p.246=15** (exactly at 15-atom floor, NOT below)
- Sub-batch 25a total: 100 (at 100-atom floor)
- Sub-batch 25b total: 110 (above 100-atom floor)
- **Alarm NOT triggered** — density distribution healthy across DOUBLE-transition batch
- Main-session PDF cross-check NOT required

## Rule A audit (slot #34 feature-dev:code-architect, AUDIT-mode pivot 15th)

- Sample: 10 atoms (1/page p.241-250), seed=20260530, stratified 4 TABLE_ROW + 3 HEADING + 2 LIST_ITEM + 1 CODE_LITERAL
- Reviewer: feature-dev:code-architect (AUDIT-mode pivot 15th, **feature-dev family 3rd burn = pool COMPLETED** post round 4)
- Tools adaptation: write-tool-less + no-Bash inline content (per round 3 batch 20 #29 plugin-dev:skill-reviewer sub-pattern); reviewer produced verdicts.jsonl + summary.md content inline; main session wrote files preserving content verbatim
- Verdict: **10/10 PASS, weighted 100%** — exceeds ≥90% threshold by 10pp margin
- Per-dimension: atom_type 10/10 PASS / verbatim 10/10 PASS / parent_section 10/10 PASS / heading_fields 3/3 PASS + 7 N/A
- TOC anchor methodology cumulative: **n=150 atoms / 0 FP / 0 inversion / 15 consecutive batches** firmly locked

## Drift calibration

**SKIPPED** per round 4 cadence — last cal batch 21 (p.205), next mandatory batch 27 (every-3-batches batch 24→27); cumulative atoms post-p.220 below ≥300 trigger threshold for batch 25; batch 24 sister session covers cadence drift cal mandatory slot.

## Findings (O-P1-75..78 reserved range, 1 used)

### O-P1-75 INFO — Round-4 NEW deep-nesting precedent: L5 sub-domain RESTART under L4 group container

**Scope**: ig34_p0248_a025 §6.3.5.7.1 Microbiology Specimen (MB) L5 HEADING + downstream MB body p.248-250

**Pattern**: §6.3.5.7 Microbiology Domains is a GROUP CONTAINER (plural "Domains" similar to §6.3.5 itself but at L4 level). Internal sub-domain §6.3.5.7.1 MB therefore RESTARTS at L5 sib=1 under §6.3.5.7 (parent='§6.3.5.7 Microbiology Domains' L4 group canonical full-form). MB own internal sub-sections (Description/Specification etc) then RESTART at L6 sib=1..N under §6.3.5.7.1 MB.

**Application**: Extends NEW7 deep-nesting model. Previously L5 chain was Description/Specification/Assumptions/Examples directly under L4 sub-domain (e.g. LB-Description L5 sib=1 under §6.3.5.6 LB). NEW round-4 case: when L4 is a group container, internal sub-domains §N.N.N.N RESTART at L5, with L6 chain underneath.

**v1.4 candidate**: Codify NEW7 with two branches — "L4 sub-domain" (no sub-domains, L5 chain head Description/Specification/Assumptions/Examples) vs "L4 group container" (plural like §6.3.5.7 Microbiology Domains, L5 RESTART for internal sub-domains §N.N.N.N, then L6 chain head under each).

## Files written

| File | Size | Purpose |
|------|------|---------|
| `evidence/checkpoints/pdf_atoms_batch_25a.jsonl` | 100 atoms | Writer 25a output (p.241-245) |
| `evidence/checkpoints/pdf_atoms_batch_25b.jsonl` | 110 atoms | Executor 25b output (p.246-250) |
| `evidence/checkpoints/_progress_batch_25.json` | full schema | Sub-progress + round_4_compliance |
| `evidence/checkpoints/P1_batch_25_report.md` | this file | Full batch report |
| `evidence/checkpoints/rule_a_batch_25_sample.jsonl` | 10 atoms | Rule A sample seed=20260530 |
| `evidence/checkpoints/rule_a_batch_25_verdicts.jsonl` | 10 verdicts | slot #34 feature-dev:code-architect inline-captured |
| `evidence/checkpoints/rule_a_batch_25_summary.md` | summary | Rule A summary inline-captured |

## Files NOT touched (留给 reconciler)

- root `pdf_atoms.jsonl`
- `audit_matrix.md`
- `_progress.json`
- sister batch files (`pdf_atoms_batch_23*`, `pdf_atoms_batch_24*`)
- `subagent_prompts/*` (v1.3 cut deferred 4th time per Rule D)
- `schema/*.json` / `PLAN.md` / `plans/*.md`
- `CLAUDE.md` / MEMORY / project meta files

## Round 4 compliance summary

| Gate | Status |
|------|--------|
| G-MS-4 halt fallback decision tree | spec'd; NOT triggered |
| G-MS-7 finding ID range pre-allocation | compliant (O-P1-75..78 reserved, 1 used) |
| G-MS-11 NEW6 dual-form codification | applied; 0 violations |
| G-MS-11.b round 3 extension (L4 self-parent) | applied; 0 recurrence (DOUBLE-transition batch) |
| G-MS-12 density alarm check | applied; alarm NOT triggered |
| G-MS-13 finding ID range cross-validation table | applied; 0 collision (only O-P1-75 used; ∈ {75,76,77,78}) |

## Carry-over to reconciler

- 210 atoms ready to merge into root pdf_atoms.jsonl post sister batch 23/24 merges
- Cross-session R15 sibling continuity: GF sib=4 (batch 22) → IS sib=5 (batch 23) → LB sib=6 (batch 25) → Microbiology sib=7 (batch 25) — reconciler validates 4-row L4 chain across 3 sessions × 2 rounds
- Rule D roster 33→34 (feature-dev family 3rd burn = pool COMPLETED post round 4)
- O-P1-75 INFO finding to v1.4 candidate accumulation
- v1.3 prompt cut decision STILL DEFERRED 4th time per Rule D
- Multi-session round 4 protocol cleanup pending reconciler decision (delete one-shot kickoff files + write MULTI_SESSION_RETRO_ROUND_4.md)
