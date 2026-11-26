# T3 回写 + 重算 (T3.1 / T3.2) — writer checkpoint

<!-- chain: E (plans) -->
> 状态: writer 已完成 (2026-11-26), 等待主控和 reviewer 独立复核. writer 为 `oh-my-claudecode:executor`, 依据 brief `subagent_prompts/t3_writer_v1.0.md`.
> 写入范围: 只改了 `.work/10_tier_b_repair/{scripts/t3,work,evidence}`.
> 未动: `knowledge_base/` `archive/` `releases/`. KB 在 S3.5 前后的 md5 一致.
> 未 commit. `_progress.json` 的 md5 字段不在 writer 的写入范围内, 未填, 请主控用下表的值填.
> G-TB1 按 brief 只写"数值达标 / 不达标", 用户 ack 放到 T4.

> 最终有效结果摘要见 §0 顶部 (= attempt 4).

## §attempt 4 (2026-11-26) — 现行结果

> 起因: attempt 3 复审 (`evidence/step_T3_audit.md` §attempt 3 复审) **FAIL**: TB 写入层 52/52 成立, 但全量扫描发现 §5.0 内 stock 标签仍有登记偏离被标 EXACT/EQUIVALENT (4 条确认 + 2 条待人工). 本节为现行; 之前各节 superseded.
> 逐条 diff (相对 attempt 3): `work/t3_attempt4_diff.jsonl` (10 行). attempt 3 判定冻结于 `work/t3_attempt3/t3_writeback_decisions.attempt3.json`. 规则数据文件改名为 `work/t3_rules.json` (原 `t3_attempt2_rules.json`; `t3_writeback.py` / `t3_attempt_diff.py` 引用已改).

### A4.1 复跑命令

同 §attempt 3 A3.1, 最后一步改为 `python3 -I $T/scripts/t3/t3_attempt_diff.py --prev $T/work/t3_attempt3/t3_writeback_decisions.attempt3.json --out $T/work/t3_attempt4_diff.jsonl`. 漏因诊断可复跑: `K3B_DEBUG=ig34_p0018_a012,ig34_p0213_a009 python3 -I $T/scripts/t3/t3_writeback.py --ts 2026-11-26T12:00:00Z | grep K3B_DEBUG`.
md5: ledger `a8011432d42e1e9db0e3fd775cf28fad` / section_coverage `f133b0f4…` (含 ts) / 真 KB `b3a04015…` (不变).

### A4.2 漏因与修正

- **漏因 (已查明)**: K3b 扫描本就覆盖全部原子 (不限 TB 行). 漏掉的是 n-gram 语境要求: registry 的 pdf_value 多为 "列名 + 值" 的描述 (如 B-ch03 T-1 `BE Keys BESDTC`、B-SU T-1 `SUENTTP 2006-01-01`、B-CP T-6 `CPTEST MonoSub`), 规则要求原子同时含差异 token 与其 PDF 侧邻词 (`keys besdtc`), 表格单元格/叙述里不会出现这种拼接 → 判不触及. 诊断输出见 `K3B_DEBUG`.
- **修正** (`t3_writeback.py`):
  1. `distinctive(t)`: 差异 token 含数字/非字母字符或 ≥ 6 字母 (变量名类) 时, 规则 (a)(b) 不再要求邻词; 规则 (c) (命中登记行) 仍要求严格 n-gram (防 `mg/kg` 同行误标).
  2. 规则 (a) 追加: PDF 侧 token 须同时不在原子自身 tier1 KB 文件 (排除审计指出的噪声: MB 原子在 MB 文件中本就正确写 `MBREFID`, 不受 B-MS T-3 的 MS supp 偏离影响).
  3. 人工 2 条入 `work/t3_k3b_manual.json` (逐字比依据见下), 作为 K3b 输入.
  4. 范围: K3b 新纳入允许集只限 §5.0 范围内原子; attempt 3 已判定的原子保持; 范围外新命中 + 审计点名的 3 条只写 `work/t3_t4_k3b_out_of_scope.txt` (不改): `ig34_p0026_a037` (B-ch04 T-7, stock PARTIAL, 本轮新发现) / `ig34_p0082_a025` (S-SPREL SE T-1, EXACT) / `ig34_p0342_a006`、`a007` (B-SC T-1, EQUIVALENT).
  5. **扩大断言**: writeback 在写完 ledger 后, 对**最终 ledger 中 §5.0 范围内全部 EXACT/EQUIVALENT 行 (TB 与 stock)** 检查是否被任一登记偏离触及, 命中即 FAIL. 本轮命中 **0**.

### A4.3 人工判定 (主控第 2 项)

| atom | PDF 原页 | KB 行 | 原子 | 判 |
|---|---|---|---|---|
| ig34_p0068_a010 | `ig34_p0068.txt:20-25` row 6: ABC12302002 / 02002 / 2006-02-03 / 2006-04-05 / 2006-01-10 / 2006-04-25 / GONZALEZ, E / 1956-05-05 / RACE …PACIFIC **ISLANDERS** | `DM/examples.md:14` 与 PDF 逐格一致, 唯 RACE 写 …PACIFIC **ISLANDER** (B-DM T-2 登记, CT 值) | ABC1230002 / 0202 / 2006-02-02 / MARIA / 1966-04-05 … (抽错多格, ∉ PDF) | **PDF_TYPO** (KB 偏离 PDF 且有登记; 原子抽错另记) |
| ig34_p0142_a015 | `ig34_p0142.txt:21-22` row 1: AESER N … AESTDTC 2018-04-21 / AEENDTC **2014-04-26** / 5 / 10 | `AE/examples.md:81` 与 PDF 逐格一致, 唯 AEENDTC **2018-04-26** (B-AE T-1 登记) | AESER Y, 2018-04-26 \| 2014-04-28, 15 \| 10 (抽错多格, ∉ PDF) | **PDF_TYPO** (同上) |

### A4.4 现行计数 (attempt 4)

| 项 | 值 |
|---|---|
| 允许集 / 翻转 / 翻转率 | 1939 (attempt 3 的 1933 + 6) / **1894** / 97.7% |
| 按新 verdict | EXACT **1016** / EQUIVALENT **54** / INTENTIONAL_EXCLUDE **494** / ATOM_ERR **197** / PDF_TYPO **122** (S1-R2 33 + writer T-n 34 + K3b 55) / FIGURE_DEFERRED **11** |
| 残留 | **1**: `ig34_p0056_a006` (pending, T4 用户) |
| attempt 3→4 diff | **10** 行: K3b 允许集扩展 6 (stock → PDF_TYPO: `p0018_a012` EQUIV / `p0018_a036` EQUIV / `p0213_a009` EQUIV / `p0132_a014` EXACT / `p0068_a010` EQUIV (人工) / `p0142_a015` EQUIV (人工)) + K3b 规则归属 4 (终态不变 PDF_TYPO: `p0206_a009`、`p0236_a014`、`p0236_a015`、`p0427_a011` 现由 K3b 而非 writer T-n 定) |
| 扩大断言 (§5.0 全部 EXACT/EQUIV × 登记偏离) | 修正后新命中 = 审计所列 6 条, **无其他新增**; 写回后断言命中 **0** |
| **G-TB1** | **数值不达标**: 残留 1 (173/174 节; 未过 §4.5.3.2). 登记类 ATOM_ERR 197 / PDF_TYPO 122 / FIGURE_DEFERRED 11, 用户 ack 待 T4 |
| **G-TB2 [闸, 范围内]** | **170/174**; [参考列, 严格] 155/174 |
| **G-TB3 [闸, mapped]** | **99.3578%** (9593/9655); [参考列 strict] 96.0741% |
| G-TB6 / G-TB7 | KB 未变, 同前 / live docs **42** |
| 直接命中 / 变异 | GREEN (TB 1016 / stock 1762 / pre_existing 58; `p0132_a014` 已从 pre_existing 移出) / M1, M3-M6 RED, M0/M2/M7 GREEN, 真 KB 不变 |
| T4 风险清单 | 节锚未生效 EXACT 508 (`work/t3_t4_risk_anchorless.txt`); K3b 范围外 4 (`work/t3_t4_k3b_out_of_scope.txt`) |

### A4.5 可复现性修复 (审计 attempt 4 复审 CONDITIONAL, A4-5)

