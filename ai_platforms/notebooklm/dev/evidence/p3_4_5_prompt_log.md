# P3.4.5 Raw Prompt & Answer Log

> **作用**: HC-4 可 replay 留档. Reviewer (HC-1) 审**本 log**, 不审 evidence 摘录.
> **HC-4 要求**: 每题**原始 prompt 字符串 + 完整 answer 全文**不 TLDR 落档.
> **HC-2 要求**: `Inline citation` 以**肉眼核 Chat UI 输出文本**为准 (形如 `[1]` `[08_ev_adverse_ae.md]`), 非 DOM panel Bucket ID.
> **HC-5 要求**: cowork / 主 session 初判记录于 evidence md, **终审**由第 10 种 subagent_type reviewer (HC-1).

**日期**: 2026-04-22
**Notebook**: `https://notebooklm.google.com/notebook/3f87a93e-9a65-407e-8292-c28706fc6287`
**Chat mode**: Custom (instructions.md 9,011 chars, P3.3 Save 后未动)
**抽样 log**: `dev/evidence/p3_4_5_sampling_log.md` (10 Req 变量 + seed)
**执行规则** (handoff §3.2):
- 每 3-4 题开新 chat session (避免 context 污染)
- Custom mode 保持激活全程
- 每题问完等答案完整 (poll 完成标记) 再下一题
- **严禁** 改题字, **严禁** 加 "请说明" / "请详述" 等 hint

---

## Session 1 — Q1..Q4

### Q1: BSSEQ (BS biospecimens) — T1 场景驱动

**Raw prompt** (原样未改字):
```
某临床研究需要记录受试者的生物样本采集 (biospecimens) 信息作为独立 SDTM 数据集. 按 SDTMIG 要求, BS 域除通用 identifiers (STUDYID / DOMAIN / USUBJID) 外, 哪些变量 Core=Req? 分别说明各变量的 Role (Identifier / Topic / Qualifier / Timing 等).
```

**Raw answer** (Chat UI 完整输出, 含 inline citation 标记):
```
在 SDTM 生物样本发现（Biospecimen Findings, BS）域中，除了通用的标识符 `STUDYID`、`DOMAIN` 和 `USUBJID` 之外，`Core` 为 `Req` (Required) 的变量共有 3 个，分别是 `BSSEQ`、`BSTESTCD` 和 `BSTEST` [42_req_variable_coverage_audit.md]。 

**Variables involved**:
| Variable | Type | Role | Core | CT | Source |
|----------|------|------|------|----|--------|
| BSSEQ | Num | Identifier | Req | | [19_fnd_morphology_bs_cp_cv.md] |
| BSTESTCD | Char | Topic | Req | C124300 | [19_fnd_morphology_bs_cp_cv.md] |
| BSTEST | Char | Synonym Qualifier | Req | C124299 | [19_fnd_morphology_bs_cp_cv.md] |

这 3 个 `Req` 变量的具体职责（Role）和用途如下：

*   **BSSEQ (Sequence Number)**：角色为 **Identifier**。用于确保每个受试者在 BS 数据集内的数据记录具有唯一性的序列号 [19_fnd_morphology_bs_cp_cv.md]。
*   **BSTESTCD (Biospecimen Test Short Name)**：角色为 **Topic**。是测量、测试或检查的短名称（不得超过8个字符），决定了该条记录的核心观测主题，例如 "VOLUME" 或 "RIN" [19_fnd_morphology_bs_cp_cv.md]。
*   **BSTEST (Biospecimen Test Name)**：角色为 **Synonym Qualifier**。是测试或检查的完整名称（逐字名称），用于对 `BSTESTCD` 提供具体的同义词限定说明，例如 "Volume" 或 "RNA Integrity Number" [19_fnd_morphology_bs_cp_cv.md]。

**Codelist**: 
*   **C124300** (Biospecimen Characteristics Test Code) — 适用于 `BSTESTCD` [19_fnd_morphology_bs_cp_cv.md, 37_ct_misc_int_dm_sp_td_gf_oi_other.md]
*   **C124299** (Biospecimen Characteristics Test Name) — 适用于 `BSTEST` [19_fnd_morphology_bs_cp_cv.md]
```

**Inline citation count** (HC-2): `8 个 inline markers; 3 unique buckets: [19_fnd_morphology_bs_cp_cv.md]×6, [42_req_variable_coverage_audit.md]×1, [37_ct_misc_int_dm_sp_td_gf_oi_other.md]×1`
**DOM panel Bucket IDs** (辅助核对): N/A (用户未 DOM 辅助)
**F-1 漂移**: `YES (Variables involved 小表 single-line malformed)`
**主判分**: **1.0** (内容 + 多源 citation 精确)

---

### Q2: SRTESTCD (SR skin response) — T2 CT 绑定

**Raw prompt** (原样未改字):
```
SDTM SR (Skin Response) 域中, SRTESTCD 变量绑定哪个 controlled terminology codelist? 对应的 C-code 是多少? 列出 2 个典型 test short code 举例 (如皮肤刺激 / 过敏 / 红斑水肿相关检测).
```

**Raw answer**:
```
在 SDTM Skin Response (SR) 域中，变量 `SRTESTCD` (Skin Response Test or Exam Short Name) 绑定的受控术语 (Controlled Terminology) 列表名称为 **Skin Response Test Code**，其对应的 C-code 是 **C112024**。

根据该受控术语字典，典型的与皮肤刺激、过敏或红斑/风团水肿相关的检测短代码（Test Short Code）举例如下：
1. **`FLRMDIAM`** (Flare Mean Diameter)：用于表示皮肤抗原激发部位周围形成的红斑（Flare）区域的平均直径。
2. **`WHEALSZ`** (Wheal Size)：用于半定量评估皮肤抗原激发部位周围形成的扁平、圆形、微凸起区域（风团/Wheal，即水肿反应）的大小。

*(其他常见的相关短代码还包括 **`REACTGR`** (Reaction Grade，反应等级) 以及 **`ASRINT`** (Allergen Skin Response Intensity，过敏原皮肤反应强度)。)*

**Variables involved**:
| Variable | Type | Role | Core | CT | Source |
|----------|------|------|------|----|--------|
| SRTESTCD | Char | Topic | Req | C112024 | |

**Codelist**: **C112024** - Skin Response Test Code
```

