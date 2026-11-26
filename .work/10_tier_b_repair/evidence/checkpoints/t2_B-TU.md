# T2 B-TU writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `f22fe6027a04c5efe09c7885f6d472b913bf3b42` (TU 两文件改前与 HEAD 一致, 工作树无 TU 改动)
- md5 TU/assumptions.md: before `12a44b1bb170203aabface0adbe77cdb` (106 行) → after `511b50ff9b11056d20a6b038516fc1e0` (116 行)
- md5 TU/examples.md: before `acf970626128034037671cf9c6ac03df` (96 行) → after `2e8e78afc707c4784e2e09a80b73e5cf` (98 行)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-TU_writer/`
  (before_root/ = 改前 KB 镜像, apply.py = 精确替换 + 命中次数断言 + 表列数断言, sent_scan.py = 双向逐句扫描, prose_scan.py = pdf_atoms 扫描,
  census_before/after.json, fp_before/after.jsonl, fp_regress.jsonl, p344-349/p353/p354/p356 110dpi 渲染)
- **页范围 (O20)**: `pdf_ranges` lo=344 已含 §6.3.12 节首 (p344 下半: §6.3.12 引言段 + §6.3.12.1 标题 + TU Description 起始), 无缺口.
  TU 部分实扫 p344 (§6.3.12 起)-p349 (TU assumptions 止) + p353-p356 (§6.3.12.3 共享例子中 TU 部分: Ex1 全部, Ex2 tu/supptu, Ex3 tu).
  p350-352 为 TR 节 (B-TR); p354 下半 / p355 / p356 上 / p356 下 / p357-358 的 TR 叙述 + tr.xpt + relrec.xpt 在 `TR/examples.md` (B-TR 已 PASS, :7/:47/:58/:103), 不复制进 TU.
  p345-346 spec 表行 + 脚注属 `TU/spec.md` (不在白名单).
- 本批 atoms 4 (VALUE_DIFF) / t2_recheck 0 / out_of_scope 0; census DIFF 3 表 (13 diffs) 全处理; pdf_only 0; unparseable 6 (其中 2 张已触碰, 见下).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | TU/examples.md:24 | ig34_p0353_a015 (census:19 r2 TUTESTCD) | REPLACED | VSIDENT → VSLIDENT (CT oncology_part2.md:69 C119569 同) | 353 |
| 2 | TU/examples.md:25 | ig34_p0353_a016 (census:19 r3 TUTEST) | REPLACED | "Limb Location Identification" → "Limb Lesion Identification" (CT C119568 同) | 353 |
| 3 | TU/examples.md:27 | ig34_p0353_a018 (census:19 r5 TUTESTCD) | REPLACED | VSIDENT → VSLIDENT | 353 |
| 4 | TU/examples.md:36 | ig34_p0354_a005 (census:31 r2 QNAM) | REPLACED | TUPAGAR → TUPAGA | 354 |
| 5 | TU/examples.md:90-91 | census:88 HEADER (TUDY) | TABLE_REBUILT | Ex3 tu.xpt 表头 TUDTC 后加 TUDY 列 + 分隔线 (PDF 列序) | 356 |
| 6 | TU/examples.md:92-98 | census:88 r1-r7 TUDY (×7) | REPLACED | 新列值 -2 / -3 / -3 / -3 / -2 / 48 / 88 (对 p356 渲染逐格); r4 行尾多余空格去掉 | 356 |
| 7 | TU/examples.md:96 | census:88 r5 TULAT | REPLACED | R1-NT02 CEREBELLUM: LEFT → RIGHT | 356 |
| 8 | TU/examples.md:3 | R3 N-1 (ig34_p0353_a005 HEADING) | INSERTED | `## §6.3.12.3 Tumor Identification/Tumor Results Examples` (MB/examples.md:3 共享例子先例; `## Example N` 未动) | 353 |
| 9 | TU/examples.md:13 | ig34_p0353_a009 (Rows 1-2) | SKIPPED_PDF_TYPO (T-1) | KB "aorto-iliac vessel" 保留; PDF 印 "aorta-iliac" | 353 |
| 10 | TU/assumptions.md:5 | R3 N-2 (ig34_p0344_a016 §6.3.12 引言段, 3 句) | INSERTED | `## 6.3.12` 标题下补 PDF 引言段, 逐字 (含 PDF 原样 "Disease Response and Clin Classification") | 344 |
| 11 | TU/assumptions.md:7 | R3 N-3 (ig34_p0344_a017 HEADING) | INSERTED | `## 6.3.12.1 Tumor/Lesion Identification (TU)` (与同文件 `## 6.3.12` 同层同写法) | 344 |
| 12 | TU/assumptions.md:21-23 | R3 N-4/N-5 (ig34_p0345_a005 HEADING + a006 spec 首句) | INSERTED | `## TU – Specification` + "tu.xpt, Tumor/Lesion Identification — Findings. One record per identified tumor per subject per assessor, Tabulation." (MB/SR 先例位置) | 345 |
| 13 | TU/assumptions.md:25 | R3 N-6 (p346 "TU – Assumptions" 标题) | INSERTED | `## TU – Assumptions` (item 1 前) | 346 |
| 14 | TU/assumptions.md:34 | R3 N-7 (ig34_p0347_a005; atom 文本有抽取错, 以渲染为准) | REPLACED (D2 删扩写, 删除清单 D-1) | 删 KB 多出的 "identified at baseline"; 按 PDF 把 "During the course…" 并回 TUTESTCD/TUTEST 段 (PDF 同一段, 同文件内归段) | 347 |
| 15 | TU/assumptions.md:52-54 | R3 N-8 (ig34_p0347_a023) | INSERTED | assumption 3 补 "This example represents tumors assessed by location of interest."; 按 PDF 分为第二段 (原句未删) | 347 |
| 16 | TU/assumptions.md:70 | R3 N-9 (ig34_p0348_a005, 6c) | REPLACED | "occurrence of a new tumor, its" → "new tumor/lesion, its" | 348 |
| 17 | TU/assumptions.md:92 | R3 N-10 (ig34_p0349_a001 区; unparseable 表 base:78) | REPLACED | METIND r3: "NOT DONE" 从 TUORRES 移到 TUSTAT (TUORRES 空), 对 p349 渲染 | 349 |
| 18 | TU/assumptions.md:100-105 | R3 N-11 (ig34_p0349_a011-a016; unparseable 表 base:88) | REPLACED | TUTESTCD DRCRLLTC → DRCRLTLC ×6 (CT oncology_part2.md:54 C123633 同) | 349 |
| 19 | TU/assumptions.md:105 | R3 N-12 (ig34_p0349_a016) | REPLACED | TUORRES "CONTRALATE RAL" → "CONTRALATERAL" (PDF 单元格折行, KB 误留空格) | 349 |

