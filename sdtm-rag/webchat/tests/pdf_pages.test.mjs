import test from "node:test";
import assert from "node:assert/strict";
import { pdfAttachView, pdfPagesSummary, PDF_RULE_HINT } from "../js/pdfpages.js";

// ── 三态 (server/router.py maybe_attach_pdf_pages 的 M3/M4 裁定) ──

test("通道关/未触发: 两个字段都是 null ⇒ 什么都不画", () => {
  assert.equal(pdfAttachView(null, null), null);
  assert.equal(pdfAttachView(undefined, undefined), null);
});

test("附上了页: 每页一枚 chip + 规则文字 + 指回正文出处的提示", () => {
  const v = pdfAttachView([{ pdf: "annotated", page: 174 }, { pdf: "workflow", page: 315 }], "R1");
  assert.equal(v.mode, "pages");
  assert.equal(v.lead, "画面页附图");
  assert.deepEqual(v.chips, ["annotated p.174", "workflow p.315"]);
  assert.equal(v.rule, "规则 R1");
  // 提示必须把这一行和答案正文里的出处串起来, 否则用户不知道这些页码是干什么的
  assert.match(v.hint, /画面目視判読/);
  assert.match(v.hint, /^R1: /m);
});

test("触发了但一页都没画出来 (M4): 说出来, 不塌成 null", () => {
  const v = pdfAttachView([], "R2");
  assert.equal(v.mode, "none");
  assert.equal(v.lead, "画面页: 未附图 (渲染失败)");
  assert.deepEqual(v.chips, []);
  assert.equal(v.rule, "规则 R2");
  assert.match(v.hint, /^R2: /m);
});

test("空列表但没有规则名 ⇒ 仍然什么都不画 (老存档/老后端没有这两个键)", () => {
  assert.equal(pdfAttachView([], null), null);
});

test("规则名未知时不编造解释, 但规则本身照样报出来", () => {
  const v = pdfAttachView([{ pdf: "annotated", page: 7 }], "R9");
  assert.equal(v.rule, "规则 R9");
  assert.equal(v.hint.includes("R9:"), false);
  assert.equal(Object.keys(PDF_RULE_HINT).length, 3);
});

test("容器级契约: pdf_pages 不是数组时不抛 (整段历史渲染的性命系于此)", () => {
  assert.equal(pdfAttachView("annotated p.1", null), null);
  assert.equal(pdfAttachView({ pdf: "annotated" }, null), null);
  // 规则名在但形状坏了 ⇒ 按"没画出来"报, 而不是假装附了图
  assert.equal(pdfAttachView("annotated p.1", "R3").mode, "none");
});

// ── ⚑ 上报摘要 ──

test("摘要: 逗号连接; 无页时是空串", () => {
  assert.equal(pdfPagesSummary([{ pdf: "workflow", page: 315 }]), "workflow p.315");
  assert.equal(pdfPagesSummary([]), "");
  assert.equal(pdfPagesSummary(null), "");
  assert.equal(pdfPagesSummary("x"), "");
});

// ── flagNote: 页码并进 note, 但绝不把整条上报撑成 422 ──
// flag.js → store.js 在 import 时就读 localStorage (node 没有), 所以先装 shim 再动态 import。
globalThis.localStorage = {
  getItem: () => null,
  setItem: () => {},
  removeItem: () => {},
};
const { flagNote } = await import("../js/flag.js");

test("有页: 在用户原话后面追加一行 pdf_pages", () => {
  assert.equal(flagNote("答弱了", { pdfPages: [{ pdf: "annotated", page: 174 }] }),
               "答弱了\npdf_pages: annotated p.174");
});

test("用户没写备注时只发这一行, 不留空行", () => {
  assert.equal(flagNote("", { pdfPages: [{ pdf: "workflow", page: 9 }] }), "pdf_pages: workflow p.9");
});

test("没有页 (通道关 / 老存档): note 逐字节不变", () => {
  assert.equal(flagNote("答弱了", { pdfPages: null }), "答弱了");
  assert.equal(flagNote("答弱了", {}), "答弱了");
  assert.equal(flagNote("答弱了", null), "答弱了");
  assert.equal(flagNote("", null), "");
});

test("撑破服务端 note 上限时丢机器附注、保住用户原话 (否则整条 ⚑ 422 丢失)", () => {
  const long = "x".repeat(1995);
  assert.equal(flagNote(long, { pdfPages: [{ pdf: "annotated", page: 174 }] }), long);
  // 刚好装得下的边界: 1970 + "\n" + 29 字符的附注 = 2000
  const line = "pdf_pages: annotated p.174";
  const fits = "y".repeat(2000 - 1 - line.length);
  assert.equal(flagNote(fits, { pdfPages: [{ pdf: "annotated", page: 174 }] }), `${fits}\n${line}`);
});
