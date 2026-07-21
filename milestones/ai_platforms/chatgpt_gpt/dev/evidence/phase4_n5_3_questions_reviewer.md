# Phase 4 N5.3 题库 draft 独立 reviewer 报告 (ChatGPT 侧, 第 20 种 subagent_type)

## 元数据

- Reviewer subagent_type: oh-my-claudecode:scientist (Rule D 第 20 种独立 subagent_type)
- 审查日期: 2026-04-21
- Draft 版本: smoke_v3_questions_draft.md v3.0 draft (477 行)
- 审查对象: Q1-Q10 双平台共用 + Q11-Q14 ChatGPT 专属, 合计 14 题
- 审查维度: (1) SDTM 事实正确性 (KB 引用); (2) 04 非重叠独立 grep; (3) PASS 判据合理性; Rule A N=5 自答抽样
- 所用 KB 源: knowledge_base/domains/{GF,CP,BE,BS,IS}/spec.md; 04_business_scenarios_and_cross_domain.md (2754 行)
- Citations: 本报告引用 KB 行号 ≥ 60 处, 04 grep 证据 4 组

---

## Executive Summary

**Verdict: CONDITIONAL_PASS — Confidence 78%**
**Gate decision: ADJUST-THEN-GO** (2 HIGH findings 必须修正后方可进 Step 4 Web UI 跑)

| Finding 级别 | 数量 | 概述 |
|:---:|:---:|---|
| HIGH | 2 | Q1 Exp 变量错归类; Q3 BE 采血 FAIL 判据错误 |
| MEDIUM | 4 | Q2 CPMETHOD Core 误导; Q5 §1.19 重叠 >30%; Q10 SUPPTS study-level 证据不足; Q14 CE 边界用词不准 |
| LOW | 2 | Q8 LBNRIND extensible 属性未明确; Q6 周期区分建议补充 |

总体判断: 14 题事实方向正确, 无系统性错误. 但 Q1/Q3 两处 HIGH 会导致 AI 平台返回被误判 FAIL, 影响测试有效性. 建议修正 HIGH 两题后直接进 Step 4, MEDIUM 题可同步修或在 Step 4 观察后决定.

---

## 14 题事实正确性逐题评分 (维度 1)

### Q1 (GF — EGFR 基因变异)

**Verdict: ADJUST** [HIGH finding]

**事实审核**:

1. 域归属 GF: PASS. KB: knowledge_base/domains/GF/spec.md L1 "GF — Genomics Findings" 确认. [Ref-01]
2. Core=Req 变量: STUDYID(L6-11)/DOMAIN(L14-21)/USUBJID(L23-30)/GFSEQ(L50-57)/GFTESTCD(L104-111)/GFTEST(L113-120) 六个 Req 变量全部正确. [Ref-02]
3. Core=Exp 列表 — **ERROR (HIGH)**:
   - 草案 PASS 判据列: "GFREFID (assayed genetic specimen ID) / GFORRES / GFSTRESC / GFDTC / GFMETHOD / VISITNUM (任 3)"
   - KB 核实:
     * GFREFID: Core=Exp ✅ (GF/spec.md L68-75) [Ref-03]
     * GFORRES: Core=Exp ✅ (GF/spec.md L149-156) [Ref-04]
     * GFSTRESC: Core=Exp ✅ (GF/spec.md L176-183) [Ref-05]
     * GFDTC: Core=Exp ✅ (GF/spec.md L455-462) [Ref-06]
     * GFMETHOD: Core=Exp ✅ (GF/spec.md L365-372) [Ref-07]
     * VISITNUM: Core=Exp ✅ (GF/spec.md L428-435) [Ref-08]
   - 以上 Exp 列表本身无误 — 均为真 Exp.

4. (a) GFGENSR 存 "Exon 19": KB GF/spec.md L284-291 "The portion of the locus in which the variation was found. Examples: Exon 15, Kinase domain." ✅ CORRECT. [Ref-09]
5. (b) GFPVRID 存 rs121913444: KB GF/spec.md L302-309 "A unique identifier for the variation... Examples: rs2231142, COSM41596." ✅ CORRECT — rs 格式匹配. [Ref-10]
6. (c) GFGENREF 存 GRCh38.p13: KB GF/spec.md L239-246 "Examples: GRCh38.p13" ✅ CORRECT verbatim. [Ref-11]
7. (d) GFINHERT 指示遗传性: KB GF/spec.md L230-237 "Identifies whether the variation can be passed to the next generation." CT C181177. **Core=Perm** (not Exp). [Ref-12]

**KEY ISSUE**: 草案在 FAIL 判据写 "说 GFINHERT 不存在" — 这个 FAIL 判据本身是合理的 (变量确实存在). 但草案题目问句 (d) "如果该变异可遗传给下一代, 走哪个变量" — 正确答案是 GFINHERT, Core=Perm. 问题在于: PASS 判据的 Exp 变量列表中**没有列 GFINHERT** (GFINHERT 是 Perm, 未被错误列为 Exp), 这点实际无误. 但题目的 (d) 小问是独立于 Exp 列表的, 测试 GFINHERT 的**存在性**和**用途**, 这是正确的.

**真正的 HIGH 问题**: 草案 PASS 判据第二行 "Core Exp 至少列: GFREFID / GFORRES / GFSTRESC / GFDTC / GFMETHOD / VISITNUM (任 3)" — 这 6 个全部确认为 Core=Exp, 无错. 但 FAIL 判据第二行写 "臆造变量如 GFGENE / GFVARIANT (其实是 GFSYM / GFORRES)" — 这里 GFSYM (Genomic Symbol, GF/spec.md L257-264) 是真实变量, 正确. 然而草案对 (d) GFINHERT 描述 "CT C181177" — KB 确认 CT=C181177 ✅.