- **去掉跨版本回读**: `t3_writeback.py` 不再读 `work/t3_attempt3/…` (原 `A3_DONE`), 也不再硬编码 `T4_ONLY` id. 改读显式数据清单 **`work/t3_k3b_out_of_scope_keep.json`** (24 条: `keep_k3b` 21 = 范围外 K3b 保留, `t4_only` 3 = `p0082_a025` / `p0342_a006` / `p0342_a007`), 每条含 atom_id / registry / 判据 (a/b/c/c′) / PDF 页:行 + token / KB 文件:行 + token. 清单由一次性脚本 `scripts/t3/t3_build_keep.py` 生成 (之后清单即源数据).
- **运行时断言**: 每条清单的 `pdf.token ⊂ norm_pdf(PDF 行)` 且 `kb.token ⊂ norm(KB 行)`; `keep_k3b` 条目必须仍被 K3b 规则触及且最终 ledger 为 PDF_TYPO. 本次: 24/24 成立.
- **(a) 排除计数** (A4-5.2): 规则 (a) "PDF 侧 token 也在原子自身其他 tier1 文件" 挡掉的 (原子, 登记) 对 = **6**, 明细写入 `work/t3_rules.json` → `K3b_a_excluded`.
- **errata 不读 T3 输出**: `t3_errata_build.py` 的 `ledger_verdict_now` 改读 `coverage_ledger.wc.pre_t3.jsonl` (原读现 ledger, 使 errata md5 随回写变化; 不影响判定). t3_errata md5 现 `1d27f0fa6c2538e5900a37b6b3cd9cd9`, 连跑两次一致.
- **源头重跑验证** (先把 `work/t3_attempt1/`、`t3_attempt2/`、`t3_attempt3/` 移到 `work/scratch/t3/hidden_attempts/`, 跑完放回):

```bash
T=.work/10_tier_b_repair; S=$T/work/scratch/t3
mkdir -p $S/hidden_attempts && mv $T/work/t3_attempt1 $T/work/t3_attempt2 $T/work/t3_attempt3 $S/hidden_attempts/
python3 -I $T/scripts/fp_match.py --sections $T/work/section_coverage.wc.baseline.jsonl --out $S/fp_head.jsonl --baseline $T/work/fp_baseline.jsonl --regress-out $S/regress_head.jsonl   # 72
rm -rf $S/kb_t2base && mkdir -p $S/kb_t2base && git archive 302ec4c knowledge_base | tar -x -C $S/kb_t2base
python3 -I $T/scripts/fp_match.py --scope all --sections $T/work/section_coverage.wc.baseline.jsonl --ledger $T/work/coverage_ledger.wc.pre_t3.jsonl --kb-root $S/kb_t2base/knowledge_base --out $S/fp_all_t2base.jsonl
python3 -I $T/scripts/fp_match.py --scope all --sections $T/work/section_coverage.wc.baseline.jsonl --ledger $T/work/coverage_ledger.wc.pre_t3.jsonl --out $S/fp_all_head.jsonl --baseline $S/fp_all_t2base.jsonl --regress-out $S/regress_all.jsonl   # 82
python3 -I $T/scripts/t3/s0_classify.py; python3 -I $T/scripts/t3/t3_t2s_atoms.py; python3 -I $T/scripts/t3/t3_errata_build.py
python3 -I $T/scripts/t3/t3_writeback.py --ts 2026-11-26T12:00:00Z   # ASSERT: OK; keep list 24, failing []; extended assertion hits 0
md5 -q $T/work/coverage_ledger.wc.jsonl                              # a8011432d42e1e9db0e3fd775cf28fad (一致)
python3 -I $T/scripts/t3/t3_direct_hit.py; python3 -I $T/scripts/t3_recompute.py; python3 -I $T/scripts/t3/t3_report.py
python3 -I $T/scripts/t3/t3_global_coverage.py $T/work/coverage_ledger.wc.jsonl; python3 tools/check_links.py 2>&1 | grep "live docs"
bash $T/scripts/t3/t3_mutation.sh > $T/evidence/checkpoints/t3_mutation.log 2>&1
mv $S/hidden_attempts/t3_attempt* $T/work/ && rmdir $S/hidden_attempts
```

结果 (隐藏 attempt 目录下): fp 回归 72 / 82, s0_classify `NEW [] BAD []` R4 = 0; writeback ASSERT OK, ledger md5 **`a8011432d42e1e9db0e3fd775cf28fad` = attempt 4 报告值 (一致)**; direct_hit GREEN; G-TB1 残留 1, G-TB2 170/174 [155], G-TB3 mapped 99.3578%; live docs 42; 变异 M0 绿 / M1 红 / M2 绿 / M3–M6 红 / M7 绿, 真 KB `b3a04015…` 不变.
md5: ledger `a8011432d42e1e9db0e3fd775cf28fad` / t3_errata `1d27f0fa6c2538e5900a37b6b3cd9cd9` / t3_t2s_atoms `33ef2fe0f125ca57cef568d33cfc01ae` / t3_fp_expected `78b22b1cd68a9235f9fffaa8b193df76` / keep 清单 `07ac3786e60842d66ed3383b61a4d03d`.

## §attempt 3 (2026-11-26) — **superseded by §attempt 4** (attempt 3 复审 FAIL, 归档 `evidence/failures/step_T3_attempt_3.md`)

> 起因: attempt 2 复审 (`evidence/step_T3_audit.md` §attempt 2 复审) **FAIL**: K3b — 登记偏离被 live-hit EXACT 遮盖 (`ig34_p0228_a009` / `p0205_a005` / `p0247_a020`). 本节为现行; §attempt 2 及更早各节 superseded.
> 逐条 diff (相对 attempt 2): `work/t3_attempt3_diff.jsonl` (98 行). attempt 2 判定冻结于 `work/t3_attempt2/t3_writeback_decisions.attempt2.json`.

### A3.1 复跑命令 (与 §attempt 2 A2.1 相同, 差别只在最后一步)

```bash
T=.work/10_tier_b_repair; S=$T/work/scratch/t3
python3 -I $T/scripts/t3/s0_classify.py && python3 -I $T/scripts/t3/t3_t2s_atoms.py && python3 -I $T/scripts/t3/t3_errata_build.py
python3 -I $T/scripts/t3/t3_writeback.py --ts 2026-11-26T12:00:00Z    # ASSERT: OK (含新 K3b 断言); ledger md5 63cd2d8666c209db18ef8eca5e840418
python3 -I $T/scripts/t3/t3_direct_hit.py --out $S/direct_hit_head.json   # GREEN
python3 -I $T/scripts/t3_recompute.py && python3 -I $T/scripts/t3/t3_report.py && python3 -I $T/scripts/t3/t3_global_coverage.py $T/work/coverage_ledger.wc.jsonl
python3 tools/check_links.py 2>&1 | grep "live docs"; bash $T/scripts/t3/t3_mutation.sh
python3 -I $T/scripts/t3/t3_attempt_diff.py --prev $T/work/t3_attempt2/t3_writeback_decisions.attempt2.json --out $T/work/t3_attempt3_diff.jsonl
```

md5: ledger `63cd2d8666c209db18ef8eca5e840418` / section_coverage `2ba22353…` (含 ts) / t3_errata `e37d5841…` (未变) / 真 KB `b3a04015…` (不变). fp_match 必钉 `--sections work/section_coverage.wc.baseline.jsonl` (C6).

### A3.2 必改项落实

| 项 | 改动 (`t3_writeback.py`) | 结果 |
|---|---|---|
| **K3b** registry 驱动 | 对 registry 中每条 `KB 写正确值` 偏离: P = pdf_value (去中文说明与 `Row 5`/`Ex3`/`asm 7` 等定位词), K = kb_text_span; difflib 对齐取差异 token (去首尾范围差、去停用词、≥3 字符) 得 pd (PDF 侧) / kd (KB 侧). 原子被"触及"须同时满足: PDF 窗 p..p+1 含登记页; 登记 kb_file ∈ 原子靶; 且 (a) 含 pd 且该 pd 已不在 KB 文件 (原子 = PDF, KB 已改) / (b) 非表行原子含 kd 且 kd 不在原子自身 PDF 窗 (抽取器已改正) / (c) 原子词边界命中恰在登记的 `kb_line_now` 行上且含 kd. (a)(b)(c) 均要求差异 token 带同侧相邻词 (n-gram 语境). 纯标点/空格类登记 (10 条: B-AE T-4, B-CP T-4, B-EX T-1, B-GF T-5, B-MB T-1, B-REL T-9 RELSUB 副本, B-SV T-1, B-TA T-2, B-ch08 T-9 ch08 副本, S-TDM TD T-1) 只按 (c′) 命中登记行判. 触及 → **PDF_TYPO, 优先于 live-hit EXACT 与 IE** (只排在 S1 errata 与 FIGURE 之后). 新断言: 任何终态 EXACT 原子若被触及 → 失败 | 触及原子 55 (其中 45 条由本规则定终态, 余 10 条已由 S1 errata 定). 审计 3 条: `ig34_p0228_a009` (B-GF T-4, c 规则, GF/examples.md:169), `ig34_p0205_a005` (S-SPC1 CP T-16b, c, CP/assumptions.md:58), `ig34_p0247_a020` (B-LB T-1, c, LB/examples.md:67) → PDF_TYPO. 每条判据写在 `matched_by.evidence.k3b` 与 `work/t3_rules.json` 的 `K3b_why`. registry 中 50 条无法机器化 (pdf_value 纯描述), 列于 `K3b_unusable_registry` |
| 指针 | 靶顺序改为 remap > triage kb_loc/target > writer fix 行 > md_atom_ids > 节靶; 同文件多处有效命中时按与 triage kb_loc 行距排序 | `ig34_p0354_a026` → `TU/examples.md:68` (hit_lines [68, 33]); `ig34_p0285_a005` → `NV/assumptions.md:11` (核实: §6.3.6 MO 退役框, S-HOST 置于 NV 顶部). diff 层 "K1 re-target" 14 |
| C5 | 靶补入原子所属域 `domains/XX/spec.md` (域码取节名 `(XX)` 或 triage kb_loc); `t3_direct_hit` 同步 | `ig34_p0296_a005` IE → EXACT (`NV/spec.md:384`). 全量同类仅此 1 条 |
| C7 口径 | delta 复审接受的 T2 fix 原子: norm(原子) ∉ PDF 窗 (p-1..p+1) → **ATOM_ERR** (KB = PDF 依据: census + `t3_delta_rereview.md` 抽样 6/6), 否则 EQUIVALENT | 45 条: ATOM_ERR 40 (C7-K4 2 + C7 原子∉PDF 38) / EQUIVALENT 5 |
| 风险登记 | 节锚未实际生效的 EXACT 写 `work/t3_t4_risk_anchorless.txt` (atom / 原因 / 文件:行) | **508** 条 (无管辖编号标题 442 / 原子节无编号 66). **T4 人工抽样须加这一层** |

