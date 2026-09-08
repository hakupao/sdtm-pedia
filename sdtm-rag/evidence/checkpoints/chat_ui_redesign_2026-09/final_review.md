# Final whole-branch review — Chat UI 重构 (ab24bad..ac388d6)

Reviewer: rev-final (Fable 5.1), read-only, no subagents. Reviewed in one pass over the 3196-line diff plus the live files in `sdtm-rag/webchat/`, `server/auth.py`, `scripts/tests/`. Everything below that says "ran" was run by me on this checkout, not taken from the task reports.

Verification I ran (2026-09-08):

```
node --test 'webchat/tests/*.test.mjs'                      → 24 pass / 0 fail
pytest test_sse_contract test_rate_limit_static_exempt
       test_webchat_cache_headers test_webchat_stream_render
       test_webchat_cache_browser -q                          → 29 passed (2 are real-browser playwright)
pytest test_model_switching -k "flag or badge or fell_back or probe" → 30 passed
```

Plus an ad-hoc node probe of `splitCitations` against 24 realistic model-output shapes and a timing of the vendored `marked.parse` on a 19 KB table-heavy answer (warm avg 1.4 ms, cold 18 ms).

## Strengths

- **The split is honest.** Every guard rail listed in spec §1 is present verbatim, including its rationale comments: `modelBadgeText` three-state + `fellBack === true` + `Array.isArray` with the ⛔ no-`filter(Boolean)` note (render.js:161-182), `flagModelName` fallback chain (flag.js:50-67), `streamAsk` terminal/onClose/onAbort three-way (stream.js:35-66), `save()` QuotaExceeded eviction (store.js:22-34), IME guard (app.js:210-218 and again in inlineRename), six-state `renderWebStatus`/`onToolResultUI` tables, `selectedCorpus` four-value map, `model` omitted when empty (stream.js:22).
- **`refreshModelBadgeLabels` never rebuilds `#messages`.** I traced all nine `renderMessages`/`paintAll` call sites in app.js (lines 13, 14, 21, 43, 55, 199, 204, 226, 231). The three that can fire during a stream (sidebar select, delete, new-chat) are the same parity behaviours as base; the two new ones (show-citations toggle, loadModelName empty-state repaint) are both guarded by `busy`, and the toggle is additionally `disabled` while sending.
- **Streaming pipeline ordering is correct.** `renderFinal` cancels the pending rAF before `finalizeBubble`; `persist` is idempotent via `saved`; every path that has tokens (done/error/close/abort) goes renderFinal → persist; paths without tokens cannot have a pending rAF. Web panel lives on the `turn`, outside the bubble that gets `innerHTML`-replaced each frame.
- **citations.js is now defensible.** Line-by-line processing, fence state machine that honours char + length, PUA sentinel, tidy-only-when-something-was-removed. My 24-case probe found no false positives on links, nested fences, hard breaks, tables, blockquotes, headings, or bold headings containing a citation (`**Severity [Source: a.md]**` → `**Severity**`).
- **Tests bite.** The retargeted guard tests kept their assertion shapes; `_frontend_sources` deliberately scans all modules so the comment-decoy still exists; the probe re-copies modules per scenario to defeat ESM caching and now drives the real submit path. The rate-limit test pins both directions (static never 429s past burst, `/api/info` still does).
- **Ratelimit ruling was the right call** and the fix is minimal: exact-match `"/"`, prefix `/static/`, nothing under `/api/`.
- **Visuals match spec §3.** Screens 02/03/04/08 read as 克制专业型: warm `#faf9f6` ground, serif headings and empty-state title, single green accent on send/active/focus ring, 12px meta chips, sources folded. The streaming frame (02) already shows rendered tables, headings and inline code with a red 停止 button, which is exactly the user-named defect #1 fixed.

## Issues

#### Critical

None.

#### Important

None that block on correctness. Two items I am elevating from the deferred list because they are trivial and user-visible, see triage table (collapsed sidebar in tab order; blank panel after deleting last conversation). Neither is a regression against main, so "With fixes" rather than "No".

#### Minor

