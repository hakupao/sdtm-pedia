# Batch 53 Kickoff — Round 14 P1 CLOSING SINGLE BATCH (sv20 p.60-74, 15 pages)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 这是 P1 closure 的 **closing batch**. 完成 STEP 1-7 之前不要总结/询问/回交 control. The boulder never stops.
>
> 唯一合法收尾信号 = STEP 7 PARALLEL_SESSION_53_DONE single-line echo.
> ═══════════════════════════════════════════════════════════════════

## §0 — Pre-flight

**Pre-conditions**:
- v1.8 baseline ACTIVE since 2026-04-30 commit `0d6efb4`
- Round 13 closed via reconciler `ae06326`: 12194 atoms / 519 pages / 52 batches / 115 findings / 47 AUDIT pivots
- This round = **round 14 SINGLE CLOSING BATCH** (no sister sessions; reconciler E follows directly)
- v1.8 baseline 1st INAUGURAL live-fire (round 14 = 1st post-v1.8-cut round running)
- Pre-allocated reviewer slot: **#67** unique vs cumulative #1-#66 (verify)
- Finding ID range pre-allocation: **O-P1-189..194** (6 IDs reserved closing batch)

**Reads required** (parallel):
1. `.work/06_deep_verification/_progress.json` (recovery_hint + round 13 cumulative + v1.8 cut details)
2. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.8.md` (179 lines, 5 NEW patches N24-N28 + Hook 21)
3. `.work/06_deep_verification/subagent_prompts/P0_reviewer_v1.8.md` (170 lines, Rule D 63 + 36-item fix matrix A-AJ)
4. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (master)
5. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_13.md` (round 13 retro for context — D-MS-NEW-13-* decisions + slot collision resolution + N26 Option H deferral + first executor-direction motif observable)
6. `.work/06_deep_verification/audit_matrix.md` tail (last entries: round 13 batches + sibling sweep + conclusion)

## §1 — Background

- **Round 14 = P1 CLOSURE round** (reaches 535/535 = 100% if Option (a) p.50 SKIP held; if v1.8 backfills sv20 p.50 separately, full closure includes 1 backfill batch — this batch SKIPs p.50 still)
- **v1.8 baseline 1st INAUGURAL live-fire**:
  - N24 multi-axis writer-direction motif taxonomy (3 axes formalized + Axis 4+ extensible)
  - N25 cross-PDF boundary §3.5 sweep (N/A this round; sv20-only)
  - N26 page-boundary off-by-one detection NEW Hook 21 (Self-Validate pre-DONE WARN-mode for dense spec-table content)
  - N27 L1 NEW HEADING parent_section single canonical form mandate (chapter-short-bracket §N [TITLE])
  - N28 L2 active-heading parent_section drift fix-up pattern
  - Self-Validate hooks 20→21
- **Page range**: sv20 p.60-74 (15 pages, single batch — Option A per round 13 retro §6)
- **Sub-batch design**: NONE for single closing batch (no a/b split; one Agent dispatch covers all 15 pages — extension of N6 single-dispatch pattern STRONGLY VALIDATED at 6 cumulative live-fires)
- **Drift cal cadence**: SKIP this batch (next mandatory would be batch 54 sv20 p.65 14th cumulative IF round 14 covered 2 batches; single closing batch design = drift cal SKIP per cumulative atoms post-sv20-p.45 ≥600 dual-threshold not met by single-batch end)

## §2 — Writer dispatch (executor MANDATORY per v1.8 N21 sustained)

**Subagent**: `oh-my-claudecode:executor` (writer-family BANNED per v1.7 N21 sustained under v1.8 baseline)

**Single-dispatch pattern N6** (STRONGLY VALIDATED at 6 cumulative live-fires post round 13): one Agent call covers all 15 pages in same agent context.

**Prompt version**: `P0_writer_pdf_v1.8.md` (179 lines, 5 NEW patches N24-N28)

**Hook 16.7 simplified pre-dispatch ban**: writer-family BANNED check before dispatch (executor permitted).

**Self-Validate hooks 1-21**: all 21 hooks must PASS before DONE echo (Hook 21 NEW = page-boundary off-by-one detection per N26).

**Hook 21 trigger conditions** (NEW v1.8): dense TABLE_ROW homogeneous + multi-row sustained-content-narrative across 5+ page sub-batch + sv20 explicit footer 'Page N' marker tracking. WARN-mode (non-blocking; logs to evidence; recommends Option H page-label correction; promote to halt-on-violation if motif persists at >1 atom per batch).

## §3 — Active heading state at start of sv20 p.60

Per round 13 batch 52 closure (sv20 p.59 end):
- **L1 active**: `§5 [STUDY-LEVEL DATA]` (sib=5 under sv20 root accounting for p.50 §4 SKIP)
- **L2 active**: `§5.1 [The Trial Design Model]` (N11 EXTENDED scope — has L3 children)
- **L3 active**: `§5.1.6 Trial Summary Information` (sib=6 under §5.1; spec-table Trial Summary rows 1-10 emitted at p.59)
- **TABLE_ROW continuation**: Trial Summary rows 11+ may continue to p.60 OR new section starts (verify pre-extraction)

## §4 — Predicted TOC transitions sv20 p.60-74 (verify pre-dispatch)

Per page_index.json + sv20 PDF source:
- §5.2 [Trial Design Datasets] L2 NEW around p.60-65 (sib=2 under §5)
- §5.3 [Other Study-Level Domains] L2 NEW around p.65-70 (sib=3 under §5)
- §5.4 [Special-Purpose Datasets] L2 NEW around p.70-74 (sib=4 under §5)
- §6 [DATASETS] L1 NEW IF reached at p.74 (final L1 transition in P1)
- Various L3/L4 sub-headings + spec tables

