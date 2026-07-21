"""Build a self-contained interactive SDTM knowledge-graph viewer (single HTML).

Source of truth: data/meta/meta.yaml (via build_neo4j.extract_graph — pure, no
Neo4j). Emits kg_viewer.html: a zero-dependency, offline, shareable page with a
hand-rolled force-directed graph and three scoped, readable views:

  1. 结构总览   Class (8) -> Domain (63)          [IN_CLASS]
  2. 域钻取     a Domain -> its Variables -> Codelists  [HAS_VARIABLE / USES_CT]
  3. 码表影响   a Codelist -> the Domains that use it   [USES_CT aggregated]

Colors: the dataviz reference categorical palette (validated CVD-safe) for the 8
SDTM classes; node TYPE encoded by shape+size (no 9th hue). Light/dark themed.

Run:  cd sdtm-rag && .venv/bin/python scripts/build_kg_viewer.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # scripts -> sdtm-rag
IMPL_PATH = ROOT / "data" / "meta" / "implicit_relations.json"
sys.path.insert(0, str(ROOT / "scripts"))

from build_neo4j import extract_graph, load_meta  # noqa: E402  (pure, no neo4j import)


def build_data() -> dict:
    graph = extract_graph(load_meta(ROOT / "data" / "meta" / "meta.yaml"))
    nodes, edges = graph["nodes"], graph["edges"]

    classes = [{"name": c["name"], "n": c["n_domains"]} for c in nodes["Class"]]
    domains = [
        {"code": d["code"], "label": d["label"], "cls": d["class"],
         "struct": d["structure"], "nv": d["n_variables"]}
        for d in nodes["Domain"]
    ]

    has_var = [[e["domain"], e["var"]] for e in edges["HAS_VARIABLE"]]
    uses_ct = [[e["var"], e["code"], e["domains"]] for e in edges["USES_CT"]]

    # variable label/role/core only for names actually shown (in a domain)
    shown_vars = {v for _, v in has_var} | {u[0] for u in uses_ct}
    var_info: dict[str, dict] = {}
    for v in nodes["Variable"]:
        if v["name"] in shown_vars:
            var_info[v["name"]] = {
                "l": v.get("label", v["name"]),
                "r": v.get("role", ""),
                "c": v.get("core", ""),
            }

    ref_codes = {u[1] for u in uses_ct}
    cls_codes = {
        c["code"]: {"n": c["name"], "e": bool(c["extensible"]), "t": c["term_count"]}
        for c in nodes["Codelist"] if c["code"] in ref_codes
    }

    # curated inter-domain relations (RELATED_TO) for the click-to-inspect panel
    related = [
        [e["src"], e["dst"], e.get("mechanism") or "", e.get("category") or "", e.get("note") or ""]
        for e in edges["RELATED_TO"]
    ]

    implicit = None
    if IMPL_PATH.exists():
        raw = json.loads(IMPL_PATH.read_text(encoding="utf-8"))
        implicit = {"domains": raw["meta"]["domains"],
                    "edges": [e for e in raw["edges"]]}  # 已含 evidence/confidence/kind

    return {
        "classes": classes,
        "domains": domains,
        "vars": var_info,
        "hasVar": has_var,
        "usesCt": uses_ct,
        "clsCodes": cls_codes,
        "related": related,
        "implicit": implicit,
        "counts": {
            "domain": len(domains), "variable": len(nodes["Variable"]),
            "codelist": len(nodes["Codelist"]), "cls": len(classes),
        },
    }


TEMPLATE = r"""<!doctype html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SDTM 知识图谱</title>
<style>
:root{
  --surface:#fcfcfb; --plane:#f9f9f7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --line:#e1e0d9; --ring:rgba(11,11,11,.10); --panel:#ffffffcc; --nodeStroke:#fcfcfb;
  --varFill:#b9b7ad; --codeFill:#6f6d78; --codeStroke:#4a4954;
  --c1:#2a78d6;--c2:#1baf7a;--c3:#eda100;--c4:#008300;--c5:#4a3aa7;--c6:#e34948;--c7:#e87ba4;--c8:#eb6834;
  --flow:#2a78d6; --link:#1baf7a; --cooc:#7a52c7;
}
:root[data-theme="dark"], :root:not([data-theme="light"]){}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --surface:#1a1a19; --plane:#0d0d0d; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781;
    --line:#2c2c2a; --ring:rgba(255,255,255,.10); --panel:#222220e6; --nodeStroke:#1a1a19;
    --varFill:#6a6862; --codeFill:#9d9ba8; --codeStroke:#c9c7d4;
    --c1:#3987e5;--c2:#199e70;--c3:#c98500;--c4:#008300;--c5:#9085e9;--c6:#e66767;--c7:#d55181;--c8:#d95926;
    --flow:#3987e5; --link:#199e70; --cooc:#9085e9;
  }
}
:root[data-theme="dark"]{
  --surface:#1a1a19; --plane:#0d0d0d; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781;
  --line:#2c2c2a; --ring:rgba(255,255,255,.10); --panel:#222220e6; --nodeStroke:#1a1a19;
  --varFill:#6a6862; --codeFill:#9d9ba8; --codeStroke:#c9c7d4;
  --c1:#3987e5;--c2:#199e70;--c3:#c98500;--c4:#008300;--c5:#9085e9;--c6:#e66767;--c7:#d55181;--c8:#d95926;
  --flow:#3987e5; --link:#199e70; --cooc:#9085e9;
}
*{box-sizing:border-box}
html,body{margin:0;height:100%}
body{background:var(--plane);color:var(--ink);
  font-family:system-ui,-apple-system,"Segoe UI",sans-serif;overflow:hidden}
#app{display:flex;flex-direction:column;height:100vh}
header{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;
  padding:10px 16px;background:var(--surface);border-bottom:1px solid var(--line)}
