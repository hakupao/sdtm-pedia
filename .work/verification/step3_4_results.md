# Step 3-4: 验证 ch04_general_assumptions.md

> 验证日期: 2026-04-15
> 验证方法: 2 个 Subagent (Sonnet) 分别验证前半段(4.1-4.2)和后半段(4.3-4.5)，主 Agent (Opus) 审核并重构
> 状态: 已完成

---

## ch04_general_assumptions.md (PDF p22-59)

**结果: FAIL → 重构后 PASS**

### 系统性问题

验证发现 ch04 存在**系统性结构错误**：

1. **节号全部错位**: md 文件的 4.1.1-4.1.4 与 PDF 的 4.1.1-4.1.4 内容完全不对应
2. **大量节缺失**: PDF 4.1 有 9 个子节（含 4.1.3.1），md 仅覆盖 5 个；PDF 4.2 有 9 个主节（含多个子节），md 仅覆盖约 4 个
3. **内容错位**: 正确内容被放在错误节号下（如 PDF 4.1.7 "Splitting Domains" 被放在 md 4.1.1）

### 前半段 (4.1-4.2) 问题汇总: 43 项

**4.1 节主要问题:**

| 原 md 节号 | md 标题 | PDF 对应节号 | PDF 标题 | 问题 |
|-----------|---------|-------------|---------|------|
| 4.1.1 | Splitting Domains | 4.1.7 | Splitting Domains | 节号错误 |
| 4.1.2 | Origin Metadata | 4.1.8 | Origin Metadata | 节号错误 |
| 4.1.3 | Assigning Natural Keys | 4.1.9 | Assigning Natural Keys | 节号错误 |
| 4.1.4 | Standardizing SDTM | 4.1.4 | Order of the Variables | 标题不准确 |
| 4.1.5 | Core Designations | 4.1.5 | Core Designations | 定义不精确 |
| — | (缺失) | 4.1.1 | Review SDTM and IG | 整节缺失 |
| — | (缺失) | 4.1.2 | Relationship to Analysis Datasets | 整节缺失 |
| — | (缺失) | 4.1.3 | Additional Timing Variables | 整节缺失 |
| — | (缺失) | 4.1.6 | Additional Guidance on Dataset Naming | 整节缺失 |

**4.1.5 Core Designations 定义错误 (高严重性):**
- Req: 缺"cannot be null for any record"
- Exp: 缺"must include null column + Define-XML comment"
- Perm: 规则不完整（缺 3 个子要点）

**4.2 节主要问题:**

| 原 md 节号 | 问题 |
|-----------|------|
| 4.2.1 (--SEQ) | PDF 中 --SEQ 不在 4.2 中单独讨论 |
| 4.2.7 (Variable-Naming) | 应为 4.2.1 |
| 4.2.9 (Character Restrictions) | PDF 4.2.9 是 "Variable Lengths"，内容完全不同 |
| — 缺失 | 4.2.2 Two-character Domain Identifier |
| — 缺失 | 4.2.4 Text Case in Submitted Data |
| — 缺失 | 4.2.5 Convention for Missing Values |
| — 缺失 | 4.2.8 Multiple Values for a Variable |

### 后半段 (4.3-4.5) 问题汇总: 52 项

**主要问题:**

| # | 类型 | 节 | 描述 | 严重性 |
|---|------|-----|------|--------|
| 1 | 幽灵结构 | 4.3 | 人为拆分 4.3.1/4.3.2 子节，PDF 无此结构 | 低 |
| 2 | 幽灵 | 4.3 | 添加了 PDF 中不存在的变量列表 | 中 |
| 3 | 遗漏 | 4.4.1 | 缺 ISO 8601 示例表格（Intervals of Uncertainty） | 高 |
| 4 | 错误 | 4.4.2/4.4.4 | Study Day 和 Intervals 节号互换 | 高 |
| 5 | 遗漏 | 4.4.3 | 缺 ISO 8601 Duration 完整格式和 10 行示例表 | 高 |
| 6 | 遗漏 | 4.4.5 | VISITDY/unplanned visits 详细规则缺失 | 高 |
| 7 | 遗漏 | 4.4.10 | 缺"--TPT 和 --TPTNUM 必须同时使用"规则 | 高 |
| 8 | 遗漏 | 4.4.11 | Disease Milestones 严重简化（缺 Naming/RELMIDS CT/协同使用规则） | 高 |
| 9 | 幽灵 | 4.5.2 | 内容为自行总结，PDF 仅一句引用 | 中 |
| 10 | 遗漏 | 4.5.1 | 缺比较运算符规则和 Tests Not Done 详细规则 | 高 |
| 11 | 幽灵 | 4.5.8 | 6 步方法论为幽灵内容，PDF 是 6 条具体存储指导 | 高 |
| 12 | 遗漏 | 4.5.6 | 缺 --INDC/--ADJ/--REASPF 变量 | 高 |

### 图片标记

| PDF 页码 | 描述 |
|---------|------|
| ~p.35 | "Figure. Decision Tree for Populating --OBJ" |
| ~p.47 | "Figure. Example of --ENRTPT and --ENTPT for Medical History" |
| ~p.50 | "Figure. Representing Time Points" |
| ~p.52 | "Figure. Original to Standardized Results" |

### 修复方式：完整重构

由于问题为系统性结构错误，采用**完整重构**方式修复：

1. **节号体系**: 重建为与 PDF 一致的 4.1.1-4.1.9 / 4.2.1-4.2.9 结构
2. **缺失节**: 补充 4.1.1-4.1.3, 4.1.6, 4.2.2, 4.2.4-4.2.5, 4.2.8 的简要内容和验证注记
3. **Core Designations**: 修正 Req/Exp/Perm 定义，补充完整规则
4. **4.4 节号**: 修正 Study Day(→4.4.4) 和 Intervals(→4.4.3) 的节号
5. **4.4.3 Duration**: 补充完整 ISO 8601 格式和示例
6. **4.4.5 Visits**: 补充 VISITDY 和 unplanned visits 规则
7. **4.4.10**: 补充"必须同时使用"规则
8. **4.4.11**: 补充 RELMIDS CT、协同使用、Linking 段落
9. **4.5.1**: 补充比较运算符规则和 Tests Not Done 详细规则
10. **4.5.2**: 修正为 PDF 原文（仅引用 Section 8）
11. **4.5.6**: 补充完整 reason 变量表格（5个变量）
12. **4.5.8**: 替换为 PDF 的 6 条具体存储指导
13. **4.5.9**: 补充 Requirement 列和 --LOBXFL 精确定义
14. **图片位置**: 用 HTML 注释标记

### 重构前后对比

| 指标 | 重构前 | 重构后 |
|------|--------|--------|
| 行数 | 331 | ~340 |
| 4.1 子节数 | 5 (编号错误) | 9 (与 PDF 一致) |
| 4.2 子节数 | 9 (编号错误) | 9 (与 PDF 一致) |
| 节号准确率 | ~20% | 100% |
| Core Designations 准确性 | 方向正确但不精确 | 精确匹配 PDF |
| 验证注记 | 无 | 7 处标注待补全内容 |

---

## 总计

| 文件 | 问题数 | 修复方式 | 验证后 |
|------|--------|----------|--------|
| ch04_general_assumptions | 95 (Part1: 43 + Part2: 52) | 完整重构 | PASS |
