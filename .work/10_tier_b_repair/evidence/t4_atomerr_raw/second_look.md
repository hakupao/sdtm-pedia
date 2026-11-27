# T4 加查 ATOM_ERR (S1-R1) 复看 — 第二位独立审查者结果 (E10-E14)

- 审查者类型: `general-purpose` (Claude Code agent), 只读; 与 brief 中 tracer 类型不同, 判定口径相同 (`subagent_prompts/t4/t4_atomerr_s1r1_v1.0.md` + `t4_supp_fullcheck_v1.0.md` 背景 / 判定口径).
- 时间: 2026-11-27T14:14:14Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 样本包: `.work/10_tier_b_repair/work/t4/atomerr/atomerr_pack_second.md` (5 条, 全判)
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`, Read 带 pages): p122, p123, p124, p133, p150; 另用 pdftoppm 300dpi 放大裁切 p123 "ADD ROW" 行、p124 ml.xpt Row 2-3、p133 整页 (输出在系统临时目录, 未入仓).
- 用过的命令:
  - `grep -F '"<atom_id>"' .work/10_tier_b_repair/work/pdf_atoms.jsonl` (5 条原子原件; 与包内 verbatim 逐字一致)
  - `grep -n` 在 `knowledge_base/domains/{ML,SU,CE}/*.md` 定位 KB 行; `sed -n` 看 ML / SU 表头与相邻行
  - `grep -n` 查 `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` (p122/123/124/133/150 及 ML / SU 相关条目)
  - `pdftoppm -r 300 -f N -l N [-x -y -W -H] -png` (放大裁切)
- 未读: `evidence/t4_atomerr_raw/pack_*.md`、`verdicts.json`、`trace.jsonl`、`evidence/checkpoints/` 下任何文件.

## 判定表

| # | atom_id | 判定 | ① 原子 vs PDF (差在哪; PDF 文件:行 或 渲染页) | ② KB vs PDF (KB 文件:行) | 说明 |
|---|---|---|---|---|---|
| E10 | `ig34_p0122_a017` | HOLDS | 成立. 第二句原子写 "Examples of nutritional items that would not be represented in other domains", PDF 是 "...that would be represented in other domains include:" (原子多 'not'). 渲染页 p122 ML – Assumptions 1; `ig34_p0122.txt:37` | 成立. `knowledge_base/domains/ML/assumptions.md:13` 两句与 PDF 逐字一致 (第一句 "would not be represented in the exposure domains", 第二句 "would be represented in other domains") | 列表标号 "1." 属归一化. 无涉登记 |
| E11 | `ig34_p0123_a012` | HOLDS | 成立. 原子 "Click here to add a row. ADD ROW", PDF 是 "Click here to add a row: ADD ROW" (冒号, 原子写成句号). 渲染页 p123 Meal Log CRF 末行 (300dpi 放大确认为冒号); `ig34_p0123.txt:19` | 成立. `knowledge_base/domains/ML/examples.md:19` "Click here to add a row: **ADD ROW**" (粗体属归一化), 位于 Meal Log CRF 表末行, 位置对 | 标点级差异, 但属 "错字/错值" 类真实差异, 非空白/引号归一化. 无涉登记 |
| E12 | `ig34_p0124_a001` | NOT_HOLD | 不成立. 原子 18 格与 PDF ml.xpt Row 2 逐格一致: MLDTC 空, MLSTDTC 2015-09-03T08:30, MLENDTC / MLEVLINT 空, RELMIDS LAST MEAL PRIOR TO, MIDS HYPO2, MIDSDTC 2015-09-03T17:00 (未截断). 渲染页 p124 顶部表 (300dpi 放大); `ig34_p0124.txt:2-5` | 成立. `knowledge_base/domains/ML/examples.md:42` 与 PDF 逐格一致, 列与表头 `examples.md:38` 对齐 | `①不成立`. PDF: Row 2 … HYPO2 / 2015-09-03T17:00; 原子: 同 PDF, MIDSDTC 完整 2015-09-03T17:00; KB: 同 PDF. 按标签定义 KB 对 PDF 为逐字 (EXACT). 登记说的 "MIDSDTC 截断" 在现原子原件中找不到; 原子 prompt_version 带 `OptionE_p124_rerun`, 可能登记时看的是重抽前版本 (仅事实描述, 未核旧版). 无涉登记 (registry `B-ML T-1` 为 Example 2 的 WHTE MILK, 不是本行) |
| E13 | `ig34_p0133_a003` | HOLDS | 成立. PDF su.xpt 有 19 列, Row 1 应为 19 格; 原子 21 格: TOBACCO 后 3 个空格 (PDF 只有 SUSTAT / SUREASND 2 个空), 且 QD 后多出 "2006-01-01 / 空" 一组 (原子: QD / 空 / 空 / 2006-01-01 / 空 / 2006-01-01 / BEFORE / 2006-01-01 / ONGOING), 串列. PDF: QD / SUSTDTC 空 / SUENDTC 空 / 2006-01-01 / BEFORE / 2006-01-01 / ONGOING. 渲染页 p133 su.xpt Row 1 (300dpi); `ig34_p0133.txt:2-4` | 成立. `knowledge_base/domains/SU/examples.md:37` 19 格, 与表头 `:35` 对齐: SUSTAT / SUREASND 空, SUDOSE 2, PACK, QD, SUSTDTC / SUENDTC 空, SUSTTPT 2006-01-01, SUSTRTPT BEFORE, SUENTPT 2006-01-01, SUENRTPT ONGOING, 与 PDF 逐格一致 | 无涉登记 (registry `B-SU T-1` 在 p132 叙述 SUENTTP 笔误, 不是本表行) |
| E14 | `ig34_p0150_a007` | HOLDS | 成立. 原子 "migraine headaches may not be considered as adverse events per protocol", PDF 是 "may not be considered to be adverse events per protocol" (换词 'to be' → 'as'). 渲染页 p150 CE – Assumptions 1a; `ig34_p0150.txt:21` | 成立. `knowledge_base/domains/CE/assumptions.md:14` 全段与 PDF 逐字一致 (含 "considered to be adverse events") | 列表标号 "(a)" vs "a." 属归一化, 不计. 无涉登记 |

## 计数

- HOLDS: 4 (E10, E11, E13, E14)
- NOT_HOLD: 1 (E12, `①不成立`; KB 对 PDF 为 EXACT)
- UNVERIFIABLE: 0
- 涉登记: 无
- 没看渲染页只看文本层: 无 (5 条均看渲染页)

## 样本外发现的 KB 内容问题

无.
