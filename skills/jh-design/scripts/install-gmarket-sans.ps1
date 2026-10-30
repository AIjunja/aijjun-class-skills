param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectRoot
)

$ErrorActionPreference = "Stop"

$projectPath = (Resolve-Path -LiteralPath $ProjectRoot).Path
$skillRoot = Split-Path -Parent $PSScriptRoot
$sourceRoot = Join-Path $skillRoot "assets\fonts"
$targetRoot = Join-Path $projectPath "public\fonts"
$fontNames = @(
    "GmarketSans-Light.ttf",
    "GmarketSans-Medium.ttf",
    "GmarketSans-Bold.ttf",
    "OFL.txt"
)

if (-not (Test-Path -LiteralPath $sourceRoot)) {
    throw "Bundled font directory was not found: $sourceRoot"
}

New-Item -ItemType Directory -Path $targetRoot -Force | Out-Null

foreach ($fontName in $fontNames) {
    $source = Join-Path $sourceRoot $fontName
    $target = Join-Path $targetRoot $fontName

    if (-not (Test-Path -LiteralPath $source)) {
        throw "Bundled font file was not found: $source"
    }

    Copy-Item -LiteralPath $source -Destination $target -Force
    Write-Host "Installed: $target" -ForegroundColor Green
}

Write-Host "Add the @font-face rules from references\gmarket-sans-css.md to the global stylesheet"
