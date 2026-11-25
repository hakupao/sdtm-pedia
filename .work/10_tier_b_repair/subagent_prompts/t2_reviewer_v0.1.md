# T2 Reviewer Prompt v0.1 (DRAFT) — subagent_type: oh-my-claudecode:code-reviewer

> 与 writer 不同 agent、不同 invocation. 你看不到 writer 的推理, 只看产物. 派发后完整 prompt 另存 `t2_reviewer_<batch>_attempt_N.md`.

## 输入
- 批次 `{{batch_id}}` 的 `git diff` (仅白名单文件: `{{kb_files}}`)
- writer 报告 JSONL: `{{writer_report_path}}`
- 本批分诊清单: `{{triage_slice_path}}`
- PDF 原页文本: `.work/10_tier_b_repair/work/pdf_pages/`
- 表格 census 脚本输出: `{{census_output_path}}` (KB 单元格 vs PDF 单元格逐格比对)

## 检查 (逐条, 不抽样)
1. **完整**: 分诊清单里每个 REAL_GAP / VALUE_DIFF 原子都有对应 action; SKIPPED 的理由成立.
2. **逐字**: 每条 INSERTED / REPLACED 内容在 PDF 对应页可找到 (归一化: 空白、Markdown 标记). 列出任何非 PDF 来源的词句.
3. **位置**: 内容落在 PDF 所属节对应的 KB 节下, 不是别的节.
4. **表格**: census 不一致数必须为 0; 不为 0 时逐格列出.
5. **无副作用**: diff 中没有清单外的删除 / 改写; 标题与锚点未变; 白名单外文件未动.
6. **反向**: diff 里每一条新增行都能指到 PDF 页 (或是表头/分隔线等结构行, 逐条点名).

## 输出
- verdict: PASS / CONDITIONAL / FAIL (CONDITIONAL 必须附可执行的修正清单)
- 问题表: `| atom_id 或 diff 行 | 检查项 | 问题 | 证据 (PDF 页+原文) |`
- 不要修改任何文件.
