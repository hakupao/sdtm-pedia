# DM1 — Task 8 最终闸 (2026-09-15, HEAD 799ab23 = T1-T7 全部落地)

> 判据 (登记于实现前, PLAN_domain_mapping.md §5): 140q / 48q 逐题 IDENTICAL-or-better; 映射 8q 整组 ↑ 且不只 DS 一题.
> 数字一律取 run JSON `summary.source_recall_avg` (study 集含 3 题 out_of_scope, 对 results 直接平均会得 88.24% 这种假值 — T5 已犯过一次, 见 failures/dm1_task5_attempt_1.md).

## 复跑命令

```bash
cd sdtm-rag
.venv/bin/python -m eval.run_eval eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup --output eval/runs/dm1_cdisc_after.json
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml --retrieval-only --hybrid --study-lookup --collection study_st01 --kb-root data/study/st01/cards --output data/study/st01/eval/runs/dm1_study_after.json
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_domain_mapping_v1.yml --retrieval-only --hybrid --structured-lookup --study-lookup --federated --corpus both --output data/study/st01/eval/runs/dm1_mapping_after.json
# 逐题 diff: 见本文件末尾脚本
```

## 结果

| 集 | before | after | worse | better |
|---|---|---|---|---|
| CDISC v3 140q | 99.17% | 99.17% | [] | [] |
| study v2 48q (gitignored) | 87.5% | 87.5% | [] | [] |
| 映射 v1 8q (gitignored) | 10.0% | 20.0% | [] | dm01, dm02, dm06, dm07 |

逐 task 中间闸 (均 worse=[]): t3 (D1) 140q 同; t4 (D2) 映射 10→20; t5 (D3, label-only) 三集同; t6 (D5) 三集同 —— t5/t6 的「三集同」只是回归判据 (worse=[]), 不是「D3/D5 无收益」的证据: recall 对组成盲, 真实收益见下「组成实验」一节. 各 task 的 run JSON: `eval/runs/dm1_cdisc_t{3,4,5,6}.json` (CDISC 侧可提交), study/映射侧在 `data/study/st01/eval/runs/dm1_*_t{4,5,6}.json`.

140q 集实测并未真正触发 D1: `_ANCHORED_CODE_RE`+`_PREFIXED_CODE_RE` 在 140 题上确有 97 次原始 match, 但全部落在既有大写域码本身或普通英文词 (the/domains/which/...) 上, 没有一次改变 `_query_domains` 的最终域名识别结果 —— 旧口径 (`_QUERY_VAR_TOKEN_RE` 大写 token pass + 长名 pass) 与新口径 (`_query_domains`) 逐题完全相同, diff=0. 所以 140q 零回归**不证明** D1 安全; D1 的安全性只由 `_LOWER_CODE_BLOCKLIST` + 单元测试保证. 未阻断且是词典词的域码 17 个 (AE CE DA EX FA HO IE MI OE RE SE TA TD TE TI TU UR), 需与域词相邻才触发. 复跑: `.venv/bin/python eval/prod_wirein/dm1_d1_140q_probe.py`（输出: 140 questions, 正则原始命中 97 次, 旧/新域名识别不同的题数 0）.

## 组成实验 (recall 看不见的收益)

D3(域码扩写)/D5(BM25 查询侧泛词停用) 在三闸上「零回归」不等于「零收益」——recall 只看 gold 是否进 top-k, 看不见非 gold 席位被什么占据。对问句「本研究中，哪些数据适合进入 sdtm 的 ds domain？」逐 lever 累加, 按 chunk source 前缀分桶 (`domains/DS/` = DS-specific; `chapters/`或`model/` = IG overview; 其余 = other), 15 席构成:

| arm | DS-specific | IG overview | other | assumptions 席位 |
|---|---|---|---|---|
| all OFF | 5 | 10 | 0 | 14 |
| D2 seat only | 5 | 10 | 0 | 1,14 |
| D2+D3 expand | 10 | 2 | 3 | 1,6,8 |
| D2+D3+D5 (shipped) | 10 | 2 | 3 | 1,6,8,10 |

