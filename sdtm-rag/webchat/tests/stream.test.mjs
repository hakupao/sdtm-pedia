import test from "node:test";
import assert from "node:assert/strict";
import { parseSSE } from "../js/stream.js";

test("parseSSE 解析 event/data; 坏 JSON 返回 null", () => {
  assert.deepEqual(parseSSE('event: token\ndata: {"text":"hi"}'), { event: "token", data: { text: "hi" } });
  assert.equal(parseSSE("event: token\ndata: {bad"), null);
  assert.equal(parseSSE("event: token"), null);
});
