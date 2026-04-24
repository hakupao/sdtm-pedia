# R2 Retrospective — Gemini Gems smoke v4 v6-post-A1 (2026-04-23)

> **Scope**: R2 单平台 Gemini Gems v6-post-A1 × 17 题 (Q1-Q14 + AHP1-3) cowork re-run
> **Rule C 强制**: Tier 2/3 项目收尾必写 retro, 三段式 (保留 / 缺口 / 决策)
> **前置**: `ai_platforms/R1_RETROSPECTIVE.md` (R1 baseline, AHP × 3 FAIL 根因); `ai_platforms/gemini_gems/dev/evidence/r2_13th_reviewer.md` (13th reviewer CONDITIONAL_PASS); `smoke_v4_r2_results.md` (R2 分项总分)

---

## 1. R2 整体结果

| 指标 | R1 (post 13th reviewer A3) | R2 (v6-post-A1) | 变化 |
|---|---|---|---|
| Q1-Q10 主 gate | 8.5/10 (85%) | **9.5/10 (95%)** | +1.0 |
| AHP × 3 hard gate | **0/3 (0%)** | **3/3 (100%)** | **+3** |
| 主 gate 合计 | 8.5/13 (65.4%) **FAIL** | **12.5/13 (96.2%) PASS ✓✓** | +4.0 pts |
| Bonus Q11-Q14 strict | 3.5/4 | 3.5/4 | 0 |
| 全量分 strict | 12.0/17 (70.6%) | **16.0/17 (94.1%)** | +4.0 / +23.5% |
| 双硬 gate | FAIL (AHP 0/3) | **PASS ✓✓** (Q1-Q10 9.5≥7, AHP 3≥2) | Gate OPEN |

**核心结论**: Gemini Phase 4 gate 完全闭合 + Phase 5 ready. AHP × 3 全线修复是 v6 CO-5 的最大成就.

---

## 2. 保留下来的做法 (Rule C 第 1 段)

### R2-1. Cowork Chrome MCP 单 session 连续跑 17 题

**做法**: 主 session 直接 Chrome MCP 控制 Gemini Gem, 每题 "new chat → fill → click send → wait_for → extract answer → write file → score inline", 17 题在同一 session 链式完成.

**为什么保留**: (1) 每题 fresh chat 避免 cross-question context 污染 (R1-1 对 R2 的延续); (2) 单 session 保 prompt 一致; (3) 直接 inline score, 避免 batch end 重读.

### R2-2. v6 CO-5 anti-hallucination 三子 (AHP-V1/V2/V3) system prompt 级锚

**做法**: 在 v5c 基础上加 CO-5 整节 (~2.1K chars) + 3 子章 (变量 / 跨域 / deprecated). 配合 Workflow Step 0 前提核 + 边界模板 ⑥⑦⑧ + 工作流程 Step 10 sanity 自检.

**为什么保留**: R2 AHP × 3 全 PASS+ 证明 system prompt 级 anti-hallucination 锚**可以修** training-data hallucination. 这推翻 R1 时期 "Gemini 的 hallucination 是训练数据固有, prompt 无法修" 的假设. **一次性 ROI 最大的修复**.

### R2-3. Rule D 13th reviewer (`pr-review-toolkit:code-reviewer`) 先审 prompt

**做法**: v6 draft 写就后先派 13th reviewer 独判 (不是 R2 跑完再审), CONDITIONAL_PASS 3 条件 (A1 dual-grep + A2 char check + A3 Q13 rescore) 主 session 先 fold A1+A3 再 apply v6 跑 R2.

**为什么保留**: "审-改-跑" 链条比 "跑-错-再改" 省一轮. 13th reviewer 发现的 A1 dual-grep (anti-false-positive NSV) 虽然**没有任何 R2 题触发其 false-positive 场景**, 但 AHP1 答案显式调用了 "双核 grep 02+01" 流程, 说明 prompt 锚到了推理路径.

### R2-4. 13th reviewer A3 Q13 re-score 在 R1 baseline 上预先 apply

**做法**: 13th reviewer 判 R1 Q13 应 PASS → PARTIAL (ARMCD 值错 + OBSERVATIONAL GROUP 虚构). 主 session 在 smoke_v4_results.md + SMOKE_V4.md §3 + R1_RETROSPECTIVE.md 预先 apply A3.

