# T2 B-QS reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base = HEAD (QS 改动未提交; `git diff HEAD -- knowledge_base/domains/QS/`). 整 KB diff 中 QS 只有 assumptions.md (+10) / examples.md (2 行改); 其余 CE/CM/FT/HO/MI 为他批, 不计.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-QS_reviewer/`
- 节页范围: §6.3.9.2 QS = p324 (标题 + Description/Overview + spec 首句 + spec 表起) – p329 (Ex1 Rows 9-10, 其后 6.3.9.3 RS). 与 writer 一致, batch lo/hi 324-329 覆盖完整; 无节引言 NOTE.

### 命令 (可复跑) 与关键输出
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-QS_reviewer; mkdir -p $S
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-QS.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  # exit 1 (全局 PDF_ONLY 338); KB tables 1; status {'OK': 1}; cells compared 150; diffs 0
  # 本批页 324-329 内 PDF_ONLY = 1 张 suppft.xpt (p324, sec 6.3.9.1 = FT 节, 属 B-FT, 非 QS); pdf_unparsed 324-329 = 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # RESULT: RED; regress 51 条, 页码前缀 p0118/0174/0215/0218/0254-0263/0289/0311/0363/0364/0370-0374/0396 — 均非 p0324-0329
grep -cE 'p03(2[4-9])|QS/' $S/fp_regress.jsonl   # 0
pdftotext -f 324 -l 329 -layout "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p324_329.txt
pdftotext -f 324 -l 329 "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p324_329raw.txt
python3 -I $S/rcmp.py $S   # 独立逐词比对 (见下)
pdftoppm -f 328 -l 329 -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### 1. 完整性
- atoms 0 / t2_recheck 0; census DIFF 1 表 (2 CELL, KB 行 19/24) → writer #1/#2 处理, 改后 census OK. writer.jsonl 5 条与报告变更清单 #1-5 一致.

### 2. G-TB4 表格 (独立方法: layout 文本 + 110dpi 渲染图逐格)
qs.xpt (examples.md:13-24) 表头 15 列 + Rows 1-10 逐格对 p328/p329 渲染图:

| KB 行 | Row | 结果 |
|---|---|---|
| 13 | 表头 | 一致 (Row STUDYID DOMAIN USUBJID QSSEQ QSTESTCD QSTEST QSCAT QSORRES QSSTRESC QSSTRESN QSLOBXFL VISITNUM QSDTC QSDY) |
| 15 | 1 | 一致 |
| 16 | 2 | 一致 (QSTEST/QSORRES 折行合并) |
| 17 | 3 | 一致 |
| 18 | 4 | 一致 |
| 19 | 5 | 一致 — QSTEST 单元格第 2 行 "Nothing" (渲染图同格内) → `SWLS01-Live Life Over Change Nothing` 正确 |
| 20 | 6 | 一致 |
| 21 | 7 | 一致 |
| 22 | 8 | 一致 |
| 23 | 9 (p329) | 一致 |
| 24 | 10 (p329) | 一致 — QSTEST 同 Row 5, "Nothing" 在同格第 2 行 |

QSDTC "2003-04-/15" 为单元格内折行 = 2003-04-15, 一致. 无 PDF_TYPO.

### 3. G-TB6 反向溯源 (diff 每条新增/改动行)
| diff 行 | 类型 | 出处 |
|---|---|---|
| assumptions.md:3 `## QS – Description/Overview` | 结构行 (PDF 原小标题) | p324 "QS – Description/Overview" — 签字 |
| assumptions.md:5 | 叙述 2 句 | p324 逐字 (逐词 68=68, 0 差) |
| assumptions.md:7 `## QS – Specification` | 结构行 (PDF 原小标题) | p324 "QS – Specification" — 签字 |
| assumptions.md:9 | spec 首句 | p324 逐字 (含 "—") |
| assumptions.md:11 `## QS – Assumptions` | 结构行 (PDF 原小标题) | p326 "QS – Assumptions" (独立小标题, 位于 spec 表脚注之后、QS 专有句之前) — **核为 PDF 原标题, 签字**; 格式同 CM/FT 先例 |
| examples.md:19 / :24 | 表格单元格 | p328 Row 5 / p329 Row 10 渲染图 |
新增/改动 7 行 (含 3 结构行), 无出处 0. 无 KB 自写解释性内容 (D6 无), 无伪节号.

### 4/5. 位置与副作用
- Description/spec 首句位于标题与 Assumptions 之间 (CM 先例同). 原 :1 标题 / `## QRS Shared Assumptions` 及以下 47 行未动 (diff 仅 +10 行插入). examples.md 仅 2 格改. 无白名单外 QS 改动; spec.md 未动.

### 双向全扫 (p324-329, 含表格原子)
- 独立脚本 `rcmp.py` (pdftotext raw, 弯引号归一, 去列表号, 去页脚):
  - Description+spec 首句: PDF 68 词 = KB 68 词, 0 差.
  - QS – Assumptions + QRS 1-10: PDF 1205 (含 2 组页脚 6 词) / KB 1199. 差异仅: (a) 1c 句 raw 抽取顺序伪差 (layout 文本确认 1c 在 b.iii 之后, KB 位置正确); (b) 页脚; (c) 6a "an resolution"→KB "a resolution" = 沿用 B-RS T-5; (d) 10 "--STRNC"→KB "--STNRC" = 沿用 B-RS T-6; (e) "--\nSPCCND" 折行伪差. 引号风格 O40 不计 (writer 报 13 处, 本脚本归一后不显).
  - Examples 引言 + "Example 1" + 标题 + 说明句: 38 = 38, 0 差.
  - qs.xpt: 见 §2 逐格.
- KB→PDF: assumptions.md 全 59 行、examples.md 全 24 行均有 PDF 出处或为导航结构 (`# QS — Assumptions`/`# QS — Examples`/`## Example 1`/粗体标签).
- PDF→KB 未覆盖: p324-326 spec 表 + 脚注 "1 In this column, an asterisk …" → 属 spec.md (不在白名单), writer F-1 已登记, 同意归 O15/O16.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无阻断问题 | — |

### R2 recheck
- t2_recheck 为空, 无.

### 观察 (非阻断)
- O-1: QS 副本引号风格 (O40) 与 T-5/T-6 沿用 B-RS 登记口径, 一致, 无需本批改.
