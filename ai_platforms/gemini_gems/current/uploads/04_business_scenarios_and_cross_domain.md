<!-- source: ai_platforms/gemini_gems/current/uploads/04_business_scenarios_and_cross_domain.md -->
# 04 Business Scenarios & Cross-Domain Reference

> 本文件由 Node 4 C 方案重整产出, 为 SDTM 业务问答场景专供.
> 不 inline NCI Codelist Term 具体值; 所有 Term 查询请走 NCI EVS Browser.
> Generated: 2026-04-21
> Tokens target: ~50,000 (cl100k_base 估算)
> 上游事实依据: `knowledge_base/domains/<D>/spec.md` + `knowledge_base/domains/<D>/assumptions.md` + `knowledge_base/chapters/ch04_general_assumptions.md`
> 本文件所有变量名 / Core 属性 / Role 都已对照 KB spec 核验; 示例数据 (浓度值 / 日期 / arm 名) 为构造, 变量语义真实.

---

## §0. 使用本文件的基本规则 (必读)

SDTM 业务问答 ≠ 字典查询. 本 Gem 的 04 弹药包聚焦**临床业务→SDTM 映射**的真实场景, 典型提问源包括:

- CDM (Clinical Data Manager): "EDC 拿到这条数据, 映射到哪个 SDTM 域? 填哪些变量?"
- SDTM Programmer: "我应该走 RELREC 还是 SUPP--? 需要拆几条记录?"
- 统计程师 / 医学监查员: "AESEV 和 AESER 都标成 SAE 了, 哪个才是对的?"
- 标准审查员: "LBSTRESN 填 0 还是 NULL? 部分精度 ISO 8601 允许到日吗?"

回答这些问题, 依赖**规则 + 变量 + 实例**三位一体, 本文件把业务场景展开, 指向 spec/assumptions/chapters 源段作为溯源依据.

### 三条硬约束

1. **AE 域 Core 属性边界锚点** (CO-1 防邻变量污染): AE 多数标识/主题变量 **Core=Req**, 但众多 Qualifier 变量 Core=Exp 或 Perm. 不得由"多数 Req"模式推断. 逐变量对照 02 spec (详见 §2.1).
2. **NCI Code 零臆造** (CO-2): 本 Gem 不 inline codelist Term 具体值 (e.g., C66742 codelist 的 "Y/N" 以外的 Synonym). 只保留 CT Code 到 codelist 英文名的映射 (§3), 所有 Term 值/Synonym 查询 → NCI EVS Browser 外链. 生成 Code 属臆造, 禁止.
3. **citation 强制格式** (CO-3): 每次回答**必须**带源路径段, 格式统一:
   > **源路径**: `knowledge_base/domains/AE/spec.md` §AESER
   > **章节**: Section 4.1.5 (若引 chapters)

   若完全无 KB 支撑, 明说 "本 Gem 无本地 KB 可溯源, 建议查 <外部源>".

---

## §1. 临床业务场景 → SDTM 映射 (15 条目, 覆盖 smoke v2 10 题)

本节条目设计原则: **1 业务场景 = 1 临床动作 → SDTM 域 + 核心变量 + 拆记录规则 + pitfall**.

### §1.1 合并用药同服多药, CM 拆记录规则 (对应 smoke Q1)

**业务场景**: 受试者同一天开始服用两种不同成分的合并药物 (如氯沙坦 50 mg/日 + 氨氯地平 5 mg/日, 指征同为高血压, 计划持续整个试验期).

**SDTM 域**: CM (Concomitant/Prior Medications). Class: Interventions. Structure: 1 record per recorded intervention occurrence or constant-dosing interval per subject.

**拆记录规则**: **拆两条独立 CM 记录**, 每药一条. 不合并. 依据 CM assumptions §2.a: "CMTRT only includes the medication/therapy name and does not include dosage, formulation, or other qualifying information." 两个独立的 CMTRT 值 → 两条记录.

**核心变量 (对照 knowledge_base/domains/CM/spec.md)**:

| 变量 | Label | Role | Core | 本场景取值 (第 1 条) | 第 2 条 |
|------|-------|------|:----:|---------------------|--------|
| STUDYID | Study Identifier | Identifier | **Req** | "ABC-001" | "ABC-001" |
| DOMAIN | Domain Abbreviation | Identifier | **Req** | "CM" | "CM" |
| USUBJID | Unique Subject Identifier | Identifier | **Req** | "ABC-001-0001" | "ABC-001-0001" |
| CMSEQ | Sequence Number | Identifier | **Req** | 1 | 2 |
| CMTRT | Reported Name of Drug | Topic | **Req** | "LOSARTAN" | "AMLODIPINE" |
| CMDECOD | Standardized Medication Name | Synonym Qualifier | Perm | "LOSARTAN POTASSIUM" | "AMLODIPINE BESYLATE" |
| CMCAT | Category for Medication | Grouping Qualifier | Perm | "CONCOMITANT" | "CONCOMITANT" |
| CMINDC | Indication | Record Qualifier | Perm | "HYPERTENSION" | "HYPERTENSION" |
| CMDOSE | Dose per Administration | Record Qualifier | Perm | 50 | 5 |
| CMDOSU | Dose Units | Variable Qualifier | Perm | "mg" | "mg" |
| CMDOSFRQ | Dosing Frequency | Variable Qualifier | Perm | "QD" | "QD" |
| CMROUTE | Route of Administration | Variable Qualifier | Perm | "ORAL" | "ORAL" |
| CMSTDTC | Start Date/Time | Timing | Perm | "2024-06-15" | "2024-06-15" |
| CMENRF | End Relative to Reference Period | Timing | Perm | "ONGOING" | "ONGOING" |

**Core 属性说明**: CM 域仅 5 个 Req (STUDYID / DOMAIN / USUBJID / CMSEQ / CMTRT). 其他**全部 Perm** (包括 CMINDC / CMDOSE / CMSTDTC). 不要把 CMCAT/CMSCAT/CMDOSE 误列为 Req.

**pitfall**:
- (1) 合并一条 `CMTRT="LOSARTAN+AMLODIPINE"` — **错**. 违反 CM assumptions §2.a (CMTRT 仅单药名).
- (2) `CMTRT="LOSARTAN 50MG TABLET"` — **错**. CM assumptions §2.a 明确: CMTRT 仅 "LOSARTAN", dose/form 走 CMDOSE/CMDOSFRM.
- (3) 指征不同时可拆开, 但本场景两药同指 HYPERTENSION, 两条 CMINDC 一致即可.

**源路径**:
- `knowledge_base/domains/CM/spec.md` (CMTRT §, CMSEQ §, CMINDC §, CMDOSE §)
- `knowledge_base/domains/CM/assumptions.md` §2.a

---

### §1.2 AE 升 SAE, 住院相关 Serious 子变量 (对应 smoke Q2)

**业务场景**: 受试者服药后出现严重皮疹, 因此住院 3 天治疗, Investigator 判为药物相关 SAE (但非危及生命、非致死、非致残、非先天异常).

**SDTM 域**: AE (Adverse Events). Class: Events. Structure: 1 record per adverse event per subject.

**核心变量取值 (对照 knowledge_base/domains/AE/spec.md + assumptions.md §7.a)**:

| 变量 | Label | Core | 本场景值 | 含义 |
|------|-------|:----:|:-------:|------|
| AETERM | Reported Term | **Req** | "Severe rash" | Verbatim 术语 |
| AEDECOD | Dictionary-Derived Term | **Req** | "Rash" | MedDRA PT |
| AEBODSYS | Body System | Perm | "Skin and subcutaneous tissue disorders" | MedDRA SOC |
| AESEV | Severity/Intensity | **Perm** | "SEVERE" | 严重性档 (MILD/MODERATE/SEVERE) |
| **AESER** | **Serious Event** | **Exp** | **"Y"** | 是否 Serious (导致住院即 Y) |
| AESHOSP | Requires or Prolongs Hospitalization | **Perm** | "Y" | 住院/延长住院 |
| AESLIFE | Is Life Threatening | **Perm** | "N" | 非危及生命 |
| AESDTH | Results in Death | **Perm** | "N" | 非致死 |
| AESDISAB | Persist or Signif Disability/Incapacity | **Perm** | "N" | 非致残 |
| AESCONG | Congenital Anomaly or Birth Defect | **Perm** | "N" | 非先天异常 |
| AESMIE | Other Medically Important SAE | **Perm** | "N" | 住院已覆盖本事件 Serious 条件, 故 N |
| AEREL | Causality | **Exp** | "RELATED" | 与研究药相关性 |
| AEACN | Action Taken with Study Treatment | **Exp** | "DRUG WITHDRAWN" | ICH E2B 值 |

**!! 边界锚点 (CO-1)**: AE 域 Core 属性**不规则**, 不得按"AE 多数 Req"推断:
- **Req** (只 6 个): STUDYID / DOMAIN / USUBJID / AESEQ / AETERM / AEDECOD
- **Exp** (约 10 个): AESER, AEREL, AEACN, AELLT, AELLTCD, AEPTCD, AEHLT, AEHLTCD, AEHLGT, AEHLGTCD
- **Perm** (剩余所有 Qualifier, **包含** AESEV / AESHOSP / AESLIFE / AESDTH / AESDISAB / AESCONG / AESMIE / AEOUT / AEACNOTH / AESCAN / AESOD / 所有 timing 变量)

**特别强调**: **AESEV (Severity) Core=Perm**, 非 Req. **AESER (Serious) Core=Exp**, 非 Req. 这两个维度变量都**不强制**, 但通常填写. 查询具体 AE 变量 Core → 必查 `02_domains_spec_and_assumptions.md` 对应变量行, 不邻变量推断.

**pitfall**:
- (1) AESEV 和 AESER 混淆 — AESEV = 严重性档 (MILD/MODERATE/SEVERE), AESER = 是否 Serious (Y/N). **两个不同维度**. SAE 但可能 AESEV=MILD (住院但症状轻).
- (2) AESER=Y 时需**至少一个 Serious 子变量=Y** (assumptions §7.a). 本例 AESHOSP=Y.
- (3) Grade 5 = 死亡 → AETOXGR=5 且 AESDTH=Y (AESEV 可填 SEVERE 但 Grade 5 不独立等于 AESEV).
- (4) AE assumptions §7.c 指出: 当 CRF 收 "Other Medically Important SAE" 描述时, 描述文本走 **SUPPAE QNAM=AESOSP**, 不直接塞进 AE 域.

**源路径**:
- `knowledge_base/domains/AE/spec.md` (AESER §, AESEV §, AESHOSP § 等逐变量)
- `knowledge_base/domains/AE/assumptions.md` §7.a-d (Serious 类别 CRF 形态 + CTCAE + SUPPAE)

---

### §1.3 实验室检验 HbA1c 超标, LB 域记录方式 (对应 smoke Q3)

**业务场景**: 受试者空腹 HbA1c = 6.8%, 实验室参考范围 4.0-6.0%, 标注 "高".

**SDTM 域**: LB (Laboratory Test Results). Class: Findings. Structure: 1 record per lab test per time point per visit per subject.

**核心变量取值 (对照 knowledge_base/domains/LB/spec.md)**:

| 变量 | Label | Core | 本场景值 | 说明 |
|------|-------|:----:|:-------:|------|
| LBTESTCD | Lab Test or Examination Short Name | **Req** | "HBA1C" | ≤8 字符, 查 C65047 codelist |
| LBTEST | Lab Test or Examination Name | **Req** | "Hemoglobin A1C" | 查 C67154 codelist |
| LBCAT | Category for Lab Test | Exp | "CHEMISTRY" | 分类 |
| LBORRES | Result in Original Units | Exp | "6.8" | **字符**, 原始结果 |
| LBORRESU | Original Units | Exp | "%" | 查 C71620 codelist |
| LBORNRLO | Reference Range Lower Limit (Orig) | Exp | "4.0" | 原单位下限 |
| LBORNRHI | Reference Range Upper Limit (Orig) | Exp | "6.0" | 原单位上限 |
| LBSTRESC | Character Result/Finding in Std Format | Exp | "6.8" | **字符**, 标准化结果 |
| LBSTRESN | Numeric Result/Finding in Standard Units | Exp | 6.8 | **数值**, 同值数值化 |
| LBSTRESU | Standard Units | Exp | "%" | 标准化单位 |
| LBSTNRLO | Reference Range Lower Limit (Std) | Exp | 4.0 | 数值下限 |
| LBSTNRHI | Reference Range Upper Limit (Std) | Exp | 6.0 | 数值上限 |
| LBNRIND | Reference Range Indicator | Exp | **"H"** | 三档: "L"/"N"/"H" (或空) |

**!! LBNRIND 三档取值** (对照 `knowledge_base/terminology/core/general_part4.md` codelist C78736 Reference Range Indicator):
- `"L"` = 低于参考范围下限
- `"N"` = 在参考范围内 (Normal)
- `"H"` = 高于参考范围上限
- 其他合法值含 `"ABNORMAL"` (仅当无 L/N/H 分类时)

**本场景**: LBNRIND = **"H"** (6.8 > 6.0).

