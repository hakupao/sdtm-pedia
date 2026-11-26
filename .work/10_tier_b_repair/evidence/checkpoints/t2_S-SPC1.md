# T2S S-SPC1 writer checkpoint (扫描批: CP / GF / IS / LB)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `056d8cc`; 本批 12 文件改前与 HEAD 一致 (`cmp` 0 差). scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPC1_writer/`
  (base/ = `git show HEAD:` 副本; apply.py 精确替换 + 命中次数断言; lscan.py 仅用 layout 文本的双向扫 (k2p / p2k, 去页脚, 不用原子); speccmp.py bbox 分列逐变量逐字段; grid.py bbox 逐格表比对 (ex / spec 两模式, 与 table_census.py 独立实现); scan.py/rscan.py/spec_cmp.py 原子法 (仅作初筛); r/ 渲染图)
- md5 after: CP/assumptions `e6b16e9df456b7a26f6e9baf2baec24d`, CP/spec `ac3cf2873aec709052cc2eda60d91734`, GF/assumptions `f666cd1384650e52a73abebefb494923`, GF/spec `d8e438b3dc7046019c6327f811044e18`, IS/assumptions `519cf2ea1da46c8a11b3fa2013083ee7`, IS/spec `63c8bce0863d81b17102cf046b0fea2e`, LB/assumptions `4240c7435cd72d8414a7d45bfc821671`, LB/spec `37e1316ab3ce9f25e89310029bb54889`; 4 个 examples.md 未动 (= HEAD).
- 方法注记: pdf_atoms 在本批页至少 12 处抽取错 (CPSCMRKS→CPCSMRKS、CPCELSTA notes、CPABCLID、CPCOLSRT、GFCHROM、ISSTNRLO、ISNRIND、LBLOINC Role、LBDRVFL、LB asm 2、p0228_a011、p0247 表行), 且原子法会让 KB 句因命中错误原子而"通过". 故终判一律用 layout 文本 (lscan.py) + bbox (speccmp/grid) + 渲染图; 原子法只作初筛.

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核 | 依据 |
|---|---|---|---|---|
| domains/CP | §6.3.5.3 | 199-220 | **199-220** (共享边界页 2 个) | p199 上部 bs.xpt (§6.3.5.2 BS, a001-a006) 不归本节, a007 标题起; p220 上部 Ex9 尾 (a001-a020) 属 CP, a021 `6.3.5.4` 起属 GF |
| domains/GF | §6.3.5.4 | 220-228 | **220-228** | p220 a021 起; p228 a001-a018 属 GF, a022 `6.3.5.5` 起属 IS |
| domains/IS | §6.3.5.5 | 228-241 | **228-241** | p228 a022 起; p241 a001-a020 属 IS (Ex11 尾), a023 `6.3.5.6` 起属 LB |
| domains/LB | §6.3.5.6 | 241-248 | **241-248** | p241 a023 起; p248 a001-a016 属 LB (Ex4/Ex5), a023 `6.3.5.7` 起属 MB |
- 本批 json 止页准确 (边界都在页中). LB/assumptions.md 顶部 §6.3.5 / §6.3.5.1 (B-LB 已终版, 源页 p194-196) 不在 241-248 内, 另以 p194-196 复扫 (见下) 并做 census_items 逐格.

### 双向全扫 — 逐页日志
方法: PDF→KB = `lscan.py p2k` (layout 段落→句, 在本域三文件中查, 空白不敏感) + 原子初筛; spec 表页以 speccmp.py (bbox 逐变量逐字段) 为准; 例表以 table_census + grid.py + 渲染为准. KB→PDF = `lscan.py k2p` (三文件逐句 vs 节页 layout 拼接) + spec 逐字段. 计数为改后.

