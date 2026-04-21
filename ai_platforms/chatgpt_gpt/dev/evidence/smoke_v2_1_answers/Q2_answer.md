# Q2 — AE 升 SAE, 住院相关 Serious 子变量填写 (v2.1)

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e7377b-4c38-83a8-8394-16ddb3ce1477
**Date**: 2026-04-21
**Thought for**: 2m 5s

## 原题

一位受试者服药后出现严重皮疹并因此住院 3 天治疗. Investigator 判断为药物相关的严重不良事件. 请问 SDTM AE 域中, 该如何记录这条事件的严重性相关变量 (AESER 及其子变量)? 请列出需要填写的 SAE 判定类变量 (AESER / AESCONG / AESDISAB / AESHOSP / AESLIFE / AESDTH / AESMIE) 各自的含义和本例取值, "Y" 还是 "N"?

## ChatGPT 答案 (完整)

**结论先说：**

这条 AE 在 AE 域里应判为 serious adverse event，所以 AE.AESER = "Y"。
导致 serious 的直接依据是 住院 3 天治疗，因此 AE.AESHOSP = "Y"。其余 SAE 判定类变量，按你给出的病例信息，概念上都应为 "N"。但要注意：在 SDTM 中，如果 CRF 设计是"先问 AESER=Yes/No，再勾选适用原因"，则未勾选的 seriousness 子变量可以留空（null）而不是必须填 N；示例里就是这种做法。

另外，**"严重皮疹"** 这句话在医学叙述里常常是指 severity/intensity 很重，对应的是 AE.AESEV；而 AESER 表示是否为 serious event。这两个概念在 SDTM 里是分开的变量。

### 本例建议填写

| 变量 | 含义 | 本例判断 | 说明 |
|------|------|:--------:|------|
| AE.AESER | Serious Event | Y | 已被 investigator 判定为严重不良事件，且满足 serious criterion（住院）。 |
| AE.AESCONG | Congenital Anomaly or Birth Defect | N | 与先天异常/出生缺陷无关。 |
| AE.AESDISAB | Persist or Signif Disability/Incapacity | N | 题干未描述持续或显著残疾/失能。 |
| AE.AESHOSP | Requires or Prolongs Hospitalization | Y | 因皮疹住院 3 天，符合住院 serious criterion。 |
| AE.AESLIFE | Is Life Threatening | N | 题干未描述危及生命。 |
| AE.AESDTH | Results in Death | N | 未死亡。 |
| AE.AESMIE | Other Medically Important Serious Event | N | 本例 serious 已被"住院"解释，不需要再用"其他医学上重要 SAE"兜底。 |

### 关键规则

AE 域假设明确说：如果 serious 类别变量是作为 "Serious?" 之后的原因勾选项 来收集，那么当 AESER = "Y" 时，至少一个 seriousness 子变量要有 "Y"；其他变量可以按 sponsor 约定填 "N" 或留空。相反，如果 CRF 是"Serious? = Yes 后只勾选适用原因"，则更常见的 SDTM 结果是：
- AESER = Y
- AESHOSP = Y
- 其余 AESCONG / AESDISAB / AESLIFE / AESDTH / AESMIE = null

最后补一句：题干里的"药物相关"不影响 AESER 及其子变量的判断，它通常体现在 AE.AEREL 这类因果关系变量，而不是 seriousness 变量。

### 源溯源

- `<!-- source: knowledge_base/domains/AE/assumptions.md -->`
- `<!-- source: knowledge_base/domains/AE/examples.md -->`
- `<!-- source: knowledge_base/chapters/ch04_general_assumptions.md -->`
- `<!-- source: knowledge_base/domains/AE/spec.md -->`

## 判据对齐 (v2.1)

- ✅ AESER = Y (严重事件识别)
- ✅ AESHOSP = Y (导致住院)
- ✅ AESLIFE = N (非危及生命)
- ✅ AESDTH = N (非导致死亡)
- ✅ AESDISAB = N (非致残)
- ✅ AESCONG = N (非先天异常)
- ✅ AESMIE = N (非重要医学事件)
- ✅ 每个变量有中英含义
- ✅ 额外区分 AESER vs AESEV (seriousness vs severity, 加分)
- ✅ 引 4 源 (AE/assumptions + AE/examples + ch04 + AE/spec.md)

## Verdict: **PASS** (1/1)

## 归因

系统 prompt v2.1 + AE 域 knowledge 命中, 7 个子变量全对 + 额外 AESER/AESEV 区分提醒 (专业增值). null-vs-N 讨论体现 SDTM 深度.
