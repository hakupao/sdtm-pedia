# T2 B-CV writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `c3625c71927d082b12c9109f19843e08be519ace` (CV 文件改前 `git diff --quiet -- knowledge_base/domains/CV` = clean)
- md5: CV/examples.md `bfdb0efdc717cd8c284c9a11de6d9ae8` → `71e6f9abbe39847649e907a3202e464b` (32 行不变); CV/assumptions.md `e90e8012b03bc017acdec533debecba7` → `2fc68d6a9db973b6df5115de8e06ad80` (5 → 15 行); CV/spec.md 未动 `de8c6d00e0a9dddeadd8c872d509170e`
- 白名单: examples.md (batch json) + assumptions.md (主控授权: Description/Overview + spec 首句, CM/BE 先例, 逐字)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CV_writer/` (examples/assumptions.before.md, p286/288/289 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 1 (REAL_GAP) / t2_recheck 0; census DIFF 1 表 (3 CELL, KB 行 25/31/32); pdf_only 0; unparseable 0; out_of_scope 0.
- pdf_ranges 覆盖核 (O20): CV 节 = p286 下半页 "6.3.7.2 Cardiovascular System Findings (CV)" (无节引言 NOTE; Description/Overview + spec 首句 + spec 表首行; p286 上半页为 §6.3.7.1 通用表, 属 NV 批, 未碰) → p287-288 (spec 续 + 脚注 + Assumptions 1-2) → p289 (Examples Ex1/Ex2; 其后 p290 为 6.3.7.3 MK). batch lo/hi = 286-289 **完整覆盖**.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | CV/assumptions.md:3-5 | ig34_p0286_a017 | INSERTED | 新增 `## CV – Description/Overview` + p286 Description 句逐字 ("A findings domain that contains physiological and morphological findings…") | 286 |
| 2 | CV/assumptions.md:7-9 | spec 首句 (主控授权) | INSERTED | 新增 `## CV – Specification` + `cv.xpt, Cardiovascular System Findings — Findings. One record per …, Tabulation.` 逐字 | 286 |
| 3 | CV/assumptions.md:11 | 导航 (CM/BE 先例) | INSERTED | 新增 `## CV – Assumptions` 标题 (PDF p288 原标题), 原列表 1-2 未动 | 288 |
| 4 | CV/examples.md:25 | census:examples.md:25:1:CVTEST | REPLACED | `Native Cardiac Valve Structure Without Intervention Type` → `Native Cardiac Valve Intervention Type` (渲染图 + CT C139050 一致) | 289 |
| 5 | CV/examples.md:31 | census:examples.md:31:7:CVTEST | REPLACED | `Minor Axis Cross-sec Diameter, MVS` → `Minor Axis Cross-sec. Diameter, MVS` (渲染图 + CT C139052) | 289 |
| 6 | CV/examples.md:32 | census:examples.md:32:8:CVTEST | REPLACED | `Major Axis Cross-sec Diameter, MVS` → `Major Axis Cross-sec. Diameter, MVS` (渲染图 + CT C139053) | 289 |

- 覆盖率自查: atoms 1 = #1; census 3 格 = #4-6 (全部处理); 授权项 #2 (+ #3 导航标题).

### census 表处理

| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:23 Ex2 cv.xpt (3 CELL) | #4-6 | OK |
| examples.md:9 Ex1 cv.xpt | census OK; 渲染图人工逐格复核 5 行×15 列一致 | OK |

census_after (manifest 含 examples + assumptions): KB tables 2, OK 2, diffs 0.

### PDF_TYPO 清单
- 无. (Ex2 行 3-6 "Cross-sec" 无点 vs 行 7-8 "Cross-sec." 有点 — 与 CT C139050-C139053 各自一致, 非 PDF 错, 照录 PDF.)

### fp 回归说明
- `fp_match` 新 hit: ig34_p0286_a017 hit_target → CV/assumptions.md (改前 null).
- 回归 2 条 ig34_p0289_a024 / a025 (Ex2 行 7/8): pdf_atoms 的 verbatim 漏了 "Cross-sec." 的点 (baseline 即 `in_pdf_page: false`, ATOM_ERR 信号); KB 现按渲染图与 CT 为 "Cross-sec.", 回归属原子抽取错, 非 KB 退化.
- 其余 regress 条目 (p0118/p0174/p0215-p0263/p0311/p0363) 均非 p0286-0289 / CV, 为他批工作树改动.

### 双向全扫 (含表格原子)
- PDF→KB: p286 Description 句 + spec 首句 cmp IDENTICAL (复跑命令); p288 Assumptions 1-2、p289 Ex1/Ex2 引言 (pdftotext -raw 规范化) 均逐字在 KB; Ex1/Ex2 两张 cv.xpt 对 110dpi 渲染图逐格人工核: 表头/列序/列数/Row 列一致, 改后 0 差. spec 表 (p286-288) 属 spec.md, 不在本批.
- KB→PDF: examples.md / assumptions.md 全文件每行均有 PDF 对应; 无 KB 自写解释性内容 (D6 无), 无伪节号; `# CV — Examples`/`## Example N`/`**cv.xpt**` 为导航.

### 新增 atom 清单 (R3)
- 无 (spec 首句 #2 属主控授权项).

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:25/:31/:32 CVTEST 旧值 | 同行 | VALUE_DIFF 旧值替换 (#4-6) | — |

### 范围外发现
- 无.

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CV_writer; P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
pdftotext -f 286 -l 286 -layout "$P" - | grep -A1 "^A findings domain that contains physiological" | sed 's/^ *//;s/ *$//' | tr '\n' ' ' | sed 's/ $//' > $S/d_pdf; sed -n 5p knowledge_base/domains/CV/assumptions.md | tr -d '\n' > $S/d_kb; cmp $S/d_pdf $S/d_kb   # IDENTICAL
pdftotext -f 286 -l 286 -layout "$P" - | grep "^cv.xpt" | sed 's/ *$//' | tr -d '\n' > $S/s_pdf; sed -n 9p knowledge_base/domains/CV/assumptions.md | tr -d '\n' > $S/s_kb; cmp $S/s_pdf $S/s_kb   # IDENTICAL
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 2 / diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p028[6-9]' $S/fp_regress.jsonl   # a024/a025 (原子抽取错, 见上)
grep -n "CVTEST\|NCVALTYP\|MNDIAMVS\|MJDIAMVS" knowledge_base/terminology/core/other_part1.md   # CT 依据
for p in 286 288 289; do pdftoppm -f $p -l $p -r 110 -png "$P" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### git diff --stat
```
 knowledge_base/domains/CV/assumptions.md | 10 ++++++++++
 knowledge_base/domains/CV/examples.md    |  6 +++---
 2 files changed, 13 insertions(+), 3 deletions(-)
```
