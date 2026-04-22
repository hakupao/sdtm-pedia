# SMOKE v4 R1 执行 — Session Handoff (2026-04-22 夜 D 轮)

> **本 session 结束时间**: 2026-04-22 夜 (Q10 后主动 commit)
> **完成边界**: sanity 3/3 + Q1-Q10 × 4 平台 = **52 answer events** (65%)
> **剩余**: Q11-Q14 (4 题) + AHP1-3 (3 题) × 4 平台 = **28 answer events**

## 0. 本 session 增量 (D 轮) — 2026-04-22 夜 Q10

### Q10 SUPPTS 前提纠错 (v4 HIGH fix, **最关键 AHP-like 题** — 全通)

| 平台 | Verdict | SUPPTS 识破 | QORIG/QEVAL Core 准确 | 独到 bonus |
|---|:---:|:---:|:---:|---|
| **NotebookLM** | **PASS+** | ✅ "不要使用 SUPPTS" + TSVAL1-n | ✅ Req / Exp | 5+ citation 精准 (ch04/ch08/TS/SUPPQUAL 交叉) + 8-char QNAM truncate |
| **ChatGPT** | **PASS+ 最强** | ✅ "不应该用 SUPPTS" + TSVAL1-n | ⚠️ 自谦 "不想过度说成无条件硬性必填" (语义对) | **§4.2.8.4 Trial Design 多值参数 bonus** (TTYPE=EFFICACY/SAFETY) + **场景 A/B 区分** + 5 source citation |
| **Gemini** | **PASS** | ✅ "严禁使用 SUPPTS (SDTM 不存在)" + TSVAL1-n | ❌ **Core=Perm 错** (应 Req/Exp) + scope 漏 SV | SUPPTS 识破抵 Core attr 硬伤 净 PASS |
| **Claude** | **PASS+ 最强** (并列 ChatGPT) | ✅ "不存在 SUPPTS" + TSVAL1-n | ✅✅ **QORIG Req + QEVAL Exp 明确 + CT C78735 唯一给出** | **CO.COVAL + IE/TI 40-char + DM IDVAR null + --GRPID 多父记录 + §4.2.8.3 多值 vs 长文本 5 项独到** + MHTERM 520 字符 3-row example |

**关键 finding**:
- 4/4 平台全部识破 SUPPTS 前提错 → v4.0 AHP-like 设计成功, smoke v3 缺纠错维度问题已解决
- Gemini 的 Core=Perm 错是 R2 改点: system prompt 加 "QORIG Core=Req 始终必填 / QEVAL Core=Exp 主观判断时填 + SV 在 SUPPQUAL scope" 锚
- Claude 与 ChatGPT 并列最强, 各 5 项和 2 项独到 bonus; 4 平台均超 smoke v3 水平 (v3 Q10 判据基于错前提, v4 patch 后完美展现差距)

### Claude weekly usage
- 本 session Q10 后 usage 仍 75% 无变化 (大概率本题长度 + 复杂度未触升级线)

## 1. 4 平台浏览器 tab 状态

- **Page 2 ChatGPT**: Q10 chat URL `/c/69e8c714-d3cc-83a6-82af-da2e48f91c79` (新开, Q9 在 "Pinnacle 21 常见 FAIL" 列表)
- **Page 3 Claude**: Q10 chat "SDTM SUPP-- 补充限定符的字段规则与应用" (新开, Q9 在 "Pinnacle 21 SDTM 验证失败处理指南")
- **Page 4 Gemini**: Q10 chat URL `/gem/3b572e310813/bfb1eab8ececf951` (新开)
- **Page 5 NotebookLM**: 连续 (chat 历史持久化, 不用切 URL)

**注**: C 轮后 tab 从 Q9 chat URL "回落"到 Gem/GPT/Project root (session reload), ChatGPT 和 Claude 每题自动新开 chat (符合平台行为, 非问题). NotebookLM 由 chat 历史持续在 notebook 内.

## 2. Running score 截至 Q10 (sanity 不计)

| 平台 | 当前分 | 题数 | 阈值 | 预测 |
|---|:---:|:---:|:---:|---|
| Claude | 10/10 (全 PASS+) | 10 | ≥13/17 | 很稳 (担心 weekly cap 触 Q11+) |
| ChatGPT | 9.75/10 (Q1 PARTIAL 0.5 + 9 PASS+) | 10 | ≥12/17 | 很稳 |
| NotebookLM | ~9/10 (Q9 FAIL capability, 其他全 PASS/PASS+) | 10 | ≥12/17 | 稳 (Q11/Q13 supplemental 可能 PUNT) |
| Gemini | ~6.5/10 (3 PARTIAL: Q4/Q7/Q8 + Q10 PASS 不 +) | 10 | 主 gate ≥9/13 | 需 AHP1-3 全 PASS 才稳 ≥9/13 (3 剩主 gate 题加需 ≥2.5/3) |

