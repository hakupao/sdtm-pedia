// 入口: 事件绑定 + 生成流程编排。渲染在 render.js, 存储在 store.js。
import { store, save, current, newConversation, deleteConversation, renameConversation,
         prefs, savePrefs, modelLabelById, HISTORY_TURNS } from "./js/store.js";
import { renderSidebar, renderMessages, messageEl, finalizeBubble, appendErr, appendRetry,
         attachTools, setSources, renderWebStatus, renderModelBadge, refreshModelBadgeLabels,
         renderContinuation, renderPdfPages, renderFirstAnswer,
         onToolCallUI, onToolResultUI } from "./js/render.js";
import { renderMarkdown } from "./js/markdown.js";
import { streamAsk } from "./js/stream.js";
import { renderDossierBadge } from "./js/dossier.js";
import { renderGroundingBadge, settleAnswer, historyFromMessages } from "./js/grounding.js";
import { $, initScrollFollow, initSettings, initSidebar, selectedCorpus, webEnabled,
         dossierMode, autoGrow } from "./js/ui.js";

// ── 渲染回调 (侧栏/消息需要的动作) ──
const sidebarHandlers = {
  onSelect: (id) => { store.currentId = id; save(); paintAll(); },
  onDelete: (id) => {
    // 删的正是在途那条 ⇒ 先掐流: 落点马上要被丢掉, 让 LLM 继续吐完只是白烧 token。
    if (busy && id === store.currentId) stop();
    deleteConversation(id);
    // 删到一条不剩 ⇒ 补一个空会话, 否则右边是块什么都没有的白板 (与启动时同一条规则)。
    if (!store.conversations.length) newConversation();
    paintAll();
  },
  onRename: (id, title) => { if (renameConversation(id, title)) renderSidebar(sidebarHandlers); },
};
const messageHandlers = {
  onPickExample: (q) => send(q),
  onRetry: (c) => retry(c),
};
function paintAll() { renderSidebar(sidebarHandlers); renderMessages(messageHandlers); }

const scroller = initScrollFollow($("messages"), $("to-bottom"));

// ── 发送 / 停止 / 重试 ──
let busy = false;
let currentAbort = null; // AbortController for the in-flight stream

function setSending(on) {
  const b = $("send");
  b.textContent = on ? "停止" : "发送";
  b.classList.toggle("stop", on);
  b.disabled = false; // stay clickable while streaming so it can Stop
  $("show-citations").disabled = on; // 生成中切换会触发整体重渲染, 抹掉在途气泡 (spec §5)
}
function stop() { if (currentAbort) currentAbort.abort(); }

async function send(text) {
  if (busy || !text.trim()) return;
  const c = current();
  c.messages.push({ role: "user", content: text });
  if (c.messages.length === 1) c.title = text.slice(0, 30);
  save(); paintAll();
  scroller.follow();
  await runGeneration(c);
}

// Re-run generation for the conversation's last user message (drops any failed/partial
// assistant turn first), without appending a duplicate user message.
function retry(c) {
  if (busy) return;
  while (c.messages.length && c.messages[c.messages.length - 1].role === "assistant") {
    c.messages.pop();
  }
  save(); renderMessages(messageHandlers);
  if (c.messages.some((m) => m.role === "user")) runGeneration(c);
}

