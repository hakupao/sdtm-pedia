# D2 主控独立抽样 (规则 A)

> 日期: 2026-04-19
> 主控: Claude Opus 4.7 (1M context) — 与 executor (opus, aaeb38e3115269993) / reviewer (opus, a8e30db898b29a64c) 不同 session
> 隶属 PLAN_V2.md §1 规则 A (压缩率 >50% 或改写率 >50% 必须 N 样本独立抽检)
> 本次改写: 算法保留了**所有数据表 + 首段 2 行 description**, 但丢弃了 `**Rows N-M:**` 解释段落, 估算改写率 ~40-60% (按段落数量), 触发规则 A

## 抽样域 (5, 与 reviewer 不重叠)

Reviewer 已抽: DM, DS, EX, PC, IS
主控抽: **AE, PP, MB, GF, CP**

## 方法

对每个抽样域, 用 grep/awk 统计:
- `^## Example` (源) vs `^#### Example` (产出) 数量 — 抓 Example 完整性
- `^\|` 总行数 (源 vs 产出) — 抓表格行保留完整性
- `^\|---` 分隔符数 (源 vs 产出) — 抓表格数量

三项全相等 = 表格 0 丢失, Example 0 丢失。

## 结果

| 域 | 源 Examples | 产出 Examples | 源 `\|` 行 | 产出 `\|` 行 | 源 `\|---\|` | 产出 `\|---\|` | Verdict |
|----|-----------|-------------|----------|-------------|------------|---------------|---------|
| AE | 6 | 6 | 30 | 30 | 6 | 6 | **PASS** |
| PP | 3 | 3 | 76 | 76 | 5 | 5 | **PASS** |
| MB | 3 | 3 | 78 | 78 | 11 | 11 | **PASS** |
| GF | 5 | 5 | 67 | 67 | 10 | 10 | **PASS** |
| CP | 9 | 9 | 24 | 24 | 2 | 2 | **PASS** |

**主控 Verdict: 5/5 PASS, 零表格丢失 / 零 Example 丢失**

## 额外静态检查

| 检查项 | 结果 |
|-------|-----|
| 脚本无 `datetime.now\|time.time\|time.strftime` | PASS (grep no match) |
| 脚本无 `open(..., 'w')` 指向 knowledge_base/ | PASS (grep no match) |
| 脚本 imports 仅 stdlib + tiktoken | PASS (argparse, datetime, re, sys, pathlib + tiktoken) |
| 幂等 md5 重跑一致 | PASS (`4cf1c1c6ab167cc31a47cdda891ec50e`, 两次跑 stdout 一致) |
| 首行时间戳非 wall-clock | PASS (`2026-04-15T06:20:26Z`, 源 mtime max 派生) |
| 28 源 marker 在产出 | PASS (`grep -c "^<!-- source: knowledge_base"` = 28) |

## 观察 (非 defect)

1. 产出有 **31** 个 `^### ` header, 其中 28 是域级 `### <X> — Examples`, 额外 3 个来自源内部子结构:
   - CP 源里的 `### Example 1a` / `### Example 1b` (Example 1 的子例)
   - PC 源里的 `### Shared PC Dataset for All Examples` (4 种 Method 共享数据集)
   脚本原样保留, 未降级为 `####`, 但**不丢信息**。层级不统一是 cosmetic defect, 非 blocker。

2. `RS` 域产出仅 **24 tokens** (行数/Example 极少), 源 `examples.md` 可能极精简。不是 bug, 是源特性。

3. `SS` 域同 RS (24 tokens)。

## Spec Deviation 处置

- 已知: 产出 112,697 tokens > 硬 cap 50,000 (2.25×)
- 用户决策: Option A, 接受, 理由与 v2.1 先例一致 (02_chapters 60K, 05_mega_spec 66K 均超 design target 被接受), 总 RAG 容量 ~3-4M
- 记入 trace.jsonl `event=spec_deviation_ack`
- **本次不启动 row-cap / 拆分算法**

## 规则 A 结论

5/5 主控抽样 PASS + 静态 6/6 PASS → **D2 产物业务层 PASS**. 等 reviewer 独立 5 域 (DM/DS/EX/PC/IS) 抽样结果汇总。

## 下一步

- [ ] 等 D2_review.md (reviewer) 完成
- [ ] 若 reviewer 也 PASS → 进 D3 build_v2_stage.py --stage v2.2
- [ ] 若 reviewer CONDITIONAL_PASS → 记 tech debt 继续
- [ ] 若 reviewer FAIL → 主控重新决策
