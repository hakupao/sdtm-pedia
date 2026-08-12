# U2 Task 5 — router 语料描述改准 + 路由闸

> 单元: doc 轨 U2 接线 (plan `docs/superpowers/plans/2026-08-12-doc-track-u2-wirein.md` Task 5)
> spec: `docs/superpowers/specs/2026-08-12-doc-track-u2-wirein-design.md` §4.4 / §5.4 / §6 自毁条款 5
> 日期: 2026-08-12 · 全部数字为实测, 复跑命令见 §7
> 红线: 本文件只写数字与 qid, **不写任何题面 / 语料正文**。

---

## 1. 改了什么 (只有 `_ROUTER_SYSTEM` 里 study 那一条 bullet)

`server/federation.py` 的 `_ROUTER_SYSTEM`, **改前**:

```
- "study": ONE specific clinical study's EDC field cards — forms/screens, field labels, item \
groups, display conditions, units. Japanese EDC vocabulary.
```

**改后**:

```
- "study": ONE specific clinical study's own artifacts — its EDC field cards \
(forms/screens, field labels, item groups, display conditions, units) AND that study's own \
protocol / procedure document sections (手順・計画文書の節: eligibility, treatment schedule, \
assessments, statistical plan). Japanese content.
```

规则 1 / 2 / 3 的正文与优先级、cdisc bullet、结尾的 JSON 输出指令**一个字节未动**
(`git diff server/federation.py` = 4 insertions / 2 deletions, 全部落在这一条 bullet 内)。

## 2. 路由闸 (spec §5.4 判据: `exact ≥ 178/181` 且 `fatal = 0`)

| | exact | acc | fatal | fallback | 三遍一致 |
|---|---|---|---|---|---|
| 改前基线 (`routing_run_{1,2,3}_u2pre.json`) | 178/181 ×3 | 98.34% | 0 | 0 | 181/181 |
| 改后 (`routing_u2_run{1,2,3}.json`) | **179/181 ×3** | **98.90%** | **0** | **0** | **181/181** |

**判据: PASS** (179 ≥ 178, fatal = 0)。自毁条款 5 未触发, prompt 不回滚。

### 2.1 逐题差异 (不是只比总分)

三遍**各自**与对应的 `routing_run_{i}_u2pre.json` 逐题比对 (181 题 id 集合先断言相等):

| run | 判库变了的题数 | 变化 | 判定 |
|---|---|---|---|
| 1 | **1** | `st_st01_v11_q22`: gold=study, pre=`both` → post=`study` | **FIX** |
| 2 | **1** | 同上 | **FIX** |
| 3 | **1** | 同上 | **FIX** |

- 另外 180 题三遍**逐题零漂移**。
- 新增 fatal: **无** (spec §5.4 要求"新增 fatal 逐题列名" —— 无可列)。
- 改后仍错的 2 题 (两者都是 `both`, 非致命, 与改前同一批):
  `q124` (gold=cdisc, pred=both) · `st_st01_v11_q17` (gold=study, pred=both)。
- 改前错的 3 题 = 上面 2 题 + `st_st01_v11_q22`; 即本次改动**只修不坏**。

## 3. doc 30 题判库 (单独报, **不并入 181 的分母**)

| | study | cdisc | both | fallback | non-study 名单 |
|---|---|---|---|---|---|
| 改前 (controller 实测, n=1 遍) | 25 | 5 | 0 | 0 | `docs_v1_q05 q15 q17 q53 q55` |
| 改后 (n=1 遍) | **27** | **3** | 0 | **0** | `docs_v1_q15 q17 q53` |

- 修好 2 题: `docs_v1_q05` · `docs_v1_q55` (cdisc → study)。
- 未修好 3 题: `docs_v1_q15` · `docs_v1_q17` · `docs_v1_q53` 仍判 cdisc。
- ⇒ doc 侧端到端**判库天花板** 25/30 = 83.3% → **27/30 = 90.0%**。剩下 3 题在生产档
  (`corpus=auto`) 下 recall 结构性归零, 与检索/席位无关 (Global Constraint 6: 这部分损耗
  记在**判库损耗**账上, 不许算进接线损耗)。
