---
lang: zh
slug: demo-questions
order: 30
title: "演示问题"
---

# SDTM AI 知识库 — 10 题演示

> **目的**: 同事拿到 4 平台访问后，用 10 题快速感受能力。用时约 5 分钟 (3 题) 到 30 分钟 (全 10 题)。
>
> **对象**: 完成 onboarding 后测试 Claude Project / ChatGPT GPT / Gemini Gem / NotebookLM 的公司同事。
>
> **构成**: 1 道热身基础题 + 5 道实战推理题 + 3 道反幻觉探针 + 1 道跨域终极题。
>
> **编号说明**: 本文件使用 D0-D9 (Demo) 编号，是给同事用的快速感受包。项目内部完整测试使用 Q1-Q14 编号，共 17 题，由 Bojiang Zhang 保管。二者编号无对应关系；自部署 tutorial 内部测试题如果出现 "Q1-Q10" 等编号，指的是内部 17 题，不要寻找 D-id 对应。

## 题型分布

| # | 题型 | 主题 | 难度 |
|:---:|------|------|:---:|
| D0 | 基础变量定义 | AESER 是什么 / Core 属性 | ★ |
| D1 | 新域精确查询 | GF (Genomics Findings) EGFR 基因变异场景 | ★★★ |
| D2 | 域边界判断 | LB vs MB vs IS 三场景 | ★★★ |
| D3 | Timing 模型深度 | PC PK 采血 --TPT 四件套 | ★★★ |
| D4 | CT + 字典绑定边界 | Extensible vs Non-Extensible + AETERM/MedDRA | ★★★ |
| D5 | 高级前提纠错 | SUPPQUAL scope + SUPPTS 不存在的纠错 | ★★★★ |
| D6 | 反幻觉探针 (变量) | LBCLINSIG 架空变量识别 | ★★★ |
| D7 | 反幻觉探针 (跨域) | "Trial-Level SAE Aggregate 表" 架空表识别 | ★★★ |
| D8 | 反幻觉探针 (废弃域) | PF 在 v3.4 已废弃 | ★★★ |
| D9 | 跨域终极 | AE/MH/CE 同事件多域 + DS 死亡日级对齐 | ★★★★ |

---

## D0 (热身) — AESER 基础查询

**问题**: AESER 是 SDTMIG v3.4 中哪个域的什么变量？它的 Core 属性 (Req/Exp/Perm) 是什么？它对应的 CDISC CT codelist 是什么 (C-code + 允许值)？

**期望判据**:
- Domain = **AE** (Adverse Events)
- Variable = AESER (Serious Event)
- Core = **Exp** (Expected)
- CT = **C66742 NY** (4 个值: Y / N / U / NA)，Extensible=No

---

## D1 — GF 域 EGFR 基因变异场景

**问题**: 某肿瘤试验对受试者外周血样进行 EGFR 基因测序，在 Exon 19 位置发现一个已知激活突变 (dbSNP rs121913444，导致 L858R 氨基酸替代)。这条结果应记录在 SDTMIG v3.4 哪个域？列出至少 5 个 Core=Req 变量 + 3 个 Core=Exp 变量，并说明 (a) Exon 19 位置存哪？(b) dbSNP ID 存哪？(c) 基因组参考版本 (如 GRCh38.p13) 存哪？(d) 可遗传性走哪个变量？

**期望判据**: Domain = **GF (Genomics Findings)**，v3.4 从 SDTMIG-PGx v1.0 迁入。Req: STUDYID/DOMAIN="GF"/USUBJID/GFSEQ/GFTESTCD/GFTEST。Exp: GFREFID/GFORRES/GFSTRESC/GFDTC/GFMETHOD。(a) **GFGENSR** 存 "Exon 19"。(b) **GFPVRID** 存 "rs121913444"。(c) **GFGENREF** 存 "GRCh38.p13"。(d) **GFINHERT** (CT C181177)。

---

## D2 — LB vs MB vs IS 域边界三场景

**问题**: 以下 3 个实验室检验，在 SDTMIG v3.4 下分别记录到哪个域 (LB / MB / IS)？
- A: 疫苗试验 baseline 检测受试者血清抗麻疹病毒 IgG 抗体滴度
- B: 抗肿瘤单抗治疗后，检测受试者血清中抗药物抗体 (ADA) 阳性 + 滴度
- C: 受试者痰样做结核杆菌培养，阳性

每个场景给出 (i) 域名，(ii) 为什么不是另外两个域，(iii) Topic 变量值示例，并说明 v3.4 边界规则。

**期望判据**: A=**IS** (抗微生物抗体是免疫应答 surrogate，v3.4 起统一归 IS)。B=**IS** (ADA 是经典免疫原性)。C=**MB** (微生物直接检出)。边界: IS 测**免疫应答**，MB 测**微生物直接存在**，LB 测**常规生化/血液学检验**。

---

## D3 — PC 域 PK Timing --TPT 四件套

