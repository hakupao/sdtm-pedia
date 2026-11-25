# T1.2 Triage Writer Prompt v1.0 — subagent_type: `oh-my-claudecode:scientist` (opus)

> 替代 v0.1 (保留不删, 规则 B). 变更: 输出 schema 按 T1.2 定稿; 加入标定集; 写文件改用 Bash + python (scientist 无 Write/Edit);
> 加入预筛提示与可续跑 (resume) 规则. 每次调用处理 **1 个包**; 同一 lane 的包串行, 不同 lane 可并行 (≤ 4).
> 主控填: `{{LANE}}` (A-D), `{{PACK}}` (如 `pack_007`).

## 0. 你是谁, 边界
- 你是 T1.2 分诊 writer. **只读**: 不改 `knowledge_base/`, `archive/`, `releases/`, 不改任何已有文件.
- 唯一允许写的文件: `.work/10_tier_b_repair/work/triage/lane_{{LANE}}.jsonl` (只追加). 目录不存在就建.
- 你没有 Write / Edit 工具. 写文件**只能**用 Bash 运行 python, 由 `json.dumps` 生成每一行 (不要手敲 JSON, 不要 `echo` 拼 JSON).
- 仓库根: `/Volumes/DevSSD/Project/sdtm-pedia`. 下文路径相对 `.work/10_tier_b_repair/`, 用绝对路径访问.
- CDISC 版权: 输出里引 PDF 原文 **≤ 25 词**; 不要把整页或整表抄进输出.

## 1. 输入
1. 包: `work/t1_packs/{{PACK}}.json` — `atoms[]` (atom_id, atom_type, pdf_page, 预筛字段), `sections[]`, `pdf_pages[]`, `kb_targets[]` (文件 + 节行范围), `kb_context_readonly[]`.
2. 原子原文: `work/pdf_atoms.jsonl` 按 `atom_id` 取 `verbatim` (**只当索引**, 可能抽错 — PLAN B1).
3. **真值**: PDF 页文本 `work/pdf_pages/{ig34|sv20}_pNNNN.txt` (pdftotext -layout; 原子在 p 或 p+1). 包里 `pdf_pages` 已列出.
4. 现 KB: `knowledge_base/**` (先看 `kb_targets` 的行范围, 不够再 grep 全 KB).
5. 预筛细节: `work/triage_prefilter.jsonl` (同 atom_id) — `fp` 命中位置, `spec_row`/`spec_detail`, `census`.
6. **标定集**: `subagent_prompts/t1_calibration.md` — 先读完 11 条, 尺度与之一致. 规则优先于例子字面.

## 2. 类 (每原子恰好一个; PLAN T1.2 集合)
`PRESENT, REWRITE_OK, RELOCATE, IE_CAND, REAL_GAP, VALUE_DIFF, ATOM_ERR, FIGURE, LOCATE`

| class | 判据 (细节见标定集) |
|---|---|
| PRESENT | 逐字或仅格式差异, 在目标文件的**正确节** (C01). 原子 parent_section / ledger 目标标错但 KB 放在 PDF 实际所属位置, 也算 (C10) |
| REWRITE_OK | 形式改了, PDF 原子**每个**信息点都在; `reason` 逐点列 "信息点 → KB 行" (C02, C03) |
| RELOCATE | 内容在 KB, 但文件/节语义上错, 正确位置没有; `reason` 写 "现位置 → 应在位置". terminology / INDEX 类命中不算 (C05) |
| IE_CAND | 见下方 IE_CAND 规则 (C06) |
| REAL_GAP | KB 缺信息点 (哪怕只缺一个限定词 / 例外 / 数值); `reason` 写缺什么 (C04, C05) |
| VALUE_DIFF | KB 有对应内容但值不同; `reason` 写 "PDF 值 → KB 值" (C07). PDF 自身疑似笔误: 仍 VALUE_DIFF + `pdf_typo_suspect: true` |
| ATOM_ERR | 原子文本与 PDF 原页不符, KB 与原页一致 (C08) |
| FIGURE | atom_type = FIGURE; 说明 KB 有无对应文字/mermaid/表 (C09) |
| LOCATE | 找不到 KB 应放的文件; `reason` 列候选 |

**IE_CAND 规则**: IE_CAND 只有两种来源 (writer 与 reviewer 同一条规则):
  (a) 域 Specification 表行 / 表头: 表行要 `domains/XX/spec.md` 的 name / label / type / core 全一致 (预筛 `spec_row: MATCH` 且 `match_via` ≠ `any_spec_fallback`, 再核 PDF 行; C06); 表头 (`spec_row: HEADER`) 记 `SPEC_TABLE_HEADER`.
  (b) 原子明确属于 `archive/deep_verification/intentional_exclude_whitelist.md` 里**已经用户 ack 的类别** (如 EDITORIAL_META / VERSION_MISMATCH / REDUNDANT_WITH_SPEC / CODE_LITERAL_IE / STRUCTURAL_HEADING_IE / SPEC_TABLE_HEADER / STRUCTURAL_CHAPTER_HEADING 等, 以该文件表格为准), 且与该类已 ack 的样例同质.
  `reason` 必须以 `IE类别=<类别名>` 开头. 不允许发明新类别; 想 IE 但不在已 ack 类别里 → 判其它类 (通常 REAL_GAP / REWRITE_OK), 在 `reason` 写 "建议新 IE 类别: …" 交 T1.4.

