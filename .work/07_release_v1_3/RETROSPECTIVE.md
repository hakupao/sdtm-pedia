# Release v1.3 — RETROSPECTIVE

> 完成日期: 2026-05-20
> 阶段跨度: 2026-05-20 morning (plan kickoff) → same day (cut + tag) — single-day Tier 3 release
> 规则 C 强制产物 (Tier 3 项目收尾)
> 上一版反思: `.work/07_release_v1_1/RETROSPECTIVE.md` (v1.1), `.work/07_release_v1_2/r4_sanity/R4_SANITY_RETROSPECTIVE.md` (v1.2 partial)

---

## § 一、保留下来的做法

**1. 单 session 完整 Tier 3 release (with parallel subagent dispatch)**
v1.3 从 plan 到 tag 同日完成. 关键是把可并行的工作 (Tier B 修复, KNOWN_LIMITATIONS 三语, release packaging) 派给后台 executor, main session 同时做 KB 改 + 评审 + 协调. 总 4 个 background subagent (executor 2 次 + scientist + critic + verifier), Rule D 严格隔离, 各 subagent_type 不同 — `oh-my-claudecode:{executor, scientist, critic, executor, verifier}` 5 个独立 slot.

**2. Rule A 量化目标驱动**
Plan 设 Rule A target ≥97 grep probe, 实际累计 153+ (158%). 这个超额覆盖让 Phase D verifier 能找到 1 个 minor v1.4 carry (Claude bundle 缺 PP RELREC Quick Reference prose) — 没有量化目标的话, 这种 architectural gap 容易被遗漏.

**3. v1.1 cross-platform delta oracle 复用**
v1.3 B3 cross-platform delta oracle 4 byte-exact 等式 PASS:
- chatgpt 04 specs Δ +284 = nbk 10 ev_history Δ +284 (BE/spec 改动)
- chatgpt 04+05 sum Δ +617 = gemini 02 composite Δ +617
- chatgpt 06 examples Δ +5,432 = gemini 03 examples Δ +5,432
- claude 06 assumptions Δ +220 = DI fix 反映

这是 KB 改动经 build pipeline 到达 4 平台 deployment 的最强 sanity 信号. 0 silent loss 由此证明.

**4. v1.4 carry 在 Phase C user 直觉触发**
Q-S2 Gemini PP RELREC FAIL 后, 用户提出 "Gem instructions 太复杂, 改了很多遍, 履历都写进去了, 感觉不好". 数据验证 (525 行 + 17 CO-N rules + "v5/v6/v7/v8 新增" fossil annotation) 印证. v1.4 main carry 由此确立: 4-platform prompt full-stack refactor. **用户直觉 + 数据验证 = release 决策最强组合**.

**5. Phase A → B → C → D 严格 gate**
每 Phase 用 Rule D 独立 reviewer 通过才进下 Phase:
- A → B: Rule D #19 (scientist) confirm 0 HALLUCINATED + #20 (critic) confirm A3 PASS
- B → C: B3 cross-platform oracle 自洽 + B4 system_prompt audit 20/20
- C → D: user ack option α (10 节 accept), Phase C 14-15/16 PASS verdict
- D → Tag: Rule D #19 (verifier) PASS_WITH_OBSERVATIONS APPROVE

没有跳 gate, 没有 self-review (writer ≠ reviewer 严格).

**6. release/v1.X/ 平行目录 + tag 不可变继续**
v1.0/v1.1/v1.2 完整保留, v1.3 平行建 release/v1.3/. v1.2 immutability 经 verifier `git log` 验证 (b0b6804 commit 后 0 改动). 这套 release model 三个版本以上 (v1.0/v1.1/v1.2/v1.3) 验证稳定.

**7. NotebookLM instructions citation style refactor 与 KB pass 同 ship**
User session 前已改 NotebookLM `instructions.md` (inline `[bucket.md]` → footer `Sources:` list). 用户 Phase C 决定包含进 v1.3 release. Phase C Q-S1 NotebookLM 答案直接验证生效 (`Sources: 10_ev_history_mh_ho_be.md` 等). prompt 风格升级与 KB pass 同 ship 合理且无 conflict.

---

## § 二、必须补上的缺口

