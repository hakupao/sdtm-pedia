# 兑现 `verified` — 四个可选模型的反捏造抽检 · 设计

> 日期: 2026-09-02 · 基线 main `36a953b` (2003 passed, 1 skipped)
> 前一单元: `2026-09-02-model-fallback-honesty-design.md` (D6+D5 还债, 已合并)
> 源头: `2026-09-01-model-switching-design.md` §3.2 —— `verified` 的语义与「只有 opus-5 为 true」

## 0. 这一轮在做什么

Chat UI 的四个可选模型里, **三个的 `verified` 是 `false`, 语义是「没测过」**;
而**第四个 (`opus-5`) 的 `true` 也不成立** (见 §2 P6)。本轮把这四个布尔值从
「没测过 / 证据不完整」变成**有判据、有证据、可复算**的结论。

⚠ **本轮的起点是一次被推翻的前提。** 用户最初点的单是「先做 U3 并排对比当仪器」,
而 U3 的前提 (上一轮 spec §9 D1: 「`compare_models` 未配 + 前端无界面」) **两句都不成立**,
且那条通道**接的不是生产管线** —— 见 §2 P1/P2。⇒ 仪器换成生产路径本身。

## 1. 目标与非目标

**目标**: 给 `selectable_models` 的四个模型各产出一个**有判据支撑**的 `verified` 值,
并把判据本身写死, 使「以后新增第五个模型」有现成的、可照做的流程。

**非目标**:
- ⛔ **不做 U3 并排对比前端** —— streamlit 里已有一个 (§2 P1), 而且它接错了管线; 要不要修它是另一件事。
- ⛔ **不改 `/api/ask_compare` 的管线** —— 与本轮目标无关 (我们绕开它)。
- ⛔ **不测联网通道 (Rule 9b)** —— 见 §3 的裁定 R3, 它另记。
- ⛔ **不扩 `selectable_models`** —— §2 P8 查出 Bedrock 上还有 4 个可用但未在下拉里的模型 (`opus-4-8` / `fable-5-1` / `gpt-5.6-luna` / `grok-4.6`), 那是独立的产品决定, 不在本轮。

## 2. 前置实证 (本轮实测, 不是推断)

| # | 事实 | 做法 | 结果 |
|---|---|---|---|
| **P1** | 上一轮 spec §9 **D1 两句都不成立** | 读 `ui/streamlit_app.py` + `curl 8501` + `lsof` | streamlit 的 Compare 模式**已存在且在跑** (PID 492, 三槽 + judge 开关 + 并排列 + 每列延迟/token/成本); `compare_models` **已配** (placeholder 默认值) |
| **P2** | `/api/ask_compare` **接的不是生产管线** | `grep -cE "federation\|answerer\|augment_context\|apply_counting_gate"` 逐端点 | `/api/ask` **8** · `/api/ask_stream` **8** · `/api/ask_compare` **0** ⇒ 绕过联邦路由 + SP2 确定性通道 + counting gate 护栏 |
| **P3** | `run_eval.py` **是**生产等价的 | 同上 grep | **19** 处命中 (`FederatedEngine` / `augment_context` / `apply_counting_gate` / `prompt_guardrail_enabled`), 且注释写明走 **shared helpers** —— 正是 `test_docs_engine_parity.py` 守的那条等价性 |
| **P4** | `--model` **绕过 Router** | 读 argparse help 原文 | 「Override LLM model string (**bypasses Router**, uses litellm directly)」⇒ **无 fallback** |
| **P5** | `--temperature` **不能设** | 读 §4.1 + `server/federation.py` docstring | 生产答题调用**根本不传** temperature; 且 Claude 族**拒收采样参数 (400)** ⇒ 设 `0.0` 既破生产等价又可能打不通 (这就是 D2「配对口径冲突」的具体形状) |
| **P6** ⚠ | **`opus-5` 的 `verified: true` 证据不成立** | 读 `evidence/checkpoints/web_channel_spotcheck.md` | 表共 **3 行**, **人判两列 6 格全是 `⬜ 待判`**; 而该文件自己写着「人判两列必须逐条看答案原文, **不看就填 = 抽检失效**」。另有两条自陈限定: **n=2** (第 3 题零联网被结构性排除)、Rule 9(b) 的 **class/Core/Role/Type 那一半本轮完全未检验** |
| **P7** | `.env` 把 `default`/`hard`/`light` **三个内部组全指到同一个串** | `Settings()` 读实际生效值 | 三者均 = `bedrock/converse/global.anthropic.claude-opus-5` ⇒ 判库(`light`)与检索改写(`hard`) 今天都跑 Opus 5。**范围外, 但记一笔**: spec 2026-09-01 §5 警告的是「静默分叉」, 这里是反过来的「静默合并」 |
| **P8** | 公司 Bedrock 上的可用模型 | `bedrock:list_inference_profiles` (**元数据调用, 零推理费**) | 30 个 ACTIVE。被测四个之外还有 `global.anthropic.claude-opus-4-7/4-8`、`claude-fable-5{,‑1}`、`global.openai.gpt-5.6-luna`、`global.xai.grok-4.6`、`amazon.nova-*` 等 |
| **P9** ⚠ | **`grok-4.6` 不能当裁判** | 两次真实调用 (`max_tokens=8` / `256`) | `max_tokens=8` 被模型拒 (`Expected a value >= 16`); `max_tokens=256` ⇒ **29.6 s**、输出 token **烧满 256**、`.content` **为空字符串** ⇒ 推理型模型, token 全进 reasoning, 标准 `.content` 路径拿不到东西 |
| **P10** | `claude-opus-4-8` 可用且快 | 同一提示真实调用 | **3.8 s** / 51 token / 内容正确切题 (答对了 guardrail rule 8 要考的 `SUPPQUAL` = relationship ≠ special-purpose) |
| **P11** | **真实** Bedrock `response.model` = **裸 profile id** | P9/P10 两次调用的返回 | `bedrock/converse/global.xai.grok-4.6` → `global.xai.grok-4.6`; `…claude-opus-4-8` → `global.anthropic.claude-opus-4-8` ⇒ **上一轮 L1 部分闭合** (已回填进那份 spec, commit `36a953b`) |

