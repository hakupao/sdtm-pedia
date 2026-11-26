# T2 B-FA reviewer

## attempt 1

> reviewer = oh-my-claudecode:code-reviewer (opus), 2026-11-26. 与 writer 不同 agent / invocation. 未改 KB. scratch = `$S` = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-FA_reviewer`.
> 审查对象 md5 (= writer 报告 after): FA/assumptions 99f5b237… / FA/examples 23bbc598… / ch02 1c39874b… / model/02 2180f142…. `git diff --numstat 4f8bde8`: ch02 0/33, FA/assumptions 66/23, FA/examples 20/21, model/02 0/18.

### Verdict: **CONDITIONAL**

writer 主体工作正确 (§6.4/§6.4.1 逐字重建、§6.4.2/§6.4.3 RELOCATE、census 3 表修正、PAPRNG/NUMEPISD 方向均核实无误). 阻断项 3 条 (C-1..C-3), 均为小改动.

### 修正清单 (writer attempt 2 执行; 改后回 reviewer 复审 delta)
| # | 位置 | 修正 | 依据 |
|---|---|---|---|
| C-1 | FA/assumptions.md :111 与 :113 之间 | 插入 `## FA – Specification` + 空行 + 逐字句 `fa.xpt, Findings About Events or Interventions — Findings About. One record per finding, per object, per time point, per visit per subject, Tabulation.` | dispatch 补充口径 "域 spec 首句 … 各批遇到缺失即补"; PDF p365 首行; 先例 CM/assumptions.md:7-9, AE/assumptions.md:7-9. 现 FA 两文件均无此句 (grep `fa.xpt` 0 命中) |
| C-2 | FA/examples.md :263-264 (Ex6 纸质 CRF) | 表头行与分隔行补到 9 列: `\| AE ID \| Adverse Event \| Start Date \| End Date \| At each visit, record the maximum severity of the adverse event since the last visit. \|  \|  \|  \|  \|` + `\|---\|---\|---\|---\|---\|---\|---\|---\|---\|`; :265-268 不动 | R2 recheck ig34_p0374_a011 = REAL_GAP (见下). 方案 A 与原子 a011 verbatim 列数一致, fp a011-a014 命中不变 |
| C-3 | FA/examples.md :118 | "linked to the parent CE record" → "linked to the parent AE record", 登记 PDF_TYPO T-7 (改正) | 补充口径 PDF_TYPO 取舍: 正确值由 PDF 自身可定 — 同例 p369 "the rash itself was represented in the AE domain", relrec RDOMAIN=AE, ae.xpt 父记录. 主控若判 "叙述措辞不改" 可改回 T4, 但须与 T-9 同口径 |

非阻断 (主控裁定, 不要求本 attempt):
- N-1 FA/assumptions.md 结构顺序: 假设 1-6 (:3-15, PDF p366-367 "FA – Assumptions") 在 §6.4 之前且无 `## FA – Assumptions` 标题; PDF 顺序为 §6.4 → 6.4.1-6.4.3 → 6.4.4 Description → Specification → Assumptions. 基线既有, writer 新增 :17 标题沿用了该顺序. 若主控要按 CM/AE 先例整理, 应单列一步.
- N-2 PDF 标题 "6.4.4 Findings About Events or Interventions (FA)" (ig34_p0364_a020) 在 KB 被并入 `## §6.4.4 FA – Description/Overview`, 基线既有, 未动.
- N-3 Ex5 CRF (p373) Diarrhea/Nausea 的 Volume 格在 PDF 为灰底 (不适用), KB 空白; 基线既有, 未触碰.

### 命令 (repo 根, 可复跑) 与结果
```
S=<scratch 如上>; mkdir -p $S
python3 -I -c "...B-FA.json pdf_ranges -> $S/manifest.json"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1
  -> "KB tables: 25; status: {'UNPARSEABLE': 10, 'OK': 15}; PDF_ONLY: 324; cells compared: 1169; diffs: 0"  (exit 1 来自全局 PDF_ONLY; 本批 pdf_pages 内 pdf_only 0, pdf_unparsed 0)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # exit 1
  -> "hit_target: 3798 ... regressions=42 new_hits=475 RESULT: RED"
# 隔离: KB 拷贝 + 本批 4 文件换回 4f8bde8
cp -R knowledge_base $S/basekb; for f in domains/FA/assumptions.md domains/FA/examples.md chapters/ch02_fundamentals.md model/02_observation_classes.md; do git show 4f8bde8:knowledge_base/$f > $S/basekb/$f; done
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/basekb --out $S/fp_noFA.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress_noFA.jsonl
  -> "regressions=21"; 集合差: 仅含 B-FA 时回归 = 23 条 (下), 仅不含时 = ig34_p0262_a029/a030 (MS 批并发改 MS/examples, 与 FA 文件无关; FA 文件不含该行)
python3 tools/check_links.py  -> "broken relative links: 18668 (live docs: 42)"  (≤42 基线)
pdftoppm -f 361 -l 375 -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p   # 逐页 Read 过 p361-364, p367, p369-374
双向扫描脚本: $S/cmp.py (FA/assumptions :17-111 vs p361-364; :1-15 vs p366-367), $S/ex.py (examples 叙述 → p367-375), 原子侧逐条 fp_match.norm 直查 (见 G)
```

