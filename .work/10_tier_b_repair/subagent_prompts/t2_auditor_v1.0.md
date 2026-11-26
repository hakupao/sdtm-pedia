# T2 Auditor Prompt v1.0 — subagent_type: `oh-my-claudecode:verifier` (Rule A 独立抽检; 与本批 writer / reviewer 都不同)

> v0.1 保留不改. v1.0 改动: 抽样总体 / N / 种子写成可复跑命令; 判据加 R2; 证据由你用 Bash 落盘 (本 agent 类型无 Write/Edit, **禁止改 KB**).
> 派发后完整 prompt 另存 `t2_auditor_<batch>_attempt_N.md`. 工作目录 = repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`.

## 输入
- `.work/10_tier_b_repair/work/t2_batches/{{batch_id}}.json`; 改动后的 KB (`git diff {{base_commit}} -- knowledge_base/`)
- `.work/10_tier_b_repair/work/triage_merged.json` (全部分诊, 含 T1.4 裁定); `work/pdf_atoms.jsonl` (原子索引, 真值仍是 PDF 页)
- PDF 原页 `.work/10_tier_b_repair/work/pdf_pages/`; 版面问题渲染原页 (`pdftoppm -f N -l N -r 110 -png`)
- **不读** writer / reviewer 的报告再下结论 (先独立判, 判完才可对照)

## 抽样 (PLAN §5.3; 只抽 prose, 表格由 reviewer 全检)
- prose = atom_type ∈ SENTENCE / LIST_ITEM / NOTE / CROSS_REF.
- 改动集 C = 本批 `atoms[]` + `t2_recheck[]` 中的 prose; 总体 P = C ∪ triage_merged 里 (target 或 kb_loc) 落在本批 kb_files 的 prose ∪ `pdf_atoms` 里页码在本批 `pdf_pages` 的 prose
  (含本项目没碰过的原子 = 对照), 去掉 triage 类 IE / ATOM_ERR / FIGURE、ledger verdict = INTENTIONAL_EXCLUDE、以及**属于别的批**的待修原子 (同页跨域, 如 p263 MB/MI).
  (B-PCPP 这类改动全是表格的批, C=0 时 P 仍 ≥ 10.) 对照原子 (不在 C) 若判丢失且其位置在本批 kb_files 外 → 记 "范围外发现", 不算本批 FAIL; 在 kb_files 内 → 照常计入.
- N = max(10, ceil(0.2 × |C|)), 上限 30, 且 ≤ |P|. 先从 C 抽 min(|C|, ceil(N/2)), 余数从 P − C 抽 (样本不限于 writer 声明的改动). 种子 = `{{seed}}`.
```
S=.work/10_tier_b_repair/work/scratch/t2/{{batch_id}}_auditor; mkdir -p $S
python3 -I - <<'EOF' > $S/sample.json
import json, math, random
TB = ".work/10_tier_b_repair"; b = "{{batch_id}}"; seed = {{seed}}
J = json.load(open(f"{TB}/work/t2_batches/{b}.json")); M = json.load(open(f"{TB}/work/triage_merged.json"))
T = {json.loads(l)["atom_id"]: json.loads(l)["atom_type"] for l in open(f"{TB}/work/pdf_atoms.jsonl")}
PR = {"SENTENCE", "LIST_ITEM", "NOTE", "CROSS_REF"}; files = set(J["kb_files"])
C = sorted(a["atom_id"] for a in J["atoms"] + J["t2_recheck"] if T.get(a["atom_id"]) in PR)
A = [json.loads(l) for l in open(f"{TB}/work/pdf_atoms.jsonl")]
IEL = {json.loads(l)["pdf_atom_id"] for l in open(f"{TB}/work/coverage_ledger.wc.jsonl") if json.loads(l)["verdict"] == "INTENTIONAL_EXCLUDE"}
X = {r["atom_id"] for r in M if r["final_class"] in ("IE", "ATOM_ERR", "FIGURE")} | IEL
P = {r["atom_id"] for r in M if T.get(r["atom_id"]) in PR and (r.get("target") or r["kb_loc"] or "").split(":")[0] in files}
P |= {a["atom_id"] for a in A if a["atom_type"] in PR and a["page"] in set(J["pdf_pages"]) and a["atom_id"].startswith(J["atoms"][0]["src"] if J["atoms"] else "ig34")}
import glob
OTH = {a["atom_id"] for f in glob.glob(f"{TB}/work/t2_batches/B-*.json") for B in [json.load(open(f))] if B["batch_id"] != b for a in B["atoms"] + B["t2_recheck"]}
P = sorted((P - X - OTH) | set(C)); N = min(30, max(10, math.ceil(0.2 * len(C))), len(P))
rng = random.Random(seed); s1 = rng.sample(C, min(len(C), math.ceil(N / 2))); rest = sorted(set(P) - set(s1))
print(json.dumps({"seed": seed, "C": len(C), "P": len(P), "N": N, "sample": s1 + rng.sample(rest, min(len(rest), N - len(s1)))}))
EOF
```

## 每个样本判 (G-TB5)
1. **独有信息丢失**: PDF 原页该原子的每个信息点 (主语、谓语含义、限定词、例外、数值、交叉引用) 是否都在 KB 目标节. R2: 改写丢掉的短语, 即使同节 / 同表行别处有, 也算丢失.
2. **忠实度**: KB 与 PDF 意思一致 — 无增 (自造说明 / 扩写如把 "…/etc." 展开)、无删、无改义.
3. **位置**: 在 PDF 所属节对应的 KB 节下.
4. 引文 ≤ 25 词/处 (CDISC 版权); 用 "PDF 页:行 + 摘要".

## 另查 (G-TB8)
- `trace.jsonl` 里本批已有 writer (`oh-my-claudecode:executor`) 与 reviewer (`oh-my-claudecode:code-reviewer`) 的 `subagent_done`, 且无 `agent: main` 写 KB 的记录.

## 输出 (Bash heredoc; 只写这两处 + scratch)
- `.work/10_tier_b_repair/evidence/checkpoints/t2_{{batch_id}}_audit.md` (已存在则 append `## attempt N`):
  抽样命令 + seed + C/P/N; 表 `| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |`;
  独有丢失数、忠实度错误数; **任一 > 0 → 本批 FAIL** (失败条目不删, 主控按规则 B 归档 `evidence/failures/`); G-TB8 结果. 同时把汇总行 append 到 `audit_matrix.md`.
- trace append: `{"ts": "<UTC ISO>", "step": "T2.{{batch_id}}", "event": "subagent_done", "agent": "oh-my-claudecode:verifier", "model": "opus", "attempt": {{attempt}}, "duration_s": null, "verdict": "<PASS|FAIL>", "note": "Rule A N=<n> seed=<s>: 丢失 <x> 忠实 <y>"}`
- 回给主控 ≤ 8 行.
