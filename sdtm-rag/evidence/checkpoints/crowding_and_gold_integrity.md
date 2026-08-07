# 收口证据: 检索同质簇挤占 + gold 完整性 (2026-08-07)

> spec: `docs/superpowers/specs/2026-08-07-retrieval-crowding-and-gold-integrity-design.md`
> plan: `docs/superpowers/plans/2026-08-07-retrieval-crowding-and-gold-integrity.md`
> retro: `docs/superpowers/2026-08-07-crowding-gold-RETROSPECTIVE.md`
> commit 链: `2e2ce21 .. 4109732` (+ 本收口 commit)
> 分段证据: `crowding_layer1.md` (层①) · `crowding_layer2.md` (层②) · `topk_jitter.md` (抖动) ·
> `pool_depth_invariance.md` (池深度) · `chapters_chunking.md` (切分) · `gold_gap_verdicts.md` (gold 判定)

---

## 0. 三句话结论

1. **段① gold 完整性: 做完了, 规则 A 抽检判"有条件 PASS"。** 27 条漏掉的权威源补进 26 题,
   q38 从"判据缺陷造成的假失分"变成"判据准了、检索确实缺一块"。全集 **99.17%** (140 题,
   retrieval-only, hybrid + structured_lookup, **含 gold 完整性修复后**)。
   **条件**: 实现方对 OR 纪律**只在拒绝时执行、在自建时未执行**, 3 题判别力实质下降 (§7)。
   **不影响本轮已出的 99.17%**, 是对未来回归的隐性风险。
   **前三条解除条件已做完** (§7.1): q73 改回 AND (**实测 140 题逐题 Δ0, 0.9917 不变**) ·
   q115/q117 yml 就地注释 · "无自动闸"入档并列为下一轮候选闸。
2. **段② 挤占是否有害: 没测出来。** 层② 判定 **`VOID_TIE` 作废**, **Task 7 是 SKIPPED —— 前置
   未满足, 不是"判定挤占无害"**。我们**仍然不知道**挤占是否有害。见 §4.1。
3. **段③ chapters 切分: 做完了, 但没解决 q38。** 取消整文件单块档后 ch02 的最好块从 #71 升到
   #63, 而真正答题的 §2.6 在 #70 —— **仍在 top-15 外**, q38 recall 仍是 0.3333。
   顺带查明 `whole_file` 是个**纯人造簇**。

---

## 1. 终值与口径

| 项 | 值 | 口径 |
|---|---|---|
| CDISC 全集 source recall | **99.17%** | 140 题, `--retrieval-only`, hybrid (RRF) + structured_lookup, `top_k=15`, **含 gold 完整性修复后** |
| 非满分题 | `{q38: 0.3333, q126: 0.5}` | 同上 |
| 测试 | **958 passed / 0 failed / 0 errors / 0 skipped** | 全量 `pytest -q` |
| `chunk_count` | 4315 → **4329** | 重灌索引后, `/api/info` |
| 层① 同名 section 簇 ≥3 席 | 28.6% (40/140) → **23.6% (33/140)** | 重灌前 → 重灌后, 单次快照 |
| 层② 判定 | **`VOID_TIE`** (33 臂全 1.00, 零方差) | 11 题 × 3 组, judge = `deepseek/deepseek-chat` |

### ⚠️ 口径断裂声明 (引用上表任何数字前必读)

**a. 99.17% 与历史 98.93% 不可比 —— 换了一把尺子。**
本轮往 26 题的 `expected_sources` 里补了 27 条此前漏掉的权威源, 判据集合本身变了。
两个数字之间的差不是检索变好或变坏, 是**被测的东西换了**。要做纵向对比, 只能拿
**同一版 gold** 跑两次。凡引用 99.17%, 必须连"含 gold 完整性修复后"这七个字一起带。

**b. 99.17% 内部也有一条断裂**: 99.29% 曾短暂存在并**随已提交的 JSON 进过仓**
(commit `7c9ee68`), 后因 q38 从 OR 组改回 AND 而降为 99.17% (commit `8930461`)。
`0.992857 + (0.3333 - 0.5)/140 = 0.991666`, 降幅 100% 来自 q38 一题。
**若在任何地方看到 99.29%, 那是已作废的中间值。**

**c. 层① 数字的可复现性是有条件的。** `max_cluster` 可以直接引用 (跨 20 进程 0/140 题变化),
但 `dup_seats` / `distinct_sections` 对 q47/q117 只能按分布引, **排位结论一律作废**。
该豁免的机制与**失效条件**见 `crowding_layer1.md` §2 / `topk_jitter.md` §5.6 ——
**"重灌索引"就是它自己明列的失效条件之一**, 故重灌后的 23.6% 是重测值而非沿用值。

**d. 层② 的 n=11 是按 `max_cluster` 挑的极端样本, 不可推广到 140 题。**
它连"这 11 题上挤占是否有害"都没测出来 (§4.1), 更不构成对全集的任何陈述。

**e. dense-only 与生产口径 (hybrid + S1) 是两套数, 混引会得出相反结论。**
`ch04 §4.2.2` 在 dense-only 下是检索 **#1**, 在生产口径下**根本不在 top-15**。
本轮开工时的诊断跑的是 dense-only, plan 里写的预期值因此是错的 (§4.6)。

---

## 2. 三段各自的前后数字

### 2.1 段① gold 完整性 (Task 1 / 2 / 3 / 3C)

| 项 | 前 | 后 |
|---|---|---|
| q38 `expected_sources` | 1 条 (`chapters/ch02`) | 3 条全 AND (`ch02` + `ch04 §4.2.2$` + `ch04 §4.1.6$`) |
| q38 source recall (dense-only) | 0.0 (**假失分**) | 0.5 |
| q38 source recall (生产口径 hybrid + S1) | 0.0 | **0.3333** |
| 全集 source recall | 98.93% (**旧尺子**) | **99.17%** (**新尺子**) |
| 补进的 gold | — | **27 条 / 26 题** |
| section 级 gold 总量 | 20 条 | **49 条 / 37 题** (耦合面 ×2.45) |
| OR 组题数 | 18 | **14** (段二 18→15; §7.1 q73 改 AND 后 15→14) |

