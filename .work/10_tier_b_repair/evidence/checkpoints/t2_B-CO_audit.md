# T2 B-CO auditor (Rule A 独立抽检) — attempt 1

- agent: oh-my-claudecode:verifier (opus); 与 writer (executor) / reviewer (code-reviewer) 不同。先独立判, 判完才对照 writer 报告。
- 改动文件 (git diff HEAD): `knowledge_base/domains/CO/examples.md:28` (Ex1 Row 4 COVAL1/COVAL2) + `knowledge_base/domains/CO/assumptions.md:5` (主控授权 M-1, §5 章引言第 2 句)。`spec.md` 未动 (mtime 2026-11-25)。
- 页范围: p60-62 (§5 章引言 + 5.1 CO); p62 后半 5.2 DM 原子属 B-DM, 排除。

## 抽样
- 命令: t2_auditor_v1.0 模板脚本 (scratch `t2_B-CO_auditor/sample.py`), 改动 3 处: kb_files ∪ `CO/assumptions.md`; pages = {60,61,62}; 追加排除 parent_section 含 "5.2" 的 DM 原子 (首跑未排除时 P=21, 含 p62 a016/a017 DM 句, 按主控指示剔除后重跑)。
- seed = 20261126; C = 0 (batch atoms/t2_recheck 为空); P = 19; N = 10 (全部来自 P−C)。
- P 全 19 原子另做机械匹配 (去连字符/空白规范化 + 去列表编号后子串比对 KB): 19/19 精确命中 `assumptions.md`。

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0061_a012 | p61 Assump 4 第 2 句: 关联评论到父记录详见 Section 8.5 | assumptions.md:30 | 否 | 是 | 是 | 逐字, 交叉引用在 |
| 2 | ig34_p0061_a011 | p61 Assump 4: >200 字符时 COVAL/COVAL1/COVALn, 见 Ex1 rows 3-4 | assumptions.md:30 | 否 | 是 | 是 | 逐字; 与 Row 4 改后 COVAL1 一致 |
| 3 | ig34_p0060_a003 | p60 §5 章引言第 2 句: special-purpose domains 提供标准结构… | assumptions.md:5 | 否 | 是 | 是 | 本批 M-1 新增句, 逐字, 接第 1 句同段 |
| 4 | ig34_p0060_a006 | p60 CO Description: 含可随其他数据收集的评论的特殊域 | assumptions.md:11 | 否 | 是 | 是 | 逐字 |
| 5 | ig34_p0061_a010 | p61 Assump 3c 末: CODTC 应 null (继承父记录时间), rows 3-5 | assumptions.md:28 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0060_a024 | p60 spec 表脚注 ¹: 星号=可能受 CT; codelist 括号 | assumptions.md:17 | 否 | 是 | 是 | 逐字 (spec 表脚注以引用块挂 spec 首句下, 既有先例) |
| 7 | ig34_p0061_a002 | p61 Assump 1 首句: CO 提交自由文本评论方案 (Section 8.5)… | assumptions.md:21 | 否 | 是 | 是 | 逐字, 交叉引用在 |
| 8 | ig34_p0061_a007 | p61 Assump 3b: 关联域非具体记录 → RDOMAIN 填, IDVAR/IDVARVAL null; row 2 | assumptions.md:27 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0060_a008 | p60 spec 首句 co.xpt, Comments — Special Purpose… | assumptions.md:15 | 否 | 是 | 是 | 逐字, U+2014 一致 |
| 10 | ig34_p0061_a014 | p61 Assump 6: 可加 Identifier/Timing, 但不用 --GRPID…--RFTDTC | assumptions.md:34 | 否 | 是 | 是 | 逐字 (PDF "--\nREFID" 折行已合并) |

- 独有信息丢失: **0/10**; 忠实度错误: **0**; 位置错误: 0; 范围外发现: 0。

## 附加核查 (非 prose, 独立方法)
- Row 4 改动: p62 `pdftotext -bbox` — Row 4 (y≈239.5) "Remaining" xMin 456.55 = COVAL1 表头 xMin 456.55 (COVAL2 表头 514.78); 渲染图 `pdftoppm -f 62 -l 62 -r 110` 目视同 (Row 4 COVAL1="Remaining text", COVAL2 空)。KB :28 改后正确; 与 Assump 4 "next 200 in COVAL1" 一致。co.xpt 8 行对渲染图其余格目视 0 差。
- Row 1-8 叙述 (TABLE_ROW 原子 p61 a017-a021, p62 a001-a003) 对 `examples.md:5-19` 逐句: 一致 (Row 6 "are populated link the comment" 为 PDF 原文照录, 非 KB 错)。
- diff 授权范围: 仅 2 行 (examples :28 表格格位; assumptions :5 主控授权章引言句), 无授权外改动; 无 D6/伪节号/KB 自写。
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (= 基线 42)。

## G-TB8
- trace: B-CO writer `oh-my-claudecode:executor` attempt 1 (05:02:18Z) + attempt 2 (05:02:59Z, M-1); reviewer `oh-my-claudecode:code-reviewer` PASS (05:04:47Z) 在 writer 末次之后 → 终态经 reviewer。
- KB mtime: examples.md 05:01:20Z, assumptions.md 05:02:45Z, 均早于 reviewer 完成 → reviewer 审的即终态。
- `grep B-CO trace.jsonl | grep -c '"main"'` → 0, 无主控写 KB 记录。**OK**。

## 对照 writer 报告 (判完后)
- writer 记 M-1 (ig34_p0060_a003) 与本审 #3 一致; Row 4 非 PDF_TYPO 判断与 bbox 结果一致。无分歧。

## 结论: **PASS** (丢失 0, 忠实 0)
