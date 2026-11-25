# T1 全量只读 census (Q9 扩展) — table_census v2

<!-- chain: E (plans) -->
> 状态: **已完成** (2026-11-26); 执行: `oh-my-claudecode:executor` (opus); 只读 (KB / archive / releases 未动; 真 KB md5 `5ae88550…` 前后一致, 见 `t0_mutation_v3.log`).
> 输出: `work/census_full.json` (md5 `18ab44d611a723a2f1b2551af3f0856c`), manifest `work/census_full_manifest.json`. 本文件只含计数、位置与少量单元格值, 无 PDF 原文段落.
> 生成: `python3 -I .work/10_tier_b_repair/scripts/helpers/census_md.py`.

## 0. 复跑

```bash
cd /Volumes/DevSSD/Project/sdtm-pedia
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest .work/10_tier_b_repair/work/census_full_manifest.json \
  --out .work/10_tier_b_repair/work/census_full.json      # 首次运行生成 work/pdf_bbox/ (gitignored); exit 1 = 有 DIFF (预期)
python3 -I .work/10_tier_b_repair/scripts/helpers/fp_sample.py   # §1 误报抽样 (seed 20261126)
```

范围: `domains/*/examples.md` + `domains/*/assumptions.md` (63 域; DI 无页码且无表) + `chapters/*.md` (6) + `model/*.md` (6) = 138 文件.
页码取 `.work/02_indexing/page_index.json` (域 = section/spec/assumptions/examples 并集), 配对容差 ±3 页 (例: TM 的 page_index 写 p417, 表实在 p415).
整本 PDF (ig34 461 页 / sv20 74 页) 一次解析, PDF_ONLY 全局计算 (避免按单元跑时邻域表的假 PDF_ONLY).

## 1. 总计

| 项 | 数 |
|---|--:|
| KB 表 (markdown) | 504 |
| 可机检 (Row 列) | 354 = OK 220 + DIFF 130 + NO_PDF 4 (其中 KB 重复副本 26) |
| 不可机检 (UNPARSEABLE: 无 Row 列, 多为 chapter/model/assumptions 的说明/变量表) | 150 张 / 1184 行 → 被 T2 触碰时 reviewer 人工逐格 |
| 比对单元格 | 32076 |
| diff 条目 | 1763 = CELL 1687 + HEADER 43 + ROW_SHAPE 11 + PDF 行缺 21 + KB 行多 1 |
| 有 CELL diff 的 KB 行 | 507 |
| PDF_ONLY (KB 缺整表) | 15 |
| PDF_UNPARSED (垂直居中, 人工逐格) | 2 |

误报抽检: 随机 20 条 CELL diff (`fp_sample.py`, seed 20261126; 输出 `scripts/helpers/fp_sample.txt`).
7 条回 PDF (版面文本 + 词框) 直接核对, 全是真差异: AE:96 AEENDTC (PDF 2018, KB 2013), DM:11 RFXSTDTC, OE:15 OEMETHOD (KB 多 BIOMICROSCOPY),
DS:346 TESTRL (KB 多 "is"), EG:29 EGDTC (KB 2003-04-36), MB:154 MBSPCCND (KB 表头列名不符致空), TR:97 TRTEST (PDF 自身截成 "Diam" → PDF_TYPO 候选);
其余 13 条落在 lane 笔记已判错的表 (PP Ex1 用了 Ex3 数据 ×5, GF Ex1/Ex3 ×6, LB Ex1 ×2), 未逐格复核, 不计入误报率.
直接核对 7 条误报 0 (样本小; 误报率只能说未见, 不给区间).
已知"真但未必要改"的 diff: TR Ex2 PDF 跳 Row 12, KB 连续编号 → `Row` 列 16 条差异 (PDF_TYPO 候选); 折行连接歧义按相等计的格 (ws_only) 36.

## 2. 每文件

