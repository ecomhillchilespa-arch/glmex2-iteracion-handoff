# 🎬 C3 (versión JSON) — "Le pedí a mi hijo que leyera mi receta"
## Veo 3.1 Pro · JSON prompting · 9:16 · 8 clips ≤8s

> **A/B contra `C3_independencia_prompts.md` (prosa).** Mismo guion, misma cara Roberto, mismo Style Block — solo cambia el formato del prompt.
> **Cómo se usa:** pega el bloque JSON completo en la caja de prompt de Veo/Flow. Adjunta el ANCHOR de Roberto en todos los shots de personaje y la imagen del producto VisionPure en Shots 5 y 8.
> **Audio muteado** (`audio: "none"`). Texto en pantalla y VO = en EDICIÓN.
> **Adaptaciones a nuestro caso** que el artículo de tenten no trae: añadí `negative_prompt`, fijé `audio: "none"`, y `aspect_ratio: "9:16"`.

---

## 🧍 ANCHOR — cara del avatar (Nano Banana, generar PRIMERO, sigue siendo texto)
```
Photorealistic portrait, a dignified 68-year-old Mexican man: warm olive-tan weathered skin, deep gentle smile lines, neatly combed silver-grey hair, thick salt-and-pepper mustache, bushy grey eyebrows, calm brown eyes, lean build, soft beige cardigan over white collared shirt, thin reading glasses on a cord. Seated at a wooden kitchen table, soft window light from the left. Intimate documentary realism, warm amber/sepia color grade, soft tungsten light mixed with gentle window daylight, lived-in middle-class Mexican home, 50mm lens, shallow depth of field, subtle film grain, photorealistic, 9:16 vertical.
```

---

## 🔁 BLOQUE COMPARTIDO (idéntico en cada shot — es el equivalente JSON del "Style Block")
Estos dos objetos se repiten dentro de cada prompt de abajo para forzar consistencia. No los generes sueltos; ya están incrustados en cada SHOT.
```json
"global_style": {
  "look": "intimate documentary realism, photorealistic, 50mm lens, shallow depth of field, subtle film grain",
  "color": "warm amber / sepia color grade",
  "lighting": "soft tungsten light mixed with gentle window daylight, lived-in middle-class Mexican home",
  "aspect_ratio": "9:16"
},
"continuity": {
  "characters": [
    { "id": "roberto", "description": "dignified 68-year-old Mexican man, silver-grey hair, salt-and-pepper mustache, beige cardigan over white collared shirt, reading glasses on a cord", "reference_images": ["ANCHOR_roberto"] }
  ],
  "props": ["small medicine bottle", "VisionPure spray bottle (attached product reference, Shots 5 & 8 only)"],
  "lighting": "consistent warm tungsten + window daylight across all shots"
}
```

---

## SHOT 1 — HOOK · adjuntar ANCHOR
```json
{
  "version": "veo-3.1",
  "output": { "aspect_ratio": "9:16", "duration_sec": 8, "fps": 24, "resolution": "1080p" },
  "global_style": {
    "look": "intimate documentary realism, photorealistic, 50mm lens, shallow depth of field, subtle film grain",
    "color": "warm amber / sepia color grade",
    "lighting": "soft tungsten light mixed with gentle window daylight, lived-in middle-class Mexican home",
    "aspect_ratio": "9:16"
  },
  "continuity": {
    "characters": [
      { "id": "roberto", "description": "dignified 68-year-old Mexican man, silver-grey hair, salt-and-pepper mustache, beige cardigan, reading glasses on a cord", "reference_images": ["ANCHOR_roberto"] },
      { "id": "son", "description": "38-year-old son, short dark hair, light stubble, dark-blue henley" }
    ],
    "props": ["small medicine bottle"]
  },
  "scene": {
    "id": "shot1_hook",
    "shot": { "type": "medium two-shot", "framing": "both men at the kitchen table, father's face readable", "camera": "slow handheld push-in" },
    "action": "Roberto extends a small medicine bottle to his adult son, who takes it and squints to read the tiny label; the father's eyes lower with quiet shame.",
    "environment": "warm lived-in middle-class Mexican kitchen",
    "mood": "tender, emotional, intimate",
    "audio": "none",
    "negative_prompt": "distorted product label, warped text, on-screen text, extra fingers, deformed hands, plastic-looking skin, oversaturated colors, watermark, shaky unstable motion, multiple conflicting camera moves, surgical imagery, young models, low resolution; no background music, no voiceover, no spoken words"
  }
}
```
**Texto (edición):** `"Mi propia medicina"` · **VO:** *"El día que tuve que pedirle a mi hijo que me leyera la etiqueta de mi propia medicina… ahí supe que algo tenía que cambiar."*

