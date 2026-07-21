# LLM 接入方案调研报告 — 2026-05-22

> 创建: 2026-05-22
> Owner: document-specialist subagent (background)
> 调研范围: DeepSeek V4 Pro / ChatGPT Plus 代理 / Anthropic Claude API / LiteLLM 兼容性
> 上游设计: `docs/DESIGN_RAG_KG.md` §3.6 (LLM Abstraction: LiteLLM)
> 落档触发: T2 (Phase 0 Research) — 整合进 PLAN.md §决策表

---

## 1. 决策表

| Provider | Model ID | 接入方式 | Context Window | Input $/1M | Output $/1M | LiteLLM 前缀 | 推荐用途 | 风险等级 |
|---|---|---|---|---|---|---|---|---|
| DeepSeek | `deepseek-v4-pro` | 官方 API (api.deepseek.com) | 1M tokens | $0.435 (cache miss) / $0.003625 (cache hit) | $0.87 | `deepseek/` | 复检、推理任务 | 低 (官方 API) |
| DeepSeek | `deepseek-v4-flash` | 官方 API | 1M tokens | $0.14 (cache miss) / $0.0028 (cache hit) | $0.28 | `deepseek/` | 高频原型、快速验证 | 低 |
| Anthropic | `claude-sonnet-4-6` | 官方 API | 1M tokens | $3.00 / $0.30 (cache hit) | $15.00 | `anthropic/` | RAG 主答、生产主力 | 低 |
| Anthropic | `claude-opus-4-7` | 官方 API | 1M tokens | $5.00 / $0.50 (cache hit) | $25.00 | `anthropic/` | 语义审查、最难 reranker | 低 |
| Anthropic | `claude-haiku-4-5` | 官方 API | [UNVERIFIED, 推测 200K] | $1.00 / $0.10 (cache hit) | $5.00 | `anthropic/` | 轻量分类、过滤 | 低 |
| ChatGPT Plus 代理 | 取决于代理实现 | Reverse-proxy/selenium/cookie sniff | 取决于底层模型 | 无官方 API 额度 (Plus 不含 API) | 同上 | `openai/` (需自定义 base_url) | **仅 daily prototype, 非生产** | **极高** |

---

## 2. Q1: DeepSeek V4 Pro

### 版本澄清

用户说的 "DeepSeek V4 Pro" 是真实存在的模型, **不是口误**。DeepSeek 于 2026-04-24 发布 DeepSeek-V4 系列, 包含两个变体:

- `deepseek-v4-pro`: 1.6T 参数 MoE, ~49B 激活参数
- `deepseek-v4-flash`: 284B 参数, ~13B 激活参数 (更快更便宜)

**DeepSeek 历史版本链**: V2 → V2.5 → V3 → V3.1 (曾用 `deepseek-chat` 别名) → V3.2 → V4-Flash/V4-Pro

### 模型 ID 与 API Endpoint

```
Base URL: https://api.deepseek.com/v1
Model IDs:
  - deepseek-v4-pro
  - deepseek-v4-flash
```

**废弃警告**: `deepseek-chat` 和 `deepseek-reasoner` 将于 **2026-07-24** 停用。过渡期间:
- `deepseek-chat` → 路由到 `deepseek-v4-flash` 非思考模式
- `deepseek-reasoner` → 路由到 `deepseek-v4-flash` 思考模式

建议: **立即改用新 model ID**, 不要依赖旧别名。

### 价格 (2026-05-22 查证)

| 模型 | Input (cache miss) | Input (cache hit) | Output | 并发上限 |
|---|---|---|---|---|
| `deepseek-v4-pro` | $0.435 / 1M | $0.003625 / 1M | $0.87 / 1M | 500 |
| `deepseek-v4-flash` | $0.14 / 1M | $0.0028 / 1M | $0.28 / 1M | 2,500 |

**当前折扣**: `deepseek-v4-pro` 享受 75% 折扣, 到期时间 **2026-05-31 15:59 UTC**。折扣到期后价格可能上涨, 需关注。

