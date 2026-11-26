# T2 B-ch03 writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base: ch03 工作树改前 = HEAD 版 (md5 `c9a5f6b80299f3d5e39e78cc939549f4`, `git show HEAD:` 同); 改后 md5 `ce391485beb5525ecb245aaba39bc835` (130 → 125 行). 只改 `knowledge_base/chapters/ch03_submitting_data.md`.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-ch03_writer/` (ch03_before.md, parse.py, pdf_rows.json, cmp.py, bidi.py, bidi2.py, p17-p21 渲染 110dpi, kbA/kbB, fpA/fpB.jsonl)
- 页范围核 (O20): §3 = p17 ("3 Submitting Data in Standard Format") → p21 (3.2.2 Conformance 末条); p16 为 §2.7 末, p22 起 §4. batch pdf_ranges 17-21 **完整覆盖** (pdf_pages 只列 17).
- 本批: atoms 1 (VALUE_DIFF) / t2_recheck 0 / census DIFF 0 / pdf_only 0 / unparseable 1 (ch03:29 → 改后 :22, **已触碰**) / out_of_scope O5.
- 标题文字与层级未动 (`diff <(grep '^#' 改后) <(git show HEAD:… | grep '^#')` 为空).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | ch03:24 | ig34_p0017_a022 | REPLACED | CO Keys `COOTC` → `CODTC` | 17 |
| 2 | ch03:48 | O5 / p18 EG 行 Keys | REPLACED | 删多出的 `, EGREPNUM` (PDF Keys 止于 EGTPTNUM) | 18 |
| 3 | ch03:52 | O5 / p18 IS 行 Keys | REPLACED | `ISSCMBDL, ISSTOPO` → `ISSCMBCL, ISTSTOPO` | 18 |
| 4 | ch03:66 | O5 / p19 RS 行 Keys | REPLACED | `RSTPTREF, RSEVAL, RSPTPNUM, RSEVALID` → `RSTPTREF, RSTPTNUM, RSEVAL, RSEVALID` | 19 |
| 5 | ch03:71 | 全表核 / p19 UR 行 Structure | REPLACED | `per location per visit` → `per location per per visit` (照录 PDF, 见 T-3) | 19 |
| 6 | ch03:37 | O5 / p18 BE 行 Keys | SKIPPED_PDF_TYPO | KB 保留 `BESTDTC`; PDF `BESDTC` → T-1 (**需主控定**) | 18 |
| 7 | ch03:49 | O5 / p18 FT 行 Keys | SKIPPED_PDF_TYPO | KB 保留 `FTTESTCD`; PDF `TESTCD` → T-2 (**需主控定**) | 18 |
| 8 | ch03:7 | R3 新增 (p17_a00x) | REPLACED | "but which assist sponsors:" → 补 "in preparing their datasets" | 17 |
| 9 | ch03:9-10 | R3 新增 | REPLACED | 粗体标签+破折号改写 bullet → PDF 两句原文 ("The CDISC Notes column provides …" / "The Core column indicates …") | 17 |
| 10 | ch03:16 | R3 新增 | REPLACED | §3.2 段按 PDF 句序重排: "In addition, comments …" 移回段末; " — typically" → "classes—typically" (PDF em dash 无空格); 补 "Dataset definition metadata should include the dataset filenames, … , as shown in Section 3.2.1, Dataset-level Metadata." (原为改写列表, 丢交叉引用) | 17 |
| 11 | ch03:20 | p17_a020 (NOTE) | REPLACED | "**Note:** The key variables …" → "Note that the key variables …"; `sponsor's` → `sponsor’s` (PDF 弯撇) | 17 |
| 12 | ch03:92 | R3 | REPLACED | "records in a dataset" → "records within a dataset" | 20 |
| 13 | ch03:96 | R3 | REPLACED | "**Definitions:**" → "**Definitions**" (PDF 小标题无冒号) | 20 |
| 14 | ch03:98, 100 | R3 (p20_a018/a025 等) | REPLACED | 两个 bullet+粗体 → PDF 两段; natural key 句补 "of an entity" / "that entity"; `"unnatural"` → `“unnatural”` | 20 |
| 15 | ch03:106 | R3 | REPLACED | "**Example:** The Vital Signs" → "For example, the Vital Signs" | 20 |
| 16 | ch03:116-125 | R3 | REPLACED | Conformance 1.-10. 编号 → PDF bullet (文字未变) | 21 |

