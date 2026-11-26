# T2S 扫描批 S-SPEC3 (spec-only: CV MI MK NV RE RP QS FT) — reviewer attempt 1

> 2026-11-26, oh-my-claudecode:code-reviewer (opus). Brief `subagent_prompts/t2s_scan_review_audit_v1.0.md` Reviewer 段 + `t2_reviewer_v1.0.md` / common brief / dispatch notes (含 T2S 段) / U1-U8 / R1-R4.
> 只读 KB; 未 stash/checkout/commit. scratch `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC3_reviewer/`.

## Verdict: **PASS**

## 方法 (独立于 writer 的 sc2w/speccmp2)
- 自写解析器 `rv_spec.py`: `pdftotext -bbox` 词框 → 按行 (y 容差 2pt) → 以页上**最后一个**含 Type/Role/Core 的表头行定 7 列 x 起点 (容差 4pt); 变量起始行 = 名称列词匹配 `^[A-Z][A-Z0-9]{1,7}$` 且 Type 列为 Char/Num; 名称列出现其他词 (脚注 "1 In this column" / 页脚 ©) 即止. 与 sc2w 无共享代码.
- 自写比对 `rv_cmp.py`: 解析 KB `### VAR` 块 (7 字段名及顺序、块外多余行), 空白归一后逐字段**全等**比较 Label/Type/CT/Role/Core/CDISC Notes; 计数闸 = PDF 变量名序列 == KB 序列, 且 Order = 1..N.
- 渲染复核 (pdftoppm 100dpi): CT 列裁图 p264 p287 p290 p295 p305 p308 p319 p324 (8 域首页/含 `*` 页); p286 整页 (两表头); p296 / p326 表尾 + 脚注.
- 复跑: `bash $S/run.sh && cd $S && python3 -I rv_cmp.py MI CV MK NV RP RE FT QS` (bb_N.html 生成命令同 writer 报告 "复跑命令" 首两行, 输出目录换成本 scratch).

## 页范围复核
- spec 表页: MI 264-265 / CV 286-288 / MK 290-291 / NV 294-296 / RP 305-306 / RE 308-310 / FT 319-320 / QS 324-326 (与 writer 一致). 解析器止点: 各域末页均止于 "1 In this column…" 脚注, 中间页止于 © 页脚.
- 表头位置: p286 两个表头 (y=89 §6.3.7.1 `--.xpt` 通用表; y=502 CV 表, 仅 STUDYID) → 取后者, 通用表 2 个 `*` (--TESTCD/--TEST) 不计本批 (渲染 p286 确认). p294 仅 1 个表头 (y=366, NV 表); 本批 20 页中除 p286 外无第二张 spec 表.

## 计数闸 (rv_cmp.py 输出)
| 域 | PDF 变量 | KB 变量 | 名称序列 | Order 1..N | 字段名 7 项且顺序一致 |
|---|---|---|---|---|---|
| MI | 37 | 37 | OK | True | 全部 |
| CV | 42 | 42 | OK | True | 全部 |
| MK | 42 | 42 | OK | True | 全部 |
| NV | 42 | 42 | OK | True | 全部 |
| RP | 36 | 36 | OK | True | 全部 |
| RE | 47 | 47 | OK | True | 全部 |
| FT | 38 | 38 | OK | True | 全部 |
| QS | 35 | 35 | OK | True | 全部 |
| 计 | 319 | 319 | | | |

## 逐字段结果汇总
- Label / Type / Role / Core / CDISC Notes: 319×5 = 1595 格, 1594 全等; 唯一不等 = QSEVLINT Notes: PDF 词流 `"- P2Y"` vs KB `"-P2Y"` → 渲染 p326 确认为负号在行尾折行 (`"-` / `P2Y"`), KB 正确, 非缺陷.
- KB 块外多余行: 仅 8 处新增脚注 (挂在各域最后一个变量块之后), 无其他.
- CT 列: 差异 115 处 = U5 107 (PDF 括号短名 vs KB C-code) + U6 8 (DOMAIN) → 归 S-CT, 本批不判. 其余 204 格全等 (含 13 个 `*`、NVDTC 等 "ISO 8601 …" 格式值).