async function runGeneration(c) {
  const lastUserIdx = c.messages.map((m) => m.role).lastIndexOf("user");
  if (lastUserIdx === -1) return;
  const text = c.messages[lastUserIdx].content;
  busy = true; setSending(true);

  const box = $("messages");
  const turn = messageEl({ role: "assistant", content: "" });
  box.appendChild(turn); scroller.scrollToBottom();
  const bubble = turn.querySelector(":scope > .bubble");

  // History = everything BEFORE the current question (excludes the last user msg), capped.
  // 只取 content: 答案闸重答过的消息, 没过核验的首轮存在 firstAnswer, 不进模型上下文。
  const history = historyFromMessages(c.messages, lastUserIdx, HISTORY_TURNS);

  let acc = "";
  let gotSources = null;
  let gotRouted = null;
  let gotWebStatus = null;
  let gotWebSearchesOk = null;
  let gotModelId = null;
  let gotVerified = null;
  let gotModelsUsed = null;
  let gotFellBack = null;
  let gotContinueRounds = null;
  let gotTruncated = null;
  let gotPdfPages = null;
  let gotPdfTrigger = null;
  let gotDossier = null;
  let gotGrounding = null;
  let firstAnswer = null;    // 答案闸 regenerate 时的首轮原文 (acc 随后从空开始装最终轮)
  let regenReasons = null;
  let lastVerdict = null;    // 最后一份 grounding 事件 (中断时合成「重答中断」判定用)
  let countFix = "";         // done.counting_correction: 重答失败还原首轮时要拼回去的计数闸修正
  let saved = false;
  let savedMsg = null;

  // ── 流式渲染: rAF 节流, 每帧最多一次全量 markdown 解析 (spec §4) ──
  // 旧版流中只 textContent 追加、done 后才渲染 —— 用户全程看裸 md 语法。全量重解析在
  // < 10 KB 文本上单次 < 2 ms, 不做增量 diff (YAGNI)。高亮只在 finalize 时跑一次 (流中会闪)。
  let dirty = false, rafId = 0;
  const paint = () => {
    rafId = 0;
    if (!dirty) return;
    dirty = false;
    try {
      bubble.innerHTML = renderMarkdown(acc, { streaming: true, showCitations: prefs.showCitations });
    } catch (_) {
      bubble.textContent = acc; // marked 理论上不抛; 真抛了也不能让流断掉
    }
    if (scroller.isFollowing()) scroller.scrollToBottom();
  };
  const renderFinal = (content) => {
    if (rafId) { cancelAnimationFrame(rafId); rafId = 0; }
    dirty = false;
    finalizeBubble(bubble, content);
    if (scroller.isFollowing()) scroller.scrollToBottom();
  };
  const persist = (content) => {
    if (saved) return;
    saved = true;
    savedMsg = { role: "assistant", content, sources: gotSources || [], routedCorpus: gotRouted,
                 webStatus: gotWebStatus, webSearchesOk: gotWebSearchesOk,
                 modelId: gotModelId, verified: gotVerified,
                 // 产物自证 (spec §6 / 2026-09-02 R5): 回退这件事必须活过刷新, 否则
                 // 存档里一条 DeepSeek 答的消息与 Opus 5 答的长得一模一样。
                 modelsUsed: gotModelsUsed, fellBack: gotFellBack,
                 // 同上: 被截断这件事必须活过刷新, 否则存档里半句话的答案与完整答案一样。
                 continueRounds: gotContinueRounds, truncated: gotTruncated,
                 // 同上 (C2R I2-4): 答案里「画面目視判読 p.NN」指的是哪几页, 只有这里记着;
                 // 不落盘的话刷新后那句出处就成了无从核对的孤证, ⚑ 也带不上页码上下文。
                 pdfPages: gotPdfPages, pdfTrigger: gotPdfTrigger,
                 // 第五次同一个坑 (DM2): 一条"整段吃了研读包"的答案与一条普通检索答案在
                 // 存档里必须长得不一样 —— 吃的是哪一版 (sha) 也只有这里记着。
                 dossier: gotDossier,
                 // 第六次: 研读包答案过没过确定性核验、重答过没有 (DM2 答案闸)。
                 grounding: gotGrounding,
                 // content 是最终轮; 没过核验的首轮单独存, 折叠展示且不进 history。
                 firstAnswer };
    c.messages.push(savedMsg);
    save(); renderSidebar(sidebarHandlers);
  };
  // 流结束时定下「这条消息的答案」: 重答失败 / 被中断 ⇒ 半截重答不作数, 还原首轮 (settleAnswer)。
  const settle = (interrupted) => {
    const r = settleAnswer({ acc, firstAnswer, grounding: gotGrounding, interrupted, lastVerdict,
                             correction: countFix });
    firstAnswer = r.firstAnswer;
    if (r.grounding !== gotGrounding) {   // 重答中断: 未过核验的首轮以「重答中断」琥珀徽章存档
      gotGrounding = r.grounding;
      renderGroundingBadge(turn, gotGrounding, gotDossier);
    }
    renderFirstAnswer(turn, firstAnswer, regenReasons);
    return r.content;
  };
  const fail = (msg) => { appendErr(bubble, msg); appendRetry(turn, () => retry(c)); };

  const ctrl = new AbortController();
  currentAbort = ctrl;
  try {
    await streamAsk({ question: text, history, corpus: selectedCorpus(), web: webEnabled(),
                      model: $("model-select").value, dossier: dossierMode() }, {
      // sources 事件先到 (done 之前), 研读包信息两处都发 —— 先收下这份, done 再覆盖:
      // 流被中断 (停止 / 连接断) 时 done 永远不来, 但答案已经吃过研读包了, 存档得说得出来。
      onSources: (s, routed, ev) => { gotSources = s; gotRouted = routed;
                                      gotDossier = (ev || {}).dossier ?? null;
                                      setSources(turn, s, routed); },
      onToken: (t) => { acc += t; dirty = true; if (!rafId) rafId = requestAnimationFrame(paint); },
      onToolCall: (d) => onToolCallUI(turn, d),
      onToolResult: (d) => onToolResultUI(turn, d),
      // 自动续写是服务端行为, 正文照旧从 token 事件流进同一个气泡 ⇒ 流中不画任何东西。
      // 留一条 debug 日志是为了排障时能看出"这条答案续写过", 而不是靠猜。
      onContinue: (d) => console.debug("auto-continue round", (d || {}).round),
      // 研读包答案闸: 每轮一个结论。记下最后一份 (重答中断时以它合成「重答中断」判定); 徽章等 done 汇总再画。
      onGrounding: (d) => { lastVerdict = d; console.debug("dossier grounding", d); },
      // 首轮已流完且没过核验: 挪进折叠区 + 分隔线, 气泡从空开始接第二轮。
      onRegenerate: (d) => { firstAnswer = acc; regenReasons = (d || {}).reasons ?? null; acc = "";
                             renderFirstAnswer(turn, firstAnswer, regenReasons);
                             dirty = true; if (!rafId) rafId = requestAnimationFrame(paint); },
      onDone: (data) => {
        gotWebStatus = (data || {}).web_status; gotWebSearchesOk = (data || {}).web_searches_ok;
        // ?? 只在 null/undefined 时取右值, false 会原样保留 —— 与 renderModelBadge 的
        // 三态语义 (spec §6) 保持一致: verified 缺失时按"未知"收, 不会误当成 false。
        gotModelId = (data || {}).model_id ?? null;
        gotVerified = (data || {}).verified ?? null;
        // 同一条 ?? 的理由: fell_back 的 false 是**确证没回退**, 不能被当成缺失塌成 null。
        // ⚠ 这两个字段原样收下、不做形状校验 —— 形状由 modelBadgeText 的 Array.isArray
        // 挡 (后端发个裸串就能让整段历史渲染不出来, 见那里的注释)。
        gotModelsUsed = (data || {}).models_used ?? null;
        gotFellBack = (data || {}).fell_back ?? null;
        renderWebStatus(turn, gotWebStatus, gotWebSearchesOk);
        gotContinueRounds = (data || {}).continue_rounds ?? null;
        gotTruncated = (data || {}).truncated ?? null;
        // C2R 画面 PDF 旁路: 两个字段同源同义, `?? null` 的理由同上 —— 但这里 null 与
        // 空数组**不能**混同 ("通道没动" vs "触发了却一页都没画出来", 后端 M4 裁定)。
        gotPdfPages = (data || {}).pdf_pages ?? null;
        gotPdfTrigger = (data || {}).pdf_trigger ?? null;
        // `?? gotDossier` 而不是 `?? null`: 老后端的 done 事件没这个键, 塌成 null 会把
        // sources 事件里已经收到的那份抹掉 (前端先于 Python 重启上线是常态)。
        gotDossier = (data || {}).dossier ?? gotDossier;
        // 研读包没挂时 done 里没有这个键 ⇒ null ⇒ 徽章不画。
        gotGrounding = (data || {}).grounding ?? null;
        countFix = (data || {}).counting_correction ?? "";
        renderModelBadge(turn, gotModelId, gotVerified, gotModelsUsed, gotFellBack);
        renderContinuation(turn, gotContinueRounds, gotTruncated);
        renderPdfPages(turn, gotPdfPages, gotPdfTrigger);
        renderDossierBadge(turn, gotDossier);
        renderGroundingBadge(turn, gotGrounding, gotDossier);
        const settled = settle(false);
        const content = settled.trim() ? settled : "(无内容)"; renderFinal(content); persist(content);
      },
      onError: (msg) => { const t = settle(true); if (t) { renderFinal(t); persist(t); } fail(msg); },
      // 干净 EOF 但无 done/error: 内容已在屏上, 落盘防刷新丢失 (规则 D HIGH 修复)。
      onClose: () => { const t = settle(true); if (t) { renderFinal(t); persist(t); fail("连接中断（已保留已生成内容）"); } else fail("连接中断"); },
      // 用户点「停止」: 保留已生成部分, 不报错样式, 给重试入口。
      onAbort: () => { const t = settle(true); if (t) { renderFinal(t); persist(t); } fail("已停止"); },
      signal: ctrl.signal,
    });
  } finally {
    busy = false; setSending(false); currentAbort = null;
    // attach the tools (复制 / ⚑) once the answer is final + persisted (skip if nothing saved)
    if (savedMsg) attachTools(turn, text, savedMsg);
  }
}

