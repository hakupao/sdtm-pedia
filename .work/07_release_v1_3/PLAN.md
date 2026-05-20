# Release v1.3 Plan — KB Pass + Prompt-KB Reconcile + 4-Platform Rebuild + R4 Full Regression

> **入口建立**: 2026-05-20 morning (post R4 sanity 5/5 PASS + v8.1 APPROVE)
> **上一版**: tag `v1.2-company-release` (Gemini-only prompt refresh v7.1 → v8.1)
> **本版定位**: **KB pass 级**, 兼修 prompt-KB 分叉, 走全栈 (KB → 4 平台 bundle → R4 regression)
> **Tier**: **Tier 3** (>15 step, 多天, KB+prompt+release 三层联动, 高 stakes)
> **终止条件**: tag `v1.3-company-release` cut + 4 平台 uploads 同步 + R4 17/17 ≥ baseline + RETROSPECTIVE.md 三段齐备 + post-audit pass 闭环
> **预估工期**: 5-8 工作日 (含 Gemini Pro quota 跨 cycle 等待)

---

## § 0. 背景: v1.2 收尾后的债务清单

v1.2 已 cut + tag verified (2026-05-19), R4 sanity 5/5 PASS + v8.1 APPROVE (2026-05-20 morning). 但下列 carries 留给 v1.3:

### 0.1 来自 v1.2 `KNOWN_LIMITATIONS.en §0` 的 5 项 deferred

| # | 项 | 类别 | 优先级 |
|:-:|---|---|:---:|
| D1 | R4 17-question full regression on Gemini v8.1 (sanity 5/5 已过, 全 17 题在 v8.1 未跑) | 测试 | HIGH |
| D2 | M2 candidate-count cap independent validation (sanity 题候选 <5, 阈值未触) | 测试 | MED |
| D3 | **BECAT EXTRACTION KB-prompt 分叉** (v8.1 prompt L272 列 EXTRACTION; KB BE/spec L111 只 inline COLLECTION/PREPARATION/TRANSPORT) | KB / prompt | HIGH |
| D4 | **437 UNSOURCED_MANUAL atoms** (06 P5 遗留, MD 有但 PDF 无, HALLUCINATED=0 但未定性) | KB | MED |
| D5 | **166 KB sections Tier B** (56 SIBLING_DROPPED + 110 CONTENT_TRUNCATED, 06 P6 Tier A 后停) | KB | MED |

### 0.2 来自 R4 SANITY RETROSPECTIVE (2026-05-20) 的 4 项 watch / 流程改进

| # | 项 | 类别 |
|:-:|---|---|
| W1 | PASS+ §1.2 strict 应否限 "AHP 专属" — sanity 中 Q1/Q5 非 AHP 也 PASS+ 合理 → KNOWN_LIMITATIONS §0 描述更新 | prompt 注释 |
| W2 | Pro quota 4 题/window 估计偏乐观 — future sanity plan 应预留 1 题缓冲 + verify quota status | 流程 |
| W3 | Flash-Lite 引入无关 framing 风险 (Q14 开头跑 CM 合并用药) — R4 全 17 题应 Pro 跑, 避 model mix | 流程 |
| W4 | Q1 model 不明示 (Gem default mode) — 测试第一步必须 verify mode picker 当前选项 | 流程 |

### 0.3 来自 06 旁枝 RETROSPECTIVE (2026-05-12) 的 6 项 缺口

| # | 项 | 优先级 |
|:-:|---|:---:|
| G1 | P4a 规格表变量行 IE 分类不彻底 (P7 抽样 12/60 误判) | LOW (verdict 标签层, 不影响 KB 内容) |
| G2 | P4a 同例表行 matcher 未检查行标识符 (6/60 WRONG) | LOW (同上) |
| G3 | **Tier B 166 节** (与 D5 同) | MED |
| G4 | **437 UNSOURCED_MANUAL** (与 D4 同) | MED |
| G5 | **PP RELREC linking 2 atoms OA-4 缺口** (PP/examples.md 缺 §6.3.5.9.3 ABC-123-0001/PPSEQ=1 vs PPSEQ=6) | HIGH (P7 唯一真实内容缺口) |
| G6 | section_coverage.jsonl stale (P6 T4 修复后未重跑 p4b_section_aggregate.py) | LOW (账本快照层) |

