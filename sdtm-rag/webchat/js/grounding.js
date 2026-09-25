// DM2 研读包答案的确定性核验 (server/dossier_gate.py): done 事件的 `grounding` / regenerate 事件
// → 徽章文案 + 分隔线 + ⚑ 存档行。纯文案与 DOM 分开 (同 js/dossier.js 的分工), 文案层才测得动。
//
// 后端三态:
//   键不在 / null            → 闸没跑 (研读包没挂, 或 index 缺)。**什么都不画**。
//   {final.ok:true, …}       → 过 (regenerated=true 时是重答后过, 首轮原因要说出来)。
//   {final.ok:false, …}      → 未过 (已重答仍不过 / 重答调用失败), 琥珀色 + 原因。
// ⚠ 形状校验全在这里: onDone 是 `?? null` 零校验, 这里一抛异常死的是整段对话历史的渲染。

function reasonsText(result) {
  const rs = result && Array.isArray(result.reasons)
    ? result.reasons.filter((r) => typeof r === "string" && r) : [];
  return rs.length ? rs.join("; ") : "原因未知";
}

export function groundingBadgeView(g) {
  if (!g || typeof g !== "object" || Array.isArray(g)) return null;
  const f = g.final;
  if (!f || typeof f !== "object" || Array.isArray(f)) return null;
  // 全等 true: 值经 JSON 往返 (localStorage / SSE) 到达, 字符串 "true" 不算过。
  if (f.ok === true) {
    if (g.regenerated === true) {
      return { text: `✓ 重答后通过确定性核验 (首次未过: ${reasonsText(g.first)})`, level: "ok" };
    }
    return { text: "✓ 确定性核验通过", level: "ok" };
  }
  let note = "";
  if (g.regenerated === true) note = " (已重答 1 次)";
  else if (typeof g.regenerate_error === "string" && g.regenerate_error) {
    note = ` (重答失败: ${g.regenerate_error})`;
  }
  return { text: `⚠ 未过确定性核验${note}: ${reasonsText(f)}`, level: "warn" };
}

// regenerate 事件 → 追加进正文 (acc) 的 markdown 分隔线。首轮答案已经流给用户了, 不能收回;
// 这条线是「上面那段没过核验、下面是重答」的诚实记录, 也随存档一起留下。
export function regenerateDividerText(d) {
  return `\n\n---\n\n> ⟳ 首次答案未过确定性核验: ${reasonsText(d)}, 重答中\n\n---\n\n`;
}

// ⚑ note 行。只留 ok / regenerated / reasons —— note 有 2000 上限, 额度优先留给用户原话。
export function groundingFlagLine(g) {
  if (!g || typeof g !== "object" || Array.isArray(g)) return "";
  const f = g.final;
  if (!f || typeof f !== "object" || Array.isArray(f)) return "";
  return `grounding: ${JSON.stringify({ ok: f.ok, regenerated: g.regenerated, reasons: f.reasons })}`;
}

// ⚠ 文案为 null 时在建任何元素之前就返回 (同 renderDossierBadge): 闸没跑时 DOM 一个空 div 都不留。
export function renderGroundingBadge(turn, g) {
  const old = turn.querySelector(":scope > .grounding-badge");
  if (old) old.remove();   // 历史重绘 + onDone 各调一次
  const view = groundingBadgeView(g);
  if (!view) return;
  const el = document.createElement("div");
  el.className = `grounding-badge ${view.level}`;
  el.title = "研读包答案的确定性核验: 引用的 EDC OID 是否都在一览中、答题语言是否与问句一致";
  el.textContent = view.text;
  // 紧跟研读包徽章 (说的是同一件事的成色); 没有就挂在 .turn-meta 之后。
  const anchor = turn.querySelector(":scope > .dossier-badge") || turn.querySelector(":scope > .turn-meta");
  if (anchor) anchor.insertAdjacentElement("afterend", el);
  else turn.appendChild(el);
}
