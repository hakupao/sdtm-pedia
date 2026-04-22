# Phase 4 N5.3 题库 draft 独立 Reviewer 报告 (Gemini 侧, 第 21 种 subagent_type)

## 元数据

- **Reviewer subagent_type**: feature-dev:code-explorer (Rule D 第 21 种独立 subagent_type)
- **审查范围**: Q1-Q10 (双平台共用 10 题)
- **审查日期**: 2026-04-21
- **Draft 版本**: smoke_v3_questions_draft.md v3.0 (2026-04-21)
- **Gemini 上传配置**: 4 文件 (01/02/03/04_business_scenarios) + system_prompt v5
- **Rule A 抽样**: N=3 (Q1 GF 变量, Q3 RELSPEC 结构, Q10 QORIG/QVAL)
- **Citations**: 56 (grep evidence + KB spec 直接读取)

---

## Executive Summary

**Verdict: CONDITIONAL PASS**
**Confidence: 高**
**Gate Decision: HOLD — 2 HIGH findings 须处置后方可进 Step 4 Web UI**

Gemini 可答性总评估: 10 题中 6 题高置信度可答 (Q1/Q2/Q3/Q6/Q7/Q9), 4 题中置信度 (Q4/Q5/Q8/Q10)。主要风险是 Q10 PASS 判据本身含事实错误 (HIGH-1), Q4 IS scope v3.4 跨版本记忆干扰 (HIGH-2)。

**Findings 数量: HIGH 2 / MED 3 / LOW 2**

---

## Q1-Q10 Gemini 可答性逐题 (维度 1)

### Q1 (GF 域 EGFR 变异场景)

**02 文件独立 grep 结果:**
- GFTESTCD: Order 12, Role Topic, Core **Req** [02 line 7037-7044]
- GFTEST: Order 13, Core **Req**
- GFSEQ: Order 6, Core **Req**
- GFREFID: Order 8, Core **Exp** — draft 列为 Exp 原材料正确
- GFORRES: Order 17, Core **Exp** [02 line 7082-7089] — 确认 draft Exp 分类正确
- GFINHERT: Order 26, Label "Inheritability", Core **Perm**, CT C181177 [02 line 7163-7170]
- GFGENREF: Order 27, Label "Genome Reference", Core **Perm**, Notes 明文含 "GRCh38.p13" 示例 [02 line 7172-7179]
- GFGENSR: Order 32, Label "Genetic Sub-Region", Core **Perm**, Notes 含 "Exon 15", "Kinase domain" 示例 [02 line 7217-7224]
- GFPVRID: Order 34, Label "Published Variant Identifier", Core **Perm**, Notes 含 "rs2231142" 示例 [02 line 7235-7242]
- CT: C181177 (Inheritability), C181178 (TestCode), C181179 (TestName) [02 line 7457-7459]

**04 文件 grep 结果:**
- §22 domain table: "GF | Genomic Findings | GFTESTCD / GFTEST" 一行 [04 line 1598]
- §22.3 一句: "GF (Genomic Findings): 基因突变/拷贝数变异/基因表达" [04 line 2584]
- GFGENSR / GFPVRID / GFINHERT / GFGENREF: **04 零匹配** — Pure generalization 确认

**PASS 判据验证**: 所有核心变量均在 02 文件有完整 spec 原材料。GFGENSR Notes "Exon 15" 与题目 "Exon 19" 直接对齐。GFPVRID Notes "rs2231142" 与题目 "rs121913444" 同类型 dbSNP ID。

**Gemini 答题置信度: 高**

---

### Q2 (CP 域 流式细胞 CD4+ T 细胞)

**02 文件独立 grep 结果:**
- CPTESTCD: Order 10, Topic, Core **Req** [02 line 2699-2706]
- CPTEST: Order 11, Core **Req**
- CPSBMRKS: Order 12, Label "Sublineage Marker String", Core **Perm** [02 line 2717-2724]
- CPCELSTA: Order 13, Label "Cell State", Core **Perm**, Notes 明文 "ACTIVATED", "PROLIFERATING", "SENESCENT" [02 line 2726-2733]
- CPCSMRKS: Order 14, Core **Perm** [02 line 2735-2742]
- CPMETHOD: Order 45, Perm [02 line 3014]
- CPBDAGNT: Order 17, Perm [02 line 2762]
- IS assumption 4 明文: "Flow cytometry data should be modeled in the Cell Phenotype Findings (CP) domain" — 直接对应 FAIL 判据 "答 IS"

