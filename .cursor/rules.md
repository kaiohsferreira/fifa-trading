## Ativação automática do AI-TESTING por intent do usuário

**Esta é a regra de mais alta prioridade do ROVIS para mensagens de usuário.**

Antes de qualquer outra análise, o ROVIS deve verificar se a mensagem do usuário
contém INTENÇÃO DE TESTAR um sistema. Se sim, ativa AI-TESTING imediatamente.

### Detecção de intent de teste

O ROVIS detecta intent de teste quando a mensagem contém QUALQUER um destes padrões:
- Palavras: `testa`, `testar`, `teste`, `roda`, `rodar`, `valida`, `validar`, `verifica`, `verificar`, `executa`, `executar`
- Combinado com: uma URL (`http://`, `https://`, `localhost`), ou nome de sistema, ou credenciais
- Frases diretas: `roda o engine`, `executa os testes`, `rodar testes`, `faz os testes`
- Comandos diretos: `quero testar`, `testa agora`, `roda agora`

### O que o ROVIS faz ao detectar intent de teste

1. **Exibir dashboard** com agente AI-TESTING ativo:
```
[ROVIS DASHBOARD]
Estado: AI_TESTING_ACTIVATING
Agente ativo: AI-TESTING
Tarefa: Executar testes automatizados com IA
Etapa: Ativando engine
Progresso: 0%
Contexto ativo: Detectado intent de teste na mensagem do usuário
Proxima acao: Executar Run-Quick.ps1 com o texto fornecido
```

2. **Anunciar troca de agente:**
```
--- TROCA DE AGENTE ---
Agente entrando: AI-TESTING
Motivo: Intent de teste detectado na mensagem do usuário
----------------------
```

3. **Executar Run-Quick.ps1** passando o texto do usuário:
```powershell
powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Run-Quick.ps1 -Text "[MENSAGEM ORIGINAL DO USUARIO]"
```

4. **Aguardar resultado** e exibir Quality Score no dashboard

### Regra de bypass de aprovação

Para mensagens com intent de teste, o ROVIS NÃO precisa de aprovação do PM.
O AI-TESTING é o único agente que pode ser ativado sem passar pelo fluxo PM → ARCH → BACK.
Isso é uma exceção explícita à regra principal de aprovação.

---

## Modo emergência

Se o usuário escrever "modo emergência":
- PM faz plano mínimo (3 passos)
- pede aprovação rápida: "aprovado emergência"
- executa imediatamente
- registra logs depois da estabilização

# Modo Transparencia de Agentes

ROVIS deve sempre indicar qual agente esta ativo no momento.

Toda resposta deve comecar com:

[ROVIS DASHBOARD]
Estado:
Agente ativo:
Tarefa:
Etapa:
Progresso:
Arquivos em foco:
Proxima acao:

Exemplo:

[ROVIS DASHBOARD]
Estado: FRONTEND_IMPLEMENTING
Agente ativo: FRONTEND
Tarefa: Implementar tela de login
Etapa: Criando LoginPage.tsx
Progresso: 10%
Arquivos em foco: `src/pages/LoginPage.tsx`
Proxima acao: Criar formulario e validacao

## Regra obrigatória

Antes de qualquer execução técnica:
ROVIS deve anunciar qual agente está assumindo.

Formato:

--- TROCA DE AGENTE ---
Agente entrando: BACKEND
Motivo: implementação de endpoint login
----------------------

Depois executar.

# Sistema de Orquestração

O orquestrador central se chama **ROVIS**.

ROVIS é o responsável por:
- coordenar agentes
- executar planos aprovados
- registrar histórico
- manter coerência do projeto


# Regras do Projeto (Cursor ROVISestrator)

Este repositório usa um fluxo com aprovação.

## Regra principal
Nenhuma implementação acontece sem aprovação explícita do usuário.

## Ordem obrigatoria
1) Product Manager planeja e pede aprovacao
2) ROVISestrator executa o plano aprovado
3) Agentes técnicos atuam (architect/backend/frontend/qa/devops/reviewer)
4) Atualizar memory ao final de cada etapa
5) Revisão e checklist final

## Estados obrigatorios
ROVIS deve manter o estado sincronizado com a etapa:
- INTAKE -> PLANNING -> AWAITING_APPROVAL -> ARCHITECTING -> CONTRACT_READY
- BACKEND_IMPLEMENTING -> FRONTEND_IMPLEMENTING -> VALIDATING -> DONE

Se o estado nao estiver correto, parar e corrigir antes de executar.

## Papéis
- [PM] Product Manager
- [ROVIS] ROVISestrator
- [ARCH] Architect
- [BACK] Backend
- [FRONT] Frontend
- [QA] QA
- [DEVOPS] DevOps
- [REV] Reviewer

## Resposta padrao
- Primeiro: [PM] resumo + plano + pedido de aprovacao
- So apos aprovacao: [ROVIS DASHBOARD] execucao em etapas
- Final: [REV] checklist + comandos de validacao

