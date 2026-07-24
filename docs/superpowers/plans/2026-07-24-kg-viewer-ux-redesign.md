# KG 查看器 UX 重构 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 SDTM 知识图谱查看器从「力导向物理 + 每次交互全量重排」重构为「每视图确定性布局 + 缓动补间 + 无常驻物理」,并赋予"精密仪器"视觉性格,根治"点一下到处飞到处弹"。

**Architecture:** 现有单文件 `build_kg_viewer.py` 的 `TEMPLATE` 拆为 `sdtm-rag/viewer/{template.html,style.css,app.js,layout.mjs}`,build 时内联成零依赖单文件 `kg_viewer.html`(产物形态不变)。纯定位数学抽到 DOM-free 的 `layout.mjs`(ESM, `node --test` 可测),渲染/补间/交互留在 `app.js`。四视图各有确定性 `position*` 函数;一个补间引擎替代物理循环。垂直切片推进:先 overview 打通管线,再逐视图接入,最后退役物理。

**Tech Stack:** Python 3.14(`.venv`,生成脚本) · 原生浏览器 JS/SVG(无框架无 CDN) · Node 26 `node:test`(纯布局单测) · pytest(既有 build 测试) · chrome-devtools / claude-in-chrome MCP(浏览器实证)。

## Global Constraints

- 产物 `kg_viewer.html` 必须是**零依赖 · 离线 · 单 HTML**:不得引外部字体/CDN/远程资源。
- **绝不手改 `kg_viewer.html`**(生成物);一切改 `sdtm-rag/viewer/*` 源码,`cd sdtm-rag && .venv/bin/python scripts/build_kg_viewer.py` 重新生成。
- 保留类的 CVD-safe 配色变量 `--c1..--c8` 与明暗双主题;暗色为主基调但**默认跟随系统偏好**(亮色用户仍得亮色)。
- 软层永不改动 `meta.yaml`;不改数据层与挖掘管线。
- 保留 SP6 既有能力无回归:图层开关、RAG"深入解释"按钮(`:8000` 探活,离线隐藏)、点推断边→证据弹窗、缩放/平移。
- 布局函数必须是**纯函数**(无随机、无时间、无 DOM):同输入永远同输出。
- 每次 commit message 末尾附项目要求的 `Co-Authored-By` / `Claude-Session` 脚注(见仓库 CLAUDE.md 提交协议)。
- 浏览器实证服务用 `:8010`(避开 RAG launchd 占用的 `:8000`)。
- 规则 D:实现(executor)与验收(另一 subagent,不同 session)分离,不自审。

---

### Task 1: U0 源码拆分(行为等价迁移)

把当前 `TEMPLATE` 原样拆到 `viewer/` 下的文件,build 时内联回去。产物与迁移前**逐视觉一致**,既有 pytest 全绿。这是纯重构,不改任何行为。

**Files:**
- Create: `sdtm-rag/viewer/template.html`(骨架 + `<style>__STYLE__</style>` + SVG defs + `<script>__APP__</script>`,`__DATA__` 占位保留)
- Create: `sdtm-rag/viewer/style.css`(现 `TEMPLATE` 内 `<style>` 全部内容,逐字搬)
- Create: `sdtm-rag/viewer/app.js`(现 `TEMPLATE` 内 `<script>` 全部内容,逐字搬,含 `const DATA=__DATA__;`)
- Modify: `sdtm-rag/scripts/build_kg_viewer.py`(用文件组装替换内联 `TEMPLATE` 字符串)
- Test: `sdtm-rag/scripts/tests/test_build_kg_viewer.py`(不改断言,验证仍绿)

**Interfaces:**
- Produces: `build_kg_viewer.TEMPLATE`(模块属性,值为组装后的完整 HTML 模板字符串,含 `__DATA__` 占位)——既有测试依赖它,必须保留。
- Produces: `build_kg_viewer.VIEWER_DIR = ROOT / "viewer"`;`assemble_template() -> str`。

- [ ] **Step 1: 拆文件**——把 `build_kg_viewer.py` 里 `TEMPLATE` 三引号串中 `<style>...</style>` 的内容原样存入 `viewer/style.css`,`<script>...</script>` 的内容(从 `const DATA=__DATA__;` 起到末尾)原样存入 `viewer/app.js`,其余骨架存入 `viewer/template.html`,并在 template.html 中把原 `<style>` 体替换为 `__STYLE__`、原 `<script>` 体替换为 `__APP__`。

`viewer/template.html`(结构示意,`<head>`/`<body>` 其余逐字保留自原 TEMPLATE):
```html
<!doctype html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SDTM 知识图谱</title>
<style>__STYLE__</style>
</head>
<body>
<div id="app"> ... 原样 ... </div>
<div id="tip"></div>
<script>__APP__</script>
</body>
</html>
```

- [ ] **Step 2: 改 build 脚本组装逻辑**——在 `build_kg_viewer.py` 用读文件组装替换写死的 `TEMPLATE`:

```python
VIEWER_DIR = ROOT / "viewer"

def assemble_template() -> str:
    """Inline viewer/{style.css,app.js} into template.html. Output identical in
    shape to the former inline TEMPLATE (still contains the __DATA__ placeholder)."""
    html = (VIEWER_DIR / "template.html").read_text(encoding="utf-8")
    css = (VIEWER_DIR / "style.css").read_text(encoding="utf-8")
    js = (VIEWER_DIR / "app.js").read_text(encoding="utf-8")
    return html.replace("__STYLE__", css).replace("__APP__", js)

TEMPLATE = assemble_template()   # module attribute: existing tests read this
```
`main()` 保持不变(它已 `TEMPLATE.replace("__DATA__", payload)`)。删除原三引号 `TEMPLATE = r"""..."""` 块。

- [ ] **Step 3: 重新生成并验证等价**

Run:
```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
cp kg_viewer.html /tmp/kg_viewer.before.html
.venv/bin/python scripts/build_kg_viewer.py
diff <(grep -v '^const DATA=' /tmp/kg_viewer.before.html) <(grep -v '^const DATA=' kg_viewer.html) && echo "EQUIVALENT (ignoring data line)"
```
Expected: 打印 `wrote .../kg_viewer.html (...KB)` 与 `EQUIVALENT (ignoring data line)`(数据行相同则整体逐字节相同;此 diff 容忍数据行差异以防 meta 变动,正常应无差异)。

- [ ] **Step 4: 既有测试保持绿**

Run: `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_build_kg_viewer.py -v`
Expected: 全部 PASS(`TEMPLATE` 组装后仍含所有被断言的子串)。

- [ ] **Step 5: Commit**

```bash
git add sdtm-rag/viewer/ sdtm-rag/scripts/build_kg_viewer.py
git commit -m "refactor(kg-viewer): 源码拆分 viewer/{template,style,app}, build 时内联(行为等价)"
```

