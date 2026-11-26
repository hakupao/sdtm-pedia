# T2 B-MS reviewer — attempt 1

**verdict: PASS** (无阻断; 3 条低优先登记项, 见问题表)

- reviewer: oh-my-claudecode:code-reviewer (opus), 与 writer 不同 agent. 只读 KB; scratch = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-MS_reviewer/`
- 被审文件 md5 (= writer 续报告): MS/examples.md bb0cfc85…, MB/examples.md a5b39219…, MS/assumptions.md f7707d7c…; MS/spec.md、MB/assumptions.md 未改 (`git diff --quiet HEAD`).
- 整个 KB diff 另含 ch02/ch08/FA/OE/TA/model02 = 并行批 (writer.jsonl kb_file 只有本批 3 文件: MS/examples 12, MS/assumptions 3, MB/examples 2).

## 命令 (repo 根, S=上面 scratch)
```
# manifest = B-MS pdf_ranges + MB/examples.md ig34 248-263
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  # exit 1; KB tables 20: OK 17 / DIFF 3, diffs 4; 本批页 pdf_only 0, pdf_unparsed 0
  # DIFF = MS:21 r9 MSSTRESC (T-1) | MB:198 suppmb Row 5/6 vs 7/8 (B-MB T-1) | MB:241 表头 (B-MB T-2/T-3); MS:45 Ex2 / :69 / :78 OK
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # RESULT: RED (全仓, 含并行批); p248-263 regress 15 条 = writer 清单逐条一致, 均为预期 (见下)
python3 tools/check_links.py > $S/links.txt; grep "live docs" $S/links.txt   # broken relative links: 18668 (live docs: 42) — 基线 42
pdftoppm -f N -l N -r 150 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/pN   # N=257,259,262 (页码与 pdf_pages 对齐, 已核)
```

## (1) 归属裁定 — 同意
PDF §6.3.5.7.3 版面: Ex1 = MB 引言 → mb.xpt → MS 叙述 (After E. faecalis… / third method) → Rows 1-4/5-6/7-10 → ms.xpt → "Although not expected…" → relrec;
Ex2 = 引言 → be/suppbe/mb/suppmb → Rows 1-2…9-10 → ms.xpt; Ex3 = … suppmb → MS 叙述 + Rows + ms/suppms → DI 句 + di → relrec.
MS 段在 PDF 中各自连续, 切分 (MS 段 → MS; 引言 + BE/BS/RELSPEC/MB/DI/RELREC → MB) 与版面一致, 与 B-MB O-a 先例一致.
MB 指针位置: MB:20 在 mb.xpt 与 "Although not expected" 之间, MB:91 在 suppmb 后, MB:207 (已有) 在 DI 句前 — 与 PDF 中 MS 段位置一致.
锚点: MS `## Example 1/2/3`, MB `### Example 1/2/3` → `#example-N` 均可解析; KB 内无其他文件链到 M[BS]/examples.md# (grep 0 条).

