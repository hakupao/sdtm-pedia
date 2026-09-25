// ⚑ dogfood 失败捕获 → POST /api/flag → dogfood_failures.md (append-only 优先级 backlog)。
import { save, modelLabelById } from "./store.js";
import { $ } from "./ui.js";
import { pdfPagesSummary } from "./pdfpages.js";
import { groundingFlagLine } from "./grounding.js";

// server/router.py `FlagRequest.note` 的上限。**不是**截断而是 422 ⇒ 用户点了 ⚑ 却什么都
// 没记下 (规则 B: backlog 是本项目最贵的数据)。
const NOTE_MAX = 2000;

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

// 装不下就丢这行机器附注, 保住用户的原话 —— 反过来 (为了页码让整条上报 422) 是本末倒置。
// 逐行判断而不是整块判断: 一行塞不下时另一行往往还塞得下, 没理由陪葬。
function appendLine(base, line) {
  const merged = base ? `${base}\n${line}` : line;
  return merged.length <= NOTE_MAX ? merged : base;
}

// DM2: 这条答案挂没挂研读包。挂了的话它的证据基础与普通检索答案根本不是一回事 (整段 PRT
// 章节 + EDC 一览, study 侧 chunks 全丢), 不写进 backlog 的话读的人无从解释答案为何厚/薄;
// 手动关掉 (forced_off) 同理 —— 那是用户自己的选择, 不是模型答弱了。
// ⛔ 不塞 sections/chars: note 有 2000 上限, 额度优先留给用户原话。
// 通道没跑 (null) / 老存档 (无此键) 时**不发这一行**: 无话可说时别占额度, 也别让"没有
// 这个信息"看起来像"通道确实没跑"。
function dossierLine(info) {
  if (!info || typeof info !== "object" || Array.isArray(info)) return "";
  return `dossier: ${JSON.stringify({ attached: info.attached, reason: info.reason, sha: info.sha })}`;
}

// C2R (I2-4) / DM2: 这条答案附过画面 PDF 页、挂过研读包的话, 把这些并进 note 一起上报。
// ⛔ 不新增请求字段: `FlagRequest` **没有** extra="forbid" (AskRequest 才有), 多发的键会被
// pydantic 静默丢掉 —— 那正是抽检脚本 v1 踩过的坑 (看着 200, 其实什么都没传到)。想让这些
// 真的落进 dogfood_failures.md, 唯一的去处就是既有的自由文本 note。
export function flagNote(note, msgObj) {
  let out = note || "";
  const summary = pdfPagesSummary(msgObj && msgObj.pdfPages);
  if (summary) out = appendLine(out, `pdf_pages: ${summary}`);
  const dossier = dossierLine(msgObj && msgObj.dossier);
  if (dossier) out = appendLine(out, dossier);
  // 研读包答案闸的结论 (过 / 重答后过 / 未过 + 原因): 读 backlog 的人要知道这条答案是否已被
  // 确定性核验标过, 否则会把闸已经抓到的问题当成新发现。闸没跑时不发这一行。
  const grounding = groundingFlagLine(msgObj && msgObj.grounding);
  if (grounding) out = appendLine(out, grounding);
  return out;
}

export async function postFlag(question, answer, note, msgObj) {
  const model = flagModelName(msgObj);
  try {
    const r = await fetch("/api/flag", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, answer, note: flagNote(note, msgObj), model }),
    });
    return r.ok;
  } catch (_) { return false; }
}