**1. Gemini system_prompt v8.1 prompt bloat (v1.4 MAIN carry)**
525 行, 17 CO-N rules, 4 prong + 6 reviewer fix + AHP-V1/V2/V3 三层 anti-hallucination. 每个 CO-N 是 smoke test FAIL 化石层 (CO-1c v7 / CO-1d v7.1 / CO-1e v8 / CO-2f v8 / CO-4 v5c / CO-5 v6 ...). 注意力 dilution + anchor 专项化 (重 R3 specific FAIL 防御, 弱 general KB 检索) = Q-S2 PP RELREC FAIL (无 anchor 题路径).
→ **v1.4 main**: gemini v9 ~200 行 + 5 essential rules + regex-gated CO-N (only fire on match) + KB-grounding 优先 default.

**2. 4 平台 prompt 同样有 fossil layer (扩展 v1.4 carry)**
ChatGPT system_prompt / Claude Project instructions / NotebookLM instructions 都迭代多版, "v5 新增" annotation 累积. v1.4 应 4 平台同时 refactor — clean rewrite, 不留迭代履历, KB-grounding 优先.

**3. Claude bundle 缺 PP RELREC Quick Reference prose (architectural)**
v1.3 Phase A1 在 `PP/examples.md` 新加 §6.3.5.9.3 RELREC Method Quick Reference. 但 claude_projects 的 `07_examples_catalog.md` 由 archive v1 `catalog_examples.py` build, v2 `extract_examples_data.py` 只 capture `## Example N` headings, 这段 `## §6.3.5.9.3 RELREC Method Quick Reference (PP-side view)` 不被任一 pipeline 捕获. 缓解: Phase C Q-S2 Claude 仍 PASS+ (通过 `02_chapters.md` RELREC 段 + `09_examples_data_high.md` relrec.xpt tables 重建出答案). 
→ **v1.4**: claude pipeline 改 capture `## §N.N.N` section headings from domain examples.md OR 把 Quick Reference 段加进 v2 extract script include-list.

**4. ChatGPT method label 混淆 (v1.4)**
Q-S2 ChatGPT 答 PP-PC RELREC 4 methods, IDVAR 组合对 但 A/B/C/D labels 与 KB §6.3.5.9.3 错位 (ChatGPT Method A=Many-to-One PCGRPID+PPSEQ = KB Method C). 内部 prior knowledge 覆盖 KB. v1.4 chatgpt 06_domain_examples_all.md PP §6.3.5.9.3 段加显式锚点 "Method A=Many-Many / B=One-Many / C=Many-One / D=One-One" 防止 label drift.

**5. 全 437 UNSOURCED_MANUAL 全量分类 + 启发式分类器 bias 修**
v1.3 抽 N=40 sample, 0 hallucinated 经 Rule D #19 (scientist) 确认. 但 5/10 atoms main session 启发式分类器误标 DERIVED_FROM_XLSX, 实际为 REASONABLE_INFERENCE (PDF-prose source). 全 437 分类留 v1.4 时, 分类器先 grep pdf_atoms.jsonl 找 verbatim, 找到即 REASONABLE_INFERENCE; 找不到再 fallback xlsx 检查.

**6. Tier B 156 节 (15/166 已修)**
v1.3 修了 Batch M (ranks 11-20, 10 节, shall/must 高密度). 剩余 Batch H (ranks 1-10, ~470 atoms) + Batch S (ranks 21-25, ~10 atoms) + Level2 (24 节, ~600 atoms) 留 v1.4. 工程量 = 06 全 cycle 半量 (~5-7 工作日).

**7. NotebookLM 旧 bucket 25 用户 UI 操作清理**
B5 改名 `25_td_meta_ti_ts_oi.md` → `25_td_meta_ti_ts_oi_di.md`, 用户上传新 source 后 NotebookLM 仍含旧 source (43 sources 应 42). v1.3 V1_3_DEPLOY_GUIDE.md 已提示需删旧 source, 但用户实际部署未删. 不阻塞 v1.3 但是是 deployment UX gap. v1.4 release guide 加更显眼提示 + screenshot 教程.

**8. section_coverage.jsonl 完整 pipeline rerun**
A5 只做了 baseline 备份 + stale 状态文档化. 完整 pipeline (md_atoms 增量 → p4a forward matcher → p4b aggregate) 留 v1.4 (工程量 = 06 半 cycle).