**pitfall**:
- (1) LBNRIND 写 "HIGH"/"LOW" — **错**. 标准 C78736 codelist 三字母档为 "H"/"L"/"N".
- (2) LBORRES 和 LBSTRESN 类型混淆: **LBORRES 是 Char** (允许"<LLOQ"/ "6.8"/ "POSITIVE" 等), **LBSTRESN 必须 Num**.
- (3) 忘记 LBSTRESC vs LBSTRESN 区分: LBSTRESC = 标准化字符 (含所有结果), LBSTRESN = 若结果是数值, 同值存 Num. 字符非数值 (如"POSITIVE") → LBSTRESN 为空.
- (4) 单位未标准化 (LBORRESU ≠ LBSTRESU) 时, LBSTRESN 是换算后的数值, 不是 LBORRES 的简单复制.
- (5) LBNRIND 不是"clinically significant" 指示器, 仅反映是否超参考范围 (spec 原文).

**源路径**: `knowledge_base/domains/LB/spec.md` (LBTESTCD §, LBNRIND § 等)

---

### §1.4 AESEV 三档 vs CTCAE Grade 映射 (对应 smoke Q4)

**业务场景**: 肿瘤试验 EDC 只收 Investigator 填的 CTCAE Grade (1-5), 填 AE 时 AESEV 怎么填?

**SDTM 规则 (对照 knowledge_base/domains/AE/assumptions.md §7.d + spec.md AESEV §)**:

**AESEV 三档取值** (C66769 Severity/Intensity Scale for Adverse Events codelist, 注: 具体 Term 去 NCI EVS 查):
- `"MILD"`
- `"MODERATE"`
- `"SEVERE"`

**CTCAE Grade 对应** (约定俗成映射, 非 SDTMIG 强制):
| CTCAE Grade | AESEV | 说明 |
|:-----------:|:------:|------|
| Grade 1 | MILD | 轻微 (asymptomatic/mild) |
| Grade 2 | MODERATE | 中度 |
| Grade 3 | SEVERE | 严重 |
| Grade 4 | SEVERE | 危及生命 (AESEV=SEVERE 且 **AESLIFE=Y**) |
| Grade 5 | SEVERE | **死亡** (AESEV=SEVERE 且 **AESDTH=Y**; 本质走 AESDTH) |

**重要**: 若试验用 CTCAE, AE assumptions §7.d 建议用 **AETOXGR (Toxicity Grade) 代替 AESEV**, 保留原始 Grade 1-5 信息. 一般**两者不同时填** (AESEV xor AETOXGR), 除非有特殊理由.

**AESEV ≠ AESER (维度彻底不同)**:
- AESEV = 严重性档 (强度, MILD/MODERATE/SEVERE)
- AESER = 是否 Serious (Y/N, 按 ICH E2A/E2B 6 条标准)
- 一个 MILD 事件可以是 Serious (如导致住院的轻度事件); 一个 SEVERE 事件不一定 Serious.

**pitfall**:
- (1) AESEV 填 Grade 1-5 数字 — **错**. AESEV 必填文本 "MILD"/"MODERATE"/"SEVERE", 若要保留 Grade 走 AETOXGR.
- (2) Grade 5 当 AESEV="GRADE5" — **错**. Grade 5 = 死亡, 走 AESDTH="Y", AESEV 填 "SEVERE".
- (3) 混淆 AESEV 和 AESER: 同一 AE 都 SAE 了但 AESEV=MILD 是合法的 (如仅住院观察未治).

**源路径**:
- `knowledge_base/domains/AE/spec.md` §AESEV (Core=Perm), §AESER (Core=Exp)
- `knowledge_base/domains/AE/assumptions.md` §7.d (CTCAE ↔ AETOXGR)

---

### §1.5 PK 采样 LLOQ 以下值的记录 (对应 smoke Q5)

**业务场景**: PK 研究, 某采样点浓度低于实验室 LLOQ (e.g., LLOQ=0.5 ng/mL, 实测不可量化).

**SDTM 域**: PC (Pharmacokinetics Concentrations). Class: Findings.

**核心变量取值 (对照 knowledge_base/domains/PC/spec.md)**:

| 变量 | Core | 本场景值 | 说明 |
|------|:----:|:-------:|------|
| PCTESTCD | **Req** | "DRUG_A" | 分析物代码 ≤8 字符 |
| PCTEST | **Req** | "Drug A Concentration" | 分析物名 |
| PCORRES | Exp | **"<LLOQ"** | Char, 带"<"符号 |
| PCORRESU | Exp | "ng/mL" | 原单位 |
| PCSTRESC | Exp | **"<LLOQ"** | Char 标准化, 保留不确定性 |
| PCSTRESN | Exp | **NULL (空)** | **不能填 0**, 非数值 |
| PCSTRESU | Exp | "ng/mL" | 标准单位 |
| PCLLOQ | Exp | 0.5 | 数值, LLOQ 本身 |

**为什么 PCSTRESN 不能填 0**:
- (1) 字符语义: `"<LLOQ"` ≠ 0, 真值可能在 (0, LLOQ) 区间任意位置.
- (2) 统计后果: PK 计算 AUC / Cmax 时, 若把 `<LLOQ` 视为 0, 会系统性低估 AUC (应按约定替换为 LLOQ/2 或 NQ, 在 ADaM 层处理, **不在 SDTM**).
- (3) 合规性: PCSTRESN 是 Num, 若填 0 数值, 下游无法区分"真 0" vs "unquantifiable".

**SDTM 原则**: **PCORRES 保留原始不确定性** (字符 "<LLOQ"), PCSTRESN 留空让下游 ADaM/统计层按 SAP 规则替换.

**pitfall**:
- (1) PCSTRESN 填 0 → 下游 PK AUC 低估, **禁**.
- (2) PCORRES 写 "BLQ" 不提 `<LLOQ` 约定 — BLQ (Below Limit of Quantitation) 是等价含义但 SDTM 惯例用 `<LLOQ` 符号.
- (3) 忘记填 PCLLOQ — PCLLOQ 是必要 context, 让审查员知道量化阈.

**源路径**:
- `knowledge_base/domains/PC/spec.md` (PCORRES §, PCSTRESN §, PCLLOQ §)
- `knowledge_base/domains/PC/assumptions.md` (§3: Controlled Terminology Rules for Pharmacokinetics)

---

### §1.6 DM.ARMCD vs DM.ARM 关系 + 中途换组 (对应 smoke Q6)

**业务场景**: 受试者因盲态问题在 Week 4 从 Arm A 换到 Arm B.

**SDTM 域**: DM (Demographics) + SE (Subject Elements) + TA (Trial Arms).

**变量定义 (对照 knowledge_base/domains/DM/spec.md)**:

| 变量 | Label | Core | 最大长度 | 含义 |
|------|-------|:----:|:--------:|------|
| ARMCD | Planned Arm Code | Exp | 20 chars | **短代号**, 如 "A"/"PBO"/"DRUG50" |
| ARM | Description of Planned Arm | Exp | — | **Full description**, 如 "Drug 50 mg QD" |
| ACTARMCD | Actual Arm Code | Exp | 20 chars | 实际经过 Arm 的代号 |
| ACTARM | Description of Actual Arm | Exp | — | 实际经过 Arm 的描述 |
| ARMNRS | Arm Null Reason | Exp | — | 若 ARM/ACTARM 为空的原因代码 |
| ACTARMUD | Desc of Unplanned Actual Arm | Exp | — | 若实际 arm 非任何 planned arm |

**关键关系**:
- ARMCD 最大 20 字符 (注意**不是 8**, 为支持 crossover 设计多 Element 拼接).
- ARMCD / ARM **必须匹配 TA (Trial Arms) 的值** (除非多阶段 arm assignment 试验).
- DM.ARMCD 与 TA.ARMCD 是键约束关系 — DM 中每个受试者的 ARMCD **必须出现在 TA 的 ARMCD 列表里**.

**中途换组的记录**:

| 域 | 职责 | 本场景 |
|----|------|--------|
| **DM** | 记录最终/概括分组: ARM/ARMCD = planned (入组时); ACTARM/ACTARMCD = actual (最终实际经过) | ARMCD="A", ACTARMCD="B" (或者 ACTARMCD 填特殊值, ACTARMUD 填自由文本) |
| **SE** (Subject Elements) | 记录**实际经过的 element 序列**, 1 record per actual Element per Subject | 多条 SE 记录, 按时序排列, 展示受试者 Week 0-4 在 Arm A Element, Week 4-End 在 Arm B Element |
| **TA** (Trial Arms) | **设计层** trial arms, 非实际; 每 Arm 下列 Element 序列 | 不因受试者换组改动, TA 是静态试验设计 |

**pitfall**:
- (1) ARMCD 和 ARM 哪个是代号说反 — ARMCD 是短代号 (Code), ARM 是描述 (Full description).
- (2) 不识别 ACTARM/ACTARMCD 概念, 只改 ARM/ARMCD 记换组 — **错**. ARM/ARMCD 是 planned, 一般入组后不变.
- (3) 把换组信息写到 TA — **错**. TA 是设计, 不是实际.
- (4) 忘记 SE 域专门记录实际经过 Element — SE 是换组/脱落等实际情况的权威源.

**源路径**:
- `knowledge_base/domains/DM/spec.md` (ARMCD §, ARM §, ACTARMCD §, ACTARM §)
- `knowledge_base/domains/SE/spec.md` (SE 定义 + assumptions)
- `knowledge_base/domains/TA/spec.md` (TA 设计层定义)

---

### §1.7 病史"高血压 10 年, 目前仍服药"映射 (对应 smoke Q7)

**业务场景**: EDC 字段 "病史: 高血压 10 年, 目前仍在服用氨氯地平 5 mg/日".

**拆域规则**: **两域都要**, MH 和 CM 各自职责不同:

#### MH (Medical History) 一条

| 变量 | Core | 取值 | 说明 |
|------|:----:|:----:|------|
| STUDYID | **Req** | "ABC-001" | |
| DOMAIN | **Req** | "MH" | |
| USUBJID | **Req** | "ABC-001-0001" | |
| MHSEQ | **Req** | 1 | |
| MHTERM | **Req** | "Hypertension" | **诊断**, 不含用药 |
| MHDECOD | Perm | "Hypertension" | MedDRA PT |
| MHCAT | Perm | "CARDIOVASCULAR" | 可选分类 |
| MHSTDTC | Perm | "2014-06-15" | 病史起始 (约 10 年前) |
| MHENRF | Perm | "ONGOING" | 持续至研究 ref period 结束 |

#### CM (Concomitant Medication) 一条

| 变量 | Core | 取值 | 说明 |
|------|:----:|:----:|------|
| STUDYID | **Req** | "ABC-001" | |
| DOMAIN | **Req** | "CM" | |
| USUBJID | **Req** | "ABC-001-0001" | |
| CMSEQ | **Req** | 1 | |
| CMTRT | **Req** | "AMLODIPINE" | **用药**, 不含诊断 |
| CMDOSE | Perm | 5 | |
| CMDOSU | Perm | "mg" | |
| CMDOSFRQ | Perm | "QD" | |
| **CMINDC** | Perm | **"HYPERTENSION"** | **指征 → 和 MH.MHTERM 语义呼应** |
| CMSTDTC | Perm | "2014-06-15" | 首次用药 (约 10 年前) |
| CMENRF | Perm | "ONGOING" | 仍在服 |

**MH 和 CM 分工** (业务核心):
- **MH** = **诊断/病史事实** (Events class). 主题是"发生过/存在某疾病事件".
- **CM** = **实际用药行为** (Interventions class). 主题是"服用某药物".
- 同一临床事件 (高血压) 在两域有**不同视角**: MH 说"患者有此病", CM 说"患者为此病服此药".

**ONGOING 语义 (MHENRF / CMENRF)**:
- `"ONGOING"` 来自 C66728 Relation to Reference Period codelist. 语义: 事件/用药**在研究 reference period 结束时仍在持续** (对应 DM.RFENDTC 或 sponsor 定义的 ref period end).
- `"BEFORE"`/`"DURING"`/`"AFTER"`/`"ONGOING"` 等枚举值覆盖相对时序.

**pitfall**:
- (1) 只进一个域 — 遗漏一半信息. MH 无法描述用药, CM 无法描述诊断.
- (2) MH 和 CM 混淆: 把 "氨氯地平" 填 MHTERM, 或把 "高血压" 填 CMTRT — **错**. MHTERM 必须是诊断术语 (MedDRA PT), CMTRT 必须是药物名.
- (3) 不填 CMINDC — 丢失"为何服此药"的业务关联, CMINDC 可填"HYPERTENSION"回指 MH.MHTERM.
- (4) 忽略 ONGOING 语义: 若病史已结束, MHENDTC 应填结束日, MHENRF 不必 ONGOING.

**源路径**:
- `knowledge_base/domains/MH/spec.md` (MHTERM §, MHENRF §)
- `knowledge_base/domains/CM/spec.md` (CMTRT §, CMINDC §, CMENRF §)
- `knowledge_base/chapters/ch04_general_assumptions.md` §4.4.7 (Use of Relative Timing Variables)

