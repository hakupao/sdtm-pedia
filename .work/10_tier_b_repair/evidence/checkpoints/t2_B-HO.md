# T2 B-HO writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `f6f06a16abd79478555d96fae7967b68185527d3` (HO 文件改前工作树 clean; 基线取 `git show HEAD:<file>`)
- md5: HO/examples.md `1cb2449fe07a30d79afdf4cfe2c1c521` → `e71563a90adf090479dce77767dd87b5` (81 行不变); HO/assumptions.md `46007dfa8411da88117542fc7a322abb` → `72e0010c2cfff8088aa60e4bfaacabe1` (13 → 23 行); HO/spec.md 未动 `c1a2c549a436a2057ef25b49592b6b39`
- 白名单: examples.md (batch json) + assumptions.md (主控通用授权: Description/Overview + spec 首句, CM/BE 先例, 逐字)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-HO_writer/` (examples/assumptions.before.md, p169-171 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 2 (VALUE_DIFF) / t2_recheck 0; census DIFF 2 表 (2 CELL, KB 行 25/72); pdf_only 0; unparseable 0; out_of_scope 0.
- 完整节页范围核 (O20): §6.2.5 HO = p167 下半 ("6.2.5 Healthcare Encounters (HO)" 标题 + Description/Overview + spec 首句 + spec 表起) → p168 (spec 续) → p169 (spec 末 + 脚注 + Assumptions 1-5 + Examples Ex1 引言/Rows 1-8) → p170 (Rows 9-12 + Ex1 ho/suppho + Ex2 引言 + Ex2 ho Rows 1-8) → p171 上半 (Ex2 ho Rows 9-11 + 句 + suppho; 其后 6.2.6 MH). batch lo/hi = 167-171 **完整覆盖** (batch `pdf_pages` 169-171 仅表/例页). 节内无引言 NOTE, 无 References.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | HO/examples.md:25 | ig34_p0169_a0024 + census:examples.md:25:5:HOTERM | SKIPPED_PDF_TYPO | KB 保留 `REHABILITATION FACILITY`; PDF Ex1 ho Row 5 印 `REHABILIATION FACILITY` → T-1 | 170 |
| 2 | HO/examples.md:72 | ig34_p0171_a0002 + census:examples.md:72:10:HOSTDTC | REPLACED | `2011-06-25T17:00` → `2011-06-25T10:00` (渲染图确认) | 171 |
| 3 | HO/examples.md:40 | R3 新增 (Ex1 Row 5 叙述, 逐词偏差) | REPLACED | "first encounter recorded for subject ABC123105" → "first encounter for subject ABC123105" (删 KB 多出的 recorded) | 170 |
| 4 | HO/examples.md:42 | R3 新增 (Ex1 Row 6 叙述, 逐词偏差) | REPLACED | "second encounter recorded for subject ABC123105" → "second encounter for subject ABC123105" | 170 |
| 5 | HO/examples.md:75 | R3 新增 (Ex2 suppho 前句) | REPLACED | `ABC123101's` → `ABC123101’s` (PDF 弯撇号, 规则 1 保持弯引号原样) | 171 |
| 6 | HO/assumptions.md:3-5 | ig34_p0167_a0020 Description/Overview (主控授权) | INSERTED | 新增 `## HO – Description/Overview` + p167 原句逐字 | 167 |
| 7 | HO/assumptions.md:7-9 | spec 首句 (主控授权) | INSERTED | 新增 `## HO – Specification` + "ho.xpt, Healthcare Encounters — Events. One record per healthcare encounter per subject, Tabulation." | 167 |
| 8 | HO/assumptions.md:11 | PDF 节标题 (CM/BE 结构) | INSERTED | 新增 `## HO – Assumptions` (p169 原标题), 原列表 1-5 未动 | 169 |

- 覆盖率自查: atoms 2 = #1-2; census 2 格 = #1-2 (同格); R3 新增 3 (#3-5); 授权项 3 (#6-8).
- #6/#7 逐字核: `pdftotext -f 167 -l 167 -layout <PDF> - | grep -A1 "^An events domain"` 合并折行 vs KB:5 → `cmp` IDENTICAL; `grep "^ho.xpt"` vs KB:9 → `cmp` IDENTICAL.

### census 表处理

| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:19 Ex1 ho.xpt (1 CELL, :25 HOTERM) | #1 PDF_TYPO | DIFF 1 (= T-1, 预期残留) |
| examples.md:61 Ex2 ho.xpt (1 CELL, :72 HOSTDTC) | #2 | OK |
| examples.md:46 / :79 suppho.xpt | census OK; 渲染图人工复核一致 | OK |

census_after: KB tables 4, OK 3, DIFF 1, diffs 1 — 仅 T-1.

### PDF_TYPO 清单 (依据 = PDF 自身)
- T-1 (p170 Ex1 ho Row 5 HOTERM): PDF "REHABILIATION FACILITY" 漏字母 t. 正确值由 PDF 自身确定: 同页 Ex2 ho Row 3 HOTERM = "REHABILITATION FACILITY"; Ex1 叙述 Rows 3-5 "transferred to a rehabilitation facility"; Assumption 1 "rehabilitation facility stays". 按 dispatch 口径 "PDF 自身拼写错 KB 保留正确拼写" → KB 不改.

### 预期 fp 回归
- fp_match 改后 p167-171 与 baseline verdict 逐条比 **0 变化** (EXACT 10 / INTENTIONAL_EXCLUDE 36 / EQUIVALENT 28 / PARTIAL 24). PARTIAL 中 p167_a023-025 / p168_a001-009 为 spec 表行 (spec.md, 范围外 O15); 其余为 example TABLE_ROW (matcher 对表行仅模糊匹配; 以 census + 渲染图为准: 4 表除 T-1 外 0 差) 及 p170_a001-003 (Ex2 引言, 人工核 KB:57 逐字).
- 全量 regress 51 条, `grep -E 'p016[7-9]|p017[01]|HO/'` = 0 (均为他批工作树改动).

### 双向全扫 (含表格原子)
- PDF→KB: p169-171 Assumptions 1-5 + 全部例子叙述按句规范化子串比对 (脚本见复跑命令), 38 句仅 1 条 "MISS" 为标题行 "HO – Examples Example 1" 与首句粘连 (导航标题, KB 有 `# HO — Examples` / `## Example 1`), 实 0 缺. 4 张表 (Ex1 ho/suppho, Ex2 ho/suppho) 对 110dpi 渲染图逐格人工核: 表头/列序/列数/Row 列一致, 除 T-1 外 0 差. p167 Description + spec 首句已补 (#6-7).
- KB→PDF: examples.md / assumptions.md 全文件每行均有 PDF 对应; 无 KB 自写解释性内容 (D6 无), 无伪节号. Assumption 5 PDF 部分 `‑‑` 为不换行连字符 (U+2011), KB 用 `--`, 属字符规范化, 未改.
- Ex1 Rows 3-4 叙述 PDF 写 "subject ABC123103" 而表 Rows 3-4 为 ABC123102 (supp Rows 3-4 才是 ABC123103; 叙述实指 suppho 行) — KB 与 PDF 一致, 非差异.

### 新增 atom 清单 (R3)
- #3 / #4 Ex1 Row 5/6 叙述删多余 "recorded"; #5 弯撇号.

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:72 旧值 T17:00 | 同行 | VALUE_DIFF 旧值替换 (#2) | — |
| D-2 | examples.md:40 / :42 "recorded" 一词 | 同行 | 逐词偏差恢复 PDF 原文 (#3/#4; 主控追加授权 RE/DM/DD 先例) | — |

### 范围外发现
- F-1: spec.md (p167-169 spec 表) 不在白名单, fp PARTIAL 12 条 → 归 O15 spec 扫描.
- 无需主控定事项.

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-HO_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-HO.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 3 / DIFF 1 / diffs 1 (=T-1)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p016[7-9]|p017[01]|HO/' $S/fp_regress.jsonl   # 0
for p in 169 170 171; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```
叙述全扫脚本: pdftotext p169-171 取 "HO – Assumptions" 至 "6.2.6 Medical" 段, 去表行/页脚, U+2011→`-`, 按句切分, 去 "Row(s) N:" / 列表号前缀后判是否为 KB (examples+assumptions, 去 `**`/换行) 的子串.

### git diff --stat
```
 knowledge_base/domains/HO/assumptions.md | 10 ++++++++++
 knowledge_base/domains/HO/examples.md    |  8 ++++----
 2 files changed, 14 insertions(+), 4 deletions(-)
```
