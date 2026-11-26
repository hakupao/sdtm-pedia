# T3 — B-PCPP / B-LB / B-CP CONDITIONAL 修正项 delta 复审

> 状态: **已完成** (2026-11-26) · reviewer: oh-my-claudecode:code-reviewer (只读; 本文件是唯一写入) · 基线: HEAD e1f0cef
> 范围: 只看 trace.jsonl :45 / :56 / :63 code-reviewer 列出的修正项是否落地、附近有无残留; 不重审整批.
> PDF 页文本: `.work/10_tier_b_repair/work/pdf_pages/ig34_pNNNN.txt` (下文简写 `$P`). 行号是 HEAD 的行号 (后续 T2S 批移动过, 按内容定位).

## 总结

| 批 | 修正项 | 结论 |
|---|---|---|
| B-PCPP (97e1895) | 3 项全部落地, 与 PDF 一致, 无残留 | **PASS** |
| B-LB (470b473) | 1 项落地, 脚注只剩 1 份, 顺序与 PDF 一致 | **PASS** |
| B-CP (59d2451) | 1 项落地, 与 p208 一致 | **PASS** |

三个文件的结构检查 (表格列数逐行等于表头, 无相邻重复行): PP/examples.md 6 表 0 异常; LB/assumptions.md 1 表 0 异常; CP/examples.md 10 表 0 异常.
脚本见文末 R0.

## B-PCPP — PASS

| # | 修正要求 | HEAD 证据 | PDF 证据 | 判定 |
|---|---|---|---|---|
| 1 | 删除 Ex1 末尾自写指针 `> See [Example 2](#example-2) for this table (supppp.xpt; PDF p274 …)` | `knowledge_base/domains/PP/examples.md` Ex1 表最后一行 (Row 24) (:39) 后接空行 + `## Example 2` (:41), 全文 grep 该指针 0 命中; 97e1895 与 HEAD 均 0 命中 | p273 Ex1 只有 pp.xpt, 后接 "Example 2" | 落地 |
| 2 | PP:167 页码 `(pp 278-280)` → `(pp 278-279)` | `PP/examples.md:165` `### Method D — One to One, Using PCSEQ and PPSEQ (pp 278-279)`; 97e1895 之前是 `278-280` | `$P/ig34_p0278.txt:56` "Method D (One to One…)" 起; `$P/ig34_p0279.txt:35` "Example 2" 止 | 落地 |
| 3 | Ex2 Row 4 截断句补齐 | `PP/examples.md:46` 句末 "…liberates the PPTEST variable from having to house hyper-specific, pre-coordinated PK parameter values." | `$P/ig34_p0273.txt:41-43` 同句; PDF 写 "pre-corrdinating", KB 写 "pre-coordinating" — 已登记 B-PCPP T-9 (`t2_B-PCPP.md:195`) | 落地 |

附近残留: 无. `PP/examples.md:108` 的 `> See [PC/assumptions.md](../PC/assumptions.md#pc-pp--relating-records) for this table.` 是另一条指针 (在 "PP Dataset for All Examples" 下, 原 review 签过的 D2 交叉引用); 目标 `PC/assumptions.md:40 ### PC-PP – Relating Records` 存在, 且 p277 那张表确实在 PC/assumptions.md:95 一带. 不算残留.

## B-LB — PASS

| 修正要求 | HEAD 证据 | PDF 证据 | 判定 |
|---|---|---|---|
| 删 `LB/assumptions.md` 原 56-57 的第二条 `> ¹In this column, an asterisk (*) …` 及其后空行 | `knowledge_base/domains/LB/assumptions.md` 中这条脚注只出现 1 次 (:52, 在通用表 :22-50 之后); 470b473 也只有 1 次 (:52) | `$P/ig34_p0196.txt:26` 通用表后的脚注 | 落地 |

后续变化 (不是回归): 后来的 S-SPC1 在 :52 之后补了 `## LB – Description/Overview` :54 / `## LB – Specification` :58 / `## LB – Assumptions` :62. 这和 PDF 顺序一致 (p241:38 Description → p242:1 Specification → 规格表 → p245:20 脚注 → p245:25 Assumptions). p245 那条脚注现在跟着 LB 规格表放在 `LB/spec.md:564`, assumptions.md 没有再出现第二份. 原 review 提的 "p245_a007 由 :52 命中" 这条理由已经被这次重排取代, 但结果没有重复也没有丢失.

## B-CP — PASS

