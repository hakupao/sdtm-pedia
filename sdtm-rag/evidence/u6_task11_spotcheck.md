# U6 Task 11 — 答题侧 spot-check (auto 档, 信号层 off vs on)

> 日期: 2026-08-18
> 执行目录: `sdtm-rag/` (以下命令逐字可复跑, 全部用 `./.venv/bin/python`)
> git rev (六个 run 全部产自此 sha): `2012258` — 跑批前后 `git status --porcelain` 均空,
> 无 `-dirty`, 即这批数字可凭 sha 复现。
> ⚠ 跑批之后本 task 走过一轮审查修复环 (§12 后两条 + 回执串), **不影响这批产物**:
> 新加的闸只拦 `--signal-layer on` + **强制**判库, 而本轮六个 run 用的是 `--corpus auto`
> (修复后仍有专门测试钉住该组合可跑); 回执串只进 gitignored 日志, 不进产物。
> 性质: spec §5.3 的 spot-check。**不是**全矩阵重跑 (那属「放宽 router」新单元, U5 §8 边界原样)。
> 上游状态: Task 10 全闸 `rc=1` (条款 1 触发), 用户裁定**保留信号层**, 单元按诚实 FAIL 收口。
> 本 task 因此测的是「一个已判 FAIL 的修法, 在答题侧到底带来了什么」。
> 红线: 本文件进 git, 只记统计值 / 题号 / 判库取值 / 命令 / rc —— 零题面, 零真实试验标识符。

---

## 0. 一句话结论 + 读法条款

**`rc=0`, `verdict_word = cost_reported`** —— 已确证代价与已确证收益**各 1 题, 各 2.08pt,
恰好抵消** (paired_net = 0.00pt), 可比池 = 稳定配对 45/48 (全 parse_ok 48/48)。

- **收益题 `st01_v2_q07`** (本轮**唯一**判库改判题): `cdisc`→`both` 三遍稳定,
  source_recall 0.0→1.0, judge 0.0→1.0 三遍稳定。判库欠账在这一题上**端到端修好了**。
- **代价题 `st01_v11_q23r`**: judge 1.0×3 → 0.0×3。但 §6 的输入同一性核验表明
  **这一题两臂的检索输入相同** (判库同为 `study`, 未被信号层触碰) —— 详见 §6 与 §13-1。

**读法条款 (进本文件任何引用)**:

1. `verdict_word` 是**唯一**判词信号。本文件里的任何 pt 读数都不是结论词。
2. 判词与代价额**只引顶层 E1**。`E1.stable_half` 带 `caliber: u5_stable_only_subset`
   标记, 是 U5 稳定半口径的**子集**, 单独摘引会把有代价的批次读成无代价 (本轮两者恰好同值,
   因为两题都同时满足稳定配对与支配, `dominance_only_ids` 为空 —— 这是**本轮的巧合**, 不是规律)。
3. 引本轮任何 pt, 必须同句写「可比池 45/48」。
4. `st01_v2_q07` 属路由 gold 的 **final 组 = 条款 5「只报告不作判据」**。§5 是单题点名,
   **不构成**「信号层修好了判库欠账」的总体结论 —— 全闸的答案是 Task 10 的 rc=1。
5. `aggregate` 与 `paired_net` 两把尺子本轮**不可读作「一致」**, 见 §10 (脚本报
   `divergent_readings=false`, 但那是 paired_net 恰为 0 造成的判定盲区, 不是两尺同向)。

---

## 1. 跑批 (逐字命令)

```bash
cd sdtm-rag
for i in 1 2 3; do for ARM in off on; do
./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --hybrid --study-lookup --federated --corpus auto --study-docs --judge --temperature 0 \
  --full-answers --signal-layer $ARM \
  --output "data/study/st01/eval/runs/u6_spot_cards_${ARM}_r${i}.json" \
  > "data/study/st01/eval/logs/u6/cards_${ARM}_r${i}.log" 2>&1
done; done
```

答题命令与 U5 Task 5 逐字同源 (U5 plan Global Constraint 6), 两处差异都是本单元定义的:
`--corpus auto` (U5 是强制 `study`/`both`) 与 `--signal-layer $ARM` (本 task 新增, §12)。
`--full-answers` 是 §2 rejudge 探针的前置。跑批日志含题面, 只在 `data/study/st01/eval/logs/u6/`
(gitignored)。

**跑批中断如实记账**: 前 3 个 run (off_r1 / on_r1 / off_r2) 由上述循环跑完后, 承载该循环的
后台进程被外部**杀掉** (`[killed]`, 非脚本报错; 当时 on_r2 跑到 51 题中的第 13 题, **未落任何
产物** —— run json 只在跑完时整体写出)。余下 3 个 run (on_r2 / off_r3 / on_r3) **在同一 sha
`2012258`、同一干净工作树下逐个重启跑完**。因此六份产物同源可比; 唯一后果是跑批时刻不连续
(见下表 mtime)。这不是「重跑追数字」: 被杀那次没有产物, 无从取舍。

### 1-1 出处 (per-run provenance)

