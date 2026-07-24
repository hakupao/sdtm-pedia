# RETROSPECTIVE — SP7 KG 查看器 UX 重构 (2026-07-24)

> 规则 C 强制三段。分支 `kg-viewer-ux-redesign` (e6f7fe1 → 9f253af); 9 build task + fit/visual/polish + final review READY WITH FOLLOW-UPS。

## 一、保留下来的做法 (what worked, keep doing)

1. **纯定位数学抽到 DOM-free 模块 + `node --test`**。把 `position*` 从渲染里分离成纯函数, 让"确定性/no-explode"这些最贵的正确性属性变成可红绿的单测 (15 例)。这是整条线的地基, 也让 layout 逻辑在后续视觉/打磨 task 里"不可能被误伤"(git log 佐证未被触碰)。
2. **垂直切片 + 物理回退共存**。先 overview 打通"确定性定位+补间"管线并保留其余视图的物理回退, 再逐视图接入, 最后一次性退役物理。每个 task 结束时 app 都可用, 每步都有可见产出。
3. **controller 脚本化断言 + 可见 banner**, 而非纯肉眼截图。把"已有节点是否移动"写成 JS 断言 (`EXISTING-MOVED=0 MAXΔ=0.00px`) 画进 banner 再截图 —— 数值证据比"看起来没动"强得多, 是 no-explode 的决定性验证。可复用技巧: 往生成的自包含 HTML 末尾注入 `<script>` 驱动内部状态 (classic script 顶层作用域共享)。
4. **规则 D 全程硬隔离**。每 task 写/审不同 subagent; final review 用异模型 (opus) 异 session 全分支审。审阅者屡次抓到写者+controller 都漏的真缺陷 (见下)。
5. **"生成物必须与源同步"当硬约束反复查**。每次 review 带一条 `regen → git diff --stat kg_viewer.html 必空` 的检查。

## 二、必须补上的缺口 (gaps / what to fix next time)

1. **生成物脱漏是本线最贵的坑, 且重复发生**。T8a fix 只提交了 `app.js`, 漏提交重新生成的 `kg_viewer.html` → HEAD 产物静默退回旧逻辑 (headless 却 PASS, 因测的是未提交工作区)。根因: subagent `git add <source>` 后忘记 `git add <generated>`。**教训**: 凡"改源→重生成"的仓库, 派单必须写死"`git add 源+产物` 且 commit 后 `git status --short` 必空并回贴"。后半程加了这条就没再犯。
2. **controller 自己写的 spec 也会有 bug, 且会被 sonnet 忠实实现**。fit-to-content 的 `freshView` 我给的是 `cur.v`-only, 漏了换域/换码 (M1 类); sticky 头公式漏了负 margin (双 padding); 整理/resize 漏重取景。**教训**: controller 给"确定性代码"时也要走查交互矩阵, 别指望 brief 字面正确 —— 审阅者(实测 29px vs 15px)和实现者(主动 flag coarse-key)都比 brief 更靠谱。
3. **视觉迭代对盲写 subagent 不友好**。8b 的像素级美学只能 controller 截图后驱动, subagent 看不到结果。以后视觉 task 应更早锁定"结构 CSS 给死值 + controller 迭代 hue/opacity"的分工, 别期望一次到位。
4. **密集图的标签可读性没有在 spec 阶段想清楚**。overview Findings=30 域的楔形注定重叠, "松包"会破 nearest-hub 不变量。这类"信息密度 vs 可读性"的取舍应在 brainstorm 就摆上桌, 而不是实现后才发现是设计选择。

## 三、关键决策复盘 (key decisions)

1. **布局范式 B (确定性+补间) 而非驯服物理 (A)**: 用户选"较大重构", B 是唯一能从根上消除"位置不可预测/一直在动"的方案。事后看完全正确 —— no-explode 变成一条可代数证明、可单测、可实测的硬不变量, 而力导向永远做不到。
2. **explore 锚定累积 而非重心 ego 导航**: 保留用户熟悉的"累积成网"语义, 只把"炸开"换成"已有节点锁死+新节点淡入"。手感连续, 且不变量干净 (target==prev)。
3. **源码拆分 `viewer/*` + build 内联**: 承 SP6 spec §8 预告。让 1523 行的重构可维护、可分文件审, 产物形态零变化。单遍 `re.sub` 内联(而非链式 replace)顺手消除了占位符级联损坏隐患。
4. **精密仪器取克制路线**: 信号色 amber 落在 8 类 CVD 色之外避免语义撞车; 网格极淡不抢戏。结果偏 refined 而非 bold —— 若用户要更鲜明的性格, 是可继续加强的已知方向。
5. **overview 密度问题选择"留给用户"而非盲改**: 判定它是设计选择(标签策略)而非缺陷, 记入 known-limit 并在收尾向用户呈选项, 避免在盲写模式下反复试错破坏不变量。
