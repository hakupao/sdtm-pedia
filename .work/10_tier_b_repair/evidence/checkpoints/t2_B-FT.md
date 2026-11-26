# T2 B-FT writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `d84a22555eb38ab1a7ccdb7645425fec8a031aa5` (FT 文件改前工作树 clean)
- md5: FT/assumptions.md `6b9669d377fb114fcdf7492b44789a48` → `fab7d333c95400865cdd1657933b2542` (53 → 76 行, 纯插入 +23); FT/examples.md 未动 `cdd1cfcc47d1a6e0045e06d17980ac27`; FT/spec.md 未动 `9b283c65fafcd3e96bab582aba940d63`
- 白名单: examples.md (batch json) + assumptions.md (主控通用授权: Description/Overview + spec 首句 + 节开头引言; 见「需主控定」Q-1 关于 §6.3.9 父节引言的位置)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-FT_writer/` (assumptions.before.md, examples.before.md, ft_qrs.md, rs_qrs.md, p318/319/323/324 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 2 (REAL_GAP, p318 §6.3.9) / t2_recheck 0; census DIFF 0; pdf_only 0; unparseable 0; out_of_scope 0.
- 页范围核 (O20): §6.3.9 父节标题 + 引言在 p318 下半 (PE Ex1 之后); §6.3.9.1 FT = p319 (标题 + Description/Overview + spec 首句 + spec 表) → p320 (spec 续 + 脚注) → p321-323 (FT Assumptions 1-2 + QRS Shared 1-10) → p323 (FT – Examples 引言 + Ex1 ft.xpt) → p324 上部 (suppft.xpt; 其后 6.3.9.2 QS). batch pdf_ranges 319-324 + pdf_pages 318 = **完整覆盖** (含 p318 父节引言).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | FT/assumptions.md:7 | ig34_p0318_a017 | INSERTED | 无 → "The SDTMIG includes the FT, QS, and RS domains … shared assumptions … domain sections." 逐字 | 318 |
| 2 | FT/assumptions.md:9 | ig34_p0318_a018 | INSERTED | 无 → "CDISC develops controlled terminology and publishes supplements … copyright holder." 逐字 | 318 |
| 3 | FT/assumptions.md:3 | R3 新增 (§6.3.9 标题, a014) | INSERTED | `## §6.3.9 Questionnaires, Ratings, and Scales (QRS) Domains (FT, QS, RS)` (NV §6.3.7 / LB §6.3.5 先例格式) | 318 |
| 4 | FT/assumptions.md:5 | R3 新增 (a015+a016) | INSERTED | §6.3.9 首段 3 句 ("This section includes domains … clinical classifications use case).") 逐字; 全 KB 原无 (fp ledger 标 EQUIVALENT 为假阳, grep 0 命中) | 318 |
| 5 | FT/assumptions.md:11-12 | R3 新增 (a019, a020) | INSERTED | 2 条 bullet (CT release downloads … / QRS supplements … + URL) 逐字 | 318 |
| 6 | FT/assumptions.md:14 | R3 新增 (a021) | INSERTED | "Each QRS supplement includes … where available." 2 句逐字 | 318 |
| 7 | FT/assumptions.md:16-18 | ig34_p0319_a003 Description/Overview (主控授权) | INSERTED | 新增 `## FT – Description/Overview` + p319 原句逐字 (CM/BE 结构) | 319 |
| 8 | FT/assumptions.md:20-22 | ig34_p0319_a006 spec 首句 (主控授权) | INSERTED | 新增 `## FT – Specification` + "ft.xpt, Functional Tests — Findings. One record per … Tabulation." 逐字 | 319 |
| 9 | FT/assumptions.md:24 | p321 "FT – Assumptions" 标题 | INSERTED | 新增 `## FT – Assumptions` (PDF 原标题; CM/BE 结构, 使原 assumptions 列表不挂在 Specification 下) | 321 |
| 10 | FT/examples.md:3 | R3 核 (examples 引言) | SKIPPED_PDF_TYPO | KB 保留 "…/qrs). Additional"; PDF p323 漏 ")." → T-1 | 323 |

- 覆盖率自查: atoms 2 = #1-2; census 0 项; R3 新增 4 (#3-6); 授权项 3 (#7-9); PDF_TYPO 1 (#10).

### census 表处理
- census DIFF 0. census_after (pdf_ranges 319-324): KB tables 2 (ft.xpt, suppft.xpt) 全 OK, cells 113, diffs 0. 两表对 110dpi 渲染图 (p323/p324) 人工逐格核: 表头/列序/列数/Row 1-6 值一致 (FTTEST/FTCAT 折行合并), suppft 1 行一致.

### PDF_TYPO 清单 (依据 = PDF 自身)
- T-1 (p323 FT – Examples 引言): PDF "(at https://www.cdisc.org/standards/foundational/qrs Additional FT examples" 缺右括号与句点. 依据: 平行句 p328 QS – Examples 为 "…/qrs). Additional QS examples"; 左括号无闭合. KB 保留 "qrs). Additional".
- 另 (QRS Shared Assumptions, 未改, 与 B-RS T-5/T-6 同): p322 6a "an resolution" (KB "a resolution"), p323 10 "--STRNC" (KB "--STNRC") — KB 已为正确值, 与 RS/QS 副本一致, 登记沿用 B-RS T-5/T-6 依据.

