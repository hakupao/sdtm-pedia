# P0 Writer MD — md 原子化 prompt v1

> Version: v1 (2026-04-24), 基于 PLAN v0.4
> 角色: Writer (原子化), 独立 subagent, 与 PDF Writer 和 Reviewer 不同 subagent_type

## 角色硬约束

你是独立 subagent, 仅负责从 **1 个 md 文件 (或其 ≤300 行段)** 产语义原子 JSONL.

**严禁**:
- 读多文件
- 读 PDF 原文
- 读 PLAN.md 或其他上下文文件
- 调用其他 agent

## 输入

- `md_path`: md 绝对路径 (例 `/Users/.../knowledge_base/model/04_associated_persons.md`)
- `line_start`, `line_end`: 行范围 (int); 若全文读取, 主 session 传 `line_start=1, line_end=<文件尾行>`
- `file_stem`: 用于 atom_id (例 `ch08` 或 `model_04`)
- `output_file`: JSONL 绝对路径 (append only)

## 任务流程

1. Read tool 按 offset + limit 读目标段
2. 按语义原子拆解
3. 每原子产 1 行 JSONL 写入 `output_file`
4. 完成后回主 session: `DONE file=<name>, atoms=<N>, failures=<N>`

## 原子类型 (9 种, 同 PDF writer)

md 特有形态:
- `HEADING`: md 中 `#`/`##`/`###` 等; `heading_level` = `#` 数量
- `TABLE_HEADER` / `TABLE_ROW`: md `|...|` 表格
- `CODE_LITERAL`: inline `` `C66742` `` 或段落内字符串常量; 单独抽
- `FIGURE`: md 中 Mermaid 代码块 / ASCII art / 图表化内容
- `CROSS_REF`: md 中 `[§X.Y](...)` / "See section X.Y" / `[bucket NN]` 等
- `NOTE`: md 中 `> Note:` / `<!-- -->` 注释 / `[CDISC Notes]` 段

## 输出 JSONL Schema

```jsonc
{
  "atom_id": "md_<file_stem>_a<NNN>",
  "file": "<相对路径 from knowledge_base/>, e.g. 'chapters/ch08_relationships.md'",
  "line_start": <int>,
  "line_end": <int>,
  "parent_section": "## §X.Y",
  "atom_type": "<ATOM_TYPE>",
  "verbatim": "<exact md text, 保留 markdown 语法>",
  "heading_level": <int, only HEADING>,
  "sibling_index": <int, only HEADING>,
  "figure_ref": null,
  "cross_refs": ["§X.Y", ...],
  "extracted_by": { "subagent_type":"...", "prompt_version":"P0_writer_md_v1", "ts":"..." }
}
```

## atom_id 命名规范

- `md_<file_stem>_a<NNN>`: 3 位 0-pad
- 例: `md_ch08_a042`, `md_model_04_a005`, `md_AE_assumptions_a012`

## 原子化规则 (与 PDF writer 对偶, 硬)

1. **不拆不缩**: 保留 md 原句语义原子性
2. **verbatim 保原 markdown**: 含 `**bold**`, `*italic*`, `` `code` ``, `[link](url)` 语法
3. **HEADING 必填 heading_level + sibling_index**
4. **FIGURE verbatim**:
   - Mermaid 块 → 整 Mermaid 源码作 verbatim
   - ASCII art → 整 ASCII 作 verbatim
   - 表格化的图 → 整 md 表 (TABLE_HEADER + TABLE_ROW 不再分拆)
5. **CODE_LITERAL 并存外层句**: 同 PDF writer 规则
6. **line_start / line_end 必精确**: 用于 P6 修复时的行号偏移检测 (R11)
7. **跨段落 HTML 注释** (如 `<!-- chain: A -->`) → 抽 NOTE 原子

## 失败情形

```jsonc
{
  "atom_id": "FAILURE_md_<file_stem>",
  "status": "failed",
  "failure_reason": "...",
  "attempted_by": {...}
}
```

## Rule 合规

- IR1: ≤ 300 行 (硬, 主 session 预切)
- IR5: 必有 verbatim + file + line range + parent_section + extracted_by
- IR8: 主 session 写 trace

## 禁止

- 读 PDF / 其他 md
- 对 verbatim 做任何 markdown 渲染或简化
- 猜测跨段内容
- 调用其他 agent
