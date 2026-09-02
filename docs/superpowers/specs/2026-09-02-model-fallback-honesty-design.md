# D6 + D5: `model_used` 上闸 + 恢复容灾且诚实呈现 — 设计

> 日期: 2026-09-02 · 分支 `fix/model-fallback-honesty` · 基线 main `2bcd840` (**1956 passed, 1 skipped**)
> 前一轮: `docs/superpowers/specs/2026-09-01-model-switching-design.md` (U1 多模型切换) §9 D5 / D6
> 前一轮账本: `.superpowers/sdd/2026-09-01-model-switching/{progress,final-review}.md`

## 0. 这一轮在还什么

U1 落地时留下两笔互相咬合的债 (spec §9):

- **D5** —— **上一轮自己引入的生产回归**: 分支前 Chat UI 永发 `default` 组 (有
  `fallbacks=[{"default": ["default-fallback"]}]` 兜底), 分支后按 §5 裁定**永发显式 id**
  落 `opus-5`, 而四个新派生组**没有 fallback 条目** ⇒ 主模型没变, **容灾网没了**。
  非理论风险: `sdtm-rag/DEPLOY_PLAN.md` 记着实测「Anthropic credits 耗尽 → DeepSeek 自动回退」
  真的生效过。
- **D6** —— `done` 事件的 `model_used` 字段**取值在整个测试套件里无任何断言**。

**顺序硬约束: D6 必须在 D5 之前。** 理由是上一轮 I-4 裁定的原话: 补 fallback 会**激活**
`model_id` (用户选的) 与 `model_used` (实际答的) 的分叉, 而 `model_used` 没有任何闸 ⇒
先补 fallback 等于**在没有闸的地方引入新行为**。终审 §7 ④ 也把这两条判为「同一件事的两面」:
今天 `model_used` 无断言之所以低风险, 正是因为四个新组没有 fallback。

## 1. 目标与非目标

**目标**: 恢复 Chat UI 主路径的容灾, 并让「实际答题的是谁」这件事在**答案徽章**与
**历史存档**两处都说真话。

**非目标**:
- U3 并排对比 / eval 多模型 / 换 embedding —— 与前一轮 §1 一致, 不动。
- 不改 `default` / `hard` / `light` 三个内部组的 fallback 布局 (C1: 判库/改写不受用户选择影响)。
- 不动 `/api/ask` (非流式) 的 `model_used` —— 它有 `AskResponse.model_used: str` 契约,
  streamlit 在读 (`ui/streamlit_app.py`)。本轮只动 SSE `done` 事件。

## 2. 用户裁定 (2026-09-02, 已批准, 不重新 brainstorm)

| # | 裁定 |
|---|---|
| R1 | D6 先做, D5 后做 |
| R2 | `create_router` 给四个 selectable 组各加 `fallbacks` → `default-fallback` |
| R3 | 后端在 `done` 事件算 `fell_back`: 拿 `model_used` 与**所选组配置的模型串**比对; 内部组无从判断 ⇒ 发 `null` |
| R4 | 前端徽章必须跟着变: 回退时显示「模型: GPT-5.6 Sol → 实际 deepseek-v4-pro（已回退）」, `verified` 按未知处理 |
| R5 | `modelUsed` + `fellBack` 一并存档, 历史记录同样诚实 |
| **R6** | (2026-09-02 追加, 由 Task 1 复审的 I-2 触发) 一次问答里**可能有多个模型各答了一段** ⇒ 按 **chunk** 收全实际报出的模型, `done` 加 `models_used` **有序去重列表**; `fell_back` = **任一个**不符即 `true`; 徽章用列表呈现 |

⚠ **R6 的来历必须写明, 否则它看起来像是凭空多出来的复杂度**: 原设计按 `model_used` (last-wins)
单值判定。Task 1 复审实测出两条路径会让它**静默说谎**:
1. **联网多轮** (`web_search_enabled` 默认 `True`, `web_max_rounds = 5`, 每轮是一次独立的
   `acompletion` ⇒ 每轮各自可能回退): 第 1 轮回退、第 2 轮落回主模型 ⇒ `model_used` 报主模型
   ⇒ `fell_back` 算成 `False` —— **回退了却不说**, 正是本轮要修的那件事本身。
