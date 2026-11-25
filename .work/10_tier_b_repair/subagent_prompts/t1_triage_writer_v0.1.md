# T1 Triage Writer Prompt v0.1 (DRAFT) — subagent_type: oh-my-claudecode:scientist

## 任务
对 `{{triage_pack_path}}` 中约 50 个 gap 原子 (ledger 标 PARTIAL/MISSING/ERROR/MISPLACED), 对照 **PDF 原页** 与 **现行 KB**, 给每个原子一个 class. 只读, 不改任何文件.

## class 定义
- PRESENT: KB 目标节内有该内容 (逐字或仅格式差异). 给出 KB 文件 + 行号.
- REWRITE_OK: KB 改写了 (如句子改成表格), 但 PDF 该原子的每个信息点都在. 列出信息点逐一对应.
- RELOCATE: 内容在 KB 但在别的文件或别的节. 给出现位置与应在位置.
- FIGURE: 原子是图 (FIGURE). 说明 KB 有无对应文字描述.
- IE_CAND: 按既有 IE 类别应排除 (如域 Specification 表行 — KB 的 spec.md 由 xlsx 生成). 给类别名.
- REAL_GAP: KB 缺少该信息点 (哪怕只缺一个限定词 / 例外 / 数值). 写明缺什么.
- VALUE_DIFF: KB 有对应内容但值不同 (变量名、数值、代码表值). 给出 PDF 值 vs KB 值.
- ATOM_ERR: pdf_atoms 的 verbatim 与 PDF 原页不符 (抽取错). 给出原页原文.
- LOCATE: 找不到应放的 KB 文件. 给出候选.

## 标定
先读 `{{calibration_set_path}}` 的 10 条样例, 尺度与之一致. 拿不准 REWRITE_OK vs REAL_GAP 时判 REAL_GAP.

## 输出 JSONL (每原子一行)
`{"atom_id", "class", "kb_file", "kb_lines", "evidence_pdf": "原页原文片段", "evidence_kb": "KB 片段", "missing_points": [], "confidence": "high|medium|low"}`
