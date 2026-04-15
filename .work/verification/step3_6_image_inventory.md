# Step 3.6 图像内容溯源 — 完整清单

> 生成日期: 2026-04-15
> 扫描范围: SDTM v2.0 (74页) + SDTMIG v3.4 (461页) = 535页
> 扫描结果: 60 幅图像

---

## 统计摘要

| 分类 | 数量 | 说明 |
|------|------|------|
| 已转化 | 37 | Step 2-final (13组/32幅) + Step 3-final (5幅) 已完成 Mermaid/ASCII 转化 |
| 故意排除 | 2 | Logo 装饰性图片 |
| 待判定 | 21 | 需用户审阅确认（3 Concept Map + 3 ch04 CRF + 12 域 CRF + 3 TD 时间轴） |
| **合计** | **60** | |

---

## 完整图像清单

### A. SDTM v2.0 PDF (4 幅)

| # | 页码 | 所属章节 | 图像类型 | 简要描述 | 转化格式 | 目标文件 | 处理批次 | 状态 | 排除理由 |
|---|------|----------|----------|----------|----------|----------|----------|------|----------|
| 1 | 1 | 封面 | Logo / 封面装饰 | CDISC 彩色圆点 Logo | — | — | — | 故意排除 | 装饰性图片，无知识内容 |
| 2 | 8 | §2 Concepts and Terms | 关系/层次图 | Concept Map: Relationships Between SDTM Domains — 树状框图，以 SDTM 为根，展开 Subject Data / AP Data / Study-Level / Relationships 四支 | — | model/01_concepts_and_terms.md | — | **待判定** | |
| 3 | 62 | §5.2.1 Device Identifiers | 关系图 | Concept Map: Device Identifier Variables — Study→Device→Identifying Characteristic→parameter→value 链式关系 | — | model/05_study_level_data.md | — | **待判定** | |
| 4 | 63 | §5.2.2 Non-host Organism IDs | 关系图 | Concept Map: Non-host Organism Identifier Variables — Study→Non-Host Organism→Taxon→parameter→value 链式关系 | — | model/05_study_level_data.md | — | **待判定** | |

### B. SDTMIG v3.4 — 通用章节 p.1-59 (9 幅)

| # | 页码 | 所属章节 | 图像类型 | 简要描述 | 转化格式 | 目标文件 | 处理批次 | 状态 | 排除理由 |
|---|------|----------|----------|----------|----------|----------|----------|------|----------|
| 5 | 1 | 封面 | Logo / 封面装饰 | CDISC 彩色圆点 Logo | — | — | — | 故意排除 | 装饰性图片，无知识内容 |
| 6 | 15 | §2.6 Creating a New Domain | 关系/层次图 | Figure: Creating a New Domain — Identifier/Timing/Topic+Qualifier Variables 组合构成 New Domain | Mermaid | chapters/ch02_fundamentals.md | Step 3-final | 已转化 | |
| 7 | 31 | §4.2.7.1 Specify for Non-result | CRF 模拟图 | EXADJ 复选框 + 镇痛药适应证选项框 — 说明 CRF 自由文本提交场景 | — | chapters/ch04_general_assumptions.md | — | **待判定** | |
| 8 | 32 | §4.2.7.2 Specify for Result | CRF 模拟图 | Eye Color CRF — Brown/Black/Blue/Green/Other specify 选项 | — | chapters/ch04_general_assumptions.md | — | **待判定** | |
| 9 | 33 | §4.2.7.3 Specify for Topic | CRF 模拟图 | Concomitant Medications CRF — Acetaminophen/Aspirin/Ibuprofen/Naproxen/Other specify | — | chapters/ch04_general_assumptions.md | — | **待判定** | |
| 10 | 34 | §4.2.7.4 Specify for --OBJ | 决策树 | Figure: Decision Tree for Populating --OBJ — 多分支判定流程 | Mermaid | chapters/ch04_general_assumptions.md | Step 3-final | 已转化 | |
| 11 | 44 | §4.4.7 Relative Timing | 时间轴 | Figure: --ENRTPT and --ENTPT for Medical History — 水平时间轴示意 | Mermaid | chapters/ch04_general_assumptions.md | Step 3-final | 已转化 | |
| 12 | 46 | §4.4.10 Representing Time Points | 时间轴/架构图 | Figure: Representing Time Points — Reference/Elapsed/Collection 三概念关系 | Mermaid | chapters/ch04_general_assumptions.md | Step 3-final | 已转化 | |
| 13 | 51 | §4.5.1.1 Original & Standardized | 流程图 | Figure: Original to Standardized Results — --ORRES→--STRESC→--STRESN 转换 | Mermaid | chapters/ch04_general_assumptions.md | Step 3-final | 已转化 | |

