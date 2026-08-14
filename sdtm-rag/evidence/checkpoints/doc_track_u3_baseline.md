# U3 T3 — 改动前基线冻结 (253 题 × 3 遍)

> 单元: doc-track U3 语料路由 (spec `docs/superpowers/specs/2026-08-13-doc-track-u3-corpus-routing-design.md`)
> 日期: 2026-08-14 · 分支 `doc-track-u3` · 代码 HEAD `046b1b9`
> 状态: **基线已冻结**。本文件记录的是**改 prompt 之前**的数字。
> 数据红线: 本文件只含 question id 与数字, 逐题明细 (含题面) 只在 gitignored 的
> `data/study/st01/eval/runs/u3_baseline_run_{1,2,3}.json`。

## 0. 为什么这一步必须先于修法

spec §6.2 防线 1: **gold 与基线必须先于 prompt 冻结**。基线若在修法之后才测,
「改进了多少」就可以被重新定义。本文件即该冻结点。

## 1. 跑批条件

| 项 | 值 |
|---|---|
| 命令 | `./.venv/bin/python -m eval.run_routing_eval --runs 3` |
| 判库模型 | `light` = `bedrock/converse/jp.anthropic.claude-haiku-4-5-20251001-v1:0` |
| temperature | 0 (`server/federation.py::route_corpus`) |
| `server/federation.py` sha256 | `b7a20ea3ef562258ac682603a1967d55710488a4ad5eae40569bb68f59e0f7c9` |
| 题量 | 253 (legacy 181 + u1_doc 27 + final 3 + dev 12 + heldout 12 + distractor_cdisc 12 + ambiguous_both 6) |
| fallback 次数 | 0 / 0 / 0 (三遍均无异常兜底, 数字不是 fallback 污染出来的) |

## 2. ⚠ rc=1 是预期, 不是跑批失败

三遍**均**打 `FAIL(条款1)`, 进程 `rc=1`。**这是设计**: 此刻 prompt 未改。
spec §7 已写死「T3 基线跑批必定 FAIL 且 rc=1 …… T3 的产出是落盘的基线数字, 不是绿灯」
(同 U2 §7 对 `run_eval` 的注)。**看到红不许去修它。**

实测输出 (三遍逐字):

```
run 1: legacy 179/181 (floor 178)  fatal_excl_final=10  fallback=0  FAIL(条款1)
         groups: legacy:179/181  u1_doc:27/27  final:0/3  dev:12/12  heldout:11/12  distractor_cdisc:7/12  ambiguous_both:0/6
         fatal ids: ['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_amb_06', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11', 'u3_doc_02']
run 2: legacy 179/181 (floor 178)  fatal_excl_final=10  fallback=0  FAIL(条款1)
         groups: legacy:179/181  u1_doc:27/27  final:0/3  dev:12/12  heldout:11/12  distractor_cdisc:7/12  ambiguous_both:0/6
         fatal ids: ['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_amb_06', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11', 'u3_doc_02']
run 3: legacy 179/181 (floor 178)  fatal_excl_final=10  fallback=0  FAIL(条款1)
         groups: legacy:179/181  u1_doc:27/27  final:0/3  dev:12/12  heldout:11/12  distractor_cdisc:7/12  ambiguous_both:0/6
         fatal ids: ['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_amb_06', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11', 'u3_doc_02']
stability: 253/253 题三遍判定一致
rc=1 (1 = 未达标, 不是跑批失败)
```

## 3. 六条条款的基线数字

准确率口径同 spec §7: `pred == gold` 精确匹配; gold=`study` 而判 `both` **算错**。

