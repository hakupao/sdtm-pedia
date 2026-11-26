# T2 B-CM auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus; 先独立判, 判完才对照 writer/reviewer 报告)

- 命令: `t2_auditor_v1.0.md` 抽样脚本, 两处按主控口径调整: `files` = batch kb_files ∪ {`knowledge_base/domains/CM/assumptions.md`} (主控授权, 本批实际改动); `J["pdf_pages"] = range(98, 104)` (CM 全节 p98-103; batch json pdf_pages 仅 102). 其余逐字不变. 输出 scratch `t2_B-CM_auditor/sample.json`.
- seed = 20261126; C = 0 (atoms/t2_recheck 均 0); P = 55; N = min(30, max(10, 0), 55) = 10 → 全部来自 P−C.
- 样本: p0102_a004, p0101_a021, p0100_a005, p0102_a017, p0102_a020, p0100_a009, p0101_a008, p0101_a010, p0102_a018, p0101_a004.
- 真值: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0{098,100,101,102,103}.txt` (layout) + p102 `pdftoppm -r 110` 渲染 (核 Ex2 Row 2).

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0102_a004 | p102:6 Ex2 首句: 研究关注受试者是否用抗惊厥药 | CM/examples.md:32 | 否 | 是 | 是 (## Example 2) | 逐字 |
| 2 | ig34_p0101_a021 | p101:23-24 Rows 7-9: ABC-0002 第 1/3 条 QD, 第 2 条 BID | CM/examples.md:11 | 否 | 是 | 是 (Ex1) | 与 PDF 页文本逐字 ("where CMSEQ is", "(CMSEQ = "2")"); 原子 verbatim 此处与 PDF 不符 = 原子错, 以 PDF 为准 |
| 3 | ig34_p0100_a005 | p100:13 spec 表脚注 "In this column, an asterisk (*) …" | — (CM 三文件均无) | 范围外 | — | — | spec 表脚注按 dispatch notes 属 spec.md (非本批 kb_files) → **范围外发现 O-1**, 不计本批; ledger 记 EQUIVALENT 与实况不符 |
| 4 | ig34_p0102_a017 | p102:19 Ex3: 用药细节 (dose, frequency) 不关注 | CM/examples.md:45 | 否 | 是 | 是 (Ex3) | 逐字 |
| 5 | ig34_p0102_a020 | p102:22 Row 3: 已征询但未收集; 原因记于 CMREASND | CM/examples.md:51 | 否 | 是 | 是 (Ex3) | 逐字 |
| 6 | ig34_p0100_a009 | p100:25-30 Assumption 2a: CMTRT topic 变量, 不含剂量等; ASPIRIN 例拆分 | CM/assumptions.md:16 | 否 | 是 | 是 (2.a) | 逐字 (弯引号→直, 全库惯例) |
| 7 | ig34_p0101_a008 | p101:9 4a: 例 受试者用避孕药 | CM/assumptions.md:27 | 否 | 是 | 是 (4.a) | 逐字 |
| 8 | ig34_p0101_a010 | p101:10 4a: 开始日期 (或部分日期) 存 CMSTDTC | CM/assumptions.md:27 | 否 | 是 | 是 (4.a) | 逐字 |
| 9 | ig34_p0102_a018 | p102:20 Row 1: 已征询且已服用 | CM/examples.md:47 | 否 | 是 | 是 (Ex3) | 逐字 |
| 10 | ig34_p0101_a004 | p101:3-4 3c: CMPRESP/CMOCCUR 为 Perm, 全自由文本收集时可省 | CM/assumptions.md:24 | 否 | 是 | 是 (3.c) | 逐字 |

**本批计分样本 9 (#3 范围外): 独有丢失 0 / 忠实度错误 0 → 抽检 PASS.**

### 本批改动逐项核 (独立)
- examples.md:39 Ex2 Row 2 `USUBJID=2, CMSEQ=1` ↔ p102:11 layout + p102 渲染图 (Row 2: ABC123/CM/2/1/VPA/ANTI-CONVULSANT) 一致.
- assumptions.md:22 3a "to indicate whether the intervention in CMTRT was prespecified" ↔ p100:40-41 逐字.
- assumptions.md:29 5 "any identifier variables, timing variables, …" ↔ p101:13 逐字.
- assumptions.md:18 2c 删末句 (D-2): 改后止于 "…Define-XML document." ↔ p100:32-34 逐字 (PDF 2c 无 "left blank" 句). 被删句副本: `sed -n 84p knowledge_base/domains/CM/spec.md` 全行 (不截断) 末尾逐字含 "If an intervention term does not have a decode value in the dictionary, then CMDECOD will be left blank." ↔ p98:26-29 CMDECOD CDISC Notes 逐字; spec.md 未改 (`git show HEAD:…spec.md | sed -n 84p | md5` = 工作树 = `dc620e0ca2fad95a1a3291ff252d716a`; mtime 2026-11-25). 删除无损.
- 授权范围: `git diff HEAD --stat -- knowledge_base/domains/CM/` = assumptions.md (3+/3−) + examples.md (1+/1−), 全为逐词/单元格级修正 + D-2 主控裁定删除; Description/spec 首句已存在未改; spec.md 未动. 无授权外改动.

### 旁证
- P 全 55 原子机械匹配 (弯/直引号归一, 去 `**`/列表号, 空白归一; scratch `mech.txt`) vs CM/{assumptions,examples,spec}.md: 48 HIT, 7 MISS — a007 (原子错 CMSTPPT, PDF/KB 均 CMSTTPT)、a021/a022/p0102_a029 (原子 verbatim 与 PDF 页文本不符, KB = PDF)、p0100_a005 (O-1)、p0103_a021/a022 (O-2). 本批 kb_files 内 0 真缺.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → 42 (基线 42).
- 对照 writer/reviewer 报告 (判后): 改动清单 #1-4 + D-2 与本 auditor 独立核一致. writer/reviewer 均未报 O-1/O-2 (两者在本批 kb_files 外; reviewer 注明 spec 表不在本批).

### 范围外发现 (不计本批, 交主控 / O15/O16)
- O-1: CM spec 表脚注 (p100:13, ig34_p0100_a005 "In this column, an asterisk (*) …") 在 CM 三文件中均缺; 属 spec.md (dispatch notes 口径), 同 MS/LB 等先例交域扫. coverage_ledger 该原子 EQUIVALENT 与实况不符.
- O-2: §6.1.3 Exposure Domains 父节引言 (p103, ig34_p0103_a021 "Clinical trial study designs can range from open label …" / a022 "To support standardization … Exposure (EX) and Exposure as Collected (EC).") `grep -rn "study designs can range" knowledge_base` 0 命中 — 全库缺失; 属 §6.1.3 (EX/EC 侧), 非 CM. 建议主控核 B-EX 是否已覆盖, 否则开项.

### G-TB8
- trace `T2.B-CM`: writer `oh-my-claudecode:executor` a1 04:58:24Z / a2 04:58:59Z, reviewer `oh-my-claudecode:code-reviewer` a1 05:01:53Z PASS; 无 `agent: main` 记录 (grep 计数 0).
- 时序: assumptions.md mtime 04:58:59Z, examples.md 04:57:35Z < reviewer 05:01:53Z (终态经 reviewer). md5 assumptions `ee387c8140bdfd9dc63516b136d1ce18` (= writer a2 报告), examples `01c3d7d7898ae19665c34b216eaccf58` (= writer a1 报告).

**结论: PASS** (丢失 0 / 忠实 0; 范围外 2 条; G-TB8 OK).
