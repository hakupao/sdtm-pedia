# Reconciler Kickoff (Multi-Session Parallel — Session E, Round 4 batches 23/24/25)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 8 STEPs (sibling sweep + sequential merge + audit_matrix update + _progress.json update + v1.3 cut decision + retro + cleanup recommendations + final message) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一合法收尾信号是 STEP 8 echo `RECONCILER_DONE_ROUND_4 root_atoms=<N> pages_done=250 batches_done=25 sibling_fixes=<N> v1.3_cut=<yes|no|deferred_3rd> retro_written=true` 单行 + user-facing summary.
>
> Halt-only fallback (per G-MS-4 round 2 spec): 若 sister session 写了 `halt_state_batch_NN.md` → 走 STEP 0.5 decision tree (carry-forward from round 2+3 spec, live-fire still NOT triggered through round 3).
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel 实验 round 4 的 **reconciler (session E)**.
> 仅在 session B (batch 23) + session C (batch 24) + session D (batch 25) **全 PARALLEL_SESSION_NN_DONE** 后启动.
> 你的职责: 串行合并 3 个独立 batch 工作到 root + audit_matrix + _progress.json + 写 round-4 retro + 决定是否 cut formal v1.3 prompt (round 4 evidence saturation 应 unblock cut OR 显式 defer 第 4 次给 dedicated session — 强烈建议本次 cut, 已 deferred 3 rounds running, 累 inline-prepend overhead 显著).

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 + Pre-flight Check
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `multi_session/MULTI_SESSION_PROTOCOL.md` (master protocol)
2. `multi_session/MULTI_SESSION_RETRO.md` (round 1)
3. `multi_session/MULTI_SESSION_RETRO_ROUND_2.md` (round 2)
4. `multi_session/MULTI_SESSION_RETRO_ROUND_3.md` (round 3 — G-MS-11.b NEW6 L4 self-parent extension + G-MS-13 NEW gap finding ID range mis-read + G-MS-14 first Option-E-resistant case)
5. `evidence/checkpoints/_progress_batch_23.json`
6. `evidence/checkpoints/_progress_batch_24.json`
7. `evidence/checkpoints/_progress_batch_25.json`
8. `audit_matrix.md` (current state, ~117 lines post round 3)
9. `_progress.json` (current state, top-level + recovery_hint ~12000 chars post round 3)

### Pre-flight 验:
- 3 sub-progress JSON 都 `status="completed"` ✓
- 6 batch jsonl + 3 batch report + (drift cal batch 24 report)
- Reviewer slot uniqueness: #32 oh-my-claudecode:security-reviewer + #33 oh-my-claudecode:scientist + #34 feature-dev:code-architect (无 cross-batch + 无 cross-round 撞 — 验 _progress_batch_NN.json reviewer_slot 字段 + audit_matrix Rule D Roster #1-#31 累)
- Drift cal: batch 23 + 25 = skipped, batch 24 = triggered NEW1 dual-threshold MANDATORY
- Halt state 检查: 任一 session 写 `halt_state_batch_NN.md` → STEP 0.5 G-MS-4 fallback
- **G-MS-13 finding ID range cross-validation post round 3**: verify batch 23 used O-P1-67..70 + batch 24 used O-P1-71..74 + batch 25 used O-P1-75..78 (3-batch table prevents round 3 batch 21 mis-read recurrence). If any sub-session mis-read range → reconciler renumber per round 3 D-MS-17 precedent.

任一验证失败 → halt + 报告. **不要** 私自 fix sub-session 的输出.

### Step 0.5 — G-MS-4 Halt Fallback Decision Tree (round 2 spec'd, round 4 carry-forward unchanged, live-fire still NOT triggered through round 3)

读 halt_state.md → recommended_fallback 字段 → 决策:
- (a) reconciler retry 全 batch — 主 session 改派 reconciler 自身重跑该 batch 单 session 单 a+b
- (b) reconciler defer 本 batch + merge sister batches only
- (c) reconciler abort experiment — 报告 user, 不动 root, 全 partial work 归档 Rule B

写 `multi_session/halt_resolution_round4.md` 决策记录 (if applicable).

═══════════════════════════════════════════════════════════════════
## STEP 1 — Cross-Batch Sibling Continuity Sweep
═══════════════════════════════════════════════════════════════════

加载 root pdf_atoms.jsonl + 6 batch files + 全部按 (page, atom_index_on_page) 排序.

