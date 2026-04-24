# Gemini Gems — Q5 FA vs QS vs CE 边界 (V5C post-apply v7 LIVE)

> **执行时间**: 2026-04-24 (V5C regression)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/5107557923d904de
> **题类**: Q5 (B2 — FA/QS/CE 三场景选域)

## Raw (DOM readback, trimmed)

### 场景 A: DAS28 对既往 MH 评分
- (i) **FA (Findings About)**
- (ii) DAS28 是对特定既往病史 MH 记录的量化评价. FA 定义: "Findings 测量/评价是关于另一个域的记录" (MH). 非 QS (非问卷), 非 CE (非临床事件).
- (iii) FATESTCD="DAS28"; FATEST="DAS28 Score"; FAOBJ="RHEUMATOID ARTHRITIS" (对应 MH.MHTERM)
- **依据**: FA Assumptions §6.3 "The FA domain is used to capture findings that are about another domain's record"

### 场景 B: SF-36 QoL 问卷
- (i) **QS (Questionnaires)**
- (ii) SF-36 是标准化 QoL 问卷. 所有问卷结构数据 → QS.
- (iii) QSTESTCD="SF3601" (或具体维度代码); QSTEST="SF-36 Physical Functioning Score"; QSCAT="SF-36"
- **依据**: QS Assumptions §6.2 "Questionnaires (QS) includes data from standard or custom questionnaires"

### 场景 C: 轻微头晕 (未达 AE 阈值)
- (i) **CE (Clinical Events)**
- (ii) 受试者自诉临床事件. 未达 AE 报告阈值 → CE 域.
- (iii) CETERM="DIZZINESS"; CECAT="NON-SERIOUS ADVERSE EVENT NOT MEETING CRITERIA"; CEDTC="2026-04-24"
- **依据**: CE Assumptions §5.3 "CE is used to capture clinical events that are not captured in the AE domain" + 04 业务弹药 §1.5

## Self-score verdict

- **Verdict**: **PASS**
- **对照 PASS 判据**:
  - A=FA ✓ (未答 QS / SUPPMH)
  - B=QS ✓
  - C=CE ✓
- **触发 FAIL?** 无
- **v5c→v7 delta**: 无 regression. QSTESTCD 只给"SF3601"占位 (不如 ChatGPT 8 维度精确), 但 PASS 判据不要求; 深度持平 N5.2 baseline.
- **Observation**: Gemini 答更简洁; ChatGPT 对 SF-36 8 维度更厚 — 跨平台风格差异 (Rule E). 非 regression.
