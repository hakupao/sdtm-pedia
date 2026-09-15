// DOM 渲染层: 侧栏 / 消息 / 元信息 chips / 来源 / 联网面板 / 空状态。
import { store, prefs, modelLabelById } from "./store.js";
import { renderMarkdown, highlightIn } from "./markdown.js";
import { copyText, flash, armDelete, inlineRename, $ } from "./ui.js";
import { flagButton } from "./flag.js";
import { pdfAttachView } from "./pdfpages.js";
import { renderDossierBadge } from "./dossier.js";

// Plan B 联邦: 库标签 (日文 UI)。map 里没有的值 (null / 未知) 一律不渲染徽章 —— 联邦关时零变化。
const CORPUS_LABEL = { cdisc: "標準", study: "本研究", both: "両方" };

const EXAMPLES = [
  { q: "AE 域中 AESER 与 AESEV 的区别是什么?", study: false },
  { q: "SUPPQUAL 什么情况下使用? 举一个 AE 的例子", study: false },
  { q: "--DTC 变量的 ISO 8601 部分日期 (只知道年月) 怎么写?", study: false },
  { q: "本研究 ST01 的 VS 域有哪些测试项?", study: true },
];

// ── 侧栏 ──
export function renderSidebar({ onSelect, onDelete, onRename }) {
  const ul = $("conv-list");
  ul.innerHTML = "";
  for (const c of store.conversations) {
    const li = document.createElement("li");
    if (c.id === store.currentId) li.className = "active";
    const t = document.createElement("span");
    t.className = "title";
    t.textContent = c.title || "新对话";
    t.title = "双击重命名";
    // e.detail > 1 = 双击的第二/三下: 不切会话。否则第一下 onSelect → renderSidebar 重建 <li>,
    // dblclick 落在已脱离文档的 span 上 (input 建在 DOM 外, focus 无效果), 重命名静默失效。
    t.onclick = (e) => { if (e.detail > 1) return; onSelect(c.id); };
    t.ondblclick = (e) => { e.preventDefault(); inlineRename(t, c.title || "新对话", (v) => onRename(c.id, v)); };
    const del = document.createElement("button");
    del.className = "del"; del.type = "button"; del.textContent = "✕"; del.title = "删除";
    del.onclick = (e) => { e.stopPropagation(); armDelete(del, () => onDelete(c.id)); };
    li.append(t, del);
    ul.appendChild(li);
  }
}

// ── 消息列表 ──
export function renderMessages({ onPickExample, onRetry }) {
  const box = $("messages");
  box.innerHTML = "";
  const c = store.conversations.find((x) => x.id === store.currentId);
  if (!c) return;
  if (!c.messages.length) { box.appendChild(emptyState(onPickExample)); return; }
  let lastUserQ = "";
  for (const m of c.messages) {
    const el = messageEl(m);
    if (m.role === "user") lastUserQ = m.content;
    else if (m.role === "assistant") attachTools(el, lastUserQ, m);
    box.appendChild(el);
  }
  box.scrollTop = box.scrollHeight;
}

function emptyState(onPick) {
  const wrap = document.createElement("div");
  wrap.className = "empty";
  const h = document.createElement("h1"); h.textContent = "SDTM 知识库助手";
  const p = document.createElement("p");
  p.textContent = "基于 CDISC SDTM IG / Model / 术语表的检索增强问答。回答附来源, 请以标准原文为准。";
  const grid = document.createElement("div"); grid.className = "examples";
  const federation = !$("scope").hidden;
  for (const ex of EXAMPLES) {
    if (ex.study && !federation) continue;
    const card = document.createElement("button");
    card.type = "button"; card.className = "example"; card.textContent = ex.q;
    card.onclick = () => onPick(ex.q);
    grid.appendChild(card);
  }
  wrap.append(h, p, grid);
  return wrap;
}

