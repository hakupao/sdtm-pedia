# T4.1 第三轮补检 brief v1.0 (主人 2026-11-27 选定的追加审查)

<!-- chain: E (plans) -->
> 用途: 仓库主人在 `evidence/checkpoints/t4_owner_decisions_round2.md` 里选了: 4a = B (SDTMIG 旧 "等价" 标签再抽 150 条)、4b = B ("PDF 笔误" 类剩下 99 条全看)、4c = B (标题类旧标签抽 60 条)、7b = A (范围外 6 条笔误同类经独立审查确认). 原话记录: `evidence/checkpoints/t4_owner_confirmation.md` 第二轮一节.
> 审查角色 `oh-my-claudecode:tracer` (opus), 只读. **先完整读** `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` 的 "背景" 与 "判定口径" 两节 (标签定义、PDF / KB 怎么看、只读约束、输出格式都沿用), 再读本文件.
> 判定口径与后果在派发前写死, 不因结果改.

## 四层各核什么

### R3_IG34_EQUIV (150 条, 抽样 seed 20261133) — 终态 EQUIVALENT, 06 旧标签, 本项目没改过
与 `subagent_prompts/t4/t4_q9_extension_v1.0.md` 的 `Q9_IG34_EQUIV` 层同口径: EQUIVALENT = KB 不逐字, 但信息完全等价 (无丢失、无改义、值一致), 且位置正确 (在该原子所属节 / 域 / 表里). 样本包里的 KB 指针多半是近似的, 必须自己到 `knowledge_base/chapters/` 或 `knowledge_base/domains/<域>/` 里找; 表格行逐格比, 值类一个字符都要对.
- **HOLDS** (KB 其实逐字承载的也判 HOLDS, 备注 "实为逐字") / **NOT_HOLD** (KB 缺内容 / 值不同 / 改义 / 位置错; 写明 PDF 是什么、KB 是什么) / **UNVERIFIABLE**.
- **TYPO_AFFECTED**: 这条原子对应处, PDF 印的是已登记的笔误写法、KB 是改正值 (登记表 `work/t2_pdf_typo_registry.jsonl`, `handling` = "KB 写正确值") → 现标签应为 PDF_TYPO. 写出登记 id. 差异若**没有登记** → 判 NOT_HOLD 并写明 "未登记".
- 原子 verbatim 抽错而 KB 与 PDF 一致的, 判 HOLDS 并在说明里注 "原子抽错".

### R3_PDF_TYPO (99 条, 全检) — 终态 PDF_TYPO
与 `subagent_prompts/t4/t4_supp_round2_v1.0.md` 的 `PDF_TYPO` 层同口径, 三件事都要成立才 **HOLDS**: ① PDF 该处确有登记所说的问题; ② KB 现状与登记的 `handling` 一致 ("KB 写正确值" → KB 是改正值; "照录" / "照录+T4" → KB 与 PDF 相同); ③ 除登记的那一处外, 这条原子其余内容 KB 与 PDF 一致. 任一条不成立 → **NOT_HOLD** (写明哪一条). 登记 id 在样本的 "登记" / "PDF 笔误登记" 行; 没给的到 `work/t3_writeback_decisions.json` (按 atom_id 查 `evidence.registry` / `registry`) 与 `work/t3_errata.json` 里找.

### R3_HEADING (60 条, 抽样) — 标题类原子, 终态 EXACT / EQUIVALENT, 06 旧标签
要核: 在该原子**自己所属文档**的 KB 文件里 (SDTMIG → `chapters/`、`domains/<域>/`; SDTM v2.0 → `model/`) 有没有对应的节 / 标题.
主人 2026-11-27 定的口径 (问题 6 = A): **KB 域文件的标题写成 `# 域代码 — 域名`、不带 PDF 节号, 是认可的写法**; 另, KB 标题在 PDF 标题后追加域代码后缀 (如 "(TE)") 也是已登记的认可写法 (U-10①).
- **HOLDS**: 终态 EXACT → KB 有文字逐字相同的标题 (节号写成 `§N.N` 或 `N.N`、Markdown `#` 层级、粗体都不算差异); 终态 EQUIVALENT → KB 有对应的标题, 文字等价 (含上面两种认可写法; 标题里把 "–" 写成 "—" 之类排版差异也算等价).
- **HOLDS_AS_EQUIV**: 终态 EXACT, KB 有对应标题但不逐字 (例如缺节号) → 内容成立, 标签级别应为 EQUIVALENT.
- **NOT_HOLD_SELF**: KB 对应位置的标题是 KB 自拟的 (文字与 PDF 标题实质不同, 例如 PDF "9.1 Device Identifiers" 对 KB "DI – Description/Overview"), 但该节的正文内容在. 写明两边的标题文字.
- **NOT_HOLD**: 自己文档的 KB 文件里没有这一节 (标题和正文都没有), 或只在另一份文档的 KB 文件里有. **UNVERIFIABLE**: 判不了.

### R3_XTYPO (6 条, 全检) — 范围外, 终态 EXACT / EQUIVALENT, 疑受已登记笔误影响
与 `t4_supp_round2_v1.0.md` 的 `TYPO_SIB` 层同口径. 复审者只在 PDF 文本层看过; 你要**看渲染页**确认: 这条原子对应处, PDF 印的是不是登记里的笔误写法, 而 KB 是改正值.
- **TYPO_AFFECTED** (写出登记 id、PDF 原文片段 ≤ 10 词、KB 文件:行) / **NOT_AFFECTED** (该处 PDF 与 KB 一致; 写明笔误实际在哪) / **NOT_HOLD** (与登记无关的其它不成立) / **UNVERIFIABLE**.

## 后果 (主控派发前写死)
- TYPO_AFFECTED (两层) → 并入改台账那一批, 改标 PDF_TYPO (主人问题 3 = A / 7b = A 已定同类的处理; 新增条目在汇报里逐条列出).
- R3_IG34_EQUIV 出现 NOT_HOLD ≥ 1 → 记 KB 观察项 (KB 冻结不修), **回报主人** (他在问题 4 的说明里被告知 "若新查出问题会再来问"), 并由主人决定是否对其余约 1900 条全检; 0 条 → 报告 "215 条 (65 + 150) 0 错" 及其置信上界, 不写成全检.
- R3_PDF_TYPO 出现 NOT_HOLD → 逐条回报主人; 0 条 → "PDF 笔误" 类 149 条全部由独立审查者看过.
- R3_HEADING: HOLDS_AS_EQUIV 归标签级别后续项; NOT_HOLD_SELF 按问题 6 = A 的做法补登记 (不动 KB), 条目列出; NOT_HOLD ≥ 1 → 回报主人.
- 任一层出现 UNVERIFIABLE → 该层不算通过, 逐条列出.

## 输出
同补检 brief 的输出格式 (文件头含真实 `date -u` 时间 / 看过的渲染页 / 表格 / 计数 / 样本外发现); 表格 `#` 用样本包里的 T 编号; 计数按本层的判定类别列. 结果只写进派发消息指定的那一个文件.
