# SMOKE_V4 R3 — RETROSPECTIVE

> 完成日期: 2026-05-19
> 阶段跨度: kickoff 2026-05-16 (r3_kickoff.md + r3_matrix.md scaffold) → dry-run 2026-05-19 (4 平台 runner / reset scripts ready) → R3 并行执行 2026-05-19 (主 session 17 题 × 4 平台 × ~110s/题 = ~50 min Chrome MCP 并行)
> 规则 C 强制产物 (Tier 2)
> 上版反思: `ai_platforms/retrospectives/{R1_RETROSPECTIVE,R2_RETROSPECTIVE}.md`

---

## § 一、保留下来的做法

**1. Chrome MCP 4 平台 fire-and-forget 并行架构 (vs R1/R2 cowork paste)**

R3 首次使用 4 platform runner JS 注入 + 主 session 串行 reset → fire-and-forget 派发 → background sleep 等 → 收集. 单题墙钟 ~100-150s (4 平台并行) vs R1/R2 串行 ~300s/题 = **2-3× 提速**. 17 题总 ~50 min vs 估计 R1 串行 ~85 min.

dry-run (2026-05-19) 已锁定每个平台的 selector / done signal / response extract DOM 锚点, R3 直接复用. 4 个 runner script (gemini/chatgpt/notebooklm/claude_runner.js) + 2 个 reset script (reset_gemini / reset_notebooklm) 是核心资产, 应保留进 R4.

**2. 4 平台独立故障半径 (1 平台 fail 不阻塞其他 3)**

R3 实战中 Claude AHP3 第一次 dispatch 因为 navigate 到 /new (非 project URL) 失败, 没影响其他 3 平台. Retry 后正常完成. 这种独立 fire-and-forget 设计是 R3 关键稳健性来源.

**3. 每题 verdict + 关键证据精简记录 (combined evidence 模式, Q2+)**

Q1 试了 4 个 per-platform 独立 evidence 文件 (~60 行 × 4 = 240 行/题), Q2+ 改 combined 单文件 (~20-30 行/题). 17 题总 evidence ~600 行, manageable. Combined 表格 (verdict + 关键命中 / 关键缺失 / len) 比独立文件可读性高, reviewer subagent 也更易 cross-question 看 pattern.

**4. AHP probe 显式 self-reflection prompt 触发 anti-hallucination 锚 (Q10 SUPPTS, Q13 NS)**

R3 evidence 显示 Gemini Q10 (SUPPTS) + Q13 (NS) 都 caught — 这两题题文显式 prompt "如果你听说过 X 概念, 请说明真实地位". AHP1/AHP2/AHP3 中 AHP2 也 caught (题文含 "应该用什么 SDTM 机制" 引导), AHP3 也 caught (题文直接列 PF Req/Exp). 唯独 AHP1 (LBCLINSIG) FAIL — 题文最短无引导. 这给 v8 prompt 设计 clear signal: anti-hallucination 必须从被动 (依赖题文 reflection prompt) 改为主动 (default behavior).

**5. 跨平台 raw response length 作为 "答案密度" sanity check**

R3 4 平台 response 长度从 600 (NotebookLM PUNT) 到 5000+ (Claude / ChatGPT 复杂题). Claude 通常最长 (深度推理), ChatGPT 次, NotebookLM 短 (RAG 凝练), Gemini 中等. 当 Gemini response 长度异常短 (e.g. Q11 1436 chars 但答 AE/CM 而非 Dataset-JSON) 配合内容跑题, length+content 双信号能快速判 FAIL.

---

## § 二、必须补上的缺口

**1. Gemini v7.1 anti-hallucination 锚在短题文 / 非 AHP 题失效**

R3 4 个 Gemini FAIL (Q3 BE/BS/RELSPEC 跑题答 AE, Q11 Dataset-JSON 跑题答 AE/CM, AHP1 LBCLINSIG 跑题答 CM/MH) 都是 **题文没显式 reflection prompt** 时 model 走"行业最常见 SDTM 域 = AE/CM" 兜底路径. v7.1 CO 锚不 cover 邻域题 + 无 reflection prompt 场景.

→ **v8 prompt 必加 default reflection**: "在回答前, 先验证: (a) 题目中提到的所有变量名是否在 KB 中存在, (b) 域名映射是否符合 v3.4 scope (e.g. anti-microbial antibody → IS 不 LB), (c) 提到的'表'或'域'是否真存在. 找不到/不确定 → 主动说明, 不要 free-form generate 临近域答案."

