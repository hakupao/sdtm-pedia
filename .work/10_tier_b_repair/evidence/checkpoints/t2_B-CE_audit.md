# T2 B-CE — Rule A 独立抽检 (auditor)

## attempt 1

- auditor: oh-my-claudecode:verifier (opus); 独立判后才读 writer/reviewer 结论 (只用 trace 做 G-TB8)
- base: `git diff HEAD -- knowledge_base/domains/CE/` (assumptions.md +10/-2, examples.md 19 行改); spec.md 未改
- 抽样脚本: t2_auditor_v1.0 原命令, 唯一改动 `J["pdf_pages"] = list(range(148, 156))` (brief: 本域完整 PDF 节 p148-155); 脚本存 scratchpad `t2_B-CE_auditor/sample.py`
  复跑: `python3 -I <scratch>/t2_B-CE_auditor/sample.py` (repo 根执行)
- seed = 20261126; C = 1; P = 50; N = 10 (C 抽 1 + P−C 抽 9)
- PDF 真值: `work/pdf_pages/ig34_p0148..0155.txt` + `pdftoppm -r 110` 渲染 p151/p152/p153 (源 `source/cdisc/SDTMIG v3.4 (no header footer).pdf`)

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0148_a015 (C) | p148:21 CE Description/Overview 句 "An events domain … not be classified as adverse events." | CE/assumptions.md:5 | 否 | 是 (逐字) | 是 (## CE – Description/Overview, 在 Specification / Assumptions 前, 同 PDF 顺序) | REAL_GAP 已补 |
| 2 | ig34_p0152_a0029 | p152:39-40 Ex3 引言第 2 句 (bone-fracture events pre-study 5 年 + on-study) | CE/examples.md:68 | 否 | 是 (逐字) | 是 (Example 3) | |
| 3 | ig34_p0148_a012 | p148:16-17 BE References 第 2 条 (Cerkovnik … doi) | BE/examples.md:161 | 否 | 是 (逐字) | 是 (BE, 本批 kb_files 外对照) | 对照原子, 不计本批 |
| 4 | ig34_p0154_a0016 | p154:28 suppce 前句 "causes of the fractures … supplemental qualifiers" | CE/examples.md:127 | 否 | 是 (逐字) | 是 (ce.xpt 后 suppce 前) | |
| 5 | ig34_p0154_a0025 | p154:38-39 pr.xpt Row 1 说明 (PRSPID←MHSPID; PRDTC=MH 收集日=MHDTC) | CE/examples.md:140 | 否 | 是 (逐字) | 是 | |
| 6 | ig34_p0150_a008 | p150:23-25 Assumption 1b vaccine trials; flags 顺序 --SCAN, --SCONG, --SDTH, --SHOSP, --SDISAB, --SLIFE, --SOD, --SMIE | CE/assumptions.md:15 | 否 | 是 (逐字, 含 flag 顺序) | 是 (1b) | 原子 verbatim 有抽取错 ("signs of symptomatology", "--SCAT/--SCOD/--SDHSP"), 以 PDF 原页为准; KB=PDF |
| 7 | ig34_p0151_a0029 | p151:35-36 Ex2 引言第 1 句 (prespecified + specifying additional events) | CE/examples.md:33 | 否 | 是 (逐字) | 是 | |
| 8 | ig34_p0151_a0031 | p151:36-37 Ex2 "Although this example CRF shows only 1 row …" | CE/examples.md:33 | 否 | 是 (逐字) | 是 | |
| 9 | ig34_p0154_a0023 | p154:36 "therapeutic measures … Procedures (PR) domain." | CE/examples.md:138 | 否 | 是 (逐字; 同段后续 PRSTDTC 句亦在) | 是 | |
| 10 | ig34_p0151_a0007 | p151:11 Ex1 引言第 1 句 (prespecified events, not reportable as AEs) | CE/examples.md:5 | 否 | 是 (逐字) | 是 | |

**独有信息丢失 0/10; 忠实度错误 0/10.**

### 补充核查
- **P 全 50 原子机械匹配** (归一空白/引号/Row 前缀后子串比对全库): 44 精确命中 (CE 40 + BE 3 对照 + 1 已核), 6 未命中逐条判:
  - p0150_a007 / a008 / a009 = 原子 verbatim 抽取错 (a007 "considered as" vs PDF "considered to be"; a009 "a record in" vs PDF "a reason for study discontinuation in"); 对 PDF p150:19-29 人工比 1a/1b/1c → KB 逐字一致.
  - p0152_a0019 = PDF 自身 "Variables,for" 缺空格, KB "Variables, for" (examples.md:54), 合理值, 不计.
  - p0155_a0015 = **DS** Description/Overview 句 (p155:18), DS 三文件皆无 → **范围外发现** (kb_files 外, 不计本批; 已被 O16 全域 Description 扫描覆盖, 主控可在 O16 下点名 DS).
- **1b / 1c 逐字核** (p150:23-29 vs assumptions.md:15-16): 机械子串比对 True ×2; 1b flag 顺序 SDTH→SHOSP→SDISAB 与 PDF 一致 (HEAD 原为 SDISAB 在前); 1c "would be reported in AE; death would also be a reason for study discontinuation in the Disposition (DS) domain." 恢复 PDF 原文 (D-2) 无增删.
- **Spec 首句** p148:23 "ce.xpt, Clinical Events — Events. One record per event per subject, Tabulation." = assumptions.md:9 逐字 (True); 三标题 `CE – Description/Overview` / `CE – Specification` / `CE – Assumptions` 与 PDF p148:20/22, p150:15 一致.
- **3 张 CRF 表对渲染图 (各 ≥3 格)**:
  - Ex1 (p151 渲染): Rash/Did it occur? = "No Yes" (PDF 无单选符号) ✓; Start Date 列空 ✓; Conjunctivitis 行 "No Yes" + 空 ✓; 表头 3 列 ✓. "Record start dates …" 为 PDF 表内标题行, KB 置于表上方段落, 文字逐字 ✓.
  - Ex2 (p152 渲染): Nausea "( ) Yes ( ) No" (PDF ○) ✓; Date Started "__/___/____ (dd/mmm/yyyy)" ✓; Other, Specify: 第 2 列为下划线 "___" ✓; Severity "( ) Mild ( ) Moderate ( ) Severe" ✓.
  - Ex3 (p153 渲染): Date of collection / Date of fracture = "--/---/--" ✓; therapeutic measures 复选 "[ ] Casting/immobilization [ ] Traction [ ] Surgery" (PDF □) ✓; laterality "Left/Right/Not applicable" ✓.
- **Ex2 ce.xpt Row 1 CEENDTC** = 2005-10-12 (p152 渲染) ✓.
- **USUBJID `ABC -US-701-002`** (mh/ce/pr 共 8 格) 与 p153-155 渲染/文本一致 = 照录 T-2 (T4 用户裁定); fp p153-155 回归按指令为照录预期, 不计.
- **授权范围**: assumptions.md 仅加 3 个 PDF 原有小标题 + Description 句 + spec 首句 + 1b/1c 修订; spec.md 未改 (git diff 空).
- **观察 (不计)**: examples.md:7/39/70 表前标签 "CE Example 1 — Prespecified Clinical Events" 等副标题为 KB 自写导航 (PDF 仅 "CRF"); Ex3 CRF 表头 "Question | Response Options" KB 自写 (PDF 首行 "Bone Fracture Assessment"). 均为 HEAD 既有、属 D6 纯导航豁免范围, reviewer 已处理, 列出供主控知悉.
- check_links: `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42 (= 基线)
- **G-TB8**: trace.jsonl 本批有 writer `oh-my-claudecode:executor` a1 (04:54:16Z) / a2 (05:02:09Z), reviewer `oh-my-claudecode:code-reviewer` a1 CONDITIONAL (05:00:55Z) / a2 PASS (05:03:32Z); 无 `agent: main` 的 B-CE 记录; KB mtime assumptions 04:52:45Z / examples 05:01:42Z 均早于 reviewer a2 PASS → 终态经 reviewer. md5 assumptions 3f9e0f67…, examples 5dbcacf1….

**判定: PASS** (丢失 0, 忠实错 0; 范围外 1 = DS Description 句, 归 O16)
