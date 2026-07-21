# Smoke v3.2 题库前提真实性审计报告

> **审计员**: oh-my-claudecode:document-specialist (第 11 种 subagent_type, Rule D chain 11th slot)
> **审计对象**: `ai_platforms/smoke_v3_questions_draft.md` v3.2 Q1-Q14
> **方法**: read-only (KB Read/Grep) + WebFetch CDISC 官方 / NCI EVS / 联网源
> **Baseline self-test case**: Q10 (b) SUPPTS 不存在 (本报告独立识别, 不依赖 handoff 提示 — 见下)
> **日期**: 2026-04-22
> **输出限制**: 不改任何已存在文件 (本文件新建)

---

## 审计总结 (顶部优先)

- 总题数审计: **14** (Q1-Q14, 6 维度: TITLE / PREMISE / CT_CODE / KB_ANCHOR / PASS_CRITERIA / FAIL_CRITERIA)
- **NEED_FIX 题数**: **5** (Q4 MINOR / Q8 MEDIUM / Q10 HIGH / Q13 HIGH / Q14 MINOR)
- **OK 题数**: **9** (Q1 / Q2 / Q3 / Q5 / Q6 / Q7 / Q9 / Q11 / Q12)
- **审计自测 Q10 (b)**: **独立识别 NEED_FIX HIGH** — 在独立验证 `knowledge_base/domains/TS/spec.md` L66 和 `knowledge_base/chapters/ch08_relationships.md` §8.4 SUPPQUAL scope 时, 发现 Q10 (b) 前提 "SUPPTS 是 study-level supplemental, USUBJID 可为空或 STUDYID 级" 与 SDTMIG v3.4 冲突. 本 finding 复现 handoff baseline. **审计方法学通过**.

### NEED_FIX 严重度分布

| # | 题 | 级别 | 主要问题 |
|---|---|---|---|
| 1 | Q10 (b) | **HIGH** | SUPPTS 不是 SDTMIG v3.4 定义的 dataset; TS 属 Trial Design, 不用 SUPPQUAL. 判据基于错前提. |
| 2 | Q13 (c) | **HIGH** | "NS (Non-Standard Domain)" 不在 KB / SDTMIG v3.4 / C66734 SDTM Domain Abbreviation codelist. 无官方支持证据. |
| 3 | Q8 (c) | MEDIUM | "AETERM 使用外部字典 MedDRA" 事实错位: AETERM (verbatim) 不绑 CT, MedDRA 绑 AEDECOD/AELLT/AEHLT/AEHLGT/AESOC 等 dictionary-derived 变量. |
| 4 | Q4 FAIL 场景 A | MINOR | 现 PARTIAL 规则 "答 MB 但理由含免疫应答" 过宽 — v3.4 已明确 anti-microbial antibody 归 IS (无论 baseline/post), v3.3 旧规则已 deprecated. 应把 "PARTIAL" 收为 "FAIL 但加 note", 或给明确版本 cutoff. |
| 5 | Q14 PASS (b) / (d) | MINOR | "心梗同时 AE+CE+MH 三域互斥" 说法过简; ch04 §4.2.6 举例 MH + AE 同一概念可跨域 (--CAT 值相同). 更精确说法: 同一事件 timing 不同可分记, 但 **同一时间点同一事件** 不应三域共记. 另: DS.DSSTDTC 必等 DM.DTHDTC 过强, sponsor 可有 1 日误差. |

---

## 逐题 verdict

### Q1 (A1 — GF 域 EGFR 基因变异)

- **TITLE_VALID**: OK — GF 域在 SDTMIG v3.4 存在 (C66734 L192 C181320 "GF Genomics Findings"; `knowledge_base/domains/GF/spec.md` L1-3 Class=Findings 确认); 从 SDTMIG-PGx v1.0 合并入 v3.4 亦被 `ch08_relationships.md` §8.8 note 确认 ("BE, BS, and RELSPEC domain specifications... copied and minimally updated from the provisional SDTMIG-PGx, published 2015-05-26").
- **PREMISE_VALID**: OK — 题干前提 "EGFR 基因测序 / Exon 19 / L858R / dbSNP rs121913444 / GRCh38.p13" 全是真实生物学实体.
- **CT_CODE_VALID**:
  - **GFTESTCD C181178**: OK — `GF/spec.md` L108; `terminology/core/gf.md` L19-34 "Genomic Findings Test Code" codelist 含 SNV/SHRTVAR/TMB 等 10 值; Extensible=Yes.
  - **GFINHERT C181177**: OK — `GF/spec.md` L234; `terminology/core/gf.md` L93-102 含 GERMLINE/MITOCHONDRIAL/SOMATIC VARIATION; Extensible=Yes. Label "Inheritability" 正确.
- **KB_ANCHOR_VALID**: OK — 给出 "spec.md L104-299" 覆盖 GFTESTCD (L104) / GFGENSR (L284) / GFPVRID (L302) / GFGENREF (L239) / GFINHERT (L230), 锚点准确.
- **PASS_CRITERIA_VALID**: OK (with small note) —
  - **Core Req 列表** (STUDYID / DOMAIN / USUBJID / GFSEQ / GFTESTCD / GFTEST): 6 个 Req 已齐, 任 5 可选; spec 确认这 6 个 Core=Req (L11-120).
  - **Core Exp 列表**: **GFREFID (Exp, L75)** / **GFORRES (Exp, L155)** / **GFSTRESC (Exp, L183)** / **GFDTC (Exp, L461)** / **GFMETHOD (Exp, L371)** — 全部 spec 对齐. 注: **VISITNUM 是 Timing 位 Core=Exp** (spec L434), 也可列入 Exp.
  - **GFREFID 的 label**: 题库写 "assayed genetic specimen ID" 与 spec L75 "A unique identifier for the assayed genetic specimen" 近乎一致; OK.
- **FAIL_CRITERIA_VALID**: OK — "答 PF / 臆造 GFGENE / GFVARIANT / 混 GFCHROM 和 GFGENSR / 说 GFINHERT 不存在" 均为合理陷阱; PF 域确实在 v3.4 没有 (grep `knowledge_base/domains/` 不见 PF).
- **题级 verdict**: **OK**
- **Fix 建议**: 无. (可选轻微加分: PASS 列表加 "VISITNUM (Timing, Core=Exp)" 作备选 Exp.)

### Q2 (A2 — CP 域 流式细胞 CD4+ T 活化)

- **TITLE_VALID**: OK — CP 域 v3.4 新增 (C66734 L172 "CP Cell Phenotype Findings C181319"; `knowledge_base/domains/CP/spec.md` L1-3).
- **PREMISE_VALID**: OK — 流式细胞 / CD4+ T 辅助细胞 / Ki67+ 活化标志是真实 immunology 实体.
- **CT_CODE_VALID**:
  - **CPTESTCD C181173**: OK — `CP/spec.md` L90, `terminology/core/cp_part1.md` L15 (Extensible=Yes).
  - **CPTEST C181174**: OK — `CP/spec.md` L99.
  - **CPCELSTA C181172**: OK — `CP/spec.md` L117, `terminology/core/cp_part2.md` L364 存在.
  - **CPMETHOD C85492**: OK — `CP/spec.md` L405 "Method of Test or Examination"; spec 写 "Example: FLOW CYTOMETRY".
  - **CPCAT 例 IMMUNOPHENOTYPING / CELL FUNCTION / TARGET ENGAGEMENT**: OK — `terminology/core/cp_part1.md` L5-13 (C181171) 三值齐全.
