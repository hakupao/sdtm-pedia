# Q2 (A2 — CP 域) 流式 PBMC 活化 helper T 细胞场景

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83120-7270-83a9-b1cf-73b6af7da6fd
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: 2m 13s

## 完整回答

**结论**: 这个测量在 **CP (Cell Phenotype Findings)** 域, 不是 LB.

CP 的定义: 基于特异 marker 表达表征单细胞/颗粒悬液中的细胞表型/谱系/功能. CP 假设进一步限定: 只有当测试依赖 cell markers 来识别特定细胞群时才用 CP. 对已定义为 CD45+CD3+CD4+CD8- 这类 helper T 细胞群做检测 → CP; 对未定义细胞群的"PBMC 总体"检测 → 不适合 CP.

### (a) Topic 变量

Findings 类域 topic 是 `--TESTCD`, CP 里就是 **CPTESTCD**.

- CPTESTCD = T helper lymphocyte 对应的 CT code
- CPTEST = `TLym Help` 或子集时 `TLym Help Sub` (科学界公认细胞群名称, 不写 marker 串本身)

### (b) 命名细胞群 vs 子集亚群

**区别原则**:
- 命名细胞群放 CPTEST/CPTESTCD (例 `TLym Help`)
- 进一步限定的子集 → 不要塞回 CPTEST, 而是:
  - CPTEST 改带 `Sub` 后缀 (例 `TLym Help Sub`)
  - 用 CPSBMRKS / CPCELSTA / CPCSMRKS 补足子集定义

本例:
- CPTEST = TLym Help Sub
- CPCELSTA = ACTIVATED
- CPCSMRKS = Ki67+

补充: SDTMIG 自带示例里 Ki67+ 更典型表示 PROLIFERATING 而非 ACTIVATED, 但模型允许 CPCSMRKS 记录"用什么 marker operationally 定义该 cell state". 若试验把 Ki67+ 规定为 ACTIVATED, 应在 Define-XML/metadata 里说明.

### (c) Marker 定义"活化"状态变量

核心两个:
- **CPCELSTA** — 细胞状态 (ACTIVATED/PROLIFERATING/SENESCENT)
- **CPCSMRKS** — 定义该 cell state 的 marker string. 规范: "用于定义 CPCELSTA 的 marker(s) or indicator(s)"

强制规则: CPCELSTA 和 CPCSMRKS **必须配对出现**.

补: **CPMRKSTR** 放完整 marker 串 (整个 test 用的所有 markers, 包括已分别出现在 CPSBMRKS/CPCSMRKS 里的). 例如 `CD45+CD3+CD4+CD8-Ki67+`.

### (d) Method 变量

**CPMETHOD = FLOW CYTOMETRY** (CP examples 多处如此填).

### (e) CP vs LB 边界

**一句话**: 看结果是不是"marker-defined cell population finding".

- **放 CP**: 结果依赖 marker 识别/限定细胞群; 关注细胞表型/谱系/功能状态; 流式 cell subset / occupancy / marker expression on defined cells
- **不放 CP, 应 LB**: 测未定义总体样本上的实验室结果; 只测"PBMC 中 Ki67 水平"但没用 markers 界定细胞群; 一般化学/血液/尿/analyte 检测

本例 "活化的 CD4+ T helper, 由 Ki67+ 识别" → 细胞群表型/状态定义, 属 CP.

### 推荐 CP 变量骨架

```
DOMAIN     = CP
CPTESTCD   = (helper T 对应 test code)
CPTEST     = TLym Help Sub
CPCELSTA   = ACTIVATED
CPCSMRKS   = Ki67+
CPSBMRKS   = (null, 除非 sublineage)
CPMRKSTR   = (完整 marker 串)
CPMETHOD   = FLOW CYTOMETRY
CPSPEC     = (按 specimen CT)
CPDTC      = (specimen/test 时间)
```

源溯源:
- `<!-- source: knowledge_base/terminology/core/general_*.md -->` (CP 域定义)
- `<!-- source: knowledge_base/domains/CP/spec.md -->`
- `<!-- source: knowledge_base/domains/CP/assumptions.md -->`
- `<!-- source: knowledge_base/domains/CP/examples.md -->`
- `<!-- source: knowledge_base/chapters/ch04_general_assumptions.md -->`

## 判据对齐

- 域 CP ✓
- Topic = CPTESTCD ✓
- 命名群 vs Sub 子集区别 ✓ (TLym Help vs TLym Help Sub)
- CPSBMRKS / CPCELSTA / CPCSMRKS 三件套 ✓
- 配对规则 (CPCELSTA + CPCSMRKS 必须同时存在) ✓
- CPMETHOD = FLOW CYTOMETRY ✓
- LB 边界 ✓ (marker-defined cell population vs 未定义总体 analyte)
- bonus: Ki67+ 通常代表 PROLIFERATING 而非 ACTIVATED 的诚实纠偏 ✓

## 归因

PASS — Pure generalization. KB CP/spec + assumptions + examples + ch04 + terminology 五锚点全命中. Sub 后缀规则 + 配对规则 + LB 边界 三个非 trivial 知识点都答对. 思考过程透明.
