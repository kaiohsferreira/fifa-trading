# QA Report - Rerun QA-SMOKE-006

Data: 2026-04-07
Escopo: `frontend-smoke-rerun-01`
Caso executado: `QA-SMOKE-006 - Login aceito cria sessao`
Agente: `.cursor/agents/11-ai-testing.md`

## Ambiente testado

- Frontend: `http://localhost:5173`
- Backend/API: `https://saas-homolog-api.alav.cloud`
- Fonte de verdade: `.cursor/qa-reports/config/environment.json`
- Navegador: Chromium headless
- Usuario usado: `admsaas@uorak.com`
- Senha: omitida do relatorio

## Resultado geral

- Total de checks: 1
- Passaram: 1
- Falharam: 0
- Quality Score: 100/100
- Faixa: Excellent

O teste `QA-SMOKE-006` passou nesta repeticao. O login respondeu `202`, a aplicacao redirecionou para `http://localhost:5173/adm/dashboard` e o navegador ficou com cookie de autenticacao presente.

## O que foi validado

- Preenchimento do formulario de login com as credenciais informadas na conversa
- Chamada de `POST /Account/Login`
- Redirecionamento para area autenticada
- Presenca de sessao por cookie de autenticacao

## Observacoes tecnicas

- Evidencia de sessao: `cookieToken=1`
- URL final: `http://localhost:5173/adm/dashboard`
- Status do login: `202`
- O bootstrap inicial ainda registrou respostas `500` em `GET /Menu/GetMenus?token=ASIDE` antes do submit, mas isso nao impediu a autenticacao nesta rodada isolada.
- Depois do login, as chamadas de menu passaram a responder `200`.

## Impacto para a pessoa usuaria

- A pessoa usuaria com essas credenciais consegue entrar no sistema e chegar ao dashboard administrativo.
- O caso especifico de criacao de sessao ficou validado com sucesso.
- Ainda existe um risco residual no carregamento inicial de menu porque houve erros `500` antes do login.

## Onde ver as evidencias

- Screenshots: `.cursor/qa-reports/2026-04-07-frontend-smoke-rerun-01/screenshots/`
- JSON tecnico: `.cursor/qa-reports/2026-04-07-frontend-smoke-rerun-01/json/qa-smoke-006-result.json`
- HTML visual: `.cursor/qa-reports/2026-04-07-frontend-smoke-rerun-01/html/relatorio-executivo-qa-smoke-006.html`
- Central de relatorios: `.cursor/qa-reports/index.html`

## Proxima acao recomendada

1. Considerar `QA-SMOKE-006` validado para as credenciais `admsaas@uorak.com`.
2. Investigar separadamente a instabilidade de `Menu/GetMenus?token=ASIDE` na carga inicial.
3. Se necessario, repetir os checks de navegacao autenticada usando esta mesma conta.
