# Stage v2.2 Audit (规则 A 终态汇总 + A/B 结果归档)

> 日期: 2026-04-19
> 入口: Stage v2.1 ack continue → D1/D2/D3/D4
> 决议: **全 PASS → 继续 Task E1 (批 3 examples 剩余域)**

## 1. 上传清单 (真实, 不含 meta)

| # | 文件 | tokens | 源头 |
|---|-----|--------|-----|
| 1 | 00_routing.md | 2,657 | v1 不变 |
| 2 | 01_index.md | 1,562 | v1 不变 |
| 3 | 02_chapters.md | 60,716 | v2.1 全展开 |
| 4 | 03_model.md | 17,689 | v1 不变 |
| 5 | 04_variable_index.md | 14,938 | v1 不变 |
| 6 | 05_mega_spec.md | 65,993 | v1 不变 |
| 7 | 06_assumptions.md | 17,509 | v1 不变 |
| 8 | 07_examples_catalog.md | 4,295 | v1 不变 |
| 9 | 08_terminology_map.md | 20,536 | v1 不变 |
| 10 | **09_examples_data_high.md** | **112,697** | **v2.2 新 (28 高频域 examples 数据表)** |
| - | **合计** | **318,592** | **v2.2 终态** |

## 2. 规则 A 语义抽检汇总 (D2)

**10 域抽样, 不重叠**:
- Reviewer (opus a8e30db898b29a64c): DM, DS, EX, PC, IS → 5/5 PASS
- 主控 (opus 本 session): AE, PP, MB, GF, CP → 5/5 PASS

**方法**: 源 `^## Example` 数量 + `^\|` 总行数 + `^\|---` 分隔符数 → 与产出对应域段逐一对齐.

**结果**:
| 域 | 源 Ex / 产出 Ex | 源 `\|` / 产出 `\|` | 源 `\|---\|` / 产出 `\|---\|` | 审方 |
|---|----------------|--------------------|------------------------------|-----|
| DM | 7/7 | verbatim | verbatim | Reviewer |
| DS | 11/11 | verbatim | verbatim | Reviewer |
| EX | 8/8 | verbatim (Ex6 EC 24×21 + EX 8×18) | verbatim | Reviewer |
| PC | 1 ##/多 ### (源结构 outlier) | 32×28 pc.xpt 逐行 + 15 relrec | verbatim | Reviewer |
| IS | 11/11 (Ex10 ISGRPID `1a/1b` + Ex11 双 suppis) | verbatim | verbatim | Reviewer |
| AE | 6/6 | 30/30 | 6/6 | 主控 |
| PP | 3/3 | 76/76 | 5/5 | 主控 |
| MB | 3/3 | 78/78 | 11/11 | 主控 |
| GF | 5/5 | 67/67 | 10/10 | 主控 |
| CP | 9/9 | 24/24 | 2/2 | 主控 |

**结论**: 10/10 PASS, 零表格丢失 / 零 Example 丢失. 规则 A 合格.

## 3. Spec Deviation 处置 (token 硬 cap)

- spec 硬 cap: 50,000 tokens
- 实际产出: 112,697 tokens (2.25×)
- 用户决策 (2026-04-19 07:01Z): **Option A 接受** — 理由: v2.1 先例 (02_chapters 60K, 05_mega_spec 66K 均超 design target), 总 RAG 容量 ~3-4M, 112K = 3.2% 单文件占比
- Evidence: `trace.jsonl event=spec_deviation_ack`

## 4. A/B 测试 (D4 Checkpoint)

| 题 | 类型 | 精度 vs v2.1 | PASS? |
|----|-----|-------------|------|
| T13 | 批 2 新 (DM Ex1) | ↑ | **PASS** (6×25 dm.xpt 完整) |
| T14 | 批 2 新 (EX 剂量调整) | ↑ | **PASS** (Ex4 6×14 ex.xpt + EXADJ free-text) |
| T1 | 回归 (AEDECOD Core) | 持平 (略 ↑) | — |
| T11 | 回归 (ch08 §8.3 RELREC) | 持平 (略 ↑) | — |

- 回归衰减 ↓: **0 / 2** (门槛: ≥2 停, ≥1 询问, 本批 0 → 自动进)
- 新增 PASS: **2 / 2**
- Capacity: **20%** (v2.1 13% + 7pp, 精确匹配 20-22% 规划)
- 决策分支 (CHECKPOINT_V2.2_HANDOFF §决策矩阵): "T1/T11 无 ↓ + T13+T14 ≥1 PASS → 继续 Task E1"

## 5. 关键观察 (RAG 质量 vs 规模)

1. **Examples 查询优先级规则生效**: T13/T14 Instructions 里 `09 > 07` 优先级被 Claude 正确解读, 答案均标 Source=09, 无一 fallback 到旧路径模板
2. **挤出/遮蔽 0 观察**: 112K 新文件未对 05_mega_spec (T1) / 02_chapters (T11) 的召回产生竞争, v2.1 答案结构完整保留
3. **容量模型线性**: v1 12% (192K) → v2.1 13% (205.9K) 子线性 → v2.2 20% (318.6K) 近线性. 每 +100K ≈ +6-7pp (据此推算 v2.3 +200K 剩余域 → ~32-34%, v2.4 +400K 高频 codelist → ~56-60%)

## 6. Tech Debt (E1 考虑)

- PC/PP 源内部使用 `## Example 1 + 多层 ###` 的非标准嵌套, 通用 extractor 丢失 Method A-D 分层 traceability. 建议 E1 批 3 时**不处理 PC/PP** (已在 D2 批 2 覆盖), 仅处理其余 35 域, 并考虑未来 dedicated PC/PP extractor 恢复 Method 标签

## 7. 下一步

- [x] D4 A/B PASS 归档
- [ ] 进 Task E1: 准备 exclude-list (D1 的 28 域), 跑 `extract_examples_data.py --tier others` 产出 10_examples_data_others.md
- [ ] E1 后同样 executor 已在 (脚本已写 tier=others 分支), 只需主控抽样 + reviewer (可跳? 因为脚本未变, 走"复用脚本审"快路径)
