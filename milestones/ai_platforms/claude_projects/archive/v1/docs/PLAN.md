# Phase 6.5 Claude Project — 压缩部署落地计划 (方案 B)

> 状态: **计划已拟定，待执行**
> 创建日期: 2026-04-17
> 所属 Phase: 6.5 AI 平台部署 / Claude Projects 路线
> 上游文档: [`ROADMAP.md`](ROADMAP.md) (高层路线) / [`../README.md`](../README.md) (三平台总览)
> 目标产出: `ai_platforms/claude_projects/output/`

---

## 1. 需求的产生

### 1.1 背景

Phase 1-6 已产出 295 个结构化 Markdown 文件（总 2,527K tokens），覆盖 63 个 SDTM 域 + 术语 + 模型 + 章节。Phase 7 自建 RAG 尚未实施，在此之前用 Phase 6.5 把知识库部署到三大 AI 平台让它"立即可用"。

Claude 路线的定位是 **"精确查询 + 规则推理"**——利用 Claude Projects 全上下文的优势，做跨域推理、变量属性查询、规则链追踪。

### 1.2 核心矛盾

| 维度 | 现状 | 要求 |
|------|------|------|
| Claude Project 容量上限 | ~200K tokens (硬约束) | 必须塞下 |
| 全量知识库 | 2,527,153 tokens (tiktoken 实测) | 超标 **12.6 倍** |
| 用户诉求 | 全量覆盖 + 允许二次创作 | 不能简单丢类别 |

### 1.3 衍生需求

1. **覆盖完整性**：63 域、术语、示例、规则都要"能被问到"，不能让用户问"AE 的 examples 里有什么？"时 Claude 完全不知道
2. **推理能力优先**：Claude 的强项是跨域规则推理，不是大规模枚举——压缩方向要突出推理能力，降低枚举类内容
3. **边界兜底**：Claude 答不了的问题要明确指向原文件位置，不能让用户陷入"死胡同"
4. **可复现 / 可迭代**：压缩过程必须脚本化，未来 knowledge_base 更新后能一键重跑
5. **不影响主知识库**：`knowledge_base/` 是只读源，所有压缩产物独立存放

---

## 2. 解决方法的讨论

### 2.1 候选路径

| # | 路径 | 可达压缩率 | 核心问题 |
|---|------|-----------|----------|
| 1 | **无损压缩** (去空格、紧凑表格) | -40% 极限 | 离 12.6x 差太远 |
| 2 | **多 Project 分片** | 每片 ≤200K | 失去跨片推理能力，违背 Claude 优势 |
| 3 | **外置 terminology** (丢给 Gemini/RAG) | -77% (terminology 全丢) | 破坏"单一入口"，用户需要跨平台切换 |
| 4 | **二次创作** (重新编码 + 降级) | -92% 可达 | 内容形态变化，需设计转换规则 |

### 2.2 三套二次创作方案对比

| 方案 | 思路 | 目标 tokens | 覆盖完整性 | 实施成本 |
|------|------|-------------|-----------|---------|
| **方案 A** 激进裁剪 | 只保留规则骨架，砍 examples + terminology | ~150K | 60% (数据和术语完全问不到) | 低 |
| **方案 B** 全覆盖重写 | 保留所有类别"存在感"，降级数据密集内容 | ~195K | 95% (数据降级为目录，术语降级为映射) | 中 |
| **方案 C** 极限重组 | 整库重新组织为"紧凑 SDTM 手册" | ~150K | 90% (统一缩写 + 合并) | 高 |

### 2.3 风险识别

| 风险 | 应对 |
|------|------|
| R1: 重写引入错误 | 脚本化处理 + 原文件只读 + 保留 `<!-- source: ... -->` 溯源标记 |
| R2: 降级内容用户体验差 | System Prompt 明确声明边界 + 给出"原始数据在哪里"的答案模板 |
| R3: 压缩后总量仍超 200K | 分级压缩策略 + 每个脚本跑完测 token，预留 5K buffer |
| R4: Claude 引用合并后文件时溯源混乱 | 合并段落前加注释块标记源路径，System Prompt 要求 Claude 引用时使用源路径 |

---

## 3. 取舍以及决定

### 3.1 最终决定：**采用方案 B（全覆盖重写）**

**选择理由**：
- 方案 A 太激进，Claude 被问到 examples/terminology 时只能说"不知道"，体验跌崖
- 方案 C 工作量大但收益（150K → 195K）并不显著优于方案 B
- 方案 B 在"覆盖完整性"和"工作量"之间取得最优平衡，且压缩后仍留 5K buffer 供 System Prompt 预留

### 3.2 关键边界决策

| # | 决策项 | 结论 | 理由 |
|---|-------|------|------|
| D1 | 63 × `spec.md` 处理 | 合并为 1 份 **Mega Spec**，按域分节 | 去除重复 frontmatter/标题，表格可合并 |
| D2 | 63 × `assumptions.md` 处理 | **条目化压缩**（去叙述，留规则） | Claude 需要的是规则本身，不是解释段落 |
| D3 | 63 × `examples.md` 处理 | **降级为目录**：每域列"Example 1-N: 一句话描述"，不保留数据表 | examples 数据表 220K tokens，价值密度最低 |
| D4 | terminology/ 处理 | **降级为映射表**：`CT Code \| Codelist Name \| 关联 Domain \| Term 数` | 1944K → 15K，保留"能定位到哪个 codelist"的能力 |
| D5 | `ch04_general_assumptions.md` 处理 | **完整保留** (60K+) | 推理基础，任何压缩都会伤害推理能力 |
| D6 | 其他 chapters (ch01/02/03/08/10) | 精简 30-50%（去举例，保留定义/规则） | 非推理核心，压缩换空间 |
| D7 | `VARIABLE_INDEX.md` 处理 | **行内紧凑化**：`AESEQ(Id/R), AEDECOD(Tp/R)` | 原始是表格浪费 tokens |
| D8 | `ROUTING.md` 处理 | **原样保留** (2.7K，极小) | 路由骨架，是 System Prompt 的延伸 |
| D9 | `model/` 处理 | **原样保留** (17K，足够小) | SDTM v2.0 模型，高价值低占用 |
| D10 | System Prompt 边界提示 | 明确声明：`examples 数据不在上下文`、`terminology 具体值不在上下文`，告知原文件位置 | R2 风险兜底 |

