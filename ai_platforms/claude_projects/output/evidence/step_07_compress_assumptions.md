# Step 7: compress_assumptions.py

> 计划锚点: [PLAN.md §7.4 Step 7](../../PLAN.md)
> 执行日期: 2026-04-17
> 状态: **PASS**

---

## 1. 输入
63 × `knowledge_base/domains/<DOM>/assumptions.md` (53,708 tokens)。目标 ≤20K。

## 2. Agent
| 角色 | model | duration | 结论 |
|------|-------|---------|------|
| executor | opus | 302s | 17509 tokens, 63/63 |
| reviewer | sonnet | 95s | APPROVE, 0 blocking issues |

## 3. 产出
- `scripts/compress_assumptions.py` (595 行)
- `output/06_assumptions.md` (md5 `742a57c06a760bda55106e63251a070d`, **17509 tokens**, 63/63 域)

压缩手法: 行级解析 `N.` / `   a.` 骨架 → REWRITES 固定词表改写（"Section X.Y"→"§X.Y" 等）→ 每 item 1 句，硬截断 top=130/sub=95 字符，`_keep_sentence` 偏向含变量名/CT 码/§引用的句子。

## 4. 复核（Reviewer 独立抽样）
| Domain | Source 顶层 | Output 顶层 | Match |
|--------|:-:|:-:|:-:|
| AE | 12 | 12 | ✓ |
| MH | 7 | 7 | ✓ |
| LB | 8 | 8 | ✓ |
| CM (独立) | 5 | 5 | ✓ |
| VS (独立) | 4 | 4 | ✓ |
| QS (独立) | 10 | 10 | ✓ |

- 63/63 `## <DOM>` + 63 `<!-- source: -->` ✓
- 变量名/CT code/§refs 保留，PDF 页码/长示例/CRF 图表删除 ✓
- mtime 时间戳, 幂等 ✓
- 源未修改 ✓

## 5. 偏差
无阻塞。1 LOW: char/4 估算 18952 vs tiktoken 17509（编码器差异，非功能问题）。

## 6. Checkpoint
否（§7.4 Step 7 无 checkpoint）。

## 7. 累计
- 总 token: 162,565 / 195K (83.4%)
- subagent: 2, 重试 0

## 8. 下一步
Step 8 返工 (content-free bullets 修复)，Step 9 已 accept。
