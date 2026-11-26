# T2 B-ML auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

- 先独立判 (PDF p121-124 txt + p122/p124 110dpi 渲染 + KB 三文件全文), 判完才对照 writer 报告.
- 抽样: 种子脚本按 t2_auditor_v1.0 改两处 (brief 口径): kb_files 加入本批实际改动 `knowledge_base/domains/ML/assumptions.md`; 页范围 = ML 节完整 p121-124 (batch json pdf_pages 只有 121/124). 脚本存 scratch `t2_B-ML_auditor/sample.py`:
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-ML_auditor
python3 -I $S/sample.py > $S/sample.json   # seed 20261126
```
- seed = 20261126; C = 1 (ig34_p0121_a005); P = 26; N = 10 (C 1 + P−C 9).

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0121_a005 | p121:5 spec 首句 "ml.xpt, Meal Data — Interventions. One record per … Tabulation." | ML/assumptions.md:9 | 否 | 是 | 是 | 逐字 (Python == 比对 True); em dash U+2014 码位同 PDF; 位于 `## ML – Specification` 下 (CM 先例). t2_recheck 闭合 |
| 2 | ig34_p0123_a005 | p123:11 Ex1 第 2 bullet "occurrence of of prespecified foods … (DILI)." | ML/examples.md:8 | 否 | 是 | 是 | PDF 重复词 "of of" 属 PDF_TYPO, KB 写 "of prespecified" (T-2, PDF 自身可定) |
| 3 | ig34_p0122_a015 | p122:33 spec 表脚注 ¹ "asterisk (*) … CDISC/NCI codelist values …" | — (ML 三文件均无) | (缺) | — | — | **不计**: spec 表脚注按主控既有裁定 DEFERRED_O26 (B-DM 先例) 并入 O15/O26 spec 脚注全域扫描; 本批 spec.md 授权仅 batch json 问题 (recheck/O4), spec.md md5 = HEAD. 原子 "NCIBI" 另为原子抽取错 (渲染图为 "CDISC/NCI"). 主控须确保 O26 覆盖 ML |
| 4 | ig34_p0123_a020 | p123:31 "Rows 1-3: Show the last meal data for 3 hypoglycemic events." | ML/examples.md:33 | 否 | 是 | 是 | 逐字 (Rows 标签加粗为格式) |
| 5 | ig34_p0124_a007 | p124:18 Ex2 引言 "examines the effect of physical modifications in a cafeteria …" | ML/examples.md:50 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0122_a017 | p122:36-38 Assumption 1 主句 + "Examples of nutritional items that would be represented in other domains include:" | ML/assumptions.md:13 | 否 | 是 | 是 | 原子抽取错: 原子写 "would not be represented in other domains", PDF txt 与 p122 渲染图均为 "would be"; KB = PDF 逐字 |
| 7 | ig34_p0122_a024 | p123:1 2a "Any additional timing variables may be added …" | ML/assumptions.md:22 | 否 | 是 | 是 | 逐字 (2a 位于 2 下) |
| 8 | ig34_p0122_a025 | p123:2-4 2b interval / MLSTDTC/MLENDTC / start not copied to MLENDTC | ML/assumptions.md:23 | 否 | 是 | 是 | 3 句逐字 |
| 9 | ig34_p0122_a022 | p122:43-44 Assumption 1 段尾 "nutritional items represented in ML may be prospectively defined …" | ML/assumptions.md:19 | 否 | 是 | 是 | 逐字, 在 1a-d 之后同缩进段 = PDF 版式 |
| 10 | ig34_p0124_a011 | p124:29 "Food-card data was collected over a 7-month period … 1 day per week." | ML/examples.md:57 | 否 | 是 | 是 | 逐字 |

**本批计分样本 9 (a015 不计): 独有丢失 0 / 忠实度错误 0 → 抽检 PASS.**

### 补充核查
- P 全 26 原子机械匹配 (空白归一后子串, ML 三文件): 22 精确命中; 4 未命中均已处置 — a015 (DEFERRED_O26), a017 (原子错, KB=PDF), p0123_a005 (T-2), p0123_a012 (原子错: 原子 "a row. ADD ROW", PDF p123:19 为 "a row: ADD ROW", KB examples.md:19 = PDF).
- 已登记原子错核: p0121_a011 `MLGRID` → PDF/KB 均 `MLGRPID` (spec.md:41; `grep MLGRID` KB 0); p0124_a001 Row 2 → examples.md:42 与 p124 渲染一致. 均成立.
- examples.md:55 (Ex2 Group 2 Details) 对 p124 渲染逐格: Group "2" / Arms "Experimental: choice architecture" / Details 引导句 + "Physical modifications included:" + 4 bullet (首字母大写、顺序、"e.g., white milk displayed in front of chocolate milk)" 末无句点) 全一致; 弯引号 "nudge" → 直引号 = F-3/O40 全局口径, 不计. Group 1 行与表头一致.
- 授权范围: `git diff HEAD` 仅 assumptions.md 纯插入 3 标题 + 2 句 (Description/Overview、spec 首句、`## ML – Assumptions` = PDF 原有小标题) 与 examples.md:55 一行; 标题 en dash U+2013 = PDF; spec.md md5 `6e3be1a4…` = HEAD (未改). Description 句 Python == PDF 行 True.
- T-1 (Ex2 Row 2 `WHTE MILK` → KB `WHITE MILK`): 依据同表 Row 8 + Details 文本 "white milk", PDF 自身可定, 同意.
- check_links: `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42 (= 基线).
- G-TB8: trace.jsonl:273 writer `oh-my-claudecode:executor` subagent_done 05:03:42Z, :292 reviewer `oh-my-claudecode:code-reviewer` PASS 05:07:39Z; 无 `agent: main` 的 B-ML 记录 (grep rc=1); ML/assumptions.md 与 examples.md mtime 05:01:59Z < writer done (reviewer 后无 KB 改动). PASS.
- 对照 writer 报告 (判后): 与 writer #1-#7、F-1..F-3 一致, 无新增发现.

### 结论
- 独有丢失 0, 忠实度错误 0 → **PASS**. 范围外/待全域: spec 表脚注 (a015) 由 O26 全域扫描兜底.
