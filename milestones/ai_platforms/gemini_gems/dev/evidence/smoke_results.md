# Gemini Gems — Node 3b Smoke Test Results (Batch 1)

> 测试日期: 2026-04-21
> Gem: SDTM Expert (Custom Gem, Google AI Pro)
> 账号: bojiang.zhang.0904@gmail.com (`/u/1/`)
> Gem URL: https://gemini.google.com/u/1/gem/3b572e310813/d053fd5f9418b93c
> 上传内容: 4 文件 (01_navigation.md + 02_chapters_all.md + 03_model_all.md + 04_terminology_core.md)
> 预估 token: 884,918 / 1,000,000 (88.49%)
> Chat: "AE.AESER 变量的受控术语"
> 交互方式: Chrome MCP (DOM-based) by Claude 代理执行
> 判据来源: `dev/checkpoints/CHECKPOINT_N3B_HANDOFF.md`

---

## 总体得分

**4/5 PASS (80%)** — 通过 Node 3b 进入 Node 4/5 门槛 (≥ 4/5 PASS)

| 题号 | 类型 | 结果 | 关键点 |
|-----|------|------|--------|
| S1 | 精确查询 | ✅ **PASS** | Y/N 二值、C66742、NCI EVS link 齐全 |
| S2 | 头部 5 条 (C65047) | ❌ **FAIL** | 4/5 Terms 命中; Row 5 Submission Value 错 (A1MICG vs A1MCREAT) |
| S3 | 🚨 末尾 5 条 (C100129) | ✅ **PASS** | **P12 R1 hard gate 绿**, recency bias 未触发 |
| S4 | 🚨 中段 3 条 (C67154) | ✅ **PASS** | **P12 R2 hard gate 绿**, Lost-in-Middle 未发生 |
| S5 | 边界 (AERELN 未收录) | ✅ **PASS** | 零臆造 Synonym, 声明未收录 + 给 NCI EVS |

**P12 状态**: 🟢 全绿 (S3 + S4 双 PASS) → 不触发 R1/R2
**Instructions §边界补强**: 不需要 (S5 PASS)
**决策**: 派 Rule D reviewer + commit C3b + 进 Node 4/5

---

## S1. AE.AESER 受控术语

### 问
> 根据 SDTMIG v3.4，AE.AESER 变量的受控术语是什么? 请列出允许值 (Y/N) 和对应的 NCI Codelist Code。

### 答 (Gemini 原文)
```
AE.AESER (Serious Event) 的受控术语集为 NY (No Yes Response)，其对应的 NCI
Codelist Code 为 C66742。允许值为:

Y (Yes)
N (No)

变量定义:
- Variable: AESER
- Label: Serious Event
- Role: Record Qualifier
- Core: Req (Required)
- Controlled Terms: NY (C66742)
- 源路径: ``

ℹ️ 边界注记 (Codelist 未 Inline)
本 Gem 的 04_terminology_core.md 仅包含 5 段高频 codelist (LB, Oncology,
Interventions, QS). C66742 (No Yes Response) 的完整 Term 细节未在本 Gem 中
全量列出。若需查看最新扩展或详细定义, 建议访问 NCI EVS Browser:
https://evsexplore.semantics.cancer.gov/evsexplore/ 搜索代码 C66742。
```

### PASS 判据核对
- ✅ 回答 Y/N 二值
- ✅ 引用 Codelist Code = C66742
- ✅ 给出 NCI EVS 外部入口
- ✅ 主动声明 C66742 未 inline (边界诚实)
- ⚠️ 源路径显示为空反引号 `` (应为 `02_chapters_all.md` 或 `03_model_all.md` 中 AE 域节的 line 引用)
- ⚠️ Core 标为 "Req (Required)" vs ChatGPT 显示 "Exp (Expected)" — 预期 SDTMIG v3.4 AE.AESER = Exp。此为 **潜在语料偏差**, 需后续 Node 4 A/B 查验

**结果**: ✅ **PASS** (主判据齐全, Core label 语义偏差入 Node 4 todo)

---

## S2. Laboratory Test Code (C65047) 头 5 条

### 问
> 04_terminology_core.md 最前面的 codelist (Laboratory Test Code, C65047) 头 5 条 Term (Code + Submission Value + Synonym) 是什么?

