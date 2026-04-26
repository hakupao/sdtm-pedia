# Reconciler Kickoff (Multi-Session Parallel — Session E, Round 3 batches 20/21/22)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 8 STEPs (sibling sweep + sequential merge + audit_matrix update + _progress.json update + v1.3 cut decision + retro + cleanup recommendations + final message) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一合法收尾信号是 STEP 8 echo `RECONCILER_DONE_ROUND_3 root_atoms=<N> pages_done=220 batches_done=22 sibling_fixes=<N> v1.3_cut=<yes|no> retro_written=true` 单行 + user-facing summary.
>
> Halt-only fallback (per G-MS-4 round 2 spec): 若 sister session 写了 `halt_state_batch_NN.md` → 走 STEP 0.5 decision tree.
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel 实验 round 3 的 **reconciler (session E)**.
> 仅在 session B (batch 20) + session C (batch 21) + session D (batch 22) **全 PARALLEL_SESSION_NN_DONE** 后启动.
> 你的职责: 串行合并 3 个独立 batch 工作到 root + audit_matrix + _progress.json + 写 round-3 retro + 决定是否 cut formal v1.3 prompt (round 3 evidence saturation 应 unblock cut OR 显式 defer 给 dedicated session).

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 + Pre-flight Check
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `multi_session/MULTI_SESSION_PROTOCOL.md`
2. `multi_session/MULTI_SESSION_RETRO.md` (round 1)
3. `multi_session/MULTI_SESSION_RETRO_ROUND_2.md` (round 2 — G-MS-11/G-MS-12 round 2 NEW 缺口)
4. `evidence/checkpoints/_progress_batch_20.json`
5. `evidence/checkpoints/_progress_batch_21.json`
6. `evidence/checkpoints/_progress_batch_22.json`
7. `audit_matrix.md` (current state, 109 lines post round 2)
8. `_progress.json` (current state)

### Pre-flight 验:
- 3 sub-progress JSON 都 `status="completed"` ✓
- 6 batch jsonl + 3 batch report + (drift cal batch 21 report)
- Reviewer slot uniqueness: #29 plugin-dev:skill-reviewer + #30 oh-my-claudecode:test-engineer + #31 oh-my-claudecode:git-master (无 cross-batch + 无 cross-round 撞 — 验 _progress_batch_NN.json reviewer_slot 字段 + audit_matrix Rule D Roster #1-#28 累)
- Drift cal: batch 20 + 22 = skipped, batch 21 = triggered NEW1 dual-threshold
- Halt state 检查: 任一 session 写 `halt_state_batch_NN.md` → STEP 0.5 G-MS-4 fallback

任一验证失败 → halt + 报告. **不要** 私自 fix sub-session 的输出.

### Step 0.5 — G-MS-4 Halt Fallback Decision Tree (round 2 spec'd, round 3 live-ready)

读 halt_state.md → recommended_fallback 字段 → 决策:
- (a) reconciler retry 全 batch — 主 session 改派 reconciler 自身重跑该 batch 单 session 单 a+b
- (b) reconciler defer 本 batch + merge sister batches only
- (c) reconciler abort experiment — 报告 user, 不动 root, 全 partial work 归档 Rule B

写 `multi_session/halt_resolution_round3.md` 决策记录.

═══════════════════════════════════════════════════════════════════
## STEP 1 — Cross-Batch Sibling Continuity Sweep
═══════════════════════════════════════════════════════════════════

加载 root pdf_atoms.jsonl + 6 batch files + 全部按 (page, atom_index_on_page) 排序.

### 检查项 (round 3 PDF p.4 PRE-VERIFIED 2026-04-26):

**Round 3 batches 20-22 实际 page→section 结构** (per PDF p.4 TOC):
- p.191-192: §6.3.3 EG tail (Examples N L5 续 batch 19)
- p.193: §6.3.4 IE (Inclusion/Exclusion Criteria Not Met) NEW
- p.194-195: §6.3.5 group container intro + §6.3.5.1 Generic Spec template
- p.196-198: §6.3.5.2 BS
- p.199-219: §6.3.5.3 CP (跨 batch 20 head + 21 全 + 22 tail = 21 页)
- p.220: §6.3.5.4 GF NEW (batch 22 末)

