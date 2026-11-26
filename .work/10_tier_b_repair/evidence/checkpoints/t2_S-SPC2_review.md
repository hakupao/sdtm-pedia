# T2S S-SPC2 reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** (无 CRITICAL/HIGH/MEDIUM; 3 条 LOW 观察, 不阻断)

- 对象: `git diff HEAD -- knowledge_base/domains/{MB,MS,PC,PP}` (含 attempt 1 delta 主控裁定 1-4). scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPC2_reviewer/`
  脚本: 复用 S-EVT reviewer 的 `bscan.py` / `speccmp.py` (非 writer 脚本), `bscan2.py` = bscan 去掉 `|` 表格行 (表格由 census + 渲染核); `flt.py` 过滤 p2k 残留中的表格/spec 列粘连行. 渲染: p249/253/268/271 (80dpi, CT 列), p257/262/263/274/277/278 (130dpi, census_items), p278/p280 Method D 句 150dpi 裁切.
- 授权范围: `git diff HEAD --stat -- knowledge_base/` 中本批改动 = MB/{assumptions,spec}, MS/{assumptions,examples,spec}, PC/{assumptions,examples,spec}, PP/{assumptions,examples,spec}; 全部 ∈ kb_files, narrow_files 空; MB/examples.md 未动 (numstat 0). 其余 29 文件为别批, 不计.

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPC2_reviewer
PDF="source/cdisc/SDTMIG v3.4 (no header footer).pdf"; for p in 249 250 251 252 253 254 255 267 268 269 271 272; do pdftotext -bbox -f $p -l $p "$PDF" $S/bb_$p.html; done
for d in MB:249,250,251 MS:252,253,254,255 PC:267,268,269 PP:271,272; do python3 -I $S/speccmp.py $S ${d%%:*} ${d#*:} | grep -v " OK$"; done
  # MB 47/47 MS 61/61 顺序一致; PC 35+6 (p267 6 变量 bbox 表头下沿漏读, layout 文本逐字段核一致) = 41; PP 24+2 (STUDYID/PPSTRESC 同, layout 核) = 26. 非 CT 字段全一致; CT 差异仅 DOMAIN (U6) + C-code (U5)
K=knowledge_base/domains; python3 -I $S/bscan2.py k2p 248 263 $K/MB/assumptions.md   # 同式 8 文件 (MS 252-263, PC 267-284, PP 271-284), 见下 KB→PDF 表
python3 -I $S/bscan2.py p2k 248 263 $K/MB/*.md $K/MS/*.md (6 文件) ; python3 -I $S/bscan2.py p2k 267 284 (PC/PP 6 文件); python3 -I $S/flt.py $S/p2k_MBMS.txt
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1; KB 表 44: OK 35 / DIFF 7 / NO_PDF 1 / UNPARSEABLE 1; cells 6395; diffs 44
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # exit 1 RED; 67 regress, 对 t2_fp_expected_regressions.jsonl 差集 6 = p199/p200/p206/p240 (别批页), 本批页 0
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### 页范围复核 (O20)
- 同意 writer 更正: MB 248-252 (p248 上部 LB Ex4/Ex5 属 §6.3.5.6); MS 252-256; MB+MS 共用例 256-263 (p263 下部起 §6.3.5.8 MI, p264-267 上部 MI); PC 267-271 (§6.3.5.9 标题下直接 §6.3.5.9.1, 无引言正文); PP 271-275; §6.3.5.9.3 275-284 (p285 首行 §6.3.6 MO).

### 双向全扫 (reviewer 计数)
| 范围 | KB→PDF (bscan2 k2p, 非表格单元) | PDF→KB (p2k, 过滤表格/spec 粘连后残留) | 结论 |
|---|---|---|---|
| MB/assumptions (248-263) | 36 单元 miss 0 | §6.3.5.7 引言 4 句全命中 (MB/asm:5) | 一致 |
| MB/examples | 146 miss 5 = H1 / `## §6.3.5.7.3 … and …` (裁定 2 不改) / 3 条 `> See [MS Example n]` 导航 | Ex1-Ex4 叙述全命中 | 一致 |
| MS/assumptions (252-263) | 32 miss 1 = MS T-5 (PDF "should only populated") | 全命中 (asm 5 与 §6.3.5.7.3 标题粘连, 原句在 :29) | 一致 |
| MS/examples | 57 miss 10 = H1 / :3 D6 (2 句) / :9 既有 D6 / 3 条 See 导航 / MS T-2 (MSCONU) | MS T-2 照前 | 一致 |
| p248-263 p2k 其余残留 | — | LB Ex4/Ex5 (p248, 别节)、MI (p263, 别节)、spec 列粘连 (speccmp 覆盖)、标题粘连 4 处 (原句均 grep 命中) | 一致 |
| PC/assumptions (267-284) | 75 miss 3 = :5 D6 (2 单元) / `## §6.3.5.9.3` 标题 | Relating Datasets/Records、Method 列表、Conclusions、Suggestions 全命中 | 一致 |
| PC/examples | 142 miss 7 = :3 D6 (3 句) / `## §6.3.5.9.3 … — Worked Examples` 标题 / :213 = T-10 / :250 = T-11 | Ex1-Ex4 + Method A-D 结构与 PDF 一致 (Ex4 仅 A/D, PDF 同) | 一致 |
| PP/assumptions (271-284) | 18 miss 0 | Description/Specification/Assumptions 标题 + 2 句全命中 | 一致 |
| PP/examples | 79 miss 37 = :3 D6 / T-9 (pre-corrdinating) / `**supppp.xpt**` 表前标签 / :106 D6 / :108 See 导航 / :110 斜体导航 / :112-170 共 30 单元全在 :114 D6 范围内 | p273 Ex1 首句命中; "space limitations" 在 p271-284 0 次 | 一致 |
| p267-284 p2k 其余残留 | — | p267 上部 MI Ex3 (别节)、spec 粘连、T-9、标题/表名粘连 4 处 (grep 原句命中) | 一致 |