### fp (H)
- B-FA 致 hit_target 丢失 **23** (writer 写 24, 其枚举实为 23: p0363 a011-a013,a015-a019 = 8; p0364 a001-a009,a011-a013,a017-a019 = 15). 全部是 RELOCATE target 迁移: 逐条 `norm(verbatim) in norm(FA/assumptions.md)` = True (含 a013 表头, hit_any 显示 FA/examples 只是 glob 序). 台账 targets 须由主控补 `knowledge_base/domains/FA/assumptions.md`.
- 其余 19 条回归 (p0118, p0215, p0218, p0254-p0263, p0396): targets 均不含本批 4 文件; 隔离运行确认与 B-FA 无关 (他批工作区改动). B-FA 非预期回归 = **0**.
- B-FA 新增 hit_target 13 (p0368_a005, p0370_a009/a016, p0371_a019-a023, p0373_a012/a024/a027, p0374_a001/a005), 与 writer 一致.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| FA/assumptions.md (缺) | 完整 / dispatch 域 spec 首句 | spec 首句缺 → C-1 | p365 "fa.xpt, Findings About Events or Interventions — Findings About. One record per finding…" |
| ig34_p0374_a011 / examples.md:263 | R2 recheck / G-TB4 | 表头 6 列、数据行 9 列; GFM 丢弃超出表头的格 → Visit 4/5/6 及其选项渲染时消失 → C-2 | p374 渲染: 9 列, "Visit 2 … Visit 6" |
| examples.md:118 T-7 | PDF_TYPO 取舍 | 正确值 PDF 自身可定, 应改正+登记 → C-3 | p370 "linked to the parent CE record"; relrec RDOMAIN "AE" |
| writer 报告 fp 段 | 记账 | "24" 应为 23 | 见 fp 段 |
| T-9 examples.md:228 | PDF_TYPO 取舍 | 见 Open Questions | p373 "FAEVINTX indicates that assessments were for the previous 24 hours" |

### (A) RELOCATE 源侧整块删除 — 逐行核
- ch02 base :187-219 共 33 行 (diff hunk `@@ -184,36 +184,3 @@`, 0 插入, 删到文件尾; 现文件以 :186 "…general observation class." + \n 结尾). 逐句: 全部 0 命中 ig34 p7-16 (8-gram 与整句均 0); 除 :188 KB 自写标题与 :190 KB 自写引导句 ("The following content is reference material from SDTMIG v3.4 §6.4.2…", 与 §6.4.2 本体重复的导航/说明, 随 RELOCATE 删除合理) 外, 其余 :192-219 每句都在 FA/assumptions.md §6.4.1 PtC (:59-62) / §6.4.2 (:69-89) 逐字存在. p7-16 中唯一 FA 字样为 p8 "Updated guidance and examples for the FA domain. See Section 6.4" (ch01 版本说明), 与被删块无关.
- 与 B-ch02 的对账: `t2_B-ch02_review.md:109` 明写 "| :188 / :214 FA 节 | B-FA 范围 | 不审 |"; `t2_B-ch02_audit.md:31` 扫描范围 "KB(ch02 FA 参考节之前)". 故 B-ch02 "每行溯源 p11-16" 不含本块, 无矛盾.
- model/02 base :206-223 共 18 行 (1 hunk, 0 插入). 逐句 vs sv20 全 74 页: 0 命中, 仅 3 处子串偶合 ("For example," / 表格 "SEV Severity/Intensity" / "TOXGR Toxicity Grade" 与 sv20 变量表 --SEV/--TOXGR 行偶合, 非本段出处); model/02 自身 --SEV (:125) / --TOXGR (:149) 变量行仍在. 其余每句在 FA §6.4.3 (:93-107) 逐字存在. 保留的 `### Findings About (Subtype)` :198-204 (sv20 §3.1.3.1) 未动.
- 结论: 无应保留的行; 超出 delete_only_source_lines 的整块删除成立 (按 B-FA.json notes 第 4 条). 全仓 (除 archive/releases) 无指向两旧标题的引用.

