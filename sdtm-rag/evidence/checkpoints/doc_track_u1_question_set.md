# doc 轨 U1 收口 — doc 侧计分题集 + doc-only 上界基线

> 状态: **DONE (有条件)** · 日期 2026-08-12 · 单元 = `DOC_TRACK_KICKOFF.md` U1
> spec `docs/superpowers/specs/2026-08-11-doc-track-u1-doc-question-set-design.md`
> plan `docs/superpowers/plans/2026-08-11-doc-track-u1-doc-question-set.md`
> 数据红线: 题集 / 锚串 / 笔记 / 失败归档全在 `data/study/`(gitignored)。**本文件零真名零正文。**

## 0. 一句话

30 题 doc 侧计分题集建成并三方独立审过; **doc-only 上界实测 100.0%, 触发了 spec §7
第一条自毁条款, 用户当场裁定豁免并改用双尺子** —— 100% 作接线损耗参照, **k=5 的 88.33%
作判别力尺子**。题集**未重写**。

---

## 1. 题集事实 (独立复核, 与交接声称逐项相同)

| 项 | 值 |
|---|---|
| 计分题 | **30** |
| expected_facts | **79** 条 (raw 长度 12–82 字, 中位 33) |
| 章覆盖 | **17** |
| L6 探针 | 2 (`q41` / `q57`) |
| 配比 | `single_section 12 / cross_section 8 / part_family 5 / table 5` (与 spec §5 逐项一致) |
| fact 数分布 | `1:3 / 2:14 / 3:7 / 4:4 / 5:1 / 6:1` |
| gold 条目 / 落点 | **40 条, 落在 36 个不同 chunk = 全库 114 的 31.6%** |
| 多 gold 题 | 10 (走 `anchors` 逐 gold 锚串) |

## 2. 四道闸 — 真实题集上全绿, 退出码 0

```
docs_gold_gates : 30 题 0 finding · 闸 D 对 2/30 有约束力 · EXIT=0
lint_gold       : 0 条 gold 未唯一定位 · EXIT=0
gold_semantic_check           : 0 处触发 · EXIT=0
gold_semantic_check --selfsuff: 1 处 (q24, 已人工判为真跨节) / 10 道多 gold 题 · EXIT=0
pytest          : 1119 passed
```

**⚠ 引用这些绿灯时必须同写的三条口径边界**:
1. **闸 B 只挡字面**, 语义等价看不见 (本单元实测栽过一次: q46 四闸全绿而 gold 漏写真实存在)。
2. **闸 D 对 28/30 题不可触发**, 其绿灯**不可证伪** —— 是「未检验」不是「通过」。
   低约束力**不是闸设计坏**: PRT 与 EDC 两侧语域在流程/手续域结构性不相交。
3. **闸的单测全部是合成 fixture** (抽检方 B 实证: docs/cards/题集全 `tmp_path` 现造)
   ⇒ **`1119 passed` ≠ 这把尺子在真实题集上量对了**, 真实题集判定必须另跑上面四条命令取证。

---

## 3. Task 8 — doc-only 上界基线

### 3.1 数字

```
avg run1 = 1.0    avg run2 = 1.0    逐题差异 = NONE    n = 30    min per-q = 1.0
top_k = 15 (run_eval 默认; plan 命令未指定 --top-k)   collection = study_st01_docs (114 chunk)
```

⇒ **PASS 条件第 2 条 (同命令两次跑逐题相同) 满足。**

> **`--kb-root cards/` 不是混库**: `RAGEngine.__init__` 硬要求 kb_root 下有 `ROUTING.md` 与
> `INDEX.md` (docs/ 没有), 而 retrieval-only 下 kb_root **只进 system prompt 不参与检索**;
> hybrid 的 BM25 索引从 **collection 自身**建。
> (spec §6.1 要求这句原样进证据 —— 否则下一个人会读成混库。)

### 3.2 ⛔ 自毁条款第 1 条触发, 用户裁定豁免

| 条款 (spec §7, 先于数据写死) | 实测 | 结果 |
|---|---|---|
| 上界 **≥ 95%** ⇒ 题集退回重写 | **100.0%** | **触发** |
| 上界 ≤ 40% ⇒ 题集退回重写 | 100.0% | 未触发 |
| 闸 2 筛掉 > 出题总量 50% ⇒ 停下报告 | 三批 4.5% / 20% / 22.2% | 未触发 |

