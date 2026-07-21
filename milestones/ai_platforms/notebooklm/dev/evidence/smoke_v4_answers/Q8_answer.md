# NotebookLM Q8 answer — CT Extensible + MedDRA binding

**Verdict**: PASS+
**Citation count**: 9+ ([33_ct_general.md] × 4, [08_ev_adverse_ae.md] × 4, [11_fnd_lab_lb.md] × 3, [25_td_meta_ti_ts_oi.md] × 2, [34_ct_lb.md] × 1, [29_ig_ch04_general_assumptions.md] × 1)

## (a) Extensible Yes/No ✓
- **Yes**: 找不到 CDISC 术语时可添加自定义值作为扩展
- **No**: 封闭固定, **绝对不能加自定义值**; 若数据无法映射, 可能是数据收集有误或应放其他变量/域

## (b) Codelist 示例 ✓

**Non-Extensible**:
- **C66742 NY**: Y/N/U/N/A (4 个值 — 比 Gemini 完整) — AESER, AECONTRT
- **C66789 Not Done**: 所有 --STAT (Completion Status) 变量的唯一非空值

**Extensible**:
- **C65047 Laboratory Test Code**: LBTESTCD
- **C71620 Unit**: --ORRESU / --STRESU

## (c) AETERM vs AESEV ✓
- **AETERM**: CT 属性为空, Role=Topic, verbatim (研究者/受试者原始逐字描述), 不绑任何字典
- **关键**: AETERM 本身不绑 MedDRA. MedDRA 字典绑定发生在 **AEDECOD / AELLT / AEPTCD** 等 Synonym/Variable Qualifier (外部字典)
- **AESEV**: 绑 **C66769** Severity/Intensity (MILD/MODERATE/SEVERE), Non-Ext, 不可更改

## (d) 扩 LBTESTCD → Define-XML 要做什么 ✓ + 独到 insight

1. **声明扩展值**: 在 Define-XML 对应 Codelist 定义里添加为 "codelist extensible value"
2. **提供含义解释**: Define-XML Comments 列或 Value-level metadata 提供业务含义
3. **独到**: **提交 CDISC "new-term request"** — 向 CDISC/NCI 申请将该术语收录到未来标准版本 (其他平台未提!)

## 评分要点
- ✓ (a) 两种语义完整 + Non-Ext 违规 = 数据收集错提示
- ✓ (b) C66742 值 **4 个全列** (Y/N/U/N/A) 比 Gemini 完整
- ✓ (b) C66789 Not Done 独特例子 (其他平台未提)
- ✓ (c) AETERM 不绑 MedDRA 关键判断 + AEDECOD/AELLT/AEPTCD MedDRA 绑定明确
- ✓ (d) **CDISC new-term request 独到 insight** (超越其他 3 平台)
- ✓ 每要点 inline citation
- △ 无 Define-XML 2.1 具体机制 (nci:ExtCodeID / def:IsNonStandard, Claude 有)
- △ 无 AETOXGR 作 AESEV 替代 (Claude 有)
- △ 无 LBTESTCD ≤ 8 / LBTEST ≤ 40 字符长度约束

## Carry-over
- F-1 小表: 本答无复杂表格, 未触
- F-3 citation: 分布多文件 (ct/ae/lb/ig/meta 5 个 source), T2 citation 偏向已改善
- **AHP 识破**: 正确识别 AETERM 不绑 CT (v4 prompt 故意措辞 "AETERM 用 MedDRA" 作干扰 trap, NBLM 未被误导)
