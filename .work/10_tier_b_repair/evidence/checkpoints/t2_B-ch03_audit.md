# T2 B-ch03 auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

- 判法: 先独立判 (PDF txt p17-21 + 110dpi 渲染 p17-p20, `pdftoppm -f N -l N -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf"`), 判完才读 writer/reviewer 报告对照.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-ch03_auditor/` (sample.json, tab.py, pdf_table.txt, p17-p20 png)
- 抽样: t2_auditor_v1.0 脚本, seed 20261126; 唯一偏离 = PAGES 由 batch pdf_pages [17] 扩为 range(17,22) (brief: 完整节页范围 p17-21). 结果 C=0 (本批 atoms 仅 1 个 TABLE_ROW), P=57, N=10 (全部来自 P−C).
- KB md5 `ce391485beb5525ecb245aaba39bc835` (= writer 报告改后值); mtime 05:09:13Z 早于 writer done 05:11:32Z / reviewer done 05:15:48Z.

### 抽样表 (N=10)
| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0020_a030 | p20 Definitions 第 2 段首句: surrogate key 定义 | ch03:100 | 否 | 是 | §3.2.1.1 ✓ | 逐字 |
| 2 | ig34_p0020_a028 | p20 natural key 段: 因有业务含义与业务耦合、需随需求返工 | ch03:98 | 否 | 是 | §3.2.1.1 ✓ | 逐字 |
| 3 | ig34_p0017_a005 | p17 §3.1: 2 列阴影列不发 FDA, 帮助 sponsor "in preparing their datasets" | ch03:7 | 否 | 是 | §3.1 ✓ | 逐字 (改动 #8, 补回丢失短语) |
| 4 | ig34_p0020_a040 | p20 §3.2.1.2 "For example, the Vital Signs (VS)…" | ch03:106 | 否 | 是 | §3.2.1.2 ✓ | 逐字 (改动 #15) |
| 5 | ig34_p0021_a002 | p21 首: 每受试者 5 条记录, 参数名在 Test Code/Name | ch03:106 | 否 | 是 | §3.2.1.2 ✓ | 逐字 (原子 section 标 §3.2.1 [Findings] 为抽取标注, PDF 实属 3.2.1.2) |
| 6 | ig34_p0017_a008 | p17 CROSS_REF "Section 4.1.5, SDTM Core Designations" | ch03:10 | 否 | 是 | §3.1 ✓ | 逐字 |
| 7 | ig34_p0020_a017 | p20 Keys 列目的 → 列出全部 natural keys | ch03:92 | 否 | 是 | §3.2.1.1 ✓ | 逐字 |
| 8 | ig34_p0020_a019 | p20 keys 应与 Define-XML 结构描述一致 | ch03:92 | 否 | 是 | §3.2.1.1 ✓ | 逐字 |
| 9 | ig34_p0020_a041 | p20 "These data are all submitted in the normalized SDTM" (跨页句前半) | ch03:106 | 否 | 是 | §3.2.1.2 ✓ | 逐字 |
| 10 | ig34_p0017_a018 | p17 §3.2 末句 "In addition, comments can also be provided where needed." | ch03:16 | 否 | 是 | §3.2 ✓ (段末, 与 PDF 句序一致) | 逐字 (改动 #10 移回段末) |

- **独有丢失 0, 忠实度错误 0.**
- 扩展机械核: P 全 57 prose 原子归一化 (弯引号/en dash/空白) 后在 KB 子串查找 → 57/57 命中. p17-21 全部非表格原子 (HEADING 8 / NOTE 2 / LIST_ITEM 12 / SENTENCE 42 / CROSS_REF 1 / TABLE_HEADER 4 / CODE_LITERAL 63) 仅 `p17_a001` 章标题 "3 Submitting Data in Standard Format" 不逐字 (KB 标题行 "Chapter 3: …", 导航).
- 反向 KB→PDF (非表格行按句切, 查 p17-21 归一化文本): 仅 :1 标题 / :3 Source 行不在 PDF (导航). 无 KB 自写解释性内容残留, D6 无需项.

### 叙述改动逐字核 (要求 ≥4, 实核 9/9)
#8 (:7 "in preparing their datasets") / #9 (:9-10 两 bullet 原句) / #10 (:16 句序 + "classes—typically" 无空格 em dash + "as shown in Section 3.2.1, Dataset-level Metadata" 交叉引用) / #11 (:20 "Note that…", sponsor’s) / #12 (:92 "within a dataset") / #13 (:96 "Definitions" 无冒号) / #14 (:98 "of an entity"/"that entity", “unnatural”) / #15 (:106 "For example, the") / #16 (:116-125 bullet, 10 条文字逐字) —— 全部与 p17/p20/p21 txt 及 p17 渲染图一致.

### 数据集表 (O5, ch03:22-86, 63 行 × 7 列)
- 独立方法: 按 pdftotext 定宽文本表头列位置切格 (`tab.py`, 与 writer 的 bbox 解析不同) → 63 行 = KB 63 行, 行序一致. 自动差异经人工归因: SE/SM/SV/AG/CM/EC (p17 列漂移)、IE、RELSPEC 为解析器串列 (对 txt 与渲染核实 KB 正确); 真实差异仅 2 格 = BE Keys (PDF `BESDTC`) / FT Keys (PDF `TESTCD`) = 已登记 T-1/T-2.
- 渲染图逐格人工核 (≥8 行要求, 实核 14 行): p17 CO (Keys …COREF, CODTC ✓) / EC (per mood, ECMOOD ✓); p18 BE (渲染 BESDTC → T-1) / EG (Keys 止于 EGTPTNUM, 无 EGREPNUM ✓) / FT (渲染 TESTCD → T-2) / IS (ISSCMBCL, ISTSTOPO ✓) / MB (microbiology specimen finding ✓, 证 ig34_p0018_a046 原子漏 "specimen" = 原子抽取错) / MS ✓; p19 OE (14 键顺序 ✓) / RS (RSTPTREF, RSTPTNUM, RSEVAL, RSEVALID ✓) / UR ("per location per per visit" 照录 ✓ → T-3) / RP (STUDYID, DOMAIN, … ✓) / TI ✓ / TS ✓.
- PDF_TYPO 依据复核: T-1 `BESDTC` 全书仅 p18 出现, BE 节 p144-147 均 `BESTDTC` → PDF 自身可定, KB 写正确值 ✓. T-2 FT spec p319 `FTTESTCD` ×5, 同表他行均带前缀 → 可定 ✓. T-3 p312 UR spec 首句同为 "per per" → 不可定, 照录 + T4 ✓. T-4 `ISSCMBCL` 全书仅 p18, KB 旧 `ISSCMBDL` 全书无 → 照录 + T4 ✓.

### 删除清单核
- D-1 (旧 :18-19 "Dataset definition metadata should include:" + bullet): 内容已由 :16 PDF 原句承载, 且原改写丢了 "as shown in Section 3.2.1…" → 删除正当.
- D-2 (旧 :21 Note "In the event that no records are present…"): 读 p453 原文 —— Changes 表 Section 3 / 3.2 行: "Removed the following paragraph as there are now guidelines in the MSG v2.0 and the Define-XML v2.1 standard: 'In the event that no records are present in a dataset …'" → v3.4 已删, KB 保留即与 v3.4 矛盾, p17-21 无此段 → D2 删除正当 ✓.
- D-3 (旧 :27 "The Dataset-level Metadata table provides examples of dataset structures:"): PDF 无, KB 自写占位句 → 按口径删 ✓.
- D-4 (EG `, EGREPNUM`): 渲染 p18 无 → ✓. D-5 改写旧文字被同位置原句覆盖 ✓.

### 其他
- 授权范围: `git diff HEAD --stat` 本批只动 ch03 (27+/32−); 标题行未改.
- 观察 (不计 FAIL, writer 已列 F-1): `## 3.2.2 Conformance` 层级应为 ### ; 3.2 标题 em dash vs PDF en dash — 均改前遗留.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (= 基线).
- G-TB8: trace.jsonl:307 writer (`oh-my-claudecode:executor`) subagent_done, :313 reviewer (`oh-my-claudecode:code-reviewer`) PASS; 无 B-ch03 `agent: main` 写 KB 记录; KB mtime 早于两者 → 终态即 reviewer 所审版本 ✓.
- 对照 writer/reviewer 报告 (判后): 结论一致, 无分歧.

**结论: PASS** (Rule A N=10 seed=20261126: 丢失 0, 忠实 0; 表 63 行双向一致, 仅 T-1/T-2 登记差异)
