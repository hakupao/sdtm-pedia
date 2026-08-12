# doc 轨 U2 — doc chunk 检索接线 设计 spec

> 日期: 2026-08-12 · 单元 = `milestones/07_rag_kg/DOC_TRACK_KICKOFF.md` §2 U2
> 前置: C1 DONE (`evidence/checkpoints/study_c1_doc_sections.md`) · U1 CLOSED 有条件
> (`evidence/checkpoints/doc_track_u1_question_set.md`, 含 §8 给 U2 的 6 条硬约束)
> 数据红线: 本文件进 git ⇒ **零真名零正文**, 只写数字/编号/形态。题集与语料留在
> `data/study/`(gitignored)。

## 0. 一句话

st01 的 114 个章节 chunk 现在检索不到。本单元把它们接进检索侧,**在 U1 已落盘的两把尺子上
量接线损耗**,并第一次碰"答题侧 context 席位挤占"这半个坑。

## 1. 开工基线 (2026-08-12 实测, 命令见 §9)

| 项 | 值 |
|---|---|
| git | `main`, 树干净 |
| pytest | **1119 passed** |
| collections | `sdtm_kb_v1` 4329 / `study_st01` 959 / `study_st01_docs` 114 |
| 卡片侧 study golden v2 | **87.50%**, 与 `runs/v2_baseline_s2on.json` **逐题 Δ0** |
| doc 侧上界 (U1, doc-only 隔离库) | k=15 → **100.0%** (⛔ 触发 spec §7 自毁条款, **用户 2026-08-12 裁定豁免**) |
| doc 侧判别力档 (U1) | k=5 → **88.33%**; k 曲线 `0.8667@3 / 0.8833@5 / 1.0000@8 起饱和` |
| 路由闸基线 | 181 题 ×3 遍, **178/181 = 98.34%**, fatal=0 |

> **引用纪律 (U1 收口 §3.2)**: 100% 这个数必须写成「触发了自毁条款, 用户豁免」,
> 不得写成「一次过」或「未触发」。

## 2. 本单元预勘察 (设计前实测, 只读零改动)

现有联邦 router 对 30 道 doc 题判库: **study 25 / cdisc 5, fallback 0** (n=1 遍)。
被判 cdisc 的 5 题 = `docs_v1_q05/q15/q17/q53/q55` (3 single_section + 2 table)。

根因看得见: `_ROUTER_SYSTEM` 把 study 定义为「ONE specific clinical study's **EDC field
cards**」——这句在 C1 之后**已过时** (study 侧现在还有 114 个手顺/計画文書章节 chunk),
偏"标准味"的题因此被判给 cdisc, 而 CDISC 库结构上答不出本研究的手顺。

⇒ 本单元必须改 router 描述, 且必须重跑路由闸 (§5.4)。

## 3. 非目标 (本单元明确不做)

1. **L1 卷首 chunk** (kickoff §3 悬案) — 用户 2026-08-12 裁定: U2 之后另开单元。
   理由: 加卷首 = 换语料 ⇒ U1 刚测的两把尺子全部失效要重测, 而 U2 的全部意义就是拿这
   两把尺子量接线损耗。另: 30 道计分题中有 **1 题** (`docs_v1_q20`) 的锚串逐字出现在卷首,
   做了卷首 chunk 后它的 gold 在字面层不再唯一, 闸 A/lint_gold 会报, 题集要跟着改。
2. **C2** (另两份 933/212 页表单版面 PDF) — kickoff §U3 三条解闸条件未满足。
3. **U4** L6 表格切点约束。
4. **doc 侧题集扩容 / gold 重写** — 尺子在本单元内**冻结**, 否则量的是尺子不是接线。
5. **卡片侧检索改动** — cards 引擎本单元零改动。

## 4. 架构

### 4.1 组件

新模块 `server/study_corpus.py` → `StudyCorpusEngine`: 一个**组合器**, 不改 `RAGEngine` 内部,
实现 `FederatedEngine` 用到的三件套 `retrieve / format_context / system_prompt`。

```
FederatedEngine(cdisc_engine, StudyCorpusEngine, llm_router)
                                     │
                       ┌─────────────┴─────────────┐
                 cards 引擎 (零改动)           docs 引擎 (新建)
                 study_st01 / 959             study_st01_docs / 114
                 top_k=15, S2 直查, hybrid     top_k=N, 无 S2, hybrid
```

- docs 引擎的 `kb_root` 仍指 `cards/` —— `RAGEngine.__init__` 硬要求 kb_root 下有
  `ROUTING.md`/`INDEX.md` (docs/ 没有), 而 kb_root **只进 system prompt 不参与检索**。
  这与 U1 测上界时**逐字同一条路径**, 数字因此可比。
- wrapper 自出 system_prompt ⇒ **docs 引擎的 system_prompt 永不使用**。这一条写成
  可执行断言 (§7), 不留成注释。
