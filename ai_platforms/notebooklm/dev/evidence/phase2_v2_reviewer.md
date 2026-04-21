# Phase 2 v2 Architecture Reviewer Report (第 9 种 subagent_type: oh-my-claudecode:architect)

> **本文件由主 session 代写落盘** (reviewer 是 read-only subagent_type). 产出时间 2026-04-21, 审查对象 `docs/PLAN.md` v2 (548 行) + 配套文档 (research.md v2 / platform_profile.md v2 / ARCHITECTURE_PIVOT_RECORD.md / _progress.json v2 架构段). Rule D 链: v1 已烧 8 种 subagent_type, 本轮为**第 9 种** (架构级独立审).

## Verdict

**CONDITIONAL_PASS, 置信度 84%**

v2 架构方向正确且可执行. 无 FAIL 级结构性问题, 无需再次 pivot. 存在 **3 条 MEDIUM 级必须在 Phase 3 前锁死的边界 + 2 条 HIGH 级但可由主 session 在进入 Phase A 前一次性补齐的证据链缺口**. HIGH 级修完后可进 Phase 3.

## Summary

v2 把 v1 三假设 (两独立模式 / 50-cap 覆盖全档 / 293 一对一最优) 干干净净推翻并重写, 方向在 SDTM 场景下站得住: 单 notebook × ≤50 source + 3 档分享切换确实能覆盖 Rule E ack 的 ABC 全旅程, 且 Q1 红线 (0 Req 丢失) 在 slot 从 30 放到 ≤50 后在**可证且更易守**一侧. 但 v2 自身残留 2 条隐藏的叙事合成风险 (证据 3 "viewer tier cap" 解读 + "单 notebook 只能一个 Chat mode" 口径), 另有 ≤50 slot 示意清单在 PLAN §3.2 里和 Req extractor 产物之间没有硬绑定. P3.2 单批拖拽 50 个 md 到 Web UI 是本次**唯一未做证据闭合的 UI 动作**.

---

## F1-F9 Findings 详细

### F1: v2 核心架构是否站得住

**总体**: 站得住. "1 notebook + 3 档 Access Level" 在 research.md Q7 v2 + 三 WebFetch 证据下是**事实描述**, 不是合成推论.

- Q7 v2 (research.md L173-247) 明确三档是同一 notebook 的 toggle, 引 answer/16322204 原文 "Set Notebook Access back to Restricted". WebFetch 实读, 非叙事引伸.
- platform_profile §E (L72-86) 档位 / 50-cap 适用 / 匿名访问 / Workspace 限制四件事独立列, 伪约束风险低.
- Rule E ack 三场景 ABC 在单 notebook 内的映射完整覆盖:
  - Scope A (个人学习) → Restricted 默认态 ✓
  - Scope B (≤50 同事) → Restricted + invite ✓
  - Scope B/C (广覆盖) → Anyone with link ✓
  - Scope C (画廊发现) → Public ✓

未发现 "某子场景单 notebook 无解" 情形. 唯一边界 case (collaborator 圈职责隔离) 不在 Rule E 范围内, Pivot Record 已正确标注保留情境.

**LOW 级 L1**: PLAN §3.1 L221 "三场景**同一 notebook**" + §3.3 把 Restricted 分成 "Scope A 私有" / "Scope B 小圈邀请" 两个独立条目, 有冗余嫌疑. 建议 §3.3 表格 "Restricted" 合并 "(无邀请 = Scope A 私有 / + invite = Scope B 小圈)".

### F2: Q1 红线 (0 Req 丢失) 是否真的更易守

**总体**: 客观更易守 (slot 从 30 → ≤50, 平均字数 ~133K → ~24K words, outlier 容错倍增), 但审计链不完整, 2 条 HIGH 级缺口.

**HIGH 级 H1**: PLAN §3.2 L248-271 的 50 slot bucket 示意表是手工写的, 与 `cluster_req_variables.py` 产出之间**没有 source-of-truth 契约**. 典型风险: L259 "findings_other" bucket 18-22 塞 20 个 domain 到 4 slot (平均 5 domain/slot), 能否"一同叙述"并 citation 召回未做验证. 脚本产物若与示意差异 >20%, PLAN §3.2 自身过时.

- **建议修法**: §3.2 表前加 "本表仅示意, Phase A3 `cluster_req_variables.py` 产物为准. 差异 >20% 触发 §3.2 同步刷新".

