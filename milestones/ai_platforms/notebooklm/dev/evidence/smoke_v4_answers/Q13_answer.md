# NotebookLM — Q13 (R1 smoke v4.0)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q13, v4.0 删 NS 虚构 + 修 ARMCD)
> **执行时间**: 2026-04-22 晚 11:00 PM
> **会话**: fresh, Custom mode
> **题类**: Q13 — RWD/Observational + ARMCD + NS premise trap

---

## 题目原文

CDISC 2024 发布 "Considerations for SDTM Implementation in Observational Studies and Real-World Data v1.0". 请回答: (a) 在 RWD/observational 场景下, SDTMIG 的哪 2-3 类 conformance rule 会**自然失效**? (b) 没有 planned ARM 的观察性研究, DM 域 **ARM/ARMCD/ARMNRS** 怎么处理 (机制和 CT 值)? (c) observational 场景下, **SUPPQUAL 和 NSV (Non-Standard Variables) 机制是否仍适用**? 有没有新的 domain-level 机制 (如果你听说过所谓 "NS (Non-Standard Domain)" 新概念, 请说明其在 SDTMIG v3.4 或 CDISC Observational v1.0 PDF 中的真实地位)? (d) SUPPDM 可以用来补什么 observational 特有数据?

---

## 模型 raw 回答 (DOM readback)

关于 CDISC 2024 年发布的 "Considerations for SDTM Implementation in Observational Studies and Real-World Data v1.0"，该特定文件**未收录 / outside the knowledge base**. 本知识库包含的是完整的 CDISC SDTMIG v3.4、SDTM v2.0 以及 CDISC 受控术语 (NCI EVS) [28_ig_ch01_ch02_ch03.md].

以下基于 SDTMIG v3.4 标准及受控术语为您进行解答, 超出此范围的新规内容将予以明确标识.

### (a) RWD/observational 场景下, SDTMIG 的 conformance rule 失效情况

**未收录 / outside the knowledge base**. 当前知识库 (SDTMIG v3.4) 并未专门列出针对 RWD 或观察性研究而自然失效的 Conformance Rule 清单.

**标准内关于观察性研究的例外说明**: 在 SDTMIG v3.4 中提到, 对于不需要干预的观察性研究, 计算 **--DY** 时依赖的参考起始日期 (**RFSTDTC**, 通常指首次给药日期) 可能为空, 此时可能需要选择其他方案 (如 **RFICDTC** 签署知情同意日期) 作为研究日计算的参考 [03_sp_demographics_subject.md].

### (b) 没有 Planned ARM 的观察性研究中, DM 域的 ARM 变量处理

在 SDTMIG v3.4 中, 如果受试者没有被分配到任何 Arm (如观察性研究), 处理机制如下:
- **ARM 和 ARMCD 必须置为空 (null)**
- **ARMNRS** (Reason Arm and/or Actual Arm is Null) **必须被填充**, 用于说明为什么 Arm 变量为空 [03_sp_demographics_subject.md]

**Variables involved**:

| Variable | Type | Role | Core | CT | Source |
|---|---|---|---|---|---|
| ARM | Char | Synonym Qualifier | Exp | | [03]/[02] |
| ARMCD | Char | Record Qualifier* | Exp | | [03]/[02] |
| ARMNRS | Char | Record Qualifier | Exp | **C142179** | [03] |

**Codelist: Arm Null Reason (C142179)** — 对于符合入排标准但未分配 Arm 且未接受治疗的受试者, 适用的标准受控术语值为 **NOT ASSIGNED** [37_ct_misc_int_dm_sp_td_gf_oi_other.md]. **其他允许的值包括 ASSIGNED, NOT TREATED, SCREEN FAILURE, UNPLANNED TREATMENT** [37_ct_misc_int_dm_sp_td_gf_oi_other.md].

### (c) SUPPQUAL/NSV 机制是否仍适用 & "NS" Domain 概念

在 SDTMIG v3.4 框架下, **SUPPQUAL 机制依然适用**. SUPPQUAL 数据集用于捕获无法容纳在常规观察类数据集 (Events、Findings、Interventions)、DM 或 SV 的标准变量中的非标准变量 (Non-Standard Variables, NSVs) [27_rel_suppqual.md].

**关于 "NS (Non-Standard Domain)" 新概念: 未收录 / outside the knowledge base**.

