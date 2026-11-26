# T2 B-CP writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `97e18955346a42d29b1528c78d1d4b8d332d8137`
- kb_files: `knowledge_base/domains/CP/examples.md` — md5 before `93c028d8bdb14fcfd14b88afa1760cdb` → after `1b25432af4d0d89feca780512ff4a399`
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_BCP_writer/` (examples.base.md, edit.py, gen.py, md_tables.json, census_before/after.json, fp_before/after.jsonl, renders p-210..p-220.png 200dpi + crops)
- 表格来源: 10 张 cp.xpt 全部由 `table_census.parse_pdf` (bbox) 生成 (gen.py; Ex9 页 p220 表头为大写 `ROW`, 解析器不识别, gen.py 里把 p220 的 `ROW` 词临时映射为 `Row` 才解析出来), 再与 `pdftotext -layout` 逐行 + 渲染图抽检 (p212 Ex2 r6-11 全列左半、p216 Ex6 r7-10 CPMRKSTR..CPTSTPNL、p220 Ex9 整页) 独立核对. 未用 atom verbatim (TABLE_ROW 原子文本多处与 PDF 不符, T1 已注).
- 叙述来源: `work/pdf_pages/ig34_p0208-0220.txt` (layout). 发现 atom verbatim 有错 (p212_a009 缺 "including"; p220_a002 "in CPBDAGNT" 实为 "using CPBDAGNT"; p220_a003 "(HA5). Rows 5-7" 实为 "(HA5) and rows 5-7"), 以 layout + 渲染 p220 为准.
- 编辑方式: `edit.py` 52 个锚定替换 (每个 assert 唯一命中), 只插入; 替换只有表格重建、VALUE_DIFF、atom 内词错 1 处、D2 删 1 处 (见下).

### 变更清单 (atoms[] 52 条)

| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | CP/examples.md:15 | ig34_p0208_a023 | INSERTED | Rows 1-3: 补 "By convention, FSC and SSC are often not included…" 两句 | 208 |
| 2 | :15 | ig34_p0209_a001 | INSERTED | 同段续句 "…CD45+ leukocytes. Once they have been included…" | 209 |
| 3 | :21 | ig34_p0209_a004 | INSERTED (+1 词 REPLACED) | Rows 8-11 补 "In these examples the laboratory…" + "In rows 9 and 11…"; 原子内 "numerator from denominator" → "numerator and denominator" | 209 |
| 4 | :23 | ig34_p0209_a005 | INSERTED | Rows 12-13 补 order 约定 + FSC SSC 3 句 | 209 |
| 5 | :25 | ig34_p0209_a006 | INSERTED | Rows 14-15 同上 (natural killer cell) | 209 |
| 6 | :52 | ig34_p0210_a020 | INSERTED | Ex1b Row 1 补 "Because FSC and SSC are nearly always used…" | 210 |
| 7 | :56 | ig34_p0210_a022 | INSERTED | Ex1b Row 4 补 "Although the preferred method…" | 210 |
| 8 | :81 | ig34_p0211_a009 | INSERTED | Ex2 Rows 9-11 之后新段 "Because the ratio in row 11…" (PDF 原文括号不闭合照录) | 211 |
| 9 | :97 | ig34_p0212_a006 | TABLE_REBUILT | Ex2 row 11 随整表补 | 212 |
| 10 | :105 | ig34_p0212_a010 | INSERTED | Ex3 新段 "In order to make it clear…Sub…" | 212 |
| 11 | :107 | ig34_p0212_a011 | INSERTED | Ex3 新段 "When considering the need to use the CPSBMRKS…" | 212 |
| 12 | :111 | ig34_p0212_a013 | INSERTED | Rows 4-5 补 numerators / CPGRPID 2 句 | 212 |
| 13 | :113 | ig34_p0212_a014 | INSERTED | 新段 "Data from rows 1-3…" | 212 |
| 14 | :115 | ig34_p0213_a001 | INSERTED | Row 6 补 5 句 (不填 CPCELSTA…RATIO in CPRESTYP) | 213 |
| 15 | :117 | ig34_p0213_a002 | INSERTED | Rows 7-9 补 6 句 | 213 |
| 16 | :119 | ig34_p0213_a003 | INSERTED | Rows 10-11 补 2 句 | 213 |
| 17 | :121 | ig34_p0213_a004 | INSERTED | 新段 "Data from rows 7-9…" | 213 |
| 18 | :136 | ig34_p0213_a013 | TABLE_REBUILT | Ex3 row 6 随整表补 | 213 |
| 19 | :148 | ig34_p0214_a001 | INSERTED | Ex4 引言后编号列表 1. (CPTSTCND) | 214 |
| 20 | :149 | ig34_p0214_a002 | INSERTED | 编号列表 2. (CPREPNUM/CPCOLSRT) | 214 |
| 21 | :155 | ig34_p0214_a005 | INSERTED | Row 7 补 "Note that calculated values…" | 214 |
| 22 | :163 | ig34_p0214_a008 | TABLE_REBUILT | Ex4 row 1 随整表补 (30 列) | 214 |
| 23 | :164 | ig34_p0214_a009 | TABLE_REBUILT | Ex4 row 2 随整表补 (30 列) | 214 |
| 24 | :165 | ig34_p0214_a010 | TABLE_REBUILT | Ex4 row 3 随整表补 (30 列) | 214 |
| 25 | :166 | ig34_p0214_a011 | TABLE_REBUILT | Ex4 row 4 随整表补 (30 列) | 214 |
| 26 | :167 | ig34_p0214_a012 | TABLE_REBUILT | Ex4 row 5 随整表补 (30 列) | 214 |
| 27 | :168 | ig34_p0214_a013 | TABLE_REBUILT | Ex4 row 6 随整表补 (30 列) | 214 |
| 28 | :169 | ig34_p0214_a014 | TABLE_REBUILT | Ex4 row 7 随整表补 (30 列) | 214 |
| 29 | :187 | ig34_p0215_a005 | TABLE_REBUILT | Ex5 row 3 (CD95X / CD95 Expression) | 215 |
| 30 | :192 | ig34_p0215_a010 | TABLE_REBUILT | Ex5 row 8 | 215 |
| 31 | :198 | ig34_p0215_a013 | INSERTED | Ex6 新段 "With the advent of increasingly complex…" | 215 |
| 32 | :200 | ig34_p0215_a014 | INSERTED | Rows 1-6 补 4 句 (CD1c- / CD303+ …) | 215 |
| 33 | :202 | ig34_p0215_a015 | INSERTED | Rows 7-10 补 "Rows 9-10 additionally show…" | 215 |
| 34 | :206 | ig34_p0215_a017 | INSERTED | Rows 15-18 补 "Rows 17-18 additionally show…"; 首句括号位置见 T-3 | 215 |
| 35 | :265 | ig34_p0218_a002 | TABLE_REBUILT | Ex7 表头 + 3 行 | 218 |
| 36 | :275 | ig34_p0218_a011 | INSERTED | Ex8 引言补 "To correct the numerator and denominator…" | 218 |
| 37 | :291 | ig34_p0219_a002 | TABLE_REBUILT | Ex8 表头 + 11 行 (32 列) | 219 |
| 38 | :325 | ig34_p0220_a006 | TABLE_REBUILT | Ex9 表头 + 14 行 (31 列), 见 "census 不可见" | 220 |
| 39 | :251 | ig34_p0217_a010 | REPLACED | "upon sample collection" → "upon sample analysis" | 217 |
| 40 | :31 | ig34_p0210_a002 | TABLE_REBUILT | Ex1a 表头 CPRESU(位于 STRESN 后) → CPSTRESU (STRESC 与 STRESN 之间); CPSPEC/CPMETHOD 顺序同 PDF; 全 16 行同步重排 | 210 |
| 41 | :35 | ig34_p0210_a005 | TABLE_REBUILT | Ex1a r3: CPSTRESU 空→% (表头重排后列) | 210 |
| 42 | :37 | ig34_p0210_a007 | TABLE_REBUILT | Ex1a r5: CPSTRESU 空→% (表头重排后列) | 210 |
| 43 | :39 | ig34_p0210_a009 | TABLE_REBUILT | Ex1a r7: CPSTRESU 空→% (表头重排后列) | 210 |
| 44 | :40 | ig34_p0210_a010 | TABLE_REBUILT | Ex1a r8: CPMRKSTR 去 "/CD45+CD3+CD19-CD14-CD56-"; CPSTRESU (表头重排后列) | 210 |
| 45 | :41 | ig34_p0210_a011 | TABLE_REBUILT | Ex1a r9: CPMRKSTR 去多余 CD19+; CPSTRESU 空→% (表头重排后列) | 210 |
| 46 | :42 | ig34_p0210_a012 | TABLE_REBUILT | Ex1a r10: CPSTRESU 空→10^6/L (表头重排后列) | 210 |
| 47 | :43 | ig34_p0210_a013 | TABLE_REBUILT | Ex1a r11: CPSTRESU 空→% (表头重排后列) | 210 |
| 48 | :44 | ig34_p0210_a014 | TABLE_REBUILT | Ex1a r12: CPMRKSTR 补 FSC SSC; CPSTRESU 空→10^6/L (表头重排后列) | 210 |
| 49 | :45 | ig34_p0210_a015 | TABLE_REBUILT | Ex1a r13: CPTESTCD MONOCLE→MONOLE; CPMRKSTR …CD56-FSC SSC/CD45+; CPSTRESU (表头重排后列) | 210 |
| 50 | :46 | ig34_p0210_a016 | TABLE_REBUILT | Ex1a r14: CPSTRESU 空→10^6/L (表头重排后列) | 210 |
| 51 | :47 | ig34_p0210_a017 | TABLE_REBUILT | Ex1a r15: CPSTRESU 空→% (表头重排后列) | 210 |
| 52 | :48 | ig34_p0210_a018 | TABLE_REBUILT | Ex1a r16: CPMETHOD FLOW CYTOMETRY→CALCULATION (表头重排后列) | 210 |

atoms 覆盖: 52/52 (REAL_GAP 38: INSERTED 24 + TABLE_REBUILT 14; VALUE_DIFF 14: REPLACED 1 + TABLE_REBUILT 13). SKIPPED: 0.

### 新增 atom 清单 (R3, 不在 atoms[], examples.md 内缺; 24 条)

T1 未分诊原因: 其中多条 fp_match `hit_target` 命中的是 `CP/assumptions.md` 的 "Example Narrative Atoms" 附录 (非本批文件), 故未进 REAL_GAP. 本批只看 examples.md, 缺则按 PDF 位置补.

| ref | 行 | 处理 |
|---|---|---|
| ig34_p0209_a002 | :17 | Rows 4-5 末 4 句 (order 约定 …"/") |
| ig34_p0209_a003 | :19 | Rows 6-7 "The order of markers…" |
| ig34_p0210_a021 | :54 | Rows 2-3 句末丢失分句 ", where they are used to distinguish…lineages." (句号→逗号接分句) |
| ig34_p0211_a004 | :71 | 改写句 "…viability marker 7AAD-." 保留, 其后插 PDF 原句 (…7AAD to exclude…(7AAD+)); "gate (CPGATE)" 句保留, 其后插 "gate name (CPGATE)" 原句 (R2) |
| ig34_p0211_a006 | :75 | 改写首句保留, 其后插 PDF 两句 (apoptotic cell state / The sponsor is reporting…); 末句改写保留, 其后插原句 (…value in CPTEST…being measured.) |
| ig34_p0212_a009 | :103 | 插 "For example, a test might…" + "Moreover…sublineage."; 改写 "3 new variables…" 后插原句 "To accommodate…"; 改写合并句后插原两句 "Two of the variables… The third variable…" |
| ig34_p0212_a012 | :109 | 插 "CPCELSTA is used to indicate that row 2…" + 末句 "The full set of markers…CPGATEDEF." |
| ig34_p0214_a017 | :175 | 插 "The analyte is repeated as part of the target cell population string (CD95+ in the example)." |
| ig34_p0217_a015 | :255 | Row 1 补 "Note in this example…(e.g. CPTSTPNL)." 3 句 |
| ig34_p0217_a016 | :257 | Row 2 补 "In this example, the CDxx marker…" 2 句 |
| ig34_p0217_a017 | :259 | Row 3 补 CD16 2 句 |
| ig34_p0218_a012 | :275 | "Although sponsors may elect…Receptor Occupancy value." |
| ig34_p0218_a013 / a014 / a015 | :277 | 新段 "Since the example is measuring binding…" 3 句 |
| ig34_p0218_a016 | :279 | 改写句 "…the mean of CDxx bound…" 保留, 其后插原句 "…the mean extent of CDxx bound…" |
| ig34_p0218_a017 | :281 | Rows 4-6 补 "Under this condition…therapeutic antibody," (PDF 以逗号结尾, 照录, T-4) |
| ig34_p0218_a018 | :283 | Rows 7-8 补 "This is indicated in CPBDAGNT…" |
| ig34_p0219_a016 | :309 | 补 "In addition to measuring the free binding sites…" 2 句 |
| ig34_p0219_a018 | :313 | 新段 "In the example showing the full set of tests…" |
| ig34_p0220_a001 / a002 | :315 | Row 1 (跨 p219-220): 改写末句 "…CPGATDEF contains the gate definition." 保留, 其后插原句 "…CPGATEDEF contains the gate definition/gating strategy." + 后续 4 句 |
| ig34_p0220_a003 | :317 | 新条目 **Rows 2-7:** |
| ig34_p0220_a004 | :319 | 新条目 **Rows 8-14:** |

注: R2 "改写保留 + 原句紧随插入" 使 :71 / :75 / :103 / :279 / :315 出现近似重复句; 是否删去改写句须主控裁 (规则 1 不许 writer 删).

### census 表处理

| census ref | 处理 | 结果 (census_after) |
|---|---|---|
| CP/examples.md:31 Ex1a (27 diffs: HEADER 1 + CELL 26) | 整表按 p210 重建 (表头 + 16 行) | OK (0 diff) |
| CP/examples.md:60 Ex1b (38 diffs: HEADER 1 + ROW_SHAPE 1 + CELL 36) | 整表重建: r1 补空 CPGATE 格 (O10 列错位); CPSPEC/CPMETHOD 顺序同 PDF; r3 CPGATE/CPGATDEF 补 LEUK/CD45+; r4 原为 r2 的复制 → PDF: CPSEQ 3 / LYMLE / CD45+FSC SSC/LEUK / 25.8 % (CPSEQ 3 与 r3 相同是 PDF 原样: r4 是 r3 的另一种写法, 叙述 Row 4 "alternative way", 故照录不登 TYPO) | OK |
| pdf_only p211-212 Ex2 (11 行) | :83-97 整表补 | OK |
| pdf_only p213 Ex3 (12 行) | :127-142 | OK |
| pdf_only p214 Ex4 (7 行) | :159-169 | OK |
| pdf_only p215 Ex5 (8 行) | :181-192 | OK |
| pdf_only p216-217 Ex6 (32 行) | :212-247 | OK |
| pdf_only p218 Ex7 (3 行) | :263-269 | OK |
| pdf_only p219 Ex8 (11 行) | :289-303 | OK |
| (census 不可见) p220 Ex9 (14 行) | :323-340 整表补; 表头照 PDF 用 `ROW` → KB 侧 UNPARSEABLE | **须 reviewer 对 p220 渲染逐格人工核** |

- 汇总: before `DIFF 2, diffs 65, 本批页 PDF_ONLY 7 (+ Ex9 不可见)` → after `OK 9 / UNPARSEABLE 1 (Ex9), diffs 0, 本批页 PDF_ONLY 0` (pdf_ranges 内剩 p199 bs.xpt, 属 BS 域非本批). cells compared 387 → 2681.
- 注意 census = 同一 bbox 解析器自比 (dispatch notes): 新表须 reviewer 用 layout 列位 / 渲染独立复核. 我做的独立抽检 (渲染图): p212 Ex2 r6-11 左 15 列逐格一致; p213 Ex3 r1-5 左 12 列一致; p216 Ex6 r7-10 CPMRKSTR..CPTSTPNL 一致; **p219 Ex8 全表 (250dpi 左右两条, 32 列 × 11 行) 逐格一致** (含 CPGRPID 空 r7/r8、CPCOLSRT MEAN r3/r6、CPREPNUM 1/2、CPANMETH r9-11); **p220 Ex9 全表 (300dpi 三条) 与 :327-340 逐格一致** (CPTPTNUM 列见 200dpi 整页: r1 空, r2-7 = 1, r8-14 = 2). 未经渲染逐格的: Ex1a/1b (census OK + layout), Ex2 右半、Ex3 右半、Ex4、Ex5、Ex6 其余格、Ex7 — bbox + layout 一致, reviewer 待核.
- 换行合并有歧义的格 (按解析器规则: 行尾 "-" 或下一行以 "/" 开头则不加空格, 否则加空格), reviewer 请看渲染:
  - USUBJID: Ex2 `0005 00542` (渲染两行 "0005"/"00542"), Ex9 `0001 00001` — 可能是一个无空格值被窄列折行; 照解析器加空格.
  - Ex2 r7/r8 CPCSMRKS `7AAD-ANXV+` (两行 "7AAD-"/"ANXV+"; 同行 r7 CPMRKSTR 单行即 `CD45+7AAD-ANXV+`, 支持无空格).
  - Ex1a r12-15 CPMRKSTR `…CD56-FSC SSC` / `…CD56+FSC SSC` (census v2 ws_only 同类).
  - Ex3 r12 CPMRKSTR `CD14+CDxx+CDyy-ANXV+`; Ex5 r6/r7 `CD45+CD19+IgD+CD27-CD95+/…`.

### 删除清单 (reviewer 逐条确认)

| # | 原位置 (base 行号) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | CP/examples.md:81 占位句 `*(Due to extreme table width, the cp.xpt table for this example contains columns: Row, … — with 11 rows of data.)*` | 替换为 `**cp.xpt**` + Ex2 整表 (:83-97) | D2 删扩写: KB 自写列清单与 PDF 矛盾 (列出 PDF 无的 CPSBMRKS; 漏 CPMRKSTR、CPTSTPNL; CPMETHOD/CPSPEC 顺序反) | 整表本身 |
| D-2 | :21 原子 ig34_p0209_a004 内 "from" | "and" | 原子内词错, 按 VALUE_DIFF 口径改 (该行只承载此一原子) | — |
| D-3 | :31-48 / :60-65 Ex1a / Ex1b 旧表 | 按 PDF 重建 | 规则 3 表格跟 PDF 走 (VALUE_DIFF 旧值替换) | — |

其余 Ex3-Ex9 占位句 `*(cp.xpt table contains N rows …)*` (KB_AUTHORED, 与 PDF 不矛盾) **未删**, 表补在其后; 建议主控裁定一并删除 (现与真表重复).

### PDF_TYPO / 照录候选 (KB 照 PDF 写入, 登记供主控裁)

| # | 位置 | PDF | KB | 说明 |
|---|---|---|---|---|
| T-1 | :81 (Ex2 段) | 括号 "(i.e., the Test Name is … NonViable"." 不闭合 | 照录 | PDF 原样 |
| T-2 | :208 Rows 19-32 | CPCSMRKR | 照录 (KB 原本即如此) | 应为 CPCSMRKS |
| T-3 | :206 Rows 15-18 首句 | "(e.g., CD40+ in rows 15-16 in addition to … marker(s))." 括号位置错 | **KB 保留原合理写法** "(e.g., CD40+ in rows 15-16) in addition to … marker(s)." | 故 ig34_p0215_a017 整句 verbatim 不会 fp 命中 |
| T-4 | :281 Rows 4-6 | 句末逗号 "…therapeutic antibody," | 照录 | PDF 原样 |
| T-5 | :92 Ex2 r6 CPDTC | 2020-08-16T04:20 (其余行 T12:20) | 照录 | 疑 PDF 笔误 |
| T-6 | :132 Ex3 r2 CPTEST | `MonoSub` (r3 起为 `Mono Sub`) | 照录 | 渲染 p213 300dpi 确认无空格 |
| T-7 | :222 Ex6 r7 CPMRKSTR | 末尾 `…CD303+CD1c` 无 "-" (r11/15 为 `CD1c-`) | 照录 | 渲染确认 (p216) |
| T-8 | :244 Ex6 r29 CPTESTCD `DCPSDC` (同类行为 DCPSDCP); r31 CPSPTSTD `CD40 MdFI … Sub Count` (同类为 `CD40 Expr MdFI … Sub`) | 照录 | bbox 词即如此 |
| T-9 | Ex6 r7-32 CPGATDEF `SSCmid\|CD45LIN-` (r3-6 为 `CD45+LIN-`) | 照录 | bbox |
| T-10 | :303 Ex8 r11 | CPORRESU `%` 但 CPSTRESU `MdFI` | 照录 | 疑 PDF 笔误 (渲染 p219 确认) |
| T-11 | :327 Ex9 r1 | CPORRES 85 vs CPSTRESC/N 83 | 照录 | 疑 PDF 笔误 (r14 为 83/83) |
| T-12 | :339 Ex9 r13 CPANMETH | "(Target Total)-(Target Total. Background)" 句点 | 照录 | r7 为逗号 |
| T-13 | :330 Ex9 r4 CPANMETH | "(Target Free) -(Target Free, Background)" 多一空格 | 照录 | 文本层即如此 |
| T-14 | :325 Ex9 表头 | `ROW` 大写、`CPTST PNL` 中间有空格 | 照录 (渲染确认) | 应为 Row / CPTSTPNL; 若主控改 `Row` 则 KB 侧可解析 (但 PDF 侧仍不可机检) |

### 范围外发现 (未改, 主控定)

- O-a 词替换型改写 (非 atoms, 规则 9 不改; 逐条 before → after):
  - :5 "CPGATE (Gate Name)" → PDF "CPGATE (Gate)"
  - :69 Ex2 引言 "their viability status in the test" → "in the dataset"; "more complex tests when the biological state" → "where"
  - :71 "Gate Definition (CPGATDEF)" → PDF "(CPGATEDEF)"
  - :73 "named in CPTEST; therefore" → PDF ", therefore"
  - :101 Ex3 引言 "qualified by the context of those variables" → PDF "content"
  - :109 "as indicated by CPCELSTA value" → "by the CPCELSTA value"; "the second record pertains" → "the record pertains"; "CPCSMRKS is used to indicate" → "The CPCSMRKS variable is used to indicate"
  - :255 / :315 "CPGATDEF contains" → PDF "CPGATEDEF" (PDF 自身 CPGATDEF/CPGATEDEF 混用)
  - :273 Ex8 首句 "This example is a use case" → PDF "The example is a use case"
- O-b `knowledge_base/domains/CP/assumptions.md:98-130` "CP – Example Narrative Atoms (Verbatim from SDTMIG v3.4)" 附录 (非本批文件): 与本次在 examples.md 补入的 Ex1a Rows 4-5 / Ex8 / Ex9 段落重复 (D2 去重候选, 保留 PDF 所属节 = examples.md); 且其中 `[ig34_p0217_a016] Row 2` 文本 "…CPGATEDEF…, as in row 1." 非 PDF 原文 (PDF 为 CPGATDEF, 无 ", as in row 1", 且漏后两句) — 与 PDF 矛盾, D2 删扩写候选.
- O-c Ex3-Ex9 KB 自写占位句 (见删除清单下注).
- O-d atom verbatim 错 (T3 回写 ledger 注意): ig34_p0212_a009 (缺 "including"; layout), ig34_p0220_a002 ("in CPBDAGNT" 应 "using"; 渲染 p220 确认), ig34_p0220_a003 ("(HA5). Rows 5-7" 应 "(HA5) and rows 5-7"; 渲染确认), ig34_p0215_a012 (atom "shows the use of", layout 为 "shows use of", KB 同 layout; 未渲染).

### 触碰过的 unparseable 表
- 新增 Ex9 表 (:325, 表头 `ROW`) KB 侧 UNPARSEABLE, PDF 侧解析器不识别 → **reviewer 须对 p220 渲染逐格人工核** (31 列 × 14 行).

### 校验 (可复跑)

```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_BCP_writer
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 9 / UNPARSEABLE 1, diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline $S/fp_before.jsonl --regress-out $S/fp_regress.jsonl
python3 tools/check_links.py | tail -1   # live docs 42 (不变)
```
- fp_match: RED, 11 条回退全部 ∉ p208-220 (`grep -E 'ig34_p02(0[89]|1[0-9]|20)_' fp_regress.jsonl` 无输出; 均为 p257/258/263 MB/MS, 并行批正在改), CP 范围 0 回退 (含 Ex1a 原 PRESENT 行 1/2/4/6 原子).
- 插入文本自检: edit.py 中所有插入字面量按句切分, `norm(s) in norm_pdf(p208-220 拼接)` 全部 True (未命中的只有旧 KB 锚点文本与占位句, 属预期); p208-220 layout 文本无弯引号, 唯一非 ASCII 破折号是 p208 标题 "CP – Examples" (未触). 本批 narrative: atoms[] 中非表格的 24 条 REAL_GAP + 1 VALUE_DIFF, 除 ig34_p0215_a017 (T-3) 外 verbatim 均在 examples.md 命中.
- 工作区另有 LB/MB/TR 文件被并行批修改, 非本批.

### git diff --stat -- kb_files
```
 knowledge_base/domains/CP/examples.md | 273 +++++++++++++++++++++++++++-------
 1 file changed, 216 insertions(+), 57 deletions(-)
