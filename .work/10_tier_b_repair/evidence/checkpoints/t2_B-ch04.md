# T2 B-ch04 writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `6fea5638720e4505be6263ec440953cb8d13fe3b`
- md5 ch04 before `ebd6a616cec349a4cf30c3c0848b6b72` → after `6cdd2ef21e7be82337ef952b72c6aaac`
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_Bch04_writer/` (ch04_before.md, edit.py, census_before/after.json, fp_before/after.jsonl, p25/42/53/54/55/56 渲染)
- 优先级: 派发要求 t2_recheck 4 条按 R2 直接补 → 覆盖 writer prompt "recheck 不改" (同 PCPP 的 D2 先例).
- 真值: 页面文本 + 渲染; 原子 verbatim 不采信 (p56_a005/a006 与页面不符; p43_a034 带截断标记).
- 编辑方式: 一律插入; 仅 3 处原位替换 (KB 句是同一 PDF 句的错述), 见「替换清单」.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | ch04:49 | ig34_p0023_a003 | INSERTED | 句首补 Permissible "should be used ... wherever appropriate" | 23 |
| 2 | ch04:300 | ig34_p0029_a028 | INSERTED | 行末补 "Conventions for representing observations not done ... individual domain models." | 29 |
| 3 | ch04:824 | ig34_p0041_a036 | INSERTED | 括号内补 "e.g., when one knows the start date/time ..." | 41 |
| 4 | ch04:830 | ig34_p0041_a040 | INSERTED | 括号内补 "e.g., where one knows the end date/time ..." | 41 |
| 5 | ch04:850 | ig34_p0042_a007 | INSERTED | Derivation notes 前补 "All study day values are integers..." + 公式块 | 42 |
| 6 | ch04:857 | ig34_p0042_a009 | INSERTED | "This method should be used across all domains." | 42 |
| 7 | ch04:869 | ig34_p0042_a012 | REPLACED | :860 句2-3 (KB 自写 "Findings ... must be used") → PDF a012 原文 | 42 |
| 8 | ch04:869 | ig34_p0042_a013 | REPLACED | 同上, 补 VISITNUM expected 句 | 42 |
| 9 | ch04:871 | ig34_p0042_a014 | INSERTED | 句首补 "Clinical encounters are described by the CDISC visit variables." | 42 |
| 10 | ch04:905 | ig34_p0043_a012 | INSERTED | --STRF 表前新段 (a012+a013) | 43 |
| 11 | ch04:905 | ig34_p0043_a013 (recheck) | INSERTED | 同段 | 43 |
| 12 | ch04:912 | ig34_p0043_a016 | INSERTED | 表后新段: O3 --STRF 限制句 + AFTER unusual 句 | 43 |
| 13 | ch04:914 | ig34_p0043_a018 | INSERTED | "If --ENRF is used, then --ENRF = "AFTER" means ..." | 43 |
| 14 | ch04:916 | ig34_p0043_a022 | INSERTED | :901 行末补 "Note also ... meets the definition of CMSTRF." | 43 |
| 15 | ch04:918 | ig34_p0043_a024 | REPLACED | :903 首句 "deriving ... may blur" → a023+a024 原文 ("in conjunction with ... will blur") | 43 |
| 16-19 | ch04:920 | ig34_p0043_a026/a027/a028/a029 | INSERTED | 新段 "In general, sponsors are cautioned ..." 四句 | 43 |
| 20 | ch04:924 | ig34_p0043_a032 | INSERTED | :907 两句间插 "As a result, 4 new timing variables ..." | 43 |
| 21 | ch04:924 | ig34_p0043_a034 | INSERTED | :907 段末补 "Unlike the variables --STRF and --ENRF ..." (跨页句) | 43 |
| 22 | ch04:924 | ig34_p0044_a001 | INSERTED | 同上句后半 | 44 |
| 23 | ch04:935 | ig34_p0044_a003 (recheck) | INSERTED | --STRTPT 表后补 p44 两情形清单逐字 | 44 |
| 24 | ch04:936 | ig34_p0044_a004 (recheck) | INSERTED | 同上 | 44 |
| 25 | ch04:937 | ig34_p0044_a005 | INSERTED | 同上 | 44 |
| 26 | ch04:939 | ig34_p0044_a006 | INSERTED | 同上 | 44 |
| 27 | ch04:942 | ig34_p0044_a008 (recheck) | INSERTED | 同上 | 44 |
| 28 | ch04:943 | ig34_p0044_a009 | INSERTED | 同上 | 44 |
| 29 | ch04:981 | ig34_p0045_a005 | INSERTED | Ex2 前补 PDF Assumptions 列表 (KB 改写行保留) | 45 |
| 30 | ch04:996 | ig34_p0045_a018 | INSERTED | Ex3 前补 PDF Assumptions 列表 (KB 改写行保留) | 45 |
| 31 | ch04:1363 | ig34_p0055_a026 | REPLACED | suppmh 表头/分隔/数据行加 QEVAL 列 (空) | 55 |
| 32 | ch04:1412 | ig34_p0056_a005 | TABLE_REBUILT | 约定表 4 PDF 列 3 行逐字 (stored as a record / COVAL1 to COVALn / TSVAL1 to TSVALn) | 56 |
| 33 | ch04:1413 | ig34_p0056_a006 | TABLE_REBUILT | Split 行 CO/TS 列补 "to improve readability" (R2) | 56 |

atoms 覆盖: 29/29 + t2_recheck 4/4. 另: O3 (ig34_p0043_a015) = #12; O12 = ch04:888 lb.xpt Week 1 VISITDY/LBDY 空 → 7 / 7.

### 替换清单 (原位替换, reviewer 逐条确认)
| 位置 (改后) | 被替换的 KB 文字 | 原因 |
|---|---|---|
| ch04:869 | "this could be the start date ..." / "In the Findings observation class, ... at least 1 timing variable must be used." | PDF 无此 Findings 断言; 换成 p42 a012+a013 原文 |
| ch04:918 | "Sponsors are cautioned that deriving --STRF and --ENRF ... may blur ..." | 丢 "in conjunction with" 限定, will→may; 换成 a023+a024 原文; 粗体标签保留 |
| ch04:1411-1414 | 约定表 4 个数据列的压缩单元格 | 规则 3 表跟 PDF; "a CO/TS domain record linked to" 与 PDF 相悖. KB "Convention" 标签列保留 (KB_AUTHORED 导航) |
无删除行 (表格单元格替换除外). :916 "Restriction on --STRTPT values" 保留不动 (偏窄, 不算错; 完整情形已在其上方补全).

### census 表处理 (ch04, ig34 p22-59)
| census ref (改前行号) | 处理 | 结果 |
|---|---|---|
| :97 qscg (4 格) | r1/r5 QSLOBXFL ''→Y, VISITDY 7→1 (p25 180dpi 渲染核) | OK |
| :121 qssw (20 格) | QSTESTCD SWLS0n→SWLS010n ×10; QSLOBXFL ''→Y ×9 (r2-5, r7-10; r1/r6 原已 Y); QSTEST "my Life"→"My Life" ×2 | OK |
| :1226 lb Ex1 (5 格) | r5 RBC→WBC, LBORRES 2+→++; r6 LBDTC 02-15→02-01; r7 LBLOBXFL ''→Y, VISITNUM 2→3 (p53 渲染) | OK |
| :1250 eg Ex2 (2 格 Row) | SKIPPED_PDF_TYPO T-1 | DIFF 残留 (已登记) |
| :1321 suppmh 表头 | 加 QEVAL | OK |
| :1336 suppae 表头 | 加 QEVAL | OK |
| pdf_only (p22-59) | 无 | — |
改后 census: OK 19 / DIFF 1 (T-1) / UNPARSEABLE 33 (改前 OK 14 / DIFF 6).

### PDF_TYPO
- T-1 (p54 eg.xpt): PDF 表行号顺序 4,6,5,7 (INTP=6, PRAG=5), 而 PDF Row 5/Row 6 说明是 INTP=5 / PRAG=6; KB 与说明一致, 不改.
- T-2 (p53 lb.xpt r7, 仅登记): 说明写 LBDRVFL="Y", 但 PDF 表无 LBDRVFL 列, Y 落在 LBLOBXFL; KB 按表格单元格填 Y. 请 reviewer 定是否改回空.
- (信息) p53 Ex2 "Row 1" 说明 PDF 写 LBSTRESC/LBSTRESN (应为 EG), KB 写 EG, 不动.

### 新增 atom (R3, 不在 atoms 内)
- p42 a008 公式块 (随 #5); p44 a002 "Allowable values for --STRTPT and --ENRTPT are as follows."; p45 a002-a004/a016/a017 Assumptions 其余条; p43 a023 (随 #15); p56 专门约定域清单 (CO/IE/TS/TI + assumption 号) + "The following table summarizes ..." 插在 ch04:1401-1408 (KB 原压缩行 :1399 保留).

### 触碰过的不可机检表 (reviewer 须对渲染逐格)
- ch04:886-890 lb.xpt (p42; O12 两格)
- ch04:1410-1414 >200 字符约定表 (p56; 无 Row 列)
- --STRF 表 (:907-910) / --STRTPT 表 (:926-931): 未改单元格, 仅在表外插文.

### fp_match (ch04 目标)
- 改前 / 改后全 KB 跑 (`python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out <scratch>/fp_after.jsonl`), 只比 ch04: 回归 0 (hit_target / hit_any); 新命中 44.
- 本批 atoms + recheck + O3 中预期不命中 3 条: p43_a034 (verbatim 带截断标记), p56_a005 / a006 (verbatim 与页面不符; 单元格已按渲染逐字写入).
- 命令: `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest <scratch>/manifest.json --out <scratch>/census_after.json` (manifest = ch04, ig34 22-59).

### 范围外发现 (未改, 请主控定)
1. ch04:848 "consistent with the ICH E3 recommendation for the calculation of study day" — p41-42 无此说法 (KB 自写); PDF 原句为 "relative to a fixed reference point, but creates problems ...".
2. ch04:861 起 Derivation notes 首条 "--DY is calculated as: `--DTC - RFSTDTC` (with no day 0)" 与 "Partial dates should not be used ..." 为 KB 自写.
3. §4.4.5 bullets: "There must be a one-to-one relationship" (PDF "should"); "VISIT: character name ..." 和 "VISITDY ... do not use --DY" 为 KB 自写; 未计划访视 bullet 丢 "as described above" 与 "between visits and values of VISITNUM" 中的 "visits and" (语义变).
4. §4.4.3.2 :828 丢 "or foreword slash"; §4.4.6 只有 2 条 KB 自写 bullet (--XSTDY/--CHSTDY 不在 p43), PDF 段落基本缺失 (这些原子未进 T1 triage, ledger EXACT/EQUIV 不可信, 同 O3 情形).
5. §4.4.7 "Example applications" 3 条 (如 AE --ENTPT = "DATE OF LAST DOSE") 与 Mermaid 图为 KB 自写.
6. trace 行 note 中 "INSERTED 27, REPLACED 3" 计数写错; 正确为 atoms: INSERTED 23 / REPLACED 4 / TABLE_REBUILT 2, recheck INSERTED 4 (trace 为 append-only, 在此更正).

### git diff --stat
```
 knowledge_base/chapters/ch04_general_assumptions.md | 123 +++++++++++++++------
 1 file changed, 87 insertions(+), 36 deletions(-)
