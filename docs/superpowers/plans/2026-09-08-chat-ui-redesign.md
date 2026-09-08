# Chat UI 重构 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 `sdtm-rag/webchat/` 重做成克制专业型视觉, 流式期间实时渲染 Markdown, 正文出处默认隐藏 (设置开关可恢复), 并加复制/重命名/删除确认/空状态/回到底部五项 UX; 后端与存档格式零改动。

**Architecture:** 原生 ES modules 无构建: `app.js` 只做入口与生成流程编排, 逻辑拆到 `js/{store,citations,markdown,render,stream,flag,ui}.js`。流式渲染 = rAF 节流下每帧全量 `marked→DOMPurify`, 出处剥除是渲染层纯函数, 存档存原文。所有既往经审阅的护栏原样搬家 (spec §1)。

**Tech Stack:** 原生 JS (ES2022 modules) / CSS 变量 / vendored marked 12 + DOMPurify 3 + highlight.js 11 / `node --test` (node 26) / pytest + playwright (可选, 未装则 skip)。

**Spec:** `docs/superpowers/specs/2026-09-08-chat-ui-redesign-design.md`

## Global Constraints

- 工作目录: 所有路径相对 `sdtm-rag/` (仓库 `/Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag`)。git 命令在仓库根 `sdtm-pedia/` 下跑, 路径加 `sdtm-rag/` 前缀。
- 不改 `server/`、不改 prompt、不改 SSE 契约、不改 localStorage `sdtm_chat_v1` / `sdtm_model` 的结构。
- 不新增 vendored 库; 无外网字体 (系统栈)。
- spec §1 列出的护栏语义逐字保留: `modelBadgeText` 三态 + `fellBack === true` + `Array.isArray` (⛔ 不加 `filter(Boolean)`); `refreshModelBadgeLabels` 原地补字不重建; `flagModelName` 回退归因; `streamAsk` terminal/onClose/onAbort; `save()` 逐出; IME 回车保护; web 六态文案; `selectedCorpus` 四值; 下拉空则省略 `model`。搬家时**连注释一起搬**。
- 每个 task 结束: `cd sdtm-rag && node --test webchat/tests/` 与 `.venv/bin/python -m pytest scripts/tests/test_webchat_cache_headers.py -q` 必须绿。
- Commit 尾注: `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>` + `Claude-Session: https://claude.ai/code/session_01C4a1F9YeNoPs5DvaTP21vU`。红线 pre-commit 闸自动跑, CLEAN 才算过。
- 中文注释; UI 文案中文 (scope 三个勾选沿用现有日/中混排文案不改)。

---

## 文件结构

| 文件 | 责任 | 动作 |
|---|---|---|
| `webchat/js/citations.js` | `splitCitations(md,{show,streaming})` 纯函数 | 创建 (T1) |
| `webchat/tests/citations.test.mjs` | node --test | 创建 (T1) |
| `webchat/js/markdown.js` | `prepareStreaming` / `mdToSafeHTML` / `highlightIn` / `renderMarkdown` | 创建 (T2) |
| `webchat/tests/markdown.test.mjs` | node --test | 创建 (T2) |
| `webchat/js/store.js` | 会话存储 + 重命名 + `prefs` + `modelLabelById` | 创建 (T3) |
| `webchat/tests/store.test.mjs` | node --test (localStorage shim) | 创建 (T3) |
| `webchat/js/stream.js` | `parseSSE` / `streamAsk` (搬家, payload 由调用方给) | 创建 (T4) |
| `webchat/js/ui.js` | 复制 / 两步删除 / 行内重命名 / 滚动跟随 / 设置弹层 / 侧栏折叠 / `selectedCorpus` / `webEnabled` | 创建 (T5) |
| `webchat/js/flag.js` | ⚑ 标记 (搬家, 挂到工具条) | 创建 (T6) |
| `webchat/js/render.js` | 侧栏 / 消息 / chips / sources / web-panel / 空状态 / 徽章 | 创建 (T6) |
| `webchat/index.html` | 新骨架, `type=module` | 重写 (T7) |
| `webchat/style.css` | tokens + 全部样式 | 重写 (T7) |
| `webchat/app.js` | 入口: 事件绑定 + `runGeneration` + `loadModelName` | 重写 (T8) |
| `scripts/tests/test_webchat_stream_render.py` | playwright e2e (可选) | 创建 (T9) |
| `webchat/vendor/README.md` | 追加一段: 模块结构说明 | 修改 (T10) |

模块依赖 (无环): `app.js → {render, stream, store, ui, markdown, flag}`; `render → {store, markdown, flag, ui, citations(经 markdown)}`; `flag → store`; `markdown → citations`; `ui / store / citations / stream` 不 import 本地模块。

---

### Task 1: `citations.js` 出处抽取/剥除 (纯函数, TDD)

**Files:**
- Create: `webchat/js/citations.js`
- Test: `webchat/tests/citations.test.mjs`

**Interfaces:**
- Produces: `splitCitations(md: string, opts?: {show?: boolean, streaming?: boolean}) → { md: string, cites: Array<{kind: 'source'|'web', ref: string, raw: string}> }`
- `show=false` 剥除并整理空白; `show=true` 替换为 `<span class="cite cite-source">Source: path</span>` (inline HTML, CSS 负责独占一行); `streaming=true` 额外剥掉文本末尾未闭合的 `[Source:` / `[Web:` 半截 (含 `[`, `[S`, `**[Sou` 等前缀)。

- [ ] **Step 1: 写失败测试**

```js
// webchat/tests/citations.test.mjs
import test from "node:test";
import assert from "node:assert/strict";
import { splitCitations } from "../js/citations.js";

test("默认剥除 bold 出处并收敛空白", () => {
  const { md, cites } = splitCitations("AETERM is the term. **[Source: domains/AE.md]** Next.");
  assert.equal(md, "AETERM is the term. Next.");
  assert.deepEqual(cites, [{ kind: "source", ref: "domains/AE.md", raw: "**[Source: domains/AE.md]**" }]);
});

test("非 bold 形式与多处出处", () => {
  const { md, cites } = splitCitations("A [Source: x.md] and B [Source: y.md].");
  assert.equal(md, "A and B.");
  assert.deepEqual(cites.map((c) => c.ref), ["x.md", "y.md"]);
});

test("Web 引用同样处理, kind=web", () => {
  const { md, cites } = splitCitations("Practice. **[Web: https://a.b/c (retrieved 2026-09-01)]**");
  assert.equal(md, "Practice.");
  assert.deepEqual(cites, [{ kind: "web", ref: "https://a.b/c (retrieved 2026-09-01)",
                             raw: "**[Web: https://a.b/c (retrieved 2026-09-01)]**" }]);
});

test("剥除后留下的空括号与标点前空格清理", () => {
  const { md } = splitCitations("Use AESEV (**[Source: a.md]**) here , ok.");
  assert.equal(md, "Use AESEV here, ok.");
});

test("show 模式渲染为 span, ref 做 HTML 转义", () => {
  const { md } = splitCitations("Term. [Source: a<b>.md]", { show: true });
  assert.equal(md, 'Term. <span class="cite cite-source">Source: a&lt;b&gt;.md</span>');
});

test("streaming 剥掉尾部半截, 非 streaming 不动", () => {
  assert.equal(splitCitations("Text **[Source: dom", { streaming: true }).md, "Text");
  assert.equal(splitCitations("Text [S", { streaming: true }).md, "Text");
  assert.equal(splitCitations("Text [", { streaming: true }).md, "Text");
  assert.equal(splitCitations("Text [Sx", { streaming: true }).md, "Text [Sx");
  assert.equal(splitCitations("Text **[Source: dom").md, "Text **[Source: dom");
});

test("无出处文本原样返回 (含代码块缩进)", () => {
  const src = "```py\n    x = 1\n```\n\nline  two";
  assert.equal(splitCitations(src).md, src.replace("line  two", "line two"));
  assert.equal(splitCitations("no cite").cites.length, 0);
  assert.equal(splitCitations(null).md, "");
});
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && node --test webchat/tests/citations.test.mjs`
Expected: FAIL, `Cannot find module '../js/citations.js'`

- [ ] **Step 3: 实现**

