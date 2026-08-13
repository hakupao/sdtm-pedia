# doc 轨 U3 设计 — 判库侧收口 (判库欠账 + `both` 档)

> 日期: 2026-08-13 · 单元 = `milestones/07_rag_kg/DOC_TRACK_KICKOFF.md` §0′ 候选 #1 + #3
> 前置: U2 DONE (`sdtm-rag/evidence/checkpoints/doc_track_u2_wirein.md`)
> 数据红线: **本文件零真名零正文**。手順書型题目 / 逐题明细一律落 `data/study/`(gitignored)。

## 0. 一句话

生产档 90.00% 里丢掉的 **10.00pt 全部是判库损耗**(3/30 道 doc 题被 router 判去 cdisc,
压根没到 study 引擎)。本单元先给 `both` 档建确定性尺子、把路由 gold 扩到手順書型,
再改 `_ROUTER_SYSTEM` 规则 2 一处 —— **顺序是硬的,尺子先于修法**。

## 1. 现状与根因

### 1.1 判库欠账 (kickoff #1)

U2 实测: 尺子③ (`corpus=auto`, N=8) 的非满分题恰好是 `docs_v1_q15` / `q17` / `q53`,
与 router 判到 cdisc 的名单逐题对上,**无残差**。这三题不是检索失败 —— 它们没到 study 引擎。

根因在 `server/federation.py:_ROUTER_SYSTEM`,两处叠加:

1. **规则 1 的排除条款主动收走它们** —— 原文写着「merely naming a clinical concept the
   standard happens to cover (**adverse events**, severity grading, lab results, dosing) does
   not [make it study]」。三题里有一道题面首词即 adverse-event 概念。
2. **规则 2 没有通向手順書的路** —— 语料描述里写了 study 含 "protocol / procedure document
   sections",但规则 2 的**可操作触发词全是 EDC 词汇**(項目 / フォーム / 画面 / 選択肢 /
   単位)。手順書内容(分類体系 / 判定基準 / 定義)在规则 2 里**没有任何触发条件**。

三题的形态(按 U1 的 category): `single_section` ×2 + `table` ×1;三题的 U1 note 均已记录
**反向查卡命中为 0**(卡片库结构上答不出) ⇒ 正解一律 `study`。

### 1.2 路由闸对这个失败形态结构上失明

`eval/run_routing_eval.py:load_gold()` 的 181 题 gold 只有三个来源:

| 来源 | n | gold |
|---|---|---|
| `eval/test_set_v3.yml` | 140 | cdisc |
| `data/study/st01/eval/test_set_study_v1_1.yml` | 25 | study (**全是卡片题**) |
| `eval/routing_gold_ja_supplement.yml` | 16 | cdisc 11 / both 5 |

合计 gold 分布 cdisc **151** / study **25** / both **5**(`load_gold()` 实测,复跑见 §10)。

**零道 doc 题**。硬规矩 19 的形态复发: 闸绿 ≠ 内容都在 —— 本单元要修的错,现有闸看不见。

### 1.3 `both` 档全程未测 (kickoff #3)

`u2_ruler3_prod.json` 记 `routing: {study: 27, cdisc: 3}` ⇒ **doc 题从未触发过 `both`**,
现有 30 题长不出 `both` 的尺子。

而 `both` 与本单元直接耦合: `_ROUTER_SYSTEM` 自己写着 "answer both in every remaining case",
且 `score_run` 里 **`both` 判错不算 fatal、只掉 exact** ⇒ 放宽规则 2 之后一部分题很可能落到
`both` 而非 `study`,那时验收就直接依赖 `both` 的行为。

`both` 下的实际席位(读 `federation.py:129` + `study_corpus.py:46` 得到,**尚未实测**):

```
k_each = ceil(15/2) = 8
  cdisc  8
  study  StudyCorpusEngine.retrieve(top_k=8) → cards 8 (从 15 减半) + docs 8 (未减半)
总计 24 席; doc 在 study 半边的占比 8/23 = 35% → 8/16 = 50%
```

这个不对称**不是谁裁定的**,是 `doc_seats` 写成引擎属性而非 k 的比例掉出来的。

## 2. 单元边界

**做**

1. `both` 档确定性尺子(只量不改)
2. 路由 gold 扩到手順書型(新文件 + 出题)
3. `_ROUTER_SYSTEM` 规则 2 增补一处触发条件

**不做**(每条注明理由)

