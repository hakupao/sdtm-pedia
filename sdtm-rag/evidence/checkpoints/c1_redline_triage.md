# C1 红线既有命中面 — 只读 triage (2026-08-26)

> 判定方 : 本轮 session (未参与 workflow 事件层任何 Task 实现/审查)
> 范围   : `oidscan_evidence.py` 对 `scripts/ server/` 的 32 处 LEAK 命中, 逐条判真/假阳性
> 性质   : 先只读评估 (§1-§4), 后按用户裁定清理 4 处真阳性 (§7) —— **未碰 git 历史,
>          未改仓库可见性**; 26 处假阳性一律未动
> 红线   : 全文零真名, 一律用 `<OID len=N>` / `<LABEL len=N>` + 用法形态指代

## 0. 一句话结论

**32 处里 28 处是假阳性 (87.5%), 4 处是真阳性且全部集中在 `scripts/tests/test_ja_tokenize.py`
一个文件的 6 行内。** 该 4 处已按用户裁定清理 (§7), 闸复测 32→26; 26 处假阳性未动。 但真阳性的**形态**比数量更值得注意: 其中一处是 **item OID 与其
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

## 7. 处置记录 (2026-08-26, 用户裁定「清理那 4 处」)

**改动面**: `sdtm-rag/scripts/tests/test_ja_tokenize.py` 单文件, 16 处字符串替换。

| 被替换 | 处数 | 替换为 | 说明 |
|---|---|---|---|
| 4 字符 CJK label | 4 | `偽項目名` | 等长同字符类 |
| 11 字符 CJK label | 1 | `偽ひらがなカタカナ漢字` | 等长, 保留 漢字/ひらがな/カタカナ 混排性质 |
| 5 字符 item OID | 1 | `FAKE5` | 等长; 沿用本仓 `_FAKE1`/`_UNUSED` 假名约定 |
| 派生 bigram 期望值 | 10 | 由假名重新推导 | **§2 的关键点**: 只换字面量不算清理 |

**两处语义保全 (不是顺手改, 是替换的必然后果)**:
1. `test_kana_and_kanji_in_same_run` 原断言取 bigram 下标 0/7/9; 换成假名后改取 **0/4/8**,
   即 `偽ひ` (漢字→ひらがな) / `なカ` (ひらがな→カタカナ) / `ナ漢` (カタカナ→漢字) ——
   三条**全部跨字种边界**, 比原下标更贴该测试 docstring 声明的意图 (「境界で切らない」)。
2. `test_bigrams_make_query_and_doc_share_tokens` 的 doc/query 交集来自尾部 `項目` 一词,
   不来自被替换的 label, 故替换不影响该断言 —— 已由测试实跑确认。

**实测 (可复跑)**:
```bash
cd sdtm-rag
./.venv/bin/python -m pytest -q --junitxml=/tmp/after.xml   # 1780 passed / 0 failed / 0 error / 0 skipped
./.venv/bin/python scripts/oidscan_evidence.py scripts server  # rc=1, LEAK 32 → 26
```
剩余 26 处 = §1 表中判定为假阳性的全部条目, 逐条未动。

**⚠ 残留限制 (必须诚实记录)**: 本次只清理了**当前 HEAD 的内容**。这 4 处真值仍存在于
公开仓的**历史 commit** 中 (`test_ja_tokenize.py` 自 2026-08-04 起的版本), 通过旧 commit
仍可访问。**彻底清除需要改写历史 + force push, 本轮按用户裁定未做。**

## 8. C2 前置: OID 池 min_len 判据 (2026-08-26, 用户裁定「先修闸的 OID 池判据」)

**问题** (§4-①): 闸对 `scripts/ server/` 的 26 处命中全部来自 **4 个** 2-3 字符 OID
needle, 无一真泄漏 (假阳性率 87.5%)。根因是 `load_needles` 缺 `min_len` 过滤 ——
`load_label_needles` 早有 `min_len=4` 且 docstring 写明理由, OID 池当初漏了这一手。

**为什么阈值取 4 而非 3**: 26 处里 **17 处**来自那个 len=2 needle, **9 处**来自三个
len=3 needle。`min_len=3` 只消掉 17 处, 闸仍是红的 —— 达不到"能接自动化"的目标。

