# U3 Task 8 attempt 1 — 条款 1 触发 (fatal 9 ≠ 0), 停下上报

> 状态: **FAIL — 条款 1 触发, 按 plan Task 8 Step 4 归档并上报用户** (2026-08-14)
> 规则 B 归档: 输入 / 产物 / 技术判定 / 业务判定 / 下一 attempt 输入

## 1. 输入

- 被测 prompt: `server/federation.py` `_ROUTER_SYSTEM` @ commit `35d717a`
  (Task 7 第 5 轮终态: 规则 1 排除条款 + 规则 3 both 判据 + 兜底句重写, spec §6.1.1)
- 基线: `data/study/st01/eval/runs/u3_baseline_run_{1,2,3}.json` (Task 6 冻结, fatal=10)
- 命令 (可复跑):
  ```bash
  ./.venv/bin/python -m eval.run_routing_eval --runs 3   # 全 253 题
  ./.venv/bin/python eval/u3_task8_verdict.py            # 六条条款判定
  ```

## 2. 产物

- `data/study/st01/eval/runs/u3_after_run_{1,2,3}.json` (gitignored, 本地留存; 三遍 253/253 判定一致)
- 判定脚本 `eval/u3_task8_verdict.py` = plan Task 8 Step 3 原脚本 + spec §7.1 处置 #2 多数类基线并排

### 六条条款逐条 (三遍确定性, unstable=0)

| # | 条款 | 结果 | 判定 |
|---|---|---|---|
| 1 | 每遍 fatal=0 且 legacy ≥ 178 | fatal=**9** (三遍同), legacy 179/181 | **⛔ 触发** |
| 2 | heldout ≥ dev − 25pt | dev 100% / heldout 91.67%, gap 8.33pt | 未触发 |
| 3 | dev ≥ 10/12 | 12/12 | 未触发 |
| 4 | distractor 较基线降 ≤ 1 | 7/12 → 7/12, drop 0 | 未触发 |
| 5 | final 只报告 | q15 study✓ / q17 cdisc✗ / q53 cdisc✗ (基线 0/3 → 1/3) | 已报告 |
| 6 | 三遍点名不一致 | unstable = 0 | 未触发 |

⚠ 条款 2/3 引用须知 (spec §7.1): dev/heldout 多数类基线各 **100%**, 两条单独看零判别力;
上表已与条款 1/4 并排。新写 42 题多数类 57.1%, 全 253 题多数类 cdisc 64.4%。

### 改动面 (基线 → 改后, 全 253 题只有 4 题预测变化, 三遍一致)

| id | group | gold | 基线 pred | 改后 pred | 效果 |
|---|---|---|---|---|---|
| docs_v1_q15 | final | study | cdisc | study | ✓ 修好 (只报告不作判据) |
| u3_amb_03 | ambiguous_both | both | study | both | ✓ 修好 |
| u3_amb_05 | ambiguous_both | both | study | both | ✓ 修好 |
| u3_dist_05 | distractor_cdisc | cdisc | both | study | **✗ 新增 fatal** (非致命错 → 致命错) |

### fatal 明细 (基线 10 → 改后 9)

| 方向 | 基线 fatal | 改后 fatal | 变化 |
|---|---|---|---|
| both → study (规则 3 目标) | amb_01…06 共 6 | amb_01/02/04/06 共 4 | −2 (amb_03/05 修好) |
| cdisc → study (过宽惩罚器) | dist_07/10/11 共 3 | dist_05/07/10/11 共 4 | **+1 (dist_05 新增)** |
| study → cdisc (规则 1 目标) | doc_02 共 1 | doc_02 共 1 | 0 (**纹丝不动**) |

## 3. 技术判定

**条款 1 触发, 无歧义**: fatal_excl_final = 9 ≠ 0, 三遍全同 (确定性, 非噪声)。
spec §1.6 事前登记的灰色情形 (「唯一剩 u3_doc_02」) **未达到** —— 实际剩 9 个, 远超。
触发后果 (spec §7 条款 1): **修法退回**; 阈值 / score_run fatal 定义 / gold 一字未动。
条款 5 纪律自本归档起生效: **已看过 final 与 heldout 结果, 本 session 不得再改 prompt**。

## 4. 业务判定

1. **Task 7 的仪器只能看到「可见集 193」(legacy 181 + dev 12), 第 5 轮出口 191/193 过闸**;
   而条款 1 的失败面 (ambiguous_both / distractor / heldout) 全部在仪器盲区。
   Task 7 出口绿 ≠ 全闸绿, 这是设计使然 (防对症下药), 不是 Task 7 执行失误。
2. **规则 1 排除条款对其唯一 held-out 目标 u3_doc_02 完全无效** (pred 仍 cdisc),
   但对同形态的 final q15 有效 (cdisc→study)。盲写概念只覆盖了 4 个同形态实例中的一部分。
3. **规则 3 both 判据只修复 6 分之 2** (amb_03/05), 其余 4 道仍被判 study。
4. **spec §1.5 预警的两方向张力实际发生**: 放宽 study 侧使 dist_05 从「both (非致命错)」
   变「study (致命错)」。条款 4 (exact 口径) 没抓到它 —— exact 7/12 恰好持平,
   但 fatal 口径下这是净新增回归。**条款 4 用 exact 而非 fatal 计数, 是本次暴露的尺子盲区**
   (改判据须用户裁定, 此处只记录)。
5. 净效果: fatal 10 → 9, 修 2 坏 1, 距条款 1 要求的 0 相差 9。**修法整体离达标很远,
   不是差一两题的边缘情形。**

## 5. 下一 attempt 输入

- **需用户裁定** (按 plan Task 8 Step 4 上报, 执行方无权选路):
  a. 按条款 1 触发后果**退回** Task 7 修法 (revert 2c060a5..35d717a 的 prompt 改动), U3 收口记 FAIL;
  b. 或用户裁定开启新一轮修法 (需换新 session 实现方 —— 本 controller session 已见
     held-out 题面与 final 结果, 按 §6.2 防线 2 已丧失实现方资格);
  c. 或用户裁定其他 (如带着已知限制收口)。
- 若开新 attempt, 失败面坐标 (只给 id 与方向, **题面不得给实现方**):
  both→study: u3_amb_01/02/04/06; cdisc→study: u3_dist_05/07/10/11; study→cdisc: u3_doc_02。
- 遗留尺子问题一并待裁定: 条款 4 的 exact 口径抓不到「非致命错 → 致命错」型回归 (见 §4.4)。
