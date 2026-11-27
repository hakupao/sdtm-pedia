# T4.3 发版记录 (推送 / 标签 / 网站核对)

<!-- chain: E (plans) -->
> 状态: **已完成** (2026-11-27T15:51:20Z; 本地日期 2026-11-28). 记录人 = 主控 (任务 `task_015df04443e6`). 本文件在标签之后的一个提交里: **main 比标签 `kb-2026.11.28` 多一个只含本记录与 trace 行的提交, KB 树相同**. 路径省略前缀 `.work/10_tier_b_repair/`.

## 1. 依据
- 主人对发版的同意 (经协调方待办项转达): 「直接发版，不用再问我」, 范围 = "这 1 条改完并复审通过" (`evidence/checkpoints/t4_owner_confirmation.md` "主人对发版的同意").
- 主人直接回答 「C1、D1、追认 M-10」 (同文件消息 5) → R4L 改 1 条 (`65d6a0f`; reviewer PASS + delta PASS) → 总闸角色 delta 闸审 **PASS** (`evidence/t4_gate_raw/attempt3_delta2_report.md`), 它列的 push 前须处理的 3 项已做 (`evidence/checkpoints/t4_gate_review.md` 文末).

## 2. 推送前检查 (在发版提交 `b2bd837` 上的最后一次; 原样)

```
range origin/main..HEAD = 7819398..b2bd837; commits 138; added lines 416742
BLOCKING  /Users/<name> or /home/<name> paths: 0
BLOCKING  personal patterns (from env, not stored): 0
BLOCKING  e-mail addresses other than the Co-Authored-By noreply address: 0
BLOCKING  private network addresses: 0
BLOCKING  key-shaped strings: 0
BLOCKING  password / secret / api key assignments: 0
REPORTED  "token": "..." assignments (text-token data fields): 31 lines; distinct values: 123-1001 2017-04-01 assessments assessments. biological\ birthdtc contained define-xml detailing document.additional idvarval informed laterallity pre-coordinating pre-corrdinating reactogencity reactogenicity received recieved replacement/ replacement/surgical repsonse tdtgtpai visitnum, 
BLOCKING  pdf / xlsx / source / pdf_pages / pdf_bbox files in the range: 0
BLOCKING  tracked files under pdf_pages / pdf_bbox / source: 0
BLOCKING  commits whose author or committer is not hakupao: 0
BLOCKING  author / committer e-mails not already public on origin/main: 0
REPORTED  machine paths without a user name: /Volumes/ 370 lines, /private/tmp 323 lines, files 366
REPORTED  Co-Authored-By trailers: 138 (noreply@anthropic.com )
RESULT: no blocking item
```

脚本之外另核的 (协调方列的三项之外, 主控加查):
- 两个远端推送前的状态 (`git ls-remote <url> refs/heads/main 'refs/tags/kb-*'`): GitHub 与 第二个远端 (自建 Gitea) 的 main 都是 `7819398` (= 本地 `origin/main`), 都只有 `kb-2026.11.25` → 快进推送, 两边一致.
- 138 个提交的说明文字: 用户目录路径 0 / 个人模式 0 / 内网地址 0 / 密钥样字符串 0 / 机器卷路径 0; 邮箱只有 `Co-Authored-By` 的 noreply 地址 (138 处).
- 变动文件名 1147 个: 个人模式 0; pdf / xlsx / 图片 / 压缩包后缀与 `pdf_pages` / `pdf_bbox` 目录 0 (唯一命中是脚本名 `scripts/t0_pdf_pages.py`, 不是 PDF 文本).
- 二进制文件 10 个, 都是 `evidence/failures/t3_attempt_{1,2,3}/` 下的 `.gz` (T3 失败归档的台账 / errata / 决策表压缩件); 解压后扫拦截模式 0、机器路径 0.
- 最大的新增文件 6.4 MB (台账及其三份改前备份), 远低于托管平台的单文件上限.
- **关于 PDF 原文**: 整页文本层 `work/pdf_pages/` 与词坐标 `work/pdf_bbox/` 在 `work/.gitignore` 里, 入库 0 个; `work/pdf_atoms.jsonl` 也被忽略 (它与远端早已公开的 `archive/deep_verification/pdf_atoms.jsonl` 逐字节相同). 脚本对 "PDF 文本" 只按路径名判. **如实说明**: 各轮审查的样本包 (`work/t4/**/…_pack_*.md`、`evidence/checkpoints/t4_human_sample.md` 等) 里带有逐条原子对应的 PDF 文本层短片段 (每条几行上下文), 这类内容与已公开的原子全文同类, 主控没有把它算作拦截项; 协调方若有不同意见, 这是事后可以处理的 (删文件 + 新提交), 但已推送的历史无法撤回.
- 本记录初稿里写了第二个远端的主机名, 被推送前检查的个人模式拦下 (主机名里含个人信息片段); 已改成 "第二个远端 (自建 Gitea)" 并修订这个尚未推送的提交后才推. 已推送的 138 个提交里没有这个主机名 (在 `b2bd837` 上个人模式计数 0).
- 不含用户名的机器路径 (卷路径 369 行 / 临时目录 322 行 / 366 个文件): 按协调方 2026-11-27 的裁定放行 (`evidence/checkpoints/t4_prepush_check.md` §2).

