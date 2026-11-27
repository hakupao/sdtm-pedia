# T4.1 第二轮补检 brief v1.0 (跨文档指针 / 已登记笔误的同类原子 / PDF_TYPO 补抽)

<!-- chain: E (plans) -->
> 用途: 对主控补检产出的独立审查 (REVIEW_B) 指出三处没覆盖到: ① 旧标签的台账指针指向 "另一份文档" 的 KB 文件、抽样没抽到; ② 已登记 PDF 笔误影响到的原子里, 有的标签仍是 EXACT / EQUIVALENT; ③ 终态 PDF_TYPO 的原子绝大多数没人独立看过.
> 审查角色 `oh-my-claudecode:tracer` (opus), 只读. **先完整读** `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` 的 "背景" 与 "判定口径" 两节 (标签定义、PDF / KB 怎么看、只读约束、输出格式都沿用), 再读本文件.
> 判定口径与后果在派发前写死, 不因结果改.

## 三层各核什么

### XDOC (27 条, 全检) — 终态 EXACT / EQUIVALENT, 06 旧标签, 本项目没改过
台账给这些原子配的 KB 位置在**另一份文档**的文件里: SDTMIG (`ig34_*`) 的原子被配到 `knowledge_base/model/` (那是 SDTM v2.0 的内容); 或 SDTM v2.0 (`sv20_*`) 的原子被配到 `knowledge_base/chapters/` / `domains/` (那是 SDTMIG 的内容). 含标题类原子.
要核: 在该原子**自己所属文档**的 KB 文件里 (SDTMIG → `chapters/`、`domains/<域>/`; SDTM v2.0 → `model/`), PDF 这条内容有没有、对不对、位置对不对. 不要因为另一份文档里有相同的字就算成立.
- **HOLDS**: 自己文档的 KB 文件里按终态定义成立 (EXACT 逐字 / EQUIVALENT 等价; 标题类 = 有对应的节标题, 节号与标题文字一致, KB 追加的域代码后缀如 "(TE)" 按已登记口径不算不同).
- **HOLDS_AS_EQUIV**: 终态写 EXACT, 内容都在但不逐字.
- **NOT_HOLD_R1**: 仅用于 SDTM v2.0 变量表行 / 表头 — KB 精简列一致, PDF 其它列的非空内容 KB 本表没收 (同 `t4_q9_extension_v1.0.md` 的定义).
- **NOT_HOLD_XDOC**: 内容只在另一份文档的 KB 文件里有, 自己文档的 KB 文件里没有 (或没有对应的节) → 旧标签是跨文档误配. 写明 PDF 是哪一节、KB 自己文档里缺什么.
- **NOT_HOLD**: 其它不成立 (值不同 / 改义 / 位置错). **UNVERIFIABLE**: 判不了, 写明缺什么.

### TYPO_SIB (63 条, 全检) — 终态 EXACT / EQUIVALENT, 与某条 "KB 写正确值" 的 PDF 笔误登记同页
每条样本的 "登记" 行给出了候选的登记 id (PDF 写什么、KB 写什么). 候选是脚本按 "原子文字含 KB 的改正值 + 与登记所在 KB 行高度重合" 筛的, **可能筛错** (登记的笔误也许在同一行的别的原子、别的格, 或者在叙述句里而这条是表格行).
要核: 看 PDF 渲染页 / 文本层, 这条原子对应的那一处, PDF 印的是不是登记里的笔误写法, 而 KB 写的是改正值.
- **TYPO_AFFECTED**: 是. 这条原子对应的 PDF 原文含该笔误, KB 是改正值 → KB 与 PDF 在这里有差异, 差异 = 已登记笔误 → 现标签 EXACT / EQUIVALENT 不准, 应为 PDF_TYPO. 写出登记 id、PDF 原文片段 (≤ 10 词)、KB 文件:行.
- **NOT_AFFECTED**: 不是. 这条原子对应的 PDF 原文与 KB 一致 (笔误在别处), 现标签按定义成立. 写一句为什么 (笔误实际在哪).
- **NOT_HOLD**: 与登记无关的其它不成立 (KB 缺内容 / 值不同且未登记 / 位置错). **UNVERIFIABLE**: 判不了.
注意: 原子 verbatim 是抽取物; 有的原子抽出来的文字本身就等于 KB 的改正值 (抽取时被 "顺手改对" 了), 所以必须看 PDF 页, 不能看原子.

### PDF_TYPO (45 条, 分层抽样 seed 20261132: 三条判定规则各 15) — 终态 PDF_TYPO
- **HOLDS**: ① PDF 该处确有登记所说的问题 (看渲染页 / 文本层); ② KB 现状与登记的处理方式一致 ("KB 写正确值" → KB 是改正值; "照录" / "照录+T4" → KB 与 PDF 相同); ③ 除登记的那一处外, 这条原子的其余内容 KB 与 PDF 一致.
- **NOT_HOLD**: 上面任一条不成立 (PDF 其实没这个问题 / KB 与登记不符 / 其余内容另有差异). 写明是哪一条.
- **UNVERIFIABLE**: 判不了. 登记 id 在样本的 "登记" / "PDF 笔误登记" 行; 登记表 `work/t2_pdf_typo_registry.jsonl` (按 `id` 查).
是否该按登记处理 (改还是照录) 由用户另行裁定, 你只判 "PDF 确有该处问题 + KB 现状与登记一致 + 其余一致".

## 后果 (主控派发前写死)
- NOT_HOLD_XDOC / NOT_HOLD_R1 / TYPO_AFFECTED → 并入待改标签清单 (`evidence/checkpoints/t4_relabel_pending.md`), 交主人裁定; 主控不改台账.
- NOT_HOLD → 记 KB 观察项 (KB 冻结不修), 上报.
- PDF_TYPO 抽样出现 NOT_HOLD ≥ 1 → 上报主人决定是否对未审的 PDF_TYPO 原子全检; 0 条 → 报告 "45 抽 0 错" 及其置信上界, 不写成全检.
- 任一层出现 UNVERIFIABLE → 该层不算通过, 逐条列出.

## 输出
同补检 brief 的输出格式 (文件头含真实 `date -u` 时间 / 看过的渲染页 / 表格 / 计数 / 样本外发现); 表格 `#` 用样本包里的 R 编号; 计数按本层的判定类别列. 结果只写进派发消息指定的那一个文件.