**真实地位判定 (基于 v3.4)**: 在 SDTMIG v3.4 中, 创建新域的机制被称为"**自定义域 (Custom Domains)**". 自定义域必须基于三大 General Observation Classes (Interventions, Events, Findings) 之一, 并且域代码 (Domain Code) **保留使用以 X、Y 或 Z 开头的双字母组合** (如 XY) [28_ig_ch01_ch02_ch03.md]. **当前 v3.4 知识库中不存在名为 "NS" 的官方领域级别 (Domain-level) 机制**.

### (d) SUPPDM 可以用来补充什么数据?

关于 2024 Observational PDF 中建议放入 SUPPDM 的特有 RWD 数据字段: **未收录 / outside the knowledge base**.

在标准 SDTMIG v3.4 框架中, SUPPDM (Demographics 的补充限定词) 严格用于记录由于标准 DM 变量限制而无法放下的受试者级别的非结果性额外数据, 典型用例包括:

- **多重种族 (Multiple Races)**: 当受试者报告了多个种族, DM.RACE 填为 MULTIPLE, 并在 SUPPDM 中使用如 RACE2, RACE5, CRACE8 (Collected Race 8) 等 QNAM 记录具体的次级分类种族 [03]
- **多重族裔 (Multiple Ethnicities)**: 通过 SUPPDM 记录 ETHNIC1, ETHNIC2 的细分值 [03]
- **"Other, specify" 的详细内容**: 例如 QNAM 为 RACEOTH (Race, Other) 来记录"其他"的具体种族, 或者用 RACEREAS (Race, Reason Details) 记录拒绝透露种族的原因 (如 "REFUGEE - DO NOT KNOW MY RACE") [03]

注: 如果属于客观的受试者身体或社会特征 (如婚姻状况、是否学生等), 应放入 Subject Characteristics (SC) 域而非 SUPPDM [27]/[03].

**Citation 数**: 5+ inline ([03]/[28]/[27]/[37]/[02])

---

## Self-score verdict

- **Verdict**: **PASS** (with NS premise-catch bonus)
- **对照 PASS 判据**:
  - (a) ⚠️ PARTIAL — Observational PDF PUNT "未收录" + 只给 RFSTDTC→RFICDTC 1 例外 (缺 Trial Design 类 / IE domain / Planned visit 3 其他 rule-type)
  - (b) ✓ PASS — **ARM 和 ARMCD 必须置为 null + ARMNRS 必填 + C142179 NOT ASSIGNED + 其他允许值 ASSIGNED NOT TREATED / SCREEN FAILURE / UNPLANNED TREATMENT** 全中, 判据核心覆盖
  - (c) ✓✓✓ **PASS+ (NS premise hallucination caught)** — SUPPQUAL/NSV 在 observational 仍适用 + **"NS (Non-Standard Domain)" 未收录** + **Custom Domains X/Y/Z 双字母 mechanism** 正确路径 + **v3.4 不存在 NS domain-level 机制** 明确识破
  - (d) ⚠️ PARTIAL — Observational PDF PUNT "未收录" + 标准 SUPPDM 典型用例 (多重种族 RACE2/CRACE8 / 多重族裔 / RACEOTH/RACEREAS "Other specify") 完整给出, **但 RWD 特有 Claims/EHR/Registry/cohort ID 未覆盖**
- **触发 FAIL 判据?** 无 (未沿 "NS 是 2024+ 新概念"前提 / 未说 SUPPQUAL 失效 / 未编 NS CT code / 未答 NOTASSGN 8-char 缩写)
- **加分**: **(c) NS premise hallucination 识破** = 本题核心抗幻觉 probe 通过
- **F-* carry-over**:
  - NotebookLM Q13 有 2 PUNT (a)(d) + 2 PASS (b)(c) 混合 pattern (同 Q11, in-KB-only 限制)
  - 但 (c) NS 识破是强信号: **in-KB-only 天然优势 — "找不到即说不存在"** 完美体现
  - ARMCD/ARMNRS (b) 所有 5 个 C142179 CT 值全列, 判据要求的 4 项全中 (NOT ASSIGNED / ASSIGNED NOT TREATED / SCREEN FAILURE / UNPLANNED TREATMENT), 这是 Q13 核心判据
