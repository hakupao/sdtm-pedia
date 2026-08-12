# doc 轨 U2 收口 — doc chunk 检索接线

> 状态: **DONE (有条件)** · 日期 2026-08-12/13 · 单元 = `DOC_TRACK_KICKOFF.md` §2 U2
> spec `docs/superpowers/specs/2026-08-12-doc-track-u2-wirein-design.md`
> plan `docs/superpowers/plans/2026-08-12-doc-track-u2-wirein.md`
> 数据红线: 题集 / 语料 / 逐题明细全在 `data/study/`(gitignored)。**本文件零真名零正文。**

## 0. 一句话

st01 的 114 个手順書章节 chunk 已接进检索侧并**生产默认启用** (N=8);
**接线损耗实测 0.00pt** (五档逐位命中 U1 的 k 曲线), **判库损耗 10.00pt** (归因闭合到 3 题);
⛔ **答题侧自毁条款 3 触发, 用户 2026-08-13 裁定豁免** —— 补测 ON-ON 对照后, 驱动它的那道题
**不复现**, 卡片侧回归**未被建立** (而非已被证明不存在)。

## 1. 架构 (spec §4)

新增组合器 `server/study_corpus.py::StudyCorpusEngine`, 对 `FederatedEngine` 保持 RAGEngine 鸭型:

```
FederatedEngine(cdisc, StudyCorpusEngine, router)
                            ├── cards 引擎  study_st01      959  top_k=15 (原样不动)
                            └── docs  引擎  study_st01_docs 114  追加 N=8 席
```

**加席不抢席**: cards 的 15 席不受影响, doc 追加在后, 按 `chunk_id` 去重, **不做跨库分数排序**。
docs 引擎的 `kb_root` 指 `cards/` —— 与 U1 测上界时**逐字同一条路径**, 数字因此可比
(实测: 同一 collection 换 kb_root 召回逐位相同, 因 study 侧 `source` 是裸文件名, `relative_to` 恒回落)。

`make_docs_engine` 工厂 (Task 3b) 让生产 lifespan 与 eval 两条路径**共用同一套装配**, 并有
跨路径同源闸 —— 原本两份复制粘贴的参数清单, 漂移不报错, 会让「尺子量的引擎 ≠ 生产跑的引擎」。

## 2. 数字

### 2.1 检索侧 (确定性, 零 LLM)

| 尺子 | 口径 | 实测 | 参照 |
|---|---|---|---|
| ① 接线损耗档 | 强制 `corpus=study`, N=15 | **1.0000** | U1 上界 **100.0%** |
| ② 判别力档 | 强制 `corpus=study`, N=5 | **0.8833** | U1 **88.33%** |
| ③ 生产档 | `corpus=auto`, N=8 | **0.9000** | 本轮建基线 |

```
U1 上界 100.00%  −  接线损耗 0.00pt  −  判库损耗 10.00pt  =  生产档 90.00%
```

- **接线损耗 = 0.00pt**: N ∈ {3,5,8,10,15} 五档**逐位命中** U1 的 k 曲线。
  抽检方 A 做了更强的一步 —— 直接拿 U1 的 run 文件**逐题**比 (而非比文档抄的数),
  **五档全部 per-question diffs = `{}`**, 尽管两边 pipeline 开关完全不同。
- **判库损耗 = 10.00pt**: 尺子③ 的非满分题**恰好**是 `q15`/`q17`/`q53` 三题 (3/30 = 10.0%),
  与 router 判到 cdisc 的名单逐题对上, **无残差**。⚠ 这三题**不得记为检索失败** ——
  它们压根没到 study 引擎。
- **反事实** (kickoff 硬验收 2): N=0 时 doc 侧召回 **0.0000** (0/30 满分)。
- **卡片侧不回归** (自毁条款 1): N=8 三遍协议全部 **0.875**, 逐题 Δ0, 三遍零变动。
  ⚠ 该绿灯**由构造保证** (cards 15 席不动) ⇒ **判别力很低**, 不构成"接线安全"的证据。

### 2.2 生产 N 的裁定

**N = 8** = 召回天花板上的**最小** N。N=5 省 28% token 但丢 11.67pt 召回; N=10/15 **零召回增益**
却把 context 从 3.17x 推到 3.68x / 5.19x。代价写清: **每道判到 study 的题 context 涨到 3.17 倍**,
包括 48 道根本不需要手順書的卡片题。

### 2.3 答题侧 (LLM, 非确定)

| | doc 30 题 | 卡片 48 题 |
|---|---|---|
| OFF | 0.0333 | 0.8958 (A) / 0.8819 (B) |
| N=3 | 0.8244 | 0.9167 |
| **N=8 (生产)** | **0.9517** | 0.8542 (ON-A) / **0.8819 (ON-B)** |

- 阳性/阴性对照**双向满格** (1.0000 / 0.0000, 两个题集, parse_ok 12/12) ⇒ 条款 4 未触发。
- doc 侧 **+91.83pt**, 29/30 题相对两个 OFF 臂都升 0 题降; 两臂同为 0.0 的 29 题 ON 臂全部答出
  ⇒ 条款 6 未触发。