**为什么保留**: R2 跑完对 R1 做 apples-to-apples 对比时, Q13 新 defect 与 R1 post-A3 baseline 对齐 (两者都 PARTIAL), 不会掩盖 R1 原始 bonus 4.25/4 的虚高. R2 强调的是 AHP × 3 + Q1-Q10 提升, 而非 bonus 波动.

### R2-5. Inline self-score + Gate 判定独立于总分

**做法**: 每题 answer.md 写 "Self-score verdict" section, 显式 PASS / PARTIAL / FAIL + 判据对照 + R1 vs R2 对比. 主 gate Q1-Q10+AHP 与 Bonus Q11-Q14 两套 gate 分别算, 双硬 gate (Q1-Q10 ≥ 7 + AHP ≥ 2) 独立判.

**为什么保留**: 双 gate 解耦避免 "bonus 高分掩盖 main gate 能力缺陷" 的 R1 陷阱. R2 Q1-Q10 9.5/10 + AHP 3/3 既确保 Core SDTM 能力, 又要求 anti-hallucination 硬底线.

---

## 3. 必须补上的缺口 (Rule C 第 2 段)

### G-R2-1. Q1 GFGENE 自相矛盾 (v6 CO-4 规则被自己违反) — **HIGH 优先, v7 必修**

**问题**: Q1 R2 答 "Core=Exp 变量" 时列 GFGENE (Gene Name). v6 CO-4 §GF L102 明文列 GFGENE 为"禁止臆造"清单第 4 项. Gemini 一边用一边在末尾预警"请勿用 GFLOC/GFVARIANT" 却漏 GFGENE — **self-contradictory**.

**影响**: R1 Q1 PASS → R2 Q1 PARTIAL (0.5), Q1 是唯一 regression 主题. 泛化风险: v6 CO-4 禁止清单在 GF 域深入问答下非 100% 生效.

**v7 必补**:
1. CO-4 §GF 禁止清单加 hard anchor: "任何 GF Exp/Req 变量清单必以 KB 实际 spec 为准, 禁套 --GENE / --VARIANT / --CHROM / --LOC / --REFVER / --STYPE / --VALGRP 通用模式"
2. 工作流程 Step 0 加 "若用户问 Req/Exp 变量清单, 先 grep 02 spec 的 Core=Req + Core=Exp 真实列, 再答"
3. Sanity 自检 (Step 10) 加 "若答案含 CO-4 禁止清单任一名, 删全篇重答"

### G-R2-2. Q13 ARMCD-null 规则未进 v6 — **HIGH 优先, v7 必修**

**问题**: R2 Q13 (b) 复制 R1 同款 defect: ARMCD="NOTASSGN" + ARMNRS C66770 (应 C142179). 13th reviewer A3 识别 R1, 但 v6 没补这个 rule, R2 仍 FAIL.

**影响**: Q13 R1 → R2 无变化 (都 PARTIAL 0.5), bonus 3.5/4 稳定. 但证明 "Gemini 对 SDTMIG v3.4 ARMCD-null 规则是系统性 prompt gap, 非 R1 偶发".

**v7 必补**:
1. CO-1c 或 CO-4 扩充 "ARMCD null 规则": 无 planned arm 观察性研究, **ARMCD 必 null (非 'NOTASSGN' 8-char 缩写), ARM 必 null, ARMNRS 填全称 (C142179 Extensible=Yes, 值含 'NOT ASSIGNED' / 'SCREEN FAILURE' / 'ASSIGNED, NOT TREATED' / 'UNPLANNED TREATMENT')**
2. Routing 规则扩: 业务场景 "RWD/observational / DM 无 planned ARM" → FA check ARMCD-null rule

### G-R2-3. 14th slot reviewer 尚未回交 — 本次 retro 缺独立复核

**问题**: 主 session self-score 17 题 → 写 results → 写 retro, 14th slot reviewer (`oh-my-claudecode:verifier`) 后台跑中但未回. Rule D 独立隔离原则要求对 R2 scoring 有独立审.

