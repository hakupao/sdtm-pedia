# Gemini v8 Dry-Run Plan — 4 fail 题验证

> 起草: 2026-05-19 (post v8 draft + reviewer dispatch)
> 范围: 只跑 R3 4 FAIL 题 (Q3 / Q4 / Q11 / AHP1), 不跑全 17 题 (节省 cycle)
> 前提: reviewer (Rule D #16) PASS 或 PASS_WITH_OBSERVATIONS, 必修项已 reconcile
> 触发条件: 用户口头 ack 进 dry-run

---

## Phase A: Preflight (5-10 min)

**1. Reviewer reconcile (若有 finding)**
- 读 `evidence/v8_reviewer_audit.md`
- 若 PASS — 直接进 Phase B
- 若 PASS_WITH_OBSERVATIONS — 主 session 在 v8 prompt 中 apply HIGH/MED 修, 再进 Phase B
- 若 FAIL — 迭代 v8.1, 不直接 dry-run

**2. v8 system_prompt 部署到 Gemini Gem**
- 拷 `ai_platforms/gemini_gems/dev/v8_draft/system_prompt_v8.md` → Gemini Gem instructions (替换 v7.1)
- 不动 KB upload bundle (v1.1 仍有效, v8 只改 prompt 不改 KB)
- Gemini Gem URL: 用户提供 (从历史 r3 runner JS 中可找)

**3. Chrome MCP 4 题 dispatch 准备**
- 用 `.work/07_release_v1_1/r3/scripts/gemini_runner.js` (R3 已验证)
- 4 题清单 (verbatim from R3):
  - Q3 (A3 BE/BS/RELSPEC) — `SMOKE_V4.md` §2 Q3 题文
  - Q4 (B1 LB vs MB vs IS) — `SMOKE_V4.md` §2 Q4 题文 (3 scenario A/B/C)
  - Q11 (Dataset-JSON bonus) — `SMOKE_V4.md` §2 Q11 题文
  - AHP1 (LBCLINSIG probe) — `SMOKE_V4.md` §2 AHP1 题文

---

## Phase B: 4 题 dispatch (10-15 min)

**串行 dispatch (Gemini 单 tab, 不并行)**:

| 题 | 期望 verdict | 关键命中条件 (PASS) | 关键命中条件 (PASS+) | FAIL 信号 |
|---|:---:|---|---|---|
| **Q3** | **PASS** | response 含 BE/BECAT/BS/BSTESTCD/RELSPEC; 不含 AE/AESEV 主体 | + BSCAT 区分 + 5 CT codes + 引 IS Example | 主体仍讨论 AE/AESEV/AEGRPID |
| **Q4 A** (麻疹 IgG) | **PASS** | Scenario A 答 **IS** + ISBDAGNT=MEASLES VIRUS + ISORRES="1:128" | + Assumption 7a 引 + Example 5/8 | 答 LB or MB |
| **Q4 B** (ADA) | **PASS** (维持 R3) | IS + ISTSTOPO=SCREEN/CONFIRM/QUANTIFY | + 三层结构 | 答 LB |
| **Q4 C** (Mtb) | **PASS** (维持 R3) | MB + MCORGIDN + MBSPEC=SPUTUM | + MBMETHOD=MICROBIAL CULTURE | 答 IS or LB |
| **Q11** | **PASS or PARTIAL** | XPT v5 痛点 (8-char/200-char/no Unicode/external metadata) + Dataset-JSON v1.1 features + Define-XML 互补 | + FDA 2026 timeline | 主体讨论 AE/CM SDTM domain |
| **AHP1** | **PASS+** | 显式 "LBCLINSIG 非 v3.4 standard variable" + 提 LBCLSIG (8-char) 是标准 + 提 SUPP-- NSV 路径 | + Core=Perm + C66742 + LBNRIND 区分 | 答 CM 多药 / MH 协同 |

**evidence 记录**: 写到 `ai_platforms/gemini_gems/dev/v8_draft/dry_run_2026-05-XX/q<NN>_combined.md`, 模仿 R3 combined evidence 格式.

---

## Phase C: Verdict + 决策 (5 min)

**4/4 PASS (期望)**: v8 验证成功 → 进 v1.2 cycle 准备
- 主 session 写 `v8_dry_run_verdict.md` 总结 4 题 verdict + 与 R3 对比
- 派 Rule D 第 17 个 unique reviewer (e.g. `oh-my-claudecode:verifier`) cross-check 4 题 verdict
- 若 reviewer PASS → 用户 ack → v8 promote 到 `current/system_prompt.md`, 准备 v1.2 cut
- v1.2 cut 包含 Gemini system_prompt v7.1 → v8 substitute, 不改 KB uploads

**3/4 PASS, 1 FAIL**: 迭代 v8.1
- 失败题 root cause analysis → 调整对应 prong → 再 dry-run
- 失败如反复发生, 考虑是否 v8 设计 fundamental 问题, 升级 v8.x → v9

**≤2/4 PASS**: 设计层问题
- 暂停 v8, 主 session 写 v8_failure_analysis.md
- 评估 prompt-level 是否能修, 还是需 KB 改 / 模型升级 / 题库分类调整

---

## Phase D: Retro + commit (5-10 min)

**1. R3 dry-run retro 写入 `v8_dry_run_retro.md`** (Tier 1-2, 简化版 retro):
- §一 保留下来的做法 (4 prong 哪个最 effective)
- §二 缺口 (哪个 prong 没完全 hit, 需要 v8.1)
- §三 关键决策复盘 (e.g. 只跑 4 题不跑 17 全题是否够 / regex trigger 是否 verbose)

**2. SYNC_BOARD 更新 + _progress.json append v8_draft 工程记录**

**3. Commit (按 CLAUDE.md wrap-up checklist)**:
- 单 commit, descriptive message
- Push to main

---

## 风险与 contingency

**R1. Gemini Gem 部署 prompt 失败 (Gemini 平台问题)**
→ Fallback: 手工 paste system_prompt_v8.md 内容到 Gemini Gem instructions field, 不 rebuild KB

**R2. v8 prompt 长度超 Gemini 限制 (~30KB 限制)**
- 当前 v8 system_prompt_v8.md ~30KB, 接近 Gemini Gem instructions 限制 (8000 字符 strict / 30K tokens-ish 实测)
→ 若超: 主 session 压缩 v8 (优先压非 v8 改动段, 保 4 prong; 写 evidence/v8_compression_log.md)

**R3. 4 题中某题 PASS 但 mode 不同 (e.g. PASS but PARTIAL detail)**
→ 接受 PASS 进 v1.2, 但 evidence 记 caveat; 不强求 R3 PASS+ 全升级

**R4. Reviewer subagent timeout / 不返回**
→ 等 5-10 min, 若超时主 session 自审 (Rule D 退化为 self-audit, 标 caveat). 但本 cycle 风险低, reviewer 通常 5 min 内返回

**R5. Chrome MCP runner 失败 (e.g. Gemini SPA navigation bug)**
→ 复用 R3 dry-run runner (`ai_platforms/gemini_gems/dev/dry_run_2026-05-19/` selectors 已验证)

---

## 不在此 dry-run scope

1. **其他 3 平台**: ChatGPT v2.2 / Claude v2.6 / NotebookLM v2 R3 全 PASS 或 KB 限制, 不需 prompt 修. v8 仅 Gemini.
2. **17 全题回归**: 节省 cycle, 只跑 4 fail. 若 4/4 PASS, v1.2 cut 后可考虑 R4 跑 17 题全量 (类 R3).
3. **KB rebuild**: v8 仅 prompt 改, KB v1.1 uploads 维持. 不需重 build.
4. **v1.2 release cut**: dry-run PASS 后单独议题, 不在 dry-run 内.
5. **NotebookLM PUNT 评分规则修订**: R3 RETRO §二 缺口 4, 留 v1.2 spec 修订, 不在 v8 scope.

---

*Plan 完成 2026-05-19. Trigger: reviewer 返回 + 用户口头 ack 后 main session 执行.*
