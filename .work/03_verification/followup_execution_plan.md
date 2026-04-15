<!-- chain: A (验证进度链)
  修改本文件后，必须检查:
  → 03_verification/issues_found.md  (问题汇总)
  → meta/worklog.md                  (工作日志)
-->

# Followup Plan 执行手顺

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 对 followup_plan.md 中 5 个中等风险项 (M1-M5) 逐项执行抽样验证，发现并修复残余缺失，消除结构性盲区。

**Architecture:** 每个 M 项由一个独立 subagent 执行「读 PDF → 读 md → 逐要点比对 → 出覆盖率报告」，修复与复核必须分离（不同 subagent）。所有 evidence 写入 `.work/03_verification/results/followup_evidence.md`。

**约束:** 严格遵守 retrospective.md §4 四条预防规则（定量 PASS / 写审分离 / AI 估算标记 / 行数比值检查）。

---

## 通用定义

### 工具

| 工具 | 用途 | 说明 |
|------|------|------|
| `Read(file_path, pages)` | 读 PDF 指定页 | 用于读取 `source/SDTMIG v3.4 (no header footer).pdf` 的指定页码 |
| `Read(file_path)` | 读 md 文件 | 用于读取 `knowledge_base/` 下的 md 文件 |
| `Grep(pattern, path)` | 搜索标记 | 用于扫描残留占位标记（待补全/TODO/placeholder） |
| `Write` / `Edit` | 写 evidence / 修复内容 | 写入 evidence 文件或修复 md 文件 |
| `Agent(subagent)` | 写审分离 | 修复后启动独立 subagent 做复核 |

### PASS/FAIL 判定标准（定量，不可妥协）

```
PASS 条件（全部满足）:
  1. 覆盖率 ≥ 95%  （已覆盖要点数 / PDF 要点总数）
  2. 零占位标记     （grep 扫描：待补全|TODO|待后续|部分覆盖|placeholder = 0）
  3. 行数/页数比值合理（本项目基准: ≈ 15-20 行/页，低于 10 行/页需解释）
  4. 已有内容无事实性错误

FAIL 条件（任一触发）:
  - 覆盖率 < 95%
  - 存在占位标记
  - 行数/页数 < 10 且无合理解释
  - 发现事实性错误
```

### Evidence 记录格式（每个检查项统一使用）

每个 M 项的 evidence 写入 `followup_evidence.md`，格式如下：

```markdown
## M{N}: {标题}

- **检查日期**: YYYY-MM-DD
- **检查人**: {agent type, e.g., Sonnet subagent / Opus main}
- **PDF 页码**: p.X-Y
- **md 文件**: `knowledge_base/path/to/file.md`
- **md 行数**: N 行
- **PDF 页数**: N 页
- **行数/页数比**: N.N 行/页

### 要点清单

| # | PDF 要点（简述） | md 中对应位置 | 状态 |
|---|-----------------|--------------|------|
| 1 | ... | §X.Y 第 N 行 | ✅ 已覆盖 / ❌ 缺失 / ⚠️ 部分覆盖 |

### 定量结果

- **PDF 要点总数**: N
- **已覆盖**: N
- **缺失**: N
- **覆盖率**: N/N = XX.X%
- **占位标记扫描**: 0 matches（附 grep 命令输出）
- **判定**: PASS / FAIL
- **FAIL 原因**（如适用）: ...

### 盲区检查

- **PDF 中存在但 md 中完全没有的段落**: {列出或"无"}
- **说明**: {是否属于结构性盲区}
```

### 修复流程（仅在 FAIL 时触发）

```
1. 修复 agent（当前上下文）读 PDF 对应页，补写缺失内容到 md
2. 启动独立复核 subagent:
   Agent(
     description: "独立复核 M{N}",
     prompt: "读 PDF p.X-Y 和 md 文件 path/to/file.md，
              输出覆盖率报告（格式见 followup_execution_plan.md 的 evidence 格式）。
              你不知道之前修复了什么，独立判断。",
     subagent_type: "general-purpose"
   )
3. 复核 PASS → 更新 evidence，标记完成
4. 复核 FAIL → 回到步骤 1，最多迭代 3 次
5. 3 次仍 FAIL → 升级为新 Issue，记入 issues_found.md
```

---

## Task 1: M4 — page_index.json 章节页码核实

**为什么排第一:** 结构化数据，可快速完成，验证流程是否顺畅。

**Files:**
- 检查: `.work/02_indexing/page_index.json`
- 对照: `source/SDTMIG v3.4 (no header footer).pdf`
- 写入: `.work/03_verification/results/followup_evidence.md`

**抽样方法:** 从 page_index.json 中选取 10 个关键条目（覆盖 chapters + 各 class 域），逐个核实起始页码。

