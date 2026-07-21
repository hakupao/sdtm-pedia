# Sanity Q2 — LBNRIND submission values

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e82e25-7a7c-83a4-9db1-87959c963522
> 提交时间: 2026-04-22
> 题: LBNRIND 的 submission values 有哪些?
> 期望: HIGH / LOW / NORMAL / ABNORMAL (C78736)
> Verdict: **PASS**

## 完整回答

LBNRIND 的 submission values 是这 4 个：
- ABNORMAL
- HIGH
- LOW
- NORMAL

依据：
- LB.LBNRIND 的 Controlled Terms 是 C78736，变量注释里也给了示例值 "NORMAL", "ABNORMAL", "HIGH", "LOW"。
- 术语表中 Reference Range Indicator (C78736) 的 CDISC Submission Value 明确列出上述 4 个值，且该 codelist 是 Extensible: Yes。

补充一点：LBNRIND 用来表示结果相对参考范围的位置，不用于表示临床意义（clinical significance）。

源溯源:
- `<!-- source: knowledge_base/domains/LB/spec.md -->`
- `<!-- source: knowledge_base/terminology/core/general_part4.md -->`

## 判据

- 4 个全字符值 (HIGH/LOW/NORMAL/ABNORMAL) ✓
- C78736 显式给出 ✓
- Extensible: Yes 标记正确 ✓
- 解释 NRIND vs CSTAT (临床意义) 边界 ✓

PASS — v5 CO-2 subclause 未被改, 底座未回归