## CT `*` 逐变量 (PDF 解析 + 渲染)
| 域 | PDF CT=`*` 变量 | KB `*` 数 | 渲染 |
|---|---|---|---|
| MI | MICAT MISCAT MIRESCAT | 3 | p264 一致 |
| CV | CVCAT CVSCAT CVSTRESC | 3 | p287 一致 |
| MK | MKCAT MKSCAT | 2 | p290 一致 |
| NV | (无) | 0 | p295 NVCAT/NVSCAT 空 |
| RP | (无) | 0 | p305 RPCAT/RPSCAT 空 |
| RE | (无) | 0 | p308 RECAT/RESCAT 空 |
| FT | FTTESTCD FTTEST | 2 | p319 一致 |
| QS | QSTESTCD QSTEST QSSCAT | 3 | p324 一致 |
- 全 20 页 bbox 独立词 `*` 计数: 264:3 287:3 290:2 319:2 324:3 286:2 (通用表) 其余 0 → 13 + 2 = 15, 与上表吻合, 无漏网.

## 脚注 (8 处; 逐字 + U7)
| 域 | PDF 页 | 逐字 (KB 行 == `> ¹` + PDF 词流) | 位置 (最后 Notes 行 / 脚注行 / Cross References 行) | atom 直查 (norm in spec.md) |
|---|---|---|---|---|
| MI | 265 | True | 336 / 339 / 341 | page_txt (无 atom) |
| CV | 288 | True | 381 / 384 / 386 | ig34_p0288_a018 True |
| MK | 291 | True | 381 / 384 / 386 | ig34_p0291_a025 True |
| NV | 296 | True | 381 / 384 / 386 | 无 atom; 出处 = p296 NV 表 (NVRFTDTC 行) 正下方, 渲染确认 |
| RP | 306 | True | 327 / 330 / 332 | ig34_p0306_a022 True |
| RE | 310 | True | 426 / 429 / 431 | ig34_p0310_a005 True |
| FT | 320 | True | 345 / 348 / 350 | ig34_p0320_a023 True |
| QS | 326 | True | 318 / 321 / 323 | ig34_p0326_a005 True |
- 每文件恰 1 处; 均在最后变量块 `---` 之后、`## Cross References` 之前 (U7). 上标 `¹` 与 CE/HO 先例同形. NV 脚注为 NV 表自身脚注 (与 NV/assumptions.md 中 §6.3.7.1 通用表脚注各属一表, 非重复).
- fp_match 对这些 NOTE 原子报 PARTIAL/hit_target null 是因 targets 只含 assumptions/examples (不含 spec.md); 直查 spec.md 全部命中.

## 授权范围 / 副作用
- `git diff HEAD -- knowledge_base/domains/{CV,MI,MK,NV,RE,RP,QS,FT}/spec.md`: 8 files, +29 / -13 = CT 空→`*` 13 处 (旧值均空串) + 脚注 8 行 (+ 8 空行). 无其他改动; 标题/锚点未动. 工作树中其他文件 (BE CM CO DM ML SM SU SV model/01/03/04) 属别批, 不计.
- G-TB6 反向溯源: 新增/改动 21 行全部有 PDF 出处 (上两表); 结构行签字: 无新增结构行 (8 个脚注前空行为 Markdown 分隔).
- 结构改动 / 删除 / D6 清单: writer 报 "无", 核实为无. PDF_TYPO: 无 (QSEVLINT 折行连字符不是 PDF_TYPO, 同意).

## census / fp_match / links
- census: batch `pdf_ranges` 为空 (spec 表非 Row 表) → 跳过, 以上独立解析 + 渲染替代. `census_items` 空.
- fp_match: `RESULT: RED`, regress 72 条, 全部在 `work/t2_fp_expected_regressions.jsonl` 中 (未登记 0) → 本批无新增回归.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (= 基线 42).

## 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无 | — |

