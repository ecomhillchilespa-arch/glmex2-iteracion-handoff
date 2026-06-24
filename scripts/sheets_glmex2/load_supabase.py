# -*- coding: utf-8 -*-
import json, os, re

TR = r"C:\Users\Unda\.claude\projects\D--Iteracion\50668ea3-c7f4-46f4-bbe9-d43a7f672c4f\tool-results"
SNAP = "2026-06-23"  # fecha del run

LABEL = {
 "120244746496800663": "Eye (CBO 1.32)", "120246706901420663": "Eye (E2)",
 "120245035555860663": "Petclean (CBO 1.48)", "120246245665230663": "Snore (CBO 1.25)",
}
GROUP = {"120244746496800663":"Eye","120246706901420663":"Eye","120245035555860663":"Petclean","120246245665230663":"Snore"}
BEP = {"Eye":1.32,"Petclean":1.48,"Snore":1.25}
ORDER_DET = ["Eye (CBO 1.32)","Eye (E2)","Petclean (CBO 1.48)","Snore (CBO 1.25)"]

WINDOWS = {
 "mtd": dict(file="mcp-claude_ai_Meta_Ads-ads_get_ad_entities-1782244197400.txt", ps="2026-06-01", pe="2026-06-23"),
 "7d":  dict(file="mcp-claude_ai_Meta_Ads-ads_get_ad_entities-1782244197124.txt", ps="2026-06-16", pe="2026-06-22"),
 "day": dict(file="mcp-claude_ai_Meta_Ads-ads_get_ad_entities-1782244199456.txt", ps="2026-06-22", pe="2026-06-22"),
}

def num(s):
    if s is None: return 0.0
    t = re.sub(r"[^\d,.\-]", "", str(s)).replace(".","").replace(",",".")
    if t in ("","-","."): return 0.0
    try: return float(t)
    except: return 0.0

def q(s):
    return "'" + str(s).replace("'","''") + "'"

def parse(path):
    with open(path,encoding="utf-8") as f: outer=json.load(f)
    return json.loads(outer["ad_entities"])

def ad_rows(win, meta):
    rows=[]
    for a in parse(os.path.join(TR, meta["file"])):
        cid=a.get("campaign_id")
        if cid not in LABEL: continue
        spend=num(a.get("amount_spent"))
        if spend<20: continue
        impr=num(a.get("impressions"))
        rv=a.get("results",{}).get("value","0") if isinstance(a.get("results"),dict) else "0"
        compras=int(num(rv.split(" ")[0]))
        cpa=num(a.get("cost_per_result",{}).get("value") if isinstance(a.get("cost_per_result"),dict) else 0)
        roas=num(a.get("purchase_roas")); thru=num(a.get("video_thruplay_watched_actions")); p100=num(a.get("video_p100_watched_actions"))
        prod=GROUP[cid]; b=BEP[prod]
        if compras==0: est,ac="Sin conversiones","Apagar"
        elif roas>=b*1.2: est,ac="GANADOR","Escalar"
        elif roas>=b: est,ac="Rentable","Mantener"
        elif roas>=b*0.85: est,ac="Marginal","Vigilar/optimizar"
        else: est,ac="Malo","Apagar"
        hold=round(thru/impr*100,1) if impr else 0
        compl=round(p100/impr*100,1) if impr else 0
        vals=[q(SNAP),q(win),q(meta["ps"]),q(meta["pe"]),q(prod),q(LABEL[cid]),q(cid),q(a.get("id")),q(a.get("name","")),
              round(spend,2),compras,round(cpa,2),roas,b,num(a.get("ctr")),num(a.get("cpc")),num(a.get("cpm")),
              num(a.get("frequency")),int(impr),int(num(a.get("clicks"))),hold,compl,q(est),q(ac)]
        rows.append((LABEL[cid],spend,"("+",".join(str(v) for v in vals)+")"))
    rows.sort(key=lambda r:(ORDER_DET.index(r[0]),-r[1]))
    return [r[2] for r in rows]

