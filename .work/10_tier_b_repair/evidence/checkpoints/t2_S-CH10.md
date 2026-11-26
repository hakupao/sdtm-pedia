# T2S S-CH10 writer checkpoint (扫描批: chapters/ch10_appendices.md, §10 Appendices)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `a54d6df`; ch10 改前与 HEAD 一致 (md5 `0a452256ab1e21168a96d53a2ccd31c8`, 329 行). scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CH10_writer/`
  (base.md = `git show HEAD:` 副本; apply.py 精确替换 + 命中次数断言; e1-e5.py 分段改动脚本; appA.md 手工录入后与 layout 首 token 逐行 diff (0) + 渲染逐行核; appD_table.md 由 layout 文本脚本生成; r-444..r-461.png 110dpi 渲染, 18 页全部看过; chk.py = KB→PDF 子串核; residue.py = PDF→KB 残余核)
- 进度日志 (分段写入, 防中断): [段 1] App A-D 已改 + 本段日志; [段 2] App E/F 见下文后续段.

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| chapters/ch10 | §10 Appendices | 444-461 | **444-461** | p443 = OI Ex1 表尾 (Row 6-14, §9.2 别节); p444 首行 `10 Appendices` + Appendix A 标题; p461 = Appendix F (全书末页, p462 不存在) |

### 段 1 日志 (p444-451)
- App A (p444-445): Name/Company 表整表缺 (KB 仅有自写摘要 "contributor table lists approximately 70 individuals…"). → 按 PDF 补整表 74 行 (p444 35 + p445 39; 首 token 与 layout 逐行 diff 0; 渲染核 2 个多行单元格 Christine Connolly / Mike Hamidi, Anita Umesh Company 空格照录); KB 摘要段 = 自写占位 → D2 删.
- App B (p446-447): 40 行脚本逐格 = layout 拼接 (修后 diff 0); 修 5 格 (Define-XML / ISO 8601 / ISO 3166 / SDS 句末句点, SDTMIG "[this document]"); PDF 无表头行 → KB 自拟表头 "Abbreviation | Full Term" 改为空表头 `| | |` (S-INT EX Ex2 先例).
- §9 引言 (KB HEAD:64-69): PDF p441 = §9 自身内容, 非 §10; 已在 DI/assumptions.md 顶 `## §9 Study References` (U3, S-SPREL 放, 逐字已核) → D2: 正文替换为一行交叉引用; 标题 `## Section 9: Study References (p441)` 规则 6 保留.
- App C (p448): 补 PDF 第 2/3 段 (New/modified terms…; Visit the CDISC…); `### Key Points` 5 条 = 本节 PDF 5 段的改写/复述 → R2 插入后 D2 删 (含标题; 全仓无入站锚点链接); C1 引言句改为 PDF 原句; C1 表 `--REAS` 格改为 PDF 原文.
- App D (p449-451): 首段 KB 截断 + 重排 + 自添子句 → 整段换 PDF 原文 (2 段); `### Rules for Using Fragments` 3 条 = 改写 → D2 删 (含标题); 片段表 KB 4 列拼排 (末尾错序, HEAD:166 行 4 格畸形) → 按 PDF 单表 2 列 106 行重建 (KB 原 106 对与 PDF 集合差 0/0).

