param(
  [Parameter(Mandatory=$true)][string]$Md,
  [Parameter(Mandatory=$true)][string]$Docx
)

$ErrorActionPreference = "Stop"
$lines = Get-Content -LiteralPath $Md -Encoding UTF8

function Convert-Inline([string]$t) {
  $t = $t -replace '&','&amp;' -replace '<','&lt;' -replace '>','&gt;'
  # inline code
  $t = [regex]::Replace($t, '`([^`]+)`', '<code>$1</code>')
  # bold
  $t = [regex]::Replace($t, '\*\*([^*]+)\*\*', '<strong>$1</strong>')
  # italic (single * not adjacent to another *)
  $t = [regex]::Replace($t, '(?<!\*)\*([^*]+)\*(?!\*)', '<em>$1</em>')
  return $t
}

$sb = New-Object System.Text.StringBuilder
[void]$sb.Append('<html><head><meta charset="utf-8"><style>')
[void]$sb.Append('body{font-family:Calibri,Arial,sans-serif;font-size:11pt;line-height:1.35;}')
[void]$sb.Append('h1{font-size:20pt;color:#1a1a1a;} h2{font-size:15pt;color:#2b4c7e;border-bottom:1px solid #ccc;padding-bottom:3px;} h3{font-size:12.5pt;color:#34495e;}')
[void]$sb.Append('table{border-collapse:collapse;width:100%;} td,th{border:1px solid #999;padding:5px 7px;font-size:10.5pt;vertical-align:top;} th{background:#2b4c7e;color:#fff;text-align:left;}')
[void]$sb.Append('code{background:#f2f2f2;font-family:Consolas,monospace;font-size:9.5pt;padding:0 2px;} blockquote{border-left:3px solid #2b4c7e;margin:6px 0;padding:4px 12px;background:#f7f9fc;color:#444;}')
[void]$sb.Append('ul,ol{margin:4px 0 8px 0;} li{margin:2px 0;}')
[void]$sb.Append('</style></head><body>')

$listStack = @()   # each entry: tag (ul/ol) with indent level
$inTable = $false
$tableRows = @()

function Close-Lists([int]$toLevel) {
  while ($listStack.Count -gt $toLevel) {
    $tag = $listStack[-1]
    [void]$sb.Append("</$tag>")
    $script:listStack = $listStack[0..($listStack.Count-2)]
    if ($listStack.Count -eq 0) { $script:listStack = @() }
  }
}

function Flush-Table {
  if (-not $script:inTable) { return }
  [void]$sb.Append('<table>')
  for ($i=0; $i -lt $script:tableRows.Count; $i++) {
    if ($i -eq 1) { continue } # separator row
    $cells = $script:tableRows[$i].Trim().Trim('|').Split('|')
    $cellTag = if ($i -eq 0) { 'th' } else { 'td' }
    [void]$sb.Append('<tr>')
    foreach ($c in $cells) { [void]$sb.Append("<$cellTag>" + (Convert-Inline $c.Trim()) + "</$cellTag>") }
    [void]$sb.Append('</tr>')
  }
  [void]$sb.Append('</table>')
  $script:inTable = $false
  $script:tableRows = @()
}

foreach ($raw in $lines) {
  $line = $raw.TrimEnd()

  # table handling
  if ($line -match '^\s*\|') {
    if (-not $inTable) { Close-Lists 0; $inTable = $true; $tableRows = @() }
    $tableRows += $line
    continue
  } elseif ($inTable) {
    Flush-Table
  }

  if ($line.Trim() -eq '') { Close-Lists 0; continue }

  if ($line -match '^---+\s*$') { Close-Lists 0; [void]$sb.Append('<hr/>'); continue }
  if ($line -match '^#\s+(.*)') { Close-Lists 0; [void]$sb.Append('<h1>' + (Convert-Inline $matches[1]) + '</h1>'); continue }
  if ($line -match '^##\s+(.*)') { Close-Lists 0; [void]$sb.Append('<h2>' + (Convert-Inline $matches[1]) + '</h2>'); continue }
  if ($line -match '^###\s+(.*)') { Close-Lists 0; [void]$sb.Append('<h3>' + (Convert-Inline $matches[1]) + '</h3>'); continue }
  if ($line -match '^>\s?(.*)') { Close-Lists 0; [void]$sb.Append('<blockquote>' + (Convert-Inline $matches[1]) + '</blockquote>'); continue }

  # lists (with one level of nesting based on indent)
  if ($line -match '^(\s*)([-*])\s+(.*)') {
    $indent = $matches[1].Length
    $level = [math]::Floor($indent/2) + 1
    while ($listStack.Count -lt $level) { [void]$sb.Append('<ul>'); $listStack += 'ul' }
    while ($listStack.Count -gt $level) { Close-Lists ($listStack.Count-1) }
    [void]$sb.Append('<li>' + (Convert-Inline $matches[3]) + '</li>')
    continue
  }
  if ($line -match '^(\s*)(\d+)\.\s+(.*)') {
    $indent = $matches[1].Length
    $level = [math]::Floor($indent/2) + 1
    while ($listStack.Count -lt $level) { [void]$sb.Append('<ol>'); $listStack += 'ol' }
    while ($listStack.Count -gt $level) { Close-Lists ($listStack.Count-1) }
    [void]$sb.Append('<li>' + (Convert-Inline $matches[3]) + '</li>')
    continue
  }

  Close-Lists 0
  [void]$sb.Append('<p>' + (Convert-Inline $line) + '</p>')
}
Flush-Table
Close-Lists 0
[void]$sb.Append('</body></html>')

$html = $sb.ToString()
$htmlPath = [System.IO.Path]::ChangeExtension($Docx, '.tmp.html')
$utf8Bom = New-Object System.Text.UTF8Encoding($true)
[System.IO.File]::WriteAllText($htmlPath, $html, $utf8Bom)

$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
  $doc = $word.Documents.Open($htmlPath)
  $doc.SaveAs([ref]$Docx, [ref]16)  # 16 = wdFormatDocumentDefault (.docx)
  $doc.Close()
} finally {
  $word.Quit()
  [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
  Remove-Item -LiteralPath $htmlPath -ErrorAction SilentlyContinue
}
Write-Output "DONE: $Docx"
