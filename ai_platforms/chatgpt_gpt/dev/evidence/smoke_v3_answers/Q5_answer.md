# Q5 (B2 — FA vs QS vs CE) 三场景域归属

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e8353e-1974-83ab-a8a7-dd4309e79d68
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: 2m 50s

## 完整回答

**结论先放前面**:
- 场景 A → **FA**
- 场景 B → **QS**
- 场景 C → **CE** (前提: 方案/申办方明确把这类"记录但不作为 AE 上报"的症状当作 clinical event 收集; 否则它也可能定义成 AE 或不进这 3 域)

| 场景 | 域 | 理由 | Topic 变量值 |
|---|---|---|---|
| A | FA | 对一条既往 MH 事件/疾病的**量化评估**, 不是新事件本身. SDTMIG 8.6.3 明确: 事件的属性被测量/评估时, 应作为 findings about the event; FA 假设也说当评估不是描述事件"整体"而是在某个时间点/某次访视对事件做评估时, 用 FA. 原始"类风湿性关节炎 15 年"仍在 MH, Visit 4 的 DAS28 评分进 FA, 与那条 MH 记录建立关系 (通常用 RELREC). | FATESTCD=DAS28, FATEST=Disease Activity Score 28; FAOBJ=RHEUMATOID ARTHRITIS |
| B | QS | 标准的问卷/量表场景. QS 定义就是"one record per questionnaire per question per time point per visit per subject". SDTMIG 8.6.3 还特别提醒: 即使问卷测的是症状/生活质量, 这类数据如果满足 QRS (Questionnaires/Ratings/Scales) 标准, 仍应进 QS/FT/RS, 不是 FA. SF-36 属典型问卷. | QSTESTCD=SF36PF, QSTEST=SF-36 Physical Functioning; QSCAT=SF-36 |
| C | CE | 独立发生的症状事件 (头晕), 不是对既有事件的评估, 所以不是 FA; 也不是问卷条目, 所以不是 QS. CE 假设说: 方案定义的、临床上有意义但不作为 AE 的事件, 应放 CE; 这类事件可包括疾病相关 signs/symptoms. 前提是研究者记录, 但未达 AE 报告阈值. | CETERM=DIZZINESS (或 verbatim Dizziness) |

### 逐条补充

**A 为什么不是 CE**:
A 不是"发生了一个新的事件", 而是对一条已经存在的 MH 记录做一次 visit-based assessment. SDTMIG 8.6.3 判断逻辑:
- 有单位/分值/量化结果 → 倾向 Findings
- 如果 finding 是"关于某 event 的", 就应是 FA
- 访视上反复做的"切片式评估"尤其符合 FA

这和 FA 例子里"AE 本身在 AE, 后续每次访视对 AE 严重度/形态的评估放 FA"是同一种建模思路, 只是父记录从 AE 换成 MH.

源溯源:
- `<!-- source: knowledge_base/chapters/ch08_relationships.md -->` (FA + RELREC)
- `<!-- source: knowledge_base/domains/FA/spec.md -->`
- `<!-- source: knowledge_base/domains/FA/assumptions.md -->`
- `<!-- source: knowledge_base/domains/QS/spec.md -->`
- `<!-- source: knowledge_base/domains/CE/spec.md -->`
- `<!-- source: knowledge_base/domains/CE/assumptions.md -->`

## 判据对齐

- A = FA ✓ (没误答 QS, 没误答 SUPPMH; FAOBJ→MH 的 RELREC 关系明确)
- B = QS ✓ (识别 SF-36 = QS 标准问卷, 引 QRS 8.6.3 优先级)
- C = CE ✓ (识别未达 AE 阈值的临床事件, 引 CE assumption)
- 每场景 (i)(ii)(iii) 三件套齐全 ✓
- bonus: FA vs CE 的"事件本身 vs 对事件的评估"二分法清晰

## 归因

PASS — 三元 FA/QS/CE 鉴别完美. KB 三域 spec/assumptions + 8.6.3 跨域规则全锚命中. 04 §1.19 仅覆盖 FA vs QS 二元, **CE 维度纯 generalization**. 对 C 的"前提条件"诚实说明 (方案/申办方定义) 体现深度. 思考过程透明 (2m 50s).
