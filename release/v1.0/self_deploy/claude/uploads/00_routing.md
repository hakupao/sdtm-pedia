# SDTM Knowledge Base — Query Routing Guide

> AI 在回答 SDTM 相关问题时，**先读本文件确定查找路径，再读目标文件获取答案**。
> 不要猜测文件位置，按下方规则路由。

---

## 快速入口

| 需要什么 | 去哪里 |
|---------|--------|
| 按变量名查找 | [VARIABLE_INDEX.md](VARIABLE_INDEX.md) |
| 按域名查找 | [INDEX.md](INDEX.md) → domains/{DOMAIN}/ |
| 按 CT Code 查找 | [VARIABLE_INDEX.md](VARIABLE_INDEX.md) § 三、CT 交叉引用 |
| 域内交叉引用 | domains/{DOMAIN}/spec.md → 末尾 Cross References 段 |

---

## 路由规则

### 1. 变量定义类

**问法示例**: "AETERM 是什么？"、"AE 域有哪些变量？"、"USUBJID 出现在哪些域？"

```
问某个变量的定义/属性 (Label, Type, Role, Core)
  → 先查 VARIABLE_INDEX.md 定位该变量所在的域
  → 再读 domains/{DOMAIN}/spec.md 获取完整定义 (含 CDISC Notes)

问某个域有哪些变量
  → 读 domains/{DOMAIN}/spec.md（全部变量按 Order 排列）

问某个变量出现在哪些域
  → 查 VARIABLE_INDEX.md §一 (通用变量) 或 §二 (专属变量)

问某类角色的变量 (如所有 Identifier、所有 Timing)
  → 查 VARIABLE_INDEX.md（按 Role 列筛选）
  → 或读 model/02_observation_classes.md（class 级变量定义）
```

### 2. 编码/术语类

**问法示例**: "AESER 可以填什么值？"、"C66742 是什么 codelist？"、"LBTESTCD 的标准编码在哪？"

```
问某个变量的允许值/编码
  → 读 domains/{DOMAIN}/spec.md 找到该变量的 Controlled Terms 字段
  → 如果有 CT Code (如 C66742):
    → 方法 1: 查 VARIABLE_INDEX.md §三 找到 CT Code 对应的 terminology 文件
    → 方法 2: 查 spec.md 末尾 Cross References → Controlled Terminology 段（有直接链接）
  → 读对应的 terminology/ 文件获取完整值列表

问某个 CT Code 的含义和值列表
  → 查 VARIABLE_INDEX.md §三 → 找到 terminology 文件路径 → 读取

问问卷类编码 (BDI-II, ADAS-COG, HAM-D 等)
  → 读 terminology/questionnaires/ 下的文件
  → 文件较多 (43 个分片)，先在 INDEX.md § Questionnaires Terminology 确认范围

问编码规范的通用规则 (如何选择 codelist, extensible 含义)
  → 读 chapters/ch04_general_assumptions.md §4.2 (Coding and Controlled Terminology)
  → 读 chapters/ch10_appendices.md (Appendix C: Controlled Terminology)
```

### 3. 业务规则/假设类

**问法示例**: "AE 数据怎么收集？"、"EPOCH 怎么用？"、"什么时候拆分 domain？"

```
问某个域的业务规则和数据收集假设
  → 读 domains/{DOMAIN}/assumptions.md（领域专属规则）
  → 补充读 chapters/ch04_general_assumptions.md（通用规则，可能被引用）

问通用变量规则 (命名、Core、Origin、Natural Key 等)
  → 读 chapters/ch04_general_assumptions.md:
    - §4.1: 域级假设 (拆分域、命名、Core 定义、Origin metadata)
    - §4.2: 变量级假设 (编码、文本大小写、自由文本、多值处理)
    - §4.3: 观察类特定假设 (--OBJ, --CAT, result qualifiers)
    - §4.4: 时间变量 (--DTC, --DY, --DUR, EPOCH, reference time points)
    - §4.5: 其他假设

问变量角色/类型的定义 (Identifier, Topic, Qualifier 是什么)
  → 读 model/01_concepts_and_terms.md

问某个 Observation Class 的变量模板
  → 读 model/02_observation_classes.md (Interventions/Events/Findings 各自的变量列表)

问提交要求 (metadata, primary key, Define-XML)
  → 读 chapters/ch03_submitting_data.md
```

### 4. 域间关系类

**问法示例**: "AE 和 CM 怎么关联？"、"什么是 SUPPQUAL？"、"RELREC 怎么用？"