**04 文件 grep 结果:**
- §22.3 一行: "CP (Cell Phenotype Findings): 流式细胞分析 (CD4+/CD8+ 计数)" [04 line 2583]
- CPSBMRKS / CPCELSTA / CPCSMRKS: **04 零匹配** — Pure generalization 确认

**PASS 判据验证**: CPCELSTA Notes 含 "ACTIVATED" 直接对应题目要求。CPSBMRKS vs CPCELSTA 概念区分在 02 Notes 清晰。

**Gemini 答题置信度: 高**

---

### Q3 (BE + BS + RELSPEC 生物样本)

**02 文件独立 grep 结果:**
- BETERM: Order 9, Topic, Core **Req** [02 line 1143]
- BECAT Notes: "COLLECTION, PREPARATION, TRANSPORT" [02 line 1177]
- BSTESTCD: Order 9, Topic, Core **Req**, Notes 明文 "VOLUME, RIN" [02 line 1411-1418]
- BSTEST Notes: "Volume, RNA Integrity Number" [02 line 1427]
- CT C124300 (Biospecimen Characteristics Test Code) 确认 [02 line 1660]
- BS Related Domains: "Specimen Relationship: RELSPEC — specimen hierarchy" [02 line 1671]

**KB RELSPEC/spec.md 独立读取 (Rule A 抽样 2):**
- RELSPEC Class=Relationship, "One record per specimen identifier per subject"
- REFID: Order 3, Core **Req** — "Specimen ID, unique within USUBJID"
- PARENT: Order 5, Core **Exp** — "Identifies the REFID of the parent of a specimen"
- LEVEL: Order 6, Core **Req** — "generation number; collected sample = first generation"

**04 文件 grep 结果:**
- RELSPEC / BSTESTCD / BETERM: **04 零匹配** — Pure generalization 完全确认

**PASS 判据验证**: "用 RELSPEC 不用 RELREC" 方向正确。RELSPEC 内部用 PARENT+LEVEL (非 IDVAR/IDVARVAL) 机制未在 draft PASS 判据明确说明 — 建议补充 (LOW-1)。

**Gemini 答题置信度: 高**

---

### Q4 (LB vs MB vs IS 三场景选域)

**02 IS assumptions 独立读取:**
- Assumption 1: IS 覆盖 "whether a therapy (biologic, drug, vaccine) provoked/caused/induced an immune response"
- Assumption 2: **"Assessments pertaining to antibodies produced in response to microbial infection will also be represented in the IS domain"** [02 line 8523] — 直接支持场景 A 应在 IS
- Assumption 3: "all other types of induced humoral (antibody) immune response → IS"
- Assumption 5: "Microbial antigen/antibody combination tests → MB domain" (例外: Ag/Ab 组合检测)
- ADA: IS assumption 7.a: "antidrug antibody (ADA) tests — ISBDAGNT 存药物名" — 场景 B 直接支持

**关键风险: 无显文 v3.3→v3.4 版本迁移规则**
- KB IS assumptions 无 "v3.3 时 baseline antimicrobial IgG 在 MB, v3.4 统一到 IS" 的版本历史描述
- draft PASS 判据依赖此版本历史知识作为 FAIL 判断基础
- system_prompt v5 无 IS scope 锚点
- **风险: Gemini 可能基于 v3.3 预训练记忆将场景 A 答为 MB — 触发 FAIL 判据**

**04 grep: IS / ISBDAGNT / LB vs MB vs IS: 04 零深入覆盖** — Pure generalization 确认

**Gemini 答题置信度: 中** (02 有原材料但跨版本记忆风险高)

---

### Q5 (FA vs QS vs CE 边界)