| 文件 | 表 | OK | DIFF | NO_PDF | 不可机检 (行) | 比对格 | diff 条目 |
|---|--:|--:|--:|--:|--:|--:|--:|
| chapters/ch01_introduction.md | 3 | 0 | 0 | 0 | 3 (20) | 0 | 0 |
| chapters/ch02_fundamentals.md | 4 | 0 | 0 | 0 | 4 (32) | 0 | 0 |
| chapters/ch03_submitting_data.md | 1 | 0 | 0 | 0 | 1 (63) | 0 | 0 |
| chapters/ch04_general_assumptions.md | 53 | 14 | 6 | 0 | 33 (142) | 1006 | 33 |
| chapters/ch08_relationships.md | 15 | 9 | 1 | 0 | 5 (34) | 442 | 11 |
| chapters/ch10_appendices.md | 5 | 0 | 0 | 0 | 5 (183) | 0 | 0 |
| domains/AE/assumptions.md | 1 | 0 | 0 | 0 | 1 (1) | 0 | 0 |
| domains/AE/examples.md | 6 | 0 | 6 | 0 | 0 (0) | 349 | 77 |
| domains/AG/examples.md | 6 | 6 | 0 | 0 | 0 (0) | 174 | 0 |
| domains/BE/examples.md | 9 | 5 | 4 | 0 | 0 (0) | 625 | 8 |
| domains/BS/examples.md | 1 | 0 | 1 | 0 | 0 (0) | 84 | 7 |
| domains/CE/assumptions.md | 1 | 0 | 0 | 0 | 1 (4) | 0 | 0 |
| domains/CE/examples.md | 11 | 7 | 1 | 0 | 3 (18) | 322 | 1 |
| domains/CM/examples.md | 5 | 4 | 1 | 0 | 0 (0) | 310 | 2 |
| domains/CO/examples.md | 1 | 0 | 1 | 0 | 0 (0) | 120 | 2 |
| domains/CP/examples.md | 2 | 0 | 2 | 0 | 0 (0) | 387 | 65 |
| domains/CV/examples.md | 2 | 1 | 1 | 0 | 0 (0) | 219 | 3 |
| domains/DA/examples.md | 3 | 2 | 1 | 0 | 0 (0) | 250 | 8 |
| domains/DD/examples.md | 5 | 5 | 0 | 0 | 0 (0) | 147 | 0 |
| domains/DM/examples.md | 15 | 11 | 2 | 0 | 2 (20) | 645 | 11 |
| domains/DS/examples.md | 21 | 10 | 11 | 0 | 0 (0) | 1434 | 54 |
| domains/DV/examples.md | 1 | 0 | 1 | 0 | 0 (0) | 36 | 1 |
| domains/EC/examples.md | 7 | 4 | 2 | 0 | 1 (5) | 546 | 17 |
| domains/EG/examples.md | 4 | 1 | 3 | 0 | 0 (0) | 1118 | 67 |
| domains/EX/examples.md | 31 | 15 | 5 | 0 | 11 (44) | 1758 | 93 |
| domains/FA/examples.md | 24 | 12 | 3 | 0 | 9 (43) | 1169 | 13 |
| domains/FT/examples.md | 2 | 2 | 0 | 0 | 0 (0) | 113 | 0 |
| domains/GF/examples.md | 10 | 6 | 4 | 0 | 0 (0) | 1192 | 339 |
| domains/HO/examples.md | 4 | 2 | 2 | 0 | 0 (0) | 318 | 2 |
| domains/IE/examples.md | 1 | 1 | 0 | 0 | 0 (0) | 64 | 0 |
| domains/IS/examples.md | 13 | 5 | 8 | 0 | 0 (0) | 1464 | 91 |
| domains/LB/examples.md | 4 | 1 | 3 | 0 | 0 (0) | 275 | 116 |
| domains/MB/examples.md | 24 | 13 | 11 | 0 | 0 (0) | 1798 | 89 |
| domains/MH/assumptions.md | 1 | 0 | 0 | 0 | 1 (4) | 0 | 0 |
| domains/MH/examples.md | 5 | 0 | 5 | 0 | 0 (0) | 444 | 24 |
| domains/MI/examples.md | 5 | 4 | 1 | 0 | 0 (0) | 208 | 1 |
| domains/MK/examples.md | 2 | 1 | 1 | 0 | 0 (0) | 608 | 6 |
| domains/ML/examples.md | 5 | 1 | 1 | 0 | 3 (9) | 189 | 1 |
| domains/MS/examples.md | 4 | 2 | 2 | 0 | 0 (0) | 530 | 68 |
| domains/NV/examples.md | 4 | 3 | 1 | 0 | 0 (0) | 478 | 4 |
| domains/OE/examples.md | 11 | 4 | 7 | 0 | 0 (0) | 637 | 14 |
| domains/OI/examples.md | 1 | 1 | 0 | 0 | 0 (0) | 112 | 0 |
| domains/PC/assumptions.md | 3 | 1 | 2 | 0 | 0 (0) | 952 | 36 |
| domains/PC/examples.md | 14 | 11 | 3 | 0 | 0 (0) | 2064 | 4 |
| domains/PE/examples.md | 1 | 1 | 0 | 0 | 0 (0) | 108 | 0 |
| domains/PP/examples.md | 7 | 1 | 3 | 2 | 1 (4) | 1096 | 271 |
| domains/PR/examples.md | 5 | 5 | 0 | 0 | 0 (0) | 143 | 0 |
| domains/QS/examples.md | 1 | 0 | 1 | 0 | 0 (0) | 150 | 2 |
| domains/RE/examples.md | 6 | 5 | 1 | 0 | 0 (0) | 216 | 5 |
| domains/RELREC/examples.md | 4 | 4 | 0 | 0 | 0 (0) | 136 | 0 |
| domains/RELSPEC/examples.md | 1 | 1 | 0 | 0 | 0 (0) | 42 | 0 |
| domains/RELSUB/examples.md | 2 | 2 | 0 | 0 | 0 (0) | 54 | 0 |
| domains/RP/examples.md | 1 | 0 | 1 | 0 | 0 (0) | 399 | 7 |
| domains/RS/examples.md | 4 | 3 | 1 | 0 | 0 (0) | 547 | 6 |
| domains/SC/examples.md | 3 | 2 | 0 | 1 | 0 (0) | 146 | 0 |
| domains/SE/examples.md | 4 | 2 | 2 | 0 | 0 (0) | 244 | 2 |
| domains/SM/examples.md | 3 | 0 | 3 | 0 | 0 (0) | 100 | 5 |
| domains/SR/examples.md | 7 | 3 | 4 | 0 | 0 (0) | 641 | 21 |
| domains/SS/examples.md | 1 | 1 | 0 | 0 | 0 (0) | 60 | 0 |
| domains/SU/examples.md | 1 | 1 | 0 | 0 | 0 (0) | 126 | 0 |
| domains/SUPPQUAL/examples.md | 2 | 0 | 1 | 1 | 0 (0) | 22 | 3 |
| domains/SV/examples.md | 3 | 2 | 1 | 0 | 0 (0) | 397 | 1 |
| domains/TA/assumptions.md | 1 | 0 | 0 | 0 | 1 (9) | 0 | 0 |
| domains/TA/examples.md | 14 | 7 | 0 | 0 | 7 (18) | 1221 | 0 |
| domains/TD/examples.md | 3 | 2 | 1 | 0 | 0 (0) | 80 | 1 |
| domains/TE/examples.md | 4 | 3 | 0 | 0 | 1 (3) | 128 | 0 |
| domains/TI/examples.md | 1 | 1 | 0 | 0 | 0 (0) | 42 | 0 |
| domains/TM/examples.md | 1 | 1 | 0 | 0 | 0 (0) | 12 | 0 |
| domains/TR/assumptions.md | 1 | 0 | 0 | 0 | 1 (1) | 0 | 0 |
| domains/TR/examples.md | 3 | 1 | 2 | 0 | 0 (0) | 1281 | 145 |
| domains/TS/assumptions.md | 2 | 0 | 0 | 0 | 2 (19) | 0 | 0 |
| domains/TS/examples.md | 4 | 2 | 2 | 0 | 0 (0) | 1104 | 3 |
| domains/TU/assumptions.md | 6 | 0 | 0 | 0 | 6 (27) | 0 | 0 |
| domains/TU/examples.md | 5 | 2 | 3 | 0 | 0 (0) | 470 | 13 |
| domains/TV/examples.md | 2 | 2 | 0 | 0 | 0 (0) | 60 | 0 |
| domains/UR/examples.md | 2 | 2 | 0 | 0 | 0 (0) | 139 | 0 |
| domains/VS/examples.md | 1 | 0 | 1 | 0 | 0 (0) | 325 | 10 |
| model/01_concepts_and_terms.md | 2 | 0 | 0 | 0 | 2 (16) | 0 | 0 |
| model/02_observation_classes.md | 16 | 0 | 0 | 0 | 16 (183) | 0 | 0 |
| model/03_special_purpose_domains.md | 7 | 0 | 0 | 0 | 7 (110) | 0 | 0 |
| model/04_associated_persons.md | 1 | 0 | 0 | 0 | 1 (4) | 0 | 0 |
| model/05_study_level_data.md | 13 | 0 | 0 | 0 | 13 (110) | 0 | 0 |
| model/06_relationship_datasets.md | 9 | 0 | 0 | 0 | 9 (58) | 0 | 0 |

