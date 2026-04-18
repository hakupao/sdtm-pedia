# B3 Review — score_codelists.py

> 复核日期: 2026-04-18
> Reviewer: oh-my-claudecode:code-reviewer (model=opus, agent aeeca56ba3fcf3a69)

## 结论
**PASS**

## 抽样验证 (5 项)
- Total ≈ 1005: ✓ (实测 Total codelists: 1005, 命中目标)
- NY/FREQ in top 200: ✓ (NY=rank 1, score 10.669; FREQ=rank 2, score 10.232 — 两者均因 hit_bonus 10.0 登顶)
- AERELN/PROBLEM_TYPE 报告为 not mapped 不崩: ✓ (输出 `AERELN: (not mapped / not in knowledge_base)` 与 `PROBLEM_TYPE: (not mapped / not in knowledge_base)`, exit=0)
- top 200 估 token ∈ [150K, 300K]: ✓ (201,660 tokens, 正中目标 ~200K)
- rank 201-500 估 token ∈ [250K, 500K]: ✓ (338,070 tokens, 在目标 300-400K 内)

## 算法复核

### sigmoid_term 实现
公式与 spec 一致 `1 / (1 + abs(log10(n+1) - log10(SIGMOID_CENTER_N)))`, `n<=0` 直接 return 0.0. 数值抽验:

| n | f(n) |
|---|------|
| 0 | 0.0000 (guard 正确) |
| 1 | 0.4595 |
| 3 | 0.5333 |
| 10 | 0.6965 |
| 30 | 0.9860 (峰值, 预期) |
| 100 | 0.6548 |
| 1000 | 0.3963 |

对数空间对称帽型符合设计, 两端衰减, 30 附近最高. 峰值 0.986 而非 1.000 源于 `log10(n+1)` vs `log10(30)` 的 +1 偏移, 属已接受的简化.

### 3 个 codelist term_count 人工核对

| C-code | 名称 | 文件 | 脚本报告 | 手工核对 | 结果 |
|--------|------|------|----------|----------|------|
| C66742 | No Yes Response | `terminology/core/general_part4.md` L5 | 4 | 4 (N/NA/U/Y) | ✓ |
| C71113 | Frequency | `terminology/core/interventions.md` L14 | 101 | 101 | ✓ |
| C99079 | Epoch | `terminology/core/general_part2.md` L88 | 12 | 12 | ✓ |

注: 落在多文件的 codelist (e.g. general_part1+part2) 由 `agg[c_code][1] += term_count` 累加, spec 明示要求, 已覆盖.

### 2 个 codelist domain_ref 人工核对

| C-code | 脚本报告 | 独立 grep | 结果 |
|--------|----------|-----------|------|
| C66742 (NY) | 164 | 164 | ✓ |
| C71113 (FREQ) | 12 | 12 | ✓ |
| C99079 (Epoch) | 88 | 88 | ✓ (附加抽样) |
| C71620 (Unit) | 90 | 90 | ✓ (附加抽样) |

排行榜头部结构 sane: C66742 (164) 为最大值, C71620 (90) 与 C99079 (88) 紧随其后.

## 幂等 + 只读
- 幂等: ✓ (连跑两次, stdout 45294 字节, md5 `14301884a359773ff37d44e2b8bc5719` 双测一致, byte-identical)
- 只读: ✓ (grep `open\(|write|remove|unlink|shutil|subprocess|os\.system|\.mkdir|rmtree` 零命中; 仅 `read_text()` 读文件)

## 关键发现 (≤ 200 字)

脚本规范、安全、可复现, 完全满足 B3 规范. 观察点:
1. 仅 Python 3 stdlib (math/re/sys/pathlib), 合规.
2. T-hit 经 C-code 匹配, 设计稳健. AERELN/PROBLEM_TYPE 明确标 `""` 触发 not-mapped 分支, **不影响 merge 但建议 PLAN §T18/T20 调整为已存在的 codelist 名**.
3. Top 200 token 估算 201,660 精准命中 ~200K; 201-500 为 338K 属理想中段.
4. [LOW] is_t_hit 每次重建 hit_c_codes set, 1005×2 量级无性能问题.
5. [LOW] count_domain_refs 拼 combined text 再逐 C 扫描, 未来规模增长可用 Counter 优化. 非阻塞.
6. [NIT] Docstring 与实测浮点有口径差 (0.37 vs 0.3963), 不影响算法.
7. 规则 D 合规: 独立 session, 未改脚本.

## 下一步
**PASS → 进 Task B4**.

**Flag for planning**: PLAN §5 T18/T20 涉及的 AERELN 和 PROBLEM_TYPE 在 knowledge_base 中找不到, 建议后续 A/B 测试题目替换为存在的 codelist (如 C66742/NY 或 C71113/FREQ), 或 user 在 Claude.ai 自行核对这些是否为别名.