### 0.4 来自 v1.1 RETROSPECTIVE Post-Audit Pass 的 5 项 method-debt

| # | 项 | 类别 |
|:-:|---|---|
| M1 | system_prompt audit pass: grep 4 平台 system_prompt 中域数/文件数/段数引用, build script segment_count 交叉对比 | release 流程 |
| M2 | KNOWN_LIMITATIONS reconcile vs 上版 RETROSPECTIVE §二 缺口, 解决项移出 / 新发现项补入 | release 流程 |
| M3 | notebooklm bucket 25 改名: `25_td_meta_ti_ts_oi` → `25_td_meta_ti_ts_oi_di` (DI 已加但名字 mismatch) | release / bundle |
| M4 | chatgpt 05 expected_segments 硬编码 → 改运行时 `len(_collect_domain_assumptions())` | build 脚本 |
| M5 | notebooklm bucket_config 缺新域检测自动化 → 写 `validate_bucket_coverage.py` | build 脚本 |

---

## § 1. v1.3 Scope 决策

### 1.1 In scope (本 release 必须完成)

| Item | 来源 carry | Phase |
|---|---|:-:|
| **PP RELREC linking 2 atoms 补全** (PP/examples.md §6.3.5.9.3) | G5 | A |
| **BECAT EXTRACTION prompt-KB 分叉修复** (KB BE/spec 加 EXTRACTION 注释 + Gemini v8.1 L272 验证一致 OR Gemini v8.2 patch) | D3 | A |
| **Tier B 高 shall/must 节修复** (56 SIBLING_DROPPED 中 shall/must 关键词出现率 ≥3 的节优先, 估 20-30 节) | D5 / G3 | A |
| **437 UNSOURCED_MANUAL 分批抽样定性** (N=40 stratified sample, 含 shall/must 关键词的优先) | D4 / G4 | A |
| **section_coverage.jsonl 重跑** (p4b_section_aggregate.py 在 Phase A KB 改完后跑一次) | G6 | A 收尾 |
| **4 平台 bundle rebuild** (claude / chatgpt / gemini / notebooklm) | KB 改了必须 rebuild | B |
| **4 平台 system_prompt audit pass** (M1, grep 数字引用) | M1 | B |
| **build 脚本 defensive 化** (chatgpt M4 + notebooklm M5 validate_bucket_coverage.py) | M4 / M5 | B |
| **notebooklm bucket 25 改名** (M3) | M3 | B |
| **R4 全 17 题回归 (Pro only)** + M2 candidate-count cap 实证 | D1 / D2 / W3 | C |
| **KNOWN_LIMITATIONS reconcile + §0 PASS+ 描述更新** (W1) | W1 / M2 | D |
| **Cut release/v1.3/ + tag `v1.3-company-release`** | release 流程 | D |
| **Post-audit pass** (用户视角主动 audit ≥1 轮, 反 v1.1 Post-Audit Pass 模式) | v1.1 method-debt | E |
| **RETROSPECTIVE.md** 三段齐备 | 规则 C | F |

### 1.2 Out of scope (v1.3 不做, 留 v1.4+)

| Item | 理由 |
|---|---|
| Tier B 全 166 节修复 (本次只做 shall/must 高密度 20-30 节) | 边际价值递减, 工程量 >1 周 |
| 437 UNSOURCED_MANUAL 全量分类 (本次只 N=40 抽样) | 全量需逐条 PDF 比对 |
| P4a IE 分类不彻底 + TABLE_ROW 行标识符 matcher (G1/G2) | verdict 标签层, 不影响 KB / deploy 答案 |
| Phase 7 RAG + KG 启动 | 与 release pass 并行不经济, 留独立 phase |
| Issue 5 §6.3.5.9.3 PC/PP 143 TABLE_ROW data-value Tier-B MEDIUM repair | 同 Tier B 范畴, 留单独 KB pass |

### 1.3 Tier 3 工作流强制产物

按 `~/.claude/templates/workflow-tier3.md` 标准:

- `.work/07_release_v1_3/PLAN.md` ← 本 plan 立项后迁入 (现 `.work/v1_3_plan.md` 是 P0 草案位)
- `.work/07_release_v1_3/_progress.json` (Tier 2 schema)
- `.work/07_release_v1_3/evidence/checkpoints/` (Phase A-F 每 step 完成事件)
- `.work/07_release_v1_3/evidence/failures/` (Rule B 强制, 失败归档不删)
- `.work/07_release_v1_3/trace.jsonl` (phase_report 事件时间线)
- `.work/07_release_v1_3/subagent_prompts/` (所有派出 subagent 的 prompt 留底)
- `.work/07_release_v1_3/audit_matrix.md` (Rule A 抽检 × 各 Phase 网格)
- `.work/07_release_v1_3/RETROSPECTIVE.md` (规则 C 强制, Phase F 产物)

---

## § 2. Phase 分解

### Phase A — KB layer fixes (估 2-3 工作日)

**A0. 立项** ← 本 plan 用户 ack 后, 主 session 建 `.work/07_release_v1_3/` 全套 Tier 3 目录 + `_progress.json` initial state.

**A1. PP RELREC linking 2 atoms 补全 (G5, 优先级 HIGH)**

- 读取 06 P7 OA-4 evidence (`branches/06_deep_verification/evidence/p7_*`) 定位 PP RELREC 缺口的 PDF 行号
- 在 `knowledge_base/domains/PP/examples.md` §6.3.5.9.3 段补 PP RELREC linking 2 atoms (ABC-123-0001/PPSEQ=1 + PPSEQ=6)
- 写 `evidence/checkpoints/a1_pp_relrec_complete.md` 含 KB diff + PDF 原文锚定
- **Rule A**: N=3 sample 抽检 KB 补全段与 PDF 原文 verbatim 一致 + 无 hallucination

**A2. BECAT EXTRACTION prompt-KB 分叉 (D3, 优先级 HIGH)**

决策选项 (用户 Phase A 启动时拍板, 默认走 A2-α):
- **A2-α (默认, 改 KB)**: `knowledge_base/domains/BE/spec.md` L111 附近加 `EXTRACTION` 作为 sponsor-extensible 第 4 例 (与 v8.1 prompt L272 对齐). 影响范围: BE 单文件 + 1 句变更.
- **A2-β (改 prompt, 不动 KB)**: Gemini v8.2 patch 把 L272 EXTRACTION 加注 sponsor-extensible 标签, 不动 KB. 影响范围: gemini system_prompt + 触发 v8.2 dry-run.
- **A2-γ (双向标注, 推荐到 v1.4)**: KB 加 EXTRACTION + prompt 加 KB-source 引用. 工程量大.

写 `evidence/checkpoints/a2_becat_extraction.md` 记决策 + diff.
**Rule A**: BE/spec.md 改动后, grep 4 平台 uploads 中 `BECAT` 段一致性 (rebuild 前 KB / rebuild 后 bundle).

**A3. Tier B shall/must 高密度节修复 (D5/G3, 20-30 节目标)**

- 从 `branches/06_deep_verification/section_coverage.jsonl` 过滤 `aggregate_verdict ∈ {SIBLING_DROPPED, CONTENT_TRUNCATED}`
- 对每节扫 PDF 原子, 统计 `shall|must|should not|required|MUST|SHALL` 关键词出现次数, 取 ≥3 的节排序
- **派 executor subagent** (sonnet, opus for borderline) 按 PDF 原子逐节补 KB (writer / reviewer 分离, Rule D)
- 每节修完写 `evidence/checkpoints/a3_tierb_section_<N>.md` 含: 节号 / 补全行数 / Rule A 抽样原子 verbatim 比对结果
- **Rule A**: 每节 N=3 抽检; 总修复节数 N≥20 → 跨节 N=10 stratified 终审

**A4. 437 UNSOURCED_MANUAL 分批抽样定性 (D4/G4, N=40)**

- 从 `branches/06_deep_verification/reverse_ledger.jsonl` 过滤 `verdict=UNSOURCED_MANUAL`
- Stratified sample N=40: 含 shall/must 关键词 N=20 (HIGH risk) + 不含 N=20 (control)
- 每条人工或 sub-agent 比对 PDF 上下文 (chapter/page 范围), 定性: **REASONABLE_INFERENCE** / **DERIVED_FROM_XLSX** / **HALLUCINATED** / **NEEDS_HUMAN_REVIEW**
- 若发现 HALLUCINATED → 阻塞, 升 Issue 17 + 立即修
- 写 `evidence/checkpoints/a4_unsourced_manual_n40.md` matrix + 类别分布
- **Rule D**: 派独立 reviewer subagent (`oh-my-claudecode:verifier` 或 `oh-my-claudecode:scientist`) 复核 N=10 sub-sample