h1{font-size:15px;margin:0;font-weight:700;letter-spacing:.2px}
h1 small{color:var(--muted);font-weight:500;margin-left:8px;font-size:12px}
.seg{display:inline-flex;border:1px solid var(--ring);border-radius:8px;overflow:hidden}
.seg button{border:0;background:transparent;color:var(--ink2);padding:6px 12px;
  font-size:13px;cursor:pointer;font-family:inherit}
.seg button+button{border-left:1px solid var(--ring)}
.seg button.on{background:var(--c1);color:#fff;font-weight:600}
select,input[type=search]{font-family:inherit;font-size:13px;color:var(--ink);
  background:var(--surface);border:1px solid var(--ring);border-radius:8px;padding:6px 9px}
select{max-width:230px}
input[type=search]{width:180px}
.spacer{flex:1}
.ghost{border:1px solid var(--ring);background:transparent;color:var(--ink2);
  border-radius:8px;padding:6px 10px;font-size:13px;cursor:pointer;font-family:inherit}
.ghost:hover{color:var(--ink)}
.hide{display:none!important}
main{position:relative;flex:1;overflow:hidden;background:var(--surface)}
svg{width:100%;height:100%;display:block;cursor:grab}
svg.panning{cursor:grabbing}
.edge{stroke:var(--line);stroke-width:1.4}
.edge.adv{stroke-dasharray:4 3}
.edge.hardrel{stroke:var(--ink2);stroke-width:1.6}
.iedge{fill:none}
.iedge.flow{stroke:var(--flow,#2a78d6);stroke-width:2.2}
.iedge.link{stroke:var(--link,#1baf7a);stroke-width:2.2;stroke-dasharray:5 3}
.iedge.cooc{stroke:var(--cooc,#7a52c7);stroke-width:2;stroke-dasharray:1 5;stroke-linecap:round}
.iedge-arrow{fill:var(--flow,#2a78d6)}
.node{cursor:pointer}
.node text{fill:var(--ink);font-size:10px;paint-order:stroke;
  stroke:var(--surface);stroke-width:3px;stroke-linejoin:round;pointer-events:none;user-select:none}
.node.big text{font-size:12px;font-weight:700}
.node circle,.node rect{stroke:var(--nodeStroke);stroke-width:1.5}
.dim{opacity:.12;transition:opacity .12s}
.dim text{opacity:0}
.hl .edge{stroke:var(--ink2);stroke-width:2}
.legend{position:absolute;left:12px;bottom:12px;background:var(--panel);
  backdrop-filter:blur(6px);border:1px solid var(--ring);border-radius:10px;
  padding:10px 12px;font-size:12px;max-width:210px;line-height:1.7}
.legend b{display:block;font-size:11px;color:var(--muted);text-transform:uppercase;
  letter-spacing:.5px;margin:2px 0 4px}
.legend .row{display:flex;align-items:center;gap:7px;color:var(--ink2)}
.sw{width:12px;height:12px;border-radius:50%;flex:none;border:1px solid var(--ring)}
.sw.dom{border-radius:50%}
.sw.sq{border-radius:3px}
.shape{width:16px;text-align:center;flex:none;color:var(--muted)}
.hint{position:absolute;right:12px;bottom:12px;background:var(--panel);
  border:1px solid var(--ring);border-radius:8px;padding:7px 11px;font-size:11px;color:var(--muted)}
#tip{position:fixed;pointer-events:none;z-index:20;background:var(--panel);
  backdrop-filter:blur(6px);border:1px solid var(--ring);border-radius:8px;
  padding:8px 10px;font-size:12px;max-width:280px;color:var(--ink);
  box-shadow:0 4px 16px rgba(0,0,0,.18);opacity:0;transition:opacity .1s}
#tip .t{font-weight:700;margin-bottom:2px}
#tip .m{color:var(--muted);font-size:11px}
#tip kbd{color:var(--ink2)}
#count{position:absolute;left:12px;top:12px;font-size:12px;color:var(--muted);
  background:var(--panel);border:1px solid var(--ring);border-radius:8px;padding:5px 9px}
#panel{position:absolute;top:12px;right:12px;width:300px;max-height:calc(100% - 24px);overflow:auto;
  background:var(--panel);backdrop-filter:blur(8px);border:1px solid var(--ring);border-radius:12px;
  padding:14px 16px;font-size:13px;box-shadow:0 8px 30px rgba(0,0,0,.18);z-index:15}
#panel .ph{display:flex;align-items:flex-start;gap:8px;margin-bottom:8px}
#panel .pt{font-size:16px;font-weight:700;line-height:1.2}
#panel .pty{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px}
#panel .x{margin-left:auto;cursor:pointer;color:var(--muted);border:0;background:none;font-size:20px;line-height:1;padding:0 2px}
#panel .x:hover{color:var(--ink)}
#panel h4{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin:13px 0 5px}
#panel .kv{color:var(--ink2);line-height:1.75}
#panel .kv b{color:var(--ink);font-weight:600}
#panel .chips{display:flex;flex-wrap:wrap;gap:4px}
#panel .chip{font-size:11px;padding:2px 7px;border:1px solid var(--ring);border-radius:20px;
  color:var(--ink2);cursor:pointer;background:var(--surface);white-space:nowrap}
#panel .chip:hover{color:var(--ink);border-color:var(--ink2)}
#panel .chip.k{font-family:ui-monospace,"SF Mono",monospace}
#panel .rel{padding:6px 0;border-top:1px solid var(--line)}
#panel .rel .m{color:var(--muted);font-size:11px;margin-top:2px}
#panel .m{color:var(--muted);font-size:11px;margin-top:4px}
#panel .adv{font-size:10px;color:var(--muted)}
#panel .q{margin:8px 0;padding:8px 10px;border-left:3px solid var(--c1);background:var(--surface);
  color:var(--ink2);font-size:12.5px;line-height:1.6;font-style:italic}
#panel .tag{font-size:10px;padding:1px 7px;border-radius:10px;color:#fff;display:inline-block;font-weight:600}
#panel .tag.flow{background:var(--flow)}
#panel .tag.link{background:var(--link)}
#panel .tag.cooc{background:var(--cooc)}
#panel .ragBtn{font-size:10px;margin-left:6px;padding:2px 9px;border:1px solid var(--ring);border-radius:20px;
  background:var(--surface);color:var(--ink2);cursor:pointer;font-family:inherit}
#panel .ragBtn:hover{color:var(--ink);border-color:var(--ink2)}
#panel .ragBtn:disabled{opacity:.55;cursor:default}
#panel .ragans{margin:8px 0;padding:8px 10px;background:var(--surface);border:1px solid var(--ring);
  border-radius:8px;font-size:12px;color:var(--ink2);line-height:1.6}
#panel .irel{cursor:pointer}
#panel .irel:hover{background:var(--surface)}
</style>
</head>
<body>
<div id="app">
  <header>
    <h1>SDTM 知识图谱 <small id="sub"></small></h1>
    <div class="seg" id="views">
      <button data-v="overview" class="on">结构总览</button>
      <button data-v="domain">域钻取</button>
      <button data-v="impact">码表影响</button>
      <button data-v="explore">网状探索</button>
    </div>
    <select id="domSel" class="hide"></select>
    <select id="codeSel" class="hide"></select>
    <div class="seg hide" id="layers" title="图层开关：硬关联(实线) · 数据流(实线+箭头) · 显式链接(虚线) · 共现(点线)">
      <button data-l="hard" class="on">硬关联 —</button>
      <button data-l="flow" class="on">数据流 →</button>
      <button data-l="link" class="on">显式链接 ╌</button>
      <button data-l="cooc" class="on">共现 ┄</button>
    </div>
    <input id="search" type="search" placeholder="搜索 code / name…">
    <div class="spacer"></div>
    <button class="ghost" id="physBtn" title="暂停/继续布局">⏸ 布局</button>
    <button class="ghost" id="fitBtn" title="重置缩放">⤢ 复位</button>
    <button class="ghost" id="themeBtn" title="切换主题">◐ 主题</button>
  </header>
  <main>
    <svg id="svg"><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path class="iedge-arrow" d="M0,0L10,5L0,10z"></path></marker></defs><g id="vp"><g id="edges"></g><g id="nodes"></g></g></svg>
    <div id="count"></div>
    <div class="legend" id="legend"></div>
    <div class="hint" id="hint">悬停看全名 · 点击节点看关系 · 拖拽 · 滚轮缩放 · 空白平移</div>
    <aside id="panel" class="hide"></aside>
  </main>
</div>
<div id="tip"></div>
<script>
const DATA = __DATA__;
const CLASS_ORDER=["Special-Purpose","Interventions","Events","Findings","Findings About","Trial Design","Relationship","Study Reference"];
const $=s=>document.querySelector(s);
const svg=$("#svg"),vp=$("#vp"),gEdges=$("#edges"),gNodes=$("#nodes"),tip=$("#tip");
const SVGNS="http://www.w3.org/2000/svg";

function isDark(){const t=document.documentElement.dataset.theme;
  if(t==="dark")return true; if(t==="light")return false;
  return matchMedia("(prefers-color-scheme: dark)").matches;}
function classColor(cls){const i=CLASS_ORDER.indexOf(cls);
  return i>=0?getComputedStyle(document.documentElement).getPropertyValue("--c"+(i+1)).trim():"#898781";}
function cvar(n){return getComputedStyle(document.documentElement).getPropertyValue(n).trim();}

// ---- indexes ----
const domByCode=new Map(DATA.domains.map(d=>[d.code,d]));
const varsByDomain=new Map();
for(const [dm,v] of DATA.hasVar){ if(!varsByDomain.has(dm))varsByDomain.set(dm,[]); varsByDomain.get(dm).push(v); }
const ctByVar=new Map();
for(const [v,code,doms] of DATA.usesCt){ if(!ctByVar.has(v))ctByVar.set(v,[]); ctByVar.get(v).push([code,doms]); }
const codeDomains=new Map(), codeVars=new Map();
for(const [v,code,doms] of DATA.usesCt){
  if(!codeDomains.has(code))codeDomains.set(code,new Set());
  doms.forEach(d=>codeDomains.get(code).add(d));
  if(!codeVars.has(code))codeVars.set(code,new Set()); codeVars.get(code).add(v);
}
const domainsByVar=new Map();
for(const [dm,v] of DATA.hasVar){ if(!domainsByVar.has(v))domainsByVar.set(v,[]); domainsByVar.get(v).push(dm); }
const relBySrc=new Map();
for(const e of (DATA.related||[])){ if(!relBySrc.has(e[0]))relBySrc.set(e[0],[]); relBySrc.get(e[0]).push({d:e[1],mech:e[2],cat:e[3],note:e[4]}); }
const implicitEdges=(DATA.implicit&&DATA.implicit.edges)?DATA.implicit.edges:[];
const implicitById=new Map(implicitEdges.map(e=>[e.id,e]));
const implicitByDomain=new Map();
for(const e of implicitEdges){
  if(!implicitByDomain.has(e.source))implicitByDomain.set(e.source,[]); implicitByDomain.get(e.source).push(e);
  if(e.target!==e.source){ if(!implicitByDomain.has(e.target))implicitByDomain.set(e.target,[]); implicitByDomain.get(e.target).push(e); }
}

// ---- view builders -> {nodes:[{id,type,label,full,cls,r}], edges:[{s,t,adv}]} ----
function vOverview(){
  const nodes=[],edges=[];
  for(const c of DATA.classes) nodes.push({id:"C:"+c.name,type:"class",label:c.name,full:c.name+" · "+c.n+" 域",cls:c.name,r:17});
  for(const d of DATA.domains){ nodes.push({id:"D:"+d.code,type:"domain",label:d.code,full:d.code+" — "+d.label,cls:d.cls,r:9});
    edges.push({s:"D:"+d.code,t:"C:"+d.cls}); }
  return {nodes,edges,title:"8 个观测类 → 63 个域（按类配色）"};
}
function vDomain(code){
  const d=domByCode.get(code); if(!d)return vOverview();
  const nodes=[{id:"D:"+code,type:"domain",label:code,full:code+" — "+d.label,cls:d.cls,r:16,big:1}],edges=[];
  const seenK=new Set();
  for(const v of (varsByDomain.get(code)||[])){
    const vi=DATA.vars[v]||{l:v};
    nodes.push({id:"V:"+v,type:"var",label:v,full:v+" — "+(vi.l||"")+(vi.c?"  ["+vi.c+"]":""),r:5});
    edges.push({s:"D:"+code,t:"V:"+v});
    for(const [cc,doms] of (ctByVar.get(v)||[])){
      if(!doms.includes(code))continue;
      if(!seenK.has(cc)){ const ci=DATA.clsCodes[cc]||{n:""};
        nodes.push({id:"K:"+cc,type:"code",label:cc,full:cc+" — "+ci.n+(ci.e?"  (可扩展)":"")+"  · "+(codeDomains.get(cc)?codeDomains.get(cc).size:"?")+" 域",r:9}); seenK.add(cc); }
      edges.push({s:"V:"+v,t:"K:"+cc});
    }
  }
  return {nodes,edges,title:code+" — "+d.label+"　("+(varsByDomain.get(code)||[]).length+" 变量, "+seenK.size+" 码表)"};
}
function vImpact(code){
  const ci=DATA.clsCodes[code]; if(!ci)return vOverview();
  const doms=[...(codeDomains.get(code)||[])].sort();
  const nodes=[{id:"K:"+code,type:"code",label:code,full:code+" — "+ci.n+(ci.e?"  (可扩展)":""),r:18,big:1}],edges=[];
  for(const dm of doms){ const d=domByCode.get(dm);
    nodes.push({id:"D:"+dm,type:"domain",label:dm,full:dm+(d?" — "+d.label:""),cls:d?d.cls:"",r:9});
    edges.push({s:"D:"+dm,t:"K:"+code}); }
  return {nodes,edges,title:code+" “"+ci.n+"” 波及 "+doms.length+" 个域 / "+(codeVars.get(code)?codeVars.get(code).size:0)+" 个变量"};
}
const IMPLICIT_LAYER={data_flow:"flow",explicit_link:"link",co_occurrence:"cooc"};
const EXPLORE_CAP=40; // anti-hairball ceiling: max domains shown at once in explore view
function vExplore(seed){
  window.__expanded=window.__expanded||new Set();
  const shown=new Set([seed]); window.__expanded.forEach(x=>shown.add(x));
  const nodes=[],edges=[],have=new Set();
  const add=(code,big)=>{ const id="D:"+code; if(have.has(id))return; have.add(id);
    const d=domByCode.get(code); if(!d)return;
    nodes.push({id,type:"domain",label:code,full:code+" — "+d.label,cls:d.cls,r:big?14:12,big:big?1:0}); };
  for(const code of shown) add(code,code===seed);
  // 硬结构层: curated RELATED_TO, only among shown nodes (Task 7 relBySrc)
  for(const [s,list] of relBySrc) if(shown.has(s)) for(const r of list) if(shown.has(r.d)){
    edges.push({s:"D:"+s,t:"D:"+r.d,layer:"hard"}); }
  // 推断层: DATA.implicit edges (data_flow / explicit_link / co_occurrence), only among shown nodes
  for(const e of (DATA.implicit?DATA.implicit.edges:[])) if(shown.has(e.source)&&shown.has(e.target)){
    edges.push({s:"D:"+e.source,t:"D:"+e.target,layer:IMPLICIT_LAYER[e.kind],dir:e.directed,ev:e}); }
  return {nodes,edges,title:"网状探索 · 从 "+seed+" 展开（"+shown.size+" 域，上限 "+EXPLORE_CAP+"）"};
}
function expandNode(code){
  window.__expanded=window.__expanded||new Set();
  const shownCount=()=>new Set([cur.seed||"TU",...window.__expanded]).size;
  if(shownCount()>=EXPLORE_CAP){ cur.v="explore"; render(); return; } // cap already hit: no new nodes
  window.__expanded.add(code);
  const tryAdd=x=>{ if(shownCount()<EXPLORE_CAP) window.__expanded.add(x); };
  // 展开优先级 (spec §5): 硬边邻居 > 推断邻居按置信度降序
  for(const [s,list] of relBySrc) for(const r of list){
    if(s===code) tryAdd(r.d); else if(r.d===code) tryAdd(s); }
  const impl=(DATA.implicit?DATA.implicit.edges:[]).slice().sort((a,b)=>(b.confidence||0)-(a.confidence||0));
  for(const e of impl){
    if(e.source===code) tryAdd(e.target); else if(e.target===code) tryAdd(e.source); }
  cur.v="explore"; render();
}

// ---- force simulation ----
let N=[],E=[],byId=new Map(),alpha=1,running=true,raf=0;
const REP=11000,REST=94,SPRING=.045,GRAV=.011,DAMP=.88,CENTER={x:0,y:0},ALPHA_MIN=0.001;
function seed(nodes){
  const R=Math.min(innerWidth,innerHeight)*0.44;
  nodes.forEach((n,i)=>{const a=i*2.399963;const r=R*Math.sqrt((i+1)/nodes.length);
    n.x=CENTER.x+r*Math.cos(a); n.y=CENTER.y+r*Math.sin(a); n.vx=0; n.vy=0;});
}
function tick(){
  const n=N.length;
  for(let i=0;i<n;i++){const a=N[i]; if(a.fix)continue;
    for(let j=i+1;j<n;j++){const b=N[j];
      let dx=a.x-b.x,dy=a.y-b.y,d2=dx*dx+dy*dy||.01; if(d2>500000)continue;
      const f=REP*alpha/d2,dd=Math.sqrt(d2),fx=dx/dd*f,fy=dy/dd*f;
      a.vx+=fx;a.vy+=fy; if(!b.fix){b.vx-=fx;b.vy-=fy;} }
  }
  for(const e of E){const a=e.a,b=e.b; let dx=b.x-a.x,dy=b.y-a.y,dd=Math.hypot(dx,dy)||.01;
    const f=(dd-REST)*SPRING*alpha,fx=dx/dd*f,fy=dy/dd*f;
    if(!a.fix){a.vx+=fx;a.vy+=fy;} if(!b.fix){b.vx-=fx;b.vy-=fy;} }
  for(const a of N){ if(a.fix)continue;
    a.vx+=(CENTER.x-a.x)*GRAV*alpha; a.vy+=(CENTER.y-a.y)*GRAV*alpha;
    a.vx*=DAMP; a.vy*=DAMP; a.x+=a.vx; a.y+=a.vy; }
  alpha*=0.985;
}
function frame(){ if(running&&alpha>ALPHA_MIN){ for(let k=0;k<2;k++)tick(); draw(); } raf=requestAnimationFrame(frame); }

// ---- render ----
function draw(){
  for(const e of E){
    if(e.isPath) e.el.setAttribute("d","M"+e.a.x+","+e.a.y+"L"+e.b.x+","+e.b.y);
    else { e.el.setAttribute("x1",e.a.x);e.el.setAttribute("y1",e.a.y);
      e.el.setAttribute("x2",e.b.x);e.el.setAttribute("y2",e.b.y); }
  }
  for(const n of N) n.g.setAttribute("transform","translate("+n.x+","+n.y+")");
}
function makeNodeShape(n){
  if(n.type==="code"){ const s=n.r; const r=document.createElementNS(SVGNS,"rect");
    r.setAttribute("x",-s);r.setAttribute("y",-s);r.setAttribute("width",2*s);r.setAttribute("height",2*s);
    r.setAttribute("rx",3); r.setAttribute("transform","rotate(45)");
    r.setAttribute("fill",cvar("--codeFill")); r.setAttribute("stroke",cvar("--codeStroke")); return r; }
  const c=document.createElementNS(SVGNS,"circle"); c.setAttribute("r",n.r);
  if(n.type==="var") c.setAttribute("fill",cvar("--varFill"));
  else c.setAttribute("fill",classColor(n.cls));
  return c;
}
function build(view){
  cancelAnimationFrame(raf);
  gEdges.textContent=""; gNodes.textContent="";
  N=view.nodes.map(n=>({...n})); byId=new Map(N.map(n=>[n.id,n]));
  E=view.edges.map(e=>({a:byId.get(e.s),b:byId.get(e.t),adv:e.adv,layer:e.layer,dir:e.dir,ev:e.ev})).filter(e=>e.a&&e.b);
  seed(N);
  for(const e of E){
    let l;
    if(e.layer&&e.layer!=="hard"){
      l=document.createElementNS(SVGNS,"path"); l.setAttribute("class","iedge "+e.layer);
      if(e.dir) l.setAttribute("marker-end","url(#arrow)");
      e.isPath=true;
    } else {
      l=document.createElementNS(SVGNS,"line");
      l.setAttribute("class","edge"+(e.adv?" adv":"")+(e.layer==="hard"?" hardrel":""));
    }
    e.el=l; gEdges.appendChild(l);
  }
  for(const n of N){ const g=document.createElementNS(SVGNS,"g");
    g.setAttribute("class","node"+(n.big?" big":"")); n.g=g;
    g.appendChild(makeNodeShape(n));
    const t=document.createElementNS(SVGNS,"text");
    t.setAttribute("y",n.r+11); t.setAttribute("text-anchor","middle"); t.textContent=n.label;
    g.appendChild(t);
    g.addEventListener("pointerenter",ev=>hover(n,ev));
    g.addEventListener("pointermove",ev=>moveTip(ev));
    g.addEventListener("pointerleave",()=>unhover());
    g.addEventListener("pointerdown",ev=>startDrag(n,ev));
    gNodes.appendChild(g);
  }
  $("#count").textContent=N.length+" 节点 · "+E.length+" 边";
  $("#sub").textContent=view.title;
  alpha=1; running=true; $("#physBtn").textContent="⏸ 布局";
  resetZoom(); raf=requestAnimationFrame(frame);
  applyLayerToggles();
}

// ---- hover / tooltip / highlight ----
function neighbors(n){const s=new Set([n.id]); for(const e of E){ if(e.a===n)s.add(e.b.id); if(e.b===n)s.add(e.a.id);} return s;}
function hover(n,ev){ const keep=neighbors(n);
  for(const m of N) m.g.classList.toggle("dim",!keep.has(m.id));
  for(const e of E) e.el.classList.toggle("dim",!(e.a===n||e.b===n));
  gNodes.parentNode.classList.add("hl");
  const tName={class:"观测类",domain:"域",var:"变量",code:"码表"}[n.type];
  tip.innerHTML='<div class="t">'+esc(n.label)+'</div><div class="m">'+tName+' · '+esc(n.full||"")+'</div>';
  tip.style.opacity=1; moveTip(ev);
}
function moveTip(ev){ const p=12; let x=ev.clientX+p,y=ev.clientY+p;
  const b=tip.getBoundingClientRect(); if(x+b.width>innerWidth)x=ev.clientX-b.width-p;
  if(y+b.height>innerHeight)y=ev.clientY-b.height-p; tip.style.left=x+"px"; tip.style.top=y+"px"; }
function unhover(){ for(const m of N)m.g.classList.remove("dim"); for(const e of E)e.el.classList.remove("dim");
  gNodes.parentNode.classList.remove("hl"); tip.style.opacity=0; applySearch(); }
function esc(s){return (s+"").replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));}