| run | `summary.signal_layer` | judge_model | n_q / n_total / oos | parse_fail | judge_avg | src_avg | routing | 产物 mtime (UTC) |
|---|---|---|---|---|---|---|---|---|
| off r1 | `off` | deepseek/deepseek-chat | 48 / 51 / 3 | 0 | 0.8542 | 0.8542 | study 45 · both 5 · cdisc 1 | 2026-08-18T05:57:08 |
| off r2 | `off` | deepseek/deepseek-chat | 48 / 51 / 3 | 0 | 0.8819 | 0.8542 | study 45 · both 5 · cdisc 1 | 2026-08-18T06:29:58 |
| off r3 | `off` | deepseek/deepseek-chat | 48 / 51 / 3 | 0 | 0.8819 | 0.8542 | study 45 · both 5 · cdisc 1 | 2026-08-18T07:16:32 |
| on r1 | `on` | deepseek/deepseek-chat | 48 / 51 / 3 | 0 | 0.8611 | 0.8750 | study 45 · both 6 | 2026-08-18T06:13:26 |
| on r2 | `on` | deepseek/deepseek-chat | 48 / 51 / 3 | 0 | 0.8715 | 0.8750 | study 45 · both 6 | 2026-08-18T06:59:45 |
| on r3 | `on` | deepseek/deepseek-chat | 48 / 51 / 3 | 0 | 0.8507 | 0.8750 | study 45 · both 6 | 2026-08-18T07:33:15 |

⚠ **出处口径限定**: `eval/run_eval.py` 的产物**没有** `generated_at` / `git_rev` 键
(那是 `run_routing_eval.py` 的 `meta`, Task 1 的 A-3 修缮只做了路由侧)。因此上表「跑批时刻」
用的是**文件 mtime**, 它会被下一次同名跑批直接抹掉。臂别本身则是产物自证的
(`summary.signal_layer`, 本 task 新增), 不靠文件名。**这是本轮的仪器缺口**, 记 §13-2。

产物验收 (12 条断言, 六份全过):

```bash
./.venv/bin/python -c "
import json, itertools
for arm, i in itertools.product(('off','on'), (1,2,3)):
    p = f'data/study/st01/eval/runs/u6_spot_cards_{arm}_r{i}.json'
    d = json.load(open(p)); s = d['summary']
    assert s['n_questions'] == 48 and s['n_total'] == 51
    assert s['judge_model'] == 'deepseek/deepseek-chat'
    assert s['signal_layer'] == arm
    assert s['federated'] is True and s['study_lookup'] is True
    assert s['top_k'] == 15 and s['hybrid']['fusion'] == 'rrf'
    assert all('answer' in r for r in d['results'] if not r.get('out_of_scope'))
    assert all('routed' in r and 'routed_fallback' in r for r in d['results'])
    assert sum(s['routing'].values()) == 51
print('ALL 6 OK')"                                     # → ALL 6 OK
```

### 1-2 三遍是真重采样, 不是缓存重放

| 检查 | 实测 |
|---|---|
| off 臂三遍答案逐字相同 | **0 / 51** |
| on 臂三遍答案逐字相同 | **0 / 51** |
| off r1 vs on r1 逐字相同 | 2 / 51 |

(同 U5 §2.1 的检查口径。`--temperature 0` 下答案仍逐遍不同 = Bedrock 侧非确定性, 与 U5 一致。)

---

## 2. rejudge 探针 (I-1 输入)

```bash
./.venv/bin/python -m eval.rejudge_run \
  data/study/st01/eval/runs/u6_spot_cards_on_r1.json \
  data/study/st01/eval/test_set_study_v2.yml \
  --output data/study/st01/eval/runs/u6_spot_probe_cards.json
# → rejudge n=48 same=47 same_rate=0.9792 orig_parse_fail=0 rejudge_parse_fail=0
```

协议同 U5 §8 (取 ON 臂 r1 一份重判)。`same_rate 0.9792 ≥ 0.95` ⇒ **I1 PASS**, 结论词不降级。
⚠ U5 §5-7 的限定原样适用且**本轮更该说**: 探针只覆盖 6 份答案集里的 1 份; 且 U5 那次是 1.0,
本轮 48 题里有 1 题重判不复现 —— judge 侧不再是零噪声, 只是仍在阈值内。

---

## 3. 判定 (frozen `eval/u6_answer_verdict.py`)

```bash
R=data/study/st01/eval/runs
./.venv/bin/python -m eval.u6_answer_verdict \
  --arm-a $R/u6_spot_cards_off_r1.json $R/u6_spot_cards_off_r2.json $R/u6_spot_cards_off_r3.json \
  --arm-b $R/u6_spot_cards_on_r1.json  $R/u6_spot_cards_on_r2.json  $R/u6_spot_cards_on_r3.json \
  --family cards --probe $R/u6_spot_probe_cards.json \
  --output $R/u6_spot_verdict.json
```

完整 stdout (逐字):

