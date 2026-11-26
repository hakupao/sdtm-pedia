# T2 B-SR reviewer
## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)
**Verdict: PASS**

Scope: SR/examples.md, SR/assumptions.md, SR/spec.md, FA/assumptions.md (vs c8802bf). Truth = `work/pdf_pages/ig34_p0375..0381.txt` + pdftoppm r110 p375-381, r200 p380 (scratch `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-SR_reviewer`).
KB diff 中其余文件 (MH 已 commit; REL*/TA = 别批 in-flight) 不属本批, 本批白名单外无改动.

### 命令 (可复跑, repo 根)
- `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json` → exit 1; KB tables 7: OK 6 / DIFF 1 (sr.xpt:14 Row7 SROBJ `BAU/mL` vs PDF `BAU mL` = T-1 登记). PDF_ONLY 332 为全局列表, 本批 p378-381 无.
- 全局 fp: `fp_match.py --baseline work/fp_baseline.jsonl` → RED 48 条, 页码 p118-p396, 无 p375-381 (来自已 commit 批次/别批 in-flight).
- 隔离 fp: $S/b = `git archive HEAD`, $S/a = b + 本批 4 文件 (`diff -rq` 仅 4 文件) → `fp_match.py --kb-root $S/a/knowledge_base --baseline $S/fpb.jsonl` → `regressions=0 new_hits=0 RESULT: GREEN`.
- `python3 tools/check_links.py | tail -1` → `broken relative links: 18668 (live docs: 42)` (≤42).

### 必查项
| # | 项 | 结果 | 证据 |
|---|---|---|---|
| 1 | Ex2 relrec R1-R3 行 2↔3,5↔6,8↔9 | 一致 | r200 p380: 每组 SR SRSPID n / SR SRSPID n+6 / EX EXSPID n; KB :66-83 18 行逐格一致 |
| 1 | Ex3 SRTESTCD | 一致 | p380 render Row1 `IDRLDIAM` = KB :97 |
| 1 | ag AGTRT | 一致 | p380 `Tuberculin PPD-S` = KB :107 |
| 1 | Ex3 叙述 N-1/N-2 | 一致 | p380 "standard tuberculin PPD (i.e., PPD-S)", "The time point variables show" = KB :87 全段逐字 |
| 2 | SR/assumptions.md 结构 | 一致 | 标题/句位置与 CM/assumptions.md :3/:7/:11 同构; a025 "SR – Description/Overview" + a026 句 = p375; "SR – Specification" + sr.xpt 首句 = p376 render 逐字; "SR – Assumptions" = p377; 假设 1-4 未动 |
| 3 | spec.md:93 | 接受 | PDF p376 `0.15 BAU mL`; 同 PDF p378 Row5/6/8 `BAU/mL` 可定正确值 → T-1 口径 |
| 3 | spec 39 变量 Label/Type/Role/Core | 39/39 一致 | 独立对 p376 render + p377 layout 文本逐行核; diff 仅 :93 一行 |
| 4 | FA/assumptions.md | 只加 :118 空行 + :119 交叉引用 | 标题未改; `../SR/assumptions.md` 存在; check_links 不升 |
| 5 | T-1 / T-3 | 保持正确值 | T-3: p377 `reactogencity`, KB :15 `reactogenicity` |
| 5 | T-2 | 照录表值 + T4 | p380 表 3 格 `2011-01-19T14:08:24`; 距 SRRFTDTC 08:30:00 = 53h38m24s ≠ 叙述 53h56m; 旧 KB 14:26 PDF 无出处; 叙述逐字保留 |

### 双向全扫 (p375 尾 + p376-381 vs SR 3 文件)
- PDF→KB: p375 SR 标题/描述句, p376 规格标题+首句, p377-378 假设 1-4, p378-381 Ex1-3 全部叙述句 + Rows 标签段 + 7 张表 (Ex1 sr 8 行, Ex2 sr 12 / ex 6 / relrec 18, Ex3 sr 3 / ag 1 / relrec 2) 全部在 KB 命中; 表格经 census (bbox) + render 目视双法.
- KB→PDF: examples.md 116 行全部有出处; 仅结构行无 PDF 原文: :1 `# SR — Examples` (承载 PDF "SR – Examples"), `## Example 1/2/3`, `**sr.xpt**` 等数据集标签, 表头分隔行.
- 未覆盖缺口: p376 spec 表脚注 "1 In this column, an asterisk…" 与 DOMAIN CT `SR` 空 → 全库 spec.md 惯例 (writer O-6, 交 O15/O16).

### G-TB6 结构行签字
| 行 | 类型 | 签字 |
|---|---|---|
| SR/assumptions.md:3 `## SR – Description/Overview` | PDF 原标题 p375 | OK |
| SR/assumptions.md:7 `## SR – Specification` | PDF 原标题 p376 | OK |
| SR/assumptions.md:11 `## SR – Assumptions` | PDF 原标题 p377 | OK |
| FA/assumptions.md:119 `> See [SR – Assumptions](…) for §6.4.5 Skin Response.` | 导航交叉引用 (D2, 不加 D6) | OK |
新增内容行: SR/assumptions.md :5、:9 (逐字), examples.md 11 行 (逐格/逐字), spec.md :93 (T-1). 无出处词句 0.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| spec.md:336 | 范围外 LOW | SRELTM Notes "indicated by EGTPTREF" 照录 PDF (PDF 自身复制错, 应为 SRTPTREF); 未改, 与 T-1 处理口径不一致, 交主控定是否登记 T-n | p377 "reference point indicated by EGTPTREF" |
| T-2 | 流程 LOW | T4 用户裁定项目前只在 checkpoint 登记, 主控需并入 T4 清单 | p380 SRDTC vs 叙述 |

### 人工逐格表 (render)
| 表 | 行 | 结果 |
|---|---|---|
| Ex2 relrec p380 | 1-18 | 一致 |
| Ex3 sr p380 | 1-3 (25 列) | 一致 |
| Ex3 ag p380 | 1 | 一致 |
| Ex1 sr p378 | 1-8 | 一致 (Row7 SROBJ T-1) |

### R2 recheck
本批 t2_recheck = 0; 新增 atom N-1/N-2 已逐字恢复.

## attempt 1 续 签字 (delta: SR/spec.md:336, T-4)
**Verdict: PASS**. diff 只改 :336 一个 token `EGTPTREF`→`SRTPTREF`, 其余与 PASS 版本相同. 依据 p377: 同表变量全部是 SR 前缀; 该行 label "Planned Elapsed Time from Time Point Ref"; 同一 Notes 的前句和第二例都写 (SRTPTREF) → 正确值能由 PDF 自身确定, T-4 keep-correct 成立.
隔离 fp (b + 本批 4 文件现状) `regressions=0 RESULT: GREEN`; `check_links` live docs 42. 原子 ig34_p0377_a015 不再逐字命中, 已由 T-4 登记覆盖.