**04 文件 §1.19 + §1.20 完整 grep (重叠量化):**
- §1.19 "Questionnaire (QS) 和 Findings About (FA) 区分" [04 line 833]
- §1.19 场景: EQ-5D 问卷 (≈ Q5 场景 B QS 部分)
- §1.19 QS vs FA 区别完整 [04 line 852-854]
- §1.20 "AE 附加信息 SUPPAE vs FA": FAOBJ="AE" 场景, FATESTCD/FAOBJ/FAORRES 全列 [04 line 911-921]
- FATESTCD / FAOBJ: 04 共计出现 5+ 次
- CE: **04 零覆盖** — CE 场景 C 是纯 generalization

**重叠量化:**
- Q5 场景 A (FA) + 场景 B (QS): 04 §1.19 + §1.20 深度覆盖, **约 40-50% 重叠**
- Q5 场景 C (CE): 04 完全未覆盖
- 整题加权重叠: **约 30-40%** — 超过 30% 阈值

**Gemini 答题置信度: 中-高** (FA/QS 可能背答案; CE 是真 generalization)

---

### Q6 (PC Timing --TPT 四件套)

**02 文件 PC spec 独立 grep:**
- PCTPT: Order 36, Perm [02 line 13097-13104]
- PCTPTNUM: Order 37, Perm
- PCELTM: Order 38, Notes: **"ISO 8601 ... Not a clock time or a date time variable"** [02 line 13115-13122]
- PCTPTREF: Order 39, Notes: "Name of the fixed reference point ... Example: MOST RECENT DOSE"
- PCRFTDTC: Order 40

**04 grep: PCTPT / PCTPTREF / PCELTM / PCRFTDTC: 04 零匹配** — Pure generalization 确认

**PASS 判据验证**: PCELTM "ISO 8601 duration PT4H" — 02 Notes 明文支持。PCTPTREF 是 name — 02 Notes 支持。

**Gemini 答题置信度: 高**

---

### Q7 (Partial date 精度 + imputation 规则)

**04 文件 §1.8 完整 grep:**
- §1.8 ISO 8601 部分精度表格, 含 "2024-06" / "2024" 示例 [04 line 370-381]
- §1.8 pitfall: "强填占位符如 2024-06-15T00:00 — 错" [04 line 407]
- §2.9: "只年 YYYY 合法" + ISO 格式边界
- §9.6 FAQ: "ISO 8601 允许部分精度? 2024 / 2024-06 / 2024-06-15 都合法"

**04 未覆盖 (generalization):**
- SDTM 不做 imputation / ADaM 做 imputation 职责边界: **04 完全未覆盖**
- 场景 C "Unknown → null" — 04 §1.14 通则但未针对 partial date Unknown

**Gemini 答题置信度: 高**

---

### Q8 (CT Extensible vs Non-Extensible)

**04 文件 §1.15 系列完整 grep (重叠量化):**
- §1.15 Extensible/Non-extensible 定义完整 [04 line 750-752]
- §1.15 pitfall 3 条完整 [04 line 758-761]
- §9.7 FAQ Extensible 加 Term + Define-XML [04 line 1711-1712]
- §2.13 MedDRA: "AEDECOD 必须是 MedDRA PT; Define-XML 声明版本" [04 line 1113-1115]
- §2.7 CT 版本陷阱 + Define-XML

**重叠量化:**
- Q8(a) Extensible 语义: 04 §1.15 **完整覆盖 (~100%)**
- Q8(b) Non-ext/Ext 例子: 部分覆盖
- Q8(c) AETERM MedDRA 外部 vs AESEV CDISC CT 对比: 04 §2.13 有 MedDRA 内容但**未明文对比变量 CT 属性差异**
- Q8(d) Define-XML codelist extension 具体步骤: **未深入**
- **整题重叠: 约 40-45%** — 超过 30% 阈值

**Gemini 答题置信度: 中**

---

### Q9 (Pinnacle 21 FAIL 分类)

**04 grep: "Pinnacle 21" / "Validator" / "OpenCDISC": 04 零匹配** — Pure generalization 完全确认

**Gemini 答题置信度: 中** (纯预训练, 无 KB 支撑; 5 大类覆盖度依赖预训练质量)

