// SMOKE_V4 R3 — Gemini Gem runner script
// Fire-and-forget. 注入前先把 __QUESTION_PLACEHOLDER__ 替换为实际题文.
// Selector 来自 dry-run 2026-05-19 evidence.
// 调用前提: 主 session 已先跑 reset_gemini.js (New chat + Pro mode) 或者当前 conversation 即是 fresh.
// 结果存到 window.__SMOKE_GEMINI_RESULT, 收集时 select_page + evaluate_script(() => window.__SMOKE_GEMINI_RESULT).

() => {
  const K = '__SMOKE_GEMINI_RESULT';
  const QUESTION = `__QUESTION_PLACEHOLDER__`;
  window[K] = { p: 'gemini', q: QUESTION, status: 'starting', t0: Date.now(), events: [] };
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
    const r = document.createRange(); r.selectNodeContents(el);
    const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r);
    document.execCommand('insertText', false, t);
    el.dispatchEvent(new InputEvent('input', { bubbles: true }));
  };
  const fI = () =>
    document.querySelector('[contenteditable="true"][aria-label*="prompt for Gemini"]') ||
    document.querySelector('[contenteditable="true"]');
  const fS = () =>
    Array.from(document.querySelectorAll('button')).find(b =>
      b.getAttribute('aria-label') === 'Send message' && !b.disabled
    );
  const extract = () => {
    const els = document.querySelectorAll('model-response');
    const last = els[els.length - 1];
    return last ? (last.textContent || '').trim() : '';
  };

  (async () => {
    try {
      // 1. Fill question
      const i = await wF(fI);
      if (!i) { W.status = 'aborted'; W.abortReason = 'no_input'; return; }
      fill(i, QUESTION);
      await sleep(500);
      const filledLen = (i.textContent || '').length;
      log('filled', { len: filledLen });
      if (filledLen < 3) { W.status = 'aborted'; W.abortReason = 'fill_failed'; return; }

      // 2. Send
      const s = await wF(fS, 6000);
      if (!s) { W.status = 'aborted'; W.abortReason = 'no_send'; return; }
      log('send_found', { aria: s.getAttribute('aria-label') });
      s.click();
      log('send_click');
      W.t_send = Date.now() - W.t0;

      // 3. Poll done signal: Send button reappears + !disabled (Gemini 生成中 send btn 完全消失)
      const MAX_TICKS = 120;
      let doneTick = null;
      for (let j = 0; j < MAX_TICKS; j++) {
        await sleep(1000);
        if (fS()) { doneTick = j + 1; break; }
      }
      if (doneTick === null) { W.status = 'aborted'; W.abortReason = 'done_signal_timeout'; return; }
      log('done_signal', { tick: doneTick });

      // 4. Grace 2s for streaming tail
      await sleep(2000);
      W.t_done = Date.now() - W.t0;

      // 5. Extract response
      const responseText = extract();
      log('extracted', { len: responseText.length });

      W.response = responseText;
      W.responseLen = responseText.length;
      W.totalMs = W.t_done;
      W.status = 'complete';
    } catch (err) {
      W.status = 'error';
      W.error = String(err);
      W.stack = err.stack;
    }
  })();

  return { p: 'gemini', dispatched: true, qPreview: QUESTION.slice(0, 40) };
}
