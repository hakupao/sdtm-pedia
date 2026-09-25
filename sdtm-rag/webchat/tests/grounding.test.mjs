import test from "node:test";
import assert from "node:assert/strict";
import { groundingBadgeView, regenerateDividerText, groundingFlagLine } from "../js/grounding.js";

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

// ── regenerate 分隔线 (进 acc, 以 markdown 画出来; 首轮答案已在屏上, 这条线是诚实记录) ──

test("分隔线带原因", () => {
  const t = regenerateDividerText({ reasons: BAD.reasons });
  assert.ok(t.startsWith("\n\n---\n\n"));
  assert.ok(t.includes("首次答案未过确定性核验: 一览中不存在的 OID 1 个: ITEM_Z9; 答题语言 ja ≠ 问句语言 zh, 重答中"));
  assert.ok(t.endsWith("\n\n---\n\n"));
});

test("分隔线: 原因缺失/畸形也照画 (线本身比原因要紧)", () => {
  assert.ok(regenerateDividerText(null).includes("首次答案未过确定性核验: 原因未知, 重答中"));
  assert.ok(regenerateDividerText({ reasons: [1, null] }).includes("原因未知"));
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
