# T4 解冻轮 台账侧独立复核 (reviewer-L)
<!-- chain: E (plans) -->
> 状态: **PASS** (2026-11-27). 审查者 `oh-my-claudecode:code-reviewer` (opus, 新实例, 与 KB 侧 reviewer 不同实例; 与 W3 writer 不同角色), 只读 (仓库产物先 tar 备份 + 4810 文件 md5 清单, 复跑后还原, 清单一致). 主控誊录要点, 未改判. 复核产物 `work/scratch/t4/reviewL/` (gitignored).

## 结论: PASS — 6 项必做全部复跑/核对, W3 终值独立复现; 无阻塞, LOW 4 + 说明 1.

| # | 严重度 | 位置 | 问题 | 建议 |
|--:|---|---|---|---|
| 1 | LOW | ledger `ig34_p0153_a0006`…`a0025` 14 行 `matched_by.evidence.t1_kb_loc_check` | 出处记为 reworked-by-T2 / c11084b / B-CE fix row, 实为 T4 U-9a CRF 改动; 标签本身对 (p153 渲染 vs CE/examples.md:72-83 ○/□ 一致); 补核 `t4_ce_p153_check.py` 14/14 仅块级 token | 后续加 T4 来源字段; 本轮不阻塞 |
| 2 | LOW | `scripts/t3/s0_classify.py:76-95` | 新 R2 条目 12 条当前不回归, s0 清单被当作逐原子改标入口, 本义变宽; 段头注释 "(R2, 16)" 实为 19 | 段头写明用途, 改计数 |
| 3 | LOW | `scripts/t3/t3_mutation.sh` armcd 替换 | 模式在 DM/spec 命中 2 处 (ARMCD :219 与 ACTARMCD 同句), 非单点; RED 只来自 :219 | 模式锚定到 :219 行 |
| 4 | LOW (T3 既有) | `work/t3_k3b_out_of_scope_keep.json` `ig34_p0342_a007` | kb 证据指 Row 2 (SC/examples.md:35), 应为 Row 3 (:36); pdf token "scdtc" 是表头词; 标签成立 | 修正行号/token |
| 5 | 说明 | `t3_errata.json` `ig34_p0362_a010` | 原子 "thought to be related", PDF p362 "thought be related"; K4 口径应留 ATOM_ERR, K3b (b) 口径为 PDF_TYPO; 现 PDF_TYPO 与 K3b (b)、主控决定 2 一致 | basis 注明依据 K3b (b) |

## 核查摘要
1. 复跑 §A4.5 (W3 `run_chain.sh`): ledger md5 **`60729f7b64b7c1dfaf2174e394f6dd9c`**; errata `f355a637…` / fp_expected `e7df6ce0…` / rules `fff771cf…` / decisions `5fd0a673…` / keep `9053d986…` / t2s `33ef2fe0…`. s0: regress 109, NEW [], BAD [], R1 32 / R2 42 / R3 47, R4 0. writeback ASSERT OK, 允许集 1978, keep 25/25, 范围外 0, 残留 0. direct_hit GREEN (unexplained / anchor_lost / tb_exact_miss 0). G-TB1 174/174 残留 0; G-TB2 严格 157/174. global strict 9567/9986, mapped 9567/9629.
2. HEAD→现 ledger: 12492 行, 12414 同, **58 行标签/规则变化 + 20 行仅指针** (= W3). 58 = S1-R2 20 (19 T4 + p0362) / K3b 6 (U-8 4 + p0041 + p0363_a009) / writer-Tn 1 / live-hit 15 / IE→live-hit 1 / S1-R1 1 (U-2) / CE 规则名 14. **R2 = 19 (16+3), R3 = 19 (5+9+5)**, 断言 `len(set)==len==121`, 无重复计数. 抽 20 条全部成立 (U-2 1、U-8 4 全、U-7 R2 8、writer-Tn 1、A5-10 R3 2、p0362、CRF 3); 渲染页 p82/153/280/281/285/298/362/419, 其余文本层.
3. registry 6 行: 仅动 W3 列出字段; N-1 p285 "may included"、N-2 p298 "links the each"、T-2 "Dose"、T-3 DOSFREQ ×3、T-4 "OUTMSPR" (p419 渲染)、T-6 p425:30 "MAXAGE" 属实.
4. 脚本: `t3_writeback.py` / `t3_direct_hit.py` / `fp_match.py` 未改, **K3b 规则未改**; errata / s0 只加逐原子数据表 + p0362 指定 registry. `> Note:` 豁免键 = (file, 整行), 5 条精确匹配, 每条恰好命中 1 次; WORKTREE 反向溯源 5414 行 UNEXPLAINED 0 / NOTE_EXEMPT 5; HEAD 模式新旧脚本 JSON 逐项相等 (5336 行). heading_diff HEAD / 00a2e93 WORKTREE 输出与已存文件逐字节相同.
5. 覆盖独立复算: EXACT 4718 / EQUIV 4015 / PARTIAL 637 / MISPLACED 197 / ATOM_ERR 197 / PDF_TYPO 149 / FIG 11 / IE 2506 / ERROR 62 = 12492. strict 9567/9986 = **95.8041%**; mapped 9567/9629 = **99.3561%**; U-1 B 9913/9986 = **99.2690%**; 内容 EXACT+EQUIV 8733/9629 = **90.6948%**.
6. t3_mutation: M0 绿 / M1 红 / M2 绿 / M3 红 (anchor_lost p0064_a001) / M4-M6 红 / M7 绿; 真 KB md5 前后 `b71a466d6e618f995c493a82de3e3eb7`. live docs 42. t0_mutation 未复跑 (既有 MISMATCH, 非本次必做).
