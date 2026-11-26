# T2 B-GF reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus; 覆盖 writer attempt 1 + 续)

**verdict: CONDITIONAL** (1 项小修; 其余全部通过)

### 命令 (可复跑; S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-GF_reviewer)
| 命令 | rc / 关键输出 |
|---|---|
| `table_census.py --manifest $S/manifest.json --out $S/census_after.json` (GF/examples p220-228) | rc=1; `status {'OK': 9, 'DIFF': 1}; cells 1206; diffs 1` = mb.xpt r1 MBTEST (T-2). pdf_only 页 220-228 = 0; pdf_unparsed 本批 0 |
| `python3 -I $S/laycmp.py $S` (独立法: `pdftotext -layout` p225/p227, 按表头字符列位逐词归列, 非 bbox) | Ex1 gf 33 列 297 格 diff 0; Ex2 gf 29 列 87 格 diff 0; Ex4 gf 22 列 132 格 diff 0; Ex5 mb 16 格 diff 1 (=T-2) |
| `fp_match.py --baseline work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` | RESULT RED, 15 回归 = p0118/p0215/p0218/p0257-p0263 (他批, 非 GF); GF (p220-228) 回归 0 |
| `python3 -I $S/scan.py $S` (自写双向逐句扫, p220 §6.3.5.4 至 p228 §6.3.5.5 前; 两个 GF 文件) | 见下 "全扫" |
| `python3 tools/check_links.py` 末行 | `broken relative links: 18668 (live docs: 42)` ≤ 42; GF 相关条目仅 archive/releases 冻结副本 |
| `grep -rn -i "example-4-p227\|gf--example-4" .` (不截断) | 仅命中 writer checkpoint 自身; `GF/assumptions.md#` 在 knowledge_base/ web/src 无命中 (rc=1) |

### 修正清单 (CONDITIONAL)
| # | 位置 | 改法 | 依据 |
|---|---|---|---|
| C-1 | GF/assumptions.md:41 | `--ORNRLO, ORNRHI, --STNRLO` → `--ORNRLO, --ORNRHI, --STNRLO`; T-6 登记补 "PDF 漏 `--` 前缀 + 逗号后缺空格" | p224 item 9 "--ORNRLO, ORNRHI,--STNRLO"; 同列表 21 项全为 `--` 前缀, 正确值可由 PDF 自身确定 → 按取舍规则写正确值 |

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| assumptions.md:41 (T-6) | PDF_TYPO 取舍 | writer 只登记逗号空格, 漏 `ORNRHI` 缺 `--` (KB 照录) → C-1 | p224 "--ORNRLO, ORNRHI,--STNRLO, --STNRHI" |
| assumptions.md:43 | 导航措辞 (LOW, 不阻断) | 标题删后 "for this content" 无指代, 置于 assumption 9 后; 可选改 `Examples 4 and 5 are in [examples.md](...)` 之类, 主控定 | — (KB 导航行) |
| examples.md:147 | 段落 (LOW, 不阻断) | PDF "Next, a series…" / "Findings from this testing…" 两段, KB 合一段; 逐字一致 | p227 |