// ---- zoom / pan ----
let T={k:1,x:0,y:0};
function applyT(){ vp.setAttribute("transform","translate("+T.x+","+T.y+") scale("+T.k+")"); }
function resetZoom(){ const r=svg.getBoundingClientRect(); T={k:1,x:r.width/2,y:r.height/2}; CENTER.x=0;CENTER.y=0; applyT(); }
svg.addEventListener("wheel",ev=>{ ev.preventDefault(); const r=svg.getBoundingClientRect();
  const mx=ev.clientX-r.left,my=ev.clientY-r.top; const s=Math.exp(-ev.deltaY*0.0015);
  const k=Math.max(.15,Math.min(4,T.k*s)); T.x=mx-(mx-T.x)*(k/T.k); T.y=my-(my-T.y)*(k/T.k); T.k=k; applyT(); },{passive:false});
let pan=null;
svg.addEventListener("pointerdown",ev=>{ if(ev.target.closest(".node"))return;
  pan={x:ev.clientX,y:ev.clientY,tx:T.x,ty:T.y}; svg.classList.add("panning"); });
addEventListener("pointermove",ev=>{ if(!pan)return; T.x=pan.tx+(ev.clientX-pan.x); T.y=pan.ty+(ev.clientY-pan.y); applyT(); });
addEventListener("pointerup",()=>{ pan=null; svg.classList.remove("panning"); });

