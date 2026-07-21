# Q4 — AESEV 三档 vs CTCAE Grade 映射

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef02-7ca8-83a4-b352-9e61c631d90c

## 原题

SDTMIG v3.4 中, AE 域的 AESEV (Severity) 变量有几档取值? 和肿瘤试验常用的 CTCAE Grade 1-5 如何对应? 如果 EDC 里只收到 Investigator 填的 CTCAE Grade, AESEV 该怎么填? Grade 5 对应什么特殊处理?

## ChatGPT 答案

**结论先说**：AE.AESEV 只有 3 档：**MILD / MODERATE / SEVERE**。它不是 CTCAE 的 1-5 级原样承载字段。CDISC 的 AE 术语里，AESEV 的同义映射只覆盖 Grade 1、2、3；而 Grade 5 是放在 AEOUT = FATAL 这个结局术语里，不在 AESEV 里。

**可操作地说，常见处理是：**

| Investigator CTCAE Grade | AESEV |
|---|---|
| Grade 1 | MILD |
| Grade 2 | MODERATE |
| Grade 3 | SEVERE |
| Grade 4 | SEVERE |
| Grade 5 | 不靠 AESEV 表达；关键是 AEOUT=FATAL |

**为什么这样**

CDISC AE 术语表里：
- Severity/Intensity Scale for Adverse Events (C66769) 只有：MILD（同义：1, Grade 1）、MODERATE（同义：2, Grade 2）、SEVERE（同义：3, Grade 3）
- Outcome of Event (C66768) 里有：FATAL（同义：5, Grade 5）

## PASS 判据自检

- [x] AESEV 三档: MILD / MODERATE / SEVERE ✓
- [x] Grade 1 → MILD; Grade 2 → MODERATE; Grade 3 → SEVERE ✓
- [x] Grade 4 → SEVERE ✓
- [x] Grade 5 特殊处理 ✓ (AEOUT=FATAL, 比 PASS 判据的 "AESDTH=Y" 更精确 — FATAL 是 AEOUT 术语的 NCI C66768 同义)
- [x] 说明 AESEV (严重性) 与 AESER (是否 Serious) 不是一回事 — 隐含在"不是 CTCAE 的 1-5 级原样承载字段"的论述里, 但未显式对比 AESER

**加分**: 引用 NCI CT Code C66769 (Severity Scale) 和 C66768 (Outcome) 精确定位.

## Verdict: **PASS**

核心判据全中, 且 Grade 5 处理答得**比 PASS 判据预期更精确** (指出 AEOUT=FATAL 而非 AESDTH=Y). AESEV vs AESER 区分隐含表达. 是 5 题里**最强的一题**, 有明确 NCI Code 溯源.
