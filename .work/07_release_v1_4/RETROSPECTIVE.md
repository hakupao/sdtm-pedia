# v1.4 Release RETROSPECTIVE (规则 C 强制, Tier 3)

> **Tag**: `v1.4-company-release` (cut 2026-05-22)
> **Predecessor**: `v1.3-company-release` (2026-05-20)
> **Tier**: 3 (>15 step, 多天, prompt + sanity + release + minor 多线联动)
> **Session arc**: 2026-05-20 PM kickoff → 2026-05-22 cut (~2 working days)

---

## 一. 保留下来的做法 (continue doing)

### 1.1 测试停 / 优化继续 — 分级维护模式 (Gemini 决策)

v1.4 最关键的决策是 **Gemini 平台从"4 平台锁步"切到"维护但不 sanity"模式**, 不是简单 abandon。这种**分级维护**模式值得纳入今后多平台 release 范式:

- Tier A (full lifecycle): ChatGPT / Claude / NotebookLM — KB 改动 + 平台 sanity + cross-platform 矩阵
- Tier B (maintenance only): Gemini — KB 改动流入, prompt 优化继续, 但**无 sanity 覆盖, 用户自验**

理由:
- Gemini Pro quota 约束 (~4 题/5h window) 长期阻碍全 17 题 R4
- v9 prompt B1 FAIL 表明单平台调优 ROI 递减
- 不轻易 abandon 平台 (用户已部署), 保留 best-effort 维护避免破坏现有部署

**写入未来 release 模板**: 平台不一定要么"全做"要么"不做", 维护态 + 优化态 + 测试态可以**独立切换**。

### 1.2 平台 prompt clean rewrite 的 fossil 移除范式

v1.4 主 carry 是 4 平台 prompt 全栈 refactor — 移除 v5/v6/v7/v8 多版本迭代累积的化石注释层, 把 KB-grounding 重新立为主路径。Gemini v8.1 525 行→v9 ~280 行 是最极端的 case, 但 ChatGPT/Claude/NotebookLM 都有类似的 fossil layer。

值得保留的工法:
- **Phase A 4 平台并行 writer subagent**: 主控派 4 个独立 writer (Rule D 强制 writer ≠ reviewer); 节省线性时间, 但**主控 cross-pollination 跨平台 review** 必须做 (否则 cross-platform parity gap 易漏, e.g. v1.4 B1 Gemini Q-S2 FAIL 就是 cross-platform anchor 没对齐)
- **A3.1 architectural pipeline fix 与 prompt rewrite 同 phase**: Claude bundle `## §N.N.N` capture pipeline 在 prompt rewrite 同 phase 内修, 不延后单独走 — 避免 sanity 阶段才发现 pipeline gap
- **Smoke test 必须覆盖跨平台 anchor parity**: A3.1 当时只 smoke 测 3 文件 (PP/PC/MB), 没察觉 cross-platform "Method label" anchor 在 Gemini 没同步加 — 此种 prompt-level anchor 应纳入 smoke 矩阵

### 1.3 Tier 3 工作流的 evidence/checkpoints/ + trace.jsonl 留底

v1.4 严格按 ~/.claude/templates/workflow-tier3.md 落 evidence 全套:
- `evidence/checkpoints/` 每 step 完成事件 (c0/c1/c2/c3/c4/c5/d/e) — 7 个 checkpoint 全齐
- `evidence/failures/` (Rule B 强制) — 本 release 无失败需归档
- `trace.jsonl` — phase 事件时间线 (phase_c_c1_complete / c2_complete / d_cut_complete / e_audit_complete)
- `subagent_prompts/` — 主要 subagent 派发的 prompt 留底
- `audit_matrix.md` — Rule A 抽检 × 各 phase 网格

**收效**: Phase E 独立 reviewer subagent 可以 read checkpoints 自检 (不需 main session 重述); 跨 session 接续不需重建上下文; 跨 release 复盘可比对 (v1.4 evidence 与 v1.3 v1.5 同结构)。

### 1.4 用户决策点 inline 处理 + 不阻塞 background subagent