## (2) 人工逐格 (渲染 p257/p259 150dpi, 独立于 bbox census)
| 表 | KB 行 | 结果 |
|---|---|---|
| Ex1 ms.xpt 表头 22 列 | MS:21 | 一致 (列序 … NHOID, MSGRPID, MSSEQ, MSREFID, MSLNKGRP … MSNAM, MSMETHOD, MSDTC) |
| Ex1 r1 | MS:23 | 一致 (MSLNKGRP 1; MSCONC/MSCONCU 空; 0.25 ug/dL 0.25 0.25 ug/dL; 06-19) |
| Ex1 r2 | MS:24 | 一致 |
| Ex1 r3 | MS:25 | 一致 (CONC/CONCU 空; 1 ug/dL 1 1 ug/dL) |
| Ex1 r4 | MS:26 | 一致 |
| Ex1 r5-6 | MS:27-28 | 一致 (MSGRPID 空; 0.5 ug/dL; MACRO BROTH DILUTION; 06-19) |
| Ex1 r7-8 | MS:29-30 | 一致 (MSDTC 2005-06-26T08:00) |
| Ex1 r9 | MS:31 | 差异仅 MSSTRESC: PDF 空 / KB 25 (T-1, 同意) ; 其余一致 |
| Ex1 r10 | MS:32 | 一致 |
| Ex2 ms.xpt 表头 18 列 | MS:45 | 一致 (MSSEQ, MSREFID, MSGRPID 序; 无 MSNAM/VISITNUM/VISIT) |
| Ex2 r1-2 | MS:47-48 | 一致 (GRPID 1; 0.004 mg/L; 06-19) |
| Ex2 r3-4 | MS:49-50 | 一致 (GRPID 2; r3 0.023 ×3) |
| Ex2 r5-6 | MS:51-52 | 一致 (GRPID 3; r5 0.125 ×3; 06-26) |
| Ex2 r7-8 | MS:53-54 | 一致 (GRPID 4; r7 0.023; r8 INTERMEDIATE ×2) |
| Ex2 r9-10 | MS:55-56 | 一致 (GRPID 5; r9 0.026; r10 INTERMEDIATE ×2; 2005-07-06T08:00) |
| Ex3 ms/suppms | MS:69-81 | 未改; 对 p262 layout 文本逐格一致 (census OK); suppms IDVAR/QNAM 照录 (T-3/T-4) |

## (3)(4) 叙述 + 删除
- MS:11 / :13 (N-1/N-2) 对 p256-257 逐句一致; MS:38-41 三处 R2 恢复 ("was found" / "from the same subject" / "was still … this drug") 与 p259 一致; `" KLEBSIELLA` 前导空格 = PDF 原样.
- MS:62 删 "from the gastric TB study (see MB Example 3)", "the culture medium", 补 PF 句 — 与 p262 逐字一致.
- MS:9 D6 `> KB note (not in SDTMIG):` 前缀正确, 内容不与 PDF 矛盾 (确认).
- D-1/D-2/D-3: 均为 KB 扩写/自写导航, PDF 无对应 — 删除正确. D-4: p259 表确无 MSNAM/VISITNUM/VISIT 三列 — 正确.
- D-5/D-6: 脚本把 MB diff 删除的 33 行逐条对 MS 保留副本 (叙述归一化子串, 表行逐格): 叙述全部命中; 表行仅 Ex1 r9 MSSTRESC 差 (MB 空 / MS 25 = T-1). **无 PDF 内容丢失.**
- 双向全扫 (含表行): KB→PDF (MS/examples + MS/assumptions 每句对 p252-263 归一化文本) 未命中仅 = 导航/KB note 行 (:3, :7, :9, :36, :60)、:11 跨页断句 (渲染核对一致)、T-2 (:65)、T-5 (assumptions:29);
  PDF→KB (MS Description、spec 首句、Assumptions p255-256、Ex1/Ex2/Ex3 MS 段) 未命中仅 = T-2 / T-5 原句 + 表头碎片 "Variable". 表格行见 (2) + census.

## (5) MS/assumptions.md
- 1.b.i: PDF p256 首行 "i. As in 1.a.ii…" 紧接 p255 1.b 之后 → KB 移到 b 后编号 i. 正确.
- :25 "BEENDTC, respectively" = p256 (MB/assumptions 的同句 PDF p252 无逗号, KB 未动, 正确).
- T-5 "should only be populated" 保留正确词, PDF 漏 "be" — 同意登记.
- O-2: MB/assumptions 3.b 是 PDF p252 原文, 非复制 — 确认无需改.

## (6) PDF_TYPO
| T | 判定 | 依据 |
|---|---|---|
| T-1 MS:31 MSSTRESC 25 | 同意 keep-correct | 同行 MSORRES 25 / MSSTRESN 25, 同表 r7 23/23/23 同式 → PDF 自身可定 |
| T-2 MS:65 MSCONCU | 同意 | 同句/Rows 1-2 均 MSCONCU |
| T-3 suppms IDVAR MBREFID | 同意照录 + T4 (见问题表 L-2) | |
| T-4 suppms QNAM MSMEDTYPE | 同意照录 + T4 | 9 字符, 正确值 (MSMEDTYP?) 非 PDF 自证 |
| T-5 assumptions:29 | 同意 | 语法缺动词 |

