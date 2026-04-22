# Q4 — LB vs MB vs IS 三场景 (Claude Projects)

> **平台**: claude.ai Projects / SDTM (v2.6 Project)
> **Chat**: `/chat/0fedf96b-69c1-4f43-84fd-dbd7b18ad607`
> **采集时间**: 2026-04-22 晚 (readback)
> **Verdict**: **PASS+** (A=IS, B=IS, C=MB, 全场景理由 + 完整 Qualifier 列表 + 边界规则表 + 决策优先级)

---

## 三场景域归属 (SDTMIG v3.4)

### 场景 A: 疫苗试验 baseline 抗麻疹 IgG 滴度 1:128

| 项 | 值 |
|---|---|
| 域 | **IS** (Immunogenicity Specimen Assessments) |
| Topic 变量 | ISTESTCD = MBIGGAB, ISTEST = Binding Microbial-induced IgG Antibody |
| 关键 Qualifier | ISBDAGNT = MEASLES VIRUS; ISCAT = NON-STUDY-RELATED IMMUNOGENICITY (若研究疫苗非麻疹); ISSCAT = HUMORAL IMMUNITY; ISORRES = 1:128 |

**理由**:
- IS 定义涵盖"微生物诱导的宿主体液/细胞免疫"评估 (§6.3.5.5 Assumption 2-3)
- 既往感染或接种形成的抗体 = "microorganism-induced humoral immunity", 即使非研究疫苗诱导也归 IS
- IS Assumption 9.b + Example 5 明确: 疫苗试验中"与研究疫苗无关但收集的免疫学数据"仍用 IS, 通过 ISCAT = NON-STUDY-RELATED IMMUNOGENICITY 区分
- 为什么不是 LB: IS Assumption 6 划界 — 只有细胞因子/趋化因子/补体蛋白归 LB; 抗体测定不归 LB
- 为什么不是 MB: MB 做的是在标本中识别/检测病原体本身, 此处检测的是宿主产生的抗体, 不是病毒

### 场景 B: 抗药抗体 (ADA) 阳性/阴性 + 滴度

| 项 | 值 |
|---|---|
| 域 | **IS** |
| Topic 变量 | ISTESTCD = ADA_BAB (Binding Antidrug Antibody) 或 ADA_NAB (Neutralizing); ISTEST 对应 |
| 关键 Qualifier | ISCAT = ANTIDRUG ANTIBODIES; ISSCAT = HUMORAL IMMUNITY; ISBDAGNT = <药物自由文本名>; ISTSTOPO = SCREEN / CONFIRM / QUANTIFY |

**理由**:
- IS Assumption 1 原文: "IS domain holds assessments that describe whether a therapy (e.g., biologic, drug) induces an immune response" — ADA 是 IS 的原型用例, Example 1 即 ADA 分层检测
- 为什么不是 LB: 药物诱导的抗体响应明确归 IS, 不是通用生化
- 为什么不是 MB: MB 只涉及微生物, ADA 与微生物无关

### 场景 C: 痰结核杆菌培养, positive

| 项 | 值 |
|---|---|
| 域 | **MB** (Microbiology Specimen) |
| Topic 变量 | MBTESTCD = MCORGIDN, MBTEST = Microbial Organism Identification |
| 关键 Qualifier | MBORRES = MYCOBACTERIUM TUBERCULOSIS; MBSPEC = SPUTUM; MBMETHOD = MICROBIAL CULTURE, SOLID; MBTSTDTL = DETECTION |

**理由**:
- MB Assumption 1.a: "针对某一生物体/生物群/抗原的检测", MBTSTDTL="DETECTION", 结果为 POSITIVE/NEGATIVE 或直接填检出菌名
- SDTMIG Example 3 正是结核杆菌 (Mtb) 痰/胃液培养场景, 归 MB
- 若做药敏 (DST) → 配套 MS (Microbiology Susceptibility) 域, 与 MB 通过 MBREFID/MSREFID 关联
- 为什么不是 LB: 微生物学标本的识别/检测/培养特征有专属域 MB, 不归通用 LB
- 为什么不是 IS: IS 测宿主免疫反应; 此处是在痰中识别病原体, 不涉及宿主抗体/细胞免疫

---

## v3.4 边界规则总览 (LB / MB / IS)

| 测量对象 | 归属 | 依据 |
|---|:---:|---|
| 宿主对药物/生物制品诱导的免疫应答 (ADA) | IS | §6.3.5.5 Assumption 1 |
| 宿主对微生物/过敏原诱导的体液/细胞免疫 (含疫苗 & 既往感染) | IS | Assumption 2, 3 |
| 标本中鉴定/检测微生物或培养特征 | MB | §6.3.5.7.1 Assumption 1 |
| 微生物药敏 | MS | §6.3.5.7.2 |
| 微生物 Ag/Ab 组合测试 (同一试剂盒同时测抗原+抗体) | MB (非 IS) | IS Assumption 5 (关键例外) |
| 流式细胞术 / 细胞表型 | CP (非 IS) | IS Assumption 4 |
| 细胞因子 / 趋化因子 / 补体蛋白 | LB (非 IS) | IS Assumption 6 |
| 一般临床化验 (血常规, 生化, 凝血, 尿液等) | LB | §6.3.5.6 |

## 决策优先级 (v3.4)

1. 是"宿主的诱导免疫应答"? → IS (再按 Assumption 4/5/6 排除 CP / MB / LB)
2. 是"标本中的微生物识别/表征/药敏"? → MB / MS
3. 否则 → LB

---

## 源溯源 (Claude 自列)

- knowledge_base/domains/IS/assumptions.md (IS 10 条 assumptions, 含关键 5/6 划界)
- knowledge_base/domains/IS/examples.md Example 1 (ADA) / Example 5 (疫苗 study-related vs non-study-related)
- knowledge_base/domains/MB/assumptions.md (MB 4 条, 含 DETECTION / 培养特征规则)
- knowledge_base/domains/MB/examples.md Example 3 (TB 痰培养)
- SDTMIG §6.3.5.5 / §6.3.5.6 / §6.3.5.7

---

## Verdict 判据

| 判据 | 是否满足 |
|---|:---:|
| A=IS | ✓ |
| B=IS | ✓ |
| C=MB | ✓ |
| 每场景理由 + 否定另外两域 | ✓ (显式否定 LB/MB 或 LB/IS) |
| Topic 变量值示例 | ✓ (ISTESTCD/MBTESTCD + 完整 Qualifier 链) |
| v3.4 边界规则 | ✓ (9 行归属表 + 3 步决策优先级) |
| 引 IS Assumption 1/2/3/4/5/6/9.b | ✓ (逐 Assumption 链路可查) |
| 补充边界 (CP / MS 等) | ✓ (bonus: 流式→CP; 药敏→MS) |

**Verdict: PASS+** (含全 3 场景 + 完整 Qualifier + 边界规则 9 行表 + 决策优先级 + 补充 CP/MS 边界)

**备注**: Claude v2.6 表现显著优于题目要求 — 主动补出流式→CP、药敏→MS 扩展归属, 以及决策优先级 3 步法. Claude + NotebookLM + ChatGPT Q4 verdict 对齐.
