# SDTM Pedia 网站 — Motion Design Spec

> **Status**: Draft v1.0
> **Date**: 2026-04-29
> **Author**: Bojiang (with brainstorming via Claude Code superpowers)
> **Scope**: 给 `web/` (Astro 6 + React 19 + Tailwind 4, 部署在 Cloudflare Pages 的 SDTM Pedia 文档站) 加一套"低调有内涵, 又能小炫技"的动效系统. 覆盖 landing / search overlay / compare / docs / nav / footer 六个 surface. 零新依赖, CSS-only + 少量 Web Animations API.

---

## 1. Goals

1. 在不增加包大小 (无新 npm 依赖) 的前提下, 给站点一套统一的 motion vocabulary.
2. 提升首屏 5 秒内的"品味识别度" — landing 的 hero / search overlay / compare 三个 set-piece moment 让访客一眼看出这站不是模板.
3. 把现有 hover / 进场 / 切换交互的体感升级一档, 但不干扰阅读 (docs 正文区刻意保持极克制).
4. 全站尊重 `prefers-reduced-motion: reduce`, 降级到瞬切, 无障碍 (a11y) 不退步.
5. 不影响 Lighthouse Performance / LCP / CLS — 动效只走 `transform` + `opacity` + `clip-path` 合成路径.
6. 拆成 4 个独立 commit / PR, 每块都不动 layout DOM 也不破 SSG 输出, 可连续 deploy 到 CF Pages.

## 2. Non-goals

- ❌ 滚动视差 (parallax) — 跟 editorial / 等宽印刷气质不搭.
- ❌ 鼠标跟随 / 磁吸 hover — D 派"物理感"语言, 已在 register 选型时排除.
- ❌ Lottie / 视频背景 / 复杂 SVG 帧动画 — 包大小 + 不必要.
- ❌ Hero 背景点阵漂移 (T3 候选) — 评估后判断和现有平面色块打架, 主动放弃.
- ❌ Changelog 时间轴动效 — 不在用户范围内, 留给 future round.
- ❌ Framer Motion / GSAP / Anime.js — 站点是 Astro-first (12 个 `.astro` vs 6 个 React island), 用不到这种"动画工具箱".

## 3. Motion Register

### 3.1 选定: **A 排印/终端派 + C 工程/数据派 (轻)**

| 选项 | 风格关键词 | 类比参考 | 决策 |
|------|-----------|----------|------|
| A. 排印/终端派 | 字符级揭示, 光标闪烁, 下划线生长, 计数器 tick | Vercel, Linear, oxide.computer | ✅ 主线 |
| B. 书卷/编辑派 | 慢速渐显, 视差极小, 衬线字优雅滑入 | NYT, Stripe Press, Apple newsroom | ❌ 太隐身 |
| C. 工程/数据派 | 网格点位漂移, SVG draw-on, 图表条目排序 | Datadog, Grafana, Cloudflare | ✅ 点缀 (Compare FLIP) |
| D. 极简物理派 | 卡片磁吸, 光标跟随, spring | Linear, Framer 自家页 | ❌ 跟无圆角平面色块打架 |

### 3.2 理由

站点已经是 editorial / 等宽印刷气质 (`font-mono` + `tracking-[0.12em]` + 平面色块, 无圆角无阴影). 沿 A 主线扩张最不违和; C 给 SDTM 这种"标准 / 结构化"内容自带的工程感留个出口 (Compare 页的 FLIP 重排正好是 C 派语言的最佳载体).

---

## 4. Motion System

### 4.1 Tokens (写进 `web/src/styles/motion.css`)

```css
:root {
  /* 时长 */
  --motion-duration-quick: 120ms;  /* hover, toggle */
  --motion-duration-base:  240ms;  /* 进场, 切换 */
  --motion-duration-slow:  480ms;  /* hero char-stagger 总时长 */

  /* 缓动 */
  --motion-ease-out:       cubic-bezier(0.22, 1, 0.36, 1);     /* 默认进场, "Linear-style" */
  --motion-ease-out-back:  cubic-bezier(0.34, 1.56, 0.64, 1);  /* toggle 轻 overshoot */
  --motion-ease-step:      steps(1, end);                      /* caret 闪烁 */

  /* 节奏 */
  --motion-stagger:        40ms;   /* 元素错峰间隔 */
}
```