```

## attempt 1 续 (主控裁定 1-5 执行, 2026-11-26)

- md5 after: `730cf38ced92da4a75df3ae9ac67fdfa`; diff --stat: 1 file, +92 / −41.

| # | 裁定 | kb 位置 (改后) | action | 摘要 |
|---|---|---|---|---|
| 1 | T-2 | ch04:1276 (lb Ex1 r7) | 不改 | 表格照录 PDF (Y 在 LBLOBXFL); 叙述 "LBDRVFL=Y" 与表矛盾 → **登记 T4 用户裁定项** |
| 2 | ICH E3 | ch04:848 | D2 删扩写 | KB 句 → p42 PDF 原文三句 (fixed reference point ... in those calculations) |
| 3 | §4.4.5 | ch04:875, 879 | REPLACED / INSERTED | "There must be" → "There should be" (**注: PDF p42 原词是 "should", KB 原是 "must"; 裁定文字写反, 按 PDF 取 should**); 补 "visits and"、", as described above" |
| 4 | §4.4.6 | ch04:893 | INSERTED (R3) + D2 删 | 补 p43 整段 (a002-a007); 删 KB 自写 "--XSTDY and --CHSTDY may be used ..." (与 PDF "sponsor may define supplemental qualifier variables" 矛盾, 且非 SDTMIG 变量) |
| 5 | Derivation notes | 原 ch04:861 | D2 删 | 删 "--DY is calculated as: `--DTC - RFSTDTC` (with no day 0)" (公式缺 +1, 与 PDF 公式矛盾) |

### 删除清单 (续)
| file:line (改前) | 被删内容 | 原因 | 保留/替代 |
|---|---|---|---|
| ch04:848 | "...relative to a reference day, and is consistent with the ICH E3 recommendation ..." | p41-42 无, KB 扩写 | 同行换为 PDF 原文 |
| ch04:861 | "--DY is calculated as: `--DTC - RFSTDTC` (with no day 0)" | 与 PDF 公式矛盾 | PDF 公式块 ch04:852-853 |
| ch04:894 (原) | "--XSTDY and --CHSTDY may be used ... (e.g., crossover studies)" | 与 PDF 矛盾 (PDF: 用 SUPPQUAL 变量) | PDF 段 ch04:893 |

### KB_AUTHORED 保留清单 (不矛盾, 待用户通用规则)
| file:line | 概括 |
|---|---|
| ch04:863 | Derivation notes "Partial dates should not be used to derive study day" |
| ch04:873 | VISIT bullet "character name of the visit from the protocol" |
| ch04:874 | VISITDY bullet 括注 "(not the actual study day; do not use --DY)" |
| ch04:895 | §4.4.6 "The reference date/time may use SE dataset element start date/time" (PDF 段内容的压缩) |
| ch04:897 | §4.4.6 "See also: Section 5.3 ..." 导航行 |
| ch04:950-953 | §4.4.7 "Example applications" 3 条 (MH INFORMED CONSENT / CM BEFORE-DURING / AE DATE OF LAST DOSE) |
| ch04:963-973 | Ex1 Mermaid 图 + 斜体图注 (替代 PDF 图) |

### T3 待查 (ledger EXACT/EQUIV 不可信例)
- §4.4.6 原子 ig34_p0043_a002 / a003 / a004 / a005 / a006 / a007: fp_baseline 无 ledger 记录 (verdict None), 未进 T1 triage, 但 KB 改前缺整段. 现已补, 逐字子串命中.
- ig34_p0042_a004 / a005 / a006 (ledger EQUIVALENT/PARTIAL, 改前 fp 不命中) 现已命中.

### 复验 (改后)
- fp_match (只比 ch04): 回归 0; 新命中 48. 预期不命中仍为 3: ig34_p0043_a034 (verbatim 截断标记), ig34_p0056_a005 / a006 (verbatim 与页面不符).
- census: OK 19 / DIFF 1 (T-1) / UNPARSEABLE 33 — 与 attempt 1 相同.
- `python3 tools/check_links.py` → `broken relative links: 18668 (live docs: 42)` = 基线 (docs/PATH_MAP.md), 不升.

## attempt 1 续 2 (D6 标注, 2026-11-26)

- 主控确认: 裁定 3 用 PDF 原词 "should" 正确.
- md5 after: `0df37d796ad96eca4723f5382100dcc1`; diff --stat: 1 file, +104 / −50.
- D6 前缀 `> KB note (not in SDTMIG):` 加到 7 处 (行号 = 改后):

| # | ch04:line | 内容 | 标注方式 |
|---|---|---|---|
| 1 | 863 | Derivation notes "Partial dates should not be used ..." | 列表项内引用块 `- > KB note ...` |
| 2 | 873 | VISIT bullet "character name of the visit from the protocol" | 同上 |
| 3 | 874-875 | VISITDY 括注 "(not the actual study day; do not use --DY)" | 括注移出原 bullet (该 bullet 其余为 PDF 内容的改写), 改为下一行嵌套 KB note "VISITDY is the planned study day, not the actual study day; do not use --DY." — 文字改动, 请 reviewer 确认 |
| 4 | 896 | §4.4.6 "The reference date/time may use SE ..." | 去列表符, 引用块 |
| 5 | 898 | §4.4.6 "See also: Section 5.3 ..." | 引用块 |
| 6 | 951-954 | §4.4.7 "Example applications" 标题 + 3 条 | 整块放进同一引用块 |
| 7 | 964 | Ex1 Mermaid 图 + 斜体图注 (原 963-973) | 图上方单独一行 KB note, 写明是 PDF Figure "Example of --ENRTPT and --ENTPT for Medical History" 的 KB 版 |

- 复验: ch04 fp_match 回归 0 (对改前基线和对续 1 都是 0), 新命中 48, 预期不命中 3 (ig34_p0043_a034 / p0056_a005 / p0056_a006, 原因同前); census OK 19 / DIFF 1 (T-1) / UNPARSEABLE 33 不变; `python3 tools/check_links.py` → live docs 42 = 基线.

## attempt 2 (reviewer CONDITIONAL C1-C10, 主控裁定全部本批做; 2026-11-26)

- attempt 1 已归档: `evidence/failures/t2_B-ch04_attempt_1.{patch,md}`. 在当前工作区基础上改, 不回滚.
- md5 改前 `0df37d796ad96eca4723f5382100dcc1` → 改后 `dca1f77da56395f55ac777f563e539a7`; 相对 base 的 diff --stat: +108 / −60.

### 变更 (行号 = 改后)
| # | ref | ch04:line | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | C1 | 300 | REPLACED (D2) | "Missing values are represented as null. When a test is not performed ... for details." → a027 原文 "Missing values for individual data items should be represented by nulls."; a028 不变 | 29 |
| 2 | C2 | 859 | DELETED (D2) | 删 "**Derivation notes:**" 标签 + 3 条复述 bullet; Partial dates KB note 改为独立一行 | 42 |
| 3 | C3 | 897 后 | DELETED (D2) | 删两行 KB note (SE start date/time 压缩复述; See also 5.3 导航重复) | 43 |
| 4 | C4 | 942 后 | DELETED (D2) | 删 "**Restriction on --STRTPT values:** ..." (复述上方 p44 清单) | 44 |
| 5 | C5 | 1398 后 | DELETED (D2) | 删旧压缩行 "The following domains have specialized conventions: CO (Section 5.1), ..." | 56 |
| 6 | C6 | 916 | REPLACED | 同段 KB 改写的句 1 / 句 3 → PDF 原文 (补 "the variables", "in the case", "(e.g., "Prior", "Ongoing") that are", "and are not limited to the study reference period"); 整段 = p43-44 逐字 | 43-44 |
| 7 | C7 | 838, 840 | REPLACED | "starting with the subject reference start date" → "starting with the reference date as day 1"; 补 "the date portion of", "in"→"from" (= p41 原文) | 41 |
| 8 | C8 | 828 | INSERTED | "solidus or foreword slash [/]" (PDF 拼写 foreword 照录) | 41 |
| 9 | C9 | 945, 949-952 | INSERTED | 新增 `#### Examples of --STRTPT, --STTPT, --ENRTPT, and --ENTPT` (层级同 `#### --STRTPT, ...`) + Ex1 Assumptions 两条; 旧改写行保留 (见 L3) | 44 |
| 10 | C10 | 871 | REPLACED | "There must/should be a **one-to-one relationship** between VISIT and VISITNUM" → p42 原文 "There should be a one-to-one relationship between values of VISIT and VISITNUM." (去粗体, 加句点, a019 才能命中) | 42 |

