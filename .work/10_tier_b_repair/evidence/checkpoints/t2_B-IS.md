# T2 B-IS writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `59d2451ccbcad079c580968ba4c7bbacb7ac2d14`
- md5 before: IS/examples.md `baec1dcdcbfbce02c71f762d43a44d2d`; after `b988ce26d32205e8a3215abea6876567` (行数 273 → 275, +2 = N-7 插入句 + 空行)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-IS_writer/`
  (examples.before.md, apply.py 精确替换 + 每组命中次数断言 + Ex4/Ex8 删列时断言该列全空 + Ex5 整表重建, prose_scan.py, census_before/after.json, fp_before/after.jsonl, p233-241 渲染图 130dpi)
- 数据来源: 所有改动格逐一对照 p234-241 渲染图 (layout 文本只作辅助); 叙述对照 `work/pdf_pages/ig34_p0233-0241.txt` + 渲染图.
- 本批 atoms 14 (VALUE_DIFF 13 / REAL_GAP 1) / t2_recheck 0; census DIFF 8 表 (91 diffs) 全部处理; pdf_only 0; unparseable 0. O7 (IS Ex4-8) 已全部覆盖.
- 后处理: Ex5 重建行空格写成 `|  |`, 已统一为同文件惯用 `| |` (改前文件无 `|  |`, 只影响 Ex5 5 行).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | IS/examples.md:48 | census:40 r7 ISGRPID, ISTEST | REPLACED | ISGRPID 3 → 4; ISTEST "Neutralize … Antidrug Ab" → "Neutraliz Cross-React Bind Antidrug AB" (= CT C147274 提交值, terminology/core/is_domain_part1.md:98) | 234 |
| 2 | :49 | census:40 r8 ISTEST | REPLACED | 同上 ISTEST | 234 |
| 3 | :85-95 | census:85 HEADER (ISGRPID) | REPLACED | 删 KB 多出的 ISGRPID 列 (表头 + 分隔线 + 9 行; 9 行该列全空, 脚本断言) | 235 |
| 4 | :113 | ig34_p0236_a008 + census:113 HEADER | TABLE_REBUILT | 表头 +ISGRPID (ISREFID 后), −ISORRESU; 原子文本漏 ISSCAT (ATOM_ERR, 渲染图有 ISSCAT), KB 保留 | 236 |
| 5 | :115-121 | ig34_p0236_a009..a015 + census:113 CELL×59 | TABLE_REBUILT | 7 行全部按渲染图重写: ISTESTCD MBIGSAB→MBIGGAB; ISTEST "IgG Antibody"→"Microbial-induced IgG Antibody"; ISMETHOD IMMUNOASSAY→ELISA; ISGRPID 1/1/2/2/空/空/空; ISSEQ 1,2,1,2,1,2,3 (U-1); ISREFID r5-7 13669/13670/13671; ISORRES 1:25/1:120/1:90/1:220/1:500 + ISSTRESC/N 同数 + ISSTRESU titer; r6/r7 STUDYID 保留 RSV1230 (T-1/T-2) | 236 |
| 6 | :143-145 | ig34_p0237_a012..a014 + census:141 CELL×9 | REPLACED | STUDYID INFLA456→INFL456; ISREFID SAMPLBC001→SAMPBL0201; ISDTC 2011-06-08→2011-08-08 (×3 行) | 237 |
| 7 | :155 | ig34_p0238_a001 | INSERTED | Rows 1-2 句尾 "in ISCNDAGT." → "in ISCNDAGT, respectively, prior to vaccination." | 238 |
| 8 | :160 | ig34_p0238_a004 + census:160 HEADER | REPLACED | 表头 ISTCND → ISTSTCND (= VARIABLE_INDEX.md:777) | 238 |
| 9 | :164-165 | census:160 r3/r4 ISDTC | REPLACED | 2017-06-27 → 2017-08-27 | 238 |
| 10 | :183-187 | ig34_p0239_a002 + census:181 HEADER | REPLACED | 删 KB 多出的 ISORRESU 列 (3 行全空, 脚本断言) | 239 |
| 11 | :187 | census:181 r3 ISDTC | REPLACED | 2017-09-27 → 2017-08-27 | 239 |
| 12 | :227-232 | census:218 r6-11 ISSEQ | REPLACED | 6..11 → 1..6 (照录 PDF, U-1) | 240 |
| 13 | :250-256 | census:244 r3-9 ISSEQ | REPLACED | 3..9 → 2,3,3,4,4,5,5 (照录 PDF, U-1) | 241 |
| 14 | :80 | R3 N-1 ig34_p0235_a013 | REPLACED | Row 6 "peginterferon beta 1a," → "beta-1a," | 235 |
| 15 | :103 | R3 N-2 ig34_p0236_a002 | REPLACED | "(or both) — yet" → "(or both)—yet" (PDF em dash 无空格) | 236 |
| 16 | :105 | R3 N-3 ig34_p0236_a003 | REPLACED | "rows 3 and 4 is" 后直引号 → PDF 弯引号 | 236 |
| 17 | :107 | R3 N-4 ig34_p0236_a004 | REPLACED | 词替换 "prospectively" → PDF "purposefully" (该行无其他原子) | 236 |
| 18 | :129 | R3 N-5 ig34_p0237_a004 | REPLACED | "secrete these antibodies" → "secrete antibodies" | 237 |
| 19 | :136 | R3 N-6 ig34_p0237_a008 | INSERTED | Row 2 "from the same blood sample" → "from the same subject's blood sample" | 237 |
| 20 | :167 | R3 N-7 ig34_p0238_a009 | INSERTED | Ex7 表后、`## Example 8` 前补 PDF 过渡句 "The next 2 examples show data from microneutralization and opsonophagocytic killing (OPK) assays, …" (位置同 :123 Ex5→Ex6 过渡段) | 238 |
| 21 | :193 | R3 N-8 ig34_p0239_a008 | INSERTED | "present in the serum" → "present in the subject's serum" | 239 |
| 22 | :213 | R3 N-9 ig34_p0240_a003 | REPLACED | Sjogren's → Sjögren's | 240 |
| 23 | :215 | R3 N-10 ig34_p0240_a004 | REPLACED | "using ISGRPID" 归位: "Rows 1 to 5 are grouped together using ISGRPID with values …"; "post-coordinated using ISGRPID and represented" → "post-coordinated and represented" (D-1) | 240 |
| 24 | :108 | T-3 ig34_p0236_a005 | SKIPPED_PDF_TYPO | KB "NON-STUDY-RELATED" 未动 | 236 |
| 25 | :153 | T-5 ig34_p0237_a018 | SKIPPED_PDF_TYPO | KB "participating in a vaccine study" 未动 | 237 |
| 26 | :215 | T-4 (ig34_p0240_a004 内) | SKIPPED_PDF_TYPO | KB "nucleolar" 未动 | 240 |
| 27 | :101 | U-2 ig34_p0235_a030 | SKIPPED_PDF_TYPO | KB = PDF "RSV-protein B" ×3 未动, T4 | 235-236 |

