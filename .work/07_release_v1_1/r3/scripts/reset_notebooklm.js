// SMOKE_V4 R3 — NotebookLM reset script
// 在 runner 之前跑 (NotebookLM 不能 navigate, 必须 in-page reset).
// 做: 点 "Chat options" → 点 "Delete chat history" menuitem → 处理 confirm dialog (若有) → 等 chat 清空 → 返回.
// ⚠ 首次跑前未实测 confirm dialog 结构 — 若 dialog 选择器不命中, 返回 {status:'partial', warn:'dialog_pending'}, 主 session 介入手处理 / take_snapshot + click 确认.
// 同步返回, 主 session 等返回再注 runner.

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
    // 1. Click "Chat options" button
    const chatOpts = Array.from(document.querySelectorAll('button')).find(b =>
      b.getAttribute('aria-label') === 'Chat options'
    );
    if (!chatOpts) return { status: 'aborted', reason: 'no_chat_options_button' };
    chatOpts.click();
    await sleep(1000);

    // 2. Find + click "Delete chat history" menuitem
    const deleteItem = await wF(() =>
      Array.from(document.querySelectorAll('[role="menuitem"]')).find(i =>
        /^Delete chat history/i.test((i.textContent || '').trim())
      )
    );
    if (!deleteItem) {
      // Close menu
      document.body.click();
      return { status: 'aborted', reason: 'no_delete_menuitem' };
    }
    const deleteText = (deleteItem.textContent || '').slice(0, 80);
    deleteItem.click();
    await sleep(1500); // wait for confirm dialog (if any) to appear

    // 3. Handle confirm dialog (best-effort, 首次需校准)
    // Common patterns: button "Delete" / "Confirm" / "Yes, delete" in a modal dialog
    const confirmBtn = await wF(() => {
      // Look in any dialog/modal first
      const dialogs = document.querySelectorAll('[role="dialog"], [role="alertdialog"], .mat-mdc-dialog-content');
      const scopes = dialogs.length ? Array.from(dialogs) : [document.body];
      for (const scope of scopes) {
        const btns = scope.querySelectorAll('button');
        for (const b of btns) {
          const txt = (b.textContent || '').trim();
          const aria = b.getAttribute('aria-label') || '';
          if (/^(Delete|Confirm|Yes,?\s*delete)$/i.test(txt) || /^(Delete|Confirm)/i.test(aria)) {
            return b;
          }
        }
      }
      return null;
    }, 3000);

    let confirmClicked = false;
    let warnDialog = null;
    if (confirmBtn) {
      confirmBtn.click();
      confirmClicked = true;
      await sleep(2000); // wait for delete to complete + chat area to reset
    } else {
      // Dialog 形态可能不同, 返 partial 让主 session 介入
      warnDialog = 'confirm_dialog_button_not_found';
    }

    // 4. Verify chat history cleared (no message bubbles, only auto-summary)
    const msgCount = document.querySelectorAll('.message-text-content').length;

    return {
      status: warnDialog ? 'partial' : 'ok',
      deleteText,
      confirmClicked,
      warnDialog,
      msgCountAfter: msgCount,
      inputReady: !!document.querySelector('textarea[aria-label="Query box"]')
    };
  } catch (err) {
    return { status: 'error', error: String(err) };
  }
}
