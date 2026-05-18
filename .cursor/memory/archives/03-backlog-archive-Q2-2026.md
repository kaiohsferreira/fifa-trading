
## Concluido - [2026-03-27] Simulacao Rateio - checkbox aba Ocorrencias concluidas

- [2026-03-27] Simulacao Rateio - checkbox aba Ocorrencias concluidas
  Titulo: Coluna de selecao na tabela de Ocorrencias concluidas igual a aba Ocorrencias
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: FE_UI adicionou coluna 36px com checkbox e estado de selecao em SimulationDeltaList.
  Arquivos: ABPAC-FrontEnd/src/components/local/SimulacaoRateio/SimulationDeltaList.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: FRONTEND

## Concluido - [2026-03-27] Simulacao Rateio - divisores verticais aba Ocorrencias

- [2026-03-27] Simulacao Rateio - divisores verticais aba Ocorrencias
  Titulo: Igualar divisoes verticais entre colunas da tabela Ocorrencias ao padrao da aba Ocorrencias concluidas
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: FE_UI aplicou border-r/border-b por celula em SimulacaoRateioOsContent, espelhando SimulationDeltaList.
  Arquivos: ABPAC-FrontEnd/src/components/local/SimulacaoRateio/SimulacaoRateioOsContent.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: FRONTEND
>>>>>>> 7248af81 (feat: implement visual enhancements and functionality for Simulacao Rateio, including checkbox selections and improved UI consistency across components)

## Concluido (ROVIS-FE)

- [2026-03-26] Ocorrencias - coluna Rateado em Sim/Não
  Titulo: Ocorrencias - trocar true/false por Sim/Não na coluna Rateado
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Adicionada coluna customizada para `isApportioned` na listagem de ocorrencias, exibindo badge "Sim" (verde) e "Não" (vermelho), incluindo parse para valores boolean/string/numero.
  Arquivos: ABPAC-FrontEnd/src/pages/ocorrencias/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/04-planning-log.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-26] Simulacao de Rateio - separar listagem inicial e editor
  Titulo: Abrir Simulacao de Rateio por listagem e mover editor para pasta separada
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: `financeiro/simulacao_rateio/lista` virou listagem padrao com criar/visualizar/editar (editar so para nao-rateadas) e a tela de simulacao foi movida para `financeiro/simulacao_rateio/simulacao`, com novas rotas de adicionar/visualizar/editar.
  Arquivos: ABPAC-FrontEnd/src/pages/financeiro/simulacao_rateio/lista/index.tsx; ABPAC-FrontEnd/src/pages/financeiro/simulacao_rateio/simulacao/index.tsx; ABPAC-FrontEnd/src/routes/appRoutes.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-26] Simulacao de Rateio - abrir na aba Ocorrencias por padrao
  Titulo: Simulacao de Rateio - ao abrir selecionar "Ocorrencias"
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Ajustado o default de `activeTab` na pagina `financeiro/simulacao_rateio/lista` para `"occurrences"`, garantindo que a tab "Ocorrencias" venha selecionada ao abrir (valor agora bate com `TAB_LIST`).
  Arquivos: ABPAC-FrontEnd/src/pages/financeiro/simulacao_rateio/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md; .cursor/memory/04-planning-log.md
  Responsavel: ROVIS_FE

- [2026-03-25] Simulacao de Rateio - Delta com endpoint GetAllFinishedPaged
  Titulo: Consumir POST /Occurrence/GetAllFinishedPaged na aba Delta com tabela paginada e busca
  Estado: Concluido
  Classificacao: CONTRACT_CONSUMPTION
  Ultima acao: Implementado SimulationDeltaList com PostRequest, tipos OccurrenceFinishedPaged*, rota API_OCCURRENCE.GET_ALL_FINISHED_PAGED, colunas a partir do retorno (preferencia *Str), debounce e NoAssociationSelected.
  Arquivos: ABPAC-FrontEnd/src/components/local/SimulacaoRateio/SimulationDeltaList.tsx; ABPAC-FrontEnd/src/config/apiRoutes/occurrence.ts; ABPAC-FrontEnd/src/types/api/OccurrenceTypes.ts; ABPAC-FrontEnd/src/pages/financeiro/simulacao_rateio/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-25] Financeiro - criar index pai de Simula??o de Rateio com header fixo e tabs
  Titulo: Estruturar tela pai de Simula??o de Rateio para acoplar componentes por aba
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Criada a p?gina `financeiro/simulacao_rateio/lista` com `PrivatePageStructure`, bloco fixo superior (t?tulo, per?odo, a??es, cards de resumo e tabs) e container din?mico para renderiza??o por aba, al?m de rota dedicada em `appRoutes.tsx`.
  Arquivos: ABPAC-FrontEnd/src/pages/financeiro/simulacao_rateio/lista/index.tsx; ABPAC-FrontEnd/src/pages/financeiro/simulacao_rateio/lista/simulacaoRateioList.module.scss; ABPAC-FrontEnd/src/routes/appRoutes.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE
