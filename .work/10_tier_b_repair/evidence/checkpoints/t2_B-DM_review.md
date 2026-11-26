# T2 B-DM reviewer

## attempt 1 (审 writer attempt 1+2 终态; oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- 基线: `git diff HEAD -- knowledge_base/domains/DM/` (本批未提交); 只看 DM 文件 (工作树中 RS/TS/model05/model06 为他批)。
- md5 (与 writer attempt 2 一致): examples.md `f7a19d07341d697a93cb67dee84c780f` (453 行); assumptions.md `9c4d2d1d3e976f4754d1ed4ed0549298` (50 行); spec.md 未动 `048374a611824d45f195a6a48f296aa9`。
- 页范围: §5.2 DM = p62-79 (p79 = Ex7 suppdm Row 1/2 叙述 + Note + suppdm.xpt, 其后 5.3 SE), 与 writer 一致; batch pdf_ranges hi=78 漏 p79 (F-4)。全扫按 62-79。
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DM_reviewer/` (p62-79 100dpi, p72/73/76/77 140dpi, p74 图 300dpi 裁剪, scan.py, census/fp 输出)。

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DM_reviewer; P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
echo '[{"file":"knowledge_base/domains/DM/examples.md","src":"ig34","lo":62,"hi":79}]' > $S/manifest.json
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  # exit 1; KB tables 15: OK 11 / DIFF 2 / UNPARSEABLE 2; diffs 2:
  #   :7 Ex1 dm.xpt L14 RACE KB "...ISLANDER" vs PDF "...ISLANDERS" (= T-2)
  #   :435 Ex7 dm.xpt L440 Row KB 4 vs PDF 3 (= T-1)
  # pdf_only 页 62-79 仅 1 张 = p62 co.xpt (§5.1 CO, 非本批); pdf_unparsed 无本批页
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # RESULT: RED (全局 51 条 regress, 页码 p118/174/215/218/254-263/289/311/363/364/370-374/396, 全为他批); grep -E 'p00(6[2-9]|7[0-9])_|DM/' → 0 条 (exit 1)
python3 -I $S/scan.py "$P" 65 67 knowledge_base/domains/DM/assumptions.md   # PDF→KB miss 0; KB→PDF 仅 L5/L9 (p62 内容, 另核 p62 逐字一致)
python3 -I $S/scan.py "$P" 68 79 knowledge_base/domains/DM/examples.md      # 见下 G-TB6
awk -F'|' 'NR>=178&&NR<=194 || NR>=330&&NR<=342 {print NF}' knowledge_base/domains/DM/examples.md | sort | uniq -c   # 30 行全部 16 (=14 列)
grep -n "(same)" knowledge_base/domains/DM/examples.md   # 0 (exit 1)
diff <(git show HEAD:knowledge_base/domains/DM/examples.md | grep -E '^#') <(grep -E '^#' knowledge_base/domains/DM/examples.md)   # 无差异
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### 1. 完整性
| ref | writer action | 复核 |
|---|---|---|
| ig34_p0064_a012 (spec 脚注 2) | DEFERRED_O26 (主控裁定) | 成立: 属 spec.md 脚注, 不在本批; spec.md md5 未变 |
| census :7 Ex1 L11 RFXSTDTC | 2006-01-18 → 2006-01-16 | p68 渲染 Row 3 RFXSTDTC = 2006-01-16, 一致 |
| census :7 Ex1 L12 ROW_SHAPE | 补 AGE/AGEU 空格 | p68 Row 4: BRTHDTC 1941-07-02, AGE 空, AGEU 空, SEX M; KB 8-14 行均 28 段 (=26 列), 一致 |
| census :411→:435 Ex7 Row | PDF_TYPO T-1 | p78 Row 列印 1,2,3,3; 同表连续编号 + Row 4 叙述 → KB 4 成立 |
| unparseable :170→:178 / :310→:330 | TABLE_REBUILT | 逐格人工核见下, 一致 |

### PDF_TYPO 依据核
- T-1: 依据 PDF 自身 (连续编号 + p78 "Row 4: Subject could not self-identify…") — 成立。
- T-2: p68 "…PACIFIC ISLANDERS"; PDF 自身 p72 RACE04 Permissible Values "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER" (p76 同, p70/p75 图同) → KB ISLANDER 成立 (census 该格 OK→DIFF 为预期)。
- T-3: p69 Row 1 "so ACTRMCD is also "AA""; 同页 dm.xpt 表头 ACTARMCD、Row 3 叙述 "ACTARMCD shows" → KB ACTARMCD 成立。
- 非 TYPO 照录 "The arm actual arm variables are null" (p68): KB L24 照录, 处理正确。

### 2. G-TB4 人工逐格 (渲染图 p72-73 / p76-77, 140dpi)
Ex4 CRF Metadata (KB L178-194) ↔ p72-73:
| KB 行 | 内容 | 结果 |
|---|---|---|
| 表头 14 列 | CDASH Variable … Hidden | 一致 |
| RACE01-07 (L180-186) | Order 1-7; Question Text 全句含 "(More than one choice is acceptable.)"; Prompt Race; CRF Completion "Study participants should self-report race, with race being asked about after ethnicity."; Text; RACE; Mapping 空; (RACE); PV AMERICAN INDIAN OR ALASKA NATIVE / ASIAN / BLACK OR AFRICAN AMERICAN / NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER / WHITE / NOT REPORTED / UNKNOWN; Pre/Query 空; checkbox; Hidden 空 | 7 行逐格一致 |
| 分隔行 L187 | "If study participant answered: **AMERICAN INDIAN OR ALASKA NATIVE**" (无 the, 值加粗) | 一致 (p72 跨列行) |
| CRACE01-CRACE04 L188 | 10; 短问句 (无括注); Race; "Select each value that applies if the subject answered "AMERICAN INDIAN OR ALASKA NATIVE". Check all that apply."; Text; SUPPDM.QVAL; "For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value."; (RACEC); "ALASKA NATIVE; AMERICAN INDIAN; CARIBBEAN INDIAN; CENTRAL AMERICAN INDIAN;"; 空; 空; checkbox; 空 | 一致 (跨 p72-73) |
| 分隔行 L189 | "If study participant answered: **ASIAN**" | 一致 |
| CRACE05-CRACE10 L190 | 11; 短问句; "…answered "ASIAN". Check all that apply."; …; PV "ASIAN AMERICAN; ASIAN INDIAN; BANGLADESHI; CHINESE; JAPANESE; KOREAN;"; checkbox; Hidden "CRACE05-CRACE10" | 一致 (Hidden 值为 PDF 原样) |
| 分隔行 L191 | "If study participant answered: **BLACK OR AFRICAN AMERICAN**" | 一致 |
| CRACE11-CRACE17 L192 | 12; …; PV "AFRICAN; AFRICAN AMERICAN; AFRICAN CARIBBEAN; BAHAMIAN; BARBADIAN; BLACK; BLACK CENTRAL AMERICAN;"; Hidden 空 | 一致 |
| 分隔行 L193 | "If study participant answered: **WHITE**" | 一致 |
| CRACE18-CRACE21 L194 | 13; …; PV "ARAB; EUROPEAN; MIDDLE EASTERN; RUSSIAN;"; Hidden 空 | 一致 |

Ex6 CRF Metadata (KB L330-342) ↔ p76-77:
| KB 行 | 内容 | 结果 |
|---|---|---|
| 表头 | 同 Ex4 | 一致 |
| RACE01-07 (L332-338) | Order 3-9; 其余各格同 Ex4 RACE 行 | 7 行逐格一致 (RACE07 跨 p76-77) |
| 分隔行 L339 | "If the study participant answered: **ASIAN**" (有 the) | 一致 (p77) |
| CRACE05-CRACE10 L340 | 11; …; PV 末尾 ";"; Hidden 空 | 一致 (p77 Hidden 空) |
| 分隔行 L341 | "If the study participant answered: **BLACK OR AFRICAN AMERICAN**" | 一致 |
| CRACE11-CRACE17 L342 | 12; …; Hidden 空 | 一致 |

其余 11 表 census OK; 另对 p68-79 渲染图目视复核 Ex1 Row 3/4/6, Ex7 dm/suppdm 全格 — 一致 (除 T-1/T-2)。

### 3. G-TB6 反向溯源 (diff 新增/改动行)
| diff 行 | 出处 | 结论 |
|---|---|---|
| assumptions L5 (合并单段) | p62 Description/Overview 单段 | 逐字一致 |
| assumptions L7 `## DM – Specification` | p62 小标题 "DM – Specification" | 结构行, 签字 |
| assumptions L9 spec 首句 | p62 "dm.xpt, Demographics — Special Purpose. One record per subject, Tabulation." | 逐字一致 |
| assumptions L19 删 "as" | p65 "…to assign subjects to arms described below, ARM…" | 一致 (主控授权) |
| examples L11/12/14 | p68 | 见上 |
| examples L68 ACTARMCD / L70 "either the open drug A" | p69 | T-3 / 逐字 |
| examples L151/153/155/157 | p70-71 图小标题 "If the study participant answered: …" ×4 | 逐字 |
| examples L322/324 | p75 图小标题 ×2 | 逐字 |
| examples L187-194, L339-342 | p72-73 / p76-77 | 见逐格表 |
| examples L245 CETHNICN / WHERE SUPPDM.QNAM = "ETHNICN" | p74 图 (300dpi 裁剪): 灰标 "CETHNICN" + 红标 "SUPPDM.QVAL WHERE SUPPDM.QNAM = "ETHNICN"" | 一致 |
| examples L246 NOTE 节点 | p74 橙框 "VALUE OF "N" IS INDICATIVE OF CHOSEN OPTIONS IN INCREMENTAL SEQUENCE." | 逐字 |
| examples L113/234/290/382 (KB note 图注) | D6 标注行 | 签字 (D6) |
| examples L159-174 / L255 / L326 / L414-423 (KB note 引用块) | D6: KB 自写摘要, 原文不变 + 前缀 | 签字 (D6), 内容核见下 |
| Mermaid 内 `Q -.- NOTE`、空行 | 结构行 | 签字 |