### spec.md Controlled Terms 逐变量 (bbox speccmp + layout + 渲染)
- MB 47 / MS 61 / PC 41 / PP 26 变量: Label/Type/Role/Core/CDISC Notes 全一致.
- PDF `*` 8 格 = KB `*` 8 格: MBCAT/MBSCAT (p249)、MSCAT/MSSCAT (p253)、PCCAT/PCSCAT (p268)、PPCAT/PPSCAT (p271); 渲染图逐格确认; layout `grep -c "Char \*"` p249/253/268/271 各 2, 其余 8 页 0.
- 其余 CT 差异: DOMAIN (MB/MS/PC/PP, U6) + C-code 记法 MB 17 / MS 22 / PC 9 / PP 8 格 (U5), 归 S-CT, 不计.
- 脚注 4 处 (MB:429 / MS:555 / PC:375 / PP:240): 逐字 = p251:16 / p255:27 / p269:36 / p272:37; 位置 = 最后变量块 `---` 之后、`## Cross References` 之前 (U7); 格式同 AE/spec.md:546 先例.
- 域首句 (gap S/D): MB/asm:13、PC/asm:9 (定义句)、PP/asm:5/:9 逐字 = p249/p267/p271 (渲染 p271 确认).

### census_items 人工逐格 (渲染, 不采信 writer)
| 表 | 渲染 | 结果 |
|---|---|---|
| MB/examples.md:198 suppmb Ex3 | p262 130dpi | 6 行 × 10 列一致; 仅 Row 列 PDF 7/8 vs KB 5/6 = MB T-1 |
| MB/examples.md:241 mb Ex4 | p263 | 2 行 × 23 列一致; 表头 PDF MBGPRID/MBTRESN vs KB MBGRPID/MBSTRESN = MB T-2/T-3 |
| MS/examples.md:21 ms Ex1 | p257 | 10 行 × 22 列一致; 仅 r9 MSSTRESC PDF 空 / KB 25 = MS T-1 |
| MS/examples.md:78 suppms Ex3 | p262 | 2 行 × 10 列一致; IDVAR PDF MBREFID / KB MSREFID = MS T-3; QNAM MSMEDTYPE 照录 (T-4) |
| PC/examples.md:75 relrec Ex1 Method A | p277 | 4 行 × 8 列一致; r3 IDVAR PDF PPGRPID / KB PCGRPID = PCPP T-1 |
| PC/examples.md:89 relrec Ex1 Method B | p278 | 26 行 × 8 列一致; r13/r26 RDOMAIN PDF PC / KB PP = T-2/T-3; RELID 全 1、r26 DY1DRGX 照 PDF (T-4) |
| PP/examples.md:52 pp Ex2 (NO_PDF) | p274 | 7 行 × 20 列一致; r6/r7 PPSEQ PDF 1/2 / KB 6/7 = PCPP T-5 |
| PP/examples.md:66 supppp Ex2 | p274 | 7 行 × 11 列一致 (r7 QORIG/QEVAL 空); 表头 PDF DOMAIN / KB RDOMAIN = T-6; 其余 34 diffs = 居中表解析器错位 |
| PP/examples.md:120 Method 映射表 (UNPARSEABLE) | p275 方法列表 (PC/asm:46-49) | 4 行 A/B/C/D × 基数/PC/PP IDVAR 与 PDF 列表一致; 在 :114 D6 范围内 |
- census DIFF 7 张 = 上表登记项, 无未登记差异; PDF_ONLY 无本批页本节表.