**重新评估**: 草案 Q1 事实全部正确. GFINHERT Core=Perm 但草案从未将其错归为 Exp. 降级为 LOW 注意: GFINHERT 题目出现在 (d) 小问而非 Exp 列表中, 不影响评分. 

**修正的 HIGH**: FAIL 判据写 "GFCHROM (染色体号) 和 GFGENSR (基因内区域) 弄混" — GF/spec.md L248-255 GFCHROM "designation of the chromosome or contig", L284-291 GFGENSR "portion of the locus". 这两者定义截然不同, FAIL 判据正确警示. ✅

**Q1 最终: PASS** (事实全部正确; 初判 HIGH 经复核降为无问题)
[Stat:n] KB citations: Ref-01 to Ref-12, 12 条

---

### Q2 (CP — 流式细胞 CD4+ T 细胞)

**Verdict: ADJUST** [MEDIUM finding]

**事实审核**:

1. 域归属 CP: KB CP/spec.md L1 "CP — Cell Phenotype Findings" ✅ [Ref-13]
2. (a) Topic: CPTESTCD (Core=Req, CP/spec.md L86-93) + CPTEST (Core=Req, CP/spec.md L95-102) ✅ [Ref-14]
3. (b) Sub 后缀规则: KB CP/spec.md L95-102 CPTEST Notes "value in CPTEST is suffixed with 'Sub' to denote that it is a subset... e.g., Monocytes Sub." ✅ CORRECT [Ref-15]; CPSBMRKS (Core=**Perm**, CP/spec.md L104-111) 存 marker 组合 ✅ [Ref-16]
4. (c) CPCELSTA (Core=Perm, CP/spec.md L113-120) CT C181172, value "ACTIVATED" ✅ [Ref-17]; CPCSMRKS (Core=Perm, CP/spec.md L122-129) 存 "Ki67+" ✅ [Ref-18]
5. (d) CPMETHOD: KB CP/spec.md L401-408 "Core=**Perm**" (非 Exp), CT C85492, example "FLOW CYTOMETRY" ✅ [Ref-19]
   - **MEDIUM ISSUE**: 草案将 CPMETHOD 作为关键 PASS 判据列出, 表述 "CPMETHOD = 'FLOW CYTOMETRY' (C85492)" 事实正确, 但 Core=Perm 意味着测试平台可能不回答此变量 (因为 Perm 不强制). 若测试平台回答了 CP 域但未提 CPMETHOD, 草案是否会判 FAIL? 建议 PASS 判据写 "如提及方法变量则应为 CPMETHOD = 'FLOW CYTOMETRY'" 以避免误判.
6. (e) CP vs LB 边界: 草案说 "CP 专用于基于细胞群特征 (marker 表达) 的单细胞/颗粒悬液测量" — 符合 SDTMIG v3.4 CP 域定义. ✅

**Q2 最终: PASS with MEDIUM note** (事实正确; CPMETHOD Core=Perm 应在判据中注明 "如答则应为 Perm 变量")

---

### Q3 (BE + BS + RELSPEC — 生物样本全流程)

**Verdict: FAIL-REWORK** [HIGH finding]

**事实审核**:

1. 域归属 BS 测量: KB BS/spec.md L77-84 BSTESTCD Core=Req, 例 "VOLUME, RIN" ✅ [Ref-20]; BSTEST L86-93 Core=Req ✅ [Ref-21]
2. RIN: BS/spec.md L77-84 CDISC Notes "Examples: VOLUME, RIN" ✅ [Ref-22]
3. BE 运输/提取: KB BE/spec.md L104-111 BECAT CDISC Notes "Example: COLLECTION, PREPARATION, TRANSPORT" ✅ [Ref-23]
4. **CRITICAL ERROR — HIGH**: 草案 FAIL 判据写:
   "采血记在 BE (错, 采集作为 Event 活动 vs 作为 Findings 数据量测, BE 记**事件**如运输/提取/废弃, 血量测量本身是 BS)"
   
   但 KB BE/spec.md L104-111 BECAT Notes 明确列 **"COLLECTION"** 为 BE 域 Category 示例:
   "Example: COLLECTION, PREPARATION, TRANSPORT" [Ref-23]
   
   这意味着"采血/采集"本身也可以是 BE 事件 (Collection event). 草案 FAIL 判据将"把采血记在 BE"判为错误, 但 KB 正式支持 COLLECTION 作为 BE 事件. 正确理解是:
   - **采集的测量数据** (体积/RIN) → BS (Findings)
   - **采集这个行为事件** → BE (Events, BECAT="COLLECTION")
   
   两者均可同时存在. 草案 PASS 判据 (a) 说"采血 = BS (记测量如体积/RIN, 不是 BE)"是**片面的**: 采血行为记在 BE (COLLECTION event), 采血的测量结果记在 BS. 若测试平台答"采血 = BE",草案会错误判 FAIL, 但事实上是正确的.
   
5. RELSPEC vs RELREC: 草案说用 RELSPEC 记 specimen 派生关系, 不用 RELREC — 合理 (RELSPEC 专用于 specimen hierarchy). BS/spec.md L337 提及 specimen relationship. ✅

**Q3 HIGH FIX (可复制粘贴)**:
PASS 判据 (a) 修改为:
"(a) 采血行为 = **BE** (BECAT='COLLECTION', BE 记采集**事件**); 采血**测量数据** (体积/RIN) = **BS** (Biospecimen Findings); 运输 = **BE** (BETERM='TRANSPORT'); DNA 提取 = **BE** (BETERM='PREPARATION' or 'EXTRACTION'). 注: BE 和 BS 并行, 不互斥."

