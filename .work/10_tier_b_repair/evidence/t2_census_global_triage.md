# T2 收尾: 全局 table census 重跑 + 非 OK 表分诊

> 状态: **已完成** (2026-11-26); 基于 HEAD `50c3958` (60 批 T2 全部提交后); 只读 KB, 未改 KB / 未动 git

## 1. 结论 (先看这里)

- **修正 manifest 对结果零影响**: 原 `work/census_full_manifest.json` 与修正版 v3 在 HEAD 上跑出的 `tables` / `pdf_only` / `pdf_unparsed` 三项逐项全等 (命令见 §3 第 3-4 条; 对照: T1 时 `work/census_full.json` 为 DIFF 130 / PDF_ONLY 15). 原因: 脚本配对允许 ±3 页且按 (例号, 数据集名) 键配对, 偏移 ≤ 2-3 页的 manifest 不改变配对.
- **全局 PDF_ONLY = 1, 不是 336-338**: 各批 reviewer 报的 336-338 来自**单批 manifest** (只装本批 KB 文件, 其他所有 PDF 表必然 unpaired). 全量 manifest 下 PDF_ONLY 仅 1 张 (p431 relrec, C2 假阳, KB 有两份逐格 OK 的副本).
- 全量 HEAD 状态: KB 表 501 = OK 311 / DIFF 37 (diffs 144) / NO_PDF 4 / UNPARSEABLE 149; PDF 表 339 (+2 PDF_UNPARSED); cells compared 35129.
- 非 OK 共 193 项 (37+4+149+1+2): A 33 / B 96 / C1 3 / C2 1 / C3 60.
- **C1 = 3 张, 均为 KB 值正确、PDF 笔误但未登记** (SE ×2 BIRTHDTC, TD ×1 TDTGPAI; 这两个域没有 T2 批) → 处置 = 补登 T-n, **KB 不改**.
- **结论适用范围**: "无 KB 必须改的真缺表 / 真差值" 只对机检过 (census OK/DIFF/NO_PDF) 与有 B 类逐格证据的表成立; C3 的 60 张 UNPARSEABLE 表状态未知.
- C3 = 60 张: ch04 23 (仅子串扫, 无按列/渲染逐格)、model/02 15、EX 8 (CRF 未触碰)、model/03 7、ch10 5、model/04 1、TR/assumptions 1 → 须人工逐格.
- 覆盖检查: KB 中含 `| Row |` 表的文件全部在 138 文件 manifest 内 (manifest 外 0 个).

## 2. 修正版 manifest 清单 (36 条, 18 个域)

规则: `set` = manifest 页属于相邻节, 直接替换; `union` = 只扩不缩 (EX/EC、MB/MS、PC/PP、TU/TR 共用例子节, manifest 故意宽, 不收窄). 依据栏: checkpoint 文件 (位于 `evidence/checkpoints/`) 或 PDF 节标题扫描 (`work/pdf_pages/ig34_pNNNN.txt` 的节号标题行, 页:行).

| KB 文件 | 原 lo-hi | 修正 lo-hi | 方式 | 依据 |
|---|---|---|---|---|
| `domains/DM/assumptions.md` | 62-78 | 62-79 | union | t2_B-DM_review.md:9 (p79 Ex7 suppdm; O34) |
| `domains/DM/examples.md` | 62-78 | 62-79 | union | t2_B-DM_review.md:9 (p79 Ex7 suppdm; O34) |
| `domains/FA/assumptions.md` | 364-375 | 361-375 | union | O20 / t2_B-FA.md:101 (§6.4 intro + §6.4.1-6.4.3 p361-364) |
| `domains/FA/examples.md` | 364-375 | 361-375 | union | O20 / t2_B-FA.md:101 (§6.4 intro + §6.4.1-6.4.3 p361-364) |
| `domains/MB/assumptions.md` | 248-262 | 248-263 | union | t2_B-MI_review.md:8 (p263 top = MB Ex3-4); t2_B-MS ranges p248-263 |
| `domains/MB/examples.md` | 248-262 | 248-263 | union | t2_B-MI_review.md:8 (p263 top = MB Ex3-4); t2_B-MS ranges p248-263 |
| `domains/MS/assumptions.md` | 252-262 | 252-263 | union | t2_B-MS checkpoint p252-263 (shared §6.3.5.7.3 examples to p263) |
| `domains/MS/examples.md` | 252-262 | 252-263 | union | t2_B-MS checkpoint p252-263 (shared §6.3.5.7.3 examples to p263) |
| `domains/RELREC/assumptions.md` | 428-430 | 427-431 | set | t2_B-REL_review.md:7 (§8 intro p427; §8.2-8.3.1 p429-431) |
| `domains/RELREC/examples.md` | 428-430 | 427-431 | set | t2_B-REL_review.md:7 (§8 intro p427; §8.2-8.3.1 p429-431) |
| `domains/RELSPEC/assumptions.md` | 438-440 | 439-440 | set | t2_B-REL_review.md:7 (§8.8 p439-440) |
| `domains/RELSPEC/examples.md` | 438-440 | 439-440 | set | t2_B-REL_review.md:7 (§8.8 p439-440) |
| `domains/RELSUB/assumptions.md` | 437-438 | 437-439 | set | t2_B-REL_review.md:7 (§8.7 p437-439) |
| `domains/RELSUB/examples.md` | 437-438 | 437-439 | set | t2_B-REL_review.md:7 (§8.7 p437-439) |
| `domains/SE/assumptions.md` | 79-83 | 79-84 | union | PDF heading scan: 5.3 SE p79:10, 5.4 SM p84:10 |
| `domains/SE/examples.md` | 79-83 | 79-84 | union | PDF heading scan: 5.3 SE p79:10, 5.4 SM p84:10 |
| `domains/SS/assumptions.md` | 342-343 | 342-344 | union | PDF heading scan: 6.3.11 SS p342:38, 6.3.12 p344:23 |
| `domains/SS/examples.md` | 342-343 | 342-344 | union | PDF heading scan: 6.3.11 SS p342:38, 6.3.12 p344:23 |
| `domains/SU/assumptions.md` | 129-132 | 129-133 | union | t2_B-SU_review.md:8 (su.xpt p133) |
| `domains/SU/examples.md` | 129-132 | 129-133 | union | t2_B-SU_review.md:8 (su.xpt p133) |
| `domains/SUPPQUAL/assumptions.md` | 430-432 | 431-434 | set | t2_B-SUPPQUAL.md / _review.md (§8.4 = p431-434) |
| `domains/SUPPQUAL/examples.md` | 430-432 | 431-434 | set | t2_B-SUPPQUAL.md / _review.md (§8.4 = p431-434) |
| `domains/TA/assumptions.md` | 385-404 | 382-402 | set | t2_B-TA.md:13 (scan p382-402, §7.1 carried by TA/assumptions) |
| `domains/TA/examples.md` | 385-404 | 382-402 | set | t2_B-TA.md:13 (scan p382-402, §7.1 carried by TA/assumptions) |
| `domains/TD/assumptions.md` | 412-416 | 410-414 | set | PDF heading scan: 7.3.2 TD p410:37, 7.3.3 TM p415:1 |
| `domains/TD/examples.md` | 412-416 | 410-414 | set | PDF heading scan: 7.3.2 TD p410:37, 7.3.3 TM p415:1 |
| `domains/TE/assumptions.md` | 404-409 | 402-407 | set | O27; t2_B-TE.md § O20 页范围 |
| `domains/TE/examples.md` | 404-409 | 402-407 | set | O27; t2_B-TE.md § O20 页范围 |
| `domains/TI/assumptions.md` | 418-419 | 415-426 | set | O48; t2_B-TI_review.md (TI/assumptions 415-426: §7.4 intro + §7.5) |
| `domains/TI/examples.md` | 418-419 | 416-417 | set | O48; t2_B-TI_review.md (TI/examples 416-417) |
| `domains/TM/assumptions.md` | 417-417 | 415-415 | set | PDF heading scan: 7.3.3 TM p415:1, 7.4 p415:50 |
| `domains/TM/examples.md` | 417-417 | 415-415 | set | PDF heading scan: 7.3.3 TM p415:1, 7.4 p415:50 |
| `domains/TS/assumptions.md` | 419-425 | 417-425 | set | t2_B-TS.md / t2_B-TS_review.md 节页范围核 p417-425 |
| `domains/TS/examples.md` | 419-425 | 417-425 | set | t2_B-TS.md / t2_B-TS_review.md 节页范围核 p417-425 |
| `domains/TV/assumptions.md` | 409-412 | 407-410 | set | O47; t2_B-TV.md § O20 页范围 |
| `domains/TV/examples.md` | 409-412 | 407-410 | set | O47; t2_B-TV.md § O20 页范围 |

