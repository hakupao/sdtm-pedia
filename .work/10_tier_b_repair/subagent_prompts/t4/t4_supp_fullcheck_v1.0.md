# T4.1 补检 (总闸 attempt 2 缺口: "0 抽中" 各类全检) brief v1.0

<!-- chain: E (plans) -->
> 用途: 关闭总闸 attempt 1/2 证据层审查者点名的抽样缺口. 审查角色 `oh-my-claudecode:tracer` (opus), 与产生这些标签的角色 (T1 scientist / critic, T2/T3 executor, 各批 code-reviewer / verifier) 及总闸角色 (`feature-dev:code-reviewer`) 都不同 (规则 D).
> 你是**只读**角色: 不改 `knowledge_base/`、台账、脚本、其它证据, 不 git add / commit. **唯一允许写的文件**是派发消息里指定的那一个结果文件.
> 派发前判定口径已写死 (本文件), 不因结果改.

## 背景 (只给事实)
- 仓库: `/Volumes/DevSSD/Project/sdtm-pedia`. 产品是 `knowledge_base/` (KB, 英文 Markdown), 由 CDISC PDF 抽取. 本项目给每个 PDF 原子 (句 / 列表项 / 表格行 / 图) 一个终态标签, 写在 `.work/10_tier_b_repair/work/coverage_ledger.wc.jsonl`.
- **KB 冻结** (下游正在用这份内容): 发现问题只记录, 不修.
- PDF 文本层: `.work/10_tier_b_repair/work/pdf_pages/ig34_pNNNN.txt` (SDTMIG v3.4) / `sv20_pNNNN.txt` (SDTM v2.0), `pdftotext -layout` 输出, 页号 = PDF 物理页. 原 PDF: `source/cdisc/SDTMIG v3.4 (no header footer).pdf` 与 `source/cdisc/SDTM_v2.0.pdf`, 可用 Read 工具带 `pages` 参数看渲染页 (同页号); 表格列对齐、字形、图的内容以渲染页为准. 需要放大可用 `pdftoppm -r 250 -f N -l N -png` 输出到你的临时目录 (不要写进仓库).
- 样本包里的 "原子 verbatim" 是 LLM 抽取物, 可能抽错, **不是真值**; "KB 现文" 指针是脚本自动给的, 可能偏 — 判 NOT_HOLD 之前必须自己在该原子所属域 / 章节文件里 Grep 找一遍.
- 终态标签定义:
  - `EXACT`: KB 在该原子所属域 / 章节的文件里逐字承载 PDF 原文 (允许空白、Markdown 表格管道符、粗体、弯直引号归一; 不允许换词、漏词、改值).
  - `EQUIVALENT`: KB 不逐字, 但信息完全等价 (无丢失、无改义、值一致), 位置正确.
  - `ATOM_ERR`: 原子 verbatim 本身抽错 (与 PDF 不符), 而 KB 按 PDF 写对了. 两半都要核: ① 原子 ≠ PDF; ② KB = PDF.
  - `PDF_TYPO`: PDF 自身有笔误, 已登记在 `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl`, KB 按登记处理.
  - `FIGURE_DEFERRED`: 该原子是 PDF 里的**图** (图片 / 示意图, 文字层抽不出其内容), 暂缓, 不要求 KB 承载图本身.