**Inline citation count** (HC-2): `0 inline markers — 答案仅在 prose 中提及 C112024, 无任何 [bucketN_xxx.md] 标记`
**DOM panel Bucket IDs** (辅助核对): N/A
**F-1 漂移**: `YES (Variables involved 单行小表 single-line malformed) + **HC-2 违规 (inline citation 完全缺失)**`
**主判分**: **0.5** (内容 PASS; inline citation 违规 -0.5)

---

### Q3: CPTEST (CP clinical endpoint) — T3 跨域一致性

**Raw prompt** (原样未改字):
```
CP (Clinical Endpoint) 域的 CPTEST 变量 Role 是什么? Core 属性是? 它与其他 Findings 域的 --TEST 变量 (如 LBTEST / VSTEST / EGTEST) 在 Role 和 Core 属性上是否一致? CPTEST 使用的 codelist 是 CP 域专属还是跨域共享?
```

**Raw answer**:
```
首先需要澄清一个 SDTM 术语细节：在 SDTM 标准中，**CP 域代表“细胞表型发现” (Cell Phenotype Findings)** [33_ct_general.md]，而不是 Clinical Endpoint（通常临床事件记录在 CE - Clinical Events 域）。基于您提到的 `CPTEST` 变量，以下是针对 CP 域的详细解答：

在 CP (Cell Phenotype Findings) 域中，`CPTEST` 的 **Role 是 Synonym Qualifier**，**Core 属性是 Req** [19_fnd_morphology_bs_cp_cv.md]。

**Variables involved**:
| Variable | Type | Role | Core | CT | Source |
|----------|------|------|------|----|--------|
| CPTEST | Char | Synonym Qualifier | Req | C181174 | [19_fnd_morphology_bs_cp_cv.md] |
| LBTEST | Char | Synonym Qualifier | Req | C67154 | [11_fnd_lab_lb.md] |
| VSTEST | Char | Synonym Qualifier | Req | C67153 | [12_fnd_vitals_vs_eg.md] |
| EGTEST | Char | Synonym Qualifier | Req | C71152; C120524 | [12_fnd_vitals_vs_eg.md] |

### 1. 与其他 Findings 域的属性一致性
`CPTEST` 与其他 Findings 发现类域（如 `LBTEST`、`VSTEST`、`EGTEST` 等）在 Role 和 Core 属性上**完全一致**。根据 SDTM Findings 通用观察类模型架构，所有的 `--TEST` 变量（即测量、测试或检查的逐字全称）都固定被定义为对 `--TESTCD` 的 **Synonym Qualifier**，并且其 Core 级别在所有 Findings 域中均强制为 **Req** [31_model_obs_classes.md]。

### 2. 受控术语 (Controlled Terminology) 的专属与共享属性
`CPTEST` 使用的 Codelist 是 **C181174** (Cell Phenotyping Test Name) [19_fnd_morphology_bs_cp_cv.md, 36_ct_specialized_micro_oncology_pk_is_cp.md]。
这是一个 **CP 域专属**的受控术语集，而非跨域共享。作为对比：
*   LB 域的 `LBTEST` 使用其专属的 C67154 (Laboratory Test Name) [11_fnd_lab_lb.md, 34_ct_lb.md]。
*   VS 域的 `VSTEST` 使用其专属的 C67153 (Vital Signs Test Name) [12_fnd_vitals_vs_eg.md]。
（注意：Findings 域的测量项目本身高度专业化，因此它们的 `--TEST` 和 `--TESTCD` 字典几乎都是按域独立维护的。）
```

**Inline citation count** (HC-2): `11 markers; 7 unique buckets: [33_ct_general.md], [19_fnd_morphology_bs_cp_cv.md]×3, [31_model_obs_classes.md], [11_fnd_lab_lb.md]×2, [12_fnd_vitals_vs_eg.md]×2, [34_ct_lb.md], [36_ct_specialized_micro_oncology_pk_is_cp.md]`
**DOM panel Bucket IDs**: N/A
**F-1 漂移**: `YES (Variables involved 4 行小表 single-line malformed)`
**主判分**: **1.0** (内容 + 跨域一致性论证 + 域名纠错 + 多源 citation 精确)

---

### Q4: QSTEST (QS questionnaires) — T2 CT 绑定 + **HC-3 trigger**

**Raw prompt** (原样未改字):
```
QS (Questionnaires) 域中 QSTEST 变量作用是什么? 它和 QSTESTCD (Topic) 的关系是? 在典型问卷数据记录中 (如 EORTC QLQ-C30 或 SF-36 或 ECOG performance status), QSTEST / QSTESTCD 具体填什么? 请举 1 个 QSTEST / QSTESTCD 的实际键值对例, 并说明对应的 codelist 出处.
```

