# AGG 通道 — Rule A 独立抽检 N=6 (2026-07-07)

> Auditor: fresh general-purpose scientist lane (非实现/非审查 agent)。Ground truth 一律 raw `yaml.safe_load(data/meta/meta.yaml)` + 自写遍历 (零 server/ import); 注入观察与 ground-truth 推导为两条独立码路; e2e 评分用自写 fact_present 重算 (不 import analyze_kgval)。

## Verdict: AUDIT_PASS (6/6, 零事实错配)

| # | 样本 | 结果 |
|---|------|------|
| 1 | resolve("at least 18 different domains") 注入 | PASS — ≥18 → 8 var (STUDYID 63 / DOMAIN 59 / USUBJID 55 / EPOCH 44 / TAETORD 43 / VISIT·VISITDY·VISITNUM 36), 计数+集合完备性双向核 |
| 2 | resolve("twelve domains or more") 拼写数字 | PASS — "twelve"→12 归一正确 (≥12 语义, 非 ≥18 巧合: 独立核实 (12,35] 区间无变量) |
| 3 | resolve("top three codelists") | PASS — top-5 注入块 C66742(123)/C71620(58)/C66789(36)/C66728(26)/C74456(19), 名称/计数/贴现 tie-break (19 三平, 码升序) 全核 |
| 4 | resolve("single codelist ... greatest number") | PASS — 正确单最大 C66742 为首行事实; 恒注入 top-5 属声明的 recall-additive 设计, 非错配 |
| 5 | e2e ah01 评分 | PASS — 手工 set_recall 24/24=1.0 与存档一致; 定性: 回答含全表, 实质切题 |
| 6 | e2e as05 评分 | PASS — 手工 3/3=1.0 一致; 定性: 明确排名 3 codelists 带码+名+计数, 非碰词 |

## 结论

通道业务主张成立: 注入的全部是可对账的真事实, e2e 评分无虚高。无需纠正动作。
