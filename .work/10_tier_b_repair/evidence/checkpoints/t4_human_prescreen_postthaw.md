# T4.2 抽样第 6-9 条 解冻后复筛

> 性质: AI 预筛 (general-purpose, opus, 新实例), 非人工判定; 对象 = 解冻后工作树 KB; 日期 2026-11-27
> 范围: `t4_human_sample.md` 第 6、7、8、9 条 (包内 KB 摘录为解冻前, 本次按工作树 `knowledge_base/domains/CE/examples.md` 现文判).
> 符号口径: S-TYPO 口径 A (按渲染外观). p152 文本层为字母 `o`, 渲染页为小圆圈, 与 KB `○` 一致; p153 文本层/渲染页均为 `○`/`□`.

| # | atom_id | 层 | 终态 | 预筛 | 理由 | 依据 |
|--:|---|---|---|---|---|---|
| 6 | `ig34_p0152_a0006` | REWRITE_OK | EQUIVALENT | 内容正确 | 原子为 Nausea 行 Severity 第 3 项 "o Severe"; KB Nausea 行 Severity 列为 "○ Mild ○ Moderate ○ Severe", 选项、顺序、符号与渲染页一致. 多行单元格压成一行属版式改写, 信息无损. | 渲染页 p152 CRF 表 Nausea 行; `knowledge_base/domains/CE/examples.md:43` |
| 7 | `ig34_p0152_a0009` | REWRITE_OK | EQUIVALENT | 内容正确 | 原子为 Vomit 行 "o Severe" (包内自动定位落在 Nausea 行, 偏一行); KB Vomit 行 Severity 为 "○ Mild ○ Moderate ○ Severe", 与渲染页一致. | 渲染页 p152 CRF 表 Vomit 行; `knowledge_base/domains/CE/examples.md:44` |
| 8 | `ig34_p0152_a0010` | REWRITE_OK | EQUIVALENT | 内容正确 | Diarrhea 行: "○ Yes ○ No"、两列日期 "__/___/____ (dd/mmm/yyyy)"、Severity "○ Mild ○ Moderate ○ Severe", 全部与渲染页一致; 日期下划线分组 (2/3/4) 与 PDF 相同. | 渲染页 p152 CRF 表 Diarrhea 行; `knowledge_base/domains/CE/examples.md:45` |
| 9 | `ig34_p0153_a0008` | REWRITE_OK | EQUIVALENT | 内容正确 | "How did fracture occur?" 选项 "○ Pathologic ○ Fall ○ Other trauma ○ Unknown", 含原子 "Other trauma", 顺序与符号 (○ 单选) 与渲染页一致. | 渲染页 p153 Bone Fracture Assessment 表; `knowledge_base/domains/CE/examples.md:77` |

计数: 内容正确 4 / 内容错误 0 / 看不出 0.

## 样本外观察 (不计入判定)

- 解冻 diff 同时把 `examples.md:39` 小标题 "CRF: CE Example 2 — Clinical Events with Severity" 改为 "CRF", 与 p152 渲染页标签 "CRF" 一致 (原标题副名非 PDF 原文).
- `examples.md:70` 仍为 "CRF: CE Example 3 — Bone Fracture Assessment"; p153 渲染页表头单元格为 "Bone Fracture Assessment", 无 "CRF: CE Example 3" 字样. 与 Example 2 处理口径不一致, 供主控确认 (不影响第 9 条判定).
- `examples.md:81`/`:83` 多选项 `□` 与 p153 渲染页 `□` 一致; 单选项 `○` 一致.
