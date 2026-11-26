# T2 B-OE writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `fb87b40901ba1c0bc615bd5285fdba1cf8700213`
- md5 before: OE/examples.md `83671b6aad27593a627947d55c9a4725` (153 行); after `df19b40475ce8ed597d79c8661b49ab9` (163 行, +10 = Ex4 AE 引导句 + ae.xpt 标签 + 表 5 行 + 空行)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-OE_writer/`
  (examples.before.md, apply.py = 精确替换 + 命中次数断言, 列数断言, prose_scan.py / prose_scan_before.py, census_after.json, fp_after.jsonl, fp_regress.jsonl, p302-p305 110dpi 整页渲染)
- 数据来源: 所有改动格逐格对照渲染图 (p302-305); census 解析器 (bbox) 改后复跑; 叙述对照 `work/pdf_pages/ig34_p0301-0305.txt`.
- 本批 atoms 0 / t2_recheck 0; census DIFF 7 表 (14 diffs) 全部处理; pdf_only 1 (p305 Ex4 ae.xpt) 已补; unparseable 0; out_of_scope 0.
- 跨行折行合并 (ae.xpt): USUBJID `XYZ-100-0001`, AEBODSYS `Nervous system disorders`, AETERM `Worsening Dry Eyes`, AEACN `DOSE NOT CHANGED`, AEREL `NOT RELATED`, 日期 `2011-05-02` 等.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | OE/examples.md:14 | census:12 r1 OEMETHOD | REPLACED | SLIT LAMP BIOMICROSCOPY → SLIT LAMP | 302 |
| 2 | :15 | census:12 r2 OEMETHOD | REPLACED | 同上 | 302 |
| 3 | :16 | census:12 r3 OEMETHOD | REPLACED | 同上 | 302 |
| 4 | :24 | census:22 r1 QNAM | REPLACED | OEDIRT → OEDIR1 | 302 |
| 5 | :77 | census:75 r1 OECLSIG | REPLACED | N → Y | 303 |
| 6 | :78 | census:75 r2 OELAT | REPLACED | LEFT → RIGHT (FOCID OD) | 303 |
| 7 | :78 | census:75 r2 OECLSIG | REPLACED | 空 → N | 303 |
| 8 | :102 | census:98 r3 PRSTDTC | REPLACED | 2012-05-25T08:30:00 → 2012-05-25T08:00:00 | 303 |
| 9 | :121 | census:121 HEADER col5 | SKIPPED_PDF_TYPO | T-1: KB IDVARVAL 保留 (PDF 表头 "IDVARAL") | 304 |
| 10 | :142-145 | census:140 r1-r4 OECAT (×4) | SKIPPED_PDF_TYPO | T-2: KB OCULAR COMFORT 保留 (PDF "OCCULAR COMFORT") | 304 |
| 11 | :153 | census:151 r1 QLABEL | REPLACED | Rating Scale → Result Criteria | 305 |
| 12 | :147 | R3 N-1 (ig34_p0305_a001) | REPLACED | KB 改写句 "The suppoe.xpt dataset represents the scale used for…" → PDF 原句 "The numeric scale used in grading ocular comfort is described in a supplemental qualifier dataset." (D2, 删除清单 D-1) | 305 |
| 13 | :155 | R3 N-2 (ig34_p0305_a005) | INSERTED | Ex4 AE 引导段 "Adverse events affecting the eyes are represented in the AE domain. …" (2 句, 逐字), suppoe 表后 | 305 |
| 14 | :157-163 | pdf_only:p305:ae.xpt | TABLE_REBUILT | 补整表 `**ae.xpt**` (19 列含 Row/AEENDTC, 3 行): AESEQ 5/6/7, Headaches / Worsening Dry Eyes ×2, FOCID 空/OD/OS, AEENDTC 2011-05-06/05/04 | 305 |

- atoms 覆盖率自查: atoms 0 → 无 atom 行. census 14 diff 格 + 1 pdf_only 全部在表中 (#1-11, #14).

### census 表处理

| census ref (before 行号) | 处理 | 结果 |
|---|---|---|
| :12 Ex1 oe.xpt (3 CELL) | #1-3 | OK |
| :22 Ex1 suppoe.xpt (1 CELL) | #4 | OK |
| :75 Ex3 oe.xpt (3 CELL) | #5-7 | OK |
| :98 Ex3 pr.xpt (1 CELL) | #8 | OK |
| :121 Ex3 relrec.xpt (1 HEADER) | #9 T-1 | DIFF 1 残留 (预期) |
| :140 Ex4 oe.xpt (4 CELL) | #10 T-2 | DIFF 4 残留 (预期) |
| :151 Ex4 suppoe.xpt (1 CELL) | #11 | OK |
| pdf_only p305 Ex4 ae.xpt | #14 | 新表 :159 OK (cells_compared 57 = 3×19, 含 AEENDTC) |

- 汇总 (census_after): KB tables 12, `OK 10 / DIFF 2, cells 694, diffs 5` (= T-1 1 + T-2 4). 改前 OE: DIFF 7 / diffs 14 + PDF_ONLY 1. Ex2 oe/suppoe、Ex3 suppoe/di 改前即 OK, 另对渲染图人工逐格复核一致, 未动.

```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-OE_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-OE.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
python3 -I $S/prose_scan.py          # 改后; prose_scan_before.py 同脚本指向 examples.before.md
python3 tools/check_links.py | tail -1   # live docs: 42
```

### fp_match
- fp_baseline 对 p301-305 只含 19 原子 (p305 a013 起, 属 RP 节); OE Examples 原子 (p301 a016-p305 a010) 不在 fp 基线范围 → 本批 fp 命中/回归 **0 变化**.
- 全量 regress 41 条 (p011/p021/p025/p026/p036x §6.4.2), grep `OE/` = 0, 均为工作树中他批 (FA/MS 等) 未提交改动, 非本批.
- **预期 fp 回归 (PDF_TYPO 修正)**: 0. T-1/T-2 KB 均未动 (保留 KB 原正确值); 若台账按 PDF 原文精确匹配, ig34_p0304_a012 (relrec 表头 IDVARAL) 与 ig34_p0304_a026-a029 (OCCULAR 行) 会保持不命中, 属预期.

### 双向全扫 (含表格原子)
- 范围: p301 "OE – Examples" 至 p305 "6.3.7.6" 前.
- PDF→KB (叙述, pdf_atoms SENTENCE/LIST_ITEM/NOTE 38 条, verbatim 归一后子串): 改后未命中 11 = OE assumptions 3 (p0301_a011-a013, 属 assumptions.md, 已存在) + RP 2 (p0305_a013/a015, 非本域) + **ATOM_ERR 6**: p0301_a017 (原子含 "OEDTC=…2012-01-19", 渲染图为 `using OETESTCD="INTP"`), p0301_a018 (原子截断 "represented in the observed…"), p0304_a020-a023 ("installation", 渲染图为 "instillation"). KB 与渲染图一致.
  改前另缺 2 条 (p0305_a001、a005) → 本次 #12/#13 补齐 (mutation check: before 脚本报 13 miss, after 11).
- KB→PDF (KB 叙述逐句在 layout 文本归一后子串): 改后 0 未命中; 改前 1 = :147 KB 改写句 (#12 已换).
- 表格原子: 12 张表 (含新 ae.xpt) 全部对 110dpi 渲染图逐格人工核, 表头 / 列序 / 列数 / Row 列均与 PDF 一致 (除 T-1/T-2). 小标题 `**xxx.xpt**`、`## Example N` 均对应 PDF.
- KB_AUTHORED / D6: 无 (文件中无超出 PDF 的解释性内容).