- [2026-03-18] Ocorrencia - padronizar tabs e acoes no dark mode
  Titulo: Ajustar tabs e bot?es do topo (Ocorr?ncia) para padr?o do sistema e dark mode
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Na tela de Ocorr?ncia (editar), as tabs estavam com visual fora do padr?o. Ajustado para usar `TabNavigation` (padr?o p?lula horizontal com ativo azul) ocupando a linha toda. Os bot?es/atalhos do topo (toolbar + Galeria de Anexos) receberam override no dark mode (bg #262626, borda #525252, texto claro) para evitar contraste errado e os bot?es do topo foram ajustados para `width: auto` (n?o ocupar tudo).
  Arquivos: ABPAC-FrontEnd/src/components/local/PageOcurrencies/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE
- [2026-03-18] CRM - Link da Cotacao (dark mode)
  Titulo: Corrigir contraste do modal "Link da Cotacao" no dark mode
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: No modal de link da cota??o (CRM), o bloco de logs e o input estavam com fundo claro no dark por dependerem de seletor global de tema. Ajustado para aplicar classes dark explicitamente (paleta `neutral`) no input e no container/lista de logs, e aplicado override no bot?o "Copiar" no tema dark (bg #262626, borda #525252, texto claro). (Sem borda/caixa nos itens do log.) Ajustado tamb?m o layout/largura para o input do link n?o ficar pequeno.
  Arquivos: ABPAC-FrontEnd/src/components/local/CrmFormPage/QuoteActionsModal/index.tsx; ABPAC-FrontEnd/src/components/local/CrmFormPage/QuoteActionsModal/quoteActionsModal.module.scss; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE
- [2026-03-18] Ades?o - Link de assinatura da ficha (dark mode)
  Titulo: Corrigir contraste do modal "Link de assinatura da ficha" no dark mode
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: No modal de link de assinatura, a paleta do dark mode estava azulada (`slate`) e o bot?o "Copiar" ficava claro demais, destoando do restante. Ajustado o SCSS do modal para paleta `neutral` (bg/border/text) e aplicado override no bot?o "Copiar" no tema dark (bg #262626, borda #525252, texto claro).
  Arquivos: ABPAC-FrontEnd/src/components/local/PageAccession/RegistrationFormManeger/SignatureActionsModal/index.tsx; ABPAC-FrontEnd/src/components/local/PageAccession/RegistrationFormManeger/SignatureActionsModal/signatureActionsModal.module.scss; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE
- [2026-03-18] Ades?o - Detalhes da ficha de inscri??o (dark mode)
  Titulo: Corrigir contraste e bot?o "Fechar" no modal Detalhes (ficha de inscri??o)
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: O modal de Detalhes (usado na ficha de inscri??o) estava com paleta `slate` no dark mode e o bot?o "Fechar" herdava largura 100% + fundo claro, ficando como uma barra branca. Ajustado `DataTableModalDetail` para usar paleta `neutral` no dark mode e for?ar `width: auto` no bot?o, com background escuro (#262626) apenas no tema dark.
  Arquivos: ABPAC-FrontEnd/src/components/ui/DataTable/DataTableModal/DataTableModalDetail.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE
- [2026-03-18] Requerimento de Ades?o - cor do card de Signat?rio igual ao Documento
  Titulo: Alinhar background/borda do card do signat?rio com o FormSection do Documento
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: O card do signat?rio estava com fundo/borda diferentes do bloco Documento no dark mode. Ajustado para usar a mesma combina??o do `FormSection` (bg-neutral-800 + border-zinc-600) e no light (bg-neutral-50 + border-neutral-200).
  Arquivos: ABPAC-FrontEnd/src/components/local/PageAccession/AdhesionManeger/FormbuildAdhesion/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE
- [2026-03-18] Requerimento de Ades?o - ajustar paleta do dark mode para padr?o do projeto
  Titulo: Remover tons azulados (slate) e alinhar dark mode para neutral do ABPAC
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: A tela estava usando classes `slate` (bg/border/text) no dark mode, resultando em apar?ncia azulada. Substitu?do por `neutral` e fundo #262626 nos selects para ficar consistente com o restante do sistema.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageAccession/AdhesionManeger/FormbuildAdhesion/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE
- [2026-03-18] Cota??o - enviar expirationDate sem timezone (YYYY-MM-DD)
  Titulo: Ajustar payload de validade da cota??o para enviar apenas a data
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: O submit da cota??o deixou de converter a data para ISO com timezone (ex: 2026-03-18T00:00:00.000Z) e passou a enviar apenas YYYY-MM-DD em expirationDate, mantendo valida??o por data.
  Arquivos: ABPAC-FrontEnd/src/components/local/CrmFormPage/FormBuildQuote/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE
- [2026-03-17] Tipos de O.S. - inputs com Label acima (padrao do sistema)
  Titulo: Ajustar labels do formulario para o componente Label
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Os campos do formulario passaram a exibir `Label` acima do input/select (incluindo asterisco de required), removendo labels customizados e garantindo o mesmo padrao visual das telas do sistema.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/tipos_de_os/components/OccurrenceWorkOrderTypeForm.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md; .cursor/memory/04-planning-log.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE
- [2026-03-17] Tipos de O.S. - Gerar Financeiro sem opcao fixa "Nao informar"
  Titulo: Remover "Nao informar" do dropdown Gerar Financeiro
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Removida a injecao local de option vazia ("Nao informar") no select Gerar Financeiro. O dropdown agora exibe apenas as opcoes vindas do getOptions (financialTypes).
  Arquivos: ABPAC-FrontEnd/src/pages/adm/tipos_de_os/components/OccurrenceWorkOrderTypeForm.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md; .cursor/memory/04-planning-log.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE
- [2026-03-12] Entrada de Estoque - modal reseta campos ao fechar e reabrir
  Titulo: Modal Entrada de Estoque deve exibir campos em branco ao reabrir
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Adicionado useEffect com ref (wasOpenRef) que ao fechar o modal (open passa de true para false) reseta todo o estado do formulario: tipo/status/rateio/financeiro/plano de contas, itens, fornecedor, datas e submodais. Ao reabrir, os useEffects existentes preenchem os padroes (API e data atual).
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/entrada/components/StockEntryModal.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE
- [2026-03-10] Transfer?ncia para T?cnico - troca de status e cancelar
  Titulo: Bot?o troca de status (Pendente -> Em transfer?ncia -> Transferido) e bot?o Cancelar no modal Transfer?ncia para T?cnico
  Estado: Concluido
  Classificacao: CONTRACT_CONSUMPTION
  Ultima acao: Consumo do contrato equipment-transfer-change-status: rota CHANGESTATUS em equipmentTransfer (query equipmentTransferId e statusId), handlers handleTrocaStatus e handleCancelar chamam POST /EquipmentTransfer/ChangeStatus, Toast e refresh da lista. Status resolvidos via formOptionsStatuses (GetFormOptions).
  Arquivos: ABPAC-FrontEnd/src/config/apiRoutes/equipmentTransfer.ts; ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/ModalTransferTecnicoList/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE
- [2026-03-10] Prote??o do Ve?culo - aviso quando h? equipamento em lan?amento ao salvar
  Titulo: Avisar e dar op??o de adicionar ou cancelar item em andamento ao clicar em Continuar
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Ao clicar em Continuar com o formul?rio "Novo Item de Prote??o" vis?vel e pelo menos um item j? adicionado, o sistema exibe modal informando que h? equipamento em lan?amento. Usu?rio pode "Adicionar antes" (fecha o modal e clica em Adicionar) ou "Cancelar lan?amento e salvar" (descarta o rascunho e salva apenas os itens j? adicionados).
  Arquivos: ABPAC-FrontEnd/src/components/local/PageAccession/VehicleManager/FormProtection/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE
- [2026-03-10] Transferencia de Unidade - corrigir dropdowns mobile das combos
  Titulo: Ajustar estilo e tamanho dos dropdowns das comboboxes em transf-unidade
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: O Select base passou a suportar dropdown customizado no mobile e modo compacto opcional. A tela transf-unidade ativou esse comportamento nas comboboxes da pagina, corrigindo o visual inconsistente do dropdown nativo e reduzindo um pouco a escala dos menus e itens.
  Arquivos: ABPAC-FrontEnd/src/components/ui/Inputs/Select/index.tsx; ABPAC-FrontEnd/src/components/ui/Inputs/Select/CustomSelect/index.tsx; ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/transfUnidade/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/04-planning-log.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE
- [2026-03-10] Transferencia de Unidade - responsividade mobile e botao da sidebar
  Titulo: Ajustar layout mobile de transf-unidade e ancorar o botao da sidebar no topo esquerdo
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: A tela transf-unidade passou a empilhar corretamente os campos de Localizar por no mobile, deixou os botoes de acao ocuparem a largura adequada em telas pequenas e reposicionou o botao recolhido da sidebar para o canto superior esquerdo com ancoragem fixa na viewport.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/transfUnidade/index.tsx; ABPAC-FrontEnd/src/components/ui/Navigation/SideMenu/sideMenu.module.scss; .cursor/memory/03-backlog.md; .cursor/memory/04-planning-log.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE
- [2026-03-10] Buscar Estoque - combo de unidade volta ao padrao visual dos inputs
  Titulo: Remover destaque extra da combobox de Unidade de Negocio no dark mode
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: A combobox de Unidade de Negocio em Buscar Estoque deixou de usar o modo de alto contraste aplicado anteriormente e voltou a seguir a mesma paleta visual dos demais inputs da tela no dark mode.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/04-planning-log.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE
- [2026-03-10] Buscar Estoque - contraste da combo de unidade no dark mode
  Titulo: Clarear os textos da combobox de Unidade de Negocio em dark mode
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: O Select buscavel ganhou um modo opcional de alto contraste para dark mode e essa configuracao foi aplicada apenas na combobox de Unidade de Negocio da tela Buscar Estoque, melhorando a leitura do valor selecionado e das opcoes do dropdown.
  Arquivos: ABPAC-FrontEnd/src/components/ui/Inputs/Select/index.tsx; ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/04-planning-log.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE
- [2026-03-10] Buscar Estoque - opcao explicita de unidade vazia
  Titulo: Adicionar Nenhuma opcao selecionada na combo de Unidade de Negocio
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: A combo de Unidade de Negocio em Buscar Estoque passou a exibir uma opcao explicita Nenhuma opcao selecionada, mapeada para o mesmo estado sem filtro de unidade ja usado pela listagem.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/04-planning-log.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE
- [2026-03-10] Buscar Estoque - combo Filtrar por via filters do contrato
  Titulo: Fazer a combo Filtrar por consumir filters de Equipment/GetGeneralStockSearchFormOptions
  Estado: Concluido
  Classificacao: CONTRACT_CONSUMPTION
  Ultima acao: A tela Buscar Estoque deixou de usar uma lista fixa para a combo Filtrar por e passou a preencher esse select com object.filters retornado por /Equipment/GetGeneralStockSearchFormOptions, mantendo fallback para variacao de casing da resposta.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/lista/index.tsx; .cursor/contracts/equipment-stock-search-form-options.contract.json; .cursor/memory/03-backlog.md; .cursor/memory/04-planning-log.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE
- [2026-03-10] Modal Transferencia de Unidade - igualar largura dos botoes de filtro
  Titulo: Ajustar tamanho do botao Filtrar para coincidir com Limpar filtros
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: O modal Transferencias de Unidade de Negocio passou a usar a mesma largura minima para os botoes Filtrar e Limpar filtros, igualando o tamanho visual entre as duas acoes.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/ModalUnitTransfer/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/04-planning-log.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE
- [2026-03-10] Transferencia de Unidade - corrigir fonte da combo Unidade destino
  Titulo: Fazer Unidade destino consumir managementBranches de EquipmentTransfer/GetFormOptions
  Estado: Concluido
  Classificacao: CONTRACT_CONSUMPTION
  Ultima acao: A tela transf-unidade deixou de reutilizar a lista operacional de unidades para o select Unidade destino e passou a preencher esse campo diretamente com managementBranches retornado por /EquipmentTransfer/GetFormOptions.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/transfUnidade/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/04-planning-log.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE
- [2026-03-10] Buscar Estoque - propagar unidade selecionada para telas de transferencia
  Titulo: Enviar managementAssociationBranchId para as telas de transferencia quando houver unidade selecionada
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: A unidade selecionada na combo de Buscar Estoque passou a ser propagada via query para as navegacoes de transferencia de unidade e transferencia de tecnico. Quando a combo esta vazia, nenhuma query de managementAssociationBranchId e enviada.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/lista/index.tsx; ABPAC-FrontEnd/src/pages/adm/estoque/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/04-planning-log.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE

- [2026-03-10] Buscar Estoque - unidade volta a ser filtro opcional
  Titulo: Remover obrigatoriedade de unidade na listagem Buscar Estoque
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Removido o bloqueio da tabela sem unidade selecionada. A tela voltou a exibir a listagem normalmente com os dados da associacao e agora so envia managementAssociationBranchId quando o usuario seleciona uma unidade na combo.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/04-planning-log.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE

- [2026-03-10] Estoque Lista - espacamento entre botoes da barra de acoes
  Titulo: Uniformizar espacamento entre grupos de botoes (TabNavigation x Transf. Unidade / Transf. Tecnico)
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Alterado o grupo dos botoes "Transf. Unidade" e "Transf. Tecnico" de gap-2 para gap-1 para igualar ao espacamento do TabNavigation (Buscar Estoque / Busca de equipamentos).
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-09] Buscar Estoque - remover label da combo de unidade
  Titulo: Simplificar a combobox de Unidade de Negocio
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Removida a label visivel da combobox de Unidade de Negocio na tela Buscar Estoque, mantendo apenas o placeholder e preservando o comportamento atual dos filtros e do estado vazio.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-09] Buscar Estoque - reposicionar combo de unidade ao lado do filtro
  Titulo: Ajustar layout dos filtros de Buscar Estoque
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: A combobox de Unidade de Negocio foi reposicionada para ficar ao lado esquerdo da combobox Filtrar por no desktop, mantendo empilhamento no mobile e preservando o comportamento do estado vazio.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-09] Buscar Estoque - estado vazio centralizado sem tabela
  Titulo: Centralizar orientacao e ocultar a tabela ate selecionar uma unidade
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: A tela Buscar Estoque deixou de renderizar a tabela quando nenhuma unidade de negocio esta selecionada e passou a exibir apenas uma mensagem centralizada orientando o usuario a selecionar uma unidade.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE

- [2026-03-09] Buscar Estoque - filtro por unidade de negocio e estado vazio orientado
  Titulo: Adicionar combobox de Unidade de Negocio na tela Buscar Estoque
  Estado: Concluido
  Classificacao: CONTRACT_CONSUMPTION
  Ultima acao: Consumidos os contratos de select de unidades e da busca paginada. A tela Buscar Estoque passou a carregar as unidades via /Equipment/GetManagementAssociationBranchSelectObject, enviar managementAssociationBranchId para /Equipment/GetGeneralStockPagedByFilter e renderizar uma linha orientativa no corpo da tabela quando nenhuma unidade estiver selecionada.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/buscaEstoque/lista/index.tsx; ABPAC-FrontEnd/src/config/apiRoutes/equipment.ts; .cursor/contracts/equipment-management-association-branch-select.contract.json; .cursor/contracts/equipment-stock-search-paged.contract.json; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE

- [2026-03-09] Equipamentos - payload com ManagementBranchId no save
  Titulo: Ajustar nome do atributo enviado no cadastro de equipamentos
  Estado: Concluido
  Classificacao: CONTRACT_CONSUMPTION
  Ultima acao: O payload de save das telas de adicionar e editar equipamento deixou de enviar managementAssociationBranchId e passou a enviar ManagementBranchId, mantendo o campo visual e a validacao local inalterados.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/equipamentos/adicionar/index.tsx; ABPAC-FrontEnd/src/pages/adm/equipamentos/editar/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE

- [2026-03-09] Equipamentos - campo obrigatorio de unidade de negocio no cadastro
  Titulo: Adicionar ManagementAssociationBranch no formulario de cadastro de equipamentos
  Estado: Concluido
  Classificacao: CONTRACT_CONSUMPTION
  Ultima acao: Consumido o contrato de Equipment/FormOptions para ler managementAssociationBranch, adicionado o campo obrigatorio managementAssociationBranchId nas telas de adicionar e editar equipamento, e redistribuida a ultima linha do formulario em 4 colunas iguais.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/equipamentos/adicionar/index.tsx; ABPAC-FrontEnd/src/pages/adm/equipamentos/editar/index.tsx; .cursor/contracts/equipment-form-options.contract.json; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md; .cursor/memory/09-done.md; .cursor/memory/10-checkpoint.md
  Responsavel: ROVIS_FE

- [2026-03-09] Ativar modo ROVIS-FE (nova solicitacao)
  Titulo: Ativacao operacional do modo ROVIS-FE com classificacao da tarefa
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Gate obrigatorio do FRONT confirmado (04-frontend, front-end/\*, 00-context); solicitacao classificada como FRONT_LOGIC; nao houve CONTRACT_CONSUMPTION, sem consumo de contrato e sem iniciar backend.
  Arquivos: .cursor/agents/08-rovis-fe.md; .cursor/agents/04-frontend.md; .cursor/agents/front-end/api-services.md; .cursor/agents/front-end/components-guide.md; .cursor/agents/front-end/form-validation.md; .cursor/agents/front-end/frontend-agent-core.md; .cursor/agents/front-end/page-patterns.md; .cursor/agents/front-end/styling-patterns.md; .cursor/memory/00-context.md; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-09] Adesao e Estoque - correcao nomenclatura categoryId protecoes
  Titulo: Corrigir uso incorreto do campo categoryId nas protecoes
  Estado: Concluido
  Classificacao: CONTRACT_CONSUMPTION
  Ultima acao: Corrigido uso do campo categoryId que estava sendo confundido. categoryId na protecao refere-se ao equipmentTypeId (tipo de equipamento), NAO a categoria do veiculo. Ajustado para passar formOptions.categories (lista de EquipmentType) ao inves de formOptions.equipments para o VehicleProtectionItemForm. Adicionados comentarios explicativos nas interfaces.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageAccession/VehicleManager/FormProtection/index.tsx; ABPAC-FrontEnd/src/components/local/PageAccession/VehicleManager/FormProtection/VehicleProtectionItemForm.tsx; ABPAC-FrontEnd/src/pages/adm/estoque/entrada/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-09] Adesao - alinhamento contrato de protecoes
  Titulo: Alinhar interface VehicleProtectionType com contrato do backend
  Estado: Concluido
  Classificacao: CONTRACT_CONSUMPTION
  Ultima acao: Adicionados campos maintenanceDate e associateRegistrationDraftVehicleId na interface VehicleProtectionType; Adicionado campo Data de Manutencao no FormProtection; Confirmado que o fluxo ja envia vehicleProtections[] no POST do veiculo e o backend preenche automaticamente o associateRegistrationDraftVehicleId.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageAccession/VehicleManager/FormProtection/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-09] Estoque visualizacao - campos de equipamento no modal de manutencao
  Titulo: Adicionar campos disabled com dados do equipamento no modal de manutencao
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Adicionados 4 campos disabled no modal de manutencao para exibir informacoes do equipamento selecionado: Tipo de Equipamento, Status do Equipamento, Numero de Serie, Fabricante. Permite consulta rapida durante cadastro de manutencao.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/entrada/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-09] Estoque visualizacao - refatoracao modal cadastro rapido
  Titulo: Refatorar modal de cadastro rapido para seguir padroes de design do FormProtection
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Refatorado modal completo usando componentes Form, SelectForm, TextInputForm, DateInputForm, InputMaskForm, Grid, FormSection; Integrado API_VEHICLE_PROTECTION.GETFORM() para buscar opcoes; Implementado VehicleProtectionItemForm para gerenciar items; Adicionado busca dinamica de cidades baseada no estado selecionado.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/entrada/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-09] Estoque visualizacao - cadastro rapido de protecao
  Titulo: Adicionar modal de cadastro rapido de protecao com SAVERANGE
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Removido botao "+ Historico"; botao "Cadastro Rapido" do topo passa a abrir modal com formulario completo de protecao (data, motivo, tecnico, instrucoes, contato, observacoes, items) enviando para API_VEHICLE_DRAFT.SAVERANGE.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/entrada/index.tsx; ABPAC-FrontEnd/src/config/apiRoutes/associateRegistrationDraftVehicle.ts; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-09] Estoque visualizacao - botao de manutencao
  Titulo: Substituir botao Cadastro (+) por Manutencao (icone de manutencao)
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Na tela `estoque/entrada`, os botoes com rotulo Cadastro foram alterados para Manutencao com icone `Wrench`, mantendo a abertura do modal generico de manutencao.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/entrada/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-09] Estoque - manutencao unificada na visualizacao
  Titulo: Remover modais por estado da lista e centralizar modal generico na tela de visualizacao
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Em `estoque/lista`, removidas as acoes/modais condicionais de Confirmar instalacao e Manutencao; em `estoque/entrada`, botao Cadastro do Historico passou a abrir modal unico de manutencao com tipos Remocao, Troca e Conserto, incluindo campos condicionais e validacoes.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/lista/index.tsx; ABPAC-FrontEnd/src/pages/adm/estoque/entrada/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-09] Ativar modo ROVIS-FE (solicitacao atual)
  Titulo: Ativacao operacional do modo ROVIS-FE com classificacao da tarefa
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Gate obrigatorio do FRONT confirmado (04-frontend, front-end/\*, 00-context); solicitacao classificada como FRONT_LOGIC; nao houve CONTRACT_CONSUMPTION, sem consumo de contrato e sem iniciar backend.
  Arquivos: .cursor/agents/08-rovis-fe.md; .cursor/agents/04-frontend.md; .cursor/agents/front-end/api-services.md; .cursor/agents/front-end/components-guide.md; .cursor/agents/front-end/form-validation.md; .cursor/agents/front-end/frontend-agent-core.md; .cursor/agents/front-end/page-patterns.md; .cursor/agents/front-end/styling-patterns.md; .cursor/memory/00-context.md; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-09] Modal Transfer?ncias de Unidade de Neg?cio: filtragem com payload initialDate/endDate (ISO) e filters.search (status), filters.page/pageSize (CONTRACT_CONSUMPTION / FRONT_LOGIC).