### 段 2 日志 (p452-460, App E)
- App E 整段按 PDF 重写 (旧 KB 为压缩改写): 叙述 2 条 bullet 原已逐字; 补 "The following changes have been made throughout:" + 11 条 bullet 逐字替换改写版 (`### General Changes Throughout` KB 标题规则 6 保留).
- MO 框: KB `### Decommissioning of MO (Morphology)` → PDF 原标题 `### A note on the decommissioning of MO` (S-TDM 口径: 全 KB 无入站锚点); 块按 PDF 顺序移到 New Domains 之前 (同文件 RELOCATE). 正文 3 段与 p452 逐字一致 (未改字).
- New Domains 表: KB 列序/表头错 (`Domain | Description`, 代码在前) → 按 PDF `Domain | Domain Abbreviation` 重建 5 行.
- 变更表 p453-460: 整表按 PDF 逐行重建 (主表 + §9 子表 + Appendices 子表, 后两张 PDF 表头为 "Change"); 单元格多 bullet 用 `• …<br>• …` (ch08 先例), 6.4.4 子项 PDF 字形 `o` → 按 ch08 先例写 `◦`; 3.2 单元格无 bullet 的引文段照录; 2.1 / Appendix A 无 bullet 照录.
- 校验 (chk.py, `pdftotext -raw` p452-460 归一后子串): KB 段 338 单元 → 未命中 7 = KB 标题 2 + T-1 / T-2 改正 2 + 跨页单元格 3 (4.2 / 5.2 / 6.4.4, raw 文本被页眉 "Section Number…" 插断, 逐段核一致). 反向: PDF `•` 171 − p459 空 bullet 行 10 = 161 = KB 单元格 `•` 147 + 列表 `-` 14; `o` 子项 2 = KB `◦` 2.

### 段 3 日志 (p461, App F)
- 4 处 VALUE_DIFF 按 PDF 改: "patents for which" → "patent claims for which"; (c) 句 "the CDISC Intellectual Property Policy ("the Policy")" → "this Policy"; (ii) 句补 "(“the Policy”)" (KB 把定义挪了位置); Liability "WHETHER ARISING UNDER" → "WHETHER UNDER" (KB 多 ARISING). `### No Other Warranties/Disclaimers` = PDF 行内粗体引导语, KB 标题规则 6 保留. chk.py 11 单元 0 未命中.

