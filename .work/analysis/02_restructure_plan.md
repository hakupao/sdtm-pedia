# 知识库重构方案（完整版）

> 创建日期：2026-04-13
> 状态：方案已确认，待进入技术细节讨论

---

## 一、决策：重新提取，不在现有基础上修改

### 原因

1. **现有目录按"重要性"分（核心/其余），非逻辑结构** — 检索需要先知道 domain 的优先级分类
2. **Specification 信息重复** — Variables_AE.md 和 FullText 中各有一份，且 Variables 版本丢失了 xlsx 的字段精度
3. **FullText 按文件大小切分，非按 domain 切分** — 一个文件混合多个 domain，查找需要知道 domain 在哪个 part
4. **改造工作量 ≈ 重建工作量** — 要拆分混合文件 + 重组目录 + 补字段精度，不如从源头重来

---

## 二、SDTM 与 SDTMIG 的关系（调研结论）

| | SDTM v2.0 | SDTMIG v3.4 |
|---|---|---|
| **性质** | 数据模型标准（Model） | 实施指南（Implementation Guide） |
| **定义什么** | 概念框架：observation class、variable role、domain 分类体系 | 具体 domain 的变量名、标签、类型、Core 状态、业务规则、示例 |
| **抽象程度** | 高 — 通用变量模板 | 低 — 每个 domain 的具体实施 |
| **版本配对** | v2.0 与 SDTMIG v3.4 同步发布 (2021-11-29) | |
| **日常使用** | 偶尔查（自定义 domain、理解设计原理） | 主要工作文档（mapping/programming） |

**SDTM v2.0 的独有价值**：Section 3.1 的三大 observation class 通用变量模板表（IG 假设你已读过）、概念定义、Associated Persons 数据模型。

---

## 三、完整目录结构（已确认）

```
knowledge_base/
├── model/                             # SDTM v2.0（概念模型层）
│   ├── concepts_and_terms.md          # Ch2: variable role 等概念定义
│   ├── observation_classes.md         # Ch3.1: Interventions/Events/Findings 通用变量模板
│   ├── special_purpose_domains.md     # Ch3.2: DM/CO/SE 等模型定义
│   ├── associated_persons.md          # Ch4: 非受试者数据模型
│   ├── study_level_data.md            # Ch5: Trial Design 概念
│   └── relationship_datasets.md       # Ch6: RELREC 等模型定义
│
├── chapters/                          # SDTMIG v3.4 通用章节
│   ├── ch01_introduction.md           # 第1章 Introduction (p7-10)
│   ├── ch02_fundamentals.md           # 第2章 Fundamentals (p11-16)
│   ├── ch03_submitting_data.md        # 第3章 Submitting Data (p17-21)
│   ├── ch04_general_assumptions.md    # 第4章 通用假设 (p22-59)
│   ├── ch08_relationships.md          # 第8章 RELREC/SUPPQUAL (p427-440)
│   └── ch10_appendices.md             # 第10章 附录 (p444+)
│
├── domains/                           # SDTMIG v3.4 per-domain 三件套
│   ├── AE/
│   │   ├── spec.md                    # ← xlsx（含 C-code 引用）
│   │   ├── assumptions.md             # ← PDF
│   │   └── examples.md               # ← PDF
│   └── ... (63 domains)
│
├── terminology/                       # SDTM Terminology (1005 codelist, ~38000 terms)
│   ├── core/                          # SDTMIG spec 直接引用的 ~143 个 C-code（日常必查）
│   │   ├── response.md                # Yes/No (C66742), Not Done (C66789) 等通用响应
│   │   ├── ae.md                      # Action Taken (C66767), Outcome (C66768), Severity (C66769)
│   │   ├── dm.md                      # Sex (C66731), Race (C74457), Ethnic Group (C66790)
│   │   ├── disposition.md             # Disposition Category (C74558), Completion (C66727), Epoch (C99079)
│   │   ├── interventions.md           # Route (C66729), Dosage Form (C66726), Frequency (C71113)
│   │   ├── findings_common.md         # Anatomical Location (C74456), Laterality (C99073)
│   │   ├── vs.md                      # VS Test Code/Name, VS Units
│   │   ├── lb.md                      # LB Test Code/Name
│   │   ├── eg.md                      # ECG Test Code/Name/Result
│   │   ├── trial_design.md            # TS Parameter Code/Name
│   │   └── other_referenced.md        # 其余被 SDTMIG 引用的
│   ├── questionnaires/                # QS 问卷相关 (~453 codelist)
│   └── supplementary/                 # 未被 SDTMIG 直接引用的其余 codelist
│
└── INDEX.md
```

