# P0 Pilot T1 — Writer findings

> 产出日期: 2026-04-24
> 阶段: P0 Pilot Step 1-2 (writer × 2 并行, 尚未 matcher/reviewer)
> Target: T1 `model/04_associated_persons.md` (38 行) × `SDTM_v2.0.pdf` p.50

## 原子产出量

| Writer | subagent_type | 原子数 | JSONL 文件 |
|---|---|---|---|
| PDF writer | `Explore` | **17** | `p0_T1_pdf_atoms.jsonl` |
| MD writer | `oh-my-claudecode:explore` | **25** | `p0_T1_md_atoms.jsonl` |

Rule D 合规: 2 writer subagent_type 不同 ✓

## 原子类型覆盖 (9 种中 5 种测到)

| TYPE | PDF | MD |
|---|---|---|
| HEADING | ✅ a001 | ✅ a001/003/007/011/016 (多级嵌套) |
| SENTENCE | ✅ | ✅ |
| LIST_ITEM | ✅ | ✅ |
| TABLE_HEADER | ✅ a011 | ✅ a018/019 (⚠️ 分离为头 + 分隔符) |
| TABLE_ROW | ✅ a012-015 | ✅ a020-023 |
| CODE_LITERAL | ❌ 未抽 (`APID` 作 CODE_LITERAL 候选但未独立原子) | ❌ 未抽 |
| CROSS_REF | ⚠️ 放入 `cross_refs` 字段, **未独立原子** | ⚠️ 同 |
| FIGURE | ❌ 本页/本文件无图 | ❌ 同 |
| NOTE | ❌ 本内容无脚注/方框注 | ❌ 同 |

**覆盖 5/9** — 需 T2/T3 补足 FIGURE / CROSS_REF / CODE_LITERAL / NOTE.

## 发现 (schema / writer behavior)

### F-T1-1 [MEDIUM] CROSS_REF 处理二义性

**现象**: 两 writer 都把 "see Section 6.3" 等引用放到 `cross_refs` 字段, 未抽独立 `CROSS_REF` 原子.

**根因**: 原 prompt 同时说 "CROSS_REF 是 1 个原子类型" 和 "每原子含 cross_refs 字段". 契约矛盾.

**Fix (v2 prompt)**: 明示 "CROSS_REF 单独抽原子 (当交叉引用是独立内容, 如段末独立句 'For more details, see §8.2.1.'); 段中嵌入的引用仅填 `cross_refs` 字段不额外抽."

### F-T1-2 [MEDIUM] MD TABLE_HEADER 分离成 2 原子

**现象**: md a018/a019 分别是 `| Variable | Label | ... |` 和 `|----------|...|`, 产出 2 个 TABLE_HEADER 原子.

**根因**: prompt 未明示 "md table header 含两行 (头 + 分隔符), 合并为 1 原子".

**Fix (v2 prompt)**: "TABLE_HEADER 合并 md table 前 2 行 (行头 + `|---|---|` 分隔) 为 1 原子, verbatim 含换行符".

### F-T1-3 [LOW] sibling_index 起始值不一致

**现象**: PDF writer `sibling_index: 1` (1-index), MD writer `sibling_index: 0` (0-index).

**Fix**: 统一 0-index (程序友好) 或 1-index (人类友好). 建议 **0-index**.

### F-T1-4 [MEDIUM] MD 部分 atom `parent_section: ""` (空)

**现象**: md a001/a002/a011/a016/a024/a025 的 `parent_section` 空字符串.

**根因**:
- a001 是 top HEADING 本身, 无父节 → 合理 (可改 "ROOT")
- a002 "Source:" 行 → 属顶层, 合理
- a011 "### Key Principles" HEADING → 父应是 `## Overview`? 但 writer 标 "" — **bug**
- a016 同上 — **bug**  
- a024/a025 line 38 收尾段 → 父应是上方 `### Variables Used in Associated Persons Data` — **bug**

**Fix**: v2 prompt 加 "HEADING 原子的 parent_section 填上一级 HEADING 的 `## §X.Y`, 顶层填 `ROOT`; 其他原子的 parent_section 填最近 HEADING (不分级别)".

### F-T1-5 [HIGH, 业务发现] **MD 版 table 5 列 vs PDF 版 12 列 — 真实 CONTENT_TRUNCATED**

