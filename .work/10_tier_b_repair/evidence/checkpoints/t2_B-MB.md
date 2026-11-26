# T2 B-MB writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `97e18955346a42d29b1528c78d1d4b8d332d8137`
- md5 before: MB/examples.md `4b1b114278ffd5a5be5f2b1222ffdcd6` (400 行)
- md5 after: MB/examples.md `64747953f6d24d1bd42604b572efde79` (305 行)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-MB_writer/` (examples.base.md 原件, build.py 构建脚本, census_before/after.json, fp_after/regress.jsonl, p256-p263 渲染 130dpi)
- 规则优先级: 批次 `notes[0]` "两份都按 PDF 修, 都不删" 与 writer prompt 规则 4 已被 **D2 (t1_user_ack.md:14)** 取代 → MB 留一份按 PDF 逐格修, 另一份删除. reviewer 读到的 batch notes 是旧口径.
- 不留交叉引用: D2 原文对 MB 只说 "留一份"; 交叉引用仅用于 PP 跨文件情形. 两份同在一个文件, 删后无需指针.
- 保留副本选择: **副本 2 (base :171-400)** — 位于 PDF 节标题 `## §6.3.5.7.3 …` 下, 独有 Ex1/Ex2 的 ms.xpt 与 Ex4, Ex1-2 叙述更贴 PDF (副本 1 Ex1 叙述有改写/乱序, Ex2 be.xpt USUBJID/日期错, Ex2 mb.xpt 列错位, Ex2 suppmb IDVAR 错, Ex3 be.xpt 2 格错).
  副本 1 独有且 PDF 有的块 (RELSPEC 段+表 base :111-122; MB 叙述+Row 1-6 说明+mb.xpt+suppmb.xpt base :140-169) → **MOVED** 进副本 2 Ex3 (按 PDF p261-262 顺序, 放在 bs.xpt 之后), 再按 PDF 修.
- 表格来源: Ex3 mb.xpt 按 p262 渲染 (130dpi) + `pdftotext -bbox` 词框 (ZIEHL/NEELSEN 分词、tuberculosis 小写、14700) 重建; di/relrec 按 p263 渲染; 其余格以 census (bbox) 与渲染图交叉核.
- 工作方式: `build.py` 对 base 行号断言后做替换/拼接 (先改副本 2, 后整体丢弃副本 1), 产物再 diff 复核.

### 变更清单

| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | MB/examples.md:261 | ig34_p0263_a001 | INSERTED | DI 句 "Data about the device used … DI domain if needed." | 263 |
| 2 | MB/examples.md:263-268 | ig34_p0263_a004 | INSERTED (整表) | `**di.xpt**` 表头 + 行 1 DEVTYPE | 263 |
| 3 | MB/examples.md:268 | ig34_p0263_a005 | INSERTED | di 行 2 TRADENAM / HAIN GENOTYPE MTBDRplus | 263 |
| 4 | MB/examples.md:270 | ig34_p0263_a006 | INSERTED | RELREC 说明句 (2 句, --LNKID/--LNKGRP; --REFID) | 263 |
| 5 | MB/examples.md:276 | ig34_p0263_a009 | INSERTED (整表) | `**relrec.xpt**` 6 行; 行 1 BE BELNKID ONE A | 263 |
| 6 | MB/examples.md:278 | ig34_p0263_a011 | INSERTED | relrec 行 3 BE BELNKID ONE B | 263 |
| 7 | MB/examples.md:280 | ig34_p0263_a013 | INSERTED | relrec 行 5 MB MBREFID ONE C | 263 |
| 8 | MB/examples.md:281 | ig34_p0263_a014 | INSERTED | relrec 行 6 MS MSREFID MANY C | 263 |
| 9 | MB/examples.md:227 | ig34_p0261_a014 | MOVED + REPLACED | (base :142) MBSPCND → MBSPCCND | 261 |
| 10 | MB/examples.md:241-248 | ig34_p0262_a003 | MOVED + TABLE_REBUILT | (base :151-158) 表头改为 PDF 24 列: MBLNKGRP 移到 MBREFID 前; 加 MBORRESU; 删 MBSPEC; MBSPCND→MBSPCCND 且移到 MBLOC 后; 全 6 行同步 | 262 |
| 11 | MB/examples.md:170 | ig34_p0260_a009 | REPLACED | Ex3 be 行 4 BEREFID 100 → 100.3 | 260 |
| 12 | MB/examples.md:176 | ig34_p0260_a015 | REPLACED | Ex3 be 行 10 BELNKID 3 → 空 | 260 |

atoms 覆盖: 12/12 (REAL_GAP 8, VALUE_DIFF 4).

### 批内追加改动 (census / R3, 非 atoms)

