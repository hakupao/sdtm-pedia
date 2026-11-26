# T2 B-VS Auditor (Rule A) — attempt 1
> agent: oh-my-claudecode:verifier (opus); 独立于 writer (executor) / reviewer (code-reviewer); 先独立判, 未读 writer/reviewer 结论.
> base 78c859f; KB diff: VS/assumptions.md +10 (Desc/Overview + Spec 首句 + Assumptions 标题), VS/examples.md 10 格.

## 抽样
- 脚本 = t2_auditor_v1.0 模板, 两处按 dispatch notes 调整: PAGES = p358-361 (VS 全节); files += VS/assumptions.md (O13 插入落在此).
  `python3 -I $S/sample.py > $S/sample.json` (S=scratchpad/t2_B-VS_auditor) → seed 20261126, C=0, P=19, N=10.
- 补抽 (主控指定): ig34_p0358_a016 spec 首句 (ledger 为 INTENTIONAL_EXCLUDE 故不在 P; 按 dispatch notes 已补入 assumptions.md).

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|------|------|------|------|
| 1 | ig34_p0361_a015 | p361 §6.4.1 Criterion 1 段 "Per Section 6.2.1 … define an event" | FA/assumptions.md (存在) | 否 | — | — | 范围外 (FA, 非本批 kb_files) |
| 2 | ig34_p0361_a014 | p361 "Criterion 1: Data or observations that have different timing…" | FA/assumptions.md:25 | 否 | — | — | 范围外 (FA) |
| 3 | ig34_p0358_a014 | p358 VS Desc/Overview "A findings domain that contains measurements…" | VS/assumptions.md:5 | 否 | 是 (逐字) | 是 (## VS – Description/Overview) | O13 新增 |
| 4 | ig34_p0360_a007 | p360 Assump 1 LOINC / VSLOINC / Define-XML | VS/assumptions.md:13 | 否 | 是 | 是 | 未改 |
| 5 | ig34_p0361_a013 | p361 §6.4.1 首段 "FA structure … criteria for using" | FA/assumptions.md (存在) | 否 | — | — | 范围外 (FA) |
| 6 | ig34_p0360_a009 | p360 Assump 3 VS codetable + URL | VS/assumptions.md:17 | 否 | 是 (URL 完整) | 是 | 未改 |
| 7 | ig34_p0360_a010 | p360 Assump 4 不常用 qualifiers --BODSYS…--FAST | VS/assumptions.md:19 | 否 | 是 | 是 | 未改 |
| 8 | ig34_p0360_a017 | p360 "Row 12: Shows a value collected in one unit…" | VS/examples.md:10 | 否 | 是 | 是 | 未改 |
| 9 | ig34_p0360_a008 | p360 Assump 2 参考范围 / VSTOX / VSCLSIG / §4.5.5 xref | VS/assumptions.md:15 | 否 | 是 (xref 完整) | 是 | 未改 |
| 10 | ig34_p0361_a017 | p361 "Repeated assessments … intermittent" | FA/assumptions.md (存在) | 否 | — | — | 范围外 (FA) |
| 11 | ig34_p0358_a016 (补抽) | p358 "vs.xpt, Vital Signs — Findings. One record per … Tabulation." | VS/assumptions.md:9 | 否 | 是 (逐字) | 是 (## VS – Specification, Desc 与 Assumptions 之间, 依 CM/IS 先例) | 新增 |

- 本批范围内 prose 样本 7/7 (含补抽) 无丢失、无忠实度错误; 另核 P 内未抽中的 VS prose (p360 a013-a016, a018) 亦逐字存在于 examples.md:5-11.
- 独有丢失数 **0**; 忠实度错误数 **0**. 范围外 4 条 (FA §6.4.1) 均已在 FA/assumptions.md, 无发现.

## vs.xpt 10 格复核 (seed 20261126, `python3 -I $S/cells.py`; 渲染 p360 @250dpi 裁切 + p361 @110dpi)
| 格 | KB | PDF 渲染 | 改动格? | 结果 |
|----|----|---------|--------|------|
| R7 VSSTRESN | 36.2 | 36.2 (p361) | 是 | OK |
| R12 VSSTRESC | 36.2 | 36.2 (p361) | 是 | OK |
| R1 VSTPT | BASELINE 1 | BASELINE / 1 (换行, p360) | 是 | OK |
| R6 VSTPT | BASELINE 1 | BASELINE / 1 (p361) | 是 | OK |
| R2 VSSTRESN | 152 | 152 | 否 | OK |
| R7 VSLOC | SUBLINGUAL REGION | SUBLINGUAL / REGION | 否 | OK |
| R8 VSDY | 1 | 1 | 否 | OK |
| R5 VSTPTNUM | (空) | (空) | 否 | OK |
| R7 VSORRESU | C | C | 否 | OK |
| R3 VSDY | 1 | 1 (p360) | 否 | OK |
10/10 一致 (4 改动格). `pdftotext -layout` p360-361 交叉印证 rows 1-4 VSDY=1.

## 登记给主控: ATOM_ERR
- ig34_p0360_a021, ig34_p0360_a022, ig34_p0360_a023, ig34_p0360_a024 (vs.xpt Rows 1-4): 原子把 VSDY 读成空、VSTPT 截成 "BASELINE" (渲染为 VSDY=1, VSTPT="BASELINE 1/2" 跨行). KB 现值与渲染一致; 原子本身错误, 不应用作真值.

## 其他检查
- fp 隔离: `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -cE 'p035[89]|p036[01]|VS/' $S/fp_regress.jsonl` → 0 (全局 RED 48 条来自他批 §6.4.2 等未提交改动).
- `python3 tools/check_links.py` → live docs 44; 新增 2 条均在 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-EC.md:59,79` (B-EC 证据文件, 非本批); VS 文件贡献 0. 提请主控在 B-EC 处理.
- G-TB8: trace L184 executor subagent_done 03:33:27Z, L190 code-reviewer PASS 03:36:09Z; VS/assumptions.md 与 examples.md mtime 12:32:57 JST (=03:32:57Z) 早于 reviewer PASS → reviewer 后无 writer 改动; trace 无 `agent: main` 写 VS 记录. OK.

## 结论
**PASS** — Rule A N=10 (+1 补抽) seed 20261126: 丢失 0, 忠实 0; 表格 10 格 0 差异; G-TB8 OK.