### C. SDTMIG v3.4 — 域章节 p.60-159 (18 幅)

| # | 页码 | 所属章节/域 | 图像类型 | 简要描述 | 转化格式 | 目标文件 | 处理批次 | 状态 | 排除理由 |
|---|------|-------------|----------|----------|----------|----------|----------|------|----------|
| 14 | 71 | DM Example 4 | CRF Mockup | aCRF for Race — RACE01-07 勾选框 + CDASH 变量标注（红/灰色块） | Mermaid | knowledge_base/DM/examples.md | Step 2-final | 已转化 | |
| 15 | 71 | DM Example 4 | CRF Mockup | 子分类 CRF — AMERICAN INDIAN OR ALASKA NATIVE 子项 (CRACE01-04) | Mermaid | knowledge_base/DM/examples.md | Step 2-final | 已转化 | |
| 16 | 72 | DM Example 4（续） | CRF Mockup | ASIAN / BLACK OR AFRICAN AMERICAN / WHITE 三个子分类 CRF (CRACE05-21) | Mermaid | knowledge_base/DM/examples.md | Step 2-final | 已转化 | |
| 17 | 74 | DM Example 5 | CRF Mockup | CRF Mock — 中国民族子分类 HAN/MANCHU/MIAO/UYGHUR/ZHUANG | Mermaid | knowledge_base/DM/examples.md | Step 2-final | 已转化 | |
| 18 | 75 | DM Example 6 | CRF Mockup | aCRF for Race（第二版）— RACE01-07 + ASIAN/BLACK 子分类 | Mermaid | knowledge_base/DM/examples.md | Step 2-final | 已转化 | |
| 19 | 78 | DM Example 7 | CRF Mockup | CRF Mock — 5 种族 + Unknown + Other + RACEOTH/RACEREAS | Mermaid | knowledge_base/DM/examples.md | Step 2-final | 已转化 | |
| 20 | 111 | EX/EC Example 1 | CRF Mockup | Exposure CRF — Bottle/Tablets Daily/Reason/Start Date/End Date | — | knowledge_base/EX/examples.md | — | **待判定** | |
| 21 | 112 | EX/EC Example 2 | CRF Mockup | Exposure CRF（注射）— Visit/Date/Injection 1-3 Volume/Location/Side | — | knowledge_base/EX/examples.md | — | **待判定** | |
| 22 | 114 | EX/EC Example 5 | CRF Mockup | 双盲交叉研究 CRF — Bottle/Time Point/Tablets/Start/End Date | — | knowledge_base/EX/examples.md | — | **待判定** | |
| 23 | 115 | EX/EC Example 6 | CRF Mockup | 单次给药交叉 CRF — Period 1/2, Day/Capsules/Tablets/DateTime | — | knowledge_base/EX/examples.md | — | **待判定** | |
| 24 | 118 | EX/EC Example 7 | CRF Mockup | 输液给药 CRF — Visit 1/2/3, Dose/Adjustment/Amount/Concentration | — | knowledge_base/EX/examples.md | — | **待判定** | |
| 25 | 119 | EX/EC Example 8 | CRF Mockup | 简化给药日志 CRF — First/Last Dose Date + Deviation Log | — | knowledge_base/EX/examples.md | — | **待判定** | |
| 26 | 123 | ML Example 1 | CRF Mockup | Meal Log CRF — Type(Snack/Drink/Meal)/Volume/Date/Time/Event ID | — | knowledge_base/ML/examples.md | — | **待判定** | |
| 27 | 123 | ML Example 1 | CRF Mockup | DILI Meal CRF — Wild mushrooms/Ackee fruit/Cycad seeds Yes/No | — | knowledge_base/ML/examples.md | — | **待判定** | |
| 28 | 139 | AE Assumptions | CRF 局部示意 | AE 严重性 CRF 片段 — Serious? Yes/No + Fatal/Life-threatening/... 勾选 | — | knowledge_base/AE/assumptions.md | — | **待判定** | |
| 29 | 151 | CE Example 1 | CRF Mockup | 预设临床事件 CRF — Rash/Wheezing/Edema/Conjunctivitis Yes/No/Date | — | knowledge_base/CE/examples.md | — | **待判定** | |
| 30 | 152 | CE Example 2 | CRF Mockup | 含严重程度 CRF — Nausea/Vomit/Diarrhea/Other + Severity 单选 | — | knowledge_base/CE/examples.md | — | **待判定** | |
| 31 | 153 | CE Example 3 | CRF Mockup | Bone Fracture Assessment CRF — 骨折评估全表（部位/侧别/治疗/并发症） | — | knowledge_base/CE/examples.md | — | **待判定** | |

