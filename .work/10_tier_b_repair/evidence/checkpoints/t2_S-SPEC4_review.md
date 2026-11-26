# T2S 扫描批 S-SPEC4 — reviewer attempt 1

> 2026-11-26, oh-my-claudecode:code-reviewer (opus). Brief `subagent_prompts/t2s_scan_review_audit_v1.0.md` Reviewer 段 + `t2_reviewer_v1.0.md` + common brief + dispatch notes (含 T2S 段) + U1-U8 + T1 ack.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC4_reviewer/` (B<p>.html bbox, L<p>.txt layout, r<p>.png 渲染, rv_parse.py / rv_cmp.py / rv_fn.py 本 reviewer 自写, 未用 writer 的 sc2*/speccmp*)

## Verdict: **PASS**

## 1. 授权范围 / diff
- `git diff HEAD --stat -- knowledge_base/`: 本批 9 文件 (RS SC TU VS SUPPQUAL TE TI TS TV spec.md) 35+/17-; 其余 8 文件 (CV FT MI MK NV QS RE RP) 属并行 S-SPEC3, 不计. narrow_files 空.
- 本批 diff 逐行读毕: 仅 `- **Controlled Terms:** ` → `- **Controlled Terms:** *` 17 处 + 脚注插入 9 处 (各 1 行 + 空行). 无删除 / 改写 / 标题 / 变量增删. 与 writer 声明一致.

## 2. 页范围复核 (渲染 + bbox)
RS 329-332 / SC 340-341 / TU 345-346 / VS 358-360 / SUPPQUAL 432 / TE 403 / TI 416 / TS 417-418 / TV 407-408 (18 页) — 与 writer 一致. p330 顶部为 RSTESTCD Notes 续行 (渲染核).

## 3. 独立双向逐变量逐字段核 (自写 bbox 列解析)
方法: `rv_parse.py` 按每页表头行 (同行含 Type/Role/Core) 的词 xMin 定 7 列起点 (Label 列若不在首行表头则取下 1-2 行 "Label/Variable" 词, 覆盖 p407/p432 缩进表头); 表头块止于全为表头词的行; 行起点 = Name 列大写变量名; 续页首部无变量名的行并入前页末变量; 止于 "In this column" / 独立上标 "1" / 页脚 "©" 行. 字段内折行: 行尾单 "-" 无空格并接, 其余空格并接. KB 侧按 `### VAR` + `- **Field:**` 解析. 逐字精确比较 (空白归一), 不等再判 "仅空白" / DIFF.
首跑把页脚 "© 2021 Clinical Data Interchange…" 混入末变量 (自身 bug), 加页脚止点后重跑; 结果如下.

| 域 | PDF 变量 | KB 变量 | 顺序 | KB Order 1..n | Label/Type/Role/Core/Notes 差异 | CT `*` (PDF=KB) | U5 / U6 (S-CT) |
|---|---|---|---|---|---|---|---|
| RS | 46 | 46 | 一致 | 是 | 0 (RSSTRESN "-- STRESC" PDF 折行, 仅空白) | 0 (PDF 无 `*`, 渲染 p329-332 确认) | 17 / 1 |
| SC | 24 | 24 | 一致 | 是 | 0 | 2 SCCAT SCSCAT | 6 / 1 |
| TU | 31 | 31 | 一致 | 是 | 0 | 0 (PDF 无 `*`, 渲染 p345-346 确认) | 14 / 1 |
| VS | 38 | 38 | 一致 | 是 | 0 | 4 VSCAT VSSCAT VSTOX VSTOXGR | 13 / 1 |
| SUPPQUAL | 10 | 10 | 一致 | 是 | 0 | 2 IDVAR QNAM | 2 / 0 |
| TE | 7 | 7 | 一致 | 是 | 0 | 2 ETCD ELEMENT | 0 / 1 |
| TI | 8 | 8 | 一致 | 是 | 0 | 3 IETESTCD IETEST IESCAT | 1 / 1 |
| TS | 11 | 11 | 一致 | 是 | 0 | 2 TSVAL TSVALCD | 3 / 1 |
| TV | 9 | 9 | 一致 | 是 | 0 | 2 ARMCD ARM | 0 / 1 |
| 计 | 184 | 184 | | | 0 | 17 | 56 / 8 |
- CT 全 184 变量: EQ 120 (含 `*` 17 + 双方空 + ISO 8601 等格式值逐字) / U5 56 / U6 8 / DIFF 0. U5 判据: PDF 为括号短名且 KB 为 C-code (不判对错, 归 S-CT).
- `*` 独立二次计数: 18 页 bbox 中含 `*` 的词 (排除脚注 "(*)") = p340:2 p358:1 p359:3 p403:2 p408:2 p416:3 p417:1 p418:1 p432:2, 余页 0 → 17, 与 KB 逐变量一致.
- KB→PDF: 9 文件变量块只含 7 字段 (Order/Label/Type/Controlled Terms/Role/Core/CDISC Notes); 块外仅 H1、`> Class|Structure` (U8)、SUPPQUAL `> Source text` (D7)、`---`、脚注、Cross References (U8). 无 kb-only 变量/字段/行.
- 注意 (不改): RSTESTCD Notes PDF 原文 `Examples: TRGRESP, "NTRGRESP, "OVRLRESP"` 引号不配对, KB 照录 = PDF (p330 渲染核), 属 PDF 原样, 非本批缺陷.

