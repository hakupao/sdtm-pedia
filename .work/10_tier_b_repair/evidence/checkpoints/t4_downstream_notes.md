# T4 给下游 sdtm-rag 的答复 (KB 格式约定 + 节变动清单)

<!-- chain: E (plans) -->
> 状态: **已完成** (2026-11-27). 主控只读核对后写的答复, 没有改 `knowledge_base/`、ledger、`archive/`、`releases/`, 也没有写 sdtm-rag 仓.
> 对象: 本地 KB 内容 = `00a2e93` (本仓 HEAD 的 KB 与之相同, `git diff --stat 00a2e93..HEAD -- knowledge_base` 为空). 对比基线 = tag `kb-2026.11.25` (sdtm-rag 现钉的版本).
> 来问: `/Volumes/DevSSD/Project/sdtm-rag/.work/10_split_and_public/evidence/checkpoints/kb_rehearsal_bf33bab.md` 的 "给 pedia 的反馈" 和 "新 KB 下的 pytest". 下文对该报告的说法逐条按本仓证据核对; 有出入的地方注明.
> 页码: `p` = SDTMIG v3.4 PDF 页 (`work/pdf_pages/ig34_pNNNN.txt`), `sv20 p` = SDTM v2.0 PDF 页.

## 一句话结论

| # | 问题 | 结论 |
|---|---|---|
| 1 | CT 单元格写法 | 共 6 种形态: 空、`*`、域码、`(短名) Cnnnnn`、多个用 `; ` 分隔、外部术语名 (如 `MedDRA`); 括号短名和 `*` 照 PDF, C-code 是 KB 补充; 已由 S-CT 断言脚本全检 + 独立审计渲染页抽 30 条核过. |
| 2 | `*` 单元格 | PDF 定义: "CDISC CT 目前没有, 但赞助方可能有自己的 CT / 将来可能有" (SDTMIG §4.3.1, p36); 是 PDF 原样的星号, 不是字典 token; 62/63 个 spec.md 表下已有 PDF 脚注原文说明. |
| 3 | DOMAIN 的 CT | 是字面值 (该变量唯一允许值 = 域码), 不是 codelist 引用 (SDTMIG §4.3.1 第 2 条, p36). |
| 4 | DM `RFSTDTC`/`RFENDTC` 类型 | 新值 `Char` 符合 PDF (p63 Type 列为 Char); 旧值 `DateTime` 来自 xlsx, 与 PDF 不一致, 已按 PDF 改 (S-SPEC1 `3a3b724`). |
| 5 | model 文件的 6 列定义行 | 是照 SDTM v2.0 PDF 的结果 (S-MOD1/S-MOD2 逐格核); 但第 6 列是 KB 自写的 Notes 列, 不是 PDF 的 Definition; 各变量在 PDF 里本来就出现在多张表, 出处见 §5 表. |
| 6 | 移走 / 改名的节 | 77 个文件标题有变 (删 85 / 增 226, 全量机器清单可复跑); 跨文件内容移动 15 组, 见 §6 表 A; 报告列的三处都成立, 另补 12 组. |
| 7 | 示例文件标题格式 | 有变, 7 个 `examples.md`; PC 新增无编号的 `## PC – Examples` (照 PDF p269), 原来 PC Example 1 误挂在 `## §6.3.5.9.3` 下, 现在 §6.3.5.9.3 只管合并例; 这很可能就是 PC 拿不到节号的原因. |

---

## 下游格式约定 (第 1-3 点; 以后改 CT 单元格格式前先通知 sdtm-rag)

> 适用于 `knowledge_base/domains/*/spec.md` 每个变量块的 `- **Controlled Terms:** <值>` 行 (63 个文件, 1917 个变量).
> 来源: 用户裁定 U5 / U6 (`evidence/checkpoints/t2_post_user_ack.md` 第 13-14 行) + 主控裁定 (d) "多 codelist 格 `(A) Cx; (B) Cy`" (`evidence/checkpoints/t2_S-CT.md` "主控裁定" 节). 执行批: S-CT (`44fb042`); `*` 由各 S-SPEC / 扫描批照录 (U2).
> **变更约定**: 这行的格式是 pedia ↔ sdtm-rag 的接口. 今后改格式 (加/删形态、改分隔符、改括号写法), 改之前在 sdtm-rag 仓说明, 并在发版说明里写明.

### 形态 (HEAD 全量统计)

复跑: 用 `^- \*\*Controlled Terms:\*\*\s?(.*)$` 取值, 把 `(…)` 记为 `(SN)`, `C\d+` 记为 `Cn` 后计数 (主控本次用的一次性 python 片段, 逻辑即此).

| 形态 | 个数 | 例 | 含义 | 下游应当 |
|---|--:|---|---|---|
| 空 | 983 | AE `STUDYID` | PDF 该格为空 | 无 CT |
| `(短名) Cnnnnn` | 560 | AE `AEPRESP`: `(NY) C66742` | PDF 写 codelist 短名 (带超链接, 括号); `Cnnnnn` 是 KB 补的 NCI codelist C-code | 括号内 = CDISC codelist submission short name; C-code = 该 codelist 的 NCI code |
| `(短名) Cnnnnn; (短名) Cnnnnn …` | 10 (2 码 6 处 / 3 码 2 处 / 5 码 2 处) | BS `BSSPEC`: `(SPECTYPE) C78734; (GENSMP) C111114` | PDF 一格列多个 codelist (纵排) | 按 `; ` 切分, 每段同上; 顺序 = PDF 顺序 |
| `*` | 129 | AE `AECAT` | 见下文第 2 点 | **不是 codelist, 也不是外部字典名** |
| 域码 (2-8 位大写) | 59 | VS `DOMAIN`: `VS` | 见下文第 3 点; 只出现在变量 `DOMAIN` | 字面值 |
| 外部术语 / 格式名 | 176 | `ISO 8601 datetime or interval` 113, `ISO 8601 duration` 45, `MedDRA` 11, `ISO 8601 duration or interval` 4, `LOINC` 2, `ISO 21090 NullFlavor` 1 | PDF 写外部术语或格式 (SDTMIG §4.3.1 第 4 条) | 外部字典 / 格式, 无 C-code |

