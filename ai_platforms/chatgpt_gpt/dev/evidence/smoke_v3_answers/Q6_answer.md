# Q6 (B3 — PC Timing) "服药后 4 小时采血"五 Timing 变量

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83684-dbb8-83a2-b014-32f6dacd5010
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: 2m 57s

## 完整回答 (要点摘录)

### 推荐落地写法

**周期 1 的"服药后 4 小时采血"**:
- PCTPT = 4h post
- PCTPTNUM = 4
- PCTPTREF = Period 1 Dose
- PCELTM = PT4H
- PCRFTDTC = 2026-05-01T08:00

**周期 2 的"服药后 4 小时采血"**:
- PCTPT = 4h post
- PCTPTNUM = 4
- PCTPTREF = Period 2 Dose
- PCELTM = PT4H
- PCRFTDTC = 2026-05-08T08:00

### (a) PCTPT vs PCTPTNUM

PCTPT 是 planned time point name (文字标签); PCTPTNUM 是其 numerical version, 用于排序. 互为对偶, 一个给人读, 一个给系统排序.

### (b) PCTPTREF

PCTPTREF 是 zero time 的文字描述 — 即 elapsed time 的"起算点". PK 多 profile 设计中需要不同的 zero time (Period 1 Dose / Period 2 Dose / Day 1 Dose / Day 11 Dose 等). PC 示例直接给了"Day 1 Dose / Day 11 Dose"区分多个 PK profile.

### (c) PCELTM ISO 8601 格式

ISO 8601 duration 基本样式: PnYnMnDTnHnMnS 或 PnW (按周).

本题映射:
- 15 min → PT15M
- 1 hour → PT1H
- **4 hours → PT4H**
- 8 hours → PT8H

**重要补充 (诚实知识点)**: PCELTM 是**计划** elapsed time, 不是实际 elapsed time. PCELTM=PT4H 表示"方案计划在给药后 4 小时采", 实际采样时间由 PCDTC 反映, 不由 PCELTM 反映. SDTM 示例也明确说 --ELTM 是 planned elapsed time.

### (d) 两周期记录区分

最关键的是**组合区分**, 不靠单变量:
1. VISITNUM / VISIT — 区分周期或周期内日期
2. PCTPTREF — 不同 zero time 的文字标签 (Period 1 Dose vs Period 2 Dose)
3. PCRFTDTC — 实际给药日期时间 (2026-05-01T08:00 vs 2026-05-08T08:00)

可选: EPOCH (TREATMENT 1 vs TREATMENT 2), PCSEQ (within-subject 排序).

## 判据对齐

- PCTPT = "4h post" (text label) ✓
- PCTPTNUM = 4 (numeric for sort) ✓
- PCTPTREF = "Period 1 Dose" / "Period 2 Dose" (zero time text) ✓
- **PCELTM = PT4H (ISO 8601 duration)** ✓
- PCRFTDTC = ISO 8601 datetime ✓
- (a) PCTPT vs PCTPTNUM 关系正确 ✓
- (b) PCTPTREF = zero time 含义正确 ✓
- (c) PCELTM ISO 8601 duration 格式正确 (PnYnMnDTnHnMnS) ✓
- (d) 两周期组合区分 (VISITNUM + PCTPTREF + PCRFTDTC) ✓
- bonus: PCELTM 是 planned 不是 actual 的诚实区分 ✓
- bonus: PCDTC vs PCELTM 边界明确 ✓

源溯源命中:
- `<!-- source: knowledge_base/domains/PC/spec.md -->`
- `<!-- source: knowledge_base/domains/PC/examples.md -->`
- `<!-- source: knowledge_base/chapters/ch04_general_assumptions.md -->`

## 归因

PASS — Pure generalization. PC Timing 五件套 (TPT/TPTNUM/TPTREF/ELTM/RFTDTC) 全对; ISO 8601 duration 格式正确写出 PT4H; 两周期区分用组合 (VISITNUM+TPTREF+RFTDTC); planned vs actual 区分 (PCELTM vs PCDTC) 是非 trivial 加分项. 思考时长 2m 57s.
