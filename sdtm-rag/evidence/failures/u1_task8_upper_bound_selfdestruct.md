# Task 8 失败归档 — 自毁条款第 1 条 (上界 ≥ 95%) 已触发

> 日期: 2026-08-12 · 归档人: U1 续跑 session (controller)
> 规则 B: 本文件只记录, **不删任何产物**。题集 `test_set_docs_v1.yml` 原样未动。

## 1. 输入

- 题集: `data/study/st01/eval/test_set_docs_v1.yml` (30 计分题, commit `beb534d` 后未改)
- collection: `study_st01_docs` (114 chunk, 实测 `chromadb.PersistentClient('data/chroma').list_collections()`)
- 开工自检五条**全绿** (见 §5), 即本次测量不是跑在坏基线上

## 2. 产物

| 文件 | 内容 |
|---|---|
| `runs/docs_v1_upper_bound.json` | 第一遍 (plan §Task 8 Step 1 逐字命令) |
| `runs/docs_v1_upper_bound_rerun.json` | 第二遍 (同命令) |
| `runs/docs_v1_kcurve_k{3,5,8,10,12}.json` | **补充诊断**, 非基线 (见 §4) |

## 3. 技术判定

```
avg run1 = 1.0        avg run2 = 1.0        逐题差异 = NONE
n = 30                min per-q recall = 1.0
top_k = 15 (run_eval 默认, plan 命令未指定 --top-k)
```

- **PASS 条件第 2 条 (可复现) 满足**: 两遍逐题相同。
- **自毁条款第 1 条触发**: 上界 100.0% ≥ 95%。阈值**未改**, 判定规则**未改**。

## 4. 成因诊断 (补充证据, 不改变上面的判定)

k 曲线 (同命令只改 `--top-k`):

| top_k | source_recall_avg | 满分题 | 最低单题 |
|---|---|---|---|
| 3 | 0.8667 | 24/30 | 0.00 |
| 5 | 0.8833 | 25/30 | 0.00 |
| 8 | **1.0000** | 30/30 | 1.00 |
| 10 | 1.0000 | 30/30 | 1.00 |
| 12 | 1.0000 | 30/30 | 1.00 |
| **15 (基线)** | **1.0000** | 30/30 | 1.00 |

**饱和点 = k≈8**。机制: 15 席 / 114 chunk = **捞走全库 13.2%**, 而每题 gold 只有 1–2 条
(实测分布 `{1 条: 20 题, 2 条: 10 题}`, 共 40 条 gold)。

**题集在小 k 下仍有判别力** —— k=5 时 5 题非满分, 其中两题 gold **完全不在 top-5**:
`q01` (single_section) r@5=0.00 · `q43` (part_family) r@5=0.00 ·
`q25` / `q41` / `q57` r@5=0.50。

⇒ **100% 是「窗口相对语料太宽」而不是「题太简单」**。按字面执行「题集退回重写加难」
**很可能不会让这个数字下降** —— 只要 gold 在库里, 15/114 的窗口就几乎必然捞到。

## 5. 排除的替代解释 (每条都实跑过)

1. **不是口径过松的假 100%**: gold 是文件名子串匹配, 而 `lint_gold` 实测 **0 条 gold 未唯一定位**;
   `load_test_set` 会对空 gold / 拼错键抛错。
2. **不是指标卡在 1.0**: 同一 harness 在 k=3/5 给出 0.8667 / 0.8833 (可证伪性成立)。
3. **两条独立路径对上**: harness 自报的 @3/@5 与我从 `top5_sources` 自算的逐位相同
   (0.8667 / 0.8833) —— 非自洽写法复算 (硬规矩 17b)。
4. **不是跑在坏基线上**: 开工自检 `pytest 1119 passed` / 四闸 EXIT 均 0 / git 树干净。

## 6. 一条 spec 内部张力 (交给用户, 不自行裁量)

- §6.1 说上界的用途是「接线后 doc 侧分数应逼近它, **差额 = 接线损耗**」——
  为这个用途, 上界 100% 反而是**最干净的**参照 (U2 的任何缺口都可归因到接线)。
