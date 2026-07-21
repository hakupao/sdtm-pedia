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
| LBNRIND | Reference Range Indicator | Exp | **"HIGH"** | 四档全写: "ABNORMAL"/"HIGH"/"LOW"/"NORMAL" |

**!! LBNRIND 合规取值** (对照 `knowledge_base/terminology/core/general_part4.md` codelist **C78736 Reference Range Indicator** 官方 submission values):
- `"LOW"` = 低于参考范围下限
- `"NORMAL"` = 在参考范围内
- `"HIGH"` = 高于参考范围上限
- `"ABNORMAL"` = 异常但无 HIGH/LOW 方向 (如定性结果)

**必须全写, 禁短码**: C78736 官方 submission value 全部是全写; 本地 KB 若历史片段出现 "H"/"L"/"N" 单字符, 那是笔误或非合规写法, **不得沿用**.

**本场景**: LBNRIND = **"HIGH"** (6.8 > 6.0).

**pitfall**:
- (1) LBNRIND 写 "H"/"L"/"N" 单字符 — **错**. C78736 官方 submission values 全是全写: **HIGH / LOW / NORMAL / ABNORMAL**. 单字符短码非 CDISC 官方, 提交被 reject.
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

**!! DM §1.6 归属硬锚点 (smoke v2 Q6 错位回补, 必读)**:

- **ACTARMCD / ACTARM 都在 SDTM DM 域 Permissible slot** (对照 `knowledge_base/domains/DM/spec.md` §ACTARMCD Order=26 Core=Exp + §ACTARM Order=27 Core=Exp). **它们不在 ADaM (ADaM 的 TRTP/TRTA 是另一层, 由 SDTM DM.ACTARMCD/ACTARM 派生)**, 也**不在 EX 域** (EX 域记 dose 暴露事实, 不记 arm assignment).
- **Planned vs Actual 分层** (对照 `knowledge_base/domains/DM/assumptions.md` §4, §4.a): DM 域同时承载 **两对** arm 变量:
  - 计划层 (Planned): **ARM / ARMCD** (入组时随机化/分配到的 arm, 一般随机化后不变)
  - 实际层 (Actual): **ACTARM / ACTARMCD** (受试者实际经过的 arm, 换组/脱落后与 ARM 不一致)
  - 辅助: **ARMNRS** (Arm Null Reason, C142179 codelist, 如 "SCREEN FAILURE" / "NOT ASSIGNED" / "ASSIGNED, NOT TREATED" / "UNPLANNED TREATMENT", DM/spec.md L250-255 原文示例)
  - 辅助: **ACTARMUD** (Description of Unplanned Actual Arm, 当 ACTARM 无法从 TA 合法值中选取时的自由文本)
- **Core 属性** (DM/spec.md 原文逐变量): ARMCD=Exp, ARM=Exp, ACTARMCD=Exp, ACTARM=Exp, ARMNRS=Exp, ACTARMUD=Exp. **全部 Permissible 集合里, 但 Core=Exp** (非 Req), 实际几乎必填.
- **CT Code 指向**: ARMCD / ACTARMCD **不绑定 CDISC CT** (DM/spec.md §ARMCD Controlled Terms 字段为空, 说明 sponsor 自由命名, 对照 TA.ARMCD). 仅 **ARMNRS** 绑定 C142179 (Arm Null Reason codelist, 见 04 §3.1 第 20 条, 具体 Term 值查 NCI EVS).
- **拆换组场景对号**: smoke v2 Q6 类"Week 4 A → B" 换组问题, **正确答案必须**:
  1. 明确 ACTARM/ACTARMCD 是 DM 域变量 (Permissible slot, 对照 DM/spec.md L230-246)
  2. 明确 ADaM 层的 TRTP/TRTA 是派生层, 不是 SDTM 的 ACTARM/ACTARMCD 本体
  3. 明确 EX 域只记 dose 暴露事实 (EXTRT/EXDOSE/EXSTDTC 等), 不记 arm 切换

**pitfall (反例, 必避)**:
- (1) ARMCD 和 ARM 哪个是代号说反 — ARMCD 是短代号 (Code), ARM 是描述 (Full description).
- (2) 不识别 ACTARM/ACTARMCD 概念, 只改 ARM/ARMCD 记换组 — **错**. ARM/ARMCD 是 planned, 一般入组后不变.
- (3) 把换组信息写到 TA — **错**. TA 是设计, 不是实际.
- (4) 忘记 SE 域专门记录实际经过 Element — SE 是换组/脱落等实际情况的权威源.
- (5) **smoke v2 Q6 硬错案 (必避)**: 答 "实际接受的治疗与计划不符, 应通过 ADaM 的 TRTP/TRTA 变量或 SDTM 的 EX 域（暴露）来区分" — **错层**. ACTARM/ACTARMCD 本身就在 SDTM DM 域 Permissible 变量 slot (DM/spec.md L230-246). ADaM TRTP/TRTA 是派生到 subject-level analysis dataset (ADSL/ADaM) 的变量, 由 SDTM DM.ACTARMCD 作为源字段派生, 不能用它来"代替"SDTM 层的 actual arm 记录. EX 域完全不承载 arm assignment 语义.
- (6) 把 ACTARMCD 写成 "TRTACD" 或其他 ADaM 风格缩写 — **错**. ACTARMCD 是 SDTM 标准变量名 (DM/spec.md §ACTARMCD Order=26 原文).
- (7) 认为 ACTARM 必须和 ARM 保持一致 — **错**. 当受试者换组 / 未治 / UNPLANNED TREATMENT 时 ACTARMCD ≠ ARMCD, 正合 assumption §4.a.iii (ARMNRS 不必填, 因 ARMCD≠ACTARMCD 已自解释).
- (8) 把 "ACTARMCD 可填任意字符串" — **错**. DM/spec.md §ACTARMCD 原文: "With the exception of studies which use multistage arm assignments, **must be a value of ARMCD in the Trial Arms dataset**." 即 ACTARMCD 必须从 TA.ARMCD 中选 (多阶段 arm assignment 除外).

**源路径**:
- `knowledge_base/domains/DM/spec.md` §ARMCD (Order 24) / §ARM (Order 25) / §ACTARMCD (Order 26) / §ACTARM (Order 27) / §ARMNRS (Order 28) / §ACTARMUD (Order 29)
- `knowledge_base/domains/DM/assumptions.md` §4 (arm-related variables 规则 i-iv), §4.a.ii (ACTARMCD null 时 ARMNRS 必填)
- `knowledge_base/domains/SE/spec.md` (SE 定义 + assumptions)
- `knowledge_base/domains/TA/spec.md` (TA 设计层定义, ARMCD 必需出现在 TA)

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
- Req: STUDYID, DOMAIN, USUBJID, SUBJID, COUNTRY, SEX
- Exp: RFSTDTC, RFENDTC, RFICDTC, RFPENDTC, RFXSTDTC(Perm), DTHDTC, DTHFL, SITEID(Req), RACE, AGE, AGEU, **ARMCD, ARM, ACTARMCD, ACTARM, ARMNRS, ACTARMUD**
- Perm: INVID, INVNAM, BRTHDTC, ETHNIC, RFCSTDTC, RFCENDTC, DMDTC, DMDY
- **ACTARMCD / ACTARM 边界锚点** (smoke v2 Q6 错位回补): ACTARM / ACTARMCD **在 SDTM DM 域 Permissible 变量集合** (Order 26, 27, Core=Exp). **不是** ADaM TRTP/TRTA, **也不是** EX 域变量. Planned (ARM/ARMCD) vs Actual (ACTARM/ACTARMCD) 分层都由 DM 承载; ADaM TRTP/TRTA 是基于 DM.ACTARMCD 派生的下游分析变量, 不应用它代替 SDTM 层 actual arm 记录. 源: `knowledge_base/domains/DM/spec.md` §ACTARMCD/§ACTARM + `DM/assumptions.md` §4.
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
- `C78736` — "Reference Range Indicator" codelist; 应用: LBNRIND (官方四档全写 HIGH/LOW/NORMAL/ABNORMAL, 禁 H/L/N 单字符).
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
| Q3 | LB HbA1c 超标, LBNRIND 三档 | §1.3 | LBNRIND="HIGH" (C78736 四档全写 HIGH/LOW/NORMAL/ABNORMAL, **禁 H/L/N 单字符**); LBORRES Char / LBSTRESN Num |
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
A: C78736 Reference Range Indicator. Char, Exp. **官方 submission values 全写**: HIGH / LOW / NORMAL / ABNORMAL (**禁 H/L/N 单字符**). 源: §1.3.

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

## §12. Trial Design 层 (TS / TI / TA / TM / TE / TV 深化)

Trial Design 是 SDTM 里**研究层级** (study-level) 的元数据段, 与 subject-level 数据 (AE/CM/LB/PC 等) 本质不同: Trial Design 域记录的是"试验怎么设计的", 与受试者个体行为无关. 新手最易错的是把 Trial Design 域记录和 subject-level 记录混为一谈.

### §12.1 Trial Summary (TS) 域核心用法

**业务定位**: TS 用一组 (TSPARMCD, TSPARM, TSVAL) 三元组表达"trial summary parameters", 是研究的元数据字段. 典型参数如最小入组年龄、最大年龄、研究类型、诊断代码等.

**核心变量 (对照 `knowledge_base/domains/TS/spec.md`)**:

| 变量 | Label | Role | Core | 说明 |
|------|-------|------|:----:|------|
| STUDYID | Study Identifier | Identifier | Req | |
| DOMAIN | Domain Abbreviation | Identifier | Req | 必为 "TS" |
| TSSEQ | Sequence Number | Identifier | Req | 同 TSPARMCD 多值时递增 |
| TSGRPID | Group ID | Identifier | Perm | 关联相关记录 |
| TSPARMCD | Trial Summary Parameter Short Name | Topic | Req | ≤8 字符, C66738 codelist, 示例 "AGEMIN" / "AGEMAX" |
| TSPARM | Trial Summary Parameter | Synonym Qualifier | Req | ≤40 字符, C67152 codelist |
| TSVAL | Parameter Value | Result Qualifier | Exp | 核心值, 如 "ASTHMA" / "18" / "YES" |
| TSVALNF | Parameter Value Null Flavor | Result Qualifier | Perm | ISO 21090 NullFlavor, 仅 TSVAL 为空时填 |
| TSVALCD | Parameter Value Code | Result Qualifier | Exp | 当 TSVAL 受控于外部 terminology (如 SNOMED CT / NCI C-code), 填对应 code |
| TSVCDREF | Name of Reference Terminology | Result Qualifier | Exp | C66788 codelist (Dictionary Name), 如 "CDISC CT" / "SNOMED" / "ISO 8601" |
| TSVCDVER | Version of Reference Terminology | Result Qualifier | Exp | 版本号, 可空 |

**常见 TSPARMCD 值** (CDISC 官方 C66738 Trial Summary Parameter Test Code, 具体 Term 查 NCI EVS):
- `AGEMIN` / `AGEMAX` — 最低/最高入组年龄
- `PLANSUB` — Planned number of subjects
- `TRT` — Trial type (如 OBSERVATIONAL / INTERVENTIONAL)
- `INDIC` — Indication (适应症, 常填 MedDRA PT 或 SNOMED code)
- `OBJPRIM` / `OBJSEC` — Primary / Secondary objective
- `TCNTRL` — Control type (如 PLACEBO / ACTIVE / NO)
- `TDIGRP` — Diagnosis group
- `RANDOM` — 是否随机化 (Y/N)
- `TBLIND` — 盲态类型 (OPEN / SINGLE BLIND / DOUBLE BLIND)

**业务拆记录规则**: 一个 TSPARMCD 允许多值 (TSSEQ 递增). 例如 study 有多个 indication → 多条同 TSPARMCD="INDIC" 记录, TSSEQ=1/2/3, 各 TSVAL 不同.

**源路径**:
- `knowledge_base/domains/TS/spec.md` (TSPARMCD / TSPARM / TSVAL / TSVALCD / TSVCDREF 逐变量)
- C66738 / C67152 / C66788 见 04 §3.1 (具体 Term 查 NCI EVS)

---

### §12.2 Trial Inclusion/Exclusion Criteria (TI) vs IE 的区别

**业务核心区分** (这是 SDTM 新手最易混的一对):

| 维度 | TI | IE |
|------|-----|-----|
| 类别 | Trial Design (study-level) | Findings (subject-level) |
| Structure | 1 record per I/E criterion | 1 record per I/E criterion **not met** per subject |
| 目的 | **定义** 试验的入排条件 (版本化管理) | **记录** 哪些受试者违反了入排 |
| 粒度 | study-level 元数据 | 每个不满足入排的受试者一行 |

**TI 核心变量** (对照 `knowledge_base/domains/TI/spec.md`):

| 变量 | Label | Core | 说明 |
|------|-------|:----:|------|
| IETESTCD | Incl/Excl Criterion Short Name | Req | 同 IE.IETESTCD, 举例 "IN01"/"EX01" |
| IETEST | Inclusion/Exclusion Criterion | Req | 完整条件文本 |
| IECAT | Inclusion/Exclusion Category | Req | C66797 codelist (INCLUSION / EXCLUSION) |
| IESCAT | Subcategory | Perm | 如 "MAJOR" / "MINOR" |
| TIRL | I/E Criterion Rule | Perm | 可执行规则 (SDTM rule language) |
| TIVERS | Protocol Criteria Versions | Perm | 多版本时标版本号 |

**关键**: TI 的 IETESTCD/IETEST 和 IE 域的**完全同名对应**, 用来**交叉验证**: IE 记录里出现的 IETESTCD 必须在 TI 里找得到.

**源路径**: `knowledge_base/domains/TI/spec.md` (7 变量全), `knowledge_base/domains/IE/spec.md` 对照

---

### §12.3 Trial Arms (TA) 与 Trial Elements (TE) 深化

**TA (Trial Arms) 定位**: 定义 study 内所有合法 arm, 每个 arm 由一系列有序 Element 组成. Structure: 1 record per planned Element per Arm.

**TA 核心变量** (对照 `knowledge_base/domains/TA/spec.md`):

| 变量 | Label | Core | 说明 |
|------|-------|:----:|------|
| ARMCD | Planned Arm Code | Req | ≤20 chars, sponsor 定义, **必被** DM.ARMCD 引用 |
| ARM | Description of Planned Arm | Req | 完整描述 |
| TAETORD | Planned Order of Element within Arm | Req | Element 序数, 从 1 起 |
| ETCD | Element Code | Req | ≤8 chars, 同 TE.ETCD |
| ELEMENT | Description of Element | Perm | |
| TABRANCH | Branch | Exp | 分支条件规则 |
| TATRANS | Transition Rule | Exp | Element 间过渡条件 |
| EPOCH | Epoch | Req | C99079 codelist |

**TE (Trial Elements) 配套**: 定义所有 Element 的详细属性 (起止规则、duration 等). TA 和 TE 通过 ETCD 关联.

**TA 和 DM 的钩接**: DM.ARMCD / DM.ACTARMCD 的合法值集**必须**来自 TA.ARMCD (除 multistage arm assignment 情形外). 这是 SDTM 层级约束的体现.

**源路径**:
- `knowledge_base/domains/TA/spec.md` (ARMCD / ARM / TAETORD / ETCD / TABRANCH / TATRANS / EPOCH)
- `knowledge_base/domains/TE/spec.md` (Element 详细定义)

---

### §12.4 Trial Disease Milestones (TM) — Disease Milestones 专用

**业务定位**: 部分疾病 (尤其 oncology, 慢性病, 多事件随访研究) 需要定义疾病里程碑事件 (如 "hypoglycemic event" / "first progression" / "first relapse"), 作为 timing reference. TM 记录每种 milestone 的定义, 不记录受试者个体发生的 milestone (后者走 Events 类或 MIDS 变量).

**TM 核心变量** (对照 `knowledge_base/domains/TM/spec.md`):

| 变量 | Label | Core | 说明 |
|------|-------|:----:|------|
| STUDYID | Study Identifier | Req | |
| DOMAIN | Domain Abbreviation | Req | 必为 "TM" |
| MIDSTYPE | Disease Milestone Type | Req | Topic 变量, 举例 "HYPOGLYCEMIC EVENT" / "FIRST PROGRESSION" |
| TMDEF | Disease Milestone Definition | Req | 完整定义文本 |
| TMRPT | Disease Milestone Repetition Indicator | Req | C66742 codelist, **"Y"=可重复发生, "N"=只发生一次** |

**MIDS 三角关系** (对照 ch04 §4.4.11 "Disease Milestones"): Disease Milestones 由 **TM** 域定义 (milestone 类型 + 定义 + 是否可重复), 由 **SM** 域 (Subject Disease Milestones, Special-Purpose class, 1 record per Disease Milestone per subject) 记录每个 subject 的 milestone 实际实例. 任何 general observation class 域 (AE/LB/CM/VS/...) 通过 **`--MIDS`** 变量 (引 SM 的 MIDS 实例名) + **`--RELMIDS`** (相对时序) 关联到该 milestone, 避免走 RELREC (更标准化).

**业务 pitfall**: 只有 TM 没有 SM → milestone 只有定义没有 subject 实例, general observation 的 `--MIDS` 值找不到 target. 需 TM + SM + 引用域三方齐备.

**源路径**:
- `knowledge_base/domains/TM/spec.md` (MIDSTYPE / TMDEF / TMRPT, milestone 定义)
- `knowledge_base/domains/SM/spec.md` (Subject Disease Milestones, milestone 实例记录)
- `knowledge_base/chapters/ch04_general_assumptions.md` §4.4.11 Disease Milestones and Disease Milestone Timing Variables (MIDS 跨域机制权威)

---

### §12.5 Trial Visits (TV) — 访视计划定义

**TV 定位**: 定义试验的 planned visit schedule. Structure: 1 record per planned visit per arm.

**核心变量**: VISITNUM / VISIT / VISITDY / TVSTRL (start rule) / TVENRL (end rule) / ARMCD (当不同 arm 有不同 visit schedule 时).

**TV 和 SV 的对比**:
- **TV** (Trial Visits, Trial Design class) = 计划层, study-level
- **SV** (Subject Visits, Special Purpose class) = 实际层, subject-level

**源路径**: `knowledge_base/domains/TV/spec.md`

---

### §12.6 研究层级数据 vs 受试者层级数据的本质区别

这是 Trial Design 段的**业务意义核心**, 也是 SDTM 新手最难过的坎:

| 层级 | 域 | 数据颗粒度 | 更新频率 |
|------|-----|-----------|---------|
| Study-level (研究层级) | TS, TI, TA, TE, TV, TM, TD | 1 record per parameter/criterion/arm/element/visit/milestone | sponsor 设计, 多数不随受试者变 |
| Subject-level (受试者层级) | DM, AE, CM, LB, VS, ... | 1 record per subject per event/observation | 随受试者行为累加 |

**常见错位**: 把 "study 的纳入条件" (IETEST) 记到 IE (subject-level) 而不是 TI (study-level). 正确做法: TI 里定义所有 I/E 条件的 master list; IE 里仅记录**违反** I/E 的受试者和具体违反哪条 (IETESTCD 反查 TI).

**源路径**:
- `knowledge_base/model/05_study_level_data.md` (Trial Design class 模型定义)
- `knowledge_base/chapters/ch04_general_assumptions.md` §3 (Datasets and Domains)

---

## §13. IE 域 (Inclusion/Exclusion Criteria Not Met) 深化

### §13.1 IE 的 subject-level 职责

IE (Class: Findings) 记录**每个受试者不满足的 I/E 条件**, 一 subject 一 criterion 一条记录. 满足所有 I/E 的受试者**在 IE 里完全没有记录** (而不是给一堆 "PASS" 记录).