### 改动 / 结构 / 删除 / D6 逐条签字
| # | 项 | 签字 | 证据 |
|---|---|---|---|
| 1 | MB/asm:5 §6.3.5.7 引言补 3 句 | OK | p248:33-35 逐字 (— 为 U+2014, PDF 同) |
| 2 | MB/asm:11-13 `## MB – Specification` + 首句 | OK | p249 渲染 |
| 3-4,6-7,12-13,19-20 | CT `*` 8 格 | OK | 渲染 p249/253/268/271 |
| 5,14,21 | 脚注 MB/PC/PP | OK | 见上 |
| 8-9 | MS 脚注 MOVED (asm:11-12 删, spec:555 插; `1In`→`¹In`) | OK | p255:27; asm 现无残留 |
| 10 | PC/asm:5 KB 自写概述 → D6 | OK, 不矛盾 | p267: §6.3.5.9 下仅 PC/PP 两子节 |
| 11 | PC/asm:7-9 Description | OK | p267:29-30 |
| 15 | PC/ex:146 Ex1 Method D Rows 1-19 改正 | OK | p278 渲染: "…"1" through "12" and PP records with PPSEQ values "1" through "7"." KB 现逐字 |
| 16 | PC/ex:250 Ex2 Method D `"1" through "7"` (T-11) | OK (主控裁定 4) | p280 渲染 `"1 through "7"`; p278/p280 Method C 同型自证 |
| 17 | PC/ex:213 T-10 保留 | OK | p279:53 `through 12",` 缺开引号 |
| 18 | PP/asm 3 标题 + 2 句 | OK | p271 渲染 / p272:40 |
| 22 / S-1 / D-1 | PP/ex 删 "Due to space limitations…" | OK | p273:4-5 `PP – Examples` 后直接 Example 1; p271-284 仅 p269:47 (PC – Examples) 有此句; PC/examples.md:7 保留原句 |
| 23 | PP/ex:106 → D6 | OK, 不矛盾 (L-1) | p277 pp 12 行 / TMAX..CLO / PPNOMDY 1、8 / 4 列 PPGRPID |
| 24 | PP/ex:114 D6 范围标注 (至文件末) | OK | :116-170 内容逐条核不矛盾 (Method 映射 = PDF 列表; Rows 句为 p277-278 改写, D6 明示 "paraphrased") |
| 25-27 / S-4 | MS/PC/PP examples:3 `*Note:*` → D6 | OK (新口径: 解释性 Note 一律 D6) | 文字未变; 内容不矛盾 |
| delta 1 | PP/ex:112 伪节号去除 → `## RELREC Method Quick Reference (PP-side view)` | OK | 节号由 KB 自写 (PDF §6.3.5.9.3 标题为 "Relating PP Records to PC Records"); `grep -rn "quick-reference"` knowledge_base 无入链 |
| S-2 | 5 个新增 `## XX – …` 标题 | OK | PDF 原有小标题 |
- 纯导航不标 (确认): MB/ex 3 条 + MS/ex 3 条 `> See …`、PP/ex:108/:110、`**supppp.xpt**`、四域 `> Class|Structure` 与 Cross References (U8).
- fp 预期回归核: ig34_p0255_a021 = MOVED (原子 `norm` 在 MS/spec.md 命中, 理由成立); ig34_p0278_a051 = 原子 verbatim 抄自旧错 KB ("…"12" and "10" through "12" and individual PP…"), p278 渲染无此文字, 理由成立 (本次 regress 列表中未出现, 已在 expected 第 62 行). 14 个 gap/footnote 原子 `norm` 直查目标文件全部命中.