**Raw answer**:
```
在 QS (Questionnaires) 域中，`QSTEST` 的主要作用是记录用于获取测量结果或发现的问卷问题（或问题组）的逐字全称（Verbatim name of the question）。

### QSTEST 与 QSTESTCD 的关系
`QSTESTCD` 是 QS 域的核心观测主题（Topic），而 `QSTEST` 是对 `QSTESTCD` 的**同义词限定说明（Synonym Qualifier）**，两者的 Core 属性均为强制必填（**Req**）。
*   **QSTESTCD (Question Short Name)**：长度不能超过 8 个字符，且不能以数字开头，主要用于在将数据集从垂直结构转换为水平结构时作为列名使用。
*   **QSTEST (Question Name)**：是具体问题的详细名称或描述，长度限制为不超过 40 个字符。对于标准化问卷（如 EORTC QLQ-C30 或 SF-36），这两个变量必须严格遵循 CDISC 控制术语 (Controlled Terminology) 中为各特定问卷独立发布的专属受控字典。

**Variables involved**:
| Variable | Type | Role | Core | CT | Source |
|----------|------|------|------|----|--------|
| QSTESTCD | Char | Topic | Req | 各问卷专属字典 | [14_fnd_questionnaire_qs_ie.md] |
| QSTEST | Char | Synonym Qualifier | Req | 各问卷专属字典 | [14_fnd_questionnaire_qs_ie.md] |

---

### 典型问卷数据记录的填写与实际键值对示例

在记录标准问卷（如 EORTC QLQ-C30）时，`QSTESTCD` 填入代表该特定问题的系统化短码，`QSTEST` 填入该短码映射的标准问题缩略描述。

**实际键值对示例（以 EORTC QLQ-C30 V3.0 为例）**：
*   **`QSTESTCD`** = **`EOR0101`** 
*   **`QSTEST`** = **`EOR01-Trouble Doing Strenuous Activities`** （原问题含义：你做剧烈活动有困难吗，比如提沉重的购物袋或手提箱？）

**对应的 Codelist 出处**：
此键值对来源于 CDISC 为该问卷专门设立的独立字典集合：
*   `QSTESTCD` 绑定 C-code: **C161619** (European Organisation for the Research and Treatment of Cancer Quality of Life Questionnaire - Core 30 Version 3.0 Questionnaire Test Code)。
*   `QSTEST` 绑定 C-code: **C161618** (European Organisation for the Research and Treatment of Cancer Quality of Life Questionnaire - Core 30 Version 3.0 Questionnaire Test Name)。

*(注：如 SF-36 或 ECOG 等其他工具也遵循完全相同的逻辑，例如 SF-36 Standard V1.0 的 `QSTESTCD` 为 `SF36101`，其对应的 `QSTEST` 为 `SF361-In General You Say Your Health Is`。)*

```

**Inline citation count** (HC-2): `2 markers (仅在 Variables table 内 [14_fnd_questionnaire_qs_ie.md]×2); Narrative 段提了具体 C161619/C161618 (EORTC QLQ-C30 V3.0 专属字典 C-code) 但**未 inline cite 到 bucket 38/39** — RAG 策略问题, 非 indexing 问题 (HC-3 补 A 证实 bucket 38 indexing OK)`
**DOM panel Bucket IDs**: N/A
**F-1 漂移**: `YES (Variables involved 2 行小表 single-line malformed)`
**HC-3 触发检查**: `NO (Q4 实际 inline citation 未命中 38/39)` — **但按 handoff §1.1 约束 (抽到 QS/FA + 预期 38/39) HC-3 仍强制 trigger 补题 A/B**
**主判分**: **0.75** (内容 + EORTC 具体 C-code 精准; 但 inline citation 缺失 bucket 38/39 -0.25)

---

## Session 2 — Q5..Q7

### Q5: FATESTCD (FA findings about) — T2 CT 绑定 + 场景融合

**Raw prompt** (原样未改字):
```
FA (Findings About) 域的 FATESTCD 变量绑定哪个 controlled terminology codelist? 对应的 C-code 是? FATESTCD 与 FAOBJ 在一条 FA 记录里各自填什么? 请以"记录某受试者某次不良事件的严重程度评估"为业务场景, 举一条 FA 记录说明 FAOBJ / FATESTCD / FAORRES 的值各填什么.
```

**Raw answer**:
```
在 SDTM Findings About (FA) 域中，关于 `FATESTCD` 与 `FAOBJ` 的受控术语及使用分工如下：

### 1. FATESTCD 的受控术语与 C-code
`FATESTCD` 变量绑定的受控术语 (Controlled Terminology) 字典名称为 **Findings About Test Code**，其对应的 C-code 是 **C101832**。
*(注：根据具体治疗领域，有时也会使用特定的治疗领域专属受控字典，但 C101832 是其通用的基础字典。)*

### 2. FATESTCD 与 FAOBJ 的数据分工
在 FA 域中，这两个变量都是强制必填的 (`Core: Req`)，它们相互配合以完整描述“对某事物的某项观察”：
*   **`FAOBJ` (Object of the Observation)**：角色为 **Record Qualifier**。它用于记录该发现或观察的**核心对象/焦点**（即被评估的“客体”），通常是具体症状、不良事件或干预措施的名称（例如 "Nausea" 或 "Injection Site Rash"）。
*   **`FATESTCD` (Findings About Test Short Name)**：角色为 **Topic**。它用于记录针对上述核心对象所进行的**特定测试、测量或检查项目的短名称**（例如严重程度、发生与否、体积等，短码如 "SEV"、"OCCUR"）。

**Variables involved**:
| Variable | Type | Role | Core | CT | Source |
|----------|------|------|------|----|--------|
| FATESTCD | Char | Topic | Req | C101832 | |
| FAOBJ | Char | Record Qualifier | Req | | |
| FAORRES | Char | Result Qualifier | Exp | | |

### 3. 业务场景示例：记录某次不良事件的严重程度评估
**场景说明**：在某临床试验中，受试者报告了不良事件“恶心”(Nausea)。在特定的访视时间点，研究者需要专门记录该次“恶心”症状在当时的严重程度（Severity）。在 FA 域中，这条数据记录的核心键值对如下填写：

*   **`FAOBJ`** = **`Nausea`** （明确观察对象是“恶心”这一不良事件。通常建议填入与 AE 域中 `AEDECOD` 相同的标准字典词）
*   **`FATESTCD`** = **`SEV`** （明确针对该对象评估的测试维度是“严重程度/Severity”）
*   **`FAORRES`** = **`MODERATE`** （填入实际的原始评估结果，如 `MILD`、`MODERATE` 或 `SEVERE`）

通过这种方式，FA 域能够精准地将事件 (Nausea) 与其特定时间点的横截面属性 (Severity = Moderate) 关联起来，而不会与 AE 域中代表整个事件全局最高严重程度的 `AESEV` 混淆。
```

**Inline citation count** (HC-2): `0 inline markers — 答案 prose 列出 C101832 / FAOBJ / FATESTCD / FAORRES 和业务场景 (Nausea/SEV/MODERATE) 但**完全无 [bucketN_xxx.md] 标记**`
**DOM panel Bucket IDs**: N/A
**F-1 漂移**: `YES (Variables involved 3 行小表 + Source 列空白 single-line malformed) + **HC-2 违规 (inline citation 完全缺失)**`
**主判分**: **0.5** (内容 PASS + AESEV 边界论证好; inline citation 违规 -0.5)

