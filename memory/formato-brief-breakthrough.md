---
name: formato-brief-breakthrough
description: Formato/estilo obligatorio para todo brief Breakthrough que pida el usuario — Word (.doc HTML) estilo VisionPure
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 84ba7a07-2cf5-4fb3-ba31-b1f202f5daa1
---

Siempre que el usuario pida un **brief Breakthrough**, entregarlo en **Word** (archivo `.doc` que es HTML maquetado, no markdown ni docx plano) con el **mismo estilo/estructura** del doc de referencia `D:\Iteracion\briefs\VisionPure_Eye_Breakthrough_Conceptos.doc` (y `PetClean_Breakthrough_Conceptos.doc`).

**Why:** el usuario se frustró cuando el brief de PetClean salió en markdown/thin y "no quedó igual" que el de VisionPure. El estándar esperado es el formato completo y maqueteado en Word, listo para producción.

**How to apply:**
- Archivo `.doc` con header HTML de Word + CSS inline (copiar el bloque `<style>` de VisionPure: h1/h2 azul `#0b3d91`, tablas con cabecera azul y filas alternadas `tr:nth-child(even)`, cajas `.razon` `.hook` `.gate` `.note` `.guion` `.tag`).
- **ENCODING (bug confirmado 2026-06-18):** usar SIEMPRE `<meta http-equiv="Content-Type" content="text/html; charset=utf-8">` + `<meta name="ProgId" content="Word.Document">`. NO usar la forma corta `<meta charset="utf-8">` → Word la IGNORA, lee el archivo como Windows-1252 y todas las tildes/ñ salen como símbolos raros (á→Ã¡). El archivo se escribe en UTF-8; el tag es lo que decide.
- **SIEMPRE 9 conceptos / 9 guiones** (regla fija del usuario, 2026-06-18). Cada uno ataca un vértice psicológico DISTINTO o más profundo que el ganador ("deeper or different"). Si un producto da menos vértices obvios, igual llegar a 9 incluyendo ángulos racionales (costo/economía) y proof-led (demostración visual antes/después), no solo emocionales.
- Estructura: Gate de Inputs → PARTE 1 Deconstrucción del ganador (8 pasos, tabla con columna **Razón**) → PARTE 2 Territorio sin explotar → (si hay advertorial) sección de alineación Regla 5 → PARTE 3 Conceptos (los 9).
- **Cada concepto** lleva: 💡 Idea+Razón · tabla Persona/Funnel/Tono/Key Messages/Concepto-a-testear · **H:** hook · tabla "Mecanismo del hook (4 gatillos)" con Razón · Enemigo+Blame shift · **Script Flow** (Sección/Voz-Guion/Visual/Texto en pantalla) · **📜 Guion corrido** listo para grabar · 🎯 Hipótesis (5 razones + métricas objetivo) · 🎨 Visual · 📌 Ejecución A/B/C · Quality gates. Cerrar con Orden de testeo (tabla por rounds) + Constantes/Compliance/Base.
- **Regla del doc:** cada afirmación lleva su **Razón**. Los dos elementos que más se olvidan y son obligatorios: **Script Flow** y **Guion corrido** por concepto.
- **Verificar el render** antes de entregar: balance de tags + abrir vía Word COM (PowerShell `Word.Application`, exportar a PDF) o screenshot con Edge `--headless=new`. Limpiar temporales después.

Relacionado: [[proyecto-iteracion-briefs]], [[frameworks-marketing-carpeta]].