| 页 | 节 | PDF→KB: 句/项/表行, 命中, 缺→已补 | KB→PDF: 对应 KB 段, 无出处→处理 | 表 (逐格/census) | 备注 |
|---|---|---|---|---|---|
| 199 | BS 尾 / CP Desc | 标题+13 句/项全命中; 0 缺 | CP/asm 1-28; :24 两处变量名改正 (T-21) | — (bs.xpt 别节) | 渲染 p199 确认 --BNDAGT/--GATEDEF 原样 |
| 200 | CP Desc 续 / Spec | 8 句 + 标题 + spec 首句 + 11 变量; 缺 2→2 (`## CP – Specification` + cp.xpt 句, gap S) | asm :30-44; :40 sting (T-17), :42 GATEDEF (T-21) | spec 11 变量逐字段一致 | 渲染: PDF 标题与 spec 句粘连 "Specificationcp.xpt" |
| 201 | Spec | 10 变量 | CPCELSTA Notes CPSMRKS→CPCSMRKS (T-20) | 逐字段一致 (CPGATE 跨页续行合并核过) | 渲染确认无 `*` |
| 202 | Spec | 16 变量 | 一致 | 逐字段一致 | 无 `*` |
| 203 | Spec | 23 变量 | 一致 | 逐字段一致 | 无 `*` |
| 204 | Spec 尾 | 6 变量 + 脚注; 缺 1→1 (脚注, gap F) | 一致 | 逐字段一致 | 脚注 → CP/spec.md:564 |
| 205 | Asm 1-6c | 17 项; asm 6 KB 多 "and CPMRKSTR" → 已删 | asm 4 KB CPCSMRKS vs PDF CPSCMRKS×3 = T-16b (KB 不动) | — | 渲染 p205 |
| 206 | Asm 6c-8d | 9 项; 8a `")"`→`"|"` 已改 | 6c CPBNDAGT (T-21), 7a CSMRKS (T-18), 8d CPSMRKS (T-19), 8d 两处未闭合引号 (T-16a, KB 不动) | — | 渲染 p206 |
| 207 | Asm 8e-8h | 14 项全命中 | 一致 | — | |
| 208 | Asm 9-10 / Examples / Ex1 | 全命中 | 一致 | — | |
| 209-219 | Ex1a-Ex9 | 叙述全命中, 余 = 已登记 T-1/T-2/T-3/T-4/T-15 | examples.md 全句有出处 (T-n 除外) | census: Ex1a/1b/3/4/5/7 OK; Ex2/6/8 DIFF = T-5/T-7/T-8a/T-8b/T-9/T-10 (渲染逐格见下) | B-CP 终版, 本次复核无新缺 |
| 220 | Ex9 尾 / GF Desc | CP 叙述 Rows 2-7/8-14 全命中; Ex9 表 | 一致 | Ex9 NO_PDF → grid.py 14×31 + 渲染 | GF 部分: 标题+3 句在 GF/asm:3-9 命中 |
| 221-223 | GF Spec | 57 变量 + 脚注; 缺 GFSYM `*` →已补; 脚注已迁入 spec.md (MOVED) | 一致 | speccmp 57/57 顺序一致, 非 CT 字段全一致 | 渲染 p221-223: 仅 GFSYM 一个 `*` |
| 223-224 | GF Asm 1-9 | 全命中 | :39 --ORNRHI = T-6 (B-GF 已改正, 沿用) | — | |
| 224-228 | GF Examples | 全命中 (余 T-1/T-3/T-4/T-5) | 一致 | census 全 OK 除 mb Ex5 (T-2, 渲染) | B-GF 终版 |
| 228 | GF 尾 / IS Desc | IS 标题+1 句命中 | IS/asm:1-5 | — | |
| 229 | IS Spec | 标题缺 1→1 (`## IS – Specification`); 17 变量; ISCAT/ISSCAT `*` 缺→已补 | 一致 | speccmp 逐字段 (STUDYID 首行 speccmp 跳过, 渲染+KB 对照一致) | |
| 230 | IS Spec | 21 变量 | 一致 | 同上 (ISORRES 首行渲染核一致) | 无 `*` |
| 231 | IS Spec 尾 / Asm 1-2 | 16 变量 + 脚注 (gap F) 缺 1→1; asm 2 "tests"→"trials" | 一致 | 逐字段一致 | 渲染 p231 |
| 232 | IS Asm 3-10 | 全命中; 7b "antigen panel"→"antigens panel" | 一致 | — | 弯引号差异归 S-TYPO |
| 233-241 | IS Examples | 全命中 (余 T-3/T-4/T-5) | examples.md 一致; asm 原 "Examples Notes" 附录与 examples.md 重复 → D2 去重 (S-2) | census 全 OK 除 Ex5 (T-1/T-2, 渲染) | B-IS 终版 |
| 241 | IS 尾 / LB Desc | LB 标题+2 句缺 → 已补 (gap D) | — | — | |
| 242 | LB Spec | 标题 + spec 首句缺 → 已补 (gap S); 17 变量; LBCAT/LBSCAT `*` 补 | 一致 | speccmp 逐字段一致 | 渲染 p242 |
| 243 | LB Spec | 17 变量 | 一致 | 一致 (LBCOLSRT 跨页续行合并核过) | 无 `*` |
| 244 | LB Spec | 22 变量; LBTOX/LBTOXGR `*` 补 | 一致 | 一致 | 渲染 p244 |
| 245 | LB Spec 尾 / Asm 1-7 | 6 变量 + 脚注 (缺→已补 LB/spec.md:564); asm 全命中 | 一致 | 一致 | |
| 246 | LB Asm 7-8 / Ex1 | 全命中 | 一致 | Ex1 census OK | |
| 247 | Ex1-Ex3 | 全命中 | 一致 | Ex2 OK; Ex3 DIFF 表头 = T-1 (渲染) | |
| 248 | Ex4-Ex5 / MB | LB 部分全命中 | 一致 | Ex4/Ex5 OK | MB 起别节 |
| 194-196 | §6.3.5 / §6.3.5.1 (LB host 顶部) | — | LB/asm:3-52 逐句全在 p194-196 layout | 通用表 grid 29×7=203 格 0 差 + 渲染 | B-LB 终版, 复核无变化 |