---

### Task 2: 纯布局模块 + 缓动 + Node 测试脚手架 + overview 定位

新建 DOM-free 的 `layout.mjs`,先落 `easeOutCubic`/`lerp`/`positionOverview`,并建 `node --test` 脚手架。TDD。此任务不接渲染,纯函数 + 单测。

**Files:**
- Create: `sdtm-rag/viewer/layout.mjs`
- Create: `sdtm-rag/viewer/tests/layout.test.mjs`
- Modify: `sdtm-rag/scripts/build_kg_viewer.py`（内联 layout.mjs，剥离 export）

**Interfaces:**
- Produces: `easeOutCubic(t:number)->number`、`lerp(a,b,t)->number`、`TAU`、`CLASS_ORDER:string[]`
- Produces: `positionOverview(view, vp) -> {[id:string]:{x:number,y:number}}`，其中 `view={nodes:[{id,type,label,cls,...}],edges}`，`vp={width,height}`；键为节点 `id`（`"C:"+类名` / `"D:"+域码`）。

- [ ] **Step 1: 写失败测试**

`viewer/tests/layout.test.mjs`:
```javascript
import { test } from "node:test";
import assert from "node:assert/strict";
import { easeOutCubic, lerp, positionOverview, CLASS_ORDER } from "../layout.mjs";

const VP = { width: 1200, height: 800 };
function overviewView() {
  const nodes = [];
  for (const c of CLASS_ORDER) nodes.push({ id: "C:" + c, type: "class", label: c, cls: c });
  // 每类给 3 个域，Findings 给 10 个（压密度）
  for (const c of CLASS_ORDER) {
    const k = c === "Findings" ? 10 : 3;
    for (let i = 0; i < k; i++) nodes.push({ id: `D:${c[0]}${i}`, type: "domain", label: `${c[0]}${i}`, cls: c });
  }
  return { nodes, edges: [] };
}

test("easing/lerp 边界", () => {
  assert.equal(easeOutCubic(0), 0);
  assert.equal(easeOutCubic(1), 1);
  assert.equal(lerp(10, 20, 0.5), 15);
});

test("overview: 8 个类枢纽等距排在同一环上", () => {
  const p = positionOverview(overviewView(), VP);
  const rs = CLASS_ORDER.map(c => Math.hypot(p["C:" + c].x, p["C:" + c].y));
  for (const r of rs) assert.ok(Math.abs(r - rs[0]) < 1e-6, "hub 半径应相等");
});

test("overview: 每个域离本类枢纽比离其他任何枢纽都近", () => {
  const view = overviewView();
  const p = positionOverview(view, VP);
  for (const n of view.nodes.filter(x => x.type === "domain")) {
    const own = Math.hypot(p[n.id].x - p["C:" + n.cls].x, p[n.id].y - p["C:" + n.cls].y);
    for (const c of CLASS_ORDER) if (c !== n.cls) {
      const other = Math.hypot(p[n.id].x - p["C:" + c].x, p[n.id].y - p["C:" + c].y);
      assert.ok(own < other, `${n.id} 应最靠近本类 ${n.cls}`);
    }
  }
});

test("overview: 纯函数——两次调用完全一致", () => {
  const v = overviewView();
  assert.deepEqual(positionOverview(v, VP), positionOverview(v, VP));
});
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && node --test viewer/tests/`
Expected: FAIL(`Cannot find module '../layout.mjs'` 或导出缺失)。

- [ ] **Step 3: 实现 layout.mjs**

`viewer/layout.mjs`:
```javascript
export const TAU = Math.PI * 2;
export const CLASS_ORDER = ["Special-Purpose","Interventions","Events","Findings",
  "Findings About","Trial Design","Relationship","Study Reference"];
export const easeOutCubic = t => 1 - Math.pow(1 - t, 3);
export const lerp = (a, b, t) => a + (b - a) * t;

// 结构总览：8 个类枢纽固定排在同一环上，各类的域成朝外楔形簇。
export function positionOverview(view, vp) {
  const pos = {};
  const R = Math.min(vp.width, vp.height) * 0.30;   // 枢纽环半径
  const byClass = {};
  for (const n of view.nodes) if (n.type === "domain") (byClass[n.cls] ??= []).push(n);
  for (const k in byClass) byClass[k].sort((a, b) => a.label < b.label ? -1 : a.label > b.label ? 1 : 0);
  const hub = {};
  CLASS_ORDER.forEach((cls, i) => {
    const ang = -Math.PI / 2 + TAU * i / CLASS_ORDER.length;
    hub[cls] = { x: R * Math.cos(ang), y: R * Math.sin(ang), ang };
    pos["C:" + cls] = { x: hub[cls].x, y: hub[cls].y };
  });
  const perRing = 6, halfW = 0.42;
  for (const cls of CLASS_ORDER) {
    const doms = byClass[cls] || [], h = hub[cls];
    doms.forEach((d, j) => {
      const ring = Math.floor(j / perRing), inRing = j % perRing;
      const count = Math.min(perRing, doms.length - ring * perRing);
      const spread = count > 1 ? (inRing / (count - 1) - 0.5) * 2 * halfW : 0;
      const rr = 46 + ring * 30, a2 = h.ang + spread;
      pos[d.id] = { x: h.x + rr * Math.cos(a2), y: h.y + rr * Math.sin(a2) };
    });
  }
  return pos;
}
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && node --test viewer/tests/`
Expected: PASS(4 tests)。

- [ ] **Step 5: build 内联 layout.mjs（剥离 export）**

在 `build_kg_viewer.py` 的 `assemble_template()` 里，把 layout.mjs 内联进 app 之前（app.js 顶部会用到这些符号）。用正则剥离模块语法，使其成为可内联的普通脚本片段：

```python
import re

def _inline_module(text: str) -> str:
    """Strip ESM export keywords so a pure .mjs can inline into a classic <script>."""
    text = re.sub(r"^export\s+(const|function|let|var)\s", r"\1 ", text, flags=re.M)
    text = re.sub(r"^export\s*\{[^}]*\};?\s*$", "", text, flags=re.M)
    return text

def assemble_template() -> str:
    html = (VIEWER_DIR / "template.html").read_text(encoding="utf-8")
    css = (VIEWER_DIR / "style.css").read_text(encoding="utf-8")
    layout = _inline_module((VIEWER_DIR / "layout.mjs").read_text(encoding="utf-8"))
    app = (VIEWER_DIR / "app.js").read_text(encoding="utf-8")
    return (html.replace("__STYLE__", css)
                .replace("__APP__", layout + "\n" + app))
```
（app.js 此刻还没用到 layout 符号，内联无害；Task 3 起才消费。）

- [ ] **Step 6: 重新生成 + 全测试**