### A3.3 现行计数 (attempt 3)

| 项 | 值 |
|---|---|
| 允许集 / 翻转 / 翻转率 | 1933 (= attempt 2 的 1903 + K3b 新入 30) / **1888** / 97.7% |
| 按新 verdict | EXACT **1016** (live-hit 998 + was-IE 18) / EQUIVALENT **54** (T1 两 agent 17 + T1+T2 改写 13 + T2 fix+PASS 16 + C7 5 + C1 3) / INTENTIONAL_EXCLUDE **494** / ATOM_ERR **197** (S1-R1 157 + C7 40) / PDF_TYPO **116** (S1-R2 33 + writer T-n 38 + K3b 45) / FIGURE_DEFERRED **11** |
| 残留 | **1**: `ig34_p0056_a006` (pending, T4 用户裁定) |
| attempt 2→3 diff | **98** 行: C7 原子∉PDF→ATOM_ERR 38 / K3b 允许集扩展 30 / K3b 改判 15 (EXACT→PDF_TYPO 4: `p0205_a005` `p0228_a002` `p0228_a009` `p0247_a020`; IE→PDF_TYPO 1: `p0063_a023`; 其余为终态未变的规则归属) / K1 改靶 14 / C5 新 EXACT 1 (`p0296_a005`) |
| **G-TB1** | **数值不达标**: 残留 1, 173/174 节 (未过 §4.5.3.2). ATOM_ERR 197 / PDF_TYPO 116 / FIGURE_DEFERRED 11 已登记, 用户 ack 待 T4 |
| **G-TB2 [闸, 范围内]** | **170/174** (§4.5.3.2 密度 0.963 + 父节 §4 / §4.5 / §4.5.3); [参考列, 严格] 155/174 |
| **G-TB3 [闸, mapped]** | **99.3582%** (9599/9661) ≥ 99.02%; [参考列 strict] 96.1342% (9599/9985) |
| G-TB6 / G-TB7 | KB 未变, 同 §4.4 (未溯源 0; C 层 1370 需抽样) / live docs **42** |
| 直接命中 / 变异 | GREEN (TB EXACT 1016, stock 1763, pre_existing 59) / M1, M3-M6 RED, M0/M2/M7 GREEN, 真 KB 不变 |

注意 (交 reviewer / T4):
1. `ig34_p0228_a002` 由 (c′) 判 PDF_TYPO (B-GF T-5 只补句号; attempt 2 复审曾判 EXACT ✓). 按主控 "一律 PDF_TYPO" 执行.
2. S-TDM TD T-1 (单句点) 的登记行上有 3 个原子 (`ig34_p0412_a006/a007/a008`) 同被 (c′) 标 PDF_TYPO, 实际只有带句点的那一句受影响 — 纯标点类无法定位到原子, 2 条可能多标.
3. C7 的 38 条 ATOM_ERR 多为表行: "原子 ∉ PDF 窗" 对表行常由文本层折行造成, 此处按主控口径判 ATOM_ERR (KB = PDF 由 census + delta 复审支撑), 并非逐条证明原子抽错.

## §attempt 2 (2026-11-26) — **superseded by §attempt 3** (attempt 2 复审 FAIL, 归档 `evidence/failures/step_T3_attempt_2.md` + `t3_attempt_2/`)

> 起因: attempt 1 被独立审计 (`evidence/step_T3_audit.md`, verifier) 判 **FAIL** (抽样 2 错 + 性质扫描 7 错 + K2 假绿), 归档 `evidence/failures/step_T3_attempt_1.md` + `t3_attempt_1/` (未动).
> 本节为现行数值与口径; 下文 §主控裁定 C1-C6、§0-§6 为 attempt 1 记录 (superseded), 保留作溯源.
> 逐条 diff: `work/t3_attempt2_diff.jsonl` (147 行, 每行 atom / layer / a1{verdict,rule,hit_file} / a2{…, hit_lines}), 审计只需复核改动层.

### A2.1 复跑命令 (仓库根, 顺序不变; 之后任何 fp_match 必须加 `--sections work/section_coverage.wc.baseline.jsonl`)

```bash
T=.work/10_tier_b_repair; S=$T/work/scratch/t3
# (S0 fp 两条命令 + kb_t2base 生成同 §0, 结果不变: in-scope 72 / scope=all 82 回归)
python3 -I $T/scripts/t3/s0_classify.py          # NEW [] BAD []; R1 32 / R2 23 / R3 28; R4 = 0  (p0334_a011 R1→R2, K4)
python3 -I $T/scripts/t3/t3_t2s_atoms.py         # 287 行 / 282 原子; no checkpoint line: 0
python3 -I $T/scripts/t3/t3_errata_build.py      # K4: R1→R2 p0338_a006 (B-RS T-5); 断言无 R1 原子 ∈ PDF; R2 皆有登记; 指针 0 缺
python3 -I $T/scripts/t3/t3_writeback.py --ts 2026-11-26T12:00:00Z   # ASSERT: OK; ledger md5 67931321905eeef1eeef7f212555122f
python3 -I $T/scripts/t3/t3_direct_hit.py --out $S/direct_hit_head.json   # 独立取靶, GREEN
python3 -I $T/scripts/t3_recompute.py            # section_coverage.wc.jsonl (含 ts)
python3 -I $T/scripts/t3/t3_report.py; python3 -I $T/scripts/t3/t3_global_coverage.py $T/work/coverage_ledger.wc.jsonl
python3 -I $T/scripts/t3/t3_reverse_trace.py; python3 tools/check_links.py 2>&1 | grep "live docs"
bash $T/scripts/t3/t3_mutation.sh                # evidence/checkpoints/t3_mutation.log
python3 -I $T/scripts/t3/t3_attempt_diff.py      # work/t3_attempt2_diff.jsonl
```

md5: ledger `67931321905eeef1eeef7f212555122f` / t3_errata `e37d5841…` / t3_t2s_atoms `33ef2fe0…` / t3_fp_expected `78b22b1c…` / section_coverage `c59ab921…` (含 ts) / 真 KB 拼接 `b3a04015…` (不变).

### A2.2 审计必改项与主控裁定的落实

