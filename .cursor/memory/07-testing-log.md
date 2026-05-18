# Testing log

(vazio)


## 2026-04-30 - Build WriteOff Save VehicleIds
Data: 2026-04-30
Agente: AI_TESTING
Comando: dotnet build ABPAC-BackEnd/AlavTech.API/AlavTech.API.csproj -v minimal
Resultado: Build succeeded; 0 errors; 2 warnings NU1902 sobre Microsoft.AspNetCore.Authentication.JwtBearer 5.0.5.

## 2026-04-30 - AI-TESTING WriteOff Save VehicleIds
Data: 2026-04-30
Agente: AI_TESTING
Comando: powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Run-AIEngine.ps1 -Mode api -SkipBrowserInstall
Resultado: falhou no script com CommandNotFoundException para -SkipInstall; targets resolvidos para http://localhost:33422 e Swagger /swagger/v1/swagger.json; build dotnet permanece OK.

## 2026-04-30 - Build WriteOff ReasonId
Data: 2026-04-30
Agente: AI_TESTING
Comando: dotnet build ABPAC-BackEnd/AlavTech.API/AlavTech.API.csproj -v minimal
Resultado: Build succeeded; 0 errors; 889 warnings existentes.
AI-TESTING: Run-AIEngine.ps1 -Mode api -SkipBrowserInstall falhou no runner com CommandNotFoundException para -SkipInstall.

## 2026-04-30 - Build CRUD WriteOffReason
Data: 2026-04-30
Agente: ROVIS_BE
dotnet build ABPAC-BackEnd/AlavTech.API/AlavTech.API.csproj -v minimal executado com sucesso: 0 erros, 2 warnings NU1902 existentes em Microsoft.AspNetCore.Authentication.JwtBearer 5.0.5. AI-TESTING api executado, mas runner falhou com CommandNotFoundException em -SkipInstall dentro de Run-AIEngine.ps1.

## 2026-04-30 - Build cancelamento WriteOff
Data: 2026-04-30
Agente: ROVIS_BE
Build padrao falhou por DLLs bloqueados por Visual Studio Insiders/IIS Express, sem erro de codigo reportado. Build isolado executado fora do sandbox com OutDir .codex-build/api passou com 0 erros e 770 warnings existentes. AI-TESTING api falhou no runner com CommandNotFoundException em -SkipInstall.

## 2026-04-30 - Build GetRenderedDocument WriteOff
Data: 2026-04-30
Agente: ROVIS_BE
Build isolado executado com OutDir .codex-build/api passou com 0 erros e 890 warnings existentes. AI-TESTING api executado, mas falhou no runner com CommandNotFoundException em -SkipInstall dentro de Run-AIEngine.ps1.

## 2026-05-04 - Build Historia 3 TDO faltantes
Data: 2026-05-04
Agente: ROVIS
dotnet build ABPAC-BackEnd/AlavTech.API/AlavTech.API.csproj --no-restore: OK, 0 erros, avisos preexistentes.`nyarn.cmd build em ABPAC-FrontEnd: OK, avisos Sass/chunk preexistentes.

## 2026-05-05 - Validacao WriteOff GetAllPendingPaged
Data: 2026-05-05
Agente: AI_TESTING
Estado: VALIDATING
Build: dotnet build ABPAC-BackEnd/AlavTech.API/AlavTech.API.csproj -v minimal -o C:\tmp\ABPAC-build\AlavTech.API => OK, 0 errors, warnings preexistentes.
Build padrao: falhou por DLLs bloqueadas por IIS Express/Visual Studio, sem erro de compilacao da alteracao.
AI-TESTING: Run-AIEngine.ps1 -Mode api -SkipInstall -SkipBrowserInstall executado; contrato novo carregado; falhou porque codex CLI nao esta no PATH (spawn codex ENOENT) e endpoint local http://localhost:33422 nao respondeu nos smoke tests.
Relatorios: .cursor/testing-module/reports/ai-final-report.json e .cursor/testing-module/reports/ai-final-report.html.