- ⚠ 只跑了 **1 遍** (与改前基线口径相同, 可比)。181 题闸三遍全稳, 但这 30 题的**稳定性未测**。

## 4. 变异测试 (Global Constraint 7 + 12: 两个方向都做)

口径: 每条变异**单独**施加于 `server/federation.py`, 跑**全量** `pytest -p no:warnings`,
记 failed, 立刻按原始字节复原并核验 sha256 (`RESTORED True`)。
harness: 私有子目录 `<scratchpad>/task5/mutate.py` (Global Constraint 11), 每轮子超时 600s,
收尾打印 `FINAL RESTORED True sha=b7a20ea3ef562258 vs base b7a20ea3ef562258`。
本轮期间的 pytest 总数从 1154 涨到 1155/1156 (并发 agent 在同期合入了自己的测试), 故
**只看 failed 与变红的测试名**, 不看 passed 总数。

### 4.1 方向① — 从新断言出发, 找能杀死它的变异

| # | 变异 | 期望 | 实测 | 变红的测试 |
|---|---|---|---|---|
| M1 | study bullet 整段回滚到 U2 之前 | ≥1 | **1 failed** | `test_router_prompt_describes_the_study_document_corpus` |
| M2 | 只删掉手順書章节那半句 (卡片描述保留) | ≥1 | **1 failed** | 同上 |
| M3 | 只删掉 field cards 那半句 (手順書保留) | ≥1 | **1 failed** | 同上 |
| M4′ | study bullet 回滚, 但把 `protocol / procedure document sections` 字样塞进 **cdisc** bullet | ≥1 | **1 failed** | 同上 |

M4′ 是本条断言**写法**的实证: 计划原文给的断言是
`assert "protocol" in _ROUTER_SYSTEM.lower()` (整段 prompt)。该写法**在改动之前就已经是绿的** ——
规则 1 的正文里本来就有 `"our protocol"` 这个例子 (改前 prompt 里 `protocol` 唯一一次出现在
下标 918)。⇒ 照抄计划 = 加一条**恒绿装饰品**。实际实现把断言范围**缩到 study 那一条 bullet**
(`split("Decide which corpus")[0].split('- "study":')[1]`), M1-M4′ 四条才都能杀死它。

### 4.2 方向② — 从代码行出发问「这行改坏了谁会红」

| # | 变异 (改的是**没人守**的行) | 实测 | 结论 |
|---|---|---|---|
| M5 | 删掉规则 3 (`"both"` 兜底规则) 整段 | **0 failed** (1155 passed) | 零覆盖 |
| M6 | `Rule 2 outranks rule 1` → `Rule 1 outranks rule 2` (优先级反写) | **0 failed** | 零覆盖 |
| M7 | 结尾 JSON 输出指令改成 `Respond however you like.` | **0 failed** | 零覆盖 |
| M8 | `route_corpus` 送出的 system 换成空串 (**prompt 常量正确, 但根本没送出去**) | **0 failed** | 零覆盖 → 已补断言 |
| M9 | `route_corpus` 送出的用户问题换成空串 | **0 failed** | 零覆盖 → 已补断言 |

M8/M9 是方向②的实际收获: 方向①**结构上不可能发现**它们 —— 断言只看常量文本, 而这两条
改的是"常量有没有被用"。补断言 `test_route_actually_sends_the_router_prompt_and_the_question`
后复验:

| # | 复验 (补断言后) | 实测 | 变红的测试 |
|---|---|---|---|
| M8 | 同上 | **1 failed** | `test_route_actually_sends_the_router_prompt_and_the_question` |
| M9 | 同上 | **1 failed** | 同上 |
| M10 | system / user 两条消息**顺序对调** (补断言后新加的变异) | **1 failed** | 同上 |

### 4.3 已知这条断言看不见什么 (硬规矩 19 — 引用本条绿灯时必须同写)

