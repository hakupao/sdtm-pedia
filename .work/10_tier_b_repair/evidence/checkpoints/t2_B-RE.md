# T2 B-RE writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `46a66e94695795a4f6d3ac2aecef248dbe7fbbe5` (RE 文件改前工作树 clean)
- md5: RE/examples.md `032395778604604b733e857fc427443e` → `40070b8992b755810c98bb7b61dae2a7` (76 行不变); RE/assumptions.md `e4165bb999b67f2c14304e8d794336ed` → `330cf84b764234aacae3c34259bf3be7` (13 → 17 行); RE/spec.md 未动 `47514a452db5bc75f9b7e9c9549f4d34`
- 白名单: examples.md (batch json) + assumptions.md (主控通用授权: Description/Overview / spec 首句 / 节引言 NOTE, 逐字)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-RE_writer/` (examples.before.md, assumptions.before.md, p308/310/311/312 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 0 / t2_recheck 0; census DIFF 1 表 (5 CELL, KB 行 17-21); pdf_only 0; unparseable 0; out_of_scope 0.
- pdf_ranges 覆盖核 (O20): RE 节 = p308 "6.3.7.7 Respiratory System Findings (RE)" (无节引言 NOTE; Description/Overview + spec 首句 + spec 表) → p309-310 (spec 续 + 脚注 + Assumptions 1-3 + Examples Ex1 引言) → p311 (Ex1 re/di/du + Ex2 引言 + re) → p312 (Ex2 suppre/di; 其后 6.3.7.8 UR). batch lo/hi = 308-312 **完整覆盖** (pdf_pages 311 仅 DIFF 表页).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | RE/examples.md:17 | census:examples.md:17:1:... | REPLACED | `...` 列数据格 `...` → 空 (渲染图: 表头 "..." 列各行为空格) | 311 |
| 2 | RE/examples.md:18 | census:examples.md:18:2:... | REPLACED | 同上 | 311 |
| 3 | RE/examples.md:19 | census:examples.md:19:3:... | REPLACED | 同上 | 311 |
| 4 | RE/examples.md:20 | census:examples.md:20:4:... | REPLACED | 同上 | 311 |
| 5 | RE/examples.md:21 | census:examples.md:21:5:... | REPLACED | 同上 | 311 |
| 6 | RE/assumptions.md:3-6 | ig34_p0308 Description/Overview (主控授权) | INSERTED | 新增 `## RE – Description/Overview` + p308 原句逐字 (Specification 前, CM/BE 结构) | 308 |
| 7 | RE/assumptions.md:9 | spec 首句 (主控授权) | — (PRESENT) | `re.xpt, Respiratory System Findings — Findings. One record per …` 已逐字存在, 未改 | 308 |

- 覆盖率自查: atoms 0; census 5 格 = #1-5 全处理; 授权项 2 (#6-7). 表头 "..." 列保留 (PDF 表头有该列; 叙述 "an ellipsis marks their place").
- #6 逐字: `pdftotext -f 308 -l 308 -layout <PDF> - | sed -n 3,4p` 去首尾空白拼接 vs `sed -n 5p RE/assumptions.md` → cmp IDENTICAL (折行处整词, 无连字符).
- p308 无节引言 NOTE (标题后直接 Description/Overview), 无需补.

### census 表处理
| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:15 Ex1 re.xpt (5 CELL) | #1-5 | OK |
| 其余 5 表 (:27 di, :36 du, :49 Ex2 re, :63 suppre, :74 Ex2 di) | census OK; 渲染图 p311/p312 人工逐格复核一致 | OK |

census_after: KB tables 6, OK 6, diffs 0.

### PDF_TYPO 清单
- 无. (注: p311 Ex2 叙述 QNAM="IRREA1" and "IREEA2" 与 suppre 表 REIRREA2 不一致, 属 PDF 原文, KB 逐字照录, 未改 —— 叙述非表格单元, 不登记 TYPO, 留 reviewer 知悉.)