**核心变量 (对照 `knowledge_base/domains/IE/spec.md`)**:

| 变量 | Label | Role | Core | 示例 |
|------|-------|------|:----:|------|
| STUDYID | Study Identifier | Identifier | Req | |
| DOMAIN | Domain Abbreviation | Identifier | Req | "IE" |
| USUBJID | Unique Subject Identifier | Identifier | Req | |
| IESEQ | Sequence Number | Identifier | Req | |
| IESPID | Sponsor-Defined Identifier | Identifier | Perm | CRF 行号 |
| IETESTCD | Short Name | Topic | Req | 与 TI.IETESTCD 一致, 如 "IN01" |
| IETEST | Criterion Verbatim | Synonym Qualifier | Req | 完整条件文本 |
| IECAT | Category | Grouping Qualifier | Req | C66797 (INCLUSION / EXCLUSION) |
| IESCAT | Subcategory | Grouping Qualifier | Perm | "MAJOR"/"MINOR" |
| IEORRES | I/E Criterion Original Result | Result Qualifier | Req | C66742 (Y/N) — 通常 "N" (not met) |
| IESTRESC | Result in Std Format | Result Qualifier | Req | C66742 标准化结果 |
| VISITNUM | Visit Number | Timing | Perm | 一般 screening 访视 |
| VISIT | Visit Name | Timing | Perm | 如 "Screening" |
| VISITDY | Planned Study Day of Visit | Timing | Perm | |
| TAETORD | Element Order | Timing | Perm | |
| EPOCH | Epoch | Timing | Perm | C99079, 一般 "SCREENING" |
| IEDTC | Date/Time of Collection | Timing | Perm | |
| IEDY | Study Day of Collection | Timing | Perm | 通常负值 (screening 期) |

**IEORRES 语义**: Y (符合本条 I/E 但这条是 Exclusion → 违反), N (不符合本条但这条是 Inclusion → 违反). 结合 IECAT 的 INCLUSION/EXCLUSION 判定 "met or not". 细节见 IE/assumptions.

### §13.2 IE 与 DS (Disposition) 的跨域关系

- IE 记录**入组前**的 I/E 违反, 数据属 Screening epoch (或更早)
- DS (Disposition, Events 类) 记录 subject 的状态事件 (如 "SCREENING FAILURE" / "COMPLETED" / "WITHDRAWN")
- 受试者 screening failure 时: **IE 里有违反记录** + **DS 里 DSTERM="SCREENING FAILURE"** + DM.ARMNRS="SCREEN FAILURE"

**跨域一致性检查**:
- IE 里有 violation → DM.ARMNRS 应填特定原因 (若因 I/E 导致 screen failure)
- DS.DSTERM="SCREENING FAILURE" → DS.DSDECOD (C66731/C99078 或 sponsor CT) 标准化, 同时 DM.RFSTDTC 可能为 null

### §13.3 IE 常见 pitfall

- (1) 把所有 I/E (含 passed) 都记到 IE — **错**. IE 只记 not met 的.
- (2) IEORRES 填 "PASS"/"FAIL" — **错**. IE 用 C66742 (Y/N) codelist.
- (3) IETESTCD 和 TI.IETESTCD 不一致 — **错**. 两者必须映射.
- (4) IECAT 空缺 — **错**. IECAT Core=Req, 必填 INCLUSION 或 EXCLUSION.

**源路径**: `knowledge_base/domains/IE/spec.md`, `knowledge_base/domains/TI/spec.md`, `knowledge_base/domains/DS/spec.md`

---

## §14. Oncology RECIST 链路 (TU / TR / RS / BOR 派生)

### §14.1 三域协同总览

肿瘤评估是 SDTM 里最结构化的 subject-level 跨域链路, **TU → TR → RS** 形成一个完整的 "识别 → 测量 → 评价" 流程:

```
TU (Tumor/Lesion Identification)
   ↓  用 TULNKID 或 TULNKGRP 链接
TR (Tumor/Lesion Results)
   ↓  用 RSLNKID 或 RSLNKGRP 链接
RS (Disease Response)
   ↓
ADaM-ADRS / ADaM-ADTR (派生 BOR, PFS 等)
```

### §14.2 TU (Tumor Identification) 核心变量

**业务定位**: 识别每个 target/non-target/new 肿瘤病灶 (baseline 和后续访视新发). Structure: 1 record per identified tumor per subject per assessor.

**核心变量 (对照 `knowledge_base/domains/TU/spec.md`)**:

| 变量 | Label | Core | 说明 |
|------|-------|:----:|------|
| TUSEQ | Sequence Number | Req | |
| TULNKID | Link ID | Exp | 跨域 link 到 TR 对应测量记录 |
| TULNKGRP | Link Group | Perm | 组链接 |
| TUTESTCD | Tumor/Lesion ID Short Name | Req | C96784 codelist, 如 "TUMIDENT" |
| TUTEST | Tumor/Lesion ID Test Name | Req | C96783, "Tumor Identification" |
| TUORRES | Original Result | Exp | 分类, **RECIST 标准**常用值: "TARGET" / "NON-TARGET" / "NEW" / "BENIGN ABNORMALITY" |
| TUSTRESC | Std Result | Exp | C123650 codelist |
| TULOC | Location | Exp | C74456 codelist, 如 "LIVER" / "LUNG" / "LYMPH NODE" |
| TULAT | Laterality | Perm | C99073, "LEFT" / "RIGHT" / "BILATERAL" |
| TUMETHOD | Method | Exp | C85492, 如 "MRI" / "CT SCAN" / "PET SCAN" |
| TULOBXFL | Last Obs Before Exposure Flag | Exp | "Y" or null |
| TUBLFL | Baseline Flag | Perm | "Y" or null |
| TUEVAL | Evaluator | Exp | 角色, "INVESTIGATOR" / "INDEPENDENT ASSESSOR" / "ADJUDICATION COMMITTEE" |
| TUEVALID | Evaluator Identifier | Perm | 多评估者时区分 |
| TUACPTFL | Accepted Record Flag | Perm | 多评估者时 accepted 的标 Y |

### §14.3 TR (Tumor/Lesion Results) 核心变量

**业务定位**: 每个肿瘤在每个 visit 的测量/评估结果. Structure: 1 record per tumor measurement per visit per subject per assessor.

**核心变量 (对照 `knowledge_base/domains/TR/spec.md`)**:

| 变量 | Label | Core | 说明 |
|------|-------|:----:|------|
| TRLNKID | Link ID | Exp | **必须**对应 TU.TULNKID (回指特定肿瘤) |
| TRTESTCD | Tumor/Lesion Assessment Short Name | Req | C96779, 示例 "TUMSTATE" / "DIAMETER" / "LESSCIND" (Lesion Success Indicator) |
| TRTEST | Test Name | Req | C96778 |
| TRORRES | Original Result | Exp | 原始测量值 (字符), 如 "25.4" mm |
| TRORRESU | Original Units | Exp | C71620, 如 "mm" |
| TRSTRESC | Std Result Char | Exp | C124309 |
| TRSTRESN | Std Result Num | Exp | 数值 |
| TRSTRESU | Std Units | Exp | "mm" (RECIST 直径统一 mm) |
| TRMETHOD | Method | Exp | 如 "CT SCAN", 通常和 TU.TUMETHOD 一致 |
| TREVAL | Evaluator | Exp | 同 TU.TUEVAL |

**RECIST 1.1 常用 TRTESTCD**:
- `DIAMETER` — 直径 (对 Target lesion, 非淋巴结 long-axis, 淋巴结 short-axis)
- `SUMDIAM` — Sum of Diameters (target lesion 直径之和)
- `VOLUME` — 体积
- `TUMSTATE` — 肿瘤状态 (PRESENT / ABSENT / NOT EVALUABLE)

### §14.4 RS (Disease Response) 核心变量

**业务定位**: RECIST 响应评估结果. Structure: 1 record per response assessment per time point per subject per assessor per medical evaluator.

**核心变量 (对照 `knowledge_base/domains/RS/spec.md`)**:

| 变量 | Label | Core | 说明 |
|------|-------|:----:|------|
| RSTESTCD | Assessment Short Name | Req | C96782, 示例 "TRGRESP" / "NTRGRESP" / "OVRLRESP" |
| RSTEST | Assessment Name | Req | C96781 |
| RSCAT | Category | Exp | **C124298** (oncology response criteria) 或 **C118971** (clinical classifications). RECIST 填 "RECIST 1.1". |
| RSORRES | Original Result | Exp | **RECIST 响应值**: "CR" (Complete Response) / "PR" (Partial Response) / "SD" (Stable Disease) / "PD" (Progressive Disease) / "NE" (Not Evaluable) |
| RSSTRESC | Std Char Result | Exp | C96785 (Oncology Response Assessment Result) |
| RSEVAL | Evaluator | Perm | 通常 "INVESTIGATOR" 或 "INDEPENDENT ASSESSOR" |
| RSLNKID | Link ID | Perm | 链到 TR/TU |
| RSLNKGRP | Link Group | Perm | 组链接 |

**常见 RSTESTCD 值 (C96782 codelist)**:
- `TRGRESP` — Target Response
- `NTRGRESP` — Non-target Response
- `NEWLRESP` — New Lesion Response (是否有新病灶)
- `OVRLRESP` — **Overall Response** (单一访视的总体响应)
- `BESTRESP` — **Best Overall Response (BOR)** (整个研究期的最佳响应, 通常派生到 ADRS)
- `PROGR` — Progression indicator

### §14.5 BOR (Best Overall Response) 派生问题

**SDTM vs ADaM 分界**:
- SDTM 层存 **每个 visit 的** OVRLRESP (RS 域, 字符"CR/PR/SD/PD/NE")
- ADaM 层 (ADRS) 派生 **BOR** (single value per subject, 按 RECIST 1.1 §4.3.3 算法), BOR 不在 SDTM

