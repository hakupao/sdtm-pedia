# P0 Reviewer — Rule D 独立审查 prompt v1.5

> Version: v1.5 (2026-04-28, post P1 round 8 cut + reconciler closure)
> 基于 v1.4 (round 7 cut + 24 round 5+6+7 candidates absorbed N1-N14 + Rule D roster 34→43 + fix matrix 13→22 items A-V) + round 8 (batches 35/36/37) carry-forward
> v1.5 变更 over v1.4: **codification only.** Rule D roster expanded 43 → 48 slots (累 round 8 + v1.5 cut); v1.5 fix verification matrix 加 3 codification items W-Y covering 8 round 8 v1.5 candidates V1-V8 (W = N15 .xpt-parent / X = N16 writer-family ban / Y = N17 post-extraction VALIDATION pass); next-pool 候选 pivot to codex / Plan-extension / Explore / claude-code-guide-extension / superpowers-extension-via-skill (NOT agent — defer to v1.6 if needed) / general-purpose-extension / omc-family-remaining; AGENT-vs-SKILL roster doc NEW per V1; STRONGLY VALIDATED status promotion N14 + G-MS-4 per V5; Write-tool-less default codification §Step 4 first-class branch per V7.

## 角色硬约束

你是独立 subagent (v1.5 carry-forward unchanged), 仅负责 Rule D 独立审查 v1.5 prompt cut OR P1 batch atomization 输出. 与 Writer/Matcher 不同 subagent_type.

**严禁** (v1.5 carry-forward):
- 主 session 自审 (Rule D 违规)
- 改写 v1.5 prompt 内容 (审查不修改, 修改回主 session)
- 跳过 fix matrix 中任一 item (M+3 NEW = M+25 items A-Y 全审)

═══════════════════════════════════════════════════════════════════
## §0 NEW v1.5: AGENT-vs-SKILL roster doc (per V1)
═══════════════════════════════════════════════════════════════════

**Source**: round 8 O-P1-121 MEDIUM kickoff §1 SKILL-vs-AGENT pre-allocation lint missing recurring O-P1-110 round 7 motif. Despite v1.4 codification removing data:* + firecrawl:* families (skills not agents), kickoff §1 still scheduled `superpowers:verification-before-completion` SKILL for batch 36 #46 → Plan family inaugural pivot required.

**Rule D pre-allocation lint protocol**: Before kickoff §1 commits a Rule D slot pre-allocation, MUST validate the candidate against the roster below. **HALT if candidate appears in SKILL list** (not AGENT list).

### Registered AGENTS list (Task tool dispatchable, post round 8)

| Family | Agents (Task subagent_type) | Status post round 8 |
|---|---|---|
| **vercel** | performance-optimizer / deployment-expert / ai-architect | EXHAUSTED 3/3 round 4 |
| **plugin-dev** | plugin-validator / agent-creator / skill-reviewer | EXHAUSTED 3/3 round 4 |
| **feature-dev** | code-architect / code-explorer / code-reviewer | EXHAUSTED 3/3 round 4 |
| **pr-review-toolkit** | code-reviewer / code-simplifier / comment-analyzer / pr-test-analyzer / silent-failure-hunter / type-design-analyzer | EXHAUSTED 6/6 round 8 batch 35 |
| **oh-my-claudecode (omc)** | analyst / architect / code-reviewer / code-simplifier / critic / debugger / designer / document-specialist / executor / git-master / planner / qa-tester / scientist / security-reviewer / test-engineer / tracer / verifier / writer | 9× saturated (release / setup / explore-deeper / planner-strategist / others 1-2 unburned) |
| **general-purpose** | general-purpose | 2× burned round 5 inaugural + round 7 G-MS-4 fallback (3rd burn extension validated) |
| **superpowers** | code-reviewer (only this from family) | 1× INAUGURAL round 6 |
| **Plan** | Plan (single-agent family) | 1× INAUGURAL round 8 batch 36 |
| **claude-code-guide** | claude-code-guide (single-agent family) | 1× INAUGURAL round 8 batch 37 |
| **codex** | codex-rescue | 1× INAUGURAL v1.5 cut (this session) |
| **Explore** | Explore | 0× — un-burned candidate |
| **statusline-setup** | statusline-setup | 0× — read-only, niche use |

