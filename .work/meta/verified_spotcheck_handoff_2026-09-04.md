# 交接 — `verified` 兑现抽检 (2026-09-04)

> 分支 `feat/verified-spotcheck` · **已推送 origin** · 测试 **2049 passed / 1 skipped / 0 failed**
> 预登记文件: `sdtm-rag/evidence/checkpoints/verified_spotcheck_2026-09.md` (**先读它, 再读本文**)

## 0″. ✅ 全部收官 (2026-09-07): 24 条人判全 PASS ⇒ gpt-terra / gpt-sol `verified: true`, sonnet-5 `false`

四模型终态: opus-5 true · gpt-terra true · gpt-sol true · sonnet-5 false ((a) q35 C66742)。
S1-S4 均未触发。config + 测试已翻。本文件转历史; 唯一余项: 生产 launchd 重启以显新徽章 (待用户)。

## 0′. (2026-09-06 下午, 已解除) 三模型已跑完, 当时阻塞: 24 条人判在用户手上

三模型生成 + (a) + 裁判扫描全部落盘 (记录 `verified_spotcheck_2026-09.md` §‡)。
(a): gpt-terra PASS · gpt-sol PASS · **sonnet-5 FAIL (q35 C66742, 1 ungrounded ⇒ `verified: false` 已定)**。
S1/S2/S4 均未触发。新 session 开局**不要代判**: 问用户拿三份包的判定
(`human_packet_{sonnet-5,gpt-terra,gpt-sol}.md`, 各 8 条, 形如 `q16: PASS`)。
拿到后: 填结果表 → 逐模型跑 S3 (比对 `class_scan_<tag>.json` verdict) → gpt-terra/gpt-sol 若 (b) PASS
则 `server/config.py` 对应 `verified=True` (+ 测试) ; sonnet-5 维持 False。

## 0. ✅ 已解除 (2026-09-06 上午): (b) 层人判 8 条全 PASS, S3 未触发, opus-5 `verified: true`

记录见 `sdtm-rag/evidence/checkpoints/verified_spotcheck_2026-09.md` §「† (b) 层人判记录」。
**用户裁定 (2026-09-06): 下个 session 三个模型 (sonnet-5 / gpt-terra / gpt-sol) 都跑。**
成本 (生成 306 + 裁判 306 = 612 次 + 24 条人判) 用户已知悉并同意, 开跑不必再问。
每模型流程: `run_eval.py` 生成 (max_tokens 8192 默认) → `check_code_grounding.py <run> on` (a) 层
→ `run_class_assertion_scan.py <run>` 裁判扫描 + 人判包 → 用户人判 8 条 → 填表 + S3。
四模型齐后再判 S2 (四个 (a) 结果完全相同 ⇒ 只能写「未发现差异」)。
⚠ 跨模型对比时记 B-2: opus-5 是 4096 上限, 其余三个 8192。以下为原文, 保留作历史。

### (原) ⛔ 唯一阻塞项: (b) 层人判 8 条在用户手上

新 session 开局**不要自己动手判, 也不要替用户判** —— 预登记写死 (b) 层是**人判**,
理由是兜裁判漏网。LLM 代判 = 用裁判去查裁判, 结构上测不到漏网。

要做的只有一件: **问用户拿 8 条判定结果** (形如 `q16: PASS`)。拿到后才有下一步。

材料已生成好, 用户已收到:
- 人判包 `sdtm-rag/evidence/checkpoints/human_packet_opus-5.md` (权威表 + 8 条答案原文, 无 verdict)
- 对照索引 `sdtm-rag/evidence/checkpoints/human_packet_opus-5_index.md` (机械抽取, 无判定倾向)

## 1. 拿到 8 条结果后做什么 (按序)

1. 填 `verified_spotcheck_2026-09.md` 结果表 opus-5 行的「人判 8 条 / (b) / verified」三列。
2. **跑 S3 判定** —— 逐条比对 `class_scan_opus-5.json` 里该题的 `verdict`:
   只要存在 **「裁判判 `consistent` 而人判 FAIL」≥ 1 条**, 则
   - 该条 FAIL ⇒ `verified = false`;
   - 且 ⛔ **不得用裁判全扫结果对其余 94 题做任何声称** (预登记原文)。
   抽中的 8 条里 **5 条来自 `consistent`、3 条来自 `inconsistent`** (构成已记录, seed=0)。
3. 按 §4 与用户商定其余三个模型跑不跑。

## 2. 本轮已经定死的结论 (别重算)