AD_COLS="snapshot_date,time_window,period_start,period_end,product,campaign_label,campaign_id,ad_id,ad_name,spend_usd,purchases,cpa_usd,roas,bep_roas,ctr,cpc_usd,cpm_usd,frequency,impressions,clicks,hold_rate,compl_rate,estado,accion"

def emit_ad(win):
    rows=ad_rows(win,WINDOWS[win])
    sql=f"insert into public.glmex2_ad_perf ({AD_COLS}) values\n"+",\n".join(rows)
    sql+="\non conflict (snapshot_date,time_window,ad_id) do update set "
    sets=[c for c in AD_COLS.split(",") if c not in ("snapshot_date","time_window","ad_id")]
    sql+=", ".join(f"{c}=excluded.{c}" for c in sets)+";"
    return sql

# ---- producto (Meta campaña completa + Shopify) ----
CAMP={
 "mtd":{"120244746496800663":(7680.56,483,2.48),"120246706901420663":(662.41,36,2.31),"120245035555860663":(3579.24,169,1.78),"120246245665230663":(2334.78,103,1.95)},
 "7d":{"120244746496800663":(3316.35,188,2.22),"120246706901420663":(212.81,8,1.78),"120245035555860663":(1387.77,64,1.73),"120246245665230663":(1078.36,42,1.72)},
 "day":{"120244746496800663":(486.45,33,2.58),"120246706901420663":(31.39,1,2.19),"120245035555860663":(185.73,7,1.88),"120246245665230663":(183.13,10,2.38)},
}
SHOP={
 "mtd":{"Eye":(648373.18,463277.74,674),"Petclean":(157185,116172.10,177),"Snore":(107417,81254,106)},
 "7d":{"Eye":(236960.84,169756.26,248),"Petclean":(57884,43083.43,66),"Snore":(43494,32937,43)},
 "day":{"Eye":(36028.40,25907.66,38),"Petclean":(10479,6791.33,8),"Snore":(9885,7590,10)},
}
FX=18.5
PROD_COLS="snapshot_date,time_window,period_start,period_end,product,meta_spend_usd,meta_purchases,meta_cpa_usd,meta_roas,bep_roas,shopify_orders,shopify_gross_mxn,shopify_net_mxn,aov_net_mxn,attribution_pct,net_usd,mer,fx_rate"

def emit_prod():
    rows=[]
    for win,meta in WINDOWS.items():
        camp=CAMP[win]; shop=SHOP[win]
        for prod in ["Eye","Petclean","Snore"]:
            cids=[c for c in camp if GROUP[c]==prod]
            spend=sum(camp[c][0] for c in cids); res=sum(camp[c][1] for c in cids)
            rev=sum(camp[c][0]*camp[c][2] for c in cids)
            roas=round(rev/spend,2) if spend else 0; cpa=round(spend/res,2) if res else 0
            g,n,o=shop[prod]; aov=round(n/o) if o else 0; attr=round(res/o*100,1) if o else 0
            netusd=round(n/FX); mer=round((n/FX)/spend,2) if spend else 0
            vals=[q(SNAP),q(win),q(meta["ps"]),q(meta["pe"]),q(prod),round(spend,2),res,cpa,roas,BEP[prod],o,round(g,2),round(n,2),aov,attr,netusd,mer,FX]
            rows.append("("+",".join(str(v) for v in vals)+")")
    sql=f"insert into public.glmex2_product_perf ({PROD_COLS}) values\n"+",\n".join(rows)
    sql+="\non conflict (snapshot_date,time_window,product) do update set "
    sets=[c for c in PROD_COLS.split(",") if c not in ("snapshot_date","time_window","product")]
    sql+=", ".join(f"{c}=excluded.{c}" for c in sets)+";"
    return sql

import sys
which=sys.argv[1] if len(sys.argv)>1 else "all"
if which in ("prod","all"): print("=== PROD ==="); print(emit_prod())
for w in ("day","7d","mtd"):
    if which in (w,"all"): print(f"=== {w.upper()} ==="); print(emit_ad(w))
