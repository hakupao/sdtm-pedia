# T2 B-TA auditor report (Rule A 独立抽检) — attempt 1 (auditor), 对应 writer attempt 2 终态

> agent: oh-my-claudecode:verifier (opus); 2026-11-26; 不改 KB; scratch = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-TA_auditor/`
> 审计对象: `git diff 466e0c3 -- knowledge_base/domains/TA/` (466e0c3..HEAD 间 TA 无改动, 已核); examples.md md5 `a1a95b892cd9c2fbe77eb920f893e964`, assumptions.md md5 `ea6bd5233aff46ae8b3d99ce9fc8cbd4` (= reviewer 终态签字值, 写报告前复核)

## 结论: **FAIL** (范围窄: 仅 Mermaid 注释标签; prose 丢失 0 / 忠实错误 0)

## 1. 抽样 (t2_auditor_v1.0 命令原样, batch=B-TA, seed=20261126)
`python3 -I - <<'EOF' > $S/sample.json` (prompt 中脚本逐字) → C=17, P=82, N=10 (C 抽 5 + P−C 抽 5)

| # | atom_id | PDF 页 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0398_a024 | p398 Ex6: TAETORD 主要用途是排序, 留空号不影响 | examples.md:804 | 否 | 是 | Ex6 TA 前段 ✓ | 全文 verbatim 子串命中 |
| 2 | ig34_p0398_a023 | p398 Ex6: 括号句 arm B follow-up 也可取 TAETORD 10 | examples.md:804 | 否 | 是 | ✓ | 同上 |
| 3 | ig34_p0384_a016 | p384 §7.2 引言: 本小节含 TE/TA 两数据集 (含 Section 7.2.2/7.2.1 交叉引用) | assumptions.md:76 | 否 | 是 | §7.2 下 ✓ | 交叉引用 2 处在 |
| 4 | ig34_p0397_a007 | p397 Ex5: 去掉该假设后与 Trial 4 本质相同 | examples.md:689 | 否 | 是 | Ex5 ✓ | |
| 5 | ig34_p0397_a010 | p397 Ex5: TDM 与 Ex4 几乎相同, 仅最大周期数=3 | examples.md:715 | 否 | 是 | Ex5 TDM 前 ✓ | |
| 6 | ig34_p0384_a011 | p384 §7.1.3: 部分剂量递增研究每剂量新队列 → arm 数不定 | assumptions.md:66 | 否 | 是 | §7.1.3 ✓ | 对照原子 |
| 7 | ig34_p0389_a021 | p389 Ex2 首段: 交叉试验图不用交叉斜线 … 元素可复用 | examples.md:161 | 否 | 是 | Ex2 首段 ✓ | assumptions.md 原副本已 D-1 去重 |
| 8 | ig34_p0396_a003 | p396 Ex4: TDM 对应显式重复的回顾视图 | examples.md:631 | 否 | 是 | Ex4 TDM 前 ✓ | |
| 9 | ig34_p0387_a008 | p387 Ex1: 用 "blocks" 画元素 … 见 Section 7.2.2 | examples.md:26 | 否 | 是 | Ex1 ✓ | 交叉引用在 |
| 10 | ig34_p0384_a014 | p384 §7.1.3: 已完成试验递交不受这些限制影响 | assumptions.md:72 | 否 | 是 | §7.1.3 ✓ | 对照原子 |

判定方法: `python3 -I $S/chk.py` — 每个原子的完整 verbatim (归一引号/破折号) 作为子串在目标文件命中, 且在 pdftotext p382-402 中命中 (非截断), 行号由脚本定位; 位置按所在 KB 节人工核.
**独有丢失 0 / 忠实度错误 0.**

### 1b. R3 叙述恢复补抽 (atoms[] 外, 主控要求重抽)
`python3 -I $S/supp.py $S/ta.diff` (seed 20261126, 池 = examples.md Ex2/Ex3/Ex7 段中 diff 新增 prose 句, 60 句, 抽 12): 12/12 与 PDF 对应页逐字一致 (p389/390/392/393/399/400), 均位于所属 Example 段. 丢失 0 / 忠实 0.

### 1c. 全量双向扫描 (非抽样, 兜底)
- PDF→KB: `python3 -I $S/ngram.py 382 402` (6-gram 覆盖): 未覆盖片段只剩 节标题拼行 / spec 表 (属 spec.md) / ta.xpt 表折行残片 → prose 0 缺.
- KB→PDF: `python3 -I $S/rev.py` (5-gram, p380-424): 未覆盖仅标题、2 条 D2 交叉引用行 (assumptions.md:96/:100), 无无出处正文.
- diff 新增句逐字: `python3 -I $S/exact.py $S/ta.diff` → 138 句中 130 句逐字在 PDF; 8 例外 = 2 交叉引用行 + 3 图注 (`> \*Disease evaluation earlier …`, 转义形式) + 2 行加粗 (`**Branch rules**`/`**Transition rules**`) + 1 补句点 (p392 "this trial The names", PDF_TYPO T-2). 均非问题.

## 2. D-1..D-17 删除核 (无截断)
`python3 -I $S/chk.py` §3: diff 删除行中与 PDF 逐字一致的句 72 条, 71 条仍在现 KB; 唯一 "缺" = p382 "3 study cell associated" → KB 改 "3 study cells" (PDF_TYPO T-1, 已登记). D-3/D-9/D-12 为与 PDF 矛盾的 KB 自写句, D-13 为 KB 自绘 2-arm 图 (PDF 无此图), D-14..D-17 为 KB 文字代图 (现由 Mermaid 承载); 1c 的 PDF→KB 全量覆盖亦证明无 PDF 叙述丢失. **D-1..D-17 无 PDF 支撑内容丢失.**

## 3. 表格复核 (渲染, 10 格 seeded)
seed 20261126 抽 Ex7 TDM 6 格 + Concept 表 4 格, 对 p401 渲染 (`pdftoppm -f 401 -l 401 -r 120`) 与 p382-383:
- Ex7 TDM: CR[4]=Chemo ✓, CR[5]=Chemo ✓, CR[9]=Off Treatment Follow-up ✓, CRS[1]=Screen ✓, 表头[1]=Screen ✓, 表头[2]=Induction ✓ (合并格按左对齐 + 空列表示, 与渲染一致).
- Concept: Element / Study cells and elements / Epoch 逐字 EXACT; Treatments 词序列 219=219 完全一致 (bullet 扁平化). 10/10 一致.

## 4. Mermaid 4 图 (seed 20261126 从 24 图抽: #2/#15/#16/#20) 对 PDF 渲染逐节点/边/标签
| # | KB 行 | PDF 图 | 节点/边/arm 标签 | 结果 |
|---|---|---|---|---|
| 2 | examples.md:55 | p388 Ex1 Prospective View | 3 epoch / Screen / Run-In / Placebo, Drug A, Drug B / arm 箭头 3 一致; **PDF 有 "Randomization" 注释 (红箭头指 Run-In|Treatment 分界), KB 无** | ✗ 缺标签 |
| 15 | examples.md:552 | p395 Ex4 Retrospective View | 节点/边/arm 一致; **缺 "Randomization" 注释** | ✗ 缺标签 |
| 16 | examples.md:578 | p395 Ex4 Retro with Explicit Repeats | A/Rest×4, B/Rest×4, 3 条 "If disease progression" 跳转/arm 一致; **缺 "Randomization" 注释** | ✗ 缺标签 |
| 20 | examples.md:755 | p398 Ex6 Study Schema | Screen/Drug A/B/Rest/Follow/Randomization/2 个 cycle 注一致; PDF 仅 1 个弯箭头 "Repeat until disease progression" (置于上方), KB 每 arm 1 条 → 同逻辑同标签, 不阻断 | ✓ (观察) |

**阻断 M-1**: 非 Study Schema 的视图 (Prospective / Retrospective / Explicit Repeats / Blinded) PDF 图内都带 "Randomization" 注释 (本次渲染确认: p388 ×3, p390 ×2, p395 ×3, p398 Ex6 Retro, p401 Ex7 Retro), KB Mermaid 全部未画; Ex3 Prosp/Retro/Blinded 另缺 "Response Evaluation" 注释 (reviewer review.md:156 已列, 但标 "可选").
理由: (a) 主控口径 "每个节点/边/arm 标签对 PDF"; (b) examples.md:49 是 PDF 原文, 明说 randomization "is indicated by a note with an arrow", 而紧下方的渲染图没有该注释 → 文图自相矛盾; (c) 同批 reviewer 修正④ 已把 "PDF 有字未画" (arm 箭头) 判为阻断, :156 标可选与其口径不一致.
修法 (仅 examples.md Mermaid, 不涉正文): 对其余约 17 张视图逐图对渲染补 "Randomization" 注释节点 (Ex3 另补 "Response Evaluation"), 指向对应 epoch 分界; 回 reviewer 复审 delta 后再派 auditor.

## 5. fp 隔离 (HEAD + 仅 TA 两文件)
`git archive HEAD knowledge_base | tar -x -C $S/before` (同法 $S/after 再覆盖 TA 两文件; `diff -rq` 仅 TA 两文件不同) →
`fp_match.py --kb-root $S/before/knowledge_base --out $S/fp_before.jsonl`; `fp_match.py --kb-root $S/after/knowledge_base --out $S/fp_after.jsonl --baseline $S/fp_before.jsonl --regress-out $S/fp_regress.jsonl` → regressions=1 仅 ig34_p0396_a009, new_hits=42.
a009 依据: 原子 verbatim "arrow **represents** this rule", pdftotext p396 原文 "arrow **represented** this rule"; KB examples.md:640 = "represented" → KB 正确, 原子抽取错 (ATOM_ERR), 预期回归.
`python3 tools/check_links.py` → live docs 42 (不升).

## 6. G-TB8
- trace: writer `oh-my-claudecode:executor` (a1 134/142, a2 154/161/164) 与 reviewer `oh-my-claudecode:code-reviewer` (151/158/162/166) 均有 subagent_done; 无 `agent: main` 写 TA KB 记录.
- 终态签字: writer 最后改动 = trace 164 (a2 续2, Retro Mermaid 4 图) → reviewer trace 166 PASS 且签 md5 a1a95b89…/ea6bd523…; 本审计时两文件 md5 与之相同 → 签字后无改动. G-TB8 PASS.
- failures 归档: `evidence/failures/t2_B-TA_attempt_1.{md,patch}` 存在 (规则 B).

## 7. 非阻断观察
- O-1: assumptions.md 节标题 "Trial Design Model Overview (§7.1)" / "Trial Arms and Trial Elements (§7.2)" 与 PDF 标题文字不同 (预存, 标题非 prose 原子).
- O-2: assumptions.md:124-150 (§7.2.2.1 TE Issues, "3-step process:" 后无步骤/表, "The following table shows a fragment…" 后无表) 属 TE 页, 非本批 pdf_pages → 范围外, 交 B-TE/O 扫描核.
- O-3: Ex4/Ex5/Ex6 Study Schema KB 每 arm 一条 repeat 边, PDF 单个弯箭头 (见 #20), 逻辑一致.

## 汇总
Rule A N=10 (+R3 补抽 12, + 全量双向扫) seed=20261126: 独有丢失 0, 忠实度错误 0; 表格 10/10; Mermaid 4 图中 3 图缺 PDF "Randomization" 注释 (M-1) → **FAIL** (仅需 Mermaid 补注释, 正文无需动).

## attempt 2 (auditor; 对应 writer attempt 3 终态, 2026-11-26)

> 对象 md5: examples.md `a96c63b2822fe30b7621a293f40e2a15`, assumptions.md `ea6bd5233aff46ae8b3d99ce9fc8cbd4` (= reviewer attempt 3 终态签字值, 写报告前复核); scratch `…/scratchpad/t2_B-TA_auditor/a2/`

**结论: PASS** — M-1 已闭合.

1. **attempt 3 改动范围**: `git archive 466e0c3 knowledge_base/domains/TA | tar -x` + `patch -p1 < evidence/failures/t2_B-TA_attempt_2.patch` 重建 attempt 2 终态 (md5 a1a95b89… = 上轮审计值) → `diff` 对现文件: 40 行, 全为新增, 0 删除; 脚本判定 0 行落在 Mermaid 块外. 新增内容 = `rand["Randomization"]` ×17 (14 指 SE, 3 指 RE = Ex1 Run-In 末随机化) + `resp["Response Evaluation"] -.-> DB` ×3 (Ex3) + 对应 style 行. assumptions.md 未变.
2. **Mermaid 6 图 (seed 20261127 从 24 图抽: #2/#5/#9/#10/#18/#19) 对渲染逐节点/边/注释**:
| # | KB 行 | PDF 图 | 结果 |
|---|---|---|---|
| 2 | :55 | p388 Ex1 Prospective | 3 epoch/5 元素/3 arm 箭头 + Randomization 注释 (Run-In 末) ✓ |
| 5 | :173 | p389 Ex2 Study Schema | 3 路径 × 6 块顺序逐一一致 + "Randomization" 边 ✓ |
| 9 | :369 | p392 Ex3 Study Schema | Screen→Drug A/B→Open A/Rescue ×2, "Randomization" + "Response Evaluation" ✓ |
| 10 | :391 | p392 Ex3 Prospective | 3 epoch / 4 arm (A-Open/A-Rescue/B-Open/B-Rescue) + Randomization (Screen 末) + Response Evaluation (Double Blind 末) ✓ |
| 18 | :707 | p397 Ex5 Study Schema | Drug A/B/Rest/Follow, Randomization, Repeat 注, 两个 "3 weeks" 周期注 ✓ (repeat 边每 arm 一条, 同上轮 O-3, 不阻断) |
| 19 | :727 | p397 Ex5 Retrospective | "Drug A \| Rest" / "B \| Rest" + Repeat 注, Follow ×2, arm Drug A/Drug B, Randomization ✓ |
6/6 一致, 0 差异.
3. **fp 隔离** (HEAD + 仅 TA 两文件; `diff -rq` 仅 2 文件不同): `fp_match.py` before/after → regressions=1 仅 ig34_p0396_a009 (ATOM_ERR, 依据见上轮 §5), new_hits=42.
4. `python3 tools/check_links.py` → live docs 42 (≤42).
5. **G-TB8**: trace 185 writer a3 (`oh-my-claudecode:executor`) → 189 reviewer (`oh-my-claudecode:code-reviewer`) PASS + 签 md5 a96c63b2… (review.md:239-240); 现文件 md5 相同 → 签字后无改动; 无 `agent: main` 写 TA 记录; 规则 B 归档 `evidence/failures/t2_B-TA_attempt_2.{md,patch}` 在.
6. 上轮 prose 结论 (丢失 0 / 忠实 0, N=10 + R3 12) 不受影响: 本轮正文 0 改动.