**阈值与判定规则自始至终未改。** 触发后当场停下上报, 用户 2026-08-12 裁定:
**豁免该条款 (理由: 它对 114 chunk 的小库不适用) + 改用双尺子**, 题集不重写。

**⚠ 引用纪律: 必须写成「触发了, 用户豁免」, 不得写成「四闸全绿一次过」或「未触发」。**

### 3.3 成因诊断 — 饱和是窗口/语料比, 不是题太简单

同命令只改 `--top-k`:

| top_k | source_recall_avg | 满分题 | 最低单题 |
|---|---|---|---|
| 3 | 0.8667 | 24/30 | 0.00 |
| 5 | **0.8833** | 25/30 | 0.00 |
| 8 | 1.0000 | 30/30 | 1.00 |
| 10 / 12 / **15 (基线)** | 1.0000 | 30/30 | 1.00 |

**饱和点 k≈8**。机制: 15 席 / 114 chunk = **捞走全库 13.2%**, 而每题 gold 仅 1–2 条
(分布 `{1条: 20题, 2条: 10题}`)。k=5 时 5 题非满分, 其中 **`q01`/`q43` 的 gold 完全不在 top-5**。

⇒ 按条款字面「退回重写加难」**大概率不会降低这个数字** —— 只要 gold 在库里, 15/114 的窗口
几乎必然捞到。**这是豁免的实证依据。**

### 3.4 排除的替代解释 (每条都实跑)

1. **不是口径过松的假 100%**: gold 走文件名子串匹配, 而 `lint_gold` 实测 **0 条未唯一定位**;
   `load_test_set` 对空 gold / 拼错 gold 键抛错。
2. **不是指标卡在 1.0**: 同一 harness 在 k=3/5 给出 0.8667 / 0.8833 (可证伪性成立)。
3. **两条独立路径对上**: harness 自报的 @3/@5 与从 `top5_sources` 自算的**逐位相同** (硬规矩 17b)。
4. **不是跑在坏基线上**: 开工自检 `1119 passed` / 四闸 EXIT 0 / git 树干净。

### 3.5 一条 spec 内部张力 (记录, 不裁量)

- §6.1: 上界的用途是「接线后 doc 侧分数应逼近它, **差额 = 接线损耗**」——
  为这个用途, 100% 反而是**最干净的**参照 (U2 的任何缺口都可归因到接线)。
- §7: ≥95% ⇒ 退回重写, 理由是「上界接近满分 ⇒ U2 分数分不清接线好还是题太简单」。

两条理由**指向相反动作**。本单元按 §7 字面触发并上报, 由用户裁定; 张力本身留档给 U2。

---

## 4. Task 9 — 三方独立核验 (规则 D)

隔离: 出题方 `general-purpose` / 审题方 `claude` / **抽检方 A `oh-my-claudecode:debugger`** /
**抽检方 B `oh-my-claudecode:test-engineer`** / controller, 五方不同 session。

### 4.1 Step 1 闸 D 实测复核 (N=6, 卡片库) — PASS

抽样规则**先写死**: 每类 qid 升序, 取 2 个的类取 `idx=⌊n/3⌋`/`⌊2n/3⌋`, 取 1 个的类取 `⌊n/2⌋`
⇒ `q05`/`q11`(single) · `q22`/`q26`(cross) · `q42`(part) · `q53`(table), 无一是本类首题。

在卡片库 `study_st01` 上 `--hybrid --study-lookup --judge`:
**judge fact-recall 0.0% (6/6), `judge_parse_ok=True` ×6, `judge_parse_failures=0`**
⇒ 卡片库确实答不出, **无题移出计分池, Task 8 基线不需重跑**。

**⚠ 按 plan 字面跑这道闸会是装饰品**: plan 判据是「答案里不含 `expected_facts`」, 而
`check_fact_recall` 是**裸子串** (`fact.lower() in answer.lower()`), 79 条 fact 全是 12–82 字整句
⇒ 子串几乎不可能命中, 判据**恒绿不可证伪**。故改用 `--judge`, 并补**双向可证伪性**:

- 负例: 卡片库答案 → judge **0.00 ×6**
- **阳性对照**: 喂「答案 = gold facts 原句拼接」→ judge **1.00 ×6 (PASS 6/6)**
- 检索非空转: 每题召回 5 张 form 级卡, top3 相似度 0.44–0.54, 主题相符