**抽样清单（固定，不可随机替换）:**

| # | 条目 | JSON 起始页 | 类型 |
|---|------|------------|------|
| 1 | ch01_introduction | 7 | chapter |
| 2 | ch04_general_assumptions | 22 | chapter |
| 3 | ch08_relationships | 427 | chapter |
| 4 | DM (Demographics) | 62 | Special Purpose |
| 5 | AE (Adverse Events) | — (需查 JSON) | Events |
| 6 | CM (Concomitant Meds) | 98 | Interventions |
| 7 | LB (Lab Tests) | — (需查 JSON) | Findings |
| 8 | VS (Vital Signs) | — (需查 JSON) | Findings |
| 9 | TA (Trial Arms) | — (需查 JSON) | Trial Design |
| 10 | RELREC | — (需查 JSON) | Relationship |

- [ ] **Step 1.1: 读取 page_index.json 完整内容**

```
Read(".work/02_indexing/page_index.json")
```

记录上述 10 个条目的 JSON 页码值。

- [ ] **Step 1.2: 逐个核实起始页码**

对每个条目，读取 JSON 标注的起始页（单页）：

```
Read("source/SDTMIG v3.4 (no header footer).pdf", pages: "N")
```

验证方法：
- 该页的章节/域标题是否与条目名称匹配
- 如果不匹配，向前/后翻 1 页确认实际起始页
- 记录：JSON 值 / 实际值 / 偏移量

- [ ] **Step 1.3: 写入 evidence**

将 10 个条目的核实结果写入 evidence，格式：

```markdown
## M4: page_index.json 页码核实

- **检查日期**: 2026-04-16
- **抽样数**: 10 / 70 (chapters 7 + domains 63)
- **抽样覆盖**: chapters 3个, Special Purpose 1个, Events 1个, Interventions 1个, Findings 2个, Trial Design 1个, Relationship 1个

| # | 条目 | JSON 起始页 | 实际起始页 | 偏移 | 判定 |
|---|------|------------|-----------|------|------|
| 1 | ch01 | 7 | ? | 0 | ✅/❌ |
| ... |

- **准确率**: N/10
- **判定**: PASS (≥ 9/10 准确) / FAIL
```

- [ ] **Step 1.4: 判定与处理**

- 10/10 准确 → PASS，M4 完成
- 9/10 准确 → PASS，记录偏差条目，评估影响
- ≤ 8/10 准确 → FAIL，扩大抽样到 20 个条目，启动全面核查

---

## Task 2: M1 — ch01_introduction.md 抽查

**Files:**
- 检查: `knowledge_base/chapters/ch01_introduction.md` (98 行)
- 对照: `source/SDTMIG v3.4 (no header footer).pdf` p.7-12 (6 页)
- 写入: `.work/03_verification/results/followup_evidence.md`

**背景:** Step 3-3 验证发现 26 个问题，修复了 3 个高严重性，23 个低/中留存。需确认留存问题不影响核心内容完整性，并检查结构性盲区。

**行数/页数比**: 98/6 ≈ 16.3 行/页 — 在合理范围内。

- [ ] **Step 2.1: 读 PDF p.7-12**

```
Read("source/SDTMIG v3.4 (no header footer).pdf", pages: "7-12")
```

逐页提取独立要点清单。要点类型包括：
- 段落级陈述（一个完整的规则或说明）
- 表格（整张表视为 1 个要点，但列定义各算子要点）
- 列表项（每个列表项算 1 个要点）
- 交叉引用（如"see Section X"算 1 个要点）

- [ ] **Step 2.2: 读 md 文件**

```
Read("knowledge_base/chapters/ch01_introduction.md")
```

- [ ] **Step 2.3: 逐要点比对**

在 evidence 中建立要点清单表（见通用 evidence 格式）。

重点关注：
1. **已知留存问题**: 对照 step3_3 的 23 个低/中问题，确认它们确实是低/中而非实际缺失核心内容
2. **结构性盲区**: PDF 中有完整段落但 md 中完全没有对应内容（不是简化/压缩，而是完全缺失）
3. **事实性错误**: md 中的陈述与 PDF 原文矛盾

- [ ] **Step 2.4: 计算覆盖率并判定**

按通用 PASS/FAIL 标准判定。

- [ ] **Step 2.5: 如 FAIL，执行修复流程**

按「通用定义 > 修复流程」执行（写审分离 + 独立 subagent 复核）。

---

## Task 3: M2 — ch02_fundamentals.md 抽查

**Files:**
- 检查: `knowledge_base/chapters/ch02_fundamentals.md` (162 行)
- 对照: `source/SDTMIG v3.4 (no header footer).pdf` p.11-16 (6 页)
- 写入: `.work/03_verification/results/followup_evidence.md`

