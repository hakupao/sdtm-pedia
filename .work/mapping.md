# 源文件 → 输出文件映射

> 记录每个输出文件的数据来源，用于追溯和验证

## xlsx → md（自动生成）

| 源文件 | 输出 | 方式 |
|--------|------|------|
| `SDTMIG_v3.4.xlsx` → Variables sheet | `domains/*/spec.md` (63 个) | Python + openpyxl |
| `SDTM Terminology.xlsx` | `terminology/core/*.md` | Python + openpyxl |
| `SDTM Terminology.xlsx` | `terminology/questionnaires/*.md` | Python + openpyxl |
| `SDTM Terminology.xlsx` | `terminology/supplementary/*.md` | Python + openpyxl |

## PDF → md（LLM 提取）

| 源文件 | 页码范围 | 输出 |
|--------|---------|------|
| `SDTMIG v3.4.pdf` | 各 domain 对应页 | `domains/*/assumptions.md` |
| `SDTMIG v3.4.pdf` | 各 domain 对应页 | `domains/*/examples.md` |
| `SDTMIG v3.4.pdf` | p7-10 | `chapters/ch01_introduction.md` |
| `SDTMIG v3.4.pdf` | p11-16 | `chapters/ch02_fundamentals.md` |
| `SDTMIG v3.4.pdf` | p17-21 | `chapters/ch03_submitting_data.md` |
| `SDTMIG v3.4.pdf` | p22-59 | `chapters/ch04_general_assumptions.md` |
| `SDTMIG v3.4.pdf` | p427-440 | `chapters/ch08_relationships.md` |
| `SDTMIG v3.4.pdf` | p444+ | `chapters/ch10_appendices.md` |
| `SDTM_v2.0.pdf` | 全文 74 页 | `model/*.md` (6 个) |

## 详细页码映射

> 由 `.work/page_index.json` 提供每个 domain 的精确页码（Phase 2 已完成）
>
> 格式：`{"AE": {"section": [134,142], "spec": [134,137], "assumptions": [137,140], "examples": [140,142]}, ...}`
>
> 63 个 domain 全部覆盖（7 verified, 3 partial, 53 estimated — Phase 3 执行时逐个校正）

## 当前完成状态

| 来源 | 输出类型 | 完成数 | 状态 |
|------|---------|--------|------|
| xlsx → spec.md | `domains/*/spec.md` | 63/63 | **已完成** |
| xlsx → terminology | `terminology/**/*.md` | 91 文件 | **已完成** |
| PDF → assumptions.md | `domains/*/assumptions.md` | 63/63 | **已完成** |
| PDF → examples.md | `domains/*/examples.md` | 63/63 | **已完成** |
| PDF → chapters | `chapters/*.md` | 6/6 | **已完成** |
| PDF → model | `model/*.md` | 6/6 | **已完成** |
| 全局索引 | `INDEX.md` | 1/1 | **已完成** |
