# T2S S-MOD2 review (model/02_observation_classes.md, 源 SDTM v2.0 §3-§3.1 p11-39)

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: CONDITIONAL** — 表格 264 行核心格 (#/Variable/Label/Type/Format/Role+Qualified) 全部与 PDF 一致, 叙述 53 原子全命中, 删除/结构/D2 全签字; 唯一修正项 = 5 行 D6 列说明措辞不完全属实 (F-1, 纯措辞, 不动表格).

- 审查对象: 工作树 md5 `b19bf1ffb56455a4e39b7feb01ead309` (399 行) vs `git show HEAD:knowledge_base/model/02_observation_classes.md` (316 行).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-MOD2_reviewer/` (下称 $S)
- 独立方法 (不用 writer 的 bbox / pdf_tabs.json / 原子 TABLE_ROW): `$S/lay.py` 解析 `work/pdf_pages/sv20_p00NN.txt` (pdftotext -layout) — 每页按表头行各列起始偏移, 逐词按起始列位归列 (容差 3), 行首数字起新行, 跳过表头续行; `$S/cmp.py` 与 KB 全部表行按序配对逐列比. 再加 29 页渲染 (`pdftoppm -f 11 -l 39 -r 75`) 逐页目视.

### 命令与结果 (可复跑, 在 repo 根)
| 命令 | 结果 |
|---|---|
| `python3 -I $S/lay.py $S/lay.json` | 264 行; 每页行数 = pdf_atoms TABLE_ROW 每页计数 (12/12/15/12/13/15/10/5/6/4/7/2/11/8/7/10/14/12/10/9/6/9/7/12/11/7/11/7) |
| `cd $S && python3 -I cmp.py` | 264 行配对 (行数断言通过); 逐列精确一致 243 行; 21 行仅因 layout 折行词序交错 (如 `-- Contact CNTMOD` / `Mode`) 未过逐列比, 字符多重集复核 `multiset diffs 0`, 21 行全部渲染逐格确认一致 (见逐格表 "核法" 列) |
| 同上末段 | `PDF fmt not in KB col` 8 行 (--DUR/--ELTM/--RFTDTC/--EVLINT/MIDSDTC/--STINT/--ENINT/--PDUR) = R1 缺列 (M-4 已裁, 不补) |
| `cd $S && python3 -I usage.py` | Findings 84 新增行 Key Notes 与 PDF Usage Restrictions **逐字相等 84/84**; 其余 16 行为既有行 (OLD) |
| `cd $S && python3 -I notes_all.py` | 264 行: PDF Usage 非空而 KB 格未承载 = 0; KB 格内限制语 (Not in… / XX domain only / Only in…) 不在 PDF Usage = 0 → `issues 0` |
| `$S/narr.py` (KB 非表行 → sv20 p11-39 layout 归一子串) | HIT 37; MISS = H1/Source 行 2 + KB `###` 分组标题 10 + D6 note 6 段 + :31 (跨 p11/p12 页脚断开, 人工核逐字一致) |
| pdf_atoms sv20 p11-39 SENTENCE/HEADING/LIST_ITEM → KB 归一子串 | `HIT 53 MISS 0` |
| `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json` | exit 0, `KB tables: 12; status: {'UNPARSEABLE': 12}; cells compared: 0` GREEN — **census 对 v2.0 表为空比较 (0 格), 不作证据**; 逐格以本文件独立 layout + 渲染为准 |
| `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline … --regress-out $S/fp_regress.jsonl` | RESULT RED (回归全为 ig34 他批页); `grep -c '"sv20' $S/fp_regress.jsonl` = 0. **注意: fp_after 中 sv20 p11-39 原子 0 条 (fp_match 不覆盖本节), 故 "sv20 回归 0" 对本批无证明力**; 以上一行 53/53 原子扫描替代 |
| `git diff HEAD --stat -- knowledge_base/model/` | 仅 `02_observation_classes.md` 1 file, +200/-117 (工作树另有 ch04/ch08/ch10 为他批, 不计) |
| `grep -rnE "02_observation_classes(\.md)?#" knowledge_base docs web/src tools .work/AGENT_GUIDE.md README.md` | 无输出, exit 1 (未截断) → D-7 删 KB 自拟 H3 无入站锚点 |
| `python3 tools/check_links.py 2>&1 \| grep "live docs"` | `broken relative links: 18668 (live docs: 42)` (写本文件后复跑见末行) |

### 页范围复核
p11 首行 `3 Study Subject Data`; p39 = Timing 48 --PDUR 后空白; `work/pdf_pages/sv20_p0040.txt` 第 5 行 `3.2 Special-purpose Domains` → 本批 = p11-39, 与 writer 一致.

### 双向全扫 — 逐页 (reviewer 自计)
| 页 | 非表原子 (类型计数) → KB | 表行 (layout 行数) → KB | KB→PDF | 备注 |
|---|---|---|---|---|
| 11 | H2 S27 L3 全命中 (:5-:31) | — | :5-:31 逐字 | 末句跨页续 p12 |
| 12 | H2 S2 + 表头1; 表题 → :39 | INT 1-12 | 一致 | |
| 13 | — | INT 13-24 | 一致 | C-2 --FTDOSD 新格 = p13 Notes 逐字 |
| 14 | — | INT 25-39 | 一致 | C-3 = Examples + Usage 逐字; C-4 = Definition + Notes 逐字 |
| 15 | H2 + 表头1; 表题 → :93 | INT 40-43, EVT 1-8 | 一致 | 双表头页, 渲染核 |
| 16 | — | EVT 9-21 | 一致 | |
| 17 | — | EVT 22-36 | 一致 | C-5 --ACNDEV: PDF Usage 空 (渲染), 新格 = Definition 逐字 |
| 18 | — | EVT 37-46 | 一致 | |
| 19 | — | EVT 47-51 | 一致 | |
| 20 | H2 + 表头1; 表题 → :162 | EVT 52-56, FND 1 | 一致 | |
| 21-31 | — | FND 2-95 (4/7/2/11/8/7/10/14/12/10/9) | 一致 | 新增行全部渲染逐格; C-6 --SPCUFL = p29 Notes 逐字 |
| 32 | H3 S5 + 表头1 (:269 :271 :273 :279 :281 :283) | FND 96-100, FA 1 | 一致 | FA Notes = PDF Notes 逐字 |
| 33 | H1 表题 → :285 | ID 1-9 | 一致 | |
| 34 | H1 S2 (:308 :310) | ID 10-16 | 一致 | :310 = PDF 两句逐字 |
| 35 | H1 表题 → :312 | TIM 1-12 | 一致 | Format ×3 = "ISO 8601 datetime or interval" |
| 36-39 | — | TIM 13-48 (11/7/11/7) | 一致 | --CHDY Label "Rel" = 渲染 p37 (原子 sv20_p0037_a001 "Relative" 为原子错); --PDUR Label "Planned Duration" = p39; --PTFL/--PDUR Usage 域列表 = p39 |
合计: 非表原子 53 / 命中 53; 表行 264 / 核心格一致 264 (Format 格 3 + Role 括注 264 含 2 处补全); 无出处行 0 (KB 自写行均在 D6 引用块或属导航).

### 主控点名项核对
| 项 | 结论 | 证据 |
|---|---|---|
| Findings 表 100 行 (新增 84) 逐格对渲染 | **一致** | p20-32 渲染逐行; layout 逐列; 逐格表 FND 段 |
| 8 Label 修正 (--ORNRLO/--ORNRHI/--STRESC/--STNRLO/--STNRHI/--STNRC/--NRIND/TIM --PDUR) | 全部 = PDF | p25/26/27/39 渲染 |
| 2 Role 修正 (--ORRESU 4 个 Qualified; --STRESU 8 个) | = PDF Qualified 全列 | p25/p26 |
| 3 Format 修正 (--DTC/--STDTC/--ENDTC) | = "ISO 8601 datetime or interval" | p35 |
| 6 格 D2 (C-1..C-6) | 原格均与 PDF 矛盾或无据 (--REASOC "event" 用于 Interventions; --FTDOSD 与 Notes/Examples 方向不符; --METHOD 把 ROUTE 值当 METHOD 例; --VAMT "Amount of diluent" 与 Notes 相反; --ACNDEV "AE domain only" PDF Usage 空; --SPCUFL "Y" 与 Notes "N" 相反); 新格均 PDF 原文逐字 | p12/13/14/17/29 |
| 另查第 7 个矛盾格 | 无 (notes_all.py 0 + 91 个非逐字格逐格读 `$S/dump.txt`) | — |
| 8 个 "无 PDF 依据" 格 "不矛盾" | **同意 8/8 不矛盾**: --SPEC/--SPCCND 为同类别例值 (PDF 例 SERUM…/CLOUDY); --LNKID/--LNKGRP "RELREC" 为 SDTMIG 用法, 与 p34 Def/Notes 不冲突; --STRF/--ENRF/--STRTPT/--ENRTPT 值列举 v2.0 未列, 与 Def 不冲突. 另有同性质 KB 补充格 (--SEQ "STUDYID, USUBJID, and DOMAIN"、--DTC "Primary date/time…"), 亦不矛盾 | p29/p34/p38/p33/p35 |
| 5 行 D6 列说明措辞属实 | **部分不属实 → F-1** | 见下 |

### 问题表
| ref | 检查项 | 问题 | 严重度 / 置信 | 证据 |
|---|---|---|---|---|
| :41 :95 :164 :287 :316 | D6 措辞属实 | 说 "condenses the PDF … columns", 但该列 8+ 格含 SDTM v2.0 没有的 KB 内容 (BLOOD/TISSUE, HEMOLYZED/LIPEMIC, --STRF 等值列举, RELREC 用法) — D6 本应标出 "非 PDF", 此句反而声称来自 PDF | MEDIUM / HIGH | p29 Examples "SERUM", "PLASMA", "URINE", "DNA", "RNA"; p38 --STRF 无值列举 |
| :164 | D6 措辞可读性 | "Rows without an earlier KB note" 指编辑历史, KB 读者无从判断哪些行 | MEDIUM / HIGH | — |
| :41 :95 :164 :287 :316 | D6 措辞 | "it is not verbatim PDF text" 低估 (约 80 格逐字, 84 新增行全逐字), 与 :164 后半句自相矛盾 | LOW / HIGH | usage.py 84/84 |
| :368 --RFTDTC Notes "ISO 8601" | R2 截断 | PDF Format "ISO 8601 datetime or interval"; 属 R1 缺列 + D6 缩写格, M-4 已裁不改 | LOW / HIGH (仅记录) | p38 |

### CONDITIONAL 修正清单 (writer attempt 2, 只改这 5 行, 表格不动)
- **F-1** 把 5 行 D6 列说明改为下列文字 (逐字替换整行):
  - :41 与 :95 → `> KB note (not in SDTM v2.0): The Key Notes column is KB-written: most cells quote or condense the PDF Definition, Notes, Examples and Usage Restrictions columns, and some cells add KB wording or example values not given in SDTM v2.0.`
  - :164 → `> KB note (not in SDTM v2.0): The Key Notes column is KB-written: most cells quote or condense the PDF Definition, Notes, Examples and Usage Restrictions columns, and some cells add KB wording or example values not given in SDTM v2.0. Cells that state only a domain restriction quote the PDF Usage Restrictions column; a blank cell means the PDF Usage Restrictions column is also blank.`
    (后句已核: 100 行中 KB 空格 52 行, 其 PDF Usage 全空 (52/52); notes_all.py USAGE_MISSING 0)
  - :287 → 同 :41 措辞, 列名改 `Notes`.
  - :316 → `> KB note (not in SDTM v2.0): In the timing sub-tables, the Notes column is KB-written: most cells quote or condense the PDF Format, Definition, Notes, Examples and Usage Restrictions columns, and some cells add KB wording or value lists not given in SDTM v2.0.`
- 改后回 reviewer 复审 delta (只核这 5 行 + md5 + check_links).

### 结构改动 / 删除 / D6 签字
| # | 内容 | 签字 | 依据 |
|---|---|---|---|
| S-1 | FND 4 子表+组名+占位句 → 1 张 100 行表, 行序 = PDF | ✔ | p20-32; 既有 16 行 Key Notes 原样迁入 (脚本核: 旧行 Notes 仅 C-6 变) |
| S-2 | KB 自拟 H3 → `### 3.1.3.1 Findings About Events or Interventions`; FA 加 # | ✔ | p32 标题; 入站锚点 0 |
| S-3 | Timing 7 子表加 Role (全 Timing); 子表 `###` 保留 + D6 拆分说明 | ✔ | p35-39 Role 列全 "Timing" |
| S-4 | 6 个 PDF 表题插表前 (:39 :93 :162 :273 :285 :312) | ✔ | p12/15/20/32/33/35, em dash "—" 与 PDF 同 |
| D-1/D-2/D-3 | `**Structure:** One Record per …` ×3 | ✔ 删 | PDF 表题本身含 "One Record per Constant-dosing Interval or Intervention Episode" / "per Event" / "per Finding" (p12/15/20) → 残留改写 (主控 S-MOD2 口径) |
| D-4 | "Key variable groups include:" | ✔ 删 | KB 占位, 子表已并 |
| D-5 | 4 组名 + 4 子表头 | ✔ 删 | 16 行全迁入; 旧 Label 为 SDTMIG 标签, 已换 v2.0 |
| D-6 | "Additional Findings-specific Variables include … --LNKID, --LNKGRP …" | ✔ 删 | 所列 Findings 变量均已在 100 行表; --LNKID/--LNKGRP 为 §3.1.4 Identifier (p34), 列为 Findings 变量 = 矛盾 |
| D-7 | `### Findings About (Subtype)` | ✔ 删 | 被 PDF H3 取代; 入站锚点 0 |
| D-8 | FA 旧改写 2 句 | ✔ 删 | :271 PDF 句承载; "subtype…record findings about events or interventions" 信息在 :23 PDF 句 |
| D-9 | " (48 variables):" | ✔ 删 | :310 恢复 PDF 原句 + a010 句; 计数留在 :314 D6 |
| D-10..15 | 6 格旧 Key Notes | ✔ | 同 C-1..C-6 |
| D6 :160 | "The Findings class has the largest number of variables…" | ✔ 不矛盾 | 100 > 56 > 43 (本文件三表) |
| D6 :314 | Timing 拆表说明 "48 … one table … row numbers follow the PDF" | ✔ 属实 | p35-39 单表 1-48 |
| D6 :41/:95/:164/:287/:316 | 列说明 | ✘ → F-1 | 见问题表 |
| 导航 (不标 D6) | H1、Source 行、`### Topic and Qualifier Variables (43/56/100 variables)` (计数核实)、Timing 7 个 `###` | ✔ 保留 (M-3) | 规则 6 |

### 逐格表 (264 行; 核心格 = layout 逐列 + 渲染; "核法" 列标明 21 行为渲染确认)
| 表 | KB 行 | # | Variable | PDF 页 | #/Var/Label/Type | Format | Role(+Qualified) | 核法 | Key Notes/Notes 核 |
|---|---|---|---|---|---|---|---|---|---|
| INT | 45 | 1 | --TRT | 12 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 46 | 2 | --MODIFY | 12 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 47 | 3 | --DECOD | 12 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 48 | 4 | --MOOD | 12 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 49 | 5 | --CAT | 12 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 50 | 6 | --SCAT | 12 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 51 | 7 | --PRESP | 12 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 52 | 8 | --OCCUR | 12 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 53 | 9 | --REASOC | 12 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 54 | 10 | --STAT | 12 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 55 | 11 | --REASND | 12 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 56 | 12 | --CNTMOD | 12 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 57 | 13 | --EPCHGI | 13 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 58 | 14 | --INDC | 13 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 59 | 15 | --CLAS | 13 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 60 | 16 | --CLASCD | 13 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 61 | 17 | --DOSE | 13 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 62 | 18 | --DOSTXT | 13 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 63 | 19 | --DOSU | 13 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 64 | 20 | --TDOSD | 13 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 65 | 21 | --FTDOSD | 13 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 66 | 22 | --DOSFRM | 13 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 67 | 23 | --DOSFRQ | 13 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 68 | 24 | --DOSTOT | 13 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 69 | 25 | --DOSRGM | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 70 | 26 | --ROUTE | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 71 | 27 | --LOT | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 72 | 28 | --LOC | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 73 | 29 | --METHOD | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 74 | 30 | --LAT | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 75 | 31 | --DIR | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 76 | 32 | --PORTOT | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 77 | 33 | --FAST | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 78 | 34 | --PSTRG | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 79 | 35 | --PSTRGU | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 80 | 36 | --TRTV | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 81 | 37 | --VAMT | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 82 | 38 | --VAMTU | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 83 | 39 | --ADJ | 14 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 84 | 40 | --RSDISC | 15 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| INT | 85 | 41 | --USCHFL | 15 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 86 | 42 | --RSTIND | 15 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| INT | 87 | 43 | --RSTMOD | 15 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 99 | 1 | --TERM | 15 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 100 | 2 | --MODIFY | 15 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 101 | 3 | --LLT | 15 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 102 | 4 | --LLTCD | 15 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 103 | 5 | --DECOD | 15 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 104 | 6 | --EVDTYP | 15 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 105 | 7 | --PTCD | 15 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 106 | 8 | --HLT | 15 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 107 | 9 | --HLTCD | 16 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 108 | 10 | --HLGT | 16 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 109 | 11 | --HLGTCD | 16 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 110 | 12 | --CAT | 16 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 111 | 13 | --SCAT | 16 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 112 | 14 | --PRESP | 16 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 113 | 15 | --OCCUR | 16 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 114 | 16 | --REASOC | 16 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 115 | 17 | --STAT | 16 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 116 | 18 | --REASND | 16 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 117 | 19 | --BODSYS | 16 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 118 | 20 | --BDSYCD | 16 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 119 | 21 | --SOC | 16 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 120 | 22 | --SOCCD | 17 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 121 | 23 | --CNTMOD | 17 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | PDF 原文子串 |
| EVT | 122 | 24 | --EPCHGI | 17 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 空 (PDF Usage 亦空) |
| EVT | 123 | 25 | --LOC | 17 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 124 | 26 | --LAT | 17 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 125 | 27 | --DIR | 17 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 126 | 28 | --PORTOT | 17 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 127 | 29 | --PARTY | 17 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 128 | 30 | --PRTYID | 17 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 129 | 31 | --SEV | 17 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 130 | 32 | --SER | 17 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 131 | 33 | --ACN | 17 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 132 | 34 | --ACNOTH | 17 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 133 | 35 | --ACNDEV | 17 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 134 | 36 | --REL | 17 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 135 | 37 | --RLDEV | 18 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 136 | 38 | --RELNST | 18 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 137 | 39 | --PATT | 18 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 138 | 40 | --OUT | 18 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 139 | 41 | --SCAN | 18 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 140 | 42 | --SCONG | 18 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 141 | 43 | --SDISAB | 18 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 142 | 44 | --SDTH | 18 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 143 | 45 | --SHOSP | 18 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 144 | 46 | --SLIFE | 18 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 145 | 47 | --SOD | 19 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 146 | 48 | --SMIE | 19 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 147 | 49 | --SINTV | 19 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 148 | 50 | --UNANT | 19 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 149 | 51 | --RLPRT | 19 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 150 | 52 | --RLPRC | 20 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 151 | 53 | --CONTRT | 20 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 152 | 54 | --TOX | 20 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| EVT | 153 | 55 | --TOXGR | 20 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| EVT | 154 | 56 | --USCHFL | 20 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| FND | 168 | 1 | --TESTCD | 20 | 一致 | — | 一致 | layout 逐列 + 渲染 | 空 (PDF Usage 亦空) |
| FND | 169 | 2 | --TEST | 21 | 一致 | — | 一致 | layout 逐列 + 渲染 | 空 (PDF Usage 亦空) |
| FND | 170 | 3 | --SBMRKS | 21 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 171 | 4 | --CELSTA | 21 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 172 | 5 | --CSMRKS | 21 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 新增行: = PDF Usage 逐字 |
| FND | 173 | 6 | --CNTMOD | 22 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 新增行: = PDF Usage 逐字 |
| FND | 174 | 7 | --EPCHGI | 22 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 新增行: = PDF Usage 逐字 |
| FND | 175 | 8 | --TSTCND | 22 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 新增行: = PDF Usage 逐字 |
| FND | 176 | 9 | --CNDAGT | 22 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 177 | 10 | --BDAGNT | 22 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 178 | 11 | --ABCLID | 22 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 179 | 12 | --MRKSTR | 22 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 180 | 13 | --GATE | 23 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 181 | 14 | --GATDEF | 23 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 182 | 15 | --TSTOPO | 24 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 183 | 16 | --MSCBCE | 24 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 新增行: = PDF Usage 逐字 |
| FND | 184 | 17 | --AGENT | 24 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 185 | 18 | --CONC | 24 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 186 | 19 | --CONCU | 24 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 187 | 20 | --MODIFY | 24 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 新增行: = PDF Usage 逐字 |
| FND | 188 | 21 | --TSTDTL | 24 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 189 | 22 | --SPTSTD | 24 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 新增行: = PDF Usage 逐字 |
| FND | 190 | 23 | --CAT | 24 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 191 | 24 | --SCAT | 24 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 192 | 25 | --TSTPNL | 24 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 193 | 26 | --POS | 25 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 194 | 27 | --BODSYS | 25 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 195 | 28 | --ORRES | 25 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| FND | 196 | 29 | --ORRESU | 25 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 空 (PDF Usage 亦空) |
| FND | 197 | 30 | --RESSCL | 25 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 198 | 31 | --RESTYP | 25 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 199 | 32 | --COLSRT | 25 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 200 | 33 | --ORNRLO | 25 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | KB 缩写/补充 (D6 下; 无矛盾) |
| FND | 201 | 34 | --ORNRHI | 26 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| FND | 202 | 35 | --ORREF | 26 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 203 | 36 | --LLOD | 26 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 204 | 37 | --STRESC | 26 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| FND | 205 | 38 | --IMPLBL | 26 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 206 | 39 | --STRESN | 26 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| FND | 207 | 40 | --STRESU | 26 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 空 (PDF Usage 亦空) |
| FND | 208 | 41 | --STNRLO | 27 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | KB 缩写/补充 (D6 下; 无矛盾) |
| FND | 209 | 42 | --STNRHI | 27 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | KB 缩写/补充 (D6 下; 无矛盾) |
| FND | 210 | 43 | --STNRC | 27 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| FND | 211 | 44 | --STREFC | 27 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 212 | 45 | --STREFN | 27 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 213 | 46 | --NRIND | 27 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| FND | 214 | 47 | --RESCAT | 27 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 215 | 48 | --INHERT | 27 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 216 | 49 | --GENREF | 27 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 217 | 50 | --CHROM | 27 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 218 | 51 | --SYM | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 219 | 52 | --SYMTYP | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 220 | 53 | --GENLOC | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 221 | 54 | --GENSR | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 222 | 55 | --SEQID | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 223 | 56 | --PVRID | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 224 | 57 | --COPYID | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 225 | 58 | --CHRON | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 226 | 59 | --DISTR | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 227 | 60 | --RESLOC | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 228 | 61 | --STAT | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 229 | 62 | --REASND | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 230 | 63 | --XFN | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 231 | 64 | --NAM | 28 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 232 | 65 | --LOINC | 29 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 233 | 66 | --SPEC | 29 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| FND | 234 | 67 | --ANTREG | 29 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 235 | 68 | --SPCCND | 29 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| FND | 236 | 69 | --SPCUFL | 29 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| FND | 237 | 70 | --LOC | 29 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 238 | 71 | --LAT | 29 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 239 | 72 | --DIR | 29 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 240 | 73 | --PORTOT | 29 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 241 | 74 | --METHOD | 29 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 新增行: = PDF Usage 逐字 |
| FND | 242 | 75 | --RUNID | 29 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 243 | 76 | --ANMETH | 29 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 244 | 77 | --TMTHSN | 30 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 245 | 78 | --LEAD | 30 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 246 | 79 | --CSTATE | 30 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 247 | 80 | --LOBXFL | 30 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 248 | 81 | --BLFL | 30 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 249 | 82 | --FAST | 30 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 250 | 83 | --DRVFL | 30 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 251 | 84 | --EVAL | 30 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 252 | 85 | --EVALID | 30 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 253 | 86 | --ACPTFL | 30 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 254 | 87 | --TOX | 31 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 255 | 88 | --TOXGR | 31 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 256 | 89 | --SEV | 31 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 257 | 90 | --CLSIG | 31 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 258 | 91 | --DTHREL | 31 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 259 | 92 | --LLOQ | 31 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 新增行: = PDF Usage 逐字 |
| FND | 260 | 93 | --ULOQ | 31 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 新增行: = PDF Usage 逐字 |
| FND | 261 | 94 | --REASPF | 31 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 262 | 95 | --EXCLFL | 31 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 263 | 96 | --REASEX | 32 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 264 | 97 | --USCHFL | 32 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 265 | 98 | --REPNUM | 32 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 新增行: = PDF Usage 逐字 |
| FND | 266 | 99 | --RSTIND | 32 | 一致 | — | 一致 | layout 逐列 + 渲染 | 新增行: = PDF Usage 逐字 |
| FND | 267 | 100 | --RSTMOD | 32 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | 新增行: = PDF Usage 逐字 |
| FA | 277 | 1 | --OBJ | 32 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| ID | 291 | 1 | STUDYID | 33 | 一致 | — | 一致 | layout 逐列 + 渲染 | 空 (PDF Usage 亦空) |
| ID | 292 | 2 | DOMAIN | 33 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| ID | 293 | 3 | USUBJID | 33 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| ID | 294 | 4 | POOLID | 33 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| ID | 295 | 5 | SPDEVID | 33 | 一致 | — | 一致 | layout 逐列 + 渲染 | 空 (PDF Usage 亦空) |
| ID | 296 | 6 | NHOID | 33 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| ID | 297 | 7 | FETUSID | 33 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| ID | 298 | 8 | FOCID | 33 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| ID | 299 | 9 | --SEQ | 33 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| ID | 300 | 10 | --GRPID | 34 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| ID | 301 | 11 | --REFID | 34 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| ID | 302 | 12 | --RECID | 34 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| ID | 303 | 13 | --SPID | 34 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| ID | 304 | 14 | --LNKID | 34 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| ID | 305 | 15 | --LNKGRP | 34 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| ID | 306 | 16 | --BEATNO | 34 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 322 | 1 | VISITNUM | 35 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 323 | 2 | VISIT | 35 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 324 | 3 | VISITDY | 35 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 325 | 4 | TAETORD | 35 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 326 | 5 | EPOCH | 35 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 327 | 6 | RPHASE | 35 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 328 | 7 | RPPLDY | 35 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 329 | 8 | RPPLSTDY | 35 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 330 | 9 | RPPLENDY | 35 | 一致 | — | 一致 | layout 词序交错→渲染逐格确认 | PDF 原文子串 |
| TIM | 336 | 10 | --DTC | 35 | 一致 | 一致 | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 337 | 11 | --STDTC | 35 | 一致 | 一致 | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 338 | 12 | --ENDTC | 35 | 一致 | 一致 | 一致 | layout 逐列 + 渲染 | 空 (PDF Usage 亦空) |
| TIM | 344 | 13 | --DY | 36 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 345 | 14 | --STDY | 36 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 346 | 15 | --ENDY | 36 | 一致 | — | 一致 | layout 逐列 + 渲染 | 空 (PDF Usage 亦空) |
| TIM | 347 | 16 | --NOMDY | 36 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 348 | 17 | --NOMLBL | 36 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 349 | 18 | --RPDY | 36 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 350 | 19 | --RPSTDY | 36 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 351 | 20 | --RPENDY | 36 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 352 | 21 | --XDY | 36 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 353 | 22 | --XSTDY | 36 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 354 | 23 | --XENDY | 36 | 一致 | — | 一致 | layout 逐列 + 渲染 | 空 (PDF Usage 亦空) |
| TIM | 355 | 24 | --CHDY | 37 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 356 | 25 | --CHSTDY | 37 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 357 | 26 | --CHENDY | 37 | 一致 | — | 一致 | layout 逐列 + 渲染 | 空 (PDF Usage 亦空) |
| TIM | 358 | 27 | --DUR | 37 | 一致 | R1 缺列 (PDF: ISO 8601 duration) | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 364 | 28 | --TPT | 37 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 365 | 29 | --TPTNUM | 37 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 366 | 30 | --ELTM | 37 | 一致 | R1 缺列 (PDF: ISO 8601 duration) | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 367 | 31 | --TPTREF | 38 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 368 | 32 | --RFTDTC | 38 | 一致 | R1 缺列 (PDF: ISO 8601 datetime or interval) | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 374 | 33 | --STRF | 38 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 375 | 34 | --ENRF | 38 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 376 | 35 | --EVLINT | 38 | 一致 | R1 缺列 (PDF: ISO 8601 duration or interval) | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 377 | 36 | --EVINTX | 38 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 378 | 37 | --STRTPT | 38 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 379 | 38 | --STTPT | 38 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 380 | 39 | --ENRTPT | 38 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 381 | 40 | --ENTPT | 38 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 387 | 41 | MIDS | 38 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 388 | 42 | RELMIDS | 39 | 一致 | — | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 389 | 43 | MIDSDTC | 39 | 一致 | R1 缺列 (PDF: ISO 8601 datetime or interval) | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 395 | 44 | --STINT | 39 | 一致 | R1 缺列 (PDF: ISO 8601 duration) | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 396 | 45 | --ENINT | 39 | 一致 | R1 缺列 (PDF: ISO 8601 duration) | 一致 | layout 逐列 + 渲染 | KB 缩写/补充 (D6 下; 无矛盾) |
| TIM | 397 | 46 | --DETECT | 39 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 398 | 47 | --PTFL | 39 | 一致 | — | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |
| TIM | 399 | 48 | --PDUR | 39 | 一致 | R1 缺列 (PDF: ISO 8601 duration) | 一致 | layout 逐列 + 渲染 | PDF 原文子串 |

### 其他
- 排版字符: 新插表题用 em dash "—" = PDF; 新插句无引号/省略号.
- 授权范围: kb_files 仅本文件, narrow_files 空; 本批 diff 只在本文件.
- PDF_TYPO: 无. 原子错 sv20_p0037_a001 (--CHDY "Relative") 同意 writer: 渲染 p37 = "Rel".

## attempt 2 复审 (2026-11-26, oh-my-claudecode:code-reviewer / opus; 只审 F-1 delta)

**Verdict: PASS**

- 工作树 md5 `795c8d061c9418a5add217bfae797cf6`, 399 行.
- 逐字: :41 / :95 / :164 / :287 / :316 与 attempt 1 F-1 替换文字逐字相等 (python 字符串全等, 5/5 True).
- 其余行未变: 把这 5 行还原为 attempt 1 原文后, 整文件 md5 = `b19bf1ffb56455a4e39b7feb01ead309` (= attempt 1 审查对象) → delta 只有这 5 行. 还原副本: `$S/attempt1_reconstructed.md`.
- 措辞属实: 新句说明该列为 KB 自写, 多数格引用或缩写 PDF 列, 部分格有 KB 补充 (覆盖 8+ 个无依据格); :164 后句 "blank cell ⇒ PDF Usage 亦空" 复跑仍成立 (FND 空格 52/52 PDF Usage 空; `notes_all.py` → `issues 0`).
- 复跑: `cd $S && python3 -I cmp.py` → 264 行, `multiset diffs 0` (与 attempt 1 相同); `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42`.