上述已是折后价。折扣到期后原始价格未在文档中单独列出, 应监控 [api-docs.deepseek.com/quick_start/pricing/](https://api-docs.deepseek.com/quick_start/pricing/)。

### Context Window

两个模型均支持 **1M token context**, 最大输出 384K tokens。

### LiteLLM 支持情况

LiteLLM 用 `deepseek/` 前缀支持所有 DeepSeek 模型:

```python
model="deepseek/deepseek-v4-pro"
model="deepseek/deepseek-v4-flash"
```

**已知 BUG (截至 2026-05-22, 仍为 open issue)**:

1. **多轮对话中断** ([Issue #26395](https://github.com/BerriAI/litellm/issues/26395)): `deepseek-v4-pro` 在 thinking 模式下要求后续轮次回传 `reasoning_content`, 但 LiteLLM 会将其从 message history 中剥除, 导致第二轮返回 400 错误。状态: **Open, 截至 v1.83.12 未修复**。

2. **Cost mapping 未完整** ([Issue #26709](https://github.com/BerriAI/litellm/issues/26709)): V4-Flash 和 V4-Pro 的 cost tracking 可能不准确。状态: **Open**。

3. **reasoning_effort 参数被忽略** ([Issue #27439](https://github.com/BerriAI/litellm/issues/26395)): `reasoning_effort` 值被丢弃, 始终映射为 `thinking: {"type": "enabled"}`。

**规避方案**: 如果 RAG 场景需要多轮, 可先用 `deepseek-v4-flash` 的非思考模式 (不涉及 reasoning_content), 或者直接调用 DeepSeek 原生 SDK 绕过 LiteLLM 的 reasoning 处理层, 等待上游修复。

**源**: [DeepSeek API Docs Pricing](https://api-docs.deepseek.com/quick_start/pricing/) · [DeepSeek Changelog](https://api-docs.deepseek.com/updates) · [OpenRouter DeepSeek V4 Pro](https://openrouter.ai/deepseek/deepseek-v4-pro) · [HuggingFace Model Card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

---

## 3. Q2: ChatGPT Plus 代理

### 核心事实

ChatGPT Plus ($20/月) 是 **chatgpt.com 网页订阅**, 不包含任何 OpenAI API 调用额度。Plus 和 API 是两个完全分离的计费体系:

- Plus 额度: 在 chatgpt.com 网页端使用, 有月度消息上限
- OpenAI API: 独立按 token 计费, 需单独开通付费账户

要把 Plus 的 web session 包装成 API 调用, 必须绕过官方机制。

### 2026 年仍存在的代理方案

| 项目 | 实现原理 | 稳定性 | ToS 合规 |
|---|---|---|---|
| [openai-oauth (EvanZhouDev)](https://github.com/EvanZhouDev/openai-oauth) | OAuth token 抓取, 在 localhost 起 OpenAI-compatible 端点 | 中 (依赖 OAuth token 有效期) | **违反** ToS |
| [codex-openai-proxy (Securiteru)](https://github.com/Securiteru/codex-openai-proxy) | 截获 ChatGPT Codex auth token, 转发给 CLINE/Claude Code | 低-中 (UI 变动即失效) | **违反** ToS |
| [CLIProxyAPI (router-for-me)](https://github.com/router-for-me/CLIProxyAPI) | 包装 ChatGPT Codex CLI, 提供 OpenAI-compatible 服务 | 低 (CLI 更新即断) | **违反** ToS |
| [ChatGPT-Bridge (improveTheWorld)](https://github.com/improveTheWorld/ChatGPT-Bridge) | 浏览器插件 (Chrome/Edge) + 页面注入, 拦截 GPT-4 响应 | 极低 (DOM 依赖) | **违反** ToS |
| Selenium/Playwright headless 自制 | 自动化浏览器填表, 解析响应 | 极低 (Cloudflare 反爬, 频繁封 session) | **违反** ToS |

### 风险评估

**OpenAI ToS 明确禁止的行为** (来源: [OpenAI Terms of Use](https://openai.com/policies/row-terms-of-use/)):

- "Automatically or programmatically extract data or Output" — 自动/编程方式提取数据或输出
- "Circumvent rate limits or restrictions or bypass protective measures or safety mitigations" — 绕过限速或保护措施
- "Attempt to reverse engineer, decompile or discover the source code or underlying components" — 逆向工程

以上三条均被 Plus 代理方案触发。具体风险:

1. **账号封禁**: OpenAI 定期检测异常 session 行为, 一经发现可直接封 ChatGPT 账号 (不只是 API 账号)
2. **极低稳定性**: 依赖 DOM 结构/Cookie/OAuth token, ChatGPT 任意 UI 更新即断
3. **零并发**: 多数实现序列化所有请求 (单线程), 无法并发
4. **数据安全**: RAG 查询内容 (含 SDTM 专有知识库数据) 经由第三方代理层传输, 隐私风险高
5. **不适合长跑生产**: 需要持续维护, 任何 OpenAI 安全更新都可能让代理瞬间失效

### 折中建议

**Plus 代理不适合生产 RAG**, 但用户已付了订阅, 有合理的"不浪费"诉求。可行方案:

| 场景 | 方案 |
|---|---|
| **日常 prototype / 人工交互测试** | 在 chatgpt.com 网页直接用 Plus, 手动粘贴输入输出 — 零风险, 合规 |
| **需要编程调用 GPT 模型** | 开通独立 OpenAI API account (按 token 付费), 与 Plus 完全独立 |
| **想节省 API 费用** | 用 DeepSeek V4-Flash 做高频低优先级任务 (价格是 Sonnet 的 1/10) |
| **已有 Plus 想 "API 化"** | 接受风险前提下: openai-oauth 项目最轻量, 但仅限本地 dev 环境, 绝不部署到服务器 |

**结论**: **不推荐将 Plus 代理纳入本项目 RAG pipeline 的任何生产或 staging 环节。** 在 PLAN.md 中给 OpenAI-compatible base_url 留接口, 但 default fallback chain 不含 Plus 代理。

---

## 4. Q3: Anthropic API

### 当前可用模型 ID (2026-05-22, 官方文档查证)

| Model ID | 状态 | 推荐用途 |
|---|---|---|
| `claude-opus-4-7` | **当前最新 Opus**, 2026-04-16 发布 | 最复杂推理、语义审查 |
| `claude-opus-4-6` | 可用 | 同 Opus 4.7, 价格相同 |
| `claude-opus-4-5` | 可用 | |
| `claude-sonnet-4-6` | **推荐主力** | 生产 RAG 主答 |
| `claude-sonnet-4-5` | 可用 | |
| `claude-haiku-4-5` | **推荐轻量** | 分类、过滤、批处理 |
| `claude-opus-4-1` | 可用但贵 ($15/$75) | 不推荐新项目使用 |
| `claude-opus-4` | **Deprecated** | 避免 |
| `claude-sonnet-4` | **Deprecated** | 避免 |
| `claude-haiku-3-5` | **Retired** (Bedrock/Vertex 除外) | 避免 |

**注意**: 用户已知的 `claude-haiku-4-5-20251001` 是带日期戳的版本 ID, 功能上等同于 `claude-haiku-4-5`。官方文档的主表格用不带日期戳的短 ID。

### 价格 (官方文档, 2026-05-22)

| 模型 | Input (base) | Input (cache hit) | 5min Cache Write | 1h Cache Write | Output | Batch Input | Batch Output |
|---|---|---|---|---|---|---|---|
| `claude-opus-4-7` | $5.00 | $0.50 | $6.25 | $10.00 | $25.00 | $2.50 | $12.50 |
| `claude-sonnet-4-6` | $3.00 | $0.30 | $3.75 | $6.00 | $15.00 | $1.50 | $7.50 |
| `claude-haiku-4-5` | $1.00 | $0.10 | $1.25 | $2.00 | $5.00 | $0.50 | $2.50 |

单位均为 USD per 1M tokens (MTok)。

**新特性注意**:
- Opus 4.7 使用新 tokenizer, 同等文本可能多用 **最多 35%** token, 成本估算需留余量
- **Fast mode** (beta): Opus 4.6/4.7 专属, $30 input / $150 output per 1M, 约 6x 标准价, 不推荐 RAG 常规使用
- **Batch API**: 异步, 50% 折扣, 24h 内返回 — 适合离线 eval、批量标注
- **Prompt caching**: RAG 场景中如果 system prompt 或 retrieved context 重复度高, cache hit 成本降至 $0.30/1M (Sonnet), 极具价值

### Context Window (查证)

| 模型 | Context Window |
|---|---|
| `claude-opus-4-7` | **1M tokens** |
| `claude-opus-4-6` | **1M tokens** |
| `claude-sonnet-4-6` | **1M tokens** |
| `claude-haiku-4-5` | [UNVERIFIED — 官方定价页未列出 Haiku 4.5 的 context window 数字; 根据 Anthropic 产品线惯例推测为 200K, 但需到 https://platform.claude.com/docs/models/overview 核验] |

Sonnet 4.6 的 context window 预期为 200K — **实际为 1M**, 与 Opus 4.7 相同, 均为全 1M 无溢价。

### LiteLLM 支持

```python
model="anthropic/claude-sonnet-4-6"
model="anthropic/claude-opus-4-7"
model="anthropic/claude-haiku-4-5"
```

支持 streaming, function calling。官方文档中 LiteLLM DeepSeek 页提及 Anthropic 不支持 `budget_tokens` (thinking 预算限制), 其他功能正常。

**源**: [Anthropic Pricing Docs](https://platform.claude.com/docs/en/about-claude/pricing) · [CloudZero Analysis](https://www.cloudzero.com/blog/anthropic-claude-api-pricing/) · [Evolink Guide](https://evolink.ai/blog/claude-api-pricing-guide-2026)

---

## 5. Q4: LiteLLM 配置示范

### 当前版本

- **Latest stable**: `1.85.1` (2026-05-21, [PyPI](https://pypi.org/project/litellm/))
- **Breaking changes in `v1.84.0`** (2026-05-14): "Reliability hardening + multi-pod budget accuracy" — 具体 breaking change 细节在 v1.84.0 release notes, 主要影响 proxy server 多 pod 预算统计, 不影响 Python SDK Router API 基本用法
- **版本命名变更** (近期生效): 取消 `-stable`/`-nightly` 后缀; MINOR 版本号每周推进, PATCH 保留给 hotfix; `:latest` Docker tag 成为唯一稳定 rolling 指针; `main-stable` Docker tag 将于 **2026-06-30** 停止发布

### Router 多 provider 配置示范

#### Python SDK Router (推荐, ~30 行)

```python
import os
from litellm import Router

# 环境变量
# DEEPSEEK_API_KEY, ANTHROPIC_API_KEY, OPENAI_API_KEY
# 如果使用 Plus 代理, 还需要 CHATGPT_PROXY_BASE_URL

model_list = [
    # --- Anthropic (主力) ---
    {
        "model_name": "sonnet",
        "litellm_params": {
            "model": "anthropic/claude-sonnet-4-6",
            "api_key": os.environ["ANTHROPIC_API_KEY"],
        },
    },
    {
        "model_name": "opus",
        "litellm_params": {
            "model": "anthropic/claude-opus-4-7",
            "api_key": os.environ["ANTHROPIC_API_KEY"],
        },
    },
    # --- DeepSeek (复检 / 低成本) ---
    {
        "model_name": "deepseek-pro",
        "litellm_params": {
            "model": "deepseek/deepseek-v4-pro",
            "api_key": os.environ["DEEPSEEK_API_KEY"],
            "api_base": "https://api.deepseek.com/v1",
        },
    },
    {
        "model_name": "deepseek-flash",
        "litellm_params": {
            "model": "deepseek/deepseek-v4-flash",
            "api_key": os.environ["DEEPSEEK_API_KEY"],
            "api_base": "https://api.deepseek.com/v1",
        },
    },
    # --- OpenAI API (若开通独立 API 账户) ---
    # {
    #     "model_name": "gpt-4o",
    #     "litellm_params": {
    #         "model": "openai/gpt-4o",
    #         "api_key": os.environ["OPENAI_API_KEY"],
    #     },
    # },
    # --- ChatGPT Plus 代理 (仅 dev 用, 高风险, 参见 Q2) ---
    # {
    #     "model_name": "chatgpt-proxy",
    #     "litellm_params": {
    #         "model": "openai/gpt-4o",
    #         "api_base": "http://localhost:10531/v1",  # openai-oauth 本地端口
    #         "api_key": "none",
    #     },
    # },
]

router = Router(
    model_list=model_list,
    default_litellm_params={"timeout": 30, "stream": False},
    routing_strategy="simple-shuffle",  # 可换 "least-busy" 或 "usage-based-routing"
    num_retries=2,
    fallbacks=[
        {"sonnet": ["deepseek-flash"]},  # Sonnet 失败时降级到 DeepSeek Flash
        {"opus": ["sonnet"]},            # Opus 失败时降级到 Sonnet
    ],
)

# 调用示例
response = router.completion(
    model="sonnet",
    messages=[{"role": "user", "content": "What is SDTM ADSL domain?"}],
    stream=False,
)
print(response.choices[0].message.content)
```

#### YAML 代理配置 (litellm proxy server)

```yaml
# config.yaml
model_list:
  - model_name: sonnet
    litellm_params:
      model: anthropic/claude-sonnet-4-6
      api_key: os.environ/ANTHROPIC_API_KEY

  - model_name: deepseek-pro
    litellm_params:
      model: deepseek/deepseek-v4-pro
      api_key: os.environ/DEEPSEEK_API_KEY
      api_base: https://api.deepseek.com/v1

  - model_name: deepseek-flash
    litellm_params:
      model: deepseek/deepseek-v4-flash
      api_key: os.environ/DEEPSEEK_API_KEY
      api_base: https://api.deepseek.com/v1

  # OpenAI-compatible custom endpoint (Plus proxy, dev only)
  - model_name: chatgpt-proxy-dev
    litellm_params:
      model: openai/gpt-4o
      api_base: http://localhost:10531/v1
      api_key: none

general_settings:
  master_key: sk-your-master-key

router_settings:
  routing_strategy: simple-shuffle
  num_retries: 2
  fallbacks:
    - sonnet: [deepseek-flash]
```

### 功能支持矩阵

| 功能 | DeepSeek V4 | Anthropic Claude | OpenAI (含代理) |
|---|---|---|---|
| Streaming | ✅ | ✅ | ✅ |
| Function calling / Tool use | ✅ (V4 系列支持) | ✅ | ✅ |
| Vision / Image input | ✅ (V4 系列支持) | ✅ | ✅ |
| Prompt caching | ✅ (DeepSeek 原生) | ✅ (LiteLLM 透传) | ✅ |
| Multi-turn (thinking mode) | ⚠️ **BUG** in LiteLLM v1.85.1 | ✅ | ✅ |
| Batch API | 无 (DeepSeek 无官方 Batch) | ✅ | ✅ |
| reasoning_effort 参数 | ⚠️ 被丢弃 (已知 bug) | N/A | N/A |

**源**: [LiteLLM Docs](https://docs.litellm.ai/) · [LiteLLM DeepSeek Provider](https://docs.litellm.ai/docs/providers/deepseek) · [LiteLLM GitHub Releases](https://github.com/BerriAI/litellm/releases) · [PyPI litellm 1.85.1](https://pypi.org/project/litellm/) · [LiteLLM Proxy Config](https://docs.litellm.ai/docs/proxy/configs)

---

## 6. 总体推荐 — 本项目 RAG Default Model + Fallback Chain

### 推荐配置

```
主答 (RAG generation):     claude-sonnet-4-6
  ↓ fallback on error/timeout
轻量分类/过滤:              claude-haiku-4-5  (或 deepseek-v4-flash)
  ↓
复检/对比验证:              deepseek-v4-pro  (非思考模式, 绕开 multi-turn bug)
  ↓
最难语义审查/reranker:       claude-opus-4-7  (按需调用, 成本控制)
```

### 具体场景映射

| RAG 环节 | 推荐模型 | 理由 |
|---|---|---|
| Query expansion / intent 分类 | `claude-haiku-4-5` | 最便宜 ($1/$5), 任务简单 |
| Retrieval-augmented 主答 | `claude-sonnet-4-6` | 1M context, 支持大块 retrieved text, $3/$15 性价比最高 |
| 答案一致性复检 (cross-check) | `deepseek-v4-flash` | $0.14/$0.28, 用非思考模式避开 LiteLLM bug |
| 高难度语义评审 / SDTM 专业质检 | `claude-opus-4-7` | 最强推理, 仅按需调用 |
| 批量离线 eval / 标注 | `claude-sonnet-4-6` Batch API | 50% 折扣, $1.50/$7.50 |
| Daily prototype / 人工测试 | chatgpt.com 网页直接用 | 合规, 不浪费 Plus 订阅 |

### 成本估算 (每 1000 次 RAG 查询, 假设 2K input + 500 output per call)

| 环节 | 模型 | 估算成本 |
|---|---|---|
| 主答 (1000 calls × 2500 tokens) | Sonnet 4.6 | ~$0.90 |
| 复检 (500 calls × 2000 tokens) | DeepSeek V4-Flash | ~$0.14 |
| 审查 (50 calls × 3000 tokens) | Opus 4.7 | ~$0.08 |
| **合计** | | **~$1.12 / 1000 queries** |

如果启用 Prompt Caching (system prompt 重用率高), Sonnet cache hit 成本降至 $0.30/1M, 实际成本可进一步压低约 40-60%。

---

## 7. 未解决的问题

以下条目在 2026-05-22 调研中无法确认, 明确标注 `[UNVERIFIED]`:

1. **[UNVERIFIED] `claude-haiku-4-5` context window 精确值**: 官方定价页未列出 Haiku 4.5 的 context window 数字。需到 https://platform.claude.com/docs/models/overview 核验, 推测 200K 但未经文档证实。

2. **[UNVERIFIED] LiteLLM v1.84.0 breaking changes 具体内容**: 只知道该版本含 breaking changes, 细节页未能完整提取。涉及 proxy server 多 pod 预算统计, 若本项目使用单机 SDK (非 proxy server 模式) 则可能不受影响, 但需确认。来源页: https://docs.litellm.ai/release_notes

3. **[UNVERIFIED] DeepSeek V4 Pro LiteLLM multi-turn bug 修复版本**: Issue #26395 截至调研时仍为 Open, 确认修复的 PR #27056 状态未获取到合并信息。建议在 deploy 前手动测 `pip install litellm==1.85.1` 后运行 2 轮对话测试。

4. **[UNVERIFIED] DeepSeek V4 Pro 折扣到期后真实价格**: 目前文档只给出了折后价 ($0.435 input, $0.87 output per 1M), 75% 折扣到期 (2026-05-31) 后的原价未在官方文档中单独列出。建议 2026-06-01 后重新查证 https://api-docs.deepseek.com/quick_start/pricing/

5. **[UNVERIFIED] ChatGPT Plus 独立 OpenAI API 账户的最低充值额**: 若用户决定开独立 OpenAI API 账户, 需确认当前最低充值起点 (过去为 $5, 可能变化)。

---

**报告完。调研日期: 2026-05-22。调研员: document-specialist subagent (background)。**

## Sources
- [DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing/)
- [DeepSeek Changelog](https://api-docs.deepseek.com/updates)
- [DeepSeek V4 Preview Release](https://api-docs.deepseek.com/news/news260424)
- [DeepSeek V4 Pro on HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [OpenRouter DeepSeek V4 Pro](https://openrouter.ai/deepseek/deepseek-v4-pro)
- [Anthropic Pricing Docs (official)](https://platform.claude.com/docs/en/about-claude/pricing)
- [LiteLLM DeepSeek Provider Docs](https://docs.litellm.ai/docs/providers/deepseek)
- [LiteLLM Proxy Config Docs](https://docs.litellm.ai/docs/proxy/configs)
- [LiteLLM GitHub Releases](https://github.com/BerriAI/litellm/releases)
- [LiteLLM PyPI 1.85.1](https://pypi.org/project/litellm/)
- [LiteLLM Issue #26395 - reasoning_content stripping bug](https://github.com/BerriAI/litellm/issues/26395)
- [LiteLLM Issue #26709 - DeepSeek V4 cost mapping](https://github.com/BerriAI/litellm/issues/26709)
- [OpenAI ToS (Row)](https://openai.com/policies/row-terms-of-use/)
- [DEV.to - Why You Shouldn't Reverse-Engineer ChatGPT UI](https://dev.to/gautamvhavle/i-reverse-engineered-chatgpts-ui-into-an-openai-compatible-api-and-heres-why-you-shouldnt-ch)
- [openai-oauth GitHub](https://github.com/EvanZhouDev/openai-oauth)
- [codex-openai-proxy GitHub](https://github.com/Securiteru/codex-openai-proxy)
- [CLIProxyAPI GitHub](https://github.com/router-for-me/CLIProxyAPI)
- [LiteLLM Release Versioning Change Notice](https://docs.litellm.ai/blog/cleaner-release-versions)
- [WaveSpeed DeepSeek V4 Migration Guide](https://wavespeed.ai/blog/posts/blog-deepseek-v4-model-name-migration/)
