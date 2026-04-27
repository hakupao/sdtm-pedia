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

- **Claude Projects** → [./claude_tutorial.en.md](./claude_tutorial.en.md) (19 files + system_prompt + 24-question smoke test)
- **ChatGPT GPTs** → [./chatgpt_tutorial.en.md](./chatgpt_tutorial.en.md) (Custom GPT + 9 files + v2.2 system prompt + 17-question smoke test)
- **Gemini Gems** → [./gemini_tutorial.en.md](./gemini_tutorial.en.md) (Gem + 4 merged files + v7.1 system prompt + AHP acceptance check)
- **NotebookLM** → [./notebooklm_tutorial.en.md](./notebooklm_tutorial.en.md) (notebook + 42 sources + Custom mode 9011 chars + three sharing tiers)

## 3. Common Prerequisites

1. `git clone` this repository locally and enter the root directory.
2. Locate the corresponding platform directory `ai_platforms/{claude_projects,chatgpt_gpt,gemini_gems,notebooklm}/current/` (do not copy from `dev/` or `archive/`).
3. Set up your account and plan (see §1 table).
4. Open the matching tutorial from §2 and follow sections in strict order (skipping steps will lose system_prompt gating rules).

## 4. Post-Deployment Verification (smoke test)

After deployment, run questions D0 + D1 + D5 from `../DEMO_QUESTIONS.md` for a quick acceptance check (5 minutes):

- **D0**: Basic AESER query (AE / Exp / C66742 NY) — validates basic RAG.
- **D1**: GF domain EGFR scenario (GFGENSR / GFPVRID / GFGENREF / GFINHERT) — validates new domain + multi-variable reasoning.
- **D5**: SUPPTS premise correction — validates anti-hallucination gating (active detection → TSVAL1-n).

All 3 PASS = deployment successful. If any question fails, consult `../KNOWN_LIMITATIONS.en.md` for troubleshooting: check first (a) whether system_prompt.md was pasted in full without truncation, and (b) whether the number and size of files in uploads/ match the tutorial checklist.

## 5. Upgrade / Maintenance

The source repository will be updated: on each minor release (`../CHANGELOG.md` tagged v1.1 / v1.2) or when a new SDTMIG version (v3.5+) is published. Re-upload steps: `git pull` → enter `current/` → delete old uploads and re-upload → **copy-paste the new system_prompt.md in full** (truncation must not occur, or AHP gating rules will be lost — e.g. Gemini v7.1 CO-1d SUPPQUAL hard anchor + ChatGPT v2.2 v3.4 new-domain variable name validation). Rollback: historical versions are retained in each platform's `dev/archive/drafts/` and can be reverted to.

## 6. Feedback

If you encounter an error or hallucination: (1) take a screenshot and keep the complete original question and AI response; (2) include platform + version (e.g. "ChatGPT GPT v2.2 LIVE 2026-04-24") + expected answer (cite SDTMIG v3.4 section number or CDISC CT C-code) + self-deployed version number + smoke score; (3) email Daisy / issue tracker / department group @Daisy. Feedback is consolidated into `../CHANGELOG.md` for the next minor release.
