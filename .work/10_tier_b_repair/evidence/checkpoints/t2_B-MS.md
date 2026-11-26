# T2 B-MS writer checkpoint — attempt 1

- base HEAD 396482e; MS/examples.md md5 before dd01d4c678ab0f67a0c7953b2248f6ac (73 行) → after bb0cfc859110c5c0b5f29956dbeee3f7 (81 行). 仅改 kb_files (MS/examples.md).
- 参照 md5 (未改): MB/examples.md 8dd0a328…, MB/assumptions.md c5bacee5…, MS/assumptions.md 4b19662d…
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-MS_writer/` (examples.base.md, manifest.json, census_before/after.json, p257/259/262/263 渲染 110dpi)
- 命令 (repo 根, S=上面 scratch):
```
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_before.json  # {'DIFF': 2, 'OK': 2}; diffs: 68
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # {'DIFF': 1, 'OK': 3}; diffs: 1 (= T-1)
python3 tools/check_links.py | tail -1   # live docs: 45; 与 MS/MB 无关 (新增 3 条来自并行批 t2_B-GF*.md 证据文件), MS/examples.md 无断链
git diff --stat -- knowledge_base/domains/MS/examples.md   # 1 file changed, 34 insertions(+), 26 deletions(-)
```

## MB/MS 跨文件重复归属裁定 (D2)
- PDF §6.3.5.7.3 为 MB/MS 共用节, 节号无法判归属. 沿用已提交 O-a 先例 (Ex3 的 MS 叙述 + ms/suppms 在 MS, MB 留指针): **每个 Example 的 MS 段 (MS 叙述 / Rows 说明 / ms.xpt / suppms.xpt) 归 MS/examples.md; 共用引言 + BE/BS/RELSPEC/MB/DI/RELREC 段归 MB/examples.md**. MS 文件内对应改为一行指针指 MB.
- 由此 MB/examples.md Ex1 (:20-53 MS 叙述 + Rows + ms.xpt) 与 Ex2 (:124-145 Rows + ms.xpt) 成为非所属副本, 应换一行交叉引用 — **MB/examples.md 不在本批 kb_files, 未改, 交主控** (建议行: `> See [MS Example 1](../MS/examples.md#example-1) for the MS description, Rows notes and ms.xpt table of this example.`; Ex2 同式 `#example-2`). 现两份均已按 PDF 逐格对 (MB 副本 B-MB 已审), 过渡态无错值, 仅 Ex1 r9 MSSTRESC 两份不一致 (见 T-1).

## 变更清单
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | MS:7 | D2 导航 | INSERTED | Ex1 指针 → MB Example 1 (mb/relrec) | 256-257 |
| 2 | MS:9 | KB_AUTHORED (D6) | REPLACED | Ex1 首句 KB 自写摘要 → 加 `> KB note (not in SDTMIG):` 前缀, 不与 PDF 矛盾 | — |
| 3 | MS:11 | R3 新增 atom N-1 | INSERTED | Ex1 MS 叙述段 (After E. faecalis … grouped together using MSGRPID) 逐字; 原改写句删去 KB 扩写 "(see MB Example 1)" | 256-257 |
| 4 | MS:13 | R3 新增 atom N-2 | INSERTED | "The third method, macro broth dilution …" 段逐字 | 257 |
| 5 | MS:23-26 | census:MS:15 r1-4 MSLNKGRP | REPLACED | 空 → 1 | 257 |
| 6 | MS:23,25 | census:MS:15 r1,r3 MSCONC/MSCONCU/MSSTRESN/MSSTRESU | REPLACED | r1: MSCONC 0.25/ug/dL→空, MSSTRESC 空→0.25, MSSTRESN 空→0.25, MSSTRESU 空→ug/dL; r3 同式 (1) | 257 |
| 7 | MS:29-32 | census:MS:15 r7-10 MSDTC | REPLACED | 2005-06-19T08:00 → 2005-06-26T08:00 | 257 |
| 8 | MS:31 | census:MS:15 r9 MSSTRESC | SKIPPED_PDF_TYPO | KB 保留 25 (PDF 空), 见 T-1 | 257 |
| 9 | MS:36 | D2 导航 | REPLACED | KB 自写句 "Susceptibility testing results from the sputum multi-visit study (see MB Example 2)." → 一行指针 → MB Example 2 | 257-258 |
| 10 | MS:39 | R2 | REPLACED | Rows 3-4 "and found" → "and was found" | 259 |
| 11 | MS:40 | R2 | REPLACED | Rows 5-8 补 "from the same subject" | 259 |
| 12 | MS:41 | R2 | REPLACED | Rows 9-10 "is still … to penicillin" → "was still … to this drug" | 259 |
| 13 | MS:45-56 | census:MS:39 (header + r1-10) | TABLE_REBUILT | 按 PDF 18 列: 列序 MSSEQ, MSREFID, MSGRPID; 删 MSNAM/VISITNUM/VISIT (PDF 无); MSGRPID 空→1,1,2,2,3,3,4,4,5,5; r3 0.125→0.023; r5 0.19→0.125; r7 4.9→0.023; r8 SUSCEPTIBLE→INTERMEDIATE; r9 4.8→0.026; r10 SUSCEPTIBLE→INTERMEDIATE; r5-8 日期 06-26 不变; r9-10 2005-07-01→2005-07-06 | 259 |
| 14 | MS:60 | D2 导航 | INSERTED | Ex3 指针 → MB Example 3 (BE/SUPPBE/BS/RELSPEC/MB/SUPPMB/DI/RELREC) | 259-263 |
| 15 | MS:62 | R3 / B-MB review | REPLACED | 删 KB 扩写 "from the gastric TB study (see MB Example 3)"; "a culture medium" → "the culture medium"; 补 PF 句 (Genotypic tests that give results of specific genetic polymorphisms … PF domain …) | 262 |
| 16 | MS:65 | PDF_TYPO T-2 | SKIPPED_PDF_TYPO | KB 保留 MSCONCU (PDF 写 MSCONU) | 262 |
| 17 | MS:69-74, 78-79 | Ex3 ms.xpt / suppms.xpt | 核对无改 | 渲染逐格与 KB 一致 (census OK) | 262 |

atoms[]: 0 条 (本批无 atoms); census DIFF 表 2/2 已处理 (:15 → #5-8, :39 → #13); kb_lines_with_diff 全覆盖 (17-20 #5/#6, 23-26 #7/#8; 41-50 #13); pdf_only 0.

### 新增 atom 清单 (R3, 非 atoms)
N-1 MS:11 p256-257 Ex1 MS 叙述 6 句; N-2 MS:13 p257 macro broth dilution 段 3 句; N-3 MS:62 p262 PF 句.

### 删除清单 (D2)
| # | 位置 (base) | 内容 | 原因 | 保留 / 替代 |
|---|---|---|---|---|
| D-1 | base:7 | 句中 "(see MB Example 1)" | KB 扩写嵌入 PDF 句 | MS:7 导航指针 |
| D-2 | base:30 | "Susceptibility testing results from the sputum multi-visit study (see MB Example 2)." | KB 自写导航摘要, PDF 无 | MS:36 指针; PDF 原引言在 MB/examples.md Ex2 |
| D-3 | base:54 | "from the gastric TB study (see MB Example 3)" 短语 | KB 扩写 (B-MB review O-a 连带) | MS:60 指针 |
| D-4 | base:39-50 | Ex2 表 MSNAM / VISITNUM / VISIT 3 列 | PDF p259 表无此 3 列 (表格跟 PDF 走) | — |

### KB_AUTHORED 保留清单
- MS:3 `*Note: MB and MS share a combined examples section …*` — 纯导航, 与 PDF 不矛盾, 保留.
- MS:7 / :36 / :60 三条 `> See [MB Example N]…` — D2 交叉引用 (纯导航).
- MS:9 KB note (D6) — 解释性, 不矛盾.

## PDF_TYPO 清单
| T | 位置 | PDF | KB | 依据 |
|---|---|---|---|---|
| T-1 | MS:31 Ex1 ms r9 MSSTRESC | 空 | 25 (保留) | 同行 MSORRES 25 / MSSTRESN 25, 同表 r7 MSSTRESC=23 同式; 可由 PDF 自身确定. **注意 MB/examples.md:52 同格为空 (B-MB 照录 PDF)**, 两份不一致 → 主控统一 (若 MB 换成指针则自然消解) |
| T-2 | MS:65 Ex3 Rows 3-4 | MSCONU | MSCONCU | 变量名拼写错, 同句前文与 Rows 1-2 均为 MSCONCU |
| T-3 (候选, 未改) | MS:78-79 suppms IDVAR | MBREFID (RDOMAIN=MS) | 照录 | IDVARVAL 100.4/100.5 = ms MSREFID, 疑应为 MSREFID; 非 PDF 自证 → T4 用户裁定 |
| T-4 (候选, 未改) | MS:78-79 suppms QNAM | MSMEDTYPE (9 字符) | 照录 | QNAM ≤8 字符; MB 对应为 MBMEDTYP → T4 用户裁定 |

## 范围外发现 (未改)
- O-1 **MB/examples.md** Ex1 :20-53、Ex2 :124-145 MS 段需换一行指针 (见上 D2 裁定), 交主控.
- O-2 **MB/assumptions.md:28** (3.b) 无需改: PDF p252 MB 假设 3 自带 a/b, p256 MS 假设 3 也自带 a/b, 两处均为 PDF 原文, 非 MS 复制.
- O-3 **MS/assumptions.md:19** "iii. As in 1.a.ii …" 位置错: PDF p256 该条是 1.b 下的 "i.", 不是 1.a.iii.
- O-4 **MS/assumptions.md:25** "BEENDTC respectively" 缺逗号 (PDF p256 "BEENDTC," ); 且 PDF 在 "respectively." 后换行另起 "--REFID …" (仅格式).
- O-5 **MS/assumptions.md:29** "should only be populated" — PDF p256 漏 "be" (PDF_TYPO, KB 正确, 登记即可).
- 已查 OK: MS Description/Overview (MS/assumptions.md:5) 与 p252 逐字一致; spec 首句 (:9) 逐字一致, 位置符合 CM/IS 先例; 脚注 (:11) 与 p255 一致.

## 触碰的 unparseable 表
无.

## attempt 1 续 (主控裁定: kb_files 扩入 MB/examples.md, MS/assumptions.md)
- md5: MB/examples.md 8dd0a328… → a5b39219072ecfd28d0d16e378be056d (305 → 253 行); MS/assumptions.md 4b19662d… → f7707d7ccfc961ed40e72ea973208a60; MS/examples.md 不变 bb0cfc85…
- 原件: scratch `mb_examples.base.md`, `ms_assumptions.base.md`. 改动脚本对 base 行首做 assert 后替换.
- 锚点预检 (不截断): `grep -rn -E "MB/examples\.md#" --exclude-dir=releases --exclude-dir=archive --exclude-dir=node_modules --exclude-dir=.git .` → 只有 MS/examples.md:7/:36/:60 (指向 `#example-1/2/3`, 标题保留) + B-MB review 证据文字; 无链接指向被删内容. MS 侧 heading `## Example 1` / `## Example 2` → 锚点 `#example-1` / `#example-2`.

### 变更清单 (续)
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 18 | MB:20 | D2 跨文件去重 | REPLACED | base :20-53 (Ex1 MS 叙述 7 段 + Rows 1-4/5-6/7-10 + ms.xpt 10 行) → 一行 `> See [MS Example 1](../MS/examples.md#example-1) …` | 256-257 |
| 19 | MB:91 | D2 跨文件去重 | REPLACED | base :124-145 (Ex2 Rows 1-2/3-4/5-8/9-10 + ms.xpt 10 行) → 一行 `> See [MS Example 2](../MS/examples.md#example-2) …` | 259 |
| 20 | MS/assumptions.md:20 | O-3 | MOVED + REPLACED | "iii. As in 1.a.ii …" (原在 1.a 下, b 之前) → 移到 1.b 之后, 编号 "i." (PDF p256 为 1.b.i); 正文未改 | 256 |
| 21 | MS/assumptions.md:25 | O-4 | REPLACED | "BEENDTC respectively" → "BEENDTC, respectively" (PDF p256 有逗号) | 256 |
| 22 | MS/assumptions.md:29 | T-5 | SKIPPED_PDF_TYPO | KB 保留 "should only be populated"; PDF p256 漏 "be" | 256 |

### 删除清单 (续)
| # | 位置 (base) | 内容 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-5 | MB/examples.md:20-53 | Ex1 MS 叙述 (After E. faecalis … MSCONCU 7 段) + Rows 1-4/5-6/7-10 + `**ms.xpt**` 表 10 行 | D2 跨文件重复, 归属 MS (O-a 先例) | MS/examples.md:11-32 (叙述逐字, 表按 PDF; 仅 r9 MSSTRESC 见 T-1) |
| D-6 | MB/examples.md:124-145 | Ex2 Rows 1-2/3-4/5-8/9-10 + `**ms.xpt**` 表 10 行 | 同上 | MS/examples.md:38-56 (Rows 逐字, 表逐格与原 MB 副本一致) |
- 保留未动: MB Ex1 引言 :7-11 + mb.xpt, "Although not expected …" + relrec (MB:22-29); MB Ex2 引言/be/suppbe/mb/suppmb; MB Ex3 全部.
- 对比确认: 被删 MB 副本与 MS 保留副本逐格/逐句比对, 唯一差异 = Ex1 r9 MSSTRESC (MB 空 = PDF; MS 25 = T-1). 叙述方面 MB 把 PDF 一段拆为多段, MS 合为 PDF 原段, 文字相同.
- T-1 更新: MB 副本已删, MB/MS 不一致消解; MS 仍登记 T-1 (KB 25 vs PDF 空).

### PDF_TYPO (续)
| T-5 | MS/assumptions.md:29 | "It should only populated" | "should only be populated" (保留) | 缺动词, 语法上可自证 |

### 验证 (S=scratch, repo 根)
```
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest2.json --out $S/census_after2.json
  # manifest2 = B-MB + B-MS pdf_ranges; KB tables 20: OK 17 / DIFF 3, diffs 4; p248-263 pdf_only 无
  # 残留 = MB:198 suppmb Row 5/6 vs 7/8 (B-MB T-1) ×2, MB:241 Ex4 表头 (B-MB T-2/T-3 MBTRESN→MBSTRESN), MS:21 r9 MSSTRESC (本批 T-1)
python3 tools/check_links.py | tail -1   # live docs: 42 (基线 42)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # 全仓 regress 41 (含并行 B-FA 的 p0364 等); p248-263 范围 15 条, 全部为预期不命中:
```
| atom | 原因 |
|---|---|
| ig34_p0257_a010, p0258_a019-a024, p0260_a009, p0260_a015, p0263_a021, p0263_a022 (11) | B-MB 已登记: verbatim 抄自旧错 KB 值, T3 须按 PDF 改 verbatim |
| ig34_p0263_a020 | Ex4 mb 表头 verbatim 含 MBTRESN; B-MB 裁定 2 已改为 MBSTRESN (非本批) |
| ig34_p0257_a016 | Ex1 ms r9 (MSSTRESC 空) 原由 MB 副本命中; MB 副本删后 MS 为 25 (T-1) |
| ig34_p0254_a040 / a042 | spec CODE_LITERAL "VISITNUM"/"VISIT", 原由 MS Ex2 表多余列命中; 该 3 列 PDF p259 无, 已删. MS/spec.md:419/:428 有 `### VISITNUM`/`### VISIT` 节 (fp 未按标题形式计) |
- 本批 MB+MS 真回归 0.

## attempt 1 续 2 (reviewer PASS 后收尾 L-1 / L-2)
- MS/examples.md md5 bb0cfc85… → ec680de8cad08260b3560890f73cdfff; MB/examples.md、MS/assumptions.md 不变.

| # | kb_file:line | ref | action | before → after | PDF 页 |
|---|---|---|---|---|---|
| 23 | MS/examples.md:7 | L-1 | REPLACED | Ex1 指针补 "the example description and"，与 :36/:60 措辞统一 | 256 |
| 24 | MS/examples.md:80-81 | L-2 / T-3 | REPLACED | suppms IDVAR MBREFID → MSREFID (r1, r2) | 262 |

- T-3 改登记为 keep-correct: PDF p262 suppms RDOMAIN=MS、IDVARVAL 100.4/100.5 恰为同例 ms.xpt r1/r2 的 MSREFID；IDVAR 须为 RDOMAIN 内变量，MS 无 MBREFID → 正确值由 PDF 自身确定.
- T-4 (QNAM `MSMEDTYPE` 9 字符) 维持照录，T4 用户裁定.
- 验证 (S=scratch):
```
table_census.py --manifest $S/manifest2.json --out $S/census_after3.json  # 20 表: OK 16 / DIFF 4, diffs 6 — 全为登记 typo: MB:198 (B-MB T-1 ×2), MB:241 (B-MB 表头), MS:21 r9 (T-1), MS:78 IDVAR ×2 (T-3)
python3 tools/check_links.py | tail -1   # live docs: 42
fp_match.py --out $S/fp_after3.jsonl --regress-out $S/fp_regress3.jsonl  # 相对上一轮新增 3: ig34_p0262_a029/a030 (suppms 行 verbatim 含 MBREFID = T-3 预期) + ig34_p0396_a009 (p396 非 MB/MS, 并行批); MB+MS 真回归 0
```
