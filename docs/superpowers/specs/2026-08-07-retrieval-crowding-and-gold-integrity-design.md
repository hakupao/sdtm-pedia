# 检索同质簇挤占 + gold 完整性 — 设计

> 建立: 2026-08-07
> 路由词入口: 「检索续跑 开始任务」→ `milestones/07_rag_kg/NEXT_ROUND_KICKOFF.md` §2 A 靶
> 状态: 设计待实施

## 0. 这份 spec 推翻了什么

`NEXT_ROUND_KICKOFF.md` §2.A 把 q38 (CDISC 140 题唯一 recall 0.0) 的根因写作
**"chapters/ 下 ≤20KB 的文件整个当一个 chunk, 语义被稀释"**。

诊断证据表明该判断不成立。q38 失分是三件独立的事叠在一起, 整文件稀释是其中最弱的一件。

### 诊断实测

**本 spec 全部数字的来源命令** —— 写这份 spec 时探针尚在 scratchpad, 落库前**只有下面这条能跑**:

```bash
cd sdtm-rag && .venv/bin/python \
  /private/tmp/claude-501/-Users-bojiangzhang-MyProject-sdtm-pedia/6968e982-799a-47d0-8532-7f176f6a8f17/scratchpad/crowding_probe.py
```

段②2a 把它落到 `sdtm-rag/eval/crowding_probe.py` 后, 本节数字必须用落库版**重跑核对**,
数字若变则以重跑值为准并在证据里记录差异。在那之前引用本节数字必须带这条 scratchpad 路径 ——
**不许提前写成 `eval/crowding_probe.py`**, 那是一条跑不出数的假命令 (硬规矩 2)。

> **⚠️ 口径警告 (2026-08-07 由 Task 1 实测补上, 初稿漏了这一行)**: 下表除注明外均为
> **dense-only** 口径。**生产口径是 hybrid + S1**, 在那里 `ch04 §4.2.2` **根本不在 top-15** ——
> hybrid RRF 把 dense 排第 1 的它挤掉了。故 q38 在 dense-only 下补完 gold 得 0.5,
> 在生产口径下仍是 **0.0**。挤占比本表初稿呈现的更严重: 不是"gold 排不进来",
> 而是"把已排第 1 的正确 chunk 挤掉"。引用本表任何数字必须带口径。

| 事实 | 数据 | 含义 |
|---|---|---|
| `ch04 §4.2.2 Two-character Domain Identifier` 正文字面回答了 q38 | dense 排名 **#1, sim 0.6970**; **hybrid 口径下不在 top-15** | dense 找得极准, 而生产口径把它丢了 |
| 该 section **不在 q38 的 gold 里** (gold 只有 `chapters/ch02`) | — | **判据缺陷: 假失分** |
| top-60 被 **59 条 `domains/*/spec.md §DOMAIN`** 占满 | sim 区间 [0.6689, 0.6851], 极差 **0.0162** | **真缺陷: 同质簇挤占** |
| gold `ch02 §whole_file` | dense **#71, sim 0.5613**; 剔掉那 59 条后升到 **#12** | 稀释真实存在, 但**剔簇后仍进不了 top-15** |

`§DOMAIN` 簇是模板化变量行 (~200–350 字符), 63 个域逐字近似:

```
### DOMAIN | Order: 2 | Label: Domain Abbreviation | Type: Char
| Role: Identifier | Core: Req | CDISC Notes: Two-character abbreviation for the domain...
```

字面含 "Two-character abbreviation", 故整簇对 q38 齐刷刷高分。同一形状存在于每个域的
每个公共变量行 (`DOMAIN` / `STUDYID` / `USUBJID` / `VISIT` / `EPOCH` …)。

### 挤占的普遍性 (层① 探针, 全 140 题, k=15)

| 指标 | 值 |
|---|---|
| 最大同名 section 簇 ≥3 席 | **40/140 (28.6%)** |
| ≥5 席 | 11 题 (7.9%) |
| ≥8 席 | 3 题 (2.1%) |
| 平均多余席位 `dup_seats` | 1.73 / 15 |
| 平均 `distinct_sections` | 13.27 / 15 |

