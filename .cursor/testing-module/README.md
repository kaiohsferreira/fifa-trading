# Testing Module

Módulo dedicado para geração e execução automática de casos de teste ao final do fluxo.

## O que este módulo cobre
- Chamada de métodos backend e validação de retorno.
- Execução de fluxo frontend (via comandos/adapter).
- Validação de campos (`required`, extensível).
- Validação de máscaras por regex.
- Geração de casos por contrato (`contract-first`/`hybrid`).
- Fuzz/property tests para campos e máscaras.
- Quality gates com fail-fast (exit code 1 em violação).
- Geração de relatório consolidado em JSON.

## Estrutura
- `config/testing-targets.sample.json`: alvo e estratégia de geração.
- `config/testing-targets.json`: alvo efetivo usado no runner.
- `config/quality-gates.json`: thresholds de qualidade e bloqueio.
- `scripts/Generate-TestCases.ps1`: gera casos automáticos.
- `scripts/Generate-TargetsFromRepo.ps1`: gera arquivo de alvos reais por auto-detecção do repo.
- `scripts/Check-RealTargetsReadiness.ps1`: mede prontidão de alvos reais (mock vs real).
- `scripts/Promote-StrictMode.ps1`: promove gate estrito quando houver comando real.
- `scripts/Run-TestModule.ps1`: executa casos e produz relatório.
- `reports/`: saída de casos e execução.
- `reports/history/`: histórico de execuções e tendências.

## Execução rápida
```powershell
powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Run-TestModule.ps1
```
Sem `-TargetsPath`, o runner escolhe automaticamente nesta ordem:
1. `.cursor/testing-module/config/testing-targets.json`
2. `.cursor/testing-module/config/testing-targets.sample.json`
3. `.cursor/testing-module/config/testing-targets.real.json` (fallback)

Para priorizar `testing-targets.real.json`, use:
```powershell
$env:PREFER_REAL_TARGETS='true'
```

## Fluxo recomendado de uso
1. Copiar `config/testing-targets.sample.json` para `testing-targets.json`.
2. Substituir comandos de exemplo por chamadas reais do projeto.
3. Executar o módulo no fim da entrega (local/CI).
4. Ler `.cursor/testing-module/reports/final-report.json`.

Atalho para iniciar com alvo real sugerido:
```powershell
powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Generate-TargetsFromRepo.ps1
```

Validação de prontidão de alvo real:
```powershell
powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Check-RealTargetsReadiness.ps1
```

Promoção automática para modo estrito:
```powershell
powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Promote-StrictMode.ps1
```

## Integração com CI
No pipeline final, chamar:
```powershell
powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Run-TestModule.ps1 -TargetsPath .cursor/testing-module/config/testing-targets.json
```
Se houver falha/violação de gate, o comando retorna código de saída `1`.

## Observabilidade
- Cada execução grava histórico em:
  `.cursor/testing-module/reports/history/run-history.jsonl`
- Resumo de tendência em:
  `.cursor/testing-module/reports/history/summary.json`
- O relatório final inclui:
  `observability.targetsSource`, `observability.commandCases`, `observability.realCommandCases`, `observability.mockCommandCases`.

## Gate de realidade em CI
- `quality-gates.json` possui `requireRealTargetsInCi=true`.
- Em ambiente CI (`CI=true`), o runner reprova quando `realCommandCases <= 0`.


## Execução automática após modificação

Watcher (cada alteração de arquivo):
```powershell
powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Watch-ChangesAndRun.ps1
```

Hooks Git (commit/merge/checkout):
```powershell
powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Install-GitHooks.ps1
```
O instalador cria também `pre-commit` e `pre-push` com bloqueio por falha de teste/gate.

## Validação de scorecard dos agentes

Executar check automático:
```powershell
powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Check-AgentScorecard.ps1
```

Esse check é consumido pelo target padrão como caso real obrigatório.