**但**: SDTM RS 域允许填 RSTESTCD="BESTRESP", RSORRES="CR" 之类的派生值, 当 sponsor 把 BOR 作为 subject-level summary 放进 RS 时, 用 RSDRVFL="Y" 标识 derived.

**pitfall**:
- (1) 把 BOR 当成每访视的 response — **错**. BOR 是整个研究期的最佳.
- (2) 混淆 Target / Non-target / New Lesion 的评估: RECIST 1.1 的 OVRLRESP 是**三者联合**结果.
- (3) 不填 RSCAT="RECIST 1.1" — **错**. 不同响应标准 (RECIST 1.0 / 1.1 / iRECIST / Choi / mRECIST) 必须分类明示.

### §14.6 RECIST 链路 smoke 题示例

**典型业务问**: "肿瘤直径合集 baseline=100 mm, Week 8 = 70 mm, 单评估者, OVRLRESP 应该写什么?"
- RECIST 1.1 规则: diameter 减少 >30% → **Partial Response (PR)**, 从 baseline 起始
- 本例 (100-70)/100 = 30% → 恰好 PR 临界, 若**>30%** 严格判 → 不足 PR, 应填 SD. 若**≥30%** 宽判 → PR
- **填法**: RS 记录 RSTESTCD="OVRLRESP", RSORRES="PR" 或 "SD" (取决于 sponsor SAP 对 "≥" 界)
- RSCAT="RECIST 1.1"

**源路径**:
- `knowledge_base/domains/TU/spec.md` (TULNKID / TULOC / TUMETHOD / TUEVAL)
- `knowledge_base/domains/TR/spec.md` (TRLNKID / TRTESTCD / TRORRES / TRSTRESN / TRSTRESU)
- `knowledge_base/domains/RS/spec.md` (RSTESTCD / RSCAT / RSORRES / RSSTRESC / RSEVAL)
- CT Codes: C123650 / C96783 / C96784 (TU), C124309 / C96778 / C96779 (TR), C124298 / C118971 / C96781 / C96782 / C96785 (RS)

---

## §15. AG (Procedure Agents) 域与 EX 的边界

### §15.1 AG 核心变量与定位

**业务定位**: AG 域记录 **与 procedure 相关的 agent 给药** — 典型如 PET 示踪剂 (tracer)、challenge agent (激发试剂)、造影剂. AG 不是 "通常的试验药物" (后者走 EX), 也不是合并药物 (后者走 CM).

**核心变量 (对照 `knowledge_base/domains/AG/spec.md`)**:

| 变量 | Label | Role | Core | 说明 |
|------|-------|------|:----:|------|
| AGSEQ | Sequence Number | Identifier | Req | |
| AGLNKID / AGLNKGRP | Link ID | Identifier | Perm | 链接到 PR 或 Findings 域 |
| AGTRT | Reported Agent Name | Topic | Req | Agent 通用名, 如 "FDG" (PET tracer) / "METHACHOLINE" (challenge) |
| AGMODIFY | Modified Reported Name | Synonym Qualifier | Perm | |
| AGDECOD | Standardized Agent Name | Synonym Qualifier | Perm | 字典标准名 |
| AGCAT | Category for Agent | Grouping Qualifier | Perm | **常用值**: "CHALLENGE AGENT" / "PET TRACER" |
| AGPRESP | Pre-specified | Variable Qualifier | Perm | Y/N, C66742 |
| AGOCCUR | Occurrence | Record Qualifier | Perm | Y/N, C66742 |
| AGDOSE | Dose per Administration | Record Qualifier | Perm | 剂量数值 |
| AGDOSU | Dose Units | Variable Qualifier | Perm | C71620, 如 "mCi" (PET tracer) / "mg" |
| AGDOSFRM | Dose Form | Variable Qualifier | Perm | C66726 |
| AGDOSFRQ | Dosing Frequency | Record Qualifier | Perm | C71113 |
| AGROUTE | Route | Variable Qualifier | Perm | C66729, 如 "INTRAVENOUS" / "INHALATION" |
| AGSTDTC / AGENDTC | Start/End Date | Timing | Perm | |
| AGSTDY / AGENDY | Study Day of Start/End | Timing | Perm | |
| AGSTRF / AGENRF | Relative to Ref Period | Timing | Perm | C66728 |
| EPOCH | Epoch | Timing | Perm | C99079 |

**AG vs EX vs CM 判定矩阵**:

| 给药类型 | 去哪 | 示例 |
|---------|------|------|
| 试验**治疗剂** (interventional drug) | **EX** (Exposure) | 抗肿瘤化疗药 / 单抗 / 小分子 |
| 合并**非试验用药** | **CM** | 降压药、抗生素、对症治疗 |
| **PET / SPECT 示踪剂** | **AG** | FDG / FLT / FMISO (PET tracer) |
| **挑战试剂** | **AG** | Methacholine / exercise challenge 的 pharmacologic challenge |
| **造影剂** | **AG** | 钆对比剂 / 碘对比剂 |
| **Procedure 本身** (非药物) | **PR** | 手术 / 活检 / 影像检查 (程序名) |

### §15.2 AG 与 EX 的协调 (RFCSTDTC / RFCENDTC)

当 study 用 challenge agent, **DM 域的 RFCSTDTC / RFCENDTC** (Core=Perm) 记录 first/last challenge agent dose, 源自 AG 域 AGSTDTC 汇总. 见 `DM/spec.md` §RFCSTDTC Order=9 + DM/assumptions §10.c.

### §15.3 AG 常见 pitfall

- (1) 把 PET tracer 写进 EX — **错**. EX 只记 interventional drug; PET tracer 是 procedure agent 走 AG.
- (2) 把 AG 当成"所有非 EX 给药" — 部分正确但不准. CM 是合并用药 (通常非试验相关), AG 专指 procedure-related agent.
- (3) AGDOSU 空着: PET tracer 必填 mCi 或 MBq (不是 mg).
- (4) AGCAT 空着: "CHALLENGE AGENT" / "PET TRACER" 是有效区分, 审查端重要.

**源路径**:
- `knowledge_base/domains/AG/spec.md` (AGTRT / AGCAT / AGDOSE / AGROUTE / AGSTDTC / AGSTRF)
- `knowledge_base/domains/DM/spec.md` §RFCSTDTC / §RFCENDTC (challenge agent refs)

---

## §16. PR (Procedures) 域与 AE / CM 的跨域链

### §16.1 PR 核心变量

**业务定位**: PR 记录**程序性操作** (surgical procedure / imaging study / biopsy / minor in-clinic procedure), **不是给药**. Structure: 1 record per recorded procedure per occurrence per subject.

**核心变量 (对照 `knowledge_base/domains/PR/spec.md`)**:

| 变量 | Label | Role | Core | 说明 |
|------|-------|------|:----:|------|
| PRSEQ | Sequence Number | Identifier | Req | |
| PRLNKID / PRLNKGRP | Link ID | Identifier | Perm | 链 AE 或 Findings 域 |
| PRTRT | Reported Name of Procedure | Topic | Req | **procedure 名**, 如 "APPENDECTOMY" / "CT SCAN - CHEST" / "ENDOSCOPY" |
| PRDECOD | Standardized Procedure Name | Synonym Qualifier | Perm | C101858 codelist |
| PRCAT / PRSCAT | Category | Grouping Qualifier | Perm | 如 "SURGICAL" / "DIAGNOSTIC" |
| PRPRESP / PROCCUR | Pre-spec / Occurred | Variable/Record Qualifier | Perm | C66742 Y/N |
| PRINDC | Indication | Record Qualifier | Perm | **为何做此 procedure**, 如 "SUSPECTED MI" 回指 AE |
| PRDOSE / PRDOSU | Dose (radiation / contrast 量) | Record Qualifier | Perm | |
| PRROUTE | Route | Variable Qualifier | Perm | C66729 |
| PRLOC / PRLAT / PRDIR / PRPORTOT | Anatomy | Variable Qualifier | Perm | C74456 / C99073 / C99074 / C99075 |
| PRSTDTC / PRENDTC | Start/End | Timing | Exp/Perm | |
| EPOCH | Epoch | Timing | Perm | C99079 |

### §16.2 PR 与 AE 的继发关系

**典型跨域场景**: 受试者发生 AE (如胸痛), 为了诊断/处理 AE, Investigator 安排了 procedure (如心电图、冠脉造影).

**建模**:
- AE 记录: AETERM="Chest pain", AEACN (Action Taken with Study Treatment) 独立于 procedure
- PR 记录: PRTRT="CORONARY ANGIOGRAPHY", **PRINDC="Chest pain"** (indication 回指 AE 诊断)
- 跨域链接: RELREC 两条 (AE 一条 + PR 一条, 同 RELID)

### §16.3 PR 与 CM 的伴随关系

**典型场景**: 手术 (PR) 同时用麻醉 (CM) + 造影剂 (AG).

**建模**:
- PR 一条: PRTRT="APPENDECTOMY"
- CM 多条: CMTRT="FENTANYL" / "PROPOFOL" (麻醉药)
- AG 一条: AGTRT="IODINE CONTRAST AGENT"
- 用 RELREC 或 PRLNKID/PRLNKGRP 串起.

### §16.4 PR pitfall

- (1) 把 procedure 写进 CM — **错**. CM 是**药物/治疗物质**, PR 是**操作**.
- (2) 把 AE 的"处理"写 AE.AEACN 而不用 PR 记 procedure — 不算错但结构化缺失, PR 让"为什么做 / 何时做"可追溯.
- (3) PRINDC 空着: PR assumptions 建议填 indication, 方便后续跨域分析.
- (4) 影像检查走 PR 还是 Findings: 影像**本身**是 PR (procedure), 影像**结果** (如 TR / LB 测量) 走相应 Findings 域.