**PDF 表头 (a011)**: `#|Variable Name|Variable Label|Type|Format|Role|Variable(s) Qualified|Usage Restrictions|Variable C-code|Definition|Notes|Examples` → **12 列**

**MD 表头 (a018)**: `| Variable | Label | Type | Role | Notes |` → **5 列**

**MD 丢失的列**:
- `#` (row number)
- `Format`
- `Variable(s) Qualified`
- `Usage Restrictions`
- `Variable C-code` (!! CDISC 标准代号, 如 C55361 for APID)
- `Examples`

**MD 把 `Definition` 与 `Notes` 合并成一个 `Notes` 列**.

**影响**: 这**正是**本工程设计要抓的 CONTENT_TRUNCATED / PARTIAL 案例. P4a 应判 md a020 (APID 行) vs pdf a012 (APID 行) = `PARTIAL` (内容保留但列被压缩), P4b 聚合该节 coverage_density < 1.0.

**业务价值证明**: 即使在 T1 这么小的测试范围, 立刻暴露出 v2 KB 对 CDISC 标准的**列级简化**. 这是之前 Step 0-4 验证未抓出的 (因为按"节/要点"验, 没按"列/字段"验). **原子级 + 字面级验证的价值第一次兑现**.

### F-T1-6 [LOW] Writer 未遵循 "no markdown fence" 指令

**现象**: 
- PDF writer 返回 ` ```json ... ``` ` 包裹
- MD writer 加 "抽取完成。" 前缀 + ` ```jsonl ... ``` ` 包裹

**根因**: Explore 型 agent 习惯性加说明; prompt 的 "不加代码块" 指令偏靠后.

**Fix (v2 prompt)**: 指令前置 + 加 "输出示例" 段, 示例中直接无 fence.

### F-T1-7 [LOW] MD 部分 `line_start == line_end` 但内含多句

**现象**: md a004/a005/a006 都 `line_start: 7, line_end: 7`, 一行 md 写了 3 句.

**原因**: md 本身一行包含多句 (无换行); writer 正确按语义拆了 3 SENTENCE 原子, 行号本身没错.

**不是 bug**, 属预期行为. 但 P6 修复时需注意 line-level diff 策略.

## Schema 适用性评估

| 字段 | PDF writer | MD writer | 评估 |
|---|---|---|---|
| atom_id | ✅ | ✅ | 命名规范有效 |
| source / file | ✅ | ✅ | OK |
| page / line_start/end | ✅ | ✅ | OK |
| parent_section | ✅ | ⚠️ 有 bug | 待 v2 prompt 修 |
| atom_type | 5/9 测到 | 5/9 测到 | 需 T2/T3 补 |
| verbatim | ✅ 严格字面 | ✅ 保 markdown | OK |
| heading_level | ✅ | ✅ | OK |
| sibling_index | ⚠️ 1-index | ⚠️ 0-index | 需统一 |
| figure_ref | null (无图) | null (无图) | 未测到 |
| cross_refs | ✅ 字段形式 | ✅ | 但与 CROSS_REF atom type 契约冲突 (F-T1-1) |
| extracted_by | ✅ | ✅ | OK |

**schema 可用, 需 v1.1 小补** (F-T1-1 / F-T1-2 / F-T1-3 / F-T1-4).

## 下一步决策点

1. **路径 X (继续 T1 完整流程)**: 派 matcher (前 forward + 反 reverse) → reviewer 抽检 T1 42 atoms → 看 verdict 分布 → 若 APID 行果然判 PARTIAL, 证明 pipeline 端到端 work
2. **路径 Y (先扩 T2/T3)**: 让 3 target 的 atoms 都产出, 再统一做 matcher + reviewer. 优点: FIGURE/CROSS_REF/CODE_LITERAL/NOTE 都测到后再冻 schema
3. **路径 Z (先升 prompt v1.1)**: 按 F-T1-1~F-T1-4 修 prompt → 重跑 T1 → 再扩. 但会丢弃本轮产出 (可归档)

**推荐路径 X**: T1 数据已足够测 matcher + reviewer 的能力. 先看端到端 verdict 分布, 再一次性 fold T1 findings + matcher findings 进 prompt v1.1. T2/T3 在 prompt v1.1 后跑, 质量更有保障.

用户决定.