scan.py examples (68-79): KB→PDF 未命中仅 KB note 行、Mermaid 节点行、L68 ACTARMCD (T-3)、L105/L282 "in RED." (PDF 文本层 "red ." 空格噪声) — 无无出处正文。PDF→KB 未命中: 表格串联噪声 (表已逐格核)、"Rows 10-11:Subject" (粘连, KB L48 有)、T-3 原拼写、p79 §5.3 SE (非本批) — 0 叙述缺失。assumptions (65-67) PDF→KB 0 缺。

### D6 逐条确认
| # | KB 位置 | 内容 | 与 PDF 关系 | 结论 |
|---|---|---|---|---|
| 1 | L113 + Mermaid L115-149 (Ex4) | 7 选项 / 4 组子类 (CRACE01-04 AI/AN, 05-10 ASIAN, 11-17 BLACK, 18-21 WHITE), 选项与顺序 | 与 p70-71 图一致 (子类挂在 R1/R2/R3/R5, 与 4 个 "If … answered" 子图对应); 图中 CRF 完成指引/红色映射注释未画 (省略, 不矛盾, CRF Metadata 表承载) | OK |
| 2 | L159-174 (Ex4 摘要) | 7 题 + 4 组子类列表 | 与 p70-72 一致 | OK |
| 3 | L234 + Mermaid L236-253 (Ex5) | ETHNIC 问句、2 选项、子类 5 项挂在 Not Hispanic、CETHNICN 注释、橙框 | 与 p74 图一致 (节点标题 "Chinese Regional Ethnicity Subcategories" 为 KB 标签, 来自本例引言, 不矛盾) | OK |
| 4 | L255 (Ex5 摘要) | ETHNIC + 5 子类 | 一致 | OK |
| 5 | L290 + Mermaid L292-320 (Ex6) | 7 选项 + ASIAN/BLACK 两组子类 | 与 p75 图一致 | OK |
| 6 | L326 (Ex6 摘要) | 删 ", and other categories" 后仅 ASIAN/BLACK | p75 图仅两组子图, p76-77 表仅 CRACE05-10/11-17 → 原句矛盾, D2 删除成立 | OK |
| 7 | L382 + Mermaid L384-412 (Ex7) | 7 选项, RACEOTH/RACEREAS 两附加题 | 与 p78 图一致; "If selected" 边为 KB 推断 (PDF 图为并列题), 与 p79 Row 1/2 叙述相符, 不矛盾 | OK |
| 8 | L414-423 (Ex7 摘要) | 选项 + 附加题 SUPPDM 映射 | 与 p78 红标 "SUPPDM.QVAL WHERE SUPPDM.QNAM = "RACEOTH"/"RACEREAS"" 一致 | OK |

