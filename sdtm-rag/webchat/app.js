// SDTM chat UI — 单模型 (DeepSeek V4 Pro) 流式聊天, 多对话存 localStorage。
const LS_KEY = "sdtm_chat_v1";
const HISTORY_TURNS = 10; // 控 token: 发给后端的最近消息条数
// Plan B 联邦: 库标签 (日文 UI)。map 里没有的值 (null / 未知) 一律不渲染徽章 —— 联邦关时零变化。
const CORPUS_LABEL = { cdisc: "標準", study: "本研究", both: "両方" };
// 模型 id → label 表, loadModelName() 拿到 /api/info 后填。页面刚打开、表还是空的时候历史
// 徽章会退化显示原始 id (不影响正确性), loadModelName 填完表后会重渲染一次消息列表补上。
let modelLabelById = {};

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
  let lastUserQ = "";
  for (const m of c.messages) {
    const el = messageEl(m.role, m.content, m.sources, m.routedCorpus, m.webStatus, m.webSearchesOk,
                          m.modelId, m.verified);
    if (m.role === "user") lastUserQ = m.content;
    else if (m.role === "assistant") attachFlag(el, lastUserQ, m);
    box.appendChild(el);
  }
  box.scrollTop = box.scrollHeight;
}

function messageEl(role, content, sources, routedCorpus, webStatus, webSearchesOk, modelId, verified) {
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
  const meta = metaEl(routedCorpus);
  if (meta) wrap.appendChild(meta);
  if (sources && sources.length) wrap.appendChild(sourcesEl(sources));
  // 刷新/切会话后复原联网状态。不复原的话, 一个"已降级为未联网"的 KB-only 答案
  // 和正常联网答案长得一模一样 (spec §7 点名的最骗人的失败模式)。
  renderWebStatus(wrap, webStatus, webSearchesOk);
  // 同一个坑, spec §6: 只做 UI 标注(下拉旁边那行提示)的话, 对话存下来后这条信息就没了。
  renderModelBadge(wrap, role, modelId, verified);
  return wrap;
}

// 答案实际用的模型 (spec §6 产物自证)。modelId 为空 (生成中占位 / 未流完就中断 / 旧历史
// 记录没存这个字段) 时什么都不画 —— 比瞎猜一个模型名更诚实, 也避免占位阶段先画一个"未知"
// 徽章、done 后又叠一个真实徽章的重复渲染。
function renderModelBadge(wrap, role, modelId, verified) {
  if (role !== "assistant" || !modelId) return;
  const b = document.createElement("div");
  b.className = "msg-meta model-meta";
  const label = modelLabelById[modelId] || modelId;
  // verified 三态不可混同 (spec §6): true 正常; false 是拿到确证的"验过且不通过";
  // null (default 组不在 selectable_models 里, 没有 verified 概念) 一律显"未知",
  // 绝不能落进 false 那支 (会把"没这个概念"误报成"验过且不通过")。
  if (verified === true) b.textContent = `模型: ${label}`;
  else if (verified === false) { b.textContent = `模型: ${label} ⚠未验证`; b.classList.add("unverified"); }
  else b.textContent = `模型: ${label} · 验证状态未知`;
  wrap.appendChild(b);
}

// 答案元信息行: 联邦实际检索了哪个库 (routed_corpus)。联邦关时后端返 null → 不渲染。
function metaEl(routedCorpus) {
  const label = CORPUS_LABEL[routedCorpus];
  if (!label) return null;
  const d = document.createElement("div");
  d.className = "msg-meta";
  d.textContent = `判定: ${label}`;
  return d;
}

// 每条来源前缀的库徽章; src.corpus 为空/未知 (单库路径) 时返 null, 来源行与联邦前一致。
function corpusBadge(corpus) {
  const label = CORPUS_LABEL[corpus];
  if (!label) return null;
  const b = document.createElement("span");
  // class 只从白名单取, 不拼服务端字符串
  b.className = corpus === "study" ? "corpus-badge study" : "corpus-badge";
  b.textContent = label;
  return b;
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
    // 注意: 取 span 必须在插徽章之前 —— 徽章也是 span, 插在最前会被 querySelector 抢走。
    div.querySelector("span").textContent = ` (sim ${(src.similarity ?? 0).toFixed(3)})`;
    const badge = corpusBadge(src.corpus);
    if (badge) div.insertBefore(badge, div.firstChild);
    const p = document.createElement("div");
    p.textContent = src.text_preview || "";
    div.appendChild(p);
    d.appendChild(div);
  }
  return d;
}

