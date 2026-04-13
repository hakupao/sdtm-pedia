# 质量问题记录

> 提取和验证过程中发现的所有问题与人工复核结论。

## 统计

| 类型 | 数量 |
|------|------|
| 内容缺失（漏段/漏条目） | 0 |
| 内容错误（错字/数据错误） | 0 |
| 格式问题（编号/表格/层级） | 0 |
| 截断问题（文件末尾不完整） | 0 |
| 工具误报 / 可接受差异 | 11 |
| **确认需返工问题** | **0** |

## 2026-04-13 Phase 3 定向人工复核

> 本轮针对当前脚本仍然标红的 domain 做 PDF vs Markdown 人工核对。结论：**未发现需要返工的真实内容缺失或数据错误**，剩余均为共享示例、摘要化表达、页码边界或 special-purpose prose 导致的工具误报/可接受差异。

| Domain | 文件 | 脚本信号 | 人工结论 | 结论类型 |
|---|---|---|---|---|
| RELREC | assumptions.md | anchor recall / similarity 低 | PDF 原文是 section prose，没有标准“Assumptions”列表；Markdown 对同一内容做了结构化重写并保留核心规则（RELID、IDVAR、--SEQ/--GRPID、peer vs dataset relationship） | 工具误报 |
| SUPPQUAL | assumptions.md | numbered-item loss / similarity 低 | `page_index` 的 assumptions 范围从中段开始，未完整覆盖整个 prose section；Markdown 保留了核心 SUPP-- 规则与 “When Not to Use” 内容，非真实缺失 | 工具误报（边界问题） |
| EC | examples.md | low text similarity | EC/EX 为共享 examples；EC 文件只保留 EC 侧数据与说明。PDF shared section中还包含 EX/RELREC 等内容，因此相似度偏低属预期 | 可接受差异 |
| MS | examples.md | low text similarity | MB/MS 为共享 examples；MS 文件按设计只保留 MS 侧数据，PDF 页面同时包含 MB narrative 与跨域联动内容 | 可接受差异 |
| PC | examples.md | low key-token recall | PC/PP shared section 很长，PC 文件采用“代表性表格摘要 + RELREC 方法说明”的压缩写法；主数据集 `pc.xpt` 与关键 RELREC 方法仍在 | 可接受差异（摘要化） |
| PP | examples.md | low text similarity | PP 文件保留了 `pp.xpt`、`supppp.xpt` 及 shared RELREC 方法说明，但没有逐字复写整段 shared section，属于有意压缩 | 可接受差异（摘要化） |
| RELSPEC | examples.md | low key-token recall | PDF example 只给 specimen lineage 图与 `relspec.xpt`；Markdown 以 ASCII 图 + `relspec.xpt` 表达同一信息，关键 lineage 关系保留 | 可接受差异 |
| RELSUB | examples.md | low key-token recall / similarity 低 | PDF 该页顶部仍是 specification/assumptions 尾部，example 位于下半页；Markdown 已完整保留 hemophilia twins 示例与 `relsub.xpt` 表 | 工具误报（页内混杂） |
| SS | examples.md | low key-token recall / similarity 低 | SDTMIG v3.4 的 SS examples 实际没有具体 dataset example；Markdown 明确写了 “does not include specific dataset examples” 的说明，符合源文件现状 | 可接受差异 |
| TR | examples.md | low text similarity | TU/TR 为共享 examples；TR 文件从 “Example 2 (continued from TU)” 开始，原因是 Example 1 属 TU 侧识别场景，TR 只保留 TR 侧 measurement/result 内容 | 可接受差异 |
| TU | examples.md | low text similarity | 共享 TU/TR section 中 PDF 页面前半仍带 TR assumptions 尾部；Markdown 中 TU 侧 3 个 example、`tu.xpt` 与 `supptu.xpt` 数据完整，低相似度主要由页码混杂与 shared section 造成 | 工具误报 / 可接受差异 |

## 当前结论

- **未确认任何 Phase 3 真实内容缺失或数据错误**
- 当前剩余 flagged domains 已人工解释
- 如后续要继续降低脚本噪音，可考虑：
  1. 对 shared-example domain 增加白名单/弱化 similarity 阈值
  2. 修正 `page_index.json` 中个别 special-purpose section 的 assumptions/examples 边界
  3. 对“摘要化表格” domain（如 PC/PP）增加 summary-mode 识别
