# 联网参考通道 (web search channel) — 设计 (spec)

> 建立: 2026-08-31 · 轨: doc/答题侧 · 性质: **agentic 工具循环, 非确定性, 不进 gold set**
> 上游前提: 同日三档模型切 `bedrock/converse/global.anthropic.claude-opus-5`
> 用户裁定 2026-08-31: 源范围 = **全网开放**; 实现 = **A1 外部搜索 API (Tavily 类)**;
> 循环尺度 = **最多 5 轮 / 15 次搜索**
> 红线: **网页内容永远不得产出 CT 码 (Cxxxxx) 与 SDTM class/category 归属**;
> `check_code_grounding.py` 一行不改

## 1. 背景 (用户的真实诉求)

不是"查更新的事实"。用户原话拆解为三条:

1. KB 未覆盖的领域问题 (FDA/PMDA 指南、ADaM/CDASH、公司 SOP)
2. 减少"上下文不足"拒答
3. **"知识库的一些 example 不能完全覆盖我的场景, 需要借鉴别的成熟项目的做法,
   而且联网的话可以有一定的推理和借鉴"**

第 3 条是重心, 也是设计的分水岭: 要的是**实践参考 + 类比推理**, 不是权威事实查询。
因此联网内容与 KB 内容**可信度等级不同**, 绝不能在答案里用同一种 `[Source:]` 呈现 ——
否则三个月后回看分不清哪句是标准、哪句是某人博客。

体验目标经用户澄清为: **"类似 ChatGPT / Claude 网页版聊天的那种感觉"**。该感觉的来源
不是"谁托管搜索", 而是**模型自己决定要不要搜、搜什么、搜几轮**, 以及**过程可见**。

## 2. 技术判决 (实测, 非查表)

### 2.1 Bedrock 拿不到 Anthropic 托管的 web 工具

`shared/platform-availability.md` 记 Web search / Web fetch 在 Bedrock 列 `No`。实测坐实:

```bash
curl -X POST ".../model/global.anthropic.claude-opus-5/converse" \
  -d '{..., "additionalModelRequestFields":{"tools":[{"type":"web_search_20260209","name":"web_search"}]}}'
# → HTTP 400  {"message":"...tool type 'web_search_20260209' is not supported for this model"}
```

### 2.2 但 Converse 的自定义工具循环可用 —— 网页版体验能做到

同端点传 `toolConfig` 定义一个 `web_search` 自定义工具, opus-5 自主发起并发查询:

```
stopReason: tool_use
TEXT      -> I'll search for recent CDISC publications and announcements.
TOOL CALL -> {"query": "CDISC news announcements this week"}
TOOL CALL -> {"query": "CDISC.org latest publications standards released"}
```

⚠ 结论要精确: **Anthropic 托管的那套拿不到; 用户想要的体验拿得到**, 代价是搜索循环
跑在自己的服务端 (搜索引擎换成 Tavily 类 API)。

## 3. 目标与范围

### In scope

1. `web` 作为**第四个正交维度**: 与 `corpus` 判库完全独立, 不参与路由、不占 `top_k` 席位
2. `web_search` 以**自定义工具**形式暴露给答题模型, 模型自主决定调用时机与查询词
3. 独立的来源标注体系 `[Web: url (retrieved YYYY-MM-DD)]`, 与 `[Source: path]` 严格区分
4. Rule 9 三条 (§5), 常驻 system prompt 但条件生效
5. SSE 事件扩展: 搜索过程对前端可见
6. 前端第三个 checkbox + 橙色 `web` 徽章

### Out of scope (明确不做)

- **KB 检索不改为工具**。更 agentic, 但会推翻整条 RAG 管线 + grounding 闸 + 码闸 +
  两套 gold set。收益不值该代价。**KB 前置注入, 只有 web 是工具**。
- **不给网络来源开码闸白名单**。见 §5 红线。
- **不进 gold set**。见 §8。
- 多研究 (st01 之外) 支持 — 与本 spec 无关, `config.py:41` 仍硬编码 `study_st01`。

## 4. 架构与数据流