### 3.3 Token 预算（硬约束 ≤195K，5K 留给对话）

| 分区 | 原始 tokens | 目标 tokens | 压缩率 | 产出文件 |
|------|-----------:|-----------:|-------:|---------|
| ROUTING.md | 2,657 | 2,657 | 0% | `00_routing.md` |
| INDEX.md (精简) | 5,032 | 3,000 | 40% | `01_index.md` |
| chapters (ch04 全保留 + 其他精简) | 60,525 | 45,000 | 26% | `02_chapters.md` |
| model/ (全保留) | 17,573 | 17,573 | 0% | `03_model.md` |
| VARIABLE_INDEX.md (行内紧凑) | 38,452 | 15,000 | 61% | `04_variable_index.md` |
| 63 × spec.md → Mega Spec | 184,943 | 60,000 | 68% | `05_mega_spec.md` |
| 63 × assumptions.md (条目化) | 53,708 | 20,000 | 63% | `06_assumptions.md` |
| 63 × examples.md → 目录 | 219,814 | 10,000 | 95% | `07_examples_catalog.md` |
| terminology → 映射表 | 1,944,449 | 15,000 | 99% | `08_terminology_map.md` |
| System Prompt | — | 5,000 | — | `system_prompt.md` |
| **合计** | **2,527,153** | **193,230** | **92.4%** | — |

**Buffer**: 200K - 193K = **~7K** 预留给对话历史和 Claude 内部开销。

---

## 4. 落地实现的方案

### 4.1 产出物清单

```
ai_platforms/claude_projects/
├── PLAN.md                    ← 本计划
├── ROADMAP.md                 ← 高层路线 (已存在)
├── scripts/                   ← 新增：压缩脚本 (Python)
│   ├── count_tokens.py        token 测算工具 (tiktoken)
│   ├── compress_index.py      INDEX 精简
│   ├── compress_chapters.py   chapters 合并 + 精简
│   ├── merge_model.py         model 6 文件合并 (不压缩)
│   ├── compress_var_index.py  VARIABLE_INDEX 行内化
│   ├── merge_specs.py         63 spec → Mega Spec
│   ├── compress_assumptions.py 63 assumptions 条目化
│   ├── catalog_examples.py    63 examples → 目录
│   ├── catalog_terminology.py terminology → 映射表
│   └── build_all.py           一键构建 + 总量验证
└── output/                    ← 最终上传内容
    ├── system_prompt.md       Project Instructions
    ├── 00_routing.md
    ├── 01_index.md
    ├── 02_chapters.md
    ├── 03_model.md
    ├── 04_variable_index.md
    ├── 05_mega_spec.md
    ├── 06_assumptions.md
    ├── 07_examples_catalog.md
    ├── 08_terminology_map.md
    └── upload_manifest.md     ← 上传清单 + 每文件实测 token + 总量
```

### 4.2 脚本通用设计要点

1. **幂等**：所有脚本读 `knowledge_base/`（只读），写 `output/`，反复跑结果一致
2. **原文件不动**：源知识库文件全部只读打开
3. **源路径标注**：合并型输出（Mega Spec、chapters 等）每段前加 `<!-- source: domains/AE/spec.md -->`
4. **Token 自测**：每个脚本结束打印 `[产出] <file>: <tokens> tokens`
5. **命令一致**：统一在 `ai_platforms/claude_projects/` 目录执行，使用相对路径

### 4.3 核心压缩算法说明

#### 4.3.1 Mega Spec (D1)
- 读 63 个 `spec.md`，去除每个文件的 `# Domain XX` 大标题和 frontmatter
- 每域输出一个 `## AE — Adverse Events` 小节
- Specification 表合并成本域的一张表（去除列内 padding 空格）
- Cross References 段保留但紧凑化（行内列 CT Code 而非表格）

#### 4.3.2 Assumptions 条目化 (D2)
- 每域一个 `### AE` 小节
- 保留层级化编号 (1, 2, 2a, 2b...) 和规则陈述
- 删除：冗长叙述段、示例性描述、PDF 页码引用（这些可以从源文件查）
- 保留：变量名、codelist 引用、约束性规则句

#### 4.3.3 Examples 目录 (D3)
- 每域一个 `### AE` 小节
- 列出 `- Example 1: 严重程度变化 AEGRPID 分组 (源: domains/AE/examples.md)`
- 不保留任何数据表
- 保留共享 examples 说明（EX/EC, MB/MS, TU/TR, PC/PP）

#### 4.3.4 Terminology 映射表 (D4)
- 表头：`CT Code | Codelist Name | Data Type | Related Domain(s) | Term Count | Source File`
- 源自 terminology/ 所有 codelist 文件的 frontmatter/表头解析
- 保留 `C66742 | NY | Char | 多域 | 4 | terminology/core/general.md` 这种一行一 codelist
- 不保留具体 Term 值

#### 4.3.5 System Prompt 设计
- **角色**: SDTM/CDISC v3.4 + SDTM v2.0 领域专家
- **资料索引**: 列出 9 个上传文件的内容说明
- **路由规则**: 压缩自 ROUTING.md 的 7 类问题路径
- **回答规范**:
  - 变量引用: `AE.AEDECOD (Role: Topic, Core: Req)`
  - 章节引用: `SDTMIG §4.2.8.1` (无 PDF 页码要求)
  - 源溯源: 引用时使用 `<!-- source: ... -->` 标记的原路径
- **边界处理模板**:
  - 问具体 example 数据: "该示例详细数据在 `domains/XX/examples.md Example N`，本 Project 仅有目录"
  - 问 terminology term 值: "CT Code CXXXXX 对应 codelist `XX`，具体 term 值在 `terminology/core/xx.md`"

### 4.4 实施顺序

| Step | 任务 | 输出 | Token 检查 |
|------|------|------|-----------|
| 1 | 写 `count_tokens.py` | 工具 | — |
| 2 | 写 `compress_index.py` | `01_index.md` | ≤3K |
| 3 | 写 `compress_chapters.py` | `02_chapters.md` | ≤45K |
| 4 | 写 `merge_model.py` | `03_model.md` | ≤18K |
| 5 | 写 `compress_var_index.py` | `04_variable_index.md` | ≤15K |
| 6 | 写 `merge_specs.py` | `05_mega_spec.md` | ≤60K |
| 7 | 写 `compress_assumptions.py` | `06_assumptions.md` | ≤20K |
| 8 | 写 `catalog_examples.py` | `07_examples_catalog.md` | ≤10K |
| 9 | 写 `catalog_terminology.py` | `08_terminology_map.md` | ≤15K |
| 10 | 复制 `ROUTING.md` → `00_routing.md` | `00_routing.md` | ~3K |
| 11 | 写 `system_prompt.md` | `system_prompt.md` | ≤5K |
| 12 | 写 `build_all.py` (一键构建 + 汇总) | `upload_manifest.md` | **总量 ≤195K** |
| 13 | 手工创建 Claude Project 并上传 | 在线 Project | — |
| 14 | 执行测试矩阵 | 测试记录 | — |

