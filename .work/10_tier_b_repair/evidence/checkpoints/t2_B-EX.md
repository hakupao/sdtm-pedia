# T2 B-EX writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `470b47383791f30c585059f8d324fb09e2ce1066`
- kb_files: `knowledge_base/domains/EX/examples.md` — md5 before `468ca4ccebe4f8a1a37f5605117fb07b` (435 行) → after `f0a7e49a6c359de9261b85bb4f349a4c` (459 行)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-EX_writer/` (examples.base.md 原件, build.py 锚定替换脚本 (每处 assert 唯一/定数命中), examples.new.md, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl, 渲染 p112/p115-p119 @130dpi, p118crf @220dpi)
- 真值来源: `work/pdf_pages/ig34_p0111-0120.txt` (layout) + 渲染图. **未采用 atom verbatim** (p116 a010-a031 / p117 a001-a002 / p118 a002-a029 均为编造或走样: 如 ECDOSU 全写 TABLET, COATED、行 13-24 USUBJID 写成 56789001、p118 ec 行 2 ECDOSE 9.9 mg/kg 等; lane B 已注).
- 规则依据: writer v1.0 规则 1/2/3/5; dispatch notes「补充口径 (B-CP 后)」(PDF_TYPO 取舍、词替换恢复、KB 自写导航保留).

### 变更清单 (atoms[] 10 条)

| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | EX/examples.md:344 | ig34_p0118_a005 | INSERTED (随 CRF 表重建) | Dose Administered 子行 "If no, give reason:" ×3 visit | 118 |
| 2 | :345 | ig34_p0118_a006 | INSERTED (随 CRF 表重建) | 子行 "Treatment discontinued due to disease progression" ×3 | 118 |
| 3 | :266 | ig34_p0116_a011 | REPLACED | Ex6 ec 行 2 ECDOSFRM CAPSULE → TABLET, COATED | 116 |
| 4 | :268 | ig34_p0116_a013 | REPLACED | 行 4 同上 | 116 |
| 5 | :270 | ig34_p0116_a015 | REPLACED | 行 6 同上 | 116 |
| 6 | :272 | ig34_p0116_a017 | REPLACED | 行 8 同上 | 116 |
| 7 | :274 | ig34_p0116_a019 | REPLACED | 行 10 同上 | 116 |
| 8 | :276 | ig34_p0116_a021 | REPLACED | 行 12 同上 | 116 |
| 9 | :346, :352-354 | ig34_p0118_a007 | TABLE_REBUILT | "Personal reason" 从 "If dose was adjusted…" 行 (V3) 移到 Dose Administered → **Other, specify:** Personal reason (V3); 末行补 Adverse event / Other, specify 选项 | 118 |
| 10 | :371 (+:369) | ig34_p0118_a027 | REPLACED + 列重排 | Ex7 ec 行 4 ECLNKID 20090220 → 20090220T1100 (行 2 同: 20090213 → 20090213T1000); 见 #16 | 118 |

atoms 覆盖: 10/10 (REAL_GAP 2, VALUE_DIFF 8). 原子文本里的其它值 (2.6 mg/kg、ECADJ 等) 与 PDF 不符, 不采用.

### 批内追加改动 (census / R3 / 补充口径, 非 atoms)

| # | kb_file:line (改后) | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 11 | :278-288 偶数行 | census:EX/examples.md:265 rows 14,16,18,20,22,24 | REPLACED | Ex6 ec 行 14-24 偶数行 ECDOSFRM CAPSULE → TABLET, COATED (渲染 p116/p117 确认, ECDOSU 原已正确) | 116-117 |
| 12 | :86-90 | census:EX/examples.md:86 (HEADER + rows 1-3) | REPLACED | Ex2 ec 补 VISITNUM 列 (ECLAT 与 VISIT 之间), 3 行值 = 3; 分隔行同步 | 112 |
| 13 | :298-323 | census:EX/examples.md:296 (HEADER + 42 CELL + 16 PDF_ROW_MISSING) | TABLE_REBUILT | Ex6 ex.xpt 8 行汇总 → PDF 24 行逐次给药; 加 EXELTM (EXTPT 与 EXTPTREF 间, 全 -PT30M); EXSTDTC 改为带时间; EXENDTC 全空 (照录 PDF, 见 T-5); EXSTDY=EXENDY 逐行 1/2/3/9/10/11; EXTRT/EXDOSE/EXDOSFRM/EPOCH 按渲染 p117 | 117 |
| 14 | :337-354 | (unparseable 表 base :319, Ex7 CRF) | TABLE_REBUILT | 表头 `| | Visit 1 | Visit 2 | Visit 3 |` → `| Visit | 1 | 2 | 3 |`; 每个选项一子行 (标签格空), **粗体 = PDF 粗体 (勾选项)**; 修正 KB 错: V3 Dose Administered Yes → **No**; Reason for Dose Adjustment 只 V2 勾选 (KB 原 V2+V3); V1 原空格补选项; "Personal reason" 归位; 末行标签补冒号; 补 Intended Dose 7.5 mg/kg、No、Adverse event、Other, specify 等选项. 格式说明: PDF 的填写下划线 "____" 未录 (避免 Markdown 强调误解析) | 118 |
| 15 | :366-373 | census:EX/examples.md:341 (HEADER + 14 CELL) | REPLACED | Ex7 ec 列序 ECADJ \| EPOCH \| VISITNUM \| VISIT → ECADJ \| VISITNUM \| VISIT \| EPOCH (按 PDF); EPOCH 值 "VISIT TREATMENT" → "TREATMENT" ×6; 分隔行同步; 行 6 ECLNKID 20090227 PDF 本无 T 时间, 未动 | 118 |
| 16 | :369 | census:EX/examples.md:341 row 2 ECLNKID | REPLACED | 20090213 → 20090213T1000 (census 的 "20090213 T1000" 空格是折行, 对照 p119 EXLNKID/VSLNKID 无空格) | 118 |
| 17 | :9 | ig34_p0111_a004 (新增 atom 清单) | REPLACED (词恢复) | `**CRF:**` → `**Exposure CRF:**` | 111 |
| 18 | :63 | ig34_p0112_a008 (新增 atom 清单) | REPLACED (词恢复) | `**CRF:**` → `**Exposure CRF**` (PDF 无冒号) | 112 |
| 19 | :92 | ig34_p0112_a030 (新增 atom 清单) | REPLACED (词恢复) | "because the location was common" → "because this location was common"; 该行只承载 a030 本身 | 112 |
| 20 | :237 | ig34_p0115_a028 (新增 atom 清单) | INSERTED | Ex6 引言后补 "The following CRFs show data for 2 subjects." (KB 只在 ch04 有, EX 缺) | 115 |
| 21 | :292, :294 | ig34_p0117 Rows 1-12 / Rows 13-24 | MOVED | 两条 Row 说明从 EC 句后/ec.xpt 前 (base :259, :261) 移到 "The EX dataset shows the unblinded administrations." 后、ex.xpt 前 (PDF p117 位置), 文字未改. **非 atoms 的 RELOCATE, 请 reviewer 确认** (理由: PDF 中两条说明属 EX 表, 且 ex.xpt 现为 24 行与 "Rows 1-24" 对应; 原 8 行表下 "Rows 13-24" 无对应行) | 117 |

新增 atom 清单 (R3): ig34_p0111_a004, ig34_p0112_a008, ig34_p0112_a030, ig34_p0115_a028.

### 删除清单 (reviewer 逐条确认)

| # | 位置 (base) | 内容 | 原因 | 保留位置 |
|---|---|---|---|---|
| D-1 | :259-262 | Rows 1-12 / Rows 13-24 说明 2 段 (+空行) | MOVED (#21), 非删除内容 | after :292-294 |
| D-2 | :298-305 | Ex6 ex.xpt 旧 8 行 | TABLE_REBUILT (#13) 被 PDF 24 行替换 | :300-323 |
| D-3 | :319-329 | Ex7 CRF 旧 11 行 | TABLE_REBUILT (#14) 被 PDF 结构替换; 旧值 "10 mg/kg / 7.5 mg/kg"、V3 Yes、"Injection site reaction / Personal reason" 与 PDF 矛盾 | :337-354 |

### census 表处理 (before 行号 → 处理)

| census ref | 处理 | after |
|---|---|---|
| :86 Ex2 ec.xpt (4 diffs) | #12 | OK |
| :265 Ex6 ec.xpt (12) | atoms #3-8 + #11 | OK |
| :296 Ex6 ex.xpt (59) | #13 整表重建 | OK (:298) |
| :341 Ex7 ec.xpt (15) | #15/#16 + atom #10 | OK (:366) |
| :380 Ex7 relrec.xpt (3, Row 标号) | T-1 PDF_TYPO, KB 保留 1-6 | DIFF 3 (:405, 预期) |
| pdf_only / pdf_unparsed | 本批无 | — |

- census after (manifest = EX/examples.md × ig34 p104-120): `KB 表 31: OK 19 / DIFF 1 / UNPARSEABLE 11, diffs 3`; 本页段 PDF_ONLY 0. before: DIFF 5, diffs 93.
- 残留 3 diffs 全为登记 PDF_TYPO T-1.

### 触碰过的 unparseable 表 (reviewer 须对渲染图逐格人工核)
- Ex7 CRF (base :319 → after :337-354): 对 p118 渲染 (220dpi crop) 逐格; 特别核粗体位置.
- 其余 10 张 unparseable 未改 (Ex1 :13/:19, Ex2 :65, Ex5 :173/:180/:187, Ex6 :241/:250 → after :243/:252, Ex8 :395/:399).

### PDF_TYPO 清单

| T | 位置 | PDF | KB 处理 | 依据 |
|---|---|---|---|---|
| T-1 | Ex7 relrec.xpt :405-413 (p119) | Row 列印成 1, 2, 6, 3, 4, 6 | KB 保留 1-6 | 同表连续编号 + 叙述 "Rows 1-3 / Rows 4-6" |
| T-2 | Ex7 Rows 1-3 说明 :399 (p119) | "using --LNKID, ." | KB 保留 "using --LNKID." | 多余逗号空格, 标点印刷错 |
| T-3 | Ex3 列表 :116 (p113) | "from ottles A, B and C" | KB 保留 "bottles" | 拼写错, 同列表其他项 "bottles" |
| T-4 | Ex5 :205 (p115) | "protocol specified unit" (无连字符) | KB 保留 "protocol-specified unit" | PDF 本节 p111/p113/p114/p118 均写 protocol-specified |
| T-5 | Ex6 ex.xpt EXENDTC 全 24 行 (p117) | 空 | **照录 PDF 空值; 登记为 T4 用户裁定项** | 疑 PDF 漏填: EXENDY 有值, EX Assumption 4b (p107) 要求点给药 EXSTDTC 复制到 EXENDTC, 同例 ec.xpt ECENDTC 有值; 但正确值不能由表格本身确定 → 不自填 |

### KB_AUTHORED (PDF 无对应, 纯导航, 不矛盾 → 保留)
- :3 "Note: Examples for EX and EC are shared in Section 6.1.3.3…" (PDF 节标题 "6.1.3.3 Exposure/Exposure as Collected Examples" 未单独成标题; 规则 6 不改标题).
- `**CRF:**` 于 Ex5 :169、Ex6 :239、Ex7 :333、Ex8 :418; `**Subject ABC123-0201**` :335.

### fp_match
```
S=<scratch>; python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # {'UNPARSEABLE': 11, 'OK': 19, 'DIFF': 1}; diffs: 3
python3 tools/check_links.py | tail -1   # live docs: 42 (基线 42)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
```
- regressions=13, **其中 EX (p104-120) 0 条**; 13 条为并行批 (ig34_p0215_a018 CP; p0257/p0258/p0260/p0263 MB 已登记的预期项), 非本批.
- 按设计仍不命中的 EX 原子 (正确 PDF / 原子走样): p0113_a011 (ottles, T-3), p0115_a009 (T-4), p0119_a011 (T-2), p0119_a017-a019 (Row 标号, T-1), p0116_a009-a031 / p0117_a001-a002 / p0118_a002-a029 (verbatim 编造, T3 回写 ledger 时须按 PDF 改).

### 范围外发现 (未改)
- O-a **EC/examples.md 是同一组 PDF 例子的副本 (census kb_duplicate=true), 带同样的错**: Ex2 ec 缺 VISITNUM (:32); Ex6 Rows 1-12/13-24 同样放在 ec 前 (:78); Ex7 ec EPOCH "VISIT TREATMENT" 且列序错 (:110-115). 是否按 D2 去重 (留一份 + 交叉引用) 或另开批修, 请主控/用户定.
- O-b Ex6 CRF 两张表 (:243/:252) 表头行 11 格而数据行 10 格 (多一个前导空格), "Period 1/Period 2" 对不上列; PDF 为 Period 1 跨 Day..End Date/Time 5 列. 未改 (unparseable, 非本批 census 项).
- O-c Ex7 引言 (:327) PDF 为两段 ("…7.5 mg/kg." / "The example CRF below…"), KB 合为一段; 文字一致, 未改.

### git diff --stat
```
 knowledge_base/domains/EX/examples.md | 119 ++++++++++++++++++++--------------
 1 file changed, 72 insertions(+), 47 deletions(-)
