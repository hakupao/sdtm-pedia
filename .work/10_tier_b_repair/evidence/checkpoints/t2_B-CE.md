# T2 B-CE writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `d84a22555eb38ab1a7ccdb7645425fec8a031aa5` (CE 文件改前工作树 clean)
- md5: CE/assumptions.md `8e60be51bbe49cf037c8557c371664d7` → `3f9e0f674e495094a45577bca2cb09f5` (25 → 35 行); CE/examples.md `2fafb6cb766b1be391c64f15f4c69a97` → `21de90e8c71327ca0ea2514f6bcd5278` (165 行不变); CE/spec.md 未动 `efe24efc6daa18c78e4bf0e78b6ea0e1`
- 白名单: assumptions.md + examples.md (均在 batch json kb_files)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CE_writer/` (assumptions/examples.before.md, p150-155 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 节页范围核 (O20): p148 下半 "6.2.3 Clinical Events (CE)" (Description/Overview + spec 首句 + spec 表) → p149-150 (spec 续; Assumptions 1-4) → p151 (5-6; Examples Ex1; Ex2 引言) → p152 (Ex2) → p153-155 (Ex3; p155 relrec 后接 6.2.4 DS). batch lo/hi 148-155 **完整覆盖**; 本域无节引言 NOTE.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | CE/assumptions.md:3-5 | ig34_p0148_a015 (REAL_GAP) | INSERTED | 新增 `## CE – Description/Overview` + 定义句逐字 (SM/CM 先例) | 148 |
| 2 | CE/assumptions.md:7-9 | spec 首句 (授权; p148_a017) | INSERTED | 新增 `## CE – Specification` + `ce.xpt, Clinical Events — Events. One record per event per subject, Tabulation.` | 148 |
| 3 | CE/assumptions.md:11 | 结构 (SM 先例) | INSERTED | 新增 `## CE – Assumptions` (PDF 原标题) | 150 |
| 4 | CE/assumptions.md:15 | R3 新增 (p150 assumption 1b) | REPLACED | flags 顺序 `--SDISAB, --SDTH, --SHOSP` → PDF 顺序 `--SDTH, --SHOSP, --SDISAB` | 150 |
| 5 | CE/assumptions.md:16 | R3 新增 (p150 assumption 1c, R2) | REPLACED | "would also be reported as a reason for…" → PDF 原文 "would be reported in AE; death would also be a reason for…" (改写丢 "reported in AE"; 该行仅承载 1c 一个原子) | 150 |
| 6 | CE/examples.md:60 | census:examples.md:60:1:CEENDTC (O10) | REPLACED | 空 → `2005-10-12` (渲染图确认) | 152 |
| 7 | CE/examples.md:46 | unparseable 表 examples.md:41 (Ex2 CRF) | REPLACED | `Other, Specify: ___` 与空格 → `Other, Specify:` / `___` 分两列 (PDF 版面: 横线在第 2 列) | 152 |
| 8 | CE/examples.md:75-76 | unparseable 表 examples.md:72 (Ex3 CRF) | REPLACED | `-- / --- / --` → `--/---/--` (PDF 字面, 两格) | 153 |

- 覆盖率自查: atoms 1 = #1; census DIFF 1 格 = #6; R3 新增 2 (#4-5); 授权/结构 2 (#2-3); unparseable 触碰 2 表 (#7-8).

### census 表处理
| census ref | 处理 | 改后 |
|---|---|---|
| examples.md:58 Ex2 ce.xpt (1 CELL, Row 1 CEENDTC) | #6 | OK |
| 其余 OK 表 (:24 :99 :108 :121 :131 :146 :160) | 渲染图 p151/153-155 逐格人工复核, 一致 | OK |

census_after (`table_census.py --manifest`): KB tables 12, OK 8, UNPARSEABLE 4, diffs 0. (RESULT: RED 来自 manifest 范围内 PDF_ONLY 计数, 与 BE 同, 非本批表.)

### 触碰的 unparseable 表 (reviewer 须对渲染图逐格人工核)
- `CE/examples.md:41` Ex2 CRF (p152): #7.
- `CE/examples.md:72` Ex3 CRF (p153): #8.
- 未触碰但已人工核: `CE/assumptions.md:20` (原 :10) assumption 2 情形表 — 与 p150 渲染一致 (Spontaneously 行三格全空); `CE/examples.md:11` Ex1 CRF — 与 p151 一致 (PDF 表内首行 "Record start dates…" 在 KB 为表前段落, 文字逐字).

