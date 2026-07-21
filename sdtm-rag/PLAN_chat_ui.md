# ChatGPT 风格单模型聊天前端 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 新建一个 ChatGPT 风格的单模型 (DeepSeek V4 Pro) 流式聊天前端, 由现有 FastAPI 托管于 `8000/`, 作为对外/主界面; Compare/Judge 不动, 留 Streamlit `8501`。

**Architecture:** 后端加一个 SSE 流式端点 `POST /api/ask_stream` (复用 retrieve/format/build, 走 Router `default`=deepseek-v4-pro)。前端是静态单页 (HTML+CSS+原生 JS, 无构建), FastAPI 静态托管; 多对话存浏览器 localStorage; markdown 经 DOMPurify 净化后渲染。

**Tech Stack:** Python/FastAPI (StreamingResponse), litellm Router acompletion(stream=True), 原生 JS (fetch + ReadableStream 解析 SSE), vendored marked / DOMPurify / highlight.js (无外网 CDN)。

**规格来源:** `branches/07_rag_kg/sdtm-rag/DESIGN_chat_ui.md` (经 brainstorming 批准 2026-06-16)。

**前置说明:** 本计划在新 session 与阶段 3 合并执行 —— **先做本计划 (聊天 UI, 全程 localhost)**, 再做阶段 3 (鉴权/绑 0.0.0.0/login gate, 见 DEPLOY_PLAN §3 + §7 待定项)。本计划全程不碰鉴权/对外绑定。

---

## 文件结构

| 文件 | 责任 | 创建/修改 |
|------|------|-----------|
| `server/router.py` | 加 `AskStreamRequest` + `POST /api/ask_stream` (SSE) | 修改 |
| `server/main.py` | 静态托管: `GET /`→index.html, `/static`→webchat/ | 修改 |
| `scripts/tests/test_ask_stream.py` | 端点 SSE 事件序列单测 (stub rag+router) | 创建 |
| `webchat/index.html` | 页面骨架 | 创建 |
| `webchat/style.css` | ChatGPT 式布局样式 | 创建 |
| `webchat/app.js` | 状态/侧栏/localStorage/渲染/发送/SSE 流式 | 创建 |
| `webchat/vendor/` | marked / DOMPurify / highlight.js (+css), 提交 | 创建 |

事件契约 (后端发, 前端解析), 每个 `data:` 一律 JSON:
- `event: sources` → `{"sources":[{chunk_id,source,domain,file_type,section,similarity,text_preview}]}`
- `event: token`   → `{"text":"<增量>"}`
- `event: done`    → `{"model_used":"...","usage":{...}|null}`
- `event: error`   → `{"message":"..."}`

localStorage key `sdtm_chat_v1` → `{"conversations":[{id,title,createdAt,messages:[{role,content,sources?}]}],"currentId":"<id>"}`。

---

## Task 1: 后端 SSE 流式端点 `/api/ask_stream` (TDD)

**Files:**
- Modify: `server/router.py` (顶部 import + 新模型 + 新端点)
- Test: `scripts/tests/test_ask_stream.py`

- [ ] **Step 1: 写失败测试** (stub 掉 rag+router, 断言事件序列)

Create `scripts/tests/test_ask_stream.py`:
```python
from types import SimpleNamespace
from fastapi import FastAPI
from fastapi.testclient import TestClient
from server.router import api_router


class _FakeRAG:
    def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
        return [SimpleNamespace(chunk_id="c1", source="domains/AE/spec.md", domain="AE",
                                file_type="spec", section="§1", similarity=0.9,
                                text="AETERM is the reported term." * 5)]
    def format_context(self, chunks):
        return "CTX"
    def build_messages(self, q, ctx, history=None):
        return [{"role": "user", "content": q}]


class _FakeRouter:
    async def acompletion(self, model, messages, stream=False, **kw):
        async def agen():
            for t in ["Hello", " world"]:
                yield SimpleNamespace(model="deepseek-v4-pro",
                                      choices=[SimpleNamespace(delta=SimpleNamespace(content=t))],
                                      usage=None)
            yield SimpleNamespace(model="deepseek-v4-pro", choices=[],
                                  usage=SimpleNamespace(prompt_tokens=10, completion_tokens=2, total_tokens=12))
        return agen()


def _client():
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.llm_router = _FakeRouter()
    return TestClient(app)


def test_ask_stream_event_sequence():
    r = _client().post("/api/ask_stream", json={"question": "what is AETERM?", "history": []})
    assert r.status_code == 200
    body = r.text
    assert "event: sources" in body
    assert "event: token" in body
    assert '"text": "Hello"' in body
    assert "event: done" in body
    assert '"total_tokens": 12' in body
    # sources event precedes first token
    assert body.index("event: sources") < body.index("event: token")


def test_ask_stream_empty_question_422():
    r = _client().post("/api/ask_stream", json={"question": "   ", "history": []})
    assert r.status_code == 422
```