### 删除清单 (attempt 2)
| file:line (attempt 2 改前) | 被删内容 | 原因 | 保留/替代 |
|---|---|---|---|
| ch04:300 句 1-3 | "Missing values are represented as null. ... See Section 4.5.1.2 for details." | 旧改写, 与 a027/a028 原文重复; 删前后 fp 不丢命中 | ch04:300 PDF 原文 |
| ch04:859-864 (除 863) | "**Derivation notes:**" + 3 条 (公式 ×2, "not suitable for mathematical calculations") | 复述 :848-857 PDF 原文 | ch04:848-857 |
| ch04:896, 898 | KB note ×2 (SE start date/time; See also 5.3) | 压缩重复 / 导航重复 ("may use" 弱于 PDF "will be") | ch04:893 PDF 段 |
| ch04:947 | "**Restriction on --STRTPT values:** ..." | 复述 p44 两情形清单 | ch04:932-942 |
| ch04:1402 | 旧压缩 CO/IE/TS/TI 行 | 与 PDF 清单重复 | ch04:1397-1404 |

### 保留的旧改写行 (L3, 按规则保留)
- Ex1 / Ex2 / Ex3 旧 "CRF contains/includes ... When ... checked:" 行 (ch04:954, 982, 998): 承载 "Example when ... checked:" 一类原子 (如 p44_a016 / p45_a006 / p45_a020), 删了会丢命中, 所以保留.