**R2 补**: 14th reviewer 回交后决策:
- 若 verdict 与主 session 一致 → 本 retro 落档, Phase 5 合流 ready
- 若 verdict 冲突 (e.g., Q1 应 PASS 非 PARTIAL, 或 AHP PASS+ 应 PASS) → 主 session 根据 confidence + 证据 重判

**Carry-over**: 14th reviewer 产物 `ai_platforms/gemini_gems/dev/evidence/r2_14th_reviewer.md` 必须主 session 接收后, 更新 _progress.json checkpoints_acked 数组 + 视需要修订 results.md.

### G-R2-4. R2 未派跨平台 cross-check (Rule E 单平台)

**问题**: R2 仅 Gemini re-run. 其他 3 平台 (Claude 17/17 / ChatGPT 16.5/17 / NotebookLM 15/17) 未同步 R2. Rule E (跨平台 cross-check 作 multi-reviewer baseline) 在 R2 不满足.

**Note**: R1 跨平台矩阵 (SMOKE_V4.md §3) 已提供 ground truth — Claude/ChatGPT/NotebookLM 的 AHP × 3 答案作为 "正确识破应该长什么样" 参考. R2 Gemini PASS+ 是否真达其他 3 平台级别, 需 14th reviewer 对比判定.

### G-R2-5. v6 效果"真修 vs 表层"的泛化性未证

**问题**: v6 CO-5 AHP-V1/V2/V3 在本组 3 个 AHP 上 work, 但:
- 如果用户换一个新的 variable hallucination 探针 (非 LBCLINSIG), CO-5 AHP-V1 是否仍触发?
- 如果跨域幻觉不提 "Trial-Level SAE Aggregate 表" 而提其他如 "Multi-Subject Aggregate View", 是否还识破?
- 如果 deprecated concept 不是 PF 而是 PG 或其他历史域, 是否识破?

**14th reviewer 应独判**: 这是真 "prompt 级 anti-hallucination 机制" 还是 "3 个特定 trap 记忆"? 若后者, v7 需泛化 CO-5 规则.

---

## 4. 关键决策复盘 (Rule C 第 3 段)

### D-R2-1. 直接 apply v6 不压缩 — **正确**

**决策**: v6 18,716 chars (+68% vs v5c 11,132). 13th reviewer Risk B 提出 "char budget prime-position dilution", 建议 pre-verify UI 接受. 主 session 未压缩, 直接 paste.

**回头看**: **正确**. (1) Gem UI 接受 18.7K (Save disabled 验证 saved); (2) CO-4 在 Q2/Q3 (v3.4 新域) R2 仍 PASS+, prime position dilution 未发生; (3) R1 时期 v5c CO-4 效果好的部分 R2 保留; (4) 新加的 CO-5 整节 work.

**但需注意**: Q1 R2 GFGENE regression 虽然不归因于 char budget 膨胀, 但 v6 CO-4 §GF 禁止清单已在 v5c 中存在, R2 仍违反. 说明 **prompt 规则长度不是问题, 执行机制才是**.

### D-R2-2. AHP × 3 hard gate 双约束 — **正确**

**决策**: R2 阈值改 "Q1-Q10 ≥ 7 + AHP ≥ 2/3" (R1 曾评价 8.5/13 summing).

**回头看**: **正确**. 若不设 AHP hard gate, R2 Gemini 12.5/13 + Q13 PARTIAL 0.5, R2 = 16.0/17 = 94.1% 总分会掩盖假如 AHP 反弹为 FAIL 时的 "核心能力缺失". 新阈值确保 Core SDTM 过 95% 同时 anti-hallucination 稳定过 67%.

### D-R2-3. Q1 regression 严格判 PARTIAL 不升 PASS — **保留但争议**

**决策**: Q1 abcd 子问全对 + 域 + 5 Req 全对, 但 Exp 列用 GFGENE (CO-4 FAIL 判据明文触发). 主 session 判 PARTIAL (0.5).

**回头看**: **严格但可争议**. 14th reviewer 可能判 PASS (abcd 占主, Exp 小瑕). 主 session 取严, 原因: (1) v6 CO-4 正是 R1→R2 要修的东西, 自违反不应 credit; (2) R2 整体已过双 gate, Q1 PARTIAL 不影响 Gate OPEN, 不需要争高分.

