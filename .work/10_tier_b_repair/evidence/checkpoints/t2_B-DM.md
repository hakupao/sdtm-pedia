# T2 B-DM writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `b0932182fdeb0139a0d6b1dae9c3f77321901294` (DM 三文件改前无未提交改动; 基线取 `git show HEAD:<file>`)
- md5: DM/examples.md `c4890c45980c6438df568613c6b72a1d` → `f7a19d07341d697a93cb67dee84c780f` (429 → 453 行); DM/assumptions.md `32bf7281fb9720d45bb9dec96a705d7a` → `ecf4af135f908510be40163bff847179` (48 → 50 行); DM/spec.md 未动 `048374a611824d45f195a6a48f296aa9`
- 白名单: examples.md (batch json) + assumptions.md (主控授权: 仅 Description/Overview + spec 首句 + 节引言 NOTE)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DM_writer/` (*.before.md, 渲染 p64/67-79 110dpi + p68/p74 300dpi 裁剪, edit_all.py, scan.py, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 1 (REAL_GAP) / t2_recheck 0; census DIFF 2 表 (KB 行 11/12/416); pdf_only 0; unparseable 2 (:170 Ex4 / :310 Ex6 CRF Metadata, **均已触碰**, 见下); out_of_scope 0.
- **页范围核 (O20)**: §5.2 DM = p62 (节标题 "5.2 Demographics (DM)" + Description/Overview + spec 首句 + spec 表起) → p63-64 (spec 续 + 脚注 1/2) → p65-67 (Assumptions 1-10) → p68-78 (Examples 1-7) → **p79** (Ex7 Rows 1-2 叙述 + Note + suppdm.xpt; 其后 5.3 SE). batch pdf_ranges 62-78 **少 p79**; 本批按 62-79 全扫 (census manifest hi=79).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | — (目标 spec.md) | ig34_p0064_a012 | SKIPPED_STRUCT (需主控定) | spec 表脚注 2 (FDA race/ethnicity guidance 文献) 属 spec.md, 不在白名单/授权内, 未补; 见 "需主控定" M-1 | 64 |
| 2 | DM/examples.md:11 | census:examples.md:11:3:RFXSTDTC | REPLACED | `2006-01-18` → `2006-01-16` (300dpi 裁剪确认) | 68 |
| 3 | DM/examples.md:12 | census:examples.md:12:4:ROW_SHAPE (+8 CELL) | REPLACED | 行少 1 格 (AGE/AGEU 两空只有 1 空, 后续列整体左移) → 补 1 空格, 26 列对齐 | 68 |
| 4 | DM/examples.md:440 | census:examples.md:416:4:Row | SKIPPED_PDF_TYPO | KB 保留 `4`; PDF Row 列重复 "3" → T-1 | 78 |
| 5 | DM/examples.md:14 | R3 新增 (Ex1 Row 6 RACE) | REPLACED | `…PACIFIC ISLANDERS` → `…PACIFIC ISLANDER` (PDF 拼写错, KB 原照录) → T-2 | 68 |
| 6 | DM/examples.md:68 | R3 新增 (Ex3 Row 1) | REPLACED | `ACTRMCD` → `ACTARMCD` (PDF 拼写错, KB 原照录) → T-3 | 69 |
| 7 | DM/examples.md:70 | R3 新增 (Ex3 Row 2, R2 丢短语) | REPLACED | "either drug A" → "either the open drug A" (PDF 原文; 该行仅此一句叙述) | 69 |
| 8 | DM/examples.md:178-194 | unparseable:examples.md:170 (Ex4 CRF Metadata) | TABLE_REBUILT | 10 处 `(same)` → PDF 原文 (RACE02-07 Question Text 全句 + CRF Completion Instructions; CRACE 4 行为**短**问句, 无 "(More than one…)"); CRACE 4 行 Permissible Values 补末尾 `;`; 补 4 条跨列分隔行 "If study participant answered: **X**" (无 "the") | 72-73 |
| 9 | DM/examples.md:330-342 | unparseable:examples.md:310 (Ex6 CRF Metadata) | TABLE_REBUILT | 同上: 6 行 RACE `(same)` ×2 → 原文, 2 行 CRACE `(same)` → 短问句, 末尾 `;`; 补 2 条分隔行 "If the study participant answered: **X**" (有 "the") | 76-77 |
| 10 | DM/examples.md:151-157 | R3 新增 (Ex4 图内小标题) | INSERTED | 4 行 "If the study participant answered: <X>" (AI/AN, ASIAN, BLACK…, WHITE) 逐字, 原仅 KB 改写 | 70-71 |
| 11 | DM/examples.md:322-324 | R3 新增 (Ex6 图内小标题) | INSERTED | 2 行 "If the study participant answered: ASIAN / BLACK OR AFRICAN AMERICAN" | 75 |
| 12 | DM/examples.md:245-250 | Ex5 Mermaid 与 PDF 图不一致 | REPLACED | `CETHNICT … (QNAM = ETHNICn)` → `CETHNICN → SUPPDM.QVAL WHERE SUPPDM.QNAM = "ETHNICN"` (300dpi 裁剪确认); 补橙框 NOTE 节点 "VALUE OF "N" IS INDICATIVE OF CHOSEN OPTIONS IN INCREMENTAL SEQUENCE." | 74 |
| 13 | DM/examples.md:113 | D6 (Ex4 Mermaid + 原 "> Variable annotation" 自写句) | REPLACED | 加 `> KB note (not in SDTMIG): … KB rendering of the PDF figure "Demographics Sample aCRF…" (Example 4) …`, 原 annotation 句并入 | 70-71 |
| 14 | DM/examples.md:159-174 | D6 (Ex4 KB 自写 CRF 摘要 7 项列表 + 4 段) | REPLACED | 原文不变, 整块改为 `> KB note (not in SDTMIG):` 引用块 | 70-71 |
| 15 | DM/examples.md:234 | D6 (Ex5 Mermaid) | INSERTED | KB note: rendering of PDF figure "CRF Mock Example" (Example 5) | 74 |
| 16 | DM/examples.md:255 | D6 (Ex5 KB 自写摘要句) | REPLACED | 加 `> KB note (not in SDTMIG):` 前缀 | 74 |
| 17 | DM/examples.md:290 | D6 (Ex6 Mermaid + annotation 句) | REPLACED | 同 #13 (Example 6) | 75 |
| 18 | DM/examples.md:326 | D6 + D2 删扩写 (Ex6 KB 自写摘要句) | REPLACED | 加 KB note 前缀; 删 ", and other categories" (PDF Ex6 图只有 ASIAN/BLACK 两组子类, 与 PDF 矛盾) → 删除清单 D-3 | 75 |
| 19 | DM/examples.md:382 | D6 (Ex7 Mermaid) | INSERTED | KB note: rendering of PDF figure "CRF Mock Example" (Example 7) | 78 |
| 20 | DM/examples.md:414-423 | D6 (Ex7 KB 自写选项列表 + Additional fields 句) | REPLACED | 原文不变, 整块改为 KB note 引用块 | 78 |
| 21 | DM/assumptions.md:5 | Description/Overview (主控授权) | REPLACED | 原拆成 2 段 → 合并为 PDF 单段 (文字不变) | 62 |
| 22 | DM/assumptions.md:7-9 | spec 首句 (主控授权) | INSERTED | 新增 `## DM – Specification` + `dm.xpt, Demographics — Special Purpose. One record per subject, Tabulation.` (CM 结构, `pdftotext -raw` p62 逐字) | 62 |

