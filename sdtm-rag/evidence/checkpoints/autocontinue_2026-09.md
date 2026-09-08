# 无上限饱和回答: 显式 max_tokens + 触顶自动续写 (2026-09-08)

> 状态: **已完成** (2026-09-08)
> 相关: `server/config.py` · `server/llm_config.py::create_router` · `server/router.py`
> (`ask` / `ask_stream`) · `webchat/js/{stream,render}.js` · `webchat/app.js`
> 研究报告: `.superpowers/research-max-output-tokens.md`

## 1. 病症与证据

一条真实回答 (VS 域用法 + 本研究映射, ~3.5k 汉字) 在 **≈4k output token** 处**半句话被
切断**, 界面上没有任何提示 —— 用户既不知道答案没写完, 也不知道为什么。

根因链:

1. `server/router.py` 从不传 `max_tokens`。
2. `bedrock/converse/...` 这条路径下 litellm (1.88.1,
   `llms/bedrock/chat/converse_transformation.py:1103-1128`) **只在**"开了 thinking 又没给
   max_tokens"那一支才补 `maxTokens`; 其余情况该字段整个不进请求体。
3. Bedrock 于是用服务端默认值。AWS 的 `InferenceConfiguration` 文档说默认是"模型允许的
   最大值", 但**实测截断在 ≈4k**, 远低于 opus-5 的 128K ⇒ 那个默认值不是模型上限。
   **截断本身就是证据**, 不需要再证明什么。

⚠ 这条路只影响 `bedrock/converse/*`。四个 `anthropic/*` 直连串走的是
`AnthropicConfig.get_max_tokens_for_model()`, litellm 会替你注入真实上限 —— 但生产 `.env`
把 default/hard/light 三组**全指到了 Bedrock**, 所以那条"安全"的路径在这里是不生效的。

## 2. 设计

### (A) 天花板: 每个 deployment 显式 `max_tokens`

写在 `create_router` 的 **`litellm_params`** 里, ⛔ 不是 per-call kwarg。两条理由:

1. **回退目标要带自己的天花板**。答题组回退到 `default-fallback` (DeepSeek) 时, per-call
   的 `max_tokens` 会被原样带过去, DeepSeek 就被扣上一个按 Claude 量的数。deployment 级
   则各组各带各的。
2. 不写 = 静默截断 (§1)。

| Router 组 | 模型串 (生产 .env 解析后) | max_tokens | 出处 |
|---|---|---:|---|
| `opus-5` | `bedrock/converse/global.anthropic.claude-opus-5` | 128000 | AWS model card 一手 |
| `sonnet-5` | `bedrock/converse/global.anthropic.claude-sonnet-5` | 128000 | AWS model card 一手 |
| `gpt-terra` | `bedrock/converse/global.openai.gpt-5.6-terra` | 128000 | ⚠ **无一手文档**, 仅 litellm 静态表 |
| `gpt-sol` | `bedrock/converse/global.openai.gpt-5.6-sol` | 128000 | ⚠ **无一手文档**, 仅 litellm 静态表 |
| `default` | `bedrock/converse/global.anthropic.claude-opus-5` | 128000 | 注释按 config.py 默认 (sonnet-4-6) 写 |
| `hard` | 同上 | 128000 | 同上 (opus-4-7) |
| `light` | 同上 | 64000 | 按 config.py 默认 haiku-4-5 的 64K 取值 |
| `default-fallback` | `deepseek/deepseek-v4-pro` | 32000 | ⚠ 保守值; DeepSeek 无一手文档 |

⚠ **接缝**: `.env` 改的是模型串, **不会**自动改天花板。错配的两个方向都不是静默的 ——
低了只是封得更严 (续写兜得住), 高了 provider 当场 `ValidationException`。`light` 现在正
处于"低了"这一侧 (64K 封在一个 128K 的模型上), 而判库/改写只吐几十个 token, 无影响。

### (B) 兜底: 触顶自动续写

用户裁定: **不要手动"继续"按钮, 服务端自己续到写完**。

- 判据: 本轮收尾理由 ∈ `{"length", "max_tokens"}` (前者 OpenAI/litellm 归一化后的拼法,
  后者 Anthropic 原生) **且**本轮没攒到工具调用。
- 动作: 往 `msgs` 追加 `assistant(本轮原文)` + `user(CONTINUE_PROMPT)`, 发一个
  `continue` SSE 事件, 用**同样的 `with_tools`** 再开一轮, token 继续流进同一个答案。
  ⚠ 本轮**一个可见字都没吐**时不加锚, 原样重开 —— 实测逼出来的一支, 见 §3b。
- 上限: `max_continue_rounds` (默认 8)。撞上限仍触顶 ⇒ `done.truncated = true`。
- `done` 永远带 `continue_rounds: int` 与 `truncated: bool`。

