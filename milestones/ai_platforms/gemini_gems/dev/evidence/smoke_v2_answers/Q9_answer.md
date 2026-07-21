# Q9 — Gemini SDTM Expert answer

> URL: https://gemini.google.com/u/1/gem/3b572e310813/f32e029135f71e1a
> Mode: Pro
> Run: 2026-04-21

## 原题
SUPPAE (Supplemental Qualifiers for AE) 的作用是什么? 什么情况下应该走 SUPPAE 而不是直接加 AE 域变量? 请举一个典型例子, 给出 QNAM / QLABEL / QVAL 三字段的完整示例 (场景自选, 无需 NCI Code).

## 答案全文

### 结论

SUPPAE (Supplemental Qualifiers for AE) 的主要作用是存储无法在 SDTMIG 标准 AE 域规范中找到对应变量的非标 Qualifier（限定词）数据。

### 应使用 SUPPAE 而不是直接在 AE 域加变量的情况

- **非标准变量**：该信息在 SDTMIG v3.4 AE 域的 Spec 中不存在（例如，特定的医学分类、赞助商自定义的标志位）。
- **非 Timing/Identifier 变量**：如果该变量既不是标准 Qualifier，也不是通用的 Timing 或 Identifier 变量，则必须放入 SUPP-- 中。
- **遵循"域规范优先"原则**：SDTM 结构是固定的，除非是 SDTMIG 明确允许添加的通用变量（如 --STRESC 等），否则任何自定义扩展属性都应走补充域。

### 依据

**通用规则 (General Assumptions)**：根据 SDTMIG Chapter 4, Section 8.4.1，补充限定词（Supplemental Qualifiers）用于捕获那些不符合域模型定义、但在原数据中存在且对分析有意义的变量。

**AE 域限定**：AE 域是一个 Events 类别的域。只有在该域 Spec 中列出的变量（如 AESEV, AESER, AEOUT 等）才能作为域变量。如果 EDC 收集了如"该 AE 是否导致研究药物永久停药"（假设已有 AEACN 但需要更细化的标志），且没有标准变量对应，则需进入 SUPPAE。

### 典型例子：AE 是否为注射部位反应 (Injection Site Reaction)

**场景**：临床方案规定需识别某些 AE 是否属于"注射部位反应"，EDC 系统中有一个 Checkbox 字段。由于 AE 域中没有 AEINJR 或类似的 Injection Site 标志位变量，该数据必须映射到 SUPPAE。

**SUPPAE 记录示例**：

| 变量名 | 示例值 | 说明 |
|--------|-------|------|
| STUDYID | ABC-101 | 研究编号 |
| RDOMAIN | AE | 关联的域名 |
| USUBJID | 001-002 | 受试者唯一标识 |
| IDVAR | AESEQ | 关联变量名（通常用序列号关联）|
| IDVARVAL | 5 | 关联的 AESEQ 值 |
| QNAM | ISREAC | Qualifier Variable Name (自定义，不超过 8 位) |
| QLABEL | Injection Site Reaction | Qualifier Variable Label (标签描述) |
| QVAL | Y | Data Value (实际收集到的值) |
| QORIG | CRF | 数据来源 |
| QEVAL | INVESTIGATOR | 评价者 |

**源路径**:
- 规则依据: knowledge_base/chapters/ch04_general_assumptions.md (Section 8.4 Supplemental Qualifiers)
- 域模型: knowledge_base/domains/AE/spec.md (用于确认变量是否存在于标准域)
- 业务逻辑: 04_business_scenarios_and_cross_domain.md §1.10 (SUPP-- vs RELREC 选择)

**注意**：如需查询具体的 QNAM 是否有 CDISC 建议的 Controlled Terminology（通常存储在 Non-extensible codelist 中），请访问 NCI EVS Browser: https://evsexplore.semantics.cancer.gov/evsexplore/。
