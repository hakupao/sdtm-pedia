# Checkpoint — KG 查看器 UX 重构 (SP7)

> 状态: **DONE, READY WITH FOLLOW-UPS** (2026-07-24)
> 分支: `kg-viewer-ux-redesign` (base `e6f7fe1` → head `9f253af`)
> Spec: `docs/superpowers/specs/2026-07-24-kg-viewer-ux-redesign-design.md`
> Plan: `docs/superpowers/plans/2026-07-24-kg-viewer-ux-redesign.md`
> 执行: subagit-driven-development (每 task: executor 写 → 独立 subagent 审 = 规则 D 隔离; controller 做浏览器实证)

## 1. 做了什么

把 `kg_viewer.html`(由 `build_kg_viewer.py` 内联 `viewer/{template.html,style.css,layout.mjs,app.js}` 生成)从**力导向物理 + 每次交互全量重排**重构为**每视图确定性布局 + 缓动补间 + 无常驻物理**,并加"精密仪器"视觉系统。根治用户抱怨"点一下到处飞到处弹"。

- 源码拆分: 单文件 `TEMPLATE` → `viewer/*` 四文件, build 时单遍 `re.sub` 内联 (产物仍零依赖离线单 HTML)。
- 纯定位模块 `layout.mjs` (DOM-free, `node --test` 15 例): `positionOverview`(放射星座) / `positionDomain`(左→右分层轨道) / `positionImpact`(轮辐) / `positionExploreFresh`(ego 雷达 BFS 分环) / `positionExploreAccumulate`(锚定累积)。
- 补间引擎 `animateTo` 替代物理; 退役 `tick/frame/seed/物理常数`。
- explore 锚定累积: 展开只加新邻居到 anchor 周围, **已有节点零位移**。
- 精密仪器视觉: 发丝网格 / 信号色 amber(落 8 类色外) / 等宽码值 / 标线环 reticle / 边辉光 / 面板棱; 暗色优先, 明暗双主题, CVD 类色保留。
- fit-to-content: 视图进入/换域/换码/换 seed 自动取景; explore 展开不重取景; 整理/resize 重取景。
- 面板/搜索打磨: sticky 头(负 margin flush) + 搜索回车居中。

## 2. 验证矩阵 (controller 浏览器实证 + 独立 review)

| 项 | 方法 | 结果 |
|---|---|---|
| overview 不炸/静止/星座 | headless 渲染 | PASS (71 节点确定性星座, 无物理抖动) |
| domain 分层轨道 | 渲染 AE(60变量2列)/LB | PASS, fit 后 69/69·81/81 节点全在视口 |
| impact 轮辐 | 渲染 C99079(44域) | PASS (码表居中·域按类分环) |
| explore 锚定累积 **no-explode** | 脚本断言 fresh TU→展开 RS,PR | **EXISTING-MOVED=0, MAXΔ=0.00px PASS** |
| 物理删除后 4 视图 + no-explode | smoke 断言 | PASS (overview71/domain69/impact45/explore12 全渲染; moved=0) |
| fit-to-content 换域重取景 | 断言 AE→LB | FRAMED PASS (81/81 in-view, k=0.51) |
| 明暗双主题 + hover(网格/信号/reticle/dim) | data-theme 注入 + 程序 hover | PASS 双主题皆成立 |
| centerOn 搜索回车居中 | 断言 | moved T YES ✓ |
| panel 打开有内容 | 断言 | visible=YES, innerHTML=2463 |

## 3. 硬不变量 (final whole-branch review, opus, 全 HOLD)

1. no-explode: `positionExploreAccumulate` value-copy 已有节点 → start==target ⇒ 补间 lerp 塌缩到 a ⇒ 全程 0px (代数证明 + 单测 + 浏览器实测三方确认)。
2. 纯函数: 5 个 `position*` 无 Date/random/DOM (grep + 5 单测)。
3. 零依赖离线单文件: 无外部字体/CDN; 仅 pre-existing `127.0.0.1:8000` RAG 可选调用。
4. CVD `--c1..--c8` + 明暗双主题保留。
5. 物理彻底删除: `requestAnimationFrame(frame)`=0, 无 tick/seed/alpha/running。
6. layout 数学未被视觉/打磨 task 触碰 (git log 佐证)。

## 4. 测试与生成物

- `node --test viewer/tests/layout.test.mjs`: **15/15 pass** (含 5 纯函数/确定性 + 几何契约 + accumulate 已有节点不变/纯度)。
- `pytest scripts/tests/test_build_kg_viewer.py`: **6/6 pass** (含新 `test_no_persistent_physics`)。
- 全仓 pytest 525/525 无回归 (多 task 复核)。
- `kg_viewer.html` 与源 `build_kg_viewer.py` 重生成**逐字节一致** (regen no-op 证明; final review 独立复核 238296 bytes 一致)。

## 5. 规则 A/B/C/D

- **规则 D (审阅隔离)**: 每 task executor(写) 与 reviewer(审) 走不同 subagent/不同 session; final review 用 opus 异 session 全分支审。无自审。
- **规则 A**: 本单元是视觉/交互重构非内容压缩; 以独立几何单测 + 独立浏览器实测 + console 干净替代"独立样本"精神。
- **规则 B**: 过程无被否需归档的失败 attempt (review 发现的缺陷均当轮修复: T3 拖拽不重绘 CRITICAL / T8a html-sync CRITICAL + 整理 lastTargets / T9 sticky 双 padding); 修复轨迹留 `.superpowers/sdd/progress.md` + task-*-report.md。
- **规则 C**: RETROSPECTIVE 见 `docs/superpowers/2026-07-24-sp7-kg-viewer-ux-RETROSPECTIVE.md`。

## 6. 已知限制 / follow-up (final review 判定非阻塞)

- **[待用户决策] overview 密集类标签重叠**: Findings 类 30 域挤在一个楔形簇, 域码标签在默认缩放下重叠。属**标签策略设计选择**(常显 / hover 显 / 缩小字号 / 换排布), 刻意留给用户定, 非缺陷。
- M2 已修 (resize 重取景); M3 已修 (plan 文档 `node --test` 命令改显式文件形式)。
- 预存 dead code (非本次引入): `isDark()` 未调用, `.sw.dom/.sq` CSS 未用 — 可后续清。