### 4.2 Reduced-Motion 合约 (写在 `motion.css` 顶部, 全局覆盖)

```css
@media (prefers-reduced-motion: reduce) {
  :root {
    --motion-duration-quick: 0ms;
    --motion-duration-base:  0ms;
    --motion-duration-slow:  0ms;
    --motion-stagger:        0ms;
  }
  .u-caret,
  .u-char-stagger > *,
  .u-underline-draw::after,
  .u-bracket-draw::before,
  .u-bracket-draw::after {
    animation: none !important;
  }
}
```

JS 路径走 `lib/motion.ts` 的 `prefersReducedMotion()` feature query, FLIP 在 reduced-motion 下直接同步 `applyFn()` 不调 WAAPI.

### 4.3 硬约束 (Hard Rules)

1. 只做 `transform` / `opacity` / `clip-path` 的合成动画 — 永不动 `width / height / top / left`.
2. `prefers-reduced-motion: reduce` 降级到瞬切, 全部动效都得有降级路径.
3. 进场动效用 `IntersectionObserver` 触发, 不全部 `animation-delay` 在首屏堆积.
4. 单页面动效总 JS 增量 ≤ 2 KB, CSS 增量 ≤ 3 KB.
5. 任何动效不能影响 LCP / CLS — hero 字符 stagger 用 `opacity` 不用 `display`.
6. 全部动效必须在 60 fps 跑 (DevTools Performance 抽检, dropped frames < 5%).

---

## 5. File Layout

### 5.1 新增文件 (2 个)

| 文件 | 职责 |
|------|------|
| `web/src/styles/motion.css` | Motion tokens (§4.1) + reduced-motion 合约 (§4.2) + 全部 `@keyframes` + 复用 utility class (`.u-caret`, `.u-caret-slide`, `.u-bracket-draw`, `.u-underline-draw`, `.u-char-stagger`) |
| `web/src/lib/motion.ts` | 三个工具: `enterOnVisible(el, opts)` (IO 触发进场), `flipReorder(container, selector, applyFn)` (Compare 重排用 WAAPI), `prefersReducedMotion(): boolean` |

### 5.2 改动现有文件 (12 个)

| 文件 | 动作 |
|------|------|
| `web/src/styles/global.css` | `@import './motion.css'`; 现有 `enter-fade` keyframes 迁移到 `motion.css` |
| `web/src/components/astro/EnterFadeScript.astro` | 改成调 `lib/motion.ts` 的 `enterOnVisible`, 逻辑统一 |
| `web/src/components/astro/HeroSection.astro` | 标题加 `.u-char-stagger` (Astro 编译期 split); CTA 加 `.u-bracket-draw` hover 类; 副标加 `.u-caret` |
| `web/src/components/astro/TopNav.astro` | 给三个 toggle 子组件留统一 token 入口 |
| `web/src/components/astro/DocsTOC.astro` | 活动项加共享 `▌` caret 元素 + `transform: translateY` 平滑跟随 (caret 元素在 DocsTOC 内, DocsSidebar 不动) |
| `web/src/components/astro/Footer.astro` | attribution 行末追加 `<span class="u-caret">_</span>` |
| `web/src/components/react/SearchOverlay.tsx` | 进出场用 CSS class 切换; 结果列表用 `--motion-stagger` 错峰; 行 hover `>` caret |
| `web/src/components/react/CompareFilter.tsx` | filter 切换前后调 `flipReorder()` 包住 `setState` |
| `web/src/components/react/ThemeToggle.tsx` | sun/moon glyph SVG `<path>` 用 `clip-path` morph |
| `web/src/components/react/LangSwitcher.tsx` | 选中 lang 时 char-roll 动效 (CSS-only, 无 React state 增量) |
| `web/src/components/react/FontSizeToggle.tsx` | 当前态指示器改成 `transform: translateX()` 滑块 |
| `web/src/styles/prose.css` | guide 正文里所有 `<a>` 加 underline-draw 替换现有色变 |

