# Gemini Gems — Q12 (R1 smoke v4.0)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q12)
> **执行时间**: 2026-04-22 晚 10:51 PM
> **执行者**: Bojiang + claude cowork MCP Chrome (type_text + Send click)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/835d06cfd12944e9
> **Gem**: SDTM Expert (v5 system prompt, 4-file KB)
> **Mode**: Pro
> **题类**: Q12 — CT 版本锁定 (bonus track)

---

## 题目原文

一个 3 年期临床试验, 从 2022 启动到 2025 DBL (database lock). 期间 CDISC 每季度发布 CT release. 请说明: (a) 这个试验锁用哪个 CT 版本 (start 时 / ongoing / DBL 时)? (b) 锁定 CT 版本的机制是什么 (Define-XML 哪个字段)? (c) AETERM 用 MedDRA 字典, MedDRA v25→v27 会不会影响 AE submission? (d) 如果 DBL 时发现某 CT codelist 已被 retire/alias, 怎么处理?

---

## 模型 raw 回答 (DOM readback)

在一个为期 3 年（2022-2025）的临床试验中，关于受控术语（CT）版本、MedDRA 版本切换以及术语处理的规则如下：

### (a) 试验锁用的 CT 版本 (Start / Ongoing / DBL)

根据 CDISC 的一般建议和行业惯例：
- **Start 时**: 通常选择研究开始时最新发布的 CT 版本作为基准版本
- **Ongoing 期间**: CDISC 每季度发布一次 CT 更新，但试验**不强制**实时同步每一个季度版本。在研究进行中，申办者通常保持版本稳定以减少数据处理成本
- **DBL (数据库锁定) 时**: 在锁定和提交前，通常建议将 CT 版本更新至尽可能新的版本，或者至少是一个符合监管机构当前接收标准的版本。FDA 和 PMDA 等机构通常会在《Data Standards Catalog》中列出支持的版本范围

### (b) 锁定 CT 版本的机制 (Define-XML 字段)

在 Define-XML 中，锁定和声明 CT 版本的核心机制:
- **CodeList 元素**: 定义了变量引用的具体术语表
- **ExternalCodeList 属性**: 对于 MedDRA 或 WHODrug 等外部字典，通过该属性的 **Dictionary** (字典名) 和 **Version** (版本号) 字段明确锁定版本
- **EnumeratedItem / CodeListItem**: 列出具体的术语值，确保提交数据与 Define 中定义的术语一致

### (c) MedDRA v25→v27 对 AE 提交的影响

**会产生影响**:
- **编码差异**: MedDRA 每半年更新一次, v25 到 v27 期间会有新的术语添加、旧术语的 PT 属性变更或 SOC 分类调整
- **--DECOD 一致性**: SDTM 要求 --DECOD 必须填充字典的首选术语 (PT). 如果版本升级导致受试者的原始术语 (Verbatim) 映射到了不同的 PT, 则需要重新编码以确保整个数据集的一致性
- **监管要求**: 监管机构通常要求在同一笔提交中，所有受试者的 AE 编码必须基于**同一版本**的 MedDRA

### (d) DBL 时发现某 CT codelist 已被 retire/alias 的处理

- **优先使用新版本**: 如果时间允许, 建议按照最新的 CDISC CT 发布说明进行映射转换, 使用新的有效 Term
- **保持追溯性**: 如果决定沿用旧版本 (因已在早期 Define 中锁定), 需在 **Reviewer's Guide (nSDRG)** 中详细说明理由, 解释该术语在研究开始时是有效的
- **Define-XML 声明**: 无论如何处理, Define-XML 必须准确反映数据中实际使用的 Term. 如果数据中使用了已退休的术语, Define-XML 的 Metadata 必须与其匹配, 以通过自动化校验 (如 Pinnacle 21)

**源路径**:
- `knowledge_base/chapters/ch01_introduction.md` §1.3 (Relationship to Prior CDISC Documents)
- `knowledge_base/chapters/ch04_general_assumptions.md` §4.3 (Coding and Controlled Terminology Assumptions)
- `knowledge_base/chapters/ch10_appendices.md` §Appendix C (Controlled Terminology)
- `knowledge_base/domains/DM/spec.md` (Define-XML mapping guidance)

**Citation 数**: 4 source paths

---

## Self-score verdict

- **Verdict**: **PASS** (bonus track 额外分, 4 分支全中)
- **对照 PASS 判据**:
  - (a) ✓ Start baseline + Ongoing 不强制同步 + DBL 更新至最新 + 符合 Data Standards Catalog. 判据 "通常锁 DBL 时最新 CT, 整个 submission 单一版本" 覆盖
  - (b) ✓ Define-XML CodeList + **ExternalCodeList Dictionary + Version** 锁定 + EnumeratedItem. 判据 "<CodeList> 引用 specific CDISC CT release date" 覆盖, 含外部字典机制细节
  - (c) ✓ 编码差异 + PT 变更 + SOC 调整 + --DECOD Verbatim→PT 重新编码 + **监管要求同一版本** ✓ (匹配判据 "所有 AE 应 recode 到统一版本")
  - (d) ✓ 优先 remap 新版本 + 沿用旧版本需 nSDRG 说明 + Define-XML 必须反映实际使用 + Pinnacle 21 校验匹配. 判据 "旧值保留 Reviewers Guide 说明" + "remap 所有相关值" 都覆盖
- **触发 FAIL 判据?** 无
  - ✗ 未混用多个 CT 版本 (说"同一版本")
  - ✗ 未混 CDISC CT 和 MedDRA (分别处理)
  - ✗ Define-XML 作用充分提
  - ✗ 未说 CT retire 值直接删
- **加分**: 无 (非 AHP)
- **F-* carry-over**:
  - Gemini 3.1 Pro 在 supplemental topics (Q11/Q12) 表现**持续意外**超 4-file KB scope, 预期 FAIL 的 bonus track 两题都 PASS
  - 干净无 extended reasoning 暴露
  - 4 source paths 列明 (Gemini 特性, 无 inline citation 编号)