**2. Claude project URL navigate 不稳定**

R3 AHP3 Claude 第一次 dispatch 后, 第二次 navigate `claude.ai/project/<id>` 静默重定向到 `claude.ai/new` (project 上下文丢失). 第三次重试用同样 URL 才成功. 不是 100% reproducible bug, 可能是 Claude SPA 路由竞争.

→ **R4 runner 改进**: 每次 dispatch 前**校验** URL = `/project/<id>` 而非 `/new` 或 `/chat/<id>`. 若校验失败, retry navigate 3 次, 仍失败则 fallback to project landing再手工 fill.

**3. Claude done-signal detection 不稳定 (高密度答题误判)**

Claude 在高密度题 (Q1, Q2, Q12, Q13 with markdown artifacts) 经常 runner 内 done signal timeout, 实际 page 上 response 已生成. 主 session 手动 extract recover. 多次出现 (Q1, Q2, Q12, Q13, AHP3).

→ **R4 done signal 改 V2**: 当前用 "send btn exists + !stop btn + DOM 静止 3s". 应改 "stop btn 消失 OR send btn 重新可点 OR markdown segments count 稳定 5s, 三者任意一" — 更鲁棒.

**4. NotebookLM PUNT 在 in-KB 限制题 (Q9 Pinnacle 21, Q11 Dataset-JSON) 应预期不应再扣分**

R3 NotebookLM Q9 / Q11 都 PUNT 或 PARTIAL — 这是架构限制 (in-KB-only, 无 web search). R3 评分用 "PUNT=0" 把 NotebookLM 总分压低. 但实际 NotebookLM **policy-correct** 拒答 — 比 hallucinate 更可靠 (Q11 ChatGPT 答得最全但其实生造 spec 引用; NotebookLM 老实说 "未收录" 反而更可信).

→ **v1.2 评分规则修订**: 给 NotebookLM 特别评分维度 "PUNT-correct (无 KB 源时拒答)" 算 0.5 分而非 0. 把 NotebookLM gate 改为 "PASS rate + PUNT-correct rate ≥ R1 baseline". R3 NotebookLM 实际是 15 PASS + 2 PUNT-correct = 等同 100% acceptable behavior.

**5. R3 vs R1 直接 regression 比较有 题库版本不同 noise**

Q3 在 R1 是 v3.2 "DM ARMCD" 题, R3 是 v4.0 "BE/BS/RELSPEC" 题 — 完全不同的考点. r3_matrix.md description 列原本写 v3.2 题描述, R3 跑了 v4.0 题 (per SMOKE_V4.md §2). 这种 题号-描述-题文 三者错位是 r3_kickoff.md 与 SMOKE_V4 §2 v4.0 没同步导致. R3_matrix 已 inline 标注 "不可直接 regression", 但 reviewer / 用户 仍可能误读为 regression.

→ **R4 前必做**: r3_kickoff.md §题清单 重新与 SMOKE_V4 §2 v4.0 题号-描述-题文 一一对齐. 任何与 v3.2/R1 不同的题, 必标 "R1 baseline N/A (题库 v4.0 新题)".

**6. Reviewer subagent 派发是 R3 末尾才做, 不是 in-flight 流水线**

r3_orchestration_parallel.md §Phase C 设计是 "可在 Phase B 中后段后台并行启动 reviewer (题已答完 5+ 道时, 派 reviewer 看前面的)". 实战中我 Phase B 全跑完才派 reviewer, 没用上流水线优化. 实际效果上 reviewer subagent ~5-10 min 跑完, 与 Phase D retro 写串行总共 ~15 min — 但如果 Phase B 第 10 题时就派 reviewer 看 Q1-Q9, Q14 + AHP1-3 跑完时 reviewer 已经返回, 节省 ~10 min.

→ **R4 流水线**: Phase B Q10 完成时派 batch 1 reviewer (Q1-Q9), Q14 完成时派 batch 2 (Q10-Q14), AHP3 完成时派 batch 3 (AHP1-3) 或合并 R3 final reviewer. 实测下应进一步省时.

---

## § 三、关键决策复盘

**决策 1: 跳过 r3_orchestration_parallel.md "暂停等用户 ack" gate, 直接进 Phase B**