**背景:** Step 3-3 验证发现 28 个问题，修复了 5 个高严重性，23 个低/中留存。

**注意:** page_index.json 记录为 p.13-20（8 页），但 ch02 md 头部标注 "Pages 13-20"。需在 Step 3.1 中确认实际页码范围。

**行数/页数比**: 162/8 ≈ 20.3 行/页 — 合理。

- [ ] **Step 3.1: 读 PDF 确认页码范围**

```
Read("source/SDTMIG v3.4 (no header footer).pdf", pages: "11-16")
```

先确认 Section 2 的实际起止页。如果 p.11-12 不属于 Section 2，调整为 p.13-16 或实际范围。

- [ ] **Step 3.2: 读 md 文件**

```
Read("knowledge_base/chapters/ch02_fundamentals.md")
```

- [ ] **Step 3.3: 逐要点比对**

重点关注：
1. §2.1 Qualifier Subclasses 表格 — 是否完整（5 个子类 × 3 列）
2. §2.3 General Observation Classes 表格 — 是否完整（3 个 class）
3. §2.5 标准域模型规则 — 7 条规则是否全部列出
4. §2.6 创建新域流程 — 11 步流程是否完整
5. §2.7 禁用变量清单 — 是否与 PDF 一致
6. **结构性盲区**: 是否有 PDF 整节在 md 中完全缺失

- [ ] **Step 3.4: 计算覆盖率并判定**

- [ ] **Step 3.5: 如 FAIL，执行修复流程**

---

## Task 4: M3 — ch03_submitting_data.md 抽查

**Files:**
- 检查: `knowledge_base/chapters/ch03_submitting_data.md` (70 行)
- 对照: `source/SDTMIG v3.4 (no header footer).pdf` p.17-21 (5 页)
- 写入: `.work/03_verification/results/followup_evidence.md`

**背景:** Step 3-3 验证发现 18 个问题，修复了 4 个。**Dataset 大表格被跳过**是已知风险。

**行数/页数比**: 70/5 = 14.0 行/页 — 偏低，接近警戒线（10 行/页）。

**重点检查:** Dataset-level Metadata 表格完整性。

- [ ] **Step 4.1: 读 PDF p.17-21**

```
Read("source/SDTMIG v3.4 (no header footer).pdf", pages: "17-21")
```

- [ ] **Step 4.2: 读 md 文件**

```
Read("knowledge_base/chapters/ch03_submitting_data.md")
```

- [ ] **Step 4.3: 重点检查 Dataset 表格**

当前 md 中 Dataset 表格仅列出 8 个域 + `...`（省略 50+ 域）。需确认：

1. **PDF 中该表格实际列出多少个域？** — 计数
2. **是否需要完整列出？** — 判断标准：
   - 如果 PDF 中该表格是信息性参考（域的完整列表在各 Section 5-7 中），则 `...` 省略可接受，但需添加明确说明
   - 如果 PDF 中该表格是规范性定义（唯一来源），则必须完整列出
3. **其他节的覆盖情况** — §3.1, §3.2.1.1, §3.2.1.2, §3.2.2 的要点比对

- [ ] **Step 4.4: 计算覆盖率并判定**

对 Dataset 表格的判定逻辑：
- 如果表格是信息性的 → `...` 省略不算缺失，但需注明引用来源
- 如果表格是规范性的 → `...` 省略算缺失，覆盖率会大幅下降

- [ ] **Step 4.5: 如 FAIL，执行修复流程**

---

## Task 5: M5 — examples.md 随机抽样验证

**Files:**
- 检查: `knowledge_base/domains/{DOMAIN}/examples.md` (63 域)
- 对照: `source/SDTMIG v3.4 (no header footer).pdf` (各域 examples 页码见 page_index.json)
- 写入: `.work/03_verification/results/followup_evidence.md`

**背景:** 63 域中 30 域做了实际修复，33 域标记为"无问题"。需从"无问题"的 33 域中抽样，验证是否真的无问题。

**抽样方法:** 从 33 个"无问题"域中随机抽取 5 个，覆盖不同 observation class。

- [ ] **Step 5.1: 确定抽样域**

先确认哪 33 个域被标记为"无问题"：

```
Read(".work/03_verification/results/step2_examples_summary.md")
```

从中选取 5 个域，选取标准：
- 至少 1 个 Interventions class 域
- 至少 1 个 Events class 域
- 至少 2 个 Findings class 域
- 至少 1 个 Special Purpose / Trial Design 域
- 优先选 examples 页数 ≥ 3 的域（内容多，验证价值高）

记录选取的 5 个域名及其 page_index.json 中的 examples 页码范围。

- [ ] **Step 5.2: 逐域验证（5 个域可并行）**

对每个抽样域，执行：