2. **流中途回退** (见 §3 P6): 同一轮里就可能有两个模型的文字。

⇒ 按轮记都不够, 必须**按 chunk** 记。而代码本来就在逐 chunk 读 `.model`, 收成有序去重列表
是顺手的事。单模型场景 (绝大多数) 列表长度为 1, 文案与 R4 原样一字不差。

⚠ **R4 不能省的理由 (用户原话)**: 不做的话「用户选 Sol、DeepSeek 答题、徽章却说 Sol」——
就是刚修掉的 **C-1 (⚑ 归错模型)** 同族缺陷换了个位置。

## 3. 前置实证 (本轮实测, 不是推断)

计划里的断言必须先验过 —— 沿用上一轮 pre-flight 的规矩。

| # | 假设 | 实证做法 | 结果 |
|---|---|---|---|
| P1 | `Router` 暴露 `.fallbacks`, 就是构造时传进去的 list[dict] | `create_router(Settings()).fallbacks` | ✅ `[{'default': ['default-fallback']}]` |
| P2 | `fallbacks` 对 **`stream=True`** 也生效 (不只非流式) | 读 litellm `router.py` `acompletion` → 无论 stream 与否都走 `async_function_with_fallbacks` | ✅ 结构上成立 |
| P3 | 回退发生时, **流式 chunk 的 `.model`** 来自 fallback 部署而非主模型 | 真 `Router` + 手工加 `{"opus-5": ["default-fallback"]}` + monkeypatch `litellm.acompletion` (主模型抛错, fallback 返 `model="deepseek-v4-pro"` 的异步生成器) | ✅ `chunk model = deepseek-v4-pro` |
| P4 | `app.js` 顶层的 `function` 声明在 node `vm` context 里能从 sandbox 上取到 (探针要驱动 `send()` / `renderMessages()`) | 最小 sandbox `runInContext` 后查 `typeof sandbox.send` 等 | ✅ 四个全是 `function` |
| P5 | `TextEncoder` 在 vm sandbox 里**默认没有** (探针要造 SSE 字节流喂 `getReader`) | 同上 | ✅ `undefined` ⇒ 必须显式加进 sandbox |
| P6 | litellm **只**在开流阶段做 fallback | 读 litellm `router.py` / `exceptions.py` | ❌ **假的**。存在 `MidStreamFallbackError` + `_completion_streaming_iterator` 包装器: 迭代过程中抛出该异常会**在流中途**走 Router 的 fallback 链 (`stream_with_fallbacks` 用 `stream_chunk_builder` 拼回已收到的分片再续) |

可复跑命令见 §9。

⚠ **P3 的边界**: 它证的是「**开流阶段**失败 → Router 换 deployment → 后续 chunk 来自 fallback」。

⚠⚠ **本文初稿在这里写错过一句, 纠正过程本身要留档**: 初稿断言「流开成功之后中途断掉**不会**
触发 fallback」, 理由是 `CustomStreamWrapper` 已经返回给调用方了。**这句是错的** —— P6 实测
litellm 有 `MidStreamFallbackError` 的中途回退通道。错法很典型: 我从"P3 只测了开流阶段"推出
"litellm 只支持开流阶段", 把**自己实验的边界**当成了**被测系统的边界**。是 Task 1 复审的
越界观察提出的, 我读源码确认。⇒ 记进 retrospective: **"我没测到"不等于"它不存在"。**

修正后的准确说法 (§7 L2):
- **开流阶段**失败 (credits 耗尽 / 认证失败 / 限流) ⇒ Router 换 deployment, **已实测** (P3);
- **流中途**抛 `MidStreamFallbackError` ⇒ 也走 fallback 链, **源码级确认, 未实测**;
- 其余中途失败 (普通网络断) ⇒ 仍走 `event: error`。

⇒ 中途回退意味着**同一次回答里可能有两个模型的文字** —— 这正是 R6 要按 chunk 收全的第二个理由。

