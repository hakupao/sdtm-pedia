# Q8 (D1 — CT Extensible vs Non-Extensible)

> Date: 2026-04-22 / Account: bojiang.zhang.0904@gmail.com / Fresh chat

---

## 题

CDISC Controlled Terminology 的每个 codelist 有 Extensible = Yes/No 属性. 请回答:
- (a) Extensible=Yes 和 Extensible=No 语义区别是什么 (sponsor 能否加自己的值)?
- (b) 举 2 个 Non-Extensible 的常见 codelist 例子 (必须完全按 CDISC 用), 和 2 个 Extensible 的例子 (允许扩);
- (c) AETERM 这种变量 "CT 值" 语义和 AESEV (Non-Extensible) 有什么区别 (AETERM 实际用 MedDRA 字典, 不是 CDISC CT);
- (d) 如果 sponsor 自己扩 LBTESTCD, Define-XML 要做什么?

## NotebookLM 答 (full text)

在 CDISC 控制术语 (Controlled Terminology, CT) 中, Codelist 的 Extensible 属性决定了该术语表是否封闭。以下是针对您问题的详细解答:

### (a) Extensible=Yes 和 Extensible=No 的语义区别

- **Extensible = Yes (可扩展)**: 如果 CDISC 现有的受控术语不能涵盖研究中收集到的特定概念, Sponsor (申办方) 允许向该 codelist 添加自定义的值 (Custom terms) [25_td_meta_ti_ts_oi.md, 29_ig_ch04_general_assumptions.md]。添加的新值必须在 Define-XML 的元数据中进行解释和说明 [25_td_meta_ti_ts_oi.md]。
- **Extensible = No (不可扩展)**: 该 Codelist 是完全封闭的, Sponsor 绝对不能添加任何自定义值。如果数据落在此列表中, 必须且只能使用 CDISC 预先发布在标准中的全拼有效值 [33_ct_general.md, 36_ct_specialized_micro_oncology_pk_is_cp.md]。

### (b) 常见的 Codelist 例子

**2 个 Non-Extensible (不可扩展, 必须完全按 CDISC 用) 的常见例子**:
- **No Yes Response (C-code: C66742)**: 用于 AESER、AECONTRT、AESCAN 等标志类变量 [08_ev_adverse_ae.md, 33_ct_general.md]。只允许使用预设的特定值: Y / N / U / NA, 绝对不允许使用变体或自行扩充 [33_ct_general.md]。
- **Not Done (C-code: C66789)**: 用于跨域的 `--STAT` (Completion Status) 变量 [06_int_concomitant_cm_ag_ml.md, 33_ct_general.md]。唯一非空的受控有效值为 `NOT DONE` [11_fnd_lab_lb.md]。

**2 个 Extensible (可扩展) 的常见例子**:
- **Laboratory Test Code (C-code: C65047)**: 用于 `LBTESTCD` (实验室检查短名) [11_fnd_lab_lb.md, 34_ct_lb.md]。由于实验室检查项目和新型生物标志物不断增多, CDISC 无法穷举, 因此允许 Sponsor 在遵守命名规则 (最大 8 字符、不能以数字开头等) 的前提下扩充新测试代码 [11_fnd_lab_lb.md]。
- **Anatomical Location (C-code: C74456)**: 用于 `--LOC` (如 AELOC, EXLOC, CELOC) 变量 [08_ev_adverse_ae.md, 33_ct_general.md]。如果研究中涉及尚未被 CDISC 囊括的特定解剖学位置, Sponsor 可以扩展该列表 [33_ct_general.md]。

### (c) AETERM 与 AESEV 在术语语义上的区别

**AETERM (Reported Term for the Adverse Event)**:
- 语义与属性: Label 为 Reported Term for the Adverse Event, Type = Char, Role = Topic, Core = Req [08_ev_adverse_ae.md]。
- 值的来源: AETERM **本身没有绑定的 CDISC CT**, 它存储的是研究者在 CRF (Case Report Form) 上直接填写的原始/逐字文本 (verbatim text) [08_ev_adverse_ae.md]。
- 字典映射: 针对 AETERM 收集的自由文本, 会使用**外部医学字典 (如 MedDRA)** 进行标准化编码, 并将 Preferred Term (PT) 存入 AEDECOD (Core = Req) 中 [08_ev_adverse_ae.md]。**外部字典属于 External Dictionary, 不在 CDISC CT 的管辖与 Extensible 属性范畴内**。

