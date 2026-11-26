# T2 B-EC auditor (Rule A) — attempt 1
> agent: oh-my-claudecode:verifier (opus); 2026-11-26; 不读 writer/reviewer 结论先独立判, 判后对照. KB 未改.

## 抽样
- 命令: t2_auditor_v1.0 脚本, 唯一改动 `pages = range(107,120)` (全量重写规则: EC §6.1.3.2 p107-110 + 共享 §6.1.3.3 p111-119); scratch `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-EC_auditor/sample.json`
- seed 20261126; C=0, P=96, N=10 (全部取自 P−C)
- 判法: 原子 verbatim 归一化后在 EC/EX KB 行内子串匹配 + 标题定位 + PDF 原页文本核

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0115_a010 | p115 Ex5 "Rows 1-2: 20 mg drug X arm" | EX/examples.md:207 | 否 | 是 | Ex5 | 逐字 |
| 2 | ig34_p0114_a003 | p114 Ex4 EX 以 mg 收集, 无需 EC | EX/examples.md:152 | 否 | 是 | Ex4 | 逐字 (EC 旧副本缺 Ex4) |
| 3 | ig34_p0107_a005 | p107 EX 假设 --DOSTOT 弃用评估 | EX/assumptions.md:31 | 否 | 是 | EX 假设 | 范围外文件, 存在 |
| 4 | ig34_p0118_a019 | p118 Ex7 实际剂量 mL+mg/mL | EX/examples.md:362 | 否 | 是 | Ex7 | 与 Rows 2,4 同行, 逐字 |
| 5 | ig34_p0119_a005 | p119 Ex7 补 VS 体重记录说明 | EX/examples.md:390 | 否 | 是 | Ex7 | 逐字 |
| 6 | ig34_p0109_a012 | p109 EC 假设 1 首句 | EC/assumptions.md:13 | 否 | 是 | EC – Assumptions | 逐字 |
| 7 | ig34_p0111_a015 | p111 Ex1 Row 3 ECOCCUR="N"/ECREASOC | EX/examples.md:29 | 否 | 是 | Ex1 | 逐字 |
| 8 | ig34_p0112_a024 | p112 Ex2 mL 及部位在 EC | EX/examples.md:82 | 否 | 是 | Ex2 | 逐字 |
| 9 | ig34_p0118_a021 | p118 Ex7 Row 6 ECREASOC/ECDOSE null | EX/examples.md:364 | 否 | 是 | Ex7 | 逐字 |
| 10 | ig34_p0110_a010 | p110 EC 假设 5a 时间变量按收集区间 | EC/assumptions.md:35 | 否 | 是 | 5. Timing variables | 逐字 |

**独有丢失 0; 忠实度错误 0.**

## EC/assumptions.md 补充全查
- p109-110 EC 节 prose 原子 26 个: 25 逐字在 EC/assumptions.md; 唯一 MISS = ig34_p0109_a010 (spec 表脚注 "asterisk … controlled terminology", 属 spec.md, 范围外, 不计).
- 新增 Description/Overview 与 Specification 首句: 对 p107:16-20 逐字一致 (含 "per mood, Tabulation."), 位置 = Description/Overview 与 Assumptions 之间 (符合 CM/IS 先例).

## 删除的 EC-only 行 (D2) 抽 10/24
- 独立复算: f22fe60 EC/examples.md 非空行 strip 后不在现 EX/examples.md 行集 = 24 行 (与 reviewer 一致). seed 20261126 抽 10.

| EC 旧行 | 类别 | PDF 依据 | EX 正确版 |
|---|---|---|---|
| :3 "Note: … See also EX Examples" | KB 自写导航 | — | 由 EC 现一行 xref 替代 |
| :32 Ex2 表头缺 VISITNUM | EC 错 | p112:28 表头 "…ECLAT VISITNUM VISIT EPOCH…" | EX:86 |
| :40 Ex3 首段截断 (缺 "The subject … took:" + 4 条列表) | EC 截断 | p113:8-9 | EX:111-116 |
| :87 Ex6 Row 2 ECDOSFRM=CAPSULE | EC 错 | p116:14 "TABLET, TABLET, COATED" | EX:266 |
| :88 Ex6 "3-12 …" 省略行 | KB 自写占位 | p116-117 逐行完整 | EX:267 起 |
| :102 Ex7 Rows 2,4 截断 (缺实际剂量说明句) | EC 截断 | p118:21 | EX:362 |
| :108 Ex7 表头 EPOCH 在 VISITNUM 前 | EC 错 | p118:24 "ECADJ VISITNUM VISIT EPOCH" | EX:369 前后表头 |
| :111 / :112 / :114 Ex7 Row 2/3/5 EPOCH="VISIT TREATMENT" | EC 错 (PDF 折行 VISIT\n1 被拼进 EPOCH) | p118:25-36 VISITNUM n, VISIT "VISIT n", EPOCH TREATMENT | EX:371/372/374 |

→ 10/10 均为 EC 错/截断/KB 自写, 正确版本全部在 EX/examples.md; 无 PDF 有而 EX 缺的内容.

## 交叉引用 / EX 改动
- EC/examples.md:3 `../EX/examples.md` → 文件存在; 文本 "§6.1.3.3 … Examples 1-8" 与 PDF 节名一致.
- EX/examples.md diff 仅 1 hunk (:3 KB note 改为 "EC/examples.md points here", 去掉回指链接, 无反向循环); 其余 0 改动.
- `python3 tools/check_links.py`: knowledge_base/domains/E[CX]/ 坏链 0; live docs 42 (= 基线).

## G-TB8
- trace: writer executor ×2 (03:27:55Z, 03:30:22Z 续), reviewer code-reviewer PASS 03:34:09Z; 无 agent:main 写 KB.
- mtime (JST): EC/examples 12:27:14, EC/assumptions 12:29:18, EX/examples 12:29:26 = 03:27-03:29Z, 均早于 reviewer PASS → reviewer PASS 后无 writer 改动.

## 判定: **PASS** (丢失 0 / 忠实 0)