- `study_lookup` (S2) 只挂 cards 引擎 —— 它的数据源是 catalog.json, 对 doc chunk 无定义。

### 4.2 席位与合并

- cards 的 `top_k=15` **原样不动**; docs **追加** N 席 ⇒ context 长度 = 15 + N。
- 合并顺序: cards 全部在前, docs 追加在后; 按 `chunk_id` 去重。
- **不做跨库分数排序** —— 沿用联邦既有纪律 (两库相似度分布不可比)。
- `format_context` 分组标注两类来源 (卡片 / 手顺書章节), 使答题方能分辨引用的是哪一类。
- **`both` 判库下 doc 席位不缩**: cdisc/study 各 `ceil(k/2)=8` 不变, doc 仍取 N 席。
  理由: doc 是加席不是抢席, 缩了则 both 题与 study 题的 doc 召回不可比。
  代价: both 题 context = 8 + 8 + N, 记入已知限制。

### 4.3 N (doc 席位) 怎么定

零 LLM sweep `N ∈ {0, 3, 5, 8, 10, 15}`, 在 doc 30 题上同时报:

1. `source_recall` (gold 召回);
2. **context 实际字符数 / token 量** —— doc chunk 正文中位 610 字符、p90 3,595、最长 22,404,
   N=8 可能是三万字符量级, **成本必须与 recall 一起摆上桌**, 不许只报 recall 选 N。

**白送的强对照**: U1 的 k 曲线 (`0.8667@3 / 0.8833@5 / 1.0000@8`) 就是本轮各 N 的**预测值**,
参照物在本单元之外且动手之前已落盘。实测偏离 = 接线损耗, 无需事后解释。

生产 N 由 recall × context 成本共同定, **选择理由写进证据**, 不许只写结论。

### 4.4 router 改动

`_ROUTER_SYSTEM` 中 study 的语料描述改准: EDC field cards **+ 本研究自己的手顺/計画文書章节**。
规则 1/2/3 的优先级结构**不动**, 只改"study 库里有什么"的事实描述。

### 4.5 配置

`server/config.py` 新增:

| 设置 | 用途 |
|---|---|
| `study_docs_enabled: bool` | doc 通道总开关 |
| `study_docs_collection_name: str = "study_st01_docs"` | doc collection |
| `study_docs_seats: int` | N |

- 开关开着而 collection 不存在 ⇒ **启动响亮失败** (与 federation 现有纪律一致, 不静默降级)。
- `study_docs_enabled=true` 而 `federation_enabled=false` ⇒ 告警留声 (仿现有
  `study_lookup_ignored` 分支), 不拒启动。
- **生产默认值 (开/关) 由 §6 自毁条款 3 的实测结果决定, 本 spec 不预设。**

### 4.6 eval 接线

`eval/run_eval.py` 新增:

| flag | 用途 |
|---|---|
| `--study-docs` | 联邦模式下启用 doc 通道 (需 `--federated`) |
| `--doc-seats N` | 覆盖 N |
| `--corpus {auto,cdisc,study,both}` | **强制判库** —— 把判库损耗与接线损耗拆开 |

`--corpus` 默认 `auto` (现行为逐字不变)。

`eval/judge_controls.py` (新, 进 git): 阳性/阴性对照 harness —— 阳性 = 把 gold facts 原句
拼接当作答案喂给 judge; 阴性 = 空 context 作答。U1 Task 9 是一次性跑的, 本单元把它变成
可复跑脚本 (U1 §8 硬约束 5)。

## 5. 判据 (先于数据写死)

### 5.1 doc 侧两把尺子 (U1 §8 硬约束 1: 两个都要报)

| 尺子 | 命令口径 | 参照 |
|---|---|---|
| ① 接线损耗档 | `--corpus study` 强制 + `--doc-seats 15` | U1 上界 **100.0%** |
| ② 判别力档 | `--corpus study` 强制 + `--doc-seats 5` | U1 **88.33%** |
| ③ 生产档 | `--corpus auto` 走完整联邦 + 生产 N | 无历史参照, 本轮建基线 |

**①与③之差 = 判库损耗**, 必须单列, 不许并进"接线损耗"。

### 5.2 卡片侧不回归

- 48 题 retrieval-only 与 `runs/v2_baseline_s2on.json` **逐题 Δ0** (87.50%)。
- ⚠ **这条在本设计下是构造保证的** (cards 15 席不动, doc 追加) ⇒ 它**判别力很低**,
  绿灯不构成"接线安全"的证据。引用时必须同写这句。卡片侧真正的风险全部转移到 §5.3。

#### 5.2.1 ⚠ 检索非确定性 (2026-08-12 Task 3b 发现, controller 溯源实证)

