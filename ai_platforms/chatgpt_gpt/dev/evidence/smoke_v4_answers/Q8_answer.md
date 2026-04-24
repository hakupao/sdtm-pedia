# ChatGPT GPTs — Q8 CT Extensible vs Non-Extensible (V5C post-apply v2.2 LIVE)

> **执行时间**: 2026-04-24 (V5C regression)
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69ead717-1634-83a8-99a6-ec44df9aad9d
> **题类**: Q8 (D1 — CT Extensible + MedDRA 绑定 + Define-XML)

## Raw (DOM readback)

**结论**: Extensible=Yes 不是"随便填"; 表示 codelist 不是封闭全集, sponsor 可在必要时加非 CDISC 标准值. Extensible=No 封闭, 提交值必须完全按 CDISC CT 规定, 不能自扩.

### (a) Extensible=Yes vs No

| 属性 | 语义 | Sponsor 能否加 |
|---|---|---|
| No | 封闭, 预期完整值集 | **不能加**. 必须用 CDISC Submission Value (AESEV 只 MILD/MODERATE/SEVERE) |
| Yes | 开放, CDISC 不穷尽 | **可以加**, 但前提: CDISC 已有概念必须用 CDISC 标准值; 只有 CDISC 没合适时才 sponsor-defined, Define-XML 声明 |

Define-XML 要求: study permissible value set 所有值都列, 即使数据未出现; 大小写按 source codelist 一致.

### (b) 例子

| Ext | CT Code | 变量 | 典型值 |
|---|---|---|---|
| No | C66769 | AESEV | MILD, MODERATE, SEVERE |
| No | C66768 | AEOUT | FATAL, NOT RECOVERED/NOT RESOLVED, RECOVERED/RESOLVED, ...  |
| No | C66742 | NY | N, NA, U, Y |
| Yes | C65047 | LBTESTCD | CDISC CT 不可能穷尽 |
| Yes | C71620 | --ORRESU/--STRESU | 单位列表不断扩展 |

### (c) AETERM 语义 vs AESEV

| 变量 | 角色 | CDISC CT 枚举? | 实际规则 |
|---|---|---|---|
| AETERM | Topic; 报告原始 AE verbatim term | **不是** CDISC CT | 来自 CRF/报告, 自由文本或预设 AE term |
| AEDECOD | Synonym Qualifier; 字典派生 | **不是** CDISC CT | 来自 **MedDRA Preferred Term**; Define-XML 说明外部字典名称+版本 |
| AESEV | Qualifier; 严重程度 | **是** CDISC CT C66769 Non-Ext | 只能 MILD / MODERATE / SEVERE |

关键: AETERM = 收集医学事件文本, 非 CDISC CT 闭合; AESEV = CDISC CT 约束 + Non-Ext. Investigator 写 "very bad headache" 可进 AETERM; 但 AESEV 不能 "VERY BAD", 必须 MILD/MODERATE/SEVERE.

### (d) Sponsor 扩 LBTESTCD 时 Define-XML 要做

LBTESTCD = C65047 Ext=Yes:
1. Define-XML 为 LBTESTCD 提供 codelist / permissible value set, 列本研究允许值 (即使数据未出现)
2. CDISC 已存 test code 必须用 CDISC Submission Value + NCI/CDISC CT 信息 (不改拼写/大小写/含义)
3. Sponsor 新增 LBTESTCD 作 sponsor-defined codelist item 声明; **不要伪造 NCI C-code**
4. 给 LBTESTCD (8 char) 与 LBTEST (40 char max) 一一对应
5. 有外部字典 (如 LOINC) 用 LBLOINC 或 Define-XML external codelist attributes 描述 dictionary name/version

**源路径**: `<!-- ch04_general_assumptions.md -->`; `<!-- terminology/core/ae.md -->` (C66769/C66768); `<!-- terminology/core/general_part4.md -->` (C66742); `<!-- terminology/core/lb_part2.md -->` (C65047); `<!-- terminology/core/general_part5.md -->` (C71620); `<!-- AE/spec.md + assumptions.md -->`

## Self-score verdict

- **Verdict**: **PASS** (PASS+ equivalent on AETERM/AEDECOD MedDRA 绑定精度)
- **对照 PASS 判据**:
  - (a) Ext Yes/No 语义 ✓
  - (b) Non-Ext 3 例 (AESEV/AEOUT/NY) 超 2 要求 ✓; Ext 2 例 (LBTESTCD/Unit) ✓ (v4.0 判据列 LBNRIND Ext=Yes 作可选, 本答未提但 LBTESTCD 达标)
  - (c) **AETERM verbatim 非 CT + AEDECOD 绑 MedDRA** 明确分离 ✓ (**PASS+ bonus**: 精确识别 "AETERM 不绑 MedDRA, MedDRA 绑 AEDECOD")
  - (d) Define-XML 所有 5 点 (values 列, sponsor-defined, 不伪造 NCI, LBTEST 40-char, LOINC) ✓
- **触发 FAIL?** 无 (未反 Extensible 语义, AESEV 未说 Extensible, AETERM 未说绑 CDISC CT)
- **加分**:
  - MedDRA 绑 AEDECOD 非 AETERM (PASS+ bonus 判据命中)
  - "very bad headache" 具体业务示例
  - LOINC 绑 LBLOINC external codelist attributes
- **v5c→v2.2 delta**: 无 regression; 深度超 N5.2 baseline, 特别是 AETERM/AEDECOD 字典绑定位置
