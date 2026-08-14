# doc 轨 U3 — 判库欠账 (corpus routing) 收口证据

> 状态: **FAIL 收口** (2026-08-14, 用户裁定) —— Task 8 全闸条款 1 触发 (fatal 9 ≠ 0),
> 按 spec §7 触发后果「修法退回」执行, prompt 改动已 revert (`c754bed`), 生产行为回到基线。
> 分支 `doc-track-u3` · spec `docs/superpowers/specs/2026-08-13-doc-track-u3-corpus-routing-design.md`
> · plan 同名 plans/ 文件 · 失败归档 `evidence/failures/u3_task8_attempt_1.md` (规则 B)
> 数据红线: 题集 / 题面全在 `data/study/` (gitignored)。**本文件零题面正文, 只有 id 与数字。**

## 1. 架构改动面

**最终生产改动面 = 零。** Task 7 曾改 `server/federation.py` `_ROUTER_SYSTEM`
(规则 1 排除条款 + 规则 3 `both` 判据 + 兜底句重写, `2c060a5..35d717a`, 共 5 轮);
Task 8 全闸条款 1 触发后, 用户裁定退回, 两文件已还原至 `1690d38` (Task 7 前)。

**本单元存续产物** (不随退回撤销):
- 路由 gold 扩到手順書型: 新写 42 题 + 确定性 dev/heldout 划分 (12/12/12/6), gold 红线闸 `eval/lint_gold.py` 扩展
- `both` 档三档确定性尺子 (只量不改): `evidence/checkpoints/doc_track_u3_both_ruler.md`
- 基线冻结仪器: `eval/run_routing_eval.py` 全 253 题三遍跑批 + `u3_baseline_run_{1,2,3}.json` (gitignored, 本地)
- 六条条款判定脚本: `eval/u3_task8_verdict.py` (plan Task 8 Step 3 + spec §7.1 多数类基线并排)

## 2. 数字

### 2.1 both 尺子 (Task 2, 三遍全一致, 详见 both_ruler 检查点)

doc 侧 1.0000 (结构恒等, 非测得稳健性); cards 侧 0.8750 → 0.8229 (−5.21pt, 归因闭合 4 题);
该代价当前**悬着未付** (脆弱 4 题现无一被判到 `both`)。

### 2.2 Task 8 全闸六条条款 (Task 7 终态 prompt, 三遍 253/253 零漂移)

| # | 条款 | 结果 | 判定 |
|---|---|---|---|
| 1 | 每遍 fatal=0 且 legacy ≥ 178 | fatal=**9** (三遍同), legacy 179/181 | **⛔ 触发** |
| 2 | heldout ≥ dev − 25pt | dev 100% / heldout 91.67%, gap 8.33pt | 未触发 |
| 3 | dev ≥ 10/12 | 12/12 | 未触发 |
| 4 | distractor 较基线降 ≤ 1 | 7/12 → 7/12, drop 0 | 未触发 |
| 5 | final 只报告 | q15 study✓ / q17✗ / q53✗ (基线 0/3 → 1/3) | 已报告 |
| 6 | 三遍不一致点名 | unstable = 0 | 未触发 |

⚠ spec §7.1: dev/heldout 多数类基线各 100%, 条款 2/3 单独零判别力, 引用必须连同条款 1/4。
新写 42 题多数类 57.1%; 全 253 题多数类 cdisc 64.4%。

**改动面**: 全 253 题仅 4 题预测变化 —— 修好 `q15`(final)/`amb_03`/`amb_05`, 变坏 `dist_05`
(both→study, **非致命错变致命错**); `u3_doc_02`(规则 1 唯一 held-out 目标)纹丝不动。
fatal 10 → 9, 修 2 坏 1, 距 0 相差 9 —— 非边缘情形。明细见失败归档。

### 2.3 退回验证 (2026-08-14, 可复跑)

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=no | tail -2   # → 1259 passed
./.venv/bin/python -m eval.run_routing_eval --runs 3            # 三遍
# routing_run_{1,2,3}.json 与 u3_baseline_run_{1,2,3}.json 比对: summary 相同 + 逐题 pred 零差异
```

结果: pytest **1259 passed**; 三遍复跑与冻结基线**逐题 EXACT MATCH** (fatal=10, 253/253 稳定)。

## 3. 触发 / 豁免

- **条款 1 触发, 无豁免**。spec §1.6 事前登记的灰色情形 (唯一剩 `u3_doc_02`) 未达到 —— 实剩 9 个。
- 用户裁定 (2026-08-14): 三选一 (退回 / 换实现方开 attempt 2 / 带限制豁免收口) 中选**退回**。
- 阈值 / `score_run` fatal 定义 / gold 全程一字未动 (条款 1 附带禁令遵守)。
- 条款 5 纪律已执行: 看过 final/heldout 结果后未再改 prompt; 本 controller session 已见
  held-out 题面 (取证需要), **若未来开新 attempt, 实现方必须是全新 session** (spec §6.2 防线 2)。

## 4. 业务结论与遗留

1. **判库欠账仍在**: fatal 10 个原样 (both→study 6 / cdisc→study 3 / study→cdisc 1),
   动机题 q17/q53 仍错。修复路径经一整轮 pattern-level 尝试未达标, 提示盲写概念对
   held-out 形态的覆盖上限, 或需要不同的机制 (非 prompt 措辞层)。
2. **尺子盲区 (遗留待裁定)**: 条款 4 用 exact 口径, 抓不到「非致命错→致命错」型回归
   (`dist_05` 实证被 7/12 持平掩盖)。未来单元若重启修法, 建议先裁定是否改用 fatal 口径。
3. **Task 7 仪器盲区是设计使然**: 可见集 193 (legacy+dev) 出口绿 ≠ 全闸绿, 防对症下药的
   代价就是全闸才见真章。本次流程按设计走完, 闸如实拦下 —— 流程本身工作正常。
4. spec §9「不能证明什么」全部仍然成立 (含: 判库准确率 ≠ 答案质量; both 席位配置未验证)。

## 5. 任务台账

| Task | 内容 | 状态 |
|---|---|---|
| 1-6 | 尺子 / gold / 划分 / 基线冻结 | DONE (存续) |
| 7 | prompt 两方向同修 (5 轮) | DONE 后被裁定退回 (`c754bed`) |
| 8 | 全闸六条条款判定 | DONE — 条款 1 触发, 归档 + 上报 + 退回 |
| 9 | 三方核验 (规则 D) | **未执行** — FAIL 收口后范围待用户定 (存续产物仍可核) |
| 10 | 收尾 (worklog / PROGRESS / RETRO) | 待执行 |