### PDF_TYPO 清单
- T-1 (p152 Ex2 Row 5 说明): PDF "Topic Variables,for" 缺空格 → KB 保留 "Topic Variables, for" (dispatch: PDF 自身拼写错 KB 保留正确写法).
- 非 TYPO 说明: Ex3 各表 USUBJID PDF 显示 "ABC -US-701-002"; bbox 两词间隙 1.95pt (<3.5pt 空格阈值, p155 pr Row 3), 属字距, KB `ABC-US-701-002` 不改; census 无差.

### 双向全扫 (含表格原子)
- PDF→KB: p148 (a013 起) – p155 (DS 前) 非表原子逐句规范化比对 (命令见下): 仅余 HEADING 导航差 (`6.2.3 …`/`CE – Examples` ↔ `# CE — Assumptions`/`# CE — Examples`, 先例同) 与 T-1. 叙述/列表逐句对 p150-151 渲染核: 1, 1a, 2, 3, 4, 5a, 5b, 6 逐字; 1b/1c 改后逐字. 9 张表 (assumption 情形表, Ex1 CRF/ce, Ex2 CRF/ce, Ex3 CRF/mh/suppmh/ce/suppce/pr/relrec) 对渲染图逐格: 改后 0 差.
- KB→PDF: 两文件逐行有 PDF 出处. KB 自写导航保留 (D6 范围外, 不加 KB note): `**CRF: CE Example 1 — Prespecified Clinical Events**` (:7)、`**CRF: CE Example 2 — Clinical Events with Severity**` (:39)、`**CRF: CE Example 3 — Bone Fracture Assessment**` (:70; "Bone Fracture Assessment" 为 PDF 表标题). 前两者描述名 PDF 无 (PDF 仅 "CRF"), 同 B-AE L-2 先例保留; 主控可选简化为 `**CRF:**`.
- 未改: assumptions.md:32 (5a) PDF "“Ongoing”" 弯引号, KB 直引号 (同句 "Prior" PDF 为直引号; 规范化等同, 未动).

