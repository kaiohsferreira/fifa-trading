$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

if (-not (Test-Path ".env")) {
  Copy-Item ".env.example" ".env"
  Write-Host "Arquivo .env criado a partir do .env.example." -ForegroundColor Yellow
}

if (-not (Get-Command codex -ErrorAction SilentlyContinue)) {
  throw "Codex CLI nao encontrado no PATH."
}

if (-not (Test-Path "node_modules")) {
  npm install
}

$port = 3001
$url = "http://localhost:$port"

Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$root'; `$env:PORT=$port; npm run start"
Start-Sleep -Seconds 3
Start-Process $url

Write-Host "ROVIS Chat iniciado em $url" -ForegroundColor Green
