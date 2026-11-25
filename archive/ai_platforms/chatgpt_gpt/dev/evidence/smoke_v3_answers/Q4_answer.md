# Q4 (B1 — LB vs MB vs IS) 三场景域归属

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e8340a-8568-83a4-b9d3-d1731338f6ec
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: 2m 27s

## 完整回答

**一句话边界**: IS 看"受试者有没有被某个东西诱导出免疫反应"; MB 看"样本里有没有微生物/是什么微生物"; LB 看"常规实验室检验", 且 LB **明确不含** microbiology.

### 场景 A: 抗麻疹病毒 IgG baseline → **IS**

**为什么 IS**: IS 适用于"由 therapy / vaccine / allergen / microorganism / endogenous molecule **诱导**的免疫反应评估", **明确包括"因微生物感染产生的抗体"**, 输出可阳/阴性、存在/不存在或定量值. v3.4 还专门说在疫苗研究里, 要区分研究疫苗相关和**非研究疫苗相关免疫原性**; 后者可来自自然感染或既往接种 — 正贴合 baseline 场景.

**为什么不是 MB**: MB 是"非宿主生物体在样本中的检测/鉴定", 看的是病原体本身, 不是宿主抗体反应.

**为什么不是 LB**: LB 是一般实验室数据; v3.4 把这类免疫原性/抗体反应单独建模到 IS. **LB 明确不含 microbiology**.

**示例**: ISTESTCD=MBIGSAB, ISTEST=IgG Antibody, ISBDAGNT=MEASLES VIRUS, ISTSTOPO=QUANTIFY, ISCAT=NON-STUDY-RELATED IMMUNOGENICITY, ISSCAT=HUMORAL IMMUNITY, ISORRES=1:128, ISORRESU=titer

### 场景 B: ADA (抗药物抗体) → **IS**

**为什么 IS**: IS 典型用例. IS assumptions 明确写到 therapy (biologic / drug / vaccine) 诱导的免疫反应属 IS; IS examples 直接给了 ADA 的 SCREEN / CONFIRM / QUANTIFY + titer 表示法.

**为什么不是 MB**: MB 是微生物检测/鉴定, ADA 靶标是药物/治疗本身, 不是非宿主生物体.

**为什么不是 LB**: 虽然也用实验室方法, 但 v3.4 把 therapy-induced immune response 专门放进 IS; ADA 还有 IS 专属变量 ISBDAGNT, ISTSTOPO 和官方示例.

**示例**: ISTESTCD=ADA_BAB, ISTEST=Binding Antidrug Antibody, ISBDAGNT=<study drug name>, ISTSTOPO=SCREEN/CONFIRM/QUANTIFY; 定量 ISORRES=40, ISORRESU=titer

### 场景 C: 痰样 MTB 培养 → **MB**

**为什么 MB**: MB 用于样本中非宿主生物体的检测/鉴定/表征. MB assumptions: 若靶向某 organism/antigen 鉴定, MBTEST 放目标, MBTSTDTL=DETECTION, 结果常为 PRESENT/ABSENT、POSITIVE/NEGATIVE 或 INDETERMINATE; 若非靶向, 则 MBTESTCD/MBTEST=MCORGIDN/Microbial Organism Identification, 结果放发现的 organism 名称. MB examples 还**专门给了 TB 场景**: 胃液样本里对 acid-fast bacilli 和 Mycobacterium tuberculosis 的检测记录存于 MB.

**为什么不是 IS**: 这里测的是痰样里有没有 MTB/培养是否阳性, 不是受试者对 MTB 的免疫反应. 若是 IGRA (M. tuberculosis IFN-gamma response) 这类宿主免疫反应, 才是 IS.

**为什么不是 LB**: LB 明确不含 microbiology.

**示例**: MBTESTCD=MCORGIDN, MBTEST=Microbial Organism Identification, MBORRES=MYCOBACTERIUM TUBERCULOSIS

源溯源:
- `<!-- source: knowledge_base/domains/IS/spec.md -->`
- `<!-- source: knowledge_base/domains/IS/assumptions.md -->`
- `<!-- source: knowledge_base/domains/IS/examples.md -->`
- `<!-- source: knowledge_base/domains/MB/spec.md -->`
- `<!-- source: knowledge_base/domains/MB/assumptions.md -->`
- `<!-- source: knowledge_base/domains/MB/examples.md -->`
- `<!-- source: knowledge_base/domains/LB/spec.md -->` (LB 不含 microbiology)

## 判据对齐

- 场景 A = IS ✓ (PASS — 明确识别 v3.4 IS scope 扩展, 引 NON-STUDY-RELATED IMMUNOGENICITY ISCAT 区分; 没触 v3.3 MB 旧规则)
- 场景 B = IS ✓ (PASS — ADA 经典用例, ISBDAGNT/ISTSTOPO 完整)
- 场景 C = MB ✓ (PASS — MCORGIDN 命中 KB 例; IGRA 为 IS 边界澄清正确)
- v3.4 边界规则三句话总结 ✓
- 每场景含 (i) 域名 (ii) 反向理由 (iii) Topic 示例 ✓

## 归因

PASS — Pure generalization (04 仅 §1.25 BE+MB 一句话). v3.4 IS scope 扩展 (anti-microbial antibody 无论 baseline 与否归 IS) 答对**没触 v3.3 MB 旧规则**, 这是高难判别点, ChatGPT 完美命中. KB IS spec/assumptions/examples + MB 三件套 + LB 边界全锚命中. 思考过程透明 (2m 27s).