---

## SHOT 2 — PÉRDIDA DE INDEPENDENCIA · adjuntar ANCHOR
```json
{
  "version": "veo-3.1",
  "output": { "aspect_ratio": "9:16", "duration_sec": 8, "fps": 24, "resolution": "1080p" },
  "global_style": {
    "look": "intimate documentary realism, photorealistic, 50mm lens, shallow depth of field, subtle film grain",
    "color": "warm amber / sepia color grade",
    "lighting": "dim warm dusk light, lived-in middle-class Mexican home",
    "aspect_ratio": "9:16"
  },
  "continuity": {
    "characters": [
      { "id": "roberto", "description": "dignified 68-year-old Mexican man, silver-grey hair, salt-and-pepper mustache, beige cardigan, reading glasses on a cord", "reference_images": ["ANCHOR_roberto"] }
    ],
    "props": ["car keys", "wooden drawer"]
  },
  "scene": {
    "id": "shot2_independence_loss",
    "shot": { "type": "close-up", "framing": "hands and partial wistful face", "camera": "slow tilt down" },
    "action": "Roberto's hand lowers a set of car keys into a drawer and gently closes it, resigned posture.",
    "environment": "warm home interior at dusk",
    "mood": "melancholic, quiet",
    "audio": "none",
    "negative_prompt": "distorted product label, warped text, on-screen text, extra fingers, deformed hands, plastic-looking skin, oversaturated colors, watermark, shaky unstable motion, multiple conflicting camera moves, surgical imagery, young models, low resolution; no background music, no voiceover, no spoken words"
  }
}
```
**Texto (edición):** `"No quería depender"` · **VO:** *"Primero dejé de manejar de noche. Después me costaba el periódico. Y lo peor… era sentir que me estaba volviendo una carga."*

---

## SHOT 3 — CÁPSULA QUE NO SIRVE · adjuntar ANCHOR
```json
{
  "version": "veo-3.1",
  "output": { "aspect_ratio": "9:16", "duration_sec": 8, "fps": 24, "resolution": "1080p" },
  "global_style": {
    "look": "intimate documentary realism, photorealistic, 50mm lens, shallow depth of field, subtle film grain",
    "color": "warm amber / sepia color grade",
    "lighting": "soft tungsten light mixed with gentle window daylight, lived-in middle-class Mexican home",
    "aspect_ratio": "9:16"
  },
  "continuity": {
    "characters": [
      { "id": "roberto", "description": "dignified 68-year-old Mexican man, silver-grey hair, salt-and-pepper mustache, beige cardigan, reading glasses on a cord", "reference_images": ["ANCHOR_roberto"] }
    ],
    "props": ["generic amber-white capsule supplement bottle"]
  },
  "scene": {
    "id": "shot3_useless_capsule",
    "shot": { "type": "close-up", "framing": "palm and face", "camera": "static locked-off" },
    "action": "Roberto tips two capsules into his palm, looks at them, gives a small disappointed head shake.",
    "environment": "warm kitchen table",
    "mood": "disappointed, resigned",
    "audio": "none",
    "negative_prompt": "distorted product label, warped text, on-screen text, extra fingers, deformed hands, plastic-looking skin, oversaturated colors, watermark, shaky unstable motion, multiple conflicting camera moves, surgical imagery, young models, low resolution; no background music, no voiceover, no spoken words"
  }
}
```
**Texto (edición):** `"No cambió nada"` · **VO:** *"Tomaba cápsulas de luteína. No cambiaron nada."*

---

