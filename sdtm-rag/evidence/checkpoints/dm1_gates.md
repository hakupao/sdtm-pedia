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

逐 task 中间闸 (均 worse=[]): t3 (D1) 140q 同; t4 (D2) 映射 10→20; t5 (D3, label-only) 三集同; t6 (D5) 三集同. 各 task 的 run JSON: `eval/runs/dm1_cdisc_t{3,4,5,6}.json` (CDISC 侧可提交), study/映射侧在 `data/study/st01/eval/runs/dm1_*_t{4,5,6}.json`.

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
