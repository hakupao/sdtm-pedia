# T2S S-CH4 writer checkpoint (扫描批: chapters/ch04_general_assumptions.md, §4 p22-59)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `669405f` (派发时 d500b1b; 期间他批提交, ch04 未变); ch04 改前与 HEAD 一致 (md5 `4ea2579c4a8b7229a433d75e9c44cf92`, 1566 行). scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CH4_writer/`
  (base.md = `git show HEAD:`; kbbase/ = git archive HEAD; lfwd.py = layout 行/格 PDF→KB; fwd.py = 原子 PDF→KB; rscan.py = KB→PDF; census_before/after.json; fp_before/after.jsonl; 渲染 p22-p59 90dpi + 小字表裁图 200dpi)
- 历史沿用: B-ch04 (4 attempts, auditor a2 PASS) 的 T-1 ~ T-7、D6 7+ 处、导航标签口径; 本批复核后沿用编号, 新增从 T-8 起.

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| chapters/ch04 | §4 | 22-59 | **22-59** | p21 末为 §3 合规清单 (非本节); p22 首行 `4 Assumptions for Domain Models` + §4.1/§4.1.1; p59 末为 §4.5.9 Baseline Values 表 + 收尾段; p60 首行 `5 Models for Special-purpose Domains` → 无 §4 内容 |

- md5 after `8a46339fbdf39871ca70c132e92abc65` (1566 → 1590 行).

### 双向全扫 — 方法
- **PDF→KB (主判)**: `lfwd.py` = `pdf_pages/ig34_pNNNN.txt` (layout) 每一行按 ≥3 空格切成格, 每格归一后须为 KB 子串 (KB 侧**先剔除 D6 块**: `> KB note` 引用块及其后紧跟的 KB 表 / Mermaid / 图注, `strip.py`); 不依赖原子. 辅判 `fwd.py` = `pdf_atoms.jsonl` 该页全部 ig34 原子 (含 TABLE_ROW / TABLE_HEADER / CODE_LITERAL), 同样剔除 D6 后比.
- **KB→PDF**: `rscan.py` = KB 每句 / 每表格单元格归一后须在 p22-59 **layout 文本** (不含原子) 中出现; 未命中项再做去连字符 + 去空白复核 (layout 折行把 "Define-XML"、"one-to-one" 等复合词拆开, 多行单元格被分行).
- 表格: 全部 KB 表对渲染图逐格核 (90dpi 整页 + 200dpi 小字裁图: p32/33/35/36/39/40/41/46/56/58/59); `table_census.py` 前后各跑一次.
- 计数为改后; "改前" 列给出本批修掉的缺口.

