<!-- chain: D (溯源链)
  修改本文件后，必须检查:
  → ../docs/TRACEABILITY.md               (溯源矩阵)
  → meta/worklog.md                  (工作日志)
-->

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

> 由 `.work/02_indexing/page_index.json` 提供每个 domain 的精确页码（Phase 2 已完成）
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

## Tier B 内容补修 (2026-11; 没有新的源文件)

> 源文件不变 (`SDTMIG v3.4.pdf` / `SDTM_v2.0.pdf` / 两份 xlsx). 这一轮是把已有产出对 PDF 原页逐原子核对后补修, 相对标签 `kb-2026.11.25` 改了 `knowledge_base/` 下 193 个文件 (domains 181 / chapters 6 / model 6).

| 新增的溯源材料 | 位置 | 内容 |
|---|---|---|
| PDF 原子 → KB 的终态标签 | `.work/10_tier_b_repair/work/coverage_ledger.wc.jsonl` | 12492 行; 每个 PDF 原子一个终态 (逐字有 / 等价 / 有意不收 / 原子抽错 / PDF 笔误 / 图暂缓) 与判定依据 |
| PDF 自身笔误登记 | `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` | 274 行; PDF 页、KB 文件:行、PDF 写法、KB 写法、处理 (KB 写正确值 195 / 照录 79) 与依据 |
| 各批改了哪些文件、依据哪几页 | `.work/10_tier_b_repair/evidence/checkpoints/t2_B-*.md` / `t2_S-*.md` / `t4_thaw_*.md` | 60 个修复批 + 22 个扫描批 + T4 解冻轮, 每批 writer / reviewer / auditor 三份 |
| KB 标题与节的变动 (给下游) | `.work/10_tier_b_repair/evidence/checkpoints/t4_downstream_notes.md`; `.work/10_tier_b_repair/work/t4/kb_heading_diff_kb-2026.11.25_HEAD.txt` | 移走 / 改名的节, CT 单元格格式约定, model 文件 6 列定义行 |

页码映射 (`.work/02_indexing/page_index.json`) 没有改.
