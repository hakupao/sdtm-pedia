# T2 B-DD writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `d84a22555eb38ab1a7ccdb7645425fec8a031aa5` (DD 目录改前 `git diff --quiet -- knowledge_base/domains/DD` = clean)
- md5: DD/assumptions.md `59a15c0f791f07cf40258621f35151d8` → `05a986aeea6f94a1c1febbf7077a37aa` (11 → 23 行); DD/examples.md 未动 `e890adecdf01c175491af14e6cfcf1aa`; DD/spec.md 未动 `8f80011d1f2fa3ca237a912feb0ad11e`
- 白名单: examples.md (batch json, 本批无需改) + assumptions.md (主控通用授权: Description/Overview + spec 首句, 逐字; 结构照 CV/RE/CM 先例)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DD_writer/` (assumptions.before.md, examples.before.md, p183-185 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl, scan.py)
- 本批 atoms 2 (REAL_GAP) / t2_recheck 0; census DIFF 0; pdf_only 0; unparseable 0; out_of_scope 0.
- 页范围核 (O20): DD 节 = p183 顶 "6.3.2 Death Details (DD)" (无节引言 NOTE; 直接 Description/Overview + Specification 首句 + spec 表 + 脚注) → p184 (Assumptions 1-5 + Examples Ex1 + Ex2 ae.xpt 及其后句) → p185 (Ex2 dd/ds/relrec + 叙述; 其后 6.3.3 EG). p182 末无 DD 内容. batch lo/hi = 183-185 **完整覆盖** (`pdf_pages` 仅 183).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | DD/assumptions.md:3-5 | ig34_p0183_a003 | INSERTED | 新增 `## DD – Description/Overview` + 首句 "A findings domain that contains the diagnosis of the cause of death…" 逐字 | 183 |
| 2 | DD/assumptions.md:7 | ig34_p0183_a004 | INSERTED | Description 第 2 段 4 句逐字; PDF 粗体 "not" ×2 写成 `**not**` | 183 |
| 3 | DD/assumptions.md:9-11 | spec 首句 (主控授权; fp ig34_p0183_a006) | INSERTED | 新增 `## DD – Specification` + "dd.xpt, Death Details — Findings. One record per finding per subject, Tabulation." 逐字 | 183 |
| 4 | DD/assumptions.md:13 | PDF 节标题 "DD – Assumptions" (R3, 导航) | INSERTED | 新增 `## DD – Assumptions` (PDF p184 原标题; 与 CV/RE/CM 先例同构), 原列表 1-5 未动 | 184 |

- 覆盖率自查: atoms 2 = #1-2; 授权项 #3; 结构标题 #4. 未删除任何行.
- 逐字核 (cmp IDENTICAL ×3): p183 layout 第 3 行 ↔ KB:5; 第 4-7 行合并 ↔ KB:7 (去 `**`); 第 9 行 ↔ KB:11. 折行均为整词边界, 无连字符.

### census 表处理
- census 0 DIFF. 改后 `table_census.py` (manifest = examples.md + assumptions.md, p183-185): KB 表 5, OK 5, diffs 0.
- 5 张例表 (Ex1 dd / Ex2 ae, dd, ds, relrec) 对 110dpi 渲染图 p184/p185 逐格人工核: 表头/列序/列数/Row 列/全部单元格一致 (relrec RELTYPE 空列一致).

### fp 核
- fp_match 改后: ig34_p0183_a003/a004/a006 hit_target None → DD/assumptions.md. 其余 DD 节 hit_target 变化仅 p184_a013 / p185_a001 (`dd.xpt` CODE_LITERAL, 首命中由 examples.md 变 assumptions.md, 仍在 target 内).
- 仍 hit_target=None: p183_a007-a020 (spec 表 + 脚注, 属 spec.md, 范围外 → O15); p184_a005 (assumption 4, 见 F-1).
- regress 输出 2 条 (ig34_p0363_a016/a017, §6.4.2) 为他批工作树改动; `grep -E 'p018[3-5]|DD/' fp_regress.jsonl` = 0.

### 双向全扫 (含表格原子)
- PDF→KB: p183-185 (截至 6.3.3) 叙述逐句 (scan.py 规范化: 弯引号→ASCII, 去 `**`, 去空白) 全部在 assumptions.md/examples.md; 未命中仅 spec 表/脚注 (spec.md)、页眉页脚、与标题/表粘连的切分片段 (人工核其句均在 KB)、assumption 4 (F-1).
- KB→PDF: 两文件每行均有 PDF 对应; 未命中仅 `# DD — Assumptions` / `# DD — Examples` (导航) 与 assumption 4 (F-1). 无 KB 自写解释性内容 (D6 无), 无伪节号.

### 新增 atom 清单 (R3)
- #4 `## DD – Assumptions` 节标题 (导航).

### PDF_TYPO 清单
- 无.

### 删除清单
- 无.

### 范围外发现
- F-1: `DD/assumptions.md:19` (assumption 4) "DD codeable" ↔ PDF p184 "DD codetable" (KB 拼写错, ig34_p0184_a005 hit None). 按授权 "assumptions 列表本身若有错记入范围外, 不改". 建议主控授权改一词.
- F-2: examples.md:5 (Ex1) "subject's" PDF 为弯撇号 (p185 两处为直撇号); 与 DM F-3 同属全库直引号惯例, 未改.
- F-3: spec.md (p183 spec 表 + 脚注, fp a007-a020 无命中) 不在白名单 → 归 O15 spec 扫描.

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DD_writer
P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
pdftotext -f 183 -l 183 -layout "$P" - | sed -n 4,7p | sed 's/^ *//;s/ *$//' | tr '\n' ' ' | sed 's/ $//' > $S/a.txt; sed -n 7p knowledge_base/domains/DD/assumptions.md | sed 's/\*\*//g' | tr -d '\n' > $S/b.txt; cmp $S/a.txt $S/b.txt
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 5 / diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p018[3-5]|DD/' $S/fp_regress.jsonl   # 0
python3 -I $S/scan.py   # KB? 仅 2 标题 + codeable; PDF? 仅 spec/页脚/粘连片段 + codetable
for p in 183 184 185; do pdftoppm -f $p -l $p -r 110 -png "$P" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### git diff --stat
```
 knowledge_base/domains/DD/assumptions.md | 12 ++++++++++++
 1 file changed, 12 insertions(+)
```

## attempt 2 (F-1 主控授权, 2026-11-26)
- 变更: `DD/assumptions.md:21` (assumption 4; attempt 1 F-1 写的 ":19" 是插入前的旧行号, 改后应为 :21) "DD codeable" → "DD codetable" (REPLACED, p184). 其余行未动.
- 未按 PDF_TYPO 处理的理由: "codetable" 是 CDISC 的正式术语 (CT 网页发布的 codetable 文件, `grep -rn codetable knowledge_base/domains/*/assumptions.md` 共 8 行 (含 DD 本处)), 不是 PDF 笔误; KB 的 "codeable" 才是错的.
- 逐字核: p184 layout 中 assumption 4 两行合并后去编号, 与 KB:21 去编号后比对 → cmp IDENTICAL.
- md5 `05a986aeea6f94a1c1febbf7077a37aa` → `78b98f31dca3afc892e57033dc255b01`; diff --stat: assumptions.md 13 insertions(+), 1 deletion(-) (删除 = 旧值替换).
- 删除清单: D-1 assumptions.md:21 旧词 "codeable" (VALUE_DIFF 旧值替换).
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → 42. F-1 状态: **已处理**.
