# T2 B-RP writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `f22fe6027a04c5efe09c7885f6d472b913bf3b42` (RP 文件工作树改前无未提交改动)
- md5: RP/examples.md before `e01f7635ad3ead455e314aeb414d5724` → after `b4370bb4475a860bacd9ea907c61130c` (31 行, 行数不变); RP/assumptions.md (白名单外, 未动) `95163e5207f2173bf8991c29682fce02`
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-RP_writer/` (examples.before.md, p-307.png 150dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 1 (REAL_GAP) / t2_recheck 0; census DIFF 1 表 (7 CELL) 全部处理; pdf_only 0; unparseable 0; out_of_scope 0.
- pdf_ranges 覆盖核 (O20): RP 节 = p305 "6.3.7.6" 起 (Description/Overview + Spec 表) → p306 (Spec 表续 + Assumptions 1-3) → p307 (Assumption 3a/4 + Examples Ex1); p308 起为 6.3.7.7 RE. B-RP.json lo/hi = 305-307 **完整覆盖**; RP 只有 Example 1.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | RP/examples.md:21 | census:9 r11 RPDTC | REPLACED | 2008-04-29 → 2008-04-16 (与 r10 同访视 Day 29) | 307 |
| 2 | :22 | census:9 r12 RPDTC | REPLACED | 2009-03-10 → 2009-03-09 | 307 |
| 3 | :23 | census:9 r13 RPDTC | REPLACED | 2009-03-10 → 2009-03-09 | 307 |
| 4 | :26 | census:9 r16 RPDTC | REPLACED | 2009-03-10 → 2009-03-09 | 307 |
| 5 | :27 | census:9 r17 RPDTC | REPLACED | 2009-03-10 → 2009-03-09 | 307 |
| 6 | :28 | census:9 r18 RPDTC | REPLACED | 2009-03-10 → 2009-03-09 | 307 |
| 7 | :29 | census:9 r19 RPDTC | REPLACED | 2009-03-10 → 2009-03-09 | 307 |
| 8 | — (目标 RP/assumptions.md, 白名单外) | ig34_p0305_a013 | SKIPPED_STRUCT | Description/Overview 句 ("A findings domain that contains physiological and morphological findings related to the male and female reproductive systems.") 缺; 应在 assumptions.md:1 后新增 `## RP – Description/Overview` (CM/IS 先例), 但 assumptions.md 不在 kb_files → 主控定 (追加白名单或交 O15/O16 全域扫描) | 305 |

