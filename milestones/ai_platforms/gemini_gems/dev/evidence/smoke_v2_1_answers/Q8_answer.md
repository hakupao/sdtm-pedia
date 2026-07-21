# Q8 Answer — ISO 8601 时间精度 + --STDY 计算

- URL: https://gemini.google.com/u/1/gem/3b572e310813/61db292d7493563f
- 模式: Pro
- Date: 2026-04-21

## 答案摘要

### 1. AESTDTC 精度 (ISO 8601)

| 场景 | AESTDTC 格式 | 示例 |
|------|------------|------|
| EDC 记录到时:分 | `YYYY-MM-DDThh:mm` | `2026-04-21T14:00` |
| EDC 只记到日 | `YYYY-MM-DD` | `2026-04-21` |
| EDC 记到小时 (无分) | `YYYY-MM-DDThh` | `2026-04-21T14` |

**核心规则**: 记录到源数据的**最高精度**, `T` 作日期-时间分隔. **严禁**无原始支持情况下补齐时间 (如补 `T00:00`).

### 2. --STDY (Study Day) 计算

**公式** (相对于 RFSTDTC):

- 事件日期 ≥ RFSTDTC: `STDY = (事件日 - RFSTDTC) + 1`
- 事件日期 < RFSTDTC: `STDY = 事件日 - RFSTDTC`

**关键锚点**: **无 Day 0** — 若计算得 0 即逻辑错误.
- Day 1 = RFSTDTC 当天
- Day -1 = RFSTDTC 前一天

### 3. AE 域变量属性

| 变量 | Core | Role | 含义 |
|------|------|------|------|
| AESTDTC | Perm | Timing | AE Start Date/Time |
| AESTDY | Perm | Timing | AE Start Study Day |

注: Core 虽 Perm, 但涉疗效/安全性分析时一般必算必递.

### 4. 源路径 (CO-3)

- ISO 8601 规则: knowledge_base/chapters/ch04_general_assumptions.md §4.1.1
- Study Day 规则: knowledge_base/chapters/ch04_general_assumptions.md §4.4.4
- AE 变量定义: knowledge_base/domains/AE/spec.md §AESTDTC, §AESTDY

## v2.1 判据对齐

| PASS 判据 | 结果 |
|----------|------|
| AESTDTC 到分精度 = YYYY-MM-DDThh:mm | ✅ 格式明确 |
| EDC 只记到日 → AESTDTC = YYYY-MM-DD (不补) | ✅ 严禁补 00:00 明确 |
| 最高精度原则 (§4.1.1) | ✅ 引用 |
| --STDY 两段式公式 (≥RFSTDTC → +1 / <RFSTDTC → 直接差) | ✅ 完整 |
| **无 Day 0** 硬锚点 (SDTMIG §4.4.4) | ✅ 命中 |
| Day 1 = RFSTDTC 当天 / Day -1 = 前一天 | ✅ 明确 |
| 源路径 CO-3 (ch04 §4.1.1 + §4.4.4 + AE spec §AESTDTC/§AESTDY) | ✅ 合规 |

| FAIL 判据 | 结果 |
|----------|------|
| AESTDTC 补 "T00:00" (无原始支持) | ✅ 未触 (明确严禁) |
| 出现 "Day 0" (Day 1 = RFSTDTC 前一天之类错算) | ✅ 未触 |
| --STDY 公式漏掉 "+1" 导致 shift by 1 | ✅ 未触 |
| ISO 8601 格式错 (如用 `/` 或 ` ` 分隔) | ✅ 未触 (T 分隔符正确) |

## 注意

- 响应后段 Gemini 试图生成"交互式计算与格式演示" (Show me the visualization) — 这是 Gemini 自发行为, 不影响主体答案判据. 文本部分在 §4 源路径后自然结束, 已覆盖所有必要信息.

## Verdict: **PASS** (1.0 分)

主判据全通过: AESTDTC 到分精度 ✅ / YYYY-MM-DD fallback 规则 ✅ / 禁补 00:00 ✅ / --STDY 两段公式 ✅ / 无 Day 0 硬锚点 ✅ / Day ±1 正确 ✅ / CO-3 源路径 ✅.

关键锚点 "无 Day 0" 命中 — 这是 v2.1 核心硬判据.
