# Proceso 04 — Tablero diario GL-MEX2

**Objetivo:** rutina diaria de performance que cruza Meta + Shopify, la consolida en Supabase y la
publica en Google Sheets para tres ventanas: **Mes (MTD) / 7 días / Día**.

## Fuentes y umbral
- **Meta Ads** (MCP): entidades a nivel ad y campaña, ventana MTD/7d/día. Umbral: ignora ads con
  `amount_spent < $20` USD (cola de ruido).
- **Shopify** (MCP): ventas/pedidos por producto + sesiones/ATC (ShopifyQL).
- Productos y BEP: Eye 1.32 · Petclean 1.48 · Snore 1.25 (ver `CLAUDE.md` §3).

## Flujo
1. **Trae datos de Meta** por las 3 ventanas (MTD `2026-06-01..hoy`, 7d, día). Guarda los tool-results.
2. **Trae Shopify** (pedidos, ingreso bruto/neto, AOV, sesiones, ATC) por producto.
3. **Genera SQL** con `scripts/sheets_glmex2/load_supabase.py` → inserta en `glmex2_ad_perf` (por ad) y
   `glmex2_product_perf` (por producto). Hace `on conflict ... do update` (idempotente por snapshot).
   - ⚠️ El script tiene rutas y un dict de datos **hardcodeados de la corrida del 23-jun**: actualiza
     `TR` (carpeta tool-results), `SNAP`, `WINDOWS`, `CAMP`, `SHOP`, `FX` a la corrida nueva.
4. **Carga a Supabase** (MCP `apply_migration`/`execute_sql`). Si tocas vistas: `notify pgrst, 'reload schema';`
5. **Publica a Sheets:** el workflow n8n `6oh0bTHD0rV0I9il` sincroniza Supabase → Sheet maestro cada 3h
   (revisa que el toggle esté activo). Alternativa manual: `make_snapshots.py` + `build_xlsx.py` para
   CSV/xlsx locales, o crear Sheet vía connector Drive (`text/csv`).

## Clasificación de estado (por ROAS vs BEP)
- `roas ≥ BEP*1.2` → **GANADOR / escalar**
- `roas ≥ BEP` → **Rentable / mantener**
- `roas ≥ BEP*0.85` → **Marginal / vigilar-optimizar**
- `roas < BEP*0.85` o `compras=0` → **Malo / apagar**

## Esquema Supabase (columnas)
- `glmex2_ad_perf`: snapshot_date, time_window, period_start/end, product, campaign_label/id, ad_id/name,
  spend_usd, purchases, cpa_usd, roas, bep_roas, ctr, cpc_usd, cpm_usd, frequency, impressions, clicks,
  hold_rate, compl_rate, estado, accion. PK conflicto: (snapshot_date, time_window, ad_id).
- `glmex2_product_perf`: …, meta_spend/purchases/cpa/roas, shopify_orders/gross/net/aov, attribution_pct,
  net_usd, mer, fx_rate. Conflicto: (snapshot_date, time_window, product).

## Cierre
Anota el snapshot del día en memoria (`tablero-glmex2-diario`).

## Parseo de números de Meta (cuidado)
Meta devuelve formato es-ES: `$960,48 USD` (coma decimal, punto miles), `4.653` = 4653, `2,55` = 2.55.
La función `num()` de `load_supabase.py` ya lo maneja (quita no-dígitos, borra `.`, cambia `,`→`.`).