| # | 条款 | 基线口径 | 三遍值 (r1 / r2 / r3) | 该组多数类基线 | 基线下条款状态 |
|---|---|---|---|---|---|
| 1 | fatal=0 **且** legacy exact ≥ 178 | `fatal_excl_final` / `legacy_exact` | **10 / 10 / 10** ; **179 / 179 / 179** | legacy 83.4% (151/181) | **未达标** (legacy 半边已满足, fatal 半边差 10) |
| 2 | heldout ≥ dev − 25.0pt | `heldout` exact/12 | **11 / 11 / 11** (91.7%) | **100%** (12/12 全 study) | 已满足 (gap = −8.3pt) — 但见 §5 |
| 3 | dev ≥ 10/12 | `dev` exact/12 | **12 / 12 / 12** (100%) | **100%** (12/12 全 study) | 已满足 — 但见 §5 |
| 4 | 干扰题较改动前下降 ≤ 1 题 | `distractor_cdisc` exact/12 | **7 / 7 / 7** (58.3%) | 100% (12/12 全 cdisc) | **基线即 7/12 ⇒ 改后须 ≥ 6/12** |
| 5 | q15/q17/q53 只报告, 不作 PASS 条件 | `final` exact/3 + 各自 pred | **0 / 0 / 0** — 三题三遍**全部 `pred=cdisc`** (gold=study) | 100% (3/3 全 study) | 报告项, 不参与判定 |
| 6 | 连跑 3 遍, 不一致的题点名 | 三遍判定一致题数 | **253 / 253** | — | 见 §4 |
| — | 参考组 | `u1_doc` exact/27 | **27 / 27 / 27** (100%) | 100% (27/27 全 study) | — |
| — | 参考组 | `ambiguous_both` exact/6 | **0 / 0 / 0** (0%) | 100% (6/6 全 both) | 6 题全 fatal |
| — | 合计 | exact / 250 (excl final) | **236 / 236 / 236** (94.4%) | 65.2% (163/250 cdisc) | — |

### 条款 4 的冻结值

**`distractor_cdisc` 改动前 = 7/12 (三遍一致)。** 条款 4 的「改动后 ≥ 基线 − 1」
⇒ 改后阈值 **≥ 6/12**。此数字随本文件冻结, 不许在看到改后结果之后重新测算。

### 基线判错逐题 (id 级, 三遍一致)

| group | id | gold | pred (r1/r2/r3) | 是否 fatal |
|---|---|---|---|---|
| legacy | `q124` | cdisc | both ×3 | 否 (both 不致命) |
| legacy | `st_st01_v11_q17` | study | both ×3 | 否 |
| final | `docs_v1_q15` | study | cdisc ×3 | 豁免 (条款 5) |
| final | `docs_v1_q17` | study | cdisc ×3 | 豁免 (条款 5) |
| final | `docs_v1_q53` | study | cdisc ×3 | 豁免 (条款 5) |
| heldout | `u3_doc_02` | study | cdisc ×3 | **是** |
| distractor_cdisc | `u3_dist_04` | cdisc | both ×3 | 否 |
| distractor_cdisc | `u3_dist_05` | cdisc | both ×3 | 否 |
| distractor_cdisc | `u3_dist_07` | cdisc | study ×3 | **是** |
| distractor_cdisc | `u3_dist_10` | cdisc | study ×3 | **是** |
| distractor_cdisc | `u3_dist_11` | cdisc | study ×3 | **是** |
| ambiguous_both | `u3_amb_01`…`u3_amb_06` | both | study ×3 (6 题全同) | **是** ×6 |
| dev (12) / u1_doc (27) | — | — | 全对 | — |

fatal 合计 10 = 6 (`u3_amb_01..06`) + 3 (`u3_dist_07/10/11`) + 1 (`u3_doc_02`)。

## 4. 三遍稳定性 (条款 6)

**三遍全一致** —— 253/253 题在三遍中判定完全相同, 不一致 id 清单为**空**。

命令与实测输出:
```bash
cd sdtm-rag && ./.venv/bin/python -c "
import json
runs = [json.load(open(f'data/study/st01/eval/runs/u3_baseline_run_{i}.json')) for i in (1,2,3)]
preds = [{d['id']: d['pred'] for d in r['detail']} for r in runs]
ids = sorted(preds[0])
unstable = {i: [p[i] for p in preds] for i in ids if len({p[i] for p in preds}) > 1}
print('unstable:', len(unstable)); [print(' ', k, v) for k, v in unstable.items()]
"
# 输出: unstable: 0
```

`temperature=0` 下三遍零抖动与预期一致; 这也意味着改动后的差异**不能**被归因于采样噪声。

