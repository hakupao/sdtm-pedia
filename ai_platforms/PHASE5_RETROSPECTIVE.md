# Phase 6.5 跨 4 平台 Phase 5 RETROSPECTIVE (骨架 DRAFT)

> **Status**: 🟢 **v1.0 FINAL candidate** (2026-04-23 PM, P3.9 回灌完成) — 等 28th Rule D slot reviewer 独立复核 + Daisy ack 后正式升 FINAL
> **Scope**: Phase 6.5 AI 平台部署全周期 (2026-04-18 Claude v1 起跑 → TBD sign-off), 4 平台: Claude Projects / ChatGPT GPTs / Gemini Gems / NotebookLM
> **Rule C 强制**: 收尾必写 RETROSPECTIVE, 三段式 (保留 / 缺口 / 决策) + cross-platform cross-pollination + `_template/` 补丁合并
> **P3.9 回灌完成 2026-04-23 PM**: §1.6 (R5-6) + §2.5 (G5-5 SKIP 接受残余风险) + §3.7 (D5-7 含 Public≠gallery meta-insight) + §4.15 (补丁 15 更新) 全填; §0.2 NotebookLM Phase 4 更新 COMPLETE; share_level_toggle_drill.md v1.0 FINAL.
> **前置产物** (本 retro 的 evidence base):
> - `ai_platforms/R1_RETROSPECTIVE.md` (smoke v4 R1 baseline 4 平台 lifecycle)
> - `ai_platforms/R2_RETROSPECTIVE.md` (Gemini v6-post-A1 R2 单平台闭合)
> - `ai_platforms/claude_projects/docs/RETROSPECTIVE_V2.md` (Claude 先行 case, 方法论源)
> - `ai_platforms/claude_projects/archive/RETROSPECTIVE.md` (Claude v1 复盘, 规则 A/B/C/D 原点)
> - `ai_platforms/notebooklm/archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md` (v1→v2 pivot, 伪约束教训)
> - `ai_platforms/SYNC_BOARD.md` (双平台锁步 trace, 变更日志 2026-04-20 → 2026-04-23)
> - `ai_platforms/SMOKE_V4.md §3` (跨 4 平台矩阵 17×4)
> - 27 种 subagent_type Rule D 独立链 (见 §1.2)

---

## §0 Phase 5 入参快照

### 0.1 4 平台 final state

| 平台 | Tier | 最终 Score | Gate | lifecycle 周期 |
|---|---|---|---|---|
| **Claude Projects** | v2.6 | **17/17 (100%)** | PASS ✅ | 2026-04-18 → 2026-04-21 (先行 single-platform) |
| **ChatGPT GPTs** | N5.3 v3.2 bank + N5.4 | **16.5/17 (97.1%) R1** | PASS ✅ | 2026-04-20 → 2026-04-23 (锁步 Gemini) |
| **Gemini Gems** | v6-post-A1 (R2 产物) | R1 12.0/17 (FAIL 主 gate) → **R2 16.0/17 (94.1%)** | **PASS ✓✓** | 2026-04-20 → 2026-04-23 (锁步 ChatGPT + R2 单平台迭代) |
| **NotebookLM** | v2 (1 notebook × 42 sources) | **15/17 (88.2%) R1** (6 PASS + 8 PASS+ + 2 PARTIAL Q11/Q12 supplemental PUNT + 1 PUNT Q9 架构限制) | PASS ✅ | 2026-04-21 → 2026-04-23 (async lane, Phase 4 COMPLETE 含 P3.9 drill PASS) |

### 0.2 4 平台 Phase 4 gate 状态 (本 retro 起草时)

