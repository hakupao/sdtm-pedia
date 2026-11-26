# T2S S-SPC1 reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** (无 CRITICAL/HIGH/MEDIUM; 5 条 LOW 观察, 不阻断)

- 对象: `git diff HEAD -- knowledge_base/domains/{CP,GF,IS,LB}`. 8 文件 md5 与 writer 报告一致; 4 个 examples.md = HEAD. 授权范围: 本批 diff 只落在 kb_files (narrow_files 空); 工作树中 AG/DA/EC/EG/EX/MB/MS/OE/PC/PE/PP/PR/SS/UR 改动属别批, 未看.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPC1_reviewer/`
  自写脚本 (不复用 writer, 不用 pdf_atoms): `pscan.py` (layout 文本双向逐句, 去页脚, xpt/Row/节号处断句), `lspec.py` (spec 表按 layout 表头字符列位置分列, 逐变量逐字段比 spec.md; 与 writer 的 bbox speccmp 方法不同), `chk.py` (定点短语); 渲染 p195/p196/p201/p212/p219/p220(300dpi 三段)/p222/p227/p229/p236/p242/p244/p247.

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPC1_reviewer; K=knowledge_base/domains
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1; OK 31 / DIFF 6 / NO_PDF 1 / UNPARSEABLE 1; cells 6379; diffs 35 (全为已登记 T-n); 本批页 PDF_ONLY 仅 p199 bs.xpt (§6.3.5.2, 别节)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # exit 1 RED; 67 regress, 对 t2_fp_expected_regressions.jsonl 差集 6 (全本批, 见下)
python3 -I $S/pscan.py k2p 199 220 $K/CP/assumptions.md $K/CP/examples.md      # 356 句, MISS 22 = 新 T-16b/17/18/19/21 + 旧 T-1..T-4/T-15 + 2 导航行
python3 -I $S/pscan.py k2p 220 228 $K/GF/assumptions.md $K/GF/examples.md      # 101 句, MISS 5 = 旧 T-1/T-3/T-4/T-5 + 1 导航行; HYPH 1 = T-6
python3 -I $S/pscan.py k2p 228 241 $K/IS/assumptions.md $K/IS/examples.md      # 194 句, MISS 4 = 旧 T-4/T-5 + 2 导航行; HYPH 1 = T-3
python3 -I $S/pscan.py k2p 241 248 $K/LB/examples.md ; python3 -I $S/pscan.py k2p 194 248 $K/LB/assumptions.md   # 49/0; 48/3 (2 个 § 标题 + 通用表脚注上标 ¹)
python3 -I $S/pscan.py p2k <lo> <hi> <本域三文件 + 邻域文件>   # 输出 $S/p2k_{CP,GF,IS,LB}.txt; 非 spec 页残留 = 表格行 (census 覆盖) / 节号标题 / 已登记 T-n
python3 -I $S/lspec.py CP 200,201,202,203,204 ; python3 -I $S/lspec.py GF 221,222,223 ; python3 -I $S/lspec.py IS 229,230,231 ; python3 -I $S/lspec.py LB 242,243,244,245
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### 页范围复核 (O20)
同意 writer: CP 199-220 (p199 上部 bs.xpt 属 BS; p220 下部 §6.3.5.4 起属 GF), GF 220-228, IS 228-241, LB 241-248 (p248 §6.3.5.7 MB 起别节); LB host 顶部 §6.3.5/§6.3.5.1 另以 p194-196 复扫.

### 双向全扫 — 逐页 (reviewer 自己的计数)
| 页 | PDF→KB | KB→PDF | 表 | 结论 |
|---|---|---|---|---|
| 199 | CP 标题/Desc 7 段 + 4 bullet 全命中 (bullet 逐条定点核); New variables 句 = T-21 | CP/asm:1-30 全有出处; :24 T-21 | bs.xpt 别节 | 一致 |
| 200 | Desc 续 3 句 (sting=T-17, GATEDEF=T-21) + `CP – Specification` + cp.xpt 句 (gap S) | asm:32-48 有出处 | spec 11 变量逐字段 (lspec) | 一致 |
| 201-204 | spec 51 变量 + 脚注 | 逐字段一致; 唯一字段差 CPCELSTA Notes CPSMRKS→CPCSMRKS = T-20 (渲染 p201 确认 PDF 原文) | CT: PDF 无 `*` (layout 0 + 渲染 p201) | 一致 |
| 205 | asm 1-6c 全命中; asm 4 CPSCMRKS×3 = T-16b (KB 原已正确); asm 6 "CPTEST depends" (词级 #2) | 全有出处 | — | 一致 |
| 206 | 6c-8d: CPBNDAGT=T-21, CSMRKS=T-18, CPSMRKS=T-19, 未闭合引号=T-16a; 8a "|" (词级 #3) | 全有出处 | — | 一致 |
| 207-208 | asm 8e-10 + Examples 引言全命中 | 全有出处 | — | 一致 |
| 209-219 | 叙述全命中, 残留 = B-CP 已登记 T-1..T-4 / T-15 (CPGATEDEF 8 处) | 全有出处 | census Ex1a/1b/3/4/5/7 OK; Ex2/6/8 DIFF 全 T-n | 一致 |
| 220 | CP Ex9 叙述 (CPGATEDEF=T-15) + Ex9 表; GF 标题+Desc | 同 | Ex9 NO_PDF → 渲染逐格 (下) | 一致 |
| 221-223 | GF spec 57 变量 + 脚注 | 逐字段一致 | `*` 仅 GFSYM (layout + 渲染 p222) | 一致 |
| 223-224 | GF asm 1-9 全命中; --ORNRHI = T-6 | 全有出处 | — | 一致 |
| 224-228 | GF Ex1-5 叙述全命中, 残留 = T-1/T-3/T-4/T-5 | 全有出处 | census 10 表 OK, mb Ex5 DIFF = T-2 (渲染 p227) | 一致 |
| 228-231 | IS 标题/Desc + `IS – Specification` (新) + is.xpt 句; spec 54 变量 + 脚注 | 逐字段一致 | `*` ISCAT/ISSCAT (渲染 p229) | 一致 |
| 231-232 | IS asm 1-10 全命中 ("allergy trials" / "mixed antigens panel" 词级 #13/#14) | 全有出处; 原 Examples Notes 附录已删 (S-2) | — | 一致 |
| 233-241 | IS Ex1-11 叙述全命中, 残留 = T-3/T-4/T-5 | 全有出处 | census 13 表 OK, Ex5 DIFF = T-1/T-2 (渲染 p236) | 一致 |
| 241-245 | LB 标题 + Desc (gap D) + `LB – Specification` + lb.xpt 句 (gap S); spec 62 变量 + 脚注 | 逐字段一致 | `*` LBCAT/LBSCAT (p242) LBTOX/LBTOXGR (p244) 渲染确认 | 一致 |
| 245-248 | LB asm 1-8 + Ex1-5 全命中; p248 下部 MB 别节 | 全有出处 | census Ex1/2/4/5 OK, Ex3 表头 = T-1 (渲染 p247) | 一致 |
| 194-196 | §6.3.5/§6.3.5.1 叙述 + 通用表 + 脚注 | LB/asm:3-52 全有出处 | 通用表渲染逐格 (下) | 一致 |
- lspec 的其余 "DIFF" 输出均为 layout 解析假差 (跨页续行 CPGATE/ISDRVFL/LBCOLSRT、Notes 溢入 Core 列 ISSPCCND/LBANMETH、Role 与 CT 粘连 CPELTM/LBDTC/LBENDTC/LBRFTDTC/LBPDUR、LBSTNRC 三行标签), 逐条对 layout 原文核过一致.

### spec.md Controlled Terms 逐变量 (lspec 分类, 合计 = 变量数)
| 域 | 变量 | PDF `*` = KB `*` | PDF 空 = KB 空 | 字面值一致 | U5 codelist (范围外) | U6 DOMAIN (范围外) | 其他 |
|---|---|---|---|---|---|---|---|
| CP | 62 | 0 | 37 | 4 (CPLOINC LOINC; CPDTC/CPRFTDTC ISO 8601 datetime or interval; CPELTM ISO 8601 duration) | 19 | 1 | 1 = CPELTM 解析粘连, 人工核一致 (已计入字面 4) |
| GF | 57 | 1 GFSYM | 39 | 3 (GFDTC GFELTM GFRFTDTC) | 13 | 1 | — |
| IS | 54 | 2 ISCAT ISSCAT | 30 | 4 (ISDTC ISENDTC ISELTM ISRFTDTC) | 17 | 1 | — |
| LB | 62 | 4 LBCAT LBSCAT LBTOX LBTOXGR | 25 (+LBSTNRC 空, 人工) | 6 (LBLOINC LBELTM LBDTC LBENDTC LBRFTDTC LBPDUR; 后 4 解析粘连, 人工核) | 25 | 1 | — |
- `*` 7 格全部有 PDF 依据 (layout `Char *` 行 p222:1 / p229:2 / p242:2 / p244:2, 其余 11 页 0; 渲染 p222/p229/p242/p244 逐格确认), KB 无多余 `*`. CP 无 `*` 确认 (p200-204 layout 0, 渲染 p201).

### gaps / footnote / footnote_moves 逐项
| 项 | 位置 | 逐字 | 签字 |
|---|---|---|---|
| CP S (p200 a009/a010) | CP/asm:46-48, Description 末段后、`## CP – Assumptions` 前 (CM/DS 先例) | 标题 en dash 同 PDF; cp.xpt 句逐字 (PDF 版面粘连 "Specificationcp.xpt") | ✔ |
| CP F (p204 a013) | CP/spec.md:564, CPRFTDTC `---` 后、`## Cross References` 前 (U7) | 逐字 | ✔ |
| GF MOVED (p223 a012) | GF/asm 旧 :15-16 删; GF/spec.md:519 (U7 位置) | 逐字 | ✔ |
| IS F (p231 a016) | IS/spec.md:492 (U7) | 逐字 | ✔ |
| IS 标题 (p229 a001) | IS/asm:7, Desc 与 is.xpt 句之间 | 逐字 | ✔ |
| LB D (p241 a024/a025) | LB/asm:54-56, 通用表脚注后、Assumptions 前 | 2 句逐字 | ✔ |
| LB S (p242 a001/a002) | LB/asm:58-60 | 逐字 | ✔ |
| LB F (p245 a007) | LB/spec.md:564 (U7); LB/asm:52 通用表脚注 (p196) 保留 = 不同表的脚注, 正确 | 逐字 | ✔ |

