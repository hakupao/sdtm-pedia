# Q4 Answer — AESEV vs CTCAE Grade 映射

- URL: https://gemini.google.com/u/1/gem/3b572e310813/2b0e45cb98b6a22e
- 模式: Pro
- Date: 2026-04-21

## 答案摘要

### AESEV 三档 (Perm)
| 取值 | 含义 |
|------|------|
| MILD | 轻度 — 通常不影响日常活动, 不需医疗干预 |
| MODERATE | 中度 — 影响日常活动, 可能需要非紧急医疗干预 |
| SEVERE | 重度 — 显著影响日常活动, 需紧急医疗干预 |

### CTCAE Grade → AESEV 映射
| Grade | AESEV | 备注 |
|-------|-------|------|
| 1 (Mild) | MILD | 轻度症状, 仅观察 |
| 2 (Moderate) | MODERATE | 症状影响日常活动 |
| 3 (Severe) | SEVERE | 需住院或显著干预 |
| 4 (Life-threatening) | SEVERE | AESER=Y + AESLIFE=Y |
| 5 (Death) | SEVERE | **AESER=Y + AESDTH=Y + AEOUT=FATAL + DM.DTHFL=Y** |

### EDC 只有 Grade 怎么办
- **方案 A**: 按 SAP 派生 AESEV (Grade 1→MILD / Grade 2→MODERATE / Grade 3-5→SEVERE)
- **方案 B**: 不派生 AESEV, 改用 AETOXGR (Toxicity Grade, Perm) 承载 Grade 原值

### AESEV vs AESER 关键区分
- AESEV = 强度 (intensity/severity), Perm
- AESER = 严重性 (serious = 监管口径, 涉及住院/致死/致残等), Exp
- Grade 3 ≠ SAE (SEVERE 只说症状强, 不代表 serious); Grade 4/5 → AESER=Y (life-threatening/death 进 serious 列)

### 源路径 (CO-3)
- knowledge_base/domains/AE/spec.md §AESEV (Perm)
- knowledge_base/domains/AE/assumptions.md (severity vs seriousness 区分)
- knowledge_base/chapters/ch04_general_assumptions.md §4.5.1
- knowledge_base/chapters/04_business_scenarios_and_cross_domain.md §1.2 (AE 强度分级) / §2.1 (AE→SAE 升级)

## 判据对齐

| PASS 判据 | 结果 |
|----------|------|
| AESEV 三档 MILD/MODERATE/SEVERE | ✅ 全列 |
| Grade 1→MILD / 2→MODERATE / 3+ →SEVERE | ✅ 映射清晰 |
| Grade 5 = 死亡, AESDTH=Y + AEOUT=FATAL + AESER=Y | ✅ 联动变量全写 |
| AESEV vs AESER 区分 (强度 ≠ 严重性) | ✅ 明确 |
| AETOXGR 作为 Grade 原值承载方案 | ✅ 给出替代路径 |

| FAIL 判据 | 结果 |
|----------|------|
| 混淆 AESEV 与 AESER | ✅ 未触 |
| 仅给两档 | ✅ 未触 |
| Grade 5 漏 AESDTH | ✅ 未触 |
| AESEV 当 Req 填 | ✅ 未触 (正确标 Perm) |

## Verdict: **PASS** (1.0 分)

三档 MILD/MODERATE/SEVERE 全对 + Grade→AESEV 映射矩阵完整 + Grade 5 联动 AESDTH/AEOUT/AESER 全链到位 + AESEV vs AESER 强度 vs 严重性边界清晰 + CO-3 源路径合规.
