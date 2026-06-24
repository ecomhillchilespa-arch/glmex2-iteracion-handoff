# -*- coding: utf-8 -*-
"""Construye el CSV de cruce Meta x Clarity x Shopify por nivel de conciencia.
Salida: cruce_niveles.csv (para subir a Drive como Google Sheet).
"""
import json, os, re, csv

TR = r"C:\Users\Unda\.claude\projects\D--Iteracion\50668ea3-c7f4-46f4-bbe9-d43a7f672c4f\tool-results"
MTD = os.path.join(TR, "mcp-claude_ai_Meta_Ads-ads_get_ad_entities-1782244197400.txt")
HERE = os.path.dirname(os.path.abspath(__file__))

CAMP = {'120244746496800663': 'Eye', '120246706901420663': 'Eye',
        '120245035555860663': 'Petclean', '120246245665230663': 'Snore'}
BEP = {'Eye': 1.32, 'Petclean': 1.48, 'Snore': 1.25}

# --- Clarity por landing (ultimos 3 dias) ---
LAND = json.load(open(os.path.join(HERE, "landing_aggregated.json"), encoding="utf-8"))
def cl(key):
    return LAND.get(key, {})

DEST = {  # link de destino + clave clarity + nombre corto
 'Eye':      ("https://alegrestiendamexico.com/pages/puremx", "alegrestiendamexico.com/pages/puremx"),
 'Petclean': ("https://alegrestiendamexico.com/pages/petcleanadv", "alegrestiendamexico.com/pages/petcleanadv"),
 'Snore':    ("https://alegrestiendamexico.com/pages/snoremx", "alegrestiendamexico.com/pages/snoremx"),
}

# --- Shopify por producto (MTD 1-23 jun) ---
# orders, gross_mxn, net_mxn  (de load_supabase SHOP['mtd'])  +  ATC y sesiones (ShopifyQL)
SHOP = {
 'Eye':      dict(orders=674, gross=648373, net=463278, atc=1132+1188+106, sess=10390+8452+803),
 'Petclean': dict(orders=177, gross=157185, net=116172, atc=723+166,       sess=8852+1892),
 'Snore':    dict(orders=106, gross=107417, net=81254,  atc=110+402,        sess=1686+4432),
}

def num(s):
    if s is None: return 0.0
    if isinstance(s, dict): s = s.get('value', '')
    t = re.sub(r"[^\d,.\-]", "", str(s).split(" ")[0]).replace(".", "").replace(",", ".")
    if t in ("", "-", "."): return 0.0
    try: return float(t)
    except: return 0.0

def level(name):
    n = re.sub(r"\bBATCH\b", "", name.upper()).strip()
    if n.startswith("U1") or n.startswith("U "): return (1, "Desconocido (Unaware)")
    if n.startswith("PR"): return (2, "Problema (Problem-aware)")
    if n.startswith("SO"): return (3, "Solucion (Solution-aware)")
    if n.startswith("PD") or n.startswith("SD"): return (4, "Producto (Product-aware)")
    if re.fullmatch(r"C\d", n): return (5, "Concepto in-house (cartoon)")
    if "VIDEO" in n or re.search(r"\bE[23]\b", n): return (6, "Sin clasificar / tests")
    return (7, "Otros / sin tag")

# notas cualitativas por ad (de los analisis previos)
NOTE = {
 ("Eye","SO3 30.1"):"Cirugia-cancelada/ancestral, mejor escala del nivel",
 ("Eye","SO6 AD 4"):"DMAE + autoridad medica, aguanta a escala",
 ("Eye","SO5 AD 7"):"Angulo cultural/ancestral, CTR altisimo -> clonar",
 ("Eye","PD2 AD 23"):"Producto directo, gran volumen rentable",
 ("Eye","SO1 AD 38"):"Pierde, apagar",
 ("Eye","PR1 AD 44"):"Problema puro: el nivel mas debil en Eye",
 ("Snore","BATCH U1B AD68"):"'Dano al corazon' (miedo salud) -> escalar, top unaware",
 ("Snore","Video 5 05"):"Sin clasificar pero gran gasto y rentable; el usuario debe describirlo",
 ("Snore","SO2 AD 19"):"MISMO VSL que AD11 pero pierde -> apagar el ad, no el mensaje",
 ("Snore","SO2 AD 11"):"Testimonial femenino, GANADOR (mismo guion que AD19)",
 ("Snore","PR1 AD 46"):"Rendimiento laboral, gana en problema",
 ("Snore","SO3 AD60"):"Desmontar remedios de nariz",
 ("Petclean","1"):"= SO5 UGC 'sin cepillo': 95% del gasto rentable cae aqui (RIESGO concentracion)",
 ("Petclean","SO7 AD 52"):"Groomer/autoridad, segundo pilar rentable",
 ("Petclean","SO8 AD 13"):"Ciencia profunda -> pierde",
 ("Petclean","SO4AD 17"):"Pierde vs su gemelo AD19 -> ejecucion",
 ("Petclean","PR1 AD 18"):"'la bacteria pasa al humano' -> infraexplotado, mover budget",
}