### 5.3 不动的边界

- 不引任何新依赖 (`web/package.json` 不变).
- 不改 `astro.config.mjs` / Tailwind 配置 / `tsconfig.json`.
- 不动 layout DOM 结构 (`BaseLayout` / `LandingLayout` / `DocsLayout` 零改).
- 不影响 SSG 输出 — 所有动效都是 client-side 后置增强.
- 不动 i18n (`ui.zh/en/ja.json`) 除非新加文案 (目前不需要).

---

## 6. 每个 Surface 的 Motion Spec

格式: **触发 → 动作 → 时长 / 缓动 → 降级回退**.

### 6.1 [T1] Hero 标题区 (`HeroSection.astro`)

#### 6.1.1 标题字符 stagger reveal

- **触发**: 页面 mount + `IntersectionObserver` (margin: 0px), 即首屏立即触发.
- **动作**: 每个字符 (CJK 单字 / 英文单词) `opacity 0 → 1` + `translateY 4px → 0`. 单字 `--motion-duration-base` (240ms), 整体错峰 `--motion-stagger` (40ms).
- **实现**: Astro 编译期把标题 split 成 `<span data-char>{char}</span>`, CSS `animation-delay: calc(var(--i) * var(--motion-stagger))`. 不走 client JS split.
  - CJK: 按字符切. 例: "SDTM 知识库" → `["S","D","T","M"," ","知","识","库"]` 7 帧 stagger (空格不计 stagger).
  - 英文: 按 word 切. 例: "Self-deploy bundles" → `["Self-deploy","bundles"]` 2 帧.
  - 切割逻辑放进 `web/src/lib/motion.ts` 的 `splitForStagger(text, lang)` 工具函数, Astro 模板调用.
- **降级**: `prefers-reduced-motion: reduce` → 全部 `opacity: 1`, 瞬现.

#### 6.1.2 副标尾部光标

- **触发**: 标题 stagger 完成 (animation-delay 加到末位 + 480ms buffer).
- **动作**: 副标后追加 `<span class="u-caret">_</span>`, `steps(1, end)` 1s 周期 (50% on / 50% off).
- **降级**: 显示静态 `_`, 不闪.

#### 6.1.3 CTA 按钮 bracket-draw hover

- **触发**: `:hover` / `:focus-visible`.
- **动作**: 按钮外圈用 `::before` (`[`) 和 `::after` (`]`) 等宽 bracket. 默认 `clip-path: inset(0 100% 0 0)` 隐藏; hover 时 `clip-path: inset(0 0 0 0)` 从两端"画"出来. `--motion-duration-quick` (120ms) ease-out.
- **降级**: 直接显示 `[ ... ]` (静态).

### 6.2 [T1] Search Overlay (`SearchOverlay.tsx`)

#### 6.2.1 进场

- **触发**: ⌘K / Ctrl+K open.
- **动作**:
  - Backdrop: `opacity 0 → 1` + `backdrop-filter: blur(0) → blur(8px)`.
  - 搜索框: `transform: translateY(-8px) scale(0.98) → translateY(0) scale(1)` + `opacity 0 → 1`.
  - 时长: `--motion-duration-base` (240ms) ease-out.
- **降级**: 瞬切 visible, 无 blur 过渡.

#### 6.2.2 结果列表 stagger

- **触发**: input 输入后 results 数组变化.
- **动作**: 每条结果 `translateY(6px) + opacity 0 → opacity 1`. 错峰 `--motion-stagger × index`. 上限: 前 8 条带 stagger, 之后瞬现 (避免 50 条排队).
- **降级**: 全部瞬现.

#### 6.2.3 结果行 hover caret

- **触发**: row `:hover`.
- **动作**: 行最左侧 `<span class="u-caret-slide">&gt;</span>` 默认 `transform: translateX(-4px)` + `opacity 0`, hover → `translateX(0)` + `opacity 1`. `--motion-duration-quick`.
- **降级**: 直接显示 `>` (静态).

### 6.3 [T1] Compare FLIP (`CompareFilter.tsx`)

#### 6.3.1 行重排

