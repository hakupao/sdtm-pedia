<!-- chain: C (新阶段启动链)
  开始执行本文件中的任务时，必须检查:
  → meta/worklog.md                  (记录启动)
  → ../docs/PROGRESS.md                   (更新看板)
  → MANIFEST.md                      (注册新文件)
-->

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
- **状态**: [x] **已验证** (2026-04-16) — V1 链接 724/724 PASS, V6 路由准确性 15/15 PASS

### 目标

在 `knowledge_base/` 下创建 `ROUTING.md`，定义问题类型到文件路径的路由规则，让 AI 按规则查找而非靠猜。

### 执行结果 (2026-04-16)

- **产出**: `knowledge_base/ROUTING.md`
- **内容**: 7 类问题路由规则 + 多文件查询策略 + 文件类型速查表
  1. 变量定义类 (定义/属性/跨域分布)
  2. 编码/术语类 (CT Code/允许值/问卷编码)
  3. 业务规则/假设类 (域规则/通用规则/时间变量)
  4. 域间关系类 (RELREC/SUPPQUAL/RELSPEC/RELSUB)
  5. 实现示例类 (数据表/试验设计/药代)
  6. 概念/模型类 (观察类/新域创建/特殊域)
  7. 跨域/全局查询类 (变量分布/class/版本变更)
- **与 P1/P2 的联动**: 路由规则中引用 VARIABLE_INDEX.md 和 Cross References 段作为定位工具
- **INDEX.md 已更新**: 添加 ROUTING.md 入口（AI 首选入口）

---

## P1：交叉引用

- **优先级**: 高，P0 完成后接着做
- **工作量**: 3-4 小时
- **精度提升**: 高
- **状态**: [x] **已验证** (2026-04-16) — V2 CT 63/63 PASS, V4 归类 8/8 PASS, V5 回归 63/63 PASS, V7 完备性 6/6 PASS

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

### 执行结果 (2026-04-16)

- **脚本**: `.work/04_optimization/scripts/generate_cross_references.py`
- **两阶段合并执行**: Layer 1 (程序化: CT 映射 + class 关联 + 通用引用) + Layer 2 (领域知识: 28 域的域间业务关联)
- **产出**: 63 个 spec.md 末尾追加 `## Cross References` 段落，含 4 小节:
  - Controlled Terminology (CT Code → terminology 文件链接，588 个引用，零未映射)
  - Related Domains (同 class 域 + 28 域的领域关联)
  - General References (ch04 + ch08 + VARIABLE_INDEX)
  - Model Definition (class → model/ 文件)
- **校验**: C1-C4 全 PASS, A3 零悬空链接, U2 幂等性验证通过
- **详细计划**: `.work/04_optimization/p1_cross_reference_plan.md`

---

## P2：变量级反向索引

- **优先级**: 中，有空做
- **工作量**: 半天
- **精度提升**: 中
- **状态**: [x] **已验证** (2026-04-16) — V3 计数 63/63 PASS, V8 精度 9/10 PASS (F1 MIDSTYPE 已修复)

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

Python 脚本从 63 个 spec.md 自动提取。

### 执行结果 (2026-04-16)

- **脚本**: `.work/04_optimization/scripts/generate_variable_index.py`
- **产出**: `knowledge_base/VARIABLE_INDEX.md` (131.4 KB)
- **三段结构**: 通用变量 (24 个) + 专属变量 (1499 个，按域分组) + CT 交叉引用 (独立 CT Code)
- **校验**: C1-C5 全部 PASS (1917 条目 / 1523 唯一变量 / 63 域 / 逐域匹配)
- **抽样验证**: A1-A3 PASS (STUDYID/USUBJID/EPOCH 分布正确，DM 专属变量 27 个匹配，C66742 共 123 引用一致)
- **详细计划**: `.work/04_optimization/p2_variable_index_plan.md`

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
