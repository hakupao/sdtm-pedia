# Reconciler Kickoff (Multi-Session Parallel — Session E)

> 你是 multi-session parallel 实验的 **reconciler (session E)**.
> 仅在 session B (batch 13) + session C (batch 14) + session D (batch 15) **全 PARALLEL_SESSION_NN_DONE** 后启动.
> 你的职责: 串行合并 3 个独立 batch 工作到 root + audit_matrix + _progress.json + 写 retro + 决定是否 cut formal v1.3 prompt.

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 + Pre-flight Check
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (你的协议)
2. `.work/06_deep_verification/evidence/checkpoints/_progress_batch_13.json`
3. `.work/06_deep_verification/evidence/checkpoints/_progress_batch_14.json`
4. `.work/06_deep_verification/evidence/checkpoints/_progress_batch_15.json`
5. `.work/06_deep_verification/audit_matrix.md` (current state)
6. `.work/06_deep_verification/_progress.json` (current state)

### Pre-flight 验:
- 3 个 sub-progress JSON 都有 `status="completed"` ✓
- 6 个 batch jsonl 文件都存在 (`pdf_atoms_batch_13a.jsonl` + `pdf_atoms_batch_13b.jsonl` + `pdf_atoms_batch_14a.jsonl` + `pdf_atoms_batch_14b.jsonl` + `pdf_atoms_batch_15a.jsonl` + `pdf_atoms_batch_15b.jsonl`)
- 3 个 batch report 都存在 (`P1_batch_13_report.md` etc.)
- Reviewer slot uniqueness: #22 vercel:performance-optimizer + #23 oh-my-claudecode:designer + #24 vercel:deployment-expert (无 cross-batch 撞 slot — 验 _progress_batch_NN.json 中 reviewer_slot 字段)
- Drift cal: batch 13 + batch 14 = skipped, batch 15 = triggered (per protocol)
- 6 batch atom_id 命名空间 partition: 13a + 13b atoms 全 page ∈ [121,130], 14a + 14b ∈ [131,140], 15a + 15b ∈ [141,150]. 跨 batch 无 atom_id 冲突 (天然 partition).

任一验证失败 → halt + 报告. **不要** 私自 fix sub-session 的输出.

═══════════════════════════════════════════════════════════════════
## STEP 1 — Cross-Batch Sibling Continuity Sweep
═══════════════════════════════════════════════════════════════════

⚠️ 关键 — 各 sub-session 不知对方 HEADING state, sib continuity 必由 reconciler 验.

加载 root pdf_atoms.jsonl + 6 batch files + 全部按 (page, atom_index_on_page) 排序.

### 检查项:
1. **§6.1.x → §6.2.x sibling continuity** under §6:
   - §6.1 L2 sib=1 (set earlier) + §6.2 L2 sib=2 (NEW batch 14)
2. **§6.1.4 / §6.1.5 / §6.1.6 sibling under §6.1** (set in batch 13):
   - §6.1.1 sib=1 (earlier) + §6.1.2 sib=2 (earlier) + §6.1.3 sib=3 (earlier) + §6.1.4 sib=4 + §6.1.5 sib=5 + §6.1.6 sib=6
3. **§6.2.1 / §6.2.2 / §6.2.3 sibling under §6.2** (set across batches 14+15):
   - §6.2.1 sib=1 (batch 14) + §6.2.2 sib=2 (batch 15) + §6.2.3 sib=3 (batch 15)
4. **L4 sub-heading convention** for each domain:
   - 各 domain L4 sib=1 (Description/Overview) / sib=2 (Specification) / sib=3 (Assumptions) / sib=4 (Examples 若有)
5. **L5 Examples N sibling continuity** (each domain restarts from sib=1 — independent across domains): 不需要跨 domain continuity, 仅 verify within each domain Examples sib=1,2,3,...

### Apply Option H fix
任何 cross-batch sib gap → inline fix in batch file + accumulate finding O-P1-NN LOW (类 batch 12 O-P1-32 pattern).

写 `multi_session/sibling_continuity_sweep_report.md` 含: 检查项 ✓/✗ table + 修过的 atom_id list + finding.

═══════════════════════════════════════════════════════════════════
## STEP 2 — Sequential Merge to Root
═══════════════════════════════════════════════════════════════════

### Step 2.1: Backup root
```bash
cp .work/06_deep_verification/pdf_atoms.jsonl .work/06_deep_verification/pdf_atoms.jsonl.pre-multi-13-15.bak
```

