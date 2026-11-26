# T2 B-EG reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus) — verdict: **PASS**

- base `0dc4f14`; 范围: `git diff 0dc4f14 -- knowledge_base/domains/EG/` (assumptions.md +6, examples.md +23/-23). 工作区其他 KB 改动 (AE/GF/ch02/ch04) 属并行批, 未审.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-EG_reviewer/` (渲染 p185/188-192 110dpi + p190 220dpi; scan.py)

### 命令 (可复跑, repo 根)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-EG_reviewer
P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
pdftoppm -f 190 -l 190 -r 220 -png "$P" $S/hi190                    # Ex1/Ex2 逐格人工核 (渲染图)
pdftotext -f 190 -l 190 -layout "$P" -                              # 独立方法 2: layout 列位 (Y/N 列位区分 EGDRVFL vs EGCLSIG)
pdftotext -f 192 -l 192 -layout "$P" - | awk '{print substr($0,length($0)-40)}'   # Ex4 EGDTC 折行值
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json  # exit 1 (RESULT RED 来自全局 PDF_ONLY); EG 4 表 :23/:48/:62/:101 全 OK
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # exit 1; hit_target 3759; regressions=15 全为 CP p215/218 + MB p257-263 (已提交前批), p185-192 / EG 文件回归 0
python3 -I $S/scan.py                                               # 双向逐句扫描, 见下
python3 tools/check_links.py | grep "live docs"                     # broken relative links: 18668 (live docs: 42) — 基线 42 未升
```

### 1. 表格 (G-TB4, 独立方法 = 220dpi 渲染图逐格 + pdftotext -layout 列位)
| 表 | 检查 | 结果 |
|---|---|---|
| Ex1 表头 (:23) | 列序 vs p190: …EGXFN, EGNAM, EGLOBXFL, EGDRVFL, EGCLSIG, VISITNUM, VISIT, EGDTC, EGDY | 一致 (24 列) |
| Ex1 r1-r12 (:25-36) | 每行逐格: EGXFN PQW436789-07.xml (r1-11; r12 空) / EGNAM "Test Lab" (r1-11; r12 空) / EGLOBXFL 全空 / EGDRVFL r5,r6=Y / EGCLSIG r1=N r2=Y / VISIT "Screening 1" / EGDTC 2003-04-15T11:58 / EGDY -36 | 12 行全一致 |
| Ex1 单格 | r6 EGSTRESC/N 446; r7-8 SPRTARRY; r9 STSTWUW + EGTEST "ST Segment, T wave, and U wave"; r10 CHYPTENL; r11 EGCAT 空, EGORRES/EGSTRESC "OTHER INCORRECT ELECTRODE PLACEMENT"; r12 EGCAT 空 | 一致 |
| Ex1 Y/N 归属 | layout: r5/r6 "Y" 位于 r1/r2 N/Y 左侧一列 → EGDRVFL; r1/r2 → EGCLSIG | 一致 (与 Assumption 9 / Rows 5-6 叙述 "Y in the EGDRVFL column" 相符) |
| Ex2 (:48-55) | 表头含 EGSTRESN (EGSTRESC 后, 全空); r1 NORMAL/NORMAL, SCREEN I; r2 ABNORMAL/ABNORMAL, EGLOBXFL Y, SCREEN II; r3-5 未改 | 一致 |
| Ex4 r3/r6 (:105/:108) | EGDTC 2014-02-11T14:32:13.3 / 2014-02-11T15:32:14.2 (layout 折行行逐个读出 12.3,12.3,13.3,13.3,13.3,14.2,14.2,14.2) | 一致; r4/r7 未改且一致 |
| Ex3 (:62) | 未改, census OK | — |
- census_after: EG 4 表全 OK, 无 DIFF/NO_PDF; 本批 pdf_only / pdf_unparsed 0.
- atom ig34_p0190_a011 fp 仍未命中: 原子 verbatim 自身抽错 (`P0W436789` vs 渲染 `PQW`, VISIT 漏折行 "1") → ATOM_ERR, KB 正确, 同意 writer.

### 2. 新增节 (assumptions.md)
- `## EG – Description/Overview` + 定义句: 与 p185 L23-25 逐字一致 (合并折行). ig34_p0185_a020 fp hit_target = EG/assumptions.md.
- `## EG – Assumptions`: p188 L16 原标题, en dash 与 PDF 同.
- 位置: H1 后先 Description/Overview 再 Assumptions, 与 SC/AE/CM/DM/IS 同惯例 (`grep -n '^## ' domains/*/assumptions.md`). 无外部锚点引用 EG/assumptions.md# (grep 0) → 无链接影响.

### 3. T4 登记项 (writer T-1..T-3) — 确认均不能由 PDF 唯一确定, 照录 PDF 合规
| T | PDF 证据 | 判定 |
|---|---|---|
| T-1 | p189 "grouped using EGCAT = \"FINDINGS\"" vs p190 表 EGCAT FINDING ×4 | 叙述与表互相矛盾, 哪方为准 PDF 内无第三证据 → T4 |
| T-2 | p190 "The ECG at Visit \"SCREEN 2\"" vs 表 r2 VISIT SCREEN II (VISITNUM 2) | 可能指 VISITNUM 2 的同一访视, 非确定笔误 → T4 |
| T-3 | p190 "performed by the principal investigation" vs EGEVAL PRINCIPAL INVESTIGATOR | 极可能笔误, 但 "investigation" 是真词, 改动属语义改写而非拼写修正 → 照录 + T4 合理 (LOW: 用户可裁为改 "investigator") |

### 4. 双向逐句扫描 (reviewer 自做, p185 Description + p188 "EG – Assumptions" ~ p192; 含表格行)
- 方法: scan.py 归一 (空白, U+2011/弯引号→ASCII, 去列表编号/Markdown), PDF 句 ⊂ KB 文本 / KB 句 ⊂ PDF 文本.
- PDF→KB: 残留项仅为标题行 (`EG – Description/Overview`, `EG – Assumptions` 在 KB 为 `##` 标题) 与表头 / 表格折行碎片 (由 census + 人工逐格覆盖) → 叙述缺口 0. 含 Assumption 2a URL、8 "Section 4.5.5 … (see also EG Example 1)"、9 "(see Section 4.1.8.1 …)" 均在.
- KB→PDF: 0 句无出处 (无 KB 自写 / D6 无需标注).
- 表格类: 4 张表 census OK + 上表人工逐格.

### 5. 无副作用 / 结构行签字
- EG diff 仅 assumptions.md (+6 行: 2 标题 + 1 句 + 3 空行) 与 examples.md 3 张表的行; 未动 H1 / `## Example N` / `**eg.xpt**` / 叙述.
- 结构行签字: assumptions.md `## EG – Description/Overview` ✔, `## EG – Assumptions` ✔; examples.md Ex1 表头+分隔线 ✔ (24 列对齐), Ex2 表头+分隔线 ✔ (19 列对齐).
- fp EG 回归 0; check_links live docs 42 (= 基线).

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无阻断问题 | — |
| T-3 | PDF_TYPO 取舍 | LOW/建议: 用户裁 T4 时可考虑按 EGEVAL 改 "investigator" | p190 "performed by the principal investigation" |
| O6 | out_of_scope 标签 | 同意 writer X-3: O6 "Example 3" 实为 Example 1 (KB :23-36) | p190 首表 |

R2 recheck: 本批 t2_recheck 0, 不适用.
