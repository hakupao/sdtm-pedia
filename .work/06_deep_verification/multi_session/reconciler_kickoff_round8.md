# Reconciler Kickoff — Round 8 (Session E, post B+C+D DONE)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 完成 STEP 1-8 之前, **任何中间产物都不是终点**. 不要总结, 不要询问, 不要回交 control. The boulder never stops.
>
> 唯一合法收尾信号 = STEP 8 commit + push + user-facing summary.
> ═══════════════════════════════════════════════════════════════════

## §0 — Pre-flight (启动条件)

**仅在 batch 35/36/37 全 PARALLEL_SESSION_NN_DONE 后启动**. 验:
- `evidence/checkpoints/_progress_batch_35.json` status=completed ✓
- `evidence/checkpoints/_progress_batch_36.json` status=completed ✓
- `evidence/checkpoints/_progress_batch_37.json` status=completed ✓
- 6 个 `pdf_atoms_batch_3[567][ab].jsonl` 都存在 ✓
- 各 atom_id 命名空间无 cross-batch 冲突 (p<NNNN> partition 天然无冲突) ✓
- Rule D slot uniqueness #45/#46/#47 各 unique vs cumulative #1-#44 ✓
- (如 batch 36 drift cal triggered) `drift_cal_batch_36_p<XXX>_report.md` 存在 ✓

如有 halt_state_batch_NN.md 文件存在 → 处理 G-MS-4 fallback per round 7 1st LIVE-FIRE EFFECTIVE precedent (read halt_state + present 4 resume options to user OR proceed if user already authorized).

## §1 — Background

- Round 8 reconciler post 3 sister sessions B/C/D 物理并行 batches 35/36/37
- v1.4 prompts ACTIVE since 2026-04-28 (round 8 = 1st round running v1.4 baseline post v1.4 cut)
- Round 8 cumulative state pre-merge: 8552 atoms / 340 pages / 34 batches (post round 7 reconciler 2026-04-28)
- Expected post-round-8 state: ~9100-9200 atoms / 370 pages / 37 batches
- Rule D last burn pre-round-8: #44 omc:document-specialist (v1.4 cut reviewer 2026-04-28)
- Rule D round 8 added: #45 pr-review-toolkit:pr-test-analyzer + #46 superpowers:verification-before-completion + #47 claude-code-guide
- AUDIT pivot count post round 8: 28th cumulative
- Findings cumulative pre-round-8: 92 (O-P1-01..116); round 8 expected adds O-P1-117..128 (12 IDs reserved)

## §2 — Required Reads (并行)

1. `.work/06_deep_verification/_progress.json` (recovery_hint + v1_4_cut_completed)
2. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.4.md` (488 lines, v1.4 N1-N14)
3. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (master)
4. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_7.md` (last retro for context)
5. 3 个 sub-progress: `evidence/checkpoints/_progress_batch_3[567].json`
6. 3 个 batch reports: `evidence/checkpoints/P1_batch_3[567]_report.md`

## §3 — Cross-Batch Sibling Continuity Sweep (mandatory)

加载 6 个 batch jsonl + root pdf_atoms.jsonl (8552 atoms baseline). 按 (page, atom_index_on_page) 排序. 检查:

### §6.3 L3 chain
- sib=10 SC (batch 34, p.339)
- sib=11 SS (batch 35, p.342) NEW
- sib=12 Tumor/Lesion Domains (batch 35, p.344) NEW group container
- sib=13 VS (batch 36, p.358) NEW

### §6.3.10 SC L4 leaf-pattern chain (per N9)
- Description=1 (batch 34) + Spec=2 (batch 34 head + batch 35 tail) + Assumptions=3 (batch 35) + Examples=4 (batch 35)

### §6.3.11 SS L4 leaf-pattern chain (per N9)
- Description=1 + Spec=2 + Assumptions=3 + Examples=4 (all batch 35)

### §6.3.12 group container L4 chain (per N7 L4 group-container branch)
- §6.3.12.1 TU L4 sib=1 (batch 35)
- §6.3.12.2 TR L4 sib=2 (batch 35 head + batch 36 tail)
- §6.3.12.3 Tumor Identification/Tumor Results Examples L4 sib=3 (batch 36) — special "Examples" L4 sub-section under group container

### §6.3.12.X own L5 chains
- TU L5 chain Description=1/Spec=2/Assumptions=3/Examples=4 (batch 35)
- TR L5 chain Description=1/Spec=2/Assumptions=3/Examples=4 (batch 36)
- Examples L5 atoms under §6.3.12.3 (Example N L5 sib=1..N RESTART)

### §6.3.13 VS L4 leaf-pattern chain (per N9, batch 36)