**HIGH 级 H2**: PLAN §3.2 L278 的 "差集等式" `全集 ∪ {slot Req} 必 = 全集 ∩ {slot Req} = 全集` **数学上不严谨**: 并集等式只有当 {slot Req} ⊆ 全集 时成立, 若脚本输出 {slot Req} 是超集, 会制造假 alarm.

- **建议修法**: 改为 "覆盖断言: ∀ req ∈ req_vars_full_set, ∃ source ∈ uploads, 使 req.variable ∈ source.covered_req_set. FAIL condition: ∃ req ∈ full_set, ∀ source, req.variable ∉ source.covered_req_set."

**MEDIUM 级 M1**: 规则 A N=10 抽检 (L280) 写 "按名查 bucket 必 100% 命中". 但 **结构检查 ≠ 语义检查** (违反用户规则 A). NotebookLM 是 grounded RAG, chunk 级检索, "bucket 里含变量名" ≠ "业务问答能召回". 

- **建议修法**: A4 保留结构 ∅ gap 断言作 Phase A 出口; 新增 Phase 3 P3.4.5 "Req 变量业务问答抽检 N=10" 作 Q1 红线**语义**自证.

### F3: 三 WebFetch 证据链

**总体**: 证据 1 + 2 闭合度高, 证据 3 解读 A 不稳但保守性有效.

- **证据 1** (answer/16206563, 50-cap 仅 Restricted): HIGH 置信, 官方原文无歧义
- **证据 2** (answer/16322204, 3 档切换): HIGH 置信, 直接证明 toggle
- **证据 3** (answer/16213268, viewer tier cap): **MEDIUM 置信, 有歧义**. 原文 "Sharing a notebook does not change the source limit for any collaborator" 两种解读:
  - 解读 A (v2 采用): Free viewer 最多看 50 sources
  - 解读 B: collaborator 查看共享 notebook 时不占自己 slot, 但可看全部
  - 解读 A 是 WebFetch AI summary 的二次解读, 非官方原文
  - **即使证据 3 错, ≤50 结论仍稳** (保守性 dominates 真相), 可接受

**MEDIUM 级 M5**: Pivot Record 六条 ≤50 理由里 (1) "Free tier viewer 兼容" 依赖证据 3 解读, 证据强度是 MEDIUM 不是 HIGH. 主要用户群 (SDTM 专家大多 Pro/Plus/Workspace) 使 (1) 成立概率 MEDIUM.

- **建议修法**: 理由 (1) 从首要降级为次要 (写明 "概率 MEDIUM, Phase 5 用户群数据确认"), 主 drive 改为 "indexing silent fail 风险降低 + citation 信噪比" (理由 2/3 证据 HIGH). 结论 ≤50 不变, 只改归因权重.

**SUGGESTION S1**: P3.9 3 档切换演练时顺手用 Free tier 小号测 "viewer 能看几个 source", 30 分钟, 闭合证据 3 解读. 非阻塞.

### F4: Phase A 简化 (A5 降级)

**总体**: 原则对, P3.2 "≤50 次 Web UI 手工拖拽" **未证据闭合**, MEDIUM 级风险.

**MEDIUM 级 M2**: "手工拖拽可行" 无 Phase 1 实测支撑. research.md Q5 只说 "indexing silent fail 实测", 未覆盖 "单批拖拽 N 个是否触发 UI 限流/队列溢出/silent drop". 若 Web UI 单批上限 <50 (例如 20), P3.2 要分批, 工时翻倍.

- **建议修法**: Phase A 期间主 session 做**一次 5-source 小样上传实测** (建废弃 notebook, 拖 5 个任选 md, 记录拖入能力 / indexing 时间 / silent fail). 证据 → `dev/evidence/phase_a_webui_small_sample.md`. 30 分钟内. 小样失败立刻调整 P3.2 为分批.

**Phase A 删减评估**: A2 删除 (Chat mode 决策) 合理 (已锁定 Custom). A5 降级需 M2 补充.

### F5: P12 降级