```

## attempt 1 续 (主控裁定后, 2026-11-26)

- md5: `f0a7e49a…` → `89f1a955a45627f18d252b4d1f139fb1` (461 行). **注意: :327 之后所有上文 after 行号 +2** (Ex7 引言拆段), 如 Ex7 CRF :339-356, Ex7 ec :368-375, relrec :407-415; :327 之前不变.

| # | kb_file:line | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 22 | :243-244, :252-253 | O-b (unparseable Ex6 CRF ×2) | REPLACED | 表头行去掉多余前导空格 (11→10 格), 分隔行 11→10 格; "Period 1" 落在 Day 列、"Period 2" 落在第 2 个 Day 列, 与 p115/p116 渲染一致; 数据行未动. reviewer 须对渲染逐格核 | 115-116 |
| 23 | :327-329 | O-c | REPLACED (拆段) | Ex7 引言按 p117 拆成两段 ("…7.5 mg/kg." / "The example CRF below…"), 文字不变 | 117 |
| 24 | :3 | D6 | REPLACED | KB 自写导航句 "Note: Examples for EX and EC are shared…" → `> KB note (not in SDTMIG): Examples for EX and EC are shared…` (不矛盾, 保留并标注) | — |
| 25 | :292, :294 | 原 #21 | **RELOCATE** (主控裁定, 不留指针) | Rows 1-12 / Rows 13-24 说明从 ec.xpt 前移到 EX 句后 (PDF p117 位置); 原 #21 / D-1 的 MOVED 改记为 RELOCATE | 117 |

- D6 其余: `**CRF:**` (Ex5 :169, Ex6 :239, Ex7 :335, Ex8 :420) 与 `**Subject ABC123-0201**` (:337) 为表前短标签 (导航, 非解释性内容), 未加 KB note 前缀; 如主控认为也须标注请指示.
- O-a 不在本批, 已转 B-EC.
- 复跑:
```
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after2.json   # {'UNPARSEABLE': 11, 'OK': 19, 'DIFF': 1}; diffs 3 (relrec :407, T-1)
python3 tools/check_links.py | tail -1   # live docs: 42
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after2.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress2.jsonl   # regress 13, EX (p104-120) 0
```
- git diff --stat: `knowledge_base/domains/EX/examples.md | 133 ++++++++------  1 file changed, 80 insertions(+), 53 deletions(-)`

## attempt 1 续 2 (auditor PASS 后主控补改, 2026-11-26)

- md5: `89f1a955…` → `f5643b21b9dff82d6bef884cb830273a` (461 行, 行号不变).

| # | kb_file:line | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 26 | :360 | ig34_p0118_a017 (T-6) | REPLACED (PDF_TYPO 取舍规则) | Ex7 Rows 1, 3, 5 说明 "Scheduled dose is represented in mg/mL." → "…in mg/kg." | 118 |

- PDF_TYPO 追加 **T-6**: p118 "Scheduled dose is represented in mg/mL" → KB 写 mg/kg. 依据: 同句前半 "intended dose levels (mg/kg)" + Ex7 ec.xpt 行 1/3/5 (SCHEDULED) ECDOSU = mg/kg, 正确值可由 PDF 自身确定.
- 预期回归 (因改正 PDF 笔误而不再命中): **ig34_p0118_a017** (verbatim 含 "mg/mL"; baseline hit_target = EX/examples.md, 现 None; EC/examples.md 也无此句). T3 回写 ledger 时按 T-6 处理.
- 复跑:
```
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after3.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress3.jsonl   # regress 15; EX (p104-120) 仅 ig34_p0118_a017 (预期); 其余 14 为并行批
python3 tools/check_links.py | tail -1   # live docs: 42
```