- atoms 覆盖率自查: atoms 4 → #1-#4 各一行 (4/4). census 13 diff 全在 #1-#7. writer.jsonl 共 27 行 (4 atom + 9 census 其余格 + 14 项 R3/PDF_TYPO/KB_AUTHORED). (trace 行 note 写 "R3 11" 为笔误, R3 实为 N-1..N-12, 以本文件为准.)

### census 表处理

| census ref (before 行号) | 处理 | 结果 (after) |
|---|---|---|
| examples:19 Ex1 tu.xpt (3 CELL) | #1-#3 | OK |
| examples:31 Ex1 supptu.xpt (1 CELL) | #4 | OK |
| examples:88 Ex3 tu.xpt (HEADER 1 + CELL 8) | #5-#7 | OK |
| assumptions:30 split 例表 (UNPARSEABLE, 9 行) | 未改; 对 p347 渲染逐格一致 | 不可机检 |
| assumptions:46 location-of-interest 表 (4 行) | 未改; 对 p347 渲染一致 (LOCATION OF INTEREST 为单元格折行合并) | 不可机检 |
| assumptions:70 NTIND/TIND 表 (3 行) | 未改; 对 p348 渲染一致 | 不可机检 |
| assumptions:78 METIND 表 (3 行) | **已触碰** #17 | reviewer 须对 p349 渲染人工逐格 |
| assumptions:88 disease recurrence 表 (6 行) | **已触碰** #18-#19 | reviewer 须对 p349 渲染人工逐格 |
| assumptions:99 SUPPTU QNAM 表 (2 行) | 未改; 对 p349 渲染一致 | 不可机检 |

