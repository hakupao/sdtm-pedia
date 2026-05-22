# A3.1 — Claude Pipeline Fix (extract_examples_data.py capture ## §N.N.N section headings)

> Phase: A.A3.1 (sub-step of A3 Claude clean rewrite)
> Date: 2026-05-20 PM
> Operator: main session (not subagent — A3 writer subagent 显式 NOT modify dev/scripts/*)
> Rule D slot: N/A (main session direct edit; A5 reviewer 会 cross-check 在 reviewer pass)

## 背景

v1.3 RETRO §二.3 finding: `claude_projects/` 的 `07_examples_catalog.md` (by archive v1 `catalog_examples.py`) + `09_examples_data_high.md` (by v2 `extract_examples_data.py`) 都只 capture `## Example N` H2 headings. 其他 H2 (含 `## §6.3.5.9.3 RELREC Method Quick Reference` PP-side view) 被 silently dropped (catch-all "anything else: drop" branch line 374-382).

实际影响超出 v1.3 RETRO 描述 — pre-fix grep 显示 3 个 domain 受影响:
- **PP/examples.md L129** `## §6.3.5.9.3 RELREC Method Quick Reference (PP-side view)` — v1.3 A1 新增, RETRO §二.3 已识别
- **PC/examples.md L7** `## §6.3.5.9.3 Relating PP Records to PC Records — Worked Examples` — PC 唯一 H2 (无 `## Example`), 整文件之前被 silently dropped
- **MB/examples.md L171** `## §6.3.5.7.3 Microbiology Specimen and Microbiology Susceptibility Examples` — 之前被 dropped

## Fix

`ai_platforms/claude_projects/dev/scripts/extract_examples_data.py` 4 处改动:

### Edit 1: docstring (line 12-15)
加 `Each ## §N.N.N section heading (...) -> #### §N.N.N (v1.4 A3.1 pipeline fix)` 在 Keeps 列表.

### Edit 2: regex constant (after line 96)
```python
# Regex: ``## §N.N.N`` style section headings (v1.4 A3.1 pipeline fix).
SECTION_HDR_RE = re.compile(r"^##\s+§\d+(\.\d+)+\b")
```

### Edit 3: Pass 1 break condition (line 258)
```python
# Before:
while i < n and not EXAMPLE_HDR_RE.match(lines[i]):
# After:
while i < n and not EXAMPLE_HDR_RE.match(lines[i]) and not SECTION_HDR_RE.match(lines[i]):
```

### Edit 4: main loop new handler (after EXAMPLE_HDR_RE handler ~line 320)
新 if branch mirror EXAMPLE_HDR_RE 处理逻辑, remap `## §N.N.N ...` → `#### §N.N.N ...` + capture first-description + 后续 tables / filenames / H3 sub-headings (existing logic).

## Rule A smoke test (3 probes)

| Probe | Domain | Pre-fix | Post-fix | Verdict |
|:-:|---|---|---|:-:|
| 1 | PP §6.3.5.9.3 RELREC Method Quick Reference (L129) | dropped (15K+ → output 含 §) | `#### §6.3.5.9.3 RELREC Method Quick Reference (PP-side view)` emitted, body description "The full 4 worked Examples..." preserved | ✅ PASS |
| 2 | PC §6.3.5.9.3 Relating PP Records to PC Records (L7) | dropped (whole-file → `(no data tables in source)` placeholder OR near-empty) | `#### §6.3.5.9.3 Relating PP Records to PC Records — Worked Examples` emitted, body + cross-ref preamble note `*Note: PC and PP share...*` preserved | ✅ PASS |
| 3 | MB §6.3.5.7.3 Microbiology Specimen Examples (L171) | dropped (Example 1-3 captured, §6.3.5.7.3 后 content silently dropped) | `#### §6.3.5.7.3 Microbiology Specimen and Microbiology Susceptibility Examples` emitted | ✅ PASS |

## Smoke test command

```bash
python3 -c "
import sys
sys.path.insert(0, 'ai_platforms/claude_projects/dev/scripts')
from extract_examples_data import extract_domain
from pathlib import Path
for d in ['PP', 'PC', 'MB']:
    text = Path(f'knowledge_base/domains/{d}/examples.md').read_text(encoding='utf-8')
    out = extract_domain(d, text)
    has_section = '§' in out
    print(f'{d}: {len(out)} chars, has §: {has_section}')
    for ln in out.splitlines():
        if '§' in ln:
            print(f'  → {ln[:120]}')
"
```

Output:
```
PP: 15799 chars, has §: True
  → #### §6.3.5.9.3 RELREC Method Quick Reference (PP-side view)
  → The full 4 worked Examples (1-4) with complete `relrec.xpt` tables for all 4 Methods (A/B/C/D) appear in `PC/examples.md
PC: 17275 chars, has §: True
  → *Note: PC and PP share a combined examples section (§6.3.5.9.3 Relating PP Records to PC Records). The shared PC/PP data
  → #### §6.3.5.9.3 Relating PP Records to PC Records — Worked Examples
MB: 24732 chars, has §: True
  → #### §6.3.5.7.3 Microbiology Specimen and Microbiology Susceptibility Examples
```

## Regression risk verify

Patch ADDS new branch (`SECTION_HDR_RE` handler) — 不修改 existing `EXAMPLE_HDR_RE` handler. Existing behavior on `## Example N` headings 不变 (all 63 domain examples.md 现行解析 byte-identical).

`SECTION_HDR_RE = r"^##\s+§\d+(\.\d+)+\b"` 严格 match `## §digits.digits...`, 不 match `## Pharmacokinetic Parameters (PP) Dataset for All Examples` (PP L106 narrative H2) — 故意保留 catch-all drop 行为 for narrative H2.

Pass 1 break condition 修改影响:
- PP: Pass 1 仍 break at L7 (`## Example 1`), 同 before
- PC: Pass 1 break at L7 (`## §6.3.5.9.3 ...`), 之前 break at EOF (无 `## Example`)
- MB: Pass 1 break at L3 (`## Example 1`), 同 before
- 其他 60 domains (无 `## §N.N.N`): 行为不变

## Next step

Phase B Claude bundle rebuild (B2 v1.3 等价) 将 trigger 真实 build pipeline:
- `extract_examples_data.py --tier high --domain-list <D1>` 生成新 `09_examples_data_high.md`
- 验证 09 output 含 `#### §6.3.5.9.3` × 2 (PP + PC) + `#### §6.3.5.7.3` × 1 (MB)
- Cross-platform delta oracle: 比较 09 byte delta vs v1.3 baseline, expected ~3-10 KB 增量 (新增 3 段 + tables, conservative cap)

A3.1 完成. 等 A3 writer subagent 完成 prompt rewrite, 然后一并进 A5 reviewer pass.