```
# 读 PDF examples 页
Read("source/SDTMIG v3.4 (no header footer).pdf", pages: "X-Y")

# 读 md
Read("knowledge_base/domains/{DOMAIN}/examples.md")
```

检查项：
1. **示例数量**: PDF 中有几个独立示例？md 中有几个？
2. **示例表格**: 每个示例表格的行数/列数是否匹配
3. **示例说明文字**: 表格前/后的说明段落是否保留
4. **交叉引用**: 是否保留了与其他域的关联说明
5. **结构性盲区**: 是否有 PDF 中的完整示例在 md 中完全缺失

- [ ] **Step 5.3: 汇总 5 域结果**

```markdown
## M5: examples.md 抽样验证

| # | 域 | PDF 示例数 | md 示例数 | 覆盖率 | 判定 |
|---|-----|-----------|----------|--------|------|
| 1 | XX | ? | ? | ?% | ✅/❌ |
| ... |

- **总体判定**: 5/5 PASS → M5 完成; 任一 FAIL → 执行修复
```

- [ ] **Step 5.4: 如有域 FAIL，执行修复流程**

每个 FAIL 域独立修复，修复后启动独立 subagent 复核。

---

## Task 6: 汇总与收尾

**Files:**
- 更新: `.work/03_verification/followup_plan.md` — 勾选完成标准
- 更新: `.work/03_verification/followup_evidence.md` — 添加汇总
- 更新: `.work/03_verification/issues_found.md` — 如有新 Issue
- 更新: `.work/meta/worklog.md` — 记录工作（Chain B）
- 更新: `.work/progress.json` — 更新状态（Chain B）
- 更新: `docs/PROGRESS.md` — 更新看板（Chain B）

- [ ] **Step 6.1: 汇总所有 M 项结果**

在 `followup_evidence.md` 末尾添加汇总表：

```markdown
# 汇总

| M# | 项目 | 覆盖率 | 修复数 | 判定 | 盲区发现 |
|----|------|--------|--------|------|----------|
| M1 | ch01 | ?% | ? | ✅/❌ | ? |
| M2 | ch02 | ?% | ? | ✅/❌ | ? |
| M3 | ch03 | ?% | ? | ✅/❌ | ? |
| M4 | page_index | ?/10 | — | ✅/❌ | — |
| M5 | examples (5域) | ?% avg | ? | ✅/❌ | ? |

**结论**: {整体风险评估}
**新增 Issue**: {有/无}
```

- [ ] **Step 6.2: 更新 followup_plan.md 状态**

将每个 M 项的状态从"待执行"改为"已完成"，勾选完成标准 checklist。

- [ ] **Step 6.3: 执行 Chain A + Chain B 更新**

Chain A:
- `issues_found.md` — 如有新 Issue，添加 Issue 3+

Chain B:
- `meta/worklog.md` — 添加工作记录
- `progress.json` — 更新 followup 状态
- `docs/PROGRESS.md` — 更新看板

- [ ] **Step 6.4: 最终确认**

```
Grep("待补全|TODO|待后续|部分覆盖|placeholder", "knowledge_base/")
```

预期结果: 0 matches。如果 > 0，逐个处理。

---

## 并行策略

```
              ┌── Task 1 (M4: page_index) ──┐
              │                              │
Start ────────┤                              ├──→ Task 6 (汇总)
              │  ┌── Task 2 (M1: ch01) ──┐   │
              │  │                        │   │
              ├──┤── Task 3 (M2: ch02) ──┤───┤
              │  │                        │   │
              │  └── Task 4 (M3: ch03) ──┘   │
              │                              │
              └── Task 5 (M5: examples) ─────┘
```

- Task 1-5 **全部互相独立**，可并行启动 5 个 subagent
- Task 6 **依赖 Task 1-5 全部完成**，串行执行
- Task 5 内部的 5 个域也可并行

**推荐执行方式:** 使用 `superpowers:subagent-driven-development`，启动 5 个并行 subagent 分别处理 Task 1-5，全部完成后主 agent 执行 Task 6。

---

## 风险与应急

| 风险 | 触发条件 | 应急措施 |
|------|---------|---------|
| PDF 读取限制 | 单次读取 > 20 页失败 | 分段读取，每次 ≤ 10 页 |
| 覆盖率极低 (< 80%) | M1-M3 任一触发 | 升级为正式 Issue，按 Issue 2 修复流程处理 |
| page_index 大面积偏差 | M4 准确率 ≤ 8/10 | 全量核查 70 个条目，可能需要重建索引 |
| examples 抽样发现系统性问题 | M5 中 ≥ 3/5 域 FAIL | 扩大抽样到 15 域，评估是否需要全量重验 |
| 修复迭代 > 3 次仍 FAIL | 任一修复项 | 升级为新 Issue，暂停该项，继续其他项 |