- [2026-03-06] Estoque - duas abas e lista Buscar Estoque: Abas "Busca de equipamentos" e "Buscar Estoque"; lista em buscaEstoque/lista com dataSearchStock (FRONT_LOGIC).

## Concluido

- [2026-03-09] Equipment - ChangeStatus para alterar status por equipmentId/statusId
  Titulo: Criar metodo ChangeStatus no repository para atualizar EquipmentStatusId e retornar Equipment
  Estado: Concluido
  Classificacao: feature
  Ultima acao: BACK adicionou ChangeStatusAsync em IEquipmentRepository/EquipmentRepository para atualizar o status do equipamento e retornar a entidade atualizada.
  Arquivos: ABPAC-BackEnd/AlavTech.Core/RepositoriesInterface/PgSql/IEquipmentRepository.cs; ABPAC-BackEnd/AlavTech.Infrastructure/RepositoriesImpl/PgSql/EquipmentRepository.cs; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_BE
- [2026-03-06] Estoque manutencao - campos condicionais por status
  Titulo: Renderizar campos do modal de manutencao conforme status selecionado
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Modal de manutencao em `estoque/lista` ajustado para regras por status: `consertado` exibe tecnico + data + descricao; `removido` sem campos adicionais; `trocado` exibe tecnico + data + motivo + descricao + dados do novo equipamento (tipo, fabricante, serial e etiqueta).
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-06] Estoque busca de equipamentos - acoes por status
  Titulo: Adicionar acoes Confirmar instalacao e Manutencao na listagem de estoque por status
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Na tela `estoque/lista` (aba Busca de equipamentos), actions agora exibem botao condicional de Confirmar instalacao para itens em estado de instalar/em estoque e botao de Manutencao para itens instalados. Implementado modal com dados da protecao de veiculo e campos operacionais (incluindo troca/manutencao).
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/lista/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-06] Estoque Localizar - filtros no padrao Adesao
  Titulo: Aplicar filtros por associado/status/placa/equipamento/fabricante/numero de serie com query no backend
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Tela `estoque/localizar` atualizada com barra de filtros no padrao da Adesao (campos locais + Buscar/Limpar), pagina??o server-side e envio de filtros por query string no endpoint paginado de VehicleProtection.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/localizar/index.tsx; ABPAC-FrontEnd/src/config/apiRoutes/vehicleProtection.ts; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-06] Estoque Localizar - indicador visual de Pr?-cadastro
  Titulo: Destacar itens de pr?-cadastro com badge, tooltip e realce de linha
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Na listagem `estoque/localizar`, a coluna de pr?-cadastro passou a exibir badge `P` com tooltip `Pr?-cadastro` para itens marcados, `-` para demais, e realce visual de linha (`bg-amber-50`) para registros de pr?-cadastro.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/localizar/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-06] Estoque - nova tela Localizar com mock dedicado
  Titulo: Criar tela de listagem da aba Localizar em Estoque com dados mockados
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Nova pagina `estoque/localizar` criada com `PrivatePageStructure + ListDefault` usando apenas `dataStock`; aba Localizar da tela `estoque/lista` passou a navegar para a nova rota, mantendo Busca de equipamentos com fluxo/API atuais.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/localizar/index.tsx; ABPAC-FrontEnd/src/pages/adm/estoque/lista/index.tsx; ABPAC-FrontEnd/src/routes/appRoutes.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-05] Ocorrencias - ajuste final do modal Selecao de Oficinas
  Titulo: Corrigir modal de oficinas com area vazia e alinhamento interno
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Modal `ModalQuickWorkshop` ajustado para layout fluido (`w-full`) com largura responsiva no `ModalGlobal`, sem wrapper interno fixo que causava espaco em branco; tabela com overflow horizontal controlado.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageOcurrencies/Tabs/Modals/ModalQuickWorkshop.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-05] Ocorrencias - refinamento visual dos modais (ModalGlobal)
  Titulo: Ajustar design dos modais de Ocorrencias apos migracao para ModalGlobal
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Melhorada proporcao dos modais com largura responsiva, altura maxima de viewport, paddings consistentes e wrappers fluidos; reduzido espaco vazio e melhorado scroll das listagens/tabelas em Processos Judiciais, Status e Causas.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageOcurrencies/Tabs/Modals/ModalJudicialProcess.tsx; ABPAC-FrontEnd/src/components/local/PageOcurrencies/Tabs/Modals/ModalQuickStatus.tsx; ABPAC-FrontEnd/src/components/local/PageOcurrencies/Tabs/Modals/ModalQuickCause.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-05] Ocorrencias - modais internos padronizados com ModalGlobal
  Titulo: Migrar modais da tela de Ocorrencias para o componente ModalGlobal
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Modais `ModalJudicialProcess`, `ModalQuickWorkshop`, `ModalQuickCause` e `ModalQuickStatus` foram alterados para usar `ModalGlobal`, mantendo fluxo atual e ajuste de largura por contexto via `modalClassName`.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageOcurrencies/Tabs/Modals/ModalJudicialProcess.tsx; ABPAC-FrontEnd/src/components/local/PageOcurrencies/Tabs/Modals/ModalQuickWorkshop.tsx; ABPAC-FrontEnd/src/components/local/PageOcurrencies/Tabs/Modals/ModalQuickCause.tsx; ABPAC-FrontEnd/src/components/local/PageOcurrencies/Tabs/Modals/ModalQuickStatus.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-05] Grid layout - breakpoints corrigidos para manter formato responsivo
  Titulo: Corrigir mapeamento de classes responsivas do componente Grid (sm/md/lg/xl)
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Corrigido bug no `Grid` onde `sm/md/lg/xl` aplicavam classe `xs`; agora cada breakpoint usa sua classe correta, restaurando o formato esperado em telas que dependem de colunas responsivas (incluindo TabEvento).
  Arquivos: ABPAC-FrontEnd/src/components/ui/Layout/Grid/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-05] Ocorrencias - TabEvento alinhado em grid no padrao de forms
  Titulo: Ajustar layout da aba de Evento para grid, seguindo padrao dos formularios do projeto
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Layout do TabEvento migrado para o componente `Grid` (container/itens) como nas demais telas, mantendo o mesmo formato visual da referencia anexada.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageOcurrencies/Tabs/TabEvento.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-05] Ocorrencias - TabEvento com selects Sim/N?o nos booleanos
  Titulo: Substituir radios booleanos por Select (Sim/N?o) na aba de Evento
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Campos `usedAssistance24h`, `isFatalVictim` e `isVehicleLoaded` foram convertidos de radios Sim/N?o para `Select` com opcoes fixas `{ label: Sim, value: true }` e `{ label: N?o, value: false }`, mantendo persistencia booleana no `editingEvent`.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageOcurrencies/Tabs/TabEvento.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-05] Assinaturas (Adesao) - aplicar tema escuro em Contrato e Ficha de Inscricao
  Titulo: Tema dark nas telas de assinatura do contrato de adesao e da ficha de inscricao
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Paginas `contrato_renderizado` e `ficha_inscricao/documentModel` atualizadas com tema escuro em paleta cinza neutra (sem azul), incluindo fundo, card, texto e containers de documento.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/adesao/contrato_renderizado/index.tsx; ABPAC-FrontEnd/src/pages/adm/adesao/contrato_renderizado/contrato_renderizado.module.scss; ABPAC-FrontEnd/src/pages/adm/adesao/ficha_inscricao/documentModel/index.tsx; ABPAC-FrontEnd/src/pages/adm/adesao/ficha_inscricao/documentModel/documentModel.module.scss; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-05] Adesao - so abrir aba Veiculos apos gerar ID do associado
  Titulo: Evitar troca para aba Veiculos antes de existir token do novo associado
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: No save de novo associado, a tela so navega para edicao quando retorna ID valido; checklist/aba de veiculos nao e mais acionado antes disso, evitando NaN no GETALL de veiculos.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageAccession/AccessionManager/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-05] Adesao veiculo - selecionar marca nao pode recarregar tela
  Titulo: Corrigir reload e perda da selecao de marca no cadastro de veiculos da adesao
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Removido loading global no fetch de modelos por marca (evita remount do formulario), aplicado loading local para modelo e blindagem no Select para nao submeter formulario ao clicar em opcoes.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageAccession/VehicleManager/FormVehicle/index.tsx; ABPAC-FrontEnd/src/components/ui/Inputs/Select/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-05] Estoque - Visualizar item abrindo na tab do equipamento selecionado
  Titulo: Ao visualizar item na lista de estoque, abrir a tela com a tab do equipamento correspondente ao item clicado
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Lista passou a enviar vehicleProtectionId na navegacao; tela de entrada identifica o item selecionado e define automaticamente Ativos/Inativos e o tipo de equipamento correto, mesmo com placas repetidas.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/lista/index.tsx; ABPAC-FrontEnd/src/pages/adm/estoque/entrada/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-05] Ativar modo ROVIS-FE (solicitacao do usuario)
  Titulo: Ativacao do modo ROVIS-FE com classificacao da tarefa e registro operacional
  Estado: Concluido
  Classificacao: FRONT_LOGIC
  Ultima acao: Gate FE carregado (04-frontend, front-end/\*, 00-context), tarefa classificada como FRONT_LOGIC, sem contrato para consumo e sem iniciar backend; registros atualizados em backlog e implementation-log.
  Arquivos: .cursor/agents/08-rovis-fe.md; .cursor/agents/04-frontend.md; .cursor/agents/front-end/api-services.md; .cursor/agents/front-end/components-guide.md; .cursor/agents/front-end/form-validation.md; .cursor/agents/front-end/frontend-agent-core.md; .cursor/agents/front-end/page-patterns.md; .cursor/agents/front-end/styling-patterns.md; .cursor/memory/00-context.md; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-03-02] Ficha de Inscricao - Logs do documento renderizado
  Titulo: Exibir listagem de logs (GetRenderedDocumentLogs) abaixo de Detalhes dos signatarios
  Estado: Concluido
  Classificacao: CONTRACT_CONSUMPTION + FRONT_LOGIC
  Ultima acao: Adicionada rota API_REGISTRATION_FORM.GETRENDEREDDOCUMENTLOGS; tipagem do log; SignatureActionsModal busca logs ao abrir e renderiza tabela de logs abaixo da tabela de signatarios.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageAccession/RegistrationFormManeger/SignatureActionsModal/index.tsx; ABPAC-FrontEnd/src/config/apiRoutes/registrationForm.ts; ABPAC-FrontEnd/src/types/api/RegistrationFormTypes.ts; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-02-26] Signatarios (Adesao) - Asterisco vermelho em todos os campos obrigatorios
  Titulo: Na tela Dados dos Signatarios (FormbuildAdhesion), todos os campos (Nome, CPF, Nascimento, E-mail, Whatsapp/Sms, Disparo) sao obrigatorios; exibir \* vermelho nos labels igual ao padrao Utilizador/outros formularios
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Substituidos labels raw por componente Label com required; asterisco vermelho via label.module.scss ($input-color-error-message).
  Arquivos: ABPAC-FrontEnd/src/components/local/PageAccession/AdhesionManeger/FormbuildAdhesion/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-02-26] Contrato renderizado - Estilizacao alinhada ? Ficha de Inscricao (documentModel)
  Titulo: Melhorar estilizacao da pagina contrato_renderizado para ficar igual/semelhante ? tela ficha_inscricao/documentModel
  Estado: Concluido
  Classificacao: VISUAL_ONLY
  Ultima acao: Criado SCSS module e layout com header (titulo + Voltar), card central, area do documento e botoes.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/adesao/contrato_renderizado/index.tsx; ABPAC-FrontEnd/src/pages/adm/adesao/contrato_renderizado/contrato_renderizado.module.scss; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-02-26] Adesao lista - Filtros (Nome/Status) mostrando opcoes de todas as paginas
  Titulo: Filtros da lista de Adesao devem exibir opcoes de todos os registros, nao apenas da primeira pagina
  Estado: Concluido
  Classificacao: bugfix (FRONT_LOGIC)
  Ultima acao: SecondListStructure/table: estado allRowsForFilterOptions + requisicao com pageSize 5000 ao montar; dropdowns usam essas linhas quando getListIsPagination + filter.
  Arquivos: ABPAC-FrontEnd/src/components/structure/SecondListStructure/table/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-02-25] Localizar - Prepare do associado na pagina Informacoes do Associado
  Titulo: Chamar prepare do associado na tela localizar/Associado quando id na URL
  Estado: Concluido
  Classificacao: bugfix
  Ultima acao: token passado ao AccessionManager com id da query (?id=); prepare() disparado conforme id.
  Arquivos: ABPAC-FrontEnd/src/pages/localizar/Associado/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-02-25] CRM - Dados do ve?culo n?o carregados ao editar (prepare)
  Titulo: Corrigir prepare do formul?rio de edi??o de ve?culo no CRM
  Estado: Concluido
  Classificacao: bugfix
  Ultima acao: Prop table passada do CrmFormPage para FormBuildVehicle; getData usa table?.rowData?.id ?? table?.id.
  Arquivos: ABPAC-FrontEnd/src/components/local/CrmFormPage/index.tsx; ABPAC-FrontEnd/src/components/local/CrmFormPage/FormBuildVehicle/index.tsx; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Responsavel: ROVIS_FE

