# C1 红线既有命中面 — 只读 triage (2026-08-26)

> 判定方 : 本轮 session (未参与 workflow 事件层任何 Task 实现/审查)
> 范围   : `oidscan_evidence.py` 对 `scripts/ server/` 的 32 处 LEAK 命中, 逐条判真/假阳性
> 性质   : **只读评估, 本轮零改动** —— 未改任何命中文件, 未碰 git 历史, 未改仓库可见性
> 红线   : 全文零真名, 一律用 `<OID len=N>` / `<LABEL len=N>` + 用法形态指代

## 0. 一句话结论

**32 处里 28 处是假阳性 (87.5%), 4 处是真阳性且全部集中在 `scripts/tests/test_ja_tokenize.py`
一个文件的 6 行内。** 但真阳性的**形态**比数量更值得注意: 其中一处是 **item OID 与其
label 成对出现在同一行**, 另一处的 label 真值可由断言的 bigram 期望值**完整重构** ——
把字面量换成假名并不能消除它。

## 1. 逐类判定

| 类 | 处数 | 文件 | 判定 | 依据 |
|---|---|---|---|---|
| 模板占位符 | 2 | `scripts/build_kg_viewer.py` | **假阳性** | `__STYLE__` / `__<OID len=3>__` 形态的 build 模板占位符, 3 字符大写词与某 item_oid 撞车 |
| Python 变量名 | 2 | `scripts/build_meta.py` | **假阳性** | `_<OID len=2>_HEADING_RE` 正则变量名, 2 字符前缀撞车 |
| 公开示例数据 | 6 | `scripts/tests/fixtures/sp5_real_sample/lb.csv` | **假阳性** | 该 fixture 是 **CDISC SDTM Pilot 公开示例数据集** (`CDISCPILOT01`), 命中值处于 `LBTESTCD` 列且紧邻 `Albumin`/`CHEMISTRY`, 属 CDISC 公开受控术语 |
| 刻意假名 fixture | 16 | `scripts/tests/study_fixtures.py` · `test_build_catalog.py` · `test_parse_config_report.py` | **假阳性** | 全部形如 `<OID len=2>_FAKE1` / `<OID len=2>_UNUSED`, 周边取值是「偽選択肢」「未参照リスト」; 2 字符前缀撞上某 item_oid |
| SDTM 标准变量名列表 | 1 | `server/routing_signals.py` | **假阳性** | 命中值处于 `SER/SEV/SHOSP/SINTV/SLIFE/SMIE/…/SOD/SPCCND/SPCUFL` 序列中, 且同行有 `<OID len=3>CD` 配对, 属 CDISC 公开变量名 |
| **真实 label / OID** | **4** | **`scripts/tests/test_ja_tokenize.py`** | **真阳性** | 见 §2 |

## 2. 4 处真阳性 (全在 `test_ja_tokenize.py`)

| 行 | 形态 | 严重度 | 说明 |
|---|---|---|---|
| :49 | `<LABEL len=11>` CJK | **高** | 11 字符日文 label, catalog `items[].label` 单条覆盖; 长度足以唯一识别 |
| :85 | `<LABEL len=4>` + `<OID len=5>` **同行成对** | **高** | 形如 `# <LABEL len=4> (<OID len=5>)` —— 把一个真实 item OID 与它的真实 label **绑定**在一起, 是识别性最强的形态 |
| :33 | `<LABEL len=4>` CJK | 低 | 通用临床词汇 (与 :85 同值); 单独看属常见术语, 但与 :85 的 OID 配对后升级 |
| :57 / :94 | `<LABEL len=4>` CJK | 低 | 同上, 作为查询串出现 |

⚠ **一条不能忽略的性质**: :33 的断言把该 label 的 **bigram 切分期望值逐个列出**
(`== ["…", "…", "…"]`)。即使把字面量替换成假名, 期望值数组仍可**无损重构**原值。
⇒ 任何后续清理必须**连断言期望值一起改**, 只换字面量等于没改。

## 3. 暴露状态 (事实陈述, 非判断)

- 仓库 `hakupao/sdtm-pedia` 为 **PUBLIC** (`gh repo view` → `"visibility":"PUBLIC"`)。
- `test_ja_tokenize.py` 当前内容与 `origin/main` **字节级一致**, 该文件最后推送 **2026-08-04**。
- 故上述 4 处至迟自 2026-08-04 起处于公开可访问状态 (更早的历史版本未在本轮核查范围内)。

## 4. 对后续单元的两条影响

**① C2 (闸接自动化) 有一个必须先做的前置。**
本次假阳性率 **87.5% (28/32)**, 根因是 **OID 池没有 `min_len` 过滤** (闸自己记的 deferred:
`min_len` 只作用于 label 池)。2-3 字符 OID 与模板占位符 / 变量名 / 大写缩写大量撞车。
若在此状态下把闸接进 pre-commit 或 CI, 它会**长期红着**, 结果必然是被人为忽略 ——
这是"纸面规则等于没规则"的另一种死法。
⇒ C2 应先给 OID 池加 `min_len` (或改成"命中须处于标识符位置"的上下文判据), 再谈自动化。

**② `sp5_real_sample/` 目录名是误导性命名。**
它装的是 CDISC 公开 Pilot 示例数据, 不是客户真实数据, 但名字里的 `real_sample` 会让
任何后来者 (含扫描闸的复核人) 默认它是敏感的。建议后续重命名为 `cdisc_pilot_sample/`。
本轮**未改**。

## 5. 复跑命令

```bash
# 闸本身 (rc=1 = 有未在 allowlist 的命中)
cd sdtm-rag && ./.venv/bin/python scripts/oidscan_evidence.py scripts server

# 本次 triage 用的掩码脚本 (临时脚本, 未进版本库; 逻辑 = 复用闸的 needle 池 +
# 打印命中所在行并把命中子串替换成 <OID len=N>/<LABEL len=N>)
# 重建方式: import oidscan_evidence, 用 load_needles/load_label_needles/
#           compile_needle_pattern 三个函数 + ALLOWLIST 过滤, 逐文件逐行 finditer
```

**本报告零真名, 已程序化自证** (见 §6)。

## 6. 自扫

```
$ ./.venv/bin/python scripts/oidscan_evidence.py evidence/checkpoints/c1_redline_triage.md
```
实测 **rc=0 · `CLEAN: 0 处未在 allowlist 的 OID/label 命中 (1 个文件)`** (2026-08-26)。
