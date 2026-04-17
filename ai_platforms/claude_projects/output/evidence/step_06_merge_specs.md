# Step 6: merge_specs.py (MEGA SPEC)

> 计划锚点: [PLAN.md §7.4 Step 6](../../PLAN.md)（⚠️ CRITICAL 最大风险点）
> 执行日期: 2026-04-17
> 状态: **PASS** (attempt 2 + patch, CONDITIONAL_PASS 后修复 COUNTRY)
> Attempt 1 归档: [failures/step_06_attempt_1.md](failures/step_06_attempt_1.md)

---

## 1. 输入

- 63 × `knowledge_base/domains/<DOM>/spec.md` (1917 变量, 184943 tokens)
- 目标: ≤60K 严 / ≤66K 接受
- 决策: PLAN §3.2 D1 / §4.3.1 / §7.4 Step 6

## 2. Agent 调度（两轮 + 修补）

| 角色 | subagent | model | duration | 产出 |
|------|---------|-------|---------|------|
| Attempt 1 executor | executor | opus | 291s | Level 4 回退（Notes 整删）58706 tok |
| Attempt 1 reviewer | code-reviewer | opus | 120s | CONDITIONAL_PASS — 20% unique info lost |
| 用户 checkpoint | 主控 | — | — | 选择"混合方案重试" |
| Attempt 2 executor | executor | opus | 678s | Smart Notes 保留 65988 tok |
| Attempt 2 reviewer | code-reviewer | opus | 172s | CONDITIONAL_PASS — COUNTRY ISO 3166 missed |
| Patch executor | executor | sonnet | 94s | RE_SN_ISO 扩展 8601\|3166\|4217\|639 |

Prompt 归档:
- [step_06_executor.md](subagent_prompts/step_06_executor.md) (attempt 1)
- [step_06_executor_attempt_2.md](subagent_prompts/step_06_executor_attempt_2.md)

## 3. 产出

| 项 | 值 |
|---|---|
| 脚本 | `scripts/merge_specs.py` (728 行, +199 smart_compact_notes) |
| 输出 | `output/05_mega_spec.md` |
| 实测 tokens | **65993** (目标 ≤60K, 接受窗口 ≤66K, 余量 7) |
| 压缩率 | 64.3% (184943 → 65993) |
| 幂等 | PASS |
| 63/63 `## DOM —` | PASS |
| 63/63 `### Cross References` | PASS |
| 63/63 `### Specification` | PASS |
| 63/63 `<!-- source: -->` | PASS |
| 1917/1917 变量 | PASS |

### 7 列表格 + Smart Notes

| # | Name | Label | Type | Role | Core | CT | Notes |

**Smart Notes 保留规则**（8 类信号，每 cell ≤60 字符）:
- `See §X.Y` 反向章节路由
- `derived from VAR1, VAR2`
- `Required when <cond>` (本次无命中, 保留为未来)
- `ISO 8601|3166|4217|639` 标准引用
- `Ex: "Value1"` (第一个示例)
- `Vals: Y and N` 枚举
- `sponsor-defined`
- `not allowed/submitted`

### Notes 非空分布（563/1917 = 29.4%）

| 信号 | 命中数 |
|-----|-------:|
| Ex: | 379 |
| ISO 8601/3166/4217/639 | 183 |
| sponsor-defined | 56 |
| derived from | 32 |
| See §X.Y | 29 |
| Vals: | 12 |
| Req when | 1 |

## 4. 复核结果

### Attempt 2 Reviewer 独立抽样 10 变量

| 变量 | 期望 | 实际 | 判定 |
|------|-----|------|:-:|
| AGE | 是 | `derived from RFSTDTC and BRTHDTC` | PASS |
| VSPOS | 是 | `Ex: "SUPINE"` | PART (1 项) |
| AESER | 是 | `Vals: "Y" and "N"` | PASS |
| AEENRF | 是 | `See §4.4.7` | PASS |
| COUNTRY | 是 | `ISO 3166-1` (修补后) | **PASS** (修补前 FAIL) |
| AETERM/AEDECOD/RACE/STUDYID | 否 | (空) | PASS |
| LBTEST | 可选 | `Ex: "Alanine Aminot…"` | OK |

Reviewer 确认 1917/1917 变量、63/63 结构、mtime 时间戳、只读、Level 4 fallback 机制就绪。

## 5. 偏差与处理

| 偏差 | 严重度 | 处理 |
|-----|-------|------|
| COUNTRY ISO 3166 漏 (attempt 2 reviewer 发现) | 中 | **已修 patch**: RE_SN_ISO 扩展匹配 8601/3166/4217/639 |
| VSPOS 只保留 1 个 Example | 低 | 设计选择（字符预算硬约束）；用户可查源 |
| Token 余量仅 7 (0.01%) | **高** | 记录 tech debt: 未来源扩展会静默触发 L4 回退，需加告警 |
| L4 fallback 静默触发 | 中 | 记录 TODO: failures/step_06_fallback.md 告警机制 |

## 6. Checkpoint（§7.7）

- §7.7 要求: 是
- 原汇报内容: Mega Spec token + 抽样 1-2 个域
- Attempt 1 CONDITIONAL_PASS → 用户决策重试混合方案
- Attempt 2 + patch 后 PASS → 用户预授权 auto-continue
- Checkpoint 归档: (集成到本文件, attempt 1 存 failures/)

## 7. 累计指标

- 总 token 进度: **145,056 / 195,000 (74.4%)**
  - 01_index: 1,562
  - 02_chapters: 44,874
  - 03_model: 17,689
  - 04_variable_index: 14,938
  - 05_mega_spec: 65,993
- 本 Step subagent: 5 (2 executor + 2 reviewer + 1 patcher)
- 本 Step 重试: 1 (attempt 2 替换 attempt 1)
- Phase A+B 累计 subagent: 14, 重试 1

## 8. 下一步

- Step 7+8+9 可**并行** (§7.5 规定)
  - Step 7: `compress_assumptions.py` 53708 → ≤20K
  - Step 8: `catalog_examples.py` 219814 → ≤10K
  - Step 9: `catalog_terminology.py` 1944449 → ≤15K (⚠️ 99% 压缩, §7.7 checkpoint)
- 剩余预算: **49,944 tokens** (Step 7+8+9+11 目标合 50K, 零余量, 需严控)
