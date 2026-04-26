# Reconciler Kickoff (Multi-Session Parallel — Session E, Round 5 batches 26/27/28)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 8 STEPs (sibling sweep + sequential merge + audit_matrix update + _progress.json update + v1.3 cut decision + retro + cleanup + final message) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一合法收尾信号 = STEP 8 echo `RECONCILER_DONE_ROUND_5 root_atoms=<N> pages_done=280 batches_done=28 sibling_fixes=<N> v1.3_cut=<yes|no|deferred_5th> retro_written=true` 单行 + user-facing summary.
>
> Halt-only fallback per G-MS-4 round 2 spec: 若任一 sister session 写了 `halt_state_batch_NN.md` → STEP 0.5 decision tree (carry-forward 5 rounds spec-only).
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel round 5 的 **reconciler (session E)**.
> 仅在 session B (batch 26) + session C (batch 27) + session D (batch 28) **全 PARALLEL_SESSION_NN_DONE** 后启动.
> 职责: 串行合并 3 个独立 batch 工作到 root + audit_matrix + _progress.json + 写 round-5 retro + 决定是否 cut formal v1.3 prompt.

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 + Pre-flight Check
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `multi_session/MULTI_SESSION_PROTOCOL.md` (master)
2. `multi_session/MULTI_SESSION_RETRO.md` (round 1)
3. `multi_session/MULTI_SESSION_RETRO_ROUND_2.md` (round 2)
4. `multi_session/MULTI_SESSION_RETRO_ROUND_3.md` (round 3)
5. `multi_session/MULTI_SESSION_RETRO_ROUND_4.md` (round 4 — 12 R-MS / 6 G-MS / 7 D-MS + NEW7 L6 RECURRENCE finding + 3 family pools EXHAUSTED + v1.3 ULTRA-CRITICAL escalation)
6. `evidence/checkpoints/_progress_batch_26.json`
7. `evidence/checkpoints/_progress_batch_27.json`
8. `evidence/checkpoints/_progress_batch_28.json`
9. `audit_matrix.md` (current state, ~129 lines post round 4)
10. `_progress.json` (current state, top-level + recovery_hint post round 4)

### Pre-flight 验:
- 3 sub-progress JSON 都 `status="completed"` ✓
- 6 batch jsonl + 3 batch report + (drift cal batch 27 report)
- Reviewer slot uniqueness #35-#37: omc:analyst (#35) + omc:architect (#36) + general-purpose (#37); 验 0 cross-batch + 0 cross-round 撞 (round 1 #22-#24 + batch 16 #25 + round 2 #26-#28 + round 3 #29-#31 + round 4 #32-#34)
- Drift cal: batch 26 + 28 = skipped, batch 27 = triggered NEW1 dual-threshold MANDATORY 5th time
- Halt state 检查: 任一 session 写 `halt_state_batch_NN.md` → STEP 0.5 G-MS-4 fallback
- **G-MS-13 finding ID range cross-validation** (round 4 EFFECTIVE codified pattern): verify batch 26 used O-P1-80..83 + batch 27 used O-P1-84..87 + batch 28 used O-P1-88..91. 若 sub-session mis-read range → reconciler renumber per round 3 D-MS-17 + round 4 D-MS-X precedent.

任一验证失败 → halt + 报告. **不要** 私自 fix sub-session 的输出.

### Step 0.5 — G-MS-4 Halt Fallback Decision Tree (5 rounds spec-only carry-forward)

读 halt_state.md → recommended_fallback 字段 → 决策:
- (a) reconciler retry 全 batch — 主 session 改派 reconciler 自身重跑该 batch 单 session 单 a+b
- (b) reconciler defer 本 batch + merge sister batches only
- (c) reconciler abort experiment — 报告 user, 不动 root

写 `multi_session/halt_resolution_round5.md` 决策记录 (if applicable).

**Round 5 retro 决议** (per round 4 §2 G-MS-4): 5 rounds spec-only no live-fire = 接受 spec-only validation OR 设计 adversarial halt scenario for round 6+.

═══════════════════════════════════════════════════════════════════
## STEP 1 — Cross-Batch Sibling Continuity Sweep
═══════════════════════════════════════════════════════════════════

