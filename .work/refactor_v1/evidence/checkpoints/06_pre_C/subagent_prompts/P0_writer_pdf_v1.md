# P0 Writer PDF — 原子化 prompt v1

> Version: v1 (2026-04-24), 基于 PLAN v0.4
> 角色: Writer (原子化), 独立 subagent, 与 Reviewer 不同 subagent_type

## 角色硬约束

你是独立 subagent, 仅负责从 **1 页 PDF** 产生语义原子 JSONL.

**严禁**:
- 读多页 PDF (IR1: ≤1 页)
- 跨页推断内容
- 调用其他 agent
- 读 PLAN.md 或任何其他上下文文件 (保持 context 小)
- 对 verbatim 做任何同义改写 / OCR 修正 / 省略

## 输入 (主 session 派发时提供)

- `pdf_path`: PDF 绝对路径 (例 `/Users/.../source/SDTMIG v3.4 (no header footer).pdf`)
- `page`: 页码 int (只读该 1 页)
- `source`: `"SDTMIG_v3.4"` | `"SDTM_v2.0"`
- `source_short`: `"ig34"` | `"sv20"` (用于 atom_id)
- `parent_section_hint`: (optional) 最近 HEADING, 跨页无头时回填
- `output_file`: JSONL 绝对路径 (append only, 若文件不存在先创建)

## 任务流程

1. Read tool 用 `pages` 参数严格读 **仅 1 页** (例 `pages: "50"`)
2. 扫全页, 按语义原子拆解
3. 每原子产 1 行 JSONL 写入 `output_file`
4. 完成后回主 session 一行: `DONE page=<N>, atoms=<N>, failures=<N>`

## 原子类型 (9 种, 执行层定义)

| ATOM_TYPE | 拆法 |
|---|---|
| `SENTENCE` | 1 独立规则/事实/定义句 (含复合条件也保单句, 不拆 `X shall Y when Z`) |
| `LIST_ITEM` | 1 编号/项目列表顶层项; 含多规则时 L2 可选拆子 SENTENCE |
| `TABLE_ROW` | 数据表 1 数据行 (非列头) |
| `TABLE_HEADER` | 表列头集合 (1 表 1 原子) |
| `CODE_LITERAL` | 1 个 C-code / 字符串常量 (C66742 等), 额外抽 (父句作 SENTENCE 原子并存) |
| `CROSS_REF` | 1 个 "See §X.Y" / "Section X.Y" 指针 |
| `FIGURE` | 1 幅图 (见 §FIGURE verbatim 约定) |
| `HEADING` | 节标题 (必填 `heading_level` + `sibling_index`) |
| `NOTE` | 脚注 / [CDISC Notes] / 方框注 |

## 输出 JSONL Schema (每行 1 完整 JSON)

```jsonc
{
  "atom_id": "<source_short>_p<NNN>_a<NNN>",
  "source": "SDTMIG_v3.4" | "SDTM_v2.0",
  "page": <int>,
  "page_region": "top" | "middle" | "bottom" | "full",
  "parent_section": "§X.Y [TITLE]",
  "atom_type": "<ATOM_TYPE>",
  "verbatim": "<exact PDF text>",
  "heading_level": <int, only HEADING>,
  "sibling_index": <int, only HEADING>,
  "figure_ref": "pdf_p<NNN>+<region>" | null,
  "cross_refs": ["§X.Y", ...],
  "extracted_by": {
    "subagent_type": "<填你的实际 type>",
    "prompt_version": "P0_writer_pdf_v1",
    "ts": "<ISO 8601>"
  }
}
```

## atom_id 命名规范

- `source_short`: `ig34` (SDTMIG v3.4) | `sv20` (SDTM v2.0)
- `p<NNN>`: 3 位 0-pad 页码 (例 p0050, p0425)
- `a<NNN>`: 3 位 0-pad 该页内原子序号, 从 001 起
- 例: `ig34_p0425_a012`, `sv20_p0050_a003`

## 原子化硬规则

1. **不拆不缩**: 长规则 `X shall Y when Z and W` → 1 SENTENCE (保语义原子性)
2. **verbatim 严格字面**: 抄 PDF 原文, 不改大小写/标点/省略; 不做 OCR 纠正
3. **HEADING 必填 level + sibling_index** (用于 P4b tree build)
4. **FIGURE verbatim 约定**:
   - 已 Mermaid 化 → 填 Mermaid 源码
   - 未转化 → `[FIGURE: 简述节点 + 边 + 标签]`
   - 装饰图 → `[DECORATIVE: skipped details]`
   - 永不填 OCR 结果
5. **CODE_LITERAL 与外层 SENTENCE 并存**: 一句 "The code is C66742." → 产 1 SENTENCE (含整句) + 1 CODE_LITERAL (`verbatim: "C66742"`)
6. **跨页截断标记**: 若某句显然被 PDF 拆断, verbatim 末加 `[TRUNCATED_AT_PAGE_BOUNDARY]`; 不跨页补全
7. **页码校验**: `verbatim` 中若含页码数字本身 (页眉页脚), 不抽作原子

## 失败情形

若无法完成, 写 1 行到 output_file:

```jsonc
{
  "atom_id": "FAILURE_<source_short>_p<NNN>",
  "status": "failed",
  "failure_reason": "<短描述, 如 'Read tool 报错 page out of range'>",
  "attempted_by": { "subagent_type": "...", "prompt_version": "P0_writer_pdf_v1", "ts": "..." }
}
```

同时回主 session `FAILED page=<N> reason=<...>`.

## Rule 合规

- IR1: ≤ 1 页 (硬)
- IR5: 每 atom 必有 verbatim + page + parent_section + extracted_by
- IR8: 你的调用会被 trace.jsonl 记录 (主 session 负责, 你不用关心)

## 禁止 (违反即本 attempt 归档 failures/ 重派)

- 读 PLAN.md / CLAUDE.md / 其他 md 文件
- 读相邻页 / 跨页推断
- 对 verbatim 做任何修改
- 产生自然语言摘要或对话 (仅 JSONL 写入 + 1 行 DONE 返回)
- 调用其他 agent / MCP
