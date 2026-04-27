# Reconciler Kickoff (Multi-Session Parallel — Session E, Round 6 batches 29/30/31)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 8 STEPs (sibling sweep + sequential merge + audit_matrix update + _progress.json update + v1.4 cut decision + retro + cleanup + final message) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一合法收尾信号 = STEP 8 echo `RECONCILER_DONE_ROUND_6 root_atoms=<N> pages_done=310 batches_done=31 sibling_fixes=<N> v1.4_cut=<yes|no|deferred> retro_written=true` 单行 + user-facing summary.
>
> Halt-only fallback per G-MS-4 round 2 spec: 若任一 sister session 写了 `halt_state_batch_NN.md` → STEP 0.5 decision tree (carry-forward 6 rounds spec-only).
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel round 6 的 **reconciler (session E)**.
> 仅在 session B (batch 29) + session C (batch 30) + session D (batch 31) **全 PARALLEL_SESSION_NN_DONE** 后启动.
> 职责: 串行合并 3 个独立 batch 工作到 root + audit_matrix + _progress.json + 写 round-6 retro + 决定是否 cut formal v1.4 prompt.

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 + Pre-flight Check
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `multi_session/MULTI_SESSION_PROTOCOL.md` (master)
2. `multi_session/MULTI_SESSION_RETRO.md` (round 1)
3. `multi_session/MULTI_SESSION_RETRO_ROUND_2.md` (round 2)
4. `multi_session/MULTI_SESSION_RETRO_ROUND_3.md` (round 3)
5. `multi_session/MULTI_SESSION_RETRO_ROUND_4.md` (round 4)
6. `multi_session/MULTI_SESSION_RETRO_ROUND_5.md` (round 5 — 最近一轮 R-MS retain + G-MS gap + D-MS decision + family pool state + general-purpose AUDIT pivot 验证 + NEW1 5th time + NEW7 L6 procedural enforcement verdict)
7. `evidence/checkpoints/_progress_batch_29.json`
8. `evidence/checkpoints/_progress_batch_30.json`
9. `evidence/checkpoints/_progress_batch_31.json`
10. `audit_matrix.md` (current state, post round 5)
11. `_progress.json` (current state, top-level + recovery_hint post round 5)

### Pre-flight 验:
- 3 sub-progress JSON 都 `status="completed"` ✓
- 6 batch jsonl + 3 batch report + (drift cal batch 30 report)
- Reviewer slot uniqueness #38-#40: **<round 6 实际选定 family>** 验 0 cross-batch + 0 cross-round 撞 (round 1 #22-#24 + batch 16 #25 + round 2 #26-#28 + round 3 #29-#31 + round 4 #32-#34 + round 5 #35-#37)
- Drift cal: batch 29 + 31 = skipped, batch 30 = triggered NEW1 dual-threshold MANDATORY 6th time
- Halt state 检查: 任一 session 写 `halt_state_batch_NN.md` → STEP 0.5 G-MS-4 fallback
- **G-MS-13 finding ID range cross-validation** (round 4+5 EFFECTIVE codified pattern, 6 sister sessions cumulative): verify batch 29 used reserved range + batch 30 used reserved range + batch 31 used reserved range. 若 sub-session mis-read range → reconciler renumber per round 3 D-MS-17 + round 4-5 precedent.

任一验证失败 → halt + 报告. **不要** 私自 fix sub-session 的输出.

### Step 0.5 — G-MS-4 Halt Fallback Decision Tree (6 rounds spec-only carry-forward if round 5 also spec-only)

读 halt_state.md → recommended_fallback 字段 → 决策:
- (a) reconciler retry 全 batch — 主 session 改派 reconciler 自身重跑该 batch 单 session 单 a+b
- (b) reconciler defer 本 batch + merge sister batches only
- (c) reconciler abort experiment — 报告 user, 不动 root

写 `multi_session/halt_resolution_round6.md` 决策记录 (if applicable).

**Round 6 retro 决议** (per round 5 §2 G-MS-4 carry-forward): 6 rounds spec-only no live-fire = 接受 spec-only validation OR 设计 adversarial halt scenario for round 7+.

═══════════════════════════════════════════════════════════════════
## STEP 1 — Cross-Batch Sibling Continuity Sweep
═══════════════════════════════════════════════════════════════════

加载 root pdf_atoms.jsonl + 6 batch files + 全部按 (page, atom_index_on_page) 排序.

### 检查项 (round 6 PDF p.4 PRE-VERIFIED by 主 session pre-dispatch):

