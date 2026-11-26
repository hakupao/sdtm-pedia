# T2 B-model05 — auditor (Rule A 独立抽检)

## attempt 1

- auditor: `oh-my-claudecode:verifier` (opus); 与 writer (executor) / reviewer (code-reviewer) 不同. 先独立判 (抽样 + 全扫 + 渲染), 判完才读 writer checkpoint 对照.
- 对象: `knowledge_base/model/05_study_level_data.md` (唯一 kb_file), `git diff HEAD` = `111 insertions(+), 74 deletions(-)`; md5 `b01d929e0c3718c8d176d90f7c4c598d` (= writer attempt 2 终态 md5, reviewer PASS 在其后).
- 源: SDTM v2.0 (`source/cdisc/SDTM_v2.0.pdf`), §5 完整页范围 sv20 p51-63 (主控指定; batch json pdf_pages 仅 [51,56]).
- scratch S = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-model05_auditor`

### 抽样命令 (t2_auditor_v1.0 脚本, 2 处按主控指令改动)
- 在 `.work/10_tier_b_repair` 下运行 v1.0 抽样脚本, b=`B-model05`, seed=`20261126`; 改动: (1) 页集合 `pages = set(range(51, 64))` 代替 `J["pdf_pages"]`; (2) 原子前缀固定 `"sv20"`. 输出 `$S/sample.json`.
- 结果: **C=5, P=45, N=10** (从 C 抽 5, P−C 抽 5). P 剔除 X (IE/ATOM_ERR/FIGURE/ledger IE) 12 条 (p52 a009; p53 a006/a007/a008; p54 a004/a005; p55 a015; p56 a003/a004/a005/a021; p58 a010) — 正是 writer R3 补回的旧 IE 句, 故另做下方 100% 全扫覆盖.

### 样本判定

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | sv20_p0056_a020 | p56:43-45 TD 使基于 SDTM 评估 assessment time bias 成为可能 (比较计划 vs 实际) | model/05:160 | 否 | 是 | 是 (TD 节, 首句后段) | 逐字 |
| 2 | sv20_p0056_a022 | p56:46-47 为 RECIST / PFS 终点研究开发 | model/05:160 | 否 | 是 | 是 | 逐字 |
| 3 | sv20_p0051_a008 | p51:14-15 列表项 "Planned sequences of reproductive stages (animal DART…; Section 5.1.3…)" | model/05:17 | 否 | 是 | 是 (§5.1 列表第 3 项) | 括注已补, 逐字 |
| 4 | sv20_p0056_a019 | p56:43 肿瘤研究中依从评估时间表以降低 assessment time bias | model/05:160 | 否 | 是 | 是 | 逐字; 与 :158 首句分段, 对应 PDF p56:41-43 段落断开 |
| 5 | sv20_p0051_a013 | p51:20-21 Trial Design 域定义研究特定术语 (e.g. arms/visits/eligibility) | model/05:23 | 否 | 是 | 是 (§5.1 列表后) | e.g. 括注已补, 逐字 |
| 6 | sv20_p0054_a020 | p54:40-41 Trial Repro Paths 描述每条 repro path 的阶段顺序 + repro phase/参考起始日 | model/05:113 | 否 | 是 | 是 (TP 节, Note 后) | 句首主语 "Trial Repro Paths" 已恢复 |
| 7 | sv20_p0052_a008 | p52:21-23 为复杂设计允许分支规则与 transition 规则 | model/05:47 | 否 | 是 | 是 (TA 节) | 逐字 (跨行合并) |
| 8 | sv20_p0054_a008 | p54:13 Trial Repro Stages 描述唯一 repro stage + 描述/代码/起止规则 | model/05:95 | 否 | 是 | 是 (TT 节) | 主语已恢复 |
| 9 | sv20_p0051_a010 | p51:17 列表项 "Study eligibility criteria (Section 5.1.5…)" | model/05:19 | 否 | 是 | 是 | 未改原子 (对照), 逐字 |
| 10 | sv20_p0057_a013 | p57:55-56 TM 用于描述疾病过程中预期发生的观察/活动, 其时间点为研究关注 | model/05:178 | 否 | 是 | 是 (TM 节) | 逐字 |

**独有丢失 0 / 10, 忠实度错误 0 / 10, 位置错误 0 / 10.**

### 100% 全扫 (超出 N=10, 覆盖 R3 补回的 14 条旧 IE 句)
- 正向: `python3 -I $S/sweep.py` (repo 根; 归一化空白/破折号/引号/星号, 原子 verbatim 子串匹配 KB 全文) → sv20 p51-63 非表格原子 74 条 (SENTENCE/LIST_ITEM/NOTE/HEADING) **74 命中**; MISS 仅 HEADING 节号标题 (O35 主控裁定不改) + TABLE_ROW/HEADER (KB 表为 5 列摘要, 表格由 reviewer 全检) + 2 FIGURE. 14 条旧 IE (p52 a009; p53 a006-a009; p54 a004/a005; p55 a013/a015; p56 a003-a005/a021; p58 a010) 全部逐字命中且在 PDF 所属节.
- 原子外补核: `awk` 抽 p51-63 layout 文本中表格外全部行 (命令见 `$S`; 表头行到下一 `5.x` 标题之间视为表格) 目视逐句对 KB: 全部叙述句、3 处列表、3 处 Note 均在 KB 对应节且顺序一致, 无原子漏抽导致的缺口.
- 反向: `python3 -I $S/rev.py` (KB 非表格行按句切分 → 子串查 p51-63 PDF 文本) → 不命中仅: :1/:3 标题与 Source 导航, `## Overview`/`## 5.1 Trial Design Model`/13 个 `### Xxx (XX)` 域标题 (O35), 4 条 D6 `> KB note (not in SDTM v2.0): **Structure:**` (TX :72 / TS :213 / DI :261 / OI :299), 2 条 D6 Mermaid 注 (:279/:317) 与 Mermaid 代码. **KB 自造或改义句 0.**