**q38 的两组口径实测** (`eval/test_set_v3.yml` 与 `scripts/tests/test_gold_q38_integrity.py`
的注释指到这里):

- **dense-only**: `ch04 §4.2.2` 排 **#1, sim 0.6970** —— 旧 gold 把这次**正确召回**判成 0.0。
  这是补 gold 的理由: **判据缺陷造成的假失分**。
- **生产口径 (hybrid + structured_lookup)**: 同一个 `§4.2.2` **不在 top-15** —— hybrid 的 RRF
  把 dense 排第 1 的它挤掉了。故"加 §4.2.2"这一步**不涨分**, 它买到的是**判别力**。
- **q38 当前值 0.3333** (不是 0.0): 后续按 gold 完整性判定又补进第三个 AND 成员
  `ch04 §4.1.6`, 它命中 ⇒ 3 缺 2。**0.0 描述的是加 §4.2.2 那一步的增量, 不是本题现值。**

**挤占的含义因此被升级**: 不是"gold 排不进来", 而是"**把已经排第 1 的正确 chunk 挤掉**"。

**判定不是实施方自己下的** (规则 D): 182 条 unmatched 由第三个 `subagent_type` 独立判定 ——
遗漏_应补 27 / 相关但非权威 119 / 不相关 36。核心结论是 **q38 不是孤例**: 27 条里 14 条同属一型
(`terminology/core/*.md` 的 `Used by variable(s)` 行逐字回答题干, q16/q92/q96 收了该源而孪生的
q43/q45/q46/q48 没收) —— **根因是判据写法自相矛盾, 属 pattern 层不是 example 层**。

判定方两条实施警告都已落地: ① `expected_sources` 是 AND, 直接追加会把题**改严**;
② 那 14 条依赖的行**不在 KB 正文**, 是 `chunkers/terminology.py:260` 注入的 ⇒ 必须同时加
**chunk 层断言**, 否则改 chunker 会让 gold 静默失效。

**q126 特别裁定** (用户 2026-08-07): 补 gold, 且**不推翻**原技术裁定。原 known limit 的结论是
"检索够不到 `SE/assumptions.md`、`TE/spec.md`", 该结论**仍然成立**; 本次改的是判据完整性这个
**独立维度** —— 检索早已召回等价权威源 `model/03#Subject Elements (SE)` 而 gold 没写它。
q126 现值 0.5, **本轮未动检索**。

**判据实现改动的等价性怎么证的**: 不是靠 eval 的 Δ0 (那把仪器分辨率不够, 见 §5), 而是靠
**逐格差分对拍** —— 已归档为 `eval/tests_support/gold_semantics_diff.py` (§3 命令 f)。

### 2.2 段② 挤占是否有害 (Task 4 / 5 / 6, Task 7 **SKIPPED**)

| 项 | 值 |
|---|---|
| 层① `max_cluster ≥3` | **40/140 = 28.6%** (重灌前单次快照) |
| 层① 重灾 | q38 `§DOMAIN` **14/15 席** · q104 `§VISIT` 9 · q39 8 · q08 7 · q29 7 · q81 7 |
| 层② 三组 | A (无配额) / B1 (同名 section 限 1 席) / B2 (限 2 席); 管线 `fuse(60) → 配额 → 截15 → S1` |
| 层② 分数 | 33 臂**全部 1.00, 零方差**, gold fact miss 总数 **0**, judge 未解析 0 次 |
| 层② 判定 | **`VOID_TIE`** (同分题 10/10 ≥ 8, 触发写死的自毁条款) |
| Task 7 | **SKIPPED —— 前置未满足** |

**配额确实生效了, 答案确实变了, 只有分数没动**: B1 与 A 的 context 逐位差 **5–13 席**,
B2 **4–12 席** (11 题无一题与 A 相同); 33 个答案里与 A 逐字相同的**一个都没有** (长度比低至 0.72);
而 33 个分数全是 1.00。**context 变了 + 答案变了 + 分数不变 ⇒ 变的是量具照不见的那部分。**

详见 §4.1 (为什么这不是"无害") 与 §4.2 (量具为什么失灵)。

**副产品 (下轮可直接用)**: `server/diversity.py` 的 `apply_section_cap` 已落地并有单测,
Task 7 真要做时不必重写。

**两条被顺手证伪的上游前提**:
- `POOL_DEEP_OK = false` —— 加深池会改 RRF 分数表 (e2e A/B 不一致 4032 对 vs A/A 空白对照 0 对)。
- `FUSE_OUT_DEEP_OK = true` —— 且**代码结构可证**: `_hybrid_fuse` 里 `k` 只出现在最后一行
  `ranked[:k]`, 分数表与全排序均与 `k` 无关 ⇒ 深融合的前 15 名恒等于浅融合 (非仅 140/140 经验)。

### 2.3 段③ chapters 切分 (Task 8)

| 项 | 前 | 后 |
|---|---|---|
| ch01 / ch02 / ch03 块数 | 1 / 1 / 1 (整文件单块) | **5 / 9 / 3** (按 H2) |
| `chunk_count` | 4315 | **4329** (+14) |
| 140 题 gold | avg 0.9917 | **avg 0.9917, 逐题零变化** |
| ch02 在全 140 题 top-15 席位 | 48 | **98** (分散在 9 个真实小节名下) |
| 层① `max_cluster ≥3` | 28.6% (40/140) | **23.6% (33/140)** |
| 层① 新簇 | — | **0 个** (单次快照口径) |

**本改动没有解决 q38** (实现方在一个"看起来成功"的 task 里主动写死了这一条):
ch02 最好的块从 #71/0.5613 提到 **#63/0.6477**, 但真正回答 q38 的 **§2.6 Creating a New Domain
在 #70/0.5963 —— 仍然远在 top-15 外**, q38 recall 仍 33%。原因: 席位是被另一侧的
14 席 `§DOMAIN` 簇吃掉的, 那是配额的辖区, 不是切分能修的。
(前值 #71 是 brief 引述的既有诊断, **本轮未复测**, 旧索引已被覆盖; 跨索引比排位不可复现,
"提了 8 位"只应读作数量级。)

