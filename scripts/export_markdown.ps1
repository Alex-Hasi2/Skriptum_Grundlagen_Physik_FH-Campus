param(
    [Parameter(Mandatory = $true)]
    [string]$SourcePath,

    [ValidateSet('docx', 'html', 'pdf')]
    [string[]]$Formats = @('docx'),

    [string]$OutputDir
)

$ErrorActionPreference = 'Stop'

function Resolve-AbsolutePath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$PathValue
    )

    return (Resolve-Path -LiteralPath $PathValue).Path
}

if (-not (Get-Command pandoc -ErrorAction SilentlyContinue)) {
    throw "pandoc is not installed or not available on PATH. Install pandoc first: https://pandoc.org/installing.html"
}

$resolvedSourcePath = Resolve-AbsolutePath -PathValue $SourcePath

if ([System.IO.Path]::GetExtension($resolvedSourcePath) -ne '.md') {
    throw "Source file must be a Markdown file (.md)."
}

if (-not $OutputDir) {
    $OutputDir = Split-Path -Parent $resolvedSourcePath
}

if (-not (Test-Path -LiteralPath $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
}

$resolvedOutputDir = Resolve-AbsolutePath -PathValue $OutputDir
$baseName = [System.IO.Path]::GetFileNameWithoutExtension($resolvedSourcePath)

foreach ($format in $Formats) {
    $outputPath = Join-Path $resolvedOutputDir "$baseName.$format"

    Write-Host "Exporting '$resolvedSourcePath' to '$outputPath'..."
    pandoc $resolvedSourcePath -o $outputPath
}

Write-Host 'Export complete.'