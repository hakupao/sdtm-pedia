# Smoke v2.1 Results — Gemini Gems SDTM Expert (Node 5.2 N5.1-post)

- **Date**: 2026-04-21
- **模式**: Pro (全 10 题)
- **Gem URL**: https://gemini.google.com/u/1/gem/3b572e310813
- **Phase**: Phase 4 Node 5.2 — 验证 N5.1 fix + §1.6/§12.4/§22.7 硬锚点 + v2.1 判据回归
- **上游**: CHECKPOINT_N5_2_HANDOFF.md (Step 1-2 用户完成: Custom Instructions v4 + 51K-token 04 knowledge 上传)
- **Upstream 智能处理**:
  - ✅ Step 3 (4 verify 题) 全 PASS — N5.1 §1.6/§12.4/§22.7 硬锚点已生效
  - ✅ Step 4 (smoke v2.1 10 题) 本报告

## 总体得分

| 指标 | 数值 | 说明 |
|------|------|------|
| **PASS 题** | **9 / 10** | Q1 / Q2 / Q4 / Q5 / Q6 / Q7 / Q8 / Q9 / Q10 |
| **FAIL 题** | 1 / 10 | Q3 (LBNRIND "H"/"L"/"N" 单字符 — CT C78736 全写失败) |
| **PARTIAL 题** | 0 / 10 | — |
| **总分** | **9.0 / 10.0** | 对齐 Node 3b smoke v2.0 同等分数 (9/10) |
| **Exit Gate** | ≥ 8/10 **达标** | 进 Phase 4 后续回归 + 完整 A/B |

## 逐题汇总

