// SDTM chat UI — 单模型 (DeepSeek V4 Pro) 流式聊天, 多对话存 localStorage。
const LS_KEY = "sdtm_chat_v1";
const HISTORY_TURNS = 10; // 控 token: 发给后端的最近消息条数

// uid 不用 crypto.randomUUID (LAN http 非安全上下文不可用)
const uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 8);

let store = load();

function load() {
  try {
    const s = JSON.parse(localStorage.getItem(LS_KEY));
    if (s && Array.isArray(s.conversations)) return s;
  } catch (_) {}
  return { conversations: [], currentId: null };
}
function save() {
  try {
    localStorage.setItem(LS_KEY, JSON.stringify(store));
  } catch (_) {
    // QuotaExceededError: store is newest-first (unshift), so evict the oldest conversations
    // until it fits — never let a storage failure throw into a stream callback (would lose the
    // just-generated answer and, before the try/finally below, brick the send button).
    while (store.conversations.length > 1) {
      store.conversations.pop();
      try { localStorage.setItem(LS_KEY, JSON.stringify(store)); return; } catch (_) {}
    }
  }
}

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

async function streamAsk(question, history, { onSources, onToken, onDone, onError, onClose, onAbort, signal }) {
  let resp;
  try {
    resp = await fetch("/api/ask_stream", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, history }), signal,
    });
  } catch (e) {
    if (signal?.aborted) { onAbort?.(); return; }
    onError("无法连接服务"); return;
  }
  if (!resp.ok) { onError(`服务错误 ${resp.status}`); return; }
  const reader = resp.body.getReader();
  const dec = new TextDecoder();
  let buf = "";
  let terminal = false; // saw a done/error frame
  const dispatch = (ev) => {
    if (!ev) return;
    if (ev.event === "sources") onSources(ev.data.sources || []);
    else if (ev.event === "token") onToken(ev.data.text || "");
    else if (ev.event === "done") { terminal = true; onDone(ev.data || {}); }
    else if (ev.event === "error") { terminal = true; onError(ev.data.message || "生成失败"); }
  };
  try {
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      buf += dec.decode(value, { stream: true });
      let i;
      while ((i = buf.indexOf("\n\n")) !== -1) {
        dispatch(parseSSE(buf.slice(0, i)));
        buf = buf.slice(i + 2);
      }
    }
  } catch (e) {
    // User hit Stop -> AbortError on the pending read. Treat as a clean stop (keep partial).
    if (signal?.aborted) { onAbort?.(); return; }
    onError("连接中断"); return; // genuine network drop mid-stream
  }
  // A terminal frame cut exactly at EOF (no trailing \n\n) would otherwise be lost.
  if (!terminal && buf.trim()) dispatch(parseSSE(buf));
  // Clean TCP close with NO done/error frame (worker killed mid-stream, reverse-proxy
  // idle-timeout in 阶段3, generator died before the done yield): neither onDone nor onError
  // fired — without this the streamed answer is on screen but never persisted (lost on reload).
  if (!terminal && onClose) onClose();
}

// ── 发送 / 停止 / 重试 ──
let busy = false;
let currentAbort = null; // AbortController for the in-flight stream

function setSending(on) {
  const b = $("send");
  b.textContent = on ? "停止" : "发送";
  b.classList.toggle("stop", on);
  b.disabled = false; // stay clickable while streaming so it can Stop
}
function stop() { if (currentAbort) currentAbort.abort(); }

async function send(text) {
  if (busy || !text.trim()) return;
  const c = current();
  c.messages.push({ role: "user", content: text });
  if (c.messages.length === 1) c.title = text.slice(0, 30);
  save(); renderSidebar(); renderMessages();
  await runGeneration(c);
}

// Re-run generation for the conversation's last user message (drops any failed/partial
// assistant turn first), without appending a duplicate user message.
function retry(c) {
  if (busy) return;
  while (c.messages.length && c.messages[c.messages.length - 1].role === "assistant") {
    c.messages.pop();
  }
  save(); renderMessages();
  if (c.messages.some((m) => m.role === "user")) runGeneration(c);
}

