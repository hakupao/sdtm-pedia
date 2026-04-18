# B4 Executor Prompt

## 上下文
你正在执行 SDTM Phase 6.5 v2 扩容的 Task B4 (PLAN_V2.md §4). 核心工具, 每个 stage 聚合入口.

## 你的任务
写 `ai_platforms/claude_projects/scripts_v2/build_v2_stage.py`, 负责分阶段构建 + 累计 token + 元文档更新.

## 工作目录
`/Users/bojiangzhang/MyProject/SDTM-compare/`

## CLI
```
python3 scripts_v2/build_v2_stage.py --stage v2.1 [--dry-run]
```
支持: v2.1 / v2.2 / v2.3 / v2.4 / v2.5

## 职责 (8 步)
1. 解析 --stage 参数, 映射到具体批次 (v2.1=批1 chapters, v2.2=批2 examples high, v2.3=批3 examples others, v2.4=批4 terminology high, v2.5=批5 terminology mid)
2. 跑当批脚本 (v2.1 跑 rebuild_chapters_full.py, v2.2 跑 extract_examples_data.py --tier high, ...) — **注: B4 不必实现对 C1 之外脚本的依赖, 只要 v2.1 分支完整即可; 其他分支留 TODO stub**
3. 对 `output_v2/*.md` 全部跑 count_tokens, 累计总 tokens (复用 v1 `scripts/count_tokens.py`)
4. 修订 `output_v2/system_prompt_v2.md` 对应阶段段落 (append 或 替换特定标记段)
5. 追加一行到 `output_v2/upload_manifest_v2.md` "阶段历史" 表
6. 写 `output_v2/evidence_v2/stage_v2.X_*.md` evidence 文件
7. 更新 `output_v2/evidence_v2/_progress.json` (current_stage / completed_stages / last_updated)
8. append 一行到 `output_v2/evidence_v2/trace.jsonl` (event=stage_done / stage=v2.X / total_tokens=N / files=M / status=PASS)

## stage 映射 (硬编码在脚本里)
```python
STAGE_MAP = {
    "v2.1": {"batch": 1, "script": "rebuild_chapters_full.py", "output": "02_chapters.md", "target_tokens_total": 270000, "description": "chapters 全展开"},
    "v2.2": {"batch": 2, "script": "extract_examples_data.py --tier high", "output": "09_examples_data_high.md", "target_tokens_total": 360000, "description": "examples 高频域"},
    "v2.3": {"batch": 3, "script": "extract_examples_data.py --tier others", "output": "10_examples_data_others.md", "target_tokens_total": 490000, "description": "examples 剩余域"},
    "v2.4": {"batch": 4, "script": "extract_terminology_terms.py --tier high", "output": "11_terminology_high.md", "target_tokens_total": 840000, "description": "terminology 高频 codelist"},
    "v2.5": {"batch": 5, "script": "extract_terminology_terms.py --tier mid", "output": "12_terminology_mid.md", "target_tokens_total": 1400000, "description": "terminology mid codelist"},
}
```

## --dry-run 行为
不改任何文件, 但打印将执行的 8 步 (格式: `[DRY] Step N: <description>, target <file>`).

## 幂等性
- 跑两次同一 --stage 应得到相同结果 (upload_manifest 不重复追加: 检查是否已有该阶段行; _progress.json completed_stages 去重)
- trace.jsonl 允许重复 append (append-only, 但每次 ts 不同, 接受)

## Evidence 文件命名
`stage_v2.X_<description_slug>.md` (如 `stage_v2.1_chapters.md`)

## system_prompt_v2.md 修订约定
PLAN §3.4 列出 5 个阶段的 prompt 增量:
- v2.1: 移除 v1 "ch01/02/03/08/10 精简" 兜底句, 新增 "02_chapters 已是完整版, ch08 §8.3/§8.4 含 RELREC + SUPP-- 完整规则"
- v2.2: 新增 "09 提供 25-28 高频域数据表, 优先 09"
- v2.3: 新增 "10 (或 10a+10b) 提供其余 ~35 域 examples 数据表"
- v2.4: 新增 "11 提供 top 200 codelist 完整 Term, CT Code 查询优先 11 > 08"
- v2.5: 新增 "12 (或 12a+12b) 提供 mid 频 codelist, CT Code 查询优先 11 > 12 > 08"

实现策略: 在 system_prompt_v2.md 末尾用 `<!-- stage v2.X begin --> ... <!-- stage v2.X end -->` 标记段, 每次 --stage vX 运行时替换或追加该段.

## 完成标准
1. 脚本文件存在
2. `python3 scripts_v2/build_v2_stage.py --stage v2.1 --dry-run` 打印 8 步, 不改文件
3. 处理 v2.1 真实 stage: 脚本能识别 chapters 是否已存在 (若不存在, 提示 "需先跑 rebuild_chapters_full.py", 不 crash)
4. 其他 stage 分支可 stub (log "v2.X TBD, 请先实施 extract_* 脚本")

## 强制要求
- P5: 只读 knowledge_base/
- 幂等
- Python 3 stdlib + tiktoken (已装)
- 不删除文件 (只 Write/Read, 不用 os.remove)
- stdout 每步 print `[Stage vX.Y] <message>` 格式

## 不要做
- 不要实现 extract_examples_data.py 或 extract_terminology_terms.py (它们是下阶段 task)
- 不要修改 knowledge_base/
- 不要写 .md 文档
- 不要解释做了什么

## 参考
- v1 `scripts/count_tokens.py` (读用法)
- v1 `output/upload_manifest.md` (格式参考)
- PLAN_V2.md §3 Task A2 Step 4-7 (upload_manifest / test_results 的表结构)