// 搜索过程条: 网页版那种「看得见它在搜什么」的观感。没有这层, 勾了联网只会
// 看到卡住半分钟然后蹦出一段话 —— 那是超时的感觉, 不是联网的感觉。
// ⚠ 挂在 holder (气泡外层) 而非 bubble: onToken 会 bubble.textContent=acc 覆盖气泡内容。
function ensureWebPanel(holder) {
  let p = holder.querySelector(":scope > .web-panel");
  if (!p) {
    p = document.createElement("div");
    p.className = "web-panel";
    holder.prepend(p);   // 搜索过程显示在答案上方
  }
  return p;
}

function onToolCallUI(holder, d) {
  const row = document.createElement("div");
  row.className = "web-row";
  row.dataset.callId = d.id || "";
  row.textContent = `🔍 搜索 "${d.query || ""}"`;
  ensureWebPanel(holder).appendChild(row);
}

function onToolResultUI(holder, d) {
  const p = ensureWebPanel(holder);
  // CSS.escape: tool id 来自模型返回, 不保证是合法选择器
  const sel = `.web-row[data-call-id="${CSS.escape(d.id || "")}"]`;
  const row = p.querySelector(sel);
  const note = document.createElement("span");
  note.className = "web-note";
  // tool_result.status 有 6 个值, 其中 bad_query/unknown_tool 是**模型**出错不是联网出错,
  // 措辞必须区分 —— 把模型的失误显示成"联网失败"会让人去查网络而不是查模型。
  note.textContent = {
    ok: ` — 找到 ${d.count} 个来源`,
    failed: " — 搜索失败",
    quota_exceeded: " — 已达搜索次数上限",
    disabled: " — 服务端未启用联网",
    bad_query: " — 跳过 (模型给出的查询无效)",
    unknown_tool: " — 跳过 (模型调用了不存在的工具)",
  }[d.status] || ` — ${d.status}`;
  (row || p).appendChild(note);
}

// web_status 落在 done 上: 勾了联网却静默降级是最骗人的失败模式, 必须显式说出来。
// ⚠ 契约以 Task 4 实现为准 (计划初稿只列了 3 个状态, 实测收口后是 6 个 + 一个计数):
//   web_status ∈ {ok, partial, failed, quota_exceeded, disabled, off}
//   web_searches_ok: int  —— 真正拿到结果的搜索次数 (bad_query/unknown_tool/quota/failed 不计)
// 三种"看起来正常其实没搜到"的情形必须分开说, 否则用户无从判断答案的成色。
function renderWebStatus(holder, status, searchesOk) {
  if (!status || status === "off") return;
  // ok + 0 次成功检索: 联网开着、一次网都没打成 (模型净吐畸形工具调用能耗光轮数)
  const msg = status === "ok"
    ? (searchesOk > 0 ? null : "ℹ 已开启联网, 但本次未实际检索到内容, 以下回答基于知识库")
    : {
        partial: "⚠ 部分搜索失败, 联网参考可能不完整 (逐条状态见上方搜索过程)",
        failed: "⚠ 本次未联网: 搜索请求失败, 以下回答仅基于知识库",
        quota_exceeded: "⚠ 本次未联网: 已达搜索配额上限, 以下回答仅基于知识库",
        disabled: "⚠ 本次未联网: 服务端未启用联网, 以下回答仅基于知识库",
      }[status] || `⚠ 本次未联网 (${status})`;
  if (!msg) return;
  const warn = document.createElement("div");
  warn.className = status === "ok" ? "web-note-block" : "web-warn";
  warn.textContent = msg;
  ensureWebPanel(holder).appendChild(warn);
}

// ── 失败捕获 (⚑ 标记答错/答弱 → POST /api/flag → dogfood_failures.md) ──
function attachFlag(wrap, question, msgObj) {
  const bar = document.createElement("div");
  bar.className = "msg-actions";
  const btn = document.createElement("button");
  btn.className = "flag-btn";
  if (msgObj && msgObj.flagged) {
    btn.textContent = "✓ 已记录"; btn.disabled = true; btn.classList.add("done");
  } else {
    btn.textContent = "⚑ 标记"; btn.onclick = () => openFlag(bar, btn, question, msgObj);
  }
  bar.appendChild(btn);
  wrap.appendChild(bar);
}

