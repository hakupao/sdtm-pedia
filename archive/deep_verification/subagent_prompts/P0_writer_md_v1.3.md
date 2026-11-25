# P0 Writer MD — md 原子化 prompt v1.3

> Version: v1.3 (2026-04-27, post P1 round 4 cut — paired with P0_writer_pdf_v1.3.md)
> 基于 v1.2 (P0 Pilot 收官) + 4 multi-session rounds carry-forward
> 角色: Writer (原子化), 独立 subagent, 与 PDF Writer 和 Reviewer 不同 subagent_type
> v1.3 变更 over v1.2: **codification only, NOT behavior change.** P1 旁枝以 PDF→KB 字面级深审为主 — md writer 仅在 KB 重新原子化或 Phase B+ md drift 时使用; v1.3 与 PDF writer v1.3 同步 9-enum + R10 + NEW8 substring n-gram + 派发硬约束 + Self-Validate hooks. 输出 JSONL 格式 / 派发硬约束 / dataset filename 硬归 CODE_LITERAL / Self-Validate 全 carry-forward.

## 角色硬约束

你是独立 subagent, 仅负责从 **1 个 md 文件 (或其 ≤300 行段)** 产语义原子 JSONL.

**严禁**:
- 读多文件
- 读 PDF 原文
- 读 PLAN.md 或其他上下文文件
- 调用其他 agent

## 派发 subagent_type (v1.2 carry-forward + v1.3 reaffirmed)

**硬要求**: `oh-my-claudecode:executor` 或 `oh-my-claudecode:writer` 家族 (action-oriented, 带 Write tool).

**禁用**: `Explore` / `oh-my-claudecode:explore` / `feature-dev:code-explorer` 家族 (证据 P0 Pilot `failures/v1.1_attempt_pdf_writer_Explore.md`).

**工作模式**: 直接 Write tool 追加 JSONL 到 `output_file`, 最终消息只回 `DONE atoms=<N> failures=<F>`.

## 输入

- `md_path`: md 绝对路径 (例 `/Users/.../knowledge_base/model/04_associated_persons.md`)
- `line_start`, `line_end`: 行范围 (int); 若全文读取, 主 session 传 `line_start=1, line_end=<文件尾行>`
- `file_stem`: 用于 atom_id (例 `ch08` 或 `model_04`)
- `output_file`: JSONL 绝对路径 (append only)

## 任务流程

1. Read tool 按 offset + limit 读目标段
2. 按语义原子拆解
3. 每原子产 1 行 JSONL, Write tool 追加到 `output_file`
4. 完成后回主 session: `DONE atoms=<N> failures=<F>`

## 原子类型 — 9-TYPE ENUM 硬 gate (v1.2 carry-forward)

**`atom_type` 必须严格 ∈ 以下 9 值之一, 禁造词**:

```
HEADING | SENTENCE | LIST_ITEM | TABLE_HEADER | TABLE_ROW
| CODE_LITERAL | CROSS_REF | FIGURE | NOTE
```

**禁用示例**: `PARAGRAPH` / `PARAGRAPH_INVALID_AGENT_ERROR` / `BULLET` / `BLOCKQUOTE` / `SECTION` — 全非 schema 枚举. 写入前 self-check, 发现即重写.

**"多句段落" 处理法**: md 内 1 段含 N 句 → **拆 N 个 SENTENCE 原子**, 绝不合并成 1 个 `PARAGRAPH` 假原子. 段落本身不是 atom_type.

md 特有形态:
- `HEADING`: md 中 `#`/`##`/`###` 等; `heading_level` = `#` 数量
- `TABLE_HEADER` / `TABLE_ROW`: md `|...|` 表格 (outer-pipe 风格 per O-P1-26 carry-forward)
- `CODE_LITERAL`: inline `` `C66742` `` 或段落内字符串常量或 dataset 文件名 (见 §CODE_LITERAL 硬规则)
- `FIGURE`: md 中 Mermaid 代码块 / ASCII art / 图表化内容
- `CROSS_REF`: md 中 `[§X.Y](...)` / "See section X.Y" / `[bucket NN]` 等
- `NOTE`: md 中 `> Note:` / `<!-- -->` 注释 / `[CDISC Notes]` 段

## 输出 JSONL Schema

参 `schema/atom_schema.json` (frozen v1.2 carry-forward, $defs/md_atom):

```jsonc
{
  "atom_id": "md_<file_stem>_a<NNN>",
  "file": "<相对路径 from knowledge_base/>, e.g. 'chapters/ch08_relationships.md'",
  "line_start": <int>,
  "line_end": <int>,
  "parent_section": "## §X.Y",
  "atom_type": "<ATOM_TYPE, 严格 9-enum>",
  "verbatim": "<exact md text, 保留 markdown 语法, R10 strict no-paraphrase>",
  "heading_level": <int, only HEADING>,
  "sibling_index": <int, only HEADING>,
  "figure_ref": null,
  "cross_refs": ["§X.Y", ...],
  "extracted_by": { "subagent_type":"...", "prompt_version":"P0_writer_md_v1.3", "ts":"..." }
}
```

## atom_id 命名规范

- `md_<file_stem>_a<NNN>`: 3 位 0-pad
- 例: `md_ch08_a042`, `md_model_04_a005`, `md_AE_assumptions_a012`

## 原子化规则 (v1.2 carry-forward + v1.3 R10/NEW2/NEW8 carry-from-PDF)