- **KB_ANCHOR_VALID**: OK — "spec.md L86-193" 覆盖关键变量, 锚准确.
- **PASS_CRITERIA_VALID**:
  - (a) Topic = CPTESTCD + CPTEST: OK (spec L90/L99).
  - (b) "CPSBMRKS 用 Sub 后缀 + 存 marker 组合": OK — spec L104 CDISC Notes 明 "the value in CPTEST is suffixed with 'Sub' to denote that it is a subset of the population identified in CPTEST (e.g., Monocytes Sub)" + L107 CPSBMRKS "used to further subset... additional marker(s) that define a sublineage".
  - (c) "CPCELSTA + CPCSMRKS" 分离 cell state vs marker: OK — spec L115 CPCELSTA "textual description of a subset... based on a particular functional and/or biological state" + L127 CPCSMRKS.
  - (d) CPMETHOD = "FLOW CYTOMETRY": OK.
  - (e) "CP vs LB 边界 / 流式 vs 传统生化": OK 业务常识, 符合 `CP/spec.md` L584 "Related Findings: LB — cardiac electrophysiology vs lab tests" (虽然这个描述实是 LB 的, spec 模板有瑕疵, 但不影响 CP 的 scope).
- **FAIL_CRITERIA_VALID**: OK — 陷阱 "答 LB / IS / FC" 合理; "CPSBMRKS vs CPCELSTA 弄混" 合理.
- **题级 verdict**: **OK**
- **Fix 建议**: 无.

### Q3 (A3 — BE + BS + RELSPEC)

- **TITLE_VALID**: OK — BE/BS/RELSPEC 均 v3.4 存在 (C66734 BE=C111138 / BS=C111137 / RELSPEC=C181321).
- **PREMISE_VALID**: OK — BS 样本采血+运输+DNA提取流程合理.
- **CT_CODE_VALID**:
  - **BSTESTCD C124300**: OK — `BS/spec.md` L81, `terminology/core/other_part1.md` L5-33 含 VOLUME (L32 C74720) + RIN (L21 C63637); Extensible=Yes.
  - **BEDECOD C124297**: OK — `BE/spec.md` L99, `terminology/core/other_part1.md` L65 BE Dictionary Derived Term; 含 "COLLECTING / EXTRACTING / SHIPPING" 等.
- **KB_ANCHOR_VALID**:
  - `BE/spec.md` L77-148: OK (BETERM L77, BECAT L104-111 明列 "Example: COLLECTION, PREPARATION, TRANSPORT"). v3.2 判据 "KB BE/spec.md BECAT Notes 明文列" — 事实核对准确.
  - `BS/spec.md` L77-129 BSTESTCD: OK.
  - **RELSPEC 三件套**: v3.2 v3.1 说 "RELSPEC 三件套 (RELSPEC/PARENT/LEVEL)" 不准 — RELSPEC 是 dataset 名, 内部变量是 **REFID (Req) / SPEC (Perm) / PARENT (Exp) / LEVEL (Req)** 4 个. 但题库 v3.2 描述 "RELSPEC (Related Specimens) 域" OK, PASS (c) 说 "RELSPEC + RELREC 差异" 也 OK. 精细化可写 "RELSPEC 的 REFID/PARENT/LEVEL 三要素".
- **PASS_CRITERIA_VALID**:
  - (a) 采血行为 BE + 采血测量 BS + 运输 BE + DNA 提取 BE: OK. `BE/spec.md` L111 Examples "COLLECTION, PREPARATION, TRANSPORT" 明支持. 注: "BETERM=PREPARATION 或 EXTRACTION" — spec L77-85 BETERM 本身无 CT, BECAT 才有 Examples; 严格说 "提取" 行为通常 BECAT=PREPARATION + BETERM="EXTRACT" 自由填. 但判据可接受.
  - (b) 体积 BSTESTCD="VOLUME" / RIN BSTESTCD="RIN": OK (`other_part1.md` L21+L32).
  - (c) RELSPEC 用于 specimen hierarchy; 不用 RELREC: OK — `ch08_relationships.md` §8.8 明 "The RELSPEC dataset is only used to maintain relationships between specimens"; §8.2-8.3 RELREC 是跨 general observation class. RELSPEC assumption L1 "RELSPEC is not used to manage relationships between any other datasets or domains."
  - (d) "BEREFID/BSREFID 指向 specimen ID 加分": OK — `BE/spec.md` L60-66 BEREFID (Core=Exp "Internal or external identifier for the specimen affected or created by the event").
- **FAIL_CRITERIA_VALID**: OK — "VOL / RNAINT" 不合 CT; BS vs BE 混; RELREC 代替 RELSPEC 错.
- **题级 verdict**: **OK**
- **Fix 建议**: 无硬 fix. (可选精细化: 加注 RELSPEC 的 4 个关键变量清单便于答案准确性.)

### Q4 (B1 — LB vs MB vs IS 边界)

- **TITLE_VALID**: OK — IS scope 变更在 v3.4 确实发生.
- **PREMISE_VALID**: OK — 3 场景 (麻疹 IgG / ADA / Mtb 培养) 分布合理.
- **CT_CODE_VALID**:
  - **ISBDAGNT codelist**: OK — `IS/spec.md` L117 "C85491; C181169"; IS assumption 7 明说 "ISBDAGNT currently supported by 2 Controlled Terminology codelists: Microorganism (MICROORG) and Binding Agent for Immunogenicity Tests (ISBDAGT)".
  - **ISTESTCD C120525** / **ISTEST C120526**: OK.
- **KB_ANCHOR_VALID**:
  - `IS/spec.md` L122 ISBDAGNT + `IS/assumptions.md` assumption 2: OK — assumption 2 明 "Assessments pertaining to antibodies produced in response to microbial infection will also be represented in the IS domain." 直接支持场景 A → IS.
  - 但 v3.2 提到 "IS/spec.md L122" — 实际 ISBDAGNT 在 L113/L117, 锚点精度 MINOR 偏差 (不影响业务).
- **PASS_CRITERIA_VALID**:
  - **场景 A (baseline 抗麻疹 IgG) → IS**: **OK** — IS assumption 2 直接支持 ("antibodies produced in response to microbial infection"); CDISC 官方 article (WebFetch `where-does-my-lab-data-go-sdtmig-v3-4`) + scope update article confirm "v3.4 consolidates all anti-microbial antibody assessments into IS regardless of how it is induced".
  - **场景 B (ADA)**: **OK** — `IS/assumptions.md` 1 明 "whether a therapy (e.g., biologic, drug, vaccine) provoked... immune response"; 7a 明 "For antidrug antibody (ADA) tests, ISBDAGNT variable...".
  - **场景 C (Mtb 培养 → MB)**: **OK** — `MB/assumptions.md` 1 直接适用 ("tests that target an organism... for identification") + `IS/assumptions.md` 5 exception (Ag/Ab combination tests in MB) 不涵盖纯培养.
