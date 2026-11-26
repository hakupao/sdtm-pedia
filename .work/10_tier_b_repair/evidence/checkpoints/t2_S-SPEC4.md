# T2S 扫描批 S-SPEC4 (spec-only: RS SC TU VS SUPPQUAL TE TI TS + 主控追加 TV) — writer attempt 1

> 2026-11-26, oh-my-claudecode:executor (opus). Brief `subagent_prompts/t2s_scan_writer_v1.0.md`; 批次 `work/t2_batches/S-SPEC4.json` (TV 由主控中途追加).
> 只改 9 个 spec.md; assumptions/examples 未碰; 未 stash/checkout/commit. 基线 = `git show HEAD:<file>` (9 文件改前与 HEAD 一致, cmp 核).
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC4_writer/`
> (bb_N.html = `pdftotext -bbox`; sc2w.py / speccmp2.py = `work/scratch/t2s_tools/` 副本; sc2w_s.py = sc2w 放宽表头识别 (见方法); cmpw_*/cmp2_* before/after; ct_N-N.png = 左半页裁图 90dpi; base/ = HEAD 副本; apply.py / apply_tv.py 精确替换+命中断言; vartable.md = 下表生成源)

md5 改后: RS `060f0df3b8cee7941831be3d8630fb1f` (448→450) · SC `8196d21d56ed020d8d98716e9ec9f468` (239→241) · TU `b801ef8cd0accecdbcc9320e6cf7069e` (312→314) · VS `9965376bdf335ff3d77692971bb07e7c` (369→371) · SUPPQUAL `2bd1968e1284994020b13f33b133ce93` (113→115) · TE `0fa6518769a340c986e3754025eabbe8` (80→82) · TI `d9fc7336023f904bd43618bdcfd93fe3` (91→93) · TS `e580a8e83b48bf8792108d63420d5944` (121→123) · TV `79af24c222af4213ed3b8c9bc0407415` (99→101)

## 完整节页范围 (O20 复核; 本批只扫各域 spec 表)
| 域 | 节 (json lo-hi) | spec 表所在页 (复核) | 起止依据 (layout `work/pdf_pages/ig34_pNNNN.txt`) |
|---|---|---|---|
| RS | §6.3.9.3 (329-339) | **329-332** | p329:8 节标题, :17 `RS – Specification`, :20 表头; p330/331/332 续表 (p330 首行为 RSTESTCD Notes 续行); p332:9 脚注, :16 §6.3.9.3.1 |
| SC | §6.3.10 (339-342) | **340-341** | p339:39 节标题 (页尾); p340:1 `SC – Specification`, :3 表头; p341:11 脚注, :14 `SC – Assumptions` |
| TU | §6.3.12.1 (344-350) | **345-346** | p344:29 节标题; p345:5 `TU – Specification`, :7 表头; p346:34 脚注, :39 `TU – Assumptions` |
| VS | §6.3.13 (358-361) | **358-360** | p358:28 节标题, :31 spec 标题, :33 表头; p360:11 脚注, :16 `VS – Assumptions` |
| SUPPQUAL | §8.4 (431-434) | **432** | p432:21 §8.4.1 标题, :25 表头 (缩进, 两行表头), :63 脚注 (上标 "1" 独立行); p433:15 §8.4.2 |
| TE | §7.2.2 (402-407) | **403** | p402:50 节标题; p403:16 `TE – Specification`, :18 表头, :39 脚注, :44 `TE – Assumptions` |
| TI | §7.4.1 (416-417) | **416** | p416:1 节标题, :14 spec 标题, :16 表头, :42 脚注, :47 `TI – Assumptions` |
| TS | §7.4.2 (417-425) | **417-418** | p417:22 节标题, :30 spec 标题, :32 表头; p418:18 脚注, :23 `TS – Assumptions` |
| TV | §7.3.1 (407-410, 主控追加) | **407-408** | p407:34 节标题, :40 spec 标题, :42 表头; p408 第二表头后 ARMCD..TVENRL, :23 脚注, :27 `TV – Assumptions` |
- 边界页上别节内容 (p329 RS 前文, p339 SC 前 RS 例, p342 SS, p344 §6.3.12 引言, p350 TR, p358 前文, p361 §6.4, p402 TA Issues, p407 TE 尾/§7.3 引言, p417 TI 例, p431 §8.3.1, p433-434 §8.4.2-8.4.4) 不归本批 (spec-only).

## 方法
- 每域两套独立 bbox 列解析交叉: `sc2w.py` (空格敏感, 折行连字符小写间合并) + `speccmp2.py` (表头词过滤, 处理续页 CONT). SUPPQUAL p432 / TV p407 表头缩进且 "Label" 不与 "Variable" 同行 → 原 sc2w 判 "no header" 崩; `sc2w_s.py` 仅改表头判据 (x<100, 同行含 "Type") 后正常. speccmp2 对 SUPPQUAL/TV 原生可用.
- 计数闸: 两脚本均报 PDF 变量数 = KB 变量数, 顺序一致, KB Order 1..n 连续 (9 域).
- 两脚本残留差异逐条用 layout 文本核, 全部为工具假阳性: RSTESTCD (sc2 漏 p330 续行; speccmp2 CONT 段与 KB 一致) / RSCAT "CHILD- PUGH" 与 RSSTRESN "-- STRESC" (PDF 折行) / RSEVAL "Role"、RSENRTPT "or"、VSSCAT "or" (speccmp2 把正文里的表头同形词 Role/or 过滤掉; layout p331:3 p332:3 p359:3 原文均含) / TV VISITDY CT "Format 1" (speccmp2 把 p408 表头残词当续行).
- 续页首行核 (layout): p331 RSEVAL, p332 RSENRTPT, p346 TUMETHOD, p359 VSSCAT, p360 VSTPTNUM, p408 ARMCD 直接以变量开头; p341/p418 首行为表头残词 "or Format1"; 唯 p330 有 RSTESTCD Notes 续行 (已核一致).
- CT `*`: bbox 全 18 页搜 `*` 词并取同行变量名 → 17 处 (下表), 全部为 KB 空; 裁图人工看 p330 (RS 无 `*`, RSCAT 双 codelist) p359 p417 p432 与 bbox 一致. RS/TU 的 spec 表无 `*`.
- KB 结构: 9 文件各变量块 7 字段; 变量块外仅 H1 / `> Class|Structure` / SUPPQUAL `> Source text` (D7) / `---` / Cross References (U8 导航).

## 双向全扫 (每域 spec 表逐变量结果表; 改后 sc2w/sc2w_s)
PDF→KB: 184/184 变量命中, 顺序一致, Order 1..N 连续; KB→PDF: kb-only 变量 0, kb-only 字段 0. Label/Type/Role/Core/CDISC Notes **零差异** (改前亦零).
CT 列剩余差异全部为 U5 (C-code vs PDF 括号短名, 56 处; 含 SUPPQUAL RDOMAIN `(DOMAIN)`) / U6 (DOMAIN, 8 处) → 归 S-CT, 本批不改.

| 域 | spec 页 | PDF 变量 | KB 变量 | 顺序 | 字段差异 (改前) | CT `*` 补 | 脚注 | U5 / U6 留 S-CT |
|---|---|---|---|---|---|---|---|---|
| RS | 329-332 | 46 | 46 | 一致 | 0 | 0 | 补 | 17 / 1 |
| SC | 340-341 | 24 | 24 | 一致 | 0 | 2 | 补 | 6 / 1 |
| TU | 345-346 | 31 | 31 | 一致 | 0 | 0 | 补 | 14 / 1 |
| VS | 358-360 | 38 | 38 | 一致 | 0 | 4 | 补 | 13 / 1 |
| SUPPQUAL | 432 | 10 | 10 | 一致 | 0 | 2 | 补 | 2 / 0 |
| TE | 403 | 7 | 7 | 一致 | 0 | 2 | 补 | 0 / 1 |
| TI | 416 | 8 | 8 | 一致 | 0 | 3 | 补 | 1 / 1 |
| TS | 417-418 | 11 | 11 | 一致 | 0 | 2 | 补 | 3 / 1 |
| TV | 407-408 | 9 | 9 | 一致 | 0 | 2 | 补 | 0 / 1 |
| 计 | 18 页 | 184 | 184 | | 0 | 17 | 9 | 56 / 8 |

### 逐变量结果
| 域 | # | 变量 | PDF 页 | Order/Label/Type/Role/Core/CDISC Notes | CT 列 | 处理 |
|---|---|---|---|---|---|---|
| RS | 1 | STUDYID | 329 | 一致 | 一致 | — |
| RS | 2 | DOMAIN | 329 | 一致 | DOMAIN CT `RS` (U6→S-CT) | — |
| RS | 3 | USUBJID | 329 | 一致 | 一致 | — |
| RS | 4 | RSSEQ | 329 | 一致 | 一致 | — |
| RS | 5 | RSGRPID | 329 | 一致 | 一致 | — |
| RS | 6 | RSREFID | 329 | 一致 | 一致 | — |
| RS | 7 | RSSPID | 329 | 一致 | 一致 | — |
| RS | 8 | RSLNKID | 329 | 一致 | 一致 | — |
| RS | 9 | RSLNKGRP | 329 | 一致 | 一致 | — |
| RS | 10 | RSTESTCD | 329 | 一致 (Notes 跨 p329-330; sc2 漏续页, speccmp2 CONT 段 + layout 核一致) | `(ONCRTSCD)` vs `C96782` (U5→S-CT) | — |
| RS | 11 | RSTEST | 330 | 一致 | `(ONCRTS)` vs `C96781` (U5→S-CT) | — |
| RS | 12 | RSCAT | 330 | 一致 (PDF "CHILD- PUGH" 折行连字符) | `(ONCRSCAT)(CCCAT)` vs `C124298; C118971` (U5→S-CT) | — |
| RS | 13 | RSSCAT | 330 | 一致 | 一致 | — |
| RS | 14 | RSORRES | 330 | 一致 | 一致 | — |
| RS | 15 | RSORRESU | 330 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| RS | 16 | RSSTRESC | 330 | 一致 | `(ONCRSR)` vs `C96785` (U5→S-CT) | — |
| RS | 17 | RSSTRESN | 330 | 一致 (PDF "-- STRESC" 折行) | 一致 | — |
| RS | 18 | RSSTRESU | 330 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| RS | 19 | RSSTAT | 330 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| RS | 20 | RSREASND | 330 | 一致 | 一致 | — |
| RS | 21 | RSNAM | 330 | 一致 | 一致 | — |
| RS | 22 | RSMETHOD | 330 | 一致 | `(QRSMTHOD)` vs `C158113` (U5→S-CT) | — |
| RS | 23 | RSLOBXFL | 330 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| RS | 24 | RSBLFL | 330 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| RS | 25 | RSDRVFL | 330 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| RS | 26 | RSEVAL | 331 | 一致 (speccmp2 丢 "Role" = 表头词过滤 FP, layout p331:3 核) | `(EVAL)` vs `C78735` (U5→S-CT) | — |
| RS | 27 | RSEVALID | 331 | 一致 | `(MEDEVAL)` vs `C96777` (U5→S-CT) | — |
| RS | 28 | RSACPTFL | 331 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| RS | 29 | VISITNUM | 331 | 一致 | 一致 | — |
| RS | 30 | VISIT | 331 | 一致 | 一致 | — |
| RS | 31 | VISITDY | 331 | 一致 | 一致 | — |
| RS | 32 | TAETORD | 331 | 一致 | 一致 | — |
| RS | 33 | EPOCH | 331 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| RS | 34 | RSDTC | 331 | 一致 | 一致 | — |
| RS | 35 | RSDY | 331 | 一致 | 一致 | — |
| RS | 36 | RSTPT | 331 | 一致 | 一致 | — |
| RS | 37 | RSTPTNUM | 331 | 一致 | 一致 | — |
| RS | 38 | RSELTM | 331 | 一致 | 一致 | — |
| RS | 39 | RSTPTREF | 331 | 一致 | 一致 | — |
| RS | 40 | RSRFTDTC | 331 | 一致 | 一致 | — |
| RS | 41 | RSEVLINT | 331 | 一致 | 一致 | — |
| RS | 42 | RSEVINTX | 331 | 一致 | 一致 | — |
| RS | 43 | RSSTRTPT | 331 | 一致 | `(STENRF)` vs `C66728` (U5→S-CT) | — |
| RS | 44 | RSSTTPT | 331 | 一致 | 一致 | — |
| RS | 45 | RSENRTPT | 332 | 一致 (speccmp2 丢 "or" = 表头词过滤 FP, layout p332:3 核) | `(STENRF)` vs `C66728` (U5→S-CT) | — |
| RS | 46 | RSENTPT | 332 | 一致 | 一致 | — |
| SC | 1 | STUDYID | 340 | 一致 | 一致 | — |
| SC | 2 | DOMAIN | 340 | 一致 | DOMAIN CT `SC` (U6→S-CT) | — |
| SC | 3 | USUBJID | 340 | 一致 | 一致 | — |
| SC | 4 | SCSEQ | 340 | 一致 | 一致 | — |
| SC | 5 | SCGRPID | 340 | 一致 | 一致 | — |
| SC | 6 | SCSPID | 340 | 一致 | 一致 | — |
| SC | 7 | SCTESTCD | 340 | 一致 | `(SCTESTCD)` vs `C74559` (U5→S-CT) | — |
| SC | 8 | SCTEST | 340 | 一致 | `(SCTEST)` vs `C103330` (U5→S-CT) | — |
| SC | 9 | SCCAT | 340 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| SC | 10 | SCSCAT | 340 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| SC | 11 | SCORRES | 340 | 一致 | 一致 | — |
| SC | 12 | SCORRESU | 340 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| SC | 13 | SCSTRESC | 340 | 一致 | 一致 | — |
| SC | 14 | SCSTRESN | 340 | 一致 | 一致 | — |
| SC | 15 | SCSTRESU | 340 | 一致 | `(UNIT)` vs `C71620` (U5→S-CT) | — |
| SC | 16 | SCSTAT | 340 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| SC | 17 | SCREASND | 340 | 一致 | 一致 | — |
| SC | 18 | VISITNUM | 340 | 一致 | 一致 | — |
| SC | 19 | VISIT | 340 | 一致 | 一致 | — |
| SC | 20 | VISITDY | 340 | 一致 | 一致 | — |
| SC | 21 | TAETORD | 341 | 一致 | 一致 | — |
| SC | 22 | EPOCH | 341 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| SC | 23 | SCDTC | 341 | 一致 | 一致 | — |
| SC | 24 | SCDY | 341 | 一致 | 一致 | — |
| TU | 1 | STUDYID | 345 | 一致 | 一致 | — |
| TU | 2 | DOMAIN | 345 | 一致 | DOMAIN CT `TU` (U6→S-CT) | — |
| TU | 3 | USUBJID | 345 | 一致 | 一致 | — |
| TU | 4 | TUSEQ | 345 | 一致 | 一致 | — |
| TU | 5 | TUGRPID | 345 | 一致 | 一致 | — |
| TU | 6 | TUREFID | 345 | 一致 | 一致 | — |
| TU | 7 | TUSPID | 345 | 一致 | 一致 | — |
| TU | 8 | TULNKID | 345 | 一致 | 一致 | — |
| TU | 9 | TULNKGRP | 345 | 一致 | 一致 | — |
| TU | 10 | TUTESTCD | 345 | 一致 | `(TUTESTCD)` vs `C96784` (U5→S-CT) | — |
| TU | 11 | TUTEST | 345 | 一致 | `(TUTEST)` vs `C96783` (U5→S-CT) | — |
| TU | 12 | TUORRES | 345 | 一致 | 一致 | — |
| TU | 13 | TUSTRESC | 345 | 一致 | `(TUIDRS)` vs `C123650` (U5→S-CT) | — |
| TU | 14 | TUNAM | 345 | 一致 | 一致 | — |
| TU | 15 | TULOC | 345 | 一致 | `(LOC)` vs `C74456` (U5→S-CT) | — |
| TU | 16 | TULAT | 345 | 一致 | `(LAT)` vs `C99073` (U5→S-CT) | — |
| TU | 17 | TUDIR | 345 | 一致 | `(DIR)` vs `C99074` (U5→S-CT) | — |
| TU | 18 | TUPORTOT | 345 | 一致 | `(PORTOT)` vs `C99075` (U5→S-CT) | — |
| TU | 19 | TUMETHOD | 346 | 一致 | `(METHOD)` vs `C85492` (U5→S-CT) | — |
| TU | 20 | TULOBXFL | 346 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| TU | 21 | TUBLFL | 346 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| TU | 22 | TUEVAL | 346 | 一致 | `(EVAL)` vs `C78735` (U5→S-CT) | — |
| TU | 23 | TUEVALID | 346 | 一致 | `(MEDEVAL)` vs `C96777` (U5→S-CT) | — |
| TU | 24 | TUACPTFL | 346 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| TU | 25 | VISITNUM | 346 | 一致 | 一致 | — |
| TU | 26 | VISIT | 346 | 一致 | 一致 | — |
| TU | 27 | VISITDY | 346 | 一致 | 一致 | — |
| TU | 28 | TAETORD | 346 | 一致 | 一致 | — |
| TU | 29 | EPOCH | 346 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| TU | 30 | TUDTC | 346 | 一致 | 一致 | — |
| TU | 31 | TUDY | 346 | 一致 | 一致 | — |
| VS | 1 | STUDYID | 358 | 一致 | 一致 | — |
| VS | 2 | DOMAIN | 358 | 一致 | DOMAIN CT `VS` (U6→S-CT) | — |
| VS | 3 | USUBJID | 358 | 一致 | 一致 | — |
| VS | 4 | VSSEQ | 358 | 一致 | 一致 | — |
| VS | 5 | VSGRPID | 358 | 一致 | 一致 | — |
| VS | 6 | VSSPID | 358 | 一致 | 一致 | — |
| VS | 7 | VSTESTCD | 358 | 一致 | `(VSTESTCD)` vs `C66741` (U5→S-CT) | — |
| VS | 8 | VSTEST | 358 | 一致 | `(VSTEST)` vs `C67153` (U5→S-CT) | — |
| VS | 9 | VSCAT | 358 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| VS | 10 | VSSCAT | 359 | 一致 (speccmp2 丢 "or" = FP, layout p359:3 核) | `*` (改前空) | REPLACED CT 空→`*` |
| VS | 11 | VSPOS | 359 | 一致 | `(POSITION)` vs `C71148` (U5→S-CT) | — |
| VS | 12 | VSORRES | 359 | 一致 | 一致 | — |
| VS | 13 | VSORRESU | 359 | 一致 | `(VSRESU)` vs `C66770` (U5→S-CT) | — |
| VS | 14 | VSSTRESC | 359 | 一致 | 一致 | — |
| VS | 15 | VSSTRESN | 359 | 一致 | 一致 | — |
| VS | 16 | VSSTRESU | 359 | 一致 | `(VSRESU)` vs `C66770` (U5→S-CT) | — |
| VS | 17 | VSSTAT | 359 | 一致 | `(ND)` vs `C66789` (U5→S-CT) | — |
| VS | 18 | VSREASND | 359 | 一致 | 一致 | — |
| VS | 19 | VSLOC | 359 | 一致 | `(LOC)` vs `C74456` (U5→S-CT) | — |
| VS | 20 | VSLAT | 359 | 一致 | `(LAT)` vs `C99073` (U5→S-CT) | — |
| VS | 21 | VSLOBXFL | 359 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| VS | 22 | VSBLFL | 359 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| VS | 23 | VSDRVFL | 359 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| VS | 24 | VSTOX | 359 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| VS | 25 | VSTOXGR | 359 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| VS | 26 | VSCLSIG | 359 | 一致 | `(NY)` vs `C66742` (U5→S-CT) | — |
| VS | 27 | VISITNUM | 359 | 一致 | 一致 | — |
| VS | 28 | VISIT | 359 | 一致 | 一致 | — |
| VS | 29 | VISITDY | 359 | 一致 | 一致 | — |
| VS | 30 | TAETORD | 359 | 一致 | 一致 | — |
| VS | 31 | EPOCH | 359 | 一致 | `(EPOCH)` vs `C99079` (U5→S-CT) | — |
| VS | 32 | VSDTC | 359 | 一致 | 一致 | — |
| VS | 33 | VSDY | 359 | 一致 | 一致 | — |
| VS | 34 | VSTPT | 359 | 一致 | 一致 | — |
| VS | 35 | VSTPTNUM | 360 | 一致 | 一致 | — |
| VS | 36 | VSELTM | 360 | 一致 | 一致 | — |
| VS | 37 | VSTPTREF | 360 | 一致 | 一致 | — |
| VS | 38 | VSRFTDTC | 360 | 一致 | 一致 | — |
| TE | 1 | STUDYID | 403 | 一致 | 一致 | — |
| TE | 2 | DOMAIN | 403 | 一致 | DOMAIN CT `TE` (U6→S-CT) | — |
| TE | 3 | ETCD | 403 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| TE | 4 | ELEMENT | 403 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| TE | 5 | TESTRL | 403 | 一致 | 一致 | — |
| TE | 6 | TEENRL | 403 | 一致 | 一致 | — |
| TE | 7 | TEDUR | 403 | 一致 | 一致 | — |
| TI | 1 | STUDYID | 416 | 一致 | 一致 | — |
| TI | 2 | DOMAIN | 416 | 一致 | DOMAIN CT `TI` (U6→S-CT) | — |
| TI | 3 | IETESTCD | 416 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| TI | 4 | IETEST | 416 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| TI | 5 | IECAT | 416 | 一致 | `(IECAT)` vs `C66797` (U5→S-CT) | — |
| TI | 6 | IESCAT | 416 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| TI | 7 | TIRL | 416 | 一致 | 一致 | — |
| TI | 8 | TIVERS | 416 | 一致 | 一致 | — |
| TS | 1 | STUDYID | 417 | 一致 | 一致 | — |
| TS | 2 | DOMAIN | 417 | 一致 | DOMAIN CT `TS` (U6→S-CT) | — |
| TS | 3 | TSSEQ | 417 | 一致 | 一致 | — |
| TS | 4 | TSGRPID | 417 | 一致 | 一致 | — |
| TS | 5 | TSPARMCD | 417 | 一致 | `(TSPARMCD)` vs `C66738` (U5→S-CT) | — |
| TS | 6 | TSPARM | 417 | 一致 | `(TSPARM)` vs `C67152` (U5→S-CT) | — |
| TS | 7 | TSVAL | 417 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| TS | 8 | TSVALNF | 418 | 一致 | 一致 | — |
| TS | 9 | TSVALCD | 418 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| TS | 10 | TSVCDREF | 418 | 一致 | `(DICTNAM)` vs `C66788` (U5→S-CT) | — |
| TS | 11 | TSVCDVER | 418 | 一致 | 一致 | — |
| SUPPQUAL | 1 | STUDYID | 432 | 一致 | 一致 | — |
| SUPPQUAL | 2 | RDOMAIN | 432 | 一致 | `(DOMAIN)` vs `C66734` (U5→S-CT) | — |
| SUPPQUAL | 3 | USUBJID | 432 | 一致 | 一致 | — |
| SUPPQUAL | 4 | IDVAR | 432 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| SUPPQUAL | 5 | IDVARVAL | 432 | 一致 | 一致 | — |
| SUPPQUAL | 6 | QNAM | 432 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| SUPPQUAL | 7 | QLABEL | 432 | 一致 | 一致 | — |
| SUPPQUAL | 8 | QVAL | 432 | 一致 | 一致 | — |
| SUPPQUAL | 9 | QORIG | 432 | 一致 | 一致 | — |
| SUPPQUAL | 10 | QEVAL | 432 | 一致 | `(EVAL)` vs `C78735` (U5→S-CT) | — |
| TV | 1 | STUDYID | 407 | 一致 | 一致 | — |
| TV | 2 | DOMAIN | 407 | 一致 | DOMAIN CT `TV` (U6→S-CT) | — |
| TV | 3 | VISITNUM | 407 | 一致 | 一致 | — |
| TV | 4 | VISIT | 407 | 一致 | 一致 | — |
| TV | 5 | VISITDY | 407 | 一致 | 一致 | — |
| TV | 6 | ARMCD | 408 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| TV | 7 | ARM | 408 | 一致 | `*` (改前空) | REPLACED CT 空→`*` |
| TV | 8 | TVSTRL | 408 | 一致 | 一致 | — |
| TV | 9 | TVENRL | 408 | 一致 | 一致 | — |

### 逐页双向扫描日志
| 页 | 节 | PDF→KB: 变量/命中, 缺→已补 | KB→PDF: 对应 KB 段, 无出处→处理 | 表 | 备注 |
|---|---|---|---|---|---|
| 329 | §6.3.9.3 RS spec | 10 / 10 | STUDYID..RSTESTCD; 0 | bbox ×2 | DOMAIN U6; 节标题/首句在 assumptions (不碰) |
| 330 | RS spec | 15 / 15 (+RSTESTCD Notes 续行命中) | RSTEST..RSDRVFL; 0 | bbox ×2 + 裁图 | U5 |
| 331 | RS spec | 19 / 19 | RSEVAL..RSSTRTPT 段; 0 | bbox ×2 | U5 |
| 332 | RS spec 尾 | 2 / 2; 脚注 1→1 | RSENRTPT RSENTPT + 脚注; 0 | bbox ×2 | |
| 340 | §6.3.10 SC spec | 20 / 20; `*` 2→2 (SCCAT SCSCAT) | STUDYID..; 0 | bbox ×2 | U6 1 |
| 341 | SC spec 尾 | 4 / 4; 脚注 1→1 | 末 4 变量 + 脚注; 0 | bbox ×2 | |
| 345 | §6.3.12.1 TU spec | 18 / 18 | 前 18; 0 | bbox ×2 | U6 1 |
| 346 | TU spec 尾 | 13 / 13; 脚注 1→1 | TUMETHOD.. + 脚注; 0 | bbox ×2 | |
| 358 | §6.3.13 VS spec | 9 / 9; `*` 1→1 (VSCAT) | STUDYID..VSCAT 段; 0 | bbox ×2 | U6 1 |
| 359 | VS spec | 25 / 25; `*` 3→3 (VSSCAT VSTOX VSTOXGR) | VSSCAT..VSTPT 段; 0 | bbox ×2 + 裁图 | |
| 360 | VS spec 尾 | 4 / 4; 脚注 1→1 | VSTPTNUM.. + 脚注; 0 | bbox ×2 | |
| 403 | §7.2.2 TE spec | 7 / 7; `*` 2→2 (ETCD ELEMENT); 脚注 1→1 | 全 7 + 脚注; 0 | bbox ×2 | U6 1 |
| 407 | §7.3.1 TV spec | 5 / 5 | STUDYID..VISITDY; 0 | bbox (sc2w_s + speccmp2) | U6 1 |
| 408 | TV spec 尾 | 4 / 4; `*` 2→2 (ARMCD ARM); 脚注 1→1 | ARMCD..TVENRL + 脚注; 0 | 同上 | |
| 416 | §7.4.1 TI spec | 8 / 8; `*` 3→3 (IETESTCD IETEST IESCAT); 脚注 1→1 | 全 8 + 脚注; 0 | bbox ×2 | U6 1 |
| 417 | §7.4.2 TS spec | 7 / 7; `*` 1→1 (TSVAL) | STUDYID..TSVAL; 0 | bbox ×2 + 裁图 | U6 1 |
| 418 | TS spec 尾 | 4 / 4; `*` 1→1 (TSVALCD); 脚注 1→1 | TSVALCD.. + 脚注; 0 | bbox ×2 | |
| 432 | §8.4.1 SUPP-- spec | 10 / 10; `*` 2→2 (IDVAR QNAM); 脚注 1→1 | 全 10 + 脚注; 0 | bbox (sc2w_s + speccmp2) + 裁图 | RDOMAIN U5 |
注: 每页变量数 = vartable.md 第 4 列按页计数 (变量起始行所在页).

## 变更清单
| # | kb_file:line (改后) | ref | action | before → after | PDF 页 |
|---|---|---|---|---|---|
| 1 | RS/spec.md:420 | ig34_p0332_a003 | INSERTED | 脚注 `> ¹In this column, …` (`---` 后, Cross References 前; gap F) | 332 |
| 2 | SC/spec.md:81/90 | pdf:p340 CT 列 (SCCAT SCSCAT) | REPLACED | CT 空 → `*` ×2 | 340 |
| 3 | SC/spec.md:222 | ig34_p0341_a005 | INSERTED | 脚注 | 341 |
| 4 | TU/spec.md:285 | pdf:p346 脚注 | INSERTED | 脚注 | 346 |
| 5 | VS/spec.md:81/90/216/225 | pdf:p358-359 CT 列 (VSCAT VSSCAT VSTOX VSTOXGR) | REPLACED | 空 → `*` ×4 | 358-359 |
| 6 | VS/spec.md:348 | ig34_p0360_a005 | INSERTED | 脚注 | 360 |
| 7 | SUPPQUAL/spec.md:38/56 | pdf:p432 CT 列 (IDVAR QNAM) | REPLACED | 空 → `*` ×2 | 432 |
| 8 | SUPPQUAL/spec.md:98 | ig34_p0432_a026 | INSERTED | 脚注 | 432 |
| 9 | TE/spec.md:27/36 | pdf:p403 CT 列 (ETCD ELEMENT) | REPLACED | 空 → `*` ×2 | 403 |
| 10 | TE/spec.md:69 | ig34_p0403_a022 | INSERTED | 脚注 | 403 |
| 11 | TI/spec.md:27/36/54 | pdf:p416 CT 列 (IETESTCD IETEST IESCAT) | REPLACED | 空 → `*` ×3 | 416 |
| 12 | TI/spec.md:78 | ig34_p0416_a022 | INSERTED | 脚注 | 416 |
| 13 | TS/spec.md:63/81 | pdf:p417-418 CT 列 (TSVAL TSVALCD) | REPLACED | 空 → `*` ×2 | 417-418 |
| 14 | TS/spec.md:105 | ig34_p0418_a005 | INSERTED | 脚注 | 418 |
| 15 | TV/spec.md:54/63 | pdf:p408 CT 列 (ARMCD ARM) | REPLACED | 空 → `*` ×2 | 408 |
| 16 | TV/spec.md:87 | ig34_p0408_a006 | INSERTED | 脚注 | 408 |
- 合计 26 处 (CT `*` 17 + 脚注 9). 脚注 9 页文字相同 (bbox 核; TE/TI/TS/TV/SUPPQUAL 版面折行 "enclosed / in parentheses."), 上标 ¹ 照渲染; 字串与已提交 53 个 spec.md 脚注完全相同.

## 结构改动清单
无 (无变量增删/挪位; 无标题改动).

## 删除清单
无 (17 处 REPLACED 旧值均为空串).

## D6 标注清单
无新增. 9 文件 `> Class|Structure` 行 + Cross References 按 U8 为导航, 不标; SUPPQUAL `> Source text` 行为 D7 既定.

## PDF_TYPO 清单
无. (RSCAT "CHILD- PUGH" / RSSTRESN "-- STRESC" = PDF 折行, KB 正确不改.)

## 范围外发现
- 无 KB 内容错.
- 工具: sc2w.py 对 "Label 不在首行表头" 的页 (p407 p432) 判 no header 崩溃 (本 scratch `sc2w_s.py` 放宽判据); speccmp2.py 表头词过滤 (HV 含 Role/or/Format…) 会误删 Notes 中同形词 (RSEVAL/RSENRTPT/VSSCAT 三处假报) 及把表头残词当续行 (TV VISITDY). 未改共享工具.

## out_of_scope 处理 (O15 / O21 / O24 / O26)
- O15 / O26 (spec 表脚注): 本批 9 域全补 → 9 域关闭. spec 首句不属 spec-only 批.
- O24: 本批 9 域 CT `*` 全补 (17); C-code 记法 → U5 S-CT.
- O21 (FA/spec) 不在本批 units, 未处理.

## 需主控定
无.

## git diff --stat
 knowledge_base/domains/RS/spec.md       |  2 ++
 knowledge_base/domains/SC/spec.md       |  6 ++++--
 knowledge_base/domains/SUPPQUAL/spec.md |  6 ++++--
 knowledge_base/domains/TE/spec.md       |  6 ++++--
 knowledge_base/domains/TI/spec.md       |  8 +++++---
 knowledge_base/domains/TS/spec.md       |  6 ++++--
 knowledge_base/domains/TU/spec.md       |  2 ++
 knowledge_base/domains/TV/spec.md       |  6 ++++--
 knowledge_base/domains/VS/spec.md       | 10 ++++++----
 9 files changed, 35 insertions(+), 17 deletions(-)

## 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC4_writer
P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
for p in 329 330 331 332 340 341 345 346 358 359 360 403 407 408 416 417 418 432; do pdftotext -bbox -f $p -l $p "$P" $S/bb_$p.html; done
bash -c 'for a in "RS 329,330,331,332" "SC 340,341" "TU 345,346" "VS 358,359,360" "TE 403" "TI 416" "TS 417,418"; do set -- $a; python3 -I '$S'/sc2w.py '$S' $1 $2; python3 -I '$S'/speccmp2.py '$S' $1 $2; done'
python3 -I $S/sc2w_s.py $S SUPPQUAL 432; python3 -I $S/sc2w_s.py $S TV 407,408   # sc2w_s = sc2w + 表头判据 (x<100, 同行 "Type")
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```