重灾: q38 `§DOMAIN` **14/15 席** · q104 `§VISIT` 9 · q39 `§Model Definition` 8 ·
q08 `§USUBJID` 7 · q29 `§Related Domains` 7 · q81 `§DOMAIN` 7。

## 1. 核心洞察: 尺子为什么看不见这件事

**除 q38 外, 上述重灾题全部 gold 满分。** 现有 140 题判据对挤占结构性失明, 机制是:

- S1 (structured lookup) 是 union-add **前置注入**: 确定性解析 gold 文件 → 直接插到 top-k 最前,
  且不会被挤掉 (`_merge_lookup_first`)。
- 于是"gold 有没有被召回"这件事, **被系统的另一个组件确定性地保证了**。
- top-k 里剩下的 `k − |S1 注入|` 个席位的质量, **从来没有被任何尺子测量过**。

实证 (同一次探针输出):

| 题 | S1 注入 | gold 结果 | 剩余席位实况 |
|---|---|---|---|
| q104 | 3 条 `VARIABLE_INDEX` (含 gold `§VISITDY`) | **满分** | 剩 12 席里 **9 席**被 `§VISIT` 簇吃掉 |
| q08 | 1 条 `VARIABLE_INDEX §USUBJID` | **满分** | `§USUBJID` 簇 7 席 |
| q38 | **0 条** (概念题, S1 resolve 不出目标) | 0.0 | 纯落 hybrid → 被簇淹没 |

**S1 保住了 gold, 却没保住 context。**

这是 VI 那轮"护栏不能自洽"(硬规矩 6) 的另一个变体: 那次参照物来自生成器内部;
这次**判据的达成条件被同一系统的另一个组件保证了**, 判据因而失去对该维度的判别力。

补充战略事实: 140 题里现在只剩 2 题失分 (q38 + 已裁定为永久 known limit 的 q126)。
**q38 一修, CDISC 这把尺子就 100%、判别力耗尽** —— 与 study golden v1.1 同一下场。
故本轮修 q38 必须同时立新尺子, 否则第 2 条真缺陷会被满分永久掩盖。

## 2. 设计

三段按依赖顺序。**② 的结论允许是"不修"** —— 若层② 判定挤占无害, 那就不动检索层。
取证若不允许得出否定结论, 取证就是走过场。

### 段① gold 完整性修复 (pattern 层, 不只 q38)

**1a. q38 判据订正**

`eval/test_set_v3.yml` 的 q38 `expected_sources` 由

```yaml
expected_sources: [chapters/ch02]
```

改为 (AND 语义, 两条都要):

```yaml
expected_sources:
  - chapters/ch02
  - chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier$
```

理由: 题干问两件事 —— "How are domain abbreviation codes **assigned**" 由 ch02 §2.6
(创建新域步骤 e/f: 确定 domain code, 不在 CDISC CT Domain Abbreviations codelist,
AD/AX/AP/SQ/SA 不可用) 回答; "rules for the **two-character** domain code" 由
ch04 §4.2.2 ("limited to A-Z for the first character, and A-Z, 0-9 for the second") 回答。
两者不可互相替代, 故 AND 而非 `expected_sources_any`。

**1b. 反例扫描 (硬性, 不允许只改 q38 收工)**

只改 q38 一题 = example-level 对症下药。必须做 pattern 层扫描:

- 程序化对全 140 题列出「当前生产口径 top-3 中不在 gold 的源」→ 差异清单 (140×3 上界)。
- 差异清单交**独立 agent** (与出题方、实施方均不同 `subagent_type`) 逐条审:
  该源是否为该题的权威答案源而 gold 遗漏了。
- 判定为遗漏的, 一并补进 gold; 判定不是的, 记录理由。

**验收**: 扫描覆盖 140/140 题; 每条判定有书面理由; 补 gold 的改动逐题列出前后 diff。

**⚠ 必须随之声明的口径断裂**: 段① 改判据后, CDISC 分数**换了一把尺子**,
与历史 98.93% (section 级) **不可比**。引用新数字必须写明"含 gold 完整性修复后口径"。

