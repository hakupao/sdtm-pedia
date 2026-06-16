# Chat UI 集成核验 (Rule A) — ChatGPT 风格单模型流式聊天

> 日期: 2026-06-16 · 计划: `PLAN_chat_ui.md` (Task 6) · 设计: `DESIGN_chat_ui.md`
> 验证者: 主 session (writer) · 独立审阅 (Rule D): 见本文 §4 (异 subagent_type)
> 服务: 临时 `127.0.0.1:8021` 实例 (不碰 launchd 8000/8501); 真模型 = DeepSeek V4 Pro

## 1. 后端 SSE 真模型流式 (curl, 非 stub)

`POST /api/ask_stream {"question":"What is AETERM? One short sentence."}` →

| 项 | 结果 |
|----|------|
| 事件序列 | **1× `event: sources` → 42× `event: token` → 1× `event: done`** ✅ |
| sources 先于 token | ✅ (sources 在迭代生成前发) |
| token 增量 | `"A"` / `"ETER"` / `"M"` … 逐字流式 ✅ |
| done.usage | `{prompt_tokens:16715, completion_tokens:200, total_tokens:16915}` — **DeepSeek 接受 `stream_options.include_usage`**, usage 真实非 null (计划所担心的 kwarg 被拒风险未发生) ✅ |
| done.model_used | `deepseek-v4-pro` ✅ |
| 重组答案 | "AETERM is the verbatim term collected for the adverse event, serving as the topic variable of the AE domain. [Source: domains/AE/spec.md; domains/AE/assumptions.md]" — 接地正确 ✅ |

单测 (stub): `scripts/tests/test_ask_stream.py` 2 passed (事件序列 + 空问题 422)。

## 2. 前端真实浏览器核验 (Playwright, 临时 8021 真后端)

逐项 (DOM + localStorage 程序化断言, 非仅截图):

| # | 验证项 | 结果 |
|---|--------|------|
| 1 | 打字机流式 + markdown 渲染 (中文问→中文答) | 答案 "AETERM 是 AE（不良事件）域的主题变量…该变量为 Required（Req）…"; `rendered_has_html_tags=true`; **语言跟随** OK, SDTM 标识符 (AETERM/Req/AE) 留英文 ✅ |
| 2 | 无 XSS | `has_script_tag=false` (经 DOMPurify.sanitize) ✅ |
| 3 | 来源面板默认折叠 | `sources_panel_present=true`, `collapsed_by_default=true`, summary `来源 (15)`, 展开见文件/相似度/片段 ✅ |
| 4 | localStorage 持久 | roles `[user,assistant]`, title=首条问题截断, asst.sources=15 条 ✅ |
| 5 | 流式结束复位 | `send_disabled=false` (busy 复位) ✅ |
| 6 | 多轮上下文 (history) | 追问「它的 Core 属性是什么？」→ "AETERM 的 Core 属性为 **Req（必需）**" — **「它」经 history 正确解析为 AETERM** ✅ |
| 7 | 新对话 + 切换 | "+ 新对话" → 侧栏 2 条 (新在顶), 切回历史对话渲染回 4 条消息 + 2 来源面板 ✅ |
| 8 | 刷新不丢 | reload 后 2 对话仍在, 历史对话仍 4 条消息 ✅ |
| 9 | 删除 | 删空对话 → 剩 1 条 ✅ |
| 10 | 错误不白屏 | 杀后端 → 提问 → 红色气泡 "⚠ 无法连接服务", 6 条消息仍在 DOM, send 复位, 侧栏完好 ✅ |

控制台: 仅 `favicon.ico 404` (无害), 无 JS 报错。

截图: `chat_ui_smoke_main.png` (流式答案 + 来源) · `chat_ui_smoke_error.png` (断后端错误气泡)。

## 3. 不回归

- `uv run --extra dev pytest` → **262 passed** (含新 test_ask_stream.py)。
- Streamlit `8501` (Compare/Judge) → HTTP 200, 未碰 (本计划只加 8000 侧)。
- launchd `com.sdtmrag.{api,ui}` 均在; 8000/8501 LISTEN 正常。
- 临时 8021 实例与 launchd 8000 **同时打开 `data/chroma` 无锁冲突** (rag_init_s=0.71)。

## 环境差异 (实施记录)

- 计划写 `.venv/bin/pytest`, 但部署期 `uv sync` 已剪掉 dev extras → 实际用 **`uv run --extra dev pytest`** (uv.lock 锁版本, 仅增 pytest/ruff/mypy, 不动 runtime 依赖, 不扰 launchd)。
- 计划 highlight.js vendor URL 包名笔误 `@highlight.js/cdn-assets` → 实为 **`@highlightjs/cdn-assets`** (无点); 已在 `webchat/vendor/README.md` 记正确 URL。
- ruff: 新端点 `ask_stream` 的 B904 (except 内 raise 不带 `from`) 与既有 `/ask`·`/ask_compare`·`/validate` 五处同款, 属 house 既有 idiom, 保持一致未改 (基线 router.py 9 errors); 新测试文件 I001 已 `--fix`。

