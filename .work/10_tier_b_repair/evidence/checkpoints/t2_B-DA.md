# T2 B-DA writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `d84a22555eb38ab1a7ccdb7645425fec8a031aa5` (DA 文件工作树改前无未提交改动)
- md5: DA/examples.md `ba48d4b2b1f153f4edc33f0ef311be46` → `e3bcd39cb400979b0ba74898d62eb6e0` (48 行不变); DA/assumptions.md `f92867d403777b41b7371e433e966543` → `79a8536ae14f5de89c06affcec87e3d2` (12 → 22 行); DA/spec.md 未动 `60cf1eb9916f9f413615291751f17dcf`
- 白名单: examples.md (batch json) + assumptions.md (主控授权: 仅 Description/Overview + spec 首句 + 节引言 NOTE, CM/BE 先例, 逐字)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DA_writer/` (examples.before.md, assumptions.before.md, p182 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 0 / t2_recheck 0; census DIFF 1 表 (8 CELL, KB 行 15/16); pdf_only 0; unparseable 0; out_of_scope 0.
- 页范围核 (O20): p180 顶部为 "6.3 Models for Findings Domains" 章引言 (2 句, 属 §6.3 而非 DA) → "6.3.1 Product Accountability (DA)" 标题 → Description/Overview → Specification 首句 + spec 表 → p181 (spec 续 + 脚注 + Assumptions 1-4) → p182 (Examples Ex1-3; 无 References). p183 起 6.3.2 DD. DA 节 = p180-182, batch lo/hi 180-182 **完整覆盖**. 6.3.1 标题与 Description 之间**无**节引言 NOTE.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | DA/examples.md:15 | census:examples.md:15:5:DAORRES | REPLACED | 空 → `10` (Row 5 自 DAORRES 起整体左移一格, 按渲染图复位) | 182 |
| 2 | DA/examples.md:15 | census:examples.md:15:5:DAORRESU | REPLACED | `10` → `TABLET` | 182 |
| 3 | DA/examples.md:15 | census:examples.md:15:5:DASTRESC | REPLACED | `TABLET` → `10` | 182 |
| 4 | DA/examples.md:15 | census:examples.md:15:5:EPOCH | REPLACED | 空 → `Study Med Period 1` | 182 |
| 5 | DA/examples.md:16 | census:examples.md:16:6:DAORRES | REPLACED | 空 → `10` | 182 |
| 6 | DA/examples.md:16 | census:examples.md:16:6:DAORRESU | REPLACED | `10` → `TABLET` | 182 |
| 7 | DA/examples.md:16 | census:examples.md:16:6:DASTRESC | REPLACED | `TABLET` → `10` | 182 |
| 8 | DA/examples.md:16 | census:examples.md:16:6:EPOCH | REPLACED | 空 → `Study Med Period 1` | 182 |
| 9 | DA/examples.md:20 | R3 新增 (词级改写) | REPLACED | "the purpose of accountability tracking" → "the purpose of **the** accountability tracking" (PDF 原词; 该行无其他原子冲突) | 182 |
| 10 | DA/assumptions.md:3-5 | p180 Description/Overview (主控授权) | INSERTED | 新增 `## DA – Description/Overview` + p180 原句逐字 | 180 |
| 11 | DA/assumptions.md:7-9 | p180 spec 首句 (主控授权) | INSERTED | 新增 `## DA – Specification` + `da.xpt, Product Accountability — Findings. One record per …, Tabulation.` 逐字 | 180 |
| 12 | DA/assumptions.md:11 | 结构 (CM/BE 先例) | INSERTED | 新增 `## DA – Assumptions` 小标题 (PDF 原标题), 原列表 1-4 未动 | 181 |

- 覆盖率自查: atoms 0; census 8 格 = #1-8 (全部处理, 无 PDF_TYPO); R3 新增 1 (#9); 授权项 3 (#10-12).
- Row 5/6 其余格 (DAREFID/DASPID/DASCAT 空, DASTRESN 10, DASTRESU TABLET, VISITNUM 1/2, DADTC) 改前即与渲染图一致.

### census 表处理

| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:9 Ex1 da.xpt (8 CELL) | #1-8 | OK |
| examples.md:24 Ex2 / :41 Ex3 | census OK; 渲染图人工逐格复核一致 (Ex3 Row 5/6 PDF 间空行为版面, 非数据) | OK |

census_after: KB tables 3, OK 3, diffs 0.

### PDF_TYPO 清单
- 无.

### fp 回归
- fp_match 改后 p180-182 原子: EXACT 30 / INTENTIONAL_EXCLUDE 30 / EQUIVALENT 3 / PARTIAL 4; 与 baseline verdict 逐条比 **0 变化**.
- PARTIAL 4 = ig34_p0182_a012/a018 (prefilter FP_HIT_SHORT, 命中 `## Example 2`/`## Example 3` 标题) 与 a014/a023 (CODE_LITERAL `da.xpt`, 命中 `**da.xpt**`): 均为短串 matcher 噪声, 人工核 KB 逐字存在.
- 全量 regress 2 条 (ig34_p0363_a016/a017, §6.4.2) — 他批工作树改动, 非本批; `grep -E 'p018[0-2]|DA/' fp_regress.jsonl` = 0.

### 双向全扫 (含表格原子)
- PDF→KB: p180 Description/spec 首句 (已补, #10-11); p180-181 spec 表 → spec.md (白名单外, 未扫改, 见 F-2); p181 Assumptions 1, 1a-c, 2-4 逐句在 assumptions.md (PDF "--\nSTNRC" 为折行); p182 Ex1-3 引言、Rows 1-2/3-4/5-6 说明、3 个 `da.xpt` 标题 逐句规范化比对 0 缺 (#9 修后); 3 张表对 110dpi 渲染图逐格人工核: 表头/列序/列数/Row 列一致, 改后 0 差.
- KB→PDF: examples.md / assumptions.md 全文件每行均有 PDF 对应; 无 KB 自写解释性内容 (D6 无), 无伪节号; `# DA — Examples`/`## Example N`/`**da.xpt**`/`**Rows x-y:**` 为导航/格式.

### 新增 atom 清单 (R3)
- #9 Ex2 引言 "the accountability tracking" 原词恢复.

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:15/:16 旧值 | 同行 | VALUE_DIFF 旧值替换 (#1-8, 列错位复位) | — |

### 范围外发现
- F-1 (需主控定): p180 §6.3 "Models for Findings Domains" 章引言 2 句 ("Most subject-level observations … The following domains correspond to the Findings class:") 在 KB 无逐字对应 (ch02_fundamentals.md:49 为另一 PDF 位置的不同句, ch10:268 仅版本变更表). 属 §6.3 章级, 不属 DA 节, 未补. §6.1/§6.2 章引言应同型, 建议主控统一定归属 (如 ch06 汇总页或首域文件).
- F-2: DA/spec.md (p180-181 spec 表 + 脚注) 不在白名单 → 归 O15 spec 扫描.

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DA_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-DA.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']]+[{'file':'knowledge_base/domains/DA/assumptions.md','src':'ig34','lo':180,'hi':182}],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # KB tables 3 / OK 3 / diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p018[0-2]|DA/' $S/fp_regress.jsonl   # 0
pdftoppm -f 182 -l 182 -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p182
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### git diff --stat
```
 knowledge_base/domains/DA/assumptions.md | 10 ++++++++++
 knowledge_base/domains/DA/examples.md    |  6 +++---
 2 files changed, 13 insertions(+), 3 deletions(-)
```
