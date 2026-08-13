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

1. **条款 2 与条款 3 在基线上就已满足** (dev 12/12, heldout 11/12, gap −8.3pt)。
   叠加 spec §7.1 已记的「两组多数类基线均 100%」, 这两条判据在本单元里
   **既无判别力, 也无可展示的余量** —— 修法对它们最好的结果只是持平。
   ⇒ **引用条款 2/3 的数字时必须同时给出条款 1 与条款 4** (spec §7.1 处置第 1 条)。

2. **「手順書题被判去公开标准库」这个欠账, 在非豁免题上只测到 1 例。**
   51 道非豁免手順書型题 (u1_doc 27 + dev 12 + heldout 12) 里基线判错 **1 题**
   (`u3_doc_02`); U1 的 27 题 **0 例**。真正大面积错的是
   `ambiguous_both` 0/6 与 `distractor_cdisc` 5/12 错。
   **这两个形状与本单元立项时描述的欠账不是同一件事。**
   本文件只陈述实测分布, 不改任何题集与阈值 (§6.2 防线 1: 看过数据之后不许动尺子)。

   ⚠ **`ambiguous_both` 0/6 不等于「路由器不会输出 `both`」** —— 全 253 题里 `pred=both`
   共 **9 次**, 且 `legacy` 组 5 道 `gold=both` 的题 **5/5 全对**。失效是**局限于新写的
   这 6 题**的: 它们被整齐地拉去了 `study` (6/6 全 `pred=study`)。
   与此同时有 **4 次 `both` 误报** (`q124` / `st_st01_v11_q17` / `u3_dist_04` / `u3_dist_05`,
   gold 均非 `both`)。⇒ 现象是**「`both` 给错了地方」而非「不会给 `both`」**,
   两者指向的病因不同, 请勿按后者去改 prompt。

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

3. **条款 1 的 fatal=0 要求命中 `u3_doc_02`, 而该题属 held-out。**
   按 spec §8, 实现方只看 dev, 看不到这一题 ⇒ 过条款 1 必须**盲测泛化**到它。
   这是设计意图 (真泛化考), 但也意味着条款 1 可能因单题不泛化而 FAIL;
   届时**不许回头看 held-out 调 prompt** (§7 条款 2 的后果是退回重写 + 换新题重测)。

4. **本基线只覆盖判库 (routing) 一层**, 不覆盖判库之后的检索与作答质量。
   判对库 ≠ 拿到该拿的内容。

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

## 7. 本 task 的改动面

**生产代码零改动, gold 零改动。** `server/federation.py` (含 `_ROUTER_SYSTEM`) 与四份 gold
(`routing_gold_docs.yml` / `test_set_docs_v1.yml` / `eval/test_set_v3.yml` /
`eval/routing_gold_ja_supplement.yml`) 一字未动 —— 见本 commit 的 diff:
本 commit 只新增本文件。
