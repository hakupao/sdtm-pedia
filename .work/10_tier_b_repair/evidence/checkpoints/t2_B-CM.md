# T2 B-CM writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `f6f06a16abd79478555d96fae7967b68185527d3` (CM 文件改前工作树 clean)
- md5: CM/examples.md `f6df052d6189815ee95eb0f06f63fc5d` → `01c3d7d7898ae19665c34b216eaccf58` (103 行不变); CM/assumptions.md `f5f4996023add39bb46cccfe267a0ac6` → `d28bc2ea19a6dc041ab9f5081f01f688` (29 行不变); spec.md 未动
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CM_writer/` (examples.before.md, assumptions.before.md, p102 渲染 110dpi, scan.py/rscan.py, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 0 / t2_recheck 0; census DIFF 1 表 (2 CELL, KB 行 39); pdf_only 0; unparseable 0; out_of_scope 0.
- 页范围核 (O20): CM 节 = p98 "6.1.2 Concomitant/Prior Medications (CM)" (无节引言 NOTE; Description/Overview + spec 首句 + spec 表) → p99-100 (spec 续; p100 Assumptions 1-3a) → p101 (3b-5 + Examples Ex1) → p102 (Ex1 续, Ex2, Ex3, Ex4) → p103 (Ex4 续, Ex5; 其后 6.1.3 Exposure Domains). batch lo/hi = 98-103 **完整覆盖** (pdf_pages=102 仅 DIFF 表页).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | CM/examples.md:39 | census:examples.md:39:2:USUBJID | REPLACED | `1` → `2` (渲染图 Ex2 Row 2 USUBJID=2) | 102 |
| 2 | CM/examples.md:39 | census:examples.md:39:2:CMSEQ | REPLACED | `2` → `1` (渲染图 CMSEQ=1) | 102 |
| 3 | CM/assumptions.md:22 | R3 新增 (assumption 3a 缺词, 主控追加授权) | REPLACED | "to indicate the intervention" → "to indicate whether the intervention" | 100 |
| 4 | CM/assumptions.md:29 | R3 新增 (assumption 5 缺词, 主控追加授权) | REPLACED | "any identifier, timing variables" → "any identifier variables, timing variables" | 101 |
| 5 | CM/assumptions.md:3-9 | Description/Overview + spec 首句 | — (PRESENT) | 已逐字存在 (p98), 未改 | 98 |

- 覆盖率自查: atoms 0; census 2 格 = #1-2; R3 新增 2 (#3-4); 授权项核 1 (#5).

### census 表处理
| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:36 Ex2 cm.xpt (2 CELL) | #1-2 | OK |
| 其余 4 表 (:17 :55 :71 :96) | census OK; Ex1/Ex3/Ex4/Ex5 对 layout 文本逐格人工核一致 (Ex5 折行单元格已合并核) | OK |

census_after: KB tables 5, OK 5, diffs 0 (RESULT RED 来自 manifest 全 PDF 解析的 PDF_ONLY 计数, 与 BE 同, 非本批).

### PDF_TYPO 清单
- 无. (Ex2 PDF 为 2 名受试者各 1 条; 叙述 "whether subjects use…" 不矛盾, 照 PDF.)

### 双向全扫 (含表格原子)
- KB→PDF: `scan.py` 对 assumptions.md + examples.md 每个非表格句规范化 (弯/直引号、破折号等价) 后在 p98-103 拼接文本中查找; 改前仅 2 MISS (#3/#4), 改后 0. 表格 5 张逐格对 PDF.
- PDF→KB: `rscan.py` + 人工逐句读 p98 (Description/spec 首句) 与 p100-103 (Assumptions 1-5、Ex1-5 叙述/Row 说明/表): 除 #3/#4 及下列 F-1 外 0 缺. 弯引号 (p100 “ASPIRIN…”、sponsor’s; p102 study’s) KB 为直引号, 规范化等价, 按 B-CE 先例未动.
- 无 KB 自写解释性内容 (D6 无), 无伪节号; 标题/`**cm.xpt**`/`**Row N:**` 为导航.

### 新增 atom 清单 (R3)
- #3 (3a "whether"), #4 (5 "variables").

### 删除清单
| # | 位置 | 原因 |
|---|---|---|
| D-1 | examples.md:39 旧值 1/2 | VALUE_DIFF 旧值替换 (#1-2) |

### 需主控定
- F-1: CM/assumptions.md:18 (assumption 2c) 末尾多一整句 "If an intervention term does not have a decode value in the dictionary, then CMDECOD will be left blank." — PDF p100 2c 无此句 (止于 "…Define-XML document."); 该句实出自 p98 spec 表 CMDECOD CDISC Notes. 属整句增补 (非逐词级), 未改. 建议: D2 删扩写 (spec.md 已承载该句时) 或 D6 标注.

### 范围外发现
- 无其他.

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CM_writer
python3 -I $S/scan.py     # 0 MISS
pdftoppm -f 102 -l 102 -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p102
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # KB tables 5, OK 5, diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -cE 'p0(09[89]|10[0-3])|CM/' $S/fp_regress.jsonl   # 0 (余 regress 为他批 §6.4.2)
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 knowledge_base/domains/CM/assumptions.md | 4 ++--
 knowledge_base/domains/CM/examples.md    | 2 +-
 2 files changed, 3 insertions(+), 3 deletions(-)
```

## attempt 2 (主控裁定 F-1, 2026-11-26T04:58:59Z)
- 核: `grep -n "decode value in the dictionary, then CMDECOD will be left blank" knowledge_base/domains/CM/spec.md` → spec.md:84 (CMDECOD CDISC Notes) 逐字含该句 (全行未截断显示核对).
- 变更: CM/assumptions.md:18 (2c) 删末句 "If an intervention term does not have a decode value … left blank." → 2c 止于 "…Define-XML document." (与 PDF p100 一致). 行数 29 不变. 新 md5 `ee387c8140bdfd9dc63516b136d1ce18`.
- 删除清单: D-2 | assumptions.md:18 末句 | D2 去重 (p98 spec CMDECOD Notes 被挪入 2c) | 保留副本 spec.md:84.
- scan.py 0 MISS; F-1 状态: **已处理**. 其余未动.