- 覆盖率自查: atoms 1 = #1; census DIFF 表 2 (行 11/12 → #2/#3; 行 416 → #4); unparseable 2 → #8/#9; R3 新增 #5-7, #10-12; D6 #13-20; 授权项 #21-22. 节引言 NOTE: §5.2 无 (p62 节标题后直接 Description/Overview).

### census 表处理

| census ref | 处理 | 改后 census (manifest 62-79) |
|---|---|---|
| examples.md:7 Ex1 dm.xpt (9 CELL + 1 ROW_SHAPE, 行 11/12) | #2 #3 | DIFF 1 = #5 T-2 (RACE ISLANDER vs PDF ISLANDERS), 预期 |
| examples.md:411 (改后 :435) Ex7 dm.xpt (1 CELL, 行 416→440) | #4 PDF_TYPO | DIFF 1 = T-1, 预期 |
| :170→:178 / :310→:330 CRF Metadata | #8 #9 | UNPARSEABLE (census 不可机检) → **reviewer 须对 p72-73 / p76-77 渲染图人工逐格** |
| 其余 11 表 | census OK; Ex2-7 dm/se/suppdm 渲染图人工复核一致 | OK |

census_after: KB tables 15, OK 11, DIFF 2, UNPARSEABLE 2, diffs 2 — 2 条均为本批登记的 PDF_TYPO.

