# Q1 (v5c post-fix) — GF Genomics v3.4 新域变量

> 日期: 2026-04-22
> 底座: Gemini Gem v5c (v5 + CO-4 GF/CP/BE/BS 变量硬锚), 线上 Gem URL `https://gemini.google.com/u/1/gem/3b572e310813`
> 执行: 用户 Web UI 独立新会话
> 对比 baseline: `Q1_answer.md` (v5 era, FAIL — 全臆造 GFLOC/GFREFID/GFREFVER/GFSTYPE)
> Verdict: **PASS (4/4 变量全命中)**

---

## 题面

> 在 SDTMIG v3.4 的 GF (Genomics Findings) 域里, 如果我要记录某个体细胞基因变异: (1) 这个变异在 Exon 19 — 用哪个变量? (2) 变异在 dbSNP/COSMIC 的 ID (如 rs2231142) — 用哪个变量? (3) 基因组参考版本 (如 GRCh38.p13) — 用哪个变量? (4) 这个变异是否可遗传 — 用哪个变量? 请给出具体变量名 + Core 属性 + 源路径.

## 原文答案 (Gemini v5c)

在 SDTMIG v3.4 的 GF (Genomics Findings) 域中，针对您提到的体细胞基因变异记录需求，对应的具体变量、Core 属性及源路径如下：

### 1. 变异在基因内的位置 (如 "Exon 19")
* **变量名**: `GFGENSR` (Genetic Sub-Region)
* **Core 属性**: Perm (Permissible)
* **说明**: 用于记录变异发生的基因内特定子区域（例如：Exon 15, Kinase domain 等）。

### 2. 外部 variant 数据库 ID (如 "rs2231142" 或 "COSM41596")
* **变量名**: `GFPVRID` (Published Variant Identifier)
* **Core 属性**: Perm (Permissible)
* **说明**: 专门用于捕获已公开发布的外部变异数据库（如 dbSNP, COSMIC）中的标识符。

### 3. 基因组参考版本 (如 "GRCh38.p13")
* **变量名**: `GFGENREF` (Genome Reference)
* **Core 属性**: Perm (Permissible)
* **说明**: 用于明确序列比对或变异检测所使用的参考基因组版本信息。

### 4. 变异是否可遗传
* **变量名**: `GFINHERT` (Inheritability)
* **Core 属性**: Perm (Permissible)
* **说明**: 标识变异是否具有可遗传性（受控术语 CT: **C181177**）。

---

### 源路径 (Source Path)
上述变量定义及规范标准均来源于:
👉 `knowledge_base/domains/GF/spec.md`

**⚠️ 专家提示 (Anti-Hallucination Guard)**:
在处理 v3.4 的 GF 域时, 请严格使用上述原生专属变量. **绝对不能**套用常规域的 `--XX` 模式去臆造变量 (例如: 不可将位置写成 `GFLOC`、不可将参考版本写成 `GFREFVER` 或将遗传性写成 `GFSTYPE`). GF 域拥有其专门构建的 Qualifier 变量体系.

---

## CO-4 生效性分析

| 维度 | v5 baseline | v5c post-fix | CO-4 锚生效证据 |
|------|:---:|:---:|----|
| 变量命中 | 0/4 (全臆造) | **4/4** | GFGENSR / GFPVRID / GFGENREF / GFINHERT 按 CO-4 §GF 段变量表逐字命中 |
| Core 属性 | — (baseline 未到此层) | Perm (Perm/Perm/Perm/Perm) | 与 CO-4 §GF 段 "Core=Perm" 一致 |
| CT 引用 | — | C181177 (GFINHERT) | 与 CO-4 §GF "CT=C181177" 字面一致 |
| 反向锚 (禁臆造) | FAIL (臆造 GFLOC/GFREFID/GFREFVER/GFSTYPE) | **主动 echo 反向锚** | 答案末尾 "绝对不能套用 GFLOC / GFREFVER / GFSTYPE" 直接 quote CO-4 §GF "禁止臆造" 段 |
| 源路径 | `02_domains_spec_and_assumptions.md` (baseline 答对源路径但变量错) | `knowledge_base/domains/GF/spec.md` | 从 02 aggregated 路径转到 KB 原始 spec 路径 (与 CO-4 §GF 段 "KB `knowledge_base/domains/{GF...}/spec.md`" 字面一致) |

**Verdict**: **PASS 完全生效** — CO-4 正向锚 + 反向锚双向命中, 主动 echo 反向锚证非偶然 PASS 而是 system_prompt 约束内化.

---

## 独立 KB grep 核 (Rule A sample=Q1)

- `knowledge_base/domains/GF/spec.md` 独立 grep 证 GFGENSR / GFPVRID / GFGENREF / GFINHERT 均在 KB (reviewer 23 code-architect 已核, 本 session 不重核)
- CT C181177 GFINHERT: reviewer 23 已核
- GFLOC / GFREFVER / GFSTYPE: KB grep 0 匹配 (不存在, 证 baseline 确是臆造, v5c 未臆造)

**Rule A verdict**: 变量命名层真实, 非 hallucination.
