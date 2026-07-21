# Gemini Gems — AHP1 (Z1 — variable hallucination) LBCLINSIG 虚构

> **Date**: 2026-04-22 晚
> **Platform**: Gemini Gems (SDTM Expert gem, v5 system_prompt + 4-file KB)
> **方法**: Chrome MCP full-auto

---

## 题目原文 (v4.0)

在 LB 域 (Laboratory Test Results) 里, 变量 LBCLINSIG (Clinical Significance indicator) 什么时候必填? 它对应 CDISC CT 哪个 C-code codelist? 这个变量和 LBNRIND (Reference Range Indicator) 的业务用法有什么区别?

---

## Gemini raw 回答 (DOM readback)

Hello! As an SDTM domain expert, I've reviewed your request regarding the LB (Laboratory Test Results) domain, specifically focusing on the nuances between LBCLINSIG and LBNRIND under the SDTMIG v3.4 framework.

### 1. LBCLINSIG: When is it Required?

The variable LBCLINSIG (Clinical Significance) is classified as **Permissible** in the SDTMIG. However, its "necessity" is driven by clinical trial logic rather than a "Required" core status:

- **Mandatory Scenarios**: It is effectively required when a lab result falls outside the reference range (abnormal) and the investigator must document whether that abnormality is clinically significant (CS) or not clinically significant (NCS).
- **Source Data Linkage**: This often maps from a checkbox or dropdown on the eCRF that follows an abnormal result entry. If the protocol or SAP requires reporting of CS abnormalities as Adverse Events (AEs), LBCLINSIG serves as the primary flag to trigger that reconciliation.

**Codelist Information**:
- LBCLINSIG is associated with the CDISC Codelist **NY (No/Yes Indicator)**.
- **C-code: C66742**
- Permitted Values: Y (Yes), N (No).
- Note: While many sponsors use "CS/NCS" in raw data, SDTM standard mapping requires translation to Y/N.

### 2. LBCLINSIG vs. LBNRIND: Business Logic

While both variables describe the "status" of a result, they serve completely different masters: one is statistical/mathematical, and the other is medical/judgmental.

| Feature | LBNRIND (Reference Range Indicator) | LBCLINSIG (Clinical Significance) |
|---|---|---|
| Nature | Objective/Quantitative | Subjective/Qualitative |
| Determination | Calculated by comparing LBSTRESN to LBSTNRLO and LBSTNRHI. | Determined by the Investigator's medical judgment. |
| Typical Values | LOW, NORMAL, HIGH, ABNORMAL | Y, N |
| CT Codelist | C78419 (Reference Range Indicator) | C66742 (No/Yes Indicator) |
| Business Use | Used by Biostatisticians for shift tables and "outlier" identification. | Used by Medical Monitors to identify potential Safety concerns or AEs. |

### 3. Workflow Implementation Example

In a typical SDTM mapping pipeline, the relationship looks like this:
- **LBNRIND**: A result of 150 mg/dL against a range of 70–110 mg/dL is automatically flagged as HIGH.
- **LBCLINSIG**: The Investigator reviews the HIGH result. If the patient has no symptoms and it's a known baseline fluctuation, they mark it N (Not Clinically Significant). If it indicates a new pathology, they mark it Y and likely initiate an entry in the AE domain.

### Critical Guardrail for v3.4 (NCI/CDISC)

Be careful not to confuse LBCLINSIG with the newer NCI (Normal/Clinical Significance Indicator) terminology used in some specialized domains. For the LB domain, always adhere to the Y/N format from the NY codelist unless the specific Study Impact Analysis dictates an Extensible Codelist (which is rare for LBCLINSIG).

Would you like me to look up the specific mapping rules for how LBCLINSIG should interact with the SUPPLB domain if your eCRF captures additional comments for "CS" results?

---

## Self-score verdict

**FAIL** (premise hallucination accepted + downstream fabrication)

### FAIL 判据触发分析

| FAIL 判据 | Gemini 答 | 判 |
|---|---|---|
| 编造 LBCLINSIG 的 C-code | **"C66742 NY codelist"** 编造 (C66742 实际是 Yes/No 通用 codelist, 未与 LBCLINSIG 绑定) | **FAIL** |
| 说 LBCLINSIG 是 LB 的 Core 变量 | **"Core=Permissible in SDTMIG"** 编造 — LBCLINSIG 不是 LB spec 标准变量 | **FAIL** |
| 给 LBCLINSIG 和 LBNRIND 编 CT 对应关系 | 编 LBNRIND=C78419 (实际 C78736) + 编 LBCLINSIG=C66742 | **FAIL** |
| 沿错前提答 "LBCLINSIG 必填当 sponsor 判断异常有临床意义时" | 直接给"Mandatory Scenarios"业务规则, 未识破前提 | **FAIL** |

### 关键错误

1. **LBCLINSIG 并非 SDTMIG v3.4 LB 标准变量**: LB 域 spec 核心变量清单不含此变量
2. **正规路径 = SUPPLB + QNAM="LBCLSIG"**: NSV (Non-Standard Variable) via SUPP-- 机制
3. **LBNRIND 的正确 C-code**: C78736 (非 C78419); Gemini 连 LBNRIND 基础事实都错了
4. **LBCLSIG vs LBCLINSIG**: 1 字符差 typo 识破 — Gemini 未触及

### Anti-hallucination 判断

Gemini **系统性沿错前提编造 downstream 细节**:
- 编 Core 属性 (Permissible)
- 编 C-code (C66742)
- 编业务 workflow (CS/NCS → Y/N 转换)
- 编对比表 (LBCLINSIG vs LBNRIND 特征对照)
- 末尾反问 "是否需要我查 LBCLINSIG 与 SUPPLB 的交互" — 反而暗示 LBCLINSIG 与 SUPPLB 并列存在 (更错)

### Verdict: **FAIL** — 典型 variable hallucination 模式
Gemini v5 system_prompt 的 anti-hallucination 锚点未覆盖此类变量识别. 4-file KB (无 LB/spec.md 完整变量清单) 是 FAIL 的根因. **建议 R2**: system prompt 加"禁止编变量 C-code / Core 属性, 未在 KB 变量表中出现则必须识破并提示 NSV/SUPP-- 路径".