合计 983+560+10+129+59+176 = 1917. 没有其他形态: 不存在 "只有 C-code 不带短名" (S-CT 断言 "un-prefixed C-code" = 0), 也不存在 "短名 + `*`" 的组合格 (SDTMIG §1.4.1 p10 提到过这种写法, 但 PDF 文本层的变量表里搜不到, KB 里 0 处).

### 第 1 点: `(短名) Cnnnnn` 照 PDF 的核对证据
- PDF 规则: SDTMIG §4.3.1 (p36) "The name of a CDISC codelist, represented as a hyperlink in parentheses (e.g., "(NY)")"; KB 对应 `knowledge_base/chapters/ch04_general_assumptions.md:655-662`.
- 写入: S-CT writer `evidence/checkpoints/t2_S-CT.md` — 63/63 域按 PDF spec 表页逐域解析, PDF 变量数 = KB 变量数 (合计 1917), 顺序一致; CT 格分类为 类 1 (加短名) 570 / 类 6 (填域码) 59 / 类 7 (已一致不动) 1288.
- 断言闸: `scripts/t2s/ct_assert.py` 规定每个 `(SHORT)→C-code` 对 `SDTM Terminology.xlsx` 实时核, 去掉 `(SHORT) ` 前缀后必须与改前相同; 结果 `class1 570 / codes 588 / class6 59 / notes 59 → RESULT PASS`, 变异 9/9 FAIL (`t2_S-CT.md` "断言闸" / "变异测试").
- 独立审计: `evidence/checkpoints/t2_S-CT_audit.md` 结论 **PASS**, 分层 N=30 (multi 6 / single 12 / DOMAIN 6 / note 5 / SR 1, seed 20261126), 每条对 PDF 渲染页的 CT 列核短名与顺序.
- KB 说明: 59 个含 C-code 的 spec.md 在脚注后、`## Cross References` 前有一行 `> KB note (not in SDTMIG): C-codes after the parenthesised codelist names are NCI codelist codes added by this KB (CDISC CT).` (例 `knowledge_base/domains/AE/spec.md:548`). SM/TD/TE/TV 不含 C-code, 不加.
- 与预演报告对照: 报告 "570 个单元格", 本仓数 = 570 格 / 588 个码, 一致. 报告说 "多个用 `; ` 分隔", 一致.

### 第 2 点: `*` 单元格
- **含义** (PDF 原文): SDTMIG §4.3.1 (p36) "A single asterisk (*) when CDISC Controlled Terminology is not currently available but the SDS Team expects that sponsors may have their own controlled terminology and/or the CDISC Controlled Terminology Team may develop controlled terminology in the future". 每张 spec 表的 PDF 脚注: "In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses." (如 p60、p64). §1.4.1 (p9) 同义.
- **为什么旧 KB 是空的**: 旧 KB 把 PDF 的 `*` 丢了. 用户裁定 U2 "CT 列照录 `*`" (`t2_post_user_ack.md:5`), 由 S-SPEC1-4 等批逐域补回; S-SPEC 各批审计做了 `*` 全总体 bbox 对 KB (如 `t2_S-SPEC1_audit.md:12` "全部 CT `*` 0 差异"; `audit_matrix.md` S-SPEC2/3 行 "CT `*` 全总体 bbox 对 KB 20/20 / 13/13").
- **KB 里有没有说明**: 有. 63 个 spec.md 中 62 个在表下照录了上面那条 PDF 脚注 (`> ¹In this column, an asterisk (*) indicates …`, 如 `knowledge_base/domains/VS/spec.md:348`). 唯一没有的是 BE: PDF p144 表头有 Format¹ 但页内没有脚注文字, KB 照 PDF 不补 (`t2_S-SPEC1_audit.md:7`); BE 有 1 处 `*` (`BEPARTY`). 另外 `chapters/ch04_general_assumptions.md:659` 是 §4.3.1 原文.
- **下游应当当成什么**: "可能受 CT 约束, 但目前没有 CDISC codelist" 的标记. 不是外部字典 token, 也没有 codelist 可查; 建议在 meta 里单独记成一个标志位 (例如 `ct_open: true`), 不进 `ct_dict`.
- 本仓不会在冻结期改写法. 用户如要 "可机读写法" (如改成文字), 属 KB 格式变更, 按上面的变更约定先通知 sdtm-rag.

### 第 3 点: DOMAIN 的 CT = 域码
- **字面值, 不是 codelist 引用.** SDTMIG §4.3.1 (p36) 第 2 条: "The single applicable value for the variable DOMAIN (e.g., "PR")". PDF spec 表里 DOMAIN 行的 CT 格就印着域码 (如 p134 AE 表 DOMAIN 行 = `AE`).
- 来源: 用户裁定 U6 "照 PDF 补域代码" (`t2_post_user_ack.md:14`); S-CT 类 6 = 59 处, 断言 "改前空 & 改后 = 本域代码且变量为 DOMAIN" (`t2_S-CT.md` 断言闸); 主控裁定 (a) 59/59 (RELREC/RELSPEC/RELSUB/SUPPQUAL 没有 DOMAIN 变量).
- 下游: 当作该变量的唯一允许值; 不要拿去查 codelist 或字典.

