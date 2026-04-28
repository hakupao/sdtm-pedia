# Batch 53 Kickoff — Round 14 Sister B (sv20 p.60-69, 10 pages)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 完成 STEP 1-7 之前不要总结/询问/回交 control. The boulder never stops.
>
> 唯一合法收尾信号 = STEP 7 PARALLEL_SESSION_53_DONE single-line echo.
> ═══════════════════════════════════════════════════════════════════

## §0 — Pre-flight

**Pre-conditions**:
- v1.8 baseline ACTIVE since 2026-04-30 commit `0d6efb4` (round 14 = **1st INAUGURAL live-fire of v1.8 baseline**)
- Round 13 closed via reconciler `ae06326`: 12194 atoms / 519 pages / 52 batches / 115 findings / 47 AUDIT pivots
- Round 14 = **3 sister sessions B/C/D parallel + reconciler E** covering sv20 closing + p.50 backfill
- Pre-allocated reviewer slot **#67** unique vs cumulative #1-#66 (verify)
- Finding ID range pre-allocation: **O-P1-189..192** (4 IDs reserved batch 53)

**Reads required** (parallel):
1. `.work/06_deep_verification/_progress.json` (recovery_hint + round 13 cumulative + v1.8 cut details)
2. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.8.md` (179 lines, 5 NEW patches N24-N28 + Hook 21)
3. `.work/06_deep_verification/subagent_prompts/P0_reviewer_v1.8.md` (170 lines, Rule D 63 + 36-item fix matrix A-AJ)
4. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (master)
5. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_13.md` (round 13 retro for context)
6. `.work/06_deep_verification/audit_matrix.md` tail (last entries: round 13 batches + sibling sweep + conclusion)

## §1 — Background

- **Round 14 = P1 CLOSURE round** (3 batches reach 535/535 = 100%)
- **v1.8 baseline 1st INAUGURAL live-fire** for batch 53
- **Page range**: sv20 p.60-69 (10 pages, standard convention)
- **Sub-batch design**: 53a (p.60-64) + 53b (p.65-69), single-dispatch N6 pattern (STRONGLY VALIDATED at 6 cumulative live-fires post round 13)
- **Drift cal cadence**: SKIP this batch (mandatory drift cal target = batch 54 sv20 p.72 per every-3-batches cadence; batch 51 was last drift cal)

## §2 — Writer dispatch (executor MANDATORY per v1.8 N21)

**Subagent**: `oh-my-claudecode:executor` (writer-family BANNED per v1.7/v1.8 N21)

**Single-dispatch pattern N6**: one Agent call covers 53a + 53b in same agent context.

**Prompt version**: `P0_writer_pdf_v1.8.md` (179 lines, 5 NEW patches N24-N28 + Self-Validate hooks 1-21)

**Hook 21 NEW v1.8 page-boundary off-by-one detection**: WARN-mode (≤1/batch logged; >1/batch halt-on-violation candidate per v1.9 promotion).

## §3 — Active heading state at start of sv20 p.60

Per round 13 batch 52 closure (sv20 p.59 end):
- L1 active: `§5 [STUDY-LEVEL DATA]`
- L2 active: `§5.1 [The Trial Design Model]` (N11 EXTENDED scope)
- L3 active: `§5.1.6 Trial Summary Information` (Trial Summary spec table rows 1-10 emitted at p.59)

**Predicted TOC transitions sv20 p.60-69** (verify pre-dispatch via `pdftotext -layout -f 60 -l 69 source/SDTM_v2.0.pdf`):
- Trial Summary spec table continuation at p.60 (if any rows 11+)
- §5.2 [Trial Design Datasets] L2 NEW around p.60-63
- §5.3 [Other Study-Level Domains] L2 NEW around p.65-67
- Various L3/L4 sub-headings + spec tables

## §4 — Self-Validate hooks 1-21 (v1.8)

Hooks 1-20 carry-forward + Hook 21 NEW v1.8 page-boundary detection (per N26).

Other hooks: Hook 13 pipe-count + Hook 16.7 simplified pre-dispatch ban + Hook 18 SENTENCE concat WARN + Hook 19 PDF-cross-verify N=10 + Hook 20 sv20 header/footer 4-pattern (STRONGLY VALIDATED at 3 cumulative).

## §5 — Rule A audit

**Slot**: #67 (unique vs cumulative #1-#66)

**Recommended subagent_type**: **codex:codex-rescue 7th burn extension** (sustains "external runtime / different model = strongest Rule D isolation" principle for P1 closure round; codex-family 7-burn intra-family depth scale CANDIDATE VALIDATION post round 14)

Alternative candidates: omc-family remaining (qa-tester / code-simplifier) / general-purpose 5th burn / claude-code-guide 3rd burn / Explore 3rd burn / Plan 4th burn

**Sample**: 10-atom stratified 1/page sv20 p.60-69 seed=20260701

**Threshold**: ≥80% weighted (kickoff §5.2 v1.8 N21 strict halt clause sustained from v1.7)

## §6 — Halt clause (v1.8 N21 sustained)

ONLY if executor-direction motif surfaces in baseline via Hook 19 PDF-cross-verify (value fab) OR schema sweep failure → halt + escalate. N26 motif at executor-direction = WARN-mode under v1.8 (not halt-grade).

## §7 — Single-line DONE echo

```
PARALLEL_SESSION_53_DONE atoms=N failures=0 repair_cycles=0 rule_a=N% drift_cal=skipped findings_added=O-P1-189..192 (4 IDs reserved per pre-allocation)
```

## §8 — Output files (this batch owns)

- `evidence/checkpoints/pdf_atoms_batch_53a.jsonl` + `pdf_atoms_batch_53b.jsonl`
- `evidence/checkpoints/_progress_batch_53.json`
- `evidence/checkpoints/P1_batch_53_report.md`
- `evidence/checkpoints/rule_a_batch_53_sample.jsonl` + `rule_a_batch_53_verdicts.jsonl` + `rule_a_batch_53_summary.md`

## §9 — DO NOT TOUCH (until reconciler scope)

- root `pdf_atoms.jsonl` / `audit_matrix.md` / `_progress.json`
- `subagent_prompts/*` / `schema/*.json`
- `PLAN.md` / `plans/*.md`
- `CLAUDE.md` / `MEMORY/*`
- sister batch files (batch 54 sister C scope, batch 55 sister D scope)

═══════════════════════════════════════════════════════════════════
STEP 0 pre-flight first; proceed to §2 writer dispatch single Agent call covering 53a + 53b.