v1.4 session 中遇到多个用户决策点 (Gemini drop framing, Q-S2 sanity skip, scope A/B/C 三选), 主控:
1. 把决策点显式列出来给用户 (不是隐式默认)
2. 等用户响应同时, 不该阻塞的工作继续 (e.g. 用户决策 Gemini drop 时, background C1/C2 subagent 仍在跑)
3. 用户 clarification 来了再 retro-update 前序框架 (e.g. ABANDONED → MAINTAINED_NO_SANITY)

**写入 future release**: 不预设用户决策 (Gemini abandon 不是 default), 显式提问 + 给选项 + 解释 implication; 用户改主意是常态, 框架要能 retro-update。

---

## 二. 必须补上的缺口 (must fix / carry to v1.5)

### 2.1 [HIGH] C1-bis: 全 LLM 驱动 pipeline rerun (md_atoms 增量)

v1.4 C1 只跑了 deterministic 的 p4b_section_aggregate.py, **md_atoms.jsonl + coverage_ledger.jsonl 仍是 May 11/12 pre-v1.3 状态**。v1.3 11 KB 文件 + v1.4 1 KB 文件 (PP/examples.md §6.3.5.9.3 mapping table) 的改动**未传入 atom 层**。

修法:
- 增量 detect 12 changed KB files (v1.3 + v1.4)
- LLM-driven P2 atom extraction (仅 changed files, 复用 v1.9.4 writer prompt)
- P4a forward matcher (新 atoms vs pdf_atoms.jsonl)
- P4b section aggregate (rerun)
- 时间预估: ~0.5-1 工作日 + Rule D reviewer

**v1.5 C1-bis 必跑**, 否则 section_coverage.jsonl 永久停在 v1.3 pre-state, 之后 Tier B repair 也会越积越多 gap。

### 2.2 [HIGH] C1-ter: 工程化 P6→P4b 自动触发 gate

C1 暴露一个**工程缺口**: v1.3 P6 T5 ledger 更新 (May 12 17:17) **从未自动传入 p4b_section_aggregate.py 重跑** — May 12 11:34 baseline 与 17:17 ledger 5h46m 不一致, 一直挂到 v1.4 C1 才被发现。

修法:
- 加 `Makefile` rule: `section_coverage.jsonl: coverage_ledger.jsonl md_atoms.jsonl pdf_atoms.jsonl` 自动跑 p4b
- 或 post-P6 commit hook: 任何 `coverage_ledger.jsonl` 改动 → 自动 trigger p4b rerun
- 加 checksum 校验: `section_coverage.jsonl` 生成时记录输入文件 md5, 后续可验证 staleness

**这是个 process 缺口, 不是数据缺口**。修一次, 后续 release 都受益。

### 2.3 [MED] C2 KB_INTERNAL_CROSSREF 新分类 + 3 deep paraphrase 手工分类

C2 N=80 抽检发现 5 NEEDS_HUMAN_REVIEW, 其中 2 atoms (`md_dmTR_ex_a002`, `md_dmEC_ex_a002`) 是 **KB-INTERNAL 跨域 cross-ref navigation notes** — 比如 "see TR/spec.md §X for detail" — 既不是 PDF paraphrase, 也不是 xlsx-derived, 是 KB 编写者的元 navigation。

修法:
- 启发式 classifier 加 KB_INTERNAL_CROSSREF 类 (regex `see (TR|EC|...)\/(spec|examples).md`)
- 3 deep paraphrase atoms 手工 / LLM-assisted review (atom-by-atom)
- 同步 reverse_ledger.jsonl 加入 new category

### 2.4 [MED] Claude system_prompt Method label anchor (post-Phase E findings)

Phase E reviewer 发现 Claude system_prompt 原本只有 KB-pointer ("PP §6.3.5.9.3 RELREC Quick Reference"), 没 inline Method label table。**已在 Phase E 后 hotfix** (`current/system_prompt.md` + `release/v1.4/self_deploy/claude/system_prompt.md` 都 sync), 但暴露 cross-platform anchor parity gap 没被 Phase A 4 writer subagent 工作流 catch。