### T-2 T4 登记 (补充)
- T-2 (p53 lb.xpt r7): 表格照录 PDF (Y 在 LBLOBXFL, VISITNUM 3); 叙述写 "LBDRVFL = "Y"". **reviewer 参考**: visit 1 的 r1-r6 都没有 LBLOBXFL=Y, 只有 visit 3 的 r7 有, 而 r7 的说明是派生记录, 所以 PDF 表头可能把 LBDRVFL 错标成了 LBLOBXFL. PDF 自身无法裁决 → T4 用户裁定.

### 复验 (attempt 2 改后)
- fp_match (`python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out <scratch>/fp_after5.jsonl`), 只比 ch04: 对 base 回归 0; 对 attempt 1 改后状态丢失 0; 对 base 新命中 57 (attempt 2 新增 a027 / p41 a038, a044, a045 / p43 a031, a033 / p44 a014, a015 / p42 a019).
- 预期不命中 3: ig34_p0043_a034 (verbatim 截断标记), ig34_p0056_a005 / a006 (verbatim 与页面不符). p44_a011 (小节标题) 无 ledger 记录, fp 不统计, 已逐字插入.
- census: OK 19 / DIFF 1 (ch04:1291 eg.xpt T-1) / UNPARSEABLE 33.
- `python3 tools/check_links.py` → `broken relative links: 18668 (live docs: 42)` = 基线.

## attempt 2 续 (reviewer 复审 PASS 后采纳可选项, 2026-11-26)

- md5 `dca1f77da56395f55ac777f563e539a7` → `545883c16b8d4f3e161f3176df3c517a`; 相对 base 的 diff --stat: +111 / −63.
- 这样处理后, attempt 2 的 L3「保留旧改写行」不再适用.

### 删除清单 (D2 去重)
| file:line | 被删内容 (旧改写行) | 替代为 PDF 原句 | 信息是否已由 PDF 原文覆盖 |
|---|---|---|---|
| ch04:954 | "CRF contains "Year Started" and a checkbox for "Active"; "Date of Assessment" is also collected. When "Active" is checked:" | `Example when "Active" is checked:` (p44_a016) | 是: 上方 Assumptions 两条 (ch04:951-952) |
| ch04:982 | "CRF includes "Start Date" and "Stop Date", and checkboxes for "Prior" (...) and "Continuing" (...). When both ... checked:" | `Example when both "Prior" and "Continuing" are checked:` (p45_a006) | 是: Assumptions 列表 (ch04:977-980) |
| ch04:998 | "CRF contains "Start Date", "Stop Date", and "Outcome" checkboxes ... No assessment date ... When "Unknown" is checked:" | `Example when "Unknown" is checked:` (p45_a020) | 是: Assumptions 三条 (ch04:993-996) |

### 复验
- fp_match (只比 ch04): 对 base 和对 attempt 2 改后状态都回归 0; p44_a016 / p45_a006 / p45_a020 都从不命中变为命中 ch04; 对 base 新命中 60; 预期不命中 3 不变 (p43_a034 / p56_a005 / p56_a006).
- `python3 tools/check_links.py` → `broken relative links: 18668 (live docs: 42)` = 基线. 改的是叙述行, 不涉及表格, census 不受影响.

## attempt 3 (auditor FAIL F1-F3 + p22-59 双向逐句全扫; 2026-11-26)

- attempt 2 已归档: `evidence/failures/t2_B-ch04_attempt_2.{patch,md}` (patch = git diff 6fea563).
- md5 `545883c16b8d4f3e161f3176df3c517a` → `e11c6093560b572277b2bb5faa033b93`; 相对 base: +240 / −168.
- 扫描方法 (scratch `scan.py` / `scan2.py`): p22-59 的 ig34 原子中 SENTENCE / LIST_ITEM / HEADING / CROSS_REF / NOTE 共 839 条 (去掉截断标记), 用 fp_match.norm 规范化后与 ch04 全文做子串比对. 改前不命中 **172**, 改后 **38**. 不命中的每条都找出 ch04 最相近的一行, 列出缺/替换的词, 再对 `work/pdf_pages` 原文 (必要时看渲染) 定性.
- 反向 (KB→PDF): 改写过的段落整段换成 PDF 原文时, 同段 KB 自写内容逐句判断: 与 PDF 矛盾 → 删; 不矛盾且 PDF 没有 → D6 KB note; 与 PDF 重复 → D2 删.