---

## 第 4 点: DM `RFSTDTC` / `RFENDTC` 的类型

- **新值 `Char` 符合 PDF.** PDF p63: `RFSTDTC  Subject Reference Start Date/Time  Char  ISO 8601 datetime or interval …`, `RFENDTC … Char …` (`work/pdf_pages/ig34_p0063.txt:4`, `:7`). KB `knowledge_base/domains/DM/spec.md:44` / `:53` 为 `Char`.
- 改动: S-SPEC1 (`3a3b724`) writer 第 3 行 "DM/spec.md:44 / :53 … DateTime → Char" (`t2_S-SPEC1.md:39`); reviewer "渲染 p63 两行 Type 列 "Char"; bbox 词 `Char` x=192.98 落 Type 列. xlsx 为 DateTime (xlsx 与 PDF 不一致, 以 PDF 为准)" (`t2_S-SPEC1_review.md:37`).
- 背景: SDTMIG 的 Type 只有 Char / Num, 所有 `--DTC` 变量都是 Char + ISO 8601 格式. 现在全部 spec.md 里 `DateTime` 已 0 处. 旧值来自 `SDTMIG_v3.4.xlsx`, 不是 PDF.

## 第 5 点: model 文件的 6 列定义行

**先说列的含义** (下游定规则前要知道):
- 用户规则 R1 (`t1_user_ack.md`; 转述见 `t2_S-MOD2.md:16`): model/ 的变量表只收 PDF 的 5 列 `# / Variable / Label / Type / Role`, PDF 其余 7 列 (Format、Variable(s) Qualified、Usage Restrictions、Variable C-code、Definition、Notes、Examples) 按 IE 不补.
- 第 6 列 (`Notes` / `Key Notes`) 是 **KB 自写**的, 每张表前有 D6 标注, 例如 `model/02_observation_classes.md:41` "The Key Notes column is KB-written: most cells quote or condense the PDF Definition, Notes, Examples and Usage Restrictions columns …"; `model/03_special_purpose_domains.md:125` 说 SE 表里 TAETORD / EPOCH 两格放的是 PDF 的 Variable C-code. 所以 "6 列行" 是 KB 格式上的特征, 不等于 PDF 有一份 "完整定义".
- 有些表只有 5 列 (如 `model/05` TA 表, `model/06` 6.3 POOLDEF / 6.6 APRELSUB), 这些行不会被 "6 列" 规则选中.

**是不是照 PDF**: 是.
- S-MOD2 (`6f2c38a`, model/02 §3.1): Findings 表从 4 张子表 16 行重建为单表 100 行, 行序 = PDF sv20 p20-32 (`t2_S-MOD2.md:63`); 时间变量 7 张子表补 Role 列 (PDF 全为 "Timing", `t2_S-MOD2.md:80`); bbox 分列逐格 "1059 格 0 DIFF" (`t2_S-MOD2.md:23`); 审计 PASS (`t2_S-MOD2_audit.md:55-56`).
- S-MOD1 (`ed7fd2b`, model/01/03/04): §3.2 / §4 逐页双向全扫 (`t2_S-MOD1.md` 段 2/段 3), model/04 §4 表 (sv20 p50) 新增.
- 旧 KB 里 model/02 时间变量表只有 5 列 (缺 Role), 所以 EPOCH / TAETORD / MIDS 的 6 列行当时只在 model/03; model/04 当时没有 APID 表行. 这就是 rag 的 `_model_defhome` "只出现在一个文件" 规则失效的原因.

**按 PDF 的出处** (sv20 页 = `work/pdf_pages/sv20_pNNNN.txt`):

| 变量 | PDF 中出现的表 (节, 页) | KB 位置 (行 / 列数) | 备注 |
|---|---|---|---|
| TAETORD | §3.1.5 Timing Variables for All Classes, 表 "All Observation Classes—Timing Variables" #4 (p35) | `model/02:325` 6 列 | 通用定义 (所有一般观测类) |
| | §3.2.3.1 Subject Elements 表 #7 (p46) | `model/03:135` 6 列 | 数据集内用法 |
| | §5.1.1.2 Trial Arms 表 #5 (p52) | `model/05:59` 5 列 | 数据集内用法 |
| EPOCH | §3.1.5 同上表 #5 (p35) | `model/02:326` 6 列 | 通用定义 |
| | §3.2.3.1 SE 表 #8 (p46) | `model/03:136` 6 列 | |
| | §5.1.1.2 TA 表 #10 (p53, 表跨页) | `model/05:64` 5 列 | |
| MIDS | §3.1.5 同上表 #41 (p38), Role = Timing | `model/02:387` 6 列 | 通用定义 |
| | §3.2.3.4 Subject Disease Milestones 表 #5 (p49), **Role = Topic** | `model/03:217` 6 列 | 同一变量两处 Role 不同, 均照 PDF |
| APID | §4 Associated Persons Data, 表 "Associated Persons—Additional Identifier Variables" #1 (p50) | `model/04:39` 6 列 | APID 的定义表 |
| | §6.1 RELREC #4 (p64) / §6.2 SUPP-- #4 (p65) / §6.3 POOLDEF #4 (p67) / §6.6 APRELSUB #2 (p69) | `model/06:38` 6 列 / `:76` 6 列 / `:106` 5 列 / `:158` 5 列 | 关系数据集的列 |
| REFID | §6.7 RELSPEC #3 (p69) | `model/06:177` 6 列 | 只有这一处叫 `REFID` |
| (`--REFID`) | §3.1.4 Identifiers for All Classes #11 (p34) | `model/02:301` 6 列 | 带前缀 `--`, 是另一个变量名 (各域 `xxREFID`) |
| SPEC | §6.7 RELSPEC #4 (p69) | `model/06:178` 6 列 | 只有这一处叫 `SPEC` |
| (`--SPEC`) | §3.1.3 Findings 表 #66 (p29) | `model/02:233` 6 列 | 带前缀, 另一个变量名; 旧 KB 的 Findings 子表没有这一行 |

