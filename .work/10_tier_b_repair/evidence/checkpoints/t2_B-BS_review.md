# T2 B-BS reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- 范围: `git diff HEAD -- knowledge_base/domains/BS/` (本批未提交); 工作树内 RE/SM 改动属 B-RE / B-SM, 不在本批审查范围. BS/spec.md 无 diff.
- 输入: batch json `work/t2_batches/B-BS.json`, writer `evidence/checkpoints/t2_B-BS.md` + `work/t2_batches/B-BS.writer.jsonl`, PDF p196-199 (text + 渲染 110/300/500 dpi).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-BS_reviewer/`

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-BS_reviewer; mkdir -p $S
P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-BS.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
#  -> KB tables: 1; status: {'OK': 1}; cells compared: 84; diffs: 0; RESULT: RED / exit 1 仅因全局 PDF_ONLY 338 (页码均不在 p196-199 的 BS 表; 本批 pdf_only = 0)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
#  -> RESULT: RED (regress 48 条, 全部为 p118/174/215/218/254-263/363-374/396 他批工作树改动); grep -cE 'p019[6-9]|BS/' $S/fp_regress.jsonl = 0
#  p196-199 89 原子: EXACT 10 / EQUIVALENT 28 / INTENTIONAL_EXCLUDE 39 / PARTIAL 12, 与 baseline verdict 逐条 0 变化
pdftoppm -f 199 -l 199 -r 300 -x 290 -y 340 -W 1850 -H 450 -png "$P" $S/p199L; pdftoppm -f 199 -l 199 -r 300 -x 2100 -y 340 -W 1830 -H 450 -png "$P" $S/p199R
pdftoppm -f 199 -l 199 -r 500 -x 3500 -y 560 -W 1100 -H 520 -png "$P" $S/p199xfn
pdftoppm -f 196 -l 196 -r 110 -png "$P" $S/p196; pdftoppm -f 198 -l 198 -r 110 -png "$P" $S/p198
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42 (基线 42)
```
- 目标文件直查 (不依赖 hit_any): 对 pdf_atoms.jsonl 中 parent_section 含 BS 的 p196-199 原子逐条判 `norm(verbatim) in norm(BS/{assumptions,examples,spec}.md)`:
  p196_a016/a017/a018 (NOTE 3 句)、a019/a021 (标题)、a020 (Description)、a022 (spec 首句) → 均命中 BS/assumptions.md; p198_a009-a013 → assumptions.md; a014 未命中 (= T-3 --STRNLO, 见下);
  p198_a015-a019/a021/a022 → examples.md; a020 未命中 (= T-1); p199_a001/a002 → examples.md; p199_a003-a006 未字面命中, 原因是 pdf_atoms 本身把 VISITDY 抽成空 (渲染图为 1), KB 正确 → 下方逐格表.
  p196_a023-p198_a008 (spec 表 + 脚注) 属 spec.md 格式, 不在本批白名单 (writer F-1, 归 O15).

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| (无 FAIL / CONDITIONAL 项) | — | — | — |
| info-1 pdf_atoms p199_a003-a006 | 工具 | 原子 VISITDY 列为空, 渲染图每行为 1; 原子抽取缺陷, 非 KB 问题 (LOW) | p199 渲染 VISITDY 列 "1" ×4 |
| info-2 pdf_atoms p198_a012 | 工具 | 原子 verbatim 已含 "part of the", 而 PDF 原文为 "part the" (抽取时被纠正); 不影响 KB (LOW) | p198 "which is part the SEND terminology listing" |
| info-3 BS/examples.md:1 | 结构 (既有) | `# BS — Examples` vs PDF "BS – Example"; 改前既有导航标题, 未触碰, 不要求改 (LOW) | p198 "BS – Example" |

### G-TB4 表格: bs.xpt 人工逐格 (渲染 p199 300dpi + BSXFN 500dpi, 独立于 census 解析器)
表头 21 列 (Row STUDYID DOMAIN USUBJID BSSEQ BSREFID BSTESTCD BSTEST BSCAT BSORRES BSSTRESC BSSTRESN BSXFN BSNAM BSSPEC BSMETHOD BSRUNID VISIT VISITNUM VISITDY BSDTC) 列序/列名 一致.

| Row | 渲染图 vs KB (examples.md:17-20) |
|---|---|
| 1 | A12345 / BS / 43871 / 1 / 1148.26704 / A260A230 / A260/A230 / QUALITY CONTROL / 2.05 / 2.05 / 2.05 / 2.16.090.1.135764.3.4:7280912 / Deluxe Central Labs / rRNA / SPECTROPHOTOMETRY / 1000450001 / Baseline / 1 / 1 / 2005-03-21T11:28:17 — 21 格一致 |
| 2 | … / 2 / 1148.26704 / A260A280 / A260/A280 / QUALITY CONTROL / 2 / 2 / 2 / …3.4:7280912 / Deluxe Central Labs / rRNA / SPECTROPHOTOMETRY / 1000450001 / Baseline / 1 / 1 / 2005-03-21T11:28:17 — 21 格一致 |
| 3 | … / 3 / 1148.26704 / I28S18S / 28S/18S / QUALITY CONTROL / 1.2 / 1.2 / 1.2 / …3.4:7280912 / Deluxe Central Labs / rRNA / ELECTROPHORESIS / 1000450001 / Baseline / 1 / 1 / 2005-03-21T11:28:17 — 21 格一致 |
| 4 | … / 4 / 1148.26704 / RIN / RNA INTEGRITY NUMBER / QUALITY CONTROL / 9.5 / 9.5 / 9.5 / …3.4:7280912 / Deluxe Central Labs / rRNA / ELECTROPHORESIS / 1000450001 / Baseline / 1 / 1 / 2005-03-21T11:28:17 — 21 格一致 |