Run:
```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
.venv/bin/python scripts/build_kg_viewer.py && node --test viewer/tests/ && .venv/bin/python -m pytest scripts/tests/test_build_kg_viewer.py -q
```
Expected: 生成成功；node 测试 4 PASS；pytest 全绿。

- [ ] **Step 7: Commit**

```bash
git add sdtm-rag/viewer/layout.mjs sdtm-rag/viewer/tests/ sdtm-rag/scripts/build_kg_viewer.py
git commit -m "feat(kg-viewer): 纯布局模块 layout.mjs + node 单测脚手架 + overview 定位(TDD)"
```

---

### Task 3: 补间引擎 + 渲染管线接入（overview 垂直切片）

给 `app.js` 加补间引擎与 `LAYOUT` 注册表；`build()` 对已注册视图走「确定性定位 + 补间」，未注册视图暂回退物理。接入 overview，浏览器实证"不炸开"。

**Files:**
- Modify: `sdtm-rag/viewer/app.js`
- Test: 浏览器实证（本任务无新单测；`positionOverview` 已在 Task 2 覆盖）

**Interfaces:**
- Consumes: `positionOverview`、`easeOutCubic`、`lerp`（内联自 layout.mjs，全局可见）
- Produces: `animateTo(targets, opts)`、`const LAYOUT = {overview: (view)=>positionOverview(view, viewport())}`、`viewport()->{width,height}`

- [ ] **Step 1: 加视口读取与补间引擎**——在 `app.js` 力模拟段附近加：

```javascript
function viewport(){ const r = svg.getBoundingClientRect(); return {width:r.width, height:r.height}; }
let tweenRAF = 0;
function animateTo(targets, {duration=380}={}){
  cancelAnimationFrame(tweenRAF);
  const from = {}; for(const n of N) from[n.id] = {x:n.x, y:n.y};
  const start = performance.now();
  function step(now){
    const t = Math.min(1, (now-start)/duration), e = easeOutCubic(t);
    for(const n of N){ const tg=targets[n.id]; if(!tg) continue;
      const f = from[n.id] || tg; n.x = lerp(f.x, tg.x, e); n.y = lerp(f.y, tg.y, e); }
    draw();
    if(t<1) tweenRAF = requestAnimationFrame(step);
  }
  tweenRAF = requestAnimationFrame(step);
}
const LAYOUT = { overview: view => positionOverview(view, viewport()) };
```

- [ ] **Step 2: 让 `build()` 分流**——在 `build(view)` 里，`seed(N)` 之后、`raf=requestAnimationFrame(frame)` 之前，插入分流。已注册视图：给新节点一个初始位（种子或中心）再补间到目标，且**不启动物理**；未注册视图：保持现有物理 `frame` 循环。

把 `build()` 尾部（现为 `alpha=1; running=true; ...; resetZoom(); raf=requestAnimationFrame(frame); applyLayerToggles();`）改为：
```javascript
  const det = LAYOUT[cur.v];
  resetZoom();
  if(det){
    const targets = det(view);
    for(const n of N){ const tg=targets[n.id]; if(tg){ n.x=tg.x; n.y=tg.y; } }  // 首帧即到位（无入场跳动）
    draw();
    running=false; $("#physBtn").textContent="⤺ 整理";   // 确定性视图：物理关，按钮语义暂改（Task 7 定稿）
  } else {
    alpha=1; running=true; $("#physBtn").textContent="⏸ 布局";
    raf=requestAnimationFrame(frame);
  }
  applyLayerToggles();
```
> 首次渲染直接到位（不做入场动画避免"炸开感"）；视图间切换的补间在 Task 7 统一（切视图会 `build()` 重建 DOM，补间需保留旧位——Task 7 引入跨 build 的位置继承）。本任务只需 overview 静止、正确、无物理抖动。

- [ ] **Step 3: 拖拽在确定性视图不被物理回收**——`startDrag` 的 `up()` 里现有 `drag.fix=0`，物理关闭时 fix 无意义但无害；确认拖拽后节点停在落点：确定性视图 `running=false`，`frame` 不 tick，落点保持。无需改码，浏览器验证即可。

- [ ] **Step 4: 重新生成并浏览器实证**

Run:
```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
.venv/bin/python scripts/build_kg_viewer.py
.venv/bin/python -m http.server 8010 >/tmp/kgsrv.log 2>&1 &
echo "served at http://localhost:8010/kg_viewer.html"
```
然后用 chrome-devtools/claude-in-chrome 打开 `http://localhost:8010/kg_viewer.html`：
- 验收 A：结构总览**静止不抖**（等 1s，无位移）。
- 验收 B：8 类枢纽成环、各类域成簇，星座形态符合 §3.1。
- 验收 C：拖一个域节点，松手后**停在落点**，其他节点不动。
- 验收 D：console 无报错（`list_console_messages`）。
截图存 `/tmp/kg_task3_overview_{light,dark}.png`。

- [ ] **Step 5: Commit**

```bash
git add sdtm-rag/viewer/app.js
git commit -m "feat(kg-viewer): 补间引擎 + 渲染管线分流; overview 确定性定位接入(无物理)"
```

---

### Task 4: 域钻取 · 左→右分层轨道布局

**Files:**
- Modify: `sdtm-rag/viewer/layout.mjs`（加 `positionDomain`）
- Modify: `sdtm-rag/viewer/app.js`（注册 domain）
- Test: `sdtm-rag/viewer/tests/layout.test.mjs`（加 domain 用例）

**Interfaces:**
- Produces: `positionDomain(view, vp) -> {[id]:{x,y}}`；view 由现有 `vDomain(code)` 产出，节点 id 为 `"D:"+code`/`"V:"+var`/`"K:"+code`，type 为 `domain`/`var`/`code`。

- [ ] **Step 1: 写失败测试**（追加到 layout.test.mjs）

```javascript
import { positionDomain } from "../layout.mjs";
function domainView(nVars) {
  const nodes = [{ id: "D:AE", type: "domain", label: "AE", cls: "Events" }];
  for (let i = 0; i < nVars; i++) nodes.push({ id: `V:v${i}`, type: "var", label: `v${i}` });
  nodes.push({ id: "K:C1", type: "code", label: "C1" }, { id: "K:C2", type: "code", label: "C2" });
  return { nodes, edges: [] };
}
test("domain: 三层 x 严格递增(域<变量<码表)", () => {
  const p = positionDomain(domainView(5), VP);
  const xVar = p["V:v0"].x, xCode = p["K:C1"].x, xDom = p["D:AE"].x;
  assert.ok(xDom < xVar && xVar < xCode, "x 应 域<变量<码表");
});
test("domain: 变量超阈值分两列", () => {
  const p = positionDomain(domainView(30), VP);
  const xs = new Set(Array.from({length:30},(_,i)=>p[`V:v${i}`].x));
  assert.equal(xs.size, 2, "30 变量应占 2 个 x 列");
});
test("domain: 纯函数", () => {
  const v = domainView(12);
  assert.deepEqual(positionDomain(v, VP), positionDomain(v, VP));
});
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && node --test viewer/tests/`
Expected: FAIL(`positionDomain` 未导出)。

