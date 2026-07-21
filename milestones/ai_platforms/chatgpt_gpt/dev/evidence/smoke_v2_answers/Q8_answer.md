# Q8 — 时间精度: AESTDTC ISO 8601 + AESTDY 计算

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef81-2edc-83a6-b13e-2c1cac11d0e7
**Title**: SDTM Expert - AESTDTC AESTDY 规则

## 原题

受试者当天早 8:00 服药, 下午 2:00 发生头痛 (AE). EDC 里精确记录了时:分. SDTM AE 域的 AESTDTC (开始日期) 变量应该填什么? ISO 8601 精度是到日 (YYYY-MM-DD) 还是到分 (YYYY-MM-DDThh:mm)? 如果 EDC 只记到日, AESTDTC 怎么填? --STDY 类 Study Day 变量又是什么计算规则?

## ChatGPT 答案

**结论先说**:

**AE.AESTDTC 应按 EDC 实际采集到的精度填写**, 不是固定只能到日. 如果 EDC 记录到时:分, 那 AESTDTC 就应填 **YYYY-MM-DDThh:mm**, 例如 `2025-05-01T14:00`. ISO 8601 在 SDTM 里允许保留到分钟; 如果秒没采集, 就不要补秒.

如果 EDC 只记到日, 那 AESTDTC 就填 **YYYY-MM-DD**, **不要臆造 00:00 或任何时间**.

**--STDY (AE 中就是 AESTDY) 只用日期部分计算, 不看时分秒**. 它是把 AESTDTC 的日期部分与 DM.RFSTDTC 的日期部分相比:
- 当天或之后: Study Day = 日期差 + 1
- 之前: Study Day = 日期差
- **没有 Day 0**

**场景示例**:

| 场景 | AESTDTC | AESTDY |
|---|---|---|
| 当天 14:00 发生头痛, EDC 记到分 | 2025-05-01T14:00 | 若 DM.RFSTDTC 日期为 2025-05-01, 则 1 |
| 当天只知道发生在这一天 | 2025-05-01 | 若 DM.RFSTDTC 日期为 2025-05-01, 则 1 |

**两个容易混淆的点**:
1. 同一天早 8:00 服药、下午 2:00 发生 AE, AESTDY 仍然只是 1. 因为 Study Day 不看时间, 只看"是不是同一个日历日". 真正体现"先服药、后发 AE"的, 是 AESTDTC 里的时间精度, 而不是 AESTDY.
2. 不要为了算 Study Day 把时间砍掉. AESTDTC 该保留分钟就保留分钟.

**补一句规则边界**: --DY/--STDY/--ENDY 的锚点是 DM.RFSTDTC, 不是你想当然的"首剂时间". 很多研究里二者一致, 但标准上是以 RFSTDTC 为准.

AE 域示例里也有这种写法: AESTDTC = 2005-10-13T13:05, 同时 AESTDY = 1.

SDTMIG 还提醒: **Study Day 不适合做持续时间等数值计算, 要用原始日期/日期时间去算**.

## PASS 判据自检

- [x] ISO 8601 允许到分: AESTDTC = "YYYY-MM-DDThh:mm" ✓ (给 2025-05-01T14:00)
- [x] 若 EDC 只记到日 → AESTDTC = "YYYY-MM-DD" ✓
- [x] ISO 8601 允许部分精度 ✓ ("时间精度由已知/已采集的组成部分决定")
- [x] AESTDY = 相对 DM.RFSTDTC 的天数 ✓
- [x] 起始日当日 = Day 1 (非 Day 0) ✓ ("没有 Day 0")
- [x] AESTDY 计算规则明确 ✓ (当天或之后=+1, 之前=直接差)

## Verdict: **PASS**

核心判据全中 + 额外 3 个亮点: (1) 明确说"不要臆造 00:00"; (2) 指出 AESTDY 锚点是 DM.RFSTDTC 非首剂时间; (3) 提醒 Study Day 不适合做持续时间数值计算. 是 10 题里最清晰的一题, 有具体 AE 域示例 (2005-10-13T13:05) 佐证.