v1.5 改进: Phase A writer 派发时, 主控**预先列出**所有题型 anchor (Method label / SDTMIG ch08 §8.3 RELREC / SUPP-- / 等), 每个 anchor 在 4 平台 prompt 全部 audit。

### 2.5 [MED] extract_examples_data.py `parents[3]` path bug — Phase 6.5 reorg-A 遗漏

`ai_platforms/claude_projects/dev/scripts/extract_examples_data.py` 在 Phase 6.5 reorg-A (commit `87573bd`) 被从 `scripts_v2/` 移到 `dev/scripts/`, 但 `REPO_ROOT = parents[3]` 没更新成 `parents[4]`。导致脚本运行时所有 28 高频域被 flagged "missing examples.md", 写 706-token 空 bundle。**v1.4 C5 rebuild 时撞到, 已修**。

但 reorg 同期可能还有其他类似 path bug **未发现**。

修法:
- v1.5 加 audit: scan `ai_platforms/` 所有 Python scripts 的 `Path(__file__).resolve().parents[N]`, 验证 N 对应实际 repo root
- 加 unit test: 跑一次 import + path resolution, 用 `assert (REPO_ROOT / "knowledge_base").exists()` 验证

### 2.6 [LOW] C3 NotebookLM screenshot 实拍

V1_4_DEPLOY_GUIDE.md §3.A.3 留 `[TODO]` — Chrome MCP 截图 `nbm_source_list.png` + `nbm_delete_button.png` 需用户登录态协作。v1.5 补。

### 2.7 [LOW] Tier B 156 节 + 全 437 UNSOURCED + Phase 7 RAG+KG (v1.3 carry, 仍 defer)

工程量 > v1.4 体量, 一直 carry。v1.5 / v1.6 应给 Tier B 单独 KB pass cycle (~5-7 工作日 dedicate)。

---

## 三. 关键决策复盘 (key decisions debrief)

### 3.1 Gemini drop framing pivot (ABANDONED → MAINTAINED_NO_SANITY_TEST)

**时间线**:
- 2026-05-22 早 user: "Gemini 不做了" → 主控编码为 ABANDONED (整平台 drop)
- 主控 Phase D 启动前 user 二次澄清: "Gemini 虽然不用继续测试, 但是该优化的部分, 还是要继续优化的"
- 主控 retro-update: ABANDONED → MAINTAINED_NO_SANITY_TEST, 把 Gemini v9 拉回 v1.4 in-scope (含 Method label anchor 同步)

**为什么早期编码 ABANDONED 错**:
- 用户口语 "不做了" 在 dev 工作中含义模糊 — 可以是"暂停", "降级", "abandon"
- 主控应**先列细分选项问** (sanity 停 / 优化停 / 整平台 drop, 三选), 而不是默认最重的解读
- 类似 v1.2 拍板 R4 α/β/γ 时主控有列选项, v1.4 Gemini 决策应同样处理

**写入未来**: 用户简短决策 → 主控**回响细分选项**确认, 不直接 commit 重解读到 _progress.json + KNOWN_LIMITATIONS。

### 3.2 Q-S2 sanity recheck skip 决策 (信任 grep-level 内容验证)

用户最终选 (C) 完整 scope 但又允许 skip Q-S2 UI sanity recheck — 这并非矛盾, 而是基于:
- Phase E reviewer 已独立 grep-verify Method label table 在 4 平台 bundle / prompt 都 PASS
- B1 sanity 12/12 PASS 已覆盖 v3/v9 prompt 主体行为
- Q-S2 复测重点是 KB-level mapping table → bundle propagate (内容验证, 非 prompt 行为验证) — grep 足够
- 跑 Chrome MCP UI 测耗时 ~30 min, ROI 不高

**写入未来**: sanity recheck **目的导向**, 不机械跑 — 当独立 review 已确认内容验证 + 行为验证两侧, UI 复测可 skip。

