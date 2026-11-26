# T2 B-PCPP writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `302ec4ca092f324b84b4051a7ffc880d610d902e`
- md5 before: PC/assumptions.md `6bff67c80858685b5fb67004c5169099`; PC/examples.md `22d5b907527d224941e219d830649405`; PP/examples.md `63377a3b4fa9204dbc262d48bb3c713d`
- md5 after: PC/assumptions.md `241c819f3e0e6faeeeb441e5e9342f9a`; PC/examples.md `6d4a088248f3ff2581843dbcdfca7676`; PP/examples.md `f54cf08f95636c49d5270beb22089f95`
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_BPCPP_writer/` (按主控派发指定; 含 census_before/after.json, pc_ex1.txt / pp_ex1.txt bbox 解析, 渲染图)
- 规则优先级: writer prompt 规则 4 / 批次 notes "两份都不删" 已被 D2 (t1_user_ack) 取代 → 按 D2 去重.
- 表格数据来源: PC Ex1 / PP Ex1 用 `table_census.parse_pdf` (bbox) 生成, 再与 `pdftotext -layout` 文本逐行 + pdftoppm 渲染 (p270 300dpi 局部、p273、p274、p277) 独立核对; 未用 atom verbatim (A854134 / 行 27 PCREFID 等有误).

### 变更清单

| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | PC/examples.md:5-46 | ig34_p0270_a012 | TABLE_REBUILT | 无 → 新增 `## PC – Examples` / `### Example 1` / `**pc.xpt**` + 32 行 31 列表 | 270 |
| 2 | PC/examples.md:15 | ig34_p0270_a013 | TABLE_REBUILT | 行 1 (DRGA_MET PREDOSE PLASMA) 随整表补 | 270 |
| 3 | PC/examples.md:16 | ig34_p0270_a014 | TABLE_REBUILT | 行 2 | 270 |
| 4 | PC/examples.md:25 | ig34_p0270_a023 | TABLE_REBUILT | 行 11 (PCSTAT NOT DONE, PCLLOQ 空, PCULOQ 20; 渲染核) | 270 |
| 5 | PC/examples.md:41 | ig34_p0271_a007 | TABLE_REBUILT | 行 27 (PCREFID A554134-20, PCDTC 11T20:03; 原子 verbatim 错) | 271 |
| 6 | PC/examples.md:43 | ig34_p0271_a009 | TABLE_REBUILT | 行 29 | 271 |
| 7 | PC/examples.md:44 | ig34_p0271_a010 | TABLE_REBUILT | 行 30 | 271 |
| 8 | PC/examples.md:45 | ig34_p0271_a011 | TABLE_REBUILT | 行 31 (PCDTC 12T08:00) | 271 |
| 9 | PC/assumptions.md:88 | ig34_p0277_a004 | REPLACED | PPGRPID(Ex4) DY1DRGX → TMAX | 277 |
| 10 | PC/assumptions.md:89 | ig34_p0277_a005 | REPLACED | Ex4 → CMAX | 277 |
| 11 | PC/assumptions.md:90 | ig34_p0277_a006 | REPLACED | Ex4 → AUC | 277 |
| 12 | PC/assumptions.md:91 | ig34_p0277_a007 | REPLACED | PPSEQ 4→5; Ex4 → OTHER | 277 |
| 13 | PC/assumptions.md:92 | ig34_p0277_a008 | REPLACED | PPSEQ 5→6; Ex4 → OTHER | 277 |
| 14 | PC/assumptions.md:93 | ig34_p0277_a009 | REPLACED | PPSEQ 6→7; Ex4 → OTHER | 277 |
| 15 | PC/assumptions.md:94 | ig34_p0277_a010 | REPLACED | PPSEQ 7→8 | 277 |
| 16 | PC/assumptions.md:95 | ig34_p0277_a011 | REPLACED | PPSEQ 8→9 | 277 |
| 17 | PC/assumptions.md:96 | ig34_p0277_a012 | REPLACED | PPSEQ 9→10 | 277 |
| 18 | PC/assumptions.md:97 | ig34_p0277_a013 | REPLACED | PPSEQ 10→12 | 277 |
| 19 | PC/assumptions.md:98 | ig34_p0277_a014 | REPLACED | PPSEQ 11→13 | 277 |
| 20 | PC/assumptions.md:99 | ig34_p0277_a015 | REPLACED | PPSEQ 12→14 | 277 |
| 21 | PP/examples.md:112 | ig34_p0277_a003 | REPLACED | D2: PP 副本 (表头 PPRFDTC) → 一行交叉引用到 PC/assumptions.md#pc-pp--relating-records (保留副本表头本就是 PPRFTDTC) | 277 |
| 22 | PP/examples.md:9, 16-40 | MANUAL_01 | TABLE_REBUILT | :9 PPRFDTC→PPRFTDTC; 表由 Ex3 数据 (DRUGA_DAY1, ABC-123-001) → p273 24 行 (DAY1_PAR/DAY1_MET/DAY11_PAR/DAY11_MET, ABC-123-0001); 表头 PPRFTDTC | 273 |
| 23 | PC/examples.md:72-73, 91-104 | MANUAL_02 | SKIPPED_PDF_TYPO | 不改: p277 文字 (Rows 14-26 RELID 2 / DY8DRGX) 与 p278 表 (RELID 1, row26 DY1DRGX) 自相矛盾, KB 两处均照抄 PDF | 277-278 |

