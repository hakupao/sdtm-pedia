# T2 B-SC reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus; 审 writer attempt 1+2 终态)

**verdict: CONDITIONAL** — KB 内容零缺陷 (无需改 KB); 修正项仅限证据/登记: T-1 Row 3 依据算术错误 + 未登记的 PDF 内部 SCDTC/SCDY 1 天不一致 (T4).

- 范围: SC/examples.md (batch) + SC/assumptions.md (主控授权 spec 首句; attempt 2 主控授权 D2 M-1). 节页范围 p339 下部 (6.3.10 标题起) → p342 上部 (6.3.11 SS 前), 与 writer 一致; p339 上部 RS 不计.
- md5 终态: assumptions.md `b2771af79138622abac5d919865604c1`, examples.md `cc07ab726ff3a5ed7734183b8b749324`, spec.md `1cf3915fdf6a124cf939b6c767f2fe8a` (未动). 与 writer 报告一致.
- `git diff HEAD --stat -- knowledge_base/domains/SC` = 2 files, +6/-4; 本批无白名单外 KB 改动 (工作树其他 M 文件属别批).

### 命令 (scratch `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SC_reviewer/`)
```
table_census.py --manifest $S/manifest.json   → KB tables 3; status OK 2, NO_PDF 1; cells 146; diffs 0 (exit 1 仅因 NO_PDF + 全局 PDF_ONLY)
fp_match.py ... --regress-out $S/fp_regress.jsonl → RESULT: RED (regressions=60, 全为他批页 p118-p263 等); grep -cE 'p03(39|4[0-2])|SC/' fp_regress.jsonl = 0; SC/ 原子 0
python3 tools/check_links.py 2>&1 | grep "live docs" → live docs: 42
pdftoppm -f 342 -l 342 -r 110 (全页) + -r 220 左/右裁切 → 人工逐格
python3 -c "date(2017,3,2)+timedelta(30), +timedelta(101), (date(2017,6,10)-date(2017,4,1)).days" → 2017-04-01, 2017-06-11, 70
```

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| writer T-1 Row 3 (examples.md:36 SCDTC) | PDF_TYPO 依据 | writer 称 "SCDY 297 = +71 天 → 2017-06-10" 算术错: 2017-04-01 + 71 = 2017-06-11; 2017-06-10 只对应 +70 (SCDY 296). KB 值 2017-06-10 本身可接受 (保留 PDF 数字 "06-10", 仅去掉年份中多余连字符, 依据 = spec SCDTC ISO 8601 + Row 1 同格式 "2017-03-02"), 但登记依据须改正 | p342 渲染 "20-17-06-10" / SCDY "297"; Row 1 "2017-03-02"/196 |
| 新 T4 (Row 3 SCDTC↔SCDY) | PDF 内部一致性 | 以 Row 1/2 (2017-03-02→196, 2017-04-01→226, 一致) 推 RFSTDTC = 2016-08-19 → Row 3 2017-06-10 应为 SCDY 296, PDF 写 297; 由 PDF 自身无法判定日期错还是 SCDY 错 → KB 照录 (2017-06-10 / 297, 现状即如此), 登记为 T4 用户裁定项 | p342 Ex2 Row 3 |

### CONDITIONAL 修正清单 (仅证据, 不改 KB)
1. `t2_B-SC.md` PDF_TYPO 清单 T-1: Row 3 依据改为 "去连字符依据 ISO 8601 + Row 1 格式, 数字照录 PDF"; 删 "+71 天 → 2017-06-10" 推算. Row 2 依据 (SCDY 226 = +30 → 2017-04-01) 正确保留.
2. 新增 T-2 (T4 用户裁定): p342 Ex2 Row 3 SCDTC 2017-06-10 与 SCDY 297 差 1 天 (按 Row 1/2 锚定应为 296 或 2017-06-11); KB 照录 PDF 双值. 主控登记到 pending_user.
- 上两项可由主控直接在证据中改正/登记, 无需 writer 重跑 KB; 改正后本批即可视为 PASS 派 auditor.