### §6.4 chapter NEW transition (batch 37) — first chapter transition since §6.3 at p.180
- §6.4 chapter HEADING parent_section per N11 (chapter-short-bracket)
- §6.4.1/2/3 L3 sub-section intro children
- §6.4.4 FA L3 sib=4 leaf-pattern domain
- §6.4.5 SR L3 sib=5 (outside batch 37 scope, p.375)

### NEW7 L6 sub-batch context drift checks
- 35a→35b INTRA-batch handoff (per round 5 D-MS-4 codification + N6 v1.4 ALL L6 sub-headings)
- 36a→36b INTRA-batch handoff
- 37a→37b INTRA-batch handoff
- batch 35→36 CROSS-batch handoff §6.3.12.2 TR L4 chain continuation (per round 5 D-MS-2 + N6 v1.4)
- batch 36→37 CROSS-batch handoff §6.3.13 VS leaf-pattern → §6.4 chapter NEW (likely no cross-batch sib continuation since chapter-level transition)

### v1.4 N6 INTRA-AGENT consistency check (NEW round-7 dimension)
- 验 ALL sub-batches of same batch emit canonical L4/L5/L6/L7 chain form parent_section consistently from start (NOT bare L4/L5 form mixed)
- Cross-sub-batch L4 canonical drift check (per round 7 batch 34 O-P1-115 LOW precedent)

### v1.4 N8 NEW9 L2 short-bracket parent-skip check (round 7 NEW round-7 motif)
- 验 non-L3-HEADING atoms parent_section NOT match `^§\d+\.\d+ \[[A-Z\s]+\]$` L2 short-bracket pattern (only L3 sub-domain HEADING atoms allowed L2 chapter-short-bracket parent per N11)

Apply Option H any cross-batch sib gap / canonical-form drift / NEW9 violation; Rule B backup `.work/06_deep_verification/pdf_atoms.jsonl.pre-multi-35-37.bak` mandatory pre-merge.

## §4 — Sequential Merge

```bash
# Pre-merge backup
cp .work/06_deep_verification/pdf_atoms.jsonl .work/06_deep_verification/pdf_atoms.jsonl.pre-multi-35-37.bak

# Sequential merge (in batch order 35→36→37, sub-batch a→b)
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_35a.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_35b.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_36a.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_36b.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_37a.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_37b.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl

# Validate
wc -l .work/06_deep_verification/pdf_atoms.jsonl
python3 -c "import json; [json.loads(l) for l in open('.work/06_deep_verification/pdf_atoms.jsonl')]; print('JSON OK')"
```

验 0 collision / 0 schema err / pages 1-370 unique / atom_id unique.

## §5 — audit_matrix.md update