```
E1 cost 2.08pt ['st01_v11_q23r'] | gain 2.08pt ['st01_v2_q07']
   dominance=['st01_v11_q23r', 'st01_v2_q07'] (其中支配独有 []) 可比池: 稳定配对 45 / 全 parse_ok 48
E4 gate_pass=True n_union=3/9 ['st01_v11_q19', 'st01_v2_q14', 'st01_v2_q18']
I1 {'same_rate': 0.9792, 'n': 48, 'n_orig_parse_fail': 0, 'pass': True}
aggregate=-1.16pt (n=48) vs paired_net=0.0pt  divergent_readings=False
verdict_word=cost_reported suppressed_by=[]
rc=0
```

### 3-1 顶层 E1 (引用只许引这一格)

| 项 | 值 |
|---|---|
| `confirmed_cost_pt` / ids | **2.08pt** / `['st01_v11_q23r']` |
| `confirmed_gain_pt` / ids | **2.08pt** / `['st01_v2_q07']` |
| `dominance_ids` | `['st01_v11_q23r', 'st01_v2_q07']` |
| `dominance_only_ids` | `[]` (两题同时满足稳定配对与支配 ⇒ 两把尺子本轮不分家) |
| 可比池 | 稳定配对 **45/48** · 全 parse_ok **48/48** |
| `verdict_suppressed_by` | `[]` |

`E1.stable_half` (子集口径, `caliber=u5_stable_only_subset`): cost 2.08pt `[q23r]` /
gain 2.08pt `[q07]` / `n_compared=45` —— 与顶层同值**纯属本轮巧合**, 不得据此认为两口径等价。

### 3-2 独立复算 (异源写法, Fraction 精确算术)

不复用 `u5_verdict` 的任何函数, 自写稳定性/配对/支配/聚合四段:

```bash
./.venv/bin/python -c "
import json
from fractions import Fraction as F
def rows(a,i):
    d=json.load(open(f'data/study/st01/eval/runs/u6_spot_cards_{a}_r{i}.json'))
    return {r['id']:(F(str(r['judge_fact_recall'])) if r.get('judge_parse_ok') else None)
            for r in d['results'] if not r.get('out_of_scope')}
A=[rows('off',i) for i in (1,2,3)]; B=[rows('on',i) for i in (1,2,3)]
ids=sorted(A[0]); assert all(sorted(m)==ids for m in A+B)
def stable(M):
    st,un={},[]
    for q in ids:
        v=[m[q] for m in M]
        (un.append(q) if (None in v or len(set(v))!=1) else st.__setitem__(q,v[0]))
    return st,sorted(un)
sa,ua=stable(A); sb,ub=stable(B); common=set(sa)&set(sb)
cost={q:sa[q]-sb[q] for q in common if sa[q]>sb[q]}
gain={q:sb[q]-sa[q] for q in common if sb[q]>sa[q]}
dom_c,dom_g={},{}
for q in ids:
    va=[m[q] for m in A]; vb=[m[q] for m in B]
    if None in va or None in vb: continue
    if max(vb)<min(va): dom_c[q]=sum(va)/3-sum(vb)/3
    elif max(va)<min(vb): dom_g[q]=sum(vb)/3-sum(va)/3
allc=dict(cost); allc.update(dom_c); allg=dict(gain); allg.update(dom_g)
print('n_compared',len(common),'union',sorted(set(ua)|set(ub)))
print('cost',sorted(allc),float(100*sum(allc.values())/48))
print('gain',sorted(allg),float(100*sum(allg.values())/48))
ok=[q for q in ids if all(m[q] is not None for m in A+B)]
print('aggregate',float(100*sum(sum(m[q] for m in B)/3-sum(m[q] for m in A)/3 for q in ok)/len(ok)))
print('paired_net',float(100*(sum(allg.values())-sum(allc.values()))/48))"
```

| 项 | 脚本 | 独立复算 | 一致 |
|---|---|---|---|
| n_compared | 45 | 45 | ✅ |
| E4 union | `[q19, q14, q18]` | `[q19, q14, q18]` | ✅ |
| cost ids / pt | `[q23r]` 2.08 | `[q23r]` 2.0833333… | ✅ |
| gain ids / pt | `[q07]` 2.08 | `[q07]` 2.0833333… | ✅ |
| dominance ids | `[q23r, q07]` | `[q23r, q07]` | ✅ |
| aggregate pt | −1.16 | −1.1574305… | ✅ |
| paired_net pt | 0.0 | 0.0 | ✅ |

（controller 自算属**自洽复算**, 不替代规则 D 的抽检方 A —— Task 12 仍须独立方复算。）

---

## 4. 逐题判库差分 (观测, 覆盖全部 51 题)

Task 10 的 widen 统计是在**路由 gold** 上做的。路由 gold 与本 task 答题集的覆盖关系
(按 id 交集, 并逐条比对题面字符串是否逐字相同, 只打计数不打内容):

| 答题集 | 与路由 gold 的 id 交集 | 题面逐字相同 | 落在哪些组 |
|---|---|---|---|
| cards `test_set_study_v2.yml` (51 题) | **1 / 51** | 1 / 1 | final ×1 (`st01_v2_q07`) |
| docs `test_set_docs_v1.yml` (30 题) | **30 / 30** | 30 / 30 | u1_doc ×27 + final ×3 |