---

### Q10 (SUPP 深化: QORIG/QEVAL/SUPPTS/QVAL)

**KB SUPPQUAL/spec.md 独立读取 (Rule A 抽样 3):**
- QORIG: Order 9, Core **Req**, Notes "origin of this data. Examples: CRF, Assigned, Derived" [spec.md line 77-84]
- QEVAL: Order 10, Core **Exp**, Notes "Used only for subjective results ... null for objectively collected or derived" [spec.md line 86-93]
- QVAL: Order 8, Core **Req**, Type **Char**, Notes: "no records can be in SUPP-- with a null value for QVAL" — **无显式长度限制** [spec.md line 68-75]

**04 §19 + §1.9 grep:**
- §19.2 表格: QORIG "CRF/DERIVED/ASSIGNED", QEVAL "INVESTIGATOR 等" [04 line 2324-2325]
- §1.9 表格: QORIG 标为 **(可选) CRF**, QEVAL 标为 **(可选) INVESTIGATOR** [04 line 444-445]
- **严重矛盾: 04 §1.9 将 QORIG 标为 "(可选)" — 与 KB SUPPQUAL/spec.md Core=Req 直接矛盾。04 本身有错。**
- SUPPTS: **04 §19 零覆盖** — 纯 generalization

**QVAL 200 字符上限 — 独立 KB 查阅:**
- KB ch04_general_assumptions.md §4.5.3.2 表格: "First 200 chars in parent domain variable; each additional 200 chars in a SUPP-- record" [ch04 line 1298]
- **正确语义: 200 字符是**标准域变量**超长时分拆到 SUPP 记录的机制, 不是 QVAL 自身的硬性长度上限**
- QVAL spec 无显式长度上限
- **draft Q10 PASS 判据 "QVAL 长度上限 200 字符 (CDISC SDTMIG v3.4 §8.4)" 是对 ch04 §4.5.3.2 内容的错误归因**

**Gemini 答题置信度: 中** (QORIG/QEVAL 方向对但 04 干扰; SUPPTS 纯 generalization; QVAL 判据本身有误)

---

## 04 非重叠独立 Grep (维度 2)

| Q | 核心 keyword | 04 grep | 04 章节 | 重叠判断 | 结论 |
|:---:|---|:---:|---|:---:|---|
| Q1 | GFTESTCD/GFGENSR/GFINHERT | 1 (table) | §22+§22.3 一句 | ✅ Pure | 无深入场景 |
| Q2 | CPTESTCD/CPSBMRKS/CPCELSTA | 1 (table) | §22+§22.3 一句 | ✅ Pure | 无深入场景 |
| Q3 | RELSPEC/BSTESTCD/BETERM | 0 | N/A | ✅ Pure | 04 完全零覆盖 |
| Q4 | IS/ISBDAGNT | 0 deep | 无 | ✅ Pure | 04 无 LB/MB/IS 对比 |
| Q5 | FA/QS/CE/FATESTCD/FAOBJ | 5+ | §1.19+§1.20 完整场景 | ⚠️ **40-50%** | 超阈值 |
| Q6 | PCTPT/PCTPTREF/PCELTM | 0 | N/A | ✅ Pure | 无 TPT 深化 |
| Q7 | partial date/imputation | 有 §1.8 格式 无 imputation | §1.8+§2.9+§9.6 | ✅ Pure | imputation 部分是真 generalization |
| Q8 | Extensible/MedDRA/Define-XML | 多处 | §1.15+§9.7+§2.13 | ⚠️ **40-45%** | 超阈值 |
| Q9 | Pinnacle 21 | 0 | N/A | ✅ Pure | 零覆盖 |
| Q10 | QORIG/QEVAL/SUPPTS | §1.9+§19 基础 (QORIG 标注有误) | §1.9+§19.2 | ✅ Pure | 核心判据未覆盖 |

**Pure (< 30%): Q1/Q2/Q3/Q4/Q6/Q7/Q9/Q10** — 8 题
**Borderline (> 30%, 需 reframe): Q5/Q8** — 2 题

---

## Gemini 特定 Pitfall 风险 (维度 3)