---

### §1.8 时间精度: 服药后 6 小时发 AE (对应 smoke Q8)

**业务场景**: 受试者早 8:00 服药, 下午 2:00 发头痛 (AE). EDC 记到时:分.

**ISO 8601 格式规则 (对照 knowledge_base/chapters/ch04_general_assumptions.md §4.4)**:

SDTM 所有日期时间变量用 **ISO 8601 字符串**, 允许**部分精度**:

| 精度 | 格式 | 示例 |
|------|------|------|
| 年 | `YYYY` | `"2024"` |
| 年-月 | `YYYY-MM` | `"2024-06"` |
| 年-月-日 | `YYYY-MM-DD` | `"2024-06-15"` |
| 到小时 | `YYYY-MM-DDThh` | `"2024-06-15T14"` |
| 到分 | `YYYY-MM-DDThh:mm` | `"2024-06-15T14:00"` |
| 到秒 | `YYYY-MM-DDThh:mm:ss` | `"2024-06-15T14:00:30"` |
| 带时区 | `YYYY-MM-DDThh:mm+HH:MM` | `"2024-06-15T14:00+08:00"` |
| 区间 | `YYYY-MM-DD/YYYY-MM-DD` | `"2024-06-15/2024-06-20"` |
| 持续时长 | `PnYnMnDTnHnMnS` | `"P3D"` (3 天), `"PT6H"` (6 小时) |

**本场景**: AESTDTC = `"2024-06-15T14:00"` (到分). 若 EDC 只记到日: AESTDTC = `"2024-06-15"` (合法, 精度降级保留).

**Study Day 计算规则 (对照 ch04 §4.4.3 Study Day)**:

```
IF AESTDTC date >= RFSTDTC date:
    AESTDY = (AESTDTC date - RFSTDTC date) + 1    # Day 1 起始
ELSE:
    AESTDY = (AESTDTC date - RFSTDTC date)         # 负值表示研究前
```

**关键**: **Day 1 是 RFSTDTC 当日**, 非 Day 0. 负值 (pre-treatment) 没有 Day 0, 直接从 -1 开始.

**--DY 计算示例**:
| RFSTDTC | AESTDTC | AESTDY |
|---------|---------|-------:|
| 2024-06-15 | 2024-06-15 | **1** |
| 2024-06-15 | 2024-06-16 | 2 |
| 2024-06-15 | 2024-06-14 | **-1** |
| 2024-06-15 | 2024-06-10 | -5 |

**pitfall**:
- (1) AESTDTC 格式写 `"06/15/2024"` / `"20240615"` / `"2024-6-15"` — **全错**. ISO 8601 要求 `YYYY-MM-DD` 零填充.
- (2) 不知 ISO 8601 允许部分精度, 强填占位符如 `"2024-06-15T00:00"` — **错**, 当 EDC 只有日精度时应直接用 `"2024-06-15"`.
- (3) Day 0 vs Day 1 混用: **SDTM 规定 RFSTDTC 当日 = Day 1**, 不是 Day 0. Day 0 不存在.
- (4) 跨时区: 多中心跨时区研究, AESTDTC 应带时区 offset, 否则 Study Day 计算可能错 1 天.

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §4.4.3 (Study Day), §4.4.4 (ISO 8601 format)

---

### §1.9 SUPPAE 边界: QNAM/QLABEL/QVAL (对应 smoke Q9)

**业务场景**: EDC 收了某个"呼吸模式"字段用于某类 AE, 但 AE 域无标准变量可承载.

**SDTM 规则 (对照 chapters/ch04_general_assumptions.md §8 Representing Relationships and Data)**:

**SUPPAE 定位**: "Supplemental Qualifiers for AE", Relationship class dataset. Structure: 1 record per supplemental qualifier per parent AE record.

**何时走 SUPPAE**:
- 标准 AE 域**无对应变量**容纳 → 走 SUPPAE
- 标准 AE 域**有对应变量**但值有限制, 又需保留原始值 → 可走 SUPPAE
- AE assumptions §7.c 明示: Other Medically Important SAE 的**描述文本** (不是 Y/N 判定) → SUPPAE QNAM="AESOSP"

**何时不走 SUPPAE**:
- 标准 AE 域已有变量 (如 AESEV / AESER / AEACN) → **不**重复走 SUPPAE
- 跨域关系 (AE 和 CM 的因果) → 走 RELREC, **不**走 SUPPAE (见 §1.10)

**SUPPAE 结构变量 (必填 6 字段)**:

| 变量 | 含义 | 示例 |
|------|------|------|
| STUDYID | Study ID | "ABC-001" |
| RDOMAIN | 父域代码 | "AE" |
| USUBJID | 受试者 | "ABC-001-0001" |
| IDVAR | 父域中用于 join 的字段名 | "AESEQ" |
| IDVARVAL | 父域对应记录的字段值 (字符) | "12" |
| QNAM | Qualifier name (≤8 字符) | **"AERESPPD"** |
| QLABEL | Qualifier 的 label (≤40 字符) | "AE Respiration Pattern" |
| QVAL | 实际值 (字符) | "Labored" |
| QORIG | 来源 (可选) | "CRF" |
| QEVAL | 评价者 (可选) | "INVESTIGATOR" |

**本例 QNAM/QLABEL/QVAL 示例**:
- QNAM = `"AERESPPD"` (AE Respiration Pattern Descriptor)
- QLABEL = `"AE Respiration Pattern"`
- QVAL = `"Labored"`

**QNAM 命名规则 (ch04 §8.4)**:
- ≤ 8 字符
- 开头通常不用父域前缀 (AE), 避免冲撞标准变量 (AE** 是 AE 域 reserved)
- 但实际约定有用 "AE" 前缀的 (如 "AESOSP"), 只要 ≤ 8 字符就合规

**pitfall**:
- (1) 把 AE 标准变量 (如 AESEV) 当 SUPPAE 示例 — **错位**. AESEV 已在 AE 域, 不走 SUPPAE.
- (2) QNAM 超 8 字符 — **错**. 标准变量命名规则, 同 --TESTCD.
- (3) 不解释 SUPPAE 的"非标存储"本质, 把它当"通用补充表" — 误解. SUPP-- 专门存**标准域没有的变量**.
- (4) IDVARVAL 没转字符: IDVARVAL 永远是 Char, 即使 IDVAR 是数值变量 (如 AESEQ=12 → IDVARVAL="12").

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §8.4 (Relating Non-Standard Variable Values)

---

### §1.10 RELREC vs SUPPAE 选择: 跨域关联 (对应 smoke Q10)

**业务场景**: 受试者某次 AE (头晕) 经 Investigator 判定与某合并用药 (复方降压药) 引起的血压下降有关.

**正确选择: RELREC**, 不是 SUPPAE/SUPPCM.

**对比 (对照 ch04 §8)**:

| 维度 | RELREC | SUPP-- |
|------|--------|--------|
| 功能 | **跨域/跨记录关系** | 单条记录的**非标补充变量** |
| 场景 | AE 和 CM 两条独立记录之间有**因果/关联** | AE 单条记录需要一个 AE 域没定义的字段 |
| Dataset | **relrec.xpt** | **suppae.xpt / suppcm.xpt** 等 |
| 典型字段 | RDOMAIN / IDVAR / IDVARVAL / RELID / RELTYPE | QNAM / QLABEL / QVAL + IDVAR/IDVARVAL |

**本场景 (头晕 AE 由降压药 CM 引起)**:

RELREC 记录 2 条 (一条指向 AE, 一条指向 CM, 两条用同 RELID 绑定):

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|:---:|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC-001 | AE | ABC-001-0001 | AESEQ | "5" | ONE | "R001" |
| 2 | ABC-001 | CM | ABC-001-0001 | CMSEQ | "3" | ONE | "R001" |

- 两条 RELREC 记录**同 RELID="R001"** 表示同一关系.
- `RELTYPE="ONE"` 表示 AE 一条 → CM 一条 (一对一关系); `"MANY"` 表示一对多.