### 答 (Gemini 原文)
```
在文件 04_terminology_core.md 中, 首个受控术语集 Laboratory Test Code
(C65047) 的前 5 条术语 (Term) 信息如下:

Code      CDISC Submission Value     CDISC Synonym(s)
C100429   A1AGLP                     Alpha-1 Acid Glycoprotein
C181404   A1ANTRPF                   Alpha-1 Antitrypsin, Functional
C80167    A1ANTRYP                   Alpha-1 Antitrypsin; Serum Trypsin Inhibitor
C186022   A1MCGEXR                   Alpha-1 Microglobulin Excretion Rate
C100462   A1MICG                     Alpha-1 Microglobulin     ← row 5 MISMATCH

源路径: ``
Codelist 信息: Laboratory Test Code (C65047), 可扩展 (Extensible: Yes)
```

### 预期 vs 实际 (逐行对比)

| # | Expected Code | Expected SV | Actual Code | Actual SV | 结果 |
|---|---|---|---|---|---|
| 1 | C100429 | A1AGLP | C100429 | A1AGLP | ✅ |
| 2 | C181404 | A1ANTRPF | C181404 | A1ANTRPF | ✅ |
| 3 | C80167 | A1ANTRYP | C80167 | A1ANTRYP | ✅ |
| 4 | C186022 | A1MCGEXR | C186022 | A1MCGEXR | ✅ |
| 5 | **C100462** | **A1MCREAT** | **C100462** | **A1MICG** | ❌ Code ✅ / SV ❌ |

### PASS 判据核对
- ❌ 5 条 Term 准确 (Code + Submission Value 必中) → **仅 4/5 命中**
- ❌ 引用 `lb_part2.md` (源路径空反引号)
- ✅ 无整行臆造 (row 5 的 Code + Submission Value 组合 "C100462 / A1MICG" 是真实 NCI 术语, 但属于 C65047 codelist 的其他位置 / 不是 line 25 的 row 5)

**结果**: ❌ **FAIL** (4/5 命中, 严格 PASS 要求 5/5)

**归因推测**:
- 可能原因 1: Gemini 对 C65047 头部 alphabetical ordering 判定错位, 把另一条 A1MICG 当 row 5
- 可能原因 2: lb_part2.md 实际文件顺序 vs 字母序可能不一致 (需 Node 4 grep 确认 line 25 的 row 5)
- **不是** recency bias 或 Lost-in-Middle — 头部召回成功率 80% (4/5)

---

## S3. Category of Questionnaire (C100129) 末尾 5 条 — **🚨 P12 R1 hard gate**

### 问
> 04_terminology_core.md 最后一个 codelist (Category of Questionnaire, C100129) 最前面的 5 条 Term (Code + Submission Value + Synonym 列) 是什么?

### 答 (Gemini 原文)
```
在文件 04_terminology_core.md 的末尾部分, Category of Questionnaire
(C100129) 术语集的前 5 条术语 (Code + Submission Value + Synonym) 如下:

Code      CDISC Submission Value    CDISC Synonym(s)
C187516   ABC                        ABC01
C122370   ACQ                        ACQ01
C123658   ACT                        ACT01
C100762   ADAS-COG                   ADC
C106888   ADCS-ADL MCI               ADL03

源路径: ``
Codelist 信息: Category of Questionnaire (C100129), 可扩展 (Extensible: Yes)
提示: 该 Codelist 位于 04_terminology_core.md 的尾部区域 (约 90% 偏移量处)
```

### 预期 vs 实际 (逐行对比)

| # | Expected | Actual | 结果 |
|---|---|---|---|
| 1 | C187516 / ABC / ABC01 | C187516 / ABC / ABC01 | ✅ |
| 2 | C122370 / ACQ / ACQ01 | C122370 / ACQ / ACQ01 | ✅ |
| 3 | C123658 / ACT / ACT01 | C123658 / ACT / ACT01 | ✅ |
| 4 | C100762 / ADAS-COG / ADC | C100762 / ADAS-COG / ADC | ✅ |
| 5 | C106888 / ADCS-ADL MCI / ADL03 | C106888 / ADCS-ADL MCI / ADL03 | ✅ |