复跑: `.venv/bin/python eval/prod_wirein/dm1_composition.py` (输出与上表逐格一致). 结论: D3+D5 把 IG overview 通论席位从 10 席砍到 2 席, DS-specific 席位 5→10, 域定义段 (assumptions.md) 多占一席 (10) —— 这是 recall 三闸完全测不出的收益, 只有组成层面能看见.

## 映射集逐题 (每题 gold = 1 定义段 + 4 张候选卡)

| 题 | 域 | 问法 | 定义段 (assumptions) | 候选卡 4 张 |
|---|---|---|---|---|
| dm01 | DS | 中文, 小写 `ds domain` (用户原句) | ✅ (before ✗) | 0/4 |
| dm02 | DS | 日文, 大写 DS | ✅ (before ✗) | 0/4 |
| dm03 | DS | 英文长名 Disposition | ✅ (before ✅) | 0/4 |
| dm04 | DM | 日文 | ✅ | 0/4 |
| dm05 | AE | 英文小写 `ae domain` | ✅ (T3 后一度 ✗, T4 复原) | 0/4 |
| dm06 | LB | 中文长名 | ✅ (before ✗) | 0/4 |
| dm07 | PR | 日文 | ✅ (before ✗) | 0/4 |
| dm08 | RS | 英文长名前缀探针 | ✅ | 0/4 |

**结论**: CDISC 侧「定义齐」8/8 达成, 且对 6 个域 / 三种语言 / 大小写 / 长名 全部生效 (模式级). study 侧「候选表单齐」0/32 张 gold 卡, 零进展 — D1-D3-D5 都没能把纯日文 label 的里程碑卡 (F_REG 登録日 / RCT 割付日 / OC 転帰 等, 代称见 gitignored `data/study/st01/eval/dm1_codenames.md`) 送进 study 引擎 top-8. T5 的独立尺子 (`eval/prod_wirein/repro_t5_study_expand.py`) 显示扩写 ON/OFF 下目标表单内卡片 16-18/40, gold 卡 0/32 — 差距不在扩写强度.

## D4 触发判定

PLAN D4 触发条件「study 侧 milestone 卡 recall < 50%」: 实测 0% → **触发**, 交用户裁 (Task 10). 候选路径:
- (a) 「域 → 候选表单」人手表 (每域 3-5 个 form_oid, 标注人工判断), 走 S2 form_scopes 通道 (每表单 3 席);
- (b) 先做区分实验: 把单张 gold 卡的正文直接当 query 查 study 库, 看它能否进 top-8 — 能则是问句→卡片的语义鸿沟 (需别名/表), 不能则是席位/切分问题.

## 逐题 diff 脚本

```python
import json
for name,b,a in [("cdisc140","eval/runs/dm1_cdisc_before.json","eval/runs/dm1_cdisc_after.json"),
                 ("study48","data/study/st01/eval/runs/dm1_study_before.json","data/study/st01/eval/runs/dm1_study_after.json"),
                 ("mapping8","data/study/st01/eval/runs/dm1_mapping_before.json","data/study/st01/eval/runs/dm1_mapping_after.json")]:
    B={r["id"]:r for r in json.load(open(b))["results"]}; A={r["id"]:r for r in json.load(open(a))["results"]}
    key=next(k for k in next(iter(B.values())) if "recall" in k and "source" in k)
    print(name, json.load(open(b))["summary"]["source_recall_avg"], "->", json.load(open(a))["summary"]["source_recall_avg"],
          "worse:", [q for q in B if A[q][key]<B[q][key]], "better:", [q for q in B if A[q][key]>B[q][key]])
```

> 2026-09-15 追记: D4 路径 (b) 区分实验已做 → **语义鸿沟** (卡片自检 100% / 日文 label 96% / 定义段→卡 6%); 详见 `dm1_d4_discrimination.md`.
