# Reconciler Kickoff (Multi-Session Parallel — Session E, Round 2 batches 17/18/19)

> 你是 multi-session parallel 实验 round 2 的 **reconciler (session E)**.
> 仅在 session B (batch 17) + session C (batch 18) + session D (batch 19) **全 PARALLEL_SESSION_NN_DONE** 后启动.
> 你的职责: 串行合并 3 个独立 batch 工作到 root + audit_matrix + _progress.json + 写 round-2 retro + 决定是否 cut formal v1.3 prompt.
> Round 2 实验 (batches 17/18/19) — 吸收 round 1 (batches 13/14/15) MULTI_SESSION_RETRO.md G-MS-4 (halt fallback) + G-MS-7 (finding ID range pre-allocation) 两条缺口修.
> **注**: batch 16 已由 single-session resume 完成 (commit `7447ec0` 2026-04-25, 不在 round 2 multi-session merge scope 内).

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 + Pre-flight Check
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (round 1 master 协议, round 2 沿用 + augmented)
2. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO.md` (round 1 retro 三段式, round 2 是其 G-MS-4 + G-MS-7 两条缺口的实测)
3. `.work/06_deep_verification/evidence/checkpoints/_progress_batch_17.json`
4. `.work/06_deep_verification/evidence/checkpoints/_progress_batch_18.json`
5. `.work/06_deep_verification/evidence/checkpoints/_progress_batch_19.json`
6. `.work/06_deep_verification/audit_matrix.md` (current state)
7. `.work/06_deep_verification/_progress.json` (current state)

### Pre-flight 验:
- 3 个 sub-progress JSON 都有 `status="completed"` ✓
- 6 个 batch jsonl 文件都存在 (`pdf_atoms_batch_17a.jsonl` + `pdf_atoms_batch_17b.jsonl` + `pdf_atoms_batch_18a.jsonl` + `pdf_atoms_batch_18b.jsonl` + `pdf_atoms_batch_19a.jsonl` + `pdf_atoms_batch_19b.jsonl`)
- 3 个 batch report 都存在 (`P1_batch_17_report.md` + `P1_batch_18_report.md` + `P1_batch_19_report.md`)
- Reviewer slot uniqueness: #26 vercel:ai-architect + #27 plugin-dev:agent-creator + #28 oh-my-claudecode:qa-tester (无 cross-batch 撞 slot, 无 cross-round 撞 — 验 _progress_batch_NN.json 中 reviewer_slot 字段 + audit_matrix Rule D Roster #1-#25 累)
- Drift cal: batch 17 + batch 19 = skipped, batch 18 = triggered (per protocol; cumulative atoms post p.147 batch 16=298 + batch 17~250-300 ≥548 + every-3-batches cadence batch 15→18)
- 6 batch atom_id 命名空间 partition: 17a + 17b atoms 全 page ∈ [161,170], 18a + 18b ∈ [171,180], 19a + 19b ∈ [181,190]. 跨 batch 无 atom_id 冲突 (天然 partition).
- Halt state 检查: 若任一 session 写了 `halt_state_batch_NN.md` 而非 PARALLEL_SESSION_NN_DONE → 走 G-MS-4 halt fallback 决策树 (Step 0.5 below).

任一验证失败 → halt + 报告. **不要** 私自 fix sub-session 的输出.

### Step 0.5 — G-MS-4 Halt Fallback Decision Tree (Round 2 NEW)

若任一 sister session 写了 `halt_state_batch_NN.md`:

读 halt_state.md → recommended_fallback 字段 → 决策:
- (a) reconciler retry 全 batch — 主 session 改派 reconciler 自身重跑该 batch 单 session 单 a+b
- (b) reconciler defer 本 batch + merge sister batches only — 跳过该 halt 的 batch, 仅 merge 其他 sisters; 该 batch 留 partial work archive 后续 single-session repair
- (c) reconciler abort experiment — 报告 user, 不动 root, 全 partial work 归档 Rule B

写 `multi_session/halt_resolution_round2.md` 决策记录 (per Rule B + retro Rule C input).

═══════════════════════════════════════════════════════════════════
## STEP 1 — Cross-Batch Sibling Continuity Sweep
═══════════════════════════════════════════════════════════════════

⚠️ 关键 — 各 sub-session 不知对方 HEADING state, sib continuity 必由 reconciler 验.

加载 root pdf_atoms.jsonl + 6 batch files + 全部按 (page, atom_index_on_page) 排序.

### 检查项:
1. **§6.2 → §6.3 chapter-level boundary** (key decision): 验 batch 18 p.180 atom 是否产生 §6.3 [MODELS FOR FINDINGS DOMAINS] HEADING L2 sib=3 under §6 (chapter-level transition) 或仅 §6.2.8 [DA] HEADING L3 sib=8 under §6.2 (chapter-internal). PDF p.180 ground truth (TOC verified): chapter-level NEW (§6.3 + §6.3.1 DA 同时存在 p.180). 若 batch 18 写 chapter-internal, Option H inline fix.
2. **§6.2.5 / §6.2.6 / §6.2.7 sibling under §6.2** (set across batches 17+18):
   - §6.2.5 [HO] sib=5 (batch 17) + §6.2.6 [MH] sib=6 (batch 18) + §6.2.7 [DV] sib=7 (batch 18)
3. **§6.3.1 / §6.3.2 / §6.3.3 sibling under §6.3** (set across batches 18+19):
   - §6.3.1 [DA] sib=1 (batch 18) + §6.3.2 [DD] sib=2 (batch 19) + §6.3.3 [EG] sib=3 (batch 19)
4. **L4 sub-heading chain per NEW7 deterministic** for each domain:
   - 各 domain L4 sib=1 (Description/Overview) / sib=2 (Specification) / sib=3 (Assumptions) / sib=4 (Examples 若有)
   - **重点验证**: HO + MH + DV + DA + DD + EG 各 L4 sub-section chain — 防止 batch 16 O-P1-41 类 sib off-by-one 复发
5. **L5 Examples N sibling continuity** (each domain restarts from sib=1 — independent across domains).
6. **NEW6 parent_section canonical format** sweep — 验 17+18+19 atoms 全用 `§N.N.N Title (CODE)` form, 无 `[Title]` 短括号 (per batch 16 O-P1-40 lesson).

### Apply Option H fix
任何 cross-batch sib gap 或 NEW6/NEW7 violation → inline fix in batch file + accumulate finding O-P1-54+ LOW (类 batch 12 O-P1-32 / batch 16 O-P1-40+41 pattern).

写 `multi_session/sibling_continuity_sweep_report_round2.md` 含: 检查项 ✓/✗ table + 修过的 atom_id list + finding O-P1-54+.

═══════════════════════════════════════════════════════════════════
## STEP 2 — Sequential Merge to Root
═══════════════════════════════════════════════════════════════════

### Step 2.1: Backup root
```bash
cp .work/06_deep_verification/pdf_atoms.jsonl .work/06_deep_verification/pdf_atoms.jsonl.pre-multi-17-19.bak
```

### Step 2.2: Append in batch order
```bash
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_17a.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_17b.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_18a.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_18b.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_19a.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_19b.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
```

### Step 2.3: Final integrity sweep
- `wc -l .work/06_deep_verification/pdf_atoms.jsonl` 期望 = 4175 + sum(3 batch atoms)
- python3 验:
  - 0 schema error (JSON parse + 9-enum + R1 atom_id format 4-digit)
  - 0 atom_id collision (unique 全 root)
  - pages range 1-190 (全 190 unique pages)
  - atom_type distribution sanity

═══════════════════════════════════════════════════════════════════
## STEP 3 — Audit_Matrix Update
═══════════════════════════════════════════════════════════════════

Append 到 `.work/06_deep_verification/audit_matrix.md`:

### Step 3.1: P1 Batch Roster table 加 3 行
- batch 17 row (从 _progress_batch_17.json + P1_batch_17_report.md 提取)
- batch 18 row (含 drift cal 注解)
- batch 19 row

### Step 3.2: P1 Drift 校准 table 加 1 行
- batch 18 drift cal (target page + dual-threshold strict + verbatim 数值 + 根因 + action + report path; per NEW1 v1.3 candidate)

### Step 3.3: P1 Rule A 独审 table 加 3 行
- batch 17 Rule A (slot #26 vercel:ai-architect)
- batch 18 Rule A (slot #27 plugin-dev:agent-creator)
- batch 19 Rule A (slot #28 oh-my-claudecode:qa-tester)

### Step 3.4: Rule D Roster 累计 update
- 25 → 28 (3 new slots: #26 vercel:ai-architect + #27 plugin-dev:agent-creator + #28 oh-my-claudecode:qa-tester)
- Reviewer quality 观察 段加 3 个 slot 评价 (从各 batch report 提取)
- 结论段更新: n=110 cumulative anchored audit (n=80 prior + 30 new), 11 consecutive batches, 5 families validated (pr/omc/vercel/plugin-dev — 4 families post round 2 batch 18 plugin-dev 2nd burn 不增家族 + new omc 3rd burn batch 19 不增家族; 实际仍 4 families pr/omc/vercel/plugin-dev)
- 9 AUDIT-mode pivots cumulative (#20-#28: 6 pre-round-2 + 3 new)

═══════════════════════════════════════════════════════════════════
## STEP 4 — _progress.json Update
═══════════════════════════════════════════════════════════════════

Update headline:
- pages_done: 160 → **190**
- atoms_done: 4175 → final (4175 + 3 batch contributions)
- batches_done: 16 → **19**
- failures_done: 1 → 1 + sum(3 batch failures, expect 0)
- last_updated: 2026-04-25 (or current)
- status: "P1_batch_17_18_19_DONE_via_multi_session_parallel_round_2_plus_reconciler_merge_..."

Rewrite recovery_hint with:
- 3-batch summary (atoms each, repair cycles each, Rule A each, drift cal batch 18 result with NEW1 dual-threshold)
- 跨 batch lessons (R15 cross-batch sibling sweep + chapter-level §6.3 boundary 决议 + NEW6/NEW7 v1.3 candidates 验)
- Round 2 vs round 1 比较 (G-MS-4 halt fallback + G-MS-7 finding ID range 实测 verdict)
- next session batch 20 kickoff 全参数 (TOC anchor for §6.3.3 EG p.191-192 tail / §6.3.4 IE p.193 / §6.3.5 Specimen-based p.194+ / etc.)
- Rule D 烧 28 (新池 vercel/plugin-dev/omc 家族 各 batch 一个独立 slot)

═══════════════════════════════════════════════════════════════════
## STEP 5 — v1.3 Prompt Formal Cut Decision (FINAL CALL)
═══════════════════════════════════════════════════════════════════

检 v1.3 patch candidates 累 ≥3 batch 验证证据 (post round 2):
- R10 (spec table wrap-cell artifact) — batch 11/12/13/14/15 验证 ≥4 batch ✓ LOCKED
- R11 (TABLE_ROW trailing empty cell) — batch 11/12/13/14/15 验证 ≥3 batch ✓ LOCKED
- R12 (transition page full-content) — batch 11/12/14/15/16/17/18/19 验证 ≥6 batch ✓ LOCKED
- R13 (numbered list item discipline) — batch 11 only post round 2, 仍 INSUFFICIENT — 继续 observation
- R14 (writer DONE wc -l self-validation) — batch 11/12/13/14/15 + round 2 batches 验证 ≥5 batch ✓ LOCKED
- R15 (cross-batch sibling continuity) — batch 12/13/14/15/16/17/18/19 验证 ≥6 batch ✓ LOCKED
- O-P1-26 (TABLE_ROW outer-pipe convention) — batch 10/11/12/13/14/15 + round 2 验 ≥6 batch ✓ READY for codification
- **NEW6 (parent_section canonical format pin)** — batch 16 + round 2 批 17/18/19 验证 ≥3 batch (若 round 2 不复发 format split) ✓ LOCKED
- **NEW7 (level-4 sub-section sib chain deterministic)** — batch 16 + round 2 批 17/18/19 验证 ≥3 batch (若 round 2 不复发 sib off-by-one) ✓ LOCKED

### Decision matrix (round 2 FINAL CALL):
- 若 R10/R11/R12/R14/R15 + O-P1-26 + NEW6/NEW7 + (NEW1/NEW2/NEW3/NEW4/NEW5 中至少 2) 累 ≥3 batch evidence → **CUT v1.3 formal MANDATORY** (post round 2 evidence saturation)
- 若 evidence 仍不足 (unlikely post round 2) → defer formal cut to round 3 (batches 20-22 if needed)

### v1.3 cut 执行 (若决定 cut):
- 写 `subagent_prompts/P0_writer_pdf_v1.3.md` (full clean rule set: R1-R15 + O-P1-26 codified + NEW1-NEW7 incorporated)
- Archive v1.2 → `subagent_prompts/archive/v1.2_final_2026-04-25/`
- Update batch 20+ kickoff prompt 改用 v1.3
- 同时 cut companion files: `P0_writer_md_v1.3.md` + `P0_matcher_v1.3.md` + `P0_reviewer_v1.3.md` (if scope evolved)

═══════════════════════════════════════════════════════════════════
## STEP 6 — Session-End Retro (Rule C 强制, Round 2)
═══════════════════════════════════════════════════════════════════

写 `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_2.md` (Rule C 三段式, separate from round 1 retro):

### §1 保留下来的做法 (round 2 reaffirmed)
- Multi-session parallel 是否 worked 二次验 (vs round 1 50% 时间节省 baseline + cross-session coordination 成本评)
- Rule D pool partition 提前分配 (round 2 cross-round + cross-batch unique #26/#27/#28 0 撞 slot 验)
- TOC anchor + R-rules unified shared 二次验 (R10-R15 + O-P1-26 + NEW1-NEW7 全 prepend, n=110 cumulative anchored audit 0 FP/0 inversion target)
- Sub-progress 文件 + final message format reaffirmed
- Reviewer AUDIT-mode pivot 新家族 (vercel ai-architect + plugin-dev agent-creator + omc qa-tester) — 验 quality 持平 vs round 1 #22-#24 + batch 16 #25
- G-MS-7 finding ID range pre-allocation 实测 — 验 0 cross-session ID collision (vs round 1 sister-collision pattern)
- G-MS-4 halt fallback decision tree spec — 实测 (若任一 session halt 触发)

### §2 必须补上的缺口 (round 2 surfaces)
- 各 session 不知对方 sib state, R15 cross-batch sibling sweep 必由 reconciler 做 (round 1 已知, round 2 reaffirmed)
- 各 session 不知对方 lessons, 若 batch 17 触新 finding, batch 18/19 不能动态 incorporate (round 1 已知, round 2 reaffirmed)
- Drift cal cumulative cadence 跨 batch 计数易混 (round 1 已知; round 2 batch 18 mandatory drift cal 跨 round 2 sister boundary 测试 cadence 计数正确性)
- 任何 sub-session halt 都需要 reconciler 决定 fallback (G-MS-4 实测 verdict)
- 如 round 2 surfaces 新缺口 → G-MS-8+ candidate

### §3 关键决策
- Round 2 multi-session 节省 vs 协调成本 二次评估
- 是否继续 multi-session round 3 (batches 20-22) — 取决于 round 2 verdict + v1.3 cut 后 prompt 稳定性
- v1.3 formal cut 是否 unblock 后续 multi-session (e.g. R-rules locked 后, 各 session prompt 更稳定 → 协调成本降)

═══════════════════════════════════════════════════════════════════
## STEP 7 — Optional Cleanup
═══════════════════════════════════════════════════════════════════

可选 (不强制):
- 删除 `multi_session/batch_17_kickoff.md` + `batch_18_kickoff.md` + `batch_19_kickoff.md` + `reconciler_kickoff.md` (one-shot use done; 留 MULTI_SESSION_PROTOCOL.md + MULTI_SESSION_RETRO.md + MULTI_SESSION_RETRO_ROUND_2.md + sibling_continuity_sweep_report_round2.md 作历史)
- 提示 user 移除 CLAUDE.md routing rule (本次实验后)

═══════════════════════════════════════════════════════════════════
## STEP 8 — Final Message + User Report
═══════════════════════════════════════════════════════════════════

Echo 单行 + 详细 user-facing summary:
```
RECONCILER_DONE_ROUND_2 root_atoms=<N> pages_done=190 batches_done=19 sibling_fixes=<N> chapter_level_boundary_§6.3=<resolved|halt> v1.3_cut=<yes|no> retro_written=true
```

User-facing summary 含:
- 3 batch contributions 各自
- Cross-batch sibling fixes (O-P1-54+ if any)
- Chapter-level §6.3 boundary 决议 (chapter-internal vs chapter-level NEW)
- Drift cal batch 18 verdict + dual-threshold per NEW1
- Reviewer quality summary (3 new slots #26/#27/#28)
- Multi-session round 2 vs round 1 比较 (节省时间 + 协调成本 + halt fallback 实测)
- v1.3 prompt cut decision rationale (post round 2 evidence saturation)
- Next batch 20 kickoff 准备情况

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- 修改 sub-session 输出 (`pdf_atoms_batch_NN[ab].jsonl`) — 那是 sub-session 的真理 (除 sibling continuity inline fix per Step 1 + NEW6/NEW7 normalization)
- 跑额外 PDF atomization (那是 sub-session 的事)
- 跑额外 Rule A reviewer (那是 sub-session 的事)
- 跑额外 drift cal (除非主 session 检 batch 18 drift cal 被 sub-session 漏跑 — halt + 报告 user 而非自己跑)
- Touch CLAUDE.md / MEMORY / project meta files (除非 STEP 7 cleanup 提示)
- Run git commit / push (留 user 决定)
- 跨 batch 改 atom 内容 (e.g. 看到 batch 18 atom 数据似有问题, 不要 reconciler 自己修, 应记 finding 让 user 决定 follow-up)

开干. 第一步 STEP 0 并行 7-file Read + Pre-flight check.
