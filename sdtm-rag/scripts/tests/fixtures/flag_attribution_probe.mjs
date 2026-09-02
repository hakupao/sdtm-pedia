// ⚑ 归因探针: 在 node 里**真的跑** webchat/app.js, 驱动 renderMessages → attachFlag →
// openFlag → postFlag 整条链, 抠出发给 /api/flag 的请求体。
//
// 为什么不是静态扫源码: 这条缺陷的形状正是"链路上某一环没把数据传下去", 而字面扫描
// 看不出 openFlag 有没有把 msgObj 传给 postFlag。也不用浏览器 —— 浏览器对 /static/app.js
// 走启发式缓存, 改了文件不刷缓存就会出现"变异没生效却表现得像修好了"(终审踩过)。
// vm 每次从磁盘重读, 没有这层。
//
// 输出: 一行 JSON, 两个场景各一份 { flagBody, topbarText, badgeText }。
import { readFileSync } from "node:fs";
import { createContext, runInContext } from "node:vm";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";

// PROBE_APP_JS 让变异验证**在副本上**跑: webchat/ 是从工作树挂载且每请求现读, 直接变异
// 工作树里的 app.js 意味着那几秒内用户刷新页面会拿到变异版。行为闸走副本即可 ——
// 只有静态闸 (读 Python 侧的 APP_JS 常量) 才必须动工作树。
const APP_JS = process.env.PROBE_APP_JS
  || resolve(dirname(fileURLToPath(import.meta.url)), "../../../webchat/app.js");

// /api/info 的模型表 —— 与 config.py 的 selectable_models 同形。topbar 会被 loadModelName
// 写成 "… · global.anthropic.claude-opus-5" (default_model 的尾段), 这正是老实现拿去
// 归因的那个串, 也是本探针用来区分"读对了没有"的诱饵。
const INFO = {
  default_model: "bedrock/converse/global.anthropic.claude-opus-5",
  federation: true,
  selectable_models: [
    { id: "opus-5", label: "Claude Opus 5", verified: true },
    { id: "gpt-sol", label: "GPT-5.6 Sol", verified: false },
  ],
};

// ── 最小 DOM ──────────────────────────────────────────────────────────────
class El {
  constructor(tag) {
    this.tagName = tag;
    this.children = [];
    this.parentNode = null;
    this._text = "";
    this._html = "";
    this._classes = new Set();
    this.dataset = {};
    this.style = {};
    this.hidden = false;
    this.disabled = false;
    this.value = "";
    this.options = [];
    this._listeners = {};
    this.scrollTop = 0;
    this.scrollHeight = 0;
    const self = this;
    this.classList = {
      add: (c) => self._classes.add(c),
      remove: (c) => self._classes.delete(c),
      contains: (c) => self._classes.has(c),
      // setSending() 用 toggle(cls, force) —— 只有走完整条 send() 的场景才碰得到,
      // 预置历史的场景走不到, 所以此前一直没暴露出缺这个方法。
      toggle: (c, force) => {
        const on = force === undefined ? !self._classes.has(c) : !!force;
        if (on) self._classes.add(c); else self._classes.delete(c);
        return on;
      },
    };
  }
  get className() { return [...this._classes].join(" "); }
  set className(v) { this._classes = new Set(String(v).split(/\s+/).filter(Boolean)); }
  get innerHTML() { return this._html; }
  set innerHTML(v) { this._html = v; this.children = []; }
  get textContent() {
    return this._text || this.children.map((c) => c.textContent).join("");
  }
  set textContent(v) { this._text = String(v); this.children = []; }
  appendChild(c) {
    c.parentNode = this;
    this.children.push(c);
    if (this.tagName === "select") this.options.push(c);
    return c;
  }
  append(...cs) { cs.forEach((c) => this.appendChild(c)); }
  remove() {
    if (!this.parentNode) return;
    const i = this.parentNode.children.indexOf(this);
    if (i >= 0) this.parentNode.children.splice(i, 1);
    this.parentNode = null;
  }
  get selectedOptions() { return this.options.filter((o) => o.value === this.value); }
  addEventListener(t, fn) { (this._listeners[t] ||= []).push(fn); }
  focus() {}
  // 只支持 `.class` (app.js 用到的全部形态); "pre code" 之类一律空集。
  querySelectorAll(sel) {
    if (!sel.startsWith(".")) return [];
    const want = sel.slice(1);
    const out = [];
    const walk = (n) => n.children.forEach((c) => { if (c._classes.has(want)) out.push(c); walk(c); });
    walk(this);
    return out;
  }
  querySelector(sel) { return this.querySelectorAll(sel)[0] || null; }
}

