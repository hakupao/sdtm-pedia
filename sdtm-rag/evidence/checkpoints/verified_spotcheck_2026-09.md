# `verified` 兑现抽检 — 2026-09

> ⛔ **本文件的「判据」与「自毁条款」两段在任何数据到达之前提交** (commit 见 git log)。
> 之后**不得修改** —— 改了就不是预登记。发现判据有问题 ⇒ 停下来报告, 由用户裁定。
> 依据 spec `docs/superpowers/specs/2026-09-02-verified-spotcheck-design.md`。

## 判据 (预登记)

`verified: true` ⟺ 在 `eval/test_set_v2.yml` (102q) 上, 该模型串同时满足:
- **(a)** `check_code_grounding.py` 报 **0 ungrounded、0 nonexistent**;
- **(b)** 分类归属**人判 8 条全 PASS**。

任一不满足 ⇒ `false`。三条边界: 不含联网 Rule 9(b) · 是对**模型串**不是 Router 组 ·
绑定那一次运行的落盘答案。

### 一条答案的人判 PASS 判据
- 无分类归属断言 ⇒ **PASS** (记 `N/A`);
- 有断言且与权威表一致 ⇒ **PASS**;
- 有断言且不一致, 或权威出处是编的 ⇒ **FAIL**。

⚠ 人判看**答案原文 + 权威表**, ⛔ 不看裁判的 verdict。裁判的 quote 只用来定位。

### 8 条的构成 (每模型)
5 条抽自裁判判 `consistent` 的 (对抗抽样) + 3 条抽自 `inconsistent`/`unsure` 的。
后者不足 3 条时**缺额用前者补满 8 条**并记下实际构成; ⛔ 不许少判。

## 自毁条款 (预登记)

| # | 条件 | 后果 |
|---|---|---|
| S1 | 某模型答案里**码总数 < 20** | (a) 层无分辨力 ⇒ ⛔ 不得判 PASS, 记 `INSUFFICIENT_CODES` |
| S2 | 四个模型 (a) 层结果**完全相同** | 题集在 (a) 上已饱和 ⇒ 只能写「未发现差异」, ⛔ 不得写「四个都可信」 |
| S3 | 人判 8 条里「裁判判 consistent、人判 FAIL」≥1 条 | 该条 FAIL (⇒ verified false); 且 ⛔ 不得用裁判全扫结果对其余 94 题做任何声称 |
| S4 | 某模型生成失败率 **>10%** | 不产出结论, 记 `RUN_FAILED`, `verified` 维持 false |

## 结果 (数据到达后填, 此刻必须全空)

| 模型 | 生成成功/102 | 码总数 | ungrounded | nonexistent | (a) | 人判 8 条 | (b) | verified | 触发条款 |
|---|---|---|---|---|---|---|---|---|---|
| opus-5 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| sonnet-5 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| gpt-terra | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| gpt-sol | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