| 项 | 改动 (脚本:函数) | 结果 |
|---|---|---|
| K1 取靶 | `t3_common.valid_hits` (新): 逐行 norm 后拼接检索; **词边界** (verbatim 首/尾为字母数字时邻字符不得为字母数字; 唯一例外: NFKC 把脚注 `¹` 变成 `1` 的 "¹In this column"); **节锚** `anchor_ok`: 命中行的"管辖编号标题" (最近标题若有编号即它; 否则向上找级别更高的编号标题; `v3.4`/`v2.0` 版本号不算编号) 须 = 原子节号或其祖先/子孙, 跨 PDF 文件不比. `t3_writeback.targets`: tier1 = md_atom_ids 文件 / S1 remap (最先) / triage kb_loc·target / writer fix 行 kb_file; tier2 = 节级 md_target_files (后备); `VARIABLE_INDEX/INDEX/ROUTING` 一律剔除 | E1 `ig34_p0153_a0019` → EQUIVALENT (T1 两 agent; TA "to surgery" 词边界拒); E2 `ig34_p0294_a017/a018/a020`, `ig34_p0295_a020` 及同类 `ig34_p0296_a005` → IE (命中只在 NV/assumptions.md §6.3.7.1 通用表, 锚拒); `sv20_p0064_a020` → IE (命中在 model/06 §6.2 下, 原子 §6.1); E3 `ec.xpt` 4 条 → EXACT 改指 `EX/examples.md` 7 处 (:33/86/122/196/263/368/441); 另 34 条 EXACT 改指更准的文件 (ch04/CE/assumptions → 各域 examples 等). 合计 diff 层 "K1 re-target" 38 / "K1 demote" 7 |
| K3 T-n | 规则 6 从 note **和 ref** 取 T-n; 新 `tn_applies`: PDF 侧与 KB 侧 norm 后相同的登记 (引号/破折号字形) 不能解释不命中; 多原子 writer 行须 PDF 侧值出现在该原子. 全量扫: writer 行 note/ref 带已登记 T-n 的原子并入允许集 (+54, 含审计点名的 B-GF/B-IS/B-ch02/S-SPC1 `p0205_a005` 等) | `ig34_p0206_a009` → PDF_TYPO (S-SPC1 CP T-19). 允许集外新入 54: EXACT 27 / PDF_TYPO 23 / EQUIVALENT 4 (B-FA 范围行 `ref new:ig34_p0361_a010..p0363_a009` 的 T-1 为引号字形, 被 `tn_applies` 排除, 只有 `p0363_a008` 因 B-FA T-5 成 PDF_TYPO) |
| K4 R1 | `t3_errata_build` K4 段: R1 须 norm(原子) ∉ norm_pdf(p-1..p+1); 原子在 PDF 且有同批 ±1 页 registry (pdf_value ⊂ 原子) → R2; 无 registry → 移出 atom_err. 断言 "无 R1 原子 ∈ PDF"; writeback 另断言 ATOM_ERR 原子 ∉ PDF 窗 | E4 `ig34_p0334_a011` → PDF_TYPO (B-RS T-8), `ig34_p0338_a006` → PDF_TYPO (B-RS T-5 RS 副本); 全量重扫后只有这 2 条; s0_classify 同步改 p0334_a011 为 R2 |
| K2 复验 | `t3_direct_hit.py` 重写: 不读 hit_file, 由一手来源 (ledger md_atom_ids / remap / triage / writer 日志 / 节靶) 独立取靶 + 同一 `valid_hits`; K11 组计数; 新增"锚失"检查: TB EQUIVALENT `T1-two-agent` 的 T1 kb_loc 行 (302ec4c 文本) 须仍在 KB, triage IE 的 spec.md `### VAR` 块标题须仍在 KB (436 行). 注: 判定与复验共用 `t3_common.valid_hits` 实现 (取靶独立, 匹配器同源) | 现 KB GREEN: TB EXACT 1018 / stock 1767, tb_exact_miss 0 / k11_short 0 / anchor_lost 0 / unexplained 0 / pre_existing 61 |
| kbcopy2 变异 | `t3_mutation.sh` M3-M7 (每项独立新拷贝, 再合并) | M3 删 CE `[ ] Surgery` → **RED** (anchor_lost p0153_a0018/a0019); M4 改名 EX/EC `ec.xpt` (7+1) → **RED** (tb_exact_miss 4); M5 删 NV/spec `### VISITNUM` 块 → **RED** (anchor_lost p0295_a020); M6 合并 → RED; M7 新拷贝 → GREEN; M0-M2 同前 (GREEN/RED/GREEN); 真 KB md5 前后 `b3a04015…` |
| K11 计数 | writeback 后置: 同节同 norm 文本的 n 个 EXACT 原子须 ≥ n 处不同的有效命中 (跨其全部靶文件); 不足者按 id 末位降级重判 | 当前 0 组不足. 审计列的 6 组 (`ec.xpt` 4/`relrec.xpt` 3/`ce.xpt` 3/`da.xpt` 2/`dd.xpt` 2/`aesmie = "y"` 2) 改靶后均 ≥ n. 注: `ig34_p0281_a049`/`p0283_a012` (PP Ex3/Ex4 relrec 表头) 的 hit_file 都是 PP/examples.md:152 (tier1 优先), 但其靶 PC/examples.md 另有 14 处 → 计数够, 指针可由 reviewer 改看 PC |
| C7 | `vp()`: CONDITIONAL 批若 `t3_delta_rereview.md` 有 `## B-XX — PASS` (B-PCPP :18 / B-LB :28 / B-CP :36) → 状态 DELTA_REREVIEW_PASS, 接受 (证据指针 = 该行 + 原 audit PASS); delta 复审点名原子 verbatim 错且 KB=PDF 的 2 条 (`ig34_p0196_a006` → t3_delta_rereview.md:58; `ig34_p0247_a021` → :51,:59) 断言原子 ∉ PDF 后给 ATOM_ERR; K7 的 CONDITIONAL 批 registry PDF_TYPO 加 `c7_delta_rereview` 指针; LB `ig34_p0245_a007` remap → `LB/spec.md`, 现命中 :564 | 45 条: EQUIVALENT 43 + ATOM_ERR 2. K7 PDF_TYPO 9 条 (审计 8 + K3 新入 `p0218_a017`) 带 delta 复审指针 |
| K5/K6/K9/K10 (LOW/MED) | 未改脚本逻辑; K10 的 G-TB6 宽口径限制照旧, 见 §4.4 C 层 | — |

### A2.3 现行计数 (attempt 2)

| 项 | 值 |
|---|---|
| 允许集 / 翻转 / 翻转率 | 1903 (triage ∪ T2S ∪ errata 键 ∪ K3 54) / **1857** / 97.6% (改写 1846 行 + 追加 5 行: 原 4 + `sv20_p0006_a020`) |
| 按新 verdict | EXACT **1018** (live-hit 1001 + was-IE 17) / EQUIVALENT **92** (T1 两 agent 17 + T1+T2 改写 13 + T2 fix+PASS 16 + C7 delta 43 + C1 3) / INTENTIONAL_EXCLUDE **496** / ATOM_ERR **159** (S1-R1 157 + C7 2) / PDF_TYPO **81** (S1-R2 33 + writer T-n 48) / FIGURE_DEFERRED **11** |
| 残留 | **1**: `ig34_p0056_a006` (pending, T4 用户裁定) |
| attempt 1→2 diff | **147** 行: K3 允许集扩展 54 / C7 45 / K1 改靶 38 / K1 降级 7 / K3 ref 1 (`p0206_a009`) / K4 1 (`p0338_a006`) / 规则变更 1 (`p0334_a011` R1→R2, 经 fp 清单) |
| **G-TB1** | **数值不达标**: §5.0 残留 1 (173/174 节过; 未过 §4.5.3.2). ATOM_ERR 159 / PDF_TYPO 81 / FIGURE_DEFERRED 11 已登记, 用户 ack 待 T4 |
| **G-TB2 [闸, 范围内]** | **170/174** (未过 §4.5.3.2 密度 0.963 + 父节 §4 / §4.5 / §4.5.3); [参考列, 严格] 155/174 |
| **G-TB3 [闸, mapped]** | **99.3629%** (9670/9732) ≥ 99.02%; [参考列 strict] 96.8647% (9670/9983); 按 id 99.3623% / 96.8615% |
| **G-TB6** | KB 未变, 同 §4.4: 5336 行未溯源 0; A 层 2136 / B 层 1830 / C 层 (writer 自定义, 需抽样) 1370 |
| **G-TB7** | live docs **42** (≤ 42) |
| 直接命中 / 变异 | GREEN / M1, M3, M4, M5, M6 均 RED, 复原 GREEN, 真 KB 不变 |

T4 清单补充: K3 新入允许集的 54 条中 23 条成 PDF_TYPO (B-EX T-2/3/4, B-ML T-2, B-MH T-3, B-CP T-4, B-GF T-1/3/6, B-IS T-3/5, B-NV T-1, B-TU T-1, B-FA T-5, S-TDM TD T-1/2, B-ch08 T-1..T-6, B-model01 T-1), 需与其余 PDF_TYPO 一起交用户 ack; 清单 `work/t3_rules.json` (`K3_extra`) + diff 文件.

## §主控裁定 C1-C6 (2026-11-26) 与 v2 结果 — **superseded by §attempt 2** (attempt 1 被审计判 FAIL, 见 `evidence/step_T3_audit.md`; 裁定 C1-C6 本身仍有效)