- 汇总 (manifest = B-TU pdf_ranges): before `DIFF 3 / OK 2 / UNPARSEABLE 6, cells 470, diffs 13` → after `OK 5 / UNPARSEABLE 6, cells 477, diffs 0`. RESULT RED 来自 manifest 外 PDF_ONLY 334, 改前改后相同.

```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-TU_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-TU.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json      # before: 改前跑 → census_before.json
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline $S/fp_before.jsonl --regress-out $S/fp_regress.jsonl
python3 -I $S/sent_scan.py ; python3 -I $S/sent_scan.py $S/before_root/knowledge_base      # 双向逐句 (layout 文本 p344-349, p353-356)
python3 -I $S/prose_scan.py                                                                 # pdf_atoms 逐原子 (TU/§6.3.12 节)
python3 tools/check_links.py | tail -1      # live docs: 42 (基线 42)
```

### fp_match (全量, --baseline fp_before)
- hit_target 3863 → 3876; `regressions=0 new_hits=13`.
- 新命中: p0353_a015/a016/a018, p0354_a005, p0356_a015-a022 (Ex3 表头 + 7 行). 另 p0305_a013 也新命中 — 非本批 (p305 不在 TU 页; 并行他批改动所致, 不归因本批).
- 注意: fp 只覆盖 p344-349 的 15/132 原子 (ledger 子集), assumptions.md 的修复以 sent_scan / prose_scan 前后对比为证据.
- **预期 fp 回归清单**: 无 (本批唯一 PDF_TYPO T-1 为"保留 KB", p0353_a009 改前已不命中 → 持续不命中, 非回归).
- **预期持续不命中 (pdf_atoms 抽取错, 非 KB 缺)**: p0347_a004 ("codeetable"), p0347_a005 ("at a given visit" — 渲染无此短语), p0347_a017/a018 ("TUTSPLIT", 渲染为 TUSPLIT), p0347_a031 (item 4 与 item 6 句子拼接), p0349_a020 ("TUFTRESSP", 渲染为 TUPREISP), p0349_a019 (多一句号), p0346_a016 ("of first appearance" / "where there are"; 渲染 p346 为 "or" / "when", KB 与渲染一致), p0347_a003 ("TULORRES"), p0348_a008 ("populated by"/"evaluations"/"ADJUDICATION COMMITTEE"; 渲染 p348 为 provided/evaluators/ADJUDICATOR), p0348_a010 / p0349_a005 / p0349_a021 / p0349_a022 / p0349_a001 (与渲染逐词比对, KB 与渲染一致, atom 文本有错字/串句); p0345-0346 spec 表行 (属 spec.md). 以上 prose_scan 改后清单已逐条对渲染核过.

### 双向全扫 (含表格原子)
- PDF→KB (sent_scan, layout 文本逐句归一子串): TU 相关句改前未命中 → 改后仅剩: "aorta-iliac" (T-1); 跨页/页脚拼接伪句 ("A record in the TU domain…•…©", 1b 跨 p346 页脚); 其余全为 TR 节 / TR 例子句 (在 `TR/examples.md` 与 `TR/assumptions.md`, B-TR 范围) 与 spec 表行 (spec.md).
- KB→PDF (sent_scan, KB 逐句在 PDF 归一文本): 改前 5 → 改后 3: examples:5 ×2 (KB_AUTHORED 导航, 见下), examples:13 (T-1).
- prose_scan (pdf_atoms): 改前 TU/§6.3.12 未命中中, p0344_a016/a017, p0345_a005/a006, p0347_a023, p0348_a005, p0349_a011-a016, p0353_a005, p0353_a015/a016/a018, p0354_a005, p0356_a015-a022 改后均命中; 余下为上列抽取错 / spec 表 / TR 内容.
- 表格原子 (逐格对 110dpi 渲染): assumptions 6 张表 (p347 ×2, p348, p349 ×3) + examples Ex1 tu/supptu (p353-354), Ex2 tu/supptu (p354), Ex3 tu (p356): 表头 / 列序 / 列数 / Row 列一致. Ex2 两表改前即一致 (未改).
- 已核非问题 (仅格式, 同 B-MH/B-EG 口径未改): 6b 弯引号 “Tumor Identification”, assumption 2 "Tumor Split”" 引号不配对, PDF 普通文本 vs KB `**Rows 1-2:**` 加粗, assumption 8 `**Note:**` (PDF 亦粗体).
- PDF 自身编号不一致 (仅登记, 不改): assumption 2 写 "see assumption 3 for details on splitting", 但 splitting 说明在 assumption 2 的无编号段落中; assumption 3 是 location of interest. KB 编号与渲染一致, 未重编号.

