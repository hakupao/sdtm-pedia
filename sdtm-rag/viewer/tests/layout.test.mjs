import { test } from "node:test";
import assert from "node:assert/strict";
import { easeOutCubic, lerp, positionOverview, CLASS_ORDER, positionDomain, positionImpact, positionExploreFresh, positionExploreAccumulate } from "../layout.mjs";

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

function impactView(nDoms) {
  const nodes = [{ id: "K:C66742", type: "code", label: "C66742" }];
  for (let i = 0; i < nDoms; i++)
    nodes.push({ id: `D:d${i}`, type: "domain", label: `d${i}`, cls: CLASS_ORDER[i % CLASS_ORDER.length] });
  return { nodes, edges: [] };
}
test("impact: 枢纽在中心", () => {
  const p = positionImpact(impactView(10), VP);
  assert.ok(Math.hypot(p["K:C66742"].x, p["K:C66742"].y) < 1e-6);
});
test("impact: 单环时所有域到中心等距", () => {
  const p = positionImpact(impactView(10), VP);
  const rs = Array.from({length:10},(_,i)=>Math.hypot(p[`D:d${i}`].x, p[`D:d${i}`].y));
  for (const r of rs) assert.ok(Math.abs(r - rs[0]) < 1e-6);
});
test("impact: 纯函数", () => {
  const v = impactView(20);
  assert.deepEqual(positionImpact(v, VP), positionImpact(v, VP));
});

function ring1View() {
  return { nodes: [{id:"D:TU",type:"domain",label:"TU"},{id:"D:TR",type:"domain",label:"TR"},
                    {id:"D:RS",type:"domain",label:"RS"},{id:"D:PR",type:"domain",label:"PR"}],
           edges: [{s:"D:TU",t:"D:TR",layer:"flow"},{s:"D:TU",t:"D:RS",layer:"hard"},
                   {s:"D:TU",t:"D:PR",layer:"cooc"}] };
}
test("exploreFresh: 种子居中", () => {
  const p = positionExploreFresh(ring1View(), VP, { seedId: "D:TU" });
  assert.ok(Math.hypot(p["D:TU"].x, p["D:TU"].y) < 1e-6);
});
test("exploreFresh: 一跳邻居等距成环", () => {
  const p = positionExploreFresh(ring1View(), VP, { seedId: "D:TU" });
  const rs = ["D:TR","D:RS","D:PR"].map(id => Math.hypot(p[id].x, p[id].y));
  for (const r of rs) assert.ok(Math.abs(r - rs[0]) < 1e-6);
});
test("exploreAccumulate: 已有节点位置不变，新节点落 anchor 附近", () => {
  const prevPos = { "D:TU": {x:0,y:0}, "D:TR": {x:100,y:0} };
  const view = { nodes:[{id:"D:TU"},{id:"D:TR"},{id:"D:MI"},{id:"D:RS"}],
                 edges:[{s:"D:TR",t:"D:MI",layer:"flow"},{s:"D:TR",t:"D:RS",layer:"hard"}] };
  const p = positionExploreAccumulate(view, VP, { prevPos, anchorId: "D:TR" });
  assert.deepEqual(p["D:TU"], {x:0,y:0});
  assert.deepEqual(p["D:TR"], {x:100,y:0});
  for (const id of ["D:MI","D:RS"])
    assert.ok(Math.hypot(p[id].x - 100, p[id].y - 0) < 200, `${id} 应落 anchor TR 附近`);
});
test("explore: 纯函数", () => {
  const v = ring1View();
  assert.deepEqual(positionExploreFresh(v, VP, {seedId:"D:TU"}), positionExploreFresh(v, VP, {seedId:"D:TU"}));
});