| # | 裁定 | 执行 | 结果 |
|---|---|---|---|
| C1 | 3 条 PRESENT 残留逐条对 PDF + 现 KB 查 | `work/t3_c1_manual.json` 逐条写 KB 文件:行 + why; `t3_writeback.py` 规则 5b 当场断言 (引用行去列表记号/粗体后 ⊂ norm_pdf(p-1..p+1)) | `ig34_p0039_a014` → EQUIVALENT (`ch04_general_assumptions.md:755`, 仅粗体使 norm 不命中) / `ig34_p0057_a001` → EQUIVALENT (`ch04_general_assumptions.md:1485`, 原子漏 PDF 括注, KB = PDF 原句, 文本层起于 p56:50) / `ig34_p0441_a003` → EQUIVALENT (`DI/assumptions.md:5`, S-SPREL U3 把 §9 引言移至 DI 顶部, `t2_S-SPREL.md:83`). 无"真不在 KB"者, **无 REAL_GAP 需开补修批**. `ig34_p0056_a006` 保持残留, T4 用户裁定 |
| C2 | errata 并入允许集 | 允许集 = triage ∪ T2S ∪ t3_errata 逐条键 (atom_err ∪ target_remap) = **1849**; 断言同步 (改动 id ⊆ 新允许集) | errata-only 原子新翻 122: ATOM_ERR 75 (EQUIV 42 / EXACT 30 / IE 2 / PARTIAL 1), PDF_TYPO 22 (EQUIV 15 / EXACT 6 / PARTIAL 1), remap 键当场命中 → EXACT 25 (EQUIV 24 / IE 1) |
| C3 | CONDITIONAL 查复审 PASS | trace.jsonl: B-PCPP :45 / B-LB :56 / B-CP :63 code-reviewer=CONDITIONAL 之后**只有** writer 续 (:46 / — / :66,:75) 与 verifier PASS (:47 / :60 / :73), 无 code-reviewer 复审 delta 记录; review 文件内亦无 CONDITIONAL 后的 PASS 签字 | **不接受**, 45 条保持原 verdict (规则 `residual-review-CONDITIONAL`): B-PCPP 20 / B-CP 17 / B-LB 8, 清单 `work/t3_audit_sets/residual.txt` |
| C4 | 闸口径 | `t3_report.py` 标注 [闸] / [参考列] | 见下表 |
| C5 | 当场命中 → EXACT 优先于 IE | 规则顺序改为 hit 在 IE 前; 原 IE ack 写入 `matched_by.evidence.ie_ack_original` | triage IE 23 条 → EXACT (`live-hit(was-IE-ack)`); 不命中的 490 保持 IE; T2S 中 stock IE 命中 → EXACT 同口径 |
| C6 | fp_match 必钉 sections; sv20_p0050_a011/a012 补行号 | §0 第一行已写; `t3_t2s_atoms.py` 页行表回退加 `aNNN-aMMM` 范围识别 | 两条均补到 `t2_S-MOD1.md:105` (p50 行 "a010-a013 段"), 保留在 T2S 集; T2S 缺 checkpoint 行号 = **0** |

v2 数值 (命令同 §0; ledger md5 `634aedcfeccd820ee182a930ec39352c`, section_coverage `57344cc9…` (含 ts), t3_errata `2897e3cf…`, t3_t2s_atoms `33ef2fe0…`):

| 项 | v2 |
|---|---|
| 允许集 / 翻转 / 翻转率 | 1849 / **1763** / 95.3% (改写 1760 行 + 追加 4 行; 断言 OK) |
| 按新 verdict | EXACT **1000** (live-hit 977 + was-IE 23) / EQUIVALENT **48** (T1 两 agent 16 + T1+T2 改写 13 + T2 fix+PASS 16 + C1 3) / INTENTIONAL_EXCLUDE **490** / ATOM_ERR **159** / PDF_TYPO **55** (S1 R2 31 + writer T-n 24) / FIGURE_DEFERRED **11** |
| 残留 (允许集内) | **46** = C3 CONDITIONAL 45 + `ig34_p0056_a006` (T4 用户) |
| **G-TB1** | **数值不达标**: §5.0 残留 46, 168/174 节过; 未过节 §4.5.3.2 (1) / §6.3.5.1 (4) / §6.3.5.3 CP (17) / §6.3.5.6 LB (4) / §6.3.5.9.1 PC (7) / §6.3.5.9.3 (13). ATOM_ERR 159 / PDF_TYPO 55 / FIGURE_DEFERRED 11 已登记, 用户 ack 待 T4 |
| **G-TB2 [闸, 范围内口径]** | **164/174**; 未过: 上述 6 个内容节 (密度 0.963 / 0.8947 / 0.9412 / 0.9355 / 0.86 / 0.8194) + 结构父节 §4, §4.5, §4.5.3, §6.3.5.9 |
| G-TB2 [参考列, 严格] | 150/174 (另 14 个结构父节仅因范围外子节不过) |
| **G-TB3 [闸, mapped]** | **99.3649%** (9700/9762) ≥ 99.02%, 不降; [参考列 strict] 97.1263% (9700/9987); 按 id 99.3642% / 97.1234% |
| 直接命中复验 | GREEN: TB EXACT 1000 条 0 漏; stock 范围内 1769, pre_existing 63, 其余 0 |
| G-TB6 / G-TB7 / 变异 | KB 未变, 结果同 §4.4 / live docs 42 / t3_mutation.log 重跑 GREEN→RED→GREEN, KB md5 不变 |

结论: C3 拒收后 G-TB1 残留 46 全部来自首批三批 (B-PCPP/B-CP/B-LB) 缺 reviewer 复审 delta 签字 + 1 条 T4. 补救路径 (主控定): 对这三批派 code-reviewer 复审 delta (只核修正项), 拿到 PASS 后重跑 `t3_writeback.py` 即自动转 EQUIVALENT (规则已在, 只缺证据).

## 0. 复跑命令

> **最终有效结果 = attempt 4** (§attempt 4, 含 §A4.5 可复现性修复; 之前各 attempt 均 superseded):
> 1. 计数: 允许集 1939 / 翻转 1894; EXACT 1016 · EQUIVALENT 54 · INTENTIONAL_EXCLUDE 494 · ATOM_ERR 197 · PDF_TYPO 122 · FIGURE_DEFERRED 11; ledger md5 `a8011432d42e1e9db0e3fd775cf28fad` (源头重跑一致).
> 2. 闸: G-TB1 **数值不达标** (残留 1, 173/174 节) · G-TB2 闸(范围内) 170/174 [严格 155] · G-TB3 闸(mapped) 99.3578% [strict 96.0741%] · G-TB6 未溯源 0 (C 层 1370 待抽样) · G-TB7 live docs 42. (G-TB4/5/8/9 属 T2/T0, 不在 T3.)
> 3. 残留: `ig34_p0056_a006` (pending_user, T4 用户裁定).
> 4. T4 待办清单: `work/t3_t4_risk_anchorless.txt` (节锚未生效 EXACT 508, 人工抽样加层) / `work/t3_t4_k3b_out_of_scope.txt` (K3b 范围外仅登记 4) / `work/t3_k3b_out_of_scope_keep.json` (范围外 K3b 保留 21 + t4_only 3) / `work/t3_audit_sets/*.txt` (ATOM_ERR 197 / PDF_TYPO 122 / FIGURE 11 用户 ack) / `work/t3_errata.json` / `work/t2_pdf_typo_registry.jsonl`.
> 5. 复跑: §A4.5 命令序列; 逐条 diff `work/t3_attempt{2,3,4}_diff.jsonl`.

### 0.1 attempt 1 原始命令 (superseded) — (attempt 1; attempt 2 的完整命令序列见 §attempt 2 — 本节以下各节数值均 superseded)

> **C6: 之后任何 fp_match 调用都必须加 `--sections work/section_coverage.wc.baseline.jsonl`** (section_coverage.wc.jsonl 已被 T3 重写, 不钉则回归 72 → 55, 与期望清单失配).


