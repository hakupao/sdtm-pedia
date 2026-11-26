# T2 B-GF writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `3c716a7ec388607cbeb64f4e1903959df799e4a6`
- md5 before: GF/examples.md `5230375406febc9dd42347932bd8415d`; after `689f017772e1dbe0847193842d80c78f` (行数 182 → 188, +6 = Ex1 DI 句 + 空行, Ex5 两段 + 空行)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-GF_writer/`
  (examples.before.md, tbl.py = bbox 词框按表头 x 起点分列的独立解析, apply.py = Ex1/Ex2/Ex4 整表重建 + 精确替换 + 命中次数断言 + 列数断言, prose_scan.py,
  census_before/after.json, fp_before/after.jsonl, p225-228 整页 110dpi + Ex1 (3 段)/Ex2 (2 段)/Ex4 (2 段)/MB 表 200-220dpi 裁切渲染图)
- 数据来源: 所有改动格逐格对照渲染图; tbl.py (bbox) 与 census 解析器 (独立实现) 双重比对一致. 叙述对照 `work/pdf_pages/ig34_p0224-0228.txt`.
- 本批 atoms 3 (VALUE_DIFF 2 / REAL_GAP 1) / t2_recheck 0; census DIFF 4 表 (339 diffs) 全部处理; pdf_only 0; unparseable 0; out_of_scope 0.
- 跨行折行合并: GFXFN `…_LCNL-` + `361/…` → `LCNL-361/…` (路径内连字符, census 解析器同样读作 `LCNL-361`); USUBJID `C12345-001`; GFREFID `4401470-2-6`; GFRUNID `MSI-010418`; 日期 `2018-05-22` / `2020-06-25` / `2020-02-04`.
- 空格式: 新表空格写 `| |` (同文件惯用, 改前文件无 `|  |`).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | GF/examples.md:27-37 | ig34_p0225_a004 + census:27 (HEADER 11 列 + CELL 212) | TABLE_REBUILT | 整表替换: KB 为 BRAF p.Val600Glu / GRCh38.p13 / rs121913227 / VISITDY -25 等 (与 PDF 全不符) → PDF: SPDEVID ACME GenePanel 500, GFGRPID 1/2, GFREFID TRF001338, r1-5 ATM (chr 11, 108175462, ENST00000278616.4, COSM41596), r6-9 CDKN2A (chr 9, 21967751, ENST00000579755.1, COSM12473), GFTESTCD SNV/CPNUMVAR, GFINHERT SOMATIC VARIATION, GFGENREF GRCh37.75, GFXFN 路径, GFNAM ACME SEQUENCING LLC, GFMETHOD TARGETED GENOME SEQUENCING, VISIT Day 1, GFDTC 2018-05-22, GFDY 2. 表头 33 列按 PDF (删 GFSTREFN/GFINHERTG/GFGENSR/GFCOPYID/GFRUNID; 增 SPDEVID/GFGRPID/GFORRESU/GFSTRESN/GFINHERT/GFXFN) | 225 |
| 2 | :62-66 | ig34_p0225_a017 + census:60 (HEADER + CELL 43) | TABLE_REBUILT | 表头 29 列按 PDF (增 GFORREF/GFSTREFC/GFSYMTYP, GFINHERTG→GFINHERT, 删 GFSTREFN/GFGENSR); GFSEQ 1/2/3; GFREFID NA18537/NA07000/NA00131; GFORRES/GFSTRESC T/T, G/T, G/G; GFORREF/GFSTREFC G/G; GFCHROM/GFGENREF 全 3 行填; GFGENLOC 4:88131171; GFNAM ACME LABS; GFMETHOD REAL_TIME POLYMERASE CHAIN REACTION (U-1); GFDTC 2020-06-25 (旧 空/空/"2020-06-3"); GFDY -3 | 225 |
| 3 | :126-133 | census:124 (HEADER + ROW_SHAPE 6 + CELL 72) | TABLE_REBUILT | 表头补 GFGENSR (GFSTRESC 后; KB 原表头漏此列致 r2-6 列错位); r1 GFTSTDTL MSI-Stable → MICROSATELLITE INSTABILITY OVERALL STATUS, r1 补 GFXFN msi_abc_gf.csv; GFRUNID MS-D10418 → MSI-010418 (×6) | 227 |
| 4 | :145 | census:141 r1 MBREFID, MBORRES | REPLACED | MBREFID INFLU0101.1 → INFLU0101 (照录, U-2); MBORRES "INFLUENZA A VIRUS SUBTYPE" → "… SUBTYPE H3N2" | 227 |
| 5 | :145 | census:141 r1 MBTEST | SKIPPED_PDF_TYPO | T-2: KB "Identification" 保留 (PDF "Idenitifcation") | 227 |
| 6 | :149 | ig34_p0227_a021 | INSERTED | Ex5 段 "The GFTEST "Single Nucleotide Variation" is used for SNP tests. …" (5 句, 逐字), 置于 "Findings from this testing …" 段后 (PDF 顺序) | 227 |
| 7 | :151 | R3 N-2 (ig34_p0227_a022) | INSERTED | Ex5 段 "Note the use of NHOID, … study subject/host." 逐字 (KB 本文件缺; 仅在 GF/assumptions.md:47 错位存在, fp 因此命中 assumptions) | 227 |
| 8 | :41 | R3 N-1 (ig34_p0225_a006) | INSERTED | Ex1 DI 段后补 "The DI example shows the device type and manufacturer for the device identified as ACME GenePanel 500." (按渲染图/layout 原文; 原子文本 "DI domain example" 为 ATOM_ERR) | 225 |
| 9 | :70 | T-3 (ig34_p0225_a019) | REPLACED | "respresented" → "represented" (PDF 拼写错, KB 写正确拼写) | 225 |
| 10 | :167 | T-4 (ig34_p0228_a009) | REPLACED | "GFLINKID matches MSLNKID" → "GFLNKID matches MSLNKID" | 228 |
| 11 | :5 | T-1 (ig34_p0224_a013) | SKIPPED_PDF_TYPO | KB "inheritability" 未动 (PDF "inheritabilty") | 224 |
| 12 | :155 | T-5 (ig34_p0228_a002) | SKIPPED_PDF_TYPO | KB Row 1 句末句号未动 (PDF 漏句号) | 228 |

- atoms 覆盖率自查: atoms 3 = 变更清单 atom 行 #1 (a004) + #2 (a017) + #6 (a021). 跳过 0.

### census 表处理

| census ref (before 行号) | 处理 | 结果 |
|---|---|---|
| :27 Ex1 gf.xpt (213 = HEADER 1 + CELL 212) | #1 整表重建 | OK |
| :60 Ex2 gf.xpt (44 = HEADER 1 + CELL 43) | #2 整表重建 | OK |
| :124 Ex4 gf.xpt (79 = HEADER 1 + ROW_SHAPE 6 + CELL 72) | #3 整表重建 | OK |
| :141 Ex5 mb.xpt (3) | #4-5 | DIFF 1 残留 = MBTEST (T-2) |

- 汇总: before `OK 6 / DIFF 4, cells 1192, diffs 339` → after `OK 9 / DIFF 1, cells 1206, diffs 1 (= T-2)`. Ex3 gf/di, Ex1 di, Ex5 gf/ms/relrec 改前即 OK, 另用 tbl.py 复核一致, 未动.
- writer.jsonl 364 行 = 3 atoms + census 355 (HEADER diff 按列展开: Ex1 11 / Ex2 7 / Ex4 7 列) + R3 2 + T 4.

```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-GF_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-GF.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # 改前同法 census_before.json
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl                                       # 改前同法 fp_before.jsonl
python3 -I $S/prose_scan.py
python3 -I $S/tbl.py .work/10_tier_b_repair/work/pdf_bbox/ig34_p0225.tsv Row 116 262   # 独立 bbox 分列 (末行会混入下方叙述, 末行以渲染图为准)
python3 tools/check_links.py | tail -1   # live docs: 42 (基线 42)
```

### fp_match (全量 6636 原子前后对比)
- 回归 0; target 变更 0. GF 新命中 3: ig34_p0227_a018 (MB 行), ig34_p0227_a021, ig34_p0228_a009 (GFLNKID).
  另有 p0133-p0142 新命中 14 条, 非本批 (fp_before/after 之间工作树中他批文件的改动), 不计入.
- 预期回归 (PDF_TYPO 修正): **0**. T-3 (a019 原子文本为 "rerspresented", 改前即未命中) 与 T-4 (a009 原子文本为 GFLNKID, 改后反而命中) 都不产生回归; T-1/T-2/T-5 KB 未动.
  若台账按 PDF 原文精确匹配: T-1 (p0224_a013)、T-3 (p0225_a019) 两条保持未命中, 是预期状态.
- 改后 p224-228 仍未命中 (均非 KB 缺失):
  - PDF_TYPO: ig34_p0224_a013 (T-1), ig34_p0225_a019 (T-3; 原子另含 "rerspresented" 抽取错).
  - FIGURE 描述原子: ig34_p0225_a004 / a017 (表已按 PDF 重建, 原子是一句描述).
  - ATOM_ERR: ig34_p0225_a006 ("DI domain example", PDF 为 "DI example"); ig34_p0226_a008-a024 (T1 已知 GFSRPD/ABU3908AS2/GFTSTOTL 等编造); ig34_p0227_a006-a012 (表头 "GFGENSER"、缺 VISITDY、VISIT "VISIT" 无 "1", 渲染图为 GFGENSR/VISITDY/VISIT 1); ig34_p0228_a011 (漏 "extracted").
  - ig34_p0224_a010 = GF assumption 9, 属 GF/assumptions.md (非本批).

### 双向叙述扫描 (R3; prose_scan.py)
- PDF→KB: p224 "GF – Examples" 起至 p228 §6.3.5.5 前的全部 SENTENCE/LIST_ITEM/NOTE 原子归一后子串检查 KB. 改后未命中 4 = p0224_a013 (T-1), p0225_a006 (ATOM_ERR), p0225_a019 (T-3), p0228_a011 (ATOM_ERR). 均已解释.
- KB→PDF: KB 叙述行按句切分, 在同范围 layout 文本 (去页脚, 跨页连续) 归一后子串检查. 改后未命中 4 句 = :5 (T-1), :70 (T-3), :155 (T-5), :167 (T-4). 无 KB 自写 / 超出 PDF 的句子.
- 改前额外缺失、已在本 attempt 修: N-1 (:41), N-2 (:151), a021 (:149).
- 未做 (仅段落切分): PDF "Next, a series …" 与 "Findings from this testing …" 为两段, KB 合为一段 (:147); 内容逐字一致, 未拆.

### 新增 atom 清单 (R3)
- N-1 :41 ig34_p0225_a006 (Ex1 DI 引导句); N-2 :151 ig34_p0227_a022 (Ex5 NHOID Note 段).

### 删除清单 (reviewer 逐条确认)

| # | 原位置 (base 行号) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | :27-37 Ex1 gf.xpt 表头 + 9 行全部旧值; 列 GFSTREFN / GFINHERTG / GFGENSR / GFCOPYID / GFRUNID | :27-37 PDF 重建表 | VALUE_DIFF 旧值替换 / 表头跟 PDF (规则 3); 删除列 PDF 无 | — |
| D-2 | :60-64 Ex2 gf.xpt 表头 + 3 行旧值; 列 GFSTREFN / GFINHERTG / GFGENSR | :62-66 PDF 重建表 | 同上 | — |
| D-3 | :124-131 Ex4 gf.xpt 表头 + 6 行 | :126-133 PDF 重建表 (仅增列/改值, 无删列) | 同上 | — |
| D-4 | :143 MBREFID ".1" 后缀、:68 "respresented"、:161 "GFLINKID" | 见 #4/#9/#10 | 旧值替换 | — |

### PDF_TYPO 清单 (正确值可由 PDF 自身确定 → KB 写正确值)

| # | 位置 | PDF | KB | 依据 |
|---|---|---|---|---|
| T-1 | :5 Ex1 引言 | "inheritabilty" | "inheritability" | 拼写错; p225 Ex2 引言拼作 "inheritability". KB 未动 |
| T-2 | :145 MB r1 MBTEST | "Microbial Organism Idenitifcation" | "Microbial Organism Identification" | 同页叙述明载 MBTEST = "Microbial Organism Identification". census 残留 1. KB 未动 |
| T-3 | :70 Ex3 引言 | "respresented" | "represented" | 拼写错 (KB 原照抄 PDF, 本次改正) |
| T-4 | :167 Ex5 MS 引导段 | "GFLINKID matches MSLNKID" | "GFLNKID" | 同例 gf.xpt 表头、relrec IDVAR 及 p228 首句均为 GFLNKID (KB 原照抄 PDF, 本次改正) |
| T-5 | :155 Ex5 GF Row 1 | 句末无句号 | 有句号 | 标点; 同列其他 Row 说明均以句号结尾. KB 未动 |

### 照录 PDF, 供主控 / T4 用户裁 (KB = PDF)
- **U-1 Ex2 GFMETHOD "REAL_TIME POLYMERASE CHAIN REACTION" (:64-66, ×3)**: 下划线疑为印刷错 (同例引言 "real-time polymerase chain reaction"); KB CT 仅有 C51962 "REAL-TIME POLYMERASE CHAIN REACTION ASSAY" (terminology/core/general_part3.md:373), 与 PDF 去下划线后仍不等 (多 ASSAY), 正确值不可单值确定 → 照录. 原 KB 值 "REAL TIME POLYMERASE CHAIN REACTION". 用户可裁: 照录 / 改 "REAL-TIME …" / 改 CT 全称.
- **U-2 Ex5 MB r1 MBREFID "INFLU0101" (:145)**: 同例 GF r1 / MS r1 的 --REFID 为 "INFLU0101.1"; 可能有意 (原样本 vs 分装) 也可能漏 ".1" → 照录 PDF.
- 已核非问题: Ex1 VISIT "Day 1" / VISITDY 1 / GFDY 2 与 Ex2 VISITDY -1 / GFDY -3 均为 PDF 原值; Ex1 叙述 Row 4 "number of times the locus … was observed" 对应 GFTSTDTL READ DEPTH, 不矛盾.

### 范围外发现 (主控决定)
- **O-GF-1 GF/assumptions.md:43-47**: KB 自写节 "## GF – Example 4 (p227)" 内含 Ex4 引言 (= examples.md:118 副本) + Ex5 NHOID Note 段 (= 本次 examples.md:151 补入). 按 D2 应删除 / 替换为交叉引用; 不在本批白名单, 未动. 若删除, fp ig34_p0227_a022 的 hit_target 会转到 examples.md (仍命中).

### 触碰过的 unparseable 表
- 无.

### git diff --stat
```
 knowledge_base/domains/GF/examples.md | 60 +++++++++++++++++++----------------
 1 file changed, 33 insertions(+), 27 deletions(-)
