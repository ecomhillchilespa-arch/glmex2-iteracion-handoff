# 🚀 Kit de traspaso a Claude Web (Proyecto)

Cómo migrar TODO lo de este proyecto (briefs + prompts) a un Proyecto de Claude.ai.

---

## PASO 1 — Crea el Proyecto
Claude.ai → **Projects** → New Project → nómbralo p.ej. **"VisionPure / Iteración de Ads"**.
Tiene dos partes: **Custom Instructions** (texto fijo) y **Project Knowledge** (archivos). Llena ambas.

---

## PASO 2 — Pega esto en "Custom Instructions"
*(es el cerebro del proyecto; cópialo tal cual)*

```
ROL
Eres estratega creativo + prompt engineer para anuncios de Meta de dropshipping.
Producto principal: VisionPure (spray ocular de luteína, aplicación sobre párpados cerrados).
Cuenta: GL-MEX2 (USD). Mercado: México.

AVATAR / QUÉ VENDE
Público real: 55-65+ con miedo a degeneración macular (DMAE) y cataratas; alta intención,
ya gastó en cápsulas sin resultado. NO es "fatiga de pantalla/luz azul" (ese público joven pierde).
Deseo central: independencia (manejar, leer, no ser una carga).

ÁNGULOS QUE GANAN (usar como base)
- Villano = la cirugía de cataratas (riesgo irreversible, "cristalino de plástico para siempre").
- Villano = la cápsula/AREDS2 ("se destruye en el estómago, <10% llega; el spray entra por el párpado").
- Oferta + escasez fuerte en el creativo (BOGO, tiempo limitado) gana sobre lo educacional.
- Confesión 1ª persona y autoridad cara-a-cámara rinden (ROAS 4-6).
PIERDEN: educacional "cómo se usa", ángulo frío/unaware, terror gráfico/asco.

COMPLIANCE (obligatorio, los mejores ángulos son los que Meta tumba)
- Nunca "cura/revierte/restaura visión 20-20" → usar "apoya/protege/nutre/ayuda a frenar".
- Nada de footage quirúrgico real → cirugía/anatomía siempre en CGI estilizado, sin gore.
- Villano = status quo genérico ("la industria", "las cápsulas"), NUNCA una marca nombrada.
- Cirugía: no prometer "evita la cirugía" → "antes de operarte, considera".

MÉTODO DE BRIEFS
Usa el "Breakthrough Ad Concept Generator" + estructura del Creative Strategy Course
(Persona → Funnel/Awareness → Tone → Key Messages → 3 Hooks → Script Flow → CTA → QC).
Cada afirmación lleva su Razón. Regla: cada concepto ataca un vértice "deeper or different"
al ganador, conservando el mecanismo (párpado vs estómago) y la autoridad/alta-intención.
Capas de culpa, Emotional Valence, Identidad Reclamada y Villain son las palancas.
Quality gates: OH SHIT · Thumb-stop · Deeper/Different · Especificidad · No auto-admisión ·
Enemigo · Story compulsion (Zeigarnik) · Embarrass-winner · Sin gore.

MÉTODO DE PROMPTS DE VIDEO (Nano Banana → Veo 3.1)
Sigue SIEMPRE la "Guía Maestra Veo 3.1" del Knowledge. Reglas duras:
- 1 prompt Nano Banana = 1 keyframe (imagen). 1 prompt Veo = 1 clip (≤8s, image-to-video).
- Fórmula 5 partes con la CINEMATOGRAFÍA al inicio; UN solo movimiento de cámara por clip.
- Cada prompt va COMPLETO en un solo bloque (Style Block + Negative ya incrustados), listo
  para pegar; nada de secciones separadas.
- Consistencia de personaje con un ANCHOR (retrato generado primero) reutilizado como imagen
  de referencia en cada keyframe. REGLA DURA: Veo no anima con dos referencias → ningún clip
  puede usar dos anchors a la vez; los momentos "juntos" se resuelven con POV o por montaje.
- El producto VisionPure NO se describe: se adjunta como imagen de referencia (el prompt lo
  llama "the bottle from the attached reference image"). Indicar en qué shots se adjunta.
- Audio muteado (negative: no voiceover, no music). Texto en pantalla y voz en off = en EDICIÓN,
  nunca en el prompt (Veo deforma el texto).
- Formato 9:16. Prompts de generación en INGLÉS; textos/VO en ESPAÑOL.
- Un ad ≈ 8 shots; si se pide ~90s, expandir a ~16 clips (como el ganador SO6 = 89,9s).

FORMA DE TRABAJAR
Antes de generar un brief o prompts, apóyate en los archivos del Knowledge (análisis + guías).
Entrega accionable, sin relleno. Marca siempre los chequeos de compliance.
```

