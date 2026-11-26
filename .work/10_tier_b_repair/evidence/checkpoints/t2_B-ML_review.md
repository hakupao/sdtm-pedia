# T2 B-ML reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS**

- 基线 `HEAD` (437c2ad); 本批 diff = `git diff HEAD -- knowledge_base/domains/ML/` → assumptions.md +10 / examples.md 1 行改; spec.md 未改 (`git diff --quiet` 0)。工作树其他 KB 改动 (CE/CM/CO/DV/HO/IE/MI) 属他批, 不计。
- md5 与 writer 报告一致: assumptions `71ef7496…`, examples `9388a1f5…`, spec `6e3be1a4…`。
- 节页范围: §6.1.4 = p121-124 (p125 起 6.1.5 PR), 与 writer 一致, 全扫按此范围。
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-ML_reviewer/`

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-ML_reviewer; mkdir -p $S
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-ML.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
#  exit 1; KB tables 5: OK 1 (:39) / DIFF 1 (:63, 1 CELL :66 MLTRT KB WHITE MILK vs PDF WHTE MILK = T-1) / UNPARSEABLE 3 (:14 :25 :52); 本批 pdf_only 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
#  RESULT: RED (全局 60 条, 页 p0118/p0153-155/p0174/p0179/p0215/p0218/p0254-263/p0289/p0311/p0363-374/p0396 = 他批); grep -cE 'p012[1-4]|ML/' fp_regress.jsonl = 0
#  p121-124 verdict: EXACT 44 / PARTIAL 39 / EQUIVALENT 6 / MISPLACED 3 / INTENTIONAL_EXCLUDE 1
cmp <(sed -n 5p knowledge_base/domains/ML/assumptions.md) <(grep -h "An interventions domain" .work/10_tier_b_repair/work/pdf_pages/ig34_p0121.txt | sed 's/^ *//;s/ *$//')   # 0 差 (DESC_IDENTICAL)
cmp <(sed -n 9p knowledge_base/domains/ML/assumptions.md) <(grep -h "ml.xpt, Meal" .work/10_tier_b_repair/work/pdf_pages/ig34_p0121.txt | sed 's/^ *//;s/ *$//')        # 0 差 (SPEC1_IDENTICAL)
for p in 121 122 123 124; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done   # 渲染图人工核
grep -rn MLGRID knowledge_base | wc -l   # 0
python3 tools/check_links.py 2>&1 | grep "live docs"   # broken relative links: 18668 (live docs: 42)
```
- p121-124 无 hit_target 的原子逐条查: spec 表行 a007-a029/p122 a001-a014 (spec.md 非 fp 目标文件, 人工全核见下); p122_a015 脚注 = F-1 (O15); p122_a017 原子文本多了 "would **not** be represented", PDF p122 为 "would be represented" → 原子错, KB assumptions.md:13 正确; p123_a005 = T-2; p123_a009-a011/a016-a018 CRF 行 (原子用 `X Snack |` 合并写法, KB 拆列, 渲染核一致); p123_a012 原子 "row." vs PDF/KB "row:" → 原子错; p124_a017 = T-1。p124_a001 原子 MIDSDTC 截为 "2015-09-03", PDF/KB 为 2015-09-03T17:00 → 原子错。均无 KB 缺失。

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | 全部 | 无阻断问题 | — |
| F-2 补充 (非本批) | spec 表 CT 列 | DOMAIN 行 PDF CT 列为 "ML", KB spec.md:18 空; 与 CM/AE spec 同为全库约定, 并入 F-2 | p121 DOMAIN 行 |

### G-TB4 人工逐格 (渲染图)
| 表 | 结果 |
|---|---|
| examples.md:52 Ex2 Group/Arms/Details (**本批触碰**) | Row 1: `1` / `Control` / "Students received standard meals in a standard cafeteria environment." 一致。Row 2: `2` / `Experimental: choice architecture` / 引导句 "…to “nudge” students towards healthier choices. Physical modifications included:" + 4 bullet: "Placing vegetables at the beginning of the lunch line" / "Placing fruits in attractive bowls, trays lined with appealing fabric, and fruit options next to cash registers" / "Promoting fruits and vegetables with prominently displayed signage and images" / "Placing white milk selection more predominantly than chocolate milk (e.g., white milk displayed in front of chocolate milk)" — 首字母大写、无分号、末项无句点, 均一致 (`norm(KB cell)==norm(PDF)` True, `<br>•` 计数 4)。仅弯引号→直引号 (F-3/O40) |
| examples.md:14 Meal Log CRF (未触碰) | 表头 Type(跨 3 列)/Volume/Start Date/Start Time/Event ID; 3 行勾选位置 X Snack / X Nutritional drink + 8 oz / X Meal, 日期 2015 Jun 03·Sep 03·Dec 31, 时间 14:15·8:30·19:00, CE001-003; ADD ROW 行 — 一致 |
| examples.md:25 DILI Meal CRF (未触碰) | Wild mushrooms X Yes 2015 DEC 24 / Ackee fruit X No / Cycad seeds X No — 一致 (PDF "2015  DEC" 双空格为排版) |
| examples.md:39 Ex1 ml.xpt (census OK) | p123-124 渲染 6 行 × 18 列抽看一致 (Row 4 MLDTC 2015-12-27 / MLSTDTC 2015-12-24 / -P1W; Rows 1-3 RELMIDS LAST MEAL PRIOR TO, MIDSDTC) |
| examples.md:63 Ex2 ml.xpt | 9 行一致, 仅 Row 2 MLTRT = T-1 |

