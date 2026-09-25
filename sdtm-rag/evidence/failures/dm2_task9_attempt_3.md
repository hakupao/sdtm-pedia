# DM2 T9 attempt 3 — Claude 两模型 + 留出题 未达预登记目标 (2026-09-25)

> 规则 B 归档。判据 `evidence/checkpoints/dm2_dossier_e2e.md` §0′ (commit `19e6ea3`, 跑前); 判定摘要 §2.3。

## 输入
- 代码 `19e6ea3`, `_DOSSIER_RULES` = `03096ad` 原样; 生产进程启动晚于最后一次 server commit (无需 kickstart)。
- 6 题 (in-sample dm01/02/05 + 留出 dm03/04/07) × `opus-5`/`sonnet-5` = 12 run, 全部 `fell_back=False`。
- 复跑: `.venv/bin/python -u eval/prod_wirein/dm2_e2e_run.py --no-resume --qids dm01,dm02,dm05,dm03,dm04,dm07 --out-subdir dm2_e2e_claude --require-no-fallback`

## 产物
- gitignored `data/study/st01/eval/runs/dm2_e2e_claude/` (12 run json + `judge_pack.json` + `judge_verdicts.md`)。

## 技术判定
- G0 PASS (12/12 attached, 12/12 真未回退)。

## 业务判定 — FAIL
- opus-5 in-sample 2/3 (目标 3/3), 留出 2/3 (达标); sonnet-5 1/3 / 1/3。
- 失败模式 (pattern 级, 不写题面):
  1. **无 CT 分组轴的声明被跳过** (sonnet 3/3 题): 规则句要求「域无 `--CAT` CT 时明说并点名替代轴」, sonnet 直接按表单分组作答。
  2. **CT 取值被意译 / codelist 名顶替或静默缺失** (两模型 dm02 ja): attempt 1 的类别轴失败模式在另一模型族上复现。
  3. **非候选段也会点名不存在的 OID** (opus dm07 排除清单 1 个; sonnet dm07 候选表 3 个虚构表单 OID)。
- 口径敏感: 两处歧义 (意译是否算写出 CT 值 / 捏造作用域) 宽判则 opus 达标; sonnet 任何口径不达标。本轮不改判。

## 判据本身暴露的缺口 (供 §0″)
- CT 取值须以原文大写字符串出现 (写死); 捏造作用域 = 全文 (写死); ③′ 上级标记能否覆盖子组 / 组尾总结句是否算;
  precision 定义过窄 18/18 = 0% 无判别力; SDTM 侧正确性 (虚构变量) 无条款; 答题语言一致性未入判据; judge pack 缺 G0 字段。

## 下一 attempt 输入 (待用户裁定, 不自动进行)
- attempt 4 = 规则句 pattern 级修订 (候选: 把「无 CT 时声明 + 点名轴」前置为独立必答步骤; CT 取值必须原文照抄; 全文 OID 只许出自一览) + §0″ 判据写死上述歧义 (**跑前**登记) + 6 题 × 2 模型全部重跑。
- 注意: §0″ 收紧判据后 attempt 3 须用新尺子同步复判, 才能与 attempt 4 比较。