### 双向全扫 — 逐页日志 (p22-59, 每页一行)
| 页 | 节 | PDF→KB: layout 格数 / 命中 / 缺→已补 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 |
|---|---|---|---|---|---|
| 22 | §4 / §4.1-§4.1.5 | 41 / 40 / 0 | :1-41; :3 Source 行 + :7 Overview D6 + :17 D6 (既有) | — | 未命中 = 章标题 `4 Assumptions…` (= KB H1 等价, 规则 6 不动) |
| 23 | §4.1.5-§4.1.7 | 50 / 50 / 1→1 | :43-80; :50-56 Core 表 D6 (既有) | Core 表 = KB_AUTHORED D6 (census 项) | 补: :60 "Controlled Terminology (URL) for standard domain codes)." (KB 原为 "at URL … codes.)", 自加词 "at") |
| 24 | §4.1.7 / §4.1.7.1 | 53 / 53 / 0 | :76-96 | relrec.xpt 2 行 (census OK) | 列表 1-10 编号一致 |
| 25 | §4.1.7.1 QS 表 | 313 / 310 / 0 | :98-149 | qscg 8 行 / qspi 6 行 / qssw 10 行 / suppqscg 2 行 (census OK; 渲染核) | 未命中 3 = 页脚. 数据集标题 "Dataset for … — xx.xpt" 拆回 PDF 两行 (#2) |
| 26 | §4.1.7.1 / §4.1.8 / §4.1.9 | 128 / 127 / 1→1 | :150-204 | suppqspi 10 行 / suppqssw 2 行 (census OK; 渲染核) | 未命中 = T-7 VISTNUM (沿用); 补: :202 句末 ":" → "." (#3) |
| 27 | §4.1.9 MK | 48 / 48 / 0 | :204-233 | — | PDF ") ." / "MKHNDPOS".This 空格 = T-10 (KB 不动) |
| 28 | §4.1.9 MK 表 / §4.2 / §4.2.1-§4.2.2 | 50 / 50 / 0 | :233-288; :260-273 D6 (既有) | MK 表 1 行 × 7 格渲染一致 (census 项 :235) | |
| 29 | §4.2.2-§4.2.6 | 64 / 64 / 0 | :288-322 | dm.xpt ×2 (census OK) | :324 "variables — such as" 两侧空格 = 排版 (S-TYPO 范围, 未改) |
| 30 | §4.2.6 层级/分组 | 54 / 54 / 3→3 | :326-366 | — | 改前未命中 3 = 应力试验 i./ii./iii. 列表; 修: 层级缩进 (DOMAIN 与 STUDYID 同级), "For the subject"/"Within subjects" 下 PDF 编号 "1.", 应力试验段拆段 + i./ii./iii. (#4-#7) |
| 31 | §4.2.6 / §4.2.7 / §4.2.7.1 | 48 / 48 / 0 | :368-404 | — | --LNKID/--LNKGRP 列表 PDF 为 1./2. → 改 (#8) |
| 32 | §4.2.7.1 | 56 / 55 / 0 | :406-462 | EXADJ CRF 3 行 / CMINDC CRF 6 选项 / CMINDC×3 + QNAM×2 小表 渲染逐格一致 | 未命中 = 填写横线长度 (图形); CMINDC CRF 表头 "Options" = KB 自造 → 空 (#9); 选项符号 [ ] vs PDF / o = U4 (S-TYPO); PDF "field :" 空格 = T-10 |
| 33 | §4.2.7.2 / §4.2.7.3 | 66 / 64 / 0 | :464-526 | Eye Color CRF / SCTEST×3 / 伴随药 CRF / CMTRT 表 渲染 (200dpi) 逐格一致 | 未命中 2 = 填写横线; 两张 CRF 表头 "Options" → 空 (#9) |
| 34 | §4.2.7.3-§4.2.8.2 | 31 / 31 / 0 | :524-562; :533-545 Mermaid D6 (既有, 与图逻辑一致) | — | `**Figure. Decision Tree…**` 已有 |
| 35 | §4.2.8.2-§4.2.8.3 | 77 / 77 / 0 | :559-615 | ae/suppae Ex1-Ex3 前 5 表 渲染 (200dpi) 逐格一致 | :559 "For example:" → "For example," (#10); "**Example 1:**" 等标签见 KB 自造标签段 |
| 36 | §4.2.8.3-§4.3.1 | 46 / 46 / 0 | :618-666 | suppae Ex3 2 行一致 | :632 "For example," (#10) |
| 37 | §4.3.2-§4.3.6 | 44 / 43 / 0 | :668-693 | — | 未命中 = T-3 (PDF 少 "in", 沿用) |
| 38 | §4.3.6-§4.4.1 | 59 / 58 / 0 | :693-737 | 主题变量表 5 行 × 4 列一致 | 未命中 = 正则 `(…(+\|-)…)` (KB :727 代码字面量逐字在, 扫描器把 \| 当分隔的假阳) |
| 39 | §4.4.1-§4.4.2 | 61 / 59 / 2→2 | :737-777 | 精度表 7 行 × 4 列 (200dpi) 一致; 首列表头 PDF 空 (KB "#") → 空 (#12) | 补: :746 句末 "." ; :758 "(e.g. 2001…)" 照 PDF (#11); 余 2 = 正则假阳 |
| 40 | §4.4.2-§4.4.3.1 | 70 / 70 / 0 | :777-822 | 区间表 4 行 / 省略分量表 6 行 (200dpi) 一致; 首列表头 "#" → 空 (#12) | |
| 41 | §4.4.3.1-§4.4.4 | 60 / 60 / 0 | :822-876; :826-832 D6 (既有) | 时长表 10 行 × 2 一致 | |
| 42 | §4.4.4-§4.4.5 | 55 / 55 / 0 | :876-922; :896, :907-908 D6 (既有) | lb.xpt 3 行 × 5 一致 (census 项 :920) | |
| 43 | §4.4.6-§4.4.7 | 49 / 46 / 0 | :926-954; :938-943 --STRF 表 D6 (既有) | — | 未命中 3: `"ONGOING"'` 多撇号 = **T-8 (新)**; "period. Although" / "CMSTRF.Some" = KB 标签 "Important restriction…"/"Caution…" 断段 + PDF 缺空格 (T-10) |
| 44 | §4.4.7 | 28 / 28 / 1→1 | :954-1020; :959-966 / :983-986 D6 (既有) | — | 补: 图标题行 `**Figure. Example of --ENRTPT…**` (:1003); Mermaid 节点文字按图改 ("MHENTPT Assessment Date and Reference Time Point of 2006-11-02", "2002"), 图注 "The medical event …" 照图; D6 措辞补 "with added edge labels not in the figure" (#13) |
| 45 | §4.4.7 Ex2-3 / §4.4.8 / §4.4.9 | 43 / 43 / 0 | :1020-1064 | Collection Type 表 2 行 × 4 一致 | |
| 46 | §4.4.9 / §4.4.10 | 71 / 71 / 1→1 | :1064-1114; :1078-1093 变量表+Mermaid D6 (既有) | VS 3 行 / LB 3 行 × 6 (200dpi) 一致 | 补: `**Figure. Representing Time Points**` (:1076) (#14); :1103 "VSDTC−VSRFTDTC" U+2212 vs PDF "-" = dash 类 (S-TYPO, 范围外登记) |
| 47 | §4.4.10 | 61 / 60 / 0 | :1114-1157 | Option 1 表 18 行 × 5 一致 (合并单元格以空格表示) | 未命中 = PDF "(–TPTREF" en dash = **T-9 (新)**; 4 个场景 PDF 为圆点列表, KB 1-4 编号 → "- " (#15) |
| 48 | §4.4.10 / §4.4.11 | 65 / 65 / 0 | :1158-1187 | Option 2 表 18 行 × 5 一致 | |
| 49 | §4.4.11 | 48 / 47 / 0 | :1187-1213 | — | 未命中 = T-4 occurrs (沿用) |
| 50 | §4.4.11 | 47 / 47 / 0 | :1213-1235 | — | |
| 51 | §4.4.11 / §4.5 / §4.5.1.1 | 41 / 41 / 1→1 | :1235-1272; :1259-1266 Mermaid D6 (既有, 已注明增边) | — | 补: `**Figure. Original to Standardized Results**` (:1257) (#14) |
| 52 | §4.5.1.1-§4.5.1.3 | 48 / 48 / 0 | :1272-1328; :1309 D6 (既有) | — | "**Example 1 (lb.xpt)**" 拆为 "**Example 1**" + 表前 "lb.xpt" (PDF 版式) (#16) |
| 53 | §4.5.1.3 Ex1-Ex2 | 155 / 151 / 0 | :1328-1358 | lb 12 行 × 12 一致; eg Row 1-3 一致 | 未命中 = 页脚 3 + T-5 (Row 1 说明 LBSTRESC, 沿用) |
| 54 | §4.5.1.3 Ex2-Ex3 / §4.5.2-§4.5.3.1 | 104 / 101 / 0 | :1358-1395 | eg Row 4-7 = T-1 (沿用, census DIFF 2 格); vs 7 行 × 11 一致 | 未命中 = 页脚; PDF "VSTESTCD= " 空格 = T-10 |
| 55 | §4.5.3.1-§4.5.3.2 | 66 / 65 / 0 | :1395-1434 | mh 1 行 / suppmh 2 行 × 11 一致 | 未命中 = "datasets. IETEST" (KB 标签 "Exception — IETEST…" 断段) |
| 56 | §4.5.3.2 / §4.5.4 | 123 / 122 / 0 | :1434-1494 | ae/suppae/pr/supppr Ex2-3 一致; 约定表: KB 多一列 "Convention" (Storage/Split rule/Label, KB 自造) → 删列, 4 列 × 3 行 (200dpi) 逐格一致 (#17) | 未命中 = "Supplemental Qualifiers – SUPP--" en dash vs KB "--" (dash 类, 范围外登记) |
| 57 | §4.5.4-§4.5.7 | 94 / 92 / 0 | :1494-1528 | suppae 3 行 × 11 / suppho 1 行 一致 | 未命中 = T-6 "result or of" (沿用) + "– SUPP--" dash 类 |
| 58 | §4.5.7-§4.5.8 | 57 / 57 / 0 | :1528-1567 | --PRESP 情况表 4 行 × 4 (200dpi) 一致 | |
| 59 | §4.5.8-§4.5.9 | 56 / 54 / 0 | :1567-1580 | baseline 表 3 行 × 5 (200dpi) 一致 | 未命中 2 = 多行单元格折行 (渲染核一致) |

- KB→PDF 未命中 (改后, D6 块外) 全部定性: (a) 多行表格单元格被 layout 拆行 (QS/MK/CRF/日期/约定/baseline 表) — 已逐格渲染核一致; (b) 复合词折行 (:190 :478 :689 :800 :912 :1126 :1211 :1270 :1405 :1549) — 去连字符复核命中; (c) :934 = T-8 (KB 正确写法); :670 T-3, :1199 T-4, :1348 T-5, :1511 T-6 (KB 正确写法); (d) 数据集名行 "ae.xpt:" 等 (PDF 无冒号, 导航标签); (e) 导航 / KB 标签 (见下 "KB 自造标签"); (f) :818 `PnYnMnDTnHnMnS` *- or -* `PnW` = PDF 居中三行的排版; (g) :1588/:1590 新交叉引用. **无未定性 KB 自写解释句** (D6 块外).
- fwd.py (原子) 改后不命中 55 (改前 62): 余量均为原子噪声 (p56-p59 原子大量编造, 如 p59_a010 "until the subject ceases or stops" ≠ PDF "dies"; p57_a002/a006 句子 PDF 不存在; TRUNCATED_AT_PAGE_BOUNDARY 3 条) 或上述已登记项; layout 主判无对应缺口.

### census_items 逐格 (39 项; 改后行号)
| # | KB 表 (HEAD → 改后) | 类 | PDF 页 / dpi | 结果 |
|---|---|---|---|---|
| 1 | :391 → :408 EXADJ CRF | C3 | p32 / 200 | 表头 2 格 + 3 行 × 2 一致; 选项符号 [ ] vs PDF 私用区复选框 = U4 (S-TYPO) |
| 2 | :408 → :425 Indication for analgesic CRF | C3 | p32 / 200 | PDF 无表头行, 左格 "Indication for analgesic" + 右格 6 选项; KB 表头右格 "Options" 为自造 → 空 (#9); 6 选项一致; 横线长度 = 图形 |
| 3 | :453 → :470 Eye Color CRF | C3 | p33 / 200 | 同上, 5 选项一致; "Options" → 空 |
| 4 | :465 → :482 SCTEST (OTHER) | C3 | p33 / 200 | 2 行 × 3 一致 |
| 5 | :471 → :488 SCTEST (GRAY) | C3 | p33 / 200 | 一致 |
| 6 | :477 → :494 SCTEST (BLUEISH GRAY) | C3 | p33 / 200 | 一致 |
| 7 | :487 → :504 伴随药 CRF | C3 | p33 / 200 | 左格问句 (PDF 4 行折行) + 5 选项一致; "Options" → 空; "subject’s" 弯撇号 = S-TYPO |
| 8 | :497 → :514 CMTRT/CMPRESP | C3 | p33 / 200 | 3 行 × 2 一致 (DICLOFENAC CMPRESP 空) |
| 9 | :558 → :576 ae.xpt AETERM/AELOC | C3 | p35 / 200 | 2 行 × 2 一致 |
| 10 | :564 → :582 suppae (AELOC1-3) | C3 | p35 / 200 | 4 行 × 3 一致 |
| 11 | :576 → :594 ae.xpt AEREL/AEACN | C3 | p35 / 200 | 一致 |
| 12 | :582 → :600 suppae (ABC/XYZ) | C3 | p35 / 200 | 5 行 × 3 一致 |
| 13 | :597 → :615 ae.xpt (POSSIBLY RELATED) | C3 | p35 / 200 | 一致 |
| 14 | :603 → :621 suppae (AERELX/AEACNX) | C3 | p36 / 200 | 3 行 × 3 一致 |
| 15 | :678 → :697 主题变量表 | C3 | p38 / 90 | 6 行 × 4 一致 (DS Modified 空) |
| 16 | :749 → :768 日期精度表 | C3 | p39 / 200 | 8 行 × 4 一致; 首列表头 PDF 空, KB "#" → 空 (#12) |
| 17 | :761 → :780 不确定区间表 | C3 | p40 / 200 | 5 行 × 3 一致; "#" → 空 |
| 18 | :1034 → :1055 Collection Type | C3 | p45 / 90 | 3 行 × 4 一致 |
| 19 | :1074 → :1097 VS 时间点 | C3 | p46 / 200 | 4 行 × 6 一致 |
| 20 | :1084 → :1107 LB 时间点 | C3 | p46 / 200 | 4 行 × 6 一致 (-PT15M) |
| 21 | :1112 → :1135 Option 1 | C3 | p47 / 90 | 19 行 × 5 一致; PDF 合并单元格 (VISIT/VISITNUM/--TPTREF 跨行) → KB 首行填值, 后续空 |
| 22 | :1135 → :1158 Option 2 | C3 | p48 / 90 | 19 行 × 5 一致, 同上 |
| 23 | :1511 → :1542 --PRESP 情况表 | C3 | p58 / 200 | 5 行 × 4 一致 (原子 a013/a017 抽取错) |
| 24 | :52 Core 表 | B (KB_AUTHORED) | p23 / 90 | D6 (上方 :50 KB note); 内容与 PDF Required/Expected/Permissible 三条不矛盾; 未改 |
| 25 | :223 → :235 MK 表 | B | p28 / 90 | 2 行 × 7 一致 |
| 26-30 | :421/:425/:431/:435/:443 → :438/:442/:448/:452/:460 CMINDC / QNAM 小表 | B | p32 / 200 | 各 2 行一致 (OTHER / FRACTURE / BROKEN ARM; CMINDOTH Other Indication BROKEN ARM) |
| 31 | :770 → :789 省略分量表 | B | p40 / 200 | 7 行 × 4 一致; "#" → 空 |
| 32 | :825 → :844 时长表 | B | p41 / 90 | 11 行 × 2 一致 (12¼, 4 ½) |
| 33 | :901 → :920 lb.xpt visit | B | p42 / 90 | 4 行 × 5 一致 |
| 34 | :921 → :940 --STRF 表 | B (KB_AUTHORED) | p43 | D6 (:938); 值集与 PDF 句一致; 未改 |
| 35 | :942 → :961 --STRTPT 表 | B (KB_AUTHORED) | p44 | D6 (:959); 未改 |
| 36 | :1057 → :1080 --TPT 变量表 | B (KB_AUTHORED) | p46 | D6 (:1078, 已注明 added labels); 未改 |
| 37 | :1328 → :1357 eg.xpt | A DIFF | p53-54 / 90 | T-1 (Row 5/6 PDF 表与说明矛盾, KB 跟说明) 沿用; census DIFF 2 格不变 |
| 38 | :1450 → :1481 >200 约定表 | B | p56 / 200 | PDF 4 列无行标签列; KB 删自造 "Convention" 列 (Storage/Split rule/Label) → 4 列 × 3 行逐格一致 (#17, 结构改动 S-3) |
| 39 | :1545 → :1576 baseline 表 | B | p59 / 200 | 4 行 × 5 一致 (PDF "--LOBXFL" 格内折行) |
- `table_census.py` (manifest = ch04 × p22-59): before = after `OK 19 / UNPARSEABLE 38 / DIFF 1, cells 1009, diffs 2` (2 = T-1); 本页段 PDF_ONLY 0.

### 变更清单 (行号 = 改后)
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | ch04:60 | ig34_p0023_a010 | REPLACED | "Controlled Terminology at URL for standard domain codes.)" → "Controlled Terminology (URL) for standard domain codes)." (删 KB 自加 "at") | 23 |
| 2 | ch04:100-102 / 115-117 / 128-130 / 147-149 / 156-158 / 173-175 | pdf:p25-26 数据集标题行 | REPLACED | "**Dataset for X — y.xpt**" → "**Dataset for X**" + 单独一行 "y.xpt" ×6 (PDF 两行, "—" 为 KB 自加) | 25-26 |
| 3 | ch04:202 | ig34_p0026_a039 | REPLACED | "…natural key for the MK domain:" → "…domain." | 26 |
| 4 | ch04:328-337 | pdf:p30:1-9 Hierarchy | REPLACED | 代码块缩进按 PDF: STUDYID/DOMAIN 同级 (KB 原把 DOMAIN 缩进到 STUDYID 下) | 30 |
| 5 | ch04:341-343, 345 | pdf:p30:11-12 | REPLACED | "**For the subject:**" + 段落 → "**For the subject**" + "1. All records…" (PDF 编号列表); "Across subjects (…):" 去冒号 | 30 |
| 6 | ch04:355-363 | pdf:p30:34-39 | REPLACED | c. 段内 "Stress-test data collection may capture the following:" 按 PDF 另起段; 3 条 "-" → "i./ii./iii." | 30 |
| 7 | ch04:367-369 | pdf:p30:41-44 | REPLACED | "Within subjects (…):" 去冒号; --GRPID 段前加 PDF 编号 "1." | 30 |
| 8 | ch04:375-376 | pdf:p31:4-7 | REPLACED | --LNKID / --LNKGRP 两条 "-" → "1." / "2." | 31 |
| 9 | ch04:425 / 470 / 504 | census :408 / :453 / :487 | REPLACED | CRF 表头右格 "Options" (KB 自造) → 空 ×3 | 32-33 |
| 10 | ch04:559 / 632 | pdf:p35:1 / p36:13 | REPLACED | "For example:" → "For example," ×2 (列表前补空行) | 35-36 |
| 11 | ch04:746 / 758 | ig34_p0039_a004 / a016 | REPLACED | 句末补 "."; "(e.g., 2001-12-26T00:00:01)" → "(e.g. 2001-…)" 照 PDF | 39 |
| 12 | ch04:768 / 780 / 789 | census :749 / :761 / :770 | REPLACED | 序号列表头 "#" (KB 自造) → 空 ×3 | 39-40 |
| 13a | ch04:1003 | ig34_p0044_a022 | INSERTED | `**Figure. Example of --ENRTPT and --ENTPT for Medical History**` (原仅在 D6 句内) | 44 |
| 13b | ch04:1005 | D6 | REPLACED | D6 措辞补 ", with added edge labels not in the figure" | 44 |
| 13c | ch04:1009-1010 | pdf:p44 图 | REPLACED | Mermaid 节点 "Reference Time Point 2006-11-02" → "MHENTPT Assessment Date and Reference Time Point of 2006-11-02"; "2002 (MHSTDTC)" → "2002" (照图) | 44 |
| 13d | ch04:1017 | pdf:p44 图框文字 | REPLACED | "The event may or may not…" → "The medical event may or may not…" (照图) | 44 |
| 14 | ch04:1076 / 1257 | ig34_p0046_a012 / p0051_a018 | INSERTED | `**Figure. Representing Time Points**` / `**Figure. Original to Standardized Results**` (同 :531 --OBJ 图先例) | 46 / 51 |
| 15 | ch04:1123-1126 | pdf:p47:8-19 | REPLACED | 4 个场景 "1.-4." → "- " (PDF 圆点列表) | 47 |
| 16 | ch04:1315/1329, 1346/1355, 1367/1375 | pdf:p52-54 Example 1-3 | REPLACED+INSERTED | "**Example n (xx.xpt)**" → "**Example n**"; 表前补 PDF 数据集名行 "lb.xpt"/"eg.xpt"/"vs.xpt" | 52-54 |
| 17 | ch04:1481-1485 | census :1450 | TABLE_REBUILT | 删 KB 自造首列 "Convention" (Storage / Split rule / Label); 余 4 列表头 + 3 行逐格 = PDF | 56 |
| 18 | ch04:1586-1590 | O19 (B-ch04 review L8) | DELETED (D2) | Appendix 引导句 + 2 个 KB 自造小标题 + 3 句 Chapter 6 副本 → 2 行交叉引用 (EX/examples.md#example-6, MB/examples.md#example-3) | 115 / 261 (批外页) |
- 插入文字全部取自 layout 文本 + 渲染核对 (未用原子 verbatim). 新增 atom 清单 (R3): #1 #3 #11 #13a #14 (原子 a010/a039/a004/a016/a022/a012/a018 改后命中, fp 翻转 2 条见下).

### 结构改动清单 (reviewer 逐条签字)
| # | 位置 | 改动 | 依据 / 与历史口径的冲突 |
|---|---|---|---|
| S-1 | :341-376 | 3 处 "-"/段落 → PDF 编号 "1." / "1. 2."; 应力试验 i./ii./iii. 拆段 | PDF p30-31 列表形态; 文字未变 |
| S-2 | :1123-1126 | 编号列表 → 圆点列表 | PDF p47 |
| S-3 | :1481-1485 | 约定表删 KB 自造标签列 "Convention" | 规则 3 "表格跟 PDF 走 (列数不同按 PDF)"; **冲突**: B-ch04 a4 checkpoint 与 auditor 曾把该列记为 "纯导航" 接受 — 本批按规则 3 改, 请 reviewer 定 |
| S-4 | :100-175, :1315-1375 | 数据集标题 / Example 标签拆回 PDF 两行版式 | PDF p25-26, p52-54 |
| S-5 | :1586-1590 | Appendix 去重 (O19) | dispatch "KB 自写附录与 PDF 内容重复 → 附录处换一行交叉引用"; 副本 EX/examples.md:239 (§6.1.3.3 Example 6) / MB/examples.md:156-158 (§6.3.5.7 Example 3) 均在; 全库无 ch04 锚点入站链接; **O19 不在本批 out_of_scope[]**, 因同文件终版一并处理, 请主控确认 |
- 无 assumption 整条增删 (ch04 无 assumptions 列表).

### 删除清单
| # | 原位置 (base) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | :60 "at" | — | VALUE_DIFF 旧值替换 (#1) | — |
| D-2 | :100-163 "— xx.xpt" 合并写法 ×6, :1290/1319/1338 "(xx.xpt)" ×3 | 拆行 | 版式恢复 (#2 #16), 文字未丢 | — |
| D-3 | :408/:453/:487 表头 "Options"; :749/:761/:770 表头 "#" | 空 | KB 自造表头词 (#9 #12) | — |
| D-4 | :1450-1454 "Convention / Storage / Split rule / Label" 列 | 删列 | KB 自造列, PDF 无 (#17) | — |
| D-5 | :988-989 Mermaid 旧节点文字; :996 "The event" | 照图 | VALUE_DIFF (#13c #13d) | — |
| D-6 | :1557-1566 Appendix 引导句 2 句 ("…recorded here for verbatim atom coverage. They illustrate…") + 小标题 `### §6.1.3.3 … (p115)` / `### §6.3.5.7 … (p261)` + 3 句副本 | 2 行交叉引用 | D2 附录去重 (O19); 引导句为 KB 元说明 (非 SDTM 解释), 随附录删 | EX/examples.md:239; MB/examples.md:156-158 |
- fp_match: 删除后 p115/p261 原子仍命中各自域文件 (翻转 0, 见复验).

### D6 标注清单
- 本批新增 D6: 0. 修改 D6 措辞 1 处 (:1005, 补 "with added edge labels not in the figure").
- 沿用既有 D6 (复核不矛盾): :7 Overview, :17 §4.1.1 SDTM 说明, :50 Core 表, :260 主题变量约定, :533 --OBJ Mermaid (与 p34 图分支一致), :826 duration designators, :896 Partial dates, :907-908 VISITDY/VISIT, :938 --STRF 表, :959 --STRTPT 表 (AFTER 限定与 p44 一致), :983 Example applications, :1005 MH 图, :1078 --TPT 变量表+图, :1259 ORRES 图 (已注明增边), :1309 NOT DONE 时空值.

### KB 自造标签 (未改, 需主控定 #1)
- `**Example 1:**`/`**Example 2:** For example, …`/`**Example 3:** For example, …` (:572 :590 :611, p35); `**Important restriction on --ENRF:**` (:949) / `**Caution on mixing collected and derived values:**` (:951) — 插在 PDF 同一段中间并断段 (p43); `**Scenarios where not all 3 uniqueness variables … are needed:**` (:1119, p47); `**Exception — IETEST in IE and TI domains:**` (:1397, p55); `**Domain-specific conventions for text > 200 characters:**` (:1464, p56); `**QS Domains**`/`**SUPPQS Domains**` = PDF 原有标题 (非自造).
- B-ch04 a4 + auditor 把上述记为 "纯导航标签, 不加 D6"; S-SPC2 主控裁定 "KB 自写解释性 *Note:* 一律 D6, 纯交叉引用才算导航". 这些标签介于两者之间 (短, 但 "Important restriction"/"Caution" 带解释色彩且拆开了 PDF 段落). 本批按 B-ch04 已过闸口径保留不改.

### PDF_TYPO 清单
| # | 位置 | PDF | KB | 依据 |
|---|---|---|---|---|
| T-1 | p54 eg.xpt (ch04:1357) | 行号 4,6,5,7 与 Row 5/6 说明矛盾 | 跟说明 | 沿用 (复核成立) |
| T-2 | p53 lb Row 7 | 说明 LBDRVFL, 表头 LBLOBXFL | 照表 | 沿用 (T4 用户裁定项) |
| T-3 | p37 (ch04:670) | "the case that appears the source" | "appears in the source" | 沿用 |
| T-4 | p49 (ch04:1199) | "occurrs" | "occurs" | 沿用 |
| T-5 | p53 Ex2 Row 1 (ch04:1348) | "copied into LBSTRESC and LBSTRESN" (eg 例) | EGSTRESC/EGSTRESN | 沿用 |
| T-6 | p57 (ch04:1511) | "a result or of" | "a result of" | 沿用 |
| T-7 | p26 (ch04:200) | "VISTNUM" | VISITNUM | 沿用 |
| **T-8** | p43:13 (ch04:934) | `"ONGOING"',` 多一个撇号 | `"ONGOING",` | 新; 同句其余三项均为 `"X",` 格式, 正确值由 PDF 自身确定 |
| **T-9** | p47:17 (ch04:1126) | "(–TPTREF" (en dash 单字符) | "(--TPTREF" | 新; 同句 "--ELTM" 及全节均为双连字符变量前缀 |
| **T-10** | p27 `") ."`, `"MKHNDPOS".This`; p32 "field :"; p43 "variables.As" / "CMSTRF.Some"; p51 "derived.For"; p54 "VSTESTCD= " | 空格缺失 / 多余 | 正常空格 | 新 (归组); 纯排版空格, KB 保留正确写法 |

### 范围外发现 (未改)
1. dash 类 (S-TYPO 范围, 脚本可能漏): ch04:1103 "VSDTC−VSRFTDTC" 用 U+2212 (PDF p46 为 "-"); ch04:1491 / :1520 "Supplemental Qualifiers -- SUPP-- Datasets" (PDF p56/p57 为 "Supplemental Qualifiers – SUPP--", en dash 被写成 "--"); ch04:324 "variables — such as … (Subcategory) — that" em dash 两侧多空格 (PDF 无空格).
2. CRF 选项符号 `[ ]` (:408-:510 共 4 张 CRF) vs PDF 私用区复选框 / "o" — U4, S-TYPO.

### 需主控定
1. KB 自造标签 (上段) 是否按 S-SPC2 口径加 D6 或删; 本批未动.
2. S-3 (约定表删列) 与 B-ch04 "纯导航" 口径冲突, 请 reviewer / 主控签字.
3. S-5 Appendix 去重处理了 O19 (不在本批 out_of_scope[]); 如不接受, 回退仅需恢复 :1586-1590 为 base :1555-1566.

### 复验 (改后)
- lfwd (layout, 剔 D6): 未命中 30 (改前 41), 全部已定性 (见逐页日志); fwd (原子, 剔 D6): 55 (改前 62).
- rscan: D6 块外未命中全部定性 (见上).
- `table_census.py`: OK 19 / UNPARSEABLE 38 / DIFF 1 (T-1), 与改前同.
- fp_match (全库, 前 = HEAD 副本): ch04 相关原子翻转 = +2 (ig34_p0039_a004 / a016 None → ch04), 回归 0; p115/p261 原子 hit_any 仍非空.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → 42.

### 验证命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CH4_writer
F=knowledge_base/chapters/ch04_general_assumptions.md
python3 $S/lfwd.py $F | grep "  p"      # 30 行, 均已定性
python3 $S/fwd.py $F | grep -c MISS     # 55
python3 $S/rscan.py $F                  # D6 块外项见上
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 19 / UNPARSEABLE 38 / DIFF 1
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbbase/knowledge_base --out $S/fp_before.jsonl
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 .../chapters/ch04_general_assumptions.md           | 146 ++++++++++++---------
 1 file changed, 85 insertions(+), 61 deletions(-)
```

### 更正 (同 attempt, 自查后; 以下取代上文对应处)
- 终态 md5 `8a46339fbdf39871ca70c132e92abc65` (1590 行); 上文 "复验" 中 fp_match / rscan 是在第二组改动 (#16 Example 标签拆行) 之前跑的, 现已对终态重跑: fp_match ch04 相关原子翻转仍为 +2 (ig34_p0039_a004 / a016 → ch04), 回归 0 (`fp_final.jsonl`); rscan 终态与前次差异仅为 3 条 "**Example n (xx.xpt)**" 标签消失 (拆行后命中).
- lfwd 改前未命中 = **40** (base 剔 D6 后实测 `grep -c "  p" lfwd_base_strip.txt`), 改后 30; 上文 "改前 41" 作废.
- 200dpi 裁图: p32 / p33 / p35 / p36 / p39 / p40 / p41 / p46 / p56 (表头 + 表体两张) / p58 / p59 均已打开并覆盖整表, 逐格一致; p38 / p42 / p45 / p47 / p48 / p28 为 90dpi 整页核 (字号足够, 上表已如实标 90).
- 终态行号更正 (第二组改动后 +2~+6): "Exception — IETEST" 标签 :1403 (上文 :1397); "Domain-specific conventions" 标签 :1470 (上文 :1464); 复合词折行项 :1411 (上文 :1405)、:1555 (上文 :1549). 其余上文引用行号已按终态核对 (T-5 :1348, T-6 :1511, eg 表 :1357, 情况表 :1542, baseline 表 :1576, 约定表 :1481, 范围外 dash :1103/:1491/:1520).
- 需主控定 #4 (新增): 变更 #11 把 KB "(e.g., 2001-…)" 改成 PDF "(e.g. 2001-…)" (照录 PDF 标点), 而 T-10 对 PDF 空格笔误是 "KB 保留正确写法"; 两者口径不一, 请 reviewer 定 #11 是否回退为 "e.g.,".
- 入站链接核查命令 (Appendix 小标题删除前实跑): `grep -rn "ch04_general_assumptions.md#" knowledge_base web/src docs releases/v1.4 | grep -i -E "appendix|6133|63557|exposure|microbiology"` → 无输出; `grep -rn "ch04_general_assumptions.md#" knowledge_base | wc -l` → 0.

## attempt 1 delta (主控裁定 1-4 执行, 2026-11-26)
- 终态 md5 `40832488e41bf01dd3dd5b6b54e56b06` (1584 行); git diff vs HEAD +90/−72.
- **裁定 1 (KB 自造粗体标签) 逐处结论**: 8 处标签全部是 "仅为 PDF 原句前的标签" (标签后紧接 PDF 原文, 无 KB 自写句) → 删标签恢复 PDF 原文 (D2 删扩写); 加 D6 的 0 处.

| # | 改后行 | 删除的标签 (base 行) | 其后内容 | PDF 页 |
|---|---|---|---|---|
| D-7 | :572 | `**Example 1:**` 独立行 (:554) | "ae.xpt" 表 (PDF 原有) | 35 |
| D-8 | :588 | `**Example 2:**` (:572) | "For example, a sponsor might…" PDF 原句 | 35 |
| D-9 | :609 | `**Example 3:**` (:593) | "For example, if Abcicin…" PDF 原句 | 35 |
| D-10 | :947 | `**Important restriction on --ENRF:**` (:930) | "Although "COINCIDENT"…" PDF 原句 | 43 |
| D-11 | :949 | `**Caution on mixing collected and derived values:**` (:932) | "Some sponsors may wish…" PDF 原句 | 43 |
| D-12 | :1117 | `**Scenarios where not all 3 uniqueness variables … are needed:**` 独立行 (:1096) | "Not all time points will…" PDF 原句 | 47 |
| D-13 | :1399 | `**Exception — IETEST in IE and TI domains:**` (:1372) | "IETEST values in the…" PDF 原句 | 55 |
| D-14 | :1466 | `**Domain-specific conventions for text > 200 characters:**` 独立行 (:1439) | "The following domains have…" PDF 原句 | 56 |
- 段落拆分 (p43 一段在 KB 为三段, p55 一段在 KB 为两段) 按 S-FND 口径不改.
- **裁定 2 (S-3)**: 采用 "直接删", 不补 D6. 理由: 删掉的行标签 Storage / Split rule / Label 只是对每行内容的概括, 各行单元格的 PDF 原文本身已说明存储 / 拆分 / 标签规则 (信息在表内有承载), 且 §4.5.3.2 正文列表 (:1411 起) 也逐条给出同样规则.
- **裁定 3**: O19 关闭 (Appendix 已 D2 去重为 2 行交叉引用, 见 S-5 / D-6).
- **裁定 4**: "e.g." 照 PDF 保留, 不回退; 需主控定 #4 关闭.
- 上文 "KB 自造标签 (未改, 需主控定 #1)" 段与 "需主控定" 1-4 全部由本 delta 结案.

### 复验 (终态)
- lfwd 未命中 27 (前 30; 少掉 p43:26 / p43:32 / p55:2 三条标签断段项, 余均已定性); rscan 少 8 条标签项, 无新增.
- table_census: OK 19 / UNPARSEABLE 38 / DIFF 1 (T-1) 不变; fp_match ch04 相关翻转仍 +2 (p39_a004 / a016), 回归 0; check_links live docs 42.