### D. SDTMIG v3.4 — 域章节 p.160-359 (0 幅)

> p.160-359 (200页) 全部为纯文字段落和标准数据表格，无图形化内容。
> 涵盖域：DS, HO, MH, DV, DA, DD, EG, IE, BS, CP, GF, IS, LB, MB, MS, BE, PC, PP, MO, CV, MK, OE, RP, RE, PE, FT, QS, RS, SC, SS, TU, TR, VS

### E. SDTMIG v3.4 — 域章节 p.360-461 (29 幅)

| # | 页码 | 所属章节/域 | 图像类型 | 简要描述 | 转化格式 | 目标文件 | 处理批次 | 状态 | 排除理由 |
|---|------|-------------|----------|----------|----------|----------|----------|------|----------|
| 32 | 386 | TA Example 1 | Study Schema | Parallel Design Study Schema — Screen→Run-In→Placebo/Drug A/Drug B | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 33 | 387 | TA Example 1 | Schema (前瞻) | Parallel Design Prospective View — 按 Epoch 分列 | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 34 | 387 | TA Example 1 | Schema (回顾) | Parallel Design Retrospective View — 网格形式 | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 35 | 387 | TA Example 1 | Schema (盲态) | Parallel Design Blinded View — 单行 Screen→Drug | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 36 | 389 | TA Example 2 | Study Schema | Crossover Trial Study Schema — 三条并行路径 | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 37 | 390 | TA Example 2 | Schema (前瞻) | Crossover Trial Prospective View | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 38 | 390 | TA Example 2 | Schema (回顾) | Crossover Trial Retrospective View | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 39 | 391 | TA Example 2 | Schema (盲态) | Crossover Trial Blinded View | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 40 | 393 | TA Example 3 | Study Schema | Multiple Branches Study Schema — 两阶段随机 | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 41 | 393 | TA Example 3 | Schema (前瞻) | Multiple Branches Prospective View | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 42 | 394 | TA Example 3 | Schema (回顾) | Multiple Branches Retrospective View | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 43 | 394 | TA Example 3 | Schema (盲态) | Multiple Branches Blinded View | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 44 | 396 | TA Example 4 | Study Schema | Cyclical Chemotherapy Study Schema — 循环箭头 | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 45 | 397 | TA Example 4 | Schema (前瞻) | Cyclical Chemotherapy Prospective View | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 46 | 397 | TA Example 4 | Schema (回顾) | Cyclical Chemotherapy Retrospective View | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 47 | 397 | TA Example 4 | Schema (回顾+显式) | Cyclical Chemo Retrospective with Explicit Repeats — 4 周期展开 | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 48 | 398 | TA Example 4 | Schema (盲态) | Cyclical Chemotherapy Blinded View | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 49 | 399 | TA Example 5 | Study Schema | Different Chemo Durations Study Schema — Drug A/B 3 周期 | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 50 | 399 | TA Example 5 | Schema (回顾) | Different Chemo Durations Retrospective View | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 51 | 400 | TA Example 6 | Study Schema | Different Cycle Durations Study Schema — A 3周/B 4周 | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 52 | 400 | TA Example 6 | Schema (回顾) | Different Cycle Durations Retrospective View | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 53 | 401 | TA Example 7 | Study Schema | RTOG 93-09 Study Schema with 5 Options — 多分支 | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 54 | 402 | TA Example 7 | Schema (前瞻) | RTOG 93-09 Prospective View — CR/CRS 双臂 | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 55 | 403 | TA Example 7 | Schema (回顾) | RTOG 93-09 Retrospective View | Mermaid | knowledge_base/TA/examples.md | Step 2-final | 已转化 | |
| 56 | 412 | TV Example 1 | 时间轴/Visit 示意 | Parallel Design Planned Visits — Retrospective + Visit flags | Mermaid | knowledge_base/TV/examples.md | Step 2-final | 已转化 | |
| 57 | 416 | TD Example 1 | 时间轴 | Disease Assessment Schedule 1(8w)/2(12w)/3(24w) — 三角标记 | — | knowledge_base/TD/examples.md | — | **待判定** | |
| 58 | 417 | TD Example 2 | 时间轴 | Disease Assessment Period 1/2, ANCH1DT/ANCH2DT, 每 8 周 | — | knowledge_base/TD/examples.md | — | **待判定** | |
| 59 | 418 | TD Example 3 | 时间轴 | Disease Assessment Double Blind/Extension, Schedule 1+2 | — | knowledge_base/TD/examples.md | — | **待判定** | |
| 60 | 440 | RELSPEC Example 1 | 层次/关系图 | Sample Specimen Relationship — SPC-001→SPC-001-A/B→SPC-001-B-1 层次衍生 | Mermaid | knowledge_base/RELSPEC/examples.md + chapters/ch08_relationships.md | Step 2-final + Step 3-final | 已转化 | |

