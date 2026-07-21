# 设计规格 — ChatGPT 风格单模型聊天前端

> 状态: **设计已批准** (2026-06-16, 经 brainstorming 流程) · 待实现
> 作用: 把当前 Streamlit 多模式 UI 之外, 新建一个干净的 ChatGPT 风格单模型聊天作为对外/主界面。
> 关联: DEPLOY_PLAN.md (阶段 3 共享时为本 UI 加鉴权/对外绑定); 本 UI 先在 localhost 建好测好。

## 0. 背景与目标

阶段 2 的 Compare/Judge 是给**开发者**用数据选主力模型的工具 —— 目的已达成 (选定 DeepSeek V4 Pro)。模型既定, **终端用户 (同事) 要的是一个干净的单模型聊天**, 不需要看到三栏对比/裁判。本设计新建该界面。

**本期目标**
1. ChatGPT 风格单页聊天: 左侧对话栏 + 主聊天区 (打字机流式) + 底部输入框。
2. **有且只有一个模型: DeepSeek V4 Pro** (后端 default, 无模型选择器)。
3. 对外部署收成一个端口 (FastAPI `8000/`), 与评测工具天然隔离。

**非目标 (本期不做)**
- 鉴权/登录门、绑 `0.0.0.0`、错误串 sanitize → **阶段 3** (共享时)。
- 服务端持久化对话 (跨设备/共享历史) → YAGNI, 不做; 对话存浏览器 localStorage。
- 删除 Compare/Judge → **保留**, 原封不动留在 Streamlit `8501` 当开发/评测工具 (token 紧, 不常用)。

## 1. 全局锁定的设计决定

| 项 | 定为 | 理由 |
|---|------|------|
| 前端形态 | 静态单页 (HTML+CSS+原生 JS, **无构建/无 Node**) | 16GB Mac mini 上最轻; FastAPI 直接托管 |
| 托管 | 现有 FastAPI: `GET /` 返回页, `/static/*` 资源 | 不新增服务; 同事访问 `http://<host>:8000/` |
| 位置 | `branches/07_rag_kg/sdtm-rag/webchat/` (`index.html`/`app.js`/`style.css`/`vendor/`) | 与 server/ 同仓 |
| 模型 | 单一 DeepSeek V4 Pro (后端 `default` 组, 保留 deepseek 自重试 fallback) | 用户决策; 无选择器 |
| 流式 | SSE (`POST /api/ask_stream`) | ChatGPT 打字机感 |
| 对话存储 | 浏览器 **localStorage** (多对话, 各浏览器各存) | 不碰服务端存储/身份 |
| 引用展示 | 每条回答下**默认折叠**的"来源 (N)"面板 | KB 工具引用有价值, 但不破坏极简 |
| 检索旋钮 | **隐藏**, 走默认 (top_k=15, 无过滤) | ChatGPT 式极简 |
| 前端依赖 | 本地 vendor (无外网 CDN) | 公司网/离线可用 |
| Compare/Judge | 不动, 留 Streamlit `8501` | 开发者私用, 与同事界面隔离 |

## 2. 布局 (经典 ChatGPT 三块)

- **顶部**: 简洁标题 "SDTM 知识库助手 · DeepSeek V4 Pro"。无模型选择器、无检索旋钮。
- **左侧栏**: "新对话"按钮 + 对话列表 (点选切换 / 重命名 / 删除); 窄屏可收起 (汉堡)。
- **主区**: 消息气泡 (用户右对齐 / 助手左对齐); 助手回答**打字机流式**; 每条助手回答下挂默认折叠的 `来源 (N)` 面板 (文件路径 + 相似度 + 片段预览); 顶部空态显示欢迎/提示。
- **底部**: 多行 textarea + 发送按钮; Enter 发送 / Shift+Enter 换行; 生成中显示停止/禁用态。

## 3. 后端 — 新增流式端点

**`POST /api/ask_stream`** (新增; 现有 `/api/ask` 非流式保留不删, 供程序化/回退)。

- 请求体 (**新增专用 Pydantic 模型, 无 `model` 字段** —— 单模型, 不让前端选): `{question, history:[{role,content}], top_k?, domain?, file_type?}`。UI 只发 question + history (走默认 top_k=15, 不传过滤)。
- 处理 (顺序):
  1. 校验 question 非空 (空 → 422)。
  2. `rag.retrieve(question, top_k=...)` **同步, 一次** → 失败抛 `HTTPException(502)` (**在开流前**, 这样还能返 JSON 错误码)。
  3. `rag.format_context` → `rag.build_messages(question, context, history)`。
  4. 返回 `StreamingResponse(gen(), media_type="text/event-stream")`, headers `Cache-Control: no-cache` + `X-Accel-Buffering: no` (禁代理缓冲, 阶段 3 反代用)。
- 生成器 `gen()` (async): `await router.acompletion(model="default", messages, stream=True, stream_options={"include_usage": True})`, 异步迭代 chunk, 产出 SSE 事件:

```
event: sources
data: {"sources":[{chunk_id,source,domain,file_type,section,similarity,text_preview}, ...]}

event: token
data: {"text":"<增量文本>"}

event: done
data: {"model_used":"deepseek-v4-pro","usage":{"prompt_tokens":..,"completion_tokens":..,"total_tokens":..}}
```

- **关键**: 每个事件的 `data:` **一律 JSON 包裹** (token 增量可能含换行, JSON 转义后不会破坏 SSE `\n\n` 分帧)。`sources` 事件在迭代生成前先发 (检索已完成)。
- 出错: 开流前失败 → HTTP 502 (普通 JSON); 流中途失败 → `event: error\ndata: {"message":"..."}` 后结束。usage 拿不到则 done 里 usage=null (不编造)。
- 模型: 走 Router `default` 组 = deepseek-v4-pro (保留 fallback)。**不**新增模型选择参数。

## 4. 前端 — 结构与数据流

**localStorage schema** (key 如 `sdtm_chat_v1`):
```
{
  "conversations": [
    {"id": "<uuid>", "title": "<首条用户消息截断>", "createdAt": <ts>,
     "messages": [{"role":"user|assistant", "content":"<md>", "sources": [...]?}]}
  ],
  "currentId": "<uuid>"
}
```

**发送流程** (`app.js`):
1. 追加用户消息 → 渲染 → 创建空助手气泡占位。
2. `fetch('/api/ask_stream', {method:'POST', body: {question, history: 最近 N=10 轮}})` —— **不用 EventSource** (只支持 GET); 用 `fetch` + `response.body.getReader()` 读流, 手动按 `\n\n` 切帧解析 `event:`/`data:`。
3. `sources` 事件 → 在助手气泡下挂折叠来源面板; `token` 事件 → 增量追加进气泡 (流式渲染: 流中可纯文本追加, `done` 后再整体 markdown 渲染一次, 避免每 token 重渲染开销); `done` → 整条 (含 sources) 存进 localStorage。
4. 历史**截断**发送 (最近 10 轮) 控 token。

**Markdown 渲染**: `marked` 解析 → **`DOMPurify.sanitize`** 后再插入 DOM (净化 LLM 输出防 XSS); 代码块用 `highlight.js`。`[Source: path]` 行内引用按纯文本渲染 (结构化引用在来源面板)。

## 5. 前端依赖 (本地 vendor, 不打 CDN)

下载进 `webchat/vendor/` 并提交: `marked.min.js` (markdown) + `highlight.min.js` + 一个代码主题 css + `dompurify.min.js` (净化)。FastAPI 静态托管。**不引用任何外网 CDN** (公司网可能拦 + 离线可用)。记录各库版本于 vendor/README 或 app.js 顶部注释。

## 6. 错误处理

- 检索失败 → 开流前 502, 前端气泡显示"检索暂不可用"。
- 生成中途断 → `event: error`, 前端在气泡内追加错误提示并**保留已生成部分**。
- 连接断/网络错 → 前端 catch, 气泡显示错误 + 可重试 (重发该轮)。
- 空回答 → 显示占位 (如"(无内容)")。
- 429/限流 → Router num_retries 在首 token 前处理; 不做前端额外重试 (避免重复扣 token)。

## 7. 共存

- 聊天: FastAPI `8000/` (新, 同事用)。Compare/Judge: Streamlit `8501` (不动, 开发者用)。同一 FastAPI 进程托管聊天, **不新增 launchd 服务**; Streamlit 服务保持。
- 不在同事聊天界面放跳转 Compare 的链接 (保持对外干净); 你自己知道 8501 即可。

## 8. 验证 & 审阅 (规则 A/D)

- **后端**: pytest/手测 `/api/ask_stream` 产出 `sources → token* → done` 事件序列 (短问题); 检索失败走 502; 中途错误走 error 事件。
- **前端**: 真实跑 + 截图核验 (发问→打字机流式→来源面板→多对话切换/刷新不丢/新对话/删除); 跨一两个浏览器验 localStorage 隔离。
- **规则 D 独立审阅** (异 subagent_type): 重点 ① XSS (markdown 必经 DOMPurify) ② SSE 手动解析鲁棒 (半包/多事件/中断) ③ 流式错误与 token 计费 ④ 不回归现有 `/api/ask` 与 Streamlit。

## 9. 文件改动清单 (预估)

| 文件 | 改动 |
|------|------|
| `server/router.py` | 加 `POST /api/ask_stream` (SSE) + 请求模型 |
| `server/main.py` | 挂静态托管 (`GET /` → index.html, `/static`) |
| `webchat/index.html` (新) | 页面骨架 |
| `webchat/app.js` (新) | 状态/侧栏/流式/localStorage/markdown |
| `webchat/style.css` (新) | ChatGPT 式样式 |
| `webchat/vendor/*` (新) | marked / highlight.js+css / dompurify (提交) |

## 10. 开放项 (实现时定, 不阻塞)

- 对话重命名是否需要 (可先只 New/切换/删除, 重命名后补)。
- 来源面板片段长度 (沿用现有 300 字符)。
- 标题自动生成规则 (首条用户消息截断 N 字)。
