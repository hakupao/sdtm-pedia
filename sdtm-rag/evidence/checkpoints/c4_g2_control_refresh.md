# C4 / G2 对照臂刷新 (2026-08-27)

> 性质: **对照臂刷新, 不是 G2 本身** · 上游: `study_c3_precision_tradeoff.md` §8 G2
> 红线: 零真名 — 卡片文件名含真实 form/item OID, 一律以题号指代

## 0. 一句话

G2 的对照臂 (卡片侧 **87.50%**) 是 2026-08-26 事件层单元闸 D 取的。此后 HEAD 又动过三处,
**拿旧值当参照物不成立**, 故本轮在 HEAD 重取三遍。结果: **与冻结基线逐题 Δ0**, 对照臂
可继续使用。

**G2 状态仍为「未测 ⬜」** —— 它的判据是「union-add 之后卡片侧三遍逐题 Δ0」, 接线不存在
就没有被测对象。本轮只刷新了它的**对照臂**。

## 1. 为什么必须重取

HEAD 自 08-26 冻结基线之后的三处改动, 每一处都在原理上可能动卡片侧检索:

| 改动 | 可能的影响路径 |
|---|---|
| `適用範囲` 标签语义反转修复 + **重灌索引** | 231/961 张卡片正文改动 ⇒ 向量变化 |
| Tier 3 名称子串层移除 | `study_lookup` 返回集合变化 (卡片侧走 `resolve()` 不走 `resolve_events`, 但同一模块) |
| L1 卷首补 11 个 chunk (114 → 125) | `study_st01_docs` 变大 (独立 collection, 但生产 docs 引擎已由 U2 接线) |

## 2. 实测

命令 (与事件层单元闸 D 同口径, 本会话实跑 ×3):

```bash
cd sdtm-rag && .venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup --collection study_st01 \
  --kb-root data/study/st01/cards --output /tmp/run_N.json
```

| 项 | 结果 |
|---|---|
| `source_recall_avg` | **0.875 ×3** (三遍逐位相同) |
| 三遍逐题一致性 | 51 个 id **0 题波动** |
| 对照冻结基线 `data/study/st01/eval/runs/v2_baseline_s2on.json` | **逐题 Δ0**; id 集合完全相同 (无新增无删除) |
| 计分 | `n_scored` 48 / `n_out_of_scope` 3 / 非满分 6 题 ⇒ 42/48 = 87.50% |
| `verdict` | PASS (threshold 0.85) |

⇒ **HEAD 那三处改动对卡片侧零漂移。**

## 3. 这个绿灯看不见什么 (硬规矩 19)

1. **它不是 G2**。G2 要测的是 union-add **之后**的回归, 本轮无 union-add。
2. **口径不是生产全栈**: 本命令走卡片侧路径 (`--study-lookup --collection study_st01`),
   **不含生产的 docs 引擎** (U2 接线的 `StudyCorpusEngine`)。选它是因为要与闸 D 的
   对照臂同口径可比, 但它**看不见 docs 侧的挤占**。
3. **`87.50%` 三版分数互不可比的老规矩仍适用** —— 该数只在 study golden v2 口径下有意义。
4. **零漂移 ≠ 三处改动无影响**: 这把尺子是 48 题 source-recall, 对「卡片正文措辞改了」
   这类变化结构上不敏感 (`適用範囲` 修复本来就实证过逐题 Δ0 无责)。