atoms 覆盖: 23/23.

### census 表处理

| census ref (before 行号) | 处理 | 结果 |
|---|---|---|
| PC/assumptions.md:55 pc.xpt (21 格) | 全改: PCGRPID Ex3 (r5,6,12) / Ex4 (r1-12), PCDTC r3/8/9/11/18, PCTPT r18 100→125 min; 另用 layout 文本独立复核 | OK |
| PC/assumptions.md:86 pp.xpt (15 格) | = 原子 #9-20 | OK |
| PC/examples.md:22 relrec Ex1 Method A r3 IDVAR | SKIPPED_PDF_TYPO (见下) | DIFF 1 (残留, 已登记) |
| PC/examples.md:36 relrec Ex1 Method B r13/r26 RDOMAIN | SKIPPED_PDF_TYPO | DIFF 2 (残留, 已登记) |
| PC/examples.md:236 relrec Ex3 Method A r3 IDVARVAL | DYIDRGX_A → DY1DRGX_A (现 :281) | OK |
| PP/examples.md:16 Ex1 pp.xpt (252) | = MANUAL_01 重建 | OK |
| PP/examples.md:47 supppp (NO_PDF) | 移到 Ex2 (现 :66-78), 见删除清单 D-2; row7 QORIG Collected → 空 (按 PDF 渲染) | DIFF (残留, 解析器问题, 见下) |
| PP/examples.md:68 Ex2 pp.xpt (NO_PDF / pdf_unparsed) | 表头 PPRFDTC→PPRFTDTC; 人工逐格 (p274 渲染) 其余 7 行 × 20 列一致; r6/r7 PPSEQ 见 PDF_TYPO | NO_PDF (PDF 垂直居中, 不可机检) |
| PP/examples.md:87 Ex3 pp.xpt (18) | 表头 PPRFTDTC; 16 格 PPRFTDTC 日期 (r1-7 2001-02-01T08:00, r8-16 2001-02-15T08:00); r7 PPORRESU L/h→L/hr | OK |
| PP/examples.md:112 (kb_duplicate) | D2 去重 → 交叉引用 | 表已不存在 |
| pdf_only p270-271 Ex1 pc.xpt (32 行) | 整表补入 PC/examples.md | OK (PDF_ONLY 消失) |
| pdf_only p274 Ex2 supppp (7 行) | KB 原有 (误放 Ex1) → 移至 Ex2 | 已匹配 (DIFF 见残留) |

