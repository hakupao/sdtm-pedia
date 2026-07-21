# 05 内容策略 + 落地方案

从"有一堆源文件"到"可上传到平台的 N 个文件 + System Prompt"的设计决策 + 执行方法.

---

## 两个决策问题

### 问题 1: 怎么切

- **源**: `knowledge_base/**` (293 个 .md 文件, 63 域 + terminology + chapters + model)
- **目的地**: 平台支持的 N 个文件, 满足平台限制 (容量 / 文件数 / 单文件大小)

### 问题 2: System Prompt 放什么

- 路由规则 (哪种问题查哪个文件)
- 回答规范 (引用哪些字段, 怎么处理边界)
- 平台特化 (发挥本平台独有能力)

---

## 内容策略设计流程

```
1. 读 platform_profile.md §B 检索机制 + §C 文件管理
2. 算源体量 vs 平台容量比
3. 从"中庸 50%"出发估算批次数
4. 按优先级 (规则 E 用户确认) 定每批内容
5. 设计 Deferred stub (如需要)
6. 设计 System Prompt 累积段 (如多批)
```

---

## 切分策略: 4 种模板

### A. 单批全上 (Single Batch)

**适用**: 源体量 << 平台容量 (e.g. Gemini 1M 窗口 vs SDTM 核心 512K)

- 合并源为 3-5 个主题文件
- 一次性上传
- System Prompt 单段

**示例**: Gemini 预计方案 (核心 ~513K, 1M 窗口内)

### B. 2-3 批到位 (Few Batches)

**适用**: 源体量接近平台文件数硬限 (e.g. ChatGPT 20 文件限)

- 先传 P0 (导航 + 核心 spec + chapters)
- 测基础查询
- 再传 P1-P2 (assumptions + examples + terminology)
- 每批 A/B, 确认文件数硬限未触

**示例**: ChatGPT 预计方案 (合并为 8-10 文件)

### C. N 批渐进 + 拐点测试 (Progressive Batches)

**适用**: 平台容量不透明 + 需建立 RAG 质量 vs 规模曲线

- 第 1 批: baseline (小而全的骨架)
- 第 2-N 批: 每批增一个维度, A/B 检测衰减
- 观察拐点, 决定何时停

**示例**: Claude Projects v2 (5 批 + 1 重平衡批, 12% → 77% capacity)

### D. 增量扩容 (Incremental After Initial)

**适用**: 基线已发布, 补齐某个维度

- 前批不动
- 新批仅新增文件 (不重写老文件)
- A/B 确认无挤出

**示例**: Claude Projects v2.6 追加批 (对 core/supp 未覆盖的 209 codelist 做 tail 压缩)

---

## 每批内容分配 (规则 E 乘入)

### 规则 E 的算法

默认打分公式 (如"按变量引用次数") 可能和用户业务优先级反向. 解法:

```
score(file) = raw_score(file) × priority_weight(file)

其中:
- raw_score: 域引用次数 / 文件大小 / 预期命中率 等
- priority_weight: 来自 PLAN §优先级段 (用户确认)
  - 最高优先级: 权重 3x
  - 中等: 权重 1x
  - 最低优先级 (可下沉下游): 权重 0.3x
```

**必须在 Phase 0/2 就问清用户优先级**, 不然等 Phase 3 才发现反向只能追加重平衡批 (Claude v2.5→v2.6 G1 教训, 1.5 小时返工).

### 每批应回答 3 问

1. **本批目标 token 数?** (来自 §容量配额)
2. **本批覆盖哪个 slice?** (core/supp/quest/chapters/...)
3. **本批 A/B 矩阵新增题?** (验证本批覆盖是否达成)

---

## Deferred Stub 模式

### 触发条件

- 平台容量有硬上限
- 源中存在**单表 >500 条目** (典型: MedDRA / WHODrug / LOINC 级 codelist)
- Inline 会挤占 >10% capacity
- 99% 下游查询只需 1-2 个条目 (不是全表)

### Stub 格式

```markdown
## <Codelist Name> (<C-code>)

- **Submission Value**: <e.g. LBTESTCD>
- **NCI CDISC Definition**: <e.g. Lab Test Code>
- **Code**: <C-code>
- **Extensible**: Yes/No
- **Source File**: `knowledge_base/terminology/core/lb_part*.md`
- **Status**: Deferred to Phase N+1 RAG (规模 <N> terms, 超 inline 阈值)
- **External Reference**: NCI EVS Browser https://evs.nci.nih.gov/ncitbrowser/
```