## 逐变量结果 (rv_cmp.py; L/T/R/C/N = Label/Type/Role/Core/Notes, `=` 全等)
| 域 | # | 变量 | PDF 页 | L | T | R | C | N | CT |
|---|---|---|---|---|---|---|---|---|---|
| MI | 1 | STUDYID | 264 | = | = | = | = | = | = |
| MI | 2 | DOMAIN | 264 | = | = | = | = | = | U6→S-CT |
| MI | 3 | USUBJID | 264 | = | = | = | = | = | = |
| MI | 4 | MISEQ | 264 | = | = | = | = | = | = |
| MI | 5 | MIGRPID | 264 | = | = | = | = | = | = |
| MI | 6 | MIREFID | 264 | = | = | = | = | = | = |
| MI | 7 | MISPID | 264 | = | = | = | = | = | = |
| MI | 8 | MITESTCD | 264 | = | = | = | = | = | U5→S-CT |
| MI | 9 | MITEST | 264 | = | = | = | = | = | U5→S-CT |
| MI | 10 | MITSTDTL | 264 | = | = | = | = | = | U5→S-CT |
| MI | 11 | MICAT | 264 | = | = | = | = | = | = (`*`) |
| MI | 12 | MISCAT | 264 | = | = | = | = | = | = (`*`) |
| MI | 13 | MIORRES | 264 | = | = | = | = | = | = |
| MI | 14 | MIORRESU | 264 | = | = | = | = | = | U5→S-CT |
| MI | 15 | MISTRESC | 264 | = | = | = | = | = | = |
| MI | 16 | MISTRESN | 264 | = | = | = | = | = | = |
| MI | 17 | MISTRESU | 264 | = | = | = | = | = | U5→S-CT |
| MI | 18 | MIRESCAT | 264 | = | = | = | = | = | = (`*`) |
| MI | 19 | MISTAT | 264 | = | = | = | = | = | U5→S-CT |
| MI | 20 | MIREASND | 264 | = | = | = | = | = | = |
| MI | 21 | MINAM | 264 | = | = | = | = | = | = |
| MI | 22 | MISPEC | 265 | = | = | = | = | = | U5→S-CT |
| MI | 23 | MISPCCND | 265 | = | = | = | = | = | U5→S-CT |
| MI | 24 | MILOC | 265 | = | = | = | = | = | U5→S-CT |
| MI | 25 | MILAT | 265 | = | = | = | = | = | U5→S-CT |
| MI | 26 | MIDIR | 265 | = | = | = | = | = | U5→S-CT |
| MI | 27 | MIMETHOD | 265 | = | = | = | = | = | U5→S-CT |
| MI | 28 | MILOBXFL | 265 | = | = | = | = | = | U5→S-CT |
| MI | 29 | MIBLFL | 265 | = | = | = | = | = | U5→S-CT |
| MI | 30 | MIEVAL | 265 | = | = | = | = | = | U5→S-CT |
| MI | 31 | VISITNUM | 265 | = | = | = | = | = | = |
| MI | 32 | VISIT | 265 | = | = | = | = | = | = |
| MI | 33 | VISITDY | 265 | = | = | = | = | = | = |
| MI | 34 | TAETORD | 265 | = | = | = | = | = | = |
| MI | 35 | EPOCH | 265 | = | = | = | = | = | U5→S-CT |
| MI | 36 | MIDTC | 265 | = | = | = | = | = | = |
| MI | 37 | MIDY | 265 | = | = | = | = | = | = |
| CV | 1 | STUDYID | 286 | = | = | = | = | = | = |
| CV | 2 | DOMAIN | 287 | = | = | = | = | = | U6→S-CT |
| CV | 3 | USUBJID | 287 | = | = | = | = | = | = |
| CV | 4 | CVSEQ | 287 | = | = | = | = | = | = |
| CV | 5 | CVGRPID | 287 | = | = | = | = | = | = |
| CV | 6 | CVREFID | 287 | = | = | = | = | = | = |
| CV | 7 | CVSPID | 287 | = | = | = | = | = | = |
| CV | 8 | CVLNKID | 287 | = | = | = | = | = | = |
| CV | 9 | CVLNKGRP | 287 | = | = | = | = | = | = |
| CV | 10 | CVTESTCD | 287 | = | = | = | = | = | U5→S-CT |
| CV | 11 | CVTEST | 287 | = | = | = | = | = | U5→S-CT |
| CV | 12 | CVCAT | 287 | = | = | = | = | = | = (`*`) |
| CV | 13 | CVSCAT | 287 | = | = | = | = | = | = (`*`) |
| CV | 14 | CVPOS | 287 | = | = | = | = | = | U5→S-CT |
| CV | 15 | CVORRES | 287 | = | = | = | = | = | = |
| CV | 16 | CVORRESU | 287 | = | = | = | = | = | U5→S-CT |
| CV | 17 | CVSTRESC | 287 | = | = | = | = | = | = (`*`) |
| CV | 18 | CVSTRESN | 287 | = | = | = | = | = | = |
| CV | 19 | CVSTRESU | 287 | = | = | = | = | = | U5→S-CT |
| CV | 20 | CVSTAT | 287 | = | = | = | = | = | U5→S-CT |
| CV | 21 | CVREASND | 287 | = | = | = | = | = | = |
| CV | 22 | CVLOC | 287 | = | = | = | = | = | U5→S-CT |
| CV | 23 | CVLAT | 287 | = | = | = | = | = | U5→S-CT |
| CV | 24 | CVDIR | 287 | = | = | = | = | = | U5→S-CT |
| CV | 25 | CVMETHOD | 287 | = | = | = | = | = | U5→S-CT |
| CV | 26 | CVLOBXFL | 288 | = | = | = | = | = | U5→S-CT |
| CV | 27 | CVBLFL | 288 | = | = | = | = | = | U5→S-CT |
| CV | 28 | CVDRVFL | 288 | = | = | = | = | = | U5→S-CT |
| CV | 29 | CVEVAL | 288 | = | = | = | = | = | U5→S-CT |
| CV | 30 | CVEVALID | 288 | = | = | = | = | = | U5→S-CT |
| CV | 31 | VISITNUM | 288 | = | = | = | = | = | = |
| CV | 32 | VISIT | 288 | = | = | = | = | = | = |
| CV | 33 | VISITDY | 288 | = | = | = | = | = | = |
| CV | 34 | TAETORD | 288 | = | = | = | = | = | = |
| CV | 35 | EPOCH | 288 | = | = | = | = | = | U5→S-CT |
| CV | 36 | CVDTC | 288 | = | = | = | = | = | = |
| CV | 37 | CVDY | 288 | = | = | = | = | = | = |
| CV | 38 | CVTPT | 288 | = | = | = | = | = | = |
| CV | 39 | CVTPTNUM | 288 | = | = | = | = | = | = |
| CV | 40 | CVELTM | 288 | = | = | = | = | = | = |
| CV | 41 | CVTPTREF | 288 | = | = | = | = | = | = |
| CV | 42 | CVRFTDTC | 288 | = | = | = | = | = | = |
| MK | 1 | STUDYID | 290 | = | = | = | = | = | = |
| MK | 2 | DOMAIN | 290 | = | = | = | = | = | U6→S-CT |
| MK | 3 | USUBJID | 290 | = | = | = | = | = | = |
| MK | 4 | MKSEQ | 290 | = | = | = | = | = | = |
| MK | 5 | MKGRPID | 290 | = | = | = | = | = | = |
| MK | 6 | MKREFID | 290 | = | = | = | = | = | = |
| MK | 7 | MKSPID | 290 | = | = | = | = | = | = |
| MK | 8 | MKLNKID | 290 | = | = | = | = | = | = |
| MK | 9 | MKLNKGRP | 290 | = | = | = | = | = | = |
| MK | 10 | MKTESTCD | 290 | = | = | = | = | = | U5→S-CT |
| MK | 11 | MKTEST | 290 | = | = | = | = | = | U5→S-CT |
| MK | 12 | MKCAT | 290 | = | = | = | = | = | = (`*`) |
| MK | 13 | MKSCAT | 290 | = | = | = | = | = | = (`*`) |
| MK | 14 | MKPOS | 290 | = | = | = | = | = | U5→S-CT |
| MK | 15 | MKORRES | 290 | = | = | = | = | = | = |
| MK | 16 | MKORRESU | 290 | = | = | = | = | = | U5→S-CT |
| MK | 17 | MKSTRESC | 290 | = | = | = | = | = | = |
| MK | 18 | MKSTRESN | 290 | = | = | = | = | = | = |
| MK | 19 | MKSTRESU | 291 | = | = | = | = | = | U5→S-CT |
| MK | 20 | MKSTAT | 291 | = | = | = | = | = | U5→S-CT |
| MK | 21 | MKREASND | 291 | = | = | = | = | = | = |
| MK | 22 | MKLOC | 291 | = | = | = | = | = | U5→S-CT |
| MK | 23 | MKLAT | 291 | = | = | = | = | = | U5→S-CT |
| MK | 24 | MKDIR | 291 | = | = | = | = | = | U5→S-CT |
| MK | 25 | MKMETHOD | 291 | = | = | = | = | = | U5→S-CT |
| MK | 26 | MKLOBXFL | 291 | = | = | = | = | = | U5→S-CT |
| MK | 27 | MKBLFL | 291 | = | = | = | = | = | U5→S-CT |
| MK | 28 | MKDRVFL | 291 | = | = | = | = | = | U5→S-CT |
| MK | 29 | MKEVAL | 291 | = | = | = | = | = | U5→S-CT |
| MK | 30 | MKEVALID | 291 | = | = | = | = | = | U5→S-CT |
| MK | 31 | VISITNUM | 291 | = | = | = | = | = | = |
| MK | 32 | VISIT | 291 | = | = | = | = | = | = |
| MK | 33 | VISITDY | 291 | = | = | = | = | = | = |
| MK | 34 | TAETORD | 291 | = | = | = | = | = | = |
| MK | 35 | EPOCH | 291 | = | = | = | = | = | U5→S-CT |
| MK | 36 | MKDTC | 291 | = | = | = | = | = | = |
| MK | 37 | MKDY | 291 | = | = | = | = | = | = |
| MK | 38 | MKTPT | 291 | = | = | = | = | = | = |
| MK | 39 | MKTPTNUM | 291 | = | = | = | = | = | = |
| MK | 40 | MKELTM | 291 | = | = | = | = | = | = |
| MK | 41 | MKTPTREF | 291 | = | = | = | = | = | = |
| MK | 42 | MKRFTDTC | 291 | = | = | = | = | = | = |
| NV | 1 | STUDYID | 294 | = | = | = | = | = | = |
| NV | 2 | DOMAIN | 294 | = | = | = | = | = | U6→S-CT |
| NV | 3 | USUBJID | 294 | = | = | = | = | = | = |
| NV | 4 | FOCID | 294 | = | = | = | = | = | = |
| NV | 5 | NVSEQ | 294 | = | = | = | = | = | = |
| NV | 6 | NVGRPID | 294 | = | = | = | = | = | = |
| NV | 7 | NVREFID | 294 | = | = | = | = | = | = |
| NV | 8 | NVSPID | 294 | = | = | = | = | = | = |
| NV | 9 | NVLNKID | 294 | = | = | = | = | = | = |
| NV | 10 | NVLNKGRP | 294 | = | = | = | = | = | = |
| NV | 11 | NVTESTCD | 294 | = | = | = | = | = | U5→S-CT |
| NV | 12 | NVTEST | 295 | = | = | = | = | = | U5→S-CT |
| NV | 13 | NVCAT | 295 | = | = | = | = | = | = |
| NV | 14 | NVSCAT | 295 | = | = | = | = | = | = |
| NV | 15 | NVORRES | 295 | = | = | = | = | = | = |
| NV | 16 | NVORRESU | 295 | = | = | = | = | = | U5→S-CT |
| NV | 17 | NVSTRESC | 295 | = | = | = | = | = | = |
| NV | 18 | NVSTRESN | 295 | = | = | = | = | = | = |
| NV | 19 | NVSTRESU | 295 | = | = | = | = | = | U5→S-CT |
| NV | 20 | NVSTAT | 295 | = | = | = | = | = | U5→S-CT |
| NV | 21 | NVREASND | 295 | = | = | = | = | = | = |
| NV | 22 | NVLOC | 295 | = | = | = | = | = | U5→S-CT |
| NV | 23 | NVLAT | 295 | = | = | = | = | = | U5→S-CT |
| NV | 24 | NVDIR | 295 | = | = | = | = | = | U5→S-CT |
| NV | 25 | NVMETHOD | 295 | = | = | = | = | = | U5→S-CT |
| NV | 26 | NVLOBXFL | 295 | = | = | = | = | = | U5→S-CT |
| NV | 27 | NVBLFL | 295 | = | = | = | = | = | U5→S-CT |
| NV | 28 | NVDRVFL | 295 | = | = | = | = | = | U5→S-CT |
| NV | 29 | NVEVAL | 295 | = | = | = | = | = | U5→S-CT |
| NV | 30 | NVEVALID | 295 | = | = | = | = | = | U5→S-CT |
| NV | 31 | VISITNUM | 295 | = | = | = | = | = | = |
| NV | 32 | VISIT | 295 | = | = | = | = | = | = |
| NV | 33 | VISITDY | 295 | = | = | = | = | = | = |
| NV | 34 | TAETORD | 295 | = | = | = | = | = | = |
| NV | 35 | EPOCH | 295 | = | = | = | = | = | U5→S-CT |
| NV | 36 | NVDTC | 295 | = | = | = | = | = | = |
| NV | 37 | NVDY | 295 | = | = | = | = | = | = |
| NV | 38 | NVTPT | 295 | = | = | = | = | = | = |
| NV | 39 | NVTPTNUM | 296 | = | = | = | = | = | = |
| NV | 40 | NVELTM | 296 | = | = | = | = | = | = |
| NV | 41 | NVTPTREF | 296 | = | = | = | = | = | = |
| NV | 42 | NVRFTDTC | 296 | = | = | = | = | = | = |
| RP | 1 | STUDYID | 305 | = | = | = | = | = | = |
| RP | 2 | DOMAIN | 305 | = | = | = | = | = | U6→S-CT |
| RP | 3 | USUBJID | 305 | = | = | = | = | = | = |
| RP | 4 | RPSEQ | 305 | = | = | = | = | = | = |
| RP | 5 | RPGRPID | 305 | = | = | = | = | = | = |
| RP | 6 | RPREFID | 305 | = | = | = | = | = | = |
| RP | 7 | RPSPID | 305 | = | = | = | = | = | = |
| RP | 8 | RPLNKID | 305 | = | = | = | = | = | = |
| RP | 9 | RPLNKGRP | 305 | = | = | = | = | = | = |
| RP | 10 | RPTESTCD | 305 | = | = | = | = | = | U5→S-CT |
| RP | 11 | RPTEST | 305 | = | = | = | = | = | U5→S-CT |
| RP | 12 | RPCAT | 305 | = | = | = | = | = | = |
| RP | 13 | RPSCAT | 305 | = | = | = | = | = | = |
| RP | 14 | RPORRES | 305 | = | = | = | = | = | = |
| RP | 15 | RPORRESU | 305 | = | = | = | = | = | U5→S-CT |
| RP | 16 | RPSTRESC | 306 | = | = | = | = | = | = |
| RP | 17 | RPSTRESN | 306 | = | = | = | = | = | = |
| RP | 18 | RPSTRESU | 306 | = | = | = | = | = | U5→S-CT |
| RP | 19 | RPSTAT | 306 | = | = | = | = | = | U5→S-CT |
| RP | 20 | RPREASND | 306 | = | = | = | = | = | = |
| RP | 21 | RPLOBXFL | 306 | = | = | = | = | = | U5→S-CT |
| RP | 22 | RPBLFL | 306 | = | = | = | = | = | U5→S-CT |
| RP | 23 | RPDRVFL | 306 | = | = | = | = | = | U5→S-CT |
| RP | 24 | VISITNUM | 306 | = | = | = | = | = | = |
| RP | 25 | VISIT | 306 | = | = | = | = | = | = |
| RP | 26 | VISITDY | 306 | = | = | = | = | = | = |
| RP | 27 | TAETORD | 306 | = | = | = | = | = | = |
| RP | 28 | EPOCH | 306 | = | = | = | = | = | U5→S-CT |
| RP | 29 | RPDTC | 306 | = | = | = | = | = | = |
| RP | 30 | RPDY | 306 | = | = | = | = | = | = |
| RP | 31 | RPDUR | 306 | = | = | = | = | = | = |
| RP | 32 | RPTPT | 306 | = | = | = | = | = | = |
| RP | 33 | RPTPTNUM | 306 | = | = | = | = | = | = |
| RP | 34 | RPELTM | 306 | = | = | = | = | = | = |
| RP | 35 | RPTPTREF | 306 | = | = | = | = | = | = |
| RP | 36 | RPRFTDTC | 306 | = | = | = | = | = | = |
| RE | 1 | STUDYID | 308 | = | = | = | = | = | = |
| RE | 2 | DOMAIN | 308 | = | = | = | = | = | U6→S-CT |
| RE | 3 | USUBJID | 308 | = | = | = | = | = | = |
| RE | 4 | SPDEVID | 308 | = | = | = | = | = | = |
| RE | 5 | RESEQ | 308 | = | = | = | = | = | = |
| RE | 6 | REGRPID | 308 | = | = | = | = | = | = |
| RE | 7 | REREFID | 308 | = | = | = | = | = | = |
| RE | 8 | RESPID | 308 | = | = | = | = | = | = |
| RE | 9 | RELNKID | 308 | = | = | = | = | = | = |
| RE | 10 | RELNKGRP | 308 | = | = | = | = | = | = |
| RE | 11 | RETESTCD | 308 | = | = | = | = | = | U5→S-CT |
| RE | 12 | RETEST | 308 | = | = | = | = | = | U5→S-CT |
| RE | 13 | RECAT | 308 | = | = | = | = | = | = |
| RE | 14 | RESCAT | 308 | = | = | = | = | = | = |
| RE | 15 | REPOS | 308 | = | = | = | = | = | U5→S-CT |
| RE | 16 | REORRES | 308 | = | = | = | = | = | = |
| RE | 17 | REORRESU | 308 | = | = | = | = | = | U5→S-CT |
| RE | 18 | REORREF | 308 | = | = | = | = | = | = |
| RE | 19 | RESTRESC | 308 | = | = | = | = | = | = |
| RE | 20 | RESTRESN | 308 | = | = | = | = | = | = |
| RE | 21 | RESTRESU | 309 | = | = | = | = | = | U5→S-CT |
| RE | 22 | RESTREFC | 309 | = | = | = | = | = | = |
| RE | 23 | RESTREFN | 309 | = | = | = | = | = | = |
| RE | 24 | RESTAT | 309 | = | = | = | = | = | U5→S-CT |
| RE | 25 | REREASND | 309 | = | = | = | = | = | = |
| RE | 26 | RELOC | 309 | = | = | = | = | = | U5→S-CT |
| RE | 27 | RELAT | 309 | = | = | = | = | = | U5→S-CT |
| RE | 28 | REDIR | 309 | = | = | = | = | = | U5→S-CT |
| RE | 29 | REMETHOD | 309 | = | = | = | = | = | U5→S-CT |
| RE | 30 | RELOBXFL | 309 | = | = | = | = | = | U5→S-CT |
| RE | 31 | REBLFL | 309 | = | = | = | = | = | U5→S-CT |
| RE | 32 | REDRVFL | 309 | = | = | = | = | = | U5→S-CT |
| RE | 33 | REEVAL | 309 | = | = | = | = | = | U5→S-CT |
| RE | 34 | REEVALID | 309 | = | = | = | = | = | U5→S-CT |
| RE | 35 | REREPNUM | 309 | = | = | = | = | = | = |
| RE | 36 | VISITNUM | 309 | = | = | = | = | = | = |
| RE | 37 | VISIT | 309 | = | = | = | = | = | = |
| RE | 38 | VISITDY | 309 | = | = | = | = | = | = |
| RE | 39 | TAETORD | 309 | = | = | = | = | = | = |
| RE | 40 | EPOCH | 309 | = | = | = | = | = | U5→S-CT |
| RE | 41 | REDTC | 309 | = | = | = | = | = | = |
| RE | 42 | REDY | 309 | = | = | = | = | = | = |
| RE | 43 | RETPT | 309 | = | = | = | = | = | = |
| RE | 44 | RETPTNUM | 310 | = | = | = | = | = | = |
| RE | 45 | REELTM | 310 | = | = | = | = | = | = |
| RE | 46 | RETPTREF | 310 | = | = | = | = | = | = |
| RE | 47 | RERFTDTC | 310 | = | = | = | = | = | = |
| FT | 1 | STUDYID | 319 | = | = | = | = | = | = |
| FT | 2 | DOMAIN | 319 | = | = | = | = | = | U6→S-CT |
| FT | 3 | USUBJID | 319 | = | = | = | = | = | = |
| FT | 4 | FTSEQ | 319 | = | = | = | = | = | = |
| FT | 5 | FTGRPID | 319 | = | = | = | = | = | = |
| FT | 6 | FTREFID | 319 | = | = | = | = | = | = |
| FT | 7 | FTSPID | 319 | = | = | = | = | = | = |
| FT | 8 | FTTESTCD | 319 | = | = | = | = | = | = (`*`) |
| FT | 9 | FTTEST | 319 | = | = | = | = | = | = (`*`) |
| FT | 10 | FTCAT | 319 | = | = | = | = | = | U5→S-CT |
| FT | 11 | FTSCAT | 319 | = | = | = | = | = | = |
| FT | 12 | FTPOS | 319 | = | = | = | = | = | U5→S-CT |
| FT | 13 | FTORRES | 319 | = | = | = | = | = | = |
| FT | 14 | FTORRESU | 319 | = | = | = | = | = | U5→S-CT |
| FT | 15 | FTSTRESC | 319 | = | = | = | = | = | = |
| FT | 16 | FTSTRESN | 319 | = | = | = | = | = | = |
| FT | 17 | FTSTRESU | 320 | = | = | = | = | = | U5→S-CT |
| FT | 18 | FTSTAT | 320 | = | = | = | = | = | U5→S-CT |
| FT | 19 | FTREASND | 320 | = | = | = | = | = | = |
| FT | 20 | FTXFN | 320 | = | = | = | = | = | = |
| FT | 21 | FTNAM | 320 | = | = | = | = | = | = |
| FT | 22 | FTMETHOD | 320 | = | = | = | = | = | U5→S-CT |
| FT | 23 | FTLOBXFL | 320 | = | = | = | = | = | U5→S-CT |
| FT | 24 | FTBLFL | 320 | = | = | = | = | = | U5→S-CT |
| FT | 25 | FTDRVFL | 320 | = | = | = | = | = | U5→S-CT |
| FT | 26 | FTREPNUM | 320 | = | = | = | = | = | = |
| FT | 27 | VISITNUM | 320 | = | = | = | = | = | = |
| FT | 28 | VISIT | 320 | = | = | = | = | = | = |
| FT | 29 | VISITDY | 320 | = | = | = | = | = | = |
| FT | 30 | TAETORD | 320 | = | = | = | = | = | = |
| FT | 31 | EPOCH | 320 | = | = | = | = | = | U5→S-CT |
| FT | 32 | FTDTC | 320 | = | = | = | = | = | = |
| FT | 33 | FTDY | 320 | = | = | = | = | = | = |
| FT | 34 | FTTPT | 320 | = | = | = | = | = | = |
| FT | 35 | FTTPTNUM | 320 | = | = | = | = | = | = |
| FT | 36 | FTELTM | 320 | = | = | = | = | = | = |
| FT | 37 | FTTPTREF | 320 | = | = | = | = | = | = |
| FT | 38 | FTRFTDTC | 320 | = | = | = | = | = | = |
| QS | 1 | STUDYID | 324 | = | = | = | = | = | = |
| QS | 2 | DOMAIN | 324 | = | = | = | = | = | U6→S-CT |
| QS | 3 | USUBJID | 324 | = | = | = | = | = | = |
| QS | 4 | QSSEQ | 324 | = | = | = | = | = | = |
| QS | 5 | QSGRPID | 324 | = | = | = | = | = | = |
| QS | 6 | QSSPID | 324 | = | = | = | = | = | = |
| QS | 7 | QSTESTCD | 324 | = | = | = | = | = | = (`*`) |
| QS | 8 | QSTEST | 324 | = | = | = | = | = | = (`*`) |
| QS | 9 | QSCAT | 324 | = | = | = | = | = | U5→S-CT |
| QS | 10 | QSSCAT | 324 | = | = | = | = | = | = (`*`) |
| QS | 11 | QSORRES | 324 | = | = | = | = | = | = |
| QS | 12 | QSORRESU | 325 | = | = | = | = | = | U5→S-CT |
| QS | 13 | QSSTRESC | 325 | = | = | = | = | = | = |
| QS | 14 | QSSTRESN | 325 | = | = | = | = | = | = |
| QS | 15 | QSSTRESU | 325 | = | = | = | = | = | U5→S-CT |
| QS | 16 | QSSTAT | 325 | = | = | = | = | = | U5→S-CT |
| QS | 17 | QSREASND | 325 | = | = | = | = | = | = |
| QS | 18 | QSMETHOD | 325 | = | = | = | = | = | U5→S-CT |
| QS | 19 | QSLOBXFL | 325 | = | = | = | = | = | U5→S-CT |
| QS | 20 | QSBLFL | 325 | = | = | = | = | = | U5→S-CT |
| QS | 21 | QSDRVFL | 325 | = | = | = | = | = | U5→S-CT |
| QS | 22 | VISITNUM | 325 | = | = | = | = | = | = |
| QS | 23 | VISIT | 325 | = | = | = | = | = | = |
| QS | 24 | VISITDY | 325 | = | = | = | = | = | = |
| QS | 25 | TAETORD | 325 | = | = | = | = | = | = |
| QS | 26 | EPOCH | 325 | = | = | = | = | = | U5→S-CT |
| QS | 27 | QSDTC | 325 | = | = | = | = | = | = |
| QS | 28 | QSDY | 325 | = | = | = | = | = | = |
| QS | 29 | QSTPT | 325 | = | = | = | = | = | = |
| QS | 30 | QSTPTNUM | 325 | = | = | = | = | = | = |
| QS | 31 | QSELTM | 325 | = | = | = | = | = | = |
| QS | 32 | QSTPTREF | 326 | = | = | = | = | = | = |
| QS | 33 | QSRFTDTC | 326 | = | = | = | = | = | = |
| QS | 34 | QSEVLINT | 326 | = | = | = | = | 折行负号, KB 正确 | = |
| QS | 35 | QSEVINTX | 326 | = | = | = | = | = | = |
