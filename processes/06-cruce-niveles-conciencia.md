# Proceso 06 — Cruce por nivel de conciencia (Meta × Clarity × Shopify)

**Objetivo:** una tabla de decisión por **producto → nivel de conciencia → ad**, con métricas de Meta +
comportamiento de Clarity + métricas de Shopify + una columna **"Qué está pasando"** (diagnóstico).

Salida real de referencia: Google Sheet `1SsbTq-IBZRufNKrupghju6v8MH6wGF9T-J9MElXymrA`.
Script: `scripts/clarity/build_cruce.py` → genera `cruce_niveles.csv` → se sube a Drive como Sheet.

## Cómo se arma
1. **Meta por ad (MTD)** desde los tool-results de `ads_get_ad_entities` (las mismas que el tablero).
   Filtra las 4 campañas (Eye CBO/E2, Petclean, Snore) y `spend ≥ $20`.
2. **Nivel de conciencia = prefijo del nombre del ad** (batch):
   - `U*` → ⚫ Desconocido (Unaware) · `PR*` → 🔴 Problema · `SO*` → 🟡 Solución · `PD*/SD*` → 🟠 Producto
   - `C#` → concepto in-house (cartoon) · `Video*`/`*E2/E3` → sin clasificar/tests · numéricos → otros.
3. **Clarity por landing** (de `landing_aggregated.json`, proceso 05): scroll % + quickback + dead.
4. **Shopify por producto** (MTD): pedidos, ingreso bruto/neto, AOV, **ATC** (= `sessions_with_cart_additions`
   por landing, sumando page+product). ⚠️ Meta NO expone add-to-cart por ad → el ATC va a **nivel producto**.
5. **"Qué está pasando"** por ad: estado por ROAS vs BEP (ver proceso 04) + nota cualitativa de
   `mensajes-ganadores-glmex2` (memoria) para los ads clave.

## Estructura de la tabla
Por producto: fila cabecera con bloque Shopify + bloque Clarity del destino; luego, por cada nivel, una
fila-resumen del nivel (gasto, compras, ROAS ponderado, estado) y los ads ≥$100 individuales; la cola
(<$100) se agrupa en "otros N ads". Columnas: Nivel · Ad · Spend · Compras · ROAS · BEP · CTR · CPC ·
CPM · Clicks · Link destino · Clarity scroll% · Clarity quickback · Clarity dead · ATC Shopify ·
Pedidos Shopify · **Qué está pasando**.

## Publicar
Codifica el CSV a base64 y crea el archivo en Drive con `create_file`, `contentMimeType:'text/csv'`
(se convierte a Google Sheet). Para versión color-codeada usar `text/html` → Google Doc nativo (ver
`artifacts/IDS.md` §técnica del conector).

## Notas / pendientes
- "Clicks de avance de página" no existe literal en Clarity; lo más cercano es **Quickback** (volver atrás).
- Para distribución de scroll por tramos (25/50/75/100%) usar el heatmap del dashboard o GA4, no la API.