⚠ **P3 用的是我们自己造的 fake provider**, 所以它证的是「我们的接线 + litellm 的 fallback 机制」,
**不是**「真实 Bedrock/DeepSeek 回退时 chunk 里写的是什么串」。后者的唯一实测证据是 `DEPLOY_PLAN.md`
里 `/api/ask` 那次 (非流式, `response.model = deepseek-v4-pro`)。⇒ 见 §7 已知限制 L1。

## 4. 架构

### 4.1 D6: `model_used` 从"无人断言"变成"三向钉死"

`server/router.py` 的 `done` 事件当前发:

```python
yield sse("done", {"model_used": model_used or "default", ...})
```

`model_used` 由流式循环里 `getattr(chunk, "model", None) or model_used` 累积 —— 这是**事实层**
(实际答题的模型), 与 `model_id`(=`body.model`, **意图层**) 是两个东西。上一轮 Task 6 复审把这个划分
判为正确, 但**只给 `model_id` 配了闸, 没给 `model_used` 配**。

本轮补三个方向 (§6 闸表 G1-G3), 并顺手改掉一处**说谎**:

⛔ **`model_used or "default"` 必须改成发 `null`。**
chunk 一个都没带 `.model` 时, 真相是「不知道」, 而它现在**自信地报"default"**。这与同一个事件里
`verified` 的裁定 (spec §6:「不得发 `false`, 那会把'没这个概念'误报成'验过且不通过'」) 是同一条原则,
只是当时没顺手管到 `model_used`。本轮 R5 要求把 `modelUsed` **存进 append-only 的历史存档**,
一个编出来的 "default" 从此会被永久记下 —— 正是规则 B 最贵的那类数据被污染。

影响面已核: 全仓 `model_used` 的读取方只有 `ui/streamlit_app.py` 两处, 读的都是 `/api/ask`
的 `AskResponse`(非 SSE), 不受影响; SSE `done` 的这个字段**今天零消费方**。

### 4.2 D5.1: fallback 表从 `selectable_models` 派生

沿用上一轮 §3.1 的单一事实源原则 —— **不手写第二份清单**:

```python
fallbacks = [{g: ["default-fallback"]} for g in ("default", *(m.id for m in selectable))]
```

- `hard` / `light` / `default-fallback` **不进**这张表 (C1: 判库/改写不受用户选择影响;
  且给 `default-fallback` 自己配 fallback 是个环)。
- 这是**用户裁定 R2 覆盖了上一轮终审 I-4 的倾向**。终审当时建议"不补 fallback, 写进 spec 记录",
  理由是回退到 `default-fallback`(= DeepSeek **个人流量**) 作答与 C3 精神相左, 该由用户拍板。
  **用户已拍板: 补。** 代价 (答题可能落到个人流量的 DeepSeek) 由 R4/R5 的诚实标注承担 ——
  用户看得见、存档记得住, 而不是偷偷发生。

### 4.3 D5.2: `fell_back` 的判定

新函数 `server/llm_config.py :: fell_back(s, model_group, reported_models) -> bool | None`。
放这里而不是 `router.py`: "模型串长什么样"这类知识已经全在 `llm_config.py`
(`_INTERNAL_GROUP_MODEL_FIELDS` / `non_bedrock_model_groups` / `register_...` 都在处理前缀),
再开一处等于又造一份真相。

**输入是列表** (R6): `reported_models` = 本次问答里逐 chunk 收到的、**有序去重**的模型串。

判定规则:

| 输入 | 返回 | 理由 |
|---|---|---|
| `model_group` 不在 `selectable_models` 里 (default/hard/light/default-fallback) | `None` | **无从判断**。⛔ 不得返 `False` —— 与 `verified` 同一条原则 |
| `reported_models` 为空 | `None` | 同上, 不知道就说不知道 |
| **每一个**都与该组配置串同一个模型 | `False` | |
| **任一个**不是 | `True` | R6: 一次回答里只要有一段是别人答的, 就必须说 |

"同一个模型"的判据 (§3 P3 已实测 `reported` 是**去掉 provider 前缀**的串):

```python
configured == reported or configured.endswith("/" + reported)
```

`bedrock/converse/global.anthropic.claude-opus-5` vs `global.anthropic.claude-opus-5` ⇒ 相同。
⛔ **必须带 `/` 边界, 不许用裸 `in`** —— 裸子串正是 retrospective 规则 6 成因 A 的形状
(`claude-opus-5` 是配置串的子串, 但它不是一个完整的模型标识)。

