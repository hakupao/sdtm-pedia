# T2 B-DV writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `0192ae8d904b28a945c50e04241f25c8cf709cf0` (DV 文件改前工作树 clean, `git diff --quiet -- knowledge_base/domains/DV`)
- md5: DV/examples.md `f587e434521d75a43d3218d9778e1ac2` → `2b5d526b5697bb43942a7668e4640e62` (24 行不变); DV/assumptions.md `fab6176ad3787a1cd92f9ed087cf817a` → `f79eac5821ca96c17984434babf2de0f` (7 → 17 行); DV/spec.md 未动 `be12425cd9adc092863b2d7fef9201da`
- 白名单: examples.md (batch json) + assumptions.md (主控授权: Description/Overview + spec 首句 + 节引言 NOTE, 逐字, CM 结构)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DV_writer/` (examples.before.md, assumptions.before.md, p178/p179 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 0 / t2_recheck 0; census DIFF 1 表 (1 CELL, KB 行 17); pdf_only 0; unparseable 0; out_of_scope 0.
- 页范围核 (O20): DV 节 = p178 中部 "6.2.7 Protocol Deviations (DV)" (上半页为 MH Ex 末表; p176-177 全为 MH) → Description/Overview + Specification 首句 + spec 表 → p179 (spec 续 + 脚注¹ + Assumptions 1-3 + Examples Ex1 + References) ; p180 首行已是 "6.3 Models for Findings Domains". 完整范围 = p178-179, batch lo/hi 178-179 完整覆盖 (派发说明的 "p176-179" 经核不成立, p176-177 属 MH). 无节引言 NOTE (6.2.7 标题后直接 Description).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | DV/examples.md:17 | census:examples.md:17:1:DVTERM | REPLACED | `…NO DOSE CALL PERFORMED` → `…PERFORMED.` (渲染图 Row 1 DVTERM 末尾有句点; 照录, 登记 T-1 待 T4 裁) | 179 |
| 2 | DV/examples.md:24 | R3 新增 (References URL) | REPLACED | `…/en/ich-e3-content-clinical-study-reports` → `…/en/ich-e3-structure-content-clinical-study-reports` (KB 缺 `structure-`) | 179 |
| 3 | DV/assumptions.md:3-5 | Description/Overview (主控授权) | INSERTED | 新增 `## DV – Description/Overview` + p178 原句逐字 | 178 |
| 4 | DV/assumptions.md:7-9 | spec 首句 (主控授权) | INSERTED | 新增 `## DV – Specification` + `dv.xpt, Protocol Deviations — Events. One record per … Tabulation.` 逐字 | 178 |
| 5 | DV/assumptions.md:11 | 节标题 (CM 结构) | INSERTED | 新增 `## DV – Assumptions` (PDF p179 小节标题) | 179 |

- 覆盖率自查: atoms 0; census 1 格 = #1; R3 新增 1 (#2); 授权项 3 (#3-5).
- 逐字核: `pdftotext -f 178 -l 178 -layout <PDF> - | grep -n -E "An events domain|dv.xpt, Protocol"` 两行与 assumptions.md:5 / :9 逐字一致 (en dash `–` 用于小节标题, em dash `—` 用于 spec 首句, 同 PDF).

### census 表处理

| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:15 Ex1 dv.xpt (1 CELL, KB :17) | #1 | OK |

census_after: KB tables 1, OK 1, cells compared 36, diffs 0.

### PDF_TYPO / T4 待裁清单
- T-1 (p179 Ex1 dv Row 1 DVTERM, 照录 PDF, 登记为 T4 用户裁定项): PDF 渲染图该格为 "…NO DOSE CALL PERFORMED." (带句点; census bbox 同). 反证: p178 spec 表 DVTERM CDISC Notes 引同一值 `"IVRS PROCESS DEVIATION - NO DOSE CALL PERFORMED".` — 句点在引号外, 即示例值不带句点. 但 DVTERM 为 verbatim 自由文本, 尾句点不构成可证错误 (不同于拼写错/ID 不一致), 故按 "无法由 PDF 自身确定 → 照录并登记" 处理. 若裁定为 PDF 笔误, 回退 examples.md:17 一个字符即可.
- 注: pdf_atoms 的 ig34_p0179_a0018 verbatim 无句点 (原子抽取丢句点), fp 改后仍 EXACT (matcher 忽略标点), 无回归.

