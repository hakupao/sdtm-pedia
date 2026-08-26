# 公开仓历史改写 — 真实标识符清除 (2026-08-26)

> 触发: `c1_redline_triage.md` §7 残留限制 ("只清理了当前 HEAD, 真值仍在公开仓历史 commit 中")
> 用户裁定: 改写历史清掉 + force push
> 红线: 本文件进 git, 只含形态/计数/路径, **零真值**

## 0. 结果

`main` **876ce4b → 9a13dd2** (force push 已完成)。全部 **7 个**真实标识符在
**930 个 commit / 6,927 个 blob / 全部提交信息**中归零; 两个 CJK label 的 bigram
残留 0 个 (无法重构)。**HEAD 树 `b0d039449bf1` 改写前后逐位相同** —— 只清历史, 内容零改动。

## 1. 清除范围 (逐条判定, 非照单全收)

**扫描面**: 全历史 12,280 个对象 / 6,927 个文本 blob + 930 条提交信息 + 两个 PR ref。
扫描器共报 **19 个 needle**, 逐条归类后**只清 7 个**:

| # | 形态 | 位置 | 判据 |
|---|---|---|---|
| 1 | LABEL len=11 | `test_ja_tokenize.py` | 唯一路径, 长日文 label |
| 2 | OID len=9 | plan 文档 + `test_docs_gold_gates.py` + **提交信息** | commit 自证"是 catalog 真实 item OID" |
| 3 | OID len=6 | `U1_RESUME.md` | 所在行写着"高危 form" |
| 4 | OID len=5 | `test_ja_tokenize.py` | 与 label 同行成对 |
| 5 | OID len=5 | `U1_RESUME.md` | 同 #3 |
| 6 | LABEL len=4 | `test_ja_tokenize.py` | 唯一路径 |
| 7 | OID len=4 | `U1_RESUME.md` | 同 #3 |

**其余 12 个判为撞车, 不清** —— 全部落在 `knowledge_base/`、`06_deep_verification/` 的
CDISC PDF 抽取 atoms、`release/`、`ai_platforms/` 等**公开 CDISC 内容**里。EDC 借用 SDTM
变量名/检查码命名条目是常态。**照单全清会毁掉公开知识库** —— 这是本次最大的误操作风险。

另有两个**已知为真但故意不清**: 一个 3 字符 form OID (同时是公开肿瘤学缩写, 3 字符全局
替换必然误伤); 一个 4 字符 OID (早在闸的 ALLOWLIST 里, 注明"用作直肠癌 MRI 通用判读用语")。

## 2. ⚠ 第一次改写失败并回滚 (必须记账)

**v1 改写后发现改坏了 19 个公开 CDISC 知识库文件**: needle#7 (4 字符 OID) 恰好是 CDISC
标准变量名 `SRGSTIND` (Surgically Sterile Indicator) 的**子串**, 被替换成
`SREDACTED_OID_07IND`。

**错因**: 做范围判定时用的是闸的**词边界**匹配 (`_bounded_contains`), 而
`git filter-repo --replace-text` 执行的是**裸子串**替换 —— **用边界感知的判据验证,
用不感知边界的工具执行**。

**处置**: 尚未推送, 从镜像备份**整仓回滚** (HEAD 与树逐位还原, 工作树 0 改动), 重做 v2/v3。

## 3. v3 的三条设计约束 (v1 教训直接转化)

1. **顺序无关**: 每条字面量互不重叠, 无论 filter-repo 以何顺序应用结果一致。
   (v2 曾想用整行字面量, 但同一行上有多个 needle —— 裸替换先命中就会让整行失配。)
2. **外溢者用带上下文的形态**: 实测 7 个 needle 里 **6 个零子串外溢** (裸替换安全),
   只有 needle#7 外溢 → 改用带反引号的形态 `` `X` `` (CDISC 文件里的 `SRGSTIND` 无反引号)。
3. **bigram 用最小上下文子串**: label 的 2 字符 bigram 若全局替换会改坏大量日文正文
   (实测一个片段出现在 **112 个路径**), 故只替换"只含片段、不含完整 needle"的括号列表子串。

## 4. 改写前的干跑 (v1 没做, 这是它失败的原因)

对 4 个目标路径的**全部 27 个历史版本**模拟应用替换表:
- 第一次干跑: **1 个版本仍可重构 label** → 补 1 条上下文字面量
- 第二次干跑: **27 个版本残留 0** ✅
- 对 v1 踩坏的 5 个样本文件模拟: **全部不变** ✅
- 对当前 main 树 **4,296 个文本文件**模拟: **0 个会被改动** ✅

## 5. 改写后验证 (本地 + 远端各一次)

| 项 | 本地 | 远端 (从 GitHub 重新 mirror clone) |
|---|---|---|
| needle #1-#6 全历史 | 0 处 | **0 处** |
| needle #7 **独立 token** | **0 处** (4 次裸子串全部嵌在 `SRGSTIND` 内) | 同左 |
| 全部 7 个在提交信息 | 0 处 | **0 处** |
| CJK label 可重构 bigram | 0 个 (需 ≥2) | — |
| HEAD 树 | `b0d039449bf1` 与改写前**逐位相同** | — |
| `pytest` | **1798 passed / 0 failed** | — |
| 红线闸默认面 | rc=0 CLEAN | — |

## 6. 做不到的部分 (force push 的边界, 不可回避)

1. **GitHub 仍保留改写前的孤儿对象** —— 旧 commit SHA 在一段时间内仍可经 URL/API 访问,
   直到 GitHub 侧 GC。**彻底清除需联系 GitHub Support 要求 purge**, 本轮未做。
2. **`refs/pull/1/head` 与 `refs/pull/2/head` 永久保留, force push 删不掉** ——
   本次运气好: 两个 PR 都是 2026-04 的 CDISC 知识库阶段, 早于任何 study 数据;
   扫描其全部 blob 的 9 个命中**逐条查证后全部是公开 CDISC 术语撞车**, 无真实标识符。
   **但这条限制本身要记住: 以后真有东西泄进 PR, force push 救不了。**
3. **已存在的 clone / fork 不受影响** —— 任何人此前克隆过的副本仍含旧历史。
4. **本地镜像备份仍含旧历史**: `~/MyProject/_sdtm_pedia_backup_20260826_224423.git` (68M)。
   它是本次的回滚保险, 确认无误后应由用户决定删除时机。

## 7. 复跑 / 回滚

```bash
# 远端侧验证 (从 GitHub 重新克隆后扫描)
git clone --mirror https://github.com/hakupao/sdtm-pedia.git /tmp/vc.git
# 然后用与本轮同一套 needle 池扫描 /tmp/vc.git 的全部 blob 与 commit message

# 整仓回滚 (若需要)
cd <repo> && git checkout --detach
git remote add _bk ~/MyProject/_sdtm_pedia_backup_20260826_224423.git
git fetch _bk '+refs/heads/*:refs/heads/*' --force
git fetch _bk '+refs/tags/*:refs/tags/*' --force
git checkout main   # HEAD 应回到 876ce4b, 树 b0d039449bf1
```
