# G2 Executor — extract_terminology_terms.py --tier mid 实现

> Subagent type: executor (sonnet or opus; opus preferred if 修改复杂)
> Session: fresh, not main-control
> Expected duration: 15-30 min
> Mode: acceptEdits (可直接编辑 scripts_v2/extract_terminology_terms.py)
> Reviewer 会在 executor 返回后独立复核 (Rule D)

## 背景 (≤ 150 字)

v2 Phase 6.5 Claude 扩容计划批 5: terminology 中频 codelist (rank 201-500 共 300 个, 主要是 QRS/PRO questionnaire pair). 批 4 (F2) 已实现 tier=high, 产出 11a/11b/11c 三文件共 351,752 tokens (含 Synonyms + NCI Description). 批 5 mid tier 需要更紧凑的压缩策略, 目标 ≤250K tokens 总量.

当前 `scripts_v2/extract_terminology_terms.py` tier=mid 分支是 stub (~580-590 行附近), 返回 `NOT_IMPLEMENTED: --tier mid is deferred to v2.5`, rc=2. 本任务实现这个分支.

## 你的任务

实现 `extract_terminology_terms.py --tier mid` 分支, 算法差异 (vs tier=high):

1. **Definition 截断 ≤ 100 字符** (vs high tier 的 ≤ 200). 截断必须在词边界 (空格处), 不要在词中间截. 截断后加 `...`.
2. **去 Synonyms 列**: 输出表格不含 Synonyms 列.
3. **去 NCI Concept Description 链接**: 若 high tier 代码中使用了 placeholder 链接, mid tier 直接省略.
4. **保留 codelist-header 级 Related Domains 行**: 与 high tier 一致, 这是结构省 token 的好设计.
5. **输出拆分**: 必拆两文件 `12a_terminology_mid_core.md` + `12b_terminology_mid_questionnaires.md` (按 terminology subdir 路由). 若 supp 子目录有 mid tier 入选 codelist, 归入 12a 或新建 12c (具体视分布决定, 观察后再说).
6. **复用 tier=high 的元数据结构**: 每 codelist 起始 source 注释 + 文件首行 generated 注释 (改为 `--tier mid`).

## 输入

- `ai_platforms/claude_projects/output_v2/evidence_v2/G1_codelist_mid.txt` (300 C-code, 一行一 code)
- `knowledge_base/terminology/{core,questionnaires,supplementary}/*.md`

## 产出

- 修改: `ai_platforms/claude_projects/scripts_v2/extract_terminology_terms.py` (仅 mid 分支 + 相关 helper; 不要动 high tier 逻辑)
- 生成: `ai_platforms/claude_projects/output_v2/12a_terminology_mid_core.md`
- 生成: `ai_platforms/claude_projects/output_v2/12b_terminology_mid_questionnaires.md`
- 可选: `12c_terminology_mid_supp.md` (若 supp 有入选)

## 执行步骤

1. Read `scripts_v2/extract_terminology_terms.py` 全文 (约 600 行), 理解 tier=high 实现
2. Read F2 evidence `evidence_v2/F2_main_audit.json` 和 `evidence_v2/F2_main_audit.md` 了解 F2 产出格式
3. 设计 mid tier diff: 在哪几个函数加 tier 参数? 新增 helper 还是扩现有?
4. 实现:
   - `_truncate_definition(text, tier)` 或新增 `_truncate_definition_mid(text, max_len=100)` (词边界截断)
   - `render_codelist(..., tier)` 按 tier 分支决定列组合 (mid: Code/Term/Definition; high: Code/Term/Synonyms/Definition)
   - `build_subdir_documents(tier, ...)` 对 mid tier 产出 `12a/12b/12c_terminology_mid_{subdir}.md`
   - 主 `main()` 去掉 stub, 调用上述函数
5. 跑 `python3 ai_platforms/claude_projects/scripts_v2/extract_terminology_terms.py --tier mid --list ai_platforms/claude_projects/output_v2/evidence_v2/G1_codelist_mid.txt 2>&1 | tee ai_platforms/claude_projects/output_v2/evidence_v2/G2_executor_run.log`
6. 验证 rc=0 + 300 codelist 无丢失 + 每文件 token 数
7. 跑第二次, 确认 idempotent (MD5 一致)
8. 打印每文件 token 数 + 总 token 数 + 判断是否在 PLAN §G2 "~250K 各" 预期内
9. 返回结构化报告

## 强制要求 (规则 A/B/D)

- **不要自审**: executor 返回后有独立 reviewer subagent 审, 你不需要在自己 session 里说 "PASS". 只报产物 + 事实数据 + 任何 warnings.
- **失败归档不删** (规则 B): 若遇 bug, 不要 rm 任何中间产出; 写 `evidence_v2/failures/stage_v2.5_g2_attempt_1.md` 记录现场, 再重试.
- **幂等性**: 跑两次, MD5 byte-identical. 如不幂等, 调查源. 已知风险: file listing 顺序依赖, 建议 `sorted(...)`.
- **不要动 tier=high 的逻辑**: 影响零回归, F2 产出不变.
- **词边界截断**: Definition 不要在 "anatomy" 中间截成 "anato..."; 在最近的空格处截, 后缀 `...`.

## 完成信号

打印并返回:
```
[Tier mid] 12a_terminology_mid_core.md: <N> tokens, <M> codelists
[Tier mid] 12b_terminology_mid_questionnaires.md: <N> tokens, <M> codelists
(如有 12c) [Tier mid] 12c_terminology_mid_supp.md: <N> tokens, <M> codelists
Total mid tier: <N> tokens, <M> codelists (target <= 250K; PLAN §G2 预期 12a/12b 各 ~250K 合计 ~500K 是上限, 我们因去 Synonyms+NCI 预计远低)
Idempotency: rerun MD5 = <same|different>
```

## 不要做

- 不要跑 tier=high (F2 已完成, 无需重跑)
- 不要改 `rebuild_chapters_full.py` / `extract_examples_data.py` (其他脚本)
- 不要升级 `scripts_v2/build_v2_stage.py` 的 v2.5 配置 (G3 负责)
- 不要 commit (主控在 Step 9 commit)

## 参考文件

- PLAN: `ai_platforms/claude_projects/PLAN_V2.md` §9 Phase G (G2 说明) 
- F2 模板: `ai_platforms/claude_projects/output_v2/evidence_v2/F2_main_audit.md` (产出质量参考)
- F1 输入: `ai_platforms/claude_projects/output_v2/evidence_v2/F1_codelist_high.txt` (300 code 格式参考, 与 G1 同)
- G1 handoff: `ai_platforms/claude_projects/output_v2/evidence_v2/G1_codelist_mid.md` (内容分布 + 拆分建议 — 批 5 ~90% questionnaire, 12a core 可能很小)