### 3.3 C1 pipeline rerun scope reduction (full LLM → deterministic p4b only)

v1.4 PLAN C1 原本期待 "完整 pipeline rerun", 实际 C1 subagent 发现:
- PLAN 引用的 `p4a_forward_match.py` 不存在
- 真实 p4a 是 LLM-driven batched extraction (Tier 3 工作量 4-6 sessions)
- 仅 deterministic p4b 可在 Phase C 内跑

C1 subagent **明智 scope reduce**, 跑 p4b + 把全 pipeline 推 v1.5 C1-bis carry。

**关键得失**:
- 得: v1.4 cut 不被 C1 阻塞 (~2 工作日内 cut)
- 得: 意外 settle 了 P6 T5 ledger 改动从未 propagate 的 stale 状态 (FULL_COVERAGE 101→137 改善)
- 失: 不能宣称 "section_coverage.jsonl 完整 reflect v1.3+v1.4 KB" — 必须 explicit document 为 v1.5 C1-bis carry

**写入未来**: PLAN 引用的 script / 工具如果不存在, **第一个 step 不是创建 script**, 而是**重评 scope** (是否真需要 / 有无替代路径 / 推迟可否)。subagent 不应硬扛 PLAN 字面要求。

### 3.4 KNOWN_LIMITATIONS §0 framing 与 _progress.json sync

v1.4 中 _progress.json 的 `gemini_platform_status` 字段经历了至少 2 次重写 (初始 ABANDONED → MAINTAINED_NO_SANITY_TEST), KNOWN_LIMITATIONS draft §0.A 同步重写。**两者必须 byte-aligned**, 不能一处改 _progress.json 而 KNOWN_LIMITATIONS 还停在旧 framing。

**写入未来**: _progress.json + KNOWN_LIMITATIONS draft + CHANGELOG draft 三者**共享 framing**, 任意一处改动**三处同步**。可考虑加 audit script: 对比三处 framing 关键词 (ABANDONED vs MAINTAINED_NO_SANITY 等), 不一致 warn。

### 3.5 Background subagent 派发模式 (C1 + C2 并行 + 主控 wait)

C1 + C2 都派 background opus executor (4 prong 估 1-2h 各), 主控 continue 其他工作。这种模式:
- ✅ 节省线性时间 (2 任务并行 vs 串行 ~2h vs ~4h)
- ✅ 主控不被 long-running task 阻塞
- ✅ subagent self-contained (no context cross-pollination)
- ⚠️ 主控需 explicit 描述 self-contained context (~300 行 prompt 各)
- ⚠️ subagent 输出 verdict + checkpoint, 主控 verify + integrate

**v1.5 改进**: 多 subagent 并行时, prompt 模板化 (Tier 3 工作流 subagent 派发 template) 节省主控写 prompt 时间。

---

## 四. v1.4 数据指标 + 验证

### 4.1 Phase 完成度

| Phase | Step | Status | Verdict | Carry |
|:-:|---|---|---|---|
| A | A1-A5 (4 platform writer + reviewer) | ✅ | PASS_WITH_OBSERVATIONS (Phase A 已 close 2026-05-20) | A3.1 §N.N.N capture + parents[3]→[4] path bug fix carry to v1.4 C5 |
| B | B1 light sanity 16 cells | ✅ | APPROVE (UI 15/16 = 12/12 ex Gemini) | Gemini Q-S2 FAIL → trigger Gemini drop discussion 2026-05-22 |
| B | B2 R4 17题 | N/A | abandoned (Gemini-only scope, drop 后无对象) | — |
| C | C1 section_coverage | ✅ | COMPLETE_WITH_CAVEAT | C1-bis full LLM pipeline rerun + C1-ter Makefile gate |
| C | C2 UNSOURCED N=80 | ✅ | COMPLETE_WITH_FINDING (0 HALLUCINATED + 5 NEEDS_REVIEW) | C2 KB_INTERNAL_CROSSREF new category + 3 deep paraphrase manual |
| C | C3 NotebookLM UX | ✅ | skeleton done | screenshot Chrome MCP 协作 |
| C | C4 Method label KB + 4-prompt anchor | ✅ | done (4 platforms 都同步) | — |
| D | Release cut artifacts | ✅ | APPROVE (Rule A 5/5 PASS) | tag deferred to F |
| E | Post-audit pass | ✅ | APPROVE (Rule A 10/10 PASS, 0 HIGH + 1 MED Claude anchor hotfix + 2 LOW) | — |
| F | RETROSPECTIVE + commit + tag | 🟡 in flight | — | — |