### 新增 atom 清单 (R3)
- #4 (1b flags 顺序), #5 (1c 改写丢 "reported in AE").

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | assumptions.md:5 (原) 1b flags 序列 | :15 同行 | 值顺序替换为 PDF (#4) | — |
| D-2 | assumptions.md:6 (原) 1c 末句改写 | :16 同行 | R2 改写句恢复 PDF 原文; 该行仅承载 1c 原子 (#5) | — |
| D-3 | examples.md:46/:75/:76 旧格式 | 同行 | 表格按 PDF 版面/字面 (#7-8) | — |

### out_of_scope
- O4 (CEBODYSYS): PDF p149 为 `CEBODSYS`; KB CE/spec.md:140 与 VARIABLE_INDEX.md:220 均为 `CEBODSYS` (正确); `grep -rn CEBODYSYS knowledge_base` = 0. 笔误仅在 PDF 原子 ig34_p0149_a006 (已判 ATOM_ERR). **CE 部分无 KB 改动, 可关闭**.
- O10 (CE Ex2 系统错值): 即 Row 1 CEENDTC 空 → `2005-10-12` (#6). **已处理**.

### 范围外发现
- F-1: pdf_atoms 原子抽错 (T1 已知 "CE spec p149-150 集中"): 另见 ig34_p0150_a007 ("considered as" vs PDF "considered to be")、a008 ("signs of symptomatology"/"flag (--SER)")、a009 ("would also be a record in…")、a012 (情形表首行 CEOCCUR=Y, PDF 空). KB 按渲染图 PDF 为准, 原子账本须更正 (非 KB).
- F-2: spec.md (p148-150 spec 表) 不在白名单; spec 原子大量 IE_CAND/ATOM_ERR, 归 O15 spec 全域扫描.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CE_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-CE.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 8 / UNPARSEABLE 4 / diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p014[89]|p015[0-5]|CE/' $S/fp_regress.jsonl   # 0 行 (仅他批 §6.4.2 p0363 回归)
pdftotext -f 150 -l 151 -layout "source/cdisc/SDTMIG v3.4 (no header footer).pdf" - | grep -n "SDISAB\|reported in AE"
for p in 150 151 152 153 154 155; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
pdftotext -f 155 -l 155 -bbox "source/cdisc/SDTMIG v3.4 (no header footer).pdf" - | grep -A1 'ABC</word>' | grep US   # 间隙 185.75→187.70
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 knowledge_base/domains/CE/assumptions.md | 14 ++++++++++++--
 knowledge_base/domains/CE/examples.md    |  8 ++++----
 2 files changed, 16 insertions(+), 6 deletions(-)
```

## attempt 2 (2026-11-26, 主控 C-1/C-2/C-3 按 reviewer CONDITIONAL)

- examples.md md5 `21de90e8c71327ca0ea2514f6bcd5278` → `5dbcacf128e69598450aeaf44664ebbd` (165 行不变); assumptions.md 未动.

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 9 | CE/examples.md:13-16 | C-1 (unparseable examples.md:11 Ex1 CRF) | REPLACED | 第 2 列 `( ) No  ( ) Yes` → `No  Yes` (PDF 无符号); 第 3 列 `___ / ___ / ___` → 空 (PDF 空), 4 行 | 151 |
| 10 | CE/examples.md:43-46 | C-2 (unparseable examples.md:41 Ex2 CRF) | REPLACED | 8 个日期格 `___ / ___ / ___ (dd/mmm/yyyy)` → `__/___/____ (dd/mmm/yyyy)` (PDF 2/3/4 位掩码) | 152 |
| 11 | CE/examples.md:101-102,123-125,148-150 | C-3 (主控裁定) | REPLACED | USUBJID `ABC-US-701-002` → 照录 PDF `ABC -US-701-002` (mh 2 + ce 3 + pr 3 = 8 格) | 153-155 |

- **更正 attempt 1 表述**: attempt 1 称 "`CE/examples.md:11` Ex1 CRF — 与 p151 一致" **不成立** (第 2 列多 `( )`, 第 3 列多占位符); 已由 #9 修正.

### 改后 CRF 表逐格对渲染图 (110dpi p151/p152/p153)
- Ex1 CRF (:11, p151): 表头 Clinical Sign / Did it occur? / Start Date of First Episode 一致; 4 行 第 1 列 Rash/Wheezing/Edema/Conjunctivitis 一致, 第 2 列 `No  Yes` 一致 (PDF 上下两行 No/Yes), 第 3 列空 一致. 表内标题行 "Record start dates…" → KB :9 段落 (逐字). 0 差.
- Ex2 CRF (:41, p152): 表头 Event (PDF 跨 2 列 → KB `Event` + 空列) 一致; Nausea/Vomit/Diarrhea 第 2 列 ○Yes ○No → `( ) Yes  ( ) No` (符号映射, reviewer 已认可); Other, Specify: / `___` 一致 (#7); Date Started / Date Ended 8 格 `__/___/____ (dd/mmm/yyyy)` 一致; Severity ○Mild ○Moderate ○Severe → `( )` 映射 一致. 0 差.
- Ex3 CRF (:72, p153): 10 行问题/选项一致, 日期 2 格 `--/---/--` (#8). 表头结构行 `| Question | Response Options |` 为 KB 自写 Markdown 结构头 (PDF 无列头, 仅标题行 "Bone Fracture Assessment" → KB :70 标签), reviewer 已签字保留.

### PDF_TYPO / T4 用户裁定项 (补登)
- T-2 (T4): Ex3 mh/ce/pr USUBJID, PDF 8 格均显示 `ABC -US-701-002` (bbox 间隙 1.95pt). PDF 自身无法确定是否为真空格 → 按主控裁定照录 PDF. 候选值 `ABC-US-701-002` (依据: USUBJID 惯例不含空格; 间隙 < 3.5pt 空格阈值, 疑为字距). 撤回 attempt 1 "字距, 不改" 的说法.
- T-3 (T4, 原 reviewer L-3): suppmh/suppce USUBJID `001-001` 与父表 mh/ce `ABC -US-701-002` 不一致 (PDF 内部矛盾); KB 照录 PDF `001-001` 不改.

### 删除清单 (追加)
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-4 | examples.md:13-16 `( )` 符号与第 3 列占位 | 同行 | KB 自写占位, 按 PDF 版面恢复 (#9) | — |
| D-5 | examples.md:43-46 日期格旧格式 | 同行 | PDF 字面 (#10) | — |

### 验证
- census_after2: `{'UNPARSEABLE': 4, 'OK': 8}` diffs 0 (`table_census.py --manifest $S/manifest.json --out $S/census_after2.json`).
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → 42.
- git diff --stat: assumptions.md 14 (+12/-2), examples.md 38 (+19/-19).
