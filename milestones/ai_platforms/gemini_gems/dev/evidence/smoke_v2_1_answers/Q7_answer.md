# Q7 Answer — MH vs CM 双录 + Ongoing 表达

- URL: https://gemini.google.com/u/1/gem/3b572e310813/c69e293c5d69a151
- 模式: Pro
- Date: 2026-04-21

## 答案摘要

### 1. 结论: MH + CM 两边都要录

- **MH 域 (疾病状态侧重)**: 既往高血压病史作为医疗背景
- **CM 域 (用药时序侧重)**: 持续服用降压药作为合并用药

### 2. 关键时间变量区分

| 域 | 变量 | 取值 | 说明 |
|----|------|------|------|
| MH | MHENRF | `ONGOING` | End Relative to Reference Period — 慢病持续, 相对于 Period 未结束 |
| MH | MHSTRTPT | `BEFORE` | Start Relative to Time Point — 10 年前起病 |
| MH | MHSTDTC | 具体日期 | 配合 MHSTRTPT = BEFORE 使用 |
| CM | CMSTRTPT | `BEFORE` | 用药起始于参考时间点 (RFSTDTC) 之前 |
| CM | CMENRTPT | `ONGOING` | 用药持续中, End Relative to Time Point 未结束 |

**关键边界**: `--ENRF` 相对于参考**周期 (Period)**; `--STRTPT` / `--ENRTPT` 相对于参考**时间点 (Time Point)**.

### 3. Ongoing 状态三原则

1. **日期变量为空**: 对应 `MHENDTC` / `CMENDTC` 必须保持 null
2. **相对时间变量标注**: 填 CT 术语 `"ONGOING"`
3. **禁填推定日期**: 严禁"至今"或虚假日期

### 4. 源路径 (CO-3)

- knowledge_base/domains/MH/spec.md §MHENRF
- knowledge_base/domains/CM/spec.md §CMSTRTPT, §CMENRTPT
- knowledge_base/chapters/ch04_general_assumptions.md §4.4.1 (Timing Variables)
- 04_business_scenarios_and_cross_domain.md §1.15 (Medication & Disease relation)

### 5. CO-2 外导

- "ONGOING" / "BEFORE" 具体 Term 定义 / Submission Value: NCI EVS Browser C25496 相关 codelist
- 注: C25496 是 Relative Timing CT 的相关 code (方向性正确)

## v2.1 判据对齐

| PASS 判据 | 结果 |
|----------|------|
| MH + CM 两边都录 | ✅ 明确结论 |
| MH 用 MHENRF 承载 Ongoing (学派派 KB §34a 偏好) | ✅ 命中 |
| CM 用 CMSTRTPT=BEFORE + CMENRTPT=ONGOING | ✅ 完整 |
| --ENRF vs --STRTPT/--ENRTPT (Period vs Time Point) 区分 | ✅ 清晰 |
| Ongoing 三原则 (日期空 / CT 值 / 禁推定) | ✅ 全列 |
| 源路径 CO-3 (MH spec + CM spec + ch04 §4.4.1 + 04_business §1.15) | ✅ 合规 |
| CO-2 外导 NCI EVS C25496 | ✅ 明确提示 |

| FAIL 判据 | 结果 |
|----------|------|
| 只录 MH 不录 CM (或反之) | ✅ 未触 |
| 用 MHENDTC 填 "至今" 或推定日期 | ✅ 未触 |
| 误用 MHENRTPT 代替 MHENRF | ✅ 未触 (明确用 MHENRF) |
| 混淆 Period vs Time Point 两类相对时间变量 | ✅ 未触 |

## 小错注意 (minor)

- **MH 记录行误写 "AETERM = HYPERTENSION"**: 应为 `MHTERM = "HYPERTENSION"`. AETERM 是 AE 域变量, MH 域主题变量是 MHTERM (Req).
- 属于笔误, 不影响主判据 (因后续时间变量全部用 MH 前缀, 上下文一致性无问题).

## Verdict: **PASS** (1.0 分)

主判据全通过: MH + CM 双录 ✅ / MHENRF Ongoing 偏好 ✅ / CMSTRTPT BEFORE + CMENRTPT ONGOING ✅ / Period vs Time Point 边界 ✅ / Ongoing 三原则 ✅ / CO-3 源路径 ✅ / CO-2 NCI EVS 外导 ✅.

学派派 KB §34a 关键偏好 (MH 用 MHENRF 而非 MHENRTPT 表达 Ongoing) 正确命中 — 这是 Q7 最核心的判据点.

MHTERM 小错为笔误, 标记但不影响 Verdict.
