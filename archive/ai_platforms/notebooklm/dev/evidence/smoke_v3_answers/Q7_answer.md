# Q7 (C2 — Partial date) EDC 只给部分日期怎么填

> Date: 2026-04-22 / Account: bojiang.zhang.0904@gmail.com / Fresh chat

---

## 题

ISO 8601 datetime 变量 (e.g., AESTDTC, CMSTDTC) 允许部分精度. 下列 3 个场景, 各应怎么填? SDTMIG v3.4 对 partial date 有没有 imputation 规则 (SDTM 级还是 ADaM 级)?
- 场景 A: EDC 只收到 "AE 开始于 2024 年 6 月" (无日)
- 场景 B: EDC 只收到 "服药开始于 2024 年" (无月日)
- 场景 C: EDC 完全没收到 AE 开始日 (Unknown)

另外回答: (d) SDTM 的 --STDTC 需要做 imputation 吗? (e) 如果 ADaM 需要 imputation, SDTM 还需要额外记什么吗?

## NotebookLM 答 (full text)

ISO 8601 格式允许通过省略 (truncation) 缺失的日期组件来表示精度的降低 [29_ig_ch04_general_assumptions.md]。针对您提出的三个场景, SDTM datetime 变量 (如 AESTDTC, CMSTDTC) 的填写规则如下:

- **场景 A** (EDC 只收到 "2024 年 6 月"): 应填写为 `2024-06` [29_ig_ch04_general_assumptions.md]。由于未知具体日期和时间, 直接从右侧截断缺失部分 [29_ig_ch04_general_assumptions.md]。
- **场景 B** (EDC 只收到 "2024 年"): 应填写为 `2024` [29_ig_ch04_general_assumptions.md]。未知的月份、日期和时间直接截断 [29_ig_ch04_general_assumptions.md]。
- **场景 C** (EDC 完全没收到 AE 开始日, Unknown): 该字段应当**置空 (null)** [29_ig_ch04_general_assumptions.md]。规则明确指出, 如果日期和时间值完全缺失, SDTM 的 datetime 字段必须为 null [29_ig_ch04_general_assumptions.md]。

**(d) SDTM 的 --STDTC 需要做 imputation 吗?**

不需要。SDTM 的核心要求之一是如实反映"最初收集或接收的数据"(Data as originally collected or received) [28_ig_ch01_ch02_ch03.md]。根据 SDTMIG v3.4 规则, 收集到的不完整日期仅需以 ISO 8601 支持的部分精度格式记录, 绝对不可以在 SDTM 层面进行估算或插补 (imputation) [29_ig_ch04_general_assumptions.md]。此外, 一般规则明确限制: "部分日期不应被用来推导研究日 (Partial dates should not be used to derive study day)" [29_ig_ch04_general_assumptions.md]。

**(e) 如果 ADaM 需要 imputation, SDTM 还需要额外记什么吗?**

SDTM 中**不需要为了支持 ADaM 的插补而额外记录任何衍生变量或标志**。SDTM 的职责是纯粹提供收集到的不完整日期原始值, 以此保证数据从 ADaM 到 SDTM 的严格可追溯性 (traceability) [28_ig_ch01_ch02_ch03.md]。为统计分析目的而进行的规则衍生和日期插补 (derived records/results outside the CRF) 应当完全在 ADaM 数据集中进行处理, 以避免在 SDTM 中模糊"收集值"与"衍生值"的界限 [17_fnd_oncology_tr_tu_rs_oe.md, 29_ig_ch04_general_assumptions.md]。

| Variable | Type | Role | Core | CT | Source |
|---|---|---|---|---|---|
| AESTDTC | Char | Timing | Exp | ISO 8601 datetime or interval | [08_ev_adverse_ae.md] |
| CMSTDTC | Char | Timing | Perm | ISO 8601 datetime or interval | [06_int_concomitant_cm_ag_ml.md] |

## Verdict

| Criterion | Required | Got | Status |
|---|---|---|:---:|
| Scenario A → "2024-06" | "2024-06" | `2024-06` ✓ + 截断规则解释 | ✅ |
| Scenario B → "2024" | "2024" | `2024` ✓ + 截断规则解释 | ✅ |
| Scenario C → null | null/空 (不可"UNKNOWN" 字符串) | "字段应当置空 (null)" + 明示 datetime 必须 null | ✅ |
| (d) SDTM 不做 imputation | SDTM 保真, 不 impute | "绝对不可以在 SDTM 层面进行估算或插补" + Partial dates 不推 study day | ✅ |
| (e) ADaM 责任, SDTM 不额外记 | SDTM 不增 imputation flag | "不需要为了支持 ADaM 的插补而额外记录任何衍生变量或标志" + traceability + ADaM 处理 | ✅ |
| 不写 imputed value | 没写 "2024-06-01"/"2024-06-15" | 严格保留 partial precision, 没补 01 | ✅ |
| 不混 SDTM/ADaM 责任 | 边界明确 | "SDTM 的职责是纯粹提供收集到的不完整日期原始值"; ADaM 才做 imputation | ✅ |

**Verdict**: ✅ **PASS** (1 / 1) — 7 项判据全中。3 个场景 ISO 8601 部分精度全对 (年月 / 年 / null) + (d)(e) SDTM/ADaM 边界清楚。加分: "Partial dates should not be used to derive study day" 一般规则原文引用 + traceability + "derived records outside the CRF" ADaM 处理原则。无 FAIL 触发 (没补 01, 没写 "UNKNOWN", 没说 SDTM 做 imputation)。