---

## 5. 结果的检查

### 5.1 Layer 1：自动检查（脚本层）

| # | 检查项 | 标准 | 执行方式 |
|---|-------|------|---------|
| C1 | 总 token 数 | ≤ 195,000 | `build_all.py` 汇总 |
| C2 | 63 域全覆盖 (Mega Spec) | 63/63 域出现 `## XX —` | grep 计数 |
| C3 | 63 域全覆盖 (Assumptions) | 63/63 域出现 `### XX` | grep 计数 |
| C4 | 63 域全覆盖 (Examples 目录) | 63/63 域出现 `### XX` | grep 计数 |
| C5 | Cross References 保留 | Mega Spec 出现 `## Cross References` 63 次 | grep 计数 |
| C6 | ch04 完整保留 | 字符数 ≥ 原文件 95% | 对比 `chapters/ch04_general_assumptions.md` |
| C7 | ROUTING 原样搬运 | `00_routing.md` 与源 MD5 一致 | md5 对比 |
| C8 | 源路径标注 | 每个合并输出包含 `<!-- source: -->` | grep 计数 |
| C9 | Terminology 映射覆盖率 | 映射表行数 ≥ 1000 (原 1005 codelist) | 行数统计 |
| C10 | 输出文件数 | `output/` 有且仅有 11 个 .md (9 内容 + routing + system_prompt) | ls |

### 5.2 Layer 2：人工抽样测试（上传 Claude Project 后）

测试矩阵（复用 ROADMAP Step 4 + 新增边界测试）：

| # | 测试类型 | 示例问题 | 期望行为 |
|---|---------|---------|---------|
| T1 | 变量精确查询 | "AE.AEDECOD 的 Core 属性是什么？" | 引用 Mega Spec，答 "Expected" |
| T2 | 规则推导 | "AE 严重程度变化如何记录？" | 引用 ch04 + AE assumptions，给出 AEGRPID 方案 |
| T3 | 跨域关联 | "PC 和 PP 通过 RELREC 关联的 4 种方法？" | 追 Cross References，列出 Method A-D |
| T4 | 反向查询 | "哪些域有 EPOCH 变量？" | 查 VARIABLE_INDEX，给出完整域列表 |
| T5 | 路由准确性 | "如何判断变量是否需要提交到 SUPP--？" | 引用 ch08 相关规则 |
| T6 | **边界-examples** | "AE Example 2 的具体数据是什么？" | 正确回复"目录中有，数据在 domains/AE/examples.md Example 2" |
| T7 | **边界-terminology** | "CT Code C66742 有哪些具体值？" | 正确回复"对应 codelist NY，值表在 terminology/core/general.md" |
| T8 | **边界-不编造** | "CV 域的所有变量值范围是什么？" | 回复 "变量定义在本 Project，具体值范围需查 examples/terminology" |

**PASS 条件**: T1-T8 全部符合预期；Claude 的每次回答都能给出"源路径"（不是凭空回答）。

### 5.3 压缩率统计（收尾归档）

记录到 `upload_manifest.md`：

```
| 分区 | 原 tokens | 压缩后 | 压缩率 | 是否有损 |
|------|----------|--------|--------|---------|
| ...                                     |
| 合计 | 2,527,153 | <实测> | <计算> | 部分有损 (examples/terminology 降级) |
```

---

## 6. 如何收尾

### 6.1 收尾触发

**前提**: Layer 1 + Layer 2 全部 PASS，用户确认 Claude Project 可用。

### 6.2 文档更新（按 Chain B + Chain C + Chain E）

- [ ] **Chain B (工作日志)**:
  - [ ] `.work/meta/worklog.md` 追加工作记录（日期、策略、压缩率、测试结果）
  - [ ] `docs/PROGRESS.md` 更新 Phase 6.5 Claude 状态为 "已完成"
- [ ] **Chain C (新阶段/新目录注册)**:
  - [ ] `.work/MANIFEST.md` 注册 `ai_platforms/claude_projects/scripts/` 和 `output/`
- [ ] **Chain E (方案变更)**:
  - [ ] `ai_platforms/claude_projects/ROADMAP.md` 状态改为"已完成"，补充最终策略决策
  - [ ] `ai_platforms/README.md` Claude 路线状态更新

### 6.3 产物归档

- [ ] `output/upload_manifest.md` 记录：上传文件清单 + 每文件 token + 总量 + 实际 Project 容量使用率
- [ ] `output/test_results.md` 记录：Layer 2 测试矩阵全部问答截图/文本
- [ ] System Prompt 的路由部分标注"可复用于 Phase 6.5 ChatGPT / Gemini 路线"
- [ ] 压缩脚本全部保留在 `scripts/`，未来 knowledge_base 更新可一键重跑

### 6.4 对下游的输入

- **对 Phase 6.5 其他平台**: System Prompt 和路由设计可复用；压缩脚本产出的文件可能也适合 ChatGPT（如合并版 Mega Spec）
- **对 Phase 7 自建 RAG**: Claude Project 的使用反馈（哪些问题答得好、哪些弱）作为 RAG 意图路由设计的参考

### 6.5 完结信号

满足以下全部条件后，Phase 6.5 Claude 路线视为完结：

1. ✅ `output/` 下 11 个文件齐备，总 token ≤195K
2. ✅ Layer 1 的 10 项自动检查全部 PASS
3. ✅ Claude Project 创建成功，Layer 2 的 8 项测试全部 PASS
4. ✅ 四条变更链（B/C/E）全部走完
5. ✅ `upload_manifest.md` + `test_results.md` 归档
6. ✅ 用户确认日常使用体验

满足后进入 Phase 6.5 第二条路线 (ChatGPT GPT)。

---

## 7. Claude Code 执行手册（Agent 调度与任务分配）