- spec 非变量行 (`# XX — …`, `> Class|Structure`, `---`, `## Cross References`) 按 U8 导航, 不标 D6.
- CT C-code 记法 (U5) 与 DOMAIN CT (U6, CP/GF/IS/LB 四处 PDF 为域代码、KB 空) 本批未改, 留 S-CT.

### spec.md Controlled Terms `*` (bbox speccmp + layout grep ` \* ` + 渲染三法)
- CP 62 变量: PDF 无 `*` (渲染 p200-204 逐页看过). 改后无需改.
- GF 57: `*` 1 = GFSYM → 已补. IS 54: ISCAT, ISSCAT → 已补. LB 62: LBCAT, LBSCAT, LBTOX, LBTOXGR → 已补. 改后 speccmp 中 `PDF[*]` 未匹配 = 0.
- 其余非 CT 字段四域全一致 (仅 bbox 跨页续行/词序假差, 均对 layout 核过).

### census_items 逐格 (渲染 + grid.py bbox 独立复核)
| 表 | 渲染 | grid.py | 结果 |
|---|---|---|---|
| CP/examples.md:85 Ex2 p211-212 | 160dpi 左右裁切 | 11×25=275 格, 差 1 | 仅 r6 CPDTC (PDF T04:20 / KB T12:20) = T-5; 其余一致 |
| CP/examples.md:206 Ex6 p216-217 | 150dpi 4 块 | 32×27=864 格, 差 29 | r7 CPMRKSTR 尾 "CD1c" (T-7); r7-32 CPGATDEF "CD45LIN-" 26 格 (T-9); r29 CPTESTCD DCPSDC (T-8a); r31 CPSPTSTD "CD40 MdFI … Sub Count" (T-8b); 其余一致 |
| CP/examples.md:279 Ex8 p219 | 160dpi 左右 | 11×32=352 格, 差 1 | r11 CPSTRESU PDF MdFI / KB % = T-10 |
| CP/examples.md:311 Ex9 p220 (NO_PDF) | 160dpi 左右 | 14×31=434 格, 差 2 | r1 CPORRES 85/83 (T-11); r13 CPANMETH "Total." (T-12); r4 "(Target Free) -(" 空格 (T-13, grid 去空白不计); 表头 `ROW` / `CPTST PNL` (T-14) |
| GF/examples.md:143 Ex5 mb p227 | 160dpi | 1×16, 差 1 | MBTEST "Idenitifcation" = T-2 |
| IS/examples.md:113 Ex5 p236 | 160dpi | 7×22=154 格, 差 2 | r6/r7 STUDYID RSC1230 = T-1/T-2 (grid 末行界 +14 时会吸入表下叙述词, 为抽取界限, 非表内容) |
| LB/assumptions.md:20 通用表 p195-196 (UNPARSEABLE) | 160dpi 3 块 | spec 模式 29×7=203 格, 差 0 | 逐格一致 (含 `*` 13 格、DOMAIN `--`、--DTC ISO 8601) |
| LB/examples.md:67 Ex3 p247 | 160dpi | 2×29=58 格, 差 0 + 表头 | 表头 PDF `LBSTRNHI` / KB `LBSTNRHI` = T-1 |
- table_census.py (pdf_ranges) before = after: `OK 31 / DIFF 6 / NO_PDF 1 / UNPARSEABLE 1, cells 6379, diffs 35` — 35 = CP T-5(1)+T-7/8/9(29)+T-10(1), GF T-2(1), IS T-1/T-2(2), LB T-1(1). 本批节内 PDF_ONLY 0 (p199 bs.xpt 属 BS).

