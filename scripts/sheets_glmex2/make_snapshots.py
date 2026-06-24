# -*- coding: utf-8 -*-
import json, os, csv, re

BASE = r"D:\Iteracion\sheets_glmex2"
DAILY = os.path.join(BASE, "daily")
os.makedirs(DAILY, exist_ok=True)

TR = r"C:\Users\Unda\.claude\projects\D--Iteracion\50668ea3-c7f4-46f4-bbe9-d43a7f672c4f\tool-results"

LABEL = {
 "120244746496800663": "Eye (CBO 1.32)",
 "120246706901420663": "Eye (E2)",
 "120245035555860663": "Petclean (CBO 1.48)",
 "120246245665230663": "Snore (CBO 1.25)",
}
# campaign -> product group for summary
GROUP = {
 "120244746496800663": "Eye",
 "120246706901420663": "Eye",
 "120245035555860663": "Petclean",
 "120246245665230663": "Snore",
}
BEP = {"Eye": 1.32, "Petclean": 1.48, "Snore": 1.25}
ORDER_DET = ["Eye (CBO 1.32)", "Eye (E2)", "Petclean (CBO 1.48)", "Snore (CBO 1.25)"]
ORDER_PROD = ["Eye", "Petclean", "Snore"]
FX = 18.5

def num(s):
    if s is None: return 0.0
    t = re.sub(r"[^\d,.\-]", "", str(s))
    t = t.replace(".", "").replace(",", ".")
    if t in ("", "-", "."): return 0.0
    try: return float(t)
    except: return 0.0

def parse_ads(path):
    with open(path, "r", encoding="utf-8") as f:
        outer = json.load(f)
    return json.loads(outer["ad_entities"])

def detail_rows(ads):
    rows = []
    for a in ads:
        cid = a.get("campaign_id")
        if cid not in LABEL: continue
        spend = num(a.get("amount_spent"))
        if spend < 20: continue
        impr = num(a.get("impressions"))
        rv = a.get("results", {}).get("value", "0") if isinstance(a.get("results"), dict) else "0"
        compras = int(num(rv.split(" ")[0]))
        cpa = num(a.get("cost_per_result", {}).get("value") if isinstance(a.get("cost_per_result"), dict) else 0)
        roas = num(a.get("purchase_roas"))
        thru = num(a.get("video_thruplay_watched_actions"))
        p100 = num(a.get("video_p100_watched_actions"))
        b = BEP[GROUP[cid]]
        if compras == 0: estado, accion = "Sin conversiones", "Apagar"
        elif roas >= b*1.2: estado, accion = "GANADOR", "Escalar"
        elif roas >= b: estado, accion = "Rentable", "Mantener"
        elif roas >= b*0.85: estado, accion = "Marginal", "Vigilar/optimizar"
        else: estado, accion = "Malo", "Apagar"
        rows.append([
            LABEL[cid], str(a.get("name","")).replace(",", " "), round(spend,2), compras,
            round(cpa,2), roas, b, num(a.get("ctr")), num(a.get("cpc")), num(a.get("cpm")),
            num(a.get("frequency")), int(impr), int(num(a.get("clicks"))),
            round(thru/impr*100,1) if impr else 0, round(p100/impr*100,1) if impr else 0,
            estado, accion, ""
        ])
    rows.sort(key=lambda r: (ORDER_DET.index(r[0]), -r[2]))
    return rows