**AESEV (Severity/Intensity)**:
- 语义与属性: Label 为 Severity/Intensity, Type = Char, Role = Record Qualifier, Core = Perm [08_ev_adverse_ae.md]。
- 值的来源: 它严格绑定 CDISC 的固有 CT Codelist Severity/Intensity Scale for Adverse Events (C-code: **C66769**) [08_ev_adverse_ae.md]。它的值受到 CDISC CT 管辖, Sponsor 必须拼写出规范的完整单词: `MILD` / `MODERATE` / `SEVERE` [08_ev_adverse_ae.md]。

### (d) 若 Sponsor 扩展了 LBTESTCD, 在 Define-XML 中需要做什么?

如果 Sponsor 针对 LBTESTCD 添加了 CDISC CT 中尚不存在的自定义值 (Custom parameters), 必须在提交的数据元数据中执行以下操作:
1. **声明完整的值集 (Permissible Value Set)**: 在 Define-XML 文档中, 必须将该研究实际用到的所有术语 (包括 CDISC 既有值和 Sponsor 自定义扩展的新值) 全部包含在提供的受控术语列表内 [29_ig_ch04_general_assumptions.md]。
2. **定义新增参数含义 (Explain in Metadata)**: 在 Define-XML 的数据集元数据 (metadata) 层面, 必须明确解释 Sponsor 自定义添加的任何新测试代码 (LBTESTCD) 和对应名称 (LBTEST) 的具体医学和业务含义 [25_td_meta_ti_ts_oi.md]。
3. **价值级别元数据 (Value-level Metadata)**: 如果是通过引入通用的 (Generic) 自定义测试代码来表征特殊的实验, 必须通过 natural key (自然键) 或 value-level metadata (值级别元数据) 明确指出该 Test 的唯一性规则, 以及它依赖哪些 Qualifier 变量 (如 LBSPEC, LBMETHOD 等) 来共同赋予其完整含义 [29_ig_ch04_general_assumptions.md]。

## Verdict

| Criterion | Required | Got | Status |
|---|---|---|:---:|
| (a) Yes/No 语义反向 | Yes 允许 sponsor 加, No 禁加 | 明确正反语义 + Define-XML 解释要求 | ✅ |
| (b) 2 Non-Ext 例子 | NY/AESEV/LBNRIND 任 2 | NY (C66742) + Not Done (C66789) ✓ | ✅ |
| (b) 2 Ext 例子 | LBTESTCD/MBTESTCD/ROUTE 任 2 | LBTESTCD (C65047) + Anatomical Location (C74456) ✓ | ✅ |
| (c) AETERM = MedDRA 不是 CDISC CT | 明确 MedDRA 外部字典 | "AETERM 本身没有绑定的 CDISC CT" + "外部医学字典 (如 MedDRA)" + AEDECOD PT + "外部字典属于 External Dictionary, 不在 CDISC CT 的管辖" | ✅ |
| (c) AESEV = C66769 Non-Ext 三档 | C66769 + MILD/MODERATE/SEVERE | C66769 + 必须全拼 + 三档 ✓ | ✅ |
| (d) Define-XML 三步 | extension values + sponsor codelist ref | 3 步: Permissible Value Set + Metadata 解释 + Value-level Metadata | ✅ |

**Verdict**: ✅ **PASS** (1 / 1) — 6 项判据全中。Yes/No 正反语义清; AETERM/MedDRA 边界明文 ("外部字典不在 CDISC CT 管辖"); AESEV C66769 + 三档全拼; Define-XML 三步骤齐 (Value Set + Metadata 解释 + Value-level Metadata)。加分: NY C66742 / Not Done C66789 / LBTESTCD C65047 / Anatomical Location C74456 / AESEV C66769 五个 C-code 全对 + LBTESTCD 命名规则 (8 字符上限 + 不能数字开头) 业务细节。无 FAIL 触发。
