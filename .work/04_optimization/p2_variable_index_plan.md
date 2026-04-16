# P2: 变量级反向索引 — 执行计划

> 创建日期: 2026-04-16
> 状态: 待审核
> 前置: Phase 5 已完成，293 文件已验证

---

## 1. 目标

创建 `knowledge_base/VARIABLE_INDEX.md`，提供**变量名 → 出现在哪些 domain → 定义位置**的反向查找能力。

**解决的问题**：当前 AI 查询某个变量时，只能逐文件搜索。有了反向索引后，AI 可以直接查表定位。

---

## 2. 数据摸底结果

| 指标 | 数值 |
|------|------|
| spec.md 文件数 | 63 |
| 变量条目总数 | 1,917 |
| 去重后唯一变量名 | 1,523 |
| 出现在所有 63 域的变量 | STUDYID |
| 出现在 55+ 域的变量 | STUDYID, DOMAIN, USUBJID |
| 出现在 36+ 域的变量 | EPOCH, TAETORD, VISITNUM, VISIT, VISITDY |
| 仅出现在 1 个域的变量 | ~1,400+ (领域专属变量) |
| 带 CDISC CT 编码的变量 | 570 |
| 观察类 (Observation Class) | 8 种 |

### spec.md 格式（统一、可解析）

```markdown
# AE — Adverse Events
> Class: Events | Structure: One record per adverse event per subject

### AETERM
- **Order:** 7
- **Label:** Reported Term for the Adverse Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim name of the event.
```

**关键结论**: 所有 63 个 spec.md 格式完全统一（Phase 1 脚本生成），解析规则一致，无特殊情况。

---

## 3. 产出文件设计

### 3.1 文件路径

`knowledge_base/VARIABLE_INDEX.md`

### 3.2 文件结构

```markdown
# SDTM Variable Index

> 自动生成，勿手动编辑 | 生成日期: YYYY-MM-DD
> 变量总数: 1523 | 条目总数: 1917 | 覆盖域: 63

## 使用说明

查询变量时，在本文件搜索变量名即可找到它出现在哪些 domain、属于什么角色/类型/核心程度。
- 通用变量（出现在多个域）：表头标注出现域数，域列表用逗号分隔
- 领域专属变量（仅 1 个域）：直接标注所属域

---

## 一、通用变量（出现在 2+ 个域）

| 变量名 | 域数 | 出现的域 | Label | Type | Role | Core |
|--------|------|---------|-------|------|------|------|
| STUDYID | 63 | 所有域 | Study Identifier | Char | Identifier | Req |
| DOMAIN | 59 | (除 CO, OI, RELSPEC, RELSUB) | Domain Abbreviation | Char | Identifier | Req |
| USUBJID | 55 | (除 TA, TD, TE, TI, TM, TS, TV, OI) | Unique Subject Identifier | Char | Identifier | Req/Exp |
| ... | | | | | | |

## 二、领域专属变量（仅 1 个域），按域分组

### AE — Adverse Events (Events)

| 变量名 | Label | Type | Role | Core | CT |
|--------|-------|------|------|------|----|
| AETERM | Reported Term for the Adverse Event | Char | Topic | Req | — |
| AESER | Serious Event | Char | Record Qualifier | Req | C66742 |
| ... | | | | | |

### AG — Procedure Agents (Interventions)
...

## 三、CDISC Controlled Terminology 交叉引用

| CT Code | CT Name | 引用此 CT 的变量 (域.变量名) |
|---------|---------|---------------------------|
| C66742 | No Yes Response | AE.AESER, AE.AESCONG, CM.CMPROPH, ... |
| C74456 | ... | ... |
| ... | | |
```

### 3.3 设计决策

| 决策点 | 选择 | 理由 |
|--------|------|------|
| 通用变量 vs 专属变量分区 | 分两个区 | 通用变量（~120 个）出现在多域，放在一起方便查看全局分布；专属变量（~1400 个）按域分组，避免冗余重复 |
| 通用变量的 Core 列 | 显示最常见值 + 标注差异 | 同一变量在不同域的 Core 可能不同（如 USUBJID 在多数域 Req，在 RELREC 是 Exp） |
| CT 交叉引用独立成节 | 是 | 570 个变量引用了 CT 编码，反向索引可回答"哪些变量用了这个 codelist" |
| 文件格式 | Markdown 表格 | 与知识库其他文件一致，AI 直接可读 |

---

## 4. 技术方案

### 4.1 Python 脚本

**脚本路径**: `.work/04_optimization/scripts/generate_variable_index.py`

**解析逻辑**:

```
对每个 domains/*/spec.md:
  1. 从第 1 行解析: domain 名, 全称 (# AE — Adverse Events)
  2. 从第 3 行解析: class, structure (> Class: Events | Structure: ...)
  3. 对每个 ### 变量块:
     a. 变量名 = ### 后的文本
     b. 逐行正则提取 7 个字段:
        - Order: 数字
        - Label: 文本
        - Type: Char/Num/DateTime
        - Controlled Terms: 文本或空
        - Role: Identifier/Topic/...
        - Core: Req/Exp/Perm
        - CDISC Notes: 文本（可选，索引中不收录）
```

**输出逻辑**:

```
1. 按变量名分组，统计每个变量出现在哪些域
2. 分区:
   - 通用变量 (域数 >= 2): 按域数降序排列
   - 专属变量 (域数 == 1): 按域名字母序分组
3. CT 交叉引用: 提取所有非空 Controlled Terms，按 CT Code 分组，列出引用变量
4. 生成 markdown
```

### 4.2 开发步骤

| # | 步骤 | 说明 | 预估时间 |
|---|------|------|---------|
| 1 | 编写 Python 脚本 | 解析 spec.md + 生成 VARIABLE_INDEX.md | 15 分钟 |
| 2 | 运行脚本 | 输出到 knowledge_base/VARIABLE_INDEX.md | 1 分钟 |
| 3 | 自动校验 | 脚本内置断言：变量总数 == 1917，域数 == 63 | 1 分钟 |
| 4 | 抽样验证 | 人工抽查 5 个变量的分布正确性 | 5 分钟 |
| 5 | 更新 INDEX.md | 在知识库入口添加 VARIABLE_INDEX.md 指引 | 2 分钟 |

---

## 5. 验收标准

### 5.1 完整性（必须全部通过）

| # | 检查项 | 方法 | 预期值 |
|---|--------|------|--------|
| C1 | 变量条目总数 | 脚本统计 + 断言 | == 1917 |
| C2 | 去重后唯一变量数 | 脚本统计 | == 1523 |
| C3 | 覆盖域数 | 脚本统计 + 断言 | == 63 |
| C4 | 每个域的变量数与 spec.md 中 `###` 数量一致 | 脚本逐域校验 | 63/63 PASS |
| C5 | 零遗漏：索引中的变量总数 == 所有 spec.md 中 `###` 行数之和 | 脚本断言 | 1917 == 1917 |

### 5.2 准确性（抽样验证）

| # | 检查项 | 方法 | 抽样量 |
|---|--------|------|--------|
| A1 | 通用变量分布正确 | 人工核对 STUDYID/USUBJID/EPOCH 出现的域列表 | 3 个变量 |
| A2 | 专属变量归属正确 | 随机选 3 个域，核对其专属变量与 spec.md 一致 | 3 个域 × 全部专属变量 |
| A3 | CT 交叉引用正确 | 选 2 个 CT Code，grep 全部 spec.md 验证引用列表 | 2 个 CT Code |
| A4 | Label/Type/Role/Core 字段正确 | 随机选 5 个变量，对照 spec.md 原文 | 5 个变量 |

### 5.3 可用性

| # | 检查项 | 方法 |
|---|--------|------|
| U1 | Markdown 渲染正确 | 目视检查表格在 GitHub/VSCode 中渲染无错位 |
| U2 | 文件体积可接受 | < 200KB（AI 可一次读取） |
| U3 | INDEX.md 已更新 | VARIABLE_INDEX.md 在知识库入口有指引 |

---

## 6. 风险与缓解

| 风险 | 概率 | 缓解 |
|------|------|------|
| 文件超大导致 AI 一次读不完 | 低 (预估 100-150KB) | 如超 200KB，拆分为通用变量/专属变量两个文件 |
| 某些 spec.md 格式不一致 | 极低 (全部脚本生成) | 解析时加容错 + 警告日志 |
| 通用变量的 Core 值跨域不一致 | 确定会出现 | 显示最常见值 + 脚注标注差异 |

---

## 7. 结果预期

完成后，知识库新增 1 个文件 `VARIABLE_INDEX.md`，提供三种查询能力：

1. **变量名 → 域**: "AETERM 出现在哪些域？" → 直接查表得到 AE
2. **域 → 专属变量**: "AE 域有哪些独有变量？" → 查专属变量区 AE 分组
3. **CT Code → 变量**: "C66742 这个 codelist 被哪些变量使用？" → 查 CT 交叉引用区

**预期效果**: AI 在回答变量相关问题时，先查 VARIABLE_INDEX.md 定位，再读对应 spec.md 获取详细定义，不再需要"猜"或遍历文件。