```js
// webchat/js/citations.js
// 正文出处 `**[Source: path]**` / `[Web: url]` 的抽取与剥除。
// prompt (server/rag.py) 强制模型写这些标记, 是反捏造设计的一部分, 前端**不改 prompt**,
// 只在渲染层处理; 存档与 ⚑ 上报永远是原文 (spec §1)。
const RE_FULL = /\*{0,2}\[(Source|Web):\s*([^\]]*)\]\*{0,2}/g;
// 流中尾部半截: `[`, `[S`, `**[Sour`, `[Source: dom` ... 都先藏起来, 下一帧闭合后走 RE_FULL。
// `[Sx` 这类不是出处前缀的不动 —— 前缀枚举比宽松匹配多几个字符, 但不会误吞正文里的 `[`。
const RE_TAIL = /\*{0,2}\[(?:S|So|Sou|Sour|Sourc|Source|W|We|Web)?(?::[^\]]*)?$/;

function escapeHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

// 剥除后的空白整理。只碰"非空白字符之间"的多余空格, 行首缩进 (代码块) 不动。
function tidy(text) {
  return text
    .replace(/\(\s*\)/g, "")
    .replace(/(\S) {2,}(?=\S)/g, "$1 ")
    .replace(/ +([.,;:!?])/g, "$1")
    .replace(/[ \t]+$/gm, "");
}

export function splitCitations(md, { show = false, streaming = false } = {}) {
  let text = md || "";
  if (streaming) text = text.replace(RE_TAIL, "");
  const cites = [];
  text = text.replace(RE_FULL, (raw, kind, ref) => {
    const k = kind.toLowerCase();
    const r = ref.trim();
    cites.push({ kind: k, ref: r, raw });
    if (!show) return "";
    return `<span class="cite cite-${k}">${kind}: ${escapeHtml(r)}</span>`;
  });
  text = tidy(text);
  return { md: text, cites };
}
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && node --test webchat/tests/citations.test.mjs`
Expected: 7 pass。若 show 模式那条因 `tidy` 把 `. <span` 变成 `.<span` 失败, 检查 `/ +([.,;:!?])/` 只匹配空格后紧跟标点, `. <span` 不受影响。

- [ ] **Step 5: Commit**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/webchat/js/citations.js sdtm-rag/webchat/tests/citations.test.mjs && git commit -m "feat(webchat): citations.js — 正文出处抽取/剥除纯函数 + 7 条单测"
```

---

### Task 2: `markdown.js` 流式围栏补全 + 渲染管线 (TDD)

**Files:**
- Create: `webchat/js/markdown.js`
- Test: `webchat/tests/markdown.test.mjs`

**Interfaces:**
- Consumes: `splitCitations` (T1)
- Produces:
  - `prepareStreaming(md: string) → string` 奇数个围栏时用最后一个围栏的记号补闭合。
  - `mdToSafeHTML(md: string) → string` (`DOMPurify.sanitize(marked.parse(md))`, 全局变量来自 vendor 脚本)。
  - `renderMarkdown(md, {streaming=false, showCitations=false}) → string` = split → (streaming ? prepare) → mdToSafeHTML。
  - `highlightIn(el: HTMLElement)` 对 `pre code` 跑 hljs。

- [ ] **Step 1: 写失败测试**

```js
// webchat/tests/markdown.test.mjs
import test from "node:test";
import assert from "node:assert/strict";
import { prepareStreaming } from "../js/markdown.js";

test("奇数个 ``` 围栏 → 末尾补闭合", () => {
  assert.equal(prepareStreaming("a\n```py\nx = 1"), "a\n```py\nx = 1\n```");
});
test("偶数个围栏不动", () => {
  const s = "a\n```py\nx\n```\nb";
  assert.equal(prepareStreaming(s), s);
});
test("~~~ 围栏用 ~~~ 闭合", () => {
  assert.equal(prepareStreaming("~~~\nx"), "~~~\nx\n~~~");
});
test("行内三反引号不算围栏; 缩进 ≤3 空格算", () => {
  assert.equal(prepareStreaming("say ```x``` ok"), "say ```x``` ok");
  assert.equal(prepareStreaming("  ```\nx"), "  ```\nx\n```");
});
test("空/null 安全", () => {
  assert.equal(prepareStreaming(""), "");
  assert.equal(prepareStreaming(null), "");
});
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && node --test webchat/tests/markdown.test.mjs`
Expected: FAIL, module not found。

- [ ] **Step 3: 实现**

```js
// webchat/js/markdown.js
// Markdown 渲染管线。marked / DOMPurify / hljs 是 vendor 脚本挂在 window 上的全局,
// 这里只在函数体内引用 —— 让 prepareStreaming 能在 node 里单测。
import { splitCitations } from "./citations.js";

const RE_FENCE = /^ {0,3}(`{3,}|~{3,})/gm;

// 流中未闭合的代码围栏会把后文全吞进 <pre>, 一帧一帧看就是"整段正文变成代码"。
// 奇数个围栏 ⇒ 补一个与最后一个开栏同记号的闭合 (``` 关不掉 ~~~)。
export function prepareStreaming(md) {
  const text = md || "";
  const fences = text.match(RE_FENCE) || [];
  if (fences.length % 2 === 0) return text;
  const last = fences[fences.length - 1].trim();
  return text + "\n" + last;
}

export function mdToSafeHTML(md) {
  return DOMPurify.sanitize(marked.parse(md || ""));
}

// 统一入口: 出处处理 → (流中) 围栏补全 → 解析 → 净化。
export function renderMarkdown(md, { streaming = false, showCitations = false } = {}) {
  const { md: body } = splitCitations(md, { show: showCitations, streaming });
  return mdToSafeHTML(streaming ? prepareStreaming(body) : body);
}

export function highlightIn(el) {
  el.querySelectorAll("pre code").forEach((b) => hljs.highlightElement(b));
}
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && node --test webchat/tests/`
Expected: 12 pass (7 + 5)。

- [ ] **Step 5: Commit**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/webchat/js/markdown.js sdtm-rag/webchat/tests/markdown.test.mjs && git commit -m "feat(webchat): markdown.js — 流式围栏补全 + renderMarkdown 管线 (出处→围栏→marked→DOMPurify)"
```

---

### Task 3: `store.js` 会话存储 + 重命名 + prefs (TDD)

**Files:**
- Create: `webchat/js/store.js`
- Test: `webchat/tests/store.test.mjs`

**Interfaces:**
- Produces:
  - `export const store` (对象引用不变, 字段 `{conversations, currentId}`; 与老 `load()` 语义一致)。
  - `save()` (含 QuotaExceeded 逐出, 注释原样搬)。
  - `current() → conv` (无则新建), `newConversation() → conv`, `deleteConversation(id)` (**只改 store + save, 不渲染**), `renameConversation(id, title: string) → boolean` (trim 后空 → false 不改)。
  - `export const prefs = {showCitations: false, sidebarCollapsed: false}`; `savePrefs()`; key `sdtm_ui_prefs`。
  - `export const modelLabelById = {}` (id→label 注册表, 供 render/flag 查)。
  - `LS_KEY = "sdtm_chat_v1"`, `HISTORY_TURNS = 10`, `uid()`。

- [ ] **Step 1: 写失败测试**

```js
// webchat/tests/store.test.mjs
import test from "node:test";
import assert from "node:assert/strict";

// localStorage shim (node 没有); 必须在 import store.js 之前装好, 所以用动态 import。
const mem = new Map();
globalThis.localStorage = {
  getItem: (k) => (mem.has(k) ? mem.get(k) : null),
  setItem: (k, v) => mem.set(k, String(v)),
  removeItem: (k) => mem.delete(k),
};
mem.set("sdtm_chat_v1", JSON.stringify({
  conversations: [{ id: "old1", title: "旧会话", createdAt: 1, messages: [{ role: "user", content: "hi" }] }],
  currentId: "old1",
}));
const S = await import("../js/store.js");

test("老存档原样读出, currentId 保留", () => {
  assert.equal(S.store.conversations.length, 1);
  assert.equal(S.current().id, "old1");
  assert.equal(S.current().messages[0].content, "hi");
});

test("newConversation 置顶并成为当前; 结构字段齐全", () => {
  const c = S.newConversation();
  assert.equal(S.store.conversations[0].id, c.id);
  assert.equal(S.store.currentId, c.id);
  assert.deepEqual(Object.keys(c).sort(), ["createdAt", "id", "messages", "title"]);
  assert.equal(JSON.parse(mem.get("sdtm_chat_v1")).currentId, c.id);
});

test("renameConversation: 空白不改, 正常改并落盘", () => {
  const id = S.store.currentId;
  assert.equal(S.renameConversation(id, "   "), false);
  assert.equal(S.renameConversation(id, "  AE 问题 "), true);
  assert.equal(S.store.conversations[0].title, "AE 问题");
  assert.equal(JSON.parse(mem.get("sdtm_chat_v1")).conversations[0].title, "AE 问题");
});

test("deleteConversation 删当前 → currentId 落到剩余首个; 不做渲染", () => {
  const id = S.store.currentId;
  S.deleteConversation(id);
  assert.equal(S.store.currentId, "old1");
  S.deleteConversation("old1");
  assert.equal(S.store.currentId, null);
  assert.equal(S.current().messages.length, 0); // current() 无则新建
});

test("prefs 默认值 + 落盘 + 坏 JSON 容错", () => {
  assert.deepEqual(S.prefs, { showCitations: false, sidebarCollapsed: false });
  S.prefs.showCitations = true; S.savePrefs();
  assert.equal(JSON.parse(mem.get("sdtm_ui_prefs")).showCitations, true);
  mem.set("sdtm_ui_prefs", "{bad");
  assert.deepEqual(S.loadPrefs(), { showCitations: false, sidebarCollapsed: false });
});
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && node --test webchat/tests/store.test.mjs`
Expected: FAIL, module not found。

- [ ] **Step 3: 实现** (从 `app.js` 1-58 行搬 `load/save/current/newConversation/deleteConversation`, 注释一起搬; 去掉 delete 里的 render 调用)

```js
// webchat/js/store.js
// 会话存储 (localStorage) + UI 偏好 + 模型 label 注册表。不碰 DOM。
export const LS_KEY = "sdtm_chat_v1";
export const PREFS_KEY = "sdtm_ui_prefs";
export const HISTORY_TURNS = 10; // 控 token: 发给后端的最近消息条数

// 模型 id → label 表, loadModelName() 拿到 /api/info 后填。页面刚打开、表还是空的时候历史
// 徽章会退化显示原始 id (不影响正确性), loadModelName 填完表后会原地补字。
export const modelLabelById = {};

// uid 不用 crypto.randomUUID (LAN http 非安全上下文不可用)
export const uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 8);

function load() {
  try {
    const s = JSON.parse(localStorage.getItem(LS_KEY));
    if (s && Array.isArray(s.conversations)) return s;
  } catch (_) {}
  return { conversations: [], currentId: null };
}
export const store = load();

export function save() {
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

export function current() {
  let c = store.conversations.find((x) => x.id === store.currentId);
  if (!c) { c = newConversation(); }
  return c;
}
export function newConversation() {
  const c = { id: uid(), title: "新对话", createdAt: Date.now(), messages: [] };
  store.conversations.unshift(c);
  store.currentId = c.id;
  save();
  return c;
}
// 只改数据; 渲染由调用方 (app.js) 负责
export function deleteConversation(id) {
  store.conversations = store.conversations.filter((x) => x.id !== id);
  if (store.currentId === id) store.currentId = store.conversations[0]?.id ?? null;
  save();
}
export function renameConversation(id, title) {
  const t = (title || "").trim();
  const c = store.conversations.find((x) => x.id === id);
  if (!t || !c) return false;
  c.title = t;
  save();
  return true;
}

// ── UI 偏好 (与会话存档分开存, 清一个不影响另一个) ──
const DEFAULT_PREFS = { showCitations: false, sidebarCollapsed: false };
export function loadPrefs() {
  try {
    const p = JSON.parse(localStorage.getItem(PREFS_KEY));
    if (p && typeof p === "object") return { ...DEFAULT_PREFS, ...p };
  } catch (_) {}
  return { ...DEFAULT_PREFS };
}
export const prefs = loadPrefs();
export function savePrefs() {
  try { localStorage.setItem(PREFS_KEY, JSON.stringify(prefs)); } catch (_) {}
}
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && node --test webchat/tests/`
Expected: 17 pass。

- [ ] **Step 5: Commit**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/webchat/js/store.js sdtm-rag/webchat/tests/store.test.mjs && git commit -m "feat(webchat): store.js — 会话存储搬家 + renameConversation + prefs (sdtm_ui_prefs)"
```

---

### Task 4: `stream.js` SSE 搬家 (payload 外置)

**Files:**
- Create: `webchat/js/stream.js`
- 参考: 现 `webchat/app.js` 的 `parseSSE` 与 `streamAsk` (约 396-470 行)

**Interfaces:**
- Produces: `parseSSE(raw) → {event, data}|null`; `streamAsk({question, history, corpus, web, model}, handlers)`; `handlers = {onSources, onToken, onToolCall, onToolResult, onDone, onError, onClose, onAbort, signal}` 与现在同名同语义。`model` 为 falsy 时**整个字段省略** (spec §1)。

- [ ] **Step 1: 写文件** (逐字搬 `parseSSE`; `streamAsk` 只改 payload 构造, 注释保留)

```js
// webchat/js/stream.js
// SSE 流式客户端。不读 DOM: 检索范围 / 联网 / 模型由调用方算好传进来。
export function parseSSE(raw) {
  let event = "message", data = "";
  for (const line of raw.split("\n")) {
    if (line.startsWith("event:")) event = line.slice(6).trim();
    else if (line.startsWith("data:")) data += line.slice(5).trim();
  }
  if (!data) return null;
  try { return { event, data: JSON.parse(data) }; } catch (_) { return null; }
}

export async function streamAsk({ question, history, corpus, web, model },
                                { onSources, onToken, onToolCall, onToolResult, onDone, onError, onClose, onAbort, signal }) {
  let resp;
  try {
    const payload = { question, history, corpus, web };
    // spec §5 裁定: UI **永远发显式 id**, 绝不依赖默认值落到 default 组 ——
    // default 与 opus-5 今天都解析到 Opus 5, 但改 .env 的 default_model 会让二者静默分叉。
    // 下拉为空 (info 没加载出来) 时**整个字段省略**, 由服务端默认值接管, 而不是硬塞 "default"
    // ——「省略」与「显式传 default」在服务端是同一行为, 但省略不会在产物里留下一个
    // 用户根本没做过的选择。
    if (model) payload.model = model;
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
```

- [ ] **Step 2: 加一条 parseSSE 单测**

```js
// webchat/tests/stream.test.mjs
import test from "node:test";
import assert from "node:assert/strict";
import { parseSSE } from "../js/stream.js";

test("parseSSE 解析 event/data; 坏 JSON 返回 null", () => {
  assert.deepEqual(parseSSE('event: token\ndata: {"text":"hi"}'), { event: "token", data: { text: "hi" } });
  assert.equal(parseSSE("event: token\ndata: {bad"), null);
  assert.equal(parseSSE("event: token"), null);
});
```

Run: `cd sdtm-rag && node --test webchat/tests/` → 18 pass。

- [ ] **Step 3: 对比确认逐字搬家**

Run: `cd sdtm-rag && diff <(sed -n '/^function parseSSE/,/^}/p' webchat/app.js) <(sed -n '/^export function parseSSE/,/^}/p' webchat/js/stream.js | sed 's/^export //')`
Expected: 无输出 (完全一致)。

- [ ] **Step 4: Commit**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/webchat/js/stream.js sdtm-rag/webchat/tests/stream.test.mjs && git commit -m "refactor(webchat): stream.js — SSE 客户端搬家, payload 由调用方构造 (逻辑零改动)"
```

---

### Task 5: `ui.js` 交互原语 (复制 / 两步删除 / 重命名 / 滚动跟随 / 设置弹层 / 侧栏折叠)

**Files:**
- Create: `webchat/js/ui.js`

**Interfaces:**
- Produces:
  - `copyText(text) → Promise<boolean>` (clipboard API, 失败退 `execCommand`)。
  - `armDelete(btn, onConfirm, {label="确认删除", ms=3000})` 两步确认。
  - `inlineRename(titleEl, currentTitle, onCommit)` 行内 input, Enter/blur 提交, Esc 取消。
  - `initScrollFollow(box, toBottomBtn) → {isFollowing(): boolean, follow(): void, scrollToBottom(): void}`。
  - `initSettings(btn, panel)` 开关 + 点外关闭。
  - `initSidebar({sidebar, collapseBtn, expandBtn, prefs, savePrefs})`。
  - `selectedCorpus() → "auto"|"cdisc"|"study"|"both"`; `webEnabled() → boolean` (读 `#scope-*`, 注释原样搬)。
  - `autoGrow(textarea)`。
  - `$ = (id) => document.getElementById(id)`。

- [ ] **Step 1: 写文件**

```js
// webchat/js/ui.js
// 与业务无关的交互原语。不 import 本地模块。
export const $ = (id) => document.getElementById(id);

// ── 复制: LAN http 下 navigator.clipboard 不存在 (非安全上下文), 退回 execCommand ──
export async function copyText(text) {
  try {
    if (navigator.clipboard?.writeText) { await navigator.clipboard.writeText(text); return true; }
  } catch (_) {}
  try {
    const ta = document.createElement("textarea");
    ta.value = text; ta.setAttribute("readonly", "");
    ta.style.cssText = "position:fixed;left:-9999px;top:0;opacity:0";
    document.body.appendChild(ta); ta.select();
    const ok = document.execCommand("copy");
    ta.remove();
    return ok;
  } catch (_) { return false; }
}

// 按钮短暂显示反馈文字后复原
export function flash(btn, text, ms = 1200) {
  const orig = btn.dataset.orig ?? btn.textContent;
  btn.dataset.orig = orig;
  btn.textContent = text;
  clearTimeout(btn._flashT);
  btn._flashT = setTimeout(() => { btn.textContent = orig; }, ms);
}

// ── 两步删除: 第一次点 → 变「确认删除」(danger), ms 内再点才真删, 超时复原 ──
export function armDelete(btn, onConfirm, { label = "确认删除", ms = 3000 } = {}) {
  if (btn.dataset.armed === "1") { onConfirm(); return; }
  const orig = btn.textContent;
  btn.dataset.armed = "1"; btn.textContent = label; btn.classList.add("armed");
  btn._armT = setTimeout(() => {
    btn.dataset.armed = ""; btn.textContent = orig; btn.classList.remove("armed");
  }, ms);
}

// ── 行内重命名 ──
export function inlineRename(titleEl, currentTitle, onCommit) {
  if (titleEl.querySelector("input")) return;
  const input = document.createElement("input");
  input.type = "text"; input.value = currentTitle; input.className = "rename-input";
  input.maxLength = 60;
  let done = false;
  const finish = (commit) => {
    if (done) return; done = true;
    const v = input.value;
    input.remove();
    titleEl.textContent = currentTitle;
    if (commit) onCommit(v);
  };
  input.addEventListener("keydown", (e) => {
    if (e.isComposing || e.keyCode === 229) return; // IME 组字中的回车不算提交
    if (e.key === "Enter") { e.preventDefault(); finish(true); }
    else if (e.key === "Escape") { e.preventDefault(); finish(false); }
  });
  input.addEventListener("blur", () => finish(true));
  input.addEventListener("click", (e) => e.stopPropagation());
  titleEl.textContent = "";
  titleEl.appendChild(input);
  input.focus(); input.select();
}

// ── 滚动跟随: 用户上滚 > 80px 就停止自动到底, 出现「回到底部」; 滚回底部或点按钮恢复 ──
export function initScrollFollow(box, toBottomBtn) {
  let following = true;
  const distance = () => box.scrollHeight - box.scrollTop - box.clientHeight;
  const scrollToBottom = () => { box.scrollTop = box.scrollHeight; };
  const sync = () => { toBottomBtn.hidden = following; };
  box.addEventListener("scroll", () => {
    following = distance() < 80;
    sync();
  });
  toBottomBtn.addEventListener("click", () => { following = true; scrollToBottom(); sync(); });
  sync();
  return {
    isFollowing: () => following,
    follow: () => { following = true; scrollToBottom(); sync(); },
    scrollToBottom,
  };
}

// ── 设置弹层: 点齿轮开关, 点面板外关闭, Esc 关闭 ──
export function initSettings(btn, panel) {
  const close = () => { panel.hidden = true; btn.setAttribute("aria-expanded", "false"); };
  const open = () => { panel.hidden = false; btn.setAttribute("aria-expanded", "true"); };
  btn.addEventListener("click", (e) => { e.stopPropagation(); panel.hidden ? open() : close(); });
  panel.addEventListener("click", (e) => e.stopPropagation());
  document.addEventListener("click", () => { if (!panel.hidden) close(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !panel.hidden) close(); });
}

// ── 侧栏折叠 (记进 prefs) ──
export function initSidebar({ sidebar, collapseBtn, expandBtn, prefs, savePrefs }) {
  const apply = () => {
    sidebar.classList.toggle("collapsed", prefs.sidebarCollapsed);
    expandBtn.hidden = !prefs.sidebarCollapsed;
  };
  collapseBtn.addEventListener("click", () => { prefs.sidebarCollapsed = true; savePrefs(); apply(); });
  expandBtn.addEventListener("click", () => { prefs.sidebarCollapsed = false; savePrefs(); apply(); });
  apply();
}

// 检索范围 checkbox → 后端 corpus 字面量 (auto|cdisc|study|both)。
// 两个都不勾 = auto: 交给 LLM 判库 (federation.decide_corpus), 与改 checkbox 前的默认行为一致。
export function selectedCorpus() {
  const cdisc = $("scope-cdisc").checked, study = $("scope-study").checked;
  if (cdisc && study) return "both";
  if (cdisc) return "cdisc";
  if (study) return "study";
  return "auto";
}
// 联网是与 corpus 正交的第四维: 只决定挂不挂 web_search 工具, 不参与判库。
export function webEnabled() { return $("scope-web").checked; }

export function autoGrow(ta) { ta.style.height = "auto"; ta.style.height = Math.min(ta.scrollHeight, 200) + "px"; }
```

- [ ] **Step 2: 语法检查**

Run: `cd sdtm-rag && node --check webchat/js/ui.js && echo OK`
Expected: OK。

- [ ] **Step 3: Commit**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/webchat/js/ui.js && git commit -m "feat(webchat): ui.js — 复制/两步删除/行内重命名/滚动跟随/设置弹层/侧栏折叠 原语"
```

---

### Task 6: `flag.js` + `render.js` (消息渲染层重做)

**Files:**
- Create: `webchat/js/flag.js`
- Create: `webchat/js/render.js`
- 参考: 现 `webchat/app.js` 60-395 行 (renderSidebar / messageEl / modelBadgeText / renderModelBadge / refreshModelBadgeLabels / metaEl / corpusBadge / sourcesEl / ensureWebPanel / onToolCallUI / onToolResultUI / renderWebStatus / attachFlag / openFlag / flagModelName / postFlag)。

**Interfaces:**
- Consumes: `store, save, prefs, modelLabelById` (T3); `renderMarkdown, highlightIn` (T2); `copyText, flash, armDelete, inlineRename, $` (T5)。
- Produces (render.js):
  - `renderSidebar({onSelect(id), onDelete(id), onRename(id, title)})`。
  - `renderMessages({onPickExample(text), onRetry(conv)})` 空会话时渲染空状态。
  - `messageEl(m: {role, content, sources?, routedCorpus?, webStatus?, webSearchesOk?, modelId?, verified?, modelsUsed?, fellBack?}) → HTMLElement` 结构:
    ```
    article.turn.{user|assistant}
      ├ .web-panel        (按需 prepend)
      ├ .bubble(.md)
      ├ .turn-meta        (chips 容器, :empty 隐藏)
      ├ .sources-slot
      └ .turn-tools       (复制 / ⚑; 仅 assistant)
    ```
  - `setSources(turn, sources, routedCorpus)`; `renderWebStatus(turn, status, searchesOk)`; `onToolCallUI(turn, d)`; `onToolResultUI(turn, d)`; `renderModelBadge(turn, modelId, verified, modelsUsed, fellBack)`; `refreshModelBadgeLabels()`; `modelBadgeText(...)` (原样); `attachTools(turn, question, msgObj)`; `finalizeBubble(bubble, content)` (完整渲染 + 高亮 + 代码块复制钮); `appendErr(bubble, msg)`; `appendRetry(turn, onClick)`.
- Produces (flag.js): `flagButton(question, msgObj, mount: HTMLElement) → HTMLButtonElement` (点击在 `mount` 内展开 flag-box); `flagModelName(msgObj)`; `postFlag(...)`。

- [ ] **Step 1: 写 `flag.js`** (逻辑与注释逐字搬; 变化: 不再自己建 `.msg-actions`, 由调用方给 mount; topbar 回退改读 `#topbar-model`)

```js
// webchat/js/flag.js
// ⚑ dogfood 失败捕获 → POST /api/flag → dogfood_failures.md (append-only 优先级 backlog)。
import { save, modelLabelById } from "./store.js";
import { $ } from "./ui.js";

export function flagButton(question, msgObj, mount) {
  const btn = document.createElement("button");
  btn.className = "tool-btn flag-btn"; btn.type = "button";
  if (msgObj && msgObj.flagged) {
    btn.textContent = "✓ 已记录"; btn.disabled = true; btn.classList.add("done");
  } else {
    btn.textContent = "⚑ 标记"; btn.onclick = () => openFlag(mount, btn, question, msgObj);
  }
  return btn;
}

function openFlag(mount, btn, question, msgObj) {
  if (mount.querySelector(".flag-box")) return; // already open
  btn.hidden = true;
  const box = document.createElement("div");
  box.className = "flag-box";
  const ta = document.createElement("textarea");
  ta.placeholder = "哪里答错/答弱? 期望是什么? (可留空)"; ta.rows = 2;
  const send = document.createElement("button"); send.textContent = "记录"; send.className = "flag-send"; send.type = "button";
  const cancel = document.createElement("button"); cancel.textContent = "取消"; cancel.className = "flag-cancel"; cancel.type = "button";
  cancel.onclick = () => { box.remove(); btn.hidden = false; };
  send.onclick = async () => {
    send.disabled = true; cancel.disabled = true; send.textContent = "...";
    const ok = await postFlag(question, msgObj ? msgObj.content : "", ta.value, msgObj);
    if (ok) {
      if (msgObj) { msgObj.flagged = true; save(); }
      box.remove();
      btn.textContent = "✓ 已记录"; btn.disabled = true; btn.classList.add("done"); btn.hidden = false;
    } else {
      send.disabled = false; cancel.disabled = false; send.textContent = "记录";
      if (!box.querySelector(".err")) {
        const e = document.createElement("span"); e.className = "err"; e.textContent = " 记录失败"; box.appendChild(e);
      }
    }
  };
  box.append(ta, send, cancel);
  mount.appendChild(box);
  ta.focus();
}

// 归因必须取**这一条答案实际用的模型** (msgObj.modelId, 由 done 事件落进历史存档)。
// topbar 文本是 /api/info 的 default_model, 与答题模型无关 —— 下拉可选模型之前"唯一
// 答题模型就是 default 组"成立, 所以拿它凑合是对的; 现在它会把 A 模型的捏造记到 B 头上,
// 而 dogfood_failures.md 是 append-only 的优先级 backlog, 错误写入即永久且无从回溯。
// modelId 缺失 (下拉上线前存的旧历史) 时才退回 topbar 文本: 那些记录确实产自 default 组。
export function flagModelName(msgObj) {
  const id = msgObj && msgObj.modelId;
  // 回退过 ⇒ 答案是 modelsUsed 里那些模型产的, **不是**用户选的那个。把 DeepSeek 的捏造
  // 记到 GPT-5.6 Sol 头上, 与终审 C-1 是同一个缺陷换了触发路径 (那次是切 topbar 文本,
  // 这次是读了 modelId 但答案不是它产的)。两边都写进去: backlog 的读者既要知道谁捏造的,
  // 也要知道当时选的是谁 —— 否则"为什么会用到这个模型"这条线索断了。
  // Array.isArray 的理由与 modelBadgeText 那处相同 (容器级契约; 元素级由 server/router.py
  // 收集处的 `if reported:` 保证, 那里只 append 真值串), 但**后果更重**: 这里抛出去的
  // 异常穿过 postFlag ⇒ 用户点了 ⚑ 却什么都没记下, 而 backlog 是 append-only 的 (规则 B)。
  // 缺陷本身把发现缺陷的渠道堵了。⛔ 同样别加 filter(Boolean): 那条路径不可达。
  if (msgObj && msgObj.fellBack === true && Array.isArray(msgObj.modelsUsed)
      && msgObj.modelsUsed.length) {
    return `${msgObj.modelsUsed.join("、")}（回退自 ${id ? (modelLabelById[id] || id) : "未知"}）`;
  }
  if (id) return modelLabelById[id] || id;   // 表没加载好就发原始 id, 归因照样正确
  // #topbar-model 显示的是 /api/info 的 default_model 短名 (loadModelName 填), 与老 topbar 语义一致
  return ($("topbar-model").dataset.defaultModel || "").trim() || null;
}

export async function postFlag(question, answer, note, msgObj) {
  const model = flagModelName(msgObj);
  try {
    const r = await fetch("/api/flag", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, answer, note, model }),
    });
    return r.ok;
  } catch (_) { return false; }
}
```

- [ ] **Step 2: 写 `render.js`**

```js
// webchat/js/render.js
// DOM 渲染层: 侧栏 / 消息 / 元信息 chips / 来源 / 联网面板 / 空状态。
import { store, prefs, modelLabelById } from "./store.js";
import { renderMarkdown, highlightIn } from "./markdown.js";
import { copyText, flash, armDelete, inlineRename, $ } from "./ui.js";
import { flagButton } from "./flag.js";

// Plan B 联邦: 库标签 (日文 UI)。map 里没有的值 (null / 未知) 一律不渲染徽章 —— 联邦关时零变化。
const CORPUS_LABEL = { cdisc: "標準", study: "本研究", both: "両方" };

const EXAMPLES = [
  { q: "AE 域中 AESER 与 AESEV 的区别是什么?", study: false },
  { q: "SUPPQUAL 什么情况下使用? 举一个 AE 的例子", study: false },
  { q: "--DTC 变量的 ISO 8601 部分日期 (只知道年月) 怎么写?", study: false },
  { q: "本研究 ST01 的 VS 域有哪些测试项?", study: true },
];

// ── 侧栏 ──
export function renderSidebar({ onSelect, onDelete, onRename }) {
  const ul = $("conv-list");
  ul.innerHTML = "";
  for (const c of store.conversations) {
    const li = document.createElement("li");
    if (c.id === store.currentId) li.className = "active";
    const t = document.createElement("span");
    t.className = "title";
    t.textContent = c.title || "新对话";
    t.title = "双击重命名";
    t.onclick = () => onSelect(c.id);
    t.ondblclick = (e) => { e.preventDefault(); inlineRename(t, c.title || "新对话", (v) => onRename(c.id, v)); };
    const del = document.createElement("button");
    del.className = "del"; del.type = "button"; del.textContent = "✕"; del.title = "删除";
    del.onclick = (e) => { e.stopPropagation(); armDelete(del, () => onDelete(c.id)); };
    li.append(t, del);
    ul.appendChild(li);
  }
}

// ── 消息列表 ──
export function renderMessages({ onPickExample, onRetry }) {
  const box = $("messages");
  box.innerHTML = "";
  const c = store.conversations.find((x) => x.id === store.currentId);
  if (!c) return;
  if (!c.messages.length) { box.appendChild(emptyState(onPickExample)); return; }
  let lastUserQ = "";
  for (const m of c.messages) {
    const el = messageEl(m);
    if (m.role === "user") lastUserQ = m.content;
    else if (m.role === "assistant") attachTools(el, lastUserQ, m);
    box.appendChild(el);
  }
  box.scrollTop = box.scrollHeight;
}

function emptyState(onPick) {
  const wrap = document.createElement("div");
  wrap.className = "empty";
  const h = document.createElement("h1"); h.textContent = "SDTM 知识库助手";
  const p = document.createElement("p");
  p.textContent = "基于 CDISC SDTM IG / Model / 术语表的检索增强问答。回答附来源, 请以标准原文为准。";
  const grid = document.createElement("div"); grid.className = "examples";
  const federation = !$("scope").hidden;
  for (const ex of EXAMPLES) {
    if (ex.study && !federation) continue;
    const card = document.createElement("button");
    card.type = "button"; card.className = "example"; card.textContent = ex.q;
    card.onclick = () => onPick(ex.q);
    grid.appendChild(card);
  }
  wrap.append(h, p, grid);
  return wrap;
}

export function messageEl(m) {
  const turn = document.createElement("article");
  turn.className = "turn " + m.role;
  const b = document.createElement("div");
  b.className = "bubble" + (m.role === "assistant" ? " md" : "");
  if (m.role === "assistant") finalizeBubble(b, m.content);
  else b.textContent = m.content;
  turn.appendChild(b);
  if (m.role === "assistant") {
    const meta = document.createElement("div"); meta.className = "turn-meta";
    const slot = document.createElement("div"); slot.className = "sources-slot";
    const tools = document.createElement("div"); tools.className = "turn-tools";
    turn.append(meta, slot, tools);
    setSources(turn, m.sources, m.routedCorpus);
    // 刷新/切会话后复原联网状态。不复原的话, 一个"已降级为未联网"的 KB-only 答案
    // 和正常联网答案长得一模一样 (spec §7 点名的最骗人的失败模式)。
    renderWebStatus(turn, m.webStatus, m.webSearchesOk);
    // 同一个坑, spec §6: 只做 UI 标注(下拉旁边那行提示)的话, 对话存下来后这条信息就没了。
    renderModelBadge(turn, m.modelId, m.verified, m.modelsUsed, m.fellBack);
  }
  return turn;
}

// 完整渲染 (非流式): markdown + 高亮 + 代码块复制钮
export function finalizeBubble(bubble, content) {
  bubble.innerHTML = renderMarkdown(content, { streaming: false, showCitations: prefs.showCitations });
  highlightIn(bubble);
  decorateCodeBlocks(bubble);
}

function decorateCodeBlocks(bubble) {
  bubble.querySelectorAll("pre").forEach((pre) => {
    if (pre.querySelector(".code-copy")) return;
    const btn = document.createElement("button");
    btn.type = "button"; btn.className = "code-copy"; btn.textContent = "复制";
    btn.onclick = async () => flash(btn, (await copyText(pre.querySelector("code")?.innerText ?? pre.innerText)) ? "已复制" : "复制失败");
    pre.appendChild(btn);
  });
}

export function appendErr(bubble, msg) {
  const e = document.createElement("div"); e.className = "err"; e.textContent = "⚠ " + msg;
  bubble.appendChild(e);
}
export function appendRetry(turn, onClick) {
  const btn = document.createElement("button");
  btn.type = "button"; btn.className = "retry"; btn.textContent = "重试";
  btn.onclick = onClick;
  turn.appendChild(btn);
}

// 工具条: 复制 Markdown (存档原文, 含出处) + ⚑
export function attachTools(turn, question, msgObj) {
  const tools = turn.querySelector(".turn-tools");
  if (!tools || tools.childElementCount) return;
  const copy = document.createElement("button");
  copy.type = "button"; copy.className = "tool-btn"; copy.textContent = "复制";
  copy.onclick = async () => flash(copy, (await copyText(msgObj.content || "")) ? "已复制" : "复制失败");
  tools.append(copy, flagButton(question, msgObj, tools));
}

// ── 元信息 chips ──
function chip(text, cls) {
  const s = document.createElement("span");
  s.className = "chip " + (cls || "");
  s.textContent = text;
  return s;
}
function metaBox(turn) { return turn.querySelector(":scope > .turn-meta"); }

// verified 三态不可混同 (spec §6): true 正常; false 是拿到确证的"验过且不通过";
// null (default 组不在 selectable_models 里, 没有 verified 概念) 一律显"未知",
// 绝不能落进 false 那支 (会把"没这个概念"误报成"验过且不通过")。
//
// 回退 (fellBack === true, 2026-09-02 spec §4.4) 优先于以上三态: 答案是**另一个(些)**
// 模型产的, 那么"用户选的那个验没验过"对这条消息不再成立 —— 拿 opus-5 的 verified: true
// 给一条 DeepSeek 答的消息背书, 就是终审 C-1 (⚑ 归错模型) 同族。琥珀色照挂: 回退是
// **已知的偏离**, 不是单纯的元数据缺失, 值得与"未验证模型"同级的视觉提示。
//
// modelsUsed 是**列表**: 联网多轮 / 流中途回退时一次回答可能有两个模型各写了一段,
// 只报一个就又变成半个真话了 (spec R6)。绝大多数情况长度为 1, 文案退化成单模型形态。
//
// ⚠ `fellBack === true` 用**全等**而非 truthy: 老后端不发这个字段 (StaticFiles 从工作树
// 现读 ⇒ 新前端会先于 Python 重启上线, spec §5 B1) 、老存档里也没有这个键, 两种情况都是
// undefined, 必须落回下面三态、文案与今天逐字相同。
export function modelBadgeText(modelId, verified, modelsUsed, fellBack) {
  const label = modelLabelById[modelId] || modelId;
  // ⚠ `Array.isArray` 不是洁癖: 只判 truthy + `.length` 挡不住**字符串** ("abc".length 是 3)
  // 也挡不住 array-like 对象 —— 两者都会走到 `.join` 上抛 TypeError, 而这一抛是在
  // `renderMessages` 里 ⇒ 死的不是一条徽章, 是**整段对话历史渲染不出来**。
  // 后端发回什么形状不由前端说了算 (onDone 是 `?? null`, 零形状校验), 所以这里必须自己挡。
  //
  // **容器级**契约到此为止, **元素级**的 (每个元素是非空串) 由后端保证:
  // `server/router.py` 收集处的 `if reported:` 只 append 真值串, 所以 `[null]` / `[""]`
  // 这类"说回退了却说不出回退到谁"的半个真话在生产上产不出来。
  // ⛔ 别在这里加 `filter(Boolean)` 之类的防御 —— 为不可达路径写防御, 下一个人会以为它可达。
  // 为什么容器级只需要这一个判断就够: 值必然经 JSON 往返 (localStorage / SSE), 到达时
  // 只可能是 null|bool|number|string|array|plain object 六种, `Array.isArray` 恰好把前五种
  // 全挡在外面 —— 这也是"`join` 被改写成别的东西"那类畸形同样不会抛的原因。
  if (fellBack === true && Array.isArray(modelsUsed) && modelsUsed.length) {
    return { text: `模型: ${label} → 实际 ${modelsUsed.join("、")}（已回退）· 验证状态未知`,
             unverified: true };
  }
  if (verified === true) return { text: `模型: ${label}`, unverified: false };
  if (verified === false) return { text: `模型: ${label} ⚠未验证`, unverified: true };
  return { text: `模型: ${label} · 验证状态未知`, unverified: false };
}

// 答案实际用的模型 (spec §6 产物自证)。modelId 为空 (生成中占位 / 未流完就中断 / 旧历史
// 记录没存这个字段) 时什么都不画 —— 比瞎猜一个模型名更诚实, 也避免占位阶段先画一个"未知"
// 徽章、done 后又叠一个真实徽章的重复渲染。
export function renderModelBadge(turn, modelId, verified, modelsUsed, fellBack) {
  if (!modelId) return;
  const b = chip("", "model-meta");
  // 这四个值存进 dataset: /api/info 比首屏渲染慢一步是常态, label 表填好后
  // refreshModelBadgeLabels() 要能原地补字, 不能靠重建 DOM 拿到它们
  // (重建会抹掉正在生成、尚未进 c.messages 的那个气泡 —— 上一轮复审用 gate stub 复现过)。
  b.dataset.modelId = modelId;
  b.dataset.verified = String(verified); // "true" | "false" | "null"
  b.dataset.modelsUsed = JSON.stringify(modelsUsed || []);
  b.dataset.fellBack = String(fellBack);  // "true" | "false" | "null" | "undefined"(老存档)
  const { text, unverified } = modelBadgeText(modelId, verified, modelsUsed, fellBack);
  b.textContent = text;
  if (unverified) b.classList.add("unverified");
  metaBox(turn).appendChild(b);
}

// loadModelName() 拿到 /api/info 的 label 表往往晚于首屏渲染, 此前画出的模型徽章只能显示
// 原始 id。这里只原地改文字, 不碰其余 DOM —— 尤其不能用 renderMessages() 整体重建: 一次
// 生成中的助手气泡是直接 appendChild 挂到 #messages 上的, 要等 onDone→persist() 之后才会
// 进 c.messages, 这个窗口内重建会把它整个抹掉(复审用 gate 住 /api/info + 卡流复现过)。
export function refreshModelBadgeLabels() {
  document.querySelectorAll(".model-meta").forEach((b) => {
    const modelId = b.dataset.modelId;
    if (!modelId) return;
    const verified = b.dataset.verified === "true" ? true : b.dataset.verified === "false" ? false : null;
    // 显式三路比较, 不用 truthy —— dataset 里存的是字符串, "false" 是 truthy 的
    const fellBack = b.dataset.fellBack === "true" ? true : b.dataset.fellBack === "false" ? false : null;
    let modelsUsed = [];
    // 坏数据不该让整条历史渲染崩掉 —— 拿不到就当"没有这个信息", 退回非回退文案
    try { modelsUsed = JSON.parse(b.dataset.modelsUsed || "[]"); } catch (_) { modelsUsed = []; }
    b.textContent = modelBadgeText(modelId, verified, modelsUsed, fellBack).text;
  });
}

// ── 来源 (SSE sources 事件) + 判定库 chip ──
export function setSources(turn, sources, routedCorpus) {
  const label = CORPUS_LABEL[routedCorpus];
  if (label) metaBox(turn).appendChild(chip(`判定: ${label}`, "corpus"));
  if (!sources || !sources.length) return;
  const slot = turn.querySelector(":scope > .sources-slot");
  slot.innerHTML = "";
  slot.appendChild(sourcesEl(sources));
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
    const head = document.createElement("div"); head.className = "src-head";
    const badge = corpusBadge(src.corpus);
    if (badge) head.appendChild(badge);
    const name = document.createElement("b");
    name.textContent = src.source + (src.section ? ` — ${src.section}` : "");
    const sim = document.createElement("span"); sim.className = "sim";
    sim.textContent = `sim ${(src.similarity ?? 0).toFixed(3)}`;
    head.append(name, sim);
    const p = document.createElement("div"); p.className = "src-preview";
    p.textContent = src.text_preview || "";
    div.append(head, p);
    d.appendChild(div);
  }
  return d;
}

// ── 联网搜索过程面板 ──
// 搜索过程条: 网页版那种「看得见它在搜什么」的观感。没有这层, 勾了联网只会
// 看到卡住半分钟然后蹦出一段话 —— 那是超时的感觉, 不是联网的感觉。
// ⚠ 挂在 turn (气泡外层) 而非 bubble: 流中会整体替换气泡 innerHTML。
function ensureWebPanel(turn) {
  let p = turn.querySelector(":scope > .web-panel");
  if (!p) {
    p = document.createElement("div");
    p.className = "web-panel";
    turn.prepend(p);   // 搜索过程显示在答案上方
  }
  return p;
}

export function onToolCallUI(turn, d) {
  const row = document.createElement("div");
  row.className = "web-row";
  row.dataset.callId = d.id || "";
  row.textContent = `🔍 搜索 "${d.query || ""}"`;
  ensureWebPanel(turn).appendChild(row);
}

export function onToolResultUI(turn, d) {
  const p = ensureWebPanel(turn);
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
export function renderWebStatus(turn, status, searchesOk) {
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
  ensureWebPanel(turn).appendChild(warn);
}
```

- [ ] **Step 3: 语法检查 + 护栏 diff**

Run:
```bash
cd sdtm-rag && node --check webchat/js/render.js && node --check webchat/js/flag.js && \
diff <(sed -n '/^function modelBadgeText/,/^}/p' webchat/app.js) <(sed -n '/^export function modelBadgeText/,/^}/p' webchat/js/render.js | sed 's/^export //') && \
diff <(sed -n '/^function refreshModelBadgeLabels/,/^}/p' webchat/app.js) <(sed -n '/^export function refreshModelBadgeLabels/,/^}/p' webchat/js/render.js | sed 's/^export //') && \
diff <(sed -n '/^function renderWebStatus/,/^}/p' webchat/app.js | sed 's/holder/turn/g') <(sed -n '/^export function renderWebStatus/,/^}/p' webchat/js/render.js | sed 's/^export //') && echo GUARDS-IDENTICAL
```
Expected: `GUARDS-IDENTICAL` (三个护栏函数逐字一致)。

- [ ] **Step 4: Commit**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/webchat/js/render.js sdtm-rag/webchat/js/flag.js && git commit -m "feat(webchat): render.js + flag.js — 消息渲染层重做 (turn/chips/tools/空状态), 护栏函数逐字搬家"
```

---

### Task 7: `index.html` + `style.css` 重写 (视觉系统)

**Files:**
- Rewrite: `webchat/index.html`
- Rewrite: `webchat/style.css`

**Interfaces:**
- 控件 id 保持: `model-select / scope / scope-cdisc / scope-study / scope-web / model-warning / messages / composer / input / send / new-chat / conv-list`。
- 新增 id: `sidebar / collapse-side / expand-side / topbar-model / settings-btn / settings-panel / show-citations / to-bottom`。
- `#topbar-model` 用 `dataset.defaultModel` 存 `/api/info` 的 default_model 短名 (flag.js 回退读)。

- [ ] **Step 1: 写 `index.html`**

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
      <div class="side-head">
        <span class="brand">SDTM Pedia</span>
        <button id="collapse-side" class="icon-btn" type="button" title="收起侧栏" aria-label="收起侧栏">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="1.5" y="2.5" width="13" height="11" rx="2"/><path d="M6 2.5v11"/></svg>
        </button>
      </div>
      <button id="new-chat" type="button">＋ 新对话</button>
      <ul id="conv-list"></ul>
    </aside>

    <main id="main">
      <header id="topbar">
        <button id="expand-side" class="icon-btn" type="button" title="展开侧栏" aria-label="展开侧栏" hidden>
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="1.5" y="2.5" width="13" height="11" rx="2"/><path d="M6 2.5v11"/></svg>
        </button>
        <span id="topbar-title">SDTM 知识库助手</span>
        <span id="topbar-model" class="topbar-model"></span>
        <div class="topbar-right">
          <button id="settings-btn" class="icon-btn" type="button" title="设置" aria-label="设置" aria-expanded="false">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg>
          </button>
          <div id="settings-panel" hidden>
            <section>
              <h3>答题模型</h3>
              <select id="model-select" title="答题模型"></select>
              <div id="model-warning" class="hint warn" hidden>⚠ 该模型的反捏造边界未在其上验证</div>
            </section>
            <!-- 联邦检索范围; /api/info 的 federation=false 时保持 hidden (见 app.js loadModelName)。
                 两个都不勾 = auto (LLM 判库), 勾选则显式指定并绕过路由。 -->
            <fieldset id="scope" title="検索範囲 (未選択 = 自動判定)" hidden>
              <legend>检索范围 (都不勾 = 自动判定)</legend>
              <label><input type="checkbox" id="scope-cdisc" /> CDISC 標準</label>
              <label><input type="checkbox" id="scope-study" /> 本研究 (ST01)</label>
              <label title="让模型自行决定是否搜索公开网络 (业界实践参考, 非标准依据)">
                <input type="checkbox" id="scope-web" /> 联网参考
              </label>
            </fieldset>
            <section>
              <h3>显示</h3>
              <label><input type="checkbox" id="show-citations" /> 显示正文行内出处 (调试用)</label>
              <div class="hint">关闭时出处只在底部「来源」里看; 生成中不可切换。</div>
            </section>
          </div>
        </div>
      </header>

      <div id="messages"></div>
      <button id="to-bottom" type="button" hidden>↓ 回到底部</button>

      <form id="composer">
        <div class="composer-box">
          <textarea id="input" rows="1" placeholder="问点关于 SDTM 的……（Enter 发送，Shift+Enter 换行）"></textarea>
          <button id="send" type="submit" aria-label="发送">发送</button>
        </div>
        <p class="footnote">回答由模型生成, 请以 CDISC 标准原文为准。</p>
      </form>
    </main>
  </div>
  <script src="/static/vendor/marked.min.js"></script>
  <script src="/static/vendor/purify.min.js"></script>
  <script src="/static/vendor/highlight.min.js"></script>
  <script type="module" src="/static/app.js"></script>
</body>
</html>
```

- [ ] **Step 2: 写 `style.css`**

```css
/* ── Design tokens (spec §3, 克制专业型) ── */
:root {
  --bg: #faf9f6; --bg-side: #f2f0eb; --bg-user: #eeece6; --bg-panel: #ffffff;
  --ink: #1c1b19; --ink-2: #5c5a55; --ink-3: #9a978f; --line: #e4e1da; --line-2: #d6d2c8;
  --accent: #1f6f5f; --accent-ink: #ffffff; --accent-soft: #e3efeb;
  --warn: #b45309; --warn-soft: #fdf3e6; --danger: #b3261e; --danger-soft: #fbeae8;
  --font-serif: "Source Serif 4", "Iowan Old Style", "Songti SC", Georgia, serif;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans", "Noto Sans CJK SC", sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  --r-sm: 6px; --r-md: 10px; --r-lg: 14px;
  --col: 720px;
  --shadow: 0 1px 2px rgba(28,27,25,.06), 0 8px 24px rgba(28,27,25,.08);
}
* { box-sizing: border-box; }
html, body { margin: 0; height: 100%; }
body { font-family: var(--font-sans); color: var(--ink); background: var(--bg); font-size: 15px; -webkit-font-smoothing: antialiased; }
button { font: inherit; color: inherit; }
#app { display: flex; height: 100vh; }

/* ── 侧栏 ── */
#sidebar { width: 260px; flex: 0 0 260px; background: var(--bg-side); border-right: 1px solid var(--line); display: flex; flex-direction: column; padding: 12px; gap: 10px; overflow: hidden; transition: width .18s ease, flex-basis .18s ease, padding .18s ease; }
#sidebar.collapsed { width: 0; flex-basis: 0; padding: 0; border-right: none; }
.side-head { display: flex; align-items: center; justify-content: space-between; padding: 4px 6px 2px; }
.brand { font-family: var(--font-serif); font-size: 17px; letter-spacing: .01em; color: var(--ink); }
.icon-btn { border: none; background: transparent; padding: 6px; border-radius: var(--r-sm); cursor: pointer; color: var(--ink-2); display: inline-flex; align-items: center; }
.icon-btn:hover { background: rgba(28,27,25,.06); color: var(--ink); }
#new-chat { padding: 9px 12px; border: 1px solid var(--line-2); border-radius: var(--r-md); background: var(--bg-panel); cursor: pointer; font-size: 14px; text-align: left; color: var(--ink); }
#new-chat:hover { border-color: var(--accent); color: var(--accent); }
#conv-list { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 2px; overflow-y: auto; }
#conv-list li { padding: 7px 8px 7px 10px; border-radius: var(--r-sm); cursor: pointer; font-size: 13.5px; color: var(--ink-2); display: flex; justify-content: space-between; align-items: center; gap: 6px; }
#conv-list li:hover { background: rgba(28,27,25,.05); color: var(--ink); }
#conv-list li.active { background: var(--accent-soft); color: var(--accent); font-weight: 500; }
#conv-list .title { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; flex: 1; }
#conv-list .rename-input { width: 100%; font: inherit; padding: 2px 4px; border: 1px solid var(--accent); border-radius: 4px; background: var(--bg-panel); color: var(--ink); outline: none; }
#conv-list .del { opacity: 0; border: none; background: none; cursor: pointer; color: var(--ink-3); font-size: 12px; padding: 2px 4px; border-radius: 4px; white-space: nowrap; }
#conv-list li:hover .del, #conv-list .del.armed { opacity: 1; }
#conv-list .del:hover { color: var(--danger); }
#conv-list .del.armed { color: var(--danger); background: var(--danger-soft); font-weight: 500; }

/* ── 主区 / 顶栏 ── */
#main { flex: 1; display: flex; flex-direction: column; min-width: 0; position: relative; }
#topbar { height: 52px; padding: 0 16px; border-bottom: 1px solid var(--line); display: flex; align-items: center; gap: 10px; background: var(--bg); }
#topbar-title { font-family: var(--font-serif); font-size: 16px; color: var(--ink); }
.topbar-model { font-size: 12.5px; color: var(--ink-3); padding: 2px 8px; border: 1px solid var(--line); border-radius: 999px; }
.topbar-model:empty { display: none; }
.topbar-right { margin-left: auto; position: relative; }
#settings-panel { position: absolute; right: 0; top: calc(100% + 8px); width: 320px; background: var(--bg-panel); border: 1px solid var(--line); border-radius: var(--r-lg); box-shadow: var(--shadow); padding: 6px 16px 12px; z-index: 20; font-size: 13.5px; }
#settings-panel section, #settings-panel fieldset { padding: 10px 0; border: none; border-top: 1px solid var(--line); margin: 0; min-inline-size: 0; }
#settings-panel section:first-child { border-top: none; }
#settings-panel h3, #settings-panel legend { font-size: 11.5px; text-transform: uppercase; letter-spacing: .06em; color: var(--ink-3); margin: 0 0 8px; padding: 0; font-weight: 500; }
#settings-panel label { display: flex; align-items: center; gap: 8px; padding: 4px 0; color: var(--ink); cursor: pointer; }
#settings-panel input[type=checkbox] { margin: 0; accent-color: var(--accent); }
#settings-panel select { width: 100%; padding: 7px 8px; border: 1px solid var(--line-2); border-radius: var(--r-sm); background: var(--bg-panel); font: inherit; color: var(--ink); }
#scope[hidden] { display: none; }
.hint { font-size: 12px; color: var(--ink-3); margin-top: 6px; line-height: 1.5; }
.hint.warn { color: var(--warn); }

/* ── 消息区 ── */
#messages { flex: 1; overflow-y: auto; padding: 28px 20px 12px; scroll-behavior: auto; }
.turn { max-width: var(--col); margin: 0 auto 26px; }
.turn.user { display: flex; justify-content: flex-end; }
.turn.user .bubble { max-width: 80%; background: var(--bg-user); padding: 10px 14px; border-radius: var(--r-lg) var(--r-lg) 4px var(--r-lg); white-space: pre-wrap; line-height: 1.6; }
.turn.assistant .bubble { line-height: 1.72; font-size: 15.5px; }
.md > :first-child { margin-top: 0; } .md > :last-child { margin-bottom: 0; }
.md h1, .md h2, .md h3, .md h4 { font-family: var(--font-serif); font-weight: 600; line-height: 1.3; margin: 1.4em 0 .5em; color: var(--ink); }
.md h1 { font-size: 1.45em; } .md h2 { font-size: 1.28em; } .md h3 { font-size: 1.12em; } .md h4 { font-size: 1em; }
.md p { margin: .7em 0; }
.md ul, .md ol { padding-left: 1.5em; margin: .6em 0; } .md li { margin: .25em 0; } .md li > p { margin: .3em 0; }
.md a { color: var(--accent); text-decoration: underline; text-underline-offset: 2px; }
.md blockquote { margin: .8em 0; padding: .2em 1em; border-left: 3px solid var(--line-2); color: var(--ink-2); }
.md hr { border: none; border-top: 1px solid var(--line); margin: 1.4em 0; }
.md code { font-family: var(--font-mono); font-size: .88em; background: rgba(28,27,25,.06); padding: .12em .35em; border-radius: 4px; }
.md pre { position: relative; background: #f4f2ed; border: 1px solid var(--line); padding: 12px 14px; border-radius: var(--r-md); overflow-x: auto; margin: .9em 0; }
.md pre code { background: none; padding: 0; font-size: 13px; line-height: 1.55; }
.code-copy { position: absolute; top: 6px; right: 6px; font-size: 11.5px; padding: 3px 8px; border: 1px solid var(--line-2); border-radius: 5px; background: var(--bg-panel); color: var(--ink-2); cursor: pointer; opacity: 0; transition: opacity .12s; }
.md pre:hover .code-copy { opacity: 1; }
.md table { border-collapse: collapse; margin: .9em 0; font-size: 14px; display: block; overflow-x: auto; max-width: 100%; }
.md th, .md td { border: 1px solid var(--line); padding: 6px 10px; text-align: left; vertical-align: top; }
.md th { background: var(--bg-side); font-weight: 600; }
/* 行内出处 (设置开关打开时): 独占一行, 淡灰等宽小字, 不与正文争眼 */
.cite { display: block; font-family: var(--font-mono); font-size: 11.5px; color: var(--ink-3); margin: 2px 0 6px; line-height: 1.4; word-break: break-all; }

/* 元信息 chips / 来源 / 工具条: 与正文左对齐 */
.turn-meta { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 12px; }
.turn-meta:empty { display: none; }
.chip { font-size: 11.5px; color: var(--ink-2); background: var(--bg-side); border: 1px solid var(--line); border-radius: 999px; padding: 2px 9px; line-height: 1.6; }
.chip.unverified { color: var(--warn); background: var(--warn-soft); border-color: #f1d9b8; } /* 同 .web-warn 的琥珀色, 未验证模型徽章一眼分辨 */
.sources-slot:empty { display: none; }
.sources { margin-top: 10px; font-size: 13px; }
.sources summary { cursor: pointer; color: var(--ink-3); list-style: none; display: inline-flex; align-items: center; gap: 6px; padding: 2px 0; }
.sources summary::-webkit-details-marker { display: none; }
.sources summary::before { content: "▸"; font-size: 11px; transition: transform .12s; }
.sources[open] summary::before { transform: rotate(90deg); }
.sources summary:hover { color: var(--ink); }
.src { border-left: 2px solid var(--line-2); padding: 6px 10px; margin: 8px 0; color: var(--ink-2); }
.src-head { display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; }
.src-head b { font-weight: 500; color: var(--ink); font-family: var(--font-mono); font-size: 12px; }
.src .sim { color: var(--ink-3); font-size: 11.5px; }
.src-preview { margin-top: 3px; font-size: 12.5px; line-height: 1.5; color: var(--ink-3); display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
.corpus-badge { font-size: 11px; padding: 0 5px; border-radius: 3px; background: #e0e7ff; color: #333; }
.corpus-badge.study { background: #ffe4e6; }
.turn-tools { display: flex; gap: 4px; align-items: center; flex-wrap: wrap; margin-top: 8px; opacity: 0; transition: opacity .12s; }
.turn:hover .turn-tools, .turn-tools:focus-within, .turn-tools:has(.flag-box) { opacity: 1; }
.tool-btn { border: none; background: none; color: var(--ink-3); cursor: pointer; font-size: 12.5px; padding: 3px 7px; border-radius: 5px; }
.tool-btn:hover { color: var(--ink); background: rgba(28,27,25,.06); }
.flag-btn:hover { color: var(--danger); }
.flag-btn.done { color: var(--accent); cursor: default; }
.flag-box { display: flex; gap: 6px; align-items: flex-start; flex-basis: 100%; margin-top: 4px; }
.flag-box textarea { flex: 1; resize: vertical; min-height: 40px; padding: 6px 8px; border: 1px solid var(--line-2); border-radius: var(--r-sm); font: inherit; font-size: 13px; }
.flag-send, .flag-cancel { padding: 5px 12px; border: 1px solid var(--line-2); border-radius: var(--r-sm); background: var(--bg-panel); color: var(--ink-2); cursor: pointer; font-size: 13px; }
.flag-send { background: var(--accent); color: var(--accent-ink); border-color: var(--accent); }
.flag-send:disabled { opacity: .5; cursor: default; }

/* 联网搜索过程面板 */
.web-panel { margin: 0 0 12px; padding: 8px 12px; background: var(--warn-soft); border-left: 3px solid #e0a552; border-radius: var(--r-sm); font-size: 13px; color: var(--ink-2); }
.web-row { padding: 2px 0; }
.web-note { color: var(--ink-3); }
.web-warn { margin-top: 6px; color: var(--warn); font-weight: 500; }
.web-note-block { margin-top: 6px; color: var(--ink-2); }

.err { color: var(--danger); font-size: 13.5px; margin-top: 8px; }
.retry { margin-top: 8px; padding: 5px 14px; border: 1px solid var(--line-2); border-radius: var(--r-sm); background: var(--bg-panel); color: var(--ink-2); cursor: pointer; font-size: 13px; }
.retry:hover { border-color: var(--accent); color: var(--accent); }

/* 空状态 */
.empty { max-width: var(--col); margin: 12vh auto 0; text-align: center; padding: 0 12px; }
.empty h1 { font-family: var(--font-serif); font-weight: 500; font-size: 30px; margin: 0 0 10px; letter-spacing: .005em; }
.empty p { color: var(--ink-2); margin: 0 auto 28px; max-width: 520px; line-height: 1.6; }
.examples { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; text-align: left; }
.example { padding: 12px 14px; border: 1px solid var(--line); border-radius: var(--r-md); background: var(--bg-panel); cursor: pointer; font-size: 14px; line-height: 1.5; color: var(--ink-2); text-align: left; }
.example:hover { border-color: var(--accent); color: var(--accent); background: var(--accent-soft); }
@media (max-width: 640px) { .examples { grid-template-columns: 1fr; } }

/* 回到底部 */
#to-bottom { position: absolute; left: 50%; transform: translateX(-50%); bottom: 118px; padding: 6px 14px; border: 1px solid var(--line-2); border-radius: 999px; background: var(--bg-panel); color: var(--ink-2); font-size: 12.5px; cursor: pointer; box-shadow: var(--shadow); z-index: 5; }
#to-bottom:hover { color: var(--accent); border-color: var(--accent); }

/* 输入区 */
#composer { max-width: calc(var(--col) + 40px); width: 100%; margin: 0 auto; padding: 4px 20px 14px; }
.composer-box { display: flex; align-items: flex-end; gap: 8px; padding: 8px 8px 8px 14px; border: 1px solid var(--line-2); border-radius: var(--r-lg); background: var(--bg-panel); box-shadow: 0 1px 2px rgba(28,27,25,.04); }
.composer-box:focus-within { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
#input { flex: 1; resize: none; max-height: 200px; padding: 6px 0; border: none; outline: none; font: inherit; font-size: 15px; line-height: 1.5; background: transparent; color: var(--ink); }
#send { padding: 8px 16px; border: none; border-radius: var(--r-md); background: var(--accent); color: var(--accent-ink); cursor: pointer; font-size: 14px; font-weight: 500; }
#send:hover { filter: brightness(.95); }
#send:disabled { background: var(--line-2); cursor: default; }
#send.stop { background: var(--danger); }
.footnote { text-align: center; font-size: 11.5px; color: var(--ink-3); margin: 8px 0 0; }
```

- [ ] **Step 3: 启动本地服务肉眼检查骨架** (此时 app.js 仍是旧版, 会因缺 id 报错 —— 只看静态样式即可)

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_webchat_cache_headers.py -q`
Expected: 全绿 (测试用 tmp 目录, 不受 html 影响; 只是确认没把服务弄坏)。

- [ ] **Step 4: Commit**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/webchat/index.html sdtm-rag/webchat/style.css && git commit -m "feat(webchat): index.html + style.css 重写 — design tokens / 设置弹层 / 空状态 / 工具条 (视觉系统)"
```

---

### Task 8: `app.js` 重写 (入口 + 流式渲染接线 + 设置)

**Files:**
- Rewrite: `webchat/app.js`

**Interfaces:**
- Consumes: 全部前序模块。
- 关键行为:
  - `runGeneration(c)`: rAF 节流流式渲染; `done/error/close/abort` 四路与旧版语义一致 (`renderFinal + persist` 组合不变)。
  - `loadModelName()`: 填 `#topbar-model` (label) 与 `dataset.defaultModel`; `#scope.hidden = !info.federation`; 下拉; `sdtm_model` 刷新保留; `refreshModelBadgeLabels()`。
  - 出处开关: 生成中 `disabled`; 切换后 `renderMessages()`。

- [ ] **Step 1: 写 `app.js`**

```js
// webchat/app.js — 入口: 事件绑定 + 生成流程编排。渲染在 render.js, 存储在 store.js。
import { store, save, current, newConversation, deleteConversation, renameConversation,
         prefs, savePrefs, modelLabelById, HISTORY_TURNS } from "./js/store.js";
import { renderSidebar, renderMessages, messageEl, finalizeBubble, appendErr, appendRetry,
         attachTools, setSources, renderWebStatus, renderModelBadge, refreshModelBadgeLabels,
         onToolCallUI, onToolResultUI } from "./js/render.js";
import { renderMarkdown } from "./js/markdown.js";
import { streamAsk } from "./js/stream.js";
import { $, initScrollFollow, initSettings, initSidebar, selectedCorpus, webEnabled, autoGrow } from "./js/ui.js";

// ── 渲染回调 (侧栏/消息需要的动作) ──
const sidebarHandlers = {
  onSelect: (id) => { store.currentId = id; save(); paintAll(); },
  onDelete: (id) => { deleteConversation(id); paintAll(); },
  onRename: (id, title) => { if (renameConversation(id, title)) renderSidebar(sidebarHandlers); },
};
const messageHandlers = {
  onPickExample: (q) => send(q),
  onRetry: (c) => retry(c),
};
function paintAll() { renderSidebar(sidebarHandlers); renderMessages(messageHandlers); }

const scroller = initScrollFollow($("messages"), $("to-bottom"));

// ── 发送 / 停止 / 重试 ──
let busy = false;
let currentAbort = null; // AbortController for the in-flight stream

function setSending(on) {
  const b = $("send");
  b.textContent = on ? "停止" : "发送";
  b.classList.toggle("stop", on);
  b.disabled = false; // stay clickable while streaming so it can Stop
  $("show-citations").disabled = on; // 生成中切换会触发整体重渲染, 抹掉在途气泡 (spec §5)
}
function stop() { if (currentAbort) currentAbort.abort(); }

async function send(text) {
  if (busy || !text.trim()) return;
  const c = current();
  c.messages.push({ role: "user", content: text });
  if (c.messages.length === 1) c.title = text.slice(0, 30);
  save(); paintAll();
  scroller.follow();
  await runGeneration(c);
}

// Re-run generation for the conversation's last user message (drops any failed/partial
// assistant turn first), without appending a duplicate user message.
function retry(c) {
  if (busy) return;
  while (c.messages.length && c.messages[c.messages.length - 1].role === "assistant") {
    c.messages.pop();
  }
  save(); renderMessages(messageHandlers);
  if (c.messages.some((m) => m.role === "user")) runGeneration(c);
}

async function runGeneration(c) {
  const lastUserIdx = c.messages.map((m) => m.role).lastIndexOf("user");
  if (lastUserIdx === -1) return;
  const text = c.messages[lastUserIdx].content;
  busy = true; setSending(true);

  const box = $("messages");
  const turn = messageEl({ role: "assistant", content: "" });
  box.appendChild(turn); scroller.scrollToBottom();
  const bubble = turn.querySelector(".bubble");

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
  let gotModelsUsed = null;
  let gotFellBack = null;
  let saved = false;
  let savedMsg = null;

  // ── 流式渲染: rAF 节流, 每帧最多一次全量 markdown 解析 (spec §4) ──
  // 旧版流中只 textContent 追加、done 后才渲染 —— 用户全程看裸 md 语法。全量重解析在
  // < 10 KB 文本上单次 < 2 ms, 不做增量 diff (YAGNI)。高亮只在 finalize 时跑一次 (流中会闪)。
  let dirty = false, rafId = 0;
  const paint = () => {
    rafId = 0;
    if (!dirty) return;
    dirty = false;
    try {
      bubble.innerHTML = renderMarkdown(acc, { streaming: true, showCitations: prefs.showCitations });
    } catch (_) {
      bubble.textContent = acc; // marked 理论上不抛; 真抛了也不能让流断掉
    }
    if (scroller.isFollowing()) scroller.scrollToBottom();
  };
  const renderFinal = (content) => {
    if (rafId) { cancelAnimationFrame(rafId); rafId = 0; }
    dirty = false;
    finalizeBubble(bubble, content);
    if (scroller.isFollowing()) scroller.scrollToBottom();
  };
  const persist = (content) => {
    if (saved) return;
    saved = true;
    savedMsg = { role: "assistant", content, sources: gotSources || [], routedCorpus: gotRouted,
                 webStatus: gotWebStatus, webSearchesOk: gotWebSearchesOk,
                 modelId: gotModelId, verified: gotVerified,
                 // 产物自证 (spec §6 / 2026-09-02 R5): 回退这件事必须活过刷新, 否则
                 // 存档里一条 DeepSeek 答的消息与 Opus 5 答的长得一模一样。
                 modelsUsed: gotModelsUsed, fellBack: gotFellBack };
    c.messages.push(savedMsg);
    save(); renderSidebar(sidebarHandlers);
  };
  const fail = (msg) => { appendErr(bubble, msg); appendRetry(turn, () => retry(c)); };

  const ctrl = new AbortController();
  currentAbort = ctrl;
  try {
    await streamAsk({ question: text, history, corpus: selectedCorpus(), web: webEnabled(),
                      model: $("model-select").value }, {
      onSources: (s, routed) => { gotSources = s; gotRouted = routed; setSources(turn, s, routed); },
      onToken: (t) => { acc += t; dirty = true; if (!rafId) rafId = requestAnimationFrame(paint); },
      onToolCall: (d) => onToolCallUI(turn, d),
      onToolResult: (d) => onToolResultUI(turn, d),
      onDone: (data) => {
        gotWebStatus = (data || {}).web_status; gotWebSearchesOk = (data || {}).web_searches_ok;
        // ?? 只在 null/undefined 时取右值, false 会原样保留 —— 与 renderModelBadge 的
        // 三态语义 (spec §6) 保持一致: verified 缺失时按"未知"收, 不会误当成 false。
        gotModelId = (data || {}).model_id ?? null;
        gotVerified = (data || {}).verified ?? null;
        // 同一条 ?? 的理由: fell_back 的 false 是**确证没回退**, 不能被当成缺失塌成 null。
        // ⚠ 这两个字段原样收下、不做形状校验 —— 形状由 modelBadgeText 的 Array.isArray
        // 挡 (后端发个裸串就能让整段历史渲染不出来, 见那里的注释)。
        gotModelsUsed = (data || {}).models_used ?? null;
        gotFellBack = (data || {}).fell_back ?? null;
        renderWebStatus(turn, gotWebStatus, gotWebSearchesOk);
        renderModelBadge(turn, gotModelId, gotVerified, gotModelsUsed, gotFellBack);
        const content = acc.trim() ? acc : "(无内容)"; renderFinal(content); persist(content);
      },
      onError: (msg) => { if (acc) { renderFinal(acc); persist(acc); } fail(msg); },
      // 干净 EOF 但无 done/error: 内容已在屏上, 落盘防刷新丢失 (规则 D HIGH 修复)。
      onClose: () => { if (acc) { renderFinal(acc); persist(acc); fail("连接中断（已保留已生成内容）"); } else fail("连接中断"); },
      // 用户点「停止」: 保留已生成部分, 不报错样式, 给重试入口。
      onAbort: () => { if (acc) { renderFinal(acc); persist(acc); } fail("已停止"); },
      signal: ctrl.signal,
    });
  } finally {
    busy = false; setSending(false); currentAbort = null;
    // attach the tools (复制 / ⚑) once the answer is final + persisted (skip if nothing saved)
    if (savedMsg) attachTools(turn, text, savedMsg);
  }
}

// ── topbar/设置: 显示后端真实 default_model + 联邦开关 + 模型下拉 (读 /api/info) ──
async function loadModelName() {
  try {
    const r = await fetch("/api/info");
    if (!r.ok) return; // not logged in / info unavailable -> keep static label, 选择器保持隐藏
    const info = await r.json();
    const m = (info.default_model || "").split("/").pop();
    const tm = $("topbar-model");
    if (m) { tm.dataset.defaultModel = m; tm.textContent = m; }
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
      if (o) tm.textContent = modelLabelById[o.value] || o.value; // 顶栏显示当前所选模型
    };
    sel.addEventListener("change", () => {
      localStorage.setItem("sdtm_model", sel.value);
      syncWarning();
    });
    syncWarning();
    refreshModelBadgeLabels(); // 原地补字, 不重建 #messages (理由见函数注释)
    // 空状态的示例卡依赖 federation 才知道要不要显示 ST01 那张; 只在空会话时重画
    const c = store.conversations.find((x) => x.id === store.currentId);
    if (c && !c.messages.length && !busy) renderMessages(messageHandlers);
  } catch (_) {}
}

// ── 事件绑定 ──
$("new-chat").onclick = () => { newConversation(); paintAll(); $("input").focus(); };
$("composer").onsubmit = (e) => {
  e.preventDefault();
  if (busy) { stop(); return; } // button is in "停止" mode while streaming
  const v = $("input").value; $("input").value = ""; autoGrow($("input")); send(v);
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
$("input").addEventListener("input", (e) => autoGrow(e.target));

initSettings($("settings-btn"), $("settings-panel"));
initSidebar({ sidebar: $("sidebar"), collapseBtn: $("collapse-side"), expandBtn: $("expand-side"), prefs, savePrefs });
$("show-citations").checked = prefs.showCitations;
$("show-citations").addEventListener("change", (e) => {
  prefs.showCitations = e.target.checked; savePrefs();
  if (!busy) renderMessages(messageHandlers); // busy 时控件是 disabled 的, 到不了这里
});

// ── 启动 ──
if (!store.conversations.length) newConversation();
paintAll();
loadModelName();
```

- [ ] **Step 2: 语法检查 + 单测 + 头测试**

Run: `cd sdtm-rag && node --check webchat/app.js && node --test webchat/tests/ && .venv/bin/python -m pytest scripts/tests/test_webchat_cache_headers.py -q`
Expected: 全绿。

- [ ] **Step 3: 浏览器冒烟 (生产 launchd 服务 localhost:8000 直接从工作树读静态文件, 普通刷新即可)**

用 Chrome MCP 打开 `http://localhost:8000/`, 逐项确认并截图:
1. 空状态: 标题 + 示例卡 (联邦开则 4 张, 否则 3 张)。
2. 点一张示例卡 → 用户块右对齐; 流中 AI 回答**已经是渲染后的标题/列表** (不是 `##`/`-`); 正文里**没有** `[Source:` 字样。
3. 完成后: 底部 chips (模型徽章), 「来源 (N)」可展开, 悬停出现 [复制][⚑ 标记]; 代码块 (若有) 悬停出现复制。
4. 设置齿轮: 模型下拉/检索范围/出处开关; 打开出处开关 → 正文出现淡灰等宽独行 `Source: …`。生成中开关灰掉。
5. 侧栏: 双击标题重命名; 点 ✕ 变红「确认删除」, 3 秒后复原; 再点即删。折叠/展开侧栏, 刷新后记住。
6. 流中上滚 → 出现「↓ 回到底部」, 点击回到底部并恢复跟随。
7. 老存档: 刷新后历史消息全部正常, 徽章/联网状态/来源都在。
8. 浏览器 console 无报错。

任一项不符 → 修复后再次冒烟, 不带着已知问题进 Task 9。

- [ ] **Step 4: Commit**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/webchat/app.js && git commit -m "feat(webchat): app.js 重写 — 模块化入口 + rAF 节流流式 Markdown 渲染 + 出处开关 + 设置弹层接线"
```

---

### Task 9: Playwright e2e (流式渲染 + 出处开关) 与回归

**Files:**
- Create: `scripts/tests/test_webchat_stream_render.py`

**Interfaces:**
- Consumes: 真 `create_app()` (与 `test_webchat_cache_browser.py` 同款 fixture), `_WEBCHAT_DIR` 指向**真实** `webchat/`, 用 `page.route` 拦截 `/api/ask_stream` 与 `/api/info` 给 stub 响应 (不碰 RAG 引擎)。

- [ ] **Step 1: 装 playwright (dev-only, 可选; 没装则本文件 skip)**

Run: `cd sdtm-rag && uv pip install --python .venv/bin/python playwright && .venv/bin/playwright install chromium` (失败也可继续: `_launch` 会退回本机 Chrome; 两者都没有则 skip)。

- [ ] **Step 2: 写测试**

```python
"""真浏览器闸: 流式期间 Markdown 已渲染 + 正文出处默认隐藏、开关后以 .cite 显示。

为什么真浏览器: 这两条都是"某一帧 DOM 长什么样"的断言, 只有浏览器能回答。
SSE 用 page.route 在浏览器侧 stub, 不需要 RAG 引擎 (lifespan 关掉)。
装法见 test_webchat_cache_browser.py docstring; 未装 playwright 则本文件可见地 skip。
"""
from __future__ import annotations

import socket
import threading
import time
from pathlib import Path
from types import SimpleNamespace

import pytest
import uvicorn

from server import main as main_mod
from server.config import Settings

pw_api = pytest.importorskip(
    "playwright.sync_api",
    reason="真浏览器闸需要 playwright (dev-only 可选; 装法见 test_webchat_cache_browser.py)",
)

_WEBCHAT = Path(__file__).resolve().parents[2] / "webchat"

_INFO = {"default_model": "bedrock/x/opus-5", "federation": False,
         "selectable_models": [{"id": "opus-5", "label": "Opus 5", "verified": True}]}

# 四帧 token: 第 2 帧之后 (done 之前) DOM 里就该有 <h2> 与 <li>; 出处夹在正文中间。
_FRAMES = [
    ('sources', '{"sources":[{"chunk_id":"c1","source":"domains/AE.md","domain":"AE","file_type":"spec",'
                '"section":"§1","similarity":0.9,"text_preview":"AETERM"}],"routed_corpus":null}'),
    ('token', '{"text":"## AE 域\\n\\n- AETERM 是报告术语 **[Source: domains/AE.md]**\\n"}'),
    ('token', '{"text":"- AEDECOD 是编码术语"}'),
    ('done', '{"model_id":"opus-5","verified":true,"web_status":"off","web_searches_ok":0,'
             '"models_used":["opus-5"],"fell_back":false}'),
]


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


@pytest.fixture
def live(monkeypatch):
    monkeypatch.setattr(main_mod, "_WEBCHAT_DIR", _WEBCHAT)
    settings = Settings(federation_enabled=False, study_lookup_enabled=False, study_docs_enabled=False)
    port = _free_port()
    server = uvicorn.Server(uvicorn.Config(main_mod.create_app(settings), host="127.0.0.1", port=port,
                                           lifespan="off", log_level="warning"))
    t = threading.Thread(target=server.run, daemon=True)
    t.start()
    deadline = time.monotonic() + 15
    while not server.started:
        if time.monotonic() > deadline or not t.is_alive():
            server.should_exit = True
            raise RuntimeError("uvicorn 没起来")
        time.sleep(0.05)
    try:
        yield SimpleNamespace(url=f"http://127.0.0.1:{port}/")
    finally:
        server.should_exit = True
        t.join(timeout=15)


def _launch(pw):
    try:
        return pw.chromium.launch()
    except Exception:
        try:
            return pw.chromium.launch(channel="chrome")
        except Exception as exc:
            pytest.skip(f"没有可用的 chromium/chrome: {exc}")


def _stub_routes(page, hold_after_frame: int, release: threading.Event):
    """/api/info 固定; /api/ask_stream 吐前 hold_after_frame 帧后**卡住**等 release, 让测试
    能在 done 之前观察 DOM。"""
    page.route("**/api/info", lambda r: r.fulfill(status=200, content_type="application/json",
                                                  body=__import__("json").dumps(_INFO)))

    def sse(route):
        def body():
            for i, (ev, data) in enumerate(_FRAMES):
                yield f"event: {ev}\ndata: {data}\n\n".encode()
                if i + 1 == hold_after_frame:
                    release.wait(timeout=20)
        route.fulfill(status=200, content_type="text/event-stream", body=b"".join(body()))
    page.route("**/api/ask_stream", sse)


def _ask(page, text: str):
    page.fill("#input", text)
    page.press("#input", "Enter")


def test_markdown_renders_before_done_and_citation_hidden(live):
    """playwright 的 route.fulfill 一次性给 body, 无法真正卡流; 所以这条用两段验证:
    (a) 全量帧完成后 DOM 是渲染后的 md 且无 [Source; (b) 用 page.evaluate 直接调
    renderMarkdown(streaming=True) 断言流中半截围栏/出处的行为 (同一份模块代码)。"""
    with pw_api.sync_playwright() as pw:
        browser = _launch(pw)
        try:
            page = browser.new_page()
            _stub_routes(page, hold_after_frame=99, release=threading.Event())
            page.goto(live.url)
            page.wait_for_selector(".empty h1")
            _ask(page, "AE 域问题")
            page.wait_for_selector(".turn.assistant .chip.model-meta")
            html = page.inner_html(".turn.assistant .bubble")
            assert "<h2" in html and "<li" in html
            assert "[Source" not in html and "Source:" not in html
            assert page.inner_text(".turn.assistant .bubble").strip().endswith("AEDECOD 是编码术语")
            # 来源折叠区仍在, 与正文出处无关
            assert page.inner_text(".sources summary") == "来源 (1)"

            # (b) 流中行为: 同一模块, streaming=True
            mid = page.evaluate("""async () => {
                const m = await import('/static/js/markdown.js');
                return [m.renderMarkdown('## T\\n\\n- a **[Source: x', {streaming:true}),
                        m.renderMarkdown('```py\\nx=1', {streaming:true})];
            }""")
            assert "<h2" in mid[0] and "<li" in mid[0] and "Source" not in mid[0]
            assert "<pre" in mid[1] and "x=1" in mid[1]

            # 开关打开 → 出处以 .cite 显示; 存档原文不变 (复制按钮拿到的还是原文)
            page.click("#settings-btn")
            page.check("#show-citations")
            page.wait_for_selector(".turn.assistant .bubble .cite")
            assert page.inner_text(".turn.assistant .bubble .cite") == "Source: domains/AE.md"
            stored = page.evaluate("() => JSON.parse(localStorage.getItem('sdtm_chat_v1')).conversations[0].messages[1].content")
            assert "**[Source: domains/AE.md]**" in stored
        finally:
            browser.close()


def test_old_archive_still_renders(live):
    """老存档 (无 modelId / fellBack 字段) 刷新后照常渲染, 徽章不画 (modelId 缺失时什么都不画)。"""
    with pw_api.sync_playwright() as pw:
        browser = _launch(pw)
        try:
            page = browser.new_page()
            _stub_routes(page, hold_after_frame=99, release=threading.Event())
            page.goto(live.url)
            page.evaluate("""() => localStorage.setItem('sdtm_chat_v1', JSON.stringify({
                conversations:[{id:'o1',title:'旧',createdAt:1,messages:[
                  {role:'user',content:'q'},
                  {role:'assistant',content:'**A** [Source: a.md]',sources:[]}]}], currentId:'o1'}))""")
            page.reload()
            page.wait_for_selector(".turn.assistant .bubble strong")
            assert page.locator(".chip.model-meta").count() == 0
            assert "Source" not in page.inner_text(".turn.assistant .bubble")
            assert page.locator(".turn-tools .flag-btn").count() == 1
        finally:
            browser.close()
```

- [ ] **Step 3: 跑全部 webchat 相关测试**

Run: `cd sdtm-rag && node --test webchat/tests/ && .venv/bin/python -m pytest scripts/tests/test_webchat_cache_headers.py scripts/tests/test_webchat_cache_browser.py scripts/tests/test_webchat_stream_render.py -q`
Expected: node 18 pass; pytest 全绿 (playwright 装了) 或 browser 两个文件可见 SKIPPED (没装)。若 `route.fulfill` 对 `text/event-stream` 不触发前端 `getReader` 分帧 —— 前端按 `\n\n` 切帧, 一次性 body 也能正确分 4 帧, 断言不受影响。

- [ ] **Step 4: Commit**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/scripts/tests/test_webchat_stream_render.py && git commit -m "test(webchat): playwright 闸 — 流式 md 已渲染 / 出处默认隐藏+开关 / 老存档兼容"
```

---

### Task 10: Rule D 独立审阅 + 文档收口

**Files:**
- Modify: `webchat/vendor/README.md` (追加「模块结构」一段)
- Create: `sdtm-rag/evidence/checkpoints/chat_ui_redesign_2026-09.md`
- Modify: `CLAUDE.md` Key Paths 中「Phase 7 Chat UI」那行 (≤ 80 字符, 指向 evidence)
- Modify: `.work/meta/worklog/phase07.md` append

- [ ] **Step 1: 派独立 reviewer (不同 subagent_type, opus)** 审阅重点 = spec §1 不变量逐条: 给它 spec 路径 + `git diff 2af9079..HEAD -- sdtm-rag/webchat` + 要求输出 PASS / PASS-WITH-FIXES / FAIL 与逐条证据。FAIL/FIXES 项修完再派一轮直到 PASS。

- [ ] **Step 2: 写 evidence checkpoint**

内容: 目标 / 改动清单 / 不变量核对表 (每条: 位置 + diff 证据命令) / 测试命令与输出 (node --test 计数, pytest 结果, 截图路径) / reviewer 结论 / 已知限制 (playwright fulfill 无法真卡流, 流中行为由 evaluate 直调模块证明; 出处剥除会同样作用于代码块内的 `[Source:` 字样, 极罕见)。

- [ ] **Step 3: README 追加**

```markdown
## 模块结构 (2026-09 重构)

`app.js` (入口, type=module) → `js/{store,render,markdown,citations,stream,flag,ui}.js`。
单测: `node --test webchat/tests/`。e2e: `scripts/tests/test_webchat_stream_render.py` (playwright 可选)。
正文 `[Source: path]` 由 `citations.js` 在渲染层剥除 (设置→显示行内出处 可开); 存档与 ⚑ 上报存原文。
```

- [ ] **Step 4: CLAUDE.md Key Paths 该行改为**

`| Phase 7 Chat UI (2026-09-08 重构: 模块化+流式 md+出处隐藏) | `sdtm-rag/webchat/` (入口 app.js→js/*); 证据 `evidence/checkpoints/chat_ui_redesign_2026-09.md`; ⚑ → `dogfood_failures.md` |`

- [ ] **Step 5: 全量回归 + Commit**

Run: `cd sdtm-rag && node --test webchat/tests/ && .venv/bin/python -m pytest scripts/tests/ -q -x --ignore=scripts/tests/test_build_neo4j.py 2>&1 | tail -3`
Expected: 无 FAIL。

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/webchat/vendor/README.md sdtm-rag/evidence/checkpoints/chat_ui_redesign_2026-09.md CLAUDE.md .work/meta/worklog/phase07.md && git commit -m "docs(webchat): Chat UI 重构收口 — evidence checkpoint + Rule D 审阅结论 + README/CLAUDE 指针"
```

---

## Self-Review

- **Spec 覆盖**: §2 文件结构 → T1-T8; §3 视觉 → T7; §4 流式 → T2 + T8 (paint/renderFinal); §5 出处 → T1 + T7 (`.cite` CSS + 开关) + T8 (disabled 时不切换); §6 五项 UX → T5 (原语) + T6 (接线 renderSidebar/attachTools/decorateCodeBlocks/emptyState) + T8 (scroller); §7 错误边界 → T8 paint try/catch, 老存档 T9; §8 测试 → T1/T2/T3/T4 node, T9 playwright, T8 Step 3 人工; Rule D → T10。
- **Placeholder**: 无 TBD; T10 Step 2 是文档内容提纲 (非代码)。
- **一致性**: `messageEl(m)` 单对象参数 (T6 定义, T8 调用 `messageEl({role:"assistant", content:""})`); `setSources(turn, s, routed)` T6/T8 一致; `streamAsk({question,history,corpus,web,model}, handlers)` T4/T8 一致; `initScrollFollow` 返回 `{isFollowing, follow, scrollToBottom}` T5/T8 一致; `flagButton(question, msgObj, mount)` T6 flag.js/render.js 一致; `#topbar-model.dataset.defaultModel` T6 flag.js 读 / T8 写 / T7 元素存在。
- **注意**: T6 `renderMessages` 中 `emptyState` 读 `$("scope").hidden` —— T7 保证 `#scope` 存在且初始 hidden。