⇒ **Task 10 对 cards 侧 50/51 题的判库行为没有任何观测**。所以本 task 不沿用推断,
直接从六份产物的逐题 `routed` 字段读差分:

```bash
./.venv/bin/python -c "
import json
R='data/study/st01/eval/runs/u6_spot_cards'
def routes(a):
    return [{r['id']: r['routed'] for r in json.load(open(f'{R}_{a}_r{i}.json'))['results']}
            for i in (1,2,3)]
off, on = routes('off'), routes('on')
ids = sorted(off[0])
diff  = [(q, [m[q] for m in off], [m[q] for m in on]) for q in ids
         if {m[q] for m in off} != {m[q] for m in on}]
drift = [q for q in ids if len({m[q] for m in off}) > 1 or len({m[q] for m in on}) > 1]
fb = {a: sorted({r['routed_fallback']
                 for i in (1,2,3)
                 for r in json.load(open(f'{R}_{a}_r{i}.json'))['results']})
      for a in ('off','on')}
n_rows = sum(len(json.load(open(f'{R}_{a}_r{i}.json'))['results'])
             for a in ('off','on') for i in (1,2,3))
print('n_questions', len(ids))
print('两臂 routed 不同:', len(diff), [(q, o, n) for q, o, n in diff])
print('三遍内 routed 漂移:', len(drift), drift)
print('routed_fallback 取值集:', fb, '总行数', n_rows)"
```

逐字输出 (只有题号与判库取值, 零题面):

```
n_questions 51
两臂 routed 不同: 1 [('st01_v2_q07', ['cdisc', 'cdisc', 'cdisc'], ['both', 'both', 'both'])]
三遍内 routed 漂移: 0 []
routed_fallback 取值集: {'off': [False], 'on': [False]} 总行数 306
```

| 项 | 实测 |
|---|---|
| 两臂 routed 不同的题 | **1 / 51**: `st01_v2_q07` `['cdisc','cdisc','cdisc']` → `['both','both','both']` |
| 三遍内 routed 漂移的题 | **0 / 51** (两臂各自三遍逐位恒定) |
| `routed_fallback` 取值集 | 两臂均 `[False]`, 共 **306** 行 |

⇒ 控制器给出的前提 (「唯一改判题是 `st01_v2_q07`」) **在 cards 侧被直接观测证实**,
而不再只是 1/51 覆盖率下的推断。off 臂的判库分布 (45 study / 5 both / 1 cdisc) 逐位复现
U5 §2.3 与 U3 §4.1 —— 信号层 off 确实等于旧基线。

⚠ **`fallback` 全 False 的引用限定 (U5 §9-5, 本轮再次坐实)**: 306 行全 False, 但 off 臂的
`st01_v2_q07` 正是判 `cdisc` 且 gold 零命中的**路由打空**题, fallback 一次都没响 ——
**fallback 只捕获异常, 不捕获错判**。「全 False」不得读作「路由健康」。

---

## 5. `st01_v2_q07` — 本轮唯一改判题 (逐题三遍两臂对照)

| 臂 | routed ×3 | source_recall ×3 | judge_fact_recall ×3 |
|---|---|---|---|
| off | `cdisc` / `cdisc` / `cdisc` | 0.0 / 0.0 / 0.0 | **0.0 / 0.0 / 0.0** |
| on | `both` / `both` / `both` | 1.0 / 1.0 / 1.0 | **1.0 / 1.0 / 1.0** |

判库拓宽 ⇒ gold 从零命中变全命中 ⇒ 答案从判 0 分变判满分, **三遍稳定, 支配关系成立**
(`max(off)=0.0 < min(on)=1.0`)。这是「判库欠账 → 答题损失」这条因果链在单题上的**首次
端到端闭合观测** (U5 只能观测到检索侧零命中, 答题侧当时未测)。

**单题点名不下总体结论** (读法条款 4): 该题属条款 5「只报告」组; 全闸结论是 Task 10 的
`rc=1`。本节**不能**用来主张信号层通过或该保留 —— 用户裁定保留是另一回事。

---

## 6. `st01_v11_q23r` — 在池检查 (U5 §9-6) + 输入同一性核验

**先答 U5 §9-6 要求的那个问题**: q23r **在本轮池里**, 且不在 E4 不可判池 ——
它是本轮**唯一的已确证代价题**。(该题是 cards v2 计分题, 不是 docs 题;
「本轮 docs 臂没跑所以 q23r 不在池」的说法与题集事实不符, 见 §8 脚注。)

| 臂 | routed ×3 | source_recall ×3 | judge ×3 | top5_sources | top5_similarities |
|---|---|---|---|---|---|
| off | `study` ×3 | 0.0 ×3 (2 miss) | **1.0 / 1.0 / 1.0** | 三遍同 | r1 与 r2/r3 差 ≤1e-4 |
| on | `study` ×3 | 0.0 ×3 (2 miss) | **0.0 / 0.0 / 0.0** | 与 off 逐条相同 | 与 off r2/r3 逐位相同 |