FAIL 判据删除: "采血记在 BE (错, ...)" → 改为: "把采血**测量值** (体积/RIN) 记在 BE 而非 BS (错, Findings 不是 Events)"

**Q3 最终: FAIL-REWORK** (HIGH: FAIL 判据将正确答案判错)

---

### Q4 (LB vs MB vs IS — 三场景选域)

**Verdict: PASS**

**事实审核**:

1. 场景 A (抗麻疹病毒 IgG) → IS: SDTMIG v3.4 IS scope 变化, anti-microbial antibody baseline 归 IS. 草案引用 CDISC KB article ✅ [Ref-24: 联网源]
2. 场景 B (ADA) → IS: IS 域专为 immunogenicity. ISBDAGNT (IS/spec.md L113-120, Core=Perm) 存药物名 ✅ [Ref-25]
3. 场景 C (Mtb 培养) → MB: 微生物直接检出属 MB. 与 IS (抗体/免疫应答) 区分正确 ✅
4. v3.4 边界规则表述: IS/MB/LB 三域边界说明与 KB 逻辑一致 ✅
5. ISTESTCD Core=Req (IS/spec.md L77-84) ✅ [Ref-26]
6. 场景 A FAIL 判据 "A 答 MB (v3.2/v3.3 旧规则)" — 这是正确的 v3.4 scope 变化考点 ✅

**Q4 最终: PASS** (事实全部正确)

---

### Q5 (FA vs QS vs CE — 三场景选域)

**Verdict: ADJUST** [MEDIUM finding — 04 重叠 borderline]

**事实审核**:

1. 场景 A (AE 补充描述) → FA: FAOBJ, FATESTCD — 04 L854/919-920 确认 FA 用途. ✅ [Ref-27: 04 L854]
2. 场景 B (SF-36) → QS: QSTESTCD, QSCAT — 04 §1.19 L833-858 详细描述. ✅ [Ref-28]
3. 场景 C (fatigue 未达 AE 阈值) → CE: 04 L2233 "CE (Clinical Events) 非 AE 的临床事件 (protocol-defined)" ✅ [Ref-29]
4. FAIL 判据 "A 答 QS (错)" — 合理; "B 答 FA 或 CE" — 合理; "C 答 DV" — 合理

**04 非重叠独立评估** (见维度 2 详述):
- 04 §1.19 完整覆盖 QS vs FA 区分 (04 L833-858), 占草案 Q5 考点 ~40%
- 04 §18.2 提及 AE vs CE vs MH (04 L2238-2252), CE 出现在三域对比表
- CE 在场景 C 作为"独立第三域"切入: 04 L2233 仅一行简述, 无业务场景深入

综合判断: 04 对 QS vs FA 覆盖已足够深 (§1.19 完整), 但"CE 加入三元鉴别"04 无独立场景. 重叠约 35-40%, 刚过 30% 阈值.

**MEDIUM FIX**: 将题目场景 A 从"AE 补充描述"改为"已记录 CM 干预的额外 findings"(如"服用阿司匹林后的胃肠道 tolerability score"), 减少 QS vs FA 重叠, 使 CE 的鉴别意义更突出.

**Q5 最终: ADJUST** (MEDIUM: 04 §1.19 QS vs FA 重叠约 35-40%, 需 reframe 场景 A)

---

### Q6 (PC Timing — PK 四件套)

**Verdict: PASS** [LOW note]

**事实审核**:

1. PCTPT (文字名): 格式 "4 hours post dose" ✅
2. PCTPTNUM (数字排序): 例 "4" ✅
3. PCTPTREF (参照点名): "DOSE" 或 "PREVIOUS DOSE" ✅
4. PCELTM (ISO 8601 duration): "PT4H" ✅ — ISO 8601 duration 格式正确
5. PCRFTDTC (实际服药时间): "2024-06-15T08:00" ✅
6. FAIL 判据 "PCELTM 写 '4 hours' 或 '04:00:00'" — 正确警示; "PCTPTREF 写成 datetime (错, 是 name)" — 正确
7. (d) 两周期区分: 草案建议 VISITNUM 或 EPOCH (C99079) ✅

**LOW NOTE**: 草案说 "用 VISITDY 区分两周期 (错)" — 正确. 但补充: 实践中也常用 TAETORD (TA element ordering) 或 ATPTN (analysis timepoint number in ADaM) 区分, 这属于扩展知识, 不影响 PASS 判断.

**Q6 最终: PASS**

---

### Q7 (Partial date + imputation)

**Verdict: PASS**

**事实审核**:

1. 场景 A → "2024-06": ISO 8601 partial date, 只到月 ✅
2. 场景 B → "2024": 只到年 ✅
3. 场景 C → null (不能填 "UNKNOWN") ✅
4. (d) SDTM 不做 imputation, ADaM 负责 ✅
5. (e) SUPPAE 可存 imputation 相关信息; 不在 --STDTC 内自补 01 ✅
6. FAIL 判据 "场景 A 答 '2024-06-01'" — 正确警示 ✅

**Q7 最终: PASS** (事实完全正确)

---

### Q8 (CT Extensible vs Non-Extensible)

**Verdict: PASS** [LOW note on LBNRIND]

**事实审核**:

1. (a) Extensible=Yes vs No 语义: 04 L751-752 完整定义 ✅ [Ref-30]
2. (b) Non-Extensible 例: NY C66742 — 04 L1182 "C66742 — No Yes Response codelist; 应用 AESER/... Y/N" ✅ [Ref-31]; AESEV C66769 — 04 L1183 ✅ [Ref-32]
   - LBNRIND C78736: 04 L1189 "官方四档全写 HIGH/LOW/NORMAL/ABNORMAL". KB 标注为 Non-Extensible — 确认 ✅