### (B) PAPRNG / NUMEPISD 方向
- 渲染 p370 faae Row 3/10 FATESTCD = **PAPRNG**; p373 Row 3/6, p374 Row 9/13 = **NUMEPISD**. 基线 KB = FAPRNG / NUMEPISO (`git show 4f8bde8:…examples.md` :105/:112/:244/:247/:250/:254). 现 KB = PDF. T1 lane 记 "PAPRNG→FAPRNG, NUMEPISD→NUMEPISO" = "PDF 值→KB 错值" 记法; writer "FAPRNG→PAPRNG" = "改前→改后" 记法; 两者描述同一修正, 方向一致.
- 是否 PDF 笔误: PAPRNG 与同表 MACRNG/VESRNG/PUSRNG/SCBRNG/SCRRNG (病损名前 3 字母 + RNG) 同构, 非笔误. NUMEPISD: PDF 4 处一致; SDTM Terminology.xlsx 中 "Number of Episodes" 的 CT 码为 EPSDNUM (codelist C124281), NUMEPISD/NUMEPISO 都不是 CT 值 → 例子中的 sponsor 码, KB 照 PDF 正确, 无需登记 T4.

### (C)(D) §6.4 / §6.4.1 / §6.4.2 / §6.4.3 逐句 (vs 文本层 + 渲染 p361-364)
- `$S/cmp.py` KB→PDF: :17-111 每句命中, 只差 4 个标题行 (带 § 前缀) 与 T-2/T-5 改正句 (:29,:31,:37,:45,:49 "Section 6.4.4," ; :64 "e.g.,"). PDF→KB: 只差同样的 T-2/T-5 句与 6.4.4 标题合并 (N-2). 渲染核: 段落切分、Criterion 1-3 只粗体 "Criterion n:" 标签、"Points to Consider" 小标题、PtC 4 条 • + 1 条 o 子条、§6.4.2 1/2/3 → o → ▪ 三层嵌套、“FA” 弯引号 ×2 与 "FA" 直引号 (RDOMAIN 句) 均与 KB 一致; FATESTCD 3 行表逐格一致.
- 旧文本删除 (D-1) 合理: 旧 :19-60 多处与 PDF 矛盾 (例 旧 :31 "maximum severity of headache" vs p362 "number of episodes of vomiting"; 旧 :39 Criterion 2 标题被改; 旧 :45-49 "Previous versions" 两段改义, 旧 :49 残句), 且不承载 fp 台账原子 (p361-363 原子不在台账). 28 个新原子 p0361_a010..p0363_a009 逐条直查: 21 条 norm 命中 FA/assumptions; 7 条非 EXACT 均已解释 = T-2 (a016/a017, p0362_a002/a006/a008)、T-5 (p0363_a008)、原子抽错 (p0362_a010 原子多 "to"; 渲染 p362 为 "thought be related").
- Description :111 补全 (p0364_a022) 命中.

### (E) R2 recheck
| atom | KB 行 | 判定 | 理由 |
|---|---|---|---|
| ig34_p0367_a013 | examples.md:14 | REWRITE_OK | 渲染 p367: PDF 本身就是 1 行 2 格, 格内折行 ("Associated symptoms:" + 4 症状 / 4 组 "○ No ○ Yes"); KB :14 同为 1 行 2 格, 全部片段按原序给出, 无丢失 (只少格内换行) |
| ig34_p0367_a016 | examples.md:17 | REWRITE_OK | 同上 (30 minutes AFTER 段) |
| ig34_p0367_a019 | examples.md:20 | REWRITE_OK | 同上 (90 minutes AFTER 段) |
| ig34_p0374_a011 | examples.md:263-268 | **REAL_GAP** | 表头 6 列 (:263)、分隔 6 列 (:264), 数据行 9 列 (:265-268); 按 GFM 超出表头的格被丢弃, 渲染只剩 Visit 2/3, "Visit 4/5/6" 与对应 3×3 选项格丢失. → C-2 (方案 A 补表头/分隔到 9 列). 方案 B (完全照渲染: 第 1 行 4 空格 + 说明, 第 2 行 AE ID…Visit 6) 版面更像 PDF, 但会使原子 a011/a012 的 fp 命中失效, 不推荐 |