## 各层要核什么
| 层 | 终态 | 要核的事 |
|---|---|---|
| `PRE_EXISTING` | EXACT (06 旧标签, 本项目未改) | 这 58 条是指纹复验 (`scripts/t3/t3_direct_hit.py`) 在现 KB 和 T2 前 KB 上都**命中不了**的旧 EXACT. 核: PDF 该处内容 KB 是否承载、值是否一致、位置是否对. 判定用下面四选一 |
| `FIG` | FIGURE_DEFERRED | ① 看渲染页确认该原子确实是图 (不是普通正文 / 表格被误当成图); ② 记录 KB 对应位置现在怎么处理 (无 / 图题文字 / Mermaid / 文字描述); ③ 若 KB 有 Mermaid 或文字再现, 核其内容与图是否矛盾 (矛盾 → NOT_HOLD 并说明; 只是没画 → 不算错) |
| `TRIAGE_ATOM_ERR`, `RULE_C7-K4-rereview` | ATOM_ERR | 两半都核 (原子 ≠ PDF; KB = PDF). 表格行要逐格 |
| `TRIAGE_RELOCATE`, `RULE_live-hit(was-IE-ack)` | EXACT | KB 逐字承载, 且在该原子所属节 / 域的正确文件里 |
| `RULE_T1-two-agent+T2-rework`, `RULE_T1-two-agent`, `RULE_T2-fix+deltaRereviewPASS+auditPASS`, `RULE_C1-manual-PDF+KB` | EQUIVALENT | KB 非逐字但信息完全等价: 逐项列出 PDF 原文的信息点, 确认 KB 一个不少、值一致、无改义 |

## 判定口径 (先定, 不因样本情况改)
- 每条四选一:
  - **HOLDS**: 终态按定义成立.
  - **HOLDS_AS_EQUIV** (只用于终态 EXACT 的条目): KB 承载了全部内容且值一致、位置对, 但不是逐字 (换了格式 / 拆并了格 / 语序) → 内容成立, 标签级别应为 EQUIVALENT. 写明差在哪.
  - **NOT_HOLD**: 终态不成立, 或 KB 内容与 PDF 不符 (缺内容 / 值不同 / 位置错 / 改义). 写明 PDF 是什么、KB 是什么.
  - **UNVERIFIABLE**: 文本层 + 渲染页都判不了. 写明缺什么.
- 拿不准不要判 HOLDS; 不要因为 "看起来大概对" 放过. 表格行必须逐格比, 值类 (日期 / 数字 / 代码 / 变量名) 一个字符都要对.
- 已登记的 PDF 笔误 (registry) 造成的 KB≠PDF 不算 NOT_HOLD, 但要写出登记 id.
- 顺手看到的 KB 内容问题 (样本之外) 单列, 不算样本判定, 不修.

## 层通过条件与后果 (主控派发前写死)
- 层通过 = NOT_HOLD 0 且 UNVERIFIABLE 0. HOLDS_AS_EQUIV 不算不通过 (EXACT / EQUIVALENT 在各覆盖率口径里同样计入), 但逐条登记, 归入 "标签级别" 后续项.
- 任何 NOT_HOLD: KB 不动 (冻结), 记为 KB 观察项; 该原子终态待改 (台账改标另走 writer → reviewer); 原样报给总闸 attempt 3.
- `PRE_EXISTING` 层出现 NOT_HOLD (KB 内容缺 / 错) ≥ 1 条 → 触发 PLAN Q9 的升级 (旧 EXACT / EQUIVALENT 标签扩检), 主控上报并另定扩检方案, 不自行结案.

## 输出 (中文, 写进派发消息指定的结果文件)
1. 文件头: 审查者类型、日期时间 (运行 `date -u +%Y-%m-%dT%H:%M:%SZ` 取真实时间)、看过的渲染页清单、用过的命令.
2. 表格: `# | atom_id | 层 | 终态 | 判定 | 依据 (PDF 文件:行 或 渲染页; KB 文件:行) | 说明 (HOLDS_AS_EQUIV / NOT_HOLD / UNVERIFIABLE 必填; FIG 层填 KB 现在的处理方式)`. `#` 用样本包里的全局编号.
3. 计数: HOLDS / HOLDS_AS_EQUIV / NOT_HOLD / UNVERIFIABLE, 并按层分列.
4. 样本外发现的 KB 内容问题 (文件:行 + PDF 页 + 说明), 没有就写 "无".
5. 路径一律用反引号包起来, 不要写成 Markdown 链接.
回复正文只需给: 四个计数、NOT_HOLD / UNVERIFIABLE / HOLDS_AS_EQUIV 的编号清单、结果文件路径.