```bash
T=.work/10_tier_b_repair; S=$T/work/scratch/t3; mkdir -p $S         # scratch/ 已被 gitignore
# S0: fp 回归, 范围为 inventory 174 节.
#   必须用 --sections 指定 T0 的 baseline sections: S3 会重写 section_coverage.wc.jsonl (见 §6 注 1)
python3 -I $T/scripts/fp_match.py --sections $T/work/section_coverage.wc.baseline.jsonl \
  --out $S/fp_head.jsonl --baseline $T/work/fp_baseline.jsonl --regress-out $S/regress_head.jsonl   # regressions=72, exit 1
# S3.2: 全原子 (scope=all) 回归. 基线 = T2 之前的 KB, 即 302ec4c
rm -rf $S/kb_t2base && mkdir -p $S/kb_t2base && git archive 302ec4c knowledge_base | tar -x -C $S/kb_t2base
python3 -I $T/scripts/fp_match.py --scope all --sections $T/work/section_coverage.wc.baseline.jsonl \
  --ledger $T/work/coverage_ledger.wc.pre_t3.jsonl --kb-root $S/kb_t2base/knowledge_base --out $S/fp_all_t2base.jsonl
python3 -I $T/scripts/fp_match.py --scope all --sections $T/work/section_coverage.wc.baseline.jsonl \
  --ledger $T/work/coverage_ledger.wc.pre_t3.jsonl --out $S/fp_all_head.jsonl \
  --baseline $S/fp_all_t2base.jsonl --regress-out $S/regress_all.jsonl                               # regressions=82
python3 -I $T/scripts/t3/s0_classify.py      # 生成 work/t3_fp_expected_regressions.jsonl. 期望输出: NEW []  BAD []  R1 33 / R2 22 / R3 28, R4 = 0
python3 -I $T/scripts/t3/t3_t2s_atoms.py     # 生成 work/t3_t2s_atoms.jsonl (287 行, 282 个原子)
python3 -I $T/scripts/t3/t3_errata_build.py  # 生成 work/t3_errata.json
python3 -I $T/scripts/t3/t3_writeback.py --ts 2026-11-26T12:00:00Z   # 首次运行时生成 pre_t3 备份; 期望 ASSERT: OK
python3 -I $T/scripts/t3/t3_direct_hit.py --out $S/direct_hit_head.json  # 期望 RESULT: GREEN
python3 -I $T/scripts/t3_recompute.py --ledger $T/work/coverage_ledger.wc.pre_t3.jsonl --out $S/section_coverage.pre_t3.jsonl  # T3 前对照
python3 -I $T/scripts/t3_recompute.py        # 生成 work/section_coverage.wc.jsonl
python3 -I $T/scripts/t3/t3_global_coverage.py archive/deep_verification/coverage_ledger.jsonl $T/work/coverage_ledger.wc.pre_t3.jsonl $T/work/coverage_ledger.wc.jsonl
python3 -I $T/scripts/t3/t3_report.py        # 输出 G-TB1/2 汇总, 生成 work/t3_audit_sets/
python3 -I $T/scripts/t3/t3_reverse_trace.py # G-TB6, 生成 $S/reverse_trace.json
python3 tools/check_links.py 2>&1 | grep "live docs"
bash $T/scripts/t3/t3_mutation.sh            # 输出见 evidence/checkpoints/t3_mutation.log
```

md5 (用 macOS `md5 -q` 计算):

| 文件 | T3 前 | T3 后 |
|---|---|---|
| `work/coverage_ledger.wc.jsonl` | `620c4a19e5d433b000327b32693c4c9c`, 与 archive ledger 及 `work/coverage_ledger.wc.pre_t3.jsonl` 相同 | `d761c92856dd7d65a1a596792ec8cda5`. `--ts` 固定为 2026-11-26T12:00:00Z, 复跑得到同一值 |
| `work/section_coverage.wc.jsonl` | `36468a8a2e7f997f90a8816cb0e239c6` | `c07c4160d80bc9277180cf7652329abf`. 文件含 `aggregated_by.ts`, 每次复跑 md5 都会变 |
| `work/t3_errata.json` / `t3_t2s_atoms.jsonl` / `t3_fp_expected_regressions.jsonl` | — | `9cef6a6b…` / `ad750a18…` / `68bdd66f…` |
| knowledge_base/ 下全部 .md 拼接 | `b3a040150c53a4256ea0dde645bd7d07` | 不变 (见 t3_mutation.log) |

## 1. S0 现状回归 diff

**期望清单的条数.** brief 写的是 "60 条 (50c3958)". 但 `work/t2_fp_expected_regressions.jsonl` 现在有 **73** 条: 之后 S-SPC1 / S-SPC2 / S-SPREL / S-SPEC1 由主控追加了 13 条. 下面两种口径都给出.

- **对 73 条:** 当前 72 条回归都在清单内, **新回归 = 0**.
  - `ig34_p0278_a051` 在清单里, 但现在不在回归中. 原因是它在 baseline 时就没有命中, 不属于 fp 回归机制. 它的原子文本抄自旧的错误 KB, 定为 R1.
- **对原 60 条:** 新增 12 条, 外加 `a051` (R1).
  - R1 4 条: SE `p0079_a004/a006/a009/a010`
  - R2 6 条: CP `p0199_a020`, `p0200_a006/a007`, `p0206_a001/a003`; IS `p0240_a004`
  - R3 2 条: `p0255_a021` → MS/spec.md; `p0060_a024` → CO/spec.md

**范围外的回归.** S3.2 用 scope=all 重跑, 基线为 302ec4c 的 KB, 回归共 82 条. 减去上面的清单后**差集为 10 条**, 都在 §5.0 范围之外. 这 10 条用同一套证据法定性后, 追加进清单:
- R1 4 条: `p0086_a011`, `p0274_a019`, `p0334_a011`, `p0342_a004`. 其中 `p0274_a019` 的依据是 PDF p274 文本层第 35 行: row 7 没有 Collected.
- R2 5 条: `p0160_a0028` (B-DS T-3), `p0335_a015..a018` (B-RS T-7)
- R3 1 条: `p0340_a002` → SC/assumptions.md:9

**新清单** `work/t3_fp_expected_regressions.jsonl` 共 **83 条: R1 33 / R2 22 / R3 28, R4 (真丢失) = 0.**
- 每条都在现 KB 上实测了三项:
  - `v∈KB`: 原子文本是否在 KB 中. R3 必须为真, R1/R2 必须为假;
  - KB 侧的证据词 ∈ norm(KB 文件);
  - PDF 侧的证据词 ∈ norm_pdf(p, p+1).
- 实测结果写在每条的 `note` 字段. 脚本断言 `BAD []`. 旧的 60 条在 HEAD 上的证据仍然全部成立.
- 判断差集 10 条不必喂 `--downgrade`, 依据是这 10 条逐条定性后都不是 R4. 这是一个**判断**, 不是"差集本来就为空".

**脚本.**
- `scripts/t3/s0_classify.py`: 由 t2 的 classify.py 扩展而来, 改动点见脚本中的 "T3 S0 additions" 和 "T3 S3 additions" 两段.
- `scripts/t3/s0_probe.py`: 逐条 diff 探针, 用环境变量 `FP_BASE=` 指定基线.

## 2. S1 errata 补全 → `work/t3_errata.json`

### 2.1 `atom_err`

共 190 条, 其中 R1→ATOM_ERR 159 条, R2→PDF_TYPO 31 条.

来源:
- t1 的 `t3_atom_err`: 100 条 (R1 80 / R2 20);
- S0 与 S3 回归清单中的 R1/R2: 18 条;
- triage 中 `ATOM_ERR`: 72 条 (另有 2 条已在 t1 中).

判定规则, 按顺序:
1. fp 清单里已有类别的, 用清单类别;
2. note 中出现"照录"的, 判 R1;
3. note 中带 `T-n` 的, 判 R2;
4. 其余判 R1.

登记号与指针:
- 每条 R2 都在 `work/t2_pdf_typo_registry.jsonl` 中有登记号, 脚本断言 "R2 without registry id: []". `p0198_a012` 的登记号是手动绑定的 B-BS T-2 ('part the').
- 每条都带一个 file:line 指针 (断言 "without file:line pointer: 0"). 指针的取法:
  - 先按 note 开头的 "B-XX review|audit|writer" 去找对应的 `t2_B-XX{_review,_audit,}.md`, 取出现该原子 id 的行;
  - triage 来源的取 `work/triage_merged.json` 中的行号;
  - fp 来源的取清单 jsonl 中的行号.
- 有 27 条只能定位到页级行: 该批在 checkpoint 中按范围或页号记录这组原子. 这 27 条**都在允许集之外, 本次没有翻转**.

### 2.2 `target_remap`

共 32 条:
- `_B-FA` 组键展开: 23 条;
- t1 原有的逐条键: 5 条, 即 `p0254_a040/a042`, `p0257_a010/a016`, `p0218_a014`;
- 本次新增: 4 条, 即 `p0240_a004` → IS/examples.md, `p0255_a021`, `p0060_a024`, `p0340_a002`.

其中 4 条同时有两个键 (`p0257_a010/a016`, `p0218_a014`, `p0240_a004`). 它们在 remap 目标里不命中是预期的: 原子本身有错, 或者 PDF 有笔误. 这 4 条的终态由 atom_err 决定.

### 2.3 `pending_user` 4 条的结论

| atom | T2 结果 | 结论 |
|---|---|---|
| ig34_p0010_a023 | B-ch01 T-2 改判为 keep-correct (`B-ch01.writer.jsonl` 中的 SKIPPED_PDF_TYPO 行) | 终态 PDF_TYPO, T4 告知用户 |
| ig34_p0011_a020 | 已实修, target ch02 命中 | 翻为 EXACT |
| ig34_p0012_a005 | 已实修, target ch02 命中 | 翻为 EXACT |
| ig34_p0056_a006 | B-ch04 用 TABLE_REBUILT 补了 'to improve readability', 但不逐字命中 | **残留** (保持 PARTIAL), 标为 T4 待裁 |

