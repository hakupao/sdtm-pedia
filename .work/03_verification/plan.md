<!-- chain: A (验证进度链)
  修改本文件后，必须检查:
  → 03_verification/issues_found.md  (问题汇总)
  → meta/findings.md                 (全局质量记录)
  → meta/worklog.md                  (工作日志)
  → progress.json                    (程序化进度)
  → ../docs/PROGRESS.md                   (进度看板)
-->

# Knowledge Base 内容验证计划

> 创建日期: 2026-04-14
> 状态: **全部完成** — Step 0 ~ 4 + Followup M1-M5 + Issue 1-4 修复
> 子计划: → repair_plan.md (Issue 2 修复，已完成) → followup_plan.md (残余风险排查，已完成)

---

## 背景

knowledge_base/ 中的 293 个文件，其中：
- **已验证**: spec.md (63) + terminology/ (91) — xlsx 自动生成，脚本校验通过
- **待验证**: assumptions.md (63) + examples.md (63) + model/ (6) + chapters/ (6) — PDF AI 提取，需对照原文验证

验证目标：对每个文件证明与 PDF 原文比较**无遗漏**（完整性）、**无错误**（准确性）。

---

## 进度总表

| Step | 任务 | 状态 | 详情 |
|------|------|------|------|
| 0 | 修正 page_index.json | **已完成** (2026-04-14) | 63 域页码全部实际翻 PDF 确认 |
| 1 | 验证 assumptions.md (61 域) | **已完成** (2026-04-14) | 16 问题已修复 → [详细结果](results/step1_assumptions.md) |
| 2 | 验证 examples.md (63 域, 21 组) | **已完成** (2026-04-14) | 33 PASS / 30 修复后 PASS → [总表](results/step2_examples_summary.md) · [详细结果](results/step2_examples_detail.md) |
| 2-final | 补全 13 幅图表 (Mermaid) | **已完成** (2026-04-14) | 13/13 图表全部完成 |
| 3 | 验证 model/ + chapters/ (12 文件) | **已完成** (2026-04-15) | 3-1~3-5 全部完成 → [3-3](results/step3_3_chapters_small.md) · [3-4](results/step3_4_ch04.md) · [3-5](results/step3_5_ch08_ch10.md) |
| 3.5 | 编写溯源矩阵 (TRACEABILITY.md) | **已完成** (2026-04-15) | 4 份源文件全覆盖，63 域页码映射 → [TRACEABILITY.md](../../docs/TRACEABILITY.md) |
| 3.6 | 图像内容溯源 | **已完成** (2026-04-15) | 60 幅图像全覆盖：37 已转化(前期) + 21 新转化(Step 3.6) + 2 排除(Logo) → [清单](scans/image_inventory.md) · [TRACEABILITY.md §6](../../docs/TRACEABILITY.md) |
| 4 | 汇总报告 | **已完成** (2026-04-16) | → [汇总报告](results/step4_summary_report.md) |

---

## Step 2-final: 补全 13 幅图表（Mermaid 复刻）

验证阶段发现 13 幅 PDF 流程图/示意图未收录到 examples.md 中。

**方法**: Read PDF 页面（Claude 多模态读图）→ 理解结构/节点/箭头/标签 → 翻译为 Mermaid 语法 → 嵌入 examples.md 对应位置

**执行顺序**：DM (4幅) → TA (7幅) → TV (1幅) → RELSPEC (1幅)