- [ ] **Step 3: 实现 positionDomain**（加入 layout.mjs）

```javascript
export function positionDomain(view, vp) {
  const pos = {};
  const vars = view.nodes.filter(n => n.type === "var");
  const codes = view.nodes.filter(n => n.type === "code");
  const domain = view.nodes.find(n => n.type === "domain");
  const x0 = -vp.width * 0.28, x1 = 0, x2 = vp.width * 0.30, gap = 34, maxCol = 24;
  const cols = vars.length > maxCol ? 2 : 1, per = Math.ceil(vars.length / cols) || 1;
  vars.forEach((v, i) => {
    const c = Math.floor(i / per), r = i % per;
    const colH = (Math.min(per, vars.length - c * per) - 1) * gap;
    pos[v.id] = { x: x1 + c * 70, y: -colH / 2 + r * gap };
  });
  const cH = (codes.length - 1) * gap;
  codes.forEach((k, i) => pos[k.id] = { x: x2, y: -cH / 2 + i * gap });
  if (domain) pos[domain.id] = { x: x0, y: 0 };
  return pos;
}
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && node --test viewer/tests/`
Expected: PASS(含新 3 用例)。

- [ ] **Step 5: 注册 domain**——app.js 的 `LAYOUT` 改为：
```javascript
const LAYOUT = {
  overview: view => positionOverview(view, viewport()),
  domain:   view => positionDomain(view, viewport()),
};
```

- [ ] **Step 6: 重新生成 + 浏览器实证**

Run: `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && .venv/bin/python scripts/build_kg_viewer.py`
浏览器（服务若已停则重开 `:8010`）切到"域钻取"，选几个域（AE=变量多、DM）：验收 域→变量→码表 三列左右排列、静止、变量多时分两列、console 干净。截图 `/tmp/kg_task4_domain.png`。

- [ ] **Step 7: Commit**

```bash
git add sdtm-rag/viewer/layout.mjs sdtm-rag/viewer/app.js sdtm-rag/viewer/tests/layout.test.mjs
git commit -m "feat(kg-viewer): 域钻取分层轨道确定性布局(TDD) + 注册"
```

---

### Task 5: 码表影响 · 轮辐布局

**Files:**
- Modify: `sdtm-rag/viewer/layout.mjs`（加 `positionImpact`）
- Modify: `sdtm-rag/viewer/app.js`（注册 impact）
- Test: `sdtm-rag/viewer/tests/layout.test.mjs`

**Interfaces:**
- Produces: `positionImpact(view, vp) -> {[id]:{x,y}}`；view 由 `vImpact(code)` 产出，id 为 `"K:"+code`（枢纽）/`"D:"+dm`；域节点带 `cls`。

- [ ] **Step 1: 写失败测试**

```javascript
import { positionImpact } from "../layout.mjs";
function impactView(nDoms) {
  const nodes = [{ id: "K:C66742", type: "code", label: "C66742" }];
  for (let i = 0; i < nDoms; i++)
    nodes.push({ id: `D:d${i}`, type: "domain", label: `d${i}`, cls: CLASS_ORDER[i % CLASS_ORDER.length] });
  return { nodes, edges: [] };
}
test("impact: 枢纽在中心", () => {
  const p = positionImpact(impactView(10), VP);
  assert.ok(Math.hypot(p["K:C66742"].x, p["K:C66742"].y) < 1e-6);
});
test("impact: 单环时所有域到中心等距", () => {
  const p = positionImpact(impactView(10), VP);
  const rs = Array.from({length:10},(_,i)=>Math.hypot(p[`D:d${i}`].x, p[`D:d${i}`].y));
  for (const r of rs) assert.ok(Math.abs(r - rs[0]) < 1e-6);
});
test("impact: 纯函数", () => {
  const v = impactView(20);
  assert.deepEqual(positionImpact(v, VP), positionImpact(v, VP));
});
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && node --test viewer/tests/`
Expected: FAIL(`positionImpact` 未导出)。

- [ ] **Step 3: 实现 positionImpact**

```javascript
export function positionImpact(view, vp) {
  const pos = {};
  const hub = view.nodes.find(n => n.type === "code");
  const doms = view.nodes.filter(n => n.type === "domain").sort((a, b) =>
    (CLASS_ORDER.indexOf(a.cls) - CLASS_ORDER.indexOf(b.cls)) || (a.label < b.label ? -1 : 1));
  if (hub) pos[hub.id] = { x: 0, y: 0 };
  const base = Math.min(vp.width, vp.height), R = base * 0.34, per = 28;
  doms.forEach((d, i) => {
    const ring = Math.floor(i / per), inRing = i % per;
    const count = Math.min(per, doms.length - ring * per);
    const ang = -Math.PI / 2 + TAU * inRing / count, rr = R + ring * base * 0.14;
    pos[d.id] = { x: rr * Math.cos(ang), y: rr * Math.sin(ang) };
  });
  return pos;
}
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && node --test viewer/tests/`
Expected: PASS。

- [ ] **Step 5: 注册 impact**——`LAYOUT` 加 `impact: view => positionImpact(view, viewport())`。

- [ ] **Step 6: 重新生成 + 浏览器实证**

生成后切"码表影响"，选波及域多的码表（如 NY/C66742）：验收 码表居中、域绕环、同类相邻着色、静止、console 干净。截图 `/tmp/kg_task5_impact.png`。

- [ ] **Step 7: Commit**

```bash
git add sdtm-rag/viewer/layout.mjs sdtm-rag/viewer/app.js sdtm-rag/viewer/tests/layout.test.mjs
git commit -m "feat(kg-viewer): 码表影响轮辐确定性布局(TDD) + 注册"
```

---

### Task 6: 网状探索 · ego 雷达 + 锚定累积 + 整理

Explore 接入确定性定位。fresh 进入/换种子/整理 → BFS 分环雷达（`positionExploreFresh`）；点节点展开 → 锚定累积（`positionExploreAccumulate`，旧节点全锁死，新邻居落 anchor 周围空槽）。加"整理"按钮。

**Files:**
- Modify: `sdtm-rag/viewer/layout.mjs`（加两个 explore 定位 + BFS 辅助）
- Modify: `sdtm-rag/viewer/app.js`（注册 explore、改 `expandNode` 为锚定累积、"整理"按钮、跨 build 位置继承）
- Test: `sdtm-rag/viewer/tests/layout.test.mjs`
- Test: `sdtm-rag/scripts/tests/test_build_kg_viewer.py`（`test_expand_follows_hard_edges_first` 断言更新为新函数名）