### 模型行为预期 (A/B 验证)

提问 "列出 C65047 所有 term", 模型应:
- ✅ 识别这是 stub (不 inline)
- ✅ 指向源文件路径
- ✅ 提供 NCI EVS Browser 入口
- ❌ **零臆造 term** (如果臆造就是 FAIL)

**验证题**: A/B 矩阵必加一题 "T<N>: 某 stub codelist 完整列表", 观察模型是否 PASS.

---

## System Prompt 设计

### 结构骨架

```markdown
# <Platform> Project: <Knowledge Base Name>

## 角色
你是 <领域> 的专家, 基于本 Project 的知识库回答问题.

## 文件路由规则
(按本次上传文件结构写)
- 问 "变量定义" → 查 `<file_N>`
- 问 "codelist 完整值" → 查 `<file_M>` (如命中 stub 则指引源 + 外部)
- ...

## 回答规范
- 每次回答必引: 变量名 + 域名 + 章节号 + 源文件路径
- 跨域查询: 追踪 Cross References
- 数据示例: 必引具体表格

## 边界处理
- 不在本 Project 的内容: **坦诚声明 "未收录"**, 给出源文件路径 + 外部资源, **零臆造**
- 对 Deferred stub codelist: 声明"超规模未 inline", 给 NCI EVS Browser 入口

## 平台特化 (发挥本平台优势)
- (e.g. Claude: RAG 自动分片, 可做跨文件 narrative 重建)
- (e.g. Gemini: 1M 全量, 可做全域对比)
```

### 累积段 (多批 Project)

如果分 N 批上传, System Prompt 也应**累积式更新**:

- 第 1 批后: 初版 (仅第 1 批文件的路由)
- 第 2 批后: 追加段 "文件 09 在, 优先级 09 > 07"
- 第 N 批后: 完整路由 + 所有 fallback

**收束时**: 把累积段**整合去版本化** (current/system_prompt.md 不应该出现 "v2.4 新增段" 这种词), 但保留每段的功能说明.

---

## 落地执行: 脚本 + 自动化

### 脚本职责单一化 (P6)

每个脚本单一输入 / 单一输出, 主控不读脚本源 (保持 context 隔离):

```
count_tokens.py              测 token
score_<X>.py                 圈定优先级
extract_<X>.py               从源文件抽取 (参数化)
merge_<X>.py                 合并文件 (如需要)
build_<platform>_stage.py    分阶段构建 + 累计 token + 写 manifest
validate_<X>.py              产物校验 (rc=0/非0)
```

### 每批 Build 必做 3 事

1. **打印 stage tokens**: `[Stage vB.1] <file>: <N> tokens (target ≤<X>K)`
2. **C12 gate / 产物校验**: `validate_<X>.py` 检查段数 == 源文件数 / md5 稳定 / 无空文件
3. **md5 幂等**: 重跑脚本产物 md5 应一致 (验证无非确定性)

### 上传方式

按 `platform_profile.md §C.上传方式` 选:
- 拖拽 (Web UI) — 手工, 稳定
- API (如支持) — 自动化, 但注意 RAG 开关可能和 Web UI 不同
- MCP / 第三方自动化 — 注意 v1 经验: MCP 上传 Claude Projects 可能被阻塞, fallback 手工

---

## 容量预算表 (每批必填)

| 批次 | 覆盖内容 | token 估算 | token 实测 | 累计 tokens | 累计 capacity% |
|------|---------|-----------|-----------|------------|----------------|
| B.1 | chapters 全展开 | ~60K | | | |
| B.2 | examples 高频域 | ~110K | | | |
| ... | ... | | | | |

估算 vs 实测偏差 > 15% 时, 回头看是不是源有冗余 / 脚本有 bug.

---

## 失败/退化应急预案 (内容策略侧)

| 失败 | 响应 |
|------|------|
| 单文件 token 超预期 | 按 subdir 拆分 or Related Domain 提 header 减重复 |
| 跨批衰减 ≥2 题 (规则 P10) | **立即停**, reviewer 归因, 可能走 rollback |
| 合并后表格断裂 (chunk 不智能) | 用 `TableAwareChunker` or md-heading 分段, 避免 row 中切 |
| 文件数超平台硬限 | 合并同类项 (e.g. 63 spec.md → 1 domain_specs_all.md) |

---

*来源: claude_projects v2 实际内容策略演进 (原计划策略 A 200K → 实际终态 1.29M 5+1 批) + Deferred stub 设计.*
