# Plano de QA - Frontend Smoke ABPAC

Data: 2026-04-07
Escopo: frontend-smoke
Agente: `.cursor/agents/11-ai-testing.md`

## Ambiente confirmado

- Frontend: `http://localhost:5173`
- Backend/API: `https://saas-homolog-api.alav.cloud`
- Fonte de verdade: `.cursor/qa-reports/config/environment.json`
- Usuario de teste: carregado de `.cursor/testing-module/ai-engine/.env`, sem registrar senha em relatorio

## Regras aplicadas

- Somente modo QA.
- Nao ativar ROVIS-FE.
- Nao ativar ROVIS-BE.
- Nao alterar codigo de produto.
- Alterar somente relatorios, planejamento, automacao de teste e configuracao de QA.
- Executar testes com navegador para escopo front-end.

## Casos planejados

| ID | Tipo | Rota/Tela | Criterio |
| --- | --- | --- | --- |
| QA-SMOKE-001 | Browser | `/` | Login renderiza com campos de e-mail, senha, botao Entrar e link de recuperacao. |
| QA-SMOKE-002 | Browser | `/` | Tela inicial nao exibe erro fatal de console nem pagina em branco. |
| QA-SMOKE-003 | Browser | `/usuario/esqueceu_senha` | Fluxo de recuperacao abre e exibe campo de e-mail. |
| QA-SMOKE-004 | Browser | `/adm/dashboard` sem sessao | Rota privada nao deve expor dashboard sem autenticacao. |
| QA-SMOKE-005 | Browser/API | `/` login | Tentativa de login com credencial de teste deve chamar `/Account/Login` e nao vazar senha no relatorio. |
| QA-SMOKE-006 | Browser | pos-login | Quando login for aceito, deve redirecionar para area interna e manter token de autenticacao. |
| QA-SMOKE-007 | Browser | rotas internas | Se autenticado, visitar dashboard/listas principais e coletar erros de console/network. |
| QA-SMOKE-008 | Responsivo | `/` | Capturar evidencia desktop, tablet e mobile da tela de login. |

## Rotas internas selecionadas

- `/adm/dashboard`
- `/adm/usuarios/lista`
- `/crm/lista`
- `/financeiro/rateio/lista`
- `/ocorrencias/lista`
- `/work-orders`

## Criterios de bloqueio

- Frontend indisponivel.
- Login renderiza pagina em branco.
- Console com erro fatal no smoke publico.
- Rota privada acessivel sem sessao de forma indevida.
- Login retorna erro 5xx.
- Quality Score abaixo de 50.

## Evidencias esperadas

- Screenshots em `../screenshots/`.
- JSON tecnico em `../json/frontend-smoke-results.json`.
- README executivo em `../README.md`.
- HTML visual em `../html/relatorio-executivo-frontend-smoke.html`.
- Indice central atualizado em `.cursor/qa-reports/index.html`.
