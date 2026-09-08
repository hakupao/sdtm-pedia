// 会话存储 (localStorage) + UI 偏好 + 模型 label 注册表。不碰 DOM。
export const LS_KEY = "sdtm_chat_v1";
export const PREFS_KEY = "sdtm_ui_prefs";
export const HISTORY_TURNS = 10; // 控 token: 发给后端的最近消息条数

// 模型 id → label 表, loadModelName() 拿到 /api/info 后填。页面刚打开、表还是空的时候历史
// 徽章会退化显示原始 id (不影响正确性), loadModelName 填完表后会原地补字。
export const modelLabelById = {};

// uid 不用 crypto.randomUUID (LAN http 非安全上下文不可用)
export const uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 8);

function load() {
  try {
    const s = JSON.parse(localStorage.getItem(LS_KEY));
    if (s && Array.isArray(s.conversations)) return s;
  } catch (_) {}
  return { conversations: [], currentId: null };
}
export const store = load();

export function save() {
  try {
    localStorage.setItem(LS_KEY, JSON.stringify(store));
  } catch (_) {
    // QuotaExceededError: store is newest-first (unshift), so evict the oldest conversations
    // until it fits — never let a storage failure throw into a stream callback (would lose the
    // just-generated answer and, before the try/finally below, brick the send button).
    while (store.conversations.length > 1) {
      store.conversations.pop();
      try { localStorage.setItem(LS_KEY, JSON.stringify(store)); return; } catch (_) {}
    }
  }
}

export function current() {
  let c = store.conversations.find((x) => x.id === store.currentId);
  if (!c) { c = newConversation(); }
  return c;
}
export function newConversation() {
  const c = { id: uid(), title: "新对话", createdAt: Date.now(), messages: [] };
  store.conversations.unshift(c);
  store.currentId = c.id;
  save();
  return c;
}
// 只改数据; 渲染由调用方 (app.js) 负责
export function deleteConversation(id) {
  store.conversations = store.conversations.filter((x) => x.id !== id);
  if (store.currentId === id) store.currentId = store.conversations[0]?.id ?? null;
  save();
}
export function renameConversation(id, title) {
  const t = (title || "").trim();
  const c = store.conversations.find((x) => x.id === id);
  if (!t || !c) return false;
  c.title = t;
  save();
  return true;
}

// ── UI 偏好 (与会话存档分开存, 清一个不影响另一个) ──
const DEFAULT_PREFS = { showCitations: false, sidebarCollapsed: false };
export function loadPrefs() {
  try {
    const p = JSON.parse(localStorage.getItem(PREFS_KEY));
    if (p && typeof p === "object") return { ...DEFAULT_PREFS, ...p };
  } catch (_) {}
  return { ...DEFAULT_PREFS };
}
export const prefs = loadPrefs();
export function savePrefs() {
  try { localStorage.setItem(PREFS_KEY, JSON.stringify(prefs)); } catch (_) {}
}
