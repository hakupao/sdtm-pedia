# Q2 Answer — AE 升 SAE, 住院相关 Serious 子变量

- URL: https://gemini.google.com/u/1/gem/3b572e310813/ffa1a644b61d8d99
- 模式: Pro
- Date: 2026-04-21

## 答案摘要 (7 子变量)

| 变量 | 取值 | 含义 |
|------|------|------|
| AESER | Y | Serious Event — 已判定为 SAE |
| AESHOSP | Y | Requires or Prolongs Hospitalization — 住院 3 天 |
| AESCONG | N | Congenital Anomaly or Birth Defect |
| AESDISAB | N | Persist or Signif Disability/Incapacity |
| AESLIFE | N | Is Life Threatening |
| AESDTH | N | Results in Death |
| AESMIE | N | Other Medically Important Serious Event (住院已覆盖) |

## CO-1 边界警示 (重要)
答案主动提示 AE 域 Core 不规则: AESER 为 **Expected (Exp)**, AESHOSP/AESCONG/AESDISAB/AESLIFE/AESDTH/AESMIE 均为 **Permissible (Perm)**. 这正是 CO-1 设计意图.

## 源路径 (CO-3)
- knowledge_base/domains/AE/spec.md §AESER, §AESHOSP, §AESCONG, §AESDISAB, §AESLIFE, §AESDTH, §AESMIE
- knowledge_base/domains/AE/examples.md Example 1

## 判据对齐

| PASS 判据 | 结果 |
|----------|------|
| AESER = Y | ✅ |
| AESHOSP = Y | ✅ |
| AESLIFE = N | ✅ |
| AESDTH = N | ✅ |
| AESDISAB = N | ✅ |
| AESCONG = N / AESMIE = N | ✅ 全 N |
| 每个变量有简短中文/英文含义 | ✅ |

| FAIL 判据 | 结果 |
|----------|------|
| AESER 填错 | ✅ 未触 |
| AESHOSP 填 N | ✅ 未触 |
| 子变量缺失 >=2 | ✅ 未触 |

## Verdict: **PASS** (1.0 分)

完美答案. 7 子变量全对 + CO-1 边界警示主动触发 + CO-3 源路径合规.
