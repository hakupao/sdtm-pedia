# T2 B-MI reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base = HEAD (`0192ae8`); 本批 diff 仅 `knowledge_base/domains/MI/assumptions.md` +12 行 (md5 `cbc0ac3f1ba0a322e4a9e47f7324140e`); `MI/examples.md` / `MI/spec.md` diff 为空. 工作树其他 M 文件 (CE/CM/FT/HO/QS) 属他批, 不计.
- 节页范围核: §6.3.5.8 = p263 下部 (节标题 + Description/Overview 2 段) → p264 (Specification 首句 + spec 表) → p265 (spec 续 + 脚注 + Assumptions 1-3) → p266 (MI – Examples, Ex1/Ex2 + suppmi) → p267 上部 (Ex3 + suppmi; 其后 6.3.5.9 PC). 与 writer 一致; p263 上部 MB Ex3-4 不计.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-MI_reviewer/`

### 命令 (可复跑, repo 根)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-MI_reviewer; mkdir -p $S
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-MI.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1; KB tables 5 {'OK': 4, 'DIFF': 1}; cells 208; diffs 1 (:50 HEADER idx17 kb MIDRVFL / pdf MIDRVL = T-1)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # RESULT: RED (全局)
grep -E 'p026[3-7]|domains/MI/' $S/fp_regress.jsonl   # 3 = ig34_p0263_a020/a021/a022 (MB, t1_errata.json 已登记 B-MB), 不计本批; 其余 RED = p0363 §6.4.2 他批
grep -E 'p0263_a03[01]"' $S/fp_after.jsonl   # a030/a031 hit_target = knowledge_base/domains/MI/assumptions.md (baseline null)
for p in 263 264 265 266 267; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # broken relative links: 18668 (live docs: 42)
```
- 独立 norm 核 (`fp_match.norm`, PDF p263/p264/p265 文本逐字): Description 2 句、spec 首句、3 个标题全部 `in norm(assumptions.md)` = True. 标题破折号 U+2013 (en dash, 同 PDF), spec 首句 U+2014 (同 PDF).

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | 1-6 | 无阻断问题 | — |
| examples.md:23 (未改行) | 观察 LOW | PDF 原句 "is a represented in a derived record" 语法瑕疵, KB 逐字照录; 正确写法无法由 PDF 自身唯一确定, 维持照录合理. 可选: 主控决定是否登记 T4 | p266 Row 3 |
| examples.md:1 (未改行) | 观察 LOW | PDF p266 "MI – Examples" 小标题由 KB H1 "MI — Examples" 承载 (域文件惯例), 非缺失 | p266 |

### T-1 依据核 (PDF_TYPO)
- p267 Ex3 mi.xpt 表头第 18 列渲染图印 "MIDRVL" (确认). 依据: (a) 同节 p266 Ex2 mi.xpt 同位置表头 "MIDRVFL"; (b) p265 Assumption 3 列有限定符 "--DRVFL"; (c) Ex3 Row 5 该列值 "Y" 且叙述 "This is a derived record"; MI 变量命名 MI+DRVFL. 正确值可由 PDF 自身确定 → KB 保留 `MIDRVFL` 成立 (表头拼写印刷错口径). census 残留 DIFF 1 = T-1, 预期.

### 人工逐格 (渲染图 110dpi vs KB, 5 张表)
| 表 (KB 行) | PDF 页 | 表头/列数 | 行 | 结果 |
|---|---|---|---|---|
| Ex1 mi.xpt (:12) | 266 | 16 列一致 | R1 ABC-1001 0/0 NEGATIVE…2001-06-15; R2 ABC-2002 2+/2+ POSITIVE | 一致 |
| Ex2 mi.xpt (:27) | 266 | 18 列一致 (含 MIDRVFL) | R1 PROPORTION 3/3/3, DRVFL 空; R2 STRONG/3/3, DRVFL 空; R3 MIORRES 空, 6/6, DRVFL Y | 一致 |
| Ex2 suppmi.xpt (:37) | 266 | 11 列一致 | R1 MIGRPID 1 MISCELOC Subcellular Location NUCLEUS CRF, QEVAL 空 | 一致 |
| Ex3 mi.xpt (:50) | 267 | 20 列; 第 18 列 PDF MIDRVL / KB MIDRVFL | R1-4 INTENSITY 0/1+/2+/3+, 25/40/35/0 %, DRVFL 空; R5 TOTAL SCORE, ORRES/ORRESU/STRESU 空, 110/110, Y | 一致 (除 T-1) |
| Ex3 suppmi.xpt (:62) | 267 | 11 列一致 | R1 … CYTOPLASM CRF, QEVAL 空 | 一致 |

### 双向全扫 (含表格原子)
- PDF→KB: p263 节标题以下、p264 首句、p265 Assumptions 1-3、p266 全页、p267 至 6.3.5.9 前: 所有叙述句 / Row 说明 / 表头 / 表格 / 数据集标签 (mi.xpt / suppmi.xpt) 均在 KB 找到; 节号标题 "6.3.5.8 Microscopic Findings (MI)" 按域文件惯例不收 (spec.md 标题承载). 缺失 0.
- KB→PDF: assumptions.md 19 行、examples.md 64 行逐行有 PDF 出处; 无 KB 自写解释 (D6 无需), 无伪节号.
- Assumptions 1-3 逐词对 p265 一致 (PDF "--\nFAST" 折行).

### G-TB6 新增行签字 (assumptions.md)
| 行 | 内容 | 类型 | 出处 |
|---|---|---|---|
| 3 | `## MI – Description/Overview` | 结构行 (PDF 原标题) | p263 签字 |
| 5 | Description 首句 | 内容 (a030) | p263 逐字 |
| 7 | "The MI dataset provides…" 2 句 | 内容 (a031) | p263 逐字, 与首句为独立段 (渲染图) |
| 9 | `## MI – Specification` | 结构行 (PDF 原标题) | p264 签字 |
| 11 | mi.xpt 首句 | 内容 (授权) | p264 逐字 |
| 13 | `## MI – Assumptions` | 结构行 (PDF 原标题) | p265 签字 |
| 2/4/6/8/10/12 | 空行 | 结构 | 签字 |
- 新增内容行 3, 无出处 0. 位置/格式与 BE/CV 先例一致 (H1 下, 列表前). 原列表 1-3 未动; H1 未动.

### R2 recheck
- `t2_recheck` 为空, 无.

### 无副作用
- 整个 KB diff 中本批文件仅 MI/assumptions.md, 属主控授权范围 (Description/Overview + spec 首句 + PDF 原标题); examples.md 未改; 无删除.