未修正但已核: EX/EC (104/107-120)、MB/MS、PC/PP (267/271-283)、TU/TR (344/350-358) 的 manifest 宽于单节, 因例子节共用 (§6.1.3.3 / §6.3.5.7.3 / §6.3.5.9.3 / §6.3.12.3), 保留. DI 无表, 不加入. chapters / model 未发现偏移证据, 未动.

## 3. 重跑命令 (可复跑, repo 根执行; 脚本与产物在 `.work/10_tier_b_repair/work/scratch/t2/global/`, gitignored)

```
G=.work/10_tier_b_repair/work/scratch/t2/global
python3 -I $G/build_manifest_v3.py $G/manifest_v3.json            # 生成修正 manifest + manifest_v3.changes.json (36 条)
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $G/manifest_v3.json --out $G/census_full_v3.json
#  → PDF tables parsed: 339 (+2 unparsed); KB tables: 501; status: {'UNPARSEABLE': 149, 'OK': 311, 'DIFF': 37, 'NO_PDF': 4}; PDF_ONLY: 1; cells compared: 35129; diffs: 144; RESULT: RED
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest .work/10_tier_b_repair/work/census_full_manifest.json --out $G/census_full_v2head.json
#  → 同上 (逐字相同的 summary 行)
python3 -I -c "import json;a=json.load(open('$G/census_full_v2head.json'));b=json.load(open('$G/census_full_v3.json'));print([a[k]==b[k] for k in ('tables','pdf_only','pdf_unparsed')])"
#  → [True, True, True]
python3 -I $G/triage_evidence.py; python3 -I $G/unparseable_evidence.py   # 分诊辅助: 每个非 OK 表在所属批 checkpoint 中的候选证据行
python3 -I $G/triage_classify.py                                          # 分诊编码 → triage_rows.json + triage_tables.md (下文 §4/§5/§6 由此生成)
```

## 4. 汇总 (状态 × 类)

A = 已登记 T-n (指到 checkpoint 登记行, 且 census 残留 diff 数 = 登记数); B = 已人工逐格核过 (指到 review/audit 逐格证据; KB_AUTHORED D6 表无 PDF 对应者也归此, 已注明); C1 = 真差值/真缺表; C2 = 解析器/manifest 假阳; C3 = 不能判定, 须人工.

| 状态 | A | B | C1 | C2 | C3 | 合计 |
|---|---|---|---|---|---|---|
| DIFF | 33 | 1 | 3 | 0 | 0 | 37 |
| NO_PDF | 0 | 4 | 0 | 0 | 0 | 4 |
| PDF_ONLY | 0 | 0 | 0 | 1 | 0 | 1 |
| PDF_UNPARSED | 0 | 2 | 0 | 0 | 0 | 2 |
| UNPARSEABLE | 0 | 89 | 0 | 0 | 60 | 149 |
| 合计 | 33 | 96 | 3 | 1 | 60 | 193 |

说明: 2 张 PDF_UNPARSED (p274 pp.xpt Ex2 / p342 sc.xpt Ex2, 垂直居中) 与 NO_PDF 的 `domains/PP/examples.md:54`、`domains/SC/examples.md:32` 是同一张表的 PDF 侧 / KB 侧, 计两次.

## 5. C 类逐张清单

C1 处置: 3 张均为 PDF 表头笔误 (PDF 同节其他页拼法与 KB 一致), 按 "PDF 自身可确定 → KB 写正确值 + 登记 T-n" 口径, 只需补登, KB 不改. C3 处置: 对 PDF 渲染逐格核 (页码列给的是 manifest 范围, 未细化到页). ch04 C3: writer `t2_B-ch04.md:358-361` 的全文件反向扫对这些表 "去空白子串命中", 能排除缺字/错字, 但看不出值落错列; reviewer `t2_B-ch04_review_a3.md:96` 建议 9 (逐表对渲染) 未见逐表落实记录.

