# T2 B-BE writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `8c4227a6cdd12835d5cf11d0b900fb5bdd2efe5c` (BE 文件工作树改前无未提交改动, `git diff --quiet -- knowledge_base/domains/BE` = clean)
- md5: BE/examples.md `9b5014d22275717210986b63606806ed` → `03155948982d159157b833d7b489cca1` (161 行不变); BE/assumptions.md `93248af1589bf3107433c18a982d2dec` → `85a4e0a69d7c6a0dd1ba95eb0b1b0e6a` (24 → 28 行); BE/spec.md 未动 `f9384c9dc59bd5a23b396bb450071d90`
- 白名单: examples.md (batch json) + assumptions.md (主控授权: 仅 Description/Overview + spec 首句, CM/SC 先例, 逐字)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-BE_writer/` (examples.before.md, assumptions.before.md, p143/145-148 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 0 / t2_recheck 0; census DIFF 4 表 (8 CELL, KB 行 29/41/43/124/125/138); pdf_only 0; unparseable 0; out_of_scope 0.
- pdf_ranges 覆盖核 (O20): BE 节 = p143 "6.2.2 Biospecimen Events (BE)" (节引言 NOTE + Description/Overview + spec 首句 + spec 表) → p144 (spec 续 + Assumptions 1-6b) → p145 (6c/7 + Examples Ex1) → p146-147 (Ex1 续 + Ex2) → p148 (Ex2 relrec + References; 其后 6.2.3 CE). batch lo/hi = 143-148 **完整覆盖**. (batch `pdf_pages` 145-147 仅表页.)

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | BE/examples.md:29 | census:examples.md:29:1:QLABEL | REPLACED | `Specimen Type` → `SPECIMEN TYPE` (Ex1 PDF 大写; Ex2 PDF 为 Specimen Type, 各照 PDF) | 145 |
| 2 | BE/examples.md:41 | census:examples.md:41:1:BSSTRESN | REPLACED | 空 → `2` (渲染图 BSSTRESN=2) | 146 |
| 3 | BE/examples.md:43 | census:examples.md:43:3:BSORRES | SKIPPED_PDF_TYPO | KB 保留 `DRY ICE/ISOPROPANOL`; PDF `ISOPOPANOL` 拼写错 → T-1 | 146 |
| 4 | BE/examples.md:43 | census:examples.md:43:3:BSSTRESC | SKIPPED_PDF_TYPO | 同上 → T-1 | 146 |
| 5 | BE/examples.md:43 | census:examples.md:43:3:BSDTC | SKIPPED_PDF_TYPO | KB 保留 `2005-03-20`; PDF 渲染 `5-0` (残缺) → T-2 | 146 |
| 6 | BE/examples.md:124 | census:examples.md:124:3:BSREFID | SKIPPED_PDF_TYPO | KB 保留 `298R1-1R0`; PDF `298B1-1R0` → T-3 | 147 |
| 7 | BE/examples.md:125 | census:examples.md:125:4:BSREFID | SKIPPED_PDF_TYPO | 同上 → T-3 | 147 |
| 8 | BE/examples.md:138 | census:examples.md:138:1:PARENT | REPLACED | `298B1` → 空 (渲染图 Row 1 PARENT 空; BLOOD 为根) | 147 |
| 9 | BE/examples.md:62 | R3 新增 (Ex2 引言) | INSERTED | 补引用标记 `[1]` (detection, 后) / `[2]` (integrity. 后); 与文末 References 1-2 对应 | 146 |
| 10 | BE/examples.md:130 | R3 新增 (词替换) | REPLACED | "See GF datasets for examples" → "See GF examples for examples" (PDF 原词; 该行无其他原子冲突) | 147 |
| 11 | BE/assumptions.md:3-6 | ig34_p0143 Description/Overview (主控授权) | INSERTED | 新增 `## BE – Description/Overview` + p143 原句逐字 (位于 Specification 前, CM 结构) | 143 |
| 12 | BE/assumptions.md:9 | spec 首句 (主控授权) | — (PRESENT) | `be.xpt, Biospecimen Events — Events. One record per … Tabulation.` 已逐字存在, 未改 | 143 |

