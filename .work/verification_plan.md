# Knowledge Base 内容验证计划

> 创建日期: 2026-04-14
> 状态: 进行中（Step 0-2, 2-final, 3-1, 3-2 已完成，Step 3-3 ~ 3-5 / 4 待执行）

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
| 1 | 验证 assumptions.md (61 域) | **已完成** (2026-04-14) | 16 问题已修复 → [详细结果](verification/step1_results.md) |
| 2 | 验证 examples.md (63 域, 21 组) | **已完成** (2026-04-14) | 33 PASS / 30 修复后 PASS → [总表](verification/step2_summary.md) · [详细结果](verification/step2_results.md) |
| 2-final | 补全 13 幅图表 (Mermaid) | **已完成** (2026-04-14) | 13/13 图表全部完成 |
| 3 | 验证 model/ + chapters/ (12 文件) | **进行中** | 3-1, 3-2 已完成；3-3 ~ 3-5 待执行 |
| 3.5 | 编写溯源矩阵 (TRACEABILITY.md) | **待开始** | 证明产出完整性，记录排除理由 |
| 4 | 汇总报告 | **待开始** | 见下方计划 |

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
| 3-3 | 验证 chapters/ 小文件 (ch01, ch02, ch03) | 中 (307 行, 15 页 PDF) | **待开始** |
| 3-4 | 验证 ch04_general_assumptions | 重 (331 行, 38 页 PDF) | **待开始** |
| 3-5 | 验证 ch08 + ch10 | 中 (457 行, 32 页 PDF) | **待开始** |

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
| ch01_introduction.md | 94 | 7-10 | — |
| ch02_fundamentals.md | 150 | 11-16 | — |
| ch03_submitting_data.md | 63 | 17-21 | — |
| ch04_general_assumptions.md | 331 | 22-59 | — |
| ch08_relationships.md | 253 | 427-440 | — |
| ch10_appendices.md | 204 | 444-461 | — |

---

## Step 3.5: 编写溯源矩阵（Traceability Matrix）

**目的**: 证明项目产出的完整性和合理性——每一页源 PDF 都被处理过，未收录的内容有明确的排除理由，而非遗漏。

**产出文件**: 项目根目录 `TRACEABILITY.md`（与 README 同级，属于项目交付物）

**内容结构**: 对每份源 PDF 逐章建立映射表：

| 列 | 说明 |
|----|------|
| 章节编号 + 标题 | PDF 原始章节 |
| 页码范围 | PDF 页码 |
| 知识库文件路径 | 对应的产出文件（如有） |
| 处理决策 | `收录` 或 `故意排除` |
| 排除理由 | 仅对排除项填写，说明不收录的原因 |

**覆盖范围**（3 份源 PDF × 全部章节）:

1. **SDTM v2.0 PDF** (74 页, 9 章) → `model/` (6 文件)
   - 收录: Chapter 2–6（模型定义的全部实质性技术内容）
   - 排除: Chapter 1 (Introduction), 7 (Changelog), 8 (Future Changes), 9 (Appendices)
2. **SDTMIG v3.4 PDF** (461 页) → `chapters/` (6 文件) + `domains/` (63 域 × 3 文件)
   - 通用章节: ch01–ch04, ch08, ch10
   - 63 域的 spec/assumptions/examples
3. **SDTM Terminology xlsx** → `terminology/` (91 文件, 脚本生成已校验)

**状态**: 待开始

---

## Step 4: 汇总与修复

1. 汇总全部验证结果，统计 PASS/FAIL 率
2. 对 FAIL 的文件逐个修复
3. 修复后重新验证
4. 更新项目质量状态
