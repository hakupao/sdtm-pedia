# Q5 — FA vs QS vs CE 三场景 (ChatGPT)

> **Chat**: fresh (`/c/69e8adbf-4cc4-83a4-8fe6-8c6a62874b39`)
> **采集时间**: 2026-04-22 晚
> **Verdict**: **PASS** (A=FA, B=QS, C=CE + 结论表 + 源溯源 + SDTMIG §8.6.3 精确引用)

## 结论表
| 场景 | 域 | 理由精要 | Topic 变量示例 |
|---|---|---|---|
| A | **FA** | 事件的测量/评估 → FA (事件本身放 MH/CE/AE). FA 与父记录只靠 FAOBJ 不够, 需 RELREC | FATESTCD="DAS28", FATEST="Disease Activity Score 28", FAOBJ="Rheumatoid Arthritis", FAORRES=4.2 |
| B | **QS** | SF-36 是命名问卷; QRS 共享假设: 量表名放 QSCAT, 题目放 QSTEST/QSTESTCD | QSTEST="Physical Functioning", QSCAT="SF-36", QSORRES 原始 / QSSTRESC/QSSTRESN 标准分 |
| C | **CE** | 协议定义为临床感兴趣但不作 AE 的事件; 可包括 disease-related signs/symptoms. 前提: 协议要求收集 | CETERM="DIZZINESS"; 自发报告时 CEPRESP/CEOCCUR 通常不填 |

## 补判断
- **A 为什么不是 CE?** 不是描述 RA 本身新发生, 而是对既往 MH 做 Visit 4 量化评估 → SDTMIG §8.6.3: 事件本身→Events, 事件测量→FA
- **C 为什么不是 AE?** 题目给前提 "未达 AE 报告阈值"; 若协议要求收集 → CE

## 源溯源 (ChatGPT 自列)
- A: FA/assumptions.md + AE/examples.md + ch08_relationships.md
- B: QS/assumptions.md + ch04_general_assumptions.md
- C: CE/assumptions.md + CE/spec.md + terminology/core/general_*.md

## Verdict
**PASS** — 3/3 场景对 + 结论表 + 源溯源 + 补判断 (A not CE / C not AE) + §8.6.3 精确锚点.