- 覆盖率自查: atoms 0; census 8 格 = #1-8 (全部处理); R3 新增 2 (#9-10); 授权项 2 (#11-12).

### census 表处理

| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:27 Ex1 suppbe.xpt (1 CELL) | #1 | OK |
| examples.md:39 Ex1 bs.xpt (4 CELL) | #2 改; #3-5 PDF_TYPO | DIFF 3 (均为登记的 T-1/T-2) |
| examples.md:120 Ex2 bs.xpt (2 CELL) | #6-7 PDF_TYPO | DIFF 2 (均为 T-3) |
| examples.md:136 Ex2 relspec.xpt (1 CELL) | #8 | OK |
| 其余 5 表 (:17 :53 :80 :101 :149) | census OK; 渲染图人工复核一致 | OK |

census_after: KB tables 9, OK 7, DIFF 2, diffs 5 — 5 条全部为本批 PDF_TYPO 登记项, 预期残留.

### PDF_TYPO 清单 (依据 = PDF 自身)
- T-1 (p146 Ex1 bs Row 3 BSORRES/BSSTRESC): PDF "ISOPOPANOL" 为拼写错; 按 dispatch 口径 "PDF 自身拼写错 KB 保留正确拼写" → KB `DRY ICE/ISOPROPANOL`.
- T-2 (p146 Ex1 bs Row 3 BSDTC): PDF 单元格仅 "5-0" (残缺). 正确值由 PDF 自身确定: 同组 Row 2 (BSGRPID 267FF) BSDTC = 2005-03-20, Row 1 同; BE Ex1 全部 BEDTC = 2005-03-20 → KB `2005-03-20`.
- T-3 (p147 Ex2 bs Rows 3-4 BSREFID): PDF "298B1-1R0". 同例 be.xpt Row 4 BEREFID、suppbe Row 3 IDVARVAL、relspec Row 3 REFID 及 Rows 4-6 PARENT 均为 `298R1-1R0` (R = RNA 命名), bs Rows 5-7 亦为 298R1-1R* → KB 保留 `298R1-1R0`.
- 非 TYPO 说明: #1 Ex1 QLABEL 大写 vs Ex2 Title case — 属 PDF 例间风格差, 非可证错误, 照录 PDF.

### 预期 fp 回归 (PDF_TYPO 修正)
- 由 T-1/T-2/T-3 导致的 fp 非 EXACT: p146 bs Row 3 表行原子、p147 bs Rows 3-4 表行原子 (KB 值 ≠ PDF 字面). 这些格 KB 改前即为正确值, 故**相对 baseline 无新增回归**.
- fp_match 改后 p143-147: EXACT 90 / INTENTIONAL_EXCLUDE 16 / PARTIAL 12 / EQUIVALENT 10; 与 baseline verdict 逐条比 **0 变化**. PARTIAL 12 中 10 条为 spec 表行 (p143_a024, p144_a001-a009, 属 spec.md, 范围外), p145_a009/a020 为 matcher 折行假阳 (人工核 KB:11/:31 逐字).
- 全量 regress 输出 2 条 (ig34_p0363_a019 / p0364_a001, §6.4.2) — 他批工作树改动, 非本批; `grep -E 'p014[3-8]|BE/'` = 0.