1. **citations.js:24 — CJK punctuation not in the glue class.** `RE_GLUE_PUNCT` only knows `.,;:!?`. Strip mode: `见 [Source: a.md]、[Source: b.md]。` → `见、。` (probe output). Show mode: the `。` after a block-display `.cite` span falls onto its own line (visible in screen 04, "Source: knowledge_base/ROUTING.md" then a lone `。`). The UI language is Chinese/Japanese and the prompt asks for a citation per claim, so this shape is common. Fix: add `。，、；：！？）` to the glue class, and in show mode emit the span *after* trailing CJK punctuation or make `.cite` `display:inline-block` with a preceding `<br>`. One regex line plus one test.
2. **citations.js — citation-only list items leave empty bullets.** `- [Source: a.md]\n- **[Source: b.md]**` → `-\n-` which marked renders as two empty `<li>`. A trailing "参考来源" list is a realistic model habit. Fix: after tidy, if a line reduced to only a list marker (`^\s*[-*+]\s*$` or `^\s*\d+\.\s*$`), drop the line.
3. **citations.js — citation at the start of a bold span breaks the bold.** `**[Source: a.md] Severity**` → `** Severity**` (leading space defeats left-flanking). Unlikely shape; note it in the header comment as a known residue.
4. **app.js:14 — deleting the in-flight conversation does not abort the stream.** The answer persists into an orphan `c` (parity with main) *and* the LLM keeps generating for nobody. Fix: track the conversation id in `runGeneration` and call `stop()` in `onDelete` when it matches. Two lines.
5. **app.js:14 — deleting the last conversation leaves a blank main panel** (`renderMessages` returns at `!c`). Spec §6's empty state never appears until the user finds 新对话. Fix: `if (!store.conversations.length) newConversation();` before `paintAll()` in `onDelete`.
6. **style.css:22 — collapsed sidebar keeps 新对话 / titles / ✕ buttons in the tab order.** A keyboard user tabs onto invisible controls and Enter on an invisible ✕ arms a delete. Fix: add `visibility:hidden` to `#sidebar.collapsed` (transition still works with `visibility` in the list) or set `sidebar.inert` in `initSidebar.apply`.
7. **stream.test.mjs asserts only `parseSSE`.** The three-way termination logic in `streamAsk` (the Rule D HIGH fix) has no node test; it is covered only indirectly by the probe's `streamScenario` (done path) and by the retargeted guard tests. A 20-line test with a fake reader for close-without-done and abort would close the gap. Not blocking because the code is a verbatim move.
8. **store.test.mjs — QuotaExceeded eviction untested** (ledger-deferred). Same reasoning: verbatim move, but a fake `setItem` that throws twice would take ten lines.
9. **test_sse_contract.py `_frontend_sources`**: `>= 6` lower bound should be `>= 8` (app.js + 7 modules) or assert `render.js` is in the list; docstring reason is inverted (ledger-noted). Task 10 material.
10. **flag_attribution_probe.mjs:197 — `Object.assign(globalThis, g)` per scenario, never reset**, and tmp dirs are removed only on the success path (line 430). Works today; a failing scenario leaves dirs behind and later scenarios inherit stale globals. Wrap in try/finally.
11. **auth.py:180 — `_is_exempt` is a bare `startswith`.** `/static/../api/info` is nominally exempt but Starlette routes it to the `/static` mount whose `StaticFiles` normalises and 404s, and browsers normalise before sending, so no real bypass. Acceptable for the planned LAN share. Optional hardening: reject paths containing `/../` before the prefix check.
12. **`/static/tests/*.test.mjs` are served** by the mount. No secrets, but they are dev files; exclude before the 阶段3 LAN go-live.
13. **CSS off-token colours**: `.corpus-badge` `#e0e7ff`/`#ffe4e6`/`#333`, `.md pre` `#f4f2ed`, `.web-panel` border `#e0a552`, `.chip.unverified` border `#f1d9b8`. Cosmetic; fold into tokens when next touching style.css.
14. **`#to-bottom` at `bottom:118px`** overlaps the composer when the textarea is at its 200px max while the user is scrolled up. Rare combination; cosmetic.
15. **a11y**: settings panel has no `role="dialog"`/focus trap; `#messages` has no `aria-live`. Reasonable to defer for an internal tool.
16. **Uncommitted file in the working tree**: `docs/superpowers/plans/2026-09-08-chat-ui-redesign.md` shows 12/12 line edits not in the reviewed range. Presumably Task 10 in progress; it must be committed or reverted before the merge so the branch state matches what was reviewed.

## Security

- `renderMarkdown` output always passes `DOMPurify.sanitize` with default config (class attribute allowed, handlers/scripts stripped). The `.cite` span is injected as text into markdown *before* parse; the ref is `escapeHtml`-ed (`& < > "`) and cannot contain `]` or newline, so it cannot close the span or add attributes. A model could emit a literal `<span class="cite">` to spoof a citation, which is a display nuisance, not an injection; archive and ⚑ payload keep raw text.
- `CSS.escape` on `data-call-id` (render.js:297) is correct.
- `copyText` fallback uses a hidden readonly textarea + `execCommand`; no injection surface.
- Rate-limit exemption: `"/"` is exact-match (`path in set`), `/static/` prefix only. Rate limiting runs before AuthGate so unauthenticated hammering of `/static/*` costs one small file read then a 401. Acceptable on an internal LAN.

## Performance

Measured on the vendored marked 12.0.2: 19 KB with 300 table rows parses in 1.4 ms warm (18 ms cold, first call only). DOMPurify and the `innerHTML` relayout will add a few ms on 300-row tables, still well inside a 16 ms frame on desktop Chrome, and the rAF throttle means the worst case is a dropped frame rather than a stalled stream. The YAGNI ruling (no incremental diff until measured) is sound. Two inherent costs worth knowing: text selection inside the streaming bubble is lost every frame, and `hljs` is correctly deferred to finalize.