### 删除清单抽核 (主控要求 ≥5; 实核 8 条)
命令: 对每条删除文本 `grep -c -F "<短语>"` p51-63 PDF 文本与当前 KB, 再 `grep -n -F` 核取代的 PDF 原句在 KB.

| D# | 删除内容关键短语 | PDF p51-63 命中 | KB 现存 | 取代的 PDF 原文在 KB | 判 |
|---|---|---|---|---|---|
| D-3 | "(TDM)" | 0 | 0 | :13 "The Trial Design Model defines…" (p51:10) | KB 自加缩写, 删正确 |
| D-4 | "basic building blocks" (TE 改写) | 0 | 0 | :31 "…periods of times through which subjects pass…" (p51:26) | 改写残留, 删正确 |
| D-7 | "pooled analysis" (TX 改写) | 0 | 0 | :68 Trial Sets 3 句 (p53:22-24) | 改写 + PDF 无的 "pooled analysis groups" (与 "planned groups" 不符), 删正确 |
| D-12 | "planned Visit per Arm" (TV Structure) | 0 | 0 | :140 a004/a005 (按 arm 分记录仅在访视因 arm 而异时) + :142 PDF 表题 | KB 无条件写法与 PDF 条件情形矛盾 → D2 删正确 |
| D-14 | "types of disease milestones" (TM 改写) | 0 | 0 | :178 (p57:55) | 删正确 |
| D-21 | "Study Reference datasets provide" | 0 | 0 | :254-257 (p61) 2 句 + 2 项列表 | 删正确 |
| D-22 | "Used to identify the devices" | 0 | 0 | :263 (p61) a007/a008 | 删正确 |
| D-23 | "bacteria and viruses" (OI 改写) | 0 | 0 | :301 (p62) a003/a004, *taxa* 斜体同渲染图 | 改写残留删除; "such as bacteria and viruses" 为 PDF 无的举例, 按 dispatch "R2 残留旧改写句 (行不承载其他原子) → 删" 处理, 可接受 (观察项, 不计失败) |

8/8 确认: 删的是 KB 改写/自加内容, PDF 原文均在 KB 所属节. (TX/TS Structure D-8/D-19 已在 writer a2 撤回删除, 现为 D6 KB note :72/:213, 核在.)

### Label 格对渲染图 (主控要求 ≥4; 实核 11/11)
`pdftoppm -f N -l N -r 110 -png source/cdisc/SDTM_v2.0.pdf $S/rN` (N=53,58,59,60,62), 逐格目视:
- p53: TXPARM "Trial Set Parameter" = KB :82 ✓; TXVAL "Trial Set Parameter Value" = :83 ✓
- p58: IETESTCD "Inclusion/Exclusion Criterion Short Name" :200 ✓; IETEST "Inclusion/Exclusion Criterion" :201 ✓; IECAT "Inclusion/Exclusion Category" :202 ✓; IESCAT "Inclusion/Exclusion Subcategory" :203 ✓
- p59: TIRL "Inclusion/Exclusion Criterion Rule" :204 ✓; TSPARM "Trial Summary Parameter" :222 ✓; TSVCDREF "Name of the Reference Terminology" :226 ✓
- p60: TSVCDVER "Version of the Reference Terminology" :227 ✓
- p62: NHOID "Non-Host Organism Identifier" (大写 H) :309 ✓
- 附带: p62 DI Concept Map 渲染图 6 节点 5 边 (involves / has one or more / has / is represented using / has) 与 KB :281-295 Mermaid 一致; 题注 "Concept Map." 句点同 PDF.

### 主控裁定不改项 (不计本批)
O35: 既有标题/层级、TT/TP Notes 列、TS Usage Restrictions、Role 括注.

### G-TB8
- `grep -n "B-model05" .work/10_tier_b_repair/trace.jsonl`: executor a1 subagent_done 04:41:36Z, executor a2 04:47:00Z, code-reviewer a1 PASS 04:50:52Z (在 writer 终态之后); `agent: main` 写本批 KB 记录 0 条. 当前 KB md5 = writer a2 终态 md5 → reviewer 审的即终态. **PASS.**

### 其他
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (= 基线).
- 范围外发现: 无.
- 对照 writer checkpoint: 独立结论与 writer 声明一致; 未发现 writer 未声明的改动.

### 结论
独有丢失 0, 忠实度错误 0 → **PASS**.
