# T2 B-NV writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `46a66e94695795a4f6d3ac2aecef248dbe7fbbe5` (NV 文件改前工作树 clean)
- md5: NV/assumptions.md `fe43e4b89b48da061b8f20e61e9e63d1` → `21f2e97e03613fb3c41faaec9b05726d` (20 → 48 行); NV/examples.md `719c3123588194d343f7163dfa0c3135` → `449c093959b652082ee9e04b2f4f10c1` (87 行不变); NV/spec.md 未动 `6b4d37aa8460de432c6c2c1febd7044f`
- 白名单: batch json kb_files = NV/assumptions.md + NV/examples.md (assumptions.md 在 kb_files 内, 全文件适用 writer 规则)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-NV_writer/` (assumptions/examples .before.md, p285/286/294/296/297/298 渲染 110dpi, fwd.py, rev.py, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批: atoms 3 (REAL_GAP 3) / t2_recheck 0; census DIFF 1 表 (4 CELL, KB 行 17/18); pdf_only 0; out_of_scope 0.

### 页范围核对 (O20)
- NV 节 (§6.3.7.4) = p294 (节标题 + Description/Overview + spec 首句 + spec 表起) → p295 (spec 表续, 仅表) → p296 (spec 表末 + 脚注 + NV – Assumptions 1-2 + Examples Ex1 叙述 + nv.xpt) → p297 (suppnv + relrec + Ex2 叙述起) → p298 (Ex2 叙述续 + nv.xpt + 末段; 其后 §6.3.7.5 OE). batch lo/hi 294-298 **完整覆盖 NV 节**.
- NV/assumptions.md 承载的 §6.3.7 / §6.3.7.1 = p285 (§6.3.7 概述段 + §6.3.7.1 引言 + 5 条 bullet) + **p286** (通用规格表 title + 12 行 + 脚注; 其后 §6.3.7.2 CV). batch pdf_pages 含 285 但**不含 286**; 本批双向全扫覆盖 p285-286 + p294-298.
- p285 顶部 §6.3.6 MO 退役框不属 NV (见 F-1).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | NV/assumptions.md:5 | ig34_p0285_a009 | INSERTED | §6.3.7 概述段末补 "Additional domains for other body systems are expected …" 句 (原两句不动) | 285 |
| 2 | NV/assumptions.md:5 | ig34_p0285_a010 | INSERTED | 紧接 #1 补 "The CDISC Controlled Terminology of SDTM domain abbreviations … not yet in the SDTMIG." | 285 |
| 3 | NV/assumptions.md:36-38 | ig34_p0294_a013 | INSERTED | 新增 `## NV – Description/Overview` + p294 定义句 (位于 §6.3.7.1 后、NV – Assumptions 前; CM/MK 结构) | 294 |
| 4 | NV/assumptions.md:40-42 | spec 首句 (R3; ig34_p0294_a014-a016 同带) | INSERTED | 新增 `## NV – Specification` + "nv.xpt, Nervous System Findings — Findings. One record per finding per location per time point …" | 294 |
| 5 | NV/assumptions.md:15 | R3 新增 (§6.3.7.1 第 5 bullet) | INSERTED | 补 "CDISC Controlled Terminology includes codelists for TEST and TESTCD values for each body-system based domain." | 285 |
| 6 | NV/assumptions.md:17-34 | R3 新增 (§6.3.7.1 通用规格表, pdf_only 性质) | TABLE_REBUILT (新增整表) | 新增粗体 title 行 "--.xpt, Body System-Based Morphology/Physiology — Findings, Version 3.3. …" + 7 列表头 + 12 行 (STUDYID…--DY) + ¹ 脚注; 格式仿 LB §6.3.5.1 | 286 |
| 7 | NV/examples.md:17 | census:examples.md:17:1:NVORRES | REPLACED | `0.95` → `.95` (渲染图) | 296 |
| 8 | NV/examples.md:17 | census:examples.md:17:1:NVSTRESC | REPLACED | `0.95` → `.95` | 296 |
| 9 | NV/examples.md:17 | census:examples.md:17:1:NVSTRESN | REPLACED | `0.95` → `.95` | 296 |
| 10 | NV/examples.md:18 | census:examples.md:18:2:NVSTRESN | SKIPPED_PDF_TYPO | KB 保留 `1.17`; PDF 空 → T-2 | 296 |
| 11 | NV/examples.md:11 | R3 扫描 (ig34_p0296_a019) | SKIPPED_PDF_TYPO | KB 保留 "a fluorodeoxyglucose"; PDF "an fluorodeoxyglucose" → T-1 | 296 |

