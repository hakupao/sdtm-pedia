import test from "node:test";
import assert from "node:assert/strict";
import { groundingBadgeView, regenerateDividerLabel, groundingFlagLine, settleAnswer, historyFromMessages }
  from "../js/grounding.js";

// ⛔ 只用虚构 OID。
const OK = { ok: true, unknown_oids: [], lang_expected: "zh", lang_observed: "zh", reasons: [] };
const BAD = { ok: false, unknown_oids: ["ITEM_Z9"], lang_expected: "zh", lang_observed: "ja",
              reasons: ["一览中不存在的 OID 1 个: ITEM_Z9", "答题语言 ja ≠ 问句语言 zh"] };

// ── 徽章: 过 / 重答后过 / 未过 + 原因 ──

test("null / 缺键 = 闸没跑 ⇒ 不画 (研读包没挂时 DOM 与上线前逐字节同)", () => {
  assert.equal(groundingBadgeView(null), null);
  assert.equal(groundingBadgeView(undefined), null);
});

test("首轮就过", () => {
  assert.deepEqual(groundingBadgeView({ final: OK, first: null, regenerated: false }),
                   { text: "✓ 确定性核验通过", level: "ok" });
});

test("重答后过: 首轮原因要说出来 (否则看不出这条答案重答过)", () => {
  assert.deepEqual(groundingBadgeView({ final: OK, first: BAD, regenerated: true }),
                   { text: "✓ 重答后通过确定性核验 (首次未过: 一览中不存在的 OID 1 个: ITEM_Z9; 答题语言 ja ≠ 问句语言 zh)",
                     level: "ok" });
});

test("未过 (已重答仍不过) ⇒ 琥珀色 + 原因", () => {
  assert.deepEqual(groundingBadgeView({ final: BAD, first: BAD, regenerated: true }),
                   { text: "⚠ 未过确定性核验 (已重答 1 次): 一览中不存在的 OID 1 个: ITEM_Z9; 答题语言 ja ≠ 问句语言 zh",
                     level: "warn" });
});

test("重答调用失败 ⇒ 未过 + 失败类名", () => {
  assert.deepEqual(groundingBadgeView({ final: BAD, first: null, regenerated: false,
                                        regenerate_error: "TimeoutError" }),
                   { text: "⚠ 未过确定性核验 (重答失败: TimeoutError): 一览中不存在的 OID 1 个: ITEM_Z9; 答题语言 ja ≠ 问句语言 zh",
                     level: "warn" });
});

test("畸形输入 ⇒ null 或降级, 绝不抛", () => {
  for (const g of ["junk", ["a"], 42, {}, { final: null }, { final: "x" }]) {
    assert.equal(groundingBadgeView(g), null);
  }
  assert.deepEqual(groundingBadgeView({ final: { ok: false, reasons: "nope" } }),
                   { text: "⚠ 未过确定性核验: 原因未知", level: "warn" });
  // ok 必须是真 true (JSON 往返后的 "true" 不算过)
  assert.equal(groundingBadgeView({ final: { ok: "true" } }).level, "warn");
});

// ── B2: 研读包挂了、闸却没跑 ⇒ 中性徽章 (不说的话「闸没跑」与「没挂研读包」长得一样) ──

test("挂上但 grounding 缺 ⇒ 核验未运行", () => {
  assert.deepEqual(groundingBadgeView(null, { attached: true }),
                   { text: "· 确定性核验未运行", level: "neutral" });
  assert.deepEqual(groundingBadgeView(undefined, { attached: true, reason: "forced_on" }),
                   { text: "· 确定性核验未运行", level: "neutral" });
  assert.equal(groundingBadgeView(null, { attached: false }), null);
  assert.equal(groundingBadgeView(null, { attached: "true" }), null);
  assert.equal(groundingBadgeView(null, null), null);
});

// ── B3: 首轮与最终轮分开存; 分隔线标签 ──

test("分隔线标签带原因; 缺失/畸形也照画", () => {
  assert.equal(regenerateDividerLabel(BAD.reasons),
               "⟳ 首次答案未过确定性核验: 一览中不存在的 OID 1 个: ITEM_Z9; 答题语言 ja ≠ 问句语言 zh · 以下为重答");
  assert.ok(regenerateDividerLabel(null).includes("原因未知"));
  assert.ok(regenerateDividerLabel([1, null]).includes("原因未知"));
});

test("settleAnswer: 没重答 ⇒ content = acc, 无 firstAnswer", () => {
  assert.deepEqual(settleAnswer({ acc: "A", firstAnswer: null, grounding: null }),
                   { content: "A", firstAnswer: null });
});

test("settleAnswer: 重答成功 ⇒ content = 最终轮, firstAnswer = 首轮", () => {
  assert.deepEqual(settleAnswer({ acc: "B", firstAnswer: "A",
                                  grounding: { final: OK, first: BAD, regenerated: true } }),
                   { content: "B", firstAnswer: "A" });
});

test("settleAnswer: 重答失败 / 被中断 ⇒ 半截重答不作数, content 还原成首轮", () => {
  assert.deepEqual(settleAnswer({ acc: "半截", firstAnswer: "A",
                                  grounding: { final: BAD, first: null, regenerated: false,
                                               regenerate_error: "RuntimeError" } }),
                   { content: "A", firstAnswer: null });
  assert.deepEqual(settleAnswer({ acc: "半截", firstAnswer: "A", grounding: null, interrupted: true }),
                   { content: "A", firstAnswer: null });
});

test("history 只取 content: 没过闸的首轮不进下一问的上下文", () => {
  const msgs = [
    { role: "user", content: "q1" },
    { role: "assistant", content: "B", firstAnswer: "A 带 ITEM_Z9", grounding: {} },
    { role: "user", content: "q2" },
  ];
  assert.deepEqual(historyFromMessages(msgs, 2, 10),
                   [{ role: "user", content: "q1" }, { role: "assistant", content: "B" }]);
  assert.deepEqual(historyFromMessages(msgs, 2, 1), [{ role: "assistant", content: "B" }]);
});

// ── ⚑ 存档行 ──

test("存档行只留 ok/regenerated/reasons", () => {
  assert.equal(groundingFlagLine({ final: BAD, first: BAD, regenerated: true }),
               `grounding: ${JSON.stringify({ ok: false, regenerated: true, reasons: BAD.reasons })}`);
  assert.equal(groundingFlagLine(null), "");
  assert.equal(groundingFlagLine({ final: null }), "");
});

globalThis.localStorage = { getItem: () => null, setItem: () => {}, removeItem: () => {} };
const { flagNote } = await import("../js/flag.js");

test("⚑ note 带 grounding 行 (在 dossier 行之后)", () => {
  const msg = { dossier: { attached: true, reason: "forced_on", sha: "abc" },
                grounding: { final: OK, first: null, regenerated: false } };
  assert.equal(flagNote("答弱了", msg),
               '答弱了\ndossier: {"attached":true,"reason":"forced_on","sha":"abc"}\n'
               + 'grounding: {"ok":true,"regenerated":false,"reasons":[]}');
  assert.equal(flagNote("x", {}), "x");
});