1. **它是关键词级, 不是语义级**。实测 (harness id `M4-protocol-moved-to-cdisc-bullet`, 该条
   构造时**写错了位置** —— 名字说塞进 cdisc bullet, 实际把字样附在了 **study bullet 尾部**):
   study bullet 回滚成 U2 之前, 尾部附一句 "(protocol / procedure document sections live
   elsewhere)" —— 语义与本改动**完全相反**, 而断言**照绿** (**0 failed / 1155 passed**)。
   构造错误反而暴露了断言的真实上界: 它只能防"字样整个丢了", 防不了"字样在但说反了"。
   位置正确的那条重跑于 round B, 即 §4.1 的 M4′ (红)。
2. **M5/M6/M7 三处仍是零覆盖** —— 规则 1/2/3 的正文、优先级句、JSON 输出指令, 改坏了 pytest
   一条都不红。本 task **未**补这三处的断言: 逐字钉死 prompt 措辞会把每次合法调 prompt 都变成
   改测试的噪声, 而它们的真闸是 `eval/run_routing_eval.py` 的 181 题三遍 (LLM, **不在 pytest 里**,
   须人工跑)。⇒ **任何改 `_ROUTER_SYSTEM` 的改动, 全量 pytest 绿都不构成证据, 必须跑路由闸。**
3. 30 题判库只跑 1 遍, 其稳定性无数据 (§3)。

## 5. 全量 pytest

- 本 task 开工前基线: **1 failed / 1153 passed** (那 1 条红是并发 agent 在 in-flight 的
  `test_main_study_docs_wiring.py::test_docs_engine_shares_every_lever_with_the_cards_engine`, 非本 task)。
- 本 task 收尾: **1156 passed / 0 failed** (含本 task 新增 2 条; 并发 agent 的红已由其自行修好)。

## 6. 自毁条款检查

- **条款 5** (`fatal > 0` 或 `exact < 178/181` ⇒ 回滚 prompt): 实测 fatal=0, exact=179/181
  ⇒ **未触发**, prompt 保留。
- 其余条款不在本 task 范围。

## 7. 复跑命令 (逐字)

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag

# §2 路由闸 (181 题 ×3 遍, 约 6 分钟, 走 Bedrock light 模型)
./.venv/bin/python -m eval.run_routing_eval --runs 3
# 逐题比 (把 routing_run_{i}.json 与 routing_run_{i}_u2pre.json 比; 本次结果已另存 routing_u2_run{i}.json)
./.venv/bin/python -c "
import json
for i in (1,2,3):
    L=lambda p:{x['id']:(x['gold'],x['pred']) for x in json.load(open(p))['detail']}
    pre=L(f'data/study/st01/eval/runs/routing_run_{i}_u2pre.json')
    post=L(f'data/study/st01/eval/runs/routing_u2_run{i}.json')
    assert set(pre)==set(post)
    print(i, [(k,pre[k][0],pre[k][1],post[k][1]) for k in pre if pre[k][1]!=post[k][1]])"

# §3 doc 30 题判库
./.venv/bin/python -c "
import yaml, collections, sys; sys.path.insert(0, '.')
from server.config import settings
from server.federation import route_corpus
from server.llm_config import create_router
qs = yaml.safe_load(open('data/study/st01/eval/test_set_docs_v1.yml'))
r = create_router(settings)
out = [(q['id'], route_corpus(r, q['question'])) for q in qs]
print(collections.Counter(c for _, (c, f) in out))
print('fallback:', sum(f for _, (c, f) in out))
print('non-study:', [(i, c) for i, (c, f) in out if c != 'study'])"

# §4 计划原文那条断言在改动前就是绿的 (装饰品实证; 需先 git stash 本 task 的 federation.py 改动)
./.venv/bin/python -c "
from server.federation import _ROUTER_SYSTEM as S
print('protocol in whole prompt:', 'protocol' in S.lower())
sb = S.split('Decide which corpus')[0].split('- \"study\":')[1]
print('protocol in study bullet:', 'protocol' in sb.lower())"

# §5 全量
./.venv/bin/python -m pytest -p no:warnings
```
