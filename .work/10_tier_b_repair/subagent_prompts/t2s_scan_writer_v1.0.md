# T2-post 扫描批 Writer Brief v1.0 — subagent_type: `oh-my-claudecode:executor`, model=opus

> 新建 2026-11-26 (主控). T2 模板 `t2_writer_v1.0.md` 是原子驱动; 扫描批无 `atoms[]`, 改为**按 PDF 节全扫**. v1.0 规则 1-11 仍适用 (逐字、只插不替、删除四种、标题锚点不动、引文 ≤25 词), 本文件覆盖其中"输入 / 自查 / 授权"三处.
> 必读: `t2_writer_v1.0.md` (规则 1-11) + `t2_dispatch_notes.md` (全部口径) + `evidence/checkpoints/t1_user_ack.md` (R1-R4, D1-D7) + `evidence/checkpoints/t2_post_user_ack.md` (U1-U4) + 批次文件 `work/t2_batches/<S-批>.json`.
> 工作目录 = repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`.

## 目标
批内每个单元 (域目录 / chapters / model 文件) 达到**终版**: 对其 PDF 完整节页范围做 PDF↔KB 双向逐句全扫 (含 TABLE_ROW / TABLE_HEADER / CODE_LITERAL), 修到与 PDF 一致. 范围外发现只登记.

## 授权 (覆盖 T2 common brief 的 "需主控定" 条款)
1. **`kb_files` 全文可改** (assumptions / examples / spec 三文件), 包括 assumptions 列表的整条增删、挪位、拆合 —— 唯一依据是 PDF 原页; 每处列入变更清单, 整条级改动另列 "结构改动清单" 供 reviewer 逐条签字.
2. **`narrow_files`**: 只许做 json 里写明的那一项 (如 "在文件顶部加 §6.2 章引言"), 其余一字不动.
3. 删除仍只限 v1.0 规则 5 的四种 + 本授权第 1 条的 "PDF 无此条" 整条删除 (须给 PDF 页范围内无出处的证据; KB 自写但不矛盾的解释 → D6 标注保留, 不删).
4. 禁止碰批外文件、`archive/`、`releases/`、`terminology/`、INDEX/ROUTING/VARIABLE_INDEX.

## 输入 (批次 json 字段)
- `units[]`, `kb_files[]`, `narrow_files[{file, scope}]`.
- `sections[{unit, sec, title, lo, hi}]`: 主控按 PDF HEADING 原子定的节页范围. **你先复核 (O20)**: 起页 = 节标题页, 止页 = 下一同级/更高级标题页; 边界页上属于别节的内容不归你. 复核结果写进 checkpoint "完整节页范围" 段.
- `gaps`: 覆盖矩阵给的缺口 (D=Description/Overview 段, S=spec 首句 "xx.xpt, …", A=`## XX – Assumptions` 标题, F=spec 表脚注). 这是**已知下限**, 全扫发现的其他缺口同样补.
- `intros[{sec, pages, host, atoms_hint}]`: U3 章/父节引言, 放 host 文件顶部 (`# XX — Assumptions` 之后, 本域 Description 之前), 标题用 `## §<sec> <PDF 原标题>`, 正文逐字 (先例: `domains/NV/assumptions.md` §6.3.7, `domains/FT/assumptions.md` §6.3.9).
- `footnote`: spec 表脚注口径 (U2): 放 spec.md 最后一个变量块之后、KB 自写 Cross References 等导航块之前 (U7), 单独一段 `> ¹<PDF 脚注原文>` (多条脚注各一段, 上标照 PDF); spec 变量的 `Controlled Terms` 字段 PDF 为 `*` 的照录 `*`. 已放在 assumptions.md 的本域 spec 脚注 (`footnote_moves`) 迁到 spec.md 末尾 (先插后删, 记 MOVED). 通用规格表 (LB §6.3.5.1 / NV §6.3.7.1) 自己的脚注属 assumptions.md, 不迁.
- **不改** CT 的 C-code 记法与 DOMAIN 变量 CT (U5/U6 归 S-CT 脚本批); `> Class|Structure` 行与 Cross References 属导航 (U8).
- `census_items[]`: 本批文件内需渲染逐格核的表 (C1 PDF 表头笔误 / C3 UNPARSEABLE 无逐格证据 / 既有 DIFF). 每张都要: 渲染 PDF 原页逐格对 KB, 结果写进 checkpoint 逐格表 (每行一行, "一致" 或差异+处理).
- `pdf_ranges[]`: 给 reviewer 跑 census 用 (你也可跑, 命令见 `t2_reviewer_v1.0.md`).
- `out_of_scope[]`: 本批要一并处理的 O# (见 `work/out_of_scope_findings.md`).
- `notes`: 本批特别注意.

## 排版字符 (U1/U4) 只有一个 owner: 最后的 S-TYPO 批
- 你**新插入**的文字照 PDF 原字符 (弯引号 ’ “ ”、en dash –、省略号 …、○ □).
- **既有文字**里仅排版字符不同 (直引号 vs 弯引号、- vs –、... vs …、( ) vs ○) → **不改、不算缺口**, 也不必登记 (S-TYPO 统一脚本处理). 标题行尤其不动 (改了会断锚点).

## 自查 (替代 "atoms 数 = 表中 atom 行数")
checkpoint 必须有 **逐页双向扫描日志**: 每个 PDF 页一行
`| 页 | 节 | PDF→KB: 句/列表/表行 数, 命中数, 缺→已补数 | KB→PDF: 该页对应 KB 段落, 无出处行数→处理 | 表 (逐格/census) | 备注 |`
外加: 变更清单 (v1.0 格式, `ref` 用 `pdf:p<页>:<atom_id 或 行摘要>`), 结构改动清单, 删除清单, D6 标注清单, PDF_TYPO 清单 (每条依据), 范围外发现, 需主控定, `git diff --stat`.
机器可读 `work/t2_batches/<S-批>.writer.jsonl` 每处改动一行 (格式同 v1.0; action 另允许 DELETED / VERIFIED).
checkpoint 文件名 `evidence/checkpoints/t2_<S-批>.md`, 必须含字样 "完整节页范围" 与 "双向全扫" (覆盖矩阵脚本按此判终版).

## 运行约束
- scratch 只用 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_<S-批>_writer/` (先 mkdir). dispatch notes / common brief 里的旧 session 路径作废.
- 多批并行: 只改本批文件; **禁止 git stash / checkout / reset / commit**; 基线用 `git show HEAD:<file>`.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` 须仍为 42. evidence 里 markdown 链接用反引号包住 (不嵌套).
- trace: 结束时 append 一行 `{"ts": "<date -u 真实时间>", "step": "T2S.<S-批>", "event": "subagent_done", "agent": "oh-my-claudecode:executor", "model": "opus", "attempt": N, "duration_s": null, "verdict": null, "note": "writer: <改动数/结构改动/删除/范围外>"}`.
- Bash heredoc 写证据一律 `<<'EOF'`.
- 回主控 ≤ 10 行: 改动数、结构改动数、删除数、PDF_TYPO、范围外、需主控定.
