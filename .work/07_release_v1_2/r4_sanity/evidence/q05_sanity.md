# R4 Sanity Q5 — FA/QS/CE 边界 (Gemini v8.1 LIVE, 3.1 Pro)

**Date**: 2026-05-20 AM
**Platform**: Gemini Gem v8.1 LIVE (SDTM Knowledge Base Gem; `ai_platforms/gemini_gems/current/system_prompt.md` 525 行)
**Model**: Gemini 3.1 Pro (mode picker 明确选 "3.1 Pro Advanced math & code")
**Conversation URL**: https://gemini.google.com/u/1/gem/3b572e310813/3dfd3f1c8c509025
**Question source**: `ai_platforms/SMOKE_V4.md:562-587`
**Execution**: Chrome DevTools MCP, 新 conversation (per 用户要求)

---

## 题目

> 以下 3 条 EDC 收集信息, 分别映射到 FA / QS / CE 哪个 SDTM 域?
>
> **场景 A**: 受试者有既往 MH "类风湿性关节炎 15 年", 研究者在 Visit 4 对这条既往 MH 记录做量化评分 (用 28-joint tender/swollen count, 记 DAS28 评分 4.2). 这是对**既往 MH 记录**的量化 findings (非针对 AE).
>
> **场景 B**: 受试者在 Visit 4 填 SF-36 生活质量问卷, 8 个维度每个打分
>
> **场景 C**: 受试者自诉 Visit 5 出现轻微头晕 (dizziness, 30 秒自愈), 研究者记录但不认为需医疗处理, 未达 AE 报告阈值
>
> 每个场景: (i) 域名 + (ii) 理由 + (iii) Topic 变量值示例

---

## Gemini v8.1 答案 (a11y snapshot 完整抽取)

### 场景 A
- **(i) 域名**: **FA** (Findings About Events or Interventions)
- **(ii) 理由**: FA 域专门用于记录针对特定 Events (如既往病史) 或 Interventions 记录的特征评估与量化测量。当测量结果只是该事件在某个时间点的切片 (snapshot) 或部分属性, 而不能代表该事件整体时, 必须使用 FA 域。本场景中, DAS28 评分是对该受试者既往的类风湿性关节炎 (MH 记录中的 Event) 在特定访视时的量化 finding, 不属于对不良事件的记录。
- **(iii) Topic 变量值示例**: **FATESTCD** = "DAS28" (或对应标准短码), **FATEST** = "DAS28 Score" (或标准全称), 并且必须使用 **FAOBJ** = "Rheumatoid arthritis" (或对应的 MH 诊断词) 以指明该测量针对的具体客体对象。

### 场景 B
- **(i) 域名**: **QS** (Questionnaires)
- **(ii) 理由**: 针对经过标准验证的问卷 (validated questionnaires, 如 EQ-5D、SF-36、HAM-D 等) 及评表, 不论是各维度的单项打分还是计算出的总分, 均属于 Findings 观察类, 明确归入独立的 QS 域。此类数据需拆分记录, 每个 item 或维度在每个时间点对应一条记录, 而不应作为 FA 处理。
- **(iii) Topic 变量值示例**: **QSTESTCD** = "SF36-xx" (对应的维度代码, 受控于特定 instrument codelist), **QSTEST** = "SF-36 - [维度名称]", 并配合 **QSCAT** = "SF-36" 将问卷的所有相关记录归类在一起。

### 场景 C
- **(i) 域名**: **CE** (Clinical Events)
- **(ii) 理由**: 根据 SDTM 规则, 在试验期间收集到的、不属于计划内测量的临床症状发作或体征, 若在当前试验方案或医学判定下不满足不良事件 (AE) 的报告标准 (即事件本身不构成 AE), 但仍作为独立事件被收集时, 应归入 CE 域。这与专门记录符合报告要求之不良事件的 AE 域形成明确分工。
- **(iii) Topic 变量值示例**: **CETERM** = "Dizziness" (受试者自诉或记录的原始事件术语)