// ---- node drag ----
let drag=null;
function startDrag(n,ev){ ev.stopPropagation(); drag=n; n.fix=1;
  const sx=ev.clientX,sy=ev.clientY; let moved=0;
  const move=e=>{ if(!drag)return; moved=Math.max(moved,Math.hypot(e.clientX-sx,e.clientY-sy));
    const r=svg.getBoundingClientRect();
    n.x=(e.clientX-r.left-T.x)/T.k; n.y=(e.clientY-r.top-T.y)/T.k; alpha=Math.max(alpha,.5); };
  const up=()=>{ if(drag){drag.fix=0; if(moved<4){ if(cur.v==="explore"&&n.type==="domain")expandNode(n.label); else openPanel(n); } drag=null;} removeEventListener("pointermove",move); removeEventListener("pointerup",up); };
  addEventListener("pointermove",move); addEventListener("pointerup",up);
}

// ---- search ----
function applySearch(){ const q=$("#search").value.trim().toLowerCase(); if(!q){ for(const n of N)n.g.classList.remove("dim"); return; }
  for(const n of N){ const hit=(n.label+" "+(n.full||"")).toLowerCase().includes(q); n.g.classList.toggle("dim",!hit); } }
$("#search").addEventListener("input",applySearch);

// ---- controls ----
let cur={v:"overview",dom:"AE",code:null,seed:"TU"};
function render(){
  closePanel(); syncUI();
  let view; if(cur.v==="overview")view=vOverview();
  else if(cur.v==="domain")view=vDomain(cur.dom);
  else if(cur.v==="explore")view=vExplore(cur.seed||"TU");
  else view=vImpact(cur.code);
  build(view); applySearch();
}
function syncUI(){
  for(const x of $("#views").children) x.classList.toggle("on",x.dataset.v===cur.v);
  $("#domSel").classList.toggle("hide",!(cur.v==="domain"||cur.v==="explore"));
  $("#codeSel").classList.toggle("hide",cur.v!=="impact");
  $("#layers").classList.toggle("hide",cur.v!=="explore");
  $("#domSel").value=cur.v==="explore"?(cur.seed||"TU"):(cur.dom||"AE"); if(cur.code)$("#codeSel").value=cur.code;
  $("#hint").textContent=cur.v==="explore"
    ? "点击域节点展开邻居 · 拖拽 · 滚轮缩放 · 空白平移 · 上方图层开关可隐藏边"
    : "悬停看全名 · 点击节点看关系 · 拖拽 · 滚轮缩放 · 空白平移";
}
$("#views").addEventListener("click",ev=>{ const b=ev.target.closest("button"); if(!b)return;
  if(b.dataset.v==="explore"&&cur.v!=="explore"){ window.__expanded=new Set(); expandNode(cur.seed||"TU"); return; } // fresh entry: 自动展开种子一跳
  cur.v=b.dataset.v; render(); });
