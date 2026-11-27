# T4.1 Q9 扩检 brief v1.0 (旧 EQUIVALENT 标签)

<!-- chain: E (plans) -->
> 用途: PLAN §9 Q9 的升级路径. 触发原因: 补检 PRE_EXISTING 层 (58 条旧 EXACT 全检) 出现 2 条 NOT_HOLD (`sv20_p0069_a001` / `sv20_p0069_a003`, SDTM v2.0 §6.6 变量表行: 旧匹配器把它们配到了另一张表, 本表 KB 没有那两格 Notes).
> 审查角色 `oh-my-claudecode:tracer` (opus), 只读. **先完整读** `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` 的 "背景" 与 "判定口径" 两节 (标签定义、PDF / KB 怎么看、只读约束、输出格式都沿用), 再读本文件的增补.
> 派发前口径已写死, 不因结果改.

## 这次审的是什么
- "旧标签" = 06 深审的匹配器 (P4a) 给的 EQUIVALENT, 本项目 (10 Tier B) 没有改过也没有复核过; 原子在本项目范围 (§5.0) 内.
- 旧 EXACT 已全部用指纹复验过 (命中不了的 58 条已逐条审完); **旧 EQUIVALENT 指纹验不了**, 所以要人看.
- 两层:
  - `Q9_SV20_EQUIV`: SDTM v2.0 (`sv20_*`) 的旧 EQUIVALENT **全部** 127 条 (全检).
  - `Q9_IG34_EQUIV`: SDTMIG v3.4 (`ig34_*`) 的旧 EQUIVALENT 2207 条里按原子类型分层随机抽的 65 条 (seed 20261131).
- 样本包里 "KB 现文" 指针多半是近似的 (旧匹配器没留行号), **必须**自己在该原子所属节 / 域的 KB 文件里找. SDTM v2.0 内容在 `knowledge_base/model/01..06_*.md`; SDTMIG 章节在 `knowledge_base/chapters/`, 域在 `knowledge_base/domains/<域>/`.

## EQUIVALENT 的判法
EQUIVALENT = KB 不逐字, 但信息完全等价 (无丢失、无改义、值一致), 且位置正确 (在该原子所属节 / 域 / 表里, 不是别处碰巧相同的文字). 逐项列出 PDF 原文的信息点再对 KB.

## 判定 (五选一; 比补检 brief 多一个 R1 类)
- **HOLDS**: EQUIVALENT 成立. KB 其实逐字承载的也判 HOLDS (备注 "实为逐字").
- **NOT_HOLD_R1** (只用于 SDTM v2.0 变量表的表行 / 表头): KB 该表的精简列 (# / Variable / Label / Type / Role 等 KB 有的列) 与 PDF 一致, 但 PDF 这一行在 KB 没有的列 (Format / Variable(s) Qualified / Usage Restrictions / Variable C-code / Definition / Notes / Examples) 里有**非空**内容, KB 本表没承载 → "信息完全等价" 不成立. 用户在 T1.4 已裁定 (R1): v2.0 变量表 KB 只收精简版, 缺的列不补, 这类行认 "有意不收 (IE)". 所以这不是 KB 内容错, 是旧标签该改成 IE. 写明 PDF 哪些列有内容没进 KB.
  - 若 PDF 那些列在该行全是空的, 或者 KB 该表另有列 (如 Notes) 把这些内容承载了 → 不属于此类, 按 HOLDS 判.
  - 内容只出现在 KB **另一张表 / 另一节** (同名变量) 而本表没有 → 属于此类 (位置不对).
- **NOT_HOLD**: 上面那类之外的不成立: KB 缺内容 / 值不同 / 改义 / 位置错. 写明 PDF 是什么、KB 是什么.
- **TOC**: 原子是 PDF 目录页的条目 (所在节 `§0 [TOC]`). 核 KB 里是否有对应的节标题 (节号 + 标题文字); 有 → 判 HOLDS 并备注 "TOC→标题"; 标题文字不同或没有该节 → NOT_HOLD.
- **UNVERIFIABLE**: 文本层 + 渲染页都判不了, 写明缺什么.

已登记的 PDF 笔误 (`work/t2_pdf_typo_registry.jsonl`) 造成的差异不算 NOT_HOLD, 写出登记 id. 拿不准不要判 HOLDS.

## 后果 (主控派发前写死)
- NOT_HOLD_R1 → 台账改标 IE (R1, 用户已 ack 的类别), 另走 writer → reviewer; 不动 KB.
- NOT_HOLD → 记 KB 观察项 (KB 冻结不修), 上报.
- `Q9_IG34_EQUIV` 抽样里出现 NOT_HOLD ≥ 1 → 上报主人决定是否对 2207 条全检; 0 条 → 报告 "65 抽 0 错" 及其置信上界, 仍由主人决定够不够.

## 输出
同补检 brief 的输出格式 (文件头含真实 `date -u` 时间 / 表格 / 计数 / 样本外发现); 表格 `#` 用样本包里的 Q 编号; 计数列出 HOLDS / NOT_HOLD_R1 / NOT_HOLD / UNVERIFIABLE (TOC 条目计入 HOLDS 或 NOT_HOLD, 另报 TOC 条数). 结果只写进派发消息指定的那一个文件.