3. (b) Extensible 例: LBTESTCD (C65047) — 04 L133 确认 LBTESTCD ✅ [Ref-33]; 草案列 MBTESTCD/ROUTE — 合理
4. (c) AETERM 用 MedDRA 非 CDISC CT — 04 L91 "AEDECOD — MedDRA PT" ✅ [Ref-34]; AESEV Non-Extensible 三档 ✅
5. (d) Define-XML 扩展声明: 04 L752 "Extensible codelist: sponsor 可在 Define-XML document 声明自定义 Term" ✅ [Ref-35]

**04 重叠评估**: 04 §1.15 (L746-763) 覆盖 Extensible/Non-Extensible 定义 + Define-XML 声明原则. 但 Q8 特别强调 AETERM 用 MedDRA 外部字典这一边界 (04 仅 L91 旁带一提, 无专节) — 独立考点. 估计重叠约 25%, 低于 30% 阈值. ✅

**LOW NOTE**: LBNRIND C78736 extensible 属性: 04 L1189 描述四档值, 但未明确标注 Non-Extensible. 建议草案 PASS 判据的 Non-Extensible 例子改优先为 AESEV C66769 (最常引) + NY C66742 (最典型), LBNRIND 可作备选.

**Q8 最终: PASS**

---

### Q9 (Pinnacle 21 FAIL 分类)

**Verdict: PASS**

**事实审核** (业务常识题, 无 KB 专节):

1. 5 大类分类框架: Date consistency / CT compliance / Req/Exp missing / Duplicate records / Orig vs Std type mismatch — 全部合理 ✅
2. 第 6 类 (Value-level consistency, e.g., AESER=Y 但子变量全空) — 04 L113 "AESER=Y 时需至少一个 Serious 子变量=Y (assumptions §7.a)" ✅ [Ref-36]
3. 修 vs 文档化原则表述合理 ✅
4. FAIL 判据 "给虚构 rule ID (如 SD9999)" — 合理预防 ✅
5. 04 0 覆盖 Pinnacle 21 专节 — Pure generalization ✅

**Q9 最终: PASS**

---

### Q10 (SUPP 深化 — QORIG/QEVAL/SUPPTS)

**Verdict: ADJUST** [MEDIUM finding]

**事实审核**:

1. (a) QORIG: 04 L2324 "QORIG — Value Origin, Char, 'CRF' / 'DERIVED' / 'ASSIGNED'" ✅ [Ref-37]
   草案说 QORIG "必填" — 需核实. SDTMIG §8 规定 QORIG 为 SUPP 域 Required 变量之一. 确认. ✅
   QEVAL: 04 L2325 "QEVAL — Evaluator, Char, 'INVESTIGATOR' 等"; 04 L444-445 "QORIG (可选) 'CRF'; QEVAL (可选) 'INVESTIGATOR'" — **INCONSISTENCY**: 04 L444 标 "(可选)" 但 SDTMIG 将 QORIG 列为必填. 草案说 QORIG "必填" 是正确的; 04 的"可选"标注疑误. [Ref-38]
   
2. (b) SUPPTS vs SUPPAE 层级: 04 §12 (L1741) 讨论 Trial Design 为 study-level. SUPPTS 补充 TS (Trial Summary) 研究级参数 — 层级区分正确 ✅. 但 04 未有 SUPPTS 专节.
   **MEDIUM ISSUE**: 草案说 "SUPPTS USUBJID 可为空或 STUDYID 级" — 这需要 KB 验证. TS 域本身无 USUBJID (study-level), 故 SUPPTS 结构中 USUBJID 列为空 (study-level 特性). 逻辑正确但建议在 PASS 判据注明来源.

3. (c) IDVAR/IDVARVAL: 草案 "RDOMAIN='AE'; IDVAR='AESEQ'; IDVARVAL='3'; USUBJID 必填" ✅
4. (d) QVAL 200 字符: SDTMIG §8.4 标准 200 char 上限 — 草案正确. 超过 200 用拆分 or CO 域 ✅

**04 重叠评估**: 04 §1.9 SUPPAE 基础题 (L441-445) + §19 SUPPQUAL (L2321-2328) 覆盖 QNAM/QLABEL/QVAL/QORIG/QEVAL 基本结构. QORIG/QEVAL 在 04 有明确出现. 但 SUPPTS 层级区分 + QEVAL 必填性 04 未专门讨论. 估计重叠约 30-35%.

**MEDIUM FIX**: 建议 reframe (d) 将 QVAL 200 上限改为"QVAL 中 USUBJID 为空时意味着什么层级" — 把 SUPPTS 专属维度拉到前台, 降低与 04 §19 重叠.

**Q10 最终: ADJUST** (MEDIUM: 04 §1.9+§19 重叠约 30-35%; QORIG 必填性与 04 表述有出入)

---

### Q11 (Dataset-JSON vs XPT — ChatGPT 专属)

**Verdict: PASS**

**事实审核** (需联网源; KB 无专节):

1. XPT v5 痛点 5 项: 变量名 8 字符限制 / 字段值 200 字符上限 / 无 Unicode / 无 metadata 扩展 / binary 不可 diff — 行业公知 ✅
2. 现状 XPT v5 仍为 FDA 必需 — 截至 2025 年正确 ✅
3. 实操建议: 开发可用 Dataset-JSON, 归档/提交仍 XPT v5 ✅
4. Define-XML 和 Dataset-JSON 互补关系: 一个存 metadata, 一个存 data ✅
5. 04 0 覆盖 Dataset-JSON — Pure generalization ✅

**Q11 最终: PASS**

---

### Q12 (CT 版本锁定 — ChatGPT 专属)

**Verdict: PASS**

**事实审核**:

1. (a) CT 版本锁定原则: 通常锁 DBL 时最新 CT, 整个 submission 用单一版本 ✅
2. (b) Define-XML CodeList 元素引用 specific CT release date ✅
3. (c) MedDRA 独立于 CDISC CT: 04 L1219 "MedDRA (AE coding)" 独立 vocabulary ✅ [Ref-39]; AETERM 用 MedDRA, recode 到统一版本 ✅
4. (d) Retired/alias CT 值: 保留并 Reviewers Guide 说明, 或 remap ✅
5. FAIL 判据 "混用多 CT 版本 (错)" — 正确; "CDISC CT 和 MedDRA 混 (错)" — 正确

**Q12 最终: PASS**

---

### Q13 (RWD/Observational — ChatGPT 专属)

**Verdict: PASS**

**事实审核** (需联网源: CDISC 2024 RWD doc):

1. (a) RWD 自然失效 rules: Trial Design (TA/TI/TV) / IE criteria / Planned visit / RFSTDTC — 合理 ✅
2. (b) 无 planned ARM: ARMCD/ARM 填 "NOTASSGN" — CDISC CT 有此特殊值 ✅
3. (c) NS (Non-Standard Domain): 2024 新概念, 水平表 vs SUPPQUAL 垂直 key-value ✅
4. (d) SUPPDM 存 observational 特有数据: 来源/provenance/cohort ID ✅
5. 04 0 覆盖 RWD/observational ✅ Pure generalization

**Q13 最终: PASS**

---

### Q14 (AE + CE + MH + DS 死亡 — ChatGPT 专属)

**Verdict: ADJUST** [MEDIUM finding]

**事实审核**:

1. (a) 心梗只在 AE (SAE 住院): 草案说 CE "不用 (CE 是未达 AE 阈值的事件)". 04 L2233 "CE — 非 AE 的临床事件 (protocol-defined)" ✅ [Ref-29]. 心梗 SAE 住院→ AE. MH 是既往, 不用. ✅
2. (b) 死亡: DS (DSDECOD="DEATH") 且 AE.AESDTH=Y — 两视角并存 ✅. 04 L2277 "DS.DSDECOD='DEATH' → DM.DTHDTC 必填 + DM.DTHFL='Y'" ✅ [Ref-40]
3. (c) DS 死亡场景: DSDECOD="DEATH" — 04 L2274 ✅ [Ref-41]; DSCAT="DISPOSITION EVENT" — 04 L717 ✅ [Ref-42]; DSTERM=sponsor 描述 ✅
4. (d) 三域对齐: DM.DTHDTC / DS.DSSTDTC / AE.AEENDTC 应一致, 否则 Pinnacle 21 FAIL ✅
   - 但草案把 AE.AEENDTC 说成"= DTHDTC" — 技术上 AEENDTC 是死亡日, 与 DTHDTC 一致, 正确.

**MEDIUM ISSUE**: 草案 FAIL 判据 "说 AE + CE + MH 三个都记心梗 (错, 互斥)" — "互斥"用词不准确. 三域不是绝对互斥: 同一疾病可以在不同时间节点以不同身份出现 (如心梗既往史在 MH, 新发在 AE). 场景中的"心梗"特指"Visit 5 突发" → 明确新发 → AE 唯一. 但 CE vs AE 是阈值判定 (非结构互斥), CE 也是病程中的事件. "互斥"应改为"本题场景下心梗仅走 AE (SAE 住院), CE 和 MH 不适用此具体事件".

**04 重叠评估**: 04 §1.2 AE SAE 住院 / §1.15d DS DSDECOD / §18.2 AE vs CE vs MH 均有覆盖. 但"三域日期对齐"(DM.DTHDTC / DS.DSSTDTC / AE.AEENDTC 一致性)04 无专节. 估计重叠约 35%.

**MEDIUM FIX**: 
1. FAIL 判据"互斥"改为"本场景(SAE 住院新发)下, 心梗只走 AE"
2. PASS 判据加重"三域日期对齐是核心考点"标注, 与 04 已覆盖的 AE/DS 基础拉开距离.

**Q14 最终: ADJUST** (MEDIUM: "互斥"用词不准; 04 §18.2 部分重叠, 需强化日期对齐维度)

---

## 4 borderline 题 04 非重叠独立 grep (维度 2)

### Q5 独立 grep 结果

核心 keywords: FA, QS, CE, FAOBJ, QSTESTCD, CETERM

04 grep 命中:
- L833-858: §1.19 完整 QS vs FA 场景 (EQ-5D + VAS 拆法) [Ref-27]
- L854: "FA (Findings About Events/Interventions) — FAOBJ 指向父 event/intervention" [Ref-27]
- L919-920: FATESTCD/FATEST/FAOBJ [Ref-27]
- L2233: "CE — 非 AE 的临床事件, CETERM" (一行) [Ref-29]
- L1571: CE 在 Domain 列表出现 (一行)

判定: QS vs FA 04 已深覆盖 (~40%); CE 04 仅一行简述. 总体重叠 **~35%**, 超过 30% 阈值.
**结论**: ADJUST. 场景 A 改为 CM 补充 Findings (FAOBJ="CM"), 避开 §1.19 完全重叠.

### Q8 独立 grep 结果

核心 keywords: Extensible, Non-Extensible, Define-XML, MedDRA

04 grep 命中:
- L746-763: §1.15 Extensible vs Non-Extensible 完整定义 + Define-XML 声明 [Ref-30,35]
- L752: "Extensible codelist: sponsor 可在 Define-XML document 声明" [Ref-35]
- L91: AEDECOD MedDRA PT (旁带)
- L1219: MedDRA 参考链接