export function messageEl(m) {
  const turn = document.createElement("article");
  turn.className = "turn " + m.role;
  const b = document.createElement("div");
  b.className = "bubble" + (m.role === "assistant" ? " md" : "");
  if (m.role === "assistant") finalizeBubble(b, m.content);
  else b.textContent = m.content;
  turn.appendChild(b);
  if (m.role === "assistant") {
    const meta = document.createElement("div"); meta.className = "turn-meta";
    const slot = document.createElement("div"); slot.className = "sources-slot";
    const tools = document.createElement("div"); tools.className = "turn-tools";
    turn.append(meta, slot, tools);
    setSources(turn, m.sources, m.routedCorpus);
    // 刷新/切会话后复原联网状态。不复原的话, 一个"已降级为未联网"的 KB-only 答案
    // 和正常联网答案长得一模一样 (spec §7 点名的最骗人的失败模式)。
    renderWebStatus(turn, m.webStatus, m.webSearchesOk);
    // 同一个坑, spec §6: 只做 UI 标注(下拉旁边那行提示)的话, 对话存下来后这条信息就没了。
    renderModelBadge(turn, m.modelId, m.verified, m.modelsUsed, m.fellBack);
    // 第三次同一个坑: 一条"写到上限被截断"的答案与一条完整答案在存档里必须长得不一样。
    renderContinuation(turn, m.continueRounds, m.truncated);
    // 第四次: 一条"看过画面 PDF 才答出来"的答案与纯卡片答案在存档里也必须长得不一样 ——
    // 正文里那句「画面目視判読 p.NN」指向哪几页, 只有这一行说得出来 (M3)。
    renderPdfPages(turn, m.pdfPages, m.pdfTrigger);
    // 第五次 (DM2): 一条"整段吃了研读包"的答案与一条普通检索答案在存档里也必须长得不一样;
    // 手动关掉研读包这件事同理 —— 它是答案为何变薄的唯一线索。
    renderDossierBadge(turn, m.dossier);
  }
  return turn;
}

// 完整渲染 (非流式): markdown + 高亮 + 代码块复制钮
export function finalizeBubble(bubble, content) {
  bubble.innerHTML = renderMarkdown(content, { streaming: false, showCitations: prefs.showCitations });
  highlightIn(bubble);
  decorateCodeBlocks(bubble);
}

function decorateCodeBlocks(bubble) {
  bubble.querySelectorAll("pre").forEach((pre) => {
    if (pre.querySelector(".code-copy")) return;
    const btn = document.createElement("button");
    btn.type = "button"; btn.className = "code-copy"; btn.textContent = "复制";
    btn.onclick = async () => flash(btn, (await copyText(pre.querySelector("code")?.innerText ?? pre.innerText)) ? "已复制" : "复制失败");
    pre.appendChild(btn);
  });
}

export function appendErr(bubble, msg) {
  const e = document.createElement("div"); e.className = "err"; e.textContent = "⚠ " + msg;
  bubble.appendChild(e);
}
export function appendRetry(turn, onClick) {
  const btn = document.createElement("button");
  btn.type = "button"; btn.className = "retry"; btn.textContent = "重试";
  btn.onclick = onClick;
  turn.appendChild(btn);
}

// 工具条: 复制 Markdown (存档原文, 含出处) + ⚑
export function attachTools(turn, question, msgObj) {
  const tools = turn.querySelector(".turn-tools");
  if (!tools || tools.childElementCount) return;
  const copy = document.createElement("button");
  copy.type = "button"; copy.className = "tool-btn"; copy.textContent = "复制";
  copy.onclick = async () => flash(copy, (await copyText(msgObj.content || "")) ? "已复制" : "复制失败");
  tools.append(copy, flagButton(question, msgObj, tools));
}

// ── 元信息 chips ──
function chip(text, cls) {
  const s = document.createElement("span");
  s.className = "chip " + (cls || "");
  s.textContent = text;
  return s;
}
function metaBox(turn) { return turn.querySelector(":scope > .turn-meta"); }

