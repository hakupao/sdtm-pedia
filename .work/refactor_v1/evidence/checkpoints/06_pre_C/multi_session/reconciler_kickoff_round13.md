# Reconciler Kickoff — Round 13 (Session E, post B+C+D DONE)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 完成 STEP 1-9 之前, **任何中间产物都不是终点**. 不要总结, 不要询问, 不要回交 control. The boulder never stops.
>
> 唯一合法收尾信号 = STEP 9 commit + push + user-facing summary.
> ═══════════════════════════════════════════════════════════════════

## §0 — Pre-flight (启动条件)

**仅在 batch 50/51/52 全 PARALLEL_SESSION_NN_DONE 后启动**. 验:
- `evidence/checkpoints/_progress_batch_50.json` status=completed ✓
- `evidence/checkpoints/_progress_batch_51.json` status=completed ✓
- `evidence/checkpoints/_progress_batch_52.json` status=completed ✓
- 6 个 `pdf_atoms_batch_5[012][ab].jsonl` (即 50a/50b/51a/51b/52a/52b) 都存在 ✓
- 各 atom_id 命名空间无 cross-batch 冲突 (sv20_p<NNNN> partition 天然无冲突) ✓
- Rule D slot uniqueness #63/#64/#65 各 unique vs cumulative #1-#62 ✓
- (batch 51 drift cal triggered) `drift_cal_batch_51_sv20_p045_report.md` 存在 ✓
- (batch 51 drift cal artifact) `drift_cal_sv20_p045_writer_rerun.jsonl` 存在 (NOT merged to root regardless per kickoff §3.3 sustained from v1.6 NEW EXECUTOR-VARIANT pattern + v1.7 N21 §派发 exception) ✓
- v1.7 N21 production scope verification pre-condition: 6 batch atom files all `extracted_by.subagent_type=oh-my-claudecode:executor` (0 writer-family contamination expected) ✓
- (batch 52 P0 overlap caveat) decision recorded: Option (a) SKIP p.50 default OR Option (c) revalidation artifact at `sv20_p050_round13_revalidation.jsonl` if main session authorized ✓

如有 halt_state_batch_NN.md 文件存在 → 处理 G-MS-4 fallback per **STRONGLY VALIDATED** protocol (round 7 batch 32 1st + round 8 batch 36 2nd + round 10 batch 42 3rd live-fire EFFECTIVE precedent — read halt_state + present 4 resume options to user OR proceed if user already authorized). **NB: under v1.7 N21 design (sustained from round 11+12), 7th+8th+9th... cumulative writer-direction recurrence at writer-direction is impossible by construction (writer NOT used in production); halt_state for batch 51 drift cal would be EXPECTED design outcome (writer rerun fabricates AGAIN OR canonical-form drift OR atom_type ENUM FABRICATION = validates N21 ban scope; NOT halt trigger since artifact NOT merged regardless). Halt only if executor-direction motif surfaces in baseline production atoms → ESCALATE to v1.8 trigger candidate per round 11+12 D-MS-NEW-* multi-axis motif type classification taxonomy.**

## §1 — Background

