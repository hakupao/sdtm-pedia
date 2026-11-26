# T2 B-OE reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base: fb87b40; 审查对象 `git diff fb87b40 -- knowledge_base/domains/OE/` (仅 OE/examples.md, +19/-9; 工作树其他 M 文件属他批, 不在本审范围)
- scratch (仓外): `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-OE_reviewer/` (p301-305 130dpi 渲染图, layout.txt, census_after.json, fp_after.jsonl, fp_regress.jsonl, rev.py, scan.py, links.txt)

### 命令与结果 (可复跑, 在 repo 根执行)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-OE_reviewer
pdftoppm -f 301 -l 305 -r 130 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p     # 渲染, 逐格人工核
pdftotext -layout -f 301 -l 305 "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/layout.txt   # 独立方法 (layout 列位)
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  # exit 1; KB tables 12, OK 10 / DIFF 2, cells 694, diffs 5 (= T-1 1 + T-2 4); 本批范围 PDF_ONLY 仅 p298 nv.xpt (NV 域, 非 OE)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # RESULT: RED, regress 42 行; grep -c "OE/" = 0; grep -c '"ig34_p030[0-5]' = 0 (全为他批 §6.4.2 等)
python3 -I $S/scan.py      # PDF 原子 p301-305 → KB (norm 子串)
python3 -I $S/rev.py $S/layout.txt   # KB 叙述/结构行 → PDF layout (norm 子串); 全部 OK, 0 MISS
python3 tools/check_links.py | grep "live docs"   # broken relative links: 18668 (live docs: 42) = 基线 42; OE/examples.md 无坏链
```
- rev.py 变异验证: "upon installation of a lubricant" → False, "upon instillation …" → True (扫描器能抓单词差异).

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| 交接说明 "5 个原子错" | 完整 | 实为 6 条 (p301_a017, a018, p304_a020-a023), writer checkpoint 写的也是 6; 均确认是原子抽取错, KB 正确 | 见下 |
| writer fp regress "41" | 证据 | 本次复跑 42 (多出 1 条来自他批并行改动), OE 相关 0 → 不影响本批 | fp_regress.jsonl |
| 无阻断问题 | — | — | — |

### 人工逐格核 (渲染图 + layout 列位独立复核; 12 表)
| KB 表 (行号) | PDF 页 | 结果 |
|---|---|---|
| :12 Ex1 oe.xpt 3×19 | 302 | 一致; OEMETHOD r1-3 = "SLIT LAMP" (渲染图), #1-3 正确 |
| :22 Ex1 suppoe 2×9 | 302 | 一致; r1 QNAM "OEDIR1" (#4) |
| :42 Ex2 oe 8×21 | 302 | 一致 (SLIT LAMP BIOMICROSCOPY r1-4 = PDF; HYPERMIA = PDF; 未动) |
| :57 Ex2 suppoe 2×9 | 303 | 一致 |
| :75 Ex3 oe 6×22 | 303 | 一致; r1 OECLSIG "Y" (#5), r2 OELAT "RIGHT" + OECLSIG "N" (#6/#7) |
| :88 Ex3 suppoe 2×9 | 303 | 一致 |
| :98 Ex3 pr 5×17 | 303-304 | 一致; r3 PRSTDTC "2012-05-25T08:00:00" (#8), r4 08:30:00 未动 = PDF |
| :110 Ex3 di 4×8 | 304 | 一致 |
| :121 Ex3 relrec 2×8 | 304 | 数据格一致; 表头 col6 PDF "IDVARAL" → KB IDVARVAL (T-1) |
| :140 Ex4 oe 4×21 | 304 | 一致, 除 OECAT ×4 PDF "OCCULAR COMFORT" → KB OCULAR (T-2); OESEQ 1/2/1/2 = PDF (U-1) |
| :151 Ex4 suppoe 1×9 | 305 | 一致; QLABEL "Result Criteria" (#11) |
| :159 Ex4 ae.xpt 3×19 (新) | 305 | 逐格一致 (57 格): 19 列序 = PDF 表头; r1 FOCID 空, AESEQ 5, AESPID 1, Headaches/Headache/Nervous system disorders, AELOC/AELAT 空, MILD, N, DOSE NOT CHANGED, NOT RELATED, RECOVERED/RESOLVED, 2011-05-02, 2011-05-06; r2 OD 6 2 … RIGHT MODERATE … 2011-05-03 / 2011-05-05; r3 OS 7 2 … LEFT … 2011-05-03 / 2011-05-04. layout.txt 行 198-204 复核同 |

### PDF_TYPO / 照录判定 (按 "可由 PDF 自身确定" 规则)
| # | 判定 | 依据 |
|---|---|---|
| T-1 relrec 表头 IDVARAL → IDVARVAL | 同意 (KB 正确值 + 登记) | RELREC 标准变量名; 同文件 supp 表头均 IDVARVAL; 表头拼写印刷错口径 |
| T-2 OECAT "OCCULAR COMFORT" → OCULAR | 同意 | p305 suppoe IDVAR=OECAT, IDVARVAL "OCULAR COMFORT" 必须等于 OECAT 值 |
| U-1 Ex4 OESEQ 1/2/1/2 照录 + T4 | 同意 | 同 USUBJID 内重复违反 --SEQ 唯一, 但正确编号 (3/4 或其他) PDF 无法确定 → 照录 |

### 叙述增改 (vs PDF 渲染)
| 行 | 动作 | 判定 |
|---|---|---|
| :147 | D-1: 删 KB 改写句 "The suppoe.xpt dataset represents the scale used for…", 换 PDF 原句 | 逐字一致 (p305 首句 "The numeric scale used in grading ocular comfort is described in a supplemental qualifier dataset."); 删除确认 |
| :155 | 新增 AE 引导段 2 句 | 逐字一致 (p305 "Adverse events affecting the eyes are represented in the AE domain. For events that affected only 1 eye…"), 位置 = suppoe 表后、ae.xpt 前, 同 PDF |

### 原子错核实 (渲染为准)
- p301_a017: 原子含 "OEDTC=\"2012-01-19\"", 渲染为 "…examination, using OETESTCD=\"INTP\". OELOC indicates…" → 原子错, KB:7 = PDF.
- p301_a018: 原子缺 "OEORRES and OESTRESC. This" 与 "spot" (串行乱码) → 原子错, KB:8 = PDF.
- p304_a020-a023: 原子 "installation", 渲染 Row 1-4 均为 "instillation" / "post-instillation" → 原子错, KB:133-136 = PDF.

### 双向全扫 (p301 "OE – Examples" 至 p305 "6.3.7.6" 前, 含表格原子)
- PDF→KB: 叙述原子 (Example 1-4 引导/bullet/Rows 说明/表间句) 全部命中, 未命中仅 6 条原子错 (上)、OE Assumptions 3 条 (属 assumptions.md)、RP 节 (p305 a011 起, 非本域). 表格原子 MISS 均为原子抽取噪声 (如 a003 FOCID OD/OESEQ 2、a015 FOCID OD、a029-a031 时间/DCT、p305_a008 USUBJID "XYZ-100-5"), 已逐条对照渲染图确认 KB = 渲染图.
  另对渲染图逐页人工通读 p301-305 例子部分: 无遗漏句.
- KB→PDF: 全文件 54 条非表行 (标题/表标签/叙述/bullet) 全部在 layout 文本中命中 (rev.py 0 MISS); 无 KB 自写解释性内容, 无需 D6.

### G-TB6 结构行签字
- :157 `**ae.xpt**` = PDF 表标签 "ae.xpt" (p305) ✔; :159 表头 19 列 = PDF ✔; :160 分隔行 (结构) ✔; 其余结构行 (`# OE — Examples` = PDF "OE – Examples", `## Example 1-4`, 各 `**xxx.xpt**`) 未改, 对应 PDF ✔.
- 新增/改动行 19 条全部有出处, 无出处 0.

### 无副作用
- OE 目录 diff 只涉及 examples.md (白名单); 无标题/锚点改动; 未改动的已正确表行未受影响 (diff 仅限上列 #1-14).
- 范围外 O-OE-1 (OE/assumptions.md 缺 Description/Overview + spec 首句) 已登记 out_of_scope_findings.md O23, 不阻断.