## 3. 推送
- 命令: `git push origin main` (origin 配两个 push URL; 没有 force).
- 结果: 两个远端都是 `7819398..b2bd837  main -> main`. 推送后逐个 `git ls-remote`: GitHub main = `b2bd8376e51e4d9e751fc49834a87a103a722b2e`; 第二个远端 (自建 Gitea) main = `b2bd8376e51e4d9e751fc49834a87a103a722b2e`.

## 4. 标签
- `kb-2026.11.28` (annotated; 打标签时本地时间 2026-11-28 00:49 JST; 同日没有别的 kb 标签, 不加 `.N`). 标签对象 `0f8a3e40c2b7c57c09649e9bd21f5a92fd94f0ff` → 提交 `b2bd8376e51e4d9e751fc49834a87a103a722b2e`.
- 标签说明写了: 范围; 过闸口径 99.2651% 与并列口径 (strict 95.5804% / mapped 99.3512% / 内容指标 90.6237%); 给下游的变更要点 (指向 `evidence/checkpoints/t4_downstream_notes.md`、两份标题变动清单 `work/t4/kb_heading_diff_kb-2026.11.25_HEAD.txt` / `kb_heading_diff_00a2e93_HEAD.txt`、PDF 笔误登记); 已知局限.
- `git rev-parse kb-2026.11.28:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a` (与发版前一致: R2L / R3L / R4L 三批与本次收尾都没有改 KB; 这个树哈希自 T4 解冻轮 `a59c2d3` 起没变过).
- 两个远端 `git ls-remote <url> refs/tags/kb-2026.11.28 'refs/tags/kb-2026.11.28^{}'`: 都是标签对象 `0f8a3e4…`, 解引用 `b2bd837…`.
- `git push origin refs/tags/kb-2026.11.28`: 两个远端都是 `* [new tag]`. 没有删除或改动任何已有标签 / 分支.

## 5. 网站 (Cloudflare Pages)
- 构建状态取自 GitHub 的 check-run (`gh api repos/hakupao/sdtm-pedia/commits/b2bd837…/check-runs`): `Cloudflare Pages | completed | success | Deployed successfully`, Latest commit `b2bd837`, 开始 2026-11-27T15:48:54Z, 结束 15:50:32Z; 预览地址 `https://731a8aac.sdtm-pedia.pages.dev`.
- `https://sdtm-pedia.pages.dev/` → 301 → `/zh/` 200 (标题 "SDTM 知识库"); `/en/` 200.
- 没有为让构建通过改任何代码; `web/` 在 `origin/main..HEAD` 里无改动.
- 本记录所在的提交推送后会再触发一次构建 (只多一个文档提交); 那一次的结果不在本文件里, 在主控给协调方的完成报告里.

## 6. 没做的 (按任务要求)
- 没改 `knowledge_base/`、`archive/`、`releases/`、`web/`; 没写 sdtm-rag 仓, 没替它做 "KB 更新" (协调方另派); 没有 force push; 没删远端的任何标签或分支.
- 待主人 (不挡): M-11 追认与 D1 的折行边界 — 已在聊天里告知 (`evidence/checkpoints/t4_owner_confirmation.md` "主控的第八次告知"), 截至本记录写入时未答.
