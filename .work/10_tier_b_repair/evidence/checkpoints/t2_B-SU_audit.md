# T2 B-SU auditor (Rule A 独立抽检) — attempt 1

> agent: oh-my-claudecode:verifier (opus); seed 20261126; base = HEAD (未提交改动)
> 先独立判, 判完才对照 writer 报告 `t2_B-SU.md`。

## 抽样
- 命令: `python3 -I <scratch>/t2_B-SU_auditor/sample.py` (= `t2_auditor_v1.0.md` 模板, 三处按主控 brief 调整):
  1. files = batch kb_files (`SU/examples.md`) ∪ 本批实际改动 `SU/assumptions.md`;
  2. pages = SU 全节 p129-133 (batch json 只写 p129);
  3. 只留 parent_section = §6.1.6 SU 的原子 (排除 p133 §6.2 章引言 a011-a018 与 §6.2.1 AE 原子, 先例 B-CO/B-DI)。另 OTH 排除 ig34_p0133_a021 (他批 AE)。
- 结果: C = 1, P = 32, N = 10. 样本: C 1 (p0129_a003) + P−C 9。
- 附加: P 全 32 原子机械匹配 (规范化弯/直引号、空白、`**`): 31 精确命中单行; 1 未命中 = p0132_a014 (Row 1), 唯一差即 T-1 `SUENTTP`→`SUENTPT`。

## 样本表
| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0129_a003 | p129:3-4 SU Description/Overview 句 (interventions domain … chronic substance use) | assumptions.md:5 | 否 | 是 | 是 | 本批 REAL_GAP 插入, 逐字; 标题 `## SU – Description/Overview` (U+2013 同 PDF) 置于 Assumptions 前, 同 CM 先例 |
| 2 | ig34_p0132_a004 | p132:5 Ex1 引言 "This example illustrates … CRF collected:" | examples.md:5 | 否 | 是 | 是 | 逐字 |
| 3 | ig34_p0131_a006 | p131:14-16 假设 1a (detailed SU info may not be required; 问句例; qualifiers 不提交) | assumptions.md:14 | 否 | 是 | 是 | 逐字 (弯→直引号) |
| 4 | ig34_p0132_a009 | p132:10 列表 "Current caffeine use" | examples.md:11 | 否 | 是 | 是 | 一级列表项, 层级同 PDF |
| 5 | ig34_p0132_a011 | p132:12 子项 "How many cups today" | examples.md:13 | 否 | 是 | 是 | 二级子项 |
| 6 | ig34_p0131_a007 | p131:17 假设 1b (prespecified + free text) | assumptions.md:15 | 否 | 是 | 是 | 逐字 |
| 7 | ig34_p0131_a014 | p131:32-33 假设 3b SUGRPID (含 see Section 4.2.6 交叉引用; 不替代 SUCAT/SUSCAT) | assumptions.md:24 | 否 | 是 | 是 | 交叉引用保留 |
| 8 | ig34_p0131_a015 | p131:34 假设 4 标题 "Timing variables" | assumptions.md:26 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0132_a010 | p132:11 子项 "What caffeine drinks subjects consumed today" | examples.md:12 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0131_a012 | p131:27 假设 3 标题 "Additional categorization and grouping" | assumptions.md:22 | 否 | 是 | 是 | 逐字 |

**独有丢失 0, 忠实度错误 0 → PASS。**

## 其他核查
- diff 授权范围: `git diff HEAD -- knowledge_base/domains/SU/` = 仅 assumptions.md +10 行纯插入 (Description/Overview 标题+句、Specification 标题+spec 首句、Assumptions 标题), 无删改; examples.md / spec.md 未改。均在 writer 授权内 (Description/Overview、spec 首句、PDF 原有小标题)。
- spec 首句 assumptions.md:9 与 p129:6 逐字, U+2014 em dash 同 PDF; 3 处标题 U+2013 同 PDF p129:2,5 / p131:12。
- T-1 (p132:19 Row 1 `SUENTTP`): 正确值由 PDF 自身可定 (p131:6 变量名 SUENTPT; p132:24 Row 3 说明; p133:2 表头) → KB `SUENTPT` (examples.md:19) 合规。小瑕疵: writer 报告与 `B-SU.writer.jsonl` 写 `examples.md:23`, 实为 :19 (:23 是 Row 3), 不影响判定。
- p133 su.xpt 表 (TABLE_ROW, 非本抽样对象) 顺带对 p133 文本: Row 3 SUENDTC=2003 / SUSTTPT=2006-03-15 / SUSTRTPT=BEFORE 与 KB examples.md:39 一致; p0133_a003 原子串列已由 reviewer 登记。
- 范围外观察 (不计本批): p133 §6.2 "Models for Events Domains" 章引言及域列表 (a011-a018) ledger 仅 PARTIAL 匹配到 ch02/ch04/varindex, KB 无对应节引言; 属 §6 章级, 非本批 kb_files。
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (基线 42)。
- G-TB8: trace.jsonl:281 writer `oh-my-claudecode:executor` subagent_done 05:05:31Z; :293 reviewer `oh-my-claudecode:code-reviewer` PASS 05:07:47Z; 无 `agent: main` 的 B-SU 写 KB 记录; assumptions.md mtime 2026-11-26T05:04:53Z (早于 writer done 与 reviewer PASS, 无 reviewer 后改动)。→ PASS
