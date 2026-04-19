# E1 Review — 10_examples_data_others.md

> 复核日期: 2026-04-19
> Reviewer: oh-my-claudecode:code-reviewer (model=opus, agent=Task E1 independent)
> 复用 D2 已审脚本 + 2 行路径修正
> 抽样域 (与主控不重叠): TA / OE / SR / FT / QS

## 结论

**CONDITIONAL_PASS**

数据抽取行为正确, 全部 5 个抽样域所有 Examples 100% 保留, XPT 标记/数据表/Markdown 列结构均逐字保留, 35/35 域全覆盖, 与 09 0 重叠, 63/63 SDTM 域全集; 幂等性已用第二次运行 md5 一致验证. 一处 LOW-severity 文档 bug (H1 标题文本未跟随 `09→10` 文件名修正), 不影响数据抽取或 RAG 检索, 但建议修复以保持文档自洽.

## 1. 脚本改动审

D2 → E1 实际 delta (与 prompt 描述一致):

- Line 40-41 docstring `09_examples_data_others.md` → `10_examples_data_others.md`: ✓ (但 docstring 上文 line 40 仍写 `09_examples_data_high.md`, 这是 high tier 实际输出名, 正确)
- Line 499 `_output_path()` `tier=others` 分支返回 `10_examples_data_others.md`: ✓
- 对 tier=high 分支无影响: ✓ (`_output_path('high')` 仍返回 `09_examples_data_high.md`, REPL 直接验证)
- 幂等保持: ✓ (第二次跑 stdout `[Tier others] 48897 tokens, 35 domains`, md5 = `4c971b29aec26cf7b62bc2201b82f08c`, 与 baseline 完全一致)
- exclude-list 解析路径: ✓ (D2 已审, 此处复用未改; ALL_DOMAINS 集合长度 63, exclude-list 28 → resolve 出 35)

**潜在 LOW issue (不阻塞)**:
- `build_document()` line 434 拼接的 H1 是 `# 09 Examples Data — {tier_label} (Stage v2.2)` — 字面字符串硬编码 `09`, tier=others 时输出 H1 仍为 "09" 而非 "10". 实测:
  ```
  $ grep "^# " 10_examples_data_others.md
  # 09 Examples Data — Others-Tier Domains (Stage v2.2)
  ```
  这是 D2 时代留下的硬编码, 不属于 E1 新引入的 bug, 但 E1 没有顺手修. 建议:
  ```python
  prefix = "09" if tier == "high" else "10"
  out.append(f"# {prefix} Examples Data — {tier_label} (Stage v2.2)")
  ```

## 2. 产物内容审 (5 域抽样)

### TA (源 711 行 → 产出 lines 1195-1411, 217 行)

