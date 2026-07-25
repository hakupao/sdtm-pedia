export const TAU = Math.PI * 2;
export const CLASS_ORDER = ["Special-Purpose","Interventions","Events","Findings",
  "Findings About","Trial Design","Relationship","Study Reference"];
export const easeOutCubic = t => 1 - Math.pow(1 - t, 3);
export const lerp = (a, b, t) => a + (b - a) * t;

// 间距常量：均为"圆心到圆心"最小距离，按 节点直径 + 标签宽度 定，保证任何环上都不糊成一坨。
const SEP_DOM = 38;    // 总览 / 影响视图里的域节点 (r=9 + 2~4 字标签)
const SEP_EXP = 62;    // 网状探索里的域节点 (r=12~14 + 加粗标签)
const SEP_VAR = 30;    // 域钻取里的变量节点 (r=5, 纵向排)
const SEP_CODE = 42;   // 域钻取里的码表菱形 (r=9 + 6~7 字符标签)

// 环形排布：以最小间距反推每环容量, 半径不够就自动外扩一环——不再把 N 个点硬塞进固定弧长。
// 返回 [{item, r, ang}]，ang 以 dir0 为中心、总角宽 2*half（half=Math.PI 即整圈）。
function ringPack(items, { r0, dr, half, dir0, sep }) {
  const out = [];
  const full = half >= Math.PI - 1e-6;
  let i = 0, ring = 0;
  while (i < items.length) {
    const r = r0 + ring * dr;
    if (full) {                                   // 整圈：均分，间距天然 ≥ sep（半径已按数量放大）
      const cap = Math.min(items.length - i, Math.max(1, Math.floor(TAU * r / sep)));
      for (let j = 0; j < cap; j++, i++)
        out.push({ item: items[i], r, ang: dir0 + TAU * j / cap });
    } else {                                      // 扇区：按弧长步进、以 dir0 居中——小簇紧凑, 大簇才铺满
      const step = sep / r;
      // 可用半角 = 扇区半角 − 两侧各留半个 sep 的弧长留白(绝对量, 非比例)：
      // 半径越大留白角越小, 保证相邻类在任何半径上的实际间隙都 ≥ sep, 窄扇区不够宽就自动外推一环。
      const halfR = Math.max(step * 0.5, half - step / 2);
      const cap = Math.min(items.length - i, Math.max(1, Math.floor(2 * halfR / step) + 1));
      for (let j = 0; j < cap; j++, i++)
        out.push({ item: items[i], r, ang: dir0 + (j - (cap - 1) / 2) * step });
    }
    ring++;
  }
  return out;
}

// 结构总览：8 个类枢纽固定排在同一环上；每类的域占据自己那 1/8 扇区、由内向外分环。
// 扇区互不重叠 ⇒ 跨类永不撞车；环容量随半径增长 ⇒ 同类内也不会挤在一起。
export function positionOverview(view, vp) {
  const pos = {};
  const byClass = {};
  for (const n of view.nodes) if (n.type === "domain") (byClass[n.cls] ??= []).push(n);
  for (const k in byClass) byClass[k].sort((a, b) => a.label < b.label ? -1 : a.label > b.label ? 1 : 0);

  const base = Math.min(vp.width, vp.height);
  // 扇区宽度按成员数加权分配：Findings(21 域) 拿宽扇区少堆几环, 两三个域的类不摊薄成一条线。
  // 基数 10 = 保底扇区: 让 2 个域的类也有立足之地, 同时避免大类把小类挤成一条缝。
  const w = CLASS_ORDER.map(c => (byClass[c] || []).length + 10);
  const wSum = w.reduce((a, b) => a + b, 0);
  // 枢纽环半径：最窄扇区也要留够类名的横向空间(~110px), 否则相邻类名会叠字。
  const minSpan = TAU * Math.min(...w) / wSum;
  const R = Math.max(base * 0.22, 150, 110 / minSpan + 40);

  let acc = 0;
  CLASS_ORDER.forEach((cls, i) => {
    const span = TAU * w[i] / wSum;
    const ang = -Math.PI / 2 + acc + span / 2;        // 枢纽居于本扇区中线
    acc += span;
    const hx = R * Math.cos(ang), hy = R * Math.sin(ang);
    // 枢纽标签朝圆心内侧放，避开外侧的域环。
    pos["C:" + cls] = { x: hx, y: hy, lx: -34 * Math.cos(ang), ly: -34 * Math.sin(ang), mid: 1 };
    for (const s of ringPack(byClass[cls] || [],
        { r0: R + 58, dr: SEP_DOM, half: span / 2, dir0: ang, sep: SEP_DOM }))
      pos[s.item.id] = { x: s.r * Math.cos(s.ang), y: s.r * Math.sin(s.ang) };
  });
  return pos;
}

