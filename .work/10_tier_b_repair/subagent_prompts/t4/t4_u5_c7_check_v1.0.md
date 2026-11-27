# U-5: C7 规则 38 条 ATOM_ERR 全检 brief v1.0 (oh-my-claudecode:tracer)
<!-- chain: E (plans) -->
先读 `subagent_prompts/t4/t4_common_v1.0.md`.

## 任务
`work/t4/u5_c7_38.jsonl` 列出 38 个终态 = ATOM_ERR、判定规则 = `C7-atom-not-in-PDF` 的原子 (T3 脚本只做了 "原子 verbatim 在 PDF 文本层搜不到" 的判断, 没逐条证明). 每条字段: atom_id / page / verbatim / pdf_page_txt / kb_loc / targets / fix_row (T2 writer 修订行) / checkpoint / discrepancy.
ATOM_ERR 成立 = **两半都成立**:
1. 原子 verbatim 确实与 PDF 不符 (以渲染页为准; 文本层对表格可能错列, 文本层搜不到 ≠ PDF 没有). 如果其实 PDF 里有与原子逐字一致的内容 (只是文本层断行/错列), 则这一半不成立.
2. KB 在对应位置按 PDF 写对了 (该原子对应的 PDF 内容在 KB 里逐字或等价承载, 值一致, 位置在该域/章节文件内). kb_loc 可能偏, 先 Grep.

## 判定 (先定, 不改)
每条三选一: **成立** / **不成立** (任一半不成立; 写明是哪一半) / **看不出** (说明缺什么).

## 输出
写到 `.work/10_tier_b_repair/evidence/checkpoints/t4_u5_c7_fullcheck.md` (只写这一个文件):
- 顶部: 标题、状态行 `> 状态: 审查完成 (2026-11-27), 审查者 oh-my-claudecode:tracer (opus), 只读`, 方法说明 (看了哪些渲染页).
- 表: `# | atom_id | 页 | 半1 原子≠PDF (依据) | 半2 KB=PDF (KB 文件:行) | 判定 | 备注`
- 计数: 成立 / 不成立 / 看不出.
- 样本外顺手发现的 KB 问题单列 (不修).
回复正文只给: 计数 + 不成立/看不出的 atom_id 与一句原因 + 输出文件路径 (≤ 200 字).