---

### Q6: SESTDTC (SE subject elements) — T2 CT 绑定 + IG ch04 Timing 规则

**Raw prompt** (原样未改字):
```
SE (Subject Elements) 域的 SESTDTC 变量属于哪一类 Role? 数据格式要求是什么标准? 按 SDTMIG ch04 对 Timing 变量的通用规则, 该变量的值必须使用哪种格式? 请给一个符合规范的 SESTDTC 取值示例, 并说明缺失值 (如只知日期无时间) 时应如何填.
```

**Raw answer**:
```
在 SE (Subject Elements) 域中，关于 `SESTDTC` (Start Date/Time of Element) 变量的具体规范如下：

**Variables involved**:
| Variable | Type | Role | Core | CT | Source |
|----------|------|------|------|----|--------|
| SESTDTC | Char | Timing | Req | ISO 8601 datetime or interval | [04_sp_se_sm_sv_co.md] |

**1. Role 与数据格式标准**
*   **Role**: `SESTDTC` 属于 **Timing** 变量 [04_sp_se_sm_sv_co.md]。
*   **格式标准**: 数据必须遵循 **ISO 8601 datetime or interval** 标准的字符型 (Char) 格式 [04_sp_se_sm_sv_co.md]。

**2. SDTMIG ch04 规定的具体格式**
根据 SDTMIG 第4章对 Timing 变量的通用要求，日期和时间必须使用 ISO 8601 的 **extended format (扩展格式)** [29_ig_ch04_general_assumptions.md]。这意味着：
*   日期部分必须使用连字符 (`-`) 作为分隔符，时间部分必须使用冒号 (`:`) 作为分隔符 [29_ig_ch04_general_assumptions.md]。
*   当日期和时间记录在同一个变量中时，必须以大写字母 `T` 作为分隔符连接 (即 `YYYY-MM-DDThh:mm:ss`)，且**绝对不允许包含空格** [29_ig_ch04_general_assumptions.md]。

**3. 合规示例**
*   **完整日期与时间**: `2006-06-01T13:14:17` [29_ig_ch04_general_assumptions.md]
*   **仅日期**: `2006-06-01` [04_sp_se_sm_sv_co.md, 29_ig_ch04_general_assumptions.md]

**4. 缺失值 (如只知日期无时间) 的填报规则**
*   **缺失处理 (Truncation)**：根据 ISO 8601 规范，如果数据收集精度降低或部分数据缺失（例如只知日期不知时间），应从右侧直接截断缺失的层级。如果完全没有时间部分，则必须省略时间指示符 `T`，直接填报为 `YYYY-MM-DD`（例如 `2006-06-01`） [29_ig_ch04_general_assumptions.md]。
*   **边界说明**：`SESTDTC` 在 SE 域中的 Core 为 **Req** (强制必填)。SDTMIG 的业务假设明确指出：由于 SE 记录的是受试者实际经历的阶段，只要受试者进入了某一个 Element，就必须提供它的起始信息，因此 **`SESTDTC` 绝不能为 null**，尽管它允许是不精确的收集值（如截断到日、月或年） [04_sp_se_sm_sv_co.md]。
```

**Inline citation count** (HC-2): `9 markers; 2 unique buckets: [04_sp_se_sm_sv_co.md]×4, [29_ig_ch04_general_assumptions.md]×5 (精确双锚: SE spec + IG ch04 Timing 规则)`
**DOM panel Bucket IDs**: N/A
**F-1 漂移**: `可能 (Variables involved 1 行小表); Narrative 段 rule 列表 render 无异常`
**主判分**: **1.0** (内容 + 双源精确 + ISO 8601 extended + 截断规则 + SE 不能 null 边界)

**Raw prompt** (原样未改字):
```
DM (Demographics) 域的 SEX 变量绑定哪个 controlled terminology codelist? C-code 是多少? 允许值列表有哪些? 按 IG ch04 demographics 相关规则, 当 SEX 信息未知或缺失时应如何处理 (填 UNKNOWN 还是留空)?
```

**Raw answer**:
```
在 DM (Demographics) 域中，变量 `SEX` 绑定的受控术语 (Controlled Terminology) 字典名称为 **Sex**，其对应的 C-code 是 **C66731** [03_sp_demographics_subject.md]。

根据该受控术语字典，`SEX` 允许填入的标准化值（Submission Values）共有以下 4 个：
*   **`F`** (Female)
*   **`M`** (Male)
*   **`U`** (Unknown - 指未知、未观察到、未记录或拒绝提供)
*   **`UNDIFFERENTIATED`** (指性别未分化或兼具两性特征)
[37_ct_misc_int_dm_sp_td_gf_oi_other.md]

### 未知或缺失时的处理规则
根据 SDTMIG 第 4 章的一般规则（General Assumptions），`SEX` 在 DM 域中的 Core 属性为 **Req**（强制必填），这意味着该变量在任何数据行中**绝对不能留空（cannot be null for any record）** [29_ig_ch04_general_assumptions.md]。因此，当性别信息未知或缺失时，不能留空，必须填入受控术语中指定的 **`U`** [37_ct_misc_int_dm_sp_td_gf_oi_other.md]。

**Variables involved**:
| Variable | Type | Role | Core | CT | Source |
|----------|------|------|------|----|--------|
| SEX | Char | Record Qualifier | Req | C66731 | [03_sp_demographics_subject.md] |

**Codelist**: **C66731** - Sex [37_ct_misc_int_dm_sp_td_gf_oi_other.md]

**Boundary note**: `SEX` 变量不使用 `UNKNOWN` 这个完整单词，必须严格使用受控术语规定的单字母短码 `U`。
```

**Inline citation count** (HC-2): `5 markers; 3 unique buckets: [03_sp_demographics_subject.md]×2, [37_ct_misc_int_dm_sp_td_gf_oi_other.md]×2, [29_ig_ch04_general_assumptions.md]×1 (精确: DM spec + DM CT + IG ch04)`
**DOM panel Bucket IDs**: N/A
**F-1 漂移**: `可能 (Variables involved 1 行小表)`
**主判分**: **1.0** (内容 + 4 允许值 + U 非 null + Core=Req 边界 + 多源 citation)