- ⛔ **条款 3 触发 → 用户豁免**, 详见 §3。

## 3. ⛔ 自毁条款 3 — 触发, 用户 2026-08-13 裁定豁免

**两句话必须分开写, 不许合并:**

1. **事实一 (不改)**: 按当时可得数据、按**先于数据写死**的算术 (`逐题降 ≥3 题 或 均值降 >2.0pt`),
   条款 3 **触发了** (OFF-A→ON-A: 降 5 / −4.17pt; OFF-B→ON-A: 降 2 / −2.78pt)。**阈值一字未改。**
2. **事实二 (新)**: 抽检方 A 要求补的 **ON-ON 对照**改变了它的可解读性 ——

```
q23r:  OFF-A 1.0   OFF-B 1.0   ON-A 0.0   ON-B 1.0   N=3 0.3333
```

- 驱动触发的那道题**不复现**。
- ON-A vs ON-B (命令逐字相同) 均值差 **+2.78pt**, 升 2 降 0 ⇒
  **ON 臂自身噪声恰好等于声称的效应量。**
- 四种 OFF × ON 组合: −4.17 (触发) / −1.39 / −2.78 (触发) / **+0.00 (不触发)**。
  **同一个实验换一条臂就从「触发」变成「零效应」。**
- 六条卡片臂全距 **6.25pt** (含**两对命令逐字相同**的臂) > 声称效应 2.8pt。

⇒ **卡片侧回归「未被建立」, 而非「已被证明不存在」。**

**用户裁定 (2026-08-13)**: 生产默认 **ON, N=8**。
**⚠ 引用纪律**: 必须写「**条款 3 触发了, 用户裁定豁免**」。
**不得**写成「未触发」「在噪声范围内」「验收通过」。

## 4. 三方核验 (规则 D, 五方不同 session)

| 角色 | subagent_type | 结论 |
|---|---|---|
| 实现方 ×4 | executor | Task 1/2/3/3b/5/7 |
| 审查方 | code-reviewer | Task 1/2 各 **REQUEST-CHANGES** (各 1 HIGH) |
| 抽检方 A | debugger | **有条件 PASS** — 算术零错, 6 条条件 |
| 抽检方 B | test-engineer | **有条件 PASS** — 57 变异 33 KILLED / 24 SURVIVED |
| controller | — | 逐 task 独立复跑 + 非自洽复算 |

### 4.1 本单元的方法论产出 — **变异测试的三个搜索方向不等价**

三次独立实证, 每个方向都抓到前一个漏掉的东西:

| 方向 | 谁做的 | 抓到什么 |
|---|---|---|
| ①**从断言出发**找能杀死它的变异 | 各实现方 | 结论"断言全被证伪过"都为真, 但**上界 = 已有断言集合** |
| ②**从代码行出发**问"这行改坏了谁会红" | 审查方 / 抽检方 B | 整块零覆盖代码: 删光 27 行装配块**测试一条不红**; Task 1 的 9 条方向② 变异**全部存活** |
| ③**从断言的逻辑形状出发** | Task 2 实现方 / 抽检方 B | **对调型 (双点/共错型, 集合或差集不变) 是集合类断言的系统性盲区** |

**方向③ 在本单元命中 5 次**: 引擎实参对调 · cards/docs 的 `top_k` 对调 · judge 的
`question`/`answer` 对调 · 两条路径共错 · **规则文本两类来源的定义互换**。
⇒ **凡用集合或差集形状的断言, 必须同时钉方向, 且变异集里必须有一条对调型。**

### 4.2 另一个母题 — 判据没被证明能区分它声称要区分的两种情况

| 位置 | 形态 |
|---|---|
| 分组标题 / 引擎实参 / 装配块 / judge 两臂 / 规则文本配对 | **该红不红** (装饰断言) |
| **自毁条款 3 的逐题半** | **总在红** (空臂即达标) |

两头是同一件事。**空臂 (OFF vs OFF) 与 ON-ON 对照是本单元最有价值的两条控制** ——
没有它们, 一次不复现的抖动会被判成真回归并直接把 doc 通道按死在生产 OFF。

## 5. 已知限制 (每条注明**它看不见什么**)

**测量类**
1. **检索有非确定性** —— 源在 **embedding API** (同一 query 6 次得 2 种向量, 1122/1536 维不同,
   max |Δ| 1.5e-4); **固定向量下检索完全确定**。⇒ 任何"逐题 Δ0"必须连跑 3 遍。
   **本仓历史上所有"零回归"说法 (C1/U1/S1/S2) 都是概率陈述**, 不追溯重跑, 但不得读作确定性相同。
2. **答题侧仪器全距 6.25pt > 声称效应 2.8pt** ⇒ 这把尺子上**讨论 3pt 级差异没有意义**。
3. **地板到阈值空隙 0.61pt < 一道题的 judge 步长 0.69pt** ⇒ 条款 3 均值半的全部余量
   **比指标自己的量子还小**; 这是**指标粒度问题**, 再多样本也补不上。