- §7 说 ≥95% ⇒ 退回重写, 理由是「上界接近满分 ⇒ U2 分数分不清接线好还是题太简单」。

两条理由指向相反动作。**§7 是写死的条款, 已按字面触发并上报**; 本节只陈述张力, 不作裁量。

## 7. 用户裁定 (2026-08-12, 本 session 当场上报后取得)

**裁定 = (C) 豁免条款 + 双尺子。** 具体:

- 该条款对「114 chunk 的小库」**不适用**, 用户签字豁免, 须写进 Task 10 收口证据
- **100% 保留为 §6.1 的接线损耗参照上界** (U2 的任何缺口都可归因到接线)
- **k=5 的 88.33% 正式记为判别力尺子** —— 给 U2 一把有余量的第二把尺
- 题集**不重写**, 继续 Task 9

未采纳: (A) 按字面退回重写 (§4 显示大概率无效) · (B) 事后把上界口径改成 k=5。
**阈值与判定规则自始至终未改**; 本次是**豁免**, 不是"没触发"。引用时必须写成
「触发了, 用户豁免」而不是「四闸全绿一次过」。

## 7b. Task 9 Step 1 结果 (闸 D 实测复核) — PASS

分层抽 N=6, 抽样规则**先写死**: 每类 qid 升序, 取 2 个的类取 `idx=⌊n/3⌋` 与 `⌊2n/3⌋`,
取 1 个的类取 `⌊n/2⌋` ⇒ `q05`/`q11` (single) · `q22`/`q26` (cross) · `q42` (part) · `q53` (table)。
无一是本类首题。

在**卡片库** (`study_st01`, 959 chunk) 上 `--hybrid --study-lookup --judge --full-answers`:

| 指标 | 值 |
|---|---|
| judge fact-recall | **0.0% (6/6 题)**, `judge_parse_ok=True` ×6, `judge_parse_failures=0` |
| 子串 fact-recall | 0.0% (无信息量, 见下) |
| 检索是否空转 | **否** — 每题召回 5 张 form 级卡, top3 相似度 0.44–0.54, 主题相符 |

⇒ 卡片库确实答不出, **无题需移出计分池, Task 8 基线不需重跑**。

**⚠ 这道闸按 plan 字面跑会是装饰品**: plan 的判据是「答案里不含 `expected_facts`」, 而
`check_fact_recall` 是**裸子串** (`fact.lower() in answer.lower()`), 全池 79 条 fact 实测
**12–82 字、中位 33 字**的整句 ⇒ 子串几乎不可能命中, 判据**恒绿不可证伪**。
故本次改用 `--judge` 语义判官, 并补**双向可证伪性**:

- 负例: 卡片库答案 → judge 0.00 ×6
- **阳性对照**: 喂「答案 = gold facts 原句拼接」→ judge **1.00 ×6 (PASS 6/6)**
  复跑: `./.venv/bin/python <scratchpad>/judge_positive_control.py` (脚本已留)

**⚠ 归因口径 (交接 §4, 引用本结果时必须同写)**: 「卡片答不出」对 PRT 流程题是**常态不是成就**,
本结果**不构成**「题出得好」的证据, 也**不支持**任何关于检索质量的结论。

## 7d. Controller 独立复算 (Step 3 前置, 非自洽路径) — 全 30 题, 不止抽样的 8 题

用 `grep -Flr -f <锚串文件>` (完全不走 Python 扫描, 与抽检方 A 的自建实现互为独立路径)
把判据② 在**全池 30 题 / 40 条锚串**上算了一遍:

- **单锚串题 (20 题): 命中文件数恒 = 1 = gold 数, MISMATCH 0**
- **多锚串题 (10 题): 每条 anchor 各命中 1 个文件, 2 锚对 2 gold** —— 与「逐 gold 锚串」设计一致
- 复跑: `<scratchpad>/anchor_count_by_grep.sh` (脚本已留)

**⚠ 抓到一条会翻转判定的口径差**: `docs_v1_q40` 的锚串在**同一个 chunk 内出现 2 次**
⇒ 命中文件数 = 1 (判 OK), 总出现次数 = 2 (判 MISMATCH)。