**源路径**:
- `knowledge_base/domains/PR/spec.md` (PRTRT / PRDECOD / PRINDC / PRLOC / PRSTDTC)
- `knowledge_base/chapters/ch04_general_assumptions.md` §4.1.2 (Interventions class)

---

## §17. 影像场景跨域链 (IE / PR / TU / TR 联动)

### §17.1 典型影像场景: Oncology baseline CT + 基线肿瘤测量

**业务场景**: Oncology study, Screening 期做 Chest CT 扫描, Radiologist 识别 3 个 target lesion + 2 个 non-target lesion.

**SDTM 记录分布**:

| 域 | 做什么 | 关键记录 |
|----|-------|---------|
| **IE** | 受试者是否满足入排 (如果 I/E 要求 "可评估肿瘤 ≥1 个") | 若未满足 → 一条 IEORRES="N" 记录 |
| **PR** | CT 检查作为 procedure | PRTRT="CT SCAN - CHEST", PRDECOD (C101858), PRSTDTC, PRINDC="Tumor assessment" |
| **TU** | 识别出来的 5 个 lesion | 5 条 TU 记录, 每条 TULNKID 唯一, TUORRES="TARGET"/"NON-TARGET", TULOC="LUNG", TUMETHOD="CT SCAN" |
| **TR** | 每个 lesion 的基线测量 | 5 条 TR 记录 (每 lesion 一条, TRTESTCD="DIAMETER", TRSTRESN=... mm), TRLNKID 回指 TU |
| **RS** | baseline overall response (一般不填 baseline RS, BOR 算法从 post-baseline 起) | 或填 RSTESTCD="BASELINE TUMOR BURDEN" |

### §17.2 跨访视随访

**Week 8 再做一次 Chest CT**:
- PR 新记录: 新 PRSTDTC / PRSEQ=2
- TR 新记录: 每 lesion 再一条 (同 TULNKID, TRLNKID 新值或按组策略), TRSTRESN 新测量
- **不需要新建 TU 记录** (除非 Week 8 发现 NEW lesion, 再加一条 TU TUORRES="NEW")
- RS 填 RSTESTCD="OVRLRESP", RSORRES="CR/PR/SD/PD/NE" (按 RECIST 1.1 算)

### §17.3 影像审查方 vs Investigator 双评估

当用 Independent Assessment + Investigator 双评估:
- TU/TR/RS 各有**两套**记录: TUEVAL="INVESTIGATOR" vs "INDEPENDENT ASSESSOR"
- 用 TUACPTFL / TRACPTFL / RSACPTFL 标识哪套是 accepted
- 或用 TUEVALID 区分多个 independent reader (e.g., "RADIOLOGIST1" / "RADIOLOGIST2")
- 当三个 reader 投票时可加 "ADJUDICATION COMMITTEE" (TUEVAL="ADJUDICATION COMMITTEE"), 其记录 ACPTFL="Y"

### §17.4 影像场景 pitfall

- (1) 把 CT scan **结果** (肿瘤测量) 写到 PR — **错**. PR 只记 procedure event, 测量结果走 TR.
- (2) 一个 lesion 在 TU 有一条 + 每访视在 TR 有一条, 搞错 cardinality → 常见错位.
- (3) RECIST 1.1 vs iRECIST 混用: 同一 study 理论可两种 response 标准并存, 用不同 RSCAT 区分, 不同 RS 记录分别填.
- (4) 忘记 TU.TULOC (anatomy location): RECIST 的 lymph node 限制仅 short-axis ≥15 mm 可成 target, 否则 non-target, TULOC="LYMPH NODE" 必填.

**源路径**:
- `knowledge_base/domains/IE/spec.md`
- `knowledge_base/domains/PR/spec.md`
- `knowledge_base/domains/TU/spec.md`
- `knowledge_base/domains/TR/spec.md`
- `knowledge_base/domains/RS/spec.md`

---

## §18. Events Class 深化 (AE / MH / CE / DS / DV / HO 对比)

### §18.1 Events Class 六域分工总览

Events Class **不记录**试验 intervention (那是 Interventions class), 也**不记录** measurement (那是 Findings class). 它只记录"发生了某事件"这个事实.

| 域 | 定位 | Topic | 典型场景 |
|----|------|-------|---------|
| **AE** (Adverse Events) | 试验期内的不良事件 | AETERM | 头痛 / 皮疹 / SAE |
| **MH** (Medical History) | 试验前已有/既往的疾病状态 | MHTERM | 高血压病史 / 既往手术 |
| **CE** (Clinical Events) | 非 AE 的临床事件 (protocol-defined) | CETERM | 复发 / 疾病进展 (非 AE 语义) |
| **DS** (Disposition) | 受试者状态变化 | DSTERM | SCREENING FAILURE / COMPLETED / WITHDRAWN |
| **DV** (Protocol Deviations) | 方案偏离 | DVTERM | 漏访 / 漏服药 / 知情同意违反 |
| **HO** (Healthcare Encounters) | 医疗机构就诊 (非 AE-driven) | HOTERM | 例行随访 / 护理咨询 |

### §18.2 AE vs CE vs MH 的常见混淆

**场景 1**: 受试者既往有糖尿病, 试验期间血糖控制稳定.
- MH: MHTERM="Diabetes mellitus", MHENRF="ONGOING", MHSTDTC 某过去日
- AE: **不记录** (既往疾病不是 AE)

**场景 2**: 受试者既往有糖尿病, 试验期间**血糖失控升高引发症状**.
- MH: MHTERM="Diabetes mellitus" (既往) 仍存
- AE: AETERM="Hyperglycemia" + AETERM="Hypoglycemic event" (试验期**新**事件)

**场景 3**: 肿瘤试验疾病进展.
- **通常走 CE** (CETERM="Disease progression"), 不走 AE (因为 PD 是疾病自然进展, 不是"不良事件"语义)
- 除非 sponsor SAP 规定 PD 计作 AE (少见)
- RS 域并存, 记 RSORRES="PD" 的响应评估

### §18.3 MH 时序变量详解 (MHENRF / MHSTRF / MHENRTPT)

**对照 `knowledge_base/domains/MH/assumptions.md` §5.a**:
- **MHENRF** (End Relative to Reference Period): 相对 **DM.RFSTDTC** (study ref period start). "ONGOING" 在 MHENRF 语义明确.
- **MHENRTPT** (End Relative to Reference Time Point): 相对 sponsor 自定义 reference time point (screening visit / randomization / first dose 等).
- **MHENTPT** (End Reference Time Point): MHENRTPT 参照点的描述.

**ONGOING 填法优先级**:
1. 若 ongoing 是相对 RFSTDTC (即事件持续到试验开始): **MHENRF="ONGOING"** (KB 首选)
2. 若 ongoing 是相对 sponsor 定义 ref (e.g., Screening visit): MHENRTPT="ONGOING" + MHENTPT="Screening Visit"

### §18.4 DS (Disposition) 特殊规则

**DS 单一职责**: 记录"subject 进入了什么状态", 不记录 AE 或疾病事件.

**常见 DSTERM 值** (subject-level):
- `"SCREENING FAILURE"` — 筛选失败 (对应 DM.ARMNRS="SCREEN FAILURE")
- `"COMPLETED"` — 完成所有 protocol 要求
- `"WITHDRAWN BY SUBJECT"` — 主动撤回
- `"LOST TO FOLLOW-UP"` — 失访
- `"ADVERSE EVENT"` — 因 AE 退出 (DS.DSDECOD 标准化)
- `"DEATH"` — 死亡

**DS 和 DM 的一致性**:
- DS.DSDECOD="DEATH" → DM.DTHDTC 必填 + DM.DTHFL="Y"
- DS.DSDECOD="SCREENING FAILURE" → DM.ARMNRS="SCREEN FAILURE"
- DS.DSDECOD="ADVERSE EVENT" → 应有对应 AE 记录 AEACN="DRUG WITHDRAWN" 或类似

### §18.5 DV (Protocol Deviations) 和 TV / IE 的差异

- **TV**: 计划 visit schedule (study-level design)
- **IE**: 入排条件**未满足**的受试者记录 (多在 screening)
- **DV**: 试验期内任何**方案偏离** (漏访 / 漏服 / 超窗 / 入排后才发现违反)

**DV 示例**: 受试者 Visit 3 超窗 (plan Day 28±3, 实 Day 35) → DV 一条 DVTERM="Visit 3 out of window", DVDECOD 分类.

### §18.6 HO (Healthcare Encounters) 域

相对新 (SDTMIG v3.4 引入), 用于记录"非 AE 驱动的就诊事件", 如 routine healthcare visit, social worker visit. 结构与 AE 类似 (Events class), Topic=HOTERM.

**源路径**:
- `knowledge_base/domains/AE/spec.md` + assumptions.md
- `knowledge_base/domains/MH/spec.md` + assumptions.md §5.a
- `knowledge_base/domains/CE/spec.md`
- `knowledge_base/domains/DS/spec.md`
- `knowledge_base/domains/DV/spec.md`
- `knowledge_base/domains/HO/spec.md`

---

## §19. SUPPQUAL 深化: 非标字段的合规存储

### §19.1 SUPP-- 与 SUPPQUAL 的关系

- **SUPP--** (如 SUPPAE / SUPPCM) = **按域拆分**的 supplemental qualifier 数据集, 每 parent domain 一个 SUPP-- 数据集
- **SUPPQUAL** = 可选的**合并形式**, sponsor 可将所有 SUPP-- 合并成一个 SUPPQUAL 数据集提交 (FDA 允许两种形式)

**提交惯例**: SDTMIG v3.4 推荐**按域拆分** (SUPPAE + SUPPCM + ...), 不推荐合并 SUPPQUAL. 但有些审查端偏好合并形式.

### §19.2 SUPP-- 核心字段再释

