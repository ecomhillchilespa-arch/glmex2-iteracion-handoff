# -*- coding: utf-8 -*-
"""Agrega el desglose Clarity-por-URL en rutas base (landing pages),
ponderando scroll depth por sesiones y sumando clicks de friccion.
Uso: python clarity_by_landing.py raw\\clarity_3d_URL_xxx.json
"""
import sys, os, json
from urllib.parse import urlsplit, unquote

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

path = sys.argv[1] if len(sys.argv) > 1 else max(
    (os.path.join("raw", f) for f in os.listdir("raw") if "URL" in f),
    key=os.path.getmtime)
data = json.load(open(path, encoding="utf-8"))


def base(u):
    if not u:
        return "(directo)"
    s = urlsplit(u)
    return unquote(s.netloc + s.path).rstrip("/")


def n(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def metric(name):
    for m in data:
        if m["metricName"] == name:
            return m["information"]
    return []


# sesiones por landing (de Traffic)
sess = {}
for r in metric("Traffic"):
    sess[base(r.get("Url"))] = sess.get(base(r.get("Url")), 0) + n(r.get("totalSessionCount"))

# scroll ponderado: cada fila trae averageScrollDepth (+ a veces sessionsCount)
scroll_num, scroll_den = {}, {}
for r in metric("ScrollDepth"):
    b = base(r.get("Url"))
    w = n(r.get("sessionsCount")) or 1
    scroll_num[b] = scroll_num.get(b, 0) + n(r.get("averageScrollDepth")) * w
    scroll_den[b] = scroll_den.get(b, 0) + w

# clicks de friccion por landing
def click_sum(metric_name, field="subTotal"):
    out = {}
    for r in metric(metric_name):
        b = base(r.get("Url"))
        out[b] = out.get(b, 0) + n(r.get(field))
    return out

quick = click_sum("QuickbackClick")
dead = click_sum("DeadClickCount")
rage = click_sum("RageClickCount")

# views por landing (pagesViews del primer metric que lo traiga, ej DeadClickCount)
views = {}
for r in metric("DeadClickCount"):
    b = base(r.get("Url"))
    views[b] = views.get(b, 0) + n(r.get("pagesViews"))

rows = []
keys = set(sess) | set(scroll_den) | set(quick)
for b in keys:
    s = sess.get(b, 0)
    sd = scroll_num.get(b, 0) / scroll_den[b] if scroll_den.get(b) else 0
    rows.append((b, s, sd, quick.get(b, 0), dead.get(b, 0), rage.get(b, 0)))

rows.sort(key=lambda r: -r[1])
print(f"{'LANDING':<60}{'Ses':>7}{'Scroll%':>9}{'Quickbk':>9}{'Dead':>7}{'Rage':>7}")
print("-" * 99)
for b, s, sd, q, d, rg in rows[:30]:
    print(f"{b[:60]:<60}{int(s):>7}{sd:>8.1f}{int(q):>9}{int(d):>7}{int(rg):>7}")

# guarda agregado json para reusar
out = {b: dict(sessions=int(s), scroll_depth=round(sd, 1), quickback=int(q),
               dead=int(d), rage=int(rg)) for b, s, sd, q, d, rg in rows}
json.dump(out, open("landing_aggregated.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print("\nGuardado: landing_aggregated.json")
