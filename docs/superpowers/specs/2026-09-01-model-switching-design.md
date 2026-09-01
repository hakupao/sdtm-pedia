# 多模型切换 (U1: 单模型按题选) — 设计

> 日期: 2026-09-01 · 分支 `feat/model-switching` · 基线 main `67d53d3` (1899 passed)
> 前置调查: `.superpowers/sdd/2026-09-01-multi-model-switch/bedrock-probe.md` (Bedrock 实测)

## 1. 目标与非目标

**目标**: 用户在 Chat UI 每次提问时自选答题模型, 四选一, 全部走公司 Bedrock。

**非目标 (本轮明确不做)**:
- **U2 容灾/限流备胎** —— Router 已有 `fallbacks=[{"default": ["default-fallback"]}]` 骨架, U1 落地后扩表即可, 另开。
- **U3 并排对比** —— ⚠ **后端已存在**: `POST /api/ask_compare` + `server/compare.py` (N 模型在**同一份检索上下文**上并发 fan-out + 第 4 个模型做 A/B/C 匿名评判)。缺的是 `settings.compare_models` 未配 + **前端无界面**。本轮不动。
- **eval 多模型** —— `run_eval.py` 已有 `--model`, 但配对 eval 撞 `--temperature`(见 §4.1), 另议。
- **换 embedding provider** —— 用户 2026-09-01 明确裁定: embedding 走个人 OpenAI key **可以接受**, 不改。(换 Bedrock embedding 需重灌整个向量库 + 全部检索基线作废重测。)
- **DeepSeek 三处** (`fallback` / `expansion` / `judge`) —— 用户裁定走自己流量**可以接受**, 保持原样。

## 2. 关键约束 (用户裁定)

| # | 裁定 | 日期 |
|---|---|---|
| C1 | 只换**答题**环节。判库(`light`)、检索改写等辅助环节继续用固定模型 —— 否则检索结果跟着变, 对比时分不清是模型差异还是检索差异 | 2026-09-01 |
| C2 | 非 Claude 模型的反捏造红线: **放开 + UI 明确标注**, 不做前置验证、不限制联网 | 2026-09-01 |
| C3 | **GPT 与 Claude 不得走用户个人 API** —— 必须走公司 Bedrock。embedding/DeepSeek 不在此约束内 | 2026-09-01 |

## 3. 架构: 配置驱动的单一事实源

### 3.1 为什么不是「Router 里手写四个组」

候选方案 A (手写命名组) 会造出**两份真相**: Router 一份模型清单、UI 下拉另一份。
本仓库刚在同型缺陷上花了两轮 —— retrospective 规则 6 成因 **B2**「断了相对关系, 没断绝对值与方向」
说的正是这种两边各自漂移而断言照绿的形状。

⇒ 采用 **C**: `settings.selectable_models` 是**唯一**事实源, Router 与 `/api/info` **都从它派生**。
「UI 提供了 Router 没有的模型」在结构上不可能发生, 而不是靠加闸去追。

### 3.2 配置形状

```python
selectable_models: list[SelectableModel]   # server/config.py
# SelectableModel: {id, label, model, verified}
```

| id | label | model | verified |
|---|---|---|---|
| `opus-5` | Claude Opus 5 | `bedrock/converse/global.anthropic.claude-opus-5` | **true** |
| `sonnet-5` | Claude Sonnet 5 | `bedrock/converse/global.anthropic.claude-sonnet-5` | false |
| `gpt-terra` | GPT-5.6 Terra | `bedrock/converse/global.openai.gpt-5.6-terra` | false |
| `gpt-sol` | GPT-5.6 Sol | `bedrock/converse/global.openai.gpt-5.6-sol` | false |

⛔ **`verified` 的语义必须写死, 否则它会退化成一个没人知道含义的布尔**:

> **`verified: true` ⟺ 该模型上跑过反捏造抽检 (Rule 9 + 答题侧 guardrail) 并通过。**

目前**只有 `opus-5` 为 true** —— 联网通道那轮抽检就在它上面做的。
⚠ **`sonnet-5` 同样是 false**: 它是 Claude 不代表验过, 没测就是没测。

### 3.3 Router 派生

`create_router()` 遍历 `selectable_models` 生成同名模型组, 与现有 `default` / `hard` / `light` /
`default-fallback` **并存**。后三者是内部用途 (C1: 不受用户选择影响)。

## 4. 能力协商

### 4.1 temperature —— 本轮无需处理 (记录以免将来误判)

`/api/ask_stream` 的答题调用**根本不传 temperature** (`kw = {"model", "messages", "stream"}`)。
仓库内仍传的两处是检索改写 (不受用户选择影响) 与 judge (范围外)。