// ── topbar/设置: 显示后端真实 default_model + 联邦开关 + 模型下拉 (读 /api/info) ──
async function loadModelName() {
  try {
    const r = await fetch("/api/info");
    if (!r.ok) return; // not logged in / info unavailable -> keep static label, 选择器保持隐藏
    const info = await r.json();
    const m = (info.default_model || "").split("/").pop();
    const tm = $("topbar-model");
    if (m) { tm.dataset.defaultModel = m; tm.textContent = m; }
    // 联邦未构建时后端会静默忽略 corpus, 别留个无效控件在界面上
    $("scope").hidden = !info.federation;
    // 下拉从 /api/info 的模型表渲染 —— 与 Router 组同源, 故不可能提供后端没有的模型。
    const sel = $("model-select");
    (info.selectable_models || []).forEach((m) => {
      const o = document.createElement("option");
      o.value = m.id;
      // 未验证的在文字上标出来: 用户选之前就该看见, 而不是选完才知道
      o.textContent = m.verified ? m.label : `${m.label} ⚠未验证`;
      o.dataset.verified = String(m.verified);
      sel.appendChild(o);
      modelLabelById[m.id] = m.label; // 供 renderModelBadge 查表, 把历史消息里的原始 id 换成人话
    });
    // 刷新保留 —— 终审 I-E (联网状态过不了刷新) 的同款, 不重犯
    const saved = localStorage.getItem("sdtm_model");
    if (saved && [...sel.options].some((o) => o.value === saved)) sel.value = saved;
    const syncWarning = () => {
      const o = sel.selectedOptions[0];
      $("model-warning").hidden = !o || o.dataset.verified === "true";
      if (o) tm.textContent = modelLabelById[o.value] || o.value; // 顶栏显示当前所选模型
    };
    sel.addEventListener("change", () => {
      localStorage.setItem("sdtm_model", sel.value);
      syncWarning();
    });
    syncWarning();
    refreshModelBadgeLabels(); // 原地补字, 不重建 #messages (理由见函数注释)
    // 空状态的示例卡依赖 federation 才知道要不要显示 ST01 那张; 只在空会话时重画
    const c = store.conversations.find((x) => x.id === store.currentId);
    if (c && !c.messages.length && !busy) renderMessages(messageHandlers);
  } catch (_) {}
}

