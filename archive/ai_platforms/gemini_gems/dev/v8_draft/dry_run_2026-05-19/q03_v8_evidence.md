# Q3 — Gemini v8.1 dry-run evidence

> 日期: 2026-05-19 16:35-16:36 PM (Pro reset 后 ~1 min)
> Mode: Gemini 3.1 Pro
> Prompt: v8.1 (525 lines, deployed by user to Gem instructions)
> Runner: Chrome MCP fire-and-forget (gemini_runner.js pattern)

## 题文

> 某 PGx 试验, 受试者 Visit 2 现场采集血样 (BS-001), 当天运输到中心实验室 (运输过程记为一个事件), 第二天从 BS-001 样本提取 DNA 得到 DNA-001 子样本. 请说明: (a) 这三个"阶段" (采血 / 运输 / DNA 提取) 分别记录在哪些域? (b) 血样的"体积 = 5 mL"和"RNA 完整性数 (RIN) = 9.2"这两个**测量**记录在哪个域, 对应 Topic 变量值分别是什么; (c) BS-001 → DNA-001 这种**样本派生关系**怎么表达? 应该用哪个 Dataset (RELREC 还是另一个)?

## Verdict 矩阵

| 维度 | R3 v7.1 | v8.1 dry-run | Delta |
|---|:---:|:---:|---|
| Verdict | **FAIL** ⚠️ (跑题答 AE) | **PASS+** ✓ | ⬆ 修复 |
| Response len | 1541 chars (off-topic) | **1439 chars** | 相当 |
| Total ms | — | 47,641 | OK |
| (a) BE 三阶段 | ❌ 答 AE/AESEV/AEGRPID | ✅ BE / BECAT COLLECTION/TRANSPORT/PREPARATION/EXTRACTION (sponsor-extensible 注) | 完全修复 |
| (b) BS 测量 | ❌ 不沾 | ✅ BSTESTCD=VOLUME / RIN + BSORRES + BSORRESU | 完全修复 |
| (c) RELSPEC vs RELREC | ❌ 不沾 | ✅ "必须 RELSPEC, 绝对不能 RELREC" 区分 | 完全修复 |
| Anti-hallucination | — | ✅ "禁止臆造 BM (Biospecimen Measurements) 域" | 加分 |
| 双域并行 | — | ✅ "BE 行为 + BS 测量 双域并行, 切勿混入" | 加分 |
| CDISC 来源 | — | ✅ BE/BS/RELSPEC spec 三段引 | 加分 |

## Prong 验证

**Prong 1 (CO-4 入口守门)**: ✅ **完全 fire**.
- 关键词 "采血样" / "运输" / "DNA 提取" / "样本派生" 触发 BE/BS/RELSPEC 锚
- 切断了 v7.1 R3 时 AE/CM fallback path

**Reviewer fix L2 (BECAT EXTRACTION sponsor-extensible)**: ✅ 也 fire 了
- v8.1 显式写 "EXTRACTION 属于 sponsor-extensible 范畴" — KB BE/spec L111 只 inline 3 个 Examples, 这个注释是 reviewer L2 fix 直接产物

## 关键 response 片段

```
针对您提出的 PGx 生物样本流转与测量场景，在 SDTMIG v3.4 标准下有非常明确的专属域划分。

(a) 采血、运输、DNA 提取阶段的记录域
结论：这三个阶段全部记录在 BE (Biospecimen Events) 域。
- 现场采血: BECAT = "COLLECTION"
- 样本运输: BECAT = "TRANSPORT"
- DNA 提取: BECAT 可填 "PREPARATION" 或根据业务扩展填 "EXTRACTION"
  (属于 sponsor-extensible 范畴)
核心规则：拆分为多条独立 Event 记录

(b) 体积与 RIN 的测量域: BS (Biospecimen Findings)
- 体积 5 mL: BSTESTCD = "VOLUME", BSORRES = "5", BSORRESU = "mL"
- RIN = 9.2: BSTESTCD = "RIN" (BSTEST = "RNA Integrity Number")
核心边界：BE 记行为, BS 记测量, 双域并行
禁止臆造所谓的 "BM" (Biospecimen Measurements) 域

(c) BS-001 → DNA-001 派生关系
结论：必须 RELSPEC (Related Specimens), 绝对不能用 RELREC
- BS-001 为父级 (Parent), DNA-001 通过 REFID 与 PARENT 关联, LEVEL 表示代次
- RELREC 作用域是 subject-level 记录间关联 (AE 与 CM 因果), 不适用样本派生

来源: SDTMIG v3.4 BE domain — spec / BS domain — spec / RELSPEC domain — spec
```

## Raw response window key

`window.__SMOKE_GEMINI_RESULT` (1439 chars), captured at 2026-05-19 16:36 PM.