| 变量 | 含义 | Char/Num | 示例 |
|------|------|:--------:|------|
| STUDYID | Study ID | Char | |
| RDOMAIN | **父域 2 字符代码** | Char | "AE" / "CM" / "MH" |
| USUBJID | Unique Subject ID | Char | (subject-level 或 record-level 时必填; dataset-level 可空) |
| IDVAR | 父域 join 字段名 | Char | "AESEQ" (通常) / null (dataset-level) |
| IDVARVAL | 父域 join 字段值 | **Char** | "12" (即使 AESEQ 是 Num, 这里也转 Char) |
| QNAM | Qualifier Name | Char | ≤8 chars, "AERESPPD" / "AESOSP" |
| QLABEL | Qualifier Label | Char | ≤40 chars, 人读形式 |
| QVAL | Qualifier Value | **Char** | 所有 type 都转 Char |
| QORIG | Value Origin | Char | "CRF" / "DERIVED" / "ASSIGNED" |
| QEVAL | Evaluator | Char | "INVESTIGATOR" 等 |

**QNAM 命名**:
- ≤8 字符, 和 --TESTCD 同规则 (ASCII 字母数字下划线)
- 可选前缀父域 2-char (如 "AESOSP" 用 "AE" 前缀), 但占用 2 字符. 大多 sponsor 不加前缀 (节约字符预算)
- 首字符不得数字

### §19.3 SUPP-- 典型业务场景

**场景 1**: AE 需要"皮疹面积 cm²"字段, AE 域无此变量.
- SUPPAE: QNAM="AEAREA", QLABEL="AE Rash Area (cm²)", QVAL="25.4" (即使数值也转 Char)
- IDVAR="AESEQ", IDVARVAL="5" (指向 AE 的 AESEQ=5 记录)

**场景 2**: CM 域的 CMINDC 只填了一个指征, 受试者实际有两个 (如降压药用于 HTN + prophylaxis).
- SUPPCM: QNAM="CMINDC2", QLABEL="Secondary Indication", QVAL="Prophylaxis"
- 或直接在 CMINDC 里用多值分隔 (取决于 sponsor convention; 推荐 SUPPCM)

**场景 3**: Dataset-level supplement (罕见).
- IDVAR 和 IDVARVAL 都空
- USUBJID 空
- QNAM="STUDYGROUP", QVAL="Phase II Cohort A"

### §19.4 SUPP-- 不该用的场景

1. **跨域关系** → RELREC, 不是 SUPP--
2. **标准变量已能容纳** → 直接父域变量, 不必 SUPP--
3. **大量非标字段** → 考虑 FA (Findings About) 或 custom domain, 避免 SUPP-- 数据爆炸
4. **基础标识字段** (如 SUBJID 之外的 subject 识别) → 直接父域 Identifier variables

### §19.5 SUPP-- 与长文本拆分的区别

**长文本拆分** (ch04 §4.5.3.2): 某标准变量 (如 AEACNOTH, CMTRT) 超 200 字符时, 拆入 SUPP-- 按顺序加 1-digit 后缀:
- 父域: AEACNOTH (前 200 字符)
- SUPP: QNAM="AEACNOT1" (第 201-400 字符), QNAM="AEACNOT2" (第 401-600 字符) ...

**非标字段 SUPP--** (常见用法): QNAM 自定义名表达域没覆盖的语义.

两者都用 SUPP--, 但 QNAM 命名模式不同.

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §8.4 (Relating Non-Standard Variable Values), §4.5.3.2 (Long Text Truncation)

---

## §20. 变量命名规则 & 业务 checklist

### §20.1 SDTM 变量命名前缀规则

**域 2 字符代码作为前缀**: 每域变量以域代码开头 (AE-, CM-, LB-, ...) 例外:
- Identifier 公用变量 (STUDYID / DOMAIN / USUBJID / SUBJID) **不带前缀**
- Timing 公用变量 (VISITNUM / VISIT / VISITDY / EPOCH / TAETORD) **不带前缀**

**--* 变量族 (per-domain)**: 同一语义在不同域用相同后缀:
- `--SEQ` — 序列号 (AESEQ / CMSEQ / LBSEQ)
- `--TERM` — Events Topic (AETERM / MHTERM)
- `--TRT` — Interventions Topic (CMTRT / EXTRT / AGTRT / PRTRT)
- `--TESTCD` / `--TEST` — Findings Topic (LBTESTCD / VSTESTCD)
- `--ORRES` — Original Result
- `--STRESC` — Std Char Result
- `--STRESN` — Std Num Result
- `--ORRESU` — Original Unit
- `--STRESU` — Std Unit
- `--DTC` — DateTime (ISO 8601)
- `--DY` — Study Day
- `--STDTC` / `--ENDTC` — Start/End DateTime
- `--STRF` / `--ENRF` — Start/End Relative to Ref Period (C66728 codelist)
- `--LOBXFL` — Last Obs Before Exposure Flag
- `--BLFL` — Baseline Flag
- `--DRVFL` — Derived Flag

### §20.2 命名长度限制

- 变量名 ≤8 字符 (SAS transport XPT 限制, SDTM 沿用)
- `--TESTCD` ≤8 字符 (Topic code, 业务值)
- `--TEST` ≤40 字符 (Topic name)
- **ARMCD** ≤20 字符 (DM/TA 破例, 支持 crossover)
- QNAM ≤8 字符
- QLABEL ≤40 字符

### §20.3 EDC → SDTM 映射 checklist (业务用)

**Step 1: 确定 General Observation Class**:
- [ ] 受试者主动: Events → 选 AE/MH/CE/DS/DV/HO
- [ ] 研究者施加: Interventions → 选 CM/EX/EC/AG/PR/SU
- [ ] 客观测量: Findings → 选 LB/VS/EG/PC/PP/QS 等
- [ ] 特殊: Special Purpose (DM/CO/SE/SV) 或 Trial Design (TA/TE/TS 等)

**Step 2: 域内 Topic 定值**:
- [ ] Events: `--TERM` Verbatim
- [ ] Interventions: `--TRT` medication/procedure name
- [ ] Findings: `--TESTCD` + `--TEST` 配对

**Step 3: Qualifier 分配**:
- [ ] Grouping: `--CAT` / `--SCAT`
- [ ] Record: `--SER` / `--REL` 等 domain-specific
- [ ] Variable: `--DOSU` / `--LAT` / `--DIR` 等
- [ ] Synonym: `--DECOD` / `--MODIFY`
- [ ] Result: `--ORRES` / `--STRESC` / `--STRESN` / `--ORRESU` / `--STRESU`

**Step 4: Timing 规范**:
- [ ] 所有日期转 ISO 8601
- [ ] Study Day 对 RFSTDTC 算
- [ ] 相对时序 (`--STRF` / `--ENRF`) 用 C66728 codelist
- [ ] EPOCH 赋 C99079 codelist 值

**Step 5: SUPP/RELREC 判断**:
- [ ] 标准变量能否容纳? 能 → 直接填
- [ ] 跨域/跨记录关系? 是 → RELREC
- [ ] 单记录非标字段? 是 → SUPP--

**Step 6: CT Code 对齐**:
- [ ] 每 Char 变量查 spec 的 C<code>, 填 CT submission value
- [ ] 非标变量 (SUPP--) 可用 sponsor 定义 codelist, Define-XML 声明

**Step 7: Null 语义处理**:
- [ ] 标准 SDTM 变量**留空** ≠ "NOT DONE" / "UNKNOWN" 字面量
- [ ] 只有在 codelist 明确允许 "UNKNOWN" 时填 "UNKNOWN"

**Step 8: Define-XML 记录**:
- [ ] 所有 sponsor 约定、extensible 扩展、derivation 在 Define-XML 记

### §20.4 常见 --REQ/--EXP/--PERM Core 速查

**通用规律**:
- STUDYID / DOMAIN / USUBJID / **--SEQ**: 全域 Req
- Topic 变量 (--TERM / --TRT / --TESTCD+--TEST): Req
- 域特异高频 variable (如 AE.AESER / LB.LBNRIND): 一般 Exp
- 其他 Qualifier / Timing: 一般 Perm
- **例外**: AE 域 Core 不规则, 详 §1.2 + §2.1 硬锚点
- **例外**: DM 域多个 Exp 而非 Req (ARMCD / ARM / ACTARMCD / ACTARM)

### §20.5 非标 domain 扩展 (custom domain)

若 sponsor 有 SDTM 未覆盖的数据类型, 可创建 **custom domain**:
- 域代码可用 X- / Y- / Z- 前缀或 2 字符 sponsor 特定代码 (需 Define-XML 声明)
- 变量命名仍遵 SDTM `--*` 规则
- 在 Define-XML 标"sponsor custom", 不能与 CDISC 标准域代码冲突

**源路径**:
- `knowledge_base/chapters/ch04_general_assumptions.md` §4 (Variable Naming)
- `knowledge_base/model/02_observation_classes.md` (General Observation Classes)

---

## §21. 常见 EDC → SDTM 专项补丁

### §21.1 Lab 数据的标准化单位转换

**业务挑战**: EDC 收到 lab 结果多种单位 (传统单位 / SI 单位), SDTM 要求 `--STRESN/--STRESU` 一致化.

**做法 (对照 LB/assumptions §3)**:
- LBORRES/LBORRESU 保**原始** (如 "120 mg/dL")
- LBSTRESC/LBSTRESN/LBSTRESU 填**标准化** (如 SI 单位 "6.66 mmol/L")
- Define-XML 标注 conversion factor

**常见 conversions**:
- Glucose: mg/dL → mmol/L (/18.0156)
- Creatinine: mg/dL → µmol/L (×88.42)
- Hemoglobin: g/dL → g/L (×10)

**pitfall**: 若标准单位无法换算 (如字符"POSITIVE"), LBSTRESC 保原值, LBSTRESN 留空, LBSTRESU 可用 NULL 或原单位.

### §21.2 Questionnaire (QS) 域的 multi-item 处理

**业务场景**: HAM-D (Hamilton Depression Rating Scale) 共 17 或 21 item, 每 item 多选项 + 总分.

