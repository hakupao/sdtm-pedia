# Q4 — LB vs MB vs IS 三场景 (ChatGPT)

> **平台**: ChatGPT GPTs / SDTM Expert
> **Chat**: `/c/69e8aac5-8c80-83a9-8bb0-be64bde96f62`
> **采集时间**: 2026-04-22 晚 (readback)
> **Verdict**: **PASS** (A=IS, B=IS, C=MB, 理由 + Topic 变量 + v3.4 边界规则全套)

---

## 结论先说

- 场景 A → IS
- 场景 B → IS
- 场景 C → MB

核心边界不是"是不是实验室结果", 而是这个结果在 SDTMIG v3.4 里表达的科学问题是什么:

- **IS**: 问"某个治疗/疫苗/过敏原/微生物/内源性分子, 是否在受试者体内诱导了免疫反应", 输出可以是阳/阴、存在/不存在、滴度或定量
- **MB**: 问"样本里有没有、是什么微生物", 典型是培养、检测、鉴定、后续药敏
- **LB**: 一般实验室检测; v3.4 还特别说明, 细胞因子/趋化因子/补体蛋白这类测定放 LB, 而不是 IS

## 场景 A — 疫苗试验 baseline 抗麻疹 IgG 滴度 1:128

(i) **域**: IS — Immunogenicity Specimen Assessments

(ii) 为什么是 IS (不是 LB / MB):
- IS 假设明确包括"治疗诱导的免疫反应""抗体定量""微生物感染后产生的抗体"; 疫苗试验 Example 5 明确展示基线抗体 (既往自然感染或接种史) 仍放 IS
- 不是 LB: LB 是一般实验室数据; v3.4 把"细胞因子/趋化因子/补体蛋白"划给 LB, 反过来说明抗体免疫原性评估不默认进 LB
- 不是 MB: MB 关注样本中微生物是否被检测/培养/鉴定; 这里测宿主产生的抗麻疹 IgG 抗体, 不是培养/识别麻疹病毒

(iii) Topic 变量示例:
- ISTESTCD = MBIGSAB
- ISTEST = IgG Antibody
- ISBDAGNT = MEASLES VIRUS
- ISORRES = 1:128
- ISORRESU = titer
- ISCAT = STUDY VACCINE-RELATED IMMUNOGENICITY (若研究疫苗本身是麻疹) 或 NON-STUDY-RELATED IMMUNOGENICITY (若为其他疫苗试验)

## 场景 B — ADA 阳性/阴性 + 滴度

(i) **域**: IS

(ii) 为什么是 IS:
- IS Assumption 1 原文: "IS domain holds assessments that describe whether a therapy (e.g., biologic, drug) induces an immune response"
- ADA 是 IS 的原型用例, Example 1 即 ADA 分层检测
- 不是 LB: 药物诱导的抗体响应明确归 IS
- 不是 MB: MB 只涉及微生物; ADA 与微生物无关

(iii) Topic 变量示例:
- ISTESTCD = ADA_BAB
- ISTEST = Binding Antidrug Antibody
- ISTSTOPO = SCREEN / CONFIRM / QUANTIFY (常分 3 条记录)
- ISBDAGNT = [study drug name]
- ISCAT = ANTIDRUG ANTIBODIES
- ISSCAT = HUMORAL IMMUNITY

## 场景 C — 痰培养结核杆菌 positive

(i) **域**: MB — Microbiology Specimen

(ii) 为什么是 MB:
- 典型微生物学培养/检测; MB 示例明确展示对样本培养/微生物鉴定放 MB
- MBTESTCD = MCORGIDN / Microbial Organism Identification
- 不是 IS: IS 关注宿主免疫反应; 这里不测宿主抗体/细胞免疫
- 不是 LB: 培养/微生物鉴定在 v3.4 有专门的 MB 域, 不混到 LB

(iii) Topic 变量示例:
- MBTESTCD = MCORGIDN
- MBTEST = Microbial Organism Identification
- MBORRES = MYCOBACTERIUM TUBERCULOSIS
- MBMETHOD = 培养方法
- MBSPEC = SPUTUM

## v3.4 下的边界规则

**1) 看"被测对象"是谁**
- 宿主的免疫反应 → IS (抗病毒 IgG / ADA / 细胞免疫反应)
- 样本里的微生物 → MB (培养阳性 / 菌种鉴定 / 药敏)
- 一般实验室 analyte → LB (化学 / 血液 / 尿常规 / 细胞因子 / 趋化因子 / 补体蛋白)

**2) 看"科学问题"是什么**
- 有没有诱导抗体/免疫反应? → IS
- 有没有这个菌/是什么菌? → MB
- 这个实验室指标是多少? → LB

**3) v3.4 的几个关键例外**
- 微生物 Ag/Ab 组合检测 (如 HIV 4 代 Ag/Ab combo) → MB, 不是 IS
- 细胞因子 / 趋化因子 / 补体蛋白 → LB, 不是 IS
- 疫苗试验 baseline 抗体仍进 IS, 用 ISCAT = STUDY VACCINE-RELATED / NON-STUDY-RELATED IMMUNOGENICITY 区分

## 源溯源 (ChatGPT 自列)

- knowledge_base/domains/IS/assumptions.md
- knowledge_base/domains/IS/examples.md
- knowledge_base/domains/LB/assumptions.md
- knowledge_base/domains/MB/examples.md
- knowledge_base/domains/IS/spec.md

---

## Verdict 判据

| 判据 | 是否满足 |
|---|:---:|
| A=IS | ✓ |
| B=IS | ✓ |
| C=MB | ✓ |
| 每场景给理由 (否定另外两域) | ✓ |
| Topic 变量值示例 | ✓ (IS: ISTESTCD/ISTEST/ISBDAGNT/ISCAT; MB: MCORGIDN/MBORRES) |
| v3.4 边界规则 | ✓ (3 步决策 + 3 关键例外) |
| 显式引 IS Assumption 4/5/6 划界 | ✓ |

**Verdict: PASS** (全 3 场景 + 边界规则显式 + Assumption 链)

**备注**: 与 NotebookLM Q4 PASS 对齐 (A=IS/B=IS/C=MB); 提示 baseline IgG ISCAT 条件判断 (study-related vs non-study-related) 是 ChatGPT 加分细节.
