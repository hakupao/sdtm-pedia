# T4 attempt 2 主控汇报 (交协调方)
<!-- chain: E (plans) -->
> 状态: **总闸 T4.1 attempt 2 = 不通过 (CONDITIONAL)**; 解冻轮已完成并本地提交; T4.2 人工闸按主人改定口径登记, 闸是否足够待主人确认 (2026-11-27). 未 push, 未打 kb tag, 未做 T4.3.

## 1. 裁定落实
- 记录: `t4_user_decisions.md` §000 (委托代裁: 裁定人 = 协调 bot「sdtm开发」, 委托原话「之前那些选项，你可以替我分析后决定嘛。我听从你的建议」, 2026-11-27; §00 "用户选" 列保持空白) + §000b (主控实施决定 M-1..M-7, 不在委托内).
- 台账行: U-2 `ig34_p0056_a006` → ATOM_ERR; U-8 `p0026_a037` / `p0082_a025` / `p0342_a006` / `p0342_a007` → PDF_TYPO. HEAD→终态 ledger 58 行标签/规则变化 + 20 行仅指针, 全部归因 (U-2 1 / U-8 4 / U-7 R2 19+p0362 / A5-10 R3 live-hit 15 / IE→live-hit 1 / K3b 2 / writer-Tn 1 / CRF 规则名 14). 见 `t4_thaw_W3.md`, `t4_thaw_review_ledger.md`.
- KB (`a59c2d3`): **25 文件, +118/−179**; 72 hunk. U-7 21 行 (28 处, 含副本) + A6 en dash 4 处 + CRF 符号 58 处 (CE 39 + ch04 19) = W1 90 处 / 16 文件; W2 A5-1..11/13/14 + U-10② 13 文件 (+57/−118), A5-14 改 `> Note:` 5 条 (KB note 170→165). registry 270→272 行 (23 行改 + U-10①④ 新登 + W3 事实修正 6 行).
- 不动 KB 的: U-1/U-3/U-4 口径; U-5 整类确认; U-9(b)(c) 照录 / 接受现状; U-10① 补登记、⑤⑥⑦ 记后续 / 不处理; Q3 MK en dash 不改.

## 2. 只读核查结论
- U-5 C7 38 条 (tracer): **38 成立 / 0 不成立 / 0 看不出** → 不改变标签, U-1 无需按新标签重算. `t4_u5_c7_fullcheck.md`.
- U-7 复核 (pr-review-toolkit:code-reviewer): A1-A3 草拟 B 26 行 → **维持 B 21 / 改回 A 5** (A2-12, A3-24, A3-28, A3-31, A3-32); B 组 15 → **维持 15 / 否决 0**; A2-16 候选值更正为 "PC records with PCGRPID". `t4_u7_rowcheck.md`.
- U-6 预筛 (general-purpose, 非人工): 解冻前 **42/42 内容正确**; 解冻后 #6-9 复筛 4/4. `t4_human_prescreen.md`, `t4_human_prescreen_postthaw.md`.
- Mermaid (U-11): 解冻前后 42/42 渲染 OK (`scripts/t4/t4_mermaid_render.sh`).

## 3. T4.2
- 主人 (经协调方转达, 本人选择) 改口径 "AI 预筛 42 + 主人抽查 6", 判 6/6 内容正确; 6 条解冻后 KB 摘录未变 → 判定仍适用. 登记 `t4_human_verdicts.md` (与 AI 预筛分开; `t4_human_sample.md` 判定栏空白, 只加指针). 仓内无主人原话独立凭证.

## 4. 重算后各闸
| 项 | 值 |
|---|---|
| ledger md5 | `60729f7b64b7c1dfaf2174e394f6dd9c` (W3 两遍 + reviewer-L 复跑一致) |
| G-TB1 残留 | 0 (174/174 节) |
| G-TB2 | 范围内 174/174; 字面严格 157/174 |
| G-TB3 U-1 B 口径 | **99.2690%** (9913/9986) ≥ 99.02% |
| strict / mapped / 内容 | 95.8041% / 99.3561% / 90.6948% |
| check_links live docs | 42 |
| t3_mutation | M0/M2/M7 GREEN, M1/M3-M6 RED, 真 KB md5 不变 |
| t0_mutation | MISMATCH (既有, T0 baseline 过期; HEAD 副本同格局) |
| census | DIFF 37→38, diffs 144→148 (DS SCRN / PP h, 均登记 KB 写正确值); 删 3 表 = A5-8/A5-10 |
| rag 映射 R4 | 72→75, 只新增 TSVALCD/TSVCDREF/TSVCDVER, 删 0 改 0 (`scripts/t4/t4_defhome_setdiff.py`) |

## 5. 总闸 attempt 2
- **CONDITIONAL (不通过)**: G-TB 无 NOT_MET (6 条带条件), 样本层变化 4+1 条重判全 HOLDS. 不 PASS 的原因: 人工判定来源可核性不足; U-1 口径与 T4.2 口径需主人本人确认; M-1..M-7 不在委托内; 仍开缺口 (C3 逐表结案清单、t0 baseline 刷新、pre_existing 58 / FIG 11 / 规则 0 抽中类、PLAN FIG 12→11 与 T4.2 口径修订、audit_matrix 行). 全文 `t4_gate_review.md` §attempt 2; 指针 `evidence/failures/step_T4.1_attempt_2.md`.

## 6. 提交与仓状态
- 本 session 本地提交: `3a24a1c` (只读核查) → `a59c2d3` (解冻轮, 唯一改 KB 的提交) → `d3f2ea9` (下游说明) → `c352529` (attempt 2) → 本汇报提交.
- KB 指纹: `git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`; `a59c2d3` 之后 KB 无改动, 工作树无未提交 KB 改动.
- 未 push (`main...origin/main [ahead N]`); 无新 `kb-*` tag (最新仍 `kb-2026.11.25`); `git diff dc6bb34..HEAD -- archive releases` 为空; sdtm-rag 仓 `git status --short` 为空 (只读运行过其 probe 脚本); `work/t4/human_sample.jsonl` md5 `5b4212ee…` 未变.
- 下游: `t4_downstream_notes.md` 末节; heading diff `work/t4/kb_heading_diff_00a2e93_HEAD.txt` (8 文件, 删 28 / 增 22) 与 `kb_heading_diff_kb-2026.11.25_HEAD.txt` (79 / 104 / 239).

## 7. 已知未修 (如实)
trace 本 session 追加行时间戳为事后取整; ack 清单 p0362_a010 记在 U-7 名下 (实为 M-4); registry B-IS T-6 页号 p241 应为 p239; TT/TP DOMAIN 格挂在 Usage Restrictions 列; O63-O67; MK en dash.
