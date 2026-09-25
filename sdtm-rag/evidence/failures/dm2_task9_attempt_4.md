# DM2 T9 attempt 4 — 规则句修订后仍未达 §0″ 目标 (2026-09-25)

> 规则 B 归档。判据 `evidence/checkpoints/dm2_dossier_e2e.md` §0″ (`b3b85c8` + 跑前补注 `7b9bdd0`); 判定摘要 §2.4。

## 输入
- 规则句 `f8523ad` + 审查修订 `7b9bdd0`; 生产 auto 暂停 (`5bd233a`), 跑批 `dossier:"on"`。
- 复跑: `.venv/bin/python -u eval/prod_wirein/dm2_e2e_run.py --no-resume --qids dm01,dm02,dm05,dm03,dm04,dm07 --out-subdir dm2_e2e_attempt4 --require-no-fallback --dossier on`

## 产物
- gitignored `data/study/st01/eval/runs/dm2_e2e_attempt4/` (12 run + judge_pack + judge_verdicts)。

## 技术判定
- G0 PASS (12/12 attached, 真未回退)。

## 业务判定 — FAIL (目标每模型 6/6)
- opus-5 6/6 (主判; ④″(ii) 严口径 3/6), sonnet-5 4/6 (任何口径 ≤5/6)。
- 修订有效的部分: 捏造 2→0, SDTM 变量捏造 2→0, 分类轴 7/12→12/12, opus 语言 zh→ja 消失。
- 仍失败: sonnet 英文问句仍日文作答 (attempt 3 同题同病); sonnet 小分母域 precision 越线。

## 下一 attempt 输入 (待用户裁定)
- ④″(ii) 四种形态的口径须用户写死 (决定 opus 是 6/6 还是 3/6)。
- sonnet 语言跟随: 规则句层已写, 未压住 ⇒ 考虑结构性手段 (如按问句语言在 user 消息尾部追加一行语言指令) 而非再加措辞。
- 泛化须新建留出题; gold 生存转归卡复核; ⑤″ 真值源 (spec vs assumptions) 不一致需定。