**改动**:
1. `load_needles(..., min_len=DEFAULT_MIN_LEN)`, 新增模块常量 `DEFAULT_MIN_LEN = 4`,
   两个池共用 (原先 label 池的 4 是裸字面量)。
2. **剪除因此变成死代码的豁免条目**: `ALLOWLIST` **13 → 2**,
   `KNOWN_PUBLIC_COLLISIONS` **11 → 6** (needle 短于 min_len 者根本进不了池, 条目恒
   不触发)。本仓刚吃过同款亏 (Ruling C1: guard "原写法恒假是死代码")。
3. 既有测试的假 OID fixture 由 3 字符升到 ≥4 (`偽F1` → `偽FRM01` 等, 38 处)。
   **两处顺带加强, 不是顺着改**: `test_load_needles_excludes_given_set` 与
   `test_known_public_collisions_are_excluded_globally` 原本用 2-3 字符 token, 加了
   min_len 后会**因长度被剔除而通过**, 证不到 exclude 这条路径 —— 已改成必须挑
   ≥ min_len 的 token。

**新增 4 条测试 (TDD, 逐条先看红)**:

| 测试 | 看红方式 | 作用 |
|---|---|---|
| `test_load_needles_drops_values_shorter_than_min_len` | `TypeError: unexpected keyword 'min_len'` | 驱动本体改动 |
| `test_allowlist_entries_are_reachable_under_default_min_len` | 实测 11 条死条目 | 不许积累永不触发的豁免 |
| `test_known_public_collisions_are_reachable_under_default_min_len` | 实测 5 条死条目 | 同上 |
| `test_short_oid_paired_with_its_label_still_leaks_via_label_pool` | **立刻绿 ⇒ 改用变异验证** | 钉住"盲区有界" |

⚠ 最后一条写完**立刻通过** (它描述的是已有行为), 按 TDD 这不构成证据。改用变异实测:
**变异 A** (`needles_raw = oid_raw`, label 池不并入) → rc=1 红; **变异 B**
(`load_label_needles(min_len=8)`, 6 字标签漏掉) → rc=1 红; 还原 → rc=0 绿。
**两次变异都能杀死它 ⇒ 不是装饰闸。**

**另一条自查**: 元测试首版的断言失败信息会把 allowlist 的真实 needle 打进 CI 日志
(pytest 的 `assert dead == []` 会 repr 整个元组) —— 一条防红线的测试自己走了模块
docstring 点名的"绕道进日志"那条路。已改成 `路径:<len=N>` 掩码形状。

**盲区 (§7 之外的新增已知限制, 数字本轮实测)**: 原始去重非数字 OID **1071** 个中
**70 个 (6.5%)** 长度 <4, 有效 needle 池 **1060 → 997** (净减 63)。但**全盲远小于 70**
—— 用短 OID 的 70 条记录 (forms 13 + items 57) 里 **63 条自身名称仍在 label 池**,
成对泄漏由 label 侧抓到 (C1 那次真实泄漏正是这个形态)。**真正全盲 7 条**
(forms 5 + items 2): 短 OID 且自身名称也过短/被排除。**用户裁定接受。**

> 订正: 本轮早先口头估过"全盲 14 条", 那是只算 items 且漏了 `group_name`/`form_name`
> 也在 label 池里所致。以本节的 7 条为准。

**实测 (可复跑)**:
```bash
cd sdtm-rag
./.venv/bin/python -m pytest -q --junitxml=/tmp/t.xml   # 1780 → 1784 passed / 0 failed / 0 error / 0 skipped
./.venv/bin/python scripts/oidscan_evidence.py                  # 默认面 rc=0 CLEAN (205 文件)
./.venv/bin/python scripts/oidscan_evidence.py scripts server   # rc=0 CLEAN (333 文件) ← 本次目标, 原 rc=1 LEAK 26
```

**本单元不含** (仍是 C2 本体): 扩默认扫描面到源码、接 pre-commit / CI。本单元只是
把"接上去会长期红"这个阻塞解掉。

## 9. C2 本体: 闸接自动化 (2026-08-26)