- atoms 覆盖率自查: atoms 1 = 表中 atom 行 1 (#8). census 7 格 = #1-7.
- 一致性核 (非 PDF_TYPO 依据, 仅佐证): PDF 值自洽 — P0002 Day 1 = 2009-03-19, 筛选 RPDY -10 → 2009-03-09; P0001 Day 29 = 2008-04-16 (RPDY 29). KB 旧值与 RPDY 矛盾, 属 KB 错.

### census 表处理

| census ref | 处理 | 结果 |
|---|---|---|
| RP/examples.md:9 Ex1 rp.xpt (7 CELL, 行 21-23/26-29) | #1-7 | census_after: KB tables 1, OK 1, cells 399, diffs 0 |

### PDF_TYPO 清单
- 无. (PDF Ex1 筛选行 VISITDY=1 而 RPDY=-10, 看似不一致, 但 KB 与 PDF 一致, 不在 atoms/census, 未动; 仅记此观察, 不登记 T-n.)

### 预期 fp 回归 (PDF_TYPO 修正)
- 0 (无 PDF_TYPO 修正). fp_match 改后: p305-307 原子 EXACT 28 / INTENTIONAL_EXCLUDE 21 / EQUIVALENT 2 / a013 PARTIAL (hit_any 仅 terminology general_part4.md, 预期, 见 #8). 全量 regress 48 条, grep `p030[5-7]|RP/` = 0, 均为工作树中他批未提交改动 (§6.4.2 等), 非本批.

### 双向全扫 (含表格原子)
- 范围: p305 "6.3.7.6" 至 p307 页末 (RP 全节). examples.md 对应 p307 "RP – Examples" 起.
- PDF→KB (examples 段): "Example 1" 标题 → `## Example 1`; 引导句 → :5 逐字; "rp.xpt" → :7 `**rp.xpt**`; 表 21 行 × 19 列对 150dpi 渲染图逐格人工核, 表头/列序/列数/Row 列一致, 改后 0 差 (含 r1-r10/r14/r15/r20/r21 未改格).
- KB→PDF (examples.md 全文件): 标题 `# RP — Examples` (导航), :5 引导句, :7 标签, 表 — 全部在 PDF 有对应; 无 KB 自写解释性内容 (D6 无), 无伪节号.
- p305-307 非 examples 部分 (白名单外, 仅报告): assumptions.md 缺 Description/Overview (#8); spec 首句 (rp.xpt, … Tabulation.) 在 assumptions.md:5 **已存在**; Assumptions 1-4 + 3a 在 assumptions.md:9-16 存在 (:9 "subject's" 为直引号, PDF 为弯引号, 微差, 范围外); spec 表属 spec.md (本批未扫格, 不在 pdf_ranges 文件).

### 新增 atom 清单 (R3)
- 无 (examples 段无缺失叙述).

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | :21-23, :26-29 RPDTC 旧值 | 同行 | VALUE_DIFF 旧值替换 (#1-7) | — |

### 范围外发现
- F-1: RP/assumptions.md 缺 `## RP – Description/Overview` 节 + p305 原句 (= atom a013, T1 lane A "RP 缺 Description/Overview"). 需主控追加 assumptions.md 到白名单或归 O15/O16.
- F-2: RP/assumptions.md:9 "subject's" 直引号 vs PDF 弯引号 (低).

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-RP_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-RP.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # status OK 1, diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p030[5-7]|RP/' $S/fp_regress.jsonl   # 0
pdftoppm -f 307 -l 307 -r 150 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p
python3 tools/check_links.py | tail -1   # live docs: 42
```

### git diff --stat
```
 knowledge_base/domains/RP/examples.md | 14 +++++++-------
 1 file changed, 7 insertions(+), 7 deletions(-)
```

## attempt 1 续 (主控扩白名单: + RP/assumptions.md)

- RP/assumptions.md md5 `95163e5207f2173bf8991c29682fce02` → `9c1bbc6cecd1e8f1074b5dba2d119cba` (16 → 20 行); examples.md 不变 (`b4370bb4…`).

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 8' | RP/assumptions.md:3-5 | ig34_p0305_a013 | INSERTED | H1 后新增 `## RP – Description/Overview` + p305 原句逐字 (SC/CM 惯例); 取代上文 #8 SKIPPED_STRUCT | 305 |

- 双向全扫 (assumptions.md 全文 vs p305-307): PDF→KB: Description/Overview 句 (本次补)、spec 首句 (:9)、Assumptions 1/2/3/3a/4 (:13-20) 全部在; spec 表属 spec.md. KB→PDF: 脚本逐行归一 (空白/弯引号/"-- " 折行) 后子串核, 0 未命中; 无 KB 自写内容 / D6 / 伪节号. 直/弯引号按主控口径不改 (撤回上文 F-2).
- fp_match 重跑: ig34_p0305_a013 hit_target null → `RP/assumptions.md` (新增命中; verdict 字段为台账静态值 PARTIAL, 非本次判定); regress grep `p030[5-7]|RP/` = 0. check_links live docs 42.
- 复跑: `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after2.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress2.jsonl; grep ig34_p0305_a013 $S/fp_after2.jsonl` (S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-RP_writer)
- git diff --stat: examples.md 14 (+7/-7); assumptions.md +4.