**输入同一性核验 (主证据 = 机制, 不是指纹比对)**:

1. **主证据 — 信号层只经 `decide_corpus` 一个入口**: `server/federation.py` 全文里
   `self.signals` 除 `__init__` 赋值外**只出现一次** (`:189`, 传进 `decide_corpus`),
   它**不进** `self.cdisc.retrieve` / `self.study.retrieve` / `format_context` /
   `build_messages` 任何一个。`decide_corpus` 对下游的唯一产出是 `routed`
   (其余两个返回值 `fallback` / `widened` 只写观测属性)。
   ⇒ **两臂 `routed` 相同 ⇒ 走的是同一条分支、同样的实参**, 检索输入**在构造上**相同,
   system prompt 也相同 (`build_messages` 按本题 routed 取 corpus)。
   复核命令: `grep -n "self\.signals\|signals" server/federation.py` (行号见上)。

   ```bash
   ./.venv/bin/python -c "
   import json
   R='data/study/st01/eval/runs/u6_spot_cards'
   q='st01_v11_q23r'
   for a in ('off','on'):
       v=[next(r for r in json.load(open(f'{R}_{a}_r{i}.json'))['results'] if r['id']==q)
          for i in (1,2,3)]
       print(a, [x['routed'] for x in v], [x['source_recall'] for x in v],
             [x['judge_fact_recall'] for x in v])"
   # → off ['study','study','study'] [0.0,0.0,0.0] [1.0,1.0,1.0]
   # → on  ['study','study','study'] [0.0,0.0,0.0] [0.0,0.0,0.0]
   ```

2. **佐证 (弱, 不作主证据)**: `top5_sources` 两臂逐条相同, `top5_similarities` 与
   off r2/r3 逐位相同 (off r1 有 ≤1e-4 浮点抖动), source_recall 两臂同为 0.0 且缺同 2 条 gold。
   ⚠ **这层只能是佐证**: run json 只落 **top5**, 而本轮 `top_k=15` —— 第 6-15 位的
   chunk 从不进产物, 指纹相同**不能**证明 15 条全同。真正把它钉死的是第 1 条的机制,
   指纹只是与机制一致的旁证。

⇒ 这 2.08pt「代价」**在机制上不可能由信号层产生**; 它是一道双峰题在两臂各自三遍里
恰好落到相反的稳定值上 (答案文本三遍全不同, §1-2)。

**纪律声明**: 以上是机制观测, **不改判词**。`verdict_word=cost_reported` 与
`confirmed_cost_ids=['st01_v11_q23r']` 照原样成立并进本文件 §3 —— 判定脚本是冻结件,
本 task 不改、不豁免、不把该题移出代价集。这条观测的用途是交 Task 12/13:
**支配尺子对双峰题存在假阳性路径**, 见 §13-1。

q23r 至此**第四次**出现 (U2 条款 3 驱动题 → U5 E4 不可判池 → 本轮已确证代价题)。

---

## 7. 检索侧脆弱 4 题 (E3 式逐题点名)

四题在**两臂各三遍共 24 次判库中全部判 `study`** —— 与 U5 §2.3「脆弱 4 题 auto 下 12/12
全判 study」同向, 样本翻倍后仍成立。

| 题号 | off ×3 | on ×3 | 池归属 | 读法 |
|---|---|---|---|---|
| `st01_v11_q19` | 1.0 / 1.0 / 1.0 | 1.0 / 1.0 / **0.5** | **E4 不可判** (on 臂不稳) | 不得下任何逐题结论 |
| `st01_v2_q14` | **0.6667** / 1.0 / 1.0 | 1.0 / 1.0 / 1.0 | **E4 不可判** (off 臂不稳) | 同上 |
| `st01_v2_q15` | 0.6667 ×3 | 0.6667 ×3 | 稳定配对池 | 两臂同分, 无代价无收益 |
| `st01_v2_q21` | 1.0 ×3 | 1.0 ×3 | 稳定配对池 | 同上 |

四题的 source_recall 两臂均为 1.0 ×3 (q19/q14/q15/q21 全命中), 即**本轮 auto 档下这 4 题的
检索侧脆弱性未在答题侧显形**。⚠ 与 U5 不可比: U5 的 q14/q21 读数出自**强制 both 档**
(反事实), 本轮是 auto 档 (生产触发面), 两者口径不同, 互比大小任何方向都错。

---

## 8. docs 侧: 构造上 Δ0 (未跑臂, 记账)

**docs 两臂没有跑**, 依据是 Task 10 的逐题 pred 差分:

- 路由 gold 覆盖 docs 答题集 **30/30**, 且 30 条题面与答题集**逐字相同** (§4 表)。
- Task 10 观测到的 widen 只有 2 条: `u3_doc_02` (heldout 组, 不在 docs 答题集内) 与
  `st01_v2_q07` (final 组, cards 题)。docs 答题集所属的 u1_doc 27 题与 final 3 题
  **widen 计数三遍全 0**。
