# T2 B-BS writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `46a66e94695795a4f6d3ac2aecef248dbe7fbbe5` (BS 文件工作树改前 clean; 基线另存 scratch `examples.before.md` / `assumptions.before.md`, 取自 `git show HEAD:`)
- md5: BS/examples.md `bf7d685304e75d9def147331d8fed9d3` → `09d77c5240ab38d156c90ed6f4b14bb8` (20 行不变); BS/assumptions.md `8038b1fac2f10041a082b8548e191b36` → `6a486d34060ec60dfaba6f7840a32de3` (11 → 23 行); BS/spec.md 未动 `e14a44612dfca53ae9ee097f8da4d5d7`
- 白名单: examples.md (batch json) + assumptions.md (主控授权: 节引言 NOTE + Description/Overview + spec 首句, 逐字, BE/CM 先例)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-BS_writer/` (before 副本, p196/198/199 渲染 110dpi, p199zoom 400dpi BSXFN 局部, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 1 (VALUE_DIFF, pdf_typo_suspect) / t2_recheck 0; census DIFF 1 表 (7 CELL, KB 行 17-20); pdf_only 0; unparseable 0; out_of_scope 0.
- 节页范围核 (O20): BS 节 = p196 下半 "6.3.5.2 Biospecimen Findings (BS)" (节引言 NOTE + Description/Overview + spec 首句 + spec 表起) → p197 (spec 续) → p198 (spec 末 + Assumptions 1-5 + Example 1 叙述) → p199 上半 (bs.xpt 表; 其后 6.3.5.3 CP). batch pdf_ranges lo/hi = 196-199 **完整覆盖** (batch `pdf_pages` 198-199 仅叙述/表页).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | BS/examples.md:7 | ig34_p0198_a020 | SKIPPED_PDF_TYPO | KB 保留 `ratios` / `may indicate`; PDF `rations` / `may indicated` 为拼写错 → T-1 | 198 |
| 2 | BS/examples.md:17 | census:examples.md:17:1:BSTESTCD | REPLACED | `A260/A230` → `A260A230` | 199 |
| 3 | BS/examples.md:18 | census:examples.md:18:2:BSTESTCD | REPLACED | `A260/A280` → `A260A280` | 199 |
| 4 | BS/examples.md:19 | census:examples.md:19:3:BSTESTCD | REPLACED | `28S/18S` → `I28S18S` (与 Row 3 叙述 "prefixed with an I" 一致) | 199 |
| 5 | BS/examples.md:17 | census:examples.md:17:1:BSXFN | REPLACED | `…135764.3.4.7280912` → `…135764.3.4:7280912` (400dpi 渲染确认冒号) | 199 |
| 6 | BS/examples.md:18 | census:examples.md:18:2:BSXFN | REPLACED | 同上 | 199 |
| 7 | BS/examples.md:19 | census:examples.md:19:3:BSXFN | REPLACED | 同上 | 199 |
| 8 | BS/examples.md:20 | census:examples.md:20:4:BSXFN | REPLACED | 同上 | 199 |
| 9 | BS/assumptions.md:3 | ig34_p0196_a016-a018 节引言 NOTE (主控授权; B-LB audit note) | INSERTED | 3 句 NOTE, 末句 "…publication, after v3.4." (BS 版, 非 §8.8 版) | 196 |
| 10 | BS/assumptions.md:5-7 | p196 Description/Overview (主控授权) | INSERTED | `## BS – Description/Overview` + 1 句原文 | 196 |
| 11 | BS/assumptions.md:9-11 | p196 spec 首句 (主控授权) | INSERTED | `## BS – Specification` + `bs.xpt, Biospecimen Findings — Findings. One record per …` | 196 |
| 12 | BS/assumptions.md:13 | 结构 (PDF 原标题) | INSERTED | `## BS – Assumptions` 标题 (p198 原标题), 把 spec 首句与编号列表分开; 照 BE/CM 结构 | 198 |

- 覆盖率自查: atoms 1 = #1; census 7 格 = #2-8 (全部处理); 授权项 #9-11; 结构标题 #12.
- 逐字核: `cmp` NOTE (PDF p196 3 行合并 vs KB :3) IDENTICAL; Description + spec 首句 (PDF p196 两行 vs KB :7/:11) IDENTICAL. 命令见下.

### census 表处理

| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:15 Ex1 bs.xpt (7 CELL) | #2-8 | OK (84 格比对, 0 diff) |

### PDF_TYPO 清单 (依据 = PDF 自身)
- T-1 (p198 Ex1 "Rows 1-2" 叙述, ig34_p0198_a020): PDF `rations` (同句后半与上句均为 ratios 语境) 与 `may indicated` (情态动词后原形) 为拼写/语法错; 按 dispatch 口径 "PDF 自身拼写错 KB 保留正确拼写" → KB 不改.
- T-2 (信息, assumptions 列表, 未改): p198 Assumption 3 PDF `which is part the SEND` (缺 of), KB `part of the` → KB 保留正确写法.
- T-3 (信息, assumptions 列表, 未改): p198 Assumption 5 PDF `--STRNLO` (变量名拼错; spec/通用 Findings 变量为 --STNRLO), KB `--STNRLO` → KB 保留正确写法.
- 非 TYPO 说明: BSXFN `3.4:7280912` 冒号无法由 PDF 自身证伪 (外部文件名), 照录 PDF. BSTESTCD 去斜杠/加 I 前缀与 p198 Row 3 叙述及 --TESTCD 规则一致, 是 PDF 正确值.