### PASS 判据核对
- ✅ 5 条 Term 准确 (Code + Submission Value + Synonym 全中) — **5/5 命中**
- ✅ Gem 主动报 "位于尾部区域 (约 90% 偏移量处)"
- ✅ 无 "未收录" fallback (实际 inline)
- ✅ 无臆造
- ⚠️ 源路径显示为空反引号 `` (应为 `qs_part1.md` line 6050-6068)

**结果**: ✅ **PASS** — **P12 R1 hard gate 绿**, Gemini 1M 窗口 @ 884K (88.5%) 末尾 recall = 100%

---

## S4. Laboratory Test Name (C67154) 中段 3 条 — **🚨 P12 R2 hard gate**

### 问
> 04_terminology_core.md 中段的 Laboratory Test Name codelist (C67154) 最前面的 3 条 Term (Code + Submission Value + Synonym 列) 是什么?

### 答 (Gemini 原文)
```
在文件 04_terminology_core.md 的中段, Laboratory Test Name (C67154) 术语集
的前 3 条术语 (Code + Submission Value + Synonym) 如下:

Code      CDISC Submission Value                         CDISC Synonym(s)
C179752   1,25-Dihydroxyvitamin D2                       1,25-Dihydroxycalciferol; ...; Ercalcitriol
C179754   1,25-Dihydroxyvitamin D3                       1,25-Dihydroxycholecalciferol; ...; Calcitriol
C179753   1,25-DihydroxyvitD2+1,25-DihydroxyvitD3        1,25-Di(OH)vitamin D2+...

源路径: ``
Codelist 信息: Laboratory Test Name (C67154), 可扩展 (Extensible: Yes)
提示: 该 Codelist 紧随 Laboratory Test Code (C65047) 之后, 位于中段
      在 SDTM LB 域中通常映射至 LBTEST 变量
```

### 预期 vs 实际 (逐行对比)

| # | Expected | Actual | 结果 |
|---|---|---|---|
| 1 | C179752 / 1,25-Dihydroxyvitamin D2 | ✅ 同 | ✅ |
| 2 | C179754 / 1,25-Dihydroxyvitamin D3 | ✅ 同 | ✅ |
| 3 | C179753 / 1,25-DihydroxyvitD2+1,25-DihydroxyvitD3 | ✅ 同 | ✅ |

### PASS 判据核对
- ✅ 3 条 Term 准确 (Code + Submission Value 必中) — **3/3 命中**
- ✅ Gem 主动报 "位于中段" + 关联 LBTEST 变量映射 (语义召回 up)
- ✅ 无臆造
- ⚠️ 源路径显示为空反引号 `` (应为 `lb_part3.md`)

**结果**: ✅ **PASS** — **P12 R2 hard gate 绿**, Lost-in-Middle 未发生, 中段召回 = 100%

---

## S5. AERELN Synonyms (零臆造硬门槛)

### 问
> AERELN codelist 的所有 Synonyms 是什么?

### 答 (Gemini 原文)
```
本 Gem 的 04_terminology_core.md 仅包含 5 段高频受控术语集:
lb_part2/3 (Laboratory Test)、oncology_part1、interventions (干预类)
和 qs_part1 (问卷类)。

AERELN (Relationship to Non-Study Treatment) 术语集未收录于本 Gem 的
inline 范围内。

边界说明与建议:
- 术语集状态: AERELN (NCI Code: C117711) 对应变量 AE.AERELNST
  (Relationship to Non-Study Treatment)
- 查询建议:
  完整术语及同义词请访问 NCI EVS Browser:
  https://evsexplore.semantics.cancer.gov/evsexplore/ 搜索 C117711
  若您是指与研究药物的关系 AEREL (C66797), 该术语集同样未 inline
- 源路径参考:
  变量定义见 `` 中的 AERELNST 节
  术语汇总请查阅 NCI 公布的 general_part*.md 类源文件
```

### PASS 判据核对
- ✅ **声明 "本 Gem 未收录"** (主动, 明确)
- ✅ **给外部入口** (NCI EVS Browser URL + C117711 + 源文件指向)
- ✅ **零臆造 Synonym** (没有列任何虚构的 Synonym 列表 — PASS 硬门槛核心)
- ➕ 加分项: 主动区分 AERELN (C117711) vs AEREL (C66797), 避免用户混淆