- 覆盖率自查: atoms 3 = #1-3 (全部 INSERTED); census 4 格 = #7-10; R3 新增 3 (#4-6); PDF_TYPO 登记 2 (#10-11).
- #6 依据: KB :12/:14 bullet 引用 "partial generic domain specification table … provided here", 而全 KB 无此表 (`grep -rn "Body System-Based Morphology/Physiology" knowledge_base` 改前 0 命中); NV/assumptions.md 在 kb_files 内; 先例 B-LB 在 LB/assumptions.md §6.3.5.1 补通用规格表整表. **若主控不认可, 回退 = 删 assumptions.md:16-34 (空行 + title + 表 + 脚注) 共 19 行, 其余改动独立.**
- #6 逐格依据 = p286 渲染图 (非照抄 LB 行): --SEQ 带 "(or within a parameter, in the case of the Trial Summary domain)"; --TEST 标签 "Name of Measurement, Test or Examination" (--TESTCD 为 "…Test or Exam"); "Subject to Domain-specific …" 大写 D 照录; --STRESC 注 "copied or derived from --ORRES in a standard format" 逗号位置照录; DOMAIN Controlled Terms 列 "--" (PDF 为超链接); Core 列: STUDYID/DOMAIN/USUBJID/--SEQ/--TESTCD/--TEST = Req, 其余 6 行 = Exp. PDF 单元格内换行 (TESTCD/TEST 的 "Subject to …" 另起一行) 合并为空格.

### census 表处理

| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:15 Ex1 nv.xpt (4 CELL) | #7-9 改; #10 PDF_TYPO | DIFF 1 (= T-2, 预期残留) |
| examples.md:28 / :48 / :74 | census OK; 渲染图 p297/p298 人工复核一致 | OK |
| assumptions.md:19 (新增通用规格表) | census **UNPARSEABLE** (无 Row 列, 非例表) | reviewer 须对 p286 渲染逐格人工核 |

### PDF_TYPO 清单 (依据 = PDF 自身)
- T-1 (p296 Ex1 "Rows 5-6" 说明): PDF "an fluorodeoxyglucose" 冠词错 (fluoro- 辅音开头); 按 dispatch "PDF 自身拼写错 KB 保留正确拼写" → KB 保留 "a fluorodeoxyglucose".
- T-2 (p296 Ex1 nv Row 2 NVSTRESN): PDF 空. 正确值由 PDF 自身确定: 同行 NVSTRESC = 1.17 (数值); 同表 Rows 1、3-6 NVSTRESN 均 = NVSTRESC; p286 通用表 --STRESC 注 "if results are numeric, they should also be stored in numeric format in --STRESN" → KB 保留 `1.17`.
- 非 TYPO 说明: #7-9 `.95` 无前导零 — PDF 原样 (Row 1 三列一致), 非可证错误, 照录 (同 B-BE QLABEL 先例 "风格差照录").

