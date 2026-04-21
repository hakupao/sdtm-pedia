# Q8 — Gemini SDTM Expert answer

> URL: https://gemini.google.com/u/1/gem/3b572e310813/84127d4e253dedf4
> Mode: Pro
> Run: 2026-04-21

## 原题
受试者当天早 8:00 服药, 下午 2:00 发生头痛 (AE). EDC 里精确记录了时:分. SDTM AE 域的 AESTDTC (开始日期) 变量应该填什么? ISO 8601 精度是到日 (YYYY-MM-DD) 还是到分 (YYYY-MM-DDThh:mm)? 如果 EDC 只记到日, AESTDTC 怎么填? --STDY 类 Study Day 变量又是什么计算规则?

## 答案全文

根据您描述的业务场景，针对 SDTM AE 域的 AESTDTC 填报及 --STDY 计算规则，解答如下：

### 1. AESTDTC 的填报精度

**结论**：如果 EDC 精确记录了"时:分"，则 AE.AESTDTC 必须包含时间部分。

依据：根据 ISO 8601 规范及 SDTMIG 指导，日期时间变量的精度应与原始采集（Source Data）保持一致。既然 EDC 记录了 14:00，则应填入完整的日期时间格式。

具体填法：`2026-04-21T14:00`（假设日期为 2026-04-21）。

### 2. 如果 EDC 只记录到"日"

**结论**：如果 EDC 仅采集了日期，则 AE.AESTDTC 仅填写日期部分，严禁人为补齐（如补 00:00）。

依据：SDTM 不鼓励在没有任何依据的情况下对缺失的时间部分进行推断或填充。ISO 8601 允许部分精度。

具体填法：`2026-04-21`。

### 3. Study Day (--STDY) 计算规则

**结论**：Study Day 变量（如 AE.AESTDY）仅基于日期计算，不考虑时间，且没有 Day 0。

计算逻辑：

- **Day 1**：即受试者参考开始日期（RFSTDTC）当天。
- 计算公式：
  - 如果 日期 >= RFSTDTC：`AESTDY = (AESTDTC 的日期部分 - RFSTDTC 的日期部分) + 1`
  - 如果 日期 < RFSTDTC：`AESTDY = (AESTDTC 的日期部分 - RFSTDTC 的日期部分)`
- 注意：如果日期部分不完整（如缺失月份或日期），--STDY 通常留空。

**本例计算**：受试者 2026-04-21 服药（RFSTDTC），当天 2026-04-21 发生头痛（AESTDTC）。AE.AESTDY = (2026-04-21 - 2026-04-21) + 1 = 1。

### 变量属性核查 (AE Domain)

| 变量名 | Role | Core | 说明 |
|--------|------|------|------|
| AESTDTC | Timing | Exp | 遵循 ISO 8601，精度随源数据。 |
| AESTDY | Timing | Perm | 基于日期计算，无 Day 0。 |

**源路径**:
- 01_navigation_and_quick_reference.md §1.8 (ISO 8601) 与 Section 4.4.3 (Study Day Algorithm)
- 02_domains_spec_and_assumptions.md AE — Adverse Events §AESTDTC / §AESTDY
- 04_business_scenarios_and_cross_domain.md §9.6 Timing / ISO 8601
