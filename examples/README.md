# Proyecto: Iteración de Conceptos de Ads

Sistema para analizar videos ganadores de Meta y generar **briefs de iteración de conceptos**.

## Flujo de trabajo

1. **Video** → se deja el ad ganador en `videos/`
2. **Análisis** → se procesa con ffmpeg (tomas + subtítulos quemados → guion) y se guarda en `analisis-videos/`
3. **Meta** → vía MCP se identifica la campaña/métricas del video (cuenta + campaña la indica el usuario)
4. **Brief** → se genera el brief de iteración en `briefs/`, apoyado en los frameworks de `documentos/`

## Estructura de carpetas

```
Iteracion/
├── videos/                         # Videos crudos a analizar (input)
├── analisis-videos/                # Guiones + desgloses de tomas (output del análisis)
├── briefs/                         # Briefs de iteración generados (output final)
├── scripts/                        # Utilidades (fb-fetch.sh: baja videos de Meta vía token)
└── documentos/                     # Material de referencia (frameworks)
    ├── prompts-research/           # Prompts de investigación de mercado/avatar
    ├── prompts-creacion/           # Prompts para crear/iterar ads
    ├── curso/                      # Curso Creative Strategy + clase en video
    └── imagenes-referencia/        # Slides: niveles de conciencia, valencia, etc.
```

## Convención de nombres

Para mantener el orden, cada video ganador genera:

- `analisis-videos/<slug>--analisis.md`  → guion + desglose de tomas (markdown de trabajo)
- `briefs/<Producto>_<Tema>_Briefs-Iteracion.doc` → conceptos de iteración en **documento Word**, estructurado según el Creative Strategy Course (Persona → Funnel/Awareness → Tone → Key Messages → 3 Hooks → Script Flow → CTA → QC 14 preguntas).

Ejemplo para el primer video:
- `analisis-videos/so6-ad37-visionpure--analisis.md`
- `briefs/VisionPure_Eye_Briefs-Iteracion.doc`

## Estado actual

| Video | Producto | Cuenta / Campaña | ROAS | Análisis | Brief |
|---|---|---|---|---|---|
| SO6 AD 37 | VisionPure (spray luteína) | GL-MEX2 / Eye CBO | 3,07 | ✅ hecho | ✅ 10 conceptos |

**Análisis Top 10 / Bottom 10:** `analisis-videos/VisionPure_Eye_Top10-Bottom10_Analisis.doc` — 20 ads → 11 creativos, mensaje + hipótesis (por qué funciona/no). 10 videos descargados en `videos/`.

**Conceptos Breakthrough:** `briefs/VisionPure_Eye_Breakthrough_Conceptos.doc` — 7 conceptos con BREAKTHROUGH como base (deconstrucción del ganador PD3 + territorio sin explotar + quality gates), estructura del curso, razones en todo, sin advertorial.