- 对 rag 的说明 (供定规则参考, 由 rag 决定): PDF 自身就让这些变量出现在多张表里. 若要 "一个变量一个定义归属", PDF 的结构是: 一般观测类通用变量在 §3.1.x (model/02), APID 在 §4 (model/04), REFID / SPEC 在 §6.7 (model/06), 其余是数据集内用法. 另外 `REFID` 和 `--REFID`、`SPEC` 和 `--SPEC` 名字不同; 预演报告把 REFID / SPEC 也算进 "多文件", 可能是匹配时去掉了 `--` 前缀, 建议 rag 核一下.
- 与预演报告对照: "EPOCH / TAETORD / MIDS (原属 model/03), APID / REFID / SPEC (原属 model/06)" — 本仓核对: APID 旧 KB 只在 model/06, 现在 model/04 也有 6 列行, 成立; REFID / SPEC 在 HEAD 只有 model/06 是不带前缀的行, 见上.

## 第 6 点: `kb-2026.11.25` → 现在, 移走 / 改名的节

**全量机器清单** (每个文件删掉 / 新增的标题 + 涉及的提交):
```bash
python3 -I .work/10_tier_b_repair/scripts/t4/t4_heading_diff.py kb-2026.11.25 HEAD > .work/10_tier_b_repair/work/t4/kb_heading_diff_kb-2026.11.25_HEAD.txt
# files removed: []; files added: []  ...  files with heading changes 77; removed 85; added 226
```
结果已存 `work/t4/kb_heading_diff_kb-2026.11.25_HEAD.txt`. 文件没有增删; 新增的 226 个标题多数是按 PDF 补的节号标题或 `XX – Description/Overview / Specification / Assumptions` 小节 (会改变 chunk 边界, 即使旧标题还在). 下面是整理后的两张表.

### 表 A: 跨文件的内容移动 (旧位置 → 新位置)

| # | 内容 | 旧位置 | 新位置 | 提交 (批) | 依据 |
|---|---|---|---|---|---|
| A1 | FA 叙述 / §6.4.2 items 2-3 / §6.4.3 Variables Unique to Findings About | `chapters/ch02_fundamentals.md` `## Findings About — Naming Findings About Domains (Reference Material)`、`model/02` `### §6.4.3 Variables Unique to Findings About (Reference Material …)` 与 `### Findings About (Subtype)` | `domains/FA/assumptions.md` (§6.4 各节) | `c8802bf` (B-FA); `6f2c38a` (S-MOD2 删 Findings About 改写副本) | `work/t2_batches/B-FA.writer.jsonl` MOVED ×6; 源处删除, 不留指针 |
| A2 | FA 假设 1-6 | `domains/FA/assumptions.md` 文件顶部 (§6.4 之前) | 同文件 `## FA – Specification` 之后 (PDF p366-367 顺序) | `330e2ed` (S-TUFA) | 同文件, 节归属变 |
| A3 | SE 节 | `model/03` `## Subject Elements (SE)` | `model/03` `### 3.2.3.1 Subject Elements` (在 `## 3.2.3 Subject Summary Domains` 下) | `ed7fd2b` (S-MOD1) | model/03 全部 4 个 Subject 节同理, 见表 B |
| A4 | EC 示例 1-8 | `domains/EC/examples.md` `## Example 1..8` | `domains/EX/examples.md` `## §6.1.3.3 Exposure/Exposure as Collected Examples` 下 (EC 文件只留一行指针) | `5440dc5` (B-EC) | PDF EX/EC 共用 §6.1.3.3 一组示例 |
| A5 | MB 示例的重复副本 | `domains/MB/examples.md` 顶层 `## Example 1..3` (副本) | 删, 保留 `## §6.3.5.7.3 …` 下 `### Example 1..4`; MS 部分换成指向 `domains/MS/examples.md` 的指针 | `c3b7b56` (B-MB), `955e9d5` (B-MS) | D2 去重 |
| A6 | SC 规格句 | `domains/SC/examples.md` `## SC – Specification (p340)` | `domains/SC/assumptions.md` `## SC – Specification` | `52858fc` (B-SC) | D2 去重 |
| A7 | CP / GF / IS 假设文件里的 "示例附录" | `domains/CP/assumptions.md` `### Example 1a/7/8/9 (pNNN)`; `domains/GF/assumptions.md` `## GF – Example 4 (p227)`; `domains/IS/assumptions.md` `### Example 1 / 8–9 / 10 / 11 (…)` | 删 (内容在各自 `examples.md`) | `59d2451` (B-CP), `bdb54fe` (B-GF), `8426871` (S-SPC1) | D2 去重 |
| A8 | ch04 附录里的错放副本 | `chapters/ch04_general_assumptions.md` `### §6.1.3.3 Exposure/Exposure as Collected Examples (p115)`、`### §6.3.5.7 Microbiology Domains — RELSPEC parent/aliquot relationship (p261)` | 删 (内容在 `domains/EX/examples.md`、`domains/MB/…`) | `42fecd3` (S-CH4, O19) | D2 去重 |
| A9 | ch02 里 §1 的副本 | `chapters/ch02_fundamentals.md` `### From §1.2 … / §1.4 … / §1.4.1 …` | 删 (原文在 `chapters/ch01_introduction.md`) | `4f8bde8` (B-ch02) | D2 去重 |
| A10 | 章 / 父节引言 (U3: 放该章第一个域的 assumptions.md 顶部) | 原来缺失或在别处 | `domains/AG/assumptions.md` `## §6.1 …`; `domains/EX/assumptions.md` `## §6.1.3 Exposure Domains`; `domains/AE/assumptions.md` `## §6.2 Models for Events Domains`; `domains/DA/assumptions.md` `## §6.3 Models for Findings Domains`; `domains/NV/assumptions.md` `## §6.3.6 Morphology (MO)`; `domains/DI/assumptions.md` `## §9 Study References` | `acb93ae` (S-INT), `056d8cc` (S-EVT), `0d0e813` (S-FND), `70a7373` (S-HOST), `669405f` (S-SPREL) | `t2_post_user_ack.md` U3 |
| A11 | ch10 的 §9 引言副本 | `chapters/ch10_appendices.md:64-69` | 换成指向 DI 的交叉引用 | `b80d263` (S-CH10) | 主控补注 (`t4_user_decisions.md` 文末) |
| A12 | spec 表脚注 | `domains/CO/assumptions.md:17`、`domains/GF/assumptions.md:15`、`domains/MS/assumptions.md:11`; AE/DS 文件末尾 | 各自 `spec.md` 最后一个变量块后、`## Cross References` 前 | `3a3b724` (S-SPEC1), `8426871` (S-SPC1), `f534395` (S-SPC2), `056d8cc` (S-EVT) | U2/U7 |
| A13 | PP: SUPPPP 表 + 引句 | `domains/PP/examples.md` Example 1 | 同文件 Example 2 (PDF p274 位置), Ex1 原处留交叉引用 | `97e1895` (B-PCPP) | RELOCATE |
| A14 | PP 的 Cross-domain summary 节 | `domains/PP/examples.md` `### Cross-domain summary (Examples 2-4 on pp 281-284)` | 删 (KB 自写摘要) | `97e1895` (B-PCPP) | DELETED_D2 |
| A15 | TA 里重复的 TE 文字 | `domains/TA/…` | 换成指向 TE 的交叉引用 | `a91e198` (B-TE) | D2 |
| A16 | model/01 一块 RELOCATE | `model/01_concepts_and_terms.md` | `model/02_observation_classes.md` | `0dc4f14` (B-model01) | writer D-11 |

