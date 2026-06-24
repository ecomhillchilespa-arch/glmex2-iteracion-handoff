# IDs de artefactos en la nube (GL-MEX2)

> Estos son **identificadores de recursos**, no secretos. Las llaves/tokens van en `.env` (ver `SECURITY.md`).
> Para tocar cualquiera de estos, el usuario debe tener el MCP connector correspondiente conectado.

## Cuentas / fuentes
- **Meta ad account GL-MEX2:** `2490898558022078` (USD).
  - Eye CBO `120244746496800663` (BEP ROAS 1.32) · Eye E2 `120246706901420663`
  - Petclean `120245035555860663` (BEP 1.48)
  - Snore `120246245665230663` (BEP 1.25)
  - ⚠️ `120246246833980663` = Car Coat (NO es Snore)
- **Shopify:** "Alegres Tienda México" (MXN), dominio `rhr9uq-tp.myshopify.com`.
  Listings: VisionPure=Eye, PetClean, QuietLab Pro=Snore. (También tiendas CL y ES.)
- **Microsoft Clarity:** proyecto `2876889344704695` (cubre tráfico MX/CL/ES).

## Supabase
- Proyecto `ads-glmex2`, id `ksxmjrsscdhozkdgmpne`, URL `https://ksxmjrsscdhozkdgmpne.supabase.co`
- Tablas: `glmex2_ad_perf`, `glmex2_product_perf`
- Vistas: `v_sheet_mes`, `v_sheet_7d`, `v_sheet_dia`, `v_sheet_dias`, `v_sheet_productos`
- Tras crear/alterar vistas por SQL: `notify pgrst, 'reload schema';`

## n8n
- Workflow "GL-MEX2 — Sync Supabase a Sheet" id `6oh0bTHD0rV0I9il` (schedule 3h; revisar toggle activo)
- Creds: Supabase ads-glmex2 = "Supabase account 2" `5c23xAG9sOmMFSpY` · Google Sheets `5xfs81o3WcC1bYKB`
- Base n8n: `vmi3310874.contaboserver.net`

## Google Drive — Sheets
- **Tablero maestro auto** (n8n escribe aquí): `1IttVsboad97-ytIHMm9oa8-51aiop7a7hCMrBJ5ykMg`
  (pestañas Mes / "7 dias" / Productos / una por día)
- **Cruce por nivel de conciencia** (Meta×Clarity×Shopify): `1SsbTq-IBZRufNKrupghju6v8MH6wGF9T-J9MElXymrA`
- Legacy CSV manuales: Mes `1ukQz78dLfkyq3G55Es_ntV28SSdIK--17w0Y-CfwOP0` · 7d `11DgmDXZk4FjVm--xUHgZeCUyb6_SIRNUhFsr5QRR7_4`

## Google Drive — Docs (informes de creativo)
- **POR AD con tablas (el bueno):** `1XLFKwT5N0m1FXhoFvdB43Q7LYbTK0OkJUDPrll4nAco`
- Batch-level (sistema+mensajes): `1KWJmqqCdL8TLAnjW2jfvAUMvBT9Ke8CDN9D9Fsa7Ptc`

## Técnica del conector de Drive (importante)
`create_file` con `contentMimeType:'text/html'` → Google Doc NATIVO con tablas/colores (usa `bgcolor`/style
inline en `<td>`). `text/csv` (o base64 + ese mime) → Google Sheet. El connector **solo crea**, no edita
ni borra ni agrega pestañas. Binario xlsx grande inlinado se corrompe → no usar; reconstruir Sheet vía CSV.