### 变更清单 (行号 = 改后)
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | CP/assumptions.md:46-48 | ig34_p0200_a009/a010 | INSERTED | `## CP – Specification` + cp.xpt 首句 (gap S, CM/DS 先例位置) | 200 |
| 2 | CP/assumptions.md:62 | ig34_p0205_a007 | REPLACED | asm 6 "CPTEST and CPMRKSTR depends" → "CPTEST depends" (删多出 3 词) | 205 |
| 3 | CP/assumptions.md:79 | ig34_p0206_a006 | REPLACED | 8a `")"` → `"|"` | 206 |
| 4 | CP/assumptions.md:40 | T-17 (p0200_a006) | REPLACED | "marker sting" → "marker string" | 200 |
| 5 | CP/assumptions.md:75 | T-18 (p0206_a003) | REPLACED | 7a "CSMRKS" → "CPCSMRKS" | 206 |
| 6 | CP/assumptions.md:82 | T-19 (p0206_a009) | REPLACED | 8d "CPTEST, CPSMRKS, and CPCELSTA" → "CPSBMRKS" | 206 |
| 7 | CP/assumptions.md:24,42,72 | T-21 (p0199_a020, p0200_a007, p0206_a001) | REPLACED | "--BNDAGT"→"--BDAGNT", "--GATEDEF"→"--GATDEF" ×2, "CPBNDAGT"→"CPBDAGNT" | 199/200/206 |
| 8 | CP/spec.md:120 | T-20 (p0201 CPCELSTA) | REPLACED | Notes "CPCELSTA and CPSMRKS" → "CPCSMRKS" | 201 |
| 9 | CP/spec.md:564 | ig34_p0204_a013 | INSERTED | spec 脚注 (U2/U7: `---` 后、Cross References 前) | 204 |
| 10 | GF/spec.md:519 | ig34_p0223_a012 | MOVED | 脚注由 GF/assumptions.md:15 迁入 (先插后删) | 223 |
| 11 | GF/spec.md:257 块 | pdf:p222:GFSYM CT | REPLACED | CT 空 → `*` | 222 |
| 12 | IS/assumptions.md:7 | ig34_p0229_a001 | INSERTED | `## IS – Specification` 标题 (is.xpt 句已在) | 229 |
| 13 | IS/assumptions.md:15 | ig34_p0231_a019 | REPLACED | asm 2 "allergy tests" → "allergy trials" | 231 |
| 14 | IS/assumptions.md:27 | ig34_p0232_a007 | REPLACED | 7b "mixed antigen panel" → "mixed antigens panel" | 232 |
| 15 | IS/assumptions.md:39-41 | 结构 S-2 | DELETED | "IS – Examples Notes" 附录 22 行 → 一行交叉引用 (D2 去重) | 233-241 |
| 16 | IS/spec.md:149/158 块 | pdf:p229:ISCAT/ISSCAT CT | REPLACED | CT 空 → `*` ×2 | 229 |
| 17 | IS/spec.md:492 | ig34_p0231_a016 | INSERTED | spec 脚注 (gap F) | 231 |
| 18 | LB/assumptions.md:54-56 | ig34_p0241_a024/a025 | INSERTED | `## LB – Description/Overview` + 2 句 (gap D) | 241 |
| 19 | LB/assumptions.md:58-60 | ig34_p0242_a001/a002 | INSERTED | `## LB – Specification` + lb.xpt 首句 (gap S) | 242 |
| 20 | LB/spec.md:113/122/392/401 块 | pdf:p242/p244 CT | REPLACED | LBCAT/LBSCAT/LBTOX/LBTOXGR CT 空 → `*` | 242/244 |
| 21 | LB/spec.md:564 | ig34_p0245_a007 | INSERTED | spec 脚注 (LB/assumptions.md:52 通用表脚注保留不迁) | 245 |
- 新增 atom 清单 (gaps 之外, 全扫发现): #2 #3 #4-#8 #12 #13 #14 #11/#16/#20 (CT `*`).