### (F) PDF_TYPO 10 条逐条裁定 (依补充口径取舍规则)
| T | 处置 | 裁定 |
|---|---|---|
| T-1 ”findings about” 引号字形 (:23) | 改正 | 同意 (标点, PDF 自身可定) |
| T-2 "Section 6.4.4.," ×5 | 改正 | 同意 (同节 "Section 6.4.1," 无多余句点) |
| T-3 "These type of" (:33) | 照录 + T4 | 同意 (语法类; 先例 B-DS U-4 照录; B-IS T-5 改正亦被接受, 口径两可, 交 T4 汇总) |
| T-4 "thought be related" (:53) | 照录 + T4 | 同意; 渲染 p362 确认 PDF 无 "to" |
| T-5 "(e.g, When?" (:64) | 改正 | 同意 |
| T-6 "FA may provided" (:65) | 照录 + T4 | 同意 (同 T-3) |
| T-7 "parent CE record" (examples :118) | 照录 + T4 | **不同意** → C-3 (PDF 同例自身可定为 AE) |
| T-8 "used to populated FADTC" (:183) | 照录 + T4 | 同意 (语法类) |
| T-9 叙述 FAEVINTX vs 表列 FAEVLINT (:228 / :239) | 照录 + T4 | 暂同意, 列 Open Question (见下) |
| T-10 Ex6 relrec STUDYID ABC vs faae XYZ (:321-322) | 照录 + T4 | 同意 (同例 ae.xpt 无 STUDYID, USUBJID 123 vs XYZ-US-701-002 亦不一致, 无单值可定) |
- D6 (:283): 前缀 `> KB note (not in SDTMIG):` 合乎 domains/ 措辞; 内容 (CRF 示 Visits 2-6、最多 3 个 AE; 满足 criterion 1) 与 p374-375 不矛盾 → 保留成立.

### (G) 双向全扫 (FA PDF 页 p361-364, p366-375, 含表格原子)
- PDF 原子 → KB: p367-375 原子 220 条 (TABLE_ROW 119 / SENTENCE 28 / LIST_ITEM 23 / TABLE_HEADER 24 / CODE_LITERAL 15 / HEADING 11) 逐条 `fp_match.norm` 直查 FA 两文件: 217 命中; 未命中 3 = p0373_a021 (原子把表头抽成 FAEVINTX, 渲染 p373 为 FAEVLINT, KB 正确)、p0375_a025/a026 (SR Description, 属 B-SR, OOS-2). p361-364 见 (C).
- KB → PDF: examples.md 全部叙述行逐句命中 p367-375, 仅 :1 文件标题、:283 D6 note. assumptions.md :1-15 逐句命中 p366-367.
- 表格: census 本批数据表 15 张全 OK, 0 diff (3 张原 DIFF 已修); 独立复核 (渲染) mh p371 全 6 行 16 列、faae p370 Row 3/10、face p373-374 Row 3/6/9/13 一致.
- 人工逐格 (UNPARSEABLE 10 张, 对渲染):

| KB 表 | PDF | 结果 |
|---|---|---|
| assumptions.md:97 FATESTCD/FATEST (新增) | p364 | 4 行 × 2 格一致 |
| examples.md:7 Ex1 CRF | p367 | 12 行一致 (症状格见 E: REWRITE_OK); 粗体 "5 minutes BEFORE dosing" 等未保留粗体, 文字一致 |
| examples.md:76 Ex2 CRF | p369 | 10 行一致 (填空线长度差视为版面) |
| examples.md:133 / :138 Ex3 CRF | p371 | 2+1 行 / 5 行一致; 表题转为 `###` 标题 (基线既有); 填空线 ___ vs _____ 版面 |
| examples.md:176 Ex4 CRF | p372 | 一致; PDF 3 症状同格折行 → KB 拆 3 行, 无丢失 |
| examples.md:219 Ex5 CRF | p373 | 一致; 灰底格未表达 (N-3) |
| examples.md:263 Ex6 CRF | p374 | **列数缺陷** → C-2 |
| examples.md:273 / :279 Ex6 模块表 | p374 | 一致 |

### G-TB6 新增 / 改动行 (72 行 + 删除) 结构行签字
- FA/assumptions.md:17 `## §6.4 Findings About Events or Interventions` — 新增节标题, 对应 p361 "6.4" 标题, 签字.
- :25 / :43 / :47 `**Criterion n:**` 粗体标签 — 对应 PDF 粗体, 签字. :57 `**Points to Consider**` — PDF 小标题, 签字.
- :67 / :91 既有标题, 其下补 PDF 全文; :97-98 表头 + 分隔线 — 签字.
- examples.md:283 `> KB note (not in SDTMIG):` 前缀 — D6 结构, 签字.
- 其余新增行全部有 PDF 出处 (见 C/G); 无出处词句 = 0.

