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
| opus-5 | 102/102 | 454 | **0** ※ | 0 | **PASS** ※ | ⬜ | ⬜ | ⬜ (待 (b)) | 无 (S1/S4 均未触发) |
| sonnet-5 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| gpt-terra | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| gpt-sol | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

## 实测记录 — opus-5 (2026-09-02, Task 5 第一轮)

落盘: `evidence/checkpoints/verified_runs/run_opus-5.{json,log,timing.txt}`;
(a) 层产物: `eval/prod_wirein/code_grounding_on.json`。

**复跑命令**
```
cd sdtm-rag
.venv/bin/python eval/prod_wirein/check_code_grounding.py \
    evidence/checkpoints/verified_runs/run_opus-5.json on
```

**耗时 (推算 → 实测)**: START 2026-09-02T13:23:14Z → END 14:00:18Z = **37m04s** / 102 题,
EXIT_CODE=0。单题 elapsed min/median/max = 8.8 / 19.2 / 46.0 s (求和 2221s, 即串行无并发)。

**答案长度** (外推依据): 字符数 min/median/max = **974 / 3187 / 8754**;
completion tokens min/median/max = 577 / 1538 / 4096; prompt tokens 中位 18371,
全轮 total_tokens 2,127,221。
⚠ **q36 / q83 的 completion 恰为 4096 且答案断在句中 ⇒ 触到 max_tokens 上限被截断**
(截断会少发码, 对 (a) 层是偏乐观方向的噪声)。

**(a) 层结果**: 码总数 **454** (70/102 题含码), grounded 446, **ungrounded 8**, **nonexistent 0**
⇒ RULE-7 违规 8 ⇒ (a) **FAIL**。违规集中在 5 题:

| qid | codes | ungrounded 码 |
|---|---|---|
| q31 | 1 | C125923 |
| q33 | 6 | C78737 |
| q35 | 4 | C49488, C66734, C78735, C78737 |
| q72 | 1 | C172330 |
| q78 | 1 | C66741 |

性质: 全部是 **mis-cited (码在 KB 里真实存在, 但不在该题重建的检索上下文里)**,
**零纯捏造**。

**自毁条款检验**
- **S1 (码总数 < 20)**: 454 ≥ 20 ⇒ **未触发**, (a) 层在本题集上**有分辨力**。
- **S4 (生成失败率 > 10%)**: 102/102 有非空答案, 失败率 0% ⇒ **未触发**。
- S2 需四模型齐全后才可判; S3 需 (b) 层人判后才可判。

**判定**: 按预登记判据 (a) 不满足 ⇒ **opus-5 `verified: false`** (与 (b) 层结果无关, 已定)。

### ⚠ 发现 V-1 (待用户裁定): (a) 层重建上下文与生成时的检索口径不一致

`check_code_grounding.py` 不读生成时的上下文 (run json 未落盘 context), 而是**重建**:

```python
# eval/prod_wirein/check_code_grounding.py :: prod_engine()
RAGEngine(..., structured_lookup_enabled=True, hybrid_enabled=True, ...)
```

但本轮生成的实际口径是**两者都关**。证据 (log 行按 `run_eval.py:872-904` 的条件拼接,
`--hybrid` / `--structured-lookup` 未给时对应片段整段不出现):

```
RAG engine: 4329 chunks, model=bedrock/converse/global.anthropic.claude-opus-5, top_k=15, guardrail=ON
                                                    ^ 无 structured_lookup=ON, 无 hybrid=, 无 rerank=, 无 expand=
```

⇒ 判 `ungrounded` 所用的 top-15 **不是模型当时看见的 top-15** (融合会挤掉部分纯 dense 命中,
structured-lookup 会 union-add 额外文件)。8 条 ungrounded 里有多少是真 mis-cite、
有多少是口径差造成的假阳性, **当前数据无法区分**。

⛔ 按本文件开头的规则, 判据 (点名了这个脚本) **不擅自改**; 记录此发现, 由用户裁定。
可选处置: (i) 维持原判 (脚本即判据, FAIL 成立); (ii) 补一次同口径诊断跑 (约 102 次 embedding,
无 LLM 生成) 量化敏感度; (iii) 后续三个模型改用与生成同口径重建。

### V-1 诊断跑结果 (⛔ 诊断, 非判据 — 用户裁定 2026-09-03: "补同口径诊断跑, 结果只作诊断不改判据")