### 双向全扫 (含表格原子)
- PDF→KB (`python3 -I /private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-NV_writer/fwd.py`: work/pdf_atoms.jsonl p285-286 全部 + p294 a013 起 + p296-298 全部, 归一化引号/破折号空格/空白/`**`/表格竖线, 子串查 NV/assumptions+examples): 未命中仅 (a) p285 a001-a005 §6.3.6 MO (F-1); (b) p286 a015-a019 §6.3.7.2 CV、p298 a023-a025 §6.3.7.5 OE (他域); (c) p294 a017-a028 / p296 a001-a005 NV spec 表行 + 脚注 (属 spec.md, 白名单外, F-2); (d) p296 a009 "NV – Examples" 标题 (KB `# NV — Examples` 导航); (e) p296 a019 = T-1, a023 = T-2; (f) p297 a037 = 页界截断原子, 全句在 examples.md:63. p286 通用表 a001-a014 (title/表头/12 行/脚注) **全命中**.
- KB→PDF (`python3 -I /private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-NV_writer/rev.py`: 两文件逐行, 叙述按句、表格逐格, 对 p285-286 + p294-298 `pdftotext -raw` 归一文本): 未命中仅 (a) `# NV — Assumptions` / `## §6.3.7 … — Overview` / `## §6.3.7.1 …` / `# NV — Examples` 导航标题 (节号与标题文字均为 PDF 原标题, "— Overview" 为既有 KB 锚点文字, 规则 6 不改); (b) assumptions.md:32 --DY 注、:48 assumption 2 = PDF 折行 "sponsor-\ndefined" / "--\nLOINC" 归一假阳; (c) examples.md 日期格 = PDF 折行 "2012-05-\n22"; (d) examples.md:11 = T-1; (e) examples.md:63 = PDF 跨页 (p297→p298) 句. 无 KB 自写解释性内容 (D6 无), 无伪节号.
- 表格: Ex1 nv/suppnv/relrec (p296-297)、Ex2 nv (p298) 对 110dpi 渲染逐格人工核: 表头/列序/列数/Row 列一致, 除 #7-10 外 0 差. 新增 p286 通用表逐格对 p286 渲染.
- 仅格式差 (未改, 同 B-ch08/B-ch02 先例, T1 ledger 判 EQUIVALENT): examples.md:37 "records — specifically" 与 :61 "eye — including … (75-100) — are" (PDF em dash 两侧无空格; p297_a009/a032); :61 "subject's" 直撇号 (PDF 弯撇号 ’). PDF 自身 "may included" (assumptions.md:13)、:13 句末无句点、"links the each" (examples.md:63) 均照录.

### 新增 atom 清单 (R3)
- #4 NV spec 首句 (+ `## NV – Specification` 小标题); #5 §6.3.7.1 第 5 bullet; #6 §6.3.7.1 通用规格表整表 (title + 12 行 + 脚注).

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:17 三格 `0.95` | 同行 `.95` | VALUE_DIFF 旧值替换 (#7-9) | — |

### 范围外发现
- F-1 (需主控定): p285 §6.3.6 Morphology (MO) "Domain Decommissioning Update" 框 (标题 + 3 句/段: MO 自 v3.4 退役 / SDS Team 背景 / 新旧版本并存时的表示) 全 KB 无 (`grep -rln "decommissioned as of SDTMIG v3.4" knowledge_base` = 0). 不属 NV 节, 未补; 需主控定宿主 (无 MO 域目录; 候选 NV/assumptions.md §6.3.7 前或 ch 级文件).
- F-2: NV/spec.md (p294-296 spec 表 + 脚注) 白名单外, fp 无命中 → 归 O15 spec 扫描; spec.md 顶部 "> Class: Findings | Structure: …" 为 KB 摘要行 (与 PDF 首句不矛盾).
- F-3: 其他体系域 (CV/MK/OE/RE/UR…) 的 assumptions 未承载 §6.3.7.1 通用表交叉引用 — 仅记录, 不建议改.

### 触碰的 unparseable 表
- NV/assumptions.md:19 新增 p286 通用规格表 (census UNPARSEABLE): **reviewer 必须对 p286 渲染逐格人工核** (12 行 × 7 列 + title + 脚注).

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-NV_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-NV.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # NV: OK 3 / DIFF 1 (examples.md:18 NVSTRESN = T-2) / UNPARSEABLE 1 (assumptions.md:19 新表)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p028[56]|p029[4-8]|NV/' $S/fp_regress.jsonl   # 0 (全量 regress 中 p0363_a019/p0364_a001 为他批)
python3 -I $S/fwd.py; python3 -I $S/rev.py   # 未命中项见上文双向全扫
for p in 285 286 294 296 297 298; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```
- fp 对比 (p285-286, p294-298, hit_target/hit_any vs baseline): 0 丢失; 新命中 a009/a010 (hit_any NV/assumptions)、p294 a013/a015/a017/a018/a020、p295_a020、p296_a005/a022 等; verdict 字段为 ledger 静态值, 0 变化.

### git diff --stat
```
 knowledge_base/domains/NV/assumptions.md | 30 +++++++++++++++++++++++++++++-
 knowledge_base/domains/NV/examples.md    |  2 +-
 2 files changed, 30 insertions(+), 2 deletions(-)
```