// verified 三态不可混同 (spec §6): true 正常; false 是拿到确证的"验过且不通过";
// null (default 组不在 selectable_models 里, 没有 verified 概念) 一律显"未知",
// 绝不能落进 false 那支 (会把"没这个概念"误报成"验过且不通过")。
//
// 回退 (fellBack === true, 2026-09-02 spec §4.4) 优先于以上三态: 答案是**另一个(些)**
// 模型产的, 那么"用户选的那个验没验过"对这条消息不再成立 —— 拿 opus-5 的 verified: true
// 给一条 DeepSeek 答的消息背书, 就是终审 C-1 (⚑ 归错模型) 同族。琥珀色照挂: 回退是
// **已知的偏离**, 不是单纯的元数据缺失, 值得与"未验证模型"同级的视觉提示。
//
// modelsUsed 是**列表**: 联网多轮 / 流中途回退时一次回答可能有两个模型各写了一段,
// 只报一个就又变成半个真话了 (spec R6)。绝大多数情况长度为 1, 文案退化成单模型形态。
//
// ⚠ `fellBack === true` 用**全等**而非 truthy: 老后端不发这个字段 (StaticFiles 从工作树
// 现读 ⇒ 新前端会先于 Python 重启上线, spec §5 B1) 、老存档里也没有这个键, 两种情况都是
// undefined, 必须落回下面三态、文案与今天逐字相同。
export function modelBadgeText(modelId, verified, modelsUsed, fellBack) {
  const label = modelLabelById[modelId] || modelId;
  // ⚠ `Array.isArray` 不是洁癖: 只判 truthy + `.length` 挡不住**字符串** ("abc".length 是 3)
  // 也挡不住 array-like 对象 —— 两者都会走到 `.join` 上抛 TypeError, 而这一抛是在
  // `renderMessages` 里 ⇒ 死的不是一条徽章, 是**整段对话历史渲染不出来**。
  // 后端发回什么形状不由前端说了算 (onDone 是 `?? null`, 零形状校验), 所以这里必须自己挡。
  //
  // **容器级**契约到此为止, **元素级**的 (每个元素是非空串) 由后端保证:
  // `server/router.py` 收集处的 `if reported:` 只 append 真值串, 所以 `[null]` / `[""]`
  // 这类"说回退了却说不出回退到谁"的半个真话在生产上产不出来。
  // ⛔ 别在这里加 `filter(Boolean)` 之类的防御 —— 为不可达路径写防御, 下一个人会以为它可达。
  // 为什么容器级只需要这一个判断就够: 值必然经 JSON 往返 (localStorage / SSE), 到达时
  // 只可能是 null|bool|number|string|array|plain object 六种, `Array.isArray` 恰好把前五种
  // 全挡在外面 —— 这也是"`join` 被改写成别的东西"那类畸形同样不会抛的原因。
  if (fellBack === true && Array.isArray(modelsUsed) && modelsUsed.length) {
    return { text: `模型: ${label} → 实际 ${modelsUsed.join("、")}（已回退）· 验证状态未知`,
             unverified: true };
  }
  if (verified === true) return { text: `模型: ${label}`, unverified: false };
  if (verified === false) return { text: `模型: ${label} ⚠未验证`, unverified: true };
  return { text: `模型: ${label} · 验证状态未知`, unverified: false };
}