- atoms 覆盖率自查: atoms 14 = 变更清单 atom 行 (#4 a008; #5 a009-a015 = 7; #6 a012-a014 = 3; #7 a001; #8 a004; #10 a002) = 1+7+3+1+1+1 = 14. 跳过 0.
- pdf_typo_suspect 原子 a014/a015 (Ex5 r6/r7): 疑点 = STUDYID RSC1230, 按取舍规则 KB 写 RSV1230 (T-1/T-2), 其余格照 PDF 重建.

### census 表处理

| census ref (before 行号) | 处理 | 结果 |
|---|---|---|
| :40 Ex2 (3) | #1-2 | OK |
| :85 Ex4 (1 HEADER) | #3 | OK |
| :113 Ex5 (60 = HEADER 1 + CELL 59) | #4-5 整表重建 | DIFF 2 残留 = r6/r7 STUDYID (T-1/T-2) |
| :141 Ex6 (9) | #6 | OK |
| :160 Ex7 (3) | #8-9 | OK |
| :181 Ex8 (2) | #10-11 | OK |
| :218 Ex10 (6) | #12 | OK |
| :244 Ex11 (7) | #13 | OK |

- 汇总: before `OK 5 / DIFF 8, cells 1464, diffs 91` → after `OK 12 / DIFF 1, cells 1452, diffs 2 (全为 T-1/T-2)`. 本批页 PDF_ONLY 0.
- jsonl census 行 92 = 91 diffs + Ex5 HEADER diff 含 2 列 (ISGRPID 增 / ISORRESU 删) 各记一行.

```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-IS_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-IS.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # 改前同法 census_before.json
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl                                       # 改前同法 fp_before.jsonl
python3 -I $S/prose_scan.py
python3 tools/check_links.py | tail -1   # live docs: 42 (基线 42)
```

### fp_match (只看 p228-241 原子及 target/hit 涉及 IS/examples.md 的原子)
- 回归 0; 新命中 35 (p0234_a011/a012, p0235_a013, p0236_a002/a004/a009-a013, p0237_a004/a008/a012-a014, p0238_a001/a004/a007/a008, p0239_a002/a005/a008, p0240_a013-a018, p0241_a005-a011).
- 改后 p233-241 仍未命中 (均非 KB 缺失):
  - 预期 (PDF_TYPO, KB 偏离 PDF): ig34_p0236_a014/a015 (T-1/T-2 RSC1230), ig34_p0236_a005 (T-3), ig34_p0237_a018 (T-5). T-4 "nucleoar" 所在 ig34_p0240_a004: fp 改前改后 hit_target 均为 IS/assumptions.md (未变, 不计回归); prose_scan 列为残留.
    这些原子改前也未命中 → **对 fp_match 不构成回归**; 若台账要求精确, 即为预期回归清单.
  - ATOM_ERR (原子抽取错, KB 按渲染图正确): ig34_p0236_a008 (表头漏 ISSCAT); ig34_p0238_a005 (Ex7 r1 ISSEQ 记作 3, 渲染图 1); ig34_p0240_a011 (Ex10 r4 列错位); ig34_p0241_a022 ("CENTRAL CA. AREA 14", 渲染图逗号).
  - 截断: ig34_p0235_a030 (TRUNCATED_AT_PAGE_BOUNDARY, KB 有全句).
  - ig34_p0241_a025 = LB 节, 非本文件.

### 双向叙述扫描 (R3; prose_scan.py)
- PDF→KB: p233-241 全部 SENTENCE/LIST_ITEM 原子归一 (去 `**`、合并空白、弯引号直化) 后在 KB 中做子串检查. 改后未命中 4 条 = ig34_p0236_a005 (T-3), ig34_p0237_a018 (T-5), ig34_p0240_a004 (T-4), ig34_p0241_a025 (LB 节). 与 T 清单一致, 无其他缺失.
- KB→PDF: KB 每行叙述按句切分, 在 p233-241 layout 文本拼接 (去页脚, 跨页连续) 归一后做子串检查. 改后未命中 3 句 = :108 (T-3), :153 (T-5), :215 (T-4). 无 KB 自写 / 超出 PDF 的句子.
- 改前 (同法) 额外缺失、已在本 attempt 修: N-1..N-10.

### 新增 atom 清单 (R3, 叙述缺失/改写; atom_id 取 work/pdf_atoms.jsonl)
- N-1 :80 p0235_a013; N-2 :103 p0236_a002; N-3 :105 p0236_a003; N-4 :107 p0236_a004; N-5 :129 p0237_a004; N-6 :136 p0237_a008;
  N-7 :167 p0238_a009; N-8 :193 p0239_a008; N-9 :213 p0240_a003; N-10 :215 p0240_a004.
- 未做 (仅格式, 同 B-DS 口径): PDF 弯撇号 "subject’s" (Ex6 Rows 1-3, Ex8/Ex9 若干处) KB 用直撇号未改; Ex9 ISBDAGNT en dash 已登记 T-6.
- N-3 说明: 该句 PDF 本身混用 (前半 ISCAT = "STUDY …" 直引号, 后半 “NON-STUDY-RELATED …” 弯引号), KB 逐字跟 PDF 恢复弯引号这一对; 其余直/弯撇号差异未动.

### 删除清单 (reviewer 逐条确认)

| # | 原位置 (base 行号) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | :213 "post-coordinated using ISGRPID and represented" 中的 "using ISGRPID" | :215 "post-coordinated and represented"; 短语归位到 "grouped together using ISGRPID with values" | KB 错位改写 (把 PDF 前一句的短语挪到后一句), 与 PDF 两句原文不符; 该行仅承载 p0240_a004 一个原子 | 同行前一句 |
| D-2 | :113-121 Ex5 表头 + 旧行 ISORRESU 列 + 全部旧值 | :113-121 PDF 重建表 | VALUE_DIFF 旧值替换 / 表头跟 PDF (规则 3) | — |
| D-3 | :85-95 Ex4 ISGRPID 列, :181-185 Ex8 ISORRESU 列 | 删列 | PDF 无该列; 列内全空 (断言) | — |
| D-4 | :107 "prospectively" | "purposefully" | 词替换型改写, 该行无其他原子 → 恢复 PDF 原词 | — |
| D-5 | :129 "these" | 删 | KB 多出词 (PDF 无) | — |

### PDF_TYPO 清单 (正确值可由 PDF 自身确定 → KB 写正确值)

| # | 位置 | PDF | KB | 依据 |
|---|---|---|---|---|
| T-1 | :120 Ex5 r6 STUDYID | RSC1230 | RSV1230 | 同列其余 5 行 RSV1230; 同行 USUBJID RSV1230-011; 同例叙述 RSV 研究. census 残留 1 |
| T-2 | :121 Ex5 r7 STUDYID | RSC1230 | RSV1230 | 同 T-1. census 残留 1 |
| T-3 | :108 Ex5 Rows 3-4 叙述 | "NON-STUDY RELATED IMMUNOGENICITY" | "NON-STUDY-RELATED IMMUNOGENICITY" | 同表 ISCAT r3/r4 及同页叙述 3 处均为 NON-STUDY-RELATED; KB 未动 |
| T-4 | :215 Ex10 Rows 1-5 叙述 | "(i.e., nucleoar)" | "nucleolar" | 同表 r5 "NUCLEOLAR PATTERN"; KB 未动 |
| T-6 | :205-207 Ex9 ISBDAGNT r1-3 | "STAPHYLOCOCCUS AUREUS–EPITOPE X" (en dash) | 连字符 "AUREUS-EPITOPE X" | 同例叙述 "S. aureus-epitope X" 用连字符; census/fp 归一后无差异; KB 未动 |
| T-5 | :153 Ex7 叙述 | "participating a vaccine study" | "participating in a vaccine study" | PDF 漏介词 (语法); KB 未动. 依据较弱 (无同文平行句), reviewer 若不认可则改照录 + T4 |

### 照录 PDF, 供主控 / T4 用户裁 (KB = PDF)
- **U-1 ISSEQ 重复 (18 格)**: Ex5 r1-7 = 1,2,1,2,1,2,3 (:115-121); Ex10 r1-11 = 1-5,1-6 (:222-232); Ex11 r1-9 = 1,2,2,3,3,4,4,5,5 (:248-256). 同一 USUBJID 内 ISSEQ 重复, 违反 IS spec "Sequence number to ensure uniqueness of records within a dataset for a subject" (IS/spec.md:41-49); 但 spec 允许 "any valid number", 正确值无法由 PDF 单值确定 (三表模式一致: 按组/成对重起) → 照录 PDF, 三表同一处理. 用户可裁: 维持照录 / 改为 Row 连续编号 (将产生 18 格 census 残留 + 对应 fp 回归).
- **U-2 Ex5 引言 "RSV-protein B" ×3 (:101)**: "antibody against RSV-protein Z was detected … previous vaccination with RSV-protein B … immunity against RSV-protein B was not the interest … data pertaining to RSV-protein B" — 语境 (同例下段: protein Z 与疫苗无关) 指向应为 Z, 但 PDF 未明载, 改写需推断 → KB = PDF 未动, T4.
- **U-3 Ex7 r3/r4 ISDTC (:164-165)**: 渲染图 VISIT 1 = 2017-08-27 (已照改), 而同受试者 RSV1230-011 在 Ex5 r5 / Ex8 r2 的 VISIT 1 = 2017-07-27. 跨例不一致, 不可由同表确定 → 照录, T4.
- **U-4 Ex9 叙述 "The assay read-out is expressed in by the opsonization index" (:193)**: 多余介词; 同例后句 "expressed by the opsonization index" 提示应删 "in", 但 "expressed in" 亦通 → 不可单值确定, KB = PDF 照录, T4.
- 已核非问题: Ex2 r7/r8 ISTEST "Neutraliz Cross-React Bind Antidrug AB" 看似截断/大小写怪, 实为 CT 提交值 (is_domain_part1.md:98/:226), 照 PDF 改; Ex5 ISREFID r5-7 = 13669/13670/13671 (不同访视不同样本, 合理).

### KB_AUTHORED / D6
- 无 (KB→PDF 扫描无自写句; 标题 `## Example N` / `**is.xpt**` 为纯导航).

### 范围外发现
- 无 (IS/assumptions.md 未扫, 非本批白名单).

### 触碰过的 unparseable 表
- 无.

### git diff --stat -- kb_files
```
 knowledge_base/domains/IS/examples.md | 114 +++++++++++++++++-----------------
 1 file changed, 58 insertions(+), 56 deletions(-)
```
- check_links: `broken relative links: 18668 (live docs: 42)` (基线 42, 未升).
- writer.jsonl: 122 行 = atoms 14 + census 92 + R3 N-1..N-10 (10) + T-3/T-5/U-2 (3) + T-6/U-3/U-4 (3). T-1/T-2 记在 census 行 (action SKIPPED_PDF_TYPO, KB 该格未动); T-4 记在 N-10 行 note.