**§6.3.5 deep-nesting Level Model** (round 3 NEW vs round 1+2 flat structure):
- §6.3.5 group = L3 sib=5 under §6.3 (新 chapter-internal section, parent='§6.3 [MODELS FOR FINDINGS DOMAINS]')
- §6.3.5.X individual domains = L4 sib=1..9 under §6.3.5 (parent='§6.3.5 Specimen-based Findings Domains')
- 各 §6.3.5.X 的 Description / Spec / Assump / Examples = **L5** (NEW7 chain 但 level +1)
- 各 §6.3.5.X.Examples N = **L6**

### 检查项:

1. **§6.3.x sub-domain L3 sib chain under §6.3 chapter** contiguous: batch 18 §6.3.1 DA=1 / batch 19 §6.3.2 DD=2 / §6.3.3 EG=3 / batch 20 §6.3.4 IE=4 / batch 20 §6.3.5 group=5. 验 §6.3.4 IE p.193 + §6.3.5 group p.194 chain 续号 ✓.

2. **§6.3.5.X L4 sib chain under §6.3.5 group** contiguous: batch 20 §6.3.5.1=1 / §6.3.5.2 BS=2 / §6.3.5.3 CP=3 + batch 22 §6.3.5.4 GF=4. 验 chain 续号 ✓.

3. **L5 sub-section deterministic chain per NEW7** at deep-nesting (round 3 NEW): 各 §6.3.5.X domain L5 chain Description=1/Spec=2/Assump=3/Examples=4 ± References=5 — 验 §6.3.5.2 BS / §6.3.5.3 CP / §6.3.5.4 GF 各 own L5 chain ✓.

4. **L6 Examples N chain restart per §6.3.5.X domain** (independent across domains, 续号 within domain across batches): 验 CP-Examples L6 sib chain 跨 batches 20→21→22 continuous (CP 跨 3 batches 21 页, Examples N 续号 contiguous) + GF-Examples L6 restart sib=1 if applicable.

5. **NEW6 parent_section dual-form sweep** (round 2 G-MS-11 修补 codified):
   - Chapter-level (§6 / §6.2 / §6.3): `§N.N [TITLE-ALL-CAPS]` short-bracket all-caps
   - L3 sub-domain group (§6.3.5): `§6.3.5 Specimen-based Findings Domains` canonical full-form (no CODE)
   - L4 §6.3.5.X individual domain: `§6.3.5.X Title (CODE)` canonical full-form (e.g., `§6.3.5.2 Biospecimen Findings (BS)`)
   - L5+ atom parent: same canonical full-form as L4 domain
   - Inline Option H fix any deviation.

6. **R15 cross-batch boundary check** — 4 boundaries critical:
   - batch 19→20: EG L5 Examples sib continuation OR EG end + IE NEW
   - batch 20→21: §6.3.5.3 CP L5 sub-section sib continuation
   - batch 21→22: §6.3.5.3 CP L5/L6 sib continuation
   - batch 22 内: CP→GF L4 sub-domain transition at p.220 (R12 sub-domain-level discipline)
   per round 2 5-atom batch 18 NEW6 lesson — sub-sessions blind to sister state, reconciler 是 safety net.

7. **R12 transition page sweep** — 验 p.193 EG→IE / p.194 IE→§6.3.5 group / p.196 §6.3.5.1→BS / p.199 BS→CP / p.220 CP→GF 各 transition page 3-zone partition + ≥8 atoms 期望.

8. **(注: batch 22 NOT 触 §6.4 chapter** — TOC §6.4 = p.361 远超 batch scope, batch 22 末仅触 §6.3.5.4 GF NEW sub-domain transition at p.220).

### Apply Option H fix for any cross-batch sib gap / NEW6 / NEW7 violation
任何 violation → inline fix in batch file + accumulate finding O-P1-55+ LOW (类 round 2 O-P1-54 pattern).

写 `multi_session/sibling_continuity_sweep_report_round3.md`.

═══════════════════════════════════════════════════════════════════
## STEP 2 — Sequential Merge to Root
═══════════════════════════════════════════════════════════════════

### Step 2.1: Backup root
```bash
cp pdf_atoms.jsonl pdf_atoms.jsonl.pre-multi-20-22.bak
```