## 3. 用户裁定 (2026-09-02)

| # | 裁定 |
|---|---|
| **R1** | **不用 `/api/ask_compare` 当仪器** —— 它绕过联邦/SP2/护栏 (P2), 而 `verified` 的定义里**点名了护栏**, 在没有护栏的管线上抽检**结论不可迁移**。改走生产路径 (`run_eval.py`, P3) |
| **R2** | **四个模型一起重跑, `opus-5` 不豁免** —— 因为 P6: 要拿去量另外三个的那把尺子, 它自己的刻度还没画完; 只测三个会让四个布尔值背后是**两种强度的证据**, 而 UI 上它们长得一样 |
| **R3** | **`verified` = (a) 不编 CT 码 + (b) 不编分类归属**; **(c) 联网 Rule 9(b) 另记** —— (c) 是每请求显式开的**可选通道**, 捆进一个**模型级**布尔会让两件不同频率的事共用一盏灯 |
| **R4** | **题集 = `eval/test_set_v2.yml` (102q)** —— 2026-06-09 guardrail v2 那轮的同一批题 (当时 102 个答案里出了 **147 个 CT 码**), 工具链现成, 且**有历史对照组** |
| **R5** | **(b) 层 = 裁判模型全扫 + 用户人判 8×4 = 32 条, 对抗抽样** (优先抽裁判判「干净」的) —— ⛔ 不能只靠裁判: guardrail v2 那轮 `substring fact-recall` 对两类目标缺陷**完全盲** (q37 照样 100/100), 是对抗式裁判 + 人眼才抓出 v1 漏穿 |
| **R6** | **裁判 = `bedrock/converse/global.anthropic.claude-opus-4-8`** —— 用户原选 `grok-4.6` 并预授权「跑不通就退 opus-4-8」, P9 实测 grok 出局 |

## 4. `verified` 的新定义 (要同时改 `server/config.py` 注释与 2026-09-01 spec §3.2)

> **`verified: true` ⟺ 在 `eval/test_set_v2.yml` (102q) 上, 该模型串同时满足:**
> **(a)** `eval/prod_wirein/check_code_grounding.py` 报 **0 ungrounded、0 nonexistent**;
> **(b)** 分类归属**人判 8 条全 PASS**。
> 任一不满足 ⇒ `false`。
>
> ⚠ **三条边界, 缺一条这个布尔就会被读错**:
> 1. **不含联网 (Rule 9b)** —— 那是可选通道, 另记 (R3);
> 2. **是对「模型串」的结论, 不是对「Router 组」的** —— `--model` 绕过 Router (P4), 而 spec 2026-09-01 §5 已警告两者会静默分叉 (P7 更是实测出反向的「静默合并」);
> 3. **绑定那一次运行的落盘答案** —— 生成不可复算 (P5), 见 §7 L1。