**意外收益: `whole_file` 是个纯人造簇。** 它原本在 **23 题**里成簇 —— ch01/ch02/ch03 三个
**内容毫不相干**的整章共用同一个 section 名, 只因按字面计簇才被认成"同质"。
旧策略不只稀释语义, 还**凭空造出跨文件假同质簇**。这直接影响 spec §0 的 28.6% (§4.3)。

**真实损失见 §4.4 (C2 溯源)。**

---

## 3. 可复跑命令 + 原始输出

全部命令从 `sdtm-rag/` 起, 解释器 `.venv/bin/python`。

### (a) 全量测试

```bash
.venv/bin/python -m pytest -q --junit-xml=/tmp/j9.xml >/dev/null 2>&1
.venv/bin/python -c "
import xml.etree.ElementTree as ET
a=ET.parse('/tmp/j9.xml').getroot().find('testsuite').attrib
print({k:a[k] for k in ('tests','errors','failures','skipped')})"
```

```
{'tests': '958', 'errors': '0', 'failures': '0', 'skipped': '0'}
```

> 开工基线**未在本 task 复跑** (需 checkout 历史 commit)。仓内两处记录不一致:
> `NEXT_ROUND_KICKOFF.md` §6 写 859, 本轮 plan 开工记录写 862。故本文只报**当前值 958**,
> 增量按 +96 ~ +99 读, 不给精确差。—— 这本身就是本轮主题的一个实例 (§4.5 c)。

### (b) 本轮新增/改动的 8 个测试文件单独跑 (确认 `test_section_gold_exists` 是 passed 而非 skipped)

```bash
.venv/bin/python -m pytest scripts/tests/test_section_gold_exists.py \
  scripts/tests/test_gold_q38_integrity.py scripts/tests/test_chapters.py \
  scripts/tests/test_crowding_probe.py scripts/tests/test_crowding_ab.py \
  scripts/tests/test_source_recall_section.py scripts/tests/test_jitter_probe.py \
  scripts/tests/test_scan_gold_gaps.py -p no:warnings -q --junit-xml=/tmp/j_sub.xml >/dev/null 2>&1
.venv/bin/python -c "
import xml.etree.ElementTree as ET
a=ET.parse('/tmp/j_sub.xml').getroot().find('testsuite').attrib
print({k:a[k] for k in ('tests','errors','failures','skipped')})"
```

```
{'tests': '95', 'errors': '0', 'failures': '0', 'skipped': '0'}
```

单独确认 section gold 存在性闸:

```bash
.venv/bin/python -m pytest scripts/tests/test_section_gold_exists.py -p no:warnings -q \
  --junit-xml=/tmp/j_sg.xml >/dev/null 2>&1
.venv/bin/python -c "
import xml.etree.ElementTree as ET
a=ET.parse('/tmp/j_sg.xml').getroot().find('testsuite').attrib
print('test_section_gold_exists:', {k:a[k] for k in ('tests','errors','failures','skipped')})"
```

```
test_section_gold_exists: {'tests': '2', 'errors': '0', 'failures': '0', 'skipped': '0'}
```

> **`skipped` 必须是 0**: 这个闸在无活索引时会 skip 而不是红。**skip 不算绿** ——
> 它 skip 只说明索引没建成, 什么也没验。

### (c) 终值 + 非满分题

```bash
.venv/bin/python -c "
import json
with open('evidence/checkpoints/gold_integrity_after.json', encoding='utf-8') as f: d=json.load(f)
s=d['summary']
print('source_recall_avg =', s['source_recall_avg'], '| n_scored =', s['n_scored'],
      '| top_k =', s['top_k'], '| hybrid =', s['hybrid'], '| structured_lookup =', s['structured_lookup'])
print('非满分题 =', {r['id']: r['source_recall'] for r in d['results'] if r['source_recall'] < 1.0})"
```

```
source_recall_avg = 0.9917 | n_scored = 140 | top_k = 15 | hybrid = {'fusion': 'rrf', 'alpha': None} | structured_lookup = True
非满分题 = {'q38': 0.3333, 'q126': 0.5}
```

### (d) 层① 重灌前后对照

```bash
.venv/bin/python -c "
import json
def load(p):
    with open(p, encoding='utf-8') as f: return json.load(f)
for tag,p in [('重灌前','evidence/checkpoints/crowding_layer1.json'),
              ('重灌后','evidence/checkpoints/crowding_layer1_after_split.json')]:
    d=load(p); n=len(d)
    ge3=sum(1 for r in d if r['max_cluster']>=3)
    print(f'{tag}: >=3 席 {ge3}/{n} = {100*ge3/n:.1f}%  | mean max_cluster {sum(r[\"max_cluster\"] for r in d)/n:.3f}'
          f' | mean dup_seats {sum(r[\"dup_seats\"] for r in d)/n:.3f}'
          f' | mean distinct {sum(r[\"distinct_sections\"] for r in d)/n:.3f}')"
```

```
重灌前: >=3 席 40/140 = 28.6%  | mean max_cluster 2.300 | mean dup_seats 1.729 | mean distinct 13.271
重灌后: >=3 席 33/140 = 23.6%  | mean max_cluster 2.157 | mean dup_seats 1.471 | mean distinct 13.529
```

### (e) 服务现状

```bash
curl -s localhost:8000/api/info
```

```
{"collection_name":"sdtm_kb_v1","chunk_count":4329,"default_model":"bedrock/converse/jp.anthropic.claude-sonnet-4-6",
"fallback_model":"deepseek/deepseek-v4-pro","top_k":15,"structured_lookup":true,"hybrid":true,"hybrid_fusion":"rrf",
"prompt_guardrail":true,"judge_model":"deepseek/deepseek-chat","index_fresh":true,
"index_freshness_reason":"index is in sync with knowledge_base","federation":true}
```

### (f) 判据等价性差分对拍 (改 `source_matches` / `check_source_recall` 前后必跑)

```bash
.venv/bin/python -m eval.tests_support.gold_semantics_diff --old-ref 501875b
```

```
旧版本: 501875b:sdtm-rag/eval/run_eval.py
真实 gold 字符串: 121 条
对拍格数: 15620
mismatches: 0
docstring: 旧 32 非空行 / 新 33
  dropped: []
  added:   ['单条匹配委托给模块级 `source_matches` —— 判据扫描工具共用同一实现 (硬规矩 1)。']
```