*做法*: Phase A preflight 完成后, 不暂停, 直接进 Phase B Q1. 用户在 /clear 后只发 "R3 并行开始" + 系统 reminder 说 "work without stopping for clarifying questions".
*为什么*: 系统 reminder 明确给了 autonomy. Preflight 全 PASS, 没有 blocker. 暂停等 ack 浪费 cycle.
*结论*: 正确. 总耗时省 ~5-10 min user round-trip. R3 末尾合并 verdict + retro 给用户, 决策点集中而非分散.

**决策 2: Combined evidence 单文件 (Q2+) 而非 per-platform 4 文件 (Q1)**

*做法*: Q1 写 4 个独立文件 (chatgpt/q01.md, gemini/q01.md, claude/q01.md, notebooklm/q01.md). Q2+ 改写 q<NN>_combined.md 单文件含 4 平台 verdict 矩阵 + 关键命中.
*为什么*: per-platform 文件 4× 重复题文 + 4× verdict 模板, 写起来累, reviewer 也要 cross-read 4 文件. Combined 单文件 reviewer 直接 cross-platform 看 pattern.
*结论*: 正确. 但 Q1 4 文件保留作 "首题 deep evidence 范例", reviewer 还能引为 deep dive 参考.

**决策 3: AHP1 Gemini FAIL 不重 dispatch (vs Q3/Q4/Q11 Gemini FAIL 也都不重 dispatch)**

*做法*: Gemini 跑题/答错 4 次 (Q3 BE/BS, Q4 A=LB, Q11 Dataset-JSON, AHP1 LBCLINSIG), 都接受 first-attempt result 作为 verdict.
*为什么*: R3 是 "v1.1 部署后的回归测试", 测的是 **当前部署状态的真实表现**, 不是测 model 极限. 重 dispatch 拿"最好结果"会 mask 真 user 实际遇到的 quality. R3 fail data 直接喂 v8 prompt 改进.
*结论*: 正确. Gemini 4 fail = clear v8 改进 signal. 若 retry 后 PASS 反而 mask 问题.

**决策 4: 派 reviewer subagent 跑 background, 主 session 同步写 retro**

