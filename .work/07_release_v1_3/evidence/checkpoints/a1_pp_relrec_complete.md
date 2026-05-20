# A1 — PP RELREC linking 2 atoms 补全 (G5)

> Date: 2026-05-20
> Phase: A — KB layer fixes
> Step: A1
> Predecessor: 06 P7 OA-4 (RETROSPECTIVE.md §二 5)
> Status: PASS

---

## 1. Carry 来源

06 deep verification P7 (2026-05-12) 人工抽样 60 原子, 2 条 CONTENT 缺口:

| Atom ID | PDF | parent_section | verbatim |
|---|:-:|---|---|
| ig34_p0278_a035 | p278 | §6.3.5.9.3 Relating PP Records to PC Records — Example 1 | `2 \| ABC-123 \| PP \| ABC-123-0001 \| PPSEQ \| 1 \| \| 1` |
| ig34_p0278_a040 | p278 | (同上) | `7 \| ABC-123 \| PP \| ABC-123-0001 \| PPSEQ \| 6 \| \| 1` |

Coverage_ledger 当时打 EQUIVALENT 但 similarity=0.5 (低质匹配, 实质未入 PP/examples.md). 06 retro §二 5 描述: "PP RELREC 链接示例 (ABC-123-0001/PPSEQ=1 和 PPSEQ=6) 未入 KB 的 PP/examples.md".

## 2. 诊断 (本 step)

a035-a041 实际是 **Example 1 Method C (Many-to-One, PCGRPID+PPSEQ) relrec.xpt** p278 7 行 — a035 (PPSEQ=1) 和 a040 (PPSEQ=6) 只是 P7 60 原子抽样命中的 2 条 sample, 全 7 行都在同一 gap.

`PC/examples.md` (PC/PP 共享 §6.3.5.9.3 host) 已含完整 Methods A/B/C/D + 4 完整 relrec.xpt tables. 但 `PP/examples.md` L129+ 原 "RELREC Method Descriptions" 段:

- 缺 Method D 描述
- 缺所有 relrec.xpt 示例表 (含 a035/a040 7 行)
- 页码错: 标 "Section 6.3.5.9.3, pp 281-282" — 281-282 是 Examples 2-3 + 总表, 而 Example 1 Methods A/B/C/D 在 277-280
- Method C 描述也有源文 typo ("PGRPID values DY1_DRGX_A and DY1_DRGX_B" — 应是 PCGRPID 单值)

## 3. 修复 (PP/examples.md L128 onwards)

### 3.1 改前 (17 行, L128-144)

```
## RELREC Method Descriptions (Section 6.3.5.9.3, pp 281-282)
### Method B — One to Many, Using PCSEQ and PPGRPID (p281)
### Method C — Many to One, Using PCGRPID and PPSEQ (p281)
### Method A — Many to Many, Using PCGRPID and PPGRPID (Example 4, p282)
```
(Method D 缺; 无 relrec.xpt 表; 页码错)

### 3.2 改后 (51 行, L129-181)

```
## §6.3.5.9.3 RELREC Method Quick Reference (PP-side view)
### Method A — Many to Many, Using PCGRPID and PPGRPID (p277)
### Method B — One to Many, Using PCSEQ and PPGRPID (pp 277-278)
### Method C — Many to One, Using PCGRPID and PPSEQ (p278)
  + relrec.xpt abbreviated table (8 行: 1 PC group row + 7 PP individual rows PPSEQ=1..7)
### Method D — One to One, Using PCSEQ and PPSEQ (pp 278-280)
### Cross-domain summary (Examples 2-4 on pp 281-284)
```

文件总长 144 → 181 行 (+37). 仅 §6.3.5.9.3 段重写, 上面 3 个 Example 主体 (含 supppp.xpt 等) 不动.

## 4. Rule A N=3 verbatim 抽检

| # | Probe atom | PDF verbatim | KB after-fix grep result | Match |
|:-:|---|---|---|:---:|
| 1 | ig34_p0278_a035 (PPSEQ=1, row 2) | `2 \| ABC-123 \| PP \| ABC-123-0001 \| PPSEQ \| 1 \| \| 1` | `\| 2 \| ABC-123 \| PP \| ABC-123-0001 \| PPSEQ \| 1 \| \| 1 \|` | ✅ |
| 2 | ig34_p0278_a040 (PPSEQ=6, row 7) | `7 \| ABC-123 \| PP \| ABC-123-0001 \| PPSEQ \| 6 \| \| 1` | `\| 7 \| ABC-123 \| PP \| ABC-123-0001 \| PPSEQ \| 6 \| \| 1 \|` | ✅ |
| 3 | ig34_p0278_a041 (PPSEQ=7, row 8) | `8 \| ABC-123 \| PP \| ABC-123-0001 \| PPSEQ \| 7 \| \| 1` | `\| 8 \| ABC-123 \| PP \| ABC-123-0001 \| PPSEQ \| 7 \| \| 1 \|` | ✅ |

**3/3 PASS** — verbatim byte-exact (markdown table 列 `|` 边界为 markdown 渲染添加, 与 PDF 字段一致).

注: KB 用 markdown 表格语法在每行两端各加一个 `|`, PDF 原文用列分隔符 `|`. 字段内容 byte-exact 一致, 是 markdown 格式约定差异不是内容差异.

## 5. 验证

| 维度 | 状态 |
|---|---|
| PP/examples.md 现含 §6.3.5.9.3 Methods A/B/C/D 完整 4 种 PP-side 视角 | ✅ |
| Method C relrec.xpt 含 PPSEQ=1..7 (a035-a041 全 7 atom 命中) | ✅ |
| 页码引用从 281-282 (错) → 277-284 (正确, 4 Examples 分布 p277-280, summary p281-284) | ✅ |
| 与 PC/examples.md 不重复 (PP 只给 abbreviated 1 table, 全 4 table 仍在 PC) | ✅ |
| 维持 cross-ref note "*See PC examples for the full description...*" (L127) | ✅ |
| Rule A N=3 verbatim PASS | ✅ |
| 0 hallucination (所有 description bullet + table row 均来自 PDF p277-284) | ✅ |

## 6. Carry status post-fix

- 06 retro §二 5 (OA-4): **RESOLVED** ★
- KNOWN_LIMITATIONS §0 D-? entry (若有): N/A (PP RELREC OA-4 未公开)
- v1.3 PLAN.md Phase A A1 gate: **PASS** ✅

## 7. 下一步

- A2 — BECAT EXTRACTION prompt-KB 分叉修复 (D3)
- 默认走 α (改 KB, 在 BE/spec.md L111 附近加 EXTRACTION 作为第 4 sponsor-extensible 例)
