# T2 B-IS reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base 59d2451; 审范围 `knowledge_base/domains/IS/examples.md` (KB diff 中其他文件 ch02/ch04/model01/model02/EX = 别批, 不审).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-IS_reviewer/`
  (p-233..241.png 150dpi 渲染; raw.txt = pdftotext p232-241; scan.py/scan2.py 独立双向逐句扫描; census_after.json; fp_after.jsonl / fp_regress.jsonl)

### 命令与关键输出 (可复跑, repo 根)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-IS_reviewer; mkdir -p $S
pdftoppm -f 233 -l 241 -r 150 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p
pdftotext -f 232 -l 241 "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/raw.txt
python3 -I $S/scan2.py $S          # 双向逐句 (去 is.xpt/Example 标题分段, 弯引号/破折号归一, 大小写敏感)
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  # exit 1; IS: status {'OK': 12, 'DIFF': 1}; cells 1452; diffs 2 (= Ex5 r6/r7 STUDYID, T-1/T-2); 本批页 pdf_only 0 / pdf_unparsed 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # RESULT: RED, 15 条回归全部 p258-263 MB/MS 等别批; 过滤 ig34 p228-241 或 target/hit 含 domains/IS → 0
python3 tools/check_links.py | tail -1    # broken relative links: 18668 (live docs: 42)  ≤ 42
```

### (1) 表格 — 独立方法 = 渲染图逐格目视 (不用 bbox 解析器)
| 表 | 核对范围 | 结果 |
|---|---|---|
| Ex5 (p236) 整表重建 | 表头 22 列 + 7 行 × 22 = 154 格全核 | 一致; 唯 r6/r7 STUDYID PDF=RSC1230, KB=RSV1230 (T-1/T-2) |
| Ex5 表头 | PDF 有 ISGRPID (ISREFID 后)、ISSCAT, 无 ISORRESU | 一致 |
| Ex4 (p235) | PDF 表头无 ISGRPID 列 (STUDYID…ISREFID, ISTESTCD) | 删列正确; 9 行其余格一致 |
| Ex8 (p239 上) | PDF 表头无 ISORRESU (ISORRES→ISSTRESC) | 删列正确; r3 ISDTC 2017-08-27 一致 |
| Ex7 (p238) | 表头 ISTSTCND; r3/r4 ISDTC 2017-08-27; r1 ISSEQ 1 | 一致 |
| Ex2 (p234) r7/r8 | ISGRPID 4/4; ISTEST "Neutraliz Cross-React Bind Antidrug AB" | 一致 |
| Ex6 (p237) 9 格 | INFL456 / SAMPBL0201 / 2011-08-08 ×3 行 | 一致 |
| Ex10 (p240) r6-11 ISSEQ | 1..6 | 一致 (U-1) |
| Ex11 (p241) r1-9 ISSEQ | 1,2,2,3,3,4,4,5,5 | 一致 (U-1) |
| 额外抽查 (未改表) | Ex3 r1-4、Ex9 r1-3、Ex10 r1-5、Ex11 全列、SUPPIS ×2 | 一致 (Ex9 ISBDAGNT en dash = T-6) |
- census 91 diff = 3+1+60+9+3+2+6+7 (batch JSON) 全部消解, 残留 2 = T-1/T-2. 目视核格数 ≥ 154 (Ex5) + 约 80 (其余改动格+抽查) ≥ 40.

### (2) PDF_TYPO 判定
| # | 判定 | 依据 |
|---|---|---|
| T-1/T-2 RSC1230→RSV1230 | 同意 keep-correct | 同列 5 行 RSV1230 + 同行 USUBJID RSV1230-011 |
| T-3 "NON-STUDY RELATED" | 同意 | 同表 ISCAT r3/r4 + 同页 3 处 NON-STUDY-RELATED |
| T-4 nucleoar | 同意 | 同表 r5 NUCLEOLAR PATTERN |
| T-5 "participating a vaccine study" | 同意 keep-correct (LOW, 可选列入 T4 透明化) | 缺词的唯一合法补全是 "in" (单值; 区别于 U-4 两种删法), 属拼写级错误, 同 pre-corrdinating 口径 |
| T-6 en dash | 同意 | 同例叙述 "S. aureus-epitope X" 用连字符; 归一后无差 |

### (3) U-1..U-4 (照录 + T4): 均确认 KB = PDF, 正确值不能由 PDF 单值确定 → 照录合规.
- U-1 三表 ISSEQ 模式一致 (按组重起), 改法不唯一; U-2 "RSV-protein B" 三处语境指向 Z 但 PDF 未明载; U-3 Ex7 VISIT 1 = 2017-08-27 vs Ex5/Ex8 VISIT 1 = 2017-07-27, 跨例; U-4 "expressed in by" 可删 in 或 by.

### (4) N-1..N-10 叙述修正: 全部逐字对 PDF 命中 (scan2 PDF→KB 无缺), 位置为原句原处; N-7 在 Ex7 表后、Example 8 前 = PDF p238 位置. 一致.

### (5) 删除清单 D-1..D-5 vs diff
| # | 结论 |
|---|---|
| D-1 "using ISGRPID" 归位 | 合规; 改后两句与 PDF p240 逐字一致 |
| D-2 Ex5 旧表 (含 ISORRESU 列, MBIGSAB/IMMUNOASSAY/NA 等旧值) | 合规; PDF 无 ISORRESU, 旧值均错 |
| D-3 Ex4 ISGRPID / Ex8 ISORRESU 列 | 合规; PDF 无该列, 删前列内全空, 无数据丢失 |
| D-4 prospectively→purposefully | 合规 (PDF p236 "purposefully") |
| D-5 "these" | 合规 (PDF p237 "secrete antibodies or cytokines") |

### (6) reviewer 自扫 (双向逐句, IS Examples 全段 p232 起至 §6.3.5.6 前)
- PDF→KB (163 段): 未命中只剩 T-3 / T-5 / T-4 三句 + 表格文本段 (表另核). 无 R2 丢失短语 / URL / "see Section" 交叉引用 (本段 PDF 无此类引用).
- KB→PDF (154 段): 未命中只剩同 3 句的 KB 正确写法. 无 KB 自写句, 无需 D6.
- 结构行 (G-TB6 签字): `## Example N`、`**is.xpt**`/`**suppis.xpt**`、表头/分隔线 (Ex4/Ex5/Ex7/Ex8 改动) 、:166 空行 — 签字通过.

