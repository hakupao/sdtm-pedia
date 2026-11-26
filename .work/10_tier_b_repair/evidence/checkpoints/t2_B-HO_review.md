# T2 B-HO reviewer checkpoint

## attempt 1 (oh-my-claudecode:code-reviewer / opus; 独立于 writer)

**verdict: PASS**

- 范围: §6.2.5 HO = p167 下半 → p171 上半 (止于 "6.2.6 Medical History (MH)"); writer O20 判定核实一致. batch pdf_ranges lo/hi 167-171 完整覆盖.
- 本批 KB diff (`git diff HEAD -- knowledge_base/domains/HO/`): assumptions.md +10, examples.md 4 行改. 整个 KB diff 其余文件 (CE/CM/FT/MI/QS) 属他批, 不计. HO/spec.md 未动.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-HO_reviewer/`

### 复跑命令与结果
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-HO_reviewer
pdftotext -f 167 -l 171 -layout "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p167_171.txt   # 独立方法 (layout 列位) 逐格核
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  # exit 1; KB tables 4: OK 3 / DIFF 1; diffs 1 = examples.md:25 HOTERM (T-1, 预期); pdf_only 中 p167-171 = 0; pdf_unparsed 本批 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # RESULT: RED (全局, 他批页码); grep -cE 'p016[7-9]|p017[01]|HO/' $S/fp_regress.jsonl = 0
for p in 170 171; do pdftoppm -f $p -l $p -r 110 -png "<PDF>" $S/p$p; done   # 渲染图逐格核
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42 (= 基线)
```

### 1. 完整性 (atoms 2 / t2_recheck 0)
| atom | writer action | 复核 |
|---|---|---|
| ig34_p0169_a0024 (examples.md:25 HOTERM) | SKIPPED_PDF_TYPO T-1 | 成立. p170 渲染图 Row 5 印 "REHABILIATION FACILITY"; 正确值由 PDF 自身定: 同节 Ex2 Row 3 "REHABILITATION FACILITY"、Ex1 叙述 "transferred to a rehabilitation facility"、Assumption 1 "rehabilitation facility stays". 按 dispatch "PDF 自身拼写错 KB 保留正确拼写", KB 不改正确. |
| ig34_p0171_a0002 (examples.md:72 HOSTDTC) | REPLACED T17:00→T10:00 | 正确. p171 渲染图 Row 10 HOSTDTC "2011-06-25T10:00". census 该表 OK. |

### 2. G-TB4 表格逐格人工核 (渲染图 p170/p171 + layout 文本, 独立于 census bbox)
| 表 | KB 行 | 结果 |
|---|---|---|
| Ex1 ho.xpt (10 列, Rows 1-12) | :19-32 | 表头/列序一致; Row 2 HOSTDTC/HOENDTC 空, HODUR P6D 一致; 除 Row 5 HOTERM (T-1) 外逐格一致 |
| Ex1 suppho.xpt (11 列, Rows 1-6) | :46-53 | 逐格一致 (QEVAL 全空) |
| Ex2 ho.xpt (11 列, Rows 1-11, 跨 p170-171) | :61-73 | 逐格一致; Row 10 HOSTDTC T10:00 (改后); Row 11 HOENDTC 空, HOENRTPT ONGOING, HOENTPT END OF STUDY 一致 |
| Ex2 suppho.xpt (Row 1) | :79-81 | 逐格一致 (IDVARVAL 7, QVAL STROKE) |

### 3. G-TB6 反向溯源 (diff 每条新增/改动行)
| diff 行 | 出处 | 结论 |
|---|---|---|
| assumptions.md:3 `## HO – Description/Overview` | p167 小标题原文 | 结构行, 签字 |
| assumptions.md:5 Description 句 | p167 "An events domain that contains data for inpatient and outpatient healthcare events…" 折行合并后逐字 | 一致 |
| assumptions.md:7 `## HO – Specification` | p167 小标题原文 | 结构行, 签字 |
| assumptions.md:9 spec 首句 | p167 "ho.xpt, Healthcare Encounters — Events. One record per healthcare encounter per subject, Tabulation." | 逐字一致 |
| assumptions.md:11 `## HO – Assumptions` | p169 小标题原文 | 结构行, 签字 |
| examples.md:40 Row 5 叙述 | p170 "For the first encounter for subject ABC123105, the indication/medical condition for the hospitalization was recorded." | 逐字一致 (删 KB 多出 "recorded" 正确) |
| examples.md:42 Row 6 叙述 | p170 "For the second encounter for subject ABC123105, the name of the hospital was recorded." | 逐字一致 |
| examples.md:72 Row 10 | p171 渲染图 | 一致 |
| examples.md:75 弯撇号 | p171 "subject ABC123101’s repeat hospitalization" (渲染图/pdftotext 均为 U+2019) | 一致; 全库引号风格 O40 待 T4, 本处随 PDF 可接受, 记录 |
无自造说明 / 扩写 / "Note:"; 无出处行 0.

### 4-5. 位置 / 无副作用
- 新增 3 段位于 H1 与原 Assumptions 列表之间, 顺序 Description → Specification → Assumptions 与 PDF 及 CM 先例结构一致. 原列表 1-5 字节未动 (diff 仅 + 行). 授权范围内 (Description/Overview、spec 首句、PDF 原有小标题).
- examples.md 行数 81 不变, 无标题/锚点改动, 无其他行改动.

### 双向全扫 (含表格原子; 本人独立执行, 非采信 writer)
- PDF→KB: p167 Description + spec 首句 → assumptions.md:5/:9; p169 Assumptions 1-5 (含 3a/3b) → :13-23 逐句一致 (5 中 `‑‑` U+2011 → `--` 字符规范化, 可接受); p169-171 Ex1 引言 + Rows 1-2/3-5/6-7/8/9-12 叙述、Row 1/2/3-4/5/6 叙述、Ex2 引言、Ex2 suppho 前句 → examples.md 逐句一致; 4 表全部原子见 §2. spec 表 (p167-169) 属 spec.md, 不在本批白名单 (writer F-1 → O15), 不计.
- KB→PDF: HO/assumptions.md 23 行、HO/examples.md 81 行逐行有 PDF 出处; 无 KB 自写解释内容 (D6 无), 无伪节号. 文件 H1 `# HO — Assumptions` / `# HO — Examples` 为 KB 既有导航标题, 未改.
- Ex1 Rows 3-4 叙述写 ABC123103 (对应 suppho Rows 3-4) 与 PDF 一致, 非差异.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无阻断问题 | — |
| examples.md:75 | 记录项 (LOW) | 弯撇号 U+2019 与全库直引号风格可能不一致, 归 O40/T4 统一裁定 | p171 "ABC123101’s" |
| examples.md:25 | 记录项 | T-1 census 预期残留 DIFF 1 | p170 "REHABILIATION FACILITY" |

### R2 recheck
- t2_recheck 为空, 无.
