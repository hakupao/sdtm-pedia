# T2 B-QS auditor (Rule A 独立抽检) — attempt 1

> agent: oh-my-claudecode:verifier (opus); seed = 20261126; base = HEAD (未提交 diff)

## 抽样
- 种子脚本同 `t2_auditor_v1.0.md`, 两处按 dispatch notes 调整: pages = 324-329 (QS 全节, 非 batch json 的 328-329); files = kb_files ∪ `knowledge_base/domains/QS/assumptions.md` (本批实际改动). 脚本存 scratch `t2_B-QS_auditor/sample.json`.
- 结果: C = 0, P = 44, N = 10 (全部来自 P − C; P 含 p324 FT 尾句 1 个、p329 RS 引言 6 个作对照).

## 样本判定
| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0328_a002 | p328:2-5 QRS 8: --EVAL/--EVALID 禁用于 QRS; 用 SUPP; QRS 网页 URL | QS/assumptions.md:52 | 否 | 是 | 是 | 逐字 |
| 2 | ig34_p0327_a015 | p327:31-34 QRS 7: --TEST >40 / --QSORRES >200 截断 + 元数据; "see Section 4 of the QRS supplement"; Section 4.5.3 | QS/assumptions.md:49 | 否 | 是 | 是 | 逐字; 原子 verbatim 漏 "; see Section 4 of the QRS supplement", PDF 原页有, KB 有 (原子抽取误差, 不计) |
| 3 | ig34_p0326_a007 | p326:18 无额外 QS 专有 assumptions, 全在 QRS Shared | QS/assumptions.md:13 | 否 | 是 | 是 | 逐字; 位于 PDF 原标题 "QS – Assumptions" 下 |
| 4 | ig34_p0329_a007 | p329 RS 引言: 数据可能/不一定用标准 CRF 收集 | RS/assumptions.md:7 | 否 | 是 | 是 | 对照, kb_files 外 (B-RS 文件), 逐字 |
| 5 | ig34_p0326_a011 | p326:26-27 QRS 1a: Naming Rules 与 CT 列表 URL | QS/assumptions.md:20 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0327_a005 | p327:9-11 QRS 4a.iii: eData 中分数视为采集数据; CT 可扩展, 申请加入 | QS/assumptions.md:36 | 否 | 是 | 是 | 逐字 (引号风格 O40 不计) |
| 7 | ig34_p0327_a007 | p327:14-15 QRS 4b: 总分填 --ORRES/--STRESC/--STRESN, 视为采集分数 | QS/assumptions.md:38 | 否 | 是 | 是 | 逐字 |
| 8 | ig34_p0327_a001 | p327:1-3 QRS 4: 查 QRS 补充件; 派生结果通常视为采集; 运营派生须 --DRVFL | QS/assumptions.md:32 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0329_a006 | p329 RS Description 首句 | RS/assumptions.md:5 | 否 | 是 | 是 | 对照, kb_files 外, 逐字 |
| 10 | ig34_p0326_a012 | p326:28 QRS 1b: 参照以下 CT codelist 取 --CAT | QS/assumptions.md:21 | 否 | 是 | 是 | 逐字; i-iii 三个 codelist 名 :22-24 亦逐字 |

**独有信息丢失 0; 忠实度错误 0.**

## 额外核查
- QRS 共用 assumptions (p326:20 – p328:13) 全段逐词 difflib (`$S/cmp.py`, 去编号/引号归一): PDF 1180 词 vs KB 1179 词, 仅 3 处差: `an`→`a` (T-5), `--STRNC`→`--STNRC` (T-6), `-- SPCCND` 跨行断字合并 (排版). 远超 "≥5 句逐字核" 要求; 0 新差.
- Description/Overview (:5) 与 spec 首句 (:9) 对 p324 原文子串精确匹配 (True); 3 个标题 "QS – Description/Overview / QS – Specification / QS – Assumptions" 均为 PDF p324/p326 原标题.
- examples.md :19/:24 QSTEST "SWLS01-Live Life Over Change Nothing" 与 p328 Row 5、p329 Row 10 (跨行 "Nothing") 一致; 其余 8 行及引言 :3/:9、标题 :7 与 p328 一致.
- 授权范围: `git diff HEAD -- knowledge_base/domains/QS/` 仅 assumptions.md 顶部纯插入 (Description/Overview、Specification + 首句、Assumptions 标题) + examples.md 2 格; 无授权外改动.
- census p324 suppft.xpt PDF_ONLY: FT/examples.md :22 叙述 + :24 `**suppft.xpt**` + :28 Row 1 (FTASSTDV/CANE) 均存在, 且 HEAD 中已存在 → census 假阳性 (非本批改动所补), 无范围外发现.
- G-TB8: trace 有 B-QS writer `oh-my-claudecode:executor` (04:58:46Z) 与 reviewer `oh-my-claudecode:code-reviewer` PASS (05:01:33Z); 无 `agent: main` 写 KB 记录 ✓.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42 (= 基线).
- 对照 writer/reviewer 报告: 判定后对照, 与 reviewer "QRS 逐词 0 新差 (T-5/T-6/O40 沿用)" 一致, 无分歧.

## 结论: PASS