### 人工逐格表 — p342 Ex2 sc.xpt (渲染 110dpi + 220dpi 裁切; KB examples.md:32-36)
| 格 | PDF 渲染 | KB | 判定 |
|---|---|---|---|
| 表头 17 列 | Row STUDYID DOMAIN USUBJID SCSEQ SCTESTCD SCTEST SCCAT SCORRES SCORRESU SCSTRESC SCSTRESN SCSTRESU SCMETHOD VISITNUM SCDTC SCDY | 同序同名 (SCORRESU 已改) | 一致 |
| 分隔行 | — | 18 个 `|`, 17 列 | 结构一致 |
| Row 1 | 1, ABC-123, SC, 101, 1, EGESTAGE, Estimated Gestational Age, PREGNANCY-RELATED FINDINGS, 100, DAYS, 100, 100, DAYS, MENSTRUAL HISTORY, 10, 2017-03-02 (折行), 196 | 同 | 17/17 一致 |
| Row 2 | 2, ABC-123, SC, 101, 2, EGESTAGE, Estimated Gestational Age, PREGNANCY-RELATED FINDINGS, 135, DAYS, 135, 135, DAYS, ULTRASOUND, 11, "20-17-04-01", 226 | SCDTC 2017-04-01, 其余同 | 16/17 一致 + SCDTC = T-1 (依据成立) |
| Row 3 | 3, ABC-123, SC, 101, 3, EGESTAGE, Estimated Gestational Age, PREGNANCY-RELATED FINDINGS, 265, DAYS, 265, 265, DAYS, BALLARD, 13.1, "20-17-06-10", 297 | SCDTC 2017-06-10, 其余同 | 16/17 一致 + SCDTC = T-1 (去连字符成立; 依据需改) + T4 见上 |
- 51 格 (17×3) + 17 表头: 差异仅 2 格 SCDTC (登记 PDF_TYPO).
- Ex1 (examples.md:11-20, p341, 8 行×10 列) / Ex3 (:44-51, p342, 6 行×11 列): census OK; 另以 pdftotext -layout 文本与渲染图 (p342 Ex3) 独立逐行核, 一致.

### 双向全扫 (含表格原子)
- PDF→KB: p339 6.3.10 起 / p340 spec 首句 / p341 Assumptions 1-3 + Examples 叙述 / p342 Ex2 两段 + Ex3 引言; 归一化逐句比对 (空白、Markdown 符号、折行连字符 `--\nXFN`), 仅标题拼接块未命中 (标题均以 KB 结构行存在), 叙述 0 缺. URL `https://www.cdisc.org/standards/terminology/controlled-terminology` 在 assumptions.md:15. 3 张表全覆盖.
- KB→PDF: assumptions.md 17 行 / examples.md 51 行逐行有 PDF 对应, 除下列结构/导航行; 无 KB 自写解释性内容 (D6 无), 无伪节号.
- spec 首句 PDF 原文即 "per subject., Tabulation." (多一句点为 PDF 原貌), KB 逐字, 不算 typo.

### G-TB6 结构行签字
| 行 | 内容 | 判定 |
|---|---|---|
| assumptions.md:7 | `## SC – Specification` | PDF p340 小标题 "SC – Specification"; 位置 (Description 与 Assumptions 间) 同 CM/RS 先例; 签字 |
| assumptions.md:9 | sc.xpt spec 首句 | p340 逐字; 签字 |
| examples.md:3 | 交叉引用 (链 `assumptions.md#sc--specification`) | 主控授权 D2 去重 (M-1); 纯导航不加 KB note; slug: "SC – Specification" → 小写、去 en dash、空格→连字符 = `sc--specification`, 与 assumptions.md:7 对应, 有效; 仓内无旧锚点 `sc--specification-p340` 引用 (grep knowledge_base/docs/web/src = 仅新链 1 条); 签字 |
| examples.md:32 | 表头 SCORESU→SCORRESU | p342 渲染 + spec 变量名; 签字 |
| examples.md:33 | 分隔行 (未改) | 签字 |
- 删除: examples.md 旧 :3-5 (KB 自加 `## SC – Specification (p340)` + 首句) → 保留副本 assumptions.md:9; 无信息丢失.

### R2 recheck / atoms
- atoms 0, t2_recheck 0 → 无 R2 判定项.

### 其他
- 范围外 (LOW, 全局非本批): 63 份 spec.md 均无 spec 表脚注 "1In this column, an asterisk (*)…" (p341); 属全局约定, 不计本批.