- [ ] **Step 2: 运行确认失败**

Run: `cd branches/07_rag_kg/sdtm-rag && .venv/bin/pytest scripts/tests/test_ask_stream.py -v`
Expected: FAIL (404 / no `/api/ask_stream` route)。

- [ ] **Step 3: 实现端点** (在 `server/router.py`)

在顶部 import 区加:
```python
import json
from fastapi.responses import StreamingResponse
```

在 `/api/ask` 端点之后 (或 `# ── Multi-model compare` 段之前) 加:
```python
class AskStreamRequest(BaseModel):
    question: str = Field(max_length=10000)
    history: list[MessageItem] = Field(default_factory=list)
    top_k: int | None = Field(None, ge=1, le=100)
    domain: str | None = None
    file_type: str | None = None


@api_router.post("/ask_stream")
async def ask_stream(body: AskStreamRequest, request: Request):
    """SSE 流式单模型问答 (DeepSeek V4 Pro via Router 'default'). 检索一次 (FR1),
    然后流式生成。检索失败在开流前返 502; 流中途失败发 error 事件。"""
    rag = request.app.state.rag
    llm_router = request.app.state.llm_router

    if not body.question.strip():
        raise HTTPException(status_code=422, detail="question must not be empty")

    try:
        chunks = rag.retrieve(
            body.question, domain=body.domain, file_type=body.file_type, top_k=body.top_k
        )
    except Exception as e:
        log.error("stream_retrieve_failed", error=str(e), exc_info=True)
        raise HTTPException(status_code=502, detail="Retrieval service temporarily unavailable.")

    context = rag.format_context(chunks)
    history_dicts = [{"role": m.role, "content": m.content} for m in body.history]
    messages = rag.build_messages(body.question, context, history_dicts or None)
    sources = [
        {"chunk_id": c.chunk_id, "source": c.source, "domain": c.domain,
         "file_type": c.file_type, "section": c.section,
         "similarity": c.similarity, "text_preview": c.text[:300]}
        for c in chunks
    ]

    def sse(event: str, data: dict) -> str:
        return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"

    async def gen():
        yield sse("sources", {"sources": sources})
        model_used = None
        usage = None
        try:
            resp = await llm_router.acompletion(
                model="default", messages=messages, stream=True,
                stream_options={"include_usage": True},
            )
            async for chunk in resp:
                choices = getattr(chunk, "choices", None)
                if choices:
                    text = getattr(choices[0].delta, "content", None)
                    if text:
                        yield sse("token", {"text": text})
                    model_used = getattr(chunk, "model", None) or model_used
                cu = getattr(chunk, "usage", None)
                if cu:
                    usage = {"prompt_tokens": cu.prompt_tokens,
                             "completion_tokens": cu.completion_tokens,
                             "total_tokens": cu.total_tokens}
            yield sse("done", {"model_used": model_used or "default", "usage": usage})
        except Exception as e:  # noqa: BLE001 — stream already open, surface as event
            log.error("stream_failed", error=str(e), exc_info=True)
            yield sse("error", {"message": "LLM stream failed"})

    return StreamingResponse(
        gen(), media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
```

> 实现注记: 若 deepseek 拒绝 `stream_options` 参数 (报错), 去掉该 kwarg —— usage 则为 null (done 里如实显示 null, 不编造)。先按上面带着跑, 集成测 (Task 6) 真实验证。

- [ ] **Step 4: 运行确认通过**

Run: `.venv/bin/pytest scripts/tests/test_ask_stream.py -v`
Expected: 2 passed。

