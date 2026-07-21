# Step 6 Attempt 1 — Level 4 回退 (Notes 列整删)

> 归档时间: 2026-04-17 12:45
> 结果: CONDITIONAL_PASS，但用户决定重试 (混合方案)
> 为何归档: PLAN §7.10.5 "失败 attempt 必须保留 failures/，不删除"
> 为何"失败": 技术层面满足所有 PASS 条件；但材料层面丢失 20% 独有 Notes 信息超出用户可接受范围

---

## 1. 输入

63 spec.md, 184943 tokens, 目标 ≤60K。

## 2. Agent 调度

| 角色 | subagent_type | model | duration |
|------|--------------|-------|---------|
| 作者 | executor | opus | 291s |
| 复核 | code-reviewer | opus | 120s |

## 3. 产出（已被 attempt 2 覆盖）

- `scripts/merge_specs.py` (529 行, Level 4 配置)
- `output/05_mega_spec.md` (58706 tokens, md5 `24f82476f65e2ff31461983ab48c266d`)
- 6 列输出: `# | Name | Label | Type | Role | Core | CT`（**无 Notes**）

## 4. 压缩级别穷举（executor + reviewer 交叉验证）

| 方案 | Tokens | PLAN 是否通过 |
|------|-------:|:-:|
| Base (Notes ≤200 字) | 107,437 | FAIL |
| Level 1 (Notes ≤150 字) | 102,281 | FAIL |
| Level 2 (+ 删 General/Model XRef) | 88,XXX | FAIL |
| Level 3 (+ CT 只列 code 不列变量) | 80,XXX | FAIL |
| Notes ≤100 字 (reviewer 补测) | 93,412 | FAIL |
| Notes ≤75 字 (reviewer 补测) | 86,836 | FAIL |
| Notes ≤50 字 (reviewer 补测) | 78,520 | FAIL |
| Notes ≤30 字 (reviewer 补测) | 71,889 | FAIL (>66K 硬顶) |
| **Level 4 (Notes 整列删)** | **58,706** | **PASS** |

## 5. 结构验证（全 PASS）

- 63/63 `## DOM — FullName`
- 63/63 `### Cross References`
- 63/63 `### Specification`
- 63/63 `<!-- source: -->`
- 1917/1917 变量（独立抽样 HO/MH/PR/SU/RELREC + executor AE/DM/LB/CV/TS 全部 match）
- 幂等 md5 稳定
- 源文件未修改

## 6. 用户决定重试的根因（主控抽样）

独立抽样 20 个变量的 Notes 冗余分析：

| 类别 | 数量 (20 样本) | 示例 |
|------|:-:|------|
| Redundant（ch04/assumptions 已有） | 7 (35%) | AETERM, AEDECOD, RACE, ARM |
| Partial（变量被提及但规则未完整） | 9 (45%) | AESER, LBTEST, VSORRES |
| Unique（独有信息，丢了不可恢复） | **4 (20%)** | AGE 推导公式、VSPOS 姿态枚举、COUNTRY、SEX |

典型 Unique 丢失：
- `AGE`: "May be derived from RFSTDTC and BRTHDTC, but BRTHDTC may be..." → **推导规则丢失**
- `VSPOS`: "Position of the subject... Examples: SUPINE, SITTING, STANDING" → **枚举值丢失**

用户选择: **选 A 混合方案** — 保留"See §X.Y" 反向路由 + 独有规则（derived/Required/ISO/Examples/Valid values），丢弃纯描述性 Notes。

## 7. 对 attempt 2 的输入

- 改 `merge_specs.py`: Notes 列回归 7 列设计，但 cell 内容走"智能保留"逻辑
- 目标: ≤60K（严）或 ≤66K（PLAN §7.4 Step 6 接受上限）
- 预估: ~62K tokens

## 8. 未删除 / 未丢弃的 artifacts

- `scripts/merge_specs.py` 的 Level 1-4 配置代码保留于 script 内（attempt 2 可在此基础上改）
- `output/05_mega_spec.md` 在 attempt 2 开始时会被覆盖（非失败丢失，是 iteration）