### 设计原则

- **model（为什么）→ chapters（通用规则）→ domains（具体怎么做）→ terminology（受控值）**
- Domain 目录采用三件套：spec（xlsx 权威源）+ assumptions（PDF）+ examples（PDF）
- Terminology 不放进 domain 目录（跨 domain 共享，如 C66742 被十几个 domain 引用），spec.md 保留 C-code 引用

### 方案选择理由（Domain 优先 vs 类型优先）

| 维度 | Domain 优先（已选） | 类型优先（放弃） |
|------|---------------------|-------------------|
| 日常查询 | 以 domain 为单位，一次 glob 拿全 | 需跨目录拼接 |
| LLM/RAG | 相关信息物理邻近，语义检索更准 | 同 domain 信息分散 |
| SDTM 工作习惯 | 契合（mapping/review 以 domain 为单位） | 不太契合 |
| 扩展灵活性 | 可异构（不要求每个 domain 文件齐整） | 要求结构齐整 |

---

## 四、数据源分工

| 内容 | 权威源 | 说明 |
|------|--------|------|
| Specification（变量表） | `SDTMIG_v3.4.xlsx` | 结构化、有 Variable Order、Controlled Terms 精确 |
| Assumptions（业务规则） | `SDTMIG v3.4.pdf` | xlsx 中没有，仅 PDF |
| Examples（示例数据） | `SDTMIG v3.4.pdf` | xlsx 中没有，仅 PDF |
| 通用章节 (ch01-ch10) | `SDTMIG v3.4.pdf` | 第1-4、8-10章 |
| 概念模型 (model/) | `SDTM_v2.0.pdf` | 74 页，概念定义和通用变量模板 |
| 受控术语 | `SDTM Terminology.xlsx` | 1005 codelist / ~38000 terms |

### Terminology 数据特征

| 类别 | Codelist 数 | 说明 |
|------|------------|------|
| General/Other | 183 | 跨 domain 通用（SDTMIG 引用的 ~143 个主要在此） |
| Questionnaire Test Code/Name | 453 | QS 专用，量大但独立 |
| Domain-specific Test Code/Name | 290 | LB/ECG/VS 等特定检查 |
| Clinical Classification | 79 | 量表评分 |

---

## 五、旧目录处理

**决定：保留 `project_knowledge_base/`，新结构验收通过后再删除。**

理由：作为对照基准用于交叉校验；无 git，删除不可逆；占用空间可忽略。

---

## 六、技术约束与优化策略

### 目标平台：Claude Project Knowledge Base

知识库文件最终上传到 Claude Project，有两种工作模式：

| | 直接加载（< ~200K tokens） | RAG 模式（超过阈值） |
|---|---|---|
| 工作方式 | 所有文件完整加载到上下文 | 按需语义检索相关片段 |
| 检索质量 | 最佳 — 交叉引用无遗漏 | 依赖匹配，可能漏跨文件关联 |
| 触发条件 | 文件少（~10-12 个以内） | 文件数多或总 token 超限 |

我们的方案 220+ 文件，**必然进入 RAG 模式**。

### RAG 模式下的优化措施

1. **文件名有语义** — `domains/AE/assumptions.md` 而非 `file_042.md`
2. **提供 INDEX.md** — 全局索引文件提升检索准确率
3. **按逻辑边界切分** — 三件套方案天然符合
4. **内容干净** — 去冗余、去 PDF 噪音