**Interfaces:**
- Consumes: view 由 `vExplore(seed)` 产出（节点 `"D:"+code`；edges `{s,t,layer}`，layer∈`hard|flow|link|cooc`）。
- Produces: `positionExploreFresh(view, vp, {seedId}) -> {[id]:{x,y}}`（seed 居中，BFS 深度分环）。
- Produces: `positionExploreAccumulate(view, vp, {prevPos, anchorId}) -> {[id]:{x,y}}`（prevPos 中的 id 原位不动，新 id 落 anchor 周围空角度槽）。

- [ ] **Step 1: 写失败测试**

```javascript
import { positionExploreFresh, positionExploreAccumulate } from "../layout.mjs";
function ring1View() {
  return { nodes: [{id:"D:TU",type:"domain",label:"TU"},{id:"D:TR",type:"domain",label:"TR"},
                    {id:"D:RS",type:"domain",label:"RS"},{id:"D:PR",type:"domain",label:"PR"}],
           edges: [{s:"D:TU",t:"D:TR",layer:"flow"},{s:"D:TU",t:"D:RS",layer:"hard"},
                   {s:"D:TU",t:"D:PR",layer:"cooc"}] };
}
test("exploreFresh: 种子居中", () => {
  const p = positionExploreFresh(ring1View(), VP, { seedId: "D:TU" });
  assert.ok(Math.hypot(p["D:TU"].x, p["D:TU"].y) < 1e-6);
});
test("exploreFresh: 一跳邻居等距成环", () => {
  const p = positionExploreFresh(ring1View(), VP, { seedId: "D:TU" });
  const rs = ["D:TR","D:RS","D:PR"].map(id => Math.hypot(p[id].x, p[id].y));
  for (const r of rs) assert.ok(Math.abs(r - rs[0]) < 1e-6);
});
test("exploreAccumulate: 已有节点位置不变，新节点落 anchor 附近", () => {
  const prevPos = { "D:TU": {x:0,y:0}, "D:TR": {x:100,y:0} };
  const view = { nodes:[{id:"D:TU"},{id:"D:TR"},{id:"D:MI"},{id:"D:RS"}],
                 edges:[{s:"D:TR",t:"D:MI",layer:"flow"},{s:"D:TR",t:"D:RS",layer:"hard"}] };
  const p = positionExploreAccumulate(view, VP, { prevPos, anchorId: "D:TR" });
  assert.deepEqual(p["D:TU"], {x:0,y:0});
  assert.deepEqual(p["D:TR"], {x:100,y:0});
  for (const id of ["D:MI","D:RS"])
    assert.ok(Math.hypot(p[id].x - 100, p[id].y - 0) < 200, `${id} 应落 anchor TR 附近`);
});
test("explore: 纯函数", () => {
  const v = ring1View();
  assert.deepEqual(positionExploreFresh(v, VP, {seedId:"D:TU"}), positionExploreFresh(v, VP, {seedId:"D:TU"}));
});
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && node --test viewer/tests/`
Expected: FAIL(两函数未导出)。

- [ ] **Step 3: 实现两个 explore 定位 + BFS**

```javascript
const LAYER_PRIO = { hard: 0, flow: 1, link: 2, cooc: 3 };

function adjacency(view) {
  const adj = new Map();
  for (const n of view.nodes) adj.set(n.id, []);
  for (const e of view.edges) {
    if (adj.has(e.s) && adj.has(e.t)) { adj.get(e.s).push(e.t); adj.get(e.t).push(e.s); }
  }
  return adj;
}

export function positionExploreFresh(view, vp, { seedId }) {
  const pos = {}, adj = adjacency(view), depth = new Map([[seedId, 0]]), q = [seedId];
  while (q.length) { const u = q.shift();
    for (const v of (adj.get(u) || [])) if (!depth.has(v)) { depth.set(v, depth.get(u) + 1); q.push(v); } }
  const byDepth = {};
  for (const n of view.nodes) { const d = depth.has(n.id) ? depth.get(n.id) : 1;
    (byDepth[d] ??= []).push(n.id); }
  const base = Math.min(vp.width, vp.height);
  pos[seedId] = { x: 0, y: 0 };
  for (const d in byDepth) {
    if (d === "0") continue;
    const ids = byDepth[d].slice().sort(), rr = base * 0.22 * Number(d);
    ids.forEach((id, i) => { const ang = -Math.PI / 2 + TAU * i / ids.length;
      pos[id] = { x: rr * Math.cos(ang), y: rr * Math.sin(ang) }; });
  }
  return pos;
}

export function positionExploreAccumulate(view, vp, { prevPos, anchorId }) {
  const pos = {};
  for (const n of view.nodes) if (prevPos[n.id]) pos[n.id] = { ...prevPos[n.id] };
  const newNodes = view.nodes.filter(n => !prevPos[n.id]).map(n => n.id).sort();
  const a = prevPos[anchorId] || { x: 0, y: 0 }, r = 90;
  const occupied = Object.values(pos).map(p => Math.atan2(p.y - a.y, p.x - a.x));
  const isFree = ang => occupied.every(o => Math.abs(((ang - o + Math.PI) % TAU) - Math.PI) > 0.35);
  let placed = 0;
  for (let k = 0; k < 64 && placed < newNodes.length; k++) {
    const ang = -Math.PI / 2 + TAU * k / 16 + Math.floor(k / 16) * 0.2;
    if (!isFree(ang)) continue;
    pos[newNodes[placed++]] = { x: a.x + r * Math.cos(ang), y: a.y + r * Math.sin(ang) };
    occupied.push(ang);
  }
  for (; placed < newNodes.length; placed++) {           // 兜底：仍未放下的排外环
    const ang = TAU * placed / newNodes.length;
    pos[newNodes[placed]] = { x: a.x + (r + 60) * Math.cos(ang), y: a.y + (r + 60) * Math.sin(ang) };
  }
  return pos;
}
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && node --test viewer/tests/`
Expected: PASS。

- [ ] **Step 5: app.js 接入 explore + 锚定累积**——在 app.js：

维护跨 build 的位置缓存与 explore 状态：
```javascript
let lastPos = {};                 // 上一帧各节点 world 坐标，供跨 build 继承/累积
let exploreAnchor = null;         // 最近一次展开的锚节点 id（null=fresh/整理）
```
在 `draw()` 末尾或 `animateTo` 收敛后更新 `lastPos`（简单起见在 `build()` 定位后写入）。`LAYOUT` 加 explore 分支（在 build() 分流处特殊处理，因它依赖 prevPos）：
```javascript
function exploreTargets(view){
  const vp = viewport();
  if(exploreAnchor && Object.keys(lastPos).length)
    return positionExploreAccumulate(view, vp, { prevPos: lastPos, anchorId: exploreAnchor });
  return positionExploreFresh(view, vp, { seedId: "D:" + (cur.seed || "TU") });
}
```
在 build() 分流里，`det` 计算改为：`const targets = cur.v==="explore" ? exploreTargets(view) : det && det(view);`（`LAYOUT` 里给 explore 占位 `explore:true` 以走确定性分支）。定位后 `lastPos = {...targets}`。

