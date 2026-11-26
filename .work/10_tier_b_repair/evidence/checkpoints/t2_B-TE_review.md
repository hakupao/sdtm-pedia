# T2 reviewer — B-TE (attempt 1)

- reviewer: `oh-my-claudecode:code-reviewer` (opus), 与 writer 不同 agent / invocation; 只读 KB, 未 stash/checkout/reset
- base = HEAD `884560f`, 本批改动未提交; 审查对象 md5 (= writer 报告 after 值, 一致):
  TA/assumptions.md `e7234e69d34e4258d072f7a3fdd1c455`; TE/assumptions.md `31755a61375a08e79f4bb7b3b9824d65`; TE/examples.md `caf18faeed5551832544a02ded3bb6f1`
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TE_reviewer/`

## Verdict: **PASS**

无 HIGH/CRITICAL 问题; 6/6 atoms 落地, pdf_only special.xpt 4 行补齐且逐格对渲染一致, 3-step 不可机检表逐格一致, TA D2 去重内容 24/24 句在 TE 副本中存在, 无出处新增行 0。
下列 LOW 项为记录/后续口径, 不阻塞。

## 页范围核实 (O27)
- `pdftotext -layout` 核 PDF: p402 第 50 行 `7.2.2 Trial Elements (TE)` + `TE – Description/Overview`; p407 第 23 行 `7.3 Schedule for Assessments`; p408 = TV。
  → TE 实际 = **p402–407** (batch json `pdf_ranges` 404–409 错, 已登记 O27)。本审 manifest 改为 402–407。

## 命令与结果 (可复跑; S = 上面 scratch)
```
python3 -I -c "import json;json.dump([{'file':'knowledge_base/domains/TE/assumptions.md','src':'ig34','lo':402,'hi':407},{'file':'knowledge_base/domains/TE/examples.md','src':'ig34','lo':402,'hi':407}],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  → exit 1; "KB tables: 5; status: {'OK': 4, 'UNPARSEABLE': 1}; cells compared: 168; diffs: 0; RESULT: RED"
  RED 仅因全局 PDF_ONLY 列表; 落在 402–407 的 PDF_ONLY 只有 TA Ex7 ta.xpt (p401–402, §7.2.1, 属 TA 非本批)。pdf_unparsed 只有 p274/p342 (非本批)。
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  → exit 1; RESULT: RED, 48 条回归, 全部不在 p402–407; 唯一 TA/TE 相关 ig34_p0396_a009 (target TA/examples.md) —
    TA/examples.md 本工作树无改动 (git status 无), 回归来自已提交的 d33674e (B-TA), 与本批无关。
python3 tools/check_links.py 2>&1 | grep "live docs"   → "broken relative links: 18668 (live docs: 42)" = 基线 42 (写完本证据后复跑仍 42)
  (注: 汇总行走 stderr, `| tail -1` 只拿到 stdout 清单末行; 需 `2>&1 | grep`)