| # | kb_file:line (改后) | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 13 | MB/examples.md:46 | census:MB/examples.md:212 (row 3) | REPLACED | Ex1 ms 行 3 MSORRES 空→1, MSSTRESC 空→1 (渲染确认; 行 9 MSSTRESC PDF 本为空, 未动) | 257 |
| 14 | MB/examples.md:109-114 | census:MB/examples.md:277 (rows 1-6) | REPLACED | Ex2 mb VISIT "VISIT" → "VISIT 1" ×6 | 258 |
| 15 | MB/examples.md:295-296 | census:MB/examples.md:388 (rows 1-2) | REPLACED | Ex4 mb VISIT WEEK 1 → WEEK 5 ×2 | 263 |
| 16 | MB/examples.md:241-248 | (Ex3 mb 其它格) | TABLE_REBUILT | MBMETHOD r1-2 "ZIEHL-NEELSEN…" → "ZIEHL NEELSEN ACID FAST STAIN"; MBTEST r4-6 "Tuberculosis" → "tuberculosis"; r5 MBORRESU CFU / MBSTRESC 14700 (原错位为 CFU) / MBSTRESN 14700 / MBSTRESU CFU/mL; MBLOC 全 STOMACH; MBSPCCND r1-2 CONCENTRATED | 262 |
| 17 | MB/examples.md:252-259 | (Ex3 suppmb, base :162-169) | MOVED + REPLACED | r1 QVAL "Smear Quantitation" → "Smear Quantification"; r5/r6 行序按 PDF (MBSEQ 6 MBQSCAL 在前, MBSEQ 5 MBDILFCT 在后); Row 标号见 T-1 | 262 |
| 18 | MB/examples.md:208-223 | (RELSPEC, base :111-122) | MOVED | RELSPEC 说明段 + relspec.xpt 6 行 (与 p261 逐格一致, 未改值) | 261 |
| 19 | MB/examples.md:210, 212 | 新增 atom ig34_p0261_a002 / a003 | INSERTED | RELSPEC "Row 1:" / "Rows 2-6:" 说明 (两份副本均缺; ledger 判 EQUIVALENT 指向他文件) | 261 |
| 20 | MB/examples.md:225-237 | (MB 叙述 + Row 1-6, base :140-147) | MOVED | 段落逐字与 p261-262 一致; 格式由 `**Row n:**` 改为副本 2 的 `- Row n:` 列表 | 261-262 |
| 21 | MB/examples.md:30 | (base :198-200) | REPLACED (合并换行) | "…zone of inhibition" 与下段 "(MSTESTCD = "DIAZOINH")…" 是 PDF 跨页断句, 合并成一段 (规则 1 允许) | 256-257 |

新增 atom 清单 (R3): ig34_p0261_a002, ig34_p0261_a003.

### census 表处理 (before 行号 → 处理)

| census ref | 处理 | after |
|---|---|---|
| :11 Ex1 mb.xpt (副本 1, 15 diffs) | D2 删除 (D-1); 保留副本 :15 (base :183) census OK | 不存在 |
| :33 Ex2 be.xpt (副本 1, 4) | D2 删除 (D-2); 保留副本 :72 OK | 不存在 |
| :63 Ex2 mb.xpt (副本 1, 17) | D2 删除 (D-2); 保留副本 :107 修 VISIT 后 OK | 不存在 |
| :76 Ex2 suppmb.xpt (副本 1, 2) | D2 删除 (D-2); 保留副本 :120 OK | 不存在 |
| :98 Ex3 be.xpt (副本 1, 2) | D2 删除 (D-3); 保留副本 :165 修 2 格后 OK | 不存在 |
| :151 Ex3 mb.xpt (副本 1 独有, 25) | MOVED → :241, 按 PDF 重建 | OK |
| :162 Ex3 suppmb.xpt (副本 1 独有, 11) | MOVED → :252, 按 PDF 修 | DIFF 2 (Row 标号, T-1) |
| :212 Ex1 ms.xpt (2) | #13 | OK |
| :277 Ex2 mb.xpt (6) | #14 | OK |
| :335 Ex3 be.xpt (2) | atoms #11/#12 | OK |
| :388 Ex4 mb.xpt (3) | #15 VISIT; 表头 MBGPRID 见 T-2 | DIFF 1 (T-2) |
| pdf_only p263 Ex3 di.xpt (2 行) | atoms #2/#3 | 已匹配 OK |
| pdf_only p263 Ex3 relrec.xpt (6 行) | atoms #5-8 | 已匹配 OK |

- 汇总 (manifest = MB/examples.md × ig34 p248-262): before `KB 表 24: OK 13 / DIFF 11, diffs 89, 本批 PDF_ONLY: di/relrec p263 + ms/suppms p262 + lb p248×2` → after `KB 表 18: OK 16 / DIFF 2, diffs 3; PDF_ONLY 剩 ms/suppms p262 (见 范围外 O-a) + lb p248 (LB 域, 非本批)`.
- 残留 3 diffs 全为登记 PDF_TYPO (T-1 ×2, T-2 ×1).