- BSXFN 500dpi 局部: "3.4:7280912" 为冒号 (非句点), 4 行相同; `pdftotext -layout` 亦为冒号. writer 7 格改动 (#2-8) 全部正确. I28S18S 首字为大写 I, 与 p198 Row 3 叙述 "prefixed with an "I"" 一致.

### atom / PDF_TYPO 判定
| atom | writer action | reviewer 判定 | 依据 |
|---|---|---|---|
| ig34_p0198_a020 | SKIPPED_PDF_TYPO (T-1) | 成立 | 逐词 diff PDF vs KB:7 仅 2 处: "rations"→"ratios", "may indicated"→"may indicate"; 同句后半 "Any ratios outside…" 与情态动词语法可由 PDF 自身确定正确值 |
| T-2 (Assumption 3, 仅登记) | KB 保留 "part of the" | 成立 | p198 "which is part the SEND terminology listing"; 逐词 diff 仅缺 "of" |
| T-3 (Assumption 5, 仅登记) | KB 保留 --STNRLO | 成立 | p198 "--STRNLO, --STNRHI, --STNRC"; 同列表 --STNRHI/--STNRC 与 Findings 通用变量 --STNRLO 确定正确值; 另一处差异 "-- CSTATE" 为折行连字 |
- t2_recheck: 0 条, 无 R2 判定.

### G-TB6 反向溯源 (diff 每行)
| KB 行 | 内容 | 出处 / 签字 |
|---|---|---|
| assumptions.md:3 | 节引言 NOTE 3 句, 末 "…publication, after v3.4." | p196 §6.3.5.2 引言框逐字 (p196 版; §8.8 p439 版止于 "future SDTMIG." 属 RELSPEC/ch08, 不混用) ✔ |
| assumptions.md:5 | `## BS – Description/Overview` | 结构行, p196 PDF 原标题 (U+2013 en dash 与 PDF 字节一致) ✔ 签字 |
| assumptions.md:7 | Description 句 | p196 逐字 ✔ |
| assumptions.md:9 | `## BS – Specification` | 结构行, p196 PDF 原标题 ✔ 签字 |
| assumptions.md:11 | `bs.xpt, Biospecimen Findings — Findings. One record per …` | p196 spec 首句逐字 ✔ |
| assumptions.md:13 | `## BS – Assumptions` | 结构行, **已对 p198 渲染图核实为 PDF 原小标题** "BS – Assumptions" (位于 spec 脚注之后、列表 1 之前), 与 BE/CM 先例同构 → 授权内 ✔ 签字 |
| assumptions.md:4/8/12/14 | 空行 | 格式 |
| examples.md:17-20 | 7 格替换 | 见逐格表 ✔ |
- 无出处词句: 0. 无 KB 自写解释性内容 (D6 无), 无伪节号.

### 双向全扫 (BS 节 p196 下半 - p199 上半, 含表格原子)
- PDF→KB: p196 NOTE/Description/Spec 首句 → assumptions.md:3/7/11; p196-198 spec 表 + 脚注 → spec.md (白名单外, 未核, 同 writer F-1); p198 "BS – Assumptions" + 1-5 → assumptions.md:13-23 (逐词 diff 仅 T-2/T-3 + 折行); p198 "BS – Example"/"Example 1"/4 段叙述 → examples.md:1-11 (a017-a019/a021/a022 EXACT, a020 = T-1); p199 bs.xpt 标签 + 表头 + 4 行 → examples.md:13-20 (逐格一致). 缺失 0.
- KB→PDF: assumptions.md 23 行、examples.md 20 行逐行均有 PDF 对应; 导航行 `# BS — Assumptions` / `# BS — Examples` / `## Example 1` / `**bs.xpt**` / `**Rows 1-2:**` 等为既有导航, 未改.
- 位置: NOTE/Description/Spec 首句置于 H1 与 Assumptions 列表之间, 与 BE (同节 NOTE) / CM 先例一致.

### 无副作用
- BS diff 仅 assumptions.md (+12) 与 examples.md (4 行替换), 均在白名单/授权内; 授权范围外 (assumptions 列表 1-5、examples 叙述、spec.md) 无改动; 原有标题/锚点未变; 表格已有正确格未被改坏 (逐格表).
- writer F-2 (live docs 44) 已关闭: 现为 42.

### Positive
- writer 正确区分 p196 版与 §8.8 版 NOTE 末句; BSXFN 冒号用 400dpi 局部确认; PDF_TYPO 均附 PDF 自身依据.
