# Q2 (A2 — CP 域) 流式细胞测 CD4+ T 细胞 ACTIVATED 亚群

> Date: 2026-04-22
> Account: bojiang.zhang.0904@gmail.com
> Notebook: SDTM Knowledge Base (42/42 sources, fresh chat after delete)

---

## 题

某免疫治疗试验用流式细胞仪检测受试者 PBMC 样本里 "活化的 CD4+ T 辅助细胞" (通过 Ki67+ 表达识别为 ACTIVATED 状态). SDTMIG v3.4 里这个测量属于哪个域? 请说明: (a) Topic 变量是什么; (b) 如何区别"T Lym Help" 这个命名细胞群与 CD4+Ki67+ 这个子集亚群; (c) 用哪些变量记录"哪些 marker 被用来定义'活化'状态"; (d) Method 变量应填什么 (测量方法); (e) 这个域和 LB 的边界是什么.

## NotebookLM 答 (full text)

针对您描述的在临床试验中使用流式细胞仪检测 PBMC 样本中"活化的 CD4+ T 辅助细胞 (Ki67+)"的场景, 在 SDTMIG v3.4 中, 该测量属于 **CP (Cell Phenotype Findings, 细胞表型发现)** 域 [235_ct_misc_int_dm_sp_td_gf_oi_other.md], [283_variable_index.md]。

### (a) Topic 变量是什么

在 CP 域中, Topic 变量是 `CPTESTCD` (Test or Examination Short Name), 其对应的 Synonym Qualifier 是 `CPTEST` (Name of Measurement, Test or Examination)。这两个变量的 Core 均为 Req [283_variable_index.md]。

### (b) 如何区别 "T Lym Help" 命名细胞群与带有特定状态的子集亚群?

根据 CP 域的规则, 当测试对象是一个基于特定细胞状态 (如活化、增殖、凋亡等) 被进一步限制的亚群时, 必须在基础细胞名称后加上 **"Sub" 后缀** [126_fnd_morphology_bs_cp_cv.md]。

- 对于标准的 T 辅助细胞, `CPTEST` 会填入 `TLym Help`。
- 对于您描述的活化亚群, `CPTEST` 必须填入对应的亚群变体, 即 `TLym Help Sub` (对应 NCI C-code 为 C184351 [263_ct_specialized_micro_oncology_pk_is_cp.md]) [134_fnd_morphology_bs_cp_cv.md]。

同时, 必须将定义该完整细胞亚群的所有 marker 组合 (例如包含 CD45, CD3, CD4, Ki67 等的完整字符串) 填入 `CPMRKSTR` (Marker String) 中, 以在操作层面完整定义该测试 [130_fnd_morphology_bs_cp_cv.md]。

### (c) 用哪些变量记录"哪些 marker 被用来定义'活化'状态"?

这需要使用一对必须联合使用的变量来精确记录 [134_fnd_morphology_bs_cp_cv.md]:

- `CPCELSTA` (Cell State): 记录细胞状态本身, 此处应填入 `ACTIVATED` (受控术语 Codelist C181172)。
- `CPCSMRKS` (Cell State Marker String): 记录专门用于定义该细胞状态 (即 CPCELSTA 中的状态) 的 marker 字符串。此处应填入 `Ki67+` [128_fnd_morphology_bs_cp_cv.md]。

### (d) Method 变量应填什么

测量方法应记录在 `CPMETHOD` (Method of Test or Examination) 变量中。基于您使用的是流式细胞术, 对应的受控术语 (Codelist C85492) 全称必须填入 **FLOW CYTOMETRY** [133_fnd_morphology_bs_cp_cv.md], [145_fnd_morphology_bs_cp_cv.md]。

### (e) CP 域和 LB 域的边界是什么?

CP 和 LB 的核心边界在于是否依赖细胞表达 marker (如 CD 表面抗原、细胞内染色等) 来鉴定特定的细胞群:

- **CP 域**: 仅用于包含"细胞表型分析"成分的测试, 即必须依赖使用细胞 marker 来识别/定义特定的细胞群 (例如使用 CD4 等 marker 定义 T 辅助细胞群, 并在该群体上测量 Ki67 表达)。所有流式细胞术 (Flow Cytometry) 的数据通常都应建模在 CP 域 [117_fnd_pharma_pc_pp.md], [134_fnd_morphology_bs_cp_cv.md]。
- **LB 域**: 常规的液体样本 (如血液、尿液) 中的细胞检查 (例如不依赖特定表型 marker 分型的全血细胞计数 CBC), 或者在未明确定义表型的宽泛细胞群 (如未分类的 PBMC) 中进行细胞因子或趋化因子的分泌测量, 应归入 LB 域 [55_fnd_biomarkers_mb_mi_ms_mk.md], [117_fnd_pharma_pc_pp.md], [134_fnd_morphology_bs_cp_cv.md]。

### 涉及的关键变量 (CP Domain)

| Variable | Type | Role | Core | CT | Source |
|---|---|---|---|---|---|
| CPTESTCD | Char | Topic | Req | C181173 | [283_variable_index.md] |
| CPTEST | Char | Synonym Qualifier | Req | C181174 | [283_variable_index.md], [126_fnd_morphology_bs_cp_cv.md] |
| CPCELSTA | Char | Variable Qualifier | Perm | C181172 | [283_variable_index.md], [128_fnd_morphology_bs_cp_cv.md] |
| CPCSMRKS | Char | Variable Qualifier | Perm | — | [283_variable_index.md], [128_fnd_morphology_bs_cp_cv.md] |
| CPMRKSTR | Char | Record Qualifier | Exp | — | [283_variable_index.md], [130_fnd_morphology_bs_cp_cv.md] |
| CPMETHOD | Char | Record Qualifier | Perm | C85492 | [283_variable_index.md], [133_fnd_morphology_bs_cp_cv.md] |

## Verdict

| Criterion | Required | Got | Status |
|---|---|---|:---:|
| Domain = CP | CP (Cell Phenotype Findings) | CP confirmed | ✅ |
| (a) Topic CPTESTCD + CPTEST (Req) | both | both ✓ | ✅ |
| (b) Sub suffix + CPMRKSTR for sub-group | Sub suffix + marker string | "TLym Help Sub" + CPMRKSTR with full marker combo | ✅ |
| (c) CPCELSTA="ACTIVATED" + CPCSMRKS="Ki67+" | both | CPCELSTA=ACTIVATED (C181172) + CPCSMRKS=Ki67+ ✓ | ✅ |
| (d) CPMETHOD = FLOW CYTOMETRY (C85492) | exact value | "FLOW CYTOMETRY" + C85492 ✓ | ✅ |
| (e) CP vs LB boundary | marker-dependent vs traditional | CP=marker-defined cell pop; LB=CBC/non-typed | ✅ |

**Verdict**: ✅ **PASS** (1 / 1) — 5 项判据全中 + 加分: CT C181172 (CPCELSTA), C181173/C181174 (CPTESTCD/CPTEST), C85492 (CPMETHOD), C184351 (TLym Help Sub) 全部对。Sub 后缀规则明文。无任何 FAIL 触发。
