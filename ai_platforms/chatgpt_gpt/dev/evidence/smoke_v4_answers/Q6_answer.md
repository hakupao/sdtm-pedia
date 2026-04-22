# ChatGPT Q6 answer — PK --TPT 四件套

**Verdict**: PASS+

## 核心表

| 场景 | PCTPT | PCTPTNUM | PCTPTREF | PCELTM | PCRFTDTC |
|---|---|---|---|---|---|
| 周期 1 4h | 4 H POST-DOSE | 4 | PERIOD 1 DOSE A-001 | PT4H | 2026-05-01T08:00 |
| 周期 2 4h | 4 H POST-DOSE | 4 | PERIOD 2 DOSE A-001 | PT4H | 2026-05-08T08:00 |

## (a) PCTPT vs PCTPTNUM
- PCTPT = 文字版 (4 H POST-DOSE); PCTPTNUM = 数值排序号 (4)
- Time point 时必须同时用 --TPT 和 --TPTNUM, 唯一性上下文一一对应
- PCTPTNUM 可按小时数 (4) 或顺序号 (1/2/3/4/5), 全研究必须一致

## (b) PCTPTREF
- Reference time point 的文字描述 = 这组 PK 采样的"零点"
- 不建议泛写 DOSE, 推荐 `PERIOD 1 DOSE A-001` / `PERIOD 2 DOSE A-001` 区分 profile
- PC examples 明确: 多 profile 时 PCTPTREF 必须不同

## (c) PCELTM 格式
**ISO 8601 duration** (非日期时间):
- P=period, T=time part, 4H=4 hours → `PT4H`
- 其他: PT15M / PT1H / PT8H
- 是 planned elapsed time, 非 actual 时差

## (d) 两周期区分
三层组合:
1. **VISIT / VISITNUM**: PERIOD 1 PK (1) vs PERIOD 2 PK (2)
2. **PCTPTREF**: PERIOD 1 DOSE A-001 vs PERIOD 2 DOSE A-001
3. **PCRFTDTC**: 2026-05-01T08:00 vs 2026-05-08T08:00

PC 自然键: VISITNUM + PCTPTREF + PCTPTNUM + PCTESTCD 组合

## 源溯源
- ch04_general_assumptions.md (通用 time point 规则)
- PC/spec.md (PC 域变量定义)
- PC/examples.md (PCTPTREF 零点描述 + 多 profile 规则)

## 评分要点
- ✓ 5 变量全填对 (4H/4/PERIOD-DOSE/PT4H/ISO datetime)
- ✓ (a) TPT 文本/TPTNUM 数值 关系 + 一致性 note
- ✓ (b) PCTPTREF 零点描述 + 多 profile 必须不同
- ✓ (c) PT4H ISO 8601 duration + planned vs actual 区分
- ✓ (d) VISIT+TPTREF+RFTDTC 三层 + 自然键说明
- ✓ 源路径标注
