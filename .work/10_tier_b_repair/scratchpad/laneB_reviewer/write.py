import json,os
B="/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair/work/triage"
rows={json.loads(l)["atom_id"]:json.loads(l) for l in open(f"{B}/lane_B.jsonl")}
plan=json.load(open(f"{B}/review_lane_B.plan.json"))
out=f"{B}/review_lane_B.jsonl"
done=set()
if os.path.exists(out): done={json.loads(l)["atom_id"] for l in open(out)}
dis={
 "ig34_p0225_a004":("VALUE_DIFF","knowledge_base/domains/GF/examples.md:27","atom_type 误标 FIGURE, 实为 Ex1 gf.xpt 数据表; KB 表数据与 PDF p225 整表不符: PDF 为 ATM/CDKN2A, GRCh37.75, TRF001338, 2018-05-22; KB 为 BRAF p.Val600Glu, rs121913227, VISITDY -25 等 (疑似旧版/编造). writer reason 'KB 有对应 markdown 表' 掩盖真错; 按 C09 字面应 FIGURE, 但终态 FIGURE_DEFERRED 会埋掉 KB 错值 → 主控裁"),
 "ig34_p0225_a017":("VALUE_DIFF","knowledge_base/domains/GF/examples.md:62","atom_type 误标 FIGURE, 实为 Ex2 gf.xpt 3 行表; PDF GFREFID NA18537/NA07000/NA00131, GFORRES T/T, G/T, G/G, GFDTC 2020-06-25, GFDY -3; KB 三行 GFREFID 均 NA01001、GFORRES 均 G/G、GFDTC 空/2020-06-3、GFDY -25/-25/-3. 同 a004, 主控裁"),
}
notes={
 "ig34_p0112_a009":"同意 ATOM_ERR; kb_loc :64 为空行, 表头 '| | |' 实在 :65",
 "ig34_p0214_a005":"同意; 注: 同义句在 CP/assumptions.md:52 (假设节), 例子节 :111 缺",
 "ig34_p0367_a013":"同意 (KB :14 与原子逐字同, 相对 PDF 4 行是合并改写)",
}
plan_ids=[(i,"full") for i in plan["full"]]+[(i,"sample") for c in ("PRESENT","IE_CAND") for i in plan["sample"][c]]
with open(out,"a") as f:
    for aid,scope in plan_ids:
        if aid in done: continue
        r=rows[aid]; wc=r["class"]
        if aid in dis:
            rc,loc,why=dis[aid]; rec={"atom_id":aid,"writer_class":wc,"reviewer_class":rc,"agree":False,"kb_loc":loc,"reason":why,"scope":scope}
        else:
            rec={"atom_id":aid,"writer_class":wc,"reviewer_class":wc,"agree":True,"kb_loc":r["evidence"]["kb_loc"],"reason":notes.get(aid,"复核 PDF 页 + KB 一致"),"scope":scope}
        f.write(json.dumps(rec,ensure_ascii=False)+"\n")
import collections
R=[json.loads(l) for l in open(out)]
c=collections.Counter((x["scope"],x["writer_class"],x["agree"]) for x in R)
for k,v in sorted(c.items()): print(k,v)
print(len(R))