| # | Domain | Example | PDF 页码 | 图片描述 | 状态 |
|---|--------|---------|---------|---------|------|
| 1 | DM | Example 4 | 70-71 | aCRF for Race（RACE01-07 + 4 个子类别分支；红=SDTMIG，灰=CDASHIG） | ✅ 已完成 |
| 2 | DM | Example 5 | 74 | CRF Mock（中国民族子分类：HAN CHINESE/MANCHU/MIAO/UYGHUR/ZHUANG） | ✅ 已完成 |
| 3 | DM | Example 6 | 75 | aCRF for Race（RACE01-07 + 2 个子类别分支） | ✅ 已完成 |
| 4 | DM | Example 7 | 78 | CRF Mock（5 种族选项+Unknown+Other；RACE/RACEOTH/RACEREAS） | ✅ 已完成 |
| 5 | TA | Example 1 | ~387-388 | Study Schema + Prospective/Retrospective/Blinded View（并行设计） | ✅ 已完成 |
| 6 | TA | Example 2 | ~389-391 | Crossover Trial 4 视图 | ✅ 已完成 |
| 7 | TA | Example 3 | ~392-393 | Multiple Branches 4 视图 | ✅ 已完成 |
| 8 | TA | Example 4 | ~394-396 | Cyclical Chemotherapy 5 视图（含显式重复） | ✅ 已完成 |
| 9 | TA | Example 5 | ~397 | Different Chemo Durations 2 视图 | ✅ 已完成 |
| 10 | TA | Example 6 | ~398 | Different Cycle Durations 2 视图 | ✅ 已完成 |
| 11 | TA | Example 7 | ~400-401 | RTOG 93-09（Schema + Prospective/Retrospective） | ✅ 已完成 |
| 12 | TV | Example 1 | 409 | Parallel Design Planned Visits（访视时间轴图） | ✅ 已完成 |
| 13 | RELSPEC | Example 1 | 440 | Specimen Relationship 层次结构图（ASCII 树 → Mermaid） | ✅ 已完成 |

---

## Step 3: 验证 model/ 和 chapters/

model/ (6 文件) 对应 SDTM v2.0 PDF (74 页)
chapters/ (6 文件) 对应 SDTMIG v3.4 PDF 的通用章节

验证方法同 Step 1/2，对照 PDF 检查完整性和准确性。

### Step 3 子步骤拆解

| 子步骤 | 内容 | 工作量 | 状态 |
|--------|------|--------|------|
| 3-1 | 建立 model/ 页码映射 + 验证小文件 (01, 04) | 轻 (118 行) | **已完成** (2026-04-14) |
| 3-2 | 验证 model/ 剩余 4 文件 (02, 03, 05, 06) | 中 (850 行) | **已完成** (2026-04-15) |
| 3-3 | 验证 chapters/ 小文件 (ch01, ch02, ch03) | 中 (307 行, 15 页 PDF) | **已完成** (2026-04-15) |
| 3-4 | 验证 ch04_general_assumptions | 重 (331 行, 38 页 PDF) | **已完成** (2026-04-15) |
| 3-5 | 验证 ch08 + ch10 | 中 (457 行, 32 页 PDF) | **已完成** (2026-04-15) |

### 文件详情

