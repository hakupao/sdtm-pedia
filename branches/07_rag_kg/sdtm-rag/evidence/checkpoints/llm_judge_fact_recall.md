# 语义 LLM-judge fact recall — 替代 substring 误导值 (② 收口)

> 状态: **DONE** (2026-06-15) — v3 140q ON-arm 答案语义 fact recall = **93.9%** (vs substring 82.6%);
> 证实 substring 指标系统性低估 ~11pt。判 = 7-shard Workflow (sonnet) + 主 session Rule A 抽验校准。

## 动机

S4 full eval 的 substring fact recall = 82.6%, 但已知 substring 对 paraphrase / 同义 / 数字异形
("two-character" vs "2-character") / 表内值 结构性盲 → 这个数字会误导。本步用语义 LLM-judge 给一个
**可信** fact recall 数字。

## 方法

- 输入: `eval/prod_wirein/judge_input_v3.json` = 140q × {question, answer (v3 ON-arm 缓存全文), expected_facts}; 466 gold facts。**不重新生成答案**, 只判已有答案。
- judge: 7-shard Workflow (各 ~20q, model=sonnet), 逐 gold fact 判"答案是否以任意表面形式传达此事实"(语义非 substring); fact_recall = covered/total。Schema 强约束。
- 聚合: 按类别 + overall。
- 产物: `eval/prod_wirein/judge_result_v3.json` (全 140 judgment + uncovered_facts)。

## 结果

| 类别 | 语义 fact recall | (对比 substring) |
|------|-----------------|------------------|
| concept | 100% | — |
| cross_domain | 93.5% | — |
| mixed | 92.0% | — |
| single_domain | 91.7% | — |
| **overall** | **93.9%** | **82.6%** (低估 11.3pt) |

分布: 121/140 全覆盖 (fr=1.0), 6 题 ≥0.75, 10 题 0.5-0.75, 3 题 <0.5。**93.9% 落在用户 93-96% band 内。**

## Rule A 抽验校准 (主 session, 异于 judge)

判 judge 是否过松/过严, 抽极值:
- **q104 (judged fr=0)**: gold ['36','Planned Study Day of Visit']。实查答案: 找到 VISITDY 但 label 给成
  "Study Day of Start of Observation" (错) 且显式 punt 全域清单 → 两 gold 确未传达。**judge 正确** (真 miss,
  非假阴; 这是 VISITDY label 检索/答题 gap)。
- **q02 (judged fr=0.43)**: gold 7 Req 变量, 答案只列 STUDYID/DOMAIN/USUBJID (3/7), 漏 SUBJID/SITEID/SEX/
  COUNTRY → **judge 正确** (已知 q02 relocation 残留, prod_wirein 已记)。
- 多个 fr=1.0 抽看均为正确全覆盖。
→ judge 未过度给分 (q104/q02 该 0 该 0.43 都判对), 93.9% 可信。

## 真实残留 miss (judge 标 uncovered, 非假阴)

q104 (VISITDY label) / q133 (TU topic 变量误判, scientist 早判 NONDETERMINISM) / q02 (Req 枚举不全) /
q97 q99 q101 (mixed 具体枚举值漏) / s05 (Extensible 标志) 等 —— 均答题侧 / 检索覆盖个例, 非检索通道缺陷。

## 缺口 — ✅ 已固化 (2026-06-15)

语义 judge 已**固化进 `run_eval.py --judge`** (不再是一次性 Workflow): 逐 gold fact LLM 判
(`check_fact_recall_judge` + 纯解析器 `_parse_covered`), `--judge-model` 默认 deepseek 与答题模型
独立; 报告 substring (次) + judge (主), verdict 用 judge; 解析失败逐题回退 substring 且
`judge_parse_ok=False` 计数上报 (不静默)。Rule D code-reviewer 抓到并修了 HIGH (非 bool 列表元素
`bool(x)` 会把 array-of-objects/字符串裁决静默膨胀为全 covered → 类型守卫拒绝→计数回退) + 2 MED
(backoff 末次空睡/封顶 + judge_fact_hits 对称) + LOW (zip strict)。pytest 260 (新 `test_run_eval_judge`
含 HIGH 回归用例); 5q 集成 smoke 实证 (q119 substring 0→judge 100, parse_fail 0)。
单测 `scripts/tests/test_run_eval_judge.py`。**下次报 fact recall 一律用 `--judge`。**

## 改动文件
- `eval/prod_wirein/judge_input_v3.json` (judge 输入) + `judge_result_v3.json` (全判) ; 无源码改动
