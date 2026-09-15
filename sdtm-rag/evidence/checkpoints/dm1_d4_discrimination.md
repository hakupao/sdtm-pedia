# DM1 — D4 区分实验 (2026-09-15, HEAD 235526b; Task 10 前置)

> 问题: 映射 gold 的 study 侧候选卡 0/32 (dm1_gates.md), 到底是「问句→卡片语义鸿沟」还是「席位/切分/索引问题」? 两者对症药不同: 前者要人手表/别名桥, 后者要修检索层, 人手表不对症.
> 复跑: `.venv/bin/python eval/prod_wirein/dm1_d4_discriminate.py > data/study/st01/eval/runs/dm1_d4_discriminate.txt 2>&1` (产物 gitignored; 本文只放代称与合计).

## §0 判据 (跑前登记)

引擎 = 联邦里那台 study cards 引擎 (与 `repro_t5_study_expand.build` 同构, 扩写按 settings 实收 ON). 判 top-8. 四臂:

| 臂 | query | 量什么 |
|---|---|---|
| A body | 卡片正文 (去 frontmatter) | 卡片自身能否回来 → 索引/席位/切分健康度 |
| B title | 卡片标题行 (表单 label + 项目 label + 两个 OID) | 凭标识能否回来 |
| C label | 仅日文 表单 label + 项目 label, 无 OID | 用户自然说法能否回来 |
| D defn | 该域 `assumptions.md` 首段定义原文 | 管线现有原料 (D2 定义段) 到卡片有没有桥 |

裁定规则: A ≥ 90% 且 C ≥ 50% 且 D ≈ 0 → **语义鸿沟**; A < 90% → **席位/切分问题**.

## §1 结果 (24 张去重 gold 卡; dm01-03 同 gold 只算一次; D 按题 32 卡位)

| 臂 | 命中 top-8 | 平均名次 (miss 记 99) |
|---|---|---|
| A body | 24/24 = 100% | 3.0 |
| B title | 24/24 = 100% | 3.0 |
| C label | 23/24 = 96% | 1.5 |
| D defn | 2/32 = 6% | — |

- C 唯一 miss = I_OUTC (转帰卡, 名次 10): 项目 label 与表单 label 同词, 被同表单 73 张卡稀释.
- A/B 名次 3-8 而非 1 的原因是**同 OID 跨表单模板近重复** (同一 item 在若干表单各有一张卡, 正文只差表单名), 不是索引缺失. 例: I_RAND_DAT 自检第 8, 前 7 席全是 RCT 及其姊妹表单 (F_RAND2) 的兄弟卡; 一张 LB 检验项卡自检第 6, 前 5 席是同检验项在 RC/AE 表单的毒性/关联卡.
- D 臂 top-8 表单构成: DS 定义 → F_DISC 4 + F_REG 2 + AE 2 (表单对了, 卡不对: F_DISC 18 张卡里没挑中 gold 那张); DM 定义 → F_REG 4 + PF 3; AE 定义 → AE 8 (命中 1 张 gold); LB 定义 → F_DISC 3 + PF 3 (表单全错); PR 定义 → TME 4 + LB 2 (表单全错, OPE 1 张命中); RS 定义 → F_REG 4 (表单全错).

## §2 裁定

**语义鸿沟, 不是席位问题.** 卡片本身健康 (自检 100%), 用户用日文自然说法也 96% 一次命中; 缺的是「SDTM 域定义 (英文概念) ↔ EDC 日文表单/项目 label」这一步的桥, 管线现有原料 (定义段 / 域名扩写 label) 过不去 (6%). 人手表/别名桥是对症药; 继续调席位、切分、扩写强度都不对症 (T5 已证扩写 ON/OFF 无差, 本实验证明原因).

## §3 对路径 (a) 人手表的两条约束 (从数据推出, 供裁定用)

1. **粒度必须到 item, 不能只到表单.** 每表单 3 席 (S2 form_scopes 通道) 对大表单不够: gold 表单卡数 AE=175 / OC=73 / TME=68 / LB=46 / OPE=40 / F_REG=32 / F_DISC=18. 定义段→F_DISC 表单已进 4 席仍 0 gold 卡, 就是这个现象. 表若只写 form_oid, 候选卡仍进不来; 要么表写到 item_oid, 要么改 gold 为表单级判据 (RETRO §2 已提).
2. **同 OID 跨表单近重复要去重或标主表单.** 否则一张 gold 卡的席位会被兄弟卡吃掉 (A 臂名次 3-8 的成因).

## §4 未做 / 限制

- 只量 study 引擎单机, 未量联邦合并后席位 (CDISC 15 席吃满是另一问题, dm1_gates.md 已记).
- 未试「英文 SDTM 概念词 → 日文 label」的自动桥 (如用 catalog 里的英文字段说明若有); 那是路径 (a) 的替代方案, 属新设计单元.