### 双向全扫 — 逐页日志 (改后; 方法: PDF→KB = layout / raw 文本逐句逐行 + 渲染 110dpi; KB→PDF = chk.py 把 KB 每段 / 每格 / 每个 `<br>` 单元归一后在 `pdftotext -raw` 页文本中子串查)
| 页 | 节 | PDF→KB: 句/列表/表行 数, 命中, 缺→已补 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 |
|---|---|---|---|---|---|
| 444 | §10 / App A | 句 2 + 表行 35 / 2 / 35→35 (整表缺) | KB:9 一致; HEAD:11 自写摘要段 → D2 删 | Name/Company 35 行逐格 (渲染) | `10 Appendices` 章标题 = KB H1 等价; 2 个多行格合并 |
| 445 | App A | 表行 39 / 0 / 39→39 | — | 39 行逐格 (渲染) | 续表重复表头不另起; Anita Umesh Company 空; "Ben Qgunsulire" / "Gbenga Ogunsulire" 照录 |
| 446 | App B | 句 2 + 表行 32 / 34 / 5 格→已修 | 无出处 0; KB 自拟表头 → 空表头 | glossary 32 行逐格 (脚本+渲染) | 修: Define-XML / ISO 8601 / ISO 3166 / SDS 句点, SDTMIG "[this document]" |
| 447 | App B | 表行 8 / 8 / 0 | 一致 | 8 行逐格 | |
| 448 | App C / C1 | 句 9 + 表行 3 (+表头) / 6 / 2 段→已补, C1 引言 1 改, --REAS 1 格改 | `### Key Points` 5 条 = 改写 → D2 删 | C1 3 行×3 列逐格 (渲染) | |
| 449 | App D | 句 6 + 表行 33 (+表头) / 2 / 首段 4 句缺/改写→整段换 | `### Rules for Using Fragments` 3 条 + 自添子句 → D2 删 | 片段表重建 (2 列) | |
| 450 | App D | 表行 47 / 47 (集合) / 0 | — | 重建后逐行 = layout | KB 原 4 列拼排顺序错 (NORMAL RANGE / MIE / NST 位置) |
| 451 | App D | 表行 26 / 26 / 0 | — | 逐行 = layout | 106 = 33+47+26 |
| 452 | App E 叙述 / MO 框 | 句 4 + bullet 13 + MO 框 4 / 4+2+4 / 11 bullet 改写→逐字换, 引导句 1 补 | 旧改写 bullet 11 → 被替换 | — | MO 标题换 PDF 原文; MO 块移到 New Domains 前 |
| 453 | New Domains / 变更表 1.3-4.2 | 表 5 行 + 句 1 + 变更表数据行 10 + 组行 4 / 句 1 / 5 行列序错→重建, 10 行 Change 格按 PDF 重写 | 旧改写格全部替换 | New Domains 5×2 逐格; 变更表逐 bullet (chk) | 2.7 / 3.2 名称折行混入 Change 列 (layout) 已按渲染分列 |
| 454 | 4.2 续 - 5.2 | 数据行 6 + 组行 1 + 4.2 续 / 6 行重写 | 同上 | 逐 bullet | 4.1 行 PDF 重复出现 (照录, 见 PDF_TYPO T-4); –DRVFL (T-1) |
| 455 | 5.2 续 - 6.2.4 | 数据行 12 + 组行 1 + 5.2 续 / 12 行重写 | 同上 | 逐 bullet | "Clinical Events" PDF 无 "(CE)" (KB 原有 → 照 PDF) |
| 456 | 6.2.4 续 - 6.3.5.5 | 数据行 13 + 6.2.4 续 / 13 行重写 | 同上 | 逐 bullet | ISCNDAGT (KB 原 ISNCNDAGT 错) |
| 457 | 6.3.5.6 - 6.4.4 | 数据行 5 / 5 行重写 | 同上 | 逐 bullet | LBBDAGNT (KB 原 LBDAGNT 错); --TETM (T-2); "version the underwent" (T-3) |
| 458 | 6.4.4 续 - 8.2.2 | 数据行 10 + 组行 2 + 6.4.4 续 / 10 行重写 | 同上 | 逐 bullet | Section 7 行 bullet 缩进格式不同 (PDF 版式), 内容逐字 |
| 459 | 8.4.1 - 8.8 / §9 / Appendices | 主表数据行 4 + §9 组行 1 + 空 bullet 行 10 + §9 子表 1 行 + Appendices 子表 2 行 / 7 行重写 | 同上 | §9 / Appendices 子表按 PDF 分表 (表头 "Change") | 空 bullet 行 10 未落 KB (无文字; 需主控定 #2) |
| 460 | Appendices 续 | 2 行 / 2→2 重写 | 同上 | 逐格 | |
| 461 | App F | 段 6 (含 Note) / 6 / 4 处值差→已修 | 一致 | — | `No Other Warranties/Disclaimers.` 行内引导语 = KB H3 (规则 6) |

- 主表数据行合计 10+6+12+13+5+10+4 = 60 + 组行 9 = 69 (= KB :337-405 行数).
- **PDF→KB 残余核 (residue.py)**: `pdftotext -raw` p444-461 全文归一后, 按长度降序删去全部 KB 单元, 残余只剩: `10` (章标题号)、单字符片段/节号 (C X N U V 5 8 9, 因脚本跳过 <2 字符单元)、跨页单元格被页眉插断的 3 处 (4.2 / 5.2 / 6.4.4 GERD 段, 已逐段核一致)、`(-DRVFL)` 与 `--TETM` (T-1/T-2)、子项字形 `o` ×2. **无遗漏句**.
- 计数: App E chk 338 单元 / 未命中 7 (全部已解释, 见段 2); App A-D chk 473 单元 / 未命中 3 (= KB 导航: `## Section 9…` 标题、交叉引用行、`### Fragment Reference Table`); App F 11 / 0.
- KB 导航 (未标 D6, 纯导航): H1 + `Source: … (Pages 444-461)` 行、`### Fragment Reference Table`、`### General Changes Throughout`、`### Key Section-by-Section Changes`、`## Section 9: Study References (p441)` + 交叉引用行、各节 `---`.
- D6 标注: 0 (改后文件无 KB 自写解释性内容; 原有改写/摘要均按 R2/D2 处理).

### census_items 逐格 (渲染 110dpi + layout/raw 脚本)
| census_item (HEAD 行) | 改后行 | 页 | 结果 |
|---|---|---|---|
| #36 Abbreviation/Full Term (:19) | :94 | p446-447 | 40 行×2 列逐格; 修 5 格 (4 句点 + "[this document]"); PDF 无表头 → KB 表头改空 |
| #37 QNAM/QLABEL/Applicable Domains (:93) | :161 | p448 | 3 行×3 列 + 表头; AESOSP / AETRTEM 一致; --REAS 第 3 格改为 PDF 原文 (KB 删了 "for an intervention" / "It", 缺句点) |
| #38 Keyword(s)/Fragment 4 列 (:119) | :177 | p449-451 | 按 PDF 重建为 2 列 106 行; 每行 = layout 行 (脚本生成 + 3 页渲染核); KB 原 106 对集合与 PDF 差 0/0 |
| #39 Domain/Description (:208) | :323 | p453 | 列序/表头错 → 重建 `Domain | Domain Abbreviation` 5 行逐格一致 |
| #40 Section Number/Name/Change(s) (:230) | :335 / :407 / :413 | p453-460 | 整表重建: 主表 69 行 (含 9 个 Section 组行) + §9 子表 1 行 + Appendices 子表 4 行; 逐行逐 bullet 对渲染 + chk.py; Section Name 列按渲染 (layout 折行混列已纠正) |

### 其他说明
- T-1 / T-2 两处 KB 有意与 PDF 字面不同 (writer.jsonl 标 SKIPPED_PDF_TYPO, note 写明 KB 写法), reviewer 逐字 diff 时预期此 2 处差异.
- ch10:141 交叉引用锚点 `#9-study-references` 依赖 S-SPREL 尚未 commit 的 DI/assumptions.md `## §9 Study References` 标题; 两批须同时过闸 / commit (check_links 现为 42).

### batch notes 结论
1. **ch10:222 MO 句 (S-HOST 转)**: "to deprecate MO in SDTMIG v3.4" 与 p452 MO 框原文逐字一致 → 属 PDF §10 自身内容, **保留不改**; 与 p285 "in a future version of the SDTMIG" 的不一致是 PDF 内部不一致 (登记 T-5, 供 T4 用户知悉, KB 不改).
2. **ch10:64-69 §9 引言 (S-SPREL 转 / O46)**: PDF p441 §9 内容, 非 §10; DI/assumptions.md 顶 `## §9 Study References` 已逐字承载 (本批只读核对) → D2: ch10 正文替换为一行交叉引用 (改后 :141), 标题行规则 6 保留. O46 中 ch10 部分关闭; "model/05:257 §9 bullet 未核" 不在本批文件, 未动.

### 变更清单 (行号 = 改后)
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | ch10:11-86 | pdf_only:p444-445:Name/Company | TABLE_REBUILT (INSERTED) | 无表 → Name/Company 74 行 | 444-445 |
| 2 | ch10:94 | census:ch10:19:hdr | REPLACED | 表头 "Abbreviation \| Full Term" → 空表头 | 446 |
| 3 | ch10:105 | census:ch10:19:Define-XML:2 | REPLACED | 补句点 | 446 |
| 4 | ch10:116 | census:ch10:19:ISO 8601:2 | REPLACED | 补句点 | 446 |
| 5 | ch10:117 | census:ch10:19:ISO 3166:2 | REPLACED | 补句点 | 446 |
| 6 | ch10:124 | census:ch10:19:SDS:2 | REPLACED | 补句点 | 446 |
| 7 | ch10:126 | census:ch10:19:SDTMIG:2 | REPLACED | 补 "[this document]" | 446 |
| 8 | ch10:141 | pdf:p441:§9 intro | REPLACED (D2) | §9 引言 + 2 bullet → 一行交叉引用到 DI | 441 |
| 9 | ch10:149 | pdf:p448:New/modified terms | INSERTED | 补 PDF 第 2 段 | 448 |
| 10 | ch10:151 | pdf:p448:Visit the CDISC CT page | INSERTED | 补 PDF 第 3 段 | 448 |
| 11 | ch10:159 | pdf:p448:C1 intro | REPLACED | "An initial set … datasets:" → PDF 原句 | 448 |
| 12 | ch10:165 | census:ch10:93:--REAS:3 | REPLACED | 改写 → PDF 原文 | 448 |
| 13 | ch10:171 | pdf:p449:App D para 1 | REPLACED | 截断/重排的 2 段 → PDF 首段全文 | 449 |
| 14 | ch10:177-284 | census:ch10:119 | TABLE_REBUILT | 4 列拼排 → 2 列 106 行 PDF 序 | 449-451 |
| 15 | ch10:292-293 | pdf:p452:intro bullets | VERIFIED | 已逐字 | 452 |
| 16 | ch10:297 | pdf:p452:The following changes… | INSERTED | 补引导句 | 452 |
| 17 | ch10:299-309 | pdf:p452:11 bullets | REPLACED | 11 条压缩改写 → PDF 原文 | 452 |
| 18 | ch10:311 | pdf:p452:MO note heading | REPLACED | `Decommissioning of MO (Morphology)` → `A note on the decommissioning of MO` | 452 |
| 19 | ch10:311-319 | pdf:p452:MO box | MOVED | MO 块移到 New Domains 之前 (正文未改) | 452-453 |
| 20 | ch10:323-329 | census:ch10:208 | TABLE_REBUILT | `Domain \| Description` (代码在前) → `Domain \| Domain Abbreviation` | 453 |
| 21 | ch10:335-405 (6.4.4 子项 o → ◦, :388) | census:ch10:230 | TABLE_REBUILT | 主表全部 Change(s) 格改写 → PDF 原文 (含 ISCNDAGT / LBBDAGNT / "Clinical Events" / 重复 4.1 行) | 453-459 |
| 22 | ch10:407-409 | census:ch10:230:§9 | TABLE_REBUILT | 组内行 → PDF 独立子表 (表头 Change) | 459 |
| 23 | ch10:411-418 | census:ch10:230:Appendices | TABLE_REBUILT | 组行 `**Appendices**` → 粗体段 + PDF 独立子表 | 459-460 |
| 24 | ch10:426 | pdf:p461:patent claims | REPLACED | patents → patent claims | 461 |
| 25 | ch10:432 | pdf:p461:this Policy | REPLACED | "the CDISC IP Policy ("the Policy")" → "this Policy" | 461 |
| 26 | ch10:432 | pdf:p461:(“the Policy”) | INSERTED | (ii) 句补定义 | 461 |
| 27 | ch10:440 | pdf:p461:WHETHER UNDER | REPLACED | 删 KB 多出的 ARISING | 461 |

### 结构改动清单 (reviewer 逐条签字)
| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| S1 | App A | 新增 Name/Company 整表 74 行, 删 KB 摘要段 | p444-445 |
| S2 | §9 块 | 正文 → 交叉引用 (D2) | p441 归 §9; DI 已承载 |
| S3 | App C | 删 `### Key Points` 标题 + 5 条 | R2/D2: 本节 PDF 5 段已逐字在 |
| S4 | App D | 删 `### Rules for Using Fragments` 标题 + 3 条 + 2 段改写; 片段表 4 列 → 2 列 | R2/D2; 规则 3 |
| S5 | App E | MO 标题换 PDF 原文 + 块前移; New Domains 表重建; 变更表拆成 PDF 的 3 张表 | p452-460; S-TDM 口径 |

### 删除清单
| # | HEAD file:line | 内容摘要 | 原因 | 保留副本 / 替代 |
|---|---|---|---|---|
| D-1 | ch10:11 | "The contributor table lists approximately 70 individuals …" | D2 KB 自写占位摘要 (真表已补) | ch10:11-86 真表 |
| D-2 | ch10:66-69 | §9 引言句 + 2 bullet | D2 跨文件重复, 非 §10 内容 | DI/assumptions.md `## §9 Study References`; ch10:141 交叉引用 |
| D-3 | ch10:81-87 | `### Key Points` + 5 条 | R2 插入后残留改写 (D2) | ch10:147-155 PDF 原文 5 段 |
| D-4 | ch10:103, :105, :107-113 | App D 首段改写 2 段 + `### Rules for Using Fragments` + 3 条 + 末段 | R2 改写 / 自添子句 "within the established naming conventions …" (PDF 无) → D2 | ch10:171 PDF 原文 |
| D-5 | ch10:119-181 | 4 列片段表 | 规则 3 表跟 PDF 走 (TABLE_REBUILT 旧版) | ch10:177-284 |
| D-6 | ch10:194-204, :208-215, :230-305 | App E 旧改写 bullet 11 条 / 旧 New Domains 表 / 旧变更表 (HEAD:218-224 MO 正文为 MOVED 原样保留, :226-228 标题+引导句保留) | VALUE_DIFF 旧值被替换 / TABLE_REBUILT | ch10:297-418 |
| D-7 | ch10:216 | `### Decommissioning of MO (Morphology)` | S-TDM: 补 PDF 原标题后删 KB 自拟同义标题 (全 KB / web/src 无 `ch10_appendices.md#` 入站锚点) | ch10:311 |
| D-8 | ch10:327 (HEAD) | 词 "ARISING" | D2 删扩写 (PDF 无) | — |

### PDF_TYPO 清单
| T | 位置 (改后) | PDF | KB 写法 | 依据 |
|---|---|---|---|---|
| T-1 | ch10:352 (4.5 行) | "(–DRVFL)" (单 en dash) | `--DRVFL` | 同表 4.4 行 "--DRVFL"; 变量前缀记法 (正确值由 PDF 自身定) |
| T-2 | ch10:387 (6.4.3 行) | "--TETM" | `--TERM` | 同句并列 --TRT / --DECOD = Topic 变量; 4.5 行 "--TRT or --TERM" |
| T-3 | ch10:386 (6.4.1 行) | "in version the underwent" | 照录 | 语法错 (应为 that), 不涉值; 照录, T4 知悉 |
| T-4 | ch10:353 (4.1 行第 2 次) | 4.1 行在 4.5 后重复 | 照录两行 | PDF 原样; 是否去重属用户裁定 (需主控定 #1) |
| T-5 | ch10:317 (MO 框) | p452 "deprecate MO in SDTMIG v3.4" vs p285 "in a future version" | 照录 p452 | PDF 内部不一致, 两处各照本节 |
| 照录 (不另立 T) | "codelists ." 多空格、"Section 9.3 PB was part of" 语法、"Nov, 2021"、"Ben Qgunsulire"/"Gbenga Ogunsulire" | — | 照录 | PDF 原文, 无法由 PDF 自身确定其他写法 |

### 范围外发现
- 无新增. (O46 中 model/05:257 §9 bullet 未核, 不在本批.)

### 需主控定
1. 变更表 4.1 行 PDF 重复 (T-4): 现照录两行; 是否删第二行.
2. p459 "Section 9. Study References" 组行下 10 个空行 (仅 • 无文字, PDF 版式残留): 未落 KB; 若需"全行照录"可补 10 行 `| | | • |`.
3. App A 名单 74 行整表补入 (原 KB 有意摘要); 若主控认为名单不属知识内容, 可改回摘要 + D6 标注.

### git diff --stat
```
 knowledge_base/chapters/ch10_appendices.md | 481 ++++++++++++++++++-----------
 1 file changed, 297 insertions(+), 184 deletions(-)
```
- md5 after `9795f2f571f6240abaf14cae10c4ca7f` (329 → 442 行). `python3 tools/check_links.py 2>&1 | grep "live docs"` → 42. 仅改本批文件 (未碰 DI/OI 等并行批文件).
- table_census.py 未由 writer 跑 (brief: reviewer 跑); 5 张 census 表 writer 侧逐格结论见上.