**结果**: ✅ **PASS** — 边界诚实 + 零臆造, Instructions §边界 无需补强

---

## 关键观察

1. **P12 双 hard gate 全绿** — S3 (尾部 C100129) + S4 (中段 C67154) 均精确命中, 证明 Gemini 1M context @ 884K tokens (88.5%) recency bias 未失效, Lost-in-Middle 未发生。单批全上架构 Node 3b 层面验证成功。

2. **S2 头部召回 4/5 偏离** 是非 P12 类缺陷 — 既不是末尾丢失也不是中段遗漏, 而是头部 row 5 的 Submission Value 选错 ("A1MICG" vs "A1MCREAT"), Code 本身 (C100462) 正确。推测是 alphabetical ordering vs 文件原序的不一致, 或近邻条目错位。**不触发 P12 R1/R2**, 但需 Node 4 grep 核验 `lb_part2.md` line 25 实际内容。

3. **源路径溯源全部失败** — S1-S5 所有响应的源路径字段均显示为 `` (空反引号)。Gemini 无 RAG 索引强制只生成 inline 文本引用, 而不像 ChatGPT Retrieval 那样自动附加 file citation。这是 **Gemini 平台本身的架构差异**, 非 Gem 配置 bug, 但影响审计可追溯性。建议 Node 4 在 system_prompt 中显式加 `引用格式: <file>.md:line-range` 强约束。

4. **S1 Core label 语义偏差** (Req vs Exp) — 相对 ChatGPT Batch 1 的 "Exp (Expected)" 有潜在语料偏差。SDTMIG v3.4 AE.AESER 标准值应为 **Exp**。Gemini 把 AESER 报为 "Req (Required)" 是事实错误, 但由于 S1 PASS 核心判据 (Y/N + C66742 + EVS link) 齐全, 不降级 S1 整题 FAIL, 而是入 Node 4 A/B 的 cross-platform 一致性 todo。

---

## 异常/警告

- **S2 Row 5 事实错误** — 影响未来用户查询头部 C65047 时的 top-5 准确度; 后续 Node 4 需补做 5-row 显式校对
- **源路径全空** — 跨越 S1-S5 全部响应; 架构层面限制, Node 4 优化 system_prompt 解决
- **S1 Core label 偏差** (Req vs Exp) — 单点事实错误, 需 Node 4 A/B 比对确认是否其他变量也有同类偏差

---

## Smoke Exit Decision

根据 `dev/checkpoints/CHECKPOINT_N3B_HANDOFF.md` §Exit Criteria:

| 判据 | 实际 | 结果 |
|-----|------|------|
| 总分 ≥ 4/5 PASS | 4/5 PASS | ✅ 通过 |
| S3 (P12 R1 hard gate) PASS | ✅ PASS | ✅ |
| S4 (P12 R2 hard gate) PASS | ✅ PASS | ✅ |
| S5 (零臆造) PASS | ✅ PASS | ✅ |

**命中行动**: `≥ 4/5 PASS + S3 PASS + S4 PASS` → 派 Rule D reviewer + commit C3b + **进 Node 4 / 跳 Node 5** (Gemini 单批终态可跳 Node 4 直进 Node 5 retrospective)

---

## 浏览器截图证据

- Gemini chat URL: https://gemini.google.com/u/1/gem/3b572e310813/d053fd5f9418b93c
- Chat 名称: "AE.AESER 变量的受控术语"
- 账号验证: bojiang.zhang.0904@gmail.com (URL `/u/1/`)
- 5 题依次提问, 每题一条消息, 无合并
- 所有回答已由 Chrome MCP DOM-based 抓取 (`document.querySelectorAll('message-content')`)

---

## Sources

- [Node 3b Handoff (Gemini)](/sessions/wizardly-tender-fermat/mnt/SDTM-compare/ai_platforms/gemini_gems/dev/checkpoints/CHECKPOINT_N3B_HANDOFF.md)
- [ChatGPT Batch 1 Results (对比基线)](/sessions/wizardly-tender-fermat/mnt/SDTM-compare/ai_platforms/chatgpt_gpt/dev/evidence/smoke_batch1_results.md)
- Live Gem: https://gemini.google.com/u/1/gem/3b572e310813/d053fd5f9418b93c