## SHOT 4 — MECANISMO (diagrama CGI) · sin referencias
```json
{
  "version": "veo-3.1",
  "output": { "aspect_ratio": "9:16", "duration_sec": 8, "fps": 24, "resolution": "1080p" },
  "global_style": {
    "look": "macro motion-graphics, photorealistic 3D render, minimal, elegant, premium",
    "color": "warm amber and teal palette, soft glow",
    "lighting": "soft internal glow",
    "aspect_ratio": "9:16"
  },
  "scene": {
    "id": "shot4_mechanism",
    "shot": { "type": "macro motion-graphics", "framing": "stylized eye + capsule path", "camera": "slow push-in" },
    "action": "Glowing particles travel from a closed human eyelid into the eye and light up the macula; beside it the capsule-in-stomach path dims, gets crossed out and fades.",
    "environment": "abstract dark premium background",
    "mood": "clear, scientific, elegant — not gory",
    "audio": "none",
    "negative_prompt": "distorted text, on-screen text, gory imagery, oversaturated colors, watermark, shaky unstable motion, multiple conflicting camera moves, low resolution; no background music, no voiceover, no spoken words"
  }
}
```
**Texto (edición):** `"Directo al ojo"` · **VO:** *"Mi hijo investigó: las cápsulas casi no llegan al ojo, se pierden en la digestión."*

---

## SHOT 5 — APLICA EL SPRAY · adjuntar ANCHOR + IMAGEN PRODUCTO
```json
{
  "version": "veo-3.1",
  "output": { "aspect_ratio": "9:16", "duration_sec": 8, "fps": 24, "resolution": "1080p" },
  "global_style": {
    "look": "intimate documentary realism, photorealistic, 50mm lens, shallow depth of field, subtle film grain",
    "color": "warm amber / sepia color grade",
    "lighting": "soft tungsten light mixed with gentle window daylight, lived-in middle-class Mexican home",
    "aspect_ratio": "9:16"
  },
  "continuity": {
    "characters": [
      { "id": "roberto", "description": "dignified 68-year-old Mexican man, silver-grey hair, salt-and-pepper mustache, beige cardigan, reading glasses on a cord", "reference_images": ["ANCHOR_roberto"] },
      { "id": "son", "description": "38-year-old son, reassuring hand on father's shoulder" }
    ],
    "props": ["VisionPure spray bottle (attached product reference image)"]
  },
  "scene": {
    "id": "shot5_apply_spray",
    "shot": { "type": "close-up", "framing": "face with closed eyes, mist over eyelids", "camera": "static, soft slow motion" },
    "action": "Roberto with eyes gently closed applies the VisionPure bottle as a soft fine mist over his closed eyelids; his son's reassuring hand on his shoulder.",
    "environment": "warm kitchen, soft window light",
    "mood": "hopeful, serene",
    "audio": "none",
    "negative_prompt": "distorted product label, warped text, on-screen text, extra fingers, deformed hands, plastic-looking skin, oversaturated colors, watermark, shaky unstable motion, multiple conflicting camera moves, surgical imagery, young models, low resolution; no background music, no voiceover, no spoken words"
  }
}
```
**Texto (edición):** `"Sobre los párpados cerrados"` · **VO:** *"Me consiguió un spray que se aplica sobre los párpados cerrados y entra directo."*

---

## SHOT 6 — LEE SOLO · adjuntar ANCHOR
```json
{
  "version": "veo-3.1",
  "output": { "aspect_ratio": "9:16", "duration_sec": 8, "fps": 24, "resolution": "1080p" },
  "global_style": {
    "look": "intimate documentary realism, photorealistic, 50mm lens, shallow depth of field, subtle film grain",
    "color": "warm amber / sepia color grade",
    "lighting": "soft morning window light, lived-in middle-class Mexican home",
    "aspect_ratio": "9:16"
  },
  "continuity": {
    "characters": [
      { "id": "roberto", "description": "dignified 68-year-old Mexican man, silver-grey hair, salt-and-pepper mustache, beige cardigan, reading glasses on a cord", "reference_images": ["ANCHOR_roberto"] }
    ],
    "props": ["small medicine bottle"]
  },
  "scene": {
    "id": "shot6_reads_alone",
    "shot": { "type": "medium close-up", "framing": "Roberto alone, face and bottle", "camera": "slow dolly-in" },
    "action": "Roberto reads the small label of his own medicine bottle unaided, then smiles softly and proudly.",
    "environment": "warm kitchen, morning light",
    "mood": "uplifting, restrained, proud",
    "audio": "none",
    "negative_prompt": "distorted product label, warped text, on-screen text, extra fingers, deformed hands, plastic-looking skin, oversaturated colors, watermark, shaky unstable motion, multiple conflicting camera moves, surgical imagery, young models, low resolution; no background music, no voiceover, no spoken words"
  }
}
```
**Texto (edición):** `"Otra vez yo"` · **VO:** *"Unas semanas después, leí la dosis de mi medicina yo solo."*

