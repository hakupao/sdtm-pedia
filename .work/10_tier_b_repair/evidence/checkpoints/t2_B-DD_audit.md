# T2 B-DD auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus; 先独立判, 判完才对照 writer/reviewer 报告)

- 命令: `t2_auditor_v1.0.md` 抽样脚本, 两处按主控口径调整: `files` = batch kb_files ∪ {`knowledge_base/domains/DD/assumptions.md`} (主控授权, 本批实际改动; examples.md 未改仍在 P); `J["pdf_pages"] = range(183, 186)` (DD 全节 p183-185; batch json pdf_pages 仅 183). 其余逐字不变. 输出 scratch `t2_B-DD_auditor/sample.json`.
- seed = 20261126; C = 2 (p0183_a003/a004); P = 19; N = min(30, max(10, 1), 19) = 10 → C 2 + P−C 8.
- 样本: p0183_a004, p0183_a003, p0184_a003, p0184_a004, p0185_a004, p0184_a006, p0184_a008, p0184_a022, p0184_a005, p0185_a005.
- 真值: `.work/10_tier_b_repair/work/pdf_pages/ig34_p018{3,4,5}.txt` (layout) + p183 `pdftoppm -r 110` 渲染 (核 bold "not" ×2).

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0183_a004 | p183:4-7 Description 第 2 段: 存放死亡时补充数据; 不替代 AE 现有数据; 不新增采集要求; 提供统一存放处 | DD/assumptions.md:7 | 否 | 是 | 是 (## DD – Description/Overview) | 逐字; 两处 `**not**` 与 p183 渲染图粗体一致 |
| 2 | ig34_p0183_a003 | p183:3 Description 首句: findings 域, 含受试者死因诊断 | DD/assumptions.md:5 | 否 | 是 | 是 (同上) | 逐字 |
| 3 | ig34_p0184_a003 | p184:4-6 Assumption 2: 死亡细节在专门 CRF 页采集; 不汇集 AE.AEOUT/AE.AESDTH/DS.DSTERM; 可用 RELREC 关联 | DD/assumptions.md:17 | 否 | 是 | 是 (## DD – Assumptions 2.) | 逐字 (含三个变量括注) |
| 4 | ig34_p0184_a004 | p184:7-8 Assumption 3: 不含尸检数据; 尸检按 PR 域建议处理 | DD/assumptions.md:19 | 否 | 是 | 是 (3.) | 逐字 |
| 5 | ig34_p0185_a004 | p185:5 Ex2: 受试者死亡也作为退出原因在 DS 中表示 | DD/examples.md:43 | 否 | 是 | 是 (## Example 2, dd.xpt 后 ds 前) | 逐字 (直撇号, 同 PDF) |
| 6 | ig34_p0184_a006 | p184:11-13 Assumption 5: 可加 identifiers/timing/qualifiers, 但 20 个 qualifier 一般不用 | DD/assumptions.md:23 | 否 | 是 | 是 (5.) | 20 项列表顺序逐项一致 (--SPEC 跨行连字符已正确合并) |
| 7 | ig34_p0184_a008 | p184:15 标签 "Example 1" | DD/examples.md:3 | 否 | 是 | 是 | `## Example 1` |
| 8 | ig34_p0184_a022 | p184:30 标签 "Example 2" | DD/examples.md:25 | 否 | 是 | 是 | `## Example 2` |
| 9 | ig34_p0184_a005 | p184:9-10 Assumption 4: DD 检测/结果分 codelist; 关联见 DD codetable + CT URL | DD/assumptions.md:21 | 否 | 是 | 是 (4.) | 逐字; 改后 "codetable" 与 PDF 一致 (原 KB "codeable" 已修), URL 完整 |
| 10 | ig34_p0185_a005 | p185:6 Ex2 "Rows 1-2: Show typical protocol milestones and disposition events." | DD/examples.md:45 | 否 | 是 | 是 (Ex2, ds.xpt 前) | 逐字 (标签加粗为 KB 格式惯例) |

**本批计分样本 10: 独有丢失 0 / 忠实度错误 0 → 抽检 PASS.**

### 旁证
- P 全 19 原子机械匹配 (弯撇号→直, 去 `**`, 去列表号, 空白归一; scratch `mech.txt`): **19/19 HIT** DD/{assumptions,examples}.md.
- Spec 首句 `assumptions.md:11` ↔ p183:9 逐字; 3 个小标题 `DD – Description/Overview / Specification / Assumptions` 对应 p183:2, :8, p184:1 (PDF 原标题, 导航).
- 授权范围: `git diff HEAD -- knowledge_base/domains/DD/` 仅 assumptions.md (+13/−1): Description 2 段 + Specification 标题/首句 + Assumptions 标题 + assumption 4 一词 (codeable→codetable, 逐词修授权内); examples.md/spec.md 未改. 无授权外改动.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → 42 (基线 42).
- 对照 writer 报告 (判后): 与 writer F-1 (attempt 2 已修)、F-2 (Ex1 弯撇号全库惯例)、F-3 (spec 表 → O15) 一致; 本 auditor 无新增发现.

### G-TB8
- trace `T2.B-DD`: writer `oh-my-claudecode:executor` a1 04:53:07Z / a2 04:53:54Z, reviewer `oh-my-claudecode:code-reviewer` a1 04:56:12Z PASS; 无 `agent: main` 记录 (grep 计数 0).
- 时序: DD/assumptions.md mtime 04:53:39Z < reviewer 04:56:12Z (终态经 reviewer); examples.md mtime 2026-11-25 (未改). md5 assumptions `78b98f31dca3afc892e57033dc255b01`, examples `e890adecdf01c175491af14e6cfcf1aa`.

**结论: PASS** (丢失 0 / 忠实 0; G-TB8 OK).
