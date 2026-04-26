# Multi-Session Parallel Protocol — Batches 13/14/15

> Date: 2026-04-25
> Strategy: 方案 B 物理并行 (3 终端各跑 1 batch + 1 reconciler 收尾)
> Lifetime: temporary (本次实验完后回归 single-session 模式 by removing CLAUDE.md routing rule)

---

## 角色 / 职责矩阵

| 终端 | Session ID | 职责 | 触发指令 (user 输入) | 输出文件 (独占) | 不动文件 (共享) |
|---|---|---|---|---|---|
| 1 | session B | batch 13 (p.121-130) | `batch 13 开始任务` | `pdf_atoms_batch_13a.jsonl` + `pdf_atoms_batch_13b.jsonl` + `_progress_batch_13.json` + `P1_batch_13_report.md` + `rule_a_batch_13_*` | root `pdf_atoms.jsonl` / `audit_matrix.md` / `_progress.json` |
| 2 | session C | batch 14 (p.131-140) | `batch 14 开始任务` | `pdf_atoms_batch_14a.jsonl` + `pdf_atoms_batch_14b.jsonl` + `_progress_batch_14.json` + `P1_batch_14_report.md` + `rule_a_batch_14_*` | (同上) |
| 3 | session D | batch 15 (p.141-150) | `batch 15 开始任务` | `pdf_atoms_batch_15a.jsonl` + `pdf_atoms_batch_15b.jsonl` + `_progress_batch_15.json` + `P1_batch_15_report.md` + `rule_a_batch_15_*` + `drift_cal_batch_15_*` (mandatory cadence) | (同上) |
| 4 | session E (启动 after 1+2+3 全 DONE) | reconciler 串行合并 | `reconciler 开始任务` | 写 root `pdf_atoms.jsonl` + `audit_matrix.md` + `_progress.json` + session-end retro | n/a (合并后所有都可写) |

---

## Pre-shared State Snapshot (本 session 12 末)

