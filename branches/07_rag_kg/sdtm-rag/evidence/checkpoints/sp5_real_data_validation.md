# SP5 缺口修正 — 真实数据验证 (CDISCPILOT01)

> 2026-07-09 · 缺口 #6 (无真实数据用合成 fixture) 修正。拿公开真实 SDTM study 跑三类检查,
> 实测误报率, 抓出并修一个真实假阳。数据源: **CDISCPILOT01** (CDISC 公开样本, phuse-org/phuse-scripts,
> `data/sdtm/cdiscpilot01/*.xpt`)。

## 方法

下载 9 个真实域 XPT (DM/AE/CM/DS/EX/LB/MH/SE/VS, 最大 LB 59580 行 / VS 29643 行), 经生产
`parse_bytes` → `run_graph_checks` (over meta.yaml GraphEngine)。全量域集合一次跑。

## 实测结果 (9 域全量, 首轮)

| rule | severity | 数量 | 判定 |
|------|----------|------|------|
| GIMPACT | INFO | 26 | 合理 (VISITNUM/VISIT/VISITDY 跨 36 域 + C66742/C71620 高 impact codelist) |
| GXDOM | WARN | 1 | **真阳**: AE RELREC-linked to PR, PR 不在提交集 (study 有 AE 无 PR, AE-PR 是真实 RELREC 关系) |
| GXDOM | INFO | 4 | 合理软提示 (AE→FA / CM→EC / EX→EC / LB→BS 缺席) |
| GCASCADE | WARN | 1 | **假阳** → 已修 (见下) |

## 抓出的真实假阳 → 修复

**C71620 (Unit) cascade 假阳**: CM 用 {%, CAPSULE, IU, mg, TABLET, ...剂量单位}, EX 用 {mg},
LB 用 {%, U/L, fL, GI/L, ...化验单位}。三域单位词表**合法地不相交** (量的是不同东西), 非嵌套 →
触发 WARN。这是**真实假阳**: 不同域用不同单位天经地义。

**根因**: C71620 是 **extensible=True** (830 词) 的开放式"杂货铺" codelist; C66742 (No Yes Response)
是 **extensible=False** (4 词) 闭合 codelist。开放式 codelist 跨域用不相交子集是设计使然, 非不一致。

**修复**: `check_ct_cascade` **跳过 extensible codelist** (`codelist(ct)["extensible"]` 为真则跳)。
只有闭合 codelist 有固定值域, 跨域发散才是真信号。单测 `test_ct_cascade_skips_extensible_codelist` 钉死。

## 复测 (9 域全量, 修后)

```
findings by (rule,severity): {('GIMPACT','INFO'): 26, ('GXDOM','WARN'): 1, ('GXDOM','INFO'): 4}
GCASCADE WARN: NONE (FP eliminated)
GXDOM WARN: AE RELREC-linked to PR (真阳, PR 确实缺席)
```

**真实全量 study 上 0 个假阳 WARN。** 唯一 WARN (AE→PR) 是真实完整性缺口。

## 残余限制 (诚实披露)

**CT cascade 是三类检查里最弱的一类**, 即使 extensible-skip + 非嵌套发散后仍有两类固有弱点:
1. **样本敏感**: 6 行小样本上 C66742 出现 AE={N} / LB={Y} → 触发 WARN, 但全量数据两域都有 Y 和 N →
   不触发 (全量实测已证)。小样本值域不全会假阳。
2. **多变量共享 codelist**: C66742 被 AESER/MHPRESP/DTHFL/LB flags 等**语义无关**变量共用, 它们各自独立
   取 Y/N, 值集本无理由跨域一致。cascade 假设"共享 codelist ⇒ 跨域值应一致"对这类 grab-bag codelist 不成立。

这与 KG 价值 eval 结论一致 (图层对精度贡献≈0); cascade 的价值在"跨域值覆盖观察"而非可靠缺陷告警,
保留 WARN 但 extensible-skip 去掉了最大一类假阳。若未来 dogfood 显示 cascade 噪声仍高, 候选降级为 INFO。

## committed 产物 (durable 回归护栏)

- **真实样本 fixture** `scripts/tests/fixtures/sp5_real_sample/{ae,cm,ex,lb,dm}.csv` (每域 6 行真实
  CDISCPILOT01 数据, 真实列/值, 全 <2KB git-friendly)。
- **集成测试** `scripts/tests/test_graph_validator_real.py` (3 测试): 真实 SDTM 形状不崩 + advisory-only /
  extensible Unit codelist 不被 cascade flag (假阳修复护栏) / RELREC 完整性对缺席 PR 触发 WARN。
- 大 XPT 原始文件不入库 (只留派生小样本 + 实测记录)。