- [ ] **Step 5: 不回归现有测试**

Run: `.venv/bin/pytest -q`
Expected: 全绿 (现有用例不受影响)。

- [ ] **Step 6: 提交**

```bash
git add server/router.py scripts/tests/test_ask_stream.py
git commit -m "07 RAG+KG chat UI: 加 /api/ask_stream SSE 流式端点 (单模型 default, TDD)"
```

---

## Task 2: FastAPI 静态托管 webchat

**Files:**
- Modify: `server/main.py`

- [ ] **Step 1: 加静态托管** (`server/main.py`)

顶部 import 加:
```python
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
```

在 `app.include_router(api_router)` 之后加:
```python
_WEBCHAT_DIR = Path(__file__).resolve().parent.parent / "webchat"
if _WEBCHAT_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(_WEBCHAT_DIR)), name="static")

    @app.get("/")
    def chat_index():
        return FileResponse(str(_WEBCHAT_DIR / "index.html"))
```

> `/static` 与 `/api/*` 路径不冲突; webchat 目录此刻可能还没建 (Task 3-5), 故 `if exists()` 守卫, 后续文件就位后自动生效。

- [ ] **Step 2: 验证 (建一个占位 index 临时测路由)**

```bash
mkdir -p webchat && echo '<!doctype html><title>ok</title>chat-shell' > webchat/index.html
.venv/bin/uvicorn server.main:app --host 127.0.0.1 --port 8021 &  # 等 ~3s
curl -s -m 5 http://127.0.0.1:8021/ | grep -q chat-shell && echo "GET / OK"
kill %1
```
Expected: `GET / OK`。(8021 临时口, 不碰 launchd 8000。)

- [ ] **Step 3: 提交**

```bash
git add server/main.py webchat/index.html
git commit -m "07 RAG+KG chat UI: FastAPI 静态托管 webchat (GET / + /static)"
```

---

## Task 3: Vendor 前端依赖 (无外网 CDN)

**Files:**
- Create: `webchat/vendor/marked.min.js`, `webchat/vendor/purify.min.js`, `webchat/vendor/highlight.min.js`, `webchat/vendor/highlight.github.min.css`, `webchat/vendor/README.md`

