# Self-Deployment Guide — SDTM AI Knowledge Base v1.0

> For colleagues who want to deploy their own copy. All 4 platforms can be deployed independently; expect to be live in 30-60 minutes.

## 1. Which Platform Should I Deploy?

| Platform | Deploy Time | Plan | Team Sharing |
|---|:---:|---|---|
| **NotebookLM** | ~30 min | Pro / Workspace | notebook invite (50-source cap) |
| **Gemini Gems** | ~30 min | Advanced / Workspace | personal sharing not available; requires Workspace |
| **ChatGPT GPTs** | ~45 min | Plus / Team / Enterprise | no review within organization; GPT Store requires review |
| **Claude Projects** | ~60 min | Pro / Team / Enterprise | Team/Enterprise shared; Pro requires individual redeploy |

Choosing by deployment preference (consistent with USER_GUIDE.en.md §3): fastest (~30 min) → NotebookLM or Gemini; deepest RAG → Claude Projects; team sharing → ChatGPT GPTs; strongest anti-hallucination → NotebookLM.

## 2. Four Platform Deployment Tutorials (Independent, Pick One)

- **Claude Projects** → [./claude/tutorial.en.md](./claude/tutorial.en.md) (19 files + system_prompt + 24-question smoke test)
- **ChatGPT GPTs** → [./chatgpt/tutorial.en.md](./chatgpt/tutorial.en.md) (Custom GPT + 9 files + v2.2 system prompt + 17-question smoke test)
- **Gemini Gems** → [./gemini/tutorial.en.md](./gemini/tutorial.en.md) (Gem + 4 merged files + v7.1 system prompt + AHP acceptance check)
- **NotebookLM** → [./notebooklm/tutorial.en.md](./notebooklm/tutorial.en.md) (notebook + 42 sources + Custom mode instructions 8,925 chars + three sharing tiers)

## 3. Common Prerequisites

1. Enter this directory (download the release pack from the company cloud, or `git clone` the repository and enter `ai_platforms/release/v1.0/`). Per-platform deploy assets are already in place under `./{claude,chatgpt,gemini,notebooklm}/` (`system_prompt.md` or `instructions.md` + `uploads/` + `tutorial.<lang>.md`).
2. Set up your account and plan (see §1 table).
3. Open the matching tutorial from §2 and follow sections in strict order (skipping steps will lose system_prompt gating rules).

## 4. Post-Deployment Verification (smoke test)

After deployment, run questions D0 + D1 + D5 from `../DEMO_QUESTIONS.md` for a quick acceptance check (5 minutes):

- **D0**: Basic AESER query (AE / Exp / C66742 NY) — validates basic RAG.
- **D1**: GF domain EGFR scenario (GFGENSR / GFPVRID / GFGENREF / GFINHERT) — validates new domain + multi-variable reasoning.
- **D5**: SUPPTS premise correction — validates anti-hallucination gating (active detection → TSVAL1-n).

All 3 PASS = deployment successful. If any question fails, consult `../KNOWN_LIMITATIONS.en.md` for troubleshooting: check first (a) whether system_prompt.md was pasted in full without truncation, and (b) whether the number and size of files in uploads/ match the tutorial checklist.

## 5. Upgrade / Maintenance

Release packs will be updated: on each minor release (`../CHANGELOG.md` tagged v1.1 / v1.2) or when a new SDTMIG version (v3.5+) is published, Bojiang Zhang distributes a fresh release pack via the company cloud. Re-upload steps: obtain the new pack → enter the matching platform subdirectory (`./{claude,chatgpt,gemini,notebooklm}/`) → delete old uploads and re-upload → **copy-paste the new system_prompt.md in full** (truncation must not occur, or AHP gating rules will be lost — e.g. Gemini v7.1 CO-1d SUPPQUAL hard anchor + ChatGPT v2.2 v3.4 new-domain variable name validation). Rollback: contact Bojiang Zhang for a historical release pack.

## 6. Feedback

If you encounter an error or hallucination: (1) take a screenshot and keep the complete original question and AI response; (2) include platform + version (e.g. "ChatGPT GPT v2.2 LIVE 2026-04-24") + expected answer (cite SDTMIG v3.4 section number or CDISC CT C-code) + self-deployed version number + smoke score; (3) email Bojiang Zhang / issue tracker / department group @Bojiang Zhang. Feedback is consolidated into `../CHANGELOG.md` for the next minor release.
