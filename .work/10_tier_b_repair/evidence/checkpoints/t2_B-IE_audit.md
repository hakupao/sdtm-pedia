# T2 B-IE auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

### 抽样
- 命令: 模板 t2_auditor_v1.0 抽样脚本, 两处按 common brief 调整: `files = kb_files ∪ {knowledge_base/domains/IE/assumptions.md}` (本批实际改动文件); `pages = {193, 194}` (IE 完整节 §6.3.4, p193 顶 - p194 中; batch pdf_pages 仅 [193]). 脚本存 scratch `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-IE_auditor/sample.py`, 输出 `sample.json`.
- seed = 20261126; C = 1; P = 11; N = 10 (C 1 + P−C 9).
- P = a003(p193), p194 a002/a003/a004/a005/a008/a009/a010/a018/a019/a020. 其中 p194 a018-a020 属 §6.3.5 (对照, KB 落在 LB/assumptions.md, 本批范围外).
- 先独立判, 判完才读 writer/reviewer 报告对照 (一致).

### 样本判定
| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0193_a003 | p193:3 IE Description 句 "A findings domain that contains those criteria …" | IE/assumptions.md:5 | 否 | 是 | 是 (`## IE – Description/Overview` 下) | 本批 REAL_GAP, 逐字 |
| 2 | ig34_p0194_a018 | p194:32-33 §6.3.5 引言首句 (IS/LB/MB 按标本分组) | LB/assumptions.md:5 | 否 | 是 | 范围外 (§6.3.5) | 对照, 存在 |
| 3 | ig34_p0194_a002 | p194:2-3 Assumption 1 (只收未满足条件; 见 Section 7.4.1) | IE/assumptions.md:13 | 否 | 是 | 是 | 交叉引用在 |
| 4 | ig34_p0194_a003 | p194:4-7 Assumption 2 (入组时点例外; 非方案偏离; 见 Section 6.2.7) | IE/assumptions.md:15 | 否 | 是 | 是 | e.g. 括号/交叉引用在 |
| 5 | ig34_p0194_a010 | p194:18 "Rows 3-4: …同一 inclusion criterion" | IE/examples.md:9 | 否 | 是 | 是 | `**Rows 3-4:**` 格式 |
| 6 | ig34_p0194_a004 | p194:8-10 Assumption 3 (IETEST 200 字符; 见 Section 4.5.3.1) | IE/assumptions.md:17 | 否 | 是 | 是 | |
| 7 | ig34_p0194_a009 | p194:17 "Rows 1-2: …2 inclusion/exclusion exceptions" | IE/examples.md:7 | 否 | 是 | 是 | |
| 8 | ig34_p0194_a020 | p194:33-34 §6.3.5 "Additional laboratory domains …" | LB/assumptions.md:5 | 否 | 是 | 范围外 (§6.3.5) | 对照, 存在 |
| 9 | ig34_p0194_a008 | p194:16 Example 1 引言 (3 subjects …) | IE/examples.md:5 | 否 | 是 | 是 | |
| 10 | ig34_p0194_a005 | p194:11-13 Assumption 4 (28 个不用 qualifier 列表) | IE/assumptions.md:19 | 否 | 是 | 是 | PDF 折行 "--\nSTRESU"/"--\nLOBXFL" 在 KB 为 `--STRESU`/`--LOBXFL`, 正确 |

- 独有信息丢失: **0**; 忠实度错误: **0**; 范围外发现: 0 (对照 2 条均存在).

### 补充核查
- P 全 11 原子机械匹配 (空白规范化 + 去 `**` 后子串): 11/11 精确命中 (IE 8 条 → IE/assumptions.md 或 examples.md; §6.3.5 3 条 → LB/assumptions.md).
- 新增 3 标题 + spec 首句码位: `IE – Description/Overview` / `IE – Specification` / `IE – Assumptions` 均 U+2013 (= PDF); spec 首句 "Not Met — Findings" U+2014 (= PDF p193:5). 位置/格式与 CM 先例一致.
- diff 授权范围: `git diff HEAD -- knowledge_base/domains/IE/` = assumptions.md +10 纯插入 (Description/Overview 段, spec 首句段, Assumptions 标题), 原列表 1-4 未动; examples.md md5 `2c90e887…` = HEAD; spec.md 未动.
- spec 表脚注 "1In this column, an asterisk (*) …" (p193:44) spec.md 缺 → O15, 按主控口径不计.
- live docs: `python3 tools/check_links.py 2>&1 | grep "live docs"` → 42 (= 基线).
- G-TB8: trace.jsonl 行 268 writer (`oh-my-claudecode:executor`, 05:01:55Z) + 行 278 reviewer (`oh-my-claudecode:code-reviewer`, PASS, 05:04:01Z) 均有 subagent_done; 无 `agent: main` 写 IE KB 记录; IE/assumptions.md mtime 05:01:12Z 早于 reviewer PASS (终态经 reviewer).

### 结论
**PASS** (Rule A N=10 seed=20261126: 丢失 0 忠实 0).