function findByClass(root, cls) {
  return root.querySelectorAll("." + cls)[0] || null;
}

function makeSandbox(flagBodies) {
  const byId = new Map();
  const root = new El("body");
  const document = {
    getElementById(id) {
      if (!byId.has(id)) {
        const el = new El(id === "model-select" ? "select" : "div");
        byId.set(id, el);
        root.appendChild(el);
      }
      return byId.get(id);
    },
    createElement: (tag) => new El(tag),
    querySelectorAll: (sel) => root.querySelectorAll(sel),
  };
  const stored = new Map();
  const sandbox = {
    document,
    localStorage: {
      getItem: (k) => (stored.has(k) ? stored.get(k) : null),
      setItem: (k, v) => stored.set(k, String(v)),
      removeItem: (k) => stored.delete(k),
    },
    DOMPurify: { sanitize: (s) => s },
    marked: { parse: (s) => s || "" },
    hljs: { highlightElement() {} },
    AbortController,
    TextDecoder,
    TextEncoder,        // vm sandbox 默认没有 (spec §3 P5 实测), 造 SSE 字节流喂 getReader 要用
    console,
    setTimeout,
    async fetch(url, opts) {
      if (String(url).includes("/api/info")) {
        return { ok: true, json: async () => INFO };
      }
      if (String(url).includes("/api/flag")) {
        flagBodies.push(JSON.parse(opts.body));
        return { ok: true };
      }
      return { ok: false };
    },
    __root: root,
    __byId: byId,
  };
  sandbox.globalThis = sandbox;
  return sandbox;
}

const flush = () => new Promise((r) => setTimeout(r, 0));

async function scenario({ modelId, modelsUsed, fellBack }) {
  const flagBodies = [];
  const sandbox = makeSandbox(flagBodies);
  const ctx = createContext(sandbox);
  const assistant = { role: "assistant", content: "捏造的答案", sources: [] };
  if (modelId) { assistant.modelId = modelId; assistant.verified = false; }
  // 显式 undefined 时**整个键都不设** —— 那正是老历史存档的样子 (spec §5 B2)。
  // ⚠ 不能写成 `assistant.modelsUsed = modelsUsed ?? undefined`: 那样键会存在且值为
  // undefined, 而老存档里这个键**根本不存在**, 两者在 `in` 判定与 JSON 往返上都不同。
  if (modelsUsed !== undefined) assistant.modelsUsed = modelsUsed;
  if (fellBack !== undefined) assistant.fellBack = fellBack;
  sandbox.localStorage.setItem("sdtm_chat_v1", JSON.stringify({
    currentId: "c1",
    conversations: [{
      id: "c1", title: "t", createdAt: 1,
      messages: [{ role: "user", content: "AETERM?" }, assistant],
    }],
  }));

  runInContext(readFileSync(APP_JS, "utf8"), ctx, { filename: APP_JS });

  // ⚠ **初次渲染那一版**必须单独抓 (F-2): 两次 flush 之后 refreshModelBadgeLabels() 会用
  // dataset 重写文案, 于是全套闸此前只观测到"刷新后"那一版。两版走的代码路径不同 ——
  // 初次渲染拿到的 fellBack 是**真的 undefined** (老后端/老存档的字面值), 而刷新那版
  // 是 dataset 三路比较后的 null。B1 降级要防的正是前者, 它此前从未被观测过。
  const messagesEarly = sandbox.__byId.get("messages");
  const badgeTextInitial =
    (findByClass(messagesEarly, "model-meta") || { textContent: null }).textContent;

  await flush(); await flush();          // loadModelName 的两段 await

  const messages = sandbox.__byId.get("messages");
  const btn = findByClass(messages, "flag-btn");
  if (!btn) throw new Error("没找到 ⚑ 按钮 — 探针的驱动路径失效了");
  btn.onclick();
  const box = findByClass(messages, "flag-box");
  const ta = box.children.find((c) => c.tagName === "textarea");
  ta.value = "答案是捏造的";
  await findByClass(box.parentNode, "flag-send").onclick();

  if (flagBodies.length !== 1) throw new Error(`/api/flag 调用次数 = ${flagBodies.length}`);
  return {
    flagBody: flagBodies[0],
    topbarText: sandbox.__byId.get("topbar-title").textContent,
    badgeText: (findByClass(messages, "model-meta") || { textContent: null }).textContent,
    badgeTextInitial,
  };
}

