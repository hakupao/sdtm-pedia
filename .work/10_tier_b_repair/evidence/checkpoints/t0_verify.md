# T0 独立复核 (T0.2 / T0.3 / T0.3b / T0.4, G-TB9)

> 状态: **PASS** (2026-11-25); 复核: `oh-my-claudecode:verifier` (与 executor 不同 subagent_type, 规则 D)
> 所有命令在仓库根 `/Volumes/DevSSD/Project/sdtm-pedia` 运行, `T=.work/10_tier_b_repair`, `SP`=会话 scratchpad (仓库外).
> 没有信任 `t0_mutation.{md,log}`, 全部重跑. 除本文件外未改任何文件.

## 0. 前置
- `find knowledge_base -type f | sort | md5` (全部文件, 不只 *.md) = `5ae88550adcecaf3c9349233f7fa07fc`; `git status --short knowledge_base archive releases` 为空.
- 工作副本 md5 与 archive 原件一致: coverage_ledger `620c4a19…`, pdf_atoms `b5dfa317…`, md_atoms `24396ac0…` (`md5 -q archive/deep_verification/X $T/work/X`).

## 1. T0.2 — PASS
- `python3 -I $T/scripts/t3_recompute.py --out $SP/sc_v.jsonl --check-against archive/deep_verification/section_coverage.jsonl`
  → `CHECK ... rows ref=399 got=399 differing=0`, `RESULT: GREEN`, exit 0.
- 自写独立 diff (python, 去 aggregated_by + tb_*): rows 399/399, unique keys 399/399, diff 0; 比对 21 个原有字段.
- 灵敏度 (防空转): ledger 副本里把 `ig34_p0008_a022` EXACT→MISSING, `--ledger $SP/ledger_mut.jsonl` 重跑 → `differing=1`, `RESULT: RED`. 比较器不是空比.
- 新增 `--out` 默认在 work/, 拒写 archive/ (代码 L43-44).

## 2. T0.3 — PASS
- `ls $T/work/pdf_pages | grep -c ^ig34_p` = 461, `^sv20_p` = 74; `pdfinfo` 两个 PDF Pages = 461 / 74.
- 页对齐抽查: `pdftotext -layout -f p -l p` 单页重抽 vs 缓存, ig34 p1/p140/p278/p461 + sv20 p30/p74 全部 MATCH.
- `git check-ignore -v`: `pdf_pages/*` ← `work/.gitignore:2`; `pdf_atoms.jsonl` ← :6; `md_atoms.jsonl` ← :7; `scratch/` ← :4. `git ls-files $T/work` 为空 (无已跟踪文件).
- 注: `work/.gitignore` 本身尚未跟踪 (git 已生效, 但须随 T0 一起提交). 未被忽略的 work 文件 = coverage_ledger.wc / section_coverage.wc(.baseline) / fp_baseline / census_BPCPP.json, 均为 archive 已公开数据的副本或派生 (archive 的 pdf_atoms/md_atoms/ledger 本就在 git 中), census json 含少量表格 cell 值, 风险低.

## 3. T0.3b / T0.4 — PASS
- 读 `scripts/t0_mutation.sh`: 写路径只有 `$K=$T/work/scratch/knowledge_base` (rm -rf / cp -R / heredoc 写入均在 `$K` 下); 真 KB 只读 (cp 源). 每个变异前 assert 原文精确匹配, 防止"改了个不存在的东西". fp_match 拒写 archive/ 与 knowledge_base/; table_census / t3_recompute 只写 `--out`.
- 扫描 `TODO|FIXME|stub|NotImplemented`: 0 命中.
- `bash $T/scripts/t0_mutation.sh > $SP/mut_rerun.log 2>&1` (1:38, exit 0). 结果 (fp / census / t3 退出码):
  | 变异 | fp | census | t3 |
  |---|:-:|:-:|:-:|
  | M0 原样 | 0 | 0 | 0 |
  | M1 删 1 句 | 1 (regressions=1) | 0 | 1 (differing=1) |
  | M2 改表值 | 0 | 1 | 0 |
  | M2b 挪空格 | 0 | 1 | 0 |
  | M2c 折行值 | 0 | 1 | 0 |
  | M2d 删行 | 0 | 1 | 0 |
  | M3 删子节 | 1 (regressions=23) | 0 | 1 (differing=2) |
  | RESTORE | 0 | 0 | 0 |
  与 executor 的矩阵逐格一致. 前后真 KB md5 均 `5ae88550…`.
- 基线不是手造的: 在真 KB 重跑 `fp_match.py --out $SP/fp_fresh.jsonl` 与 `work/fp_baseline.jsonl` 排序后 byte-identical (atoms checked 6636, hit_target 3365 — 非空比);
  `table_census.py ... --baseline $T/work/census_BPCPP.json` → identical (18 PDF 表 / 24 KB 表 / 3551 cells compared);
  `sc_v.jsonl` vs `section_coverage.wc.baseline.jsonl` 399 行 diff 0.
- **自设变异 V1 (executor 未做)**: 新临时副本 `$SP/kbv/knowledge_base`, `domains/ML/examples.md:57` 原子 `ig34_p0124_a011` (EXACT, 文件内唯一) 改 1 个字符 `7-month`→`8-month`.
  `fp_match.py --kb-root $SP/kbv/knowledge_base --baseline ... --regress-out $SP/reg_v1.jsonl` → `regressions=1 REGRESS ig34_p0124_a011`, `RED`, exit 1;
  `t3_recompute.py --downgrade $SP/reg_v1.jsonl --baseline ...` → `DIFF §6.1.4 [Meal Data (ML)] coverage_density 0.5376→0.5269, tb_residual_gap 42→43`, `RED`, exit 1. 单字符改动被捕获.

## 4. 收尾
- `git status --short knowledge_base archive releases` → 空; KB 全文件 md5 = `5ae88550adcecaf3c9349233f7fa07fc` (不变).

## 5. 盲区 / 非阻塞问题
1. `t0_mutation.sh` 只打印退出码, 不断言预期 (脚本恒 exit 0); 红绿判定靠人读 log. 建议加 expect 表 + 不符即 exit 1. — 低
2. fp_match 只覆盖 scope (inventory 174 节 + Issue 5 主节); scope 外的 KB 改动看不到; norm 会抹掉 `| * _ # >` 等符号, 只改这些符号的变异按设计不变红. — 低 (已在 t0_mutation.md §3 列明部分)
3. `work/.gitignore` 未跟踪, 提交 T0 时必须一并提交. — 中 (版权护栏)