### 必查项结论
1. **Ex1/Ex2/Ex4 整表重建 + MB r1**: 独立 layout 法逐格 516 格 0 差异 (Ex1 旧 BRAF/GRCh38.p13/rs121913227 数据全部被替换为 PDF ATM/CDKN2A/GRCh37.75/COSM41596); 跨行合并 `LCNL-361`、`C12345-001`、`4401470-2-6`、`MSI-010418`、日期均与 layout 一致. MB r1: MBREFID INFLU0101 (=PDF, U-2), MBORRES "…SUBTYPE H3N2" (=PDF), MBTEST T-2. 一致.
2. **3 处叙述补入 + 脚注**: examples.md:41 "The DI example shows … ACME GenePanel 500." = p225 逐字 (原子 a006 "DI domain example" 为 ATOM_ERR, layout 为 "DI example"); :149 a021 五句 = p227 逐字; :151 NHOID Note = p227 逐字; 位置均按 PDF 顺序. assumptions.md:15 "CDISC/NCI codelist values are enclosed in parentheses." = p223 脚注逐字; 旧 URL 句在 p220-228 无出处 (grep rc=1). 通过.
3. **PDF_TYPO / U**: T-1 inheritabilty (KB 正确, p225 Ex2 同词拼对) OK; T-2 Idenitifcation (同页叙述 MBTEST = "Microbial Organism Identification") OK; T-3 respresented→represented OK; T-4 GFLINKID→GFLNKID (表头/relrec/p228 首句) OK; T-5 Row 1 句号 OK; T-6 见 C-1. U-1 REAL_TIME (layout 确为下划线, CT 无单值) 照录+T4 OK; U-2 INFLU0101 (GF/MS r1 为 .1, 不可单值确定) 照录+T4 OK.
4. **assumptions D-5..D-8**: D-6 Ex4 引言 = examples.md:118 逐字在; D-7 NHOID Note = examples.md:151 逐字在 (fp a022 hit 转 examples.md); D-5 标题 PDF 无, 无入链; D-8 见 2. 无 PDF 内容丢失. 锚点 `#example-4`/`#example-5` 对应 examples.md:116 `## Example 4` / :135 `## Example 5`, 可解析.
5. **双向全扫**: KB→PDF 未命中 6 句 = assumptions :15 (仅 "¹" 上标形式差) / :41 (T-6) / :43 (导航) / examples :5 (T-1) / :70 (T-3) / :167 (T-4), 无自写句. PDF→KB 未命中仅为 spec 表描述 (属 GF/spec.md, 非本批)、表格碎片拼接噪声、T-1/T-3/T-4/T-5/T-6; 无叙述缺失. 标题: `GF - Description/Overview` / `GF – Specification` / `GF – Assumptions` / `Example 1-5` 均与 PDF 同; `# GF — Assumptions`/`# GF — Examples` 为文件级结构标题, 无 KB 自写解释性子标题 (D6 无需 KB note).
6. **fp / census / links**: GF 回归 0; GF 新命中 p0223_a012/p0227_a018/a021/p0228_a009; 残留未命中 p0224_a010 (T-6) / a013 (T-1) / p0225_a004,a017 (FIGURE 描述) / a006 (ATOM_ERR) / a019 (T-3) / p0228_a011 (ATOM_ERR, PDF 为 "influenza extracted from") 均解释. census OK 9 / DIFF 1 (T-2). live docs 42.

### 无副作用
- GF diff 仅 GF/examples.md + GF/assumptions.md (白名单); 其他 KB 改动属并行他批 (ch02/ch04/AE/EG/model), 不在本审范围. Ex3/Ex5 其他表及 di 表未动且 census OK.

### G-TB6 结构行签字
- examples.md:27/28 (Ex1 表头+分隔), :62/63 (Ex2), :126/127 (Ex4) 表头按 PDF 列序 — 签字.
- examples.md:40/42/148/150/152 空行; assumptions.md:43 交叉引用 (D2 去重导航行) — 签字.
- 新增/改动数据行 9+3+6+1 = 19 行逐格有出处; 叙述新增 3 段 + 改 3 处 (T-3/T-4/脚注) 有出处; 无出处 0.

### R2 recheck
- t2_recheck = 0, 无.

## attempt 1 续 签字 (复审 writer 「attempt 1 续 2」delta)

**verdict: PASS**
- C-1 assumptions.md:41 `--ORNRLO, --ORNRHI, --STNRLO`: 依据 p224 item 9 列表其余项都带 `--`, 写入正确值; T-6 已改登记为两处 (缺 `--` + 缺空格). 通过.
- assumptions.md:43 交叉引用改为 "…Example 4 … for the microsatellite instability example and … Example 5 … for the NHOID note.": 纯导航, 两处指代都与 p227 内容对得上 (Ex4 MSI 引言, Ex5 NHOID Note), 锚点 examples.md `## Example 4`/`## Example 5` 仍存在; 不需要加 KB note. 通过.
- examples.md:147/149 拆为两段, 文字未改 = p227 分段. 通过.
- 复跑: `scan.py` KB→PDF 未命中仍为既有 6 处 (:15 上标 / :41 T-6 / :43 导航 / ex :5 T-1 / :70 T-3 / :169 T-4), 没有新增自写句; `laycmp.py` 表格 532 格只有 1 处差异 (T-2), 表格未受影响; `fp_match` 回归共 15 条, GF (p220-228) 0 条; `check_links` live docs 42.