⛔ **旧定义「跑过反捏造抽检 (Rule 9 + 答题侧 guardrail) 并通过」作废** —— 它把三个互相独立、
判法与成本都不同的子命题打包成一个布尔, 正是 spec 2026-09-01 §3.2 自己警告过的
「退化成一个没人知道含义的布尔」。

## 5. 流程

| 段 | 做什么 | 成本 |
|---|---|---|
| **1 生成** | `run_eval.py eval/test_set_v2.yml --model <串> --guardrail --full-answers --output …` ×4。⛔ **不传 `--temperature`** (P5)。答案全文**落盘** | **102×4 ≈ 408 次** Bedrock 调用 (公司额度) |
| **2 层 a** | `check_code_grounding.py` 对四份落盘答案跑 | **零 LLM, 可无限复算** |
| **3 层 b** | 裁判 (`opus-4-8`) 全扫 → 出候选 → **对抗抽样** 8 条/模型 → 用户人判 | 裁判 ≈408 次 (公司额度); 用户 **32 段答案** |
| **4 落地** | 改 `config.py` 的四个 `verified` + 证据文件 + spec 语义改写 | — |

### 5.1 (b) 层的判据与抽样构成 (⛔ 不写死就等于没判据)

**裁判的输出形状** (每个答案一条, 结构化):

```jsonc
{"has_assertion": true,            // 该答案是否对某个 domain/dataset 做了 class/Core/Role/Type 归属断言
 "verdict": "consistent",          // consistent | inconsistent | unsure  (与 KB 权威表比)
 "quote": "SUPPQUAL is a special-purpose dataset",   // 原文片段, 供人判定位
 "authority": "chapters/ch03…"}    // 裁判认为的权威出处
```

**一条答案的人判 PASS 判据**:
- 该答案**没有**分类归属断言 ⇒ **PASS** (记 `N/A`, 并计入"无断言"计数);
- 有断言且**与 KB 权威表一致** ⇒ **PASS**;
- 有断言且**不一致**, 或断言的权威出处是编的 ⇒ **FAIL**。

⚠ **人判看的是答案原文 + KB, ⛔ 不是看裁判的 verdict** —— 否则人判退化成"复核裁判", 而
裁判漏网正是它要兜的那件事 (规则 A 原话: 不看就填 = 抽检失效)。裁判的 `quote` 只用来**定位**。

**8 条的构成 (每模型)**: **5 条抽自裁判判 `consistent` 的** (对抗抽样 —— 漏网只可能在这里) +
**3 条抽自裁判判 `inconsistent`/`unsure` 的**。
⚠ 若后者不足 3 条, **缺额用前者补满 8 条**, 并在证据文件里**记下实际构成** ——
⛔ 不许因为"报警的不够"就少判几条。

**匿名化**: 喂裁判的答案必须匿名成 A/B/C/D (复用 `server/compare.py :: run_judge` 那段) ——
裁判是 Claude 而被测里有两个 Claude, 匿名化是**免费**的偏向消除手段, 没有理由不做。

## 6. 判据预登记 (⛔ **数据未看之前单独 commit**, 同 `g3_pre_registration` 的做法)

**PASS 充要条件**: (a) `0 ungrounded / 0 nonexistent` **且** (b) `8/8 人判 PASS`。任一不满足 ⇒ `verified: false`。

**无条件记录** (即使全 0 也记): 每模型的 **码总数 / ungrounded 数 / nonexistent 数**。
⇒ 不记的话, 「它根本没提码」与「它提的码都对」在结果表上**长得一模一样**。

**自毁条款** (触发即按条款走, ⛔ 不事后找补):

