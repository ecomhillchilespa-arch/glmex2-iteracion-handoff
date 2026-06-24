param(
  [Parameter(Mandatory=$true)][string]$Md,
  [Parameter(Mandatory=$true)][string]$Docx
)
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$lines = Get-Content -LiteralPath $Md -Encoding UTF8

function XmlEsc([string]$s) {
  return ($s -replace '&','&amp;' -replace '<','&lt;' -replace '>','&gt;' -replace '"','&quot;')
}

# Inline markdown -> array of run XML
function Get-Runs([string]$t) {
  $out = New-Object System.Text.StringBuilder
  $rx = [regex]'(`[^`]+`)|(\*\*[^*]+\*\*)|(\*[^*]+\*)'
  $pos = 0
  foreach ($m in $rx.Matches($t)) {
    if ($m.Index -gt $pos) {
      $plain = $t.Substring($pos, $m.Index - $pos)
      [void]$out.Append('<w:r><w:t xml:space="preserve">' + (XmlEsc $plain) + '</w:t></w:r>')
    }
    $tok = $m.Value
    if ($tok.StartsWith('`')) {
      $inner = $tok.Substring(1, $tok.Length-2)
      [void]$out.Append('<w:r><w:rPr><w:rStyle w:val="CodeChar"/><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/></w:rPr><w:t xml:space="preserve">' + (XmlEsc $inner) + '</w:t></w:r>')
    } elseif ($tok.StartsWith('**')) {
      $inner = $tok.Substring(2, $tok.Length-4)
      [void]$out.Append('<w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">' + (XmlEsc $inner) + '</w:t></w:r>')
    } else {
      $inner = $tok.Substring(1, $tok.Length-2)
      [void]$out.Append('<w:r><w:rPr><w:i/></w:rPr><w:t xml:space="preserve">' + (XmlEsc $inner) + '</w:t></w:r>')
    }
    $pos = $m.Index + $m.Length
  }
  if ($pos -lt $t.Length) {
    [void]$out.Append('<w:r><w:t xml:space="preserve">' + (XmlEsc $t.Substring($pos)) + '</w:t></w:r>')
  }
  if ($out.Length -eq 0) { [void]$out.Append('<w:r><w:t xml:space="preserve"></w:t></w:r>') }
  return $out.ToString()
}

$body = New-Object System.Text.StringBuilder
$inTable = $false
$tableRows = @()
$orderedCounters = @{}   # level -> counter