`done` 事件加**两个**字段:

```jsonc
"models_used": ["deepseek-v4-pro", "global.openai.gpt-5.6-sol"],  // 有序去重, 逐 chunk 收
"fell_back":   true                                               // true | false | null
```

`model_used` (单值) **保持不动** = 最后一个报出的模型串。理由: 它是既有字段, Task 1 的三条闸
钉着它, 且"最后一段文字是谁写的"本身也是个事实。⇒ **两个字段各记一件事, 不拿一个冒充另一个**
(上一轮 Task 6 复审对 `model_id`(意图) / `model_used`(事实) 的划分给的就是这条理由)。

⚠ **`models_used` 的收集必须放在 `if choices:` 之外, 且不能覆盖式赋值** —— Task 1 修复轮已
把 `model_used` 的累积移出去并配了两条闸 (保值 / usage-only), `models_used` 沿用同一位置。

回退为真时打一条 `log.warning("model_fell_back", model_id=..., models_used=[...])` ——
让运维日志里也有痕迹, 不只在用户屏幕上。

### 4.4 D5.3/D5.4: 前端徽章与存档

`webchat/app.js`:

| 处 | 改动 |
|---|---|
| `onDone` | 多读 `data.models_used` / `data.fell_back`, 一律 `?? null` (三态语义, 与现有 `verified` 同款) |
| `persist` | 存档对象多存 `modelsUsed` / `fellBack` |
| `renderMessages` → `messageEl` → `renderModelBadge` | 多传这两个值; dataset 多存两项 (供 `refreshModelBadgeLabels` 原地补字) |
| `modelBadgeText` | 加回退分支 |
| `flagModelName` | 回退时归到**实际答题的模型** |

徽章文案 (三态 × 回退):

| `fellBack` | 文案 | `.unverified` 样式 |
|---|---|---|
| `true` | `模型: {label} → 实际 {modelsUsed.join("、")}（已回退）· 验证状态未知` | **是** |
| `false` / `null` | 与今天**逐字相同** (`模型: X` / `模型: X ⚠未验证` / `模型: X · 验证状态未知`) | 同今天 |

⚠ 单模型场景 (绝大多数) 列表长度为 1, 文案退化成 `模型: GPT-5.6 Sol → 实际 deepseek-v4-pro（已回退）· 验证状态未知`
—— 与 R4 原样一字不差。多模型只在联网多轮 / 流中途回退时出现。

⛔ 回退时**必须**盖掉 `verified` 那一支 (R4「verified 按未知处理」): `verified` 描述的是
**用户选的**模型验没验过, 而答案是**另一个**模型产的 —— 把 `opus-5` 的 `verified: true`
显示在一条 DeepSeek 答的消息上, 就是 C-1 同族。加 `.unverified` 琥珀色: 回退是**已知的偏离**,
不是单纯的元数据缺失, 值得与"未验证模型"同级的视觉提示。

**⚑ 归因** (`flagModelName`): 回退时返回 `` `${modelsUsed.join("、")}（回退自 ${label}）` ``。
`dogfood_failures.md` 是 append-only 的优先级 backlog (规则 B), 把 DeepSeek 的捏造记到
`GPT-5.6 Sol` 头上, 与终审 C-1 修掉的缺陷**一模一样**, 只是触发路径从"切 topbar 文本"
变成了"读 modelId 但答案不是它产的"。

## 5. 兼容性 —— 两个必须成立的降级方向

⚠ **`server/main.py` 把 `webchat/` 以 `StaticFiles` 从工作树挂载**, 每请求现读 ⇒
**改了 `app.js` 就立刻出现在用户正在跑的 launchd 服务上**, 而 Python 改动要重启才生效
(上一轮 Task 7 前置调查已实测)。所以下面第一条不是假想, 是**必然发生的中间态**:

| # | 场景 | 要求 |
|---|---|---|
| B1 | **新前端 + 老后端** (`done` 不带 `model_used`/`fell_back`) | `?? null` ⇒ 徽章与今天**逐字相同**, 不报错 |
| B2 | **新前端 + 老历史存档** (localStorage 里的旧消息没有 `modelUsed`/`fellBack`) | 同上 |