| 不做 | 理由 |
|---|---|
| 席位不对称的修改 | 改它需要自己的判据,而判据只能来自本单元量出来的数字 |
| 答题侧测量 | U2 §5-2 实测答题侧全距 6.25pt,本类差异大概率落噪声里(#4 仪器未做) |
| 检索侧代码 / `study_lookup` / `StudyCorpusEngine` | 本单元自变量只有 router prompt |
| 给 router prompt 加开关 | YAGNI;回滚手段 = git revert,闸在合并前跑 |

## 3. 顺序 (硬的)

```
T1 both 尺子 (零 LLM)
T2 扩 gold + 出题 (规则 D 隔离)
T3 冻结改动前基线  ← 不可省
T4 改 prompt (只看 dev)
T5 验收 (held-out + 旧 181 子集 + 终审三题)
T6 三方核验 (规则 D)
T7 收口
```

**T3 为什么不能省**: 加 72 道题后 `exact_acc` 的分母从 181 变成 253,
**历史的 179/181 与新闸不可比**(本仓已吃过多次「换尺子当成回归」的亏)。
故闸内保留两个口径:

- **旧 181 子集** —— 与历史可比,回归条款 1 只看它
- **全 253 题** —— 新基线,本单元建立

## 4. `both` 尺子 (T1, 只量不改)

`eval/run_eval.py:739` 已支持 `--corpus both`,**不需要新代码,只需要跑**。

| 档 | 题集 | 口径 | 参照物 |
|---|---|---|---|
| B1 | doc 30 题 | `--corpus both --study-docs` | U1 k=8 的 1.0000 |
| B2 | cards 48 题 | `--corpus both --study-docs` | study 档的 0.8750 |
| B3 | doc 30 题 | `--corpus study --study-docs --doc-seats 8` | 隔离「cards 减半」的效应 |

**每档连跑 3 遍**(U2 §5-1: 检索非确定性源在 embedding API,固定向量下检索完全确定
⇒ 任何「逐题 Δ0」必须三遍)。三遍不一致的题必须逐题点名。

预期 B2 会低于 0.8750(cards 15 席 → 8 席)。**掉多少是本环唯一要产出的数字**;
席位不对称写进已知限制,本单元不动。

## 5. 路由 gold 扩充 (T2)

### 5.1 文件位置与红线

新文件 `data/study/st01/eval/routing_gold_docs.yml`,**必须 gitignored**。

理由: `eval/routing_gold_ja_supplement.yml` 是 **git 跟踪的**(已用 `git ls-files` 确认),
它能进 git 是因为其内容一律用「この項目」「このフォーム」这类通用指代、不含任何真实
study 内容。手順書型题目做不到这一点,故只能落 `data/study/`(`.gitignore:10` 覆盖)。

**§5.2 的 42 道新题全部落这一个文件,包括 cdisc 干扰题与 both 题** —— 虽然后两组原则上
不含 study 内容、理论上可进 tracked 的 `ja_supplement`,但它们是**照着手順書题的近似形态**
写出来的,难保不回声具体临床概念;且 dev/held-out 划分放在一个文件里才不会漂移。
代价是这 18 题的题面不进 git 无法被后人直接复审 —— **补偿手段**: 文件头前置声明
(形态 / 计数 / 出题依据,零题面)**原样抄进收口证据**,使设计可复审、内容仍不入库。

`run_routing_eval.py` 加第 4 个 gold 来源,**复用 `load_supplement` 的严格校验**
(缺文件 raise / 空文件 raise —— 悄悄少几题 = 闸口变松却无人察觉)。

### 5.2 题量与配比

| 组 | n | gold | 来源 |
|---|---|---|---|
| U1 doc 题 | 30 | **一律 study** | 已有 `test_set_docs_v1.yml` |
| 新写 手順書型 | 24 | study | 114 chunk 按 17 章分层抽,与 U1 30 题**不重叠** |
| 新写 近似干扰 | 12 | cdisc | 「听起来像临床规约但问的是标准」 |
| 新写 真两可 | 6 | both | 补 `ja_supplement` 文件头自认的空白(**无标准侧显式标记**的真两可形态) |

**U1 30 题一律 study,不做逐题裁定** —— 手順書内容 CDISC 结构上答不了,统一标签消掉一个
作弊面(逐题裁定意味着标签可以被结果反向塑造)。

### 5.3 出题纪律 (规则 D 延伸到出题环)

1. 出题 subagent **不告知** `q15`/`q17`/`q53` 是哪三道,**也不告知它们的题型** ——
   否则会下意识出成同一形状,held-out 当场失效。
2. **不许先探路由器判什么再照着写**(抄 `ja_supplement` 文件头已有的这条纪律:
   "两组出题均在接触路由器之前完成 —— 未先探路由器对什么措辞判对再照着写,
   那等于给规则送分")。
3. 出题依据写进文件头**前置声明**,含形态覆盖的诚实说明(抄 `ja_supplement` 的
   「审阅 I-2 修正」写法: 明写本文件**没**覆盖什么)。
4. **dev / held-out 的划分由出题方之外的人做**,且用**确定性规则**而非挑选
   —— 挑选就是 cherry-pick。规则写死为: 24 道手順書型题**按所属章节号升序排序
   (同章内按 id 升序),取偶数位为 dev、奇数位为 held-out**。该规则保证恰好 12/12
   且跨章分布对称;「按章号奇偶」做不到这一点(17 章分布不均,会给出不等的两半)。

### 5.4 已有的天然哨兵

`ja_supplement` 里 `ja_supp_01`(有害事象はどのドメイン)与 `ja_supp_09`
(severity と seriousness)是 AE 味的 cdisc-gold 题,**正落在放宽规则 2 的误伤区**;
其文件头还自标 `ja_supp_04` / `ja_supp_07` 为「本文件两道最脆的题」。
本单元不新增哨兵,直接靠它们惩罚过宽。

## 6. 修法 (T4) 与三道反对症下药防线

### 6.1 改动面

**只改 `server/federation.py` 的 `_ROUTER_SYSTEM` 规则 2 一处**:补上「本研究自身の
手順・計画文書に定義された分類体系 / 判定基準 / 定義」这一**类**的触发条件。

写成 **pattern 不写成 example**: 规则文本里**不得**出现来自 held-out 三题的任何具体
临床概念(解剖学部位名 / 特定评价体系名 / 特定测量阈值)。

### 6.2 三道防线

| # | 防线 | 挡住什么 |
|---|---|---|
| 1 | **gold 先于 prompt** —— T3 在改动前跑完并落盘 | 基线被事后重定义 |
| 2 | **held-out 12 题 + `q15`/`q17`/`q53` 全程封存**,改 prompt 时只看 dev 12 题 | 对着具体反例调措辞 |
| 3 | **旧 181 子集不许退化** —— **151** 道 cdisc-gold 题 | 规则放得过宽 |

旧 181 子集的 gold 分布(`load_gold()` 实测,复跑见 §10): cdisc **151** / study **25** / both **5**。

### 6.3 必须点名的风险

`_ROUTER_SYSTEM` 是**模块常量,没有开关**。改了就是生产改了,回滚手段只有 `git revert`。
本单元不加开关(YAGNI),但**闸必须在合并前跑**。

## 7. 判据与自毁条款 (先于数据写死,阈值不许事后改)

**准确率口径(全表统一)**: `pred == gold` 的精确匹配,即 `score_run` 的 `exact`;
判成 `both` 而 gold 是 `study` **算错**(虽然它在 fatal 口径下是安全的)。

| # | 条款 | 触发后果 |
|---|---|---|
| 1 | 三遍**每一遍** fatal=0(口径见下)且**旧 181 子集** exact ≥ **178** | 修法退回。**不许改 `EXACT_THRESHOLD` / 不许改 `score_run` 的 fatal 定义 / 不许从 gold 删题** |
| 2 | held-out 手順書题准确率 ≥ dev 手順書题准确率 − **25.0pt**(各 n=12,25pt = 3 题) | 判定为对 dev 拟合 ⇒ prompt **退回重写,且须换新题重测** |
| 3 | dev 手順書题准确率 ≥ **10/12** | 规则没写对,**不许上生产** |
| 4 | 新写 cdisc 干扰题较改动前下降 **≤ 1 题** | 规则过宽,退回 |
| 5 | **`q15`/`q17`/`q53` 只报告不作 PASS 条件** | 看到结果后**不许再回头改 prompt**;仍错则记为已知限制,**不重跑** |
| 6 | 所有跑批**连跑 3 遍**,三遍不一致的题必须点名 | 只报一遍的数 = 伪造确定性 |

**条款 1 的 fatal 口径 = 全 253 题 减去 `final` 组(`q15`/`q17`/`q53`)** ——
这三题的 gold 是 `study`,判去 cdisc 按 `score_run` 就是 fatal;若把它们算进条款 1,
条款 1 与条款 5(只报告不作判据)会互相打架。**分组口径写死在这里,不许实施时再议。**
其余 250 题(旧 181 + U1 其余 27 + 新写 42)一律计入 fatal。

**条款 1 的 178 从哪来**: U2 收口实测三遍稳定 179/181,留 1 题噪声余量。
下调阈值(如 175)会让「系统性下滑」逃过闸;上调到 179 则不留噪声余量。

**⚠ T3 基线跑批必定 FAIL 且 rc=1** —— 那时 prompt 还没改,手順書题大面积判错。
**rc=1 不是跑批失败**(同 U2 §7 对 `run_eval` 的注)。T3 的产出是**落盘的基线数字**,
不是绿灯。

**条款 5 是自约束型**: n=3 没有统计意义,把它当 PASS 条件就等于直接对症下药。
这三题是本单元的动机,但**不是**它的判据。

## 8. 三方核验 (T6, 规则 D)

| 角色 | 要求 |
|---|---|
| 出题方 | 独立 session,按 §5.3 隔离 |
| 划分方 | 独立 session,只执行 §5.3 第 4 条的确定性划分规则 |
| 实现方 | 改 prompt,只看 dev |
| 审查方 | 独立 `subagent_type`,审规则文本是否 pattern-level、是否泄漏 held-out 概念 |
| 抽检方 | 独立 `subagent_type`,变异测试新闸(删题 / 放宽阈值 / 双口径混用 是否会红) |
| controller | 逐 task 独立复跑 + **非自洽复算**关键数字(硬规矩 17b) |

**硬规矩 17 复用**: 派 agent 时要求**边做边落盘**;拿不到报告就当那一环没发生并在证据里点名。
**硬规矩 18**: 新加的取证信号当场补断言。

## 9. 本单元明确不能证明什么

- **不能**证明生产 `auto` 下答案质量变好 —— 判库准确率不是答案质量
- **不能**证明 `both` 档是对的席位配置 —— 只量不改
- **不能**证明新触发条件对**未来**的手順書题泛化 —— held-out 只有 12 题
- **不能**证明答题侧不受影响 —— 答题侧仪器(kickoff #4)未做,全距 6.25pt
- **不能**证明 27.42% 未章节化原文(C1 L1)相关的问题变得可答 —— 本单元不碰语料

## 10. 开工自检与本文引用数字的复跑命令

```bash
cd sdtm-rag
./.venv/bin/python -m pytest -p no:warnings -q                  # → 1189 passed (见下注)
./.venv/bin/python -c "
import chromadb; cl = chromadb.PersistentClient(path='data/chroma')
print({c.name: c.count() for c in cl.list_collections()})"      # → 4329 / 959 / 114

# §1.2 与 §6.2 的 gold 分布 (cdisc 151 / study 25 / both 5, 合计 181)
./.venv/bin/python -c "
import sys, collections; sys.path.insert(0,'.')
from eval.run_routing_eval import load_gold
g = load_gold(); print(len(g), collections.Counter(x['gold'] for x in g))"

# §1.3 的 routing={study:27, cdisc:3} (读 U2 已落盘工件, 不重跑)
./.venv/bin/python -c "
import json; print(json.load(open(
  'data/study/st01/eval/runs/u2_ruler3_prod.json'))['summary']['routing'])"

# §5.1 的红线边界 (前者被 ignore, 后者被 tracked)
git check-ignore -v data/study/st01/eval/test_set_docs_v1.yml
git ls-files --error-unmatch eval/routing_gold_ja_supplement.yml
```

三条对不上就先查环境,不要在错的基线上开工。

**⚠ 开工前已发现一处口径差(硬约束 5「数字对不上先查口径」的当场应用)**:
`docs/PROGRESS.md` 与 U2 收口证据都写 **1181 passed**,而本机实测 **1189**。
差 8 的来源查明 = U2 最后一个 commit `6812e6d`(修抽检 B 的放行条件)补了 6 个测试文件、
**在 PROGRESS 那句话写下之后**。**1189 是本单元的正确开工基线**;PROGRESS 的 1181 已陈旧,
收尾时一并更正。

**⚠ 顺带一条工具陷阱**: `pyproject.toml` 的 `addopts` 已含 `-q`,命令行**再加一个 `-q`
就是 `-qq`,pytest 会吞掉 `N passed` 汇总行** —— 于是 `grep passed` 什么都抓不到,
看起来像跑批没输出。**不要再加 `-q`**;`pytest -p no:warnings --tb=no | tail -2` 即可。
(本单元自己先踩了一次,绕道去解析 `--junitxml` 才发现根因在命令行不在 pytest。)
