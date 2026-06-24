# Handoff — Sistema de Iteración de Ads + Tablero GL-MEX2

Paquete **portátil** para que **otra sesión de Claude Code** (u otra persona) retome este proyecto
sin empezar de cero. Reúne el método, los procesos, los scripts y ejemplos reales de output.

## Cómo usarlo (sesión nueva de Claude Code)
1. Copia esta carpeta a la máquina/proyecto nuevo (o haz `git clone` si la subiste a GitHub).
2. Abre Claude Code con esta carpeta como working directory. Lee **`CLAUDE.md`** (bootstrap) y luego **`START-HERE.md`**.
3. Configura secretos y conectores siguiendo **`SECURITY.md`** + **`.env.example`**.
4. Siembra la memoria desde `memory/` (instrucciones en `START-HERE.md`).

## Estructura
```
handoff/
├── CLAUDE.md            # ⭐ bootstrap: quién eres, el sistema, productos, reglas
├── START-HERE.md        # orden de lectura + cómo sembrar memoria + setup
├── SECURITY.md          # manejo de secretos (qué rotar, qué nunca subir)
├── .env.example         # nombres de las llaves (sin valores)
├── .gitignore
├── memory/              # las memorias del proyecto (estado real, IDs, lecciones)
├── processes/           # ⭐ los playbooks paso a paso (lo que se replica)
│   ├── 01-analisis-videos.md
│   ├── 02-briefs-breakthrough.md
│   ├── 03-prompts-video-veo.md
│   ├── 04-tablero-glmex2.md
│   ├── 05-clarity.md
│   └── 06-cruce-niveles-conciencia.md
├── artifacts/IDS.md     # todos los IDs de la nube (Supabase, n8n, Drive, Meta, Shopify, Clarity)
├── scripts/             # tooling (sheets_glmex2, clarity, utils)
├── reference/           # frameworks de copy, guías Veo, voz de cliente, prompts de animación
└── examples/            # outputs reales: análisis de videos y briefs (referencia de calidad)
```

## Qué SÍ y qué NO se transfiere
- ✅ **El método y los procesos** (lo valioso), los scripts, ejemplos de output, los IDs de la nube.
- ❌ **No** se transfiere el acceso a las cuentas: la sesión nueva necesita sus propios MCP
  connectors y tokens (los del usuario). Sin eso puede leer/escribir documentos pero no tocar Meta/Shopify/etc.
- ❌ **No** se incluye media pesada (videos/frames/audios) ni secretos.

## Estado del proyecto al momento del handoff (2026-06-23)
Ver `memory/` para el detalle vivo. Resumen: tablero diario GL-MEX2 funcionando (Supabase+n8n+Sheets),
Clarity recién conectado (process 05), cruce por nivel de conciencia generado (process 06),
briefs Breakthrough hechos para VisionPure/PetClean/QuietLab.