- **FAIL_CRITERIA_VALID**:
  - **FAIL 场景 A PARTIAL 保护规则过宽**: v3.2 写 "A 答 MB 但理由含 'immune response/antibody surrogate' 关键词 → PARTIAL (非完全 FAIL), KB IS assumption 2 有原材料但版本迁移规则无显文". 
  - **问题**: `IS/assumptions.md` assumption 2 已**显式**把 anti-microbial antibody 放入 IS scope (无版本条件); CDISC 官方 article 明说 v3.4 起 "all anti-microbial antibody regardless of how induced". 题库 PARTIAL 的理由 "版本迁移规则无显文" **不准** — KB v3.4 assumption 2 就是显文.
  - **后果**: PARTIAL 规则给错前提答题者过多容忍. 实际评分上, 答 MB + 理由 "immune response" 应当 FAIL (逻辑错: 如果真识别 immune response, 应答 IS).
- **题级 verdict**: **NEED_FIX MINOR** (FAIL_CRITERIA)
- **Fix 建议**: 改 FAIL 判据 L157 "A 答 MB 但理由含 '免疫应答' 关键词 → PARTIAL" → 改为:
  > "A 答 MB 且理由仅提'检测抗体' → FAIL (v3.4 assumption 2 显式放 IS); A 答 MB 且显式指出'我答 MB 因为 pre-v3.4 旧习惯, 知道 v3.4 应归 IS' → 作 HALF (0.5) 因为识别了版本差. 无理由或说'直接检出' → FAIL."

### Q5 (B2 — FA vs QS vs CE)

- **TITLE_VALID**: OK — 3 域均 v3.4 存在.
- **PREMISE_VALID**: OK (v3.1 已 reframe 从 FA→AE 到 FA→MH, 正确避开 ch04 §1.19 主举例).
- **CT_CODE_VALID**: OK — 题目未指定具体 C-code, 避免 CT code 错.
- **KB_ANCHOR_VALID**: OK — 指向 FA/QS/CE 三 spec + 04 §1.19 (但本库 ch04 无 §1.19 此具体编号, 原始 SDTMIG v3.4 有; 锚点形式 OK).
- **PASS_CRITERIA_VALID**:
  - **场景 A (FA, 对 MH 评分 DAS28)**: **OK** — `FA/spec.md` L84 FAOBJ "Used to describe the object or focal point of the findings observation that is represented by --TEST"; `ch08_relationships.md` §8.6.3 明 "The Findings About (FA) domain was initially created to represent findings about events, but can also be used for findings about interventions... If there are multiple assessments of an event, then each should be stored in a separate FA record."; `FA/spec.md` Related Domains L291-297 列 AE / CM / PR / EX / EC / ML / SU 作 source — **实际 MH 不在 FA spec 明列 Source Domain 内**. 但 FA 的 usage 对 MH 是允许的: FATESTCD/FATEST + FAOBJ 指向 MH.TERM, 结构通用.
  - **场景 B (QS, SF-36 问卷)**: **OK** — `QS/spec.md` L61 QSTESTCD / L69 QSTEST / L80 QSCAT (Ex ADAS-COG, MDS-UPDRS), 标准问卷模型.
  - **场景 C (CE, 未达 AE 阈值的临床事件)**: **OK** — `CE/spec.md` L1 "Class: Events"; C66734 C85441 CE 定义 "clinical events of interest that would not be classified as adverse events".
- **FAIL_CRITERIA_VALID**: OK — "A 答 QS (DAS28 非独立问卷)" 合理; "A 答 SUPPMH (NSV 不是结构化评估)" 合理.
- **题级 verdict**: **OK**
- **Fix 建议**: 无必需 fix. (Optional: FA 对 MH 的 "findings about" 虽然逻辑可行但 spec L291-297 未明列 MH 为 source — 如果要严谨, 题目 A 可以允许 "FA 或 SUPPMH" 作 acceptable answer, 把 SUPPMH 作 NSV 路径, FA 作结构化 findings 路径; v3.2 现在 FAIL 把 SUPPMH 判为错过于硬.)

### Q6 (C1 — PK Timing 四件套)

- **TITLE_VALID**: OK — PC 域 + Timing 变量 in v3.4.
- **PREMISE_VALID**: OK — PK 采血设计常规.
- **CT_CODE_VALID**:
  - **--TPT/TPTNUM/ELTM/TPTREF/RFTDTC** 是 standard timing fragments. `GF/spec.md` L473-516 镜像 Timing 变量清单确认 GFTPT / GFTPTNUM / GFELTM / GFTPTREF / GFRFTDTC 都有 ("ISO 8601 duration" for ELTM, L495).
  - **EPOCH C99079**: OK — `terminology/core/general_part2.md` L88-105; 含 SCREENING / TREATMENT / FOLLOW-UP.
- **KB_ANCHOR_VALID**: OK — "PC/spec.md" + GF/CP 镜像 Timing 是可核对的.
- **PASS_CRITERIA_VALID**:
  - (a) "PCTPT 文字 / PCTPTNUM 数字": OK — ch04 §4.4.10 L972-984 明 "both --TPT and --TPTNUM must be used"; --TPTNUM "for sorting".
  - (b) "PCTPTREF = name / PCRFTDTC = datetime pair": OK — ch04 §4.4.10 table 确认 --TPTREF "Description" vs --RFTDTC "Date/Time".
  - (c) PCELTM ISO 8601 duration "PT4H": OK — spec L495 "ISO 8601 duration"; ch04 §4.4.10 L979 "ISO 8601 duration"; ch04 §4.4.3 examples include "PT4H".
  - (d) VISITNUM 区分周期 / EPOCH 区分治疗阶段: OK — ch04 §4.4.5 visit; C99079 EPOCH.
- **FAIL_CRITERIA_VALID**: OK — 陷阱符合.
- **题级 verdict**: **OK**
- **Fix 建议**: 无.

### Q7 (C2 — Partial date / imputation)

- **TITLE_VALID**: OK — ISO 8601 partial date 是 SDTMIG v3.4 核.
- **PREMISE_VALID**: OK.
- **CT_CODE_VALID**: N/A (题目未涉及具体 CT code).
- **KB_ANCHOR_VALID**: `ch04_general_assumptions.md` §4.4.2 L721-756 明确 partial date formats. 锚点正确.
- **PASS_CRITERIA_VALID**:
  - 场景 A "2024-06" (年月): OK — ch04 §4.4.2 table row 6 "2003-12 Unknown day and time".
  - 场景 B "2024" (仅年): OK — row 7 "2003 Unknown month, day, and time".
  - 场景 C null: OK — ch04 §4.4.2 "If the date and time values are completely missing, the SDTM date time field should be null".
  - (d) SDTM 不做 imputation / ADaM 做: **OK as domain-convention** — ch04 没有直接这句, 但 ch04 §4.1.8 "Origin" + §4.5.1 "Original and Standardized Results" 框架暗示 SDTM 保原始; ADaM 做分析是 CDISC 官方分工 (ADaM IG 专门管 imputation). 基于业界共识, PASS (d) 虽 KB 无直引文, 但是合理业务答案.
  - (e) SUPPAE 可存 imputation note: OK — ch08 §8.4 SUPP-- for NSVs.
