# 路由准确率闸 (Plan B 闸 1) — 收口证据

> 状态: **PASS** (2026-08-04). 闸脚本 `eval/run_routing_eval.py`; 三遍全过退出码 0。
> 本文件只含统计与题 id, **不含任何题面** (study 题面属临床数据, 红线)。

## 1. 闸定义 (写死在代码里, 不可调)

| 项 | 值 |
|----|----|
| exact | `pred == gold` |
| fatal | `pred` 是单库且 `!= gold`, 或 `pred` 缺失 —— 该题 recall 归零 |
| both | 非 exact 但非 fatal (更宽, 证据仍可达) |
| PASS 条件 | **每一遍** `exact_acc >= 0.95` **且** `fatal == 0` |
| stability | 三遍逐题判定一致数 (观测值, 不设闸) |

`gold: both` 的题同样适用: 判 both = exact, 判任一单库 = fatal (单测钉住)。

## 2. gold 组成 (181 题)

| 子集 | n | gold | 来源 |
|------|---|------|------|
| 英文 CDISC 标准题 | 140 | cdisc | `eval/test_set_v3.yml` |
| 日文 study EDC 题 | 25 | study | `data/study/st01/eval/test_set_study_v1_1.yml` (剔除 `out_of_scope` 2 题; **不入库**) |
| 日文 CDISC 标准题 | 11 | cdisc | `eval/routing_gold_ja_supplement.yml` (`ja_supp_01..11`) |
| 日文 跨库/映射题 | 5 | both | `eval/routing_gold_ja_supplement.yml` (`ja_supp_b01..b05`) |

后两组是补盲区专用: 原 gold 里语言与语料一一对应 (cdisc 全英/study 全日) 且无 both 题,
任何"按语言判库"或"見到 項目 就判 study"的规则都无法被证伪。出题依据声明写在 yml 文件头。

## 3. 三遍结果 (Bedrock `jp.anthropic.claude-haiku-4-5`, temperature 0)

```
run 1: exact 178/181 = 98.3%  fatal=0  fallback=0  PASS
run 2: exact 178/181 = 98.3%  fatal=0  fallback=0  PASS
run 3: exact 178/181 = 98.3%  fatal=0  fallback=0  PASS
stability: 181/181 题三遍判定一致
```

逐子集分布 (三遍完全相同):

| 子集 | n | → cdisc | → study | → both | exact |
|------|---|---------|---------|--------|-------|
| 英文 cdisc | 140 | 139 | 0 | 1 | 139 |
| 日文 cdisc (`ja_supp_*`) | 11 | 11 | 0 | 0 | 11 |
| 日文 both (`ja_supp_b*`) | 5 | 0 | 0 | 5 | 5 |
| study (`st_*`) | 25 | 0 | 23 | 2 | 23 |

- **fatal = 0**, 无任何题落到错误的单库。
- **fallback = 0** (543 次调用零降级), 无降级数据充数。
- 3 题非 exact 均为安全侧 `both` (三遍相同): `q124`、`st_st01_v11_q17`、`st_st01_v11_q22`。

历史轨迹 (同一闸脚本, gold 逐轮扩充):

| 轮次 | gold | 结果 |
|------|------|------|
| Task 5 基线 prompt | 165 | 156/165 = 94.6% FAIL (差 1 题) |
| Task 5 终版 | 165 | 163/165 = 98.8% PASS |
| Task 5b (+11 日文 cdisc) | 176 | 174/176 = 98.9% PASS |
| Task 5c (+5 日文 both) | 181 | **178/181 = 98.3% PASS** |

## 4. 已知限制 (必须随闸一起读)

1. **调优集 == 闸集, 无 holdout**。prompt 判据是对着这 181 题调出来的, 三遍数字是
   **拟合后**的表现, 不是对新问题的泛化估计。真实泛化只能靠线上 dogfood 反馈继续观测。
2. **反向盲区未覆盖**: "英文提问本研究 EDC 字段" 这一类一道题都没有 —— 该方向的误判
   同样不可证伪。现实里 EDC 用户基本用日语提问, 故优先级低, 但记档为已知缺口。
3. **闸对模型敏感**: 基线 prompt 在 Anthropic 直连与 Bedrock 上给出完全相同的 156/165,
   说明结果对通道不敏感; 但换模型 (或换 haiku 版本) 后判据表现无保证 —— **换模型必须重跑**。
4. **`_ROUTER_SYSTEM` 是被本闸把守的资产**: 改动那段 prompt 必须重跑
   `python -m eval.run_routing_eval --runs 3`, 三遍全 PASS 才算数。
5. **两道最脆的哨兵题**: `ja_supp_04` (「単位」既是标准概念也是 EDC 字段) 与
   `ja_supp_07` (不含任何标准构造词, 只靠「提出」定性)。判据一旦偏向 study 侧, 这两题最先掉。
6. 逐题明细写在 `data/study/st01/eval/runs/routing_run_N.json` (**gitignored**, 含题面, 不入库)。

## 5. 复跑方式

```bash
cd sdtm-rag && .venv/bin/python -m eval.run_routing_eval --runs 3   # 退出码 0 = 三遍全过
```
约 181×3 ≈ 543 次 light 模型调用, 顺序执行约 5-8 分钟。
