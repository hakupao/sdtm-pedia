# T2 B-SM writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `46a66e94695795a4f6d3ac2aecef248dbe7fbbe5` (SM 文件改前 `git diff --quiet -- knowledge_base/domains/SM` = clean)
- md5: SM/examples.md `0a194b2666fc57a96c1518cc67f55518` → `7294b62b70be7aeff857f6a5b93807c1` (40 行不变); SM/assumptions.md `d1a91a911f4b30b7922868c1dbb6154a` → `0a144f4887de3455873e9ea859a5eb40` (13 → 23 行); SM/spec.md 未动 `a1a8f357f84472a51b5a2f65926884cd`
- 白名单: examples.md (batch json) + assumptions.md (主控授权: 仅 Description/Overview + spec 首句; `## SM – Assumptions` 标题按 B-TU 先例 9478eb7 同步加, 防列表挂到 Specification 下)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SM_writer/` (examples.before.md, assumptions.before.md, p84/85/86 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl, desc/spec cmp 文件)
- 本批 atoms 1 (REAL_GAP) / t2_recheck 0; census DIFF 3 表 (5 CELL, KB 行 19/30/39/40); pdf_only 0; unparseable 0; out_of_scope 0.
- pdf_ranges 覆盖核 (O20): SM 节 = p84 "5.4 Subject Disease Milestones (SM)" (位于 DM Ex2 dm.xpt Row 2 续表之后; 无节引言 NOTE) → Description/Overview + spec 首句 + spec 表 + 脚注 + Assumptions 1-2a → p85 (2b-3d + Examples Ex1 引言/Row 说明/sm.xpt/mh.xpt) → p86 (ce.xpt; 其后 5.5 SV). **p83 不属 SM** (DM Ex2 / SE). batch lo/hi = 84-86 完整覆盖.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | SM/assumptions.md:3-5 | ig34_p0084_a004 | INSERTED | 新增 `## SM – Description/Overview` + p84 原句 ("A special-purpose domain that is designed to record the timing …") 逐字 | 84 |
| 2 | SM/assumptions.md:7-9 | spec 首句 (主控授权) | INSERTED | 新增 `## SM – Specification` + `sm.xpt, Subject Disease Milestones — Special Purpose. One record per …` 逐字 | 84 |
| 3 | SM/assumptions.md:11 | 结构 (B-TU 先例) | INSERTED | 新增 `## SM – Assumptions` (PDF 原小标题) | 84 |
| 4 | SM/examples.md:19 | census:examples.md:19:3:SMSTDTC | REPLACED | `2013-09-24T6:48` → `2013-09-24T8:48` (照印, 不补零) | 85 |
| 5 | SM/examples.md:30 | census:examples.md:30:1:MHDY | REPLACED | 空 → `1` (渲染图 Row 1 MHDY=1) | 85 |
| 6 | SM/examples.md:39 | census:examples.md:39:1:CEENDTC | REPLACED | `2013-09-01T12:30` → `2013-09-01T2:30` (照录 PDF; 登记 T-2, T4 用户裁定项) | 86 |
| 7 | SM/examples.md:40 | census:examples.md:40:2:CESTDTC | REPLACED | `2013-09-24T6:48` → `2013-09-24T8:48` | 86 |
| 8 | SM/examples.md:40 | census:examples.md:40:2:CESEQ | SKIPPED_PDF_TYPO | KB 保留 `2`; PDF `1` → T-1 | 86 |
| 9 | SM/examples.md:11 | R3 新增 (词替换) | REPLACED | Row 4 说明 "study day of this disease milestone was populated" → "this milestone" (PDF 原词; 该行仅承载 Row 4 说明) | 85 |

- 覆盖率自查: atoms 1 = #1; census 5 格 = #4-8 (全处理); R3 新增 1 (#9); 授权项 2 (#2-3).
- 逐字核: #1 / #2 用 `pdftotext -layout` p84 抽段 → `cmp` 与 KB assumptions.md:5 / :9 **IDENTICAL** (命令见下).

### census 表处理

| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:15 sm.xpt (1 CELL) | #4 | OK |
| examples.md:28 mh.xpt (1 CELL) | #5 | OK |
| examples.md:37 ce.xpt (3 CELL) | #6/#7 改; #8 PDF_TYPO | DIFF 1 (CESEQ, = T-1 预期残留) |

census_after: KB tables 3, OK 2, DIFF 1, diffs 1. CEENDTC 照录后与 PDF 一致故不残留. 3 表全部格对 p85/p86 渲染图人工逐格核: 表头/列序/列数/Row 列一致, 除 T-1 外 0 差.

