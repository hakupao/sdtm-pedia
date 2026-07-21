# Gemini Gems — Q6 PC PK Timing 4-件套 (V5C post-apply v7 LIVE)

> **执行时间**: 2026-04-24 (V5C regression)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/2b8dec9cedef5226
> **题类**: Q6 (C1 — Timing 深化)

## Raw (DOM readback)

PC (Pharmacokinetics Findings) 域 "服药后 4 小时采血" 记录的 Timing 变量:

### 1. 变量填充示例

| 变量 | 填充值 | 说明 |
|---|---|---|
| PCTPT | **4 h POST-DOSE** | 计划时间点名称 |
| PCTPTNUM | **4** | 排序数值 |
| PCTPTREF | **A-001 DOSE** | 参考点名称 |
| PCELTM | **PT4H** | ISO 8601 duration |
| PCRFTDTC | **2026-04-24T08:00** | 参考点实际 datetime |

### 2. 规则解释

- **(a) PCTPT vs PCTPTNUM**: PCTPT 文字描述 (PRE-DOSE / 4 h POST-DOSE); PCTPTNUM 数值排序. 一对一关系. (依据: 02_spec PC §)
- **(b) PCTPTREF**: 计划时间点所相对的固定参照物/事件的名称. PK 里通常 "PREVIOUS DOSE" 或 "A-001 DOSE".
- **(c) PCELTM 格式**: ISO 8601 **duration**. P (Period) 开头 + T 时间部分. 15 min=PT15M / 4 h=**PT4H** / 1 h 30 min=PT1H30M. 记录计划偏离时间 (非实际).
- **(d) 两周期区分**:
  - VISIT / VISITNUM (e.g., "Period 1" / "Period 2")
  - EPOCH (e.g., "PERIOD 1" / "PERIOD 2")
  - PCRFTDTC: 两周期参考服药时间不同, 最直接的时序区分

### 源路径

- `knowledge_base/domains/PC/spec.md` §PCTPT / §PCTPTNUM / §PCTPTREF / §PCELTM / §PCRFTDTC
- `knowledge_base/chapters/ch04_general_assumptions.md` §4.4.10 Planned Elapsed Time + §4.1.4.10 EPOCH

## Self-score verdict

- **Verdict**: **PASS**
- **对照 PASS 判据**:
  - PCTPT "4 h POST-DOSE" ✓
  - PCTPTNUM 4 ✓
  - PCTPTREF "A-001 DOSE" ✓ (name, not datetime)
  - PCELTM "PT4H" ISO duration ✓
  - PCRFTDTC ISO datetime ✓
  - (a)(b)(c)(d) 全解释 ✓
- **触发 FAIL?** 无
- **加分**:
  - EPOCH (C99079) 区分治疗阶段 (PASS 判据列出)
  - PCRFTDTC 作周期时序区分最直接 (bonus observation)
- **v5c→v7 delta**: 无 regression, 深度持平 N5.2 baseline