// 答案实际用的模型 (spec §6 产物自证)。modelId 为空 (生成中占位 / 未流完就中断 / 旧历史
// 记录没存这个字段) 时什么都不画 —— 比瞎猜一个模型名更诚实, 也避免占位阶段先画一个"未知"
// 徽章、done 后又叠一个真实徽章的重复渲染。
export function renderModelBadge(turn, modelId, verified, modelsUsed, fellBack) {
  if (!modelId) return;
  // 用户 turn 没有 .turn-meta 容器 —— 旧 app.js 靠 role !== "assistant" 分支不走到这里,
  // 拆成模块后调用方可能直接传进来, 缺容器时静默跳过而不是抛。
  const meta = metaBox(turn);
  if (!meta) return;
  const b = chip("", "model-meta");
  // 这四个值存进 dataset: /api/info 比首屏渲染慢一步是常态, label 表填好后
  // refreshModelBadgeLabels() 要能原地补字, 不能靠重建 DOM 拿到它们
  // (重建会抹掉正在生成、尚未进 c.messages 的那个气泡 —— 上一轮复审用 gate stub 复现过)。
  b.dataset.modelId = modelId;
  b.dataset.verified = String(verified); // "true" | "false" | "null"
  b.dataset.modelsUsed = JSON.stringify(modelsUsed || []);
  b.dataset.fellBack = String(fellBack);  // "true" | "false" | "null" | "undefined"(老存档)
  const { text, unverified } = modelBadgeText(modelId, verified, modelsUsed, fellBack);
  b.textContent = text;
  if (unverified) b.classList.add("unverified");
  meta.appendChild(b);
}

// loadModelName() 拿到 /api/info 的 label 表往往晚于首屏渲染, 此前画出的模型徽章只能显示
// 原始 id。这里只原地改文字, 不碰其余 DOM —— 尤其不能用 renderMessages() 整体重建: 一次
// 生成中的助手气泡是直接 appendChild 挂到 #messages 上的, 要等 onDone→persist() 之后才会
// 进 c.messages, 这个窗口内重建会把它整个抹掉(复审用 gate 住 /api/info + 卡流复现过)。
export function refreshModelBadgeLabels() {
  document.querySelectorAll(".model-meta").forEach((b) => {
    const modelId = b.dataset.modelId;
    if (!modelId) return;
    const verified = b.dataset.verified === "true" ? true : b.dataset.verified === "false" ? false : null;
    // 显式三路比较, 不用 truthy —— dataset 里存的是字符串, "false" 是 truthy 的
    const fellBack = b.dataset.fellBack === "true" ? true : b.dataset.fellBack === "false" ? false : null;
    let modelsUsed = [];
    // 坏数据不该让整条历史渲染崩掉 —— 拿不到就当"没有这个信息", 退回非回退文案
    try { modelsUsed = JSON.parse(b.dataset.modelsUsed || "[]"); } catch (_) { modelsUsed = []; }
    b.textContent = modelBadgeText(modelId, verified, modelsUsed, fellBack).text;
  });
}

// ── 输出触顶自动续写 (2026-09-08) ──
//
// 后端在模型报"被输出上限切断"时会自动回灌原文让它接着写, 所以正文本身是连续的, 用户
// **不需要**看到中间换过几次 API 调用。这里只呈现两件与答案成色有关的事:
//   continueRounds > 0 且没触顶 → 一枚安静的 chip (信息, 不是警告: 答案是完整的)
//   truncated === true          → 琥珀色警告行 (答案**可能不完整**, 这是必须说的)
// 两者互斥: 触顶时警告里已经含轮数, 再挂一枚 chip 是同一件事说两遍。
//
// ⚠ `truncated === true` 用全等而非 truthy, 与 `fellBack` 同一条理由: 老存档和老后端
// (StaticFiles 现读工作树 ⇒ 新前端会先于 Python 重启上线) 都没有这个键, undefined 必须
// 落回"什么都不画", 而不是被当成某种状态。
export function renderContinuation(turn, continueRounds, truncated) {
  const n = Number(continueRounds) || 0;
  if (truncated === true) {
    if (turn.querySelector(":scope > .turn-note.warn")) return;
    const note = document.createElement("div");
    note.className = "turn-note warn";
    note.textContent = `⚠ 已达自动续写上限 (${n} 轮), 回答可能不完整`;
    // 挂在气泡**正后方**而不是 turn 末尾: 警告说的是这段正文的成色, 隔着来源折叠区和
    // 工具条就读不出这层关系了。
    const bubble = turn.querySelector(":scope > .bubble");
    if (bubble) bubble.insertAdjacentElement("afterend", note);
    else turn.appendChild(note);
    return;
  }
  if (n <= 0) return;
  const meta = metaBox(turn);
  if (!meta || meta.querySelector(".chip.continue")) return;
  meta.appendChild(chip(`自动续写 ×${n}`, "continue"));
}