加载 root pdf_atoms.jsonl + 6 batch files + 全部按 (page, atom_index_on_page) 排序.

### 检查项 (round 5 PDF p.4 PRE-VERIFIED by 主 session pre-dispatch):

**Round 5 batches 26-28 实际 page→section 结构** (per PDF p.4 TOC; 主 session pre-dispatch verify):
- p.251-262: §6.3.5.7 Microbiology Domains group container 续 (likely §6.3.5.7.1 MB body + 可能 §6.3.5.7.2 MS NEW sub-domain RESTART)
- **p.263**: §6.3.5.8 MI Microscopic Findings NEW L4 sub-domain transition (R12 critical)
- p.264-280: §6.3.5.8 MI body + 可能 §6.3.5.9+ NEW sub-domain transition

### §6.3.5 Level Model carry-forward from round 1-4:
- §6.3.5 group = L3 sib=5 under §6.3
- §6.3.5.X individual domain = L4 sib=1..N under §6.3.5
- §6.3.5.X own L5 chain Description=1 / Spec=2 / Assump=3 / Examples=4 ± References=5
- §6.3.5.X.Examples N = L6 sib=N RESTART under §6.3.5.X
- Example Na/Nb sub-examples = L7 sib=1, 2 RESTART under Example N (round 3 NEW7 L7 precedent)
- §6.3.5.X group container (e.g. §6.3.5.7) internal §N.N.N.N sub-domain = L5 sib=1..N RESTART under group container; own L6 chain (round 4 NEW round-4 group-container precedent O-P1-75)

### 检查项:

1. **§6.3.5 L4 sib chain contiguous across rounds**: GF=4 (b22) / IS=5 (b23) / LB=6 (b25) / Microbiology Domains=7 (b25) / **MI=8 (b27)** / **§6.3.5.9+=9+ (b27 or b28 if NEW)**. 验 chain 续号 ✓.

2. **L5 sub-section deterministic chain per NEW7** at deep-nesting: 各 §6.3.5.X domain L5 chain Description=1/Spec=2/Assump=3/Examples=4 ± Refs=5 — 验 §6.3.5.7.1 MB (b25 + b26) / §6.3.5.7.2 MS (b26 if applicable) / §6.3.5.8 MI (b27 + b28) / §6.3.5.9+ (b28 if NEW) own L5 chain ✓.

3. **L6 Examples N chain restart per §6.3.5.X domain**: 验 MB-Examples L6 sib chain (if any in b26) + MI-Examples L6 sib chain (if any in b27/b28) + 任何 §6.3.5.9+ Examples L6 sib chain (if any in b28).

4. **🔴 NEW7 L6 sub-batch handoff effectiveness check (round 5 procedural enforcement validation)**:
   - 任何 SENTENCE 'Example N' under §6.3.5.X domain → must be HEADING hl=6 sib=K RESTART (round 3+4 RECURRENCE pattern; round 5 procedural prepend should prevent — 0 violation expected if prepend EFFECTIVE)
   - 任何 LB-Examples-style L5 'Examples' header at hl=6 sib=K (instead of hl=5 sib=4) → Option H 修
   - **若 round 5 仍出现 NEW7 L6 sub-batch context drift** → escalate v1.4 + adjust v1.3 cut spec to add procedural enforcement explicit bullet

5. **NEW6 parent_section dual-form sweep** (round 4 G-MS-11.b proactive EFFECTIVE 4× across IS/LB/Microbiology Domains/MI):
   - L4 §6.3.5.X individual domain HEADING parent = L3 group container `§6.3.5 Specimen-based Findings Domains` (NEVER self-parent)
   - 应用 to: §6.3.5.7.2 MS (if NEW b26) / §6.3.5.8 MI (b27, p.263) / §6.3.5.9+ (b28 if NEW)
   - **Round 5 high-watch batch 27** (1 R12 transition critical; 4× round 4 EFFECTIVE precedent — expect 0 violation)

