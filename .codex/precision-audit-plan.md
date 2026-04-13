# Precision Audit Plan

## Objective

判断“源文件 -> Markdown 知识库”的转换过程中，是否发生了会影响后续使用的数据内容精度丢失。

这里的“精度丢失”包括：

- 漏段落、漏条目、漏示例
- 表格行列缺失
- 数值、日期、变量名、代码值被改写
- 层级关系丢失（编号、子条目、共享示例关系）
- 交叉引用被删弱

## What Looks Safe Already

### 1. spec.md

`spec.md` 由 xlsx 自动生成，并且已有精确比对脚本：

- 脚本：`.work/scripts/validate_spec.py`
- 能校验：
  - domain 是否齐全
  - variable 是否齐全
  - 字段值是否逐项一致
  - 变量顺序是否一致

结论：

- 这部分精度风险最低
- 后续 review 只需复跑脚本并补一份结果快照

### 2. assumptions/examples 的抽样状态

已做小规模人工抽查：

- `DM assumptions/examples` 对照 PDF p65-78
- `EX examples` 对照 PDF p111-120

抽查结论：

- 目前没看到明显的数值/date/变量名丢失
- 共享示例（`EX`/`EC`）的说明和主要表格都在
- 但这只能说明“样本暂无明显问题”，不能替代系统化审计

## Main Risk Area

### PDF -> Markdown

当前最大风险集中在：

- `knowledge_base/domains/*/assumptions.md`
- `knowledge_base/domains/*/examples.md`

原因：

- 内容来自 PDF，而不是结构化 xlsx
- 提取中包含长段落、深层编号、CRF 文本、宽表格、共享 example
- 仓库里目前没有自动验证脚本

## Proposed Audit Strategy

### Phase A: Inventory Audit

目的：先确认“该有的文件”是否都在。

检查项：

- 每个 domain 是否存在 `spec.md`
- 已完成 domain 是否同时存在 `assumptions.md` 和 `examples.md`
- `worklog` / `PROGRESS.md` / 实际文件数是否一致

当前已发现：

- 实际未补全 domain 为 `13` 个
- 与 `worklog` 描述存在偏差

### Phase B: terminology Exact Audit

目的：给 `terminology/` 补上和 `spec.md` 同等级别的自动校验。

建议新增脚本：

- `.work/scripts/validate_terminology.py`

建议校验内容：

- codelist 数量是否一致
- 每个 codelist 的名称、extensible 值是否一致
- term 数量是否一致
- 每个 term 的 code / submission value / synonym / definition 是否一致
- 分片输出后，是否出现重复或遗漏

### Phase C: assumptions Structural Audit

目的：验证 PDF 规则文本没有漏项、错项、层级降级。

建议新增脚本：

- `.work/scripts/audit_assumptions_pdf_vs_md.py`

建议方法：

1. 用 `pdftotext` 按 `page_index.json` 抽出 assumption 页段
2. 对 PDF 文本和 markdown 做 normalization
3. 提取编号结构并比较：
   - 主条目数量
   - 子条目层级
   - 关键锚点句是否都存在
4. 输出：
   - `missing_sections`
   - `numbering_mismatches`
   - `low_similarity_domains`

注意：

- 这一阶段重点不是“逐字完全相同”，而是“信息项和层级不能丢”

### Phase D: examples Data Audit

目的：验证示例数据表没有漏列、漏行、改值。

建议新增脚本：

- `.work/scripts/audit_examples_pdf_vs_md.py`

建议方法：

1. 用 `pdftotext -layout` 提取 example 页段
2. 从 markdown 中提取：
   - 示例标题
   - 数据集标题（如 `dm.xpt`, `ex.xpt`, `relrec.xpt`）
   - 表头
   - 表格行数
   - 高频关键 token（变量名、日期、药物名、代码值）
3. 建立“签名比对”而不是脆弱的逐字比对：
   - 表头字段集合
   - row 数
   - 关键值集合
   - `Example N` 数量
4. 对高风险 domain 单独做人工复核：
   - `DM`
   - `DS`
   - `EX` / `EC`
   - `MB` / `MS`
   - `PC` / `PP`
   - `RS`
   - `FA`

### Phase E: Manual Review Lane

目的：把自动审计筛出来的疑点人工确认掉。

人工优先检查：

- 宽表格
- 跨页表格
- 共享 examples
- 深层编号规则
- 带 CRF 说明的大段 prose

人工 review 输出位置：

- `.work/findings.md`

## Recommended Execution Order

1. 先修正文档口径，明确“哪些 domain 真正已完成”
2. 复跑 `validate_spec.py`
3. 新增 `validate_terminology.py`
4. 新增 `audit_assumptions_pdf_vs_md.py`
5. 新增 `audit_examples_pdf_vs_md.py`
6. 根据审计结果做人工复核和修正

## Success Criteria

满足以下条件，才能说“当前知识库没有明显精度丢失风险”：

- `spec.md` 全量通过自动校验
- `terminology/` 全量通过自动校验
- `assumptions/examples` 全量完成 inventory 对账
- PDF 审计脚本没有高风险疑点，或疑点已人工关闭
- `.work/findings.md` 中所有问题都已定性为“已修复”或“可接受差异”

## Immediate Next Step

最值得马上做的不是继续盲目补内容，而是先补“验证器”。

原因：

- 目前已经生成了大量产物
- 如果验证能力滞后，后面再返工成本会更高
- 审计器补齐后，后续批次 10-11、Phase 4-5 都能直接复用