```

## census_after (本批 KB 表)
| KB 表 | 状态 | 复核方式 |
|---|---|---|
| TE/examples.md:11 Ex1 te.xpt (5 行) | OK, 40 格 0 diff | 渲染 p405 目视一致 |
| TE/examples.md:25 Ex2 te.xpt (6 行) | OK, 48 格 | 渲染 p405 一致 |
| TE/examples.md:40 Ex3 te.xpt (5 行) | OK, 40 格 | 渲染 p405 一致 (Row1/Row4 TEDUR 空) |
| TE/examples.md:79 3-step 表 | UNPARSEABLE | 人工逐格 (下表) |
| TE/examples.md:99 special.xpt (4 行, 新建) | OK, 40 格 | 独立方法: 渲染 p407 (160/400/1200 dpi) 逐格 (下表) |

## 人工逐格 — TE/examples.md:79 3-step 表 vs p406 渲染 (160 dpi)
| 行 | Step | Step question | How step question is answered… | 结果 |
|---|---|---|---|---|
| 表头 | Step | Step question | How step question is answered by information in the TA datasets | 一致 |
| 1 | 1 | 一致 | 一致 ("…are in TEENRL in the TE dataset.") | 一致 |
| 2 | 2 | 一致 | 一致; 本批改动 "branch" → "branch point" 对 (PDF "If there is a branch point at this point in the trial") | 一致 |
| 3 | 3 | 一致 | 一致 ("…specified in TESTRL in the TE dataset.") | 一致 |

## 人工逐格 — special.xpt vs p407 渲染 (独立于 census bbox)
| Row | ARM | EPOCH | TAETORD | ELEMENT | TESTRL | TEENRL | TEDUR | TABRANCH | TATRANS |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 一致 | 一致 | 一致 | 一致 | 一致 | 一致 | 空=空 | 一致 ("Randomized to A") | 空=空 |
| 2 | 一致 | 一致 | 一致 | 一致 | 一致 (含 "in", 见 T-1) | 一致 | 一致 P5D | 空=空 | 空=空 |
| 3 | 一致 | 一致 | 一致 | 一致 | 一致 | 一致 (见 T-2) | 空=空 | 空=空 | 一致 ("If disease progression, go to Follow-up Epoch") |
| 4 | 一致 | 一致 | 一致 | 一致 | 一致 | 一致 | 一致 P5D | 空=空 | 空=空 |
- 表头 10 列一致; 表名: 1200 dpi 下读作 `special.xpt` (bbox word 同), KB `**special.xpt**` (加粗为本文件惯例)。
- 位置: PDF 中表在 p406 "Note that" 两 bullet 之后、p407 "Note that rows 2 and 4" 段之前; KB :93–106 顺序一致。

## atoms 逐条 (norm(verbatim) in norm(target) 直查)
| atom | target | 命中 | KB 行 | 备注 |
|---|---|---|---|---|
| ig34_p0403_a011 | TE/assumptions.md | 是 | :13 | |
| ig34_p0404_a012 | TE/assumptions.md | 是 | :49 | |
| ig34_p0407_a003 | TE/examples.md | 是 | :101 | |
| ig34_p0407_a004 | TE/examples.md | 是 | :102 | |
| ig34_p0407_a005 | TE/examples.md | 是 | :103 | atom verbatim 把 TATRANS 值放在 TABRANCH 列 (抽取错位); 渲染/census 均证 KB 放 TATRANS 正确 (L-3) |
| ig34_p0407_a006 | TE/examples.md | 是 | :104 | |
t2_recheck = 0 条 (无 R2 判定项)。

## G-TB6 反向溯源 (diff 每条新增/改动行)
| diff 行 (改后) | 出处 | 结论 |
|---|---|---|
| TE/asm:11 (拆段前半) | p403 "An element is a building block … called elements." | 有出处; 渲染 p403 确为独立段 |
| TE/asm:13 | p403 "Trial elements represent … conditions for leaving the element." | 有出处; "valid element" 与 PDF 原词一致 |
| TE/asm:15 `## TE — Specification` | p403 "TE – Specification" | 结构行, 签字 |
| TE/asm:17 spec 首句 | p403 "te.xpt, Trial Elements — Trial Design. One record per planned Element, Tabulation." | 逐字一致 |
| TE/asm:19 `## TE — Assumptions` | p403 "TE – Assumptions" | 结构行, 签字 (与本文件 :3 "—" 风格一致, CM 先例为 "–", L-2) |
| TE/asm:27 尾 2 句 | p404 "For example, every arm of a trial that involves treating disease episodes …randomization." | 有出处 |
| TE/asm:45 | p404 "15 days after start of element and after WBC values have recovered" | 有出处 |
| TE/asm:47 | p404 "TEDUR is expressed in ISO 8601." | 有出处 (删扩写 "format") |
| TE/asm:49 尾句 | p404 "For instance, a washout with a fixed duration of 14 days …otherwise." | 有出处 |
| TE/ex:63 (缩进) | p406 该段渲染在 c. 下缩进 | 有出处, 仅格式 |
| TE/ex:82 | p406 "If there is a branch point at this point" | 有出处 |
| TE/ex:87,89,91,93–95 | p406 "As illustrated in the table…", "It can be useful…", "However, such a working dataset…", "The following table shows a fragment…", "Note that" + 2 bullets | 均有出处 |
| TE/ex:97 `**special.xpt**` | p407 表名 | 结构行, 签字 |
| TE/ex:99–100 表头+分隔线 | p407 表头 | 结构行, 签字 |
| TE/ex:101–104 | p407 Row 1–4 | 逐格见上 |
| TE/ex:106 | p407 "Note that rows 2 and 4 … their first dose in this element." | 有出处 |
| TA/asm:104 `> See `[../TE/examples.md#distinguishing-elements-study-cells-and-epochs](…)` for this text.` | D2 交叉引用 (导航, 无需 D6) | 结构行, 签字; 锚点 slug 对应 TE/examples.md:65 标题 |
| TA/asm:108 `> See `[../TE/examples.md#transitions-between-elements](…)` for this text.` | 同上 | 结构行, 签字; slug 对应 :75 |
新增/改动行 21 处 (含结构行 6), 无出处 0。

## TA D2 去重核实
- diff: TA/assumptions.md 仅删 base :104–122 与 :126–150 (+2 行交叉引用), 两个 `### §7.2.2.1 …` 标题保留; :110 `## TA-Specific Assumptions` 及之前 TA 自身内容 (§7.1/§7.2.1 段、Example 2 / 7.2.1.1 指针) 未动。
- 被删 24 个非空行逐行 norm (引号归一) 比对 TE/examples.md 改后: **24/24 IN_TE, 0 MISSING** (脚本见 scratch 命令记录)。
- 归属: 被删文本为 PDF p406–407 §7.2.2.1 (TE Issues), 留 TE 份符合 D2 "留 PDF 所属节那份"; TE 份本批已对 PDF 补全 (3-step 表原有, special.xpt 新建, 叙述 4 段补入)。
- 与主控 "一行交叉引用" 差异: 两小节各一行 (共 2 行) 并保留标题 — 仿 TA :94–100 既有写法, 可接受 (L-1)。
- 全仓引用: 无对 TA 这两节锚点的引用 (writer 未截断 grep; check_links live docs 42 未升)。

## 双向全扫 (p402 §7.2.2 起 – p407 §7.3 前; 含表格原子)
- 脚本: pdftotext p402–407 切 `7.2.2 Trial Elements (TE)`..`7.3 Schedule` → KB 两文件逐句/逐格 norm 互查。
- KB→PDF: 全部命中, 余 3 条残差均为 PDF 折行连字符伪差 (`non-treatment`/`2-week`) 与 Ex2 Row4 单元格折行 ("10 mg / drug"), 渲染核一致。
- PDF→KB: 未命中仅为 (a) spec 变量表 + 脚注 (属 TE/spec.md, 不在 kb_files; writer F-1 已登记), (b) 标题与句子/表格在 pdftotext 中粘连的伪差, 逐条人工确认 KB 有对应。
- 表格原子: Ex1/2/3、3-step、special.xpt 全部逐格过 (census + 渲染)。
- KB_AUTHORED / D6: 本批两文件无 KB 自写解释性内容; 无 D6 标注需确认 (0 条)。TA 交叉引用为纯导航。

## T-1 / T-2 依据核验
- T-1 (Row 2/4 TESTRL "First dose of treatment in Element, …"): 渲染 p407 两行确有 "in"; p407 叙述引作 "First dose of treatment Element, …"; TE Ex3 Row 2/3 (p405) 无 "in"。
  依据成立 (PDF 内部矛盾属实)。补充给 T4 裁定: 3 处无 "in" (Ex3 Row2、Row3、p407 叙述) vs 2 处有 (片段表 Row2/4), 且片段表定义为 "supplements the TA dataset with the TESTRL…" 即取自 TE 值 → 若用户按 "可由 PDF 自身确定" 规则, 倾向去 "in"; 照录 + T4 亦合规 (L-4)。
- T-2 (Row 3 TEENRL "16 days after start of Element and WBC recovers" vs Ex3 "At least 16 days … WBC recovered"): 两处差异 ("At least"、时态) 无法由 PDF 唯一确定哪处为准, 照录 + T4 依据成立。

## 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| L-1 TA/asm:102–108 | 位置/D2 | 交叉引用 2 行 + 保留 2 标题, 而非主控说的 "一行" | 仿 TA:94–100 既有写法, 保锚点; LOW, 不改 |
| L-2 TE/asm:15,19 | 结构 | 新标题用 "—" (本文件风格), CM 先例用 "–" | 文件内一致; LOW, O15/O16 统一时可顺带 |
| L-3 atom ig34_p0407_a005 | 原子数据 | atom verbatim 列错位 (TATRANS 值在 TABRANCH 位) | p407 渲染: "If disease progression…" 在 TATRANS 列; KB 正确; 建议 pdf_atoms 勘误 |
| L-4 T-1 | PDF_TYPO 口径 | 有 3:2 多数且语义上片段表取自 TE, 或可按 "PDF 自身可定" 处理 | 见上; 交 T4 用户裁定 |
| L-5 TE/ex:58–61 (既有, 非本批 diff) | 渲染格式 | a./b./c. 行紧接 item 3 无空行, Markdown 渲染会并入 item 3 段落 | 内容与 p405–406 一致; LOW, 可后续格式批 |
| L-6 batch json | 元数据 | pdf_ranges 404–409 应为 402–407 | O27 已登记 |

## 无副作用
- `git diff HEAD --stat -- knowledge_base/`: 本批仅 TE/assumptions.md、TE/examples.md、TA/assumptions.md; 其余 BE/MK/TU 6 文件属别批 (B-BE/B-MK/B-TU), 未审。
- 本批 diff 全文已读 (未截断), 无异常 / 外来内容; 标题锚点未变 (新增 `## TE — Specification`/`## TE — Assumptions` 除外); 已有正确表行未改坏 (census OK + 渲染)。
- writer stash/pop: 本批三文件 md5 与 writer 报告 after 值一致。