⚠ 且**拒收 temperature 不是 GPT 独有**: `server/federation.py` 模块 docstring 明写
「temperature 已移除 —— light 档走 Claude Opus 5, 该模型族拒收采样参数 (400)」。
⇒ 这个坑仓库**早已踩过并处理**。它只在将来 eval 支持多模型时 (`--temperature` 配对口径) 才回来咬。

### 4.2 工具能力注册 —— 必须做

LiteLLM 1.88.1 的 bedrock provider allowlist 只认 `anthropic|mistral|cohere|meta.llama3-*|amazon.nova`,
其余走 `supports_function_calling()` 兜底, 而 registry 无这两个 GPT ⇒ **拒收 `tools`**
(`UnsupportedParamsError`), 联网通道对 GPT 直接不可用。

**裸 boto3 Converse 已实测工具调用本身通** ⇒ 这是**客户端元数据缺口, 不是服务端限制**。

做法: 启动时对白名单模型 `litellm.register_model()`。
⚠ **key 必须去掉 `bedrock/` 前缀** (`converse/global.openai.gpt-5.6-terra`) ——
控制器实测时用带前缀的 key **注册静默无效**, 这是个不报错的失败。

⇒ 配**启动期自检**而非等运行时报错: 注册未生效要在 ready 日志显式说明。
理由: 注册失败的表现是「一切正常, 直到有人开联网」。

### 4.3 `reasoningContent` —— 显式决定丢弃

流式循环只读 `getattr(delta, "content")` 与 `getattr(delta, "tool_calls")`, 其余字段一律忽略
⇒ Sol 的推理块今天就是被丢的。功能上正确 (模型内部思考不该进知识库答案), 但目前是
**构造上的偶然而非决定**, 补一行注释使其成为决定。

⚠ 准确边界: 控制器**流式**实测中两个模型均**未**发 `reasoning_content` 增量; 只有**非流式** boto3
调用时 Sol 发了 `reasoningContent` 块。⇒ 这条是预防, 不是现实问题。

## 5. 请求契约

`AskStreamRequest` 加 `model: str = "default"` —— 与 `AskRequest` **现有**同名字段同默认值, 两端点口径一致。

- 校验: 必须在 Router 已知组名集合内, 否则 **422**。
  ⛔ **不得静默退回 default** —— 静默退回正是本仓库反复栽的形状 (参见 `AskRequest` 的
  `extra="forbid"` 注释所记的抽检事故)。
- **不传 `model` 时请求体与今日逐位相同** (零影响硬要求, 配闸)。

⚠ **`default` 与 `opus-5` 的关系必须写明, 否则是个静默歧义**: 两者今天都解析到 Opus 5
(`default` 组读 `s.default_model`), 但它们是**两个独立的组**, 改 `.env` 的 `default_model`
会让二者**静默分叉**。裁定:

- `default` 组**保留**, 仅供既有调用方 (`/api/ask`、脚本) 向后兼容;
- **UI 下拉永远发显式 id**, 绝不依赖默认值落到 `default`;
- 因此「用户看到的 Opus 5」= `opus-5` 组, 与 `default` 组各自独立可配。

`/api/info` 的 `InfoResponse` 加字段吐出模型表 (含 `verified`), 前端下拉直接渲染。

## 6. 产物自证 (记事实不记意图)

SSE `done` 事件带**实际答题的模型 id 与其 `verified` 值**, 前端存历史时一并存。

⚠ **`default` 组没有 `verified` 值** (它不在 `selectable_models` 里)。裁定: 此时
`verified` 发 **`null`**, 语义是「**未知**」—— 不得发 `false` (会把"没这个概念"误报成"验过且不通过"),
更不得发 `true`。前端对 `null` 的显示与 `false` 区分开。

**理由**: 只做 UI 标注的话, 对话存下来之后这条信息就没了 —— 读的人得靠记得自己当时选了什么。
这与本仓库 2026-09-01 刚清掉的 **B6** 同形: **产物必须能自证**。

## 7. UI

`#scope` fieldset 旁加 `<select>`, 选项由 `/api/info` 模型表渲染 (`label` 显示, `id` 提交)。

- 未验证模型的选项文字带标记 (如 `Claude Sonnet 5 ⚠未验证`);
- 选中未验证模型时, composer 上方显示一行常驻提示: 反捏造边界未在该模型上验证;
- 选择存 `localStorage`, **刷新保留** —— 这是终审 I-E (联网状态过不了刷新) 的同款, 不重犯。

## 8. 测试闸 (每条都要能被变异打红)

