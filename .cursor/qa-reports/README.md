# Padrao de relatorios de QA da IA

Esta pasta guarda os relatorios de testes feitos pela IA em um formato facil de entender.

O arquivo central da pasta e:

```text
.cursor/qa-reports/index.html
```

Ele deve listar todos os relatorios em ordem, mostrar um resumo de cada execucao e renderizar o HTML visual selecionado dentro da propria pagina.

Sempre que a IA fizer um teste, ela deve criar uma pasta assim:

```text
.cursor/qa-reports/YYYY-MM-DD-escopo-do-teste/
  README.md
  plans/
  screenshots/
  json/
  html/
```

## O que cada pasta deve ter

- `README.md`: explicacao simples do teste para uma pessoa usuaria.
- `plans/`: planejamento do teste, quando a entrega for uma bateria planejada ou quando a rodada precisar de roteiro antes da execucao.
- `screenshots/`: imagens do navegador, telas de erro, telas testadas e evidencias visuais.
- `json/`: relatorios tecnicos em JSON, como `ai-final-report.json`, `final-report.json`, `generated-cases.json` e relatorios de Playwright.
- `html/`: relatorios HTML, quando existirem.
- `html/relatorio-executivo.html` ou nome equivalente: pagina HTML em portugues, baseada no `README.md`, com resumo visual, galeria, modal de imagem e links para screenshots.

## Template visual obrigatorio

Usar sempre o mesmo padrao do arquivo:

```text
.cursor/qa-reports/2026-04-06-admin-adm1/html/relatorio-executivo-admin.html
```

O contrato detalhado do HTML de QA fica em:

```text
.cursor/qa-reports/templates/qa-html-report-standard.md
```

Esse padrao inclui:
- Hero executivo no topo.
- Cards de status.
- Cards de resumo.
- Timeline de prioridades.
- Secao de erros detalhados.
- Galeria de evidencias.
- Modal para abrir screenshots dentro do proprio HTML.
- Links para JSONs e relatorios tecnicos.
- Secao de proximas acoes.

Ao criar um novo relatorio, adaptar textos, erros, imagens e links, mas manter a mesma estrutura visual.

Na secao de erros detalhados, cada erro deve conter:
- ID unico do erro, por exemplo `QA-SMOKE-001`.
- Severidade.
- Status.
- Area/tela afetada.
- Pre-condicoes.
- Passos para reproduzir.
- Resultado esperado.
- Resultado obtido.
- Sintoma observado.
- Evidencia tecnica, incluindo rota, endpoint, status HTTP, mensagem de console ou screenshot quando houver.
- Impacto pratico para a pessoa usuaria.
- Hipotese de causa provavel.
- Proxima acao recomendada.

## O README.md de cada teste deve explicar

- Qual ambiente foi testado.
- Qual usuario foi usado.
- Quais telas ou fluxos foram testados.
- O que funcionou.
- O que deu erro.
- Qual e o impacto do erro para a pessoa usuaria.
- Onde ficam as imagens.
- Onde ficam os arquivos tecnicos.
- Qual a proxima acao recomendada.

## Regra para abrir o HTML

Depois de terminar um teste e criar a pasta do relatorio, a IA deve sempre tentar abrir primeiro o HTML central:

```text
.cursor/qa-reports/index.html
```

Esse e o painel que reune todos os testes.

Depois disso, quando fizer sentido, a IA tambem pode abrir o HTML visual especifico da rodada.

Se nao conseguir abrir automaticamente, deve informar o caminho do HTML na resposta final.

## Exemplo de nome de pasta

```text
.cursor/qa-reports/2026-04-06-admin-adm1/
```

## Regra importante

Mesmo que os relatorios tecnicos continuem em `.cursor/testing-module/reports/`, a IA deve tambem copiar ou consolidar as evidencias aqui em `.cursor/qa-reports/`.

Depois de criar ou atualizar qualquer relatorio de teste, a IA deve tambem atualizar `.cursor/qa-reports/index.html` com a nova entrada em ordem cronologica, apontando para o HTML visual principal, README e pasta do teste.

Quando o item for um planejamento, a pasta `plans/` deve ficar dentro da pasta do proprio escopo, por exemplo:

```text
.cursor/qa-reports/2026-04-06-bateria-testes-planejamento/plans/
```

Antes de iniciar qualquer bateria, a IA deve ler `.cursor/qa-reports/config/environment.json` e confirmar se `frontendUrl` e `backendUrl` continuam corretas. Se o usuario ja tiver informado as URLs na conversa atual, a IA pode usar essas URLs e atualizar o arquivo.

