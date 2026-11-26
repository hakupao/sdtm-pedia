# T2 B-BE reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base: HEAD 884560f (本批未提交); 审查范围 `knowledge_base/domains/BE/examples.md` (batch kb_files) + `knowledge_base/domains/BE/assumptions.md` (主控授权: Description/Overview + spec 首句 + F-1 节引言 NOTE)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-BE_reviewer/`

### 命令与结果 (可复跑, repo 根)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-BE_reviewer; mkdir -p $S
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-BE.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  # exit 1; KB tables 9; OK 7, DIFF 2; diffs 5 (= T-1 x2, T-2, T-3 x2, 全部登记 PDF_TYPO)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # exit 1 RESULT: RED, regressions=48 — 全部 p0118/p0174/p0215-0263/p0363-0396 (他批工作树改动 MK/TE/TU/TA 等)
grep -cE 'p014[3-8]' $S/fp_regress.jsonl   # 0 → 本批无回归
for p in 143 144 145 146 147 148; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
  # + 200dpi 裁切 z146_bs_L/R, z146_be, z147_be, z147_bs, z147_rs (逐格核)
pdftotext -f 143 -l 148 "<PDF>" $S/p143_148.txt; python3 -I $S/scan.py $S   # 双向叙述扫描
diff <(pdftotext -f 143 -l 143 -layout "<PDF>" - | sed -n 2,4p | sed 's/^ *//;s/ *$//' | tr '\n' ' ' | sed 's/ $//') <(sed -n 3p knowledge_base/domains/BE/assumptions.md | tr -d '\n')   # IDENTICAL
python3 tools/check_links.py | tail -1   # live docs: 42 (= 基线)
```

### 无副作用 / 范围
- `git diff HEAD --stat -- knowledge_base/`: BE 仅 assumptions.md (+6) / examples.md (5 行改); 其余 MK/TA/TE/TU 为他批, 与本批无关.
- examples.md: 5 行替换 (:29 :41 :62 :130 :138), 161 行不变; 标题/锚点未变; 其他表行未动.
- assumptions.md: 仅新增 :3-:8 (NOTE 段 + 空行 + `## BE – Description/Overview` + 句 + 空行); 原 :1 标题与 spec 首句/Assumptions 1-7 字节未变. 授权范围外无改动.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无 FAIL / CONDITIONAL 项 | — |

观察 (非本批缺陷, 不阻断): Ex2 bs Row 1 BSORRES 12 mL vs BSSTRESC/BSSTRESN 6 — KB 与 PDF 一致 (p147 渲染 "12 | mL | 6 | 6"), PDF 自身疑似内部不一致但无法由 PDF 确定正确值, 照录合规; 如需可列 T4 用户裁定.

### writer 变更逐条核 (对渲染图)
| # | ref | 判定 | 证据 |
|---|---|---|---|
| 1 | examples:29 QLABEL `SPECIMEN TYPE` | 一致 | p145 suppbe Row 1 渲染 "SPECIMEN TYPE" (大写); Ex2 p147 为 "Specimen Type", KB :103-108 照录 |
| 2 | examples:41 BSSTRESN `2` | 一致 | p146 bs Row 1 BSSTRESN "2" (200dpi) |
| 3-4 | examples:43 BSORRES/BSSTRESC (T-1) | PDF_TYPO 成立 | p146 "DRY ICE/ISOPOPANOL" 两格; isopropanol 拼写错, 按 dispatch 口径保留正确拼写 |
| 5 | examples:43 BSDTC (T-2) | PDF_TYPO 成立 | p146 Row 3 BSDTC 仅 "5-0"; 依据 PDF 自身: 同组 Rows 1-2 = 2005-03-20, Ex1 BEDTC 全为 2005-03-20, Assumption 6b BEDTC=specimen collection |
| 6-7 | examples:124-125 BSREFID (T-3) | PDF_TYPO 成立 | p147 bs Rows 3-4 "298B1-1R0"; 同例 be Row 4 / suppbe Row 3 / relspec Row 3 REFID 与 Rows 4-6 PARENT 均 "298R1-1R0" |
| 8 | examples:138 relspec Row 1 PARENT 空 | 一致 | p147 relspec 200dpi Row 1 PARENT 空格 |
| 9 | examples:62 `[1]` `[2]` | 一致 | p146 "cancer detection,[1] but has poor integrity.[2]In this example" (KB 在 [2] 后补空格, 属空白归一化) |
| 10 | examples:130 "See GF examples for examples of GF datasets." | 一致 | p147 同句逐字 |
| 11 | assumptions:5-7 Description/Overview | 逐字一致 | p143 `diff` 除取词时多带下一标题外完全一致 |
| 12 | assumptions:11 spec 首句 | 未动, 逐字 | p143 加粗句 |
| F-1 | assumptions:3 节引言 NOTE | 逐字 IDENTICAL; 位置正确 (标题后, Description 前, 同 PDF 顺序) | p143 末句 "…publication, after v3.4."; layout 第 21277-21278 行 (§8.8 RELSPEC) 为 "…in a future SDTMIG." → 两处各对其源, 非缺陷 |