**⚠ 归因口径**: 「卡片答不出」对 PRT 流程题是**常态不是成就**, 本结果**不构成**「题出得好」的
证据, 也**不支持**任何关于检索质量的结论 (EDC 基于 PRT 但两者有非原则性出入)。

### 4.2 Step 2 抽检方 A — 三元组核验 (N=8) — **有条件 PASS**

哈希抽样 (seed 读数据前写死): `q01`/`q02`/`q16` · `q20`/`q26` · `q42`/`q43` · `q53`。
**24/24 项 (8 题 ×3 判据) 全 PASS, 0 FAIL。** 开工/收工 `docs/` sha256 **相同** ⇒ 产物目录全程未动。

A 自己抓到的一条判据问题: **plan Step 2 判据② 的字面写法「出现次数 == expected_sources 条数」
只适用于单 anchor 题**; 多 gold 题已于 commit `1626f83` 改判为逐 gold (期望次数是 **1 不是 2**)。
照字面读会把 `q20`/`q26` 误判成 FAIL。A 额外验了**配对顺序** (`anchors[i]` ↔ `expected_sources[i]`)
正确 —— 这一格纯计数口径查不到。

### 4.3 Step 2 抽检方 B — 四闸物理变异测试 — **0 个装饰闸, 但点名 2 条装饰输出**

变异手法: 函数体首行插入 `return []` (恒绿), 跑**全量**单测。已实证仓内无 ruff/flake8/py_compile
类测试 ⇒ 不可达代码不制造假阳性, 每条红都可归因到闸本身。

| 闸 | 函数 | 变异后 | 判定 |
|---|---|---|---|
| A | `gate_gold_unique` | 4 failed / 1115 passed | 非装饰品 |
| B | `gate_anchor_unique` | **19 failed** / 1100 passed | 非装饰品 |
| C | `gate_fact_length` | 7 failed / 1112 passed | 非装饰品 |
| D | `gate_card_unanswerable` | 8 failed / 1111 passed | 非装饰品 |

闸 B 的红名单里**包含复审文档列的四条 fail-open 回归**(OR-only+捏造锚串 / 完全无 gold /
锚串错位 / 多 gold 半数错位) ⇒ 那四条不是注释声明, 是可执行断言。

🔴 **点名: `gold_semantic_check` 的两条可见性输出零断言** —— `[selfcov]` 逐 gold 逐 fact 分数行
与 selfsuff 末尾汇总行, 删掉后**全套 `1119 passed` 一条不红**。而同仓同设计意图的闸 D `[probe]`
行**是被钉住的** (`test_main_prints_probe_binding_visibility`) ⇒ **照抄了设计没照抄断言, 是漏做不是口径分歧。**

### 4.4 Step 3 controller 非自洽复算 (硬规矩 17b)

复算路径**刻意不同**: A 逐页 `pdftotext -f N -l N` + 自建扫描; controller **整本抽取一次**按 `\f`
分页 + `str.count`; 抽样规则按 A 报告文字**重新实现**而非复用其脚本。

| A 的关键数字 | 复算 |
|---|---|
| 抽中 8 题 | **逐 qid 相同** ⇒ 未挑题 |
| 10 条锚串的 PDF 命中页 | **逐条相同** |
| ③ 页覆盖 10/10 | **10/10 复现** |
| L3: `q20` anchor[0] 去空白口径下多命中目次 p4 | **复现成立** (exact=[81], nospace=[4,81]) |
| 「21 条 fact 中 9 条非逐字」 | **口径差**: 去空白=9 (同 A) / raw=16 |

对 B 的复算 (变异手法不同: sed 删整行 vs `_ = shown`):
`[selfcov]` 行删掉 → **1119 passed** (装饰确认) · `[probe]` 行删掉 → **2 failed** (对照成立)。

**全池扩测** (超出 plan 要求的 N=8):

| 判据 | A 覆盖 | controller 全池 |
|---|---|---|
| ① 锚串在 PDF 逐字存在 | 8 题 | **40/40 条锚串, 0 缺失** |
| ② 锚串唯一定位 | 8 题 | **30/30 题** (`grep -F` 路径) |
| ③ gold 页区间覆盖锚串页 | 10 条 | **40/40 条, 0 FAIL** |
| 口径脆弱 (exact 唯一但去空白不唯一) | q20[0] | **全池仅 q20[0] 一条** |

