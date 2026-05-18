# QA Report - Frontend Smoke ABPAC

Data: 2026-04-07
Escopo: `frontend-smoke`
Agente: `.cursor/agents/11-ai-testing.md`

## Ambiente testado

- Frontend: `http://localhost:5173`
- Backend/API: `https://saas-homolog-api.alav.cloud`
- Fonte de verdade: `.cursor/qa-reports/config/environment.json`
- Navegador: Chromium headless
- Perfil usado: credencial de teste configurada na engine de QA; senha omitida do relatorio

## O que foi testado

- Renderizacao publica da tela de login
- Console inicial da aplicacao
- Tela de recuperacao de senha
- Protecao de rota privada sem sessao
- Tentativa de login contra `/Account/Login`
- Persistencia de sessao apos login
- Responsividade da tela de login em desktop, tablet e mobile

## Resultado geral

- Total de checks: 10
- Passaram: 7
- Falharam: 2
- Skip: 1
- Quality Score: 72/100
- Faixa: Acceptable

O frontend local abriu corretamente e a tela de login ficou utilizavel nos tres viewports avaliados. A rota privada sem sessao tambem se manteve protegida.

Os problemas relevantes da rodada ficaram concentrados em autenticacao e carregamento de menu. O login de teste chamou a API, mas retornou `401` e nao criou sessao. Alem disso, a carga publica registrou erros `500` em `GET /Menu/GetMenus?token=ASIDE`, o que degradou o score e gerou erro de console.

## Lista de erros

### QA-FE-002 - Erro de console com falha 500 no carregamento de menu

- Severidade: Alta
- Status: Aberto
- Area afetada: Login / bootstrap inicial
- Evidencia principal: `screenshots/01-login-desktop.png`
- Evidencia tecnica: `GET https://saas-homolog-api.alav.cloud/Menu/GetMenus?token=ASIDE -> 500`
- Impacto pratico: a pessoa usuaria pode encontrar comportamento instavel logo na carga inicial, mesmo antes do login.

### QA-AUTH-001 - Login de teste nao estabeleceu sessao

- Severidade: Alta
- Status: Aberto
- Area afetada: Autenticacao
- Evidencia principal: `screenshots/05-post-login.png`
- Evidencia tecnica: `POST https://saas-homolog-api.alav.cloud/Account/Login -> 401`
- Impacto pratico: a pessoa usuaria de teste nao conseguiu entrar no sistema e o smoke das rotas internas ficou bloqueado.

## Impacto para a pessoa usuaria

- O acesso inicial ao sistema continua disponivel, mas o bootstrap ja apresenta erro de backend em recurso de menu.
- A navegacao autenticada nao foi validada nesta rodada porque a sessao nao foi criada com a credencial configurada no ambiente de QA.
- O risco residual esta concentrado em menu lateral, disponibilidade de rotas internas e confiabilidade do fluxo de login.

## Onde ver as evidencias

- Screenshots: `.cursor/qa-reports/2026-04-07-frontend-smoke/screenshots/`
- JSON tecnico: `.cursor/qa-reports/2026-04-07-frontend-smoke/json/frontend-smoke-results.json`
- HTML visual: `.cursor/qa-reports/2026-04-07-frontend-smoke/html/relatorio-executivo-frontend-smoke.html`
- Central de relatorios: `.cursor/qa-reports/index.html`

## Observacoes da execucao

- A rodada tecnica usada neste consolidado veio do arquivo `json/frontend-smoke-results.json`, gerado em 2026-04-07 11:04:49.
- Foi feita tentativa de reexecucao local nesta sessao, mas o `node` da sandbox falhou ao resolver o caminho do workspace via `OneDrive` (`EPERM: lstat c:\\Users\\deviv\\OneDrive`). O bloqueio foi do ambiente da automacao, nao do produto testado.

## Proxima acao recomendada

1. Investigar o `500` em `/Menu/GetMenus?token=ASIDE`.
2. Validar a credencial de QA e o motivo do `401` em `/Account/Login`.
3. Reexecutar o smoke de front-end apos a correcao para liberar o bloco de rotas internas autenticadas.
