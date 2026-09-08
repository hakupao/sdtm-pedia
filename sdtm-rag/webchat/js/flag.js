// ⚑ dogfood 失败捕获 → POST /api/flag → dogfood_failures.md (append-only 优先级 backlog)。
import { save, modelLabelById } from "./store.js";
import { $ } from "./ui.js";

export function flagButton(question, msgObj, mount) {
  const btn = document.createElement("button");
  btn.className = "tool-btn flag-btn"; btn.type = "button";
  if (msgObj && msgObj.flagged) {
    btn.textContent = "✓ 已记录"; btn.disabled = true; btn.classList.add("done");
  } else {
    btn.textContent = "⚑ 标记"; btn.onclick = () => openFlag(mount, btn, question, msgObj);
  }
  return btn;
}

function openFlag(mount, btn, question, msgObj) {
  if (mount.querySelector(".flag-box")) return; // already open
  btn.hidden = true;
  const box = document.createElement("div");
  box.className = "flag-box";
  const ta = document.createElement("textarea");
  ta.placeholder = "哪里答错/答弱? 期望是什么? (可留空)"; ta.rows = 2;
  const send = document.createElement("button"); send.textContent = "记录"; send.className = "flag-send"; send.type = "button";
  const cancel = document.createElement("button"); cancel.textContent = "取消"; cancel.className = "flag-cancel"; cancel.type = "button";
  cancel.onclick = () => { box.remove(); btn.hidden = false; };
  send.onclick = async () => {
    send.disabled = true; cancel.disabled = true; send.textContent = "...";
    const ok = await postFlag(question, msgObj ? msgObj.content : "", ta.value, msgObj);
    if (ok) {
      if (msgObj) { msgObj.flagged = true; save(); }
      box.remove();
      btn.textContent = "✓ 已记录"; btn.disabled = true; btn.classList.add("done"); btn.hidden = false;
    } else {
      send.disabled = false; cancel.disabled = false; send.textContent = "记录";
      if (!box.querySelector(".err")) {
        const e = document.createElement("span"); e.className = "err"; e.textContent = " 记录失败"; box.appendChild(e);
      }
    }
  };
  box.append(ta, send, cancel);
  mount.appendChild(box);
  ta.focus();
}

// 归因必须取**这一条答案实际用的模型** (msgObj.modelId, 由 done 事件落进历史存档)。
// topbar 文本是 /api/info 的 default_model, 与答题模型无关 —— 下拉可选模型之前"唯一
// 答题模型就是 default 组"成立, 所以拿它凑合是对的; 现在它会把 A 模型的捏造记到 B 头上,
// 而 dogfood_failures.md 是 append-only 的优先级 backlog, 错误写入即永久且无从回溯。
// modelId 缺失 (下拉上线前存的旧历史) 时才退回 topbar 文本: 那些记录确实产自 default 组。
export function flagModelName(msgObj) {
  const id = msgObj && msgObj.modelId;
  // 回退过 ⇒ 答案是 modelsUsed 里那些模型产的, **不是**用户选的那个。把 DeepSeek 的捏造
  // 记到 GPT-5.6 Sol 头上, 与终审 C-1 是同一个缺陷换了触发路径 (那次是切 topbar 文本,
  // 这次是读了 modelId 但答案不是它产的)。两边都写进去: backlog 的读者既要知道谁捏造的,
  // 也要知道当时选的是谁 —— 否则"为什么会用到这个模型"这条线索断了。
  // Array.isArray 的理由与 modelBadgeText 那处相同 (容器级契约; 元素级由 server/router.py
  // 收集处的 `if reported:` 保证, 那里只 append 真值串), 但**后果更重**: 这里抛出去的
  // 异常穿过 postFlag ⇒ 用户点了 ⚑ 却什么都没记下, 而 backlog 是 append-only 的 (规则 B)。
  // 缺陷本身把发现缺陷的渠道堵了。⛔ 同样别加 filter(Boolean): 那条路径不可达。
  if (msgObj && msgObj.fellBack === true && Array.isArray(msgObj.modelsUsed)
      && msgObj.modelsUsed.length) {
    return `${msgObj.modelsUsed.join("、")}（回退自 ${id ? (modelLabelById[id] || id) : "未知"}）`;
  }
  if (id) return modelLabelById[id] || id;   // 表没加载好就发原始 id, 归因照样正确
  // #topbar-model 显示的是 /api/info 的 default_model 短名 (loadModelName 填), 与老 topbar 语义一致
  return ($("topbar-model").dataset.defaultModel || "").trim() || null;
}

export async function postFlag(question, answer, note, msgObj) {
  const model = flagModelName(msgObj);
  try {
    const r = await fetch("/api/flag", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, answer, note, model }),
    });
    return r.ok;
  } catch (_) { return false; }
}
