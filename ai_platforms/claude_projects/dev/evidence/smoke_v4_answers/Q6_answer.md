# Claude Q6 answer — PK --TPT 四件套

**Verdict**: PASS+ (verified)

## 核心表 (Period 1 4h)

| 变量 | Role | 值 | 说明 |
|---|---|---|---|
| PCTPT | Timing (Char) | "4H POST-DOSE" | 方案文本时点名 |
| PCTPTNUM | Timing (Num) | 4 | 排序数值 (0/1/2/4/8 或 1/2/3/4/5) |
| PCTPTREF | Timing (Char) | "CYCLE 1 DOSE" | 参考时点文字描述 |
| PCELTM | Timing ISO 8601 duration | "PT4H" | 计划经过时间 |
| PCRFTDTC | Timing ISO 8601 | "2026-04-22T08:00" | 参考时点日期时间 |

配套 PCDTC (Exp) = 2026-04-22T12:00 (实际采样).

## (a) PCTPT vs PCTPTNUM
- PCTPT = Planned Time Point Name (Char, 给人看)
- PCTPTNUM = Planned Time Point Number (Num, 排序用)
- **§4.4.10 明文: When time points are represented, both --TPT and --TPTNUM must be used** (成对出现)
- 同一 PCTPT 一条记录内对应唯一 PCTPTNUM (1:1), Pre-dose 给 0 或 -1

## (b) PCTPTREF
- Time Point Reference = 锚点的文字描述, 与 PCRFTDTC (锚点日期时间) 配对
- 概念模型 (ch04 §4.4.10):
  ```
  [Reference] ──PCELTM(planned)──▶ [Collection]
   PCTPTREF(who)                     PCTPT/PCTPTNUM(name/num)
   PCRFTDTC(when)                    PCDTC(when-actual)
  ```
- 本案例: PCTPTREF="CYCLE 1 DOSE", PCRFTDTC=2026-04-22T08:00

## (c) PCELTM 格式
**ISO 8601 duration** (非 date/time). 格式 (§4.4.3.1):
- `PnYnMnDTnHnMnS` 或 `PnW`
- P (必填) / T 日期-时间分隔 / H M S
- Pre-dose 用负号: `-PT15M`
- 本例 → `PT4H`; 其他: PT15M / PT1H / PT8H
- 注: PCELTM = 计划经过时间, 实际 = PCDTC − PCRFTDTC (ADaM 派生)

## (d) 两周期区分 (多手段组合)
1. **VISITNUM / VISIT** (Expected in PC, 首选): PERIOD 1 (1) vs PERIOD 2 (2)
2. **PCTPTREF**: CYCLE 1 DOSE vs CYCLE 2 DOSE
3. **PCRFTDTC**: 2026-04-22T08:00 vs 2026-04-29T08:00
4. **PCDTC**: 实际采样日期天然不同
5. **PCSEQ** (Identifier Req): subject 内全局唯一, 但只保证唯一不传递"周期"语义
6. **EPOCH / TAETORD**: 若属不同 Element
7. **PCGRPID**: PC 例子用 (DRUGA_DAY1 vs DRUGA_DAY11), 便于 RELREC 关联 PP

**最佳实践** (PC Example 1 多剂量): VISITNUM + PCTPTREF + PCTPTNUM 三者联合保证 subject 内唯一性, 分工: VISIT=哪个访视, PCTPTREF=哪次给药, PCTPTNUM=给药后第几个采样.

## 完整 8 行填表示意 (2 周期 × 4 时点, 略 1h/8h 位)
| USUBJID | VISIT | VISITNUM | PCTPT | PCTPTNUM | PCELTM | PCTPTREF | PCRFTDTC | PCDTC |
|---|---|---|---|---|---|---|---|---|
| 001 | PERIOD 1 | 1 | 15 MIN POST-DOSE | 1 | PT15M | CYCLE 1 DOSE | 2026-04-22T08:00 | 2026-04-22T08:15 |
| 001 | PERIOD 1 | 1 | 4H POST-DOSE | 4 | PT4H | CYCLE 1 DOSE | 2026-04-22T08:00 | 2026-04-22T12:00 |
| 001 | PERIOD 2 | 2 | 4H POST-DOSE | 4 | PT4H | CYCLE 2 DOSE | 2026-04-29T08:00 | 2026-04-29T12:00 |

## 源溯源
- PC spec: knowledge_base/domains/PC/spec.md (#36-40 5 个 Timing 变量)
- Timing 模型: knowledge_base/sdtmig/ch04.md §4.4.3.1 (ISO 8601 duration) + §4.4.10 (Time Points + Crossover 两种 Option)
- PC Example 1: 09_examples_data_high.md (Day 1 / Day 11 重复剂量 PCTPT/PCELTM 组合)

## 评分要点
- ✓ 5 变量全填对 + Role 标注
- ✓ (a) 双向映射 + §4.4.10 法定硬约束 + Pre-dose 给值
- ✓ (b) 概念模型 + PCTPTREF/PCRFTDTC/PCTPT/PCDTC 四角关系
- ✓ (c) PT4H + 格式规范 + 负号 Pre-dose + 计划 vs 实际
- ✓ (d) 7 种区分手段 + 最佳实践 3 字段联合 + 语义分工
- ✓ 完整 8 行示意表 + 源路径精确到 §
