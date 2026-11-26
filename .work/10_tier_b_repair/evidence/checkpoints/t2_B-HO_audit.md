# T2 B-HO auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus; 先独立判, 判完才对照 writer/reviewer 报告)

- 命令: `t2_auditor_v1.0.md` 抽样脚本, 两处按主控口径调整: `files` = batch kb_files ∪ {`knowledge_base/domains/HO/assumptions.md`} (主控授权, 本批实际改动); 页集合 = range(167, 172) (HO 全节 p167 下半-p171 上半; batch json pdf_pages 仅 169-171), 前缀固定 `ig34`. 其余逐字不变. 脚本 scratch `t2_B-HO_auditor/sample.py` → `sample.json`: `python3 -I $S/sample.py > $S/sample.json`.
- seed = 20261126; C = 0 (本批 2 atoms 均 TABLE_ROW); P = 31 (含 p167 上半 DS 原子 8 条 + p171 MH 1 条 = 对照); N = min(30, max(10, 0), 31) = 10 → 全部 P−C.
- 样本: p0169_a0011, p0169_a0010, p0167_a0002, p0169_a0017, p0169_a0031, p0167_a0003, p0169_a0005, p0169_a0006, p0169_a0018, p0167_a0008.
- 真值: `.work/10_tier_b_repair/work/pdf_pages/ig34_p01{67,69,70,71}.txt` (layout) + `pdftotext -layout "source/cdisc/SDTMIG v3.4 (no header footer).pdf"` p167/p169/p171 复核 + p171 `pdftoppm -r 110` 渲染.

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0169_a0011 | p169:28-30 Assumption 5: 可加 identifier/timing/Events qualifier, 但 20 个 qualifier 一般不用 | HO/assumptions.md:23 | 否 | 是 | 是 (## HO – Assumptions 5.) | 20 项顺序逐项一致. 原子 verbatim 写 "--BODYS" 为原子抽取错; PDF 文本层与 pdftotext 复核均为 "‑‑BODSYS", KB "--BODSYS" 正确 (BODYS→BODSYS 替换后整句子串命中). U+2011 非断连字符 → "--" 属既有规范化, 不计 |
| 2 | ig34_p0169_a0010 | p169:25-27 Assumption 4: 提供者/机构名用 SUPPHO QNAM=HONAM; --NAM 属 Findings 类 | HO/assumptions.md:21 | 否 | 是 | 是 (4.) | 逐字 |
| 3 | ig34_p0167_a0002 | p167:1-2 DS 例: 研究治疗处置日期 = 该治疗末次给药日 | DS/examples.md:389 | 否 | 是 | 是 (DS 例, ds.xpt DS10 前) | 对照原子 (DS, 范围外), 逐字 |
| 4 | ig34_p0169_a0017 | p169:37 Ex1 Rows 6-7: ABC123103 有 2 条住院记录 | HO/examples.md:11 | 否 | 是 | 是 (## Example 1) | 逐字 |
| 5 | ig34_p0169_a0031 | p170:19 Ex1 suppho Row 1: ABC123101 首次就诊记录了适应症 | HO/examples.md:34 | 否 | 是 | 是 (ho.xpt 后 suppho 前) | 逐字 (原子页标 p169, 实在 p170:19, 不影响判定) |
| 6 | ig34_p0167_a0003 | p167:3 DS 例 Rows 1-2: 筛选期知情同意与随机化 | DS/examples.md:391 | 否 | 是 | 是 | 对照原子, 逐字 |
| 7 | ig34_p0169_a0005 | p169:15-16 Assumption 1: HO 含住院/门诊事件 (4 个 e.g.) | HO/assumptions.md:13 | 否 | 是 | 是 (1.) | 逐字 |
| 8 | ig34_p0169_a0006 | p169:17-18 Assumption 2: HOTERM 描述场所; HOSTDTC/HOENDTC 含义 | HO/assumptions.md:15 | 否 | 是 | 是 (2.) | 逐字 |
| 9 | ig34_p0169_a0018 | p169:38 Ex1 Row 8: ABC123104 心导管室 | HO/examples.md:13 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0167_a0008 | p167:11 DS 例 Row 7: 随访期处置, 受试者死亡 | DS/examples.md:401 | 否 | 是 | 是 | 对照原子, 逐字 |

**独有丢失 0, 忠实度错误 0 → PASS** (范围外发现 0).

### 补充核 (超出样本)
- P 全 31 原子机械匹配 (`python3 -I $S/match.py $S`, 规范化 U+2011/U+2019/粗体/空白): 30 EXACT; 1 MISS = p0169_a0011 (原子 BODYS 抽取错, 见 #1). p0167_a0020 Description → HO/assumptions.md:5 EXACT; p0171_a0004 → HO/examples.md:75 EXACT (弯撇号与 PDF U+2019 一致; 引号风格 O40 不计); p0169_a0034/35 → examples.md:40/42 EXACT (删 "recorded" 后与 PDF p170:22-23 一致).
- examples.md:72 Row 10 HOSTDTC `2011-06-25T10:00`: pdftotext p171 行 "10 … 2011-06-25T10:00 2011-06-29T19:30" + p171 110dpi 渲染图目视一致.
- assumptions.md 新增 3 标题/2 句: 标题 U+2013、spec 首句 U+2014 码位与 PDF p167 一致; spec 首句与 PDF p167:22 逐字.
- diff 授权范围: `git diff HEAD --stat -- knowledge_base/domains/HO/` = assumptions +10 (纯顶部插入, 列表 1-5 未动) / examples 4 行替换 (:40/:42/:72/:75), 均在授权内. md5 examples `e71563a90adf090479dce77767dd87b5`, assumptions `72e0010c2cfff8088aa60e4bfaacabe1` = writer 报告改后值.
- T-1 (Ex1 Row 5 PDF "REHABILIATION") KB 保留正确拼写, 依据 PDF 自身 (Ex2 Row 3 / Ex1 叙述 / Assumption 1), 已登记, 不计.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (= 基线).

### G-TB8
- trace.jsonl `T2.B-HO`: writer `oh-my-claudecode:executor` subagent_done 2026-11-26T04:58:51Z; reviewer `oh-my-claudecode:code-reviewer` subagent_done PASS 05:00:53Z (晚于 writer); `grep B-HO trace.jsonl | grep '"agent": "main"'` 无输出 → 无主控写 KB. 通过.

### 对照 writer/reviewer (判完后)
- writer 变更清单 #1-#8 与本审 diff 一致; reviewer PASS 结论与本审不冲突.