### 文件大小策略

- **目标：单文件控制在 ~100KB 以内**
- **执行原则：先做完整文件，根据结果再拆超标的**
- 拆分是简单的后置操作（按 `##` 标题切分）；提前设计拆分规则会增加方案复杂度且可能猜错
- 预估大部分 spec/assumptions/examples 在 5-30KB，不会超标
- 可能需要拆分的：ch04（38 页）、terminology 中 LB/QS 相关大 codelist

### 格式选择：Markdown

Markdown 是 LLM 知识库的最优格式：体积最小、结构表达力强（标题/表格/列表）、LLM 原生理解度最高。

---

## 七、文件格式模板（已确认）

### 跨 Class 结构扫描结论

对 DM（Special Purpose）、CM（Interventions）、AE（Events）、LB（Findings）、TA（Trial Design）五个代表性 domain 进行了 PDF 原文扫描，发现：

- **Assumptions 层级不统一**：DM 最深 4 级（4→a→c→ii→1），AE 3 级，CM/LB/TA 2 级。模板必须支持任意深度嵌套
- **Assumptions 主题标题非标准**：部分条目有加粗标题（如 AE "**AE description and coding**"），部分无。需原样保留
- **Examples 复杂度差异极大**：TA 含设计矩阵和大量叙述；LB 数据表 40+ 列；DM 有跨 domain 联动示例（dm.xpt + se.xpt）
- **TA 的 Examples 结构与其他 domain 差异最大**：不是简单"场景+数据表"，而是完整教学文档

### 表格 vs 平铺决策

**核心判断：220+ 文件必然走 RAG 模式，RAG 的检索单位是 chunk。表格被 chunk 切割后会丢失表头，平铺格式每个 chunk 自解释。**