### 4.2 Rule A 累计

- Phase A: per-step probes (见 audit_matrix.md)
- Phase B B1: 16 cells = 16 probes (12 PASS post 3-platform filter)
- Phase C C1: 5 probes (3 PASS, 1 PASS_WITH_CAVEAT, 1 FAIL_BY_DESIGN — KB delta not propagated, v1.5 carry)
- Phase C C2: 10 probes (10/10 PASS)
- Phase D: 5 probes (5/5 PASS)
- Phase E: 10 probes (10/10 PASS)
- **Total: 56+ probes (v1.4 累计)**

### 4.3 Rule D 独立 reviewer slots used

| Slot | Subagent type | Phase | Verdict |
|:-:|---|:-:|---|
| 22 | pr-review-toolkit:code-reviewer | A.A5.1 (Gemini reviewer) | PASS_WITH_OBSERVATIONS |
| 23 | oh-my-claudecode:scientist | A.A5.2 (ChatGPT reviewer) | PASS_WITH_OBSERVATIONS |
| 24 | oh-my-claudecode:critic | A.A5.3 (Claude reviewer ×2 attempt) | PASS_WITH_OBSERVATIONS (post fix) |
| 25 | oh-my-claudecode:verifier | A.A5.4 (NotebookLM reviewer) | PASS_WITH_OBSERVATIONS |
| 26 | oh-my-claudecode:verifier | E (post-audit) | APPROVE |

Writer ≠ reviewer 严格保持 (writer 全部 `oh-my-claudecode:executor`)。

### 4.4 4 平台部署文件清单 (release/v1.4/self_deploy/)

| 平台 | 文件 | 状态 |
|---|---|---|
| ChatGPT | system_prompt.md (119L v3) + uploads/06_domain_examples_all.md (rebuild) + tutorial.{en,zh,ja}.md (v1.3 inherit) | ✅ |
| Claude | system_prompt.md (133L v3 + Method label anchor 2026-05-22) + uploads/09_examples_data_high.md (3268L A3.1 fix) + tutorial.* | ✅ |
| NotebookLM | instructions.md (156L v3) + uploads/16_fnd_pharma_pc_pp.md (rebuild) + tutorial.* | ✅ |
| Gemini | system_prompt.md (292L v9 + Method label anchor 2026-05-22) + tutorial.* | ✅ MAINTAINED_NO_SANITY_TEST |

---

## 五. 下个 release (v1.5) 建议入口

**主线候选 (3 选 1)**:
- **(A) Tier B 全量 KB pass** (~5-7 工作日): 156 节修复 (Batch H 1-10 ~470 atoms + Batch S 21-25 ~10 atoms + level-2 24 节 ~600 atoms). 与 C1-bis 同 phase, 顺带 P2 增量 + P4a forward match + P4b rerun.
- **(B) Phase 7 RAG + KG 启动**: 设计已完成 (`docs/DESIGN_RAG_KG.md`), 实施前 5 步待办. 与 prompt refactor 解耦.
- **(C) 维护期 micro-release**: C1-bis + C1-ter Makefile gate + C2 KB_INTERNAL_CROSSREF + C3 screenshot + Claude anchor cleanup. 不引入新主线, 仅闭 v1.4 carries.

推荐 (A) — Tier B 全量是 v1.3+v1.4 最大未做项, 影响知识库 ~1080 atoms 完整度 (~10% 知识库体量)。

---

(写入: 2026-05-22 Phase F by main session; Rule C 三段齐备 ✓ 保留/缺口/复盘)
