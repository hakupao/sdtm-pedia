# T2 B-SC writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `beaefa9cbea4bdd86deffb7091650174ca411c83` (SC 文件改前 `git diff --quiet -- knowledge_base/domains/SC` = clean)
- md5: SC/assumptions.md `bd69fb3a8aea342bec54e9a794a2e05b` → `b2771af79138622abac5d919865604c1` (13 → 17 行); SC/examples.md `cba5350fb358cd24d14991b5356c7c30` → `bf0ddfae1d72f35e65ab991a236fe527` (53 行不变); SC/spec.md 未动 `1cf3915fdf6a124cf939b6c767f2fe8a`
- 白名单: examples.md (batch json) + assumptions.md (主控授权: Description/Overview + spec 首句 + 节引言 NOTE + 逐词偏差)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SC_writer/` (examples/assumptions.before.md, p339/p341/p342 渲染 110dpi, p342hi 220dpi 裁切, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 0 / t2_recheck 0; census DIFF 表 1 (examples.md:34 Ex2 sc.xpt, NO_PDF, 0 格); pdf_unparsed 1 (p342 Ex2 sc.xpt, 垂直居中); pdf_only 0; unparseable 0; out_of_scope 0.
- 节页范围核 (O20): §6.3.10 SC = p339 下部 (节标题 "6.3.10 Subject Characteristics (SC)" + Description/Overview; 上部为 RS Ex1) → p340 (Specification 首句 + spec 表) → p341 (spec 续 + 脚注 + Assumptions 1-3 + Examples Ex1 + Ex2 首段) → p342 上部 (Ex2 续 2 段 + 表 + Ex3; 其后 6.3.11 SS). batch lo/hi = 339-342 **完整覆盖**. 无节引言 NOTE.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | SC/examples.md:34 | census:examples.md:34 (NO_PDF) / pdf_unparsed p342 Ex2 sc.xpt 表头 | REPLACED | 表头 `SCORESU` → `SCORRESU` (渲染图; 与 spec 变量名一致) | 342 |
| 2 | SC/examples.md:37 | p342 Ex2 Row 2 SCDTC | SKIPPED_PDF_TYPO | KB 保留 `2017-04-01`; PDF 单元格 "20-17-04-01" → T-1 | 342 |
| 3 | SC/examples.md:38 | p342 Ex2 Row 3 SCDTC | SKIPPED_PDF_TYPO | KB 保留 `2017-06-10`; PDF "20-17-06-10" → T-1 | 342 |
| 4 | SC/assumptions.md:7-9 | spec 首句 (主控授权) | INSERTED | 新增 `## SC – Specification` + p340 spec 首句逐字 (CM 结构: Description 与 Assumptions 之间) | 340 |
| 5 | SC/assumptions.md:3-5 | Description/Overview | — (PRESENT) | 已逐字存在, 未改 | 339 |

- 覆盖率自查: atoms 0; census NO_PDF 表 1 → #1-3 (人工逐格, 17 列 × 3 行 = 51 格); 授权项 2 (#4-5).

