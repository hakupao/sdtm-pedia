# T4.1 第二轮补检 — XDOC 层结果 (R1-R27)

- 审查者: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:41:17Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` (背景 / 判定口径 / 输出) + `subagent_prompts/t4/t4_supp_round2_v1.0.md` XDOC 节 (冲突以后者为准)
- 看过的渲染页: SDTMIG v3.4 p60, p79, p80, p114, p115, p116, p195, p196, p364, p441; SDTM v2.0 p4, p5, p9
- 用过的命令 (仓库根目录下执行):
  - `sed -n` / `cat` 读 `.work/10_tier_b_repair/work/pdf_pages/ig34_p0060.txt` `ig34_p0079-0080` `ig34_p0114-0116` `ig34_p0195-0196` `ig34_p0364` `ig34_p0440-0442` `sv20_p0004/0005/0009.txt`
  - `grep -rn "provide specific, standardized structures" knowledge_base` ; `grep -rn "6\.3\.5\.1\|Generic Specimen" knowledge_base` ; `grep -rn "Identifiers for devices\|Identifiers for non-host organisms" knowledge_base`
  - `grep -n "^#" knowledge_base/domains/{SE,EX,FA,DI,OI}/*.md knowledge_base/model/01_concepts_and_terms.md`
  - `grep -rn "^#.*\(Subject Elements\|Device Identifiers\|Non-host Organism Identifiers\)" knowledge_base/chapters knowledge_base/domains` (不截断)
  - `grep -n "O60\|域标题\|自拟标题" .work/10_tier_b_repair/evidence/checkpoints/t4_user_decisions.md .work/10_tier_b_repair/work/out_of_scope_findings.md` (查有没有登记过 "域文件标题不带节号" 的豁免: **没有**)
  - 规模统计: `cd knowledge_base/domains; for d in */; do d=${d%/}; grep -qE "^#+ §?[0-9]+(\.[0-9]+)+ .*\($d\)" $d/*.md || echo $d; done | wc -l` → 57 (共 64 个域目录)
- 总说明: 包里的 KB 指针都不采信, 下表 KB 依据都是在原子**自己所属文档**的 KB 文件里重新找到的行 (IG → `chapters/` / `domains/`; v2.0 → `model/`).

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| R1 | `ig34_p0060_a003` | XDOC | EQUIVALENT | HOLDS | `ig34_p0060.txt:2-3`, 渲染 p60; `knowledge_base/domains/CO/assumptions.md:5` (在 `:3 ## §5 Models for Special-purpose Domains` 下) | 实为逐字. §5 章引言放在第一个域 (CO) 文件里, 位置符合 `subagent_prompts/t2_dispatch_notes.md:41` (有正文的章引言由首域承载) |
| R2 | `ig34_p0079_a001` | XDOC | EQUIVALENT | NOT_HOLD | `ig34_p0079.txt:10`, 渲染 p79 (`5.3 Subject Elements (SE)`); `knowledge_base/domains/SE/spec.md:1` `# SE — Subject Elements` | 标题文字在, **节号 5.3 不在**: SE 三个文件里都没有带 5.3 的标题 (`assumptions.md` 只有 `## SE – Description/Overview` 等小节). round2 brief 要求 "节号与标题文字一致"; 没查到 "域文件标题不带节号" 的登记豁免. 不是 XDOC 误配 (自己文档有对应节和正文), 是标题缺节号; 属同类系统现象 (见样本外发现) |
| R3 | `ig34_p0079_a016` | XDOC | EQUIVALENT | HOLDS | `ig34_p0079.txt:32`, 渲染 p79; `knowledge_base/domains/SE/spec.md:14-21` | 逐格: DOMAIN / Domain Abbreviation / Char / SE / Identifier / Two-character abbreviation for the domain. / Req 全一致 |
| R4 | `ig34_p0080_a003` | XDOC | EQUIVALENT | HOLDS | `ig34_p0080.txt:10-11`, 渲染 p80; `knowledge_base/domains/SE/spec.md:59-66` | 逐格一致 (Num / 空 CT / Timing / "…planned order of the element within…" / Perm). 原子抽错: 写成 "elements"、漏 Core 列; KB 与 PDF 一致 (单数 element, Perm) |
| R5 | `ig34_p0080_a009` | XDOC | EQUIVALENT | HOLDS | `ig34_p0080.txt:22-23`, 渲染 p80; `knowledge_base/domains/SE/spec.md:113-120` | 逐格一致 (Char / 空 CT / Synonym Qualifier / 注释全文 / Perm) |
| R6 | `ig34_p0114_a014` | XDOC | EQUIVALENT | HOLDS | `ig34_p0114.txt:17`, 渲染 p114; `knowledge_base/domains/EX/examples.md:173` | `**Subject ABC5001**`, 在 `## Example 5` (:167) 下, 节 `## §6.1.3.3` (:3) 内; PDF 为粗体小标签, 对应 |
| R7 | `ig34_p0114_a018` | XDOC | EQUIVALENT | HOLDS | `ig34_p0114.txt:22`, 渲染 p114; `knowledge_base/domains/EX/examples.md:180` | 同上 |
| R8 | `ig34_p0114_a022` | XDOC | EQUIVALENT | HOLDS | `ig34_p0114.txt:27`, 渲染 p114; `knowledge_base/domains/EX/examples.md:187` | 同上 |
| R9 | `ig34_p0115_a029` | XDOC | EQUIVALENT | HOLDS | `ig34_p0115.txt:33`, 渲染 p115; `knowledge_base/domains/EX/examples.md:243` | 在 `## Example 6` (:235) 下 |
| R10 | `ig34_p0116_a001` | XDOC | EQUIVALENT | HOLDS | `ig34_p0116.txt:1`, 渲染 p116; `knowledge_base/domains/EX/examples.md:252` | 同上 |
| R11 | `ig34_p0195_a020` | XDOC | EQUIVALENT | HOLDS | `ig34_p0195.txt:35-36`, 渲染 p195; `knowledge_base/domains/LB/assumptions.md:33` | 逐格一致 (含 CT 列 `*`). 位置: LB 文件里自己的 `## §6.3.5.1 Generic Specimen-based Lab Findings Domain Specification` (:7) 下 (§6.3.5 父节由首个相关域文件承载, 参照 `t2_dispatch_notes.md:41`) |
| R12 | `ig34_p0195_a022` | XDOC | EQUIVALENT | HOLDS | `ig34_p0195.txt:40-42`, 渲染 p195; `knowledge_base/domains/LB/assumptions.md:35` | 逐格一致 (CT 空, Exp, 注释两句全文); 位置同 R11 |
| R13 | `ig34_p0195_a024` | XDOC | EQUIVALENT | HOLDS | `ig34_p0195.txt:45-46`, 渲染 p195; `knowledge_base/domains/LB/assumptions.md:37` | 逐格一致 (CT `*`, Perm); 位置同 R11 |
| R14 | `ig34_p0196_a001` | XDOC | EQUIVALENT | HOLDS | `ig34_p0196.txt:3-4`, 渲染 p196; `knowledge_base/domains/LB/assumptions.md:38` | 逐格一致 (CT `*`, "NOT DONE", Perm); 位置同 R11 |
| R15 | `ig34_p0196_a002` | XDOC | EQUIVALENT | HOLDS | `ig34_p0196.txt:5-6`, 渲染 p196; `knowledge_base/domains/LB/assumptions.md:39` | 逐格一致; 位置同 R11 |
| R16 | `ig34_p0196_a009` | XDOC | EQUIVALENT | HOLDS | `ig34_p0196.txt:19`, 渲染 p196; `knowledge_base/domains/LB/assumptions.md:46` | 逐格一致; 位置同 R11 |
| R17 | `ig34_p0196_a010` | XDOC | EQUIVALENT | HOLDS | `ig34_p0196.txt:20`, 渲染 p196; `knowledge_base/domains/LB/assumptions.md:47` | 逐格一致; 位置同 R11 |
| R18 | `ig34_p0364_a014` | XDOC | EQUIVALENT | HOLDS | `ig34_p0364.txt:24`, 渲染 p364; `knowledge_base/domains/FA/assumptions.md:85` | 在 `## §6.4.3 Variables Unique to Findings About` (:77) 的 FATESTCD/FATEST 表里, 逐格一致 |
| R19 | `ig34_p0364_a015` | XDOC | EQUIVALENT | HOLDS | `ig34_p0364.txt:25`, 渲染 p364; `knowledge_base/domains/FA/assumptions.md:86` | 同上 |
| R20 | `ig34_p0364_a016` | XDOC | EQUIVALENT | HOLDS | `ig34_p0364.txt:26`, 渲染 p364; `knowledge_base/domains/FA/assumptions.md:87` | 同上 |
| R21 | `ig34_p0441_a004` | XDOC | EQUIVALENT | HOLDS | `ig34_p0441.txt:4`, 渲染 p441; `knowledge_base/domains/DI/assumptions.md:7` | 在 `## §9 Study References` (:3) 下, 逐字; §9 引言放首域 DI 文件, 符合 `t2_dispatch_notes.md:41` |
| R22 | `ig34_p0441_a005` | XDOC | EQUIVALENT | HOLDS | `ig34_p0441.txt:5`, 渲染 p441; `knowledge_base/domains/DI/assumptions.md:8` | 同上 |
| R23 | `ig34_p0441_a006` | XDOC | EQUIVALENT | NOT_HOLD | `ig34_p0441.txt:7`, 渲染 p441 (`9.1 Device Identifiers`, 下面直接是正文, 没有 "DI – Description/Overview" 小标题); `knowledge_base/domains/DI/assumptions.md:10` `## DI – Description/Overview (§9.1)` | 节号 §9.1 在, **标题文字不一致**: KB 用的是自拟的 "DI – Description/Overview", 没有 "Device Identifiers"; `chapters/` `domains/` 里没有任何以 Device Identifiers 为标题的行. 没有登记豁免. 正文 (:12) 在, 不是 XDOC 误配 |
| R24 | `ig34_p0442_a001` | XDOC | EQUIVALENT | NOT_HOLD | 原子页号写的是 442, 实际在 `ig34_p0441.txt:14`, 渲染 p441 (`9.2 Non-host Organism Identifiers (OI)`); `knowledge_base/domains/OI/spec.md:1` `# OI — Non-host Organism Identifiers` | 和 R2 一样: 标题文字在, **节号 9.2 不在** (OI 三个文件里都没有 9.2 / §9.2). 没有登记豁免. 自己文档里有对应节和正文, 不是 XDOC 误配 |
| R25 | `sv20_p0004_a002` | XDOC | EQUIVALENT | HOLDS | `sv20_p0004.txt:7`, 渲染 v2.0 p4; `knowledge_base/model/01_concepts_and_terms.md:7` `## 1.1 Purpose` | 节号与标题文字一致 (包里给的 IG `ch01` 指针不采信) |
| R26 | `sv20_p0005_a001` | XDOC | EQUIVALENT | HOLDS | `sv20_p0005.txt:5`, 渲染 v2.0 p5; `knowledge_base/model/01_concepts_and_terms.md:30` `## 1.3 Relationship to Prior CDISC Models` | 一致. 包指针指的是 IG 的 "…Prior CDISC Documents" (另一份文档), 不采信 |
| R27 | `sv20_p0009_a001` | XDOC | EQUIVALENT | HOLDS | `sv20_p0009.txt:5`, 渲染 v2.0 p9; `knowledge_base/model/01_concepts_and_terms.md:154` `## 2.1 Model Concepts and Terms – Variables` | 一致 |

## 计数

| 判定 | 条数 | 编号 |
|---|---|---|
| HOLDS | 24 | R1, R3-R22, R25-R27 |
| HOLDS_AS_EQUIV | 0 | (27 条终态都是 EQUIVALENT, 这一类不适用) |
| NOT_HOLD_R1 | 0 | — |
| NOT_HOLD_XDOC | 0 | — |
| NOT_HOLD | 3 | R2, R23, R24 |
| UNVERIFIABLE | 0 | — |

- 按原子所属文档分: IG 24 条 (HOLDS 21 / NOT_HOLD 3); v2.0 3 条 (HOLDS 3).
- 3 条 NOT_HOLD 都是**标题类**, 原因是 KB 标题与 PDF 不完全一致 (缺节号或标题文字是自拟的). 对应节的正文都在自己文档里, 不是跨文档误配, 也不是正文内容错.
- 判 NOT_HOLD 的依据是 round2 brief 对标题类的写死口径 ("节号与标题文字一致"; 登记过的豁免只有追加域代码后缀). 台账里同类旧 EQUIVALENT 的 discrepancy 字段写过 "heading without PDF section number", 但那正是本层被审的旧标签, 不能当豁免. 如果主控 / 主人认定 "域文件 H1 `# XX — 域名` 不带节号" 是可接受的 KB 惯例, 那 R2 和 R24 可以复议为 HOLDS; R23 的标题文字是自拟的, 复议时要单独看.

## 样本外发现 (不计入判定, 不修)

1. **域文件标题普遍不带 PDF 节号.** 64 个域目录里有 57 个没有任何 `N.N… 域名 (XX)` 形式的编号标题 (命令见文件头), 只有 H1 `# XX — 域名`. PDF 每个域节都有编号标题 (例: p79 `5.3 Subject Elements (SE)`, p441 `9.2 … (OI)`). 所以 R2 / R24 这类 "标题缺节号" 是系统现象, 同类 IG 域节标题原子 (台账里约几十条标 EQUIVALENT) 按本层口径都会判 NOT_HOLD. 建议主控按类处理 (统一认定为惯例并登记, 或统一改标), 不要逐条处理.
2. `knowledge_base/domains/DI/assumptions.md:10` `## DI – Description/Overview (§9.1)` 是 KB 自拟标题, PDF p441 §9.1 下没有 "DI – Description/Overview" 小标题. 和 O60 / A5-11 (KB 自拟标题 vs PDF 原标题) 是同一类, 但 O60 / A5-11 的清单里没有点名这一条.
3. 原子抽取偏差 (不影响判定): `ig34_p0080_a003` 原子写成 "elements", 而且漏了 Core 列; `ig34_p0442_a001` 的页号偏了 (实际在 p441).