### Step 2.2: Append in batch order
```bash
cat evidence/checkpoints/pdf_atoms_batch_20a.jsonl evidence/checkpoints/pdf_atoms_batch_20b.jsonl evidence/checkpoints/pdf_atoms_batch_21a.jsonl evidence/checkpoints/pdf_atoms_batch_21b.jsonl evidence/checkpoints/pdf_atoms_batch_22a.jsonl evidence/checkpoints/pdf_atoms_batch_22b.jsonl >> pdf_atoms.jsonl
```

### Step 2.3: Final integrity sweep
- `wc -l pdf_atoms.jsonl` 期望 = 4894 + sum(3 batch atoms)
- python3 验: 0 schema error + 0 atom_id collision + pages 1-220 全 220 unique + atom_type distribution sanity

═══════════════════════════════════════════════════════════════════
## STEP 3 — Audit_Matrix Update
═══════════════════════════════════════════════════════════════════

Append 到 `audit_matrix.md`:

### Step 3.1: P1 Batch Roster table 加 3 行 (batches 20/21/22)
### Step 3.2: P1 Drift 校准 table 加 1 行 (batch 21 NEW1 dual-threshold result)
### Step 3.3: P1 Rule A 独审 table 加 3 行 (batches 20/21/22)
### Step 3.4: Rule D Roster 累计 update
- 28 → 31 (3 new slots: #29 plugin-dev:skill-reviewer + #30 oh-my-claudecode:test-engineer + #31 oh-my-claudecode:git-master)
- Reviewer quality 观察 段加 3 个 slot 评价
- 结论段 update: n=140 cumulative anchored audit (n=110 prior + 30 new), 14 consecutive batches, 4 families validated (pr/omc/vercel-pool-exhausted/plugin-dev-pool-completed if #29 plugin-dev:skill-reviewer is plugin-dev's 3rd burn → completes plugin-dev family)
- 12 AUDIT-mode pivots cumulative (#20-#31)

═══════════════════════════════════════════════════════════════════
## STEP 4 — _progress.json Update
═══════════════════════════════════════════════════════════════════

Update headline:
- pages_done: 190 → **220**
- atoms_done: 4894 → final (4894 + 3 batch contributions)
- batches_done: 19 → **22**
- failures_done: 1 → 1 + sum(3 batch failures, expect 0)
- last_updated: 2026-04-26 (or current)
- status: "P1_batch_20_21_22_DONE_via_multi_session_parallel_round_3..."

Rewrite recovery_hint with 3-batch summary + cross-batch lessons + Round 3 vs round 2 comparison + next batch 23 kickoff prep + Rule D 烧 31 (3 families remaining: pr-exhausted-mostly / omc-pool-deep / plugin-dev-completed-if-applicable / new candidates from data/firecrawl/superpowers/codex/feature-dev/general-purpose for round 4).

═══════════════════════════════════════════════════════════════════
## STEP 5 — v1.3 Prompt Formal Cut Decision (FINAL CALL — 2nd opportunity post round 2 RECOMMENDED)
═══════════════════════════════════════════════════════════════════

Round 2 reconciler RECOMMENDED v1.3 cut + DEFERRED execution. Round 3 reconciler 2nd opportunity:

### Decision matrix:
- 若 v1.3 cut **STILL DEFERRED** (e.g. user 决定 dedicated session 跑) → 不动 prompt files + 文档 RECOMMENDED 第 2 次 + 推荐 EVEN-MORE-STRONGLY schedule v1.3 cut session BEFORE batch 24 drift cal next mandatory
- 若 v1.3 cut **EXECUTED** (e.g. dedicated session 已跑 OR user 显式授权) → archive v1.2 + activate v1.3 + update batch 23+ kickoff prompts to use v1.3

### v1.3 cut 执行 (若决定 cut):
- 写 `subagent_prompts/P0_writer_pdf_v1.3.md` (full clean rule set: R1-R15 + O-P1-26 codified + NEW1-NEW7 incorporated + NEW6 dual-form codified per round 2 G-MS-11 + density alarm threshold codified per round 2 G-MS-12)
- Archive v1.2 → `subagent_prompts/archive/v1.2_final_2026-04-26/`
- Update batch 23+ kickoff prompt to use v1.3
- 同时 cut companion: `P0_writer_md_v1.3.md` + `P0_matcher_v1.3.md` + `P0_reviewer_v1.3.md` (if scope evolved)

═══════════════════════════════════════════════════════════════════
## STEP 6 — Session-End Retro (Rule C 强制, Round 3)
═══════════════════════════════════════════════════════════════════

写 `multi_session/MULTI_SESSION_RETRO_ROUND_3.md` (Rule C 三段式, separate from round 1+2 retros):

### §1 保留下来的做法 (round 3 reaffirmed/extended)
- Multi-session parallel 三轮验 (round 1 ~50% + round 2 ~52% + round 3 ?% wall savings)
- Rule D pool partition cross-round 验 (#29-#31 vs round 1 #22-#24 + batch 16 #25 + round 2 #26-#28 = 0 cross-round collision)
- TOC anchor + R-rules unified shared 三轮验 (n=140 cumulative anchored audit 0 FP / 0 inversion target)
- NEW6 dual-form codification (G-MS-11 round 2 修补) 实测 round 3 (是否 0 chapter-parent format split — 若 0 → ✅ 修补 effective)
- Density alarm threshold (G-MS-12 round 2 修补) 实测 round 3 (是否 caught any writer-family under-extraction proactively)
- NEW1 dual-threshold drift cal 第 2 次实测 (batch 21 — 验是否再次 STRONGLY VALIDATED as designed)
- AUDIT-mode pivot 跨 4-family 多 burn depth (post round 3: pr×1 / omc×5+ / vercel-exhausted / plugin-dev-completed-2-or-3)
- G-MS-7 finding ID range pre-allocation 第 3 次验 (是否 0 cross-session collision)
- G-MS-4 halt fallback decision tree spec round 3 实测 (若任一 session halt OR 仍未触发 spec-only)

### §2 必须补上的缺口 (round 3 surfaces)
- 各 session blindness recur (round 1+2 不变)
- Drift cal cumulative cadence cross-batch state (round 1+2 不变)
- 任何 sub-session halt → reconciler decision tree (G-MS-4 spec'd)
- 如 round 3 surfaces 新 NEW6/NEW7/R15 violation pattern → G-MS-13+ candidate
- 如 round 3 surfaces v1.3 cut 仍 deferred 第 2 次 → escalate to user as HIGH

### §3 关键决策
- Round 3 multi-session 节省 vs round 1+2 比较
- 是否继续 multi-session round 4 (batches 23-25) — 取决 v1.3 cut 状态 + round 3 verdict
- v1.3 formal cut 是否 unblock 后续 (e.g. R-rules locked → 各 session prompt 更稳定 → 协调成本降)
- Multi-session 是否提升 Tier 3 default pattern (3 rounds saturation 后)

═══════════════════════════════════════════════════════════════════
## STEP 7 — Optional Cleanup
═══════════════════════════════════════════════════════════════════

可选 (不强制):
- 删除 round 3 one-shot kickoff (`batch_20_kickoff.md` + `batch_21_kickoff.md` + `batch_22_kickoff.md` + `reconciler_kickoff_round3.md`)
- 累计 round 1+2+3 one-shot kickoffs delete candidate = 11 files
- 留 MULTI_SESSION_PROTOCOL.md + 3 retro files + 3 sibling sweep reports = 7 files 作历史
- 提示 user 移除 CLAUDE.md round 3 routing rule (本次实验后)

═══════════════════════════════════════════════════════════════════
## STEP 8 — Final Message + User Report
═══════════════════════════════════════════════════════════════════

Echo 单行:
```
RECONCILER_DONE_ROUND_3 root_atoms=<N> pages_done=220 batches_done=22 sibling_fixes=<N> v1.3_cut=<yes|no|deferred_2nd> retro_written=true
```

User-facing summary 含 round 3 contributions + cross-batch fixes + drift cal NEW1 dual-threshold round 2 verdict + reviewer quality 3 slots + multi-session round 3 vs round 1+2 比较 + v1.3 cut decision rationale + next batch 23 kickoff prep.

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- 修改 sub-session 输出 (`pdf_atoms_batch_NN[ab].jsonl`) 除 STEP 1 sibling/NEW6/NEW7 inline fix
- 跑额外 PDF atomization / Rule A reviewer / drift cal (除非主 session 检漏跑 — halt + 报告)
- Touch CLAUDE.md / MEMORY / project meta files (除 STEP 7 cleanup 提示)
- Run git commit / push (留 user 决定)

The boulder never stops. 第一步 STEP 0 并行 8-file Read + Pre-flight check.