### 新增 atom 清单 (R3)
- N-1 :147 ig34_p0305_a001 (替换 KB 改写句); N-2 :155 ig34_p0305_a005 (AE 引导段).

### 删除清单 (reviewer 逐条确认)

| # | 原位置 (base 行号) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | :147 "The suppoe.xpt dataset represents the scale used for the ocular comfort rating." | :147 PDF 原句 | R2 残留改写句 / 词替换型改写; 该行不承载 fp 原子 (fp 基线不含 OE Examples 原子) → 删除改写, 换 PDF 原文 | — |
| D-2 | :14-16, :24, :77-78, :102, :153 旧值 | 同行 | VALUE_DIFF 旧值替换 (#1-8, #11) | — |

### PDF_TYPO 清单 (正确值可由 PDF 自身确定 → KB 写正确值)

| # | 位置 | PDF | KB | 依据 |
|---|---|---|---|---|
| T-1 | :121 Ex3 relrec.xpt 表头 col5 | IDVARAL | IDVARVAL | 同文件 suppoe 表头及 RELREC 结构 (p304 同节其他 relrec/supp 表) 均为 IDVARVAL; 表头大小写/拼写印刷错口径. KB 未动, census 残留 1 |
| T-2 | :142-145 Ex4 oe.xpt OECAT ×4 | OCCULAR COMFORT | OCULAR COMFORT | 同例 p305 suppoe IDVAR=OECAT 的 IDVARVAL 为 "OCULAR COMFORT" (必须等于 OECAT 值), 叙述亦作 "ocular comfort". KB 未动, census 残留 4 |

### 照录 PDF, 供主控 / T4 用户裁 (KB = PDF)
- **U-1 Ex4 oe.xpt OESEQ 1/2/1/2 (:142-145)**: 同一 USUBJID XYZ-100-0001 内 OESEQ 重复 (OS 行又从 1 起), 违反 --SEQ 主体内唯一; 正确值 (3/4?) 不能由 PDF 自身确定 → 照录. 同 subject 的 AE AESEQ 5/6/7.
- 已核非问题: Ex1 OEMETHOD "SLIT LAMP" 为 CT 提交值 (`knowledge_base/terminology/core/general_part3.md:407` C75583, 同义词 Slit Lamp Biomicroscopy), 故按 PDF 改无疑; Ex2 "SLIT LAMP BIOMICROSCOPY" (×4) 为 PDF 原值, KB=PDF 未动 (非 CT 提交值, 仅记录). Ex2 OETESTCD "HYPERMIA" 为 PDF 原值, 未动.

### 范围外发现 (主控决定)
- **O-OE-1 `knowledge_base/domains/OE/assumptions.md`**: 缺 "OE – Description/Overview" 句 (p298, 1 句) 与 spec 首句 (p299, "oe.xpt, Ophthalmic Examinations — Findings. One record per ophthalmic finding per method per location, …, Tabulation."). 按 CM/IS 先例应放在 assumptions.md 的 Description/Overview 与 Assumptions 之间; 不在本批白名单, 未动 (O15/O16 全域扫描可兜底). OE/spec.md:3 仅有 KB 自写 "Class / Structure" 摘要行.

### 触碰过的 unparseable 表
- 无.

### git diff --stat
```
 knowledge_base/domains/OE/examples.md | 28 +++++++++++++++++++---------
 1 file changed, 19 insertions(+), 9 deletions(-)
```
- 本批只改 knowledge_base/domains/OE/examples.md (其他 M/?? 为他批既有改动, 未触碰). 未 commit. check_links live docs 42 (基线 42).