// 域钻取：左→右分层轨道——域(左) → 变量(中，按列高上限自动分列) → 码表(右)。
// 列宽按变量名实际宽度给足，标签不再左右相撞。
export function positionDomain(view) {
  const pos = {};
  const vars = view.nodes.filter(n => n.type === "var");
  const codes = view.nodes.filter(n => n.type === "code");
  const domain = view.nodes.find(n => n.type === "domain");
  const maxRows = 22, colW = 150;
  const cols = Math.max(1, Math.ceil(vars.length / maxRows));
  const per = Math.ceil(vars.length / cols) || 1;
  vars.forEach((v, i) => {
    const c = Math.floor(i / per), r = i % per;
    const colH = (Math.min(per, vars.length - c * per) - 1) * SEP_VAR;
    pos[v.id] = { x: c * colW, y: -colH / 2 + r * SEP_VAR };
  });
  const xCode = (cols - 1) * colW + 200, cH = (codes.length - 1) * SEP_CODE;
  codes.forEach((k, i) => pos[k.id] = { x: xCode, y: -cH / 2 + i * SEP_CODE });
  if (domain) pos[domain.id] = { x: -200, y: 0 };
  return pos;
}

// 码表影响：枢纽居中，被波及的域按类分组、整圈分环——环容量同样由最小间距推出。
export function positionImpact(view, vp) {
  const pos = {};
  const hub = view.nodes.find(n => n.type === "code");
  const doms = view.nodes.filter(n => n.type === "domain").sort((a, b) =>
    (CLASS_ORDER.indexOf(a.cls) - CLASS_ORDER.indexOf(b.cls)) || (a.label < b.label ? -1 : 1));
  if (hub) pos[hub.id] = { x: 0, y: 0 };
  const base = Math.min(vp.width, vp.height);
  const r0 = Math.max(base * 0.24, 140);
  for (const s of ringPack(doms, { r0, dr: 46, half: Math.PI, dir0: -Math.PI / 2, sep: SEP_DOM }))
    pos[s.item.id] = { x: s.r * Math.cos(s.ang), y: s.r * Math.sin(s.ang) };
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

// fresh 进入 / 换种子 / 整理：种子居中，按 BFS 深度分环；环半径同时受深度和"这一环塞得下"约束。
export function positionExploreFresh(view, vp, { seedId }) {
  const pos = {}, adj = adjacency(view), depth = new Map([[seedId, 0]]), q = [seedId];
  while (q.length) { const u = q.shift();
    for (const v of (adj.get(u) || [])) if (!depth.has(v)) { depth.set(v, depth.get(u) + 1); q.push(v); } }
  const byDepth = {};
  for (const n of view.nodes) { const d = depth.has(n.id) ? depth.get(n.id) : 1;
    (byDepth[d] ??= []).push(n.id); }
  const base = Math.min(vp.width, vp.height);
  pos[seedId] = { x: 0, y: 0 };
  let prevR = 0;
  for (const d of Object.keys(byDepth).map(Number).sort((a, b) => a - b)) {
    if (d === 0) continue;
    const ids = byDepth[d].slice().sort();
    // 环半径 = max(按深度的名义半径, 该环节点数所需的最小周长, 上一环 + 最小环距)
    const rr = Math.max(base * 0.20 * d, SEP_EXP * ids.length / TAU, prevR + SEP_EXP * 1.6);
    ids.forEach((id, i) => { const ang = -Math.PI / 2 + TAU * i / ids.length;
      pos[id] = { x: rr * Math.cos(ang), y: rr * Math.sin(ang) }; });
    prevR = rr;
  }
  return pos;
}

// 点击展开：prevPos 中的已有节点原位不动；新节点落在 anchor 周围的空角度槽——防止"点一下到处飞"。
// 槽位半径按新节点数量放大，保证同一圈上的新邻居彼此至少隔 SEP_EXP。
export function positionExploreAccumulate(view, vp, { prevPos, anchorId }) {
  const pos = {};
  for (const n of view.nodes) if (prevPos[n.id]) pos[n.id] = { ...prevPos[n.id] };
  const newNodes = view.nodes.filter(n => !prevPos[n.id]).map(n => n.id).sort();
  const a = prevPos[anchorId] || { x: 0, y: 0 };
  const r = Math.max(120, SEP_EXP * Math.max(1, newNodes.length) / TAU);
  const minAng = Math.min(0.9, SEP_EXP / r);          // 角度间隔 ≈ 弧长 SEP_EXP
  const near = Object.values(pos).filter(p => Math.hypot(p.x - a.x, p.y - a.y) < r * 1.8);
  const occupied = near.map(p => Math.atan2(p.y - a.y, p.x - a.x));
  const isFree = ang => occupied.every(o => Math.abs(((ang - o + Math.PI) % TAU) - Math.PI) > minAng);
  const slots = Math.max(8, Math.ceil(TAU / minAng));
  let placed = 0;
  for (let k = 0; k < slots * 3 && placed < newNodes.length; k++) {
    const lap = Math.floor(k / slots);
    const ang = -Math.PI / 2 + TAU * (k % slots) / slots + lap * minAng * 0.5;
    const rr = r + lap * SEP_EXP;                     // 一圈放不下就外推一圈，而不是硬挤
    if (lap === 0 && !isFree(ang)) continue;
    pos[newNodes[placed++]] = { x: a.x + rr * Math.cos(ang), y: a.y + rr * Math.sin(ang) };
    if (lap === 0) occupied.push(ang);
  }
  for (; placed < newNodes.length; placed++) {        // 兜底：仍未放下的排最外环
    const ang = TAU * placed / newNodes.length;
    const rr = r + 3 * SEP_EXP;
    pos[newNodes[placed]] = { x: a.x + rr * Math.cos(ang), y: a.y + rr * Math.sin(ang) };
  }
  return pos;
}
