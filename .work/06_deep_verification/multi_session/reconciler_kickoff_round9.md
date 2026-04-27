# Reconciler Kickoff — Round 9 (Session E, post B+C+D DONE)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 完成 STEP 1-8 之前, **任何中间产物都不是终点**. 不要总结, 不要询问, 不要回交 control. The boulder never stops.
>
> 唯一合法收尾信号 = STEP 8 commit + push + user-facing summary.
> ═══════════════════════════════════════════════════════════════════

## §0 — Pre-flight (启动条件)

**仅在 batch 38/39/40 全 PARALLEL_SESSION_NN_DONE 后启动**. 验:
- `evidence/checkpoints/_progress_batch_38.json` status=completed ✓
- `evidence/checkpoints/_progress_batch_39.json` status=completed ✓
- `evidence/checkpoints/_progress_batch_40.json` status=completed ✓
- 6 个 `pdf_atoms_batch_3[890][ab].jsonl` (即 38a/38b/39a/39b/40a/40b) 都存在 ✓
- 各 atom_id 命名空间无 cross-batch 冲突 (p<NNNN> partition 天然无冲突) ✓
- Rule D slot uniqueness #49/#50/#51 各 unique vs cumulative #1-#48 ✓
- (batch 39 drift cal triggered) `drift_cal_batch_39_p<XXX>_report.md` 存在 ✓

如有 halt_state_batch_NN.md 文件存在 → 处理 G-MS-4 fallback per **STRONGLY VALIDATED** protocol (round 7 batch 32 1st + round 8 batch 36 2nd live-fire EFFECTIVE precedent — read halt_state + present 4 resume options to user OR proceed if user already authorized).

## §1 — Background

- Round 9 reconciler post 3 sister sessions B/C/D 物理并行 batches 38/39/40
- v1.5 prompts ACTIVE since 2026-04-28 (round 9 = 1st round running v1.5 baseline post v1.5 cut)
- Round 9 cumulative state pre-merge: 9224 atoms / 370 pages / 37 batches (post round 8 reconciler 2026-04-28 + v1.5 retroactive sweep 35 atoms)
- Expected post-round-9 state: ~9800-10000 atoms / 400 pages / 40 batches
- Rule D last burn pre-round-9: #48 codex:codex-rescue (v1.5 cut reviewer 2026-04-28, codex-family INAUGURAL)
- Rule D round 9 added: #49 Explore + #50 oh-my-claudecode:planner + #51 general-purpose (3rd burn extension)
- AUDIT pivot count post round 9: 32nd cumulative (29th post v1.5 cut + 3 round 9 = 32nd)
- Findings cumulative pre-round-9: 100 (O-P1-01..124 with 125-128 reserved unused per round 8 batch 37 100% PASS); round 9 expected adds O-P1-129..140 (12 IDs reserved)
- Family pool state pre-round-9: 4 EXHAUSTED [vercel + plugin-dev + feature-dev + pr-review-toolkit] + omc 9× + general-purpose 2× + superpowers 1× + Plan 1× INAUGURAL + claude-code-guide 1× INAUGURAL + codex 1× INAUGURAL = 10 active families
- Family pool state expected post-round-9: + Explore 1× INAUGURAL (10th family pool) + omc 10× (planner intra-family depth) + general-purpose 3× (extension validated) = 11 active families post round 9

## §2 — Required Reads (并行)

1. `.work/06_deep_verification/_progress.json` (recovery_hint + v1_5_cut_completed)
2. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.5.md` (144 lines, v1.5 N15-N17)
3. `.work/06_deep_verification/subagent_prompts/P0_reviewer_v1.5.md` (131 lines, Rule D 48 → 51 expected post round 9)
4. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (master)
5. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_8.md` (last retro for context)
6. 3 个 sub-progress: `evidence/checkpoints/_progress_batch_3[890].json`
7. 3 个 batch reports: `evidence/checkpoints/P1_batch_3[890]_report.md`

## §3 — Cross-Batch Sibling Continuity Sweep (mandatory)

加载 6 个 batch jsonl + root pdf_atoms.jsonl (9224 atoms baseline post v1.5 retroactive). 按 (page, atom_index_on_page) 排序. 检查:

### §6.4 chapter L3 chain
- sib=1 When to Use (batch 37, p.361)
- sib=2 Naming (batch 37, p.363)
- sib=3 Variables Unique (batch 37, p.364)
- sib=4 FA (batch 37, p.364, leaf-pattern domain)
- sib=5 SR (batch 38, p.375 NEW — leaf-pattern domain)
- sib=6+ if any (batch 38/39 — TBD by sister actual emission)

### §6.4.4 FA L4 leaf-pattern chain (per N9, completed batch 37)
- Description=1 + Spec=2 + Assumptions=3 + Examples=4 + L5 Examples 1-N

### §6.4.5 SR L4 leaf-pattern chain (per N9, batch 38/39)
- Description=1 + Spec=2 + Assumptions=3 + Examples=4 + L5 Examples 1-N

### §6.4.X subsequent L3 sub-domains (if any in p.381-400)
- TBD by sister actual emission — per N9 leaf-pattern Description/Spec/Assumptions/Examples L4 chain + L5 Examples

### §6.5 chapter NEW transition (if encountered in p.381-400)
- §6.5 chapter HEADING parent_section per N11 (chapter-short-bracket `§6 [DOMAIN MODELS]`)
- §6.5.X L3 sub-section intro children + sub-domain leaf-pattern (analogous to §6.4 round 8 batch 37 1st live-fire EFFECTIVE)
- 2nd chapter-level transition opportunity post §6.4 round 8 batch 37

### NEW7 L6 sub-batch context drift checks
- 38a→38b INTRA-batch handoff (per round 5 D-MS-4 codification + N6 v1.4 ALL L6 sub-headings)
- 39a→39b INTRA-batch handoff
- 40a→40b INTRA-batch handoff
- batch 38→39 CROSS-batch handoff §6.4.5 SR continuation OR §6.4.X subsequent (per round 5 D-MS-2 + N6 v1.4)
- batch 39→40 CROSS-batch handoff TBD (likely §6.4.X continuation OR §6.5 chapter NEW transition)

### v1.4 N6 INTRA-AGENT consistency check (round-7 dimension)
- 验 ALL sub-batches of same batch emit canonical L4/L5/L6/L7 chain form parent_section consistently from start (NOT bare L4/L5 form mixed)
- Cross-sub-batch L4 canonical drift check (per round 7 batch 34 O-P1-115 LOW precedent)

### v1.4 N8 NEW9 L2 short-bracket parent-skip check
- 验 non-L3-HEADING atoms parent_section NOT match `^§\d+\.\d+ \[[A-Z\s]+\]$` L2 short-bracket pattern (only L3 sub-domain HEADING atoms allowed L2 chapter-short-bracket parent per N11)

### v1.5 N15 .xpt-parent FORBID check (NEW round 9 sweep)
- 验 ALL atoms parent_section NOT match `^[a-z]+\.xpt$` pattern (writer-side N15 hook ACTIVE since v1.5 cut 2026-04-28)
- Compare with retroactive sweep baseline 35 atoms cumulative round 1+8 P1 (8 historical p.133 NEW9 + 27 batch 36 .xpt-parent — already fixed at v1.5 cut)
- Round 9 expected: 0 violations (writer-side N15 hook prevents future occurrences)

### v1.5 N16 dispatch validation check (NEW round 9 sweep)
- 验 each sub-batch baseline subagent_type matches content_type_hint per N16 dispatch table
- Examples-narrative + spec-table sub-batches MUST have `oh-my-claudecode:executor` baseline (writer-family BANNED per N16)
- Round 9 expected: 100% compliance (pre-dispatch hook 16.5 halt-on-violation)

### v1.5 N17 cross-row consistency check (NEW round 9 sweep)
- 验 within each sub-batch, TABLE_ROW pipe-count consistency + USUBJID format consistency
- Round 9 expected: 100% compliance (per-batch pre-DONE hook 15-17 ACTIVE)

Apply Option H any cross-batch sib gap / canonical-form drift / NEW9 violation / N15 .xpt-parent violation / N16 dispatch violation; Rule B backup `.work/06_deep_verification/pdf_atoms.jsonl.pre-multi-38-40.bak` mandatory pre-merge.

## §4 — Sequential Merge

