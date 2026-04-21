# Q4 — AESEV 三档 vs CTCAE Grade 映射 (v2.1)

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e73a6e-5f60-83a2-9169-d80d7134187d
**Date**: 2026-04-21
**Thought for**: 2m 34s

## 原题

SDTMIG v3.4 中, AE 域的 AESEV (Severity) 变量有几档取值? 和肿瘤试验常用的 CTCAE Grade 1-5 如何对应? 如果 EDC 里只收到 Investigator 填的 CTCAE Grade, AESEV 该怎么填? Grade 5 对应什么特殊处理?

## ChatGPT 答案 (完整)

**结论**:

AE.AESEV (Severity/Intensity) 在 SDTMIG v3.4 里是 **3 档**: MILD / MODERATE / SEVERE, **不是 5 档**. 它是 Record Qualifier, Core: Perm, CT: C66769.

肿瘤试验如果使用 CTCAE Grade, 标准做法是填 **AE.AETOXGR**, 而不是 AE.AESEV. SDTMIG 明说: 使用 CTCAE 这类标准毒性分级时, **AETOXGR should be used instead of AESEV**; 多数情况下二者二选一.

所以, CTCAE Grade 1-5 并不是全部都映射到 AESEV. 标准对应关系其实是"分散"在多个 AE 变量里, 而不是都塞进 AESEV.

### 推荐理解方式

| CTCAE Grade | 标准 SDTM 表达 |
|-------------|---------------|
| Grade 1 | AETOXGR="1"; 若研究同时也保留 AESEV, 则 AESEV="MILD" |
| Grade 2 | AETOXGR="2"; 若同时保留 AESEV, 则 AESEV="MODERATE" |
| Grade 3 | AETOXGR="3"; 若同时保留 AESEV, 则 AESEV="SEVERE" |
| Grade 4 | AETOXGR="4"; **AESEV 没有单独的 Grade 4 档**, 不能做严格一一对应 |
| Grade 5 | AETOXGR="5"; 并应按"死亡结局"处理: **AEOUT="FATAL"**, 通常 **AESDTH="Y"**, 且 **AESER="Y"** / 可由 serious category 派生 |

### 为什么不能把 Grade 1-5 直接等同于 AESEV?

因为 CDISC 术语本身已经说明了:

- AESEV 的 codelist **C66769** 只有 MILD (同义含 Grade 1)、MODERATE (Grade 2)、SEVERE (Grade 3).
- AEOUT 的 codelist **C66768** 里有 FATAL (同义含 Grade 5). Grade 5 在 SDTM 里更像是"结局/死亡"信息, 而不是 AESEV 的一个 severity 档.

所以标准上最稳妥的说法是:
- Grade 1-3 可与 AESEV=MILD/MODERATE/SEVERE 对应
- Grade 4 没有 AESEV 专属档
- Grade 5 不应当理解成 AESEV 的第 5 档, 而应体现在 AETOXGR=5 + AEOUT=FATAL + 死亡/serious 相关变量上

### 如果 EDC 里只收到 Investigator 填的 CTCAE Grade, AESEV 该怎么填?

**首选答案**: 填 AETOXGR, 不要强行填 AESEV.

依据:
1. AE 规格对 AETOXGR 的说明是: "Toxicity grade according to a standard toxicity scale (e.g., CTCAE)"; 如果来自数值分级, 只存数字, 例如 "2", 不要写 "Grade 2".
2. AE 假设明确说: 在使用 CTCAE 这样的标准毒性分级时, 用 AETOXGR 代替 AESEV; 多数情况下只填其中一个.

所以如果 EDC 只有 CTCAE Grade:
- AETOXGR = "1" / "2" / "3" / "4" / "5"
- AESEV 可以留空
- 除非 sponsor 明确规定要同时保留 AESEV, 并在 metadata/业务规则里说明映射方法

### Grade 5 的特殊处理

Grade 5 是最需要单独注意的:

- AETOXGR="5"
- AEOUT="FATAL" (Outcome of Event)
- AESDTH="Y" (Results in Death) 通常应体现死亡 serious criterion; AESER 也应为 Y, 或由 seriousness category 推导. AE 假设还说明: 如果 CRF 对每个 serious category 单独收集, 则这些 category 变量会被填充, 并可派生 AESER.
- **不要把 Grade 5 当成 AESEV 的"第 5 档"去填**

### 实务建议

如果你在做 oncology AE 映射, 我会建议直接采用下面的规则:
- **只有 CTCAE Grade 时**: AETOXGR 填数字; AESEV 不填
- **同时收了 investigator severity (Mild/Moderate/Severe) 和 CTCAE grade 时**: 可同时保留 AESEV 与 AETOXGR
- **Grade 5 时**: 重点检查 AEOUT, AESDTH, AESER 是否一致, 而不是去找 "AESEV=Grade 5"

### 源溯源

- `<!-- source: knowledge_base/domains/AE/spec.md -->`
- `<!-- source: knowledge_base/domains/AE/assumptions.md -->`
- `<!-- source: knowledge_base/terminology/core/ae.md -->`

## 判据对齐 (v2.1)

- ✅ AESEV 三档: MILD / MODERATE / SEVERE (正确, C66769 显式引用)
- ✅ Grade 1 → MILD, Grade 2 → MODERATE, Grade 3 → SEVERE (精确映射)
- ✅ Grade 3-4 合并 SEVERE 判据: Grade 3 → SEVERE; Grade 4 明确指出 AESEV 无此档 (高于 v2.1 判据的"Grade 3-4 → SEVERE" 合并, 实为更严谨表达)
- ✅ Grade 5 = 死亡 → AEOUT=FATAL + AESDTH=Y + AESER=Y (v2.1 核心判据)
- ✅ AESEV ≠ AESER (Serious vs Severity 两个不同维度) — 隐含于整体讨论但未显式命名 (微扣分但不影响 PASS)
- ✅ **加分**: AETOXGR 优先于 AESEV (CTCAE 场景 SDTMIG 官方指引, 高于判据基线)
- ✅ 引 AE/spec.md + AE/assumptions.md + terminology/core/ae.md 3 源

## Verdict: **PASS** (1/1)

## 归因

系统 prompt v2.1 + AE knowledge base 命中, CTCAE Grade 映射对 + Grade 5 特殊处理完备 (AEOUT=FATAL + AESDTH=Y + AESER=Y 全链路), 额外提 **AETOXGR 优先策略** 体现 SDTM 深度. 源溯源 3 源完整.