**Round 6 batches 29-31 实际 page→section 结构** (per PDF p.4 TOC; 主 session pre-dispatch verify):
- p.281-310: 续 round 5 batch 28 终态 §6.3.5.X+ body + 任何 §6.3.5.X+ NEW sub-domain transitions + 可能 §6.3.6+ / §6.4+ class transition if §6.3.5 完结于 round 5/早 round 6
- 实际 sub-domain 节号 / transition 数 = round 5 retro carry-forward + round 6 主 session pre-dispatch verify

### §6.3.5 Level Model carry-forward from round 1-5:
- §6.3.5 group = L3 sib=5 under §6.3
- §6.3.5.X individual domain = L4 sib=1..N under §6.3.5
- §6.3.5.X own L5 chain Description=1 / Spec=2 / Assump=3 / Examples=4 ± References=5
- §6.3.5.X.Examples N = L6 sib=N RESTART under §6.3.5.X
- Example Na/Nb sub-examples = L7 sib=1, 2 RESTART under Example N (round 3 NEW7 L7 precedent)
- §6.3.5.X group container (e.g. §6.3.5.7) internal §N.N.N.N sub-domain = L5 sib=1..N RESTART under group container; own L6 chain (round 4 NEW O-P1-75)
- 任何 §6.3.6+ / §6.4+ NEW class L3 transition (round 6 first if §6.3.5 完结) — parent = §6 chapter L2 (R12 chapter-level discipline)

### 检查项:

1. **§6.3.5 L4 sib chain contiguous across rounds**: GF=4 (b22) / IS=5 (b23) / LB=6 (b25) / Microbiology Domains=7 (b25) / MI=8 (b27 round 5) / **<round 5 retro 回填实际 §6.3.5.9+ L4 sib state>** / round 6 任何 NEW L4. 验 chain 续号 ✓.

2. **L5 sub-section deterministic chain per NEW7** at deep-nesting: 验各 §6.3.5.X domain L5 chain Description=1/Spec=2/Assump=3/Examples=4 ± Refs=5.

3. **L6 Examples N chain restart per §6.3.5.X domain**: 验各 sub-domain L6 sib chain.

4. **🔴 NEW7 L6 sub-batch handoff effectiveness check (round 6 procedural enforcement validation)**:
   - 任何 SENTENCE 'Example N' under §6.3.5.X domain → must be HEADING hl=6 sib=K RESTART (round 3+4+5 = 3× CROSS-batch RECURRENCE pattern, last incidence round 5 reconciler-side O-P1-92 Option H 4-atom fix; round 5 INTRA-batch procedural prepend EFFECTIVE 1st live-fire 0 recurrence per O-P1-81; CROSS-batch handoff codification round 6 mandatory)
   - 任何 LB-Examples-style L5 'Examples' header at hl=6 sib=K (instead of hl=5 sib=4) → Option H 修
   - **若 round 6 仍出现 NEW7 L6 sub-batch context drift after round 5 procedural enforcement** → escalate v1.4 + emergency cut required

5. **NEW6 parent_section dual-form sweep** (round 4-5 G-MS-11.b proactive EFFECTIVE 4-5×):
   - L4 §6.3.5.X individual domain HEADING parent = L3 group container `§6.3.5 Specimen-based Findings Domains` (NEVER self-parent)
   - 应用 to: 任何 round 6 §6.3.5.X+ / §6.3.6+ NEW L4 transition
   - **Round 6 high-watch**: 若 round 5 NEW6.b proactive 5× streak holds, expect 0 violation; 若 round 5 break streak → procedural rebuild

6. **R15 cross-batch boundary check** — 4 boundaries critical:
   - batch 28 → 29: round 5 batch 28 终态 (round 5 retro 回填) → batch 29 contiguous
   - batch 29 → 30: chain continuation OR domain change
   - batch 30 → 31: chain continuation OR transition
   - batch 31 内: 任何 chapter/class transition (R12 discipline)

7. **R12 transition page sweep**: 验各 batch NEW L4/class transition 3-zone partition + ≥8 atoms.

### Apply Option H fix for any cross-batch sib gap / NEW6 / NEW6.b / NEW7 violation
任何 violation → inline fix in batch file + accumulate finding O-P1-105+ LOW (类 round 4 O-P1-79 + round 5 O-P1-92 reconciler-side pattern; if 4th cross-batch recurrence post round 6 cross-batch handoff codification → ESCALATE v1.4 EMERGENCY-CRITICAL).

写 `multi_session/sibling_continuity_sweep_report_round6.md`.

═══════════════════════════════════════════════════════════════════
## STEP 2 — Sequential Merge to Root
═══════════════════════════════════════════════════════════════════

### Step 2.1: Backup root
```bash
cp pdf_atoms.jsonl pdf_atoms.jsonl.pre-multi-29-31.bak
```