**A5. section_coverage.jsonl 重跑 (G6)**

- 跑 `scripts/p4b_section_aggregate.py` (或在 `branches/06_deep_verification/scripts/` 找)
- diff 新旧 jsonl, 确认 A3 修复节的 `aggregate_verdict` 从 SKELETON_ONLY/SIBLING_DROPPED → COMPLETE/PARTIAL
- 旧版备份到 `coverage_ledger.jsonl.pre_v1_3.bak`

**Phase A Gate**:
- [ ] A1 PP RELREC 2 atoms 补 ✅ + Rule A 3/3 PASS
- [ ] A2 BECAT 分叉决策 + 单一方向应用
- [ ] A3 Tier B 节数 ≥20 + 跨节 Rule A N=10 PASS
- [ ] A4 N=40 抽样无 HALLUCINATED + Rule D N=10 PASS
- [ ] A5 section_coverage.jsonl 重跑 + verdict 提升数据
- [ ] **用户 ack Phase A 完成** (PASS 四条第 4 条)

---

### Phase B — 4 平台 bundle rebuild + system_prompt audit (估 1-2 工作日)

**B0. baseline 备份**
- `cp -r ai_platforms/{chatgpt_gpt,gemini_gems,notebooklm,claude_projects}/current/uploads .work/07_release_v1_3/backups/`
- size 应 ~25 MB

**B1. build 脚本 defensive 化 (M4 + M5)**