```
- `git status`: 本批只改 knowledge_base/domains/GF/examples.md (其他 M/?? 为他批既有改动, 未触碰). 未 commit.

## attempt 1 续 (主控追加: kb_files 扩入 GF/assumptions.md, 处理 O-GF-1 + assumptions 全文双向扫描)

- GF/assumptions.md md5 before `0085498642526060493ace205dc24903` (47 行) → after `87a19802de7f02fcaa5061d44c437f92` (43 行). examples.md 未再改 (md5 仍 `689f017772e1dbe0847193842d80c78f`).
- 锚点检查 (不截断): `grep -rn --exclude-dir=node_modules --exclude-dir=.git -i "example-4-p227\|gf--example-4\|gf-example-4" .` → 无命中 (rc=1); `grep -rn "GF/assumptions.md#" .` → 无命中 (rc=1). 删除标题无入链.
- 双向扫描: `python3 -I $S/prose_scan_assm.py` (p220 §6.3.5.4 起至 p224 "GF – Examples" 前; KB 句→PDF layout, PDF 原子→KB). 范围: Description p220, Spec 说明/脚注 p221/p223, Assumptions 1-9 p223-224.

### 变更清单 (续)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 13 | GF/assumptions.md:15 | R3 N-3 ig34_p0223_a012 | REPLACED | 脚注 "CDISC/NCI codelists will be available in CDISC Controlled Terminology, available at https://…" (PDF 无, 与 PDF 不符) → PDF "CDISC/NCI codelist values are enclosed in parentheses." | 223 |
| 14 | GF/assumptions.md:43 (base :43-47) | O-GF-1 | REPLACED (D2 去重) | KB 自写节 "## GF – Example 4 (p227)" + Ex4 引言副本 + Ex5 NHOID Note 副本 → 一行 `> See [Example 4](examples.md#example-4) and [Example 5](examples.md#example-5) for this content.` | 227 |
| 15 | GF/assumptions.md:41 | T-6 ig34_p0224_a010 | SKIPPED_PDF_TYPO | KB "ORNRHI, --STNRLO" 未动 (PDF "ORNRHI,--STNRLO" 逗号后缺空格; 同列表其余项均 ", --") | 224 |

- 其他: Description p220 在 PDF 为一段, KB 拆为 3 段 (:5/:7/:9), 内容逐字一致, 未动. Assumptions 1-8 逐字一致.
- 双向扫描改后残留: KB→PDF 仅 :41 (T-6) 与 :43 (交叉引用, 纯导航); PDF→KB 仅 ig34_p0224_a010 (T-6). 改前另有 :15 / :45 / :47 三处, 已修.

### 删除清单 (续)

| # | 原位置 (base 行号) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-5 | GF/assumptions.md:43 "## GF – Example 4 (p227)" | 删 | KB 自写标题 (PDF assumptions 页无此节); 无入链 (见锚点检查) | — |
| D-6 | GF/assumptions.md:45 Ex4 引言 "This example shows findings from an assessment of microsatellite instability…" | 删 → :43 交叉引用 | D2 去重: PDF p227 Ex4 内容, 非 assumptions 页原文 | GF/examples.md:118 |
| D-7 | GF/assumptions.md:47 "Note the use of NHOID, … study subject/host." | 删 → :43 交叉引用 | D2 去重: PDF p227 Ex5 内容, 非 assumptions 页原文 | GF/examples.md:151 (本 attempt 补入) |
| D-8 | GF/assumptions.md:15 脚注后半 "codelists will be available … https://www.cancer.gov/…" | 换为 PDF 原文 | 与 PDF 不符 (旧版措辞), 旧值替换 | — |

### 验证 (续)
- fp_match 全量 (vs 本 attempt 改前 fp_before): 回归 0; GF 新命中 4 (p0223_a012, p0227_a018, p0227_a021, p0228_a009); hit_target 变更 2 (p0227_a002、p0227_a022: assumptions.md → examples.md, 仍命中, 符合归属).
- census (manifest 加 assumptions.md p220-224): OK 9 / DIFF 1 (= T-2 MBTEST), diffs 1; assumptions.md 无表.
- check_links: live docs 42 (基线 42).
- git diff --stat: GF/assumptions.md 8 (+4/−4 行级), GF/examples.md 60; 共 2 files, 35 insertions(+), 33 deletions(-).

## attempt 1 续 2 (reviewer CONDITIONAL 后修正: C-1 + LOW)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 16 | GF/assumptions.md:41 | C-1 / T-6 ig34_p0224_a010 | REPLACED | "--ORNRLO, ORNRHI, --STNRLO" → "--ORNRLO, --ORNRHI, --STNRLO" | 224 |
| 17 | GF/assumptions.md:43 | LOW (O-GF-1 交叉引用措辞) | REPLACED | 去掉无指代的 "for this content" → "> See [Example 4](examples.md#example-4) for the microsatellite instability example and [Example 5](examples.md#example-5) for the NHOID note." | 227 |
| 18 | GF/examples.md:147-149 | LOW (段落切分) | REPLACED | "Next, a series … testing)." 与 "Findings from this testing …" 按 PDF 拆回两段 (插空行; 文字不变). 此后行号 +2: a021 段 :151, NHOID Note :153, GFLNKID 句 :169 | 227 |

- **T-6 重登记** (替代续 1 的 T-6 "KB 未动"): PDF "ORNRHI,--STNRLO" 有两处印刷错 — ORNRHI 缺 "--" 前缀，逗号后缺空格。同一列表其余 21 项均带 "--"，且以 ", " 分隔，正确值可由 PDF 自身确定，所以 KB 写 "--ORNRHI" 并保持 ", --STNRLO"。
- md5 after: assumptions.md `4dc691a9138d65f67ee0bc7b06138a3a`, examples.md `177549cde963a5bef080b00317476c66`.
- fp_match 全量: 回归 0 (相对续 2 改前与相对 attempt 1 改前均为 0). 因 --ORNRHI 改正不再命中的原子: **无** — ig34_p0224_a010 改前改后均未命中 (hit_target None → None; 原子文本照录 PDF "ORNRHI,--STNRLO"); 本 attempt 全程该原子即 T-6 预期未命中项. 新命中 5 条 (p0032/p0134/p0185) 非 GF, 为他批工作树改动.
- 双向扫描 (prose_scan_assm.py): 残留仅 :41 (T-6) 与 :43 (纯导航交叉引用); PDF→KB 仅 p0224_a010 (T-6).
- check_links: live docs 42 (基线 42). 未 commit.
