# S1 Deterministic Structured-Lookup — Result Record

> 状态: **PASS** (2026-06-09) — retrieval-only, 53q, collection `sdtm_kb_v1` (4146 chunks, 未重建)

## 杠杆描述
向量/BM25 都救不了、但 KB 以结构化形式已有答案的两类查询, 通过精确查表 union-add 进检索结果:
- (1) 术语/CT 码查询: 变量名 → (codelist, CT码, 术语文件) — 主源 spec.md Cross References 块, §二 CT 列 + terminology 标题交叉验证。
- (2) 分布/关系查询: "哪些域用了 X" / "share codelist Y" → VARIABLE_INDEX.md。

默认 off (`--structured-lookup` flag), 向后兼容。意图关键词不命中即返回 `[]`, 走原 cosine。

## 复现命令
```
# baseline (84.0%)
python eval/run_eval.py eval/test_set_v1.yml --retrieval-only \
  --output eval/ablation_t1/baseline_recheck.json

# +lookup (90.6%)
python eval/run_eval.py eval/test_set_v1.yml --retrieval-only --structured-lookup \
  --output eval/ablation_t1/structured_lookup.json
```

## 逐类别 src recall: BEFORE → AFTER
| 类别 | before | after | delta |
|------|--------|-------|-------|
| single_domain | 96.4% | **100.0%** | +3.6 |
| cross_domain | 61.5% | 76.9% | +15.4 |
| concept | 84.6% | 84.6% | +0.0 |
| mixed | 92.3% | **100.0%** | +7.7 |
| **OVERALL** | **84.0%** | **90.6%** | **+6.6** |

## Kill-switch
single_domain 96.4% → 100.0% — **PASS** (要求 ≥96.4%, 实际不降反升)。
零回归: 53 题无一题 recall 下降; 5 题上升 (q07 q34 q16 s04 s05)。

## 5 道目标题
| qid | cat | gold | before | after |
|-----|-----|------|--------|-------|
| q07 | cross | VARIABLE_INDEX.md | 0% | 100% |
| q34 | cross | VARIABLE_INDEX.md | 0% | 100% |
| q16 | mixed | AE/spec + terminology/core/ae.md | 50% | 100% |
| s04 | mixed | AE/spec + terminology/core/ae.md | 50% | 100% |
| s05 | single | VS/spec + terminology/core/vs.md | 50% | 100% |

q08 (gold DM/spec.md, 非查表目标) 注入 VARIABLE_INDEX.md 后 recall 仍 100% (DM/spec.md 保留在 rank 3) — union-add 纯增量, 不挤掉已命中 gold。

## 触发面
lookup 在 19/53 触发, 34/53 保守 no-op。触发但 recall 不变的 14 题 = 注入的术语文件正确但非该题 gold (gold 是 spec.md, 已被 cosine 命中) — 增量无害。

## 仍未推进
- concept (84.6%) 完全没动: 该类 miss 是 chapters/model 文件 (q38 ch02, q39 model/02_observation_classes.md), 非变量/CT 查表场景。
- cross_domain 余下 miss: q09/q33 (RELREC/RELSPEC spec.md), q10/q32 (TR/SV spec.md) — 这些是"按域名/关系名定位 spec"而非变量/CT 查表, S1 不覆盖。
