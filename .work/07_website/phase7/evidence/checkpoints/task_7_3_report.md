# Task 7.3 — `build:fresh` script + replace `web/README.md` placeholder (C-P6-8)

> **Date**: 2026-04-29
> **Mode**: direct main-session, 2 files
> **Carryover absorbed**: C-P6-8 (also resolves G-P6-3 web/README.md gap)
> **Files touched**: 2

## Verdict

**PASS** — `build:fresh` script added + working; `web/README.md` replaced from default Astro starter (43 lines, "Astro Starter Kit: Minimal" boilerplate) to project-specific content (113 lines, 5,513 bytes) covering stack / scripts / architecture / 5 tribal-knowledge sections / hosting / release / phase trace.

## Files modified

| File | Δ | Purpose |
|---|---|---|
| `web/package.json` | +1 line | new `build:fresh` script: `rm -rf .astro node_modules/.astro dist && astro build && pagefind --site dist` |
| `web/README.md` | -43 / +113 | full replacement: project-specific content replacing default Astro starter boilerplate |

## README structure

8 sections:
1. **Tagline** — what the site is + production URL
2. **Stack** — 6 tools (Astro 6 / React 19 / Tailwind 4 / Vitest 4 / Playwright / Pagefind) with links
3. **Scripts** — 7 commands incl. new `build:fresh`
4. **Architecture** — 5 bullets covering routes / content collection / remark plugin / i18n keys / layouts (matches Phase 6 D-P6-1 + Phase 7 design choices)
5. **Tribal knowledge** — 5 sections that were prior pain points:
   - Astro content cache after markdown processor edits → use `build:fresh` (Phase 6 D-P6-7 / C-P6-8)
   - Playwright `reuseExistingServer: true` foot-gun → `lsof -ti:4321 | xargs kill` (C-P6-4)
   - Lang-neutral entries (no `lang:` frontmatter, no `.md` cross-refs — fail-loud throw)
   - Adding a new doc — 4-step recipe
   - Soft-404 on unmatched `/[lang]/*` paths (C-P7-1, accept-as-is)
6. **Hosting** — CF Pages auto-deploy + no `_redirects` overrides + local preview
7. **Release** — pointer to `RELEASE.md`
8. **Phase trace** — pointer to `.work/07_website/phase{N}/`

## Verifications

| Check | Cmd | Result |
|---|---|---|
| README replaced | `head -3 README.md` | "# SDTM Pedia — website" (project-specific, NOT "Astro Starter Kit: Minimal") |
| README size | `ls -l README.md` | 5,513 bytes (was 1,114 bytes default Astro) |
| New script works | `npm run build:fresh` | clean build green, pagefind 27 indexed pages, 31 HTML emitted |
| Existing tests preserved | `npm test -- --run` | 32/32 (no regression) |
| package.json valid JSON | (Astro build wouldn't run if invalid) | implicit PASS |

## Tribal-knowledge accuracy spot-check

Verified each piece against actual project state:

| Tribal section | Verification |
|---|---|
| Cache invalidation requires `build:fresh` after plugin edit | Phase 6.4 evidence (`task_6_4_report.md` H2 first-attempt regression) confirms |
| Playwright `reuseExistingServer: true` | `cat playwright.config.ts` confirms config |
| Lang-neutral entries throw on `.md` cross-refs | `remark-md-link-rewrite.mjs` source confirms throw at `frontmatter.lang === undefined && url.endsWith('.md')` |
| Adding new doc — slug-based catchall | `web/src/pages/[lang]/guide/[...slug].astro` source confirms |
| Soft-404 200 + meta-refresh | Task 7.0 report F-7.0-2 + 3 nonsense-URL probes confirms |

All 5 tribal sections accurately describe current project behavior. No stale or fabricated content.

## Carryover delta

- C-P6-8 Astro content-cache invalidation undocumented: **RESOLVED** in 7.3 (script + README documented)
- G-P6-3 no `web/README.md` (handoff phrasing): **RESOLVED** in 7.3 (file existed but had Astro starter boilerplate; now has project content)
- C-P6-4 Playwright `reuseExistingServer: true`: **PARTIAL** — covered by README tribal-knowledge box (no code change; user-discoverable). Code-level fix (kill-stale-port script OR `!process.env.CI` flag) deferred indefinitely
- C-P7-1 Astro i18n soft-404: **DOCUMENTED** in 7.3 README (accept-as-is per Task 7.0 recommendation)

## Commit

```
git commit -m "07 Website Phase 7.3 — build:fresh script + replace web/README.md placeholder with project content (C-P6-8 absorbed)"
```