### (7) ATOM_ERR 确认 (原子 verbatim vs 渲染)
| atom | 原子文本 | 渲染图 | 结论 |
|---|---|---|---|
| ig34_p0236_a008 | 表头缺 ISSCAT | p236 表头有 ISSCAT (ISCAT 后) | 原子错 |
| ig34_p0238_a005 | Ex7 r1 ISSEQ=3 | p238 r1 ISSEQ=1 | 原子错 |
| ig34_p0240_a011 | r4 列错位 (多空格, 缺 ISSTRESN 170) | ISTSTOPO QUANTIFY / 1:170 / 170 / 170 / titer | 原子错, KB 行正确 |
| ig34_p0241_a022 | "CENTRAL CA. AREA 14" | "CENTRAL CA, AREA 14" | 原子错, KB:275 正确 |

### (8) 回归: fp IS 回归 0; census 本批 OK 12 / DIFF 1 (T-1/T-2 登记残留); live docs 42.

### 问题表 (均非阻断)
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| T-5 :153 | PDF_TYPO 取舍 | 依据为语法单值补全, 非同表/CT; 接受, 建议主控 T4 汇总时一并列出供用户知悉 | p237 "subject participating a vaccine study" |
| 弯/直撇号 | 格式 | N-3 恢复了一对弯引号, 其余 subject’s 等保持直撇号, 口径不完全一致 (LOW, 不影响信息) | p237 "subject’s blood sample" |

### 新增 atom / KB_AUTHORED / 范围外: 无新增发现.