function openFlag(bar, btn, question, msgObj) {
  if (bar.querySelector(".flag-box")) return; // already open
  btn.style.display = "none";
  const box = document.createElement("div");
  box.className = "flag-box";
  const ta = document.createElement("textarea");
  ta.placeholder = "哪里答错/答弱? 期望是什么? (可留空)"; ta.rows = 2;
  const send = document.createElement("button"); send.textContent = "记录"; send.className = "flag-send";
  const cancel = document.createElement("button"); cancel.textContent = "取消"; cancel.className = "flag-cancel";
  cancel.onclick = () => { box.remove(); btn.style.display = ""; };
  send.onclick = async () => {
    send.disabled = true; cancel.disabled = true; send.textContent = "...";
    const ok = await postFlag(question, msgObj ? msgObj.content : "", ta.value);
    if (ok) {
      if (msgObj) { msgObj.flagged = true; save(); }
      box.remove();
      btn.textContent = "✓ 已记录"; btn.disabled = true; btn.classList.add("done"); btn.style.display = "";
    } else {
      send.disabled = false; cancel.disabled = false; send.textContent = "记录";
      if (!box.querySelector(".err")) {
        const e = document.createElement("span"); e.className = "err"; e.textContent = " 记录失败"; box.appendChild(e);
      }
    }
  };
  box.append(ta, send, cancel);
  bar.appendChild(box);
  ta.focus();
}

async function postFlag(question, answer, note) {
  const model = ($("topbar-title").textContent.split("·").pop() || "").trim() || null;
  try {
    const r = await fetch("/api/flag", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, answer, note, model }),
    });
    return r.ok;
  } catch (_) { return false; }
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

// 检索范围 checkbox → 后端 corpus 字面量 (auto|cdisc|study|both)。
// 两个都不勾 = auto: 交给 LLM 判库 (federation.decide_corpus), 与改 checkbox 前的默认行为一致。
function selectedCorpus() {
  const cdisc = $("scope-cdisc").checked, study = $("scope-study").checked;
  if (cdisc && study) return "both";
  if (cdisc) return "cdisc";
  if (study) return "study";
  return "auto";
}

// 联网是与 corpus 正交的第四维: 只决定挂不挂 web_search 工具, 不参与判库。
function webEnabled() { return $("scope-web").checked; }

