# 08 Evidence 三层分层

Tier 2/3 项目的过程可追溯性保障. 三层分工 + single source of truth 原则.

---

## 为什么要三层 (而不是只有 progress.json)

v1 G2 教训: `_progress.json` + `trace.jsonl` + `evidence/step_NN.md` 在记同一件事 → 三写不一致 / 维护负担 / 复盘时不知该信哪个.

v2 修订后: **明确三层职责**, 各层不重复:

| 层 | 类型 | 唯一性 | 作用 |
|----|------|-------|------|
| L1 | 状态层 | single source of truth | "当前在哪一步, 哪些 ack, 哪些 pending" |
| L2 | 事件流层 | append-only | "谁在什么时刻做了什么" |
| L3 | 证据链层 | 分散文件 | "为什么得到这个产物, 原始输入/输出/决策" |

---

## 层 1 (L1): `_progress.json` — 状态 Single Source of Truth

### 位置

`<platform>/dev/evidence/_progress.json`

### Schema

```json
{
  "version": "v2.6",
  "status": "completed",               // running | paused | completed | failed
  "updated_at": "2026-04-20T23:45:00Z",
  "stages": {
    "v2.0_setup": {"status": "done", "acked": true, "at": "2026-04-18T10:00:00Z"},
    "v2.1_chapters": {"status": "done", "acked": true, "at": "..."},
    "v2.2_examples_high": {"status": "done", "acked": true, "at": "..."},
    "v2.3_examples_others": {"status": "done", "acked": true, "at": "..."},
    "v2.4_terminology_high": {"status": "done", "acked": true, "at": "..."},
    "v2.5_terminology_mid": {"status": "merged_into_v2.6", "acked": false},
    "v2.6_terminology_tail": {"status": "done", "acked": true, "at": "..."}
  },
  "checkpoints_acked": ["v2.1", "v2.2", "v2.3", "v2.4", "v2.6"],
  "current_stage": null,
  "pending_tasks": [],
  "phase_final_metrics": {
    "total_tokens": 1286161,
    "total_files": 19,
    "capacity_percent": 77,
    "ab_pass_ratio": "24/24"
  }
}
```

### 更新规则

- **每 Step 完成立即更新** (规则 P7)
- JSON 可被脚本 (e.g. `jq`) 或人读
- 不写详情, 详情到 L2/L3
- 如果冲突 (某字段 L1 和 L2 矛盾), **L1 胜出** (它是 source of truth)

### 反例

```json
// ❌ 反例: 把详情塞进 L1
"v2.1_chapters": {
  "status": "done",
  "full_trace": [...20 条事件...],   // 应该放 L2
  "prompts": [...writer prompt 全文...],  // 应该放 L3
}
```

---

## 层 2 (L2): `trace.jsonl` — Append-only 事件流

### 位置

`<platform>/dev/evidence/trace.jsonl`

### 格式

每行一个 JSON event, **只追加**, 不改历史行.

### Event 类型 (建议覆盖)

```jsonl
{"ts": "...", "event": "phase_init", "phase": "v2"}
{"ts": "...", "event": "stage_start", "stage": "v2.1"}
{"ts": "...", "event": "executor_dispatched", "stage": "v2.1", "subagent_type": "executor", "prompt_file": "..."}
{"ts": "...", "event": "executor_done", "stage": "v2.1", "verdict": "success"}
{"ts": "...", "event": "main_audit_done", "stage": "v2.1", "sample_n": 10, "business_pass": 8}
{"ts": "...", "event": "reviewer_dispatched", "stage": "v2.1"}
{"ts": "...", "event": "reviewer_done", "stage": "v2.1", "verdict": "PASS"}
{"ts": "...", "event": "ab_report_received", "stage": "v2.1", "pass_ratio": "7/8"}
{"ts": "...", "event": "user_consult", "stage": "v2.1", "question": "continue given T3 regression?"}
{"ts": "...", "event": "checkpoint_acked", "stage": "v2.1"}
{"ts": "...", "event": "stage_done", "stage": "v2.1"}
```

### 用途

- 复盘时做时间线可视化
- 查"谁先发生, 谁后发生"
- 统计平均批次耗时 / reviewer verdict 分布

### Source of Truth 冲突

L2 和 L1 冲突时 L1 胜出. L2 是参考, L1 是状态权威.

Claude v2 实测: trace.jsonl 65 events 有部分 event 名和初版 retrospective 对不上 (evidence-freshness cosmetic), 最终口径以 `_progress.json` 为准.

---

## 层 3 (L3): 证据链层 — 分散文件

### 子目录