改 `expandNode(code)`：保留其"选哪些新邻居入 `window.__expanded`"的优先级逻辑不变，仅在末尾设 `exploreAnchor = "D:"+code;` 再 `render()`；`render()`→`build()` 会用 accumulate 把新节点落 anchor 周围、旧节点原位。

fresh 进入/换种子：在 `$("#views")` 与 `$("#domSel")` 的 explore 分支里，展开前置 `exploreAnchor=null; lastPos={};`（强制走 Fresh 全新布局）。

- [ ] **Step 6: "整理"按钮**——explore 下点 `#physBtn`（此时文案"⤺ 整理"）触发 fresh 重排 + 补间：
```javascript
$("#physBtn").addEventListener("click",()=>{
  if(cur.v==="explore"){ exploreAnchor=null;
    const view=vExplore(cur.seed||"TU"), targets=positionExploreFresh(view, viewport(), {seedId:"D:"+(cur.seed||"TU")});
    lastPos={...targets}; animateTo(targets); return; }
  /* 非 explore 的旧物理暂停逻辑保留到 Task 7 */
});
```
（此监听替换现有 `#physBtn` 监听中 explore 相关部分；非 explore 分支 Task 7 清理。）

- [ ] **Step 7: 更新受影响的 pytest 断言**——`test_expand_follows_hard_edges_first` 仍应通过（`expandNode` 内 `relBySrc`/`confidence` 优先级保留）。若 `expandNode` 结构变动导致断言方式失效，改为断言新入口：
```python
def test_expand_anchors_accumulate():
    fn = V.TEMPLATE.split("function expandNode(code)")[1].split("\n}")[0]
    assert "relBySrc" in fn and "confidence" in fn      # 展开优先级不变
    assert "exploreAnchor" in fn                        # 锚定累积语义
```

- [ ] **Step 8: 重新生成 + 全测试 + 浏览器实证**

Run:
```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
.venv/bin/python scripts/build_kg_viewer.py && node --test viewer/tests/ && .venv/bin/python -m pytest scripts/tests/test_build_kg_viewer.py -q
```
Expected: 生成成功、node PASS、pytest 绿。
浏览器切"网状探索"（种子 TU）：**核心验收**——连续点 3-5 个域展开，**已展开节点纹丝不动**，新邻居从 anchor 周围淡入滑到位，**全程不炸开**；点"整理"→全体补间重排成雷达环；换种子→全新雷达。截图序列 `/tmp/kg_task6_explore_{1,2,3,tidy}.png`。

- [ ] **Step 9: Commit**

```bash
git add sdtm-rag/viewer/layout.mjs sdtm-rag/viewer/app.js sdtm-rag/viewer/tests/layout.test.mjs sdtm-rag/scripts/tests/test_build_kg_viewer.py
git commit -m "feat(kg-viewer): explore ego 雷达 + 锚定累积展开 + 整理(TDD, 不炸开)"
```

---

### Task 7: 退役物理

四视图都已确定性定位，删除物理引擎全部残留，统一跨 build 补间，收口 `#physBtn` 语义，重写物理相关 pytest。

**Files:**
- Modify: `sdtm-rag/viewer/app.js`
- Test: `sdtm-rag/scripts/tests/test_build_kg_viewer.py`（重写 `test_layout_comes_to_rest`）

**Interfaces:**
- Removes: `tick`、`frame`、`seed`、`REP/REST/SPRING/GRAV/DAMP/CENTER/ALPHA_MIN/alpha/running/raf` 及物理回退分支。
- Produces: `build()` 对所有视图走「定位 + 跨 build 补间」；`#physBtn` 仅 explore 显示为"⤺ 整理"，非 explore 隐藏。

- [ ] **Step 1: 删物理**——移除 `tick()`、`frame()`、`seed()`、物理常数与 `let N=[]...alpha=1,running=true,raf=0` 中的物理量（保留 `N/E/byId`）。`build()` 分流去掉 `else{...frame}` 物理回退，统一：
```javascript
function build(view){
  cancelAnimationFrame(tweenRAF);
  gEdges.textContent=""; gNodes.textContent="";
  N=view.nodes.map(n=>({...n})); byId=new Map(N.map(n=>[n.id,n]));
  E=view.edges.map(e=>({a:byId.get(e.s),b:byId.get(e.t),adv:e.adv,layer:e.layer,dir:e.dir,ev:e.ev})).filter(e=>e.a&&e.b);
  // ... 建边/节点 DOM（原样）...
  $("#count").textContent=N.length+" 节点 · "+E.length+" 边"; $("#sub").textContent=view.title;
  resetZoom();
  const targets = cur.v==="explore" ? exploreTargets(view) : LAYOUT[cur.v](view);
  for(const n of N){ const tg=targets[n.id]; const prev=lastPos[n.id];
    if(prev){ n.x=prev.x; n.y=prev.y; } else if(exploreAnchor&&lastPos[exploreAnchor]){ n.x=lastPos[exploreAnchor].x; n.y=lastPos[exploreAnchor].y; } else { n.x=tg.x; n.y=tg.y; } }
  draw(); animateTo(targets); lastPos={...targets};
  applyLayerToggles();
}
```
即：有旧位的节点从旧位补间到新位（视图切换/展开平滑），无旧位的新节点从 anchor（或直接到位）淡入。`LAYOUT` 恢复为纯函数表：`{overview,domain,impact}`（explore 走 `exploreTargets`）。

- [ ] **Step 2: 收口 `#physBtn`**——非 explore 视图隐藏该钮，explore 显示"⤺ 整理"。在 `syncUI()` 末尾加：`$("#physBtn").classList.toggle("hide", cur.v!=="explore"); if(cur.v==="explore")$("#physBtn").textContent="⤺ 整理";`。删除 `#physBtn` 监听里所有非 explore（物理暂停/继续）分支，只留 Task 6 的整理逻辑。删 `#fitBtn` 里的 `alpha=Math.max(...)`，只留 `resetZoom()`。

- [ ] **Step 3: 拖拽收口**——`startDrag` 去掉 `alpha=Math.max(alpha,.5)`；`up()` 去掉 `drag.fix=0`（无物理，fix 概念移除）；拖动直接改 `n.x/n.y` 并 `draw()`，落点即终点。移动中同步 `lastPos[n.id]={x:n.x,y:n.y}` 使后续 build 继承手动位置。

