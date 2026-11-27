# U-7: A/B 逐行复核 brief v1.0 (pr-review-toolkit:code-reviewer)
<!-- chain: E (plans) -->
先读 `subagent_prompts/t4/t4_common_v1.0.md`. 被审表: `.work/10_tier_b_repair/evidence/checkpoints/t4_user_decisions.md` §0 (用法), §1 A1-A3, §2 B 组. 你只读 KB 与既有文件, 不改它们 (该文件也不改); 只写下面指定的一个输出文件.

## 规则 (裁定方已定, 你逐行套用, 不改规则)
- A = 照录 PDF (KB 保持 PDF 原值); B = KB 改为候选值.
- **默认 A.** 只有当该行的正确值能被**单值确定**时才 B. 合格依据仅限: (i) CT 提交值 (`knowledge_base/terminology/` 里的 codelist 提交值), (ii) spec 约束 (该域 spec.md / SDTMIG 规则明确只允许一个值), (iii) **同页**表值 (PDF 同一页的表格给出唯一值), (iv) 语法上只有一种补法 (与已接受的 B-IS T-5 "participating in"、B-ch01 T-1 "has not yet been" 同口径: 只能这样补, 不存在第二种合理改法).
- 不合格: 跨页/跨例推断、"多数写法"、"疑似"、两种以上改法都通、改正属语义改写.
- 草拟建议不是前提; 草拟 B 的依据栏若自写 "不单值 / 无依据 / 不可唯一" 要特别核.

## 审什么
1. **A1-A3 中草拟建议为 B 的 26 行**: A1-9, A1-21, A2-2, A2-3, A2-4, A2-5, A2-6, A2-7, A2-8, A2-11, A2-12, A2-14, A2-15, A2-16, A3-2, A3-5, A3-7, A3-8, A3-9, A3-14, A3-15, A3-24, A3-28, A3-31, A3-32 (随 SE T-2), A3-34. 每行判 **维持 B** / **改回 A**. 草拟为 A 的行不审.
2. **B 组 15 行 (B-1..B-15, KB 已写正确值)**: 判 **维持** / **否决** (正确值其实不能单值确定 → 改回 PDF 原样).
每行都要: 核 PDF 原值确实如表所写 (渲染页), 给出决定性依据 (文件:行 / PDF 页 / CT codelist 行); 维持 B 的行还要写出**精确改法**: KB 文件:行, 旧串 → 新串, 以及同一 PDF 问题的全部 KB 副本 (Grep 全库找; 例 A3-31/A3-32 SE/SM 两处).

## 输出
写到 `.work/10_tier_b_repair/evidence/checkpoints/t4_u7_rowcheck.md` (只写这一个文件; 顶部状态行 `> 状态: 审查完成 (2026-11-27), 审查者 pr-review-toolkit:code-reviewer (opus)`), 内容:
1. 表: `行 | 判定 | 单值依据类型 (i-iv 或 无) | 决定性依据 | 精确改法 (维持 B 时) / 否决回退 (否决时)`
2. 计数: A1-A3 维持 B n / 改回 A n; B 组 维持 n / 否决 n.
3. 顺手发现 (不修) 单列.

回复正文只给: 两组计数 + 改回 A / 否决的行号与一句原因 + 文件路径 (≤ 200 字).
