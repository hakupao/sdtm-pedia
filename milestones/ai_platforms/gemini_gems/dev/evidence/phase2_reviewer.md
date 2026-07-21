# Gemini Gems Phase 2 PLAN — Reviewer Verdict

**Verdict**: CONDITIONAL_PASS
**Reviewed by**: oh-my-claudecode:verifier (独立 lane, 规则 D)
**Date**: 2026-04-20
**Subject**: ai_platforms/gemini_gems/docs/PLAN.md (578 行)

---

## P1-P12 覆盖矩阵

| # | 规则 | PLAN 对应位置 | 具象化程度 | 状态 |
|---|------|-------------|----------|------|
| P1 | 量化 PASS 标准 | §1.2 P1 + §2.4 脚本职责 | 四文件各有 token target: 01~120K / 02~168K / 03~225K / 04~200K; 总 target ≤800K | PASS |
| P2 | 写/审分离执行态 | §1.2 P2 | Writer=executor, Reviewer=code-reviewer/verifier; Phase B 合并脚本 + Phase D A/B 双 lane 显式 | PASS |
| P3 | 估算值前缀 ~ | §1.2 P3 | manifest 中 ~713K = 估算说明; §2.1 文件清单中全部估算值加 ~ 前缀 | PASS |
| P4 | Checkpoint 级别: hard/soft/none 不擅自连推 | §1.2 P4 + §4 每 Task | 每 Task 均有 checkpoint 级别标注 (详见 §4 Task 分解) | PASS |
| P5 | 源文件只读 | §1.2 P5 + §2.3 | knowledge_base/** 强制禁写; 合并脚本只读源 | PASS |
| P6 | Subagent 上下文隔离 | §1.2 P6 + §2.4 | merge_for_gemini.py 派独立 executor, 主控不读脚本源 | PASS |
| P7 | 进度持久化 | §1.2 P7 | 每 Task 完成立即更新 _progress.json | PASS |
| P8 | (同规则 B) | §1.2 P8 | 引用 B | PASS |
| P9 | (同规则 A) | §1.2 P9 | 引用 A | PASS |
| P10 | A/B 衰减强制响应 | §1.2 P10 + §4 Phase D P10 触发段 | ≥2 题停 / ≥1 题 regression evidence; 末尾召回 2 题独立 gate (P12) | PASS |
| P11 | 单批到位 (平台独有) | §1.3 P11 | 1 批全上; 依据 arxiv 2403.05530 (100% recall @530K, >99.7% @1M); 硬约束: >900K 触发 §8 R2; **不做 Claude v2 式 5 批拐点建模** | PASS |
| P12 | 末尾召回强验 (Phase 1 F-1 carry-over 兑现) | §1.3 P12 | T-tail-1 + T-tail-2 两题 hard gate; 2 题均 PASS 才放行; FAIL 响应分支明确 (1 题 / 2 题均 FAIL 各有处置); "来源" 一栏注明 arxiv + Google 官方 + Chroma 2025 | PASS |

**P1-P12 覆盖: 12/12**

---

## Rule E 乘入审核 (Q3/Q4/Q5)

### 公式存在性

§3.1 明确公式:
```
score(item) = coverage_weight × priority_weight × position_fit
```

### Q3=C (精确查询 + 全域对比兼顾) 乘入

| 乘入位置 | 具体体现 | 追溯 |
|---------|---------|------|
| coverage_weight 对导航层加成 1.2 | §3.1: "chapters/model 作为引导层 weight=1.2" | 支撑全域对比 (Q3=C 全域能力) |
| §7 A/B 矩阵两类题型各 3-4 题 | §7.1 精确查询 4 题 (T1-T4) + §7.2 全域对比 4 题 (T5-T8) | 精确 + 全域各等权 |
| §3.2 Q3=C 对应表 | "spec/knowledge 全量 (支撑精确查询)" | 可追溯 |

**Q3=C 乘入: VERIFIED**

### Q4=A (terminology 高频段注入 ~713K) 乘入

| 乘入位置 | 具体体现 | 追溯 |
|---------|---------|------|
| priority_weight P2=1.5 | §3.1: "P2 (terminology_core) = 1.5 (Q4=A 注入但体量上给予合理节制)" | 显式标注 Q4=A |
| position_fit=0.9 (尾部) | §3.1: "尾部 terminology (04 position=0.9, recency bias; 若 >250K 降至 0.6 触发 §8 R2)" | 尾部放置 + 超大降级阈值 |
| §2.4 merge_for_gemini.py 位置策略 | "04 (terminology) 高频优先, 尾部留给最常查的 codelist (recency bias 有利)" | 代码级落地 |
| P12 末尾召回 hard checkpoint | §1.3 P12 T-tail-1/T-tail-2 | Q4=A 注入后必须强验 |
| §3.2 Q4=A 对应表 | "04_terminology_core.md ~200K 高频段, 尾部放置; P12 末尾召回 hard checkpoint 强验" | 可追溯 |

**Q4=A 乘入: VERIFIED**

### Q5=A (63 域全量平权) 乘入

| 乘入位置 | 具体体现 | 追溯 |
|---------|---------|------|
| coverage_weight 每域 1.0 | §3.1: "63 域 Q5=A 全量平权, 每域 weight=1.0" | 显式 |
| §4 Phase B B2/B3 全量合并 | "02/03 文件不减配低频域, 全量合并" | B3 产物 03_domain_knowledge.md 全量 |
| §3.2 Q5=A 对应表 | "Phase B 02/03 文件不减配低频域, 全量合并" | 可追溯 |

**Q5=A 乘入: VERIFIED**

### 乘入总结

Rule E 三个用户优先级 (Q3=C / Q4=A / Q5=A) 均在打分公式中有明确数值体现, 且可追溯到具体 PLAN 段落. **无事后重平衡风险.**

---

## 公开语义正确性 (Gemini vs ChatGPT)

### 审查结论: CORRECT

**Gemini "公开" = 链接分享给同事 (定向/内部传播)** — 正确体现在以下位置:

| 位置 | 原文 | 评判 |
|------|------|------|
| §0 修订记录 | "Phase 1 Q3 澄清: Gemini '公开' = 分享链接给同事 (定向/内部), 非 GPT Store 全网广播 → §4 Phase F 发布决策 + §7 A/B 矩阵不含陌生公开受众语气题" | 正确 |
| §4 Phase F1 | "选项 B (可选扩展): 分享链接给同事 (定向内部传播, Viewer 权限; **不追求** Store 式广播发现, 与 ChatGPT 公开路径语义不同)" | 正确; 与 ChatGPT 对比明确 |
| §7 设计原则 | "**不含陌生公开受众语气题** (本平台分享语义 = 给同事, 非广播)" | 正确 |
| §8 R3 | "澄清本平台'公开' ≠ GPT Store 广播 (Phase 1 Q3 session 澄清已落地 _progress.json)" | 正确; 引用 _progress.json 证据 |
| _progress.json | publish_scope_semantics_clarification_2026-04-20 字段: "Gemini 的'公开' 语义 ≠ GPT Store 全网广播, 而是'分享链接给同事'(定向/内部传播)" | 证据链完整 |

**A/B 矩阵不含陌生公开受众语气题**: §7 矩阵 10 题 (T1-T9 + T10 optional) 全部面向"SDTM 专业使用者"视角, 无"外部陌生用户能否理解"类测试. CORRECT.

**Phase F 发布决策**: 两个选项均为 "私有 OR 链接分享给同事", **不含 Store 式公开发布路径**. CORRECT.

---

## Phase 1 F-1 Carry-over 三处一致性

| 位置 | 内容 | 一致性 |
|------|------|-------|
| §1.3 P12 | "Phase D 终态 A/B 矩阵必含 2 道末尾召回精确 term 题 (hard checkpoint): T-tail-1 (末尾 ≤10% 位置) + T-tail-2 (中段 40-60% 位置, Lost-in-Middle 验证)" | 建立 gate |
| §4 Phase D | D1 "10 题含末尾召回 2 题"; D2 "P12 末尾召回 hard checkpoint 独立 gate 判定 (2 题均 PASS 才放行)"; D3 独立 reviewer; §7.3 T-tail-1/T-tail-2 详细题目 | 兑现 gate |
| §8 R1 | "触发信号: T-tail-1 或 T-tail-2 FAIL; 响应: 1 题/2 题均 FAIL 各有处置; 兜底: P12 hard checkpoint 保证该风险不漏网" | 风险兜底 |

**三处内容互相一致, F-1 carry-over 完全兑现. VERIFIED.**

---

## research.md 8 条修订吸收

§1.4 "Phase 1 Research '对 PLAN 的修订' 8 条吸收" 逐条核查:

| # | research.md 原条目 | §1.4 PLAN 吸收 | 追溯 |
|---|------------------|--------------|------|
| 1 | E section "仅个人" → 2025-09 起支持链接/公开/Workspace | "§4 Phase F 发布决策给出 '私有默认 + 可选分享' 分支; A/B 不含陌生受众语气 (Q3 澄清)" | §4 F1 + §7 |
| 2 | 公开发布=否 → 已支持 | 同上 (合并处理) | §4 F1 |
| 3 | F-1 末尾数字无来源 → 官方区间 | "P12 明示 hard checkpoint; §8 R1 持续监控" | §1.3 P12 + §8 R1 |
| 4 | 文件 3-5 合并, 硬限 10 确认 | "§2 设计 4 文件 + 1 spare 余量; 硬限 10 文件标注" | §2 文件结构 |
| 5 | 单文件大小上限 100MB 精确 | "§2 单文件目标 <5MB, 不构成瓶颈" | §2 + P11 |
| 6 | pricing URL 待核 → AI Plans URL 给出 | "§2 不涉及 PLAN, 仅记录" | §1.4 row 6 |
| 7 | 2M tokens API 层澄清 | "§2 按 1M 规划, 不依赖 2M" | P11 + §5 |
| 8 | Q4 API 复用 → Gems 与 API 不共享 | "§9 开放问题 Phase 7 独立路径" | §9 item 1 |

**8/8 修订均已吸收, 可追溯到 PLAN 具体段落.**

---

## 18 Task 合理性 + 12 Hard Checkpoint 必要性

### Task 数量合理性

| Phase | Tasks | 评判 |
|-------|-------|------|
| A (Setup) | 3 (A1/A2/A3) | 合理; 均为 none checkpoint 轻量操作 |
| B (合并产出) | 6 (B1-B6) | 合理; B1 脚本 + B2-B4 三阶段产出 + B5 语义抽检 + B6 校验 |
| C (Gem 创建+上传) | 3 (C1/C2/C3) | 合理; Instructions + 上传 + 烟雾测试 |
| D (A/B 矩阵) | 3 (D1/D2/D3) | 合理; 跑题 + P12 gate + 独立 reviewer |
| F (发布决策) | 2 (F1/F2) | 合理; F2 仅条件执行 |
| G (收束) | 5 (G1-G5) | 合理; Retro + 教程 + ROADMAP + 索引 + commit |

**18 Tasks: 合理**

### 12 Hard Checkpoint 必要性逐一审查

| Checkpoint | 必要性理由 | 评判 |
|-----------|---------|------|
| B2 (token 实测偏差 >15%) | 01+02 产出后第一个累计 token 校验点; 若此时已超预期, B3/B4 会更严重; 早发现早止损 | **合理** (但级别略高, 见下方分析) |
| B3 (累计 token 阶段校验) | 03 产出后核实累计是否超 600K; 超则需重估 04 策略; 防止 B4 超出 900K 硬限 | **合理** (同上) |
| B4 (总累计 ≤800K 验证) | P11 硬约束的直接验证; >900K 触发 §8 R2 降级决策 | **明确必要** |
| B5 (Rule A 语义抽检 N=5) | Q4=A 对 terminology 做选择性注入 = 改写 >50%; 规则 A 强制触发 | **明确必要** |
| C1 (Instructions reviewer lane) | System Prompt 直接决定回答质量; 规则 D 写审分离; 此处无独立审则整个 PLAN 的规则 D 形同虚设 | **明确必要** |
| C2 (用户上传确认) | 手工操作 + 用户握手; 无法自动化验证; 用户 ack 是唯一确认手段 | **明确必要** |
| D1 (终态 A/B 10 题) | 终态回归; 规则 D 独立 reviewer | **明确必要** |
| D2 (P12 末尾召回独立 gate) | Phase 1 F-1 carry-over 的专属兑现; 2 题均 PASS 才放行; 独立于 D1 的总 PASS 率 | **合理** (见下方说明) |
| D3 (独立 reviewer 复核) | 规则 D 在终态 A/B 的执行; D1 是 writer 跑题 + 记录, D3 是 reviewer 判定 | **明确必要** |
| F1 (用户拍板发布范围) | 发布决策不可代判; 用户手动确认 | **明确必要** |
| G1 (RETROSPECTIVE 独立复核) | 规则 C + 规则 D 联合要求; Tier 2 收尾必须 | **明确必要** |
| G5 (commit + push 用户 ack) | 最终归档; push 到 main 不可逆 | **明确必要** |

**B2/B3 hard 级别分析**:

B2 和 B3 的 hard 定义是"token 实测偏差 >15% 触发审查" (B2) 和 "累计 >600K 考虑降级 04" (B3). 两者都是**条件触发内部审查**, 而非"用户 ack 握手"或"独立 reviewer lane". 严格定义下, hard checkpoint 应含 (a) 人工 ack 或 (b) 独立 reviewer 复核. B2/B3 更接近**有预警阈值的 soft checkpoint**.

然而, 在本平台 (Tier 1-2, token budget 是单批到位的唯一扩缩依据) 将 B2/B3 标为 hard 有其防御价值: 防止 executor 自行判断"15%以内 OK"而跳过。将两者保持为 hard 是**略微保守但可接受**的设计——不构成 FAIL, 记为 CONDITIONAL 缺口 (LOW)。

**D2 独立于 D1 的必要性**:

D2 是 Phase 1 carry-over F-1 的专属落地, 有独立的 checkpoint 产物文件 (`D2_tail_recall_gate.md`). D1 的 PASS 门槛是"总 PASS ≥90%", 而 D2 的 PASS 门槛是"末尾 2 题均 PASS" — 两个条件独立 (可能总 PASS ≥90% 但末尾 2 题均 FAIL). 因此 D2 作为独立 gate **必要性成立**.

**综合评判**: 12 个 hard checkpoints 中 10 个明确必要, B2/B3 略高于标准定义但有防御价值. 整体偏多但在 Tier 1-2 可接受范围内.

---

## Q4 terminology position 数字依据

### 审查对象

§3.1 position_fit 数值:
- 01 (导航层前置): 0.9
- 02-03 (中段 spec/knowledge): 0.7
- 04 (尾部 terminology): 0.9, 若 >250K 降至 0.6

### 依据分析

| 数值 | 依据来源 | 合理性 |
|------|---------|-------|
| 0.9 (头部+尾部) | recency bias (尾部) + primacy bias (头部); Google 官方建议 "put query at the end" 暗示尾部权重高; 头部也因 primacy 效应相对安全 | **合理经验值**, 非随意 |
| 0.7 (中段) | "Lost in the Middle" 效应 (Liu et al. TACL 2024, Chroma 2025 18 模型实测); research.md Q1: "中间位置才是最危险区" | **有研究支撑的方向性判断** |
| 0.6 (>250K 降级阈值) | 04 体量过大时 recency bias 减弱 (高频 codelist 仍在末尾但"尾部"范围扩大导致中间化); §8 R2 触发降级决策 | **保守防御值, 合理** |

**注意**: 这些数值是打分公式的权重系数, 是内容排布优先级的设计决策, **不是宣称的 Gemini 实测召回率**. 因此无 hallucinate 风险——这是 PLAN 设计层面的参数, 而非数据层面的断言.

**结论**: 数字有依据, 方向正确, 无随意性. VERIFIED.

---

## 缺口 / hallucinate 风险

### 缺口 1 (LOW) — B2/B3 hard checkpoint 定义略高于标准

**描述**: B2 ("token 偏差 >15% 触发审查") 和 B3 ("累计 >600K 考虑降级") 被标为 hard, 但实质是条件预警 + 内部审查, 缺乏独立 reviewer lane 或用户 ack 的 hard 定义要件.

**风险**: executor 执行时可能对"hard"理解有歧义 — 是"触发则立即停等用户 ack"还是"触发则内部审查再继续"? PLAN 描述更接近后者, 与 hard 定义有微小矛盾.

**建议**: Phase 3 执行前, 主 session 向 executor 澄清 B2/B3 的 hard 处置方式: token 偏差 >15% → 写 trace 记录 + reviewer 确认偏差原因 + 主控 ack. 不需要修改 PLAN, 执行时口头澄清即可.

**阻断性**: 不阻断. LOW.

### 缺口 2 (LOW) — §7 "10 题" 与实际 12 条目有计数差异

**描述**: §7 A/B 矩阵标题和 §5 批次表均称 "10 题", 但 §7 实际列出 T1-T9 + T10(可选) = 10 必答 + 1 可选, 加上 T-tail-1/T-tail-2 = 共 12 条目 (其中 T-tail-1/T-tail-2 已包含在 T1-T9 外的 §7.3). 

实际计数: T1-T4 (4) + T5-T8 (4) + T-tail-1 + T-tail-2 (2) + T9 + T10-opt (2) = 12 条目. 但 §7.5 的 "10 题中 ≥9 PASS" 与 D1 的 "10 题" 一致. 差异在于: T-tail-1/T-tail-2 IS included in the 10 required questions — the 10 count is T1-T4 + T5-T8 + T-tail-1 + T-tail-2 + T9 = 10, with T10 optional making 11th.

**风险**: 轻微计数混乱可能导致 executor 对"哪些是必答 10 题"有疑问. §7.5 门槛 "10 题中 ≥9 PASS" 与"T-tail-1/T-tail-2 独立 gate"并行运作是否存在交叉? 答案是不存在 (末尾 2 题即使入 10 题计算, 其独立 gate 仍独立于 ≥90% 门槛). 

**建议**: Phase 3 前确认执行者理解 "必答 10 题 = T1-T9 + T-tail-1 + T-tail-2 (其中 T-tail-1/T-tail-2 = §7.3)" 的组成, T10 为可选第 11 题.

**阻断性**: 不阻断. LOW.

### hallucinate 风险扫描

全文未发现以下危险模式:
- 声称未公开的 Gemini 精确召回率数字 — **未发生**
- 将 API 层 2M 窗口等同于 Gems Web UI — **已明确区分** (P11 + §5 + §9 Q1)
- 将 Lost in the Middle (GPT-3.5/4 论文) 直接外推为 Gemini 精确数字 — **未发生** (§3 仅用作方向性参考, 有独立 Gemini 证据链)
- 声称 Gem Marketplace / Store 存在 — **未发生** (§4 F1 明确 "不追求 Store 式广播", §9 Q4)
- Token 估算数字来源不明 — **可追溯** (~713K = ~513K core + ~200K terminology, 来自 research.md + Rule E Q4=A)

**hallucinate 风险: 无**

---

## 放行结论

### 审查总分

| 审查项 | 状态 |
|--------|------|
| P1-P12 覆盖 | 12/12 PASS |
| Rule E Q3/Q4/Q5 乘入 | 全部 VERIFIED |
| 公开语义正确 (Gemini=链接分享给同事) | CORRECT |
| F-1 carry-over 三处一致 | VERIFIED |
| research.md 8 条修订吸收 | 8/8 VERIFIED |
| 18 Task 合理性 | 合理 |
| 12 Hard Checkpoint 必要性 | 10/12 明确必要, B2/B3 略高但可接受 |
| Q4 terminology position 数字依据 | 有依据 (非随意值) |
| 批次 = 1 (单批到位) | VERIFIED |
| 无 hallucinate | VERIFIED |
| 失败归档规则 B 路径 | §6.2 明示 |
| Phase E merged to D 合理性 | 合理 (Tier 1-2 轻量, carry-over 已在 D 兑现) |
| Lost-in-Middle 警示保留 | VERIFIED (§3.1 中段 0.7 + research.md Q1 审慎注记) |

### CONDITIONAL_PASS 条件

**CON-1 (LOW)**: Phase 3 执行前, 主 session 向 executor 口头澄清 B2/B3 hard checkpoint 的处置方式 (token 偏差 >15% → trace 记录 + reviewer 确认 + 主控 ack, 不是自行判断继续). 不需要修改 PLAN.

**CON-2 (LOW)**: Phase 3 执行前, 主 session 确认执行者理解 A/B 必答 10 题的组成 (T1-T4 + T5-T8 + T-tail-1 + T-tail-2 + T9 = 10; T10 为可选第 11 题). 不需要修改 PLAN.

以上两条均为执行层面的口头澄清, **不阻断 Phase 2 → 3 gate 放行**.

### 放行: YES

**理由**: PLAN.md 覆盖全部必备结构 (P1-P12 + §0-§10), Rule E 三个优先级 (Q3=C/Q4=A/Q5=A) 均已乘入打分公式且可追溯, 公开语义正确反映"Gemini=链接给同事"而非 Store 广播, F-1 carry-over 三处一致, research.md 8 条修订全部吸收, 18 Task 结构合理, 12 hard checkpoint 整体可接受 (2 条偏多但不构成实质风险), 无 hallucinate 数据. 两条 LOW 缺口均不阻断. 可进入 Phase 3 落地执行.

---

*Reviewed by: oh-my-claudecode:verifier subagent (独立 lane, 规则 D 满足)*
*参考文件: PLAN.md + platform_profile.md + research.md + phase1_reviewer.md + _progress.json + _template/04_plan.md + _template/05_solution.md + SYNC_BOARD.md*