逐变量 CT 结果 (自动生成自 rv_cmp.out):
| 域 | 变量: PDF CT 渲染/bbox → KB (判定) |
|---|---|
| RS (47) | RSSTRESN(pCDISC Notes) `WS-ONLY`→`Used for continuous or numeric results or findings in standard format; copied in numeric format from -- STRESC. --STRESN should store all numeric test results or findings. For Clinical Classifications, this may be a score.` Used for continuous or numeric results or findings in standard format; copied in numeric format from --STRESC. --STRESN should store all numeric test results or findings. For Clinical Classifications, this may be a score.; STUDYID(p329) 空=空; DOMAIN(p329) `RS`→`空` U6; USUBJID(p329) 空=空; RSSEQ(p329) 空=空; RSGRPID(p329) 空=空; RSREFID(p329) 空=空; RSSPID(p329) 空=空; RSLNKID(p329) 空=空; RSLNKGRP(p329) 空=空; RSTESTCD(p329) `(ONCRTSCD)`→`C96782` U5; RSTEST(p330) `(ONCRTS)`→`C96781` U5; RSCAT(p330) `(ONCRSCAT)(CCCAT)`→`C124298; C118971` U5; RSSCAT(p330) 空=空; RSORRES(p330) 空=空; RSORRESU(p330) `(UNIT)`→`C71620` U5; RSSTRESC(p330) `(ONCRSR)`→`C96785` U5; RSSTRESN(p330) 空=空; RSSTRESU(p330) `(UNIT)`→`C71620` U5; RSSTAT(p330) `(ND)`→`C66789` U5; RSREASND(p330) 空=空; RSNAM(p330) 空=空; RSMETHOD(p330) `(QRSMTHOD)`→`C158113` U5; RSLOBXFL(p330) `(NY)`→`C66742` U5; RSBLFL(p330) `(NY)`→`C66742` U5; RSDRVFL(p330) `(NY)`→`C66742` U5; RSEVAL(p331) `(EVAL)`→`C78735` U5; RSEVALID(p331) `(MEDEVAL)`→`C96777` U5; RSACPTFL(p331) `(NY)`→`C66742` U5; VISITNUM(p331) 空=空; VISIT(p331) 空=空; VISITDY(p331) 空=空; TAETORD(p331) 空=空; EPOCH(p331) `(EPOCH)`→`C99079` U5; RSDTC(p331) `ISO 8601 datetime or interval`=`ISO 8601 datetime or interval`; RSDY(p331) 空=空; RSTPT(p331) 空=空; RSTPTNUM(p331) 空=空; RSELTM(p331) `ISO 8601 duration`=`ISO 8601 duration`; RSTPTREF(p331) 空=空; RSRFTDTC(p331) `ISO 8601 datetime or interval`=`ISO 8601 datetime or interval`; RSEVLINT(p331) `ISO 8601 duration or interval`=`ISO 8601 duration or interval`; RSEVINTX(p331) 空=空; RSSTRTPT(p331) `(STENRF)`→`C66728` U5; RSSTTPT(p331) 空=空; RSENRTPT(p332) `(STENRF)`→`C66728` U5; RSENTPT(p332) 空=空 |
| SC (24) | STUDYID(p340) 空=空; DOMAIN(p340) `SC`→`空` U6; USUBJID(p340) 空=空; SCSEQ(p340) 空=空; SCGRPID(p340) 空=空; SCSPID(p340) 空=空; SCTESTCD(p340) `(SCTESTCD)`→`C74559` U5; SCTEST(p340) `(SCTEST)`→`C103330` U5; SCCAT(p340) `*`=`*`; SCSCAT(p340) `*`=`*`; SCORRES(p340) 空=空; SCORRESU(p340) `(UNIT)`→`C71620` U5; SCSTRESC(p340) 空=空; SCSTRESN(p340) 空=空; SCSTRESU(p340) `(UNIT)`→`C71620` U5; SCSTAT(p340) `(ND)`→`C66789` U5; SCREASND(p340) 空=空; VISITNUM(p340) 空=空; VISIT(p340) 空=空; VISITDY(p340) 空=空; TAETORD(p341) 空=空; EPOCH(p341) `(EPOCH)`→`C99079` U5; SCDTC(p341) `ISO 8601 datetime or interval`=`ISO 8601 datetime or interval`; SCDY(p341) 空=空 |
| TU (31) | STUDYID(p345) 空=空; DOMAIN(p345) `TU`→`空` U6; USUBJID(p345) 空=空; TUSEQ(p345) 空=空; TUGRPID(p345) 空=空; TUREFID(p345) 空=空; TUSPID(p345) 空=空; TULNKID(p345) 空=空; TULNKGRP(p345) 空=空; TUTESTCD(p345) `(TUTESTCD)`→`C96784` U5; TUTEST(p345) `(TUTEST)`→`C96783` U5; TUORRES(p345) 空=空; TUSTRESC(p345) `(TUIDRS)`→`C123650` U5; TUNAM(p345) 空=空; TULOC(p345) `(LOC)`→`C74456` U5; TULAT(p345) `(LAT)`→`C99073` U5; TUDIR(p345) `(DIR)`→`C99074` U5; TUPORTOT(p345) `(PORTOT)`→`C99075` U5; TUMETHOD(p346) `(METHOD)`→`C85492` U5; TULOBXFL(p346) `(NY)`→`C66742` U5; TUBLFL(p346) `(NY)`→`C66742` U5; TUEVAL(p346) `(EVAL)`→`C78735` U5; TUEVALID(p346) `(MEDEVAL)`→`C96777` U5; TUACPTFL(p346) `(NY)`→`C66742` U5; VISITNUM(p346) 空=空; VISIT(p346) 空=空; VISITDY(p346) 空=空; TAETORD(p346) 空=空; EPOCH(p346) `(EPOCH)`→`C99079` U5; TUDTC(p346) `ISO 8601 datetime or interval`=`ISO 8601 datetime or interval`; TUDY(p346) 空=空 |
| VS (38) | STUDYID(p358) 空=空; DOMAIN(p358) `VS`→`空` U6; USUBJID(p358) 空=空; VSSEQ(p358) 空=空; VSGRPID(p358) 空=空; VSSPID(p358) 空=空; VSTESTCD(p358) `(VSTESTCD)`→`C66741` U5; VSTEST(p358) `(VSTEST)`→`C67153` U5; VSCAT(p358) `*`=`*`; VSSCAT(p359) `*`=`*`; VSPOS(p359) `(POSITION)`→`C71148` U5; VSORRES(p359) 空=空; VSORRESU(p359) `(VSRESU)`→`C66770` U5; VSSTRESC(p359) 空=空; VSSTRESN(p359) 空=空; VSSTRESU(p359) `(VSRESU)`→`C66770` U5; VSSTAT(p359) `(ND)`→`C66789` U5; VSREASND(p359) 空=空; VSLOC(p359) `(LOC)`→`C74456` U5; VSLAT(p359) `(LAT)`→`C99073` U5; VSLOBXFL(p359) `(NY)`→`C66742` U5; VSBLFL(p359) `(NY)`→`C66742` U5; VSDRVFL(p359) `(NY)`→`C66742` U5; VSTOX(p359) `*`=`*`; VSTOXGR(p359) `*`=`*`; VSCLSIG(p359) `(NY)`→`C66742` U5; VISITNUM(p359) 空=空; VISIT(p359) 空=空; VISITDY(p359) 空=空; TAETORD(p359) 空=空; EPOCH(p359) `(EPOCH)`→`C99079` U5; VSDTC(p359) `ISO 8601 datetime or interval`=`ISO 8601 datetime or interval`; VSDY(p359) 空=空; VSTPT(p359) 空=空; VSTPTNUM(p360) 空=空; VSELTM(p360) `ISO 8601 duration`=`ISO 8601 duration`; VSTPTREF(p360) 空=空; VSRFTDTC(p360) `ISO 8601 datetime or interval`=`ISO 8601 datetime or interval` |
| SUPPQUAL (10) | STUDYID(p432) 空=空; RDOMAIN(p432) `(DOMAIN)`→`C66734` U5; USUBJID(p432) 空=空; IDVAR(p432) `*`=`*`; IDVARVAL(p432) 空=空; QNAM(p432) `*`=`*`; QLABEL(p432) 空=空; QVAL(p432) 空=空; QORIG(p432) 空=空; QEVAL(p432) `(EVAL)`→`C78735` U5 |
| TE (7) | STUDYID(p403) 空=空; DOMAIN(p403) `TE`→`空` U6; ETCD(p403) `*`=`*`; ELEMENT(p403) `*`=`*`; TESTRL(p403) 空=空; TEENRL(p403) 空=空; TEDUR(p403) `ISO 8601 duration`=`ISO 8601 duration` |
| TI (8) | STUDYID(p416) 空=空; DOMAIN(p416) `TI`→`空` U6; IETESTCD(p416) `*`=`*`; IETEST(p416) `*`=`*`; IECAT(p416) `(IECAT)`→`C66797` U5; IESCAT(p416) `*`=`*`; TIRL(p416) 空=空; TIVERS(p416) 空=空 |
| TS (11) | STUDYID(p417) 空=空; DOMAIN(p417) `TS`→`空` U6; TSSEQ(p417) 空=空; TSGRPID(p417) 空=空; TSPARMCD(p417) `(TSPARMCD)`→`C66738` U5; TSPARM(p417) `(TSPARM)`→`C67152` U5; TSVAL(p417) `*`=`*`; TSVALNF(p418) `ISO 21090 NullFlavor`=`ISO 21090 NullFlavor`; TSVALCD(p418) `*`=`*`; TSVCDREF(p418) `(DICTNAM)`→`C66788` U5; TSVCDVER(p418) 空=空 |
| TV (9) | STUDYID(p407) 空=空; DOMAIN(p407) `TV`→`空` U6; VISITNUM(p407) 空=空; VISIT(p407) 空=空; VISITDY(p407) 空=空; ARMCD(p408) `*`=`*`; ARM(p408) `*`=`*`; TVSTRL(p408) 空=空; TVENRL(p408) 空=空 |

