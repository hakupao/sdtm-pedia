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