### 结构改动清单 (reviewer 逐条签字)
| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| S-1 | CP/asm:46, IS/asm:7, LB/asm:54/58 | 新增 `## CP – Specification` / `## IS – Specification` / `## LB – Description/Overview` / `## LB – Specification` 标题 | PDF 标题原子 p200 a009 / p229 a001 / p241 a024 / p242 a001; DS (S-EVT) 先例 |
| S-2 | IS/assumptions.md 旧 :39-62 | 4 个 `###` 小节 + 16 行叙述 → `> See [IS/examples.md](examples.md) for these narratives (…)`; `## IS – Examples Notes` 标题保留 (规则 6) | dispatch notes "KB 自写附录与 PDF 内容重复 → 留 PDF 所属节那份, 附录处一行交叉引用"; CP D-19 先例. 逐条保留副本见删除清单. 全库 grep 无链接指向被删 `###` 锚点 |
| S-3 | GF/assumptions.md 旧 :15-16 | spec 脚注 + 空行删除 (已迁 GF/spec.md:519) | U2 footnote_moves |

### 删除清单
| # | 原位置 (base) | 原因 | 保留副本 (IS/examples.md, 改后行号) |
|---|---|---|---|
| D-1 | IS/asm:39-43 Ex1 Row 1-3 | D2 去重 | Ex1 Row 1/2/3 叙述 (`norm(body) in examples.md` = True) |
| D-2 | IS/asm:45-47 Examples 8–9 引句 | D2 去重 | 同上 True |
| D-3 | IS/asm:49-54 Ex10 引言 + Rows 1-5 + Rows 6-11 | D2 去重 | True; Rows 1-5 附录为 PDF 原拼写 "nucleoar", examples.md:215 为 "nucleolar" (B-IS T-4 KB 正确值) — 唯一差异 |
| D-4 | IS/asm:56-62 Ex11 Row 1 / Rows 2-9 | D2 去重 | True |
| D-5 | GF/asm:15-16 脚注 | MOVED (先插后删) | GF/spec.md:519 |
| D-6 | CP/asm:62 "and CPMRKSTR" (3 词) | PDF 无 (授权 1) | — |
| D-7 | #3-#8, #11/#13/#14/#16/#20 旧值 | VALUE_DIFF / T-n 改正旧值替换 | — |

### D6 / KB_AUTHORED
- 无新增 D6. 纯导航保留不标: CP/asm:102-104 `## CP – Example Narrative Atoms …` + 交叉引用 (B-CP 已裁), GF/asm:41 `> See [Example 4]…` 交叉引用, IS/asm:39-41 新交叉引用, spec.md `> Class|Structure` 行与 Cross References (U8).