function Para([string]$style, [string]$runs, [string]$extraPpr="") {
  $ppr = ""
  if ($style -or $extraPpr) {
    $ppr = "<w:pPr>"
    if ($style) { $ppr += "<w:pStyle w:val=`"$style`"/>" }
    $ppr += $extraPpr + "</w:pPr>"
  }
  [void]$script:body.Append("<w:p>$ppr$runs</w:p>")
}

function Flush-Table {
  if (-not $script:inTable) { return }
  $rows = $script:tableRows
  $tbl = New-Object System.Text.StringBuilder
  [void]$tbl.Append('<w:tbl><w:tblPr><w:tblW w:w="5000" w:type="pct"/><w:tblBorders><w:top w:val="single" w:sz="4" w:space="0" w:color="999999"/><w:left w:val="single" w:sz="4" w:space="0" w:color="999999"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="999999"/><w:right w:val="single" w:sz="4" w:space="0" w:color="999999"/><w:insideH w:val="single" w:sz="4" w:space="0" w:color="999999"/><w:insideV w:val="single" w:sz="4" w:space="0" w:color="999999"/></w:tblBorders></w:tblPr>')
  for ($i=0; $i -lt $rows.Count; $i++) {
    if ($i -eq 1) { continue }
    $cells = $rows[$i].Trim().Trim('|').Split('|')
    [void]$tbl.Append('<w:tr>')
    foreach ($c in $cells) {
      $txt = $c.Trim()
      if ($i -eq 0) {
        $runs = '<w:r><w:rPr><w:b/><w:color w:val="FFFFFF"/></w:rPr><w:t xml:space="preserve">' + (XmlEsc $txt) + '</w:t></w:r>'
        [void]$tbl.Append('<w:tc><w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="2B4C7E"/></w:tcPr><w:p>' + $runs + '</w:p></w:tc>')
      } else {
        $runs = Get-Runs $txt
        [void]$tbl.Append('<w:tc><w:tcPr></w:tcPr><w:p>' + $runs + '</w:p></w:tc>')
      }
    }
    [void]$tbl.Append('</w:tr>')
  }
  [void]$tbl.Append('</w:tbl><w:p/>')
  [void]$script:body.Append($tbl.ToString())
  $script:inTable = $false
  $script:tableRows = @()
}

foreach ($raw in $lines) {
  $line = $raw.TrimEnd()

  if ($line -match '^\s*\|') {
    if (-not $inTable) { $inTable = $true; $tableRows = @() }
    $tableRows += $line
    continue
  } elseif ($inTable) { Flush-Table }

  if ($line.Trim() -eq '') { $orderedCounters = @{}; continue }

  if ($line -match '^---+\s*$') {
    Para "" '<w:r><w:t xml:space="preserve"></w:t></w:r>' '<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="BBBBBB"/></w:pBdr>'
    continue
  }
  if ($line -match '^#\s+(.*)')   { Para "Heading1" (Get-Runs $matches[1]); continue }
  if ($line -match '^##\s+(.*)')  { Para "Heading2" (Get-Runs $matches[1]); continue }
  if ($line -match '^###\s+(.*)') { Para "Heading3" (Get-Runs $matches[1]); continue }
  if ($line -match '^>\s?(.*)')   { Para "Quote"    (Get-Runs $matches[1]); continue }

  if ($line -match '^(\s*)([-*])\s+(.*)') {
    $indent = $matches[1].Length
    $level = [math]::Floor($indent/2)
    $ind = 360 + $level*360
    $runs = '<w:r><w:t xml:space="preserve">&#8226;  </w:t></w:r>' + (Get-Runs $matches[3])
    Para "" $runs "<w:ind w:left=`"$ind`" w:hanging=`"360`"/>"
    continue
  }
  if ($line -match '^(\s*)(\d+)\.\s+(.*)') {
    $indent = $matches[1].Length
    $level = [math]::Floor($indent/2)
    if (-not $orderedCounters.ContainsKey($level)) { $orderedCounters[$level] = 0 }
    $orderedCounters[$level]++
    $num = $orderedCounters[$level]
    $ind = 360 + $level*360
    $runs = '<w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">' + $num + '.  </w:t></w:r>' + (Get-Runs $matches[3])
    Para "" $runs "<w:ind w:left=`"$ind`" w:hanging=`"360`"/>"
    continue
  }

  $orderedCounters = @{}
  Para "" (Get-Runs $line)
}
Flush-Table

$documentXml = @"
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>$($body.ToString())<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="709" w:footer="709" w:gutter="0"/></w:sectPr></w:body></w:document>
"@

$stylesXml = @"
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="22"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:before="240" w:after="120"/></w:pPr><w:rPr><w:b/><w:color w:val="1A1A1A"/><w:sz w:val="40"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:before="240" w:after="80"/><w:pBdr><w:bottom w:val="single" w:sz="4" w:space="2" w:color="CCCCCC"/></w:pBdr></w:pPr><w:rPr><w:b/><w:color w:val="2B4C7E"/><w:sz w:val="30"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:before="160" w:after="60"/></w:pPr><w:rPr><w:b/><w:color w:val="34495E"/><w:sz w:val="25"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Quote"><w:name w:val="Quote"/><w:basedOn w:val="Normal"/><w:pPr><w:pBdr><w:left w:val="single" w:sz="18" w:space="8" w:color="2B4C7E"/></w:pBdr><w:shd w:val="clear" w:color="auto" w:fill="F7F9FC"/><w:ind w:left="200"/></w:pPr><w:rPr><w:color w:val="444444"/><w:i/></w:rPr></w:style>
<w:style w:type="character" w:styleId="CodeChar"><w:name w:val="Code Char"/><w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/><w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/><w:sz w:val="19"/></w:rPr></w:style>
</w:styles>
"@

$contentTypes = @"
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>
"@

$rels = @"
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>
"@

$docRels = @"
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>
"@

if (Test-Path -LiteralPath $Docx) { Remove-Item -LiteralPath $Docx -Force }
$enc = New-Object System.Text.UTF8Encoding($false)
$fs = [System.IO.File]::Open($Docx, [System.IO.FileMode]::CreateNew)
$zip = New-Object System.IO.Compression.ZipArchive($fs, [System.IO.Compression.ZipArchiveMode]::Create)
function Add-Entry($path, $content) {
  $e = $zip.CreateEntry($path, [System.IO.Compression.CompressionLevel]::Optimal)
  $s = $e.Open()
  $bytes = $enc.GetBytes($content)
  $s.Write($bytes, 0, $bytes.Length)
  $s.Close()
}
Add-Entry '[Content_Types].xml' $contentTypes
Add-Entry '_rels/.rels' $rels
Add-Entry 'word/document.xml' $documentXml
Add-Entry 'word/styles.xml' $stylesXml
Add-Entry 'word/_rels/document.xml.rels' $docRels
$zip.Dispose()
$fs.Close()
Write-Output ("DONE: {0} ({1:N0} bytes)" -f $Docx, (Get-Item $Docx).Length)