⚠ **A 的条件 C1 (「仅覆盖 8/30 不外推」) 由此解除, 但解除它的是 controller 侧全池复算
(不同代码路径, 判据是机械的), 不是第二次独立抽检。不得写成「两方独立验过全池」。**

### 4.5 本单元当场修掉的缺陷

按硬规矩 18, 给 `test_main_selfsuff_mode_exits_zero_with_findings` 补两条**整句带数值**断言
(不写 `"1 处" in out` —— 它是 `"11 处"` 的子串, 那样只证明"打了"不证明"打对了")。

**变异复验: 两条变异现在都变红** (删 `[selfcov]` 行 → 1 failed; 汇总行去掉数字 → 1 failed),
还原后 `1119 passed`。测试总数不变 (加断言不加用例)。

---

## 5. 已知限制 (每条注明**它看不见什么**)

**量具类**
1. **闸 B 只挡字面** —— 看不见语义等价的表述。本单元实测栽过一次 (q46)。
2. **闸 D 对 28/30 题不可触发** —— 绿灯不可证伪, 是「未检验」不是「通过」。
3. **闸的单测全是合成 fixture** —— 看不见真实 114 chunk 的 `match_names` 子串歧义、真实 959 张卡的
   日文分词/大小写行为、真实 YAML 形状 (块标量尾换行/全角空格)。
4. **变异粒度只到函数级** —— 看不见「闸内某个分支守卫失效而其他分支照报」。
5. **变异只证「闸非恒绿」, 未证「闸口径正确」** —— 看不见闸与测试**一起**写错 (两边同错则同绿)。
6. **闸 C 零余量且口径脆弱** —— 全池最短 fact raw 恰好 **12 = 阈值**, 而它含 2 个空白字符:
   闸 C 量的是 raw `len()`, **若哪天改成去空白口径, 这条 fact 变 10 < 12 直接变红**。
7. **`--mode selfsuff` 不在默认输出里** —— 跑默认命令看不到单 gold 自足性。

**题集类**

8. **逐 gold 锚串证明「答案分布在这几块」, 不证明「这几块之外没有答案」。**
9. **part 家族 5 题的来源隔离不适用** (用户裁定接受) —— 不能用于论证题集与切分器无共谋。
10. **③ 页覆盖是必要非充分** —— 页区间在节/part 边界重叠 (实测每个 gold 的页区间平均被另外
    2–5 个 chunk 触及), 看不见「页码对但归属错」。
11. **同页多 gold 时 ③ 零判别力** —— 如 `q26` 两个 gold 都是 p100-100, 它的 PASS 是「没矛盾」不是「有证据」。
12. **`q20` anchor[0] 的唯一性依赖两个前提**: 目次页不在语料内 + exact 空白口径。
    若目次日后进语料或改用去空白口径, 该锚串不再唯一 (全池仅此一条)。
13. **抽中的 2 道 part_family 都不是切点探针** —— 看不见 part 家族最该考的「切点两侧串味」。
14. **L6 探针 n=2 且供给已尽** —— 全语料 113 切点全覆盖勘察判定可探针**仅 1 个**。
    `q57` 的判定是**生成侧**实测 (n=18, 单模型单温度), **不是检索侧**; 换模型或修剪切口**可能翻转**。
15. **`s10_3` 两个表体在 PDF 文本层就已丢失** (非切分器) ⇒ 该主题**无 gold 可依, 不得出题**。
16. **3 题只有 1 条 fact** (`q04`/`q42`/`q51`) ⇒ fact-recall 退化成 0/1 二值。
17. **`q57` 的 `anchors[0]` 含定长空格串** ⇒ 换 poppler 版本重抽语料会被闸 B 误报成假红。
18. **未验证 chunk 正文整体忠实于 PDF** —— 锚串只锚了每块的一小段 (如 `q43` 的 gold 有 22404 字,
    锚串 50 字), 未被锚覆盖的部分是否漏字/串页, 本轨手段看不见 (C1 L9 盲点)。
19. **两套 PDF 抽取口径同源 poppler** —— 看不见 poppler 与 PDF 字形层的差异 (连字/异体字/CID),
    不构成独立信源。

**基线类**

20. **上界 100% 是 k=15 下的饱和值** —— 看不见 k<8 时的判别力差异, 故并列保留 **k=5 = 88.33%**。
21. **`source_recall` 量的是 gold 召回不是答案质量** —— 看不见 doc chunk 进 context 后
    答案是否变好/变差, 也看不见对卡片题的席位挤占。
