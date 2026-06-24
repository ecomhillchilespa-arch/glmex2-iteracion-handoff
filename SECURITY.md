# SECURITY — manejo de secretos

**Regla de oro:** este paquete NO contiene ninguna llave. Antes de subirlo a GitHub o compartirlo,
verifica que sigue siendo así.

## Secretos que el sistema usa (van en `.env`, nunca en el repo)
| Secreto | Para qué | Dónde se usa |
|---|---|---|
| `CLARITY_TOKEN` (JWT) | Data Export API de Microsoft Clarity | `scripts/clarity/clarity_token.txt` |
| `META_TOKEN` | bajar videos del ad account (`fb-fetch.sh`) | archivo que pasas como arg al script |
| `SUPABASE_*` (URL + service/anon key) | tablero | connector MCP de Supabase (lo conecta el usuario) |
| Google / n8n / Shopify / Meta Ads | MCP connectors | los conecta el usuario en su cliente |

## Cómo configurar en una sesión nueva
1. Copia `.env.example` → `.env` y llena los valores (el `.env` está en `.gitignore`).
2. Para Clarity: copia `scripts/clarity/clarity_token.txt.example` → `clarity_token.txt` y pega tu JWT.
   - El token se genera en el dashboard de Clarity → Settings → Data Export (scope `Data.Export`).
3. Los MCP connectors (Meta Ads, Shopify, Supabase, n8n, Google Drive) los activa el usuario en su
   cliente de Claude; este paquete solo documenta los IDs de recursos (`artifacts/IDS.md`), no las creds.

## Si algún token se filtró en un commit
- **Clarity:** regenera el token en el dashboard (invalida el anterior).
- **Meta:** rota el token en Business Settings / Graph API.
- Reescribe la historia de git o, más simple, crea el repo limpio desde cero.

## Antes de `git init` / push — checklist
- [ ] No existe `clarity_token.txt` (solo el `.example`).
- [ ] No hay `.env` con valores reales.
- [ ] `grep -ri "eyJ" .` no devuelve JWTs; `grep -ri "access_token" .` no devuelve llaves.
- [ ] No se coló media ni `raw/`.