- [2026-02-24] AssociateRegistrationDraftVehicle - retorno com AssociateRegistrationDraftVehicleReturnVO
  Titulo: Substituir VehicleReturnVO por AssociateRegistrationDraftVehicleReturnVO nos endpoints de draft vehicle
  Estado: Concluido
  Classificacao: feature
  Ultima acao: Novo VO criado e endpoints GetAll/GetAllByManagementAssociation retornam o novo tipo.
  Arquivos: ABPAC-BackEnd/AlavTech.Communication/ViewObjects/Vehicle/VehicleVO.cs; ABPAC-BackEnd/AlavTech.Core/Profiles/VehicleProfile.cs; ABPAC-BackEnd/AlavTech.Core/ServicesInterface/API/IAssociateRegistrationDraftVehicleService.cs; ABPAC-BackEnd/AlavTech.Infrastructure/ServicesImpl/API/AssociateRegistrationDraftVehicleService.cs; ABPAC-BackEnd/AlavTech.API/Controllers/AssociateRegistrationDraftVehicleController.cs; .cursor/contracts/associate-registration-draft-vehicle-get-all.contract.json; .cursor/contracts/associate-registration-draft-vehicle-get-all-by-management-association.contract.json
  Responsavel: ROVIS_BE

- [2026-02-24] AssociateRegistrationDraftServiceOrder/GetOptions - adicionar vehicleAmount
  Titulo: Retornar vehicleAmount no GetOptions de ServiceOrder
  Estado: Concluido
  Classificacao: feature
  Ultima acao: Campo vehicleAmount adicionado no OptionsVO e calculado via count de vehicles no latest draft (DisabledAt == null).
  Arquivos: ABPAC-BackEnd/AlavTech.Communication/ViewObjects/AssociateRegistrationDraftServiceOrder/AssociateRegistrationDraftServiceOrderVO.cs; ABPAC-BackEnd/AlavTech.Infrastructure/ServicesImpl/API/AssociateRegistrationDraftServiceOrderService.cs; .cursor/contracts/associate-registration-draft-service-order-get-options.contract.json
  Responsavel: ROVIS_BE

