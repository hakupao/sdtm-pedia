# Smoke v3 题库 draft — N5.3 Full A/B Generalization Probe

> **版本**: v3.1 (2026-04-22, reviewer fix post Step 3)
> **v3.0 → v3.1 修改** (双 reviewer 独立审后主 session 修):
> - Q3 PASS (a): "采血=BS 不是 BE" → "采血行为=BE BECAT=COLLECTION + 采血测量=BS 并存" (ChatGPT reviewer HIGH, KB BE/spec.md BECAT "Example: COLLECTION" 明文支持)
> - Q3 FAIL: 删除 "采血记在 BE (错)" → 改为 "采血测量值记在 BE (错, Findings vs Events)"
> - Q4 FAIL (场景 A): 添加 PARTIAL 保护 "答 MB 但理由含免疫应答 → PARTIAL 非 FAIL" (Gemini reviewer HIGH, 跨版本记忆风险缓冲)
> - Q5 题目 + PASS + FAIL: 场景 A 从 "FA 指向 AE 头痛" reframe 为 "FA 指向 MH DAS28 评分" (04 §1.19 主覆盖 FA→AE, 非 FA→MH); 场景 C 从 "疲劳 unscheduled visit" reframe 为 "轻微头晕 30 秒自愈" (CE 边界更清晰, 降 04 重叠 35-40% → 目标 <25%)
> - Q10 PASS (d) + FAIL: "QVAL 200 字符上限 §8.4" 归因改为 "ch04 §4.5.3.2 父域 GOC 变量拆分机制; QVAL 自身无 SDTMIG 显式业务长度" (两 reviewer 交叉共识 HIGH)
> - Q14 PASS (c): DSDECOD CT code C66728 → **C66727** (C66728 是 Relation to Reference Period, 错归; C66727 是 Disposition From Study); DSCAT 从 "CT 强制" → "sponsor 约定非 CT 强制" (ChatGPT reviewer MED)
>
> **v3.0 原版**: 2026-04-21
> **基础**: N5_3_QUESTIONS_DESIGN.md + 联网 WebSearch × 6 + WebFetch × 4 (IS scope 精华) + 本地 KB GF/CP/BE/BS/IS/SV spec × 6
> **起因**: N5.2 双平台等价 10/10 PASS, 但 smoke v2.1 10 题全落入 04 §1.1-§1.10 预设 scenario → generalization probe 设计
> **双平台共用**: 10 题 (Q1-Q10), **ChatGPT 专属**: 4 题 (Q11-Q14)
> **合格阈**: ChatGPT ≥ 10/14 (71%), Gemini ≥ 7/10 (70%)
> **04 非重叠**: 每题成稿后反向 grep 04, 重叠 >30% 换题
> **题源锚点**: 每题末尾列 KB 源文件 + 联网源 URL

---

## 题型分布 (最终)

| # | Type | 主题 | 平台 |
|---|------|------|:---:|
| Q1 | A1 v3.4 新域 | GF (Genomics Findings) 基因变异场景 | 双平台 |
| Q2 | A2 v3.4 新域 | CP (Cell Phenotype) 流式细胞场景 | 双平台 |
| Q3 | A3 v3.4 新域 | BE + BS + RELSPEC 生物样本全流程 | 双平台 |
| Q4 | B1 域边界 | LB vs MB vs IS 三场景归属 | 双平台 |
| Q5 | B2 域边界 | FA vs QS vs CE 三场景归属 | 双平台 |
| Q6 | C1 Timing 深化 | --TPTREF/--TPT/--STTPT/--ENTPT/--DUR 组合 | 双平台 |
| Q7 | C2 Timing 深化 | Partial date 精度 + imputation 规则 | 双平台 |
| Q8 | D1 CT 深化 | Extensible vs Non-Extensible codelist | 双平台 |
| Q9 | E1 实战验证 | Pinnacle 21 常见 FAIL 分类 | 双平台 |
| Q10 | H1 SUPP 深化 | QORIG/QEVAL/QLABEL + SUPPTS vs SUPP-- | 双平台 |
| Q11 | F1 新技术 | Dataset-JSON v1.1 vs XPT v5 submission | **ChatGPT 专属** |
| Q12 | D2 CT 深化 | CT 版本锁定 + AETERM 跨版本一致性 | **ChatGPT 专属** |
| Q13 | G1 RWD | Observational/RWD conformance 失效 + NS 域 | **ChatGPT 专属** |
| Q14 | I1 跨域 | 同一临床事件 AE+CE+MH 共记 + DS 死亡记录 | **ChatGPT 专属** |

---

# 10 题全文 (双平台共用)

---

## Q1 (A1 — GF 域) EGFR 基因变异场景

> **题**: 某肿瘤试验对受试者外周血样进行 EGFR 基因测序, 在 Exon 19 位置发现一个已知的激活突变 (dbSNP rs121913444, 导致 L858R 氨基酸替代). 这条结果应该记录在 SDTMIG v3.4 的哪个域? 请列出该记录至少 **5 个 Core=Req 变量** 和 **3 个 Core=Exp 变量** (按 Topic 变量优先), 并说明: (a) 如何记录"Exon 19"位置信息; (b) 如何引用 dbSNP ID; (c) 基因组参考版本 (比如 GRCh38.p13) 存哪; (d) 如果该变异可遗传给下一代, 走哪个变量.

**PASS 判据 (核心事实必中)**:
- 正确识别域为 **GF (Genomics Findings)** (v3.4 新增, 从 SDTMIG-PGx v1.0 迁入), 不是旧 PF 或 LB
- Core Req 至少列: STUDYID / DOMAIN="GF" / USUBJID / **GFSEQ** / **GFTESTCD** / **GFTEST** (任 5)
- Core Exp 至少列: **GFREFID** (assayed genetic specimen ID) / **GFORRES** / **GFSTRESC** / **GFDTC** / **GFMETHOD** / VISITNUM (任 3)
- (a) **GFGENSR** (Genetic Sub-Region, 示例 "Exon 15" / "Kinase domain") 存 "Exon 19"
- (b) **GFPVRID** (Published Variant Identifier) 存 "rs121913444" (dbSNP ID)
- (c) **GFGENREF** (Genome Reference) 存 "GRCh38.p13"
- (d) **GFINHERT** (Inheritability, CT C181177) 指示可否遗传