### census_items 逐格 (渲染, 不采信 writer)
| 表 | 方法 | 结果 |
|---|---|---|
| CP/examples.md:311 Ex9 p220 (NO_PDF) | 300dpi 三段裁切, 14 行 × 31 列 = 434 格人工逐格 | 差异仅: r1 CPORRES PDF 85 / KB 83 (T-11); r13 CPANMETH PDF "Total." / KB 逗号 (T-12); r4 CPANMETH PDF "(Target Free) -(" 多空格 / KB 无 (T-13); 表头 PDF `ROW`、`CPTST PNL` / KB `Row`、`CPTSTPNL` (T-14). 其余一致 (USUBJID PDF 两行 "0001/00001" = KB "0001 00001") |
| LB/assumptions.md:20 通用表 p195-196 (UNPARSEABLE) | 170dpi 裁切 3 张, 29 行 × 7 列 = 203 格人工逐格 | 全一致; `*` 11 格 (--TESTCD --TEST --CAT --SCAT --ORRESU --STRESU --STAT --NAM --SPEC --METHOD --LOBXFL), DOMAIN `--`, --DTC ISO 8601 datetime or interval |
| CP/examples.md:85 Ex2 p211-212 | census 275 格 + 渲染 p212 裁切 | 唯一差 r6 CPDTC PDF 2020-08-16T04:20 (渲染确认) / KB T12:20 = T-5 |
| CP/examples.md:206 Ex6 p216-217 | census 864 格 + bbox 词计数 | 29 差 = T-7 (r7 CD1c) + T-8a (DCPSDC, p217 bbox) + T-8b + T-9 (CD45LIN- 词 p216 18 + p217 8 = 26 格) |
| CP/examples.md:279 Ex8 p219 | census 352 格 + 渲染 p219 裁切 | r11 CPORRESU `%` / CPSTRESU `MdFI` (渲染确认) / KB `%` = T-10 |
| GF/examples.md:143 Ex5 mb p227 | census 16 格 + 渲染 | MBTEST PDF "Idenitifcation" (渲染确认) = T-2 |
| IS/examples.md:113 Ex5 p236 | census 154 格 + 渲染 | r6/r7 STUDYID PDF RSC1230 (渲染确认), r2-r5 RSV1230, USUBJID 全 RSV1230-011 = T-1/T-2 |
| LB/examples.md:67 Ex3 p247 | census 58 格 + 渲染表头 | 表头 PDF `LBSTRNHI` (渲染确认) / KB `LBSTNRHI` = T-1 |
- 说明: 6 张 DIFF 表的非差异格采信 table_census (bbox, 项目工具, 非 writer 的 grid.py; 这些表本批未改); 差异格全部以渲染/bbox 复核 PDF 原值.