def build_window(title, subtitle, ad_path, camp, shop):
    ads = parse_ads(ad_path)
    det = detail_rows(ads)
    out = []
    out.append([title]); out.append([subtitle])
    out.append(["Nota: Hook rate (2seg) NO disponible. Hold% = ThruPlays/Impresiones. Compl% = video100%/Impresiones. Meta en USD, Shopify en MXN."])
    out.append([])
    out.append(["DETALLE POR VIDEO (META)"])
    out.append(["Producto","Video","Gasto USD","Compras","CPA USD","ROAS","BEP ROAS","CTR %","CPC USD","CPM USD","Frecuencia","Impresiones","Clicks","Hold %","Compl %","Estado","Accion","Notas"])
    out.extend(det)
    out.append([])
    # summary by product (Eye combined)
    out.append(["META vs SHOPIFY (POR PRODUCTO)"])
    out.append([f"FX 1 USD = {FX} MXN (editable). MER = Ventas netas USD / Gasto Meta USD. Meta = campana completa. Shopify = toda la tienda."])
    out.append(["Producto","Meta Gasto USD","Meta Compras","Meta CPA USD","Meta ROAS","Shopify Ordenes","Shopify Bruto MXN","Shopify Neto MXN","AOV neto MXN","% Atrib Meta","Neto USD","MER"])
    tot = dict(spend=0.0, res=0, ord=0, bruto=0.0, neto=0.0)
    concl = []
    for prod in ORDER_PROD:
        cids = [c for c in camp if GROUP[c] == prod]
        spend = sum(camp[c][0] for c in cids)
        res = sum(camp[c][1] for c in cids)
        rev = sum(camp[c][0]*camp[c][3] for c in cids)
        roas = round(rev/spend,2) if spend else 0
        cpa = round(spend/res,2) if res else 0
        g, n, o = shop.get(prod, (0,0,0))
        aov = round(n/o) if o else 0
        attr = round(res/o*100,1) if o else 0
        netusd = round(n/FX)
        mer = round((n/FX)/spend,2) if spend else 0
        out.append([prod, round(spend,2), res, cpa, roas, o, round(g,2), round(n,2), aov, f"{attr}%", netusd, mer])
        tot["spend"]+=spend; tot["res"]+=res; tot["ord"]+=o; tot["bruto"]+=g; tot["neto"]+=n
        concl.append((prod, round(spend,2), res, cpa, roas, BEP[prod], o, mer, attr))
    merT = round((tot["neto"]/FX)/tot["spend"],2) if tot["spend"] else 0
    attrT = round(tot["res"]/tot["ord"]*100,1) if tot["ord"] else 0
    out.append(["TOTAL", round(tot["spend"],2), tot["res"], "", "", tot["ord"], round(tot["bruto"],2), round(tot["neto"],2), "", f"{attrT}%", round(tot["neto"]/FX), merT])
    out.append([])
    out.append(["CONCLUSIONES"])
    for p,sp,res,cpa,roas,b,o,mer,attr in concl:
        out.append([f"{p}: Meta USD {sp} -> ROAS {roas} (BEP {b}), CPA USD {cpa}, {res} compras | Shopify {o} ordenes, MER {mer}, atribucion Meta {attr}%."])
    out.append([f"TIENDA (3 prod): Meta USD {round(tot['spend'],2)} | {tot['ord']} ordenes Shopify | MXN {round(tot['neto'],2)} netos | MER {merT}."])
    return out

def write_csv(path, rows):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        for r in rows: w.writerow(r)

# ---- data per window ----
MTD_CAMP = {
 "120244746496800663": (7680.56,483,15.90,2.48,2.63,429791),
 "120246706901420663": (662.41,36,18.40,2.31,2.59,19969),
 "120245035555860663": (3579.24,169,21.18,1.78,1.94,186227),
 "120246245665230663": (2334.78,103,22.67,1.95,2.35,146708),
}
MTD_SHOP = {"Eye":(648373.18,463277.74,674),"Petclean":(157185,116172.10,177),"Snore":(107417,81254,106)}

W7_CAMP = {
 "120244746496800663": (3316.35,188,17.64,2.22,1.92,182953),
 "120246706901420663": (212.81,8,26.60,1.78,1.96,6164),
 "120245035555860663": (1387.77,64,21.68,1.73,1.49,59088),
 "120246245665230663": (1078.36,42,25.68,1.72,1.67,70417),
}
W7_SHOP = {"Eye":(236960.84,169756.26,248),"Petclean":(57884,43083.43,66),"Snore":(43494,32937,43)}

DAY_CAMP = {
 "120244746496800663": (486.45,33,14.74,2.58,1.52,24890),
 "120246706901420663": (31.39,1,31.39,2.19,1.31,863),
 "120245035555860663": (185.73,7,26.53,1.88,1.14,7140),
 "120246245665230663": (183.13,10,18.31,2.38,1.34,10526),
}
DAY_SHOP = {"Eye":(36028.40,25907.66,38),"Petclean":(10479,6791.33,8),"Snore":(9885,7590,10)}

mes = build_window("GL-MEX2 + SHOPIFY - MES (MTD)", "Periodo: 1-jun-2026 a 23-jun-2026 (mes en curso; hoy parcial) | Actualizado: 23-jun-2026",
                   os.path.join(TR,"mcp-claude_ai_Meta_Ads-ads_get_ad_entities-1782244197400.txt"), MTD_CAMP, MTD_SHOP)
w7 = build_window("GL-MEX2 + SHOPIFY - 7 DIAS", "Periodo: 16-jun-2026 a 22-jun-2026 | Actualizado: 23-jun-2026",
                  os.path.join(TR,"mcp-claude_ai_Meta_Ads-ads_get_ad_entities-1782244197124.txt"), W7_CAMP, W7_SHOP)
day = build_window("GL-MEX2 + SHOPIFY - DIA 22-jun-2026", "Periodo: 22-jun-2026 (dia unico) | Snapshot permanente",
                   os.path.join(TR,"mcp-claude_ai_Meta_Ads-ads_get_ad_entities-1782244199456.txt"), DAY_CAMP, DAY_SHOP)

write_csv(os.path.join(BASE,"mes.csv"), mes)
write_csv(os.path.join(BASE,"7dias.csv"), w7)
write_csv(os.path.join(DAILY,"Dia_2026-06-22.csv"), day)

print("Snapshots escritos.")
for name, rows in [("MES",mes),("7DIAS",w7),("DIA",day)]:
    det = sum(1 for r in rows if len(r)>2 and r[0] in ORDER_DET)
    print(f"{name}: {det} videos en detalle")