> 本章把 §4.4 的 14 个 Step 翻译为 Claude Code 可直接执行的指令剧本。
> 阅读对象：未来执行本 PLAN 的 Claude Code 主 agent (你)。

### 7.1 执行总原则（强制遵守）

继承 `.work/meta/retrospective.md` 的 4+3 条预防规则，针对本计划进一步强化：

| # | 原则 | 适用方式 |
|---|------|---------|
| P1 | **量化 PASS 标准** | 每个 Step 完成后必须打印 `[产出] <file>: <tokens> tokens`，与 §3.3 预算对比 |
| P2 | **写/审分离** | 写脚本和复核脚本不能由同一个 subagent 完成。复核必须由独立 `code-reviewer` 或 `verifier` agent 跑 |
| P3 | **AI 估算值标记** | 任何"看起来差不多"的 token 估算都不能写入 manifest，只能写实测值 |
| P4 | **人工抽查检查点** | Step 5 / Step 9 / Step 12 后**主动停下汇报用户**，不擅自连续推进 |
| P5 | **源文件只读** | `knowledge_base/` 下任何文件不允许 Edit/Write，只能 Read |
| P6 | **subagent 上下文隔离** | 每个压缩脚本由独立 `executor` subagent 写，避免主上下文累积 9 个脚本 + 9 份产出 |
| P7 | **逐 Step 可中断恢复** | 每个 Step 完成立即更新 `output/_progress.json`，允许新 session 续跑 |

### 7.2 Agent 角色分配表

| 角色 | subagent_type | 职责 | 调用时机 |
|------|--------------|------|---------|
| **主控** | (你本身, Opus) | 任务分发、checkpoint 决策、向用户汇报 | 全程 |
| **脚本作者** | `oh-my-claudecode:executor` (model=opus) | 写单个压缩脚本 + 跑通 + 自测 token | Step 1-12（每个 Step 一个） |
| **脚本复核** | `oh-my-claudecode:code-reviewer` 或 `pr-review-toolkit:code-reviewer` | 独立读脚本+产出，验 P1/P5/源路径标注 | 每个 Step 写完后立刻调用 |
| **总量验证** | `oh-my-claudecode:verifier` | 跑 `build_all.py` + 比对 §5.1 的 10 项 C1-C10 | Step 12 |
| **System Prompt 起草** | `oh-my-claudecode:writer` (Haiku 起稿) → `executor` (Opus 终稿) | 写 `system_prompt.md`，避免主上下文写文档 | Step 11 |
| **测试矩阵执行** | (用户在 Claude Project 网页端手动) | T1-T8 真实问答 | Step 14 |

**禁止**：
- 用 `general-purpose` agent 写脚本（缺乏 SDTM 项目上下文，容易跑偏）
- 用同一个 subagent 同时写脚本和复核（违反 P2）
- 让 subagent 直接 Edit `output/` 之外的文件

### 7.3 上下文管理策略

主控 agent (你) 的上下文 ≈ 200K，必须严格控制：

**主控只保留**：
- 本 PLAN.md 全文
- `_progress.json` 当前状态
- 每个 Step 的"一行结论"（脚本路径 + 产出 token 数 + PASS/FAIL）
- 失败时的关键错误日志（≤200 行）

**主控不保留**：
- 任何脚本源代码（让 subagent 写完直接落盘，主控不读）
- 任何压缩产出文件内容（>3K tokens 的全部交给 subagent 处理）
- 中间调试输出（subagent 内部消化）

**Subagent 调用模板**（统一格式）：

```
description: <Step N - 任务名>
subagent_type: oh-my-claudecode:executor
model: opus
prompt:
  ## 上下文
  你正在执行 SDTM Phase 6.5 Claude Project 压缩部署的 Step <N>。
  完整计划见 ai_platforms/claude_projects/PLAN.md §<对应小节>。

  ## 你的输入
  - 源文件: <绝对路径列表>
  - 参考决策: 见 PLAN.md §3.2 决策 D<n>
  - Token 目标: ≤<X>K tokens

  ## 你的产出
  1. 写脚本: ai_platforms/claude_projects/scripts/<name>.py
  2. 跑脚本生成: ai_platforms/claude_projects/output/<file>.md
  3. 用 count_tokens.py 测产出 token 数

  ## 强制要求
  - 源文件只读 (P5)
  - 输出第一行加 `<!-- generated by scripts/<name>.py at <timestamp> -->`
  - 合并型输出每段前加 `<!-- source: <原路径> -->`
  - 脚本可重复执行 (idempotent)

  ## 完成标准
  打印一行：`[Step N DONE] <file>: <tokens> tokens (target: ≤<X>K)`
  并报告任何与目标偏差 >10% 的情况。

  ## 不要做
  - 不要修改 knowledge_base/ 任何文件
  - 不要写任何 .md 文档说明
  - 不要解释你做了什么，只报告结果
```

### 7.4 Step-by-Step 执行剧本

> 每个 Step 包含：**触发条件 / Agent 调度 / 输入 / 验证 / 检查点行为**

#### Step 1: `count_tokens.py` 工具

| 项 | 内容 |
|---|------|
| Agent | `executor` (Opus) |
| 输入 | tiktoken 库 (`cl100k_base`) |
| 产出 | `scripts/count_tokens.py`，CLI: `python count_tokens.py <file_or_dir>` |
| 验证 | 主控直接 Bash 跑 `python count_tokens.py knowledge_base/ROUTING.md`，预期输出 `2657 tokens` |
| 检查点 | 否（基础工具，PASS 即继续） |

#### Step 2: `compress_index.py`

| 项 | 内容 |
|---|------|
| Agent | `executor` (Opus) → `code-reviewer` 复核 |
| 输入 | `knowledge_base/INDEX.md` |
| 算法 | 删除 ASCII art、合并目录树为单层、去重描述 |
| 产出 | `output/01_index.md` ≤ 3K tokens |
| 复核 prompt | "对比 source 和 output，确认 (a) 入口指引未丢 (b) 9 类文件路径仍可定位 (c) token ≤3000" |
| 检查点 | 否 |

#### Step 3: `compress_chapters.py`

