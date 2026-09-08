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