## 4. 脚注 9 处 (逐字 + U7 位置)
- PDF (bbox 抽 p332/341/346/360/432/403/416/418/408): 9 页均为 上标1 + "In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses." 渲染 p332/p346/p432 目视一致.
- KB: 9 文件各 1 行 `> ¹In this column, … enclosed in parentheses.` 与 PDF 逐字一致; 全 KB 该行 62 份完全相同 (= 已提交 53 + 本批 9).
- 位置 (行号): RS 末 Notes 417 → `---` → 脚注 420 → CR 422; SC 219/222/224; TU 282/285/287; VS 345/348/350; SUPPQUAL 95/98/100; TE 66/69/71; TI 75/78/80; TS 102/105/107; TV 84/87/89 — 全部在最后变量块之后、Cross References 之前 (U7). 
- 新插入字符: `(*)`、`CDISC/NCI` 与 PDF 原字符一致 (无引号/dash 类字符).

## 5. 表头缩进页 (p407 TV / p432 SUPPQUAL)
渲染 + 本 reviewer 解析器: 表头 "Variable Name / Variable Label / Type / Controlled Terms, Codelist or Format¹ / Role / CDISC Notes / Core", Label 列表头分两行; 解析得 TV 5+4、SUPPQUAL 10 变量, 逐字段零差异. p432 IDVAR/QNAM `*`, RDOMAIN `(DOMAIN)`, QEVAL `(EVAL)` 渲染确认.