Ex2 pp.xpt 人工逐格 (p274 渲染): 各行 STUDYID ABC-123 / DOMAIN PP / USUBJID 123-1001 / PPRFID B2222 / PPSCAT NCA / PPSPEC PLASMA / PPFAST Y / PPNOMDY 1 / PPRFTDTC 2001-02-01T12:00 一致; PPTESTCD AUCINT×3, RAAUC×2, AUCIFO, AUCIFP; PPTEST、PPCAT、PPORRES(154.1/144.5/294.7/1.07/0.52/520/510)、单位 (r4-5 空)、PPANMETH 均一致. 唯一不一致 r6/r7 PPSEQ (PDF 1/2, KB 6/7) → PDF_TYPO.

### 删除清单 (D2, reviewer 逐条确认)

| # | 原位置 (base 行号) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | PP/examples.md:110-125 (`**pp.xpt**` + 12 行 PP 共用表) | :112 `> See [PC/assumptions.md](../PC/assumptions.md#pc-pp--relating-records) for this table.` | D2: p277 PP 表两份副本; PDF 所属节 §6.3.5.9.3 "PC-PP – Relating Records" 在 PC/assumptions.md | PC/assumptions.md:84-99 (已按 PDF 逐格修, census OK). 标题 `## Pharmacokinetic Parameters (PP) Dataset for All Examples` 与 :110 KB 自写说明句保留未动 |
| D-2 | PP/examples.md:43-55 (SUPPPP 引句 + `**supppp.xpt**` + 7 行表, 位于 Ex1) | :43 `> See [Example 2](#example-2) for this table (...)`; 原文整体移到 Ex2 :66-78 | PDF p274 SUPPPP 属 Example 2 (census pdf_only p274 ex2); 采 D2 "保留所属节, 另处一行引用" 处理. **需主控确认**: 严格说这是 RELOCATE (不在 atoms / delete_only_source_lines), 按 D2 套用 | PP/examples.md:66-78 |

### PDF_TYPO 清单 (KB 保留合理值, 不改)

| # | 位置 | PDF | KB (保留) | 理由 |
|---|---|---|---|---|
| T-1 | PC/examples.md:67 (Ex1 Method A r3) | RDOMAIN PC + IDVAR PPGRPID + DY8_DRGX | IDVAR PCGRPID | PCGRPID 值配 PPGRPID 变量自相矛盾 |
| T-2 | PC/examples.md:91 (Method B r13) | RDOMAIN PC, IDVAR PPGRPID | RDOMAIN PP | 同上 |
| T-3 | PC/examples.md:104 (Method B r26) | RDOMAIN PC, IDVAR PPGRPID | RDOMAIN PP | 同上 |
| T-4 | MANUAL_02 PC/examples.md:72-73 vs 91-104 | p277 文字 RELID 2/DY8DRGX vs p278 表 RELID 1/DY1DRGX | 两处均照 PDF 原样 | PDF 自身文字与表矛盾, KB 不能单方面裁 |
| T-5 | PP/examples.md:63-64 (Ex2 r6/r7 PPSEQ) | 1 / 2 (渲染确认) | 6 / 7 | 同受试者 PPSEQ 重复无效; SUPPPP IDVARVAL 1-7 支持 6/7 |
| T-6 | PP/examples.md:70 SUPPPP 表头 | DOMAIN | RDOMAIN | SUPPQUAL 标准变量为 RDOMAIN |
| T-7 (候选, 已按 PDF 写入) | PP/examples.md:18, 21 PPSTRESU | `H` (渲染确认大写) | 写入 `H` (verbatim) | 与同列 `h` 不一致, 疑 PDF 笔误; 整表新建无"KB 合理值"可保留, 故照录并登记, 主控可裁改 `h` |
| T-8 (候选, 未改) | PC/examples.md:272-273 散文 `DYIDRGX_A` / `DYIDRGX_HALF` | p280 文本层即为 DYIDRGX (I 非 1) | 散文照 PDF 保留; 表格 :281 已改 DY1DRGX_A | PDF 散文与表不一致 |