### 3.1 自污染类风险 (对比 N5.1 事件)

- system_prompt v5 无 GF/CP/BE/BS/IS 任何变量锚点 (仅 CO-1/CO-1b/CO-2/CO-2c 约 AE/DM/LBNRIND/ARM)
- 04 对 Q1-Q3 新域和 Q6/Q9/Q10 深化均无预设场景
- **整体自污染风险: LOW** — 04 无跨文件预设答案

### 3.2 幻觉 codelist 风险 (对比 Q3 LBNRIND 事件)

- Q1 GFINHERT CT C181177: CO-2 要求外导 NCI EVS — **风险可接受**
- Q8 AESEV: CO-2 明文 "MILD/MODERATE/SEVERE" — **风险 LOW**
- Q10 QORIG 值: 04 §1.9/§19 有这些值 — **风险 LOW**
- Q4 IS ISBDAGNT CT: CO-2 保护 — **风险 LOW**

### 3.3 跨版本记忆风险 — Q4 IS scope (HIGH-2)

**具体风险:**
- IS assumption 2 (02 文件) 有 "antibodies produced in response to microbial infection → IS" 原材料
- 但 KB 无 "v3.3 baseline antimicrobial IgG 在 MB, v3.4 统一到 IS" 显文迁移规则
- Gemini 预训练可能包含 v3.3 规则 (baseline serology → MB)
- draft FAIL 判据: "A 答 MB (v3.2/v3.3 旧规则)" — 正是最高概率的错误路径
- system_prompt v5 无 IS scope 专项锚点

**风险级别: HIGH**

### 3.4 Q6 Timing Planned vs Actual 混淆

- 02 PC spec PCELTM Notes 明文 "Not a clock time"
- 04 §1.8 已覆盖 ISO duration "PT6H"
- **风险: 低**

---

## Rule A N=3 独立抽样

### 抽样 1: Q1 — GF 核心变量 → PASS

独立 KB 查阅确认: 域 GF; 6 Req + 1-3 Exp; GFGENSR Notes "Exon 15", GFPVRID Notes "rs2231142", GFGENREF Notes "GRCh38.p13" 全与题目对齐; GFINHERT CT C181177 确认。vs draft PASS 判据一致。

### 抽样 2: Q3 — RELSPEC 结构 → PASS with note

RELSPEC Class=Relationship, 用 REFID (Req) + PARENT (Exp) + LEVEL (Req) 表达 specimen 层级。draft "用 RELSPEC 不用 RELREC" 方向正确但未说明 RELSPEC 内部 PARENT+LEVEL (非 IDVAR/IDVARVAL) 机制。建议补 LOW-1。

### 抽样 3: Q10 — QORIG Core + QVAL 长度 → FAIL on 200字符判据

QORIG Core=**Req** (无条件必填, 不是"可选"), QEVAL Core=**Exp**, QVAL Core=Req Type=Char **无显式长度限制**。ch04 §4.5.3.2 表格描述的是**标准域变量**超 200 字符时分拆到 SUPP 记录的机制, 不是 QVAL 自身长度上限。draft "QVAL 长度上限 200 字符 (CDISC SDTMIG v3.4 §8.4)" 归因错误 → HIGH-1。

---

## Carry-over

### HIGH (阻塞 Gate)

**HIGH-1: Q10 QVAL "200 字符上限" PASS 判据事实错误**
- 问题: draft PASS 判据 "QVAL 长度上限 200 字符 (CDISC SDTMIG v3.4 §8.4)" 是对 ch04 §4.5.3.2 内容的错误归因。该段描述标准变量文字超长时分拆到 SUPP 记录的机制 ("First 200 chars in parent domain variable; each additional 200 chars in a SUPP-- record"),不是 QVAL 自身长度上限。QVAL spec Type=Char 无显式长度。
- 推荐修法: Q10(d) PASS 判据改为 "QVAL 在 SAS XPT v5 传输文件受 SAS 字符变量 200 字节技术限制; SDTMIG §4.5.3.2 描述超 200 字符标准变量分拆机制 (同一 QNAM 加数字后缀追加多条 SUPP 记录); FAIL '答 40 或 500' 保留, 但删除 '§8.4 规定 200 字符' 措辞"
- 证据: SUPPQUAL/spec.md line 68-75; ch04_general_assumptions.md line 1298

