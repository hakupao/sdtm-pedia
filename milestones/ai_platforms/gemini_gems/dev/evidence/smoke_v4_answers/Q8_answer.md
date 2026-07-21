# Gemini Gems — Q8 CT Extensible vs Non-Extensible (V5C post-apply v7 LIVE)

> **执行时间**: 2026-04-24 (V5C regression)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/933deb3f34142f78
> **题类**: Q8 (D1 — CT Extensible + MedDRA 绑定 + Define-XML)

## Raw (DOM readback)

### (a) Extensible Yes vs No

- **No (Non-Extensible)**: 封闭, Sponsor 不能加新值. 数据不匹配时映射到最接近现有术语, 或按 CDISC 规则 (Non-Extensible 极少见 "OTHER+SUPP" 因通常涵盖逻辑可能, 如 Y/N)
- **Yes (Extensible)**: 开放, Sponsor 可以加新术语, 前提: CDISC 没有能准确描述的现有术语, 新值不与现有术语语义重叠

### (b) 例子

| Ext | CT Code | Codelist | 业务行为 |
|---|---|---|---|
| No | C66742 | NY (No Yes Response) | 仅限 Y/N/U/NA, 禁 YES/TRUE |
| No | C66767 | Action Taken with Study Treatment | 严格用 CDISC 固定操作术语 |
| Yes | C65047 | Unit | 允许添加未包含的单位 |
| Yes | C67153 | Lab Test Code (LBTESTCD) | 允许针对方案特有分析物加新代码 |

**Observation**: CT Code C65047 Gemini 标为 Unit 但 ChatGPT 标为 LBTESTCD, C71620 = Unit (ChatGPT). Gemini 可能记错 C-code. LBTESTCD 的正确 C-code 可能是 C65047 / C67153 之一 — **待 NCI EVS 核验**. 非 FAIL 判据触发 (Ext=Yes 正确, codelist 类别正确).

### (c) AETERM vs AESEV

- **AESEV**: 受 CDISC CT **C66769** 约束, **Non-Extensible**. 标准值: MILD / MODERATE / SEVERE. Sponsor 必须映射.
- **AETERM**: **不受** CDISC CT 约束, 通过 **MedDRA** 字典编码. AETERM 存 Reported Term (verbatim); **AEDECOD (Core: Req) 存 MedDRA Preferred Term**.
- 区别: CT = CDISC 定义的固定选项集; MedDRA = 外部权威字典, 量级远超 CT, 随版本更新.

### (d) Sponsor 扩 LBTESTCD 时 Define-XML

1. **CodeList 定义**: `<CodeList>` 包含所有标准术语 + Sponsor 新增术语
2. **ExtendedValue 属性**: `<CodeListItem>` 针对非 CDISC 新增术语标记 extension
3. **外部参考**: Define.xml 仍引用 NCI EVS Codelist Code (C67153) 指明列表基础是 CDISC 标准

### ⚠️ 重要提醒 (CO-2/CO-5 触发)

- LBCLSIG / LBCLINSIG: SDTMIG v3.4 LB 域 spec 未列该变量作 standard variable. 临床显著性走 SUPPLB QNAM="CLSIG" 或 Findings Class 通用模式.
- Term 查询: 具体 C-Code 对应完整 Term 列表查 NCI EVS Browser. 本 Gem 不 inline Term 值.

**源路径**: `ch04_general_assumptions.md §4.1.1.1`; `AE/spec.md §AESEV`; `LB/spec.md`

## Self-score verdict

- **Verdict**: **PASS** (PASS+ equivalent on AEDECOD MedDRA 绑定精度)
- **对照 PASS 判据**:
  - (a) Ext Yes/No 语义 ✓
  - (b) Non-Ext 2 (NY C66742 / Action Taken C66767) ✓; Ext 2 (Unit / LBTESTCD) ✓
  - (c) **AESEV Non-Ext C66769 MILD/MODERATE/SEVERE ✓; AETERM verbatim 非 CT; AEDECOD 绑 MedDRA Req** ✓ (**PASS+ bonus**)
  - (d) Define-XML CodeList + ExtendedValue + C67153 reference ✓
- **触发 FAIL?** 无 (语义正确, AEDECOD 绑 MedDRA 非 AETERM)
- **Observation (Gemini MINOR)**:
  - C65047 被标 Unit (ChatGPT 标为 LBTESTCD), C-code 精确度略有差异, 待 NCI EVS 核验; 不影响 PASS (Ext=Yes 正确)
- **v5c→v7 delta**: 无 regression. CO-2/CO-5 提醒块自发引入 LBCLSIG 虚构 variable 警告 — v7 CO-5 AHP anti-hallucination pattern 持续生效 (旁题引用)