### NOT AGENTS (SKILLS list — loaded via Skill tool only, NEVER pre-allocate as Rule D slot)

`superpowers:verification-before-completion` / `superpowers:executing-plans` / `superpowers:dispatching-parallel-agents` / `data:*` (debugging-dags / etc) / `firecrawl:*` (skill-gen / etc) / all `oh-my-claudecode:*-skill` non-agent / `claude-md-management:*` / `code-review:*` / `commit-commands:*` / `pr-review-toolkit:review-pr` (slash command not agent) / `chrome-devtools-mcp:*` / `claude-code-setup:*` / `data:*` / `firecrawl:*` (skill-gen / firecrawl) / `frontend-design:*` / `playground:*` / `plugin-dev:create-plugin` (slash command, the agent variants are listed above) / `skill-creator:*` / `vercel:*` (auth/bootstrap/deploy/etc are skills not agents — except the explicit subagent_types vercel:ai-architect/deployment-expert/performance-optimizer above) / `supabase:*` / `oh-my-claudecode:cancel/autopilot/team/etc` (skills not agents).

**Verification mechanism**: pre-allocation lint script (out-of-scope this prompt — see MULTI_SESSION_PROTOCOL.md v1.5 codification candidate); manual cross-check against this §0 roster.

## 已烧 Rule D roster (post P1 round 8 + v1.5 cut, 累 48 slots)

参 v1.4 §已烧 Rule D roster + 5 NEW slots round 8 + v1.5 cut:

| Slot | Subagent_type | Round / Batch | AUDIT pivot # | Family burn count |
|---|---|---|---|---|
| #44 | oh-my-claudecode:document-specialist | v1.4 cut 2026-04-28 | 25th | omc-family 9× saturated |
| #45 | pr-review-toolkit:pr-test-analyzer | round 8 batch 35 | 26th | pr-family 4th-agent intra-family depth burn = FIRST 4th-agent for ANY family + family pool COMPLETED 6/6 |
| #46 | Plan | round 8 batch 36 | 27th | Plan-family INAUGURAL single-agent (pivoted from `superpowers:verification-before-completion` SKILL not AGENT recurring O-P1-110 → O-P1-121 motif) |
| #47 | claude-code-guide | round 8 batch 37 | 28th | claude-code-guide-family INAUGURAL 9th family pool |
| **#48** | **codex:codex-rescue** | **v1.5 cut 2026-04-28** | **29th** | **codex-family INAUGURAL 10th family pool inaugural (external runtime / different model = strongest Rule D isolation)** |

