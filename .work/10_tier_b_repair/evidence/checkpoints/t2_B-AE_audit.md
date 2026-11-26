# T2 B-AE auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

**verdict: PASS** — 独有丢失 0/10, 忠实度错 0; G-TB8 通过.

### 抽样 (repo 根复跑)
- 命令 = `subagent_prompts/t2_auditor_v1.0.md` 抽样块, `b="B-AE"; seed=20261126`; 输出 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-AE_auditor/sample.json`
- C=5 (t2_recheck p139_a010 为 TABLE_ROW, 不计 prose), P=45, N=10; C 抽 5 + P−C 对照 5.
- KB 基线: `git diff 3c716a7 -- knowledge_base/domains/AE/`; 当前 md5 assumptions `71ce6c47…`, examples `f8dd2e92…` = writer 续 后声明值 (reviewer 续签之后无 KB 改动).
- 判法: 先独立判 (PDF txt + 渲染图 110dpi p139/p141/p142, `pdftoppm -f N -l N -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf"`), 判完才读 writer/reviewer 报告.

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0142_a010 | 142:Ex5 叙述 "…hip joints…novel material…" 含 AEUNANT 分句 | examples.md:71 | 否 | 是 | 是 | 归一后逐字; AEUNANT 分句已补 |
| 2 | ig34_p0142_a012 | 142:Ex5 Row 2 "Osteomyelitis right hip…probably related to the event" | examples.md:75 | 否 | 是 (PDF_TYPO T-3) | 是 | "are specified" 已修; "event"→"device" 独立复核成立 (见下) |
| 3 | ig34_p0133_a021 | 133:AE Description/Overview 定义句 | assumptions.md:5 | 否 | 是 | 是 | 新 `## AE – Description/Overview` 下逐字 |
| 4 | ig34_p0141_a016 | 141:Ex3 叙述 "…included in the study only once…Events or Interventions…" | examples.md:37 | 否 | 是 | 是 | 逐字 |
| 5 | ig34_p0141_a007 | 141:Ex2 叙述 "…several visits…via prespecification…" | examples.md:21 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0139_a015 | 139:7e "structure of the AE domain is 1 record per…" | assumptions.md:57 | 否 | 是 | 是 | 未改动对照, 逐字 |
| 7 | ig34_p0139_a007 | 139:7a "If categories of serious events…may be null:" | assumptions.md:43 | 否 | 是 | 是 | 冒号 + 另起段 = PDF 版面 |
| 8 | ig34_p0139_a013 | 139:7c "Other Medically Important…AESOSP…Section 8.4…Appendix C1" | assumptions.md:55 | 否 | 是 | 是 | AEOSOSP→AESOSP 已修; 两处交叉引用在 |
| 9 | ig34_p0133_a017 | 133:§6.2 Events 类域列表项 "Medical History (MH)" | — (AE kb_files 外) | 范围外 | — | — | 属 §6.2 引言, 非 §6.2.1 AE; KB 全库无 "correspond to the Events class" 引言+列表 → 范围外发现 OOS-1, 不计本批 |
| 10 | ig34_p0141_a009 | 141:Ex2 Row 3 "…headache…null value for AEPRESP" | examples.md:25 | 否 | 是 | 是 | 未改动对照, 逐字 |

- 独有丢失数 0; 忠实度错误数 0 (样本 9 个 in-scope + 1 范围外).

### 补充: p133-142 §6.2.1 prose 全量归一子串扫 (非抽样, 辅助)
- 未命中 2: ig34_p0137_a010 (spec 表脚注 → spec.md, 范围外, writer 已报), ig34_p0142_a012 (T-3 预期). 其余全部逐字在 AE 两文件.

