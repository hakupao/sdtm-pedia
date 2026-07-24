export const TAU = Math.PI * 2;
export const CLASS_ORDER = ["Special-Purpose","Interventions","Events","Findings",
  "Findings About","Trial Design","Relationship","Study Reference"];
export const easeOutCubic = t => 1 - Math.pow(1 - t, 3);
export const lerp = (a, b, t) => a + (b - a) * t;

// 结构总览：8 个类枢纽固定排在同一环上，各类的域成朝外楔形簇。
export function positionOverview(view, vp) {
  const pos = {};
  const R = Math.min(vp.width, vp.height) * 0.30;   // 枢纽环半径
  const byClass = {};
  for (const n of view.nodes) if (n.type === "domain") (byClass[n.cls] ??= []).push(n);
  for (const k in byClass) byClass[k].sort((a, b) => a.label < b.label ? -1 : a.label > b.label ? 1 : 0);
  const hub = {};
  CLASS_ORDER.forEach((cls, i) => {
    const ang = -Math.PI / 2 + TAU * i / CLASS_ORDER.length;
    hub[cls] = { x: R * Math.cos(ang), y: R * Math.sin(ang), ang };
    pos["C:" + cls] = { x: hub[cls].x, y: hub[cls].y };
  });
  const perRing = 6, halfW = 0.42;
  for (const cls of CLASS_ORDER) {
    const doms = byClass[cls] || [], h = hub[cls];
    doms.forEach((d, j) => {
      const ring = Math.floor(j / perRing), inRing = j % perRing;
      const count = Math.min(perRing, doms.length - ring * perRing);
      const spread = count > 1 ? (inRing / (count - 1) - 0.5) * 2 * halfW : 0;
      const rr = 46 + ring * 30, a2 = h.ang + spread;
      pos[d.id] = { x: h.x + rr * Math.cos(a2), y: h.y + rr * Math.sin(a2) };
    });
  }
  return pos;
}

// 域钻取：左→右分层轨道——域(左) → 变量(中，超阈值分两列) → 码表(右)。
export function positionDomain(view, vp) {
  const pos = {};
  const vars = view.nodes.filter(n => n.type === "var");
  const codes = view.nodes.filter(n => n.type === "code");
  const domain = view.nodes.find(n => n.type === "domain");
  const x0 = -vp.width * 0.28, x1 = 0, x2 = vp.width * 0.30, gap = 34, maxCol = 24;
  const cols = vars.length > maxCol ? 2 : 1, per = Math.ceil(vars.length / cols) || 1;
  vars.forEach((v, i) => {
    const c = Math.floor(i / per), r = i % per;
    const colH = (Math.min(per, vars.length - c * per) - 1) * gap;
    pos[v.id] = { x: x1 + c * 70, y: -colH / 2 + r * gap };
  });
  const cH = (codes.length - 1) * gap;
  codes.forEach((k, i) => pos[k.id] = { x: x2, y: -cH / 2 + i * gap });
  if (domain) pos[domain.id] = { x: x0, y: 0 };
  return pos;
}

// 码表影响：枢纽居中，被波及的域绕环分组排列。
export function positionImpact(view, vp) {
  const pos = {};
  const hub = view.nodes.find(n => n.type === "code");
  const doms = view.nodes.filter(n => n.type === "domain").sort((a, b) =>
    (CLASS_ORDER.indexOf(a.cls) - CLASS_ORDER.indexOf(b.cls)) || (a.label < b.label ? -1 : 1));
  if (hub) pos[hub.id] = { x: 0, y: 0 };
  const base = Math.min(vp.width, vp.height), R = base * 0.34, per = 28;
  doms.forEach((d, i) => {
    const ring = Math.floor(i / per), inRing = i % per;
    const count = Math.min(per, doms.length - ring * per);
    const ang = -Math.PI / 2 + TAU * inRing / count, rr = R + ring * base * 0.14;
    pos[d.id] = { x: rr * Math.cos(ang), y: rr * Math.sin(ang) };
  });
  return pos;
}

// 网状探索：BFS 分环（fresh）/ 锚定累积（accumulate）——两者共用的邻接表。
function adjacency(view) {
  const adj = new Map();
  for (const n of view.nodes) adj.set(n.id, []);
  for (const e of view.edges) {
    if (adj.has(e.s) && adj.has(e.t)) { adj.get(e.s).push(e.t); adj.get(e.t).push(e.s); }
  }
  return adj;
}

// fresh 进入 / 换种子 / 整理：种子居中，按 BFS 深度分环等距排布。
export function positionExploreFresh(view, vp, { seedId }) {
  const pos = {}, adj = adjacency(view), depth = new Map([[seedId, 0]]), q = [seedId];
  while (q.length) { const u = q.shift();
    for (const v of (adj.get(u) || [])) if (!depth.has(v)) { depth.set(v, depth.get(u) + 1); q.push(v); } }
  const byDepth = {};
  for (const n of view.nodes) { const d = depth.has(n.id) ? depth.get(n.id) : 1;
    (byDepth[d] ??= []).push(n.id); }
  const base = Math.min(vp.width, vp.height);
  pos[seedId] = { x: 0, y: 0 };
  for (const d in byDepth) {
    if (d === "0") continue;
    const ids = byDepth[d].slice().sort(), rr = base * 0.22 * Number(d);
    ids.forEach((id, i) => { const ang = -Math.PI / 2 + TAU * i / ids.length;
      pos[id] = { x: rr * Math.cos(ang), y: rr * Math.sin(ang) }; });
  }
  return pos;
}

// 点击展开：prevPos 中的已有节点原位不动；新节点落在 anchor 周围的空角度槽——防止"点一下到处飞"。
export function positionExploreAccumulate(view, vp, { prevPos, anchorId }) {
  const pos = {};
  for (const n of view.nodes) if (prevPos[n.id]) pos[n.id] = { ...prevPos[n.id] };
  const newNodes = view.nodes.filter(n => !prevPos[n.id]).map(n => n.id).sort();
  const a = prevPos[anchorId] || { x: 0, y: 0 }, r = 90;
  const occupied = Object.values(pos).map(p => Math.atan2(p.y - a.y, p.x - a.x));
  const isFree = ang => occupied.every(o => Math.abs(((ang - o + Math.PI) % TAU) - Math.PI) > 0.35);
  let placed = 0;
  for (let k = 0; k < 64 && placed < newNodes.length; k++) {
    const ang = -Math.PI / 2 + TAU * k / 16 + Math.floor(k / 16) * 0.2;
    if (!isFree(ang)) continue;
    pos[newNodes[placed++]] = { x: a.x + r * Math.cos(ang), y: a.y + r * Math.sin(ang) };
    occupied.push(ang);
  }
  for (; placed < newNodes.length; placed++) {           // 兜底：仍未放下的排外环
    const ang = TAU * placed / newNodes.length;
    pos[newNodes[placed]] = { x: a.x + (r + 60) * Math.cos(ang), y: a.y + (r + 60) * Math.sin(ang) };
  }
  return pos;
}