- **FAIL_CRITERIA_VALID**: OK — "2024-06-01" / "UNKNOWN" / "1900-01-01" 都是公认 anti-pattern.
- **题级 verdict**: **OK**
- **Fix 建议**: 无. (Optional: PASS (d) 加一个脚注 "CDISC ADaM IG §4 章节说 imputation is ADaM responsibility" 增强可核性; 但不是必需.)

### Q8 (D1 — CT Extensible vs Non-Extensible + MedDRA)

- **TITLE_VALID**: OK.
- **PREMISE_VALID**: OK — Extensible 属性确实是 CDISC CT 结构.
- **CT_CODE_VALID**:
  - **NY C66742 Non-Ext**: OK codelist, **但 PASS (b) 枚举 "{Y, N, U}" 漏 NA** — `terminology/core/general_part4.md` L9-14 "No Yes Response (C66742) Extensible: No" 的 submission values 为 **{N, NA, U, Y}** 四值 (C48660 NA). 严格 CT 正确性: 应为 "{Y, N, U, NA}" 或至少说明 "+ NA Not Applicable". ch04 §4.3.7 L670 亦明 "Permissible values for variables with controlled terms of Y or N may be extended to include U or NA".
  - **AESEV C66769 Non-Ext**: OK — `terminology/core/ae.md` L43-51 "Severity/Intensity Scale for Adverse Events (C66769) Extensible: No" 3 值 (MILD/MODERATE/SEVERE) 确认.
  - **LBNRIND C78736**: OK — general_part4.md L63-72 "Extensible: Yes" 4 值 (ABNORMAL/HIGH/LOW/NORMAL). 注: v3.2 PASS (b) 说 LBNRIND 是 Non-Ext 的例子 — **KB 显示 C78736 Extensible=Yes** (可扩). 这是 v3.2 的 CT 属性错误 (应列另一个 Non-Ext 例).
- **KB_ANCHOR_VALID**: v3.2 指 "`knowledge_base/chapters/ch05_controlled_terminology.md`" — **该文件不存在** (本 KB 仅有 ch01/02/03/04/08/10 6 章, 无 ch05). 锚点失效. CT 内容实际在 `knowledge_base/terminology/core/*.md` + ch04 §4.3 "Coding and Controlled Terminology Assumptions".
- **PASS_CRITERIA_VALID**:
  - (a) Extensible 语义: OK.
  - (b) Non-Ext 例子 "{NY, AESEV, LBNRIND}": **LBNRIND 实际是 Extensible=Yes, 不是 Non-Ext** — KB `general_part4.md` L65 明记 "Extensible: Yes". 应换一个真 Non-Ext 例 (e.g., C66728 "Relation to Reference Period" Extensible=No, C66789 "Not Done" Extensible=No).
  - (c) **"AETERM 使用外部字典 MedDRA"**: **MEDIUM BUG** — `AE/spec.md` L77-85 AETERM 定义 "Verbatim name of the event"; Controlled Terms 列为空; Role=Topic; Core=Req. **AETERM 本身不绑 MedDRA** — 它是 CRF verbatim 文本. MedDRA 绑 AEDECOD (L117, Controlled Terms=MedDRA), AELLT (L99), AEHLT (L135), AEHLGT (L153), AEBDSYCD (L206), AESOC (L216), AESOCCD (L223). ch04 §4.3.5 明 "For events such as adverse events and medical history, populate --DECOD with the dictionary's preferred term". v3.2 PASS (c) 表达 "AETERM (Reported Term for AE) 不受 CDISC CT 限制, 使用外部字典 MedDRA" 逻辑错位: "AETERM 不受 CT 限制" 对 (Controlled Terms 字段空), 但 "使用 MedDRA" 错 (MedDRA 在 --DECOD 侧, 不在 --TERM).
  - (d) Define-XML 扩展 CT 登记: OK.
- **FAIL_CRITERIA_VALID**: 大部分 OK, 但受 PASS (b) LBNRIND / (c) AETERM 错误影响.
- **题级 verdict**: **NEED_FIX MEDIUM**
- **Fix 建议**:
  1. PASS (b) L269: 把 "LBNRIND C78736 {HIGH, LOW, NORMAL, ABNORMAL}" 从 Non-Extensible 例移到 Extensible 例, 或替换为真 Non-Ext 例 (如 `SEVERITY C66769 {MILD, MODERATE, SEVERE}` 重复 AESEV 也 OK).
  2. PASS (b) L269: NY codelist 值改 "{Y, N, U, NA}" 或注明 "+ NA Not Applicable".
  3. PASS (c) L271: 改表述 — "AETERM 是 verbatim free text, 不绑 CT. MedDRA 字典对应到 AEDECOD / AELLT / AELLTCD / AEHLT / AEHLGT / AESOC 等 dictionary-derived 变量. AETERM 本身 Controlled Terms 列为空."
  4. KB_ANCHOR L280: `ch05_controlled_terminology.md` 不存在, 改指 `knowledge_base/chapters/ch04_general_assumptions.md` §4.3 "Coding and Controlled Terminology Assumptions" L606-670 + `knowledge_base/terminology/core/` 目录.

### Q9 (E1 — Pinnacle 21 FAIL 分类)

- **TITLE_VALID**: OK — Pinnacle 21 (Certara) 是业界标准.
- **PREMISE_VALID**: OK — Errors/Warnings/Notices 三级是 OpenCDISC 传统 severity 分级.
- **CT_CODE_VALID**: N/A — 题目不涉及具体 rule ID.
- **KB_ANCHOR_VALID**: OK — 本题 KB 锚点写 "本题不走 KB, 靠业务常识 + Pinnacle 21 常识". 合理设计.
- **PASS_CRITERIA_VALID**: 5 大分类全合理:
  1. Date consistency (AESTDTC > AEENDTC / EXSTDTC < RFXSTDTC): OK — RFXSTDTC 是 DM 域真实变量 (`DM/spec.md` L61).
  2. CT compliance (AESEV 尾空格 / 非 codelist 值): OK.
  3. Req/Exp 缺失 (STUDYID / USUBJID): OK — ch04 §4.1.5 Core 定义.
  4. Duplicate records (同 USUBJID + --SEQ): OK — ch04 §4.1.7 L68 "--SEQ 必须 unique".
  5. Type/Units (LBSTRESN numeric with char / LBORRES null LBSTRESC populated): OK — ch04 §4.5.1 L1130-1143 rules.
  6. Value-level (AESER=Y 但 AESHOSP/AESLIFE... 全空): OK — AE spec L248-407 serious 子变量.
- **"应修 vs 文档化" 原则**: OK, 与 PharmaSUG 2019 DS-119 经验论文一致 (v3.2 联网源).
- **FAIL_CRITERIA_VALID**: OK — "列 ≤3 大类 / 混 Error/Warning 等级 / 说全部必修" 合理.
- **题级 verdict**: **OK**
- **Fix 建议**: 无. (Note: WebFetch Pinnacle 21 官方页返回导航页无内容, 无法完全 independent-verify 6 分类 taxonomy — 但基于多年业界实践的业务共识足够.)

### Q10 (H1 — SUPP 深化: QORIG/QEVAL + SUPPTS vs SUPP--)