**embedding API 本身非确定**, 检索层与融合层确定。三步探针 (命令见 §9):

| 探针 | 实测 |
|---|---|
| 同一 query 连续 embed 6 次 | **2 种不同向量**; 1122/1536 维不同, max \|Δ\| = **1.5e-4** |
| **固定向量**下检索 6 次 | 顺序 1 种 / 成分 1 种 ⇒ **完全确定** |
| 全链路 (每次重新 embed) | 微扰只在两块分数近乎并列时翻位 |

**打到计分上的量级**: controller 在两条路径各跑 3 遍 (卡片路径 / doc-ON 联邦路径),
**6 遍全部 `0.875` 逐题零变动**; Task 3b 实现方在 doc-ON 路径 4 遍中翻过 **1 次**
(`st01_v2_q15` 1.0 → 0.5)。合计 **7 遍 1 次**。

**推论 (必须执行)**:
1. **任何"逐题 Δ0"必须连跑 3 遍且 3 遍都成立**, 单跑一次有假红/假绿。
   逐题变动的题**按抖动记账, 不按回归记账**, 但必须列名并附遍数。
2. 本仓历史上所有"逐题 Δ0 / 零回归"的说法 (C1 的 87.50% · U1 的两遍 NONE ·
   S1/S2 的零回归) 都是**概率陈述而非确定性陈述**。**不追溯重跑**, 但引用时不得
   读作"确定性相同"。
3. **答题侧双臂必须先测噪声地板** (见 §5.3.1) —— embedding 抖动在那里只是二阶,
   LLM 生成与 judge 本身的抖动是一阶。

### 5.3 答题侧双臂 (kickoff 硬验收第 3 条 — 从未碰过的那半个坑)

同一模型同一温度, doc 通道 OFF / ON 两臂:

| 组 | n | 指标 |
|---|---|---|
| 卡片 48 题 | 48 ×2 臂 | `judge_fact_recall` 逐题 Δ |
| doc 30 题 | 30 ×2 臂 | `judge_fact_recall` 逐题 Δ |
| 阳性对照 | 两组各抽 6 | judge 应 ≈1.0 |
| 阴性对照 | 两组各抽 6 | judge 应 ≈0.0 |

**对照组抽样规则先写死** (仿 U1 Task 9, 读数据前定): 各组按 `id` 升序排序后取
`idx = ⌊n/7⌋, ⌊2n/7⌋, …, ⌊6n/7⌋` 六个位置。该规则不依赖任何分数, 事后不许换。

#### 5.3.1 空臂 (OFF vs OFF) — 噪声地板, 先于 ON 臂跑

**加一条空臂: doc 通道 OFF 跑两遍**, 同一模型同一温度, 逐题比。
两遍之间的差异 = **本尺子的噪声地板**, 它是解读 OFF-vs-ON 的前提。

⚠ **这不是改判据, 阈值一个字不动** (§6 自毁条款 3 仍是「逐题下降 ≥3 题 或 均值降 >2.0pt」)。
空臂的作用是让那个阈值**可解读**:

- 若噪声地板 **< 3 题**且均值波动 **< 2.0pt** ⇒ 阈值有判别力, 照常判。
- 若噪声地板 **≥ 3 题**或均值波动 **≥ 2.0pt** ⇒ **必须在证据里大声写明「自毁条款 3
  在本尺子上不具判别力」**, 并把 ON 臂结果与地板并列呈现。
  **不许**拿"这在噪声范围内"来消化一次真回归 —— 那正是本仓反复在防的读法。

- **必须开 `--judge`** (U1 §8 硬约束 2: 裸子串对 12–82 字整句 fact 恒接近零, 与检索质量无关)。
- `judge_parse_ok=False` 的题**单独列出**, 不许混进均值 (它会静默退回子串口径)。

### 5.4 路由闸

`eval/run_routing_eval.py --runs 3`, gold 集**一个字不改** (181 题: v3 CDISC + study v1.1 + 日语补充)。

- 判据: `exact ≥ 178/181` 且 `fatal = 0` (= 现基线, 不许放宽)。
- 逐题与基线比, **新增的 fatal 逐题列名**。
- 30 道 doc 题的判库分布**单独报**, **不并入 181 的分母** (并进去 = 换尺子, 历史数字立刻不可比)。

## 6. 自毁条款 (阈值先于数据写死, 触发即停并上报, **不许改阈值**)

1. 卡片侧 48 题 retrieval-only **不是**逐题 Δ0 ⇒ 构造保证被打脸, 说明存在未知机制,
   **方案作废退回设计**, 不许就地打补丁。
2. 尺子① (强制 study, N=15) **< 90.0%** ⇒ 接线有实质损耗 (上界 100%, 容差 10pt),
   **停下诊断**, 不许靠调 N/调 pool 把数字调上去再报。
