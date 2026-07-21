# Step 9: catalog_terminology.py

> 计划锚点: [PLAN.md §7.4 Step 9](../../PLAN.md)（§7.7 checkpoint, 99% 压缩率）
> 执行日期: 2026-04-17
> 状态: **PASS (ACCEPT, 超目标但 floor-constrained)**

---

## 1. 输入
`knowledge_base/terminology/` 91 文件（core 42 + questionnaires 43 + supplementary 6）, 1,944,449 tokens。目标 ≤15K（压缩 99.2%）。

## 2. Agent
| 角色 | model | duration | 结论 |
|------|-------|---------|------|
| executor | opus | 403s | 20536 tokens, 1005 codelists, floor analysis 12505 在 names |
| reviewer | opus | 194s | **ACCEPT** - 独立穷举 5 种优化, floor 16.3K 确认不可压 |
| 用户 checkpoint | — | — | **Accept** (用户授权) |

## 3. 产出
- `scripts/catalog_terminology.py` (273 行)
- `output/08_terminology_map.md` (**20,536 tokens**, 1005 codelists, 91 file sections)

格式: `| CT Code | Codelist Name | Ext | Terms | -> Related Domain |`

## 4. Reviewer Floor 验证（关键）

| 方案 | Tokens | Delta |
|------|-------:|------:|
| **Baseline (当前)** | **20,536** | — |
| V1 删 Data Type 列 | 20,536 | 0（代码已不发射） |
| V2 Terms 粗桶化 | 21,656 | **+1,120** (反向!) |
| V3 删 Related Domain | 20,198 | +338（但损路由语义）|
| V4 Name 缩写 | 20,650 | -114 (反向, NCI 术语 BPE 高效) |
| V5 扁平 5 列 table | 30,281 | **-9,745** (灾难性) |
| V2+V4 | 21,770 | -1,234 (反向) |

**纯 floor (仅 code+name) = 16,270 tokens** — 1005 NCI 官方名称不可缩写。

## 5. 结构检查
- 91/91 `### <file>` sections ✓
- 1005 CT codes ✓
- Related Domain 覆盖 **75.5%** (低于 PLAN 80% 阈值 4.5pp，根因: 16 个 cross-domain heading 都是真跨域)
- 无 Term 值泄漏 ✓
- 幂等 ✓
- mtime 时间戳 ✓
- 源未修改 ✓

## 6. 偏差与处理

| 偏差 | 处理 |
|-----|------|
| 20,536 vs 15K 目标 (+37%) | **Accept** — floor 16.3K, 15K 语义不可达 |
| Related Domain 75.5% < 80% | 接受 — 16 个 cross-domain 标签是语义正确的 |
| PLAN §7.6 ">10% 重试"规则 | **不机械执行** — reviewer + executor 均独立确认 floor; 重试只会浪费 Opus tokens |

## 7. Checkpoint (§7.7)
- §7.7 要求: 是（99% 压缩容易丢东西）
- **PASS**: 1005 codelist 全部一行映射 ✓, 0 Term 值泄漏 ✓, 75% 域归属（比 80% 略低但语义正确）
- 用户 ack: Accept

## 8. 累计
- 总 token 后 Step 9: **183,101 / 195K (93.9%)**
- 剩余: Step 10 (2657) + Step 11 (≤4500) = 7,157
- 预计最终: ~190,258 / 195,000 (buffer 4,742)

## 9. 下一步
- Step 8 返工（attempt 2）
- Step 10 routing 复制（并行）
- Step 11 system_prompt 目标降至 ≤4500（用户授权）
