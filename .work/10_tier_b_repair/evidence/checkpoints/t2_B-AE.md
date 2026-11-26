# T2 B-AE writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `3c716a7ec388607cbeb64f4e1903959df799e4a6` (AE 两文件改前工作区干净)
- md5 before: AE/assumptions.md `d660dc469cdc654d84e301fabf8ebdfa`, AE/examples.md `c7941a27f2351d6705fb6f6e4822ab15`
- md5 after: AE/assumptions.md `ee76fb53f35f5c2737350b43b198c80b` (58 → 64 行, +6 = 两个新标题 + Description 句 + 空行), AE/examples.md `f8dd2e9226ebcd2f29d1e9b51ece2e45` (97 行不变)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-AE_writer/`
  (assumptions/examples.before.md, apply.py 精确替换 + 每组命中次数断言 + 表格每行竖线数 = 表头断言, prose_scan.py, census_before/after.json, fp_before/after.jsonl,
  渲染图 p133/p139/p141/p142 130dpi + Ex4/Ex5/Ex6 表与 p139 CRF 表 200-260dpi 局部放大)
- 数据来源: 表格逐格对照渲染图 (layout 文本只辅助); 叙述对照 `work/pdf_pages/ig34_p0133-0142.txt` + 渲染图.
- 本批 atoms 5 (REAL_GAP 2 / VALUE_DIFF 3) + t2_recheck 1 (O11, 按用户 D2 处理); census DIFF 6 表 (77 diffs) 全处理; pdf_only 0; unparseable 1 (已触碰).
- O8 / O11 已处理. 批次 JSON `notes` 中 "O11 报告, 不删" 已被用户裁定 D2 (`t1_user_ack.md`:14 "AE 恢复 PDF 原文") 取代.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | assumptions.md:3-7 | ig34_p0133_a021 | INSERTED | 新增 `## AE – Description/Overview` + 定义句 (逐字, 含 PDF 原有不通顺语法) + `## AE – Assumptions` 标题 (PDF 原标题, 结构仿 CM/IS); H1 未动 | 133 / 137 |
| 2 | examples.md:21 | ig34_p0141_a007 | REPLACED | "Findings About Events and Interventions" → "…Events or Interventions"; "solicited by prespecification" → "via" | 141 |
| 3 | examples.md:37 | ig34_p0141_a016 | REPLACED | "Events and Interventions" → "Events or Interventions" | 141 |
| 4 | examples.md:71 | ig34_p0142_a010 | INSERTED | 补 "if the AE was unanticipated (AEUNANT)," 分句; 后续 "if the AE was related" 随 PDF 为 "if it was related" | 142 |
| 5 | examples.md:75 | ig34_p0142_a012 | REPLACED + SKIPPED_PDF_TYPO | "laterality is specified" → "are specified"; "related to the event" 不照录, KB 保留 "device" (T-3) | 142 |
| 6 | assumptions.md:45 | ig34_p0139_a010 (t2_recheck, O11, D2) | REPLACED | 6 项扩写 → PDF "[ ] Fatal [ ] Life-threatening [ ] Inpatient hospitalization… [ ] etc."; "apply:" → "apply" (无冒号) | 139 |
| 7 | assumptions.md:49 | O8 (7c) | REPLACED | AEOSOSP → AESOSP | 139 |
| 8 | examples.md:81-82 | O8 (Ex5) + census:79 | TABLE_REBUILT | 整表按 PDF 重建 (见 #16); STUDYID T992 → T002 两行均是 (不止一格) | 142 |
| 9 | assumptions.md:13 | R3 N-1 ig34_p0137_a015 | INSERTED | 补 "The modified term is listed in AEMODIFY." | 137 |
| 10 | assumptions.md:19 | R3 N-2 ig34_p0138_a004 | REPLACED | "domain, see Section 4.2.6" → "domain; see" | 138 |
| 11 | assumptions.md:39 | R3 N-3 ig34_p0139_a007 | REPLACED | "may be null." → "may be null:" | 139 |
| 12 | assumptions.md:64 | R3 N-4 ig34_p0140_a008 | REPLACED | AESOCD → AESOCCD (spec.md:221 亦为 AESOCCD) | 140 |
| 13 | examples.md:15-17 | census:13 Ex1 (11) | REPLACED | r1/r2 自 AEACN 起整体错一列 (r1 AEACN 空、r2 多出 "RELATED") → 按 PDF 归位; AEMODIFY "Headache"/"Back pain" → HEADACHE / BACK PAIN; r2 AETERM "FOR 5 HOURS" → "FOR 6 HOURS"; r3 AEENRF "AFTER TREATMENT" → AFTER | 141 |
| 14 | examples.md:32-33 | census:29 Ex2 (2) | REPLACED | r2 AESTDTC 13T13:05 → 13T13:00; r3 AEENDTC 空 → 2005-10-21 | 141 |
| 15 | examples.md:43-46 | census:43 Ex3 (HEADER 1 + 4) | TABLE_REBUILT | 表头 → PDF 16 列 (+AEACN AEREL AESTDTC AEENDTC 均空; AESTDY → AEDY) | 141 |
| 16 | examples.md:63 | census:60 Ex4 (1) | REPLACED | r2 AEENDTC 2005-10-15 → 2005-10-16 | 142 |
| 17 | examples.md:79-82 | census:79 Ex5 (41) | TABLE_REBUILT | 表头按 PDF 列序 (AERELDEV→AERLDEV; 删 AEREL; +AESINTV; AESCONG 后 AESHOSP AESDISAB AESDTH…; AEUNANT AERLPRC AERLPRT); 行: AEDECOD SPRAIN / AELOC ANKLE JOINT, 日期 2018-…, AESTDY 5/15, 各 Y/N 照 PDF | 142 |
| 18 | examples.md:94-97 | census:94 Ex6 (HEADER 1 + 16) | TABLE_REBUILT | 表头 AESHOSP 前移到 AESCONG 后; STUDYID 1001 → T001; r1 USUBJID 002, AESPID AE0007, AEACNDEV SENSOR REPOSITIONED, AERLDEV CAUSAL, AESINTV N, 日期 2018-09-01/07, 27/33; r2 日期照 PDF | 142 |
| 19 | examples.md:81 | T-1 | SKIPPED_PDF_TYPO | Ex5 r1 AEENDTC 写 2018-04-26 (PDF 2014-04-26) | 142 |
| 20 | examples.md:82 | T-2 | SKIPPED_PDF_TYPO | Ex5 r2 AEOUT 写 SEQUELAE (PDF SEQUELLAE) | 142 |
| 21 | examples.md:79 | T-4 | SKIPPED_PDF_TYPO | Ex5 表头首格 PDF 空白, KB 写 `Row` | 142 |
| 22 | assumptions.md:43 | R3 N-5 (CRF 表 Yes/No) | REPLACED | "[ ] Yes  [ ] No" 双空格 → 单空格 (格式) | 139 |

- atoms 覆盖率自查: atoms 5 = #1 a021, #2 a007, #3 a016, #4 a010, #5 a012; t2_recheck 1 = #6 a010. 跳过 0 (a012 部分 PDF_TYPO).
- pdf_typo_suspect 原子 a012: 依同表 r2 AERLDEV = PROBABLE / AEACNDEV = REMOVED 可确定应为 "device" → T-3.

### census 表处理

| census ref (before 行号) | 处理 | 结果 |
|---|---|---|
| examples.md:13 Ex1 (11) | #13 | OK |
| :29 Ex2 (2) | #14 | OK |
| :43 Ex3 (5) | #15 | OK |
| :60 Ex4 (1) | #16 | OK |
| :79 Ex5 (41) | #8/#17 整表重建 | DIFF 2 残留 = T-1 (r1 AEENDTC), T-2 (r2 SEQUELAE) |
| :94 Ex6 (17) | #18 整表重建 | OK |
| assumptions.md:37 UNPARSEABLE | #6/#22 触碰 (改后 :43-45) | reviewer 须对 p139 渲染图人工核 |

- 汇总: before `UNPARSEABLE 1 / DIFF 6, cells 349, diffs 77` → after `UNPARSEABLE 1 / OK 5 / DIFF 1, cells 361, diffs 2 (全为 T-1/T-2)`.

```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-AE_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-AE.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # 改前同法 census_before.json
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl                                       # 改前同法 fp_before.jsonl
python3 -I $S/prose_scan.py
python3 tools/check_links.py | tail -1   # live docs: 42 (基线 42)
```

### fp_match (p133-142 原子)
- 回归 0; 新命中 14: p0133_a021, p0137_a015, p0138_a004, p0139_a007/a010/a013, p0140_a008, p0141_a007/a014/a016/a019, p0142_a004/a010/a014. hit_target 全库 3734 → 3748.
- 改后 p133-142 仍未命中 (均非本批 KB 缺失):
  - p0134_a002..p0137_a010 (spec 表 + spec 首句 + 脚注; 目标 spec.md, 非本批白名单; 改前同样未命中) 及 p0133_a003 (SU 节).
  - **预期 (PDF_TYPO, KB 偏离 PDF)**: ig34_p0142_a012 (T-3 "device"), ig34_p0142_a016 (T-2 SEQUELAE; 另 atom 有 "RECOVERED/ RESOLVED" 斜杠后空格). 若台账要求精确, 这两条即预期回归清单 (改前也未命中, 对 fp 不构成回归). T-1 所在 Ex5 r1 atom a015 同样受影响 (见下).
  - ATOM_ERR (原子抽取错, KB 已按渲染图): p0141_a003 (r1 AEDECOD / AEENDY 空, 渲染图有 Headache / -1), p0141_a004 / a013 (AEENDTC "2005-10-19:00", 渲染图 2005-10-13T19:00), p0141_a005 (AESHOSP/AESLIFE 列错位), p0142_a015 (r1 AESER Y / 日期 2018-04-26/2014-04-28 / AESTDY 15 等, 渲染图 N / 2018-04-21 / 2014-04-26 / 5), p0142_a022 (表头漏 AESPID), p0142_a023/a024 (仅 "RECOVERED/ RESOLVED" 斜杠后空格; 值与 KB 一致).

### 双向叙述扫描 (R3; prose_scan.py)
- PDF→KB: p133-142 AE 节非表格原子 (SENTENCE/LIST_ITEM/NOTE/HEADING) 归一后子串检查. 改后未命中: p0134_a001/a002、p0137_a010 (spec 节标题/首句/脚注 → spec.md, 范围外 F-1); p0140_a009 "AE – Examples" (KB H1 `# AE — Examples` 等价); p0142_a012 (T-3).
- KB→PDF: 改后未命中: assumptions.md:41 `**CRF: AE Seriousness Classification**` (KB 自写表前短标签, 纯导航, 保留, 不加 KB note); examples.md:75 "related to the device" (T-3). 无其它 KB 自写/超出 PDF 句.
- 改前同法额外缺失、本 attempt 已修: N-1..N-4 + atoms a021/a007/a016/a010/a012(部分) + O8 7c.
- 未做 (仅格式): 弯/直引号、撇号差异 (如 “Y”、sponsor’s) 未动; assumptions 7a PDF 在 "may be null:" 后另起段 "For example…", KB 同行未拆段.

### 新增 atom 清单 (R3)
- N-1 assumptions.md:13 ig34_p0137_a015; N-2 :19 ig34_p0138_a004; N-3 :39 ig34_p0139_a007; N-4 :64 ig34_p0140_a008; N-5 :43 CRF 表 Yes/No 空格 (ig34_p0139_a010 同表).

### 删除清单 (reviewer 逐条确认)

| # | 原位置 (base 行号) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | assumptions.md:39 CRF 行 "Inpatient hospitalization or prolongation of existing hospitalization … Persistent or significant disability/incapacity … Congenital anomaly/birth defect … Other medically important serious event" | :45 "[ ] Inpatient hospitalization… [ ] etc." | D2 删扩写 (O11, 用户裁定): KB 把 PDF "…/etc." 扩写成 6 项 | 无 (PDF 原文即截断形式) |
| D-2 | examples.md:75 "is specified" | "are specified" | VALUE_DIFF 旧值替换 | — |
| D-3 | examples.md:71 "if the AE was related to the procedure" 中 "the AE" | "if it was related" | 随 REAL_GAP 补句恢复 PDF 原文 (该行仅承载 a010) | — |
| D-4 | examples.md:21 "by prespecification" | "via" | 词替换型改写 (a007 原子范围内) | — |
| D-5 | Ex1/Ex3/Ex5/Ex6 表旧值、旧表头列 (Ex5 删 AEREL 列; Ex3 AESTDY 列名) | PDF 值 | VALUE_DIFF / 表格跟 PDF (规则 3) | — |

### PDF_TYPO 清单 (正确值可由 PDF 自身确定 → KB 写正确值)

| # | 位置 | PDF | KB | 依据 |
|---|---|---|---|---|
| T-1 | examples.md:81 Ex5 r1 AEENDTC | 2014-04-26 | 2018-04-26 | 同行 AESTDTC 2018-04-21 = AESTDY 5, AEENDY 10 → 恰 +5 天 = 2018-04-26 (单值); census 残留 1 |
| T-2 | examples.md:82 Ex5 r2 AEOUT | RECOVERED/RESOLVED WITH SEQUELLAE | …WITH SEQUELAE | CT C49495 (terminology/core/ae.md:38); census 残留 1 |
| T-3 | examples.md:75 Ex5 Row 2 叙述 | "probably related to the event" | "…related to the device" (KB 原值未动) | 同表 r2 AERLDEV = PROBABLE、AEACNDEV = REMOVED; 本例主题为器械关系; fp a012 残留 |
| T-4 | examples.md:79 Ex5 表头 | 首格空白 | `Row` | 同文件其他表一致; 列下为行号 1/2 |

### 照录 PDF, 供主控 / T4 用户裁 (KB = PDF)
- **U-1 Ex5 r2 AEENDY 25 (:82)**: AESTDTC 2018-05-01 = Day 15 → AEENDTC 2018-05-10 应为 Day 24. 日期与 Day 谁错不可单值确定 → 照录.
- **U-2 Ex6 r2 AEENDTC 2014-11-27 (:97)**: 早于 AESTDTC 2018-10-24, 年份必错; 但按 AESTDY 78 / AEENDY 113 推得 2018-11-28, 与 "11-27" 也不符 → 非单值, 照录.
- **U-3 Ex6 USUBJID r1 002 / r2 001 (:96-97)**: 同 SPDEVID、AESEQ 1/2、叙述同一 subject; 哪个对不可确定 → 照录.
- **U-4 Ex6 AESTDY r1 27 (2018-09-01) → r2 78 (2018-10-24)**: 推算应为 80 → 照录.
- **U-5 Ex6 r1 AERLDEV "CAUSAL" (:96)**: KB 原 "CAUSAL RELATIONSHIP"; PDF 渲染图 "CAUSAL"; KB terminology 无 ISO 14155 码表可证 → 照录 PDF.

### KB_AUTHORED / D6
- `**CRF: AE Seriousness Classification**` (assumptions.md:41): 表前短标签, 纯导航, 按 D6 范围不加 KB note, 保留.
- 其它: 无 (KB→PDF 扫描无自写解释句).

### 范围外发现
- F-1: AE spec 首句 "ae.xpt, Adverse Events — Events. One record per adverse event per subject, Tabulation." (ig34_p0134_a002) 与 spec 表脚注 (ig34_p0137_a010) 在 AE 三文件均无; 目标 spec.md 非本批白名单 (CM/IS 把首句放在 assumptions.md 的 Specification 节). 主控定是否追加.

### 触碰过的 unparseable 表
- assumptions.md:37 (改后 :43-45) CRF 表: reviewer 须对 p139 渲染图逐格人工核.

### git diff --stat -- kb_files
```
 knowledge_base/domains/AE/assumptions.md | 20 ++++++++++-----
 knowledge_base/domains/AE/examples.md    | 44 ++++++++++++++++----------------
 2 files changed, 35 insertions(+), 29 deletions(-)
```
- check_links: `broken relative links: 18668 (live docs: 42)` (基线 42, 未升).
- writer.jsonl: 97 行 = atoms 5 + t2_recheck 1 + O8 2 + R3 N-1..N-5 (5) + census 77 + T-4 1 + U-1..U-5 (5) + unparseable 1. T-1/T-2 记在 census 行 note, T-3 记在 a012 行.

## attempt 1 续 (reviewer PASS 后主控收尾指令; 须回 reviewer 复审 delta)

| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 23 | assumptions.md:43-45 | L-1 (ig34_p0139_a007/a008) | REPLACED | "may be null: For example…" 同行 → "may be null:" 后另起段 (6 空格缩进, 同 "On the other hand" 段), 文字不变 | 139 |
| 24 | assumptions.md:7-9 | F-1 ig34_p0134_a002 | INSERTED | Description 与 Assumptions 之间新增 `## AE – Specification` + spec 首句逐字 (仿 CM/assumptions.md:7-9); p137 表脚注 a010 不动 (留 spec.md 扫描) | 134 |

- L-2: 保留 (主控裁定).
- md5 after: AE/assumptions.md `71ce6c47b9141ee69e8f5d88a9bda7bb` (64 → 70 行); examples.md 未动 `f8dd2e9226ebcd2f29d1e9b51ece2e45`.
- fp_match (`fp_after2.jsonl`): p133-142 对改前回归 0、对 attempt 1 回归 0; 新命中 ig34_p0134_a002. census 不变 (DIFF 1 / diffs 2 = T-1/T-2). check_links live docs 42 (基线 42).