另有同文件内的段落移动 (DS / RS / TA / ch02 / ch04 / ch10 / RELREC / MS, 共约 15 处), 不换文件, 但可能换节; 明细见各批 `work/t2_batches/<批>.writer.jsonl` 中 `action` = MOVED / RELOCATE 的行.

### 表 B: 改名 / 改号的标题 (同一文件, 旧 → 新)

| 文件 | 旧标题 | 新标题 | 提交 |
|---|---|---|---|
| `model/01_concepts_and_terms.md` | `# SDTM v2.0 — Chapter 2: Model Concepts and Terms` | `# SDTM v2.0 — Sections 1-2: Introduction; Model Concepts and Terms – Organization of the SDTM` (新增 `## 1 Introduction` ~ `## 1.4 …`、`## 2 …`) | `0dc4f14` (B-model01), `ed7fd2b` |
| | `### Concept Map: Relationships Between SDTM Domains` | `### Concept Map. Relationships Between SDTM Domains` | `ed7fd2b` (S-MOD1) |
| | `### Domain Codes` | 删 (KB 自拟) | `ed7fd2b` |
| `model/02_observation_classes.md` | `# SDTM v2.0 — Chapter 3.1: The General Observation Classes` / `## Overview` | `# SDTM v2.0 — Sections 3-3.1: …` / `## 3 Study Subject Data` + `## 3.1 The General Observation Classes` | `0dc4f14`, `6f2c38a` |
| | `### Findings About (Subtype)` | `### 3.1.3.1 Findings About Events or Interventions` | `6f2c38a` (S-MOD2) |
| `model/03_special_purpose_domains.md` | `## Demographics (DM)` / `## Comments (CO)` / `## Subject Elements (SE)` / `## Subject Repro Stages` / `## Subject Visits (SV)` / `## Subject Disease Milestones (SM)` | `## 3.2.1 Demographics` / `## 3.2.2 Comments` / `## 3.2.3 Subject Summary Domains` 下 `### 3.2.3.1 Subject Elements` / `### 3.2.3.2 Subject Repro Stages` / `### 3.2.3.3 Subject Visits` / `### 3.2.3.4 Subject Disease Milestones`; 另加 `### 3.2 Special-purpose Domains` | `ed7fd2b` (S-MOD1) |
| `model/04_associated_persons.md` | — | 新增 `### 4 Associated Persons Data` | `ed7fd2b` |
| `model/05_study_level_data.md` | `## Overview` / `## 5.1 Trial Design Model` / `### Trial Elements (TE)` / `### Trial Arms (TA)` / `### Trial Sets (TX)` / `### Trial Reproductive Stages (TT)` / `### Trial Reproductive Paths (TP)` / `### Trial Visits (TV)` / `### Trial Disease Assessments (TD)` / `### Trial Disease Milestones (TM)` / `### Trial Inclusion/Exclusion Criteria (TI)` / `### Trial Summary (TS)` / `### Challenge Agent Characterization (AC)` / `### Device Identifiers (DI)` / `### Non-host Organism Identifiers (OI)` | `## 5 Study-level Data` / `## 5.1 The Trial Design Model` / `### 5.1.1 Trial Arms and Trial Elements` + `### 5.1.1.1 Trial Elements (TE)` / `### 5.1.1.2 Trial Arms (TA)` / `### 5.1.2 Trial Sets (TX)` / `### 5.1.3 …` + `### 5.1.3.1 Trial Repro Stages (TT)` / `### 5.1.3.2 Trial Repro Paths (TP)` / `### 5.1.4 Trial Planned Data Collection` + `### 5.1.4.1 Trial Visits (TV)` / `### 5.1.4.2 …(TD)` / `### 5.1.4.3 …(TM)` / `### 5.1.5 …(TI)` / `### 5.1.6 Trial Summary Information (TS)` / `### 5.1.7 …(AC)` / `### 5.2.1 Device Identifiers Dataset (DI)` / `### 5.2.2 Non-host Organism Identifiers Dataset (OI)` | `a197773` (S-MOD3) |
| `model/06_relationship_datasets.md` | 按 PDF 重写 (6.1-6.7) | 见机器清单 | `cbc6b75` (B-model06) |
| `chapters/ch02_fundamentals.md` | `### Must NEVER be used in DM domain (SEND nonclinical only):` / `### Use with extreme caution (not fully evaluated …):` / `### May be used when appropriate:` | `… for human clinical trials (SEND nonclinical only):` / `(not evaluated for use in human clinical trials):` / `### May be used in human clinical trials when appropriate:` | `4f8bde8` (B-ch02) |
| | `### Points to Consider` | 删 | `4f8bde8` |
| `chapters/ch04_general_assumptions.md` | `### 4.2.1 Variable-Naming Conventions` + `#### 4.2.1.1-4.2.1.3 …` (KB 自拟子节) | `### 4.2.1 Variable-naming Conventions` (子节删) | `42fecd3` (S-CH4) |
| | `#### 4.2.7.1 "Specify" Values for Non-Result Qualifier Variables` | `… Non-result …` | `42fecd3` |
| | `### 4.3.5 … (MedDRA and WHODrug)` + `#### MedDRA Coding (Events)` / `#### WHODrug Coding (Interventions)` | `### 4.3.5 Storing Controlled Terminology for Synonym Qualifier Variables` (子节删) | `42fecd3` |
| | `#### Disease Milestone Naming (MIDS)` | `#### Disease Milestone Naming` + `#### Disease Milestone Name (MIDS)` | `42fecd3` |
| | `### 4.5.1 Original and Standardized Results` | `### 4.5.1 Original and Standardized Results of Findings and Tests Not Done` + `#### 4.5.1.1 Original and Standardized Results` | `42fecd3` |
| `chapters/ch08_relationships.md` | `## 8.1 … Using --GRPID` / `## 8.3 Relating Datasets Using RELREC` / `### 8.4.3 Examples` / `## 8.6 Where Data Belong` | `## 8.1 … Using the --GRPID Variable` / `## 8.3 Relating Datasets` / `### 8.4.3 SUPP-- Examples` / `## 8.6 How to Determine Where Data Belong in SDTM-Compliant Data Tabulations` | `718c278` (B-ch08), `fe3f59c` (S-CH8) |
| | `### Key Rules`; RELSUB / RELSPEC 下的 `### Specification` / `### Assumptions` / `### Example` | 删; `### RELSUB — Description/Overview / Specification / Assumptions / Examples`、`### RELSPEC — Specification / Assumptions / Examples` | 同上 |
| `chapters/ch10_appendices.md` | `### Key Points` / `### Rules for Using Fragments` / `### Decommissioning of MO (Morphology)` | 前两个删 (KB 自拟); 第三个 → `### A note on the decommissioning of MO` | `b80d263` (S-CH10) |
| `chapters/ch01_introduction.md` | `### Related Implementation Guides` | 删 (§1 按 PDF p7-10 逐字重写) | `78c859f` (B-ch01) |
| `domains/PP/examples.md` | `## §6.3.5.9.3 RELREC Method Quick Reference (PP-side view)` | `## RELREC Method Quick Reference (PP-side view)` (去掉了借用的节号; 本节是 KB 自写, 见 `t4_user_decisions.md` A5-10) | `f534395` (S-SPC2) |
| | `### Method D — … (pp 278-280)` | `… (pp 278-279)` | `97e1895` |
| `domains/TA/assumptions.md` | `## TA-Specific Assumptions` | `## TA – Assumptions`; 另加 `### §7.2.1 Trial Arms (TA) – Specification` | `d500b1b` (S-TDM) |
| 多数 `domains/*/assumptions.md` | (无对应 H2) | 新增 PDF 小节标题 `## XX – Description/Overview`、`## XX – Specification`、`## XX – Assumptions` (CP/EC/FA/IS/MB/PC/PP/SC/TA 等) | 各扫描批 (S-SPC1/S-SPC2/S-INT/S-EVT/S-FND/S-TUFA/S-SPREL) |