### 新增 atom 清单 (R3)
- N-1 ig34_p0353_a005, N-2 p0344_a016, N-3 p0344_a017, N-4 p0345_a005, N-5 p0345_a006, N-6 p0346 "TU – Assumptions" 标题, N-7 p0347_a005, N-8 p0347_a023, N-9 p0348_a005, N-10 p0349 METIND r3 (unparseable 表格), N-11 p0349_a011-a016 (TUTESTCD), N-12 p0349_a016 (CONTRALATERAL).

### 删除清单 (reviewer 逐条确认)

| # | 原位置 (base 行号) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | assumptions:26 "a tumor/lesion identified at baseline might split" 中的 "identified at baseline" | :34 删 | D2 删扩写: p347 渲染为 "a tumor/lesion might split"; 该行只承载本句所在段落原子 (p0347_a005, 改前未命中) → 恢复 PDF 原文 | — |
| D-2 | assumptions:24/:26 之间的段落分隔 | :34 合并 | 同文件内按 PDF 归段 (PDF 为同一段), 无文字删除 | — |
| D-3 | 旧值替换 #1-#7, #16-#19 | 同行 | VALUE_DIFF / 表格跟 PDF 的旧值替换 | — |

### PDF_TYPO 清单

| T | 位置 | PDF | KB | 依据 / 处理 |
|---|---|---|---|---|
| T-1 | examples:13 Ex1 "Rows 1-2" | "…within the aorta-iliac vessel." | "aorto-iliac" (未改) | 正确值由 PDF 自身确定: 同例叙述 p353 "aorto-iliac vessel (L01-1)" 与表 r2 TULOC "AORTO-ILIAC PERIPHERAL ARTERY" → KB 保留并登记. p0353_a009 改前即不命中, 持续不命中, 非回归 |

### KB_AUTHORED (D6 / 导航)
- examples:5 "Note: TU and TR share examples. See also `[TR Examples](../TR/examples.md)`." — 纯导航, 不矛盾, 保留不加 D6 标注 (与 `TR/examples.md:3` 同形, B-TR review 已认可).
- 标题 `# TU — Assumptions` / `# TU — Examples` 为结构标题. 无其他 KB 自写解释内容.

### 范围外发现 (主控决定)
- **O-TU-1 `knowledge_base/domains/TU/spec.md`**: 无 spec 表脚注 "1In this column, an asterisk (*) …" (p346); spec 表行 (p345-346) 未核. 不在白名单, 未动 → 并入 O15/O24 spec 扫描.
- 无其他.

### 触碰过的 unparseable 表
- **TU/assumptions.md:90-92** (base :78) METIND 表: r3 "NOT DONE" 从 TUORRES 移到 TUSTAT. reviewer 须对 p349 渲染人工逐格.
- **TU/assumptions.md:98-105** (base :88) disease recurrence 表: TUTESTCD ×6、r6 TUORRES. reviewer 须对 p349 渲染人工逐格.

### git diff --stat
```
 knowledge_base/domains/TU/assumptions.md | 34 +++++++++++++++++++++-----------
 knowledge_base/domains/TU/examples.md    | 28 ++++++++++++++------------
 2 files changed, 37 insertions(+), 25 deletions(-)
```
- 只改本批 2 文件; 工作树其他 M/?? 为他批既有改动, 未触碰. 未 commit. check_links live docs 42 (基线 42).