---

## 交叉比对：已处理图像映射

### Step 2-final (13 组 → 32 幅扫描图像)

| 原编号 | 域/Example | 计划页码 | 实际扫描页码 | 清单序号 | 扫描子图数 |
|--------|-----------|----------|-------------|----------|-----------|
| 1 | DM Example 4 | 70-71 | 71-72 | #14-16 | 3 |
| 2 | DM Example 5 | 74 | 74 | #17 | 1 |
| 3 | DM Example 6 | 75 | 75 | #18 | 1 |
| 4 | DM Example 7 | 78 | 78 | #19 | 1 |
| 5 | TA Example 1 | ~387-388 | 386-387 | #32-35 | 4 |
| 6 | TA Example 2 | ~389-391 | 389-391 | #36-39 | 4 |
| 7 | TA Example 3 | ~392-393 | 393-394 | #40-43 | 4 |
| 8 | TA Example 4 | ~394-396 | 396-398 | #44-48 | 5 |
| 9 | TA Example 5 | ~397 | 399 | #49-50 | 2 |
| 10 | TA Example 6 | ~398 | 400 | #51-52 | 2 |
| 11 | TA Example 7 | ~400-401 | 401-403 | #53-55 | 3 |
| 12 | TV Example 1 | 409 | 412 | #56 | 1 |
| 13 | RELSPEC Example 1 | 440 | 440 | #60 | 1 |

### Step 3-final (6 幅 → 5 幅独立 + 1 幅与 Step 2-final 重叠)