$("#domSel").addEventListener("change",e=>{
  if(cur.v==="explore"){ cur.seed=e.target.value; window.__expanded=new Set(); expandNode(cur.seed); return; }
  cur.dom=e.target.value; render();});
$("#codeSel").addEventListener("change",e=>{cur.code=e.target.value;render();});
const LAYER_SEL={hard:".edge.hardrel",flow:".iedge.flow",link:".iedge.link",cooc:".iedge.cooc"};
function applyLayerToggles(){
  for(const b of $("#layers").children){
    const on=b.classList.contains("on");
    document.querySelectorAll(LAYER_SEL[b.dataset.l]).forEach(el=>el.style.display=on?"":"none");
  }
}
$("#layers").addEventListener("click",ev=>{ const b=ev.target.closest("button"); if(!b)return;
  b.classList.toggle("on"); applyLayerToggles(); });

// ---- RAG deep-explain (optional local backend at :8000, graceful offline) ----
let RAG_OK=false;
fetch("http://127.0.0.1:8000/api/health").then(r=>{ if(r&&r.ok){RAG_OK=true; applyRagVisibility();} }).catch(()=>{});
function applyRagVisibility(){ document.querySelectorAll(".ragBtn").forEach(b=>b.classList.toggle("hide",!RAG_OK)); }
function ragExplain(a,b,btn){
  if(!RAG_OK)return;
  const q=b?("In SDTM, explain how domain "+a+" relates to "+b+" and why.")
           :("In SDTM, explain domain "+a+"'s role and how it typically relates to other domains.");
  if(btn){ btn.disabled=true; btn.textContent="思考中…"; }
  fetch("http://127.0.0.1:8000/api/ask",{method:"POST",headers:{"Content-Type":"application/json"},
    body:JSON.stringify({question:q})})
   .then(r=>r.json()).then(d=>{
     const ans=document.createElement("div"); ans.className="ragans"; ans.textContent=d.answer||"(无回答)";
     if(btn&&btn.parentNode)btn.replaceWith(ans); else $("#panel").appendChild(ans);
   })
   .catch(()=>{ if(btn){ btn.disabled=false; btn.textContent="深入解释"; } });
}

