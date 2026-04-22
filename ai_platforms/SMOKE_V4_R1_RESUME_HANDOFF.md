# SMOKE v4 R1 执行 — Session Handoff (2026-04-22 晚 C 轮)

> **本 session 结束时间**: 2026-04-22 晚 (Q9 后主动 ctx handoff, 用户要求 commit)
> **完成边界**: sanity 3/3 + Q1-Q9 × 4 平台 = **48 answer events** (60%)
> **剩余**: Q10-Q14 (5 题) + AHP1-3 (3 题) × 4 平台 = **32 answer events**

## 0. 本 session 增量 (C 轮) — 2026-04-22 晚 Q6-Q9

### Q6 PK --TPT 四件套 (所有平台 PASS+/PASS)
| 平台 | Verdict | 亮点 |
|---|:---:|---|
| ChatGPT | **PASS+** | 2 周期表 + 5 vars 全对 + abcd 全对 + Pre-dose=-1 编码 |
| Claude | **PASS+** | §4.4.10 锚点 + 概念模型图 + 7 种区分手段 + 完整 8 行示意表 |
| Gemini | **PASS** | 5 vars + abcd + 干净答复; R2 显式分场景答已生效 |
| NBLM | **PASS** | 6+ citations + 5 vars Role/Core/CT 完整表 |

### Q7 Partial date (出现 Gemini 关键幻觉!)
| 平台 | Verdict | 亮点 / 关键 finding |
|---|:---:|---|
| ChatGPT | **PASS+** | 3 场景 + §4.4.2 锚点 + 相对 timing 完整清单 |
| Claude | **PASS+** | 3 场景 + §4.4.2 truncation 表 + Solidus 区间 + §4.4.7 Ex3 AE Unknown + ADaM ASTDTF 机制 |
| **Gemini** | **PARTIAL (0.5)** | ❌ **(e) 层混淆幻觉**: 称 SDTM 要记 --DTF (AEDTF/CMDTF), 实际 --DTF 是 ADaM-only (ASTDTF/AENDTF) |
| NBLM | **PASS** | 3 场景 + (d)(e) 正确 + **避开 --DTF 幻觉陷阱** (7+ citations) |

### Q8 CT Extensible + MedDRA (AETERM 纠偏)
| 平台 | Verdict | 亮点 |
|---|:---:|---|
| ChatGPT | **PASS+** | (a)(b)(c)(d) 全对 + C-code 全对 + AETERM 不绑 CT 精确纠偏 prompt 措辞 |
| Claude | **PASS+** | 4+4 例子 + **4 层 CT 绑定语义总表** + Define-XML 2.1 (nci:ExtCodeID/def:IsNonStandard) + AETOXGR 替代 + C65047 Deferred 坦诚 |
| **Gemini** | **PARTIAL (0.5)** | ❌ (b) **C66767 Action Taken 错分 Ext=Yes** (实际 Non-Ext) + C66742 只 2/4 值 |
| NBLM | **PASS+** | (a)(b)(c)(d) 全对 + C66742 4 值全 + C66789 Not Done 独特 + **CDISC new-term request** 独到 insight |

### Q9 Pinnacle 21 FAIL 分类
| 平台 | Verdict | 亮点 |
|---|:---:|---|
| ChatGPT | **PASS+** | 6 类 + 三问法决策 + Must Fix/Explain 两篮 + 坦诚"非 P21 官方分组" |
| Claude | **PASS+ 最强** | 6 类 + Rule ID 示意 + **TRC 自动拒收层** + cSDRG 5 字段 + 边界声明 |
| Gemini | **PASS** | 5 类 + 修/文档化; 缺 Rule ID + 无 TRC |
| **NBLM** | **FAIL (safety-correct PUNT)** | 架构合规 PUNT + 补 SDTMIG §3.2.2 10 条 upstream; Phase 4 Scoping 稳定 vs smoke v3 |

## 1. 4 平台浏览器 tab 状态 (所有 tab 在 Chrome 9222)
- **Page 2 ChatGPT**: Q9 chat
- **Page 3 Claude**: Q9 chat (**usage 仍 75% 无变化**, 下一题可能触升)
- **Page 4 Gemini**: Q9 chat
- **Page 5 NotebookLM**: Q9 chat (未 Delete history, 继续即可)

## 2. Running score 截至 Q9 (sanity 不计)

| 平台 | 当前分 | 题数 | 阈值 | 预测 |
|---|:---:|:---:|:---:|---|
| NotebookLM | ~8/9 (Q9 FAIL capability) | 9 | ≥12/17 | 稳 (Q11/Q13 可能再 PUNT) |
| ChatGPT | ~8.75/9 | 9 | ≥12/17 | 稳 |
| Gemini | ~6/9 (2 PARTIAL: Q7/Q8) | 9 | 主 gate ≥9/13 | Q10+AHP1/2/3 需高分才稳 |
| Claude | 9/9 (全 PASS+) | 9 | ≥13/17 | 强 (担心 weekly cap) |

## 3. 剩余 8 题 prompt (从 SMOKE_V4.md §2 verbatim)

