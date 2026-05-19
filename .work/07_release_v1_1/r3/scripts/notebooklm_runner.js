// SMOKE_V4 R3 — NotebookLM runner script
// Fire-and-forget. 注入前先把 __QUESTION_PLACEHOLDER__ 替换为实际题文.
// ⚠ NotebookLM 不能 navigate_page (会丢 chat 状态), 必须用 scripts/reset_notebooklm.js 内部 click "Delete chat history" 重置.
// ⚠ NotebookLM 比其他 3 平台多 30+s RAG 检索时间, max timeout 调到 180s.
// 结果存到 window.__SMOKE_NOTEBOOKLM_RESULT.

() => {
  const K = '__SMOKE_NOTEBOOKLM_RESULT';
  const QUESTION = `__QUESTION_PLACEHOLDER__`;
  window[K] = { p: 'notebooklm', q: QUESTION, status: 'starting', t0: Date.now(), events: [] };
  const W = window[K];
  const log = (k, d = {}) => W.events.push({ t: Date.now() - W.t0, k, ...d });
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const wF = async (fn, ms = 8000) => {
    const s = Date.now();
    while (Date.now() - s < ms) {
      try { const v = fn(); if (v) return v; } catch (e) {}
      await sleep(200);
    }
    return null;
  };
  const fill = (el, t) => {
    el.focus();
    if (el.tagName === 'TEXTAREA') {
      Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set.call(el, t);
      el.dispatchEvent(new Event('input', { bubbles: true }));
    } else {
      const r = document.createRange(); r.selectNodeContents(el);
      const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r);
      document.execCommand('insertText', false, t);
      el.dispatchEvent(new InputEvent('input', { bubbles: true }));
    }
  };
  // ⚠ 严格用 a11y label === "Query box", 避免误选 notebook 标题改名框 (那个 aria 是 notebook 名)
  const fI = () => {
    for (const c of document.querySelectorAll('textarea, [contenteditable="true"]')) {
      const aria = c.getAttribute('aria-label') || '';
      if (/^Query box$/i.test(aria)) return c;
    }
    return null;
  };
  const fSubmit = () =>
    Array.from(document.querySelectorAll('button')).find(b =>
      b.getAttribute('aria-label') === 'Submit'
    );
  const extract = () => {
    const els = document.querySelectorAll('.message-text-content');
    const last = els[els.length - 1];
    return last ? (last.textContent || '').trim() : '';
  };
  const countMsgs = () => document.querySelectorAll('.message-text-content').length;

  (async () => {
    try {
      // 1. Fill (用户必须先跑 reset_notebooklm.js)
      const i = await wF(fI);
      if (!i) { W.status = 'aborted'; W.abortReason = 'no_query_box'; return; }
      log('input_found', { tag: i.tagName, aria: i.getAttribute('aria-label') });
      const msgCountPre = countMsgs();
      W.msgCountPre = msgCountPre;

      fill(i, QUESTION);
      await sleep(500);
      const filledLen = (i.textContent || i.value || '').length;
      log('filled', { len: filledLen });
      if (filledLen < 3) { W.status = 'aborted'; W.abortReason = 'fill_failed'; return; }

      // 2. Submit (button is always present, but disabled when input empty; after fill it enables)
      const s = await wF(() => {
        const b = fSubmit();
        return b && !b.disabled ? b : null;
      }, 6000);
      if (!s) { W.status = 'aborted'; W.abortReason = 'submit_not_enabled'; return; }
      log('submit_found');
      s.click();
      log('submit_click');
      W.t_send = Date.now() - W.t0;

      // 3. Poll done signal: Submit button reappears with disabled=true (after RAG + streaming)
      // ⚠ NotebookLM 头 30+s 是 RAG 检索, 看似无反应; max 180s 给足
      const MAX_TICKS = 180;
      let doneTick = null;
      for (let j = 0; j < MAX_TICKS; j++) {
        await sleep(1000);
        const b = fSubmit();
        // Done = submit btn exists AND disabled AND message count increased
        if (b && b.disabled && countMsgs() > msgCountPre) {
          doneTick = j + 1; break;
        }
      }
      if (doneTick === null) { W.status = 'aborted'; W.abortReason = 'done_signal_timeout'; return; }
      log('done_signal', { tick: doneTick });

      // 4. Grace 3s for RAG streaming tail
      await sleep(3000);
      W.t_done = Date.now() - W.t0;

      // 5. Extract last message (assumed assistant since user msg added before this)
      const responseText = extract();
      log('extracted', { len: responseText.length });

      W.response = responseText;
      W.responseLen = responseText.length;
      W.totalMs = W.t_done;
      W.status = 'complete';
    } catch (err) {
      W.status = 'error';
      W.error = String(err);
    }
  })();

  return { p: 'notebooklm', dispatched: true, qPreview: QUESTION.slice(0, 40) };
}
