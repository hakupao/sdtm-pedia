# 路由准确率闸 (Plan B 闸 1) — 收口证据

> 状态: ⛔ **FAIL (条款 1)** · 最新数字见 **§6 (2026-08-31, Claude Opus 5)**。
> 闸脚本 `eval/run_routing_eval.py`。
> 本文件只含统计与题 id, **不含任何题面** (study 题面属临床数据, 红线)。
>
> ⚠ **状态沿革** (读 §2/§3 前必读): 本文件 §1-§5 是 **2026-08-04 Plan B 闸 1 的收口快照**
> (gold 181 题 · haiku · PASS)。此后:
> - **2026-08-17/18 U6**: gold 扩至 **254 题** (新增 dev/heldout/distractor_cdisc/
>   ambiguous_both/u1_doc/final 六组), 闸转 ⛔ **FAIL** (`fatal 8~9`, 要求 0);
>   用户裁定「保留信号层 + 按部分达成 FAIL 诚实收口」。证据: `doc_track_u6_routing_debt.md`。
> - **2026-08-31**: 换模型重跑 (见 §6)。**FAIL 状态自 U6 起延续至今, 非本次换模型引入。**
>
> ⇒ §2 的「181 题」与 §3 的 PASS 数字**均为历史**, 不是当前闸面貌。

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

both 组 5 题**全部**是映射/并列类: 每题都同时含 study 侧指代 (この項目 / このフォーム /
この試験) 与**显式的标准侧标记** (標準 / SDTM / コントロールターミノロジー)。
**无标准侧标记、只凭主题就该判 both 的"真两可"形态未覆盖** (见 §4.5)。

后两组是补盲区专用: 原 gold 里语言与语料一一对应 (cdisc 全英/study 全日) 且无 both 题,
任何"按语言判库"或"見到 項目 就判 study"的规则都无法被证伪。出题依据声明写在 yml 文件头。

## 3. 三遍结果 — 历史 (2026-08-04, Bedrock `jp.anthropic.claude-haiku-4-5`, temperature 0)

> 本节数字是 **`ja_supp_b03` 题面修正后重跑**的结果 (审阅 I-3: 原题面用了中文词
> 「受控術語」, 日语无此构词, 已改为「コントロールターミノロジー」), 与当前入库题面一致。
> 修正前后三遍数字恰好相同 (178/181, fatal=0), b03 两版均判 both。

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
3. **both 组与规则 3 线索词重合, 该方向不可证伪**: 5 道 both 题的题面都带着规则 3 的
   线索词 (対応 / マッピング / どの変数に…), 而 gold 里**没有一道含这些词但 gold ≠ both
   的负例** —— 例如「SDTMIG で --ORRES と --STRESC はどう対応しますか」这类纯标准题
   (含「対応」但正解是 cdisc)。也就是说, 现在无法区分路由器是**读懂了跨库需求**, 还是
   只是**见到线索词就判 both**。补一批这样的 cdisc 负例才能证伪, 本轮未做。
4. **闸对模型敏感**: 基线 prompt 在 Anthropic 直连与 Bedrock 上给出完全相同的 156/165,
   说明结果对通道不敏感; 但换模型 (或换 haiku 版本) 后判据表现无保证 —— **换模型必须重跑**。
   ✅ 该纪律已于 **2026-08-31 换 Opus 5 时执行** (§6); 结论: 判库质量升 (fatal 9→2),
   但**确定性丢失** —— 详见 §6.3。
5. **both 组只覆盖"带显式标准侧标记"的形态**: 5 题都同时含 study 指代与标准侧标记
   (標準 / SDTM / コントロールターミノロジー); **无标准侧标记、只凭主题就该判 both 的
   真两可形态未覆盖**, 留作后续。
6. **`_ROUTER_SYSTEM` 是被本闸把守的资产**: 改动那段 prompt 必须重跑
   `python -m eval.run_routing_eval --runs 3`, 三遍全 PASS 才算数。
7. **两道最脆的哨兵题**: `ja_supp_04` (「単位」既是标准概念也是 EDC 字段) 与
   `ja_supp_07` (不含任何标准构造词, 只靠「提出」定性)。判据一旦偏向 study 侧, 这两题最先掉。
8. 逐题明细写在 `data/study/st01/eval/runs/routing_run_N.json` (**gitignored**, 含题面, 不入库)。

## 5. 复跑方式

```bash
cd sdtm-rag
.venv/bin/python -m eval.run_routing_eval --runs 3 --signal-layer on   # 对齐生产的口径
.venv/bin/python -m eval.run_routing_eval --runs 3                     # 裸判库 (--signal-layer 默认 off)
# 退出码 0 = 三遍全过; 当前恒为 1 (条款 1 未过, 见 §6)
```