### Q10 — SUPP + SUPPTS 前提纠错 (v4 HIGH fix, **最关键**)
```
SDTM 的 SUPP-- (Supplemental Qualifiers) 家族里, 请回答:

(a) 每条 SUPP 记录有 QNAM / QLABEL / QVAL / QORIG / QEVAL 5 个关键字段. QORIG 和 QEVAL 什么时候必填, 什么时候不填? 含义分别是?
(b) SUPPQUAL 机制在 SDTMIG v3.4 下适用于哪些数据集 scope? 对于不适用 SUPPQUAL 的数据集 (比如 Trial Design 模型中的 TS "Trial Summary"), 长文本 (>200 字符) 怎么处理? 同一受试者的 AE 记录有 NSV 时用 SUPPAE; 那么对 TS 的长 parameter value, 理应用 "SUPPTS" 吗?
(c) 一条 SUPPAE 记录如何通过 RDOMAIN + IDVAR + IDVARVAL 定位到具体的 AE 父记录? USUBJID 怎么用?
(d) QVAL 长度上限是多少? 超过怎么拆?
```
**PASS+ AHP-like 判据**: (b) **SUPPQUAL scope 限 Events/Findings/Interventions + DM + SV; TS 不在 scope; "SUPPTS" 不是 v3.4 real dataset — 必显式纠错; TS 长 TSVAL 用 TSVAL1-TSVALn 内部派生 (ch04 §4.5.3.2); 沿 "SUPPTS 存在" 答 → FAIL premise hallucination**

### Q11-Q14 见原 handoff §3 (不变, verbatim prompts)
### AHP1-3 见原 handoff §3 (不变, verbatim prompts)

## 4. 执行流程模板 (每题 4 平台) — 不变

## 5. fill/readback JS 模板 — 不变 (见原 handoff §5)

## 6. 禁用事项 — 不变

## 7. 本 session 观察 (新增)

### 关键 AHP-like findings (v4 gene design 已产出数据!)
1. **Gemini Q7 --DTF 幻觉**: 成功暴露 ADaM/SDTM layer 混淆 → R2 system prompt 需加 "SDTM 无 --DTF, --DTF 是 ADaM-only" 锚点
2. **Gemini Q8 C66767 错分**: 误 Non-Ext 为 Ext → R2 需加 "C66767 Action Taken = Non-Extensible" 锚点 + C66742 NY 4 值完整
3. **NBLM Q9 架构 PUNT 稳定**: smoke v4 Q9 行为与 smoke v3 P3.8 Q9 一致 — in-KB-only safety 跨版本稳定
4. **Claude Q9 TRC 层独到**: 给出 FDA Technical Rejection Criteria 作第 3 级决策层 (ChatGPT/Gemini 均无)
5. **NBLM Q8 new-term request 独到**: 给出 CDISC new-term request workflow (其他 3 平台无)

### Claude weekly usage
- 本 session 4 题 4 次长答, usage 仍显 75%, 未升级 → 剩余 8 题可能触发 cap
- 若 Claude 后期降级/停写, 建议 R1 记录 cap 时间点 (非平台能力问题)

### Citation / F-1 / F-3 observations
- NBLM citation Q6-Q9 普遍 3-9+, 分布合理
- F-1 小表渲染漂移: 本 session 无触发 (无大表格题)
- F-3 citation T2 偏向: Q7-Q9 citation 跨 source 分布, 未见明显偏向

## 8. 下次 session 启动 prompt (简易版)

```
继续 smoke v4 R1. 读 ai_platforms/SMOKE_V4_R1_RESUME_HANDOFF.md 拿当前进度 (sanity + Q1-Q9 完成, 48/80 events).

下一题 Q10 SUPPTS 前提纠错 (**最关键 AHP-like 题**, v4 HIGH fix). 从 handoff §3 开始.

操作:
1. ToolSearch 加载 Chrome MCP 工具
2. list_pages 确认 4 tab (page 2/3/4/5 = ChatGPT/Claude/Gemini/NotebookLM)
3. 按 handoff §3 Q10 prompt 跑 4 平台
4. 重点评分 Q10 (b): 若 sponsor 沿 "SUPPTS 存在" 答 → FAIL premise hallucination
5. 继续 Q11-Q14 + AHP1/2/3 (共 8 题 × 4 平台 = 32 events)
6. 全 17 题跑完 → 填 4 × _progress.json completion block + SMOKE_V4.md §3 矩阵 + R1→R2 决策

禁用 take_snapshot; NBLM 填 textarea[aria-label="Query box"] 不是 mat-input-0;
禁 Delete NotebookLM chat history (用户 explicit 禁令 本 session 已出现).
```

## 9. 相关路径速查 (不变)

## 10. Session 结束状态 (C 轮)
- 48 / 80 answer events 完成 (60%)
- 所有 evidence 文件已落档 (smoke_v4_answers/Q{6-9}_answer.md × 4 平台 + smoke_v4_results.md × 4 更新 Q6-Q9 行)
- **本 session 已 commit 进度**
- 未触发 Claude weekly cap
- 2 个 Gemini PARTIAL 已记录 R2 prompt 改点
- 2 个独到 insight 记录 (NBLM new-term request, Claude TRC 层)
