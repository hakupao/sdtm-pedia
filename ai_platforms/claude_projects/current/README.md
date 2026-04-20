# current/ — v2.6 终态可部署产物

> 这是当前的"可用版", 里面的 19 个文件是 Claude Project 应上传的最终内容.
> 上游设计与历史见 [../docs/](../docs/), 开发过程见 [../dev/](../dev/).

## 部署步骤

1. **创建 Claude Project** (或打开已有 v2 Project)
2. **粘贴 System Prompt**: 把 [system_prompt.md](system_prompt.md) 的完整内容粘到 Project 的 "Custom instructions" 框
3. **上传 Knowledge**: 把 [uploads/](uploads/) 下全部 19 个 `.md` 文件**全选** → 拖到 Project Knowledge 面板
4. **等 Indexing**: UI indicator 可能持续显示 "Indexing" 超过 30-60 分钟, **但不必等** — 直接试问即可命中 (见历史经验 [../docs/rag_decay_curve.md](../docs/rag_decay_curve.md) §2.5 观察)
5. **验证** (可选 smoke test): 跑 [../dev/test_results.md](../dev/test_results.md) 里的 T1/T17/T22 三题, 确认 answer 与矩阵记录一致

## 上传清单 (19 文件, 1,286,161 tokens, capacity 77%)

| # | 文件 | Tokens | Tier | 批次 | 源 |
|---|------|-------:|------|------|---|
| 00 | routing.md | — | 导航 | v2.1 | v2.1 重建 |
| 01 | index.md | — | 导航 | v2.1 | v2.1 重建 |
| 02 | chapters.md | — | 规则推理 | v2.1 | byte-exact expand from `knowledge_base/chapters/` |
| 03 | model.md | — | 规则推理 | v2.1 | v2.1 重建 |
| 04 | variable_index.md | — | 变量反向索引 | v2.1 | v2.1 重建 |
| 05 | mega_spec.md | — | spec 表 | v2.1 | v2.1 重建 |
| 06 | assumptions.md | — | 业务规则 | v2.1 | v2.1 重建 |
| 07 | examples_catalog.md | — | examples 目录 | v2.1 | v2.1 重建 |
| 08 | terminology_map.md | — | CT 映射 | v2.1 | v2.1 重建 |
| 09 | examples_data_high.md | 112,697 | examples 数据 | v2.2 | 高频 28 域 |
| 10 | examples_data_others.md | 48,897 | examples 数据 | v2.3 | 其余 35 域 (63 域 100% 覆盖) |
| 11a | terminology_high_core.md | 68,559 | CT 完整 Term | v2.4 | top 200 core |
| 11b | terminology_high_questionnaires.md | 256,336 | CT 完整 Term | v2.4 | top 200 QRS |
| 11c | terminology_high_supp.md | 26,857 | CT 完整 Term | v2.4 | top 200 supp |
| 12a | terminology_mid_core.md | 129,963 | CT 中频 | v2.5 | rank 201-500 core |
| 12b | terminology_mid_questionnaires.md | 224,659 | CT 中频 | v2.5 | rank 201-500 QRS |
| 12c | terminology_mid_supp.md | 23,317 | CT 中频 | v2.5 | rank 201-500 supp |
| 13a | terminology_tail_core.md | 145,787 | tail (含 6 giants stub) | v2.6 | rank 501+ core 全量 |
| 13c | terminology_tail_supp.md | 43,194 | tail | v2.6 | rank 501+ supp 全量 |

**注**: 13b (terminology tail questionnaires) **by design 不存在** — quest 是用户最低优先级, tail 批未扩容, 保持 v2.5 的 55.8% 覆盖, 长尾 296 条归 Phase 7 RAG.

## 元信息

- [system_prompt.md](system_prompt.md) — Project Instructions, 含 stage v2.1-v2.6 累积 prompt 段 + CT 查询优先级 `11*>12*>13*>08`
- [upload_manifest.md](upload_manifest.md) — 各 stage token 统计 + C12 hard cap 实测

## 常见问题

**Q: 如果 Claude Project capacity 提示超限怎么办?**
A: UI 显示 77% 是正常; paid 套餐 RAG 会自动分片. 如果真超, 优先移除 11b (256K, 最大单文件) 试试, 其次 12b (224K). 见 [../docs/capacity_research.md](../docs/capacity_research.md).

**Q: 能不能只上传部分?**
A: 不建议. T1-T22 + 2 优先级验证的 24/24 PASS 是 19 文件全上的基线. 少文件会恢复到 v2.1/v2.4 中间状态 (仍能用, 但功能退化).

**Q: v2.6 之后还会扩容吗?**
A: 默认不. 见 [../ROADMAP.md](../ROADMAP.md) 后续可选扩展段. 想推高到 85-90% capacity 或补 quest 覆盖到 80% 需新开批次.

---

*更新: 2026-04-20 晚 reorg.*
