// ⚑ 归因探针: 在 node 里**真的跑** webchat/ 那套前端 (app.js 入口 + js/*.js), 驱动
// renderMessages → attachTools → flagButton → openFlag → postFlag 整条链, 抠出发给
// /api/flag 的请求体。
//
// 为什么不是静态扫源码: 这条缺陷的形状正是"链路上某一环没把数据传下去", 而字面扫描
// 看不出 openFlag 有没有把 msgObj 传给 postFlag。也不用浏览器 —— 浏览器对 /static/app.js
// 走启发式缓存, 改了文件不刷缓存就会出现"变异没生效却表现得像修好了"(终审踩过)。
// 本探针每个场景都从磁盘**重新拷一份再 import**, 没有这层。
//
// ⚠ 2026-09-08 前端拆成 ES 模块后, 原来的 `vm.runInContext(app.js)` 走不通了 (源码里有
// import/export, 而 vm 的模块加载器至今 experimental)。改成: stub 装进真 globalThis,
// 再 `await import()` 那份副本。三件事跟着变, 都是**加载方式**的变化, 不是被测语义:
//   1. **每个场景一份新目录**: ESM 注册表按解析后的 URL 缓存, 同一路径只求值一次, 而
//      store.js 在**求值时**读 localStorage —— 不换路径的话第二个场景拿到的是第一个场景的
//      store。(只给 app.js 挂 `?v=N` 查询串不够: 它对 "./js/store.js" 的静态依赖不带查询,
//      那一层仍是同一份。)
//   2. app.js 不再往全局挂函数, `sandbox.send` / `sandbox.renderMessages` 没有了 ——
//      send 改走**真实 UI 路径** (填 #input → 触发 #composer 的 submit), renderMessages /
//      refreshModelBadgeLabels 从**同一份副本**的 js/render.js import (同一 URL ⇒ 同一实例,
//      与 app.js 共享同一个 store)。
//   3. `/api/info` 的 stub 应答**跨一次宏任务**才返回 (见 makeGlobals): `await import()`
//      本身会放跑若干微任务, 不隔一层的话 loadModelName 可能在 import 返回前就跑完,
//      "初次渲染那一版" (F-2) 就再也观测不到了。真实的网络往返本来就 ≥ 一个宏任务,
//      这一层让时序**更**贴近真实, 不是把闸放松。
//
// 输出: 一行 JSON, 每个场景一份 { flagBody, topbarText, badgeText, ... }。
import { mkdtempSync, mkdirSync, copyFileSync, readdirSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { fileURLToPath, pathToFileURL } from "node:url";
import { dirname, resolve, join } from "node:path";

// PROBE_WEBCHAT_DIR 让变异验证**在副本上**跑: webchat/ 是从工作树挂载且每请求现读, 直接变异
// 工作树里的模块意味着那几秒内用户刷新页面会拿到变异版。行为闸走副本即可 ——
// 只有静态闸 (读 Python 侧的 FLAG_JS / RENDER_JS 常量) 才必须动工作树。
const WEBCHAT = process.env.PROBE_WEBCHAT_DIR
  || resolve(dirname(fileURLToPath(import.meta.url)), "../../../webchat");

// /api/info 的模型表 —— 与 config.py 的 selectable_models 同形。topbar 会被 loadModelName
// 把 default_model 的尾段写进 #topbar-model 的 dataset, 这正是老实现拿去归因的那个串,
// 也是本探针用来区分"读对了没有"的诱饵。
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
    this.clientHeight = 0;
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
  // attachTools 的幂等守卫 (`if (tools.childElementCount) return`) 读它。缺了的话
  // undefined 恒 falsy ⇒ 守卫形同虚设, 重复挂 ⚑ 按钮也测不出来。
  get childElementCount() { return this.children.length; }
  appendChild(c) {
    c.parentNode = this;
    this.children.push(c);
    if (this.tagName === "select") this.options.push(c);
    return c;
  }
  append(...cs) { cs.forEach((c) => this.appendChild(c)); }
  prepend(c) { c.parentNode = this; this.children.unshift(c); return c; }
  remove() {
    if (!this.parentNode) return;
    const i = this.parentNode.children.indexOf(this);
    if (i >= 0) this.parentNode.children.splice(i, 1);
    this.parentNode = null;
  }
  get selectedOptions() { return this.options.filter((o) => o.value === this.value); }
  addEventListener(t, fn) { (this._listeners[t] ||= []).push(fn); }
  focus() {}
  // 支持 `.class` 与 `:scope > .class` (前端用到的全部形态); "pre code" 之类一律空集。
  // `:scope >` 只看直接子元素: render.js 用它把"本条消息的 .turn-meta"与别处的同名节点
  // 分开, 当成全树搜就会让 metaBox 拿到**上一条**消息的容器, 徽章挂错气泡。
  querySelectorAll(sel) {
    const scoped = sel.startsWith(":scope >");
    const s = (scoped ? sel.slice(":scope >".length) : sel).trim();
    if (!s.startsWith(".")) return [];
    const want = s.slice(1);
    const out = [];
    if (scoped) {
      this.children.forEach((c) => { if (c._classes.has(want)) out.push(c); });
      return out;
    }
    const walk = (n) => n.children.forEach((c) => { if (c._classes.has(want)) out.push(c); walk(c); });
    walk(this);
    return out;
  }
  querySelector(sel) { return this.querySelectorAll(sel)[0] || null; }
}