3. 答题侧卡片 48 题: judge 逐题下降 **≥ 3 题** 或均值下降 **> 2.0pt** ⇒
   doc 通道**生产默认 OFF**, 本轮不上生产 (接线代码仍可合入, 但开关关着)。
4. 阳性对照 **< 0.80** 或 阴性对照 **> 0.20** ⇒ **尺子失效**, 当场停,
   **不许解读任何双臂数字** (U1 教训: 恒绿的闸 = 装饰品)。
5. 路由闸 `fatal > 0` 或 `exact < 178/181` ⇒ **router 改动回滚**;
   回滚形态下必须在证据里写明 doc 侧端到端天花板被压到 25/30 = 83.3%。
6. doc 侧答题 ON 臂 judge **< 0.50** ⇒ "检索到了但答不出",
   接线不算成功, **停下诊断**, 不许拿 retrieval 数字当交付。

## 7. 测试与反装饰

- `StudyCorpusEngine` 单测: cards 优先序 / doc 席位上限 / 去重 / format_context 分组 /
  system_prompt 组成 / **docs 引擎 system_prompt 从不被读** / collection 缺失响亮失败 /
  `both` 模式席位。
- **每条新断言做物理变异测试** (函数体首行 `return []` 或删输出行), 证明它会变红。
  U1 抽检方 B 抓到过两条"打了但没断言"的装饰输出, 本单元不许重犯 (硬规矩 18)。
- 反回归钉子: 仿 `test_main_persists_docs_into_a_separate_collection`, 钉住
  "cards 的 15 席不被 doc 挤占"。

## 8. 已知会看不见什么 (硬规矩 19 — 引用本单元任何绿灯时必须同写)

1. 卡片侧 retrieval-only Δ0 **由构造保证** ⇒ 该绿灯不可证伪 (§5.2)。
2. doc 侧 gold 只锚了每块一小段 (U1 限制 18) ⇒ 本单元同样**看不见 chunk 正文是否忠于 PDF**。
3. 答题侧单模型单温度 ⇒ 换模型可能翻转 (U1 `q57` 的先例)。
4. 30 题题集的判别力只在 k≤5 档实测过 (U1 §6) ⇒ 生产档 k=15 已饱和, ③ 的绿灯判别力未知。
5. 27.42% 原文在首锚点之前**不属于任何 chunk** (C1 L1), 本单元不改这件事。
6. `both` 判库下 context = 8+8+N, 本单元不评估其成本上限。

## 9. 复跑命令 (逐字)

```bash
cd sdtm-rag
# 开工自检
git status --short --branch
./.venv/bin/python -m pytest -p no:warnings --tb=short          # 1119 passed
./.venv/bin/python -c "
import chromadb; cl = chromadb.PersistentClient(path='data/chroma')
print({c.name: c.count() for c in cl.list_collections()})"      # 4329 / 959 / 114
./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards --output /tmp/chk_v2_baseline.json
#   → 87.5%, 与 data/study/st01/eval/runs/v2_baseline_s2on.json 逐题 Δ0
```

三条对不上先查环境, 不要在错的基线上开工。

### 9.1 检索非确定性溯源 (§5.2.1 的三步探针)

```python
# 同一 query: A) 连续 embed 6 次比向量  B) 固定向量检索 6 次  C) 全链路 6 次
# A 变 = 源在 embedding API; B 变 = 源在 chroma/融合层。实测 A 变 (2 种向量) B 不变。
vecs = [tuple(eng._embed_query(q)) for _ in range(6)]
seqs = [tuple(c.chunk_id for c in eng._search(q, 15, None, query_embedding=list(vecs[0])))
        for _ in range(6)]
full = [tuple(c.chunk_id for c in eng.retrieve(q, top_k=15)) for _ in range(6)]
```

计分层量级 (两条路径各 3 遍, 逐题比):

```bash
for i in 1 2 3; do ./.venv/bin/python -m eval.run_eval \
  data/study/st01/eval/test_set_study_v2.yml --retrieval-only --hybrid --study-lookup \
  --federated --corpus study --study-docs --output /tmp/jit_docon_$i.json; done
#   -> avg [0.875, 0.875, 0.875] · per-q varying across 3 runs: {}
```

## 10. 规则 D 编制 (写/审/抽检不同 session 不同 subagent_type)

| 角色 | 职责 |
|---|---|
| 实现方 | 代码 + 单测 + 变异测试 + 自跑判据 |
| 审查方 | 读 diff 判设计与判据一致性 (不与实现方同 session) |
| 抽检方 | 独立复算关键数字, 用**非自洽写法** (硬规矩 17b) |
| controller | 复现抽检结论 + 全池扩测 + 收口证据 |

失败 attempt 归档 `evidence/failures/` (规则 B)。收口证据
`evidence/checkpoints/doc_track_u2_wirein.md`。
