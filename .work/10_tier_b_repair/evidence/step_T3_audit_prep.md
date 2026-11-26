# T3 回写 — reviewer 抽样底稿 (attempt 2: 翻转率 97.6% > 50%, 规则 A)

> **attempt 4**: 只需复核 `work/t3_attempt4_diff.jsonl` (10 行: K3b 扩展 6 + 规则归属 4) 与扩大断言输出 (`t3_writeback.py` 打印 "K3b extended assertion … hits = 0"); T4 清单 `work/t3_t4_k3b_out_of_scope.txt`.
> (attempt 3 记录:) 只需复核改动层 — `work/t3_attempt3_diff.jsonl` (98 行: C7→ATOM_ERR 38 / K3b 扩展 30 / K3b 改判 15 / K1 改靶 14 / C5 1); K3b 判据见 `work/t3_rules.json` `K3b_why`; 节锚未生效 EXACT 508 条见 `work/t3_t4_risk_anchorless.txt` (T4 人工抽样加层).
> (attempt 2 记录:) 只需复核改动层 — `work/t3_attempt2_diff.jsonl` (147 行, 按 layer: K3 扩展 54 / C7 45 / K1 改靶 38 / K1 降级 7 / K3 ref 1 / K4 2). 全集计数以 `work/t3_audit_sets/*.txt` 为准 (已按 attempt 2 重生成; 下表条数为 attempt 1 值, superseded).

<!-- chain: E (plans) -->
> 生成: `python3 -I .work/10_tier_b_repair/scripts/t3/t3_report.py` (写 `work/t3_audit_sets/`). 本文件只列全集路径与建议层, N 与种子由 reviewer 定.
> 每个 atom 的完整判定证据 (rule / targets / hit_file / triage / writer 行 / checkpoint / review / audit / registry) 在 `work/t3_writeback_decisions.json`; 改动行本身在 `work/coverage_ledger.wc.jsonl` 的 `matched_by.evidence`.

| 层 | 全集文件 (`work/t3_audit_sets/`) | 条数 | 核什么 |
|---|---|--:|---|
| EXACT (当场命中) | `live-hit__EXACT.txt` | 977 | `hit_file` 中 norm(verbatim) 子串 (脚本已断言); 命中位置是否为正确节 (`hit_target_src`) |
| EXACT (原 triage IE, C5) | `live-hit(was-IE-ack)__EXACT.txt` | 23 | 命中位置正确; evidence.ie_ack_original |
| EXACT 短 verbatim (<25 字符) | `EXACT_short_verbatim.txt` | 163 | 子串命中可能偶然, 提高抽样比例 |
| EQUIVALENT — T1 两 agent (kb_loc 行未改) | `T1-two-agent__EQUIVALENT.txt` | 16 | evidence.t1_kb_loc_check.head_line 语义完整 |
| EQUIVALENT — T1 + T2 同表块改写 | `T1-two-agent+T2-rework__EQUIVALENT.txt` | 13 | t1_kb_loc_check.fix_row 覆盖该行; 改写后语义完整 |
| EQUIVALENT — T2 fix + review/audit PASS | `T2-fix+PASS__EQUIVALENT.txt` | 16 | fix_row / checkpoint / review / audit 指针可达且声明已修 |
| EQUIVALENT — C1 人工 | `C1-manual-PDF+KB__EQUIVALENT.txt` | 3 | `work/t3_c1_manual.json` 的 KB 行 = PDF |
| INTENTIONAL_EXCLUDE | `IE-ack__INTENTIONAL_EXCLUDE.txt` | 490 | ∈ t1_ie_final.md (已断言) |
| ATOM_ERR (S1 R1) | `S1-R1__ATOM_ERR.txt` | 159 | 原子 ≠ PDF 且 KB = PDF (t3_errata.json basis + checkpoint 指针; 27 条为页级指针) |
| PDF_TYPO (S1 R2) | `S1-R2__PDF_TYPO.txt` | 31 | registry T-n 与原子差异词一致 |
| PDF_TYPO (writer T-n → registry) | `writer-Tn-registry__PDF_TYPO.txt` | 24 | writer 行的 T-n 是不命中原因 |
| FIGURE_DEFERRED | `FIGURE__FIGURE_DEFERRED.txt` | 11 | 确为图 |
| 残留 | `residual.txt` | 46 | C3 CONDITIONAL 45 + pending 1 |

另需抽查: `work/t3_t2s_atoms.jsonl` 的 ref 展开 (范围 `..` / `-` / `/`) 与页行表 checkpoint 回退 (含 `aNNN-aMMM` 范围).