function findByClass(root, cls) {
  return root.querySelectorAll("." + cls)[0] || null;
}

const flush = () => new Promise((r) => setTimeout(r, 0));

function makeGlobals(flagBodies) {
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
    // initSettings() 往 document 上挂 click/keydown (点面板外/Esc 关闭)
    addEventListener() {},
  };
  const stored = new Map();
  return {
    document,
    localStorage: {
      getItem: (k) => (stored.has(k) ? stored.get(k) : null),
      setItem: (k, v) => stored.set(k, String(v)),
      removeItem: (k) => stored.delete(k),
    },
    DOMPurify: { sanitize: (s) => s },
    marked: { parse: (s) => s || "" },
    hljs: { highlightElement() {} },
    // 流式渲染的 rAF 节流 (app.js paint): node 没有这两个, 用宏任务代
    requestAnimationFrame: (fn) => setTimeout(fn, 0),
    cancelAnimationFrame: (id) => clearTimeout(id),
    async fetch(url, opts) {
      if (String(url).includes("/api/info")) {
        // ⚠ 跨一次宏任务 (见文件头注释 3): 真实网络往返本来如此, 而且这是
        // "初次渲染那一版" (F-2) 还能被观测到的前提。
        await flush();
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
}

// 每个场景一份磁盘副本 + 一次 import (理由见文件头注释 1)。返回同一份副本的 render.js
// 模块实例 —— app.js 与它共享 store, 与浏览器里的实际情形一致。
const tmpDirs = [];
async function loadApp(g) {
  const dir = mkdtempSync(join(tmpdir(), "webchat-probe-"));
  tmpDirs.push(dir);
  mkdirSync(join(dir, "js"));
  copyFileSync(join(WEBCHAT, "app.js"), join(dir, "app.js"));
  for (const f of readdirSync(join(WEBCHAT, "js"))) {
    copyFileSync(join(WEBCHAT, "js", f), join(dir, "js", f));
  }
  Object.assign(globalThis, g);
  let error = null;
  try {
    await import(pathToFileURL(join(dir, "app.js")).href);
  } catch (e) {
    error = String(e);   // 入口求值抛了 (renderMessages 死在首屏) —— 依赖模块本身仍可用
  }
  const render = await import(pathToFileURL(join(dir, "js", "render.js")).href);
  return { render, error };
}

// #topbar-model 的 dataset.defaultModel = /api/info 的 default_model 尾段, 也就是
// flagModelName 缺 modelId 时的回退源。诱饵断言读的就是它。
const topbarOf = (g) => g.__byId.get("topbar-model").dataset.defaultModel ?? null;
const badgeOf = (messages) =>
  (findByClass(messages, "model-meta") || { textContent: null }).textContent;

async function scenario({ modelId, modelsUsed, fellBack, verified = false }) {
  const flagBodies = [];
  const g = makeGlobals(flagBodies);
  const assistant = { role: "assistant", content: "捏造的答案", sources: [] };
  // verified 默认 false —— 既有两个场景 (withModelId / legacyNoModelId) 的行为逐位不变。
  // 可覆盖是为了造 verified===true 那一档: 琥珀色的**反方向**闸需要它 (终审 I-1)。
  if (modelId) { assistant.modelId = modelId; assistant.verified = verified; }
  // 显式 undefined 时**整个键都不设** —— 那正是老历史存档的样子 (spec §5 B2)。
  // ⚠ 不能写成 `assistant.modelsUsed = modelsUsed ?? undefined`: 那样键会存在且值为
  // undefined, 而老存档里这个键**根本不存在**, 两者在 `in` 判定与 JSON 往返上都不同。
  if (modelsUsed !== undefined) assistant.modelsUsed = modelsUsed;
  if (fellBack !== undefined) assistant.fellBack = fellBack;
  g.localStorage.setItem("sdtm_chat_v1", JSON.stringify({
    currentId: "c1",
    conversations: [{
      id: "c1", title: "t", createdAt: 1,
      messages: [{ role: "user", content: "AETERM?" }, assistant],
    }],
  }));

  const { error } = await loadApp(g);
  if (error) throw new Error(`app.js 求值抛了: ${error}`);

  // ⚠ **初次渲染那一版**必须单独抓 (F-2): 两次 flush 之后 refreshModelBadgeLabels() 会用
  // dataset 重写文案, 于是全套闸此前只观测到"刷新后"那一版。两版走的代码路径不同 ——
  // 初次渲染拿到的 fellBack 是**真的 undefined** (老后端/老存档的字面值), 而刷新那版
  // 是 dataset 三路比较后的 null。B1 降级要防的正是前者, 它此前从未被观测过。
  const badgeTextInitial = badgeOf(g.__byId.get("messages"));

  await flush(); await flush();          // loadModelName 的两段 await

  const messages = g.__byId.get("messages");
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
    topbarText: topbarOf(g),
    badgeText: badgeOf(messages),
    // 琥珀色 (`.unverified`) 是**独立于文案**的一路信号, 必须单独导出才能上闸 (终审 I-1):
    // 文案对但没颜色时, 四个可选模型里三个 verified=false 的琥珀是常态 ⇒ 唯独"真出事"
    // 那条长得像正常消息。
    badgeClass: (findByClass(messages, "model-meta") || { className: null }).className,
    badgeTextInitial,
  };
}

// F-1: `modelsUsed` 形状不对时 (后端发了字符串 / null / 对象 / 数字), 徽章必须**落回老文案
// 且不抛**, 且**整段历史渲染不中止**。现有 try/catch 只包了 JSON.parse, 没包 .join ——
// `.join is not a function` 抛在 renderMessages 里, 死的不是一条徽章而是整段历史。
async function badShapeScenario(modelsUsed) {
  const flagBodies = [];
  const g = makeGlobals(flagBodies);
  g.localStorage.setItem("sdtm_chat_v1", JSON.stringify({
    currentId: "c1",
    conversations: [{
      id: "c1", title: "t", createdAt: 1,
      messages: [{ role: "user", content: "AETERM?" },
                 { role: "assistant", content: "答案", sources: [],
                   modelId: "gpt-sol", verified: false, modelsUsed, fellBack: true }],
    }],
  }));
  const { error: renderError } = await loadApp(g);
  const messages = g.__byId.get("messages");
  // ⚠ 先抓徽章再驱动 ⚑: 下面的 `await` 会把 loadModelName 的微任务放跑,
  // label 表一到位 refreshModelBadgeLabels 就把文案从原始 id 改成 label ——
  // 抓晚了断言的就不再是"畸形形状下落回老文案", 而是"label 表加载完了没"。
  const badgeText = badgeOf(messages);

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
  const g = makeGlobals([]);
  g.localStorage.setItem("sdtm_chat_v1", JSON.stringify({
    currentId: "c1",
    conversations: [{
      id: "c1", title: "t", createdAt: 1,
      messages: [{ role: "user", content: "AETERM?" },
                 { role: "assistant", content: "答案", sources: [],
                   modelId: "gpt-sol", verified: false,
                   modelsUsed: ["deepseek-v4-pro"], fellBack: true }],
    }],
  }));
  const { render, error } = await loadApp(g);
  if (error) throw new Error(`app.js 求值抛了: ${error}`);
  await flush(); await flush();          // 先让 label 表到位, 与真实刷新时序一致
  const messages = g.__byId.get("messages");
  findByClass(messages, "model-meta").dataset.modelsUsed = "{不是合法 JSON";
  let refreshError = null;
  try {
    render.refreshModelBadgeLabels();
  } catch (e) {
    refreshError = String(e);
  }
  return { refreshError, badgeText: badgeOf(messages) };
}

// 走完整条 send() → streamAsk() → onDone() → persist() 链, 然后重建 DOM。
// 为什么必须这么测: 前面的场景都是**预置**历史再渲染, `persist` 有没有把新字段存下来
// 它们一个都看不见 —— 而"存档不诚实"正是本轮 R5 要防的事。
async function streamScenario(doneData) {
  const flagBodies = [];
  const g = makeGlobals(flagBodies);
  const frames =
    `event: sources\ndata: {"sources":[],"routed_corpus":null}\n\n` +
    `event: token\ndata: {"text":"ok"}\n\n` +
    `event: done\ndata: ${JSON.stringify(doneData)}\n\n`;
  const baseFetch = g.fetch;
  g.fetch = async (url, opts) => {
    if (String(url).includes("/api/ask_stream")) {
      const bytes = new TextEncoder().encode(frames);
      let sent = false;
      return { ok: true, body: { getReader: () => ({
        read: async () => (sent ? { done: true } : ((sent = true), { value: bytes, done: false })),
      }) } };
    }
    return baseFetch(url, opts);
  };
  const { render, error } = await loadApp(g);
  if (error) throw new Error(`app.js 求值抛了: ${error}`);
  await flush(); await flush();
  g.__byId.get("model-select").value = "gpt-sol";

  // app.js 不再往全局挂 send() —— 走**真实 UI 路径**: 填输入框 + 触发 composer 的 submit。
  // 比原来直接调 send() 多覆盖一段接线, 少覆盖的一样也没有。
  g.__byId.get("input").value = "AETERM?";
  g.__byId.get("composer").onsubmit({ preventDefault() {} });
  // onsubmit 不 await send() (它是 async), 所以轮询到落盘为止 —— 整条链只靠微任务 +
  // setTimeout(0) 推进 (fetch stub / reader.read / rAF stub 都是), 不会卡真时间。
  const persisted = () => JSON.parse(g.localStorage.getItem("sdtm_chat_v1"))
    .conversations[0].messages.some((m) => m.role === "assistant");
  for (let i = 0; i < 200 && !persisted(); i++) await flush();
  if (!persisted()) throw new Error("send 链没跑完 — 存档里没有 assistant 消息");

  const stored = JSON.parse(g.localStorage.getItem("sdtm_chat_v1"));
  const last = stored.conversations[0].messages.at(-1);
  // 模拟刷新: 只从存档重建 (与 app.js 共享同一份 render.js 实例 ⇒ 同一个 store)
  render.renderMessages({ onPickExample() {}, onRetry() {} });
  const messages = g.__byId.get("messages");
  const btn = findByClass(messages, "flag-btn");
  if (!btn) throw new Error("没找到 ⚑ 按钮 — streamScenario 的驱动路径失效了");
  btn.onclick();
  const box = findByClass(messages, "flag-box");
  box.children.find((c) => c.tagName === "textarea").value = "答案是捏造的";
  await findByClass(box.parentNode, "flag-send").onclick();

  return { stored: last, badgeAfterReload: badgeOf(messages), flagBody: flagBodies[0] };
}

// ⚠ 前两条**一字不动** —— 它们是终审 C-1 (⚑ 归错模型) 的既有闸。
// withModelId 同时兼任 spec §5 B1/B2 的降级场景: 它的历史记录里**没有** modelsUsed/fellBack
// 两个键, 正是"新前端 + 老后端"与"新前端 + 老存档"的形状。
const out = {
  withModelId: await scenario({ modelId: "gpt-sol" }),
  legacyNoModelId: await scenario({ modelId: null }),
  verifiedTrue: await scenario({ modelId: "opus-5", verified: true }),
  // ⚠ verified=true **且**回退 —— opus-5 是四个里唯一 verified:true 的, 又是下拉第一项,
  // 所以"用户停在 Opus 5 → Bedrock 挂 → DeepSeek 答"是最可能真实发生的那一次回退,
  // 而它的琥珀色恰好落在此前没闸的那一格 (终审第 2 轮 N-1)。
  fellBackVerified: await scenario({ modelId: "opus-5", verified: true, fellBack: true,
                                     modelsUsed: ["deepseek-v4-pro"] }),
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
for (const d of tmpDirs) rmSync(d, { recursive: true, force: true });
process.stdout.write(JSON.stringify(out));
