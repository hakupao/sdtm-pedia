<!-- TEMPLATE: 复制本文件为 step_<NN>_<name>.md 后填写 -->

# Step <N>: <任务名>

> 计划锚点: [PLAN.md §7.4 Step <N>](../../PLAN.md#step-<N>)
> 执行日期: YYYY-MM-DD
> 状态: PASS | FAIL | RETRY

---

## 1. 输入

- 源文件:
  - `knowledge_base/...` (md5: ...)
- 参考决策: PLAN §3.2 D<n>
- Token 目标: ≤ <X>K

## 2. Agent 调度

| 角色 | subagent_type | model | 调用时间 | 完整 prompt |
|------|--------------|-------|---------|------------|
| 作者 | oh-my-claudecode:executor | opus | YYYY-MM-DD HH:MM | [link](subagent_prompts/step_<NN>_executor.md) |
| 复核 | oh-my-claudecode:code-reviewer | sonnet | YYYY-MM-DD HH:MM | [link](subagent_prompts/step_<NN>_reviewer.md) |

## 3. 产出

| 项 | 值 |
|---|---|
| 脚本 | `scripts/<name>.py` (lines: ...) |
| 输出文件 | `output/<file>.md` |
| 实测 tokens | ... |
| 目标 tokens | ... |
| 偏差 | +X% / -X% |
| 源路径标注数 | grep `<!-- source:` 计数 |

## 4. 复核结果

复核 agent 返回：

```
<复核 agent 的关键结论摘要 (≤200 字)>
```

- [ ] 检查项 1: 描述 — PASS/FAIL
- [ ] 检查项 2: 描述 — PASS/FAIL
- ...

## 5. 偏差与处理

> 如全部 PASS，本节填 "无偏差"

| 偏差 | 严重度 | 处理 |
|-----|-------|------|
| ... | 高/中/低 | 已修复 / 接受 / 待处理 |

## 6. Checkpoint（如 §7.7 要求）

- 是否需要 checkpoint: 是 / 否
- 汇报内容: 见 [checkpoints/ckpt_step<NN>.md](checkpoints/ckpt_step<NN>.md)
- 用户回应: yes / 调整 / 暂停
- 回应时间: YYYY-MM-DD HH:MM

## 7. 累计指标

- 本 Step 后总 token 进度: <累计> / 195K (<%>)
- 本 Step 调用 subagent 数: <N>
- 本 Step 重试次数: <N>

## 8. 下一步

- 下一 Step: Step <N+1> — <名称>
- 是否阻塞: 否 / 是 (原因: ...)