### PDF_TYPO 清单 (依据 = PDF 自身)
- T-1 (p78 Ex7 dm.xpt 第 4 行 Row 列): PDF 印 "3" (与上一行重复). 同表连续编号 + 本例叙述 "Row 4: Subject could not self-identify…" (p78) → KB `4`.
- T-2 (p68 Ex1 dm Row 6 RACE): PDF "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDERS". PDF 自身 Ex4 CRF 图/CRF Metadata RACE04 Permissible Value (p70/p72) 与 Ex6 (p75/p76) 均为 "…PACIFIC ISLANDER" (RACE CT 值) → KB 写 `ISLANDER`. 注: 这使 census 该格由 OK 变 DIFF (预期).
- T-3 (p69 Ex3 Row 1 叙述): PDF "ACTRMCD"; 变量名为 ACTARMCD (同页 dm.xpt 表头、Row 3 叙述 "ACTARMCD shows…"、spec p64) → KB `ACTARMCD`.
- 非 TYPO (照录): p68 Ex2 Row 3 "The arm actual arm variables are null" (疑缺 "and", 但无法由 PDF 自身确定) → KB 照录未动. p74 "…have been provided.suppdm.xpt" 为 PDF 文本层粘连, KB 正常分段.

### 触碰的 unparseable 表 (reviewer 须人工逐格)
- `DM/examples.md:178` (原 :170) Ex4 CRF Metadata, 14 列 × 15 行 (11 数据 + 4 分隔) ↔ p72-73 渲染图.
- `DM/examples.md:330` (原 :310) Ex6 CRF Metadata, 14 列 × 11 行 (9 数据 + 2 分隔) ↔ p76-77 渲染图.
- 分隔行写法: PDF 为整行跨列格 "If [the] study participant answered: **X**" (X 加粗), KB 首格放文字、其余 13 格空 (仿 B-TA "跨列宽格左对齐 + 空格" 惯例). Ex4 无 "the", Ex6 有 "the" — 各照 PDF.
- Ex4 CRACE05-CRACE10 行 Hidden 列 `CRACE05-CRACE10` 为 PDF 原样 (p73), 未动; Ex6 同行 Hidden 空 (p77), 未动.