| 原编号 | 文件/章节 | 计划页码 | 实际扫描页码 | 清单序号 |
|--------|----------|----------|-------------|----------|
| 1 | ch02 Creating a New Domain | ~p.16 | 15 | #6 |
| 2 | ch04 Decision Tree --OBJ | ~p.35 | 34 | #10 |
| 3 | ch04 --ENRTPT/--ENTPT | ~p.47 | 44 | #11 |
| 4 | ch04 Representing Time Points | ~p.50 | 46 | #12 |
| 5 | ch04 Original→Standardized | ~p.52 | 51 | #13 |
| 6 | ch08 Specimen Relationship | ~p.443 | 440 | #60 (与 Step 2-final #13 重叠) |

---

## 待判定图像分类 (21 幅)

### 类型 1: Concept Map — SDTM 模型结构图 (3 幅)

| 清单# | 页码 | 描述 | 建议 |
|--------|------|------|------|
| #2 | v2.0 p.8 | SDTM Domains 全局关系树状图 | 模型核心架构图，建议转化 |
| #3 | v2.0 p.62 | Device Identifier Variables 关系图 | 设备标识结构图，建议转化 |
| #4 | v2.0 p.63 | Non-host Organism Identifier Variables 关系图 | 非宿主生物标识结构图，建议转化 |

### 类型 2: ch04 General Assumptions CRF 示例 (3 幅)

| 清单# | 页码 | 描述 | 建议 |
|--------|------|------|------|
| #7 | IG p.31 | EXADJ 复选框 + 镇痛药适应证 CRF | 说明 Specify 值处理，结构简单 |
| #8 | IG p.32 | Eye Color CRF (Other specify) | 说明 Result Qualifier Specify，结构简单 |
| #9 | IG p.33 | Concomitant Medications CRF (Other specify) | 说明 Topic Variable Specify，结构简单 |

### 类型 3: 域 CRF Mockup — Exposure (6 幅)

| 清单# | 页码 | 描述 | 建议 |
|--------|------|------|------|
| #20 | IG p.111 | EX Example 1 — 口服给药 CRF | 表格形式 CRF |
| #21 | IG p.112 | EX Example 2 — 注射给药 CRF | 表格形式 CRF |
| #22 | IG p.114 | EX Example 5 — 双盲交叉 CRF | 表格形式 CRF |
| #23 | IG p.115 | EX Example 6 — 单次给药交叉 CRF | 表格形式 CRF |
| #24 | IG p.118 | EX Example 7 — 输液给药 CRF | 详细字段 CRF |
| #25 | IG p.119 | EX Example 8 — 简化给药日志 CRF | 简表 CRF |

### 类型 4: 域 CRF Mockup — 其他域 (6 幅)

| 清单# | 页码 | 域 | 描述 | 建议 |
|--------|------|------|------|------|
| #26 | IG p.123 | ML | Meal Log CRF — Snack/Drink/Meal | 表格形式 CRF |
| #27 | IG p.123 | ML | DILI Meal CRF — 毒蘑菇/荔枝/苏铁 | 表格形式 CRF |
| #28 | IG p.139 | AE | 严重性分类 CRF 片段 — Serious?/Fatal/... | 小型示意，非完整 CRF |
| #29 | IG p.151 | CE | Example 1 CRF — 预设临床事件 | 表格形式 CRF |
| #30 | IG p.152 | CE | Example 2 CRF — 含严重程度 | 表格形式 CRF |
| #31 | IG p.153 | CE | Example 3 Bone Fracture Assessment CRF | 详细评估表 |

### 类型 5: TD 时间轴 (3 幅)

| 清单# | 页码 | 描述 | 建议 |
|--------|------|------|------|
| #57 | IG p.416 | TD Example 1 — 3 段评估计划 (8w/12w/24w) | 时间轴图，建议转化 |
| #58 | IG p.417 | TD Example 2 — 2 段 Period (ANCH1DT/ANCH2DT) | 时间轴图，建议转化 |
| #59 | IG p.418 | TD Example 3 — Double Blind + Extension | 时间轴图，建议转化 |
