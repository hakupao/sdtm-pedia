# Knowledge Base 内容验证计划

> 创建日期: 2026-04-14
> 状态: 进行中（Step 0-2, 2-final 已完成，Step 3 / 4 待执行）

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
| 3 | 验证 model/ + chapters/ (12 文件) | **待开始** | 见下方计划 |
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

---

## Step 4: 汇总与修复

1. 汇总全部验证结果，统计 PASS/FAIL 率
2. 对 FAIL 的文件逐个修复
3. 修复后重新验证
4. 更新项目质量状态