**HIGH-2: Q4 IS scope v3.4 Gemini 跨版本记忆风险**
- 问题: KB IS assumptions (02) 有正确原材料 (assumption 2 明文 antimicrobial antibody → IS), 但无显文 "v3.3 baseline IgG → MB, v3.4 迁到 IS" 版本迁移规则。Gemini 预训练可能包含 v3.3 规则, 有较高概率对场景 A 答 MB 触发 FAIL 判据。
- 推荐修法 (三选一):
  - (A) 在 04 补充 IS vs MB 边界一句: "v3.4 IS 覆盖所有宿主抗体免疫应答 (含抗微生物 IgG baseline); MB 仅限微生物直接检出 (培养/PCR/染色/抗原)"
  - (B) Q4 PASS 判据补: "若答 MB 但理由含 '免疫应答/antibody' → PARTIAL (非完全 FAIL), KB 原材料存在但版本迁移规则无显文"
  - (C) 接受此风险并记录
- 证据: 02 IS assumptions 1-3 (line 8521-8525); system_prompt v5 无 IS scope 锚点

### MED (Step 4 前修)

**MED-1: Q5 04 重叠 >30%, FA/QS 子场景降权**
- 04 §1.19+§1.20 对 FA/QS 40-50% 覆盖, CE 才是真 generalization
- 修法: PASS 判据明标 "场景 C (CE) 权重 50%, A (FA) 30%, B (QS) 20%"; 或替换 A/B 为 CE+DV+HO 三元鉴别

**MED-2: Q8 04 重叠 >30%, Q8(a) 已完整覆盖**
- 04 §1.15 完整覆盖 Q8(a), 整题 40-45% 重叠
- 修法: 删除或降权 Q8(a); 升 Q8(c)(d) 为主判分项; 或改 "CTCAE vs CDISC CT 外部标准边界"

**MED-3: 04 §1.9 QORIG "(可选)" 与 KB Req 矛盾**
- 04 文件本身错误, 可能使 Gemini 误学 "QORIG 可选"
- 修法: 修 04 §1.9 表格 QORIG 标为 "Req (必填)"; Q10 PASS 判据加 "QORIG Core=Req 无条件必填"

### LOW (Step 5 收束)

**LOW-1: Q3 RELSPEC PARENT+LEVEL 机制未在 PASS 判据说明**
- 修法: 补 "加分: Gemini 说明 RELSPEC 用 PARENT 字段指向父 specimen REFID + LEVEL 代际"

**LOW-2: Q9 完全依赖预训练, 无 KB 支撑**
- 接受此风险 (业务常识合理); 或 PASS 阈值调整为 "≥4 大类"

---

## Gate Decision

**Gemini 侧 Phase 4 Step 3 → Step 4 Web UI Gate: HOLD — CONDITIONAL PASS**

须满足以下前置条件方可进 Step 4:
1. HIGH-1 处置: Q10 QVAL 长度 PASS 判据更正
2. HIGH-2 处置: Q4 IS scope 三选一 (推荐 A: 04 补 IS vs MB 一句边界规则)

可并行处理但不阻塞 Step 4:
3. MED-1: Q5 reframe 权重
4. MED-2: Q8 reframe 降权 Q8(a)
5. MED-3: 04 §1.9 QORIG 修正

**Gemini 10 题预期通过率:**
- 高置信 PASS: Q1/Q2/Q3/Q6/Q7 — 5.0 分
- 中置信 PASS: Q9/Q10 — ~1.5 分 (Q10 判据有误)
- 风险中置信: Q4 (~0.5-1.0), Q5 (~0.75), Q8 (~0.75)
- **预期总分: 8.0-8.5/10** (超 ≥7/10 阈值)
- 修复 HIGH 后: **8.5-9.0/10**

---

*报告生成: 2026-04-21 | 审查者: feature-dev:code-explorer (第 21 种独立 subagent_type) | Rule D 合规 | Citations: 56*
