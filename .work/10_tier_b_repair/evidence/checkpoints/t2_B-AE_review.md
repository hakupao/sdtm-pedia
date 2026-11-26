# T2 B-AE reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS** (0 blocking; 2 LOW 备注; F-1 归属建议交主控)

base 3c716a7; 只审 `knowledge_base/domains/AE/{assumptions,examples}.md` (全 KB diff 中其余 6 文件属并行批 B-ch02/B-ch04/B-EG/B-GF/B-model01, 不在本批).
scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-AE_reviewer/` (渲染图 p133/139/141/142 110dpi + 220dpi 局部裁剪 ex1L/R, ex3, ex5L/R, ex6L/R, crf; scan.py)

### 命令与结果 (可复跑, repo 根)
```
S=<scratch>; python3 -I -c "...manifest..."   # 同 prompt
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  -> exit 1; AE: UNPARSEABLE 1 / OK 5 / DIFF 1; cells 361; diffs 2 (Ex5 r1 AEENDTC = T-1; r2 AEOUT = T-2)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  -> exit 1 RED; 15 回归 = p118/p215/p218/p257-263 (CP/MB/ch04 页), p133-145 回归 0 (AE 无回归)
python3 tools/check_links.py | grep "live docs"   -> broken relative links: 18668 (live docs: 42)  (≤42 ✓)
pdftoppm -f N -l N -r 220 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/hiN ; sips 裁剪后目视逐格
python3 -I $S/scan.py   # 独立双向逐句扫描 (KB 句→PDF p133-142 文本; PDF 句→KB)
```
fp 目标命中: a021/a015/a004/a007(p139)/a010(p139)/a013/a008/p141_a007/p141_a016/p142_a010 均命中 AE 目标文件; p142_a012 未命中 = T-3 预期.

### 人工逐格 (渲染图, 独立于 bbox 解析器)
| 表 | KB 行 | 结果 |
|---|---|---|
| Ex1 (p141) 表头 26 列 | :13 | 一致 (列序 AESCONG AESDISAB AESDTH AESHOSP AESLIFE AESMIE EPOCH…) |
| Ex1 r1 | :15 | 一致 (AEMODIFY HEADACHE; AEACN NOT APPLICABLE; AEREL DEFINITELY NOT RELATED; 严重性 6 列空) |
| Ex1 r2 | :16 | 一致 (BACK PAIN FOR 6 HOURS; BACK PAIN; DOSE REDUCED; PROBABLY RELATED; 13T13:05/13T19:00; 1/1) |
| Ex1 r3 | :17 | 一致 (AESHOSP Y, AESLIFE Y; AEENDTC 空; 9; AEENRF AFTER) |
| Ex2 r1-r3 | :31-33 | 一致 (r2 13T13:00; r3 AEENDTC 2005-10-21) |
| Ex3 表头 16 列 + r1-r2 | :43-46 | 一致 (AESER/AEACN/AEREL/AESTDTC/AEENDTC 空; AEDTC 2005-10-29; AEDY 19) |
| Ex4 r1-r6 | :62-67 | 一致 (r2 AEENDTC 2005-10-16) |
| Ex5 表头 29 列 | :79 | 一致; 首格 PDF 空白 → `Row` (T-4) |
| Ex5 r1 | :81 | 除 AEENDTC (PDF 2014-04-26, KB 2018-04-26 = T-1) 外一致: T002 AE 002 HipX22 1 AE0099 Twisted left ankle SPRAIN ANKLE JOINT LEFT N MILD NONE NOT RELATED RECOVERED/RESOLVED N N N N N N N Y N Y 2018-04-21 … 5 10 |
| Ex5 r2 | :82 | 除 AEOUT (PDF SEQUELLAE, KB SEQUELAE = T-2) 外一致: … REMOVED PROBABLE … N Y Y N N N Y Y N N 2018-05-01 2018-05-10 15 25 |
| Ex6 表头 25 列 | :94 | 一致 (AESCONG AESHOSP AESDISAB AESDTH…) |
| Ex6 r1 | :96 | 一致 (T001 002 AE0007 SENSOR REPOSITIONED CAUSAL … N×7 2018-09-01 2018-09-07 27 33) |
| Ex6 r2 | :97 | 一致 (T001 001 AE0049 SENSOR REPLACED AND REPOSITIONED PROBABLE … N Y N N N N Y 2018-10-24 2014-11-27 78 113) |
| CRF 表 (UNPARSEABLE) c1/c2 | assumptions:43 | "Serious?" / "[ ] Yes [ ] No" 一致 |
| CRF 表 c3/c4 | assumptions:45 | "If yes, check all that apply" (无冒号) / "[ ] Fatal [ ] Life-threatening [ ] Inpatient hospitalization… [ ] etc." 一致 |
CRF 表: PDF 无表头行, KB 首行作 Markdown 表头 + 分隔线 = 结构行 (签字).

### PDF_TYPO / U 判定 (严格口径)
| # | 判定 | 依据 |
|---|---|---|
| T-1 2014→2018 | 成立 | 同行 AESTDTC 2018-04-21=Day5 ⇒ Day1=2018-04-17; AEENDY 10 ⇒ 2018-04-26, 与 PDF 月日 04-26 完全吻合; r2 2018-05-01=Day15 同一 Day1 印证. 单值. |
| T-2 SEQUELLAE | 成立 | CT 拼写 (dispatch: PDF 自身拼错保留正确拼写) |
| T-3 event→device | 成立 (MEDIUM 信心) | 同句主语 "The device was removed"; 同行 AERLDEV=PROBABLE 而 AERLPRC=N、AERLPRT=N ⇒ "probably related" 唯一指向器械; "AE related to the event" 自指无义. Ex6 r2 平行句 "probably related to the device" |
| T-4 Row | 成立 | 同文件其他表一致 |
| U-1 Ex5 r2 AEENDY 25 | 不可定 ✓ | 2018-05-10 应为 Day24; 日期/Day 谁错不可单值 |
| U-2 Ex6 r2 2014-11-27 | 不可定 ✓ | 年份必错, 但月日按 Day 推算 (r2 起点 +35 = 11-28; r1 Day1 2018-08-06 +112 = 11-26) 均≠11-27, 非单值 |
| U-3 USUBJID 002/001 | 不可定 ✓ | 叙述未给 USUBJID |
| U-4 AESTDY 78 | 不可定 ✓ | Day1 2018-08-06 ⇒ 10-24 = Day80; 日期/Day 谁错不可定 |
| U-5 CAUSAL | KB=PDF ✓ | 渲染图 "CAUSAL"; PDF 内无码表可证 "CAUSAL RELATIONSHIP" |

### 其它必查
- O11 / D-1: KB :45 = PDF 原文; 删掉的 "Persistent… / Congenital… / Other medically important…" 3 项及 "…or prolongation of existing hospitalization" 均不在 PDF → 无 PDF 内容丢失. R2 recheck ig34_p0139_a010: 恢复后逐字 → 结案 (非 REAL_GAP).
- AEOSOSP→AESOSP (:49), AESOCD→AESOCCD (:64), AEMODIFY 句 (:13), "; see" (:19), "null:" (:39), Yes/No 单空格 (:43): 均与 p137-140 逐字一致.
- D-2..D-5: 旧值均为 KB 错值, 新值见上表; Ex5 删 AEREL 列 (PDF 无此列), Ex3 AESTDY→AEDY (PDF 列名 AEDY) → 无 PDF 丢失.
- 位置: Description/Overview 句落在新 `## AE – Description/Overview` (PDF p133 标题), `## AE – Assumptions` (p137 标题) → 结构行签字; H1 未动.
- 无副作用: AE 两文件外无本批改动; 未改其它标题/锚点.