### fp 检查
- fp_match 改后 p196-199 (89 原子): EXACT 10 / EQUIVALENT 28 / INTENTIONAL_EXCLUDE 39 / PARTIAL 12; 与 baseline verdict 逐条比 **0 变化** (a016-a018 已由 ch08/BE 副本命中; a018 改后 hit_target = BS/assumptions.md).
- PARTIAL 12: p196_a003-a013 (8) 为通用规格表/ spec 表行 (属 LB / spec.md, 范围外); p198_a020 = T-1; p198_a021 = matcher 把 PDF 一句拆成 KB 两段 (md_dmBS_ex_a008/a009) 假阳, 人工核 KB:7 内容齐; p199_a010/a014 属 CP 节.
- 全量 regress 48 条均非 BS / p196-199 (`grep -E 'p019[6-9]|BS/'` = 0), 为他批工作树改动.

### 双向全扫 (含表格原子)
- PDF→KB: p196 节引言/Description/spec 首句 → assumptions.md:3/:7/:11 (逐字); p198 Assumptions 1-5 → assumptions.md 列表 (除 T-2/T-3 外逐字; "PGx-related"/"--\nCSTATE" 为折行); p198 Example 1 叙述 4 段 → examples.md:5/:7/:9/:11 (除 T-1 外逐字); p199 bs.xpt 表头 21 列列序/列名与 KB 一致, 4 行逐格对渲染图人工核 (含 BSTEST Row 4 "RNA INTEGRITY NUMBER", BSDTC 2005-03-21T11:28:17), 改后 0 差. p196-198 spec 表属 spec.md (不在白名单).
- KB→PDF: examples.md 全文件每行均有 PDF 对应; assumptions.md 全文件均有 PDF 对应; 无 KB 自写解释性内容 (D6 无), 无伪节号; `# BS — Examples` / `## Example 1` / `**bs.xpt**` / `**Rows 1-2:**` 为导航 (PDF 节标题 "BS – Example").

### 新增 atom 清单 (R3)
- 无 (授权项 #9-11 之外未发现叙述缺失).

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:17-20 旧 BSTESTCD (3 格) / BSXFN (4 格) | 同行 | VALUE_DIFF 旧值替换 (#2-8) | — |

### 范围外发现
- F-1: spec.md (p196-198 spec 表) 不在白名单, 未核 → 归 O15 spec 扫描.
- F-2: `tools/check_links.py` live docs 现为 44 (要求 42); 新增 2 条均来自 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-TE_review.md:87-88` (他批 evidence, 非本批); 本批改动不含任何链接. 需主控处理 B-TE review 文件.

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-BS_writer
P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
pdftotext -f 196 -l 196 -layout "$P" - | grep -A2 "^BE, BS, and RELSPEC" | sed 's/^ *//;s/ *$//' | tr '\n' ' ' | sed 's/ $//' > $S/note_pdf.txt; sed -n 3p knowledge_base/domains/BS/assumptions.md | tr -d '\n' > $S/note_kb.txt; cmp $S/note_pdf.txt $S/note_kb.txt && echo NOTE_IDENTICAL
pdftotext -f 196 -l 196 -layout "$P" - | grep -E "^(A findings domain that contains data related to biospecimen|bs.xpt, )" > $S/desc_pdf.txt; sed -n '7p;11p' knowledge_base/domains/BS/assumptions.md > $S/desc_kb.txt; cmp $S/desc_pdf.txt $S/desc_kb.txt && echo DESC_SPEC_IDENTICAL
pdftotext -f 199 -l 199 -raw "$P" - | grep -o "2.16.090[^ ]*"   # 4x ...3.4:7280912
pdftoppm -f 199 -l 199 -r 400 -x 3100 -y 450 -W 1000 -H 250 -png "$P" $S/p199zoom
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-BS.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # KB tables 1, OK 1, diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p019[6-9]|BS/' $S/fp_regress.jsonl   # 0
python3 tools/check_links.py 2>&1 | grep "live docs"   # 44 (+2 = t2_B-TE_review.md:87-88, 非本批)
```

### git diff --stat
```
 knowledge_base/domains/BS/assumptions.md | 12 ++++++++++++
 knowledge_base/domains/BS/examples.md    |  8 ++++----
 2 files changed, 16 insertions(+), 4 deletions(-)
```

- F-2 更新 (写完 checkpoint 后复跑): `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42 (B-TE review 文件已被他方修复); F-2 关闭, 无需主控处理.
