# DM2 T8 attempt 1 — cdisc140 触发扫描 1/140 误触 (q29), 未提交

> 日期: 2026-09-15 / 单元: DM2 Task 8 (L2 零 LLM 闸: 触发扫描 + 零回归) / 判定: **BLOCKED, 不提交, 交 controller 裁**

## 1. 输入 (跑了什么)

`eval/prod_wirein/dm2_trigger_sweep.py`（新写, Step 1 产物, 未 commit）对三个题集逐题跑
`decide_dossier(question, "auto", True, lookup._query_domains)`，`lookup` 用
`StructuredLookup(settings.kb_root, MetaStore(settings.meta_path))` 构造 (仿 `server/rag.py:198`)。

```
.venv/bin/python eval/prod_wirein/dm2_trigger_sweep.py
```

## 2. 产物: 三行数字

```
cdisc140: 1/140 fired  ['q29']
study48: 0/51 fired  []
mapping8: 7/8 fired  ['dm01', 'dm02', 'dm03', 'dm04', 'dm05', 'dm06', 'dm07']
```

**Gate 判据 (brief §Step2): `cdisc140` 必须 `0/140`。实测 `1/140`，未过闸。**

## 3. 技术判定: q29 为什么误触

`eval/test_set_v3.yml` q29 (纯 CDISC 通论题，无 study/EDC 语境):

> "How do the four Trial Design domains TA (Trial Arms), TE (Trial Elements), TV (Trial Visits), and TI (Trial Inclusion/Exclusion) work together to define a study design?"

`_SCOPE_RE` (server/dossier_trigger.py) 命中位置与命中串:

```python
>>> _SCOPE_RE.search(q29_question)
<re.Match object; span=(12, 21), match='our Trial'>
```

命中的不是问句里任何"本研究"语境词，而是 **"f<our Trial>"** —— `_SCOPE_RE` 的
`our trial` 分支没有 `\b` 词边界，跨词边匹配到了 "f**our** **Trial**" (four 的词尾
"our" + 空格 + Trial) 里。`domains` 侧同题命中 TA/TE/TV/TI 四个域码 (非空)，
`domains and _SCOPE_RE.search(...)` 两个条件同时满足 → `attach=True`。

这是 fix round 1 收紧 "裸 EDC / in our" 时未覆盖到的**另一个**词边界漏洞：`our study` /
`our trial` / `this study` / `this trial` 四个英文分支都缺 `\b`，任何以
`...our`/`...our`-结尾单词 (four/endour/…) 紧跟 " study"/" trial" 都会误触发。
本题集内实测只有 q29 撞上 (140 题里唯一一处 "four Trial(s)" 搭配)，但这是**正则结构性
漏洞**，不是 q29 专属的黑名单可修问题。

## 4. 业务判定: 为什么不能自己动手修

Controller 决议明确: cdisc140 触发 > 0 时不许我自己碰正则，须归档本文件并把命中题号/
命中范围词报回，交 controller 裁。因此本 attempt 到 Step 2 为止，未跑 Step 3 (零回归复跑)
/ Step 4 (checkpoint + commit)。`eval/prod_wirein/dm2_trigger_sweep.py` 已写好且可跑
(逻辑与 brief 一致，仅按 controller 决议修正了 `StructuredLookup` 构造方式)，未改动
`server/dossier_trigger.py`。

## 5. 附带观察 (非本 attempt 的阻断条件, 供 controller 参考)

- **mapping8 7/8** (brief 期望 8/8): 缺的是 `dm08`
  ("Which of the data our study collects should be represented as Disease Response
  records?", domain=RS)。`_SCOPE_RE` 对该题**能**命中 "our study" (合法命中，非边界漏洞)，
  但 `lookup._query_domains(question)` 对该题返回 `[]` —— "Disease Response" 未被
  域名识别器映射到 RS，与 `_SCOPE_RE` 无关，是 D1/S3 长名匹配表的覆盖缺口。
- **study48 0/51**: 51 题 (48 计分 + 3 out_of_scope) 全部未触发 —— 没有一题同时满足
  "范围词命中" 与 "domains 非空" 两个条件。是否符合预期未定, brief 只要求"记 N 与题号"，
  未设下限；本 attempt 未进一步归因 (与 cdisc140 阻断问题无直接关系)。

## 6. 下一 attempt 输入 (若 controller 裁定收窄 `\b` 边界)

若 controller 认可"给 `our study|this study|our trial|this trial` 四个分支加 `\b` 词边界"
这类**词类级**收紧 (非针对 q29 字面的黑名单)，修法预期为:

```python
r"...|\bour study\b|\bthis study\b|\bour trial\b|\bthis trial\b|in (?:our|this) (?:study|trial|research)"
```

修后需重跑本脚本确认 `cdisc140: 0/140`，且**不能**引入新的漏检 (例如 "in our study" 分支
本身已用 `in (?:our|this) (?:study|trial|research)` 覆盖，不受 `\b` 影响)；随后重跑本文件
step 2 三行数字 + step 3 零回归 + step 4 checkpoint。