覆盖率自查: atoms 1/1 (#1). O5 = 表 Keys 列 5 处差异 (#2-4 改, #6-7 PDF_TYPO) + 全表 Structure 1 处 (#5). 叙述 R3 #8-16.

### 表格全表双向核 (O5; unparseable ch03:22 触碰, **reviewer 须对 p17-p20 渲染逐格人工核**)
- 方法: `pdftotext -bbox` 词框 (`work/pdf_bbox/ig34_p0017-0020.tsv`) 按表头 7 列 x 位置切格、按 Dataset 列起行 (parse.py → pdf_rows.json, 63 行) vs KB 63 行逐格 (cmp.py); 差异再对 110dpi 渲染图人工确认.
- 行集合双向: PDF 63 行 = KB 63 行, 行序一致 (CO…OI), 无缺行/多行. 列: 7 列名/列序一致.
- 改前 7 格差 (CO/BE/EG/FT/IS/RS Keys + UR Structure); 改后 2 格差 = T-1/T-2 (登记的 PDF_TYPO). 其余 434 格逐字一致 (含 Description/Class/Structure/Purpose/Location).
- fp 原子 p18_a046 (MB 行) 不命中: 原子 verbatim 漏 "specimen" ("microbiology finding"), 渲染图为 "microbiology specimen finding per time point …" = KB → 原子抽取误差, KB 正确.

### 删除清单 (D2)
| # | 原位置 (改前) | 被删内容 | 原因 | 替代 / 保留 |
|---|---|---|---|---|
| D-1 | ch03:18-19 | "Dataset definition metadata should include:" + 1 条 bullet | 同句改写 (丢 "as shown in Section 3.2.1, Dataset-level Metadata"), 该段已改为 PDF 原句 | :16 |
| D-2 | ch03:21 | **Note:** "In the event that no records are present in a dataset … should not be described in the Define-XML document." | **与 v3.4 矛盾**: PDF p453 (Changes from v3.3, §3.2 行) 写明该段在 v3.4 中 "Removed … as there are now guidelines in the MSG v2.0 and the Define-XML v2.1 standard". KB 把已删除的 v3.3 文字当现行规则 | 无 (p17-21 无此段) |
| D-3 | ch03:27 | "The Dataset-level Metadata table provides examples of dataset structures:" | KB 自写占位句 (表前), PDF 无; 按补充口径 D2 删 | — |
| D-4 | ch03:55 (改后 :48) | Keys 末 `, EGREPNUM` | VALUE_DIFF 旧值 (PDF 无) | — |
| D-5 | 各 REPLACED 行旧文字 (#8-16) | 改写版 | 已被同位置 PDF 原文逐字覆盖 (单段/单 bullet 对单 PDF 句, 无他原子承载冲突; fp 回归 0 证明) | 同行 |

### PDF_TYPO 清单
- **T-1 (需主控定)** p18 BE 行 Keys "BESDTC": SDTMIG v3.4 全文仅 p18 此处出现; BE spec (p143-144) 及 p145-147 例子变量为 `BESTDTC`, 无 BESDTC 变量 → 正确值可由 PDF 自身确定, KB 保留 `BESTDTC`. 与主控派单 "Keys 按 PDF 逐字修" 字面冲突, 故列需主控定 (若定为照录则改 `BESDTC` 并转 T4).
- **T-2 (需主控定)** p18 FT 行 Keys "TESTCD": 缺域前缀; FT spec p319 (×5)、p323 用 `FTTESTCD`, 同表其他 Findings 行均为 `<XX>TESTCD` → KB 保留 `FTTESTCD`. 同上冲突, 列需主控定.
- **T-3 (T4 候选, 已照录)** p19 UR 行 Structure "per location per per visit": PDF 自身 p312 UR spec 首句同样为 "per per" (KB `UR/spec.md:3` 亦照录), 缺词还是多词无法由 PDF 自身确定 → 照录 PDF.
- **T-4 (T4 候选, 已照录)** p18 IS 行 Keys "ISSCMBCL": SDTMIG v3.4 全文仅此一处, IS spec 无 ISSCM* 变量; KB 原值 "ISSCMBDL" 在 PDF 中不存在 → 照录 PDF `ISSCMBCL`. (同格 `ISTSTOPO` 在 IS spec p229-240 存在, 正常修正.)

### 叙述双向全扫 (p17-p21)
- PDF→KB: bidi2.py — PDF 文本去标题行与表格区后按句切, 归一化 (去 `**`、弯引号→直、空白合并、折行连字符合并) 后在 KB 非表格文本中子串查找 → **0 缺**. 变异校验: 对改前文件跑同脚本报 10 处缺 (#8-16 对应), 证明脚本有检出力.
- KB→PDF: bidi.py — KB 每个非表格、非标题行按句切, 查 PDF p17-21 归一化文本 → 仅 `:3 Source: SDTMIG v3.4, Section 3 (Pages 17-21)` 不在 PDF (KB 导航行, 保留). 无 KB 自写解释性内容 (D6 无), 无伪节号.
- `---` (:112) 为 KB 分隔线 (导航), 保留.

### 范围外发现
- F-1: `## 3.2 Using the CDISC Domain Models in Regulatory Submissions — Dataset Metadata` PDF 为 "–" (en dash); `## 3.2.2 Conformance` 层级与 3.2.1 不对称 (PDF 3.2.2 为 3.2 子节, 应 `###`). 规则 6 不改标题, 未动.
- F-2: `UR/spec.md:3` 照录 "per per" — 与 T-3 同一 PDF 问题, 若 T4 裁定改则两处同改.
- F-3: 各域批 writer 报告的 "O5 ch03 Keys" — `t2_B-BE.md` F-2、`t2_B-RS.md` F-1、`t2_B-FT.md` F-1 — 本批已处理 (BE/FT 为 T-1/T-2 待主控定, RS 已修); EG/IS/CO 亦已修.

### 需主控定
1. T-1 (BE `BESDTC`) / T-2 (FT `TESTCD`): 按 dispatch notes PDF_TYPO 规则 KB 保留正确值 (现状), 还是按派单 "逐字" 照录 PDF.

### fp_match (隔离副本, 只差 ch03)
- kbA = 当前 KB + ch03 改前版; kbB = 当前 KB. `regressions=0 new_hits=8 RESULT: GREEN`.
- p17-21 原子 hit_target: 145 → 153 / 156. 新命中: p17_a020 a022, p18_a034 a042, p19_a018 a028, p20_a018 a025. 仍不命中 3: p18_a012 (BE, T-1)、p18_a036 (FT, T-2)、p18_a046 (原子抽取误差, 见上).

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-ch03_writer
python3 -I $S/parse.py $S/pdf_rows.json          # PDF 表 63 行 (bbox)
python3 -I $S/cmp.py knowledge_base/chapters/ch03_submitting_data.md   # diffs 2 (= T-1/T-2); 对 $S/ch03_before.md → diffs 7
python3 -I $S/bidi2.py knowledge_base/chapters/ch03_submitting_data.md # PDF→KB 0 缺; 对 ch03_before.md → 10 缺
python3 -I $S/bidi.py knowledge_base/chapters/ch03_submitting_data.md | grep KB-   # 仅 :3 Source 行
rm -rf $S/kbA $S/kbB; cp -R knowledge_base $S/kbA; cp $S/ch03_before.md $S/kbA/chapters/ch03_submitting_data.md; cp -R knowledge_base $S/kbB
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbA --out $S/fpA.jsonl
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbB --out $S/fpB.jsonl --baseline $S/fpA.jsonl --regress-out $S/fp_regress.jsonl   # regressions=0
for p in 17 18 19 20 21; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### git diff --stat
```
 knowledge_base/chapters/ch03_submitting_data.md | 59 +++++++++++--------------
 1 file changed, 27 insertions(+), 32 deletions(-)
```