---

## Session 3 — Q8..Q10

### Q8: REFID (RELSPEC specimen relationships) — T1 场景驱动 + T3 跨变量协作

**Raw prompt** (原样未改字):
```
某研究需要记录生物样本的谱系关系 (specimen-to-specimen relationships), 使用 SDTM RELSPEC 域. RELSPEC 域中 REFID 变量的 Role 和用途是什么? 它与 RDOMAIN / RSUBJID / LEVEL 等变量在 RELSPEC 数据集里如何组合表达 "某母样本拆分为若干子样本" 的层级关系? 举一条最简 RELSPEC 记录示意.
```

**Raw answer**:
```
在 SDTM RELSPEC (Related Specimens) 域中，`REFID` 的角色（Role）为 **Identifier**，Core 属性为 **Req** [26_rel_relrec_relspec_relsub.md]。它的用途是作为样本标识符（Specimen ID），在同一个 `USUBJID` 内必须具有唯一性，用于精准标识参与谱系/层级关系的具体生物样本 [26_rel_relrec_relspec_relsub.md]。

### 关于变量组合与层级关系的澄清

首先需要纠正您问题中的一个前提：**RELSPEC 数据集中绝对不包含 `RDOMAIN` 和 `RSUBJID` 这两个变量** [26_rel_relrec_relspec_relsub.md]。 
*   `RDOMAIN` 是用于 `RELREC`、`SUPPQUAL` 和 `CO` 域的关系锚点变量。
*   `RSUBJID` 是专门用于 `RELSUB`（Related Subjects，记录受试者间关系如亲属、双胞胎等）域的变量 [26_rel_relrec_relspec_relsub.md]。

在 RELSPEC 中，表达“母样本拆分/衍生为若干子样本”的谱系层级关系（Genealogy），是完全通过 **`REFID`、`PARENT` 和 `LEVEL`** 这三个专属变量的组合来实现的 [26_rel_relrec_relspec_relsub.md]：

1.  **初代母样本**：最初直接从人体采集的样本被视为第一代（First generation），其 `LEVEL` 必须设为 `1`，且它的 `PARENT` 变量留空（Null） [26_rel_relrec_relspec_relsub.md]。
2.  **衍生的子样本**：当母样本被拆分（Aliquoted）或提取处理成子样本时，每个子样本都会获得一个新的、专属的 `REFID`。此时，子样本的 `PARENT` 变量会填入其对应母样本的 `REFID` 值，同时其 `LEVEL` 变量会递增为 `2`（如果是从第二代再次拆分，则子样本的 `LEVEL` 变为 `3`，以此类推） [26_rel_relrec_relspec_relsub.md]。

**Variables involved in RELSPEC**:
| Variable | Type | Role | Core | CT | Source |
|----------|------|------|------|----|--------|
| STUDYID | Char | Identifier | Req | | [26_rel_relrec_relspec_relsub.md] |
| USUBJID | Char | Identifier | Req | | [26_rel_relrec_relspec_relsub.md] |
| REFID | Char | Identifier | Req | | [26_rel_relrec_relspec_relsub.md] |
| SPEC | Char | Variable Qualifier | Perm | C78734; C111114 | [26_rel_relrec_relspec_relsub.md] |
| PARENT | Char | Identifier | Exp | | [26_rel_relrec_relspec_relsub.md] |
| LEVEL | Num | Variable Qualifier | Req | | [26_rel_relrec_relspec_relsub.md] |

---

### 最简 RELSPEC 记录示意

以下记录摘自 SDTMIG 官方示例，展示了受试者 `001-01` 的原始组织样本（`SPC-001`，母样本）被拆分为两个子样本（`SPC-001-A` 和 `SPC-001-B`）的追踪过程 [26_rel_relrec_relspec_relsub.md]。

| Row | STUDYID | USUBJID | REFID | SPEC | PARENT | LEVEL |
|---|---|---|---|---|---|---|
| 1 | ABC-123 | 001-01 | SPC-001 | TISSUE | | 1 |
| 2 | ABC-123 | 001-01 | SPC-001-A | TISSUE | SPC-001 | 2 |
| 3 | ABC-123 | 001-01 | SPC-001-B | TISSUE | SPC-001 | 2 |

**Boundary note**: RELSPEC 域是专门为维护生物样本自身血统/谱系而设计的特殊关系域，它不需要依赖 `RELREC` 数据集来进行样本间的关联管理 [26_rel_relrec_relspec_relsub.md]。
```

**Inline citation count** (HC-2): `~10 markers, 1 unique bucket: [26_rel_relrec_relspec_relsub.md] (单源但精确 — RELSPEC 域专属 bucket)`
**DOM panel Bucket IDs**: N/A
**F-1 漂移**: `部分 (Variables involved 6 行表 + 示例 4 行表 render 情况不确定)`
**主判分**: **1.0** (内容 + **用户 prompt 前提纠错** RDOMAIN/RSUBJID 不在 RELSPEC + REFID/PARENT/LEVEL 三件套 + 官方示例表)

---

### Q9: TSPARM (TS trial summary) — T2 CT 绑定

**Raw prompt** (原样未改字):
```
TS (Trial Summary) 域的 TSPARM 变量对应哪个 controlled terminology codelist? 对应的 C-code 是多少? TSPARM 和 TSPARMCD 在 Role 和填写内容上的分工是什么? 请列举 2-3 个典型 trial summary parameter (如适应症 / 研究分期 / 主要目标 / 试验期数) 对应的 TSPARMCD 短代码.
```

