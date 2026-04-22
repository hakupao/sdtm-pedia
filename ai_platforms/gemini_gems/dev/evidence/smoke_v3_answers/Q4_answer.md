# Q4 — Gemini SDTM Expert 回答 (B1 — LB vs MB vs IS 三场景)

> 期望核心: A=IS (抗麻疹 IgG) + B=IS (ADA) + C=MB (Mtb 培养) + v3.4 边界规则 (IS=免疫应答, MB=微生物直接检出, LB=常规生化)
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/bbd295645d40e656
> 时间: 2026-04-22
> Mode: Pro

## 完整回答

根据 SDTMIG v3.4 的定义及领域间边界规则（Boundary Rules），这三个实验室检验结果的归属及理由如下：

### 场景 A：疫苗试验中的抗麻疹病毒 IgG 抗体滴度

(i) 域名: IS (Immunogenicity Specimen Assessments)

(ii) 理由:
- IS 还是 LB? IS 领域专门用于记录对"挑战物"（如疫苗）产生的免疫反应，或评估受试者过往的免疫状态。本例是在疫苗试验中检测抗体滴度以评估过往感染或接种史，符合 IS 的定义。LB 通常记录常规生化、血液学等指标。
- IS 还是 MB? MB 用于记录微生物（如病毒、细菌）的存在或鉴定。抗体检测是受试者体内的免疫反应产物，而非直接检测微生物本身。

(iii) Topic 变量值示例: ISTEST = "Measles Virus IgG Antibody", ISTESTCD = "MSLIGG"

(iv) v3.4 边界规则: 当实验室测试旨在评估受试者对外部抗原的免疫状态（Immune Status）或对疫苗的免疫反应（Immune Response）时，应归入 IS 领域。

### 场景 B：治疗后的抗药物抗体 (ADA) 阳性/阴性 + 滴度

(i) 域名: IS (Immunogenicity Specimen Assessments)

(ii) 理由:
- IS 还是 LB? ADA 是受试者对所施用的生物药物（作为一种免疫原/挑战物）产生的特异性免疫反应。SDTMIG 明确指出，评估受试者对研究药物产生的抗体属于 IS。
- IS 还是 PC? PC (Pharmacokinetics) 记录药物在体内的浓度，而 IS 记录受试者对药物产生的免疫反应结果（抗体）。

(iii) Topic 变量值示例: ISTEST = "Anti-Drug Antibody", ISTESTCD = "ADAB"

(iv) v3.4 边界规则: 对于生物技术产品，检测受试者是否产生针对该产品的抗体（Anti-Drug Antibodies）是免疫原性评估的核心，必须放入 IS 领域。

### 场景 C：痰样结核杆菌培养 (Culture)

(i) 域名: MB (Microbiology Specimen)

(ii) 理由:
- MB 还是 LB? MB 用于鉴定样本中是否存在特定的微生物。结核杆菌培养旨在确认受试者体内是否有该致病菌，属于典型的微生物鉴定任务。LB 虽然也有微生物子类，但 IG 规定一旦涉及菌种鉴定、培养或敏感性测试，应优先使用 MB 及其相关领域（MS）。
- MB 还是 IS? 此场景是检测微生物的存在，而非检测受试者对该微生物产生的抗体反应。

(iii) Topic 变量值示例: MBTEST = "Mycobacterium tuberculosis Culture", MBTESTCD = "MTBCULT"

(iv) v3.4 边界规则: 微生物学领域（MB）用于记录来自人体样本的微生物（细菌、病毒、真菌等）的检测、发现和鉴定。

### 源路径:
- knowledge_base/domains/IS/assumptions.md (关于免疫状态和疫苗反应的定义)
- knowledge_base/domains/MB/assumptions.md (关于微生物鉴定和培养的定义)
- knowledge_base/chapters/ch04_general_assumptions.md §4.5 (Findings 类通用规则)
- 04_business_scenarios_and_cross_domain.md §1.3 (IS vs LB 映射指南)

## 判据对齐

| 维度 | 期望 | 实际 | Hit |
|------|------|------|-----|
| A (抗麻疹 IgG) | IS + MSLIGG-style | IS + MSLIGG / Measles Virus IgG Antibody | ✅ |
| B (ADA) | IS + ADA codelist + ISBDAGNT=药物名 | IS + ADAB + Anti-Drug Antibody | ✅ |
| C (Mtb 培养) | MB + MTBCULT | MB + MTBCULT | ✅ |
| v3.4 边界规则 | IS 免疫应答 / MB 微生物直接 / LB 常规生化 | 明确阐述 3 档边界 + A 对 LB/MB 区分 + B 对 LB/PC 区分 + C 对 LB/IS 区分 | ✅ |

## Verdict

**PASS** — 3/3 场景域全对 + Topic 变量示例合理 (MSLIGG / ADAB / MTBCULT) + v3.4 边界规则 3 档完整阐述 + 每场景主动对比"为什么不是另外两个域"符合题目要求. ISBDAGNT 未显示列出但 Topic 变量示例正确. Pure generalization 考核通过.

- 04 引用: 1 次 ("04_business_scenarios_and_cross_domain.md §1.3 IS vs LB 映射指南"), 04 弹药包直接命中但本题要求的是 IS/MB/LB 三元, 弹药包主要覆盖 IS vs LB — 04 辅助作用
- CO-2 触发: 无 (Topic 变量示例直接给, 但未查 NCI EVS 字典确认 — 本题 Topic 示例是 "合理猜" 非 CT 强制)
- Score: 1 / 1
