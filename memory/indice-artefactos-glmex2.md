---
name: indice-artefactos-glmex2
description: "Índice de TODOS los IDs (Supabase, n8n, Google Drive/Docs/Sheets, cuentas) del sistema de tablero+informes GL-MEX2"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 50668ea3-c7f4-46f4-bbe9-d43a7f672c4f
---

Índice maestro de IDs del proyecto tablero/informes GL-MEX2 (jun-2026). Ver [[tablero-glmex2-diario]] y [[mensajes-ganadores-glmex2]].

**Cuentas / fuentes:**
- Meta ad account GL-MEX2: `2490898558022078` (USD). Campañas: Eye CBO `120244746496800663` (BEP 1.32) · Eye E2 `120246706901420663` · Petclean `120245035555860663` (BEP 1.48) · Snore `120246245665230663` (BEP 1.25). OJO: `120246246833980663` = Car Coat (no Snore).
- Shopify: "Alegres Tienda México" (MXN). Listings: VisionPure=Eye, PetClean, QuietLab Pro=Snore.

**Supabase:** proyecto `ads-glmex2` id `ksxmjrsscdhozkdgmpne`, URL `https://ksxmjrsscdhozkdgmpne.supabase.co`. Tablas `glmex2_ad_perf`, `glmex2_product_perf`. Vistas `v_sheet_mes/7d/dia/dias/productos`. (Tras crear vistas por SQL: `notify pgrst, 'reload schema';`.)

**n8n:** workflow "GL-MEX2 — Sync Supabase a Sheet" id `6oh0bTHD0rV0I9il` (schedule 3h; falta activar toggle). Creds: Supabase ads-glmex2 = "Supabase account 2" `5c23xAG9sOmMFSpY`; Google Sheets = `5xfs81o3WcC1bYKB`. Base n8n: vmi3310874.contaboserver.net.

**Google Drive — Sheets:**
- Tablero maestro auto (n8n escribe aquí): `1IttVsboad97-ytIHMm9oa8-51aiop7a7hCMrBJ5ykMg` (pestañas Mes / "7 dias" / Productos / una por día con fecha; borrar pestaña vieja "Dias").
- Sheets CSV manuales legacy (23-jun): Mes `1ukQz78dLfkyq3G55Es_ntV28SSdIK--17w0Y-CfwOP0` · 7d `11DgmDXZk4FjVm--xUHgZeCUyb6_SIRNUhFsr5QRR7_4` · Día22 `1gosfzdaG_Yzw9mfAfSvTd7ExJohw-R1IpFn-4GsCduE`.

**Clarity (Data Export API):** proyecto `2876889344704695` (tienda Alegres MX/CL/ES). Token + scripts en `D:\Iteracion\clarity\` (clarity_token.txt, clarity_fetch.py, clarity_by_landing.py). LÍMITE 10 req/día, numOfDays 1–3. Destinos clave (scroll 3d): Eye `/pages/puremx` 44%, Petclean `/pages/petcleanadv` 43%, Snore `/pages/snoremx` 42%. OJO 34% sesiones con errores JS en el theme.

**Google Drive — Sheet cruce niveles de conciencia:** `1SsbTq-IBZRufNKrupghju6v8MH6wGF9T-J9MElXymrA` (Meta×Clarity×Shopify por nivel ⚫🔴🟡🟠, MTD jun, ads≥$100 individuales + cola agrupada, columna "Qué está pasando"). ATC = Shopify nivel-producto (Meta MCP NO expone add_to_cart).

**Google Drive — Docs (informes):**
- POR AD con tablas (el bueno): `1XLFKwT5N0m1FXhoFvdB43Q7LYbTK0OkJUDPrll4nAco`
- Batch-level (sistema+mensajes): `1KWJmqqCdL8TLAnjW2jfvAUMvBT9Ke8CDN9D9Fsa7Ptc`
- Por-ad en párrafos (obsoleto): `1ofYBTsoVDrI2GaMlW2-f96ux804LRuvoqSFB2IRsqpc`

**Técnica conector Drive:** `create_file` con `contentMimeType:'text/html'` → convierte a Google Doc NATIVO con tablas/colores/estilos (usar `bgcolor`/style inline en <td>). `text/csv` → Google Sheet. El conector NO edita ni borra ni agrega pestañas (solo crea). Binario (xlsx base64 grande) se corrompe al inlinar → no usar.

**Scripts locales:** `D:\Iteracion\sheets_glmex2\` (make_snapshots.py, load_supabase.py, build_xlsx.py). Análisis de ads (docx originales) en `D:\Iteracion\*_Analisis_Ads.docx`; texto limpio extraído en scratchpad `clean_eye/petclean/snore.txt`.
