# T2 B-ML writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `85d3057a666767b7beaadfc5a85ff11ee87a720b` (ML 文件改前无未提交改动; 基线取 `git show HEAD:<file>`)
- md5: ML/assumptions.md `8a8e578b3b026f55a0dec2c4613ecdae` → `71ef74961dbe7d91aa230fc617fe2c14` (15 → 25 行); ML/examples.md `90d9cb5c4818671036dda09d5b2c8ee2` → `9388a1f560175ab32cbdc9bd7d29976d` (73 行不变); ML/spec.md 未动 `6e3be1a41217bbd97757c7654b96b2ff`
- 白名单: examples.md + spec.md (batch json) + assumptions.md (主控通用授权: 仅 Description/Overview + spec 首句 + 节引言 NOTE, CM 先例, 逐字)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-ML_writer/` (*.before.md, p121-124 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl, speccheck.py)
- 本批 atoms 0 / t2_recheck 1 (不改, reviewer 判) / census DIFF 1 表 1 格 / pdf_only 0 / unparseable 3 / out_of_scope O4.
- 节页范围核 (O20): §6.1.4 ML = p121 (节标题 "6.1.4 Meal Data (ML)" + Description/Overview + spec 首句 + spec 表起) → p122 (spec 表末 + 脚注 + ML – Assumptions 1, 2 起) → p123 (2a/2b/3 + ML – Examples Ex1 引言/CRF 两张/Note/Rows 说明 + ml.xpt Row 1) → p124 (Rows 2-6 + Ex2 全部; 其后 p125 6.1.5 PR). batch lo/hi = 121-124 **完整覆盖**. 无节引言 NOTE, 无 References.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | ML/examples.md:66 | census:examples.md:66:2:MLTRT | SKIPPED_PDF_TYPO | KB 保留 `WHITE MILK`; PDF `WHTE MILK` → T-1 | 124 |
| 2 | ML/spec.md:3 | ig34_p0121_a005 (t2_recheck) | — (不改, reviewer 判) | spec.md:3 为 KB 结构行; 原句另已逐字补进 assumptions.md:9 (#4), 供 reviewer 判 | 121 |
| 3 | ML/assumptions.md:3-5 | Description/Overview (主控授权; = ig34_p0121_a003) | INSERTED | 新增 `## ML – Description/Overview` + p121 原句逐字 | 121 |
| 4 | ML/assumptions.md:7-9 | spec 首句 (主控授权; = ig34_p0121_a005) | INSERTED | 新增 `## ML – Specification` + `ml.xpt, Meal Data — Interventions. One record per …, Tabulation.` 逐字 | 121 |
| 5 | ML/assumptions.md:11 | PDF 节标题 "ML – Assumptions" (CM 结构) | INSERTED | 新增 `## ML – Assumptions` 标题 (列表本身未动) | 122 |
| 6 | ML/examples.md:55 | R3 新增 (Ex2 Group 2 Details 单元格, 词级改写) | REPLACED | 4 个 PDF 项目符号被改写为小写分号串 → 恢复 `<br>• Placing …` 4 项 (首字母大写、无分号、末项无句点), 逐字按 p124; `<br>` 先例 B-TS | 124 |
| 7 | — | O4 MLGRID | SKIPPED_ATOM_ERR | PDF p121 渲染图与 layout 均为 `MLGRPID`; KB spec.md:41 `MLGRPID` 正确; 笔误仅在原子 ig34_p0121_a011 (T1.1 spec NOT_FOUND 源); `grep -rn MLGRID knowledge_base` = 0 → KB 无需改, O4 ML 部分可关闭 | 121 |

- 覆盖率自查: atoms 0; t2_recheck 1 = #2; census 1 格 = #1; R3 新增 1 (#6); 授权项 3 (#3-5); O4 = #7.

### census 表处理

| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:63 Ex2 ml.xpt (1 CELL, :66 MLTRT) | #1 PDF_TYPO | DIFF 1 (= T-1, 预期残留) |
| examples.md:39 Ex1 ml.xpt | census OK; 渲染图 p123-124 逐格人工核 6 行 × 18 列一致 (MLDTC 仅 Rows 4-6, MLSTDTC Rows 1-4, MLEVLINT -P1W, RELMIDS "LAST MEAL PRIOR TO") | OK |
| unparseable :14 Meal Log CRF | 未触碰; 渲染图核: 勾选 (X) 位置、8 oz、日期/时间/Event ID 一致 | — |
| unparseable :25 DILI Meal CRF | 未触碰; 渲染图核一致 (2015 DEC 24) | — |
| unparseable :52 Ex2 Group/Arms/Details | **触碰 (#6)**, reviewer 须对 p124 渲染图人工逐格核 | — |

census_after: KB tables 5, OK 1, DIFF 1 (diffs 1 = T-1), UNPARSEABLE 3.

### PDF_TYPO 清单 (依据 = PDF 自身)
- T-1 (p124 Ex2 ml Row 2 MLTRT): PDF `WHTE MILK`; 同表 Row 8 `WHITE MILK`、Ex2 Details 文本 "white milk" → KB 保留 `WHITE MILK`.
- T-2 (p123 Ex1 引言第 2 项目符号, examples.md:8): PDF "occurrence of of prespecified" 重复词; KB "occurrence of prespecified" 保留正确 (未改动, 登记).

### fp_match (p121-124)
- 改后 EXACT 44 / PARTIAL 39 / EQUIVALENT 6 / MISPLACED 3 / INTENTIONAL_EXCLUDE 1; 与 baseline verdict 逐条比 **0 变化**; regress 中 `grep -E 'p012[1-4]|ML/'` = 0 (全量 regress 2 条 p0263/p0289 属他批).
- PARTIAL 39 中 37 条为 spec 表行 (p121_a007-a029, p122_a001-a014; spec.md 经人工逐变量核一致, 见下), a005 = t2_recheck (现 hit_target assumptions.md), p123_a019 = 折行假阳 (examples.md:31 逐字). MISPLACED p124_a022-a024 (Rows 7-9) 在 examples.md:71-73 逐字, matcher 噪声.

### 双向全扫 (含表格原子)
- PDF→KB: p121 Description + spec 首句 → assumptions.md:5/:9 (新增, `cmp` 逐字). p121-122 spec 表 37 变量 → spec.md: Label/Type/Role/Core/Notes 逐变量核 (speccheck.py 4-gram + 人工对 layout 折行), 0 差; Controlled Terms 列 `*` (MLTRT/MLCAT/MLSCAT) KB 空、`(NY)` 等以 C 码表示 = KB 全库约定 (见 F-2). p122 脚注 → KB 无 (F-1). p122-123 Assumptions 1-3 (含 1a-d, 2a-b) → assumptions.md:13-25 逐句一致. p123-124 Examples: Ex1 引言 + 2 项目符号 (T-2) / 2 CRF 标题与提示句 / Note / Rows 1-3, 4-6 / ml.xpt 6 行; Ex2 引言 / Group 表 (#6 后一致, 弯引号 “nudge” 见 F-3) / Food-card 2 句 / 表引导句 / ml.xpt 9 行 → examples.md 全部对应.
- KB→PDF: assumptions.md / examples.md 全文件每行有 PDF 对应; `# ML — Examples` / `## Example N` / `**ml.xpt**` / `**CRF: …**` 为导航; 无 KB 自写解释性内容 (D6 无), 无伪节号. spec.md 尾部 Cross References 为 KB 全库导航结构.

### 新增 atom 清单 (R3)
- #6 Ex2 Details 单元格 4 项目符号原文恢复.

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:55 小写分号串 "placing …; placing …; promoting …; placing … ." | 同行 | 词级改写恢复 PDF 原文 (#6; 该行仅承载此单元格) | — |

### 范围外发现
- F-1: spec 表脚注 (p122 "1 In this column, an asterisk (*) indicates …") ML 三文件皆无; 不在授权范围 (assumptions 仅限 Description/spec 首句/引言 NOTE; spec.md 本批仅限 batch json 问题与 O4) → 归 O15/O16 spec 扫描 (先例 GF/CO/MS 放在 assumptions.md spec 首句后). 原子 ig34_p0122_a015 文本 "CDISC/NCIBI" 为原子错, PDF 为 "CDISC/NCI".
- F-2: spec.md Controlled Terms 列不保留 PDF `*` 标记 (KB 全库约定, CM 等同) → 全库格式问题, 不在本批.
- F-3: examples.md:55 "nudge" 直引号 vs PDF 弯引号 → O40 全局引号口径, 未改.
- O4 (ML 部分): 见 #7, 可关闭.

### 触碰的 unparseable 表
- examples.md:52 Ex2 Group/Arms/Details (#6) — reviewer 须对 p124 渲染图逐格人工核.

### 需主控定
- 无 (F-1 若主控授权, 建议补在 assumptions.md:9 后, 用 GF/CO 格式 `> ¹In this column, …`).

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-ML_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-ML.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 1 / DIFF 1 (=T-1) / UNPARSEABLE 3
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p012[1-4]|ML/' $S/fp_regress.jsonl   # 0
for pat in "An interventions domain" "ml.xpt, Meal"; do a=$(grep -h "$pat" .work/10_tier_b_repair/work/pdf_pages/ig34_p0121.txt | sed 's/^ *//;s/ *$//'); b=$(grep -h "$pat" knowledge_base/domains/ML/assumptions.md); [ "$a" = "$b" ] && echo IDENTICAL; done
python3 -I $S/speccheck.py   # 37 vars; 4-gram miss 仅来自 layout 折行与 Core 列交错
for p in 121 122 123 124; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
grep -rn MLGRID knowledge_base   # 0
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 knowledge_base/domains/ML/assumptions.md | 10 ++++++++++
 knowledge_base/domains/ML/examples.md    |  2 +-
 2 files changed, 11 insertions(+), 1 deletion(-)
```
