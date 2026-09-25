import test from "node:test";
import assert from "node:assert/strict";
import { dossierBadgeText } from "../js/dossier.js";

// ── 三态 (server/router.py maybe_attach_dossier 的裁定, 与 pdf 通道同一条纪律) ──

test("null = 通道没跑 ⇒ 不画徽章", () => {
  assert.equal(dossierBadgeText(null), null);
  assert.equal(dossierBadgeText(undefined), null);
});

test("挂上了: 章数 + 字数 + 触发理由 + sha", () => {
  assert.equal(dossierBadgeText({ attached: true, reason: "auto:domain+scope", sha: "abc",
                                  sections: ["4.1", "4.2"], chars: 123456 }),
               "📖 研读包 · 2 章 · 123,456 字 · auto:domain+scope · abc");
});

test("跑了但没挂 ⇒ 安静, 不是徽章", () => {
  assert.equal(dossierBadgeText({ attached: false, reason: "auto:no_match", sha: "abc",
                                  sections: [], chars: 0 }), null);
});

test("手动关掉 ⇒ 说出来 (用户的选择必须在存档里看得见)", () => {
  assert.equal(dossierBadgeText({ attached: false, reason: "forced_off", sha: "abc",
                                  sections: [], chars: 0 }), "📖 研读包 · 已手动关闭");
});

test("畸形输入 ⇒ null, 绝不抛 (整段历史渲染的性命系于此)", () => {
  assert.equal(dossierBadgeText("junk"), null);
  assert.equal(dossierBadgeText(["a"]), null);
  assert.equal(dossierBadgeText(42), null);
  assert.equal(dossierBadgeText({}), null);
});

test("attached 必须是真 true: 老存档的字符串 \"true\" 不算挂上了", () => {
  assert.equal(dossierBadgeText({ attached: "true", reason: "forced_on", sections: [], chars: 1 }), null);
});

test("attached 但 sections/chars 形状坏了 ⇒ 降级报数, 仍不抛", () => {
  assert.equal(dossierBadgeText({ attached: true, reason: "forced_on", sha: "abc",
                                  sections: "4.1", chars: "many" }),
               "📖 研读包 · 0 章 · ? 字 · forced_on · abc");
  assert.equal(dossierBadgeText({ attached: true }), "📖 研读包 · 0 章 · ? 字 · ? · ?");
});

// ── ⚑ 上报: 研读包这件事必须进 backlog (答案为何厚/薄的唯一线索) ──
// flag.js → store.js 在 import 时就读 localStorage (node 没有), 所以先装 shim 再动态 import。
globalThis.localStorage = { getItem: () => null, setItem: () => {}, removeItem: () => {} };
const { flagNote } = await import("../js/flag.js");

test("挂上了: 在用户原话后追加一行 dossier (只留 attached/reason/sha)", () => {
  assert.equal(
    flagNote("答弱了", { dossier: { attached: true, reason: "auto:domain+scope", sha: "abc",
                                    sections: ["4", "5"], chars: 10 } }),
    '答弱了\ndossier: {"attached":true,"reason":"auto:domain+scope","sha":"abc"}');
});

test("跑了没挂也要写 (「没命中」与「用户关了」是两件事)", () => {
  assert.equal(flagNote("", { dossier: { attached: false, reason: "forced_off", sha: "abc" } }),
               'dossier: {"attached":false,"reason":"forced_off","sha":"abc"}');
});

test("通道没跑 / 老存档: note 逐字节不变", () => {
  assert.equal(flagNote("答弱了", { dossier: null }), "答弱了");
  assert.equal(flagNote("答弱了", {}), "答弱了");
  assert.equal(flagNote("答弱了", null), "答弱了");
  assert.equal(flagNote("答弱了", { dossier: "junk" }), "答弱了");
});

test("两条机器附注逐行判断: 撑破上限的丢掉, 装得下的照留", () => {
  const msg = { pdfPages: [{ pdf: "annotated", page: 174 }],
                dossier: { attached: true, reason: "forced_on", sha: "abc" } };
  const pdfLine = "pdf_pages: annotated p.174";
  const dLine = 'dossier: {"attached":true,"reason":"forced_on","sha":"abc"}';
  assert.equal(flagNote("答弱了", msg), `答弱了\n${pdfLine}\n${dLine}`);
  // 只装得下 pdf 那行时 dossier 那行丢掉, 但 pdf 行不陪葬
  const tight = "y".repeat(2000 - 1 - pdfLine.length);
  assert.equal(flagNote(tight, msg), `${tight}\n${pdfLine}`);
  // 两行都装不下 ⇒ 保住用户原话
  const full = "y".repeat(1995);
  assert.equal(flagNote(full, msg), full);
});

test("auto 暂停且本题命中 ⇒ 说出来并指路手动开", () => {
  assert.equal(dossierBadgeText({ attached: false, reason: "auto:paused", sha: "abc",
                                  sections: [], chars: 0 }),
               "📖 研读包 · 自动挂载暂停中 (本题命中; 需要时选「研读:开」)");
});