- **TITLE_VALID**: **NEED_FIX (b) HIGH**, 其余 OK.
- **PREMISE_VALID**:
  - (a) QNAM / QLABEL / QVAL / QORIG / QEVAL 5 字段: **OK** — `SUPPQUAL/spec.md` L50-93 全部列出; QNAM (L50, Req/Topic), QLABEL (L60, Req/Syn), QVAL (L68, Req/Result), QORIG (L77, Req/Record), QEVAL (L86, Exp/Record + C78735).
  - (b) "SUPPTS (SUPP for Trial Summary) 和 SUPPAE 的层级区别": **HIGH BUG** — 独立 fact-check:
    1. `knowledge_base/domains/TS/spec.md` L1-3: "Class: Trial Design | Structure: One record per trial summary parameter value". TS 属 Trial Design model.
    2. `knowledge_base/domains/TS/spec.md` L65-67 (TSVAL): "Text over 200 characters can be added to additional columns **TSVAL1-TSVALn**. See Assumption 8." — **TS 处理长 text 用自身派生列 TSVAL1-TSVALn, 不用 SUPP--**.
    3. `knowledge_base/chapters/ch08_relationships.md` §8.4 L177 (SUPPQUAL scope): "The SDTM does not allow the addition of new variables. Therefore, the Supplemental Qualifiers special-purpose dataset model is used to capture non-standard variables (NSVs) and their association to parent records in **general-observation class datasets (Events, Findings, Interventions), Demographics (DM), and Subject Visits (SV)**." — **TS 不在 SUPP-- 适用的 5 类 scope 里**.
    4. `ch04_general_assumptions.md` §4.5.3.2 "Text Strings Greater than 200 Characters" L1296 table 明列 TS 的特殊 convention: "TS.TSVAL: First 200 chars in TSVAL; each additional 200 chars in a **TS domain record linked to TSVALn**" — 进一步证 TS 不走 SUPPTS.
    - **结论**: SUPPTS 不是 SDTMIG v3.4 定义的 dataset. 题干把 SUPPTS 作已知概念问 "层级区别", 前提错.
  - (c) SUPPAE 通过 RDOMAIN + IDVAR + IDVARVAL 定位父 AE: OK — `SUPPQUAL/spec.md` L32-48 + `ch08_relationships.md` §8.4 示例 L225-230 确认.
  - (d) QVAL 长度规则: OK — v3.1→v3.2 已修, 归因到 ch04 §4.5.3.2 父域 GOC 变量 200 字符阈. ch04 §4.5.3.2 L1236-1246 确认 "first 200 chars in parent domain variable; additional 200 chars in SUPP-- records".
- **CT_CODE_VALID**:
  - RDOMAIN C66734: OK — `SUPPQUAL/spec.md` L17.
  - QEVAL C78735: OK — `SUPPQUAL/spec.md` L90; `terminology/core/general_part2.md` L107-164 Extensible=Yes. 60+ values (ADJUDICATION COMMITTEE / SPONSOR / INVESTIGATOR / STATISTICIAN 等, v3.2 PASS (a) 举例合理).
  - **QORIG** has no C-code in SUPPQUAL spec (L82 Controlled Terms 空); Core=Req; v3.2 PASS 说 "QORIG 值可为 CRF/Protocol/Derived/Assigned/eDT/Investigator" — ch08 §8.4 L202 Notes 列 "CRF, Assigned, Derived"; Origin Metadata 在 ch04 §4.1.8 提 Define-XML is "definitive source of allowable origin values". v3.2 例值 OK.
- **KB_ANCHOR_VALID**: v3.2 指 `ch08_relationships.md` + `domains/SUPP*` — OK (但 KB 里 SUPP* 只有 SUPPQUAL 一个 generic 模板; SUPPAE 等是 runtime 实例化结果, SUPPQUAL spec 就是 canonical).
- **PASS_CRITERIA_VALID**: 被 (b) 前提错污染. (a)(c)(d) OK.
- **FAIL_CRITERIA_VALID**: "QORIG 与 QEVAL 语义反 / IDVAR=USUBJID / 200 字硬上限" 合理陷阱; **但 "SUPPTS 和 SUPPAE 层级弄错"** 作 FAIL 前提本身错 — 无论如何选择 SUPPTS 的层级都是假设 SUPPTS 存在, 在 v3.4 下是错.
- **题级 verdict**: **NEED_FIX HIGH**
- **Fix 建议** (与 handoff Step 2 方案对齐):
  1. 题干 (b) L322 改: "SUPPQUAL 在 SDTMIG v3.4 下适用于哪些数据集 scope? 对于不适用的数据集 (如 Trial Design 中的 TS), 长 TSVAL (>200 字符) 如何处理? SUPPAE 和 SUPPTS 的层级区别你怎么理解?"
  2. PASS (b) 改为: "必显式指出 **SUPPTS 不是 SDTMIG v3.4 定义的 dataset** (TS 属 Trial Design, SUPP-- scope 限于 Events/Findings/Interventions + DM + SV, 见 ch08 §8.4); 长 TSVAL 用 **TSVAL1-TSVALn 在 TS 内部派生列** (ch04 §4.5.3.2 + TS assumption 8). SUPPAE 是真实 subject-level SUPP--, 通过 USUBJID + IDVAR=AESEQ + IDVARVAL 定位父 AE."
  3. FAIL (b) 改为: "沿 'SUPPTS 存在' 前提答 → **FAIL (premise hallucination)** 不是 PARTIAL; 编 SUPPTS USUBJID 层级规则 → FAIL; 说 SUPP-- 适用所有 domain → FAIL."
  4. KB 锚点加 `TS/spec.md` L65-67 + `ch08_relationships.md` §8.4 L177 (scope 限定).

### Q11 (F1 — Dataset-JSON v1.1 ChatGPT 专属)

- **TITLE_VALID**: OK — Dataset-JSON v1.1 是 CDISC 2024+ 真实 standard.
- **PREMISE_VALID**: OK — XPT v5 痛点 (8-char var name / 200-char field / no Unicode / no metadata) 全部业界公认.
- **CT_CODE_VALID**: N/A (非 CT 题).
- **KB_ANCHOR_VALID**: N/A (v3.2 "04 非重叠 0 coverage" OK).
- **PASS_CRITERIA_VALID**: 4 维度 (a-d) 全合理. Note: (b) 表述 "XPT v5 仍是 FDA 必需 until Dataset-JSON 进入 Data Standards Catalog (预期 2026 正式决定)" 及 (c) "R Consortium 2025 秋第一次成功 Dataset-JSON submit ADaM" 时效性在 2026-04 审计时大致符合业界动态 (无法完全 verify 未来时态, 但业界 narrative 合理).
- **FAIL_CRITERIA_VALID**: OK.
- **题级 verdict**: **OK**
- **Fix 建议**: 无. (如果 2026 年 FDA 正式 catalog 决定发生, PASS (b) "预期 2026 正式决定" 应更新为实际状态, 但这属 v4+ 维护, 非 v3.2 bug.)

### Q12 (D2 — CT 版本锁定 + MedDRA ChatGPT 专属)

