---
lang: en
slug: compare
order: 20
title: "4 Platforms — Multi-dimensional Comparison"
---

# 4 Platforms — Multi-dimensional Comparison

> Side-by-side comparison across 9 dimensions. Data snapshot: 2026-04-27 v1.0.

## 1. Evaluation Score (smoke v4 / 17 questions)

| Platform | Score | Version | Main Failure Points |
|---|:---:|:---:|---|
| Claude Projects | 17/17 (100%) | v2.6 | None |
| ChatGPT GPTs | 16.5/17 (97%) | v2.2 LIVE | Q1 GFINHERT spelling (fixed in v2.2); long-tail chunk mid-table may miss |
| Gemini Gems | 16/17 (94%) | v7.1 LIVE | Q10 SUPP-- Core anchor (fixed in v7.1); R1 65% → R2 94% (v6→v7 upgrade) |
| NotebookLM | 15/17 (88%) | v1.0 / Custom mode | Q9 Pinnacle 21 / Q11 Dataset-JSON / Q12 CT version — three questions PUNT (in-KB-only architecture limit; safe behavior, not a bug) |

## 2. Capacity Ceiling

| Platform | Capacity Ceiling | Current Usage | Headroom |
|---|---|---|---|
| Claude Projects | 1.29M tokens (near Pro soft limit) | 19 files / 77% | ~23%; adding files requires deprioritizing lower-priority ones first |
| ChatGPT GPTs | 20-file hard limit | 9 files (post-merge, e.g. 04_domain_specs_all.md) | 11-file headroom |
| Gemini Gems | 1M-token context window | 4 files (most aggressive merge) | Window headroom ample; first-token cold start slightly slower |
| NotebookLM | 50-source hard limit (Pro plan) | 42 sources | 8-source headroom |

## 3. Team Sharing

| Platform | Sharing Method | Review Required |
|---|---|---|
| Claude Projects | Organization / Project invite (Team / Enterprise plan shares Project; Pro users must each redeploy independently) | N/A (direct internal invite) |
| ChatGPT GPTs | Share Custom GPT within organization (no review) or publish to GPT Store (OpenAI review required) | Store publishing only |
| Gemini Gems | Workspace plan: Daisy shares directly; personal account: colleagues self-deploy (paste full v7.1 system prompt) | N/A |
| NotebookLM | Email-invite to join notebook (Pro / Workspace), or colleagues build their own (50-source cap) | N/A |

## 4. Subscription Requirements

| Platform | Supported Plans | Available on Free |
|---|---|:---:|
| Claude Projects | Claude Pro / Team / Enterprise | No |
| ChatGPT GPTs | ChatGPT Plus / Team / Enterprise | No |
| Gemini Gems | Gemini Advanced personal / Google Workspace | No |
| NotebookLM | NotebookLM Pro / Google Workspace | No (50-source cap is Pro/Workspace only) |

## 5. Internet Access

| Platform | Internet Access | Default State |
|---|---|---|
| Claude Projects | Web search can be enabled manually | Off by default; toggle as needed |
| ChatGPT GPTs | Web browsing can be enabled manually | Off by default; toggle as needed |
| Gemini Gems | Can be enabled manually (Google Search integration) | Off by default; toggle as needed |
| NotebookLM | Strict in-KB-only (42 sources only; no internet) | By design, not a bug; proactively PUNTs out-of-source questions |

## 6. Anti-hallucination Posture

| Platform | Strength | Mechanism |
|---|:---:|---|
| Claude Projects | Strong | Multi-step reasoning + system prompt anti-fabrication anchor + Stage 6 Deferred Stub rules |
| ChatGPT GPTs | Medium | System prompt guidance + post-v2.2 GFINHERT precise variable validation; long-tail chunks occasionally miss |
| Gemini Gems | Moderately strong (post v7.1) | v6→v7 upgrade added AHP guardrail; R1→R2 score rose from 65% to 94%; colleagues must paste full v7.1 system prompt when self-deploying |
| NotebookLM | Very strong | in-KB-only architecture is inherently anti-hallucination; PUNTs rather than fabricates for anything outside 42 sources; inline citation verification |

## 7. File Count Limit

| Platform | File Count Limit | Current File Count |
|---|---|:---:|
| Claude Projects | Soft limit governed by token capacity (~77% used / 1.29M tokens) | 19 |
| ChatGPT GPTs | 20-file hard limit | 9 |
| Gemini Gems | No explicit file count limit (bounded by 1M-token window) | 4 |
| NotebookLM | 50-source hard limit (Pro) — see §2 | 42 |

## 8. Best-at Scenario

| Platform | Best-at Scenario |
|---|---|
| Claude Projects | Precise variable lookup + multi-step reasoning (Core + C-code + cross-variable, e.g. PCTPT five-item set); wrong-premise correction (SUPPTS); domain boundary determination |
| ChatGPT GPTs | Full-domain queries; team sharing / GPT Store publishing; organization-internal sharing without review |
| Gemini Gems | One-shot large-context ingestion / cross-domain pattern comparison; long sessions; broad exploration; deep 4-file merge |
| NotebookLM | Strong anti-hallucination (audit / compliance); inline citation verification; refusal preferred over fabrication; cross-domain death-date–level alignment and v3.4 new-domain PASS+ |

## 9. Worst-at Scenario

| Platform | Worst-at Scenario |
|---|---|
| Claude Projects | Real-time internet (FDA / Pinnacle 21 requires manual check at cdisc.org); very large-scale domain batch comparison; capacity already at 77% near Pro soft limit |
| ChatGPT GPTs | Multi-step reasoning slightly weaker than Claude; Free account users cannot find the entry point; long-tail chunk mid-table may miss |
| Gemini Gems | Personal account cannot share with team directly (requires Workspace); colleagues self-deploying must paste full v7.1 system prompt or AHP guardrail is lost |
| NotebookLM | Questions outside the 42 sources (real-time Pinnacle 21 / breaking news / Dataset-JSON v1.1 / CT version locking + MedDRA) are proactively PUNTed — by design, not a bug |

---
*v1.0 — 2026-04-27 — Maintained by Daisy*
