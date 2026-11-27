# T4.1 第二轮补检 — TYPO_SIB 层 包 3 (R28-R52) 审查结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:39:42Z (`date -u`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` (背景 / 判定口径) + `subagent_prompts/t4/t4_supp_round2_v1.0.md` (TYPO_SIB 层, 冲突以后者为准)
- 样本包: `.work/10_tier_b_repair/work/t4/round2/round2_pack_3.md` (25 条)
- 登记表: `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` (按 id 查 15 条: S-CH4 T-8 / T-9 / T-10e, S-SPEC1 T-3, B-DM T-1 / T-3, B-SM T-3, B-EX T-1 / T-3 / T-4, B-ML T-1, B-AE T-4, B-BE T-3, B-HO T-1, S-SPC1 CP T-16b)
- 看过的渲染页 (SDTMIG v3.4 物理页, 250 dpi 局部裁切): p43 (两处: "ONGOING"' 行; CMSTRF.Some 行), p47 (–TPTREF 所在列表项), p64 (脚注 ²), p69 (Ex3 Row 1-3 叙述), p78 (Ex7 dm 表), p85 (Rows 叙述 + sm.xpt + 表下叙述 hyypoglycemic), p113 (列表四项), p114 (EX 叙述), p119 (vs.xpt + relrec.xpt), p124 (ml.xpt r5-r9), p142 (Ex5 表头 + Ex6 表头), p147 (bs.xpt / suppbe.xpt / relspec.xpt / be.xpt 续), p170 (Ex1 r2-r7 + Ex2 r1-r6), p205 (asm 3-5)
- 用过的命令:
  - `pdftotext -f N -l N -bbox "source/cdisc/SDTMIG v3.4 (no header footer).pdf" <scratch>/bb_N.html` (定位词坐标)
  - `pdftoppm -r 250 -f N -l N -x 0 -y <top> -W <pagewidth*250/72> -H <h> -png ...` (裁切放大; 脚本 `<scratch>/crop.sh`, scratch = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/r2_s1/`)
  - `grep -n` 各页文本层 `work/pdf_pages/ig34_pNNNN.txt`; `sed -n Lp` 读 KB 对应行; `grep -n "^| Row | STUDYID" knowledge_base/domains/AE/examples.md` 定位 AE Ex5/Ex6 表头

## 判定表

| # | atom_id | 层 | 终态 | 登记 | 判定 | 依据 (PDF / KB) | 说明 |
|---|---|---|---|---|---|---|---|
| R28 | `ig34_p0043_a010` | TYPO_SIB | EXACT | S-CH4 T-8 | **TYPO_AFFECTED** | PDF p43 文本层 L13 + 渲染页; KB `knowledge_base/chapters/ch04_general_assumptions.md:932` | 渲染页确印 `"PRIOR", "ONGOING"', or "CONTINUING"` (多一撇号), 正是本原子句; KB 写 `"ONGOING",`. 差异 = 登记笔误 → 应为 PDF_TYPO |
| R29 | `ig34_p0043_a022` | TYPO_SIB | EXACT | S-CH4 T-10e | NOT_AFFECTED | PDF p43 L31-32 + 渲染页; KB `ch04_general_assumptions.md:947` (下一句在 :949) | PDF 印 `definition of CMSTRF.Some sponsors` — 笔误是本原子句末与下一句 ("Some sponsors…") 之间缺空格, 本原子自身字符 (`…meets the definition of CMSTRF.`) 与 KB 逐字一致; KB≠PDF 仅为空白 (KB 在 947/949 分段), EXACT 定义允许空白归一, 现标签成立. (边界型登记, 主控如采用更严口径可另议) |
| R30 | `ig34_p0047_a008` | TYPO_SIB | EXACT | S-CH4 T-9 | NOT_AFFECTED | PDF p47 L12-14 + 渲染页; KB `ch04_general_assumptions.md:1121` | 本项两处均印 `--TPTREF` (双连字符), 与 KB 逐字一致. 笔误 `(–TPTREF` 在下一列表项 (即 R31, p47 L17) |
| R31 | `ig34_p0047_a009` | TYPO_SIB | EXACT | S-CH4 T-9 | **TYPO_AFFECTED** | PDF p47 L17 + 渲染页; KB `ch04_general_assumptions.md:1122` | 渲染页确印 `dosing (–TPTREF and --ELTM would not` (en dash 单字符), 正是本原子; KB 写 `(--TPTREF`. 原子 verbatim 已被抽取 "顺手改对" |
| R32 | `ig34_p0064_a012` | TYPO_SIB | EXACT | S-SPEC1 T-3 | **TYPO_AFFECTED** | PDF p64 L40-42 + 渲染页; KB `knowledge_base/domains/DM/spec.md:296` | 渲染页确印 `…/ucm126396.pdf)` (URL 后孤立右括号), 即本脚注原子; KB 删去 `)`. 原子 verbatim 也无 `)` (抽取改对) |
| R33 | `ig34_p0069_a008` | TYPO_SIB | EQUIVALENT | B-DM T-3 | NOT_AFFECTED | PDF p69 L26-27 + 渲染页; KB `knowledge_base/domains/DM/examples.md:70` | 本原子 (Row 2 叙述) PDF 印 `ARMCD, ARM, ACTARMCD, and ACTARM`, 与 KB 一致. 笔误 `ACTRMCD` 在 Row 1 叙述 (p69 L23 `so ACTRMCD is also "AA"`; KB :68) |
| R34 | `ig34_p0069_a011` | TYPO_SIB | EQUIVALENT | B-DM T-3 | NOT_AFFECTED | PDF p69 L29-30 + 渲染页; KB `DM/examples.md:72` | 本原子 (Row 3 叙述) PDF 印 `ACTARMCD shows their actual treatment, "BR"`, 无笔误; KB 与 PDF 逐字一致 (含 `assignments`). 注: 原子 verbatim 写 `assignment` (少 s), 属原子抽取差异, KB = PDF |
| R35 | `ig34_p0078_a022` | TYPO_SIB | EXACT | B-DM T-1 | **TYPO_AFFECTED** | PDF p78 L26 + 渲染页 (Ex7 dm.xpt 第 4 行); KB `DM/examples.md:440` | 渲染页该行 Row 格印 `3` (与上一行重复), 其余格 `ABC789 DM ABC789-010-048 010-048 33 YEARS M UNKNOWN HISPANIC OR LATINO`; KB Row 格写 `4`, 其余逐格一致 |
| R36 | `ig34_p0085_a009` | TYPO_SIB | EXACT | B-SM T-3 | NOT_AFFECTED | PDF p85 L13 + 渲染页; KB `knowledge_base/domains/SM/examples.md:5` | 本句 PDF 印 `hypoglycemic` (正确), 与 KB 逐字一致. 笔误 `hyypoglycemic` 在 sm.xpt 表下叙述 (p85 L28 "Information in SM is taken from…"; KB :22) |
| R37 | `ig34_p0085_a011` | TYPO_SIB | EXACT | B-SM T-3 | NOT_AFFECTED | PDF p85 L16-17 + 渲染页; KB `SM/examples.md:9` | 同上, 本句 PDF 印 `2 hypoglycemic events` (正确), KB 一致 |
| R38 | `ig34_p0085_a012` | TYPO_SIB | EXACT | B-SM T-3 | NOT_AFFECTED | PDF p85 L18-20 + 渲染页; KB `SM/examples.md:11` | 同上, 本句 PDF 印 `No hypoglycemic events` (正确), KB 一致 |
| R39 | `ig34_p0113_a008` | TYPO_SIB | EQUIVALENT | B-EX T-3 | NOT_AFFECTED | PDF p113 L10 + 渲染页; KB `knowledge_base/domains/EX/examples.md:115` | 本列表项 (2011-01-14 至 01-20) PDF 印 `from bottles A, B and C`, 与 KB 一致. 笔误 `from ottles` 在第 4 项 (2011-01-23 至 01-28, p113 L13; KB :118) |
| R40 | `ig34_p0114_a003` | TYPO_SIB | EXACT | B-EX T-4 | NOT_AFFECTED | PDF p114 L4-5 + 渲染页; KB `EX/examples.md:154` | 本句两处 PDF 均印 `protocol-specified` (带连字符), KB 一致. 登记的 `protocol specified unit` 在 p115 L10 (登记 pdf_page=115; KB :207), 不在本页 |
| R41 | `ig34_p0119_a017` | TYPO_SIB | EQUIVALENT | B-EX T-1 | **TYPO_AFFECTED** | PDF p119 L21 + 渲染页 (Ex7 relrec.xpt 第 3 行); KB `EX/examples.md:413` | 渲染页 relrec Row 列印 `1,2,6,3,4,6`, 本原子行 Row 格印 `6` (`6 ABC123 VS VSLNKID ONE 1`); KB 写 `| 3 | ABC123 | VS | | VSLNKID | | ONE | 1 |`, 其余格一致. 包内 KB 指针给 413-416 区间, 对应行为 :413 |
| R42 | `ig34_p0124_a023` | TYPO_SIB | EXACT | B-ML T-1 | NOT_AFFECTED | PDF p124 L41 + 渲染页; KB `knowledge_base/domains/ML/examples.md:72` | 本行 (r8) PDF 印 `WHITE MILK`, 逐格与 KB 一致. 笔误 `WHTE MILK` 在 r2 (p124 L35; KB :66) |
| R43 | `ig34_p0142_a022` | TYPO_SIB | EQUIVALENT | B-AE T-4 | NOT_AFFECTED | PDF p142 L40 + 渲染页 (Ex6 ae.xpt 表头); KB `knowledge_base/domains/AE/examples.md:94` | 本原子是 **Example 6** 表头, 渲染页首格印 `Row`, 25 列与 KB :94 逐格一致. 登记的 "表头首格空白" 在 **Example 5** 表头 (p142 上方表, 渲染页确为空白; KB :79). 包内 KB 指针 (:79, Ex5) 偏了. 注: 原子 verbatim 漏 `AESPID` 列 (原子抽取差异), KB 按 PDF 有该列 |
| R44 | `ig34_p0147_a013` | TYPO_SIB | EXACT | B-BE T-3 | NOT_AFFECTED | PDF p147 L15 + 渲染页 (suppbe.xpt r3); KB `knowledge_base/domains/BE/examples.md:105` | suppbe r3 IDVARVAL PDF 印 `298R1-1R0` (正确), 逐格与 KB 一致. 笔误 `298B1-1R0` 在 bs.xpt r3/r4 BSREFID |
| R45 | `ig34_p0147_a026` | TYPO_SIB | EXACT | B-BE T-3 | **TYPO_AFFECTED** | PDF p147 L31 + 渲染页 (bs.xpt r4); KB `BE/examples.md:125` | 渲染页 bs r4 BSREFID 印 `298B1-1R0`; KB 写 `298R1-1R0`. 其余格 (RIN / RNA Integrity Number / QUALITY CONTROL / 9.3 / 空 / 9.3 / 9.3 / 空 / RNA / 2 / 2010-04-01T11:50) 逐格一致 |
| R46 | `ig34_p0147_a036` | TYPO_SIB | EXACT | B-BE T-3 | NOT_AFFECTED | PDF p147 L42 + 渲染页 (relspec r3); KB `BE/examples.md:140` | relspec r3 PDF 印 `298R1-1R0 RNA 298B1-1 3`, 逐格与 KB 一致 (PARENT `298B1-1` 为正确值, 非笔误). 笔误在 bs r3/r4 |
| R47 | `ig34_p0147_a037` | TYPO_SIB | EXACT | B-BE T-3 | NOT_AFFECTED | PDF p147 L43 + 渲染页; KB `BE/examples.md:141` | relspec r4 PDF 印 `298R1-1R1 RNA 298R1-1R0 4`, 与 KB 一致 |
| R48 | `ig34_p0147_a038` | TYPO_SIB | EXACT | B-BE T-3 | NOT_AFFECTED | PDF p147 L44 + 渲染页; KB `BE/examples.md:142` | relspec r5 PDF 印 `298R1-1R2 RNA 298R1-1R0 4`, 与 KB 一致 |
| R49 | `ig34_p0147_a039` | TYPO_SIB | EXACT | B-BE T-3 | NOT_AFFECTED | PDF p147 L45 + 渲染页; KB `BE/examples.md:143` | relspec r6 PDF 印 `298R1-1R3 RNA 298R1-1R0 4`, 与 KB 一致 |
| R50 | `ig34_p0170_a0007` | TYPO_SIB | EQUIVALENT | B-HO T-1 | NOT_AFFECTED | PDF p170 L41 + 渲染页 (Ex2 ho.xpt r3); KB `knowledge_base/domains/HO/examples.md:65` (表头 :61) | 本行 PDF 印 `REHABILITATION FACILITY` (正确), 11 列与 KB 表头/行逐格一致 (HOENRTPT/HOENTPT 空). 笔误 `REHABILIATION FACILITY` 在 Ex1 r5 (p170 L8; KB :25). 注: 原子 verbatim 在 HOTERM 后多一空格 (抽取差异) |
| R51 | `ig34_p0205_a006` | TYPO_SIB | EXACT | S-SPC1 CP T-16b | NOT_AFFECTED | PDF p205 L15-18 + 渲染页; KB `knowledge_base/domains/CP/assumptions.md:60` | Assumption 5 PDF 两处均印 `CPCSMRKS` (正确), KB 逐字一致. 笔误 `CPSCMRKS ×3` 在 Assumption 4 (p205 L13-14; KB :58) |
| R52 | `ig34_p0205_a010` | TYPO_SIB | EXACT | S-SPC1 CP T-16b | NOT_AFFECTED | PDF p205 L26-27 (文本层; 与 asm 5 同字形); KB `CP/assumptions.md:65` | 6.ii PDF 印 `CPSBMRKS and/or CPCSMRKS` (正确), KB 逐字一致. 笔误在 Assumption 4 |

## 计数 (TYPO_SIB, 本包 25 条)

| 判定 | 计数 | 编号 |
|---|---|---|
| TYPO_AFFECTED | 6 | R28, R31, R32, R35, R41, R45 |
| NOT_AFFECTED | 19 | R29, R30, R33, R34, R36-R40, R42-R44, R46-R52 |
| NOT_HOLD | 0 | — |
| UNVERIFIABLE | 0 | — |

TYPO_AFFECTED 6 条按 brief 并入待改标签清单候选 (EXACT/EQUIVALENT → PDF_TYPO), 交主人裁定; 本角色不改台账.

## 样本外 / 标签级观察 (非样本判定, 不修)

KB 内容问题: 无 (本包涉及的 KB 行均与 PDF 一致或按登记写改正值).

标签 / 抽取层观察 (供主控参考, 不影响上表判定):
1. R29 `S-CH4 T-10e` 是 "句间缺空格" 型登记, 落在两原子边界; 按 EXACT 允许空白归一判 NOT_AFFECTED. 若主控对此类登记采用 "影响相邻原子" 口径, 受影响的也可能是下一原子 (`Some sponsors may wish…`, KB `ch04_general_assumptions.md:949`), 不在本包.
2. R43 原子 verbatim 漏 `AESPID`, R34 原子写 `assignment`, R50 原子多一空格 — 均为原子抽取差异, KB = PDF; 现标签 EQUIVALENT 内容成立.
3. 包内自动 KB 指针偏离两处: R43 指向 Ex5 表头 `AE/examples.md:79` (应为 Ex6 `:94`); R41 给区间 413-416 (对应行 `:413`).
