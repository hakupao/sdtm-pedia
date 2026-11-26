# T2 B-DA auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus; 先独立判, 判完才对照 writer/reviewer 报告)

- 命令: `t2_auditor_v1.0.md` 抽样脚本, 两处按主控口径调整: `files` = batch kb_files ∪ {`knowledge_base/domains/DA/assumptions.md`} (主控授权, 本批实际改动); `J["pdf_pages"] = [180, 181, 182]` (DA 全节 p180-182). 其余逐字不变. 输出 scratch `t2_B-DA_auditor/sample.json`, `P.json`.
- seed = 20261126; C = 0; P = 18 (含 ig34_p0180_a0002 = §6.3 章引言, O39 排除, 未入样本); N = 10 → P−C 10.
- 样本: p0182_a020, p0182_a019, p0180_a0005, p0182_a002, p0182_a003, p0182_a022, p0181_a017, p0181_a018, p0181_a016, p0182_a012.
- 真值: `pdftotext -layout` p180-182 + `pdftoppm -r 110` p180-182, p182 顶部另 200dpi 裁剪 (Ex1 表).

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0182_a020 | p182 Ex3 "Rows 1-2: …first feed of the diary (day 1)" | DA/examples.md:33 | 否 | 是 | 是 (## Example 3) | 逐字 (Rows 标签加粗 = 格式) |
| 2 | ig34_p0182_a019 | p182 Ex3 引言: nutrition study, 配方奶准备量与剩余量 | DA/examples.md:31 | 否 | 是 | 是 | 逐字 |
| 3 | ig34_p0180_a0005 | p180 DA Description/Overview: findings domain, accountability of study products (receipt/dispensing/return/packaging) | DA/assumptions.md:5 | 否 | 是 | 是 (## DA – Description/Overview, 本批新增) | 逐字; 标题 en dash U+2013 同 PDF |
| 4 | ig34_p0182_a002 | p182 "Example 1" 标题 | DA/examples.md:3 | 否 | 是 | 是 | 导航 |
| 5 | ig34_p0182_a003 | p182 Ex1 引言: 2 study meds + 1 rescue, tablets; EPOCH, DASPID/DAREFID | DA/examples.md:5 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0182_a022 | p182 Ex3 "Rows 5-6: …third feed of the diary (day 2)" | DA/examples.md:37 | 否 | 是 | 是 | 逐字 |
| 7 | ig34_p0181_a017 | p181 Assumption 1b: drugs 用 "Dispensed Amount"/"Returned Amount" | DA/assumptions.md:15 | 否 | 是 | 是 (1.b) | 逐字 |
| 8 | ig34_p0181_a018 | p181 Assumption 1c: nutrition 例 "Prepared Amount"/"Unused Amount" | DA/assumptions.md:16 | 否 | 是 | 是 (1.c) | 逐字 |
| 9 | ig34_p0181_a016 | p181 Assumption 1a: 器械转移归 DT, 见 SDTMIG-MD (URL) | DA/assumptions.md:14 | 否 | 是 | 是 (1.a) | 逐字含 URL |
| 10 | ig34_p0182_a012 | p182 "Example 2" 标题 | DA/examples.md:18 | 否 | 是 | 是 | 导航 |

**本批计分样本 10: 独有丢失 0 / 忠实度错误 0 → 抽检 PASS.**

### 旁证: P 全 18 原子机械匹配 (空白/加粗/列表号归一)
- 17/17 DA 原子精确命中 (assumptions.md 8, examples.md 9), 含 Ex2 引言 a013 "the purpose of the accountability tracking" (本批恢复原词) 与 Spec 后 Assumptions 全 4 条.
- 1 未命中 = p0180_a0002 §6.3 章引言 (O39 / writer F-1, 章级, 不属 DA 节, 不计本批).
- 另核: assumptions.md:9 spec 首句 "da.xpt, Product Accountability — Findings. One record per product accountability finding per subject, Tabulation." 与 p180 逐字; 三个 `## DA –` 标题码位 U+2013 与 PDF 一致, 顺序 Description → Specification → Assumptions 同 PDF.

### 额外必查: Ex1 Rows 5/6 改动格对 p182 渲染图 (200dpi) 逐格
- KB Ex1 表全部 8 行 (表头/分隔/Row 1-6) 均 19 列 (机检 `|` 计数), 与 PDF 19 列一致.
- Row 5: DAREFID 空 ✓, DASPID 空 ✓, DATESTCD DISPAMT ✓, DACAT Rescue Medication ✓, DASCAT 空 ✓, DAORRES 10 ✓, DAORRESU TABLET ✓, DASTRESC 10 ✓, DASTRESN 10 ✓, DASTRESU TABLET ✓, VISITNUM 1 ✓, EPOCH "Study Med Period 1" ✓, DADTC 2004-06-15 ✓.
- Row 6: 同上, DATESTCD RETAMT / Returned Amount ✓, VISITNUM 2 ✓, EPOCH "Study Med Period 1" ✓, DADTC 2004-07-15 ✓.
- 原 KB (HEAD) 错位: DASCAT 后多一空格致 DAORRES..VISITNUM 左移、DASTRESN 丢、EPOCH 空 → 已复位; Row 1-4 未改且与渲染一致. 0 差.
- Ex2/Ex3 表 (未改) 抽看渲染: 列数 17/17 与 PDF 一致.

### 对照 writer/reviewer (判完后)
- 与 writer checkpoint 一致 (12 改动; F-1 §6.3 章引言需主控定; F-2 spec.md 归 O15). reviewer PASS 无冲突. 授权范围外无改动 (`git diff HEAD -- knowledge_base/domains/DA/` 仅 assumptions.md 头部 3 标题 + 2 段, examples.md Ex1 Row 5/6 + Ex2 一词).
- 非计分观察: examples.md 用 `# DA — Examples` (KB 文件标题) 承载 PDF "DA – Examples" 小标题, 导航, 不计.

### G-TB8
- trace.jsonl:240 writer (oh-my-claudecode:executor) subagent_done 04:53:01Z; :248 reviewer (oh-my-claudecode:code-reviewer) PASS 04:55:16Z; 无 `agent: main` 写 B-DA KB 记录.
- DA/assumptions.md, examples.md mtime 13:51:21 +0900 (= 04:51:21Z) 早于 writer done 与 reviewer PASS, reviewer 后无改动. md5: assumptions 79a8536ae14f5de89c06affcec87e3d2, examples e3bcd39cb400979b0ba74898d62eb6e0.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42 (基线 42).

**结论: PASS** (丢失 0 / 忠实 0; 范围外 1 = p0180_a0002 §6.3 章引言 O39, 不计).