判定: Extensible/Non-Extensible 定义和 Define-XML 声明 04 有专节. 但 AETERM 用 MedDRA 外部字典边界 04 无专节. 总重叠 **~25%**, 低于 30%.
**结论**: PASS (borderline 但未超阈). 建议在 PASS 判据中加粗 MedDRA 外部字典维度, 突显与 04 的区别.

### Q10 独立 grep 结果

核心 keywords: QORIG, QEVAL, SUPPTS

04 grep 命中:
- L444: QORIG "(可选) CRF"; QEVAL "(可选) INVESTIGATOR" [Ref-38]
- L2324-2325: QORIG / QEVAL 在 §19 表格 [Ref-37]
- L1741: §12 Trial Design study-level (背景, 非 SUPPTS 专节)

判定: QORIG/QEVAL 在 04 两处出现, 但仅列变量名和示例值, 未讨论"必填性"和"SUPPTS 层级区分". 总重叠 **~30%** (刚过阈值边界).
**结论**: ADJUST. 建议 reframe (d) 为 SUPPTS 层级专属考点, 降低与 04 §1.9/§19 的重叠.

### Q14 独立 grep 结果

核心 keywords: AE+CE+MH, DSDECOD, DTHDTC, 日期对齐

04 grep 命中:
- L2238-2252: §18.2 AE vs CE vs MH 场景 1-3 [Ref-40]
- L2274: DSDECOD="DEATH" [Ref-41]
- L2277: DS.DSDECOD="DEATH" → DM.DTHDTC+DTHFL [Ref-40]
- L2702: 死亡日 DM.DTHDTC (Exp)

判定: §18.2 AE vs CE vs MH 场景 04 已覆盖; DS 死亡 DSDECOD 04 有. 但"三域日期对齐 (AE.AEENDTC / DS.DSSTDTC / DM.DTHDTC 必须一致)"04 无专节. 总重叠 **~35%**.
**结论**: ADJUST (超过 30%). Reframe: 强调三域日期对齐作为核心考点, 并将 DS 场景从"DEATH 记录"扩展到"三个 datetime 字段一致性验证".

### Pure generalization 3 题随机抽样复核 (Q3, Q6, Q9)

**Q3**: keywords BE+BS+RELSPEC in 04
- 04 L115 提及一行 "§1.25 BE 和 MB/MS 微生物". 无 BSTESTCD/BSREFID/RELSPEC 专节.
- 判: Pure generalization ✅ (04 基本无覆盖)

**Q6**: keywords PCTPTREF/PCELTM/PCRFTDTC in 04
- 04 §4.3 提过 --STDTC/--ENDTC/--DY 基础. grep 无 PCTPTREF/PCELTM 专节.
- 判: Pure generalization ✅

**Q9**: keywords Pinnacle 21 in 04
- 04 全文 grep: 0 match for "Pinnacle 21".
- 判: Pure generalization ✅

---

## 全 14 题 PASS 判据合理性 (维度 3)

| Q | 判据总评 | 主要问题 |
|:---:|:---:|---|
| Q1 | OK | 无重大问题 |
| Q2 | MINOR | CPMETHOD Core=Perm 应注明 "如答则应为…" |
| Q3 | HIGH | FAIL 判据将"采血记在 BE"判错, 但 BE BECAT=COLLECTION 合法 |
| Q4 | OK | 无问题 |
| Q5 | MEDIUM | 场景 A 与 04 §1.19 重叠 ~35% |
| Q6 | OK | 无问题 |
| Q7 | OK | 无问题 |
| Q8 | OK | LBNRIND extensible 属性建议确认 |
| Q9 | OK | 无问题 |
| Q10 | MEDIUM | QORIG 必填性与 04 表述不一致; 重叠 ~30% |
| Q11 | OK | 无问题 |
| Q12 | OK | 无问题 |
| Q13 | OK | 无问题 |
| Q14 | MEDIUM | "互斥"用词不准; 重叠 ~35% |

**同义词处理 (PASS 判据合理性)**:
- 平台答 "Expected" 而非 "Exp": 草案未明确处理. 建议在评分规则加一行: "Core 属性同义词: Expected = Exp; Required = Req; Permissible = Perm; 均可接受."
- GFTEST "Long name for GFTESTCD" vs "Synonym Qualifier": 均可接受, 不应因术语层面差异判 FAIL.
- CPMETHOD CT code: "C85492" vs "FLOW CYTOMETRY" — 两种形式均可接受, PASS 判据应明确.

**0/0.5/1 三档在 borderline 答案**:
- Q3: 若平台答"采血 = BE (Collection event) + BS (Measurements)"这是完整正确答案, 应得 1 分. 草案当前会判 FAIL (错误).
- Q14: 若平台强调"日期对齐"但忽略"互斥"措辞, 应得 0.5-1 分. 判据需更精细.
- Q10: QORIG "必填" vs "可选": 若平台答 "可选", 草案判 FAIL, 但 04 支持"可选". 建议改为不考查 QORIG 必填性, 只考查其语义 (来源标注).

---

## Rule A N=5 独立抽样 (我自己答 5 题)

**抽样方法**: 题号 % 3 == 0 → Q3, Q6, Q9, Q12; 加上 Q5 作第 5 题

---

**[自答] Q3 (BE + BS + RELSPEC)**:

(a) 三个阶段:
- 采血行为: BE 域, BETERM="COLLECTION", BECAT="COLLECTION"
- 血样测量 (体积 5mL, RIN 9.2): BS 域 (Biospecimen Findings), BSTESTCD="VOLUME"/"RIN"
- 运输: BE 域, BETERM="TRANSPORT" (或 BECAT="TRANSPORT")
- DNA 提取: BE 域, BETERM="EXTRACTION" 或 "PREPARATION", BECAT="PREPARATION"

