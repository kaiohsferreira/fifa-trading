# Plano de QA - Rerun QA-SMOKE-006

Data: 2026-04-07
Escopo: `frontend-smoke-rerun-01`
Objetivo: repetir somente o teste `QA-SMOKE-006 - Login aceito cria sessao`
Agente: `.cursor/agents/11-ai-testing.md`

## Ambiente confirmado

- Frontend: `http://localhost:5173`
- Backend/API: `https://saas-homolog-api.alav.cloud`
- Fonte de verdade: `.cursor/qa-reports/config/environment.json`
- Credenciais informadas na conversa atual:
  - Email: `admsaas@uorak.com`
  - Senha: omitida dos relatorios

## Regra desta rodada

- Modo QA somente
- Sem ativar ROVIS-FE
- Sem ativar ROVIS-BE
- Sem alterar codigo de produto
- Executar somente o caso `QA-SMOKE-006`

## Caso planejado

| ID | Tipo | Rota/Tela | Criterio |
| --- | --- | --- | --- |
| QA-SMOKE-006 | Browser | `/` pos-login | Login deve ser aceito e gerar sessao persistida via token, cookie e/ou redirecionamento para area autenticada. |

## Evidencias esperadas

- Screenshot antes do envio do login
- Screenshot apos o retorno do login
- JSON tecnico da rodada
- README executivo
- HTML visual consolidado