## 3. S2 T3.1 回写 (`scripts/t3/t3_writeback.py`)

### 3.1 允许集

允许集共 **1727** 个原子 = triage 1459 个 ∪ T2S 282 个.
- triage 排除了 MANUAL_01/02: 这两条不是 pdf atom, 不写入 ledger.
- T2S 只收 S-* writer.jsonl 中满足两个条件的行:
  - ref 写明了原子 id;
  - action ∈ {INSERTED, REPLACED, TABLE_REBUILT, MOVED}.
- ref 中的范围写法都按 pdf_atoms 的顺序展开: `a010..a018`、`a0014/a0015`、`a014-a018`, 以及跨页范围.
- `:src`、`-adj`、`pdf:`、`census` 这几类 ref 不收. 无法解析的 ref 片段为 0.
- 每行带有 writer 指针 (file:line)、review/audit PASS 指针和 commit.
- 每行还应带 checkpoint 行号, 依次用以下方式查找:
  1. 原子 id;
  2. 范围首项;
  3. ref 原文;
  4. `文件:kb_line_after`;
  5. 页行表中的 `| 页 | … aNNN`.

  仍然缺行号的有 **2 行**: `sv20_p0050_a011/a012` (S-MOD1.writer.jsonl:71-72, 这两行 writer 的 note 为空). 这 2 条是 T2S-only 原子, 原 verdict 为 stock IE, 当场命中, 已翻为 EXACT.

### 3.2 判定规则 (按优先级, 完整说明见脚本 docstring)

1. S1 errata;
2. FIGURE;
3. IE: 断言 id ∈ `t1_ie_final.md` 中的 513 个;
4. pending 残留;
5. **EXACT: 只给当场命中的**;
6. writer 行给出的 T-n 在 registry 中有登记 → PDF_TYPO;
7. 两个 agent 一致 → EQUIVALENT. 这条要求 T1 判定时看的 kb_loc 行 (302ec4c 版本) 在 HEAD 中仍然原样存在; 如果该行已被改写, 则要求同一 HEAD 表块内有一个 PASS 批的 fix 行;
8. T2 有 fix 行, 且 review 和 audit 都是 PASS → EQUIVALENT;
9. 其余为残留.

### 3.3 结果

- 翻转 **1683** 个原子, 改写 1680 行. 重复 id `sv20_p0004_a003` 的两行一起改.
- **追加 4 行**: `ig34_p0017_a029`, `p0042_a007`, `p0048_a012`, `p0396_a004`. 这 4 个是范围内的 triage 原子, 原 ledger 中没有对应的行.
- 断言 OK:
  - 改动的 id 和追加的 id 都 ⊆ 允许集;
  - 没改的行与备份逐字节相同;
  - 每条改动行 `matched_by.phase == "TB"`;
  - IE 翻转 ⊆ t1_ie_final;
  - 每条 EXACT 的 `hit_file` 当场复验命中.

| 新 verdict | 数 | 规则 |
|---|--:|---|
| EXACT | 952 | live-hit (triage 739 + T2S 213) |
| EQUIVALENT | 90 | 见下 |
| INTENTIONAL_EXCLUDE | 513 | IE-ack. `category` = ie_cat; `approved_by` = t1_user_ack R4 / t1_ie_final |
| ATOM_ERR | 84 | S1 R1 |
| PDF_TYPO | 33 | S1 R2 9 + writer T-n→registry 24 |
| FIGURE_DEFERRED | 11 | triage FIGURE |

EQUIVALENT 90 条的构成:
- T1 两 agent 一致, 且 kb_loc 行未改: 16 条;
- T1 一致, 但该行已被 T2 改写, 同表块内有 PASS 批的 fix 行: 13 条, 即 B-CE CRF ×11、B-DM ×1、S-CH4 ×1;
- T2 fix + review PASS + audit PASS: 16 条;
- **T2 fix + review CONDITIONAL + audit PASS: 45 条**, 即 B-PCPP 20 / B-CP 17 / B-LB 8, 见 §5-3.

- 翻转率 = 1683/1727 = **97.5%**, 超过 50%, 因此附了 `evidence/step_T3_audit_prep.md`.
- 允许集内的**残留共 4 条**, verdict 保持原值:
  - `ig34_p0039_a014` / `p0057_a001` / `p0441_a003`: triage 为 PRESENT, 未经 reviewer 复核, 不命中, 也没有 fix 行;
  - `ig34_p0056_a006`: pending.
- **errata 中有 97 条在允许集之外, 未翻转.** 其中 ATOM_ERR 75 条, PDF_TYPO 22 条. 它们当前的 ledger verdict: EQUIVALENT 57 / EXACT 36 / IE 2 / PARTIAL 2.
  - 这些原子由 T2 B 批或 census 修过, 但不在 triage 中, 例如 MB 表行、CP T-15、CE USUBJID.
  - brief 的 ⊆ 断言禁止翻转它们. 它们不算 G-TB1 残留, 但 stock 标签不准.
  - **需主控决定**是否并入允许集. 清单见 `work/t3_errata.json`, 按 `in_allowed_set=false` 筛选.

## 4. S3 T3.2 重算与复验

### 4.1 stock 口径如何处理新 verdict

- stock `section_stats` 只把 EXACT 和 EQUIVALENT 计为 matched, 分母是全部非 HEADING 原子.
- 因此 ATOM_ERR / PDF_TYPO / FIGURE_DEFERRED (以及 IE) 都会被当作未覆盖, stock 的 `coverage_density` 和 `aggregate_verdict` 会偏低.
- T0.2 时加的 `tb_*` 列已经把这四类从分母中去掉.
- stock 逻辑没有改动. G-TB3 另写了脚本 `t3_global_coverage.py`, 两个口径都报.

### 4.2 直接命中复验 (`scripts/t3/t3_direct_hit.py`)

复验对象:
- TB 行中的全部 EXACT: 952 条, 不论是否在 §5.0 范围内, HEADING 也算在内. 目标文件取 `matched_by.evidence.hit_file`.
- §5.0 范围内的 stock EXACT: 1793 条. 目标文件取 fp targets ∪ remap.

结果为 **GREEN**: tb_exact_miss 0, unexplained 0.
- 不命中但有解释的: expected_regression 16 条, errata 6 条.
- **pre_existing 63 条**: 在 302ec4c 的 KB 上同样不命中, 说明 P4a 给的 EXACT 从来没有指纹支撑. 这与 PLAN Q9 的对照层有关, 清单在 `$S/direct_hit_head.json`.

fp 回归差集的处理见 §1: 差集 10 条, 逐条定性后都不是 R4, 所以**没有使用 `--downgrade`**.

### 4.3 重算结果

| 指标 | T3 前 (pre_t3 重算) | T3 后 |
|---|---|---|
| §5.0 范围 174 节的残留原子 | 1459 | **4** |
| G-TB1 通过的节 | 59/174 | 170/174 |
| G-TB2 通过的节 (stock `tb_g2_pass`, 严格口径) | 35/174 | **152/174** |
| G-TB2 (结构父节只看范围内子节) | — | **167/174** |
| stock aggregate_verdict (399 节) | FULL 137 / MOSTLY 51 / CT 93 / SD 49 / SKEL 46 / DRIFT 23 | FULL 197 / MOSTLY 53 / CT 60 / SD 36 / SKEL 36 / DRIFT 17 |
| 当前 Tier B (SD+CT) 节 | 142 (残留 1389) | 96 (残留 76; stock 口径, 含范围外节, 分母含 IE) |

**G-TB1: 数值不达标.**
- 残留 4 条 ≠ 0, 分布在 4 节: §4.4.1 (`p0039_a014`)、§4.5.3.2 (`p0056_a006`)、§4.5.4 (`p0057_a001`)、§9 (`p0441_a003`).
- 如果主控不接受 §5-3 中的 45 条, 残留为 **49**; 如果只承认 B-PCPP 的用户 ack, 残留为 29.
- ATOM_ERR 84 / PDF_TYPO 33 / FIGURE_DEFERRED 11 已登记, 用户 ack 待 T4.

**G-TB2: 严格口径 152/174.**
- 内容节中未通过 4 节, 就是上面 4 个残留节, 密度依次为 0.9643 / 0.963 / 0.8571 / 0.75.
- 另外 15 个结构父节没通过, 原因只是它们在 §5.0 范围外的 21 个子节有 stock PARTIAL, 例如 §4.1.6、§6.2.4 DS、sv20 §3.1.3. 这些子节不在分诊范围内, 本项目没有碰过.
- 结构父节只看范围内子节时为 167/174. 未通过的 7 节 = 4 个残留节 + 它们的父节 §4、§4.5、§4.5.3.

