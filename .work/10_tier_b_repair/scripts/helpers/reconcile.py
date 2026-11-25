import json, sys
v1 = json.load(open(sys.argv[1])); v2 = json.load(open(sys.argv[2]))
t1 = {(t["file"], t["line"]): t for t in v1["tables"]}
tot1 = tot2 = 0
for t in v2["tables"]:
    a = t1.get((t["file"], t["line"]), {})
    r1 = {str(d["row"]) for d in a.get("diffs", [])}
    r2 = {str(d.get("kb_row") or d.get("pdf_row") or "HEADER") if d["type"] != "HEADER" else "HEADER" for d in t.get("diffs", [])}
    tot1 += len(a.get("diffs", [])); tot2 += len(t.get("diffs", []))
    if r1 or r2 or a.get("status") != t["status"]:
        print(f'{t["file"].split("knowledge_base/")[1]}:{t["line"]} v1={a.get("status")}/{len(a.get("diffs",[]))} v2={t["status"]}/{len(t.get("diffs",[]))}'
              f' lost={sorted(r1 - r2)} new={sorted(r2 - r1)}')
print("diff entries v1", tot1, "v2", tot2)
