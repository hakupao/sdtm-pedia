# T4.1 第三轮补检 — 包 9 (R3_PDF_TYPO, T201-T225) 独立审查结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T06:40:05Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round3_v1.0.md` (R3_PDF_TYPO 层; 三件事 ① PDF 确有登记的问题 ② KB 与 `handling` 一致 ③ 其余内容 KB = PDF)
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`): p267 (整页 110dpi); p274 (表格区 200dpi); p280 (整页 + 引言段与 Method A 两段 300dpi 放大, 区分 I / 1 字形); p281 (整页); p293 (表格区 220dpi); p304 (relrec 区 250dpi); p336 (rs.xpt 区 200dpi); p342 (sc.xpt 区 200dpi). 另出图未细看: p273/285/296/298/311/328/332/334/335/338 (这些是正文句子, 以文本层为准).
- 用过的命令:
  - `pdftoppm -r {110|200|220|250|300} -f N -l N [-x -y -W -H] -png "<SDTMIG pdf>" <scratchpad>/r3_9/...`
  - `pdftotext -f 293|294 -l 293|294 -raw "<SDTMIG pdf>" - | grep -n -A1 REPLACEMENT`
  - PDFKit (`swift <scratchpad>/r3_9/k.swift`) 打印 p293/p294 "REPLACEMENT/" 与 "MISSING" 之后的字符码 (看折行处是否有空格字符)
  - Python 比对: 取 `work/pdf_pages/ig34_pNNNN.txt` 对应行拼接, 只套用登记的那一处替换, 归一化 (空白 / `**` / 列表前缀) 后在 `knowledge_base/domains/<域>/*.md` 全文件里找子串 (T202/T204-T210/T212/T213/T215-T221/T223 共 18 条全部命中, 命中行见表); 另 `grep -c -F` 确认每处登记笔误串确实在 PDF 文本层里
  - 从 `work/t2_pdf_typo_registry.jsonl` 按 id 取出全部 21 条相关登记核 `handling`

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| T201 | `ig34_p0267_a006` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p267 mi.xpt 表头; `ig34_p0267.txt:8`; `knowledge_base/domains/MI/examples.md:50` | B-MI T-1. 渲染页表头确为 "MIDRVL"; KB "MIDRVFL" (改正值); 其余 19 个表头逐格一致 |
| T202 | `ig34_p0273_a037` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0273.txt:41-43`; `knowledge_base/domains/PP/examples.md:46` | B-PCPP T-9. PDF "pre-corrdinating", KB "pre-coordinating"; 其余逐字一致 |
| T203 | `ig34_p0274_a009` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p274 pp.xpt r6; `ig34_p0274.txt:20-22`; `knowledge_base/domains/PP/examples.md:59` | B-PCPP T-5. 渲染页 r6 PPSEQ 印 "1", KB 写 6; 其余 19 格 (ABC-123/PP/123-1001/B2222/AUCIFO/AUC Infinity Obs/DRUG PARENT/NCA/520/h*ng/L/520/520/h*ng/L/PLASMA/LIN-LOG TRAPEZOIDAL METHOD/Y/1/2001-02-01T12:00) 逐格一致 |
| T204 | `ig34_p0280_a036` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p280 (300dpi); `ig34_p0280.txt:42-45`; `knowledge_base/domains/PC/examples.md:278` | B-PCPP T-8b. 渲染页确为 "DYDRGX_HALF" (同页 relrec IDVARVAL 为 DY1DRGX_HALF); KB "DY1DRGX_HALF"; 其余逐字一致 |
| T205 | `ig34_p0280_a039` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p280 (300dpi); `ig34_p0280.txt:50-52`; `knowledge_base/domains/PC/examples.md:284` | B-PCPP T-8. 放大后字形为衬线大写 I ("DYIDRGX_A"), 与同段 "DY1_DRGX_A" 的 1 不同, 不是文本层误识; KB "DY1DRGX_A"; 其余逐字一致 |
| T206 | `ig34_p0281_a002` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p281 Method B; `ig34_p0281.txt:2-3`; `knowledge_base/domains/PC/examples.md:299` | S-SPC2 N-1. PDF "includes PP records with PCSEQ", 同页 relrec r1-12 RDOMAIN=PC; KB "PC records"; 其余逐字一致 |
| T207 | `ig34_p0281_a003` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p281 Method B; `ig34_p0281.txt:4-5`; `knowledge_base/domains/PC/examples.md:300` | S-SPC2 N-1 (包里 KB 指针给的是 :299, 实际对应 :300). PDF "PP records with PCSEQ", KB "PC records"; 其余逐字一致 |
| T208 | `ig34_p0281_a031` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p281 Method C; `ig34_p0281.txt:35-36`; `knowledge_base/domains/PC/examples.md:333` | S-SPC2 N-2. PDF "all PP records with PGRPID values", 同页 relrec r1-2 RDOMAIN=PC / IDVAR=PCGRPID; KB "all PC records with PCGRPID values"; 其余逐字一致 |
| T209 | `ig34_p0281_a032` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p281 Method C; `ig34_p0281.txt:37-38`; `knowledge_base/domains/PC/examples.md:334` | S-SPC2 N-2 (包里指针 :333, 实际 :334). PDF "all PP records with PGRPID value", relrec r8 RDOMAIN=PC/PCGRPID; KB "all PC records with PCGRPID value"; 其余逐字一致 |
| T210 | `ig34_p0285_a015` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0285.txt:30-33`; `knowledge_base/domains/NV/assumptions.md:23` (在 `## §6.3.7.1 Generic Morphology/Physiology Specification` 下) | B-NV N-1. PDF "may included", KB "may include"; 其余逐字一致, 位置在 §6.3.7.1 节下 |
| T211 | `ig34_p0293_a038` | R3_PDF_TYPO | PDF_TYPO | UNVERIFIABLE | 渲染 p293 mk.xpt r3 (220dpi); `ig34_p0293.txt:38-40`; `pdftotext -raw` p293 / p294; `knowledge_base/domains/MK/examples.md:53` | B-MK T-2. ② ③ 成立: KB "REPLACEMENT/SURGICAL", 其余 19 格逐格一致 (含 3 个空格子、NOT DONE、PROXIMAL INTERPHALANGEAL JOINT 2 OF THE HAND 等). ① 判不了: 渲染页 MKREASND 格里 "REPLACEMENT/" 在行尾, "SURGICAL ALTERATION" 在下一行, 这是单元格自动折行; 折行处有没有空格字符, 渲染页看不出来. 文本层、`pdftotext -raw`、PDFKit 都只给一个换行, 对已知按空格折行的地方 ("MISSING⏎ANATOMY") 也只给换行, 所以分不出来. p294 r12 同值印成一行 "REPLACEMENT/SURGICAL", 但那一页的列宽不同, 不能反推 r3. 登记自己的 note 也写着 "折行歧义而非确证印刷错". 缺的东西: 字符级解析 p293 内容流 (这台机器上没有 mutool / PyMuPDF / pypdf). 如果其实没有空格, 那 KB = PDF, 标签应该是 EXACT 而不是 PDF_TYPO; 两种情况下 KB 内容本身都没错 |
| T212 | `ig34_p0296_a019` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0296.txt:28`; `knowledge_base/domains/NV/examples.md:11` | B-NV T-1. PDF "an fluorodeoxyglucose", KB "a fluorodeoxyglucose"; 其余逐字一致 |
| T213 | `ig34_p0298_a001` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0298.txt:1-2`; `knowledge_base/domains/NV/examples.md:63` | B-NV N-2. PDF "links the / each" (跨行), KB "links each"; 原子这一段在 KB :63 末尾, 其余逐字一致 |
| T214 | `ig34_p0304_a012` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p304 relrec (250dpi); `ig34_p0304.txt:14`; `knowledge_base/domains/OE/examples.md:121` | B-OE T-1. 渲染页表头确为 "IDVARAL"; KB "IDVARVAL"; 其余 7 个表头一致 (下方 r1/r2 数据也一致: :123-:124) |
| T215 | `ig34_p0311_a035` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0311.txt:43-44`; `knowledge_base/domains/RE/examples.md:59` | B-RE T-1. PDF "IREEA2", KB "IRREA2"; 其余逐字一致 |
| T216 | `ig34_p0328_a007` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0328.txt:14-16` (QS 节, 下接 "QS – Examples"); `knowledge_base/domains/QS/assumptions.md:59` | B-RS T-6 (QS 副本). PDF "--STRNC", KB "--STNRC"; 其余逐字一致 ("--⏎SPCCND" 是折行) |
| T217 | `ig34_p0332_a009` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0332.txt:21-24`; `knowledge_base/domains/RS/assumptions.md:28` | B-RS T-2. PDF "will contained", KB "will contain"; 其余逐字一致 |
| T218 | `ig34_p0334_a011` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0334.txt:18-19`; `knowledge_base/domains/RS/examples.md:12` | B-RS T-8. PDF "symptomatic determination", KB "symptomatic deterioration"; 其余逐字一致 |
| T219 | `ig34_p0335_a016` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0335.txt:29-31`; `knowledge_base/domains/RS/examples.md:51` | B-RS T-7. PDF "RSPLNKGRP = "CM2"", KB "RSLNKGRP"; 其余逐字一致 (包里指针 :50 是 Row 1, 实际 :51) |
| T220 | `ig34_p0335_a017` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0335.txt:32-34`; `knowledge_base/domains/RS/examples.md:52` | B-RS T-7. PDF "RSPLNKGRP = "PR2"", KB "RSLNKGRP"; 其余逐字一致 |
| T221 | `ig34_p0335_a018` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0335.txt:35-37`; `knowledge_base/domains/RS/examples.md:53` | B-RS T-7. PDF "RSPLNKGRP = "CM3"", KB "RSLNKGRP"; 其余逐字一致 |
| T222 | `ig34_p0336_a005` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p336 rs.xpt r3 (200dpi); `ig34_p0336.txt:2,7-8`; `knowledge_base/domains/RS/examples.md:57,61` | B-RS T-1. 渲染页 RSSTRESC 格确为 "REPSONSE" (RSORRES 是 RESPONSE); KB 写 "MINIMAL RESPONSE". 23 格逐格一致 (表头 23 列; RSDTC/RSDY/RSSTRTPT/RSSTTPT 四格空, RSENRTPT=BEFORE, RSENTPT=SCREEN). 注: 原子 verbatim 少一个空格子 (3 个), KB 的 4 个与 PDF 对得上, 是原子抽错 |
| T223 | `ig34_p0338_a006` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0338.txt:13-14` (RS 节, p336 "RS – Clinical Classifications Use Case Assumptions" 之后); `knowledge_base/domains/RS/assumptions.md:113` (在 `## QRS Shared Assumptions` 下) | B-RS T-5 (RS 副本). PDF "providing an resolution", KB "providing a resolution"; 其余逐字一致 |
| T224 | `ig34_p0342_a006` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p342 sc.xpt r2 (200dpi); `ig34_p0342.txt:14-18`; `knowledge_base/domains/SC/examples.md:35` | B-SC T-1. 渲染页 SCDTC 印 "20-17-04-01"; KB "2017-04-01"; 其余 16 格逐格一致 |
| T225 | `ig34_p0342_a007` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p342 sc.xpt r3 (200dpi); `ig34_p0342.txt:19-23`; `knowledge_base/domains/SC/examples.md:36` | B-SC T-1. 渲染页 SCDTC 印 "20-17-06-10"; KB "2017-06-10"; 其余 16 格逐格一致 (VISITNUM 13.1, SCDY 297) (包里指针 :35 是 r2, 实际 :36) |

## 计数 (R3_PDF_TYPO 层, 本包)

- HOLDS: 24
- NOT_HOLD: 0
- UNVERIFIABLE: 1 (T211 `ig34_p0293_a038`, B-MK T-2)

按层规则 ("任一层出现 UNVERIFIABLE → 该层不算通过"), 本包不算通过, 卡在 T211.

## 样本外发现

KB 内容问题: 无.

登记表文字前后不一致 (这里只记下, 没改; 不影响本包判定, `handling` 与 `kb_value` 一致, KB 也与之一致):
- `S-SPC2 N-2` 的 `basis` 写 "应为 PPGRPID, 照录", 与 `handling` = "KB 写正确值"、`kb_value` = "PC / PCGRPID" 对不上 (该条 `note` 已说明 PPGRPID 是草稿候选值, 有误). `S-SPC2 N-1`、`B-NV N-1`、`B-NV N-2` 的 `basis` 也带 "照录" 二字, 同样与 `handling` = "KB 写正确值" 对不上. 建议后续整理登记时把 `basis` 的文字改成与 `handling` 一致.
- 样本包里几条 KB 指针偏了 (T207 → :300、T209 → :334、T219-T221 → :51-:53、T225 → :36), 是自动给的指针问题, 不是 KB 的问题.
