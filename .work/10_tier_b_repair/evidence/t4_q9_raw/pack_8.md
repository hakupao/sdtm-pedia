# T4.1 Q9 扩检 — 包 8 结果 (Q9_IG34_EQUIV, Q180-Q192)

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:03:05Z (`date -u`)
- brief: `.work/10_tier_b_repair/subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `.work/10_tier_b_repair/subagent_prompts/t4/t4_q9_extension_v1.0.md`
- 样本包: `.work/10_tier_b_repair/work/t4/q9/q9_pack_8.md`
- 看过的渲染页: SDTMIG v3.4 p68, p395, p396 (另 p396 用 `pdftoppm -r 400` 局部放大 Blinded View 图, 输出在 scratchpad `q9_8/`, 未写仓库)
- 用过的命令: `grep -rn` (KB 全文定位), `sed -n` / `awk` (PDF 文本层 `ig34_p{0046,0074,0075,0187-0191,0227,0228,0255,0257,0396,0405,0426,0427}.txt` 与 KB 文件取行、取所在标题), `grep` 台账 `coverage_ledger.wc.jsonl` (Q185 旧匹配链接), `pdftoppm -r 400 -f 396 -l 396 -x 500 -y 750 -W 2400 -H 800 -png`

## 逐条判定

| # | atom_id | 层 | 终态 | 判定 | 依据 | 说明 |
|---|---|---|---|---|---|---|
| Q180 | `ig34_p0426_a006` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | PDF `ig34_p0426.txt:16-18`; KB `knowledge_base/domains/TI/assumptions.md:50` (节 `## §7.5 How to Model the Design of a Clinical Trial`, 第 38 行) | 实为逐字. 列表号 9、TD 数据集名、全部措辞一致; 前后 8/10 条顺序一致, 位置为 §7.5 节 |
| Q181 | `ig34_p0427_a006` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | PDF `ig34_p0427.txt:8-10`; KB `knowledge_base/chapters/ch08_relationships.md:10` (Ch8 Overview 列表) | 实为逐字 (项目符号 • → `-`). 8.1-8.8 列表顺序一致 |
| Q182 | `ig34_p0046_a019` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | PDF `ig34_p0046.txt:26`; KB `knowledge_base/chapters/ch04_general_assumptions.md:1098` (节 `### 4.4.10 Representing Time Points`) | 实为逐字. `PT1H` 位于 VS 时间点表第 2 行; 整行 6 格 (2 / 60 MIN / PT1H / DOSE ADMINISTRATION / 2006-08-01T08:00 / 2006-08-01T09:01) 逐格一致 |
| Q183 | `ig34_p0190_a028` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | PDF `ig34_p0190.txt:1` (EG Example 1 数据集标签, Example 1 文字在 p189); KB `knowledge_base/domains/EG/examples.md:21` (`## Example 1` 下) | 实为逐字 (加粗). 下接表头 24 列与 PDF 一致 |
| Q184 | `ig34_p0228_a018` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | PDF `ig34_p0228.txt:27`; KB `knowledge_base/domains/GF/examples.md:185` (`## Example 5`, 前句 183 行一致) | 实为逐字. 后接 relrec 表 2 行 (PS001/GF/GFLNKID/ONE/1; PS001/MS/MSLNKID/ONE/1) 逐格一致 |
| Q185 | `ig34_p0255_a036` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | PDF `ig34_p0255.txt:40` (本页唯一一处 MSSTRESC, MS Assumption 1.a.ii); KB `knowledge_base/domains/MS/assumptions.md:16` | 实为逐字, 整句 "(MSORRES, MSSTRESC/MSSTRESN) ... MSORRESU/MSSTRESU" 一致, 位置在 MS Assumptions. 注: 包给的 KB 指针 (MS/examples.md 表头) 与台账旧匹配链接 `md_dmMS_ex_a027` 都指向 examples, 不是该原子的对应处; 内容判定以 assumptions.md:16 为准, 成立 |
| Q186 | `ig34_p0405_a003` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | PDF `ig34_p0405.txt:3`; KB `knowledge_base/domains/TE/examples.md:9` (`## Example 1`, 前句 "This example shows the TE dataset for TA Example Trial 1." 一致) | 实为逐字 (加粗) |
| Q187 | `ig34_p0068_a004` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p68 (DM Example 1 dm.xpt 表头); KB `knowledge_base/domains/DM/examples.md:7` (`## Example 1`) | KB 26 列与渲染页逐列一致 (… RFXENDTC, **RFICDTC**, RFPENDTC … ARMNRS, **ACTARMUD**, COUNTRY), 实为逐字. 原子 verbatim 抽错两处: `RFCIDITC` (PDF 为 RFICDTC)、`ACTARMNRS` (PDF 为 ACTARMUD). KB = PDF, 无 KB 问题; 标签层面此条实为 "原子抽错 + KB 逐字", 若要细化可另记 (不影响本次 HOLDS) |
| Q188 | `ig34_p0257_a027` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | PDF `ig34_p0257.txt:44`; KB `knowledge_base/domains/MB/examples.md:39` (`## §6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples` → `### Example 2` → be.xpt) | 实为逐字, 8 列一致; 下接 3 行数据也一致. MS/examples.md Example 2 用指针指向 MB Example 2, 位置正确 |
| Q189 | `ig34_p0396_a006` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p396 (Example 4 Trial Design Matrix); KB `knowledge_base/domains/TA/examples.md:667` (Example 4 段, 523 起) | PDF 表头: 空 / Screen / Treatment (横跨 8 格) / Follow-up. KB 用 Treatment 后 7 个空格模拟合并单元格, 列数 11 与数据行 (A/B 行 Screen, Trt×4+Rest×4, Follow-up) 一致. 信息等价 |
| Q190 | `ig34_p0075_a003` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | PDF `ig34_p0075.txt:1-2` (接 p74 末 Example 6 引言); KB `knowledge_base/domains/DM/examples.md:286` (`## Example 6`) | 实为逐字. "CDASHIG v2.1, Section 7.3" 版本号/节号一致; 前后顺序 (CDASH 引言 → 本句 → aCRF 图题) 与 PDF 一致 |
| Q191 | `ig34_p0227_a022` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | PDF `ig34_p0227.txt:40-41`; KB `knowledge_base/domains/GF/examples.md:153` (`## Example 5`) | 实为逐字, 两个 "Note" 都在 |
| Q192 | `ig34_p0396_a002` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p396 + 400dpi 局部放大; KB `knowledge_base/domains/TA/examples.md:638-661` (`**Blinded View**` + Mermaid) | 确为图 (Example Trial 4, Cyclical Chemotherapy Blinded View). KB 用 Mermaid 再现, 附 KB note 标图题. 逐项对照: Screening Epoch/Screen ✓; Treatment Epoch 内 Rx→Rest 4 次 ✓; 3 条绿色 "If disease progression" 箭头从第 1-3 个 Rest 末尾跳到 Follow ✓ (与 TA 表行 3/5/7 TATRANS 一致); Follow-up Epoch/Follow ✓; 右侧 Blind 箭头指向 Follow-up ✓; 底部 Randomization 箭头 ✓. 无矛盾. 前后文字 (blinded 引言、设计矩阵说明) 逐字 |

## 计数

- HOLDS: 13 (其中 TOC 条目 0; 实为逐字 11 条, Q189 / Q192 为非逐字等价)
- NOT_HOLD_R1: 0
- NOT_HOLD: 0
- UNVERIFIABLE: 0

按层: Q9_IG34_EQUIV 13 条 — HOLDS 13 / NOT_HOLD_R1 0 / NOT_HOLD 0 / UNVERIFIABLE 0.

附注 (不改判定): Q187 原子 verbatim 抽错 (RFCIDITC / ACTARMNRS), KB 按 PDF 写对; Q185 旧匹配链接指向 MS examples 而非 assumptions, 内容实在 MS/assumptions.md:16.

## 样本外发现的 KB 内容问题

无.