### LOW 观察 (不阻断)
| # | 位置 | 观察 | 建议 |
|---|---|---|---|
| L-1 | PP/examples.md:106 (D6) | "4 PPGRPID columns … for the 4 RELREC method examples" — PDF 4 列对应 Example 1-4 (每例含 Method A-D), 非 4 个 Method; "STUDYDRUG analyte" 为 PC 表 PCTEST 值, PP 表无. 措辞不精确, 未构成与 PDF 矛盾 | 可选: 改 "for Examples 1-4"; 或留待 S-TYPO/后续 |
| L-2 | PP/examples.md:114 | D6 标注在标题下方而非上方; dispatch notes 允许 "上方单独一行", 此处位置在节内首行, 语义等价 | 无需改 |
| L-3 | 原子台账 | writer 列出的原子抽取错 (p249 a010/a019 等) 本审 speccmp/渲染亦见 MBREFID/MBORRES 字段与原子不符而 KB = PDF, 支持其 T3 登记 | T3 处理 |

### Open Questions
- 无.

## attempt 1 delta 2 复审 (reviewer L-1 修正; oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** (L-1 关闭; L-2 按主控不改)

- 对象: PP/examples.md:106 D6 句 (md5 `383ff50c1524fb58a3560c76e496b04f`). `git diff HEAD -- knowledge_base/domains/PP/examples.md` 的改动块与 attempt 1 审时相同 (:3 D6 / 删 space limitations / :106 D6 / :112 去节号 / :114 D6), 只有 :106 句的文字变了.
- 新句各说法对 p277 渲染图 (`$S/f277-277.png`, 130dpi) 逐项核:
| 说法 | PDF p277 | 结果 |
|---|---|---|
| 12 rows | Row 1-12 | 成立 |
| PPTESTCD TMAX, CMAX, AUCALL, LAMZHL, VZO, CLO | r1-6 / r7-12 各为此 6 个 | 成立 |
| PPCAT = "DRUG X" | 12 行 PPCAT 均为 DRUG X | 成立 |
| Day 1 and Day 8 (PPNOMDY 1 and 8) | PPNOMDY r1-6 = 1, r7-12 = 8; PPRFTDTC 2001-02-01 / 02-08 | 成立 |
| 4 PPGRPID columns, 1 for each of Examples 1-4 of Section 6.3.5.9.3 | 表头 PPGRPID (Example 1)…(Example 4); p276:5 "4 --GRPID columns, 1 for each of the example situations" | 成立 |
| (shown in PC/examples.md) | PC/examples.md 有 Example 1-4 (:62/:192/:274/:390) | 成立 |
- 已删的 "STUDYDRUG analyte" 与 "4 RELREC method examples" 两个不准确说法; 新句与 PDF 无矛盾, D6 前缀保留.
- 其余 11 个本批文件 md5 = writer attempt 1 记录值 (a598140f / a5b39219 / b3f7f47b / 13db4f98 / fd8a948c / 79fa4aa2 / f00ae3ee / ecbea2a1 / 74e05018 / 44564a3d / 78c05498), 也就是 attempt 1 审过的内容; `git diff HEAD --stat` 中这 11 个文件的增删行数与 attempt 1 相同.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42.