## 6. 测试闸 (每条都要能被变异打红, 两个方向都钉)

> 全局约束沿用上一轮: **变异验证一律跑整个测试文件, 禁用 `-k` 过滤**;
> 变异脚本必须**自证变异真的打上了** (改完 grep 回读 / 比 sha256);
> 还原用**字节回写**, ⛔ 不许 `git checkout -- <file>` (工作区有未提交修复时它撤销的是一切)。

| # | 闸 | 两个方向 |
|---|---|---|
| G1 | `done.model_used` = Router **实际返回**的串 | 正: `_CapturingRouter` 回 `resolved-{group}` ⇒ 断言等于它 (≠ `model_id`) / 反: 换个只回固定串的 Router ⇒ 断言跟着变 |
| G2 | `model_used` **不是** `model_id` 的回显 | 变异 `"model_used": body.model` ⇒ G1 两条都红 |
| G3 | chunk 无 `.model` ⇒ 发 `null` | 正: 断 `is None` / 反: 变异回 `or "default"` ⇒ 红 |
| G3b | **累积端保值** (Task 1 复审 I-1): 首 chunk 报 model、次 chunk 带 choices 但不报 ⇒ 保住先前值 | 变异删 ` or model_used` ⇒ 红 (且**不**打红 G3c) |
| G3c | **累积端位置** (Task 1 复审 M-1): 只有 `choices=[]` 的 usage chunk 带 model ⇒ 仍收得到 | 变异把累积行挪回 `if choices:` 内 ⇒ 红 (且**不**打红 G3b) |
| G4 | 每个 selectable 组都有 `→ ["default-fallback"]` 的 fallback 条目 (带尺寸下限 `>= 5`) | 正 |
| G5 | `hard` / `light` / `default-fallback` **没有** fallback 条目; `default` 仍有 | 反 (防"一律加"的偷懒实现 ⇒ 打破 C1) |
| G6 | **真 `Router` 端到端**: 主模型开流抛错 ⇒ 流仍成功, `done.model_used` / `models_used` 来自 fallback, `fell_back` 为 `true` | 反: 抽掉该组的 fallback 条目 ⇒ 变成 `event: error` |
| G7 | `fell_back` 三态: 全部是配置串 ⇒ `False`; 有别的串 ⇒ `True`; 内部组 / 列表为空 ⇒ `None` (⛔ 不是 `False`) | 三向各一条 |
| **G7b** | **R6 核心**: 列表 `["配置串", "别的串"]` ⇒ `True` (**任一**不符即回退) | 反: `["配置串"]` ⇒ `False`。变异成"只看最后一个" ⇒ 正向红 —— 这条正是 I-2 那个静默谎言 |
| **G7c** | `models_used` 是**有序去重**: 同一模型连报 N 个 chunk ⇒ 列表长度 1; 两个模型交替 ⇒ 按首次出现顺序各一次 | 两个方向 (去重坏掉→长度爆炸; 顺序坏掉→顺序断言红) |
| G8 | 匹配必须带 `/` 边界 | `reported="claude-opus-5"` (真子串但非完整尾段) ⇒ `True`; 变异成裸 `in` ⇒ 红 |
| G9 | 徽章: `fellBack=true` ⇒ 文案含 `→ 实际 {modelsUsed 顿号连接}`+`已回退`+`验证状态未知` 且带 `.unverified` | 反: `fellBack=false` ⇒ 与今天**逐字相同** |
| **G9b** | 多模型 (`modelsUsed` 两项) ⇒ 两个名字**都**出现在徽章上 | 反: 单项时文案与 R4 原样一字不差 (不许出现悬空的顿号) |
| G10 | 兼容 B1/B2: `fell_back`/`models_used` 缺失 ⇒ 徽章与今天**逐字相同** | 正 |
| G11 | 存档诚实: 走完整流 (`onDone`→`persist`) 后 localStorage 里有 `modelsUsed`/`fellBack`, 重建 DOM 后徽章仍显示回退 | 反: 不回退的流存档里 `fellBack` 为 `false` |
| G12 | ⚑ 归因: 回退时 `/api/flag` 的 `model` = 实际模型 (**诱饵**: `msgObj.modelId` 是 `gpt-sol`, 读它就红) | 反: 既有两条 (`withModelId` / `legacyNoModelId`) 必须仍绿 |
| G13 | 静态形状闸 (node 缺席时仍在): `.fellBack` / `.modelsUsed` 属性读取存在 | 照 `test_flag_payload_reads_the_message_model_id` 双闸写法 |

