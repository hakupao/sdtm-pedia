# P1: 交叉引用 — 执行计划

> 创建日期: 2026-04-16
> 状态: 待审核
> 前置: P2 变量反向索引已完成

---

## 1. 目标

在每个 domain 的 spec.md **末尾**添加 `## Cross References` 段落，让 AI 读完一个 domain 后知道还需要去哪里找补充信息。

**解决的问题**: 当前 AI 查完 `AE/spec.md` 后不知道要去 `terminology/core/ae.md` 查编码值、去 `ch04` 查通用规则、去 `FA/` 查 findings about。交叉引用把这些"隐性关联"变成"显式指针"。

---

## 2. 数据摸底结果

### 2.1 可程序化提取的关联 (Layer 1)

| 关联类型 | 数据源 | 自动化程度 | 覆盖范围 |
|---------|--------|-----------|---------|
| spec.md → terminology 文件 | spec.md 中 137 个 CT Code → terminology/ 中 `## ... (C-code)` 标题 | 100% 自动 | 63 域 |
| 同 class 域列表 | spec.md 第 3 行 `> Class: XXX` | 100% 自动 | 63 域 |
| 通用章节引用 | 所有域 → ch04 通用假设 | 100% 静态 | 63 域 |
| 关系数据引用 | 涉及 RELREC/SUPPQUAL 的域 → ch08 | 半自动 (grep assumptions) | ~20 域 |

### 2.2 需要领域知识的关联 (Layer 2)

| 关联类型 | 说明 | 需要人工/AI | 数量 |
|---------|------|-----------|------|
| 域间业务关联 | 如 AE↔CM(伴随用药)、AE↔FA(预设AE)、PC↔PP(药代动力学) | 需要 SDTM 领域知识 | ~30 对 |
| 共享数据集 | EX/EC、MB/MS、PC/PP、TU/TR 等共享 examples | 从 examples 验证记录提取 | ~4 对 |
| 模型层引用 | domain → 对应的 model/ 文件 | 从 class 映射 | 63 域 |

### 2.3 CT Code → Terminology 文件映射

spec.md 中使用 137 个唯一 CT Code，terminology/ 文件中定义了 335 个 CT Code。
映射方法：扫描 terminology/ 全部文件的 `## ... (C-code)` 标题行，建立 C-code → 文件路径的查找表。

---

## 3. 交叉引用格式设计

在每个 `domains/*/spec.md` 末尾追加：

```markdown

---

## Cross References

### Controlled Terminology
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — AESER, AEPRESP, AESCONG, ...
- [Action Taken with Study Treatment (C66767)](../../terminology/core/ae.md) — AEACN
- ...

### Related Domains
- **Same class (Events):** CE, DS, DV, HO, MH
- **Findings About:** [FA](../FA/) — prespecified AE findings
- **Concomitant Treatment:** [CM](../CM/) — linked via RELREC
- **Procedures:** [PR](../PR/) — linked via RELREC

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Observation Classes](../../model/02_observation_classes.md) — Events class variable definitions
```

### 设计决策

| 决策点 | 选择 | 理由 |
|--------|------|------|
| 追加而非新建文件 | 追加到 spec.md 末尾 | AI 读 spec.md 时自然看到引用，不需额外步骤 |
| 使用相对路径链接 | `../../terminology/...` | GitHub/IDE 中可点击跳转 |
| CT 引用列出使用变量 | 是 | 帮助 AI 判断是否需要查看该 codelist |
| 域间关联标注关系类型 | 是（如"linked via RELREC"） | 让 AI 理解关联的性质 |

---

## 4. 技术方案

### 4.1 两阶段执行

**阶段 A: Python 脚本自动生成 (Layer 1)**

脚本路径: `.work/04_optimization/scripts/generate_cross_references.py`

```
1. 扫描 terminology/ 全部文件，建立 CT Code → (文件路径, 名称) 映射表
2. 对每个 domain 的 spec.md:
   a. 提取 class 信息 → 列出同 class 其他域
   b. 提取所有 CT Code → 查映射表得到 terminology 文件路径
   c. 检查 assumptions.md 是否提及 RELREC/SUPPQUAL → 添加 ch08 引用
   d. 映射 class → model/ 文件
   e. 生成 Cross References 段落
3. 追加到 spec.md 末尾（幂等：先删除已有的 Cross References 段，再追加）
```

**阶段 B: AI 补充域间业务关联 (Layer 2)**

方法: 读取每个域的 assumptions.md + examples.md，提取域间关联信息，补充到 Cross References 的 "Related Domains" 小节。