| 项 | 内容 |
|---|------|
| Agent | `executor` (Opus) → `code-reviewer` 复核 |
| 输入 | `knowledge_base/chapters/ch01-ch10` 6 文件 |
| 算法 | ch04 完整保留；ch01/02/03/08/10 删除冗余举例段落、保留所有定义/规则/Specification 表 |
| 产出 | `output/02_chapters.md` ≤ 45K tokens |
| 复核 prompt | "确认 ch04 字符数 ≥ 源文件 95%；其他章节的所有 `### ` 三级标题完整保留" |
| 检查点 | **是** — 因为 ch04 是推理基础，主控必须把脚本输出 token 数报给用户确认再继续 |

#### Step 4: `merge_model.py`

| 项 | 内容 |
|---|------|
| Agent | `executor` (Sonnet 即可) → `code-reviewer` |
| 输入 | `knowledge_base/model/` 6 文件 |
| 算法 | 直接拼接 + 加源路径注释，几乎不压缩 |
| 产出 | `output/03_model.md` ≤ 18K tokens |
| 检查点 | 否 |

#### Step 5: `compress_var_index.py`

| 项 | 内容 |
|---|------|
| Agent | `executor` (Opus) → `code-reviewer` |
| 输入 | `knowledge_base/VARIABLE_INDEX.md` |
| 算法 | 通用变量段保留为表；专属变量段从表格转行内 `AESEQ(Id/R), AEDECOD(Tp/R)`；CT 引用段保留分组 |
| 产出 | `output/04_variable_index.md` ≤ 15K tokens |
| 复核 prompt | "随机抽 5 个域，确认所有 spec.md 中的变量都在行内列表里，0 漏；星号 (跨域差异) 全部保留" |
| 检查点 | **是** — 反向索引是路由核心，主控向用户汇报"压缩后是否仍能定位变量？" |

#### Step 6: `merge_specs.py` ⚠️ 最大风险点

| 项 | 内容 |
|---|------|
| Agent | `executor` (Opus, 必须) → `code-reviewer` (独立 Opus) |
| 输入 | 63 × `domains/*/spec.md` |
| 算法 | 见 §4.3.1。关键：保留 Variable Name / Label / Type / Role / Core / CT Code / Notes 7 列；Cross References 段从表格转紧凑列表 |
| 产出 | `output/05_mega_spec.md` ≤ 60K tokens |
| 复核 prompt | "(1) 63/63 域均出现 `## XX —`；(2) 抽 AE/DM/LB/CV/TS 5 域，每个变量都在；(3) 每域 Cross References 段保留" |
| 检查点 | **是** — 此 Step 失败整个 PLAN 失败。主控必须停下，让用户抽查 Mega Spec 的 1-2 个域 |
| 失败回退 | 若 token 超 60K，调整为：删除 Cross References 表格 → 保留 CT Code 内联引用 → 重测 |

#### Step 7: `compress_assumptions.py`

| 项 | 内容 |
|---|------|
| Agent | `executor` (Opus) → `code-reviewer` |
| 输入 | 63 × `domains/*/assumptions.md` |
| 算法 | 见 §4.3.2。保留编号体系 + 规则陈述；删 PDF 页码引用、冗长背景叙述 |
| 产出 | `output/06_assumptions.md` ≤ 20K tokens |
| 复核 prompt | "随机抽 AE/MH/LB 3 域，列出原文所有顶层 assumption 编号，确认压缩版无遗漏" |
| 检查点 | 否 |

#### Step 8: `catalog_examples.py`

| 项 | 内容 |
|---|------|
| Agent | `executor` (Sonnet) → `code-reviewer` |
| 输入 | 63 × `domains/*/examples.md` |
| 算法 | 见 §4.3.3。每个 Example 仅保留一句话标题 + 源路径 + 行号 |
| 产出 | `output/07_examples_catalog.md` ≤ 10K tokens |
| 复核 prompt | "(1) 63/63 域有 ### 节；(2) 共享 examples (EX/EC, MB/MS, TU/TR, PC/PP) 4 处明确标注共享关系" |
| 检查点 | 否 |

#### Step 9: `catalog_terminology.py` ⚠️ 高压缩比

| 项 | 内容 |
|---|------|
| Agent | `executor` (Opus) → `code-reviewer` |
| 输入 | `knowledge_base/terminology/` 全部 91 文件 |
| 算法 | 见 §4.3.4。解析每个 codelist 的 frontmatter / 标题 / 表头，输出一行映射 |
| 产出 | `output/08_terminology_map.md` ≤ 15K tokens |
| 复核 prompt | "(1) 1005 codelist 全部有一行；(2) 'Related Domain(s)' 列覆盖率 ≥80%；(3) 不出现具体 Term 值" |
| 检查点 | **是** — 99% 压缩率最容易丢东西。主控向用户汇报"是否所有 codelist 都被映射？" |

#### Step 10: 复制 ROUTING.md

| 项 | 内容 |
|---|------|
| Agent | 主控直接 Bash `cp` |
| 验证 | `md5 knowledge_base/ROUTING.md` == `md5 output/00_routing.md` |
| 检查点 | 否 |

#### Step 11: `system_prompt.md`

| 项 | 内容 |
|---|------|
| Agent | `executor` (Opus) → `code-reviewer` (Opus) |
| 输入 | §4.3.5 设计要点 + §3.3 文件清单 + 8 个测试用例期望行为 |
| 产出 | `output/system_prompt.md` ≤ 5K tokens |
| 复核 prompt | "(1) 9 个文件都被介绍；(2) 4 类边界处理模板齐全；(3) 引用规范明确" |
| 检查点 | **是** — System Prompt 决定 Claude 行为，必须用户审阅文本后批准 |

#### Step 12: `build_all.py` + Layer 1 验证

| 项 | 内容 |
|---|------|
| Agent | `executor` 写脚本 → `verifier` 跑全量验证 |
| 输入 | 全部 11 个产出文件 |
| 算法 | 顺序跑全部 9 个压缩脚本 + 跑 §5.1 的 C1-C10 检查 + 生成 `upload_manifest.md` |
| 产出 | `output/upload_manifest.md` 含每文件 token + 总量 + 10 项检查结果 |
| 验证 | **总量必须 ≤ 195K**；C1-C10 全 PASS |
| 检查点 | **是** — 主控向用户汇报最终 token 报告，等待"上传到 Claude Project 吗？"决策 |
| 失败回退 | 若 C* 任一 FAIL，回到对应 Step 的 executor 修脚本，不要在 build 阶段 hack |

#### Step 13: 上传到 Claude Project（手动）