```
S=<scratch>; python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-MB.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # status {'OK': 16, 'DIFF': 2}; diffs: 3
python3 tools/check_links.py | tail -1   # live docs: 42 (基线 42)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
```

### fp_match: regressions=11 (全部为预期, 非丢失)
ig34_p0257_a010, p0258_a019-a024, p0260_a009, p0260_a015, p0263_a021/a022 — 这 11 条 pdf_atoms 的 verbatim 是从**错的 KB 值**抄来的 (行 3 MSORRES 空 / "VISIT" 无 1 / BEREFID 100 / BELNKID 3 / WEEK 1), 与 PDF 渲染不符; KB 改成 PDF 值后自然不再命中. T3 回写 ledger 时须按 PDF 改这些 atom 的 verbatim. (new_hits=67 含并行批 B-TR 的改动, 未拆分.)

### 删除清单 (D2 去重, reviewer 逐条确认)

| # | 原位置 (base 行号) | 内容 | 保留副本 (改后行号) | 备注 |
|---|---|---|---|---|
| D-1 | MB/examples.md:3-24 | 副本 1 `## Example 1`: 叙述 2 段, mb.xpt (列错, MBORRES=PRESENT 等 14 格错), relrec 句+表 | :5-62 (Ex1 叙述、mb :13、ms :40、relrec :57) | 副本 1 无 ms.xpt |
| D-2 | MB/examples.md:25-79 | 副本 1 `## Example 2`: 叙述, be (USUBJID ABC-01-001 / 07-01 错), SUPPBE 段+表, Rows 说明, mb (多 MBSPEC 列错位), suppmb (IDVAR MBSEQ 错) | :64-145 | — |
| D-3 | MB/examples.md:80-110 | 副本 1 `## Example 3` 叙述 3 段 + Row 说明 + be (2 格错) | :147-176 | base :86 末句 "MBGRPID is used to connect … rows 5-7." 是 KB 把 p261 Row 4 句误挂到 Ex3 引言 (D2 删扩写), 原文保留在 :233 Row 4 |
| D-4 | MB/examples.md:123-139 | 副本 1 BS 说明 + bs.xpt | :195-206 | 两份一致 |
| M-1 | MB/examples.md:111-122 | RELSPEC 段 + 表 | **MOVED** → :208-223 | 非删除 |
| M-2 | MB/examples.md:140-170 | MB 叙述 + Row 1-6 + mb.xpt + suppmb.xpt | **MOVED** → :225-259 (按 PDF 修) | 非删除 |

