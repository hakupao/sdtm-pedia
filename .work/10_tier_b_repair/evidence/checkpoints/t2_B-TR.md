# T2 B-TR writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `97e18955346a42d29b1528c78d1d4b8d332d8137`
- md5 before: TR/assumptions.md `c4f681f0e281e9eb2ac41e5219ba2c79`; TR/examples.md `839fba93ff923ec68838f10a35942ef8`
- md5 after: TR/assumptions.md `c4f681f0e281e9eb2ac41e5219ba2c79` (未动); TR/examples.md `415debd69c524ff5ee855b89f4f44df4`
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-TR_writer/` (manifest.json, census_before/after.json, build_ex3.py, apply.py, p355-358 渲染图 110dpi)
- 数据来源: Ex2 逐格对照 p355/p356 渲染图 + `pdftotext -layout`; Ex3 整表按 p356-358 渲染图逐行手录 (build_ex3.py), 再由 census (bbox) 复核. 行号: Ex2 未变 (原地改格); Ex3 表 :68-101 (32 行), 新增 relrec :103-110.

### 变更清单 (atoms 19/19)

| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | TR/examples.md:17 | ig34_p0355_a002 | REPLACED | 表头 TREASND → TRREASND | 355 |
| 2 | TR/examples.md:25 | ig34_p0355_a009 | REPLACED | 行 7 TRDY -2 → -3 | 355 |
| 3 | TR/examples.md:26 | ig34_p0355_a010 | REPLACED | 行 8 TRDY 空 → -2 | 355 |
| 4 | TR/examples.md:30 | ig34_p0355_a014 | SKIPPED_PDF_TYPO | Row/TRSEQ 12 (PDF 13); 其余格一致. T-1 | 355 |
| 5 | TR/examples.md:31 | ig34_p0355_a015 | SKIPPED_PDF_TYPO | Row/TRSEQ 13 (PDF 14); 其余格一致. T-1 | 355 |
| 6 | TR/examples.md:32 | ig34_p0355_a016 | REPLACED (+T-1) | VISIT 空/TRDTC "WEEK 6" 列错位 → VISIT WEEK 6, TRDTC 空; Row/TRSEQ 保留 | 355 |
| 7 | TR/examples.md:33 | ig34_p0355_a017 | REPLACED (+T-1) | 同上列错位; TRTEST Non-Lymph → Non Lymph | 355 |
| 8 | TR/examples.md:34 | ig34_p0355_a018 | REPLACED (+T-1) | 列错位修正 (LNSTATE) | 355 |
| 9 | TR/examples.md:35 | ig34_p0355_a019 | REPLACED (+T-1) | 列错位修正 (ACNSD) | 355 |
| 10 | TR/examples.md:36 | ig34_p0355_a020 | REPLACED (+T-1) | 列错位修正 (PCBSD) | 355 |
| 11 | TR/examples.md:37 | ig34_p0355_a021 | REPLACED (+T-1) | 列错位修正 (PCNSD) | 355 |
| 12 | TR/examples.md:38 | ig34_p0355_a022 | SKIPPED_PDF_TYPO | 仅 Row/TRSEQ 偏 1. T-1 | 355 |
| 13 | TR/examples.md:39 | ig34_p0355_a023 | SKIPPED_PDF_TYPO | 仅 Row/TRSEQ 偏 1. T-1 | 355 |
| 14 | TR/examples.md:40 | ig34_p0355_a024 | SKIPPED_PDF_TYPO | 仅 Row/TRSEQ 偏 1. T-1 | 355 |
| 15 | TR/examples.md:41 | ig34_p0355_a025 | SKIPPED_PDF_TYPO | 仅 Row/TRSEQ 偏 1. T-1 | 355 |
| 16 | TR/examples.md:42 | ig34_p0355_a026 | REPLACED (+T-1) | T03 NOT DONE 行多填 TRDTC 2010-04-02 → 空 (PDF 无日期) | 355 |
| 17 | TR/examples.md:43 | ig34_p0355_a027 | REPLACED (+T-1) | TRREASND "NOT ASSESSABLE: IMAGE OBSCURED TUMOR" → "NOT ASSESSABLE: POOR IMAGE QUALITY" (跨页 p355→p356 顶) | 355-356 |
| 18 | TR/examples.md:44 | ig34_p0356_a001 | REPLACED (+T-1) | NT01 TRSTAT NOT DONE / TRREASND "POOR IMAGE INEQUALITY" → 均空 (PDF 该行仅 CT SCAN…日期 88) | 356 |
| 19 | TR/examples.md:45 | ig34_p0356_a002 | SKIPPED_PDF_TYPO | 仅 Row/TRSEQ 偏 1 (KB 27 / PDF 28). T-1 | 356 |

"9 条真 KB 错" 对应 #6-11, #16-18 (与 lane D 记录一致).

### census 表处理

| census ref (before 行号) | 处理 | 结果 |
|---|---|---|
| TR/examples.md:17 Ex2 tr.xpt (55 diffs) | 表头 + 原子 #1-19; 另 census-only: :21 行 3 TRDTC 2010-01-01→2010-01-02, TRDY -3→-2; :24 行 6 TRTEST Non-Lymph→Non Lymph | DIFF 32 残留 = 16 行 × (Row, TRSEQ), 全为 T-1 |
| TR/examples.md:68 Ex3 tr.xpt (90 diffs, PDF 32 行 / KB 28 行) | TABLE_REBUILT: 表头按 PDF 列序 (TRNAM 在 TRMETHOD 前, 互换); 32 行按 p356-358 重录. 主要差: KB 缺行 19 NEW 组 / 31-32 (R1-NEW01/02 EQUIVOCAL/UNEQUIVOCAL) / 29-30; KB 行 20 (R1-NEW01 DIAMETER, TRDY 55) PDF 无; 行 6/7/9 日期; 行 20-22 A3 值; 行 27-28 (-26 / 48); TRTEST 文字 (Non Lymph, From Nadir, Change Baseline in Sum of Diam) | DIFF 1 残留 = :84 TRSTRESC (T-2) |
| pdf_only p358 Ex3 relrec.xpt (2 行) | 补 PDF 引句 "The relationship between the TU and TR records…" + `**relrec.xpt**` + 2 行 (:103-110) | OK |
| TR/assumptions.md:15 UNPARSEABLE | 未触碰 | — |

- 汇总 (本批 2 文件, 命令见下): before `OK 1 / DIFF 2 / UNPARSEABLE 1, cells 1281, diffs 145, 本批页 TR PDF_ONLY 1` → after `OK 2 / DIFF 2 / UNPARSEABLE 1, cells 1389, diffs 33 (全为登记 PDF_TYPO), 本批页 TR PDF_ONLY 0`. 剩余 pdf_range 内 PDF_ONLY 均为 TU 表 (p353-354, p356 tu.xpt/supptu.xpt; 非本批文件).

```
S=<scratch>; python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-TR.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
python3 tools/check_links.py | tail -1   # live docs: 42 (基线 42)
```

### 新增 atom 清单 (census-only / R3)
- N-1 TR/examples.md:21 Ex2 行 3 TRDTC/TRDY (census).
- N-2 TR/examples.md:24 Ex2 行 6 TRTEST (census).
- N-3 TR/examples.md:68-101 Ex3 整表重建 (census DIFF, 不在 atoms).
- N-4 TR/examples.md:103-110 Ex3 RELREC 引句 + 表 (pdf_only p358).

### 删除清单
- 无 D2 删除. 仅 VALUE_DIFF 旧值替换; Ex3 表整表按 PDF 重录 (规则 3 "表格跟 PDF 走"), 旧 KB 行 20 (R1-NEW01 DIAMETER 7mm WEEK 6, TRDY 55) 在 PDF 中无对应, 随重建消失 — reviewer 请确认.

### PDF_TYPO 清单 (KB 保留合理值)

| # | 位置 | PDF | KB (保留) | 理由 |
|---|---|---|---|---|
| T-1 | TR/examples.md:30-45 Ex2 Row 与 TRSEQ (16 行 × 2 格) | 跳 12: 1-11, 13-28 (Row 与 TRSEQ 同跳) | 连续 1-27 | PDF 自身叙述 "Rows 9-21 / 22-27" 与连续编号一致; 共 27 行 |
| T-2 | TR/examples.md:84 Ex3 行 15 PCBSD TRSTRESC | -60 | -50 | 同行 TRORRES -50 / TRSTRESN -50, PDF 行内自相矛盾 |
| T-3 | TR/examples.md:43 Ex2 行 25 TRREASND (随 #17 写入) | 文本层 "POOR IMAGEQUALITY" (bbox 单词 IMAGEQUALITY) | "POOR IMAGE QUALITY" | PDF 缺空格; census 归一后不报 diff |

| T-4 (候选, 已按 PDF 写入) | TR/examples.md:44 Ex2 行 26 (PDF 行 27) NT01 TUMSTATE | TRORRES/TRSTAT/TRREASND 全空, 但有 CT SCAN / 2010-04-02 / 88 | 改前 KB: TRSTAT NOT DONE + TRREASND "POOR IMAGE INEQUALITY"; 现已清空 | 无结果又无 NOT DONE 的行在 SDTM 上不自洽, 疑 PDF 漏填; 但 T1 (lane_D reason) 明确判 PDF 该两格为空, KB 旧值 "INEQUALITY" 亦为错拼, 无"合理值"可保留 → 照 PDF; **需主控裁**: 若改判 PDF_TYPO, 可恢复 TRSTAT=NOT DONE |

### KB_AUTHORED (保留, 纯导航不矛盾)
- :3 "Note: TU and TR share examples. See also [TU Examples]…"; :5 / :56 标题 "(continued from TU)".

### 范围外发现
- 无. (Ex3 行 28 PCNSD 48% 等数值语义可疑但 PDF 明载, 已照录, 未登记为 typo.)

### 触碰过的 unparseable 表
- 无 (TR/assumptions.md:15 未动).

### git diff --stat -- kb_files
```
 knowledge_base/domains/TR/examples.md | 101 +++++++++++++++++++---------------
 1 file changed, 57 insertions(+), 44 deletions(-)
```
