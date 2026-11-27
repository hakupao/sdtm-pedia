# T4 第二轮改台账 (R2L) — 独立 auditor (规则 A)

<!-- chain: E (plans) -->
> 状态: **PASS** (2026-11-27). 审查者 `oh-my-claudecode:verifier` (opus), 严格只读 (没有运行 `scripts/` 下任何脚本); 主控誊录, 不改判. 对象: 工作树里 writer 改后的台账 (md5 `16024ac09721cb3f8519cd68fa455196`).
> 方法: N 先定 = 33; `random.Random(20261134)`, 各组 id 排序后 `rng.sample`: R1-row 抽 15 / 51、v2.0-TOC 全核 2、registered-typo 抽 10 / 19、registered-typo-oos 全核 6. 每条先独立判 (SDTM v2.0 各页看渲染页; SDTMIG 各页先 `pdftotext -bbox` 定位单元格再 `pdftoppm -r 250` 裁切放大), 判完再对照先前审查者的原始结果.

## 结论
抽检 33 条, **33 条全部成立**, 无 "不成立"、无 "看不出"; 与先前审查者的结论 33 / 33 一致. 两项机械核通过. 抽样范围内 KB 的精简列和改正值没有发现写错.

## 逐条结果 (誊录)

| # | atom_id | 组 | 新标签 | 判定 | 依据 |
|---|---|---|---|---|---|
| 1 | `sv20_p0059_a010` | R1-row | IE | 成立 | p59 TS 表 TSSEQ: 精简列与 `model/05_study_level_data.md:221` 一致; PDF Notes 有内容, KB 本表无 Notes 列 |
| 2 | `sv20_p0059_a002` | R1-row | IE | 成立 | p59 TI 表 TIVERS, 与 05:207 一致; Notes 有内容, KB 未收 |
| 3 | `sv20_p0069_a004` | R1-row | IE | 成立 | p69 §6.6 SREL (Role = Record Qualifier), 与 `model/06_relationship_datasets.md:154` 一致; Notes 三段 KB §6.6 表未收; `04_associated_persons.md:42` 收的是 p50 那句 (device), 不能算收了 p69 的 Notes |
| 4 | `sv20_p0058_a007` | R1-row | IE | 成立 | p58 TM TMRPT, 与 05:190 一致; Notes 未收 |
| 5 | `sv20_p0055_a007` | R1-row | IE | 成立 | p55 TP TPSTGORD, 与 05:125 一致 (含 Usage 列); Notes 未收 |
| 6 | `sv20_p0053_a016` | R1-row | IE | 成立 | p53 TX TXPARMCD, 与 05:79 一致; Notes 未收 |
| 7 | `sv20_p0059_a015` | R1-row | IE | 成立 | p59 TS TSVALNF, 与 05:226 一致; Notes 未收 |
| 8 | `sv20_p0059_a012` | R1-row | IE | 成立 | p59 TS TSPARMCD, 与 05:223 一致; Notes 与 Examples 未收 |
| 9 | `sv20_p0059_a014` | R1-row | IE | 成立 | p59 TS TSVAL, 与 05:225 一致; Notes 与 Examples 未收 |
| 10 | `sv20_p0053_a014` | R1-row | IE | 成立 | p53 TX SET: Qualified 列的 SETCD 已在 05:77 写进 Role 括号; Notes 未收 |
| 11 | `sv20_p0060_a001` | R1-row | IE | 成立 | p60 TSVCDVER, 与 05:229 一致 (Usage = Not in nonclinical trials); Notes 未收 |
| 12 | `sv20_p0055_a006` | R1-row | IE | 成立 | p55 TP RPATH, 与 05:124 一致; Notes 未收 |
| 13 | `sv20_p0058_a006` | R1-row | IE | 成立 | p58 TM TMDEF, 与 05:189 一致; Notes 未收 |
| 14 | `sv20_p0059_a017` | R1-row | IE | 成立 | p59 TS TSVCDREF, 与 05:228 一致; Notes 与 Examples 未收 |
| 15 | `sv20_p0055_a012` | R1-row | IE | 成立 | p55 TP RPRFDY, 与 05:130 一致; Notes 未收 |
| 16 | `sv20_p0003_a011` | v2.0-TOC | IE | 成立 | `sv20_p0003.txt:18` "9 APPENDICES"; `knowledge_base/model/` 下 grep appendi / warrant / disclaim 零命中 |
| 17 | `sv20_p0003_a012` | v2.0-TOC | IE | 成立 | `sv20_p0003.txt:19` Appendix A; `model/` 里没有; KB 只有 SDTMIG 的 `chapters/ch10_appendices.md:422` Appendix F (另一份文档) |
| 18 | `ig34_p0037_a002` | registered-typo | PDF_TYPO | 成立 | p37 印 "case that appears the source"; `ch04_general_assumptions.md:668` 写 "appears in the source"; 登记 B-ch04 T-3 |
| 19 | `ig34_p0278_a015` | registered-typo | PDF_TYPO | 成立 | p278 Method B 第 13 行 RDOMAIN 印 PC; `PC/examples.md:103` 写 PP; 登记 B-PCPP T-2 |
| 20 | `ig34_p0262_a016` | registered-typo | PDF_TYPO | 成立 | p262 suppmb Row 列印 1,2,3,4,7,8; `MB/examples.md:204` 写 5; 登记 B-MB T-1 |
| 21 | `ig34_p0357_a014` | registered-typo | PDF_TYPO | 成立 | p357 第 15 行 TRSTRESC 印 -60; `TR/examples.md:84` 写 -50; 登记 B-TR T-2 |
| 22 | `ig34_p0147_a025` | registered-typo | PDF_TYPO | 成立 | p147 bs 第 3 行 BSREFID 印 298B1-1R0; `BE/examples.md:124` 写 298R1-1R0; 登记 B-BE T-3 |
| 23 | `ig34_p0119_a017` | registered-typo | PDF_TYPO | 成立 | p119 Ex7 relrec Row 列印 1,2,6,3,4,6; `EX/examples.md:413` 写 3; 登记 B-EX T-1 |
| 24 | `ig34_p0147_a026` | registered-typo | PDF_TYPO | 成立 | p147 bs 第 4 行同上; KB :125; 登记 B-BE T-3 |
| 25 | `ig34_p0277_a026` | registered-typo | PDF_TYPO | 成立 | p277 Method A 第 3 行 IDVAR 印 PPGRPID; `PC/examples.md:79` 写 PCGRPID; 登记 B-PCPP T-1 |
| 26 | `ig34_p0047_a009` | registered-typo | PDF_TYPO | 成立 | p47 放大: "(–TPTREF" 单个 en dash; `ch04:1122` 写 "(--TPTREF"; 登记 S-CH4 T-9 |
| 27 | `ig34_p0201_a005` | registered-typo | PDF_TYPO | 成立 | p201 放大: CPCELSTA Notes 印 "CPCELSTA and CPSMRKS"; `CP/spec.md:120` 写 CPCSMRKS; 登记 S-SPC1 CP T-20 |
| 28 | `ig34_p0083_a020` | typo-oos | PDF_TYPO | 成立 | p83 底部 Ex2 dm.xpt 表头印 BIRTHDTC; `SE/examples.md:79` 写 BRTHDTC; 登记 S-SPREL SE T-1 |
| 29-32 | `ig34_p0304_a026` ~ `a029` | typo-oos | PDF_TYPO | 成立 | p304 oe.xpt 第 1-4 行 OECAT 印 OCCULAR COMFORT; `OE/examples.md:142-145` 写 OCULAR; 登记 B-OE T-2 |
| 33 | `ig34_p0316_a023` | typo-oos | PDF_TYPO | 成立 | p316 放大: PELAT Notes 印 "laterallity"; `PE/spec.md:174` 写 laterality; 登记 S-FND PE T-1 |

