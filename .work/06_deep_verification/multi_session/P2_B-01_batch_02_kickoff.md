# P2 B-01 batch 02 — Multi-Session Kickoff

> 创建: 2026-04-29 (post P2 Pilot + B-01 batch 01 闭环 same day)
> 父 sub-plan: `plans/P2_md_atomization.md` v1.0 (2026-04-29 user ack'd)
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.md` (cut 2026-04-29 post-pilot, 8 NEW patches C-1..C-8)
> 路由词: 用户在新 session 说 **"P2 bulk B-01 batch 02 开始任务"** 即触发本 kickoff

---

## 1. Session 启动前必读 (按序)

1. `.work/06_deep_verification/evidence/checkpoints/p2_pilot_report.md` — Pilot 2-attempt 闭环结论 + v1.9 cut 缘由
2. `.work/06_deep_verification/subagent_prompts/P0_writer_md_v1.9.md` (134 行, **主体 prompt**) + `P0_reviewer_v1.9.md` (75 行)
3. `.work/06_deep_verification/audit_matrix.md` 末段 P2 section (cumulative state)
4. 本 kickoff 文件 (本身)

---

## 2. Batch 02 任务

### 2.1 Target

- **文件**: `knowledge_base/model/02_observation_classes.md` (298 lines)
- **估 atoms**: ~210 (per file 0.7 atoms/line empirical from pilot)
- **切片建议**: 单文件 1 dispatch 即 ~17K tokens 输出, 距 32K cap 充足. **不需要切片**, 但若 dispatch 撞 token 上限 (前例 P2 pilot Attempt 2 第 5 个 file 撞 32K), fallback 切 2 段 lines 1-150 + 151-298.

### 2.2 Dispatch 模板

派 `oh-my-claudecode:executor` 单 dispatch, prompt 模板 (镜像 batch 01 模式):

- 加载 `subagent_prompts/P0_writer_md_v1.9.md` + archive v1.8/v1.7 base
- 加载 `schema/atom_schema.json` v1.2 frozen
- atom_id prefix `md_model02_a{NNN}` from `a001`
- batch_id `P2_B-01_batch_02`
- 输出 `evidence/checkpoints/P2_B-01_batch_02_md_atoms.jsonl`
- prompt_version `"P0_writer_md_v1.9"`
- subagent_type `"oh-my-claudecode:executor"`
- file 字段全路径 `knowledge_base/model/02_observation_classes.md` (C-8)
- 22 hooks self-validate

### 2.3 Rule A 跟进

派 `oh-my-claudecode:scientist` (slot 72 复用 OK, fresh dispatch independence) 跑 10-atom 分层独审:
- 加载 `subagent_prompts/P0_reviewer_v1.9.md` (含 §R-C1 sub-line tolerance + §R-C3..C-7 anti-defect)
- 输出 `evidence/checkpoints/rule_a_P2_B-01_batch_02_verdicts.jsonl` + `_summary.md`
- gate ≥90% PASS

### 2.4 Append + checkpoint

PASS 后:
- cat batch 02 jsonl → `md_atoms.jsonl` 追加 (`>> md_atoms.jsonl`)
- `wc -l md_atoms.jsonl` 验证累计原子数 (post batch 01 = 506; post batch 02 应 ~716)
- `audit_matrix.md` P2 Bulk 表 batch 02 行从 TBD 更新到具体值
- `trace.jsonl` 写 batch 02 phase_report 事件

---

## 3. Batch 03 + 04 (跟进同 session 或下下 session)

| Batch | File | Lines | 估 atoms | 切片? |
|---|---|---|---|---|
| **P2_B-01_batch_03** | `knowledge_base/model/03_special_purpose_domains.md` | 190 | ~135 | 单 dispatch OK |
| **P2_B-01_batch_04** | `knowledge_base/model/05_study_level_data.md` | 296 | ~210 | 单 dispatch OK (fallback 2 段) |

batch 04 完成后 B-01 全闭环 (model/* 剩 4 文件全原子化), 转 B-02 (chapters/ 剩 5 + ch04 续 5 段).

---

## 4. v1.9.1 候选 (open finding from batch 01)

- **md_model06_a029 line_start off-by-one** — atom 写 line 43 但实际 heading "### RELTYPE Combinations" 在 line 42. 1/14 HEADING atoms 漂移. v1.9.1 候选: writer prompt 显式提醒 "HEADING atom line_start = source heading 物理行号, 不要靠 grep/Read tool offset 估算"
- 累计 v1.9.1 候选: 1 (LOW), 不阻塞 bulk

---

## 5. 路由词 quick reference

| 用户说 | session 动作 |
|---|---|
| `P2 bulk B-01 batch 02 开始任务` | 读本 kickoff + dispatch executor for model/02 |
| `P2 bulk B-01 batch 03 开始任务` | (本 kickoff §3 spec) dispatch for model/03 |
| `P2 bulk B-01 batch 04 开始任务` | (§3 spec) dispatch for model/05 |
| `P2 bulk B-02 开始任务` | (待写新 kickoff) — chapters/ 剩 5 + ch04 续 5 段 |

---

## 6. Recovery hint

若 session 中断:
- 看 `_progress.json` (主) 或 `evidence/checkpoints/_progress_P2_pilot_and_B-01_batch_01.json` (sidecar) 找 `current_phase` + `last_completed_batch`
- 看 `trace.jsonl` 尾 phase_report 事件
- 看 `audit_matrix.md` P2 Bulk 表最后 PASS 行

---

*Kickoff written 2026-04-29 (P1 CLOSURE + P2 Pilot + B-01 batch 01 同日闭环). 下一 session 资源齐.*