- **触发**: filter chip toggle 改变可见行集合.
- **动作**: FLIP 三步 (First / Last / Invert + Play)
  1. **First** — `before setState`: 拿全部行 `getBoundingClientRect()` 缓存到 Map\<string, DOMRect\>, key 用行 stable id (= 当前 React `key` prop, 即 SDTM domain row 的 `data-domain-id` 属性, 由 `CompareFilter.tsx` 给每个 row 渲染时挂上).
  2. **Last** — `after setState` (`requestAnimationFrame` 后): 拿新位置.
  3. **Invert + Play** — 对每行用 WAAPI:
     ```ts
     el.animate(
       [
         { transform: `translate(${dx}px, ${dy}px)` },
         { transform: 'translate(0, 0)' },
       ],
       { duration: 240, easing: 'cubic-bezier(0.22, 1, 0.36, 1)' }
     );
     ```
- **新增 / 移除行**: `opacity` 配合 fade in/out (120ms), 不做 height 折叠 (避免 layout thrash).
- **空态**: filter 后 0 结果时显示 `> 无匹配 ▌` 加闪烁 caret.
- **实现入口**: `web/src/lib/motion.ts` 的 `flipReorder(container: HTMLElement, selector: string, applyFn: () => void)`.
- **降级**: `prefersReducedMotion()` 返回 true 时直接 `applyFn()`, 不调 WAAPI.

### 6.4 [T2] ThemeToggle glyph morph (`ThemeToggle.tsx`)

- **触发**: click 切换 light / dark.
- **动作**: SVG `<path>` 用 `clip-path` 从太阳 (full circle) 过渡到月亮 (offset circle 切口); 图标整体 `transform: rotate(20deg)` 微转 (起到"翻面"暗示).
- **时长 / 缓动**: `--motion-duration-quick` (120ms) `--motion-ease-out-back` (轻 overshoot).
- **降级**: 直接换 icon, 无过渡.

### 6.5 [T2] LangSwitcher char-roll (`LangSwitcher.tsx`)

- **触发**: click 切换 zh → en → ja.
- **动作**: 当前选中文字 `translateY(-100%) → 0%` + `opacity` 切换. 用 `overflow: hidden` 容器 + 两层文字栈 (旧字向上滑出, 新字从下滑入).
- **时长 / 缓动**: `--motion-duration-base` (240ms) ease-out.
- **降级**: 直接换字.

### 6.6 [T2] FontSizeToggle slider (`FontSizeToggle.tsx`)

- **触发**: click 切换 4 档 (S / M / L / XL).
- **动作**: 4 档背景下层加 `<div class="indicator">` 用 `transform: translateX(calc(N * 100%))` 滑动到当前格. 当前格按钮文字加粗.
- **时长 / 缓动**: `--motion-duration-base` ease-out.
- **降级**: 静态显示 active 样式 (无滑块平移).

### 6.7 [T2] TOC active marker (`DocsTOC.astro`)

- **触发**: scroll 改变 active heading (现有 IntersectionObserver 逻辑).
- **动作**: active item 左侧 `<span class="caret">▌</span>`. 所有 item 共享一个绝对定位 caret, `transform: translateY(N * itemHeight)` 平移到当前 active item 位置 (N = active item index). 颜色用 `accent`.
- **时长 / 缓动**: `--motion-duration-base` ease-out.
- **降级**: 静态显示在 active item 边, 无平移.
- **等高假设**: 本期假设所有 TOC item 等高 (目前 prose 列表确实等高), 用 `itemHeight` 单值乘 `index` 平移. 未来 TOC 出现多行 item 时需要换成 measure-based 跟随 (拿每个 item 的 `offsetTop` 直接定位). 先 ship 等高假设.

### 6.8 [T2] Section enter-fade upgrade

- **触发**: IntersectionObserver 进入视口 (现有 `EnterFadeScript` 路径).
- **动作**: 现有 `enter-fade` (`opacity 0 → 1`) 升级加 `translateY(6px → 0)`. Section 内子元素加 stagger (40ms 错峰, 前 5 个; 之后瞬现).
- **时长 / 缓动**: `--motion-duration-base` (240ms) ease-out.
- **降级**: 直接 visible (现有降级路径不变).

