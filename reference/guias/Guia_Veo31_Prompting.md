# Guía Maestra de Prompting para Veo 3.1 — Videos (referencia del proyecto)

> Estándar operativo para construir TODOS los prompts de video del proyecto. Resumen accionable de la guía completa entregada por el usuario (2026-06-16).

## 7 reglas de oro
1. **Un clip = una idea.** Clips de 4/6/8s. Una acción clara por clip.
2. **Lenguaje de cine, no de charla** ("plano medio, dolly-in lento", no "una toma que se acerca").
3. **Front-load la cinematografía** (el tipo de plano va al inicio del prompt).
4. **Una sola cámara por clip** (no paneo+zoom+tracking juntos → movimiento inestable).
5. **Siempre negative prompt.**
6. **La consistencia se construye:** imagen de referencia + first/last frame + Style Block idéntico en todos los clips.
7. **Audio dirigido — o muteado.** Para ads casi siempre: mutea el audio de Veo y pon voz/música propia en edición.

## Fórmula de 5 partes
`[Cinematografía] + [Sujeto] + [Acción] + [Contexto] + [Estilo y ambiente]`

## Consistencia entre clips (3 técnicas)
- **Style Block:** párrafo idéntico de estética/luz/lente pegado al final de cada prompt.
- **I2V / Ingredients:** imagen hero de producto/persona (Nano Banana o foto real) reusada en cada clip → fidelidad.
- **First & Last Frame:** último frame del clip A = primer frame del clip B → continuidad invisible.

Flujo: `Nano Banana (keyframe) → Veo I2V (clip 1) → último frame → first/last frame (clip 2) → repetir`.

## Capacidades / límites Veo 3.1
- 720p/1080p · 16:9 o 9:16 · clips 4/6/8s (no largos de una sola vez → se ensambla).
- I2V, Ingredients-to-Video, First&Last Frame, Add/Remove (corre en Veo 2, sin audio).
- **El texto en pantalla lo deforma → todo texto/precio/CTA va en EDICIÓN.**
- No subir personas reales identificables ni nombres de famosos.
- Manos/dedos pueden fallar → 3-4 variantes y elegir.

## Negative prompt base (ajustar por producto)
```
distorted product label, warped text, extra fingers, deformed hands, blurry product,
plastic-looking skin, oversaturated colors, watermark, logo glitch, shaky unstable motion,
multiple conflicting camera moves, low resolution, jpeg artifacts.
```
Para mutear audio añadir: `no background music, no voiceover, no spoken words`.

## Beats de un ad
Hook → Problema → Reveal → Demo → Beneficios → Prueba social/Antes-Después → CTA.
- 30s ≈ 4 clips · 60-90s ≈ 7+ beats (1 clip c/u) · 3-10min: expandir Demo/Beneficios por tandas.

## Costos
Iterar en **Fast**, render final en **Quality**. ~60s ≈ 8-12 clips con descartes. Créditos Flow no se acumulan.

## Vocabulario clave
- Cámara: dolly in/out, tracking, crane, pan, tilt, POV, orbit, handheld, static/locked-off.
- Encuadre: extreme close-up, close-up, medium, wide, establishing, low/high angle, OTS, two-shot.
- Lente/foco: shallow DOF, deep focus, macro, rack focus, soft focus, bokeh.
- Luz: soft natural, golden hour, rim light, high-key, low-key, studio softbox.
- Acabado: photorealistic high-end commercial, UGC handheld iPhone look, cinematic film grain.
- Truco UGC: `micro jitters, slight exposure shifts, breathing focus, handheld iPhone footage`.

## Checklist por clip
Plano al inicio · una acción + una cámara · 5 partes · Style Block idéntico · referencia de producto (I2V) · negative prompt · texto/CTA en edición · iterar en Fast · ratio correcto (9:16).