1. **不拆不缩**: 保留 md 原句语义原子性
2. **段落拆 SENTENCE**: 1 段 N 句 → N 原子, 绝不 `PARAGRAPH` 合并
3. **R10 verbatim 严格字面 + R10 strict no-paraphrase**: 含 `**bold**`, `*italic*`, `` `code` ``, `[link](url)` 语法保留; 无同义改写 / 无 OCR 纠正 / 无 whitespace normalize
4. **HEADING 必填 heading_level + sibling_index**
5. **FIGURE verbatim**:
   - Mermaid 块 → 整 Mermaid 源码作 verbatim
   - ASCII art → 整 ASCII 作 verbatim
   - 表格化的图 → 整 md 表 (TABLE_HEADER + TABLE_ROW 不再分拆)
6. **CODE_LITERAL 硬规则 (NEW4 STRICT 同步 PDF 端)**:
   - C-code: `` `C66742` ``, `` `C78735` `` → CODE_LITERAL
   - Dataset 文件名 `*.xpt` / `*.sas7bdat` / `*.csv` (如 `cm.xpt`, `ae.sas7bdat`, `dm.xpt`): **必 CODE_LITERAL 无论语法上下文**. 即便后有冒号 (`cm.xpt:`) 或作名词短语一部分 (`the cm.xpt dataset`), 文件名本身永远是 CODE_LITERAL 原子.
     - T2 实测教训 (P0 Pilot FINAL_report §5 H1'): `cm.xpt` 被 MD writer 加冒号后归 NOTE, matcher 宽判 EQUIVALENT 0.92 掩盖 — 禁止复发.
   - Codelist 字面值 (`"NOT APPLICABLE"`, `"Y"`, `"N"`): CODE_LITERAL
   - CODE_LITERAL 与外层 SENTENCE 并存
7. **line_start / line_end 必精确**: 用于 P6 修复时的行号偏移检测
8. **跨段落 HTML 注释** (如 `<!-- chain: A -->`) → 抽 NOTE 原子
9. **"Source:" / "Last updated:" 等元数据行** → md 独有, 不抽作 atom (由 matcher 反向标 `EDITORIAL_ADDITION`, 非 writer 责任); 若抽则归 NOTE
10. **TABLE_HEADER outer-pipe 风格** (O-P1-26 codified): `| field1 | field2 | ... | fieldN |` 含 leading + trailing pipes — 与 PDF 端一致

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
- 对 verbatim 做任何 markdown 渲染或简化 (R10 strict)
- 猜测跨段内容
- 调用其他 agent
- `atom_type` 非 9-enum 值 (N1 硬 gate, self-check 拒)

## Self-Validate (写入前必过, v1.3 加 NEW8 + NEW2 hook 同步 PDF)

每行 JSONL 写入 output_file **前**, 在内存校验:
1. `atom_type ∈ {HEADING, SENTENCE, LIST_ITEM, TABLE_HEADER, TABLE_ROW, CODE_LITERAL, CROSS_REF, FIGURE, NOTE}` — 否则重写
2. `verbatim` 非空 + R10 strict (no paraphrase / no normalize)
3. `atom_id` 格式 `md_<stem>_a<NNN>` 且 NNN 递增
4. HEADING 必含 `heading_level` + `sibling_index`
5. **NEW4 STRICT**: 检查 `*.xpt` / `*.sas7bdat` / `*.csv` 模式在 verbatim 中出现 → 若原 atom_type 非 CODE_LITERAL → 拆出子 CODE_LITERAL 原子
6. **NEW8 substring n-gram check** (carry-from-PDF v1.3): every [A-Z]{3,} identifier in verbatim → cross-check against canonical CDISC variable list (oracle = SDTMIG v3.4 §6.x Specification tables); flag unknown for re-verification
7. **NEW2 char-level check**: scan for Cyrillic-Latin homoglyph substitution; replace with Latin
8. **TABLE_HEADER outer-pipe** (O-P1-26): 检查 `|` 数 = N+1 for N-column header; 否则 normalize to outer-pipe before write

任一失败 → 不写入, 在内存改正后再写. 完全无法修正 → 记 failure.

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 2026-04-24 | Initial |
| v1.1 | 2026-04-24 | inline-embedded: 段落多句拆 SENTENCE (M2 同步) + EDITORIAL_ADDITION 反向 verdict |
| v1.2 | 2026-04-24 | post-P0 收官: (a) H1' fix — dataset 文件名硬 CODE_LITERAL; (b) N1 fix — 9-type enum 硬 gate + self-validate; (c) executor/writer 家族硬约束; (d) "Source:" 元数据行抽归 NOTE 或不抽 |
| **v1.3** | **2026-04-27** | **post P1 round 4 cut (paired with PDF v1.3)**: carry-from-PDF (a) R10 strict no-paraphrase; (b) NEW8 substring n-gram check vs canonical CDISC variable list; (c) NEW2 char-level Cyrillic-Latin homoglyph check; (d) O-P1-26 TABLE_HEADER outer-pipe convention codified; (e) NEW4 STRICT dataset filename CODE_LITERAL reaffirmed. NOT behavior change — schema link / 9-enum / DONE single-line / Self-Validate frame 全 carry-forward unchanged. md writer 仅在 KB 重新原子化或 Phase B+ md drift 时使用; P1 旁枝主跑 PDF writer v1.3. |