**RELREC 用途 (ch04 §8)**:
- 跨域 (AE ↔ CM) 关联
- 同域跨记录关联 (AE #5 和 AE #12 是同一事件的不同阶段)
- 数据集级关联 (整个 FA 数据集和某 QS 关联)

**SUPP-- 用途** (对比):
- **只解一域内补充**, 不跨记录, 不跨域
- 典型: AE 需要"皮疹面积 cm²"这类非标数值 → SUPPAE

**pitfall**:
- (1) 选 SUPPAE 存 "和 CM 相关" → **错**. SUPPAE 不记录跨域关系.
- (2) 把 "AE 由 CM 引起" 填 AEACNOTH (自由文本) — 不算错但丢失结构化关系, 审查工具无法 join.
- (3) RELREC 的 IDVARVAL 忘转字符 — 永远 Char.
- (4) 同一 RELREC 关系的两条记录用**不同 RELID** — **错**. 同关系必须同 RELID.
- (5) 混淆 RELREC 和 Disease Milestone (ch04 §4.4.10 MIDS): Milestone 有专门 MIDS 变量, **优先用 MIDS 不用 RELREC**, 如 ch04 §4.4.10 明示.

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §8.1-8.3 (RELREC 类型 + 示例), §4.4.10 (MIDS vs RELREC)

---

### §1.11 Exposure (EX vs EC) 域选择

**业务场景**: 受试者按计划服药 vs 实际服药差异.

**SDTM 选择**:
- **EX (Exposure)**: **计划**协议规定的暴露 (按 dose 计划推导). 数据来源: Investigator 记录 / CRF 计划 dose.
- **EC (Exposure as Collected)**: **实际**从 EDC 采集的 dose. 数据来源: CRF 原始采集.

**何时用哪个**:
- 试验有明确 dose 协议且执行严格 → **主用 EX**
- EDC 采集的 dose 数据有调整 / 错漏 → **用 EC 保留原始**, EX 作 derived
- 多剂量研究 → 两域并存, EX 做 summary, EC 存每次实际服药

**核心变量相似度**: EX 和 EC 绝大多数变量同名 (EXDOSE vs ECDOSE, EXSTDTC vs ECSTDTC).

**源路径**: `knowledge_base/domains/EX/spec.md`, `knowledge_base/domains/EC/spec.md`

---

### §1.12 General Observation Class (Events / Findings / Interventions) 分类决策

**判定三步**:

1. **动作源**: 谁发起?
   - 受试者/疾病**自发** → Events (AE, MH, CE, DS, DV)
   - 研究者/医护**施加** → Interventions (EX, CM, PR, AG)
   - 检测/观测**测量** → Findings (LB, VS, EG, LB, PC 等)

2. **Topic 变量**:
   - Events 类: `--TERM` (e.g., AETERM)
   - Interventions 类: `--TRT` (e.g., CMTRT) 或 `--TERM`
   - Findings 类: `--TESTCD` + `--TEST` + `--ORRES`/`--STRESC`

3. **Structure**:
   - Events: 1 record per event per subject
   - Interventions: 1 record per intervention occurrence
   - Findings: 1 record per test per time point per visit per subject

**误判示例**:
- "Rescue medication" (救援用药) → 看作 Intervention (CM), 不是 Event.
- "Protocol Deviation" → Special Purpose (DV), 非标准三类.
- "Baseline lab" → Findings (LB), 不是 Event.

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §4.1.2 (General Observation Classes)

---

### §1.13 Subject Reference Start/End Date 在 Study Day 计算中的角色

**定义 (对照 knowledge_base/domains/DM/spec.md)**:
- **RFSTDTC**: Subject Reference Start Date. Core=Exp. 通常 = 第一次暴露日 (First Dose Date).
- **RFENDTC**: Subject Reference End Date. Core=Exp. 通常 = 最后一次暴露/观察日.
- **RFXSTDTC**: Reference Start Date for Study Treatment (详细首给药). Core=Perm.
- **RFXENDTC**: Reference End Date for Study Treatment. Core=Perm.
- **RFICDTC**: Informed Consent Date. Core=Perm.
- **RFPENDTC**: End of Participation Date. Core=Perm.

**Study Day 计算依据** (ch04 §4.4.3):
- 所有 `--DY` 变量 (e.g., AESTDY, CMSTDY, LBDY) 都相对 **RFSTDTC** 计算 (除非 sponsor 定义特殊 ref).
- `--DY = 日期 - RFSTDTC + 1` (若日期 ≥ RFSTDTC); `= 日期 - RFSTDTC` (若日期 < RFSTDTC, 得负值).
- **Day 1 = RFSTDTC 当日**, 无 Day 0.

**业务意义**:
- Screening 期 (pre-dose) 事件 → AESTDY 负值
- 首日 dosing 即触发的 AE → AESTDY = 1
- 3 天后 AE → AESTDY = 4 (不是 3, 因 Day 1 已消耗)

**pitfall**:
- 把 RFSTDTC 填 informed consent date → **错**. RFSTDTC 通常是 first exposure, 非 consent.
- 把 ICH ref (consent) 和 dose ref (first dose) 混 → RFSTDTC vs RFICDTC 用途不同.

**源路径**: `knowledge_base/domains/DM/spec.md` (RFSTDTC §, RFENDTC §), `knowledge_base/chapters/ch04_general_assumptions.md` §4.4.3

---

### §1.14 EDC → SDTM 的 NULL / "UNKNOWN" / "NOT DONE" 约定

**业务场景**: EDC 里某字段留空, 映射到 SDTM 要不要填特殊标记?

**SDTM 约定 (对照 ch04 §4.2)**:

| EDC 情况 | SDTM 填法 | 示例变量 |
|---------|----------|----------|
| 字段**未收集** (CRF 无此字段) | 目标 SDTM 变量**留空** (NULL) | 任何 Perm/Exp 变量 |
| 字段**已收集但值为空** (subject 未填) | 目标变量留空; 可加 --STAT="NOT DONE" + --REASND | LBSTAT="NOT DONE" + LBREASND="SPECIMEN LOST" |
| 字段收到 "UNKNOWN" | 按 codelist 是否允许 "UNKNOWN" 决定; 若不允许, 留空 + 用 SUPP-- 记 | --CAT, --STAT |
| 字段"N/A" | 一般留空, 不填 "N/A" 字符串 | 各种 Qualifier |

**原则**: SDTM 变量留空比填占位符 (NULL / N/A / UNKNOWN) 优先. 只有在 codelist 明确允许 UNKNOWN 时才填.

**"NOT DONE" 特殊模式 (Findings class)**:
- LBSTAT = "NOT DONE" + LBREASND = <reason>
- LBORRES 留空 (非 "N/A")
- 保留 LBTESTCD / LBTEST 做 denominator

**AE 不收集的特殊处理** (AE assumptions §4.d):
- 若 subject 无 AE, **不**在 AE dataset 建 "no events" record. 空 AE 行 ≠ 正面声明.

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §4.2 (handling of missing values)

---

### §1.15a Vital Signs (VS) 域常规填写

**业务场景**: 访视时测血压, SBP=140 mmHg, DBP=90 mmHg, 位置=坐位.

**SDTM 域**: VS (Vital Signs). Class: Findings.

**拆记录规则**: **每个参数一条记录**. 血压拆 SBP 和 DBP 两条, 不合并.

**核心变量**:

| 变量 | Core | SBP 记录 | DBP 记录 |
|------|:----:|---------|---------|
| VSTESTCD | **Req** | "SYSBP" | "DIABP" |
| VSTEST | **Req** | "Systolic Blood Pressure" | "Diastolic Blood Pressure" |
| VSORRES | Exp | "140" | "90" |
| VSORRESU | Exp | "mmHg" | "mmHg" |
| VSSTRESC | Exp | "140" | "90" |
| VSSTRESN | Exp | 140 | 90 |
| VSSTRESU | Exp | "mmHg" | "mmHg" |
| VSPOS | Perm | "SITTING" | "SITTING" |
| VSLOC | Perm | "ARM" | "ARM" |
| VSLAT | Perm | "LEFT" (or appropriate) | "LEFT" |

**pitfall**:
- 把 SBP/DBP 合并成一个字符串 "140/90" — **错**, 拆两条.
- VSPOS (position) 和 VSLOC (location) 混淆: VSPOS = 体位 (SITTING/STANDING/SUPINE), VSLOC = 身体部位 (ARM/LEG).
- VSORRES 数值化但忘记 VSSTRESN: 数值结果必须双填 VSSTRESC (Char) + VSSTRESN (Num).

**源路径**: `knowledge_base/domains/VS/spec.md`

---

### §1.15b ECG (EG) 域和 Findings Class 模式

**业务场景**: 12 导联 ECG 检查, 结果含 HR (心率) / PR interval / QT / QTc.

**SDTM 域**: EG (ECG). Class: Findings.

**拆记录规则**: **每参数一条**. 每个导联可能再拆.

**核心变量**:

| 变量 | Core | 示例 (HR) |
|------|:----:|----------|
| EGTESTCD | **Req** | "HR" |
| EGTEST | **Req** | "Heart Rate" |
| EGORRES | Exp | "72" |
| EGORRESU | Exp | "beats/min" |
| EGSTRESC | Exp | "72" |
| EGSTRESN | Exp | 72 |
| EGSTRESU | Exp | "beats/min" |
| EGMETHOD | Perm | "12 LEAD ECG" |
| EGLEAD | Perm | (特定导联时填) |
| EGEVAL | Perm | "INVESTIGATOR" |

**pitfall**: QTc 要看是 Fridericia (QTcF) 还是 Bazett (QTcB) 校正, EGTESTCD 不同 (QTCF vs QTCB).

**源路径**: `knowledge_base/domains/EG/spec.md`

---

### §1.15c Exposure 域 EX.EXTRT vs EX.EXDOSE

**业务场景**: 给药 Drug A 50 mg QD, 静脉给药, 持续 28 天.

**核心变量 (对照 knowledge_base/domains/EX/spec.md)**:

| 变量 | Core | 示例 |
|------|:----:|------|
| EXTRT | **Req** | "DRUG A" (Topic, 药物名) |
| EXDOSE | Exp | 50 |
| EXDOSU | Exp | "mg" |
| EXDOSFRQ | Exp | "QD" |
| EXROUTE | Exp | "INTRAVENOUS" |
| EXSTDTC | Exp | "2024-06-15" |
| EXENDTC | Exp | "2024-07-12" |

**EX vs EC 抉择**:
- 按协议计划 dose → EX
- 实际采集到的 dose (可能有漏服/调整) → EC, 保原始

**pitfall**:
- EXTRT 写药物通用名 (USAN/INN), 不写商品名.
- 漏服 dose 记录: EX 的一条跨 28 天 + SUPPEX 记漏服? 还是 EC 每天一条?  → 建议 EC 细粒度, EX 做 summary.

**源路径**: `knowledge_base/domains/EX/spec.md`

---

### §1.15d DS (Disposition) 受试者终止原因

**业务场景**: 受试者在 Week 8 因 AE 提前退出研究.

**SDTM 域**: DS (Disposition). Class: Events.

**核心变量**:

| 变量 | Core | 示例 |
|------|:----:|------|
| DSTERM | **Req** | "Adverse Event" (Topic) |
| DSDECOD | **Req** | "ADVERSE EVENT" (标准 codelist Term) |
| DSCAT | Exp | "DISPOSITION EVENT" |
| DSSCAT | Perm | "STUDY PARTICIPATION" |
| DSSTDTC | Exp | "2024-08-10" |

**pitfall**:
- DSTERM 和 DSDECOD 应该一致 (DSDECOD 来自 C66727 codelist), 但 sponsor 有选择填法.
- 受试者完成研究 (非退出) 也要 DS 记录, DSDECOD="COMPLETED".
- DS 和 EX 的 end date 可能不同 (EX 最后给药日 vs DS 退出/完成日).

**源路径**: `knowledge_base/domains/DS/spec.md`

---

### §1.15e TA (Trial Arms) vs TE (Trial Elements) vs TV (Trial Visits)

**Trial Design 域关系**:
- **TA** (Trial Arms): 各 Arm 下 Element 有序序列. 关键: ARMCD, ELEMENT, ETCD.
- **TE** (Trial Elements): 每 Element 定义. 关键: ETCD, ELEMENT (描述), TESTRL (Start Rule), TEENRL (End Rule).
- **TV** (Trial Visits): Visit 计划. 关键: VISITNUM, VISIT, TVSTRL.

**关系**:
- TA.ETCD **必须**在 TE.ETCD 中存在 (TE 是 TA 的字典).
- DM.ARMCD **必须**在 TA.ARMCD 中存在 (如前 §1.6 所述).
- 受试者实际经过 Element 序列 → SE 域 (非 TA/TE).

**源路径**: `knowledge_base/domains/TA/spec.md`, `knowledge_base/domains/TE/spec.md`, `knowledge_base/domains/TV/spec.md`

---

### §1.15 Controlled Terminology Extensible vs Non-Extensible

**业务场景**: 某 SDTM 变量对应的 NCI codelist 是 "extensible", sponsor 想加自定义 Term 行不行?

**定义 (CDISC Controlled Terminology rule)**:
- **Non-extensible codelist**: sponsor **不得**添加 Term, 必须用已有 Term 值. 如 C66742 No Yes Response 只许 "Y"/"N".
- **Extensible codelist**: sponsor **可**在 Define-XML document 声明自定义 Term, 前提是不与现有 Term 冲突. 如 C66767 Action Taken with Study Treatment 多数是 extensible.

**判定途径**:
- 每 codelist 在 NCI EVS Browser 标有 Extensible Y/N flag.
- 或查 spec.md 的 "Controlled Terms" 字段 + assumptions 说明.

**pitfall**:
- (1) 对 Non-extensible codelist 用自定义 Term → 违规, 审查会 reject.
- (2) Extensible codelist 用了自定义 Term 但未在 Define-XML 声明 → 违规.
- (3) 把 "extensible" 误解为"随便改 codelist 名称" — **错**. Extensible 仅指**添加新 Term**, codelist 自身 identifier/定义不可改.

**如何查 codelist extensible?** → NCI EVS Browser (`https://evsexplore.semantics.cancer.gov/evsexplore/`) 搜 CT Code, 查 codelist metadata 的 Extensible 字段.

---

### §1.16 实验室 Baseline 标记 LBBLFL

**业务场景**: 受试者基线期和 Week 2 都查了 ALT, 需要区分哪个是 baseline.

**SDTM 变量**: LBBLFL = Baseline Flag (Char, Perm, Role=Record Qualifier). 取值 "Y" / Null.

**判定规则 (ch04 §4.2.7)**:
- LBBLFL = "Y" 标记在**分析定义**的 baseline record
- 通常是**研究药首次给药前的最后一次测量**
- 若同日多测, 依 sponsor 规则 (last / average / worst)
- **非 baseline 记录 LBBLFL = Null**, 不填 "N"

**pitfall**:
- LBBLFL 填 "N" — **错**. 按约定只填 "Y" 或留空.
- 多次 screening 测量全标 "Y" — **错**. 只 1 条 baseline.

**源路径**: `knowledge_base/domains/LB/spec.md` §LBBLFL (若有), `knowledge_base/chapters/ch04_general_assumptions.md` §4.2.7

---

### §1.17 CO (Comments) 域用法

**业务场景**: 数据审查员对某 AE 记录有补充说明, 但不是 SUPPAE 的结构化数据.

**SDTM 域**: CO (Comments). Class: Special Purpose.

**核心变量**:

| 变量 | Core | 说明 |
|------|:----:|------|
| STUDYID | **Req** | |
| DOMAIN | **Req** | "CO" |
| USUBJID | Exp | (若 dataset 级关系可空) |
| COSEQ | **Req** | 序号 |
| COREF | Exp | 指向的父记录标识 |
| COVAL | Exp | 评论文本 (≤ 200 字符, 超长拆 COVAL1-COVALn) |
| RDOMAIN | Exp | 父域代码 (如 "AE") |
| IDVAR | Exp | 父域 join 字段 (如 "AESEQ") |
| IDVARVAL | Exp | 父域对应值 |

**CO vs SUPP-- 区别**:
- CO = **自由文本评论**, 无结构
- SUPP-- = **结构化 Qualifier**, 有 QNAM/QLABEL 命名规则
- AE 某记录的"其他备注" → CO
- AE 某记录的"呼吸模式"非标字段 → SUPPAE

**源路径**: `knowledge_base/domains/CO/spec.md`

---

### §1.18 Demographics 域 RACE vs ETHNIC

**业务场景**: 填 DM 域的 RACE 和 ETHNIC.

**SDTM 变量 (对照 knowledge_base/domains/DM/spec.md)**:
- RACE (Exp): 使用 C74457 codelist (Race) 或 sponsor 约定
- ETHNIC (Perm): 使用 C66790 codelist (Ethnic Group)

**关键**: 按 FDA guidance 应**按**规定 codelist 收. sponsor 自定义前提: extensible + Define-XML 声明.

**RACE 多选处理**: 若受试者是混血, **记 SUPP-- QNAM="RACE1"/"RACE2"/...** (不把多 Term 塞 RACE 字段).

**源路径**: `knowledge_base/domains/DM/spec.md` §RACE, §ETHNIC + FDA Race/Ethnicity Data Standards guidance

---

### §1.19 Questionnaire (QS) 和 Findings About (FA) 区分

**业务场景**: 收集 EQ-5D 问卷 (5 个 dimension + 1 VAS) 的 baseline 和 Week 12 数据.

**SDTM 域**: QS (Questionnaires). Class: Findings.

**拆记录规则**: 每 item 一条 (5 dimension 各一条 + VAS 一条 = 6 条 per time point).

**核心变量**:

| 变量 | Core | 示例 |
|------|:----:|------|
| QSTESTCD | **Req** | "EQ5-3M" (Mobility dimension code) |
| QSTEST | **Req** | "EQ-5D-5L Mobility" |
| QSCAT | Exp | "EQ-5D-5L" |
| QSORRES | Exp | "1" (自评等级) |
| QSSTRESC | Exp | "1" |
| QSSTRESN | Exp | 1 |

**QS vs FA 区别**:
- **QS** = 标准化 validated 问卷 (EQ-5D / SF-36 / HAM-D 等)
- **FA** (Findings About Events/Interventions) = 针对 Events/Interventions 的 findings (如 AE 的"皮疹面积"), **FAOBJ** 指向父 event/intervention

**pitfall**:
- 合并 EQ-5D 5 dimension 成一个字符串 — **错**, 拆 5 条.
- QS 的 VAS 部分 (0-100 数值) 混记 → VAS 独立一条 QSTESTCD.

**源路径**: `knowledge_base/domains/QS/spec.md`, `knowledge_base/domains/FA/spec.md`

---

### §1.20 DV (Protocol Deviations) 域

**业务场景**: 受试者访视延迟 5 天, 算 protocol deviation.

**SDTM 域**: DV (Protocol Deviations). Class: Events.

**核心变量**:

| 变量 | Core | 示例 |
|------|:----:|------|
| DVTERM | **Req** | "Visit window exceeded by 5 days" (Topic) |
| DVDECOD | Exp | "VISIT OUT OF WINDOW" |
| DVCAT | Exp | "INCLUSION/EXCLUSION" or "PROCEDURE" |
| DVSTDTC | Exp | "2024-07-05" |

**pitfall**:
- DV 不是 AE — 两者分别走不同域.
- DV 可能关联到某 Visit → RELREC 记 (DV 和 VISIT 表记录关系).

**源路径**: `knowledge_base/domains/DV/spec.md`

---

### §1.21 长文本拆分 (>200 字符)

**业务场景**: AETERM verbatim 文本 350 字符超 SDTM 长度规则.

**SDTM 规则 (ch04 §4.5.3.2)**:
- 标准 Char 变量长度限 200 字符 (AETERM / CMTRT 等)
- 超长文本拆分: 前 200 存父域变量, 余下拆入 **SUPP-- QNAM + 1-digit 后缀**
- 示例: AETERM 200 字符 + SUPPAE QNAM="AETERM1" (后 150 字符)

**命名规则**:
- 第 1 个后缀 QNAM 不带 numeric suffix (QNAM 直接等于父变量)
- 追加 1-digit 累加 (QNAM1, QNAM2, ...)

**pitfall**:
- 把 350 字符塞一个变量 — 可能导致下游工具截断报错.
- SUPP-- QNAM 取数字前缀 — 违规 (QNAM ≤8 且不数字开头).

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §4.5.3.2

---

### §1.22 Findings About (FA) 跨 Events/Interventions

**业务场景**: 某 AE (e.g., 皮疹) 需要记录 "面积 cm²", AE 域无此变量.

**SDTM 选择**:
- **选项 A**: SUPPAE QNAM="AERASHARE" QVAL="15.5 cm²"
- **选项 B**: FA 域 1 record, FAOBJ="AE" + FAREF 指向 AE 记录

**推荐**: 有 Y/N 或单值 → SUPPAE; 有多个 finding 字段 (面积 / 颜色 / 深度) → FA.

**FA 关键字段**:
- FATESTCD / FATEST: finding 代码和名
- FAOBJ: 所关联的 object 类型 (Event/Intervention 的 topic)
- FAORRES / FASTRESC / FASTRESN: 值

**源路径**: `knowledge_base/domains/FA/spec.md`, `knowledge_base/chapters/ch04_general_assumptions.md` §6.4

---

### §1.23 Subject Visits (SV) 域

**业务场景**: 记录受试者实际访视.

**SDTM 域**: SV (Subject Visits). Class: Special Purpose.

**核心变量**:
- STUDYID / DOMAIN / USUBJID / VISITNUM / VISIT / SVSTDTC / SVENDTC

**SV vs SE 区别**:
- SV = 实际**访视** (物理访视日期)
- SE = 实际**经过 Element** (TA/TE 设计层对应)

**源路径**: `knowledge_base/domains/SV/spec.md`, `knowledge_base/domains/SE/spec.md`

---

### §1.24 Non-Compartmental PK (PP) 域

**业务场景**: 计算 AUC / Cmax 等 PK 参数.

**SDTM 域**: PP (PK Parameters). Class: Findings.

**核心变量**:
- PPTESTCD / PPTEST (如 "AUCIFO" / "CMAX")
- PPORRES / PPSTRESC / PPSTRESN
- PPRFTDTC (reference time point date)

**PC vs PP 区别**:
- PC = 血药浓度 (原始采样数据)
- PP = PK 参数 (NCA/compartmental 分析结果)

**源路径**: `knowledge_base/domains/PC/spec.md`, `knowledge_base/domains/PP/spec.md`

---

### §1.25 BE (Bulk Events / Genetics) 和 Microbiology (MB/MS)

**域简介**:
- **BE** (Bulk Events): 已废弃, 被 MB/MS 替代
- **MB** (Microbiology Specimen): 微生物采样
- **MS** (Microbiology Susceptibility): 抗生素敏感性

**核心变量** (MB):
- MBTESTCD / MBTEST (如 "ORG" organism)
- MBORRES: 病原体名 (e.g., "E. coli")
- MBPOS: 阳性/阴性

**MS 关联到 MB**: RELREC + MS.MSORG 指向 MB 的 organism.

**源路径**: `knowledge_base/domains/MB/spec.md`, `knowledge_base/domains/MS/spec.md`

---

### §1.26 常见 Core 属性对照表 (Quick Reference)

本节给**最常问的 6 域** Core 属性摘要, 便于快速查验, 详情查 02 spec.

#### AE 域 (Events, 不规则):
- Req (6): STUDYID, DOMAIN, USUBJID, AESEQ, AETERM, AEDECOD
- Exp (~10): AELLT, AELLTCD, AEPTCD, AEHLT, AEHLTCD, AEHLGT, AEHLGTCD, AEBDSYCD, AESOC, AESOCD, AESER, AEREL, AEACN
- Perm (其余): AESEV, AEBODSYS, AESCAT, AECAT, AESHOSP, AESLIFE, AESDTH, AESDISAB, AESCONG, AESMIE, AESCAN, AESOD, AESINTV, AEUNANT, AEACNOTH, AEACNDEV, AEOUT, AECONTRT, AETOXGR, AEPATT, AERELNST, AELAT, AELOC, 所有 timing

#### CM 域 (Interventions):
- Req (5): STUDYID, DOMAIN, USUBJID, CMSEQ, CMTRT
- Exp: (基本无, 多数 Perm)
- Perm (其余全部, 含 CMINDC, CMDOSE, CMROUTE, CMSTDTC 等)

#### DM 域 (Special Purpose):
- Req (少数): STUDYID, DOMAIN, USUBJID, SUBJID(Exp), RFSTDTC(Exp), RFENDTC(Exp), COUNTRY(Req)
- Exp: RFXSTDTC(Perm), SEX(Req), RACE, ARM, ARMCD, ACTARM, ACTARMCD, ARMNRS, AGE(Exp), AGEU(Exp), DMDTC(Exp)
- 具体逐变量查 02 spec

#### LB 域 (Findings):
- Req: STUDYID, DOMAIN, USUBJID, LBSEQ, LBTESTCD, LBTEST
- Exp: LBCAT, LBORRES, LBORRESU, LBORNRLO, LBORNRHI, LBSTRESC, LBSTRESN, LBSTRESU, LBSTNRLO, LBSTNRHI, LBNRIND, 各种 timing
- Perm: LBMETHOD, LBSPEC, LBSCAT 等

#### PC 域 (Findings):
- Req: STUDYID, DOMAIN, USUBJID, PCSEQ, PCTESTCD, PCTEST
- Exp: PCORRES, PCORRESU, PCSTRESC, PCSTRESN, PCSTRESU, PCLLOQ, PCNAM, PCSPEC
- Perm: PCCAT, PCSCAT, PCMETHOD, PCSPCCND

#### VS 域 (Findings):
- Req: STUDYID, DOMAIN, USUBJID, VSSEQ, VSTESTCD, VSTEST
- Exp: VSORRES, VSORRESU, VSSTRESC, VSSTRESN, VSSTRESU, 各种 timing
- Perm: VSPOS, VSLOC, VSLAT, VSMETHOD

**!! 通用规则**: 每域的 STUDYID / DOMAIN / USUBJID / --SEQ 必 Req; Topic 变量 (--TERM / --TRT / --TESTCD+--TEST) 必 Req. 其余逐变量查 02 spec.

---

## §2. 常见 pitfall 警示 (负例合集)

本节是 §1 场景里零散 pitfall 的**集中版**, 便于审查 checklist 用.

### §2.1 AE 域 Core 属性陷阱 (CO-1 重点)

- **AESEV Core=Perm** (非 Req). 很多 CDM 默认填, 但规范允许空.
- **AESER Core=Exp** (非 Req). AESER=Y 时 Serious 子变量至少 1 个 Y (AE assumptions §7.a).
- **Serious 子变量** (AESHOSP / AESLIFE / AESDTH / AESDISAB / AESCONG / AESMIE) **全部 Core=Perm**. 不是 Req, 但 AESER=Y 时逻辑必填.
- **AEREL Core=Exp**, 但无 SDTMIG 强制 codelist, sponsor 定义 ("RELATED" / "UNLIKELY RELATED" 等).
- **AEACN Core=Exp**, 用 C66767 codelist. 不要和 AEACNOTH (Perm) 混.
- 查 AE 任何变量 Core → **必查 02 spec 对应变量行**, 不按"AE 多数 Req"推断.

### §2.2 LB/PC 数值/字符类型陷阱

- **LBORRES / PCORRES 都是 Char** (允许 "<LLOQ" / ">ULOQ" / "POSITIVE" 等), 不是 Num.
- **LBSTRESN / PCSTRESN 必须 Num**. 字符结果 (如 "POSITIVE") → 这两个变量留空.
- **LBSTRESC / PCSTRESC 是 Char**, 保留所有标准化结果 (数值或字符).
- PCSTRESN 填 0 代 `<LLOQ` 是 **严重 PK 数据错误** (见 §1.5).

### §2.3 DM 域 Arm 双维度陷阱

- ARM/ARMCD = **planned** (designed). 入组后不变.
- ACTARM/ACTARMCD = **actual**. 中途换组/脱落反映在这里.
- TA = **设计**, 不是实际执行. 换组不改 TA.
- SE 域 = **实际经过 Element 序列**, 是换组的权威源.

### §2.4 Timing 和 Study Day 陷阱

- **Day 1 = RFSTDTC 当日**, 无 Day 0.
- ISO 8601 允许部分精度 (年/月/日/时/分/秒), 不强填占位.
- 相对时序词 (ONGOING / BEFORE / DURING / AFTER) → C66728 codelist, 各 --ENRF/--STRF 变量.
- CMSTDTC 早于 RFSTDTC → CMSTDY 负值, 正确.

### §2.5 RELREC vs SUPP-- 陷阱

- 跨域关系 → **RELREC**, 不是 SUPP--.
- 同域非标字段补充 → SUPP--, 不是 RELREC.
- Disease Milestone 关联 → **MIDS 优先**, 不 RELREC (ch04 §4.4.10).
- 同一 RELREC 关系的多条记录必须**同 RELID**.

### §2.6 Terminology 臆造陷阱 (CO-2 重点)

- 本 Gem 不 inline codelist Term 具体值. 所有 Term 查询 → NCI EVS Browser.
- **零臆造 CT Code**: 若问 "<codelist X> 的 CT Code", 答 "请查 NCI EVS 搜 codelist 名", 不从记忆生成.
- **零臆造 Term 值**: 若问 "C66742 codelist 有哪些 Synonym", 答 "请查 NCI EVS 搜 C66742", 不从记忆列.
- 若 §3 索引表列了该 CT Code, 可答 codelist 英文名 (不给 Term 值).

### §2.7 Controlled Terminology 版本陷阱

- SDTM CT Package 每季度更新 (Q1/Q2/Q3/Q4). 同一 CT Code 在不同版本可能增/改 Term.
- sponsor 应在 Define-XML 标注使用的 CT Package 版本.
- 本 Gem 不绑定特定 CT 版本, 如问"某 Term 在 CT 2024Q1 是否存在" → 请查对应版本 NCI EVS.

### §2.8 Study Day 常错算法

- **Day 0 不存在**: SDTM 规定 RFSTDTC 当日 = Day 1, 前一日 = -1, 无 Day 0.
- 跨月跨年: `--DY` 是 **calendar 天差**, 不是 working day.
- 时区不一致导致 Day 计算错 1: 最佳实践同一 study 统一时区或全带 offset.
- RFSTDTC 未定义导致 `--DY` 留空 — 合规但数据受限.

### §2.9 ISO 8601 格式边界

- 只年 `YYYY` 合法, 但某些工具会补 "-01-01" → 丢失精度. 注意 parser 配置.
- "YYYY-MM-DDT" (尾随 T 无时间) — **非法**.
- 日期分隔符**只能 `-`**, 不能 `/` 或 `.`.
- 区间用 `/` 分隔 (`2024-06-15/2024-06-20`), 不用 `~` 或 `to`.
- Duration 前缀 `P` 必须有 (`P3D` 不能 `3D`).

### §2.10 Topic 变量拼写

- 不同 GOC Topic 变量不同:
  - Events: `--TERM` (AETERM / MHTERM / DSTERM / DVTERM / CETERM)
  - Interventions: `--TRT` (CMTRT / EXTRT / AGTRT / PRTRT) 或 `--TERM` 某些域
  - Findings: `--TESTCD` + `--TEST` 组合
- **--TESTCD ≤8 字符**, 同 QNAM 规则.
- Findings About: **FAOBJ** 作为链接变量, 不是典型 Topic.

### §2.11 --SEQ 唯一性

- `--SEQ` 是域内对单 USUBJID 的序号, **必须**唯一.
- 同 USUBJID 两条记录同 --SEQ = **致命错**, 下游 SUPP/RELREC 无法正确 join.
- --SEQ 是 Num, 从 1 开始, 连续或稀疏均可 (推荐连续).

### §2.12 Reference Period 理解

- **Study Reference Period** 定义: 从 RFSTDTC 到 RFENDTC 的时段.
- `--STRF` / `--ENRF` / 其 codelist C66728 Term (BEFORE/DURING/AFTER/ONGOING) 都相对此 period.
- sponsor 可定义**次级 reference** (如"各 dosing period") 写 `--STTPT` / `--ENTPT`, 但 `--STRF` / `--ENRF` 永远对 study reference.

### §2.13 MedDRA 版本与 AEDECOD

- AEDECOD 必须是 MedDRA PT (Preferred Term).
- AELLT (Lowest Level Term) 可选, 但记录原始最低层级.
- **MedDRA 版本**: 同一 Term 可能在新版本微调, sponsor 在 Define-XML 声明版本.
- 从 AETERM 到 AEDECOD 的映射由 MedDRA coding 完成, 不能随意改 AEDECOD.

### §2.14 VS 域多参数拆记录

- 血压拆 SBP / DBP 两条 (不是 "140/90" 一条).
- 脉搏和心率不同: PULSE (外周脉搏) vs HR (心率, EG 域).
- 温度单位常混: VSORRESU 可能 "C" 或 "F", VSSTRESU 统一 "C" (standard).

### §2.15 LB 域 Fasting Status 位置

- LBFAST 在 LB 域 (Char, Perm, C66742 codelist, Y/N).
- PC 域类似有 PCFAST.
- 空腹 vs 餐后数值意义完全不同, LBFAST 填写很重要.

### §2.16 PR (Procedures) vs CM/EX 选择

- 医疗操作/手术 → PR (Procedures) Interventions 域
- 药物给药 → EX (协议 dose) 或 EC (实际)
- 合并药物 → CM
- 三域易混: 看是"药物"还是"操作".

### §2.17 SUBJID vs USUBJID

- SUBJID = study 内 subject ID (非全局唯一, 可能多 study 重用)
- USUBJID = **unique** subject ID (跨 study 全局唯一), 通常 STUDYID-SITEID-SUBJID 拼接
- DM 域两者都有, 其他域只有 USUBJID.

### §2.18 Laterality 和 Location 变量

- `--LAT` (Laterality): LEFT / RIGHT / BILATERAL / UNILATERAL
- `--LOC` (Location): 解剖部位
- `--POS` (Position): 体位 (SITTING / STANDING / SUPINE)
- 三者不互换, 不同 codelist.

### §2.19 Events Class 不用 --OCCUR/--STAT

- AE assumptions §10 明示: AE 域**不用** --OCCUR / --STAT / --REASND.
- 原因: AE 只记实际发生事件, 无 "did it occur?" 语义.
- CE, DS, DV 类似, 但部分 Event 域允许 --OCCUR (如 MH 的 MHOCCUR).

### §2.20 Domain 简写大小写

- SDTM domain code **全大写 2 字符** (AE, CM, LB, 不 "ae" 或 "Ae").
- DOMAIN 变量值 = 大写 2 字符 code.
- 文件名 (XPT) 小写 (ae.xpt, cm.xpt).

### §2.21 --LNKID / --LNKGRP 链接变量

- 用于 RELREC 的 IDVAR 替代 (ch04 §4.4.15).
- `--LNKID` 单记录链接, `--LNKGRP` 组链接.
- 常搭配 RELREC 的 RELTYPE=ONE/MANY.

---

## §3. Controlled Terminology 外部参考 (CT Code → codelist 名索引)

**本 Gem 不 inline codelist Term 具体值** (CO-2 约束). 所有 Term / Synonym / Submission Value 查询走 **NCI EVS Browser**:

- URL: `https://evsexplore.semantics.cancer.gov/evsexplore/`
- 查询方式: 输入 CT Code (如 `C66742`) 或 codelist 名 (如 `No Yes Response`)
- Advanced Search 支持 Synonym / Preferred Term 反查

### §3.1 常问 codelist 索引 (仅 CT Code + codelist 英文名, 不给 Term 值)

本节索引采用**列表格式** (非标准 markdown 表格) 以避免与 codelist Term 值表混淆. 每条仅 CT Code 反引号包裹 + codelist 英文名 + 应用变量, **不含**任何 Term 值.

- `C66742` — "No Yes Response" codelist; 应用: AESER, AESHOSP, AESCONG, AESDISAB, AESDTH, AESLIFE, AESMIE, AESCAN, AESOD, AESINTV, AEUNANT, AEPRESP, CMPRESP, CMOCCUR, MHPRESP, MHOCCUR, PCFAST, PCDRVFL, LBDRVFL 等 Y/N 类二值字段.
- `C66769` — "Severity/Intensity Scale for Adverse Events" codelist; 应用: AESEV (严重性 3 档).
- `C66767` — "Action Taken with Study Treatment" codelist; 应用: AEACN (ICH E2B 行动分类).
- `C66768` — "Outcome of Adverse Event" codelist; 应用: AEOUT.
- `C111110` — "Action Taken with Device" codelist; 应用: AEACNDEV.
- `C66728` — "Relation to Reference Period" codelist; 应用: AEENRF, CMSTRF, CMENRF, MHENRF, CMSTRTPT, CMENRTPT 等相对时序.
- `C66789` — "Completion Status" codelist; 应用: LBSTAT, CMSTAT, MHSTAT, PCSTAT, VSSTAT (NOT DONE 类标记).
- `C78736` — "Reference Range Indicator" codelist; 应用: LBNRIND (三档).
- `C65047` — "Laboratory Test Code" codelist; 应用: LBTESTCD.
- `C67154` — "Laboratory Test Name" codelist; 应用: LBTEST.
- `C71620` — "Unit" codelist; 应用: LBORRESU, LBSTRESU, CMDOSU, EGORRESU 等单位.
- `C102580` — "Laboratory Test Standard Character Result" codelist; 应用: LBSTRESC.
- `C85494` — "PK Units of Measure" codelist; 应用: PCORRESU, PCSTRESU.
- `C85492` — "Method of Test" codelist; 应用: PCMETHOD.
- `C78734` — "Specimen Material Type" codelist; 应用: PCSPEC, LBSPEC.
- `C78733` — "Specimen Condition" codelist; 应用: PCSPCCND, LBSPCCND.
- `C99079` — "Epoch" codelist; 应用: EPOCH (各域 Timing).
- `C142179` — "Arm Null Reason" codelist; 应用: ARMNRS.
- `C66726` — "Unit of Drug Dispensed or Returned" codelist; 应用: CMDOSFRM.
- `C66729` — "Route of Administration" codelist; 应用: CMROUTE, EXROUTE.
- `C124301` — "Medical History Event Date Type" codelist; 应用: MHEVDTYP.
- `C181175` — "Lab Test Condition" codelist; 应用: LBTSTCND.
- `C181170` — "Test Operational Objective" codelist; 应用: LBTSTOPO.
- `C177908` — "Collected Summary Result Type" codelist; 应用: LBCOLSRT.
- `C177910` — "Result Scale" codelist; 应用: LBRESSCL.
- `C179588` — "Result Type" codelist; 应用: LBRESTYP.

**说明**: 本节只列 CT Code → codelist 英文名映射. 具体 Term 值/Synonym/Submission Value 一律查 NCI EVS. 臆造 Term 或 Code 是**硬错误**.

### §3.2 外部参考 URL

| 资源 | URL | 用途 |
|------|-----|------|
| NCI EVS Browser | `https://evsexplore.semantics.cancer.gov/evsexplore/` | 查任一 CT Code / codelist / Term / Synonym |
| CDISC Library | `https://www.cdisc.org/standards/foundational/sdtm` | SDTMIG 版本 + CT Package 下载 |
| CDISC CT Quarterly | `https://www.cdisc.org/standards/terminology/controlled-terminology` | Q1-Q4 CT 更新 release notes |
| FDA Study Data Standards | `https://www.fda.gov/industry/study-data-standards-resources` | FDA 规范版本要求 |
| MedDRA (AE coding) | `https://www.meddra.org/` | AEDECOD 所用字典 |
| WHO Drug (CM coding) | `https://www.who-umc.org/whodrug/` | CMDECOD 所用字典 |

### §3.3 超出本 Gem 范围的查询示例模板

```
用户问: "C66742 codelist 完整 Term 列表?"
回答模板:
  "CT Code C66742 的 codelist 英文名是 'No Yes Response' (见 §3.1). 具体
   Term 值 (如 Submission Value / Synonym 完整列表) 请查 NCI EVS Browser:
   https://evsexplore.semantics.cancer.gov/evsexplore/ 搜 C66742.
   本 Gem 不 inline CT Term 值以保业务场景完整覆盖."
```

```
用户问: "<某未在 §3.1 表列出的 codelist> 的 CT Code 是什么?"
回答模板:
  "本 Gem §3.1 未列此 codelist 的 CT Code. 请查 NCI EVS Browser 输入
   codelist 英文名搜. 本 Gem 不记忆/生成 NCI Code 以避免臆造."
```

---

## §4. 跨域规则 (RELREC / SUPP-- / Timing)

### §4.1 RELREC 跨域关联规则详解

**RELREC 三种用法 (对照 ch04 §8)**:

1. **跨域记录对记录** (最常见): AE #5 和 CM #3 有因果关系
   - 2 条 RELREC 记录, 同 RELID, 各指向 AE 和 CM
   - RELTYPE = "ONE" (一对一) 或 "MANY" (一对多)

2. **同域跨记录**: AE #5 (头痛初始) 和 AE #12 (头痛恶化) 是同一事件阶段
   - 2 条 RELREC 记录, 同 RELID, 都 RDOMAIN="AE"
   - 常用 RELTYPE = "MANY" (一对多)

3. **数据集级关系**: 整个 FA 数据集和某 QS 关联
   - IDVAR 可为空 (dataset-level), 只填 RDOMAIN + RELID
   - ch04 §8.3 明示

**RELREC 字段最小集**:
- STUDYID (Req)
- RDOMAIN (Req) — 父域代码
- USUBJID (可空, dataset 级时)
- IDVAR (可空) — 父域中 join 字段名, 通常 --SEQ
- IDVARVAL (可空) — 父域对应值 (**Char**)
- RELTYPE (Req) — ONE / MANY
- RELID (Req) — 关系标识, 同关系多条记录共享

**避免 RELREC 的情况**:
- Disease Milestone 关联 → 用 **MIDS** 变量 (更强)
- Visit 关联 → 用 **VISITNUM / VISIT** 字段
- Same-subject same-record 补充 → **SUPP--** 不是 RELREC

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §8.1-8.3

### §4.2 SUPP-- 存储边界

**SUPP-- 何时用**:
- 标准域**无对应变量**承载 EDC 字段
- 标准变量有**值限制**但需保留原始 (如 CMINDC 限 5 个 Term 但需保自由文本 → SUPPCM QNAM="CMINDOTH")
- 长文本 >200 字符拆分 (ch04 §4.5.3.2): 前 200 字符在父域变量, 余下拆入 SUPP-- 按顺序加 1-digit 后缀

**SUPP-- 何时不用**:
- 跨域关系 → RELREC
- 标准变量已能容纳 → 直接父域
- 大量非标数据 → 考虑 Findings About (FA) 而非 SUPP--

**SUPP-- QNAM 命名规则**:
- ≤ 8 字符
- 和 --TESTCD 同规则 (数字不可开头, 仅 ASCII 字母数字下划线)
- 可选前缀 (如 "AESOSP" 用 AE 前缀), 但前缀占用字符数

**SUPP-- QLABEL**: ≤ 40 字符, 人类可读

**SUPP-- QVAL**: **Char**, 所有类型都存为 Char (数值也转字符)

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §8.4

### §4.3 Timing 变量体系与 Study Day 计算

**SDTM Timing 变量矩阵**:

| 变量族 | 类型 | 含义 | 示例 |
|-------|------|------|------|
| `--DTC` | Char ISO 8601 | 日期/时间 (绝对) | AESTDTC, CMSTDTC |
| `--DY` | Num | Study Day (相对 RFSTDTC) | AESTDY, LBDY |
| `--STDTC` | Char ISO 8601 | 开始日期 | CMSTDTC |
| `--ENDTC` | Char ISO 8601 | 结束日期 | CMENDTC |
| `--STRF` | Char | 相对 ref period 开始 | CMSTRF (BEFORE/DURING/AFTER/ONGOING) |
| `--ENRF` | Char | 相对 ref period 结束 | CMENRF |
| `--STRTPT` | Char | 相对 ref time point 开始 | CMSTRTPT |
| `--ENRTPT` | Char | 相对 ref time point 结束 | CMENRTPT |
| `--STTPT` | Char | ref time point (开始) | CMSTTPT |
| `--ENTPT` | Char | ref time point (结束) | CMENTPT |
| `--DUR` | Char ISO 8601 duration | 持续时长 | CMDUR ("P3D") |

**Study Day 黄金公式** (ch04 §4.4.3):

```
IF date ≥ RFSTDTC:
    --DY = (date - RFSTDTC) + 1    # Day 1 为 RFSTDTC
ELSE:
    --DY = (date - RFSTDTC)         # 无 Day 0, -1 紧接 Day 1
```

**EPOCH 变量** (ch04 §4.1.4.10):
- EPOCH = ch04 §4.1.4.10 定义的"研究周期 phase" (e.g., SCREENING, TREATMENT, FOLLOW-UP)
- 绑定 C99079 codelist
- 各 General Observation Class 域可有 EPOCH, 但 Core 通常 Perm (i.e., AE.EPOCH Perm, LB.EPOCH Perm)

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §4.4 (Timing), §4.1.4.10 (EPOCH)

### §4.4 Visit 变量

**变量**:
- VISITNUM (Num, Exp in Findings): Visit 序号, 数字
- VISIT (Char, Perm): Visit 名
- VISITDY (Num, Perm): Visit planned Study Day

**关系**: VISITNUM 是 visit 序数 (1, 2, 3, ...), VISIT 是描述 (e.g., "Week 2 Visit"). 两者应**一一对应** (同 VISITNUM 同 VISIT).

**VISIT 和 EPOCH 区别**:
- VISIT = 单次访问 (访视), 可能一个 EPOCH 下有多个 VISIT
- EPOCH = 研究周期段 (SCREENING / TREATMENT / FOLLOW-UP 等)

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §4.4.2

### §4.5 Dataset Splitting 规则

**业务场景**: QS 域数据量巨大 (多个 questionnaire × 多访视 × 多 subject), 拆分 dataset.

**SDTM 规则 (ch04 §3)**:
- 可按 **QSCAT** (questionnaire type) 拆分: QSHAMA (HAM-A), QSHAMD (HAM-D), ...
- dataset name 格式: 原 domain + 2-4 字符 suffix
- 拆分后 SUPP-- 同步拆: SUPPQSHAMA, SUPPQSHAMD
- RELREC RDOMAIN 可填完整 dataset name (如 "QSHAMA") 或仅 domain code ("QS")

**何时拆**:
- 数据量 > 1GB (操作理由)
- 业务语义显著不同 (如多个独立 questionnaire instrument)
- 审查方偏好 (FDA/NMPA 可能有 preference)

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §3.x (Dataset Splitting)

### §4.6 Baseline 和 Analysis Flags

**SDTM 层**:
- `--BLFL` (Baseline Flag, Char, Perm): Y / Null, 标记 baseline record
- 可能也有 `--DRVFL` (Derived Flag): 是否 sponsor 衍生记录

**ADaM 层**:
- SDTM 主要是**原始数据**, 分析 flags (ABLFL, ANL01FL 等) 走 ADaM 层
- SDTM 的 --BLFL 是 "operational baseline", ADaM 的 ABLFL 是 "analysis baseline", 可能不同

### §4.7 EDC → SDTM 映射原则清单

1. **Topic 先定**: 先想域 (AE/CM/LB/...), 再想 Topic 变量 (--TERM / --TRT / --TESTCD).
2. **Class 决定 structure**: Events = 1 record per event; Findings = 1 record per test per time; Interventions = 1 record per occurrence.
3. **Qualifier 分配**: 按 Role (Grouping / Record / Variable / Synonym / Result) 分配字段.
4. **Timing 规范**: 所有日期转 ISO 8601, Study Day 对 RFSTDTC 算.
5. **SUPP/RELREC 用最少**: 先看标准变量能否容纳, 不能再考虑 SUPP/RELREC.
6. **Controlled Terminology 对齐**: 每 Char 变量查 spec 的 C<code>, 填 CT submission value.
7. **NULL 语义**: 标准 SDTM 变量留空 ≠ "NOT DONE" / "UNKNOWN" 字面量.
8. **Define-XML 标注**: 所有 sponsor 约定 / extensible 扩展 / derivation 在 Define-XML 记录.

### §4.8 Split Domain 命名规则

- 拆分 dataset name: 2-4 字符 suffix 接原 domain code
  - 示例: QS → QSHAMA, QSHAMD, QSEQ5D
  - 示例: SUPPQS → SUPPQSHAMA, SUPPQSHAMD
- RDOMAIN 在 SUPP-- 中填**原 2-char domain code** (如 "QS"), 不是 split dataset name.

### §4.9 跨域 Link 可用选项 (优先级)

| 优先级 | 工具 | 用途 | 适用 |
|:------:|------|------|------|
| 1 | **VISIT / VISITNUM** | 同 Visit 内相关 | 所有 Findings/Events/Interventions |
| 2 | **MIDS** (Disease Milestone) | 同 Milestone 内相关 | 有 Milestone 定义时 |
| 3 | **--LNKID / --LNKGRP** | 专门 Link 变量 | 用在 RELREC 的 IDVAR |
| 4 | **RELREC** | 其他跨域关系 | 无上述标准机制时 |
| 5 | **SUPP--** | **非关系, 是补充** | 标准变量不够时 |

**原则**: 优先用**标准机制** (VISITNUM / MIDS / --LNKID), 不够再用 RELREC. **不能**用 SUPP-- 记跨域关系.

### §4.10 Define-XML 关系 (submission 清单)

- **Define-XML v2.0/2.1**: SDTM 变量的 metadata
- 每域的 variable list / CT code / 约束 / derivation 全在 Define.xml
- SDTM 提交必含 Define.xml (FDA 要求)
- codelist extensible 声明也在 Define.xml

---

## §5. smoke v2 10 题判据映射 (自测对照)

本节逐题列 smoke v2 对应的 04 section, 方便自测.

| # | smoke Q 摘要 | 对应 04 section | 关键变量 / 判据 |
|:-:|-------------|----------------|----------------|
| Q1 | CM 合并用药同服两药拆记录 | §1.1 | 两条 CM; CMTRT/CMSEQ Req; CMINDC Perm |
| Q2 | AE 升 SAE, Serious 子变量填写 | §1.2 + §2.1 | AESER=Y Exp; AESHOSP=Y / AESLIFE=N / AESDTH=N / AESDISAB=N / AESCONG=N / AESMIE=N (全 Perm) |
| Q3 | LB HbA1c 超标, LBNRIND 三档 | §1.3 | LBNRIND="H" (L/N/H 三档); LBORRES Char / LBSTRESN Num |
| Q4 | AESEV vs CTCAE Grade 映射 | §1.4 + §2.1 | AESEV 三档 MILD/MODERATE/SEVERE; Grade 5 走 AESDTH; AESEV ≠ AESER |
| Q5 | PK 采样 `<LLOQ` 记法 | §1.5 | PCORRES="<LLOQ" Char; PCSTRESN=NULL; 不填 0 |
| Q6 | DM.ARMCD vs ARM 关系 + 中途换组 | §1.6 | ARMCD Char 20 代号; ARM Full desc; 换组走 ACTARM/SE, TA 不改 |
| Q7 | 病史+CM 双域 | §1.7 | 两域都要; MHENRF="ONGOING" / CMINDC="HYPERTENSION" |
| Q8 | ISO 8601 精度 + Study Day | §1.8 + §4.3 | 允许部分精度; Day 1 = RFSTDTC 当日, 无 Day 0 |
| Q9 | SUPPAE QNAM/QLABEL/QVAL | §1.9 + §4.2 | QNAM ≤8 字符; 举例 AERESPPD / AE Respiration Pattern / Labored |
| Q10 | RELREC vs SUPP-- 选择 | §1.10 + §4.1 | 跨域因果 → RELREC; 2 条记录同 RELID |

---

## §6. 回答模板示例 (CO-3 citation 强制格式)

### §6.1 业务场景题标准回答格式

```
用户: 合并用药同服两种降压药, CM 域如何拆记录?

回答:
**结论**: 拆两条独立 CM 记录, 每药一条. 不能合并 CMTRT.

**核心变量** (每条至少):
- STUDYID (Req): "ABC-001"
- DOMAIN (Req): "CM"
- USUBJID (Req): "ABC-001-0001"
- CMSEQ (Req): 1 / 2 (序号区分)
- CMTRT (Req, Topic): "LOSARTAN" / "AMLODIPINE"
- CMINDC (Perm): "HYPERTENSION" (同指征可两条相同)
- CMSTDTC (Perm): "2024-06-15"

**依据**:
- CM assumptions §2.a: CMTRT 仅单药名, 不含 dose/form
- 两个独立 CMTRT 值 → 两条记录

**源路径**: `knowledge_base/domains/CM/spec.md` §CMTRT, §CMSEQ
          `knowledge_base/domains/CM/assumptions.md` §2.a
```

### §6.2 CT Term 查询的标准边界回答

```
用户: C66742 的完整 Term 列表?

回答:
**结论**: 本 Gem 不 inline codelist 具体 Term 值 (C 方案决策).

CT Code C66742 对应 codelist 英文名: **"No Yes Response"** (见 04 §3.1).

**查询建议**: 请查 NCI EVS Browser:
- URL: https://evsexplore.semantics.cancer.gov/evsexplore/
- 搜索: C66742
- 可看: Preferred Term / Submission Values / Synonym / Extensible flag

**源路径**: 本 Gem 04 §3.1 CT 索引表 (codelist 英文名). 具体 Term 查 NCI EVS (外部).
```

### §6.2b 臆造 CT Code 规避 (CO-2 强化)

```
用户: C117711 的 codelist 是什么?

回答:
**结论**: 本 Gem §3.1 CT 索引表**未收录** C117711. 本 Gem 不记忆/生成 NCI Code.

**查询建议**:
- 若 C117711 是真实 NCI Code, 请查 NCI EVS Browser (https://evsexplore.semantics.cancer.gov/evsexplore/) 搜 C117711, 查看其 codelist 归属.
- 若来源不明 (可能 Code 本身拼写错或其他 system), 建议先核对 Code 来源.

**边界声明**: 本 Gem 拒绝臆造 NCI Code 或臆造 codelist 归属. 零臆造是硬约束 (CO-2).

**源路径**: 本 Gem 04 §0 基本规则 (零臆造硬约束), §3.1 CT 索引表 (已收录清单).
```

### §6.3 AE 域 Core 属性查询标准回答 (CO-1 防污染)

```
用户: AE.AESER 的 Core 是什么? 是 Req 吗?

回答:
**结论**: AE.AESER **Core=Exp** (Expected, 非 Req).

**必读锚点**: AE 域 Core 属性**不规则**:
- Req (6 个): STUDYID / DOMAIN / USUBJID / AESEQ / AETERM / AEDECOD
- Exp (10 个左右): AESER / AEREL / AEACN / AELLT / AELLTCD / AEPTCD / AEHLT / AEHLTCD / AEHLGT / AEHLGTCD
- Perm (其余全部): AESEV / AESHOSP / AESLIFE / AESDTH / AESDISAB / AESCONG / AESMIE 等

**所以**: 不得按"AE 多数 Req"推断 AESER=Req. 逐变量必查 02 spec.

**源路径**: `knowledge_base/domains/AE/spec.md` §AESER (L248)
          本 Gem 04 §2.1 AE 域 Core 陷阱
```

---

## §7. 快速索引 (变量 → 04 section)

- AESEV / AESER / AESHOSP / AESLIFE / AESDTH / AESDISAB / AESCONG / AESMIE → §1.2 + §2.1
- AEACN / AEACNOTH / AEREL → §1.2 + §2.1
- AETOXGR / CTCAE Grade → §1.4
- CMTRT / CMSEQ / CMINDC / CMSTDTC / CMENRF → §1.1, §1.7
- LBTESTCD / LBTEST / LBORRES / LBSTRESC / LBSTRESN / LBNRIND → §1.3 + §2.2
- PCORRES / PCSTRESC / PCSTRESN / PCLLOQ → §1.5 + §2.2
- ARMCD / ARM / ACTARMCD / ACTARM / ARMNRS → §1.6 + §2.3
- MHTERM / MHENRF → §1.7
- AESTDTC / --DY / Study Day → §1.8 + §4.3
- SUPPAE / QNAM / QLABEL / QVAL / IDVAR / IDVARVAL → §1.9 + §4.2
- RELREC / RELID / RELTYPE / RDOMAIN → §1.10 + §4.1
- EX / EC → §1.11
- Events / Findings / Interventions → §1.12
- RFSTDTC / RFENDTC / RFICDTC / Day 1 → §1.13 + §4.3
- NULL / NOT DONE / UNKNOWN → §1.14
- Extensible / Non-extensible codelist → §1.15
- CT Code 索引 → §3.1
- ISO 8601 / --DTC / --DUR → §1.8 + §4.3
- VISIT / VISITNUM / VISITDY → §4.4
- EPOCH → §4.3

---

## §8. 域速查表 (63 域 Class + Structure + 典型 Topic 变量)

本节按 SDTM v2.0 / SDTMIG v3.4 列常见域的 Class 和 Structure, 供快速定位.

### §8.1 Special Purpose 域 (4)

| Domain | Name | Structure | 典型变量 |
|:------:|------|-----------|---------|
| DM | Demographics | 1 record per subject | STUDYID, USUBJID, ARMCD, RFSTDTC |
| CO | Comments | 1 record per comment per subject | COSEQ, COVAL, RDOMAIN |
| SE | Subject Elements | 1 record per actual Element per subject | ETCD, SESTDTC, SEENDTC |
| SV | Subject Visits | 1 record per actual visit per subject | VISITNUM, SVSTDTC |

### §8.2 Interventions Class (6)

| Domain | Name | Topic | Structure |
|:------:|------|-------|-----------|
| CM | Concomitant Medications | CMTRT | 1 per medication intervention per subject |
| EX | Exposure | EXTRT | 1 per protocol-specified dose per subject |
| EC | Exposure as Collected | ECTRT | 1 per CRF dose record per subject |
| AG | Procedure Agents | AGTRT | 1 per procedure agent per subject |
| PR | Procedures | PRTRT | 1 per procedure per subject |
| SU | Substance Use | SUTRT | 1 per substance use per subject |

### §8.3 Events Class (7)

| Domain | Name | Topic | Structure |
|:------:|------|-------|-----------|
| AE | Adverse Events | AETERM | 1 per adverse event per subject |
| MH | Medical History | MHTERM | 1 per medical history event per subject |
| CE | Clinical Events | CETERM | 1 per clinical event per subject |
| DS | Disposition | DSTERM | 1 per disposition event per subject |
| DV | Protocol Deviations | DVTERM | 1 per protocol deviation per subject |
| HO | Healthcare Encounters | HOTERM | 1 per healthcare encounter per subject |
| SA | Clinical Safety | SATERM | 1 per safety event per subject |

### §8.4 Findings Class (许多, 下列部分常见)

| Domain | Name | Topic (--TESTCD / --TEST) | Structure |
|:------:|------|-----|-----------|
| LB | Laboratory Tests | LBTESTCD / LBTEST | 1 per lab test per time point per subject |
| VS | Vital Signs | VSTESTCD / VSTEST | 1 per vital sign measurement per subject |
| EG | ECG | EGTESTCD / EGTEST | 1 per ECG measurement per time point per subject |
| PC | PK Concentrations | PCTESTCD / PCTEST | 1 per concentration per sample per subject |
| PP | PK Parameters | PPTESTCD / PPTEST | 1 per PK parameter per subject (per analyte) |
| QS | Questionnaires | QSTESTCD / QSTEST | 1 per questionnaire item per time point per subject |
| IE | Inclusion/Exclusion | IETESTCD / IETEST | 1 per deviation per I/E criterion per subject |
| MB | Microbiology Specimen | MBTESTCD / MBTEST | 1 per microbiology finding per specimen per subject |
| MS | Microbiology Susceptibility | MSTESTCD / MSTEST | 1 per susceptibility per organism per specimen per subject |
| FA | Findings About | FATESTCD / FATEST + FAOBJ | 1 per finding about an object per subject |
| FT | Functional Tests | FTTESTCD / FTTEST | 1 per functional test per subject |
| RP | Reproductive System Findings | RPTESTCD / RPTEST | 1 per finding per subject |
| RS | Response Evaluations | RSTESTCD / RSTEST | 1 per response per time point per subject |
| SC | Subject Characteristics | SCTESTCD / SCTEST | 1 per characteristic per subject |
| TU | Tumor Identification | TUTESTCD / TUTEST | 1 per tumor identification per subject |
| TR | Tumor Results | TRTESTCD / TRTEST | 1 per tumor measurement per time point |
| CP | Cell Phenotype Findings | CPTESTCD / CPTEST | 1 per cell finding per subject |
| GF | Genomic Findings | GFTESTCD / GFTEST | 1 per genomic finding per subject |
| OE | Ophthalmic Examinations | OETESTCD / OETEST | 1 per ocular exam per eye per visit |
| RE | Respiratory System Findings | RETESTCD / RETEST | 1 per respiratory finding per subject |
| SS | Subject Status | SSTESTCD / SSTEST | 1 per status per subject |
| UR | Urinalysis | URTESTCD / URTEST | 1 per urinalysis finding per subject |

### §8.5 Trial Design 域 (7)

| Domain | Name | Structure |
|:------:|------|-----------|
| TA | Trial Arms | 1 per element per arm |
| TD | Trial Disease Assessments | 1 per assessment schedule |
| TE | Trial Elements | 1 per element |
| TI | Trial Inclusion/Exclusion | 1 per I/E criterion |
| TM | Trial Disease Milestones | 1 per milestone |
| TS | Trial Summary | 1 per summary parameter value |
| TV | Trial Visits | 1 per visit |

### §8.6 Relationship 域

| Domain | Name | Structure |
|:------:|------|-----------|
| RELREC | Related Records | 1 per related record/group/dataset |
| SUPP-- | Supplemental Qualifiers | 1 per suppqual per parent record |
| SUPPQUAL | 集合 SUPP-- 合并 | (若 sponsor 提交合并形式) |
| RELSUB | Related Subjects | 1 per subject pair relationship |

---

## §9. 高频 FAQ 速答

本节用 Q/A 格式直接答最常被问的业务问题, 每 Q 不超过 150 字, 带源路径.

### §9.1 AE / Events 类

**Q: AE 什么时候必须填 AETERM?**
A: 永远, AETERM 是 Topic Req. 每条 AE 记录必有 AETERM verbatim 文本. 源: `knowledge_base/domains/AE/spec.md` §AETERM.

**Q: AESER 和 AESEV 区别?**
A: AESER = 是否 Serious (Y/N, 按 ICH E2A 定义的 6 条 Serious 标准). AESEV = 严重性档 (MILD/MODERATE/SEVERE). 两个完全不同维度, SAE 可以 MILD, SEVERE 可以不 Serious. 源: §1.2 + §1.4.

**Q: AEDECOD 可以为空吗?**
A: 原则 AEDECOD Core=Req 不能空. 但 AE assumptions §2.c 允许: 若 AETERM 未在字典中, AEDECOD 可空 (记在 sponsor 文档). 源: `knowledge_base/domains/AE/assumptions.md` §2.c.

**Q: Serious 子变量几个是 Y 的前提?**
A: 若 AESER=Y, 至少一个 Serious 子变量 (AESHOSP / AESLIFE / AESDTH / AESDISAB / AESCONG / AESMIE) 必须 Y. AE assumptions §7.a. 若 AESER=N, 所有子变量可为 Null.

**Q: 肿瘤试验用 AETOXGR 还是 AESEV?**
A: AE assumptions §7.d 建议肿瘤试验用 CTCAE 时用 **AETOXGR** (Grade 1-5), 一般**不同时填 AESEV 和 AETOXGR**. AETOXGR 保留更细粒度.

### §9.2 CM / Interventions 类

**Q: CM 拆记录 vs EX?**
A: 试验**计划 dose** → EX; **合并用药** (非 study drug) → CM. EX 的 EXTRT = study drug, CM 的 CMTRT = any other medication.

**Q: CMSTDTC 必须填吗?**
A: CMSTDTC Core=Perm, 非必填. 但实际 sponsor 通常都填 (否则无法做 concomitant 分析).

**Q: 两个药一起服怎么填 CMTRT?**
A: **拆两条记录**, 每药一条 CMTRT. CMTRT 只含单药名 (不含 dose/form). 源: §1.1.

### §9.3 LB / Findings 类

**Q: LBTESTCD 最长几位?**
A: ≤8 字符 (所有 --TESTCD 规则统一). 首字母不得数字. 源: LB spec.md §LBTESTCD.

**Q: LBORRES 和 LBSTRESC 区别?**
A: LBORRES = **原始单位**的原始值 (e.g., "120 mg/dL"). LBSTRESC = **标准化单位**的标准化字符值 (e.g., "6.66" in mmol/L). 都是 Char. 源: §1.3.

**Q: LBSTRESN 什么时候空?**
A: 当结果不是数值 (如"POSITIVE" / "<LLOQ" / "POSITIVE >= 1:128") → LBSTRESC 填字符, **LBSTRESN 留空** (因为无法数值化).

**Q: LBNRIND 用什么 codelist?**
A: C78736 Reference Range Indicator (三档 L/N/H 或 ABNORMAL). Char, Exp. 不填 "HIGH"/"LOW". 源: §1.3.

### §9.4 DM / Trial Design 类

**Q: ARMCD 最长几位?**
A: ≤20 字符 (DM.ARMCD / TA.ARMCD / ACTARMCD 同规则). 比其他 `--TESTCD` 的 8 字符上限**宽**, 以支持 crossover 多 Element 命名.

**Q: RFSTDTC 是什么?**
A: Subject Reference Start Date. 通常 = 首次给药日. 所有 `--DY` 变量相对此计算. Core=Exp. 源: `knowledge_base/domains/DM/spec.md` §RFSTDTC.

**Q: ARMNRS 什么时候填?**
A: 当 ARM/ARMCD (或 ACTARM/ACTARMCD) 为空时, 必填 ARMNRS 给原因代码 (如 "SCREEN FAILURE" / "NOT ASSIGNED"). 源: §1.6.

### §9.5 RELREC / SUPP--

**Q: RELREC 何时优于 SUPP--?**
A: 跨域 (AE ↔ CM) 或跨记录 (AE #5 ↔ AE #12) 的**关系**走 RELREC. 单域单记录的**非标字段补充**走 SUPP--. 两者不可替代. 源: §1.10 + §4.1.

**Q: QNAM 长度限制?**
A: ≤8 字符, 同 --TESTCD 规则. QLABEL ≤40 字符.

**Q: RELID 必须唯一吗?**
A: 同关系的多条 RELREC 记录**共享**同 RELID. 不同关系用不同 RELID. RELID 在 study 内 unique.

### §9.6 Timing / ISO 8601

**Q: Study Day 1 是 RFSTDTC 当日吗?**
A: 是. SDTMIG 规定 Day 1 = RFSTDTC 当日, **无 Day 0**. Day -1 是前一日. 源: ch04 §4.4.3.

**Q: ISO 8601 允许部分精度吗?**
A: 允许. `"2024"` / `"2024-06"` / `"2024-06-15"` / `"2024-06-15T14:00"` 都合法. 不强填占位. 源: §1.8.

**Q: 区间用什么分隔?**
A: `/` (如 `"2024-06-15/2024-06-20"`). 不用 `~` 或 `to`.

### §9.7 Controlled Terminology

**Q: 如何查 C66742 的 Term 值?**
A: 查 NCI EVS Browser (`https://evsexplore.semantics.cancer.gov/evsexplore/`) 搜 C66742. 本 Gem 不 inline. 源: §3.

**Q: Extensible codelist 可以加 Term 吗?**
A: 可以, sponsor 可添加不冲突的 Term, 在 Define-XML 声明. Non-extensible 不可. 源: §1.15.

**Q: sponsor 自定义 codelist 怎么办?**
A: 在 Define-XML 定义, 用自己的 CodelistID, 所有该变量引用该 codelist. **不占用** CDISC CT 的 C-code.

---

## §10. 版本映射 (SDTMIG v3.4 + SDTM v2.0)

本 Gem 基于:
- **SDTMIG v3.4** (CDISC Study Data Tabulation Model Implementation Guide, 2023)
- **SDTM v2.0** (Study Data Tabulation Model, 2021)

**SDTMIG v3.3 vs v3.4 主要差异**:
- v3.4 新增若干 domain (如更多 Specialty domains)
- Core 属性调整若干变量
- CT codelist 更新

**SDTM v1.8 vs v2.0 主要差异**:
- v2.0 引入新 Class (Findings About) 的正式定义
- Timing 变量扩充
- Relationship 支持增强

**业务用户角度**: 若你的 study 用 v3.3, 大部分规则相同, 个别 Core 属性需核对对应 IG 版本. sponsor 必在 Define-XML 声明使用的 IG 版本.

---

## §11. 变更记录

| 日期 | 变更 | 原因 |
|------|------|------|
| 2026-04-21 | 04 弹药包首版 (C 方案 Node 4) | 舍弃 terminology inline, 空余容量换业务问答完整覆盖 |

---

*本文件是 Gemini Gems C 方案 Node 4 的核心业务问答弹药包. 任何业务场景题、规则判断题、EDC→SDTM 映射题、跨域鉴别题, 都优先查本文件对应 section, 回答后必附源路径 (CO-3 强制).*