```
问两个域之间如何关联
  → 读 chapters/ch08_relationships.md（关联机制总述）
  → 读 domains/RELREC/（RELREC 变量定义 + 使用假设 + 示例）
  → 查两个域的 spec.md 末尾 Cross References → Related Domains 段

问 Supplemental Qualifier (SUPPQUAL / SUPP--)
  → 读 domains/SUPPQUAL/spec.md + assumptions.md
  → 读 chapters/ch08_relationships.md §8.4 (SUPP-- 详细规则)

问 RELREC 的用法和示例
  → 读 domains/RELREC/（spec + assumptions + examples）
  → 读 chapters/ch08_relationships.md §8.2-8.3

问标本关系 (specimen hierarchy)
  → 读 domains/RELSPEC/
  → 读 chapters/ch08_relationships.md §8.5

问受试者关系 (pooled subjects)
  → 读 domains/RELSUB/
  → 读 chapters/ch08_relationships.md §8.6
```

### 5. 实现示例类

**问法示例**: "给我看一个 AE 的数据示例"、"交叉试验的 TA 怎么建？"

```
问某个域的数据表示例
  → 读 domains/{DOMAIN}/examples.md

问试验设计示例 (并行/交叉/周期设计)
  → 读 domains/TA/examples.md（7 个完整试验设计示例，含 Mermaid 图）

问访视设计示例
  → 读 domains/TV/examples.md

问药代动力学数据示例
  → 读 domains/PC/examples.md + domains/PP/examples.md（共享数据集）
```

### 6. 概念/模型类

**问法示例**: "SDTM 的数据模型是什么？"、"怎么创建新 domain？"、"Events 和 Findings 有什么区别？"

```
问 SDTM 整体模型概念
  → 读 model/01_concepts_and_terms.md（概念总述）
  → 读 model/02_observation_classes.md（三大观察类）

问如何创建自定义 domain
  → 读 chapters/ch02_fundamentals.md（创建新域的流程和规则）
  → 读 model/02_observation_classes.md（确认适用的观察类）

问特殊用途域 (DM, CO, SE, SV, SM)
  → 读 model/03_special_purpose_domains.md

问 Associated Persons 数据
  → 读 model/04_associated_persons.md

问试验设计模型 (TE/TA/TV/TD/TM/TI/TS)
  → 读 model/05_study_level_data.md

问关系数据集模型 (RELREC/SUPP/POOLDEF/RELSUB)
  → 读 model/06_relationship_datasets.md
```

### 7. 跨域/全局查询类

**问法示例**: "哪些域用了 EPOCH？"、"Events class 包含哪些域？"、"哪些变量用了 C66742？"

```
问某个变量在哪些域中使用
  → 查 VARIABLE_INDEX.md §一 (通用变量区)

问某个 class 包含哪些域
  → 查 VARIABLE_INDEX.md §二 的域分组标题 (每个域标注了 class)
  → 或查 INDEX.md 的域列表 (按 class 分组)

问哪些变量引用了某个 CT Code
  → 查 VARIABLE_INDEX.md §三 (CT 交叉引用)

问 SDTM 版本变更/新增内容
  → 读 chapters/ch01_introduction.md §1.3 (Changes from v3.3)

问术语表/词汇定义
  → 读 chapters/ch10_appendices.md (Appendix B: Glossary)
```

---

## 多文件查询策略

当一个问题涉及多个文件时，按以下优先级读取：

1. **先定位**: VARIABLE_INDEX.md 或 INDEX.md（确定目标文件）
2. **再读主文件**: spec.md 或 assumptions.md（获取核心信息）
3. **按需补充**: Cross References 中的链接（扩展相关信息）
4. **通用规则兜底**: ch04_general_assumptions.md（如果主文件未覆盖）

**不要一次读取超过 3 个文件**。先读最可能包含答案的文件，根据其中的线索决定是否需要补充读取。

---

## 文件类型速查

| 文件类型 | 路径模式 | 内容 | 何时读 |
|---------|---------|------|--------|
| spec.md | domains/{DOMAIN}/spec.md | 变量定义表 (Order, Label, Type, CT, Role, Core, Notes) | 查变量属性 |
| assumptions.md | domains/{DOMAIN}/assumptions.md | 域专属业务规则，编号列表 | 查数据收集/处理规则 |
| examples.md | domains/{DOMAIN}/examples.md | 数据表示例 + Mermaid 图 | 查实际数据格式 |
| model/*.md | model/01-06_*.md | SDTM v2.0 概念模型 | 查模型定义/变量模板 |
| chapters/*.md | chapters/ch01-10_*.md | SDTMIG 实施指南通用章节 | 查通用规则/关系/提交 |
| terminology/*.md | terminology/{category}/*.md | CDISC 受控术语值列表 | 查编码允许值 |
| VARIABLE_INDEX.md | knowledge_base/VARIABLE_INDEX.md | 1523 变量反向索引 | 按变量名/CT Code 查找 |
| INDEX.md | knowledge_base/INDEX.md | 知识库总目录 | 初始导航 |