### 段② 挤占: 先取证, 后定修法

**2a. 层① 结构探针 (确定性, 零 LLM) — 落库常驻**

scratchpad 探针定型后落到 `sdtm-rag/eval/crowding_probe.py`, 输出:
`dup_seats` / `max_cluster` / `max_cluster_section` / `distinct_sections` + 完整 top-k composition。

配套单测断言探针本身正确 (构造已知组成的假 chunk 列表, 验统计口径)。
**探针只描述结构, 不判定好坏** —— 好坏归层②。

**2b. 层② 损害证明 (外部锚)**

- **题面**: max_cluster ≥5 的 11 题 + q38 = **12 题**。**零造题** —— 题面一字不动,
  杜绝"由已知缺陷倒推出题"的对症下药。
- **三组对照** (候选池 = hybrid fusion 之后、S1 注入之前的那一份, 三组同池同序, 唯一差别是配额):
  - A = 生产 top-15 (现状, 无配额)
  - B1 = 同名 section **限 1 席**, 腾出的席位由池中下一位依次补足到 15
  - B2 = 同上, **限 2 席**
  - S1 注入的 chunk 三组一律豁免配额 (它们是确定性 gold, 不属被检验对象)
- 三组各自 `format_context` → 同一答题模型 → `--judge` 语义口径评答案正确性。
- **锚**: 答案正确性, 独立于 `section 名`这个代理量 (满足硬规矩 6: 参照物在被检验机制之外)。
- B1 与 B2 同跑的理由: B1 回答"挤占有没有害", B2 回答"去多了会不会反伤枚举类题"。
  单跑一个无法区分这两种失败。

**判定规则 (先写死, 不许看到数据再定)**。

n=12 谈不上统计显著性, 故**不用均分差, 用逐题方向**。对每组 B 与 A 逐题比 judge 分:
`improved` = B 分 > A 分的题数, `regressed` = B 分 < A 分的题数。
定义 **净改善 = improved − regressed**, 判定门槛 **净改善 ≥ 3 且 regressed ≤ 1**
(12 题里 3 题净改善 = 1/4 样本方向一致, 且几乎无反伤)。

| 结果 | 结论 |
|---|---|
| B1 与 B2 均过门槛 | 挤占有害 → 进 2c, N 取净改善更高者; 并列取 **N=2** (保守, 少动) |
| 仅 B2 过门槛 | 去冗有价值但 1 席过激 → **N=2** |
| 仅 B1 过门槛 | 挤占有害且需强去冗 → **N=1**, 但须在证据里单列 B2 为何不够 |
| 两组都不过门槛且 `regressed` 均 ≤1 | **挤占存在但无害 → 不修检索层**, 结论写进证据, 探针留作常驻监控 |
| 任一组 `regressed ≥ 4` | 同质簇对那些题是**有效信号**而非噪声 → 不修, 并在证据里更正本 spec 的假设 |

judge 打分若出现 A/B 完全同分的题, 计入分母但不计入 improved/regressed (作"无判别力"记录)。
**若无判别力题 ≥ 8/12, 整个层② 判定作废** —— 那说明这 12 题的答案质量对 context 组成不敏感,
锤子选错了, 须换锚重做而不是顺着读结论。

**样本量诚实声明**: n=12, 且这 12 题是按 `max_cluster` 选出的极端样本,
**不是 140 题的随机样本**。结论只能推广到"重挤占题", 不能推广到全集。

**2c. 修法 (仅当 2b 判定有害才做)**

检索层 per-section 配额: 在 fusion 之后、S1 注入之前对候选重排。
选这一层的理由: 不重灌索引; S1 前置注入语义不受影响; 确定性无超参数; 可单测。
实施细节留给实施计划。

**验收**: 全 140 题零回归 (逐题 Δ 对照, 段① 新口径下) + 层② 复跑改善成立 +
`pytest` 全绿 + 新增配额逻辑单测。

### 段③ chapters 切分策略

