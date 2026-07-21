# S4 三修 (dist 同义词 + 斜杠变体 + 短词锚定) — Result Record

> 状态: **PASS / 全类 ≥95% gate 恢复** (2026-06-12) — retrieval-only, v3 140q,
> collection `sdtm_kb_v1` (4146 chunks, 未重建)
> 上游: `testset_v3_expansion_summary.md` §4-§6 (v3 暴露的 gate FAIL + 根因分类 + 修复提案)
> Rule D 审查: `s4_rule_d_review.md` — **APPROVE_WITH_NITS** (0 CRITICAL/HIGH, 2 MED 已采纳, 4 LOW 记录)

## 背景

题集 v3 (140q) 暴露 per-category gate FAIL: cross 93.0% / single 92.5%, 其中 q139/q140 是
ON 劣于 OFF 的真回归 (s3 守卫排除 + hybrid collateral 组合伤害)。根因四类, 本修针对前三类
(全部 pattern 级); 第 (d) 类 (概念定义→chapters/model 通道, q73/q119/q126) 单独立项。

## 三修内容 (`server/structured_lookup.py`)

| 修 | 内容 | 性质 |
|----|------|------|
| (a) | `_DIST_DOMAINS_RE`: `\bdomains\b` → `\b(?:domains\|datasets)\b` | 同义词泛化; 已知变量+成员动词双锚不放宽 |
| (b) | 斜杠复合长名变体: 含 "/" 的 token 按备选展开 ("Concomitant/Prior Medications" → +"Concomitant Medications"+"Prior Medications") | KB 数据驱动通用变换; 自动覆盖 CM/IE/TI/TU/TR 全部 5 个斜杠名 (10 变体), 非只修动机题 |
| (c) | 短词单词长名 (<10 字符, EX "Exposure"/CO "Comments") 由整体跳过改为**锚定匹配**: 仅 `<name>\s+(dataset\|domain)s?\b` fire; "data" 故意不作锚 (太松) | 守卫放宽但保留防撞; q96 "Cumulative Exposure)" 实测不 fire |
| 附带 | matcher 排序键 pattern 串长 → 长名长度 (锚定后缀会污染串长排序) | 正确性修复, "Exposure as Collected" 仍胜 "Exposure" |

## 验证 (五层防御, 全过)

1. **pytest 236 passed** — 新增 `scripts/tests/test_structured_lookup.py` (本模块首个单测, 22 用例):
   存量行为锁定 + 三修正反例 + **集外泛化探针** (SITEID 分布 / "Prior Medications" / "Comments
   domain" / EC 不被遮蔽) + 负例 (裸 "Exposure" 散文不 fire / q96 撞车案例) + map 卫生不变量。
2. **s3 探针 13/13**: 全部长名题走确定性通道 (修前 10/13; q134 经斜杠变体, q139/q140 经锚定)。
   `eval/ablation_t1/v3_s3_probe_fixed.json`。
3. **零回归 gate**: v3 140q ON 复跑逐题 diff (`v3_on.json` vs `v3_on_fixed.json`):
   **救回恰好预测的 4 题 (q107/q134/q139/q140, 全 0%→100%), 回归 0 题**;
   9 题 top5 顺序变化全部 recall 不变 (union-add 注入只增不删)。OFF 臂构造上不变
   (`structured_lookup_enabled=False` 不实例化本模块)。
4. **逐类别成绩** (v3 140q retrieval-only, --structured-lookup --hybrid):

   | 类别 | 修前 ON | **修后 ON** | gate ≥95% |
   |------|---------|------------|-----------|
   | single_domain (40) | 92.5% (净负于 OFF) | **100%** | ✅ |
   | cross_domain (50) | 93.0% | **95.0%** | ✅ (零 margin) |
   | concept (25) | 100% | 100% | ✅ |
   | mixed (25) | 100% | 100% | ✅ |
   | **overall** | 95.4% | **98.2%** | ✅ |

5. **Rule D 异 type 代码审** (`oh-my-claudecode:code-reviewer`): APPROVE_WITH_NITS。
   审查员独立复跑 pytest + git stash 对照存量行为 + grep 验证 logic 零 eval 题面 token
   (反过拟合确认: "genuinely pattern-level, not example-tuned")。
   2 MED 已当场采纳 (均为测试加固): MED-1 多斜杠 token 守卫断言 (未来 KB 名变化 fail loudly) /
   MED-2 "datasets" 同义词 union-add 保序探针。

## 已记录的 known boundaries (审查 LOW, 按建议不反应式修)

- **存量**: "Procedures" (10 字符)/"Disposition" (11) 过 ≥10 阈值裸匹配, 泛义散文
  ("standard procedures") 会误注入 PR/DS spec — **本修未引入未恶化** (git stash 对照确认);
  union-add 语义下伤害上限是 top-15 尾部挤压, 零回归 gate 实测 0 伤害。后续若做, 走
  "常见英语词锚定" 泛化, 不针对这两词。
- "datasets" 同义词会给部分单域题多注入 VARIABLE_INDEX (recall-additive, 不挤掉 gold,
  MED-2 探针已锁定保序)。
- matcher 等长名平局按 dict 插入序 (确定性, 未显式文档)。

## 残留 (本修范围外, 下一杠杆)

q73 / q119 / q126 — 同一类: 概念/定义型 gold 在 chapters/model, 题面不点名域
(--LNKID/--LNKGRP 定义、SE-TE 对比、RDOMAIN 载体清单)。cross 95.0% 零 margin,
把 cross 拉开需此 **(d) "通用变量/概念定义 → chapters/model 定义文件通道"** 立项
(P1 时已记录的方向, 架构件)。

## 改动文件

- `server/structured_lookup.py` — 三修 (上表)
- `scripts/tests/test_structured_lookup.py` — 新增 22 用例 (本模块首个单测)
- `eval/ablation_t1/v3_on_fixed.{json,log}` + `v3_s3_probe_fixed.json` — 修后 evidence
- 生产语义: structured_lookup 默认开 (config), 本修随下次部署生效; KB/向量索引/提示词未动