### 残留 (census_after, 本批 3 文件; 命令见下)

- PC/examples.md:63 relrec DIFF 1 (T-1), :77 relrec DIFF 2 (T-2/T-3) — 均为登记 PDF_TYPO.
- PP/examples.md:70 supppp DIFF: 表头 RDOMAIN (T-6) + 34 格 — 后者为 census 解析器在该居中对齐表上列错位 (`IDVARVAL` 读成 "1 PKCOND" 等), 渲染逐格核对 KB 7 行值与 PDF 一致 (row7 QORIG 已按 PDF 置空). 非 KB 错.
- PP/examples.md:56 Ex2 pp.xpt NO_PDF (PDF 垂直居中不可机检) — 已人工逐格, 见上.
- PP/examples.md:122 UNPARSEABLE (KB Method 映射表, 未触碰).
- PDF_ONLY 落在 pdf_ranges 内的只剩 p267 mi.xpt / suppmi.xpt (MI 域, 非本批).
- 汇总: before `OK 13 / DIFF 8 / NO_PDF 2 / UNPARSEABLE 1, diffs 311, 本批页 PDF_ONLY 2` → after `OK 19 / DIFF 3 / NO_PDF 1 / UNPARSEABLE 1, diffs 38, 本批页 PDF_ONLY 0`.

```
S=<scratch>; python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-PCPP.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
python3 tools/check_links.py | tail -1   # live docs 42 (改前 42, git stash 实测)
```

### 范围外发现 (未改, 主控定)

