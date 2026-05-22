# Q-S1 BECAT EXTRACTION × 4 平台 — UI-level Chrome MCP fire

> Date: 2026-05-20 18:21+09:00
> Method: Chrome MCP fire-and-forget, new conversation per platform
> Question: 在 SDTMIG v3.4 BE 域 (Biospecimen Events) 里, BECAT 变量除了 CDISC canonical 三个 examples (COLLECTION / PREPARATION / TRANSPORT) 之外, sponsor 还能扩展什么值? 给一个 DNA / molecular biology specimen processing 场景下的常见扩展例子, 并说明 BECAT 是否 sponsor-extensible.

---

## Verdict 汇总

| 平台 | UI-level Verdict | Paper-level | Bridge |
|---|:-:|:-:|---|
| Gemini v9 | **PASS+** | PASS | (no bridge needed; KB direct) |
| ChatGPT v3 | **PASS** | PASS | (no bridge needed) |
| Claude v3 | **PASS+** ★ | PARTIAL | ★ **paper PARTIAL → UI PASS+** via R5 premise correction + Example 2 reasoning |
| NotebookLM v3 | **PASS** | PASS | (no bridge needed) |

**4/4 UI-level PASS (Q-S1 100%)**

---

## Gemini v9 — PASS+

URL: https://gemini.google.com/u/1/gem/3b572e310813/b76bce39a5d33285

**Conclusion (BECAT Sponsor-Extensible 性质)**: BECAT 是 Sponsor-Extensible（可扩展）的。
- COLLECTION / PREPARATION / TRANSPORT 是 canonical examples
- DNA/分子生物学扩展: **EXTRACTION** (提取) + ALIQUOTING (分装) + QUANTIFICATION (定量) + STORAGE (存储)
- 表格示例: BETERM="DNA Extraction from Buffy Coat", BECAT=EXTRACTION (扩展值), BEREFID="DNA-001-Aliquot-A"
- Cite: knowledge_base/domains/BE/spec.md §BECAT + assumptions.md §1
- Follow-up: 是否需了解 RELSPEC

★ 加分: 4 个扩展值列举 + 完整 BE 域示例表格 + RELSPEC cross-domain reference

---

## ChatGPT v3 — PASS

URL: https://chatgpt.com/.../c/6a0d7d10-7640-83a8-933d-858659d91401

**Conclusion**: 可以扩展。
- BECAT 没有绑定 CDISC CT codelist, Perm Grouping Qualifier
- 给 BETERM 这类 topic-variable values 分组
- DNA/molecular biology 场景: **EXTRACTION**
- 示例表: DNA EXTRACTED → BECAT=EXTRACTION (从全血/组织样本提取 DNA), DNA PURIFIED → BECAT=EXTRACTION (纯化步骤归同类)
- 依据: BE 域覆盖 specimen actions (collection / freezing/thawing / aliquoting / transportation)
- 结论: BECAT sponsor-extensible; 建议清晰预定义全大写 controlled-vocabulary 风格, 并在 Define-XML 中描述
- Reasoning trace: "Thought for 9s" — 显示 R1 KB-grounding primary fire (variable definition + CT + assumptions lookup)

---

## Claude v3 — PASS+ ★ (paper PARTIAL → UI PASS+)

URL: https://claude.ai/chat/10cfb1dd-3459-49de-a869-39de91b478b4

**Conclusion**: **BECAT 是 sponsor-extensible 的** — SDTMIG v3.4 BE 域 spec 中 BECAT 的 CT 栏为空, 未绑定任何 CDISC 受控术语 codelist。Role: Grouping Qualifier, Core: Perm。

**R5 Premise Correction 实战体现** ★:
> "需要先纠正一个前提: COLLECTION / PREPARATION / TRANSPORT 这"三个 canonical 值" 并不是 CDISC 官方 CT 列表, 而只是 CDISC 在 SDTMIG v3.4 §6.2.2 BE 域 Examples 里反复出现的常见 sponsor 约定。CDISC 自己的 example 里就已经把 BECAT 扩展到了这三个之外的值。"

**CDISC example 中实际出现的 6 个 BECAT 值**:
- COLLECTION (Collecting), PREPARATION (Aliquoting/Flash Freezing/Thawing/Sequencing/Freezing/Concentrating), TRANSPORT (Shipping), **EXTRACTION (Extracting)**, STORING, CULTURE