| 项 | 内容 |
|---|------|
| Agent | (用户操作) |
| 主控行为 | 把 11 个文件路径打印给用户，附 `system_prompt.md` 内容（粘贴到 Project Instructions），列出操作步骤 |
| 等待 | 用户回报"上传完成 + 显示容量 X%" |

#### Step 14: Layer 2 测试矩阵（手动 + 记录）

| 项 | 内容 |
|---|------|
| Agent | 用户在 Claude Project 网页端跑 T1-T8 |
| 主控行为 | 把 8 个测试问题打印给用户，提供"期望行为"对照表，提示用户把回答粘贴回来 |
| 评判 | 每个 T 由用户判 PASS/FAIL；FAIL 项主控分析根因（System Prompt 缺规则？文件压得过猛？） |
| 产出 | `output/test_results.md` |

### 7.5 并行调度策略

**可并行**（独立无依赖）：
- Step 4 (model 合并) 与 Step 5 (var_index)
- Step 7 (assumptions) 与 Step 8 (examples) 与 Step 9 (terminology)

**必须串行**：
- Step 1 (count_tokens) → 所有其他 Step
- Step 6 (Mega Spec) 完成后再做 Step 7 (assumptions 引用 spec 的变量)
- Step 12 (build_all) 必须全部完成后

**并行调用方式**（同一个消息中多个 Agent 工具）：

```
Agent(description="Step 7 assumptions", subagent_type="executor", prompt=...)
Agent(description="Step 8 examples", subagent_type="executor", prompt=...)
Agent(description="Step 9 terminology", subagent_type="executor", prompt=...)
```

主控等三者都返回后，再统一调 3 个 `code-reviewer` 并行复核。

### 7.6 失败处理策略

| 失败类型 | 处理 |
|---------|------|
| Subagent 报告 token 超目标 ≤10% | 接受，记录到 manifest，但需在 Step 12 总量里吸收 |
| 超目标 >10% | 回到该 Step，给 executor 重新分配，prompt 中明确"上次产出 X tokens 超标，请进一步压缩 Y 段落" |
| 复核 reviewer 提出 ≥1 个高优先问题 | 不要让 executor 自己改，开新 executor + 新 reviewer 循环 |
| 总量 195K 仍超 | 优先压缩顺序：terminology > examples > spec Cross References > VARIABLE_INDEX > chapters 非 ch04 |
| 脚本 bug 导致产出错误 | 主控不直接 Edit 脚本，开新 `debugger` subagent 修；修完再走 reviewer |
| 上传后 Claude 行为异常 | 不重做压缩，先调 System Prompt（Step 11 重跑） |

### 7.7 检查点与用户互动协议

主控在以下时机**必须停下**，主动向用户汇报并等待批复：

| 时机 | 汇报内容 | 等待批复内容 |
|------|---------|------------|
| Step 3 完成 | "ch04 是否完整保留？token 数多少？" | "继续 Step 4-5" |
| Step 5 完成 | "VARIABLE_INDEX 压缩后样例" | "继续 Step 6" |
| Step 6 完成 | "Mega Spec token + 抽样 1-2 个域" | "继续 Step 7-9" |
| Step 9 完成 | "terminology map 1005 行覆盖率" | "继续 Step 10-12" |
| Step 11 完成 | "System Prompt 完整文本" | "批准 / 修改" |
| Step 12 完成 | "总 token 报告 + Layer 1 PASS 表" | "上传到 Claude Project 吗？" |
| Step 14 完成 | "Layer 2 测试结果" | "Phase 6.5 Claude 收尾？" |

汇报模板：

```
=== Checkpoint @ Step <N> ===
本 Step 产出: <file> = <tokens> tokens (target ≤<X>K) [PASS/FAIL]
累计已完成: Step 1-<N>，总 token 进度 <累计>/195K
本 Step 关键发现: <一句话>
建议下一步: <Step N+1 描述>
是否继续？(yes / 调整 / 暂停)
```

### 7.8 进度持久化

每 Step 完成立即由主控更新 `output/_progress.json`：

```json
{
  "phase": "6.5-claude",
  "plan": "ai_platforms/claude_projects/PLAN.md",
  "current_step": 6,
  "completed": [
    {"step": 1, "output": "scripts/count_tokens.py", "tokens": 0, "status": "PASS"},
    {"step": 2, "output": "output/01_index.md", "tokens": 2876, "status": "PASS"},
    ...
  ],
  "checkpoints_acked": ["step3", "step5"],
  "last_updated": "2026-04-17T..."
}
```

新 session 恢复协议：
1. 读 `_progress.json` 找 `current_step`
2. 读 PLAN.md §7.4 对应 Step
3. 跳过 `completed` 中 status=PASS 的 Step
4. 从断点续跑

### 7.9 完结确认协议

主控在所有 Step 完成、用户确认 Layer 2 全 PASS 后，按 §6.2 走 Chain B/C/E：

1. 调一个 `executor` (Sonnet) 一次性更新 `worklog.md` + `PROGRESS.md` + `MANIFEST.md` + `ROADMAP.md` + `README.md` 5 个文件
2. 调 `git-master` 或主控直接做 commit + push（按 CLAUDE.md "收尾" 协议）
3. 主控向用户报告：单行总结 + 下一阶段建议（ChatGPT GPT 路线）

### 7.10 运行轨迹与 Evidence 记录

> 设计目标: 让任何人（包括未来的 Claude session、用户、复核者）能从 evidence 还原"谁在什么时候用什么 prompt 跑出了什么结果"。
> 设计先例: `.work/03_verification/results/repair_evidence.md`（Issue 2 修复时已验证有效）

#### 7.10.1 三层记录体系

| 层 | 文件 | 粒度 | 写入频率 | 用途 |
|----|------|------|---------|------|
| **L1 状态层** | `output/_progress.json` | 整体 | 每 Step 完成 | 断点恢复、进度查询 |
| **L2 轨迹层** | `output/evidence/trace.jsonl` | 事件 | 每个事件实时 | 时序回放、性能分析 |
| **L3 证据层** | `output/evidence/step_NN_*.md` | Step | 每 Step 完成 | 复核审计、根因分析 |

#### 7.10.2 文件布局

