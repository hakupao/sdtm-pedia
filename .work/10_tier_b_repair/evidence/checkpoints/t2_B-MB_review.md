# T2 B-MB reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS** (无阻断缺陷; 3 条低优先登记项 + O-a 裁定的一行导航指针交主控执行)

- base 97e1895, MB/examples.md md5 before 4b1b1142… (400) / after 64747953… (305), 与 writer 报告一致. KB diff 本批只涉及 MB/examples.md (其余 CP/LB/TR 为并行批, 未审).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-MB_reviewer/` (base.md / after.md / dedup.py / census / fp / 渲染 png)

### 命令 + 结果 (S=上面 scratch, 工作目录 repo 根)
```
git show 97e1895:knowledge_base/domains/MB/examples.md > $S/base.md
python3 -I $S/dedup.py $S/base.md knowledge_base/domains/MB/examples.md   # 副本1 (base:1-170) 每行归一化后在 after 中查找; 列出 MISSING 行 → 逐条对 PDF
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1; KB 表 18: OK 16 / DIFF 2, diffs 3 (suppmb Row 5/6 vs PDF 7/8 = T-1; Ex4 表头 MBGRPID vs MBGPRID = T-2)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # exit 1; regressions=11 (见下)
python3 tools/check_links.py | tail -1   # live docs: 42 (基线 42)
grep -rn -E "MB/examples(\.md)?#" --exclude-dir=.git --exclude-dir=.work --exclude-dir=node_modules .   # 0 命中 → 无锚点链接
pdftoppm -f N -l N -r 110|150|220 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf"  (N=257,258,260,262,263; p262 mb 表另裁 220dpi 左右两半)
```
独立方法: 表格以渲染图 + `pdftotext -layout` (work/pdf_pages) 核, 不用 census bbox 解析器.

### (1) D2 去重: 副本 1 (base:3-170) 删除行逐条处置
dedup.py 对副本 1 列出 33 条不在 after 中的行, 逐条对 PDF:

| base 行 | 内容 | 处置 | PDF 依据 |
|---|---|---|---|
| 3/25/80 | `## Example 1/2/3` | 结构行删; after 保留 `### Example n` | — |
| 5 | Ex1 叙述 1 段 | after:7-11 拆 3 段, 文字全同 | p256 |
| 7 | Ex1 MS 叙述 (乱序, 缺 "such as susceptible…" 位置) | after:20-32 按 PDF 顺序, 信息全含 | p256-257 "(MSTESTCD = "MICROSUS") such as susceptible, intermediate, or resistant" |
| 11,13,14 | Ex1 mb (MBTSTDTL 列, PRESENT, 06-19) | 副本 1 错; after:15-18 与 PDF 一致 | p256 "ENTEROCOCCUS FAECALIS … 2005-07-21T08:00" |
| 35-37 | Ex2 be USUBJID ABC-01-001, r3 07-01 | 副本 1 错; after:74-76 = PDF | p257 "ABC-001-001 … 2005-07-06T08:00" |
| 39 | "SUPPBE table" | 副本 1 改写; after:78 "SUPPBE dataset" = PDF | p258 |
| 63-72 | Ex2 mb (多 MBSPEC 空列) | 副本 1 错列; after:107-116 = PDF (VISIT 1 已修) | p258 |
| 78 | Ex2 suppmb IDVAR MBSEQ/2 | 副本 1 错; after:122 MBTSTDTL / CELL COUNT = PDF | p258 |
| 84 | Ex3 叙述 2 ("many domains", "in Sections") | 副本 1 改写; after:151 "many tests", "in the Sections" = PDF | p259 |
| 86 | "…culture results in MB and MS. MBGRPID … rows 5-7." | 副本 1 改写+误挂句; after:153 "(MB and MS)" = PDF; MBGRPID 句在 after:233 Row 4 = PDF p261 | p259/p261 |
| 100,107 | Ex3 be r1 BESTDTC 05:00, r8 BESTDTC 02-21T10:00 | 副本 1 错; after:167/174 = PDF (06:00 / 02-02T10:00) | p260 渲染 |
| 142 | Row 1 "MBSPCND" | MOVED→after:227 改 MBSPCCND = PDF | p261 |
| 151-158 | Ex3 mb (副本 1 独有) | MOVED→after:241-248, 整表重建; 人工逐格见下 | p262 |
| 164,168,169 | Ex3 suppmb | MOVED→after:254-259 (Quantification; 行序按 PDF) | p262 |
| 其余 | RELSPEC 段+表 (111-122), BS 段+表 (124-138), MB 叙述 + Row 2-6 (140,143-147), relrec Ex1, suppbe Ex2, Rows 说明 | 归一化后在 after 中逐字存在 (MOVED 或副本 2 已有) | — |

结论: 副本 1 无独有且 PDF 有的信息被丢; 删除的均为副本 2 已有或副本 1 自身错值/改写. 同文件去重不留指针 (主控裁定) 可接受; 全仓无 `MB/examples.md#` 锚点链接, check_links 42 不变 → 无悬空锚点.
副本 2 改动 (diff copy2 vs after) 只有: :30 跨页断句合并; ms r3 MSORRES/MSSTRESC=1; Ex2 mb VISIT 1 ×6; Ex3 be r4 100.3 / r10 BELNKID 空; Ex4 WEEK 5 ×2; 插入 :208-282 块. 无其它行被改.

