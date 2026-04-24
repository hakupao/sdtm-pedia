# ChatGPT GPTs — Q6 PC PK Timing 4-件套 (V5C post-apply v2.2 LIVE)

> **执行时间**: 2026-04-24 (V5C regression)
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69ead5fa-2840-83a2-88d5-c4f0911fa6eb
> **题类**: Q6 (C1 — Timing 深化 PCTPT/PCTPTNUM/PCTPTREF/PCELTM/PCRFTDTC)

## Raw (DOM readback, trimmed)

**结论**: PC (Pharmacokinetics Concentrations) 记录的 Timing 变量 (假设研究只有 post-dose 4 个计划采血点):

| Timing 变量 | 建议取值 | 说明 |
|---|---|---|
| PCTPT | **4H** 或 "4 h post-dose" | 计划时间点文字名称 |
| PCTPTNUM | **3** | 排序: 15 min=1 / 1 h=2 / 4 h=3 / 8 h=4 |
| PCTPTREF | **PERIOD 1 DOSE / PERIOD 2 DOSE** 或 A-001 DOSE 加周期 | zero time 描述; 多 PK profile 必须能区分 |
| PCELTM | **PT4H** | ISO 8601 duration/period 格式 |
| PCRFTDTC | `<Period N dosing date>T08:00` | 参考点实际 ISO 8601 datetime |

### 解释

- **(a) PCTPT vs PCTPTNUM**: PCTPT 文字描述; PCTPTNUM 数值排序. 一对一关系, 同编号不能有不同文字. SDTMIG §4.4.10 强调 --TPT 和 --TPTNUM 必须配对用.
- **(b) PCTPTREF**: time point 的参考点文字描述 (zero time). 服药事件 A-001 DOSE. 多周期时需区分 PERIOD 1 DOSE / PERIOD 2 DOSE.
- **(c) PCELTM 格式**: ISO 8601 **duration/period**, 不是 clock time. 4 小时 = **PT4H**. §4.4.10 明 --ELTM 是 planned elapsed time; 实际可由 PCDTC - PCRFTDTC 派生.
- **(d) 两周期区分**:

| 周期 | VISITNUM | VISIT | PCTPT | PCTPTNUM | PCTPTREF | PCRFTDTC |
|---|---|---|---|---|---|---|
| Period 1 | 1 | PERIOD 1 | 4H | 3 | PERIOD 1 DOSE | `<P1 date>T08:00` |
| Period 2 | 2 | PERIOD 2 | 4H | 3 | PERIOD 2 DOSE | `<P2 date>T08:00` |

用 VISITNUM/VISIT 区分周期 + --TPTREF 区分 day/dose + --TPTNUM 相对参考点时间. SDTMIG §4.4.10 crossover/multiple-period 例子.

## Self-score verdict

- **Verdict**: **PASS**
- **对照 PASS 判据**:
  - PCTPT "4H" / "4 h post-dose" ✓
  - PCTPTNUM (数字排序) ✓
  - PCTPTREF (name, 给药参考点) ✓
  - PCELTM ISO duration "PT4H" ✓ (未写成 "4 hours" 或 "04:00:00")
  - PCRFTDTC ISO datetime ✓
  - (a)(b)(c)(d) 全解释 ✓
- **触发 FAIL?** 无 (未写 "4 hours" / 未写 datetime 作 PCTPTREF / 未混 Planned vs Actual / 未用 VISITDY 错误区分)
- **加分**:
  - 多 PK profile 时 PCTPTREF 必须不同 (深入)
  - 两周期完整示例表 (crossover 场景)
  - SDTMIG §4.4.10 明确引用
- **v5c→v2.2 delta**: 无 regression, 完整 4-件套 + 两周期表深度超 N5.2 baseline