| 项 | 值 |
|---|---|
| pages_done | 120 (p.1-120) |
| atoms_done (root) | 3200 |
| batches_done | 12 |
| failures_done | 1 (batch 06 attempt 1, Rule B archived) |
| Findings | 35 (O-P1-01..35) |
| Rule D 烧 | 21 (last: oh-my-claudecode:debugger #21 AUDIT-mode pivot) |
| Repair cycles cumulative | 14 |
| TOC anchor methodology | locked at n=40 cumulative 0 FP / 0 inversion across slot #18-#21 |
| Drift cal last | p.118 (batch 12), cumulative since = 271 atoms (just batch 12 net) |
| Drift cal next mandatory | batch 15 (per "every 3 batches" cadence; cumulative atoms ≥300 also met) |

---

## Reviewer Pool Partition (Rule D unique, **HARDCODED 不可改**)

| Batch | Slot # | 候选 Agent | Mode | Family Pivot |
|---|---|---|---|---|
| 13 | #22 | `vercel:performance-optimizer` | AUDIT (NOT performance optimization) | vercel-family **首烧** (3rd AUDIT-pivot post slot #20 pr / #21 omc) |
| 14 | #23 | `oh-my-claudecode:designer` | AUDIT (NOT design) | omc-family extension (4th AUDIT-pivot) |
| 15 | #24 | `vercel:deployment-expert` | AUDIT (NOT deployment) | vercel-family extension (5th AUDIT-pivot) |

**严禁** session 自选 reviewer slot — 必须用上面预分配 (避免跨 session 撞烧 Rule D).

If pre-assigned reviewer fails to dispatch (agent type not available), session 必须 halt 并报告, **不要** 私自选 fallback (会 Rule D 撞).

---

## Output Files Per Session (独占, 不冲突)

每 session 只在以下路径写:

```
.work/06_deep_verification/evidence/checkpoints/
  pdf_atoms_batch_NNa.jsonl                  ← 写手 A 输出
  pdf_atoms_batch_NNb.jsonl                  ← 写手 B 输出
  pdf_atoms_batch_NNa.jsonl.pre-*.bak        ← Option H 修前 backup (Rule B)
  pdf_atoms_batch_NNb.jsonl.pre-*.bak        ← Option H 修前 backup (Rule B)
  _progress_batch_NN.json                    ← session 自己的 sub-progress (新文件, 非主 _progress.json)
  P1_batch_NN_report.md                      ← session 自己的 batch report
  rule_a_batch_NN_sample.jsonl               ← Rule A sample
  rule_a_batch_NN_verdicts.jsonl             ← Rule A verdicts
  rule_a_batch_NN_summary.md                 ← Rule A summary
  drift_cal_batch_NN_pXXX_*.{jsonl,md}       ← (仅 batch 15 必有, 13/14 不触)
```

NN ∈ {13, 14, 15}. 任何 session 写跨 NN 的文件都是错.

---

## Shared Files (绝对不动 / 留给 reconciler)

每 session **不可写, 仅可读**:

```
.work/06_deep_verification/
  pdf_atoms.jsonl                            ← root, reconciler 串行 merge
  audit_matrix.md                            ← reconciler 串行 append 3 batch row + Rule A row + Rule D update
  _progress.json                             ← reconciler 串行 update headline + recovery_hint
  subagent_prompts/v1.3_patch_candidates.md  ← v1.3 cut EXECUTED 2026-04-27 (historical)
  subagent_prompts/P0_writer_pdf_v1.3.md     ← v1.3 active 2026-04-27 (cut completed; P0_writer_pdf_v1.2.md retained side-by-side per archive convention)
  schema/*.json                              ← 不动
  PLAN.md                                    ← 不动
  plans/*.md                                 ← 不动
```

CLAUDE.md / MEMORY 类全项目文件: **绝对不动**.

`evidence/checkpoints/_progress.json.pre-batch11.bak` 等历史 backup: **绝对不动**.

`pdf_atoms.jsonl.pre-batch12.bak` / `pdf_atoms.jsonl.pre-OptionE-p119.bak`: **绝对不动**.

---

## R-Rules Unified (15 累, 全 batch 通用)

R1-R14 same as batch 12 (atom_id 4-digit/3-digit / DONE single-line / HEADING vs LIST_ITEM TOC-anchored / lettered list dedup / TOC anchor parent_section / codelist literal verbatim / output JSONL pure + DONE strict match / TABLE_ROW empty cell `\| \|` / dataset filename CODE_LITERAL physical-page parent / spec table wrap-cell artifact / TABLE_ROW trailing empty cell preservation / transition page full-content discipline / numbered list item discipline regardless of bold / writer DONE atoms=N self-validation).

**R15 NEW from batch 12 O-P1-32**: Cross-batch sibling_index continuity. Parallel writer agents lack each other's HEADING state. Main session post-merge must sweep cross-batch sibling continuity for HEADING atoms (Examples N / Subject XXX / sub-headings sib=1,2,3,...). Each kickoff prompt includes prior batch's terminal HEADING list as context for sibling continuity.

详见各 kickoff 文件内 inline 完整 R-rule block.

---

## Drift Cal Trigger Schedule

- **Batch 13**: 不触发 (cumulative 自 p.118 当前 271 atoms; 加 batch 13 ~250 = ~521; per "every 3 batches" cadence next mandatory at batch 15)
- **Batch 14**: 不触发 (per cadence)
- **Batch 15**: **MANDATORY** (every-3-batches cadence + cumulative ≥300 双触发)
  - Target page candidate: TBD by session D (suggest dense TABLE_ROW page in §6.2.1 AE Examples region, e.g. p.143 BE start or p.148 CE start or p.150 AE Examples if applicable)
  - 2-way: writer 15b baseline + executor rerun
  - Threshold ≥80%
  - 报告: `drift_cal_batch_13_15_pXXX_report.md` (注: 文件名 prefix 用 batch range — last cal batch + current batch)

---

## Halt Conditions (per session)

任一触发则 halt 并报告:
- writer failure rate >15% in batch
- drift cal 2-way <80% AND tiebreaker <80%
- Rule A raw FAIL <70% (单 session 单批不会触发整个 P1 halt, 但 session 必须 halt 等 reconciler 决定)
- ctx 用量超 80%
- 预分配 reviewer 不可派发 (Rule D 撞风险)
- 任何尝试写 shared file 的代码路径

---

## Session Final Message Format

每 session 末尾必须 echo 单行:

```
PARALLEL_SESSION_NN_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=<triggered|skipped> findings_added=<list>
```

例:
```
PARALLEL_SESSION_13_DONE atoms=247 failures=0 repair_cycles=2 rule_a=92% drift_cal=skipped findings_added=O-P1-36,O-P1-37
```

Reconciler session 读这些 line 知道各 session 状态.

---

## Reconciler Protocol

Reconciler session E 负责 (当 1+2+3 全 PARALLEL_SESSION_NN_DONE 后):

1. **Pre-flight checks**:
   - 验 3 个 `_progress_batch_NN.json` 都有 status=completed
   - 验 6 个 `pdf_atoms_batch_NN[ab].jsonl` 都存在
   - 验 各 atom_id 命名空间无 cross-batch 冲突 (n[NN_a vs n[NM]_a, NN ≠ NM 天然 partition)
   - 验 reviewer slot uniqueness (#22 / #23 / #24 各 unique, 无 cross-batch 撞)

2. **Cross-batch sibling continuity sweep**:
   - 加载 6 个 batch jsonl + root pdf_atoms.jsonl
   - 按 (page, atom_index_on_page) 排序
   - 对每个 HEADING 类系列 (Examples N / 各章节 sub) 检查 sibling_index 连续性
   - Apply Option H fix 任何 cross-batch sib gap

3. **Sequential merge to root**:
   - Backup `pdf_atoms.jsonl` → `pdf_atoms.jsonl.pre-multi-13-15.bak`
   - cat 6 batch files → root (按 batch order 13/14/15)
   - 验 root 0 collision / 0 schema err

4. **Audit_matrix update**:
   - Append batch 13/14/15 rows
   - Append Rule A 13/14/15 rows
   - Append drift cal 15 row (若 batch 15 触发)
   - Update Rule D roster: 21 → 24

5. **_progress.json update**:
   - pages_done 120 → 150
   - atoms_done 3200 → final
   - batches_done 12 → 15
   - findings 累 35 → final
   - last_updated date
   - Rewrite recovery_hint with 3-batch summary + lessons + next batch 16 kickoff

6. **v1.3 prompt formal cut decision**:
   - **RESOLVED 2026-04-27** in dedicated v1.3 cut session — 4 v1.3 prompts written + Rule D reviewer #35 PASS + v1.2 archived. Round 5+ reconcilers skip this step; v1.4 candidates surface to retro instead.

7. **Session-end retro**:
   - 写 `multi_session/MULTI_SESSION_RETRO.md` (Rule C 强制)
   - 三段: 保留 / 缺口 / 决策

8. **Cleanup multi_session/ kickoff files** (optional):
   - keep MULTI_SESSION_PROTOCOL.md + MULTI_SESSION_RETRO.md as historical
   - delete batch_NN_kickoff.md + reconciler_kickoff.md (one-shot use done)
   - 提示 user 移除 CLAUDE.md routing rule (本次实验后)

---

## User-Facing Cheatsheet

```
终端 1:  $ claude        (boot Claude Code session B)
         > batch 13 开始任务
         (Claude reads batch_13_kickoff.md, runs, ends with PARALLEL_SESSION_13_DONE)

终端 2:  $ claude        (boot Claude Code session C)
         > batch 14 开始任务
         (Claude reads batch_14_kickoff.md, runs, ends with PARALLEL_SESSION_14_DONE)

终端 3:  $ claude        (boot Claude Code session D)
         > batch 15 开始任务
         (Claude reads batch_15_kickoff.md, runs, ends with PARALLEL_SESSION_15_DONE)

— 等 3 个终端全 DONE —

终端 4 (or 复用 1/2/3 任一):
         > reconciler 开始任务
         (Claude reads reconciler_kickoff.md, merges, writes retro, reports)
```

3 batch 物理并行 + 1 reconciler 收尾 = ~60-80 min wall (vs serial ~150 min, 节省 50%).