// F-1: `modelsUsed` 形状不对时 (后端发了字符串 / null / 对象 / 数字), 徽章必须**落回老文案
// 且不抛**, 且**整段历史渲染不中止**。现有 try/catch 只包了 JSON.parse, 没包 .join ——
// `.join is not a function` 抛在 renderMessages 里, 死的不是一条徽章而是整段历史。
// 今天不可达 (onDone 还没接通这两个字段), 但接通它的正是同一个 commit。
async function badShapeScenario(modelsUsed) {
  const flagBodies = [];
  const sandbox = makeSandbox(flagBodies);
  const ctx = createContext(sandbox);
  sandbox.localStorage.setItem("sdtm_chat_v1", JSON.stringify({
    currentId: "c1",
    conversations: [{
      id: "c1", title: "t", createdAt: 1,
      messages: [{ role: "user", content: "AETERM?" },
                 { role: "assistant", content: "答案", sources: [],
                   modelId: "gpt-sol", verified: false, modelsUsed, fellBack: true }],
    }],
  }));
  let renderError = null;
  try {
    runInContext(readFileSync(APP_JS, "utf8"), ctx, { filename: APP_JS });
  } catch (e) {
    renderError = String(e);
  }
  const messages = sandbox.__byId.get("messages");
  // ⚠ 先抓徽章再驱动 ⚑: 下面的 `await` 会把 loadModelName 的微任务放跑,
  // label 表一到位 refreshModelBadgeLabels 就把文案从原始 id 改成 label ——
  // 抓晚了断言的就不再是"畸形形状下落回老文案", 而是"label 表加载完了没"。
  const badgeText =
    (findByClass(messages, "model-meta") || { textContent: null }).textContent;

  // 也驱动一次 ⚑ (I-5): 护栏加在 flagModelName 那处同样必须有闸。那里抛的话异常穿过
  // postFlag ⇒ **用户点了 ⚑ 却什么都没记下**, 而 dogfood_failures.md 是 append-only 的
  // 优先级 backlog (规则 B)。"归错模型"至少还留下一条错记录; 这个是**连记录都没有**,
  // 且用户以为记上了 —— 比徽章那处更贴本轮主题。
  let flagError = null;
  try {
    const btn = findByClass(messages, "flag-btn");
    if (btn) {
      btn.onclick();
      const box = findByClass(messages, "flag-box");
      box.children.find((c) => c.tagName === "textarea").value = "答案是捏造的";
      await findByClass(box.parentNode, "flag-send").onclick();
    }
  } catch (e) {
    flagError = String(e);
  }

  return {
    renderError,
    renderedCount: messages.children.length,     // 2 条消息都画出来 = 渲染没中止
    badgeText,
    flagError,
    flagBody: flagBodies.length ? flagBodies[0] : null,
  };
}

// F-3: refreshModelBadgeLabels 里 JSON.parse 的 try/catch 在做事, 但此前无人钉。
// 直接把 dataset 弄脏再驱动它 —— 该 try/catch 的契约就是"坏数据不该让整条历史渲染崩掉"。
async function corruptDatasetScenario() {
  const sandbox = makeSandbox([]);
  const ctx = createContext(sandbox);
  sandbox.localStorage.setItem("sdtm_chat_v1", JSON.stringify({
    currentId: "c1",
    conversations: [{
      id: "c1", title: "t", createdAt: 1,
      messages: [{ role: "user", content: "AETERM?" },
                 { role: "assistant", content: "答案", sources: [],
                   modelId: "gpt-sol", verified: false,
                   modelsUsed: ["deepseek-v4-pro"], fellBack: true }],
    }],
  }));
  runInContext(readFileSync(APP_JS, "utf8"), ctx, { filename: APP_JS });
  await flush(); await flush();          // 先让 label 表到位, 与真实刷新时序一致
  const messages = sandbox.__byId.get("messages");
  findByClass(messages, "model-meta").dataset.modelsUsed = "{不是合法 JSON";
  let refreshError = null;
  try {
    runInContext("refreshModelBadgeLabels()", ctx);
  } catch (e) {
    refreshError = String(e);
  }
  return {
    refreshError,
    badgeText: (findByClass(messages, "model-meta") || { textContent: null }).textContent,
  };
}

