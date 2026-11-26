# T2 B-SM — Auditor (Rule A 独立抽检)

## attempt 1

- agent: `oh-my-claudecode:verifier` (opus); 2026-11-26; base = `HEAD` (未提交改动, `git diff HEAD -- knowledge_base/domains/SM`)
- 先独立判, 判完才对照 writer/reviewer checkpoint.

### 抽样
- 命令: `t2_auditor_v1.0.md` §抽样 脚本原样 (b=B-SM, seed=20261126), 输出写 scratch `t2_B-SM_auditor/sample.json` (未写入仓库).
- batch pdf_pages = 84,85,86 = SM 全节 (p84 "5.4" 起 → p86 ce.xpt 止), 无需扩页. kb_files 按主控口径视为 `SM/examples.md` + `SM/assumptions.md`.
- C=1 (ig34_p0084_a004), P=28 (含 p86 SV 原子 a003-a016 作对照), N=10; C 抽 1 + P−C 抽 9.
- p86 顶部 SM 叙述 (CE 段 2 句) 无 ledger 原子 → 人工补看渲染图, 见下 "补看".

### 样本判定
| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0084_a004 | p84:12-13 SM Description/Overview "special-purpose domain … timing … TM domain" | SM/assumptions.md:5 | 否 | 是 | 是 (新 `## SM – Description/Overview` 下) | C 原子 REAL_GAP; 逐字一致 |
| 2 | ig34_p0085_a020 | p85:30-32 MH records for diabetes … RELMIDS/MIDSDTC not needed | SM/examples.md:24 | 否 | 是 | 是 | 逐字 |
| 3 | ig34_p0084_a021 | p84:43 Assumption 2 "name … recorded in MIDS" | SM/assumptions.md:15 | 否 | 是 | 是 | 逐字 |
| 4 | ig34_p0086_a007 | p86:15-16 SV Desc "multiple dates and/or date/times … more complex" | — (SV/assumptions.md 无) | **是** | — | — | **范围外** (SV, 不在本批 kb_files); 见范围外发现 R-1 |
| 5 | ig34_p0086_a009 | p86:17-18 SV Desc "visit … within 1 day … multiday period" | SV/assumptions.md:5 | 否 | 是 | 是 | 对照; 范围外 |
| 6 | ig34_p0084_a022 | p84:44-45 Assumption 2a TMRPT="N" … "may an abbreviated version" | SM/assumptions.md:16 | 否 | 是 | 是 | PDF 缺词照录 (未扩写) |
| 7 | ig34_p0085_a009 | p85:13 Ex1 引言 "initial diagnosis and hypoglycemic events … Section 7.3.3 … Example 1" | SM/examples.md:5 | 否 | 是 | 是 | 交叉引用保留 |
| 8 | ig34_p0085_a010 | p85:14-15 Row 1 "October 2005 … SMDY is not populated" | SM/examples.md:7 | 否 | 是 | 是 | "SMDY" 照录 = O32 (已登记 T4) |
| 9 | ig34_p0085_a005 | p85:8-9 Assumption 3c end date/time less important … not collected | SM/assumptions.md:22 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0086_a011 | p86:19-20 SV Desc "planned but not expected visits due to a subject not completing the study" | SV/assumptions.md:5 | 否(信息点) | **否** | 是 | **范围外**; KB 作 "planned but not completed visits" (原子 verbatim 同错 = 抽取错, 渲染图为准); 见 R-1 |

- 本批 (kb_files 内) 独有丢失 **0**, 忠实度错误 **0**. 范围外 2 (#4 丢失, #10 改义), 不计本批 FAIL.

### 补充核验
- P 全 28 原子机械匹配 (规范化引号/空白): SM 16 中 15 精确命中; p0085_a019 唯一差为 PDF "hyypoglycemic" → KB "hypoglycemic" (T-3 PDF 拼写错, 规则正确). SV 12 中 7 命中, a003-a007 五句不在 SV/assumptions.md (范围外).
- 新增内容逐字: 3 个标题 `SM – Description/Overview` / `SM – Specification` / `SM – Assumptions` (EN DASH) 与 spec 首句 (EM DASH) 均与 `pdf_pages/ig34_p0084.txt` 字节级 grep -F 命中 1:1; 位置 = Description/Overview 与 Assumptions 之间, 合 CM/IS 先例.
- examples.md 改动 4 格 + 1 词, 对 p85/p86 渲染图 (110dpi) 逐一核: Row 4 "this milestone" (PDF 原词, 删 KB 扩写 "disease") ✓; sm.xpt Row3 SMSTDTC 2013-09-24T8:48 ✓; mh.xpt Row1 MHDY 1 ✓; ce.xpt Row1 CEENDTC 2013-09-01T2:30 照录 (T-2, T4) ✓; ce.xpt Row2 CESTDTC T8:48 ✓. ce.xpt Row2 CESEQ PDF=1, KB=2 = T-1 已登记 (同表连续编号可定).
- 补看 p86:1-2 (无原子): "In this study, information about hypoglycemic events was collected in a separate CRF module … distinct values of MIDS." → SM/examples.md:33 逐字, 位置在 ce.xpt 前 ✓.
- spec 脚注 p0084_a018 = triage IE (REDUNDANT_WITH_SPEC), 不入 P.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (= 基线 42).

### G-TB8
- trace: B-SM 有 `oh-my-claudecode:executor` subagent_done (04:28:19Z) + `oh-my-claudecode:code-reviewer` subagent_done PASS (04:31:28Z); 无 `agent: main` 写 SM 的记录.
- SM/assumptions.md 与 examples.md mtime 均 2026-11-26T04:26:52Z (< writer done < reviewer done) → reviewer 之后无 KB 改动. md5: assumptions `0a144f4887de3455873e9ea859a5eb40`, examples `7294b62b70be7aeff857f6a5b93807c1`.

### 范围外发现 (交主控登记, 不计本批)
- **R-1 SV/assumptions.md `## SV – Description/Overview`** (PDF p86:11-22): 缺前 5 句 (p0086_a003 "A special purpose domain …", a004, a005, a006, a007), KB 从 "The method for deriving …" 起; 且 "planned but not expected visits due to a subject not completing the study" 被改写为 "planned but not completed visits" (改义; pdf_atoms a011 verbatim 亦错 → 抽取错). B-SV kb_files 只含 SV/examples.md (p89-90), 当前无批覆盖 → 建议主控登记 O 项并授权 B-SV 扩到 SV/assumptions.md.

### 结论
**PASS** (本批: 丢失 0 / 忠实 0; 范围外 2 条归 R-1).