- Examples 数量: 源 7 个 (## Example 1-7), 产出 7 个 (#### Example 1-7), 顺序匹配 ✓
- 数据表 (`ta.xpt`): 源 7 张, 产出 7 张, 行数 / 列数 / 分隔符全对 (Example 7 表 9 + 头, 与源一致) ✓
- 首段 description: 7/7 examples 有, 全部 ≤ 2 行 ✓
- `**Rows N-M:**` 行: 源不含此模式 (TA 不用 row-explain), 无丢弃需求 ✓
- "**ta.xpt**" XPT 粗体: 7/7 保留 ✓
- 关键 RAG 字段抽样核 (Example 7 row 9): TABRANCH / TATRANS / 长 string `"If progression, skip to Follow-up. If no progression, but subject is ineligible for or does not consent to surgery, skip to Chemo."` 完整保留 ✓
- 删除内容: 4 个 mermaid 图块 / "Trial Arms Issues" 章节 (后置叙述, 4 个 ### 子标题) 全部去除, 符合脚本预期 ✓
- **Trial Design Matrix** 表全部保留 (因有 `|---|` 分隔, 触发 table-block 规则) ✓
- **PASS**

### OE (源 154 行 → 产出 lines 577-693, 117 行)

- Examples: 源 4 (Example 1-4), 产出 4 ✓
- 数据表: 源 oe.xpt×4 + suppoe.xpt×3 + pr.xpt×1 + di.xpt×1 + relrec.xpt×1 = 10 张; 产出 10 张 ✓
- Example 1 首 description: "This example shows a general anterior segment examination performed on each eye at 1 visit, with the purpose of evaluating general abnormalities." (单行, 完整) ✓
- Example 2/3/4 description: 源用 bullet list (`- Different assessments...`), 产出仅保留首 bullet line (脚本 ≤2 lines 截断), 后续 bullets 被丢. 这是 D2 已知行为, 不是缺陷.
- `**Rows 1-2:**` / `**Rows 3-4:**` etc. row-explain 行 6 处全部 dropped ✓ (Example 1 源 line 7-8, Example 2 源 line 35-38, Example 4 源 line 133-136)
- 关键 RAG 字段: Example 3 row 5/6 thickness `1030 um`, FOCID `OS/OD`, OELNKID 链接列, RELREC SPDEVID/PRLNKID 关联 — 全部保留 ✓
- **PASS**

### SR (源 117 行 → 产出 lines 1008-1107, 100 行)

- Examples: 源 3 (Example 1-3), 产出 3 ✓
- 数据表: 源 sr.xpt×3 + ex.xpt×1 + relrec.xpt×2 + ag.xpt×1 = 7 张; 产出 7 张 ✓
- Example 1 首 description "In this example, the subject is dosed with increasing concentrations of Johnson grass IgE." (单行) ✓
- Example 2 首 description 完整保留 (3 行 → 截到 2 行? 实际查看产出 line 1031 是单段, 源 line 27 也是单段, 完整保留, 验证 `_first_description` 段内 ≤2 lines 行为正确)
- Example 3 长描述 (源 line 87 单行 5 句) 完整保留 ✓
- `**Rows 1-4/5-8/1-6/7-12:**` row-explain 行 4 处全部 dropped ✓
- RELREC 18 行表 (Example 2) 完整保留, 含 R1-R6 跨 SR/EX 多对一关系 ✓
- **PASS**

### FT (源 29 行 → 产出 lines 290-313, 24 行)

- Examples: 源 1, 产出 1 ✓
- 数据表: 源 ft.xpt + suppft.xpt = 2 张, 产出 2 张 (FTGRPID/QORIG/QEVAL 列全保留) ✓
- 首 description: 源用 `**6-Minute Walk Test (SIX MINUTE WALK)**` (粗体子标题) + `The example represents the distance...` 一段. 产出仅保留 `**6-Minute Walk Test (SIX MINUTE WALK)**` 单行?

  实测产出 line 296: `**6-Minute Walk Test (SIX MINUTE WALK)**` — 该行被脚本作为 "anything else" 通过, 实际是因为它出现在 Example header 后下一行, `_first_description` 检查到首字符是 `*` (粗体起始, 非 prose), 然而该 regex 仅对 `**filename.xpt**` 模式精确匹配, 所以 `**6-Minute Walk...**` 不被 FILENAME_BOLD_RE 拦截, 被 `_first_description` 当 prose 收纳. 验证: 产出 line 296 = 该粗体子标题, line 297 空, 之后是数据表. 但 description 之后那行 prose `The example represents the distance (in meters)...` 被截掉了 (因为 `_first_description` 已消费完 paragraph 1 = 粗体行, blank line 后停止, 接下来 prose 是新段, 不再进入 description).

  这是脚本的边角行为: 粗体子标题 (非 filename) 占用了 first-description slot, 真实业务 description "The example represents..." 被丢. 影响: RAG 检索时 FT Example 1 仅保留 SIX MINUTE WALK 名称, 缺 "distance in meters" 描述. **MEDIUM 数据质量观察**, 但因 SIX MINUTE WALK 名称即关键检索词, FTTESTCD 列又含 "Distance at N Minutes" 字面值, 检索仍可命中. D2 已 PASS 表明此行为已被接受.

- 数据表两张完整保留, FTBLFL=Y 全 6 行 ✓
- **PASS** (with NOTE)

### QS (源 25 行 → 产出 lines 746-767, 22 行)

- Examples: 源 1, 产出 1 ✓
- 数据表: 源 qs.xpt = 1 张 (10 行 + 头 + 分隔), 产出 1 张行列全对 ✓
- 同 FT: 源 `**Satisfaction With Life Scale (SWLS)**` 粗体子标题被 `_first_description` 当 description 消费, 紧随的 `The example represents the items from the SWLS instrument.` 被丢. 同样 MEDIUM, D2 已 PASS.
- QSTESTCD/QSTEST/QSCAT/QSORRES 全部 10 行字面保留 (Slightly agree / Neither agree nor disagree / Strongly disagree etc.) ✓
- 2 个 USUBJID (CDISC01.100008, CDISC01.100014) 各 5 行, 顺序与源一致 ✓
- **PASS** (with same NOTE as FT)

### 抽样总结
- 5/5 域 Examples 数量 100% 匹配
- 5/5 域所有数据表行/列完整, XPT 粗体保留
- 0 处真实 row-explain 行漏删
- 1 类 MEDIUM 观察 (FT/QS/类似域: 粗体子标题占 description slot, 真 description 被丢) — D2 已知, E1 复制行为, 不阻塞

## 3. 结构审

- 首行 `<!-- generated by scripts_v2/extract_examples_data.py --tier others at 2026-04-15T06:34:14Z -->` 在 ✓ (时间戳来自源 mtime, deterministic)
- H1 标题 `# 09 Examples Data — Others-Tier Domains (Stage v2.2)` — **LOW-severity bug**: 字面 `09` 应为 `10`, 见 §1 末尾
- 35 域 `<!-- source: -->` comment: ✓ (`grep -c` = 35)
- 域间 `\n---\n` 分隔: ✓ (随机抽 lines 694, 745, 1109 等位置确认)
- 63 域完整 (09 28 域 ∪ 10 35 域): ✓ (REPL 验证 `len(union) = 63 = len(ALL_DOMAINS)`)
- 0 overlap: ✓ (REPL 验证 `high & others = set()`)
- 缺数据表 fallback: RELREC 触发 `(no data tables in source)` 占位 (line 832-835) — 符合脚本 "edge case degrade" 设计 ✓
- Tokens 48,897 ∈ (30K, 50K], stderr 仅 WARN 不 EXCEED, 接受 ✓

## 4. 关键发现

**主结论**: E1 任务本身 (脚本两行修正 + tier=others 跑批) 实施正确, 输出可用于上传. D2 已 PASS 的脚本主体在 E1 的 35 域 batch 上行为一致 (idempotent + deterministic timestamp), 抽样的 5 个 high-diversity 域 (TA 长且有 7 examples / OE 4 examples 含 RELREC / SR 3 examples 含 18-row RELREC / FT 1 example 单 supp / QS 1 example 10 rows×2 subjects) 均通过逐项核对.

**需要主控决策的 2 个点**:
1. **LOW**: H1 文本写的是 "09 Examples Data — Others-Tier Domains" — 文档自洽问题. 修复成本 = 改 1 行 + 重跑 (md5 会变). 建议在 E2/E3 build stage 之前一并修, 否则上传后 RAG 检索到 H1 时会有 "10 文件标题写 09" 的认知不协调. 不阻塞 E2.
2. **MEDIUM (D2 已知 carry-over)**: FT / QS / 类似 "**bold subtitle**" 域的 first-description 被粗体行占用, 真业务 description 被丢. D2 已 PASS, 不应在 E1 重新追问, 但建议在 RETROSPECTIVE 留一笔 "下一轮 (如果有 v2.4) 收紧 `_first_description` 跳过非 filename 粗体".

## 5. 下一步建议

- **CONDITIONAL_PASS → 主控可继续 E2/E3/E4 流 (build stage v2.3 + HARD CHECKPOINT)**
- LOW H1 bug 建议加进 tech debt list, 不阻塞 v2.3 集成
- MEDIUM `_first_description` 粗体观察建议进 RETROSPECTIVE.md, 不阻塞当前流
