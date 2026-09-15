import test from "node:test";
import assert from "node:assert/strict";
import { parseSSE, streamAsk } from "../js/stream.js";

test("parseSSE 解析 event/data; 坏 JSON 返回 null", () => {
  assert.deepEqual(parseSSE('event: token\ndata: {"text":"hi"}'), { event: "token", data: { text: "hi" } });
  assert.equal(parseSSE("event: token\ndata: {bad"), null);
  assert.equal(parseSSE("event: token"), null);
});

// ── streamAsk 的 sources 回调: 第三参 = 整个事件体 (新字段从这里取, 不改形参列表) ──

function fakeResponse(frames) {
  const enc = new TextEncoder();
  let i = 0;
  return {
    ok: true,
    body: {
      getReader: () => ({
        read: async () => (i < frames.length
          ? { value: enc.encode(frames[i++]), done: false }
          : { value: undefined, done: true }),
      }),
    },
  };
}

async function runStream(frames, handlers, args = {}) {
  const orig = globalThis.fetch;
  let sent = null;
  globalThis.fetch = async (_url, opts) => { sent = JSON.parse(opts.body); return fakeResponse(frames); };
  try {
    await streamAsk({ question: "q", history: [], corpus: "auto", web: false, ...args },
                    { onToken: () => {}, onDone: () => {},
                      onError: (m) => { throw new Error(`unexpected onError: ${m}`); },
                      ...handlers });
  } finally { globalThis.fetch = orig; }
  return sent;
}

const SOURCES_FRAME = 'event: sources\ndata: {"sources":[{"chunk_id":"c1"}],"routed_corpus":"both",'
  + '"dossier":{"attached":true,"reason":"forced_on","sections":["4","5"],"chars":10,"sha":"abc"}}\n\n';
const DONE_FRAME = 'event: done\ndata: {"model_id":"m1"}\n\n';

test("sources 回调拿得到整个事件体 ⇒ dossier 有处可取", async () => {
  let got = null;
  const sent = await runStream([SOURCES_FRAME, DONE_FRAME],
    { onSources: (s, routed, ev) => { got = { s, routed, ev }; } },
    { dossier: "on" });
  assert.equal(got.routed, "both");
  assert.equal(got.s.length, 1);
  assert.equal(got.ev.dossier.attached, true);
  assert.equal(got.ev.dossier.reason, "forced_on");
  assert.deepEqual(got.ev.dossier.sections, ["4", "5"]);
  // 控件的三态必须真的进请求体 —— 不进的话界面上选了"关", 后端照样挂
  assert.equal(sent.dossier, "on");
});

test("只声明两个形参的老回调逐字节不受影响", async () => {
  let got = null;
  await runStream([SOURCES_FRAME, DONE_FRAME],
    { onSources: (s, routed) => { got = { n: s.length, routed }; } });
  assert.deepEqual(got, { n: 1, routed: "both" });
});