```
question, web=true
   │
   ├─ KB retrieve (corpus 路由: auto|cdisc|study|both) ──→ ## Retrieved Context
   │                                                        ↑ 现有管线一字不改
   └─→ LLM ⟳ 工具循环 (上限 5 轮 / 15 次搜索)
         │   stopReason=tool_use → 执行 Tavily → toolResult 回灌 → 继续
         └─  stopReason=end_turn → 收尾
                    ↓
        answer + sources[kb…] + sources[web…] + web_status
```

**checkbox 语义** (三个并列, 可任意组合):

| cdisc | study | web | corpus 值 | 说明 |
|---|---|---|---|---|
| ✗ | ✗ | ✗ | `auto` | 现状, LLM 判库 |
| ✓ | ✗ | ✗ | `cdisc` | |
| ✗ | ✓ | ✗ | `study` | |
| ✓ | ✓ | ✗ | `both` | |
| ✗ | ✗ | ✓ | `auto` + web | KB 仍查 (判库), 附加联网工具 |
| ✓ | ✗ | ✓ | `cdisc` + web | 标准权威 + 业界参考 = 核心借鉴场景 |

⚠ `web` **不会**关掉 KB 检索。KB 是本产品的地基, 不提供"纯联网"模式。

## 5. 反捏造边界 (核心红线)

### Rule 9 — 常驻 system prompt, 条件生效

措辞写成 *"当 `## Web References` / web 工具结果存在时…; 不存在时本条无效"*。

**为什么常驻而不是按需追加**: 按开关拼装会造出两套 system prompt, 行为漂移无法归因,
且毁掉将来做 prompt cache 的可能。同时规则必须待在 system 层才有权威 —— 不能塞进
user content 里跟不可信的网页数据同框。

三条:

1. Web 结果是**未经验证的业界参考, 不是标准依据**。引用格式
   `[Web: url (retrieved YYYY-MM-DD)]`, 与 `[Source: path]` 严格区分。
2. **禁止**从 Web 结果产出: CT 码 (`Cxxxxx`)、SDTM class/category 归属、
   变量的 Core/Role/Type 断言。这些只能来自 KB。
3. 基于 Web 的做法建议必须标为推测/借鉴 (沿用 `federation.py::_ROUTER_SYSTEM` 已有的
   EDC↔SDTM inference 标注先例)。

### 为什么不给网络来源开码闸白名单

`eval/prod_wirein/check_code_grounding.py` 把不在 `knowledge_base/` 的 `Cxxxxx` 判为
`NONEXISTENT` (纯捏造)。若为网页内容开豁免, 等于教会模型用"网上看到的"绕过 Rule 7,
闸即废。

**代价已知并接受**: 即使网页上是个真实的新 C 码, 助手也只会给名称, 并叫用户去终端
文件确认。对临床数据这个取舍是对的 —— 漏一个码永远安全, 错一个码是严重缺陷
(Rule 7 原话: "A wrong clinical code is a serious defect; omitting a code is always safe")。

**因此 `check_code_grounding.py` 与 `apply_counting_gate` 均不改动。**

### 全网开放的风险如何兜

用户裁定源范围 = 全网开放 (风险: 过时博客 / AI 生成内容 / 无法归因 — 已在决策时告知)。
不用白名单兜, 改用**标注 + 权限限制**兜:

- 每条网络来源强制带 URL + 抓取时间 → 可追溯、可自行判断新旧
- Rule 9.2 的硬断言禁令 → 风险被限制在"参考质量"层, 不渗进权威层

## 6. 组件

| 组件 | 变更 | 说明 |
|---|---|---|
| `server/web_search.py` | **新增** | Tavily 调用; 超时/失败/空结果降级; 返回 `WebRef(url, title, content, published_date?, retrieved_at)` |
| `server/rag.py::_build_system_prompt` | 改 | 追加 Rule 9 (常驻) |
| `server/router.py` | 改 | `AskRequest.web: bool = False`; 工具循环; 响应加 `web_status`; `sources` 加 web 条目 |
| `server/config.py` | 改 | `web_search_enabled` / `web_max_rounds=5` / `web_max_searches=15` / 日配额 |
| `webchat/index.html,app.js,style.css` | 改 | 第三个 checkbox; `tool_call`/`tool_result` 事件渲染; 橙色 web 徽章 |

