# Proceso 01 — Análisis de videos ganadores

**Objetivo:** convertir un ad en video en un guion + desglose de tomas + hipótesis de por qué
funciona, para alimentar la iteración de briefs (proceso 02).

## Input
- El video ganador en `videos/<nombre>.mp4` (lo deja el usuario, o se baja con
  `scripts/utils/fb-fetch.sh <token_file> <act_id> videos/ "patrón del título"`).
- La cuenta/campaña y métricas las indica el usuario o se sacan vía MCP de Meta Ads.

## Pasos
1. **Extrae tomas y subtítulos con ffmpeg.** Quema los subtítulos / saca keyframes por toma para
   reconstruir el guion y la estructura visual. (Frames a una carpeta `_frames`; no se versiona.)
2. **Visión:** describe cada toma (qué se ve, texto en pantalla, on-screen, transición) y transcribe la
   voz en off. Reconstruye el **guion corrido** y el **desglose por toma** (timecode → visual → copy).
3. **Clasifica:** nivel de conciencia (⚫🔴🟡🟠), ángulo/mensaje, villano, oferta, mecanismo, autoridad.
4. **Hipótesis:** por qué gana o pierde (cruza con métricas reales: ROAS vs BEP, CTR, hold/completion).
5. **Guarda** en `analisis-videos/<slug>--analisis.md`.

## Output (molde)
Mira ejemplos reales en `examples/analisis-videos/`:
- `so6-ad37-visionpure--analisis.md` — deconstrucción del ganador (el molde principal).
- `eye-angulos-faltantes--analisis.md` — qué ángulos faltan por explotar.
- `fotos-imagenes-eye--analisis.md` — qué funciona en imagen (oferta vs educacional).
- `VisionPure_Eye_Top10-Bottom10_Analisis.doc` — 20 ads → 11 creativos con mensaje + hipótesis.

## Reglas
- CTR alto ≠ venta: si retiene pero no convierte, el problema es oferta/landing, no el hook.
- "Mata el ad, no el mensaje": dos ejecuciones del mismo guion pueden dar ROAS opuestos.
- Conserva el **mecanismo** (ej. VisionPure: "entra por el párpado" vs "la cápsula se destruye en el estómago").