### census / pdf_unparsed 表处理 (人工逐格)
- Ex2 sc.xpt (KB :34, PDF p342): 渲染图 110dpi + 220dpi 裁切逐格核. 列序/列数 (17 列 Row..SCDY) 一致; 表头仅 SCORRESU 一处差 (#1). 数据 3 行 × 16 值: STUDYID ABC-123, USUBJID 101, SCSEQ 1/2/3, EGESTAGE, "Estimated Gestational Age", "PREGNANCY-RELATED FINDINGS", SCORRES/SCSTRESC/SCSTRESN 100/135/265, DAYS ×2, SCMETHOD MENSTRUAL HISTORY/ULTRASOUND/BALLARD, VISITNUM 10/11/13.1, SCDY 196/226/297 全部一致; SCDTC Row 1 `2017-03-02` 一致 (PDF 折行 "2017-/03-02"), Rows 2-3 见 T-1.
- Ex1 sc.xpt (KB :13, p341) / Ex3 sc.xpt (KB :46, p342): census OK; 另以 layout 文本逐行分列脚本比对 14 行全等, 渲染图人工复核一致.
- census_after: KB tables 3, OK 2, NO_PDF 1 (Ex2, 解析器无法读居中表, 预期残留; 已人工核), diffs 0.

### PDF_TYPO 清单 (依据 = PDF 自身)
- T-1 (p342 Ex2 Rows 2-3 SCDTC): PDF 单元格渲染为 "20-17-04-01" / "20-17-06-10" (年份中多一连字符, 非合法 ISO 8601). 正确值由 PDF 自身确定: Row 1 同格式为 2017-03-02 / SCDY 196; Row 2 SCDY 226 = Row 1 + 30 天 → 2017-04-01; Row 3 SCDY 297 = +71 天 → 2017-06-10; spec SCDTC 为 ISO 8601. KB 保留正确值.

### 双向全扫 (含表格原子)
- PDF→KB: p339 SC 部分 (节标题/Description)、p340 spec 首句、p341 spec 脚注后 Assumptions 1-3 + Examples 叙述、p342 Ex2 两段 + Ex3 引言, 规范化逐句比对 (除标题前缀外) 0 缺; 3 张表见上. spec 表 (p340-341) 属 spec.md, 不在本批.
- KB→PDF: examples.md / assumptions.md 全文件逐行均有 PDF 对应; 无 KB 自写解释性内容 (D6 无), 无伪节号. Assumptions 1-3 逐字 (PDF "--\nXFN" 为折行).
- fp_match: SC 页 (p339-342) 无 fp 原子 (fp universe 未抽到); 全量 regress 2 条 (ig34_p0263 §6.3.5.7.3 MB/MS) 为他批工作树改动, `grep -cE 'p03(39|4[0-2])|SC/'` = 0.

### 新增 atom 清单 (R3)
- 无 (叙述 0 缺).

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:34 旧表头 `SCORESU` | 同行 | VALUE_DIFF 旧值替换 (#1) | — |

### 需主控定
- M-1: `SC/examples.md:3-5` 有 KB 自置的 `## SC – Specification (p340)` 节 + spec 首句 (全 KB 仅 SC 如此; PDF 中 spec 属 Specification 节, 位于 Assumptions 前). 现 assumptions.md 已按 CM 先例补入 (#4), examples.md 这份成为跨文件重复. 建议 D2 去重: examples.md:3-5 替换为一行交叉引用 (指向 assumptions.md `#sc--specification`), 或整段删除. 涉及删标题 (锚点变化; 已 grep 仓内无 `SC/examples.md#` 引用), 超出授权, 未动.

### 范围外发现
- 无.

### 触碰的 unparseable 表
- 无 (Ex2 为 census NO_PDF / PDF_UNPARSED, 已人工逐格; reviewer 须对渲染图逐格复核).

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SC_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-SC.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 2 / NO_PDF 1 / diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -cE 'p03(39|4[0-2])|SC/' $S/fp_regress.jsonl   # 0
for p in 339 341 342; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
pdftoppm -f 342 -l 342 -r 220 -x 0 -y 300 -W 2600 -H 500 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p342hi
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### git diff --stat
```
 knowledge_base/domains/SC/assumptions.md | 4 ++++
 knowledge_base/domains/SC/examples.md    | 2 +-
 2 files changed, 5 insertions(+), 1 deletion(-)
```

## attempt 2 (主控裁定 M-1, 2026-11-26)
- 变更: `SC/examples.md:3` — 原 :3-5 (KB 自加 `## SC – Specification (p340)` 标题 + 空行 + spec 首句) 替换为一行交叉引用 `> See [SC/assumptions.md](assumptions.md#sc--specification) for the dataset specification sentence.` (D2 跨文件去重). 其余行未动; examples.md 53 → 51 行, md5 `cc07ab726ff3a5ed7734183b8b749324`.
- 锚点核: assumptions.md:7 `## SC – Specification` → GitHub slug `sc--specification` (同 `PC/assumptions.md#pc-pp--relating-records` 先例规则); check_links 不验锚点, 已人工核. 仓内无 `SC/examples.md#sc--specification-p340` 引用 (attempt 1 grep).
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42.

### 删除清单 (追加)
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-2 | examples.md:3-5 (标题 + spec 首句) | examples.md:3 交叉引用 | D2 跨文件去重 (主控裁定 M-1) | SC/assumptions.md:9 (PDF 所属位置) |

- M-1 状态: **已处理**.

### git diff --stat (attempt 2 后)
```
 knowledge_base/domains/SC/assumptions.md | 4 ++++
 knowledge_base/domains/SC/examples.md    | 6 ++----
 2 files changed, 6 insertions(+), 4 deletions(-)
```

## 主控勘误 (2026-11-26, 据 t2_B-SC_review.md CONDITIONAL 修正清单; KB 不改)
- (1) T-1 Row 3 依据更正: 原写 "+71 天 → 2017-06-10" 算术错 (2017-04-01 + 71 天 = 2017-06-11)。正确依据: PDF "20-17-06-10" 按 ISO 8601 及 Row 1 格式去掉多余连字符, 数字照录 PDF → KB `2017-06-10`。Row 2 依据 (SCDY 226 = 196 + 30 → 2017-04-01) 成立。
- (2) 新增 T-2 (T4 用户裁定项): PDF 自身矛盾 —— 按 Row 1/2 推算 2017-06-10 应对应 SCDY 296, PDF 写 297; 单凭 PDF 定不了日期错还是 SCDY 错 → KB 两值照录 PDF (现状), 登记 O52。