// ── 事件绑定 ──
$("new-chat").onclick = () => { newConversation(); paintAll(); $("input").focus(); };
$("composer").onsubmit = (e) => {
  e.preventDefault();
  if (busy) { stop(); return; } // button is in "停止" mode while streaming
  const v = $("input").value; $("input").value = ""; autoGrow($("input")); send(v);
};
$("input").addEventListener("keydown", (e) => {
  // IME 组字中 (中文拼音/日文假名等) 的回车是「上屏候选/确认」, 不能当发送。
  // isComposing 覆盖现代浏览器; keyCode===229 是组字态的传统兜底 (个别浏览器不置 isComposing)。
  if (e.key === "Enter" && !e.shiftKey && !e.isComposing && e.keyCode !== 229) {
    e.preventDefault();
    if (busy) return; // 生成中不用 Enter 触发停止 (避免误触); 停止请点按钮
    $("composer").requestSubmit();
  }
});
$("input").addEventListener("input", (e) => autoGrow(e.target));

initSettings($("settings-btn"), $("settings-panel"));
initSidebar({ sidebar: $("sidebar"), collapseBtn: $("collapse-side"), expandBtn: $("expand-side"), prefs, savePrefs });
$("show-citations").checked = prefs.showCitations;
$("show-citations").addEventListener("change", (e) => {
  prefs.showCitations = e.target.checked; savePrefs();
  if (!busy) renderMessages(messageHandlers); // busy 时控件是 disabled 的, 到不了这里
});

// ── 启动 ──
if (!store.conversations.length) newConversation();
paintAll();
loadModelName();