## 5. ⚠ 这份基线**不能**证明什么

### 5.1 条款 2 与条款 3 在基线上就已满足

(dev 12/12, heldout 11/12, gap −8.3pt) 叠加 spec §7.1 已记的「两组多数类基线均 100%」,
这两条判据在本单元里**既无判别力, 也无可展示的余量** —— 修法对它们最好的结果只是持平。
⇒ **引用条款 2/3 的数字时必须同时给出条款 1 与条款 4** (spec §7.1 处置第 1 条)。

### 5.2 ⛔ 已撤回: ~~「欠账在非豁免题上只测到 1 例」~~

**本条已于 2026-08-14 撤回 —— 由 Task 6 独立审阅推翻, 本人复算确认。正确读法见 §5.2a。**

> **撤回原文** (保留而非删除, 本仓惯例: 「怎么错的」比「结论是什么」更值得留):
> ~~「手順書题被判去公开标准库」这个欠账, 在非豁免题上只测到 1 例。
> 51 道非豁免手順書型题 (u1_doc 27 + dev 12 + heldout 12) 里基线判错 **1 题**
> (`u3_doc_02`); U1 的 27 题 **0 例**。真正大面积错的是 `ambiguous_both` 0/6 与
> `distractor_cdisc` 5/12 错。这两个形状与本单元立项时描述的欠账不是同一件事。~~
>
> **错在哪 (两根支柱都塌了)**:
> 1. **「u1_doc 27/27」是循环论证**, 却被放进了分母 51。
> 2. **「新写 24 题只错 1 题」没有统计功效**, 却被当成了否证。
>
> 数字本身属实且未改动; 被撤回的是从数字推出的**结论**。
> ⚠ **「51 道判对 50」这个分母作废, 不许再用** —— 改用两个可比数字分开报:
> **U1 30 题 27/30** 与 **新写 24 题 23/24**, 并注明前者的 27 是循环选出来的。

### 5.2a 正确读法 (修订, 2026-08-14)

**(a) `u1_doc` 27/27 对「失效形态的基率」零信息 —— 它是按结果选出来的子集。**
`run_routing_eval.py` 的 `FINAL_IDS` 把 U2 已实测判错的三题切出去,
剩下的 27 题**恰好就是 U2 实测判对的那 27 题**。从 U2 产物直接可证:

```bash
cd sdtm-rag && ./.venv/bin/python -c "
import json
d=json.load(open('data/study/st01/eval/runs/u2_ruler3_prod.json'))
print('U2 routing:', d['summary']['routing'])
print('U2 非满分题:', sorted(r['id'] for r in d['results'] if r['source_recall']<1.0))
"
```
```
U2 routing: {'study': 27, 'cdisc': 3}
U2 非满分题: ['docs_v1_q15', 'docs_v1_q17', 'docs_v1_q53']
```
⇒ `u1_doc` = 30 题减去「已知会错的 3 题」= **已知会对的 27 题**。
拿它去估「手順書型被判去 cdisc 的比率」是**在结果上做选择**。

⚠ 精确一点 (与审阅口径的一处细化): 27/27 **并非完全零信息** ——
它证明这 27 题相对 U2 **没有回归**。零信息的是它对**失效形态基率**的贡献,
而 §5.2 撤回原文正是拿它去估基率的。

**⇒ 正确口径: 在 U1 那 30 题上基线是 `27/30`, 三题全部 `study → cdisc`,
与 spec §1.1 完全同向 —— 本次基线一比一复现了 U2, 没有推翻它。**

**(b) 「新写 24 题只错 1 题」没有统计功效, 不构成否证。**
唯一真正新增的证据是 **23/24**。与 U1 的 3/30 相比:

```bash
cd sdtm-rag && ./.venv/bin/python - <<'PY'
from math import comb
a,b,c,d = 3,27,1,23                      # [[3,27],[1,23]]  U1 vs 新写 24
n1,n2,K,N = a+b, c+d, a+c, a+b+c+d
probs = {k: comb(n1,k)*comb(n2,K-k)/comb(N,K) for k in range(K+1) if K-k <= n2}
obs = probs[a]
print('fisher two-sided p =', round(sum(p for p in probs.values() if p <= obs+1e-12), 4))
for pr in (0.05, 0.10, 0.15, 0.20):
    print(f'P(X<=1 | n=24, p={pr:.2f}) =',
          round(sum(comb(24,k)*pr**k*(1-pr)**(24-k) for k in (0,1)), 4))
PY
```
```
fisher two-sided p = 0.6204
P(X<=1 | n=24, p=0.05) = 0.6608
P(X<=1 | n=24, p=0.10) = 0.2925
P(X<=1 | n=24, p=0.15) = 0.1059
P(X<=1 | n=24, p=0.20) = 0.0331
```
⇒ 两组失败率**在统计上无法区分** (p = 0.62); 且**即使真实失败率就是 10%**,
24 题中出 ≤1 例的概率仍有 **0.29**。n=24 连 10% → 4% 都分辨不了。
**「只错 1 题」不是否证, 只是没有功效。**

**(c) ⇒ 基线给了 §1.1 第 4 个独立实例, 且是盲写的。**
`u3_doc_02` 与三道豁免题**同向** (`study → cdisc`), 且与 `docs_v1_q17` / `q53`
**同属第 3 章** (元数据, 非题面):

```bash
cd sdtm-rag && ./.venv/bin/python -c "
import yaml
from pathlib import Path
d=yaml.safe_load(Path('data/study/st01/eval/routing_gold_docs.yml').read_text('utf-8'))
print([(q['id'], q['chapter']) for q in d if q['id']=='u3_doc_02'])
"
# [('u3_doc_02', 3)]
```
出题方**未接触路由器、未被告知失效形态** (spec §5.3 隔离) ⇒ 这一例的证据强度**高于**前三例。
**基线加强了 §1.1, 不是推翻了它。**

**(d) `ambiguous_both` 0/6 不等于「路由器不会输出 `both`」。**
全 253 题里 `pred=both` 共 **9 次**, 且 `legacy` 组 5 道 `gold=both` 的题 **5/5 全对**。
失效是**局限于新写的这 6 题**的: 它们被整齐地拉去了 `study` (6/6 全 `pred=study`)。
与此同时有 **4 次 `both` 误报** (`q124` / `st_st01_v11_q17` / `u3_dist_04` / `u3_dist_05`,
gold 均非 `both`)。⇒ 现象是**「`both` 给错了地方」而非「不会给 `both`」**,
两者指向的病因不同, 请勿按后者去改 prompt。

**(e) ⛔ 不得把这两组的错误率外推成「路由器过度偏向 study」** (本文件初版这么写过, 已撤回):
`distractor_cdisc` 与 `ambiguous_both` **都是对抗构造题**, 其错误率**按构造就该高** ——
出题方 (`task-4-report.md` §2) 自己声明: 干扰组「目标是一旦有人为了让手順書型判对而放宽规则,
这 12 题必须开始判错」, 且刻意去掉了 `ja_supplement` 保留的标准侧概念词, **原理上比它更脆**;
`ambiguous_both` 则是**专门补** `ja_supplement` 文件头自认的空白 (「無標準側標記的真两可形态本文件未覆盖」)。
⇒ 这是**对抗集上的错误率**, 不是路由器在自然分布上的倾向。要谈总体倾向,
得用非对抗的 `legacy` 181 题 —— 那里是 179/181。

命令与实测输出:
```bash
cd sdtm-rag && ./.venv/bin/python -c "
import json
from collections import Counter
d=json.load(open('data/study/st01/eval/runs/u3_baseline_run_1.json'))['detail']
print('pred 分布 (全 253):', dict(Counter(x['pred'] for x in d)))
gb=[x for x in d if x['gold']=='both']
for g in sorted({x['group'] for x in gb}):
    sub=[x for x in gb if x['group']==g]
    print(' ', g, 'n=',len(sub), 'pred=both 命中', sum(1 for x in sub if x['pred']=='both'),
          dict(Counter(x['pred'] for x in sub)))
pb=[x for x in d if x['pred']=='both']
print('pred=both 共', len(pb), '误报 ids:', sorted(x['id'] for x in pb if x['gold']!='both'))
"
```
```
pred 分布 (全 253): {'cdisc': 161, 'both': 9, 'study': 83}
  ambiguous_both n= 6 pred=both 命中 0 {'study': 6}
  legacy n= 5 pred=both 命中 5 {'both': 5}
pred=both 共 9 误报 ids: ['q124', 'st_st01_v11_q17', 'u3_dist_04', 'u3_dist_05']
```