```

## attempt 1 续 (2026-11-26, 主控裁定 1-7 + dispatch notes「补充口径 (B-CP 后)」)

- kb_files 扩为 CP/examples.md + CP/assumptions.md. md5: examples `1b25432a…` → `914c1918c42756d6c6b9a3126568ef3f`; assumptions `18a43173c1187b53f63c075632285d03` → `1d006b6c8ee6f822b8232eb6849b38e0`. 脚本: scratch `edit2.py` (41 个锚定替换, 均 assert 唯一/定数命中); 改前副本 `examples.attempt1.md`, `assumptions.base.md`.
- 行号: 下文均为续改后行号 (占位句删除使 Ex3 之后行号整体前移).

### 1. PDF_TYPO 重判 (取舍规则: 能由 PDF 自身定 → 写正确值; 否则照录 + T4)

| # | 位置 (现) | PDF | KB 现值 | 判定 | 依据 |
|---|---|---|---|---|---|
| T-1 | :81 | 括号 "(i.e., the Test Name is … NonViable"." 未闭合 | 补 ")" → `…NonViable").` | 改正 | 同句 "(i.e.," 开括号, 句内无其它闭合位置 |
| T-2 | :202 | CPCSMRKR | CPCSMRKS | 改正 | 变量名 (同段 / spec / 本例表头均为 CPCSMRKS); **代价: ig34_p0215_a018 fp 回退, 见下** |
| T-3 | :200 | "(e.g., CD40+ in rows 15-16 in addition to … marker(s))." | 保留 KB "(e.g., CD40+ in rows 15-16) in addition to … marker(s)." | 改正 (KB 原值) | 同段 Rows 7-10 平行句 "(e.g., CD83+ in rows 7-8) in addition to…" |
| T-4 | :271 | 段末逗号 "…therapeutic antibody," | 句号 | 改正 | 段落结束 (其后为下一 Rows 条目) |
| T-5 | :92 Ex2 r6 CPDTC | 2020-08-16T04:20 | 2020-08-16T12:20 | 改正 | 同表其余 10 行同一受试者同一检测均为 T12:20 (r6 由 r5/r1 计算) |
| T-6 | :130 Ex3 r2 CPTEST | MonoSub | Mono Sub | 改正 | 同 CPTESTCD MNS 的 r3/r8/r9/r12 均为 "Mono Sub"; 叙述 "Monocytes Sub" |
| T-7 | :214 Ex6 r7 CPMRKSTR | 分母 `…CD303+CD1c` | `…CD303+CD1c-` | 改正 | 分母 = r6 (DC Plasmacytoid) CPMRKSTR `…CD303+CD1c-`; r11/r15 同构分母均带 "-" |
| T-8a | :236 Ex6 r29 CPTESTCD | DCPSDC | DCPSDCP | 改正 | 同 CPTEST "DC Plasmacytoid Sub/DC Plasmacytoid" 的 r7/11/15/21/25 均为 DCPSDCP |
| T-8b | :238 Ex6 r31 CPSPTSTD | `CD40 MdFI CD40+CD123+ … Sub Count` | `CD40 Expr MdFI CD40+CD123+ … Sub` | 改正 | 同构 MdFI 表达行 r9/13/17/23/27 均为 "<X> Expr MdFI … Sub" (无 Count) |
| T-9 | Ex6 r7-r32 CPGATDEF (26 格) | `SSCmid\|CD45LIN-\|…` | `SSCmid\|CD45+LIN-\|…` | 改正 | r3-r6 同门控层级为 `CD45+LIN-`; 各行 CPMRKSTR 均以 CD45+ 起 |
| T-10 | :291 Ex8 r11 CPSTRESU | MdFI | % | 改正 | 同行 CPORRESU %, CPRESTYP NUMBER FRACTION, CPSTRESC = CPORRES |
| T-11 | :313 Ex9 r1 CPORRES | 85 (CPSTRESC/N 83) | 83 | 改正 | 同行 CPSTRESC/N 83; Row 1 叙述 = 只报最终占有率, 与 r14 (同受试者同 CPDTC 24T09:00, TGOCC) 83 一致 |
| T-12 | :325 Ex9 r13 CPANMETH | `(Target Total. Background)` | `(Target Total, Background)` | 改正 | r7 同公式为逗号; CPTEST 值 "Target Total, Background" |
| T-13 | :316 Ex9 r4 CPANMETH | `(Target Free) -(Target…` | `(Target Free)-(Target…` | 改正 | r10 同公式无空格 |
| T-14 | :311 Ex9 表头 | `ROW`, `CPTST PNL` | `Row`, `CPTSTPNL` | 改正 (裁定 5) | 同文件其他 9 张表均 `Row`; 变量名 CPTSTPNL (Ex2-8 表头) |

- T4 用户裁定项: 无 (14 条均可由 PDF 自身定).
- census_after2 残留 DIFF 全部为上表登记格: Ex2 :85 1 格 (T-5); Ex6 :206 29 格 (T-7 1 + T-8 2 + T-9 26); Ex8 :279 1 格 (T-10). Ex9 :311 现 KB 可解析, PDF 侧表头 `ROW` 解析器不识别 → NO_PDF (人工核见 attempt 1 渲染).

### 2. R2 残留旧改写句 (D2 去重删除)

每行用 atom 首/尾 60 字符扫 p207-221 全部原子: :71/:75/:103/:269 只承载各自 1 个原子 (p0211_a004 / a006 / p0212_a009 / p0218_a016); :303 承载 p0219_a019 + p0220_a001/a002, 删除句不在其 verbatim 内 (删后 a019/a001 仍 fp 命中) → 全部删除.

| # | 行 | 删除的旧改写句 (摘要) | 保留的 PDF 原句 |
|---|---|---|---|
| D-4 | :71 | "…based on the use of viability marker 7AAD-." | "…7AAD to exclude cells … (7AAD+)." |
| D-5 | :71 | "…is included in the gate (CPGATE)." | "…included in the gate name (CPGATE)." |
| D-6 | :75 | "…for the apoptotic lymphocyte subpopulation, both as a cell count…" | "…for the apoptotic cell state. The sponsor is reporting…" |
| D-7 | :75 | "…value of CPTEST to indicate it is … (i.e., apoptotic, being defined)." | "…value in CPTEST to indicate that it is … being measured." |
| D-8 | :103 | "3 new variables that qualify CPTEST have been added…" | "To accommodate the need for further subsetting, 3 new variables…" |
| D-9 | :103 | "Two of the variables…, and the third variable, CPSBMRKS…" | "…cell state. The third variable, CPSBMRKS…" |
| D-10 | :269 | "…the mean of CDxx bound…" | "…the mean extent of CDxx bound…" |
| D-11 | :303 | "CPGATE contains … and CPGATDEF contains the gate definition." | "…and CPGATEDEF contains the gate definition/gating strategy." |

### 3. KB 自写占位句 (D2 删扩写)

| # | 原行 (attempt 1) | 内容 |
|---|---|---|
| D-12 | :125 | `*(Due to extreme table width, the cp.xpt table for this example contains 12 rows …)*` (Ex3) |
| D-13 | :157 | `*(cp.xpt table contains 7 rows …)*` (Ex4) |
| D-14 | :179 | `*(cp.xpt table contains 8 rows …)*` (Ex5) |
| D-15 | :210 | `*(cp.xpt table contains 32 rows …)*` (Ex6) |
| D-16 | :261 | `*(cp.xpt table contains 3 rows …)*` (Ex7) |
| D-17 | :287 | `*(cp.xpt table contains 11 rows …)*` (Ex8) |
| D-18 | :321 | `*(cp.xpt table contains 14 rows …)*` (Ex9) |

(各连同其后空行; 真表在原处 `**cp.xpt**` 之下, 未动.)

### 4. CP/assumptions.md 附录 (D2)

| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-19 | assumptions.md:100-130 (说明句 + 4 个 `###` 小节 + 11 条 `[atom]` 段) | :100 一行 `> See [CP/examples.md](examples.md) for these narratives (…)`; 标题 :98 `## CP – Example Narrative Atoms (Verbatim from SDTMIG v3.4)` 保留 (规则 6) | 与 PDF 所属节 (examples.md) 重复 | examples.md: p0209_a002 :17, p0218_a012 :265, p0218_a013-15 :267, p0219_a018 :301, p0220_a002 :303, a003 :305, a004 :307 (逐条 `norm(body) in norm(examples.md)` = True) |
| D-20 | assumptions.md:108 `[ig34_p0217_a016] Row 2: … CPGATEDEF … , as in row 1.` | 删 | 与 PDF 矛盾: PDF 为 CPGATDEF, 无 ", as in row 1", 且漏后两句; PDF 原文在 examples.md :249 | examples.md :249 |
| 注 | assumptions.md 原 `[ig34_p0220_a001]` 段 | (随 D-19 删) | 附录文本 "…for the test, is not part…" 本身改写 (PDF "it is not part"); examples.md :303 为 PDF 原文 | examples.md :303 |
- 全仓 grep 无指向该节锚点的链接.

### 5. Ex9 表头 → 见 T-14.

### 6. USUBJID 换行 (Ex2 `0005 00542`, Ex9 `0001 00001`) — 保留空格
- 依据 (渲染 p212 250dpi / p220 300dpi): 两表所有行一律首行 4 位、次行 5 位. 若原值为无空格 9/10 位数字, Word 强制字符级折行会把首行填满, 首行至少容纳次行的 5 位, 不可能只放 4 位; 首行恰为完整 4 位段 → 折行发生在空格处 → 原值含空格. 同表 STUDYID `IM001-`/`123`、`CA123-`/`456` 断在连字符, 亦为合法断点, 解析器按规则无空格拼接, 一致.
- 结论: 维持 `0005 00542` / `0001 00001` (每行一致), 登记为渲染推断, reviewer 复核.

### 7. 词替换型改写 (O-a) 恢复

| 行 | before → after | 该行原子 |
|---|---|---|
| :69 | "status in the test" → "in the dataset"; "tests when the biological" → "where" | p0211_a003 only |
| :71 | "(CPGATDEF)" → "(CPGATEDEF)" | p0211_a004 only |
| :73 | "CPTEST; therefore" → "CPTEST, therefore" | p0211_a005 only |
| :101 | "context of those variables" → "content" | p0212_a008 only |
| :109 | "by CPCELSTA value" → "by the CPCELSTA value"; "the second record pertains" → "the record pertains"; "CPCSMRKS is used" → "The CPCSMRKS variable is used" | p0212_a012 only |
| :247 | "CPGATDEF contains the gate definition or gating strategy" → "CPGATEDEF …" | p0217_a015 only |
| :263 | "This example is a use case" → "The example is a use case" | p0218_a007 only |
| :5 | "CPGATE (Gate Name)" → **保留未改** | 承载 p0208_a009 + p0208_a010 (PRESENT/EXACT) → 按规则保留, 登记 |
- :303 (Ex9 Row 1) 的 CPGATDEF 改写句已随 D-11 删除, 不再适用.

### 重跑 (续)
```
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after2.json
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after2.jsonl --baseline $S/fp_before.jsonl --regress-out $S/fp_regress2.jsonl
grep -E 'ig34_p02(0[89]|1[0-9]|20)_' $S/fp_regress2.jsonl
python3 tools/check_links.py | tail -1
```
- census: `OK 6 / DIFF 3 / NO_PDF 1, diffs 31` — 31 格全部 = 登记的 PDF_TYPO 改正 (T-5/T-7/T-8/T-9/T-10), 其余 0; 本批页 PDF_ONLY 0.
- fp_match: CP 范围回退 **1 条 = ig34_p0215_a018** (Rows 19-32), 原因 = T-2 把 PDF 笔误 CPCSMRKR 改为 CPCSMRKS (取舍规则要求), 非内容丢失. **与 "CP 范围 0 回退" 闸冲突, 交主控裁**: 维持改正 (回退登记为预期) 或回滚为照录 (T4). 其余回退 (p0257/258/263) 为并行 MB/MS 批.
- 同理 (原本就未命中, 不算回退): p0211_a009 (T-1 补括号)、p0218_a017 (T-4 逗号→句号)、p0215_a017 (T-3) 与 PDF verbatim 不再逐字一致; p0212_a009 / p0215_a012 / p0220_a002 / a003 为 atom 文本错 (O-d); p0208_a009 为 :5 保留项.
- check_links: live docs 42 (不变).
- git diff --stat: `CP/assumptions.md | 32 +---`, `CP/examples.md | 283 ++++---` (2 files, 215 insertions, 100 deletions).

## attempt 1 续 2 (2026-11-26, reviewer CONDITIONAL → 主控裁定)

- md5: examples `914c1918…` → `4ea2a491085427cf70156e4570fe79ef`; assumptions `1d006b6c…` → `797f86ae5ff6d4d00a47cb1292e64b3a`.

| # | kb_file:line | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 53 | CP/examples.md:5 | ig34_p0208_a009 (O-a 原保留项) | REPLACED | "CPGATE (Gate Name)" → "CPGATE (Gate)"; 该词只属 a009 (a010 不受影响, 仍命中) — 撤销续 1 §7 的 ":5 保留" | 208 |
| 54 | CP/assumptions.md:100 | D-20 去处 | REPLACED | 交叉引用补 "Example 7 Row 2" (PDF 原文在 examples.md:249) | 217 |

- D6 (KB 自写不矛盾内容加 `> KB note (not in SDTMIG):`): 本批保留的 KB 自写内容只有 assumptions.md:98 标题 `## CP – Example Narrative Atoms (Verbatim from SDTMIG v3.4)` (规则 6 保留锚点) 与 :100 D2 交叉引用行, 均为导航, 非解释性内容 → 未加 KB note; examples.md 中 KB 自写内容 (占位句) 已全部删除, 无其它保留项. reviewer 若认为该标题须标注, 主控定.
- 重跑: fp_match CP 范围回退仅 ig34_p0215_a018 (T-2, 已登记); ig34_p0208_a009 / a010 均 hit_target = CP/examples.md. census 不变 (OK 6 / DIFF 3 / NO_PDF 1, diffs 31 = 登记 TYPO). check_links live docs 42.

## attempt 1 续 3 (2026-11-26, auditor 口径一致性 → 主控裁定)

- md5: examples `4ea2a491…` → `f34aa7506e1e07eacfcafd35d3699e86`; assumptions 未动 (`797f86ae…`, 无 CPGATEDEF).

| # | 位置 | PDF | KB 现值 | 判定 | 依据 |
|---|---|---|---|---|---|
| T-15 | CP/examples.md :71 (1), :109 (2), :117 (2), :247 (1), :267 (1), :303 (1) — 共 8 处 | 叙述中 `CPGATEDEF` | `CPGATDEF` | 改正 | PDF p202 CP spec 表变量名为 CPGATDEF (p202 第 7 行; 同页注释 "in CPGATDEF"); 与 T-2 (CPCSMRKR→CPCSMRKS) 同口径 |

- 因 T-15 不再逐字命中的原子 (预期): ig34_p0211_a004, ig34_p0212_a012, ig34_p0213_a002, ig34_p0217_a015, ig34_p0218_a014, ig34_p0220_a001. 其中原 fp 命中 → 现回退: **ig34_p0218_a014** (fp_regress); 其余 5 条改前即非 hit_target, 不计回退.
- 重跑: fp_match CP 范围回退 = ig34_p0215_a018 (T-2) + ig34_p0218_a014 (T-15), 均为登记 TYPO 改正. check_links live docs 42 (不变).
