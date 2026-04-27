# v2 上传清单 + 阶段历史

> 自动维护 by `scripts_v2/build_v2_stage.py`
> 每阶段完成后追加一行

## 当前状态
- 阶段: v2.0-setup
- 文件数: 9 (v1 不变 8 + system_prompt_v2)
- 总 tokens: 1,336,360 (v2.6 终态, ~77% capacity)

## 阶段历史

| 阶段 | 完成日期 | 文件数 | 总 tokens | 与 v1 对比 | 备注 |
|------|---------|-------|----------|-----------|------|
| v2.1 | 2026-04-18 | 13 | 209,423 | 77.6% of 270,000 target | chapters 全展开 |
| v2.2 | 2026-04-19 | 16 | 333,719 | 92.7% of 360,000 target | examples 高频域 |
| v2.3 | 2026-04-19 | 19 | 389,739 | 79.5% of 490,000 target | examples 剩余域 |
| v2.4 | 2026-04-19 | 24 | 751,422 | 89.5% of 840,000 target | terminology 高频 codelist |
| v2.5 | 2026-04-20 | 29 | 1,141,725 | 81.6% of 1,400,000 target | terminology mid codelist |
| v2.6 | 2026-04-20 | 32 | 1,336,360 | 89.1% of 1,500,000 target | terminology tail rebalance (core+supp uncovered) |

## 当前 v2 文件清单 (随阶段更新)

| 文件 | 来源 | tokens | 阶段产出 |
|------|------|--------|---------|