⚠ **`--signal-layer` 默认是 `off`, 而生产默认 ON** (`study_lookup_enabled` 为真即挂,
无 env 开关)。**不带该参数跑出来的数字不能用来描述生产判库**——2026-08-31 本节作者
第一次就跑错了这个口径。

gold **254 题** (非 §2 的 181)。耗时随 light 档模型走: haiku 约 5-8 分钟;
**Opus 5 实测 OFF ≈ 12 分钟/遍、ON ≈ 22 分钟/遍** (三遍 ON ≈ 66 分钟)。

## 6. 换模型重跑 — Claude Opus 5 (2026-08-31)

> 触发: light 档由 `bedrock/converse/jp.anthropic.claude-haiku-4-5-20251001-v1:0`
> 换为 `bedrock/converse/global.anthropic.claude-opus-5` (三档全线切, 用户裁定)。
> 依据 §4.4「换模型必须重跑」。git rev: `0479eba`(-dirty)。

### 6.1 三遍结果 (两个口径各三遍)

```
--signal-layer on   (对齐生产)
run 1: legacy 180/181  fatal_excl_final=2  fallback=0  FAIL(条款1)
run 2: legacy 181/181  fatal_excl_final=2  fallback=0  FAIL(条款1)
run 3: legacy 181/181  fatal_excl_final=2  fallback=0  FAIL(条款1)
stability: 250/254 题三遍判定一致       fatal ids (三遍相同): u3_amb_03, u3_dist_10

--signal-layer off  (裸判库)
run 1..3: legacy 181/181  fatal_excl_final=2  fallback=0  FAIL(条款1)
stability: 251/254 题三遍判定一致       fatal ids (三遍相同): u3_amb_03, u3_dist_10
```

### 6.2 与 U6 基线对照 (同为 signal-layer ON)

⚠ U6 文档有**两个口径**, 引用前必须分清: §2.1 冻结基线 = `--signal-layer off`
(`fatal_excl_final` **9**); §2.2 全闸 = `--signal-layer on` (`fatal` **8**)。
下表两列同为 **ON**, 故基线取 8。

| 指标 | U6 基线 haiku·**ON**<br>(2026-08-17/18 §2.2) | **Opus 5·ON**<br>(本次) | 变化 |
|---|---|---|---|
| `fatal_excl_final` | **8 / 8 / 8** | **2 / 2 / 2** | **↓ 6** |
| `legacy` exact | 179 / 179 / 179 | 180 / 181 / 181 | **↑** |
| `distractor_cdisc` exact | 7.0 (条款 4) | 8 / 8 / 6 | ↑ (含波动) |
| `heldout` exact | 11 / 12 (91.67%, 条款 2) | 12 / 12 | ↑ |
| `u1_doc` | 27·27·0 (条款 7) | 27·27·0 | = |
| 三遍稳定性 | **254 / 254** (条款 6) | **250 / 254** | ⚠ **↓** |
| `ambiguous_both` exact | — (§2.2 未列) | 4 / 6 | 不可比 |

**ON 口径 fatal 8 → 2**: U6 期 8 个 (`u3_amb_01..05` + `u3_dist_07/10/11`) 中的 6 个
在 Opus 5 下不再 fatal; **剩余 2 个三遍恒定**: `u3_amb_03`、`u3_dist_10`。
(OFF 口径则是 9 → 2, 差的那 1 个是 `u3_doc_02` —— 它在 haiku 时代已由信号层修好,
见 U6 §「三遍全修好 (1): u3_doc_02」。)

### 6.3 结论与代价

1. **闸仍 ⛔ FAIL, 但非本次引入**。条款 1 要求 `fatal=0`, 现为 2。FAIL 状态自 U6 起延续;
   本次换模型**把欠账砍掉大半** (ON 口径 8→2, OFF 口径 9→2), 方向是改善。
2. ⚠ **确定性永久丢失 (本次最重要的代价)**。haiku 时代 `temperature=0` 保证三遍
   254/254 逐题一致; **Opus 5 拒收采样参数** (400 `temperature is deprecated`) 且默认开
   adaptive thinking ⇒ 判库有固有抖动, 实测 ON 250/254、OFF 251/254 (3-4 题在遍次间摇摆)。
   ⇒ **本闸的数字自此不再逐位可复现, 引用任何单次数值都必须带「±3~4 题抖动」的限定**;
   把某一遍的 `legacy 181/181` 当成可复算基线是错的。
3. 判库延迟 haiku 0.72s → Opus 5 3.26s (同 prompt ×3 均值), 每题都付。
4. 口径纪律: 本次先跑错了 `--signal-layer off` (默认值) 才补跑 ON, 已在 §5 加警示。
