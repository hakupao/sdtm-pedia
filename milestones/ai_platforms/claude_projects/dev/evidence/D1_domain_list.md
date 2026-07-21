# Stage v2.2 域清单 (批 2 输入)

> 产出日期: 2026-04-19
> 产出脚本: `scripts_v2/score_domains.py` (打分) + 主控 review
> 输出日志: `evidence_v2/D1_domain_score.log`
> 幂等确认: 与 B2 review 记录 (`B2_review.md`, md5 `cba513e0817f54ba09bcf26353e6e239`) 字节一致
> 上游 PLAN: `PLAN_V2.md §6 Task D1`

## 用户 20 必选

BE, BS, CE, CM, DD, DM, DS, EX, FA, GF, LB, MH, MI, PR, RS, SE, SS, SU, TR, TU

## T_test_hits 必选 (非用户清单部分)

AE, PC, PP (另 EX, MH, LB 与用户清单重合)

## 打分新增 (按 merge 规则, top-5 非必选补齐至 28)

| 域 | score | 入选原因 |
|----|-------|---------|
| IS | 0.53 | Immunogenicity, 最长 examples.md (13694 tokens) |
| CP | 0.48 | Cell Phenotype, marker string 规则密集 |
| EG | 0.39 | ECG, 高频临床域 + QT 校正逻辑 |
| MB | 0.38 | Microbiology, 与 MS 共享 examples |
| MS | 0.35 | Microbiology Sensitivity, 药敏测试 |

## 主控人工补充判定

- **PC+PP 硬 pin**: ✓ 已通过 `must (T_test_hits)` 进入 merge_set (v2.1 T3 衰减案例的源文件所在域, 批 2 必须覆盖)
- **是否补 VS/EG**: EG 已在 top-5 (0.39) 自动入选; VS score 0.17 排 16, T1-T12 无 VS 专题, 不手工补, 延后到 E1 批 3 others tier 兜底
- **是否补 TA/CV**: TA (0.30) 和 CV (0.30) 在 top-10 内但 slot 已被 IS/CP/EG/MB/MS 填满; CV 与 T8 "CV 域所有变量值范围" 相关, 但 T8 精度需求靠 05_mega_spec (已在 v2.1 上传) + E1 批 3 others tier 兜底, 不手工提前
- **总数**: 28 域, 严格贴 MERGE_MAX 上限 (设计允许 25-28), 无溢出

## 最终清单 (28 个域)

```
AE, BE, BS, CE, CM, CP, DD, DM, DS, EG,
EX, FA, GF, IS, LB, MB, MH, MI, MS, PC,
PP, PR, RS, SE, SS, SU, TR, TU
```

## Cross-check vs v2.1 test matrix 覆盖

| 测试题 | 关键域 | 是否在批 2 清单 |
|-------|-------|---------------|
| T1 AEDECOD Core | AE | ✓ |
| T2 AE severity 变化 | AE | ✓ |
| T3 PC↔PP RELREC 4 方法 | PC, PP | ✓ (v2.1 衰减案主, 批 2 目标覆盖) |
| T6 AE Example 2 具体数据 | AE | ✓ |
| T13 DM Example 1 数据表 | DM | ✓ |
| T14 EX 剂量调整 Example | EX | ✓ |

## 延到批 3 (E1 --tier others, exclude-list = 本 28 域)

所有 63 域减去本 28 = 剩余 35 域:
AG, CO, CV, DA, DV, EC, FT, HO, IE, MK, ML, NV, OE, PE, QS, RE, RELREC, RELSPEC, RELSUB, RP, SC, SM, SR, SUPPQUAL, SV, TA, TD, TE, TI, TM, TS, TV, UR, VS + (任何本阶段未入选的)

## 下一步

D2: `extract_examples_data.py --tier high --domain-list <this_file>` (或直接 hardcode 上表 28 域), 产出 `output_v2/09_examples_data_high.md` (target ≤30K, 硬上限 50K)