**14th reviewer 若升 Q1 为 PASS**: Q1-Q10 变 10/10, Main gate 13/13 = 100%, Strict 16.5/17 = 97.1%. 但 v7 carry-over 仍保留 GFGENE 问题.

### D-R2-4. Q13 与 R1 同 PARTIAL 不再下调 — **正确**

**决策**: R2 Q13 与 R1 post-A3 Q13 同样 ARMCD 规则 defect. 判 PARTIAL (0.5) 与 R1 对齐.

**回头看**: **正确**. Q13 是 "v6 未修" 问题, 不是 R2 新 defect, 判同等 0.5 反映 "v6 覆盖空缺 ≠ R2 regression". V7 补后再升.

### D-R2-5. R2 retrospective 并列 R1_RETROSPECTIVE.md — **正确**

**决策**: 写成独立 `R2_RETROSPECTIVE.md` (本文) 而非在 R1_RETROSPECTIVE.md 追加.

**回头看**: **正确**. R1 文件锁定 R1 决策快照 (不修), R2 文件做 R1 基础上的增量. 若 v7 → R3, 再写 `R3_RETROSPECTIVE.md`. 保持决策可溯源.

### D-R2-6. 14th reviewer 派 `oh-my-claudecode:verifier` 非 `feature-dev:code-reviewer` — **正确**

**决策**: Rule D chain 13 slots 已烧, 14th 候选 `oh-my-claudecode:verifier` 或 `feature-dev:code-reviewer`. 选前者.

**回头看**: **正确**. verifier 专做 "verification before completion" 职责, 对 R2 "是否真过 gate / v6 是否真 work" 问题更契合. code-reviewer 更适合代码修改类审阅, 非 prompt/evidence 验证.

---

## 5. R2 → Phase 5 pointers

1. **等 14th reviewer 回交** → 根据 verdict 决定:
   - PASS/CONDITIONAL_PASS → Gemini Phase 4 正式闭合 → SYNC_BOARD row → Phase 5 ready
   - FAIL → 主 session 重判 / 补证据 / 可能重跑部分题
2. **v7 iteration 可选 (post Phase 5)**: Q1 GFGENE 强化 + Q13 ARMCD-null 锚 + 14th reviewer 若指出 CO-5 泛化性缺陷
3. **跨 4 平台 Phase 5 RETROSPECTIVE**: 等 NotebookLM P3.9 拉齐 + ChatGPT R2 (可选) + Claude R2 (可 skip) → 4 平台合流写 `PHASE5_RETROSPECTIVE.md`
4. **Rule E 候选**: R2 单平台 re-run 证明 "cross-platform cross-check 是 ground truth" 假设依然有效 — R1 跨平台矩阵作 R2 verdict 的 "correctness oracle"

---

## 6. Rule A/B/C/D/E 合规自查

- **Rule A (语义抽检)**: 主 session 逐题 inline score + 17 题 answer.md 判据对照 + R1 vs R2 显式对比 + 14th reviewer 独审. **Pending** 14th reviewer 回交最终 sign-off.
- **Rule B (失败归档)**: Q1 GFGENE + Q13 ARMCD 同款 defect 完整归档 answer.md (annotated "REGRESSION" + "R1 vs R2 对比"). ✓
- **Rule C (Retro 强制)**: 本文即 R2 retro, 三段 (保留 R2-1-5 / 缺口 G-R2-1-5 / 决策 D-R2-1-6). ✓
- **Rule D (审阅隔离)**: R2 scoring 由主 session 独立于 13th reviewer (他只审 prompt+R1); 14th reviewer (`oh-my-claudecode:verifier`) 后台跑中独审 R2 scoring. **Pending** 回交.
- **Rule E (跨平台 cross-check)**: R2 单平台 Gemini, 与 R1 4 平台矩阵 ground truth 隐式对照. 无额外 R2 平台跑, 但这在 R2 设计阶段已决策 (不需全平台 R2).

---

*v1.0 2026-04-23 PM. R2 lifecycle 收尾. Gemini 双硬 gate 全过, Phase 4 gate 闭合, Phase 5 ready. 14th reviewer 回交前本 retro 为 draft, post-回交可能微修 §3/§4.*