- 与预演报告对照: 三处 (`c8802bf` FAOBJ 叙述 / `ed7fd2b` SE 标题 / `cbc6b75` model/06 重写) 都成立, 分别对应 A1 / A3 + 表 B model/03 行 / 表 B model/06 行. q117 的 "三点改为省略号" 属 S-TYPO (U1) 排版, 不是节变动, 本表不列.
- 这份清单可直接用于发版说明 (T4.3 时以 tag 当天的 HEAD 重跑一次脚本, 数字以重跑为准).

## 第 7 点: 域示例文件的标题格式

有变, 涉及 7 个文件 (下表由 `git show kb-2026.11.25:<f>` 与现文件的 `##`-`####` 标题按数字归一后比较得到):

| 文件 | 旧 | 新 | 提交 |
|---|---|---|---|
| `domains/PC/examples.md` | 文件首段 → `## §6.3.5.9.3 Relating PP Records to PC Records — Worked Examples` → `### Example 1` (这里的 Example 1 其实是 PC 自己的例, PDF p269-270) … | `## PC – Examples` (无节号, PDF p269 原标题) → `### Example 1` (PC 自己的例); 之后 `## §6.3.5.9.3 …` → `### Example 1..4` + `#### Method A-D` (合并例) | `97e1895` (B-PCPP), `f534395` (S-SPC2) |
| `domains/EC/examples.md` | `## Example 1/2/3/5/6/7/8` | 无示例标题, 只留指向 EX 的指针行 | `5440dc5` (B-EC) |
| `domains/EX/examples.md` | `## Example 1..8` | 先 `## §6.1.3.3 Exposure/Exposure as Collected Examples`, 再 `## Example 1..8` | `acb93ae` (S-INT) |
| `domains/MB/examples.md` | 顶层 `## Example 1..3` (副本) + `## §6.3.5.7.3 …` + `### Example 1..4` | 只剩 `## §6.3.5.7.3 …` + `### Example 1..4` | `c3b7b56`, `955e9d5` |
| `domains/TU/examples.md` | `## Example 1..3` | 先 `## §6.3.12.3 Tumor Identification/Tumor Results Examples`, 再 `## Example 1..3` | `9478eb7` (B-TU) |
| `domains/PP/examples.md` | `## §6.3.5.9.3 RELREC Method Quick Reference (PP-side view)` | `## RELREC Method Quick Reference (PP-side view)`; `### Cross-domain summary …` 删 | `97e1895`, `f534395` |
| `domains/SC/examples.md` | 有 `## SC – Specification (p340)` | 删 (移到 assumptions) | `52858fc` |