### 预期 fp 回归
- fp_match 改后: `grep -E 'p03(1[89]|2[0-4])|FT/' fp_regress.jsonl` = 0. 全量 regress 2 条 (ig34_p0363_a016/a017, §6.4.2 FA) 为他批工作树改动, 非本批.
- p318 a015-a021 改后 hit_target 全部 = FT/assumptions.md (改前 a017/a018 无命中). p319_a003/a006 hit_any = FT/assumptions.md (该节 targets 未列 assumptions.md, 故 hit_target null; 逐字已在).
- p319-320 spec 表行 (a007-a023, p320_a001-a023) 属 spec.md, 不在白名单 → 范围外 F-2.

### 双向全扫 (含表格原子)
- PDF→KB: p318 §6.3.9 引言 (标题 + 6 段/条) 逐句 → assumptions.md:3-14 逐字 (pdftotext 折行均整词边界, 无连字符). p319 Description/spec 首句 → :18/:22 逐字. p321 FT assumptions 1-2 → :28/:30 逐字. p321-323 QRS Shared 1-10 → :32-76: 与 PDF 文字逐词一致, 仅差 (a) T-5/T-6 已登记两处, (b) 弯引号 (见 Q-2). p323-324 Examples 引言 (T-1)、Ex1 标题/叙述、ft.xpt 6 行、suppft 引言 + 1 行 → examples.md 全一致.
- KB→PDF: assumptions.md 与 examples.md 全文件每行均有 PDF 对应; 无 KB 自写解释性内容 (D6 无), 无伪节号; `# FT — Assumptions` / `# FT — Examples` / `## Example 1` / `**ft.xpt**` 为导航.
- 未加 `§6.3.9.1 Functional Tests (FT)` 子节标题 (文件即 FT; NV/LB 先例亦未对域本身加号); 如需可由主控定.

### 新增 atom 清单 (R3)
- #3 (a014 标题), #4 (a015, a016), #5 (a019, a020), #6 (a021).

### 删除清单
- 无 (纯插入).

### 需主控定
- Q-1 (位置): §6.3.9 父节引言 (含本批 2 个 REAL_GAP 原子) 放在 FT/assumptions.md 顶部 (`## §6.3.9 …`, 位于 FT Description 前). kb_files 仅 examples.md; 依据 = 通用授权 "节标题与 Description 之间的引言" + NV/assumptions.md:3 (§6.3.7)、LB/assumptions.md:3 (§6.3.5) 父节引言先例 + T1 triage 候选位置. 若主控不认可, 回退 = 删 assumptions.md:3-15.
- Q-2 (QRS Shared Assumptions 弯引号; 按本批派发特别事项 "FT 副本差异列需主控定" 未改, 虽追加授权覆盖逐词级偏差): FT 副本 (改后 :47 QRS 3, :50-54 QRS 4a-iii.1, :67 QRS 7a) 用直引号 "standardized responses" ×5 / "total" / instrument's ×5 (含 CT 一处 instrument's CT); PDF p321-322 为弯引号 “ ” ’. RS 副本已按 PDF 改为弯引号 (B-RS); 文字逐词一致. 建议: 按 PDF 改为弯引号 (与 RS 副本一致), QS 副本同样待核.

### 范围外发现
- F-1: O5 (ch03 Keys for FT) — 不在本批.
- F-2: spec.md (p319-320 spec 表行 + 脚注) 不在白名单, fp PARTIAL 若干 → 归 O15 spec 扫描.

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-FT_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-FT.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # KB tables 2 OK, diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p03(1[89]|2[0-4])|FT/' $S/fp_regress.jsonl   # 0
grep -rln "differ only in concept\|domains used to represent data from questionnaires" knowledge_base   # 改后仅 FT/assumptions.md
diff <(sed -n '/^## QRS Shared/,$p' knowledge_base/domains/FT/assumptions.md) <(sed -n '/^## QRS Shared/,$p' knowledge_base/domains/RS/assumptions.md)   # 仅弯引号差 (Q-2)
for p in 318 319 323 324; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 knowledge_base/domains/FT/assumptions.md | 23 +++++++++++++++++++++++
 1 file changed, 23 insertions(+)
```

## attempt 2 (2026-11-26, 主控采纳 reviewer L-1)
- 变更: `knowledge_base/domains/FT/assumptions.md:16` 新增 `## §6.3.9.1 Functional Tests (FT)` (+ 空行 :17), 位于 §6.3.9 父节引言末段 (:14) 后、`## FT – Description/Overview` (改后 :18) 前. 标题文字逐字 = p319 首行 "6.3.9.1 Functional Tests (FT)"; 记法同 NV `## §6.3.7.1` / RS `## §6.3.9.3.1`, 层级 `##` 与同文件同类节一致. 其余行未动 (纯插入 2 行).
- md5: `fab7d333c95400865cdd1657933b2542` → `0cd5c84b1a7f7976d5e3c7a37d622cad`; `git diff --stat -- knowledge_base/domains/FT` = assumptions.md 25 insertions (attempt 1 的 23 + 2).
- 原 attempt 1 行号 :16 及之后统一 +2 (Description :18-20, Specification :22-24, FT – Assumptions :26).
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → 42.
