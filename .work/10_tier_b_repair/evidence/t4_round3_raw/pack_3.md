# T4.1 第三轮补检 — 包 3 (R3_IG34_EQUIV, T51-T75) 审查结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T06:36:56Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round3_v1.0.md` (R3_IG34_EQUIV 层)
- 看过的渲染页: SDTMIG v3.4 p146 (核 T57 "[2]In" 脚注标记与空格)
- 用过的命令 (临时脚本在 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/r3_3/`):
  - `python3 -I scratchpad/r3_3/chk.py` — 原子文本 (去弯引号 / `**` / 空白归一, 去 "Row(s) N:" 前缀) 在 `knowledge_base/**/*.md` 逐行全库包含检索 (不依赖包里的 KB 指针)
  - `python3 -I scratchpad/r3_3/chk2.py` — 原子文本对 PDF 文本层 `ig34_pNNNN.txt` 归一后包含检查 (含 `--`+换行 合并), 25/25 原子与 PDF 一致 (无原子抽错)
  - `awk` 取每个 KB 命中行之前最近的 `#` 标题; `grep -E '^\s*Example [0-9]+'` 取 PDF 页 (含前 2 页) 上最近的 Example 编号, 两边对位
  - `grep -n` DM/examples.md 中 "QNAM-QLABEL" 全部出现处 (T52 多重命中消歧); 读 `ig34_p0077.txt`、`PC/assumptions.md` 95-112 行、`RS/assumptions.md` 10-20 行、`ig34_p0332.txt` 1-16 行
  - `python3 -I -c ...` 列出 `work/t2_pdf_typo_registry.jsonl` 中 pdf_page 落在本包 21 个页上的全部登记 (14 条), 逐条确认均不落在本包原子句内

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| T51 | `ig34_p0046_a014` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0046.txt:22-23`; `knowledge_base/chapters/ch04_general_assumptions.md:1093` (§4.4.10 Representing Time Points, 1070 行起) | 实为逐字; 位置对 |
| T52 | `ig34_p0077_a021` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0077.txt:46-48`; `knowledge_base/domains/DM/examples.md:362` (## Example 6) | 实为逐字. 包指针 212/214/216 是 Example 4 同句异处; 真正对应处是 362 行 (前后接同一 dm.xpt 3 行表与 suppdm Rows 1-3, 整段 "Collected race ... 1 race subcategory. CDASH ..." 与 PDF 一致) |
| T53 | `ig34_p0101_a009` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0101.txt:9-10`; `knowledge_base/domains/CM/assumptions.md:27` (CM – Assumptions, 假设 a) | 实为逐字 |
| T54 | `ig34_p0119_a012` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0119.txt:16` (Example 7); `knowledge_base/domains/EX/examples.md:405` (## Example 7) | 实为逐字 (仅 `Rows 4-6:` 加粗). 同页登记 B-EX T-1/T-2 在 relrec 表与 Rows 1-3 句, 不涉本句 |
| T55 | `ig34_p0119_a030` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0119.txt:39` (Example 8); `knowledge_base/domains/EX/examples.md:437` (## Example 8) | 实为逐字; 日期 2012-01-15 一致 |
| T56 | `ig34_p0141_a017` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0141.txt:33` (Example 3); `knowledge_base/domains/AE/examples.md:39` (## Example 3) | 实为逐字 |
| T57 | `ig34_p0146_a017` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0146.txt:22-24` + 渲染页 p146; `knowledge_base/domains/BE/examples.md:62` (## Example 2) | KB 在 "[2]" 与 "In" 之间多一空格 (渲染页确认 PDF 印作 "integrity.[2]In"), 其余逐字; 纯空白差, 信息等价. 同页登记 B-BE T-1/T-2 在 bs.xpt 表, 不涉本句 |
| T58 | `ig34_p0151_a0007` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0151.txt:11` (Example 1); `knowledge_base/domains/CE/examples.md:5` (## Example 1) | 实为逐字 |
| T59 | `ig34_p0208_a012` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0208.txt:26-27` (Example 1); `knowledge_base/domains/CP/examples.md:9` (## Example 1) | 实为逐字 |
| T60 | `ig34_p0218_a007` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0218.txt:12` (Example 8); `knowledge_base/domains/CP/examples.md:263` (## Example 8) | 实为逐字. 同页登记 B-CP T-4 在下一段段末, 不涉本句 |
| T61 | `ig34_p0219_a016` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0219.txt:59-65` (Example 9, 56 行起); `knowledge_base/domains/CP/examples.md:297` (## Example 9) | 实为逐字 (整段 4 句全在). 同页登记 B-CP T-10 在 Ex8 表格, 不涉本段 |
| T62 | `ig34_p0227_a019` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0227.txt:33-34` (Example 5); `knowledge_base/domains/GF/examples.md:147` (## Example 5) | 实为逐字. 同页登记 B-GF T-2/U-2 在 MB 表格, 不涉本句 |
| T63 | `ig34_p0233_a008` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0233.txt:6-7` (Example 1); `knowledge_base/domains/IS/examples.md:7` (## Example 1) | 实为逐字; ISTSTOPO / SCREEN / CONFIRM / QUANTIFY 一致 |
| T64 | `ig34_p0237_a004` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0237.txt:5-6` (Example 6); `knowledge_base/domains/IS/examples.md:129` (## Example 6) | 实为逐字. 同页登记 B-IS T-5/U-3 在 Ex7, 不涉本句 |
| T65 | `ig34_p0246_a006` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0246.txt:12-14` (Example 1); `knowledge_base/domains/LB/examples.md:5` (## Example 1) | 实为逐字; 8 个变量名逐一一致 |
| T66 | `ig34_p0248_a012` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0248.txt:16-19` (Example 5); `knowledge_base/domains/LB/examples.md:90` (## Example 5) | 实为逐字 (仅 "Note:" 加粗) |
| T67 | `ig34_p0277_a018` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0277.txt:19` (§6.3.5.9.3 Example 1); `knowledge_base/domains/PC/examples.md:66` (## §6.3.5.9.3 Relating PP Records to PC Records — Worked Examples > ### Example 1) | 实为逐字. 包指针 PP/examples.md:106-108 偏; 真正对应处在 PC/examples.md:66, 紧接 "#### Method A" (68 行), 与 PDF 顺序一致. 同页登记 B-PCPP T-1/T-4 在 Method A 表/文字, 不涉本句 |
| T68 | `ig34_p0284_a007` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0284.txt:9-12` (PC-PP Conclusions); `knowledge_base/domains/PC/assumptions.md:107` (### PC-PP Conclusions, 于 ## §6.3.5.9.3 下) | 实为逐字. 包里 KB 指针为 "(无)", 全库检索命中 1 处 |
| T69 | `ig34_p0284_a008` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0284.txt:13-22`; `knowledge_base/domains/PC/assumptions.md:109` (### PC-PP Conclusions) | 实为逐字 (PDF "--\nGRPID" 为断行, KB "--GRPID"). 包里 KB 指针 "(无)", 全库检索命中 1 处 |
| T70 | `ig34_p0297_a029` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0297.txt:35` (Example 2); `knowledge_base/domains/NV/examples.md:61` (## Example 2) | 实为逐字 |
| T71 | `ig34_p0298_a021` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0298.txt:32-33` (Example 2 末, 34 行起 §6.3.7.5); `knowledge_base/domains/NV/examples.md:87` (## Example 2) | 实为逐字. 同页登记 B-NV N-2 在 "links the each" 句, 不涉本句 |
| T72 | `ig34_p0332_a004` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0332.txt:14` (spec 表后、§6.3.9.3.1 前); `knowledge_base/domains/RS/assumptions.md:18` (## RS – Specification 后、## §6.3.9.3.1 前) | 实为逐字; 位置与 PDF 次序一致. 同页登记 B-RS T-2 在 28 行 "will contain", 不涉本句 |
| T73 | `ig34_p0400_a003` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0400.txt:11-12` (TA Example 7); `knowledge_base/domains/TA/examples.md:889` (## Example 7, 865 行起) | 实为逐字 |
| T74 | `ig34_p0400_a010` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0400.txt:29` (TA Example 7); `knowledge_base/domains/TA/examples.md:931` (## Example 7) | 实为逐字. 包指针 572/721/803 是 Example 4/5/6 的同句; Example 7 的对应处是 931 行段首 |
| T75 | `ig34_p0400_a012` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0400.txt:31-32` (TA Example 7); `knowledge_base/domains/TA/examples.md:931` (## Example 7) | 实为逐字 |

## 计数 (R3_IG34_EQUIV, 25 条)

| 判定 | 条数 |
|---|---|
| HOLDS | 25 (其中 24 条实为逐字; T57 仅多一空格) |
| TYPO_AFFECTED | 0 |
| NOT_HOLD | 0 |
| UNVERIFIABLE | 0 |

原子抽错: 0 (25 条原子均与 PDF 文本层一致).

## 样本外发现的 KB 内容问题

无.
