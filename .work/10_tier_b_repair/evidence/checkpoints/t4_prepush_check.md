# T4.3 推送前检查 (push 之前; 只读)

<!-- chain: E (plans) -->
> 状态: **最终一次已跑, 无拦截项** (见 §4); 下面 §3 是预跑 (2026-11-27T14:30:33Z; HEAD `734b91e` 时). 真正 push 之前在最终 HEAD 上重跑一次, 输出追加在文末 "§3 最终一次". 路径省略前缀 `.work/10_tier_b_repair/`.
> 检查对象 = `git push origin main` 会公开的东西: `origin/main..HEAD` 的新增行 + 提交元数据.

## 1. 怎么查 (可复跑)

```
PREPUSH_PERSONAL='<用户名|姓名片段|邮箱本地部分>' bash .work/10_tier_b_repair/scripts/t4/t4_prepush_check.sh
```

- 个人模式 (用户名 / 姓名 / 邮箱本地部分) **不写进仓库**, 运行时用环境变量传入; 本次用的是本机登录名、它去掉姓氏后缀的片段、git 提交邮箱的本地部分, 共 3 个.
- 任何一项 "BLOCKING" 计数非 0 → 脚本退出码 1 → 不 push, 停下来汇报.

## 2. 口径 (谁定的)

- 协调方在任务 `task_015df04443e6` 里列的检查项: 新增内容里没有本机绝对路径、邮箱或真实姓名; `work/pdf_pages/` 等原始 PDF 文本没有入库; 提交作者都是 hakupao.
- 主控预跑时发现: 新增行里用户目录类路径 0、邮箱 0、个人模式 0, 但有约 680 行**不含用户名的机器路径** (卷路径 `/Volumes/DevSSD/Project/…` 364 行, 临时目录 `/private/tmp/claude-501/…` 319 行, 分布在 363 个文件里; 基本都在 `88e1918` 及之前的提交: 变异日志、各批 checkpoint、派发 prompt、脚本里的 ROOT 常量). 这与协调方先前说的 "到 `88e1918` 为止查过是 0" 对不上, 主控向协调方提问 (消息 `msg_a963916e81e9`), 回答之前不 push.
- **协调方 2026-11-27 的裁定 (决定人 = 协调方; 回复 `msg_c4a777a2918b`)**: 口径定为 (a) — 这类不含用户名的机器路径**不算不干净, 按现状推**; 不改历史, 不批量改这些文件. 协调方同时更正: 它先前那句 "查过是 0" 不准确 (当时只查了用户目录路径、邮箱和真实姓名, 没把卷路径和临时目录路径算进去); 它自己复核的数字与主控一致, 并说会把这个更正告诉主人; 主人若在 push 之前对这些路径有不同意见, 它会转告, 届时停在 push 之前.
- 协调方给的理由 (照录要点): 这些路径不含用户名、邮箱、姓名、内网地址或密钥, 只有卷名、项目目录名、uid 和会话 uuid; 远端 main 上早已公开了更具标识性的同类内容; 这次要推的比已公开的更不敏感.
- **仍然算不干净、要停下来的** (协调方原列): 新增内容里出现用户名、邮箱、真实姓名、内网地址、密钥或口令样的字符串, 或原始 PDF 文本、pdf / xlsx 文件被纳入版本库.
- 后续 (协调方要求): 以后新写的证据和脚本尽量用仓库相对路径 → 写进 RETROSPECTIVE "必须补上的缺口".

## 3. 预跑输出 (2026-11-27T14:30:33Z; 原样)

```
range origin/main..HEAD = 7819398..734b91e; commits 129; added lines 402785
BLOCKING  /Users/<name> or /home/<name> paths: 0
BLOCKING  personal patterns (from env, not stored): 0
BLOCKING  e-mail addresses (except noreply@anthropic.com): 0
          (of which not noreply@anthropic.com: 0)
BLOCKING  private network addresses: 0
BLOCKING  key-shaped strings: 0
BLOCKING  password / secret / api key assignments: 0
REPORTED  "token": "..." assignments (text-token data fields): 31 lines; distinct values: 123-1001 2017-04-01 assessments assessments. biological\ birthdtc contained define-xml detailing document.additional idvarval informed laterallity pre-coordinating pre-corrdinating reactogencity reactogenicity received recieved replacement/ replacement/surgical repsonse tdtgtpai visitnum, 
BLOCKING  pdf / xlsx / source / pdf_pages / pdf_bbox files in the range: 0
BLOCKING  tracked files under pdf_pages / pdf_bbox / source: 0
BLOCKING  commits whose author or committer is not hakupao: 0
BLOCKING  author / committer e-mails not already public on origin/main: 0
REPORTED  machine paths without a user name: /Volumes/ 364 lines, /private/tmp 319 lines, files 363
REPORTED  Co-Authored-By trailers: 129 (noreply@anthropic.com )
RESULT: no blocking item
```

- 说明: `"token": "…"` 那 31 行是本项目数据文件里的文本 token 字段 (PDF / KB 行里的词, 值已全部列在上面), 不是凭据; 脚本只列出不拦.
- 提交邮箱: 129 个待推提交的作者 / 提交者邮箱与远端 main 上已公开的提交相同 (脚本比较的是两边的邮箱集合, 新出现的 0 个).

## 4. 最终一次 (2026-11-27T15:45:57Z; 在收尾提交 `4e70f9f` 上; 原样)

```
range origin/main..HEAD = 7819398..4e70f9f; commits 137; added lines 416717
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
REPORTED  machine paths without a user name: /Volumes/ 369 lines, /private/tmp 322 lines, files 366
REPORTED  Co-Authored-By trailers: 137 (noreply@anthropic.com )
RESULT: no blocking item
```

- 结论: 拦截项 0 → 可以 push. 不含用户名的机器路径 369 + 322 行 / 366 个文件, 按 §2 协调方的裁定放行 (比预跑多出的几行来自预跑之后的提交: 重生成的总闸预跑日志、引用这两类路径前缀的审查记录与本文件).
- 本文件这一节提交后 HEAD 会再前进一个提交 (只含本节、`RETROSPECTIVE.md` 的一处数字更正与 trace 行); 提交后主控又跑了一次同一命令确认结果仍是 "no blocking item", 那次输出记在 `evidence/checkpoints/t4_release.md`.
- 另核 (命令在 `t4_release.md`): `git status --short` 为空; `git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`; `origin/main..HEAD` 对 `archive/`、`releases/`、`web/` 无改动; `python3 tools/check_links.py` live docs = 42.