- [ ] **Step 4: 重写物理 pytest**——`test_layout_comes_to_rest` 依赖已删的 `alpha`/`ALPHA_MIN`，改为断言"无常驻物理、有补间收敛"：
```python
def test_no_persistent_physics():
    t = V.TEMPLATE
    assert "requestAnimationFrame(frame)" not in t      # 物理循环已删
    assert "function tick(" not in t and "function seed(" not in t
    assert "function animateTo(" in t                   # 补间引擎在
    assert "easeOutCubic" in t
```
`test_pan_reset_does_not_kill_node_click` 应仍通过（pointerup 行逻辑不变）；若 drag 收口改了该行，确保它仍不含 `drag` 重置。

- [ ] **Step 5: 全测试 + 浏览器回归**

Run:
```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
.venv/bin/python scripts/build_kg_viewer.py && node --test viewer/tests/ && .venv/bin/python -m pytest scripts/tests/test_build_kg_viewer.py -q
```
Expected: 全绿。浏览器四视图逐一回归：切换有平滑补间、无抖动、无报错；explore 展开/整理正常；拖拽落点保持。截图 `/tmp/kg_task7_{overview,domain,impact,explore}.png`。

- [ ] **Step 6: Commit**

```bash
git add sdtm-rag/viewer/app.js sdtm-rag/scripts/tests/test_build_kg_viewer.py
git commit -m "refactor(kg-viewer): 退役力导向物理, 统一跨 build 补间; 收口按钮与拖拽; 重写物理测试"
```

---

### Task 8: 精密仪器视觉系统

在 `style.css` + `template.html` 落地暗色优先的工程/仪表盘美学：发丝网格背景、信号色、等宽码值、标线环、边辉光、面板棱。结构 CSS 给定实值，像素级微调在本任务内对着截图迭代（明确的浏览器子循环，非占位）。

**Files:**
- Modify: `sdtm-rag/viewer/style.css`
- Modify: `sdtm-rag/viewer/template.html`（SVG 网格 `<pattern>` + defs）
- Modify: `sdtm-rag/viewer/app.js`（hover 标线环：给选中节点加/去 class）

**Interfaces:**
- Produces: CSS 变量 `--signal`、`--grid`、`--reticle`；`.node.sel` 标线环样式；`main` 网格背景。
- Consumes: 既有 `--c1..--c8`、`--surface/--ink/...`（保留）。

- [ ] **Step 1: 新增视觉变量（暗色优先，双主题）**——在 `:root`（亮）与暗色两处各加：

亮色 `:root`：
```css
--signal:#c77400; --grid:rgba(11,11,11,.04); --reticle:#c77400;
```
暗色（`@media` 与 `:root[data-theme="dark"]` 两块都加）：
```css
--signal:#f5b301; --grid:rgba(255,255,255,.05); --reticle:#f5b301;
```
> 信号色取琥珀系（落在 8 类色之外，避免与蓝/绿/紫语义边撞车）；第 3 步截图后如对比不足再调。

- [ ] **Step 2: 发丝网格背景**——template.html 的 `<svg>` defs 内（`<marker>` 旁）加网格 pattern，并在 `#vp` 前铺一层背景 rect：
```html
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
  <path d="M40 0H0V40" fill="none" stroke="var(--grid)" stroke-width="1"/>
</pattern>
```
在 `<g id="vp">` 内最底层加 `<rect id="gridbg" x="-6000" y="-6000" width="12000" height="12000" fill="url(#grid)"/>`（随平移缩放一起变换，营造坐标纸）。

- [ ] **Step 3: 节点/边/字体精修**——style.css：
  - 码值等宽：`#count, .legend, #panel .kv, #panel .chip.k, #sub { font-variant-numeric: tabular-nums; }`；域码/码号文本用等宽——给节点 label 里 code 类节点加 `.node.code text{font-family:ui-monospace,"SF Mono",monospace}`（app.js 已按 type 建节点，可在建 text 时按 `n.type` 加 class）。
  - 描边利落：`.node circle,.node rect{stroke-width:1.25}`。
  - 边发丝 + 高亮辉光：`.hl .edge{stroke:var(--signal);stroke-width:1.8}`；`.iedge`高亮时 `filter:drop-shadow(0 0 3px var(--signal))`（仅 `.hl` 态）。
  - 小标题小型大写 + 收紧字距：`#panel h4,.legend b{letter-spacing:.6px}`（已近似，微调）。

- [ ] **Step 4: 标线环(reticle)**——app.js `hover(n)` 里给 `n.g` 加 `sel` class、`unhover()` 去除；style.css：
```css
.node.sel > :first-child{ filter:drop-shadow(0 0 0 var(--reticle)); }
.node.sel::after{ }              /* SVG 无 ::after；改用 JS 画环 */
```
SVG 无伪元素，改在 hover 时于 `n.g` 内插一个 `<circle class="reticle" r="n.r+6" fill=none stroke=var(--reticle)>`、unhover 移除。（app.js 实现该插入/移除。）

- [ ] **Step 5: 面板/工具栏/图例仪表盘化**——style.css：
  - 面板棱：`#panel{border:1px solid var(--ring);box-shadow:0 8px 30px rgba(0,0,0,.28),inset 0 1px 0 rgba(255,255,255,.06)}`；减重毛玻璃 `backdrop-filter:blur(6px)`。
  - 分段控件激活：`.seg button.on{background:var(--signal);color:#000}`（暗色下琥珀配黑字）；亮色下 `color:#fff`——用变量或分主题覆盖。
  - `#count` 仪表读数：`#count{font-family:ui-monospace;letter-spacing:.5px;color:var(--ink2)}`。
  - 图例 key：`.legend b{color:var(--muted)}`（保留），swatch 描边 `1px var(--ring)`。

- [ ] **Step 6: 重新生成 + 明暗双主题实证迭代**

Run: `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && .venv/bin/python scripts/build_kg_viewer.py`
浏览器逐视图 × {亮, 暗}（主题钮切换）截图，对照验收：网格隐约可见不抢戏、信号色只在焦点/激活、码值等宽、标线环清晰、面板有仪表质感、CVD 类色未变。**若对比/层次不足，在本步内调 §Step1 实值与 §Step3/5 参数后重生成再看**，直至明暗都成立。截图 `/tmp/kg_task8_{view}_{light,dark}.png`（4×2=8 张）。

- [ ] **Step 7: Commit**

```bash
git add sdtm-rag/viewer/style.css sdtm-rag/viewer/template.html sdtm-rag/viewer/app.js
git commit -m "feat(kg-viewer): 精密仪器视觉系统(网格/信号色/等宽码值/标线环/面板棱, 明暗双主题)"
```

---

### Task 9: 面板 / 搜索 / hover 联动打磨

**Files:**
- Modify: `sdtm-rag/viewer/app.js`
- Modify: `sdtm-rag/viewer/style.css`