| 项 | 值 | 出处 |
|---|---|---|
| opus-5 生成 | 102/102 非空, 37m04s, EXIT 0 | `evidence/checkpoints/verified_runs/run_opus-5.*` |
| (a) 层 | **PASS** — codes 454, grounded 454, ungrounded 0, nonexistent 0 | `eval/prod_wirein/code_grounding_on.json` |
| 重建保真 | **102/102** top5 与落盘一致 | 判据脚本自打印 |
| S1 (码 < 20) | **未触发** (454) ⇒ (a) 层有分辨力, 题集不用换 | 同上 |
| S4 (失败率 > 10%) | **未触发** (0%) | 同上 |
| 裁判扫描 | 98 consistent / 4 inconsistent, parse_error 0, 失败 0 | `evidence/checkpoints/class_scan_opus-5.json` |
| `verified` | **true** (2026-09-06, (b) 8/8 PASS, S3 未触发) | `verified_spotcheck_2026-09.md` §† |

## 3. 三条会让人误读的边界

**B-1. 判据被实质修改过 (V-1), 且方向对被测对象有利。**
`check_code_grounding.py` 原写死 `structured_lookup=ON, hybrid=ON` 重建上下文, 而生成时
两者都关 ⇒ 判 ungrounded 的 top-15 不是模型看见的那个。修订经用户 2026-09-03 裁定。
⛔ 汇报时**必须连带说明**这次修订, 不能只报"(a) PASS"。完整记录与可复核证据在
`verified_spotcheck_2026-09.md` §「判据修订记录」(102/102 vs 0/102 定方向 · 阈值未动 ·
新脚本更容易 FAIL 的两道闸 · 变异复跑命令)。

**B-2. opus-5 那轮跑在 V-2 修复前, 上限仍是 4096。**
q36/q83 撞顶被截断 (影响有界: 各发 0 / 3 个码, 且 3 个全 grounded)。
其余三模型将在 **8192** 下跑 ⇒ **与 opus-5 上限不同**, 跨模型比较时这是已知不齐。
要抹平只能重跑 opus-5 (102 次)。

**B-3. (b) 层是「每模型 8 条」, 不是全局 8 条。**
预登记原文 §「8 条的构成 (每模型)」。四模型全做 = **32 条人判**。

## 4. 成本账 (用户对此敏感, 报数要准)

- 已花: opus-5 生成 **102 次** + 裁判扫描 **102 次** = 204 次 (另每次提问走一次 OpenAI
  embedding, spec 2026-09-01 §9 D3 已裁定接受的既有开销)。
- 若跑完其余三个: 生成 **306** + 裁判 **306** = **612 次**, 外加 **24 条人判**。
- ⚠ 四模型总量是 **408 生成 + 408 裁判 = 816 次**, 不是"408 次" —— 早期沟通里只算了生成那一半。

**为什么建议先判 8 条再决定烧不烧这 612 次**: 若 S3 触发, 说明这个裁判在本题集上会漏网,
那么用同一裁判给其余三个模型做"对抗抽样"的可信度就打折 —— 该先换裁判/换方法, 而不是
先烧钱。与上一轮"先跑 opus-5 一个模型"同构。

## 5. 关键命令

```bash
cd sdtm-rag

# (a) 层判据 (零 LLM 生成, 走检索 embedding)
.venv/bin/python eval/prod_wirein/check_code_grounding.py \
    evidence/checkpoints/verified_runs/run_opus-5.json on

# 换渲染顺序重出人判包 (零 LLM 调用; 不动抽样)
.venv/bin/python eval/prod_wirein/run_class_assertion_scan.py \
    evidence/checkpoints/verified_runs/run_opus-5.json \
    --reuse-scan evidence/checkpoints/class_scan_opus-5.json

# 跑下一个模型 (⚠ 每个 102 次生成, 须先报成本等用户明确同意)
# 生成侧现已显式 --max-tokens 8192 (默认), 报告会落盘 retrieval_levers + truncated

.venv/bin/python -m pytest scripts/tests -q   # 期望 exit 0, 2049 passed / 1 skipped
```

## 6. 本轮 commit (分支 `feat/verified-spotcheck`)

| commit | 内容 |
|---|---|
| `dee16b8` | V-1 判据口径修正 (读落盘 lever + 保真/退化双闸) + V-2 max_tokens 显式钉死 |
| `9ff271b` | SF-36 加入 oidscan `KNOWN_PUBLIC_COLLISIONS` (公开量表名撞车, 非泄漏) |
| `7892e67` | opus-5 首轮实测落盘 + 判据修订记录 |
| `b7d4d83` | (b) 层驱动 + 裁判扫描落盘 + 人判包 |

## 7. 一个未处理的风险 (诚实记录)

上一 session 在核验 `blind_order` 修复时, 往终端打印过「裁判报警项在人判包里的位置」。
若用户的终端显示了那行工具输出, **用户在判之前已被锚定**。
补救选项 (零调用): 用 `--reuse-scan` 只换渲染顺序重出一份包 —— **抽样仍是预登记的
seed=0, 不算重掷**。用户尚未表态是否需要。