| # | 闸 |
|---|---|
| 1 | 白名单外的 `model` → **422**, 不是静默退回 default |
| 2 | 不传 `model` → 请求体与今日**逐位相同** (零影响) |
| 3 | `/api/info` 吐的模型表 **⊆ Router 已知组名** (结构上杜绝 UI 提供 Router 没有的模型) |
| 4 | 每个白名单模型都**已注册工具能力** (否则联网对它不可用) |
| 5 | SSE `done` 带**实际**答题模型 id + `verified`, **两个方向都钉** |
| 6 | 答题侧模型不以 `bedrock/` 开头 → ready 日志**显著告警** (C3; 告警不阻止启动) |

⚠ 闸 6 的背景: `server/config.py` 里三个 Claude 模型的**硬编码默认值是 `anthropic/` 直连**,
只有 `.env` 把它们改写成 Bedrock, 且**无任何启动期校验**。⇒ `.env` 缺失/被覆盖时服务会
**静默**改用 Anthropic 直连 —— 正是 C3 要防的事, 且不报错不记日志。
又一个「只靠配置文件维系、无人守护的不变量」。

## 9. 已知欠账 (本轮不做)

| # | 欠账 | 用户裁定 |
|---|---|---|
| D1 | `/api/ask_compare` + `compare.py` 已建但 `compare_models` 未配、前端无界面 | 另开 (U3) |
| D2 | `run_eval.py` 多模型 + `--temperature` 配对口径冲突 | 另议 |
| D3 | embedding 走个人 OpenAI key (每次提问必走) | **接受, 不改** |
| D4 | fallback / expansion / judge 走 DeepSeek 个人流量 | **接受, 不改** |
| **D5** ⚠ | **Chat UI 主路径失去 fallback (本分支引入的回归)** —— 分支前 UI 永发 `default` 组, 该组有 `fallbacks=[{"default": ["default-fallback"]}]` 兜底; 分支后 UI **永发显式 id** (§5 裁定) 落 `opus-5`, 而四个新派生组**无 fallback 条目** ⇒ 主模型没变, **容灾网没了**。非理论风险: `sdtm-rag/DEPLOY_PLAN.md` 记着实测「Anthropic credits 耗尽 → DeepSeek 自动回退」**真的生效过** | **本轮只记录不修**。理由: (a) 扩 fallback 表属 §1 明确划为非目标的 **U2**; (b) 更要紧 —— 加了会**激活 `model_id` 与 `model_used` 的分叉** (用户选 `gpt-sol` 却拿到 DeepSeek 的答案), 而 `model_used` **目前无任何取值断言** (见 D6), 等于在没有闸的地方引入新行为。<br>⛔ **在 U2 落地前, `opus-5` 失败时前端直接收到 `event: error`, 不再自动回退。** |
| **D6** | `model_used` 字段的**取值**在整个测试套件里无任何断言 (既有欠账, 非本分支引入) | 与 D5 同轮处理 —— U2 引入 fallback 时**必须**先补上, 否则分叉发生时无人可证 |
| **D7** | `/api/info` 直接读 `s.selectable_models`, **未经** `_validated_selectable_models` 的撞名 fail-loud 闸 —— 五条读路径里四条过闸, 它是唯一例外 | 当前生产够不到 (`create_router` 在 lifespan 启动期就会因撞名让应用起不来)。⚠ 若将来把 `create_router` 改成懒加载、或把撞名异常改成 catch-and-log, `/api/info` 会在无人守护下把撞名 id 吐给前端, 而子集闸测的是默认配置、测不出该漂移 |
| **D8** | `/api/ask_stream` 接受 `hard` / `light` / `default-fallback` 作答题模型 | 终审判定按 §5 字面**合规** (「必须在 Router 已知组名集合内」), UI 也够不到 (`/api/info` 不吐它们), `done` 事件对它们发 `verified: null` 语义正确。**不改** —— 改了会与 §5 字面定义冲突 |
| **D9** | streamlit 端另有一份模型清单 (第四份真相); 两处失效文档指针 (指向已删的 `VALID_MODELS`、引用旧事件名 `selectable_models_not_on_bedrock`) | 终审修复轮按指示未动, 清单见 `.superpowers/sdd/2026-09-01-model-switching/fix-final-report.md` §4 |
| **D10** | `webchat/app.js` 顶部注释与最终实现**相反**, 且过时那条正好描述的是被 C-1 修掉的 bug 行为 (「从 topbar 切模型名」) | 终审 M-1, 未修。⚠ 本仓库既有判例: **假约束注释比过期注释更害人** —— 它会让后来人以为当前实现就是那样。1 行改动, 建议下轮清掉 |
| **D11** | `/api/ask` 现在能用未验证模型答题 (I-3 修法把接受值 3→8 的必然结果), 但 `AskResponse` 没有 `model_id` / `verified` ⇒ **自证面缺一块** | 终审 M-7。今天无调用方这么用, 不阻塞; 若将来 `/api/ask` 真被用来跑非 Claude 模型, 这条要补 |
