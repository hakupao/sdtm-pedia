# T2 B-QS writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `ab8e73d7917ff9946d9910be4ea00b1862fa0895` (QS 文件改前工作树 clean)
- md5: QS/assumptions.md `4285b7a3319c7c27152851d2fd086369` → `4b4f09c87fe5d61d3ea8bd7aada313fa` (49 → 59 行); QS/examples.md `d110bcbfb3b611e99b7dcc1b315c9a72` → `7ce6c59f39949d5c7b148b03befe8936` (24 行不变); QS/spec.md 未动 `da14edf6a99a426ab100fdad929a7eac`
- 白名单: examples.md (batch json) + assumptions.md (主控通用授权: Description/Overview + spec 首句; 逐词偏差)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-QS_writer/` (assumptions.before.md, examples.before.md, cmp.py, p-328/p-329 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 0 / t2_recheck 0; census DIFF 1 表 (2 CELL, KB 行 19/24); pdf_only 0; unparseable 0; out_of_scope 0.
- 节页范围核 (O20): §6.3.9.2 QS = p324 (节标题 "6.3.9.2 Questionnaires (QS)" 在 FT suppft 表之后; Description/Overview + spec 首句 + spec 表) → p325-326 (spec 表续 + 脚注) → p326 (QS – Assumptions + QRS Shared 引言 + 1-3) → p327 (4-7) → p328 (7a-10 + QS – Examples 引言 + Ex1 qs.xpt Rows 1-8) → p329 (Rows 9-10; 其后 6.3.9.3 RS). batch lo/hi 324-329 **完整覆盖**; 无节引言 NOTE (节标题后直接 Description/Overview).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | QS/examples.md:19 | census:examples.md:19:5:QSTEST | REPLACED | `SWLS01-Live Life Over Change` → `SWLS01-Live Life Over Change Nothing` (渲染图单元格折行第 2 行 "Nothing") | 328 |
| 2 | QS/examples.md:24 | census:examples.md:24:10:QSTEST | REPLACED | 同上 (Row 10) | 329 |
| 3 | QS/assumptions.md:3-5 | Description/Overview (主控授权) | INSERTED | 新增 `## QS – Description/Overview` + p324 两句逐字 (位于标题后, CM/FT 结构) | 324 |
| 4 | QS/assumptions.md:7-9 | spec 首句 (主控授权) | INSERTED | 新增 `## QS – Specification` + "qs.xpt, Questionnaires — Findings. One record per … Tabulation." 逐字 | 324 |
| 5 | QS/assumptions.md:11 | PDF 节标题 "QS – Assumptions" | INSERTED | 新增 `## QS – Assumptions` 小节标题 (PDF 原标题; CM/FT 同结构; 原首句 :13 不动) | 326 |

- 覆盖率自查: atoms 0; census 2 格 = #1-2; 授权项 #3-5. 既有标题/锚点未改.

### census 表处理

| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:13 Ex1 qs.xpt (2 CELL, 行 19/24) | #1-2 | OK (KB tables 1, OK 1, diffs 0) |

另对 p328/p329 渲染图逐格人工核 qs.xpt 表头 15 列 + Rows 1-10 全部格: 除 #1-2 外 0 差 (QSDTC "2003-04-\n15" 为单元格折行 = 2003-04-15).

### QRS Shared Assumptions 逐词核 (QS 副本 vs p326-328)
- 方法: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-QS_writer/cmp.py` — PDF p326-328 "QS – Assumptions" 至 "QS – Examples" 文本 vs KB `## QS – Assumptions` 之后全文; 空白归一、去列表号、处理 "--\nSPCCND" 折行; **引号不归一**; 词级 difflib. 词数 PDF 1199 = KB 1199.
- 结果: 文字逐词一致, 仅差:
  - 引号风格 13 处 (PDF “ ” ’ vs KB 直引号: "standardized responses" ×5, "total", instrument's ×5 含 "instrument's CT", instrument's annotated CRF) → O40 已登记, **不改**.
  - QRS 6a PDF "providing an resolution" vs KB "a resolution" → 沿用 B-RS T-5 (冠词笔误, 语法确定; FT/RS 副本同), KB 保留.
  - QRS 10 PDF "--STRNC" vs KB "--STNRC" → 沿用 B-RS T-6 (--STRNC 非 SDTM 变量; 同节 DR 11 / spec 为 --STNRC), KB 保留.
- QS 专有句 "There are no additional QS-specific assumptions; …" 与 QRS 引言句逐字. 列表层级 (1-10, a-d, i-iii, iii.1) 与 PDF 一致.

### PDF_TYPO 清单
- 无新增. QRS 6a / 10 两处沿用 B-RS T-5 / T-6 登记 (KB 已为正确值, 本批未改).

### 双向全扫 (含表格原子)
- PDF→KB: p324 Description 2 句 + spec 首句 → assumptions.md:5/:9 逐字 (新增). p324-326 spec 表行 → spec.md (不在白名单, 未核, 见 F-1). p326 脚注 "1 In this column, an asterisk …" → 见 F-1. p326-328 QS – Assumptions + QRS 1-10 → assumptions.md:13-59 (见上节). p328 Examples 引言 2 句 / "Example 1" / "Satisfaction With Life Scale (SWLS)" / "The example represents …" / "qs.xpt" → examples.md:3/:5/:7/:9/:11 逐字. qs.xpt 10 行逐格 (渲染图) 见 census 节.
- KB→PDF: examples.md 全 24 行每行有 PDF 对应 (`# QS — Examples`/`## Example 1`/粗体标签为导航). assumptions.md 全 59 行每行有 PDF 对应; `## QRS Shared Assumptions` 对应 PDF 小标题. 无 KB 自写解释性内容 (D6 无), 无伪节号.
- fp_match 改后: p324-328 无 QS 原子落入 fp 范围; `grep -E 'p03(2[4-9])|QS/' fp_regress.jsonl` = 0 (全量 RED 来自 §6.4.2 ig34_p0363_a016/a017, 他批工作树改动, 非本批).

### 新增 atom 清单 (R3)
- #5 `## QS – Assumptions` 小节标题 (PDF 原标题; 授权内结构, reviewer 确认).

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:19/:24 旧 QSTEST 值 | 同行 | VALUE_DIFF 旧值替换 (#1/#2) | — |

### 范围外发现
- F-1: QS/spec.md 未含 p326 spec 表脚注 ("1 In this column, an asterisk (*) indicates …"); FT/spec.md 同. spec.md 不在白名单 → 归 O15/O16 spec 扫描.
- F-2: QRS 副本引号风格 (O40) 仍待 T4 全局口径.

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-QS_writer
git show HEAD:knowledge_base/domains/QS/assumptions.md > $S/assumptions.before.md; git show HEAD:knowledge_base/domains/QS/examples.md > $S/examples.before.md
python3 -I $S/cmp.py   # QRS 逐词: 仅引号 13 处 + an resolution + --STRNC; 词数 1199/1199
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-QS.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # KB tables 1 OK, diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p03(2[4-9])|QS/' $S/fp_regress.jsonl   # 0
pdftoppm -f 328 -l 329 -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 knowledge_base/domains/QS/assumptions.md | 10 ++++++++++
 knowledge_base/domains/QS/examples.md    |  4 ++--
 2 files changed, 12 insertions(+), 2 deletions(-)
```
