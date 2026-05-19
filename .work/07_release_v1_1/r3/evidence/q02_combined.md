# Q2 — Cross-Platform Combined Evidence

> 2026-05-19 跑. Q1 后采用 combined 单文件 (减 token, 不损 evidence 质).
> 题: CP 域 — 流式细胞测 CD4+ T 细胞 ACTIVATED 亚群 + 5 子问 (Topic / Sub / state markers / Method / vs LB)
> R1 baseline: 4 平台全 PASS. R3 期望: 持平或升级.

## 4 平台 Verdict 矩阵

| 平台 | Verdict | t_done | response 长度 | 关键命中 |
|---|:--:|:--:|:--:|---|
| Gemini Gem | PASS | 44s | 1038 chars | CP + CPTESTCD/CPTEST + Sub 后缀 + CPSBMRKS + CPCELSTA=ACTIVATED + CPCSMRKS=Ki67+ + CPMETHOD=FLOW CYTOMETRY + vs LB |
| ChatGPT GPT | **PASS+** | ~115s | 2183 chars | + CPMRKSTR 全 marker string + **PROLIFERATING 临床纠错 bonus** (Ki67+ 更典型 PROLIFERATING, 用 ACTIVATED 需 Define-XML 解释) + 区分 CPSBMRKS/CPMRKSTR/CPCSMRKS 三 marker 字段 |
| NotebookLM | PASS | 109s | 1874 chars | + 互锁规则 (CPCELSTA / CPCSMRKS 一填另必填) + cytokines→LB 反例 + RAG 引 KB 3 文件 (19_fnd_morphology_bs_cp_cv.md / 36_ct_specialized.../ 33_ct_general.md) |
| Claude Project | **PASS+** | ~170s (manual extract) | 3561 chars | + **CPGATE/CPGATDEF 门控专用变量** + CPANMETH + CPSPEC=PBMC(C78734) + 5 CT codelist 全引 (C181172-4 + C85492 + C78734) + 反例 "WBC + 5-part diff = LB" + 引用 SDTMIG §6.3.5.3 Example 1a/1b/2/5 |

## PASS 判据全表 (CR: critical, BONUS: 加分)

| 判据 | Gemini | ChatGPT | NotebookLM | Claude |
|---|:--:|:--:|:--:|:--:|
| CR 域 = CP | ✅ | ✅ | ✅ | ✅ |
| CR (a) Topic = CPTESTCD + CPTEST Req | ✅ | ✅ | ✅ | ✅ + 区分 Topic vs Synonym Qualifier 角色 |
| CR (b) Sub 后缀 + CPSBMRKS 区分 | ✅ | ✅ | ✅ | ✅ + 5 变量分工最完整 |
| CR (c) CPCELSTA=ACTIVATED + CPCSMRKS=Ki67+ | ✅ | ✅ | ✅ + 互锁 | ✅ + CPMRKSTR + CPGATE |
| CR (d) CPMETHOD = FLOW CYTOMETRY (C85492) | ✅ | ✅ | ✅ | ✅ + CPANMETH + CPSPEC |
| CR (e) CP vs LB 边界 | ✅ | ✅ | ✅ + cytokines→LB | ✅ + WBC/diff→LB 反例 |
| BONUS 临床纠错 / 额外变量 / 例子引用 | — | ✅ PROLIFERATING | ✅ RAG sources | ✅ CPGATE/Example refs |

## FAIL 判据全过 (0 命中)

| FAIL 判据 | Gemini | ChatGPT | NotebookLM | Claude |
|---|:--:|:--:|:--:|:--:|
| 答 LB / IS / 自创 FC | ❌ | ❌ | ❌ | ❌ |
| CPSBMRKS vs CPCELSTA 混 | ❌ | ❌ | ❌ | ❌ |
| 漏 Sub 后缀规则 | ❌ | ❌ | ❌ | ❌ |
| Method 答 PCR/ELISA | ❌ | ❌ | ❌ | ❌ |

## R1 vs R3 Delta

| 平台 | R1 | R3 | Delta |
|---|:--:|:--:|---|
| Gemini | PASS | PASS | = (持平) |
| ChatGPT | PASS | PASS+ | ↑ (PROLIFERATING 纠错升级) |
| NotebookLM | PASS | PASS | = |
| Claude | PASS | PASS+ | ↑ (5 marker 分工 + gating-specific 变量) |

**Q2 R3 净增 2 个 PASS+ upgrade (ChatGPT + Claude), 0 regression** ✅

## Raw response paths

- Gemini: window.__SMOKE_GEMINI_RESULT (1038 chars; conversation cc71c67fd7da1b11→8de06c78ef9d75ef)
- ChatGPT: window.__SMOKE_CHATGPT_RESULT (2183 chars; URL c/6a0bd859-b9e4-83a2-9780-d07c95bbe155)
- NotebookLM: window.__SMOKE_NOTEBOOKLM_RESULT (1874 chars)
- Claude: window.__SMOKE_CLAUDE_RESULT (3561 chars manual extract; URL 70481abe-8935-48bd-8630-4a42997943a6)

## Runner 改进 carry (Q2 期间发现)

Claude runner Q2: done signal 失效原因 = Claude **input 空时 send btn 整个被移除而非 disabled**. 现有 `fSendAny()` 找 `aria-label="Send message"` 找不到. 临时手动 extract.

→ Carry to Q3+ Claude runner: done signal 改为 `!stopBtn && (mdSegCount > preCount) && DOM static for 3s` — 不依赖 send btn 存在.
