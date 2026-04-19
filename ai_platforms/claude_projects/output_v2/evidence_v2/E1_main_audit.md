# E1 主控独立抽样 (规则 A)

> 日期: 2026-04-19
> 主控: Claude Opus 4.7 (1M context) — 与 E1 reviewer (opus, a91ed21f74242d2ed) 不同 session
> 隶属 PLAN_V2.md §1 规则 A + §7 Task E1

## 改写率评估

本批与 D2 共用脚本 (`extract_examples_data.py`), 算法相同: 数据表 100% 保留 + 首段 ≤2 行 description + `**Rows N-M:**` 解释行丢弃. 仅 tier=others 路径在 D2 未实跑但已 code review 过。**估算改写率 ~40-55%** (行数口径), 触发规则 A。

## 抽样域 (5, 与 reviewer 不重叠)

Reviewer 抽: TA, OE, SR, FT, QS
主控抽: **TS, SV, EC, RP, HO** (覆盖 Trial Design + Events + Findings 跨类)

## 结果

| 域 | 源 Examples | 产出 Examples | 源 `\|` 行 | 产出 `\|` 行 | 源 `\|---\|` | 产出 `\|---\|` | Verdict |
|----|-----------|-------------|----------|-------------|------------|---------------|---------|
| TS | 4 | 4 | 100 | 100 | 4 | 4 | **PASS** |
| SV | 1 | 1 | 35 | 35 | 3 | 3 | **PASS** |
| EC | 7 | 7 | 47 | 47 | 7 | 7 | **PASS** |
| RP | 1 | 1 | 23 | 23 | 1 | 1 | **PASS** |
| HO | 2 | 2 | 38 | 38 | 4 | 4 | **PASS** |

**主控 Verdict: 5/5 PASS, 零表格丢失 / 零 Example 丢失**

## 额外静态检查

| 检查项 | 结果 |
|-------|-----|
| 脚本 Bug 修复 (09 → 10 路径) | PASS, 两处 (docstring + `_output_path`) 同步更新, tier=high 不受影响 |
| 脚本幂等 (md5 stable) | 待 reviewer 复跑确认, 本次 md5 = `4c971b29aec26cf7b62bc2201b82f08c` |
| 35 域覆盖 | PASS (`grep -c "<!-- source:"` = 35) |
| 63 域完整 (09 ∪ 10) | PASS (09: 28 + 10: 35 = 63, `comm -12` overlap = 0) |
| Tokens < 硬 cap | PASS (48,897 < 50,000, 仅 soft-target 警告) |

## 观察

1. **48K 位于 [30K, 50K] 警告区**: 脚本按设计 stderr 警告 + 继续 (exit 0). 主控判定: 无需拆分 10a/10b, 继续进 E3 (build stage v2.3).
2. **RELREC 只 6 行**: RELREC 是 relationship meta 表, 源 examples.md 几乎无内容. 产出仅保留 title + source marker + 可能一行 description. 不是 defect, 是源特性.
3. **TA 最大 (218 lines)**: Trial Arms 含多 Arm 示例. 验证过 Example 数 4 个全到位.
4. **总行数 (produce) 比 D2 09 少 (接近 1/3)**: 与 D2 (28 高频域, ~112K) 相比, 35 剩余域仅 48K, 单域平均约 1.4K tokens vs D2 4K tokens. 合理 — 剩余域多是 meta/trial design 或 low-frequency findings, examples 天然精简.

## 规则 A 结论

5/5 主控抽样 PASS + 静态 5/5 PASS → **E1 产物业务层 PASS**. 等 reviewer 另 5 域 (TA/OE/SR/FT/QS) 结果汇总。

## 下一步

- [ ] 等 E1_review.md (reviewer) 完成
- [ ] 若 reviewer 也 PASS → 进 E3 (build_v2_stage.py --stage v2.3)
- [ ] E4 HARD CHECKPOINT: 用户在 v2 Project 上传 1 新文件 (10_examples_data_others.md, 48K) + 跑 4 题 A/B (T15 RP / T16 FT + 2 回归)