## 机械核
1. 改后台账 78 行的 `verdict` 全部等于清单的 `to`; 改前全部等于 `now`; 改前改后 verdict 有变化的行正好是这 78 行; `ig34_p0412_a006` / `a007` / `a008`、`ig34_p0413_a010`、`ig34_p0293_a038` 前后都是 PDF_TYPO. 另有 5 行只改了其它字段 (登记指针), 归结构 reviewer 核.
2. 新增两条登记属实: `T4R2 sv20 N-1` (p69 "subject or pool" vs p50 "device"; 两处 Role 也不同; KB `04_associated_persons.md:42` 照录 p50, `06:154` 只有精简列); `T4R2 RELSPEC N-1` (p440 图里 SPC-003 标 "(Brain)", 表第 5 行 SPEC = TISSUE; KB `RELSPEC/examples.md:17` 与 `:50` 两处照录).

## 顺带看到的 (只记录)
- 台账辅助字段过期 (不影响标签): 两条 TOC 原子的 `md_atom_ids` 仍指向 SDTMIG 的 `md_ch10_a240` / `a245`; `sv20_p0060_a001` 的 `discrepancy` 文字与 KB 现文不符; `ig34_p0304_a026` / `a027` 同指 `md_dmOE_ex_a093`、`a028` / `a029` 同指 `a095`.
- 原子 verbatim 抽错 (再次说明它不是真值): 被 "顺手改对" 的 `ig34_p0147_a026` / `p0277_a026` / `p0047_a009` / `p0278_a015`; 抽成别的错值的 `p0201_a005`、`p0304_a026` ~ `a029`、`p0147_a025`.
- 收尾: `git status --short knowledge_base archive releases` 无输出; `git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`.
