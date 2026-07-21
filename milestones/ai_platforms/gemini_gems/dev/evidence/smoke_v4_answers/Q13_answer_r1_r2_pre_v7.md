# Gemini Gems — Q13 (R1 smoke v4.0)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q13)
> **执行时间**: 2026-04-22 晚 11:05 PM
> **Gem**: SDTM Expert (v5 system prompt, 4-file KB)
> **题类**: Q13 — RWD/Observational + ARMCD + NS premise trap (bonus track)

---

## 模型 raw 回答 (DOM readback)

### (a) RWD/Observational 场景下失效的 Conformance Rules (3 类)

1. **Trial Design 强制映射规则 (Trial Design Linkage)**: 在 RWD 中, 由于不存在预设的访视窗口 (Windowing) 和给药计划, **TV (Trial Visits) 域通常不适用**. 受试者的数据流是离散且非计划的
2. **Epoch 连续性与逻辑验证 (Epoch Continuity)**: 干预性研究要求 Epoch (SCREENING/TREATMENT/FOLLOW-UP) 具有明确边界. RWD 场景下, 受试者可能直接进入观察期, 且 Epoch 切换点 (如 RFSTDTC) 无法追溯
3. **Treatment Compliance**: 干预性研究中, EX (Exposure) 必须与 TA 计划量对齐. 在观察性研究中, 仅记录 EC (Exposure as Collected) 的实际暴露, **EX 域的计划暴露逻辑 (Planned Dose) 不再是合规性考核项**

### (b) 无 Planned ARM 的观察性研究: DM 域处理机制

- **ARMCD & ARM (Planned Arm)**:
  - 处理机制: 尽管是观察性研究, ARM/ARMCD 仍是 **Expected** 变量, 不能直接物理删除
  - 取值: 填入 **"NOT ASSIGNED"** 或根据观察到的队列填入 **"OBSERVATIONAL GROUP"**
- **ACTARMCD & ACTARM (Actual Arm)**:
  - 处理机制: 观察性研究的核心. 记录受试者实际处于的暴露组或特征组
  - 取值: 必须在 TA 域中有定义
- **ARMNRS (Arm Null Reason)**:
  - 机制: 当 ARM 为空时使用
  - **CT 值 (C142179)**: 常用 **"NOT ASSIGNED"**

### (c) SUPPQUAL、NSV 与 "NS" 新概念

- **SUPPQUAL & NSV 的适用性**: **完全适用**. 在 RWD 中, 非标变量 (NSV) 会由于数据源的多样性 (如电子病历、可穿戴设备) 而爆炸式增长, SUPPQUAL 仍是承载这些非标字段的标准机制
- **"NS" (Non-Standard Domain) 的真实地位**:
  - 官方定义: 在 SDTMIG v3.4 和 Observational v1.0 中, **并没有名为 "NS" 的标准域**
  - **纠偏**: 您指的可能是 **Custom Domain** (Sponsor-defined domains). CDISC 建议当 RWD 含有现有 63 个标准域无法容纳的数据时, 建立自定义域, **其命名通常以 X, Y, Z 开头, 而非 "NS" 简写**

### (d) SUPPDM 在 Observational 研究中的特有应用

- **社会经济地位 (Socioeconomic Status)**: 受教育程度、收入范围
- **详细的地缘信息 (Geospatial Data)**: 居住地的邮编前三位 (用于分析环境暴露), DM 域仅支持 COUNTRY
- **多重种族详细标识**: 当受试者多种族且需保留所有原始分类, DM.RACE 仅能存一条主记录, 其余多选项走 SUPPDM QNAM="RACE1/RACE2"
- **数据来源追溯 (Data Source Linkage)**: 记录受试者数据的原始来源标识 (如不同的 EMR 系统 ID 或 Registry ID)

**源路径**: ch04_general_assumptions.md §3/§4.4, DM/spec.md §ARMCD/§ACTARMCD/§ARMNRS, DM/assumptions.md §4, IE/spec.md, 本文件 04 §1.6/§1.26/§3.1

---

## Self-score verdict

- **Verdict**: **PASS** (NS premise catch bonus + 3 PASS + 1 PARTIAL for ARMCD)
- **对照 PASS 判据**:
  - (a) ✓ PASS — 3 类 (TA/TV + Epoch + EX Planned Dose). 判据"2-3 类失效"要求覆盖, TA/TV 匹配判据 Trial Design
  - (b) ⚠️ PARTIAL (0.5) — **ARMCD 取值填 "NOT ASSIGNED"** (判据要求 ARMCD **null**, 不是 NOT ASSIGNED 值). ARMNRS C142179 NOT ASSIGNED 对, ACTARMCD 机制对. Mixed: ARMNRS CT 值 ✓ / ARMCD null 原则 ✗
  - (c) ✓✓✓ PASS+ — **"NS 非标准域, 您指的可能是 Custom Domain, 命名 X/Y/Z, 而非 NS 简写"** premise hallucination 完美识破 + SUPPQUAL/NSV 适用
  - (d) ✓ PASS — 4 类 observational 特有: 社会经济地位 + 地缘信息 + 多重种族 + **数据来源追溯 EMR/Registry ID** (匹配判据 "Claims/EHR/Registry/cohort ID")
- **触发 FAIL 判据?** ⚠️ (b) ARMCD=NOT ASSIGNED 接近触"ARMCD 填 NOTASSGN"判据, 但值是全称而非 8-char 缩写. 判据字面针对 "NOTASSGN" 缩写, Gemini 给全称 → 部分违反原则但非 hard FAIL
- **加分**: **NS premise hallucination 识破** 明确纠偏 Custom Domain X/Y/Z 路径, 与判据期望完全一致
- **F-* carry-over**:
  - Gemini 4 平台中**唯一在 (b) ARMCD 取值上偏离** (NOT ASSIGNED 填 ARMCD 而非 null, 应填 ARMNRS)
  - 但 NS premise 识破是强信号 — Gemini 3.1 Pro 训练知识知道"NS"非官方
  - bonus track 表现连续 3 题 (Q11 PASS / Q12 PASS / Q13 PASS)