### 变更 (行号 = 改后)
| # | ch04:line | ref (原子 / 发现) | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | 866 | F1 p42_a015/a016 | INSERTED | "(see Section 7.3.1, Trial Visits)" | 42 |
| 2 | 1365 | F2 p55_a016 | REPLACED | §4.5.3.2 子 bullet 换成 PDF 原文, 补原因从句 | 55 |
| 3 | 1344 | F3 p54_a025 | INSERTED | URL (https://documentation.sas.com/) | 54 |
| 4 | 1359-1366 | p55_a010-a017 | REPLACED | §4.5.3.2 conventions 列表整体换成 PDF 原文 (去 KB 粗体, 补 "which is", "(i.e., …)", "As an example" 等) | 55 |
| 5 | 1368-1371, 1386-1389, 1404-1409 | p55_a021/a032, p56 Ex3 | REPLACED | Example 1/2/3 引导句 → "In this example, the text …" 原文; Ex3 句移到 pr.xpt 表后 (= PDF 顺序) | 55-56 |
| 6 | 1351 | p55_a004 | INSERTED | IETEST 例外段末补 "See Section 6.3.4 …, assumption 3; and Section 7.4.1 …, assumption 5." | 55 |
| 7 | 66 | p23_a019 | REPLACED | "A Findings About" → "The Findings About" | 23 |
| 8 | 95, 136 | p25_a001/a035 | INSERTED / REPLACED | 补 "**QS Domains**"; "**SUPP-- Domains**" → "**SUPPQS Domains**" | 25 |
| 9 | 171 | p26_a021 | INSERTED | "Define-XML document file" | 26 |
| 10 | 198 | p27_a014 | REPLACED | "Sharp/Genari" → "Sharp/Genant" (KB 值错) | 27 |
| 11 | 376 | p31_a025 | INSERTED | "Section 8.4, Relating Non-standard Variable Values to a Parent Domain," | 31 |
| 12 | 552, 573 | p35_a026/a039 | REPLACED | Example 2/3 引导句 → PDF 原文 (KB 粗体标签保留) | 35 |
| 13 | 635 | p37_a005/a006 | REPLACED | "a reference to the controlled terminology … document file … the submitted data" | 37 |
| 14 | 647-653 | p37_a021-a026 | REPLACED | §4.3.5 4 条 bullet 换成 PDF 原文; 删 :645 重复句 ("If a dictionary is multi-axial …" 出现两次, KB 错); KB "one to represent a code and one to represent a text label" → PDF; CMCLAS 两条合并为 PDF 一条 | 37 |
| 15 | 675 | p38_a014/a015 | REPLACED | "In situations such as these"; "(--LOBXFL) variables" | 38 |
| 16 | 730, 732 | p39_a022/a024/a027 | REPLACED | 补 "by ISO 8601"; "date time field" → "date field"; 补 "using ISO 8601 "appropriate right truncations" …" | 39 |
| 17 | 796, 802, 804, 835 | p41_a002/a008/a011/a042 | REPLACED | 补 "within the calendar year"; 补 "As is the case with the date/time representation, … (in addition to the missing time)"; 去 KB 多加的 "ISO 8601"; "duration, "Pn…"," | 41 |
| 18 | 868, 870 | p42_a018/a020 | REPLACED | VISITNUM / VISITDY 两条 bullet → PDF 原文 (KB 前缀 "**VISITNUM**: numeric, …" 删) | 42 |
| 19 | 874 | p42_a021 | REPLACED | "may vary:" → "may vary." (去 KB 粗体) | 42 |
| 20 | 880-882 | p42_a025 | REPLACED | "**Example** (lb.xpt sample rows …):" → PDF 句 + "lb.xpt" | 42 |
| 21 | 907, 909 | p43_a014/a017 | INSERTED | "Allowable values for --STRF / --ENRF are …" | 43 |
| 22 | 911 | p43_a019 | REPLACED | 去掉 "**not appropriate … --ENRF variables**" 的粗体 (粗体让句号前多出空格, 匹配不上) | 43 |
| 23 | 941 | p44_a010 | REPLACED | "**Note:** … codelist but describe …" → PDF 原句 | 44 |
| 24 | 989-1006 | p45_a011/a014/a021/a025 | REPLACED | "=" → "is" (词替换; 这几行只承载各自的原子) | 45 |
| 25 | 1011 | p45_a030/a031/a034 | REPLACED | §4.4.8 "**LB domain specific rules:**" 列表 + "**Collection type …:**" 标签 + 表后 "**Note:**" → PDF 段落原文 (Note 句按 PDF 放在表前) | 45 |
| 26 | 1032 | p46_a009 | INSERTED | "(the date/time)" | 46 |
| 27 | 1034 | p46_a012 | INSERTED | D6 KB note: 变量表 + Mermaid 是 PDF "Figure. Representing Time Points" 的 KB 版 | 46 |
| 28 | 1071 | p46_a034 | REPLACED | 删 KB 加的 "rather than to define time relative to a reference point. In such cases," → "; as such," | 46 |
| 29 | 1084-1089, 1112 | p47_a010-a013 | REPLACED / MOVED | "For trials with many time points …" 移到 4 条列表之后 (= PDF 顺序), 后接 "For instance, in a crossover trial …" + 两个编号选项; 删 KB 标签 "**Crossover trials …:**" 和 "Option 1/2 — …" 说明 → PDF "Option 1" / "Option 2" | 47-48 |
| 30 | 1135-1141 | p48_a021-a036 | INSERTED | §4.4.10 末尾整缺的 4 段 (--TPT/--TPTNUM 一一对应、--ELTM、文本时间点、更严要求) | 48 |
| 31 | 1145-1199 | p48_a039-p51_a007 | REPLACED (整节) | §4.4.11 正文整体换成 PDF p48-51 原文; 小标题按 PDF: "Disease Milestone Naming" (原 KB "… Naming (MIDS)") + 新增 "Disease Milestone Name (MIDS)"; 删 KB MIDS/RELMIDS/MIDSDTC 表 (含与 PDF 矛盾句, 见删除清单) | 48-51 |
| 32 | 1203-1226 | p51_a008-p52_a003 | REPLACED | 标题 → "4.5.1 Original and Standardized Results of Findings and Tests Not Done"; 新增 "#### 4.5.1.1 Original and Standardized Results" + p51-52 原文 6 段; Mermaid 保留, 加 D6 KB note (PDF "Figure. Original to Standardized Results"); 删 KB "3-level framework" 引导句、"Key rules"、"Tests Not Done (§4.5.1.2)" 摘要 (与 PDF 重复); 摘要里 PDF 没有的一句保留为 KB note (:1226) | 51-52 |
| 33 | 1267, 1273 | p52_a033/a034/a038 | REPLACED | "are meant to illustrate … variables, and …", "for more than 1 subject", "from the LBORRES" | 52 |
| 34 | 1443 | p56-57 (QEVAL 例) | REPLACED | "**Example:** An adjudication committee …" → "This example illustrates a case where …" | 57 |
| 35 | 1455 | p57_a008 | INSERTED | "is a record in the domain" | 57 |
| 36 | 1482 | p57 PRESP | REPLACED | "It has controlled terminology" → "The --PRESP variable has controlled terminology" | 57 |
| 37 | 1509 | p58 | REPLACED | 恢复 PDF 分段 ("The following example illustrates …" 独立一段) | 58 |
| 38 | 1520 | p59_a025 | REPLACED | "--LOBXFL, with a core value of expected, was added to contain …" (语序同 PDF) | 59 |

### 删除清单 (attempt 3; D2 / 矛盾删)
| file:line (attempt 3 改前) | 被删内容 | 原因 | 替代 |
|---|---|---|---|
| ch04:645 | 重复句 "If a dictionary is multi-axial … used for the sponsor's analysis." | KB 内重复 (第二遍还截短了) | PDF 原文一遍 (:647) |
| ch04:651 | CMCLAS 单独 bullet | PDF 是同一 bullet 的第二句 | :652 合并 |
| ch04:1008-1010, 1014, 1021 | "**LB domain specific rules:**" + 2 条; "**Collection type …:**" 标签; 表后 "**Note:** …" | PDF 原文的改写 / 重复 | :1011 PDF 段落 |
| ch04:1069 后半 | "rather than to define time relative to a reference point. In such cases," | KB 加的, PDF 没有 | PDF 原句 |
| ch04:1089, 1091, 1114 | "**Crossover trials …:**" 标签 + "Option 1/2 — …" 两行说明 | PDF 编号选项的改写 | :1084-1089 PDF 原文 |
| ch04:1139-1185 (§4.4.11 原正文) | KB 压缩版正文 + MIDS/RELMIDS/MIDSDTC 三行表 + "**Special use of RELMIDS …:**" 标签 | 改写丢句 (TM/SM 交叉引用、MIDS 记录不含 RELMIDS/MIDSDTC 一段、MIDSDTC 无日期一段、迁移病例等); **表中 RELMIDS 一格写 "RELMIDS is represented as ISO 8601 duration", 与 PDF "--ELTM is represented ISO 8601 duration" 相反** | PDF p48-51 原文 (:1145-1199) |
| ch04:1188 (原 3-level 引导) + 1197-1210 | "The SDTM provides a 3-level result framework …"; "**Key rules:**" 5 条; "**Tests Not Done (§4.5.1.2):**" 6 条 | 与 4.5.1.1 / 4.5.1.2 PDF 原文重复 (KB 摘要) | PDF 原文; 其中 PDF 没有的 "--ORRES/--STRESC/--STRESN 在 NOT DONE 时为 null; --ORRESU/--STRESU 也为 null" 保留为 KB note (:1226) |
| ch04:1421 前缀 | "**Example:**" 标签 + 改写句首 | PDF 原句 | :1443 |

### 新增 D6 KB note (本 attempt)
| ch04:line | 内容 |
|---|---|
| 1034 | §4.4.10 变量表 + Mermaid 是 PDF "Figure. Representing Time Points" 的 KB 版 |
| 1213 | §4.5.1.1 Mermaid 是 PDF "Figure. Original to Standardized Results" 的 KB 版 |
| 1226 | NOT DONE 时结果/单位变量为 null (原 KB 摘要句, PDF 无, 不矛盾) |

### 扫描剩余 38 条不命中的定性 (都不改)
| 类别 | 原子 | 说明 |
|---|---|---|
| 原子 verbatim 错 (与 PDF 原页不符) | p40_a024 (PDF "quantity of time"), p41_a010 (PDF "representation"), p56_a001 (ATOM_ERR), p57_a001/a002/a006 (QEVAL 句在 p56, 页面形式与原子不同), p57_a011/a012/a015/a018, p58_a003/a007, p59_a005/a010/a011/a018/a020/a021/a024/a025, p51_a014 (原子含西里尔字母 С) | KB 与 PDF 原页一致 |
| PDF 笔误, KB 保留正确写法 (登记) | p37_a002 (PDF 少 "in"), p49_a008 (PDF "occurrs"), p53_a023 (PDF Ex2 Row 1 写成 LBSTRESC/LBSTRESN), p57_a011 (PDF "result or of") | T-3 ~ T-6, 依据为 PDF 自身上下文 |
| 只差标点/格式 (无信息丢失) | p23_a010 (URL 写法 "at …"), p24_a012 / p32_a011 ("Note:" vs "Note that"), p26_a039 / p32_a013 (冒号/句号), p27_a006, p29_a030 (破折号空格), p39_a004/a014/a016/a019, p54_a008 | 词替换型改写; 都在承载其他原子的长行里, 按补充口径保留 |
| 标题形式 | p22_a001 (KB 文件标题 "SDTMIG v3.4 - Chapter 4: …") | 导航, 不改 |

### 复验 (改后)
- fp_match (`python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out <scratch>/fp_after7.jsonl`), 只比 ch04: 对 base 回归 0 (hit_target / hit_any). 对 attempt 2 状态仅 ig34_p0013_a019 的 hit_any 从 ch04 变成 ch02: 这是并行批改了 ch02 后 fp_match 只记第一个命中文件; 该句仍逐字在 ch04 (grep -c = 1), 不算回归. 对 base 新命中 114 (attempt 3 新增 56).
- 本批 atoms 预期不命中仍为 3: ig34_p0043_a034 / p0056_a005 / p0056_a006.
- census: OK 19 / DIFF 1 (eg.xpt T-1, 现 :1307) / UNPARSEABLE 32 (少 1 张 = 已删的 KB MIDS 表).
- `python3 tools/check_links.py | grep "broken relative"` → `broken relative links: 18668 (live docs: 42)` = 基线.
- 标题: 改了 / 新增了 §4.5.1 标题、"Disease Milestone Naming"、"Disease Milestone Name (MIDS)"、"4.5.1.1"; 仓内没有指向 ch04 锚点的链接 (grep `ch04_general_assumptions.md#` 0 条).

## attempt 4 (reviewer a3 CONDITIONAL 修正清单 1-13 + H1-H4 + 含表格原子的完整双向扫描; 2026-11-26)

- attempt 3 已归档: `evidence/failures/t2_B-ch04_attempt_3.{patch,md}` (patch = git diff 6fea563, 818 行).
- 已读 dispatch notes 末尾新增 3 条: 全扫含表格原子 / 伪节号 / Mermaid.
- md5 `e11c6093560b572277b2bb5faa033b93` → `4ea2579c4a8b7229a433d75e9c44cf92`; 相对 base: +323 / −230.

### 修正清单执行 (行号 = 改后)
| ref | ch04:line | action | 摘要 | PDF 页 |
|---|---|---|---|---|
| H1 | 832 (+835-836) | REPLACED | "14 days 2 hours 57 minutes / P14DT2H57M" → "14 days 7 hours 57 minutes / P14DT7H57M"; L11 "12 1/4" → "12¼", "4 1/2" → "4 ½". 整张时长表 10 行 × 2 列按 p41 120dpi 渲染逐格核过, 其余格一致 | 41 |
| H2 | 223-225 | TABLE_REBUILT | 补 p28 顶部 MK 示例表 (7 列 × 1 行), 按 130dpi 渲染逐格; MKTEST / MKLOC 在 PDF 里折行, 已合并 | 28 |
| H3 | 248-261 | REPLACED | 去掉伪节号 "4.2.1.1-4.2.1.3" 和 3 个小标题; 7 条内容都不与 PDF 矛盾 → 合成一个 D6 KB note 引用块 | 28 |
| H4 | 514-528 | REPLACED | --OBJ 决策树 Mermaid 按 p34 渲染重画: 根 → "Parent record exists?"; Yes → "Topic variable coded?" (Yes --DECOD / No topic variable value); No → "Name of event or intervention coded?" (Yes coded value / No verbatim value); 图上方加 D6 KB note | 34 |
| M1 | 803-813 | MOVED | designator 列表恢复 PDF 顺序 [P] [n] [W]; [Y][M][D][T][H][S] 6 条移到列表后, 作为 D6 KB note 引用块 | 40-41 |
| M2 | 7, 17 | ANNOTATED | Overview 段加 D6 前缀; §4.1.1 末尾追加的 "The SDTM describes …" 从 PDF 段中拆出, 单独一行 D6 | 22 |
| M3 | 663 | REPLACED | 标题恢复 "### 4.3.5 Storing Controlled Terminology for Synonym Qualifier Variables"; 删两个 KB 子标题 (MedDRA / WHODrug), 4 条 bullet 连成 PDF 的一个列表 | 37 |
| M4 | 43-56 | REPLACED / MOVED | 补 PDF Required bullet (Expected 之前); Permissible 段改为 bullet, 3 条下级改为子 bullet (同 PDF 层级); Core 三行表移到列表后并加 D6 KB note (:50) | 23 |
| M5 | 919 | ANNOTATED | --STRF/--ENRF 表加 D6 | 43 |
| M6 | 940 | ANNOTATED | --STRTPT/--ENRTPT 表加 D6, 并写明 AFTER 只在参考时点早于采集/评估日期时有效 (参考时点等于采集日期时无效) | 44 |
| L1 | 554 | DELETED (D2) | "**Example 1:** A rash with locations on the face, neck, and chest:" 去掉复述, 只留 "**Example 1:**" | 35 |
| L2 | 92, 402 | REPLACED | "> **Note:** Submission…" / "> **Note:** QNAM references…" → "Note that submission…" / "Note that QNAM references…" | 24, 32 |
| L3 | checkpoint | 文档 | attempt 3 剩余定性漏列 ig34_p0057_a019 (原子 "SUPP--Datasets" 少空格, KB 内容正确) → 补列, 归 "原子 verbatim 错" | 57 |
| L4 | 190 附近 | 登记 | PDF 笔误 T-7: p26 自然键代码行 "STUDYID, USUBJID, VISTNUM, MKTESTCD", KB 写 VISITNUM. 依据: 同页其余自然键行和 p27 都是 VISITNUM | 26 |
| L5 | 1055, 1234 | REPLACED | D6 措辞补 "with added variable labels/examples not in the figure" / "with added --ORRESU/--STRESU edge and edge labels not in the figure" | 46, 51 |
| L6 | 1284 | MOVED | NOT DONE 的 KB note 从 4.5.1.1 末尾移到 4.5.1.2 末尾 | 52 |
| L7 | 886-889, 893, 895 | MOVED / REPLACED | §4.4.5 planned visits 列表顺序 = PDF (VISITNUM → one-to-one → VISITDY), VISIT KB note 放最后; 去掉 KB 加粗 "same value (e.g., 99)" / "not" | 42 |
| L9 | 231, 380 | REPLACED | 标题 "Variable-naming", "Non-result" (= PDF 大小写) | 28, 31 |
| L10 | 1321 | REPLACED | Example 2 Row 1 "numeric value" → "numeric result" | 53 |
| L12 | 636 | REPLACED | 去掉 §4.3 首段的 "> **Note:**" 标签 (PDF 是正文段) | 36 |
| L13 | 1261-1262 | REPLACED | PDF 编号选项 "1. 2." (原为 bullet) | 52 |
| L8 | Appendix | 不改 | 批外页 (p115/p261), 交主控 | — |

### 全扫中新发现并修复 (reviewer 清单外)
| # | ch04:line | 发现方式 | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| N1 | 773, 774 | 反向逐格扫 + p40 110dpi 渲染 | REPLACED | 缺项日期表 2 格: KB "2003-12-15T--:15" / "2003-12-15T13:--:17" → PDF "2003-12-15T-:15" / "2003-12-15T13:-:17" (PDF 同段: "only a single hyphen is to be used to indicate an omitted component") | 40 |
| N2 | 421-447 | 正向表格原子扫 (p32_a018/a020/a022/a024/a027) | TABLE_REBUILT | §4.2.7.1 三个选项下 KB 用 bullet "CMINDC = …" / "SUPPCM QNAM = …" → 按 PDF 改为小表 (CMINDC 1 列表 ×3; QNAM/QLABEL/QVAL 表 ×2), 值逐格同 p32 | 32 |

### 删除清单 (attempt 4)
| file:line (attempt 4 改前) | 被删内容 | 原因 | 替代 |
|---|---|---|---|
| ch04:241, 247, 252 | 伪节号小标题 "#### 4.2.1.1/4.2.1.2/4.2.1.3 …" | PDF 无此三节 (伪节号) | 内容进 D6 引用块 :248-261 |
| ch04:534 后半 | "A rash with locations on the face, neck, and chest:" | 复述 :532 PDF 原句 | :552 |
| ch04:645, 650 | 子标题 "#### MedDRA Coding (Events)" / "#### WHODrug Coding (Interventions)" | KB 自写, 并把通用条款归到 MedDRA 下 | 无 (PDF 只有一个列表) |
| ch04:643 标题后缀 | "(MedDRA and WHODrug)" | 不同于 PDF 标题 | PDF 标题 |
| ch04:501-507 (Mermaid 旧分支) | 先问 "Topic variable coded?" 的分支 | 与 p34 图逻辑相反 | 按 PDF 重画 |
| ch04:420-421, 425-426, 431 | "- CMINDC = …" / "- SUPPCM QNAM = …" bullet | PDF 是表 | 小表 (N2) |

### 完整双向扫描 (scratch `scan5.py`, 可复跑: `python3 scan5.py fwd` / `python3 scan5.py rev`)
- 正向: p22-59 的 ig34 **全部** 原子 (SENTENCE / LIST_ITEM / HEADING / CROSS_REF / NOTE 用 fp_match.norm 子串比; TABLE_ROW / TABLE_HEADER / CODE_LITERAL / FIGURE 去掉空白、竖线和连字符后比), 对 ch04 全文. 不命中 **101**, 逐条定性:
  | 类别 | 数 | 原子 |
  |---|---|---|
  | 叙述类原子 verbatim 错 (KB 与 PDF 原页/渲染一致) | 20 | p40_a024, p41_a010, p51_a014, p56_a001, p57_a001/a002/a006/a012/a015/a018, p58_a003/a007, p59_a005/a010/a011/a018/a020/a021/a024/a025 |
  | 叙述类 PDF 笔误 (KB 保留正确写法, 登记) | 4 | p37_a002 (T-3), p49_a008 occurrs (T-4), p53_a023 LBSTRESC (T-5), p57_a011 "result or of" (T-6) |
  | 叙述类只差标点/格式 | 12 | p22_a001 (文件标题), p23_a010 (URL 写法), p26_a039 / p32_a013 (冒号), p27_a006, p29_a030 (破折号空格), p39_a004/a014/a016/a019, p54_a008, p57_a019 (L3) |
  | 表格原子 verbatim 错 (census bbox OK 或渲染核过) | 56 | p25_a005/a006/a009/a015/a016/a019/a025-a034 (16; 单元格错位/漏值, qscg/qspi/qssw census OK); p47_a017-a033 + p48_a004-a020 (31; 原子把 VISIT/VISITNUM/TPTREF 填进每一行, PDF 只在块首行, KB 与 PDF 版面一致); p56_a004-a007 (4); p58_a013/a014/a017 (3); p59_a027/a030 (2) |
  | 表格 PDF 笔误 | 1 | p26_a037 VISTNUM (T-7) |
  | 表格 PDF 自相矛盾 (已登记) | 1 | p54_a002 eg.xpt 行号 (T-1) |
  | 图 → KB Mermaid (已加 D6) | 4 | p34_a012, p44_a023, p46_a013, p51_a019 (原子是图描述文字) |
  | CRF 样式块 (KB 用 "[ ]" + "Options" 表头表示勾选项; 选项文字都在) | 3 | p32_a014, p33_a004, p33_a021 |
  (叙述类 36 + 表格类 65 = 101.)
- 反向: ch04 **全文件** 每个非空行 (表格逐格; 正文按句切分; 跳过标题、代码围栏、KB note 行) 去掉空白和连字符后, 与 p22-59 页文本比. 有不命中的行 **148**, 逐类定性:
  - D6 KB note 块内容 / KB Mermaid 代码行 / KB 汇总表 (Core 表、--STRF 表、--STRTPT 表、§4.4.10 变量表): 已标注, 不矛盾.
  - 导航标签 / 数据集名行 ("dm.xpt:", "**Example 1 (lb.xpt)**", "**For the subject:**", "**Scenarios where …**", "**Domain-specific conventions …**", "**Important restriction on --ENRF:**", "**Caution on mixing …**", "**Exception — IETEST …**", 约定表 "Convention" 标签列): 纯导航, 按 D6 范围不加标注.
  - PDF 单元格折行导致整格连续串不在 layout 文本里: qspi (PI01-Pain Intensity / VISUAL ANALOG SCALE), suppqspi "Anchor Text High"/"Anchor Value …", MK 表, 日期表 3 格, suppmh QLABEL, suppae "Possibly related to aspirin use", 基线表各格 — 均对渲染或 bbox 核过, 一致.
  - CRF 样式块的 "[ ]" 选项格: 格式.
  - PDF 笔误更正 (:651 "appears in the", :1321 EGSTRESC, :1176 "occurs", :1500 "result of").
  - 批外: Appendix (:1555 起, p115/p261) = L8, 交主控.
  - 反向扫描没有发现新的未标注 KB 自写解释句 (全部已在 D6 / 导航 / 折行 / 笔误中).

### 不可机检表人工核 (本 attempt 触碰或新增)
- 时长表 (p41, 10 行) ✓; 缺项日期表 (p40, 6 行; N1) ✓; MK 示例表 (p28, 新增) ✓; §4.2.7.1 CMINDC / SUPPCM 小表 ×5 (p32, 新增) ✓; Core 表 / --STRF 表 / --STRTPT 表 (KB 自写, D6, 未改单元格).
- census UNPARSEABLE 32 → 38: +1 MK 表, +5 CMINDC/QNAM 小表 (均无 Row 列); 请主控把这 6 张加入人工核清单.

### 复验 (改后)
- fp_match (`--out <scratch>/fp_after8.jsonl`), 只比 ch04: 对 base / attempt 3 状态的命中变化只有 ig34_p0013_a019 (hit_any 记为 ch02, 原因同前; norm 子串仍在 ch04) → 回归 0. 对 base 新命中 117. 本批 atoms 预期不命中 3 (p43_a034 / p56_a005 / p56_a006).
- census: OK 19 / DIFF 1 (eg.xpt T-1, 现 :1328) / UNPARSEABLE 38; p22-59 范围内 pdf_only 0.
- `python3 tools/check_links.py | grep "broken relative"` → `broken relative links: 18668 (live docs: 42)` = 基线.
