import { test } from "node:test";
import assert from "node:assert/strict";
import { easeOutCubic, lerp, positionOverview, CLASS_ORDER, positionDomain } from "../layout.mjs";

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

function domainView(nVars) {
  const nodes = [{ id: "D:AE", type: "domain", label: "AE", cls: "Events" }];
  for (let i = 0; i < nVars; i++) nodes.push({ id: `V:v${i}`, type: "var", label: `v${i}` });
  nodes.push({ id: "K:C1", type: "code", label: "C1" }, { id: "K:C2", type: "code", label: "C2" });
  return { nodes, edges: [] };
}
test("domain: 三层 x 严格递增(域<变量<码表)", () => {
  const p = positionDomain(domainView(5), VP);
  const xVar = p["V:v0"].x, xCode = p["K:C1"].x, xDom = p["D:AE"].x;
  assert.ok(xDom < xVar && xVar < xCode, "x 应 域<变量<码表");
});
test("domain: 变量超阈值分两列", () => {
  const p = positionDomain(domainView(30), VP);
  const xs = new Set(Array.from({length:30},(_,i)=>p[`V:v${i}`].x));
  assert.equal(xs.size, 2, "30 变量应占 2 个 x 列");
});
test("domain: 纯函数", () => {
  const v = domainView(12);
  assert.deepEqual(positionDomain(v, VP), positionDomain(v, VP));
});
