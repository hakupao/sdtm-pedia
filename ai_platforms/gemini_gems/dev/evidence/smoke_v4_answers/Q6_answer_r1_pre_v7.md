# Gemini Q6 answer — PK --TPT 四件套

**Verdict**: PASS

## 1. 变量填写建议 (服药 2026-04-20 08:00)

| 变量 | 值 |
|---|---|
| PCTPT | 4h post (或 4 HR POST-DOSE) |
| PCTPTNUM | 4 |
| PCTPTREF | Day 1 Dose (或 A-001 ADMINISTRATION) |
| PCELTM | PT4H (ISO 8601 duration) |
| PCRFTDTC | 2026-04-20T08:00 |

## (a) PCTPT vs PCTPTNUM
- PCTPT = Planned Time Point Name (文本描述, 直观展示)
- PCTPTNUM = Planned Time Point Number (数值, 排序)
- **一一对应**: PCTPTNUM 确保 PCTPT 按时间轴正确排序 (避免 "10h post" 排到 "2h post" 前)

## (b) PCTPTREF
- Time Point Reference = 计算 PCTPT/PCTPTNUM/PCELTM 的"零点"
- PK 通常指某次给药 (PREVIOUS DOSE 或具体 Day 11 Dose)
- 多周期必须能区分以保证唯一性

## (c) PCELTM 格式
**ISO 8601 duration**:
- PT4H = 4 小时后; PT15M = 15 min 后
- 是时间间隔, 非时钟时间
- 从 PCTPTREF 到计划观察点的计划偏移

## (d) 两周期区分
1. **VISIT / VISITNUM** (最核心): Day 1 vs Day 8
2. **PCTPTREF / PCRFTDTC**: Day 1 Dose vs Day 8 Dose + 日期相隔一周
3. **EPOCH**: 若方案定义不同 Element/Epoch (PERIOD 1, PERIOD 2) 可辅助

## 评分要点
- ✓ 5 变量全填对
- ✓ (a) TPT/TPTNUM 一一对应 + 排序用途
- ✓ (b) PCTPTREF 零点 + 多周期唯一性
- ✓ (c) PT4H ISO 8601 duration + 时间间隔而非时钟时间
- ✓ (d) 3 种区分手段 (VISIT + TPTREF/RFTDTC + EPOCH)
- △ 未显式提 §4.4.10 章节锚点; 深度一般
- ✓ 无 extended reasoning 暴露 (干净答复)

## 与 ChatGPT/Claude 对比
- 结构对, 覆盖全面 (5 vars + abcd + 3 种区分手段)
- 无 Claude 级完整 8 行示意表, 无 ch04 §ref 精确锚点
- 但比 Q4 PARTIAL 时已显式分 (a)(b)(c)(d) 答 — R2 prompt 改点在 Gemini 已生效