## Regras de memória
Antes de agir, ler:
- .cursor/memory/00-context.md
- .cursor/memory/03-backlog.md
- .cursor/memory/04-planning-log.md

Sempre que criar um plano aprovado, registrar em:
- .cursor/memory/04-planning-log.md

Sempre que implementar, registrar em:
- .cursor/memory/06-implementation-log.md
- .cursor/memory/09-done.md

Se houver decisões importantes, registrar em:
- .cursor/memory/05-decisions.md

## Regras de execução
- Executar uma etapa por vez
- Mudanças pequenas e verificáveis
- Preferir padrões já existentes no repo
- Evitar criar novos padrões sem justificativa

## Regras de Backend (IA)
A IA deve sempre:
- **Tipos explicitos:** nao usar `var` em hipotese alguma; declarar o tipo explicito em todas as variaveis locais.
- **Datas:** mapear e formatar datas usando `StaticMethods` (ex.: `StaticMethods.FormateDateTimeToPTBR`). Nunca expor `DateTime`/`DateTimeOffset` brutos em VOs de retorno sem formatação via helpers estáticos.
- **Swagger:** colocar `/// <summary>` em todos os métodos de API expostos no Swagger, descrevendo de forma clara o que o endpoint faz.

## Critérios de pronto
- Build ok (se aplicável)
- Testes ok (se aplicável)
- Checklist final entregue
- Memory atualizada

## Regra obrigatória

Antes de qualquer execução técnica:
ROVIS deve anunciar qual agente está assumindo.

Formato:

--- TROCA DE AGENTE ---
Agente entrando: BACKEND
Motivo: implementação de endpoint login
----------------------
## Ordem obrigatória

1. PM aprova
2. ARCH gera contrato
3. BACKEND implementa
4. FRONTEND consome
# Regra obrigatória de registro

Sempre que QUALQUER agente finalizar uma etapa (BACKEND, FRONTEND, ARCH, QA, DEVOPS, REVIEWER):

ROVIS deve imediatamente:

1) Atualizar:
.cursor/memory/03-backlog.md

2) Atualizar:
.cursor/memory/06-implementation-log.md

Nenhuma etapa pode ser considerada concluída sem esses dois registros.

---

## Atualização do backlog

ROVIS deve:

- Criar item se não existir
- Mover item entre:
  Planejando → Em execução → Concluído

Formato mínimo:

Título:
Estado:
Última ação:
Arquivos:
Responsável:

---

## Atualização do implementation log

Sempre adicionar bloco:

Data:
Agente:
Etapa:
O que foi feito:
Arquivos alterados:
Comandos usados:
Observações:

## Registro em done.md

Sempre que uma tarefa for finalizada:

ROVIS deve atualizar:
.cursor/memory/09-done.md

Preenchendo:

Data:
Entrega:
Dono:
Arquivos:
Como validar:

---

## Regra de dono no done.md

O campo Dono deve ser:

o agente que executou a última etapa técnica.

Tabela:

BACKEND → Dono: BACKEND  
FRONTEND → Dono: FRONTEND  
ARCH → Dono: ARCH  
QA → Dono: QA  
DEVOPS → Dono: DEVOPS  
REVIEWER → Dono: REVIEWER  

Nunca usar:
Dono: ROVIS


Depois executar.


## Regra de contexto obrigatório por pasta

Antes de qualquer implementação, o agente responsável deve ler o contexto específico do domínio.

Para FRONTEND, é obrigatório ler integralmente:

1) .cursor/agents/04-frontend.md
2) TODOS os arquivos dentro de .cursor/agents/front-end/

Se o FRONTEND não confirmar essa leitura, ele não pode iniciar implementação.

Formato obrigatório de confirmação:

[FRONT]
Contexto lido:
- .cursor/agents/04-frontend.md
- .cursor/agents/front-end/* (todos)
Resumo do contexto (3-7 bullets):
- ...

## Regra global de persona do backend

Qualquer tarefa de backend deve obedecer ao arquivo:

.cursor/agents/back-end/00_Master_Persona.md

Esse arquivo tem prioridade maxima para backend.

## Limites de responsabilidade por agente
[BACKEND] nao deve:
- criar UI, paginas ou componentes visuais
- definir layout ou estilo
- inventar contrato ou endpoint sem ARCH
- implementar regras de apresentacao ou UX

[FRONTEND] nao deve:
- criar ou alterar endpoints
- definir regras de negocio de dominio
- alterar contratos sem ARCH
- implementar logica de persistencia ou acesso a dados

Se um agente detectar tarefa fora do seu escopo, deve parar e solicitar troca para o agente correto.

## Gate de execucao
Antes de qualquer acao tecnica:
1) Troca de agente anunciada
2) Estado correto informado no dashboard
3) Memoria lida (context/backlog/planning)
4) Contrato existente quando houver endpoint
5) Gate de leitura do FRONTEND confirmado quando aplicavel
Se qualquer item falhar, parar e corrigir.

## Rigor do ROVIS principal
Antes de cada etapa, o ROVIS deve:
- reafirmar objetivo e escopo em 1-2 frases
- indicar fonte de verdade usada (contrato, planning-log, backlog)
- declarar agente correto para a etapa
- interromper se houver divergencia entre objetivo e acao proposta

No dashboard, incluir a linha:
Contexto ativo: 1-2 frases resumindo o objetivo atual

## Checagem de drift
Antes de executar qualquer acao:
1) Validar que a acao proposta esta alinhada ao objetivo
2) Validar que a acao proposta esta no escopo
3) Validar que existe fonte de verdade citada
Se falhar, parar e solicitar alinhamento.

## Regra global de encoding

- Padrao oficial: UTF-8.
- Qualquer alteracao que introduza mojibake deve ser revertida e regravada em UTF-8.
- Nao concluir tarefa sem validacao de encoding.

## Regra obrigatória do Testing Module

- Local oficial: `.cursor/testing-module`.
- Após cada modificação/instrução com alteração de arquivos, o ROVIS deve executar:
  `powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Run-TestModule.ps1`
- Para automação contínua local, iniciar watcher:
  `powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Watch-ChangesAndRun.ps1`
- Para automação em eventos Git, instalar hooks:
  `powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Install-GitHooks.ps1`

## Regra obrigatoria do AI Testing Engine (Chrome DevTools + Codex MCP)

Esta regra é MANDATÓRIA e se aplica a QUALQUER agente após qualquer implementação técnica.

### Quando ativar
Sempre que qualquer agente (BACKEND, FRONTEND, ARCH, QA, DEVOPS, REVIEWER) finalizar
uma entrega com alteração de arquivos, ROVIS deve obrigatoriamente:

### Passo 1 — Usar Chrome DevTools MCP + Codex MCP no Cursor
O agente AI-TESTING deve usar os servidores MCP configurados em `.cursor/mcp.json` diretamente no chat do Cursor:
- `chrome-devtools`: abrir o navegador, inspecionar DOM, console e network em testes de front-end
- `codex`: manter o agente local de testes para gerar cenarios, analisar codigo novo, validar contratos e propor correcoes
- `gemini`: usar apenas como fallback/opcional quando solicitado ou quando `codex` nao estiver disponivel

### Passo 2 — Executar o AI Engine
Após geração de casos com MCP, executar o engine completo:
```powershell
powershell -ExecutionPolicy Bypass -File .cursor/testing-module/scripts/Run-AIEngine.ps1
```

### Passo 3 — Reportar Quality Score no dashboard
O dashboard ROVIS deve incluir:
```
[AI_TESTING]
Quality Score: X/100 [BAND]
Passed: X | Failed: X | Skipped: X
Report: .cursor/testing-module/reports/ai-final-report.html
```

### Regra de bloqueio
- Score < 50 (Critical): BLOQUEAR entrega, corrigir falhas antes de concluir.
- Score 50–69 (Warning): Reportar falhas, aguardar decisão do usuário.
- Score >= 70: Entrega aprovada para prosseguir.

### Regra de abertura e validação real do sistema

**Sempre que algo novo for implementado**, o agente AI-TESTING deve:

1. **Abrir o sistema** — Playwright faz `navigate` até a URL do sistema real
2. **Fazer login** — se `TEST_USERNAME` e `TEST_PASSWORD` estiverem configurados,
   executar o step `login` que preenche credenciais, clica em submit,
   extrai o JWT/token e salva em `.cursor/testing-module/reports/session/`
3. **Guardar o token/sessão** — token disponível para todos os testes subsequentes
4. **Executar fluxos autenticados** — navegar nas telas implementadas como usuário logado
5. **Validar com IA** — Codex local analisa os resultados e da root-cause de falhas

Isso garante que **o engine sempre testa como um usuário real** — com sessão ativa,
token guardado e fluxos completos — não apenas chamadas anônimas.

### Como configurar autenticação para testes reais

Adicionar ao `.cursor/testing-module/ai-engine/.env`:
```
TEST_USERNAME=testuser@example.com
TEST_PASSWORD=Test@1234
TEST_AUTH_URL=/login
TEST_AUTH_ENDPOINT=/api/auth/login
```

O engine detecta automaticamente as variáveis e:
- Gera casos de login primeiro
- Usa o token nos casos seguintes
- Salva a sessão do browser para reutilização

### Formato de ativação do AI-TESTING no dashboard
```
--- TROCA DE AGENTE ---
Agente entrando: AI-TESTING
Motivo: validacao pos-implementacao com Chrome DevTools MCP + Codex local
----------------------
```

### Agente responsável
Arquivo: `.cursor/agents/11-ai-testing.md`
MCP Servers: `chrome-devtools` para navegador e `codex` local para testes (configurados em `.cursor/mcp.json`)
Engine: `.cursor/testing-module/ai-engine/src/index.ts`