**model/** (SDTM_v2.0.pdf):

| 文件 | 行数 | PDF 页码 | 验证结果 |
|------|------|----------|----------|
| 01_concepts_and_terms.md | 80→89 | 8-10 | FAIL→修复后 PASS (6处遗漏已补) |
| 02_observation_classes.md | 275→292 | 11-39 | FAIL→修复后 PASS (10处: 5错误+2遗漏+2幽灵+1不精确) |
| 03_special_purpose_domains.md | 187→203 | 40-49 | FAIL→修复后 PASS (16处: 11错误+4遗漏+1幽灵域) |
| 04_associated_persons.md | 38→39 | 50 | FAIL→修复后 PASS (2错误+3遗漏已修) |
| 05_study_level_data.md | 224→230 | 51-63 | FAIL→修复后 PASS (19处: 13错误+4遗漏+3幽灵) |
| 06_relationship_datasets.md | 164→155 | 64-69 | FAIL→修复后 PASS (27处: 16错误+6遗漏+6幽灵) |

**chapters/** (SDTMIG v3.4 PDF):

| 文件 | 行数 | PDF 页码 | 验证结果 |
|------|------|----------|----------|
| ch01_introduction.md | 94→100 | 7-12 | FAIL→修复后 PASS (26处: 3高已修) |
| ch02_fundamentals.md | 150→155 | 13-20 | FAIL→修复后 PASS (28处: 5高已修) |
| ch03_submitting_data.md | 63→78 | 17-22 | FAIL→修复后 PASS (18处: 4高已修, 1幽灵已删, 补Conformance节) |
| ch04_general_assumptions.md | 331→340 | 22-59 | FAIL→重构后 PASS (95处: 系统性节号错位, 完整重构) |
| ch08_relationships.md | 253→265 | 427-446 | FAIL→修复后 PASS (43处: 6 Core值错+3变量缺失/幽灵+示例修正) |
| ch10_appendices.md | 204→215 | 444-461 | FAIL→修复后 PASS (43处: 词汇表修正+片段补全+新域表补全) |

---

## Step 3-final: 补全 chapters/ 图表（Mermaid 复刻）

验证阶段发现 6 幅 PDF 流程图/示意图未收录到 chapters/ 文件中。

**方法**: Read PDF 页面（Claude 多模态读图）→ 理解结构/节点/箭头/标签 → 翻译为 Mermaid 语法 → 嵌入对应位置

| # | 文件 | PDF 页码 | 图片描述 | 状态 |
|---|------|---------|---------|------|
| 1 | ch02 | ~p.16 | Creating a New Domain 流程图 | ✅ 已完成 |
| 2 | ch04 | ~p.35 | Decision Tree for Populating --OBJ | ✅ 已完成 |
| 3 | ch04 | ~p.47 | --ENRTPT and --ENTPT for Medical History 时间轴 | ✅ 已完成 |
| 4 | ch04 | ~p.50 | Representing Time Points 关系图 | ✅ 已完成 |
| 5 | ch04 | ~p.52 | Original to Standardized Results 转换图 | ✅ 已完成 |
| 6 | ch08 | ~p.443 | Sample Specimen Relationship 层次图 | ✅ 已完成 |

---

## Step 3.5: 编写溯源矩阵（Traceability Matrix）— 已完成

**目的**: 证明项目产出的完整性和合理性——每一页源 PDF 都被处理过，未收录的内容有明确的排除理由，而非遗漏。

**产出文件**: [`TRACEABILITY.md`](../../docs/TRACEABILITY.md)（项目根目录）

**完成日期**: 2026-04-15

**覆盖范围**: 4 份源文件 × 全部章节，含 63 域完整页码映射表、排除内容分类汇总。

---

## Step 3.6: 图像内容溯源（Image Traceability）

**目的**: 补全溯源矩阵中对图像内容的追踪——确保两份 PDF 中的每一幅图像都有明确去向（已转化 / 故意排除），而非遗漏。

**背景**: Step 3.5 的溯源矩阵按页码追踪了文本内容，但图像是一类独立的内容形态（流程图、CRF 模拟图、关系图等），需要特殊处理（图像 → Mermaid / ASCII art），应单独建立清单。Step 2-final 和 Step 3-final 已处理 19 幅图像，但这 19 幅是验证过程中发现的，不保证是全集。

### 图像定义

**纳入**: PDF 中所有非文字、非表格的视觉内容，包括：
- 流程图 (Flowchart)
- 决策树 (Decision Tree)
- CRF 模拟图 (CRF Mockup)
- 关系/层次图 (Relationship / Hierarchy Diagram)
- 时间轴 (Timeline)
- Schema / 架构图
- 任何其他图形化内容

**排除**: 纯文本、标准数据表格（已作为 markdown table 收录）

### 每幅图像记录的字段

| 字段 | 说明 |
|------|------|
| 序号 | 全局编号 |
| 源 PDF | SDTM v2.0 / SDTMIG v3.4 |
| 页码 | PDF 页码 |
| 所属章节/域 | 如 Ch4 §4.4.10 或 DM Example 4 |
| 图像类型 | 流程图 / CRF 模拟 / 关系图 / 时间轴 / Schema / Logo / 装饰 等 |
| 简要描述 | 一句话说明图像内容 |
| 转化格式 | Mermaid / ASCII art / 文字描述 / — |
| 目标文件 | 知识库文件路径（如有） |
| 处理批次 | Step 2-final / Step 3-final / Step 3.6 / — |
| 状态 | 已转化 / 故意排除 |
| 排除理由 | 仅对排除项填写（如 "Logo 装饰性图片" "纯重复性图表边框"） |

### 执行步骤

| 子步骤 | 内容 | 说明 |
|--------|------|------|
| 3.6-1 | 扫描 SDTM v2.0 PDF (74 页) | 1 个 agent, 4 次读取 |
| 3.6-2 | 扫描 SDTMIG v3.4 PDF (461 页) | 5 个 agent 并行, 共 24 次读取 |
| 3.6-3 | 交叉比对 | 与 Step 2-final (13幅) 和 Step 3-final (6幅) 已处理清单核对 |
| 3.6-4 | 编制完整清单 | 汇总所有图像，标注状态（已转化 / 故意排除 / 待转化） |
| 3.6-5 | 用户验收 | 用户审阅清单，确认排除决策，指定待转化项 |
| 3.6-6 | 执行转化 | 对用户确认的待转化项进行 Mermaid/ASCII 转化 |
| 3.6-7 | 写入 TRACEABILITY.md | 将完整图像清单作为新章节写入溯源矩阵 |

### 3.6-1 / 3.6-2 扫描批次明细

**模型选择**: Sonnet（多模态视觉识别足够，速度快）扫描 → Opus（主线程）汇总判定

**并发方案**: 6 个 Sonnet agent 全部并行发出，每个 agent 在内部串行读取 PDF（每次 20 页）

| Agent | 源 PDF | 页码范围 | 读取次数 | 输出文件 |
|-------|--------|----------|----------|----------|
| Agent 1 | SDTM v2.0 | p.1-74 | 4 次 (1-20, 21-40, 41-60, 61-74) | `step3_6_scan_v20.md` |
| Agent 2 | SDTMIG v3.4 | p.1-59 | 3 次 (1-20, 21-40, 41-59) | `step3_6_scan_ig_ch.md` |
| Agent 3 | SDTMIG v3.4 | p.60-159 | 5 次 (60-79, 80-99, 100-119, 120-139, 140-159) | `step3_6_scan_ig_d1.md` |
| Agent 4 | SDTMIG v3.4 | p.160-259 | 5 次 (160-179, 180-199, 200-219, 220-239, 240-259) | `step3_6_scan_ig_d2.md` |
| Agent 5 | SDTMIG v3.4 | p.260-359 | 5 次 (260-279, 280-299, 300-319, 320-339, 340-359) | `step3_6_scan_ig_d3.md` |
| Agent 6 | SDTMIG v3.4 | p.360-461 | 6 次 (360-379, 380-399, 400-419, 420-439, 440-459, 460-461) | `step3_6_scan_ig_d4.md` |

**总计**: 6 个 agent × 3~6 次读取 = 28 次 PDF 读取，覆盖全部 535 页

**每个 agent 的输出格式**: markdown 表格，每行一幅图像，字段见上方「每幅图像记录的字段」

### 工作流

```
第一阶段：并行扫描 (3.6-1 + 3.6-2)
  ├─ 6 个 Sonnet agent 同时启动
  ├─ 各自串行读取 PDF → 识别图像 → 记录元数据
  └─ 输出到 .work/03_verification/scans/

第二阶段：汇总与比对 (3.6-3 + 3.6-4)
  ├─ Opus 主线程合并 6 份扫描结果
  ├─ 与已知 19 幅图像 (Step 2-final: 13 + Step 3-final: 6) 交叉比对
  ├─ 标注状态（已转化 / 待判定 / 故意排除）
  └─ 生成完整清单

第三阶段：用户验收 (3.6-5)
  └─ 用户审阅清单 → 确认排除决策 → 指定待转化项

第四阶段：执行 + 写入 (3.6-6 + 3.6-7)
  ├─ 对待转化项执行 Mermaid/ASCII 转化
  └─ 将完整图像清单写入 TRACEABILITY.md
```

**状态**: 已完成 (2026-04-15)

### 执行结果

| 子步骤 | 状态 | 结果 |
|--------|------|------|
| 3.6-1 | 已完成 | SDTM v2.0: 4 幅图像 |
| 3.6-2 | 已完成 | SDTMIG v3.4: 56 幅图像 (ch: 9, d1: 18, d2: 0, d3: 0, d4: 29) |
| 3.6-3 | 已完成 | 与 Step 2-final (13组/32幅) + Step 3-final (6幅) 交叉比对完成 |
| 3.6-4 | 已完成 | 完整清单 60 幅: 37 已转化 + 21 待判定 + 2 排除 |
| 3.6-5 | 已完成 | 用户决定: CRF→表格, 其余→Mermaid, 无排除 |
| 3.6-6 | 已完成 | 21 幅全部转化: 6 Mermaid + 15 表格 |
| 3.6-7 | 已完成 | TRACEABILITY.md §6 图像内容溯源章节已写入 |

---

## Step 4: 汇总报告 — 已完成 (2026-04-16)

**产出文件**: [`results/step4_summary_report.md`](results/step4_summary_report.md)

**内容**:
1. 知识库规模与文件分类统计
2. 验证执行总表 (293/293 文件 100% 通过)
3. 发现问题统计 (397 处问题 + 4 个 Issue)
4. 内容修复量化 (行数变化 + 40 幅图表补全)
5. 溯源完整性 (535 页 PDF 97.9% 覆盖 + 60 幅图像)
6. 质量保障机制 (5 层验证 + 7 条预防规则)
7. 已知限制与结论