另: `domains/TV/examples.md` 粗体例题标签 `**Example …**` 0 → 1 处. 其余 `domains/*/examples.md` 的示例标题格式没有变 (仍是 `## Example N`).

- **PC 拿不到节号, 很可能就在这里**: 旧 KB 里 PC 的 Example 1 挂在带节号的 `## §6.3.5.9.3 …` 下, 所以 chunk 能拿到 6.3.5.9.3 (其实节号挂错了, PC 自己的例属于 §6.3.5.9.1 PC). 现在它在 `## PC – Examples` 下, 这个标题照 PDF 没有节号. SDTMIG 各域的 "XX – Examples" 在 PDF 里本来就不编号, 节号要从所属域节 (§6.3.5.9.1) 继承. 这是 rag chunker 的映射问题, 不是 KB 错.
- 其他域的 `examples.md` 一直没有 `## XX – Examples` 这一层 (直接 `## Example N`), PC 现在是少数; 如 rag 需要统一, 可按 "文件所在域 → 域节号" 取节号. KB 冻结期不改.

## 核对中发现的 KB 观察项 (不修, 已记入 `t4_user_decisions.md` §00 U-10)
- ⑥ `model/06_relationship_datasets.md:177-178` RELSPEC 表 REFID / SPEC 的 Notes 列: 旧 KB 有 `C82531` / `C70713` (PDF 的 Variable C-code), B-model06 重写后为空; 同类的 `model/03` SE 表 TAETORD / EPOCH 仍在 Notes 列放 C-code (`model/03:125` D6 说明). Notes 列是 KB 自写列, R1 不要求补 PDF 的 C-code 列, 所以不算错, 但两处做法不一致.
- ⑦ PC 示例层级与其他域不一致 (见第 7 点), 属格式口径问题.

## 复跑
```bash
cd /Volumes/DevSSD/Project/sdtm-pedia
python3 -I .work/10_tier_b_repair/scripts/t4/t4_heading_diff.py kb-2026.11.25 HEAD | tail -1     # files with heading changes 77; removed 85; added 226
grep -c "^- \*\*Controlled Terms:\*\* \*$" knowledge_base/domains/*/spec.md | awk -F: '{s+=$2} END {print s}'   # 129
grep -l "asterisk (\*) indicates that the variable may be subject" knowledge_base/domains/*/spec.md | wc -l    # 62
grep -rn "DateTime" knowledge_base/domains/*/spec.md | wc -l                                                  # 0
git diff --stat 00a2e93..HEAD -- knowledge_base | wc -l                                                       # 0
```

---

## T4 解冻轮 (本地 `a59c2d3`, 2026-11-27) 给 sdtm-rag 的增量说明

> 背景: T4 用户裁定 (委托代裁, `evidence/checkpoints/t4_user_decisions.md` §000) 需要改 KB 的部分在这一轮一次改完; KB 只变这一次, rag 需在新指纹上重跑入库预演. 未 push、未打 `kb-*` tag.
> 不变的接口: spec.md 的 `- **Controlled Terms:**` 单元格 0 改动 (本文件前面的格式约定继续有效); model 文件变量表 `#` 编号 0 改动 (auditor 逐行核: model/05 110 行、model/06 47 行与解冻前相同). U-10⑥ (model/06 RELSPEC REFID/SPEC 的 Notes 列为空、model/03 SE 表 TAETORD/EPOCH Notes 放 C-code) **本次不处理**, 将来改之前先通知 rag.