**Pre-dispatch verification**: Run `pdftotext -layout -f 60 -l 74 source/SDTM_v2.0.pdf` + extract TOC anchors + cross-verify against page_index.json BEFORE writer dispatch (G-MS-NEW-10-3 motif preventive — main session pre-dispatch verifies PDF ground truth).

## §5 — Self-Validate hooks 21 (v1.8)

Hooks 1-20 carry-forward from v1.7 + Hook 21 NEW.

**Hook 21 page-boundary detection** (NEW v1.8 N26):
- Cross-page row physical-page disambiguation via pdftotext per-page extraction OR explicit footer 'Page N' marker tracking
- sv20 has 'Page N' footers usable for auto-validation
- WARN-mode threshold: 1 atom/batch (≤1/batch = WARN logged to evidence; >1/batch = halt-on-violation candidate per v1.9 promotion path)
- Disposition: log + recommend Option H page-label correction at reconciler stage (deferred not enforced under v1.8 WARN-mode)

**Other hooks** (existing):
- Hook 13 TABLE_ROW pipe-count consistency
- Hook 15 N5 documented exception detection
- Hook 16.7 simplified pre-dispatch writer-family ban
- Hook 18 SENTENCE-paragraph-concat WARN
- Hook 19 PDF-cross-verify N=10
- Hook 20 sv20 header/footer 4-pattern check (STRONGLY VALIDATED at 3 cumulative live-fires post round 13)

## §6 — Rule A audit

**Slot**: #67 (unique vs cumulative #1-#66)

**Subagent_type candidates** (Rule D AGENT-vs-SKILL roster post round 13 + v1.8 cut):
- omc-family remaining: qa-tester / code-simplifier / scientist / test-engineer / writer (per N21 §派发 exception for AUDIT pivot reviewer slots only)
- general-purpose 5th burn extension (4-burn validated post round 10)
- claude-code-guide 3rd burn extension (2-burn validated post round 11)
- Explore 3rd burn extension (2-burn validated post round 12)
- codex 7th burn extension (6-burn validated post round 13)
- Plan 4th burn extension (3-burn validated post round 13)

**Recommended choice**: codex:codex-rescue 7th burn extension (sustains "external runtime / different model = strongest Rule D isolation" principle for closing batch + P1 CLOSURE milestone audit purpose; 7-burn intra-family depth scale CANDIDATE VALIDATION post round 14).

**Sample**: 10-atom stratified 1/page sv20 p.60-74 (15 pages) — 10 random pages stratified seed=20260701.

**Threshold**: ≥80% weighted (kickoff §5.2 v1.7/v1.8 N21 strict halt clause unchanged).

**Halt clause**: ONLY if executor-direction motif surfaces in baseline via Hook 19 PDF-cross-verify (value fab) OR schema sweep failure. N26 motif at executor-direction is WARN-mode under v1.8 (not halt-grade).

## §7 — Single-line DONE echo

After all hooks PASS + Rule A PASS + 0 halt-grade verbatim FAILs:

```
PARALLEL_SESSION_53_DONE atoms=N failures=0 repair_cycles=0 rule_a=N% drift_cal=skipped findings_added=O-P1-189..194 (6 IDs reserved per pre-allocation)
```

## §8 — Output files (this batch owns)

- `evidence/checkpoints/pdf_atoms_batch_53.jsonl` (single file — no a/b split for closing batch)
- `evidence/checkpoints/_progress_batch_53.json`
- `evidence/checkpoints/P1_batch_53_report.md`
- `evidence/checkpoints/rule_a_batch_53_sample.jsonl`
- `evidence/checkpoints/rule_a_batch_53_verdicts.jsonl`
- `evidence/checkpoints/rule_a_batch_53_summary.md`
- `evidence/checkpoints/rule_a_batch_53_pdf_groundtruth.txt` (optional, per reviewer choice)

## §9 — DO NOT TOUCH (until reconciler scope)

- root `pdf_atoms.jsonl` (12194 atoms baseline post round 13)
- `audit_matrix.md` / `_progress.json` root
- `subagent_prompts/*` (v1.8 active 不动)
- `schema/*.json` (frozen v1.2)
- `PLAN.md` / `plans/*.md`
- `CLAUDE.md` / `MEMORY/*` (project-scope)
- sister batch files (NO sister sessions this round; closing batch single dispatch)

## §10 — Round 14 closing context

- **P1 CLOSURE milestone trigger**: at sv20 p.74 = 535/535 = 100% (assuming Option (a) p.50 SKIP held; if v1.8 backfills sv20 p.50 separately, full closure includes 1 backfill batch — this batch SKIPs p.50 still)
- **Post-round-14 expected state**: 12194 + N atoms / 534-535 pages / 53 batches / Rule D #67 / 48 AUDIT pivots / 11 active families + 4 EXHAUSTED unchanged
- **Reconciler E round 14**: triggers formal P1 closure documentation per `plans/P1_pdf_atomization.md` v1.0 + ack to Daisy + transition to P2 / P3 / P4 stages per parent PLAN.md v0.6 §3
- **v1.9 candidate stack carry-forward**: 15 cumulative items post round 13 (9 NEW + 6 carry-forward) — multi-axis taxonomy refinement + per-family cumulative tracking + N26 promote WARN→halt + Axis 4/5 codification + halt clause extension + heading_text schema clarification + TABLE_HEADER continuation-page convention + Hook 21 backport + executor-direction motif watch + P0 baseline absence backfill + carry-forward v1.8 OBS items

═══════════════════════════════════════════════════════════════════
The boulder never stops. STEP 0 pre-flight check first (verify v1.8 prompts loaded + Rule D slot #67 unique + finding ID range available); proceed to §2 writer dispatch single Agent call covering all 15 pages.
