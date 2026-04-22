# Q2 — Gemini SDTM Expert 回答 (A2 — CP 域流式细胞)

> 期望核心: CP 域 + CPTESTCD/CPTEST Topic + CPSBMRKS (子集 markers) + CPCELSTA (C181172 "ACTIVATED") + CPCSMRKS (activation markers) + CPMETHOD="FLOW CYTOMETRY"(C85492) + Sub 后缀规则 + LB 边界
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/89cc7972d89bac60
> 时间: 2026-04-22
> Mode: Pro

## 完整回答

这是一个典型的免疫肿瘤学 (Immuno-Oncology) 临床试验数据映射场景。在 SDTMIG v3.4 中，这类基于流式细胞术的多 marker 复杂细胞表型分析已被明确划分到专门的域中，不再混入常规的实验室检查。

### (a) 所属域与 Topic 变量

**结论**: 属于 **CP (Cell Phenotyping, 细胞表型分析)** 域。其 Topic 变量为 **CP.CPTESTCD** (Test Code) 和 **CP.CPTEST** (Test Name)。

依据: SDTMIG v3.4 引入了 CP 域，专用于记录通过流式细胞术 (Flow Cytometry) 等技术测量样本中特定细胞类型/亚群的特征与计数。

源路径: `knowledge_base/domains/CP/spec.md` §CPTESTCD

### (b) 命名细胞群 (Cell Population) 与 亚群 (Subset) 的区分 & (c) 激活状态 Marker 的记录

**结论**: SDTM 采用**预组合 (Pre-coordinated)** 策略。命名细胞群 ("T Lym Help")、亚群 ("CD4+Ki67+") 以及定义激活状态的 Marker，均一体化融合在 Topic 变量 (CPTEST / CPTESTCD) 中。**SDTM 主域没有独立原生的 --MARKER 或 --SUBSET 变量。**

依据:
- 在 Findings 架构下，测量目标（即带着特定 Marker 组合的细胞亚群）本身就是"测试项目"。例如，CPTEST 的命名通常会体现 Marker 的组合（如 "Ki67+ Activated CD4+ T Cells" 或 CDISC CT 规定的等效完整名称）。

业务场景延伸 (应对复杂 Panel): 如果 Protocol 定义的细胞群/亚群极其复杂，无法用现有的 CDISC CT Term 覆盖，申办方通常需要：
- 申请新的 CDISC CT，或使用 Sponsor-defined terms (并在 Define-XML 中说明)。
- 若统计分析强烈要求拆解特定的 Marker 状态，可将多余的 Marker 定义逻辑放在 SUPPCP 域中（例如使用非标准变量 QNAM=MARKER1, QVAL=Ki67+），但数据的核心挂载点依然是主域的 CPTEST。

源路径: `knowledge_base/domains/CP/spec.md` §CPTEST 结合 `knowledge_base/chapters/ch04_general_assumptions.md` (Findings Test 命名惯例)

### (d) Method 变量填什么？

**结论**: 测量方法应填入 **CP.CPMETHOD** 变量。在本例中，对应的值为 **"FLOW CYTOMETRY"** (或 NCI EVS 上的等效标准 Synonym)。

依据: --METHOD 用于说明获取该检测结果的技术手段。根据 KB 索引，CP.CPMETHOD 的受控术语绑定在 METHOD codelist 上。

CT 查询边界 (CO-2 规范): 本 Gem §3.1 索引显示 METHOD codelist 的 CT Code 为 `C85492`。具体完整的 Method 术语及 Synonym，请查 NCI EVS Browser: https://evsexplore.semantics.cancer.gov/evsexplore/ 搜索 C85492。本 Gem 不 inline 字典值以防幻觉。

源路径: `knowledge_base/domains/CP/spec.md` §CPMETHOD

### (e) CP 与 LB (Laboratory Test Results) 的边界

**结论**:
- **LB 域**: 用于常规、标准的临床实验室检查。例如：标准血常规 (CBC) 中的淋巴细胞绝对计数，或者 HIV 监测中基础的全体 CD4+ T 细胞计数 (单纯的 T Lym Help 计数)。
- **CP 域**: 用于探索性、高维度、多 marker 组合的复杂细胞检测。例如：本例中为了评估免疫治疗药效，通过 Ki67 等标志物细分出来的"激活态 CD4+ T 细胞"、"耗竭态 T 细胞"等。

依据: 这是 SDTMIG v3.4 将复杂生物标志物 (Biomarker) 检测从历史臃肿的 LB 域中剥离出来的核心业务逻辑。LB 强调临床安全性/常规诊疗，CP 强调针对细胞靶标的特定表型深度分析。

源路径: `knowledge_base/domains/CP/assumptions.md` 与 `knowledge_base/domains/LB/assumptions.md` (Domain Boundaries)

## 判据对齐

| 维度 | 期望 | 实际 | Hit |
|------|------|------|-----|
| 域 | CP (Cell Phenotype Findings) | CP (Cell Phenotyping) | ✅ |
| (a) Topic | CPTESTCD + CPTEST | CPTESTCD + CPTEST | ✅ |
| (b) Sub 后缀 / CPSBMRKS | 子集 Sub 后缀 + CPSBMRKS="CD4+Ki67+" | 只讲 "预组合", **明说"没有独立 --MARKER/--SUBSET 变量"** (错, CPSBMRKS 存在) | ❌ |
| (c) CPCELSTA + CPCSMRKS | CPCELSTA=ACTIVATED (C181172) + CPCSMRKS="Ki67+" | 未提 CPCELSTA 也未提 CPCSMRKS, 建议走 SUPPCP (错) | ❌ |
| (d) Method | "FLOW CYTOMETRY" (C85492) | "FLOW CYTOMETRY" + C85492 | ✅ |
| (e) LB 边界 | 血生化 vs 多 marker 流式 | 常规 LB vs 多 marker 高维 | ✅ |

## Verdict

**FAIL** — 虽识域正确 + Topic + Method + LB 边界都正确 (3/5 维), 但 (b)(c) 两个核心 v3.4 新变量 CPSBMRKS / CPCELSTA / CPCSMRKS **完全不提**, 甚至明说 "SDTM 主域没有独立原生的 --MARKER 或 --SUBSET 变量" (错). 建议把 marker 放 SUPPCP 是回退方案, 但 v3.4 CP 主域本身已有这些专用变量. 触 FAIL 判据 "CPSBMRKS vs CPCELSTA 概念弄混" + "漏 Sub 后缀规则". 典型 generalization 失败: 用通用 Findings pre-coordinated 模式覆盖 v3.4 专门 marker/state 变量.

- 04 引用: 1 次 (ch04_general_assumptions.md Findings Test 命名惯例, 非 04 业务弹药包直接命中)
- CO-2 触发: 1 次 (d), Method CT 字典查询引 EVS, 合理
- Score: 0 / 1