// ── C2R 画面 PDF 旁路 (I2-4) ──
//
// 三态语义与"什么都不画"的边界全在 js/pdfpages.js 的 pdfAttachView 里, 这里只负责画。
// ⚠ view 为 null 时**在建任何元素之前**就返回: 通道关 (默认) 时这条渲染路径必须与本功能
// 上线前逐字节相同, 一个空 div 都不留 —— 有人靠"页面上有没有这一行"判断开关开没开。
export function renderPdfPages(turn, pdfPages, pdfTrigger) {
  const view = pdfAttachView(pdfPages, pdfTrigger);
  if (!view) return;
  if (turn.querySelector(":scope > .pdf-attach")) return; // 历史重绘 + onDone 各调一次
  const row = document.createElement("div");
  // class 只从白名单取, 不拼服务端字符串 (同 corpusBadge)
  row.className = view.mode === "none" ? "pdf-attach empty" : "pdf-attach";
  const lead = document.createElement("span");
  lead.className = "pdf-lead";
  lead.textContent = view.lead;
  if (view.hint) lead.title = view.hint;
  row.appendChild(lead);
  for (const label of view.chips) row.appendChild(chip(label, "pdf-page"));
  if (view.rule) {
    const r = document.createElement("span");
    r.className = "pdf-rule";
    r.textContent = view.rule;
    if (view.hint) r.title = view.hint;
    row.appendChild(r);
  }
  // 紧跟 chips 行、在「来源」折叠区之前: 说的是这条答案的证据成色, 与 judgement/模型徽章同级。
  const meta = metaBox(turn);
  if (meta) meta.insertAdjacentElement("afterend", row);
  else turn.appendChild(row);   // 缺 .turn-meta 容器时不抛 (同 renderModelBadge)
}

// ── 来源 (SSE sources 事件) + 判定库 chip ──
export function setSources(turn, sources, routedCorpus) {
  const label = CORPUS_LABEL[routedCorpus];
  const meta = metaBox(turn);   // 同上: 缺 .turn-meta 时只跳过 chip, 来源该怎么处理还怎么处理
  if (label && meta) meta.appendChild(chip(`判定: ${label}`, "corpus"));
  if (!sources || !sources.length) return;
  const slot = turn.querySelector(":scope > .sources-slot");
  slot.innerHTML = "";
  slot.appendChild(sourcesEl(sources));
}

// 每条来源前缀的库徽章; src.corpus 为空/未知 (单库路径) 时返 null, 来源行与联邦前一致。
function corpusBadge(corpus) {
  const label = CORPUS_LABEL[corpus];
  if (!label) return null;
  const b = document.createElement("span");
  // class 只从白名单取, 不拼服务端字符串
  b.className = corpus === "study" ? "corpus-badge study" : "corpus-badge";
  b.textContent = label;
  return b;
}

function sourcesEl(sources) {
  const d = document.createElement("details");
  d.className = "sources";
  const s = document.createElement("summary");
  s.textContent = `来源 (${sources.length})`;
  d.appendChild(s);
  for (const src of sources) {
    const div = document.createElement("div");
    div.className = "src";
    const head = document.createElement("div"); head.className = "src-head";
    const badge = corpusBadge(src.corpus);
    if (badge) head.appendChild(badge);
    const name = document.createElement("b");
    name.textContent = src.source + (src.section ? ` — ${src.section}` : "");
    const sim = document.createElement("span"); sim.className = "sim";
    sim.textContent = `sim ${(src.similarity ?? 0).toFixed(3)}`;
    head.append(name, sim);
    const p = document.createElement("div"); p.className = "src-preview";
    p.textContent = src.text_preview || "";
    div.append(head, p);
    d.appendChild(div);
  }
  return d;
}