async function streamAsk(question, history, { onSources, onToken, onToolCall, onToolResult, onDone, onError, onClose, onAbort, signal }) {
  let resp;
  try {
    const payload = { question, history, corpus: selectedCorpus(), web: webEnabled() };
    // spec §5 裁定: UI **永远发显式 id**, 绝不依赖默认值落到 default 组 ——
    // default 与 opus-5 今天都解析到 Opus 5, 但改 .env 的 default_model 会让二者静默分叉。
    // 下拉为空 (info 没加载出来) 时**整个字段省略**, 由服务端默认值接管, 而不是硬塞 "default"
    // ——「省略」与「显式传 default」在服务端是同一行为, 但省略不会在产物里留下一个
    // 用户根本没做过的选择。
    const chosen = $("model-select").value;
    if (chosen) payload.model = chosen;
    resp = await fetch("/api/ask_stream", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload), signal,
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
    if (ev.event === "sources") onSources(ev.data.sources || [], ev.data.routed_corpus || null);
    else if (ev.event === "token") onToken(ev.data.text || "");
    else if (ev.event === "tool_call") onToolCall?.(ev.data || {});
    else if (ev.event === "tool_result") onToolResult?.(ev.data || {});
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
  let gotRouted = null;
  let gotWebStatus = null;
  let gotWebSearchesOk = null;
  let gotModelId = null;
  let gotVerified = null;
  let saved = false;
  let savedMsg = null;
  const renderFinal = (content) => { bubble.innerHTML = mdToSafeHTML(content); highlightIn(bubble); };
  const persist = (content) => {
    if (saved) return;
    saved = true;
    savedMsg = { role: "assistant", content, sources: gotSources || [], routedCorpus: gotRouted,
                 webStatus: gotWebStatus, webSearchesOk: gotWebSearchesOk,
                 modelId: gotModelId, verified: gotVerified };
    c.messages.push(savedMsg);
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
      onSources: (s, routed) => {
        gotSources = s; gotRouted = routed;
        const meta = metaEl(routed);
        if (meta) holder.appendChild(meta);
        if (s.length) holder.appendChild(sourcesEl(s));
      },
      // 流中只追加纯文本 (DESIGN §4: 避免每 token 重解析 markdown/重高亮, O(n^2) jank)。
      onToken: (t) => { acc += t; bubble.textContent = acc; box.scrollTop = box.scrollHeight; },
      onToolCall: (d) => onToolCallUI(holder, d),
      onToolResult: (d) => onToolResultUI(holder, d),
      // done 后整体渲染 markdown 一次; 空回答用占位 (DESIGN §6)。
      onDone: (data) => {
        gotWebStatus = (data || {}).web_status; gotWebSearchesOk = (data || {}).web_searches_ok;
        // ?? 只在 null/undefined 时取右值, false 会原样保留 —— 与 renderModelBadge 的
        // 三态语义 (spec §6) 保持一致: verified 缺失时按"未知"收, 不会误当成 false。
        gotModelId = (data || {}).model_id ?? null;
        gotVerified = (data || {}).verified ?? null;
        renderWebStatus(holder, gotWebStatus, gotWebSearchesOk);
        renderModelBadge(holder, "assistant", gotModelId, gotVerified);
        const content = acc.trim() ? acc : "(无内容)"; renderFinal(content); persist(content);
      },
      onError: (msg) => { if (acc) { renderFinal(acc); persist(acc); } appendErr(msg); appendRetry(); },
      // 干净 EOF 但无 done/error: 内容已在屏上, 落盘防刷新丢失 (规则 D HIGH 修复)。
      onClose: () => { if (acc) { renderFinal(acc); persist(acc); appendErr("连接中断（已保留已生成内容）"); } else appendErr("连接中断"); appendRetry(); },
      // 用户点「停止」: 保留已生成部分, 不报错样式, 给重试入口。
      onAbort: () => { if (acc) { renderFinal(acc); persist(acc); } appendErr("已停止"); appendRetry(); },
      signal: ctrl.signal,
    });
  } finally {
    busy = false; setSending(false); currentAbort = null;
    // attach the ⚑ flag affordance once the answer is final + persisted (skip if nothing saved)
    if (savedMsg) attachFlag(holder, text, savedMsg);
  }
}

// ── topbar: 显示后端真实 default_model + 联邦开关 (读 /api/info) ──
async function loadModelName() {
  try {
    const r = await fetch("/api/info");
    if (!r.ok) return; // not logged in / info unavailable -> keep static label, 选择器保持隐藏
    const info = await r.json();
    const m = (info.default_model || "").split("/").pop();
    if (m) $("topbar-title").textContent = "SDTM 知识库助手 · " + m;
    // 联邦未构建时后端会静默忽略 corpus, 别留个无效控件在界面上
    $("scope").hidden = !info.federation;
    // 下拉从 /api/info 的模型表渲染 —— 与 Router 组同源, 故不可能提供后端没有的模型。
    const sel = $("model-select");
    (info.selectable_models || []).forEach((m) => {
      const o = document.createElement("option");
      o.value = m.id;
      // 未验证的在文字上标出来: 用户选之前就该看见, 而不是选完才知道
      o.textContent = m.verified ? m.label : `${m.label} ⚠未验证`;
      o.dataset.verified = String(m.verified);
      sel.appendChild(o);
      modelLabelById[m.id] = m.label; // 供 renderModelBadge 查表, 把历史消息里的原始 id 换成人话
    });
    // 刷新保留 —— 终审 I-E (联网状态过不了刷新) 的同款, 不重犯
    const saved = localStorage.getItem("sdtm_model");
    if (saved && [...sel.options].some((o) => o.value === saved)) sel.value = saved;
    const syncWarning = () => {
      const o = sel.selectedOptions[0];
      $("model-warning").hidden = !o || o.dataset.verified === "true";
    };
    sel.addEventListener("change", () => {
      localStorage.setItem("sdtm_model", sel.value);
      syncWarning();
    });
    syncWarning();
    // 首屏 renderMessages() 早于这个 fetch 落地, 历史消息的模型徽章当时只能显示原始 id;
    // 表填好后重画一遍补上人话 label (renderMessages 全量重建 #messages, 幂等, 代价可忽略)。
    renderMessages();
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