**SDTM 做法**:
- QS 一条记录一个 item: QSTESTCD / QSTEST / QSORRES / QSSTRESC / QSSTRESN
- QSCAT="HAMD" 区分 instrument
- 总分也作为一条 QS 记录, QSTESTCD="HAMDTOT", QSDRVFL="Y" (derived 派生值)
- 每 item 独立 subject-visit-item 记录

**Dataset 拆分**: 若 QS 数据量巨大, 按 QSCAT 拆成 QSHAMD / QSHAMA 等 (ch04 §3 Dataset Splitting).

### §21.3 Vital Signs 三体位血压

**业务场景**: orthostatic hypotension assessment, 测 supine + sitting + standing 三个血压.

**SDTM 做法** (每体位 SBP + DBP 两条):
- 共 6 条 VS 记录: SBP×SITTING / DBP×SITTING / SBP×STANDING / DBP×STANDING / SBP×SUPINE / DBP×SUPINE
- 每条 VSPOS 不同 ("SITTING" / "STANDING" / "SUPINE")
- VSTPT (Planned Time Point) 可加时间描述 ("2 min after standing")

### §21.4 Lab Reflex Testing (反射检测)

**场景**: primary lab test 阳性触发 reflex 做 confirmatory test (如 HIV screening → confirmatory Western Blot).

**SDTM 做法**:
- LB 两条记录: LBTESTCD="HIVSCR" (primary) + LBTESTCD="HIVCONF" (reflex)
- 用 LBLNKID 或 SUPPLB.RELREC 关联两条
- LBCAT 区分 "SCREENING" / "CONFIRMATORY"

### §21.5 PK vs PD 数据

- **PC (PK Concentrations)**: 药物浓度, Findings class, 每采样点一条
- **PP (PK Parameters)**: PK 参数 (AUC / Cmax / Tmax), Findings class, 通常每 subject-analyte 一组
- **FA (Findings About) for PD**: 药效学结果 (biomarker 变化), Findings About 承载

**数据流**: EDC 采血 → LB 分析物浓度 (PC 域) → ADaM 派生 AUC/Cmax (PP 域部分可直接存 SDTM).

### §21.6 Adverse Event Time-to-Event 数据

AE 的 time-to-event 分析 (如 Time to First Grade ≥3 AE) 通常在 ADaM 层 (ADAE / TTE datasets) 派生, **不在 SDTM**.

SDTM 提供原料:
- AESTDTC (AE 起始)
- AETOXGR (toxicity grade, 若用 CTCAE)
- RFXSTDTC (首次暴露, 分母)

### §21.7 Electronic Diary (eDiary) 数据

**场景**: 受试者每日记录疼痛评分 (0-10 VAS scale), 持续 28 天.

**SDTM 做法**:
- FT (Functional Tests) 或 QS 承载
- 每天一条记录, VISITNUM 可空 (非 visit-based), FTTPT/FTTPTREF 记录具体时间点
- FTSTRESN 数值

**VISITNUM 空的合规性**: eDiary 通常不关联 formal visit, 但 ch04 §4.4 允许无 VISITNUM 只有 DTC. 可用 sponsor 自定义 Epoch 关联 (如 "DIARY PHASE").

### §21.8 Pregnancy Reporting

**场景**: Subject 或其伴侣怀孕, 需要 SDTM 报告.

**SDTM 做法**:
- **RP (Reproductive System Findings)** 主承载: RPTESTCD="PREG", RPORRES="POSITIVE"
- SR (Skin Response) 不用
- 若后续有 AE (妊娠 AE 如 miscarriage), AE 域记录并 RELREC 关联 RP

**pitfall**: 不用 AE 记录妊娠本身 (妊娠不是"不良"事件), 除非 SAE (如致命 congenital anomaly).

**源路径**:
- `knowledge_base/domains/LB/assumptions.md` §3 (unit conversion)
- `knowledge_base/domains/QS/spec.md`, `knowledge_base/domains/QS/assumptions.md`
- `knowledge_base/domains/VS/spec.md`
- `knowledge_base/domains/PC/spec.md`, `PP/spec.md`
- `knowledge_base/domains/FT/spec.md`
- `knowledge_base/domains/RP/spec.md`

---

## §22. Specialty Finding 域精选场景

本节对 Findings Class 里**不常问但容易踩坑**的 specialty 域做精确定位, 覆盖 MB / MS / MI / CP / GF / OE / SC / SS / UR / NV 等 sub-specialty.

### §22.1 MB + MS 微生物双域

**场景**: 痰培养分离出某病原体, 做抗生素敏感性.

- **MB (Microbiology Specimen)**: MBTESTCD="ORG" / "ORGNM" / "ORGCOLONY", MBORRES 填病原体名 (e.g., "E. coli"). Topic 是"找到了什么"
- **MS (Microbiology Susceptibility)**: MSTESTCD 填抗生素名, MSORRES 填 "S" (sensitive) / "I" (intermediate) / "R" (resistant) / MIC 数值. 一个 organism 对多药敏感性 → 多条 MS.
- **跨域关联**: RELREC 把 MB 的 organism 和 MS 记录串起.

### §22.2 MI (Microscopic Finding) 病理微观

组织切片镜下发现 (非 gross pathology). MITESTCD / MITEST 定义镜下检测项, MIORRES 结果. 常见 Category: "BIOPSY" / "AUTOPSY" / "CYTOLOGY".

### §22.3 CP + GF 分子 / 基因组

- **CP (Cell Phenotype Findings)**: 流式细胞分析 (CD4+ / CD8+ 计数)
- **GF (Genomic Findings)**: 基因突变 / 拷贝数变异 / 基因表达. GFTESTCD = 基因名 或"突变类型", GFORRES 填突变/状态描述.

### §22.4 OE (Ophthalmic Exam) 眼科检查

**业务特点**: 每只眼单独一条 (左/右), OELAT="LEFT"/"RIGHT"/"BILATERAL" 必填. OETESTCD 支持 "VACUITY" (视力) / "IOP" (眼压) / "FUNDUS" 等.

**pitfall**: 双眼合并填一条 → **错**, 必须拆两条 OELAT 各值.

### §22.5 SC (Subject Characteristics) 与 DM 的界限

- DM: 常用 demographics 字段 (age / sex / race / ethnicity / arm)
- SC: 其他 subject-level characteristics (handedness / education / smoking status), SCTESTCD 灵活扩展

**选择**: 若不是标准 DM 字段但是 subject-level 且 time-invariant → SC.

### §22.6 SS (Subject Status) 状态快照

记录不同时间点的"subject 状态变量", 如 "Performance Status (ECOG)" / "Karnofsky Score". SSTESTCD / SSORRES. 和 CE / DS 的事件语义不同: SS 是"状态值" (如 ECOG=2), 不是"状态变化事件".

### §22.7 UR (Urinary System Findings) 尿系统发现域

独立 Findings 域 (Urinary System Findings, 非 LB), 承载尿检 (urinalysis) 项 + 其他泌尿系统 findings. URTESTCD 绑 C129942 (Urinary System Test Code), 支持尿常规 ("pH" / "SPEC_GRAV" / "PROTEIN" / "BLOOD") + semi-quantitative 结果 (trace/+/++/+++) + 其他泌尿发现. 业务边界: Label "Urinary System Findings" 比 Urinalysis 更广, 但 urinalysis 场景是其最常用子集.

### §22.8 NV (Nervous System Findings) 神经系统

类似 OE, 支持神经学检查结果 (reflexes / strength / sensory). NVTESTCD 用 standardized test codes.

### §22.9 specialty 域 pitfall 共性

- (1) 全 Findings class, Topic 都是 `--TESTCD` + `--TEST`
- (2) laterality/location 变量 (--LAT / --LOC / --POS) 在 specialty 域使用率高
- (3) 结果字段永远 `--ORRES` (Char 原始) + `--STRESC`/`--STRESN` (Std)
- (4) 常与 TU/TR/RS 或 LB 通过 RELREC 协同

**源路径**:
- `knowledge_base/domains/MB/spec.md`, `MS/spec.md`
- `knowledge_base/domains/MI/spec.md`
- `knowledge_base/domains/CP/spec.md`, `GF/spec.md`
- `knowledge_base/domains/OE/spec.md`
- `knowledge_base/domains/SC/spec.md`, `SS/spec.md`
- `knowledge_base/domains/UR/spec.md`
- `knowledge_base/domains/NV/spec.md`

---

## §23. 业务 Q&A 补充 (场景类高频, 不重复 §9)

### §23.1 Oncology 场景

**Q: Oncology study 里"Disease Progression (PD)"走哪个域?**
A: 首选 **CE (Clinical Events)** CETERM="Disease progression"; 同时在 **RS (Disease Response)** 记 RSORRES="PD" (as overall response). 不走 AE (除非 SAP 要求).
源: §14 + §18.2 场景 3

**Q: Target lesion 和 Non-target lesion 怎么区分?**
A: RECIST 1.1 规定: ≥1 个 "measurable" 病灶 (non-lymph node long-axis ≥10mm 或 lymph node short-axis ≥15mm) 可选为 target. TU.TUORRES="TARGET"/"NON-TARGET". Target 数量限制: 每器官 ≤2, 总 ≤5.
源: §14.2, RECIST 1.1 guideline

**Q: BOR (Best Overall Response) 在 SDTM 还是 ADaM?**
A: 通常 **ADaM (ADRS)**. SDTM RS 只存每 visit 的 OVRLRESP. 但 sponsor 可选择在 SDTM RS 记 RSTESTCD="BESTRESP" + RSDRVFL="Y" 作为 derived.
源: §14.5

### §23.2 Trial Design 场景

**Q: TS 的 TSPARMCD="INDIC" 多值怎么处理?**
A: 每 indication 一条 TS, 用 TSSEQ 递增 (1/2/3), 各 TSVAL 不同 (e.g., "ASTHMA" / "COPD"). 若有 ICD 或 SNOMED code 填 TSVALCD + TSVCDREF.
源: §12.1