> Task 2 当时跑的是 **12870 格 / 96 条真实 gold**; 现在是 **15620 格 / 121 条**, 因为段① 往
> 题集里补了 27 条 gold, 网格自己长大了。**两个格数不是矛盾, 是两个时点。**

### (g) 剔除人造簇后重算 28.6% (spec §0 的标注命令)

见 `docs/superpowers/specs/2026-08-07-retrieval-crowding-and-gold-integrity-design.md` §0 尾部,
原样输出:

```
>=3 total: 40
head==whole_file: ['q14', 'q37', 'q40', 'q66', 'q86']
excl. whole_file: 38 => 27.1%
```

### (h) 层② 从落盘 JSON 重算判定 (零 LLM 调用)

```bash
.venv/bin/python -m eval.crowding_ab --summarize evidence/checkpoints/crowding_layer2.json
```

原样输出见 `evidence/checkpoints/crowding_layer2.md` §5.1 (逐题分数表 + `VOID_TIE` 判定行)。

---

## 4. 必须点名的事

### 4.1 ⛔ Task 7 是 SKIPPED —— 前置未满足, **不是**"判定挤占无害"

**这条最容易被下一个人读反, 所以写死在这里。**

层② 的判定是 **`VOID_TIE` 作废**, 不是 "no effect"。二者的区别是:

- "判定无害" = 我们测了, 挤占没影响 ⇒ 不用修 ⇒ 这条线可以关掉。
- "判定作废" = **量具失灵, 本轮没有产生任何关于挤占是否有害的信息** ⇒
  **我们仍然不知道挤占是否有害** ⇒ 这条线还开着, 只是要换把尺子重做。

**为什么必然是后者 —— 一条逻辑闭合的理由**:
`llm_judge_fact_recall.md:29` 记着全 140 题的 fact-recall 分布 —— **121/140 (86.4%) 本来就是
fr=1.0**, 仅 19 题有下探空间。这是**本实验开跑之前就已落库**的事实, 不是事后归因。
本轮按 `max_cluster` 挑的 11 题**一个有下探空间的都没有**, 于是 **A 组自己也是 1.00**。
**一把对所有臂都顶格的尺子, 在逻辑上无法区分"无效应"与"有效应"** —— B 组没有任何向上余量
可显示, 向下的 regressed 又要求答案漏掉 gold 关键词 (几乎不可能, §4.2)。
**所以本轮无论真相如何, 都必然产出 10/10 同分。**

**这条判定规则是在动手之前写死的**, 而且"两组都不过门槛"排在"同分题 ≥8 ⇒ 作废"**之后**。
最省事的读法本来是"两组都不过门槛 ⇒ 挤占无害 ⇒ 跳过 Task 7, plan 干净收尾"。
实现方照实报了作废。**判定规则先于数据写死, 是这件事能发生的唯一原因** (retro §关键决策)。

### 4.2 ⚠️ fact gold 的分辨力问题 —— 影响面超出本轮

**这 11 题的 33 条 `expected_facts` 里, 28 条 (85%) 是 1–2 个词的关键词碎片。**

```
q38:  'two-character' | 'DOMAIN'                 ← 字面就是这两个词
q104: '36' | 'Planned Study Day of Visit'
q39:  'Findings About' | 'FAOBJ'
q08:  'USUBJID' | 'Identifier' | 'unique'
q29:  'TA' | 'TE' | 'TV' | 'TI'
q81:  '2-character' | 'A-Z' | '0-9'
q108: 'C66729' | 'CM.CMROUTE' | 'EX.EXROUTE' | 'SU.SUROUTE'
q77:  'EPOCH' | 'Timing' | 'AE' | 'EX'
q07:  'EPOCH' | 'Timing'
q84:  'intervention' | 'event' | 'physiological effect'
q118: (唯一 4 条句子级事实)
```

一道问"域缩写码怎么分配"的题, **任何**像样的答案都必然出现 `two-character` 和 `DOMAIN`。
于是 q38 三组全部满分 —— **包括只有 3 席 context 的 B1**。语义 judge 在这种 gold 上
**退化成关键词在场检测**。

**旁证 (两把判据互相打脸)**: q38 在生产口径下 `expected_sources` recall = **0.3333**
(正确的 `ch04 §4.2.2` 被挤出 top-15), 而**同一条 context** 的 fact-recall = **1.00**。
同一道题, 源级说"三缺二", 事实级说"全覆盖" —— **后者显然不是在度量答案质量。**

> **推论 (必须写进下一轮的前提)**: **所有用 fact-recall 读出来的答案质量结论, 分辨力都存疑。**
> 这不限于本轮的 11 题 —— 86.4% 顶格是全 140 题的性质。历史上任何"fact recall 没变 ⇒ 没有回归"
> 的论证, 强度都不超过"关键词还在"。

> **别想当然的一条**: q118 是唯一有**句子级** gold 的题, **它同样三组同分**。所以
> "把 fact 改写成句子"这条换锚路线**本身尚未被证明够用 (n=1)**。下轮选锚必须先独立验证锚的
> 分辨力, 见 §6。

**用户裁定 (2026-08-07)**: 本轮**不修** fact gold, 只把这个问题写进收口证据 + kickoff。
换锚重做层② 归下一轮, 属新设计单元。

### 4.3 spec §0 的 28.6% 双重失效 (现值 23.6%)

`spec §0` 那张"挤占普遍性"表 (28.6% / 7.9% / 2.1% / 1.73 / 13.27) **两重失效**, 已在 spec
就地标注 (commit `4109732`), 此处呼应:

1. **含 `whole_file` 人造簇**: 40 题中 **5 题**的簇头就是它 (q14/q37/q40/q66/q86)。剔除后
   同口径 **27.1% (38/140)** —— 复算命令与原样输出见 §3(g)。
2. **已被重灌取代**: Task 8 的切分 + 重灌正是 `max_cluster` 豁免**自己明列的失效条件 3 与 4**。
   **现值 23.6% (33/140)**, 四组均值同步为 `max_cluster` 2.300→2.157 / `dup_seats`
   1.729→1.471 / `distinct_sections` 13.271→13.529。

**历史数字不改写** —— 改了就是伪造当轮实测。要引用挤占普遍性, **引 23.6%**;
要与 spec 表对照, 必须连"含人造簇"这一条一起带。

