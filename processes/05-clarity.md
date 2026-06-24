# Proceso 05 — Microsoft Clarity (Data Export API)

**Objetivo:** traer comportamiento on-site (scroll depth, fricción/clicks, tráfico) por landing para
cruzarlo con performance de ads.

## Setup
- Token JWT en `scripts/clarity/clarity_token.txt` (ver `.example` y `SECURITY.md`). Scope `Data.Export`.
- Proyecto Clarity: `2876889344704695` (cubre las tiendas MX/CL/ES).
- Sin librerías externas (urllib puro). Corre con Python 3.

## Límites de la API (importantes)
- **Máximo 10 requests por día por proyecto.** Cada llamada guarda el JSON crudo en `raw/` para no
  desperdiciar cuota.
- `numOfDays` solo acepta **1, 2 o 3**. Es "live insights" de los últimos días; NO hay histórico ni rangos largos.
- El endpoint da `averageScrollDepth` = **un solo promedio en %** (no la distribución 25/50/75/100;
  esa solo existe en el dashboard/heatmaps de Clarity, no en la API).

## Scripts
- `clarity_fetch.py [numDays] [dim1 dim2 dim3]` — pega a `project-live-insights`, imprime resumen
  (tráfico, engagement, scroll, fricción, breakdowns) y guarda `raw/clarity_*.json`.
  - Dimensiones: Browser, Device, Country, OS, Source, Medium, Campaign, Channel, **URL**.
  - Ej: `python clarity_fetch.py 3 URL` → desglose por URL de los últimos 3 días.
- `clarity_by_landing.py [raw/...json]` — el desglose por URL viene fragmentado por querystrings
  (fbclid/utm). Este script **normaliza por ruta base** y consolida: scroll ponderado por sesiones +
  quickback/dead/rage por landing. Genera `landing_aggregated.json`.

## Cómo leerlo
- `averageScrollDepth` ya es **% promedio de página scrolleada** por sesión.
- Señales de fricción por landing: `QuickbackClick` (volvieron atrás), `DeadClickCount`, `RageClickCount`.
- Cruza scroll + ATC (de Shopify) para diagnosticar landing: ej. scroll bajo + ATC alto = oferta clara arriba.

## Destinos clave (tiendas)
Eye `/pages/puremx` · Petclean `/pages/petcleanadv` · Snore `/pages/snoremx`. (En la última corrida: el
theme mostraba ~34% de sesiones con errores JS → vale revisarlo.)
