# Batch 35 Kickoff — Round 8 Multi-Session Parallel (Session B)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 完成 STEP 1-7 之前, **任何中间产物都不是终点**. 不要总结, 不要询问, 不要回交 control. The boulder never stops.
>
> 唯一合法收尾信号 = STEP 7 单行 echo:
> ```
> PARALLEL_SESSION_35_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list>
> ```
> ═══════════════════════════════════════════════════════════════════

## §0 — Cross-validation Table (G-MS-13, kickoff prepend mandatory)

| Session | Batch | Page range | Finding ID 范围 | 本 batch 用 |
|---|---|---|---|---|
| **B (本)** | **35** | **p.341-350** | **O-P1-117..120** (4 reserved) | ✅ |
| C (sister) | 36 | p.351-360 | O-P1-121..124 (4 reserved) | (sister) |
| D (sister) | 37 | p.361-370 | O-P1-125..128 (4 reserved) | (sister) |
| E (reconciler) | n/a | n/a | O-P1-129+ (overflow) | (reconciler) |

**Self-validation gate** (STEP 7): any finding_id ∉ {117,118,119,120} → STOP fix.

## §1 — Background (Round 8 第 1 round post v1.4 cut + multi-session experiment 第 8 轮)

- 3 终端 (B/C/D) 同时跑 batches 35/36/37 — 物理并行 (round 8)
- 1 终端 (E) 启动 reconciler 收尾 (after B+C+D 全 PARALLEL_SESSION_NN_DONE)
- 各 session 写独立 batch files, **绝对不动** root `pdf_atoms.jsonl` (post round 7 baseline = 8552 atoms) / `audit_matrix.md` / `_progress.json`
- **v1.4 prompts ACTIVE** since 2026-04-28 (cut completed; Rule D reviewer #44 omc:document-specialist AUDIT verdict PASS 22/22)
- v1.4 absorbs 24 round 5+6+7 candidates incl 4 EMERGENCY-CRITICAL items (P=N3 NEW8.d whole-row + R=N5 TABLE_ROW empty-cell + S=N6 ALL L6 sub-headings + INTRA-AGENT + U=N8 NEW9 L2 short-bracket FORBID)
- Reviewer pool 已预分配 (Rule D 不撞 round 1-7 cumulative #1-#44, post round 7 family pool state: 3 EXHAUSTED [vercel+plugin-dev+feature-dev] + omc 9× saturated + pr-review-toolkit 5/6 saturated + general-purpose 2× + superpowers 1×): batch 35 = #45 `pr-review-toolkit:pr-test-analyzer` (**pr-family 4th-agent intra-family depth burn** = FIRST 4th-agent intra-family depth burn for ANY family in P1 cumulative; validates AUDIT recipe at 4-agent depth scale; **AUDIT pivot 26th cumulative**) / batch 36 = #46 `superpowers:verification-before-completion` (superpowers family 2nd burn intra-family depth + drift cal carrier 8th time, AUDIT pivot 27th) / batch 37 = #47 `claude-code-guide` (claude-code-guide family INAUGURAL burn, NEW family AUDIT pivot 28th)
- Round 8 protocol sustains round 7 spec: G-MS-4 halt fallback (round 7 1st LIVE-FIRE EFFECTIVE — accept resume via halt_state file + user authorization fallback) + G-MS-7 finding ID range pre-allocation + G-MS-13 cross-validation table at top of each kickoff + N14 strict alternation methodology procedural enforcement (drift cal in batch 36 only)
- 🔴 **NEW7 L6 sub-batch handoff codification status** — 5 cumulative recurrences pre-round-8 (round 3 batch 23 + round 4 batch 25 + round 5 reconciler + round 6 batch 29 + round 7 batch 33 INTRA-AGENT inconsistency NEW dimension). Round 8 v1.4 N6 ACTIVE: handoff template extended to ALL L6 sub-headings (Examples + non-Example like Conclusions/Suggestions/Datasets/Records/Description/Specification/Assumptions/References) + INTRA-AGENT consistency check field (ALL sub-batches of same batch MUST emit canonical L4/L5/L6/L7 chain form parent_section consistently from start). 主 session dispatch sub-batch 35b prompt MUST inline-prepend prior sub-batch 35a 终态. 主 session dispatch batch 35a prompt MUST inline-prepend prior batch 34b 终态 (per cross-BATCH handoff codification round 5 D-MS-2 + N6 v1.4).
- batch 35 NO drift cal (batch 36 mandatory)
- 每 kickoff 顶部 HARD-STOP DIRECTIVE — 唯一合法停止 = `PARALLEL_SESSION_35_DONE` 单行 echo OR `HALT_BATCH_35 reason=<X>` halt 信号

## §2 — Required Reads (并行 Read, ≤300 lines each)

1. `.work/06_deep_verification/_progress.json` (top-level + recovery_hint + v1_4_cut_completed)
2. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.4.md` (488 lines, MAIN writer base) — note v1.4 N1-N14 14 NEW patches + Self-Validate hooks 14 items
3. `.work/06_deep_verification/subagent_prompts/P0_reviewer_v1.4.md` (273 lines, Rule D reviewer base) — note Rule D roster 43 + v1.4 fix matrix 22 items A-V
4. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (master 219 lines)
5. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_7.md` (round 7 retro for context — G-MS-4 1st LIVE-FIRE + alternation 1st live-fire EFFECTIVE)
6. `source/SDTMIG v3.4 (no header footer).pdf` p.4-5 TOC ground truth (verify §6.3.10 SC ends ~p.341 / §6.3.11 SS p.342 / §6.3.12 TU group p.344 / §6.3.12.1 TU L4 p.344 / §6.3.12.2 TR L4 p.350)

**附读** (batch 34 terminal state for cross-BATCH handoff): `evidence/checkpoints/_progress_batch_34.json` — last L4/L5/L6/L7 sib state

## §3 — Pre-shared State + Cross-Batch Handoff (N6 v1.4 mandatory)

```
PRIOR BATCH 34 HEADING STATE (batch 35 sub-batch a MUST continue, NOT restart):
- Last L3 sib used (under §6.3 [MODELS FOR FINDINGS DOMAINS]): sib=10 (§6.3.10 SC at p.339)
- Last L4 sib used (under §6.3.10 SC): sib=2 ('SC – Specification' at p.340; head — Spec table likely continues into p.341)
- Last L5 sib used (under §6.3.10 SC L4): NONE yet (SC L4 chain hasn't entered L5 — Spec is L4 head; L5 chain Description/Spec/Assumptions/Examples NOT applicable for SC leaf-pattern; SC follows pre-canonical L4 layout per N9 NEW7 L3 leaf-pattern: Description=L4 sib=1 + Specification=L4 sib=2 / Assumptions=L4 sib=3 / Examples=L4 sib=4)
- Last L6 sib used: NONE (SC L4-leaf, no L6 yet)
- Last L7 sib used: NONE (no L7 in SC scope yet)
- Convention: SC follows N9 leaf-pattern (Description=1/Spec=2/Assumptions=3/Examples=4 at L4); §6.3.10 SC L3 single-domain (NOT group container); v1.4 N10 leaf-pattern Examples-at-L5 distinction applies
- §6.3.10 SC L4 atom parent = '§6.3.10 Subject Characteristics (SC)' canonical full-form (NEVER self-parent per NEW6.b)
- L5/L6 atoms (when entered) parent = '§6.3.10 Subject Characteristics (SC)' canonical full-form (NOT bare shortcut per O-P1-91/N7)
- §6.3.11 SS L3 sib=11 NEW at p.342 — leaf-pattern (single-domain L3 like SC; NOT group container)
- §6.3.12 Tumor/Lesion Domains L3 sib=12 NEW at p.344 — GROUP CONTAINER (analogous to §6.3.5 / §6.3.7 / §6.3.9; sub-domains TU + TR + Examples)
- §6.3.12.1 Tumor/Lesion Identification (TU) L4 sib=1 NEW at p.344 — under group container per N7 L4 group-container branch
- §6.3.12.2 Tumor/Lesion Results (TR) L4 sib=2 NEW at p.350 — barely starts at p.350 edge (likely cross-batch into batch 36)
```

## §4 — Steps (sequential, no skip)

### STEP 1: TOC verify + main session pre-dispatch state cross-validation
- Read PDF p.4 TOC for §6.3.10/11/12 page boundaries (above)
- Cross-validate root `pdf_atoms.jsonl` tail (last 50 atoms ≈ p.339-340 batch 34) with handoff state above per O-P1-93 round 6 procedural enforcement gap
- Confirm: §6.3.10 SC L3 sib=10 + L4 Spec head at p.340 ✓

### STEP 2: Dispatch 35a (oh-my-claudecode:executor OR oh-my-claudecode:writer per alternation; recommend executor)
- Pages: p.341-345 (~5 pages)
- Output: `evidence/checkpoints/pdf_atoms_batch_35a.jsonl`
- Inline-prepend cross-BATCH handoff state from §3 above
- Expected content: §6.3.10 SC Spec table tail (p.341) + §6.3.10 SC Assumptions L4 sib=3 + §6.3.10 SC Examples L4 sib=4 + Examples N at L5 (per N9 leaf-pattern Examples-at-L5) + §6.3.11 SS L3 sib=11 NEW (p.342) + SS L4 chain Description/Spec head + §6.3.12 Tumor/Lesion Domains L3 sib=12 NEW (p.344 group container) + §6.3.12.1 TU L4 sib=1 NEW (p.344 under group container per N7) + TU L5 chain Description=1/Spec=2 head
- Wait for DONE, capture atoms count

### STEP 3: Dispatch 35b (alternation per N14: opposite of 35a; e.g. if 35a=executor → 35b=writer)
- Pages: p.346-350 (~5 pages)
- Output: `evidence/checkpoints/pdf_atoms_batch_35b.jsonl`
- Inline-prepend prior sub-batch 35a 终态 (last L4/L5/L6/L7 sib + Examples convention + N6 ALL L6 sub-headings + INTRA-AGENT consistency check per v1.4)
- Expected content: §6.3.12.1 TU L5 chain continuation (Spec / Assumptions / Examples) + TU L6 Examples N RESTART per §6.3.12.1 + §6.3.12.2 TR L4 sib=2 NEW (p.350 edge — head only)

### STEP 4: Pre-reviewer schema sweep (Option H if needed)
- 验 6 atom schema: 9-enum atom_type / R10 strict verbatim / TABLE_ROW pipe-count regex (v1.4 N5) / NEW2 11+ chars Cyrillic homoglyph (v1.4 N2) / NEW8 oracle SUPPQUAL (v1.4 N1) / NEW8.d whole-row (v1.4 N3 EMERGENCY-CRITICAL) / NEW9 L2 short-bracket parent FORBID (v1.4 N8 — non-L3-HEADING atoms)
- Density alarm check (v1.4 N12 LIST_ITEM-heavy floor 8 / sub-batch floor 80 if applicable)
- INTRA-AGENT consistency check (v1.4 N6: ALL sub-batches MUST emit canonical chain form consistently)
- Apply Option H any defects + Rule B backup `pdf_atoms_batch_35[ab].jsonl.pre-OptionH-*.bak`

### STEP 5: Rule A 10-atom audit via reviewer slot #45 `pr-review-toolkit:pr-test-analyzer`
- AUDIT-mode pivot 26th cumulative (pr-review-toolkit family 4th-agent intra-family depth burn — first 4th-agent intra-family depth burn for ANY family in P1)
- Mode prompt: `"Mode: AUDIT for SDTM PDF atomization quality, NOT PR test coverage analysis on TypeScript/code tests / NOT test gap detection / NOT critical test coverage review for PRs"`
- Sample: 10 atoms stratified 1/page (p.341-350)
- Output: `evidence/checkpoints/rule_a_batch_35_sample.jsonl` + `rule_a_batch_35_verdicts.jsonl` + `rule_a_batch_35_summary.md`
- Threshold: ≥80% raw weighted (PASS) / WARN band 70-90% / FAIL <70%
- 4-agent intra-family depth burn precedent: pr-review-toolkit family burned 4× total post batch 35 = code-simplifier round 1 + code-reviewer round 6 + silent-failure-hunter round 6 + comment-analyzer round 7 + type-design-analyzer round 7 + pr-test-analyzer round 8 (LAST agent; family pool COMPLETED)

### STEP 6: Drift cal SKIP (next mandatory at batch 36 per cadence)

### STEP 7: Compose `_progress_batch_35.json` + `P1_batch_35_report.md` + DONE echo
- Single-line DONE: `PARALLEL_SESSION_35_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list O-P1-117..120 used>`

## §5 — Drift cal trigger schedule (本 batch SKIP)

- Batch 35: SKIP (cumulative since batch 33 p.325 ~250 atoms; per cadence next at batch 36)
- Batch 36 (sister C): MANDATORY (every-3-batches batch 33→36 + cumulative ≥600 双触发; per N14 strict alternation table)
- Batch 37 (sister D): SKIP

## §6 — Halt conditions (per session — halt + write `halt_state_batch_35.md` + 4 resume options A-D + wait user auth per G-MS-4 round 7 1st LIVE-FIRE EFFECTIVE precedent)

- writer failure rate >15%
- drift cal 2-way <80% (n/a 本 batch)
- Rule A raw FAIL <70%
- ctx 用量超 80%
- 预分配 reviewer 不可派发 (Rule D 撞风险 — write halt_state per G-MS-4)
- 任何尝试写 shared file 的代码路径
- INTRA-AGENT inconsistency detected (v1.4 N6 NEW round-7 dimension — sub-batches divergent canonical chain form)

## §7 — Final message format (single-line echo)

```
PARALLEL_SESSION_35_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-117,...>
```

## §8 — Do NOT touch (shared files reserved for reconciler)

```
.work/06_deep_verification/
  pdf_atoms.jsonl                            ← root, reconciler 串行 merge
  audit_matrix.md                            ← reconciler 串行 append
  _progress.json                             ← reconciler 串行 update
  subagent_prompts/*                         ← v1.4 active 不动
  schema/*.json                              ← 不动
  PLAN.md                                    ← v0.6 不动
  plans/*.md                                 ← 不动
  multi_session/sibling_continuity_sweep_report*.md ← 历史
  multi_session/MULTI_SESSION_PROTOCOL.md    ← 历史
  multi_session/MULTI_SESSION_RETRO_*.md     ← 历史
  evidence/checkpoints/halt_state_batch_32.md ← G-MS-4 1st LIVE-FIRE 历史 evidence (round 7 D-MS-8)
```

CLAUDE.md / MEMORY 类全项目文件: **绝对不动**.

`pdf_atoms.jsonl.pre-multi-*-*.bak` 历史 backup: **绝对不动**.

The boulder never stops. STEP 1 并行 6-file Read.