### Step 2.2: Append in batch order
```bash
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_13a.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_13b.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_14a.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_14b.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_15a.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
cat .work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_15b.jsonl >> .work/06_deep_verification/pdf_atoms.jsonl
```

### Step 2.3: Final integrity sweep
- `wc -l .work/06_deep_verification/pdf_atoms.jsonl` 期望 = 3200 + sum(3 batch atoms)
- python3 验:
  - 0 schema error (JSON parse + 9-enum + R1 atom_id format)
  - 0 atom_id collision (unique 全 root)
  - pages range 1-150 (全 150 unique pages)
  - atom_type distribution sanity (HEADING/SENTENCE/LIST_ITEM/TABLE_HEADER/TABLE_ROW/CODE_LITERAL/NOTE/FIGURE/CROSS_REF 都 >= 0)

═══════════════════════════════════════════════════════════════════
## STEP 3 — Audit_Matrix Update
═══════════════════════════════════════════════════════════════════

Append 到 `.work/06_deep_verification/audit_matrix.md`:

### Step 3.1: P1 Batch Roster table 加 3 行
- batch 13 row (从 _progress_batch_13.json + P1_batch_13_report.md 提取)
- batch 14 row (同)
- batch 15 row (含 drift cal 注解)

### Step 3.2: P1 Drift 校准 table 加 1 行
- batch 15 drift cal (target page + match rate + root cause + action + report path)