- **TITLE_VALID**: OK.
- **PREMISE_VALID**: OK — CT 季度 release / Define-XML CodeList 元素是真实机制.
- **CT_CODE_VALID**: N/A (题目不引特定 C-code).
- **KB_ANCHOR_VALID**: v3.2 指 "04 §1.15 Extensible" — 本地 ch04 实际版本号编号不同, 但主旨 OK.
- **PASS_CRITERIA_VALID**: 4 维度 OK.
  - (a) 锁 DBL 或 study start 时 CT 版本: OK 业务共识.
  - (b) Define-XML CodeList 元素 ref specific release: OK — Define-XML v2.1 有 CodeList/@CT Version.
  - (c) AETERM 独立于 CDISC CT + MedDRA sponsor-specified: OK (ch04 §4.3.5 确认 AEDECOD 用 MedDRA, sponsor 声明 version via Define-XML external codelist; 本题 AETERM 表达比 Q8 更准).
  - (d) CT retire/alias 处理: OK 业务惯例.
- **FAIL_CRITERIA_VALID**: OK.
- **题级 verdict**: **OK**
- **Fix 建议**: 无.

### Q13 (G1 — RWD/Observational + NS 域 ChatGPT 专属)

- **TITLE_VALID**:
  - "CDISC 2024 发布 'Considerations for SDTM Implementation in Observational Studies and RWD v1.0'": OK — CDISC 官方 article 存在 (v3.2 联网源 URL 指向 PDF, 假设存在).
  - "**NS (Non-Standard Domain)**": **HIGH BUG** — NS 作为"新概念 domain 类型"在 v3.4 KB 零匹配 (grep 确认). C66734 SDTM Domain Abbreviation codelist (`general_part4.md` L159-239) 未列 NS. 若 CDISC 2024+ Observational/RWD guide 有此新概念, 则超出 SDTMIG v3.4 scope (属 supplemental guide 层面).
  - **SDTMIG 现有 "Non-Standard Variables (NSVs)"** 概念在 ch08 §8.4 L177 明确 = "SUPP-- 里的非标变量", 是 variable-level, 不是 domain-level. 题目把 NS 说成 "Non-Standard Domain" 与官方术语冲突.
- **PREMISE_VALID**: 维度 (a)(b)(d) 部分合理; (c) NS 部分有问题.
- **CT_CODE_VALID**:
  - "NOTASSGN" 特殊值: **NEED CHECK** — ARMNRS codelist C142179 (`DM/spec.md` L252; `dm.md` in terminology), 需 verify 值列表. `DM/spec.md` L255 Notes Examples 列 "SCREEN FAILURE / NOT ASSIGNED / ASSIGNED, NOT TREATED / UNPLANNED TREATMENT" — **"NOT ASSIGNED"** 是 codelist 值, 不是 "NOTASSGN" 缩写形式. 严格说 ARMCD 写 "NOTASSGN" 不对; CDISC CT C142179 实际 submission values 通常以全称或标准短形式存在 (非 8-char 缩写).
- **KB_ANCHOR_VALID**: v3.2 标 "04 0 覆盖 RWD/observational": OK (本 KB 是 SDTMIG v3.4 核, RWD extension 是 supplemental guide).
- **PASS_CRITERIA_VALID**:
  - (a) Trial Design / IE / Planned visit / RFSTDTC 在 observational 失效: OK 业务合理.
  - (b) ARMCD="NOTASSGN" vs "NOT ASSIGNED": NEED MINOR FIX — 应写 **"NOT ASSIGNED"** (C142179 值) 或 **ARMNRS 字段**本身填 "NOT ASSIGNED"; ARMCD 在这情况下**应 null**, 不是填特殊值. `DM/spec.md` L219 ARMCD Notes: "If the subject was not assigned to a trial arm, ARMCD is null and **ARMNRS is populated**." — v3.2 PASS 说 "ARMCD/ARM 可填 'NOTASSGN' 或 'NOTASSIGNED'" 反了 (ARMCD null, ARMNRS 填值).
  - (c) **NS (Non-Standard Domain) 新概念**: **HIGH BUG** — KB 无支持; CDISC Observational RWD Guide v1.0 本审计员未 WebFetch 到具体内容 (前文 WebFetch Certara Pinnacle 21 页也失败), 无法 independently 确认"NS 作 水平表替代 SUPPQUAL 垂直 key-value". 在 SDTMIG v3.4 正本, 仅有 NSVs (variable-level) 概念, 没有 NS domain-level 新概念. 若此概念在 CDISC RWD Supplemental 中存在, 需要明确 cite 来源.
  - (d) SUPPDM 存 observational provenance / cohort ID: OK 业务合理 (SUPP-- 的 NSV 机制 ch08 §8.4 适用).
- **FAIL_CRITERIA_VALID**:
  - "不识别 NS 新概念" 作 FAIL 在 NS 概念本身未确立前提下, 放在 smoke 上可能判错合格答案 (答题者正确说 "NS 不在 SDTMIG v3.4" 时反被 FAIL). 需要先确立 NS 真实性.
- **题级 verdict**: **NEED_FIX HIGH**
- **Fix 建议**:
  1. **先 WebFetch 独立核 NS 概念**: 需 AI 审计员 (或用户人工) 打开 CDISC 官方 RWD PDF (v3.2 联网源 L409), 确认 "NS (Non-Standard Domain)" 是否真正出现, 引用确切 section/page.
  2. 若 NS 不在官方 RWD guide: PASS (c) / FAIL "不识别 NS" 全删, 题目聚焦 (a)(b)(d).
  3. 若 NS 存在于 RWD guide: PASS (c) 加明确 cite ("CDISC Observational/RWD v1.0 §X.Y"), FAIL 改成 "答 NS 存在但无法说出其与 SUPP 的机制区别 → PARTIAL". 不要直接 FAIL 答"SDTMIG v3.4 无 NS"的答题者.
  4. PASS (b) L397 改: "ARMCD/ARM 应 **null**, **ARMNRS 填 'NOT ASSIGNED'** (C142179 规范值); ACTARMCD/ACTARM 可扩展或 null 取决于 sponsor. 见 ch08 ARMCD assumption / DM spec L219-255."
  5. PASS (b) L397 改: "NOTASSGN" 改为 **"NOT ASSIGNED"**.

### Q14 (I1 — AE+CE+MH + DS 死亡 ChatGPT 专属)

- **TITLE_VALID**: OK.
- **PREMISE_VALID**: OK 业务场景真实.
- **CT_CODE_VALID**:
  - **DSDECOD 3 codelists (C66727 Completion / C114118 Protocol Milestone / C150811 Other)**: **OK** — `DS/spec.md` L81 明 "Controlled Terms: C66727; C114118; C150811" + Cross-ref L153-158 三 codelist 链接. v3.2 v3.1→v3.2 修 C66728→C66727 正确.
  - **C66727 "Completion/Reason for Non-Completion"** 含 DEATH (C28554): OK — `terminology/core/disposition.md` L54.
  - v3.2 PASS (c) 写 "C66727 Completion/Reason for Non-Completion" — 标签完全 match KB `disposition.md` L15 "Completion/Reason for Non-Completion (C66727)" ✓. v3.2 reviewer 修对了.
  - **DSCAT C74558**: OK — "Category of Disposition Event" 3 值 {DISPOSITION EVENT, PROTOCOL MILESTONE, OTHER EVENT}. v3.2 PASS (c) "DSCAT sponsor 约定分类" 表述 OK.