async function runGeneration(c) {
  const lastUserIdx = c.messages.map((m) => m.role).lastIndexOf("user");
  if (lastUserIdx === -1) return;
  const text = c.messages[lastUserIdx].content;
  busy = true; setSending(true);

  const box = $("messages");
  const holder = messageEl("assistant", "", null);
  box.appendChild(holder); box.scrollTop = box.scrollHeight;
  const bubble = holder.querySelector(".bubble");

  // History = everything BEFORE the current question (excludes the last user msg), capped.
  const history = c.messages.slice(0, lastUserIdx)
    .filter((m) => m.role === "user" || m.role === "assistant")
    .slice(-HISTORY_TURNS)
    .map((m) => ({ role: m.role, content: m.content }));

  let acc = "";
  let gotSources = null;
  let saved = false;
  const renderFinal = (content) => { bubble.innerHTML = mdToSafeHTML(content); highlightIn(bubble); };
  const persist = (content) => {
    if (saved) return;
    saved = true;
    c.messages.push({ role: "assistant", content, sources: gotSources || [] });
    save(); renderSidebar();
  };
  const appendErr = (msg) => {
    const e = document.createElement("div"); e.className = "err"; e.textContent = "⚠ " + msg;
    bubble.appendChild(e);
  };
  const appendRetry = () => {
    const btn = document.createElement("button");
    btn.className = "retry"; btn.textContent = "重试";
    btn.onclick = () => retry(c);
    holder.appendChild(btn);
  };

  const ctrl = new AbortController();
  currentAbort = ctrl;
  try {
    await streamAsk(text, history, {
      onSources: (s) => { gotSources = s; if (s.length) holder.appendChild(sourcesEl(s)); },
      // 流中只追加纯文本 (DESIGN §4: 避免每 token 重解析 markdown/重高亮, O(n^2) jank)。
      onToken: (t) => { acc += t; bubble.textContent = acc; box.scrollTop = box.scrollHeight; },
      // done 后整体渲染 markdown 一次; 空回答用占位 (DESIGN §6)。
      onDone: () => { const content = acc.trim() ? acc : "(无内容)"; renderFinal(content); persist(content); },
      onError: (msg) => { if (acc) { renderFinal(acc); persist(acc); } appendErr(msg); appendRetry(); },
      // 干净 EOF 但无 done/error: 内容已在屏上, 落盘防刷新丢失 (规则 D HIGH 修复)。
      onClose: () => { if (acc) { renderFinal(acc); persist(acc); appendErr("连接中断（已保留已生成内容）"); } else appendErr("连接中断"); appendRetry(); },
      // 用户点「停止」: 保留已生成部分, 不报错样式, 给重试入口。
      onAbort: () => { if (acc) { renderFinal(acc); persist(acc); } appendErr("已停止"); appendRetry(); },
      signal: ctrl.signal,
    });
  } finally {
    busy = false; setSending(false); currentAbort = null;
  }
}

// ── topbar: 显示后端真实 default_model (读 /api/info) ──
async function loadModelName() {
  try {
    const r = await fetch("/api/info");
    if (!r.ok) return; // not logged in / info unavailable -> keep static label
    const info = await r.json();
    const m = (info.default_model || "").split("/").pop();
    if (m) $("topbar").textContent = "SDTM 知识库助手 · " + m;
  } catch (_) {}
}

// ── 事件绑定 ──
$("new-chat").onclick = () => { newConversation(); renderSidebar(); renderMessages(); $("input").focus(); };
$("composer").onsubmit = (e) => {
  e.preventDefault();
  if (busy) { stop(); return; } // button is in "停止" mode while streaming
  const v = $("input").value; $("input").value = ""; $("input").style.height = "auto"; send(v);
};
$("input").addEventListener("keydown", (e) => {
  // IME 组字中 (中文拼音/日文假名等) 的回车是「上屏候选/确认」, 不能当发送。
  // isComposing 覆盖现代浏览器; keyCode===229 是组字态的传统兜底 (个别浏览器不置 isComposing)。
  if (e.key === "Enter" && !e.shiftKey && !e.isComposing && e.keyCode !== 229) {
    e.preventDefault();
    if (busy) return; // 生成中不用 Enter 触发停止 (避免误触); 停止请点按钮
    $("composer").requestSubmit();
  }
});
$("input").addEventListener("input", (e) => { e.target.style.height = "auto"; e.target.style.height = e.target.scrollHeight + "px"; });

// ── 启动 ──
if (!store.conversations.length) newConversation();
renderSidebar();
renderMessages();
loadModelName();
