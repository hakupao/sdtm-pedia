# v1.4 Audit Matrix — Rule A 抽检 × Phase 网格

> 累计目标 ≥97 抽检 (v1.3 实际 153+, 158% over-coverage)
> 创建: 2026-05-20 PM (Phase A0)
> 更新协议: 每 step 完成时 append 一行, 跟 `_progress.json.rules.A.applied[]` 同步

## 累计 status

| Rule A 维度 | Target | Applied | PASS | FAIL | Notes |
|---|:-:|:-:|:-:|:-:|---|
| A1 Gemini v9 essential rules + 0 fossil + regex-gated CO-N | 5 (writer) + 5 (reviewer) | 10 | 9 (5 writer + 4 reviewer strict) + 1 reviewer borderline 282L | 0 | ✅ Writer 5/5 + Reviewer (pr-review-toolkit:code-reviewer slot #22) PASS_WITH_OBSERVATIONS — 4 LOW + 1 MED (F3 Q2 KB-grounding defer Phase C), no HIGH, promote OK after user ack |
| A2 ChatGPT v3 essential rules + 0 fossil + method label anchor | 5 (writer) + 5 (reviewer) | 10 | 10 | 0 | ✅ Writer 5/5 + Reviewer (scientist slot #23) PASS_WITH_OBSERVATIONS — 0 HIGH/MED + 2 LOW. **Method label BYTE-ALIGNED**: KB §6.3.5.9.3 Method A=Many-to-Many ↔ v3 prompt A=Many-to-Many ✅; v1.3 Q-S2 drift CORRECTED |
| A3 Claude v3 attempt 1 writer | 5 | 5 | 5 (strict, missed semantic) | 0 self | ⚠️ Writer 5/5 self strict but critic adversarial found 6 issues (see attempt 2 row) — attempt 1 archived `evidence/failures/a3_claude_attempt_1.md` per Rule B |
| A3 Claude v3 attempt 1 reviewer | 5 (reviewer) | 5 | 0 (NEEDS_REVISION) | 5 | ❌ NEEDS_REVISION — critic (slot #24 attempt 1) escalated ADVERSARIAL, 3 CRITICAL (file count + table contradiction + Coverage Notes archive refs) + 3 MAJOR (rationale line count + R1-R5 positions + lost named-file routing) |
| A3 Claude v3 attempt 2 (main session writer + critic re-audit) | 6 findings verify | 0 | 0 | 0 | ⏳ Main session surgical fix 120→133L applied; critic re-audit slot #24 attempt 2 in flight |
| A3.1 Claude pipeline fix (## §N.N.N capture; PP/PC/MB smoke) | 3 + reviewer 4 | 7 | 7 | 0 | ✅ PASS — main session edit + critic A5.3 separate verdict APPROVED with reservations (regex correct on 9 edge cases, 0 cross-ref regression across 63 domains, no double-emission risk, smoke 3/3) |
| A4 NotebookLM v3 essential rules + 0 fossil + footer citation preserved | 5 (writer) + 5 (reviewer) | 10 | 10 | 0 | ✅ Writer 5/5 + Reviewer (verifier slot #25) PASS — footer Sources SEMANTIC EQUIVALENT (behavior preserved, not byte-byte; example 3→2 buckets illustrative only); 6 LOW/MED observations all accepted, 0 blocker |
| B1 light sanity 4 题 × 4 平台 (KB-grounding default 不 regression) | 16 paper + 16 UI = 32 | 15 PASS (UI) + 13 PASS (paper) | 0 PARTIAL (UI) / 3 PARTIAL (paper) | 1 FAIL (UI: Gemini Q-S2) / 0 FAIL (paper) | ✅ **APPROVE** (UI 15/16). Paper-level 13/16 PASS + 3 PARTIAL (Claude bundle KB gap, v1.3 RETRO §二.3); **UI-level 15/16 PASS** post user UI deploy via Chrome MCP — 3 paper PARTIAL → UI PASS+ (reasoning bridge + v1.4 A3.1 §N.N.N pipeline 实战命中 ★★); 1 NEW UI FAIL Gemini Q-S2 Method label drift (v9 prompt 缺 Method label anchor, ChatGPT v3 L78 有, v1.5 carry). Evidence: `b1_sanity/b1_aggregate.md` (paper) + `b1_UI_aggregate.md` (UI) + 8 detail files |
| B2 R4 17 题 × 1 Gemini v9 (anti-cheating long-tail) | 17 | 0 | 0 | 0 | pending Phase B (or defer β) |
| C1 section_coverage rerun (status flag 自洽) | 5 | 0 | 0 | 0 | pending Phase C |
| C2 UNSOURCED N=80 (HALLUCINATED=0 + cat consistency) | 80 | 0 | 0 | 0 | pending Phase C |
| C3 NotebookLM bucket 25 UX 教程 (screenshot 完整性 + 红色警告) | 3 | 0 | 0 | 0 | pending Phase C |
| C4 KB label anchor (PP/examples.md + 4 平台 uploads cross-check) | 4 | 0 | 0 | 0 | pending Phase C |
| D3 verifier audit (≥15 probes 类似 v1.3) | 15 | 0 | 0 | 0 | pending Phase D |
| E1 Post-audit self-check | 6 | 0 | 0 | 0 | pending Phase E |
| **累计** | **≥97** (target) | **16** (B1 done) | **13 PASS + 3 PARTIAL** | **0** | Phase A 各 cell 已 logged via per-step rows; B1 done 16; B2/C/D/E pending |

## 每 step 详细 (append-only)

### Phase A — 4 平台 prompt clean rewrite

(待 Phase A 启动后 append)

### Phase B — Sanity validation

**B1 Light Sanity** (2026-05-20 PM, paper-level, deterministic, 不依赖 UI deploy)

| Cell | Layer 1 (prompt) | Layer 2 (KB) | Verdict |
|---|---|---|:-:|
| Q-S1 Gemini | PASS R1+R3 biospecimen L94-101 | PASS `02_*.md:1177` 完整 CDISC Notes 段 | PASS |
| Q-S1 ChatGPT | PASS R1 L47+R3 L67 | PASS `04_*.md:1081` 完整 byte-identical | PASS |
| Q-S1 Claude | PASS R1 L45+R3 L64 | **PARTIAL** — bundle 缺 "sponsor-extensible" claim (v1.3 RETRO §二.3 arch gap) | PARTIAL |
| Q-S1 NotebookLM | PASS R1 L16+R3 L39 | PASS `10_*.md:947` 完整 | PASS |
| Q-S2 Gemini | PASS R1+R2 AHP | PASS `03_*.md:4659+` 4 Methods | PASS |
| Q-S2 ChatGPT | PASS R1+R2+R3 L78 Method label anchor | PASS `06_*.md:4650+` 4 Methods | PASS |
| Q-S2 Claude | PASS R1+R2 | **PARTIAL** — Method D 0 hits + `## §6.3.5.9.3` Quick Ref gap (v1.4 A3.1 script fix done, rebuild pending C4) | PARTIAL |
| Q-S2 NotebookLM | PASS R1+R2 | PASS `16_*.md:555+` 4 Methods | PASS |
| Q-S3 Gemini | PASS R2 AHP regex | PASS `02_*.md:19561` | PASS |
| Q-S3 ChatGPT | PASS R2 AHP regex | PASS `04_*.md:17524` | PASS |
| Q-S3 Claude | PASS R2 AHP | PASS `05_mega_spec.md` TRSTRESN/TRSTRESU row | PASS |
| Q-S3 NotebookLM | PASS R2 AHP L26 | PASS `17_*.md:164` | PASS |
| Q-S4 Gemini | PASS R2 AHP | PASS `02_*.md:4224` + `04_*.md:1653` 完整 SDTMIG-MD + study reference | PASS |
| Q-S4 ChatGPT | PASS R2 | PASS `05_*.md:392` 完整 | PASS |
| Q-S4 Claude | PASS R2 | **PARTIAL** — `06_assumptions.md:331` truncated at "SDTMIG-MD", 缺 "study reference dataset" 直接 binding | PARTIAL |
| Q-S4 NotebookLM | PASS R2+bucket 25 | PASS `25_*.md:726` 完整 | PASS |

**B1 Aggregate (paper-level)**: 13 PASS + 3 PARTIAL + 0 FAIL = 13/16 strict (3 PARTIAL Claude bundle KB gap)

**B1 Aggregate (UI-level Chrome MCP, post user UI deploy)**: **15/16 PASS** (11 PASS+ / 4 PASS / 0 PARTIAL / 1 FAIL) → **APPROVE**
- 3 paper PARTIAL → UI PASS+ via reasoning bridge + v1.4 A3.1 §N.N.N pipeline 实战命中 ★★
- 1 NEW UI FAIL: **Gemini Q-S2 Method label drift** ❌ — v9 prompt 缺 Method label anchor (ChatGPT v3 L78 有), cross-platform parity gap, v1.5 carry
- Evidence: `b1_sanity/evidence/q_s{1,2,3,4}_UI_all_platforms.md` + `b1_UI_aggregate.md`

**Final B1 Verdict**: APPROVE (UI 15/16) with v1.5 carry "Gemini v9 prompt Method label anchor sync"

(B2/B3 待 Phase B 决策点)

### Phase C — Minor carries

(待)

### Phase D — KNOWN_LIMITATIONS + Release cut

(待)

### Phase E — Post-audit

(待)