// ---- click-to-inspect relationship panel ----
function closePanel(){ $("#panel").classList.add("hide"); }
function nav(v,key){ cur.v=v; if(v==="domain")cur.dom=key; else cur.code=key; render(); }
function chips(arr,kind){ return '<div class="chips">'+arr.map(c=>'<span class="chip '+(kind==="code"?"k navcode":"navdom")+'" data-code="'+esc(c)+'">'+esc(c)+'</span>').join("")+'</div>'; }
function openPanel(n){
  const P=$("#panel"),tName={class:"观测类",domain:"域",var:"变量",code:"码表"}[n.type];
  let h='<div class="ph"><div><div class="pty">'+tName+'</div><div class="pt">'+esc(n.label)+'</div></div><button class="x" id="pClose">×</button></div>';
  if(n.type==="domain"){
    const d=domByCode.get(n.label)||{label:n.label,cls:"",struct:"",nv:0};
    const vs=varsByDomain.get(n.label)||[]; const codes=new Set();
    for(const v of vs)for(const [cc,doms] of (ctByVar.get(v)||[]))if(doms.includes(n.label))codes.add(cc);
    const mates=DATA.domains.filter(x=>x.cls===d.cls&&x.code!==n.label).map(x=>x.code);
    const rels=relBySrc.get(n.label)||[];
    h+='<div class="kv"><b>'+esc(d.label)+'</b><br>类: <span style="color:'+classColor(d.cls)+'">●</span> '+esc(d.cls)+'<br>结构: '+esc(d.struct)+'<br>变量: <b>'+d.nv+'</b> · 码表: <b>'+codes.size+'</b></div>';
    if(rels.length){ h+='<h4>跨域关系 · curated</h4>';
      for(const r of rels) h+='<div class="rel"><span class="chip navdom" data-code="'+esc(r.d)+'">'+esc(r.d)+'</span> '+(r.mech?'<span class="adv">['+esc(r.mech)+']</span>':'')+'<div class="m">'+esc(r.cat)+(r.note?' — '+esc(r.note):'')+'</div></div>'; }
    const impl=implicitByDomain.get(n.label)||[];
    if(impl.length){
      const KIND_LABEL={data_flow:"数据流",explicit_link:"显式链接",co_occurrence:"共现"};
      const byKind={}; for(const e of impl)(byKind[e.kind]=byKind[e.kind]||[]).push(e);
      h+='<h4>关系 · 分层（推断） · '+impl.length+'</h4>';
      for(const k of ["data_flow","explicit_link","co_occurrence"]){
        const list=byKind[k]; if(!list||!list.length)continue;
        for(const e of list){
          const other=e.source===n.label?e.target:e.source;
          const arrow=e.directed?(e.source===n.label?" → ":" ← "):" — ";
          h+='<div class="rel irel" data-eid="'+esc(e.id)+'"><span class="tag '+IMPLICIT_LAYER[k]+'">'+esc(KIND_LABEL[k])+'</span> '
            +'<span class="chip navdom" data-code="'+esc(other)+'">'+esc(other)+'</span>'+arrow
            +'<span class="adv">置信 '+e.confidence+(e.verified?" · ✓":" · 未核验")+'</span>'
            +'<button class="ragBtn'+(RAG_OK?"":" hide")+'" data-a="'+esc(n.label)+'" data-b="'+esc(other)+'">深入解释</button>'
            +(e.relation?'<div class="m">'+esc(e.relation)+'</div>':'')+'</div>';
        }
      }
    }
    h+='<h4>同类域 · '+mates.length+'</h4>'+chips(mates,"dom");
    h+='<h4>码表 · '+codes.size+'</h4>'+chips([...codes],"code");
    h+='<button class="ragBtn'+(RAG_OK?"":" hide")+'" data-a="'+esc(n.label)+'" style="margin-top:12px">深入解释 / 为何相关</button>';
  } else if(n.type==="var"){
    const vi=DATA.vars[n.label]||{}; const doms=(domainsByVar.get(n.label)||[]).slice().sort();
    const cc=(ctByVar.get(n.label)||[]).map(x=>x[0]);
    h+='<div class="kv"><b>'+esc(vi.l||n.label)+'</b><br>role: '+esc(vi.r||"—")+' · core: '+esc(vi.c||"—")+'</div>';
    h+='<h4>出现于 '+doms.length+' 个域</h4>'+chips(doms,"dom");
    if(cc.length) h+='<h4>使用码表</h4>'+chips(cc,"code");
  } else if(n.type==="code"){
    const ci=DATA.clsCodes[n.label]||{}; const doms=[...(codeDomains.get(n.label)||[])].sort();
    const nv=(codeVars.get(n.label)||new Set()).size;
    h+='<div class="kv"><b>'+esc(ci.n||"")+'</b><br>'+(ci.e?"可扩展 extensible":"不可扩展 closed")+' · 术语数: '+(ci.t??"—")+'<br>影响: <b>'+doms.length+'</b> 域 / <b>'+nv+'</b> 变量</div>';
    h+='<h4>波及域 · '+doms.length+'</h4>'+chips(doms,"dom");
  } else if(n.type==="class"){
    const doms=DATA.domains.filter(x=>x.cls===n.label).map(x=>x.code);
    h+='<div class="kv">观测类,含 <b>'+doms.length+'</b> 个域</div><h4>域 · '+doms.length+'</h4>'+chips(doms,"dom");
  }
  P.innerHTML=h; P.classList.remove("hide");
}
function openEvidence(e){
  const P=$("#panel");
  const kindLabel={data_flow:"数据流",explicit_link:"显式链接",co_occurrence:"共现"}[e.kind]||e.kind;
  let h='<div class="ph"><div><div class="pty">推断边 · '+esc(kindLabel)+'</div><div class="pt">'+esc(e.source)+(e.directed?' → ':' — ')+esc(e.target)+'</div></div><button class="x" id="pClose">×</button></div>';
  if(e.relation) h+='<div class="kv">'+esc(e.relation)+'</div>';
  h+='<div class="q">'+esc(e.evidence.quote)+'</div>';
  h+='<div class="m">来源: '+esc(e.evidence.source_file)+':'+e.evidence.line+'</div>';
  h+='<div class="m">置信 '+e.confidence+(e.verified?' · ✓ 已核验':' · 未核验')+'</div>';
  h+='<button class="ragBtn'+(RAG_OK?"":" hide")+'" data-a="'+esc(e.source)+'" data-b="'+esc(e.target)+'" style="margin-top:10px">深入解释 / 为何相关</button>';
  P.innerHTML=h; P.classList.remove("hide");
}
$("#panel").addEventListener("click",ev=>{ if(ev.target.id==="pClose"){closePanel();return;}
  const rag=ev.target.closest(".ragBtn"); if(rag){ if(!rag.classList.contains("hide"))ragExplain(rag.dataset.a,rag.dataset.b,rag); return; }
  const el=ev.target.closest("[data-code]"); if(el){ if(el.classList.contains("navcode"))nav("impact",el.dataset.code); else nav("domain",el.dataset.code); return; }
  const re=ev.target.closest("[data-eid]"); if(re){ const e=implicitById.get(re.dataset.eid); if(e)openEvidence(e); } });
