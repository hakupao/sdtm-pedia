# Gemini Gems — Q10 SUPP + SUPPTS premise trap (post-apply v7.1 LIVE)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q10)
> **执行时间**: 2026-04-24 PM (post v7.1 CO-1d apply to Gem UI)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/2ed5141637e7bbc4
> **题类**: Q10 (H1 — SUPP 深化 + SUPPTS AHP premise trap) / **post-apply 验证 v7.1 CO-1d "SUPP-- Core + scope 硬锚" patch**
> **System prompt live**: v7.1 (v7 + CO-1d SUPP-- Core + scope hard anchor)

## Prompt

同 SMOKE_V4.md §2 Q10 原题

## Raw 回答 (DOM readback)

根据 SDTMIG v3.4 规范及知识库 (02_domains_spec_and_assumptions.md 与 04_business_scenarios_and_cross_domain.md) 的硬锚定规则:

### (a) QORIG 与 QEVAL

- **QORIG (Origin)**:
  - **Core: Req (Required)** ✓ — 每条 SUPP 记录**必须填写 QORIG**
  - 含义: 标识 Qualifier 的来源
  - 必填场景: 始终必填
  - 常见值: "CRF" / "Derived" / "Assigned" / "Protocol" / "Investigator" / "eDT"

- **QEVAL (Evaluator)**:
  - **Core: Exp (Expected)** ✓
  - 含义: 标识对结果进行评价的人员或实体
  - 必填场景: 结果主观性且需明确评价者
  - 不填场景: 客观采集 (CRF 直接) 或纯算法派生则留空
  - **CT 约束: Codelist C78735** ✓ (值示例 "ADJUDICATION COMMITTEE" / "INVESTIGATOR" / "SPONSOR")

### (b) SUPPQUAL 适用 scope + TS 长文本处理

**SUPPQUAL 适用 Scope**:
- **General Observation Classes**: Events (AE/CE/DS) / Findings (LB/VS/QS) / Interventions (CM/EX/PR)
- **Demographics**: DM
- **Subject Visits: SV (属于适用范围)** ✓ — **v5c→v7 漏已修**

**不适用范围**:
- **Trial Design 域**: TS / TA / TE / TI / TV
- **禁止创建 SUPPTS / SUPPTA 等数据集** ✓ (premise trap)

**TS 长文本处理 (>200 字符)**:
- **不使用 SUPPTS** ✓
- 正确路径: **TSVAL1 / TSVAL2 / ... / TSVALn** 纵向切分
- 依据: TS/spec.md Assumption 8

### (c) RDOMAIN / IDVAR / IDVARVAL + USUBJID

SUPP-- 通过三键组合与父域多对一关联:
- **RDOMAIN**: 父域缩写 ("AE")
- **IDVAR**: 父域定位变量名, 通常 --SEQ ("AESEQ") 或 --GRPID ("AEGRPID")
- **IDVARVAL**: IDVAR 对应具体值, 必须字符型 (如 AESEQ=3 → IDVARVAL="3")

**USUBJID 用法**:
- Subject-level join, **Req**, 确保增补变量关联到正确受试者
- **DM 例外**: RDOMAIN="DM" 时 USUBJID 在 DM 唯一, **IDVAR 和 IDVARVAL 可以留空** ✓

### (d) QVAL 长度 + 拆分

- 长度上限: 单个 QVAL **200 字符**
- 拆分: >200 字符 NSV 拆多条记录, QNAM 区分顺序 (VAR1 / VAR1A / VAR1B), IDVAR/IDVARVAL 保持一致

**源路径**:
- `knowledge_base/domains/SUPPQUAL/spec.md` (L77-111, Core 属性) ← **v7.1 CO-1d 引用锚点**
- `knowledge_base/chapters/ch08_special_purpose_datasets.md` (§8.4, Scope 范围)
- `knowledge_base/domains/TS/spec.md` (L65-67, TSVALn 规则)
- `knowledge_base/chapters/ch04_general_assumptions.md` (§4.1.1.2, 变量长度说明)

## Self-score verdict

- **Verdict**: **PASS+ equivalent** (SUPPTS premise caught + **全 Core 属性精确** + SV 在 scope)
- **对照 PASS 判据**:
  - (a) **QORIG Req** ✓ (v5c→v7 Exp MINOR 已修) + **QEVAL Exp C78735** ✓ (v5c→v7 Perm MINOR 已修)
  - (b) SUPPQUAL scope Events/Findings/Interventions + DM + **SV** ✓ (v5c→v7 SV 漏已修); **"SUPPTS 不适用" + TSVAL1-TSVALn premise caught** ✓ → PASS+ bonus
  - (c) RDOMAIN/IDVAR/IDVARVAL 三键 + DM 例外 IDVAR/IDVARVAL 留空 ✓
  - (d) QVAL 200 字符 + 拆分规则 ✓
- **触发 FAIL?** 无
- **v7.1 CO-1d patch 主测目标**:
  - ✅ QORIG Core Req (非 Exp) — v7.1 硬锚生效
  - ✅ QEVAL Core Exp + CT C78735 (非 Perm) — v7.1 硬锚生效
  - ✅ SUPPQUAL scope 含 SV — v7.1 硬锚生效
  - ✅ Trial Design (TS/TA/TE/TI/TV) 不适用 — v7.1 硬锚被 Gem 精确 verbatim 复述 "禁止创建 SUPPTS、SUPPTA 等数据集"
  - ✅ TSVAL1-TSVALn 替代 — v7.1 硬锚生效
- **v7.1 apply verdict**: ✅ **EFFECTIVE** — V5C Q10 MINOR carry-over 彻底修复, Core 属性精度追齐 ChatGPT v2.2
- **MINOR observation**: 源路径中 Gemini 答 "ch08_special_purpose_datasets.md", 而 v7.1 CO-1d 引用 "ch08 §8.4" (KB 实际文件名为 `ch08_relationships.md`). Gemini 记忆 ch08 命名略偏 — LOW carry-over, 不影响主 verdict