查实: **闸 B (`gate_anchor_unique`) 的口径是 membership 不是数量**, docstring 明确写了
旧数量口径的四条 fail-open。所以 q40 **不是缺陷**, 闸 B 判它绿是对的。

**但 plan Task 9 Step 2 判据② 的字面写法「anchor 出现次数 == expected_sources 数」
正是那个被废弃的旧口径** —— 照字面实现会把 q40 报成假阳性。
⇒ 这条要写进 Task 10 的已知限制: **plan 的判据文字落后于闸的实现口径, 未同步。**

## 7e. Task 9 Step 3 — 非自洽复算抽检方 A 的关键数字 (硬规矩 17b)

复算路径与 A **刻意不同**: A 逐页 `pdftotext -f N -l N` + 自建扫描函数; 我**整本抽取一次**
再按 `\f` 分页 + `str.count`/`in`; 抽样规则按 A 报告的文字**重新实现**而非复用其脚本。

| A 的关键数字 | 复算结果 |
|---|---|
| 抽中 8 题 (哈希抽样) | **逐 qid 相同** ⇒ 未挑题 |
| 10 条锚串的 PDF 命中页 | **逐条相同** (24/24/58/81/86/100/100/75/106/33) |
| ③ 页覆盖 10/10 | **10/10 复现** |
| L3: q20 anchor[0] 去空白口径下多命中目次 p4 | **复现成立** (exact=[81], nospace=[4,81]) |
| 「21 条 fact 中 9 条非逐字」 | **口径差**: 去空白=9 (同 A) / raw=16 (我的初值) |

**第三次「数字分歧实为口径差」** (前两次: fact 最长 82 raw vs 78 去空白; q40 锚串计数)。
含义反而更硬: 21 条里 **7 条只差空白** ⇒ 与 `-layout` 数字-单位空格是同一现象,
**加强**了 A「是改述不是杜撰」的结论, 也再次说明**跑分必须开 `--judge`**。

### 全池扩测 (超出 plan 要求, 用于解除 A 的 C1)

| 判据 | A 的覆盖 | Controller 全池复算 |
|---|---|---|
| ① 锚串在 PDF 逐字存在 | 8 题 | **40/40 条锚串, 0 缺失** |
| ② 锚串唯一定位 | 8 题 | **30/30 题** (`grep -F` 路径) |
| ③ gold 页区间覆盖锚串页 | 10 条 | **40/40 条, 0 FAIL** |
| 口径脆弱性 (exact 唯一但去空白不唯一) | q20[0] | **全池仅 q20[0] 一条** |

⚠ **写法纪律**: A 的条件 C1 (「仅覆盖 8/30 不外推」) 由此解除, 但解除它的是
**controller 侧的全池复算 (不同代码路径, 判据是机械的)**, **不是第二次独立抽检**。
引用时不得写成「两方独立验过全池」。

## 7c. 下一 attempt 的输入 (若将来仍要重写题集)

- 按 §4, 单纯"把题出难"不会降低 k=15 的上界; 要动的是**窗口/语料比**或**改用 rank 指标**
- k=5 的 5 道非满分题 (`q01`/`q43` gold 完全不在 top-5, `q25`/`q41`/`q57` 各中一半)
  是现成的判别力样本, 重写时应保住这类题

## 8. 复跑命令 (逐字)

```bash
cd sdtm-rag
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
  --retrieval-only --hybrid \
  --collection study_st01_docs --kb-root data/study/st01/cards \
  --output data/study/st01/eval/runs/docs_v1_upper_bound.json
# k 曲线
for K in 3 5 8 10 12; do .venv/bin/python -m eval.run_eval \
  data/study/st01/eval/test_set_docs_v1.yml --retrieval-only --hybrid --top-k $K \
  --collection study_st01_docs --kb-root data/study/st01/cards \
  --output data/study/st01/eval/runs/docs_v1_kcurve_k$K.json; done
```

> `--kb-root cards/` **不是混库**: `RAGEngine.__init__` 硬要求 kb_root 下有 `ROUTING.md` 与
> `INDEX.md` (docs/ 没有), 而 retrieval-only 下 kb_root **只进 system prompt 不参与检索**;
> hybrid 的 BM25 索引从 **collection 自身**建。
