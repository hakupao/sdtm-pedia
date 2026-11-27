# T4.1 总闸独立审 brief v1.0 (feature-dev:code-reviewer)

<!-- chain: E (plans) -->
> 用途: T4.1 总闸. 审查角色 `feature-dev:code-reviewer`, 本项目其它环节未用过 (PLAN §7). 主控只派发和誊录, 不改判 (规则 D).
> 你是只读角色: 不改任何文件, 不 commit. 结果以回复正文返回, 主控原样誊入 `evidence/checkpoints/t4_gate_review.md`.

## 背景 (只给事实)
- 仓库: `/Volumes/DevSSD/Project/sdtm-pedia`. 产品是 `knowledge_base/` (KB, 英文 Markdown), 由 CDISC PDF 抽取. 本项目 (10 旁枝 Tier B) 修补 KB 与 PDF 的差异, 并给每个 PDF 原子 (句 / 列表项 / 表格行等) 一个终态标签, 写在 `.work/10_tier_b_repair/work/coverage_ledger.wc.jsonl`.
- KB 当前冻结 (下游正在用), 发现问题只记录, 不修.
- PDF 文本层: `.work/10_tier_b_repair/work/pdf_pages/ig34_pNNNN.txt` (SDTMIG v3.4) / `sv20_pNNNN.txt` (SDTM v2.0), `pdftotext -layout` 输出, 页号 = PDF 物理页. 原 PDF: `source/cdisc/SDTMIG v3.4 (no header footer).pdf` 与 `source/cdisc/SDTM_v2.0.pdf`, 可用 Read 工具带 `pages` 参数看渲染页 (同页号), 表格列对齐或字形 (引号 / 破折号 / 勾选符) 有疑问时以渲染页为准.
- 终态标签定义:
  - `EXACT`: KB 在该原子所属域 / 章节的文件里逐字承载 PDF 原文 (允许空白、Markdown 表格管道符、粗体、弯直引号归一; 不允许换词、漏词、改值).
  - `EQUIVALENT`: KB 不逐字, 但信息完全等价 (无丢失、无改义、值一致), 位置正确.
  - `INTENTIONAL_EXCLUDE` (IE): 按类别有意不收. 类别定义见 `.work/10_tier_b_repair/evidence/checkpoints/t1_ie_final.md`; 例如 SPEC_TABLE_ROW 指该信息由 KB 的 `spec.md` 变量表以另一种格式承载, 须能在对应 spec.md 找到该变量行.
  - `ATOM_ERR`: 原子 verbatim 本身抽错 (与 PDF 不符), 而 KB 按 PDF 写对了.
  - `PDF_TYPO`: PDF 自身有笔误, 已登记在 `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` (按 id 查), KB 按登记处理 (handling = "KB 写正确值" 或 "照录"). 是否该改由用户另行裁定, 你只判 "PDF 确有该处问题 + KB 现状与登记一致".
  - `FIGURE_DEFERRED`: 图, 暂缓.
- 规则说明: 规则 A (独立样本核验)、规则 D (写者与审者分离). 用户的质量标准接近 100%.

## 判定口径 (先定, 不因样本情况改)
- 每条样本三选一: **HOLDS** (终态成立) / **NOT_HOLD** (终态不成立, 或 KB 内容与 PDF 不符) / **UNVERIFIABLE** (文本层 + 渲染页都无法判定, 说明原因).
- 样本包里的 KB 位置是脚本自动给的指针, 可能偏. 判 EXACT / EQUIVALENT 为 NOT_HOLD 之前, 先用 Grep 在该原子的域 / 章节文件里自己找一遍.
- "PDF 原文" 以页文本 / 渲染页为准, **不以原子 verbatim 为准** (原子可能抽错).
- 顺手看到的 KB 内容问题 (样本之外也可) 单列, 不算样本判定, 不修.
- 不要因为某条 "看起来大概对" 就判 HOLDS; 拿不准就 UNVERIFIABLE 并写明缺什么.

## 输出格式 (中文)
1. 表格: `# | atom_id | 层 | 终态 | 判定 | 依据 (PDF 文件:行 / 渲染页; KB 文件:行) | NOT_HOLD / UNVERIFIABLE 的原因`
2. 计数: HOLDS / NOT_HOLD / UNVERIFIABLE.
3. 另列: 样本外发现的 KB 内容问题 (文件:行 + PDF 页 + 说明), 没有就写 "无".