### 4.4 C2: chapters 页码溯源行不再进索引 (真实损失, 非零成本)

H2 切分从第一个 `## ` 开始, **首个 H2 之前的前言不进任何 chunk**。实测被丢弃的量:

```
ch01_introduction.md     86 B / 11058   '# SDTMIG v3.4 — Chapter 1: Introduction\n\nSource: SDTMIG v3.4, Section 1 (Pages 7-12)\n\n'
ch02_fundamentals.md     99 B / 18115   '# SDTMIG v3.4 — Chapter 2: Fundamentals of the SDTM\n\nSource: ... Section 2 (Pages 13-20)\n\n'
ch03_submitting_data.md 109 B / 19698   '# SDTMIG v3.4 — Chapter 3: ...\n\nSource: ... Section 3 (Pages 17-21)\n\n'
```

丢的是 **H1 标题 + 一行 `Source: ... (Pages N-M)` 页码溯源**, 合计 86/99/109 B。

**⚠️ 规则 A 抽检 (S6) 把这条的范围改大了 —— 本文初稿写窄了。**
实测全库: **4329 个 chunk 里, 含 `Source: SDTMIG` 的 = 0, 含 `Pages ` 的 = 0**。
ch04/ch08/ch10 (一直按 H2/H3 切) **从来就没有过**这行。

```bash
.venv/bin/python -c "
import chromadb
a=chromadb.PersistentClient(path='data/chroma').get_collection('sdtm_kb_v1').get(include=['documents'])
print('total', len(a['documents']),
      '| Source: SDTMIG', sum(1 for d in a['documents'] if 'Source: SDTMIG' in d),
      '| Pages ', sum(1 for d in a['documents'] if 'Pages ' in d))"
```

```
total 4329 | Source: SDTMIG 0 | Pages  0
```

**两种读法都要写下来, 因为它们指向不同的行动**:

- **抽检方的读法 (本轮改动无害)**: 本次只是把 ch01/02/03 **对齐到既有行为**, 不是新增一类损失。
  **这条成立**, 且它是判"切分改动无害"的正当理由。
- **但更该被记住的是那个更广的事实**: **RAG 索引里任何 chapter 都检索不到页码** ——
  这不是本轮造成的, 却是本轮才查清的。`page_index.json` 在 `CLAUDE.md` 里标着
  **authoritative**, 06 阶段做过**页码级 PDF→KB 深审**, 下一个做溯源的人**会默认索引里有页码**。
  **它一直没有。**

- **源 markdown 里这些行完整**, `knowledge_base/` 未被改动; 丢的只是索引侧。
- 章身份未丢: metadata `source` 保留章文件名, `server/rag.py:853` 拼 context 时写
  `### [{i}] {c.source} -- {c.section}`, 模型看得见章文件名与节名。
- 140 题零回归说明**当前题集**不依赖它, 但那是"没人问过", 不是"不重要"。
- 已同步到 `.work/MANIFEST.md` (Chain D 段) 与 `docs/PROGRESS.md`。
- **修法 (未做)**: chunker 里把前言 prepend 到首块 (块数仍为 5/9/3, 现有断言不受影响),
  或对**全部** chapters 统一注入溯源行 —— 后者才是解决那个更广的事实。

### 4.5 数字比它的适用条件传播得快 —— 本轮出现三次

这是本轮最系统的一类问题, 三次形态相同:

- **a. 99.29% 进了仓, 口径声明没进。** 数字随已提交的 JSON 入库 (commit `7c9ee68`), 而"换尺子
  不可比" + q126 三点声明只写在 **gitignored 且收尾会被 `rm -rf` 的 SDD workspace** 里。
  修法: 搬进已提交的 `gold_gap_verdicts.md`。(**这是 plan 的疏忽, 不是实施方的。**)
- **b. `max_cluster_section` 的禁忌写在 markdown, 而下游读的是 JSON。** "并列时簇头由排位决定,
  排位结论作废"这条写在三份外部文档里, 而 Task 6 读的是 `crowding_layer1.json`。
  修法: `max_cluster_section_tied` 标记落进 **JSON 本体** (71 题并列 / 69 题不并列)。
- **c. spec §0 的 28.6% 依赖的豁免已被击穿。** 见 §4.3。而本文 §3(a) 的"开工基线 859 还是 862"
  是**同一形态的第四次, 尚未闭合** —— 两处记录不一致且都没附命令, 故本文拒绝给精确增量。

**通用教训**: **数字与它的适用条件必须在同一个可提交的载体里**, 且**载体格式要与下游读取
方式一致** (下游读 JSON 就必须写进 JSON)。

### 4.6 kickoff §2.A 的根因描述是错的 (且是上一轮收口时写下的)

`NEXT_ROUND_KICKOFF.md` §2.A 把 q38 的根因写作 **"chapters/ 下 ≤20KB 的文件整个当一个 chunk,
语义被稀释"**。本轮实测推翻它 —— 详见 §2.3 与 kickoff 的订正段。
**根因被写进 kickoff 之前, 没有做过诊断验证。** 这条进 retro。

---

## 5. 已知限制全表