- [2026-02-20] Estoque - Prepare GetProtectionSummaryByVehicle na tela visualizar
  T?tulo: Na tela de visualiza??o de ve?culo do Estoque (/adm/estoque/visualizar/:id), implementar o prepare que busca os dados via GetProtectionSummaryByVehicle?vehicleId= e preenche Associado, Placa, Equipamento, Contratado (Ativos/Inativos) e ajustes de layout conforme Figma.
  Estado: Conclu?do
  Classifica??o: CONTRACT_CONSUMPTION / FRONT_LOGIC / VISUAL_ONLY
  ?ltima a??o: Criados tipos ProtectionSummaryByVehicleTypes; p?gina vizualizar com useParams(id), prepare via GetRequest(API_ASSOCIATE_REGISTRATION_DRAFT_VEHICLE.GETPROTECTIONSUMMARYBYVEHICLE), mapeamento object.associate.label, plates.join, category+year/yearModel, activeProtectionTypes.length/inactiveProtectionTypes.length; layout alinhado ao Figma (grid 7-3-2, Contratado row-span-2, bot?es "+ Cadastro"/"+ Hist?rico", tags pill).
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/vizualizar/index.tsx; ABPAC-FrontEnd/src/types/api/ProtectionSummaryByVehicleTypes.ts; .cursor/memory/03-backlog.md; .cursor/memory/06-implementation-log.md
  Respons?vel: ROVIS_FE