- 被删的标题: 副本 1 的 `## Example 1/2/3` (锚点 #example-1/2/3). 全仓 grep 无指向 MB/examples.md 锚点的链接 (只有 INDEX.md 文件级链接); 删除后副本 2 的 `### Example n` 锚点由 #example-n-1 变为 #example-n. check_links live docs 42 不变.
- base :1-2 (`# MB — Examples` + 空行) 保留.

### PDF_TYPO 清单 (KB 保留合理值)

| # | 位置 | PDF | KB (保留) | 理由 |
|---|---|---|---|---|
| T-1 | MB/examples.md:258-259 Ex3 suppmb Row 列 | 1,2,3,4,**7,8** (渲染确认) | 5, 6 | PDF Row 标号跳号 (同 TR 跳 Row 12 一类); 行内容与行序已按 PDF |
| T-2 | MB/examples.md:293 Ex4 mb 表头 | MBGPRID | MBGRPID | 变量名拼写错, 标准变量为 MBGRPID |
| T-3 (候选, 未改) | MB/examples.md:293 Ex4 mb 表头 | MBTRESN | MBTRESN (KB 已照 PDF) | 疑为 MBSTRESN 笔误; KB 与 PDF 一致, census 不报; 主控/用户定是否改 |
| T-4 (候选, 未改) | MB/examples.md:225 Ex3 MB 叙述 "The sputum sample was aliquoted 5 times" | 原文如此 | 照录 | Ex3 实为胃灌洗液 (lavage fluid) 样本, PDF 原文写 sputum; 不改 |

### 范围外发现 (未改, 主控定)

- O-a: PDF p262 Ex3 的 MS 段 (说明段 + Rows 1-2 / 3-4 + ms.xpt + suppms.xpt) 不在 MB/examples.md, 现存于 MS/examples.md Ex3 (B-MS 批). 但 MB/examples.md Ex1/Ex2 都带 ms.xpt, Ex3 没有 → 本文件 :261 DI 句里 "rows 3-4 of the MS dataset example" 在本文件内无对应表. 未补 (不在 atoms / pdf_only 清单, 且与 D2 去重方向冲突), 也未加指针 (自造文字). census 仍报 p262 ms/suppms PDF_ONLY (manifest 只含 MB 文件所致).
- O-b: MB/examples.md Ex1/Ex2 的 ms.xpt 与 MS/examples.md Ex1/Ex2 是跨文件重复 (O9 同类); MS/examples.md Ex2 r10 可见 SUSCEPTIBLE / 2005-07-01 等疑错值 (未核, B-MS 批).
- O-c: 副本 2 Ex1 叙述 (:7-11, :20-28) 把 PDF 一段拆成多段, 仅格式差, 未动.
- O-d: :232 (Row 4 说明) "rows 5-7" 与表只有 6 行 — PDF 原文如此, 照录.

### 触碰过的 unparseable 表
- 无 (本批 `unparseable_kb_tables_hand_check_if_touched` 为空). Ex3 mb.xpt 为整表重建, reviewer 须对 p262 渲染逐格人工复核 (dispatch notes: 新建/重建表须独立方法核).

### git diff --stat -- kb_files
```
 knowledge_base/domains/MB/examples.md | 269 +++++++++++-----------------------
 1 file changed, 87 insertions(+), 182 deletions(-)
```

### 更正 (attempt 1, 交付前自查)
- O-d 行号 :232 → **:233** (Row 4 说明). D-4 保留副本范围 :195-206 → **:191-206** (BS 说明段起于 :191).
- writer.jsonl: ig34_p0261_a014 action 记为 `REPLACED` (VALUE_DIFF; 随 M-2 块移动, 见 note). census 副本删除项 action `DELETED_D2` 不在 prompt 枚举内, 沿用 B-TR 已用写法 (t3_recompute.py 不按 action 取值).
- 新增 atom ID 已核: `pdf_atoms.jsonl` 中 ig34_p0261_a002 / a003 verbatim 即 RELSPEC "Row 1:" / "Rows 2-6:" 两句.
- fp_match 表述更正: 实测为 "这 11 条 atom verbatim 与 PDF 渲染不符、且与 base KB 对应行逐字相同"; "抄自 KB" 为推断.
- 交叉引用: 按 t1_user_ack D2 对 MB 的文字 ("留一份") 未留指针; writer 规则 5 字面要求另一份替换为交叉引用 → **请主控确认** (同文件内副本, 留指针意义不大).
- 协调: `work/t2_batches/*.json` 中只有 B-MB.json 引用 MB/examples.md 行号或 p263 di/relrec 原子; 其它批不受行号漂移影响.

## attempt 1 续 (2026-11-26, reviewer PASS 后主控裁定)

- md5 after (续): MB/examples.md `8dd0a3281433fd51392fd5a7aa62f937` (307 行). 行号漂移: 改后 ≥ :261 的行一律 +2 (DI 句现 :263, di.xpt :265-270, RELREC 句 :272, relrec :274-283, Ex4 标题 :285, Ex4 mb 表头 :295, Ex4 行 :297-298, suppmb :302-304).

| # | kb_file:line (改后) | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 22 | MB/examples.md:261 | 裁定 1 / O-a | INSERTED (KB_AUTHORED 纯导航) | DI 句前加 `> See [MS Example 3](../MS/examples.md#example-3) …`; 锚点按 MS/examples.md:52 `## Example 3` 校准 | 262 |
| 23 | MB/examples.md:295 | 裁定 2 / T-3 | REPLACED | Ex4 表头 MBTRESN → MBSTRESN | 263 |

### PDF_TYPO 更新
- T-1 维持 (suppmb Row 5/6, PDF 7/8).
- **T-3 (正式)**: p263 Ex4 mb.xpt 表头 PDF 文本层字形为 `MBTRESN` (`pdftotext -bbox` 词框 xMin≈606, 与 MBSTRESU 相邻); MB/spec.md 无 MBTRESN 变量, 有 MBSTRESN (:167), 同表行 2 该列值 87 = MBSTRESC 数值 → PDF 印刷错, KB 改为 MBSTRESN 并登记. 与 T-2 (MBGPRID→保留 MBGRPID) 同口径.
- T-4 维持候选 (叙述 "sputum", 照录).

### 重跑
- census (MB): KB 表 18, OK 16 / DIFF 2, diffs 3 — 残留 = :252 suppmb Row 标号 ×2 (T-1) + :295 表头 1 项 (含 MBGPRID T-2 / MBTRESN T-3 两列).
- fp_match: regressions=12 = 原 11 条 ATOM_ERR + **ig34_p0263_a020** (Ex4 表头 atom, verbatim 含 MBTRESN; 因 T-3 改值后不再命中, 同属预期). new_hits=122 (含并行批).
- check_links: live docs 42 (不变).