### 6.9 [T2] Underline-draw (`prose.css` + nav 链接)

- **触发**: `a:hover` / `:focus-visible`.
- **动作**: `::after` 绝对定位伪元素, `transform: scaleX(0 → 1)` + `transform-origin: left` (避免 width 触发 reflow, 保留色变作为复合反馈).
- **时长 / 缓动**: `--motion-duration-quick` (120ms) ease-out.
- **降级**: 现有 `transition-colors` 仍生效 (色变保留).
- **范围**: landing 全部链接 + nav + footer + guide 正文 (`prose.css`).

### 6.10 [T3] Footer caret (`Footer.astro`)

- **触发**: 持续闪烁 (页面可见时).
- **动作**: attribution 行末追加 `<span class="u-caret">_</span>`, `steps(1, end)` 1s 周期. Tab 失去焦点时 `animation-play-state: paused`.
- **降级**: 静态 `_`, 不闪.

---

## 7. Performance & A11y 约束

### 7.1 Performance

- 全部动效只走 `transform` / `opacity` / `clip-path` 合成路径, 不触发 layout / paint.
- 单页面动效总 JS 增量 ≤ 2 KB; CSS ≤ 3 KB.
- `IntersectionObserver` 用于 enter-fade 触发 (不在首屏堆 animation-delay).
- Hero char-stagger 用 `opacity` 不用 `display` — LCP / CLS 不受影响.
- Search overlay 进场动效不阻塞主线程, 走 GPU 合成.
- Compare FLIP 用 WAAPI (`el.animate()`) 而非 React state, 不触发 React re-render.

### 7.2 A11y

- `prefers-reduced-motion: reduce` 全局降级到瞬切 (§4.2).
- 焦点可见性 (`:focus-visible`) 优先于 hover, 键盘用户也能触发 underline-draw / bracket-draw.
- caret 闪烁用 `aria-hidden="true"`, 屏幕阅读器忽略.
- 所有动效均为视觉增强, 关键内容 (链接 / 按钮 / 文字) 在动效前已 DOM ready.
- 不依赖 motion 才能完成的核心交互 — search / compare / toggle 在 reduced-motion 下功能完整.

---

## 8. 测试策略

按现有 vitest + playwright 框架延伸, 不引新工具.

| 层级 | 工具 | 测什么 | 不测什么 |
|------|------|--------|---------|
| **Unit** | `web/src/lib/motion.test.ts` (新增) | `prefersReducedMotion()` (mock matchMedia); `enterOnVisible()` (mock IO 触发); `flipReorder()` (mock getBoundingClientRect + 验 WAAPI 调用次数); `splitForStagger(text, lang)` 切字逻辑 | 视觉效果 — vitest 测不了 |
| **Component (vitest + RTL)** | `*.test.tsx` 现有套件扩 | DOM 结构正确: caret 元素存在; char-stagger spans 数量 = title 字符数; reduced-motion 下没有 inline animation 属性 | 真实动画时序 |
| **E2E (playwright)** | `tests/animations.spec.ts` (新增) | hero 标题在 IO 触发后变 `opacity: 1`; search overlay 按 ⌘K 打开后 backdrop visible; compare filter toggle 后 row 数量正确 (不测 FLIP 时序, 测最终态) | 60 fps / 真实视觉 |
| **Manual (chrome-devtools MCP)** | Performance panel 录制 | 每个 set-piece 60 fps; LCP 不退化; CLS = 0; reduced-motion 下零动画 | — |
| **Regression** | `helpers.test.ts` (现有 key-parity 测试) | i18n key 不漏 — 给三个 toggle 加新文本时不漏译 (本期暂无新文案, 但保留约束) | — |

---

## 9. Acceptance Criteria

完成判定 (写进 PR description 当 checklist):