**Raw answer**:
```
在 TS (Trial Summary) 域中，`TSPARM` 变量绑定的受控术语字典（Codelist）名称为 **Trial Summary Parameter Test Name**，对应的 C-code 是 **C67152** [25_td_meta_ti_ts_oi.md, 37_ct_misc_int_dm_sp_td_gf_oi_other.md]。

**Variables involved**:
| Variable | Type | Role | Core | CT | Source |
|----------|------|------|------|----|--------|
| TSPARMCD | Char | Topic | Req | C66738 | [25_td_meta_ti_ts_oi.md] |
| TSPARM | Char | Synonym Qualifier | Req | C67152 | [25_td_meta_ti_ts_oi.md] |

### TSPARM 与 TSPARMCD 的分工
两者在结构上配对使用，Core 属性均被强制要求为 **Req**，但它们的职责（Role）和字符规范截然不同 [25_td_meta_ti_ts_oi.md, 42_req_variable_coverage_audit.md]：

*   **TSPARMCD (Trial Summary Parameter Short Name)**：
    *   **Role**: **Topic** [25_td_meta_ti_ts_oi.md]。
    *   **分工**: 作为 TS 记录的核心观测主题，它是系统化的短代码。长度被严格限制在 8 个字符以内，主要用于在数据处理和编程时提供简便、标准的键值（Key）识别 [25_td_meta_ti_ts_oi.md]。其绑定的字典 C-code 为 **C66738** (Trial Summary Parameter Test Code) [25_td_meta_ti_ts_oi.md]。
*   **TSPARM (Trial Summary Parameter Name)**：
    *   **Role**: **Synonym Qualifier** [25_td_meta_ti_ts_oi.md]。
    *   **分工**: 作为对 `TSPARMCD` 的同义词限定说明，它提供人类可读的参数全称或描述。其长度限制为 40 个字符以内（例如 "Planned Minimum Age of Subjects"） [25_td_meta_ti_ts_oi.md]。

### 典型的 Trial Summary Parameter 短代码 (TSPARMCD) 示例
根据 CDISC Controlled Terminology 规范，以下为常见的临床试验特征参数短代码举例：

1.  **适应症 (Indication)** 
    *   TSPARMCD: **`INDIC`** 
    *   TSPARM: Trial Disease/Condition Indication [25_td_meta_ti_ts_oi.md, 37_ct_misc_int_dm_sp_td_gf_oi_other.md]
2.  **研究分期 (Trial Phase)**
    *   TSPARMCD: **`TPHASE`** 
    *   TSPARM: Trial Phase Classification [25_td_meta_ti_ts_oi.md, 37_ct_misc_int_dm_sp_td_gf_oi_other.md]
3.  **主要目标 (Primary Objective)**
    *   TSPARMCD: **`OBJPRIM`** 
    *   TSPARM: Trial Primary Objective [25_td_meta_ti_ts_oi.md, 37_ct_misc_int_dm_sp_td_gf_oi_other.md]
4.  **计划的组别/试验臂数量 (Number of Arms)**
    *   TSPARMCD: **`NARMS`** 
    *   TSPARM: Planned Number of Arms [25_td_meta_ti_ts_oi.md, 37_ct_misc_int_dm_sp_td_gf_oi_other.md]
```

**Inline citation count** (HC-2): `12 markers; 3 unique buckets: [25_td_meta_ti_ts_oi.md]×7, [37_ct_misc_int_dm_sp_td_gf_oi_other.md]×4, [42_req_variable_coverage_audit.md]×1 (精确三源: TS spec + TD CT + 覆盖审计)`
**DOM panel Bucket IDs**: N/A
**F-1 漂移**: `YES (Variables involved 2 行小表 single-line malformed)`
**主判分**: **1.0** (内容 + C67152/C66738 + Role 分工 + 4 典型 TSPARMCD INDIC/TPHASE/OBJPRIM/NARMS 全对)

---

### Q10: BETERM (BE biospecimen events) — T3 跨域一致性 + 边界

**Raw prompt** (原样未改字):
```
BE (Biospecimen Events) 域专门记录什么类型的数据? BETERM 变量的 Core 和 Role 分别是? BETERM 与 AE 域的 AETERM 以及 MH 域的 MHTERM 在 Role 和 Core 属性上是否一致? BE 域与 AE / MH 在数据记录边界上如何界定 (即某个事件应归 BE / AE / MH 中的哪一个)?
```

**Raw answer**:
```
在 SDTM 中，**BE (Biospecimen Events)** 域专门用于记录那些影响或可能影响**生物样本 (biospecimen)**的操作与事件，例如样本的采集 (collection)、冷冻 (freezing) 与解冻 (thawing)、分装 (aliquoting) 以及运输 (transportation)。该域适用于任何形式的样本追踪数据，无论最初采集该样本的临床原因为何 [10_ev_history_mh_ho_be.md]。

关于 `BETERM` 变量，它的 `Role` 是 **Topic**，`Core` 属性是 **Req** [10_ev_history_mh_ho_be.md]。

`BETERM` 与 AE 域的 `AETERM` 以及 MH 域的 `MHTERM` 在 `Role` 和 `Core` 属性上是**完全一致**的。根据 SDTM 事件类 (Events) 观察模型的基础架构，这三个变量都是各自数据集的核心观测主题（Topic），且被强制要求必填（Req）[31_model_obs_classes.md, 42_req_variable_coverage_audit.md]。

**Variables involved**:
| Variable | Type | Role | Core | CT | Source |
|----------|------|------|------|----|--------|
| BETERM | Char | Topic | Req | | [10_ev_history_mh_ho_be.md] |
| AETERM | Char | Topic | Req | | [08_ev_adverse_ae.md] |
| MHTERM | Char | Topic | Req | | [10_ev_history_mh_ho_be.md] |

---

**Boundary note (数据记录边界界定)**:
在判断某个事件应归入 BE、AE 还是 MH 域时，核心界定标准在于**事件的作用对象（受试者 vs. 样本）**以及**医学事件发生的时间线（试验前 vs. 试验中）**：

| 域 | 作用对象与核心性质 | 典型场景示例 | Source |
|---|---|---|---|
| **BE** (Biospecimen Events) | **作用于离体生物样本的操作行为**。不涉及受试者自身的临床医学症状，而是专门记录脱离人体后（包括采集过程）样本的物流与处理生命周期。 | 样本的采集 (Collecting)、冷冻 (Flash Freezing)、分装 (Aliquoting)、运输 (Shipping) | [10_ev_history_mh_ho_be.md, 36_ct_specialized_micro_oncology_pk_is_cp.md] |
| **AE** (Adverse Events) | **作用于受试者的不良医学事件**。受试者在参与临床研究期间（通常为知情同意或首次给药后）发生的任何不良的医疗事件 (untoward medical occurrence)，无论其是否与研究药物有因果关系。 | 试验期间受试者报告的头痛 (Headache)、恶心 (Nausea) 或意外骨折 | [08_ev_adverse_ae.md, 33_ct_general.md] |
| **MH** (Medical History) | **作用于受试者的既往医学事件或状况**。受试者在临床试验开始（入组/基线）之前就已经发生或存在的疾病史、手术史等临床状况。 | 试验前就确诊的 2型糖尿病、既往的手术史或陈旧性骨折 | [10_ev_history_mh_ho_be.md, 33_ct_general.md] |

总结而言：如果事件描述的是“对一管血/一块组织做了什么处理”，归 **BE**；如果事件描述的是“受试者生了什么病/出现了什么症状”，根据其发生于试验期间还是试验前，分别归入 **AE** 或 **MH** [08_ev_adverse_ae.md, 10_ev_history_mh_ho_be.md]。
```