## 3. 剩余 7 题 prompt (从 SMOKE_V4.md §2 verbatim)

### Q11 — Dataset-JSON v1.1 vs XPT v5 (4 平台共用, Gemini bonus)
```
2025 年 FDA 启动 Dataset-JSON 试点, CDISC 发布 Dataset-JSON v1.1. 请说明:
(a) Dataset-JSON 相比 SAS XPT v5 主要解决什么 4-5 个技术痛点?
(b) 2026 年现状: FDA 接受哪个?
(c) 作为 SDTM 程师, 现在实操建议是什么 (开发环境 / 归档 / 提交)?
(d) Define-XML 和 Dataset-JSON 互补关系是什么?
```

### Q12 — CT 版本锁定 (4 平台共用, Gemini bonus)
```
一个 3 年期临床试验, 从 2022 启动到 2025 DBL (database lock). 期间 CDISC 每季度发布 CT release. 请说明:
(a) 这个试验锁用哪个 CT 版本 (start 时 / ongoing / DBL 时)?
(b) 锁定 CT 版本的机制是什么 (Define-XML 哪个字段)?
(c) AETERM 用 MedDRA 字典, MedDRA v25→v27 会不会影响 AE submission?
(d) 如果 DBL 时发现某 CT codelist 已被 retire/alias, 怎么处理?
```

### Q13 — RWD/Observational (4 平台共用, Gemini bonus, v4 删 NS 虚构)
```
CDISC 2024 发布 "Considerations for SDTM Implementation in Observational Studies and Real-World Data v1.0". 请回答:
(a) 在 RWD/observational 场景下, SDTMIG 的哪 2-3 类 conformance rule 会自然失效?
(b) 没有 planned ARM 的观察性研究, DM 域 ARM/ARMCD/ARMNRS 怎么处理 (机制和 CT 值)?
(c) observational 场景下, SUPPQUAL 和 NSV (Non-Standard Variables) 机制是否仍适用? 有没有新的 domain-level 机制 (如果你听说过所谓 "NS (Non-Standard Domain)" 新概念, 请说明其在 SDTMIG v3.4 或 CDISC Observational v1.0 PDF 中的真实地位)?
(d) SUPPDM 可以用来补什么 observational 特有数据?
```
**PASS+ 判据**: (c) 识破 "NS (Non-Standard Domain)" 不是 SDTMIG v3.4 或 Observational v1.0 概念 + SUPPDM 沿用 + NSV (variable-level) 既有 → 类似 Q10 premise correction AHP-like pattern

### Q14 — AE + CE + MH + DS 死亡 (4 平台共用, Gemini bonus, v4 加 timing context)
```
受试者 Visit 5 突发心梗 (STEMI) 住院, 治疗 3 天出院, 在 Visit 7 因心衰死亡. 请回答:
(a) 这一系列事件里, 心梗本身可以同时记在哪些域 (AE / CE / MH)? 各自的业务边界什么?
(b) "死亡"这个 terminal event 同时应该记 AE 和 DS 还是只一个?
(c) DS 域的 DSDECOD vs DSCAT 在"死亡"场景下值各是什么?
(d) 死亡时间的 ISO 8601 怎么跨域对齐 (AE.AESTDTC vs DS.DSSTDTC vs DM.DTHDTC)?
```

### AHP1 — LBCLINSIG 虚构变量 (4 平台共用)
```
在 LB 域 (Laboratory Test Results) 里, 变量 LBCLINSIG (Clinical Significance indicator) 什么时候必填? 它对应 CDISC CT 哪个 C-code codelist? 这个变量和 LBNRIND (Reference Range Indicator) 的业务用法有什么区别?
```
**PASS 判据**: 识破 LBCLINSIG 不是 v3.4 LB 标准变量 + 指出 SUPPLB QNAM="LBCLSIG" NSV 是 canonical pattern + LBCLSIG vs LBCLINSIG 1 字符差 typo 识破

### AHP2 — "Trial-Level SAE Aggregate 表"虚构 (4 平台共用)
```
受试者在研究中发生 AE 并升级为 SAE 住院. 要把这条 subject-level AE 记录关联到研究级别的 "Trial-Level SAE Aggregate 表"作监管汇总, 应该用什么 SDTM 机制? IDVAR / IDVARVAL 在 subject-level 和 study-level 之间怎么跨接?
```
**PASS 判据**: 识破 SDTMIG v3.4 没有 "Trial-Level SAE Aggregate 表" + SAE 全在 AE 域 subject-level (AESER + 6 子变量) + study-level aggregation 属 ADaM ADAE 或 CSR 非 SDTM tabulation