### 5.3 条款 1 的 fatal=0 要求命中 `u3_doc_02`, 而该题属 held-out

按 spec §8, 实现方只看 dev, 看不到这一题 ⇒ 过条款 1 必须**盲测泛化**到它。
这是设计意图 (真泛化考), 但也意味着条款 1 可能因单题不泛化而 FAIL;
届时**不许回头看 held-out 调 prompt**。
(spec §1.6 已就此做事前登记: 仍按条款 1 触发处理并上报用户, 执行方不得自行豁免。)

### 5.4 本基线只覆盖判库 (routing) 一层

不覆盖判库之后的检索与作答质量。**判对库 ≠ 拿到该拿的内容。**

### 5.5 🔴 新写的 24 道手順書题系统性欠采样了失效形态

⇒ 它们对「手順書型会不会被判去 cdisc」这个问题**几乎没有取证能力**。

spec §1.1 记录的失效形态是**纯医学域的分類体系 / 定義 / 判定基準**
(且落在 `_ROUTER_SYSTEM` 规则 1 排除条款自己列举的临床概念射程内 ——
例子清单见 spec §1.1 / `server/federation.py`, 此处不复制)。
而新写 24 题的形态由出题方 (`task-4-report.md` §2)
**统一声明为「運用実務型」**: 「问规定值、期限、区分界线、手续步骤、机构要件 ——
即手順書里写死了、别处推不出来的东西」。
⇒ **两者不是同一形态。** 24 题里落进失效形态的实测只有 `u3_doc_02` 一道 (它错了)。

**本条的取证边界 (据实声明)**: 「≈1 道」来自 ① 出题方对全组形态的**统一设计声明** +
② 只有 `u3_doc_02` 在该方向失败, **不是**我对 24 题逐题做形态分类的结果 ——
**我没有做那个逐题分类**。若下一单元要据此决策, 应先补一次独立的逐题形态标注。

**对下一单元的直接含义**: 若要真正检验这个失效形态, 需要**专门按该形态出题**;
现有 24 题即使全对也不能说明该形态已修好。
⚠ 但**本单元内不许据此改题集** —— gold 必须先于 prompt 冻结 (§6.2 防线 1),
此刻加题 = 看过数据之后动尺子。**记下来, 不动它。**

## 6. 产物

| 文件 | 内容 | git |
|---|---|---|
| `data/study/st01/eval/runs/u3_baseline_run_{1,2,3}.json` | 253 题逐题明细 × 3 遍 (含题面) | **gitignored** (`.gitignore:10 data/study/`) |
| `data/study/st01/eval/runs/routing_run_{1,2,3}_u2post.json` | 被本次跑批覆盖前的 U2 快照 (181 题), 跑批前备份 | gitignored |
| 本文件 | 只含 id 与数字 | tracked |

产物验证 (命令 + 实测输出):
```bash
cd sdtm-rag && ./.venv/bin/python -c "
import json
for i in (1,2,3):
    d = json.load(open(f'data/study/st01/eval/runs/u3_baseline_run_{i}.json'))
    s = d['summary']
    assert len(d['detail']) == 253, len(d['detail'])
    print(i, 'legacy', s['legacy_exact'], 'fatal_excl_final', s['fatal_excl_final'],
          {k: (v['exact'], v['n']) for k, v in s['by_group'].items()})
"
# 1 legacy 179 fatal_excl_final 10 {'legacy': (179, 181), 'u1_doc': (27, 27), 'final': (0, 3), 'dev': (12, 12), 'heldout': (11, 12), 'distractor_cdisc': (7, 12), 'ambiguous_both': (0, 6)}
# 2 legacy 179 fatal_excl_final 10 {...同上...}
# 3 legacy 179 fatal_excl_final 10 {...同上...}
```

