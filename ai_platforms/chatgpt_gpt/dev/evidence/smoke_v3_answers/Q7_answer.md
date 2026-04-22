# Q7 (B4 — Partial date ISO 8601 + Imputation) CM 部分日期场景

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83822-a2b8-83a9-b66d-e130948b5659
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: 2m 2s

## 完整回答 (要点摘录)

### (a) ISO 8601 partial date 填法

| 源数据 | CMSTDTC | CMENDTC |
|---|---|---|
| 起 "2025 年 3 月" / 终 "2025-04-15" | `2025-03` | `2025-04-15` |
| 起 "2024" / 终 "2024-06" | `2024` | `2024-06` |

**关键**: 不需要写成区间 (如 `2025-03-01/2025-03-31`), 因为这是**不完整日期 (reduced precision)**, 不是"明确记录成一个不确定区间". SDTM 优先允许**右截断**保留原始精度.

### (b) SDTM 阶段是否需要 imputation

**不需要, 通常也不应该.**

SDTMIG 说明 `--DTC / --STDTC / --ENDTC` 可存:
- complete date/time
- partial date/time
- incomplete date/time

缺失部分通过**右截断**或在中间缺项时用连字符表示; 整条日期/时间都缺失时该 SDTM 日期字段应为 **null**.

实务总结:
- partial date 保持 partial, 不强行补全
- 不要把未采集到的日/月"伪造"进 CMSTDTC / CMENDTC

### (c) ADaM 阶段处理与 SDTM 的关键不同

**ADaM 与 SDTM 不一致, 这正是两层最大差异.**

ADaM 目标: 支持分析判定 (是否 treatment-emergent / 用药是否基线前后 / 用药持续时长 / 与其他分析窗口比较), 因此**常常会把 partial date 补成完整分析日期**, 再配合 imputation flag / traceability.

补全规则必须**预先定义、可追溯、与 SAP/分析规则一致**.

实务结论:
- **SDTM**: 保留 `2025-03` / `2024`
- **ADaM**: 可以根据分析规则补成完整日期, 但那是 **analysis derivation**, 不是 SDTM 原值

常见做法: ADaM 会针对"起始日期缺日""结束日期缺日"采用保守补全, 但具体补到月初/月末/治疗开始日/或其他规则, 取决于分析目的和 sponsor 规则.

### (d) "unknown / 不详" SDTM 该怎么填

**未知日期本身 → CMSTDTC / CMENDTC 置 null (空)**.

若采集到"之前 / 持续中 / 未知"这类**相对时序信息**, 用 CMSTRTPT / CMENRTPT (或更常见的 CMSTRTPT / CMENRTPT) 这类相对时间变量表达, 而**不是编一个日期**.

CM 规范明确允许这类 "PRIOR / ONGOING / CONTINUING" 信息.

例子:
- CRF 勾"Prior" 且起始日期未知/未采集 → CMSTRTPT = "BEFORE", CMSTTPT = <参考日期>, CMSTDTC = null
- 勾"Continuing" 且结束日期未采集 → CMENRTPT = "ONGOING", CMENTPT = <参考日期>, CMENDTC = null

### 一句话落地规则

- 有年有月没日: `YYYY-MM`
- 只有年: `YYYY`
- 完全不知道: 空值 null

## 判据对齐

- (a) CMSTDTC partial date "2025-03" + "2024" 正确 ✓; CMENDTC "2025-04-15" + "2024-06" 正确 ✓
- (b) SDTM 不需要 imputation ✓ (3 类 complete/partial/incomplete 全允许)
- (c) ADaM 不同 — 分析层会补全 + imputation flag, 是 derivation 不是 SDTM 原值 ✓
- (d) unknown → null + 相对时序 (CMSTRTPT/CMENRTPT BEFORE/ONGOING) ✓
- bonus: 一句话规则三档清晰 (YYYY-MM / YYYY / null) ✓
- bonus: 不写成"区间"避免 reduced precision 与不确定区间混淆 ✓

源溯源命中:
- `<!-- source: knowledge_base/domains/CM/spec.md -->`
- `<!-- source: knowledge_base/chapters/ch04_general_assumptions.md -->`

## 归因

PASS — Pure generalization (04 ch04 一般 ISO 8601 + 各域 STDTC/ENDTC 通用规则). ChatGPT 完整答出 4 子问题, partial date 三档 (YYYY-MM / YYYY / null) 清晰; SDTM vs ADaM 边界明确 ("SDTM 原值 vs ADaM derivation"); 相对时序变量 CMSTRTPT/CMENRTPT 作为兜底方案是非 trivial 加分项. 思考时长 2m 2s.