无表文件 (55): domains/AG/assumptions.md, domains/BE/assumptions.md, domains/BS/assumptions.md, domains/CM/assumptions.md, domains/CO/assumptions.md, domains/CP/assumptions.md, domains/CV/assumptions.md, domains/DA/assumptions.md, domains/DD/assumptions.md, domains/DM/assumptions.md, domains/DS/assumptions.md, domains/DV/assumptions.md, domains/EC/assumptions.md, domains/EG/assumptions.md, domains/EX/assumptions.md, domains/FA/assumptions.md, domains/FT/assumptions.md, domains/GF/assumptions.md, domains/HO/assumptions.md, domains/IE/assumptions.md, domains/IS/assumptions.md, domains/LB/assumptions.md, domains/MB/assumptions.md, domains/MI/assumptions.md, domains/MK/assumptions.md, domains/ML/assumptions.md, domains/MS/assumptions.md, domains/NV/assumptions.md, domains/OE/assumptions.md, domains/OI/assumptions.md, domains/PE/assumptions.md, domains/PP/assumptions.md, domains/PR/assumptions.md, domains/QS/assumptions.md, domains/RE/assumptions.md, domains/RELREC/assumptions.md, domains/RELSPEC/assumptions.md, domains/RELSUB/assumptions.md, domains/RP/assumptions.md, domains/RS/assumptions.md, domains/SC/assumptions.md, domains/SE/assumptions.md, domains/SM/assumptions.md, domains/SR/assumptions.md, domains/SS/assumptions.md, domains/SU/assumptions.md, domains/SUPPQUAL/assumptions.md, domains/SV/assumptions.md, domains/TD/assumptions.md, domains/TE/assumptions.md, domains/TI/assumptions.md, domains/TM/assumptions.md, domains/TV/assumptions.md, domains/UR/assumptions.md, domains/VS/assumptions.md

