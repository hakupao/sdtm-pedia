# T2 Reviewer Prompt v1.0 — subagent_type: `oh-my-claudecode:code-reviewer` (与 writer 不同 agent / 不同 invocation)

> v0.1 保留不改. v1.0 改动: 给出可执行的 census v2 / fp_match 命令; 逐格 + 逐行 (G-TB4 / G-TB6); R2 recheck 判定; 证据由你用 Bash 落盘
> (本 agent 类型无 Write/Edit; 只允许写下面列出的证据路径与 scratch, **禁止改 KB**). 派发后完整 prompt 另存 `t2_reviewer_<batch>_attempt_N.md`.
> 工作目录 = repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`. 你看不到 writer 的推理, 只看产物.

## 输入
- `.work/10_tier_b_repair/work/t2_batches/{{batch_id}}.json` (原子清单 / census 引用 / 白名单 / 源行白名单 / notes)
- writer 报告 `.work/10_tier_b_repair/evidence/checkpoints/t2_{{batch_id}}.md` + `work/t2_batches/{{batch_id}}.writer.jsonl`
- `git diff {{base_commit}} -- knowledge_base/` (**整个 KB**, 用来抓白名单外改动)
- PDF 原页 `.work/10_tier_b_repair/work/pdf_pages/`; 需要看版面时 `pdftoppm -f N -l N -r 110 -png <pdf> <scratch>/pN` 后 Read 图
- 标定集 `subagent_prompts/t1_calibration_v1.1.md` + R2 (见下)

## 命令 (scratch = `.work/10_tier_b_repair/work/scratch/t2/{{batch_id}}_reviewer/`, 先 mkdir; 不用别的目录)
```
S=.work/10_tier_b_repair/work/scratch/t2/{{batch_id}}_reviewer; mkdir -p $S
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/{{batch_id}}.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1 = 有 DIFF/NO_PDF/PDF_ONLY, 看报告
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
```
- `pdf_ranges` 为空 (本批文件无 Row 表, 如 B-DI) → 跳过 census, 在证据里写明; 若 writer 新增了 Row 表, 主控须先补 manifest 区间再跑.
- census v2: PDF 侧按 `pdftotext -bbox` 词框分列; 垂直居中表 = PDF_UNPARSED (人工). PDF_ONLY 是**全局**列表 → 只看页码落在本批 `pdf_pages` 内的.
  KB 每份副本都被比对 (`kb_duplicate`), 重复副本 (MB Ex1-3 两份 / p277 PP 两份) 都必须 OK.
- fp_match: `RESULT: RED` (有回归 = writer 弄丢了原本命中的原子) → 逐条查; RELOCATE 源行被删造成的回归是**预期**的 (B-FA), 只要该原子在 target 命中.
  `hit_any` 只给第一个命中文件 (glob 序), 不一定是本批文件 → 对本批每个 prose REAL_GAP / RELOCATE (SENTENCE / LIST_ITEM / NOTE) **直接查目标文件**:
  `python3 -I -c "import sys; sys.path.insert(0,'.work/10_tier_b_repair/scripts'); from fp_match import norm; import json; ..."` 判 `norm(verbatim) in norm(open(target).read())`;
  不命中的要么 writer 漏了, 要么原子文本与原页不符 (查原页再定).

## 检查 (逐条, 不抽样)
1. **完整**: `atoms[]` 每条在 writer 报告里有 action; SKIPPED_* 理由成立 (PDF_TYPO 须是 PDF 自身问题, 不是 writer 偷懒). census 每张 DIFF/NO_PDF 表、每个本批 pdf_only 表都处理了.
2. **G-TB4 表格**: 本批白名单文件里所有被触碰的表, census_after 状态 = OK / OK_SUBSET; 不一致只允许已登记的 PDF_TYPO. 触碰到的 UNPARSEABLE 表 + `pdf_unparsed` 表 →
   你**人工逐格**对 PDF (渲染原页), 结果表写进证据 (每格一行或每行一行, 写 "一致" 或差异).
3. **G-TB6 反向溯源**: diff 里每一条新增 / 改动行 → 在 PDF 对应页能找到 (归一化: 空白、Markdown 符号、折行连字符). 表头、分隔线、锚点、新增节标题 = 结构行, 逐条点名签字.
   任何找不到出处的词句 (自造说明、扩写、"Note:") → FAIL 项.
4. **位置**: 内容落在 PDF 所属节对应的 KB 节下; RELOCATE: 目标处有原文 + 源行只删了 `delete_only_source_lines` 指定行.
5. **无副作用**: 整个 KB diff 只涉及白名单文件 (+ 源行); 无清单外删除 / 改写; 标题、锚点未变 (新增节除外); 表格的已有正确行没被改坏.
6. **R2 recheck** (`t2_recheck[]`): 对每条回 PDF 判 REWRITE_OK 还是 REAL_GAP. R2 (用户 T1.4): **改写丢掉的短语, 即使在同节上下文 / 同表行别处已有, 也算 REAL_GAP**.
   判据: KB 在该原子位置是否逐信息点给出了 PDF 的每个片段 (限定词 / 计数 / 术语 / 交叉引用); 靠别的行、隐含、约定才能凑齐的 → REAL_GAP. 每条给 KB 行号证据.
   判 REAL_GAP 的列入 CONDITIONAL 修正清单 (writer 下一 attempt 补).
7. 引文: 证据里引 PDF ≤ 25 词/处.

## 输出 (你用 Bash heredoc 写, 只写这两处 + scratch)
- `.work/10_tier_b_repair/evidence/checkpoints/t2_{{batch_id}}_review.md` (已存在则 append `## attempt N`):
  verdict PASS / CONDITIONAL / FAIL (CONDITIONAL 必附可执行修正清单); 命令与 exit code / 关键输出行 (可复跑);
  问题表 `| ref (atom_id / diff 行 / census 格) | 检查项 | 问题 | 证据 (PDF 页 + ≤25 词) |`; 人工逐格表; R2 recheck 判定表; G-TB6 结构行签字清单.
- trace append 一行到 `.work/10_tier_b_repair/trace.jsonl`:
  `{"ts": "<UTC ISO>", "step": "T2.{{batch_id}}", "event": "subagent_done", "agent": "oh-my-claudecode:code-reviewer", "model": "opus", "attempt": {{attempt}}, "duration_s": null, "verdict": "<PASS|CONDITIONAL|FAIL>", "note": "G-TB4 <n 表 OK/差异>; G-TB6 <新增行数/无出处数>; recheck <n→RG>"}`
- 回给主控 ≤ 10 行.