### PDF_TYPO 清单 (依据 = PDF 自身)
- T-1 (p86 ce.xpt Row 2 CESEQ): PDF `1`. 同受试者 001 Row 1 CESEQ 已为 1; spec CESEQ/--SEQ 为受试者内唯一序号 (同表连续编号) → 正确值 2 由 PDF 自身确定, KB 保留 `2`.
- T-2 (p86 ce.xpt Row 1 CEENDTC, **T4 用户裁定项**): PDF `2013-09-01T2:30` 早于同行 CESTDTC `T11:00`, 明显有误; 但正确时刻 (12:30? 其他?) PDF 内无他处可证 (`grep -l "2013-09-01T" work/pdf_pages/ig34_p*.txt` 仅 p85/p86; sm.xpt Row 2 SMENDTC 为空) → 按口径照录 PDF `T2:30`, 待用户裁定. 原 KB `T12:30` 为 KB 自推值.
- T-3 (p85 叙述 "hyypoglycemic"): PDF 拼写错; KB 保留 `hypoglycemic` (未改).
- 信息项 (非改动): PDF 时刻 `T8:48` / `T2:30` 小时不补零 (ISO 8601 应为 T08:48); KB 照印, 未补零. 与 KB 原值 `T6:48` 同风格.

### 预期 fp 回归
- fp_match 改后 p84-86: EXACT 22 / PARTIAL 13 / EQUIVALENT 3, 与 baseline verdict 逐条 **0 变化** (verdict 取自静态 ledger). a004 的 `hit_target` 由 null → `knowledge_base/domains/SM/assumptions.md` (原仅 terminology/core/general_part4.md 命中).
- PARTIAL 13 中 a007-a018 为 p84 spec 表 / 脚注 (属 spec.md, 范围外 F-1).
- 全量 regress 输出 4 条 (ig34_p0363_a017-a019 / p0364_a001, §6.4.2) — 他批工作树改动, 非本批; `grep -E 'p008[4-6]|SM/'` = 0.

### 双向全扫 (含表格原子)
- PDF→KB: p84-86 SM 节叙述逐句规范化比对 (弯引号/星号归一) — 除 #9 (已修)、T-3 外 0 缺; Description/Overview + spec 首句已补 (#1/#2). Assumptions 1-3d 逐句在 assumptions.md. 3 张例表逐格见上.
- KB→PDF: examples.md / assumptions.md 全文件每行均有 PDF 对应; 无 KB 自写解释性内容 (D6 无), 无伪节号; `# SM — Examples` / `## Example 1` / `**sm.xpt**` / `**Row N:**` 为导航.
- 未改的细差 (范围外, 记录): p85 Row 4 "subject 002’s" PDF 为弯撇号, KB 直撇号 (Row 1 PDF 本身直撇号); assumptions.md 3a PDF 弯引号 “start date”, KB 直引号 — 均为字符归一差, 未动.

### 新增 atom 清单 (R3)
- #9 Row 4 说明 "this milestone" 原词恢复.

### 删除清单
| # | 原位置 | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:19/:30/:39/:40 旧值 | 同行 | VALUE_DIFF 旧值替换 (#4-7) | — |
| D-2 | examples.md:11 "disease" 一词 | 同行 | 词替换型改写恢复 PDF 原词 (#9) | — |

### 范围外发现
- F-1: spec.md (p84 spec 表 + 脚注, fp PARTIAL a007-a018) 不在白名单 → 归 O15 spec 扫描.
- F-2: `knowledge_base/domains/SM/spec.md` 顶部为 `> Class: Special-Purpose | Structure: …` 摘要行 (KB 自写); spec 首句已补入 assumptions.md, 未动 spec.md.
- 无其他域受影响: `grep -rn "T6:48\|T12:30\|HYPO2" knowledge_base/` 仅 SM/examples.md 与 ML/examples.md:42 (ML 的 HYPO2 为不同研究, 无关).

### 需主控定
- T-2 (CEENDTC `T2:30` 照录 vs 原 KB `T12:30`) 列入 T4 用户裁定.

### 触碰的 unparseable 表
- 无.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SM_writer; P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
pdftotext -f 84 -l 84 -layout "$P" - | awk '/SM – Description/{f=1;next}/SM – Specification/{f=0}f' | sed 's/^ *//;s/ *$//' | tr '\n' ' ' | sed 's/ *$//' > $S/desc_pdf.txt; sed -n 5p knowledge_base/domains/SM/assumptions.md | tr -d '\n' > $S/desc_kb.txt; cmp $S/desc_pdf.txt $S/desc_kb.txt   # IDENTICAL
pdftotext -f 84 -l 84 -layout "$P" - | grep '^ *sm.xpt' | sed 's/^ *//;s/ *$//' | tr -d '\n' > $S/spec_pdf.txt; sed -n 9p knowledge_base/domains/SM/assumptions.md | tr -d '\n' > $S/spec_kb.txt; cmp $S/spec_pdf.txt $S/spec_kb.txt   # IDENTICAL
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-SM.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 2 / DIFF 1 / diffs 1 (= T-1)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p008[4-6]|SM/' $S/fp_regress.jsonl   # 0
for p in 84 85 86; do pdftoppm -f $p -l $p -r 110 -png "$P" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### git diff --stat
```
 knowledge_base/domains/SM/assumptions.md | 10 ++++++++++
 knowledge_base/domains/SM/examples.md    | 10 +++++-----
 2 files changed, 15 insertions(+), 5 deletions(-)
```
