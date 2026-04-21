# Phase 4 Node 5.2 — Gemini 用户操作 Handoff

> **Node**: Phase 4 N5.2 (smoke v2.1 重新上传 + 回归)
> **前置 commit**: `1cff7fe` (Phase 4 N5.1 前置修复 PASS)
> **执行者**: 用户 + claude cowork MCP 代理 (execCommand insertText + InputEvent + wait 2s 绕 Quill ngModel race)
> **估时**: 更新 Custom Instructions ~3 min + 删老 + 上新 04 ~3 min + 验证 ~5 min + smoke 10 题 ~30-45 min (Pro mode 每次 navigate 需手动重选)
> **下游 gate**: 回报 smoke v2.1 score → 主 session 派 N5.2 reviewer 第 18 种 subagent_type + 决策进 N5.3

---

## Step 1: 更新 Custom Instructions

1. 登录 https://gemini.google.com/u/1/gem/3b572e310813 (bojiang.zhang.0904@gmail.com, Google AI Pro)
2. "Edit Gem" (或 ⚙ Settings) → Instructions 框**整段清空**, 粘贴 `ai_platforms/gemini_gems/current/system_prompt.md` **全文** (v4)
3. 核查: 字符数 ~7,093 chars (UI 显示按 chars 计, 含中文). Gem budget 8000 chars, 当前 buffer 907 chars (11.3%)
4. 核查 header 第一行含 "**v4 C 方案 + CO-2 边界显式化**"
5. 保存

## Step 2: Knowledge 文件 (**必须替换 04**)

Gemini 侧 N5.1 改了 04 内容 (30K→51K, 含 §1.6 DM ACTARM 硬锚点 + §12-§24 13 新段 + MED fix). Knowledge Upload 不能 in-place 编辑, 必须删老上新:

### 2a. 删老 04
- 进入 Gem 的 "Knowledge" 管理页面
- 找到 `04_business_scenarios_and_cross_domain.md` (前版, ~30K tokens)
- 删除 (Delete / Remove)

### 2b. 上新 04
- 上传 `ai_platforms/gemini_gems/current/uploads/04_business_scenarios_and_cross_domain.md` (新版, 51,358+ tokens, 含 N5.1 MED fix)
- 等待上传完成 + indexing (~30-60 sec)

### 2c. 其他 3 knowledge 不变
- `01_navigation_and_quick_reference.md` (124,515 tokens) — 保留
- `02_domains_spec_and_assumptions.md` (240,453 tokens) — 保留
- `03_domains_examples.md` (220,657 tokens) — 保留
- 总 4 knowledge 合计 **637,308 tokens / 1M window 63.7% 占用 (buffer 262K 到 900K WARN 阈)**

## Step 3: 验证 Step 1+2 生效

新开对话问 4 题 (验 N5.1 MED fix 全落地):

### Q_verify_1: "AESER 的 Core 属性是 Req 还是 Exp?"
- **期望**: Exp (Expected), 引 AE/spec.md L254 或 §AESER
- **反例 (回归)**: Req (LLM 邻变量污染幻觉, Node 3b 原错, N4 CO-1 已修)

### Q_verify_2: "ACTARMCD 在哪个域? Core 属性? 谈谈它和 ARMCD 的区别"
- **期望**: SDTM DM 域 (非 ADaM 非 EX), Order=26 Core=Exp Permissible slot, ACTARM Order=27 Core=Exp; ACTARMCD = 实际分组, ARMCD = protocol-planned 分组
- **反例 (Q6 错层 smoke v2.0)**: 答"ADaM TRTP/TRTA" 或 "EX 域" (N5.1 §1.6 硬锚点 fix 后应该改正)

### Q_verify_3: "Disease Milestones 实际发生记录在哪个域? TM 和 SM 什么关系?"
- **期望**: SM 域 (Subject Disease Milestones, Special-Purpose class, 1 record per milestone per subject); TM 定义 milestone 类型 + SM 记录每 subject 的实际发生 + 其他 general obs 域用 `--MIDS` 变量引 SM 的实例名 → MIDS 三角关系
- **反例 (N5.1 MED2 已修前 writer 漏 SM)**: 只说"记录到任何 general observation class 域", 不提 SM

### Q_verify_4: "UR 域是什么? 专门做尿检吗?"
- **期望**: UR = Urinary System Findings (尿系统发现域, Findings class 非 LB), 范围比 urinalysis 广, 可承载尿常规 (pH/PROTEIN/BLOOD) + 其他泌尿发现
- **反例 (N5.1 MED1 已修前 writer 窄化)**: 答 "UR (Urinalysis) 尿检" 单一范围

4 题全 PASS → Step 1+2 生效, 进 Step 4

## Step 4: 跑 SMOKE_QUESTIONS_V2.md v2.1 (10 题)

