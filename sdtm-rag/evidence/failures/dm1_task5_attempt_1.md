# DM1 T5 attempt 1 — 域码扩写 label+structure: CDISC 140q 回归 1 题, 映射集零收益

> 日期: 2026-09-15 / 单元: DM1 Task 5 (D3 域码确定性扩写) / 判定: **FAIL, 不提交**

## 1. 输入 (这一 attempt 试的是什么)

`server/domain_expand.py::DomainExpander.expand()` 按 Task 5 brief 原样实现:
问句里认出的域码 (≤3 个, 复用 `StructuredLookup._query_domains`) 追加该域 meta.yaml 的
`label` **与** `structure`, 形如 `<原句> Disposition (One record per disposition status or
protocol milestone per subject)`。扩写文本只喂稠密 embedding / `_search` / `_bm25_search`;
S1/S2 直查通道与 LLM 恒收原句。

复跑 (本 attempt 的代码已被 attempt 2 覆盖, 复跑需把 `expand()` 的 `parts.append` 一行
改回 `f"{label} ({structure})" if structure else label`):

```
.venv/bin/python -m eval.run_eval eval/test_set_v3.yml --retrieval-only --hybrid \
  --structured-lookup --output eval/runs/dm1_cdisc_t5.json
```

## 2. 产物 / 三闸数字

| 闸 | before | attempt 1 | worse | better |
|---|---|---|---|---|
| CDISC 140q (`eval/runs/dm1_cdisc_before.json`) | 99.17% | 98.81% | **`['q47']`** | `[]` |
| study 48q (`data/study/st01/eval/runs/dm1_study_before.json`) | 87.5% | 87.5% | `[]` | `[]` |
| 映射 8q (`data/study/st01/eval/runs/dm1_mapping_t4.json`) | 20.0% | 20.0% | `[]` | `[]` |

⚠ **勘误 (2026-09-15)**: 本表 study 48q 一行原写 88.24%, 错。88.24% 是拿逐题对比脚本对 51 条 results **全部**求平均得到的, 而题集含 3 条 `out_of_scope`; 报告口径取`summary.source_recall_avg` = 计分的 48 题 = **87.5%**。worse/better 判据不受影响 (那 3 条两臂逐位相同)。

## 3. 技术判定: 为什么 q47 掉

q47 = `How do QS (Questionnaires) domains handle instrument-specific variables using QSCAT,
and what role does QSTESTCD play in organizing question-level data?`, gold 两条
(`domains/QS/spec.md` + `domains/QS/assumptions.md`), before 两条全中 (recall 1.0)。

扩写追加 `Questionnaires (One record per questionnaire per question per time point per
visit per subject)`。实测 `domains/QS/assumptions.md` 在 top-15 里的位次:

```
OFF  rank 9  (另在 rank 15 再出现一次)
ON   不在 top-15
```

被顶上来的是 `domains/AE/assumptions.md` / `domains/PC/assumptions.md` /
`chapters/ch03_submitting_data.md` —— 都是 "One record per ... per subject" 这类**记录
粒度**行文密集的块。structure 字段本身就是这句式的模板, 追加它等于往问句里灌一段
**跨域通用**的散文, 稠密与 BM25 两侧同时把"讲记录粒度的块"整体上浮, 把问句真正问的
那条 (QS 自己的 assumptions) 挤出 15 席。

附带证据: q47 的问句里**已经**写着 `(Questionnaires)`, 即 label 部分是纯重复; 掉分完全
由 structure 段贡献。

## 4. 业务判定: 这一 attempt 即使不回归也不该收

映射 8q (本单元的目标集) **一题都没动**, 8/8 停在 recall 0.2。逐题看 top5, 变化只发生在
第 5 位 (CDISC 侧尾巴的位次churn, 如 dm01 `chapters/ch02_fundamentals.md` →
`chapters/ch04_general_assumptions.md`), **没有任何一张 study 侧候选卡片进入任何一题的
top5**。

原因不在扩写强弱, 而在席位: 联邦 `--corpus both` 下 CDISC 引擎的 15 席被 S1 直查注入
(域 assumptions 定义席 + 3 条域 spec 行) 与域内 cosine 尾巴吃满; 映射题的 5 条 gold 里
4 条是 study 卡片, 它们要出现得先有席位。给 CDISC 侧的问句加英文散文不改变这一点 ——
D3 的作用面 (让 2 字母域码对 embedding/BM25 可见) 与本单元 gold 的缺口 (study 侧卡片
拿不到席位) **不是同一个问题**。

## 5. 下一 attempt 的输入

按 brief Step 5 的处置: 收窄成 **label only, no structure** (`parts.append(label)`), 重跑
同三闸。预期 q47 的扰动降到"一个已在问句中的词重复一次", 有机会过 `worse: []`;
但按 §4, 映射集大概率仍为 0 收益 —— 那属于 D3 的作用面问题, 不是本 attempt 的实现缺陷,
须在报告里如实上报而不是继续调扩写强度。
