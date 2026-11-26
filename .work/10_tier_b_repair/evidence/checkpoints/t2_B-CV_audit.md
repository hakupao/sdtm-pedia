# T2 B-CV auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus; 先独立判, 判完才对照 writer/reviewer 报告)

- 命令: `t2_auditor_v1.0.md` 抽样脚本, 两处按主控口径调整: `files` = batch kb_files ∪ {`knowledge_base/domains/CV/assumptions.md`} (主控授权, 本批实际改动); `pdf_pages` → CV 全节 {286,287,288,289}. 其余逐字不变. 输出 scratch `t2_B-CV_auditor/sample.json`.
- seed = 20261126; C = 1 (ig34_p0286_a017); P = 9; N = min(30, max(10, 1), |P|) = 9 → P 全量 (C 1 + P−C 8).
- P 小的原因: CV 节 p287-288 全是 spec 表 (IE), p289 主体为两张例子表 (表格由 reviewer 全检); prose 仅 Description、Assumptions 1-2、Ex1/Ex2 引言 + p286 上半页 NV 通用表脚注 1 条.
- 样本: p0286_a017, p0289_a015, p0286_a014, p0289_a004, p0289_a006, p0288_a021, p0288_a020, p0289_a005, p0289_a003.

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0286_a017 | p286:41-42 Description: CV 为 findings 域, 心血管系统 (心脏/血管/淋巴管) 生理与形态发现 | CV/assumptions.md:5 | 否 | 是 | 是 (## CV – Description/Overview, 在 Specification 前) | REAL_GAP 已补, 空白归一后逐字 |
| 2 | ig34_p0289_a015 | p289:20 Ex2 引言: CVTEST 表示经胸超声评估的主动脉瓣结构 | CV/examples.md:19 | 否 | 是 | 是 (## Example 2) | 逐字 |
| 3 | ig34_p0286_a014 | p286:36-37 §6.3.7.1 通用表脚注 (asterisk = CT) | NV/assumptions.md:34 | — | — | — | 范围外不计: 属 §6.3.7.1 (B-NV, 已提交 b093218), 不在 CV kb_files; 已在 NV 处存在, 无发现 |
| 4 | ig34_p0289_a004 | p289:3-4 Ex1: 主动脉肾上/肾下/胸段检查动脉瘤 | CV/examples.md:5 | 否 | 是 | 是 (## Example 1) | 逐字 |
| 5 | ig34_p0289_a006 | p289:4-5 Ex1: rows 1-3 为胸主动脉动脉瘤相关评估, 用 CVGRPID 分组 | CV/examples.md:5 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0288_a021 | p288:49-50 Assumption 2: 可加 Identifiers/Timing/Findings qualifiers, 列出 8 个一般不用 | CV/assumptions.md:15 | 否 | 是 | 是 (## CV – Assumptions 2.) | 逐字, 8 个变量齐 |
| 7 | ig34_p0288_a020 | p288:47-48 Assumption 1: CV 表示心血管诊断程序结果; 程序实施信息入 PR | CV/assumptions.md:13 | 否 | 是 | 是 (## CV – Assumptions 1.) | 逐字 |
| 8 | ig34_p0289_a005 | p289:4 Ex1: 解剖位置细节在 CVLOC | CV/examples.md:5 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0289_a003 | p289:3 Ex1 首句: 主动脉相关发现 + 腹主动脉瘤有无评估 | CV/examples.md:5 | 否 | 是 | 是 | 逐字 |

**本批计分样本 8: 独有丢失 0 / 忠实度错误 0 → 抽检 PASS.** (a014 范围外 1 条, 无发现.)

### 旁证: CV 节全部非表原子机械匹配 (空白归一, 列表号去除)
- prose 8 条 (上表 #1,2,4-9) 全部精确命中 CV/{assumptions,examples}.md.
- HEADING: `CV – Description/Overview` / `CV – Specification` / `CV – Assumptions` (en dash U+2013) 与 PDF pdftotext 码位一致 (assumptions.md:3/7/11); `Example 1`/`Example 2` 命中; `CV – Examples` 由文件标题 `# CV — Examples` 承载 (导航, 与他域一致); `6.3.7.2 Cardiovascular System Findings (CV)` 节号标题 KB 未单列, 与他域同惯例 (导航, 不计).
- spec 首句: assumptions.md:9 与 PDF p286:44 repr 逐字一致 (含 em dash U+2014).
- p288_a018 (CV spec 表脚注) = IE, 属 spec.md, 不在本批.

### 本批改动表格单元独立核 (渲染 p289 `pdftoppm -f 289 -l 289 -r 110`)
- Ex2 Row1 CVTEST = "Native Cardiac Valve Intervention Type" ✓ (旧值 "…Structure Without Intervention Type" 为 KB 自造错误, 已纠正); Row1 CVLOC = "AORTIC VALVE" (无 ANNULUS) ✓.
- Ex2 Row7/8 CVTEST "Minor/Major Axis Cross-sec. Diameter, MVS" 带点 ✓; Row3-6 "Cross-sec" 无点 ✓ (渲染图与 pdftotext layout p289:32-52 一致). 原子 ig34_p0289_a024/a025 漏点 = 已登记原子抽取错, 以渲染图为准.
- Ex1 5 行 × 15 列对渲染图抽核: 002-2004 / CVGRPID 2,2,2,空,空 / CLASS A / SUPRARENAL/INFRARENAL AORTA / 2015-06-09T14:20 均一致.

### 授权范围核
- `git diff HEAD -- knowledge_base/domains/CV/`: assumptions.md 仅 +10 行 (Description/Overview 标题+句、Specification 标题+首句、Assumptions 标题), 列表 1-2 未动; examples.md 仅 3 格 CVTEST; spec.md 未动 (md5 `de8c6d00e0a9dddeadd8c872d509170e`). 无授权范围外改动.

### G-TB8
- trace.jsonl T2.B-CV: writer `oh-my-claudecode:executor` subagent_done a1 (04:35:58Z) + reviewer `oh-my-claudecode:code-reviewer` a1 PASS (04:38:28Z); 无 `agent: main` 写 KB 记录 ✓.
- 终态经 reviewer: 现 md5 assumptions `2fc68d6a9db973b6df5115de8e06ad80` / examples `71e6f9abbe39847649e907a3202e464b` = writer 声明值; KB mtime 04:34:35Z 早于 reviewer checkpoint 04:39:04Z ✓.

### live docs
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (写本文件前; 基线 42).

### 对照 writer/reviewer (判后)
- 与 writer 变更清单 #1-6 及 reviewer PASS 一致; 无分歧.

### 结论
**PASS** — Rule A N=9 (P 全量, 计分 8 + 范围外 1) seed=20261126: 丢失 0, 忠实 0; 范围外发现 0.
