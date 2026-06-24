# START HERE — Orden de arranque para la sesión nueva

## Paso 1 — Lee en este orden
1. `CLAUDE.md` — quién eres, el sistema, productos, reglas. (obligatorio)
2. `memory/MEMORY.md` — índice del estado real del proyecto.
3. El/los proceso(s) de `processes/` según lo que pida el usuario.
4. `artifacts/IDS.md` — solo cuando vayas a tocar la nube.

## Paso 2 — Siembra tu memoria
Este proyecto usa el sistema de memoria de archivos de Claude Code. Las memorias están en `memory/`.
En la sesión nueva:
- Si trabajas en el **mismo** entorno de Claude Code del usuario, las memorias del proyecto se cargan
  solas desde `~/.claude/projects/<proyecto>/memory/`. Copia los `.md` de `memory/` ahí y agrega cada
  línea al `MEMORY.md` índice (formato `- [Título](archivo.md) — gancho`).
- Si es otro entorno, **lee `memory/*.md` al inicio** y trátalas como contexto base. Lo más importante:
  - `proyecto-iteracion-briefs.md` — objetivo y flujo general.
  - `mensajes-ganadores-glmex2.md` — qué ángulos/ads ganan por producto y nivel.
  - `indice-artefactos-glmex2.md` — todos los IDs de la nube.
  - `tablero-glmex2-diario.md` — rutina diaria.
  - `formato-brief-breakthrough.md` + `registrar-avances-briefs.md` — cómo entregar y registrar.

## Paso 3 — Conecta los servicios (solo si la tarea los necesita)
Ver `SECURITY.md` y `.env.example`. Resumen de connectors MCP que el usuario debe tener activos:
- **Meta Ads** (leer métricas/entidades), **Shopify** (ventas/sesiones/ATC), **Supabase** (tablero),
  **n8n** (sync), **Google Drive** (crear Sheets/Docs). 
- **Clarity** NO es un MCP: es un script local (`scripts/clarity/`) que pega a la Data Export API con
  un token JWT. Pon el token en `scripts/clarity/clarity_token.txt` (ver `.example`).

## Paso 4 — Trabaja
Identifica el frente:
- ¿Video nuevo / brief / prompts? → `processes/01`, `02`, `03` + `reference/`.
- ¿Tablero diario / análisis de performance? → `processes/04`, `05`, `06`.

**Regla de cierre (de la memoria `registrar-avances-briefs`):** al terminar cada brief/video o corrida
del tablero, anota el avance en memoria (qué video + qué conceptos / qué snapshot).

## Mapa rápido: tarea → archivos
| El usuario pide… | Lee | Usa |
|---|---|---|
| "analiza este video" | `processes/01` | ffmpeg, `examples/analisis-videos/*` como molde |
| "hazme un brief / conceptos" | `processes/02` | `reference/frameworks/BREAKTHROUGH…`, curso, `examples/briefs/*` |
| "prompts de video para Veo" | `processes/03` | `reference/guias/Guia_Veo31…`, `reference/prompts-animacion/*` |
| "corre el tablero / métricas de hoy" | `processes/04` | `scripts/sheets_glmex2/*`, Supabase, n8n |
| "datos de Clarity" | `processes/05` | `scripts/clarity/*` |
| "cruce por nivel de conciencia" | `processes/06` | `scripts/clarity/build_cruce.py` |