### 双向全扫 (含表格原子)
- PDF→KB: p145-148 叙述逐句规范化比对 (脚本见复跑命令) 0 缺; 9 张表 (be/suppbe/bs/relrec ×Ex1, be/suppbe/bs/relspec/relrec ×Ex2) 对 110dpi 渲染图逐格人工核: 表头/列序/列数/Row 列一致, 除 T-1..T-3 外 0 差. References 1-2 逐字. p143-145 assumptions 1-7 (含 6a-c) 逐句在 assumptions.md (PDF "single-\nsponsor"/"--\nHLGTCD" 为折行).
- KB→PDF: examples.md 全文件每行均有 PDF 对应; 无 KB 自写解释性内容 (D6 无), 无伪节号; `# BE — Examples`/`## Example N`/`**xxx.xpt**`/`**References**` 为导航. assumptions.md 全文件均有 PDF 对应.
- 缺失 (范围外, 见 F-1): p143 节引言 NOTE 3 句.

### 新增 atom 清单 (R3)
- #9 Ex2 引言 citation 标记 [1][2]; #10 "GF examples" 原词恢复.

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:29/:138 旧值 | 同行 | VALUE_DIFF 旧值替换 (#1/#8) | — |
| D-2 | examples.md:130 "datasets" 一词 | 同行 | 词替换型改写恢复 PDF 原词 (#10) | — |

### 范围外发现
- F-1 (需主控定): p143 §6.2.2 节引言 NOTE ("BE, BS, and RELSPEC domain specifications … copied and minimally updated from the provisional SDTMIG-PGx …" 3 句) BE 文件中缺失; 现仅在 RELSPEC/assumptions.md:5 与 ch08:410 (RELSPEC 节). 授权仅限 Description/Overview + spec 首句, 故未补. 建议: assumptions.md 标题后、Description/Overview 前补入 (与 RELSPEC/assumptions.md:5 同格式).
- F-2: O5 (ch03 Keys for BE) — ch03 不在本批, 未动.
- F-3: spec.md (p143-144 spec 表) 不在白名单, fp PARTIAL 10 条 → 归 O15 spec 扫描.

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-BE_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-BE.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 7 / DIFF 2 / diffs 5 (=T-1..T-3)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p014[3-8]|BE/' $S/fp_regress.jsonl   # 0
for p in 143 145 146 147 148; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
python3 tools/check_links.py | tail -1   # live docs: 42
```

### git diff --stat
```
 knowledge_base/domains/BE/assumptions.md |  4 ++++
 knowledge_base/domains/BE/examples.md    | 10 +++++-----
 2 files changed, 9 insertions(+), 5 deletions(-)
```

## attempt 1 续 (F-1 主控授权)
- 变更: `knowledge_base/domains/BE/assumptions.md:3` 新增 p143 §6.2.2 节引言 NOTE 3 句 (普通段落, 位于 `# BE — Assumptions` 后、`## BE – Description/Overview` 前; 与 RELSPEC/assumptions.md:5 同格式), 空行 :4. 其余行未动.
- 新 md5: `d94ec29ad3b637fed939197d20b5a90c`
- PDF 逐字核对: `pdftotext -f 143 -l 143 -layout "source/cdisc/SDTMIG v3.4 (no header footer).pdf" - | sed -n 2,4p | sed 's/^ *//;s/ *$//' | tr '\n' ' ' | sed 's/ $//'` 与 `sed -n 3p knowledge_base/domains/BE/assumptions.md | tr -d '\n'` → `cmp` IDENTICAL. p143 3 行折行处均为整词边界, 无连字符.
- 注意: p143 末句为 "…for inclusion in a future SDTMIG publication, after v3.4."; RELSPEC/assumptions.md:5 与 ch08:410 为 "…in a future SDTMIG." — 经 `pdftotext -layout <PDF> - | grep -n -A1 "extensive revision"` 核: §8.8 (RELSPEC 源) PDF 原文即 "future SDTMIG.", 两处各自对源无误, 非缺陷. 同句另见 PDF 第 9020 行附近 (疑 BS 节引言), 不在本批.
- `python3 tools/check_links.py | tail -1` → live docs: 42 (不变).
- F-1 状态: **已处理** (主控授权, 2026-11-26).