**Interfaces:**
- Consumes: 既有 `openPanel/openEvidence/applySearch/hover`；不改数据契约与 RAG/证据行为。

- [ ] **Step 1: 面板排版层次**——style.css：面板 `.pt` 字号/行高微增、`h4` 与内容间距规整、`.kv` 行距舒展、`.rel` 分隔用发丝 `border-top:1px solid var(--line)`；码值 `.chip.k` 等宽已在 Task 8。sticky 头：`#panel .ph{position:sticky;top:-14px;background:var(--panel);padding-top:14px;z-index:1}`。确认 RAG"深入解释"按钮、证据弹窗样式在新配色下可读。

- [ ] **Step 2: 搜索命中居中（可选增强）**——`applySearch()` 命中唯一或回车时，把首个命中节点补间到视口中心：加
```javascript
function centerOn(id){ const n=byId.get(id); if(!n)return; const r=svg.getBoundingClientRect();
  T.x=r.width/2 - n.x*T.k; T.y=r.height/2 - n.y*T.k; applyT(); }
$("#search").addEventListener("keydown",e=>{ if(e.key!=="Enter")return;
  const hit=N.find(n=>!n.g.classList.contains("dim")); if(hit)centerOn(hit.id); });
```

- [ ] **Step 3: hover 联动 + 标线环协同**——确认 Task 8 的 reticle 与既有 `dim`/`hl` 不冲突：hover 时非邻居 `dim`、焦点加 reticle、邻居边高亮辉光。`unhover` 全复位。浏览器验证无残留 class。

- [ ] **Step 4: 重新生成 + 实证**

Run: `cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && .venv/bin/python scripts/build_kg_viewer.py`
浏览器：点各类型节点看面板层次；搜索 "AE"/"C66" 回车居中；hover 联动 + 标线环；点推断边看证据弹窗；RAG 按钮（离线应隐藏）。截图 `/tmp/kg_task9_panel.png`。

- [ ] **Step 5: Commit**

```bash
git add sdtm-rag/viewer/app.js sdtm-rag/viewer/style.css
git commit -m "feat(kg-viewer): 面板排版层次 + 搜索命中居中 + hover 标线环协同"
```

---

### Task 10: 收尾验收（Rule D 隔离 + evidence + 收尾）

**Files:**
- Modify: `sdtm-rag/kg_viewer.html`（最终重新生成）
- Create: `sdtm-rag/evidence/checkpoints/kg_viewer_ux_redesign.md`
- Create: `docs/superpowers/plans/../../.../RETROSPECTIVE`（见下，随收尾）
- Modify: `docs/PROGRESS.md`、`.work/meta/worklog/<phase>.md`

- [ ] **Step 1: 最终重新生成 + 全绿**

Run:
```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
.venv/bin/python scripts/build_kg_viewer.py && node --test viewer/tests/ && .venv/bin/python -m pytest scripts/tests/test_build_kg_viewer.py -q
```
Expected: 生成成功、node 全 PASS、pytest 全绿。

- [ ] **Step 2: 验收矩阵截图**——服务 `:8010`，四视图 × 明暗 = 8 张主截图 + explore 展开序列 3 张 + 整理 1 张，存 `sdtm-rag/evidence/checkpoints/assets/`。逐项对照 spec §9 成功标准打勾。

- [ ] **Step 3: Rule D 独立核验**——派一个**不同 subagent（不同 session，如 code-reviewer/verifier）**，只给它截图与 spec §9，让它独立判"是否炸开/位置是否稳定/精密仪器性格是否成立/明暗是否都可读/有无回归"，产出业务 PASS/FAIL。结论写入 checkpoint。**不自审。**

- [ ] **Step 4: 写 evidence checkpoint**——`sdtm-rag/evidence/checkpoints/kg_viewer_ux_redesign.md`：记录改动摘要、验收矩阵结果、Rule D 结论、node/pytest 输出、console 干净证据、已知限制。

- [ ] **Step 5: 失败归档(Rule B)**——把过程中被否的布局/视觉 attempt（若有）整理进 `sdtm-rag/failures/`（或 evidence 下 failures 子目录），不删。

- [ ] **Step 6: RETROSPECTIVE(Rule C 三段)**——写保留的做法 / 必补的缺口 / 关键决策复盘（垂直切片、纯函数可测、退役物理时机、源码拆分收益）。位置随项目惯例（如 `docs/superpowers/` 或 milestone 下）。

- [ ] **Step 7: 收尾（走项目 CLAUDE.md 收尾清单）**——更新 `docs/PROGRESS.md`（加 SP7 milestone 状态）、`.work/meta/worklog/<phase>.md`（append 本次记录）；CLAUDE.md Key Paths 若需加 `viewer/` 源码指针则加一行（≤80 字符）。最终 commit + push。

```bash
git add -A
git commit -m "docs(kg-viewer): SP7 UX 重构收尾 — evidence/RETROSPECTIVE/PROGRESS/worklog"
```

---

## Self-Review

**Spec coverage（spec §→task 映射）:**
- §1.3 决策 1-7 → 分散落实：布局 B(Task 2-7)、保留 4 视图(Task 3-6)、精密仪器(Task 8)、锚定累积(Task 6)。
- §2 源码拆分 → Task 1。
- §3.1/3.2/3.3/3.4 四布局 → Task 2/4/5/6。
- §4 补间/退役物理 → Task 3(引擎) + Task 7(退役)。
- §5 视觉系统 → Task 8。
- §6 面板/搜索/hover → Task 9。
- §7 U0-U8 单元 → Task 1-10 全覆盖。
- §8 测试核验（确定性/浏览器/Rule A·B·C·D）→ Task 内 node/pytest + Task 10 Rule D/B/C。
- §9 成功标准 → Task 10 验收矩阵逐项。
- §10 开放问题（信号色/变量分列/补间手感）→ Task 8 Step6 迭代 / Task 4 分列 / Task 3·7 补间实测。

**Placeholder scan:** 无 TBD/TODO；视觉像素微调在 Task 8 Step6 显式标为"对截图迭代"的浏览器子循环，附起始实值，非隐藏占位。

**Type consistency:** `positionOverview/Domain/Impact/ExploreFresh/ExploreAccumulate` 全返回 `{[id]:{x,y}}`；`animateTo(targets)` 消费同形；`lastPos/exploreAnchor` 在 Task 6 引入、Task 7 消费，命名一致；`LAYOUT` 表在 Task 3/4/5 累加、Task 7 定稿（explore 走 `exploreTargets` 而非表项，已在 Task 7 Step1 明确）。

**已知取舍:** Task 3-6 期间 explore 之外视图先确定性、explore 在 Task 6 才接入，其间物理仅残留于"未注册视图"回退分支，Task 7 清除——每个 task 结束时 app 都可用。