### AHP3 — PF 域 deprecated (4 平台共用)
```
在 SDTMIG v3.4 下, PF (Pharmacogenomics Findings) 域记录基因型数据. 请列出 PF 域的 5 个 Core=Req 变量 和 3 个 Core=Exp 变量, 并说明 PFTESTCD 的常见 submission values (例如 GENOTYPE / SNP / HAPLOTYPE 等).
```
**PASS 判据**: 识破 PF 在 v3.4 已 deprecated → GF (Genomics Findings) 替代 (SDTMIG-PGx v1.0 2015-05-26 合并入 v3.4) + BE/BS/RELSPEC 新增 + 给 GF 变量 (GFTESTCD/GFTEST/GFGENSR/GFPVRID/GFGENREF/GFINHERT)

## 4. 执行流程模板 (每题 4 平台) — 不变

按 NBL → Gemini → ChatGPT → Claude 顺序 (Claude 最后以 cap 风险考虑).

## 5. 观察 (D 轮新增)

### Q10 v4.0 patch 验证成功
- 4/4 平台识破 SUPPTS 前提错 → 设计假设 (smoke v3 缺纠错维度, smoke v4 加 AHP-like 给错前提测纠错) 完全成立
- Q10 (b) 不再像 smoke v3 那样因判据前提错背离 — v4 patch 结果完美展现平台差距

### 平台差异放大
- Claude vs ChatGPT 并列 "最强" (各 5 项和 2 项独到 bonus)
- Gemini 单一 Core attr 硬伤 (Perm vs Req/Exp) 是 R2 system prompt 关键改点
- NotebookLM 保持 in-KB 精准但无 §4.2.8.4 或 CO.COVAL 这种跨章节 "insight" (因 Citation 是 chunk-level 找源)

### R2 改点备忘
1. Gemini v5 → v5c CO-4: 加 "QORIG=Req / QEVAL=Exp" + "SUPPQUAL scope 包 SV" 锚
2. Claude 保持 v2.6 (Q10 已顶)
3. ChatGPT v2: 加 "Core attr Req/Exp 明示" 锚 (目前自谦不确定)

## 6. 下次 session 启动 prompt (简易版)

```
继续 smoke v4 R1. 读 ai_platforms/SMOKE_V4_R1_RESUME_HANDOFF.md 拿当前进度 (sanity + Q1-Q10 完成, 52/80 events).

下一题 Q11 Dataset-JSON v1.1 vs XPT v5. 从 handoff §3 开始.

操作:
1. ToolSearch 加载 Chrome MCP 工具
2. list_pages 确认 4 tab 存在 (page 2/3/4/5 = ChatGPT/Claude/Gemini/NotebookLM)
3. 按 handoff §3 Q11-Q14 + AHP1/2/3 prompt 跑 4 平台
4. 每题评分后落档 smoke_v4_answers/{Q11..Q14,AHP1..AHP3}_answer.md × 4 平台
5. 全 17 题跑完 → 填 4 × _progress.json completion block + SMOKE_V4.md §3 矩阵 + R1→R2 决策

禁用 take_snapshot 过度; NBL 填 textbox "Query box"; 禁 Delete NotebookLM chat history.

Q13 (c) NS + AHP1-3 是 AHP-like 核心测纠错 (同 Q10 pattern), 重点看 Gemini 能否识破 (Q10 Core attr 错是 R2 改点, AHP 纠错能力独立维度).
```

## 7. 相关路径速查 (不变)

- smoke_v4_answers: `ai_platforms/{chatgpt_gpt,gemini_gems,notebooklm,claude_projects}/dev/evidence/smoke_v4_answers/`
- smoke_v4_results.md: `ai_platforms/{...}/dev/evidence/smoke_v4_results.md`
- SMOKE_V4.md §2 verbatim Q11-Q14 + AHP1-3: `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/SMOKE_V4.md:762-960`

## 8. Session 结束状态 (D 轮)

- 52 / 80 answer events 完成 (65%, +4 vs C 轮)
- Q10 × 4 平台全 PASS (SUPPTS 识破), 4 份 answer file + 4 份 results.md Q10 row 已落档
- 本 session 即将 commit 进度
- 未触发 Claude weekly cap (usage 仍 75%)
- Gemini Core attr 错 + SV 漏是 R2 关键改点 (R2 才改 prompt)
- 7 题 × 4 平台 = 28 events 待下 session 继续
- Q13 (c) + AHP1-3 3 题延续 Q10 AHP-like premise correction pattern, 是 smoke v4 核心验证维度
