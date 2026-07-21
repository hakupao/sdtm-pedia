# Q9 (E1 — Pinnacle 21 常见 FAIL 分类)

> Date: 2026-04-22 / Account: bojiang.zhang.0904@gmail.com / Fresh chat

---

## 题

Pinnacle 21 (OpenCDISC Validator) 是 FDA 审查 SDTM 数据时常用的验证工具, 对一份 SDTM 数据会返回 Errors / Warnings / Notices 三级 issue. 请按类型分类列举 5-6 大类常见 FAIL, 每类举 1 个典型触发例子, 并说明: 遇到 Pinnacle 21 FAIL 时, 什么时候应该修数据, 什么时候应该在 Reviewers Guide 文档化并保留不修?

**KB 锚点声明** (源题): "本题不走 KB, 靠业务常识 + Pinnacle 21 常识"

## NotebookLM 答 (full text)

未收录 / outside the knowledge base

当前的 42 个知识库文件涵盖了 CDISC SDTMIG v3.4 标准、SDTM v2.0 概念模型以及相关的受控术语 (NCI EVS), 但并未收录关于 Pinnacle 21 (OpenCDISC) 验证工具的具体规则、报错分类 (Errors / Warnings / Notices) 以及 Study Data Reviewer's Guide (SDRG) 的文档化策略。

知识库仅能根据 SDTMIG v3.4 回答特定的变量属性 (如 Core = Req / Exp / Perm)、受控术语 (CT) 的限定以及各 domain 的官方 mapping 业务规则。

如果您想核对某个具体的报错是否违背了 SDTMIG v3.4 的官方定义 (例如某个特定的 Core 是否必须填值, 或者某个变量的 ISO 8601 时间格式要求), 或者您可以提供特定的 CDISC/验证文档参考, 请告诉我具体的变量或场景!

## Verdict

| Criterion | Required | Got | Status |
|---|---|---|:---:|
| 列 5-6 大类 FAIL | Date / CT / Req-Exp 缺失 / Duplicate / 类型错 等 5 类 | 0 类 (未收录) | ❌ |
| 每类 1 例 | 例 AESTDTC>AEENDTC, AESEV="SEV" 等 | 0 例 | ❌ |
| 修 vs 文档化决策 | 真错→修 / 标准不匹配但数据真→SDRG 文档化 | 未给出 | ❌ |
| 不混 Error/Warning/Notice 等级 | 三级清晰 | N/A (未答) | — |
| 不给虚构 rule ID | 不要求具体 ID | N/A (未答) | — |

**Verdict**: ❌ **FAIL (PUNT)** (0 / 1) — NotebookLM 礼貌回避, 触发 in-KB-only Custom mode 边界. 

**根因分析**:
- 题目本身设计: KB 锚点显式声明 "本题不走 KB, 靠业务常识 + Pinnacle 21 常识" — 这是 generalization probe, 测 NotebookLM 是否能跨 KB 触达通用业务知识.
- NotebookLM 行为: Custom mode instructions.md 13 条 behavior rule 强调 "authoritative layer 优先级 spec > ch04 > CT > assumptions > examples", 严格 in-KB. NotebookLM 没有 web search, 没有外部 fallback, 在 KB 找不到 Pinnacle 21 时 punt 是 correct policy 行为, 但对 generalization probe 来说算 FAIL.
- 替代解读: 这不是 hallucination FAIL (没编造错答案), 是 "scope decline" — 模型边界正确但能力不及 ChatGPT/Gemini (有 web search). 算 PARTIAL/PUNT 也合理.

**记 FAIL 严格记**: 严格按 "PASS 判据 5 大类必含" 评判, 0/5 ⇒ FAIL.