- ⇒ docs 30 题在 off / on 两臂下**判库逐题相同**; 判库是信号层唯一能改的东西
  (widen-only, 不动 `_ROUTER_SYSTEM`) ⇒ **检索输入逐题相同 ⇒ 构造上 Δ0**。

⚠ **「构造上 Δ0」不等于「实测 Δ0」**: 若真跑 docs 双臂, 答题侧仍会出现非零逐题差 ——
本轮 §6 正好量出了这种差能有多大 (输入完全相同的一题, 两臂稳定差 1.0 分 = 2.08pt)。
所以「docs Δ0」只许写成**检索输入层面的构造性结论**, 不许写成「docs 侧信号层无代价」。

（脚注: 派单说明里「q23r 因 docs 臂未跑而不在池」的前提不成立 —— q23r 是 cards v2 计分题,
本轮在池且是唯一代价题, 见 §6。此处如实记录以免下游沿用错误前提。）

---

## 9. E4 并集 vs 闸

| 项 | 值 |
|---|---|
| off 臂不稳定 | `['st01_v2_q14', 'st01_v2_q18']` (2) |
| on 臂不稳定 | `['st01_v11_q19', 'st01_v2_q18']` (2) |
| **并集** | `['st01_v11_q19', 'st01_v2_q14', 'st01_v2_q18']` (**3**) |
| 闸 (cards) | ≤ **9** (spec §4.3 冻结, = 20% × 48) |
| 判定 | **PASS** (3/9), rc 不受影响 |

**Task 5 carry-forward ③「Task 11 消费前确认 concat 变异已死」— 本轮闭合**:
本批**本身就是活判别 case**。两臂各 2 题不稳定, 重叠 1 题 (`st01_v2_q18` 两臂都不稳),
故集合并集 = **3** 而 `sorted(unstable_a + unstable_b)` 的双计口径 = **4**。
两者都 ≤9 不改本轮判定, 但**产物数字不同** ⇒ 这批数据能区分两种实现 (若脚本是 concat,
上面表里那格会写 4)。闸响侧则由
`test_e4_union_deduplicates_overlapping_ids_at_the_gate_boundary` 钉死 (闸边界构造:
去重 9 = PASS vs concat 11 = 假触发不可判)。**活判别 + 边界测试两侧齐备, 该 carry-forward 关闭。**

并集 3 题 = 6.25% —— 显著低于 U5 的 14.6% (U5 §5-2 点名「并集从未被闸」, 本轮该闸已存在
且实际生效判 PASS)。⚠ 两批不可直接比: U5 是强制 study/both 两档, 本轮是 auto 同档双臂,
档内噪声本就更小。

---

## 10. 两把尺子并列 + `divergent_readings` 的判定盲区

| 尺子 | 值 | 口径 |
|---|---|---|
| `aggregate_mean_diff_pt` | **−1.16pt** (n=48) | 全 parse_ok 池的三遍均值差 (on − off), 负 = ON 更低 |
| `paired_net_pt` | **0.00pt** | 已确证 (gain − cost) / 48 = (1.0 − 1.0)/48 |
| `divergent_readings` | **false** | — |

**这里必须读清楚**: `divergent=false` **不代表两把尺子同向**。脚本的判据是
`abs(agg) > eps and abs(net) > eps and sign(agg) != sign(net)`; 本轮 `net` 恰为 **0**,
合取项第二半为假 ⇒ 无论 `agg` 是什么符号都判 false。也就是说 **paired_net 恰好为 0 的批次
天然逃过分歧检测** —— 而「代价与收益各一题恰好抵消」正是最容易出现 net=0 的形态。

聚合口径的 −1.16pt 落在哪: 它含被 E1 排除的 3 道不可判题, 也含所有稳定同分题;
off 臂三遍 judge_avg 0.8542/0.8819/0.8819 (mean 0.8727, 极差 2.77pt),
on 臂 0.8611/0.8715/0.8507 (mean 0.8611, 极差 2.08pt) —— **同配置跨遍极差 (2.77pt) 大于
两臂均值差 (1.16pt)**, 即聚合口径本轮承载不了这个量级的结论 (U5 §2.4 同款教训)。

source_recall 侧则是干净的: off 0.8542 ×3 / on 0.8750 ×3, **两臂各自三遍零方差**,
差 +2.08pt, 全部来自 `st01_v2_q07` 一题 (§5)。

---

## 11. spec §5.4 指标 (docs 侧 auto vs 强制 study 的 source_recall 差)

**本 task 未测**: 该指标要求 docs 侧 auto 档与强制 study 档对跑, 而本轮 docs 双臂未跑
(§8), 强制档更是没跑。cards 侧 auto 的 source_recall 为 off 0.8542 / on 0.8750,
**不能**替代该指标 (不同题集、无强制档对照)。此项交 Task 13 记为未闭合。

---

## 12. 代码改动 (本 task 唯一改动面)

commit `2012258` — `eval/run_eval.py` 加 `--signal-layer {off,on}` 透传:

- 默认 `off` = 逐位同加 flag 之前 (`signals=None`, `build_signals` 根本不导入不调用)
- `on` 经**生产同款工厂** `server.routing_signals.build_signals(settings, study_lookup=...)`
  构造, 并**复用 `--study-lookup` 那一份 S2** —— 与 `server/main.py` lifespan 同口径
  (那里的注释: 不造第二份, 因为两份可以来自不同文件而信号层那份从不出现在日志里)
- 工厂返回 `None` 拒绝跑批 (否则 summary 写着 `on` 的一批数字其实是 off)
- 非联邦下给 `--signal-layer on` = usage error (rc=2)
- **强制判库下给 `--signal-layer on` = usage error** (审查修复环 1): 强制档不经
  `decide_corpus` ⇒ 信号层整层惰性, 而 summary 与回执照样写 `on` —— 那是**假标签面**,
  一批信号层从未通电的数字事后与真 on 臂一字不差。`--corpus auto` (本轮跑批用的组合)
  与强制档 + `--signal-layer off` (U5 矩阵用的组合) 都照样跑得动, 各有测试钉住。
- **联邦回执打命令行真给的 corpus** (审查修复环 1): 原先硬编码 `corpus=auto`,
  强制档跑批的屏幕与日志因此自称 auto —— 而那正是 U5 拆「判库损耗 vs 接线损耗」的开关。
- `summary.signal_layer` + 屏幕回执各留一处出处

**冻结件零改动**: `server/routing_signals.py` (信号层定义) 与 `eval/u5_verdict.py` /
`eval/u6_answer_verdict.py` / `eval/u6_gate_verdict.py` (判定脚本) 一字未动。

测试: `scripts/tests/test_run_eval_federated.py` **+13 wiring test** (首轮 9 + 修复环 4);
`scripts/tests/test_run_eval_doc_channel.py` 的 `_fed` 桩签名跟随真构造器加 `signals`
(不加则 `TypeError`, 5 个既有测试红 —— 这正是接线测试该有的响应)。

四道 guard / 回执各做过**变异验杀** (改坏 → 目标测试 FAILED, 恢复 → 全绿):

| 变异 | 被杀的测试 |
|---|---|
| 删 `--signal-layer` 非联邦那行 `parser.error` | `test_signal_layer_requires_federated` |
| `raise SystemExit` → `pass` (工厂返 None) | `test_signal_layer_on_refuses_a_none_factory_result` |
| 删强制档那行 `parser.error` | `test_signal_layer_on_rejects_a_forced_corpus` |
| 回执改回硬编码 `corpus=auto` | `test_federated_receipt_prints_the_real_corpus` |

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=short | tail -2   # 1641 → 1654 passed
```

---

## 13. 已知限制 (每条注明它看不见什么)

### 13-1 判定设计类 (交 Task 12/13, 本 task 不改冻结件)

1. **支配尺子对双峰题有假阳性路径** (本轮 §6 实证): 一道题在两臂**输入完全相同**时,
   仍可能各自三遍稳定落在相反值上, 于是被判「已确证代价/收益」。n=3 下, 一道 p≈0.5 的
   双峰题出现这种 3/3 相反形态的概率约 1/32。**看不见**: 代价集合里哪些是机制性的、
   哪些是采样巧合 —— 判定产物本身不区分, 必须靠逐题输入同一性核验 (本文件 §6 是手工做的,
   脚本没做)。
2. **`divergent_readings` 在 `paired_net == 0` 时天然失效** (§10): 而「代价收益各一题抵消」
   恰是最常见的 net=0 形态。**看不见**: 本轮 aggregate(−1.16pt) 与 paired(0.00pt) 的读数
   落差 —— 脚本报 `false`, 只有人读 §10 才知道那不是「两尺同向」。
3. **`dominance_only_ids` 为空是本轮巧合**: 两把口径不分家纯属两题都同时满足两个条件。
   **看不见**: 该字段在本轮没有判别力, 不能据此说「支配尺子与稳定半一致」。

### 13-2 仪器 / 出处类

4. **`run_eval` 产物无 `generated_at` / `git_rev`** (§1-1): Task 1 的 A-3 修缮只覆盖了
   `run_routing_eval`。**看不见**: 产物自身无法证明跑批时刻与 sha, 只能靠 mtime (可被覆盖)
   与本文件的记账。臂别本身已自证 (`summary.signal_layer`)。
5. **产物不落 `widened_by`**: 本文件 §4 的改判判定走的是**两臂 `routed` 差分**, 与 Task 10
   的 pred 差分同一形态。**看不见**: 「判库漂移伪装成同形状」在原理上排除不掉 —— 支撑只有
   「两臂各自三遍 routed 逐位恒定」这一观测 (51/51 × 2 臂)。
6. **rejudge 探针只覆盖 6 份答案集里的 1 份** (U5 §5-7 原样), 且本轮 same_rate 从 U5 的
   1.0 掉到 0.9792。**看不见**: 其余 5 份答案集上的 judge 行为。
7. **检索非逐位可复现**: `st01_v11_q04` / `st01_v2_q01` / `st01_v2_q12` 三题的 top5_sources
   在遍与遍之间漂移 (near-tie 的排序抖动), **与臂无关** (off 臂自身三遍也漂), 三题分数
   全程 judge=1.0 / src=1.0 未受影响。**看不见**: 这种抖动在其它题上是否曾改过分数。

### 13-3 覆盖类

8. **只测 cards 一侧 48 题, 一个模型一个温度一个 judge** (Bedrock sonnet 答题 / deepseek
   judge temp 0)。换模型可能翻转。
9. **spot-check 范围外的题未测** (spec §8 预登记): 不能说答案质量整体变好或变差。
10. **docs 侧是构造性结论不是实测** (§8)。
11. **spec §5.4 顶层指标未闭合** (§11)。

---

## 14. 本单元/本 task 明确不能证明什么

- **不能**说「信号层在答题侧净收益/净代价」—— 顶层判词是 `cost_reported`,
  代价与收益各 1 题恰好抵消, 且代价题经核验输入未被信号层触碰 (§6), 收益题属条款 5 只报告组 (§5)。
- **不能**拿 §5 的 q07 单题结果论证「判库欠账修好了」—— 全闸结论是 Task 10 `rc=1`,
  8 条 fatal 三遍原样仍在。
- **不能**拿 −1.16pt 的聚合读数下结论 (同配置跨遍极差 2.77pt > 该差, §10)。
- **不能**对 E4 的 3 道不可判题 (`q19` / `q14` / `q18`) 任一单题下结论。
- **不能**说「docs 侧实测无代价」(未跑, §8); **不能**说「fallback 全 False = 路由健康」(§4)。
- **不能**把本轮 auto 档数字与 U5 强制 both 档数字互比 (口径不同, §7)。
- **放宽 router 仍是新单元** (U5 §9-4 原样)。

---

## 15. 复跑命令 (逐字, 在 `sdtm-rag/` 下)

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=no | tail -2      # → 1654 passed
R=data/study/st01/eval/runs
# 判定 (确定性, 只读已落盘产物; 答题 run 非确定, 重跑数字会变)
./.venv/bin/python -m eval.u6_answer_verdict \
  --arm-a $R/u6_spot_cards_off_r1.json $R/u6_spot_cards_off_r2.json $R/u6_spot_cards_off_r3.json \
  --arm-b $R/u6_spot_cards_on_r1.json  $R/u6_spot_cards_on_r2.json  $R/u6_spot_cards_on_r3.json \
  --family cards --probe $R/u6_spot_probe_cards.json --output $R/u6_spot_verdict.json   # rc=0
```

