# T2 B-MI writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `f6f06a16abd79478555d96fae7967b68185527d3` (改前 `git diff --quiet -- knowledge_base/domains/MI` = clean)
- md5: MI/assumptions.md `e23d92f207604bea4414467738823e91` → `cbc0ac3f1ba0a322e4a9e47f7324140e` (7 → 19 行); MI/examples.md 未动 `ca930a2cbfd159be0d23cc3fb04ea876`; MI/spec.md 未动 `81489798619b0d4dd949942abda69232`
- 白名单: examples.md (batch json) + assumptions.md (主控授权: Description/Overview + spec 首句, CM/BE/CV 先例, 逐字). 2 条 REAL_GAP 原子即 Description/Overview 两句, 按授权落在 assumptions.md (batch kb_loc=null).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-MI_writer/` (assumptions/examples.before.md, p263/265/266/267 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl, scan.py, wdiff.py)
- 本批 atoms 2 (REAL_GAP) / t2_recheck 0; census DIFF 1 表 (HEADER 1, 0 CELL); pdf_only 0; unparseable 0; out_of_scope 0.
- 完整节页范围 (O20): §6.3.5.8 = p263 下部 (节标题 + MI – Description/Overview 2 句; 上半页属 MB Ex3-4, 不碰) → p264 (MI – Specification 首句 + spec 表) → p265 (spec 表续 + 脚注 + MI – Assumptions 1-3) → p266 (MI – Examples Ex1, Ex2 + suppmi) → p267 上部 (Ex3 + suppmi; 其后 6.3.5.9 PC). batch lo/hi = 263-267 **完整覆盖**. 无节引言 NOTE.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | MI/assumptions.md:3 | 导航 (CM/BE/CV 先例) | INSERTED | 新增 `## MI – Description/Overview` (PDF 原标题) | 263 |
| 2 | MI/assumptions.md:5 | ig34_p0263_a030 | INSERTED | Description 首句 "A findings domain that contains histopathology findings…" 逐字 | 263 |
| 3 | MI/assumptions.md:7 | ig34_p0263_a031 | INSERTED | "The MI dataset provides a record for each microscopic finding observed. …" 2 句逐字 (PDF 为独立段落, 渲染图核) | 263 |
| 4 | MI/assumptions.md:9-11 | spec 首句 (主控授权) | INSERTED | `## MI – Specification` + "mi.xpt, Microscopic Findings — Findings. One record per finding per specimen per subject, Tabulation." 逐字 | 264 |
| 5 | MI/assumptions.md:13 | 导航 (CV 先例) | INSERTED | 新增 `## MI – Assumptions` (PDF p265 原标题), 原列表 1-3 未动 | 265 |
| 6 | MI/examples.md:50 | census:examples.md:50:header:col17 | SKIPPED_PDF_TYPO | KB 保留 `MIDRVFL`; PDF Ex3 表头 `MIDRVL` → T-1 | 267 |

- 覆盖率自查: atoms 2 = #2/#3; census 1 项 = #6; 授权/导航项 3 (#1/#4/#5).

### census 表处理

| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:50 Ex3 mi.xpt (HEADER 1) | #6 PDF_TYPO | DIFF 1 (=T-1, 预期残留) |
| 其余 4 表 (:12 Ex1 mi, :27 Ex2 mi, :37 Ex2 suppmi, :62 Ex3 suppmi) | census OK; 渲染图 p266/267 人工逐格复核一致 | OK |

census_after (本批 manifest): KB tables 5, OK 4, DIFF 1, cells 208, diffs 1 (= T-1).

### PDF_TYPO 清单 (依据 = PDF 自身)
- T-1 (p267 Ex3 mi.xpt 表头第 18 列, 渲染图确认印 "MIDRVL"): 正确值由 PDF 自身确定 — 同节 p266 Ex2 mi.xpt 同列表头为 "MIDRVFL"; Assumption 3 列 "--DRVFL" 为该限定符名; Row 5 该列值 "Y" 与叙述 "This is a derived record" 对应 Derived Flag. → KB 保留 `MIDRVFL` (表头大小写/拼写印刷错口径).

### 双向全扫 (含表格原子)
- PDF→KB: p263 l.40-43, p264 l.1-2, p265 l.37-49, p266 全, p267 l.1-26 叙述与 KB (assumptions+examples, 非表行) 做词序列 difflib 比对 (`wdiff.py`): 唯一差为 PDF 节号标题 "6.3.5.8 Microscopic Findings (MI)" (KB 域文件惯例不收节号标题, 与 CM/BE/CV 一致; spec.md 标题 "MI — Microscopic Findings" 承载) 与 KB H1 "Assumptions". 5 张表对渲染图逐格: 表头/列序/列数/Row 列/全部格一致, 除 T-1.
- KB→PDF: 两文件每个非表行句子均在 PDF 规范化文本中 (`scan.py`), 仅 H1 标题 2 条 (导航). 无 KB 自写解释性内容 (D6 无), 无伪节号.
- Assumptions 1-3 逐词核: 与 p265 一致 (PDF "--\nFAST" 为折行), 无短语级偏差.

### fp_match
- ig34_p0263_a030 / a031: hit_target null (baseline, 仅 terminology 偶中) → `knowledge_base/domains/MI/assumptions.md` (verdict 字段为 ledger 静态值 PARTIAL, 不随改动变).
- regress 输出中 `grep -E 'p026[3-7]|MI/'` 命中 3 条 = ig34_p0263_a020-022 (§6.3.5.7.3 MB Ex3 DI 表, target MB/examples.md), 系已提交 B-MB/B-MS (c3b7b56/955e9d5) 对 MB 文件的改动所致, 非本批 (本批未碰 MB/MS 文件); 另有 ig34_p0363 (§6.4.2) 为他批工作树改动.

### 新增 atom 清单 (R3)
- 无 (叙述全扫 0 缺).

### 删除清单
- 无.

### 范围外发现
- F-1: spec.md 不在白名单; p264-265 spec 表行 fp PARTIAL (ig34_p0264_a004-a009 等) → 归 O15 spec 扫描. spec.md 顶部 "> Class: … Structure: …" 非 PDF 首句原文, 首句已补在 assumptions.md (同 CM/BE 先例).

### 需主控定
- 无.

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-MI_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-MI.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # KB tables 5: OK 4 / DIFF 1 / diffs 1 (=T-1 MIDRVFL vs MIDRVL)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p026[3-7]|MI/' $S/fp_regress.jsonl   # 3 = p0263_a020-022 (MB, 已提交他批)
grep -nF "A findings domain that contains histopathology findings and microscopic evaluations." knowledge_base/domains/MI/assumptions.md   # :5
for p in 263 264 265 266 267; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
python3 -I $S/wdiff.py; python3 -I $S/scan.py knowledge_base/domains/MI/assumptions.md knowledge_base/domains/MI/examples.md
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### git diff --stat
```
 knowledge_base/domains/MI/assumptions.md | 12 ++++++++++++
 1 file changed, 12 insertions(+)
```