```
ai_platforms/claude_projects/output/
├── _progress.json                  ← L1 状态（已建）
└── evidence/
    ├── README.md                   ← evidence 使用规范（已建）
    ├── _step_template.md           ← L3 模板（已建，复制使用）
    ├── trace.jsonl                 ← L2 时序轨迹（已建，append-only）
    ├── step_01_count_tokens.md     ← L3 每 Step 一份
    ├── step_02_compress_index.md
    ├── ...
    ├── checkpoints/                ← 用户互动归档
    │   └── ckpt_step<NN>.md
    ├── subagent_prompts/           ← 完整 prompt 归档
    │   └── step_<NN>_<role>.md
    └── failures/                   ← 失败 attempt 归档（不删）
        └── step_<NN>_attempt_<M>.md
```

#### 7.10.3 主控操作流程（每 Step 必做）

```
┌──────────────────────────────────────────────────────────┐
│ Step N 启动                                               │
│  └─ 1. 写 trace.jsonl: {event: step_start, ...}          │
│  └─ 2. 更新 _progress.json: in_progress = N              │
│  └─ 3. 把 subagent prompt 落盘到                          │
│        evidence/subagent_prompts/step_NN_executor.md     │
│  └─ 4. 调 executor subagent                              │
└──────────────────────────────────────────────────────────┘
            │ (subagent 返回)
            ▼
┌──────────────────────────────────────────────────────────┐
│ Step N 复核                                               │
│  └─ 5. 落盘 reviewer prompt 到                            │
│        evidence/subagent_prompts/step_NN_reviewer.md     │
│  └─ 6. 调 reviewer subagent                              │
│  └─ 7. 复核 PASS:                                         │
│        - 写 trace.jsonl: {event: step_done, status: PASS}│
│        - 复制 _step_template.md → step_NN_<name>.md      │
│        - 填充 evidence 8 节                              │
│        - 更新 _progress.json: completed[] += {...}       │
│     复核 FAIL:                                            │
│        - 写 trace.jsonl: {event: step_fail, ...}         │
│        - 写 failures/step_NN_attempt_M.md                │
│        - 更新 _progress.json: failed[] += {...}          │
│        - 回到 Step N 启动 (attempt M+1)                  │
└──────────────────────────────────────────────────────────┘
            │ (PASS 路径)
            ▼
┌──────────────────────────────────────────────────────────┐
│ Step N Checkpoint 判定                                    │
│  └─ 8. 查 §7.7 是否需 checkpoint                          │
│     需要:                                                 │
│        - 写 checkpoints/ckpt_stepNN.md (待用户回应)      │
│        - 用 §7.7 模板向用户汇报                          │
│        - 等用户 ack                                       │
│        - 用户回应后补完 ckpt 文件，更新 _progress.json   │
│          checkpoints_acked[] += "stepNN"                 │
│     不需要:                                               │
│        - 直接进入 Step N+1                               │
└──────────────────────────────────────────────────────────┘
```

#### 7.10.4 trace.jsonl 事件类型

每行一个 JSON，append-only，**永不修改已有行**：

| event | 必填字段 | 说明 |
|-------|---------|------|
| `phase_init` | ts, phase, plan | 初始化（已记录） |
| `step_start` | ts, step, agent, model, attempt | Step 开始 |
| `subagent_done` | ts, step, role, duration_s, tokens_in, tokens_out | subagent 返回 |
| `step_done` | ts, step, output_file, tokens, target, status | Step 通过 |
| `step_fail` | ts, step, attempt, reason | Step 失败 |
| `checkpoint_open` | ts, step, summary | 等待用户 |
| `checkpoint_ack` | ts, step, response (yes/adjust/pause) | 用户回应 |
| `phase_done` | ts, total_tokens, total_steps, total_subagents | 全程结束 |

示例：
```json
{"ts":"2026-04-17T10:00:00Z","step":1,"event":"step_start","agent":"oh-my-claudecode:executor","model":"opus","attempt":1}
{"ts":"2026-04-17T10:01:30Z","step":1,"event":"subagent_done","role":"executor","duration_s":90}
{"ts":"2026-04-17T10:02:00Z","step":1,"event":"step_done","output_file":"scripts/count_tokens.py","tokens":0,"target":0,"status":"PASS"}
```

#### 7.10.5 Evidence 写作规范

每份 `step_NN_*.md` 必须填齐 `_step_template.md` 的 8 节：

1. **输入** — 源文件 + md5（可用 `md5 <file>` 取）
2. **Agent 调度** — 包含 subagent_prompts/ 链接，**完整 prompt 必须落盘**
3. **产出** — 实测 token、目标偏差、源路径标注计数
4. **复核结果** — reviewer 关键结论（≤200 字，主控压缩）
5. **偏差与处理** — 全 PASS 写"无偏差"
6. **Checkpoint** — 链接到 checkpoints/ 文件
7. **累计指标** — 当前 token 进度
8. **下一步** — 下一 Step + 阻塞情况

**Evidence 不可变原则**：
- 已写入的 evidence 不允许修改（除错别字）
- 失败 attempt 必须保留在 `failures/`，不删除
- 勘误统一在文末加 `## 勘误 (YYYY-MM-DD)` 段

#### 7.10.6 Subagent prompt 归档

每次调 subagent **必须**先把完整 prompt 落到 `subagent_prompts/step_NN_<role>.md`，再发 Agent 调用。这样：

- 用户可审 prompt 质量
- 失败时可看 prompt 是否写歪
- 未来可复用相同 prompt 模板

文件格式：
```markdown
# Step <N> <role> Prompt
> 调用时间: YYYY-MM-DD HH:MM
> Agent: oh-my-claudecode:executor
> Model: opus

## Description
<3-5 词描述>

## Prompt
<完整 prompt 原文>

## Subagent 返回结论（粘贴一行结论）
<返回的关键 1-3 行>
```

#### 7.10.7 Checkpoint 归档

用户每次回应后写 `checkpoints/ckpt_step<NN>.md`：

```markdown
# Checkpoint @ Step <N>
> 时间: YYYY-MM-DD HH:MM

## 主控汇报
<用 §7.7 模板汇报的原文>

## 用户回应
<原文>

## 决议
- 继续 / 调整 / 暂停
- 调整内容（如有）: ...
- 是否产生新 issue: 是 / 否（如有: ...）
```

#### 7.10.8 阶段汇报（每个 checkpoint 强制执行）

主控除了 §7.7 单 Step 汇报模板，**累计 3 个 Step 完成后必须发"阶段汇报"**，格式：