**Inline citation count** (HC-2): `11 markers; 6 unique buckets: [10_ev_history_mh_ho_be.md]×4, [31_model_obs_classes.md]×1, [42_req_variable_coverage_audit.md]×1, [08_ev_adverse_ae.md]×2, [33_ct_general.md]×2, [36_ct_specialized_micro_oncology_pk_is_cp.md]×1 (多源精确: BE spec + model + AE + CT)`
**DOM panel Bucket IDs**: N/A
**F-1 漂移**: `MIXED — Variables involved 3 行小表 FAIL (single-line malformed), Boundary note 3 行跨域大表 **RENDER 成功** (用户明证) — F-1 非单一 "bug/fix", 列数+密度+空 cell 综合归因`
**主判分**: **1.0** (内容 + BE/AE/MH 边界 (对象 vs 时间线) + 一致性 Topic+Req + 多源 citation)

---

## HC-3 补题 (条件触发: Q4 citation 命中 bucket 38/39)

### 补题 A: bucket 38 **头段** codelist 定位验证

**Raw prompt** (待 Q4 结果确认后填):
```
SDTM QS 域用于记录 CDR (Clinical Dementia Rating Scale) 评估时, QSCAT 应填什么? QSTESTCD 的典型编码样式是什么 (举 1-2 个 QSTESTCD / QSTEST 键值对)? 对应的 CDISC questionnaire controlled terminology codelist 名称和 C-code 是多少?
```

**Raw answer**:
```
在 SDTM QS（Questionnaires）域中记录 Clinical Dementia Rating (CDR) 评估时，各字段的填报规则和受控术语（Controlled Terminology）如下：

**1. QSCAT（问卷类别）应填入的值：**
`QSCAT` 应填入标准值 **`CDR`** [35_ct_findings_eg_qs_vs_mi_ae_dispo.md]。在 QRS 命名规则中，`QSCAT` 用于表明该问题所属的问卷名称，此值对应问卷类别（Category of Question, C-code: `C100129`）中的 Clinical Dementia Rating 受控术语（Term C-code: `C102114`）[14_fnd_questionnaire_qs_ie.md, 35_ct_findings_eg_qs_vs_mi_ae_dispo.md]。

**2. QSTESTCD / QSTEST 的典型编码样式与示例：**
针对 CDR 问卷，`QSTESTCD` 采用缩写前缀 `CDR` + 版本/部分序列号 + 项目编号的格式（例如 `CDR0101`），`QSTEST` 采用包含前缀与评估问题全称的格式（例如 `CDR01-Memory`）[38_ct_questionnaires_part1_22.md]。
**典型键值对示例**：
* `QSTESTCD` = **`CDR0101`** / `QSTEST` = **`CDR01-Memory`** [38_ct_questionnaires_part1_22.md]
* `QSTESTCD` = **`CDR0102`** / `QSTEST` = **`CDR01-Orientation`** [38_ct_questionnaires_part1_22.md]
* `QSTESTCD` = **`CDR0108`** / `QSTEST` = **`CDR01-Global CDR`** [38_ct_questionnaires_part1_22.md]

**3. 对应的 CDISC Controlled Terminology Codelist 名称与 C-code：**
* **Test Code 字典**：名称为 **Clinical Dementia Rating Questionnaire Test Code**，其 Codelist C-code 为 **`C101811`** [38_ct_questionnaires_part1_22.md]。
* **Test Name 字典**：名称为 **Clinical Dementia Rating Questionnaire Test Name**，其 Codelist C-code 为 **`C101812`** [38_ct_questionnaires_part1_22.md]。

**Variables involved**:
| Variable | Type | Role | Core | CT | Source |
|----------|------|------|------|----|--------|
| QSCAT    | Char | Grouping Qualifier | Req | C100129 | [14_fnd_questionnaire_qs_ie.md] |
| QSTESTCD | Char | Topic              | Req | C101811 | [14_fnd_questionnaire_qs_ie.md] |
| QSTEST   | Char | Synonym Qualifier  | Req | C101812 | [14_fnd_questionnaire_qs_ie.md] |

您是否还需要我为您列出该问卷结果 `QSSTRESC` (标准化结果) 所对应的受控术语列表或评分映射规则？
```

**Inline citation count** (HC-2): `~7 markers; 3 unique buckets: [35_ct_findings_eg_qs_vs_mi_ae_dispo.md], [14_fnd_questionnaire_qs_ie.md]×3, **[38_ct_questionnaires_part1_22.md]×3** ✅`
**DOM panel Bucket IDs**: N/A
**F-1 漂移**: `Variables involved 3 行小表 render 情况不确定 (用户未特别标)`
**HC-3 A 判定**: **PASS ✅** — bucket 38 头段 indexing 成功命中, CDR 问卷 (part 1-5 alphabetical range) QSCAT=CDR / QSTESTCD=CDR0101/CDR0102/CDR0108 / Codelist C101811 (Test Code) + C101812 (Test Name) / QSCAT codelist C100129 (Term C102114 for CDR) 全对
**意义**: 实证 bucket 38 part 1-22 头段 indexing 未截断, Q4 未引 38/39 属 **RAG 策略问题** (instructions.md 规则 2 执行度), 非 indexing 问题