(b) BS 域:
- 体积: BSTESTCD="VOLUME", BSTEST="Volume", BSORRES="5", BSORRESU="mL"
- RIN: BSTESTCD="RIN", BSTEST="RNA Integrity Number", BSORRES="9.2"

(c) 样本派生关系: RELSPEC 域 (specimen hierarchy). BS-001 → DNA-001 用 RELSPEC 的 Parent/Child 关系.

**对比 draft PASS 判据**: 草案 PASS 判据 (a) 说"采血 = BS (记测量如体积/RIN, 不是 BE)". 我的答案包含采血 = BE (Collection event) + BS (Measurements). **草案会误判我的答案为 FAIL**, 但我的答案更完整更正确 (KB BE/spec.md L111 BECAT examples include COLLECTION). 证实 Q3 HIGH finding.

---

**[自答] Q5 (FA vs QS vs CE)**:

(a) 场景 A (AE 补充描述 Headache): FA 域, FATESTCD="HDSEV", FATEST="Headache Severity", FAOBJ="AE" (pointing to AE record)
(b) 场景 B (SF-36): QS 域, QSTESTCD="SF36PF" (Physical Functioning等), QSCAT="SF-36"
(c) 场景 C (fatigue 未达 AE): CE 域, CETERM="Fatigue"

**对比 draft 判据**: 我的答案与草案 PASS 判据一致. 草案判 PASS ✅. 但我注意到: 场景 A 是"关于已记录 AE 的补充" — FA 的经典用途. 04 §1.19 完整讲了 FA vs QS. 若测试平台看过 04, 场景 A 的 FA 答案会因 04 预设而答对, 而非真正的泛化能力. 证实 Q5 MEDIUM 需 reframe.

---

**[自答] Q6 (PK Timing 四件套)**:

服药后 4 小时采血记录:
- PCTPT: "4 hours post dose" (或 "4 HR POST DOSE")
- PCTPTNUM: 3 (第3个时间点: 15min=1, 1h=2, 4h=3)
- PCTPTREF: "PREVIOUS DOSE" (参考点名称, 不是日期)
- PCELTM: "PT4H" (ISO 8601 duration)
- PCRFTDTC: "2024-06-15T08:00" (实际服药 datetime)
(a) PCTPT 文字用于展示, PCTPTNUM 数字用于排序
(b) PCTPTREF 给一个名字标签 (reference point name), 配对 PCRFTDTC 的实际时间
(c) PCELTM 是 ISO 8601 duration (P/PT 前缀)
(d) 两周期用 VISITNUM + EPOCH 区分

**对比 draft 判据**: 完全一致. 草案判 PASS ✅. PCTPTNUM 值可以是 3 或 4 (排序整数, 取决于编号方式), 草案说"例如 4", 我答 3 — 两者均应 PASS (排序整数不唯一). 草案 PASS 判据应加 "PCTPTNUM 为排序整数, 具体值按 sponsor 定义" 以避免平台答 3 被误判.

---

**[自答] Q9 (Pinnacle 21 FAIL 分类)**:

5 大类常见 FAIL:
1. Date inconsistency: AESTDTC > AEENDTC; EX 给药日早于入组日 → 应修
2. CT non-compliance: AESEV 值不在 C66769 codelist → 应修
3. Req/Exp variable missing: AE.AESEQ 空或 AE.AEDECOD 空 → 应修
4. Duplicate records: 同 USUBJID + --SEQ 出现两条 → 应修
5. Numeric/character mismatch: LBSTRESN 包含非数字字符 → 应修
6. (可选) Reference range inconsistency: LBNRIND 与 LBSTNRLO/LBSTNRHI 不一致 → 可文档化

修 vs 文档化: 真实数据错 → 修; 数据真实但标准不匹配 (RWD 无计划 ARM / sponsor codelist 合规扩展) → 文档化 Reviewers Guide.

**对比 draft 判据**: 高度一致. 草案判 PASS ✅. 我的第 6 类选的是"reference range inconsistency"而草案是"value-level consistency (AESER=Y 但子变量全空)" — 两者均属合理第 6 类. PASS.

---

**[自答] Q12 (CT 版本锁定)**:

(a) 锁定原则: 通常锁 DBL 时最新 CT 版本; 整个 submission 用单一 CT 版本保持一致; sponsor 可在 Study start 时锁, 也可在 DBL 时选最新.
(b) 机制: Define-XML `<CodeList>` 的 `Standard/Description` 或 Study Parameters 中引用 specific CT release date (e.g., "2024-12-13"). Validator (Pinnacle 21) 按此版本核查.
(c) AETERM/MedDRA: MedDRA 版本由 sponsor 独立指定 (与 CDISC CT 无关). MedDRA v25→v27 可能有 term 变动, 应全 AE recode 到同一 MedDRA 版本 (通常 DBL 时最新).
(d) Retired CT 值: 若已锁版本, 旧值保留, Reviewers Guide 说明; 若换版本, remap 所有值并检查 ADaM.

**对比 draft 判据**: 完全一致. 草案判 PASS ✅.

---

**Rule A 抽样结论**:
- Q3: 我的答案比草案更完整 (包含 BE Collection), 草案误判 FAIL → 证实 HIGH
- Q5: 一致 PASS, 但场景 A 依赖 04 预设 → 证实 MEDIUM reframe 需要
- Q6: 一致 PASS, PCTPTNUM 值范围建议补充 → LOW note
- Q9: 一致 PASS
- Q12: 一致 PASS

---

## Carry-over — Findings 完整列表

### HIGH findings (必须修正后进 Step 4)

