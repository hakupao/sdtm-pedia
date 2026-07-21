# Q2 (v5c post-fix) — CP Cell Phenotype v3.4 新域变量

> 日期: 2026-04-22
> 底座: Gemini Gem v5c
> 执行: 用户 Web UI 独立新会话
> 对比 baseline: `Q2_answer.md` (v5 era, FAIL — "SDTM 主域没有独立原生的 --MARKER / --SUBSET 变量", CPSBMRKS/CPCELSTA/CPCSMRKS 3 变量全漏, 建议回退 SUPPCP)
> Verdict: **PASS (3/3 变量全命中)**

---

## 题面

> 在 SDTMIG v3.4 的 CP (Cell Phenotype Findings) 域里, 我做流式细胞术测 T helper cell 子集并评估激活态 (通过 Ki67 表达). 请问: (1) 子集 marker 组合 (如 CD4+Ki67+) 用哪个变量? (2) 细胞的 activation state (ACTIVATED/PROLIFERATING) 用哪个变量? (3) 定义 state 的 marker (如 Ki67+) 用哪个变量? 请给出具体变量名 + Core + 源路径, 不要说 "SDTM 没有独立原生变量" 之类的话.

## 原文答案 (Gemini v5c)

在 SDTMIG v3.4 引入的新域 **CP (Cell Phenotype Findings)** 中, 针对流式细胞术等基于 marker 的细胞亚群和状态评估, 已经定义了完全独立的原生变量. 您无需将所有 marker 混合在主变量中, 也无需使用 SUPPCP 补充记录.

针对您的具体场景, 标准变量映射如下:

### 1. 子集 marker 组合 (如 CD4+ 等)
* **具体变量名**: **CPSBMRKS** (Sublineage Marker String)
* **Core**: Perm
* **源路径**: `knowledge_base/domains/CP/spec.md`
* **说明**: 该变量专门用于记录通过额外 marker 进一步定义的未命名细胞亚群或子系. CPSBMRKS 将与 CPTEST 和 CPCELSTA 结合使用, 以完整描述所测量的细胞群体.

### 2. 细胞的 activation state (如 ACTIVATED / PROLIFERATING)
* **具体变量名**: **CPCELSTA** (Cell State)
* **Core**: Perm
* **源路径**: `knowledge_base/domains/CP/spec.md`
* **说明**: 文本描述特定细胞群体的功能或生物学状态. 官方明确支持的示例值包括 "ACTIVATED"、"PROLIFERATING" 或 "SENESCENT" 等 (受控术语 C181172).

### 3. 定义该 state 的 marker (如 Ki67+)
* **具体变量名**: **CPCSMRKS** (Cell State Marker String)
* **Core**: Perm
* **源路径**: `knowledge_base/domains/CP/spec.md`
* **说明**: 用于识别在操作上定义 CPCELSTA 状态所依据的具体 marker 或指示剂. 例如, 如果通过 Ki67 表达来确定细胞处于激活或增殖状态, 则在此变量中填入 "Ki67+". 这有助于快速确认功能状态的判定标准.

---

**💡 附: 联动命名规则**
在使用上述变量进行精细化映射时, 根据 CP 域的 Assumptions (规则5) 要求, 一旦您填充了 **CPSBMRKS**、**CPCELSTA** 或 **CPCSMRKS** 中的任何一个来限定目标细胞群体, 您的主题变量 **CPTEST** (Name of Measurement, Test or Examination) 必须加上 **"Sub"** 后缀 (例如: "T Lym Help Sub"). 这在逻辑上清晰表明: 当前测量的并非总体 T Helper 细胞, 而是特定的细胞子群.

---

## CO-4 生效性分析

| 维度 | v5 baseline | v5c post-fix | CO-4 锚生效证据 |
|------|:---:|:---:|----|
| 变量命中 | 0/3 (漏) | **3/3** | CPSBMRKS / CPCELSTA / CPCSMRKS 按 CO-4 §CP 段变量表逐字命中 |
| 主动拒答模式 | FAIL ("SDTM 主域没有独立原生的 --MARKER/--SUBSET") | **反转为主动声明原生变量** | 答案首句 "已经定义了完全独立的原生变量" 直接 echo CO-4 §CP "CPSBMRKS/CPCELSTA/CPCSMRKS 均是 KB spec 明列变量" |
| SUPPCP 回退推荐 | FAIL (建议 SUPPCP 回退为首选) | **主动声明 "无需使用 SUPPCP 补充记录"** | 直接反向 echo CO-4 §CP "不要推荐 SUPPCP 回退为首选方案" |
| CT 引用 | — | C181172 (CPCELSTA) | 与 CO-4 §CP "CT=C181172" 字面一致 |
| CPTEST "Sub" 后缀规则 | 未提 | **主动引 "CP 域 Assumptions 规则 5"** "CPTEST 必须加 Sub 后缀" | 与 CO-4 §CP "子集用 'Sub' 后缀" 一致, 并反查到 KB CP assumptions (02 文件) |
| 源路径 | aggregated 02 | `knowledge_base/domains/CP/spec.md` | 与 CO-4 §CP "KB `knowledge_base/domains/CP/spec.md`" 一致 |

**Verdict**: **PASS 完全生效** — CO-4 正向锚 (3 变量列) + 反向锚 (SUPPCP 拒) + 深度内化 (Sub 后缀规则主动引) 三重命中.

---

## 独立 KB grep 核 (Rule A sample=Q2)

- `knowledge_base/domains/CP/spec.md` 独立 grep 证 CPSBMRKS / CPCELSTA / CPCSMRKS (reviewer 23 已核)
- CT C181172 CPCELSTA: reviewer 23 已核
- CPTEST "Sub" 后缀规则: reviewer 23 已核 KB `domains/CP/assumptions.md` 规则 5 存在

**Rule A verdict**: 变量命名层真实, 深度内化 assumptions 规则.