- 现状 (`scripts/chunkers/chapters.py`): >50KB→H3, 20KB–50KB→H2, ≤20KB→整文件单块。
  落在整块档的是 ch01 (11,070 B) / ch02 (18,141 B) / ch03 (19,708 B)。
- 改动: 下调 whole_file 阈值使这三个文件按 `^## ` 切。H2 数实测
  (`grep -c '^## ' knowledge_base/chapters/<f>.md`): ch01 **5** / ch02 **9** / ch03 **3**;
  ch02 切后平均 ~2.0KB。
  (初稿此处写"ch02 有 8 个 H2"是**数错的、未实测**的数字 —— 正是硬规矩 2 要防的东西, 已订正。)
  无该级标题时仍回落整文件 (现有回落分支保留)。
- **需重建索引**, 且 `chunk_count` 会变 (当前 4315), `/api/info` 与 freshness 断言需同步。

**排最后的理由**: 证据显示它对 q38 非主因 (剔簇后 ch02 仍只到 #12)。它的真实收益
只有在段①(判据准) + 段②(挤占这个更强的干扰被处理或被证无害) 之后才测得出。

**验收**: 全 140 题零回归 + 层① 探针复跑 (确认切分没制造**新的**同质簇 ——
ch02 切成 8 块后 `§whole_file` 这个簇头会消失, 但要确认没换成别的簇) +
`pytest` 全绿 + 索引重灌后 `reconcile_meta` / freshness 全 OK。

## 3. 本 spec 遵守的既有硬规矩

引自 `NEXT_ROUND_KICKOFF.md` §3:

1. **判据检查工具与判据逐字同语义** — 段①1b 的扫描工具须与 `check_source_recall` 同语义,
   加等价性测试锁 (上一轮 lint 剥 `.md` 后匹配制造 8 条假阳性的教训)。
2. **写「实测」必附可复跑命令, 且数字必须真的从那条命令跑出来, 单位对齐** ——
   本 spec 所有数字均出自 §0 那条探针命令。
3. **红线检查程序化** — 本轮不碰 study 库, 红线风险低, 但涉及 study 的任何产出仍走程序化复扫。
4. **三方隔离 (规则 D)** — 出题/改 gold ≠ 实施 ≠ 抽检验收, 三个不同 `subagent_type`。
   段①1b 的独立审必须不是改 gold 的那个 agent。
5. **规则 A 抽样总体 = 本轮实际变更集合** (改动的 gold 条目 + 改动的检索行为), 非变更后全集。
6. **护栏不能自洽** — 层② 的锚是答案正确性, 在 section-name 代理量之外。**本轮新增变体**:
   参照物不仅不能来自生成器内部, 也**不能被系统的另一个组件确定性保证** (S1 钉死 gold recall
   正是这种情况)。
7. **一个 gold fact 钉不住穷举类题目** — 段①补 gold 时, 多问的题钉多条独立可判定源 (q38 即 AND 两条)。

## 4. 已知限制 (随结论一起声明)

- 层② n=12 且为极端样本, 结论不能推广到全集 (见 2b)。
- 层① 的"同质簇"定义只用 **section 名字面相同**, 不含语义近似。语义近似但 section 名不同的
  冗余 (如不同域的 `Related Domains` vs `Overview`) 照不出来。这是刻意的确定性取舍。
- 段① 修 gold 后 CDISC 分数与历史口径断裂, 且新尺子在 q38 修好后很可能再次逼近饱和 ——
  **CDISC 140 题这把尺子的剩余寿命有限**, 长期需要新题源, 不在本轮范围。
- 段③ 重灌索引会改变 `chunk_count`, 任何引用 4315 的断言/文档需同步。
- q126 仍是永久 known limit, 本轮不动。

## 5. 不在本轮范围

- Plan B Phase 4 联网搜索 (kickoff §2.C, 依赖联邦答题闸)。
- 联邦答题闸本体 (kickoff §2.B 的后半; 其一行硬前置已于本轮开工前修完并 862 passed)。
- 答题侧「域数估而不数」(kickoff §2.D3), `vic01` 探针继续保持故意失分。
- study `form_overview` 50% (kickoff §2.D1)。