### Step 3.3: P1 Rule A 独审 table 加 3 行
- batch 13 Rule A (slot #22 vercel:performance-optimizer)
- batch 14 Rule A (slot #23 oh-my-claudecode:designer)
- batch 15 Rule A (slot #24 vercel:deployment-expert)

### Step 3.4: Rule D Roster 累计 update
- 21 → 24 (3 new slots: #22 vercel:performance-optimizer + #23 oh-my-claudecode:designer + #24 vercel:deployment-expert)
- Reviewer quality 观察 段加 3 个 slot 评价 (从各 batch report 提取)
- 结论段更新 n=70 cumulative anchored audit (n=40 prior + 30 new)

═══════════════════════════════════════════════════════════════════
## STEP 4 — _progress.json Update
═══════════════════════════════════════════════════════════════════

Update headline:
- pages_done: 120 → **150**
- atoms_done: 3200 → final (3200 + 3 batch contributions)
- batches_done: 12 → **15**
- failures_done: 1 → 1 + sum(3 batch failures, expect 0)
- last_updated: 2026-04-25 (or current)
- status: "P1_batch_13_14_15_DONE_via_multi_session_parallel_plus_reconciler_merge_..."

Rewrite recovery_hint with:
- 3-batch summary (atoms each, repair cycles each, Rule A each, drift cal batch 15 result)
- 跨 batch lessons (R15 cross-batch sibling, multi-session protocol validation)
- next session batch 16 kickoff 全参数 (TOC anchor for §6.2.4 DS p.155 / §6.2.5 HO p.167 / etc.)
- Rule D 烧 24 (新池 vercel/omc 家族扩)

═══════════════════════════════════════════════════════════════════
## STEP 5 — v1.3 Prompt Formal Cut Decision
═══════════════════════════════════════════════════════════════════

检 v1.3 patch candidates 累 ≥3 batch 验证证据:
- R10 (spec table wrap-cell artifact) — batch 11/12 验证 ≥2 batch ✓
- R11 (TABLE_ROW trailing empty cell) — batch 11/12 验证 ≥2 batch ✓
- R12 (transition page full-content) — batch 11/12/14/15 验证 ≥4 batch ✓
- R13 (numbered list item discipline) — batch 11 only, 需更多 evidence
- R14 (writer DONE wc -l self-validation) — batch 11/12 验证 ≥2 batch ✓ (batch 12 R14 BREAKTHROUGH)
- R15 (cross-batch sibling continuity) — batch 12 only, 需更多 evidence
- O-P1-26 (TABLE_ROW outer-pipe convention) — INFO defer

### Decision matrix:
- 若 R10/R11/R12/R14 + (R13 / R15 / O-P1-26 中至少 1) 累 ≥3 batch → **CUT v1.3 formal**
  - 写 `subagent_prompts/P0_writer_pdf_v1.3.md` (full clean rule set)
  - Archive v1.2 → `subagent_prompts/archive/v1.2_final_2026-04-25/`
  - Update batch 16+ kickoff prompt 改用 v1.3
- 若 evidence 不足 → defer formal cut, 继续累 batch 16-20 evidence

═══════════════════════════════════════════════════════════════════
## STEP 6 — Session-End Retro (Rule C 强制)
═══════════════════════════════════════════════════════════════════

写 `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO.md` (Rule C 三段式):

### §1 保留下来的做法
- Multi-session parallel 是否 worked (vs serial baseline 50% 时间节省 vs cross-session coordination 成本)
- Rule D pool partition 提前分配 vs 各 session 自选 — 验 0 撞 slot
- TOC anchor + R-rules unified shared — 验 0 inversion / 0 R-rule violation
- Sub-progress 文件 + final message format — reconciler 是否 easily aggregate
- Reviewer AUDIT-mode pivot 跨 family (vercel + omc + vercel) — 验 quality 持平 vs slot #20/#21

### §2 必须补上的缺口
- 跨 session 协调成本 (e.g. user 必须手开 3 终端 + reconciler 串行)
- 各 session 不知 sibling state, R15 cross-batch sibling sweep 必由 reconciler 做
- 各 session 不知对方 lessons, 若 batch 13 触新 finding, batch 14/15 不能动态 incorporate
- Drift cal cumulative cadence 跨 batch 计数易混 (e.g. batch 13 = 不触, batch 15 = 必触, 跨 session 状态难维护)
- 任何 sub-session halt 都需要 reconciler 决定 fallback (vs single-session 主 session 直接 decide)

### §3 关键决策
- multi-session 适合 **independent 工作 + low coordination overhead** 场景 (本次 P1 batch 是 independent + medium coord, 适合)
- 不适合 **high cross-batch coupling** (e.g. batch 16-20 若 chapter §6.3 includes complex cross-domain Examples, multi-session 协调成本 > 节省)
- 推荐: P1 后续 batches if dense + low coupling → 继续 multi-session; if § 跨 batch 复杂 → fall back single-session
- v1.3 formal cut 是否 unblock 后续 multi-session (e.g. R-rules locked 后, 各 session prompt 更稳定 → 协调成本降)

═══════════════════════════════════════════════════════════════════
## STEP 7 — Optional Cleanup
═══════════════════════════════════════════════════════════════════

可选 (不强制):
- 删除 `multi_session/batch_13_kickoff.md` + `batch_14_kickoff.md` + `batch_15_kickoff.md` + `reconciler_kickoff.md` (one-shot use done; 留 MULTI_SESSION_PROTOCOL.md + MULTI_SESSION_RETRO.md + sibling_continuity_sweep_report.md 作历史)
- 提示 user 移除 CLAUDE.md routing rule (本次实验后)

═══════════════════════════════════════════════════════════════════
## STEP 8 — Final Message + User Report
═══════════════════════════════════════════════════════════════════

Echo 单行 + 详细 user-facing summary:
```
RECONCILER_DONE root_atoms=<N> pages_done=150 batches_done=15 sibling_fixes=<N> v1.3_cut=<yes|no> retro_written=true
```

User-facing summary (类 batch 12 mid-session 汇报 format) 含:
- 3 batch contributions 各自
- Cross-batch sibling fixes (O-P1-NN if any)
- Drift cal batch 15 verdict + action
- Reviewer quality summary (3 new slots)
- Multi-session experiment verdict (节省时间 vs 协调成本)
- v1.3 prompt cut decision rationale
- Next batch 16 kickoff 准备情况

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- 修改 sub-session 输出 (`pdf_atoms_batch_NN[ab].jsonl`) — 那是 sub-session 的真理 (除 sibling continuity inline fix per Step 1)
- 跑额外 PDF atomization (那是 sub-session 的事)
- 跑额外 Rule A reviewer (那是 sub-session 的事)
- 跑额外 drift cal (除非主 session 检 batch 15 drift cal 被 sub-session 漏跑 — halt + 报告 user 而非自己跑)
- Touch CLAUDE.md / MEMORY / project meta files (除非 STEP 7 cleanup 提示)
- Run git commit / push (留 user 决定)
- 跨 batch 改 atom 内容 (e.g. 看到 batch 14 atom 数据似有问题, 不要 reconciler 自己修, 应记 finding 让 user 决定 follow-up)

开干. 第一步 STEP 0 并行 6-file Read + Pre-flight check.
