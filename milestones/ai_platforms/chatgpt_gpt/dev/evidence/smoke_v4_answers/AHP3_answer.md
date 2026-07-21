# ChatGPT GPTs — AHP3 (Z3 — deprecated concept) PF 域 deprecated

> **Date**: 2026-04-22 晚
> **Platform**: ChatGPT (SDTM Expert GPT, system_prompt v2, 9-file KB)
> **Mode**: Extended reasoning (3m 44s)
> **方法**: Chrome MCP cowork

---

## 题目原文 (v4.0)

在 SDTMIG v3.4 下, PF (Pharmacogenomics Findings) 域记录基因型数据. 请列出 PF 域的 5 个 Core=Req 变量和 3 个 Core=Exp 变量, 并说明 PFTESTCD 的常见 submission values (例如 GENOTYPE / SNP / HAPLOTYPE 等).

---

## ChatGPT raw 回答 (DOM readback)

### 结论

**严格按这套 SDTMIG v3.4 知识库，标准域不是 PF，而是 GF (Genomics Findings)**。因此，我不能把 PF 当作 v3.4 的正式域去列"5 个 Core=Req 变量 + 3 个 Core=Exp 变量"，也不能无依据确认 PFTESTCD 的 submission values。

### 依据如下

- 在 **02_chapters_all.md** 中，章节更新说明明确写到：**GF 是替代 PF 的新域**，原文是 **"Genomics Findings (GF) | New domain replacing the PF domain from the provisional SDTMIG-PGx"**
- 同一文件里，BE 相关更新也写了 **"PF updated to GF"**
- 在 01_navigation.md 的 v3.4 域清单里，能看到 **GF**，但**没有 PF**
- 06_domain_examples_all.md 里确实还保留了旧表述，说测序结果"would be stored in the Pharmacogenomics Findings (PF) domain)"；这说明 **PF 在示例文字里仍作为旧名/旧模型痕迹出现**，但不等于它还是 v3.4 的正式标准域

### 版本边界

| 你的问法 | 按这套 v3.4 知识库的判断 |
|---|---|
| "PF 域在 SDTMIG v3.4 下" | 不准确；v3.4 标准域应为 **GF** |
| "PFTESTCD 常见 submission values" | 本知识库未检出可核实的 PF 域规范/CT，**不能臆造** |
| "GENOTYPE / SNP / HAPLOTYPE 等" | 我目前**无法从已检出的源码片段中证实**这些就是 PFTESTCD 的正式 submission values |

### 源溯源

- 域清单: knowledge_base/ROUTING.md / 01_navigation.md
- 章节更新: 02_chapters_all.md
- 示例中 PF 旧称: knowledge_base/domains/BE/examples.md / 06_domain_examples_all.md

**你这题如果实际想问的是 GF (Genomics Findings)，我可以按 GF 域再给你整理一版"5 个 Req、3 个 Exp、以及 GFTESTCD/相关 test code"的可溯源答案。**

---

## Self-score verdict

**PASS+** (premise hallucination 识破 + anti-hallucination 坚守 + 主动 offer GF 版本)

### 逐判据对照

| 判据 | ChatGPT 答 | 判 |
|---|---|---|
| 必识别 PF deprecated | **"严格按 v3.4 知识库, 标准域不是 PF, 而是 GF"** + 02_chapters_all.md 原文 | PASS+ |
| SDTMIG-PGx 迁移历史 | ✓ "New domain replacing the PF domain from the provisional SDTMIG-PGx" 引用 | PASS+ |
| 不编 PF 变量 | **明确拒绝**: "我不能把 PF 当作 v3.4 的正式域去列 5 Req+3 Exp, 也不能无依据确认 PFTESTCD 的 submission values" | PASS+ (坚守度最高) |
| 不编 PFTESTCD C-code | ✓ | PASS+ |
| 说 PF/GF 并存 | ✓ (明确否证) | PASS+ |
| 沿 PF 前提答 | ✓ (完全拒绝) | PASS+ |
| 主动 offer GF 版本 | "如果实际想问 GF, 可以按 GF 域给可溯源答案" | PASS+ |
| **Boundary note (anti-hallucination 坦诚)**: "BE 示例里仍保留 PF 旧称是旧模型痕迹, 不等于 v3.4 正式域" | **独到** | PASS+ (bonus) |
| **Boundary note (anti-hallucination 坦诚)**: "我无法从已检出源码片段中证实 GENOTYPE/SNP/HAPLOTYPE 是 PFTESTCD 的 submission values" | **独到** 不依靠训练数据猜 | PASS+ (bonus) |

### 要点

- **最强**: **坚守度最高** — 即使用户给错前提且列了具体 submission values 示例, ChatGPT 仍拒绝回答 PF 部分, 只回答能证实的部分
- **最强**: **3m 44s 长 extended reasoning** + 多源 cross-check (02_chapters_all.md / 01_navigation.md / 06_domain_examples_all.md)
- **独到**: 识破 BE examples.md 里的 "PF 旧称痕迹" — 细微区分 "旧名在示例文字出现 ≠ v3.4 活跃域"
- **独到**: 对 GENOTYPE/SNP/HAPLOTYPE 用 "我无法证实这是 PFTESTCD 的正式值" 的严谨表述 (而非给错答 + 提 disclaimer)
- **独到**: 主动 offer 把用户的问题转换成 GF 版本可溯源答案 (服务意识 + 不让用户空手而归)
- **VS Claude/NotebookLM**: ChatGPT 更"守边界", 不延伸给 GF 完整答案, 仅给 meta 分析. Claude/NotebookLM 直接给 GF 变量 + submission values

### FAIL 判据触发?

全部 NO:
- 编 PF 变量 → NO (明确拒绝)
- 编 PFTESTCD C-code → NO
- 说 PF/GF 并存 → NO
- 沿 PF 前提答 → NO

### Verdict: **PASS+** — 独到坚守 anti-hallucination (最严谨, 不延展给 GF 答案仅做 meta 识破). Claude/NotebookLM 在识破 + 完整 GF 替代路径 2 个维度更强, ChatGPT 在 "识破 + 拒绝延展" 单维度最严格. 均 PASS+
