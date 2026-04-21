# Q5 Answer — PK LLOQ (BLQ) 处理

- URL: https://gemini.google.com/u/1/gem/3b572e310813/05e0cced60365fa5
- 模式: Pro
- Date: 2026-04-21

## 答案摘要

| 变量 | 填写规则 | 说明 |
|------|----------|------|
| PCORRES | 原始报告字符 (如 "< 0.5" 或 "BLQ") | 必须反映原始记录字符形式 |
| PCSTRESC | 与 PCORRES 一致 (如 "< 0.5" 或 "BLQ") | 标准单位下字符结果, 便于汇总展示 |
| **PCSTRESN** | **保持为空 (Null)** | **关键规则: 实际数值未知且无法定量, 不能填数值** |
| PCLLOQ | 具体定量下限数值 (如 "0.5") | 记录检测方法的定量下限, 供统计分析参考 |

## 为什么不能直接写 0 (三条理由)

1. **科学准确性**: 低于 LLOQ 不等于浓度为 0, 只表示浓度在 0~LLOQ 区间但无法准确测量
2. **统计处理灵活性**: 不同 SAP 对 BLQ 的处理不同 (按 0 / 按 LLOQ / 按 LLOQ/2), SDTM 保留"无法定量"事实, 具体估算留 ADaM
3. **区分缺失与零**: 填 0 后审阅时无法区分"真实零结果" (极罕见于 PK) vs "低于下限结果"

## Findings 类通用准则 (SDTMIG §4.1.5.1)

对于无法转化为数值的非数值型结果 (如 "< 0.5"), `--STRESN` **必须为空**.

## 源路径 (CO-3)

- knowledge_base/domains/PC/assumptions.md §3, §4 (BLQ 处理 + PCLLOQ 使用)
- knowledge_base/chapters/ch04_general_assumptions.md §4.1.5.1 (Findings Result Variables)

## 判据对齐

| PASS 判据 | 结果 |
|----------|------|
| PCORRES = "< 0.5" / "BLQ" 字符 | ✅ |
| PCSTRESC 与 PCORRES 一致 | ✅ |
| **PCSTRESN 必须为空** | ✅ 明确标 Null |
| PCLLOQ 填数值 (如 0.5) | ✅ |
| 不能直接写 0 理由 (科学准确性 / SAP 灵活性 / 区分零与缺失) | ✅ 三条全列 |
| 引 SDTMIG §4.1.5.1 | ✅ |

| FAIL 判据 | 结果 |
|----------|------|
| PCSTRESN 填 0 | ✅ 未触 |
| PCSTRESN 填 LLOQ/2 (属 ADaM 派生) | ✅ 未触 |
| 忘记 PCLLOQ | ✅ 未触 |
| 混 PCSTRESC / PCSTRESN 类型 | ✅ 未触 (字符 vs 数值明确分开) |

## Verdict: **PASS** (1.0 分)

PCSTRESN=Null 硬核规则命中 + PCLLOQ 捕获 LLOQ 值 + 三条拒填 0 理由完整 (科学/统计/缺失-零区分) + CO-3 源路径合规 (§4.1.5.1 Findings 类通用准则引用).