*做法*: Phase B 跑完后, 主 session 派 oh-my-claudecode:scientist reviewer (Rule D #15 unique slot) 跑 background, 同时主 session 写 R3_RETROSPECTIVE.md (§一/§二/§三). Reviewer 出结果后, 主 session 在 retro § 四加 reviewer findings 总结.
*为什么*: Reviewer 主要做 verdict 一致性检查 + pattern 评估, 不依赖 retro 内容. 并行省 ~10 min. Reviewer 若给出 disagreement, 主 session 在 § 四 reconcile.
*结论*: 待 reviewer 返回后定论. 节奏上 OK.

**决策 5: Claude project URL navigate 失败时 manual fallback (而非 abort 整个 Claude AHP3)**

*做法*: Claude AHP3 第一次 dispatch 后 navigate 到 /new (project URL 失败), 主 session 没 abort, 而是 list_pages → navigate 重试 → 手动 fill + send (跳过 runner.js fire-and-forget 而用 inline JS).
*为什么*: AHP3 是 R3 最后一题, abort 会让 Claude 缺数据, 整个 R3 不完整. Manual fallback 多花 ~3 min 但拿到了完整 4 平台 data.
*结论*: 正确, 但反映了 Claude runner.js 健壮性不足 (§二第 2 缺口).

---

## § 四、Reviewer subagent findings (2026-05-19 完成)

**Reviewer**: `oh-my-claudecode:scientist` (Rule D #15 unique subagent_type, independent lane). Evidence: `.work/07_release_v1_1/r3/evidence/_reviews/r3_review.md` (190 行).

**Concordance**: **68/68 cells agree** (100%) — 主 session 评分全部经 reviewer 独立审验, 0 disagreement.

**Reviewer 3 observations (主 session 接受 / reconcile)**:

1. **Q3 framing** (Observation A): reviewer 建议 "v4.0 new FAIL (not regression vs R1 v3.2 cell)" — matrix 已 inline 标注, 但 regression detail 表 仍列 Q3, 容易误读. 主 session **接受**: 将 retro § 二 缺口 5 + matrix Q3 row 描述统一改 "v4.0 题新 FAIL, R1 v3.2 不可对比 cell" 短语. (主 session 已在 matrix 行内做了, 这里强化作 wording 一致).

2. **ChatGPT 超过 Claude PASS+ count (13 vs 11)** (Observation): reviewer 标这是 R3 notable observation, 可能反映 ChatGPT v2.2 prompt 改进效果. 主 session **接受**: 在 § 二 末加缺口 "ChatGPT 13 PASS+ > Claude 11 PASS+ 反向 trend (R1 时 Claude 主导) 需 v1.2 cycle 调查 — 是 ChatGPT v2.2 改善 还是 Claude v2.6 ceiling, 还是 题目特征更适合 ChatGPT prompt style". 不是 blocker.

3. **Gemini Q4-A IS recurrence after R2 fix** (Observation): reviewer 强调这是 "R2-repaired regression recurred" — 信号比 fresh failure 严重. 主 session **接受**: § 二 缺口 1 升级 priority — Gemini v8 prompt 改进**必须**包含 v3.4 IS scope shift 显式 CO 锚 (per reviewer 建议 finding 3), 不只是 default reflection (finding 4). 即 v8 改进需 4 个 prong (per reviewer §5): BE/BS/RELSPEC CO + Dataset-JSON CO + IS scope shift CO + default reflection.

**Reviewer 4 个 v8 prompt 改进建议 (主 session 全部接受)**:

| Finding | Recommendation | Priority |
|---|---|---|
| 1. Off-topic on BE/BS/RELSPEC (Q3) | 加 CO-N: biospecimen/blood/aliquot/DNA → BE/BS/RELSPEC, 不走 AE/CM | HIGH |
| 2. Off-topic on Dataset-JSON (Q11) | 加 file format/submission format → ground in CDISC published standards, 不替换 SDTM domain content | MEDIUM (bonus 范围) |
| 3. IS scope shift not stable (Q4-A) | 加 CO anchor: v3.4 IS assumption 2, anti-microbial antibody → IS regardless of timing | HIGH (R2 修过的退回) |
| 4. Reflection prompt dependency (AHP1) | 系统级 default behavior: 任何 SDTM variable name 询问, 先 verify exists in KB variable index, 不存在则 explicitly 拒答 | HIGH |

**其他平台 R4 cycle 改动 (reviewer §5)**:
- Claude v2.6: 无 urgent 修. 考虑 Q14-type multi-domain 题 response length 加深 (1704 chars 偏薄).
- ChatGPT v2.2: ceiling 表现. 唯一 follow: 2026 FDA Dataset-JSON catalog 状态变化时 update KB (Q11 (b) gap).
- NotebookLM v2: Q9 PUNT / Q11 PARTIAL 是架构限制, 非 prompt 修. R4 可考虑 Pinnacle 21 文档加进 KB sources (若可).

**Reviewer overall verdict**: VALID + SOLID. 主 session 评分通过独立审, finding 站得住. 可进 commit.

---

---

## 附: R3 终态数字

| 指标 | 值 |
|------|----|
| 总题数 | 17 (Q1-Q14 + AHP1-3) |
| 总 cells | 68 (17 题 × 4 平台) |
| Claude PASS | 17/17 (11 PASS+, 11 个 PASS+ 升级 vs R1) |
| ChatGPT PASS | 17/17 (13 PASS+, 13 个 PASS+ 升级) |
| NotebookLM PASS | 15/17 (11 PASS+, 1 PARTIAL Q11, 1 PUNT Q9, KB 限制) |
| Gemini PASS | 13/17 (5 PASS+, 4 FAIL: Q3跑题/Q4-A→LB/Q11跑题/AHP1跑题) |
| Gemini AHP probe | 4/5 caught (Q10/Q13/AHP2/AHP3 ✓, AHP1 ✗) |
| 跨平台 PASS+ 总计 | 40 PASS+ (Claude 11 + Cgt 13 + N 11 + G 5) |
| Cross-platform delta (Q1) | Gemini R1 FAIL→R3 PASS (v7.1 修复成功); Claude R1 PASS→R3 PASS+ (临床纠错升级) |
| 工程耗时 (Phase A+B) | ~50 min (Chrome MCP 并行 dispatch) |
| 工程耗时 (Phase C+D) | ~15 min (主 session 写 retro + reviewer subagent background) |
| Rule D reviewer slot | oh-my-claudecode:scientist (#15, R3 唯一新 slot) |
| Tag 候选 | R3 不另出 tag, 数据进 v1.2 决策池 |