// 走完整条 send() → streamAsk() → onDone() → persist() 链, 然后从 localStorage 重建 DOM。
// 为什么必须这么测: 前面的场景都是**预置**历史再渲染, `persist` 有没有把新字段存下来
// 它们一个都看不见 —— 而"存档不诚实"正是本轮 R5 要防的事。
async function streamScenario(doneData) {
  const flagBodies = [];
  const sandbox = makeSandbox(flagBodies);
  const frames =
    `event: sources\ndata: {"sources":[],"routed_corpus":null}\n\n` +
    `event: token\ndata: {"text":"ok"}\n\n` +
    `event: done\ndata: ${JSON.stringify(doneData)}\n\n`;
  const baseFetch = sandbox.fetch;
  sandbox.fetch = async (url, opts) => {
    if (String(url).includes("/api/ask_stream")) {
      const bytes = new TextEncoder().encode(frames);
      let sent = false;
      return { ok: true, body: { getReader: () => ({
        read: async () => (sent ? { done: true } : ((sent = true), { value: bytes, done: false })),
      }) } };
    }
    return baseFetch(url, opts);
  };
  const ctx = createContext(sandbox);
  runInContext(readFileSync(APP_JS, "utf8"), ctx, { filename: APP_JS });
  await flush(); await flush();
  sandbox.__byId.get("model-select").value = "gpt-sol";
  await sandbox.send("AETERM?");

  const stored = JSON.parse(sandbox.localStorage.getItem("sdtm_chat_v1"));
  const last = stored.conversations[0].messages.at(-1);
  sandbox.renderMessages();                       // 模拟刷新: 只从存档重建
  const messages = sandbox.__byId.get("messages");
  const btn = findByClass(messages, "flag-btn");
  if (!btn) throw new Error("没找到 ⚑ 按钮 — streamScenario 的驱动路径失效了");
  btn.onclick();
  const box = findByClass(messages, "flag-box");
  box.children.find((c) => c.tagName === "textarea").value = "答案是捏造的";
  await findByClass(box.parentNode, "flag-send").onclick();

  return {
    stored: last,
    badgeAfterReload: (findByClass(messages, "model-meta") || { textContent: null }).textContent,
    flagBody: flagBodies[0],
  };
}

// ⚠ 前两条**一字不动** —— 它们是终审 C-1 (⚑ 归错模型) 的既有闸。
// withModelId 同时兼任 spec §5 B1/B2 的降级场景: 它的历史记录里**没有** modelsUsed/fellBack
// 两个键, 正是"新前端 + 老后端"与"新前端 + 老存档"的形状。
const out = {
  withModelId: await scenario({ modelId: "gpt-sol" }),
  legacyNoModelId: await scenario({ modelId: null }),
  fellBack: await scenario({ modelId: "gpt-sol", modelsUsed: ["deepseek-v4-pro"], fellBack: true }),
  fellBackMulti: await scenario({ modelId: "gpt-sol", fellBack: true,
                                  modelsUsed: ["deepseek-v4-pro", "global.openai.gpt-5.6-sol"] }),
  notFellBack: await scenario({ modelId: "gpt-sol", fellBack: false,
                                modelsUsed: ["global.openai.gpt-5.6-sol"] }),
  badShapeString: await badShapeScenario("deepseek-v4-pro"),   // 后端发了裸串而非列表
  badShapeObject: await badShapeScenario({ 0: "x", length: 1 }),  // array-like, 没有 .join
  corruptDataset: await corruptDatasetScenario(),
  streamFellBack: await streamScenario({ model_id: "gpt-sol", verified: false,
                                         model_used: "deepseek-v4-pro",
                                         models_used: ["deepseek-v4-pro"], fell_back: true,
                                         web_status: "off", web_searches_ok: 0 }),
  streamNoFallback: await streamScenario({ model_id: "gpt-sol", verified: false,
                                           model_used: "global.openai.gpt-5.6-sol",
                                           models_used: ["global.openai.gpt-5.6-sol"],
                                           fell_back: false,
                                           web_status: "off", web_searches_ok: 0 }),
  // spec §5 B1 在**存档层**的形状: done 事件里压根没有 models_used / fell_back 两个键
  // (新前端已上线、Python 侧还没重启)。上面两条都发了显式值, 看不见"缺失"与"false"的差别。
  streamOldBackend: await streamScenario({ model_id: "gpt-sol", verified: false,
                                           model_used: "global.openai.gpt-5.6-sol",
                                           web_status: "off", web_searches_ok: 0 }),
};
process.stdout.write(JSON.stringify(out));