**DNA / molecular biology specimen processing 场景示例** — Example 2 (cell-free RNA from plasma) 完整 9 行表:
| BESEQ | BEREFID | BETERM | BEDECOD | BECAT | 备注 |
|---|---|---|---|---|---|
| 1 | 298B1 | Collecting | COLLECTING | COLLECTION | 血样采集 |
| 2 | 298B1-1 | Extracting | EXTRACTING | EXTRACTION | 现场离心制备血浆 |
| 3 | 298B1-1 | Shipping | SHIPPING | TRANSPORT | 运至中央实验室 |
| 4 | 298R1-1R0 | Extracting | EXTRACTING | **EXTRACTION** | 实验室提取/纯化 cell-free RNA |
| 5-7 | 298R1-1R1/R2/R3 | Aliquoting | ALIQUOTING | PREPARATION | 分成 3 份 aliquot |
| 8 | 298R1-1R1 | Sequenced | SEQUENCING | PREPARATION | 1 份立即测序(归 PREPARATION 而非另建) |
| 9 | 298R1-1R2 | Frozen | FREEZING | PREPARATION | 其余冻存 |

**行业惯例扩展**: AMPLIFICATION / SEQUENCING (若不愿混 PREPARATION) / STORAGE-STORING / QC-QUALITY CONTROL / THAWING

**实践建议**:
- Define-XML 显式声明 sponsor-defined codelist (e.g. `BECAT_VALS`), 列出本研究允许的 BECAT 值
- 优先复用 CDISC example 中出现过的值 (COLLECTION/PREPARATION/TRANSPORT/EXTRACTION/STORING/CULTURE)
- BEDECOD 受 C124297 控制 — 才是"动作语义"主战场
- Cite: SDTMIG v3.4 §6.2.2 + C124297 + https://evsexplore.semantics.cancer.gov/evsexplore/

★★ **Bridge mechanism**:
- Paper-level Layer 2 KB grep miss: bundle 缺 "sponsor-extensible" 字眼显式段
- UI-level reasoning bridge:
  1. R1 KB-grounding → routing 05_mega_spec.md (BECAT row CT 空)
  2. AHP-V1 verify BECAT exists in 04_variable_index.md
  3. AHP-V2 verify Core=Perm (允许自定义)
  4. **Inference**: "CT 空 + Perm + Grouping Qualifier" → 必 sponsor-extensible
  5. R5 Premise Correction 进一步识破用户"三 canonical"前提是非 CT 列表 (Example 反复出现的 sponsor 约定)
  6. 引用 09_examples_data_high.md Example 2 完整 9 行表数据 (含 EXTRACTION 多行)
  7. Cite path-line + §6.2.2 + C124297 NCI EVS URL

**Reasoning-bridge upgrade**: paper PARTIAL → **UI PASS+** ★

---

## NotebookLM v3 — PASS

URL: https://notebooklm.google.com/notebook/2cebc5cb-1466-4788-9474-bdf2d75d2060

**Conclusion**: BECAT (Category for Biospecimen Event) | Type: Char | Role: Grouping Qualifier | Core: Perm | CT: 无 ✓

**是否 sponsor-extensible**: 是的, 允许申办方扩展; 只要扩展值遵循 single-token 受控词汇结构约定即可。
**Citation**: [1: 10_ev_history_mh_ho_be.md]

**DNA / 分子生物学场景扩展**: **EXTRACTION** (提取) 是最常见且常规使用的申办方扩展值。
**Citation**: [1: 10_ev_history_mh_ho_be.md]

**具体用例**: 例如血浆样本离心分离, 或从中提取纯化 RNA 以备后续测序使用时, 相应标本处理事件 (如 BETERM="Extracting") 的 BECAT 即记录为 EXTRACTION。
**Citation**: [2: 10_ev_history_mh_ho_be.md]

**Footer Sources**: 10_ev_history_mh_ho_be.md (bucket 10 含 BE)

★ 注: NotebookLM citation 风格保留 v1.3 footer Sources style (v3 prompt design 保留承诺验证 ✓), inline `[N: bucket.md]` chip 也在 (符合 NotebookLM native UX)

---

## 跨平台对比

- **R1 KB-grounding primary**: 4/4 平台全 fire (Claude 显式 cite §6.2.2 / Gemini cite spec.md+assumptions.md path / ChatGPT 隐式 lookup / NotebookLM bucket 10 citation chip)
- **R5 Premise Correction**: Claude 触发 (识破"三 canonical 非 CT 列表"前提) — 其他 3 平台没触发因前提没问题
- **Sponsor-extensible 关键 claim**: 4/4 平台都答 "是"
- **EXTRACTION 必命中**: 4/4 平台
- **答案深度**: Claude > Gemini > ChatGPT > NotebookLM (符合 model capability + Claude project-scope KB advantage)
