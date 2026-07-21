# Q8 — Gemini SDTM Expert 回答 (A8 — CT Extensible vs Non-Extensible)

> 期望核心: (a) Ext=Yes 可扩 / No 不可扩 + (b) 2 Non-Ext + 2 Ext 例子 + (c) AETERM (MedDRA free text) vs AESEV (CDISC CT Non-Ext) 区别 + (d) Define-XML ExtendedValue="Yes" 标记
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/52ffd5f7542e1ed7
> 时间: 2026-04-22
> Mode: Pro

## 完整回答

这是关于 CDISC 数据标准化中核心的"受控术语（Controlled Terminology, CT）"机制的经典问题。

### (a) Extensible=Yes 与 Extensible=No 的语义区别

CDISC 控制术语表中的每个 codelist 都有一个 Extensible（可扩展性）属性：

- **Extensible = Yes (可扩充)**: 当申办方在官方 CT 列表中找不到对应术语时，允许添加自定义值 (Sponsor-defined terms). 前提: 新增值必须遵循该 codelist 的命名和格式规范 (如 8 字符限制), 且不能与现有标准术语语义重叠.
- **Extensible = No (不可扩充)**: 绝对不允许申办方添加自定义值. 数据必须映射到现有 CDISC 官方术语. 若无法映射, 通常意味着收集设计缺陷.

### (b) Codelist 示例

**2 个 Non-Extensible 的常见 Codelist**:

1. **Severity/Intensity** (`C66769`) — 用于 AESEV. 只能映射到 MILD / MODERATE / SEVERE.
2. **Yes/No Response** (`C66742`) — 用于 AESER (是否严重) 等 Flag 变量. 只能 Y / N 或 空, 不允许 MAYBE/UNKNOWN.

**2 个 Extensible 的常见 Codelist**:

1. **Laboratory Test Code (LBTESTCD)** — 检验技术日新月异, 申办方引入新 Biomarker 时可自创 ≤8 字符的 Code.
2. **Vital Signs Test Code (VSTESTCD)** — 特殊体征测量项目未被收录时, 可依规扩充.

### (c) AETERM 与 AESEV 的 CT 语义区别

- **AETERM** (Reported Term for the Adverse Event): 自由文本 (Free Text) 变量, Core=Req. 原样照录研究者在 CRF/EDC 填写的原始事件描述, **完全没有 CDISC CT Codelist 约束**. 标准化归类依赖 AEDECOD, 使用外部标准医学词典 (MedDRA), 而不是 CDISC 维护的 CT.
- **AESEV** (Severity/Intensity): 分类标识变量, Core=Perm. 严格绑定 CDISC CT 的 **Non-Extensible codelist** (C66769). 对不良事件烈度标准化分级, 无自由发挥空间.

### (d) 若申办方扩充 LBTESTCD, Define-XML 要做什么?

扩充 Extensible=Yes 变量 (如 LBTESTCD) 时, 必须在 Define-XML 中向监管机构透明化声明:

- **添加新建项**: 在 Define-XML 对应的 `<CodeList>` 结构下, 加入代表该扩充术语的 `<CodeListItem>`.
- **标记扩展属性**: 对自建的、不在官方 NCI 列表中的项, 必须使用属性 `ExtendedValue="Yes"` 明确标记 (Define-XML v2.0/v2.1). 这让 Pinnacle 21 等审评工具和审评员清晰识别哪些术语是官方标准, 哪些是申办方补充.

### 源路径溯源

- `knowledge_base/domains/AE/spec.md` §AETERM, §AESEV, §AEDECOD
- `knowledge_base/domains/LB/spec.md` §LBTESTCD
- Define-XML v2.1 Specification + ICH MedDRA 指南 (边界外围)
- NCI EVS Browser (CT 查询)

## 判据对齐

| 维度 | 期望 | 实际 | Hit |
|------|------|------|-----|
| (a) Ext=Yes/No 语义 | Yes 可扩 / No 不可扩 | Yes 可扩 (+ 命名规范 + 8字符限制) / No 必须映射 | ✅ |
| (b) 2 Non-Ext 例 | AESEV/AESER 等 Non-Ext | AESEV C66769 + AESER C66742 | ✅ |
| (b) 2 Ext 例 | LBTESTCD/VSTESTCD 等 Ext | LBTESTCD + VSTESTCD | ✅ |
| (c) AETERM vs AESEV | AETERM=free text (MedDRA via AEDECOD), AESEV=Non-Ext CT | AETERM=Req free text + AEDECOD MedDRA, AESEV=Non-Ext C66769 | ✅ (minor: AESEV Core 实际是 Exp 非 Perm, 但核心 CT 边界对) |
| (d) Define-XML ExtendedValue | `<CodeListItem>` + ExtendedValue="Yes" | CodeListItem + ExtendedValue="Yes" (v2.0/v2.1) | ✅ |

## Verdict

**PASS** — 全部 4 子问题 (a/b/c/d) 精准命中期望. Ext=Yes/No 语义准确 + 4 个 codelist 例子对齐 (Non-Ext: C66769/C66742; Ext: LBTESTCD/VSTESTCD) + AETERM (free text MedDRA) 和 AESEV (CT Non-Ext) 边界清楚 + Define-XML ExtendedValue="Yes" 标记正确. 唯一 minor: AESEV Core 写 Perm 而实际 Exp, 但不影响 CT 边界核心判据.

- 04 引用: 无 (业务 CT 层, 非 04 业务弹药包直接触发)
- CO-2 触发: 1 次 (EVS Browser link, "不 inline 完整术语列表"), 合理
- Score: 1 / 1
