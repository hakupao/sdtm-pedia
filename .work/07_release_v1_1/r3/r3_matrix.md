# SMOKE_V4 R3 — Cross-Platform Matrix (17 × 4 = 68 cells)

> 跑题后填. 单元格格式: `PASS` / `PASS+` / `PARTIAL` / `FAIL` / `PUNT` / `—` (未跑)
> 详细每题 verdict 见 `evidence/<platform>/q<NN>.md`

| # | 题 (1 行简述) | Claude v2.6 | ChatGPT v2.2 | Gemini v7.1 | NotebookLM v2 | R1 基线 (对比) |
|:-:|---|:--:|:--:|:--:|:--:|---|
| Q1  | GF 域变量拼写 (GFINHERT) + Core | — | — | — | — | C:PASS / G:FAIL / Cgt:Q1拼写 R1 / N:PASS |
| Q2  | CP 细胞表型 (CPCSMRKS 等) | — | — | — | — | C:PASS / G:PASS / Cgt:PASS / N:PASS |
| Q3  | DM ARMCD/ACTARMCD Core | — | — | — | — | C:PASS / G:PASS / Cgt:PASS / N:PASS |
| Q4  | 微生物多场景 (IS/MB/CP) | — | — | — | — | C:PASS / G:PARTIAL→PASS R2 / Cgt:PASS / N:PASS |
| Q5  | 多场景归域 (FA/QS/CE) | — | — | — | — | C:PASS / G:PASS / Cgt:PASS / N:PASS |
| Q6  | PK 时间窗 PCTPT/PCTPTREF | — | — | — | — | C:PASS / G:PASS / Cgt:PASS / N:PASS |
| Q7  | DTC imputation | — | — | — | — | C:PASS / G:PASS / Cgt:PASS / N:PASS |
| Q8  | AE / SUPP-- 边界 | — | — | — | — | C:PASS / G:PASS / Cgt:PASS+ / N:PASS+ |
| Q9  | Pinnacle 21 错误分类 | — | — | — | — | C:PASS / G:PASS / Cgt:PASS / N:PARTIAL |
| Q10 | SUPPTS 前提纠错 (AHP) | — | — | — | — | C:PASS / G:PARTIAL→PASS R2 / Cgt:PASS+ / N:PASS+ |
| Q11 | 罕见 codelist | — | — | — | — | C:PASS / G:PASS / Cgt:PASS / N:PUNT (bonus) |
| Q12 | TI/TE Trial Design | — | — | — | — | C:PASS / G:PASS / Cgt:PASS / N:PUNT (bonus) |
| Q13 | ARMCD null (observational) | — | — | — | — | C:PASS / G:FAIL R1→PASS R2 / Cgt:PASS / N:PASS |
| Q14 | RELREC 选择 (AE↔CM) | — | — | — | — | C:PASS / G:PASS / Cgt:PASS / N:PASS |
| AHP1 | NSV attention gap | — | — | — | — | C:PASS / G:FAIL R1→PASS R2 / Cgt:PASS / N:PASS |
| AHP2 | 虚构 LBNRIND | — | — | — | — | C:PASS / G:FAIL R1→PASS R2 / Cgt:PASS / N:PASS |
| AHP3 | AEDECOD MedDRA 边界 | — | — | — | — | C:PASS / G:FAIL R1→PASS R2 / Cgt:PASS+ / N:PASS |

**汇总** (R3 跑完后):

| 平台 | R3 PASS 计数 | R3 总分 | R1 基线分 | R3 vs R1 delta | Gate (R3 ≥ R1?) |
|------|:-:|:-:|:-:|:-:|:-:|
| Claude v2.6 | — | — | 17/17 | — | — |
| ChatGPT v2.2 | — | — | 16.5/17 | — | — |
| Gemini v7.1 | — | — | 16/17 (R2 post-v6-A1) | — | — |
| NotebookLM v2 | — | — | 15/17 | — | — |

**R3 通过判定**: 4 平台 R3 ≥ R1 基线 (允许 ±1 噪声) + 06 修复涉及的 Q (PC RELREC / TA / DI) 期望持平或提升, 无回归.
