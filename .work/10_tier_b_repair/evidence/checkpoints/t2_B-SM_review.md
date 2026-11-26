# T2 B-SM reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus; base = HEAD 工作树未提交改动)

**verdict: PASS** (无阻断项; 2 个信息项交主控, 见末尾)

### 命令与关键输出 (可复跑; S = scratchpad/t2_B-SM_reviewer)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SM_reviewer; P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  -> KB tables: 3; status: {'OK': 2, 'DIFF': 1}; diffs: 1; exit 1  (唯一 diff = ce.xpt Row2 CESEQ kb 2 / pdf 1 = T-1)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  -> RESULT: RED, regressions=48 (全部 p118/p174/p215-263/p363-396, 他批/已提交批的基线漂移); grep -cE 'p008[4-6]|SM/' $S/fp_regress.jsonl = 0
python3 -I $S/scan.py $S        # 双向逐句扫 (pdftotext -f 84 -l 86 原始流, 截 "5.4 Subject Disease…" 至 "5.5 Subject Visits")
for p in 84 85 86; do pdftoppm -f $p -l $p -r 110 -png "$P" $S/p$p; done; 表区 160dpi 裁图 d85 / c85 / c86 / d86
git diff HEAD --quiet -- knowledge_base/domains/SM/spec.md && echo spec_unchanged   # spec_unchanged
md5 -q knowledge_base/domains/SM/*.md   # 0a144f48… / 7294b62b… / a1a8f357… = writer 报告一致
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42 (= 基线)
```
- 注: writer 报告 "全量 regress 4 条", 本次复跑为 48 条 (均非 SM 页), 系工作树/基线随别批变化; 对本批无影响 (LOW, 仅记录).

### 1. 完整性
| ref | writer action | 复核 |
|---|---|---|
| ig34_p0084_a004 (REAL_GAP) | INSERTED assumptions.md:5 | p84 原句与 KB:5 逐字一致 (连字符/逗号/括号); fp hit_target = SM/assumptions.md |
| census sm.xpt Row3 SMSTDTC | T6:48→T8:48 | 渲染图 "2013-09-24T8:48" 一致 |
| census mh.xpt Row1 MHDY | 空→1 | 渲染图 MHDY=1 一致 |
| census ce.xpt Row1 CEENDTC | T12:30→T2:30 | 渲染图 "2013-09-01T2:30" 一致 (T-2) |
| census ce.xpt Row2 CESTDTC | T6:48→T8:48 | 渲染图 "2013-09-24T8:48" 一致 |
| census ce.xpt Row2 CESEQ | SKIPPED_PDF_TYPO | 依据成立 (见 T-1) |
| R3 examples.md:11 | "this disease milestone" → "this milestone" | p85 Row 4: "the study day of this milestone was populated" 一致 |
| 授权: spec 首句 assumptions.md:9 | INSERTED | 与 p84 逐字一致 (含 em dash U+2014) |
| 结构: `## SM – Assumptions` :11 | INSERTED | PDF 原小标题 "SM – Assumptions" (en dash U+2013), 格式同 CM/BE 先例 |

### PDF_TYPO 依据核
| T | 位置 | 判定 | 依据 |
|---|---|---|---|
| T-1 | p86 ce.xpt Row2 CESEQ (PDF 1) | 成立, KB 保留 2 正确 | 同 USUBJID 001 Row1 已为 CESEQ 1; --SEQ 保证受试者内唯一 (p84 SMSEQ 注 "ensure uniqueness of subject records"), 同表连续编号 → 2 由 PDF 自身确定 |
| T-2 | p86 ce.xpt Row1 CEENDTC (PDF T2:30 < CESTDTC T11:00) | 成立, 照录 + T4 正确 | 独立 grep `work/pdf_pages/*.txt` "2013-09-01T\|HYPO1\|2013-09-24T": 仅 p85/p86 (+无关 ML p123 / sv20 p49); sm.xpt SMENDTC 空; p85 "only start date/times have been collected" 亦无终止时刻 → 正确值 (12:30/14:30/…) PDF 内无法确定; 原 KB T12:30 为 KB 自推 |
| T-3 | p85 "hyypoglycemic" | 成立 | PDF 自身拼写错; KB:22 保留 "hypoglycemic" (未改动) |

### 2. G-TB4 表格人工逐格 (渲染图 160dpi, 独立于 census)
| 表 | 行 | 结果 |
|---|---|---|
| sm.xpt (p85) | 表头 11 列 | 一致 |
| sm.xpt | Row 1-4 (44 格) | 一致 (Row3 SMSTDTC 2013-09-24T8:48; SMENDTC/SMENDY 全空; SMSTDY 空/25/50/-1046) |
| mh.xpt (p85) | 表头 15 列 | 一致 |
| mh.xpt | Row 1-2 (30 格) | 一致 (MHENDTC 空; MHDY 1/1) |
| ce.xpt (p86) | 表头 13 列 | 一致 |
| ce.xpt | Row 1 | 一致 (CEENDTC 2013-09-01T2:30) |
| ce.xpt | Row 2 | 除 CESEQ (KB 2 / PDF 1 = T-1) 外一致 (CESTDTC 2013-09-24T8:48, CEENDTC 2013-09-24T10:00) |

### 3. 双向全扫 (p84 "5.4" 起 – p86 "5.5" 止, 含表格原子)
- PDF→KB: 叙述句 0 缺 (scan 报的 MISS 均为标题/表格/页脚粘连或 spec 表; 逐条手核粘连句: Description 句 KB assumptions:5, "In this study, the disease milestones…" examples:5, "Information in SM is taken…" examples:22, CE 引言 examples:33 均在). 唯一字面差 = T-3.
  Assumptions 1-3d (ig34_p0084_a020 – p0085_a006) fp EXACT 命中 assumptions.md. spec 表 + 脚注 (a007-a018) 属 spec.md, 范围外 (writer F-1).
- KB→PDF: assumptions.md / examples.md 全文件每行 (含表格每格) 在 p84-86 有出处; 仅 `# SM — Assumptions` / `# SM — Examples` (既有 H1 导航) 与 T-3 不字面匹配. 无 KB 自写解释、无伪节号, D6 无适用.
- 注: 原子 ledger 无 p86 的 SM 原子 (CE 引言句 + ce.xpt 未被原子化), 本次由人工扫 + census 覆盖.

### 4/5. 位置与副作用
- Description → Specification → Assumptions 顺序 = PDF p84 顺序; 例子内容未移位.
- 整个 KB diff: SM 只动 assumptions.md + examples.md; spec.md 未动; BS/NV/RE 为别批, 与本批无关. 无清单外删除/改写; 既有标题/锚点未变.
- 授权范围: assumptions.md 仅新增 3 个 `##` 标题 + Description 句 + spec 首句; Assumptions 列表 1-3d 未动.

### 6. R2 recheck
- `t2_recheck[]` 为空; 无判定.

### G-TB6 新增/改动行反向溯源签字
| diff 行 | 类型 | 出处 |
|---|---|---|
| assumptions.md:3 `## SM – Description/Overview` | 结构行 (新增节标题) | p84 小标题, 签字 |
| assumptions.md:5 | 内容 | p84 "A special-purpose domain that is designed to record the timing…" |
| assumptions.md:7 `## SM – Specification` | 结构行 | p84 小标题, 签字 |
| assumptions.md:9 | 内容 | p84 "sm.xpt, Subject Disease Milestones — Special Purpose. One record per Disease Milestone per subject, Tabulation." |
| assumptions.md:11 `## SM – Assumptions` | 结构行 | p84 小标题, 签字 |
| assumptions.md 空行 ×5 | 结构 | 签字 |
| examples.md:11 / :19 / :30 / :39 / :40 | 内容 | p85 Row 4 说明 / p85 sm.xpt / p85 mh.xpt / p86 ce.xpt (见上表) |
- 新增/改动行 10 (内容 7 + 结构标题 3), 无出处 0.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| fp regress 计数 | 记录准确性 | writer 报 4 条, 复跑 48 条; 均非 SM, 不影响本批 | `grep -cE 'p008[4-6]\|SM/'` = 0 |
| examples.md:7 "SMDY" | 信息 (非阻断) | PDF 原文 "SMDY is not populated", 而 SM 无 SMDY 变量 (spec 为 SMSTDY); KB 照录 PDF, 未登记 | p85 Row 1: "Because this is a partial date, SMDY is not populated." |

### 需主控定 (信息项, 不阻断 PASS)
- T-2 (CEENDTC T2:30 照录) 进 T4 用户裁定 —— 同意 writer.
- "SMDY" (p85 Row 1 叙述, 疑为 SMSTDY 印刷错): 是否按 PDF_TYPO 口径登记 T-4 (正确值可由 spec / Rows 2-3 "SMSTDY has been populated" 确定). 当前 KB 照录, 不改亦不违规.