```bash
# Pre-merge backup
cp .work/06_deep_verification/pdf_atoms.jsonl .work/06_deep_verification/pdf_atoms.jsonl.pre-multi-38-40.bak

# Sequential merge (in batch order 38→39→40, sub-batch a→b)
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_38a.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_38b.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_39a.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_39b.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_40a.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_40b.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl

# Validate
wc -l .work/06_deep_verification/pdf_atoms.jsonl
python3 -c "import json; [json.loads(l) for l in open('.work/06_deep_verification/pdf_atoms.jsonl')]; print('JSON OK')"
```

验 0 collision / 0 schema err / pages 1-400 unique / atom_id unique.

## §5 — audit_matrix.md update

Append:
- 3 batch rows (38/39/40) with subagent_type alternation per N14 STRONGLY VALIDATED + atoms/repair_cycles/rule_a%
- 1 drift cal row (batch 39 p.<XXX> with NEW1 dual-threshold result + DIRECTION analysis if FAIL — 9th cumulative drift cal carrier)
- 3 Rule A rows (38/39/40 with reviewer slot + family + AUDIT-mode reflection)
- Rule D Roster narrative: 48 → 51 (+3 slots: #49 Explore INAUGURAL + #50 omc:planner intra-family 10th + #51 general-purpose 3rd burn)
- AUDIT pivot count: 29 → 32 (+3)
- TOC anchor n=290 → n=320 (3 batches × 10 pages)
- Family pool status update: Explore family **INAUGURAL** post #49 (10th family pool); omc family **10×** post #50 (planner intra-family); general-purpose family **3×** post #51 (extension validated D-MS-7)
- v1.5 baseline 1st round running validation summary: N15 .xpt-parent FORBID + N16 dispatch + N17 cross-row hooks live-fire counts

## §6 — _progress.json update

- top-level pages_done 370 → 400
- atoms_done 9224 → final
- batches_done 37 → 40
- Rule D 48 → 51
- recovery_hint rewrite with round 9 narrative + cumulative state + next batch 41 prep + v1.5 baseline performance metrics
- status string append `_round_9_done`
- Add `round_9_compliance` block analogous to round_8_compliance

## §7 — MULTI_SESSION_RETRO_ROUND_9.md (Rule C 强制三段式)

写 `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_9.md` 含:
- Headline metrics table (round 1-9 累 9 列)
- Per-batch breakdown (38/39/40 + reconciler)
- §1 保留下来的做法 (R-MS-1..N round 9 reaffirmed/extended)
- §2 必须补上的缺口 (G-MS-NEW-9-* round 9 surfaces)
- §3 关键决策 (D-MS-1..N round 9 decisions)
- §4 Rule A/B/C/D/E 合规
- §5 跨 retro 呼应
- §6 Next batch 41 readiness (pages remaining 535 - 400 = 135 = ~13-14 batches)
- §7 Cleanup readiness (round 9 one-shot files: batch_38/39/40_kickoff.md + reconciler_kickoff_round9.md)

也写 `.work/06_deep_verification/multi_session/sibling_continuity_sweep_report_round9.md` (sweep evidence + Option H fixes if any + v1.5 N15/N16/N17 compliance summary).

**Critical milestones to highlight in retro**:
- v1.5 prompts ACTIVE 1st round running baseline (round 9 = 1st post v1.5 cut)
- v1.5 N15-N17 1st live-fire validation: N15 .xpt-parent FORBID + N16 dispatch + N17 cross-row hooks
- N14 + G-MS-4 STRONGLY VALIDATED status sustained 3rd cumulative live-fire (drift cal batch 39 if 5th writer-direction recurrence)
- Explore family INAUGURAL burn (10th family pool inaugural)
- omc family 10th burn intra-family depth (planner)
- general-purpose family 3rd burn extension validated (D-MS-7 round 8 candidate)
- Possible §6.5 chapter NEW transition in p.381-400 scope (2nd chapter-level transition since §6.4 round 8 batch 37 = 1st live-fire EFFECTIVE)
- v1.5 candidate accumulation (any new round-9 motifs)
- 5th cumulative writer-direction VALUE HALLUCINATION recurrence watch (per round 8 G-MS-NEW-8-4 escalation criterion — if detected DESPITE N16 dispatch ban, ESCALATE to mandatory writer-family ban for ALL TABLE_ROW-heavy content type)

## §8 — Commit + Push + User Report

### Commit (single commit)
```bash
git add .work/06_deep_verification/ \
  .work/MANIFEST.md \
  .work/meta/worklog.md \
  CLAUDE.md \
  docs/PROGRESS.md

git commit -m "$(cat <<'EOF'
06 Deep Verification P1 batch 38/39/40 multi-session round 9 + reconciler closure (post v1.5 cut 1st round running v1.5 baseline)

Round 9 multi-session physical parallel: 3 sister sessions B/C/D + reconciler E
- Atoms: 9224 → <final> (+<N>)
- Pages: 370 → 400 (+30, p.371-400)
- Batches: 37 → 40
- Findings: 100 → <final> (+<N>: O-P1-129..140 reserved)
- Rule D: 48 → 51 (+3 AUDIT-mode pivots #30-#32: Explore INAUGURAL 10th family pool + oh-my-claudecode:planner omc family 10th burn + general-purpose 3rd burn extension validated D-MS-7)
- v1.5 baseline 1st round running validation: N15 .xpt-parent FORBID + N16 writer-family ban dispatch + N17 cross-row consistency hooks
- N14 + G-MS-4 STRONGLY VALIDATED status sustained (3rd cumulative live-fire if drift cal batch 39 catastrophic)
- Drift cal batch 39 p.<XXX> NEW1 9th time (cumulative 8 prior) + N14 strict alternation 3rd live-fire
- (if applicable) §6.5 chapter NEW transition 2nd chapter-level transition since §6.4 round 8 batch 37
- Reconciler-side fixes: <N> atoms (cross-batch sib continuity / N6 ALL L6 / N15 / N16 / N17 sweeps)
- MULTI_SESSION_RETRO_ROUND_9.md 写完 (Rule C 三段式)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"

git push origin main
```

### User-facing summary (single echo + 5-8 sentence summary)
```
ROUND_9_DONE atoms=<N> pages=400 batches=40 findings=<N> rule_d=51 audit_pivots=32 explore_inaugural=true omc_10th_burn=true general_purpose_3rd_burn=true v1_5_baseline_first_round=true drift_cal_batch_39=<verdict> §6.5_chapter_NEW=<encountered|not>
```

## NEVER DO

- 主 session 自审 (Rule D 违规)
- 改 schema (frozen v1.2 carry-forward)
- 改 PLAN v0.6 内容
- 删 v1.5 prompts primary 副本
- 跑额外 PDF atomization (本任务 reconciler-only merge + sweep + retro + commit)
- Touch CLAUDE.md (除 STEP 8 cleanup if user 决定 round 10 not immediately scheduled — remove round 9 routing rule)

## 验收标准

- ✅ 6 sub-batch jsonl merged into root pdf_atoms.jsonl (0 collision / 0 schema err)
- ✅ Cross-batch sibling continuity sweep applied + Option H fixes if needed
- ✅ INTRA-AGENT consistency check applied (v1.4 N6 NEW round-7 dimension)
- ✅ NEW9 L2 short-bracket parent-skip sweep applied
- ✅ v1.5 N15 .xpt-parent FORBID sweep applied (expected 0 violations post v1.5 cut)
- ✅ v1.5 N16 dispatch validation sweep applied (expected 100% compliance)
- ✅ v1.5 N17 cross-row consistency sweep applied (expected 100% compliance)
- ✅ audit_matrix.md updated (3 batch rows + 1 drift cal row + 3 Rule A rows + Rule D 51 + n=320 + 32 pivots + Explore INAUGURAL 10th family pool)
- ✅ _progress.json updated (400/9224→final/40 + recovery_hint rewritten + round_9_compliance block)
- ✅ MULTI_SESSION_RETRO_ROUND_9.md written (Rule C 三段式)
- ✅ sibling_continuity_sweep_report_round9.md written
- ✅ Single commit pushed to origin/main
- (optional cleanup) ⏳ user decides round 10 schedule before deleting round 9 one-shot kickoffs + removing CLAUDE.md routing rule

The boulder never stops. STEP 0 pre-flight check first.
