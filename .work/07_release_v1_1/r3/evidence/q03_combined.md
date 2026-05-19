# Q3 — Cross-Platform Combined Evidence

> Q3 (A3 — BE + BS + RELSPEC): PGx 样本 BS-001 采血/运输/DNA 提取 + VOLUME/RIN + 派生关系
> R1 baseline: 4/4 PASS. R3: ⚠️ Gemini regression (跑题).

## Verdict 矩阵

| 平台 | Verdict | 关键观察 |
|---|:--:|---|
| Gemini Gem | **FAIL** ⚠️ | **跑题** — user query 正确 (BS-001/DNA-001 PGx), 但 Gemini 答 AE 拆分/合并 (AESEV/AEGRPID), 完全不沾 BE/BS/RELSPEC. responseLen 1541 chars 全部 off-topic. v7.1 system prompt 锚没拉住 |
| ChatGPT GPT | **PASS+** | BE 三阶段 + BEREFID/BETERM/BECAT (COLLECTION/TRANSPORT/PREPARATION) + BS BSTESTCD=VOLUME/RIN + RELSPEC REFID/PARENT/LEVEL + 区分 RELREC vs RELSPEC + RIN 应在 RNA 子样本临床纠错 |
| NotebookLM | **PASS** | BE/BS/RELSPEC 全中 + BSORRESU mL (C71620) + RAG KB 引 4 文件 |
| Claude Project | **PASS+** | + BEPARTY 责任方 + BSCAT (SPECIMEN MEASUREMENT vs QUALITY CONTROL) + 5 CT codes (C124300/C124299/C78734/C111114/C74720/C63637) + RELSPEC assumption 原文引 + ASCII 数据流图 |

## R1 vs R3 Delta

| 平台 | R1 | R3 | Delta |
|---|:--:|:--:|---|
| Gemini | PASS | **FAIL** | ⚠️ **REGRESSION** (跑题 hallucination) |
| ChatGPT | PASS | PASS+ | ↑ |
| NotebookLM | PASS | PASS | = |
| Claude | PASS | PASS+ | ↑ |

## Gemini regression 根因猜测 (待 Phase D 拷打)

1. **v7.1 system prompt 不含 BE/BS/RELSPEC 专项锚** — CO-1/CO-2/CO-3 主要锚 AE/DM/ARM, BE/BS 没在 CO-N 提及, 当题文带 "受试者... 样本... 实验室..." 时 Gemini 走通用 SDTM associated 路径走偏到 AE.
2. **题目长度 + 多子问 + PGx 上下文** 触发 Gemini 跑题模式 — 模型 attention 锚被 "受试者... 阶段... 测量..." 拽到 AE 高密 token.
3. **Pro mode 高密度回答倾向先给"行业最常见域"AE 当兜底** — KB 内 AE 信号最强.

→ Follow-up R3 RETRO: Gemini system prompt 加 BE/BS/RELSPEC 专项锚 (CO-N), 或在 system prompt 加 "如果题文含 'biospecimen/blood/sample/aliquoting' 关键字, 强制走 BE/BS/RELSPEC 不走 AE/CM" 守门.

## Raw response paths

- Gemini: window.__SMOKE_GEMINI_RESULT (1541 chars off-topic AE answer)
- ChatGPT: window.__SMOKE_CHATGPT_RESULT (2178 chars)
- NotebookLM: window.__SMOKE_NOTEBOOKLM_RESULT (1420 chars)
- Claude: window.__SMOKE_CLAUDE_RESULT (4142 chars)