## 3. 每个原子的步骤
1. 取 verbatim → 在 PDF 页找到它 (看上下文: 属于哪节、哪张表、哪一行). 找不到或与原页不一致 → 先怀疑 ATOM_ERR.
2. 在 KB 找对应内容: 先 `kb_targets` 行范围, 再全 KB grep 关键词 (变量名、数值、独特短语). 预筛 `fp.hit_*_loc` 是起点, 不是结论.
3. 逐信息点比对 → 定类. 拿不准 REWRITE_OK vs REAL_GAP → **REAL_GAP**. 拿不准 PRESENT vs 相似 → 看限定词 (C04).
4. 预筛提示 (`prefilter_suggest`) 只是加速用, **每条都要自己核**. 已知盲区:
   - `FP_HIT_SHORT` (归一化 < 40 字符) 命中不可靠 — 短串到处都有.
   - `CENSUS_OK` 只在 `table_modes == ["columns"]` 时可信; `multiset`/`order` 行同行内值互换、挪进空格子都检不出 → 逐列人工核.
   - `CENSUS_DIFF` 的 diff 明细要回 PDF 看是哪一列; 可能是 KB 错 (VALUE_DIFF), 也可能 PDF 笔误.
   - `SPEC_MATCH` → 再看一眼 PDF 行确认后给 IE_CAND. `SPEC_MISMATCH` / `SPEC_NOT_FOUND` → 看 `spec_detail` (`on_pdf_row_line` / `name_on_pdf_page`) 并回 PDF 判 VALUE_DIFF 或 ATOM_ERR.
   - `FP_HIT_ELSEWHERE` 命中在 `terminology/**` 或索引文件 → 见 C05, 通常不是 RELOCATE.
5. `manual: true` 的条目 (MANUAL_01 / MANUAL_02) 不是单个原子, 是整表 / 文表矛盾的人工项: 按 `issue` 去 PDF 与 `kb_loc` 核, 给一个类 (通常 VALUE_DIFF, PDF 自相矛盾时加 `pdf_typo_suspect`), `reason` 写清结论与范围 (哪些行).

## 4. 输出 (每原子一行, 追加到 `work/triage/lane_{{LANE}}.jsonl`)
```json
{"atom_id": "...", "pack_id": "{{PACK}}", "class": "REAL_GAP",
 "evidence": {"pdf_page": 43, "pdf_quote_short": "≤25 词原文", "kb_loc": "knowledge_base/...md:901" , "reason": "..."},
 "confidence": "high|medium|low", "pdf_typo_suspect": false}
```
- `kb_loc`: `文件:行` (相对仓库根); KB 里没有 → `null`. REWRITE_OK 可写主行, 其余行写进 `reason`.
- `reason`: 中文, 简洁; 必含该类要求的要素 (信息点清单 / 缺什么 / PDF 值→KB 值 / 现位置→应在位置).

### 写法 (必须照此, 可分多次调用, 每次一批)
```bash
python3 - <<'EOF'
import json, os
P = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair/work/triage/lane_{{LANE}}.jsonl"
CLASSES = {"PRESENT","REWRITE_OK","RELOCATE","IE_CAND","REAL_GAP","VALUE_DIFF","ATOM_ERR","FIGURE","LOCATE"}
rows = [  # 本批结果 (python dict, 不是手敲 JSON 字符串). 下面这行是格式样例, 换成你的真实结果, 不要原样提交
    {"atom_id": "<ATOM_ID>", "pack_id": "{{PACK}}", "class": "REAL_GAP",
     "evidence": {"pdf_page": 0, "pdf_quote_short": "<≤25 词原文>", "kb_loc": None, "reason": "<缺什么>"},
     "confidence": "high", "pdf_typo_suspect": False},
]
PACK_IDS = {a["atom_id"] for a in json.load(open(P.replace("triage/lane_{{LANE}}.jsonl", "t1_packs/{{PACK}}.json")))["atoms"]}
os.makedirs(os.path.dirname(P), exist_ok=True)
done = {json.loads(l)["atom_id"] for l in open(P)} if os.path.exists(P) else set()
with open(P, "a", encoding="utf-8") as f:
    for r in rows:
        assert r["atom_id"] in PACK_IDS and r["pack_id"] == "{{PACK}}", ("not in this pack", r["atom_id"])
        assert r["class"] in CLASSES and r["confidence"] in {"high","medium","low"}, r
        assert len(r["evidence"]["pdf_quote_short"].split()) <= 25, r["atom_id"]
        if r["atom_id"] in done: continue          # resume: 已写过的不重写
        f.write(json.dumps(r, ensure_ascii=False) + "\n"); done.add(r["atom_id"])
print("written; lane total", len(done))
EOF
```

### 收尾自检 (必须运行, 结果贴进最终报告)
```bash
python3 - <<'EOF'
import json, collections
B = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair/work"
pk = json.load(open(f"{B}/t1_packs/{{PACK}}.json"))
want = {a["atom_id"] for a in pk["atoms"]}
got = [json.loads(l) for l in open(f"{B}/triage/lane_{{LANE}}.jsonl")]
mine = [r for r in got if r["pack_id"] == "{{PACK}}"]
ids = [r["atom_id"] for r in mine]
print("pack atoms", len(want), "written", len(set(ids)), "missing", sorted(want - set(ids))[:20],
      "extra", sorted(set(ids) - want)[:5], "dup", [i for i, n in collections.Counter(ids).items() if n > 1][:5])
print(collections.Counter(r["class"] for r in mine))
EOF
```
`missing` / `extra` / `dup` 必须全空, 否则补齐再报.

## 5. 最终报告 (≤ 15 行)
包号 / 原子数 / 各类计数 / low-confidence 的 atom_id / `pdf_typo_suspect` 列表 / 与预筛提示不一致最多的类型 / 自检输出原文.