**Q: TA 必须有吗?**
A: 几乎所有 interventional study 都**必须**有 TA (定义合法 arm). Observational 或 natural history study 可能无 TA, 但 FDA 强烈建议有.
源: §12.3

### §23.3 Timing / Visits 场景

**Q: eDiary 每日记录没有 VISIT, 如何规范?**
A: Findings 类变量的 VISITNUM 可以为空 (Core=Exp 但 Exp 不是 Req). 用 FTDTC/QSDTC 日期时间代替 Visit. 可自定义 EPOCH="DIARY PHASE" 分段.
源: §21.7

**Q: 超窗访视怎么记?**
A: SV (Subject Visits) 记实际日期. TV 记 plan. SV.SVSTDTC vs TV.VISITDY 比较找超窗. DV 域记 Deviations (DVTERM="Visit out of window").
源: §18.5

### §23.4 跨域关联场景

**Q: AE 由合并药 CM 引起, 数据怎么存?**
A: RELREC 2 条 (AE + CM, 同 RELID). 不用 SUPP--. **或者**: AE.AEACN="DRUG WITHDRAWN" + CM.CMREAS="AE-related" (若 CM 因 AE 停药) — 两种建模可共存.
源: §1.10 + §4.1

**Q: 多 milestone 的肿瘤随访, MIDS 怎么用?**
A: 先在 **TM** 定义 milestone (e.g., "FIRST PROGRESSION"), 然后在相关 observation class 域用 MIDS / MIDSTYPE 变量回指. MIDS 优于 RELREC (更标准化, ch04 §4.4.10).
源: §12.4 + §4.1

### §23.5 Controlled Terminology 场景

**Q: sponsor 自定义 codelist 会覆盖 CDISC CT 吗?**
A: 不会. Sponsor 若定义新 codelist 必须用 Define-XML 单独标注, 用自己的 CodelistID. CDISC CT 的 C-code (如 C66742) **专属** CDISC.
源: §9.7 + §2.7

**Q: extensible codelist 加 Term 的程序?**
A: Define-XML 里标 codelist.Extensible="Y" (若允许), 然后把 sponsor 新增的 Term 连同 Preferred Term 和 Submission Value 一起在 codelist.CodeListItem 中声明.
源: §9.7

---

## §24. 跨域反向变量索引 (业务提问视角)

### §24.1 "哪个变量记 X" 常问题反查

本节对"用户已知业务含义, 要找对应 SDTM 变量"的反向查询做聚合. 业务提问的典型模式"死亡原因填哪里" / "入排违反填哪里" / "受试者体重基线填哪里" 都靠此索引定位.

| 业务含义 | SDTM 变量 / 域 | 源 / 注意点 |
|---------|---------------|-----------|
| 受试者 ID | DM.USUBJID / 各域 USUBJID | DM 权威, 其他域引 |
| 首次给药日 | DM.RFSTDTC (Exp) 或 DM.RFXSTDTC (Perm, 若 RFSTDTC 不等于 first dose) | §1.13 |
| 年龄 / 年龄单位 | DM.AGE / DM.AGEU (C66781) | |
| 性别 | DM.SEX (Req, C66731 codelist) | |
| 种族 / 民族 | DM.RACE / DM.ETHNIC | 多 RACE 值 → SUPPDM (DM/assumptions §6) |
| **死亡日** | DM.DTHDTC (Exp, 若未知可估) | |
| **死亡标** | DM.DTHFL (Exp, "Y" 或 null, C66742) | §9.4 问 DTHDTC |
| 死亡原因 | 可能 AE (致死 AE AESDTH="Y") 或 DS (DSDECOD="DEATH") | 交叉核对 |
| 随机化分组 (planned) | DM.ARMCD / DM.ARM | §1.6 |
| 实际分组 | DM.ACTARMCD / DM.ACTARM (DM 域 Permissible slot, Core=Exp) | §1.6 + §1.26 |
| 不分组原因 | DM.ARMNRS (C142179 codelist) | §1.6 硬锚点 |
| 入排违反 | IE 域 (每违反一条) + TI 域 (定义) | §13 |
| 筛选失败 | IE (违反记录) + DS (DSDECOD="SCREENING FAILURE") + DM (ARMNRS="SCREEN FAILURE") | §13 + §18.4 |
| 研究完成 | DS (DSDECOD="COMPLETED") | §18.4 |
| 研究退出原因 | DS (DSDECOD="ADVERSE EVENT" / "WITHDRAWN BY SUBJECT" 等) | §18.4 |
| 合并用药 | CM 域, CMTRT (药名) + CMINDC (指征) | §1.1, §1.7 |
| 试验药物 | EX 域 (计划), EC 域 (实际采集) | §1.11 |
| 手术/操作 | PR 域 PRTRT | §16 |
| PET/造影/挑战 agent | AG 域 AGTRT | §15 |
| 病史 | MH 域 MHTERM | §1.7, §18.2 |
| AE 严重性 | AE.AESEV (Perm, 三档 MILD/MODERATE/SEVERE) | §1.2, §1.4 |
| AE 是否 SAE | AE.AESER (Exp, Y/N) + 6 Serious 子变量 | §1.2 |
| CTCAE Grade | AE.AETOXGR (Perm, 数字 1-5) 或 SUPPAE | §1.4 |
| Lab 超参考范围 | LB.LBNRIND (C78736 codelist) | §1.3 |
| PK 浓度 `<LLOQ` | PC.PCORRES="<LLOQ" + PCSTRESN=NULL | §1.5 |
| Vital Signs 血压 | VS 拆 SBP/DBP 两条 | §1.15a |
| ECG 心率 | EG.EGTESTCD="HR" / EGORRES | §1.15b |
| 试验 visit schedule | TV (plan) + SV (实际) | §12.5 + §18.5 |
| Milestone 事件 | TM (定义) + MIDS 变量 (关联) | §12.4 |
| 肿瘤识别 | TU 域, TUORRES="TARGET/NON-TARGET/NEW" | §14.2 |
| 肿瘤测量 | TR 域 TRTESTCD + TRSTRESN | §14.3 |
| 肿瘤响应 | RS 域 RSTESTCD + RSORRES (CR/PR/SD/PD/NE) | §14.4 |
| Best Overall Response | 通常 ADaM (ADRS); 可在 SDTM RS 用 RSDRVFL="Y" 标 | §14.5 |
| 方案偏离 | DV 域 DVTERM | §18.5 |
| Sponsor 自定义字段 | SUPP-- (per-domain) 或 SUPPQUAL (合并) | §19 |
| 跨域关联 | RELREC (RDOMAIN / IDVAR / RELID / RELTYPE) | §1.10, §4.1 |

### §24.2 EPOCH 跨域一致性

EPOCH 是 Timing 公用变量 (不带前缀), 任何 general observation class 域都能有, Core 通常 Perm. 一个 subject 的 AE/LB/CM 记录的 EPOCH 应当**与该时间点的 Epoch 定义一致** (由 TA/TE 派生). 常见值 (C99079 codelist, 具体 Term 查 NCI EVS): "SCREENING" / "TREATMENT" / "FOLLOW-UP" / "WASHOUT".

**跨域校验**: 同一 subject 同一日的 AE.EPOCH 应当 = LB.EPOCH = CM.EPOCH (若都在该日发生). 跨记录 EPOCH 不一致是数据质量问题.

### §24.3 MIDS 变量跨域扩散

MIDS (Milestone Identification) 变量族允许各 general observation class 域引用 TM 定义的 disease milestone. 典型变量:
- `--MIDS` (直接关联 Milestone, 域前缀)
- `--MIDSTYPE` (冗余, 确认 milestone 类型)
- `--RELMIDS` (事件相对 milestone 的时序, 如 "AT MILESTONE" / "BEFORE")

**业务意义**: 用 MIDS 代替 RELREC 做 "AE #5 发生在 first progression 那次" 这类关系, 避免 RELREC 膨胀, 数据更 queryable.

**源路径**:
- `knowledge_base/VARIABLE_INDEX.md` (全局变量反查权威)
- `knowledge_base/domains/TM/spec.md` + `knowledge_base/domains/SM/spec.md` (MIDS 三角关系的定义域 + 实例域)
- `knowledge_base/chapters/ch04_general_assumptions.md` §4.1.4.10 (EPOCH), §4.4.11 Disease Milestones (MIDS 跨域机制权威)

---

## §11. 变更记录

| 日期 | 变更 | 原因 |
|------|------|------|
| 2026-04-21 | 04 弹药包首版 (C 方案 Node 4) | 舍弃 terminology inline, 空余容量换业务问答完整覆盖 |
| 2026-04-21 | Node 5.1 扩容: §1.6 + §1.26 ACTARM/ACTARMCD 硬锚点 + 新增 §12-§21 段 (Trial Design / IE / RECIST Oncology / AG / PR / 影像场景跨域 / Events class / SUPPQUAL / 变量命名 checklist / EDC 专项) | smoke v2 Q6 错层回补 (CO-2 from reviewer) + 04 覆盖扩到 50-60K target (MED-1 reviewer 建议) |
| 2026-04-21 | Node 5.1 reviewer 闭合: §12.4 MIDS 三角关系补 SM 域 + §4.4.10→§4.4.11 章节号 修 2 处 (§12.4 + §24.3 源路径) + §22.7 UR Label 窄化修为 "Urinary System Findings" 广义尿系统发现域 | Gemini reviewer (security-reviewer 第 17 种) 独立 N=15 抽样发现 2 MED 事实偏差 (UR Label + MIDS/SM + §4.4.10 章节号), 主 session 内闭合以保 N5.1 0 carry-over |

---

*本文件是 Gemini Gems C 方案 Node 4 的核心业务问答弹药包. 任何业务场景题、规则判断题、EDC→SDTM 映射题、跨域鉴别题, 都优先查本文件对应 section, 回答后必附源路径 (CO-3 强制).*