- M4: `merge_for_chatgpt.py` — 把 expected_segments 改运行时 `len(_collect_domain_assumptions())`, 与 baseline diff > 5% 时 warn 不 fail
- M5: 新建 `ai_platforms/notebooklm/dev/scripts/validate_bucket_coverage.py`: 列 KB 所有 domain/*, 比对 bucket_config.json 覆盖, 漏域 fail + 建议 bucket
- 跑 validate_bucket_coverage.py, 确认 v1.3 KB 无新加域 (Tier B / UNSOURCED_MANUAL 仅修内容, 不加域); 如新加 → 记决策

**B2. 4 平台并行 rebuild** (派 4 个 subagent 并行, 主 session 总控)

- chatgpt: `merge_for_chatgpt.py --stage all` (含 M4 改进)
- gemini: `merge_for_gemini.py --stage c_refactor`
- notebooklm: `merge_sources.py` (含 M3 bucket 25 改名)
- claude_projects: v1 + v2 双 builder (派 background executor subagent, 类 v1.1 模式)

**B3. cross-platform delta oracle 自洽校验 (v1.1 method)**
- chatgpt 05_assumptions delta vs gemini 02_specs_and_assumptions delta — 字节级一致 = 双 pipeline 同源 sanity
- 与 v1.2 baseline diff: 改动应集中在 A1/A2/A3 涉及的 KB 源文件
- 写 `evidence/checkpoints/b3_delta_oracle.md`

**B4. system_prompt audit pass (M1, 关键 v1.1 gap)**
- 对 4 平台 system_prompt + tutorials grep 数字引用: `(域|domain).{0,10}(63|64)`, `(63|64).{0,5}个`, segment_count 数字
- 与 build script 输出 segment_count 交叉对比 — 不一致即 FAIL
- 写 `evidence/checkpoints/b4_system_prompt_audit.md`

**B5. notebooklm bucket 25 改名 (M3)**
- bucket_config.json bucket 25: `25_td_meta_ti_ts_oi` → `25_td_meta_ti_ts_oi_di`
- 重跑 merge_sources.py 验证产物文件名正确

**Phase B Gate**:
- [ ] B0 baseline 备份完成 (size sanity 25 MB)
- [ ] B1 两个 build 脚本 defensive 化 + validate_bucket_coverage.py 跑 PASS
- [ ] B2 4 平台 rebuild ≥3 完整 + ≤1 文件 fallback (Rule B 失败归档)
- [ ] B3 跨平台 delta oracle 字节级一致
- [ ] B4 system_prompt audit 0 不一致
- [ ] B5 bucket 25 改名 + 产物正确

---

### Phase C — R4 全 17 题回归 (Pro only, 估 2-3 工作日含 quota 等待)

**C0. Pre-flight (W4 流程改进)**
- 打开 Gemini, **第一步 verify mode picker 当前选项 = "3.1 Pro"** (W4)
- 截图 mode + quota dashboard 存 `evidence/checkpoints/c0_preflight.md`
- 计算 quota 缓冲: 17 题 / 4 题/window = 5 cycle (含缓冲), 跨 ~20-25 h (含 5h reset × 4)
- **Window 1 plan 3-4 题** (W2 改进, 不再贪 4)

**C1. R4 17 题串行执行**
- 题源: `ai_platforms/SMOKE_V4.md` Q1-Q17 (含 AHP1-3)
- 已 dry-run 验过 PASS+ 的 4 题 (Q3/Q4/Q11/AHP1) **不跳过**, 重测确认 v8.1 LIVE 一致
- 已 sanity 验过 5 题 (Q1/Q2/Q5/Q6/Q14) — Q1/Q2/Q5 Pro 验过, Q6/Q14 Flash-Lite 验过 → R4 用 Pro 重测 Q6/Q14
- 每题 evidence: `.work/07_release_v1_3/r4_full/evidence/q{NN}_r4.md`
- 用 Chrome DevTools MCP 全自动 (per R4 sanity 经验)
- 每题 Strict 判据 per R3 SMOKE_V4 规则 (PASS+/PASS/PARTIAL/FAIL)

**C2. M2 candidate-count cap 实证 (D2)**
- C1 跑题中, 凡 multi-variable 题 (Q2/Q4/Q6/Q14/AHP2) 显式数候选项数, 验证 v8.1 不输出 >5 候选 (M2 fix 实证)
- 若发现 over-limit → finding 写 v1.3.x patch trigger

**C3. 决策树 (per R4 sanity_plan 模式)**
```
17/17 ≥ R3 baseline (无 regression, 允许 PARTIAL ≤2)
  → R4 APPROVE
  → 进 Phase D cut

≥1 FAIL on previously-PASS 题
  → halt + v8.2 patch decision (rollback / patch / accept doc)

PARTIAL > 3 题
  → halt + 触发 deep-dive on regression class
```

**C4. R4 retrospective**
- `.work/07_release_v1_3/r4_full/R4_FULL_RETROSPECTIVE.md` 三段
- 累计 watch finding × 17 题 matrix (类 R4 sanity 的 4 项 watch 但更系统)

**Phase C Gate**:
- [ ] C0 Pre-flight pass (mode = Pro, quota 充足)
- [ ] C1 17/17 跑完 + evidence 齐
- [ ] C2 M2 实证完成
- [ ] C3 决策树命中 APPROVE
- [ ] C4 retrospective 三段齐备

---

### Phase D — Cut release/v1.3/ + KNOWN_LIMITATIONS reconcile (估 0.5-1 工作日)

**D1. KNOWN_LIMITATIONS reconcile (M2 + W1)**
- 读 v1.2 `KNOWN_LIMITATIONS.{en,zh,ja}.md` §0
- 解决项移出 §0 deferred:
  - D1 (R4 17 题 full regression) ← Phase C 完成
  - D2 (M2 candidate-count cap) ← Phase C 完成
  - D3 (BECAT 分叉) ← Phase A2 完成
- 部分进展项更新:
  - D4 (437 UNSOURCED_MANUAL) ← N=40 抽样完成, 全量留 v1.4 → 改写描述
  - D5 (166 Tier B) ← 20-30 节修复, 剩余留 v1.4 → 改写描述
- 新增 §0 entry (W1): "PASS+ §1.2 strict 适用范围扩展 — sanity/R4 实证, 非 AHP 题 KB-grounded + 主动深度也合理 PASS+"

**D2. 平行建 release/v1.3/ 全目录**
- 复制 v1.2 baseline → release/v1.3/
- 4 平台 `self_deploy/` rebuild bundle 替换 (来自 ai_platforms/*/current/uploads/)
- 元文档 (METHODOLOGY/USER_GUIDE/PLATFORM_COMPARISON/DEMO_QUESTIONS/GLOSSARY/README × 3 + CHANGELOG.md) 评估:
  - 若 06 后 KB 改动影响 demo questions → 重写 DEMO_QUESTIONS
  - 否则 byte-identical 继承 v1.2