- O-a: **PC Ex1 叙述段缺失** (p270 a001-a011: Example 1 标题后两段 + Rows 1-2 … 21-30 说明 + pc.xpt). coverage_ledger 标 EXACT 是旧版 KB (md_dmPC_ex_a004-014 指向已不存在的行), 当前 KB 全无 → 实为 REAL_GAP, 未进 atoms. 本次只补了标题 + 表; 建议追加原子补叙述 (插入点 PC/examples.md:9 (### Example 1) 与 :11 (**pc.xpt**) 之间).
- O-b: PP/examples.md:82 (Ex3 叙述) 两处 `PPRFDTC`, PDF p274 为 PPRFTDTC.
- O-c: PP/examples.md:3 / :110 / :116-179 KB 自写的速查/摘要段 (非 PDF 原文); :110 说明 "contains 12 rows…" 现指向交叉引用; :174-179 "Cross-domain summary" 页码与内容疑与 PDF 不符 (如 Example 3 写成 PCSEQ+PPGRPID). 未核未改.
- O-d: Ex1 SUPPPP 在 KB 原处有 `**supppp.xpt**` 标题行, PDF p274 无该标题; 随移保留.
- O-e: PC/examples.md:5 新增 `## PC – Examples` 使旧 "### Example 1" (§6.3.5.9.3) 锚点由 #example-1 变 #example-1-1; 全仓 grep 无指向 PC/PP examples 锚点的链接, check_links live docs 不变.

### 触碰过的 unparseable 表
- 无 (PP/examples.md:122 Method 映射表未改). Ex2 pp.xpt (pdf_unparsed) 已改表头, 人工逐格如上, reviewer 须人工复核.

### git diff --stat -- kb_files
```
 knowledge_base/domains/PC/assumptions.md |  50 +++++------
 knowledge_base/domains/PC/examples.md    |  43 +++++++++-
 knowledge_base/domains/PP/examples.md    | 137 ++++++++++++++-----------------
 3 files changed, 129 insertions(+), 101 deletions(-)
```

## attempt 1 续 (2026-11-26, 主控裁定 O-a / O-b / O-c / D-2 后)

- md5 after (续): PC/assumptions.md `241c819f3e0e6faeeeb441e5e9342f9a` (未动); PC/examples.md `664b4e0176db9b6e8af2cd03b1e48e64`; PP/examples.md `a33b5f182cf390e078efc81c19fb67a6`
- 行号漂移: PC/examples.md 在 :10-21 新插 12 行 → 上文 PC/examples 行号 ≥ 9 一律 +12 (PC Ex1 表现为 :25-58; T-1 现 :79, T-2/T-3 现 :103 / :116; Ex3 relrec 修正格现 :293; T-8 散文现 :284-285). PP/examples.md 行号 ≤ 116 不变.

### 新增变更

| # | kb_file:line (改后) | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 24 | PC/examples.md:11 | ig34_p0270_a002 | INSERTED | Ex1 首句 (concentration data for drug A …) | 270 |
| 25 | PC/examples.md:13 | ig34_p0270_a003 | INSERTED | PCTPTREF 段 (保持弯引号 “zero”) | 270 |
| 26 | PC/examples.md:15 | ig34_p0270_a004 | INSERTED | Rows 1-2 | 270 |
| 27 | PC/examples.md:16 | ig34_p0270_a005 | INSERTED | Rows 3-4 | 270 |
| 28 | PC/examples.md:17 | ig34_p0270_a006 | INSERTED | Rows 5-6 | 270 |
| 29 | PC/examples.md:18 | ig34_p0270_a007 | INSERTED | Rows 7-12 | 270 |
| 30 | PC/examples.md:19 | ig34_p0270_a008 | INSERTED | Rows 13-16 | 270 |
| 31 | PC/examples.md:20 | ig34_p0270_a009 | INSERTED | Rows 17-20 (3 行合并) | 270 |
| 32 | PC/examples.md:21 | ig34_p0270_a010 | INSERTED | Rows 21-30 (PDF 原文如此, 表实有 32 行) | 270 |
| 33 | PC/examples.md:9 / :23 | ig34_p0270_a001 / a011 | (已在 attempt 1 插入) | `### Example 1` 标题 / `**pc.xpt**` | 270 |
| 34 | PP/examples.md:82 | O-b | REPLACED | Ex3 叙述 2 处 PPRFDTC → PPRFTDTC | 274 |

- 新增 atom 清单 (O-a): ig34_p0270_a001 … a011 (11 条; a001/a011 attempt 1 已落, a002-a010 本次). 自查: `fp_match.norm(verbatim) in norm(PC/examples.md)` 11/11 True.
- **ledger 注**: coverage_ledger.wc.jsonl 中 a001-a011 判 EXACT/EQUIVALENT, 指向 md_dmPC_ex_a004-a014 — 这些 md atom 来自旧版 PC/examples.md (行 7-?), 当前文件 (修复前) 已无该内容; T3 回写 ledger 时须改指新行.

### D-2 改记
- D-2 (SUPPPP 引句 + 表, base PP/examples.md:43-55 → 现 :66-78) action 由 MOVED/D2 **改记为 RELOCATE** (主控裁定, PDF p274 为准). Ex1 原处 :43 一行交叉引用保留.

### O-c: PP/examples.md:108-179 (base 行号) 逐条对 PDF

| # | 现行号 | 内容 (摘要) | PDF 对照 | 判定 |
|---|---|---|---|---|
| C-1 | :108 | 标题 `## Pharmacokinetic Parameters (PP) Dataset for All Examples` | p277 原标题 | PDF 原文, 保留 |
| C-2 | :110 | "shared PP dataset contains 12 rows … Day 1 and Day 8, 4 PPGRPID columns" | p277 表: 12 行, Day 1/8, 4 列 Ex1-4; PPCAT=DRUG X (STUDYDRUG 是 PC 的 PCTEST) | KB_AUTHORED, 不矛盾, 保留 |
| C-3 | :112 | D2 交叉引用 | — | KB_AUTHORED (本批 D-1) |
| C-4 | :114 | "*See PC examples for the full description …*" | 导航 | KB_AUTHORED, 保留 |
| C-5 | :116 | 标题 `## §6.3.5.9.3 RELREC Method Quick Reference (PP-side view)` | 无对应 | KB_AUTHORED 标题, 保留 (规则 6) |
| C-6 | :118 | 导语 "full 4 worked Examples … in PC/examples.md …" | 导航 | KB_AUTHORED, 保留; 括注 "the most common pattern …" 删 (D-3) |
| C-7 | :120-127 | Method label mapping 表 A/B/C/D × IDVAR | p275-276 方法列表: A PCGRPID+PPGRPID / B PCSEQ+PPGRPID / C PCGRPID+PPSEQ / D PCSEQ+PPSEQ, 基数一致 | KB_AUTHORED, 与 PDF 一致, 保留 (UNPARSEABLE 表未改) |
| C-8 | :129 | "canonical mappings … cite this table directly" | 面向检索的指令句 | KB_AUTHORED, 保留, 交 reviewer |
| C-9 | :131-136 | Method A 小节 (p277) + row form + Rows 1-2 / 3-4 | Rows 1-2 逐字一致; Rows 3-4 PDF 为 "GRPID = …" (KB 写成 PCGRPID/PPGRPID) | KB_AUTHORED 改写, 不矛盾, 保留; 逐字原文在 PC/examples.md |
| C-10 | :138-143 | Method B (pp 277-278) + 两条 | 与 p277 文字一致 (少 "the"); 页码对 | KB_AUTHORED, 保留 (表 RELID 矛盾见 MANUAL_02) |
| C-11 | :145-150 | Method C (p278) + 两条 | 与 p278 一致 (省 "=" / "a" / "of") | KB_AUTHORED, 保留 |
| C-12 | :152-163 | 节选 relrec.xpt Method C 行 1-8 | p278 Method C 行 1-8 逐格一致 | KB_AUTHORED 节选, 保留 |
| C-13 | :165 | "Reading the PP-side rows …" 首句 | 与表一致 | KB_AUTHORED, 保留; 次句删 (D-4) |
| C-14 | :167 | 标题 `### Method D … (pp 278-280)` | Ex1 Method D 在 p278-279 (p280 是 Ex2) | KB_AUTHORED 标题页码偏差; 规则 6 不改标题, 交 reviewer/主控 |
| C-15 | :169-172 | Method D row form + 两条 | p278 Rows 1-19 / 20-38 内容一致 (省 Rows 标签, "PP"→"individual PP") | KB_AUTHORED, 保留 |
| C-16 | base :187-192 | `### Cross-domain summary (Examples 2-4 on pp 281-284)` 全节 | 见 D-5 | 删 (D-5) |

### 删除清单 (续, D2 删扩写)

| # | 原位置 | 改后 | 原因 (PDF 依据) | 保留副本 |
|---|---|---|---|---|
| D-3 | PP/examples.md:118 句末括注 "(the most common pattern when individual PP parameters need to be linked to a group of PC concentration records)" | 删括注, 句子止于 "for Method C." | PDF 无"最常用"之说; p284 Conclusions 称 Method A 最省、D 最易实现, B/C 为 hybrid → 与 PDF 评价矛盾 | — |
| D-4 | PP/examples.md:165 次句 "This is what "Many to One" means here — many distinct PP records linked to one PC group." | 删 | 方向与 PDF 相反: p275 "Method C (many to one, using PCGRPID and PPSEQ)" = 多条 PC (PCGRPID 组) 对一条 PP (PPSEQ); 对照 B "one to many, PCSEQ and PPGRPID" | — |
| D-5 | PP/examples.md base:187-192 (标题 + 引句 + 3 条) | 删整节 (末尾) | 页码全错 (Ex2 实 p279-280, Ex3 p280-281, Ex4 p282-283); Ex3 "PCSEQ + PPGRPID (mirror of Method B)" 与 PDF 矛盾 (Ex3 演示 A-D 四法, 按 half-life 分组); Ex4 "PCGRPID + PPSEQ" 矛盾 (p282 只演示 A 与 D, A 用 PCGRPID+PPGRPID); 全仓无指向该锚点的链接 | PDF 原文在 PC/examples.md Ex2-4 |

### PDF_TYPO 候选 (维持照录, 用户 T4 统一裁)
- T-7 PP Ex1 PPSTRESU "H" (PP/examples.md:18, :21) — 照 PDF.
- T-8 PC/examples.md:284-285 散文 "DYIDRGX_A" / "DYIDRGX_HALF" — 照 PDF. (另: p280 同段 "DYDRGX_HALF" 在 Ex3 引言, 若 KB 照录亦属同类, 未改.)

### census / check_links (续, 重跑)
- census_after2: `OK 19 / DIFF 3 / NO_PDF 1 / UNPARSEABLE 1, diffs 38`, 本批页 PDF_ONLY 0 (与 attempt 1 末相同; 残留同上: PC/examples.md:75 表 1 格 + :89 表 2 格 = PDF_TYPO; PP:70 SUPPPP 35 = 表头 T-6 + 解析器错位; PP:56 NO_PDF; PP:122 UNPARSEABLE).
- check_links: live docs 42 (改前 42).
- git diff --stat: 见 `git diff --stat -- knowledge_base/domains/PC knowledge_base/domains/PP`.

## attempt 1 续 2 (2026-11-26, reviewer CONDITIONAL → 主控裁定)

- md5 after (续 2): PP/examples.md `f5bdc6e45e790045ef10f5de8ce6596d`; PC/assumptions.md / PC/examples.md 未动 (`241c819f…` / `664b4e01…`).
- PP/examples.md 行号: 原 :42-43 (空行 + 指针) 删除 → 其后行号 −2 (SUPPPP 现 :64-76, Ex2 表头 :54, Ex3 叙述 :80, D-1 交叉引用 :110, Method D 标题 :165).

| # | kb_file:line (改后) | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 35 | PP/examples.md:42 (原 :43) | 裁定 1 / D-2 | DELETED | 删 SUPPPP 指针行及其前空行; D-2 为 RELOCATE, 原处不留指针 (只有 D2 去重副本留引用, 即 D-1) | 274 |
| 36 | PP/examples.md:165 | 裁定 2 / C-14 | REPLACED | 标题页码 (pp 278-280) → (pp 278-279); 全仓无指向该锚点的链接 | 278-279 |
| 37 | PP/examples.md:50 | 裁定 3 | 无需改 | 核对: Row 4 说明句在 KB 中已完整, 含 "…from having to house hyper-specific, pre-coordinated PK parameter values." (p273-274); KB 拼写 "pre-coordinating" 保留 | 273 |

- 删除清单更新: D-2 = RELOCATE (base PP/examples.md:43-55 → 现 :64-76), 原处 **无** 交叉引用 (attempt 1 续中 "Ex1 原处 :43 一行交叉引用保留" 一句作废).

### PDF_TYPO 正式清单 (补)
- T-8b: PC/examples.md:278 Ex3 引言 "DYDRGX_HALF" — p280 原文如此 (应为 DY1DRGX_HALF), KB 照录.
- T-9: PP/examples.md:50 Ex2 Row 4 — PDF p273 拼作 "pre-corrdinating", KB 保留正确拼写 "pre-coordinating".

### 重跑 (续 2)
- census: `OK 19 / DIFF 3 / NO_PDF 1 / UNPARSEABLE 1, diffs 38`, 本批页 PDF_ONLY 0 (与续 1 相同, 残留均已登记).
- fp_match: regressions=0, new_hits=10, RESULT: GREEN.
- check_links: live docs 42 (不变).