## 6. census / fp_match / 清单签字
- census: `pdf_ranges` 空, `census_items` 空 → 跳过 (spec 表无 Row 列; 由第 3 节独立解析 + 渲染替代).
- fp_match: `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` → RESULT: RED, regress 72 条, 全部在 `work/t2_fp_expected_regressions.jsonl` 内 (未预期 0; 本批页码 0).
- 结构改动清单 无 / 删除清单 无 (17 处旧值为空串) / D6 清单 无 / PDF_TYPO 无 — 逐条核, 签字同意.
- G-TB6: 新增 26 行全部有 PDF 出处 (17 个 `*` = CT 列; 9 脚注 = 表下脚注); 无出处 0.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (= 基线 42).

## 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无缺陷 | — |

## 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC4_reviewer
P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
for p in 329 330 331 332 340 341 345 346 358 359 360 403 407 408 416 417 418 432; do pdftotext -bbox -f $p -l $p "$P" $S/B$p.html; done
python3 -I $S/rv_cmp.py $S > $S/rv_cmp.out     # 计数闸 + 逐字段 + CT 分类
python3 -I $S/rv_fn.py $S                       # 9 页脚注原文
for p in 329 330 331 332 345 346 407 432; do pdftoppm -f $p -l $p -r 80 -png "$P" $S/r$p; done
```
