# T2 B-DA reviewer

## attempt 1 (oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base = HEAD (d84a225); 本批文件: DA/examples.md (md5 e3bcd39cb400979b0ba74898d62eb6e0), DA/assumptions.md (79a8536ae14f5de89c06affcec87e3d2); DA/spec.md 未动 (60cf1eb9916f9f413615291751f17dcf, = writer 报告)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DA_reviewer/`
- 页范围: DA 节 p180 (6.3.1 标题起) - p182; p183 起 DD. 与 writer 一致. p180 顶部 §6.3 章引言 2 句 (a0001/a0002) 不属本批 (O39).

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DA_reviewer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-DA.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  # KB tables: 3; status: {'OK': 3}; diffs: 0 (exit 1 仅因全局 PDF_ONLY 336, 无落在 p180-182 的)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # RESULT: RED; regress 51 条全部为他批页 (p118/174/215/218/254-263/289/311/363-374/396), grep -cE 'p018[0-2]|DA/' = 0
  # p180-182: EXACT 30 / INTENTIONAL_EXCLUDE 30 / EQUIVALENT 3 / PARTIAL 4
pdftoppm -f 180 -l 182 -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p
pdftotext -f 180 -l 182 -layout / -raw  (独立方法核表与逐句)
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```
- PARTIAL 4 (a012/a018 'Example 2/3', a014/a023 CODE_LITERAL 'da.xpt'): 短串 matcher 噪声, KB examples.md:18/29/22/39 逐字存在. EQUIVALENT a0005 (Description) 现 KB assumptions.md:5 逐字.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无阻断问题 | — |
| examples.md:1 / assumptions.md:1 | G-TB6 结构 (LOW, 非本批改动) | 文件标题用 em dash `—`, PDF 节内小标题为 en dash "DA – Examples"; 全库文件标题惯例, 未改动, 不计 | p182 "DA – Examples" |

### G-TB4 人工逐格 (p182 110dpi 渲染图 + pdftotext -layout, 独立于 census bbox)
| 表 | 表头/列序 | Row 1 | Row 2 | Row 3 | Row 4 | Row 5 | Row 6 |
|---|---|---|---|---|---|---|---|
| Ex1 da.xpt (19 列) | 一致 | 一致 | 一致 | 一致 | 一致 | 一致 (DAREFID/DASPID/DASCAT 空; DAORRES 10, DAORRESU TABLET, DASTRESC 10, DASTRESN 10, DASTRESU TABLET, VISITNUM 1, EPOCH Study Med Period 1, DADTC 2004-06-15) | 一致 (同 Row 5 但 RETAMT/Returned Amount, VISITNUM 2, DADTC 2004-07-15) |
| Ex2 da.xpt (17 列) | 一致 | 一致 | 一致 | — | — | — | — |
| Ex3 da.xpt (17 列) | 一致 | 一致 | 一致 | 一致 | 一致 | 一致 | 一致 (PDF Row 5/6 间空白为版面) |

### G-TB6 反向溯源 (diff 每行)
| diff 行 | 出处 |
|---|---|
| assumptions.md:3 `## DA – Description/Overview` | 结构行 = p180 原小标题 (en dash 一致), 签字 |
| assumptions.md:5 Description 句 | p180 逐字 |
| assumptions.md:7 `## DA – Specification` | 结构行 = p180 原小标题, 签字 |
| assumptions.md:9 spec 首句 | p180 逐字 (含 em dash, 与 PDF 字符一致) |
| assumptions.md:11 `## DA – Assumptions` | 结构行 = p181 PDF 原标题 "DA – Assumptions" (U+2013 一致), 签字 |
| examples.md:15/16 Row 5/6 | p182 渲染图逐格一致 (见上) |
| examples.md:20 "the purpose of the accountability tracking" | p182 原词, 逐字 |
新增行 13 / 无出处 0. 位置: Description→Specification→Assumptions 顺序同 PDF 与 CM 先例.

### 双向全扫 p180-182 (含表格原子)
- KB→PDF: assumptions.md / examples.md 全部非表行规范化后逐行在 PDF 原文命中 (仅 2 个文件主标题 `# DA — …` 为导航); 表格行见逐格表. 无 KB 自写解释内容 (D6 无), 无伪节号.
- PDF→KB: p180 Description / spec 首句 / 3 个小标题 已在; p181 Assumptions 1, 1a-c, 2-4 逐句命中 (含 URL; "--\nSTNRC" 折行); p182 Ex1-3 引言、Rows 1-2/3-4/5-6、3 张表 全在. p180-181 spec 表 + 脚注 → spec.md (白名单外, F-2/O15). p180 §6.3 章引言 → O39 (主控已排除).
- 授权范围: assumptions 列表 1-4 未改; 无白名单外 DA 文件改动. 整个 KB diff 中其他文件 (CE/DD/DM/FT/TS/model05/06) 属他批.

### R2 recheck
- t2_recheck 为空 (0 条).

### 完整性
- atoms 0; census 8 CELL 全部处理 (#1-8), 改后 OK; R3 新增 1 (#9) 成立; PDF_TYPO 无; unparseable 无.
