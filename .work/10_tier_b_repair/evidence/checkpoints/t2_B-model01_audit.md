# T2 B-model01 — auditor (Rule A 独立抽检)

## attempt 1

- auditor: `oh-my-claudecode:verifier` (opus); 与 writer (executor) / reviewer (code-reviewer) 不同. 先独立判 (diff + PDF 页 + 机检), 判完才读 writer/reviewer 报告对照.
- 审计对象: `git diff ae17f74 -- knowledge_base/model/01_concepts_and_terms.md knowledge_base/model/02_observation_classes.md` (2 files); md5 01 `531c2d5459604aefdc238ff56eb92bef` / 02 `00146fbcca61f529bbf1026df381c69f` (= writer 续3 终态).
- scratch: `S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-model01_auditor`

### 抽样
- 正式样本: `t2_auditor_v1.0.md` 抽样脚本原样 (b=B-model01, seed=20261126) → `$S/sample.json`: **C=28, P=75, N=10**.
- 扩展样本 (dispatch "N=max(10, ceil(0.2×prose atoms))" + 主控要求覆盖 R3 新增): C' = pp4-12 全部 sv20 非标题 prose 原子中 base(ae17f74) KB 不含原文者 = 124 → N'=25 (seed 20261126; 先从 C'−正式样本抽 13, 余 12 从未改对照抽) → `$S/sample_ext.json`. 合计 35 样本.
- 补充全扫 (100%): `python3 -I $S/chk.py $S` (`$S/sweep.tsv`) — sv20 pp4-12 全部 169 个 prose/标题原子 verbatim (归一化) 对 KB 子串: 164 命中, 5 不命中 = p6 a020 (T-1 改值, 见下) + p9 a014/a015/a017 (列表→表格, 前缀 "X Qualifiers," 拆到 Subclass 格; Purpose 格逐字, 人工核过) + p12 a004 (表题, KB 用 `**Structure:**` 既有格式, 非本批). 反向 `python3 -I $S/rev.py` (KB 句→PDF pp4-12): 不命中仅标题/Source/导航、Key 行 (Concept Map 既有)、D6 KB note + KB 自写 Examples 列、跨页句 (01:188 / 02:33, 目视 p9-10 / p11-12 连续一致) — 0 处 KB 自造或改义.

### 样本表

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | sv20_p0004_a024 | p4 §1.2 TAUGs 项 (含 URL) | 01:26 | 否 | 是 | §1.2 ✓ | 逐字 |
| 2 | sv20_p0004_a023 | p4 "In addition to the IGs…" 引导句 | 01:24 | 否 | 是 | §1.2 ✓ | 逐字 |
| 3 | sv20_p0004_a005 | p4 §1.1 changes 见 Section 1.4 与 Section 7 | 01:9 | 否 | 是 | §1.1 ✓ | 两处交叉引用全 |
| 4 | sv20_p0005_a005 | p5 §1.3 SDTM 演进句 | 01:34 | 否 | 是 | §1.3 ✓ | 逐字 |
| 5 | sv20_p0005_a009 | p5 §1.4 少数旧变量可 deprecated | 01:38 | 否 | 是 | §1.4 ✓ | "however, isolated" 保留 |
| 6 | sv20_p0004_a015 | p4 §1.2 Sponsors 应先读 IGs | 01:15 | 否 | 是 | §1.2 ✓ | 逐字 |
| 7 | sv20_p0005_a027 | p5 列表 "Variable Qualified (when Role is…)" | 01:62 | 否 | 是 | §1.4 Changes to Structures ✓ | 引号限定保留 |
| 8 | sv20_p0005_a032 | p5 列表 "Examples" | 01:67 | 否 | 是 | 同上 ✓ | 11 项顺序 = PDF |
| 9 | sv20_p0005_a015 | p5 Domain-specific 内容移至 3.1.1/3.1.2/3.1.3 | 01:47 | 否 | 是 | §1.4 Reorganization ✓ | 3 处交叉引用全 |
| 10 | sv20_p0004_a019 | p4 SDTMIG-AP 项 + URL | 01:19 | 否 | 是 | §1.2 ✓ | URL 一致 |
| 11 | sv20_p0008_a005 | p8 §2 SDTM 主要目的 (subjects—…—or devices) | 01:114 | 否 | 是 | §2 ✓ | em dash 恢复 PDF |
| 12 | sv20_p0006_a027 | p6 --LOINC 角色改 Record Qualifier 及原因 | 01:104 | 否 | 是 | §1.4 Changes to Datasets ✓ | "--SPEC and --METHOD" 全 |
| 13 | sv20_p0004_a008 | p4 监管机构另有指南 | 01:11 | 否 | 是 | §1.1 ✓ | 逐字 |
| 14 | sv20_p0010_a003 | p10 §2.2 引导句 | 01:192 | 否 | 是 | §2.2 ✓ | "this document" 恢复 PDF |
| 15 | sv20_p0010_a011 | p10 Variable C-code (NCI-EVS 全称) | 01:201 | 否 | 是 | §2.2 ✓ | 全称保留 (旧表丢的已补) |
| 16 | sv20_p0004_a016 | p4 "The following implementation guides…" | 01:15 | 否 | 是 | §1.2 ✓ | 段尾 |
| 17 | sv20_p0011_a028 | p11 domain code 作前缀的理由 | 02:31 | 否 | 是 | §3.1 ✓ | 逐字 |
| 18 | sv20_p0006_a006 | p6 未全有 c-code, 将补 | 01:75 | 否 | 是 | §1.4 ✓ | 逐字 |
| 19 | sv20_p0006_a010 | p6 --OCCUR 不得用于 AE | 01:81 | 否 | 是 | §1.4 ✓ | 逐字 |
| 20 | sv20_p0010_a007 | p10 Format (ISO / "number-number") | 01:197 | 否 | 是 | §2.2 ✓ | 逐字 |
| 21 | sv20_p0005_a017 | p5 3 个多余标题层级被删 | 01:49 | 否 | 是 | §1.4 ✓ | 分号分隔 3 标题全 |
| 22 | sv20_p0010_a006 | p10 Type (SAS data type, 见 2.1) | 01:196 | 否 | 是 | §2.2 ✓ | 交叉引用全 |
| 23 | sv20_p0004_a020 | p4 SENDIG 项 + URL | 01:20 | 否 | 是 | §1.2 ✓ | 逐字 |
| 24 | sv20_p0009_a004 | p9 每观测由命名变量组成; 按 role 分类 | 01:160 | 否 | 是 | §2.1 ✓ | 未改对照 |
| 25 | sv20_p0008_a003 | p8 observations 概念 | 01:112 | 否 | 是 | §2 ✓ | 未改对照 (粗体为 KB 格式) |
| 26 | sv20_p0005_a030 | p5 列表 "Definition" | 01:65 | 否 | 是 | §1.4 ✓ | 未改对照 (短原子) |
| 27 | sv20_p0009_a013 | p9 Qualifier 分 5 子类 | 01:172 | 否 | 是 | §2.1 ✓ | 未改对照 |
| 28 | sv20_p0005_a026 | p5 列表 "Role" | 01:61 | 否 | 是 | §1.4 ✓ | 未改对照 |
| 29 | sv20_p0011_a016 | p11 Interventions 类定义 (列表项) | 02:23 | 否 | 是 | §3.1 ✓ | 唯一一份 (D-12 去重后) |
| 30 | sv20_p0010_a005 | p10 列表 "Variable Label" | 01:195 | 否 | 是 | §2.2 ✓ | 未改对照 |
| 31 | sv20_p0009_a020 | p9 DOMAIN/RDOMAIN 4 句 | 01:186 | 否 | 是 | §2.1 ✓ | 未改对照 |
| 32 | sv20_p0009_a002 | p9 flat files + metadata | 01:158 | 否 | 是 | §2.1 ✓ | 未改对照 |
| 33 | sv20_p0011_a006 | p11 study subject 数据集 2 类 | 02:11 | 否 | 是 | §3 ✓ | 原 Overview 合并句已拆回 PDF 位置 |
| 34 | sv20_p0011_a020 | p11 identifier/timing 变量通用 | 02:27 | 否 | 是 | §3.1 ✓ | 未改对照 |
| 35 | sv20_p0010_a015 | p10 v1.x Description 列内容去向 | 01:206 | 否 | 是 | §2.2 ✓ | 未改对照 |

(行号: 正式样本 #1-10, 扩展样本 #11-35; 行号由 `$S` 内 grep 定位脚本输出, 01 = model/01, 02 = model/02.)

**独有丢失 0/35, 忠实度错 0/35, 位置错 0/35** (全扫 169 原子同样 0 丢失 / 0 改义).

### PDF_TYPO
- T-1 (p6 a020 "Section 3, Associated Persons Data" → KB 01:94 "Section 4"): 由 PDF 自身确定 (p5 a013/a014、p8 a007 均为 Section 4; §3 = Study Subject Data, p11) → 符合 PDF_TYPO 取舍规则, 已登记. 不计忠实度错.

### 删除核 (D-1..D-14)
- D-1/D-2/D-4..D-8: 改写体被同处 PDF 原文取代, 原文全在 (全扫命中).
- D-3 (Synonym Examples 删 --LOINC): KB 自写且与 p6 a027 矛盾 → D2 正确; 表上 D6 前缀 `> KB note (not in SDTM v2.0):` 01:174 在.
- D-9 (§2.2 旧两列表 + Note 段): 被 p10 a003-a016 逐字列表取代; 旧表独有内容 (`Char`/`Num`、`--` 前缀说明) 非 PDF p10 内容, 无 PDF 依据丢失.
- D-10 (model/02 旧 Overview 两段): 信息全在 02:9-27 (p11 a006/a015/a019/a020 原文).
- D-11 (model/01 旧 `### Domain Codes` 3 块): p11 内容, 原文已在 02:15-17 / 02:29 / 02:33 (a011-a013, a027, a030-a032 + p12 a001); 01 无残留指针 (RELOCATE 规则).
- D-12/D-13/D-14 (主控点名复核的终态 delta): `grep -n "Observation Class represents" knowledge_base/model/02_observation_classes.md` → 仅 :23/:24/:25; `grep -n -i "class represents" work/pdf_pages/sv20_p0015.txt work/pdf_pages/sv20_p0020.txt` → 无 (rc=1); p15:28 `3.1.2` 标题后直接为表题 "Events—Topic and Qualifier Variables—One Record per Event", p20:50 `3.1.3` 后直接为 Findings 表题 → 3.1.1/3.1.2/3.1.3 下定义句非 PDF 所属位置, 删除正确; 02:89 `## 3.1.2` / 02:154 `## 3.1.3` 下现为 `**Structure:**` 行. 原 Findings 句 "ECG testing" 的唯一一份 02:25 已为 PDF 原文 "electrocardiogram (ECG) testing".
- 结论: 14 项删除无一丢失 PDF 依据内容.

### 回归
- `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_reg.jsonl` → RED, 15 回退全为 ig34_p0257-0263 (并行 MB/MS 批文件); `grep -c sv20 $S/fp_reg.jsonl` = **0**. sv20 pp4-12 verdict 分布 after = base (PARTIAL 36 / EQUIVALENT 20 / EXACT 2 / IE 1; PARTIAL 因 ledger target 为 ch01_introduction.md, hit_any 现为 model/01).
- `python3 tools/check_links.py | grep "broken relative links"` → `broken relative links: 18668 (live docs: 42)` (不升).

### G-TB8
- trace.jsonl T2.B-model01: writer `oh-my-claudecode:executor` subagent_done ×6 (attempt 1-2 含续1-3), reviewer `oh-my-claudecode:code-reviewer` subagent_done ×3 (CONDITIONAL / PASS / CONDITIONAL); 无 `agent: main` 写 KB 记录 → **PASS**.
- 注 (流程): reviewer 最后一条为 续2 CONDITIONAL (指定 R-2 = D-13/D-14), writer 续3 落实后未再派 reviewer 复审 ("终态必经 reviewer" 口径). 本 auditor 已逐项独立复核该 delta (见上), 内容无误; 是否补一条 reviewer delta 签字由主控定.

### 观察 (非 FAIL, 低风险)
- O-1: model/02 `## Overview` 现为空标题 (紧接 `## 3 Study Subject Data`), H1 "Chapter 3.1" 与 Source "Section 3.1 (Pages 11-39)" 未体现新增 §3 引言 (p11 页码正确). writer 为保锚点保留; 纯导航, 不涉丢失/忠实. 建议主控决定是否改 Source 为 "Sections 3-3.1".
- O-2: Concept Map Key 行 (01:152) 与 `### Variable Roles` / `### Qualifier Variable Subclasses` 为 KB 既有导航/图注, 本批未动.

### 判定
- 独有丢失 0, 忠实度错 0 → **PASS** (Rule A N=10 正式 + 25 扩展 + 169 全扫).