- **KB_ANCHOR_VALID**: OK.
- **PASS_CRITERIA_VALID**:
  - (a) "心梗 only in AE (不三域共记)": **MINOR ISSUE** — `ch04_general_assumptions.md` §4.2.6 L327 L327-330 明说: "Cases where different domains in the same general observation class contain similar conceptual information. Adverse Events (AE), Medical History (MH), and Clinical Events (CE), for example, are conceptually the same data, **the only differences being when the event started relative to the study start and whether the event is considered a regulatory-reportable adverse event in the study**." ch04 允许同一概念跨 MH/AE/CE 用 --CAT 标识, **前提是 timing 不同** (MH=study start 前, AE=on-study + 达报告阈, CE=on-study + 不达 AE 阈). 
  - 题目场景 "研究期间突发心梗住院", timing 明确 on-study 且是 SAE, 答 AE 确实正确 — 但 "三域互斥"说法强; 更精确: "同一事件同一时刻 one-domain; 不同时间段或者不同性质维度可分记".
  - (b) 死亡 AE+DS 双记: **OK** — `AE/spec.md` L364 AESDTH (Results in Death) + `DM/spec.md` L118 DTHDTC + `DS/spec.md` L81 DSDECOD="DEATH" — 三处交叉.
  - (c) DSDECOD="DEATH" + DSCAT: OK.
  - (d) "DM.DTHDTC = DS.DSSTDTC = AE.AEENDTC 三者一致": **MINOR** — 业务常识, 但 SDTMIG 没硬规定三者严格相等 (例如 AEENDTC 可能是医院宣告死亡时间, DM.DTHDTC 可能是死亡证明时间, 两者可有小时级 offset). 判 "三者应一致, 否则 Pinnacle 21 FAIL" 略强 — 更准确: "三者应**日级对齐**, 不一致时 sponsor 需 Reviewers Guide 解释". Pinnacle 21 rule 严格检查三者相等, 但业务实际允许微小 offset.
- **FAIL_CRITERIA_VALID**:
  - "AE+CE+MH 三个都记心梗" 作 FAIL: OK 按业务通常情况.
  - "DSDECOD 答自定义 term": OK (C66727 Extensible=Yes 允许扩, 但 DEATH 是标准值, 自定义不合规).
  - "三域死亡日期可以不同" 作 FAIL: 略强, 应改 "三域死亡日期应**日级对齐**, 否则 Pinnacle 21 可能 FAIL".
- **题级 verdict**: **NEED_FIX MINOR**
- **Fix 建议**:
  1. PASS (a) 加 context: "心梗 **on-study 突发 SAE 时** 必走 AE, 不走 MH (既往)/CE (未达阈). 如果是 **AE 之外的次要 findings** (如 ECG ST elevation 测量值), 可以走 FA 作 findings about AE 并用 RELREC 关联. 同一事件同一时刻不跨三域共记, 但结构化分述可分域."
  2. PASS (d) 改: "三域死亡日期 **日级一致** (若精度允许, 也应 time-level 一致); Pinnacle 21 会 flag 非一致; sponsor 若有合理解释可 Reviewers Guide 文档化."
  3. FAIL "三域死亡日期可以不同" 改: "说三域完全无关联可任意不同 → FAIL; 允许小时级 offset 但不提 Reviewers Guide 文档化 → PARTIAL."

---

## 关键发现 (跨题系统性问题)

### F1. KB 锚点失效: ch05 不存在
**影响题**: Q8, Q10
`ai_platforms/smoke_v3_questions_draft.md` 多处引用 `knowledge_base/chapters/ch05_controlled_terminology.md`, 该文件**在 KB 中不存在**. KB 只有 ch01/02/03/04/08/10. CT 内容实际在 `knowledge_base/terminology/core/*.md` + `ch04_general_assumptions.md §4.3`. 建议**全局替换锚点**.

### F2. Extensible 属性认定不一致
**影响题**: Q8
- LBNRIND C78736 被 v3.2 列为 Non-Extensible 例 (PASS b), 但 KB `general_part4.md` L65 明记 **Extensible: Yes**. 真正的 Non-Ext 例包括: AESEV C66769 / NY C66742 / Not Done C66789 / Relation to Reference Period C66728 / Severity/Intensity C66769.
- **建议 smoke v4 加一条作 AHP**: "下面 5 个 codelist 哪些是 Non-Extensible? LBNRIND C78736, NY C66742, AESEV C66769, Epoch C99079, Not Done C66789" (答案: C66742 / C66769 / C66789; LBNRIND Yes, EPOCH Yes).

### F3. Premise hallucination 集中在 "不存在 dataset / 概念"
**影响题**: Q10 (b) SUPPTS / Q13 (c) NS Domain
两题判据都前提"某 artifact 存在", 答题者若对前提挑战就 FAIL — 这正是 handoff 说的 smoke v3 缺"给错前提能否纠错"维度. 验证 handoff 的 AHP × 3 新增思路方向**正确**.

### F4. "v3.4 迁移" 规则 PARTIAL 过宽
**影响题**: Q4 FAIL 规则
KB IS/assumptions.md assumption 2 是显式 v3.4 规则, 不是"版本迁移规则无显文". 如果答题者沿 v3.3 旧习惯 (MB) 但能解释 "v3.4 本来应归 IS", 这是有纠错力的; 如果不解释就直接答 MB, 则应 FAIL 而非 PARTIAL.

### F5. Variable identity 精度问题 (AETERM vs AEDECOD)
**影响题**: Q8 (c)
"AETERM 使用 MedDRA" 是业界常见 **misspeak** — 其实 MedDRA 绑 AEDECOD, AETERM 是 verbatim. 这在 smoke test 里作 correct 判据会误导用户. 建议 smoke v4 加一题专门区分 --TERM / --DECOD / --BODSYS / --LLT 的 MedDRA 绑定位置 (也是一种 AHP for variable-identity accuracy).

### F6. Non-SDTMIG-v3.4 concepts 渗入 (NS, Dataset-JSON)
Q11 (Dataset-JSON) 和 Q13 (NS Domain) 都是 post-v3.4 / 非 v3.4 正本的 supplemental concepts. 若题库定位"纯 SDTMIG v3.4 generalization probe", 这些 supplemental concepts 应**清楚标签分类** (如"Extension topic, not in SDTMIG v3.4 core"), 防止 NotebookLM/ChatGPT 等 in-KB-only 平台被错 FAIL.

### F7. RELSPEC 变量数描述偏差
**影响题**: Q3 (minor) + handoff matrix (minor)
Handoff 校验 matrix 写 "RELSPEC 三件套 (RELSPEC/PARENT/LEVEL)", 实际 RELSPEC dataset 有 **6 变量** (STUDYID / USUBJID / REFID / SPEC / PARENT / LEVEL); "三件套" 说法不准, 核心 join key 是 **REFID / PARENT / LEVEL** (后两者为 Exp/Req). 不是 "SPEC/PARENT/LEVEL".

---

## 建议 smoke v4 设计补充 (基于 6 维度审计结果)

### 已由 handoff 规划 (确认方向正确)
- **AHP1 variable hallucination (LBCLINSIG)**: OK, 合理 trap. 但注意 LBCLSIG (真实变量) vs LBCLINSIG (不存在) 仅 1 字符差, 题干需精确拼写.
- **AHP2 cross-domain false premise (Trial-Level SAE Aggregate)**: OK, SDTMIG 确实无此表, 业界常有此误解 → 好 trap.
- **AHP3 deprecated concept (PF → GF)**: OK, PF 在 v3.4 已合并入 GF, KB grep 确认 PF 无独立 spec.