- [ ] `cd web && npm test` 全绿.
- [ ] `cd web && npm run test:e2e` 全绿 (含新增 `animations.spec.ts`).
- [ ] `cd web && npm run build:fresh` 成功, dist 无 console error.
- [ ] Lighthouse 在 `https://sdtm-pedia.pages.dev/zh/` 上 Performance ≥ 95 (基线对比), LCP < 2.5 s, CLS = 0.
- [ ] Chrome DevTools Performance trace: T1 三个动效 (hero / search overlay open / compare filter) 全部 60 fps (dropped frames < 5%).
- [ ] 手测 `prefers-reduced-motion: reduce` (系统设置 + DevTools rendering pane): 全部动效降级为瞬切.
- [ ] 手测三浏览器: Chrome / Safari / Firefox (macOS 当前版本即可).
- [ ] 独立 reviewer agent (规则 D) 跑一遍 visual review — 用 `oh-my-claudecode:visual-verdict` 或 `code-reviewer` subagent, 截图对比并签 PASS.

---

## 10. 交付节奏 (4 个独立 commit / PR)

每块独立 commit, 独立 visual review, 后块出问题不影响前块. 每块都不动 layout / SSG 输出, CF Pages 可连续 deploy.

| # | 包 | 改动文件 | 视觉 diff | 风险 |
|---|----|---------|----------|------|
| **C1 — 基座** | `motion.css` + `lib/motion.ts` + `EnterFadeScript` refactor + `motion.test.ts` | 5 文件 | 无 (refactor only) | 低 — 纯重构, 验现有 enter-fade 不退化 |
| **C2 — T2 Micro** | TopNav 三 toggle (Theme/Lang/FontSize) + DocsTOC caret + section enter-fade 升级 + underline-draw (nav + prose) | ~7 文件 | 中 — hover/click 体感升级 | 低 — 增量 |
| **C3 — T1 Set-piece** | Hero char-stagger + SearchOverlay 进出场 + CompareFilter FLIP | ~3 文件 | 大 — 三个 set-piece moment 上线 | 中 — Compare FLIP 是唯一带 WAAPI 的, 需细测 |
| **C4 — T3 Atmospheric** | Footer caret | 1 文件 | 微 — 末行多个闪光标 | 极低 |

每块完成 → 独立 reviewer subagent (规则 D) 跑 visual-verdict → 用户 ack → 进下一块.

---

## 11. Out-of-scope (本期不做, 防止 scope creep)

- ❌ 滚动视差 (任何形式).
- ❌ 鼠标跟随 / 磁吸 hover.
- ❌ Lottie / 视频背景 / 复杂 SVG 帧动画.
- ❌ Hero 背景点阵漂移 (T3 候选, 主动放弃).
- ❌ Changelog 时间轴动效 (留 future round).
- ❌ Framer Motion / GSAP / Anime.js / Motion One.
- ❌ Docs guide 正文区域内动效 (除链接 hover underline-draw + TOC active marker 外).
- ❌ i18n 新文案 (本期 motion 不需要新增文本).

---

## 12. Open Questions / Followups

无. 全部决策已在 brainstorming 收敛, 见上各节.

未来 round 可考虑 (不在本期):
- Hero 字符 split 改成 client-side IntersectionObserver 触发 (而非 mount 即触发) — 如果加更多 hero variant.
- TOC 多行 item 的 measure-based 跟随 (本期假设等高).
- Changelog 时间轴动效 (B 派 / editorial 风, 跟当前 A+C 主线不同).
- Hero 背景点阵漂移 — 如果调色板未来变化, 平面色块感减弱时可重新评估.

---

## 13. References

- 现有 phase 11.5-fix 收尾后状态: `web/src/styles/global.css` 已有 `enter-fade` keyframes + `transition-colors` + `prefers-reduced-motion` 守卫.
- 现有 React island: `CountUp.tsx` (数字 tween, 已有 reduced-motion check, 可作为新动效 a11y 对照参考).
- Astro 6 文档: islands client directives (`client:load` / `client:visible`) — Search/Compare 已用 `client:load`, 不变.
- Web Animations API: `el.animate()` 浏览器支持 100% (Chrome / Safari / Firefox 当前版).
- FLIP 技法: First-Last-Invert-Play, by Paul Lewis (https://aerotwist.com/blog/flip-your-animations/).
- Motion register A 参考: Linear, Vercel, oxide.computer.
- Motion register C 参考: Datadog, Cloudflare 主页.
