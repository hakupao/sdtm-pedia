# T2 B-SC auditor (Rule A) — attempt 1

> agent: oh-my-claudecode:verifier (opus); 与 writer (executor) / reviewer (code-reviewer) 不同 subagent_type。先独立判, 后对照 writer/reviewer 报告。

## 抽样
- 命令: `t2_auditor_v1.0.md` 抽样脚本, 改动: files = kb_files ∪ {SC/assumptions.md} (本批实际改动), pages = 339-342 (SC 完整节页范围); 结果再去掉 parent_section 为 §6.3.9 (p339 上部 RS) 与 SS (p342 下部) 的原子, 用 seed 重抽。
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SC_auditor/sample2.json`
- seed = 20261126; C = 0; P = 11; N = 10 (C 0 + P−C 10)。P 只有 11 条, 未抽中的 ig34_p0342_a001 也一并核过 (P 全覆盖)。

## 样本判定
| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0341_a024 | p341 下: Ex2 引言 "only infants were study subjects…APSC…APID, RSUBJID, SREL" | SC/examples.md:24 | 否 | 是 | 是 (Example 2) | 逐字 |
| 2 | ig34_p0342_a009 | p342 中: Ex3 引言 "multi-year study…collected annually" | SC/examples.md:40 | 否 | 是 | 是 (Example 3) | 逐字 |
| 3 | ig34_p0339_a023 | p339 下: SC Description "A findings domain that contains subject-related data…" | SC/assumptions.md:5 | 否 | 是 | 是 (Description/Overview) | 逐字 |
| 4 | ig34_p0340_a002 | p340 上: spec 首句 "sc.xpt, Subject Characteristics — Findings. One record per…" | SC/assumptions.md:9 | 否 | 是 | 是 (新增 SC – Specification, 位于 Description 与 Assumptions 间, CM 先例) | 逐字; 标题 U+2013、句中 U+2014 码位与 PDF 一致 |
| 5 | ig34_p0341_a012 | p341 中: Ex1 引言 "data collected once per subject…national origin and marital status" | SC/examples.md:7 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0341_a005 | p341 上: spec 表脚注 "¹In this column, an asterisk (*)…" | — (SC 三文件均无) | 范围外 | — | — | spec 表脚注属 spec.md, 不在本批 kb_files/授权; 全库共性已登记 O15/O24/O26 (B-SV 先例同判范围外), 不计本批 |
| 7 | ig34_p0341_a009 | p341 中: Assumption 3 限定词列表 (--MODIFY…--SEV, 22 项) | SC/assumptions.md:17 | 否 | 是 | 是 | 逐字 (PDF "--\nXFN" 折行) |
| 8 | ig34_p0342_a002 | p342 上: "Gestational age is often expressed…converted to days" | SC/examples.md:28 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0341_a008 | p341 中: Assumption 2 SC Codetable + CT URL | SC/assumptions.md:15 | 否 | 是 | 是 | 逐字, URL 完整 |
| 10 | ig34_p0341_a007 | p341 上: Assumption 1 结构/人口学/示例 | SC/assumptions.md:13 | 否 | 是 | 是 | 逐字 |
| (+) | ig34_p0342_a001 | p342 上: Ex2 第二段 "Although there is a test for gestational age…METHOD codelist" | SC/examples.md:26 | 否 | 是 | 是 | 非样本, 全覆盖补核, 逐字 |

- 机械匹配 (空白规范化子串): 11 条中 10 条精确命中上表位置; a005 无命中 (范围外, 见 #6)。
- **独有丢失 0 (范围外 1: spec 脚注 → O15/O24/O26); 忠实度错误 0。**

## 额外核查
- **p342 Ex2 sc.xpt 对渲染图** (250 dpi 裁切 `y-342.png`): 逐格核 3 行 × 17 列 (含表头) 全部; 列举抽核 ≥5 格: 表头 SCORRESU (KB:32 已由 SCORESU 改正, 与 spec.md:104 一致) ✔; Row 1 SCMETHOD "MENSTRUAL HISTORY" ✔; Row 2 VISITNUM 11 / SCDY 226 ✔; Row 3 VISITNUM 13.1 / SCMETHOD BALLARD / SCDY 297 ✔; Row 1 SCDTC 2017-03-02 (PDF 折行 "2017-/03-02") ✔; 全行 STUDYID ABC-123、USUBJID 101、SCCAT "PREGNANCY-RELATED FINDINGS"、SCORRES/SCSTRESC/SCSTRESN 100/135/265、DAYS ✔。Rows 2-3 SCDTC PDF 渲染为 "20-17-04-01"/"20-17-06-10" (年份内多连字符), KB 2017-04-01/2017-06-10 → T-1 PDF_TYPO, 同意 (ISO 8601 + Row 1 格式可由 PDF 自身定)。Ex1/Ex3 两表对 p341/p342 渲染行列一致。
- **交叉引用锚点**: examples.md:3 `assumptions.md#sc--specification` → assumptions.md:7 `## SC – Specification` (U+2013), GitHub slug = 小写、去标点、空格→连字符 = `sc--specification` ✔ 有效。被替换的旧 examples.md:3-5 内容 (KB 自置标题 + spec 首句) 在 assumptions.md:9 有逐字保留副本, D2 去重无信息丢失; 交叉引用为纯导航, 不需 D6 标注。
- **主控勘误算术**: `python3 -c` 计算: 2017-04-01 + 71 天 = 2017-06-11 (原 writer 依据 "+71 → 2017-06-10" 确为错), +70 天 = 2017-06-10。由 Row 1 (2017-03-02, SCDY 196) 反推 RFSTDTC = 2016-08-19 → 2017-04-01 = SCDY 226 ✔ (Row 2 依据成立), 2017-06-10 = SCDY 296 ≠ PDF 297 → T-2 / O52 (PDF 自身矛盾, KB 照录) 判定正确。勘误 (1)(2) 均成立。
- **授权范围**: `git diff --stat HEAD -- knowledge_base/domains/SC/` = assumptions.md +4 (仅 Specification 标题 + 首句), examples.md 6 行 (表头 1 格 + M-1 主控裁定去重); spec.md 未动 (mtime 2026-11-25)。无授权外改动。
- **md5**: examples.md `cc07ab726ff3a5ed7734183b8b749324`, assumptions.md `b2771af79138622abac5d919865604c1` = writer attempt 2 报告终态。
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42 (基线 42)。

## G-TB8
- trace: T2.B-SC writer `oh-my-claudecode:executor` subagent_done a1 (05:07:51Z) / a2 (05:08:48Z); reviewer `oh-my-claudecode:code-reviewer` subagent_done (05:11:45Z, CONDITIONAL 仅证据修正, 主控已勘误)。无 `agent: main` 写 KB 记录。
- KB 文件 mtime: assumptions.md 05:06:27Z, examples.md 05:08:35Z, 均早于 reviewer 完成 → 终态经 reviewer 审过。✔

## 对照 writer / reviewer (判完后)
- 与 writer 变更清单 / reviewer 51 格人工核一致; 本 auditor 未发现新增问题。

## 结论
- **PASS** — 丢失 0 / 忠实 0 (范围外 1: SC spec 表脚注 ig34_p0341_a005, 已在 O15/O24/O26 覆盖)。