run 产物与探针均 gitignored 本地件 (`data/study/` 下); 缺失时按 §1 / §2 命令重生成。

---

## 16. 本文件泄漏自检

```bash
./.venv/bin/python scripts/leakscan_evidence.py evidence/u6_task11_spotcheck.md --min-len 12
```

### 16-1 逐字输出

```
target      : evidence/u6_task11_spotcheck.md
needles     : 306 条 question (6/6 个 gold set 可读)
                eval/test_set_v3.yml: 140 条
                eval/routing_gold_ja_supplement.yml: 16 条
                data/study/st01/eval/test_set_study_v1_1.yml: 27 条
                data/study/st01/eval/test_set_study_v2.yml: 51 条
                data/study/st01/eval/test_set_docs_v1.yml: 30 条
                data/study/st01/eval/routing_gold_docs.yml: 42 条
rule        : stride=4, min_len=12, 原文匹配 (不折叠大小写)
CLEAN: 0 条 question 片段出现在目标文件 (min_len=12)
rc=0
```

needle **6/6 完整** (无 `--allow-missing`), 故 CLEAN 可信。

### 16-2 阈值敏感性 (引用 CLEAN 必须连阈值一起写)

`--min-len 8` 下报 **LEAK 17 条**, 但 17 条**全部来自 `eval/test_set_v3.yml`**
(英文 CDISC 公开题集), 片段为 `controll` ×6 / `ontrolle` ×4 / `nstraint` ×2 /
`question` / `summary ` / `allback ` / ` is not ` / `upplemen` —— 即脚本 docstring
明载的**通用英文词形假阳性**类。其中 `upplemen` 命中的是**本文件 §16-1 里逐字抄录的
扫描器自身输出**那行 gold set 文件名 (`routing_gold_ja_supplement.yml`), 与题面无关。
`data/study/` 下四个 gold set (真实试验内容) 在 min_len=8 下命中 **0 条**。

复核命令 (按来源分组数命中):

```bash
./.venv/bin/python scripts/leakscan_evidence.py evidence/u6_task11_spotcheck.md \
  --min-len 8 --show 20 | grep -E "yml:" | sort | uniq -c | sort -rn
```

补充 kana 扫描 (中文正文不含假名, 日文题面必含):

```bash
grep -c -P '[\x{3040}-\x{309F}\x{30A0}-\x{30FF}]' evidence/u6_task11_spotcheck.md   # → 0
```

