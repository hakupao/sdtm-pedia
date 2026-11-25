# T2 Auditor Prompt v0.1 (DRAFT) — subagent_type: oh-my-claudecode:verifier (Rule A 独立抽检)

> 与本批 writer (executor)、reviewer (code-reviewer) 均不同. 只读.

## 输入
- 批次 `{{batch_id}}` 改动后的 KB 文件 `{{kb_files}}` 与 `git diff`
- 本批分诊清单 `{{triage_slice_path}}`; PDF 原页 `.work/10_tier_b_repair/work/pdf_pages/`
- 抽样: 种子 `{{seed}}`, N = max(10, ceil(0.2 × 本批改动 prose 原子数)), 上限 30; 从**本批范围内全部 prose 原子**随机抽 (含 writer 未声明改动的)

## 每个样本判
1. PDF 原页该原子的每个信息点是否都在 KB 目标节 (独有信息丢失?)
2. KB 表述是否与 PDF 意思一致 (忠实度: 无增、无删、无改义、限定词/例外/数值未变)
3. 位置是否正确

## 输出
- 表: `| # | atom_id | PDF 原文 | KB 对应 | 丢失? | 忠实? | 位置? |`
- 独有丢失率、忠实度错误数; 任一 >0 → 本批 FAIL
- 写入 `evidence/checkpoints/t2_{{batch_id}}_audit.md` 的内容由你给出, 主控落盘; 你不改 KB.
