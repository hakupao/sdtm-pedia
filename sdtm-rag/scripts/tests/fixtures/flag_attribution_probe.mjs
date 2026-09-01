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

const APP_JS = resolve(dirname(fileURLToPath(import.meta.url)), "../../../webchat/app.js");

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

async function scenario({ modelId }) {
  const flagBodies = [];
  const sandbox = makeSandbox(flagBodies);
  const ctx = createContext(sandbox);
  const assistant = { role: "assistant", content: "捏造的答案", sources: [] };
  if (modelId) { assistant.modelId = modelId; assistant.verified = false; }
  sandbox.localStorage.setItem("sdtm_chat_v1", JSON.stringify({
    currentId: "c1",
    conversations: [{
      id: "c1", title: "t", createdAt: 1,
      messages: [{ role: "user", content: "AETERM?" }, assistant],
    }],
  }));

  runInContext(readFileSync(APP_JS, "utf8"), ctx, { filename: APP_JS });
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
  };
}

const out = {
  withModelId: await scenario({ modelId: "gpt-sol" }),
  legacyNoModelId: await scenario({ modelId: null }),
};
process.stdout.write(JSON.stringify(out));