### 10 格随机复核 (rng seed 20261126, 从 Ex3/Ex5/Ex6 数据行抽, 对渲染图 p141/p142)
| 表 | KB 行 | 列 | KB 值 | PDF | 结果 |
|---|---|---|---|---|---|
| Ex6 | 97 | AESEV | MODERATE | MODERATE | ✓ |
| Ex6 | 97 | DOMAIN | AE | AE | ✓ |
| Ex3 | 45 | AESER | (空) | 空 | ✓ |
| Ex3 | 46 | AEDECOD | Vomiting | Vomiting | ✓ |
| Ex5 | 82 | AESCONG | N | N | ✓ |
| Ex5 | 82 | AERLPRT | N | N | ✓ |
| Ex5 | 81 | AESTDY | 5 | 5 | ✓ |
| Ex5 | 82 | AESHOSP | Y | Y | ✓ |
| Ex3 | 46 | AEDTC | 2005-10-29 | 2005-10-29 | ✓ |
| Ex6 | 96 | AESDTH | N | N | ✓ |
10/10 一致. 另目视 Ex5/Ex6 全部单元格与 p142 一致 (除 T-1/T-2 登记格); Ex1 r3 AESHOSP/AESLIFE 列位、AEENRF "AFTER" 与 p141 一致.

### 两条改值 PDF_TYPO 独立复核
- **T-1** Ex5 r1 AEENDTC (PDF 2014-04-26 → KB 2018-04-26): 同行 AESTDTC 2018-04-21 = AESTDY 5 ⇒ Day1 = 2018-04-17; AEENDY 10 ⇒ 2018-04-26, 与 PDF 月日吻合, 且 2014 早于起始日不可能; r2 2018-05-01 = Day 15 同一 Day1 印证 → 单值可定, 合 dispatch "正确值能由 PDF 自身确定" → **成立**.
- **T-3** Ex5 Row 2 "related to the event" → "device": 同句主语 "The device was removed"; 同行 AERLDEV = PROBABLE, AEACNDEV = REMOVED, AERLPRC = N, AERLPRT = N ⇒ "probably related" 只能指器械; "AE related to the event" 自指无义; Ex6 Row 2 平行句 "probably related to the device" → **成立** (改词判断, 信心中高; 已登记 T-3, 建议 T4 用户裁定清单里一并列示).
- 对照: Ex6 r2 AEENDTC 2014-11-27 照录 (U-2) 处理正确 — 按 Day 推算 11-28 ≠ 11-27, 非单值, 不应改.

### 删除行核对 (无 PDF 内容丢失)
- assumptions CRF 行: 删去 "…or prolongation of existing hospitalization / Persistent… / Congenital… / Other medically important…" 均不在 PDF; 现值 = p139 "[ ] Fatal [ ] Life-threatening [ ] Inpatient hospitalization… [ ] etc." (D2/O11).
- "If yes, check all that apply:" 冒号去除 = PDF; AESOCD→AESOCCD = p140; "domain, see"→"; see" = p138.
- examples: Ex1 旧错位值、"FOR 5 HOURS"、"AFTER TREATMENT"; Ex3 旧表头 (缺 AEACN/AEREL/AESTDTC/AEENDTC, AESTDY); Ex5 旧 AEREL 列 / T992 / 2015 日期; Ex6 旧 1001 / 2013-2014 日期 / "CAUSAL RELATIONSHIP" — 均为 KB 错值, PDF 无对应 → 无丢失.
- "the AE was related" → "it was related", "by prespecification" → "via", "Events and" → "Events or" = PDF 原词.

### AE fp 回归
- 依 reviewer 复跑 fp_match: p133-145 回归 0 (本 audit 未重跑 fp_match; 上表全量子串扫为独立旁证).

### G-TB8
- trace.jsonl: writer `oh-my-claudecode:executor` subagent_done 02:16:40 (L102) + 续 02:22:52 (L114); reviewer `oh-my-claudecode:code-reviewer` PASS 02:21:21 (L113) + 续签 PASS 02:23:33 (L116) — reviewer 签字晚于 writer 最后改动 ✓.
- 无 `"agent": "main"` 写 B-AE KB 记录 ✓; 当前 md5 = writer 续 声明值 ✓.

### 范围外发现
- OOS-1: §6.2 "Models for Events Domains" 引言句 + 7 项 Events 类域列表 (p133, 如 ig34_p0133_a017) 在 KB 全库未见 (`grep -rn "correspond to the Events class" knowledge_base` 空), triage_merged 亦无条目 → 不属 AE kb_files, 交主控定归属 (疑 §6.1/6.3 等类引言同型缺失, 建议 O 项全库扫).
