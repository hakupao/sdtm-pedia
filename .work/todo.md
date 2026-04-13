# Knowledge Base 检索精度优化 — TODO

> 目标：提升 SDTM knowledge_base 的 AI 检索精度，减少幻觉
> 创建日期: 2026-04-13

---

## 当前瓶颈

当前检索链路：`用户提问 → AI 看 INDEX.md → 猜测该读哪个文件 → 读取 → 回答`

| # | 问题 | 影响 |
|---|------|------|
| 1 | AI 靠"猜"定位文件 | 复杂问题涉及多文件时容易遗漏 |
| 2 | 跨文件关联缺失 | 如查 AEACN 的 CT 值，需同时看 spec.md 和 terminology/，但无显式关联 |
| 3 | 没有反向索引 | 无法从变量名快速定位到它出现在哪些 domain |

---

## P0：ROUTING.md 问题路由索引

- **优先级**: 最高，先做
- **工作量**: 1-2 小时
- **精度提升**: 高
- **状态**: [ ] 待开始

### 目标

在 `knowledge_base/` 下创建 `ROUTING.md`，定义问题类型到文件路径的路由规则，让 AI 按规则查找而非靠猜。

### 路由规则设计

```
问某个 domain 的变量定义
→ 读 domains/{DOMAIN}/spec.md

问某个 domain 的业务规则/假设
→ 读 domains/{DOMAIN}/assumptions.md + chapters/ch04_general_assumptions.md

问某个变量应该填什么值
→ 先读 domains/{DOMAIN}/spec.md 找到 Controlled Terms 字段
→ 再读对应的 terminology/core/{xxx}.md

问两个 domain 之间的关系
→ 读 chapters/ch08_relationships.md + domains/RELREC/

问如何创建新的自定义 domain
→ 读 chapters/ch02_fundamentals.md + model/observation_classes.md

问 Supplemental Qualifier
→ 读 domains/SUPPQUAL/ + chapters/ch08_relationships.md
```

---

## P1：交叉引用

- **优先级**: 高，P0 完成后接着做
- **工作量**: 3-4 小时
- **精度提升**: 高
- **状态**: [ ] 待开始

### 目标

在每个 domain 的 spec.md 末尾添加交叉引用段落，让 AI 读完一个文件后知道还需要去哪里找补充信息。

### 格式示例（以 AE 为例）

```markdown
## 交叉引用
- **Controlled Terminology**: terminology/core/ae.md
- **相关 Findings**: domains/FA/ (预设AE条目的存在/缺失)
- **关联 domain**: CM/PR (通过 RELREC 关联治疗措施)
- **通用规则**: chapters/ch04_general_assumptions.md
- **关系数据**: domains/RELREC/, chapters/ch08_relationships.md
```

### 覆盖范围

全部 63 个 domain 的 spec.md 都需要添加。可用脚本批量生成基础模板，再人工补充特定关联。

---

## P2：变量级反向索引

- **优先级**: 中，有空做
- **工作量**: 半天
- **精度提升**: 中
- **状态**: [ ] 待开始

### 目标

创建 `knowledge_base/VARIABLE_INDEX.md`，建立变量名→domain→定义位置的映射表。

### 格式设计

```markdown
| 变量名     | 出现的 Domain       | 类型       | 定义位置                          |
|-----------|--------------------|-----------|---------------------------------|
| STUDYID   | 所有 domain         | Identifier | model/observation_classes.md     |
| USUBJID   | 所有 domain         | Identifier | model/observation_classes.md     |
| AETERM    | AE                 | Topic      | domains/AE/spec.md               |
| AESER     | AE                 | Qualifier  | domains/AE/spec.md               |
| --TERM    | Events class 通用   | Topic      | model/observation_classes.md     |
| --TESTCD  | Findings class 通用 | Topic      | model/observation_classes.md     |
| EPOCH     | 多个 domain         | Timing     | chapters/ch04_general_assumptions.md |
```

### 实施方案

可编写 Python 脚本从 63 个 spec.md 中自动提取所有变量名、类型、角色，生成完整索引表。

---

## P3：结构化元数据

- **优先级**: 长期，为未来扩展打基础
- **工作量**: 数天
- **精度提升**: 为接入向量数据库/知识图谱做准备
- **状态**: [ ] 待开始

### 目标

将 spec.md 的变量信息转为结构化的 YAML/JSON，支持程序化查询。

### 格式设计（以 AE 为例）

```yaml
domain: AE
class: Events
structure: "One record per adverse event per subject"
variables:
  - name: AETERM
    order: 7
    type: Char
    role: Topic
    core: Req
    controlled_terminology: null
    cross_ref: ["terminology/core/ae.md"]

  - name: AESER
    order: 22
    type: Char
    role: Qualifier
    core: Exp
    controlled_terminology: "C66742 (No Yes Response)"
    cross_ref: ["terminology/core/general_part1.md"]

relationships:
  - target: FA
    type: "prespecified AE ↔ findings"
    link_method: RELREC
  - target: CM
    type: "concomitant treatment for AE"
    link_method: RELREC
```

### 覆盖范围

全部 63 个 domain。可编写 Python 脚本从 spec.md 自动解析生成，再人工补充 relationships 和 cross_ref。