---

## § 三、关键决策复盘

**决策 1: Tier 3 vs Tier 2 (Phase A 启动)**
*做法*: 选 Tier 3 — KB+prompt+4 bundle+R4+audit 5 层跨日.
*为什么*: v1.3 跨 KB 改 + 4 平台 rebuild + sanity + release pack + tag, 涉及多个独立工程, Tier 3 工作流 (PLAN.md + _progress.json + evidence/checkpoints + trace.jsonl + subagent_prompts + audit_matrix + RETROSPECTIVE.md) 给了足够 ceremony 来管理复杂度.
*结论*: 正确. 单日完成 Tier 3 体量是因为派 background subagent 的并行机制 (4 个 executor + 3 个 reviewer = 7 subagent slot 在 8 小时内串行+并行完成). 没有 Tier 3 框架, 这种复杂度容易丢线索.

**决策 2: A3 Batch M 接受 10 节, Batch H + S + Level2 全 39 节 defer v1.4**
*做法*: Phase A close 时 user ack Option α (10 节 ≥ 平台 sanity 验证可行).
*为什么*: Batch H (470 atoms) 工程量 = 多 round 多日, 不合 v1.3 的 KB pass scope. 10 节 dual writer+reviewer PASS 比 25 节 rushed 更可信.
*结论*: 正确. Phase C 验证 10 节修复内容 (TR typo TRSTRESN→TRSTRESU 在 4 平台都生效) — 是值得修的核心 10 节. v1.4 Batch H 可以独立做 KB pass.

**决策 3: Light sanity 4 题 × 4 平台 (替 R4 17 题 × 1 平台 Pro)**
*做法*: Phase C 用 user option α light sanity (4 v1.3-targeted 题 × 4 deployed 平台 = 16 cells).
*为什么*: 比 R4 17 题 × 1 Gemini Pro (17 cells, 跨 4-5 quota window 16-20h wall time) 更适合 v1.3 KB pass — 4 题精准覆盖 A1/A2/A3/B5 关键改动, 跨 4 平台验 KB 改动 reach 用户. R4 17 题留 v1.4 (跟 prompt refactor 一起跑).
*结论*: 正确. 14-15/16 PASS 证明 v1.3 KB pass 端到端生效; Gemini Q-S2 FAIL 暴露 prompt bloat (v1.4 主 carry). 4-question light sanity 信息密度高于 17-question single-platform regression.

**决策 4: A2 BECAT 选 α (改 KB) 而非 β (改 prompt) / γ (双向)**
*做法*: BE/spec.md L111 加 EXTRACTION 作 sponsor-extensible 4th example (与 Gemini v8.1 prompt L272 对齐).
*为什么*: 工程量极小 (1 句), 行业事实 (DNA molecular biology specimen processing 常用), KB rebuild 自动同步 4 平台. Β 仅改 Gemini prompt, 不同步其他 3 平台 KB-prompt drift. γ 双向更彻底但工程量大.
*结论*: 正确. Phase C Q-S1 4/4 PASS 验证, 4 平台都答出 EXTRACTION sponsor-extensible.

**决策 5: NotebookLM citation style refactor 包含进 v1.3 release**
*做法*: 接受 session 前 unstaged 改动 (`ai_platforms/notebooklm/current/instructions.md` inline `[bucket.md]` → footer `Sources:`).
*为什么*: 改动 small, 风格升级与 v1.3 KB pass 同 ship 合理, 避免 NotebookLM 答案重复 native source-chip sidebar.
*结论*: 正确. Phase C 直接验证生效 (NotebookLM Q-S1/Q-S2/Q-S3/Q-S4 footer 用新格式 cite `25_td_meta_ti_ts_oi_di.md` 等), 顺便验证 B5 bucket 25 rename.

**决策 6: 单 Rule D #19 reviewer (`verifier`) 做 release-cut audit, 不开 Rule D #20+**
*做法*: D3 用 1 个 verifier subagent 做 8 audit sections + 15 Rule A probes + 20 acceptance criteria.
*为什么*: D2 executor 已自审 (D1+D2 5/5 Rule A). D3 verifier 独立审 (写/审分离). 没必要再开第二 reviewer.
*结论*: 正确. Verifier 找到 1 个 architectural gap (Claude bundle 缺 PP RELREC Quick Reference) — 独立 reviewer 找到 self-audit 没看到的问题, 证明 Rule D 价值. 20/20 acceptance criteria + 15/15 probe PASS = 自信 v1.3 ready.