### 本审计新增建议 (smoke v4 可考虑加)
1. **AHP4 Variable identity** (--TERM vs --DECOD, 跨 AE/CM/MH/CE): 测纠错"AETERM 用 MedDRA"这类 misspeak.
2. **AHP5 CT Extensibility attribute**: 给 5 codelist, 判 Extensible Yes/No, 识破混淆.
3. **AHP6 Non-core SDTMIG extensions** (Dataset-JSON / NS / RWD): 问"这个概念在 SDTMIG v3.4 正本存在吗?", 测能否识别 supplemental guide vs core IG 的 scope 分界.

### Smoke v4 PASS/FAIL 判据通用原则建议
- **Premise hallucination caught** (答题者纠正错前提): 应 **PASS+** 或 额外 0.25 分 bonus.
- **Premise hallucination accepted + answered downstream**: 应 **FAIL** (非 PARTIAL).
- **Partial premise correction**: 可 PARTIAL (0.5).

---

## 附录 A: WebFetch 源 (fact-check 用到)

| # | URL | 用途 | 查询日期 |
|---|---|---|---|
| A1 | https://www.cdisc.org/kb/articles/where-does-my-lab-data-go-sdtmig-v3-4 | Q4 IS vs MB scope (WebFetch 只返回 decision tree 提及, 未明引 anti-measles IgG) | 2026-04-22 |
| A2 | https://www.cdisc.org/kb/articles/domain-scope-update-sdtmig-v3-4-development-history-and-difficulties-standardizing | Q4 anti-microbial antibody consolidation to IS 证据 (WebFetch 成功获取摘要) | 2026-04-22 |
| A3 | https://standards.pinnacle21.certara.net/validation-rules/sdtm | Q9 Pinnacle 21 rule categories (WebFetch 仅返回导航页无内容) | 2026-04-22 |

## 附录 B: KB 内部锚点 (已核对)

| # | 文件 | 行号 | 核对内容 |
|---|---|---|---|
| B1 | `knowledge_base/domains/GF/spec.md` | L104-299 | Q1 GF 变量集 (GFTESTCD C181178 / GFGENSR / GFPVRID / GFGENREF / GFINHERT C181177) |
| B2 | `knowledge_base/domains/CP/spec.md` | L86-193 | Q2 CP 变量集 (CPTESTCD C181173 / CPSBMRKS / CPCELSTA C181172 / CPCSMRKS / CPMETHOD C85492) |
| B3 | `knowledge_base/domains/BE/spec.md` | L77-148 | Q3 BETERM / BECAT Example "COLLECTION, PREPARATION, TRANSPORT" |
| B4 | `knowledge_base/domains/BS/spec.md` | L77-129 | Q3 BSTESTCD C124300 Example "VOLUME, RIN" |
| B5 | `knowledge_base/domains/RELSPEC/spec.md` | L1-76 | Q3 RELSPEC 6 变量 (STUDYID/USUBJID/REFID/SPEC/PARENT/LEVEL) |
| B6 | `knowledge_base/domains/IS/assumptions.md` | L1-28 (assumption 2) | Q4 anti-microbial antibody → IS 显式规则 |
| B7 | `knowledge_base/domains/MB/assumptions.md` | L1-20 | Q4 MB scope (targeted organism identification) |
| B8 | `knowledge_base/domains/TS/spec.md` | **L65-67** (TSVAL assumption 8) | Q10 **TSVAL1-TSVALn 替代 SUPPTS, SUPPTS 不存在** (baseline self-test 证据) |
| B9 | `knowledge_base/chapters/ch08_relationships.md` | §8.4 L177 | Q10 SUPPQUAL scope 限于 Int/Events/Findings + DM + SV (TS 不在) |
| B10 | `knowledge_base/chapters/ch04_general_assumptions.md` | §4.5.3.2 L1296 | Q10 TS.TSVAL convention table (TS 走自身 TSVAL1-n 非 SUPP--) |
| B11 | `knowledge_base/terminology/core/general_part4.md` | L159-239 (C66734) | Q13 NS 不在 SDTM Domain Abbreviation codelist (NS not listed) |
| B12 | `knowledge_base/terminology/core/general_part4.md` | L63-72 (C78736) | Q8 LBNRIND Extensible=**Yes** (与 v3.2 PASS b 冲突) |
| B13 | `knowledge_base/domains/AE/spec.md` | L77-85 (AETERM) | Q8 AETERM Controlled Terms 列空, 非 MedDRA |
| B14 | `knowledge_base/domains/AE/spec.md` | L113-120 (AEDECOD) | Q8 AEDECOD Controlled Terms=MedDRA |
| B15 | `knowledge_base/domains/DM/spec.md` | L212-255 (ARMCD/ARMNRS) | Q13 ARMCD null + ARMNRS="NOT ASSIGNED" 正确机制 |
| B16 | `knowledge_base/terminology/core/disposition.md` | L15-57 (C66727) | Q14 C66727 "Completion/Reason for Non-Completion" 含 DEATH (C28554) |
| B17 | `knowledge_base/domains/SUPPQUAL/spec.md` | L1-111 | Q10 QORIG Req / QEVAL Exp (C78735) / RDOMAIN C66734 |
| B18 | `knowledge_base/chapters/ch04_general_assumptions.md` | §4.2.6 L327-330 | Q14 AE/MH/CE 跨域 --CAT 允许, 但 timing 区分 (v3.2 "三域互斥" 强化了) |
| B19 | `knowledge_base/terminology/core/ae.md` | L43-51 (C66769) | Q8 AESEV Non-Extensible {MILD, MODERATE, SEVERE} 确认 |
| B20 | `knowledge_base/terminology/core/gf.md` | L19-34 (C181178) | Q1 GFTESTCD 10 submission values (SNV/SHRTVAR/TMB 等) |

## 附录 C: 审计过程 trace (Rule D compliance)

- **Subagent_type**: `oh-my-claudecode:document-specialist` (第 11 种, 不重复前 10 种)
- **Model**: opus (claude-opus-4-7[1m])
- **Mode**: background, read-only
- **Tools used**: Read (×20+), Bash (grep/ls only), WebFetch (×2 成功 + 1 低质量), ToolSearch (×3)
- **Files modified**: **仅本文件新建** (ai_platforms/smoke_v3_audit_notes.md); 任何 KB / smoke_v3_questions_draft / _progress.json 文件**未动**.
- **Self-test baseline**: Q10 (b) 在独立读 `TS/spec.md` L65-67 + `ch08` §8.4 时识别前提错; 不依赖 handoff 提示 (虽然 handoff 事后 cross-reference 确认方向一致).

---

**报告结束**. 建议 main session:
1. 优先修 Q10 (HIGH) + Q13 (HIGH) + Q8 (MEDIUM) 进 v3.3 (若仍走 Step 2-3 patch 路径) 或 直接 v4.0 (走 handoff Step 4 AHP+v4 路径).
2. Q4 / Q14 MINOR 可 bundle 进 v4.0.
3. Smoke v4 AHP 设计采纳 handoff 3 类 + 本报告 3 类补充 (AHP4/5/6).
4. KB 锚点 ch05 → ch04 §4.3 + terminology/core/ 全局替换.