---

## PASO 3 — Sube estos archivos a "Project Knowledge"

### 🅰️ BRIEFS (lo principal #1)
| Archivo | Para qué |
|---|---|
| `briefs/VisionPure_Eye_Breakthrough_Conceptos.doc` | Los 7 conceptos C1-C7 (base de iteración) |
| `briefs/VisionPure_Eye_Briefs-Iteracion.doc` | Briefs de iteración del ganador (estructura del curso) |
| `documentos/curso/creative_strategy_course_COMPLETO (1).md` | El método/estructura de brief |
| `documentos/voz-de-cliente-VisionPure.md` | Voz de cliente / lenguaje del avatar |
| `documentos/prompts-creacion/villain_marketing_implementation (1).txt` | Framework de villano |
| `documentos/prompts-research/Extraccion identidad.txt` | Framework de identidad reclamada |

### 🅱️ PROMPTS DE VIDEO (lo principal #2)
| Archivo | Para qué |
|---|---|
| `documentos/Guia_Veo31_Prompting.md` | **EL estándar** de prompting Veo (reglas de oro, 5 partes, consistencia) |
| `prompts-animacion/C3_independencia_prompts.md` | Plantilla de referencia (formato listo-para-pegar) |
| `prompts-animacion/C4_testigo_prompts.md` | Ejemplo con 2 anchors + regla 1-ref-por-clip (POV) |
| `prompts-animacion/C5_industria_prompts.md` | Ejemplo exposé/autoridad |
| `prompts-animacion/C6_plastico_prompts.md` | Ejemplo con CGI + compliance quirúrgico |
| **Imagen hero del producto VisionPure** (PNG limpio) | Referencia visual del producto para adjuntar en Veo |

### 🆑 CONTEXTO / DATOS (para fundamentar decisiones)
| Archivo | Para qué |
|---|---|
| `Eye_CBO_Documento_Maestro.md` | Correlación métricas × mensaje × audiencia × compliance |
| `Analisis_Eye_CBO_7dias.md` | Métricas 7d (ad sets, edad, sexo, ubicación, plataforma) |
| `analisis-videos/eye-angulos-faltantes--analisis.md` | Qué mensajes/ángulos funcionan (video) |
| `analisis-videos/fotos-imagenes-eye--analisis.md` | Qué funciona en imagen (oferta vs educacional) |
| `analisis-videos/so6-ad37-visionpure--analisis.md` | Deconstrucción del video ganador |
| `analisis-videos/VisionPure_Eye_Top10-Bottom10_Analisis.doc` | Top/Bottom de creativos |
| `README.md` | Mapa del proyecto y convenciones de nombres |

> **No subir:** el token de Meta, ni `adv_*` (advertorial — fuera del funnel actual), ni carpetas de frames/_sheets (pesadas, son intermedios).

---

## PASO 4 — Cómo pedirle cosas en la web (ejemplos)
- *"Genérame los prompts del C7 en el mismo formato listo-para-pegar de C3-C6."*
- *"Arma un brief nuevo sobre el villano cirugía para público 65+, estructura del curso."*
- *"Adapta el C4 a variante mamá-hija."*

---

## Notas
- Claude web **no** ejecuta MCP de Meta ni baja videos por token como acá; para datos nuevos de
  la cuenta, pásalos tú o vuelve a esta sesión de Claude Code.
- Si actualizas un análisis, vuelve a subir el archivo al Knowledge (no se sincroniza solo).
- Límite de Knowledge: si no caben todos, prioriza 🅰️ y 🅱️ (briefs + guía de prompts + 1-2 plantillas).
```