| 修正要求 | HEAD 证据 | PDF 证据 | 判定 |
|---|---|---|---|
| `CP/examples.md:5` `CPGATE (Gate Name)` → `CPGATE (Gate)` | `knowledge_base/domains/CP/examples.md:5` 现为 "…CPMRKSTR (Marker String), CPGATE (Gate), CPGATDEF (Gate Definition)…"; 全文件 "Gate Name" 0 命中; 59d2451 已是 `CPGATE (Gate)` | `$P/ig34_p0208.txt:21` "CPGATE (Gate), CPGATDEF (Gate Definition)" | 落地 |

附带检查: `CP/assumptions.md:24` 仍写 `--GATE (Gate Name)`, 这与 `$P/ig34_p0199.txt:34` 原文一致, 是正确的, 不要连带改. 同一行的 `--BDAGNT` / `--GATDEF` 与 PDF 的 `--BNDAGT` / `--GATEDEF` 不同, 但已登记 S-SPC1 CP T-21 PDF_TYPO (`t3_errata.json:1163`), 不属于本复审范围.

## 45 条残留原子 (residual.txt) 是否受影响

`work/t3_audit_sets/residual.txt` 一共 46 行 = 45 条 C3 CONDITIONAL + 1 条 pending (ig34_p0056_a006, B-ch04, 与这三批无关; `step_T3_audit_prep.md:21`).
45 条分布: LB p195/196/247 共 9 条, CP p210-220 共 17 条, PC/PP p270/271/277 共 19 条.

**修正项不会影响它们**: 五处修正只动了 p273 (PP Row 4)、p278-279 (Method D 页码)、无 PDF 出处的指针行、p196/p245 脚注、p208 (CP 导语). 45 条残留的页码里没有 p208/p273/p278/p279/p245. p196 只有 ig34_p0196_a006 (--LOBXFL 表行), 不是脚注行, 删脚注碰不到它.

**为什么 45 条都还是 MISS**: 按原子 verbatim 归一化后做子串匹配, 只有 ig34_p0277_a003 (PP 表头) 命中 `PC/assumptions.md`, 其余 44 条 MISS. 主要原因是旧 extractor 的 verbatim 本身不准: 例如 p0196_a006 写 "Operationally defined", PDF 是 "derived"; p0247_a021 写 "PtFtv / 1999-05-15", PDF 是 "PrThr / 1999-06-19"; p0277_a007 写 "PPSEQ 4 … DY1DRGX", PDF 是 "PPSEQ 5 … OTHER"; p0214_a014 的列已经错位. 另一个原因是表行的空格分布不同. 所以 MISS 不代表 KB 有错, 要对 PDF 页文本逐格核对.

**抽样 6 条 (要求 5 条), KB 与 PDF 逐格/逐字核对:**

| 原子 | 批 | KB 位置 | PDF 位置 | 结果 |
|---|---|---|---|---|
| ig34_p0195_a004 (LIST_ITEM) | LB | `LB/assumptions.md:14` | `$P/ig34_p0195.txt:8` | 逐字一致 ("o" 子弹 → 二级 `  - `) |
| ig34_p0196_a006 (--LOBXFL 行) | LB | `LB/assumptions.md:43` | `$P/ig34_p0196.txt:13-14` | 7 格一致 ("Operationally derived"; 原子 verbatim 写错) |
| ig34_p0247_a021 (HCG Row 1) | LB | `LB/examples.md:69` | `$P/ig34_p0247.txt:70-72` | 29 格一致 (PrThr / 2106-3 / 1999-06-19T04:00 / LBPTFL Y) |
| ig34_p0211_a009 (SENTENCE) | CP | `CP/examples.md:81` | `$P/ig34_p0211.txt:26-29` | 一致; KB 补了闭合括号 `")` = 已登记 B-CP T-1 (`t2_pdf_typo_registry.jsonl:21`) |
| ig34_p0214_a014 (Row 7 Stimulation Index) | CP | `CP/examples.md:165` | `$P/ig34_p0214.txt:32-34` (按表头 :13 列位对齐) | 30 格一致 (CPTSTCND 空, CPCNDAGT "MACROPHAGE INFLAMMATORY PROTEIN 1BETA", CPANMETH STIMULATED/UNSTIMULATED) |
| ig34_p0277_a007 (PP Row 4) | PCPP | `PC/assumptions.md:95` | `$P/ig34_p0277.txt:7` | 20 格一致 (PPSEQ 5, DY1DRGX_HALF, OTHER, 4.69 h) |