**FAIL 判据**:
- 答成 LB 或 PGx/PF 旧域 (v3.4 已废 PGx)
- 臆造变量如 GFGENE / GFVARIANT (其实是 GFSYM / GFORRES)
- GFCHROM (染色体号) 和 GFGENSR (基因内区域) 弄混
- 说 GFINHERT 不存在

**KB 源锚点**: `knowledge_base/domains/GF/spec.md` L104-299 (GFTESTCD/GFGENSR/GFPVRID/GFGENREF/GFINHERT 定义) + SDTMIG v3.4 §6.3.5.5 Genomics Findings

**04 非重叠检查**: 04 无 §GF 章节, 无 "GFTESTCD / GFGENSR / GFPVRID" 关键字, Pure generalization ✅

**联网源**:
- [CDISC SDTMIG v3.4 GF Domain Intro](https://www.cdisc.org/sites/default/files/pdf/IntroToGFDomain-Webinar_0.pdf)
- [PhUSE 2025 DS11 — Evolution of Genomic Data Mappings PF→GF](https://www.lexjansen.com/phuse-us/2025/ds/PAP_DS11.pdf)

---

## Q2 (A2 — CP 域) 流式细胞测 CD4+ T 细胞 ACTIVATED 亚群

> **题**: 某免疫治疗试验用流式细胞仪检测受试者 PBMC 样本里 "活化的 CD4+ T 辅助细胞" (通过 Ki67+ 表达识别为 ACTIVATED 状态). SDTMIG v3.4 里这个测量属于哪个域? 请说明: (a) Topic 变量是什么; (b) 如何区别"T Lym Help" 这个**命名**细胞群与 CD4+Ki67+ 这个**子集**亚群; (c) 用哪些变量记录"哪些 marker 被用来定义'活化'状态"; (d) Method 变量应填什么 (测量方法); (e) 这个域和 LB 的边界是什么.

**PASS 判据**:
- 正确识别为 **CP (Cell Phenotype Findings)** 域 (v3.4 新增)
- (a) Topic: **CPTESTCD** (Req, 例 "CD4THLP" 或 "CD4HELP") + **CPTEST** (例 "T Lym Help")
- (b) 命名群: CPTEST="T Lym Help"; 子集: CPTEST 加 "Sub" 后缀 (e.g., "T Lym Help Sub") + **CPSBMRKS** (Sublineage Marker String, 例 "CD4+Ki67+") 存具体 marker 组合
- (c) **CPCELSTA** (Cell State, C181172, 值 "ACTIVATED") + **CPCSMRKS** (Cell State Marker String, 例 "Ki67+") 说明 Ki67 表达定义 activation
- (d) **CPMETHOD** = "FLOW CYTOMETRY" (C85492)
- (e) 边界: CP 专用于基于**细胞群特征** (marker 表达) 的单细胞/颗粒悬液测量, LB 是血生化/血常规等传统实验室检查. CP 共享一些 marker/binding 变量 (如 CPBDAGNT) 与 IS/LB 但 Topic 性质不同.

**FAIL 判据**:
- 答 LB 或 IS 或自创 FC 域
- CPSBMRKS vs CPCELSTA 概念弄混 (sublineage marker 定义**亚群** vs cell state marker 定义**状态**)
- 漏 Sub 后缀规则 (子集必须 Sub 后缀)
- Method 答 "PCR" 或 "ELISA" (非流式)

**KB 源锚点**: `knowledge_base/domains/CP/spec.md` L86-193 (CPTESTCD/CPTEST/CPSBMRKS/CPCELSTA/CPCSMRKS/CPMETHOD 定义)

**04 非重叠**: 04 仅 §22.3 "CP + GF 分子/基因组" 一行提过, 无深入. Pure generalization ✅

---

## Q3 (A3 — BE + BS + RELSPEC) 生物样本从采集到 DNA 提取

> **题**: 某 PGx 试验, 受试者 Visit 2 现场采集血样 (BS-001), 当天运输到中心实验室 (运输过程记为一个事件), 第二天从 BS-001 样本提取 DNA 得到 DNA-001 子样本. 请说明: (a) 这三个"阶段" (采血 / 运输 / DNA 提取) 分别记录在哪些域? (b) 血样的"体积 = 5 mL"和"RNA 完整性数 (RIN) = 9.2"这两个**测量**记录在哪个域, 对应 Topic 变量值分别是什么; (c) BS-001 → DNA-001 这种**样本派生关系**怎么表达? 应该用哪个 Dataset (RELREC 还是另一个)?

**PASS 判据**:
- (a) **采血行为** = **BE** (BECAT="COLLECTION", BE 记采集**事件**) + **采血测量** (体积/RIN) = **BS** (Biospecimen Findings, BE 和 BS 并行不互斥); 运输 = **BE** (BETERM="TRANSPORT"); DNA 提取 = **BE** (BETERM="PREPARATION" 或 "EXTRACTION"). KB BE/spec.md BECAT Notes 明文列 "Example: COLLECTION, PREPARATION, TRANSPORT"
- (b) 血样测量在 **BS**:
  - 体积: BSTESTCD="VOLUME", BSTEST="Volume", BSORRES="5", BSORRESU="mL"
  - RIN: BSTESTCD="RIN", BSTEST="RNA Integrity Number", BSORRES="9.2"
  - (Topic 变量 BSTESTCD, C124300 官方支持 VOLUME / RIN)
- (c) 样本派生关系用 **RELSPEC** (Related Specimens) 域, 不用 RELREC (RELREC 是跨 general observation class 记录关系, RELSPEC 是 specimen 之间的层级关系)
- 补充加分: BEREFID / BSREFID 指向 specimen ID

**FAIL 判据**:
- 把 BS 和 BE 混淆 (Findings vs Events)
- 说用 RELREC 记 specimen hierarchy (错, 应 RELSPEC)
- Topic 变量用 "VOL" 或 "RNAINT" (错, 官方 CT C124300 是 VOLUME / RIN)
- 把采血**测量值** (体积/RIN) 记在 BE (错, Findings 测量数据不是 Events; 采血行为可记 BE COLLECTION, 但测量值必走 BS)

**KB 源锚点**: 
- `knowledge_base/domains/BE/spec.md` L77-148 (BETERM/BECAT 定义 + Examples COLLECTION/PREPARATION/TRANSPORT)
- `knowledge_base/domains/BS/spec.md` L77-129 (BSTESTCD C124300 Examples: VOLUME, RIN)
- Cross-ref `BS/spec.md` L337 Specimen Relationship → RELSPEC

**04 非重叠**: 04 仅 §1.25 提 "BE 和 MB/MS 微生物" 一行. ✅

**联网源**:
- [SDTMIG-PGx v1.0 (deprecated, 现迁入 SDTMIG v3.4)](https://www.cdisc.org/standards/foundational/pgx-sdtmig/sdtmig-pgx-v1-0)

---

## Q4 (B1 — LB vs MB vs IS 边界) 三场景选域

> **题**: 以下 3 个实验室检验结果, 在 SDTMIG v3.4 下分别记录到哪个域 (LB / MB / IS)?
>
> **场景 A**: 疫苗试验, baseline (入组当日) 检测受试者血清中抗麻疹病毒 IgG 抗体滴度 (测过往感染或接种史), 数值 1:128
> **场景 B**: 抗肿瘤单抗治疗后, 受试者血清中检测抗药物抗体 (ADA) 阳性/阴性 + 滴度
> **场景 C**: 受试者痰样做结核杆菌 (Mycobacterium tuberculosis) 培养, 结果 positive
>
> 每个场景给出: (i) 域名; (ii) 理由 (为什么不是另外两个域); (iii) Topic 变量值示例. v3.4 下边界规则是什么?

**PASS 判据**:
- **场景 A** (抗麻疹病毒 IgG baseline): **IS** (Immunogenicity Specimen). 理由: 测 "对抗原暴露的免疫应答" (抗体水平), v3.4 起 anti-microbial antibody 无论 baseline 与否都归 IS (过去 v3.3 baseline 在 MB, v3.4 统一到 IS). Topic: ISTESTCD="MEASIGG" 或 "MVIGG", ISBDAGNT="Measles virus"
- **场景 B** (ADA): **IS** (无歧义). 理由: 抗药物抗体是经典免疫原性测量, IS 域是为此设计. Topic: ISTESTCD (ADA codelist), ISBDAGNT=药物名
- **场景 C** (Mtb 培养): **MB** (Microbiology Specimen). 理由: MB 测 "微生物直接检出" (培养 / PCR / 染色), 不是 surrogate 抗体. Topic: MBTESTCD="MTBCULT" 或类似
- v3.4 边界规则: IS 测**免疫应答** (抗体/免疫细胞/细胞因子, 不管触发因素), MB 测**微生物直接存在** (培养/PCR/染色/抗原检出), LB 测**常规血生化/血液学** (肝肾功能/电解质/血常规)

**FAIL 判据**:
- A 答 MB (v3.2/v3.3 旧规则, 忽略 v3.4 scope 变化) — **若答 MB 但理由含 "免疫应答/antibody surrogate" 关键词 → PARTIAL (非完全 FAIL), KB IS assumption 2 有原材料但版本迁移规则无显文; 若无理由或答 "直接检出" → FAIL**
- A 答 LB (错, 抗体不是常规生化)
- C 答 IS (错, 直接检出微生物不是免疫应答)
- B 答 LB (错, ADA 是免疫应答不是常规生化)
- 不给理由或边界规则

**KB 源锚点**: `knowledge_base/domains/IS/spec.md` L122 ISBDAGNT + IS/assumptions.md + 联网 CDISC IS Scope Update article

**04 非重叠**: 04 仅 §1.25 BE+MB 提过, 无 LB/MB/IS 三域 scope 对比. ✅

**联网源**:
- [CDISC — IS Domain Scope Update for SDTMIG v3.4](https://www.cdisc.org/kb/articles/domain-scope-update-sdtmig-v3-4-development-history-and-difficulties-standardizing)
- [CDISC — Where Does My Lab Data Go in SDTMIG v3.4](https://www.cdisc.org/kb/articles/where-does-my-lab-data-go-sdtmig-v3-4)
- [CDISC Webinar — LB/MB Scope Changes](https://www.cdisc.org/events/webinar/lb-mb-domain-scope-changes-sdtmig-v3-4-and-impact-controlled-terminology)

---

## Q5 (B2 — FA vs QS vs CE 边界) 三场景选域

> **题** (v3.1 reframe reduce 04 §1.19 overlap): 以下 3 条 EDC 收集信息, 分别映射到 FA / QS / CE 哪个 SDTM 域?
>
> **场景 A**: 受试者有既往 MH "类风湿性关节炎 15 年", 研究者在 Visit 4 对这条既往 MH 记录做量化评分 (用 28-joint tender/swollen count, 记 DAS28 评分 4.2). 这是对**既往 MH 记录**的量化 findings (非针对 AE).
> **场景 B**: 受试者在 Visit 4 填 SF-36 生活质量问卷, 8 个维度每个打分
> **场景 C**: 受试者自诉 Visit 5 出现轻微头晕 (dizziness, 30 秒自愈), 研究者记录但不认为需医疗处理, 未达 AE 报告阈值
>
> 每个场景: (i) 域名 + (ii) 理由 + (iii) Topic 变量值示例

**PASS 判据**:
- **A**: **FA** (Findings About). 理由: FA 专为"关于某个已存在 Event/Intervention/Finding 记录的 additional findings"设计, Topic 是 FATESTCD (measurement about an existing record), 配合 **FAOBJ 指向 MH 记录** (不是 AE). 不用 QS (QS 是独立患者报告问卷, DAS28 是临床评估非 patient-reported). 不用 SUPPMH (SUPPMH 是单条 MH 加非标字段, FA 是结构化独立评估记录).
- **B**: **QS** (Questionnaires). 理由: QS 专门记标准化问卷仪器 (SF-36 / EORTC / PROMIS). Topic: QSTESTCD (e.g., "QSPF01"), QSCAT="SF-36", QSSCAT=各 domain. 不用 FA.
- **C**: **CE** (Clinical Events). 理由: CE 记录不到 AE 阈值但临床相关的事件 ("meaningful clinical events that are not AE"). 不用 AE (未达标), 不用 DV (DV 是 protocol deviation 非临床事件).

**FAIL 判据**:
- A 答 QS (错, DAS28 不是独立问卷而是对既往病史的临床评估, 走 FA)
- A 答 SUPPMH (错, SUPPMH 是非标字段补充, FA 是结构化独立评估)
- B 答 FA 或 CE
- C 答 AE (明确未达 AE 阈值) 或 DV (DV 是协议偏离非临床事件)

**KB 源锚点**: `knowledge_base/domains/FA/` + `knowledge_base/domains/QS/` + `knowledge_base/domains/CE/` (本题要求跨域鉴别)

**04 非重叠**: 04 §1.19 "QS vs FA" 已提过, 本题加 CE 三元鉴别 — 04 未覆盖三元. borderline ⚠️ (需 reframe: 可能强调 CE 维度判断, 若 reviewer 判 >30% 重叠则改)

**联网源**: SDTMIG v3.4 §6.3.11 (FA) + §6.3.17 (QS) + §6.2.4 (CE)

---

## Q6 (C1 — Timing 深化) PK 定时采血 --TPT 四件套

> **题**: 某 PK 研究的访视日安排: 受试者上午 8:00 服用研究药物 (A-001), 之后 15 min / 1 h / 4 h / 8 h 各采一次血样用于 PK. 一周后再来同样做一次 (两周期). 请说明 PK 域 (PC 域) 里, 对"服药后 4 小时采血"那一条记录, 下列 5 个 Timing 变量应怎么填:
>
> PCTPT / PCTPTNUM / PCTPTREF / PCELTM / PCRFTDTC
>
> 并解释: (a) PCTPT vs PCTPTNUM 关系; (b) PCTPTREF 指什么; (c) PCELTM 是 ISO 什么格式; (d) 同一受试者两周期记录用什么区分.

**PASS 判据**:
- **PCTPT** (Planned Time Point Name, 文字): "4 hours post dose" / "4 HR POST DOSE" (文字可读)
- **PCTPTNUM** (数字版用于排序): 例如 "4" (或 4; 排序整数, 15min=1, 1h=2, 4h=3, 8h=4 也可)
- **PCTPTREF** (Time Point Reference): "DOSE" 或 "PREVIOUS DOSE" 或 "STUDY DRUG DOSE" (名字指向 fixed reference point)
- **PCELTM** (Planned Elapsed Time): **ISO 8601 duration 格式** = "PT4H" (P=period, T=time, 4H=4 hours)
- **PCRFTDTC** (Date/Time of Reference): 实际服药时间 ISO 8601 datetime, 例 "2024-06-15T08:00"
- (a) PCTPT 是文字标识 (排序差), PCTPTNUM 是数字用于排序
- (b) PCTPTREF 给一个**名字** (reference point name), 与 PCRFTDTC 实际 datetime 成对
- (c) PCELTM 是 **ISO 8601 duration** (P/PT 前缀, 不是 datetime)
- (d) 两周期用 **VISITNUM** 区分 (Cycle 1 vs Cycle 2 两个 visit), 或用 **EPOCH** (C99079) 区分治疗阶段

**FAIL 判据**:
- PCELTM 写成 "4 hours" 或 "04:00:00" (错, 必须 ISO duration "PT4H")
- PCTPTREF 写成 datetime (错, 是 name, datetime 在 PCRFTDTC)
- 混淆 Planned (TPT/TPTNUM/ELTM/TPTREF) 与 Actual (RFTDTC + STDTC); 4 个计划变量独立于 PCSTDTC (实际采血时)
- 用 VISITDY 区分两周期 (错, VISITDY 可能相同)

**KB 源锚点**: `knowledge_base/domains/PC/spec.md` (PC 域完整 Timing); 本题可参考 GF/CP Timing (PCTPT 模板和 GFTPT 镜像)

**04 非重叠**: 04 §4.3 Timing 基础提过 --STDTC/--ENDTC/--DY 但 **未深入 --TPT/--TPTREF/--ELTM/--RFTDTC 四件套**. ✅

---

## Q7 (C2 — Partial date) EDC 只给部分日期怎么填

> **题**: ISO 8601 datetime 变量 (e.g., AESTDTC, CMSTDTC) 允许**部分精度**. 下列 3 个场景, 各应怎么填? SDTMIG v3.4 对 partial date 有没有 imputation 规则 (SDTM 级还是 ADaM 级)?
>
> **场景 A**: EDC 只收到 "AE 开始于 2024 年 6 月" (无日)
> **场景 B**: EDC 只收到 "服药开始于 2024 年" (无月日)
> **场景 C**: EDC 完全没收到 AE 开始日 (Unknown)
>
> 另外回答: (d) SDTM 的 --STDTC 需要做 imputation 吗? (e) 如果 ADaM 需要 imputation, SDTM 还需要额外记什么吗?

**PASS 判据**:
- **A** (年月): AESTDTC = "**2024-06**" (ISO 8601 部分精度只到月)
- **B** (年): AESTDTC = "**2024**" (只到年)
- **C** (完全未知): AESTDTC = **null / 空** (不能填 "UNKNOWN" 字符串, 必须 null)
- (d) **SDTM 级不做 imputation** — SDTM 保留原始精度, 不因后续分析需要而猜月/日. Imputation 是 **ADaM 级** (ADSL / ADAE 等分析数据集派生 imputed date 存 ADT 类变量, 并记 ADTF imputation flag).
- (e) SDTM 可用 SUPPAE 存 imputation 相关 supplemental qualifier (比如 "Onset date reported as: June 2024"), 或用 -DY 留空. 绝对**不要在 --STDTC 内自己补 01 或 1st**.

**FAIL 判据**:
- 场景 A 答 "2024-06-01" 或 "2024-06-15" (错, imputation 不是 SDTM 职责)
- 场景 C 答 "1900-01-01" 或 "UNKNOWN" (错, 空值必须 null)
- 说 SDTM 做 imputation (错, SDTM 保真, ADaM imputation)
- 不识 ISO 8601 部分精度 (只写 full datetime)

**KB 源锚点**: `knowledge_base/chapters/ch04_general_assumptions.md` (ISO 8601 + partial date 规则)

**04 非重叠**: 04 §1.8 / §2.9 提过 ISO 8601 基础, 但 **未深入 imputation SDTM vs ADaM 职责边界**. ✅

---

## Q8 (D1 — CT Extensible vs Non-Extensible)

> **题**: CDISC Controlled Terminology 的每个 codelist 有 **Extensible = Yes/No** 属性. 请回答: (a) Extensible=Yes 和 Extensible=No 语义区别是什么 (sponsor 能否加自己的值)? (b) 举 2 个 **Non-Extensible** 的常见 codelist 例子 (必须完全按 CDISC 用), 和 2 个 **Extensible** 的例子 (允许扩); (c) AETERM 这种变量"CT 值"语义和 AESEV (Non-Extensible) 有什么区别 (AETERM 实际用 MedDRA 字典, 不是 CDISC CT); (d) 如果 sponsor 自己扩 LBTESTCD, Define-XML 要做什么?

**PASS 判据**:
- (a) **Extensible=Yes** 允许 sponsor 在 CDISC CT 基础上**加新的 submission value** (通常加在 codelist 末尾, 不改已有值); **Extensible=No** 必须完全按 CDISC CT, 不加不改
- (b) Non-Extensible 例子: **NY (No/Yes) C66742 {Y, N, U}** / **AESEV C66769 {MILD, MODERATE, SEVERE}** / **LBNRIND C78736 {HIGH, LOW, NORMAL, ABNORMAL}** (任 2)
- (b) Extensible 例子: **LBTESTCD / LBTEST** (常规实验室测试名, sponsor 可加自己的) / **MBTESTCD / MBTEST** / **ROUTE (C66729 Route of Admin, 不限)** (任 2)
- (c) **AETERM** (Reported Term for AE) 不受 CDISC CT 限制, 使用**外部字典 MedDRA** (非 CDISC CT); AEDECOD (AE Dictionary Derived) 是 MedDRA 的 LLT/PT; 这是"外部词典"而非 CDISC 内部 CT 概念. AESEV 使用 CDISC CT (C66769 Non-Extensible) 三档固定.
- (d) sponsor 扩 LBTESTCD 时, Define-XML 必须在 codelist metadata 中注明 extension values + sponsor-defined codelist reference

**FAIL 判据**:
- 混淆 Extensible / Non-Extensible 语义 (反着说)
- 说 AETERM 用 CDISC CT (错, 用 MedDRA 外部字典)
- AESEV 说是 Extensible (错, Non-Extensible 三档固定)
- Define-XML 作用不提

**KB 源锚点**: `knowledge_base/chapters/ch05_controlled_terminology.md` + `terminology/core/general_part4.md` (AESEV C66769, LBNRIND C78736)

**04 非重叠**: 04 §1.15 "Controlled Terminology Extensible vs Non-Extensible" 标题提过但内容仅一句, **未深入 MedDRA 外部字典边界 + Define-XML**. borderline ⚠️ (reframe: 强调 MedDRA 边界 + Define-XML)

---

## Q9 (E1 — Pinnacle 21 常见 FAIL 分类)

> **题**: Pinnacle 21 (OpenCDISC Validator) 是 FDA 审查 SDTM 数据时常用的验证工具, 对一份 SDTM 数据会返回 Errors / Warnings / Notices 三级 issue. 请按**类型分类**列举 **5-6 大类**常见 FAIL, 每类举 **1 个典型触发例子**, 并说明: 遇到 Pinnacle 21 FAIL 时, 什么时候应该**修数据**, 什么时候应该**在 Reviewers Guide 文档化并保留**不修?

**PASS 判据 (必含 5 大类, 合理即 PASS)**:
1. **Date consistency** (日期逻辑): 例如 AESTDTC > AEENDTC, 或 EXSTDTC < RFXSTDTC. 应修 (真错).
2. **Controlled Terminology compliance**: 例如 AESEV="MODERATE " (尾空格) 或 AESEV="SEV" (非 codelist 值). 应修.
3. **Required / Expected variable 缺失**: 例如 AE 域 STUDYID 空, DM 域 USUBJID 空. 应修.
4. **Duplicate records**: 例如同一 USUBJID + --SEQ 出现两条. 应修 (--SEQ 必须唯一).
5. **Orig vs Std units / numeric vs character 类型错**: 例如 LBSTRESN = "6.8%" (numeric 列带字符) 或 LBORRES 空 但 LBSTRESC 填了. 应修.
6. (可选) **Value-level consistency**: 例如 AESER=Y 但所有子变量 (AESHOSP/AESLIFE/AESCONG/AESMIE 等) 全空. 边界 case, 可文档化.
- **应修 vs 文档化决策原则**: 如果是**真实数据错** (比如 EDC entry 错, 日期倒序) → 修. 如果是**标准不匹配但数据是真实** (比如 RWD 场景没有 planned arm, 或小儿 BMI 不适用成人 range, 或 sponsor-defined codelist legit extension) → 在 **Reviewers Guide** / **csdrg.pdf** 文档化解释, 保留 issue, 不改数据.

**FAIL 判据**:
- 只列 ≤3 大类
- 混淆 Error / Warning / Notice 等级
- 说"所有 FAIL 必修" (错, 有些该文档化保留)
- 给具体虚构 rule ID (比如答 "SD9999") — 不要求具体 ID, 要求分类合理

**KB 源锚点**: 本题不走 KB, 靠业务常识 + Pinnacle 21 常识

**04 非重叠**: 04 **0 覆盖 Pinnacle 21**. Pure generalization ✅

**联网源**:
- [Pinnacle 21 SDTM Validation Rules](https://standards.pinnacle21.certara.net/validation-rules/sdtm)
- [Pinnacle 21 by Certara — SDTM Mapping Process Simplified](https://www.certara.com/blog/the-sdtm-mapping-process-simplified/)
- [PharmaSUG 2019 DS-119 — Common Pinnacle 21 Report Issues: Shall we Document or Fix?](https://www.lexjansen.com/pharmasug/2019/DS/PharmaSUG-2019-DS-119.pdf)

---

## Q10 (H1 — SUPP 深化) QORIG/QEVAL/QLABEL + SUPPTS vs SUPP--

> **题**: SDTM 的 SUPP-- (Supplemental Qualifiers) 家族里, 请回答:
>
> (a) 每条 SUPP 记录有 QNAM / QLABEL / QVAL / **QORIG** / **QEVAL** 5 个关键字段. QORIG 和 QEVAL 什么时候**必填**, 什么时候**不填**? 含义分别是?
> (b) **SUPPTS** (SUPP for Trial Summary) 和 **SUPPAE** (SUPP for AE) 的**层级**区别是什么? (subject-level vs study-level)
> (c) 一条 SUPPAE 记录如何通过 RDOMAIN + IDVAR + IDVARVAL 定位到**具体**的 AE 父记录? USUBJID 怎么用?
> (d) QVAL 长度上限是多少? 超过怎么拆?

**PASS 判据**:
- (a) **QORIG** (Origin): 必填. 指 QVAL 来源, 值可为 "CRF" / "Protocol" / "Derived" / "Assigned" / "eDT" / "Investigator" 等. **QEVAL** (Evaluator): 当 QVAL 需人评估时填 (如 "ADJUDICATION COMMITTEE" / "INVESTIGATOR" / "SPONSOR"); 纯机器/CRF 录入时可不填.
- (b) **SUPPTS** 是 **study-level** supplemental (TS 域是 Trial Summary, 研究级别 parameter, SUPPTS USUBJID **可为空或 STUDYID 级**); **SUPPAE** 是 **subject-level** (每条 SUPP 记录必含 USUBJID + AE 父记录的 --SEQ).
- (c) SUPPAE: RDOMAIN = "AE"; IDVAR = "AESEQ" (通常, 也可 AEGRPID); IDVARVAL = 具体的 AESEQ 值 (字符化, e.g., "3"). USUBJID 必填 (subject-level). 三字段联合定位父 AE 记录.
- (d) **超长文本处理** (ch04 §4.5.3.2 正确归因): 父域 GOC 变量 (如 AETERM / CMTRT) 超 200 字符时按拆分规则 — 前 200 字符留父域, **超出部分按顺序写入 SUPP-- QVAL** (同一 QNAM 加数字后缀如 QNAM1/QNAM2). QVAL 自身**无 SDTMIG 显式业务长度规定**, 实践受 SAS XPT v5 字段约束 (~200 字节). 200 字符是父域 GOC 变量上限, 不是 QVAL 自身硬性上限.

**FAIL 判据**:
- QORIG 与 QEVAL 语义反
- SUPPTS 和 SUPPAE 层级弄错
- IDVAR / IDVARVAL 用法错 (e.g., 说 IDVAR="USUBJID")
- 错答 "QVAL 本身有 200 字符硬上限" (归因错; 200 是父域 GOC 变量拆分阈值, 不是 QVAL 自身限制). 错答 40 或 500 也 FAIL.

**KB 源锚点**: `knowledge_base/chapters/ch08_relationships.md` + `knowledge_base/domains/SUPP*/` (SUPP 家族)

**04 非重叠**: 04 §1.9 SUPPAE 基础题, §19 SUPPQUAL 深化有 QNAM/QLABEL 基础. **未深入 QORIG/QEVAL/SUPPTS vs SUPP--**. borderline ⚠️ (reframe: 强调 QORIG/QEVAL + SUPPTS 层级, 04 未覆盖这两个角度)

---

# 4 题 ChatGPT 专属 (Q11-Q14)

---

## Q11 (F1 — Dataset-JSON v1.1 vs XPT v5) ChatGPT 专属

> **题**: 2025 年 FDA 启动 Dataset-JSON 试点, CDISC 发布 Dataset-JSON v1.1. 请说明: (a) Dataset-JSON 相比 SAS XPT v5 主要解决什么 4-5 个**技术痛点**? (b) 2026 年现状: FDA 接受哪个? (c) 作为 SDTM 程师, 现在实操建议是什么 (开发环境 / 归档 / 提交)? (d) Define-XML 和 Dataset-JSON 互补关系是什么?

**PASS 判据**:
- (a) XPT 痛点 5 项任 4: **变量名长度限制 8 字符** / **字段值 200 字符上限** / **无 Unicode 支持** / **无 metadata 扩展** (Define-XML 必须外挂) / **存储低效 (binary 不可读不可 diff)** / **数据类型有限** (只 num/char)
- (b) 现状: **XPT v5 仍是 FDA 必需**直到 Dataset-JSON 加入 Data Standards Catalog (预期 2026 正式决定). R Consortium 2025 秋第一次成功 Dataset-JSON submit ADaM.
- (c) 实操: (i) 开发环境可用 Dataset-JSON (便于 version control 和 diff) / (ii) 归档和最终 submit 仍用 XPT v5 / (iii) 有双向转换工具 (如 Atorus datasetjson R 包 / Pinnacle 21 支持) / (iv) 密切关注 FDA catalog 更新
- (d) Define-XML 是 metadata (变量定义 / CT reference / origin); Dataset-JSON 是 data. 两者互补: Define-XML 描述结构, Dataset-JSON 存数据. 未来 Define-XML v3.0 也在 align Dataset-JSON (可能简化 metadata 嵌入).

**FAIL 判据**:
- 说 FDA 已全面 Dataset-JSON (错, 仍 XPT 必需)
- 列不出 XPT 技术痛点
- 混淆 Define-XML 和 Dataset-JSON 角色

**04 非重叠**: 04 0 覆盖. Pure generalization ✅

**联网源**:
- [Clinical Leader — Piloting New Dataset-JSON For FDA Submissions](https://www.clinicalleader.com/doc/no-more-xpt-piloting-new-dataset-json-for-fda-submissions-0001)
- [Clinical Standards Hub — FDA Standards 2025](https://www.clinstandards.org/blog/navigating-fda-standards-2025)
- [Atorus Research — datasetjson R package](https://www.atorusresearch.com/datasetjson-0-0-1-release/)

---

## Q12 (D2 — CT 版本锁定) ChatGPT 专属

> **题**: 一个 3 年期临床试验, 从 2022 启动到 2025 DBL (database lock). 期间 CDISC 每季度发布 CT release. 请说明: (a) 这个试验**锁用**哪个 CT 版本 (start 时 / ongoing / DBL 时)? (b) 锁定 CT 版本的机制是什么 (Define-XML 哪个字段)? (c) AETERM 用 MedDRA 字典, MedDRA v25→v27 会不会影响 AE submission? (d) 如果 DBL 时发现某 CT codelist 已被 retire/alias, 怎么处理?

**PASS 判据**:
- (a) 锁定原则: 一般**锁试验启动或 DBL 时的 CT 版本** (通常 DBL, sponsor 决策; 也可 "study start"). **长期试验多数锁 DBL 时最新 CT**. 整个 submission 用**单一 CT 版本**, 保持 sponsorship 内一致.
- (b) 机制: **Define-XML** 的 `<CodeList>` 元素**引用 specific CDISC CT release date** (e.g., "SDTM CT 2024-12-13"). 每个 codelist 版本都标注. Validator 按这个版本检查.
- (c) AETERM 是 MedDRA 字典 (**sponsor 指定版本, 与 CDISC CT 无关**). 一般 submission 全用同一 MedDRA 版本 (e.g., "MedDRA v27.1"). v25→v27 可能有 term 改名或分类调整, **所有 AE 应 recode 到统一版本** (通常 DBL 时最新 MedDRA).
- (d) Retired/alias 的 CT 值: (i) 若 submission 已 lock CT 版本, 旧值保留, Reviewers Guide 说明; (ii) 若更换 CT 版本, 需要 **remap 所有相关值**, ADaM 可能也要调整.

**FAIL 判据**:
- 说可以混用多个 CT 版本 (错)
- 把 CDISC CT 和 MedDRA 混 (两个独立 vocabulary)
- Define-XML 作用不提
- 说 CT retire 值直接删 (错, 要文档化)

**04 非重叠**: 04 §1.15 Extensible 已提但**未深入 CT 版本锁定 / Define-XML 引用 / MedDRA**. ✅

---

## Q13 (G1 — RWD/Observational) ChatGPT 专属

> **题**: CDISC 2024 发布 "Considerations for SDTM Implementation in Observational Studies and Real-World Data v1.0". 请回答: (a) 在 RWD/observational 场景下, SDTMIG 的哪 2-3 类 conformance rule 会**自然失效**? (b) 没有 planned ARM 的观察性研究, DM 域 ARM/ARMCD 怎么处理? (c) 2024+ 新概念 **NS (Non-Standard Domain)** 和传统 SUPPQUAL 区别? (d) SUPPDM 可以用来补什么 observational 特有数据?

**PASS 判据**:
- (a) 失效 rule 类型: (i) **Trial Design 相关** — 无 Arm (ARMCD/ARM/TA) / 无 Trial Elements (TE) / 无 Trial Visits (TV); (ii) **IE domain** — 无 protocol Inclusion/Exclusion criteria; (iii) **Planned visit** — observational 可能无计划访视; (iv) **Study Reference Start Date** — observational 可能无单一 RFSTDTC.
- (b) 无 planned ARM: ARMCD/ARM 可填 "NOTASSGN" 或 "NOTASSIGNED" (Not Assigned 特殊值), CDISC CT 有留此值; **ACTARMCD/ACTARM** 可能需要扩展 codelist 填实际观察组 (e.g., "EXPOSED" vs "CONTROL").
- (c) **NS (Non-Standard Domain)** 是 2024+ 新概念: 对于完全不在标准 SDTM 域之内的 observational data, 用 **水平 NS 表** (1 dataset 多变量), 而非 SUPPQUAL 的**垂直 key-value**. NS 更易 analyze, SUPPQUAL 更 formal.
- (d) **SUPPDM** 可存 observational 特有: 观察来源 (Claims / EHR / Registry) / 数据 provenance / 队列 cohort ID / 暴露 exposed yes/no 等.

**FAIL 判据**:
- 说 RWD 必须强行匹配 clinical trial SDTM 所有 rule (错)
- 不识别 NS 新概念
- ARMCD 随便填 (错, CT 有 "NOTASSGN" 专值)

**04 非重叠**: 04 0 覆盖 RWD/observational. Pure generalization ✅

**联网源**:
- [CDISC — Considerations for SDTM Implementation in Observational Studies and RWD v1.0](https://www.cdisc.org/sites/default/files/2024-02/Considerations%20for%20SDTM%20Implementation%20in%20Observational%20Studies%20and%20Real-World%20Data%20v1.0.pdf)
- [CDISC — Using CDISC Standards in Observational Studies](https://www.cdisc.org/kb/articles/considerations-using-cdisc-standards-observational-studies)

---

## Q14 (I1 — AE + CE + MH 同事件共记 + DS 死亡记录) ChatGPT 专属

> **题**: 受试者 Visit 5 突发心梗 (STEMI) 住院, 治疗 3 天出院, 在 Visit 7 因心衰死亡. 请回答: (a) 这一系列事件里, **心梗本身**可以同时记在哪些域 (AE / CE / MH)? 各自的业务边界什么? (b) "死亡" 这个 terminal event 同时应该记 AE 和 DS 还是只一个? (c) DS 域的 **DSDECOD** vs **DSCAT** 在"死亡"场景下值各是什么? (d) 死亡时间的 ISO 8601 怎么跨域对齐 (AE.AESTDTC vs DS.DSSTDTC vs DM.DTHDTC)?

**PASS 判据**:
- (a) **AE**: 如果心梗是**研究期间发生的新事件且研究药物治疗期**, 必记 AE (AETERM="Myocardial Infarction", AESER=Y 因 SAE 住院, AESHOSP=Y). **CE**: 不用 (CE 是未达 AE 阈值的事件, SAE 住院必走 AE). **MH**: 不用 (MH 是**既往**病史, 非研究期间新发). 所以**心梗只在 AE**, 业务边界: AE=研究中新 TEAE + MH=既往 + CE=研究中但未达 AE 阈值 (如轻微主诉).
- (b) 死亡: **必记 DS** (DSDECOD 有专门 DEATH) **且 AE.AESDTH=Y** (如果死亡归因于某 AE). 两个是**不同视角**: AE 层记"哪个 AE 导致死亡", DS 层记"受试者 status = 死亡". 两者都要, 非互斥.
- (c) DS 死亡场景: **DSDECOD** = "DEATH" (CDISC CT **C66727** Disposition From Study codelist, 含 "DEATH" / "COMPLETED" / "WITHDRAWAL BY SUBJECT" 等值). **DSCAT** = sponsor 约定分类 (常见值 "DISPOSITION EVENT", 区别 "PROTOCOL MILESTONE" / "OTHER EVENT"; 非 CT 强制值, 接受 sponsor 合理变体). **DSTERM** = sponsor 描述 (e.g., "Subject died due to heart failure").
- (d) 三域对齐: **DM.DTHDTC** = 死亡日期 ISO 8601 (DM 级, 每 subject 唯一); **DS.DSSTDTC** = disposition event 开始 datetime (= 死亡日期 for DEATH row); **AE.AEENDTC** = 导致死亡的 AE 结束 datetime (通常 = DTHDTC). 三者**应一致**, 否则 Pinnacle 21 FAIL.

**FAIL 判据**:
- 说 AE + CE + MH 三个都记心梗 (错, 互斥)
- 死亡只记 AE 不记 DS (错, DS 必记)
- DSDECOD 答自定义 term (错, 有 CDISC CT DEATH)
- 三域死亡日期可以不同 (错, 应一致)

**04 非重叠**: 04 §1.2 AE SAE 住院 提过 AESER/AESHOSP, §1.15d DS 提过 DSDECOD 基础, §18.2 AE vs CE vs MH 有提. **未覆盖"同事件多域共记边界 + DS 死亡三域日期对齐"**. borderline ⚠️ (reframe 可, 强调**对齐**维度 04 未深入)

---

# PASS 阈值 + 评分规则

- **ChatGPT**: 14 题 × (0/0.5/1) = 0 / 7 / 14. PASS 阈 ≥ **10/14 (71%)** → Phase 4→5 Gate 候选
- **Gemini**: 10 题 × (0/0.5/1) = 0 / 5 / 10. PASS 阈 ≥ **7/10 (70%)** → Phase 4→5 Gate 候选
- **PASS** 题: 核心判据全中 + 无 FAIL 判据 → 1 分
- **PARTIAL**: 核心判据 ≥ 50% + 0-1 小缺漏 → 0.5 分
- **FAIL**: 核心判据 < 50% 或触 FAIL 判据 → 0 分

## Borderline 题目备注 (需 Step 2 reviewer 判 04 重叠度)

- **Q5 (FA vs QS vs CE)**: 04 §1.19 提过 FA vs QS, 未覆盖 CE 加入三元. 若 reviewer 判 >30% 重叠 → reframe 强调 CE 维度, 或换为 DV vs CE 二元.
- **Q8 (Extensible CT)**: 04 §1.15 有标题但无深. 若判重叠 → reframe 强调 MedDRA 外部字典 + Define-XML.
- **Q10 (SUPP)**: 04 §1.9 基础 + §19 深化. 若判重叠 → 限定 QORIG/QEVAL + SUPPTS 两维度 (04 未覆盖).
- **Q14 (AE+CE+MH + DS 死亡)**: 04 §1.2 / §1.15d / §18.2 有基础. reframe 强调**日期对齐**维度.

---

# 附录 A: 04 非重叠 audit 表 (初步, 待 Step 3 reviewer 正式跑)

| Q | 核心 keyword | Grep 04 预期 | 重叠判断 |
|:---:|---|---|:---:|
| Q1 | GFTESTCD / GFGENSR / GFINHERT | 04 0 匹配 | ✅ pure |
| Q2 | CPTESTCD / CPSBMRKS / CPCELSTA | 04 0 匹配 | ✅ pure |
| Q3 | BE+BS+RELSPEC | 04 §1.25 一句 | ✅ pure |
| Q4 | IS / anti-drug antibody / LB vs MB | 04 0 深入 | ✅ pure |
| Q5 | FA vs QS vs CE | 04 §1.19 FA vs QS 提过 | ⚠️ borderline |
| Q6 | --TPTREF / --ELTM | 04 未深入 | ✅ pure |
| Q7 | partial date imputation | 04 §1.8 基础 | ✅ pure |
| Q8 | Extensible / Non-Extensible / Define-XML | 04 §1.15 标题 | ⚠️ borderline |
| Q9 | Pinnacle 21 | 04 0 匹配 | ✅ pure |
| Q10 | QORIG / QEVAL / SUPPTS | 04 未覆盖两维度 | ⚠️ borderline |
| Q11 | Dataset-JSON / XPT | 04 0 匹配 | ✅ pure |
| Q12 | CT 版本 / Define-XML / MedDRA | 04 0 深入 | ✅ pure |
| Q13 | RWD / NS / Observational | 04 0 匹配 | ✅ pure |
| Q14 | AE + CE + MH 同事件 + DS 死亡日期对齐 | 04 有基础 | ⚠️ borderline |

**Pure generalization**: 10 题 (Q1/Q2/Q3/Q4/Q6/Q7/Q9/Q11/Q12/Q13)
**Borderline** (需正式 reviewer 判): 4 题 (Q5/Q8/Q10/Q14)
**04 预设作弊风险**: 0 题 (所有题要么 pure generalization, 要么至少重点**非** 04 覆盖面)

---

# 附录 B: 执行决策 (待用户 ack 后)

### 选项 A (推荐): 全 14 题原样提交 Step 3 reviewer 独立审
- 利: 充分 probe; 4 borderline 题的 reframe 可由 reviewer 精准建议
- 弊: 如果 reviewer 判 borderline 为 >30% 重叠, 需返工

### 选项 B: 主 session 先 reframe 4 borderline, 再进 Step 3
- 利: 提前降低返工风险
- 弊: 主 session 未必判准 04 重叠度, 可能过度删减

### 选项 C: 减到 10 纯 generalization 题 (砍 4 borderline)
- 利: 0 风险
- 弊: 降低 probe 覆盖面, Gemini 10 vs ChatGPT 10 没了专属差

### 推荐: **选项 A**

---

*来源: N5.3 design doc + 联网 WebSearch × 6 + WebFetch × 4 + 本地 KB 6 spec + SDTMIG v3.4 官方 + CDISC webinars + PharmaSUG/PhUSE 论文 + Pinnacle 21 + Observational RWD doc.*

*下一步: 用户 ack 选项 A/B/C → 主 session 执行相应 reframe / 进 Step 3 两 reviewer 独立审 SDTM 事实正确性 + 04 非重叠判定 + PASS 判据合理性.*