22. **plan 的判据文字落后于闸的实现口径** (判据② 用的是已被废弃的数量口径) —— 照抄 plan 会产生假阳性。

---

## 6. 本单元**不能**证明什么

- 不能证明 doc chunk 接线后检索得到 —— **U1 全程是 doc-only 隔离库**, 没碰联邦/挤占。
- 不能证明题集对 U2 有判别力 —— 判别力只在 k≤5 的诊断档实测过, 生产档 k=15 已饱和。
- 不能证明「卡片答不出」= C1 的价值假设成立 —— 那是**领域论据不是实证** (实证等 U2),
  且**不许**与低污染率那个测量合并引用 (后者对 C1 零信息量)。
- 不能证明 chunk 正文忠实于 PDF (限制 18)。
- 不能证明未来加页/换 poppler 后锚串仍唯一 (限制 12/17)。

---

## 7. 复跑命令 (逐字)

```bash
cd sdtm-rag
# 四闸 + 全量测试
P=data/study/st01/eval/test_set_docs_v1.yml
./.venv/bin/python -m eval.docs_gold_gates $P --docs-dir data/study/st01/docs --cards-dir data/study/st01/cards
./.venv/bin/python -m eval.lint_gold $P --docs-dir data/study/st01/docs
./.venv/bin/python -m eval.gold_semantic_check $P --docs-dir data/study/st01/docs
./.venv/bin/python -m eval.gold_semantic_check $P --docs-dir data/study/st01/docs --mode selfsuff
./.venv/bin/python -m pytest -p no:warnings --tb=short     # 1119 passed
#   ⚠ 勿加 -q: pyproject addopts 已含 "-ra -q", 再加变 -qq 会关掉汇总行
#   ⚠ 取退出码别接管道: `cmd | tail` 后的 $? 是 tail 的

# 上界基线 (两遍)
./.venv/bin/python -m eval.run_eval $P --retrieval-only --hybrid \
  --collection study_st01_docs --kb-root data/study/st01/cards \
  --output data/study/st01/eval/runs/docs_v1_upper_bound.json
# k 曲线 (诊断档)
for K in 3 5 8 10 12; do ./.venv/bin/python -m eval.run_eval $P --retrieval-only --hybrid \
  --top-k $K --collection study_st01_docs --kb-root data/study/st01/cards \
  --output data/study/st01/eval/runs/docs_v1_kcurve_k$K.json; done

# 产物目录未被动过
find data/study/st01/docs -name '*.md' | sort | xargs shasum -a 256 | shasum -a 256
#   -> 0f13797f1871a3ddbab9b4741560e6a38451fce9e0ebebacbdac69e7d4f78dfd
```

抽检方原始报告: `evidence/step_u1_audit.md` (A) · `evidence/step_u1_audit_mutation.md` (B)。
自毁条款触发归档 (规则 B, 进 git): `evidence/failures/u1_task8_upper_bound_selfdestruct.md`
—— 含触发时的完整现场、用户裁定原文、k 曲线与全池复算表。
被否的候选题归档仍在 `data/study/st01/eval/failures/`(gitignored, 含锚串)。

---

## 8. 给 U2 的硬约束

1. **两把尺子都要报**: 生产档 k=15 (上界 100%, 量接线损耗) + 诊断档 k=5 (88.33%, 量判别力)。
   只报前者会看不出接线好坏, 只报后者会与 spec §6.1 的口径断裂。
2. **必须跑 `--judge`** —— 裸子串对 12–82 字整句 fact 得到接近零的 fact-recall,
   **与检索质量无关**。本单元实测 21 条 fact 里 **7 条只差空白**。
3. **失分不得默认归因到检索质量** —— 先分清「PRT 有而 EDC 结构上就没有」与「检索没找到」。
4. **接线后的硬验收照 kickoff 不变**: 卡片侧 48 题逐题 Δ0 + doc 侧判别力反事实 + 答题侧不变差。
5. **写「实测」必附可复跑命令** —— 上一轮 6 例假实测全部由复现驳回抓出、无一次自查发现。
6. **数字对不上先查口径** —— 本单元三次数字分歧 (fact 最长 82/78 · q40 锚串计数 · fact 逐字 16/9)
   **全部是口径差不是缺陷**。