- 新写 CHANGELOG.{en,zh,ja,md} v1.3 entry (说明: KB pass + Phase A 修 + R4 全 17 题 PASS + BECAT 分叉解 + Tier B 部分修)
- BUILD_MANIFEST.json v1.3 metadata

**D3. Rule D #19 独立 reviewer**
- 候选 subagent_type (与主 session 不同): `oh-my-claudecode:verifier` (opus) / `oh-my-claudecode:critic` (opus) / `pr-review-toolkit:code-reviewer` / `oh-my-claudecode:scientist`
- 评估范围: rebuilt uploads 真实反映 Phase A KB 改动 / system_prompt audit 0 不一致 / KNOWN_LIMITATIONS reconcile 完整 / cut diff 与 v1.2 一致
- 输出 `evidence/checkpoints/d3_rule_d_v1_3_audit.md`

**D4. tag cut**
- 用户 ack 后: `git tag -a v1.3-company-release -m "v1.3 — KB pass: PP RELREC + BECAT + Tier B + R4 17/17"`
- Push tag

**Phase D Gate**:
- [ ] D1 KNOWN_LIMITATIONS 三语 reconcile 完成
- [ ] D2 release/v1.3/ 结构完整 + CHANGELOG 三语 + BUILD_MANIFEST.json
- [ ] D3 Rule D #19 APPROVE
- [ ] D4 tag pushed

---

### Phase E — Post-audit pass (反 v1.1 模式, 估 0.5 工作日)

**E1. 主动模拟用户视角 audit (v1.1 method-debt 修)**
- 自查清单 ≥6 项 (模拟用户拷问 "四个平台是不是最后还差测试 / system_prompt 数字引用对不对 / KNOWN_LIMITATIONS 真的反映 v1.3 / Rule A 抽检多少够"):
  1. Rule A 累计 N≥20 + 跨 KB 与 4 平台 124 grep probe
  2. 4 平台 system_prompt 数字引用 0 不一致 (B4 复核)
  3. KNOWN_LIMITATIONS §0 与 v1.2 § 0 + R4 retro 缺口逐条 reconcile (M2)
  4. release/v1.3/ root 三语 meta 文档 0 漏 (v1.1 Post-Audit Pass §四 b 教训)
  5. CHANGELOG 三语 v1.3 entry 完整 + 风格统一
  6. tag 链路完整 (annotated + push verify)

**E2. 若发现 gap → 主 session 立刻修, 不留 v1.4**
- 类 v1.1 Post-Audit Pass 模式

**Phase E Gate**:
- [ ] E1 self-audit ≥6 项 0 gap
- [ ] E2 gap (如有) 全部 close

---

### Phase F — RETROSPECTIVE + Sync state + Commit (规则 C 强制, 估 0.5 工作日)