$("#physBtn").addEventListener("click",()=>{ running=!running; if(running){alpha=Math.max(alpha,.4);} $("#physBtn").textContent=(running?"⏸":"▶")+" 布局"; });
$("#fitBtn").addEventListener("click",()=>{ resetZoom(); alpha=Math.max(alpha,.5); });
$("#themeBtn").addEventListener("click",()=>{ const cur=document.documentElement.dataset.theme;
  const next=cur==="dark"?"light":cur==="light"?"":"dark"; if(next)document.documentElement.dataset.theme=next; else document.documentElement.removeAttribute("data-theme");
  refreshColors(); });
function refreshColors(){ for(const n of N){ const shape=n.g.firstChild;
  if(n.type==="code"){shape.setAttribute("fill",cvar("--codeFill"));shape.setAttribute("stroke",cvar("--codeStroke"));}
  else if(n.type==="var")shape.setAttribute("fill",cvar("--varFill"));
  else shape.setAttribute("fill",classColor(n.cls)); } buildLegend(); }

// ---- selects + legend ----
function initSelects(){
  const ds=$("#domSel"); ds.innerHTML=DATA.domains.slice().sort((a,b)=>a.code.localeCompare(b.code))
    .map(d=>'<option value="'+d.code+'">'+d.code+" — "+esc(d.label)+"</option>").join("");
  ds.value=cur.dom;
  const cs=$("#codeSel"); const codes=Object.keys(DATA.clsCodes)
    .map(c=>({c,n:DATA.clsCodes[c].n,d:(codeDomains.get(c)||new Set()).size}))
    .sort((a,b)=>b.d-a.d||a.c.localeCompare(b.c));
  cs.innerHTML=codes.map(o=>'<option value="'+o.c+'">'+o.c+" — "+esc(o.n)+"  ("+o.d+" 域)</option>").join("");
  cur.code=codes[0].c; cs.value=cur.code;
}
function buildLegend(){
  const rows=CLASS_ORDER.map((c,i)=>'<div class="row"><span class="sw" style="background:'+classColor(c)+'"></span>'+esc(c)+'</div>').join("");
  $("#legend").innerHTML=
    '<b>节点类型</b>'+
    '<div class="row"><span class="shape">●</span>观测类 / 域（按类配色）</div>'+
    '<div class="row"><span class="shape">·</span>变量</div>'+
    '<div class="row"><span class="shape">◆</span>码表 Codelist</div>'+
    '<b style="margin-top:6px">观测类配色</b>'+rows;
}

initSelects(); buildLegend(); render();
addEventListener("resize",()=>{ if(cur.v)render(); });
matchMedia("(prefers-color-scheme: dark)").addEventListener?.("change",refreshColors);
</script>
</body>
</html>
"""


def main() -> None:
    data = build_data()
    payload = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    payload = payload.replace("<", "\\u003c")
    html = TEMPLATE.replace("__DATA__", payload)
    out = ROOT / "kg_viewer.html"
    out.write_text(html, encoding="utf-8")
    kb = len(html.encode("utf-8")) / 1024
    print(f"wrote {out}  ({kb:.0f} KB)")
    print("counts:", data["counts"])
    print(f"vars shown={len(data['vars'])}  ref codelists={len(data['clsCodes'])}  "
          f"hasVar={len(data['hasVar'])}  usesCt={len(data['usesCt'])}")


if __name__ == "__main__":
    main()
