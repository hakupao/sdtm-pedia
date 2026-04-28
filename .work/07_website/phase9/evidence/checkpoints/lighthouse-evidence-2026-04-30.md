# Lighthouse audit evidence — 2026-04-30 (Phase 9 / master plan §10.1)

> **URL audited**: `https://sdtm-pedia.pages.dev/zh/`
> **Tool**: Chrome DevTools MCP `lighthouse_audit` mode=navigation device=desktop
> **Reports**: `web/qa/lighthouse-zh-landing-2026-04-30.{html,json}` (311 KB HTML / 177 KB JSON)
> **Daisy ack**: "还可以" (2026-04-30 — accepted as v1.0 baseline; remediation deferred)

## Category scores

| Category | Score | Master plan §9 target | Verdict |
|---|---|---|---|
| Accessibility | 91 | ≥ 95 | -4 below target |
| Best Practices | 73 | ≥ 95 | -22 below target |
| SEO | 100 | (not in §9 explicit, but ≥ 95 implied) | ✅ above |
| Performance | (not measured) | ≥ 95 | requires `performance_start_trace` (separate tool) — deferred |

Note: the Lighthouse MCP tool excludes Performance audit by design ("excludes performance. For performance audits, run performance_start_trace"). Performance trace deferred to **C-P9-4** below.

## Failed audits (6 of 51 total)

| Audit ID | Score | Category | What | Disposition |
|---|---|---|---|---|
| `color-contrast` | 0 | A11y | Background/foreground contrast ratio insufficient on some text | **C-P9-5** — likely `--ink-mute` (`#555555` on `#f8f5ef` = ~7.4:1 passes; `#b8b3a8` on `#0d0c0a` ~7.6:1 passes) but fine-text or `--ink-faint` rgba(*, 0.4) likely fails. Audit in DevTools "View origin" pane to identify offending nodes. Cheap CSS fix expected. |
| `label-content-name-mismatch` | 0 | A11y | Visible button text doesn't match its accessible name | **C-P9-6** — likely the ⌘K hint button (visible text from `t['search.shortcut']` = "Cmd K", aria-label "Open search" — these don't match). Pattern: aria-label should *contain* visible text per WCAG 2.5.3. Fix candidates: aria-label="Open search (⌘K)" OR drop aria-label and use visible text only. |
| `target-size` | 0 | A11y | Touch targets < 24×24 CSS px or insufficient spacing | **C-P9-7** — mobile-only audit at desktop viewport; may be footer links / TOC small fonts / nav micro-buttons. Inspect via Lighthouse "View" links. Fix candidates: bump `py-0.5` → `py-1` on dense flex menus + add `min-h-[24px]` on micro buttons. |
| `errors-in-console` | 0 | Best Practices | Console errors logged | **C-P9-8** — likely Pagefind dynamic-import warning logged in PROD (Phase 8 F-4 fix surfaces this on purpose for telemetry). Acceptable if intentional; otherwise gate behind `import.meta.env.DEV`. Triage from `lighthouse-zh-landing-2026-04-30.json` audits[errors-in-console].details. |
| `inspector-issues` | 0 | Best Practices | Issues panel reports (overlapping with errors-in-console + 3rd-party cookies) | covered by other items |
| `third-party-cookies` | 0 | Best Practices | Third-party cookies (Cloudflare/CF Pages telemetry) | **ACCEPTED** — out of our control (CF Pages baseline). Documented as expected. |

## Aggregate verdict

- 45 / 51 audits passed (88%); 0 manual / 0 not-applicable / 0 informative excluded.
- All failures are **single-line cheap polish** EXCEPT third-party-cookies (vendor-imposed) and performance (tool-limited here).
- Daisy ack 2026-04-30: "还可以" — accept as v1.0 baseline. v1.1 polish target: 95/95/95.

## Carryover for Phase 10 / v1.1 polish

- **C-P9-4** Lighthouse Performance trace via `chrome-devtools__performance_start_trace`. Deferred.
- **C-P9-5** color-contrast remediation (likely fine-text + `--ink-faint` 0.4 alpha)
- **C-P9-6** label-content-name-mismatch on ⌘K hint button
- **C-P9-7** target-size mobile audit + bump dense flex spacing
- **C-P9-8** errors-in-console triage (Pagefind warn intentional? or gate to DEV?)
- **C-P9-9** third-party-cookies — ACCEPTED indefinitely (CF Pages baseline)

## Provenance

- Audit run from this main session via Chrome DevTools MCP `lighthouse_audit` tool with `mode=navigation` (full page reload + audit) on production URL.
- Pre-existing Chrome MCP browser session (Daisy's normal browsing tabs); audit ran in new tab #5; tab closed post-audit.
- Reports preserved verbatim under `web/qa/` for archival reference.