## (7) fp 预期未命中 (p248-263, 15 条)
- ig34_p0254_a040 "VISITNUM" / a042 "VISIT": CODE_LITERAL 来自 p254 **MS spec 表** (邻接 a039/a041 为 VISITNUM/VISIT TABLE_ROW); targets 只列 MS/assumptions + MS/examples (映射偏差), 原命中仅来自 Ex2 错误多余列.
  MS/spec.md:419 `### VISITNUM` (Order 47, Exp) / :428 `### VISIT` (Order 48, Perm) 存在且本批未动 → 内容未丢; T3 应把 target 改为 MS/spec.md.
- ig34_p0257_a016: verbatim = PDF (r9 MSSTRESC 空), MB 副本删后 MS 为 25 (T-1) → 预期; T3 按 T-1 处置.
- p0257_a010, p0258_a019-a024, p0260_a009/a015, p0263_a020-a022: B-MB 已登记 (verbatim 抄自旧错 KB 值 / Ex4 表头). 本批真回归 0.

## 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| L-1 MS:7 | 导航措辞 (LOW) | Ex1 指针只写 "mb.xpt and relrec.xpt tables", 未像 :36/:60 写 "example description" (MB Ex1 有引言 MB:7-11 与 "Although not expected" 句). 非 PDF 内容问题, 可选统一 | p256 "In this example, both a central and a local lab…" |
| L-2 T-3 | PDF_TYPO 判定 (LOW, open) | IDVAR=MBREFID 可能算 PDF 自证 (RDOMAIN=MS, IDVARVAL 100.4/100.5 = 同例 ms.xpt MSREFID, mb.xpt 无 100.4/100.5); writer 保守走 T4 亦可, 交用户裁定时附此依据 | p262 suppms "MS ABC-01-101 MBREFID 100.4" |
| L-3 fp a040/a042 | 原子映射 (LOW) | target 未含 MS/spec.md, T3 重算前须改 target, 否则持续报回归 | p254 spec 表 VISITNUM/VISIT 行 |

## G-TB6 结构行签字
MS:7, MS:36, MS:60 (D2 交叉引用); MB:20, MB:91 (D2 交叉引用); MS:9 (D6 KB note); MS:45-46 (Ex2 表头 + 分隔线, 18 列对 p259). 均签字通过. 新增/改动叙述行无无出处词句.

## 续 签字 (writer attempt 1 续 2: L-1 / L-2 delta) — **PASS**
- delta 隔离: 把 MS:7 与 MS:80-81 反向替换回去, md5 = bb0cfc85… (上轮审过的版本) → 只改了这 3 行; MB/examples.md a5b39219…、MS/assumptions.md f7707d7c… 不变.
- MS:7 Ex1 指针补 "the example description and"，与 :36/:60 统一; 纯导航, MB Ex1 引言 (MB:7-11, p256) 存在 — 签字.
- MS:80-81 IDVAR MBREFID→MSREFID: p262 suppms RDOMAIN=MS, IDVARVAL 100.4/100.5 = 同例 ms.xpt r1/r2 MSREFID; p262 mb.xpt 中 MBREFID 只有 100.1-100.3 → 由 PDF 自身可定, T-3 改为 keep-correct, 同意. T-4 维持照录 + T4.
- census (`$S/census_after3.json`, manifest 同上): OK 16 / DIFF 4, diffs 6 = MS:21 r9 (T-1) + MS:78 IDVAR ×2 (T-3) + MB:198 ×2 / MB:241 (B-MB 已登记); 无未登记差异.
- fp (`$S/fp_regress3.jsonl`): p248-263 = 上轮 15 条 + ig34_p0262_a029/a030 (verbatim 含 "MBREFID" = T-3 预期; T3 按 T-3 改 verbatim); MB+MS 真回归 0.
- `python3 tools/check_links.py | grep "live docs"` → live docs: 42 (≤42).