### G-TB4 人工逐格 (9 表 全部对 110/200dpi 渲染逐行核)
| 表 (KB 行) | PDF | 行数/列 | 结果 |
|---|---|---|---|
| Ex1 be.xpt (:17) | p145 | 5 行 × 18 列 | 一致 (Row 3 SPDEVID 309827, Row 5 LN43871 / BEPRTYID 空 均核) |
| Ex1 suppbe.xpt (:27) | p145 | 1 × 11 | 一致 (#1 改后) |
| Ex1 bs.xpt (:39) | p146 | 3 × 19 | Row 1 一致 (#2 改后); Row 2 一致; Row 3 除 T-1 (2 格)、T-2 (1 格) 外一致; Row 3 BSORRESU/BSSTRESN/BSSTRESU 空 一致 |
| Ex1 relrec.xpt (:53) | p146 | 4 × 8 | 一致 |
| Ex2 be.xpt (:80) | p146-147 | 10 × 16 | 一致 (Row 3 BEENDTC 2010-04-02T8:00, Row 4 2010-04-02T9:00/2010-04-05T13:50, Row 7 Aliquoted, Row 8 Sequenced/PREPARATION/2010-04-06T10:30 均核) |
| Ex2 suppbe.xpt (:101) | p147 | 6 × 11 | 一致 (QORIG CRF×2 / Collected×4) |
| Ex2 bs.xpt (:120) | p147 | 7 × 17 | 除 T-3 (Rows 3-4 BSREFID) 外一致; Row 4 RIN/QUALITY CONTROL/9.3/单位空 核 |
| Ex2 relspec.xpt (:136) | p147 | 6 × 7 | 一致 (#8 改后) |
| Ex2 relrec.xpt (:149) | p148 | 6 × 8 | 一致 (Rows 1-2 USUBJID/IDVARVAL 空, RELTYPE MANY) |

census v2 自比之外以渲染图独立复核, 无 NO_PDF / UNPARSEABLE / pdf_unparsed / 本批 pdf_only.

### 双向全扫 (p143-148)
- KB→PDF: 两文件全部非表行脚本比对命中; 仅 assumptions:21 / :30 NOHIT, 原因为 PDF 折行 "single-\nsponsor" 与 "--\nHLGTCD" 被归一化脚本误连, 对 p144/p145 渲染核 KB "single-sponsor" / "--HLGTCD" 正确.
- PDF→KB: MISS 仅为 spec 表 (p143-144, 属 spec.md, 范围外 F-3)、§6.2.3 CE (下一节)、表格串文与跨页拼接片段; 拼接片段中的句子均已在 KB 逐句命中. 叙述 0 缺, References 1-2 逐字, 引用标记 [1][2] 已补.
- 表格原子: 见上 G-TB4 逐格表.
- KB 自写解释性内容: 无 (D6 不适用); 伪节号: 无.

### R2 recheck
- `t2_recheck` 为空, 无条目.

### G-TB6 新增/改动行签字
| 行 | 类型 | 出处 |
|---|---|---|
| assumptions:3 | 叙述 | p143 节引言 NOTE (逐字) |
| assumptions:5 `## BE – Description/Overview` | 结构行 (节标题) | p143 小标题 "BE – Description/Overview" — 签字 |
| assumptions:7 | 叙述 | p143 Description 句 (逐字) |
| examples:29 / :41 / :138 | 表行 | p145 / p146 / p147 渲染 |
| examples:62 | 叙述 | p146 Ex2 引言 |
| examples:130 | 叙述 | p147 |
新增/改动 8 行, 无出处 0.

### 结论
PASS — 12 项变更 + F-1 全部有 PDF 出处; 5 格残留 census DIFF 均为依据 PDF 自身成立的 PDF_TYPO (T-1..T-3); 本批 fp 回归 0; live docs 42 不变.