- 打开 `ai_platforms/SMOKE_QUESTIONS_V2.md` (v2.1, Q3 判据 2026-04-21 修正版)
- 按题号顺序问 10 题, 每题**开新对话**避 context 污染
- 推荐方式: claude cowork MCP 代理 `execCommand('insertText')` + `InputEvent` dispatch + `wait 2s` + UI click (绕 Quill ngModel race, 参考 N4 smoke v2 经验; Q3/Q6 各踩一次 race)
- 严格按 v2.1 判据评分:
  - Q3 v2.1: PASS="HIGH/LOW/NORMAL" 全写 / FAIL="H"/"L"/"N" 单字符
  - Gemini Q3 可能仍 FAIL 因 CO-2 拒答设计 (KB 无原文则外导 EVS), 这不是平台缺陷是 guard 过度保守. 折衷接受 ≥9/10 strict

## Step 5: 落档

保存到: `ai_platforms/gemini_gems/dev/evidence/smoke_v2_1_results.md`

结构 (沿用 smoke_v2_results.md 格式):
```markdown
# Gemini Gems — smoke v2.1 10 题回归结果

> Date: <date>
> SMOKE_QUESTIONS_V2.md v2.1 (Q3 判据 HIGH/LOW/NORMAL 修正版)
> 前置 commit: 1cff7fe (Phase 4 N5.1 前置修复 PASS)
> 执行者: user + claude cowork MCP Chrome JS Quill helper
> 预期 score: ≥9/10 strict (Q3 CO-2 拒答可接受, Q6 ACTARM N5.1 §1.6 fix 后必 PASS)

## 逐题结果

### Q1: CM 域多条 concomitant medication 怎么合并
- 对话 URL: https://gemini.google.com/...
- 完整回答路径: dev/evidence/smoke_v2_1_answers/Q1_answer.md
- 判据对齐: ...
- Verdict: PASS / FAIL / PARTIAL
- 归因: ...

### Q2-Q10: 类似
```

另存每题完整回答到 `dev/evidence/smoke_v2_1_answers/Q{N}_answer.md`

## Step 6: 回报主 session

回报格式:
```
Gemini smoke v2.1 完成: X/10 strict PASS
- Q3: PASS (判据 v2.1 生效) / FAIL (CO-2 拒答设计, 可接受)
- Q6: ACTARM 层级 PASS (N5.1 §1.6 fix 生效) / FAIL (回归)
- Q7 (MHENRTPT vs MHENRF): 学派派 (KB §34a 偏好 MHENRF) 接受否?
- 其他: ...
- CO-1 AESER 验证: PASS / FAIL
- CO-2 NCI EVS guard 验证: PASS (外导) / FAIL
- CO-3 citation 格式: PASS (全带源路径) / PARTIAL
```

主 session 接手后: 派 N5.2 reviewer (第 18 种 subagent_type) 独立审双平台 smoke v2.1 对比 + 进 N5.3 Full A/B 矩阵.

---

## 若 smoke v2.1 未达预期 (<9/10 strict)

- **Q6 ACTARM 仍错层**: 核 04 §1.6 硬锚点段是否上传成功 (4 knowledge 文件名排序看 04 有无被 UI 过滤错位); 若确实上传但仍错, Rule B 归档 `failures/stage_n5_2_attempt_<N>.md`, system_prompt 可能需要加 "ACTARMCD 在 DM 域不在 ADaM 任何域" 硬锚点
- **MIDS/SM 仍漏**: 核 §12.4 扩段是否完整 (可 grep uploads/04 "MIDS 三角"), 若 truncate 重合并重传
- **UR 仍窄化**: 核 §22.7 (可 grep "Urinary System Findings"); 若 truncate 同上
- **CO-2 拒答覆盖超 1 题**: guard 过度保守, system_prompt 子条款需要软化 (允许 KB Examples 里字面出现的 term inline), Phase 4 N5.3 前补

## 相关路径

- SMOKE 题目: `ai_platforms/SMOKE_QUESTIONS_V2.md` (v2.1)
- 前轮 smoke (v2.0): `ai_platforms/gemini_gems/dev/evidence/smoke_v2_results.md` (8/10)
- 前轮 reviewer: `ai_platforms/gemini_gems/dev/evidence/smoke_v2_reviewer.md` (test-engineer 第 15 种 subagent_type)
- N5.1 writer 产物: `ai_platforms/gemini_gems/dev/evidence/node5_1_gemini_writer_summary.md`
- N5.1 reviewer 产物: `ai_platforms/gemini_gems/dev/evidence/phase4_n5_1_reviewer.md`
- Phase 4 总 plan: `ai_platforms/PHASE4_PLAN.md` (§3 N5.2 行, §4 P1/P2/P3/P4 消化)
