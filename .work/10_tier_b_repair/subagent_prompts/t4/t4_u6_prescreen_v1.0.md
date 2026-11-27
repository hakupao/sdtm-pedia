# U-6: T4.2 人工抽样 42 条 AI 预筛 brief v1.0 (general-purpose)
<!-- chain: E (plans) -->
先读 `subagent_prompts/t4/t4_common_v1.0.md`.

## 任务
`.work/10_tier_b_repair/evidence/checkpoints/t4_human_sample.md` 是交给主人 (人工) 判定的 42 条抽样包, 文件头 "怎么判" 一节是判据. **你不是主人, 你做的是 AI 预筛, 不是人工判定.**
- **绝不修改 `t4_human_sample.md`** (不勾选、不填备注), 也不要运行 `scripts/t4/t4_render.py` / `t4_sample.py`.
- 对每条: 打开包里给的 PDF 页 (文本层 + 渲染页) 和 KB 现文 (自己 Grep 定位, 包里行号可能偏), 判 KB 是否忠实承载 PDF 信息 (内容错误 = 漏信息 / 改了意思 / 值不对 / 放错位置). 终态为 ATOM_ERR / PDF_TYPO / INTENTIONAL_EXCLUDE 的按包里 "怎么判" 的特别说明判.

## 判定 (先定)
每条三选一: **内容正确** / **内容错误** / **看不出** (说明缺什么). 每条 1-3 句理由 + 依据 (PDF 页:行或渲染页; KB 文件:行).

## 输出
写到 `.work/10_tier_b_repair/evidence/checkpoints/t4_human_prescreen.md` (只写这一个文件):
- 顶部写明: `> 性质: AI 预筛 (general-purpose, opus), 不是人工判定; 不替代 T4.2 人工闸; t4_human_sample.md 用户判定栏保持空白.` 以及日期 2026-11-27、KB 版本 = 当前 HEAD 的 KB (冻结).
- 表: `# | atom_id | 层 | 终态 | 预筛 | 理由 | 依据`
- 按层计数 (REWRITE_OK 10 / REAL_GAP 10 / VALUE_DIFF+IE 10 / RISK_ANCHORLESS 12).
- 样本外发现单列.
回复正文只给: 分层计数 + 内容错误/看不出的编号与一句原因 + 文件路径 (≤ 200 字).
