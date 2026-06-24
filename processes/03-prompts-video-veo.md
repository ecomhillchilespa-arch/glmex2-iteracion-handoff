# Proceso 03 — Prompts de video (Nano Banana → Veo 3.1)

**Objetivo:** convertir un concepto/brief en prompts listos-para-pegar que generen el ad clip por clip.

**Estándar:** sigue SIEMPRE `reference/guias/Guia_Veo31_Prompting.md`. Ejemplos listos-para-pegar en
`reference/prompts-animacion/` (C3 independencia, C4 testigo/2-anchors, C5 industria/exposé, C6 plástico/CGI).

## Reglas duras
- **1 prompt Nano Banana = 1 keyframe (imagen). 1 prompt Veo = 1 clip** (≤8s, image-to-video).
- **Fórmula de 5 partes** con la **CINEMATOGRAFÍA al inicio**; **UN solo movimiento de cámara** por clip.
- Cada prompt va **COMPLETO en un solo bloque** (Style Block + Negative incrustados), listo para pegar.
  Nada de secciones separadas.
- **Consistencia de personaje con un ANCHOR**: genera primero un retrato y reúsalo como imagen de
  referencia en cada keyframe. **REGLA DURA: Veo no anima con dos referencias** → ningún clip usa dos
  anchors a la vez; los momentos "juntos" se resuelven con POV o por montaje.
- **El producto NO se describe**: se adjunta como imagen de referencia ("the bottle from the attached
  reference image"). Indica en qué shots se adjunta.
- **Audio muteado** (negative: no voiceover, no music). Texto en pantalla y voz en off = en EDICIÓN,
  nunca en el prompt (Veo deforma el texto).
- **Formato 9:16.** Prompts de generación en **inglés**; textos/VO en **español**.
- Un ad ≈ 8 shots; si se pide ~90s, expandir a ~16 clips (el ganador SO6 = 89.9s).

## Cartoon / claymation (track in-house "C")
Para conceptos cartoon ver `reference/guias/DOCUMENTO_MAESTRO_ANIMACION_CARTOON_IA.pdf` y los ejemplos
C3–C6. Lección de performance: los cartoon ganan **cuando reciben presupuesto** → ponlos en su propio
ad set (si comparten CBO el algoritmo casi no los reparte). Ver memoria `mensajes-ganadores-glmex2`.
