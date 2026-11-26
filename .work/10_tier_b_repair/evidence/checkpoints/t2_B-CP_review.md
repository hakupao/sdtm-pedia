# T2 B-CP reviewer (oh-my-claudecode:code-reviewer / opus) — attempt 1 (含 续)

**verdict: CONDITIONAL** (1 项可执行修正; 其余全部通过)

## 命令 (scratch = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_BCP_reviewer`, 仓外)
```
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  -> exit 1; status {'OK': 6, 'DIFF': 3, 'NO_PDF': 1}; cells 2681; diffs 31; 本批页 PDF_ONLY 仅 p199 bs.xpt (BS 域, 非本批)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  -> exit 1 RED; 13 回归: CP 仅 ig34_p0215_a018 (= 登记预期, T-2); 其余 12 条 p0257/0258/0260/0263 = MB 并行批
python3 tools/check_links.py | tail -2   -> live docs: 42 (≤ 42)
独立表格核对: $S/code/lay.py + cmp.py + cmp2.py (pdftotext -layout 列起始位置分列, 与 bbox 解析器无共用代码) + pdftoppm 渲染 (p210 200dpi 全页; p216/p217 300dpi 裁切)
G-TB6: $S/code/g6.py (diff 新增非表行按句 norm ∈ p205-220 pdf_pages); 删除: $S/code/del.py (diff 删除行按句 norm ∈ 改后 CP 两文件)
```

## 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| CP/examples.md:5 (ig34_p0208_a009) | 词替换型改写口径 | 保留 "CPGATE (Gate Name)"; writer 依据 "该行承载 p0208_a009+a010 (PRESENT/EXACT)" 不成立: a009 在 fp_after **未命中** (baseline 亦未命中), 改写词只在 a009 内, a010 是独立句不受影响 → 按口径应恢复 PDF 原词 | p208 "…CPMRKSTR (Marker String), CPGATE (Gate), CPGATDEF (Gate Definition)…" |
| CP/assumptions.md:100 | 交叉引用 (LOW, 可选) | 指针列 "Example 1a Rows 4-5, Example 8, Example 9", 原附录还含 Example 7 Row 2 (D-20 删) — 不影响正确性 | — |

### CONDITIONAL 修正清单
1. `knowledge_base/domains/CP/examples.md:5`: `CPGATE (Gate Name)` → `CPGATE (Gate)`; 重跑 fp_match 确认 ig34_p0208_a009 命中、a010 仍命中.
2. (可选) assumptions.md:100 列表补 "Example 7 Row 2".

## G-TB4 表格 (独立方法: layout 列位 + 渲染)
- 10 张 cp.xpt 全部 3115 格 (含 Row 列) 与 layout 分列比对 (忽略空白): Ex2–Ex9 差异仅为登记 PDF_TYPO 格 = Ex2 r6 CPDTC (T-5); Ex6 r7 CPMRKSTR (T-7) + r7-r32 CPGATDEF 26 格 (T-9) + r29 CPTESTCD (T-8a) + r31 CPSPTSTD (T-8b); Ex8 r11 CPSTRESU (T-10). 共 31 格 = census 31 diffs, 一一对应.
- Ex9 (NO_PDF, 表头 ROW / "CPTST PNL"): layout 解析映射 ROW→Row、CPTST+PNL→CPTSTPNL 后 14 行 × 31 列逐格比对, 差异仅 r1 CPORRES 83 vs PDF 85 (T-11)、r13 CPANMETH 逗号 vs PDF 句点 (T-12); r4 CPANMETH 空格差 (T-13, 空白不敏感比对外单列). 其余全部一致 (含 CPTPTNUM r1 空 / r2-7=1 / r8-14=2, CPBLFL r2/r5=Y).
- 合计 3115 格, compact 差异 94 = 61 (Ex1a/1b layout 窄列串列伪差, 渲染核实 KB 正确) + 33 (全部登记 PDF_TYPO 格).
- Ex1a/Ex1b: layout 在 p210 窄列处把 CPSTRESU/CPSTRESN/CPRESSCL/CPRESTYP 错位一列 (Ex1a r4-16) 与 Ex1b r2-3 CPTEST/CPMRKSTR 串列; 串接顺序与 KB 完全一致. 渲染 p210 逐行人工核: 表头顺序 (…CPORRES CPORRESU CPSTRESC CPSTRESU CPSTRESN CPRESSCL CPRESTYP CPSPEC CPMETHOD CPDTC) 一致; r1-16 各格一致 (r16 CPORRESU/CPSTRESU 空, CPMETHOD CALCULATION; r13 MONOLE; r8 CPMRKSTR 无分母; r12-15 "…CD56-FSC SSC" 无空格与 r2 "CD45+FSC SSC" 同构); Ex1b r1 CPGATE 空/CPGATDEF FSC SSC, r2-3 LEUK/CD45+, r4 (p211) 一致.
- 折行拼接: 无空格拼接 336 处 (全部行尾 "-"), 加空格 890 处 (全部为词边界), 1 处 x-NOSP = Ex9 r4 CPANMETH (T-13). 无异常.