### 检查项 (round 4 PDF p.4 PRE-VERIFIED 2026-04-26):

**Round 4 batches 23-25 实际 page→section 结构** (per PDF p.4 TOC):
- p.221-227: §6.3.5.4 GF body (continuing from batch 22 p.220)
- p.228: §6.3.5.5 IS NEW sub-domain transition
- p.229-240: §6.3.5.5 IS body (head + body across batches 23+24)
- p.241: §6.3.5.6 LB NEW sub-domain transition
- p.242-247: §6.3.5.6 LB body (LB largest finding domain)
- p.248: §6.3.5.7 Microbiology Domains group NEW L4 group container transition
- p.249-250: §6.3.5.7 Microbiology body (potentially with internal sub-domains §6.3.5.7.1 MB / §6.3.5.7.2 MS or generic spec — TBD by sub-session D)

**§6.3.5.X deep-nesting Level Model carry-forward from round 3**:
- §6.3.5 group = L3 sib=5 under §6.3
- §6.3.5.X individual domains = L4 sib=1..N under §6.3.5
- §6.3.5.X own L5 chain Description=1 / Spec=2 / Assump=3 / Examples=4 ± References=5
- §6.3.5.X.Examples N = L6 sib=N RESTART under §6.3.5.X
- Example Na/Nb sub-examples = L7 sib=1, 2 RESTART under Example N (round 3 NEW7 L7 precedent batch 21)

**§6.3.5.7 Microbiology Domains group container (round 4 NEW for batch 25 — analogous to §6.3.5 itself)**:
- §6.3.5.7 = L4 sib=7 under §6.3.5 (group container per "Domains" plural)
- IF internal sub-domains visible in p.248-250 (e.g. §6.3.5.7.1 MB / §6.3.5.7.2 MS): they are L5 sib=1, 2 RESTART under §6.3.5.7 — own L5 chain at L6 level
- IF generic spec (no nested sub-domains): L5 chain Description=1 directly under §6.3.5.7

### 检查项:

1. **§6.3.x sub-domain L3 sib chain under §6.3 chapter** contiguous: batch 18 §6.3.1 DA=1 / batch 19 §6.3.2 DD=2 / §6.3.3 EG=3 / batch 20 §6.3.4 IE=4 / batch 20 §6.3.5 group=5. (No new §6.3.x sub-domain in round 4; all batch 23-25 work inside §6.3.5 group.)

2. **§6.3.5.X L4 sib chain under §6.3.5 group** contiguous: batch 20 §6.3.5.1=1 / §6.3.5.2 BS=2 / §6.3.5.3 CP=3 + batch 22 §6.3.5.4 GF=4 + batch 23 §6.3.5.5 IS=5 + batch 25 §6.3.5.6 LB=6 + batch 25 §6.3.5.7 Microbiology Domains=7. 验 chain 续号 ✓.

3. **L5 sub-section deterministic chain per NEW7** at deep-nesting (round 3 NEW): 各 §6.3.5.X domain L5 chain Description=1/Spec=2/Assump=3/Examples=4 ± References=5 — 验 §6.3.5.4 GF (batch 22+23) / §6.3.5.5 IS (batch 23+24) / §6.3.5.6 LB (batch 25) / §6.3.5.7 Microbiology (batch 25 if generic spec OR L6 chain if group container) 各 own L5 chain ✓.

4. **L6 Examples N chain restart per §6.3.5.X domain** (independent across domains, 续号 within domain across batches): 验 GF-Examples L6 sib chain (if any in batch 23) + IS-Examples L6 sib chain (if any in batch 24) + LB-Examples L6 sib chain (if any in batch 25).

5. **NEW6 parent_section dual-form sweep** (round 2 G-MS-11 + round 3 G-MS-11.b extension):
   - Chapter-level (§6 / §6.2 / §6.3): `§N.N [TITLE-ALL-CAPS]` short-bracket all-caps (no chapter transitions in round 4 batches; all sub-domain only)
   - L3 sub-domain group (§6.3.5): `§6.3.5 Specimen-based Findings Domains` canonical full-form (no CODE)
   - L4 §6.3.5.X individual domain: `§6.3.5.X Title (CODE)` canonical full-form (e.g., `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`, `§6.3.5.6 Laboratory Test Results (LB)`)
   - L4 §6.3.5.7 group container: `§6.3.5.7 Microbiology Domains` canonical full-form (no CODE since plural group container)
   - L5+ atom parent: same canonical full-form as L4 domain
   - **NEW6.b round 3 extension CRITICAL**: L4 sub-domain section-start HEADING parent = L3 group container `§6.3.5 Specimen-based Findings Domains` (NOT self-parent). Applies to:
     - §6.3.5.5 IS L4 HEADING on p.228 (batch 23)
     - §6.3.5.6 LB L4 HEADING on p.241 (batch 25)
     - §6.3.5.7 Microbiology Domains L4 HEADING on p.248 (batch 25)
   - Inline Option H fix any deviation. **Round 4 high-risk batch 25** (DOUBLE L4 transitions = 2× violation risk despite explicit kickoff spec; round 3 batch 22 saw 1 violation despite spec).

