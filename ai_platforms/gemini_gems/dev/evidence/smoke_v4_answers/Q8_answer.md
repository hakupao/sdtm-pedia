# Gemini Q8 answer — CT Extensible + MedDRA binding

**Verdict**: **PARTIAL (0.5)** — (a)(c)(d) 对, 但 (b) C66767 错分 Ext=Yes (实际 Non-Ext) + C66742 只列 Y/N (缺 U/NA)

## (a) Extensible 语义 ✓
- Non-Ext (No): 封闭, sponsor 不得加自定义值, 必须严格用 CDISC 发布值, 违规 → 监管拒绝
- Ext (Yes): 开放, CDISC 未覆盖时可在 Define-XML 声明扩, 前提不冲突

## (b) Codelist 示例 ⚠️ 部分错误
**Non-Extensible (给出 2 个)**:
- C66742 (NY): 仅 "Y"/"N" ← **不完整** (CDISC 发布值含 N/Y/U/NA 4 个)
- C66728 (Relation to Reference Period): BEFORE/DURING/AFTER/ONGOING — 正确分类为 Non-Ext

**Extensible (给出 2 个)**:
- **C66767 (Action Taken with Study Treatment) ← ❌ 错误**: 实际 **Non-Extensible** (CDISC 发布且 ChatGPT/Claude 都列为 Non-Ext 例子)
- C65047 (Laboratory Test Code) ← ✓ 对

## (c) AETERM vs AESEV ✓
- **AESEV (Non-Ext)**: CDISC CT C66769, MILD/MODERATE/SEVERE
- **AETERM (无 CT 绑定)**: Topic 变量, 存 verbatim, 不绑任何 CDISC CT
- AEDECOD 绑 MedDRA PT, AELLT 绑 MedDRA LLT (外部字典, 非 CDISC CT)

## (d) 扩 LBTESTCD Define-XML 操作 ✓ (简明版)
1. 声明自定义值: CodeList 节点下 custom EnumeratedItem/CodeListItem
2. 提供对应 LBTEST 描述, Value-level Metadata 可溯源
3. 指定 Origin (CRF/Assigned), Comment 解释扩展原因
4. 外部字典引用 (如 LOINC) 指明字典名+版本

## 源路径
- ch04 §4.3 (Coding and Controlled Terminology)
- 04_business_scenarios_and_cross_domain.md §1.15

## 评分要点
- ✓ (a) 语义正确
- ✗ **(b) C66767 误分类** (Ext=No 误为 Yes) + C66742 只 2/4 值
- ✓ (c) AETERM 无 CT 绑定 + MedDRA 外部字典 + AEDECOD/AELLT 正确
- △ (d) 4 点框架正确但缺 Define-XML 2.1 具体机制 (nci:ExtCodeID / def:IsNonStandard)
- △ 无 LBTESTCD ≤ 8 字符 / LBTEST ≤ 40 字符长度约束
- △ 无 AETOXGR 作 AESEV Non-Ext 扩的替代方案

## R2 改 prompt 建议
system_prompt v5 加锚点: "C66767 Action Taken with Study Treatment = Non-Extensible; C66742 NY values = Y/N/U/NA (4 values, not 2)"

## 与其他平台对比
- ChatGPT PASS+: 5 Non-Ext + 3 Ext 例子, C-code + 值全对, Treatment Intent 作 Ext
- Claude PASS+: 4+4 例子 + 4 层 CT 绑定语义总表 + Define-XML 2.1 具体机制 + AETOXGR 替代
- Gemini PARTIAL: (a)(c)(d) 对, (b) 错一个 + 一个不完整