- Round 13 reconciler post 3 sister sessions B/C/D 物理并行 batches 50/51/52
- v1.7 prompts ACTIVE since 2026-04-29 commit `6d19992` (round 13 = **3rd round running v1.7 baseline** post round 12 2nd cumulative EFFECTIVE 2026-04-30 commit `ba1ae12`)
- Round 12 cumulative state pre-merge: 11774 atoms / 490 pages / 49 batches (post round 12 reconciler 2026-04-30 commit `ba1ae12` + round 12 retro D-MS-NEW-12-7 P1 closure trajectory 91.6% / 45 pages residual → user implicit ack continuation by requesting batches 50/51/52 kickoff)
- Expected post-round-13 state: ~12000-12200 atoms / 519-520 pages / 52 batches (depending on Option (a)/(b)/(c) for P0 overlap p.50)
- Rule D last burn pre-round-13: #62 Explore (round 12 batch 49 2nd burn extension)
- Rule D round 13 added: #63 oh-my-claudecode:architect (omc 15th burn) + #64 codex:codex-rescue (5th burn extension) + #65 Plan (3rd burn extension)
- AUDIT pivot count post round 13: 46th cumulative (43 post round 12 + 3 round 13 = 46th)
- Findings cumulative pre-round-13: 109 (O-P1-01..176 with 156/157-160/162-164/167-176 reserved unused per round 11+12); round 13 expected adds O-P1-177..188 (12 IDs reserved)
- Family pool state pre-round-13: 4 EXHAUSTED [vercel + plugin-dev + feature-dev + pr-review-toolkit] + omc 14× + general-purpose 4× + superpowers 1× + Plan 2× + claude-code-guide 2× + codex 4× + Explore 2× = 11 active families
- Family pool state expected post-round-13: + omc 15× (architect #63 = 15-burn intra-family depth — D-MS-7 candidate "architect-strategist" 6th successive D-MS-7 candidate omc agent at 15th-burn intra-family depth) + codex 5× (5-burn intra-family depth scale validated) + Plan 3× (3-burn intra-family depth scale validated, 1st single-agent family at 3-burn post v1.7 cut) = 11 active families post round 13 (no NEW family inaugural this round; all 3 reviewers from previously-active families intra-family-depth extension)

## §2 — Required Reads (并行)

1. `.work/06_deep_verification/_progress.json` (recovery_hint + round 12 cumulative state)
2. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.7.md` (176 lines, v1.7 N21 + Hook 16.7)
3. `.work/06_deep_verification/subagent_prompts/P0_reviewer_v1.7.md` (137 lines, Rule D 62 → 65 expected post round 13)
4. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (master)
5. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_12.md` (round 12 retro for context — D-MS-NEW-12-1 multi-axis motif taxonomy + G-MS-NEW-12-1 multi-axis formalization v1.8 codification + R-MS-15 single-agent family 2-burn pattern + D-MS-NEW-12-7 P1 closure trajectory)
6. 3 个 sub-progress: `evidence/checkpoints/_progress_batch_5[012].json`
7. 3 个 batch reports: `evidence/checkpoints/P1_batch_5[012]_report.md`
8. `evidence/checkpoints/drift_cal_batch_51_sv20_p045_report.md` (13th time NEW1 dual-threshold + v1.7 N21 3rd cumulative drift cal validation + 2nd in sv20 + multi-axis motif taxonomy 3rd cumulative validation outcome)
9. (Option (c) only) `evidence/checkpoints/sv20_p050_round13_revalidation.jsonl` if main session authorized P0 overlap revalidation pass

## §3 — Cross-Batch Sibling Continuity Sweep (mandatory, v1.6 §0.5 reconciler-side sweep codification carry-forward, round 13 = 5th cumulative live-fire opportunity preventive — STRONGLY VALIDATED status promotion EXPECTED)

### §3.1 INTRA-AGENT consistency cross-session sweep

For each L3/L4/L5/L6 parent_section appearing in multiple sub-batches across sister sessions B/C/D, verify canonical-form consistency. If short-form and full-form BOTH appear across sister sessions, prefer full-form alignment with the dominant sister session convention (per round 9 batch 39 reconciler 37-atom Option H precedent; round 10 + round 11 + round 12 reconciler 0 fixes preventive carry-forward).

### §3.2 v1.7 N21 production atom verification (sustained from round 11+12)

For each merged production atom from batches 50/51/52, verify `extracted_by` field does NOT match writer-family pattern (`oh-my-claudecode:writer`) per N21 production scope mandatory check. If any production atom emitted by writer-family found → mark with `[N21_writer_family_deprecation_violation]` HIGH severity marker + escalate to halt + investigate dispatch-time error / Hook 16.7 bypass / legacy atom pre-v1.7.

### §3.3 §0.5 reconciler-side cross-session canonical-form drift sweep (v1.6 §0.5 codification carry-forward, round 13 = 5th cumulative live-fire opportunity preventive — STRONGLY VALIDATED status promotion EXPECTED)

Round 9 batch 39b 37-atom Option H = 1st cumulative live-fire EFFECTIVE; round 10 = 2nd cumulative live-fire opportunity passed cleanly; round 11 = 3rd cumulative live-fire opportunity passed cleanly; round 12 = 4th cumulative live-fire opportunity passed cleanly = preventive EFFECTIVE 4 cumulative. Round 13 = **5th cumulative live-fire opportunity** — sweep should be preventive (no fixes needed) → expected STATUS PROMOTION TO STRONGLY VALIDATED firmly post 5 cumulative live-fires (1 actual fix + 4 cumulative preventive).

### §3.4 N6 INTRA-AGENT consistency cross-sub-batch via single-dispatch / SendMessage / inline-prepend (round 11-12 3-pattern observed, single-dispatch STRONGLY VALIDATED candidate at 3 cumulative)

If batches 50/51/52 used round 11 batch 46 single-dispatch NEW PRECEDENT pattern (one Agent call covers both a+b sub-batches in same agent context) → verify canonical parent_section forms preserved zero drift per N6 INTRA-AGENT consistency check. Round 13 expected pattern usage: all 3 batches likely single-dispatch per round 12 R-MS-11 STRONGLY VALIDATED candidate; if confirmed at 3 batches × round 13 = STATUS PROMOTION TO STRONGLY VALIDATED firmly post 6 cumulative live-fires.

### §3.5 Cross-PDF boundary canonical-form sweep (v1.8 codification candidate — round 13 NOT applicable, sv20-only round)

Round 13 = sv20-only round (no cross-PDF boundary; ig34 fully atomized post round 12); §3.5 cross-PDF sweep step skipped. Future cross-PDF batches (none expected — P1 closure scope = ig34 + sv20 fully atomized post round 14) would invoke this sweep dimension.

### §3.6 ⚠️ P0 Pilot baseline overlap verification (NEW round 13)

Round 13 batch 52 covers sv20 p.50-59 with P0 Pilot baseline overlap at sv20 p.50. **Reconciler-side P0 overlap verification**:
- **Option (a) SKIP p.50 (default)**: verify batch 52 atoms do NOT contain `sv20_p0050_aXXX` namespace atoms (executor SKIPped per kickoff §0.5 Option (a) instruction); if any sv20_p0050 atoms present → halt + Option H repair (delete sv20_p0050 atoms from batch 52 output OR escalate to main session for Option (b)/(c) reclassification)
- **Option (b) RE-ATOMIZE p.50** (NOT RECOMMENDED): if main session authorized, verify atom_id collision resolution per Option H (replace P0 baseline OR keep P0 baseline + drop new atoms OR document divergence as cross-version validation evidence)
- **Option (c) COMPARE p.50 cross-version validation artifact** (OPTIONAL): verify revalidation atoms preserved at `evidence/checkpoints/sv20_p050_round13_revalidation.jsonl` (NOT merged to root); document P0 baseline vs round 13 v1.7 N21 executor canonicalization divergence as v1.8 candidate stack evidence (P0 baseline drift detection at multi-version intervals)

## §4 — Sequential Merge Protocol

### §4.1 Pre-merge backup (Rule B)

`cp pdf_atoms.jsonl pdf_atoms.jsonl.pre-multi-50-52.bak` (preserve pre-merge state per Rule B failure archival not deletion + cumulative round 12 + reconciler).

### §4.2 Sequential append (atom_id partition guarantees no collision)

For each batch in order 50a → 50b → 51a → 51b → 52a → 52b, sequentially `cat pdf_atoms_batch_<NN><ab>.jsonl >> pdf_atoms.jsonl`.

### §4.3 Post-merge verification

- `wc -l pdf_atoms.jsonl` matches expected ~12000-12200 atoms (depending on Option for P0 overlap)
- `python3 -c "import json; [json.loads(l) for l in open('pdf_atoms.jsonl')]"` 0 JSON err
- `cut -f1 -d' ' <(grep -oE '"atom_id":\s*"[^"]+"' pdf_atoms.jsonl) | sort -u | wc -l` matches total line count (no dup atom_ids)
- ig34 pages contiguous 1-461 (last page reflects ig34 fully atomized milestone preserved post round 12)
- sv20 pages contiguous 1-59 (sv20 first 59 pages atomized post round 13; **NB Option (a) p.50 = P0 baseline preserved unchanged**)
- `source` field distribution: `~95-96%` "SDTMIG v3.4" + `~4-5%` "SDTM v2.0" (sv20 ratio rises round 14 P1 closure)

### §4.4 Drift cal artifact preservation (v1.7 N21 carry-forward sustained from round 11+12)

`drift_cal_sv20_p045_writer_rerun.jsonl` from batch 51 drift cal preserved at `evidence/checkpoints/drift_cal_sv20_p045_writer_rerun.jsonl` (artifact only, NOT merged to root regardless per kickoff §3.3 sustained from v1.6 NEW EXECUTOR-VARIANT pattern + v1.7 N21 §派发 exception). Document in `MULTI_SESSION_RETRO_ROUND_13.md` §3 D-MS-NEW-13 decision: drift cal artifact preservation policy v1.7 baseline 3rd cumulative + 2nd in sv20 + multi-axis motif taxonomy 3rd cumulative validation outcome.

### §4.5 (Option (c) only) P0 overlap revalidation artifact preservation

If main session authorized Option (c) P0 overlap revalidation pass: `sv20_p050_round13_revalidation.jsonl` preserved at `evidence/checkpoints/sv20_p050_round13_revalidation.jsonl` (artifact only, NOT merged to root; provides cross-version validation evidence for v1.8 candidate stack — P0 baseline drift detection at multi-version intervals).

## §5 — Audit Matrix Update (audit_matrix.md)

Append round 13 batch entries to audit_matrix.md per round 12 entry pattern:
- Batch 50 multi-session B round 13 (v1.7 baseline 3rd round running) | sv20 p.30-39 | 10-atom 1/page (seed=20260601) | oh-my-claudecode:architect (#63, AUDIT pivot 44th cumulative, **omc family 15th burn intra-family depth — D-MS-7 candidate "architect-strategist" 1st live-fire EFFECTIVE/INEFFECTIVE per actual outcome**) | sv20 §3.2 Special-Purpose Domains L2 NEW transition + sv20 model-level abstract hierarchy review verdict + N6 single-dispatch pattern STRONGLY VALIDATED candidate at 4-cumulative live-fires
- Batch 51 multi-session C round 13 (v1.7 baseline + drift cal MANDATORY sv20 p.45) | sv20 p.40-49 | 10-atom 1/page (seed=20260602) | codex:codex-rescue (#64, AUDIT pivot 45th, codex family 5-burn intra-family depth scale extension) | drift cal NEW1 dual-threshold 13th time outcome + N14 7th cumulative live-fire + v1.7 N21 3rd cumulative + 2nd in sv20 + multi-axis motif taxonomy 3rd cumulative validation outcome
- Batch 52 multi-session D round 13 (v1.7 baseline) | sv20 p.51-59 (Option (a)) OR p.50-59 (Option (b)/(c)) | 9-atom (Option (a)) OR 10-atom 1/page (Option (b)/(c)) (seed=20260603) | Plan (#65, AUDIT pivot 46th, single-agent family Plan 3-burn intra-family depth scale extension — 1st single-agent family at 3-burn extension post v1.7 cut) | sv20 model-level continuation review verdict + P0 Pilot baseline overlap p.50 caveat handling outcome (Option (a)/(b)/(c)) + N6 single-dispatch pattern carry-forward
- 结论 round-13 addendum (累 460 sample 跨 slot #18-#65, post round 12 #62 + round 13 batches 50/51/52): cumulative state outcome

## §6 — _progress.json Update (round 13 cumulative state)

Update keys:
- `current_phase` field append round 13 cumulative state
- `recovery_hint` field append round 13 outcome + v1.7 N21 3rd cumulative live-fire validation result + 2nd sv20 drift cal multi-axis motif classification + P0 overlap p.50 handling Option (a)/(b)/(c) outcome
- `status` field append round 13 cumulative status string
- **NEW round 13** P1 closure trajectory field: post-round-13 state 519-520/535 = 97.0-97.2% + 15-16 pages residual + estimated 1 round (round 14 closing) to P1 closure milestone

## §7 — Sibling Continuity Sweep Report Write

Write `sibling_continuity_sweep_report_round13.md` per round 12 sweep template:
- Reconciler-side Option H fixes (count + atoms touched + Rule B backups preserved; expected 0 per §3.3 5th cumulative live-fire opportunity preventive — STRONGLY VALIDATED status promotion EXPECTED)
- Schema violations (count, expected 0)
- Cross-batch sibling continuity gaps (count, expected 0 post v1.6 §0.5 codification 5th cumulative live-fire opportunity)
- P0 Pilot baseline overlap verification result (Option (a)/(b)/(c) outcome + atom_id collision check)
- v1.8 candidates filed (round 11+12 9 carry-forward + any NEW round 13 candidates)
- v1.7 N21 production scope verification result (no writer-family `extracted_by` in production atoms)

## §8 — MULTI_SESSION_RETRO_ROUND_13.md Write (Rule C 强制 8 段)

Per round 12 retro template:
- §0 Headline metrics table (round 1-13 cumulative)
- §0.1 Per-batch breakdown (batch 50 + 51 + 52 + reconciler E)
- §1 R-MS-1..N retain (reaffirmed sustained recipes)
- §2 G-MS-NEW-13-1..N gap (round 13 surfaces)
- §3 D-MS-NEW-13-1..N decision (round 13 decisions)
- §4 Rule A/B/C/D/E 合规
- §5 跨 retro 呼应
- §6 Next round 14 closing readiness OR P1 CLOSURE milestone trajectory
- §7 Cleanup readiness
- §8 Round 13 closure

Round 13 expected reaffirmations:
- R-MS-1 multi-session physical parallel protocol (13 cumulative rounds × ~1.5h savings = ~18-20h wall savings cumulative)
- R-MS-2 TOC anchor methodology n=440 firmly locked at 44 consecutive batches (round 13 extends n=410→n=440)
- R-MS-3 cross-round Rule D zero-collision with 46 AUDIT-mode pivots cumulative
- R-MS-4 G-MS-4 STRONGLY VALIDATED sustained at 3 cumulative live-fires (no halt round 13 expected per v1.7 N21 design)
- R-MS-5 N14 strict alternation STRONGLY VALIDATED post 7th live-fire (round 13 batch 51)
- R-MS-7 v1.7 N21 EMERGENCY-CRITICAL writer-family complete deprecation 3rd cumulative live-fire EFFECTIVE/INEFFECTIVE per actual round 13 outcome
- R-MS-NEW-13 NEW: D-MS-7 candidate sister chain extended to 6 successive omc agents at 10/11/12/13/14/15th-burn intra-family depth (planner round 9 + verifier + tracer round 10 + code-reviewer round 11 + critic round 12 + architect round 13)
- R-MS-NEW-13 NEW: codex 5-burn intra-family depth scale VALIDATED post round 13 batch 51 (#48+#52+#56+#61+#64)
- R-MS-NEW-13 NEW: Plan 3-burn intra-family depth scale VALIDATED post round 13 batch 52 (#46+#58+#65 = 1st single-agent family at 3-burn extension post v1.7 cut)
- R-MS-NEW-13 NEW: drift cal multi-axis motif taxonomy round 12 D-MS-NEW-12-1 sustained at 3rd cumulative validation (round 13 batch 51 outcome) + multi-axis cumulative count update
- R-MS-NEW-13 NEW: P0 Pilot baseline overlap p.50 handling Option (a)/(b)/(c) precedent codified (round 13 batch 52 1st live-fire of P0 overlap protocol)

Round 13 expected gaps:
- G-MS-NEW-13-1: outcome of v1.7 N21 baseline drift cal at sv20 p.45 (multi-axis motif type classification + cumulative count update)
- G-MS-NEW-13-2: P0 Pilot baseline overlap p.50 handling Option codification (Option (a)/(b)/(c) recommendation for v1.8)
- G-MS-NEW-13-3: round 14 closing batch design (1 batch covering sv20 p.60-74 OR 2 batches 53/54; reviewer slot #66/#67 candidates)
- G-MS-NEW-13-4+: TBD per actual round 13 surfaces

## §9 — STEP 9 Commit + Push

Single commit covering:
- root pdf_atoms.jsonl merge (+~220-470 atoms cumulative)
- audit_matrix.md round 13 batch entries
- _progress.json round 13 update + P1 closure trajectory 97.0-97.2%
- sibling_continuity_sweep_report_round13.md
- MULTI_SESSION_RETRO_ROUND_13.md
- 3 batch reports (P1_batch_50/51/52_report.md)
- 3 sub-progress JSON
- drift cal report (batch 51 sv20 p.45)
- 6 batch atom JSONL files (sub-session output preserved for audit trail per Rule B)
- drift_cal_sv20_p045_writer_rerun.jsonl artifact (NOT merged to root, preserved as v1.7 N21 baseline 3rd cumulative drift cal evidence + 2nd in sv20 + multi-axis motif taxonomy 3rd cumulative validation artifact)
- (Option (c) only) sv20_p050_round13_revalidation.jsonl artifact (NOT merged to root, preserved as P0 baseline cross-version validation evidence for v1.8 candidate stack)

Push to main per established v1.x cut + multi-session round closure precedent.

User-facing summary:
- Round 13 cumulative state (atoms / pages / batches / Rule D / AUDIT pivots / family pools)
- P1 closure trajectory: 519-520/535 = 97.0-97.2% (15-16 pages residual sv20 p.60-74 — round 14 closing)
- v1.7 N21 3rd cumulative live-fire validation outcome + 2nd sv20 drift cal outcome + multi-axis motif taxonomy 3rd cumulative validation
- N14 7th cumulative live-fire outcome
- D-MS-7 candidate sister chain extended to 6 successive omc agents validation
- codex 5-burn intra-family depth scale validated
- Plan 3-burn intra-family depth scale validated (1st single-agent family at 3-burn extension post v1.7 cut)
- P0 Pilot baseline overlap p.50 handling Option (a)/(b)/(c) precedent codified
- N+ carry-forward + N NEW v1.8 candidates filed
- Round 14 P1 closure trajectory: batches 53/54 (or single closing batch 53) cover sv20 p.60-74 → P1 CLOSURE milestone reached at sv20 p.74 = 535/535 = 100%

## §10 — DO NOT TOUCH (until reconciler scope complete)

- `subagent_prompts/*` (v1.7 active 不动)
- `schema/*.json`
- `PLAN.md` / `plans/*.md` (P1 closure trajectory updated in §6 retro NOT in plans/)
- `CLAUDE.md` / `MEMORY/*` (project-scope; round 13 routing rule cleanup deferred per round 12 reconciler §7 carry-forward)
- root `audit_matrix.md` until §5 explicit update step
- root `_progress.json` until §6 explicit update step
- **NEW round 13**: P0 Pilot baseline atoms at sv20 p.50 in root `pdf_atoms.jsonl` (Option (a) default preserves unchanged; Option (b) NOT RECOMMENDED but if authorized requires explicit Option H; Option (c) preserves both via separate revalidation artifact file)

## §11 — Round 14 / P1 closure trajectory prep notes

Post round 13 reconciler completion, P1 closure trajectory:
- Round 13 ends: 519-520/535 = 97.0-97.2% (15-16 pages residual = sv20 p.60-74)
- **Round 14 (closing) prep**: batches 53/54 (or single closing batch 53) cover sv20 p.60-74 (15 pages residual); pre-allocated reviewer slots #66/#67 (NOT cumulative #1-#65); drift cal target batch 54 sv20 p.65 (14th cumulative + N14 8th live-fire) IF round 14 covers 2 batches OR drift cal SKIP if single closing batch 53 (cumulative atoms post-sv20-p.45 ≥600 dual-threshold not yet met by round 14 single-batch end); candidates: omc-family remaining (qa-tester / code-simplifier / scientist / test-engineer / writer per N21 §派发 exception) + general-purpose 5th burn extension + claude-code-guide 3rd burn extension + Explore 3rd burn extension + codex 6th burn extension + superpowers extension (only `superpowers:code-reviewer` AGENT and BURNED at #36; superpowers family no other AGENT eligible)
- **P1 CLOSURE milestone**: trigger formal P1 closure documentation per v1.7 cut handoff §x P1 closure scope per `plans/P1_pdf_atomization.md` v1.0 + ack to Daisy + transition to P2 / P3 / P4 stages per parent PLAN.md v0.6 §3
- Possible round 14 sub-pattern: single closing batch 53 covers all 15 pages residual sv20 p.60-74 (deviation from 10-page-per-batch convention; justified by P1 closure proximity + 15 pages < 2-batch threshold + reviewer slot #66 single allocation = simpler closure); main session decides batch 53 vs 53+54 split pre-round-14 dispatch

═══════════════════════════════════════════════════════════════════
The boulder never stops. STEP 0 pre-flight check first (verify all 3 sub-progress files completed; if any missing → halt + present status to user).
