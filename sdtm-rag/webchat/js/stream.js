// SSE 流式客户端。不读 DOM: 检索范围 / 联网 / 模型由调用方算好传进来。
export function parseSSE(raw) {
  let event = "message", data = "";
  for (const line of raw.split("\n")) {
    if (line.startsWith("event:")) event = line.slice(6).trim();
    else if (line.startsWith("data:")) data += line.slice(5).trim();
  }
  if (!data) return null;
  try { return { event, data: JSON.parse(data) }; } catch (_) { return null; }
}

export async function streamAsk({ question, history, corpus, web, model },
                                { onSources, onToken, onToolCall, onToolResult, onDone, onError, onClose, onAbort, signal }) {
  let resp;
  try {
    const payload = { question, history, corpus, web };
    // spec §5 裁定: UI **永远发显式 id**, 绝不依赖默认值落到 default 组 ——
    // default 与 opus-5 今天都解析到 Opus 5, 但改 .env 的 default_model 会让二者静默分叉。
    // 下拉为空 (info 没加载出来) 时**整个字段省略**, 由服务端默认值接管, 而不是硬塞 "default"
    // ——「省略」与「显式传 default」在服务端是同一行为, 但省略不会在产物里留下一个
    // 用户根本没做过的选择。
    if (model) payload.model = model;
    resp = await fetch("/api/ask_stream", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload), signal,
    });
  } catch (e) {
    if (signal?.aborted) { onAbort?.(); return; }
    onError("无法连接服务"); return;
  }
  if (!resp.ok) { onError(`服务错误 ${resp.status}`); return; }
  const reader = resp.body.getReader();
  const dec = new TextDecoder();
  let buf = "";
  let terminal = false; // saw a done/error frame
  const dispatch = (ev) => {
    if (!ev) return;
    if (ev.event === "sources") onSources(ev.data.sources || [], ev.data.routed_corpus || null);
    else if (ev.event === "token") onToken(ev.data.text || "");
    else if (ev.event === "tool_call") onToolCall?.(ev.data || {});
    else if (ev.event === "tool_result") onToolResult?.(ev.data || {});
    else if (ev.event === "done") { terminal = true; onDone(ev.data || {}); }
    else if (ev.event === "error") { terminal = true; onError(ev.data.message || "生成失败"); }
  };
  try {
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      buf += dec.decode(value, { stream: true });
      let i;
      while ((i = buf.indexOf("\n\n")) !== -1) {
        dispatch(parseSSE(buf.slice(0, i)));
        buf = buf.slice(i + 2);
      }
    }
  } catch (e) {
    // User hit Stop -> AbortError on the pending read. Treat as a clean stop (keep partial).
    if (signal?.aborted) { onAbort?.(); return; }
    onError("连接中断"); return; // genuine network drop mid-stream
  }
  // A terminal frame cut exactly at EOF (no trailing \n\n) would otherwise be lost.
  if (!terminal && buf.trim()) dispatch(parseSSE(buf));
  // Clean TCP close with NO done/error frame (worker killed mid-stream, reverse-proxy
  // idle-timeout in 阶段3, generator died before the done yield): neither onDone nor onError
  // fired — without this the streamed answer is on screen but never persisted (lost on reload).
  if (!terminal && onClose) onClose();
}