脚本 `eval/prod_wirein/diag_code_grounding_same_config.py` (新增, 与判据脚本并列存在,
**不修改也不替代** `check_code_grounding.py`)。复跑:

```
cd sdtm-rag
.venv/bin/python eval/prod_wirein/diag_code_grounding_same_config.py \
    evidence/checkpoints/verified_runs/run_opus-5.json
```

**结果**: 同口径 (structured_lookup=OFF, hybrid=OFF, rerank=OFF, expansion=none) 下

| | 判据口径 (lookup/hybrid=ON) | 同口径 (与生成一致) |
|---|---|---|
| 码总数 | 454 | 454 |
| grounded | 446 | **454** |
| ungrounded | **8** | **0** |
| nonexistent | 0 | 0 |

⇒ **8 条 ungrounded 全部是口径差假阳性, 无一是真 mis-cite。**

**否定控制** (防"ctx 退化成全库导致全部 grounded"这一自欺): 假码 `C99999` 在全部 102 题的
重建上下文中均未出现 ✓ (已写进脚本, 控制失败即 SystemExit fail-loud)。

**逐条定位** (三题抽样, 两口径 ctx 实测互不相同):

| qid | ctx 长度 生成口径 / 判据口径 | 目标码在生成口径 ctx | 目标码在判据口径 ctx |
|---|---|---|---|
| q35 | 15905 / 31549 | C49488, C66734, C78735, C78737 (全在) | 一个都不在 |
| q31 | 22715 / 18286 | C125923 (在) | 不在 |
| q72 | 27185 / 25219 | C172330 (在) | 不在 |

成因: hybrid 融合 + structured-lookup union-add 改变了 top-15 的构成, **把真正含这些码的
chunk 挤了出去**。模型当时看得见这些码, 判据脚本重建时看不见。

**⛔ 记录状态**: 上方结果表**维持** (a)=FAIL / verified=false 不变 —— 判据点名的是
`check_code_grounding.py`, 预登记不因结果难看而改。是否修判据口径, 需用户第二次裁定。

### V-1 保真度实证 (决定性): 重建 top5 vs 落盘 top5_sources

上面"参数对上了"只是论证。用 run json 里**已落盘**的 `top5_sources` 直接验重建是否忠实
(零 LLM 生成, 只走检索):

| 重建口径 | 重建 top5 == 落盘 top5_sources |
|---|---|
| 生成口径 (lookup/hybrid/rerank OFF, expansion=none) | **102 / 102** |
| 判据口径 (`check_code_grounding.py` 写死 lookup/hybrid=ON) | **0 / 102** |

⇒ 判据脚本重建的上下文**在 102 题上无一还原模型当时看见的检索结果**。
"哪个口径符合'上下文'的定义"由这组数据判定, 不是事后选的。

复跑 (见 worklog `.work/meta/worklog/phase07.md` 同日条目附完整脚本):
两台 `RAGEngine` 只差 `structured_lookup_enabled` / `hybrid_enabled`, 逐题比
`[c.source for c in eng.retrieve(q)][:5]` 与 `result["top5_sources"]`。

### 发现 V-2: max_tokens 从未显式设置 (litellm provider 默认)

`eval/run_eval.py:355` 的 `comp_kwargs` 只放 `messages` (+ 可选 `temperature`), **从不设
`max_tokens`** ⇒ 4096 是 litellm 对 Bedrock Converse 的默认值, 不是任何人选的。
不同 provider 默认值不同 ⇒ 四模型会有**不同的截断率**, 而截断会少发码
⇒ 话痨模型在 (a) 层显得更干净。这是跨模型比较的系统性混淆, 应在跑其余三个模型前显式钉死。

本轮影响有界: 仅 q36 / q83 两题截断, q36 发 **0** 个码、q83 发 **3** 个码且全 grounded,
两题 fact_recall / source_recall 均 1.0。

### 成本提示: (b) 层是额外开销

`class_assertion_scan.py` 是**逐答案**问裁判 ⇒ **102 次裁判调用 / 模型**, 在 102 次生成之外。
四模型全跑 = 408 次生成 + 408 次裁判 = **816 次**, 而非"408 次"。

## ※ 判据修订记录 (2026-09-03) —— 结果表上方数字据此改过, 必须连读

⛔ **本文件"判据"与"自毁条款"两段仍一字未动。** 被改的是判据**点名的那个脚本**
`eval/prod_wirein/check_code_grounding.py`, 属对预登记判据的**实质修订**, 记录如下:

| 项 | 内容 |
|---|---|
| 谁裁定 | 用户, 2026-09-03, 在看过 V-1 诊断数据之后 |
| 改了什么 | 重建上下文的检索口径: 原**写死** `structured_lookup=ON, hybrid=ON` → 改为**读报告落盘的 `retrieval_levers`** (老报告退回 run_eval 默认全 OFF) |
| 阈值动了吗 | **没有。** 仍是 0 ungrounded / 0 nonexistent |
| 判据变松还是变紧 | **变紧**: 新增两道 fail-loud 闸, 任一触发即**拒绝出数** (见下) |
| 对 opus-5 的影响 | (a) 由 FAIL(8 ungrounded) 变 PASS(0) —— 8 条经实证全是口径差假阳性 |

**⚠ 修订发生在看过数据之后, 且方向对被测对象有利。** 这个事实必须摆在明面上。
支持它不是"挑数字"的证据是可复核的:

1. 方向不是选的, 是数据判的 —— 判据说码要 grounded 在"上下文"里, 而"上下文"只有一个
   定义(模型当时看见的那个)。哪个口径符合定义: 生成口径重建 **102/102** 还原落盘
   `top5_sources`, 旧写死口径 **0/102**。
2. 阈值一个没动。
3. 新脚本比旧的**更容易 FAIL**, 不是更容易 PASS:
   - `ReconstructionMismatchError` —— 重建 top5 != 落盘 top5 ⇒ 拒绝出数
     (变异实证: 把 `retrieval_levers` 改回旧写死值, q01 当场炸, 不再安静报 8 条);
   - `DegenerateContextError` —— KB 中不存在的 `C99999` 出现在上下文里 ⇒ 上下文疑似退化
     成整库 ⇒ 拒绝出数 (堵的是本判据**唯一的假 PASS 通道**, 保真闸拦不住它,
     因为那条 bug 在 `format_context` 而非 `retrieve`)。

**复跑 (判据本身)**
```
cd sdtm-rag
.venv/bin/python eval/prod_wirein/check_code_grounding.py \
    evidence/checkpoints/verified_runs/run_opus-5.json on
# -> 重建保真: 102/102 ✓ ; codes=454 grounded=454 ungrounded=0 NONEXISTENT=0 -> PASS
```

**复跑 (闸有没有牙 —— 变异)**
```
python3 -c "import json;d=json.load(open('evidence/checkpoints/verified_runs/run_opus-5.json'));\
d['summary']['retrieval_levers']={'top_k':15,'structured_lookup':True,'hybrid':True,\
'rerank':False,'query_expansion':'none'};json.dump(d,open('/tmp/mutant.json','w'))"
.venv/bin/python eval/prod_wirein/check_code_grounding.py /tmp/mutant.json on
# -> ReconstructionMismatchError: q01 ... 拒绝出数
```

### V-2 的修复 (同日, 同一裁定)

`eval/run_eval.py`: 生成调用改走 `build_completion_kwargs(...)`, **显式**带
`max_tokens`(新常量 `MAX_TOKENS = 8192`, 可用 `--max-tokens` 覆盖); 报告 summary 新增
`max_tokens` 与 `truncated`(撞顶题 id), 撞顶时 stdout 打 `⚠ TRUNCATED ...`。
⇒ 截断不再静默, 且四模型共用同一上限 (provider 默认值不同会造成差异化截断率)。

⚠ **opus-5 那轮是在修复前跑的**, 上限仍是 4096, q36/q83 截断照旧存在 —— 这是本轮
**未消除**的 known limitation, 影响有界 (q36 发 0 码 / q83 发 3 码且全 grounded)。
其余三个模型将在 8192 下跑, 与 opus-5 **上限不同**, 跨模型比较时须记住这一点。

### 回归证据

`.venv/bin/python -m pytest scripts/tests -q` → **exit 0, 2043 passed / 1 skipped / 0 failed**
(修改前基线 2023 passed; 新增 20 条测试:
`test_code_grounding_fidelity.py` 9 · `test_run_eval_max_tokens.py` 6 ·
`test_run_eval_report_provenance.py` 5)。
`test_run_eval_flags.py` 的两个 FakeEngine 补了 4 个属性 —— summary 读引擎实收值,
替身缺属性会 AttributeError; 补替身而非在生产代码里 getattr 兜底 (兜底会把"记实收值"退回猜)。