- [ ] **Step 1: 下载固定版本进 vendor/**

```bash
cd branches/07_rag_kg/sdtm-rag/webchat && mkdir -p vendor && cd vendor
curl -sL https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js -o marked.min.js
curl -sL https://cdn.jsdelivr.net/npm/dompurify@3.1.6/dist/purify.min.js -o purify.min.js
curl -sL https://cdn.jsdelivr.net/npm/@highlight.js/cdn-assets@11.9.0/highlight.min.js -o highlight.min.js
curl -sL https://cdn.jsdelivr.net/npm/@highlight.js/cdn-assets@11.9.0/styles/github.min.css -o highlight.github.min.css
```
> 仅**下载时**用 CDN; 运行时全部本地 serve, 不依赖外网。版本固定。

- [ ] **Step 2: 验证文件非空且像 JS/CSS**

Run:
```bash
cd branches/07_rag_kg/sdtm-rag/webchat/vendor
for f in marked.min.js purify.min.js highlight.min.js highlight.github.min.css; do
  test -s "$f" && head -c 40 "$f" && echo "  <- $f OK" || echo "EMPTY: $f"
done
```
Expected: 4 个文件均非空 (marked/purify/highlight 头部是 JS, css 是样式)。若某个空 (网络/版本变动), 换镜像或版本重下。

- [ ] **Step 3: 记录版本 + 提交**

Create `webchat/vendor/README.md`:
```markdown
# Vendored frontend libs (无外网 CDN, 运行时本地 serve)
- marked@12.0.2 — markdown 渲染
- dompurify@3.1.6 — 净化 LLM 输出 (XSS 防护)
- highlight.js@11.9.0 (cdn-assets) + github 主题 — 代码高亮
下载源 jsDelivr (仅下载时)。升级: 重下对应版本并复测。
```

```bash
git add webchat/vendor
git commit -m "07 RAG+KG chat UI: vendor marked/dompurify/highlight.js (无外网 CDN)"
```

---

## Task 4: 页面骨架 + 样式

**Files:**
- Create/Overwrite: `webchat/index.html`, `webchat/style.css`

- [ ] **Step 1: 写 index.html** (覆盖 Task 2 的占位)

```html
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>SDTM 知识库助手</title>
  <link rel="stylesheet" href="/static/vendor/highlight.github.min.css" />
  <link rel="stylesheet" href="/static/style.css" />
</head>
<body>
  <div id="app">
    <aside id="sidebar">
      <button id="new-chat">+ 新对话</button>
      <ul id="conv-list"></ul>
    </aside>
    <main id="main">
      <header id="topbar">SDTM 知识库助手 · DeepSeek V4 Pro</header>
      <div id="messages"></div>
      <form id="composer">
        <textarea id="input" rows="1" placeholder="问点关于 SDTM 的……（Enter 发送，Shift+Enter 换行）"></textarea>
        <button id="send" type="submit">发送</button>
      </form>
    </main>
  </div>
  <script src="/static/vendor/marked.min.js"></script>
  <script src="/static/vendor/purify.min.js"></script>
  <script src="/static/vendor/highlight.min.js"></script>
  <script src="/static/app.js"></script>
</body>
</html>
```

- [ ] **Step 2: 写 style.css** (ChatGPT 式两栏 + 气泡 + 粘底输入)

```css
* { box-sizing: border-box; }
html, body { margin: 0; height: 100%; font-family: -apple-system, "Segoe UI", "PingFang SC", sans-serif; }
#app { display: flex; height: 100vh; }
#sidebar { width: 260px; background: #f7f7f8; border-right: 1px solid #e5e5e5; display: flex; flex-direction: column; padding: 12px; gap: 8px; overflow-y: auto; }
#new-chat { padding: 10px; border: 1px solid #d0d0d0; border-radius: 8px; background: #fff; cursor: pointer; font-size: 14px; }
#new-chat:hover { background: #ececf1; }
#conv-list { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 4px; }
#conv-list li { padding: 8px 10px; border-radius: 8px; cursor: pointer; font-size: 13px; color: #333; display: flex; justify-content: space-between; align-items: center; gap: 6px; }
#conv-list li:hover { background: #ececf1; }
#conv-list li.active { background: #e3e3ec; font-weight: 600; }
#conv-list .title { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; flex: 1; }
#conv-list .del { opacity: 0; border: none; background: none; cursor: pointer; color: #999; }
#conv-list li:hover .del { opacity: 1; }
#main { flex: 1; display: flex; flex-direction: column; min-width: 0; }
#topbar { padding: 14px 20px; border-bottom: 1px solid #ececec; font-size: 15px; font-weight: 600; color: #444; }
#messages { flex: 1; overflow-y: auto; padding: 24px 0; }
.msg { max-width: 760px; margin: 0 auto 18px; padding: 0 20px; display: flex; gap: 12px; }
.msg .role { width: 28px; height: 28px; border-radius: 6px; flex: 0 0 28px; text-align: center; line-height: 28px; font-size: 12px; color: #fff; }
.msg.user .role { background: #19c37d; }
.msg.assistant .role { background: #ab68ff; }
.msg .bubble { flex: 1; min-width: 0; line-height: 1.6; color: #1a1a1a; }
.msg .bubble pre { background: #f6f8fa; padding: 12px; border-radius: 8px; overflow-x: auto; }
.msg .bubble code { font-family: ui-monospace, Menlo, monospace; font-size: 13px; }
.msg .bubble table { border-collapse: collapse; }
.msg .bubble th, .msg .bubble td { border: 1px solid #ddd; padding: 4px 8px; }
.sources { max-width: 760px; margin: -8px auto 18px; padding: 0 20px 0 52px; }
.sources summary { cursor: pointer; color: #666; font-size: 13px; }
.sources .src { font-size: 12px; color: #555; border-left: 2px solid #ddd; padding: 4px 8px; margin: 6px 0; }
.err { color: #c00; }
#composer { max-width: 760px; width: 100%; margin: 0 auto; padding: 12px 20px 20px; display: flex; gap: 8px; }
#input { flex: 1; resize: none; max-height: 200px; padding: 12px; border: 1px solid #d0d0d0; border-radius: 12px; font-size: 15px; font-family: inherit; }
#send { padding: 0 18px; border: none; border-radius: 12px; background: #19c37d; color: #fff; cursor: pointer; font-size: 15px; }
#send:disabled { background: #b8b8b8; cursor: default; }
```

- [ ] **Step 3: 视觉核验**

Run: `.venv/bin/uvicorn server.main:app --host 127.0.0.1 --port 8021` 然后浏览器开 `http://127.0.0.1:8021/`。
Expected: 看到左侧栏 (有"+ 新对话") + 顶栏标题 + 底部输入框的空壳布局 (还不能对话)。截图留存。停 uvicorn。

- [ ] **Step 4: 提交**

```bash
git add webchat/index.html webchat/style.css
git commit -m "07 RAG+KG chat UI: 页面骨架 + ChatGPT 式样式"
```

---

## Task 5: app.js — 状态/侧栏/localStorage/渲染/发送/流式

**Files:**
- Create: `webchat/app.js`

- [ ] **Step 1: 写 app.js (完整)**

```javascript
// SDTM chat UI — 单模型 (DeepSeek V4 Pro) 流式聊天, 多对话存 localStorage。
const LS_KEY = "sdtm_chat_v1";
const HISTORY_TURNS = 10; // 控 token: 发给后端的最近消息条数

// uid 不用 crypto.randomUUID (LAN http 非安全上下文不可用, 阶段 3 会踩坑)
const uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 8);

let store = load();

function load() {
  try {
    const s = JSON.parse(localStorage.getItem(LS_KEY));
    if (s && Array.isArray(s.conversations)) return s;
  } catch (_) {}
  return { conversations: [], currentId: null };
}
function save() { localStorage.setItem(LS_KEY, JSON.stringify(store)); }

function current() {
  let c = store.conversations.find((x) => x.id === store.currentId);
  if (!c) { c = newConversation(); }
  return c;
}
function newConversation() {
  const c = { id: uid(), title: "新对话", createdAt: Date.now(), messages: [] };
  store.conversations.unshift(c);
  store.currentId = c.id;
  save();
  return c;
}
function deleteConversation(id) {
  store.conversations = store.conversations.filter((x) => x.id !== id);
  if (store.currentId === id) store.currentId = store.conversations[0]?.id ?? null;
  save();
  renderSidebar();
  renderMessages();
}

// ── 渲染 ──
const $ = (id) => document.getElementById(id);

function renderSidebar() {
  const ul = $("conv-list");
  ul.innerHTML = "";
  for (const c of store.conversations) {
    const li = document.createElement("li");
    if (c.id === store.currentId) li.className = "active";
    const t = document.createElement("span");
    t.className = "title";
    t.textContent = c.title || "新对话";
    t.onclick = () => { store.currentId = c.id; save(); renderSidebar(); renderMessages(); };
    const del = document.createElement("button");
    del.className = "del"; del.textContent = "✕";
    del.onclick = (e) => { e.stopPropagation(); deleteConversation(c.id); };
    li.append(t, del);
    ul.appendChild(li);
  }
}

function mdToSafeHTML(md) {
  return DOMPurify.sanitize(marked.parse(md || ""));
}
function highlightIn(el) {
  el.querySelectorAll("pre code").forEach((b) => hljs.highlightElement(b));
}

function renderMessages() {
  const box = $("messages");
  box.innerHTML = "";
  const c = store.conversations.find((x) => x.id === store.currentId);
  if (!c) return;
  for (const m of c.messages) {
    box.appendChild(messageEl(m.role, m.content, m.sources));
  }
  box.scrollTop = box.scrollHeight;
}

function messageEl(role, content, sources) {
  const wrap = document.createElement("div");
  const msg = document.createElement("div");
  msg.className = "msg " + role;
  const r = document.createElement("div");
  r.className = "role"; r.textContent = role === "user" ? "你" : "AI";
  const b = document.createElement("div");
  b.className = "bubble";
  if (role === "assistant") { b.innerHTML = mdToSafeHTML(content); highlightIn(b); }
  else { b.textContent = content; }
  msg.append(r, b);
  wrap.appendChild(msg);
  if (sources && sources.length) wrap.appendChild(sourcesEl(sources));
  return wrap;
}

function sourcesEl(sources) {
  const d = document.createElement("details");
  d.className = "sources";
  const s = document.createElement("summary");
  s.textContent = `来源 (${sources.length})`;
  d.appendChild(s);
  for (const src of sources) {
    const div = document.createElement("div");
    div.className = "src";
    div.innerHTML = `<b></b> <span></span>`;
    div.querySelector("b").textContent = src.source + (src.section ? ` — ${src.section}` : "");
    div.querySelector("span").textContent = ` (sim ${(src.similarity ?? 0).toFixed(3)})`;
    const p = document.createElement("div");
    p.textContent = src.text_preview || "";
    div.appendChild(p);
    d.appendChild(div);
  }
  return d;
}

// ── SSE 流式 ──
function parseSSE(raw) {
  let event = "message", data = "";
  for (const line of raw.split("\n")) {
    if (line.startsWith("event:")) event = line.slice(6).trim();
    else if (line.startsWith("data:")) data += line.slice(5).trim();
  }
  if (!data) return null;
  try { return { event, data: JSON.parse(data) }; } catch (_) { return null; }
}

async function streamAsk(question, history, { onSources, onToken, onDone, onError }) {
  let resp;
  try {
    resp = await fetch("/api/ask_stream", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, history }),
    });
  } catch (e) { onError("无法连接服务"); return; }
  if (!resp.ok) { onError(`服务错误 ${resp.status}`); return; }
  const reader = resp.body.getReader();
  const dec = new TextDecoder();
  let buf = "";
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    buf += dec.decode(value, { stream: true });
    let i;
    while ((i = buf.indexOf("\n\n")) !== -1) {
      const ev = parseSSE(buf.slice(0, i));
      buf = buf.slice(i + 2);
      if (!ev) continue;
      if (ev.event === "sources") onSources(ev.data.sources || []);
      else if (ev.event === "token") onToken(ev.data.text || "");
      else if (ev.event === "done") onDone(ev.data || {});
      else if (ev.event === "error") onError(ev.data.message || "生成失败");
    }
  }
}

// ── 发送 ──
let busy = false;

async function send(text) {
  if (busy || !text.trim()) return;
  busy = true; $("send").disabled = true;
  const c = current();
  c.messages.push({ role: "user", content: text });
  if (c.messages.length === 1) c.title = text.slice(0, 30);
  save(); renderSidebar(); renderMessages();

  // 助手占位气泡 (流式写入)
  const box = $("messages");
  const holder = messageEl("assistant", "", null);
  box.appendChild(holder); box.scrollTop = box.scrollHeight;
  const bubble = holder.querySelector(".bubble");

  const history = c.messages.slice(0, -1)
    .filter((m) => m.role === "user" || m.role === "assistant")
    .slice(-HISTORY_TURNS)
    .map((m) => ({ role: m.role, content: m.content }));

  let acc = "";
  let gotSources = null;
  await streamAsk(text, history, {
    onSources: (s) => { gotSources = s; if (s.length) holder.appendChild(sourcesEl(s)); },
    onToken: (t) => { acc += t; bubble.innerHTML = mdToSafeHTML(acc); highlightIn(bubble); box.scrollTop = box.scrollHeight; },
    onDone: () => {
      c.messages.push({ role: "assistant", content: acc, sources: gotSources || [] });
      save(); renderSidebar();
    },
    onError: (msg) => {
      const e = document.createElement("div"); e.className = "err"; e.textContent = "⚠ " + msg;
      bubble.appendChild(e);
      if (acc) { c.messages.push({ role: "assistant", content: acc, sources: gotSources || [] }); save(); }
    },
  });
  busy = false; $("send").disabled = false;
}

// ── 事件绑定 ──
$("new-chat").onclick = () => { newConversation(); renderSidebar(); renderMessages(); $("input").focus(); };
$("composer").onsubmit = (e) => { e.preventDefault(); const v = $("input").value; $("input").value = ""; $("input").style.height = "auto"; send(v); };
$("input").addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); $("composer").requestSubmit(); }
});
$("input").addEventListener("input", (e) => { e.target.style.height = "auto"; e.target.style.height = e.target.scrollHeight + "px"; });

// ── 启动 ──
if (!store.conversations.length) newConversation();
renderSidebar();
renderMessages();
```

- [ ] **Step 2: 真实端到端核验** (连 launchd 8000 的真后端, 或临时 8021)

Run: 用临时实例 (不碰 launchd): `.venv/bin/uvicorn server.main:app --host 127.0.0.1 --port 8021`, 浏览器开 `http://127.0.0.1:8021/`。
逐项核验 (截图留存):
1. 问一题 (如 "What is AETERM?") → 看到**打字机流式**逐字出 + 答案是 markdown (粗体/表格正常)。
2. 答案下有**默认折叠的"来源 (N)"**, 展开能看到文件/相似度/片段。
3. 点 "+ 新对话" → 开新会话; 侧栏出现两条; 切换能看到各自历史。
4. **刷新页面** → 对话还在 (localStorage)。删除一条 → 消失。
5. 故意停后端再问 → 气泡显示 "⚠ 无法连接服务", 不白屏。
停 uvicorn。

- [ ] **Step 3: 提交**

```bash
git add webchat/app.js
git commit -m "07 RAG+KG chat UI: app.js 状态/侧栏/localStorage/流式渲染/来源面板"
```

---

## Task 6: 集成核验 + 独立审阅 (规则 D)

**Files:** 无新增 (验证 + 评审)

- [ ] **Step 1: 全链路核验 (连真模型)**

Run 临时实例, 浏览器跑 3-5 个真实 SDTM 问题, 确认: 流式正常、引用正确、多轮追问 (后端收 history) 上下文连贯、中文问→中文答、代码/表格渲染 OK。截图存 `evidence/checkpoints/chat_ui_smoke.md` (Rule A)。

- [ ] **Step 2: 确认不回归**

```bash
.venv/bin/pytest -q
```
Expected: 全绿 (含 Task 1 新测)。手动确认 Streamlit `8501` Compare/Judge 仍正常 (本计划没碰它)。

- [ ] **Step 3: 独立审阅 (规则 D, 异 subagent_type)**

派 `security-reviewer` (或 code-reviewer) 独立审, 重点:
- **XSS**: 所有 LLM 输出/用户输入插入 DOM 前是否都经 `DOMPurify.sanitize` (assistant 气泡 `mdToSafeHTML`) 或 `textContent` (user 气泡、来源片段)。确认没有裸 `innerHTML = 用户/模型内容`。
- **SSE 解析**: 半包/跨 chunk 分帧、多事件同 chunk、token 含换行 (JSON 转义) 是否都正确; 流中断/error 事件处理。
- **流式与计费**: 错误不触发自动重发 (避免重复扣 token); history 截断生效。
- **不回归**: `/api/ask` (非流式) 与 Streamlit Compare/Judge 未受影响。
修掉真问题 (BLOCKER/HIGH 必修), 落 evidence。

- [ ] **Step 4: 提交修复 (若有)**

```bash
git add -A && git commit -m "07 RAG+KG chat UI: 落地独立审阅修复 + 集成核验证据"
```

---

## 完成标准
- `http://127.0.0.1:8021/` (本机) ChatGPT 式聊天: 流式、多对话侧栏 (localStorage)、来源折叠、单模型 DeepSeek、markdown+代码高亮、错误不白屏。
- `pytest` 全绿; Streamlit Compare/Judge 不回归; 规则 D 审阅 SHIP。
- **接阶段 3**: 把本 UI 经 launchd 经 8000 对外 (绑 0.0.0.0) + 加 login gate + 错误串 sanitize (DEPLOY_PLAN §3 + §7 待定项)。本计划全程 localhost, 不含鉴权。

## 自查 (writing-plans self-review)
- 规格覆盖: 流式端点 (Task1) / 静态托管 (Task2) / vendor 无 CDN (Task3) / 布局 (Task4) / 侧栏+localStorage+流式+来源+检索隐藏 (Task5) / 验证+规则D (Task6) —— DESIGN 各节均有对应任务。✓
- 占位扫描: 无 TBD/TODO; "实现注记" 是带回退方案的真实代码, 非占位。✓
- 类型一致: SSE 事件名 (sources/token/done/error) 后端发与前端 parseSSE 分支一致; localStorage key `sdtm_chat_v1` 全程一致; `mdToSafeHTML`/`highlightIn`/`messageEl`/`sourcesEl`/`streamAsk` 调用与定义一致。✓