结论: 抽样 6/6 与 PDF 一致. C3 拦下这 45 条的唯一理由是 "CONDITIONAL 之后缺 reviewer 复审 delta"; 本复审三批都给 PASS, 这个理由可以解除. 是否据此改写这 45 条的 v, 由主控按 T3 口径决定, 本文件不改 ledger.

## 发现 (按严重度)

- 无 CRITICAL / HIGH / MEDIUM.
- [LOW, 置信度 HIGH] `t2_B-LB_review.md` 修正清单写的理由 "p245_a007 由 :52 命中" 已经被 S-SPC1 重排取代 (p245 脚注现在在 `LB/spec.md:564`). 结果是对的, 只是那条理由过时了. 建议: 如果 T3 要引用这条依据, 改为引用 spec.md:564.
- [LOW, 置信度 MEDIUM] residual 原子的 verbatim 有多处 extractor 错误 (见上). 如果 T3 用 "子串命中" 来自动解除残留, 这 44 条不会命中, 需要按本表这样人工对照 PDF. 建议: 在 T3 口径里写明以 PDF 页文本为准, 不以原子 verbatim 为准.

## 可复跑命令 (repo 根; P=.work/10_tier_b_repair/work/pdf_pages)

```
# B-PCPP
grep -n -E 'See \[Example 2\]|supppp.xpt; PDF' knowledge_base/domains/PP/examples.md      # 期望 0 行
git show 97e1895:knowledge_base/domains/PP/examples.md | grep -c 'See \[Example 2\]'         # 0
grep -n 'Method D' knowledge_base/domains/PP/examples.md                                     # :165 (pp 278-279)
grep -n 'Method D' $P/ig34_p0278.txt; grep -n '^Example 2' $P/ig34_p0279.txt                 # p278:56 / p279:35
grep -n 'liberates' knowledge_base/domains/PP/examples.md; sed -n 41,43p $P/ig34_p0273.txt
# B-LB
grep -c 'In this column, an asterisk' knowledge_base/domains/LB/assumptions.md               # 1
grep -n 'In this column, an asterisk' $P/ig34_p0196.txt $P/ig34_p0245.txt knowledge_base/domains/LB/spec.md
grep -n '^## ' knowledge_base/domains/LB/assumptions.md
# B-CP
sed -n 5p knowledge_base/domains/CP/examples.md | grep -o 'CPGATE ([^)]*)'                   # CPGATE (Gate)
grep -c 'Gate Name' knowledge_base/domains/CP/examples.md                                    # 0
sed -n 21p $P/ig34_p0208.txt; sed -n 34p $P/ig34_p0199.txt
# 抽样
sed -n 14p knowledge_base/domains/LB/assumptions.md; sed -n 8p $P/ig34_p0195.txt
sed -n 43p knowledge_base/domains/LB/assumptions.md; sed -n 13,14p $P/ig34_p0196.txt
sed -n 69p knowledge_base/domains/LB/examples.md; sed -n 70,72p $P/ig34_p0247.txt | tr -s ' '
sed -n 81p knowledge_base/domains/CP/examples.md; sed -n 26,29p $P/ig34_p0211.txt
sed -n 165p knowledge_base/domains/CP/examples.md; sed -n 13p $P/ig34_p0214.txt; sed -n 32,34p $P/ig34_p0214.txt
sed -n 95p knowledge_base/domains/PC/assumptions.md; sed -n 7p $P/ig34_p0277.txt
```

R0 结构检查 (表格列数 + 相邻重复行), 脚本内容:
```
python3 - knowledge_base/domains/PP/examples.md knowledge_base/domains/LB/assumptions.md knowledge_base/domains/CP/examples.md <<'PY'
import sys,re
for f in sys.argv[1:]:
    L=open(f).read().split('\n'); n=None; bad=0; t=0
    for i,l in enumerate(L,1):
        if l.startswith('|'):
            c=len(re.split(r'(?<!\\)\|',l.strip()))-2
            if n is None: n=c; t+=1
            elif c!=n: print(f,i,c,n); bad+=1
        else: n=None
    print(f,'tables',t,'bad',bad,'dup',[i+1 for i in range(1,len(L)) if L[i].strip() and L[i]==L[i-1]])
PY
# 实测输出: PP 6/0/[]; LB 1/0/[]; CP 10/0/[]
```