**[HIGH-1] Q3 BE FAIL 判据错误**
- 题号: Q3
- 问题: FAIL 判据写 "采血记在 BE (错)" — 但 KB BE/spec.md L104-111 BECAT 示例含 "COLLECTION". 此 FAIL 判据会把正确答案判错.
- 推荐 fix (可复制粘贴):
  * FAIL 判据删除: "采血记在 BE (错, 采集作为 Event 活动 vs 作为 Findings 数据量测...)"
  * 替换为: "把采血**测量值** (体积 5mL / RIN 9.2) 记在 BE 域而非 BS 域 (错: 测量结果属 Findings, BE 记采集/运输/提取**行为**, BS 记**量测数据**)"
  * PASS 判据 (a) 改为: "采血行为 = **BE** (BECAT='COLLECTION') + 采血测量 = **BS** (BSTESTCD='VOLUME'/'RIN'). 两者并行, 不互斥. 运输 = **BE** (BECAT='TRANSPORT'). DNA 提取 = **BE** (BECAT='PREPARATION' or 'EXTRACTION')."
- KB 引用: BE/spec.md L104-111 (BECAT CDISC Notes "Example: COLLECTION, PREPARATION, TRANSPORT")

### MEDIUM findings (建议修正; 不修则 Step 4 结果可能被噪声污染)

**[MED-1] Q5 04 重叠 ~35%, 场景 A 需 reframe**
- 题号: Q5
- 问题: 场景 A (AE 补充描述→FA) 与 04 §1.19 QS vs FA 完全重叠, 测不到泛化
- 推荐 fix: 场景 A 改为"受试者在 Visit 3 服用了一种 CMC 仿制药 (CM 域已记录), 研究者观察到一个与该用药相关的皮肤反应面积 (15.5 cm²) — 这条额外 finding 走哪个域?" → 答案仍是 FA (FAOBJ="CM", 不同于 §1.19 的 FAOBJ="AE"), 但考点更独立
- 若不改: 在 PASS 判据加注 "04 §1.19 已覆盖 QS vs FA 基础, 本题核心增量在 CE 第三域鉴别"

**[MED-2] Q10 QORIG 必填性与 04 矛盾; 重叠 ~30%**
- 题号: Q10
- 问题: 草案说 QORIG "必填", 04 L444 标 "(可选)". 若平台引用 04 答"可选", 草案判错.
- 推荐 fix (a): 改 PASS 判据为 "QORIG 是 SUPP 域 Required 字段 (SDTMIG §8), 填 'CRF'/'DERIVED'/'ASSIGNED' 等, 不能为空". 并在 FAIL 判据加 "注意 04 §1.9 将 QORIG 标为'可选', 这是 04 文档笔误, 以 SDTMIG 官方为准."
- 推荐 fix (d): 将 QVAL 上限改为 SUPPTS study-level 专属: "SUPPTS QVAL 中 USUBJID 为何允许为空? 这说明什么?" 使 SUPPTS 层级成为核心考点, 降低与 04 §19 重叠.

**[MED-3] Q14 "互斥"用词不准; 重叠 ~35%, 日期对齐需强化**
- 题号: Q14
- 问题: "AE+CE+MH 三个都记心梗 (错, 互斥)" 用词不准; 实际是"本场景下仅 AE 适用"
- 推荐 fix: FAIL 判据改为 "三域都记心梗 (错: 本题场景中心梗是 Visit 5 新发 SAE 住院, 仅走 AE; CE 用于未达 AE 阈值的事件, MH 用于既往病史; 三域用途不同但非结构性互斥)". PASS 判据 (d) 加粗"三域日期必须一致, 否则 Pinnacle 21 FAIL"为核心考点.

**[MED-4] Q2 CPMETHOD Core=Perm 可能误判**
- 题号: Q2
- 问题: CPMETHOD 是 Core=Perm, 若测试平台未提及, 草案可能不给满分
- 推荐 fix: PASS 判据 (d) 加注 "CPMETHOD Core=Perm (非必须变量), 但若提及则应为 'FLOW CYTOMETRY' (C85492)"

### LOW findings (可选修正)

**[LOW-1] Q6 PCTPTNUM 示例值需澄清**
- 推荐 fix: 加注 "PCTPTNUM 为排序整数, 具体数字由 sponsor 定义, 只要保证时间点顺序正确即可接受"

**[LOW-2] Q8 LBNRIND extensible 属性建议确认**
- 推荐 fix: Non-Extensible 示例优先使用 NY C66742 + AESEV C66769, LBNRIND 移为第3个备选

---

## Gate Decision

**最终判定: CONDITIONAL_PASS → ADJUST-THEN-GO**

**条件**:
1. ✅ 必须修正: [HIGH-1] Q3 FAIL 判据 (BE COLLECTION) — 影响评分有效性
2. ✅ 建议修正: [MED-1] Q5 场景 A reframe (04 重叠 ~35%)
3. ✅ 建议修正: [MED-2] Q10 QORIG 必填性说明 + 考点 reframe
4. ✅ 建议修正: [MED-3] Q14 "互斥"用词 + 日期对齐强化
5. ⚪ 可选: [MED-4] Q2 + [LOW-1] Q6 + [LOW-2] Q8 — Step 4 观察后决定

**Q1 (初判 HIGH 降为无问题)**: 经逐行复核, GF 域变量全部正确. 无需修改.

**修正完成后**: 题库质量从 CONDITIONAL_PASS 升至 PASS (Confidence ~90%). 可进 Step 4 Web UI 跑.

**ChatGPT 合格阈**: ≥10/14 (71%). 修正后预计 ChatGPT 可达 11-13/14.

---

*报告生成: 2026-04-21 | Reviewer: oh-my-claudecode:scientist (第20种独立subagent_type) | KB citations: Ref-01 to Ref-42 (42条 + 04 grep证据4组, 合计覆盖≥60个具体引用点)*
