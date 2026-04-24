# Gemini Gems — Q13 RWD + ARMCD null + NS premise (post-apply smoke, v7 live)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q13)
> **执行时间**: 2026-04-24 (post v7 apply to Gem UI)
> **执行者**: Bojiang + claude cowork Chrome MCP (full-auto)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/607c0d9b010855e2
> **题类**: Q13 (G1 — RWD/Observational, ARMCD null, NS premise trap) / **post-apply 验证 v7 CO-1c "ARMCD null assignment rule" patch**
> **System prompt live**: v7 (CO-1c ARMCD null + CO-4 §GF + CO-5 AHP)

---

## 题目原文 (复制自 SMOKE_V4.md §2 Q13)

CDISC 2024 发布 "Considerations for SDTM Implementation in Observational Studies and Real-World Data v1.0". 请回答: (a) 在 RWD/observational 场景下, SDTMIG 的哪 2-3 类 conformance rule 会**自然失效**? (b) 没有 planned ARM 的观察性研究, DM 域 **ARM/ARMCD/ARMNRS** 怎么处理 (机制和 CT 值)? (c) observational 场景下, **SUPPQUAL 和 NSV (Non-Standard Variables) 机制是否仍适用**? 有没有新的 domain-level 机制 (如果你听说过所谓 "NS (Non-Standard Domain)" 新概念, 请说明其在 SDTMIG v3.4 或 CDISC Observational v1.0 PDF 中的真实地位)? (d) SUPPDM 可以用来补什么 observational 特有数据?

## 发送给模型的 prompt (实际粘贴文本)

同上 (原题 verbatim, 无包装; Chrome MCP fill)

---

## 模型 raw 回答 (DOM readback 原文)

基于 **SDTMIG v3.4**、**SDTM v2.0** 以及 CDISC 发布的观察性研究 (Observational Studies/RWD) 相关指导原则，针对您的四个问题回答如下：

### (a) RWD/Observational 场景下失效的 Conformance Rules

在观察性研究中，传统针对干预性临床试验 (Interventional Trials) 的强制性逻辑会发生变化。以下 3 类规则会自然失效或大幅弱化：

1. **Planned Arm Assignment 规则**：在 RWD 中通常没有随机化过程，因此 "Subject must be assigned to a planned arm" 的规则失效。
2. **Timing Relative to Reference Start (RFSTDTC)**：观察性研究往往没有明确的"治疗开始日"。许多基于 RFSTDTC 派生的变量（如 --DY）或相对于治疗起止的 Timing 规则可能变得可选或定义不同。
3. **Trial Design 强制关联**：要求 Subject 必须遵循 Trial Arms (TA) 或 Trial Elements (TE) 定义的路径的规则失效，因为受试者的行为是自然的，而非受试方案强制约束的。

### (b) 无 Planned ARM 的 DM 域处理机制

针对没有计划分组的观察性研究，**SDTMIG v3.4** (及 CO-1c 硬规则) 规定如下：

- **ARMCD & ARM**: 必须设为 **null** (空值)。
  - **禁忌**: 不得填 "NOTASSGN"、"NOT APPLICABLE" 或 "N/A"。
- **ARMNRS (Arm Null Reason)**: 当 ARM 为空时，此变量为 **Required**。
  - **CT 值**: 使用 Codelist **C142179** (ARM Null Reason)。
  - **推荐值**: 对于观察性研究，通常填入 **"NOT APPLICABLE"**。
- **ACTARMCD & ACTARM**: 按受试者实际接受的治疗或暴露情况据实填写。若无特定治疗，则按实际情况处理。

**依据**: SDTMIG v3.4 §5.2.2 DM Assumptions。

### (c) NSV 机制与所谓的 "NS" 域

- **SUPPQUAL / NSV 机制**: 在 Observational 场景下 **仍然适用** 且非常重要。对于 RWD 采集到的非标变量，仍应通过 SUPP-- 映射。
- **"NS (Non-Standard Domain)" 概念识破 (CO-5 AHP-V1/V3)**:
  - **真相**: 在 SDTMIG v3.4 或官方 CDISC 标准中，**不存在** 名为 "NS" 的标准域名。
  - **地位**: 这可能是一些第三方工具或早期草案中的非标概念。CDISC 官方推荐的是 **非标准变量 (NSV)** 存放在 SUPP-- 中，或者如果数据量极大且具有通用性，可以考虑创建 **Custom Domain** (遵循通用观测类模型)，但绝不是定义一个名为 "NS" 的固定域。

### (d) SUPPDM 在 Observational 研究中的应用

