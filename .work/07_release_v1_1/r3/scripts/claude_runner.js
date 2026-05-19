// SMOKE_V4 R3 — Claude Project runner script
// Fire-and-forget. 注入前先 sed __QUESTION_PLACEHOLDER__ 替换为实际题文.
// 前提: 主 session 已 navigate_page 到 project URL (回 landing), conversation fresh.
// 结果存到 window.__SMOKE_CLAUDE_RESULT.

() => {
  const K = '__SMOKE_CLAUDE_RESULT';
  const QUESTION = `__QUESTION_PLACEHOLDER__`;
  window[K] = { p: 'claude', q: QUESTION, status: 'starting', t0: Date.now(), events: [] };
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
    document.querySelector('[contenteditable="true"][aria-label*="prompt to Claude"]') ||
    document.querySelector('[contenteditable="true"]');
  const fSend = () =>
    Array.from(document.querySelectorAll('button')).find(b =>
      b.getAttribute('aria-label') === 'Send message' && !b.disabled
    );
  const fStop = () =>
    Array.from(document.querySelectorAll('button')).find(b =>
      /Stop response/i.test(b.getAttribute('aria-label') || '')
    );
  const extract = () => {
    const els = document.querySelectorAll('.standard-markdown');
    // Take the LAST markdown block (could be multiple if artifact / code), join for full response
    if (!els.length) return '';
    // If multiple, concat all that came after the last user message turn boundary
    // Simplest: take last element (covers single-segment responses)
    const last = els[els.length - 1];
    return last ? (last.textContent || '').trim() : '';
  };

  (async () => {
    try {
      // 1. Fill
      const i = await wF(fI);
      if (!i) { W.status = 'aborted'; W.abortReason = 'no_input'; return; }
      log('input_found', { aria: i.getAttribute('aria-label') });
      fill(i, QUESTION);
      await sleep(500);
      const filledLen = (i.textContent || '').length;
      log('filled', { len: filledLen });
      if (filledLen < 3) { W.status = 'aborted'; W.abortReason = 'fill_failed'; return; }

      // 2. Send
      const s = await wF(fSend, 6000);
      if (!s) { W.status = 'aborted'; W.abortReason = 'no_send'; return; }
      log('send_found', { aria: s.getAttribute('aria-label') });
      s.click();
      log('send_click');
      W.t_send = Date.now() - W.t0;

      // 3. Poll done signal: stop-response btn → gone, send btn reappears
      // Wait for stop btn to appear first
      const stopAppeared = await wF(fStop, 5000);
      if (!stopAppeared) log('warn_stop_never_appeared');
      log('stop_appeared');

      // Wait for send btn to come back (== stop gone)
      const MAX_TICKS = 120;
      let doneTick = null;
      for (let j = 0; j < MAX_TICKS; j++) {
        await sleep(1000);
        if (fSend() && !fStop()) { doneTick = j + 1; break; }
      }
      if (doneTick === null) { W.status = 'aborted'; W.abortReason = 'done_signal_timeout'; return; }
      log('done_signal', { tick: doneTick });

      // 4. Grace
      await sleep(2000);
      W.t_done = Date.now() - W.t0;

      // 5. Extract
      const responseText = extract();
      log('extracted', { len: responseText.length });
      // Also capture all .standard-markdown count (multi-segment if artifact)
      W.markdownSegmentCount = document.querySelectorAll('.standard-markdown').length;

      W.response = responseText;
      W.responseLen = responseText.length;
      W.totalMs = W.t_done;
      W.status = 'complete';
    } catch (err) {
      W.status = 'error';
      W.error = String(err);
    }
  })();

  return { p: 'claude', dispatched: true, qPreview: QUESTION.slice(0, 40) };
}