已知关联（从 Phase 5 验证中积累的领域知识）:

| 域 | 关联域 | 关系类型 | 来源 |
|----|--------|---------|------|
| AE | FA | Findings About (预设 AE) | assumptions #4b |
| AE | CM, PR | 伴随治疗/措施 (via RELREC) | assumptions #6a |
| PC | PP | 共享药代数据集 | examples 共享区段 |
| EX | EC | 共享暴露数据集 | examples 共享区段 |
| MB | MS | 共享微生物数据集 | examples 共享区段 |
| TU | TR | 共享肿瘤数据集 | examples 共享区段 |
| DM | all | 人口统计学基础域 | SDTM 标准 |
| RELREC | all | 关系记录 | SDTM 标准 |
| SUPPQUAL | all | 补充限定符 | SDTM 标准 |
| FA | AE, CM, PR, EX, EC, ML, SU | Findings About 源域 | model definition |
| SR | AE, CM, PR, EX, EC, ML, SU | Findings About 源域 (device) | model definition |

补充方法: 用 AI agent 读取每个域的 assumptions.md，提取明确提到的其他域名。人工审核后写入。

### 4.2 开发步骤

| # | 步骤 | 说明 | 预估时间 |
|---|------|------|---------|
| 1 | 编写 Python 脚本 (阶段 A) | CT 映射 + class 关联 + 通用引用 + 幂等追加 | 20 分钟 |
| 2 | 运行脚本 | 63 个 spec.md 全部追加 Cross References | 1 分钟 |
| 3 | 自动校验 | 断言: 63 个 spec.md 都含 `## Cross References`；CT 映射零未命中 | 1 分钟 |
| 4 | 抽样检查 (阶段 A) | 人工抽查 3 个域的引用正确性 | 5 分钟 |
| 5 | AI 补充域间关联 (阶段 B) | 读 assumptions.md 提取跨域引用 + 已知关联表 | 15 分钟 |
| 6 | 人工审阅 (阶段 B) | 用户审核域间关联的准确性 | 按需 |
| 7 | 最终校验 | 链接有效性检查（文件路径存在） | 5 分钟 |

---

## 5. 验收标准

### 5.1 完整性

| # | 检查项 | 方法 | 预期值 |
|---|--------|------|--------|
| C1 | 63 个 spec.md 都含 `## Cross References` | grep 全量检查 | 63/63 |
| C2 | 所有 CT Code 引用指向存在的 terminology 文件 | 脚本校验路径 | 零悬空链接 |
| C3 | 每个域至少有 General References 和 Model Definition | grep 检查 | 63/63 |
| C4 | 同 class 域列表正确 | 与 P2 中的 class 数据交叉验证 | 8 class 全部匹配 |

### 5.2 准确性

| # | 检查项 | 方法 | 抽样量 |
|---|--------|------|--------|
| A1 | CT Code 映射正确 | 选 3 个域，核对 CT Code → terminology 文件 | 3 域 |
| A2 | 域间关联准确 | 选 AE/PC/FA 核对关联域列表 | 3 域 |
| A3 | 相对路径链接有效 | 脚本检查所有链接的目标文件存在 | 全量 |

### 5.3 可用性

| # | 检查项 | 方法 |
|---|--------|------|
| U1 | 追加内容不破坏 spec.md 原有格式 | 抽查 3 个域的 markdown 渲染 |
| U2 | 幂等性: 重复运行脚本结果不变 | 运行两次，diff 无差异 |

---

## 6. 风险与缓解

| 风险 | 概率 | 缓解 |
|------|------|------|
| CT Code 在 terminology 文件中找不到 | 中 (spec 有 137 个, terminology 有 335 个) | 脚本报警但不中断，标注 `(未收录)` |
| 域间关联遗漏 | 中 | Layer 2 先覆盖已知关联，后续可迭代补充 |
| 追加内容后 spec.md 过大 | 低 (追加约 20-40 行) | 交叉引用段简洁，不膨胀 |

---

## 7. 结果预期

完成后，每个 domain 的 spec.md 末尾都有结构化的交叉引用段，提供四类导航：

1. **CT → terminology**: "AESER 的编码值在哪？" → 直接点击链接到 terminology 文件
2. **Class siblings**: "和 AE 同类型的域有哪些？" → 直接看列表
3. **域间关联**: "AE 相关的治疗数据在哪？" → CM/PR via RELREC
4. **通用规则**: "变量命名规则在哪？" → ch04

**预期效果**: AI 读完 spec.md 后不再需要"猜"下一步去哪，交叉引用提供了明确的导航路径。