**G-TB3 (06 口径 = (EXACT+EQUIV+PARTIAL+MISPLACED) / (行数 − IE), 按行计).**
- 先在 archive ledger 和 pre_t3 上复现了原值: 10298/10400 = **99.0192%**, 即 99.02%.
- T3 后有两个口径:
  - **mapped** (新三类与 IE 一样从分母中去掉): 9771/9833 = **99.3695%**. ≥ 99.02%, 没有下降;
  - **strict** (新三类计为未覆盖): 9771/9961 = **98.0926%**, 下降.
- 下降的原因:
  - 06 口径把 PARTIAL 计为已覆盖. 这些 PARTIAL 翻成 IE (509 条)、ATOM_ERR、PDF_TYPO 之后, 分子变小;
  - 追加的 4 行让分母 +4.
- MISSING+ERROR 从 102 降到 62.
- 按 id 计 (去掉重复行) 为 99.3688% / 98.0906%.

**G-TB7.** `python3 tools/check_links.py 2>&1 | grep "live docs"` 的输出为 `broken relative links: 18668 (live docs: 42)`, 满足 ≤ 42.

### 4.4 G-TB6 反向溯源 (`scripts/t3/t3_reverse_trace.py`)

**基线与范围.**
- 基线 = **302ec4c**. 它是 T2 首批提交 97e1895 (B-PCPP) 的父提交, 即 T1.4 rulings 提交.
- 302ec4c 的 KB 与 7819398 相同: `git diff --stat 7819398 302ec4c -- knowledge_base` 输出为空.
- 范围: `git diff -U0 302ec4c..HEAD -- knowledge_base/` 中新增的 **5336** 行.

**结果分三层报.**

| 层 | 行 | 组成 |
|---|--:|---|
| A. 在 PDF 中找到 (严格子串) | **2136** | PDF_SUBSTR 1877 / PDF_LOOSE 25 (连字符两侧的空格差异) / PDF_SENTENCES 14 / PDF_SEGMENTS 4 / HEADING_PDF 216 |
| B. brief 列出的类 | **1830** | BLANK 815 / STRUCT 111 (分隔行、空表行、xpt 标签、列表桩) / PDF_TYPO 205 (行中含 registry 的 kb_text_span/kb_value, 去掉后其余内容在 PDF 中或在同一页对上) / U_RULE 699 (S-CT U5/U6: 去掉 C-code 后在 PDF 中; 或者是 CT `*`, 即 U2) |
| C. **writer 自行增加的类** (reviewer 应抽样) | **1370** | TABLE_TOKENS 680 / MERMAID 322 / KB_NOTE 248 / SPEC_FIELD 61 / XREF_D2 23 / HEADING_NOT_IN_PDF 21 / KB_NOTE_SCOPE 15 |
| 未溯源 | **0** | PDF_NEAR 0 / UNEXPLAINED 0 |

C 层各类的含义:
- **TABLE_TOKENS**: 表格行的字母数字词元全部出现在同一个 PDF 页对上. 这是**宽口径**, 不证明逐格的值正确; 值的正确性由 G-TB4 census 负责.
- **MERMAID**: ```mermaid 块内的行, 这些是按 PDF 图重画的.
- **KB_NOTE**: D6 / D7 / U8 标注块.
- **SPEC_FIELD**: spec.md 中 `- **Field:** value` 形式的行, 其 value 在 PDF 中.
- **XREF_D2**: D2 去重后留下的指针.
- **HEADING_NOT_IN_PDF**: 标题文本不在 PDF 中. 典型如 `### 5.1.1.1 Trial Elements (TE)`、`## RELREC Method Quick Reference (PP-side view)`、ch02 的 `### Must NEVER be used …`. 共 21 条, 需要 reviewer 逐条判断它们是结构标题还是 KB 自拟.
- **KB_NOTE_SCOPE**: 位于某条 D6 标注所声明的范围内. 15 行如下, 箭头后为对应的标注行:
  - `chapters/ch04_general_assumptions.md:1015` → :1003 (Mermaid caption)
  - `domains/PP/examples.md:116`, `:163` → :114 (整节 KB 自写)
  - `model/02_observation_classes.md:166`, `:235` → :164 (Key Notes 列由 KB 编写)
  - `model/02_observation_classes.md:336/365/374/375/378/379/380/381/388` → :316 (timing 子表的 Notes 列由 KB 编写)
  - `model/06_relationship_datasets.md:194` → :188 (汇总表由 KB 编写)

A 层中 PDF_SEGMENTS 的 4 行是被分页或脚注隔开的 2-3 段, 每段都在 PDF 中: `domains/BE/examples.md:62`、`domains/MS/examples.md:11`、`model/01_concepts_and_terms.md:191`、`model/02_observation_classes.md:31`.

**说明.**
- 最后 19 行是在本 session 内新加了 D6 范围规则和 PDF_SEGMENTS 规则之后才清零的. 规则写在脚本 docstring 中, 可以复跑.
- 逐行明细在 `work/scratch/t3/reverse_trace.json`. 该文件位于 gitignore 的 scratch 下, 含 KB 文本, 需要时按上面的命令复跑生成.

### 4.5 变异测试 (规则 5)

脚本 `scripts/t3/t3_mutation.sh`, 日志 `evidence/checkpoints/t3_mutation.log`.

做法: 在 `work/scratch/t3/kbcopy` 中删掉 B-AE INSERTED 的原句 `ig34_p0133_a021`. 选这句的原因: 它是 TB EXACT, 而且在 302ec4c 时不存在.

结果:
- 原样拷贝: GREEN;
- 删句后: **RED**, tb_exact_miss = [ig34_p0133_a021], rc=1;
- 在同一份拷贝上跑 fp_match 回归: 72 条, 被删的原子**不在其中**. 这印证了 brief 所说的"回归机制对 T2 新补的原子是盲的";
- 复原后: GREEN;
- 真 KB 的 md5 前后都是 `b3a04015…`.

## 5. 阻塞项 / 需主控裁定

1. **G-TB1 残留 4 条**: 3 条 PRESENT 在 T1 时未经复核, 现在也不命中; 1 条 pending. 需要 T4 或主控补裁, 或者补一次 reviewer 复核.
2. **errata 中有 97 条在允许集之外, 未翻转** (见 §3.3). 并入允许集需要主控授权.
3. **45 条 EQUIVALENT 只有 CONDITIONAL review 作依据** (B-PCPP 20 / B-CP 17 / B-LB 8).
   - 这三批的 review 文件里没有最终 PASS 签字, 只有 "verdict: CONDITIONAL … 其余全部通过".
   - 其他依据: 修正后的 audit PASS, 以及 commit 标记 `(PASS; local)`.
   - B-PCPP 还有用户 ack (`t2_B-PCPP_user_ack.md`), 依据更强.
   - 如果不接受, 残留会升到 49; 只接受 B-PCPP 时为 29.
4. **G-TB2 结构父节用哪个口径**: 严格口径 152, 只看范围内子节 167.
5. **G-TB3 用哪个口径**: strict 为 98.09%, 下降; mapped 为 99.37%, 达标. 需要确认采用 mapped, 即"06 口径中新三类视同 IE 排除".
6. **G-TB6 C 层 1370 行**是 writer 自行定义的类, 不是 brief 列出的类. 需要 reviewer 抽样, 尤其是 TABLE_TOKENS 和 21 条 HEADING_NOT_IN_PDF.
7. 给 T4 的提示:
   - triage 的 IE 中有 **23 条** verbatim 现在命中 KB, 本次仍保持 IE. 按 R4 规则 ("原文逐字在 KB → PRESENT"), 它们可以改为 EXACT; 清单见 `work/t3_audit_sets/IE_now_hits_KB.txt`.
   - 与此相对, T2S 中有 69 条原本是 stock IE 的原子, 因当场命中被翻成了 EXACT. 两种处理不一致, 请主控统一.
   - R4-blocked 的 5 条保持 IE.

## 6. 注

1. **fp_match 的默认 `--sections` 已经变了.** 重写 `work/section_coverage.wc.jsonl` 之后, md_target_files 变宽了. 如果不用 `--sections …baseline.jsonl` 指定 baseline, 全局回归数会从 72 变为 55, 与 83 条期望清单对不上. 以后 reviewer 跑 fp 闸时必须指定 baseline sections, 否则就要重新定期望清单.
2. CONDITIONAL 的判据见 `t3_writeback.py` 中 `vp()` 的 docstring. trace.jsonl 里这三批的 code-reviewer 结论是 CONDITIONAL, verifier 结论是 PASS.
3. `t3_recompute.py` 输出的 `tb_verdict_counts` 会带出值为 0 的键, 这是 defaultdict 被访问后留下的. 只影响外观, stock 脚本没有改.