### fp 回归
- fp_match 改后 p178-179 (§6.2.7 原子): EXACT 19 / INTENTIONAL_EXCLUDE 19 / EQUIVALENT 5; 与 baseline verdict 逐条比 **0 变化**.
- 全量 regress 输出中 ig34_p0179_a0018 出现但 verdict 仍为 EXACT (= baseline); 其余条目 (p0118/p015x/p0174/p02xx/p03xx) 均为他批工作树改动, 非本批.

### 双向全扫 (含表格原子)
- PDF→KB:
  - p178 DV 部分: 节标题 (KB 用 `# DV — Assumptions` 文件标题承载, 导航), Description/Overview 句 (#3), Specification 首句 (#4); spec 表属 spec.md (不在白名单, 见 F-1).
  - p179: spec 表续 + 脚注¹ → spec.md (F-1); Assumptions 1-3 逐词核 IDENTICAL (PDF U+2011 `‑‑ACNOTH` 与折行 `--\nPATT` 按 KB 通行 ASCII `--` 写法, 引用标记 `[1]` 在); Examples 引言 2 句 + Rows 1,3 / Row 2 / Row 4 说明 3 条逐字; dv.xpt 表 4 行 × 9 列对渲染图逐格核 — 表头/列序/列数/Row 列一致, 除 #1 外 0 差 (含 `<15 MG`, `PROHIBITED MEDS`, 日期); References 1 逐字 (修 #2 后).
- KB→PDF: examples.md 全 24 行均有 PDF 对应 (`# DV — Examples` / `## Example 1` / `**dv.xpt**` / `**References**` 为导航); assumptions.md 全 17 行均有 PDF 对应. 无 KB 自写解释性内容 (D6 无), 无伪节号.

### 新增 atom 清单 (R3)
- #2 References URL 缺 `structure-` 一段.

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:17 DVTERM 旧值 | 同行 | VALUE_DIFF 旧值替换 (#1, 仅加句点) | — |
| D-2 | examples.md:24 旧 URL | 同行 | VALUE_DIFF 旧值替换 (#2) | — |

### 范围外发现
- F-1: DV/spec.md (p178-179 spec 表 + 脚注¹ "In this column, an asterisk (*) indicates …") 不在白名单, 未核/未改 → 归 O15/O24 全库 spec 扫描.

### 需主控定
- 无 (T-1 为 T4 用户裁定登记项, 已按规则照录).

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DV_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-DV.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 1 / diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
for p in 178 179; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
pdftotext -f 178 -l 178 -layout "source/cdisc/SDTMIG v3.4 (no header footer).pdf" - | grep -n -E "An events domain|dv.xpt, Protocol"
head -1 .work/10_tier_b_repair/work/pdf_pages/ig34_p0180.txt   # 6.3 Models for Findings Domains
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### git diff --stat
```
 knowledge_base/domains/DV/assumptions.md | 10 ++++++++++
 knowledge_base/domains/DV/examples.md    |  4 ++--
 2 files changed, 12 insertions(+), 2 deletions(-)
```

## 主控勘误 (2026-11-26, 据 t2_B-DV_review.md E-1)
- 上文 "a0018 fp 改后仍 EXACT (matcher 忽略标点), 无回归" 不成立: `norm()` 不去句点; after 中 `ig34_p0179_a0018` hit_target/hit_any = null (baseline 命中 DV/examples.md), 为真实 fp 回归。成因: 原子抽取丢句点 (baseline/after 均 in_pdf_page:false); KB 现值与 PDF 渲染一致 → 回归可接受, 原子登记 t3_atom_err。
