# T2 dispatch notes (主控, B-PCPP 试点后的口径补充; writer/reviewer/auditor 都要读)
- RELOCATE 不在原处留指针; 只有 D2 重复副本去重才留一行交叉引用.
- census 用同一 bbox 解析器生成并自比 = 自证. reviewer 对新增/重建的表须用独立方法 (layout 列位置或渲染图) 复核.
- 居中/不可机检表 (NO_PDF / UNPARSEABLE / census 读串列): reviewer 必须对渲染图逐格人工核, 不采信 writer 的 "解析器读串列, KB 是对的".
- reviewer 读 KB 长行时不要截断显示 (cut/head -c), 防止把显示截断误判为内容截断 (B-PCPP reviewer 缺陷 3 即此误判).
- PDF_TYPO: KB 保留合理值, 登记 T-n; PDF 自身拼写错 (如 pre-corrdinating) KB 保留正确拼写.
- KB_AUTHORED (KB 自写, PDF 无对应): 与 PDF 矛盾 → D2 删扩写; 纯导航且不矛盾 → 保留并在 checkpoint 列出.
- 叙述段: 即使不在 atoms 里, 批内发现的 PDF 叙述缺失也补 (R3 全部纳入), checkpoint 记 "新增 atom 清单".
- 每个 agent 的 scratch 只用 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_<BATCH>_<role>/` (当前 session; 换 session 改此路径), 绝不写进仓库目录.
- 不 commit (主控按批 commit). 多批并行: 只改本批 kb_files, 不碰别批文件.

## 补充口径 (B-CP 后, 主控 2026-11-26)
- **PDF_TYPO 取舍规则**: 正确值能由 PDF 自身确定 (同行其他列、同表连续编号、spec/CT、叙述明确) → KB 写正确值并登记; 无法由 PDF 自身确定 → 照录 PDF 并登记为 T4 用户裁定项. 每条登记写明依据.
- **R2 插入后残留的旧改写句**: 若该行 fp_match 显示不承载其他 PRESENT/REWRITE_OK 原子 → 删除旧改写句 (D2 去重), 列入删除清单; 承载其他原子 → 保留, 记录原因.
- **KB 自写占位句** (如 "the table shows …" 而真表已补) → 删除 (D2 删扩写).
- **KB 自写附录 / 摘要与 PDF 内容重复** → 留 PDF 所属节那份, 附录处替换为一行交叉引用; 附录中与 PDF 矛盾的句子删除.
- **词替换型改写** (同义词替换, 无信息丢失): 该行不承载其他原子时恢复 PDF 原词; 承载时保留并登记.
- **表头大小写/拼写印刷错** (如 `ROW`): KB 用与同文件其他表一致的正确写法 (`Row`), 登记.
- **D6 (用户裁定)**: KB 自写且不与 PDF 矛盾的解释性内容 → 保留, 加前缀 `> KB note (not in SDTMIG):` (多行/表/图放进同一引用块, 或在其上方单独一行标注). 与 PDF 矛盾 → 删 (D2). reviewer 逐条确认.
- **跨文件重复例子** (如 EX/EC 同一组例子): 按 D2, 留 PDF 所属节那份并修对, 另一处一行交叉引用; 归属由 PDF 章节号判定.
- D6 范围: 只针对解释性内容. 纯导航 (标题/锚点/交叉引用/表前短标签如 `**CRF:**`) 不加 KB note 标注.
- D6 标注措辞: chapters/ 与 domains/ 用 `> KB note (not in SDTMIG):`; model/ (源为 SDTM v2.0) 用 `> KB note (not in SDTM v2.0):`.
- **reviewer 必做全扫 (B-ch04 auditor FAIL 教训)**: 叙述类批次, reviewer 须对本批 PDF 页做双向逐句扫描 (PDF 句→KB, KB 句→PDF), 不只核 writer 声明的改动; R2 丢失短语/URL/交叉引用 ("see Section …") 一律算缺.
- **终态必经 reviewer**: writer 在 reviewer PASS 之后的任何 KB 改动, 须回给 reviewer 复审 delta 后才派 auditor.
- **不截断输出**: 判 "无/没有" 之前的 grep/diff 输出不得用 head/cut/tail 截断 (B-PCPP 与 B-model01 reviewer 两次因此误判).
- **全扫必须含表格类原子 (B-ch04 a3 教训)**: 双向扫描要覆盖 TABLE_ROW / TABLE_HEADER / CODE_LITERAL, 不只叙述; census UNPARSEABLE 或无 Row 列的表 census 会漏报, 必须人工逐格对渲染; 反向扫描覆盖全文件, 不只改写过的段.
- **KB 自写的伪节号** (PDF 不存在的 4.2.1.1 等): 去掉节号; 内容不矛盾 → D6 标注保留, 矛盾 → 删.
- **PDF 图的 Mermaid 重绘**: 必须与 PDF 图逻辑一致 (分支/顺序), 并加 D6 标注 "rendering of PDF Figure …"; 不一致 → 按 PDF 改正.
- **域 spec 首句** ("xx.xpt, <Domain> — <Class>. One record per …"): 按 CM/IS 先例放在 `<XX>/assumptions.md` 的 Description/Overview 与 Assumptions 之间 (逐字); spec 表脚注属 spec.md. 各批遇到缺失即补 (O15/O16 全域扫描会兜底).
- **evidence 文件里引用 markdown 链接写法时一律用反引号包住** (否则 check_links 把它算成坏链, B-GF 曾使 live docs 42→45).
- **同文件内顺序/归节** 与 PDF 不一致 (段落挂错标题、属于下一小节): 允许在同一文件内按 PDF 顺序移位 (记 RELOCATE, 不留指针), 不需另授权.
- **抽样页范围**: 全量重写的批次, auditor 抽样 P 以该文件对应 PDF 的完整页范围为准 (不只 batch json 的 pdf_pages).
- **禁止 git stash / checkout / reset 等改动共享工作树的命令** (多批并行; 取基线用 `git show HEAD:<file>` 或 `git worktree`/临时副本). B-TE writer 曾 stash+pop, 已核其他批文件 md5 未受影响.

- **evidence 里 markdown 链接不要嵌套反引号** (B-TE review 嵌套反引号使链接暴露, live docs 42→44; 主控 eb13510 已修).