Append:
- 3 batch rows (35/36/37) with subagent_type alternation + atoms/repair_cycles/rule_a%
- 1 drift cal row (batch 36 p.<XXX> with NEW1 dual-threshold result + DIRECTION analysis if FAIL)
- 3 Rule A rows (35/36/37 with reviewer slot + family + AUDIT-mode reflection)
- Rule D Roster narrative: 44 → 47 (+3 slots: #45 pr-test-analyzer + #46 verification-before-completion + #47 claude-code-guide)
- AUDIT pivot count: 25 → 28 (+3)
- TOC anchor n=260 → n=290 (3 batches × 10 pages)
- Family pool status update: pr-review-toolkit family **6/6 COMPLETED** post #45 pr-test-analyzer (last agent burned) — 4th family pool exhausted post round 8 (after vercel + plugin-dev + feature-dev round 4)

## §6 — _progress.json update

- top-level pages_done 340 → 370
- atoms_done 8552 → final
- batches_done 34 → 37
- Rule D 44 → 47
- recovery_hint rewrite with round 8 narrative + cumulative state + next batch 38 prep
- status string append `_round_8_done`
- Add `round_8_compliance` block analogous to round_7_compliance

## §7 — MULTI_SESSION_RETRO_ROUND_8.md (Rule C 强制三段式)

写 `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_8.md` 含:
- Headline metrics table (round 1-8 累 8 列)
- Per-batch breakdown (35/36/37 + reconciler)
- §1 保留下来的做法 (R-MS-1..N round 8 reaffirmed/extended)
- §2 必须补上的缺口 (G-MS-NEW-8-* round 8 surfaces)
- §3 关键决策 (D-MS-1..N round 8 decisions)
- §4 Rule A/B/C/D/E 合规
- §5 跨 retro 呼应
- §6 Next batch 38 readiness
- §7 Cleanup readiness (round 8 one-shot files: batch_35/36/37_kickoff.md + reconciler_kickoff_round8.md)

也写 `.work/06_deep_verification/multi_session/sibling_continuity_sweep_report_round8.md` (sweep evidence + Option H fixes if any).

**Critical milestones to highlight in retro**:
- v1.4 prompts ACTIVE 1st round running baseline (round 8 = 1st post v1.4 cut)
- 4 EMERGENCY-CRITICAL hooks 1st live-fire check: N3 NEW8.d (whole-row) + N5 (TABLE_ROW empty-cell) + N6 (ALL L6 + INTRA-AGENT) + N8 NEW9 (L2 short-bracket FORBID)
- pr-review-toolkit family 4th-agent intra-family depth burn = FIRST 4th-agent for ANY family in P1 cumulative (slot #45 pr-test-analyzer)
- pr-review-toolkit family 6/6 COMPLETED post round 8 (4th family pool exhausted)
- claude-code-guide family INAUGURAL burn (NEW family AUDIT pivot 28th)
- §6.4 chapter NEW transition first chapter-level transition since §6.3 at p.180
- N14 strict alternation methodology 2nd live-fire (post round 7 1st live-fire EFFECTIVE)
- v1.5 candidate accumulation (any new round-8 motifs)

## §8 — Commit + Push + User Report

### Commit (single commit)
```bash
git add .work/06_deep_verification/ \
  .work/MANIFEST.md \
  .work/meta/worklog.md \
  CLAUDE.md \
  docs/PROGRESS.md

git commit -m "$(cat <<'EOF'
06 Deep Verification P1 batch 35/36/37 multi-session round 8 + reconciler closure (post v1.4 cut 1st round running v1.4 baseline)

Round 8 multi-session physical parallel: 3 sister sessions B/C/D + reconciler E
- Atoms: 8552 → <final> (+<N>)
- Pages: 340 → 370 (+30, p.341-370)
- Batches: 34 → 37
- Findings: 92 → <final> (+<N>: O-P1-117..128)
- Rule D: 44 → 47 (+3 AUDIT-mode pivots #25-#28: pr-review-toolkit:pr-test-analyzer 4th-agent intra-family depth burn FIRST 4th-agent for ANY family in P1 + superpowers:verification-before-completion 2nd burn intra-family + claude-code-guide INAUGURAL 28th pivot)
- pr-review-toolkit family 6/6 COMPLETED (4th family pool exhausted post round 8 after vercel+plugin-dev+feature-dev round 4)
- v1.4 baseline 1st round running 4 EMERGENCY-CRITICAL hooks live-fire validation: N3 NEW8.d whole-row + N5 TABLE_ROW empty-cell + N6 ALL L6 sub-headings + INTRA-AGENT consistency + N8 NEW9 L2 short-bracket FORBID
- Drift cal batch 36 p.<XXX> NEW1 8th time + N14 strict alternation 2nd live-fire (round 7 1st live-fire EFFECTIVE precedent)
- §6.4 chapter NEW transition (first chapter-level transition since §6.3 at p.180) + N9 leaf-pattern + N11 chapter-short-bracket extension validations
- Reconciler-side fixes: <N> atoms (cross-batch sib continuity / N6 ALL L6 / N9 / N14 / NEW9 sweep)
- MULTI_SESSION_RETRO_ROUND_8.md 写完 (Rule C 三段式)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"

git push origin main
```

### User-facing summary (single echo + 5-8 sentence summary)
```
ROUND_8_DONE atoms=<N> pages=370 batches=37 findings=<N> rule_d=47 audit_pivots=28 pr_pool_completed=true v1_4_baseline_first_round=true drift_cal_batch_36=<verdict> §6.4_chapter_NEW=validated
```

## NEVER DO

- 主 session 自审 (Rule D 违规)
- 改 schema (frozen v1.2 carry-forward)
- 改 PLAN v0.6 内容
- 删 v1.4 prompts primary 副本
- 跑额外 PDF atomization (本任务 reconciler-only merge + sweep + retro + commit)
- Touch CLAUDE.md (除 STEP 8 cleanup if user 决定 round 9 not immediately scheduled — remove round 8 routing rule)

## 验收标准

- ✅ 6 sub-batch jsonl merged into root pdf_atoms.jsonl (0 collision / 0 schema err)
- ✅ Cross-batch sibling continuity sweep applied + Option H fixes if needed
- ✅ INTRA-AGENT consistency check applied (v1.4 N6 NEW round-7 dimension)
- ✅ NEW9 L2 short-bracket parent-skip sweep applied
- ✅ audit_matrix.md updated (3 batch rows + 1 drift cal row + 3 Rule A rows + Rule D 47 + n=290 + 28 pivots + pr-family COMPLETED)
- ✅ _progress.json updated (370/8552→final/37 + recovery_hint rewritten + round_8_compliance block)
- ✅ MULTI_SESSION_RETRO_ROUND_8.md written (Rule C 三段式)
- ✅ sibling_continuity_sweep_report_round8.md written
- ✅ Single commit pushed to origin/main
- ✅ User-facing summary echoed
- (optional cleanup) ⏳ user decides round 9 schedule before deleting round 8 one-shot kickoffs + removing CLAUDE.md routing rule

The boulder never stops. STEP 0 pre-flight check first.