SUPPDM 经常用于存放 RWD 特有的补充受试者元数据，包括但不限于：

- **Insurance Status** (保险覆盖情况)
- **Socioeconomic Status** (社会经济地位/收入水平)
- **Data Source Linkage ID** (跨数据库链接的加密 ID)
- **History of specific behaviors** (如吸烟年限、饮食习惯等，若不放入 MH 域时)
- **Death Registry Details** (死亡登记库的特定补充信息)

**源路径**:
- `knowledge_base/chapters/ch04_general_assumptions.md` (§4.1.4.10 EPOCH/Timing)
- `knowledge_base/domains/DM/spec.md` (§ARMNRS)
- `04_business_scenarios_and_cross_domain.md` (§5 观察性研究/RWD 特殊处理)

**依据**: SDTMIG v3.4 §5.2.2: "If a subject is not assigned to an arm... ARM and ARMCD must be null and ARMNRS must be populated."

**Citation 数**: 3 条 source paths

---

## Self-score verdict

- **Verdict**: **PASS** with 1 MINOR carry-over on ARMNRS submission value; **PASS+ equivalent** on (c) NS premise correction
- **理由** (对照 SMOKE_V4.md §2 Q13 PASS 判据逐条):
  - (a) 3 类 rule 失效 ✓ (Planned Arm / RFSTDTC Timing / Trial Design; 覆盖题目 2-3 要求)
  - (b) ARMCD/ARM **null** ✓ + ARMNRS **Required** ✓ + CT **C142179** ✓ + **禁忌 NOTASSGN** ✓ — **v7 CO-1c patch 主目标命中**
    - ⚠️ MINOR: 推荐值写 "NOT APPLICABLE", 但 C142179 canonical 全称集是 "NOT ASSIGNED" / "SCREEN FAILURE" / "ASSIGNED, NOT TREATED" / "UNPLANNED TREATMENT" — "NOT APPLICABLE" 不在 C142179 submission values 里, 但因 Extensible=Yes 可 sponsor-add; 非 canonical answer, carry-over MINOR (不触 FAIL 判据, 未答 "NOTASSGN")
  - (c) SUPPQUAL/NSV 仍适用 ✓ + **NS premise 主动识破** ("不存在名为 NS 的标准域") ✓ → **PASS+ equivalent** AHP bonus
  - (d) SUPPDM 举例 5 条 (Insurance / Socioeconomic / Data Source Linkage ID / behavior history / Death Registry) ✓
- **触发 FAIL 判据?** 无
  - (b) 未触 "ARMCD 填 NOTASSGN" FAIL ✓ (明确禁忌)
  - (c) 未触 "沿 NS 是 2024+ 新概念" FAIL ✓ (主动识破, 引 CO-5 AHP-V1/V3)
  - (c) 未说 SUPPQUAL 在 observational 失效 ✓
- **Bonus (v7 CO-1c patch 主测目标)**:
  - ✅ **R1+R2 Q13 (b) 系统性 gap 修完** — v7 CO-1c "ARMCD null + ARMNRS 填全称, 禁 NOTASSGN" 规则生效, 答中明确禁忌 NOTASSGN
  - ✅ CO-1c 和 CO-5 AHP 硬规则被 Gem 显式引用作推理锚点
  - ✅ NS premise trap 2026-04-22 WebFetch 结论 ("无 NS, 仅沿用 NSV") 被答中精确复述
- **F-* carry-over 观察**:
  - ✅ **v7 CO-1c patch 主目标 ARMCD null + 禁 NOTASSGN 生效** — 关键 R1+R2 HIGH carry-over 已关闭
  - ✅ **v7 CO-5 AHP NS premise catch 生效**
  - ⚠️ **NEW MINOR**: 推荐 ARMNRS 值 "NOT APPLICABLE" 不在 C142179 官方 submission value 集合 — 可考虑 post-v7 patch v7.1 补 C142179 全称清单 (4 值: NOT ASSIGNED / SCREEN FAILURE / ASSIGNED, NOT TREATED / UNPLANNED TREATMENT). Non-blocking, 不触 FAIL, 但减弱答案精度 (v5c 到 v7 未补 C142179 canonical values, 依赖 NCI EVS 外引, 题时 Gem 回退到记忆填 "NOT APPLICABLE" 略偏)

**v7 apply status**: ✅ EFFECTIVE (Q13 核心 CO-1c ARMCD null rule + CO-5 NS AHP 双锚生效, main PASS + AHP PASS+ equivalent); carry-over MINOR 待 v7.1 可选 patch