## 7. 已知限制

| # | 限制 |
|---|---|
| **L1** | §3 P3 的实测用的是我们自己的 fake provider ⇒ 证的是「我们的接线 + litellm 机制」。**真实回退时 chunk 里到底写什么串**没有本轮实测 (唯一证据是 `DEPLOY_PLAN.md` 里 `/api/ask` 非流式那次)。若真串与配置串对不上, 表现是**每条答案都误报"已回退"** —— 是**响的**失败不是静默的, 但会立刻吵到用户。⇒ 上线后第一条真实回答就能证伪, 见 §9 冒烟步骤 |
| **L2** | (⚠ **本文初稿在这条上写错过, 见 §3 P6**) 准确说法: **开流阶段**失败 ⇒ 换 deployment, **已实测**; **流中途**抛 `MidStreamFallbackError` ⇒ 也走 fallback 链, **源码级确认、未实测**; 其余中途失败 (普通网络断) ⇒ 仍走 `event: error`。中途回退会让一次回答里出现两个模型的文字 —— 由 R6 的 `models_used` 列表如实呈现 |
| **L3** | 内部组 (`default`/`hard`/`light`) 的 `fell_back` 一律 `null`。技术上 `default` 组是**可判**的 (配置串在 `s.default_model`), 本轮按 R3 裁定不做 —— UI 永远发显式 id, 够不到这条路径; 若将来 `/api/ask_stream` 被脚本用 `model=default` 大量调用, 这条要补 |
| **L4** | 回退目标是 `default-fallback` = **DeepSeek 个人流量** (C3/D4)。这是 R2 的既定代价, 由 R4/R5 的标注承担 |

## 8. 收尾要动的文档

- 前一轮 spec `2026-09-01-model-switching-design.md` §9: **D5 / D6 标记为已还** + 指向本文
- `.work/meta/worklog/phase_07_rag_kg.md` / `docs/PROGRESS.md` / `CLAUDE.md` Key Paths
- 本轮 `RETROSPECTIVE.md` (规则 C)

## 9. 可复跑命令

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag

# 基线
.venv/bin/python -m pytest scripts/tests/ -p no:warnings          # 1956 passed, 1 skipped @2bcd840

# P1: Router.fallbacks 形状
.venv/bin/python -c "
import sys; sys.path.insert(0,'.')
from server.config import Settings
from server.llm_config import create_router
r = create_router(Settings()); print(r.fallbacks)"

# P3: 真 Router + stream=True 的 fallback 生效 (零外部调用)
.venv/bin/python - <<'PY'
import sys, asyncio; sys.path.insert(0,'.')
import litellm
from types import SimpleNamespace
from server.config import Settings
from server.llm_config import create_router
r = create_router(Settings())
r.fallbacks = [{"default": ["default-fallback"]}, {"opus-5": ["default-fallback"]}]
async def fake(**kw):
    if "anthropic" in str(kw.get("model")): raise Exception("primary boom")
    async def agen():
        yield SimpleNamespace(model="deepseek-v4-pro", usage=None,
                              choices=[SimpleNamespace(delta=SimpleNamespace(content="ok"))])
    return agen()
litellm.acompletion = fake
async def main():
    resp = await r.acompletion(model="opus-5", messages=[{"role":"user","content":"hi"}], stream=True)
    async for ch in resp: print("chunk model =", getattr(ch, "model", None))
asyncio.run(main())
PY
# 期望: chunk model = deepseek-v4-pro
```

**上线后冒烟 (验 L1, 需重启服务; 用户点头后再做)**: 正常问一句 → 徽章**不该**出现「已回退」。
若出现, 说明真实 `chunk.model` 与配置串对不上, §4.3 的匹配规则要按实测串修。