---

## SHOT 7 — MANEJA DE DÍA · adjuntar ANCHOR
```json
{
  "version": "veo-3.1",
  "output": { "aspect_ratio": "9:16", "duration_sec": 8, "fps": 24, "resolution": "1080p" },
  "global_style": {
    "look": "intimate documentary realism, photorealistic, 50mm lens, shallow depth of field, subtle film grain",
    "color": "warm amber / sepia color grade",
    "lighting": "soft natural daylight through windshield",
    "aspect_ratio": "9:16"
  },
  "continuity": {
    "characters": [
      { "id": "roberto", "description": "dignified 68-year-old Mexican man, silver-grey hair, salt-and-pepper mustache, beige cardigan, reading glasses on a cord", "reference_images": ["ANCHOR_roberto"] }
    ],
    "props": ["car steering wheel"]
  },
  "scene": {
    "id": "shot7_drives_daytime",
    "shot": { "type": "medium shot", "framing": "Roberto at the wheel, both hands", "camera": "static locked-off dashboard-mounted" },
    "action": "Roberto drives in daylight, glancing ahead, relaxed and at ease with a small content smile.",
    "environment": "car interior, warm daytime",
    "mood": "free, content",
    "audio": "none",
    "negative_prompt": "distorted product label, warped text, on-screen text, extra fingers, deformed hands, plastic-looking skin, oversaturated colors, watermark, shaky unstable motion, multiple conflicting camera moves, surgical imagery, young models, low resolution; no background music, no voiceover, no spoken words"
  }
}
```
**Texto (edición):** `"Volví a manejar de día"` · **VO:** *"Y volví a manejar de día, sin que nadie me acompañara. Volví a ser yo."*

---

## SHOT 8 — CTA · adjuntar ANCHOR + IMAGEN PRODUCTO
```json
{
  "version": "veo-3.1",
  "output": { "aspect_ratio": "9:16", "duration_sec": 8, "fps": 24, "resolution": "1080p" },
  "global_style": {
    "look": "intimate documentary realism, photorealistic, 50mm lens, shallow depth of field, subtle film grain",
    "color": "warm amber / sepia color grade",
    "lighting": "soft tungsten light mixed with gentle window daylight, lived-in middle-class Mexican home",
    "aspect_ratio": "9:16"
  },
  "continuity": {
    "characters": [
      { "id": "roberto", "description": "dignified 68-year-old Mexican man, silver-grey hair, salt-and-pepper mustache, beige cardigan, reading glasses on a cord", "reference_images": ["ANCHOR_roberto"] }
    ],
    "props": ["VisionPure spray bottle (attached product reference image, soft-focus foreground)"]
  },
  "scene": {
    "id": "shot8_cta",
    "shot": { "type": "medium close-up", "framing": "Roberto to camera, bottle soft-focus foreground", "camera": "slow dolly-in" },
    "action": "Roberto looks warmly into camera and gives a small reassuring nod; the VisionPure bottle rests softly in the foreground.",
    "environment": "warm kitchen table",
    "mood": "dignified, at peace, reassuring",
    "audio": "none",
    "negative_prompt": "distorted product label, warped text, on-screen text, extra fingers, deformed hands, plastic-looking skin, oversaturated colors, watermark, shaky unstable motion, multiple conflicting camera moves, surgical imagery, young models, low resolution; no background music, no voiceover, no spoken words"
  }
}
```
**Texto (edición):** `"Tu independencia"` (tarjeta final con producto) · **VO:** *"Si tú también empezaste a depender de alguien para cosas que antes hacías solo… se llama VisionPure. El enlace está aquí abajo."*

---
*C3 versión JSON · A/B contra la versión prosa. Método: developer.tenten.co/veo-331-pro-json-prompting · Estándar del proyecto: `documentos/Guia_Veo31_Prompting.md`.*
*Nota: el campo `reference_images` documenta qué adjuntar; en Flow/Veo la imagen se sube por la UI, no por la ruta del JSON.*
</content>
</invoke>