### Step 2.2: Append in batch order
```bash
cat evidence/checkpoints/pdf_atoms_batch_29a.jsonl evidence/checkpoints/pdf_atoms_batch_29b.jsonl evidence/checkpoints/pdf_atoms_batch_30a.jsonl evidence/checkpoints/pdf_atoms_batch_30b.jsonl evidence/checkpoints/pdf_atoms_batch_31a.jsonl evidence/checkpoints/pdf_atoms_batch_31b.jsonl >> pdf_atoms.jsonl
```

### Step 2.3: Final integrity sweep
- `wc -l pdf_atoms.jsonl` 期望 = round 5 baseline + sum(3 batch atoms)
- python3 验: 0 schema error + 0 atom_id collision + pages 1-310 全 310 unique + atom_type distribution sanity

═══════════════════════════════════════════════════════════════════
## STEP 3 — Audit_Matrix Update
═══════════════════════════════════════════════════════════════════

Append 到 `audit_matrix.md`:

### Step 3.1: P1 Batch Roster table 加 3 行 (batches 29/30/31)
### Step 3.2: P1 Drift 校准 table 加 1 行 (batch 30 NEW1 dual-threshold result 6th time)
### Step 3.3: P1 Rule A 独审 table 加 3 行 (batches 29/30/31)
### Step 3.4: Rule D Roster 累计 update
- 37 → 40 (3 new slots: #38 + #39 + #40 — round 6 实际 family/agent 选)
- Reviewer quality 观察 段加 3 个 slot 评价
- 结论段 update: n=230 cumulative anchored audit (n=200 prior + 30 new), 23 consecutive batches, family validation extended (post round 6: 6+ families validated + family-agnostic recipe 5+ rounds 验证)
- 21 AUDIT-mode pivots cumulative (#20-#40)

═══════════════════════════════════════════════════════════════════
## STEP 4 — _progress.json Update
═══════════════════════════════════════════════════════════════════

Update headline:
- pages_done: round 5 baseline → **310**
- atoms_done: round 5 baseline → final (round 5 baseline + 3 batch contributions)
- batches_done: 28 → **31**
- failures_done: round 5 baseline + sum(3 batch failures, expect 0)
- last_updated: <date>
- status: "P1_batch_29_30_31_DONE_via_multi_session_parallel_round_6..."

Rewrite recovery_hint with 3-batch summary + cross-batch lessons + Round 6 vs round 1+2+3+4+5 comparison + next batch 32 kickoff prep + Rule D 烧 40 (post round 6 family state: pr-review-toolkit family burned 2× via #38 code-reviewer + #40 silent-failure-hunter; superpowers family first burn via #39 code-reviewer; cumulative families post round 6 = pr/omc-burned-deep/vercel-EXHAUSTED/plugin-dev-EXHAUSTED/feature-dev-EXHAUSTED/general-purpose-r5/superpowers-r6/pr-r6 = 8 families; remaining unburned = claude-code-guide + codex + Plan + Explore + statusline-setup + plugin-dev:plugin-validator residual + omc-family unburned variants for round 7+).

═══════════════════════════════════════════════════════════════════
## STEP 5 — v1.4 Prompt Cut Decision (round 6 first opportunity)
═══════════════════════════════════════════════════════════════════

**Round 5 已 cut v1.3** (2026-04-27 dedicated session 完成). Round 6 reconciler 评估是否 cut v1.4:

### Decision matrix:
- 若 round 5+6 surfaces 累计 v1.4 candidate ≥3 (e.g. NEW8.b SENTENCE-trigram + NEW8.c TABLE_HEADER column-set + content-type-aware density floor + writer-family bulk reconciler-deferred sweep + drift cal cumulative state structured field + canonical CDISC variable list shipped) → RECOMMEND v1.4 cut next dedicated session
- 若 round 5+6 surfaces NEW7 L6 RECURRENCE 3rd time despite procedural enforcement → EMERGENCY-CRITICAL v1.4 cut required (procedural prepend → spec-level enforcement)
- 若 round 5+6 surfaces 0 net new G-MS gaps → DEFER v1.4 cut, accept v1.3 saturation

### v1.4 cut 执行 (若决定 cut, dedicated session per Rule D writer/reviewer isolation):
- 写 `subagent_prompts/P0_writer_pdf_v1.4.md` 完整 (v1.3 base + 任何 round 5+6 累 v1.4 candidates)
- Archive v1.3 → `subagent_prompts/archive/v1.3_final_<date>/`
- Update batch 32+ kickoff prompt to use v1.4
- 同时 cut companion: `P0_writer_md_v1.4.md` + `P0_matcher_v1.4.md` + `P0_reviewer_v1.4.md`

═══════════════════════════════════════════════════════════════════
## STEP 6 — Session-End Retro (Rule C 强制, Round 6)
═══════════════════════════════════════════════════════════════════

写 `multi_session/MULTI_SESSION_RETRO_ROUND_6.md` (Rule C 三段式):

### §1 保留下来的做法 (round 6 reaffirmed/extended)
- Multi-session parallel 6 rounds (round 1 ~50% + round 2 ~52% + round 3 ~50% + round 4 ~50% + round 5 ?% + round 6 ?% wall savings — round 6 实际)
- Rule D pool partition cross-round 验 (#38-#40 vs prior #1-#37 = 0 cross-round collision target, 6 rounds running)
- TOC anchor + R-rules unified shared 6 rounds (n=230 cumulative anchored audit 0 FP / 0 inversion target)
- NEW6/NEW6.b dual-form codification round 6 实测
- 🔴 **NEW7 L6 procedural sub-batch handoff round 6 实测 (round 3+4 RECURRENCE 已停 by round 5 procedural prepend? 还是 3rd recurrence?)**
- NEW1 dual-threshold drift cal 第 6 次实测 (batch 30)
- AUDIT-mode pivot 跨 N-family multi-burn depth (post round 6 family pool state)
- G-MS-7 finding ID range pre-allocation 第 6 次验 + G-MS-13 cross-validation table 第 3 次验
- v1.3 prompts inline-prepend retire (round 5 起) effectiveness round 6 验证

### §2 必须补上的缺口 (round 6 surfaces)
- 各 session blindness recur (6 rounds 不变)
- 任何 sub-session halt → reconciler decision tree (G-MS-4 6 rounds spec-only — accept OR design live-fire round 7)
- 如 round 6 surfaces NEW7 L6 RECURRENCE 3rd time despite round 5 procedural prepend → EMERGENCY-CRITICAL v1.4 cut
- 如 round 6 surfaces v1.4 cut RECOMMENDED 1st time → schedule dedicated session
- 如 round 6 family-agnostic AUDIT pivot 失败 (新 family adaptation issue) → 探更广 family adaptation pattern
- 如 round 6 NEW1 first FAIL → drift cal spec rethink

### §3 关键决策
- Round 6 multi-session 节省 vs round 1+2+3+4+5 比较
- 是否继续 multi-session round 7 (batches 32-34) — 取决 v1.4 cut 状态 + round 6 verdict
- v1.4 formal cut 是否 unblock 后续 efficiency
- Multi-session 是否升 Tier 3 default pattern (6 rounds saturation)
- Family-agnostic AUDIT pivot recipe 是否扩展到更多 cross-family pivots round 7+
- §6.3.5 完结后 (round 5 / round 6 mid?) 是否扩 scope 到 §6.3.6+ / §6.4+ / §7+ chapters

═══════════════════════════════════════════════════════════════════
## STEP 7 — Optional Cleanup
═══════════════════════════════════════════════════════════════════

可选 (不强制):
- 删除 round 6 one-shot kickoff (`batch_29_kickoff.md` + `batch_30_kickoff.md` + `batch_31_kickoff.md` + `reconciler_kickoff_round6.md`)
- 留 MULTI_SESSION_PROTOCOL.md + 6 retro files + 6 sibling sweep reports = 13 files 作历史
- 提示 user 移除 CLAUDE.md round 6 routing rule (本次实验后 OR 切换到 round 7 routing if applicable)
- 提示 user N cumulative reconciler-deferred manual repair items 待清 (O-P1-65/66/67/74/79 + 任何 round 5+6 累)

═══════════════════════════════════════════════════════════════════
## STEP 8 — Final Message + User Report
═══════════════════════════════════════════════════════════════════

Echo 单行:
```
RECONCILER_DONE_ROUND_6 root_atoms=<N> pages_done=310 batches_done=31 sibling_fixes=<N> v1.4_cut=<yes|no|deferred> retro_written=true
```

User-facing summary 含 round 6 contributions + cross-batch fixes + drift cal NEW1 6th time verdict + reviewer quality 3 slots (含 family-agnostic recipe round 6 验证) + multi-session round 6 vs round 1+2+3+4+5 比较 + v1.4 cut decision rationale + next batch 32 kickoff prep + cleanup recommendation.

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- 修改 sub-session 输出 (`pdf_atoms_batch_NN[ab].jsonl`) 除 STEP 1 sibling/NEW6/NEW6.b/NEW7 inline fix
- 跑额外 PDF atomization / Rule A reviewer / drift cal (除非主 session 检漏跑 — halt + 报告)
- Touch CLAUDE.md / MEMORY / project meta files (除 STEP 7 cleanup 提示)
- Run git commit / push (留 user 决定)

The boulder never stops. 第一步 STEP 0 并行 11-file Read + Pre-flight check.