| # | 题目 | URL | Verdict | 核心判据命中 | 小错 |
|---|------|-----|:-------:|--------------|------|
| Q1 | 合并用药 CM 拆分 | [c15d655937375ff8](https://gemini.google.com/u/1/gem/3b572e310813/c15d655937375ff8) | ✅ PASS | 2 条 + STUDYID/DOMAIN/USUBJID/CMSEQ/CMTRT Core=Req 全中 | — |
| Q2 | AE 升 SAE 住院子变量 | [ffa1a644b61d8d99](https://gemini.google.com/u/1/gem/3b572e310813/ffa1a644b61d8d99) | ✅ PASS | 7 子变量全对 + CO-1 AESER=Exp 边界主动提示 | — |
| **Q3** | **HbA1c LB LBNRIND 三档** | [cb5b90d24326a18d](https://gemini.google.com/u/1/gem/3b572e310813/cb5b90d24326a18d) | ❌ **FAIL** | LBNRIND 答 "H"/"L"/"N" 单字符 — **非 CDISC CT C78736 官方全写** | 根源: KB 示例片段与 CT 冲突 (LB/spec.md L264 + terminology 4 处) |
| Q4 | AESEV vs CTCAE Grade | [2b0e45cb98b6a22e](https://gemini.google.com/u/1/gem/3b572e310813/2b0e45cb98b6a22e) | ✅ PASS | 三档 MILD/MODERATE/SEVERE + Grade 1-5 映射 + Grade 5 AESDTH/AEOUT/AESER 联动 | — |
| Q5 | PK LLOQ 处理 | [05e0cced60365fa5](https://gemini.google.com/u/1/gem/3b572e310813/05e0cced60365fa5) | ✅ PASS | PCSTRESN=Null 硬锚 + PCLLOQ + 三拒填 0 理由 (§4.1.5.1) | — |
| Q6 | ARM 中期换组 | [777b9a699fe1ac6e](https://gemini.google.com/u/1/gem/3b572e310813/777b9a699fe1ac6e) | ✅ PASS (primary) | DM 域锚定 ✅ (N5.1 §1.6 生效) + Planned/Actual 区分 + ITT 原则 | Core 属性小错: ACTARMCD/ACTARM 应 Exp, Gemini 答 Req (与 verify Q_verify_2 行为一致); CO-2 误引 C66735 (实为 Route of Admin) |
| Q7 | MH+CM 双录 Ongoing | [c69e293c5d69a151](https://gemini.google.com/u/1/gem/3b572e310813/c69e293c5d69a151) | ✅ PASS | MH+CM 双录 + MHENRF 学派派偏好 ✅ + CMSTRTPT=BEFORE/CMENRTPT=ONGOING + Ongoing 三原则 | MH 记录行笔误 "AETERM" 应为 MHTERM (上下文一致) |
| Q8 | ISO 8601 + --STDY | [61db292d7493563f](https://gemini.google.com/u/1/gem/3b572e310813/61db292d7493563f) | ✅ PASS | AESTDTC 到分精度 + 禁补 00:00 + --STDY 两段公式 + **无 Day 0** 硬锚 | Gemini 自发生成 "Show me the visualization" 交互 (不影响文本判据) |
| Q9 | SUPPAE 边界 | [17b69b342445e583](https://gemini.google.com/u/1/gem/3b572e310813/17b69b342445e583) | ✅ PASS | SUPPAE 非标存储本质 + AESI 典型例子 + QNAM/QLABEL/QVAL 三字段 + 8/40 字符限 | — |
| Q10 | RELREC vs SUPPAE | [35cc6e1d775de61c](https://gemini.google.com/u/1/gem/3b572e310813/35cc6e1d775de61c) | ✅ PASS | 选 RELREC + 跨域记录关系本质 + SUPP-- 差异对比 + IDVAR/IDVARVAL/RELID 绑定 | 示例表漏列 RDOMAIN 字段 (写了 DOMAIN=RELREC 但未单列 RDOMAIN=AE/CM) |

## 跨题行为模式总结

### N5.1 §1.6 / §12.4 / §22.7 硬锚点生效验证

| 硬锚点 | 相关题 | Verify (Step 3) | Smoke (Step 4) | 状态 |
|--------|--------|:----:|:----:|:----:|
| §1.6 ACTARMCD 锁 DM 域 (非 ADaM TRTP) | Q_verify_2 + Q6 | ✅ PASS | ✅ PASS (Q6) | **稳定生效** |
| §12.4 Disease Milestones (DM) vs Special Purpose (SM) 三角 | Q_verify_3 | ✅ PASS | — (非 smoke 题) | **稳定生效** |
| §22.7 UR Label | Q_verify_4 | ✅ PASS | — (非 smoke 题) | **稳定生效** |

### CO-1 边界主动提示

- Q2 (AESER=Exp 非 Req) — ✅ 主动提示触发
- Q4 (AESEV=Perm, 非 Req) — ✅ 主动标注 Perm

### CO-2 NCI EVS 外导行为

- Q3 (LBNRIND): C78736 引用正确但 inline "H/N/L" 短码 — **structural 冲突根源**
- Q6 (ARM): 引用 C66735 但该 code 实为 Route of Administration (误引)
- Q7 (Ongoing/Before): 引用 C25496 (Relative Timing CT, 方向正确)
- Q9 / Q10: 无需 CO-2, 结构化答案

### CO-3 源路径引用

- **10/10 题** 提供 CO-3 源路径 (knowledge_base/... §...) — **合规**

## Q3 FAIL 归因 (与 Node 4 smoke v2.0 一致)

1. **KB 历史示例**: `LB/spec.md` L264 等 4 处用 "H"/"L"/"N" 短码 — system_prompt v4 CO-2 子条款"KB Examples 里字面出现的 term 允许 inline"设计允许
2. **CT 权威值**: CDISC CT C78736 官方 submission values = **ABNORMAL / HIGH / LOW / NORMAL** 全写 — 无 "H/N/L"
3. **v2.1 判据**: 以 CT C78736 官方为准, 单字符短码不合规
4. **修复路径** (Phase 4 内决):
   - (a) KB LB 示例片段统一改 HIGH/LOW/NORMAL
   - (b) system_prompt CO-2 子条款加 "LBNRIND 硬锚点必须全写"

## N5.1 vs N5.2 对比 (Node 4 → Node 5.2 行为迁移)

| 题 | Node 4 (v2.0 判据) | Node 5.2 (v2.1 判据) | 变化 |
|---|:---:|:---:|---|
| Q1 | PASS | PASS | — |
| Q2 | PASS | PASS | — |
| Q3 | FAIL (CO-2 拒答) | FAIL (inline H/N/L) | **行为变迁** (v2.1 下仍 FAIL) |
| Q4 | PASS | PASS | — |
| Q5 | PASS | PASS | — |
| Q6 | ❌ FAIL (答 ADaM TRTP) | ✅ **PASS** (锁 DM 域) | **N5.1 §1.6 修复 LANDED** |
| Q7 | PASS | PASS | — |
| Q8 | PASS | PASS | — |
| Q9 | PASS | PASS | — |
| Q10 | PASS | PASS | — |
| **总** | 8/10 | **9/10** | **+1 题 (Q6)** |

## 结构性小错清单 (Phase 4 carry-over)

| 小错 | 题 | 性质 | 建议 |
|------|---|------|------|
| ACTARMCD/ACTARM Core 答 Req (应 Exp) | Q6 | system_prompt 未硬锚 Core | N5.3: system_prompt v5 加 ACTARMCD/ACTARM Core=Exp 硬锚点 |
| CO-2 误引 C66735 (Route of Admin 非 ARM) | Q6 | system_prompt NCI code 误引 | N5.3: system_prompt 改 ARM/ACTARM 不引特定 NCI code |
| LBNRIND inline "H/N/L" vs CT C78736 全写 | Q3 | KB 示例片段与 CT 冲突 | N5.3: (a) KB 片段改全写 或 (b) system_prompt CO-2 硬锚 LBNRIND=全写 |
| MHTERM 误写 "AETERM" | Q7 | Gemini 生成笔误 | 不需修 (上下文一致, 结构判据 PASS) |
| RELREC 示例漏列 RDOMAIN 字段 | Q10 | Gemini 结构细节疏漏 | 不需修 (主判据 PASS, 可考虑 KB RELREC examples 强化) |

## Exit 评估

- **Gate 达标**: ≥ 8/10 PASS → **进 Phase 4 后续回归 + 完整 A/B**
- **carry-over Q3**: 结构性 CT 冲突, 非语义拒答, 进 N5.3 system_prompt/KB 统一化修复
- **N5.1 效果确认**: §1.6 硬锚点 LANDED (Q6 从 FAIL → PASS), 整体 smoke 得分 +1 (8→9).

## 跨平台对比 (占位, 待 ChatGPT Gemini 对齐 Node 5.2 后填表)

| 题 | ChatGPT batch 2 | Gemini N5.2 | 差异分析 |
|---|:---:|:---:|---|
| Q1-Q10 | (待 ChatGPT Node 5.2 完成) | 9/10 | — |

## 下一步 (Step 6 回报)

1. 主 session 读本 results 文件 + 10 个 Q*_answer.md
2. 对照 SYNC_BOARD Phase 4 Node 5.2 gate
3. 判定是否进 Node 5.3 (system_prompt v5 修 Q3 结构冲突 + Q6 Core 硬锚)
4. Rule D 独立 subagent_type reviewer (新 subagent_type, 与历次不重复)

---

*smoke v2.1 Node 5.2 结果落档完成. 主 session 可直接基于本文件决策 Node 5.3 优先级.*
