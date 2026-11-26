# T2 B-DM auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus; 先独立判, 判完才对照 writer/reviewer 报告)

- 命令: `t2_auditor_v1.0.md` 抽样脚本, 两处按主控口径调整: `files` = batch kb_files ∪ {`knowledge_base/domains/DM/assumptions.md`} (主控授权, 本批实际改动); `J["pdf_pages"] = range(62, 80)` (DM 全节 p62-79; batch json 漏 p79, F-4/O34). 其余逐字不变. 输出 scratch `t2_B-DM_auditor/sample.json`.
- seed = 20261126; C = 1 (ig34_p0064_a012); P = 191; N = min(30, max(10, 1), 191) = 10 → C 1 + P−C 9.
- 样本: p0064_a012, p0071_a020, p0065_a008, p0075_a030, p0077_a019, p0065_a021, p0069_a009, p0070_a007, p0075_a034, p0067_a009.
- 真值: `pdftotext -layout` + `pdftoppm -r 110` p62-79; Ex5/Ex7 图另 300/200dpi 裁剪.

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0064_a012 | p64:40-42 spec 表脚注 2: FDA race/ethnicity 指南文献 + URL | — | — | — | — | **不计** (DEFERRED_O26, 主控裁定并入 spec 脚注全域扫描; 归属 spec.md 非本批授权). 不补抽, 保持种子可复跑 (同 B-CV/B-SM 先例) |
| 2 | ig34_p0071_a020 | p71 Ex4 图 BLACK 子图选项 "BARBADIAN" | DM/examples.md:136 (Mermaid SC3), :192 (CRF Metadata), :172 (KB note) | 否 | 是 | 是 (## Example 4) | 子类顺序 AFRICAN…BLACK CENTRAL AMERICAN 与图一致 |
| 3 | ig34_p0065_a008 | p65:7-8 Assumption 2: 受试者偶尔在试验中换中心 | DM/assumptions.md:15 | 否 | 是 | 是 (Assumptions 2.) | 逐字 |
| 4 | ig34_p0075_a030 | p75 Ex6 图 BLACK 子图选项 "AFRICAN CARIBBEAN" | DM/examples.md:312 (Mermaid SC2), :342 (CRF Metadata) | 否 | 是 | 是 (## Example 6) | 与 p75 图 / p77 表一致 |
| 5 | ig34_p0077_a019 | p77 末段: Collected race (每受试者具体子类) 入 SUPPDM 以保自我认同/国别要求 | DM/examples.md:362 | 否 | 是 | 是 (Ex6, dm.xpt 后 suppdm 前) | 逐字 (区别于 Ex4 :212 的 "(or subcategories) selected by" 版本, 各照 PDF) |
| 6 | ig34_p0065_a021 | p65:33-34 Assumption 4b: 多阶段分配, see Section 7.2.1, Trial Arms, Example Trial 3 | DM/assumptions.md:25 | 否 | 是 | 是 (4.b) | 逐字, 交叉引用完整 |
| 7 | ig34_p0069_a009 | p69 Ex3 Row 3: Subject "003" 随机到 drug A 但接受 drug B | DM/examples.md:72 | 否 | 是 | 是 (## Example 3) | 逐字 (含引号 "003") |
| 8 | ig34_p0070_a007 | p70:7-8 Ex4 引言: 因篇幅只显示部分选项 ("is shown") | DM/examples.md:109 | 否 | 是 | 是 (## Example 4) | 逐字; Ex6 :286 为 "are shown" 照 p75 |
| 9 | ig34_p0075_a034 | p75 Ex6 图 BLACK 子图选项 "BLACK CENTRAL AMERICAN" | DM/examples.md:312, :342 | 否 | 是 | 是 (## Example 6) | 一致 |
| 10 | ig34_p0067_a009 | p67:12-14 Assumption 7b: 该对变量保证审评者总能引用首末研究暴露参考期 | DM/assumptions.md:48 | 否 | 是 | 是 (7.b) | KB 与 PDF 逐字 ("…exposure reference period"); 原子文本漏 "reference" = 原子抽取错, 以 PDF 页为准 |

**本批计分样本 9: 独有丢失 0 / 忠实度错误 0 → 抽检 PASS.** (a012 DEFERRED_O26 不计.)

### 旁证: P 全 191 原子机械匹配 (空白/引号归一, 列表号去除; scratch `mech.txt`)
- 162 精确命中 DM/{assumptions,examples}.md.
- 9 命中 SE/ (p79 a003-a011, §5.3 SE): 仅因页范围 62-79 落入 P, 属 SE 域, 非本批.
- 20 未命中, 逐条处置:
  - a012 (p64): DEFERRED_O26 (同上).
  - p66 a009/a010/a018/a020, p67 a009/a010: 原子抽取错 (p66 为 p67 句的重复/错字: "exposure period" 漏 reference、"SSTDTC" 应 SESTDTC、"RFICIDITC"、"RFPENDTC will be the last date of any record" 两句拼接); KB :48/:50 与 p67:12-29 PDF 原文逐字一致.
  - p69 a002 ("arm A" vs PDF p68 Row 1 "arm "Drug A""), a004 ("ACTRMD" vs PDF "ACTRMCD", KB 按 T-3 写 ACTARMCD), a011 ("assignment" vs PDF "assignments", KB :72 = PDF); p78 a004 ("designated 1 race" vs PDF p78 "selected", KB :366 = PDF): 均为原子抽取错.
  - p70 a012-a018 ("RAC601 BAC - …"): 图内 OCR 噪声 (RACE01 + RACE 标签), 非 PDF 叙述; p75 a023/a035 "<RACEC codelist>": 图内标注, KB 由 CRF Metadata "(RACEC)" 列承载, 非独有信息.
  - 结论: P 内 DM 叙述 0 实际缺失.

### 额外必查 (a): 两张 CRF Metadata 表对渲染图逐格 (≥5 格/表)
- Ex4 (KB :178-194 ↔ p72-73 渲染): ① RACE02 Question Text = 全句 "Which of the following racial designations best describes you? (More than one choice is acceptable.)" ✓; ② RACE02 CRF Completion Instructions = "Study participants should self-report race, with race being asked about after ethnicity." ✓; ③ CRACE01-04 Question Text 为短句 (无 "(More than one…)") ✓; ④ CRACE01-04 Permissible Values 末尾 "CENTRAL AMERICAN INDIAN;" ✓ (CRACE05-10/11-17/18-21 同样末尾 ";") ✓; ⑤ 分隔行 "If study participant answered: **AMERICAN INDIAN OR ALASKA NATIVE**" (无 "the", 值加粗) ✓ ×4; ⑥ CRACE05-CRACE10 Hidden = "CRACE05-CRACE10" ✓, 其余行 Hidden 空 ✓; ⑦ Order 1-7, 10-13 ✓; ⑧ RACE04 PV "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER" ✓; ⑨ CRACE 行 SDTM Target Mapping "For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and …choice value." ✓; List Style 全 checkbox ✓.
- Ex6 (KB :330-342 ↔ p76-77 渲染): ① Order RACE01-07 = 3-9 ✓, CRACE05-10 = 11, CRACE11-17 = 12 ✓; ② 分隔行 "If the study participant answered: **ASIAN**" / "**BLACK OR AFRICAN AMERICAN**" (有 "the") ✓; ③ CRACE05-10 Hidden 空 (p77, 与 Ex4 不同) ✓; ④ CRACE11-17 PV 末尾 "BLACK CENTRAL AMERICAN;" ✓; ⑤ RACE02 Question Text 全句 ✓; ⑥ CRACE Question Text 短句 ✓; ⑦ Type Text / Target SUPPDM.QVAL / CT (RACEC) ✓.
- 0 差.

### 额外必查 (b): 4 个 Mermaid 逐个对 PDF 图核逻辑 (判据: 分支/顺序与 PDF 不矛盾; 图已在 D6 note 下)
| 图 | PDF | KB Mermaid | 判定 |
|---|---|---|---|
| Ex4 (:113-149) | p70-71: RACE01-07 七题 (顺序 AI/AN, ASIAN, BLACK, NHOPI, WHITE, NOT REPORTED, UNKNOWN) + 4 子图, 各以 "If the study participant answered: X" 引出 (X = AI/AN, ASIAN, BLACK, WHITE) | 7 选项同序; R1/R2/R3/R5 "If selected" → SC1-4 (CRACE01-04/05-10/11-17/18-21, 子类同序); R4/R6/R7 无子类 | 一致 — 条件边由 PDF 子图小标题直接支撑 |
| Ex5 (:234-253) | p74: ETHNIC 问句 + "O Hispanic or Latino" / "O Not Hispanic or Latino"; 5 个子类 checkbox 位于 Not Hispanic 选项下; CETHNICN 标签 + 红框 SUPPDM.QVAL WHERE SUPPDM.QNAM = "ETHNICN" (版面在两选项之间); 橙框 "VALUE OF "N"…INCREMENTAL SEQUENCE." 在问句栏 | H/NH 两选项; NH -.->Subcategories SC (含 CETHNICN 映射 + 5 子类同序); Q -.- NOTE | 一致 — 子类挂 NH 有版面锚 (checkbox 缩进在其下) 与 dm.xpt ETHNIC = NOT HISPANIC 支撑; CETHNICN 徽标版面位置略松, 归入子类节点不矛盾 |
| Ex6 (:290-320) | p75: 同 Ex4 七题 + 2 子图 (ASIAN, BLACK) | R2 → SC1 (CRACE05-10), R3 → SC2 (CRACE11-17) | 一致 |
| Ex7 (:382-412) | p78: 一题 7 checkbox (AI/AN, Asian, Black, NHOPI, White, Unknown, Other) + 其下两独立行 "What was the other race?" (RACEOTH) / "If Unknown, please specify:" (RACEREAS) | 7 选项同序; R7(Other) -.->"If selected" OTH; R6(Unknown) -.->"If selected" UNK | **一致 (非 FAIL)** — 见下 |
- Ex7 "If selected" 裁定: 逐边看是否与 PDF 矛盾. (1) Unknown → RACEREAS: PDF 该行提示语本身即 "If Unknown, please specify:" (p78 图), 条件逻辑由 PDF 给出. (2) Other → RACEOTH: 提示语 "What was the other race?" 以选了 "Other" 为前提; p79 Row 1 叙述 "Sponsor allowed for an "Other" option…specify details are in SUPPDM" 与 p78 Row 3 "selected "Other"" 支撑该关联. 两边配对未交换 (Other↔RACEOTH, Unknown↔RACEREAS), 选项顺序与 p78 一致. PDF 版面为并列行而非箭头, 但 Mermaid 已标 D6 "KB rendering", 用条件边表达该依存不与 PDF 矛盾. → 记 LOW 观察 (同 reviewer 观察 #120), 不计 FAIL. 可选改进 (非必须): 边标签改为 PDF 原文 ("If Unknown" / "Other") 以减少 KB 推断措辞.

### 其他核对
- PDF_TYPO T-1 (p78 Row 列 "3" 重复 → KB 4)、T-2 (p68 "ISLANDERS" → ISLANDER, PDF 自身 RACE04 PV p72/p76 为单数)、T-3 (p69 "ACTRMCD" → ACTARMCD, 同页表头/Row 3) 依据均由 PDF 自身确定 ✓. Ex1 Row 3 RFXSTDTC 2006-01-16 / Row 4 AGE+AGEU 两空 对 p68 ✓.
- assumptions.md: Description/Overview 单段 = p62 逐字 ✓; `## DM – Specification` + "dm.xpt, Demographics — Special Purpose. One record per subject, Tabulation." = p62 ✓; Assumption 4 删 "as" → p65:15 "…to assign subjects to arms described below, ARM" ✓ (主控追加授权, writer a2).
- 授权范围: `git diff HEAD -- knowledge_base/domains/DM/` 仅 assumptions.md (Desc 合段 / Spec 节+首句 / asm4 一词) + examples.md; spec.md 未动 (md5 `048374a611824d45f195a6a48f296aa9`) ✓.
- D6: 4 Mermaid 前 KB note + 4 块摘要 (Ex4/Ex5/Ex6/Ex7) 均为 `> KB note (not in SDTMIG):` ✓; Ex6 摘要 ", and other categories" 已删 (与 p75 仅两组子类矛盾) ✓.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` ✓ (基线 42).

### G-TB8
- trace.jsonl T2.B-DM: writer `oh-my-claudecode:executor` a1 (04:42:45Z) + a2 (04:43:27Z) subagent_done; reviewer `oh-my-claudecode:code-reviewer` a1 PASS (04:47:49Z); 无 `agent: main` 写 KB 记录 ✓.
- 终态经 reviewer: 现 md5 assumptions `9c4d2d1d3e976f4754d1ed4ed0549298` / examples `f7a19d07341d697a93cb67dee84c780f` = writer a2 声明 = reviewer 记录值; KB mtime (assumptions 04:43:16Z, examples 04:39:59Z) 早于 reviewer checkpoint 04:47:49Z; reviewer L79 已核 a2 delta (asm4 删 "as") ✓.

**结论: PASS** (计分 9: 丢失 0 / 忠实 0; CRF 表 2×≥5 格 0 差; 4 Mermaid 逻辑一致, Ex7 "If selected" 判一致记 LOW).
