# T2 B-IE writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `0192ae8d904b28a945c50e04241f25c8cf709cf0` (IE 文件改前工作树 clean)
- md5: IE/assumptions.md `b2d924f5e494cd66192677de6c20e93c` → `52184de0d2ce3bb54509155501fbec67` (9 → 19 行); IE/examples.md 未动 `2c90e887fa81855d646b031280c29aba`; IE/spec.md 未动 `54c1d1e0916b34d7473a1e449a795c4b`
- 白名单: examples.md (batch json) + assumptions.md (主控授权: Description/Overview + spec 首句, QS/CM 先例, 逐字)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-IE_writer/` (assumptions.before.md, examples.before.md, p-194.png 110dpi)
- 本批 atoms 1 (REAL_GAP) / t2_recheck 0 / census DIFF 0 / pdf_only 0 / unparseable 0 / out_of_scope 0.
- pdf_ranges 覆盖核 (O20): IE 节 = p193 "6.3.4 Inclusion/Exclusion Criteria Not Met (IE)" (无节引言 NOTE; Description/Overview + spec 首句 + spec 表 + 脚注) → p194 (Assumptions 1-4 + Examples Ex1 ie.xpt; 其后 6.3.5). 主控提示 "p191-194" 不准: p191-192 属 EG (§6.3.3). batch lo/hi = 193-194 **完整覆盖**.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | IE/assumptions.md:3-5 | ig34_p0193_a003 | INSERTED | 新增 `## IE – Description/Overview` + p193 原句 "A findings domain that contains those criteria …" 逐字 | 193 |
| 2 | IE/assumptions.md:7-9 | spec 首句 (主控授权) | INSERTED | 新增 `## IE – Specification` + "ie.xpt, Inclusion/Exclusion Criteria Not Met — Findings. One record per …, Tabulation." 逐字 | 193 |
| 3 | IE/assumptions.md:11 | PDF 小标题 "IE – Assumptions" (p194) | INSERTED | 新增 `## IE – Assumptions` 小标题 (QS/CM 先例结构; 原列表 1-4 未改) | 194 |

- 覆盖率自查: atoms 1 = #1. 授权项 #2; 结构标题 #3.
- 逐字核: 4 段字符串 (`grep -F`) 在 ig34_p0193.txt / p0194.txt 与 assumptions.md 各命中 1 (含 en dash `–` / em dash `—`).

### census 表处理
- 本批 census 无 DIFF/pdf_only. ie.xpt (examples.md:13-18) 对 p194 110dpi 渲染图逐格人工核: 16 列表头/列序一致, 4 行全部单元格一致 (XYZ-0007 等为折行, WEEK -8 / 1999-01-10 等同), 0 差.

### PDF_TYPO 清单
- 无.

### 双向全扫 (含表格原子)
- PDF→KB: p193 Description/Overview、spec 首句 (现已补); spec 表 + 脚注属 spec.md (范围外, 见 F-1/F-2). p194 Assumptions 1-4 逐句在 assumptions.md (规范化比对 OK; item 4 的 "--\nSTRESU" / "--\nLOBXFL" 为 PDF 折行, 渲染图确认 KB `--STRESU`/`--LOBXFL` 正确); Examples 引言 + Rows 1-2/3-4 + `ie.xpt` + 表 4 行逐字在 examples.md. 0 缺.
- KB→PDF: assumptions.md / examples.md 全文件每行均有 PDF 对应; `# IE — Assumptions` / `# IE — Examples` / `## Example 1` / `**ie.xpt**` / `**Rows …:**` 为导航/格式. 无 KB 自写解释性内容 (D6 无), 无伪节号.

### 新增 atom 清单 (R3)
- 无 (叙述 0 缺).

### 删除清单
- 无.

### 范围外发现
- F-1: spec.md 缺 p193 spec 表脚注 "1In this column, an asterisk (*) indicates …" (spec.md 不在白名单) → 归 O15 spec 扫描.
- F-2: spec.md:84 IESCAT CDISC Notes "or for to categorize as a major or minor exceptions" 与 PDF 一致 (PDF 自身语病), 仅登记, 不需改.

### 触碰的 unparseable 表
- 无.

### git diff --stat
```
 knowledge_base/domains/IE/assumptions.md | 10 ++++++++++
 1 file changed, 10 insertions(+)
```

### 复跑命令
```
P=.work/10_tier_b_repair/work/pdf_pages; K=knowledge_base/domains/IE/assumptions.md
for s in "A findings domain that contains those criteria that cause the subject to be in violation of the inclusion/exclusion criteria." "ie.xpt, Inclusion/Exclusion Criteria Not Met — Findings. One record per inclusion/exclusion criterion not met per subject, Tabulation." "IE – Description/Overview" "IE – Specification"; do grep -cF "$s" $P/ig34_p0193.txt; grep -cF "$s" $K; done   # 全 1
grep -cF "IE – Assumptions" $P/ig34_p0194.txt   # 1
grep -n "6\.3\.[345]" $P/ig34_p019*.txt   # 节范围 p193-194
pdftoppm -f 194 -l 194 -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" <scratch>/p   # ie.xpt 逐格
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```
- live docs: 42 (改后实测).

### 需主控定
- 无.