⚠ **为什么追加 user 消息而不是 assistant prefill**: prefill (把上一轮原文塞成最后一条
assistant 消息让模型接着补全) 是 Anthropic 特有能力, 走 Bedrock Converse 的两个 GPT 模型
不支持。同一段代码要服务四个可选模型 + DeepSeek 兜底, 只能用所有 provider 都认的形状。

⚠ **续写不消耗工具轮预算**: 内层 `while` 嵌在 `for rnd` 里面, 而不是把 `total_rounds`
加大 —— 后者会让"续写"偷偷买到额外的搜索机会。同时有工具调用又报触顶时**工具优先**,
走原有路径 (那一轮的文本本来就会被回灌进 assistant 消息)。

### (C) 两个端点都要

`/api/ask` (同步 `completion`) 与 `/api/ask_stream` (异步 `acompletion`) 是**两份**实现,
不共用辅助函数。只改流式的话, eval 脚本 (全走 `/api/ask`) 会继续静默拿到被截断的答案去
打分 —— 那是最不该被截断的地方。两边共用同一对常量
(`CONTINUE_PROMPT` / `_TRUNCATED_FINISH_REASONS`), ⛔ 不许各抄一份。
`AskResponse` 加了同名两字段, 默认值是"没发生过", 老调用方一行不改照常工作。

### (D) 前端

流中**不画任何东西** —— 正文是连续的, "这里换了一次 API 调用"是实现细节
(`onContinue` 只留一条 `console.debug`)。done 之后分两种:

| 情形 | 呈现 |
|---|---|
| `continue_rounds > 0` 且未触顶 | `.chip.continue`「自动续写 ×N」, 灰色 |
| `truncated === true` | `.turn-note.warn`「⚠ 已达自动续写上限 (N 轮), 回答可能不完整」, 琥珀色 |

chip **刻意不用琥珀色**: 续写完成的答案是完整的, 画成警告与本功能目的相反。
两字段进 localStorage 并在 `messageEl` 复原 —— 与 `webStatus` / `fellBack` 同一条教训:
只在 `onDone` 里画的话, 存档里一条被截断的答案与完整答案长得一模一样。

## 3. 探针实测 (2026-09-08)

脚本 `.superpowers/probe_max_tokens.py` (一次性, **不提交**)。用真 `create_router(Settings())`
(含 `.env` 覆盖 + deployment 级 `max_tokens`), `fallbacks` 与 `num_retries` 都关掉 ——
否则某个 deployment 被拒会静默落到 DeepSeek 上答成功, 探针就报了个假绿。

```
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
.venv/bin/python ../.superpowers/probe_max_tokens.py
```

| group | max_tokens | 结果 |
|---|---:|---|
| opus-5 | 128000 | OK |
| sonnet-5 | 128000 | OK |
| gpt-terra | 128000 | OK |
| gpt-sol | 128000 | OK |
| default | 128000 | OK |
| default-fallback | 32000 | OK |
| hard | 128000 | OK |
| light | 64000 | OK |

**8/8 provider 接受**, 无一处 `ValidationException` ⇒ 没有任何模型的天花板需要下调。

⚠ **这条实测证的是什么**: provider **接受**这个 `max_tokens` 参数值。它**不**证明模型真
的会吐满 128K, 也不证明 128K 就是 GPT-5.6 Terra/Sol 的真实上限 —— 那两个值仍然只有
litellm 静态表背书。真实上限若低于 128000, 表现是"到那个数就触顶", 而触顶已经由自动续写
兜住了 (代价只是多几次调用)。

## 3b. 端到端实测: 真 Bedrock 上真的接着写了吗 (2026-09-08)

脚本 `.superpowers/probe_e2e_continue.py` (一次性, **不提交**): 真 `create_router` + 真
`/api/ask_stream` (fake RAG 只为跳过检索), 把 opus-5 的 `max_output_tokens` 压到 4000 逼出
真实续写, `fallbacks` 关掉。

| 指标 | 值 |
|---|---|
| API 调用 | 3 次 (`continue` 事件 2 次) |
| 正文 | 19,310 字符 / 111 行 |
| `done.truncated` | **false** (第 3 轮模型自然收尾) |
| `usage.completion_tokens` | 11,430 (跨 3 轮累加) |

**接缝质量** (对产出全文做的机械核验, 非目测):

| 检查 | 结果 |
|---|---|
| 重复的长行 (>25 字符) | **0** |
| 重复标题 | **0** (17 个标题各不相同) |
| 接缝元话语 (Continuing…/Sorry…/Resuming…) | **0** |
| 文档结构 | `# 标题` → `## 1. Purpose and Scope` → … → `## 10. Summary`, **跨 3 次调用连续编号** |

⇒ 病症侧的 ≈4k token 截断已被消除 (19,310 字符 ≫ 事故那条的 ~3.5k 汉字), 且
`CONTINUE_PROMPT` 在 opus-5 上实测有效。