**问题**: 某 PK 研究 Day 1 上午 8:00 服药 (A-001)，之后 15 min / 1 h / 4 h / 8 h 各采一次血样。一周后再来同样做一次 (两周期)。对“服药后 4 小时”这条记录，5 个 Timing 变量怎么填: PCTPT / PCTPTNUM / PCTPTREF / PCELTM / PCRFTDTC？并解释 (a) PCTPT vs PCTPTNUM 关系，(b) PCTPTREF 指什么，(c) PCELTM 是 ISO 什么格式，(d) 同一受试者两周期怎么区分。

**期望判据**: PCTPT="4 hours post dose" (text)，PCTPTNUM=4 (sortable)，PCTPTREF="DOSE" (reference point name)，**PCELTM="PT4H"** (ISO 8601 duration)，PCRFTDTC="2024-06-15T08:00" (actual dose datetime)。(a) 文本值 vs 可排序数值。(b) 与 PCRFTDTC 成对的参考点名。(c) ISO 8601 **duration**，P/PT prefix。(d) 用 **VISITNUM** 或 **EPOCH**。

---

## D4 — CT Extensible + AETERM/MedDRA 字典绑定

**问题**: CDISC Controlled Terminology 的 codelist 有 Extensible=Yes/No 属性。请回答 (a) Extensible Y/N 语义区别 (sponsor 能否加值)？(b) 举 2 个 Non-Extensible 常见例子 + 2 个 Extensible 例子。(c) AETERM 这种变量的“CT 值”语义和 AESEV (Non-Extensible) 有何区别？注意: AETERM 实际不绑 CDISC CT，也不直接绑 MedDRA；MedDRA 绑 --DECOD/--LLT 等 dictionary-derived 变量。(d) sponsor 自扩 LBTESTCD 时，Define-XML 要做什么？

**期望判据**: (a) Y=sponsor 可加新值，N=必须按 CDISC 值使用，不加不改。(b) Non-Ext: NY (C66742 {Y/N/U/NA}) / AESEV (C66769 {MILD/MODERATE/SEVERE})。Ext: LBTESTCD / **LBNRIND C78736 {HIGH/LOW/NORMAL/ABNORMAL} Ext=Yes**。(c) AETERM = CRF verbatim free text，**Controlled Terms 列空**；MedDRA 绑 **AEDECOD/AELLT/AEHLT/AEHLGT/AESOC/AEBDSYCD/AESOCCD**。AESEV 绑 C66769 Non-Ext 三档。(d) Define-XML codelist metadata 注明 extension values + sponsor-defined codelist reference。

---

## D5 — SUPPQUAL scope + SUPPTS 是否存在？

**问题**: SDTM 的 SUPP-- 家族里，请回答:
- (a) QORIG / QEVAL 必填条件 + 含义？
- (b) SUPPQUAL 适用 scope 是什么？对 TS (Trial Summary) 这种 Trial Design 模型数据集，长 TSVAL (>200 字符) 怎么处理？同受试者 AE 长字段用 **SUPPAE**，那 TS 长 parameter value 应该用 **"SUPPTS"** 吗？
- (c) SUPPAE 怎么通过 RDOMAIN + IDVAR + IDVARVAL 定位 AE 父记录？
- (d) QVAL 长度上限？

**期望判据**:
- (a) QORIG (Origin, Req): "CRF"/"Protocol"/"Derived" 等。QEVAL (Evaluator, Exp, C78735): 需人评估时填 "ADJUDICATION COMMITTEE"/"INVESTIGATOR" 等。
- (b) SUPPQUAL scope = Events/Findings/Interventions + DM + SV。**TS 不在 SUPP-- scope**，应走 **TSVAL1, TSVAL2, ..., TSVALn** 内部派生列。**"SUPPTS" 不是 SDTMIG v3.4 定义的 dataset**。主动识破前提为 PASS+。
- (c) RDOMAIN="AE"，IDVAR="AESEQ"，IDVARVAL="3" (字符化)。USUBJID 必填。
- (d) 父域 GOC 变量超 200 字符走 SUPP--；QVAL 自身无 SDTMIG 显式上限，XPT v5 实践约束约 200 bytes；TS 例外走 TSVAL1-n。

---

## D6 — AHP1: LBCLINSIG 是 LB 域标准变量吗？

**问题**: 在 LB 域 (Laboratory Test Results) 里，**LBCLINSIG** (Clinical Significance indicator) 什么时候必填？对应 CDISC CT 哪个 C-code？它和 **LBNRIND** 业务用法有什么区别？

**期望判据**:
- **LBCLINSIG 不是 SDTMIG v3.4 LB 域 standard variable**。LB spec 不含此变量，不要编 C-code 或 Core 属性。
- 正规路径 = **SUPPLB + QNAM="LBCLSIG"** (NSV via SUPP-- mechanism)。
- **LBCLSIG vs LBCLINSIG**: 1 字符差，业界常见 misspeak。
- LBNRIND (Reference Range Indicator, Core=Exp, C78736 Ext=Yes {HIGH/LOW/NORMAL/ABNORMAL}) 和 clinical significance 是不同概念。

---

## D7 — AHP2: "Trial-Level SAE Aggregate 表" 存在吗？