## Deferred-minor triage

| Ledger item | Verdict | Reason |
|---|---|---|
| prepareStreaming misses list-indented / nested-family fences | Defer | marked closes an open fence at the container end; mid-stream cosmetic only |
| save() eviction untested | Defer (do in Task 10 if cheap) | verbatim move; 10-line test would close it |
| store.test order dependency | Defer | tests pass in file order; node --test runs a file serially |
| RE_FULL case-sensitive | Defer | prompt mandates the exact form; my probe confirms `[source:` is left alone, which is the safer failure |
| `/static/tests/*.mjs` served | Defer to 阶段3 go-live | no secrets |
| Sentinel U+0000 | Fixed (PUA) | verified by test |
| `a ((cite))` → `a ()`, `*[cite]*` → `**`, 4-space indented code stripped | Defer | rare shapes; document in header comment |
| `#to-bottom` overlap at 200px textarea | Defer | rare combination, cosmetic |
| Collapsed sidebar in tab order | **Fix before merge** | one CSS line; invisible ✕ can arm a delete via keyboard |
| decorateCodeBlocks innerText fallback | Defer | marked always emits `<pre><code>`, fallback unreachable |
| off-token colours, `.model-meta` no style | Defer | `.chip` covers it; fold into tokens later |
| settings-panel role/focus, `#messages` aria-live | Defer | internal tool; note in Task 10 |
| spec §6 sidebar-collapse not in settings panel | Defer | brief intentional; record the deviation in Task 10 docs |
| web status in web-panel not chip | Defer | forced by verbatim guard rail |
| onRetry dead interface | Defer | harmless; remove or wire when next touching render.js |
| delete mid-stream orphans answer | Defer, but add `stop()` | parity; two-line improvement (Minor #4) |
| busy set outside try | Defer | parity; nothing between line 63 and 125 can realistically throw |
| delete last conversation → blank panel | **Fix before merge** | one line; the redesign made delete first-class and §6 promises an empty state |
| show-mode `。` orphan | Defer, but see Minor #1 | the same regex gap also produces `见、。` in strip mode, which is default-visible |
| `_is_exempt` bare startswith | Defer | StaticFiles traversal guard + browser normalisation; optional `/../` reject |
| auth.py mixed-language comment | Defer | style |
| `_frontend_sources` docstring / bound 6→8 | Defer to Task 10 | docs task anyway |
| probe tmp cleanup / globalThis reuse | Defer | wrap in try/finally when next touched |

## Rulings review

None overturned. Specific confirmations:

- **Feature branch instead of worktree**: correct given launchd serves the working tree.
- **I1/I2 override of plan text in citations.js**: correct; the plan's global tidy would have mangled code blocks, my probe confirms the local approach leaves untouched lines byte-identical.
- **Fence length rule**: correct per CommonMark and tested.
- **`e.detail > 1` fix for select vs rename**: correct analysis; the second click's target is the span created after the first re-render, and suppressing `onSelect` there keeps it attached for `dblclick`.
- **I2 (empty-state ST01 card) covered by loadModelName repaint**: verified at app.js:197-199, guarded by `!busy`.
- **setSources `.sources-slot` unguarded**: agree; only assistant turns reach it.
- **Rate-limit exemption breaking the "no server/ change" constraint**: agree; raising BURST would only defer the failure and the exemption is scoped correctly.
- **Task 8b retarget instead of weakening**: agree; assertion shapes are unchanged and the probe got stronger (real submit path).
- **YAGNI on incremental render**: agree, now with a measurement.

## Recommendations

Before merge (about 15 minutes, all in files already touched by this branch):

1. `style.css`: `#sidebar.collapsed { ...; visibility: hidden; }` (Minor #6).
2. `app.js` `onDelete`: abort if it is the streaming conversation, and `newConversation()` when the list becomes empty (Minor #4, #5).
3. `citations.js`: add CJK punctuation to `RE_GLUE_PUNCT`; add one node test for `见 [Source: a]、[Source: b]。` → `见。` (Minor #1). Optional in the same touch: drop citation-only list-item lines (Minor #2).
4. Commit or revert the modified plan document so the branch matches the reviewed state (Minor #16).

Task 10 (docs) should also record: the spec §6 deviation (sidebar collapse lives in the sidebar head, not the settings panel), the `webchat/vendor/README.md` module section, the `node --test 'webchat/tests/*.test.mjs'` command form, and the `_frontend_sources` bound/docstring fix.

Later: `streamAsk` termination unit test, QuotaExceeded eviction test, exclude `webchat/tests/` from the static mount before LAN go-live, fold off-token colours into tokens.

## Assessment

**Ready to merge? With fixes.** Spec §1 invariants hold end-to-end across the module boundaries, all suites I ran are green including the real-browser gate, and the security and performance questions have concrete answers rather than assumptions. The four pre-merge items are each one to three lines in files this branch already owns and none is a regression against main, so they should be folded in now rather than deferred into a redesign that made sidebar delete and the empty state first-class features.