## 7. 本 task 的改动面: 生产代码零改动, gold 零改动

### 7.1 生产代码 (tracked ⇒ `git` 是有效证据)

```bash
git diff --stat 046b1b9 HEAD -- server/ eval/     # 046b1b9 = 本 task 开工时的 HEAD
# (空)
shasum -a 256 server/federation.py
# b7a20ea3ef562258ac682603a1967d55710488a4ad5eae40569bb68f59e0f7c9   (与跑批前一致)
```
⇒ `server/`(含 `_ROUTER_SYSTEM`)与 `eval/` 下的两份 tracked gold
(`test_set_v3.yml` / `routing_gold_ja_supplement.yml`) 零改动。

### 7.2 ⚠ 另外两份 gold 是 **gitignored**, 对它们用 `git diff` 是**空证**

`routing_gold_docs.yml` 与 `test_set_docs_v1.yml` 都在 `data/study/` 下 ⇒
**`git diff` 对它们恒空, 证明不了任何事**。
(本文件初版就是用 `git diff` 一并"证明"了四份 gold —— 其中 2/4 是恒真命令。
Task 6 审阅指出, 已改用下列三条真证据。)

**证据 A — Task 5 已把 draft 的字节 sha256 钉在 tracked 测试里, 且 `FINAL` 的题面摘要必须等于 draft**
(`scripts/tests/test_u3_gold_redline.py:55` 常量 + `:143` 字节断言 + `:167` 题面摘要相等):

**证据 B — 冻结基线 `detail` 里记录的题面/gold/group 与当前两份 yml 逐字一致**
(这条最强: 它直接证明"当前的 yml"就是"跑批时用的那份"):

```bash
cd sdtm-rag && ./.venv/bin/python - <<'PY'
import hashlib, json, yaml
from pathlib import Path
from eval.run_eval import load_test_set

DRAFT = Path("data/study/st01/eval/routing_gold_docs_draft.yml")
PINNED = "b1373fd81214b11816b817b5c24539fac3e9753c6f1ada7b34f4921b88d94099"
print("A draft sha256 live == pinned:", hashlib.sha256(DRAFT.read_bytes()).hexdigest() == PINNED)

det = json.load(open("data/study/st01/eval/runs/u3_baseline_run_1.json"))["detail"]
frozen = {d["id"]: (d["question"], d["gold"], d["group"]) for d in det}
new = yaml.safe_load(Path("data/study/st01/eval/routing_gold_docs.yml").read_text("utf-8"))
print("B1 routing_gold_docs.yml n=%d mismatch=%d" % (
    len(new), sum(frozen.get(q["id"]) != (q["question"], q["gold"], q["group"]) for q in new)))
u1 = load_test_set("data/study/st01/eval/test_set_docs_v1.yml")
print("B2 test_set_docs_v1.yml  n=%d mismatch=%d" % (
    len(u1), sum(frozen.get(q["id"], (None,))[0] != q["question"] for q in u1)))
PY
```
```
A draft sha256 live == pinned: True
B1 routing_gold_docs.yml n=42 mismatch=0
B2 test_set_docs_v1.yml  n=30 mismatch=0
```

**证据 C — 两份 gold 的 mtime 均早于本 task 开工**:
```bash
stat -f "%Sm %N" -t "%Y-%m-%d %H:%M:%S" \
  data/study/st01/eval/routing_gold_docs.yml \
  data/study/st01/eval/test_set_docs_v1.yml \
  data/study/st01/eval/runs/u3_baseline_run_1.json
```
```
2026-08-14 01:16:06 data/study/st01/eval/routing_gold_docs.yml
2026-08-12 15:42:44 data/study/st01/eval/test_set_docs_v1.yml
2026-08-14 01:26:50 data/study/st01/eval/runs/u3_baseline_run_1.json
```
两份 gold 的 mtime 均早于跑批产物 (01:26), 也早于本 task 的第一条命令 (约 01:18)。
⚠ mtime 是三条里**最弱**的一条 (可被 `touch` 伪造), 只作旁证; 主证据是 A 与 B。

### 7.3 commit 面

本 commit 只动本文件, 不含任何代码或 gold。
