// 与业务无关的交互原语。不 import 本地模块。
export const $ = (id) => document.getElementById(id);

// ── 复制: LAN http 下 navigator.clipboard 不存在 (非安全上下文), 退回 execCommand ──
export async function copyText(text) {
  try {
    if (navigator.clipboard?.writeText) { await navigator.clipboard.writeText(text); return true; }
  } catch (_) {}
  try {
    const ta = document.createElement("textarea");
    ta.value = text; ta.setAttribute("readonly", "");
    ta.style.cssText = "position:fixed;left:-9999px;top:0;opacity:0";
    document.body.appendChild(ta); ta.select();
    const ok = document.execCommand("copy");
    ta.remove();
    return ok;
  } catch (_) { return false; }
}

// 按钮短暂显示反馈文字后复原
export function flash(btn, text, ms = 1200) {
  const orig = btn.dataset.orig ?? btn.textContent;
  btn.dataset.orig = orig;
  btn.textContent = text;
  clearTimeout(btn._flashT);
  btn._flashT = setTimeout(() => { btn.textContent = orig; }, ms);
}

// ── 两步删除: 第一次点 → 变「确认删除」(danger), ms 内再点才真删, 超时复原 ──
export function armDelete(btn, onConfirm, { label = "确认删除", ms = 3000 } = {}) {
  if (btn.dataset.armed === "1") { onConfirm(); return; }
  const orig = btn.textContent;
  btn.dataset.armed = "1"; btn.textContent = label; btn.classList.add("armed");
  btn._armT = setTimeout(() => {
    btn.dataset.armed = ""; btn.textContent = orig; btn.classList.remove("armed");
  }, ms);
}

// ── 行内重命名 ──
export function inlineRename(titleEl, currentTitle, onCommit) {
  if (titleEl.querySelector("input")) return;
  const input = document.createElement("input");
  input.type = "text"; input.value = currentTitle; input.className = "rename-input";
  input.maxLength = 60;
  let done = false;
  const finish = (commit) => {
    if (done) return; done = true;
    const v = input.value;
    input.remove();
    titleEl.textContent = currentTitle;
    if (commit) onCommit(v);
  };
  input.addEventListener("keydown", (e) => {
    if (e.isComposing || e.keyCode === 229) return; // IME 组字中的回车不算提交
    if (e.key === "Enter") { e.preventDefault(); finish(true); }
    else if (e.key === "Escape") { e.preventDefault(); finish(false); }
  });
  input.addEventListener("blur", () => finish(true));
  input.addEventListener("click", (e) => e.stopPropagation());
  titleEl.textContent = "";
  titleEl.appendChild(input);
  input.focus(); input.select();
}

// ── 滚动跟随: 用户上滚 > 80px 就停止自动到底, 出现「回到底部」; 滚回底部或点按钮恢复 ──
export function initScrollFollow(box, toBottomBtn) {
  let following = true;
  const distance = () => box.scrollHeight - box.scrollTop - box.clientHeight;
  const scrollToBottom = () => { box.scrollTop = box.scrollHeight; };
  const sync = () => { toBottomBtn.hidden = following; };
  box.addEventListener("scroll", () => {
    following = distance() < 80;
    sync();
  });
  toBottomBtn.addEventListener("click", () => { following = true; scrollToBottom(); sync(); });
  sync();
  return {
    isFollowing: () => following,
    follow: () => { following = true; scrollToBottom(); sync(); },
    scrollToBottom,
  };
}

// ── 设置弹层: 点齿轮开关, 点面板外关闭, Esc 关闭 ──
export function initSettings(btn, panel) {
  const close = () => { panel.hidden = true; btn.setAttribute("aria-expanded", "false"); };
  const open = () => { panel.hidden = false; btn.setAttribute("aria-expanded", "true"); };
  btn.addEventListener("click", (e) => { e.stopPropagation(); panel.hidden ? open() : close(); });
  panel.addEventListener("click", (e) => e.stopPropagation());
  document.addEventListener("click", () => { if (!panel.hidden) close(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !panel.hidden) close(); });
}

// ── 侧栏折叠 (记进 prefs) ──
export function initSidebar({ sidebar, collapseBtn, expandBtn, prefs, savePrefs }) {
  const apply = () => {
    sidebar.classList.toggle("collapsed", prefs.sidebarCollapsed);
    expandBtn.hidden = !prefs.sidebarCollapsed;
  };
  collapseBtn.addEventListener("click", () => { prefs.sidebarCollapsed = true; savePrefs(); apply(); });
  expandBtn.addEventListener("click", () => { prefs.sidebarCollapsed = false; savePrefs(); apply(); });
  apply();
}

// 检索范围 checkbox → 后端 corpus 字面量 (auto|cdisc|study|both)。
// 两个都不勾 = auto: 交给 LLM 判库 (federation.decide_corpus), 与改 checkbox 前的默认行为一致。
export function selectedCorpus() {
  const cdisc = $("scope-cdisc").checked, study = $("scope-study").checked;
  if (cdisc && study) return "both";
  if (cdisc) return "cdisc";
  if (study) return "study";
  return "auto";
}
// 联网是与 corpus 正交的第四维: 只决定挂不挂 web_search 工具, 不参与判库。
export function webEnabled() { return $("scope-web").checked; }

export function autoGrow(ta) { ta.style.height = "auto"; ta.style.height = Math.min(ta.scrollHeight, 200) + "px"; }
