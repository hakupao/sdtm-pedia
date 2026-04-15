# Step 3-1: model/ 页码映射 + 验证 01, 04

> 验证日期: 2026-04-14
> 验证方法: 逐段对照 SDTM_v2.0.pdf 原文，检查完整性（无遗漏）和准确性（无错误）
> 状态: 已完成

---

## 页码映射（SDTM_v2.0.pdf，共 74 页）

根据 PDF 目录（第 2-3 页）确认：

| 文件 | PDF 章节 | 页码范围 | 页数 |
|------|---------|---------|------|
| 01_concepts_and_terms.md | Ch 2: Model Concepts and Terms | 8-10 | 3 |
| 02_observation_classes.md | Ch 3.1: General Observation Classes | 11-39 | 29 |
| 03_special_purpose_domains.md | Ch 3.2: Special-Purpose Domains | 40-49 | 10 |
| 04_associated_persons.md | Ch 4: Associated Persons Data | 50 | 1 |
| 05_study_level_data.md | Ch 5: Study-Level Data | 51-63 | 13 |
| 06_relationship_datasets.md | Ch 6: Relationships | 64-69 | 6 |

---

## 01_concepts_and_terms.md (PDF p8-10)

**结果: FAIL → 修复后 PASS**

### 发现的问题

| # | 类型 | 描述 | 严重性 |
|---|------|------|--------|
| 1 | 遗漏 | 缺少开篇示例（"Subject 101 had an adverse event of mild nausea..."） | 低 |
| 2 | 遗漏 | 缺少 metadata/Define-XML 引用段落（p9 首段） | 中 |
| 3 | 遗漏 | 缺少变量可在不同数据集中扮演不同角色的说明（ARMCD 例子、--MODIFY 例子） | 中 |
| 4 | 遗漏 | 缺少 DOMAIN/RDOMAIN 使用规则段落（哪些数据集包含 DOMAIN/RDOMAIN） | 中 |
| 5 | 遗漏 | 缺少 SAS v5 transport / FDA 格式约束段落 | 中 |
| 6 | 遗漏 | Section 2.2 末尾缺少 "definition-like information has been removed for variables which have approved definitions" 从句 | 低 |

### 无错误的部分

- Concept Map 树形图：准确反映了 PDF 中的结构图，所有节点和层级关系正确
- 5 种变量角色（Identifier/Topic/Timing/Qualifier/Rule）：内容准确
- 5 种 Qualifier 子类（Grouping/Result/Synonym/Record/Variable）：描述准确，KB 额外添加了变量名示例（--CAT, --ORRES 等），这些来自 PDF 其他章节的变量表，经核实准确
- Section 2.2 Table Structure 列表：11 列全部列出，描述准确
- Domain Codes 小节：内容来自 p9 散布的信息综合整理，内容准确

### 修复内容

1. 在开篇段落后补充 PDF 示例
2. 在 Section 2.1 开头补充 metadata/Define-XML 引用
3. 补充变量角色跨数据集差异说明（含 ARMCD、--MODIFY 例子）
4. 补充 DOMAIN/RDOMAIN 使用规则
5. 补充 SAS v5 transport 格式约束
6. 补全 Section 2.2 末尾从句

---

## 04_associated_persons.md (PDF p50)

**结果: FAIL → 修复后 PASS**

### 发现的问题

| # | 类型 | 描述 | 严重性 |
|---|------|------|--------|
| 1 | **错误** | RSUBJID 标签写为 "Related Subject Identifier"，PDF 原文为 "Related Subject or Pool Identifier" | 高 |
| 2 | **错误** | SREL 标签写为 "Subject Relationship"，PDF 原文为 "Subject, Device, or Study Relationship" | 高 |
| 3 | 遗漏 | 开篇定义缺少 "associated with a study, a particular study subject, or a device used in the study" 精确措辞 | 中 |
| 4 | 遗漏 | 缺少 SREL 条件描述（RSUBJID populated → subject/pool 关系；RDEVID populated → device 关系；两者为空 → study 关系） | 中 |
| 5 | 遗漏 | 缺少末尾段落关于 Associated Persons Relationships dataset 的说明 | 中 |

### 无错误的部分

- AP 域三条基本规则（Identifier assumptions / AP prefix / APID required）：准确
- SDTMIG-AP 引用：正确提及
- 变量表结构：APID 和 RDEVID 基本描述准确
- APDM 示例虽非 PDF 原文但符合 AP 命名规则，保留

### 修复内容

1. 修正 RSUBJID 标签为 "Related Subject or Pool Identifier"
2. 修正 SREL 标签为 "Subject, Device, or Study Relationship"
3. 修正开篇定义措辞
4. 补充 SREL 条件描述
5. 补充 AP Relationships dataset 段落
