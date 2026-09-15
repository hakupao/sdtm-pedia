// DM2 研读包 (study dossier): done / sources 事件的 `dossier` → 徽章文案 + 一行渲染。
// 纯判断与 DOM 分开 (同 js/pdfpages.js 的分工): render.js 要整套 DOM shim 才跑得起来,
// 文案这层单拆出来才测得动。
//
// 后端 (server/router.py maybe_attach_dossier) 的三态在这里必须原样保留:
//   null                      → 通道没跑 (总闸 dossier_enabled=false)。**什么都不画**:
//                               DOM 与本功能上线前逐字节相同 —— "默认不打扰"在前端的落点。
//   {attached:false, reason}  → 跑了但没挂。auto 没命中是常态, 安静收掉; 但
//                               reason="forced_off" 是**用户自己关的**, 必须说出来:
//                               不说的话"这题研读包没命中"与"这题我把研读包关了"在存档里
//                               长得一模一样, 而后者是解释答案为何变薄的唯一线索。
//   {attached:true, …}        → 挂上了。章数/字数/sha 是这条答案吃进了哪一版研读包的唯一
//                               记录 (sha 变 = 研读包内容变, 见 config.dossier_prt_sections)。
//
// ⚠ 形状校验全在这里: onDone 是 `?? null` 零校验, 这里一抛异常死的不是一行徽章, 是整段
// 对话历史渲染不出来 (同 pdfpages.js / modelBadgeText 的理由)。
export function dossierBadgeText(info) {
  if (!info || typeof info !== "object" || Array.isArray(info)) return null;
  // 全等 true: 值经 JSON 往返 (localStorage / SSE) 到达, 老存档里的 "true" 不是挂上了。
  if (info.attached === true) {
    const n = Array.isArray(info.sections) ? info.sections.length : 0;
    const chars = Number.isFinite(info.chars) ? info.chars.toLocaleString("en-US") : "?";
    return `📖 研读包 · ${n} 章 · ${chars} 字 · ${info.reason || "?"} · ${info.sha || "?"}`;
  }
  if (info.reason === "forced_off") return "📖 研读包 · 已手动关闭";
  return null;
}

// ⚠ 文案为 null 时**在建任何元素之前**就返回 (同 renderPdfPages): 通道没跑时这条渲染路径
// 必须与本功能上线前逐字节相同, 一个空 div 都不留。
export function renderDossierBadge(turn, info) {
  const old = turn.querySelector(":scope > .dossier-badge");
  if (old) old.remove();   // 历史重绘 + onDone 各调一次; 后者的 info 更全, 覆盖前者
  const text = dossierBadgeText(info);
  if (!text) return;
  const el = document.createElement("div");
  el.className = "dossier-badge";
  el.title = "本题跳过了 study 侧检索, 整段喂入 PRT 章节 + EDC 全项目一览";
  el.textContent = text;
  // 挂在 .turn-meta 之后 (同 renderPdfPages): 说的是这条答案的证据成色, 与模型徽章同级。
  // 直接 appendChild 会让实时流 (工具条还没挂) 与历史重绘 (工具条已在) 的位置不一致。
  const meta = turn.querySelector(":scope > .turn-meta");
  if (meta) meta.insertAdjacentElement("afterend", el);
  else turn.appendChild(el);   // 缺 .turn-meta 容器时不抛 (同 renderModelBadge)
}