```
dev/evidence/
├── _progress.json                        (L1)
├── trace.jsonl                           (L2)
├── stage_<vX.Y>_<content>.md             (L3: writer 产物摘要)
├── stage_<vX.Y>_audit.md                 (L3: 主控 Rule A 抽样报告)
├── <X>_reviewer.md                       (L3: reviewer 独立审报告)
├── <H-task>_main_audit.md                (L3: 主控结构化审)
├── subagent_prompts/                     (L3: 每次 prompt 原文)
│   ├── B1_executor_chapters.md
│   ├── B1_reviewer_chapters.md
│   └── ...
├── failures/                             (L3: 失败归档, 规则 B)
│   └── stage_<vX.Y>_attempt_<M>.md
├── checkpoints/                          (L3: Hard checkpoint handoff)
│   └── ckpt_<vX.Y>.md                   (如逐批写, 本次仅 v2.1 写了)
├── rag_decay_observations/               (L3: 如建立 RAG 曲线)
│   └── stage_<vX.Y>_decay_obs.md
├── _phase_summary.md                     (L3: 执行时间线摘要)
└── SESSION_HANDOFF_<date>.md             (L3: 跨 session 交接)
```

### `subagent_prompts/` 约定

- **全留或不留, 不留半截** (v1 G3 教训)
- 每次 subagent 调用 = 一个 .md 文件
- 文件名: `<stage>_<role>_<description>.md`

### `failures/` 约定 (规则 B)

每个失败 attempt 一个 .md, 包含:

```markdown
# Stage <X.Y> Attempt <M> — Failure Record

## 输入
- Writer prompt: `../subagent_prompts/<...>.md`
- 依赖文件: `...`

## 产物
- `...` (如有, 不论成功与否)

## 技术判定
- Reviewer verdict: FAIL
- 原因: <具体>

## 业务判定
- 主控判: FAIL / PASS_WITH_ISSUES
- 证据: <样本 X 丢失 Y>

## 下一 attempt 输入
- 调整: <改 prompt 哪里, 加哪个依赖>
- 预期改进: <...>
```

### `checkpoints/` 约定

每个 hard checkpoint 生成一个 handoff 文档:
- 当前状态
- 用户需要做什么 (e.g. 在 Claude Project 上跑 A/B)
- 回来之后 continue 的 prompt 文本

**Claude v2 实测**: 逐批写 `ckpt_v2.X.md` 太重, 最终只写了 v2.1, 后续批用 `_progress.json.checkpoints_acked` 字段归档. 证明 hybrid (JSON 字段 + 必要时文件) 够用.

---

## Tier 伸缩

| 层 | Tier 1 | Tier 2 | Tier 3 |
|----|--------|--------|--------|
| L1 `_progress.json` | 可选 (或放 notepad) | 必 | 必 |
| L2 `trace.jsonl` | 跳过 | 必 | 必 |
| L3 `stage_*_audit.md` | 一段话复盘 | 每批一份 | 每批 + 跨批对照 |
| L3 `subagent_prompts/` | 跳过 | 关键节点 (5-8 份) | 全留 (10+ 份) |
| L3 `failures/` | 跳过 | 必 (规则 B) | 必 |
| L3 `checkpoints/` | 跳过 | hybrid (JSON + 关键 1-2 份) | 逐批写 |

---

## 检查工具

### 自检脚本 (推荐 Tier 3)

写 `dev/scripts/audit_evidence.py`, 跑:
- [ ] L1 `_progress.json` schema 合规
- [ ] L2 `trace.jsonl` 每行是 valid JSON
- [ ] L3 subagent_prompts 覆盖率 (每个 stage 至少 writer + reviewer 2 份)
- [ ] L3 failures 数 == trace.jsonl failed event 数
- [ ] L1 checkpoints_acked 数 == trace.jsonl checkpoint_acked 事件数

---

## 反例 (应避免)

| 反例 | 问题 |
|------|------|
| 用 `notepad.md` / conversation 记状态 | 下一 session 丢失, 不能跨 session 交接 |
| 三层同记一件事 | v1 G2, 三写不一致 |
| trace.jsonl 改写历史行 | 破坏 append-only 性质, 审计失效 |
| failures/ 删除失败 attempt | 违反规则 B, 重跑无参考 |
| subagent_prompts/ 只留部分 | v1 G3, 假装完整 |

---

## 复盘时的用法

写 RETROSPECTIVE 时的信息源优先级:

1. **L1 `_progress.json`** — 当前状态
2. **L2 `trace.jsonl`** — 时间线 & 事件分布统计
3. **L3 subagent_prompts/** — 具体决策的输入/输出
4. **L3 failures/** — 关键教训的直接证据
5. **L3 ab_reports/** — 质量演进数据点

复盘数字的 source of truth 顺序: L1 → L2 → L3. 若 L1 说 6 个 checkpoint acked, 但 L3 只有 5 份 ckpt 文档, 以 L1 为准 (L3 可能用了 hybrid 存储).

---

*来源: claude_projects v1 G2 "状态三写" 教训 + v2 三层明确分工 + v2 RETROSPECTIVE 附录 trace.jsonl 65 events 实测口径.*