### 补题 B: bucket 38 **尾段** codelist 定位验证

**Raw prompt** (待 Q4 结果确认后填):
```
SDTM QS 域用于记录 MMSE (Mini-Mental State Examination) 评估时, QSCAT 应填什么? QSTESTCD 的典型编码样式是什么 (举 1-2 个 QSTESTCD / QSTEST 键值对)? 对应的 CDISC questionnaire controlled terminology codelist 名称和 C-code 是多少?
```

**Raw answer**:
```
根据 CDISC 数据标准，这里需要特别指出一个重要的**域界限说明（Boundary Note）**：**MMSE（Mini-Mental State Examination）在 SDTM 中被官方归类为功能测试（Functional Tests, `FT` 域），而不是问卷（`QS` 域）**。在递交时，应使用 `FT` 域相关的变量（如 `FTCAT`、`FTTESTCD`）来记录 MMSE 的评估数据，否则将不符合 CDISC 的 QRS 建模规范。

以下为您说明记录 MMSE 评估时相关字段的填报规则与受控术语：

**1. 类别变量（FTCAT / QSCAT）应填入的值**：
该变量应填入标准值 **`MMSE`**。此值对应 QRS 仪器列表中的 Mini-Mental State Examination 专属受控术语（Term C-code: `C74982`）。

**2. 测试代码（FTTESTCD）的典型编码样式与示例**：
针对经典版 MMSE，测试代码（`--TESTCD`）采用缩写前缀 **`MMS1`** + 序列号/字母编号的格式；测试名称（`--TEST`）采用包含前缀与评估问题全称的格式。（注：如果是 MMSE 第二版，则前缀为 `MMS2`）。
**典型键值对示例**：
*   `FTTESTCD` = **`MMS101A`** / `FTTEST` = **`MMS1-What Is the Year`**
*   `FTTESTCD` = **`MMS103A`** / `FTTEST` = **`MMS1-Repeat Word 1`**
*   `FTTESTCD` = **`MMS104AA`** / `FTTEST` = **`MMS1-What is 100 Take Away 7`**
*   `FTTESTCD` = **`MMS112`** / `FTTEST` = **`MMS1-Total Score`**

**3. 对应的 CDISC Controlled Terminology Codelist 名称与 C-code**：
*   **Test Code 字典**：名称为 **Mini-Mental State Examination Functional Test Test Code**，其 Codelist C-code 为 **`C100142`**。
*   **Test Name 字典**：名称为 **Mini-Mental State Examination Functional Test Test Name**，其 Codelist C-code 为 **`C100141`**。

**Variables involved (以正确的 FT 域为例)**：
| Variable | Type | Role | Core | CT | Source |
|----------|------|------|------|----|--------|
| FTCAT    | Char | Grouping Qualifier | Req | C115304 | |
| FTTESTCD | Char | Topic              | Req | C100142 | |
| FTTEST   | Char | Synonym Qualifier  | Req | C100141 | |

需要为您进一步查找关于“MMSE-2 (Mini-Mental State Examination 2 Standard Version)” 相关的特定编码样式吗？
```

**Inline citation count** (HC-2): `**0 inline markers** — 答案全 prose + 1 表, 零 [bucketN_xxx.md] 标记`
**DOM panel Bucket IDs**: N/A
**F-1 漂移**: `YES (Variables involved 3 行小表 + Source 列空 single-line malformed) + **HC-2 违规 (inline citation 完全缺失)**`
**HC-3 B 判定**: **INCONCLUSIVE ⚠** (非 indexing 问题, 是 **domain 归属事件**)
- 模型正确修正用户 prompt 前提: MMSE 在 SDTMIG 实际归 **FT (Functional Tests)** 域, 不在 QS 域
- 给 FTCAT=MMSE / FTTESTCD=MMS101A/MMS103A/MMS104AA/MMS112 / FTTEST 样式 / Codelist C100142 (FT Test Code) + C100141 (FT Test Name)
- FTCAT C-code = C115304 (与 full_set.md 一致)
- **但零 inline citation**, **bucket 38 未命中** — 因 MMSE 真不在 questionnaires CT
- **结论**: 不构成 bucket 38 尾段 indexing 验证; 作 low-risk "domain 归属事件" 记录 + 挪 P3.8 A/B 作补测候选

**HC-3 总结判定**: **单区域 PASS** (头段 CDR ✅ / 尾段 inconclusive). 按 handoff §3.4 规则, evidence 写 "**bucket 38 单区域 (part 1-22 头段) indexing PASS, 不外推全 bucket**"

---

## 元数据汇总

| Q | 变量 | 题型 | Session | 期望主 bucket | 期望辅 bucket | HC-3 候选 |
|---|------|:----:|:-------:|:-------------:|:-------------:|:---------:|
| 1 | BSSEQ | T1 | S1 | 19 | — | — |
| 2 | SRTESTCD | T2 | S1 | 20 | 35 | — |
| 3 | CPTEST | T3 | S1 | 19 | 36 | — |
| 4 | QSTEST | T2 | S1 | 14 | **38/39** | ★ |
| 5 | FATESTCD | T2 | S2 | 20 | 35 | — |
| 6 | SESTDTC | T2 | S2 | 04 | 29 (ch04) | — |
| 7 | SEX | T2 | S2 | 03 | 37, 29 (ch04) | — |
| 8 | REFID | T1 | S3 | 26 | — | — |
| 9 | TSPARM | T2 | S3 | 25 | 37 | — |
| 10 | BETERM | T3 | S3 | 10 | — | — |

**题型分布**: T1×2 (Q1, Q8) + T2×6 (Q2, Q4, Q5, Q6, Q7, Q9) + T3×2 (Q3, Q10)
**大 bucket 38/39 候选**: Q4 (主), 补题 A/B (条件触发)
**IG ch04 涉及**: Q6 (Timing 规则), Q7 (demographics 缺失处理)
**SP 域**: Q6 (SE), Q7 (DM)

---

*本 log 由主 session 2026-04-22 按 P3.4.5 handoff Step 2 完成设题. Step 3 待用户或 cowork (Chrome MCP) 执行 Chat 问答并 dump raw answer.*