### 范围 / 副作用
- 本批 4 文件 md5 = writer 报告; 工作区其他 KB 改动 (ch08, MB, MS, OE, TA) 属他批. 标题/锚点: 删除 ch02 `## Findings About — …(Reference Material)` 与 model/02 `### §6.4.3 …(Reference Material…)` 两 KB 自写标题 (RELOCATE), 无引用; 其余未变.
- Ex2 "Additional data…" 段移至 ae.xpt 后、Ex4 Row 1/2 注释移至 ae.xpt 前: 渲染 p370 / p372-373 顺序一致, 签字. examples.md:30 去 "the" = p368 原文.

### Open Questions (低置信, 不阻断)
- T-9 (examples.md:228): 叙述 "FAEVINTX" vs 表列 FAEVLINT (-PT24H, ISO 8601 时长). FA spec (p365-366) 不含 --EVLINT/--EVINTX 行, PDF 内唯一佐证是 Ex6 FAEVINTX 列装文本 "SINCE LAST VISIT" — 倾向叙述错, 但需借 SDTM 模型定义才能单值确定. 建议主控与 C-3 同口径定: 若采 C-3, T-9 亦可改正为 FAEVLINT 并登记; 否则两者都留 T4.

## attempt 1 续 复审 (delta C-1..C-3 + 主控裁定)

> Verdict: **PASS**. delta = FA/assumptions +4 行 (:113-116), FA/examples 5 行 (:118, :228, :263-265); numstat 现 assumptions 70/23, examples 25/26, ch02 0/33, model/02 0/18.

| # | 位置 | 核对 | 结果 |
|---|---|---|---|
| 1 | assumptions.md:113 `## FA – Specification` + :115 | p365 标题 "FA – Specification" + 首句逐字 (两行折行合并), 放在 Description (:111) 后 / SR (:117) 前 = PDF 顺序 | 一致, 签字 (结构行 :113) |
| 2 | examples.md:263-268 Ex6 CRF | 对 p374 渲染逐格: 第 1 行 4 空 + "At each visit, record the maximum severity of the adverse event since the last visit." + 4 空 (跨 5 列标题); 第 2 行 AE ID / Adverse Event / Start Date / End Date / Visit 2…Visit 6; 3 数据行 4 空 + 5×"○ Mild ○ Moderate ○ Severe"; 9 列统一 (表头/分隔/数据) | 一致; 按主控裁定以渲染为准, p0374_a011 登记原子抽错 (原子把 AE ID 等放进第 1 行) |
| 3 | examples.md:118 "parent AE record" | p369 "the rash itself was represented in the AE domain" + p370 relrec RDOMAIN=AE → PDF 自身可定 | 同意 T-7 改正+登记 |
| 3 | examples.md:228 "FAEVLINT indicates…" | 同例 face 表列头 FAEVLINT (p373 渲染) 且值全为 -PT24H (ISO 8601 时长); Ex6 FAEVINTX 列装文本 "SINCE LAST VISIT" 佐证; 主控据同例表列定 → 接受 | 同意 T-9 改正+登记 (原 Open Question 关闭) |
| 4 | fp | `fp_match.py --out $S/fp_after2.jsonl --baseline … --regress-out $S/fp_regress2.jsonl` → regressions=48; 其中 p036x/p037x = **26** = 23 target 迁移 (含 p0364_a013) + p0370_a021 (T-7) + p0373_a013 (T-9) + p0374_a011 (原子抽错); 其余 22 条 targets 不含本批文件 (含新增 p0174_a0012 MH / p0262_a029,a030 MS = 他批并行) | B-FA 非预期回归 0 |
| 4 | p0364_a013 表头 `\| FATESTCD \| FATEST \|` | 未丢: `norm` 在 FA/assumptions.md (:97) 与 FA/examples.md 均命中; 回归原因 = 台账 verdict INTENTIONAL_EXCLUDE 且 targets 只有 model/02 (源已删) → 属 target 迁移, 已含在 23 条中. writer 报 "27 = 23 + p0364_a013 + 3" 把 a013 重复计 1 次, 实为 26 | 台账 targets 补 FA/assumptions.md 即消 |
| — | check_links | `python3 tools/check_links.py` → "live docs: 42" | ≤42 |
- p0374_a012 (Visit 行) 仍 hit_target FA/examples.md; C-1..C-3 无新增无出处词句.