### 词级修正 / 结构 / 删除 逐条签字
| # | 改动 | PDF 依据 | 签字 |
|---|---|---|---|
| W-1 (#2) | CP asm 6 删 "and CPMRKSTR" → "general structure of CPTEST depends" | p205 l19 | ✔ |
| W-2 (#3) | CP asm 8a `")"` → `"|"` | p206 l25 `"/", "|")` | ✔ |
| W-3 (#13) | IS asm 2 "allergy tests" → "allergy trials" | p231 l49 | ✔ |
| W-4 (#14) | IS asm 7b "mixed antigen panel" → "mixed antigens panel" | p232 l21 | ✔ |
| S-1 | 新增 `## CP – Specification` / `## IS – Specification` / `## LB – Description/Overview` / `## LB – Specification` | p200 / p229 / p241 / p242 标题 | ✔ |
| S-2 / D-1..D-4 | IS/asm "IS – Examples Notes" 附录 16 非空行 (4 个 KB 自拟 `###` 标题 + 12 行叙述) → 1 行交叉引用 | 12 行叙述逐条 `norm in IS/examples.md` = True (Ex1 Row 1/2/3、Ex8-9 引句、Ex10 引言、Rows 6-11、Ex11 Row 1/2-3/4-5/6-7/8-9); Rows 1-5 唯一差 "nucleoar" → examples.md:215 "nucleolar" (B-IS T-4), 替换后 True. 4 个 `###` 为 KB 自拟标签, 全库无锚点引用 | ✔ |
| S-3 / D-5 | GF/asm 脚注 + 空行删 (已迁 spec.md) | U2 footnote_moves | ✔ |
| D-4 CT | 7 格 空 → `*` | 见 CT 表 | ✔ |
- G-TB6: 新增/改动行 41+/44- 全有 PDF 出处或为签字结构行 (4 个标题、4 个 `> ¹` 引用块前缀、IS 交叉引用行 = 导航); 无出处 0. D6: 本批无新增 D6, 也无应加未加.

### PDF_TYPO 依据核查 (新 T-16..T-21; 主控口径: 正确值可由 PDF 自身定 → KB 写正确值)
| T | PDF 原文 (layout 定位) | 依据是否成立 |
|---|---|---|
| T-16a | p206 l42-43 `"CD3+CD19- (T lymphocyte)`、`"CD278+ (activated)` 未闭合 | 成立: 同句平行项 "CD45" / "CD4+CD8-" / "CD197+CD45RA-" 均闭合; KB 原即闭合, 不动 |
| T-16b | p205 l13-14 CPSCMRKS ×3 | 成立: spec 变量名 CPCSMRKS (p201); pdf_atoms a005 误抽为 CPCSMRKS, 以 layout 为准; KB 原即正确 |
| T-17 | p200 l10 "marker sting" | 成立: 拼写错, 同节 "marker string" 多处 |
| T-18 | p206 l6 "CPCELSTA and CSMRKS" | 成立: 同段 l8/l11/l12 三处 "CPCELSTA and CPCSMRKS" |
| T-19 | p206 l39 "ordered combination of CPTEST, CPSMRKS, and CPCELSTA" | 成立: spec CPMRKSTR Notes p201 l45 "combination of CPTEST, CPSBMRKS, and CPCELSTA" (同一三元组); 层级顺序 test→sublineage→state |
| T-20 | p201 CPCELSTA Notes "CPCELSTA and CPSMRKS, in combination with … CPTEST and CPSBMRKS" (渲染确认) | 成立: 同句已列 CPSBMRKS, 余者只能为 CPCSMRKS; asm 4 "CPCELSTA is used in conjunction with CPCSMRKS" |
| T-21 | p199 l33-34 --BNDAGT/--GATEDEF; p200 l11 --GATEDEF; p206 l1 CPBNDAGT | 成立: spec 变量 CPBDAGNT (p201 l35) / CPGATDEF (p202 l7); p208 l20-21 列 "CPBDAGNT (Binding Agent) … CPGATDEF (Gate Definition)"; 与 T-15 同口径. 补充: SDTM v2.0 Findings 变量表 (sv20 p22/p23) 泛型名即 --BDAGNT / --GATDEF, 泛型 "--" 名同样可定 |

### fp_match 回归定性 (本批新增 6, 全部预期)
| atom | 原因 | 定性 |
|---|---|---|
| ig34_p0199_a020 / p0200_a007 / p0206_a001 | T-21 改正值 (原子含 PDF 错名) | 预期 |
| ig34_p0200_a006 | T-17 sting→string | 预期 |
| ig34_p0206_a003 | T-18 CSMRKS→CPCSMRKS | 预期 |
| ig34_p0240_a004 | S-2 删附录; 原子为 PDF "nucleoar" 原文, 唯一承载处被删, examples.md 为 T-4 改正值 | 预期 |
- p0255_a021 等非本批页回归不计.

### 问题表 (全部 LOW, 不阻断)
| ref | 检查项 | 问题 | 证据 / 建议 |
|---|---|---|---|
| L-1 t2_fp_expected_regressions.jsonl | 台账 | 本批 6 条预期回归尚未登记进 expected 文件 (writer 报告已列) | 主控 commit 前追加, 否则后续批 fp 差集会重复报 |
| L-2 t2_S-SPC1.md census_items 行 | writer 报告 | LB 通用表写 "含 `*` 13 格", 实为 11 格 (渲染 p195-196 + KB 计数一致) | 仅报告笔误, KB 无误; 可在 writer 报告旁注 |
| L-3 IS/assumptions.md:41 | 导航措辞 | 交叉引用写 "verbatim at their PDF positions", 但 Ex10 Rows 1-5 在 examples.md 为 T-4 改正值 (nucleolar) | 与 CP/asm:104 先例同措辞, 可接受; 如求严谨可去掉 "verbatim" |
| L-4 IS/assumptions.md:39 | 结构 | `## IS – Examples Notes` 为 KB 自拟标题 (PDF 无), 现只承载交叉引用 | 规则 6 不改标题, 纯导航, 不计忠实错误; auditor brief 已按 U8 口径 |
| L-5 IS/assumptions.md:27 等 | 排版 | 既有文字直引号 vs PDF 弯引号 (如 “antigen”) | 归 S-TYPO (U1), 非本批缺陷 |

### R2 recheck
- 本批 json 无 `t2_recheck[]`; 全扫未发现改写丢短语 (R2) 项. 新增 REAL_GAP 0.

### 总结
- G-TB4: census 39 表 = OK 31 + DIFF 6 (35 格, 全为已登记 T-n, PDF 值渲染/bbox 复核) + NO_PDF 1 (Ex9 434 格人工逐格) + UNPARSEABLE 1 (LB 通用表 203 格人工逐格).
- G-TB6: 新增/改动 KB 行全有 PDF 出处或签字结构行; 无出处 0. spec 4 域 235 变量逐字段一致 (除 U5/U6 范围外 + T-20). CT `*` 7/7, CP 0 确认.
- fp_match 本批新增回归 6 全预期; check_links live docs 42.