### 人工逐格 (渲染图)
| 表 | KB 行 | PDF | 结果 |
|---|---|---|---|
| Ex3 mb.xpt (重建, 24 列 × 6 行) | :241-248 | p262 220dpi 裁图 | 一致 (表头 24 列顺序; SPDEVID 仅 r3 ABC765; MBGRPID 1,1,空,2,2,2; MBLNKGRP 仅 r4-6=1; MBORRESU 仅 r5 CFU; MBRSLSCL r5 Qn 其余 Ord; r5 14700/14700/CFU/mL; MBLOC 全 STOMACH; MBSPCCND r1-2 CONCENTRATED; "ZIEHL NEELSEN ACID FAST STAIN"; MBTEST r4-6 小写 tuberculosis; 无 MBSPEC 列; VISIT WEEK 1; 2011-01-17T06:00) |
| Ex3 suppmb.xpt | :254-259 | p262 | 一致, 除 Row 列 PDF 7/8 → KB 5/6 (T-1) |
| Ex3 di.xpt (新增) | :265-268 | p263 | 一致 |
| Ex3 relrec.xpt (新增) | :274-281 | p263 | 一致 (6 行 BE/MB/BE/MS/MB/MS; ONE/MANY/ONE/ONE/ONE/MANY; A,A,B,B,C,C) |
| Ex3 be.xpt r4, r10 | :170, :176 | p260 | 一致 (100.3; BELNKID 空) |
| Ex1 ms.xpt r3 | :46 | p257 | 一致 (MSORRES 1, MSSTRESC 1; r9 MSSTRESC PDF 本空) |
| Ex2 mb.xpt VISIT | :109-114 | p258 layout "VISIT / 1" | 一致 |
| Ex4 mb.xpt VISIT + 表头 | :293-296 | p263 | WEEK 5 一致; 表头 PDF MBGPRID (T-2, KB MBGRPID), MBTRESN (KB 照 PDF) |

### (2) fp_match 11 条回归 → 判定: writer 正确, 全部 ATOM_ERR (原子 verbatim 错, 非 KB 缺陷)
| atom | 原子 verbatim (错) | PDF 渲染 (对) | KB 现值 |
|---|---|---|---|
| ig34_p0257_a010 | MSORRES/MSSTRESC 空 | 1 / 1 | :46 = PDF |
| ig34_p0258_a019-024 | VISIT "VISIT" | "VISIT 1" | :109-114 = PDF |
| ig34_p0260_a009 | BEREFID 100 | 100.3 | :170 = PDF |
| ig34_p0260_a015 | BELNKID 3 | 空 | :176 = PDF |
| ig34_p0263_a021/a022 | VISIT WEEK 1 | WEEK 5 | :295-296 = PDF |
T3 回写 ledger 时须按 PDF 改这 11 条 verbatim. 注意 a009/a015 是本批 VALUE_DIFF 原子本身, 其 verbatim 也是错值 → 同样 ATOM_ERR.
prose 原子直查目标文件 (norm in MB/examples.md): p0263_a001/a006, p0261_a002/a003/a014 全部 True.

### (3) O-a 裁定 (p262 ms/suppms)
- PDF p262 无新节标题: MS 叙述 ("Results from drug susceptibility tests…") + Rows 1-2/3-4 + ms.xpt + suppms.xpt 属 §6.3.5.7.3 (p256 标题 "Microbiology Specimen/Microbiology Susceptibility Examples") 的 Example 3 — MB/MS **共用**节, 无单一域独占.
- 该内容已在 MS/examples.md Example 3 (:52-73). MB 再抄一份 = 新造跨文件重复, 与 D2 去重方向相反 → **MB 不补表**.
- 归为 D2 跨文件重复类 → MB/examples.md 在 :261 DI 句之前加**一行交叉引用**到 `../MS/examples.md` Example 3 (MS 叙述 + ms.xpt + suppms.xpt, PDF p262), 使 "rows 3-4 of the MS dataset example" 可解析. 属纯导航, 符合 dispatch notes D2 交叉引用 + KB_AUTHORED 纯导航规则. 由主控指派执行 (本批 writer 正确地未自造).
- 连带 (B-MS/主控): MB Ex1/Ex2 的 ms.xpt 与 MS/examples.md Ex1/Ex2 是同类跨文件重复 (O-b), 处置口径应与此统一; MS/examples.md Ex3 叙述有 KB 扩写 "from the gastric TB study (see MB Example 3)" 且缺 PF 一句 (p262 "Genotypic tests that give results of specific genetic polymorphisms…"), 交 B-MS.

### 问题表 (均非阻断)
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| MB/examples.md:258-259 (T-1) | G-TB4 | Row 标号 PDF 7/8, KB 改 5/6; 改了 PDF 原值, 属编辑判断 → 主控确认 PDF_TYPO 口径 (TR 跳号先例) | p262 suppmb Row 列 "4 … 7 … 8" |
| MB/examples.md:293 (T-2/T-3) | 一致性 | 同一表头两处 PDF 笔误处理不一: MBGPRID→KB MBGRPID (修), MBTRESN 照录 (未修); 建议统一 | p263 "MBGPRID", "MBTRESN" |
| O-a | 完整/导航 | :261 引 "MS dataset example" 本文件无对应 → 加一行指针 (见上) | p263 "rows 3-4 of the MS dataset example" |

### G-TB6 反向溯源
新增/改动行全部在 PDF 找到出处 (p256-263), 无自造词句. 结构行签字: :3 节标题 (原副本 2 已有), `**relspec.xpt**` `**mb.xpt**` `**suppmb.xpt**` `**di.xpt**` `**relrec.xpt**` 标签行, 各表头/分隔线 (:216-217, :241-242, :252-253, :265-266, :274-275), `- Row n:` 列表格式 (由 `**Row n:**` 改写, 纯格式). 位置: RELSPEC/MB 块按 PDF p261-262 顺序置于 bs.xpt 之后, di/relrec 在 Ex3 末 Ex4 前 = PDF 顺序.
R2 recheck: 本批 t2_recheck 为空.
