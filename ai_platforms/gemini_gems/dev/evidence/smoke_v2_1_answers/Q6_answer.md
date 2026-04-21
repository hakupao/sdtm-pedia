# Q6 Answer — ARM/ARMCD/ACTARM/ACTARMCD 中期换组

- URL: https://gemini.google.com/u/1/gem/3b572e310813/777b9a699fe1ac6e
- 模式: Pro
- Date: 2026-04-21

## 答案摘要

### 1. 变量定义 (DM 域)

| 变量 | 标签 | Core | 含义 |
|------|------|------|------|
| ARMCD | Planned Arm Code | **Req (Gemini 答)** | 计划分组代码 (短名称) |
| ARM | Description of Planned Arm | **Req (Gemini 答)** | 计划分组名称 (完整描述) |
| ACTARMCD | Actual Arm Code | **Req (Gemini 答)** | 实际分组代码 |
| ACTARM | Description of Actual Arm | **Req (Gemini 答)** | 实际分组名称 |

### 2. 本场景取值

- **ARM / ARMCD = Arm A** (意向治疗 ITT, 不因中途变动改变)
- **ACTARM / ACTARMCD = 实际路径** (通常 ACTARMCD="ARMB" 或 "Arm A then Arm B" 或 "Multiple Arms", 按 sponsor 定义)

### 3. 源路径 (CO-3)

- knowledge_base/domains/DM/spec.md §ARM, §ARMCD, §ACTARM, §ACTARMCD
- knowledge_base/chapters/ch04_general_assumptions.md §4.1.2 (Planned vs Actual)

### 4. CO-2 外导

- 提示 "本 Gem 不 inline 具体 Term 值, 请查 NCI EVS Browser C66735"
- 注: C66735 实际是 Route of Administration (不是 ARM 的 CT); ARM/ACTARM 的 CT 是方案 study-specific, 不对应某 NCI code — **此处 C66735 为误引** (minor)

## v2.1 判据对齐

| PASS 判据 | 结果 |
|----------|------|
| ARM/ARMCD/ACTARM/ACTARMCD **全在 SDTM DM 域** (非 ADaM 非 EX) | ✅ (N5.1 §1.6 硬锚点生效) |
| ARM = Planned, ACTARM = Actual 区分 | ✅ 明确 |
| 本场景 ARM/ARMCD = Arm A, ACTARM = Arm B 或组合 | ✅ 解释清晰 (ITT 原则 + sponsor 定义) |
| ITT 原则引用 | ✅ 明确引"意向治疗" |

| FAIL 判据 | 结果 |
|----------|------|
| 错层 (答 ADaM TRTP/TRTA) | ✅ 未触 (N5.1 §1.6 fix 生效, 锁定 DM 域) |
| 答 EX 域 | ✅ 未触 |
| Core 属性小错 (ACTARMCD/ACTARM 应为 **Exp**, Gemini 答 Req) | ❌ **小错** |
| Core 属性小错 (ARM 应为 **Req**; ARMCD Req) | ⚠️ ARM/ARMCD Req 正确 |

## Core 属性细节

按 SDTMIG v3.4 DM spec 权威:
- ARMCD: **Req**
- ARM: **Req**
- ACTARMCD: **Exp**
- ACTARM: **Exp**

Gemini 答四个全 Req, 其中 ACTARMCD/ACTARM 应为 Exp — 与 Q_verify_2 行为一致 (小错但不影响主判据 DM 域锚点 PASS).

## Verdict: **PASS (primary)** — Core 属性小错

主判据全通过: DM 域锚点 ✅ / Planned vs Actual 区分 ✅ / 本场景取值 ✅ / ITT 原则 ✅ / 源路径 CO-3 ✅.

小错: ACTARMCD/ACTARM Core 应为 Exp, Gemini 答 Req. 该错误与 verify Q_verify_2 一致, 属 N5.1 未修复残留 (system_prompt v4 尚未硬锚 ACTARMCD Core=Exp).

CO-2 外导的 C66735 为误引 Code (该 code 实为 Route of Administration, 非 ARM CT) — 建议 N5.3 修 system_prompt 引用.