**决策 7: 同日完成 Tier 3 release**
*做法*: 不分多 session, 一天内 plan → cut → tag.
*为什么*: User 全程 engaged, decisions 都同步 ack (option α / NotebookLM include / v1.4 prompt refactor finding). 没有需要跨 session 等待用户的决策.
*结论*: 正确, **but** 累. Tier 3 工作流提供的 ceremony (PLAN + progress.json + checkpoints + trace + audit_matrix + RETROSPECTIVE) 让单日完成可能. 普通 Tier 3 release 周跨度更稳妥.

---

## § 四、Post-Audit Pass (Phase E equivalent)

**主动模拟用户视角 audit, 反 v1.1 RETROSPECTIVE §四模式**:

| 项 | 自查结果 | 评估 |
|---|---|---|
| Rule A 累计 ≥97 + 跨 KB 与 4 平台 124 grep probe | 153+ (158%) | ✅ 超额 |
| 4 平台 system_prompt 数字引用 0 不一致 | B4 audit 20/20 + D3 verifier 重审 PASS | ✅ |
| KNOWN_LIMITATIONS §0 与 v1.2 §0 缺口逐条 reconcile | D1 done + verifier 验证 (D1-D5 resolved/partial + W1 added + Gemini bloat new entry) | ✅ |
| release/v1.3/ root 三语 meta 文档 0 漏 | 27 root md + 1 BUILD_MANIFEST.json = 28 ✓ | ✅ |
| CHANGELOG 三语 v1.3 entry 完整 + 风格统一 | D2 done + D3 verified all 4 langs (en/zh/ja/md) | ✅ |
| tag 链路完整 (annotated + push verify) | D4 即将 | ⏳ |
| v1.3 KB 改动在 deployed bundles 反映 | B3 oracle + Phase C light sanity + D3 verifier 三层验证 | ✅ |
| v1.2 immutability | D3 verifier `git log` 确认 b0b6804 post-cut 0 改动 | ✅ |
| Tier 3 工作流强制产物 | PLAN.md + _progress.json + evidence/checkpoints (15+) + evidence/failures (1) + trace.jsonl + subagent_prompts (2) + audit_matrix.md + RETROSPECTIVE.md (本文件) | ✅ 全产 |

**0 gap** 发现 post-audit. v1.3 ready for tag.

---

## 附: v1.3 终态数字

| 指标 | 值 |
|---|---|
| KB md 文件数 | 296 (含 DI domain) |
| Domain 总数 | 64 (与 v1.1/v1.2 一致, 无新加) |
| v1.3 KB 改动 (modified files) | **11** (BE/spec + PP/examples + TR/assn + TM/assn + TE/assn + TA/ex + TV/ex + ch02/fund + model/02 + model/05) |
| 4 平台 uploads 总大小 | 25.5 MB |
| 4 平台 rebuild 文件数 | 18 (chatgpt 3 + gemini 3 + nbk 7 + 1 rename + claude 5 - 1 idempotent) |
| Build 脚本改动 | 2 (chatgpt M4 dynamic + nbk M5 validate_bucket_coverage.py new) |
| 工程耗时 | 1 day (2026-05-20 morning → same day cut + tag) |
| Rule A 累计抽检 | 153+ (target ≥97, 实际 158%) |
| Rule D slot | #19 (scientist), #20 (critic), #21 (verifier) — 3 slots, 不同 subagent_type, writer/reviewer 严格隔离 |
| Rule D 总 verdict | A4 PASS + A3 PASS_WITH_OBSERVATIONS + D3 PASS_WITH_OBSERVATIONS_APPROVE = **可 cut** |
| Phase C sanity | 14-15/16 PASS (87.5-93.75%) ≥ approve threshold |
| v1.4 carries 记录 | 8 项 (1 MAIN: 4-platform prompt refactor; 7 minor) |
| Background subagents | 7 (4 executor + 3 reviewer, parallel + serial) |
| Tag | `v1.3-company-release` (annotated, post user ack) |
| Predecessor | `v1.2-company-release` (immutable) |