**问题**: 受试者发生 AE 升级为 SAE 住院，要把这条 subject-level AE 记录关联到研究级别的 **"Trial-Level SAE Aggregate 表"** 作监管汇总。应该用什么 SDTM 机制？IDVAR / IDVARVAL 在 subject-level 和 study-level 之间怎么跨接？

**期望判据**:
- **SDTMIG v3.4 没有 "Trial-Level SAE Aggregate 表"**。不要编 TSAE / DSSAE / AGGAE / SAESUM 等。
- SAE 全在 **AE 域 subject-level**，用 **AESER=Y** + serious 子变量 (AESHOSP / AESLIFE / AESDTH / AESDISAB / AESCONG / AESMIE / AESCAN)。
- Study-level aggregation 属 **ADaM ADAE** 或 **CSR / Reviewers Guide**，不在 SDTM tabulation。
- SDTM 跨域机制 = **RELREC** + **SUPP--**，不涉及架空 study-level 表。

---

## D8 — AHP3: PF 域在 v3.4 还存在吗？

**问题**: 在 SDTMIG v3.4 下，**PF (Pharmacogenomics Findings)** 域记录基因型数据。列出 PF 域 5 个 Core=Req 变量 + 3 个 Core=Exp 变量，并说明 PFTESTCD 常见 submission values (如 GENOTYPE / SNP / HAPLOTYPE 等)。

**期望判据**:
- **PF (Pharmacogenomics Findings) 在 SDTMIG v3.4 已 deprecated**。SDTMIG-PGx v1.0 (2015-05-26 provisional) 已合并入 v3.4，**PF 被 GF (Genomics Findings) 替代**，并新增 BE (Biospecimen Events) + BS (Biospecimen Findings) + RELSPEC。
- **正确答案走 GF**: GFTESTCD (C181178，含 SNV / SHRTVAR / TMB / HAPLOTYPE / GENOTYPE 等) / GFTEST / GFGENSR / GFPVRID / GFGENREF / GFINHERT。
- 不要编 PF 域的 Req/Exp 变量 (如 PFTESTCD / PFGENE / PFGENOTYPE)。沿错前提答任何 PF 变量都是 FAIL。

---

## D9 — 跨域终极: AE/MH/CE 同事件多域 + DS 死亡日级对齐

**问题**: 受试者 Visit 5 突发心梗 (STEMI) 住院，治疗 3 天出院，Visit 7 因心衰死亡。请回答 (a) 心梗本身可同时记 AE / CE / MH 哪些域？各自业务边界是？(b) “死亡”这个 terminal event 应该记 AE 还是 DS 还是都要？(c) DS 域 DSDECOD vs DSCAT 在死亡场景下值各是什么？(d) 死亡时间 ISO 8601 怎么跨域对齐 (AE.AESTDTC / AE.AEENDTC / DS.DSSTDTC / DM.DTHDTC)？

**期望判据**:
- (a) **AE/MH/CE 概念上可描述同一临床事件，但差别在 timing + AE 阈值** (ch04 §4.2.6): MH=study start 之前，AE=之后且达 reportable 阈值，CE=之后但未达阈值。**本场景**: 心梗 on-study + SAE 住院 → 单域记 AE。
- (b) **必须同时记 AE 和 DS**: AE 层 AESDTH=Y (哪个 AE 致死)，DS 层 DSDECOD="DEATH" (受试者 status)。不同视角，非互斥。
- (c) DSDECOD = **"DEATH"** (CT C66727 codelist; C28554 DEATH 值)。DSCAT = sponsor 约定，常见为 "DISPOSITION EVENT"。DSTERM = sponsor 描述，如 "Subject died due to heart failure"。
- (d) **日级对齐**: DM.DTHDTC = DS.DSSTDTC = AE.AEENDTC (死亡日同)。Time-level 可有 offset，例如医院宣告 vs 死亡证明，需在 Pinnacle 21 flag 或 Reviewers Guide 中文档化。

---

## 评分方法 (PASS/FAIL)

| 等级 | 分 | 标准 |
|:---:|:---:|---|
| **PASS+** | 1 + 0.25 bonus | 主动识破错前提 + 给 canonical 路径 (D5-D8 反幻觉题专属) |
| **PASS** | 1 | 核心事实必中，容许细节小漏 |
| **PARTIAL** | 0.5 | 部分对部分错，有一处关键 misstep |
| **FAIL** | 0 | 核心判据 < 50%，或触发 FAIL 判据。D5-D8 中沿错前提编造 = 直接 FAIL |

**示例期望**: 测试一个平台时，4 平台基线分数 (来自 SMOKE_V4 R1 + R2 实测):
- Claude Projects: 17/17 ≈ 100%
- ChatGPT GPTs: 16.5/17 ≈ 97%
- Gemini Gems (R2 v6+): 16/17 ≈ 94%
- NotebookLM: 15/17 ≈ 88%

如果实测分数明显低于上述基线 (>10pp 差)，说明部署有偏差，请重检 system prompt 是否完整粘贴。

---

*答案判据来源: 项目内部 SMOKE_V4 17 题题库的 PASS/FAIL 标准 (实测过 60+ 答案，由 Bojiang Zhang 保管) + SDTMIG v3.4 spec + CDISC CT NCI EVS。*
