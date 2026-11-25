# Q5 — FA vs QS vs CE 三场景 (Gemini Gems)

> **Chat**: fresh (`/gem/3b572e310813/b7104a862f527c04`)
> **采集时间**: 2026-04-22 晚
> **Verdict**: **PASS** (A=FA, B=QS, C=CE + 理由 + Topic 变量; 无 extended reasoning 暴露)

## A — 既往 MH DAS28 量化
- 域: **FA** (Findings About Events or Interventions)
- 理由: 评估是对某个 Event (MH) 的进一步发现/量化, 具与原始事件不同时间点 → FA
- Topic: FAOBJ="RHEUMATOID ARTHRITIS", FATEST="Disease Activity Score 28", FAORRES="4.2"

## B — SF-36 问卷
- 域: **QS** (Questionnaires)
- 理由: SF-36 是标准化量表/问卷; QS 专存受试者对问卷中具体问题的回答或得分 (每维度/每题一条记录)
- Topic: QSCAT="SF-36", QSTEST="Physical Functioning Score", QSORRES="85"

## C — 轻微头晕未达 AE
- 域: **CE** (Clinical Events)
- 理由: 属临床现象但不符 AE 报告标准; CE 记协议定义的感兴趣临床事件 或 不构成 AE 但仍收集的 signs/symptoms
- Topic: CETERM="DIZZINESS", CEOCCUR="Y", CECAT="SIGNS AND SYMPTOMS"

## Verdict
**PASS** — 3/3 场景对 + 理由 + Topic 变量. 回答简洁无 extended reasoning 暴露, 较 sanity 早期 verbose 好转. 未显式给 SDTMIG §8.6.3 锚点或 QRS 特定 Codelist 码 (不影响 PASS, 对比 NBLM Q5 Codelist C177716 的细节精度稍低).