## 7. 错误处理与可见性

### 过程可见 (网页版感觉的一半)

单轮 SSE 扩为多轮事件流, 新增 `tool_call` / `tool_result` 事件类型 (复用现有 `sse()`)。
前端按时间顺序渲染, 搜索过程可折叠:

```
🔍 搜索 "CDISC SDTM custom domain mapping practice"
🔍 搜索 "PHUSE paper non-standard EDC field SDTM"
   └─ 找到 6 个来源 ▾
💭 (思考)
📝 正文流式输出…
```

⚠ 没有这层, 勾了联网只会看到卡住 40 秒后蹦出一段话 —— 那是超时的感觉, 不是网页版的感觉。

### 失败必须可见

搜索失败 / 超时 / 无 key / 超配额 → 答案照常出 (降级为未联网), 但:

- 响应带 `web_status: ok | failed | quota_exceeded | disabled`
- 前端**显式提示"本次未联网"**

⚠ 勾了联网却静默降级成没联网, 是这类功能最容易骗人的地方。

### 5 轮 / 15 次的后果 (用户已裁定接受)

- **延迟**: 每轮 = opus-5 思考 (adaptive thinking 默认开) + 搜索往返, 跑满可能 **1-2 分钟**。
  `llm_config.py` Router `timeout=120` 是**单次调用**上限, 不管循环总时长;
  **前端与反代的总超时须一并调**, 否则跑满时断在半路。
- **费用**: Tavily 按次计费, 15 次/题消耗很快。**须加日配额兜底**, 防止忘关跑飞。

## 8. eval 与可复算性

**联网路径不进 gold set。** 联网默认 off, 140q 与 study golden v2 48q 跑法一字不改,
配对 A/B 可复算性完整保住。

联网答案本质不可复算 (同一题两次搜到的页面不同), 故改用**规则 A 的语义抽检**:
N 样本人工核验 —— `[Web:]` 标注是否规矩、有无从网页搬 CT 码 —— 结果留 `evidence/`。

⚠ 直接后果: **联网通道的质量不会有 eval 数字背书**, 只有抽检。用户已知悉并接受。

## 9. 测试策略

1. `web_search.py` 解析与降级: mock Tavily 响应, 覆盖超时 / 空结果 / 畸形 JSON / 无 key
2. 循环上限: 第 6 轮必须停, 且拿现有结果作答 (不得无限循环)
3. **回归闸**: `web=false` 时 system prompt 与当前版本**逐字节相同** ——
   证明本功能对现有路径零污染 (同 `prompt_guardrail_enabled` 当初的 A/B 回滚闸套路)
4. 集成: 勾联网跑一题, 验证 sources 含 web 条目、答案带 `[Web:]`、
   且答案内**无**任何非 KB-grounded 的 `Cxxxxx`

## 10. 前置条件与未决项

- **阻塞前置**: Tavily API key (用户 2026-08-31 已去申请)。无 key 时可先用 mock 跑通
  全部单测, 但"能否真跑通"会一直悬着。
- ⚠ **未验证的技术风险 (实现第一步必须先验)**: §2.2 的工具循环实测走的是**裸 curl 到
  Bedrock Converse**, 尚未验证 **LiteLLM Router 这一层**的
  `completion(tools=..., stream=True)` + `bedrock/converse/` 组合能否正常透传
  `toolUse` / 回灌 `toolResult`。生产调用走的是 Router (`llm_config.py`), 不是裸 curl。
  若 Router 层不支持, 备选是该路径绕开 Router 直接用 `litellm.completion` (需自行处理
  fallback), 或裸 boto3/HTTP。**此项未验证前不要开工写业务逻辑。**
- 未决: Tavily 具体额度与单价 (申请时确认, 本 spec 不编数字); 日配额取值待定。
- 未决: 反代/前端总超时的具体调整值, 实现时按跑满 5 轮的实测时长定。