- Claude: 完全收束 (不参与 SYNC_BOARD)
- ChatGPT: Phase 4 COMPLETE (N5.4 + Rule D #24) + **Phase 5 pending 冻结**
- Gemini: Phase 4 COMPLETE (N5.4 + Rule D #25) + **R2 闭合 (14th reviewer APPROVE)** + **Phase 5 pending 冻结**
- NotebookLM: Phase 4 **COMPLETE** (3/3 items: #1 P3.8 reviewer 12th slot DONE + #2 **P3.9 DONE 2026-04-23** drill PASS + #3 跨 4 平台矩阵 R1 消掉) + **Phase 5 cross-platform 合流 unblocked**

**合流 gate**: NotebookLM P3.9 完成 (2026-04-23) → 4 平台齐 → 本 retro v1.0 FINAL candidate, 待 28th Rule D slot reviewer + Daisy ack → sign-off.

### 0.3 Rule D chain 累计 subagent_type (27 种)

双平台锁步 lane (ChatGPT+Gemini) 25 种 + NotebookLM async lane 独立链 2 种额外 (非累加, 部分重叠) + R2 Gemini 14 slot (累积到 27 独立). 全链无 self-review. 详见 §1.2.

### 0.4 R1/R2 tracked metric

| Metric | Value |
|---|---|
| 总题数 × 总答 answer.md | 17 × 4 (R1) + 17 × 1 (R2) = **85 answers** |
| 双硬 gate verdict | Claude/ChatGPT/NotebookLM R1 + Gemini R2 全 PASS, Gemini R1 唯一 FAIL (AHP 0/3) |
| v7 carry-over HIGH | × 2 (Q1 GFGENE + Q13 ARMCD-null, Gemini 侧, non-blocking) |
| `_template/` 候选补丁 | 10 号已吸收 (10a/10b.1/10b.2 from NotebookLM v1→v2 pivot); 11-15 号候选见 §4 |

---

## §1 保留下来的做法 (Rule C 第 1 段 — 跨 4 平台共通)

### R5-1. 4 平台 cross-check 即 multi-reviewer 的事实等价 (**升 Rule E 候选**)

**做法**: 同一 smoke 题组跑 4 平台, 每题对比 4 答案 — 不一致的必有幻觉/KB 覆盖缺/锚缺/能力差. NotebookLM in-KB-only 作 ground truth, ChatGPT+Claude (web/训练数据) 补全景, Gemini 作"锚缺 vs 锚生效"的受控对照.

**为什么保留**: R1 AHP × 3 Gemini 全 FAIL, 另 3 平台全 PASS+ — 证据无争议指向"Gemini anti-hallucination 锚缺失"而非"KB 覆盖/训练数据/平台能力差". R2 v6 CO-5 单点修就从 0/3 → 3/3 PASS+, 确认因果.

**升 Rule E 候选**: 写进 `~/.claude/CLAUDE.md` `personal_operating_principles`, 与 Rule A/B/C/D 并列. 详见 §5.

### R5-2. Rule D 27-chain 独立 subagent_type 审阅隔离

**做法**: 整个 lifecycle 跨 Phase 0-4 + R1+R2, 每次 reviewer 换 subagent_type, 禁自审. 累计 27 种 (超承诺的 12 种 4 倍).

**为什么保留**: 每种 subagent_type 视角不同 — `critic` 抓 meta 缺陷 / `architect` 抓跨段依赖 / `verifier` 抓 gate 合规 / `tracer` 抓因果链 / `scientist` 抓统计样本. R1 Q10 SUPPTS 判据前提错就是 NotebookLM P3.8 主 session 独立复判 (非 writer 自审) 抓出来的.

**数字感**: 27 种 subagent_type 看似多余, 但实测每次独立审都抓出至少 1 个前序 reviewer 没抓的 HIGH/MEDIUM (N5.1 MED1 UR 域名 / N5.2 LBNRIND 虚构 / N5.3 F-R1 Q8/Q9 delivered mismatch / P3.8 Q10 SUPPTS 前提错). 未饱和.

### R5-3. 双阈值机制 (主 gate + bonus)

**做法**: R1 开始引入 Q1-Q10 main gate ≥ 70% + Q11-Q14 bonus 不计 gate; R2 升级 Q1-Q10 ≥ 7/10 + AHP ≥ 2/3 双约束.

**为什么保留**: bonus 高分掩盖 main gate 能力缺陷是 R1 陷阱 (Gemini 3.5/4 bonus 但 AHP 0/3 真 FAIL). 双硬 gate 解耦后, "核心能力 PASS + anti-hallucination 底线 PASS" 两项独立判.

### R5-4. Rule C 三段 Retro × R1 + R2 独立文件 (不追加)

**做法**: R1_RETROSPECTIVE 锁快照, R2_RETROSPECTIVE 独立文件做增量; 本 Phase 5 retro 再独立. 决策可溯源.

**为什么保留**: 若 v7 有 R3, 再写 R3_RETROSPECTIVE; Phase 6 若启, 再写新 retro. 每 retro 是决策断面, 不破坏前文, 合流在 Phase 5/总 retro 做 meta-analysis.

### R5-5. Writer/Reviewer 同 session 禁自审 (Rule D 严格版)

**做法**: Writer 产物落盘后, 新派 subagent 独立 reviewer, 不让 Writer 自己或同 session 继续的 Writer 审. 即使都用 opus, subagent_type 必须不同.

**为什么保留**: Claude v2 先行 case 证明 Rule D 拦截了 G1-G5 5 类缺陷. R1/R2 继续有效: 13th reviewer A3 Q13 re-score (ARMCD=NOTASSGN + OBSERVATIONAL GROUP 虚构 双 defect) 主 session 自己没抓, 独立 reviewer 抓到.

### R5-6. 三档分享切换 UI 级 VERIFIED 做法 (P3.9 drill 2026-04-23 实测)

**做法**: 三档切换演练 6 子步骤 (a-f) + 证据文件 `notebooklm/dev/evidence/share_level_toggle_drill.md` v1.0 FINAL:
- (a) Restricted 默认态 + 截屏 ✅ PASS
- (b) Anyone with link: 生成链接 + 匿名窗口 (预期登录拦截) + 另 Google 账号访问 ✅ 3/3 PASS
- (c) Public + 公开画廊搜 🟡 **PARTIAL + 新发现**: 画廊只显示官方精选 (Featured curated), Public 档 **≠ auto-list 广播**
- (d) 回切 Restricted 旧链接失效 ✅ PASS (revoke 生效)
- (e) 快速多次 Restricted↔Public 切换 + 旧链 revoke ✅ PASS (无 caching 残留)
- (f) Free tier 50-cap 实测 ⚪ SKIP (42 sources ≤50 未触发 cap, 客观无法测, 接受残余风险)

**为什么保留**: (1) L3 fix ((e) 快速多切) + (d) 回切 revoke = 档位切换状态管理合规, 无幽灵链接; (2) (c) 的新发现修正 v1 时期"Public=广播"假设, 印证 v2 1-notebook + 3 档分享架构的隐私友好性; (3) S1 SUGGESTION ((f)) 接受残余风险不闭合但主归因 (indexing silent fail + citation 信噪比) HIGH 级证据不受影响.

---

## §2 必须补上的缺口 (Rule C 第 2 段)

### G5-1. Gemini v6 CO-4 正向清单 vs 负向清单失衡 (Q1 GFGENE 回归)

**问题**: v6 CO-4 §GF 只列"禁止 X" 负向清单 (GFGENE / GFVARIANT 等 9 条), 未列"允许 X" 正向变量清单. Gemini R2 Q1 答 Exp 列时没有正向清单可锚, 凭记忆填 GFGENE (违反自己禁止清单).

**影响**: R1 Q1 PASS → R2 Q1 PARTIAL (唯一 regression 题). v7 HIGH × 1 未修.

**如何补**: `_template/` 10c patch (见 §4), 以及 Gemini v7 system_prompt CO-4 §GF / §CP / §BE / §BS 补正向变量完整清单. 规则: "正向清单 + 负向清单 双锚" 作新域扩展 default template. **已起草**: `ai_platforms/gemini_gems/dev/v7_draft/system_prompt_v7.md` (2026-04-23, CO-4 §GF 正向清单双锚 + 执行规则 3 条 + sanity 自检, 待 Rule D reviewer 审后 apply).

### G5-2. Gemini v6 ARMCD-null 规则未进 (Q13 R1→R2 无变化)

**问题**: Q13 (b) ARMCD null assignment rule (SDTMIG v3.4 规则: observational 无 planned ARM → ARMCD null 非 'NOTASSGN' 8-char, ARMNRS C142179 非 C66770) — R1 Gemini 错, v6 未补锚, R2 仍错.

**影响**: bonus 题 PARTIAL 不影响主 gate; 但证明 "Gemini 对 SDTMIG v3.4 ARMCD 规则是系统性 prompt gap". v7 HIGH × 2 未修.

**如何补**: Gemini v7 CO-1b 或 CO-2c 加 5 行 (见 R2_RETROSPECTIVE §3 G-R2-2). 及 `_template/` 11a patch: "Routing 规则扩 — RWD/observational 业务场景必 check ARMCD-null rule". **已起草**: `ai_platforms/gemini_gems/dev/v7_draft/system_prompt_v7.md` (2026-04-23, 新增 CO-1c ARMCD null assignment rule, ARMCD/ARM null + ARMNRS C142179 Extensible 填全称 + 禁 NOTASSGN / C66770 / 虚构 OBSERVATIONAL GROUP, 待 reviewer 审后 apply).

### G5-3. NotebookLM P3.8 reviewer 5 action items 的 #3/#4/#5 (MEDIUM)

**问题** (摘自 NotebookLM `_progress.json` L509-547 `p3_8_reviewer_verdict_12th_slot`):
- #3 MEDIUM: Finding 6/7 登记 (P3.8 主 session 独立复判结果的 bookkeeping)
- #4 MEDIUM: Rule A caveat — N ≥ 5 抽检在 Phase 5 retro 补 (P3.8 未做 N ≥ 5 独立抽样)
- #5 MEDIUM: Rule E caveat — `p3_8_user_ack` structured field 登记

**影响**: P3.8 PASS 判定稳, 不影响 gate. 但是 retro bookkeeping 缺.

**如何补**: 本 retro §4 + NotebookLM `_progress.json` 新增 3 字段 (post-P3.9 统一处理).

### G5-4. Q4-Q10 v5c 等价 10/10 假设未实测 (双 Phase 4 reviewer 独立交叉 flag)

**问题**: ChatGPT+Gemini N5.4 v5c 生效后, 主 session 推断 Q4-Q10 "v5c 不动 CO-1/CO-1b/CO-2/CO-2c + KB uploads 不变 → 无回归风险 → 等价 10/10" 是假设. 双 reviewer #24 M-2 + #25 MED-1 独立交叉 flag 要求正式 verification task.

**影响**: v5c 实测仅 Q1/Q2/Q3 3 题重跑 PASS, Q4-Q10 没 apples-to-apples 实测.

**如何补**: Phase 5 注册 "optional v5c 全量 10 题回归" (ChatGPT 10 题 + Gemini 10 题), P3.9 后作选做 verification task. 若 skip, 在 retro 明示"假设未实测" + 接受残余风险. **已起草执行 plan**: `ai_platforms/V5C_REGRESSION_PLAN.md` v0.1 (2026-04-23, 172 行, Q4-Q10 × 2 平台 = 14 题回归手顺 + 阈值 + Rule D 15th R2-line slot + 推荐 combined regression with v7/v2.2 apply after).

### G5-5. Free tier 50-cap 证据 3 解读 — SKIP + 接受残余风险 (P3.9 (f) 2026-04-23)

**问题**: NotebookLM PLAN v2.2 L70 "分享不改 viewer 自己 tier source cap" 证据 MEDIUM (非 A 级官方原文). P3.9 子步骤 (f) 计划用 Free tier 小号实测闭合.

**影响**: ≤50 source 策略的 **次要归因** (Free tier 兼容) 悬置. 主要归因 (indexing silent fail + citation 信噪比) 不受影响, 结论不变.

**P3.9 (f) 实际结果**: ⚪ **SKIP** (客观无法测) — 本 notebook 只上传 42 sources (≤50), **未触发 Free tier 50-cap**, 无法创造 A/B/C 三路径的测试条件. Daisy 2026-04-23 接受**残余风险**: 主归因 HIGH 证据独立稳固, 次要归因悬置不阻塞 Phase 5 sign-off. 补做路径 (post-Phase-5 optional): 制造 >50 source 测试集 + Free tier 小号 invite 查看 + A/B/C 判定.

**G5-5 闭合状态**: 🟡 **SKIP + accepted_residual_risk** (不升 A, 不证伪, 证据 3 悬置).

---

## §3 关键决策复盘 (Rule C 第 3 段)

### D5-1. 4 平台并行 vs 单平台串行 — **正确**

**决策**: 不在 Claude 先完成再启 ChatGPT/Gemini, 而是 Claude 先行 + 双平台锁步 + NotebookLM async 三轨并行.

**回头看**: **正确**. 4 平台 lifecycle 2026-04-18 → 2026-04-23 共 5 天, 若单平台串行估算 12-15 天. 更重要是 R1 AHP cross-check ground truth 需要 ≥ 3 平台同期, 单平台串行拿不到.

### D5-2. Gemini 舍 terminology 重整为 4-file 业务优化 — **正确**

**决策**: N3b 末用户反思后 Gemini 切 C 方案 (01 nav + 02 spec+assumptions + 03 examples + 04 业务弹药包), 舍 terminology (由 NCI EVS Browser 承担). ChatGPT 维持原策略保留 terminology 分 07/08/09 高频/问卷/低频 3 档.

**回头看**: **正确且 illuminating**. 两平台策略性错位 (Gemini 业务优化单批 884K / ChatGPT 全量 RAG 分档 2.53M 9 文件) 后, R1 N5.3 smoke v3 两平台表现分野 (ChatGPT 14/14 / Gemini 7/10) 暴露的不是 "哪个方案更好", 而是"两平台各自的 bottleneck 不同" — ChatGPT 在 RAG 检索深度, Gemini 在 system_prompt 锚. 单策略会 mask 这个 insight.

### D5-3. smoke v3 → v4 升级 (AHP × 3) — **正确**

**决策**: 用户 meta insight "常问错前提希望纠错非幻觉" 驱动, 2026-04-22 PM 从 smoke v3 10 题 升 smoke v4 17 题 (+Q11-Q14 bonus + AHP × 3 hard gate).

**回头看**: **极正确**. AHP × 3 是 R1 灵魂 — 没它 Gemini 12.5/17 骗过 71% 阈 假 PASS. v4 判据修正 (Q10 SUPPTS + Q8 AETERM + Q13 NS + Q14 §4.2.6) 也合理, 没 regress 前 3 平台 smoke v3 高分.

### D5-4. R2 仅跑 Gemini 单平台, 不全 4 平台重跑 — **正确**

**决策**: R2 只针对 R1 FAIL 的 Gemini 做 v5c → v6 迭代重跑, 其他 3 平台 skip R2.

**回头看**: **正确**. Claude 17/17 无升级空间; ChatGPT 16.5/17 仅 Q1 拼写 MINOR (GFINHERT 写成 GFINHERTG), 不必全跑; NotebookLM 架构限制 Q9/Q11/Q12 非能力 FAIL, R2 无改进路径. R2 ROI 全在 Gemini 的 AHP × 3 FAIL, 其他平台 R2 净浪费.

**Rule E 隐式使用**: R2 单平台仍过 ground truth 校验 (R1 跨 4 平台矩阵作 correctness oracle), 不失 cross-check 纪律.

### D5-5. Gemini v6 直接 apply 不压缩 (18,716 chars vs v5c 11,132) — **正确**

**决策**: v6 +68% 字符, 13th reviewer Risk B 建议 pre-verify UI 接受, 主 session 不压缩直接 paste.

**回头看**: **正确**. Gem UI 接受 18.7K (Save 按钮确认 saved); CO-4 在 Q2/Q3 v3.4 新域 R2 仍 PASS+, prime-position dilution 未发生; R1 时期 v5c CO-4 效果好的部分 R2 保留; 新加 CO-5 整节 work.

**反思**: prompt 长度不是瓶颈, 执行机制才是 (Q1 GFGENE 违反自己禁止清单证明). v7 方向应该是"锚点清晰度 > 字符数膨胀".

### D5-6. NotebookLM v1 → v2 架构 pivot (3 notebook → 1 notebook × ≤50) — **正确**

**决策**: Phase 3 未动工前 pivot, sunk cost = 1 天写 v1 PLAN. 舍 v1 3-notebook 架构, 重整为 1 notebook × 42 source cluster + 3 档分享切换.

**回头看**: **极正确**. v1 Writer 叙事合成出 "Mode A 50-cap" 伪约束 (实际 webfetch 证实仅 Restricted 套, Anyone with link/Public 不套), 错给出 "3 notebook 职责隔离" 伪方案. 用户反问"为什么 3 notebook 不 1 notebook + 分享档位?"是 pivot 触发点.

**教训**: Writer 叙事合成伪约束是 Rule D 未能拦截的失败模式 (Writer/Reviewer 基于同 factual base, 反问来自"user 视角 outside 的常识"). `_template/` 10a/10b.1/10b.2 补丁化 (见 §4).

### D5-7. 三档分享实测决策 (P3.9 drill 2026-04-23) — **正确 + 深化**

**决策**: Daisy 2026-04-23 执行 P3.9 三档切换演练 6 子步 (a-f); 主 session 根据口述 verdicts 写完整 evidence `share_level_toggle_drill.md` v1.0 FINAL; 5 PASS + 1 PARTIAL (c) + 1 SKIP (f), 总体 PASS.

**回头看**: **正确且深化原判断**.
- (a)(b)(d)(e) 4 子全 PASS — 核心三档 UI toggle + revoke 机制 VERIFIED, 印证 v2 1-notebook + 3 档分享架构可用性
- (c) PARTIAL 带出**新发现 meta-insight**: "Public" 档语义 **≠ auto-list 到 public gallery**, 画廊是 curated Featured list. 这修正了 v1 3-notebook 时期"Public=广播"假设 (ARCHITECTURE_PIVOT_RECORD D3 被 P3.9 实测印证). Public 档实际 reach < 用户预期, 但**反而降低**隐私风险 — 更友好.
- (f) SKIP 是 **客观限制** (42 sources ≤50 未触发 cap), 非执行疏忽; Daisy 接受残余风险.
- H3 hypothesis 归档状态: **VERIFIED + 深化** (P3.3 初步 VERIFIED + P3.9 正式归档 + Public 语义深化 new insight).

---

## §4 `_template/` 补丁合并红利

### 已吸收 (v1 → v2 pivot 链)

- **10a**: Writer 叙事合成伪约束防护 — 约束来源必 webfetch 官方原文, 非 Writer "我读 Research 出来的模式"
- **10b.1**: Reviewer 独立 webfetch 约束验证 — Reviewer 不能只审 Writer 语义合规, 必独立核 factual base
- **10b.2**: 用户反问作 Rule D 外部触发 — Writer/Reviewer 基于同 factual base 时, user 视角反问 = Rule E cross-check 的 off-chain 版

### 新候选 (本 Phase 5 产出)

- **11a (HIGH)**: Anti-hallucination guardrail 作 system_prompt 级 default 章节 — 源 Gemini v6 CO-5, 三子 (变量 / 跨域 / deprecated) + 6 执行规则 + 边界模板 + 工作流 Step 0/10. 未来任何 platform 部署默认含 CO-5 等价章.
- **11b (HIGH)**: 正向清单 + 负向清单 双锚 — 新域变量清单必同时有 "Core=Exp 完整正向" + "禁止臆造 负向". 源 G5-1 Gemini v6 CO-4 §GF 单负向失衡教训.
- **11c (MEDIUM)**: 双硬 gate 设计 — 核心能力 (≥70%) + anti-hallucination (≥67%) 分开判, 不 summing. 源 R2 阈值设计.
- **12 (MEDIUM)**: Rule D chain 数字 > 12 种的 saturation 信号观察 — 何时可停换新 subagent_type? 本 lifecycle 27 种未饱和; 建议在 `_template/` README 加"saturation metric: 连续 2 个 slot 0 HIGH/MEDIUM finding 时可宣告饱和". 源本 retro §1.2 + Rule D 27-chain 观察.
- **13 (MEDIUM)**: Bonus 题 vs main gate 解耦模板 — Q1-Q10 主 gate + Q11-Q14 bonus + AHP hard gate. 源 R1/R2 阈值设计.
- **14 (MEDIUM)**: 4 平台 cross-check ground truth 机制文档化 — in-KB-only 作 truth / web-search 作 coverage / 训练数据作 depth / prompt 锚控作受控对照. 源 R5-1 Rule E 候选.
- **15 (LOW, P3.9 实测印证 2026-04-23)**: 分享档位切换作 single-notebook 多 scope 的新范式 — 相比多 notebook 职责隔离, 性价比更优. 源 NotebookLM v2 架构. **P3.9 (c) 实测新增**: 补丁文案应**明示** "Public 档位 ≠ 广播到公开画廊 — NotebookLM 公开画廊是 curated Featured list, 非 auto-listed; Public 档实质语义 = '允许任何持链接者无需登录访问' 而非 '被动曝光给搜索的人'. 此语义比 ChatGPT GPT Store 'Public=全网广播' **保守**, 隐私友好性更高, 适合小圈内部分享 + 定向外发场景". 这是 single-notebook 多 scope 架构的**实用优势**.

---

## §5 Rule E 跨平台 cross-check — 写进全局 CLAUDE.md 候选

**草案 (写进 `~/.claude/CLAUDE.md` `<personal_operating_principles>`)**:

```markdown
- **跨平台 cross-check 强制 (规则 E)**: Tier 2/3 项目若涉及多平台/多引擎并行部署, ≥ 3 平台同期 ground truth 对比作 multi-reviewer baseline 的事实等价. 单平台 self-score + 同 session reviewer 无法拦截 "锚缺 / KB 覆盖缺 / 训练数据 bias" 这三类系统性缺陷. 4 平台跑完同一 smoke 题组, 不一致的必有因; 同一幻觉跨平台重现 = 数据问题 (KB 错); 同一幻觉单平台发生 3 平台不发 = 锚缺 / 训练 bias. Rule E = Rule D 的外部化版本.
```

**支持证据 (本 Phase 5)**:
- R1 Gemini AHP 0/3 FAIL + 另 3 平台 12/12 PASS+ → 无争议定位 "Gemini anti-hallucination 锚缺"
- R2 Gemini v6 CO-5 单点修 → 0/3 → 3/3 PASS+ (因果闭环)
- R1 Q10 SUPPTS 判据前提错, NotebookLM in-KB-only 主动纠错反衬判据 bug — 无 NotebookLM 会以 4 平台全 PASS 错判

**应用门槛**: Tier 2 (5-15 step, 半天-1 天) 以上. Tier 1 小任务不套.

**与 Rule D 关系**: Rule D = 同项目内多 subagent_type 独立审; Rule E = 跨平台多引擎独立验证. 两者正交, 叠加使用效果最强.

---

## §6 下一步 (post sign-off)

### 6.1 立即 (P3.9 完成即触发)

1. P3.9 drill 结果回灌本 retro §1.6 / §2.5 / §3.7 / §4.15
2. 本 retro DRAFT → FINAL, 过 Rule D 独立复核 (28th subagent_type 候选: `oh-my-claudecode:critic` 或 `superpowers:code-reviewer`)
3. 用户 ack 进 Phase 5 COMPLETE

### 6.2 近期 (Phase 5 后 1-2 周)

4. Rule E 写入 `~/.claude/CLAUDE.md` `<personal_operating_principles>` (§5 草案)
5. `_template/` 11a-15 补丁 PR (合入 AI 平台部署范本)
6. `ROADMAP.md` 4 平台状态 **待开始** → **已完成** + capacity / score / A/B 数据
7. `ai_platforms/README.md` 总览表格更新
8. `CLAUDE.md` Key Paths 回填新入口 (本 retro + Rule E 补丁)

### 6.3 可延后 (optional / nice-to-have)

9. Gemini v7 迭代 (Q1 GFGENE + Q13 ARMCD-null 双 HIGH carry-over) — **draft ready**: `gemini_gems/dev/v7_draft/system_prompt_v7.md` 21,071 chars (wc -m, UTF-8 chars) / 28,107 bytes (wc -c), 待 reviewer + apply
10. ChatGPT v2.1 → v2.2 Q1 拼写 MINOR fix (GFINHERT 写全禁 GFINHERTG) — **draft ready**: `chatgpt_gpt/dev/v2.2_draft/system_prompt_v2.2.md` 6,654 chars (wc -m, UTF-8 chars) / 8,777 bytes (wc -c), 待 reviewer + apply
11. Q4-Q10 v5c 全量回归 (G5-4 假设未实测 verification task) — **plan ready**: `V5C_REGRESSION_PLAN.md` v0.1, 推荐 combined with #9+#10 apply 后跑
12. NotebookLM P3.5/P3.6/P3.7 Studio 三件套 post-project 精雕 (v2.1 ICEBOX)

---

## §7 Rule A/B/C/D/E 合规自查

- **Rule A (语义抽检)**: **部分满足** — 本 retro trace 了 5 上游产物作为 evidence base (R1/R2/NotebookLM/Claude 独立 retro + SYNC_BOARD 变更日志 + P3.9 drill evidence), 这是 **meta-evidence trace**, 非 Rule A 严格意义的"N 独立样本抽检". 严格 Rule A N≥5 独立样本审挪 G5-3 #4 post-project optional (28th reviewer F3 finding, 撤回原"✓"自证, 承认 category error).
- **Rule B (失败归档)**: R1 Gemini AHP FAIL / R2 Q1 GFGENE regression / v1 3-notebook 伪约束 pivot / Phase 3 Node 2 attempt_1 双边 FAIL — 全归档. ✓
- **Rule C (Retro 强制)**: 本文即 Phase 5 跨 4 平台 retro, 三段 (§1 保留 R5-1-6 / §2 缺口 G5-1-5 / §3 决策 D5-1-7). ✓ [v1.0 FINAL candidate 2026-04-23 PM, P3.9 回灌完成 + 28th reviewer 5 condition 修完, 等 Daisy ack 升 FINAL]
- **Rule D (审阅隔离)**: 本 retro 起草由主 session 独立于 R1/R2 retro + Claude retro. 28th slot 独立 reviewer `oh-my-claudecode:critic` 已完成独审 (CONDITIONAL_PASS 82, 5 fix conditions applied), evidence `ai_platforms/phase5_28th_reviewer.md`. 详见 Appendix A Rule D chain roster.
- **Rule E (跨平台 cross-check)**: 本 retro 核心**证据**是 4 平台 R1 ground truth 矩阵 (`SMOKE_V4.md §3` 17×4 verdict 矩阵); Rule E 候选 (§5) 是该证据的**规则化产物**, 待 Daisy ack 升 `~/.claude/CLAUDE.md`. **不是**说 Rule E 本身 = 证据 (避免 F9 循环论证).

---

## Appendix A — Rule D Chain Roster (28-slot post-hoc reconstruction, F2 fix)

**来源**: 本花名册是 post-hoc 从 3 平台 `_progress.json` (`rule_d_chain_subagent_types` / `cumulative_*` 字段) + `SYNC_BOARD.md` 变更日志 (2026-04-20 → 2026-04-23) + R1/R2 retros 中 reviewer 段 **重构**. 原始权威记录在各 `_progress.json` + SYNC_BOARD trace, 非本 retro 独创.

**Convention**: 一 slot = 一次独立 reviewer 评审 instance (不是 unique subagent_type 数). 部分 subagent_type 在不同 phase/lane 被重用作独立 reviewer (每次是新 context, 不违 Rule D "同一 context 自审 = 无审" 原则).

**Phase 0-2 (NotebookLM 独立 lane + ChatGPT+Gemini 锁步 lane 混算, 9 slots)**:
- #1 `general-purpose` (NotebookLM Phase 1 writer1 lane)
- #2 `oh-my-claudecode:verifier` (NotebookLM Phase 1 reviewer1)
- #3 `oh-my-claudecode:executor` (NotebookLM Phase 1 writer2)
- #4 `oh-my-claudecode:critic` (NotebookLM Phase 1 reviewer2; 本 Phase 5 28th slot 同 type 不同 instance)
- #5 `oh-my-claudecode:planner` (NotebookLM Phase 2 v1)
- #6 `oh-my-claudecode:analyst` (NotebookLM Phase 2 v1)
- #7 `feature-dev:code-architect` (NotebookLM Phase 2 v1)
- #8 `pr-review-toolkit:code-reviewer` (NotebookLM Phase 2 v1; 后续 Phase 4 N5.2 Gemini lane 重用)
- #9 `oh-my-claudecode:architect` (NotebookLM Phase 2 v2 审)

**Phase 3 (ChatGPT+Gemini 锁步 lane, 7 new slots + reuse, SYNC_BOARD L189-200)**:
- #10 `oh-my-claudecode:debugger` (Phase 3 N1 v1.2 delta)
- #11 `feature-dev:code-reviewer` (Phase 3 N2 v1.3c audit)
- #12 `pr-review-toolkit:comment-analyzer` (Phase 3 N3a Gemini)
- #13 `pr-review-toolkit:pr-test-analyzer` (Phase 3 N3b ChatGPT)
- #14 `oh-my-claudecode:scientist` (Phase 3 N3b Gemini; 后续 NotebookLM P3.4.5 + N5.3 reuse)
- #15 `superpowers:code-reviewer` (Phase 3 N4 writer review)
- #16 `oh-my-claudecode:tracer` (Phase 3 N4 smoke v2 ChatGPT)
- #17 `oh-my-claudecode:test-engineer` (Phase 3 N4 smoke v2 Gemini)

**Phase 4 (ChatGPT+Gemini 锁步 + NotebookLM async, 6 new slots + reuse)**:
- #18 `pr-review-toolkit:silent-failure-hunter` (Phase 4 N5.1 ChatGPT)
- #19 `oh-my-claudecode:security-reviewer` (Phase 4 N5.1 Gemini)
- #20 `pr-review-toolkit:type-design-analyzer` (Phase 4 N5.3 ChatGPT)
- #21 `feature-dev:code-architect` reuse (Phase 4 N5.3 Gemini, same type as #7 different evidence)
- #22 `oh-my-claudecode:code-reviewer` (Phase 4 N5.4 ChatGPT AB #24 reviewer)
- #23 `feature-dev:code-explorer` (Phase 4 N5.4 Gemini AB #25 reviewer)
- (NotebookLM async lane:) #24 `oh-my-claudecode:document-specialist` (smoke v3→v4 audit 11th slot) + #25 `feature-dev:code-reviewer` reuse (P3.8 reviewer 12th slot, same type as #11 different evidence)

**Phase 5 / R2-line (Gemini 单平台 iteration + Phase 5 retro, 3 slots)**:
- #26 `pr-review-toolkit:code-reviewer` reuse (R2 13th R2-line slot for v6 adequacy, same type as #8)
- #27 `oh-my-claudecode:verifier` reuse (R2 14th R2-line slot for R2 scoring, same type as #2)
- #28 `oh-my-claudecode:critic` reuse (**本 retro 28th slot**, same type as #4 — 不同 context/evidence, CONDITIONAL_PASS 82, 5 fix conditions applied 2026-04-23 PM)

**Unique subagent_type count**: ~21 distinct types across 28 slots (部分类型被重用作不同 evidence 的独立 reviewer).

**Caveat**: 本 roster 是 post-hoc reconstruction, 若与 SYNC_BOARD 变更日志 / `_progress.json` cumulative 字段有 off-by-1 偏差, 以 trace 源为准. 此 appendix 是 reviewer F2 "27-chain unfalsifiable talisman" finding 的修复 — 把"27 种"从口头数字升级为可核对花名册.

---

## §8 本 retro DRAFT 版本管理

| 版本 | 日期 | 状态 | 触发 |
|---|---|---|---|
| v0.1 | 2026-04-23 AM | DRAFT 骨架 | R2 Gemini 闭合 commit `680d99b` 之后 |
| v1.0 candidate | 2026-04-23 PM | 🟢 FINAL candidate (P3.9 回灌完成) | P3.9 drill PASS + evidence `share_level_toggle_drill.md` v1.0 + 4 TBD marker 全灌 |
| **v1.0 post-28th-reviewer** | **2026-04-23 PM** | 🟢 **post-fix, ack-ready** | 28th slot `oh-my-claudecode:critic` CONDITIONAL_PASS 82 + 5 blocking fix applied (F1 NotebookLM 详细 / F2 Appendix A roster / F3 Rule A 部分满足 / F6+F7 char 双单位 / F9 Rule E 循环论证修) + F4/F5/F8 deferred non-blocking. Evidence `ai_platforms/phase5_28th_reviewer.md` |
| v1.0 FINAL | [TBD, Daisy ack 时] | ✅ FINAL | Daisy ack → Phase 6.5 全 lifecycle sign-off 🎉 |

---

*DRAFT v0.1 2026-04-23 AM. 骨架先于 P3.9 drill 写就, 是为了让 P3.9 跑完即可灌入, 不卡在起草. 升 FINAL 前不要对外引用. 起草 session: R2 闭合 commit 同一 session 增量产出.*