6. **R15 cross-batch boundary check** — 4 boundaries critical:
   - batch 25 → 26: §6.3.5.7.1 MB L6 sib=2 (Specification) → batch 26 sib=3 (Assumptions) contiguous OR §6.3.5.7.2 MS L5 sib=2 NEW
   - batch 26 → 27: §6.3.5.7末 → §6.3.5.8 MI L4 sib=8 NEW (no sib chain crossing — domain change)
   - batch 27 → 28: §6.3.5.8 MI L5 chain or L6 Examples chain continuation
   - batch 28 内: 任何 §6.3.5.9+ L4 transition (R12 sub-domain-level discipline)

7. **R12 transition page sweep**: 验 b27 p.263 §6.3.5.7→§6.3.5.8 MI 3-zone partition + ≥8 atoms; b28 任何 §6.3.5.9+ NEW transition.

### Apply Option H fix for any cross-batch sib gap / NEW6 / NEW6.b / NEW7 violation
任何 violation → inline fix in batch file + accumulate finding O-P1-92+ LOW (类 round 4 O-P1-79 reconciler-side pattern).

写 `multi_session/sibling_continuity_sweep_report_round5.md`.

═══════════════════════════════════════════════════════════════════
## STEP 2 — Sequential Merge to Root
═══════════════════════════════════════════════════════════════════

### Step 2.1: Backup root
```bash
cp pdf_atoms.jsonl pdf_atoms.jsonl.pre-multi-26-28.bak
```

### Step 2.2: Append in batch order
```bash
cat evidence/checkpoints/pdf_atoms_batch_26a.jsonl evidence/checkpoints/pdf_atoms_batch_26b.jsonl evidence/checkpoints/pdf_atoms_batch_27a.jsonl evidence/checkpoints/pdf_atoms_batch_27b.jsonl evidence/checkpoints/pdf_atoms_batch_28a.jsonl evidence/checkpoints/pdf_atoms_batch_28b.jsonl >> pdf_atoms.jsonl
```

### Step 2.3: Final integrity sweep
- `wc -l pdf_atoms.jsonl` 期望 = 6146 + sum(3 batch atoms)
- python3 验: 0 schema error + 0 atom_id collision + pages 1-280 全 280 unique + atom_type distribution sanity

═══════════════════════════════════════════════════════════════════
## STEP 3 — Audit_Matrix Update
═══════════════════════════════════════════════════════════════════

Append 到 `audit_matrix.md`:

### Step 3.1: P1 Batch Roster table 加 3 行 (batches 26/27/28)
### Step 3.2: P1 Drift 校准 table 加 1 行 (batch 27 NEW1 dual-threshold result 5th time)
### Step 3.3: P1 Rule A 独审 table 加 3 行 (batches 26/27/28)
### Step 3.4: Rule D Roster 累计 update
- 34 → 37 (3 new slots: #35 omc:analyst + #36 omc:architect + #37 general-purpose)
- Reviewer quality 观察 段加 3 个 slot 评价
- 结论段 update: n=200 cumulative anchored audit (n=170 prior + 30 new), 20 consecutive batches, 5 families validated (pr/omc/vercel-EXHAUSTED/plugin-dev-EXHAUSTED/feature-dev-EXHAUSTED + general-purpose first burn)
- 18 AUDIT-mode pivots cumulative (#20-#37)

═══════════════════════════════════════════════════════════════════
## STEP 4 — _progress.json Update
═══════════════════════════════════════════════════════════════════

Update headline:
- pages_done: 250 → **280**
- atoms_done: 6146 → final (6146 + 3 batch contributions)
- batches_done: 25 → **28**
- failures_done: 1 → 1 + sum(3 batch failures, expect 0)
- last_updated: <date>
- status: "P1_batch_26_27_28_DONE_via_multi_session_parallel_round_5..."

Rewrite recovery_hint with 3-batch summary + cross-batch lessons + Round 5 vs round 1+2+3+4 comparison + next batch 29 kickoff prep + Rule D 烧 37 (5 families: pr/omc/vercel-EXHAUSTED/plugin-dev-EXHAUSTED/feature-dev-EXHAUSTED/general-purpose-first-burn; omc-family burned 9× post round 5 architect; remaining = data/firecrawl/superpowers/general-purpose-extension/omc-family-remaining for round 6+).

═══════════════════════════════════════════════════════════════════
## STEP 5 — v1.3 Prompt Cut Status (ALREADY COMPLETED 2026-04-27)
═══════════════════════════════════════════════════════════════════

**v1.3 cut RESOLVED 2026-04-27** in dedicated cut session — 4 v1.3 prompts written (P0_writer_pdf/P0_writer_md/P0_matcher/P0_reviewer v1.3) + 13 codification items A-M codified inline + Rule D reviewer #35 oh-my-claudecode:critic AUDIT verdict PASS 13/13 + v1.2 archived to `subagent_prompts/archive/v1.2_final_2026-04-27/`. Round 5 batches 26/27/28 already use v1.3 prompts (kickoff §2 cross-references). Round 5 reconciler skips this STEP — v1.3 cut decision is OBSOLETE; this STEP becomes "verify v1.3 prompts continue to deliver effectiveness round 5 (any G-MS-NEW-5-X gaps surfaced) → log to retro for v1.4 candidate planning".

(Historical context retained below for round 1-4 narrative continuity:)

Round 1+2+3+4 reconcilers all RECOMMENDED v1.3 cut + DEFERRED execution per Rule D writer/reviewer isolation. Round 5 reconciler **5th opportunity**:

### Decision matrix:
- 若 v1.3 cut **STILL DEFERRED 5th time** → escalate to **EMERGENCY-CRITICAL** + halt-recommend further multi-session round 6 until v1.3 cut完成 (累 16+ batches inline-prepend overhead = ~80-160 min growing 重复劳动 + 2× NEW7 L6 RECURRENCE = formal codification mandatory now overdue)
- 若 v1.3 cut **EXECUTED** (e.g. dedicated session 已跑 OR user 显式授权) → archive v1.2 + activate v1.3 + update batch 29+ kickoff prompts to use v1.3

### v1.3 cut 执行 (若决定 cut):
- 写 `subagent_prompts/P0_writer_pdf_v1.3.md` 完整 (R1-R15 + O-P1-26 + NEW1-NEW8 + NEW6 dual-form + NEW6.b L4 self-parent + NEW7 L6 procedural sub-batch handoff (round 3+4+5 recurrence formal codification mandatory) + NEW7 L7 sub-example + NEW7 L4 group-container precedent (round 4 NEW O-P1-75) + density alarm threshold spec G-MS-12 + content-type-aware floor v1.4 candidate + G-MS-13 finding ID range cross-validation kickoff prepend + NEW8 substring n-gram + NEW8.b SENTENCE-trigram (round 4 candidate) + NEW8.c TABLE_HEADER column-set (round 4 candidate))
- Archive v1.2 → `subagent_prompts/archive/v1.2_final_<date>/`
- Update batch 29+ kickoff prompt to use v1.3
- 同时 cut companion: `P0_writer_md_v1.3.md` + `P0_matcher_v1.3.md` + `P0_reviewer_v1.3.md`

═══════════════════════════════════════════════════════════════════
## STEP 6 — Session-End Retro (Rule C 强制, Round 5)
═══════════════════════════════════════════════════════════════════

写 `multi_session/MULTI_SESSION_RETRO_ROUND_5.md` (Rule C 三段式):

### §1 保留下来的做法 (round 5 reaffirmed/extended)
- Multi-session parallel 5 rounds (round 1 ~50% + round 2 ~52% + round 3 ~50% + round 4 ~50% + round 5 ?% wall savings)
- Rule D pool partition cross-round 验 (#35-#37 vs prior #1-#34 = 0 cross-round collision, 5 rounds running)
- TOC anchor + R-rules unified shared 5 rounds (n=200 cumulative anchored audit 0 FP / 0 inversion target)
- NEW6/NEW6.b dual-form codification round 5 实测 (是否 0 violation across §6.3.5.7.2 MS / §6.3.5.8 MI / §6.3.5.9+ L4 transitions — 若 0 → ✅ 修补 5× EFFECTIVE)
- 🔴 **NEW7 L6 procedural sub-batch handoff round 5 实测 (round 3+4 RECURRENCE 是否 stopped — 若 0 violation → procedural enforcement EFFECTIVE; 若仍 recurrence → v1.3 cut 必须 emergency)**
- NEW1 dual-threshold drift cal 第 5 次实测 (batch 27)
- NEW8 substring n-gram + NEW8.b/c v1.4 candidates 实测 round 5
- AUDIT-mode pivot 跨 5-family multi-burn depth (post round 5: pr×1 / omc×9 / vercel-EXHAUSTED×3 / plugin-dev-EXHAUSTED×3 / feature-dev-EXHAUSTED×3 / general-purpose first burn ×1)
- G-MS-7 finding ID range pre-allocation 第 5 次验 + G-MS-13 cross-validation table 第 2 次验

### §2 必须补上的缺口 (round 5 surfaces)
- 各 session blindness recur (5 rounds 不变)
- 任何 sub-session halt → reconciler decision tree (G-MS-4 5 rounds spec-only — accept OR design live-fire round 6)
- 如 round 5 surfaces 新 NEW7 L6 RECURRENCE despite procedural prepend → escalate to v1.4 + spec hardening
- 如 round 5 surfaces v1.3 cut 仍 deferred 第 5 次 → escalate user as EMERGENCY-CRITICAL halt-recommendation
- 如 round 5 NEW family general-purpose AUDIT pivot 失败 (full-tool reviewer 不一定遵守 read-only AUDIT mode) → 探 NEW family adaptation pattern
- 如 round 5 surfaces drift cal NEW1 first FAIL or first ALL-PASS → 验 NEW1 spec stable

### §3 关键决策
- Round 5 multi-session 节省 vs round 1+2+3+4 比较
- 是否继续 multi-session round 6 (batches 29-31) — 取决 v1.3 cut 状态 + round 5 verdict
- v1.3 formal cut 是否 unblock 后续 efficiency
- Multi-session 是否升 Tier 3 default pattern (5 rounds saturation 后 final)
- general-purpose family AUDIT pivot recipe family-agnostic 验证 — 是否扩展到更多 cross-family pivots round 6+
- 5 family pools EXHAUSTED post round 5: 是否 stop multi-session OR pivot to data/firecrawl/superpowers families

═══════════════════════════════════════════════════════════════════
## STEP 7 — Optional Cleanup
═══════════════════════════════════════════════════════════════════

可选 (不强制):
- 删除 round 5 one-shot kickoff (`batch_26_kickoff.md` + `batch_27_kickoff.md` + `batch_28_kickoff.md` + `reconciler_kickoff_round5.md`)
- 留 MULTI_SESSION_PROTOCOL.md + 5 retro files + 5 sibling sweep reports = 11 files 作历史
- 提示 user 移除 CLAUDE.md round 5 routing rule (本次实验后 OR 切换到 round 6 routing if applicable)
- 提示 user 5 cumulative reconciler-deferred manual repair items 待清 (O-P1-65/66/67/74 + 任何 round 5 累)

═══════════════════════════════════════════════════════════════════
## STEP 8 — Final Message + User Report
═══════════════════════════════════════════════════════════════════

Echo 单行:
```
RECONCILER_DONE_ROUND_5 root_atoms=<N> pages_done=280 batches_done=28 sibling_fixes=<N> v1.3_cut=<yes|no|deferred_5th> retro_written=true
```

User-facing summary 含 round 5 contributions + cross-batch fixes + drift cal NEW1 5th time verdict + reviewer quality 3 slots (含 general-purpose family first burn AUDIT-mode pivot recipe family-agnostic 验证) + multi-session round 5 vs round 1+2+3+4 比较 + v1.3 cut decision rationale + next batch 29 kickoff prep + cleanup recommendation.

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- 修改 sub-session 输出 (`pdf_atoms_batch_NN[ab].jsonl`) 除 STEP 1 sibling/NEW6/NEW6.b/NEW7 inline fix
- 跑额外 PDF atomization / Rule A reviewer / drift cal (除非主 session 检漏跑 — halt + 报告)
- Touch CLAUDE.md / MEMORY / project meta files (除 STEP 7 cleanup 提示)
- Run git commit / push (留 user 决定)

The boulder never stops. 第一步 STEP 0 并行 10-file Read + Pre-flight check.