### G-TB6 双向逐句扫描 (scan.py, 独立)
- KB→PDF 未命中 3 处: `**CRF: AE Seriousness Classification**` (KB 自写表前标签, 见 L-2); :54 "…Regulatory Submissions – Dataset Metadata…" (PDF 折行 en-dash 归一伪阴性, 目视逐字一致); :75 "…related to the device" (T-3). 其余新增/改动行全部在 PDF 找到出处.
- PDF→KB 未命中: 全部为 p134-137 spec 表行 (属 spec.md, 范围外) + 表格残片拼接伪阴性 (逐条目视: Ex1 Row 3 句、Ex2-6 叙述末句、Ex6 Row1/Row2 句、6b 列表、CRF 表均在 KB). 无真实叙述缺失.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| L-1 assumptions.md:39 | 版面 | PDF 在 "may be null:" 后另起段 "For example…", KB 同行 (信息无损; LOW, 可选) | p139 7a |
| L-2 assumptions.md:41 | D6 | `**CRF: AE Seriousness Classification**` 为 KB 自写标签, 比 `**CRF:**` 多了描述名; 按 D6 纯导航口径可保留 (LOW, 主控可选择简化为 `**CRF:**`) | PDF 表上方无标题 |
| F-1 (报告) | 归属 | p134 spec 首句 "ae.xpt, Adverse Events — Events. One record per adverse event per subject, Tabulation." AE 三文件均无. CM/IS 先例放在 assumptions.md (`## CM – Specification` + 句, CM/assumptions.md:7-9; IS/assumptions.md:7) → 建议同法补入 AE/assumptions.md Description 与 Assumptions 之间; spec 表脚注 (p137 "In this column, an asterisk (*)…") 属 spec.md. 主控裁 | p134 / p137 |

### 结构行签字
assumptions.md:3 `## AE – Description/Overview`, :7 `## AE – Assumptions`, :43-44 CRF 表首行+分隔线; examples.md:79-80 / :94-95 / :43-44 重建表头+分隔线 —— 均签字.

### dispatch notes 第 26 条 (表格类原子全扫) 覆盖说明
- AE 两文件全部 7 张表 (Ex1-Ex6 + CRF) 逐格对渲染图 (见上表), 不只改动行; 反向扫描 scan.py 覆盖两文件全文 (非仅改写段). 无 CODE_LITERAL. 结论不变: PASS.

## 续 签字 (writer attempt 1 续 delta: L-1 + F-1)
- F-1 assumptions.md:7-9 `## AE – Specification` + "ae.xpt, Adverse Events — Events. One record per adverse event per subject, Tabulation." = p134 首两行逐字 (标题 en-dash 与 PDF/CM 一致); 位置 Description → Specification → Assumptions, 同 CM/assumptions.md:5-11 先例. 结构行 (标题) 签字. fp ig34_p0134_a002 命中 AE/assumptions.md.
- L-1 assumptions.md:43/45: "may be null:" 后另起段 "For example…" = p139 版面, 文字未变. examples.md md5 f8dd2e92… 未变.
- 复跑: fp_match AE 页 (p133-145) 回归 0; check_links `live docs: 42`. **verdict 维持 PASS**.
