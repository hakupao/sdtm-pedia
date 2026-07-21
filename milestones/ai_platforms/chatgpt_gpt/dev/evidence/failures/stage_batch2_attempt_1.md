# Stage batch 2 attempt 1 — 06_domain_examples V5 FAIL

> 日期: 2026-04-21
> 归档依据: Rule B (失败归档不删)
> Phase 6.5 双平台锁步 · ChatGPT GPTs · Node 4 batch 2

## 1. 输入

- 脚本: `merge_for_chatgpt.py` v1.4 + `validate_chatgpt_stage.py` v1.4
- 命令:
  ```
  python3 ai_platforms/chatgpt_gpt/dev/scripts/merge_for_chatgpt.py --stage batch2
  python3 ai_platforms/chatgpt_gpt/dev/scripts/validate_chatgpt_stage.py --stage batch2
  ```

## 2. 产物

| 文件 | tokens 实测 | token_cap (v1.4 初始) | 差 |
|------|------------:|---------------------:|---:|
| 05_domain_assumptions_all.md | 54,658 | 69,000 | ✅ PASS (-20.78%) |
| **06_domain_examples_all.md** | **220,575** | **190,000** | ❌ **+16.09%** |
| 07_terminology_core_high_freq.md | 200,746 | 260,000 | ✅ PASS (-22.79%) |
| 08_terminology_quest_and_supp.md | 1,047,119 | 1,250,000 | ✅ PASS (-16.23%) |
| 09_terminology_core_mid_tail.md | 698,081 | 820,000 | ✅ PASS (-14.87%) |

## 3. 技术判定 (V5 FAIL)

```
[FAIL] 06_domain_examples_all.md V5=FAIL — 220,575 > cap 190,000
```

V5 token 上限 FAIL. 其他 V1/V2/V3/V4/V7 皆 PASS (md5=04bc0a05ef072ede1b7df1b487ec7485).

## 4. 业务判定

- 06 examples 合并 63 域 examples.md, 包含大量实例数据表格 (AE/LB/VS/PC 等密集
  domain 每域多 Example 场景, Example 2/3/... 多行 IDVAR/IDVARVAL/RELTYPE 数据
  + 批注文本).
- 原 cap 190K 来自 PLAN_BATCH2.md §估算 (661 KB × 0.75 token/char ≈ 165K
  +15% buffer = 190K). 实测 220K 高于估算 +16%, 与 01_navigation.md 的 VARIABLE_
  INDEX 偏差 (+17% 密度) 机理一致 — chars/token 密度在含表格 + 长 domain name
  + 长 CT label 的 md 中稳定偏低 (3.3-3.6 chars/token), PLAN 的 4 chars/token
  粗估偏乐观.
- 业务影响: 0 (cap 只控单文件 tokens 上限作为预算守护, 不是 ChatGPT 平台硬限).

## 5. 下 attempt 输入

**方案 A (采纳)**: token_cap 190_000 → 254_000 (实测 220,575 × 1.15 = 253,661,
向上取整 254K, 保留 15.2% buffer). 同步更新 merge.py MERGE_CONFIGS[5].token_cap
+ validate.py EXPECTS[5].token_cap. 不改数据 (P5 只读), 不改合并逻辑, 不动 V5 校
验阈值算法. 与 01_navigation 的 v1.3 cap 微调模式一致.

**方案 B (不采)**: 拆分 06 为 06_examples_part1.md + 06_examples_part2.md.
缺点: 违反"每域 examples 原子" 原则 (63 域全量平权), 增加 20 文件硬限占用
(6→7 占用, 剩 13 槽). 收益: cap 压力缓解, 单文件 chunk 密度降低. 劣势 >
收益. 暂不采纳.

## 6. 决策

采方案 A. v1.5 标记 merge + validate 的 docstring cap 微调段.
