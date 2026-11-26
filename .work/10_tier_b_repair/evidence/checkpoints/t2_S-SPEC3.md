# T2S 扫描批 S-SPEC3 (spec-only: CV MI MK NV RE RP QS FT) — writer attempt 1

> 2026-11-26, oh-my-claudecode:executor (opus). Brief `subagent_prompts/t2s_scan_writer_v1.0.md`; 批次 `work/t2_batches/S-SPEC3.json`.
> 只改 8 个 spec.md; assumptions/examples 未碰; 未 stash/checkout/commit. 基线 = `git show HEAD:<file>` (8 文件改前与 HEAD 一致, `cmp` 已核).
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC3_writer/`
> (bb_N.html = `pdftotext -bbox`; run.sh 跑共享工具 `work/scratch/t2s_tools/{sc2w,speccmp2}.py`; cmpw_/cmp2_ before/after.txt (改后 speccmp2 只剩 DOMAIN U6 + p286 通用表复合行 + RPSTRESC `or` 盲区, `*` 差异清零); ct_N-N.png = Name~CT 列裁图 90dpi; stars.py = bbox CT 列 `*` 定位; apply.py = 精确替换+断言; base/ = HEAD 副本)

md5 改后: CV `1c0abe729f1c5ebbf351ab1be6071cad` (409→411) · MI `0f4f537ab9763f0587ee63e9c51fcce8` (366→368) · MK `12d5622012dd8b22d4939eb068685fec` (409→411) · NV `c3e254914cea195492b31841e988458f` (408→410) · RE `db9ff08b06adda8764c3dd1c1c162658` (454→456) · RP `8322f864d5f6e389553440379ca0f147` (348→350) · QS `574e5b8682b39e8db2daaf9da855a170` (341→343) · FT `f4d5159f342444b6efbb923689e1ed7b` (368→370)

## 完整节页范围 (O20 复核; 本批只扫各域 spec 表)
| 域 | 节 (json lo-hi) | spec 表所在页 (复核) | 起止依据 (layout `work/pdf_pages/ig34_pNNNN.txt` 行号) |
|---|---|---|---|
| MI | §6.3.5.8 (263-267) | **264-265** | p263:40 节标题 (+Description, 非 spec); p264:1 `MI – Specification`; p265:35 脚注, :37 `MI – Assumptions` |
| CV | §6.3.7.2 (286-290) | **286-288** | p286:1-37 = §6.3.7.1 通用表尾 + 其脚注 (属 NV/assumptions.md, 非本批); :39 CV 节标题, :43 `CV – Specification`, 页上第 2 表头 (仅 STUDYID); p288:41 脚注, :46 `CV – Assumptions` |
| MK | §6.3.7.3 (290-294) | **290-291** | p290:1 节标题, :5 `MK – Specification`; p291:52 脚注; p292:1 `MK – Assumptions` |
| NV | §6.3.7.4 (294-298) | **294-296** | p294:31 节标题, :34 `NV – Specification`; p296:10 脚注, :15 `NV – Assumptions` |
| RP | §6.3.7.6 (305-308) | **305-306** | p305:17 节标题, :20 `RP – Specification`; p306:42 脚注, :47 `RP – Assumptions` |
| RE | §6.3.7.7 (308-312) | **308-310** | p308:1 节标题, :5 `RE – Specification`; p310:15 脚注, :17 `RE – Assumptions` |
| FT | §6.3.9.1 (319-324) | **319-320** | p319:1 节标题, :5 `FT – Specification`; p320:51 脚注; p321:1 `FT – Assumptions` |
| QS | §6.3.9.2 (324-329) | **324-326** | p324:1-7 = FT 例尾 suppft (非本批); :8 节标题, :12 `QS – Specification`; p326:15 脚注, :17 `QS – Assumptions` |
- json 止页多出的页 (p263 起页、p266-267、p289、p292-293、p297-298、p307、p311-312、p321-323、p327-329) 为 Description / Assumptions / Examples, 已终版, 非 spec-only 批范围.
- 续页首行复核 (sc2 盲区 "跨页续行"): 12 个续页 p265 287 288 291 295 296 306 309 310 320 325 326 表头后首行均以变量名开头 (MISPEC DOMAIN CVLOBXFL MKSTRESU NVTEST NVTPTNUM RPSTRESC RESTRESU RETPTNUM FTSTRESU QSORRESU QSTPTREF) → 无跨页折断的 Notes 续行.

## 方法
- 主工具 `sc2w.py` (空格敏感, 折行连字符归一; 表头取页上最后一个 → p286 正确跳过 §6.3.7.1 通用表) 逐变量比 Label/Type/CT/Role/Core/CDISC Notes 全文 + 变量数/顺序 + KB `Order` 连续性.
- 交叉工具 `speccmp2.py`: 两处已知盲区误报, 均已排除: ① p286 取了第一个表头 (§6.3.7.1 通用表) → CV 假报 3 个复合行 (`USUBJID --SEQ …` / `VISITNUM --DTC --DY`) 与 "45 vs 42"; ② RPSTRESC (p306 表头下首行) Notes 丢两个 "or" (表头词表 HV 含 `or` 被过滤) → 渲染 `top_306-306.png` 确认 PDF 有 "copied or derived … standard format or in standard units … results or findings", KB 一致. 其余 7 域两工具结果相同.
- 计数闸: 8 域 PDF 变量数 = KB 变量数, 顺序一致, Order 1..N 连续 (两工具一致, CV 以 sc2w 为准).
- CT 列 `*`: bbox 定位 (`stars.py`, CT 列 x 200-340 的 `*`) 得 15 处, 其中 p286 `--TESTCD/--TEST` 属 §6.3.7.1 通用表 → 本批 13 处; 渲染裁图人工看 8 页 p264 p287 p290 p295 p305 p308 p319 p324 (含全部 5 个有 `*` 的域首页: `*` 位置与 bbox 一致; NVCAT/NVSCAT、RPCAT/RPSCAT、RECAT/RESCAT PDF 为空, 非 `*`). 无窗口全量 `grep -c '>\*<'` 20 页 bb = 15 (= 13 + p286 通用表 2), 另 9 个 `(*)` 均为脚注正文 (x≈163), 排除 CT 列窗口外漏网.
- KB 结构: 8 文件各变量块恰 7 字段 (Order/Label/Type/Controlled Terms/Role/Core/CDISC Notes), 块外仅 H1 / `> Class|Structure` / `---` / Cross References (U8 导航).

## 双向全扫 (每域 spec 表逐变量结果表; 改后 sc2w.py)
PDF→KB: 319/319 变量命中, 顺序一致; KB→PDF: kb-only 变量 0, kb-only 字段 0. Label/Type/Role/Core/CDISC Notes **零差异** (唯一非 OK = QSEVLINT Notes `"- P2Y"` = PDF 折行连字符, 渲染 `qsevlint-326.png` 确认, KB `"-P2Y"` 正确).
CT 列剩余差异全部为 U5 (C-code vs PDF 括号短名, 107 处) / U6 (DOMAIN, 8 处) → 归 S-CT, 本批不改.

| 域 | spec 页 | PDF 变量 | KB 变量 | 顺序 | 字段差异 (改前) | CT `*` 补 | 脚注 | U5 / U6 留 S-CT |
|---|---|---|---|---|---|---|---|---|
| MI | 264-265 | 37 | 37 | 一致 | 0 | 3 | 补 | 16 / 1 |
| CV | 286-288 | 42 | 42 | 一致 | 0 | 3 | 补 | 16 / 1 |
| MK | 290-291 | 42 | 42 | 一致 | 0 | 2 | 补 | 16 / 1 |
| NV | 294-296 | 42 | 42 | 一致 | 0 | 0 | 补 (gaps 未列, 全扫发现) | 15 / 1 |
| RP | 305-306 | 36 | 36 | 一致 | 0 | 0 | 补 | 9 / 1 |
| RE | 308-310 | 47 | 47 | 一致 | 0 | 0 | 补 | 16 / 1 |
| FT | 319-320 | 38 | 38 | 一致 | 0 | 2 | 补 | 10 / 1 |
| QS | 324-326 | 35 | 35 | 一致 | 0 | 3 | 补 | 9 / 1 |
| 计 | 20 页 | 319 | 319 | | 0 | 13 | 8 | 107 / 8 |

### 逐变量结果
| 域 | # | 变量 | PDF 页 | Order/Label/Type/Role/Core/CDISC Notes | CT 列 | 处理 |
|---|---|---|---|---|---|---|
| MI | 1 | STUDYID | 264 | 一致 | 一致 | — |
| MI | 2 | DOMAIN | 264 | 一致 | DOMAIN CT `MI` (U6→S-CT) | — |
| MI | 3 | USUBJID | 264 | 一致 | 一致 | — |
| MI | 4 | MISEQ | 264 | 一致 | 一致 | — |
| MI | 5 | MIGRPID | 264 | 一致 | 一致 | — |
| MI | 6 | MIREFID | 264 | 一致 | 一致 | — |
| MI | 7 | MISPID | 264 | 一致 | 一致 | — |
| MI | 8 | MITESTCD | 264 | 一致 | `(MITSCD)` vs `C132263` (U5→S-CT) | — |
| MI | 9 | MITEST | 264 | 一致 | `(MITS)` vs `C132262` (U5→S-CT) | — |
| MI | 10 | MITSTDTL | 264 | 一致 | `(MIFTSDTL)` vs `C125922` (U5→S-CT) | — |
| MI | 11 | MICAT | 264 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| MI | 12 | MISCAT | 264 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| MI | 13 | MIORRES | 264 | 一致 | 一致 | — |
| MI | 14 | MIORRESU | 264 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| MI | 15 | MISTRESC | 264 | 一致 | 一致 | — |
| MI | 16 | MISTRESN | 264 | 一致 | 一致 | — |
| MI | 17 | MISTRESU | 264 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| MI | 18 | MIRESCAT | 264 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| MI | 19 | MISTAT | 264 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| MI | 20 | MIREASND | 264 | 一致 | 一致 | — |
| MI | 21 | MINAM | 264 | 一致 | 一致 | — |
| MI | 22 | MISPEC | 265 | 一致 | `(SPECTYPE)` vs `C78734` (U5→S-CT) | — |
| MI | 23 | MISPCCND | 265 | 一致 | `(SPECCOND)` vs `C78733` (U5→S-CT) | — |
| MI | 24 | MILOC | 265 | 一致 | `(LOC)` vs `C74456` (U5→S-CT) | — |
| MI | 25 | MILAT | 265 | 一致 | `(LAT)` vs `C99073` (U5→S-CT) | — |
| MI | 26 | MIDIR | 265 | 一致 | `(DIR)` vs `C99074` (U5→S-CT) | — |
| MI | 27 | MIMETHOD | 265 | 一致 | `(METHOD)` vs `C85492` (U5→S-CT) | — |
| MI | 28 | MILOBXFL | 265 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| MI | 29 | MIBLFL | 265 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| MI | 30 | MIEVAL | 265 | 一致 | `(EVAL)` vs `C78735` (U5→S-CT) | — |
| MI | 31 | VISITNUM | 265 | 一致 | 一致 | — |
| MI | 32 | VISIT | 265 | 一致 | 一致 | — |
| MI | 33 | VISITDY | 265 | 一致 | 一致 | — |
| MI | 34 | TAETORD | 265 | 一致 | 一致 | — |
| MI | 35 | EPOCH | 265 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| MI | 36 | MIDTC | 265 | 一致 | 一致 | — |
| MI | 37 | MIDY | 265 | 一致 | 一致 | — |
| CV | 1 | STUDYID | 286 | 一致 | 一致 | — |
| CV | 2 | DOMAIN | 287 | 一致 | DOMAIN CT `CV` (U6→S-CT) | — |
| CV | 3 | USUBJID | 287 | 一致 | 一致 | — |
| CV | 4 | CVSEQ | 287 | 一致 | 一致 | — |
| CV | 5 | CVGRPID | 287 | 一致 | 一致 | — |
| CV | 6 | CVREFID | 287 | 一致 | 一致 | — |
| CV | 7 | CVSPID | 287 | 一致 | 一致 | — |
| CV | 8 | CVLNKID | 287 | 一致 | 一致 | — |
| CV | 9 | CVLNKGRP | 287 | 一致 | 一致 | — |
| CV | 10 | CVTESTCD | 287 | 一致 | `(CVTESTCD)` vs `C101847` (U5→S-CT) | — |
| CV | 11 | CVTEST | 287 | 一致 | `(CVTEST)` vs `C101846` (U5→S-CT) | — |
| CV | 12 | CVCAT | 287 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| CV | 13 | CVSCAT | 287 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| CV | 14 | CVPOS | 287 | 一致 | `(POSITION)` vs `C71148` (U5→S-CT) | — |
| CV | 15 | CVORRES | 287 | 一致 | 一致 | — |
| CV | 16 | CVORRESU | 287 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| CV | 17 | CVSTRESC | 287 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| CV | 18 | CVSTRESN | 287 | 一致 | 一致 | — |
| CV | 19 | CVSTRESU | 287 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| CV | 20 | CVSTAT | 287 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| CV | 21 | CVREASND | 287 | 一致 | 一致 | — |
| CV | 22 | CVLOC | 287 | 一致 | `(LOC)` vs `C74456` (U5→S-CT) | — |
| CV | 23 | CVLAT | 287 | 一致 | `(LAT)` vs `C99073` (U5→S-CT) | — |
| CV | 24 | CVDIR | 287 | 一致 | `(DIR)` vs `C99074` (U5→S-CT) | — |
| CV | 25 | CVMETHOD | 287 | 一致 | `(METHOD)` vs `C85492` (U5→S-CT) | — |
| CV | 26 | CVLOBXFL | 288 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| CV | 27 | CVBLFL | 288 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| CV | 28 | CVDRVFL | 288 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| CV | 29 | CVEVAL | 288 | 一致 | `(EVAL)` vs `C78735` (U5→S-CT) | — |
| CV | 30 | CVEVALID | 288 | 一致 | `(MEDEVAL)` vs `C96777` (U5→S-CT) | — |
| CV | 31 | VISITNUM | 288 | 一致 | 一致 | — |
| CV | 32 | VISIT | 288 | 一致 | 一致 | — |
| CV | 33 | VISITDY | 288 | 一致 | 一致 | — |
| CV | 34 | TAETORD | 288 | 一致 | 一致 | — |
| CV | 35 | EPOCH | 288 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| CV | 36 | CVDTC | 288 | 一致 | 一致 | — |
| CV | 37 | CVDY | 288 | 一致 | 一致 | — |
| CV | 38 | CVTPT | 288 | 一致 | 一致 | — |
| CV | 39 | CVTPTNUM | 288 | 一致 | 一致 | — |
| CV | 40 | CVELTM | 288 | 一致 | 一致 | — |
| CV | 41 | CVTPTREF | 288 | 一致 | 一致 | — |
| CV | 42 | CVRFTDTC | 288 | 一致 | 一致 | — |
| MK | 1 | STUDYID | 290 | 一致 | 一致 | — |
| MK | 2 | DOMAIN | 290 | 一致 | DOMAIN CT `MK` (U6→S-CT) | — |
| MK | 3 | USUBJID | 290 | 一致 | 一致 | — |
| MK | 4 | MKSEQ | 290 | 一致 | 一致 | — |
| MK | 5 | MKGRPID | 290 | 一致 | 一致 | — |
| MK | 6 | MKREFID | 290 | 一致 | 一致 | — |
| MK | 7 | MKSPID | 290 | 一致 | 一致 | — |
| MK | 8 | MKLNKID | 290 | 一致 | 一致 | — |
| MK | 9 | MKLNKGRP | 290 | 一致 | 一致 | — |
| MK | 10 | MKTESTCD | 290 | 一致 | `(MUSCTSCD)` vs `C127269` (U5→S-CT) | — |
| MK | 11 | MKTEST | 290 | 一致 | `(MUSCTS)` vs `C127270` (U5→S-CT) | — |
| MK | 12 | MKCAT | 290 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| MK | 13 | MKSCAT | 290 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| MK | 14 | MKPOS | 290 | 一致 | `(POSITION)` vs `C71148` (U5→S-CT) | — |
| MK | 15 | MKORRES | 290 | 一致 | 一致 | — |
| MK | 16 | MKORRESU | 290 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| MK | 17 | MKSTRESC | 290 | 一致 | 一致 | — |
| MK | 18 | MKSTRESN | 290 | 一致 | 一致 | — |
| MK | 19 | MKSTRESU | 291 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| MK | 20 | MKSTAT | 291 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| MK | 21 | MKREASND | 291 | 一致 | 一致 | — |
| MK | 22 | MKLOC | 291 | 一致 | `(LOC)` vs `C74456` (U5→S-CT) | — |
| MK | 23 | MKLAT | 291 | 一致 | `(LAT)` vs `C99073` (U5→S-CT) | — |
| MK | 24 | MKDIR | 291 | 一致 | `(DIR)` vs `C99074` (U5→S-CT) | — |
| MK | 25 | MKMETHOD | 291 | 一致 | `(METHOD)` vs `C85492` (U5→S-CT) | — |
| MK | 26 | MKLOBXFL | 291 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| MK | 27 | MKBLFL | 291 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| MK | 28 | MKDRVFL | 291 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| MK | 29 | MKEVAL | 291 | 一致 | `(EVAL)` vs `C78735` (U5→S-CT) | — |
| MK | 30 | MKEVALID | 291 | 一致 | `(MEDEVAL)` vs `C96777` (U5→S-CT) | — |
| MK | 31 | VISITNUM | 291 | 一致 | 一致 | — |
| MK | 32 | VISIT | 291 | 一致 | 一致 | — |
| MK | 33 | VISITDY | 291 | 一致 | 一致 | — |
| MK | 34 | TAETORD | 291 | 一致 | 一致 | — |
| MK | 35 | EPOCH | 291 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| MK | 36 | MKDTC | 291 | 一致 | 一致 | — |
| MK | 37 | MKDY | 291 | 一致 | 一致 | — |
| MK | 38 | MKTPT | 291 | 一致 | 一致 | — |
| MK | 39 | MKTPTNUM | 291 | 一致 | 一致 | — |
| MK | 40 | MKELTM | 291 | 一致 | 一致 | — |
| MK | 41 | MKTPTREF | 291 | 一致 | 一致 | — |
| MK | 42 | MKRFTDTC | 291 | 一致 | 一致 | — |
| NV | 1 | STUDYID | 294 | 一致 | 一致 | — |
| NV | 2 | DOMAIN | 294 | 一致 | DOMAIN CT `NV` (U6→S-CT) | — |
| NV | 3 | USUBJID | 294 | 一致 | 一致 | — |
| NV | 4 | FOCID | 294 | 一致 | 一致 | — |
| NV | 5 | NVSEQ | 294 | 一致 | 一致 | — |
| NV | 6 | NVGRPID | 294 | 一致 | 一致 | — |
| NV | 7 | NVREFID | 294 | 一致 | 一致 | — |
| NV | 8 | NVSPID | 294 | 一致 | 一致 | — |
| NV | 9 | NVLNKID | 294 | 一致 | 一致 | — |
| NV | 10 | NVLNKGRP | 294 | 一致 | 一致 | — |
| NV | 11 | NVTESTCD | 294 | 一致 | `(NVTESTCD)` vs `C116104` (U5→S-CT) | — |
| NV | 12 | NVTEST | 295 | 一致 | `(NVTEST)` vs `C116103` (U5→S-CT) | — |
| NV | 13 | NVCAT | 295 | 一致 | 一致 | — |
| NV | 14 | NVSCAT | 295 | 一致 | 一致 | — |
| NV | 15 | NVORRES | 295 | 一致 | 一致 | — |
| NV | 16 | NVORRESU | 295 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| NV | 17 | NVSTRESC | 295 | 一致 | 一致 | — |
| NV | 18 | NVSTRESN | 295 | 一致 | 一致 | — |
| NV | 19 | NVSTRESU | 295 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| NV | 20 | NVSTAT | 295 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| NV | 21 | NVREASND | 295 | 一致 | 一致 | — |
| NV | 22 | NVLOC | 295 | 一致 | `(LOC)` vs `C74456` (U5→S-CT) | — |
| NV | 23 | NVLAT | 295 | 一致 | `(LAT)` vs `C99073` (U5→S-CT) | — |
| NV | 24 | NVDIR | 295 | 一致 | `(DIR)` vs `C99074` (U5→S-CT) | — |
| NV | 25 | NVMETHOD | 295 | 一致 | `(METHOD)` vs `C85492` (U5→S-CT) | — |
| NV | 26 | NVLOBXFL | 295 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| NV | 27 | NVBLFL | 295 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| NV | 28 | NVDRVFL | 295 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| NV | 29 | NVEVAL | 295 | 一致 | `(EVAL)` vs `C78735` (U5→S-CT) | — |
| NV | 30 | NVEVALID | 295 | 一致 | `(MEDEVAL)` vs `C96777` (U5→S-CT) | — |
| NV | 31 | VISITNUM | 295 | 一致 | 一致 | — |
| NV | 32 | VISIT | 295 | 一致 | 一致 | — |
| NV | 33 | VISITDY | 295 | 一致 | 一致 | — |
| NV | 34 | TAETORD | 295 | 一致 | 一致 | — |
| NV | 35 | EPOCH | 295 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| NV | 36 | NVDTC | 295 | 一致 | 一致 | — |
| NV | 37 | NVDY | 295 | 一致 | 一致 | — |
| NV | 38 | NVTPT | 295 | 一致 | 一致 | — |
| NV | 39 | NVTPTNUM | 296 | 一致 | 一致 | — |
| NV | 40 | NVELTM | 296 | 一致 | 一致 | — |
| NV | 41 | NVTPTREF | 296 | 一致 | 一致 | — |
| NV | 42 | NVRFTDTC | 296 | 一致 | 一致 | — |
| RP | 1 | STUDYID | 305 | 一致 | 一致 | — |
| RP | 2 | DOMAIN | 305 | 一致 | DOMAIN CT `RP` (U6→S-CT) | — |
| RP | 3 | USUBJID | 305 | 一致 | 一致 | — |
| RP | 4 | RPSEQ | 305 | 一致 | 一致 | — |
| RP | 5 | RPGRPID | 305 | 一致 | 一致 | — |
| RP | 6 | RPREFID | 305 | 一致 | 一致 | — |
| RP | 7 | RPSPID | 305 | 一致 | 一致 | — |
| RP | 8 | RPLNKID | 305 | 一致 | 一致 | — |
| RP | 9 | RPLNKGRP | 305 | 一致 | 一致 | — |
| RP | 10 | RPTESTCD | 305 | 一致 | `(RPTESTCD)` vs `C106479` (U5→S-CT) | — |
| RP | 11 | RPTEST | 305 | 一致 | `(RPTEST)` vs `C106478` (U5→S-CT) | — |
| RP | 12 | RPCAT | 305 | 一致 | 一致 | — |
| RP | 13 | RPSCAT | 305 | 一致 | 一致 | — |
| RP | 14 | RPORRES | 305 | 一致 | 一致 | — |
| RP | 15 | RPORRESU | 305 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| RP | 16 | RPSTRESC | 306 | 一致 | 一致 | — |
| RP | 17 | RPSTRESN | 306 | 一致 | 一致 | — |
| RP | 18 | RPSTRESU | 306 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| RP | 19 | RPSTAT | 306 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| RP | 20 | RPREASND | 306 | 一致 | 一致 | — |
| RP | 21 | RPLOBXFL | 306 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| RP | 22 | RPBLFL | 306 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| RP | 23 | RPDRVFL | 306 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| RP | 24 | VISITNUM | 306 | 一致 | 一致 | — |
| RP | 25 | VISIT | 306 | 一致 | 一致 | — |
| RP | 26 | VISITDY | 306 | 一致 | 一致 | — |
| RP | 27 | TAETORD | 306 | 一致 | 一致 | — |
| RP | 28 | EPOCH | 306 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| RP | 29 | RPDTC | 306 | 一致 | 一致 | — |
| RP | 30 | RPDY | 306 | 一致 | 一致 | — |
| RP | 31 | RPDUR | 306 | 一致 | 一致 | — |
| RP | 32 | RPTPT | 306 | 一致 | 一致 | — |
| RP | 33 | RPTPTNUM | 306 | 一致 | 一致 | — |
| RP | 34 | RPELTM | 306 | 一致 | 一致 | — |
| RP | 35 | RPTPTREF | 306 | 一致 | 一致 | — |
| RP | 36 | RPRFTDTC | 306 | 一致 | 一致 | — |
| RE | 1 | STUDYID | 308 | 一致 | 一致 | — |
| RE | 2 | DOMAIN | 308 | 一致 | DOMAIN CT `RE` (U6→S-CT) | — |
| RE | 3 | USUBJID | 308 | 一致 | 一致 | — |
| RE | 4 | SPDEVID | 308 | 一致 | 一致 | — |
| RE | 5 | RESEQ | 308 | 一致 | 一致 | — |
| RE | 6 | REGRPID | 308 | 一致 | 一致 | — |
| RE | 7 | REREFID | 308 | 一致 | 一致 | — |
| RE | 8 | RESPID | 308 | 一致 | 一致 | — |
| RE | 9 | RELNKID | 308 | 一致 | 一致 | — |
| RE | 10 | RELNKGRP | 308 | 一致 | 一致 | — |
| RE | 11 | RETESTCD | 308 | 一致 | `(RETESTCD)` vs `C111106` (U5→S-CT) | — |
| RE | 12 | RETEST | 308 | 一致 | `(RETEST)` vs `C111107` (U5→S-CT) | — |
| RE | 13 | RECAT | 308 | 一致 | 一致 | — |
| RE | 14 | RESCAT | 308 | 一致 | 一致 | — |
| RE | 15 | REPOS | 308 | 一致 | `(POSITION)` vs `C71148` (U5→S-CT) | — |
| RE | 16 | REORRES | 308 | 一致 | 一致 | — |
| RE | 17 | REORRESU | 308 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| RE | 18 | REORREF | 308 | 一致 | 一致 | — |
| RE | 19 | RESTRESC | 308 | 一致 | 一致 | — |
| RE | 20 | RESTRESN | 308 | 一致 | 一致 | — |
| RE | 21 | RESTRESU | 309 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| RE | 22 | RESTREFC | 309 | 一致 | 一致 | — |
| RE | 23 | RESTREFN | 309 | 一致 | 一致 | — |
| RE | 24 | RESTAT | 309 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| RE | 25 | REREASND | 309 | 一致 | 一致 | — |
| RE | 26 | RELOC | 309 | 一致 | `(LOC)` vs `C74456` (U5→S-CT) | — |
| RE | 27 | RELAT | 309 | 一致 | `(LAT)` vs `C99073` (U5→S-CT) | — |
| RE | 28 | REDIR | 309 | 一致 | `(DIR)` vs `C99074` (U5→S-CT) | — |
| RE | 29 | REMETHOD | 309 | 一致 | `(METHOD)` vs `C85492` (U5→S-CT) | — |
| RE | 30 | RELOBXFL | 309 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| RE | 31 | REBLFL | 309 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| RE | 32 | REDRVFL | 309 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| RE | 33 | REEVAL | 309 | 一致 | `(EVAL)` vs `C78735` (U5→S-CT) | — |
| RE | 34 | REEVALID | 309 | 一致 | `(MEDEVAL)` vs `C96777` (U5→S-CT) | — |
| RE | 35 | REREPNUM | 309 | 一致 | 一致 | — |
| RE | 36 | VISITNUM | 309 | 一致 | 一致 | — |
| RE | 37 | VISIT | 309 | 一致 | 一致 | — |
| RE | 38 | VISITDY | 309 | 一致 | 一致 | — |
| RE | 39 | TAETORD | 309 | 一致 | 一致 | — |
| RE | 40 | EPOCH | 309 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| RE | 41 | REDTC | 309 | 一致 | 一致 | — |
| RE | 42 | REDY | 309 | 一致 | 一致 | — |
| RE | 43 | RETPT | 309 | 一致 | 一致 | — |
| RE | 44 | RETPTNUM | 310 | 一致 | 一致 | — |
| RE | 45 | REELTM | 310 | 一致 | 一致 | — |
| RE | 46 | RETPTREF | 310 | 一致 | 一致 | — |
| RE | 47 | RERFTDTC | 310 | 一致 | 一致 | — |
| FT | 1 | STUDYID | 319 | 一致 | 一致 | — |
| FT | 2 | DOMAIN | 319 | 一致 | DOMAIN CT `FT` (U6→S-CT) | — |
| FT | 3 | USUBJID | 319 | 一致 | 一致 | — |
| FT | 4 | FTSEQ | 319 | 一致 | 一致 | — |
| FT | 5 | FTGRPID | 319 | 一致 | 一致 | — |
| FT | 6 | FTREFID | 319 | 一致 | 一致 | — |
| FT | 7 | FTSPID | 319 | 一致 | 一致 | — |
| FT | 8 | FTTESTCD | 319 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| FT | 9 | FTTEST | 319 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| FT | 10 | FTCAT | 319 | 一致 | `(FTCAT)` vs `C115304` (U5→S-CT) | — |
| FT | 11 | FTSCAT | 319 | 一致 | 一致 | — |
| FT | 12 | FTPOS | 319 | 一致 | `(POSITION)` vs `C71148` (U5→S-CT) | — |
| FT | 13 | FTORRES | 319 | 一致 | 一致 | — |
| FT | 14 | FTORRESU | 319 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| FT | 15 | FTSTRESC | 319 | 一致 | 一致 | — |
| FT | 16 | FTSTRESN | 319 | 一致 | 一致 | — |
| FT | 17 | FTSTRESU | 320 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| FT | 18 | FTSTAT | 320 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| FT | 19 | FTREASND | 320 | 一致 | 一致 | — |
| FT | 20 | FTXFN | 320 | 一致 | 一致 | — |
| FT | 21 | FTNAM | 320 | 一致 | 一致 | — |
| FT | 22 | FTMETHOD | 320 | 一致 | `(QRSMTHOD)` vs `C158113` (U5→S-CT) | — |
| FT | 23 | FTLOBXFL | 320 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| FT | 24 | FTBLFL | 320 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| FT | 25 | FTDRVFL | 320 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| FT | 26 | FTREPNUM | 320 | 一致 | 一致 | — |
| FT | 27 | VISITNUM | 320 | 一致 | 一致 | — |
| FT | 28 | VISIT | 320 | 一致 | 一致 | — |
| FT | 29 | VISITDY | 320 | 一致 | 一致 | — |
| FT | 30 | TAETORD | 320 | 一致 | 一致 | — |
| FT | 31 | EPOCH | 320 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| FT | 32 | FTDTC | 320 | 一致 | 一致 | — |
| FT | 33 | FTDY | 320 | 一致 | 一致 | — |
| FT | 34 | FTTPT | 320 | 一致 | 一致 | — |
| FT | 35 | FTTPTNUM | 320 | 一致 | 一致 | — |
| FT | 36 | FTELTM | 320 | 一致 | 一致 | — |
| FT | 37 | FTTPTREF | 320 | 一致 | 一致 | — |
| FT | 38 | FTRFTDTC | 320 | 一致 | 一致 | — |
| QS | 1 | STUDYID | 324 | 一致 | 一致 | — |
| QS | 2 | DOMAIN | 324 | 一致 | DOMAIN CT `QS` (U6→S-CT) | — |
| QS | 3 | USUBJID | 324 | 一致 | 一致 | — |
| QS | 4 | QSSEQ | 324 | 一致 | 一致 | — |
| QS | 5 | QSGRPID | 324 | 一致 | 一致 | — |
| QS | 6 | QSSPID | 324 | 一致 | 一致 | — |
| QS | 7 | QSTESTCD | 324 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| QS | 8 | QSTEST | 324 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| QS | 9 | QSCAT | 324 | 一致 | `(QSCAT)` vs `C100129` (U5→S-CT) | — |
| QS | 10 | QSSCAT | 324 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| QS | 11 | QSORRES | 324 | 一致 | 一致 | — |
| QS | 12 | QSORRESU | 325 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| QS | 13 | QSSTRESC | 325 | 一致 | 一致 | — |
| QS | 14 | QSSTRESN | 325 | 一致 | 一致 | — |
| QS | 15 | QSSTRESU | 325 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| QS | 16 | QSSTAT | 325 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| QS | 17 | QSREASND | 325 | 一致 | 一致 | — |
| QS | 18 | QSMETHOD | 325 | 一致 | `(QRSMTHOD)` vs `C158113` (U5→S-CT) | — |
| QS | 19 | QSLOBXFL | 325 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| QS | 20 | QSBLFL | 325 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| QS | 21 | QSDRVFL | 325 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| QS | 22 | VISITNUM | 325 | 一致 | 一致 | — |
| QS | 23 | VISIT | 325 | 一致 | 一致 | — |
| QS | 24 | VISITDY | 325 | 一致 | 一致 | — |
| QS | 25 | TAETORD | 325 | 一致 | 一致 | — |
| QS | 26 | EPOCH | 325 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| QS | 27 | QSDTC | 325 | 一致 | 一致 | — |
| QS | 28 | QSDY | 325 | 一致 | 一致 | — |
| QS | 29 | QSTPT | 325 | 一致 | 一致 | — |
| QS | 30 | QSTPTNUM | 325 | 一致 | 一致 | — |
| QS | 31 | QSELTM | 325 | 一致 | 一致 | — |
| QS | 32 | QSTPTREF | 326 | 一致 | 一致 | — |
| QS | 33 | QSRFTDTC | 326 | 一致 | 一致 | — |
| QS | 34 | QSEVLINT | 326 | 一致 (PDF `"- P2Y"` 为折行连字符, KB `"-P2Y"` 正确) | 一致 | — |
| QS | 35 | QSEVINTX | 326 | 一致 | 一致 | — |

### 逐页双向扫描日志
| 页 | 节 | PDF→KB: 变量/命中, 缺→已补 | KB→PDF: 对应 KB 段, 无出处→处理 | 表 | 备注 |
|---|---|---|---|---|---|
| 264 | MI spec | 21 / 21; `*` 3→3 (MICAT MISCAT MIRESCAT) | STUDYID..MINAM; 0 | bbox + 裁图 | U5 6; U6 1 |
| 265 | MI spec | 16 / 16; 脚注 1→1 | MISPEC..MIDY + 脚注; 0 | bbox | U5 10 |
| 286 | CV spec | 1 / 1 | STUDYID..STUDYID; 0 | bbox | 页上半 §6.3.7.1 通用表 (NV/assumptions.md, 非本批) |
| 287 | CV spec | 24 / 24; `*` 3→3 (CVCAT CVSCAT CVSTRESC) | DOMAIN..CVMETHOD; 0 | bbox + 裁图 | U5 10; U6 1 |
| 288 | CV spec | 17 / 17; 脚注 1→1 | CVLOBXFL..CVRFTDTC + 脚注; 0 | bbox | U5 6 |
| 290 | MK spec | 18 / 18; `*` 2→2 (MKCAT MKSCAT) | STUDYID..MKSTRESN; 0 | bbox + 裁图 | U5 4; U6 1 |
| 291 | MK spec | 24 / 24; 脚注 1→1 | MKSTRESU..MKRFTDTC + 脚注; 0 | bbox | U5 12 |
| 294 | NV spec | 11 / 11 | STUDYID..NVTESTCD; 0 | bbox | U5 1; U6 1 |
| 295 | NV spec | 27 / 27 | NVTEST..NVTPT; 0 | bbox + 裁图 | U5 14 |
| 296 | NV spec | 4 / 4; 脚注 1→1 | NVTPTNUM..NVRFTDTC + 脚注; 0 | bbox |  |
| 305 | RP spec | 15 / 15 | STUDYID..RPORRESU; 0 | bbox + 裁图 | U5 3; U6 1 |
| 306 | RP spec | 21 / 21; 脚注 1→1 | RPSTRESC..RPRFTDTC + 脚注; 0 | bbox | U5 6 |
| 308 | RE spec | 20 / 20 | STUDYID..RESTRESN; 0 | bbox + 裁图 | U5 4; U6 1 |
| 309 | RE spec | 23 / 23 | RESTRESU..RETPT; 0 | bbox | U5 12 |
| 310 | RE spec | 4 / 4; 脚注 1→1 | RETPTNUM..RERFTDTC + 脚注; 0 | bbox |  |
| 319 | FT spec | 16 / 16; `*` 2→2 (FTTESTCD FTTEST) | STUDYID..FTSTRESN; 0 | bbox + 裁图 | U5 3; U6 1 |
| 320 | FT spec | 22 / 22; 脚注 1→1 | FTSTRESU..FTRFTDTC + 脚注; 0 | bbox | U5 7 |
| 324 | QS spec | 11 / 11; `*` 3→3 (QSTESTCD QSTEST QSSCAT) | STUDYID..QSORRES; 0 | bbox + 裁图 | U5 1; U6 1; 页顶 FT 例尾 (非本批) |
| 325 | QS spec | 20 / 20 | QSORRESU..QSELTM; 0 | bbox | U5 8 |
| 326 | QS spec | 4 / 4; 脚注 1→1 | QSTPTREF..QSEVINTX + 脚注; 0 | bbox | QSEVLINT 折行连字符 |
注: 每页变量数 = 变量起始行所在页 (sc2w 输出机械生成, `vartable.md`).

## 变更清单
| # | kb_file:line (改后) | ref | action | before → after | PDF 页 |
|---|---|---|---|---|---|
| 1 | MI/spec.md:99/108/162 | pdf:p264 CT 列 (MICAT MISCAT MIRESCAT) | REPLACED | CT 空 → `*` ×3 | 264 |
| 2 | MI/spec.md:339 | page_txt p265 脚注 | INSERTED | 脚注 `> ¹In this column, …` (`---` 后, Cross References 前; gap F) | 265 |
| 3 | CV/spec.md:108/117/153 | pdf:p287 CT 列 (CVCAT CVSCAT CVSTRESC) | REPLACED | 空 → `*` ×3 | 287 |
| 4 | CV/spec.md:384 | ig34_p0288_a018 | INSERTED | 脚注 | 288 |
| 5 | MK/spec.md:108/117 | pdf:p290 CT 列 (MKCAT MKSCAT) | REPLACED | 空 → `*` ×2 | 290 |
| 6 | MK/spec.md:384 | ig34_p0291_a025 | INSERTED | 脚注 | 291 |
| 7 | NV/spec.md:384 | pdf:p296:脚注 (gaps 未列, 全扫新增) | INSERTED | 脚注 | 296 |
| 8 | RP/spec.md:330 | ig34_p0306_a022 | INSERTED | 脚注 | 306 |
| 9 | RE/spec.md:429 | ig34_p0310_a005 | INSERTED | 脚注 | 310 |
| 10 | FT/spec.md:72/81 | pdf:p319 CT 列 (FTTESTCD FTTEST) | REPLACED | 空 → `*` ×2 | 319 |
| 11 | FT/spec.md:348 | ig34_p0320_a023 | INSERTED | 脚注 | 320 |
| 12 | QS/spec.md:63/72/90 | pdf:p324 CT 列 (QSTESTCD QSTEST QSSCAT) | REPLACED | 空 → `*` ×3 | 324 |
| 13 | QS/spec.md:321 | ig34_p0326_a005 | INSERTED | 脚注 | 326 |
- 合计 21 处 (CT `*` 13 + 脚注 8). 脚注文字取自 bbox 原词 (8 页文字相同, sc2w `FOOT` 8 页均有独立词 "1"), 上标 ¹ 经渲染 `fn310-310.png` 确认; 格式与 S-SPEC2 / CE 先例逐字一致.
- 新增 atom 清单: NV 脚注 (pdf:p296) — batch json `gaps` 未列 NV, 全扫发现并补.

## 结构改动清单
无 (无变量增删/挪位; 无标题改动).

## 删除清单
无 (13 处 REPLACED 的旧值均为空串).

## D6 标注清单
无新增. 8 文件 `> Class|Structure` 行 + Cross References 按 U8 为导航, 不标.

## PDF_TYPO 清单
无. (QSEVLINT Notes `"- P2Y"` = PDF 折行连字符 (p326), 非笔误, KB `"-P2Y"` 不改.)

## 范围外发现
- 无 KB 内容错.
- 工具: `speccmp2.py` 两盲区再现 (一页两表头取第一个 / 表头下首行丢 `or` 等表头词), 已用 sc2w + 渲染排除; sc2w 本批无误报. 未改共享工具.
- NV/assumptions.md:44 的 `> ¹In this column…` 是 §6.3.7.1 通用表 (p286) 的脚注, 按 brief 属 assumptions.md, 不迁; NV spec 表自己的脚注 (p296) 已补入 NV/spec.md, 两处并存为各自表的脚注, 非重复.

## out_of_scope 处理 (O15 / O21 / O24 / O26)
- O15 / O26 (spec 表脚注): 本批 8 域全补 → 8 域关闭. spec 首句不属 spec-only 批 (各域 assumptions.md 已终版).
- O24: 本批 8 域 CT `*` 全补 (13); C-code 记法 → U5 S-CT.
- O21 (FA/spec) 不在本批 units, 本批不处理.

## 需主控定
无.

## git diff --stat
 knowledge_base/domains/CV/spec.md | 8 +++++---
 knowledge_base/domains/FT/spec.md | 6 ++++--
 knowledge_base/domains/MI/spec.md | 8 +++++---
 knowledge_base/domains/MK/spec.md | 6 ++++--
 knowledge_base/domains/NV/spec.md | 2 ++
 knowledge_base/domains/QS/spec.md | 8 +++++---
 knowledge_base/domains/RE/spec.md | 2 ++
 knowledge_base/domains/RP/spec.md | 2 ++
 8 files changed, 29 insertions(+), 13 deletions(-)

## 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC3_writer
P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
for p in 264 265 286 287 288 290 291 294 295 296 305 306 308 309 310 319 320 324 325 326; do pdftotext -bbox -f $p -l $p "$P" $S/bb_$p.html; done
bash $S/run.sh sc2w.py      # 或 speccmp2.py; run.sh 内为 "MI 264,265" "CV 286,287,288" "MK 290,291" "NV 294,295,296" "RP 305,306" "RE 308,309,310" "FT 319,320" "QS 324,325,326"
python3 $S/stars.py $S/bb_{264,265,286,287,288,290,291,294,295,296,305,306,308,309,310,319,320,324,325,326}.html
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```