| # | 限制 | 影响面 | 状态 |
|---|---|---|---|
| L1 | **层② 判定作废, 挤占是否有害仍未知** | 段②2c / Task 7 | 换锚重做归下一轮 |
| L2 | **fact gold 85% 是关键词碎片** ⇒ 所有 fact-recall 结论分辨力存疑 | 全 140 题, 含历史结论 | 用户裁定本轮不修 |
| L3 | 句子级 gold 的分辨力**尚未被证明** (q118, n=1 也同分) | 下一轮选锚 | 换锚前须独立验证 |
| L4 | 层② n=11 是按 `max_cluster` 挑的极端样本 | 不可推广到 140 题 | 声明 |
| L5 | 层① 只认 **section 名字面**, 不认语义 | `whole_file` 曾被算成同质簇 (已查明) | 已标注 |
| L6 | 层① 排位结论**一律不可复现**; `dup_seats`/`distinct` 对 q47/q117 只能按分布引 | 层① 逐题数字 | `crowding_layer1.md` §2 |
| L7 | `max_cluster` 豁免是**有条件的** (条件 = churn 发生在簇内部), 且机制比表述窄 (q120 的 churn 跨出了 section 名, 它 `max_cluster` 没动是 2→2 的算术) | 引用豁免必须带失效条件 | `topk_jitter.md` §5.6 |
| L8 | 跨进程取样只验了 **16 题** (124 题未覆盖); `n_procs=20` 只是**检出下限**, 不足以刻画分布尾部 | 若有第二个 q47, 本轮看不见 | 声明 |
| L9 | **CDISC 140 题尺子接近饱和** —— 修完只剩 q38 (0.3333) 与 q126 (0.5) | 长期需要新题源 | 未排期 |
| L10 | **q126 未动检索** —— 原 known limit ("检索够不到 SE/assumptions.md、TE/spec.md") 仍成立 | 段① 只改了判据完整性这个独立维度 | 声明 |
| L11 | **C2 溯源损失** —— ch01/02/03 的页码行不再进索引 | 按页码溯源/答题 | 修法已写, 未做 |
| L12 | **剩 2 题**的 OR 成员严格弱于同组其他成员 (**q117 0/4 facts · q115 1/3**), 且它们的 OR 组是该题**唯一计分单位** ⇒ 只命中最弱成员即得 `source_recall = 1.0`。**q73 已在本轮改回 AND** (§7.1) | **动检索时会兑现** —— OR 组会吃掉回归让分数纹丝不动。**当前未虚高** (两题均已命中强成员) | **下轮动检索前必扫**。规则 A 抽检把 q19 排除 (它保留了 AND 成员, facts 分摊两侧, 不构成问题) |
| L20 | **OR 纪律第 1 条 ("每个成员独立覆盖全部 `expected_facts`") 在主题集上无任何自动闸** —— `eval/lint_gold.py` 是 study 轨的闸, 且第 66 行对 section 级 gold 直接 `raise`, **根本不作用于 `test_set_v3.yml`**; 其 `or_groups()` 注释明写"由人判" | 本轮该人工防线**未生效** (实现方只在拒绝时执行纪律, 自建 15 个 OR 组时未执行) | 规则 A 抽检查清; **下轮应补自动闸** |
| L21 | ~~q73 的处理与 q25 不一致~~ → ✅ **已解决 (§7.1)**: q73 改回 AND 与 q25 统一。**实测 140 题逐题 Δ0, 全集 0.9917 不变** (两成员本就都命中); 反事实实测证明判别力已买到 (只召回 VI 那一行: 旧 OR 1.0 → 新 AND 0.5) | — | DONE |
| L22 | **q68 的 `Completion Status` fact 在现 gold 下不可满足** —— 题干称 "the Completion Status codelist (C66789)", 而 KB 里 C66789 的码表名是 **`Not Done`**; `Completion Status` 是 `--STAT` 的**变量标签**, 只在 `VARIABLE_INDEX.md` §二 与各域 spec, 而这两处都不在 q68 的 gold 里 | **既有出题缺陷, 非本轮引入也未修复** | 单开条目跟踪 |
| L23 | **RAG 索引里任何 chapter 都检索不到页码** (全库 `Source: SDTMIG` / `Pages ` 命中数均为 **0**) —— 不是本轮造成的, 是本轮才查清的 | 页码溯源必须走源 md / `page_index.json` | 见 §4.4 + `.work/MANIFEST.md` |
| L13 | 8 个 OR 组保留路径级成员 (如 q46 的 `AE/spec.md`, 64 个 chunk 里 63 个不含答案却足以命中) | 判别力稀释 | 记 follow-up |
| L14 | gold 灰区 10 条维持原判 (含勉强判应补的 q39, 与字面命中但按"片段不算答案源"否掉的 q88/q122) | 段① | 记 follow-up |
| L15 | section 级 gold 20 → 49 (耦合面 ×2.45), 存在性闸只判"存在"**不判"对不对"** | gold 指到真实但错误的 section 照绿 | 已知缺口 |
| L16 | 扫描器口径 (hybrid/structured_lookup) **硬编码无 flag** | 生产口径若变会静默偏离 | 记 follow-up |
| L17 | 判定只对"这 182 条被召回过的条目"成立, **不能反过来当"其他 chunk 不该进 gold"的证据** | 未被 top-3 召回的正确源本轮扫不到 | 判定方边界声明 |
| L18 | 配额施加在 S1 **之前** ⇒ S1 前插不受配额约束, 可能把被挤走的同名 section **带回来** | q29 实证: B1 名义 cap=1 实际 3 席, **该题根本没拿到 cap=1 的处理** | 定死顺序 + 声明 |
| L19 | plan 规则表有空档: "两组都不过门槛且 regressed 为 2–3" 不落在任何一行 | 本轮未走到该分支 (实现按保守方向落"不修"并用单测钉死) | plan 缺陷 |

---

## 6. 下一轮入口

**换锚重做层②** (新设计单元, 归下一轮)。入口写在
`milestones/07_rag_kg/NEXT_ROUND_KICKOFF.md` §2.A′。

**零成本前置闸 (评审给的, 换锚前先跑)**:
> 换锚的前置不只是"锚在题集上方差 > 0", 还应**先在 A 组单臂上验** ——
> **如果 A 组自己就顶格, 任何 A/B 都不可能有信息。**
> 这条闸不需要跑 B 组, 不花 judge 的钱, 却能在开跑前排除整轮白做。

配套已就位: `server/diversity.py` 的 `apply_section_cap` + 单测, `eval/crowding_ab.py` 的
三组框架与 `--summarize` 重算路径, `eval/jitter_probe.py` 的跨进程取样。

---

## 7. 规则 A 语义抽检 (Step 1, 独立 agent)

抽样总体 = **本轮实际变更集合** (改动的 gold 条目 + 改动的检索行为 + 切分改动的三个 chapters
文件), **不是变更后全集**。N = **8**, 由**第三个** `subagent_type` 独立核验 (规则 D 隔离:
既非改 gold 方, 亦非实施方)。

**结果**: `sdtm-rag/evidence/step_09_audit.md` — **判定: 有条件 PASS (7/8 样本干净)**

**独立证实的 (未采信任何既有 JSON, 全新重跑)**:

- `source_recall_avg = 0.9917` 与仓内 `gold_integrity_after.json` **逐位相同** (四个 category 全同);
  **q38 仍 0.3333 / q126 仍 0.5 —— 两条已声明的限制独立证实为真, 未被粉饰**。
- 14 条依赖**注入抬头**的 gold, 正文依据**逐条属实**; 判定口径 (按 chunk 正文而非 KB 文件判) 正确。
- 两次"撤回 OR 改回 AND"的技术判定 (q46 / q38) **均经正文实测证实成立, 注释未夸大**:
  q46 的 `Perm` 不在码表 chunk 里 (`'Perm' in chunk -> False`); q38 的 §4.1.6 **全文不含**
  任何 `two-character`/`2-character` 变体而 §4.2.2 含 —— **两节确为互补**。
- chapters 切分**未切断任何语义单元** (逐块查边界; 含 mermaid 的 §2.6 完整落在一块内);
  `whole_file` 残留 = 0; 前言损失见 §4.4 (抽检把范围改大了)。
- 两道新闸**经变异测试证实会红** (改 section 名 → 按预期报出 q38/q43/q82), 且结构上强制复用
  `source_matches` 不自带第二份实现。**没红过的绿闸不是证据 —— 抽检自己做了变异。**

### ⚠️ 抽检发现的问题【中】: OR 纪律第 1 条**只在拒绝时执行, 在自建时未执行**

`check_source_recall` docstring 的纪律第 1 条要求 **"`any_of` 的每个成员必须独立覆盖全部
`expected_facts`"**。实现方对 q43/q45/q46/q59/q62 **正确执行了它** (拒绝并成 OR),
**却对自己新建的 15 个 OR 组未同样执行**。抽检机械扫描全部 15 组: 合格 7 / 不合格 8。

抽检**没有停在机械结果上**, 逐条读了成员正文后把结论分三层:

| 题 | 最弱成员覆盖 | 抽检判定 |
|---|---|---|
| q117 | 0/4 facts | 源判定**站得住** (ch04 §4.5.4 确实答了主问); 缺陷在 `expected_facts` 照 ch08 措辞逐字抄, **与单一源强耦合** ⇒ source 与 fact 判据会**系统性背离** |
| q115 | 1/3 | 同上 (SUPPQUAL/assumptions#overview 含 "For objective data, the value in QEVAL will be null." 直答题干) |
| q73 | 1/3 | **唯一真正语义弱的新增成员**。VI 那行只答"哪些域携带 RDOMAIN", 答不了"RDOMAIN 标识什么"。**且同形态的 q25 本轮补成 AND, q73 却补成 OR —— 同一轮内两种处理** |
| q34 / q68 | 1/2 · 2/3 | **既有缺陷, 非本轮引入**。q68 更值得单记: 题干称 "the Completion Status codelist (C66789)" 而 KB 里 C66789 的码表名是 **`Not Done`**, `Completion Status` 是 `--STAT` 的**变量标签** ⇒ **该 fact 在现 gold 下不可满足** |
| q19 / q91 / q126 | — | **判不构成问题**: 保留了 AND 成员, facts 分摊在两侧; 纪律第 1 条按字面套到"有 AND 成员的题"上过严 |

**为什么没被任何闸拦住 (机制层面, 抽检查清的)**: `eval/lint_gold.py` 是 **study 轨**的闸
(需要 card catalog), 且第 66 行对 section 级 gold 直接 `raise ValueError`, **根本不作用于
`test_set_v3.yml`**。它的 `or_groups()` 注释明写"语义上『每个成员能否独立回答该题』**由人判**"。
⇒ **纪律第 1 条在主题集上目前无任何自动闸, 唯一防线是人, 本轮该防线未生效。**

**对头条数字的影响: 无。** q117/q73/q115 当前实测**均已命中强成员**, 99.17% **未被虚高**
(命令 (c) 的 miss 列只有 q38/q126 可佐证)。问题在**未来** —— 检索一旦退化到只够着弱成员,
**分数不会掉**。这与 L12 是同一件事的两个发现路径 (L12 从"新成员严格弱于旧成员"看,
抽检从"成员是否独立覆盖 facts"看), 抽检的版本更准: **q19 应被排除, q34/q68 应被归为既有缺陷**。

### 抽检提的四条处置 — 前三条已做

| # | 条件 | 处置 |
|---|---|---|
| 1 | **q73 改 AND** (与 q25/q46/q59 统一) | ✅ **已做并实测**, 见下 §7.1 |
| 2 | q115/q117 在 yml 就地记明"facts 措辞绑定单一源, OR 成员命中时 fact_recall 会背离" | ✅ **已做** (`eval/test_set_v3.yml` 两处注释) |
| 3 | "纪律第 1 条在主题集上无自动闸"显式入档 | ✅ **已做** (本节 + §5 L20 + kickoff §2.D.4 列为下一轮候选) |
| 4 | q68 的 `Completion Status` 不可满足, 单开条目跟踪 | ✅ **已入档** (§5 L22 + kickoff §4), 非本轮引入, 不阻塞收口 |

### 7.1 q73 OR → AND: 实测分数变化 = **0**

**改动**: `expected_sources_any` → `expected_sources` (两成员不变), 与同形态的 q25 统一
(q25 = `MH/assumptions.md` + `MH/spec.md#MHTERM$`, 本轮即补成 AND)。

**复跑命令** (改前改后各跑一次全 140 题, 同一索引同一 session):

```bash
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml \
  --retrieval-only --hybrid --structured-lookup --output /tmp/q73_after_AND.json
```

原样输出 (逐题对照脚本见下方):

```
=== 全集 ===
  改前 (q73=OR) avg = 0.9917
  改后 (q73=AND) avg = 0.9917
  category 改前: {'concept': 0.9733, 'cross_domain': 0.99, 'mixed': 1.0, 'single_domain': 1.0}
  category 改后: {'concept': 0.9733, 'cross_domain': 0.99, 'mixed': 1.0, 'single_domain': 1.0}

=== 非满分题 ===
  改前: {'q38': 0.3333, 'q126': 0.5}
  改后: {'q38': 0.3333, 'q126': 0.5}

=== 逐题 recall 变化 ===
  有变化的题: 无 (0/140 题)

=== q73 改后 ===
  recall = 1.0
  hits   = ['model/06_relationship_datasets.md', 'VARIABLE_INDEX.md#§一 通用变量: RDOMAIN$']
  misses = []
```

**为什么不掉分**: 两个成员**本来就都命中** (`misses` 空)。所以这次改的是**判据的严格程度**,
不是这一题当前的检索表现。**分数不变 ≠ 改动没意义** —— 见下。

**判别力确实买到了 (反事实实测, 零 LLM 调用)**:

```bash
.venv/bin/python -c "
import sys; sys.path.insert(0,'.')
from eval.run_eval import check_source_recall
G=['model/06_relationship_datasets.md','VARIABLE_INDEX.md#§一 通用变量: RDOMAIN\$']
only_vi_src=['kb/VARIABLE_INDEX.md']; only_vi_sec=['§一 通用变量: RDOMAIN']
both_src=['kb/VARIABLE_INDEX.md','kb/model/06_relationship_datasets.md']
both_sec=['§一 通用变量: RDOMAIN', None]
for name,(s,sec) in [('只召回 VI 那一行',(only_vi_src,only_vi_sec)),('两源都召回',(both_src,both_sec))]:
    old=check_source_recall(s, [], G, sec)
    new=check_source_recall(s, G, None, sec)
    print(f'{name:16s}  旧(OR) = {old[0]:.4f}   新(AND) = {new[0]:.4f}')"
```

```
只召回 VI 那一行        旧(OR) = 1.0000   新(AND) = 0.5000
两源都召回             旧(OR) = 1.0000   新(AND) = 1.0000
```

⇒ **旧 OR 下两种情形同分 (不可区分); 新 AND 下 0.5 vs 1.0 (可区分)。**
这与 Task 3 段二对 q46/q59 做的实证同形: **判别力优先于分数**。

**已提交工件 `gold_integrity_after.json` 未重新生成, 且仍然有效** —— 它跑在 q73 改动**之前**,
但程序化核对确认: `summary` **零差异**, 逐题 `source_recall` / `source_hits` / `source_misses`
**零差异** (因为 q73 两成员在 OR 与 AND 下都命中, 计分路径不同而结果相同)。
**故意不覆盖**: 重跑会带来 `top5_similarities` 的抖动噪声 (`topk_jitter.md` 已量化),
把一个"结论零变化"的改动伪装成"工件变了"。核对命令:

```bash
.venv/bin/python -c "
import json
def load(p):
    with open(p, encoding='utf-8') as f: return json.load(f)
old=load('evidence/checkpoints/gold_integrity_after.json'); new=load('/tmp/q73_after_AND.json')
print('summary 差异:', [k for k in set(old['summary'])|set(new['summary'])
                     if old['summary'].get(k)!=new['summary'].get(k)] or '无')
o={r['id']:r for r in old['results']}; n={r['id']:r for r in new['results']}
f=['source_recall','source_hits','source_misses']
print('逐题差异:', [i for i in o if any(o[i].get(x)!=n[i].get(x) for x in f)] or '无')"
# summary 差异: 无
# 逐题差异: 无
```

> 逐题对照用的脚本 (从两份 JSON 重算, 不依赖任何中间结论):
> ```bash
> .venv/bin/python -c "
> import json
> def load(p):
>     with open(p, encoding='utf-8') as f: return json.load(f)
> b=load('/tmp/q73_before_OR.json'); a=load('/tmp/q73_after_AND.json')
> bb={r['id']: r['source_recall'] for r in b['results']}
> aa={r['id']: r['source_recall'] for r in a['results']}
> print('avg', b['summary']['source_recall_avg'], '->', a['summary']['source_recall_avg'])
> print('变化题:', {k for k in bb if bb[k]!=aa.get(k)} or '无 (0/140)')"
> ```

### 抽检自陈的两条

- **流程失误 (低)**: S7/S8 的变异测试直接 `sed` 改了仓内 `eval/test_set_v3.yml` 再复原,
  而当时另一 agent 正在并发编辑同一文件。**终态已核实无损** (变异无残留 `grep` 无输出;
  对方的指针修改完整保留; 三闸复跑 13 passed; 评测复跑 0.9917 与仓内一致)。
  **正确做法应是在 `/tmp` 副本上变异。** 抽检主动记录未掩饰。
- **未能核实的事项 (标了"⚠️ 无法从证据验证"而非写成断言 —— 正是硬规矩 10 要的)**:
  层② 判定作废的原始论证 / 跨进程抖动探针的统计充分性, 均不在 N=8 抽样内, **未独立核验**;
  且本抽检**同样受 `gold_gap_verdicts.md` §1.4 的边界限制** —— **不能反证 gold 现在完整**。

---

## 8. 落库产物清单

| 产物 | 路径 |
|---|---|
| 层① 结构探针 | `eval/crowding_probe.py` + `scripts/tests/test_crowding_probe.py` |
| 层② A/B 框架 | `eval/crowding_ab.py` + `scripts/tests/test_crowding_ab.py` |
| 配额实现 (生产侧, 未接线) | `server/diversity.py` |
| top-k 抖动探针 | `eval/jitter_probe.py` + `scripts/tests/test_jitter_probe.py` |
| 池深度探针 | `eval/pool_depth_probe.py` |
| gold 缺口扫描器 | `eval/scan_gold_gaps.py` + `scripts/tests/test_scan_gold_gaps.py` |
| **判据等价性差分对拍 (本轮归档)** | `eval/tests_support/gold_semantics_diff.py` |
| section gold 存在性闸 | `scripts/tests/test_section_gold_exists.py` |
| q38 gold 完整性锁 | `scripts/tests/test_gold_q38_integrity.py` |
| 判据共享实现 | `eval/run_eval.py::source_matches` (扫描工具共用同一份) |
| 分段证据 | `evidence/checkpoints/{crowding_layer1,crowding_layer2,topk_jitter,pool_depth_invariance,chapters_chunking,gold_gap_verdicts}.md` |
| 数据工件 | `evidence/checkpoints/{crowding_layer1,crowding_layer1_after_split,crowding_layer1_stability,crowding_layer2,crowding_layer2_dryrun,crowding_layer2_attribution,gold_integrity_after,chapters_split_after}.json` |