### 双向全扫 (含表格原子)
- PDF→KB: p68-79 `pdftotext -raw` 规范化分句 vs examples.md 全文 (scan.py): 叙述句除 T-3 外 0 缺 (其余未命中均为表格/图片文本串联噪声与 p79 SE 节); 15 张表对 110dpi 渲染图逐格人工核: Ex1 dm (26 列) 除 #2/#3/T-2 外一致; Ex2 dm/se, Ex3 dm/se, Ex4 dm/suppdm, Ex5 dm/suppdm, Ex6 dm/suppdm, Ex7 dm/suppdm 0 差; CRF Metadata 两表见上. 4 幅 CRF 图对 Mermaid 逐项核: 选项/顺序/子类组/变量标签一致 (Ex5 两处已修 #12).
- p62-67 → assumptions.md: Description/Overview + spec 首句 (已修/补), Assumptions 1-10 (含 4a-c, 6a, 8a-b, 10a-d) 逐句在 KB, 唯一差异见 F-2.
- KB→PDF: examples.md 全文件逐行: 非表/非图/非 KB note 行全部在 PDF (除 `# DM — Examples` 导航标题); KB 自写解释性内容 6 块全部已加 D6 标注 (#13/#14/#16/#17/#18/#20), 无伪节号; `**CRF Metadata**` / `**CRF Mock Example**` / `**xxx.xpt**` 为 PDF 标题/导航.
- p62-64 spec 表 + 脚注 1/2 属 spec.md, 不在本批 (见 M-1 / F-1).

### 新增 atom 清单 (R3)
- #5 ISLANDER (T-2), #6 ACTARMCD (T-3), #7 "the open", #10 Ex4 图内小标题 ×4, #11 Ex6 图内小标题 ×2, #12 Ex5 图 CETHNICN + 橙框注; #8/#9 CRF Metadata `(same)` 还原 / 末尾 `;` / 分隔行.

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:11/12/14/68 旧值 | 同行 | VALUE_DIFF / PDF_TYPO 正确值替换 (#2 #3 #5 #6) | — |
| D-2 | examples.md:70 "either drug A" | 同行 "either the open drug A" | R2 改写丢短语, 行内仅此句 → 恢复原文 (dispatch: 不承载其他原子 → 删旧改写) | — |
| D-3 | examples.md:306 (改后 :326) ", and other categories" | 删 | D2 删扩写: KB 自写句与 PDF 矛盾 (Ex6 图仅 ASIAN / BLACK OR AFRICAN AMERICAN 两组子类, p75) | — |
| D-4 | examples.md:173-182 / :313-320 `(same)` ×18 | PDF 原文 | KB 自写占位缩写, 表格跟 PDF 走 | — |
| D-5 | examples.md:245 `CETHNICT` / `(QNAM = ETHNICn)` | `CETHNICN` / `SUPPDM.QNAM = "ETHNICN"` | Mermaid 与 PDF 图不一致 → 按 PDF 改 | — |
| D-6 | assumptions.md:5-7 段间空行 | 合并单段 | PDF 为单段 (文字未删) | — |

### 需主控定
- **M-1 (ig34_p0064_a012, REAL_GAP)**: DM spec 表脚注 2 ("Food and Drug Administration. Collection of Race and Ethnicity Data in Clinical Trials. …2016. Accessed January 8, 2020. <fda url>"; p64) 全 KB 无. 归属 `DM/spec.md` (spec 表脚注), 不在 kb_files 与 assumptions.md 授权内 → **未补, 停在此项**. 建议: 授权在 `DM/spec.md` 变量表后 (General References 前) 补 p64 脚注 1 + 2 逐字; 或并入 O15/O24/O26 全库 spec 脚注扫描统一口径后补 (该原子届时关闭).

### 范围外发现
- F-1: `DM/spec.md:201` RACE Notes "FDA guidance2" 与 `:210` ETHNIC Notes "FDA guidance1" 均为 PDF 原样角标 (p63: ETHNIC 处 PDF 即印 "guidance1", 与脚注 1 = 星号说明冲突, 疑 PDF 角标错); 脚注本体缺失 → 随 M-1 / O15 一并处理.
- F-2: `DM/assumptions.md:19` 假设 4 "…assign subjects to arms **as** described below…" — PDF p65 为 "…to arms described below…" (KB 多 "as"). assumptions 列表授权外, 未改.
- F-3: `DM/assumptions.md` 假设 6 "MULTIPLE"/"Other, Specify"/"OTHER" 与 10d "subject's": PDF 为弯引号/弯撇号, KB 为直引号 (全库惯例?), 未改, 供 O15/O16 口径参考.
- F-4: batch json `pdf_ranges` hi=78 漏 p79 (Ex7 尾) → O20 同型.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DM_writer
echo '[{"file":"knowledge_base/domains/DM/examples.md","src":"ig34","lo":62,"hi":79}]' > $S/manifest.json
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 11 / DIFF 2 / UNPARSEABLE 2 / diffs 2 (=T-1, T-2)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p00(6[2-9]|7[0-9])_|DM/' $S/fp_regress.jsonl   # 0 (全量 51 条 regress 均为他批 §6.4.2 等)
python3 -I $S/scan.py "source/cdisc/SDTMIG v3.4 (no header footer).pdf" 68 79 knowledge_base/domains/DM/examples.md     # 叙述双向
python3 -I $S/scan.py "source/cdisc/SDTMIG v3.4 (no header footer).pdf" 62 67 knowledge_base/domains/DM/assumptions.md  # 仅 F-2
for p in 68 69 70 71 72 73 74 75 76 77 78 79; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
awk -F'|' '/^\| (RACE|CRACE|If )/{print NF}' knowledge_base/domains/DM/examples.md | sort | uniq -c   # 全部 16 (=14 列)
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 knowledge_base/domains/DM/assumptions.md |   6 +-
 knowledge_base/domains/DM/examples.md    | 124 ++++++++++++++++++-------------
 2 files changed, 78 insertions(+), 52 deletions(-)
```

## attempt 2 (主控裁定后, 2026-11-26T04:43:27Z)

- M-1 (ig34_p0064_a012): **DEFERRED_O26** — 主控裁定不在本批补, 并入 O15/O26 spec 脚注全域扫描; attempt 1 的 SKIPPED_STRUCT 改记 DEFERRED_O26.
- F-2 (主控追加授权): `DM/assumptions.md:19` 假设 4 删去多出的 "as" ("…assign subjects to arms described below, …"), 按 p65 逐字; 只改这一处. 复核: `scan.py … 62 67 DM/assumptions.md` PDF→KB / KB→PDF 未命中仅剩标题行 (0 内容差).
- F-4: 主控已知.
- 新 md5: DM/assumptions.md `9c4d2d1d3e976f4754d1ed4ed0549298`; examples.md 未动 `f7a19d07341d697a93cb67dee84c780f`.
- 删除清单追加: D-7 `assumptions.md:19` 一词 "as" — KB 多出 PDF 无的词, 恢复 PDF 原文 (主控授权).
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → 42.
- git diff --stat: assumptions.md 8 +- / examples.md 124; 2 files, 79 insertions(+), 53 deletions(-).