// ── 联网搜索过程面板 ──
// 搜索过程条: 网页版那种「看得见它在搜什么」的观感。没有这层, 勾了联网只会
// 看到卡住半分钟然后蹦出一段话 —— 那是超时的感觉, 不是联网的感觉。
// ⚠ 挂在 turn (气泡外层) 而非 bubble: 流中会整体替换气泡 innerHTML。
function ensureWebPanel(turn) {
  let p = turn.querySelector(":scope > .web-panel");
  if (!p) {
    p = document.createElement("div");
    p.className = "web-panel";
    turn.prepend(p);   // 搜索过程显示在答案上方
  }
  return p;
}

export function onToolCallUI(turn, d) {
  const row = document.createElement("div");
  row.className = "web-row";
  row.dataset.callId = d.id || "";
  row.textContent = `🔍 搜索 "${d.query || ""}"`;
  ensureWebPanel(turn).appendChild(row);
}

export function onToolResultUI(turn, d) {
  const p = ensureWebPanel(turn);
  // CSS.escape: tool id 来自模型返回, 不保证是合法选择器
  const sel = `.web-row[data-call-id="${CSS.escape(d.id || "")}"]`;
  const row = p.querySelector(sel);
  const note = document.createElement("span");
  note.className = "web-note";
  // tool_result.status 有 6 个值, 其中 bad_query/unknown_tool 是**模型**出错不是联网出错,
  // 措辞必须区分 —— 把模型的失误显示成"联网失败"会让人去查网络而不是查模型。
  note.textContent = {
    ok: ` — 找到 ${d.count} 个来源`,
    failed: " — 搜索失败",
    quota_exceeded: " — 已达搜索次数上限",
    disabled: " — 服务端未启用联网",
    bad_query: " — 跳过 (模型给出的查询无效)",
    unknown_tool: " — 跳过 (模型调用了不存在的工具)",
  }[d.status] || ` — ${d.status}`;
  (row || p).appendChild(note);
}

// web_status 落在 done 上: 勾了联网却静默降级是最骗人的失败模式, 必须显式说出来。
// ⚠ 契约以 Task 4 实现为准 (计划初稿只列了 3 个状态, 实测收口后是 6 个 + 一个计数):
//   web_status ∈ {ok, partial, failed, quota_exceeded, disabled, off}
//   web_searches_ok: int  —— 真正拿到结果的搜索次数 (bad_query/unknown_tool/quota/failed 不计)
// 三种"看起来正常其实没搜到"的情形必须分开说, 否则用户无从判断答案的成色。
export function renderWebStatus(turn, status, searchesOk) {
  if (!status || status === "off") return;
  // ok + 0 次成功检索: 联网开着、一次网都没打成 (模型净吐畸形工具调用能耗光轮数)
  const msg = status === "ok"
    ? (searchesOk > 0 ? null : "ℹ 已开启联网, 但本次未实际检索到内容, 以下回答基于知识库")
    : {
        partial: "⚠ 部分搜索失败, 联网参考可能不完整 (逐条状态见上方搜索过程)",
        failed: "⚠ 本次未联网: 搜索请求失败, 以下回答仅基于知识库",
        quota_exceeded: "⚠ 本次未联网: 已达搜索配额上限, 以下回答仅基于知识库",
        disabled: "⚠ 本次未联网: 服务端未启用联网, 以下回答仅基于知识库",
      }[status] || `⚠ 本次未联网 (${status})`;
  if (!msg) return;
  const warn = document.createElement("div");
  warn.className = status === "ok" ? "web-note-block" : "web-warn";
  warn.textContent = msg;
  ensureWebPanel(turn).appendChild(warn);
}
