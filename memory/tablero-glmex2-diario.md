---
name: tablero-glmex2-diario
description: "Tablero diario de campañas GL-MEX2 (Meta+Shopify) — 3 vistas (Mes/7d/Día), cómo actualizarlo"
metadata: 
  node_type: memory
  type: project
  originSessionId: 50668ea3-c7f4-46f4-bbe9-d43a7f672c4f
---

Tablero de trabajo de campañas en cuenta **GL-MEX2** (Meta ad_account `2490898558022078`, USD) cruzado con **Shopify "Alegres Tienda México"** (MXN). Productos: Eye, Snore, Petclean. Ver [[proyecto-iteracion-briefs]].

**Rutina (el usuario la pide a diario):** actualizar 3 vistas:
- **Mes (MTD)**: del día 1 del mes a hoy (NO 30 días fijos). Se sobrescribe.
- **7 días**: últimos 7 (ej. 16–22). Se sobrescribe.
- **Día**: el día anterior (ayer), SIEMPRE una hoja NUEVA permanente con su fecha. La 1ª fue Día 2026-06-22.

**Umbral confirmado:** solo videos con gasto ≥ $20 (capturan ~95% del gasto; las campañas CBO tienen 230+ anuncios activos pero la mayoría gasta centavos).

**Campaign IDs:** Eye CBO `120244746496800663` (BEP 1.32) · Eye E2 `120246706901420663` · Petclean `120245035555860663` (BEP 1.48) · Snore `120246245665230663` (BEP 1.25). OJO: `120246246833980663` es **Car Coat**, no Snore.

**Estado por video** según ROAS vs BEP: 0 compras→Sin conversiones/Apagar; ≥BEP·1.2→GANADOR/Escalar; ≥BEP→Rentable/Mantener; ≥BEP·0.85→Marginal/Vigilar; resto→Malo/Apagar. Hook rate 2seg NO disponible en la cuenta → uso Hold% (ThruPlay/impr) y Compl% (p100/impr). FX 1 USD = 18.5 MXN (editable); MER = ventas netas USD / gasto Meta.

