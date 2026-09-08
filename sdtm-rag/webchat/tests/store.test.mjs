import test from "node:test";
import assert from "node:assert/strict";

// localStorage shim (node 没有); 必须在 import store.js 之前装好, 所以用动态 import。
const mem = new Map();
// 配额上限 (字节), 默认无限 ⇒ 前面几条测试的行为逐位不变; 最后一条把它调到能装两条会话的
// 大小, 好让 save() 的逐出分支真的跑起来 (浏览器的 QuotaExceededError 也是按字节判的)。
let quotaLimit = Infinity;
globalThis.localStorage = {
  getItem: (k) => (mem.has(k) ? mem.get(k) : null),
  setItem: (k, v) => {
    if (String(v).length > quotaLimit) {
      const e = new Error("quota exceeded"); e.name = "QuotaExceededError"; throw e;
    }
    mem.set(k, String(v));
  },
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

// save() 的 QuotaExceededError 分支: 存档是 newest-first (unshift), 爆配额时从**最老**的
// 开始逐出直到装得下, 而且**绝不能把异常抛回调用方** —— save() 就在流回调里被调用,
// 抛出去等于刚生成的答案连屏上都留不住 (store.js 那段注释说的正是这个)。
test("save() 爆配额 → 逐出最老的会话, 保留最新的, 且不抛", () => {
  S.store.conversations.length = 0;
  const oldest = S.newConversation(); oldest.title = "最老";
  const middle = S.newConversation(); middle.title = "中间";
  const newest = S.newConversation(); newest.title = "最新";
  // 每条塞一段填充, 让"条数"与"字节数"单调对应, 阈值才能精确卡在 2 条与 3 条之间
  for (const c of [oldest, middle, newest]) {
    c.messages.push({ role: "assistant", content: "x".repeat(300) });
  }
  // 阈值 = "只剩两条时的实际字节数", 用**同一条序列化路径**量出来, 不手写魔法常数
  const all = S.store.conversations;
  S.store.conversations = all.slice(0, 2);
  quotaLimit = JSON.stringify(S.store).length;
  S.store.conversations = all;

  assert.doesNotThrow(() => S.save());
  assert.equal(S.store.conversations.length, 2);                     // 逐出了最老的那条
  assert.deepEqual(S.store.conversations.map((c) => c.title), ["最新", "中间"]);
  const persisted = JSON.parse(mem.get("sdtm_chat_v1"));             // 落盘的也是逐出后的版本
  assert.deepEqual(persisted.conversations.map((c) => c.title), ["最新", "中间"]);
  quotaLimit = Infinity;
});
