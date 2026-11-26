# T2 B-RS auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus; 先独立判, 判完才对照 writer/reviewer 报告)

- 命令: `t2_auditor_v1.0.md` 抽样脚本, 两处按主控口径调整: `files` = batch kb_files ∪ {`knowledge_base/domains/RS/assumptions.md`} (主控授权 M-1/M-2/M-3, 本批实际改动); `pdf_pages` → RS 全节 range(329, 340). 其余逐字不变. 输出 scratch `t2_B-RS_auditor/sample.json`.
- seed = 20261126; C = 0 (batch json atoms/t2_recheck 均空; 改动全由全扫/主控授权产生); P = 89; N = min(30, max(10, 0), 89) = 10 → 全部从 P−C 抽.
- 因实际改动集大, 另加: (i) p332:14–p339:4 全段 PDF↔KB assumptions.md:18-128 词级 difflib (覆盖 p337-339 新增全文); (ii) 从 p337-339 新增全文另抽 6 句逐句核; (iii) D-1..D-6 抽 4 条核; (iv) P 全 89 原子机械匹配.

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0337_a008 | p337:9 QRS 1b: 参照下列 CT codelist 取 QRS --CAT 术语 | RS/assumptions.md:90 | 否 | 是 | 是 (QRS 共用 1.b) | 逐字; i-iii 三个 codelist 名 :91-93 齐 |
| 2 | ig34_p0337_a004 | p336:36 CC 3d (原子页码误标 337): RSSTRESC/RSSTRESN 填仪器规定序数分 | RS/assumptions.md:82 | 否 | 是 | 是 (CC 3.d) | 逐字 |
| 3 | ig34_p0329_a010 | p329:15 Description bullet 3: 其他疾病分类/评分系统 (如 staging) 基于已发表标准 | RS/assumptions.md:11 | 否 | 是 | 是 (## RS – Description/Overview) | 逐字 (新增) |
| 4 | ig34_p0338_a011 | p338:23 QRS 7a: 仪器 annotated CRF 也可作全文参考 | RS/assumptions.md:119 | 否 | 是 | 是 (QRS 7.a) | 逐字, 弯撇号同 PDF |
| 5 | ig34_p0339_a003 | p339:6-7 CC Examples 引言 + qrs URL | RS/examples.md:72 | 否 | 是 | 是 (## RS — Examples - Clinical Classifications) | 逐字含 URL |
| 6 | ig34_p0332_a009 | p332:21-24 DR 2: 肿瘤负荷变化; RECIST[1]/Lugano[2]; 每标准 1 个 supplement | RS/assumptions.md:28 | 否 | 是 | 是 (DR 2) | 唯一差 "will contained"→"will contain" = T-2 (PDF 语法笔误, 合规) |
| 7 | ig34_p0334_a011 | p334:18-19 Ex1 Rows 4-7 叙述 (week 12, pleural effusion) | RS/examples.md:12 | 否 | 是 | 是 (Example 1) | "symptomatic determination"→"deterioration" = T-8; 依据 p334:16 同例引言 + Row 6 RSTEST, PDF 自身可定 |
| 8 | ig34_p0335_a014 | p335:25 Ex3 引言: best response + 对既往/后续治疗的 progression | RS/examples.md:48 | 否 | 是 | 是 (Example 3) | 逐字 |
| 9 | ig34_p0338_a013 | p338:28-31 QRS 9: SDS QRS Subteam 统筹 supplement 开发 | RS/assumptions.md:123 | 否 | 是 | 是 (QRS 9) | 与 PDF 页文本逐字 (原子 verbatim 抽取有误: "for FT"/"value"/"instruments", 以 PDF 页为准) |
| 10 | ig34_p0333_a016 | p333:35-p334:2 DR 8: RSACPTFL 由独立评估者标识 accepted 记录 (跨页) | RS/assumptions.md:58 | 否 | 是 | 是 (DR 8) | 跨页合并完整, 例举 3 个 assessor 值齐 |

**本批计分样本 10: 独有丢失 0 / 忠实度错误 0 → 抽检 PASS.**

### 额外 A: p337-339 新增 QRS 全文另抽 6 句
| 句 | PDF 页:行 | KB assumptions.md | 结果 |
|----|-----------|-------------------|------|
| QRS 1 (--CAT 命名, ADAS-COG/BPI SHORT FORM/APACHE II/4 STAIR ASCEND) | p337:3-6 | :88 | 逐字 |
| QRS 3 (numeric standardized responses 条件) | p337:17-20 | :99 | 逐字 (弯引号同 PDF) |
| QRS 4a-iii (eData 中的 subtotal/total 视为 captured, CT 可扩展) | p337:28-30 | :105 | 逐字 |
| QRS 7 (--TEST >40 / --QSORRES >200, Section 4 / 4.5.3 交叉引用) | p338:19-22 | :118 | 逐字, 两处 Section 交叉引用齐 |
| QRS 8 (--EVAL/--EVALID 禁用 + qrs URL) | p338:24-27 | :121 | 逐字 |
| QRS 9a-i (supplement 发布于 CDISC 网站 + URL) | p338:34 | :125 | 逐字 |

### 额外 B: 全段词级 diff (p332:14–p339:4 vs assumptions.md:18-128, 去页脚/列表号/5c 表行)
- 命令: scratch `t2_B-RS_auditor/worddiff.txt` (python difflib, PDF 2704 词 / KB 2702 词). 非 equal 共 11 处, 全部可归类:
  - PDF_TYPO 已登记: "will contained" (T-2), "a a source" (T-3), "derived ." / "domains ." (T-4), "an resolution" (T-5), "--STRNC" (T-6, 依据同节 DR 11 与 spec 为 --STNRC). 各条依据均可由 PDF 自身确定 ✓.
  - pdftotext 断行假差: "-- SPCCND" ×2.
  - 导航: KB 用例小标题 "RS —" (em dash) vs PDF "RS –" (en dash), HEAD 已有、本批未动; KB 插入 `## QRS Shared Assumptions` 导航标题 (PDF p337 无标题; 与 FT/QS 同名标题一致, 纯导航, 按口径不加 D6).
  - 0 处信息丢失 / 改义.
- p329:8-19 Description/Overview + spec 首句 vs assumptions.md:3-16 词级 diff 0 差; spec 首句 em dash U+2014 同 PDF.
- DR 5c SYMPTDTR 示例表 (assumptions.md:46-48) 5 格对 p333:21-23 一致.

### 额外 C: 删除清单抽核 (D-1, D-3, D-4, D-5, D-6)
- D-1 (examples Ex3 表旧值): 对 p336 渲染图 (`pdftoppm -f 336 -l 336 -r 110`, 源 `SDTMIG v3.4 (no header footer).pdf`) 核: Row1 RSDTC 2010-02-18; Row4 VISIT FOLLOW-UP MONTH 4 / RSDTC 2010-04-02; Row5 FOLLOW-UP MONTH 6 / 2010-06-01 → KB 新值正确, 旧值 (2015-*, MONTH 6/8) 为 KB 错误, 删除合理. Row3 RSSTRESC PDF "MINIMAL REPSONSE" = T-1 (同行 RSORRES 可定) ✓.
- D-3 (DR 引言): KB 旧句 "The following assumptions are unique to the RS domain disease response use case:" 为 p336:23 CC 引言仿写; PDF p332:18 实为 "Assumptions here discuss the oncology use case …" → 替换正确, 无独有信息损失.
- D-4 (QRS 自写指针 "see FT assumptions"): PDF p337-339 在 RS §6.3.9.3.2 内确有全文 (无标题), 主控 M-3 授权换全文; 全文已逐词核 (额外 B) → 删除指针正确.
- D-5 (列表旧值): ONCRSRR→ONCRSR ×3 (p332:25/28/34 ✓); DR 5a "that domain"→"the domain" (p333:13 ✓); CC 3b 弯撇号 (p336:33 ✓). CC 3a 保留 "that domain" (p336:31 PDF 即 "that") ✓.
- D-6 (T-7/T-8): RSPLNKGRP→RSLNKGRP ×4, 依据 p336 表头 RSLNKGRP 列值 CM1/CM2/PR2/CM3 与叙述一致 + p329 spec; PDF 自身可定 ✓.

### 旁证: P 全 89 原子机械匹配 (空白/引号归一, 列表号去除)
- 70 精确命中; 19 未命中全部人工判定: T-2/T-7(×4)/T-8 PDF_TYPO 5+1; 空格 1 (T-4); 原子 verbatim 抽取错 9 (p337_a002/a003 实为 p336 CC 3b/3c 且含 "RSORRESRU"/">-3"; p337_a006 "ADAS-Cog"/"al STAIR"; p337_a015, p338_a002/a003/a006/a010/a013, p339_a001 与 PDF 页文本不符 — 均以 PDF 页为准, KB 与页文本一致); 范围外 2 (见下).

### 范围外发现 (不计本批)
- ig34_p0332_a003 spec 表脚注 (asterisk = CT, codelist 括号) 不在 RS/spec.md (spec.md 不在本批文件, 与他域同类, 由 O15/O16 兜底).
- ig34_p0339_a023 属 SC Description, 已在 SC/assumptions.md:5.
- pdf_atoms p337-339 多条 verbatim 失真 (见上), 建议登记 ATOM_ERR.

### 授权范围核
- `git diff HEAD -- knowledge_base/domains/RS/`: assumptions.md 改动 = Description/Overview + Specification 首句 (通用授权) + M-1 (共用引言/两个 § 小标题/DR 引言) + M-2 (列表值/5c 表) + M-3 (QRS 全文) — 全在主控授权内; examples.md = Ex3 5 格 + References 同文件 RELOCATE + T-7/T-8 词. spec.md 未动 (md5 `7ec990f0654540174bcbd2f8384f206a`).

### G-TB8
- trace.jsonl T2.B-RS: writer `oh-my-claudecode:executor` a1/a2/a3 + reviewer `oh-my-claudecode:code-reviewer` a1 CONDITIONAL / a2 PASS (04:45:33Z, 在 writer a3 04:44:35Z 之后, delta 复审); `agent: main` 记录 0 ✓.
- 终态经 reviewer: 现 md5 assumptions `4976b5443c133bec34b530209fe57362` / examples `6e121b076e5c37e7728492e5dc027ddf` = reviewer a2 记录值; KB mtime 04:39:16Z / 04:44:21Z 均早于 reviewer checkpoint 04:45:33Z ✓.

### live docs
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (写本文件前; 基线 42).

### 对照 writer/reviewer (判后)
- 与 writer 变更 #1-22、T-1..T-8、D-1..D-6 及 reviewer a2 PASS 一致; 无分歧. 本 auditor 独立 difflib 结果与 writer "QRS 全文仅差 T-5/T-6" 吻合.

### 结论
**PASS** — Rule A N=10 seed=20261126 (C=0, P=89): 丢失 0, 忠实 0; 额外 p337-339 6 句 + 全段词级 diff 0 丢失; D-1/D-3/D-4/D-5/D-6 处理正确; 范围外发现 2 (spec 脚注 / SC, 不计) + ATOM_ERR 观察.