**总体**: 降级正确, 无实质风险. 单 notebook 场景下 "跨 notebook 引用" 物理不可能. Phase 7 RAG/KG handoff 时 notebook 只交付 artifact (current/uploads/*.md), Phase 7 自处理 source identity. 无建议修改.

### F6: §6 Task 分解

**MEDIUM 级 M3**: P3.4 indexing smoke 采样 N=3 (≤50 source 采样率 6%), 漏检风险高. 
- **建议修法**: smoke 题数 3 → **10** (首/末/中间 8 个随机), 每题检查 citation 精确指向. 工时 1h → 1.5h.

**LOW 级 L3**: P3.9 3 档切换只测 4 态单向, 未测快速多次切换. 
- **建议修法**: 加子步骤 (e) "连续 Restricted ↔ Public 2 次, 验证老链接 revoke". +10 分钟.

**SUGGESTION S2**: P3.4 smoke 至少 1 题选 non-core domain (DD/HO/ML 等) 的独有 Req 变量, 测 "findings_other" bucket 18-22 的 RAG 信号强度.

### F7: RETROSPECTIVE pivot 归因

**MEDIUM 级 M4**: §11 (PLAN L515-524) 归因准确但**深度不够**. 深层盲区 3 层:
1. Rule D 只防 writer = reviewer 同 session 污染, **不防 "writer 叙事范式 → reviewer 接受范式"**. v1 Q7 "Mode A/B 两独立" 被 8 种 subagent_type 全部继承, 无回 WebFetch 原文核对. **范式锁定**问题, 与 subagent_type 多样性无关.
2. Reviewer 审查焦点由前 Phase 提供的 spec 决定, **不会倒回去质疑 research**. 缺跨 Phase reviewer 角色.
3. 用户反问是**外部触发**, 不是 Rule D 链的胜利.

补丁候选 #10 只覆盖层 1.

- **建议修法**: 补丁拆为 10a + 10b:
  - 10a (现 _template/03_research.md Writer 立场警示, 防层 1)
  - 10b **新增** _template/04_plan.md planner 接 research 时加 "**核心约束原文回溯**" 段 (强制回 Phase 1 A 级 URL 原文, 防层 2) + "**Phase 2 PASS 前用户反问 gate**" (Phase 2 PASS 前强制一次用户反问机会, 防层 3).

### F8: v2 PLAN 自身是否有新伪约束 (最重要)

发现 **3 条潜在伪约束**.

**HIGH 级 H3**: PLAN §3.4 + Pivot Record D10 说 "**单 notebook 只能一个 Chat mode**". 证据**缺失**:
- research.md Q6 未明说 "每 notebook 只能一个 chat mode"
- blog.google 2025-10-29 原文只说 "customize chat to adopt a specific goal, voice or role"
- XDA 报道说 UI 是 "**Configure Chat**" 每次可切, 可能 notebook 级配 Custom + 单 chat session 临时切换 Learning Guide

**可能真相**: Custom mode 的 10K char 写 notebook 级 config, 但单 chat session 可在三档间切换. 若真, "只能一个" 是伪约束, 实际可做 "notebook 级 Custom 默认 + 用户临时切 Learning Guide 自学".

- **建议修法**: P3.3 加子步骤 "验证 chat session 是否可切换三档, 事实回写 platform_profile §D + research.md Q6". 10 分钟. 验证前 PLAN 口径改 "notebook 级默认 Custom, 单 session 内可能可切换, Phase 3 验证".

**MEDIUM 级 M5 (承接 F3)**: "≤50 slot 是 Free tier viewer 兼容水位" 首要归因不稳.

**LOW 级 L2**: PLAN §3 多处 "Scope ABC 只能通过分享档位切换实现" 是"**当前 Rule E ack 条件下**", 不是平台硬约束.
- **建议修法**: 加 "在本次 Rule E ack 下" 前缀.

**反向关键字扫描**:
- "**必须**" 6 次, 都合理硬约束 (Q1 红线 / ∅ gap 必证 / Rule A N=10 必跑 / 用户 ack 必过), **无伪约束**
- "**只能**" 1 次 (§3.4 Chat mode, 即 H3)
- "**本质上**" 0 次 (v1 Q7 "本质两选一" 已清干净)
- "**无解/无法**" 0 次

**v2 伪约束密度明显低于 v1**, 但仍有 H3/M5/L2 三处.

### F9: v1 残留污染 (干干净净检查)

**总体**: 干净. 有 2 处合法历史引用 (非污染) + 2 处 LOW 级不一致.

扫描关键字 ("3 notebook / multi-notebook / Mode A / Mode B / Notebook 1-3 / uploads_main/invite/public / 45 题次 / 353 次"): 所有匹配均在 **pivot audit 段 / v1 对比陈述**, 语境清晰, 合法.

**LOW 级 L4**: research.md §11 L361-371 有**重复的 "来源" 段** (pivot 重写时没清干净的历史残留).
- **建议修法**: 删重复段.

**LOW 级 L5**: research.md Writer #2 日志 L472 前置声明已加 pivot 注记, 但正文 L483 "3b Mode A/B" 表格无 inline 失效标注.
- **建议修法**: 前置声明再加 "**下表第 3b 行 Mode A/B 框架已在 Q7 v2 废止, 以 Q7 v2 三档为准**".

### F10: SUGGESTION

- **S1 (F3)**: P3.9 3 档切换演练用 Free tier 小号测 viewer 看几个 source
- **S2 (F6)**: P3.4 smoke 至少 1 题选 non-core domain (DD/HO/ML 等) 独有 Req 变量
- **S3 (F8)**: PLAN §11 补 "v2 自身的叙事合成风险自查清单" (扫 必须/只能/本质上/无解/无法 五关键字 + 每处回溯证据) 作方法论交付
- **S4**: `cluster_req_variables.py` config 改 ≤30 → ≤50 时重点检查**聚类距离阈值**是否随之放松; slot 利用率应 ≥80% (>40 slot 有内容), 否则 50 cap 是纸面宽松
- **S5**: Phase 5 `cross_platform_compare.md` 加 "citation 精度 (Req 变量级)" 列, NotebookLM inline citation 是本平台独特优势

---

## HIGH 级 findings (必修)

| # | 位置 | 问题 | 建议修法 | 主 session 处置 |
|---|------|------|---------|----------------|
| **H1** | PLAN §3.2 L248-271 | 50 slot bucket 示意表和脚本产物无 source-of-truth 契约 | 表前加契约声明 | ✅ **直接修** (文档级) |
| **H2** | PLAN §3.2 L278 | Req 全覆盖断言集合等式数学不严谨 | 改蕴含形式 | ✅ **直接修** (文档级) |
| **H3** | PLAN §3.4 + Pivot Record D10 | "Chat mode 单 notebook 只能一个" 无 A 级证据 | P3.3 加验证, 口径改假设 | ⏸️ **等用户 ack** (Q-REV-1) |

## MEDIUM 级 findings (建议修)

| # | 位置 | 问题 | 建议修法 | 主 session 处置 |
|---|------|------|---------|----------------|
| **M1** | PLAN A4 + §6 P3.4 | A4 ∅ gap 是结构检查非语义检查 (违反规则 A) | 新增 P3.4.5 业务问答 N=10 | ⏸️ **等用户 ack** (Q-REV-3) |
| **M2** | PLAN §6 P3.2 + Phase A | Web UI 单批 50 拖拽无小样闭合 | Phase A 加 A5' 5-source 小样实测 | ⏸️ **等用户 ack** (Q-REV-2) |
| **M3** | PLAN §6 P3.4 | smoke 采样率 6% 漏检风险 | smoke 题 3 → 10 | ✅ **直接修** |
| **M4** | PLAN §11 + 补丁 #10 | pivot 归因只覆盖层 1 | 补丁 10a + 10b | ✅ **直接修** (PLAN §11 + _progress.json) |
| **M5** | Pivot Record + PLAN L69 | 证据 3 解读 A 不稳, "Free tier 兼容" 首要归因不稳 | 理由 (1) 降级, 主 drive 改 2/3 | ✅ **直接修** (Pivot Record 不可改; 改 PLAN 引用) |

## LOW 级 findings (可选)

| # | 位置 | 问题 | 建议修法 | 主 session 处置 |
|---|------|------|---------|----------------|
| **L1** | PLAN §3.3 | Restricted 档分两行易误读 | 合并 "(无邀请 = Scope A / +invite = Scope B)" | ✅ **直接修** |
| **L2** | PLAN 多处 | "Scope ABC 只能分享档位切换" 非硬约束 | 加 "本次 Rule E ack 下" 前缀 | ✅ **直接修** |
| **L3** | PLAN P3.9 | 3 档切换未测快速多次 toggle | 加子步骤 (e) | ✅ **直接修** |
| **L4** | research.md §11 L361-371 | "来源" 段重复 | 删重复 | ✅ **直接修** |
| **L5** | research.md L472 前置声明 | 日志正文无 inline 失效标注 | 前置声明加废止提醒 | ✅ **直接修** |

---

## 可进 Phase 3 的前置条件 (Gate)

Phase 3 入口需主 session 完成以下 5 项, 缺一不可:

1. **H1 修**: PLAN §3.2 加 source-of-truth 契约
2. **H2 修**: PLAN §3.2 断言改蕴含形式, 脚本实装严格对齐
3. **H3 修**: PLAN §3.4 + Pivot Record D10 口径调假设待 P3.3 验证; P3.3 加验证子步骤
4. **M1 修**: 新增 P3.4.5 业务问答 N=10 (Q1 红线语义自证)
5. **M2 修**: Phase A 加 A5' 5-source Web UI 小样实测

**M3-M5 + LOW + SUGGESTION** 可与 Phase 3 并行, 不作 gate.

---

## 主 session 需要 ack 的问题 (Q-REV)

### Q-REV-1 (关于 H3 — Chat mode 切换假设)

是否接受 "Chat mode 单 notebook 只能一个" 降级为假设待验证, P3.3 用户实测后落回 RETROSPECTIVE?

**主 session auto mode 默认**: ✅ **接受假设待验证** (主 session 无权登 Google 账号做 UI 实测, 由用户 P3.3 同步验证最经济; 在验证前 PLAN 口径用 "notebook 级默认 Custom, 单 session 内可能可切换, Phase 3 验证")

### Q-REV-2 (关于 M2 — Phase A 5-source 小样实测)

是否接受 Phase A 加 A5' "5-source Web UI 小样闭合实测"? 放哪?

**主 session auto mode 默认**: ✅ **接受, 放 A5' (与 A1 并行)** (不依赖 A2/A3 产物, 30 分钟完成, 证据 `phase_a_webui_small_sample.md`)

### Q-REV-3 (关于 M1 — Q1 双锚)

Q1 红线是否双锚 "A4 结构自证 + P3.4.5 语义自证"?

**主 session auto mode 默认**: ✅ **接受双锚** (符合用户规则 A "结构检查 ≠ 语义检查" + Q2 "质量第一不赶工", 增加 1-2 小时 Phase 3 工时可接受)

**用户如需纠正**, 在 C5.2 commit 前 ack; auto mode 默认接受.

---

## Rule D 9-lane 链完整性自检

| # | Subagent type | Phase | 产物 |
|---|--------------|-------|------|
| 1 | general-purpose | Phase 1 Writer #1 | research.md 初版 |
| 2 | oh-my-claudecode:verifier | Phase 1 Reviewer #1 | phase1_reviewer.md (已归档) |
| 3 | oh-my-claudecode:executor | Phase 1 Writer #2 | research.md 修正版 |
| 4 | oh-my-claudecode:critic | Phase 1 Reviewer #2 | phase1_reviewer2.md (已归档) |
| 5 | oh-my-claudecode:planner | Phase 2 v1 Writer #3 | PLAN_v1_3notebook.md (已归档) |
| 6 | oh-my-claudecode:analyst | Phase 2 v1 Reviewer #3 | phase2_reviewer.md (已归档) |
| 7 | feature-dev:code-architect | Phase 2 v1 Writer #4 | PLAN v1.1 14 edits (已归档) |
| 8 | pr-review-toolkit:code-reviewer | Phase 2 v1 Reviewer #4 | phase2_reviewer2.md (已归档) |
| — | 主 session (非 subagent) | Phase 2 v2 Writer (pivot) | PLAN.md v2 |
| **9** | **oh-my-claudecode:architect** | **Phase 2 v2 Reviewer (本次)** | **本文件 phase2_v2_reviewer.md** |

**Rule D 合规**: 每种 subagent_type 独立, 无自审. 主 session 作为 Phase 2 v2 Writer 非 subagent 但作为 Rule D 链中的 Writer 角色存在, 独立审由第 9 种 subagent_type 承担, 合规.

---

*审查完毕. 主 session 将按 auto mode 默认应用可修条目 (H1/H2 + M3/M4/M5 + L1-L5), 并按 Q-REV 默认假设处置 H3/M1/M2. C5.2 commit 含: reviewer evidence + PLAN 修订 + _progress.json 更新. 用户如需纠正 Q-REV 默认, C5.2 commit 前 ack.*