| # | 类 | 状态 | KB file:line | PDF 页 | ex / ds | 判断 / 处置 | 依据 |
|---|---|---|---|---|---|---|---|
| 1 | C3 | UNPARSEABLE | `domains/EX/examples.md:13` | ig34:p104-120 | 1 / None | Bottle / Number of Tablets Taken Daily / Reason for Variatio | t2_B-EX.md:70 (未改, 未逐格) |
| 2 | C3 | UNPARSEABLE | `domains/EX/examples.md:19` | ig34:p104-120 | 1 / None | Bottle / Number of Tablets Taken Daily / Reason for Variatio | t2_B-EX.md:70 (未改, 未逐格) |
| 3 | C3 | UNPARSEABLE | `domains/EX/examples.md:65` | ig34:p104-120 | 2 / None |  /  | t2_B-EX.md:70 (未改, 未逐格) |
| 4 | C3 | UNPARSEABLE | `domains/EX/examples.md:173` | ig34:p104-120 | 5 / None | Bottle / Time Point / Number of Tablets Taken / Start Date / | t2_B-EX.md:70 (未改, 未逐格) |
| 5 | C3 | UNPARSEABLE | `domains/EX/examples.md:180` | ig34:p104-120 | 5 / None | Bottle / Time Point / Number of Tablets Taken / Start Date / | t2_B-EX.md:70 (未改, 未逐格) |
| 6 | C3 | UNPARSEABLE | `domains/EX/examples.md:187` | ig34:p104-120 | 5 / None | Bottle / Time Point / Number of Tablets Taken / Start Date / | t2_B-EX.md:70 (未改, 未逐格) |
| 7 | C3 | UNPARSEABLE | `domains/EX/examples.md:422` | ig34:p104-120 | 8 / None | First Dose Date / Last Dose Date | t2_B-EX.md:70 (未改, 未逐格) |
| 8 | C3 | UNPARSEABLE | `domains/EX/examples.md:426` | ig34:p104-120 | 8 / None | Date / Number of Doses Daily If/When Deviated from Plan | t2_B-EX.md:70 (未改, 未逐格) |
| 9 | C1 | DIFF | `domains/SE/examples.md:44` | ig34:p82/83 | 1 / dm.xpt | 表头 KB BRTHDTC vs PDF p82 BIRTHDTC; PDF p63-68 DM spec/例均 BRTHDTC → PDF 笔误, KB 值正确; 处置=补登 T-n, KB 不改 | 无 (SE 无 T2 批; 全 evidence/work 无 BIRTHDTC 登记) |
| 10 | C1 | DIFF | `domains/SE/examples.md:79` | ig34:p83/84 | 2 / dm.xpt | 同上 (PDF p83-84) | 同上 |
| 11 | C1 | DIFF | `domains/TD/examples.md:161` | ig34:p414 | 3 / td.xpt | 表头 KB TDTGTPAI vs PDF p414 TDTGPAI; PDF p411-413 spec/例均 TDTGTPAI → PDF 笔误, KB 值正确; 处置=补登 T-n, KB 不改 | 无 (TD 无 T2 批; 无登记) |
| 12 | C3 | UNPARSEABLE | `domains/TR/assumptions.md:15` | ig34:p350-358 | None / None | TRLNKID / TRTESTCD / TRTEST / TRORRES / TRORRESU / TRSTRESC  | t2_B-TR.md:44 (未触碰, 未逐格) |
| 13 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:391` | ig34:p22-59 | None / None | Reason for Dose Adjustment (EXADJ) / Describe | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 14 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:408` | ig34:p22-59 | None / None | Indication for analgesic / Options | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 15 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:453` | ig34:p22-59 | None / None | Eye Color / Options | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 16 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:465` | ig34:p22-59 | None / None | SCTEST / SCORRES / SCSTRESC | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 17 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:471` | ig34:p22-59 | None / None | SCTEST / SCORRES / SCSTRESC | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 18 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:477` | ig34:p22-59 | None / None | SCTEST / SCORRES / SCSTRESC | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 19 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:487` | ig34:p22-59 | None / None | Indicate which of the following concomitant medications was  | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 20 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:497` | ig34:p22-59 | None / None | CMTRT / CMPRESP | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 21 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:558` | ig34:p22-59 | 1 / ae.xpt | AETERM / AELOC | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 22 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:564` | ig34:p22-59 | 1 / suppae.xpt | QNAM / QLABEL / QVAL | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 23 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:576` | ig34:p22-59 | 1 / ae.xpt | AETERM / AEREL / AEACN | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 24 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:582` | ig34:p22-59 | 1 / suppae.xpt | QNAM / QLABEL / QVAL | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 25 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:597` | ig34:p22-59 | 1 / ae.xpt | AETERM / AEREL / AEACN | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 26 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:603` | ig34:p22-59 | 1 / suppae.xpt | QNAM / QLABEL / QVAL | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 27 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:678` | ig34:p22-59 | None / None | Domain / Original Verbatim / Modified Verbatim / Standardize | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 28 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:749` | ig34:p22-59 | None / None | # / Date and Time as Originally Recorded / Precision / ISO 8 | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 29 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:761` | ig34:p22-59 | None / None | # / Interval of Uncertainty / ISO 8601 Date/Time | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 30 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:1034` | ig34:p22-59 | None / None | Collection Type / --DTC / --STDTC / --ENDTC | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 31 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:1074` | ig34:p22-59 | None / None | VSTPTNUM / VSTPT / VSELTM / VSTPTREF / VSRFTDTC / VSDTC | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 32 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:1084` | ig34:p22-59 | None / None | LBTPTNUM / LBTPT / LBELTM / LBTPTREF / LBRFTDTC / LBDTC | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 33 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:1112` | ig34:p22-59 | None / None | VISIT / VISITNUM / --TPT / --TPTNUM / --TPTREF | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 34 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:1135` | ig34:p22-59 | None / None | VISIT / VISITNUM / --TPT / --TPTNUM / --TPTREF | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 35 | C3 | UNPARSEABLE | `chapters/ch04_general_assumptions.md:1511` | ig34:p22-59 | None / None | Situation / Value of --PRESP / Value of --OCCUR / Value of - | 仅 t2_B-ch04.md:358-361 全文件表格去空白子串反向扫 clean; 无按列定位/渲染逐格 (review_a3.md:96 建议 9 未见逐表落实) |
| 36 | C3 | UNPARSEABLE | `chapters/ch10_appendices.md:19` | ig34:p444-461 | None / None | Abbreviation / Full Term | 无 T2 批 |
| 37 | C3 | UNPARSEABLE | `chapters/ch10_appendices.md:93` | ig34:p444-461 | None / None | QNAM / QLABEL / Applicable Domains | 无 T2 批 |
| 38 | C3 | UNPARSEABLE | `chapters/ch10_appendices.md:119` | ig34:p444-461 | None / None | Keyword(s) / Fragment /  / Keyword(s) / Fragment | 无 T2 批 |
| 39 | C3 | UNPARSEABLE | `chapters/ch10_appendices.md:208` | ig34:p444-461 | None / None | Domain / Description | 无 T2 批 |
| 40 | C3 | UNPARSEABLE | `chapters/ch10_appendices.md:230` | ig34:p444-461 | None / None | Section Number / Section Name / Change(s) | 无 T2 批 |
| 41 | C3 | UNPARSEABLE | `model/02_observation_classes.md:41` | sv20:p11-39 | None / None | # / Variable / Label / Type / Role / Key Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 42 | C3 | UNPARSEABLE | `model/02_observation_classes.md:93` | sv20:p11-39 | None / None | # / Variable / Label / Type / Role / Key Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 43 | C3 | UNPARSEABLE | `model/02_observation_classes.md:162` | sv20:p11-39 | None / None | Variable / Label / Type / Role | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 44 | C3 | UNPARSEABLE | `model/02_observation_classes.md:169` | sv20:p11-39 | None / None | Variable / Label / Type / Role / Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 45 | C3 | UNPARSEABLE | `model/02_observation_classes.md:179` | sv20:p11-39 | None / None | Variable / Label / Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 46 | C3 | UNPARSEABLE | `model/02_observation_classes.md:190` | sv20:p11-39 | None / None | Variable / Label / Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 47 | C3 | UNPARSEABLE | `model/02_observation_classes.md:202` | sv20:p11-39 | None / None | Variable / Label / Type / Role / Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 48 | C3 | UNPARSEABLE | `model/02_observation_classes.md:212` | sv20:p11-39 | None / None | # / Variable / Label / Type / Role / Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 49 | C3 | UNPARSEABLE | `model/02_observation_classes.md:237` | sv20:p11-39 | None / None | # / Variable / Label / Type / Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 50 | C3 | UNPARSEABLE | `model/02_observation_classes.md:251` | sv20:p11-39 | None / None | # / Variable / Label / Type / Format / Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 51 | C3 | UNPARSEABLE | `model/02_observation_classes.md:259` | sv20:p11-39 | None / None | # / Variable / Label / Type / Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 52 | C3 | UNPARSEABLE | `model/02_observation_classes.md:279` | sv20:p11-39 | None / None | # / Variable / Label / Type / Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 53 | C3 | UNPARSEABLE | `model/02_observation_classes.md:289` | sv20:p11-39 | None / None | # / Variable / Label / Type / Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 54 | C3 | UNPARSEABLE | `model/02_observation_classes.md:302` | sv20:p11-39 | None / None | # / Variable / Label / Type / Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 55 | C3 | UNPARSEABLE | `model/02_observation_classes.md:310` | sv20:p11-39 | None / None | # / Variable / Label / Type / Notes | B-FA / B-model01 触碰过本文件, 但变量表未逐格 (t2_B-model01_review.md:102) |
| 56 | C3 | UNPARSEABLE | `model/03_special_purpose_domains.md:17` | sv20:p40-49 | None / None | # / Variable / Label / Type / Role / Notes | 无 T2 批 |
| 57 | C3 | UNPARSEABLE | `model/03_special_purpose_domains.md:60` | sv20:p40-49 | None / None | Variable / Description / Typical Use | 无 T2 批 |
| 58 | C3 | UNPARSEABLE | `model/03_special_purpose_domains.md:79` | sv20:p40-49 | None / None | # / Variable / Label / Type / Role | 无 T2 批 |
| 59 | C3 | UNPARSEABLE | `model/03_special_purpose_domains.md:105` | sv20:p40-49 | None / None | # / Variable / Label / Type / Role / Notes | 无 T2 批 |
| 60 | C3 | UNPARSEABLE | `model/03_special_purpose_domains.md:131` | sv20:p40-49 | None / None | # / Variable / Label / Type / Role / Notes | 无 T2 批 |
| 61 | C3 | UNPARSEABLE | `model/03_special_purpose_domains.md:152` | sv20:p40-49 | None / None | # / Variable / Label / Type / Role / Notes | 无 T2 批 |
| 62 | C3 | UNPARSEABLE | `model/03_special_purpose_domains.md:179` | sv20:p40-49 | None / None | # / Variable / Label / Type / Role / Notes | 无 T2 批 |
| 63 | C3 | UNPARSEABLE | `model/04_associated_persons.md:31` | sv20:p50-50 | None / None | Variable / Label / Type / Role / Notes | 无 T2 批 |
| 64 | C2 | PDF_ONLY | - | ig34:p[431] | 1 / relrec.xpt | §8.3.1 Ex1 relrec 2 行; KB 两份副本均逐格 OK; 同 ±3 页内 §8.2.2 Ex1 relrec (p430) 同键 (Ex1, relrec.xpt) 冲突 (疑) 致一对一槽位未落到 p431 → 配对算法假阳, KB 不缺表 | census_full_v3.json: RELREC/examples.md:63 与 ch08_relationships.md:162 均 OK 配到 p431 (kb_duplicate=True) |