4. **空臂 n=1 对 / ON 臂 n=2** ⇒ 噪声地板是**点估计**, 对其离散度零信息。
5. **judge 落点是粗网格** `{0, .3333, .5, .6667, .75, .8, 1}`。
6. **单模型单温度** (`jp.anthropic.claude-sonnet-4-6` / `deepseek-chat`) ⇒ 换模型可能翻转。

**收益类**
7. **doc 侧空臂差 0.00pt 是触底假象不是低噪声** —— 29/30 题钉在 0.0, 没有向下抖的空间。
8. **+91.83pt 有选题选择性偏差** —— 这 30 题是 U1 **从 doc 语料里造出来的**。
   (抽检方 A 点名: 同一把怀疑的尺子先前只用在了不利的绿灯上, 已补正。)

**覆盖类**
9. **卡片侧 retrieval Δ0 由构造保证** ⇒ 绿灯不可证伪。
10. **`both` 判库档全程未测** —— 生产会出现 `both` (context = 8+8+N), 三把尺子都不覆盖。
11. **判库损耗只测了 n=1 遍判库** —— 181 题路由闸三遍稳定, 但 doc 30 题只跑过 1 遍。
12. **27.42% 原文在首锚点之前不属于任何 chunk** (C1 L1) —— 本单元不改这件事。
13. **未验证 chunk 正文整体忠于 PDF** (C1 L9 盲点, U1 限制 18) —— 本单元同样看不见。

## 6. 本单元**不能**证明什么

- 不能证明 doc 通道**不伤**卡片题 —— 只能说这把尺子**量不出来** (§3)。
- 不能证明 N=8 是最优工作点 —— 只测了 N=3 与 N=8 两个点的答题侧。
- 不能证明题集判别力 —— U1 §6 已写明生产档 k=15 已饱和。
- 不能证明生产 `auto` 下的真实表现 —— 三把尺子里只有尺子③ 走 auto, 且答题侧全部强制 `corpus=study`。

## 7. 复跑命令 (逐字)

```bash
cd sdtm-rag
# 开工自检
./.venv/bin/python -m pytest -p no:warnings --tb=short
./.venv/bin/python -c "
import chromadb; cl = chromadb.PersistentClient(path='data/chroma')
print({c.name: c.count() for c in cl.list_collections()})"   # 4329 / 959 / 114

# 三把尺子
D=data/study/st01/eval/test_set_docs_v1.yml
./.venv/bin/python -m eval.run_eval $D --retrieval-only --hybrid --study-lookup \
  --federated --corpus study --study-docs --doc-seats 15 --output /tmp/r1.json   # 1.0000
./.venv/bin/python -m eval.run_eval $D --retrieval-only --hybrid --study-lookup \
  --federated --corpus study --study-docs --doc-seats 5  --output /tmp/r2.json   # 0.8833
./.venv/bin/python -m eval.run_eval $D --retrieval-only --hybrid --study-lookup \
  --federated --study-docs --output /tmp/r3.json                                  # 0.9000

# 卡片侧三遍协议 (自毁条款 1)
for i in 1 2 3; do ./.venv/bin/python -m eval.run_eval \
  data/study/st01/eval/test_set_study_v2.yml --retrieval-only --hybrid --study-lookup \
  --federated --corpus study --study-docs --output /tmp/cards_$i.json; done       # 0.875 x3

# 路由闸 (改 prompt 后)
./.venv/bin/python -m eval.run_routing_eval --runs 3    # 179/181 x3, fatal=0

# 答题侧对照 (自毁条款 4 —— 不成立则不许解读任何双臂数字)
for M in positive negative; do for S in docs_v1 study_v2; do
  ./.venv/bin/python -m eval.judge_controls data/study/st01/eval/test_set_$S.yml \
    --mode $M --n 6 --output /tmp/ctrl_${S}_$M.json; done; done   # 1.0000 / 0.0000
```

⚠ `run_eval` 在分数低于阈值时返回 **rc=1**, 那**不是**跑批失败 (doc 侧 OFF 臂本来就该低分)。

## 8. 给下一单元的硬约束

1. **答题侧任何 3pt 级的结论都需要先测仪器** —— 本单元实测全距 6.25pt。空臂 + ON-ON 两条控制
   是最低配置, 缺一条就会把抖动读成效应 (本单元差点犯)。
2. **`both` 判库档是未测区** —— 生产已启用 doc 通道, `both` 下 context = 8+8+8。
3. **判库损耗 10pt 是真实欠账** —— `q15`/`q17`/`q53` 在生产 `auto` 下拿不到 doc chunk。
   要修得改 router, 不是改检索。
4. **写「实测」必附可复跑命令** (U1 §8 硬约束 5, 本单元仍适用)。
   本单元自己栽过一次: shell 变量未加引号导致 6 次跑批全失败而 `echo` 照打 6 次 "done" ——
   **输出说成功不代表事情发生了, 去看产物不要看日志。**
5. **数字对不上先查口径** —— 本单元三次: 51 池 vs 48 池 (两次, 且第二次是在自己刚记过教训的
   隔壁文件里复发) · rc=1 vs 跑批失败。
