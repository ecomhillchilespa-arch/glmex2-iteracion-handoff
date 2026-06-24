# -*- coding: utf-8 -*-
"""
Conector local Microsoft Clarity (Data Export API) -> GL-MEX2 / Alegres Tienda.

Uso:
    python clarity_fetch.py                 # ultimos 1 dia, sin dimensiones
    python clarity_fetch.py 3               # ultimos 3 dias (max permitido)
    python clarity_fetch.py 1 Device OS     # 1 dia, desglosado por hasta 3 dimensiones

Dimensiones validas: Browser, Device, Country, OS, Source, Medium, Campaign, Channel, URL, ...

OJO: la API permite SOLO 10 requests por dia por proyecto, y numOfDays = 1..3.
Cada llamada guarda el JSON crudo en raw/ para no desperdiciar cuota.
"""
import sys, os, json, datetime
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
TOKEN = open(os.path.join(HERE, "clarity_token.txt"), encoding="utf-8").read().strip()
URL = "https://www.clarity.ms/export-data/api/v1/project-live-insights"


def fetch(num_days=1, dims=None):
    qs = f"?numOfDays={num_days}"
    for i, d in enumerate(dims or [], start=1):
        qs += f"&dimension{i}={d}"
    req = Request(URL + qs, headers={"Authorization": "Bearer " + TOKEN})
    try:
        with urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8"))
    except HTTPError as e:
        body = e.read().decode("utf-8", "ignore")
        raise SystemExit(f"HTTP {e.code}: {body}\n"
                         f"(429 = pasaste las 10 llamadas/dia; 401 = token vencido)")
    except URLError as e:
        raise SystemExit(f"Red: {e}")


def g(data, name):
    for m in data:
        if m.get("metricName") == name:
            return m.get("information", [])
    return []


def n(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def resumen(data, num_days, dims):
    L = []
    L.append("=" * 56)
    L.append(f"  CLARITY  |  ultimos {num_days} dia(s)" + (f"  |  dims: {', '.join(dims)}" if dims else ""))
    L.append("=" * 56)

    tr = g(data, "Traffic")
    if tr:
        t = tr[0]
        ses = int(n(t.get("totalSessionCount")))
        bot = int(n(t.get("totalBotSessionCount")))
        users = int(n(t.get("distinctUserCount")))
        ppp = n(t.get("pagesPerSessionPercentage"))
        L.append(f"Sesiones: {ses:,}   Usuarios: {users:,}   Bots: {bot:,}   Pags/sesion: {ppp:.2f}")

    et = g(data, "EngagementTime")
    if et:
        L.append(f"Tiempo total: {et[0].get('totalTime')}s   activo: {et[0].get('activeTime')}s")
    sd = g(data, "ScrollDepth")
    if sd:
        L.append(f"Scroll promedio: {sd[0].get('averageScrollDepth')}%")

    # Senales de friccion (UX)
    L.append("-" * 56)
    L.append("FRICCION (UX):")
    for met, etiqueta in [("DeadClickCount", "Dead clicks"),
                          ("RageClickCount", "Rage clicks"),
                          ("QuickbackClick", "Quickback"),
                          ("ErrorClickCount", "Error clicks"),
                          ("ScriptErrorCount", "Errores JS"),
                          ("ExcessiveScroll", "Scroll excesivo")]:
        info = g(data, met)
        if info:
            r = info[0]
            pct = r.get("sessionsWithMetricPercentage", 0)
            L.append(f"  {etiqueta:<16} {pct}% de sesiones   (subtotal {r.get('subTotal')})")

    # Breakdowns
    for met, etiqueta in [("Country", "PAISES"), ("Device", "DISPOSITIVOS"),
                          ("OS", "OS"), ("Browser", "NAVEGADORES"),
                          ("ReferrerUrl", "REFERIDORES"), ("PageTitle", "PAGINAS (titulo)"),
                          ("PopularPages", "PAGINAS POPULARES")]:
        info = g(data, met)
        if info:
            L.append("-" * 56)
            L.append(etiqueta + ":")
            for row in info[:10]:
                if "sessionsCount" in row:
                    L.append(f"  {row.get('name') or '(directo)':<48} {int(n(row['sessionsCount'])):>6}")
                elif "visitsCount" in row:
                    L.append(f"  {(row.get('url') or '')[:48]:<48} {int(n(row['visitsCount'])):>6}")
    return "\n".join(L)


def main():
    num_days = 1
    dims = []
    args = sys.argv[1:]
    if args and args[0].isdigit():
        num_days = max(1, min(3, int(args[0])))
        dims = args[1:3]
    elif args:
        dims = args[:3]

    data = fetch(num_days, dims)

    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    tag = f"{num_days}d" + ("_" + "-".join(dims) if dims else "")
    raw_path = os.path.join(HERE, "raw", f"clarity_{tag}_{stamp}.json")
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(resumen(data, num_days, dims))
    print("-" * 56)
    print("JSON crudo guardado en:", raw_path)


if __name__ == "__main__":
    main()