**Pipeline (en `D:\Iteracion\sheets_glmex2\`):** 1) bajo Meta nivel-campaña + nivel-anuncio (3 ventanas) y Shopify ShopifyQL por producto; 2) edito los dicts de fechas/datos en `make_snapshots.py` y corro → genera `mes.csv`, `7dias.csv`, `daily/Dia_YYYY-MM-DD.csv`; 3) subo cada CSV a Drive con `create_file` (text/csv → Sheet nativo).

**LIMITACIÓN del conector Drive:** solo CREA archivos (no edita celdas, no agrega pestañas, no borra). Por eso NO se puede tener 1 Sheet con pestañas Mes/7d/Día de forma confiable (el xlsx multi-pestaña requiere subir binario base64 ~27k chars y se corrompe). Solución: **3 Google Sheets separados** (CSV nativo = confiable). Cada update crea archivos nuevos (URL cambia); los viejos de Mes/7d se pueden borrar a mano. `build_xlsx.py` existe por si algún día hay forma de subir xlsx.

**URLs sheets CSV manuales (23-jun, legacy):** Mes `1ukQz78dLfkyq3G55Es_ntV28SSdIK--17w0Y-CfwOP0` · 7d `11DgmDXZk4FjVm--xUHgZeCUyb6_SIRNUhFsr5QRR7_4` · Día22 `1gosfzdaG_Yzw9mfAfSvTd7ExJohw-R1IpFn-4GsCduE`.

## Arquitectura NUEVA (Supabase → n8n → 1 Sheet) — en construcción (23-jun-2026)
Reemplaza los "mil sheets". El usuario pidió: BD propia + n8n manda a Supabase y luego a UNA sheet que se actualiza in-place.
- **Proyecto Supabase NUEVO y separado de SAC:** `ads-glmex2` (id `ksxmjrsscdhozkdgmpne`, us-east-1, free). URL `https://ksxmjrsscdhozkdgmpne.supabase.co`.
- **Tablas (public):** `glmex2_ad_perf` (por video) y `glmex2_product_perf` (por producto). Clave upsert: ad = (snapshot_date,time_window,ad_id); prod = (snapshot_date,time_window,product). Col `window` es reservada → se llama `time_window`. RLS on (service_role bypassa).
- **Carga:** yo (MCP) corro `D:\Iteracion\sheets_glmex2\load_supabase.py <prod|day|7d|mtd|all>` → imprime SQL upsert → lo ejecuto con Supabase `execute_sql`. (No tengo service key ni DB pass para conectar Python directo.)
- **Sheet maestra única (n8n target):** `1IttVsboad97-ytIHMm9oa8-51aiop7a7hCMrBJ5ykMg`.
- **n8n creds existentes:** Google Sheets `5xfs81o3WcC1bYKB`, Shopify AegresMexico `oiP0QI3gxOoCe7nt`, Supabase (apunta a SAC) `LBzRPTKifz6qOPhA`. **FALTA:** credencial Supabase/Postgres para el proyecto NUEVO `ads-glmex2` (yo NO puedo crear credenciales en n8n; el usuario la agrega en la UI con la URL de arriba + service_role key del dashboard).
- **Vistas Supabase para el sync:** `v_sheet_mes`, `v_sheet_7d` (último snapshot), `v_sheet_dias` (histórico, con `row_key=period_end|ad_id`), `v_sheet_productos` (último snapshot 3 ventanas, `row_key=time_window|product`).
- **Workflow n8n creado:** "GL-MEX2 — Sync Supabase a Sheet" id `6oh0bTHD0rV0I9il`. Schedule cada 3h → 4 ramas: Mes/7d/Productos = crear pestaña (onError continue) + limpiar + leer vista + append (refresh completo); Días = crear pestaña + leer + appendOrUpdate por `row_key`. Pestañas en sheet: Mes, "7 dias", Productos, Dias (sin acentos).
- **Credenciales (RESUELTO 23-jun):** n8n auto-asignó la credencial vieja "Supabase account" (`LBzRPTKifz6qOPhA`, apunta a SAC) → daba "tabla no existe". El usuario creó **"Supabase account 2"** (`5c23xAG9sOmMFSpY`, apunta a ads-glmex2) y yo la fijé en los 4 nodos "Leer v_sheet_*" vía update_workflow. Google Sheets = "Google Sheets account 2" (`5xfs81o3WcC1bYKB`). OJO al crear vistas nuevas por SQL: correr `notify pgrst, 'reload schema';` o el nodo Supabase no las ve.
- **Estado: FUNCIONA y validado en re-ejecución (23-jun).** Workflow rediseñado a 19 nodos. Aprendizajes clave:
  - El nodo "create sheet" con `onError:continueRegularOutput` devuelve salida VACÍA al fallar (pestaña ya existe) → corta la cadena. FIX: sacar "Asegurar pestana" del camino de datos (rama lateral muerta colgada del trigger). Las ramas de datos (limpiar→leer→escribir) cuelgan directo del trigger.
  - `appendOrUpdate` falla en pestaña recién creada vacía (sin encabezados) → error `columns.schema`. FIX: usar **clear + append** en todas.
  - Mes/7d/Productos: clear(wholeSheet)+append (refresh completo, sin duplicados).
  - **Pestaña del día = nombre con la FECHA** (vista `v_sheet_dia` = último día). 3 ramas: leer→crear(executeOnce, title={{$json.fecha}}), leer→limpiar(executeOnce, sheetName={{fecha}}), leer→append. Orden por conexión: crear→limpiar→escribir. Cada día = pestaña nueva; las viejas quedan intactas (histórico). row_key=fecha|ad_id en la vista.
  - Vista nueva: `v_sheet_dia` (último día). La pestaña vieja única "Dias" quedó obsoleta → el usuario puede borrarla a mano.
- **Pendiente usuario:** activar el toggle del workflow (schedule cada 3h). Borrar pestaña obsoleta "Dias".
