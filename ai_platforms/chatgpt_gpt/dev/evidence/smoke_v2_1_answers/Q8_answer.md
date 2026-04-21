# Q8 — ISO 8601 精度 + AESTDTC / AESTDY 规则 (v2.1)

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e740d2-f124-83a5-805b-2e5e2e7502a5
**Date**: 2026-04-21
**Thought for**: 2m 13s

## 原题

受试者当天早 8:00 服药, 下午 2:00 发生头痛 (AE). EDC 里精确记录了时:分. SDTM AE 域的 AESTDTC (开始日期) 变量应该填什么? ISO 8601 精度是到日 (YYYY-MM-DD) 还是到分 (YYYY-MM-DDThh:mm)? 如果 EDC 只记到日, AESTDTC 怎么填? --STDY 类 Study Day 变量又是什么计算规则?

## ChatGPT 答案 (完整)

**结论**:

**AE.AESTDTC (Role: Timing, Core: Exp)** 应按 EDC 实际采集到的最细精度填 ISO 8601. 若 EDC 记到了"时:分", AESTDTC 就应填到分钟, 例如 `YYYY-MM-DDThh:mm`, 不应降到仅日期. AE 规范本身把 AESTDTC 定义为"Start Date/Time of Adverse Event", 格式为 ISO 8601 datetime or interval.

SDTMIG 明确说明: 日期时间精度由 ISO 8601 的"已知/缺失组件"表达; 如果只知道到分钟, 可以写成 `2003-12-15T13:14`; 如果没有时间部分, 则必须省略 `T`, 只写日期.

AE 示例也直接给出了分钟级的 AESTDTC, 如 `2005-10-13T13:05`, 并同时给出 AESTDY, 说明 AE 域完全允许保存到分钟.

### 按你这个场景

受试者当天 08:00 服药, 14:00 发生头痛, 且 EDC 精确记录到时:分
→ **AE.AESTDTC = YYYY-MM-DDT14:00**

不是填成仅 YYYY-MM-DD, 因为那会丢失已采集到的时间精度.
药物时间是给药记录自己的时间; AESTDTC 填的是 AE 的开始时间, 不是给药时间.

### 如果 EDC 只记到日

**AE.AESTDTC = YYYY-MM-DD**

不要人为补 `T00:00`, `T14:00` 或从别的记录"猜"时间.

### --STDY 公式

若 date(--DTC/--STDTC/--ENDTC) >= date(RFSTDTC)
→ **Study Day = 日期差 + 1**

若 date(--DTC/--STDTC/--ENDTC) < date(RFSTDTC)
→ **Study Day = 日期差**

Study Day 必须是整数; 部分日期不要用于推导 study day.

放到 AE 上:
- AESTDY 用 date(AESTDTC) 和 date(DM.RFSTDTC) 算
- AEENDY 用 date(AEENDTC) 和 date(DM.RFSTDTC) 算

### 小例子

假设 `DM.RFSTDTC = 2026-04-21`:
- 头痛发生于 `2026-04-21T14:00` → AESTDTC = 2026-04-21T14:00, **AESTDY = 1**
- 头痛发生于 `2026-04-22T14:00` → AESTDY = 2
- 头痛发生于 `2026-04-20T14:00` → **AESTDY = -1**

### 一句话概括

- **AESTDTC**: 保留已采集的最细实际精度
- **AESTDY**: 只按日期部分算, 相对 DM.RFSTDTC, Day 1 为参考起始日, **无 Day 0**

### 源溯源

- `knowledge_base/domains/AE/spec.md`
- `knowledge_base/chapters/ch04_general_assumptions.md`
- `knowledge_base/domains/AE/examples.md`

## 判据对齐 (v2.1)

- ✅ ISO 8601 允许到分: AESTDTC = "YYYY-MM-DDT14:00" (精度到分钟)
- ✅ ISO 8601 示例命中 `2005-10-13T13:05` (AE/examples 级)
- ✅ 若 EDC 只记到日 → AESTDTC = "YYYY-MM-DD" (部分精度保留)
- ✅ **不要人为补 T00:00 / 不从别记录猜时间** (加分边界)
- ✅ ISO 8601 部分精度机制 (`T` 省略规则)
- ✅ AESTDY = date 相对 DM.RFSTDTC 天数
- ✅ **Day 1 为起始日 (无 Day 0)** (v2.1 FAIL 陷阱规避, 答对)
- ✅ AESTDY 公式: 公式两分支 (>= RFSTDTC 则 +1, < RFSTDTC 则纯日期差负值)
- ✅ Study Day 必须整数 / 部分日期不推导 (边界完整)
- ✅ Study Day 只看 date 部分不看时分 (加分)
- ✅ 三示例 Day 1 / Day 2 / Day -1 立即 illustrative
- ✅ "药物时间 ≠ AE 开始时间" 额外区分 (加分)
- ✅ 引 3 源 (AE/spec + ch04 + AE/examples)

## Verdict: **PASS** (1/1)

## 归因

系统 prompt v2.1 + AE knowledge 全命中: ISO 8601 精度规则 + 部分精度表达 + AESTDY 公式两分支 + Day 1 (非 Day 0) + 3 示例 + "不猜时间" 边界告警, 均超判据基线. Study Day 整数 + 只用 date 细节 (加分). 3 源溯源完整.