**先破一个假选项**: "接成一条 pytest / 接 GitHub Actions" **结构上行不通** ——
needle 源 `data/study/st01/catalog.json` 是 gitignored 且**永远不能推**(它本身就是要
保护的东西), 所以 CI 里根本没有 needle 源, 闸只会 fail-closed ABORT。一条在干净检出
里永远 skip 的测试就是装饰闸, 正是本单元要治的病。**唯一可行的自动化是本地**。
(本仓现状实测: `.github/workflows` 不存在、无 pre-commit 框架、`.git/hooks/` 为空
—— C2 是从零建, 不是往现成管道上挂。)

**为什么 hook 只扫暂存文件**: 闸的匹配是 1638 个 needle 编进一条交替正则逐行跑,
实测 **62 ms/文件**; 默认面 542 文件要 **11.3 秒**。一个每次 commit 加 10+ 秒的 hook
迟早被 `--no-verify` 绕过 —— "纸面规则等于没规则"换个死法。暂存文件典型 1-5 个,
实测约 0.3 秒。

**交付**:

| 件 | 说明 |
|---|---|
| `sdtm-rag/scripts/precommit_oidscan.py` | 逻辑本体 (可测). 复用 `oidscan_evidence.main`, 不另写一套匹配/掩码, 免得 hook 与手跑两条路径悄悄分叉 |
| `.githooks/pre-commit` | 三行 shim (shell 难测, 故逻辑全在 Python 里) |
| `.githooks/install.sh` | 一次性 `git config core.hooksPath .githooks` |
| `DEFAULT_TARGETS` += `scripts/` `server/` | 手动全仓审计终于覆盖 C1 的暴露发生地 |

**四条行为 (各有先行失败测试, 共 6 条新测试)**:
1. 暂存项里的**已删除路径与二进制文件**先滤掉 —— 否则一次纯删除的提交会撞上闸的
   "0 个文件可扫"fail-closed 被误拦。
2. 过滤后为空 → **在调用闸之前**放行。
3. `catalog` 不在本机 → **拦下** (没 needle 源 = 没有任何保证, 与闸同纪律), 且必须
   **具名**告知逆转: `OIDSCAN_NO_CATALOG=1 git commit`。**不引导去用 `--no-verify`**
   —— 那会顺手关掉未来所有 hook, 且不留"我知道我在绕过什么"的痕迹。
4. `OIDSCAN_NO_CATALOG=1` → 放行但**响亮**打印"本次提交未经任何 OID/label 泄漏检查"。
   静默的逃生门用两次就变成默认路径。

**`core.hooksPath` 不随 clone 传播** (它写在 `.git/config`), 所以本 hook 的 fail-closed
只作用于**主动启用它的人**; 别人 clone 本公开仓不会因此无法提交。这条不是缺陷,
是选 `core.hooksPath` 而非 `.git/hooks/` 直写的附带好处 (后者还不受版本控制, 改坏无痕)。

**端到端实证 (不止测 Python 层)**:
```
A 干净路径 : 暂存 4 个文件 → hook rc=0, CLEAN, 瞬时
B 泄漏路径 : 程序化写入一个真 needle (len=23) 的探针文件并 git add -f
             → hook rc=1, 输出 `_e2e_leak_probe.md:1: <OID len=23>` (掩码, 未打真值)
C 真提交   : `git commit -m "THIS MUST BE BLOCKED"` → **rc=1, HEAD 未动**
             (证明 core.hooksPath 接线真的生效, 而非手动调了个脚本)
D 清除     : 探针 unstage + 删除; `git status` 无残留; 闸对全仓复扫 rc=0
```

**实测 (可复跑)**:
```bash
sh .githooks/install.sh                                  # 一次性启用
cd sdtm-rag
./.venv/bin/python -m pytest -q                          # 1784 → 1791 passed / 0 failed
./.venv/bin/python scripts/oidscan_evidence.py           # 默认面 rc=0 CLEAN (542 文件, 原 205)
```

**已知限制**:
- hook 只管**新进 git 的**文件; 存量面靠不带参数的手动全仓审计, 没有定期跑的强制力。
- 默认面仍不含 `knowledge_base/` `web/` `milestones/` `.work/` —— 本轮未评估这些树的
  必要性与耗时, 未扩。
- `OIDSCAN_NO_CATALOG=1` 与 `--no-verify` 都仍能绕过; 本设计只做到"绕过要具名且响亮",
  做不到"绕不过"。
