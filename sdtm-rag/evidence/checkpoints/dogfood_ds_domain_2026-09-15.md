# Dogfood ⚑ 2026-09-15 13:27 · DS 域被缩窄成 F_DISC — 归因

> 状态: **归因完成, 未修** (2026-09-15). 触发: `dogfood_failures.md` 末条 (GPT-5.6 Sol, 三轮问答, 第一轮只给出 F_DISC.DSDECOD / I_DISC_RSN2 两个候选).

## 复现 (零 LLM, corpus 强制 both, 生产引擎)

```bash
cd sdtm-rag && .venv/bin/python eval/prod_wirein/repro_ds_domain.py 2>&1 | grep -E "^###|^\s+\[|study forms"
```
(第一轮原问句未落盘 — 服务端只记 flag 不记 ask; 用三句重构问句代替, 结论对问法敏感, 见下.)

## 实测 (top_k=15 → both 各 8 席, 共 24 chunk)

| 问句 | CDISC 侧 8 席 | study 侧 16 席 | DS 定义 (assumptions item_1) 是否进上下文 |
|---|---|---|---|
| 中文「哪些数据适合进入 SDTM 的 DS 域」 | S1 命名域直查占 4 席 = spec 变量行 DSDY/DSSCAT/DSSTDY/DSREFID; 余 4 席噪声 (ch04 4.5.8, supplementary「SDTM Version Response」×2, ch02 2.4) | F_DISC ×5, F_REG 排除标准 ×1, DM 噪声 ×2, 手順書 8 节 (9.1 EDC, 9.3 原資料, 13.3 個人情報 … 全是噪声) | **否** |
| 中文 + 写明「Disposition」+「PRT」 | 同上 4 席 S1 + assumptions item_1 + Example 1 | F_DISC ×5, PF ×2, F_REG ×1, 手順書 8 节 (含 5.2 登録の手順) | 是 |
| 日文「DSドメインに入るべきデータ」 | assumptions overview + item_1 + Example 1/2/4 | F_DISC ×1, F_REG ×2, DM/GN/LB 噪声 | 是 |

RCT.I_RAND_DAT (割付日 = RANDOMIZED 里程碑)、F_REG.I_REG_DAT (登録日)、OC.I_OUTC (転帰) 三张卡在三句里 **一次都没进**.

## 归因 (分层)

1. **检索 — CDISC 侧概念定义缺席 (主因)**. 中文短问句只带 token「DS」, S1 命名域通道确定性地把 DS spec.md 拉进来并按 query 向量在 spec 内选 4 行变量, 都是 Timing/Identifier 行, 没有一行讲「DS 收什么」. 讲这件事的 `domains/DS/assumptions.md item_1` (milestones + disposition of study participation / treatment, per epoch) 排不进余下 4 席; 余席被「SDTM」字面命中的 supplementary 版本应答章节挤掉. 与 (d) 通道 concept-definition 已知缺口 (q126) 同类, 这次是**域级**定义而非变量级.
2. **检索 — study 侧被 OID 前缀锚定**. 卡片正文里 DSDECOD / I_DISC_DAT / I_DISC_RSN2 等 OID 与「DS」字面/向量都近, 5/8 卡片席位落在 F_DISC; 真正的里程碑卡 (RCT 割付日 / F_REG 登録日 / OC 転帰) label 是纯日文, 与「DS」零字面重叠, 没有别名表条目 (`lookup_aliases.yml` 只有 放射線→F_PRERT), 进不来. 手順書 8 席全是 EDC/原資料/個人情報 等运营章节, 没有一节是治療中止規準或追跡.
3. **知识 — 语料里本来就没有 EDC→SDTM 映射文档** (federation rules 已声明), 所以「哪些数据进 DS」只能靠「DS 定义 × 各表单语义」推理. 前两层把定义和里程碑卡都截掉后, 上下文只剩「DS 变量行 + F_DISC 中止理由」, 模型据此得出「只有两个候选」是**对上下文忠实**的结果, 不是幻觉.
4. **护栏副作用**. 反捏造规则 (只从上下文取证 + 码闸 + 映射须标推測) 让模型不敢用参数知识补「DS 含 protocol milestone」; 第二/三轮之所以对, 是用户追问里出现了 F_DISC / DS / prt 三个词, 改变了检索 (对应上表第 2 行), assumptions item_1 才进来.

## 修法候选 (未做, 待裁)

- (a) S1 命名域通道: 命中域名时**保底带一段该域 assumptions 首条** (域级定义), 再填变量行. 最便宜, 确定性, 对「域收什么」类题直接补齐第 1 层.
- (b) study 侧: 别名表加「里程碑」类词 → F_REG/RCT/OC 表单 scope (登録/割付/転帰/追跡 → form), 或在 prompt 的 both 模式加规则句「域级映射题先从标准定义枚举事件类别, 再逐表单找状态/日期/理由字段」.
- (c) 服务端 `ask_stream` 落盘问句 (只记 question 前 100 字 + routed corpus), 否则下次 ⚑ 仍无法拿到第一轮原句复现.

裁定前不动代码. 修后需用本文件三句 + 用户原句 (待补) 复跑同一命令.
