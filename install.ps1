param(
    [string]$Skill = 'all',
    [string]$DestinationRoot = (Join-Path $HOME '.claude\skills')
)

$ErrorActionPreference = 'Stop'
$skillsSource = Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) 'skills'
$names = if ($Skill -eq 'all') {
    Get-ChildItem -Path $skillsSource -Directory | ForEach-Object { $_.Name }
} else {
    @($Skill)
}

New-Item -ItemType Directory -Path $DestinationRoot -Force | Out-Null

foreach ($name in $names) {
    $source = Join-Path $skillsSource $name
    if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md'))) {
        throw "Skill source not found: $source"
    }
    $destination = Join-Path $DestinationRoot $name
    New-Item -ItemType Directory -Path $destination -Force | Out-Null
    Copy-Item -Path (Join-Path $source '*') -Destination $destination -Recurse -Force
    Write-Host "Installed: $name -> $destination" -ForegroundColor Green
}

Write-Host 'Restart Claude Code to refresh the skill list.' -ForegroundColor Cyan
