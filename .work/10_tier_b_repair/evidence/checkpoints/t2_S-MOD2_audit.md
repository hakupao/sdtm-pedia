# T2S.S-MOD2 Auditor (Rule A) — attempt 1 (批次 writer a2 + reviewer a2 PASS 终态)

> agent: oh-my-claudecode:verifier (opus); 先独立判, 判完才读 `t2_S-MOD2.md` / `t2_S-MOD2_review.md`. 只读 KB.
> 对象: `git diff HEAD -- knowledge_base/model/02_observation_classes.md` (+200/-117); 源 SDTM v2.0 §3.1 p11-39 (`source/cdisc/SDTM_v2.0.pdf`).
> 注意 (dispatch notes S-MOD2 review 教训): table_census / fp_match 对 sv20 页无证明力, 本审不采用; 表格以独立 layout 列解析 + 渲染逐格为准.

## 抽样 (可复跑)
scratch = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-MOD2_auditor/`; `python3 -I $S/sample.py` (repo 根执行).
- P = pdf_atoms 中 sv20_ 且 p11-39, atom_type ∈ SENTENCE/LIST_ITEM/NOTE/CROSS_REF/TABLE_ROW, parent_section 以 "§3.1" 开头 (排除 p11 的 §3 引言原子 14 条), 去 ledger INTENTIONAL_EXCLUDE (R1: 236 条 v2.0 变量表行 IE + 7 句). intros 空.
- |P| = 48 (SENTENCE 32 含 §3.1/3.1.3.1/3.1.4/3.1.5, LIST_ITEM 3, TABLE_ROW 28 中非 IE). writer.jsonl 涉及页 = p11-39 全部 → C = P = 48.
- N = min(30, max(20, ceil(0.1×48)), 48) = 20; 其中 ceil(20/3)=7 取自 C, 13 取自 P−s1. seed = 20261126.
- 样本: sv20_p0022_a004, p0021_a004, p0011_a017, p0027_a009, p0028_a002, p0011_a020, p0012_a001, p0012_a010, p0011_a031, p0012_a007, p0011_a023, p0022_a005, p0012_a012, p0011_a032, p0011_a025, p0022_a003, p0024_a011, p0028_a001, p0011_a028, p0023_a001.

## 样本判定 (TABLE_ROW 判据: R1 下 KB 5 列 = #/Variable/Label/Type/Role(+Qualified), Usage Restrictions 须在 Key Notes; 缺 4 列不计. 均对渲染 p12/21/22/23/24/27/28 逐格核)
| # | atom_id | PDF 页 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | p0022_a004 | p22 FND 9 --CNDAGT Test Condition Agent / Char / Record Qualifier / UR CP, IS, LB | :176 | 否 | 是 | §3.1.3 | 渲染 p22 逐格一致 |
| 2 | p0021_a004 | p21 FND 5 --CSMRKS / Var Qual --TESTCD / CP only | :172 | 否 | 是 | §3.1.3 | 渲染 p21 |
| 3 | p0011_a017 | p11 Events Observation Class bullet | :22 | 否 | 是 | §3.1 | 逐字 |
| 4 | p0027_a009 | p27 FND 49 --GENREF / Var Qual --METHOD / GF only | :216 | 否 | 是 | §3.1.3 | 渲染 p27 |
| 5 | p0028_a002 | p28 FND 52 --SYMTYP / Var Qual --SYM / GF only | :219 | 否 | 是 | §3.1.3 | 渲染 p28 |
| 6 | p0011_a020 | p11 "As a general rule, any valid identifier or timing variable…" | :25 | 否 | 是 | §3.1 | 逐字 |
| 7 | p0012_a001 | p12 跨页续句 "observation class variables; the Usage Restrictions column…" | :31 | 否 | 是 | §3.1 | 逐字 |
| 8 | p0012_a010 | p12 INT 5 --CAT Category / Grouping Qualifier | :49 | 否 | 是 | §3.1.1 | 渲染 p12; Key Notes 简写 Definition (D6) |
| 9 | p0011_a031 | p11 "The variable names include the specific domain prefix." | :31 | 否 | 是 | §3.1 | 逐字 |
| 10 | p0012_a007 | p12 INT 2 --MODIFY Modified Treatment Name / Synonym Qual --TRT | :46 | 否 | 是 | §3.1.1 | 渲染 p12 |
| 11 | p0011_a023 | p11 "Domain specification tables in the implementation guides…" | :27 | 否 | 是 | §3.1 | 逐字 |
| 12 | p0022_a005 | p22 FND 10 --BDAGNT / Var Qual --TESTCD / CP, IS, LB | :177 | 否 | 是 | §3.1.3 | 渲染 p22 |
| 13 | p0012_a012 | p12 INT 7 --PRESP / Var Qual --TRT / Not in nonclinical trials | :51 | 否 | 是 | §3.1.1 | UR + Notes "Y or null" 在 Key Notes |
| 14 | p0011_a032 | p11 "Domain-specific variables are included in the table…" | :31 | 否 | 是 | §3.1 | 逐字 |
| 15 | p0011_a025 | p11 "The SDTM includes information on variables which are not to be used in human clinical trials." | :27 | 否 | 是 | §3.1 | 逐字 |
| 16 | p0022_a003 | p22 FND 8 --TSTCND / Var Qual --TESTCD / CP, IS, LB | :175 | 否 | 是 | §3.1.3 | 渲染 p22 |
| 17 | p0024_a011 | p24 FND 25 --TSTPNL / Grouping Qual / CP only | :192 | 否 | 是 | §3.1.3 | 渲染 p24 |
| 18 | p0028_a001 | p28 FND 51 --SYM / Var Qual --ORRES; --STRESC; --STRESN / GF only | :218 | 否 | 是 | §3.1.3 | 渲染 p28 (KB "/" 分隔 = 本文件统一记法) |
| 19 | p0011_a028 | p11 "The domain code is used as a variable prefix to minimize the risk…" | :29 | 否 | 是 | §3.1 | 逐字 |
| 20 | p0023_a001 | p23 FND 13 --GATE / Record Qual / CP only | :180 | 否 | 是 | §3.1.3 | 渲染 p23 |

**独有丢失 0/20; 忠实度错误 0.**

## 补充独立核 (超出样本; P 小因 R1 表行 IE, 故对全表补做)
- 独立 layout 列解析 (`python3 -I $S/layout_parse.py $S/pdf_rows.json` + `python3 -I $S/compare.py $S`, pdftotext -layout 按每页表头列位切分, 不经 bbox/atoms): PDF 264 行 = KB 264 行, 6 表行数 INT 43 / EVT 56 / FND 100 / FA 1 / ID 16 / TIM 48 全等且逐行序号对齐. 65 行报差, 逐条看均为 layout 列溢出假阳 (变量名/标签折行跨列, Format 值溢入 Role); 其中语义可疑的 --IMPLBL (标签/UR)、--TPT 标签、--NAM 标签、--CHENDY 已渲染 p26/p37/p28 核, KB 正确.
- Usage Restrictions: 全 264 行凡 PDF UR 非空, 其文字均在 KB Key Notes/Notes 格内 (0 缺). FND 表 D6 说明 ":164 blank cell ⇒ PDF UR 也空" 核实属实 (0 反例); 非空且无 UR 的 FND 格 12 个 (--ORRES/--ORNRLO/--SPEC 等) 为 KB 简写/例值, 不矛盾.
- 渲染逐格 (左 9 列): p12, p21, p22, p23, p24, p26, p27, p28, p37 — 共 ~95 行逐格一致.
- Key Notes 矛盾抽查 (对 layout 文本 Notes/Examples): INT --METHOD/--FAST/--VAMT/--EPCHGI, EVT --PRESP/--SER/--SCAN/--BODSYS/--OCCUR..--REASND/--TOX, ID --SEQ, TIM --STDTC/--PTFL/--PDUR/--STRF/--STRTPT/--ENRTPT: 均不矛盾 (TIM 值列举为 KB 补充, 已由 D6 "value lists not given in SDTM v2.0" 覆盖). --SPCUFL 现为 PDF Notes 原文 (HEAD 的 "Y or null" 矛盾已 D2 修正).
- 非表叙述: §3 / §3.1 / §3.1.3.1 / §3.1.4 / §3.1.5 全部 SENTENCE/LIST_ITEM 与 6 个表题、5 个节标题在 KB 逐字在位 (对 p11-12/p32/p34 layout 文本).
- 反向 KB→PDF 全文件 (399 行): 无出处行仅 H1、`Source:` 行、`### Topic and Qualifier Variables (43/56/100 variables)` (计数核实)、Timing 7 个子表 `###` (由 :314 D6 覆盖) = 导航 (U8); 解释性 KB 内容 :160 / :41 / :95 / :164 / :287 / :314 / :316 均已 `> KB note (not in SDTM v2.0):` 标注, 措辞属实 ("some cells add KB wording or example values"). 3.1.3.1 --OBJ Notes 格 = PDF Notes 逐字 (无需 D6). 0 未标 D6 解释句.
- 授权范围: `git diff HEAD --stat -- knowledge_base/` 本批只动 `model/02_observation_classes.md` (ch04 属 S-CH4 并行批). gaps / intros / footnote 均空 (json).
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (= 基线 42).
- G-TB8: trace.jsonl 本批 executor subagent_done ×3 (a1, a1 delta, a2) + code-reviewer subagent_done ×2 (a1 CONDITIONAL, a2 PASS delta); writer a2 (F-1) 之后有 reviewer a2 复审 → 终态经 reviewer; 无 agent: main 写 KB 记录. ✔

## 判完后对照 writer / reviewer
- 与 reviewer 一致: 264 行核心格全一致, 叙述原子全命中, 原子错 sv20_p0037_a001 (--CHDY "Relative" vs 渲染 "Rel") 同意不影响 KB; --RFTDTC Notes "ISO 8601" 为 Format 简写 (R1 缺列 + D6, 不矛盾), 同意仅记录.
- 无新增分歧.

## 结论
丢失 0 / 忠实错误 0 → **PASS**.
