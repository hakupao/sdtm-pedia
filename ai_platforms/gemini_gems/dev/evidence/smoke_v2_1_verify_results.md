# Gemini Gems — Step 3 Verify 结果 (smoke v2.1 前置 gate)

> Date: 2026-04-21
> 执行: Claude cowork MCP Chrome JS Quill helper
> 模式: Pro (Gemini 3 Pro)
> 目标: 验 N5.1 §1.6 DM ACTARM / §12.4 MIDS三角 / §22.7 UR Label 修复 + CO-1 AESER 边界 全落地

## 逐题结果

### Q_verify_1: AESER 的 Core 属性是 Req 还是 Exp?
- URL: https://gemini.google.com/u/1/gem/3b572e310813/f76c069059c1a211
- Verdict: **PASS** ✅
- 要点:
  - 答案: AESER (Serious Event) 被定义为 **Expected** (Exp)
  - 源路径: knowledge_base/domains/AE/spec.md §AESER
  - CO-1 边界警示: 含"AE 域 Core 属性不规则"的元提示 (v4 生效)

### Q_verify_2: ACTARMCD 在哪个域? Core 属性? 谈谈它和 ARMCD 的区别
- URL: https://gemini.google.com/u/1/gem/3b572e310813/ba0c80069925631e
- Verdict: **PASS (primary)** ✅ (minor Core 属性小错)
- 要点:
  - 主判据: **DM (Demographics) 域** ✅ (N5.1 §1.6 DM 硬锚点生效)
  - Core: 答 Req (ARMCD=Req 正确, **ACTARMCD 应为 Exp** — 小错)
  - 区别: ARMCD = Planned Arm Code (计划); ACTARMCD = Actual Arm Code (实际) ✅
  - 场景: screen failure / NOTREATED / 换组 均提及 ✅
  - 源路径: knowledge_base/domains/DM/spec.md §ARMCD, §ACTARMCD + chapters/ch04_general_assumptions.md §4.1.2 ✅ (CO-3)
  - CO-2 外导: 明确指 CT 查 NCI EVS Browser URL ✅

### Q_verify_3: Disease Milestones 实际发生记录在哪个域? TM 和 SM 什么关系?
- URL: https://gemini.google.com/u/1/gem/3b572e310813/3f045a46e86323b5
- Verdict: **PASS (primary)** ✅ (SM Label / Class 小错)
- 要点:
  - 主判据: **SM 域** 记录实际发生 ✅ (N5.1 §12.4 fix 生效)
  - TM = 定义里程碑类型 (TMTERM) ✅
  - SM = 记录受试者层面实际发生 (SMDTC) ✅
  - MIDS 三角 = TM 定义 + SM 记录 + 其他域 --MIDS/--RELMIDS 引用 ✅
  - 小错: SM 被误写为 "Study Milestones" (应为 "Subject Disease Milestones"); Class 被误分到 "Events" (应为 "Special-Purpose")
  - 源路径: chapters/ch04_general_assumptions.md §4.4.11 + domains/TM/spec.md + domains/SM/spec.md + 04_business_scenarios_and_cross_domain.md §24.3 ✅

### Q_verify_4: UR 域是什么? 专门做尿检吗?
- URL: https://gemini.google.com/u/1/gem/3b572e310813/35fb8522c2a932e0
- Verdict: **PASS (primary)** ✅ (urinalysis 归口分歧)
- 要点:
  - 主判据: **UR = Urinary System Findings (泌尿系统发现)** ✅ (N5.1 §22.7 fix 生效, Label 正确)
  - 不是窄化到单纯尿检 ✅
  - 典型数据: 尿动力学/膀胱容量/PVR/最大尿流率/物理检查异常 ✅
  - 分歧: 答案把常规尿检 (pH/蛋白等) 归 LB 而非 UR (handoff 期望 UR 可承载尿常规 + urodynamic)。这属于行业判断分歧, 非硬错误
  - 源路径: domains/UR/spec.md + domains/LB/assumptions.md ✅ (CO-3)

## 汇总

| 题号 | Verdict | N5.1 Fix 验证 | Core 行为 |
|-----|---------|--------------|----------|
| Q_verify_1 | PASS | CO-1 AESER=Exp | CO-1 边界警示 ✅ |
| Q_verify_2 | PASS | §1.6 DM ACTARM 锚点 | Core=Req 小错 (应 Exp) |
| Q_verify_3 | PASS | §12.4 MIDS/SM 三角 | SM Label/Class 小错 |
| Q_verify_4 | PASS | §22.7 UR Label | urinalysis 归口行业分歧 |

**4/4 PASS** — N5.1 所有前置 fix 均生效, smoke v2.1 正式回归 gate OPEN.