### 双向全扫 (含表格原子)
- PDF→KB: p308-312 `pdftotext` (非 layout) 句级规范化比对脚本: RE examples/assumptions 范围内 0 缺, 除 F-1; 其余 MISS 均为 spec 表行 / spec 脚注 (spec.md 范围外, F-2) / 版权页脚 / UR 节. 6 张表对渲染图逐格人工核: 表头/列序/列数/Row 列一致, 改后 0 差.
- KB→PDF: examples.md 全文件每行均有 PDF 对应 (标题 `# RE — Examples` / `## Example N` / `**xxx.xpt**` 为导航); 无 KB 自写解释性内容 (D6 无), 无伪节号. assumptions.md 全文件有 PDF 对应.

### 新增 atom 清单 (R3)
- 无 (Description/Overview 属主控授权项 #6).

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:17-21 "..." 数据格 | 同行置空 | VALUE_DIFF 旧值替换 (#1-5) | — |

### 范围外发现
- F-1 (assumptions 列表, 按授权不改): RE/assumptions.md:17 assumption 3 "Any Identifier, Timing variables, …" — PDF p310 为 "Any Identifier variables, Timing variables, …" (缺 "variables" 一词).
- F-2: RE/spec.md 缺 p310 spec 表脚注 ("In this column, an asterisk (*) indicates …"; `grep -c asterisk` = 0); spec.md 不在白名单 → 归 O15/O16.

### 触碰的 unparseable 表
- 无.

### 环境注记
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → **44** (非 42). 新增 2 条来自 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-TE_review.md:87-88` (已在 HEAD, 非本批); RE 文件与本 checkpoint 无坏链. 需主控知悉.
- fp_match 全量 RESULT RED, regress 48 条, `grep -E 'p030[89]|p031[0-2]|RE/'` = 0 (均为他批 / §6.4.2 等, 非本批).

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-RE_writer
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 6 / diffs 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p030[89]|p031[0-2]|RE/' $S/fp_regress.jsonl   # 0
for p in 308 310 311 312; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # 44 (B-TE_review 2 条, 非本批)
```

### git diff --stat
```
 knowledge_base/domains/RE/assumptions.md |  4 ++++
 knowledge_base/domains/RE/examples.md    | 10 +++++-----
 2 files changed, 9 insertions(+), 5 deletions(-)
```

## attempt 2 (2026-11-26, 主控按 reviewer CONDITIONAL 指令)

- md5: RE/examples.md → `18d19ec35257afe16700ba2d7140be46`; RE/assumptions.md → `925dabf63f731a4dcf0f401144a389ce`; spec.md 未动.

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 8 | RE/examples.md:59 | C-1 (reviewer) | REPLACED (PDF_TYPO 已修正) | 叙述 QNAM `"IREEA2"` → `"IRREA2"` | 311 |
| 9 | RE/assumptions.md:17 | N-1/O30 (主控追加授权; 原 F-1) | INSERTED | assumption 3 "Any Identifier, Timing variables" → "Any Identifier variables, Timing variables" (PDF 逐字) | 310 |

### PDF_TYPO 清单 (attempt 2)
- T-1 (p311 Ex2 Rows 2-4 叙述): PDF "IREEA2" 为笔误。正确值可由 PDF 自身确定：同一句 "IRREA1" 是去掉 RE 前缀的写法；p312 suppre Row 4 的 QNAM = REIRREA2，QLABEL = "Inadequate Result Reason 2"。因此 KB 写 `IRREA2`。
- attempt 1 中 "无 PDF_TYPO" 的说明作废, 以本条为准.

### 删除清单 (attempt 2)
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-2 | examples.md:59 "IREEA2" | 同行 | PDF_TYPO 正确值替换 (#8) | — |

- F-1 状态: **已处理** (#9). F-2 (spec.md 脚注) 不变.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → 42.
- `git diff --stat -- knowledge_base/domains/RE`: assumptions.md 6 (+5 −1), examples.md 12 (+6 −6).