## 6. A / B 类逐张 (依据)

注: checkpoint 中的行号是该批当时的行号, 后续批可能有移动 (如 SC :34 → 现 :32, PP :56 → 现 :54); 以例号 + 数据集名对应. 同一 T-n 跨 attempt 变更的 (CP T-5/T-10 照录→改正, MS T-3 候选→keep-correct, MB T-3 候选→改) 指最终 attempt 行. NO_PDF 表 census 无法计偏差, 已登记偏差写在说明栏.

| 类 | 状态 | KB file:line | PDF 页 | diffs | 说明 | checkpoint 依据 |
|---|---|---|---|---|---|---|
| B | UNPARSEABLE | `domains/AE/assumptions.md:49` | ig34:p133-142 | 0 | Serious? / [ ] Yes [ ] No | t2_B-AE_review.md:39 |
| A | DIFF | `domains/AE/examples.md:79` | ig34:p142 | 2 | T-1 AEENDTC + T-2 SEQUELAE (2 diffs) | t2_B-AE.md:98-99 |
| A | DIFF | `domains/BE/examples.md:39` | ig34:p146 | 3 | T-1 ISOPOPANOL x2 + T-2 BSDTC (3) | t2_B-BE.md:18,20,44 |
| A | DIFF | `domains/BE/examples.md:120` | ig34:p147 | 2 | T-3 BSREFID x2 (2) | t2_B-BE.md:21,46 |
| B | UNPARSEABLE | `domains/CE/assumptions.md:20` | ig34:p148-155 | 0 | Situation / Value of CEPRESP / Value of CEOCCUR / Value of C | t2_B-CE_review.md:50-51 |
| B | UNPARSEABLE | `domains/CE/examples.md:11` | ig34:p148-155 | 0 | Clinical Sign / Did it occur? / Start Date of First Episode | t2_B-CE_review.md:50-66 (Ex1/Ex2/Ex3 CRF 逐格) |
| B | UNPARSEABLE | `domains/CE/examples.md:41` | ig34:p148-155 | 0 | Event /  / Date Started / Date Ended / Severity | t2_B-CE_review.md:50-66 (Ex1/Ex2/Ex3 CRF 逐格) |
| B | UNPARSEABLE | `domains/CE/examples.md:72` | ig34:p148-155 | 0 | Question / Response Options | t2_B-CE_review.md:50-66 (Ex1/Ex2/Ex3 CRF 逐格) |
| A | DIFF | `domains/CP/examples.md:85` | ig34:p211/212 | 1 | T-5 CPDTC (1) | t2_B-CP.md:202 (final attempt) |
| A | DIFF | `domains/CP/examples.md:206` | ig34:p216/217 | 29 | T-7 1 + T-8a/b 2 + T-9 26 (29) | t2_B-CP.md:204-207,215 |
| A | DIFF | `domains/CP/examples.md:279` | ig34:p219 | 1 | T-10 CPSTRESU (1) | t2_B-CP.md:208 |
| B | NO_PDF | `domains/CP/examples.md:311` | ig34:p199-220 | 0 | NO_PDF: PDF Ex9 表头 `ROW` 解析器不识别; reviewer layout 逐格 14 行×31 列, 差异仅登记 T-11/T-12/T-13 (KB 改正) + T-14 表头 | t2_B-CP_review.md:28; t2_B-CP.md:209-212 |
| A | DIFF | `domains/DM/examples.md:7` | ig34:p68 | 1 | T-2 RACE ISLANDER(S) (1) | t2_B-DM.md:54; t2_B-DM_review.md:18 |
| B | UNPARSEABLE | `domains/DM/examples.md:178` | ig34:p62-79 | 0 | CDASH Variable / Order / Question Text / Prompt / CRF Comple | t2_B-DM_review.md:38,84,126 |
| B | UNPARSEABLE | `domains/DM/examples.md:330` | ig34:p62-79 | 0 | CDASH Variable / Order / Question Text / Prompt / CRF Comple | t2_B-DM_review.md:38,84,126 |
| A | DIFF | `domains/DM/examples.md:435` | ig34:p78 | 1 | T-1 Row 4 vs 3 (1) | t2_B-DM_review.md:19,37 |
| A | DIFF | `domains/DS/examples.md:292` | ig34:p165 | 1 | T-1 SDSEQ->SESEQ (1) | t2_B-DS.md:94 |
| A | DIFF | `domains/DS/examples.md:342` | ig34:p166 | 1 | T-2 TESTRL 'is' (1) | t2_B-DS.md:95 |
| B | UNPARSEABLE | `domains/EX/examples.md:243` | ig34:p104-120 | 0 | Period 1 /  /  /  /  / Period 2 /  /  /  /  | t2_B-EX_review.md:52-53 (Ex6 CRF) |
| B | UNPARSEABLE | `domains/EX/examples.md:252` | ig34:p104-120 | 0 | Period 1 /  /  /  /  / Period 2 /  /  /  /  | t2_B-EX_review.md:52-53 (Ex6 CRF) |
| B | UNPARSEABLE | `domains/EX/examples.md:339` | ig34:p104-120 | 0 | Visit / 1 / 2 / 3 | t2_B-EX_review.md:31 (Ex7 CRF) |
| A | DIFF | `domains/EX/examples.md:407` | ig34:p119 | 3 | T-1 Row 1,2,6,3,4,6 (3) | t2_B-EX.md:76; t2_B-EX_review.md:58 |
| B | UNPARSEABLE | `domains/FA/assumptions.md:97` | ig34:p361-375 | 0 | FATESTCD / FATEST | t2_B-FA_review.md:101 |
| B | UNPARSEABLE | `domains/FA/examples.md:7` | ig34:p361-375 | 0 | Migraine Symptoms Diary /  | t2_B-FA_review.md:97-108,131 |
| B | UNPARSEABLE | `domains/FA/examples.md:76` | ig34:p361-375 | 0 | Rash Assessment /  | t2_B-FA_review.md:97-108,131 |
| B | UNPARSEABLE | `domains/FA/examples.md:133` | ig34:p361-375 | 0 | Date of assessment / DD-MMM-YYYY | t2_B-FA_review.md:97-108,131 |
| B | UNPARSEABLE | `domains/FA/examples.md:138` | ig34:p361-375 | 0 | Symptom / Was the symptom present? / If yes, what was the se | t2_B-FA_review.md:97-108,131 |
| B | UNPARSEABLE | `domains/FA/examples.md:176` | ig34:p361-375 | 0 | Date of assessment / DD-MMM-YYYY | t2_B-FA_review.md:97-108,131 |
| B | UNPARSEABLE | `domains/FA/examples.md:219` | ig34:p361-375 | 0 | Symptoms /  / Investigator GERD Symptom Measurement (if symp | t2_B-FA_review.md:97-108,131 |
| B | UNPARSEABLE | `domains/FA/examples.md:263` | ig34:p361-375 | 0 |  /  /  /  / At each visit, record the maximum severity of th | t2_B-FA_review.md:97-108,131 |
| B | UNPARSEABLE | `domains/FA/examples.md:273` | ig34:p361-375 | 0 | AE ID / Adverse Event / Start Date / End Date | t2_B-FA_review.md:97-108,131 |
| B | UNPARSEABLE | `domains/FA/examples.md:279` | ig34:p361-375 | 0 | Visit / AE ID / Maximum severity since last visit | t2_B-FA_review.md:97-108,131 |
| A | DIFF | `domains/GF/examples.md:143` | ig34:p227 | 1 | T-2 Idenitifcation (1) | t2_B-GF.md:90 |
| A | DIFF | `domains/HO/examples.md:19` | ig34:p170 | 1 | T-1 REHABILIATION (1) | t2_B-HO.md:39 |
| A | DIFF | `domains/IS/examples.md:113` | ig34:p236 | 2 | T-1/T-2 RSC1230 (2) | t2_B-IS.md:107-108 |
| B | UNPARSEABLE | `domains/LB/assumptions.md:20` | ig34:p241-248 | 0 | Variable Name / Variable Label / Type / Controlled Terms, Co | t2_B-LB_review.md:34 |
| A | DIFF | `domains/LB/examples.md:67` | ig34:p247 | 1 | T-1 LBSTRNHI header (1) | t2_B-LB.md:105 |
| A | DIFF | `domains/MB/examples.md:198` | ig34:p262 | 2 | T-1 suppmb Row 7/8 (2) | t2_B-MB.md:100 |
| A | DIFF | `domains/MB/examples.md:241` | ig34:p263 | 1 | T-2 MBGPRID + T-3 MBTRESN header (1) | t2_B-MB.md:101,140 |
| B | UNPARSEABLE | `domains/MH/assumptions.md:36` | ig34:p171-178 | 0 | Situation / Value of MHPRESP / Value of MHOCCUR / Value of M | t2_B-MH_review.md:34; t2_B-MH_audit.md:70 |
| A | DIFF | `domains/MI/examples.md:50` | ig34:p267 | 1 | T-1 MIDRVL header (1) | t2_B-MI.md:35 |
| B | UNPARSEABLE | `domains/ML/examples.md:14` | ig34:p121-124 | 0 | Type /  /  / If Nutritional Drink, Volume (ounces) / Start D | t2_B-ML_review.md:35-41 |
| B | UNPARSEABLE | `domains/ML/examples.md:25` | ig34:p121-124 | 0 | Type / Occurrence /  / If yes, Date | t2_B-ML_review.md:35-41 |
| B | UNPARSEABLE | `domains/ML/examples.md:52` | ig34:p121-124 | 0 | Group / Arms / Details | t2_B-ML_review.md:35-41 |
| A | DIFF | `domains/ML/examples.md:63` | ig34:p124 | 1 | T-1 WHTE MILK (1) | t2_B-ML.md:39 |
| A | DIFF | `domains/MS/examples.md:21` | ig34:p257 | 1 | T-1 MSSTRESC r9 (1) | t2_B-MS.md:60 |
| A | DIFF | `domains/MS/examples.md:78` | ig34:p262 | 2 | T-3 IDVAR MBREFID->MSREFID (2) | t2_B-MS.md:125,127 (final; :62 superseded) |
| B | UNPARSEABLE | `domains/NV/assumptions.md:19` | ig34:p294-298 | 0 | Variable Name / Variable Label / Type / Controlled Terms, Co | t2_B-NV_review.md:37; t2_B-NV_audit.md:34 |
| A | DIFF | `domains/NV/examples.md:15` | ig34:p296 | 1 | T-2 NVSTRESN (1) | t2_B-NV.md:46 |
| A | DIFF | `domains/OE/examples.md:121` | ig34:p304 | 1 | T-1 IDVARAL header (1) | t2_B-OE.md:85 |
| A | DIFF | `domains/OE/examples.md:140` | ig34:p304 | 4 | T-2 OCCULAR x4 (4) | t2_B-OE.md:86 |
| A | DIFF | `domains/PC/examples.md:75` | ig34:p277 | 1 | T-1 IDVAR PPGRPID (1) | t2_B-PCPP.md:72 |
| A | DIFF | `domains/PC/examples.md:89` | ig34:p278 | 2 | T-2/T-3 RDOMAIN (2) | t2_B-PCPP.md:73-74 |
| B | NO_PDF | `domains/PP/examples.md:54` | ig34:p271-283 | 0 | NO_PDF: PDF p274 垂直居中 (PDF_UNPARSED); 人工逐格 (checkpoint 当时行号 :56); 已登记偏差 T-5 r6/r7 PPSEQ (t2_B-PCPP.md:76) | t2_B-PCPP.md:53,85; t2_B-PCPP_review.md:33 |
| B | DIFF | `domains/PP/examples.md:68` | ig34:p274 | 35 | 35 diffs = T-6 表头 RDOMAIN 1 + 解析器列错位 34 (居中表), 人工逐格一致 | t2_B-PCPP.md:77,84; t2_B-PCPP_review.md:34,56 |
| B | UNPARSEABLE | `domains/PP/examples.md:120` | ig34:p271-283 | 0 | Method / Cardinality / PC-side IDVAR / PP-side IDVAR | t2_B-PCPP_review.md:36 (KB_AUTHORED Method 映射表, 对 p275 方法列表) |
| B | UNPARSEABLE | `domains/RS/assumptions.md:46` | ig34:p329-339 | 0 | RSTESTCD / RSTEST / RSCAT / RSORRES / RSSTRESC | t2_B-RS_review.md:53 |
| A | DIFF | `domains/RS/examples.md:57` | ig34:p336 | 1 | T-1 REPSONSE (1) | t2_B-RS.md:41 |
| B | NO_PDF | `domains/SC/examples.md:32` | ig34:p339-342 | 0 | NO_PDF: PDF p342 垂直居中 (PDF_UNPARSED); 人工逐格 (checkpoint 当时行号 :34) | t2_B-SC.md:27; t2_B-SC_review.md:31 |
| A | DIFF | `domains/SM/examples.md:37` | ig34:p86 | 1 | T-1 CESEQ (1) | t2_B-SM.md:23,40 |
| A | DIFF | `domains/SR/examples.md:14` | ig34:p378 | 1 | T-1 BAU mL (1) | t2_B-SR.md:12 |
| B | NO_PDF | `domains/SUPPQUAL/examples.md:24` | ig34:p431-434 | 0 | NO_PDF: PDF p434 例标题缺编号致未配对; 44 格人工逐格一致 (ch08:241 同表 census OK) | t2_B-SUPPQUAL.md:34 |
| B | UNPARSEABLE | `domains/TA/assumptions.md:31` | ig34:p382-402 | 0 | Concept / Definition | t2_B-TA_review.md:55 |
| B | UNPARSEABLE | `domains/TA/examples.md:141` | ig34:p382-402 | 0 |  / Screen / Run-in / Treatment | t2_B-TA_review.md:64,71 |
| B | UNPARSEABLE | `domains/TA/examples.md:325` | ig34:p382-402 | 0 |  / Screen / First Treatment / First Rest / Second Treatment  | t2_B-TA_review.md:64,71 |
| B | UNPARSEABLE | `domains/TA/examples.md:495` | ig34:p382-402 | 0 |  / Screen / Double Blind / Open Label | t2_B-TA_review.md:64,71 |
| B | UNPARSEABLE | `domains/TA/examples.md:667` | ig34:p382-402 | 0 |  / Screen / Treatment /  /  /  /  /  /  /  / Follow-up | t2_B-TA_review.md:64,71 |
| B | UNPARSEABLE | `domains/TA/examples.md:753` | ig34:p382-402 | 0 |  / Screen / Treatment /  /  /  /  /  / Follow-up | t2_B-TA_review.md:64,71 |
| B | UNPARSEABLE | `domains/TA/examples.md:835` | ig34:p382-402 | 0 |  / Screen / Treatment /  /  /  /  /  /  /  / Follow-up | t2_B-TA_review.md:64,71 |
| B | UNPARSEABLE | `domains/TA/examples.md:976` | ig34:p382-402 | 0 |  / Screen / Induction /  / Continuation /  /  /  /  / Follow | t2_B-TA_review.md:64,71 |
| B | UNPARSEABLE | `domains/TE/examples.md:79` | ig34:p402-407 | 0 | Step / Step question / How step question is answered by info | t2_B-TE_review.md:36,39 |
| A | DIFF | `domains/TR/examples.md:17` | ig34:p355/356 | 32 | T-1 Row/TRSEQ 跳号 (32) | t2_B-TR.md:67; t2_B-TR_review.md:21 |
| A | DIFF | `domains/TR/examples.md:68` | ig34:p356/357/358 | 1 | T-2 TRSTRESC -60 (1) | t2_B-TR.md:68 |
| B | UNPARSEABLE | `domains/TS/assumptions.md:45` | ig34:p417-425 | 0 | TSSEQ / TSGRPID / TSPARMCD / TSPARM / TSVAL | t2_B-TS_review.md:75 (:45), :55 (:75) |
| B | UNPARSEABLE | `domains/TS/assumptions.md:75` | ig34:p417-425 | 0 | Rank / Code / Display Name / Definition | t2_B-TS_review.md:75 (:45), :55 (:75) |
| A | DIFF | `domains/TS/examples.md:74` | ig34:p421/422 | 1 | T-1 Trial Type->Title (1) | t2_B-TS.md:56 |
| B | UNPARSEABLE | `domains/TU/assumptions.md:38` | ig34:p344-358 | 0 | TULNKID / TUTESTCD / TUTEST / TUORRES / VISIT | t2_B-TU_review.md:39,59 |
| B | UNPARSEABLE | `domains/TU/assumptions.md:56` | ig34:p344-358 | 0 | TULNKID / TUTESTCD / TUTEST / TUORRES / TULOC / TUMETHOD | t2_B-TU_review.md:39,59 |
| B | UNPARSEABLE | `domains/TU/assumptions.md:80` | ig34:p344-358 | 0 | TULNKID / TUTESTCD / TUTEST / TUORRES / TULOC / TUMETHOD | t2_B-TU_review.md:39,59 |
| B | UNPARSEABLE | `domains/TU/assumptions.md:88` | ig34:p344-358 | 0 | TULNKID / TUTESTCD / TUTEST / TUORRES / TUSTAT / TULOC / TUM | t2_B-TU_review.md:39,59 |
| B | UNPARSEABLE | `domains/TU/assumptions.md:98` | ig34:p344-358 | 0 | TUREFID / TULNKID / TUTESTCD / TUTEST / TUORRES / TULOC / TU | t2_B-TU_review.md:39,59 |
| B | UNPARSEABLE | `domains/TU/assumptions.md:109` | ig34:p344-358 | 0 | QNAM / QLABEL / Definition | t2_B-TU_review.md:39,59 |
| B | UNPARSEABLE | `chapters/ch03_submitting_data.md:22` | ig34:p17-21 | 0 | Dataset / Description / Class / Structure / Purpose / Keys / | t2_B-ch03_review.md:54 |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:52` | ig34:p22-59 | 0 | Core Value / Meaning / Rule | KB_AUTHORED D6 Core 表, 无 PDF 对应; t2_B-ch04_review_a3.md M4 落实 (p23 渲染) |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:223` | ig34:p22-59 | 0 | SPDEVID / MKTESTCD / MKTEST / MKLOC / MKLAT / MKMETHOD / QNA | t2_B-ch04_audit.md:127 (p28 渲染); review_a3 H2 |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:421` | ig34:p22-59 | 0 | CMINDC | t2_B-ch04_audit.md:128 (p32 渲染) |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:425` | ig34:p22-59 | 0 | QNAM / QLABEL / QVAL | t2_B-ch04_audit.md:128 (p32 渲染) |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:431` | ig34:p22-59 | 0 | CMINDC | t2_B-ch04_audit.md:128 (p32 渲染) |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:435` | ig34:p22-59 | 0 | QNAM / QLABEL / QVAL | t2_B-ch04_audit.md:128 (p32 渲染) |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:443` | ig34:p22-59 | 0 | CMINDC | t2_B-ch04_audit.md:128 (p32 渲染) |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:770` | ig34:p22-59 | 0 | # / Date and Time as Originally Recorded / Level of Uncertai | t2_B-ch04_audit.md:129 (p40 渲染) |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:825` | ig34:p22-59 | 0 | Duration as originally recorded / ISO 8601 Duration | t2_B-ch04_audit.md:126 (p41 渲染); review_a3 H1 |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:901` | ig34:p22-59 | 0 | USUBJID / VISIT / VISITNUM / VISITDY / LBDY | t2_B-ch04_audit.md:33 (p42 lb.xpt 渲染) |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:921` | ig34:p22-59 | 0 | Variable / Allowable Values / Purpose | KB_AUTHORED D6 --STRF 表, 无 PDF 对应; review_a3 M5/M6 落实 (p43 渲染) |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:942` | ig34:p22-59 | 0 | Variable / Allowable Values / Purpose | KB_AUTHORED D6 --STRTPT 表, 无 PDF 对应; review_a3 M5/M6 落实 (p44 渲染) |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:1057` | ig34:p22-59 | 0 | Variable / Purpose | KB_AUTHORED D6 (§4.4.10 图的 KB 表达), 无 PDF 表对应 |
| A | DIFF | `chapters/ch04_general_assumptions.md:1328` | ig34:p53/54 | 2 | T-1 eg.xpt Row 5/6 (2) | t2_B-ch04.md:70; t2_B-ch04_review.md:37 |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:1450` | ig34:p22-59 | 0 | Convention / Text Strings >200 Char Conventions General Obse | t2_B-ch04_audit.md:33 (p56 约定表渲染) |
| B | UNPARSEABLE | `chapters/ch04_general_assumptions.md:1545` | ig34:p22-59 | 0 | Variable / Structure Where It Is Defined / Requirement in Th | t2_B-ch04_audit.md:130 (p59 渲染) |
| B | UNPARSEABLE | `chapters/ch08_relationships.md:86` | ig34:p427-440 | 0 | Variable Name / Variable Label / Type / Controlled Terms, Co | t2_B-ch08_review.md:53,70-74 |
| B | UNPARSEABLE | `chapters/ch08_relationships.md:197` | ig34:p427-440 | 0 | Variable Name / Variable Label / Type / Controlled Terms, Co | t2_B-ch08_review.md:53,70-74 |
| B | UNPARSEABLE | `chapters/ch08_relationships.md:319` | ig34:p427-440 | 0 | Question / Interpretation of Answers | t2_B-ch08_review.md:53,70-74 |
| B | UNPARSEABLE | `chapters/ch08_relationships.md:351` | ig34:p427-440 | 0 | Variable Name / Variable Label / Type / Controlled Terms, Co | t2_B-ch08_review.md:53,70-74 |
| B | UNPARSEABLE | `chapters/ch08_relationships.md:420` | ig34:p427-440 | 0 | Variable Name / Variable Label / Type / Controlled Terms, Co | t2_B-ch08_review.md:53,70-74 |
| B | UNPARSEABLE | `model/01_concepts_and_terms.md:176` | sv20:p8-10 | 0 | Subclass / Purpose / Examples | t2_B-model01_review.md:45 |
| B | UNPARSEABLE | `model/05_study_level_data.md:35` | sv20:p51-63 | 0 | # / Variable / Label / Type / Role | t2_B-model05_review.md:80-94 (触碰 4 表渲染, 其余 layout+原子 5 列核) |
| B | UNPARSEABLE | `model/05_study_level_data.md:53` | sv20:p51-63 | 0 | # / Variable / Label / Type / Role | t2_B-model05_review.md:80-94 (触碰 4 表渲染, 其余 layout+原子 5 列核) |
| B | UNPARSEABLE | `model/05_study_level_data.md:74` | sv20:p51-63 | 0 | # / Variable / Label / Type / Role | t2_B-model05_review.md:80-94 (触碰 4 表渲染, 其余 layout+原子 5 列核) |
| B | UNPARSEABLE | `model/05_study_level_data.md:99` | sv20:p51-63 | 0 | # / Variable / Label / Type / Role / Notes | t2_B-model05_review.md:80-94 (触碰 4 表渲染, 其余 layout+原子 5 列核) |
| B | UNPARSEABLE | `model/05_study_level_data.md:117` | sv20:p51-63 | 0 | # / Variable / Label / Type / Role / Notes | t2_B-model05_review.md:80-94 (触碰 4 表渲染, 其余 layout+原子 5 列核) |
| B | UNPARSEABLE | `model/05_study_level_data.md:144` | sv20:p51-63 | 0 | # / Variable / Label / Type / Role | t2_B-model05_review.md:80-94 (触碰 4 表渲染, 其余 layout+原子 5 列核) |
| B | UNPARSEABLE | `model/05_study_level_data.md:164` | sv20:p51-63 | 0 | # / Variable / Label / Type / Role | t2_B-model05_review.md:80-94 (触碰 4 表渲染, 其余 layout+原子 5 列核) |
| B | UNPARSEABLE | `model/05_study_level_data.md:182` | sv20:p51-63 | 0 | # / Variable / Label / Type / Role | t2_B-model05_review.md:80-94 (触碰 4 表渲染, 其余 layout+原子 5 列核) |
| B | UNPARSEABLE | `model/05_study_level_data.md:196` | sv20:p51-63 | 0 | # / Variable / Label / Type / Role | t2_B-model05_review.md:80-94 (触碰 4 表渲染, 其余 layout+原子 5 列核) |
| B | UNPARSEABLE | `model/05_study_level_data.md:215` | sv20:p51-63 | 0 | # / Variable / Label / Type / Role | t2_B-model05_review.md:80-94 (触碰 4 表渲染, 其余 layout+原子 5 列核) |
| B | UNPARSEABLE | `model/05_study_level_data.md:235` | sv20:p51-63 | 0 | # / Variable / Label / Type / Role | t2_B-model05_review.md:80-94 (触碰 4 表渲染, 其余 layout+原子 5 列核) |
| B | UNPARSEABLE | `model/05_study_level_data.md:267` | sv20:p51-63 | 0 | # / Variable / Label / Type / Role | t2_B-model05_review.md:80-94 (触碰 4 表渲染, 其余 layout+原子 5 列核) |
| B | UNPARSEABLE | `model/05_study_level_data.md:305` | sv20:p51-63 | 0 | # / Variable / Label / Type / Role | t2_B-model05_review.md:80-94 (触碰 4 表渲染, 其余 layout+原子 5 列核) |
| B | UNPARSEABLE | `model/06_relationship_datasets.md:33` | sv20:p64-69 | 0 | # / Variable / Label / Type / Role / Notes | t2_B-model06_review.md:33-87 (:50/:190 = KB_AUTHORED D6 表, 无 PDF 对应) |
| B | UNPARSEABLE | `model/06_relationship_datasets.md:50` | sv20:p64-69 | 0 | Source RELTYPE / Target RELTYPE / Meaning | t2_B-model06_review.md:33-87 (:50/:190 = KB_AUTHORED D6 表, 无 PDF 对应) |
| B | UNPARSEABLE | `model/06_relationship_datasets.md:71` | sv20:p64-69 | 0 | # / Variable / Label / Type / Role / Notes | t2_B-model06_review.md:33-87 (:50/:190 = KB_AUTHORED D6 表, 无 PDF 对应) |
| B | UNPARSEABLE | `model/06_relationship_datasets.md:101` | sv20:p64-69 | 0 | # / Variable / Label / Type / Role | t2_B-model06_review.md:33-87 (:50/:190 = KB_AUTHORED D6 表, 无 PDF 对应) |
| B | UNPARSEABLE | `model/06_relationship_datasets.md:118` | sv20:p64-69 | 0 | # / Variable / Label / Type / Role | t2_B-model06_review.md:33-87 (:50/:190 = KB_AUTHORED D6 表, 无 PDF 对应) |
| B | UNPARSEABLE | `model/06_relationship_datasets.md:136` | sv20:p64-69 | 0 | # / Variable / Label / Type / Role | t2_B-model06_review.md:33-87 (:50/:190 = KB_AUTHORED D6 表, 无 PDF 对应) |
| B | UNPARSEABLE | `model/06_relationship_datasets.md:155` | sv20:p64-69 | 0 | # / Variable / Label / Type / Role | t2_B-model06_review.md:33-87 (:50/:190 = KB_AUTHORED D6 表, 无 PDF 对应) |
| B | UNPARSEABLE | `model/06_relationship_datasets.md:173` | sv20:p64-69 | 0 | # / Variable / Label / Type / Role / Notes | t2_B-model06_review.md:33-87 (:50/:190 = KB_AUTHORED D6 表, 无 PDF 对应) |
| B | UNPARSEABLE | `model/06_relationship_datasets.md:190` | sv20:p64-69 | 0 | Dataset / Code / Purpose / Subject-level? | t2_B-model06_review.md:33-87 (:50/:190 = KB_AUTHORED D6 表, 无 PDF 对应) |
| B | PDF_UNPARSED | - | ig34:p[274] | 0 | vertically centred cells; KB 侧 = domains/PP/examples.md:54 (NO_PDF, 同一张表) | t2_B-PCPP.md:53; t2_B-PCPP_review.md:33 |
| B | PDF_UNPARSED | - | ig34:p[342] | 0 | vertically centred cells; KB 侧 = domains/SC/examples.md:32 (NO_PDF, 同一张表) | t2_B-SC_review.md:31 |

## 7. 局限

- PDF_ONLY = 1 是下界: 解析器读不出表头的 PDF 表 (如 CP Ex9 `ROW` 大写表头) 既不进 `pdf_only` 也不进 `pdf_unparsed`; 若其 KB 副本缺失, census 不会报. 覆盖检查只证明 KB 侧 Row 表全在 manifest 内.
- model/05 未触碰表的 B 依据是 layout 文本 + 原子 5 列核, 非渲染逐格.
- C2 (p431) 的配对机制 (p430/p431 同键冲突) 为推断; 可靠事实是两份 KB 副本均以 OK 配到 p431.
- 分诊证据靠 grep + 人工阅读 checkpoint, 未对 A/B 类再做独立渲染复核 (各批 reviewer 已做).
- `t2_B-MS.md:60` 提到 MB/examples.md 的 Ex1 ms.xpt 副本 r9 MSSTRESC 为空 (与 MS:31 不一致): 现 MB/examples.md 已无 MSSTRESC 列 (`grep -n MSSTRESC knowledge_base/domains/MB/examples.md` 0 行), 该项已消解.