### ⚠ 空轮: 实测逼出来的一个真缺陷 (已修)

同一个探针把天花板压到 200 / 1200 时, **某一轮 `delta.content` 一个字都没有却报
`length`** —— 预算被模型的内部思考吃光了 (仓库有意丢弃 `reasoning_content`, 但那些
token 照样计入 `max_tokens` 与 `completion_tokens`)。

按初版设计照做 (回灌 `assistant: 本轮原文`) 就是回灌 `assistant: ""`:

- litellm 当场警告 `Potential consecutive user/tool blocks. Trying to merge.`, 把空消息
  丢掉并合并相邻的两条 user 块;
- 模型于是收到一句"从断处接着写"却**没有可接的东西**, 只能凭空编一个续写点。实测产物
  是从中段小标题 `### Timing variables and the temporal anchoring of measurements` 开始
  的、**没有开头**的文章 —— 一个"看起来像答案"的错误产物。

修法: 本轮没吐字就**什么都不加**, 原样重开一轮 (预算刷新)。两个端点都改, 由
`test_{ask_stream,ask_non_stream}_empty_round_retries_without_an_empty_anchor` 钉住
(先红后绿)。

## 4. 复跑命令

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag

# 后端: 续写循环 (流式 4 条 + 非流式 3 条)
.venv/bin/python -m pytest scripts/tests/test_ask_stream.py -q -o addopts=""

# 天花板: Router 每个 deployment 都带值 + 字面量锚
.venv/bin/python -m pytest scripts/tests/test_model_switching.py -q -o addopts="" \
  -k "max_tokens or documented_numbers"

# SSE 契约 (后端事件 ⊆ 前端 dispatch 认得的) + 前端真浏览器呈现
.venv/bin/python -m pytest scripts/tests/test_sse_contract.py \
  scripts/tests/test_webchat_stream_render.py -q -o addopts=""

# 前端单测 + 全量回归
node --test 'webchat/tests/*.test.mjs'
.venv/bin/python -m pytest scripts/tests/ -q -x \
  --ignore=scripts/tests/test_build_neo4j.py -o addopts=""

# 真打网的三个探针 (一次性脚本, 不在仓库里; 合计约几分钱到一两毛)
.venv/bin/python ../.superpowers/probe_max_tokens.py      # 天花板 provider 收不收
.venv/bin/python ../.superpowers/probe_finish_reason.py   # 触顶时 finish_reason 写什么
.venv/bin/python ../.superpowers/probe_e2e_continue.py    # 端到端真的接着写吗
```

## 5. 已知边界

1. **接缝处依赖模型听话**。续写靠 `CONTINUE_PROMPT` 让模型"从断处接着写、不要重复"。
   §3b 在 opus-5 上实测接缝干净 (0 重复行 / 0 重复标题 / 0 元话语, 章节跨调用连续编号),
   但那是 **n=1**, 不是保证。模型不听话时接缝处可能重复半句或补一段小标题。
   **没有**程序化的去重 —— 自动去重需要猜"重复到哪里算重复", 猜错会**删掉真内容**,
   比留一句重复严重得多。
2. **8 轮上限只是跑飞兜底, 不是预期值**。天花板抬到 128K 之后正常回答一轮就该写完; 真
   跑到 8 轮说明模型在打转, 那时 `truncated: true` + 前端警告如实呈现, 不假装完整。
3. **gpt-terra / gpt-sol 的 128000 未经一手文档确认** (§3 末段)。
4. **DeepSeek 的 32000 是保守值, 不是实测上限**。极长回答走到 fallback 时会多续写几轮 ——
   功能正确, 只是多几次调用。
5. **探针只证"参数被接受"**, 不证"能吐满"。
6. **真实 `finish_reason` 已实测, 但只在这三条路上**
   (`.superpowers/probe_finish_reason.py`, per-call `max_tokens=200` 逼出触顶):
   opus-5 / gpt-terra / default-fallback(DeepSeek) 报的都是 **`length`**, 均被
   `_TRUNCATED_FINISH_REASONS` 认下。`"max_tokens"` 那个拼法**没有**在本仓库观测到 ——
   它是照 Anthropic 原生 API 的文档留的保险, 不是实测所得。
7. **空轮重试可能空转**。修完之后, 一轮全花在内部思考上时会用同样的 msgs 重开 ——
   模型若每轮都这么干, 8 轮全空转后以 `truncated: true` 收场。天花板压到 1200 时实测
   就是这样 (3 轮 0 字符)。生产的 128K 下到不了这一支; 也**没有**为它加特殊处理, 因为
   任何"猜模型为什么不吐字"的逻辑都比这条诚实的兜底更容易出错。
8. **本轮实测只覆盖 opus-5** 的长答案续写。另外三个可选模型的接缝质量未测。
