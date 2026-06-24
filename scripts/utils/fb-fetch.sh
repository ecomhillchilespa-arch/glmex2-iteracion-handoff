#!/usr/bin/env bash
# Descarga videos de un ad account de Meta por coincidencia de nombre de archivo.
# Uso:  bash scripts/fb-fetch.sh <token_file> <act_id> <out_dir> "patron1" "patron2" ...
# Si no se pasan patrones, solo construye el manifiesto en /tmp/adv.tsv y lista titulos.
set -u

TOKFILE="${1:?token file}"
ACT="${2:?act id sin act_}"
OUTDIR="${3:?carpeta destino}"
shift 3
TOK=$(cat "$TOKFILE")
MAN=/tmp/adv.tsv
: > "$MAN"

URL="https://graph.facebook.com/v23.0/act_${ACT}/advideos?fields=id,title,source&limit=200&access_token=${TOK}"
page=0
while [ -n "$URL" ] && [ "$page" -lt 12 ]; do
  RESP=$(curl -s -m 45 "$URL")
  printf '%s' "$RESP" \
    | sed 's/},{/}\n{/g' \
    | sed -nE 's/.*"id":"([0-9]+)".*"title":"([^"]*)".*"source":"([^"]+)".*/\1\t\2\t\3/p' \
    | sed 's@\\/@/@g' >> "$MAN"
  URL=$(printf '%s' "$RESP" | grep -oE '"next":"[^"]+"' | head -1 | sed 's/"next":"//; s/"$//; s@\\/@/@g; s@\\u0025@%@g')
  page=$((page+1))
done

total=$(wc -l < "$MAN" | tr -d ' ')
echo "Manifiesto: $total videos con source ($page paginas)"

if [ "$#" -eq 0 ]; then
  echo "--- titulos unicos ---"
  cut -f2 "$MAN" | sort -u
  exit 0
fi

mkdir -p "$OUTDIR"
for pat in "$@"; do
  line=$(grep -iE "	${pat}" "$MAN" | head -1)
  [ -z "$line" ] && line=$(grep -iF "$pat" "$MAN" | head -1)
  if [ -z "$line" ]; then echo "NO encontrado: $pat"; continue; fi
  title=$(printf '%s' "$line" | cut -f2)
  src=$(printf '%s' "$line" | cut -f3)
  safe=$(printf '%s' "$title" | sed 's/[^A-Za-z0-9 ._-]/_/g')
  out="$OUTDIR/$safe"
  curl -s -m 240 -o "$out" "$src"
  sz=$(wc -c < "$out" | tr -d ' ')
  echo "OK  $title  ->  $out  (${sz} bytes)"
done