6. **R15 cross-batch boundary check** — 4 boundaries critical:
   - batch 22→23: §6.3.5.4 GF L5 sub-section sib continuation (Description=1 batch 22 → Specification=2 batch 23) + §6.3.5.5 IS L4 sib=5 NEW
   - batch 23→24: §6.3.5.5 IS L5 sub-section sib continuation (Specification=2 batch 23 head → batch 24 body / Assumptions=3 / Examples=4)
   - batch 24→25: §6.3.5.5 IS body terminal → §6.3.5.6 LB L4 sib=6 NEW (no sib chain crossing — domain change)
   - batch 25 内: LB→Microbiology L4 sub-domain transition at p.248 (R12 sub-domain-level discipline DOUBLE)
   per round 2 5-atom batch 18 NEW6 lesson + round 3 batch 22 GF L4 self-parent lesson — sub-sessions blind to sister state, reconciler 是 safety net.

7. **R12 transition page sweep** — 验 p.228 GF→IS / p.241 IS→LB / p.248 LB→Microbiology Domains 各 transition page 3-zone partition + ≥8 atoms 期望.

8. **(注: batch 25 NOT 触 §6.4 chapter** — TOC §6.4 = p.361 远超 batch scope, batch 25 末仅触 §6.3.5.7 Microbiology Domains NEW L4 group container at p.248-250).

### Apply Option H fix for any cross-batch sib gap / NEW6 / NEW6.b / NEW7 violation
任何 violation → inline fix in batch file + accumulate finding O-P1-79+ LOW (类 round 2 O-P1-54 pattern).

写 `multi_session/sibling_continuity_sweep_report_round4.md`.

═══════════════════════════════════════════════════════════════════
## STEP 2 — Sequential Merge to Root
═══════════════════════════════════════════════════════════════════

### Step 2.1: Backup root
```bash
cp pdf_atoms.jsonl pdf_atoms.jsonl.pre-multi-23-25.bak
```

### Step 2.2: Append in batch order
```bash
cat evidence/checkpoints/pdf_atoms_batch_23a.jsonl evidence/checkpoints/pdf_atoms_batch_23b.jsonl evidence/checkpoints/pdf_atoms_batch_24a.jsonl evidence/checkpoints/pdf_atoms_batch_24b.jsonl evidence/checkpoints/pdf_atoms_batch_25a.jsonl evidence/checkpoints/pdf_atoms_batch_25b.jsonl >> pdf_atoms.jsonl
```

### Step 2.3: Final integrity sweep
- `wc -l pdf_atoms.jsonl` 期望 = 5502 + sum(3 batch atoms)
- python3 验: 0 schema error + 0 atom_id collision + pages 1-250 全 250 unique + atom_type distribution sanity

═══════════════════════════════════════════════════════════════════
## STEP 3 — Audit_Matrix Update
═══════════════════════════════════════════════════════════════════

Append 到 `audit_matrix.md`:

### Step 3.1: P1 Batch Roster table 加 3 行 (batches 23/24/25)
### Step 3.2: P1 Drift 校准 table 加 1 行 (batch 24 NEW1 dual-threshold result)
### Step 3.3: P1 Rule A 独审 table 加 3 行 (batches 23/24/25)
### Step 3.4: Rule D Roster 累计 update
- 31 → 34 (3 new slots: #32 oh-my-claudecode:security-reviewer + #33 oh-my-claudecode:scientist + #34 feature-dev:code-architect)
- Reviewer quality 观察 段加 3 个 slot 评价
- 结论段 update: n=170 cumulative anchored audit (n=140 prior + 30 new), 17 consecutive batches, 4 families validated (pr/omc/vercel-pool-exhausted/plugin-dev-pool-exhausted/feature-dev-pool-exhausted post round 4 batch 25 if #34 feature-dev:code-architect is feature-dev's 3rd burn → completes feature-dev family = 3rd family pool exhausted)
- 15 AUDIT-mode pivots cumulative (#20-#34)

═══════════════════════════════════════════════════════════════════
## STEP 4 — _progress.json Update
═══════════════════════════════════════════════════════════════════

Update headline:
- pages_done: 220 → **250**
- atoms_done: 5502 → final (5502 + 3 batch contributions)
- batches_done: 22 → **25**
- failures_done: 1 → 1 + sum(3 batch failures, expect 0)
- last_updated: 2026-04-26 (or current)
- status: "P1_batch_23_24_25_DONE_via_multi_session_parallel_round_4..."

Rewrite recovery_hint with 3-batch summary + cross-batch lessons + Round 4 vs round 1+2+3 comparison + next batch 26 kickoff prep + Rule D 烧 34 (4 families pools status: vercel + plugin-dev + feature-dev EXHAUSTED post round 4; omc burned 7×; remaining = data/firecrawl/superpowers/omc-family-remaining for round 5+).

═══════════════════════════════════════════════════════════════════
## STEP 5 — v1.3 Prompt Formal Cut Decision (FINAL CALL — 4th opportunity post round 1+2+3 RECOMMENDED-DOUBLE-RECOMMENDED)
═══════════════════════════════════════════════════════════════════

Round 1+2+3 reconcilers all RECOMMENDED v1.3 cut + DEFERRED execution per Rule D writer/reviewer isolation. Round 4 reconciler **4th opportunity**:

### Decision matrix:
- 若 v1.3 cut **STILL DEFERRED 4th time** (e.g. user 决定 dedicated session 跑) → 不动 prompt files + 文档 RECOMMENDED-TRIPLE 第 4 次 + 推荐 ESCALATED-CRITICAL-ULTRA schedule v1.3 cut session BEFORE batch 27 drift cal next mandatory + carry-forward overhead (累 13+ batches inline-prepend overhead = ~65-130 min growing 重复劳动)
- 若 v1.3 cut **EXECUTED** (e.g. dedicated session 已跑 OR user 显式授权) → archive v1.2 + activate v1.3 + update batch 26+ kickoff prompts to use v1.3

### v1.3 cut 执行 (若决定 cut):
- 写 `subagent_prompts/P0_writer_pdf_v1.3.md` (full clean rule set: R1-R15 + O-P1-26 codified + NEW1-NEW8 incorporated + NEW6 dual-form codified per round 2 G-MS-11 + NEW6.b L4 sub-domain section-start HEADING parent extension per round 3 G-MS-11.b + density alarm threshold spec per round 2 G-MS-12 + NEW7 L7 sub-example codification per round 3 + NEW8 substring n-gram cross-check per round 3 + G-MS-13 finding ID range cross-validation kickoff prepend codification per round 3)
- Archive v1.2 → `subagent_prompts/archive/v1.2_final_2026-04-26/`
- Update batch 26+ kickoff prompt to use v1.3
- 同时 cut companion: `P0_writer_md_v1.3.md` + `P0_matcher_v1.3.md` + `P0_reviewer_v1.3.md` (if scope evolved)

═══════════════════════════════════════════════════════════════════
## STEP 6 — Session-End Retro (Rule C 强制, Round 4)
═══════════════════════════════════════════════════════════════════

写 `multi_session/MULTI_SESSION_RETRO_ROUND_4.md` (Rule C 三段式, separate from round 1/2/3 retros):

### §1 保留下来的做法 (round 4 reaffirmed/extended)
- Multi-session parallel 四轮验 (round 1 ~50% + round 2 ~52% + round 3 ~50% + round 4 ?% wall savings)
- Rule D pool partition cross-round 验 (#32-#34 vs round 1 #22-#24 + batch 16 #25 + round 2 #26-#28 + round 3 #29-#31 = 0 cross-round collision, 4 rounds running)
- TOC anchor + R-rules unified shared 四轮验 (n=170 cumulative anchored audit 0 FP / 0 inversion target)
- NEW6 dual-form codification (G-MS-11 round 2 修补) 实测 round 4 + NEW6.b L4 self-parent extension (G-MS-11.b round 3 修补) 实测 round 4 (是否 0 violation across 3 L4 transitions IS/LB/Microbiology — 若 0 → ✅ 修补 effective)
- Density alarm threshold (G-MS-12 round 2 修补) 实测 round 4
- NEW1 dual-threshold drift cal 第 3 次实测 (batch 24 — 验是否再次 STRONGLY VALIDATED as designed)
- NEW8 substring n-gram cross-check (round 3 NEW v1.3 candidate) 实测 round 4 (是否在 GF/IS/LB writer-family work 中 catch any adjacent-letter swap)
- AUDIT-mode pivot 跨 4-family 多 burn depth (post round 4: pr×1 / omc×7 / vercel-exhausted / plugin-dev-exhausted / feature-dev-exhausted-3rd if #34 feature-dev:code-architect = feature-dev pool COMPLETED)
- G-MS-7 finding ID range pre-allocation 第 4 次验 + G-MS-13 round 3 NEW fix kickoff cross-validation table at top of each kickoff (是否 0 cross-session mis-read like round 3 batch 21)
- G-MS-4 halt fallback decision tree spec round 4 实测 (若任一 session halt OR 仍未触发 spec-only 4 rounds running → spec-only validation accepted)

### §2 必须补上的缺口 (round 4 surfaces)
- 各 session blindness recur (round 1+2+3 不变)
- Drift cal cumulative cadence cross-batch state (round 1+2+3 不变)
- 任何 sub-session halt → reconciler decision tree (G-MS-4 spec'd 4 rounds running, live-fire still NOT triggered — accept spec-only OR design live-fire scenario)
- 如 round 4 surfaces 新 NEW6.b L4 violation pattern despite kickoff spec → escalate to v1.4
- 如 round 4 surfaces v1.3 cut 仍 deferred 第 4 次 → escalate to user as ULTRA-CRITICAL
- 如 round 4 surfaces 新 G-MS-14 Option-E-resistant case (batch 25 LB largest domain 7th writer-family wide-table corruption candidate) → v1.4 candidate column-aware cell parsing reaffirm

### §3 关键决策
- Round 4 multi-session 节省 vs round 1+2+3 比较
- 是否继续 multi-session round 5 (batches 26-28) — 取决 v1.3 cut 状态 + round 4 verdict
- v1.3 formal cut 是否 unblock 后续 (e.g. R-rules locked → 各 session prompt 更稳定 → 协调成本降)
- Multi-session 是否升 Tier 3 default pattern (4 rounds saturation 后)
- Round 4 batch 25 §6.3.5.7 Microbiology Domains group container 结构验 (round 4 NEW group-of-group L4 vs L5 nesting precedent — extends round 3 NEW7 L7 sub-example precedent)

═══════════════════════════════════════════════════════════════════
## STEP 7 — Optional Cleanup
═══════════════════════════════════════════════════════════════════

可选 (不强制):
- 删除 round 4 one-shot kickoff (`batch_23_kickoff.md` + `batch_24_kickoff.md` + `batch_25_kickoff.md` + `reconciler_kickoff_round4.md`)
- 留 MULTI_SESSION_PROTOCOL.md + 4 retro files + 4 sibling sweep reports = 9 files 作历史
- 提示 user 移除 CLAUDE.md round 4 routing rule (本次实验后 OR 切换到 round 5 routing if applicable)

═══════════════════════════════════════════════════════════════════
## STEP 8 — Final Message + User Report
═══════════════════════════════════════════════════════════════════

Echo 单行:
```
RECONCILER_DONE_ROUND_4 root_atoms=<N> pages_done=250 batches_done=25 sibling_fixes=<N> v1.3_cut=<yes|no|deferred_4th> retro_written=true
```

User-facing summary 含 round 4 contributions + cross-batch fixes + drift cal NEW1 dual-threshold round 3 verdict + reviewer quality 3 slots + multi-session round 4 vs round 1+2+3 比较 + v1.3 cut decision rationale + next batch 26 kickoff prep + cleanup recommendation.

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- 修改 sub-session 输出 (`pdf_atoms_batch_NN[ab].jsonl`) 除 STEP 1 sibling/NEW6/NEW6.b/NEW7 inline fix
- 跑额外 PDF atomization / Rule A reviewer / drift cal (除非主 session 检漏跑 — halt + 报告)
- Touch CLAUDE.md / MEMORY / project meta files (除 STEP 7 cleanup 提示)
- Run git commit / push (留 user 决定)

The boulder never stops. 第一步 STEP 0 并行 9-file Read + Pre-flight check.