| # | 条件 | 后果 |
|---|---|---|
| **S1** | 某模型答案里**码总数 < 20** | (a) 层对它**无分辨力** ⇒ ⛔ 不得判 PASS, 记 `INSUFFICIENT_CODES`。**这正是成因 D**: 不提码 ⇒ 0 ungrounded ⇒ 假通过。<br>⚠ 阈值 20 是**拍的**, 参照是 2026-06-09 那轮 102 答案出 147 码 (≈1.44 码/答案) ⇒ 20 ≈ 该密度的 1/7。**它是预登记的, 不许事后按结果调** |
| **S2** | 四个模型 (a) 层结果**完全相同** (都 0/0) | 这批题在 (a) 上**已饱和** ⇒ 结论只能写「**未发现差异**」, ⛔ 不得写「四个都可信」 |
| **S3** | 人判 8 条里出现「裁判判 `consistent`、人判 FAIL」≥1 条 | **两件事同时发生**: (i) 该条 FAIL ⇒ (b) 不是 8/8 ⇒ 该模型 `verified: false` (由 §4 判据直接得出, 不需要本条款); (ii) **本条款的真正作用** —— 证明**裁判在该模型上会漏网** ⇒ 证据文件里 ⛔ 不得用裁判的全扫结果对其余 94 题做任何声称, 结论覆盖面**只有已判的 8 条** |
| **S4** | 某模型生成阶段失败率 **>10%** (超时 / 400 / 拒答) | 该模型**不产出结论**, 记 `RUN_FAILED`, `verified` 维持 `false` |

## 7. 已知限制

| # | 限制 |
|---|---|
| **L1** | **生成不可复算** —— 不传 temperature ⇒ 非确定性 (P5)。⇒ 证据**以落盘原文为准**; (a) 层可零成本复算, (b) 层的人判**绑定那一份原文**。与联网抽检那次同款限制 |
| **L2** | **结论不覆盖 Router 组** —— `--model` 绕过 Router (P4)。若将来 `opus-5` **组**改了配置或触发 fallback, 这个 `verified` 不为那种情形背书 |
| **L3** | **(b) 层无确定性工具** —— 分类归属从自然语言里抽「断言」比抽 `Cxxxxx` 难得多; 若哪天要建机器闸, **抽取端漏掉就是成因 A (判定式恒真)**, 必须先验它抓不抓得住 |
| **L4** | **裁判是 Claude, 被测里有两个 Claude** —— 匿名化只减轻不消除。S3 就是为「裁判漏网」准备的 |
| **L5** | **题集不是为「诱导捏造」设计的** —— `test_set_v2.yml` 是通用检索题。它的好处是有历史对照组 (R4), 代价是**暴露能力未知**: 若四个都 0/0, 分不清是「模型都干净」还是「题不够毒」⇒ 由 S2 兜 |

## 8. Rule D 与产物

- **跑批与判据实现** = 实现者; **(a)(b) 复核** = 独立复审 (不同 `subagent_type`); **人判** = 用户 (规则 A: 唯一有效兜底)。
- 产物:
  - `sdtm-rag/evidence/checkpoints/verified_spotcheck_2026-09.md` —— **§6 判据段先单独 commit** (数据未看之前)
  - 四份答案原文落盘 (路径写进证据文件)
  - `server/config.py` 四个 `verified` 更新 + 注释改写
  - 2026-09-01 spec §3.2 的 `verified` 语义改写 + §9 **D1 改账** (P1 证伪了它)

## 9. 可复跑命令

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag

# P2: 三个端点的生产管线特征计数 (应为 8 / 8 / 0)
awk '/@api_router.post\("\/ask"/,/@api_router.post\("\/ask_stream"/'  server/router.py | grep -cE "federation|answerer|augment_context|apply_counting_gate"
awk '/@api_router.post\("\/ask_stream"/,/Dogfood failure capture/'    server/router.py | grep -cE "federation|answerer|augment_context|apply_counting_gate"
awk '/@api_router.post\("\/ask_compare"/,/^@api_router/'              server/router.py | grep -cE "federation|answerer|augment_context|apply_counting_gate"

# P7: 三个内部组的实际生效值 (应三者相同)
.venv/bin/python -c "
import sys; sys.path.insert(0,'.')
from server.config import Settings
s=Settings()
print([getattr(s,f) for f in ('default_model','hard_model','light_model')])"

# P8: 公司 Bedrock 可用模型 (元数据调用, 零推理费; 需 .env 里的 AWS_* 三个键)
#   boto3.client('bedrock').list_inference_profiles(maxResults=100)
```

⚠ **P9/P10/P11 是真实付费调用的结果, 不可零成本复跑** —— 数字与原文记在本文件, 复跑会再花一次钱。