## 3. PDF_ONLY (KB 没有对应表)

| PDF 页 | 节 | Example | 数据集 | 行数 |
|---|---|---|---|--:|
| 211,212 | 6.3.5.3 | 2 | cp.xpt | 11 |
| 213 | 6.3.5.3 | 3 | cp.xpt | 12 |
| 214 | 6.3.5.3 | 4 | cp.xpt | 7 |
| 215 | 6.3.5.3 | 5 | cp.xpt | 8 |
| 216,217 | 6.3.5.3 | 6 | cp.xpt | 32 |
| 218 | 6.3.5.3 | 7 | cp.xpt | 3 |
| 219 | 6.3.5.3 | 8 | cp.xpt | 11 |
| 247 | 6.3.5.6 | 1 | lb.xpt | 18 |
| 263 | 6.3.5.7.3 | 3 | di.xpt | 2 |
| 263 | 6.3.5.7.3 | 3 | relrec.xpt | 6 |
| 270,271 | 6.3.5.9.1 | 1 | pc.xpt | 32 |
| 274 | 6.3.5.9.2 | 2 | None | 7 |
| 305 | 6.3.7.5 | 4 | ae.xpt | 3 |
| 358 | 6.3.12.3 | 3 | relrec.xpt | 2 |
| 407 | 7.2.2.1 | None | special.xpt | 4 |

## 4. NO_PDF (KB 表找不到 PDF 对应) / PDF_UNPARSED (人工逐格)

| KB 表 | Example | 数据集 | 行数 |
|---|---|---|--:|
| domains/PP/examples.md:47 | 1 | supppp.xpt | 7 |
| domains/PP/examples.md:68 | 2 | pp.xpt | 7 |
| domains/SC/examples.md:34 | 2 | sc.xpt | 3 |
| domains/SUPPQUAL/examples.md:22 | 2 | suppqs.xpt | 4 |

| PDF 页 | Example | 数据集 | 原因 | 行数 |
|---|---|---|---|--:|
| 274 | 2 | pp.xpt | vertically centred cells | 7 |
| 342 | 2 | sc.xpt | vertically centred cells | 3 |

## 5. 与 v1 的关系

- B-PCPP (p275-284): v2 复现 v1 全部 42 处 DIFF (按表+行对照 0 丢失), 粒度细到格 (54 条); v1 的 13 张 OK 表 v2 仍 OK.
- EG / CP / TR / MB 四个 T1 单元: v1 的 DIFF 行 v2 全部保留; 表面"丢失"的 3 处均为表达方式变化 — TR Ex2 v1 的 row 28 "KB 缺行" 现为
  行号对齐 (KB 12-27 ↔ PDF 13-28, `Row` 列 diff); MB:162 v1 的 row 7/8 缺行现为 KB 5/6 ↔ PDF 7/8 行号 diff; MB:229 由 DIFF 变 OK (v1 误配 Ex3 relrec, 见 `t0_mutation.md` §6).