| 文件类型 | 格式 | 理由 |
|---------|------|------|
| **spec.md** | **平铺（逐变量块）** | 变量定义是逐条查询场景，chunk 必须自包含 |
| **model/observation_classes.md** | **平铺（逐变量块）** | 同 spec — 通用变量模板，查询模式相同 |
| **assumptions.md** | 编号段落 + 嵌套列表 | 本身已是散文/列表结构，天然平铺 |
| **examples.md** | 保留表格 | 数据表是内容本身，展示 .xpt 行列关系 |
| **terminology/core/*.md** | 保留表格 | 查询模式是"codelist 有哪些值"，需一次扫描全部 terms |
| **chapters/*.md** | 原文结构 | 叙述性文本为主 |

### spec.md 模板

```markdown
# {DOMAIN} — {Domain Label}

> Class: {Class} | Structure: {one record per...}

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:**
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### AETERM
- **Order:** 9
- **Label:** Reported Term for the Adverse Event
- **Type:** Char
- **Controlled Terms:**
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim name of the event.
```

来源：xlsx（权威源）。所有 domain 格式统一。

### assumptions.md 模板

```markdown
# {DOMAIN} — Assumptions

1. {第一条 assumption 文本}

2. **{主题标题（如有）}**
   a. {子条目}
   b. {子条目}
      i. {三级条目}
      ii. {三级条目}
         1. {四级条目}

3. {无主题标题的条目}
```

来源：PDF。原则：忠实保留原文编号层级和加粗标题，不做结构改造。

### examples.md 模板

```markdown
# {DOMAIN} — Examples

## Example 1

{场景描述文字}

{Row-by-row 说明（如有）}

**{domain}.xpt**

| Row | STUDYID | DOMAIN | ... |
|-----|---------|--------|-----|
| 1   | ...     | ...    | ... |

## Example 2
...
```

来源：PDF。特殊处理：
- 跨 domain 联动示例：在同一个 example 下保留多个 .xpt 表
- TA 等含设计矩阵的：保留矩阵表格和叙述，图表用文字描述替代

---

## 八、技术实现方案（已确认）

### 重要约束

1. **现有 `project_knowledge_base/` 产物不可复用** — 未经逐字验证，目视检查有明显内容丢失
2. **PDF 单次读取页数不宜过多** — 页数过大导致精度丢失、内容遗漏（前期制作经验）
3. **以单个 md 文件为最小执行单位** — 一次交互产出一个 md 文件

### 提取来源与方式

| 目标文件 | 来源 | 方式 |
|---------|------|------|
| `domains/*/spec.md` | SDTMIG_v3.4.xlsx | Python 脚本自动生成 |
| `domains/*/assumptions.md` | SDTMIG v3.4 PDF | Claude 逐 domain 读取 PDF |
| `domains/*/examples.md` | SDTMIG v3.4 PDF | Claude 逐 domain 读取 PDF |
| `terminology/` | SDTM Terminology.xlsx | Python 脚本自动生成 |
| `model/` | SDTM_v2.0.pdf | Claude 读取 PDF |
| `chapters/` | SDTMIG v3.4 PDF | Claude 读取 PDF |

### PDF 读取页数控制

| 内容类型 | 建议单次页数 | 理由 |
|---------|------------|------|
| Assumptions | 5-8 页 | 层级嵌套深，需精确保留编号结构 |
| Examples（简单 domain） | 5-8 页 | 数据表列数少 |
| Examples（复杂 domain，如 LB/TA） | 3-5 页 | 列数多（40+列），需高精度 |
| Chapters 叙述性文本 | 8-10 页 | 纯文字，精度压力小 |

**原则：宁可多读几轮，不要一次塞太多。**

### 单次交互产出规则

- 简单 domain（<8 页）→ 一次读完，直接输出一个 md 文件
- 复杂 domain 或长章节（>8 页）→ 分多次读取，每次 5-8 页，拼接成一个 md 文件
- 每个 md 文件独立可验证：产出后立即检查完整性

示例：

| 目标文件 | 读取计划 |
|---------|---------|
| `domains/AE/assumptions.md` | 读 p137-140（4页）→ 一次完成 |
| `domains/AE/examples.md` | 读 p140-142（3页）→ 一次完成 |
| `domains/TA/examples.md` | 读 p384-390 → 再读 p390-396 → 拼接 |
| `chapters/ch04_general_assumptions.md` | 分 5 次（p22-30, p30-38, p38-46, p46-54, p54-59）→ 拼接 |

### 执行路线

```
Phase 1: 自动化部分
  ① Python 脚本生成 spec.md（63 个文件）
  ② Python 脚本生成 terminology/
  ③ 自动校验 spec.md（与 xlsx 逐字段比对）

Phase 2: 建立页码索引
  ④ 扫描 PDF 目录页，建立 domain → 页码映射表
     精确到每个 domain 的 Spec/Assumptions/Examples 起始页

Phase 3: PDF 逐批提取（按 class 分批，每批一个会话）
  批次 1: Special Purpose — CO, DM, SE, SM, SV（5 domain）
  批次 2: Interventions — AG, CM, EC, EX, ML, PR, SU（7 domain）
  批次 3: Events — AE, BE, CE, DS, DV, HO, MH（7 domain）
  批次 4-8: Findings — 每批 5-6 个 domain（~28 domain）
  批次 9: Findings About — FA, SR（2 domain）
  批次 10: Trial Design — TA, TD, TE, TI, TM, TS, TV（7 domain）
  批次 11: Relationships + Study Ref（~5 domain）

  每个 domain 执行：
    → 读 Assumptions 页码范围 → 写 assumptions.md
    → 读 Examples 页码范围 → 写 examples.md
    → 快速自检（编号连续性、example 数量、末尾截断检查）

Phase 4: 补充内容
  ⑦ model/（从 SDTM_v2.0.pdf 提取，74 页，~8-10 轮读取，6 个文件）
  ⑧ chapters/（从 SDTMIG PDF 提取通用章节，6 个文件）

Phase 5: 收尾
  ⑨ 全量校验
     - spec.md：与 xlsx 自动比对
     - assumptions：编号连续性 + 抽样 PDF 原文对照
     - examples：example 数量 + 数据表列数比对
     - 文件完整性：每个 domain 三件套齐全
  ⑩ 生成 INDEX.md