### spec.md (未改) 全核
p121-122 text 层 + p121 渲染逐变量对 spec.md 37 变量: Label / Type / Role / Core / CDISC Notes 0 差; CT 码 NY→C66742, ND→C66789, UNIT→C71620, FRM→C66726, EPOCH→C99079 对应正确; ISO 8601 格式列一致。`*` 与 DOMAIN "ML" 不保留 = F-2 全库约定。O4: p121 渲染为 `MLGRPID`, spec.md:41 `MLGRPID` 正确, 笔误只在原子 ig34_p0121_a011 → **O4 (ML) 判原子错成立, 可关闭**。

### R2 recheck
| atom | 判定 | 证据 |
|---|---|---|
| ig34_p0121_a005 "ml.xpt, Meal Data — Interventions. One record per … per subject, Tabulation." | 原 kb_loc spec.md:3 (`> Class: Interventions \| Structure: …`) 按 R2 = **REAL_GAP** (丢 "ml.xpt"、数据集标签 "Meal Data"、"Tabulation"); writer 已在 assumptions.md:9 逐字补入 (cmp 0 差, fp hit_target = assumptions.md) → **已闭合, 无需 CONDITIONAL**。spec.md:3 为 63 域 spec 统一结构行 (CM 先例保留), 不按 D2 删 | p121 spec 首句; assumptions.md:9 |

### PDF_TYPO
- T-1 (p124 Ex2 Row 2 `WHTE MILK`): 同表 Row 8 `WHITE MILK` + Group 2 Details "white milk" → PDF 自身可定, KB `WHITE MILK` 正确。
- T-2 (p123 "occurrence of of prespecified"): 重复词为 PDF 自身明显排印错 (语法唯一可定), KB examples.md:8 单 "of" 正确, 未改动。

### 双向全扫 (含表格原子)
- PDF→KB: p121 节标题 (KB 用文件标题约定) / Description/Overview 标题+句 → assumptions.md:3,5 / Specification 标题+首句 → :7,9 / spec 表 37 行 → spec.md / p122 脚注 → 缺 (F-1, O15) / ML – Assumptions 标题 → :11 / Assumption 1 (a-d + 段) / 2 (a, b) / 3 → :13-25 逐句一致 / p123 ML – Examples, Example 1 引言 + 2 bullet + 2 CRF (标题/提示句/表) + Note + Rows 1-3/4-6 + ml.xpt → examples.md:1-46 / p124 Example 2 引言 + Group 表 + Food-card 2 句 + 引导句 + ml.xpt → :48-73。无遗漏 (除 F-1)。
- KB→PDF: assumptions.md 全 25 行、examples.md 全 73 行逐行有 PDF 出处; 无 KB 自写解释内容 (D6 无), 无伪节号。

### G-TB6 结构行签字
- assumptions.md:3 `## ML – Description/Overview` (PDF p121 标题) ✓
- assumptions.md:7 `## ML – Specification` (PDF p121 标题) ✓
- assumptions.md:11 `## ML – Assumptions` (PDF p122 标题) ✓
- 空行 :2/:4/:6/:8/:10 ✓。新增正文 :5 / :9 逐字 (cmp) ✓; examples.md:55 改动行有出处 ✓。无出处词句 0。

### 无副作用
本批 KB 改动仅 ML/assumptions.md (授权范围: Description/Overview + spec 首句 + PDF 原有小标题) 与 ML/examples.md:55 (白名单); assumptions 列表未动; 锚点/既有标题未变; 无其他文件。

### 范围外 (沿用 writer)
F-1 脚注 → O15; F-2 CT 列 `*`/DOMAIN 值 → 全库约定; F-3 弯引号 → O40; 原子错 p0121_a011 (MLGRID) / p0122_a015 (NCIBI) / p0122_a017 ("not") / p0123_a012 ("row.") / p0124_a001 (MIDSDTC 截断) 供 ledger 修正参考。