**来源**:
- SDTMIG v3.4 FA domain — assumptions
- SDTMIG v3.4 §6.4.1 When to Use Findings About Events or Interventions
- SDTMIG v3.4 QS domain — assumptions
- SDTMIG v3.4 CE domain — assumptions

---

## Strict 判据 evaluation

| 项 | 判据 | v8.1 答案 | 命中 |
|---|---|---|:---:|
| 1 | A: FA, FAOBJ 指向 MH | ✅ FA + FAOBJ="Rheumatoid arthritis (对应 MH 诊断词)" | ✓ |
| 2 | A: 不用 QS (DAS28 非独立问卷而是 MH 评估) | ✅ 明确"DAS28 评分是对既往的类风湿性关节炎(MH 记录中的 Event)... 的量化 finding" | ✓ |
| 3 | A: 不用 SUPPMH | ✅ 答 FA 不答 SUPPMH (判据是否定项, 不需主动否定) | ✓ |
| 4 | B: QS + QSTESTCD/QSCAT | ✅ QS + QSTESTCD="SF36-xx" + QSCAT="SF-36" | ✓ |
| 5 | C: CE, 不用 AE/DV | ✅ CE + 明确"不满足 AE 报告标准"+"与 AE 域形成明确分工" | ✓ |
| 6 | FAIL: A 答 QS? | ✅ 没 | ✓ |
| 7 | FAIL: A 答 SUPPMH? | ✅ 没 | ✓ |
| 8 | FAIL: B 答 FA 或 CE? | ✅ 没 | ✓ |
| 9 | FAIL: C 答 AE 或 DV? | ✅ 没 | ✓ |

**9/9 命中, 0 FAIL**

---

## Watch finding (Rule D #17 — Q5 关注 CO-2f 文件格式 gate)

| Watch | 该题观察 | 风险 |
|---|---|---|
| CO-2f 文件格式 gate (v8.1 4-prong 新增) 是否把正常域判别题误锁? | Q5 是 FA/QS/CE 域判别, 完全非文件格式题. v8.1 gate 没误触发, 答案直接正常给出 ✓ | ✓ no risk |
| CO-5 default reflection 在多场景判别题里是否过度? | Q5 三场景串答, 每场景"(i)域名/(ii)理由/(iii) Topic 变量" 结构清晰, 无过度自我修正; 但场景 B/C 没主动列"不用 X" 的禁忌对照 (vs Q1 风格) | LOW (caveat) |

---

## PASS+ upgrade evidence (vs R3 v7.1 baseline PASS)

R3 v7.1 答案是 PASS. R4 v8.1 升级到 PASS+:

1. **主动列多 instrument 类型** (EQ-5D / SF-36 / HAM-D) — 比题目要求多 2 个 instrument, KB grounded
2. **FA §6.4.1 KB 章节级 citation** — "When to Use Findings About Events or Interventions" 引用了 SDTMIG specific section
3. **主动 FA 原理引用** — "切片(snapshot)或部分属性, 而不能代表该事件整体" — 主动解释为何不能用 MH 直接
4. **主动 QS 数据 granularity 规则** — "每个 item 或维度在每个时间点对应一条记录" — 超出题目要求
5. **CE vs AE 边界声明** — "与专门记录符合报告要求之不良事件的 AE 域形成明确分工" — 主动 boundary clarification

---

## Conclusion

**Verdict: PASS+** ★ (R3 baseline PASS, v8.1 **升级**)

**Regression status**: ✅ 无回归, 反而升级.

**v8.1 prompt 表现**:
- 4-prong CO-2f 文件格式 gate 没误触发 Q5 域判别 ✓
- CO-5 default reflection 适度 (结构化 ABC 三场景), 无过度修正
- KB citation §6.4.1 章节级精确, 超出 Q2 PASS 的 § 级 citation

**Sanity 累计 3/5 题** (Q1 PASS+ / Q2 PASS / Q5 PASS+) — 全部 ≥ R3 baseline, 0 regression.

**Next**: Q6 (PK timing 四件套, watch CO-5 default reflection 在 timing 题里是否过度自我修正).