```

### 工具

| 步骤 | 工具 |
|------|------|
| xlsx → md | Python + openpyxl |
| PDF 提取 | Claude 读 PDF 页（每次 ≤8 页） |
| 自动校验 | Python 脚本 |
| 页码索引 | Claude 读 PDF 目录页 |

---

## 九、执行策略与断点恢复（已确认）

### 页码索引（Phase 2 前置产物）

在 PDF 提取之前，先建立结构化页码索引文件 `.work/page_index.json`：

```json
{
  "AE": {"spec": [134, 137], "assumptions": [137, 140], "examples": [140, 142]},
  "CM": {"spec": [93, 97], "assumptions": [97, 100], "examples": [100, 103]},
  ...
}
```

用途：
- 精确控制每次 PDF 读取的页码范围，避免多读或少读
- 作为断点恢复的基础数据——中断后无需重新定位页码
- 验证阶段可用于比对提取完整性

### Token 效率策略

核心原则：**让 Python 做搬运，让 LLM 只做判断。**

| 环节 | 方式 | LLM Token 消耗 |
|------|------|----------------|
| spec.md（63 个） | Python + openpyxl 直接生成 | **零** |
| terminology/ | Python + openpyxl 直接生成 | **零** |
| assumptions.md | LLM 读 PDF 目标页范围，一次一文件 | 按需，每次 3-8 页 |
| examples.md | 同上 | 按需，每次 3-8 页 |
| 清理/格式化 | 读取时直接按模板输出，不做二次加工 | 省一轮往返 |

**不做"先全读再总结"，而是"读一段写一段"——每次只读目标页范围，直接输出 md 文件。**

### 断点恢复机制

使用进度追踪文件 `.work/progress.json`：

```json
{
  "phase": "phase3_pdf_extraction",
  "completed": ["AE/spec.md", "AE/assumptions.md", "AE/examples.md", "CM/spec.md"],
  "current": "CM/assumptions.md",
  "status": "in_progress",
  "last_updated": "2026-04-13T12:00:00"
}
```

工作流程：
1. 每完成一个 md 文件 → 立即写入磁盘 + 更新 progress.json 的 completed 列表
2. 如果中断（断电 / usage 超限 / 网络问题）→ 下次启动时读 progress.json
3. 跳过所有 `completed` 的文件，从 `current` 重新开始
4. 已写入磁盘的 md 文件不会丢失

**原子单位：单个 md 文件。一个文件要么完整生成并记录为 completed，要么中断后整个重做。不存在"半个文件"的状态。**

### Agent 执行策略

| 阶段 | 策略 | 理由 |
|------|------|------|
| Phase 1: xlsx → md | **单 agent** | Python 脚本一次跑完，无并发需求 |
| Phase 2: 页码索引 | **单 agent** | 扫描 TOC 是线性任务 |
| Phase 3: PDF → md | **单 agent，按批次串行** | PDF 提取需精度控制，并发增加出错风险；串行配合 progress.json 断点恢复简单 |
| Phase 4: 补充内容 | **单 agent** | 同 Phase 3 |
| Phase 5: 验证 | **多 agent 并发** | 验证是无状态的，每个文件独立检查，适合并行加速 |

Phase 3 不用多 agent 并发的原因：
- PDF 提取最怕内容丢失，需逐个确认质量
- 多 agent 同时写文件容易产生冲突和追踪困难
- 串行执行下用户可在每个批次之间抽检，及时纠偏

---

## 十、待执行

- [x] 源文件关系梳理（01 文档）
- [x] 目录结构设计
- [x] SDTM vs SDTMIG 关系调研
- [x] Terminology 分组策略
- [x] 技术约束与文件大小策略
- [x] 文件格式模板设计
- [x] 技术实现方案
- [ ] **开始执行 Phase 1：自动化部分（spec.md + terminology）**
- [ ] 开始执行 Phase 2：建立页码索引
- [ ] 开始执行 Phase 3-5：PDF 提取 + 校验 + 收尾
