// SMOKE_V4 R3 — Gemini Gem reset script
// 在 runner 之前跑 (主 session select_page Gemini → evaluate_script(this), 等返回 status:ok 再注 runner).
// 做: 点 toolbar "New chat" → 等输入框 ready → 点 mode picker → 找 Pro 选项点 → 等菜单关 → 返回.
// 同步返回 (await-able): 不是 fire-and-forget, 主 session 等返回再继续.

async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const wF = async (fn, ms = 8000) => {
    const s = Date.now();
    while (Date.now() - s < ms) {
      try { const v = fn(); if (v) return v; } catch (e) {}
      await sleep(200);
    }
    return null;
  };

  try {
    // 1. Click "New chat" toolbar button (NOT the sidebar "New chat" link which goes to /app)
    // The toolbar one is button[aria-label="New chat"] inside main, near current Gem name
    // Sidebar's is a <link>; we want the <button>
    const newChatBtns = Array.from(document.querySelectorAll('button')).filter(b =>
      b.getAttribute('aria-label') === 'New chat'
    );
    if (!newChatBtns.length) return { status: 'aborted', reason: 'no_new_chat_button' };
    // Toolbar one is typically the first button (not sidebar link). Just click first.
    newChatBtns[0].click();
    await sleep(1500); // wait for new conversation to load

    // 2. Verify input box reappears
    const input = await wF(() => document.querySelector('[contenteditable="true"][aria-label*="prompt for Gemini"]'));
    if (!input) return { status: 'aborted', reason: 'input_not_back_after_new_chat' };

    // 3. Click mode picker
    const picker = await wF(() =>
      Array.from(document.querySelectorAll('button')).find(b => b.getAttribute('aria-label') === 'Open mode picker')
    );
    if (!picker) return { status: 'aborted', reason: 'no_mode_picker' };
    picker.click();
    await sleep(800);

    // 4. Find "Pro" menuitem (text starts with "Pro", not "Upgrade")
    const proItem = await wF(() =>
      Array.from(document.querySelectorAll('[role="menuitem"]')).find(i => {
        const t = (i.textContent || '').trim();
        return /^Pro\b/.test(t) && !/Upgrade/.test(t);
      })
    );
    if (!proItem) {
      // Close menu before bail
      document.body.click();
      return { status: 'aborted', reason: 'no_pro_menuitem' };
    }
    const proLabel = (proItem.textContent || '').slice(0, 60);
    proItem.click();
    await sleep(1200); // wait for menu close + mode switch

    return { status: 'ok', proLabel, inputReady: !!document.querySelector('[contenteditable="true"][aria-label*="prompt for Gemini"]') };
  } catch (err) {
    return { status: 'error', error: String(err) };
  }
}