```
=== 阶段汇报 (Step <N1>-<N2> 完成) ===
完成: Step <N1>, <N2>, <N3>
总 token 进度: <X>K / 195K (<Y>%)
本阶段产出文件: <list>
本阶段调 subagent 总数: <N>
本阶段重试: <N>
Evidence 全部归档于: output/evidence/step_<NN>_*.md
关键发现: <1-3 条>
下一阶段: Step <N4>-<N5> (<描述>)
```

阶段汇报对应自然分组：
- 阶段 A: Step 1-3（基础工具 + 索引/章节）
- 阶段 B: Step 4-6（model + var_index + Mega Spec）
- 阶段 C: Step 7-9（assumptions + examples + terminology，可并行）
- 阶段 D: Step 10-12（routing + system_prompt + build）
- 阶段 E: Step 13-14（上传 + 测试）

#### 7.10.9 完结归档（Step 14 后）

主控必须产出 3 份"总结性 evidence"：

| 文件 | 内容 |
|------|------|
| `output/upload_manifest.md` | 11 个文件清单 + 每文件 token + 总量 + Layer 1 C1-C10 表 |
| `output/test_results.md` | T1-T8 完整问答 + PASS/FAIL 判定 + 根因（FAIL 时） |
| `output/evidence/_phase_summary.md` | 全程总结：Step 总耗时、subagent 总数、重试总数、checkpoint 总数、关键决策回顾 |

写完后在 `_progress.json` 中：
```json
{"status": "completed", "phase_done_at": "...", "ready_for_next_phase": "chatgpt_gpt"}
```

#### 7.10.10 Evidence 复核与可审计性

任何时刻，外部审计者（用户/未来 Claude/code-reviewer）应能：

1. 读 `_progress.json` → 知道当前在哪
2. 读 `trace.jsonl` 末尾 100 行 → 知道最近发生了什么
3. 读 `step_NN_*.md` → 知道某 Step 详细执行
4. 读 `subagent_prompts/step_NN_*.md` → 知道当时给 subagent 的指令
5. 读 `checkpoints/ckpt_stepNN.md` → 知道用户当时的决定
6. 读 `failures/` → 知道历史失败和原因

**断点恢复 SOP**（新 session）：
```
1. cat output/_progress.json | jq .next_step
2. tail -20 output/evidence/trace.jsonl
3. ls output/evidence/failures/  (有失败说明上次断在重试中)
4. 读 PLAN.md §7.4 对应 next_step
5. 复核 _progress.json.completed 中所有 PASS Step 的 evidence 文件存在
6. 从断点续跑（先写新的 trace.jsonl 行 {event: session_resume, ...}）
```

---

## 8. Postscript — 容量假设修订 (2026-04-18)

> Step 14 实测后发现本 PLAN 的核心假设之一 ("Claude Project 容量上限 ~200K tokens") 站不住。
> 详细调研见 [`capacity_research.md`](capacity_research.md)。
> 本节作为 postscript 不重写历史决策, 仅记录新认识与对 Phase 7 的影响。

### 8.1 实测偏差

- 上传 9 文件 / 192,036 tokens (本地 tiktoken)
- UI 显示 **"12% of project capacity used"**, 而非预期 95-98%
- 偏差 8 倍

### 8.2 根本原因 (基于 capacity_research.md)

1. **Pro/Max 套餐 RAG 自动扩容到 10x** (官方明文)
2. **GitHub Issue #25759 实测推算**: capacity 分母约 3-4M tokens
3. **我们已经触发 RAG 模式** ("Indexing" 标签 + 12% 实测都是信号), 但工作正常 (T1-T8 全 PASS)

### 8.3 哪些前提需要标注 "已修订"

| 位置 | 旧表述 | 新认识 |
|------|-------|-------|
| §1.2 表 | "Claude Project 容量上限 ~200K tokens (硬约束)" | 200K 是 context window 限制; paid 套餐 RAG 自动扩 10x; 实际 RAG 索引容量 ~3-4M |
| §3.3 表头 | "硬约束 ≤195K" | 实际 ≤195K 是 "保证不触发 RAG" 的软约束, 而非硬约束 |
| §3.2 D3/D4 动机 | "因 200K 装不下, 降级 examples/terminology" | 动机修订为 "降低价值密度低的内容占比", 不是容量被迫 |
| 附录 A | "Claude Project 容量: ~200K tokens" | Project context window 200K; RAG 模式索引容量 ~3-4M |

### 8.4 历史决策不撤销

虽然前提变了, **方案 B 压缩工作仍然成功** (Smoke + T1-T8 全 PASS, 边界模板生效)。代价是过度压缩, examples 数据表 / terminology Term 值原文被剔除, T3/T6/T7 出现间接重建场景。

### 8.5 对 Phase 7 的指引

由于实际剩余 ~88% 容量, Phase 7 可分批扩回:
1. ch06 完整 + ch08 §8.3 完整 (+30-50K) — 解决 T3 间接重建
2. examples 高频域数据表 (+50-100K) — 解决 T6
3. terminology 高频 codelist Term 值 (+200-500K) — 解决 T7/T8
4. ch01/02/03/08/10 撤销精简 (+30-50K)

总扩 ~300-700K, 远低于 RAG 上限。**RAG 检索质量随集合增大可能下降**, 扩容前需建 baseline (当前 T1-T8 PASS), 扩容后回归测试。

### 8.6 必须保留的设计

无论是否扩容:
- System Prompt 边界处理模板 (兜底)
- 源路径标注 `<!-- source: ... -->` (跨文件追溯)
- System Prompt 路由规则 (RAG 基础上提升精确度)

---

## 附录 A：关键数据参考

**源知识库体量** (tiktoken cl100k_base 实测, 2026-04-17):

```
ROUTING.md                    2,657 tokens
INDEX.md                      5,032 tokens
VARIABLE_INDEX.md            38,452 tokens
chapters/ (6)                60,525 tokens
model/ (6)                   17,573 tokens
domains/*/spec.md (63)      184,943 tokens
domains/*/assumptions.md (63) 53,708 tokens
domains/*/examples.md (63)  219,814 tokens
terminology/core (42)       898,174 tokens
terminology/questionnaires (43) 930,026 tokens
terminology/supplementary (6) 116,249 tokens
────────────────────────────────────────
TOTAL                     2,527,153 tokens
```

**Claude Project 容量**: ~200K tokens (根据官方文档与社区测试)

**超标倍数**: 12.6x

**目标压缩率**: 92.4%