def estado(prod, roas, compras):
    b = BEP[prod]
    if compras == 0 or roas == 0: return "Sin conversiones -> APAGAR"
    if roas >= b*1.2: return "GANADOR -> escalar"
    if roas >= b:     return "Rentable -> mantener"
    if roas >= b*0.85:return "Marginal -> vigilar"
    return "Malo -> apagar"

# --- parse ads ---
outer = json.load(open(MTD, encoding="utf-8"))
ads = json.loads(outer["ad_entities"])
data = {p: {} for p in ("Eye", "Petclean", "Snore")}
for a in ads:
    p = CAMP.get(a.get("campaign_id"))
    if not p: continue
    sp = num(a.get("amount_spent"))
    if sp < 20: continue
    lv, lvname = level(a.get("name", ""))
    rv = a.get("results"); rv = rv.get("value") if isinstance(rv, dict) else rv
    compras = int(num(str(rv).split(" ")[0])) if rv else 0
    row = dict(name=a.get("name", ""), spend=sp, compras=compras,
               roas=num(a.get("purchase_roas")), ctr=num(a.get("ctr")),
               cpc=num(a.get("cpc")), cpm=num(a.get("cpm")),
               clicks=int(num(a.get("clicks"))), lv=lv, lvname=lvname)
    data[p].setdefault((lv, lvname), []).append(row)

# --- escribir CSV ---
out = open(os.path.join(HERE, "cruce_niveles.csv"), "w", newline="", encoding="utf-8-sig")
w = csv.writer(out)
H = ["Nivel conciencia", "Ad", "Spend USD", "Compras", "ROAS", "BEP", "CTR %",
     "CPC USD", "CPM USD", "Clicks", "Link destino",
     "Clarity scroll %", "Clarity quickback", "Clarity dead clicks",
     "Shopify ATC (prod)", "Shopify pedidos (prod)", "Qué está pasando"]

for prod in ("Eye", "Petclean", "Snore"):
    b = BEP[prod]
    link, ck = DEST[prod]
    c = cl(ck)
    sh = SHOP[prod]
    atc_rate = round(sh["atc"]/sh["sess"]*100, 1) if sh["sess"] else 0
    aov = round(sh["net"]/sh["orders"]) if sh["orders"] else 0
    # cabecera de producto
    w.writerow([])
    w.writerow([f"=== {prod}  (BEP ROAS {b}) ==="])
    w.writerow([f"SHOPIFY MTD: pedidos {sh['orders']} | ATC {sh['atc']} ({atc_rate}% de sesiones) | "
                f"ingreso bruto {sh['gross']:,} MXN | neto {sh['net']:,} MXN | AOV {aov:,} MXN"])
    w.writerow([f"DESTINO {link} -> CLARITY 3d: scroll {c.get('scroll_depth','?')}% | "
                f"quickback {c.get('quickback','?')} | dead clicks {c.get('dead','?')} | rage {c.get('rage','?')}"])
    w.writerow(H)
    for (lv, lvname) in sorted(data[prod].keys()):
        rows = sorted(data[prod][(lv, lvname)], key=lambda r: -r["spend"])
        sp_t = sum(r["spend"] for r in rows); cm_t = sum(r["compras"] for r in rows)
        roas_w = round(sum(r["roas"]*r["spend"] for r in rows)/sp_t, 2) if sp_t else 0
        # fila resumen de nivel
        w.writerow([f"-- {lvname} --  ({len(rows)} ads, ${sp_t:,.0f}, {cm_t} compras, ROAS pond {roas_w}) "
                    f"=> {estado(prod, roas_w, cm_t)}"])
        big = [r for r in rows if r["spend"] >= 100]
        small = [r for r in rows if r["spend"] < 100]
        for r in big:
            note = NOTE.get((prod, r["name"]), "")
            diag = estado(prod, r["roas"], r["compras"])
            qpasa = (note + " | " if note else "") + diag
            w.writerow([lvname, r["name"], round(r["spend"], 2), r["compras"], r["roas"], b,
                        r["ctr"], r["cpc"], r["cpm"], r["clicks"], link,
                        c.get("scroll_depth", ""), c.get("quickback", ""), c.get("dead", ""),
                        sh["atc"], sh["orders"], qpasa])
        if small:
            sp_s = sum(r["spend"] for r in small); cm_s = sum(r["compras"] for r in small)
            roas_s = round(sum(r["roas"]*r["spend"] for r in small)/sp_s, 2) if sp_s else 0
            w.writerow([lvname, f"otros {len(small)} ads (<$100)", round(sp_s, 2), cm_s, roas_s, b,
                        "", "", "", "", link, c.get("scroll_depth", ""), c.get("quickback", ""),
                        c.get("dead", ""), sh["atc"], sh["orders"],
                        f"cola larga del nivel -> {estado(prod, roas_s, cm_s)}"])
out.close()
print("OK -> cruce_niveles.csv")
# resumen en consola
for prod in ("Eye","Petclean","Snore"):
    tot=sum(r['spend'] for k in data[prod] for r in data[prod][k])
    print(f"  {prod}: {sum(len(v) for v in data[prod].values())} ads, ${tot:,.0f}")