无伪节号; `**CRF Metadata**` / `**CRF Mock Example**` / `**xxx.xpt**` / `# DM — Examples` 为 PDF 标题或导航, 不需 D6。

### 4/5. 位置与副作用
- 内容均在 PDF 所属 Example 下; 无 RELOCATE。
- DM diff 只涉及 examples.md + assumptions.md (授权范围: Description/Overview、spec 首句、主控追加 assumption 4 "as"); 其他 assumptions 条目未动; spec.md 未动。
- examples.md 标题集合与 HEAD 完全一致; assumptions.md 仅新增 `## DM – Specification` (PDF 小标题, CM 先例)。
- 已有正确表行未改坏 (census 11 表 OK)。

### 6. R2 recheck
- batch `t2_recheck` = 0 条。批内发现的 R2 型丢短语 1 处 (Ex3 Row 2 "the open") 已由 writer 补, 核 p69 一致。

### 问题表
| ref | 检查项 | 问题 | 证据 | 严重度 |
|---|---|---|---|---|
| examples L151-157 / L322-324 | 可读性 (非阻断) | 图小标题作为连续裸段落置于 Mermaid 之后, 与 PDF "小标题→子图" 交错版面不同; 文字逐字正确, D6 图注已说明含子图 | p70-71, p75 | LOW |
| examples L403-407 (Ex7 Mermaid) | D6 (非阻断) | "If selected" 条件边与 `(QNAM = …)` 简写为 KB 推断/缩写; 不矛盾, 已在 KB note 下 | p78 | LOW |
| batch json pdf_ranges | 元数据 | hi=78 漏 p79 (F-4, 主控已知) | p79 | LOW |

无 CONDITIONAL 修正项。

### 结论
PASS — G-TB4: 13 表 census OK/预期 PDF_TYPO, 2 张 UNPARSEABLE 表逐格人工核一致 (共 30 数据/分隔行); G-TB6: 新增/改动行均有 PDF 出处或为 D6 标注/结构行, 无出处正文 0; PDF_TYPO T-1..T-3 依据均由 PDF 自身确定; D6 8 处逐条确认; assumptions p62/p65-67 双向 0 差; live docs 42。