## 4. 独立审阅 (Rule D)

3 lens 异 subagent_type 并行 (writer=主 session, 审阅独立 context) — workflow `chat-ui-rule-d-review` (218k tok, 3 agent):
- **security-reviewer (XSS/注入)** → **SHIP**, 0 BLOCKER/HIGH。逐一追踪 DOM 注入点: assistant 输出全经单一 choke `mdToSafeHTML=DOMPurify.sanitize(marked.parse())`; 来源 src.*/用户气泡/标题全 textContent; sourcesEl 只 innerHTML 静态字面量。对抗向量 (`<img onerror>`/`javascript:`/`data:`/`<script>`) 被 DOMPurify 3.1.6 默认拦截 (无 setConfig 放宽)。后端 error 事件发服务端常量, 不回显输入。
- **code-reviewer (SSE 鲁棒)** → REQUEST_CHANGES (1 HIGH)。后端 framing 全对 (每帧 `\n\n` 收尾; json.dumps 转义换行); 缺陷在前端终止处理。
- **critic (计费/回归/perf)** → ACCEPT-WITH-RESERVATIONS (1 HIGH)。计费安全 SOUND (onError 不自动重发=不重复扣 token; busy 防并发; history slice 正确; /api/ask + Streamlit 不回归; model=default 有效组)。

### 已修 (6 项, 均带验证)

| # | Sev | 修复 | 验证 |
|---|-----|------|------|
| 1 | HIGH | 干净 EOF 无 done/error 帧 → 答案丢失。`streamAsk` 加 terminal 追踪 + 尾 buf flush + `onClose`; `send` 在 onClose 落盘 acc | stub fetch 模拟无 done 帧 → 内容 "Partial answer" **落盘**, 提示「连接中断（已保留）」, send 复位 ✅ |
| 2 | HIGH | 每 token 重渲染 markdown+高亮 (违 DESIGN §4, O(n²)) → 改流中纯文本追加, done 后渲染一次 | 真模型 markdown 题: 终态 DOM 有 `<ul><li><strong>`, 无裸 `**`, console 0 warning (无 hljs 重高亮刷屏) ✅ |
| 3 | MED | 空回答 → 空白气泡 (违 DESIGN §6) → done 且 acc 空时占位 "(无内容)" | stub done 零 token → 落盘+显示 "(无内容)" ✅ |
| 4 | MED | busy 复位不在 finally → 回调抛异常永久锁 send → 包 try/finally | send 复位实测 ✅ |
| 5 | MED | `save()` 无配额保护 → QuotaExceeded 丢答案/锁 UI → try/catch + 淘汰最旧对话重试 | 代码审 (淘汰 newest-first 尾部) |
| 7 | MED | 提供商拒 `stream_options` → 整答案空白, 无回退 → 后端 `_open_stream` 首次失败则去掉 kwarg 重试一次 (usage→null 不编造; 迭代中失败不重试=不重复生成) | 新单测 `test_ask_stream_falls_back_without_stream_options` (3 passed) ✅ |

### 延后 (已记录, 非阻塞; 多属阶段 3 共享/暴露范围)

- **#6 Stop/Abort + 重试 UX** (critic MED; DESIGN §2「停止/禁用态」的「/」可读作仅禁用, §6「可重试」当前靠重打字): 属功能增强, **留给用户决定是否在阶段 3 拉进** (AbortController + Stop 按钮 + AbortError 当干净取消不报错)。
- **#8 topbar 模型真实性** (critic INFO): 现 `.env` 已设 deepseek (启动日志实证), topbar 硬编码正确; 阶段 3 部署时改为读 `/api/info` 的 default_model + 部署 checklist 校验 (防无 `.env` 时显示 DeepSeek 实跑 Sonnet)。
- **#10 CSP / X-Content-Type-Options** (security LOW) + **请求超时** (INFO): 阶段 3 随鉴权/绑 0.0.0.0 一并加 `default-src 'self'`。
- **INFO** parseSSE 多行 data 拼接耦合单行 JSON: 当前后端恒单行 JSON, 安全; 若复用于多行 data 需按 SSE 规范以 `\n` join。

> 净: 2 HIGH + 4 MED 全修并验证; XSS lens 全清; 计费安全/不回归经独立确认。残留全为阶段 3 暴露相关增强, 非本期 localhost 阻塞。
