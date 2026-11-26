# T3 writer brief v1.0 (T3.1 ledger 回写 + T3.2 重算)

角色: writer (oh-my-claudecode:executor, opus). 工作目录 `/Volumes/DevSSD/Project/sdtm-pedia`. 用中文写证据文档.
**不得改 `knowledge_base/`、`archive/`、`releases/`** (只读). 只写 `.work/10_tier_b_repair/{scripts,work,evidence}` 下文件. 不 commit (主控提交).

## 必读
- `.work/10_tier_b_repair/PLAN.md` §4 T3.1/T3.2、§5.0-§5.2 (终态类、G-TB1/2/3/6/7)
- `.work/10_tier_b_repair/HANDOFF.md`
- `evidence/t2_fp_expected_regressions.md` 全文 (fp_match 口径、R1-R4、errata 缺口 33 条、双键 3 条)
- `scripts/fp_match.py`, `scripts/t3_recompute.py` (尤其 `section_stats` / verdict 计算 / tb_* 列)
- `work/triage_merged.json` (1461 条, final_class), `work/t1_errata.json` (kb_loc / pending_user / t3_atom_err / t3_target_remap), `work/t2_pdf_typo_registry.jsonl`
- `evidence/checkpoints/t1_user_ack.md`, `t2_post_user_ack.md` (U1-U8), `t2_batch_table.md`, 各 `t2_B-*.md` / `t2_S-*.md` (按需)

## 步骤 (按序; 前一步有阻塞就停下报告, 不要硬往下走)

### S0 现状回归 diff (只读)
重跑全局 fp_match (命令见回归文档 §2, 输出放 `work/scratch/t3/`), 与 `work/t2_fp_expected_regressions.jsonl` (60 条, 定格于 HEAD 50c3958, 早于 S-CT/S-TYPO 等扫描批) 做 diff.
新增回归逐条按 R1/R2/R3/R4 定性 (同 classify.py 证据法: KB 侧 / PDF 侧证据词实测), 追加到一份新清单 `work/t3_fp_expected_regressions.jsonl` (60 旧 + 新增, 字段同旧). **R4 (真丢失) ≠ 0 → 停, 报告, 不进 S2.**

### S1 errata 补全 → `work/t3_errata.json` (不改 t1_errata.json; 新文件 = t1 errata 的 t3 段展开版)
- `t3_atom_err` 拆成两类: R1 (原子抽错, KB=PDF) → 终态 `ATOM_ERR`; R2 (原子=PDF, KB 有意偏离, 有 T-n / PDF_TYPO) → 终态 `PDF_TYPO`. 每条带依据 (checkpoint 路径 + T-n).
- `_B-FA` 组键展开为 23 条逐条 remap (清单在 `evidence/checkpoints/t2_B-FA.md` fp 节); 回归文档列的 33 条缺键补齐; 3 条双键 (`ig34_p0257_a010/a016`, `ig34_p0218_a014`) 两键都有.
- `pending_user` 4 条: 查 T2 对应批是否实修, 记结论 (实修且 target 命中 → 可翻; 否则残留并标 T4 待裁).

### S2 T3.1 回写脚本 `scripts/t3_writeback.py` → `work/coverage_ledger.wc.jsonl` (先备份为 `work/coverage_ledger.wc.pre_t3.jsonl`, 记前后 md5)
允许集 = `triage_merged.json` 1461 atom ∪ 显式 T2S 清单 `work/t3_t2s_atoms.jsonl` (每行 atom_id / batch / 证据 checkpoint 路径 + 行号; **只收扫描批明确声明"修复/补入了该原子"的**, 不要 grep checkpoint 里所有 atom id — 那里混有抽样提到的).
映射规则 (每条写 `matched_by = {phase:"TB", subagent_type:"script/t3_writeback", batch_id, evidence, prompt_version:"t3_writer_v1.0", ts}`):
- EXACT: **只有**当场在现 KB 的 target 文件 (remap 后) 命中 `fp_match.norm(verbatim)` 才给.
- EQUIVALENT: 非逐字, 且有证据: PRESENT/REWRITE_OK 由 T1.2+T1.3 一致判定 (指 triage 记录); REAL_GAP/VALUE_DIFF/RELOCATE 由 T2 批 checkpoint 声明已修 + reviewer/auditor PASS (指针到文件:行). 没证据 → **保持原 verdict (残留)**, 列入报告, 不批量翻.
- INTENTIONAL_EXCLUDE: final_class=IE 且在 `t1_ie_final.md` 用户 ack 清单内 (category / exclusion_reason / approved_by 写明 ack 文件).
- ATOM_ERR / PDF_TYPO: 按 S1.  FIGURE → `FIGURE_DEFERRED`.
- 断言 (脚本内, 失败 exit 1): 改动行 atom_id ⊆ 允许集; 未改行与备份逐字节相同; 每条改动行 matched_by.phase=="TB"; 统计每类翻转数.

### S3 T3.2 重算 + 复验
1. 先确认 `t3_recompute.py` stock 口径 (aggregate_verdict / coverage_density / 全局覆盖率) 如何对待新 verdict ATOM_ERR / PDF_TYPO / FIGURE_DEFERRED. 若当成未覆盖导致 G-TB3 假性下降, **不改原 stock 逻辑**, 另加一列/一个报告口径并写明映射 (06 口径视作 IE 类排除) — 两个数都报.
2. **直接命中复验** (回归机制对 T2 新补的原子是盲的: 它们在 T0 baseline 本就不命中): 对 ledger 中范围内所有 EXACT (含本次新翻) 在现 KB target 上直接查 `norm(verbatim)` 子串, 不命中即列出; 对本范围外原有 EXACT/EQUIVALENT 用 fp_match regress 差集 (regress − t3 期望清单) 复验. 差集非空 → 才喂 `--downgrade`, 且只喂差集.
3. 跑 `t3_recompute.py` 出 `work/section_coverage.wc.jsonl` (前后 md5), 报 G-TB1 残留 (按节/按类)、G-TB2 节 pass 数与未过节清单、G-TB3 全局覆盖率 (06 口径 vs 99.02%)、G-TB7 (`python3 tools/check_links.py 2>&1 | grep "live docs"` ≤ 42).
4. G-TB6 反向溯源: `git diff <T2 前基线 commit>..HEAD -- knowledge_base/` 每条新增内容行能在 PDF 页文本 (`work/pdf_pages/`, 归一化) 找到; 找不到的按 结构行 (表头/锚点/分隔) / PDF_TYPO 登记 / U1-U8 规则产物 (CT 短名、排版字符) / 未解释 分类, 未解释的逐条列出. 基线 commit 从 git log 找 T2 首批 (B-PCPP) 之前那个, 写明.
5. 变异 (规则 5): 在 KB 临时副本 (`work/scratch/t3/kbcopy`, 不碰真 KB) 删一句 T2 新补内容 → S3.2 直接命中检查必须变红; 复原变绿. 真 KB md5 前后一致.

### 输出
- `evidence/checkpoints/t3_recompute.md`: 每步命令 (可复跑, 用户规则: 写"实测"必附命令) + 计数 + 残留清单 + 阻塞项. G-TB1 只能写 "数值达标/不达标, 用户 ack 待 T4", 不写 PASS.
- 回写翻转率 >50% 时附 `evidence/step_T3_audit_prep.md`: 按类列出供 reviewer 抽样的全集文件路径.
- 返回: 简短汇总 (各类翻转数、残留数、G-TB1/2/3/6/7 数值、R4 数、阻塞项).
