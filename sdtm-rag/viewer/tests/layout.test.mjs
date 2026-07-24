import { test } from "node:test";
import assert from "node:assert/strict";
import { easeOutCubic, lerp, positionOverview, CLASS_ORDER } from "../layout.mjs";

const VP = { width: 1200, height: 800 };
function overviewView() {
  const nodes = [];
  for (const c of CLASS_ORDER) nodes.push({ id: "C:" + c, type: "class", label: c, cls: c });
  // 每类给 3 个域，Findings 给 10 个（压密度）
  for (const c of CLASS_ORDER) {
    const k = c === "Findings" ? 10 : 3;
    for (let i = 0; i < k; i++) nodes.push({ id: `D:${c.replace(/[^A-Za-z]/g, "")}${i}`, type: "domain", label: `${c[0]}${i}`, cls: c });
  }
  return { nodes, edges: [] };
}

test("easing/lerp 边界", () => {
  assert.equal(easeOutCubic(0), 0);
  assert.equal(easeOutCubic(1), 1);
  assert.equal(lerp(10, 20, 0.5), 15);
});

test("overview: 8 个类枢纽等距排在同一环上", () => {
  const p = positionOverview(overviewView(), VP);
  const rs = CLASS_ORDER.map(c => Math.hypot(p["C:" + c].x, p["C:" + c].y));
  for (const r of rs) assert.ok(Math.abs(r - rs[0]) < 1e-6, "hub 半径应相等");
});

test("overview: 每个域离本类枢纽比离其他任何枢纽都近", () => {
  const view = overviewView();
  const p = positionOverview(view, VP);
  for (const n of view.nodes.filter(x => x.type === "domain")) {
    const own = Math.hypot(p[n.id].x - p["C:" + n.cls].x, p[n.id].y - p["C:" + n.cls].y);
    for (const c of CLASS_ORDER) if (c !== n.cls) {
      const other = Math.hypot(p[n.id].x - p["C:" + c].x, p[n.id].y - p["C:" + c].y);
      assert.ok(own < other, `${n.id} 应最靠近本类 ${n.cls}`);
    }
  }
});

test("overview: 纯函数——两次调用完全一致", () => {
  const v = overviewView();
  assert.deepEqual(positionOverview(v, VP), positionOverview(v, VP));
});