**F1. `.work/07_release_v1_3/RETROSPECTIVE.md` 三段**
- § 一 保留下来的做法 (≥5 项)
- § 二 必须补上的缺口 (列 v1.4 candidates)
- § 三 关键决策复盘 (≥4 决策)
- § 附 v1.3 终态数字 (KB diff / 4 平台 size / R4 17/17 verdict matrix / Rule D #19 PASS)

**F2. Sync state (v1.1 path 复用)**
- `ai_platforms/SYNC_BOARD.md`: 加 v1.3 cut Phase 段
- 各 `dev/evidence/_progress.json`: 加 v1.3 entry
- `.work/meta/worklog/phase_07_release.md`: append v1.3 cut record
- `docs/PROGRESS.md`: milestone "Release v1.3 cut + R4 17/17 PASS"
- `CLAUDE.md` Key Paths: 加 `release/v1.3/` 入口 (复用 `Phase 6.5 Release v1.1` 行模板, 改路径)

**F3. 单 commit + push**
- 信息: `"07 Release v1.3 — KB pass: PP RELREC G5 + BECAT D3 + Tier B partial + R4 17/17 ≥ baseline + tag v1.3-company-release"`

**Phase F Gate (终审)**:
- [ ] F1 RETROSPECTIVE 三段齐备
- [ ] F2 4 处 sync state 更新
- [ ] F3 commit pushed, tag visible on remote
- [ ] **用户 ack 收尾** (PASS 四条第 4 条最终)

---

## § 3. 规则 A/B/C/D + PASS 四条 落地

### 规则 A (语义抽检强制)

| Phase | 抽检范围 | N | 备注 |
|:-:|---|:-:|---|
| A1 | PP RELREC 补全段 vs PDF 原文 | 3 | 单文件小改 |
| A2 | BECAT KB 改动 (如走 α 方案) vs 4 平台 uploads 同步 | 4 (一平台一抽) | rebuild 前 |
| A3 | Tier B 节修复 (跨节 stratified) | 10 | ≥20 节修, 10/20 抽样 |
| A4 | UNSOURCED_MANUAL 抽样 | 40 (stratified shall/must = 20 + control = 20) | + Rule D N=10 sub |
| B3 | rebuild 后 4 平台 uploads vs KB 改动 | 5 (跨 4 平台 + 1 跨平台 oracle) | cross-platform delta 验证 |
| B4 | 4 平台 system_prompt 数字引用 | 4 平台 × 3 数字 = 12 grep | 0 不一致 |
| C1 | R4 17 题 Strict 判据 | 17 (全题) | per R3 method |
| E1 | Post-audit self-check | 6 项 | 反 v1.1 Post-Audit Pass |
| **累计** | | **≥97** | 远超 v1.1 N=20+ 124 grep 标准 |

### 规则 B (失败归档不删)

任何 step 失败:
- `failures/<phase>_<step>_attempt_N.md` 含 输入 / 产物 / 技术判定 / 业务判定 / 下一 attempt 输入
- 不 rm, 不 archive 出 `.work/`

### 规则 C (Retro 强制)

- Phase C 收尾: `r4_full/R4_FULL_RETROSPECTIVE.md` 三段
- 总收尾: Phase F `RETROSPECTIVE.md` 三段

### 规则 D (审阅隔离 / writer ≠ reviewer)

**candidate reviewer subagent_type list** (Phase D3 用):
- `oh-my-claudecode:verifier` (opus) — 优先级 1, v1.1 用过
- `oh-my-claudecode:critic` (opus) — 优先级 2, v1.2 cut audit 用过 (#18)
- `pr-review-toolkit:code-reviewer` — 优先级 3, 06 旁枝多次
- `oh-my-claudecode:scientist` — 优先级 4, R3 SMOKE_V4 reviewer #15

主 session 主写 Phase A/B/D/E/F, 派 background subagent 写 A3 (Tier B 节修复) + claude_projects rebuild (B2).

### PASS 四条

每 Phase Gate 必过:
1. evidence 存在 (`evidence/checkpoints/<step>.md`)
2. writer 产物合规 (符合 plan 规定结构)
3. 独立 reviewer subagent PASS (Phase D 总审)
4. 用户口头 ack

---

## § 4. Risk register + 失败模式预案

| Risk | Likelihood | Mitigation |
|---|:-:|---|
| Phase A3 Tier B 节数 <20 (PDF 原文晦涩, 补不动) | M | 降级目标 ≥10 节, 剩余 20+ 节明确留 v1.4, KNOWN_LIMITATIONS 注明 |
| Phase A4 N=40 抽样发现 HALLUCINATED | L | 升 Issue 17, 立即修该原子 + 扩展 N=100 安全样本 |
| Phase B2 build 脚本 defensive 化破坏向后兼容 | L | M4/M5 改动加 unit test + 与 v1.2 baseline diff 应为 0 |
| Phase B4 system_prompt 4 平台数字引用不一致 → 大改 | L-M | 提前 grep 一遍 (Phase B 开头), 不一致 ≤2 即手改不改脚本 |
| Phase C Gemini Pro quota 用光 4 cycle 仍跑不完 17 题 | M | 接受 Window 3+ 跨日, 退路: 余下题用 Flash-Lite + retro 标 model caveat (R4 sanity 经验) |
| Phase C ≥1 FAIL on previously-PASS 题 | L | v8.2 patch dry-run + re-promote, plan 增量 ~1 周 |
| Phase D Rule D #19 FAIL (KNOWN_LIMITATIONS 不一致 / system_prompt 漏) | L | reviewer 列 finding, 主 session 立即修, re-submit |
| Phase E post-audit 发现新 gap | M | 反 v1.1 模式: 立刻修, 不留 v1.4 |
| BECAT A2 决策方向错 (走 α 后发现应走 β) | L | failures/ 归档第一次决策, 第二次方向重跑 (Rule B) |

---

## § 5. 关键决策点 (执行中拍板)

1. **A2 BECAT 方向** (Phase A 启动时): α (改 KB) / β (改 prompt) / γ (双向 → 推迟 v1.4)
   - 默认 α (KB 改动小 + 与 prompt 对齐)
2. **A3 Tier B 节优先级** (Phase A 启动时): shall/must 关键词阈值 (≥3 / ≥5 / ≥10)
   - 默认 ≥3, 估 20-30 节
3. **C1 跑 Q6/Q14 Pro 重测 vs 接受 R4 sanity Flash-Lite caveat** (Phase C 启动时)
   - 默认 Pro 重测 (W3 流程改进, R4 全题用 Pro)
4. **D2 元文档继承策略** (Phase D 启动时): byte-identical 继承 vs 选择性重写
   - 默认: METHODOLOGY/USER_GUIDE/PLATFORM_COMPARISON/GLOSSARY 三语继承; DEMO_QUESTIONS/README/CHANGELOG 重写 (KB 改了)
5. **Rule D #19 subagent_type 选择** (Phase D3 前): 从 candidate list 选
   - 默认 `oh-my-claudecode:critic` (与 v1.2 #18 同 type, 跨 release 对比可比)

---

## § 6. Exit criteria (Phase F 终止条件)

- [ ] release/v1.3/ 目录完整, byte-equivalence vs v1.2 baseline 不重复部分 + v1.3 真改部分 = sum
- [ ] tag `v1.3-company-release` annotated + push verified
- [ ] CHANGELOG.{en,zh,ja,md} 4 文件 v1.3 entry 完整
- [ ] KNOWN_LIMITATIONS.{en,zh,ja} 三语 §0 reconcile + W1 entry 加
- [ ] BUILD_MANIFEST.json v1.3 metadata
- [ ] 4 平台 uploads ai_platforms/*/current/uploads/ ≡ release/v1.3/self_deploy/*/uploads/ byte-identical
- [ ] R4 17/17 evidence + retro 完整
- [ ] Rule A 累计 ≥97 抽检 全 PASS
- [ ] Rule D #19 APPROVE
- [ ] RETROSPECTIVE.md 三段齐备
- [ ] Post-audit pass 0 gap 闭环
- [ ] docs/PROGRESS.md / SYNC_BOARD.md / phase_07_release.md / CLAUDE.md Key Paths 4 处 sync 更新
- [ ] commit pushed to main + tag visible on remote
- [ ] **用户 ack 收尾** (PASS 四条第 4 条最终)

---

## § 7. 上线指令 (本 plan ack 后)

> "**v1.3 Phase A 启动**: 主 session 建 `.work/07_release_v1_3/` Tier 3 全套目录 + `_progress.json` initial state, 然后开 A1 PP RELREC 补全."

主 session 收到后:
1. mkdir `.work/07_release_v1_3/{evidence/{checkpoints,failures},subagent_prompts,r4_full/evidence,backups}`
2. 把本 `.work/v1_3_plan.md` mv → `.work/07_release_v1_3/PLAN.md` (本 plan 的正式位置)
3. 建 `_progress.json` Tier 2 schema initial: `{"version": "v1.3", "tier": 3, "phase": "A", "step": "A1", "status": "in_progress", "rules": {"A": [], "B": [], "C": null, "D": []}, "checkpoints": [], "failures": []}`
4. 建 `trace.jsonl` empty + 首条 `phase_report` event `phase=A step=A0 status=initialized`
5. 建 `audit_matrix.md` skeleton (Phase × Rule A 抽检格)
6. 开始 A1

---

## § 8. 决策日志 (本 plan 起草过程)

- **2026-05-20 morning** — 本 plan 起草, 基于 4 来源 carry 清单 (v1.2 KNOWN_LIMITATIONS §0 / R4 sanity retro / 06 旁枝 retro / v1.1 Post-Audit Pass)
- **Tier 3 决定**: 跨 KB + prompt + 4 平台 + release tag + R4 全题 5 层, 跨日多 quota cycle, 高 stakes → Tier 3
- **Scope narrow 决定**: Tier B 不全做 (>1 周), 437 UNSOURCED 不全分类 (>1 周), P4a verdict 标签层不修 (不影响 KB / deploy)
- **本 plan 位置**: 草案在 `.work/v1_3_plan.md`, 用户 ack 后由 Phase A0 主 session 迁移到 `.work/07_release_v1_3/PLAN.md`
