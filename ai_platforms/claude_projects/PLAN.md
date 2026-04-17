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