## PDF_TYPO 判定 (取舍规则: 正确值能否由 PDF 自身确定)
| # | 判定 | 依据 (PDF) |
|---|---|---|
| T-1 | 可定 ✓ | 同句 "(i.e.," 开括号未闭合 |
| T-2 | 可定 ✓ | CPCSMRKR 非变量; 同段/本表表头 CPCSMRKS (fp 回退 p0215_a018 = 预期) |
| T-3 | 可定 ✓ | Rows 7-10 平行句 "(e.g., CD83+ in rows 7-8) in addition to…" |
| T-4 | 可定 ✓ | 段落末, 下接新 Rows 条目 |
| T-5 | 可定 ✓ | Ex2 其余 10 行同受试者同样本 CPDTC 均 T12:20 |
| T-6 | 可定 ✓ | 同 CPTESTCD 他行 "Mono Sub" |
| T-7 | 可定 ✓ | 分母 = r6 CPMRKSTR "…CD303+CD1c-"; 渲染 p216 确认 PDF 无 "-" |
| T-8a | 可定 ✓ | 同 CPTEST 行 r7/11/15/21/25 = DCPSDCP |
| T-8b | 可定 (MEDIUM) ✓ | "Count" 与同行单位 MdFI / CPMRKSTR "CD40 MdFI…" 矛盾 (渲染 p217: 系 r30 "…Sub Count" 照抄); "Expr" 依 r9/13/17/23/27 同构. 建议主控知悉 "Expr" 属类比补, 非同行直接可得 |
| T-9 | 可定 ✓ | "CD45LIN-" 缺 +/- 非合法标记写法; 同行 CPMRKSTR 以 CD45+ 起, 父门 r3-6 = CD45+LIN- (渲染 p216/217 确认 PDF r7-32 确为 CD45LIN-) |
| T-10 | 可定 ✓ | 同行 CPORRESU %、CPRESTYP NUMBER FRACTION、CPANMETH "*100" |
| T-11 | 可定 ✓ | 同行 CPSTRESC/CPSTRESN 83, 单位同为 % 无换算; r14 = 83 |
| T-12 | 可定 ✓ | r7 同公式逗号; CPTEST "Target Total, Background" |
| T-13 | 可定 ✓ | r10 同公式无空格 |
| T-14 | 可定 ✓ | 同文件 9 表 "Row"; 变量名 CPTSTPNL |
T4 用户裁定项: 无.

## 删除 D-4..D-20 (del.py: 删除行逐句检查在改后 CP 文件中是否仍存在; 不存在者逐条判)
- D-4/D-5/D-6/D-7/D-8/D-9/D-10/D-11: 旧改写句, 同行 PDF 原句已在 (p211 Rows 1-2/5-6, p212 引言, p218 Rows 1-3, p219-220 Row 1 已逐句 grep 核对); 行内无其他原子丢失 ✓
- Rows 8-11 "separate the numerator from denominator" → "and" (D-2): PDF p209 = "numerator and denominator" ✓
- 引言 / Rows 1-3 / Ex7 / Ex8 词替换恢复 (O-a 7 行): 均与 PDF 一致 ✓ (g6.py 新增句全命中)
- D-12..D-18 占位句 7 条 + D-1: KB 自写, 真表已补 ✓
- D-19 附录: 11 条 [atom] 段在 examples.md 均有 PDF 原文副本 ✓; 附录 a0220_a001 "is not part" 为改写 (PDF "it is not part") 随删 ✓
- D-20 [ig34_p0217_a016] ", as in row 1" + CPGATEDEF: 与 PDF 矛盾, PDF 原文在 examples.md Ex7 Row 2 ✓
- 结论: 无 PDF 内容丢失.

## G-TB6 反向溯源
- examples.md + assumptions.md diff 新增非表行 58; 按句 norm ∈ PDF p205-220: 未命中 6 = T-1、T-3、T-2、T-4 (登记改正) + Ex9 Row 1 跨页句 (p219 末 + p220 首, 拼接后存在) + assumptions.md:100 交叉引用 (结构行).
- 结构行签字: examples.md 各 `**cp.xpt**` 标签、10 张表表头 + 分隔线、Rows 2-7 / Rows 8-14 条目标签; assumptions.md:98 标题保留、:100 交叉引用 (链接 examples.md 存在) ✓
- 无自造说明 / "Note:" 扩写.

## USUBJID 折行裁定
- bbox: p220 USUBJID 表头宽 15.2pt, "0001" 7.7pt, "00001" 9.6pt; p212 表头 22.0pt, "0005" 11.1pt, "00542" 13.8pt. 若原值为无空格 9/10 位数字, Word 字符级断行会把首行填满 (≥7 位), 不可能只放 4 位 → 断点为空格. **维持 `0005 00542` / `0001 00001`** (HIGH-MEDIUM).

## fp_match
- CP 回退 = {ig34_p0215_a018} ✓ (登记预期). 52 atoms 全部在 writer 报告有 action; 未命中的 prose 原子仅 p0211_a009 (T-1)、p0215_a017 (T-3)、p0218_a017 (T-4)、p0212_a009 / p0215_a012 / p0220_a002 / p0220_a003 (atom 文本错, KB 与 PDF layout 一致, 已核)、**p0208_a009 (见问题表, 待修)**.

## R2 recheck
- t2_recheck[] 为空, 无项.

## 范围
- 本批只审 CP 两文件; 工作区 ch04 / LB / MB / TR 改动属其他并行批.