Cumulative: 48 slots / 29 AUDIT pivots (28 post round 8 + #48 v1.5 cut codex INAUGURAL) / 4 family pools EXHAUSTED (vercel + plugin-dev + feature-dev round 4 + pr-review-toolkit round 8) / 9 active families + codex-family INAUGURAL = 10 active families post v1.5 cut.

## 候选 slot (post round 8 + v1.5 cut, 池余主要在)

- `Explore` (0× — un-burned candidate, 11th family pool inaugural)
- `oh-my-claudecode:release` / `oh-my-claudecode:setup` (omc-family-remaining)
- `general-purpose` (3rd burn extension validated)
- `claude-code-guide` (extension burn after #47 inaugural)
- `Plan` (extension burn after #46 inaugural — single-agent family)
- `codex:codex-rescue` (extension burn after #48 inaugural — but external runtime expensive, prefer once per cut session)
- `oh-my-claudecode:remember` / other omc-skills mistakenly listed as agents — verify per §0 AGENT-vs-SKILL roster before pre-allocation

═══════════════════════════════════════════════════════════════════
## §Step 1-3 (v1.4 carry-forward)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.4_final_2026-04-28/P0_reviewer_v1.4.md` for:
- §Step 1 N 原子逐条独立判 (4-dimension verdict per atom)
- §Step 2 v1.5 Fix 验证矩阵 (25 items A-Y, expanded over v1.4 22-item matrix — see below)
- §Step 3 产出 reviewer_report.md template

### v1.5 Fix 验证矩阵 (25 items A-Y, expanded over v1.4 22-item matrix)

参 v1.4 §Step 2 for items A-V (22 items v1.3 base + v1.4 NEW). v1.5 NEW items W-Y:

| Item | v1.5 codification | Verification |
|---|---|---|
| **W** | **N15 .xpt-parent / table_caption FORBID** (per V2 + retroactive sweep) | Verify writer-side codification: `parent_section` regex assert NOT match `^[a-z]+\.xpt$`; canonical replacement form table; Self-Validate Hook 14.5 halt-on-violation; reconciler-side retroactive Option H bulk fix 35 atoms applied (27 batch 36 .xpt-parent + 8 historical p.133 NEW9). PASS if all codified + retroactive sweep applied + 0 post-fix violations. |
| **X** | **N16 writer-family ban for Examples-narrative + spec-table content type** (per V3 ESCALATION) | Verify writer-side codification: §派发 subagent_type table content-type-aware dispatch; Examples-narrative + spec-table → executor MANDATORY (writer-family BANNED); SENTENCE-paragraph + LIST_ITEM-heavy → free; mixed structural transition → executor PREFERRED; NEW input field `content_type_hint` mandatory; Self-Validate Hook 16.5 pre-dispatch assert; halt threshold for 5th cumulative writer-direction recurrence ESCALATES to mandatory writer-family ban for ALL TABLE_ROW-heavy content type. PASS if codified per round 5+6+7+8 4 cumulative writer-direction VALUE HALLUCINATION recurrences. |
| **Y** | **N17 post-extraction VALIDATION pass — Self-Validate hooks 14→17 extension** (per V4) | Verify writer-side codification: Self-Validate hooks expand 14→17 (Hook 15 cross-row TABLE_ROW pipe-count consistency + Hook 16 cross-row USUBJID format consistency + Hook 17 multi-axis value-cell spot-check sample N=3); spec checklist embedded in writer prompt §任务流程 step 7 NEW; light implementation no new tooling. PASS if codified per round 8 G-MS-NEW-8-5 detection-not-prevention escalation. |

═══════════════════════════════════════════════════════════════════
## §Step 4 NEW: Write-tool-less default codification (per V7)
═══════════════════════════════════════════════════════════════════

**Source**: round 8 G-MS-NEW-8-7 — Plan family inaugural burn at slot #46 (single-agent family) + claude-code-guide family inaugural burn at slot #47 (full family) + codex:codex-rescue v1.5 cut #48 — all completed Write-tool-less / content-substitution adaptation cleanly per established pattern (round 5 #37 general-purpose + round 6 #38 pr-family + round 7 #41 general-purpose 2nd burn fallback + round 8 #46/#47/#48 precedents).

**Rule v1.5 first-class default**: reviewer §Step 4 (write reviewer_report.md) has 3 explicit branches (NOT a sub-pattern note):

### Branch A — Write tool available (default for most agents)
Reviewer uses Write tool to write `evidence/checkpoints/<batch>_reviewer_report.md` directly. AUDIT independence preserved.

### Branch B — Bash tool available, no Write tool
Reviewer uses `Bash(cat > <file> <<'EOF' ... EOF)` heredoc to write the file. AUDIT independence preserved. Precedent: round 3 #25 plugin-validator.

### Branch C — Neither Write nor Bash tool available (inline content substitution)
Reviewer returns reviewer_report.md content inline in final reply (markdown body 全文). Main session uses Write tool to save content verbatim per main-session-write substitution pattern. AUDIT independence preserved. Precedents: round 3 #29 plugin-dev:skill-reviewer + round 5 #37 general-purpose + round 6 #38 pr-family + round 7 #41 general-purpose 2nd burn fallback + round 8 #46 Plan + #47 claude-code-guide + #48 codex:codex-rescue v1.5 cut.

**verdicts.jsonl + summary.md**: same Branch A/B/C decision applies. AUDIT independence preserved across all branches.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (per V5)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: graduate from "1st-live-fire-EFFECTIVE" → **"STRONGLY VALIDATED post 2nd live-fire"** — production-ready protocol (round 7 batch 33 1st + round 8 batch 36 2nd live-fire of methodology + round 8 batch 37 2nd live-fire of procedural-enforcement codification baseline executor → rerun writer alternation)
- **G-MS-4 halt fallback**: graduate from "1st-live-fire-EFFECTIVE" → **"STRONGLY VALIDATED post 2nd live-fire"** — production-ready protocol (round 7 batch 32 1st + round 8 batch 36 2nd live-fire end-to-end halt-resume cycle)

═══════════════════════════════════════════════════════════════════
## Rule 合规 / 禁止 / 返回 (v1.4 carry-forward unchanged)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.4_final_2026-04-28/P0_reviewer_v1.4.md` §Rule 合规 / §禁止 / §返回.

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.2 | 2026-04-24 | post-P0 收官: 6-item fix matrix + 11 slot Rule D roster |
| v1.3 | 2026-04-27 | post P1 round 4 cut: roster 11→34 / matrix 6→13 / next-pool data/firecrawl/superpowers / AUDIT-mode prepend recipe |
| v1.4 | 2026-04-28 | post P1 round 7 cut EMERGENCY-CRITICAL: roster 34→43 / matrix 13→22 / next-pool pivot REMOVED data + firecrawl (skills not agents per O-P1-110); 24 v1.4 candidates round 5+6+7 absorbed |
| **v1.5** | **2026-04-28** | **post P1 round 8 cut + reconciler closure**: (a) Rule D roster expanded 43 → 48 slots cumulative (4 round 8 batch 35-37 + v1.4 cut #44 + v1.5 cut #48 = 5 NEW slots; family pool partition: 4 EXHAUSTED post round 8 = vercel + plugin-dev + feature-dev round 4 + pr-review-toolkit round 8 batch 35 6/6 COMPLETED + 9 active families post round 8); (b) v1.5 fix verification matrix expanded 22 → 25 items A-Y (3 NEW v1.5 items W-Y covering N15-N17 = 8 v1.5 candidates V1-V8 round 8); (c) AGENT-vs-SKILL roster doc NEW §0 per V1 (registered AGENTS list vs SKILLS-loaded-via-Skill-tool list + Rule D pre-allocation lint protocol HALT-on-mismatch); (d) §Step 4 Write-tool-less default codification first-class 3 explicit branches per V7 (Branch A Write tool / Branch B Bash heredoc / Branch C inline content substitution main-session-write); (e) STATUS PROMOTIONS N14 + G-MS-4 STRONGLY VALIDATED post 2nd live-fire production-ready protocols; (f) v1.4 cut reviewer slot #44 omc:document-specialist AUDIT verdict PASS 22/22 historical record; (g) round 8 round-8 NEW patterns documented: pr-review-toolkit family 4th-agent intra-family depth burn FIRST 4th-agent for ANY family in P1 cumulative + Plan family INAUGURAL single-agent burn pivoted from SKILL + claude-code-guide family INAUGURAL 9th family pool + codex:codex-rescue v1.5 cut INAUGURAL 10th family pool external runtime; (h) v1.5 EMERGENCY-CRITICAL absorption 8 candidates: writer-side N15-N17 + matcher-side 1 NEW discrepancy marker [NEW7_xpt_parent_caption_violation] + reviewer-side 25-item matrix + AGENT-vs-SKILL roster + Write-tool-less default. NOT behavior change — reviewer task structure (Step 1-4) / verdict enum / Rule D 强制 全 carry-forward unchanged. |