- [2026-02-20] Ades?o (O.S.) - Tela igual ? imagem no step Ades?o (O.S.)
  T?tulo: Na tela PageAccession, no step "Ades?o (O.S.)", exibir tela com Lista de equipamentos (Cat, Equipamento, Placa, Valor ades?o), se??o ISEN??O DE ADES?O (Motivo, Valor Ajustado), Total de ades?es, Respons?vel (com tooltip), bot?es Visualizar O.S. e Avan?ar. Dados de AccessionExemple (DataExemple).
  Estado: Conclu?do
  Classifica??o: VISUAL_ONLY / FRONT_LOGIC
  ?ltima a??o: Implementado conte?do do step 4 em PageAccession/index.tsx com tabela, isen??o, total, respons?vel (useUserContext), StyledTooltip, Button; estilos em associatedBuild.module.scss. Sem altera??o de outros componentes.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageAccession/index.tsx; ABPAC-FrontEnd/src/components/local/PageAccession/associatedBuild.module.scss
  Respons?vel: ROVIS_FE
- [2026-02-20] Ades?o - Listagem em ?rvore no AdhesionList (Contrato ades?o)
  T?tulo: Na tela PageAccession (Contrato ades?o), o componente AdhesionList exibe listagem em estilo de ?rvore (um n?vel): Equipamento expand?vel com Requerimento Ades?o (Editar, #, Data, Signat?rio, Sign. CPF, Status). Semelhante ? galeria de arquivos do associado, com um ?nico n?vel de expans?o.
  Estado: Conclu?do
  Classifica??o: VISUAL_ONLY / FRONT_LOGIC
  ?ltima a??o: Implementado AdhesionList com cabe?alho (Equipamento, Cat, Placa, Ben, L, B, Requerimento Ades?o), linhas expand?veis (ChevronDown/ChevronRight), sublinha com Editar, #, Data, Signat?rio, Sign. CPF, Status. Props token, getList (opcional), editPath. PageAccession passa token para AdhesionList.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageAccession/AdhesionManeger/AdhesionList/index.tsx; ABPAC-FrontEnd/src/components/local/PageAccession/index.tsx
  Respons?vel: ROVIS_FE
- [2026-02-19] Ades?o - bot?es Galeria/Cancelar/Salvar abaixo do t?tulo em mobile e tablet
  T?tulo: Na tela de Ades?o (Informa??es do Associado), em mobile e tablet os bot?es Galeria de Arquivos, Cancelar e Salvar devem ficar abaixo do t?tulo (em desktop permanecem ? direita).
  Estado: Conclu?do
  Classifica??o: VISUAL_ONLY
  ?ltima a??o: Layout do header em AccessionManager: flex-col + gap-4 quando screenWidth < 1024; em mobile/tablet Cancelar e Salvar em coluna com 100% de largura (cada um ocupa toda a linha); Flexbox com w-full quando em coluna.
  Arquivos: ABPAC-FrontEnd/src/components/local/PageAccession/AccessionManager/index.tsx
  Respons?vel: ROVIS_FE
- [2026-02-19] Ades?o mobile - bot?es Pr?-Cadastro/Lista/Kanban em coluna
  T?tulo: No m?dulo Ades?o, em mobile os 3 bot?es (Pr?-Cadastro, Lista, Kanban) estavam cortados; alterado para modo coluna no mobile ocupando a largura total da tela.
  Estado: Conclu?do
  Classifica??o: VISUAL_ONLY
  ?ltima a??o: Tabs passou a aceitar flexDirection; SecondListStructure passa "column" quando screenWidth < 768; estilos para bot?es full-width em coluna.
  Arquivos: ABPAC-FrontEnd/src/components/ui/Tabs/index.tsx; ABPAC-FrontEnd/src/components/ui/Tabs/tabs.module.scss; ABPAC-FrontEnd/src/components/structure/SecondListStructure/table/index.tsx
  Respons?vel: ROVIS_FE
- [2026-02-19] Tela Estoque - Busca de equipamentos
  T?tulo: Criar tela de Estoque baseada na lista CRM, com tabs (mocadas), apenas aba Busca de equipamentos funcional, dados de data.js, sem Transf. T?cnico e sem bloco Localizar por; busca padr?o do ListDefault.
  Estado: Conclu?do
  Classifica??o: VISUAL_ONLY / FRONT_LOGIC
  ?ltima a??o: P?gina estoque/lista criada com ListDefault, externalTable, TabNavigation, cards, coluna Status customizada; data.js com colunas ID, Ativa??o, Dias, Associado, Cat, Tipo, Placa, Fabricante, Equipamento, N. s?rie, Status; rota /adm/estoque/lista registrada.
  Arquivos: ABPAC-FrontEnd/src/pages/adm/estoque/lista/index.tsx; ABPAC-FrontEnd/src/pages/adm/estoque/data.js; ABPAC-FrontEnd/src/routes/appRoutes.tsx
  Respons?vel: ROVIS_FE
- [2026-02-16] Adicionar campo adhesionDaysLimit na modal EditAssociationModal
  T?tulo: Configurar intervalo permitido (em dias) para data de ades?o
  Estado: Concluido
  Classifica??o: FRONT_LOGIC
  ?ltima a??o: TextInputForm do type number adicionado, interface ManagementAssociationType criada, types importados e validados sem erros.
  Arquivos: ABPAC-FrontEnd/src/components/local/Modals/EditAssociationModal/EditAssociationModal.tsx; ABPAC-FrontEnd/src/types/api/ManagementTypes.ts
  Respons?vel: ROVIS_FE- [2026-02-13] Campos Renavan, Chassi e Ades?o (data) no formul?rio de ve?culo da ades?o (FormVehicle). Classifica??o: FRONT_LOGIC. Arquivo: ABPAC-FrontEnd/src/components/local/PageAccession/VehicleManager/FormVehicle/index.tsx.
- [2026-02-13] CRUD de Equipamentos
  T?tulo: Criar CRUD completo de Equipamentos (lista, adicionar, editar)
  Estado: Concluido
  Classifica??o: CONTRACT_CONSUMPTION
  ?ltima a??o: P?ginas criadas, rotas registradas, sem erros de lint.
  Arquivos: src/config/apiRoutes/equipment.ts; src/pages/adm/equipamentos/lista/index.tsx; src/pages/adm/equipamentos/adicionar/index.tsx; src/pages/adm/equipamentos/editar/index.tsx; src/routes/appRoutes.tsx
  Respons?vel: ROVIS_FE
