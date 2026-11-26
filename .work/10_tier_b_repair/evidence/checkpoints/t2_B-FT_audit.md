# T2 B-FT auditor (Rule A 独立抽检) — attempt 1
> agent: oh-my-claudecode:verifier (opus); seed 20261126; 2026-11-26T05:01Z

## 抽样
- 命令: t2_auditor_v1.0.md 种子脚本, 改两处 (按 common brief §6): `files = kb_files ∪ {knowledge_base/domains/FT/assumptions.md}`; pages = 318-324 (§6.3.9 父节引言 p318 + §6.3.9.1 FT 全节 p319-324); 前缀 ig34. 输出 scratch `t2_B-FT_auditor/sample.json`.
- C = 2 (a017/a018), P = 53, N = 10 (C 2 + P−C 8).
- 先独立判 (PDF 页文本 + KB 全文 + 原子 verbatim 子串机检), 判完才读 writer checkpoint 对照.

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0318_a018 | p318:34-35 CDISC 为公有领域/获授权 QRS 工具开发 CT 与 supplement | FT/assumptions.md:9 | 否 | 是 | 是 (§6.3.9 引言) | 逐字 (C) |
| 2 | ig34_p0318_a017 | p318:32-33 SDTMIG 含 FT/QS/RS, 仅概念/域码/例子不同, 共享假设 | FT/assumptions.md:7 | 否 | 是 | 是 | 逐字 (C) |
| 3 | ig34_p0318_a005 | p318:5-7 PE Ex1 Rows 3-5 PESPID/MedDRA 说明 | PE/examples.md:8 | 否 | 是 | 是 (PE Ex1) | 对照原子, 在本批 kb_files 外, 逐字 |
| 4 | ig34_p0322_a014 | p322:31 QRS 7a annotated CRF 可作全文参考 | FT/assumptions.md:69 | 否 | 是 | 是 | 逐字 (’ vs ' 引号风格 O40 不计) |
| 5 | ig34_p0323_a002 | p323:3-6 QRS 9 supplement 由 SDS QRS Subteam 统筹 | FT/assumptions.md:73 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0318_a019 | p318:36-37 CT 下载 URL 条目 | FT/assumptions.md:11 | 否 | 是 | 是 | 逐字含 URL |
| 7 | ig34_p0321_a011 | p321:19 ii. Category of Functional Test | FT/assumptions.md:42 | 否 | 是 | 是 | 逐字 |
| 8 | ig34_p0321_a013 | p321:21 1c TESTCD/TEST codelist 按工具名分列 | FT/assumptions.md:44 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0322_a015 | p322:32-33 (+p323:1-2 续) QRS 8 --EVAL/--EVALID 禁用 | FT/assumptions.md:71 | 否 | 是 | 是 | 原子跨页截断; KB 含完整句 + 续文 + URL |
| 10 | ig34_p0321_a007 | p321:11-14 QRS 1 --CAT 承载工具名 + 例 | FT/assumptions.md:38 | 否 | 是 | 是 | 逐字 |

- 独有信息丢失 0; 忠实度错误 0; 位置错 0.

## 额外核
- p318 §6.3.9 父节引言 (p318:27-41, 206 词, 3 段 + 2 bullet + 末段) vs FT/assumptions.md:3-14: 规范化空白后 **逐字全等** (python 比对 True, 0 diff). 标题 `## §6.3.9 …` 与 p318:27 一致.
- p319:1-6 `§6.3.9.1 Functional Tests (FT)` / Description 句 / spec 首句 → :16/:20/:24 逐字 (比对 True).
- git diff HEAD: FT/assumptions.md 纯插入 (+25 行, 第 3-26 行), 0 删除; 内容限于父节引言 + 子节标题 + Description/Overview + spec 首句 + PDF 原有 `FT – Assumptions` 小标题 → 均在授权范围. FT/examples.md 无改动.
- P 全 53 原子机械子串匹配: 48 精确; 5 不匹配全部可解释: p322_a009 (PDF "an resolution", KB "a resolution", 已登记沿用 B-RS T-5); p323_a006 (PDF "--STRNC", KB "--STNRC", T-6); p322_a013 (已登记原子抽取错, KB 7 条含 "see Section 4 of the QRS supplement" 与 p322:29 一致); p323_a008 (PDF 缺 ")." → T-1, 依据 p328 平行句成立); p324_a007 (QS Description, §6.3.9.2, 在 QS/assumptions.md:5 逐字, 非本批).
- 父节引言放置 (writer Q-1) 仅此一处 (grep 全 KB 唯一, 无重复副本); 是否认可位置由主控定, 不影响本批抽检结论.
- G-TB8: trace 有 B-FT writer (executor a1 04:54:16Z, a2 04:58:45Z) 与 reviewer (code-reviewer a1 04:57:49Z PASS, a2 delta 04:59:16Z PASS) subagent_done; 终态改动 (L-1 标题) 已经 reviewer delta 复审; 无 `agent: main` 写 B-FT KB 记录.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (基线 42).
- 对照 writer checkpoint: 结论一致, 无新增分歧.

## 结论: **PASS** (Rule A N=10 seed=20261126: 丢失 0 / 忠实 0)