### 1. 定义出处映射 (`_model_defhome`) 的实际影响
- 原因: A5-3 给 `model/05` TS 表 (原 5 列) 加第 6 列 `Usage Restrictions`, TSVALCD / TSVCDREF / TSVCDVER 三行填 PDF 的 "Not in nonclinical trials" (sv20 p59-60), 与 TT/TP 表同一承载方式; 同时 A5-2 把 TT/TP 表第 6 列列名 `Notes` 改为 `Usage Restrictions` (格内容不变).
- 实算 (rag 只读脚本 `defhome_rules.py`, 本仓未写 rag):
```bash
# 解冻前 (= 00a2e93 内容) vs 解冻后
/Volumes/DevSSD/Project/sdtm-rag/.venv/bin/python -I /Volumes/DevSSD/Project/sdtm-rag/.work/10_split_and_public/evidence/probes/defhome_rules.py <git archive 3a24a1c knowledge_base 展开> knowledge_base
# R0: old 64 new 67 / R4: old 72 new 75 / R4n: old 107 new 116      → 输出全文 work/t4/defhome_pre_vs_thaw.txt
# kb-2026.11.25 vs 解冻后: R0 59→67 / R4 62→75 / R4n 98→116        → work/t4/defhome_tag_vs_thaw.txt
```
- **R4 相对解冻前只新增 `TSVALCD` / `TSVCDREF` / `TSVCDVER` → model/05, 删除 0、改动 0** (KB reviewer 与 auditor 各自用集合差独立核过). A5-2 (列名) 与 A5-4 (Role 列括注统一, 如 QLABEL "Synonym Qualifier (QNAM)") 没有让别的变量进出映射.
- **R4n 提醒**: R4n (不要求第 6 格非空) 下, TS 表另 6 行 (TSSEQ / TSGRPID / TSPARMCD / TSPARM / TSVAL / TSVALNF) 因升为 6 格也被计入; rag 现用的 R4 不受影响, **请勿改用 R4n**.
- TT/TP 表 DOMAIN 行第 6 格仍是 `"TT"` / `"TP"` (现挂在 `Usage Restrictions` 列下, 表上 KB note 写明是例外); 本次不清空, 因为清空会改变 rag 读到的内容 (记后续).

### 2. 标题 / 节变动 (解冻轮本身)
复跑: `python3 -I .work/10_tier_b_repair/scripts/t4/t4_heading_diff.py 00a2e93 HEAD` → `work/t4/kb_heading_diff_00a2e93_HEAD.txt` (8 个文件; 删 28 / 增 22). 相对 rag 现钉版本: `t4_heading_diff.py kb-2026.11.25 HEAD` → `work/t4/kb_heading_diff_kb-2026.11.25_HEAD.txt` (文件增删 0; 79 个文件标题有变, 删 104 / 增 239; 替代本文件 §6 的 77 / 85 / 226).

| 文件 | 变动 | 裁定 |
|---|---|---|
| `domains/FA/assumptions.md` | `## §6.4.4 FA – Description/Overview` 拆成 `## §6.4.4 Findings About Events or Interventions (FA)` + `## FA – Description/Overview` (PDF p364 两行标题) | A5-11 |
| `domains/MB/examples.md` | `## §6.3.5.7.3 Microbiology Specimen and Microbiology Susceptibility Examples` → `…Specimen/Microbiology Susceptibility Examples` | A5-11 |
| `domains/PP/examples.md` | **删除整节** `## RELREC Method Quick Reference (PP-side view)` 及 5 个 `###` 子节 (KB 自写摘要), 换成一行交叉引用到 `PC/examples.md` 的 worked examples (内容在 PC/examples.md Example 1 Method A-D); PP 文件标题 11 → 5 | A5-10 |
| `domains/SS/examples.md` | `##### Example 1` → `## Example 1` | A5-11 |
| `domains/TA/assumptions.md` | `## Trial Design Model Overview (§7.1)` → `## §7.1 Introduction to Trial Design Model Datasets`; `## Trial Arms and Trial Elements (§7.2)` → `## §7.2 Experimental Design (TA and TE)` | A5-11 |
| `domains/TI/assumptions.md` | `## §7.4 Trial Eligibility and Summary (TI, TS) — Introduction` → `## §7.4 Trial Eligibility and Summary (TI and TS)` | A5-9 |
| `model/05_study_level_data.md` | 5.1.1.1-2 / 5.1.3.1-2 / 5.1.4.1-3 七个标题 `###` → `####` (文字不变, "(XX)" 域代码后缀保留) | A5-1 |
| `model/06_relationship_datasets.md` | `## Overview` → `## 6 Datasets for Representing Relationships`; 6.1-6.7 改 PDF 原标题 (多数加 "Dataset", 6.6 → "Associated Persons Relationships (APRELSUB)"); 删 `### RELTYPE Combinations` (KB 自写表, 换成指向 ch08 §8.3.1 的交叉引用) | A5-5 / A5-8 |

- 所有改 / 删标题在 knowledge_base / web/src / tools / docs 中入站链接 0 (auditor 按 slug 复核).
- 非标题但影响 chunk 文本的: CE/examples.md:39 自拟粗体 CRF 标题改为 `**CRF**` (U-10②); CRF 选项符号 CE 39 + ch04 19 处 `( )`/`[ ]` → ○ / □ (U-9a, 按 PDF 渲染外观; ML 的 `[X]`/`[ ]` 不变); 5 条 `> KB note (not in SDTMIG):` 改为 `> Note:` (EX/examples:5、MS/examples:3、PC/examples:3、PP/examples:3、RELREC/assumptions:5; 只说明来源/位置的 note, A5-14). 其余 165 条 KB note 前缀不变 (C-code note 59 条不变). 值改动 21 行 (U-7) + en dash 2 处 (A6), 清单 `evidence/checkpoints/t4_thaw_W1.md`.