### PDF_TYPO (沿用 B-CP/B-GF/B-IS/B-LB 编号; CP 新增 T-16..T-21)
- 沿用复核仍成立: CP T-1..T-15 (census/grid/渲染复核 T-5/T-7/T-8a/T-8b/T-9/T-10/T-11/T-12/T-13/T-14); GF T-1..T-6 (T-2 渲染复核); IS T-1..T-6 (T-1/T-2 渲染复核); LB T-1 (渲染复核).
| T | 位置 | PDF | KB | 处理 | 依据 |
|---|---|---|---|---|---|
| CP T-16a | asm 8d (CP/asm:82) | `"CD3+CD19- (T lymphocyte)`、`"CD278+ (activated)` 引号未闭合 | 闭合 | KB 不动 | 同句平行项 "CD45" / "CD4+CD8-" / "CD197+CD45RA-" 均闭合; 渲染 p206 |
| CP T-16b | asm 4 (CP/asm:58) | CPSCMRKS ×3 | CPCSMRKS | KB 不动 (原子误作 CPCSMRKS 掩盖) | spec 变量 CPCSMRKS; 渲染 p205 |
| CP T-17 | CP/asm:40 | "marker sting" | "marker string" | 改正 | 同节 "marker string" 多处; PDF 自身拼写错 (B-GF T-3 先例) |
| CP T-18 | asm 7a (CP/asm:75) | "CPCELSTA and CSMRKS" | CPCSMRKS | 改正 | 同段其后 3 处均 "CPCELSTA and CPCSMRKS"; spec |
| CP T-19 | asm 8d (CP/asm:82) | "CPTEST, CPSMRKS, and CPCELSTA" | CPSBMRKS | 改正 | spec CPMRKSTR Notes "combination of CPTEST, CPSBMRKS, and CPCELSTA" |
| CP T-20 | CP/spec.md:120 CPCELSTA Notes | "CPCELSTA and CPSMRKS, in combination with … CPTEST and CPSBMRKS" | CPCSMRKS | 改正 | 同句已列 CPSBMRKS, 余者只能是 CPCSMRKS; asm 4 "CPCELSTA is used in conjunction with CPCSMRKS" |
| CP T-21 | CP/asm:24 ×2, :42, :72 | --BNDAGT, --GATEDEF ×2, CPBNDAGT | --BDAGNT, --GATDEF, CPBDAGNT | 改正 | spec 变量 CPBDAGNT/CPGATDEF (p201/p202); p208 a009 列 "CPBDAGNT (Binding Agent) … CPGATDEF (Gate Definition)"; 与 T-15 (CPGATEDEF→CPGATDEF) 同口径 |
- T-21 动了 Description 段的泛型变量名 (--XXX), reviewer 若认为 "--" 泛型名不适用取舍规则, 可回退为照录 + T4 (见需主控定 #1).

### fp_match (预登记回归)
- `fp_match.py --baseline work/fp_baseline.jsonl` 对 `t2_fp_expected_regressions.jsonl` 差集 7 条: 本批 6 条均为预期 = ig34_p0199_a020 (T-21), p0200_a006 (T-17), p0200_a007 (T-21), p0206_a001 (T-21), p0206_a003 (T-18), p0240_a004 (S-2 删附录; 该原子 PDF 原文 "nucleoar", 唯一承载处是被删附录, examples.md 为 T-4 改正值). 第 7 条 ig34_p0255_a021 (p255 MB) 非本批文件, 为并行批.

### 范围外 / out_of_scope
- out_of_scope[] 空. 新范围外: 无.
- 原子抽取错 (供 T3 台账): ig34_p0205_a005 (CPSCMRKS 被写成 CPCSMRKS), p0201_a005/a010, p0202_a024, p0222_a006, p0230_a009/a012, p0243_a015, p0244_a007, p0245_a010, p0228_a011, p0247_a005/a012-a014/a021/a022, p0220_a007-a020 (CP Ex9 行被误归 spec 形).

### 需主控定
1. T-21 (Description 中泛型名 --BNDAGT/--GATEDEF 改为 --BDAGNT/--GATDEF): 按取舍规则已改并登记; 若主控认为 Description 层泛型名应照录, 回退 4 处 (apply.py 第 1/2/4/7 对).
2. U6 (DOMAIN CT 4 处) / U5 (C-code) 留 S-CT, 本批未动.

### 验证命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPC1_writer
K=knowledge_base/domains
python3 -I $S/lscan.py k2p CP 199 220 $K/CP/assumptions.md $K/CP/examples.md   # 残留 = T-n / 导航行 (GF/IS/LB 同法, 页范围见上)
python3 -I $S/lscan.py p2k IS 228 241 $K/IS/assumptions.md $K/IS/examples.md $K/IS/spec.md
python3 -I $S/speccmp.py $S LB 242,243,244,245     # 需 $S/bb_<p>.html (pdftotext -bbox); 残留仅 CT C-code/DOMAIN (U5/U6)
python3 -I $S/grid.py $K/CP/examples.md 311 220 ex ; python3 -I $S/grid.py $K/LB/assumptions.md 20 195,196 spec
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 31 / DIFF 6 / NO_PDF 1 / UNPARSEABLE 1; diffs 35 = 全 T-n
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 knowledge_base/domains/CP/assumptions.md | 20 ++++++++++++--------
 knowledge_base/domains/CP/spec.md        |  4 +++-
 knowledge_base/domains/GF/assumptions.md |  2 --
 knowledge_base/domains/GF/spec.md        |  4 +++-
 knowledge_base/domains/IS/assumptions.md | 31 +++++--------------------------
 knowledge_base/domains/IS/spec.md        |  6 ++++--
 knowledge_base/domains/LB/assumptions.md |  8 ++++++++
 knowledge_base/domains/LB/spec.md        | 10 ++++++----
 8 files changed, 41 insertions(+), 44 deletions(-)
```
