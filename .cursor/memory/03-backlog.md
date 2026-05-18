# Backlog

## Pendentes
- ...

## Planejando
- 2026-05-05: Sessao ROVIS-FE ativa - aguardando proxima demanda frontend para classificar como VISUAL_ONLY, FRONT_LOGIC ou CONTRACT_CONSUMPTION; sem backend nem alteracao de contrato nesta ativacao.
- 2026-04-06: Sessao ROVIS-FE ativa ï¿½ proxima demanda a classificar (VISUAL_ONLY / FRONT_LOGIC / CONTRACT_CONSUMPTION); sem backend nem alteracao de contrato no front.
- 2026-03-30: Bugfix backend produto (ajuste escopo) - garantir concordancia estrita no ProductSimple: tudo do SaveVO deve persistir em colunas/tabelas especificas (sem payload solto) e o Prepare deve retornar exatamente das mesmas origens, incluindo fluxo de deposito interno/externo sem descontinuidade.
- 2026-03-30: Bugfix backend produto - validar todos os fluxos/tabelas de caracteristicas (Product, ProductSimple, ProductCharacteristics, ProductSimpleData, ProductTax, ProductStock) e corrigir campos nao preenchidos no round-trip Save/Prepare.
- 2026-03-26: CONTRACT_CONSUMPTION + FRONT_LOGIC - /adm/produto/editar: corrigir consumo de `ProductSimple/FormOptions` para aceitar payload em `camelCase` (alÃ©m de `UPPERCASE`) e mapear aliases esperados pela tela (`groupOptions`/`typeOptions`), mantendo `productClassificationTemplate` para componente especÃ­fico de categoria.
- 2026-03-23: Bugfix ProductGenerics ListFrontVO - regularizar nomes de colunas em portugues e corrigir acentuacao das labels publicas (ex.: `Descricao` -> `DescriÃ¯Â¿Â½Ã¯Â¿Â½o`, `Descricao Complementar` -> `DescriÃ¯Â¿Â½Ã¯Â¿Â½o Complementar`) nas listas retornadas pela controller.
- 2026-03-23: FRONT_LOGIC + CONTRACT_CONSUMPTION - /adm/embalagenscodigosereferencias: substituir fluxo de fornecedor/produto por selects (`suppliers` de `/Product/GetFormOptions` + novo `/Product/GetProductsSO`) e alinhar payload do modal.
- 2026-03-23: FRONT_LOGIC + CONTRACT_CONSUMPTION - /adm/produto: carregar cards do dashboard via `GET /Product/GetDashboardCards` (totalProducts, lowStock, zeroStock, pendingPriceUpdates).
- 2026-03-23: FRONT_LOGIC - /adm/produto/editar (dados bÃ¡sicos): salvar/carregar fabricante nos campos `fabricatorId`, `fabricatorProductCode` e `fabricatorDescription`, usando fabricante/referÃªncia/descriÃ§Ã£o do fabricante da tela; remover duplicidade de `Cod.Fab.` e `Fabricante` no card de classificaÃ§Ã£o.
- 2026-03-23: FRONT_LOGIC - /adm/produto/editar: reforÃ§ar round-trip de `fabricatorId`/`fabricatorDescription`/`fabricatorProductCode` no load/save e ajustar grid do card de classificaÃ§Ã£o para 3 campos por linha.
- 2026-03-23: FRONT_LOGIC - /adm/produto/editar aba imagens: corrigir regra de imagem principal para respeitar `isPrimary=true` escolhido no switch (nÃ£o forÃ§ar primeira imagem), mantendo fallback na primeira apenas quando nenhuma estiver marcada.
- 2026-03-23: FRONT_LOGIC - /adm/produto/editar: adicionar loading estilizado para carregamento do PrepareSave e para persistÃªncia no salvar (overlay + estado de botÃ£o).
- 2026-03-23: FRONT_LOGIC - /adm/produto/editar aba observaÃ§Ãµes: vincular campo de observaÃ§Ã£o ao `notes` (carregar/salvar em `notes`), corrigindo binding que estava em `generalObservations`.
- 2026-03-23: VISUAL_ONLY - /adm/produto/editar aba variaÃ§Ãµes: padronizar select de variaÃ§Ã£o para usar o mesmo componente/estilizaÃ§Ã£o do select de fornecedores (`SelectForm` + `select-py`).
- 2026-03-23: VISUAL_ONLY - /adm/produto/editar: corrigir overlay de loading (prepare/save) para nÃ£o ficar atrÃ¡s de inputs/selects com z-index elevado, migrando para portal global.
- 2026-03-23: VISUAL_ONLY - /adm/gestaodeestoque: remover botÃ£o `Ver detalhes` do card expandido `Detalhes do lote`.
- 2026-03-23: VISUAL_ONLY - /adm/cest: substituir loading inline de NCM no select para usar componente padrÃ£o da aplicaÃ§Ã£o (`Spinner`) em vez de `SkeletonLoading`.
- 2026-03-23: FRONT_LOGIC - desativar rota `/adm/modelo` para nÃ£o abrir/redirecionar para pÃ¡gina de modelo.
 
 





- 2026-03-18: Bugfix Product Save - corrigir FK de `package_reference_id` para utilizar referÃ¯Â¿Â½ncia de `ProductPackageReferenceComplementaries` no fluxo de gravaÃ¯Â¿Â½Ã¯Â¿Â½o de produto (evitar violaÃ¯Â¿Â½Ã¯Â¿Â½o `FK_Products_ProductPackageReferences_package_reference_id`).
- 2026-03-13: Auditoria ROVIS-BE da sprint backend (arquivos alterados, backlog/logs, requisitos, convenÃ¯Â¿Â½Ã¯Â¿Â½es `var`, `try/catch`, mensagens constantes e aderÃ¯Â¿Â½ncia arquitetural)


## Contrato criado e pronto para backend`r`n- 2026-03-23: Product Save barcode validation - `product-save-barcode-validation-fix.contract.json` `r`n- 2026-03-23: ProductGenerics labels publicas - `product-generics.contract.json` v1.1
- 2026-03-23: Product Save/Update - `product-save-update-audit-image-fix.contract.json`
- MÃƒÂ³dulos: Fornecedores, Motivo de Acerto de Estoque, Tipo de CobranÃƒÂ§a, Tipo de Documento, ClassificaÃƒÂ§ÃƒÂ£o CP, ClassificaÃƒÂ§ÃƒÂ£o CR
- Menu: headerMenu (Save, GetById, GetMenusByUserAsync)
- Produto: FormOptions e ProductGenerics (GetTypesSelect + Save por TypeId)

## Em execucao`r`n- 2026-03-23: Bugfix Product Save - falso positivo de codigo de barras duplicado corrigido no backend e validado por build.`r`n- 2026-03-23: Bugfix ProductGenerics ListFrontVO - acentuacao de labels publicas no backend validada por contrato, com build parcial bloqueado por lock de DLL no ambiente.
- 2026-03-13: Auditoria ROVIS-BE da sprint backend (arquivos alterados, requisitos, contratos, convencoes e validacao tecnica)

## Concluido
- 2026-03-23: FRONT_LOGIC - rota `/adm/modelo` removida do roteador principal (`routes/index.tsx`), evitando abertura/redirect para a pÃ¡gina de modelo.
- 2026-03-23: VISUAL_ONLY - loading de NCM em /adm/cest padronizado com `Spinner` no campo do select, removendo uso de `SkeletonLoading` nesse ponto.
- 2026-03-23: VISUAL_ONLY - botÃƒÂ£o `Ver detalhes` removido do card `Detalhes do lote` em /adm/gestaodeestoque.
- 2026-03-23: VISUAL_ONLY - loading de /adm/produto/editar corrigido com overlay em portal (`document.body`) e z-index mÃƒÂ¡ximo, eliminando sobreposiÃƒÂ§ÃƒÂ£o de inputs/selects sobre a mÃƒÂ¡scara.
- 2026-03-23: VISUAL_ONLY - select de variaÃƒÂ§ÃƒÂ£o na aba VariaÃƒÂ§ÃƒÂµes padronizado para `SelectForm`, alinhado visualmente ao select de fornecedores e mantendo sincronismo com `selectedVariationIds`.
- 2026-03-23: FRONT_LOGIC - aba ObservaÃƒÂ§ÃƒÂµes de /adm/produto/editar corrigida para usar `notes` no editor, garantindo carregamento e persistÃƒÂªncia no campo de observaÃƒÂ§ÃƒÂ£o.
- 2026-03-23: FRONT_LOGIC - /adm/produto/editar com loading estilizado aplicado no PrepareSave e no Save (overlay com spinner/mensagem + botÃƒÂµes bloqueados + estado loading no botÃƒÂ£o de salvar).
- 2026-03-23: FRONT_LOGIC - normalizaÃƒÂ§ÃƒÂ£o de imagens no save de produto corrigida para preservar `isPrimary` vindo da UI; quando houver uma marcada no switch ela vira principal, e fallback para primeira sÃƒÂ³ ocorre sem marcaÃƒÂ§ÃƒÂ£o.
- 2026-03-23: FRONT_LOGIC - /adm/produto/editar com round-trip corrigido de `fabricatorId` (select fabricante), `fabricatorDescription` (descriÃƒÂ§ÃƒÂ£o do fabricante) e `fabricatorProductCode` (referÃƒÂªncia), alÃƒÂ©m de grid do card de classificaÃƒÂ§ÃƒÂ£o ajustado para 3 campos por linha.
- 2026-03-23: FRONT_LOGIC - /adm/produto/editar ajustado para persistir fabricante/referÃƒÂªncia/descriÃƒÂ§ÃƒÂ£o no trio `fabricatorId`/`fabricatorProductCode`/`fabricatorDescription` e remover os campos duplicados `Cod.Fab.` + `Fabricante` do card inferior.
- 2026-03-23: ProductGenerics ListFrontVO com labels publicas ajustadas apenas na apresentacao, mantendo propriedades e payload originais e corrigindo acentuacao para `DescriÃƒÂ§ÃƒÂ£o`, `DescriÃƒÂ§ÃƒÂ£o Complementar` e correlatos.
- 2026-03-23: Auditoria Save/Update de Product concluida com contrato gerado, round-trip de `section`/`maximumStock`, limpeza de imagens/fornecedores com lista vazia e migration para `image_data` em texto.
- Data de pagamento no ato do pagamento + ediÃƒÂ§ÃƒÂ£o em lote de datas (lista empresas rÃƒÂ¡pida)
- Parcelas de licenÃƒÂ§a conforme tipo de plano (mensal=1, trimestral=3, semestral=6, anual=12; vencimentos mensais)
- Definir escopo da solicitacao inicial (init.md)
- Backend: mÃƒÂ³dulos Fornecedores e GenericTypes (Motivo de Acerto, Tipo de CobranÃƒÂ§a, Tipo de Documento, ClassificaÃƒÂ§ÃƒÂ£o CP/CR)
- Menu: headerMenu (backend + frontend)
- Fix: GetById headerMenu/menuRolePermission e header no topo
- Remover breadcrumb (Adm > Dashboard)
- Controle de licenÃƒÂ§a por usuÃƒÂ¡rios (limite e janela)
- Bugfix NotifyExpiration: modal de aviso nao aparece com hasAccess=true e mensagem (FRONT_LOGIC)
- Bugfix logout: limpar chaves de aviso de licenca no storage

- Ativacao do modo ROVIS com gate obrigatorio de PM e registro em memory (.cursor)
- 2026-03-05: Ativacao do modo ROVIS na sessao atual com uso de .cursor, gate PM-first e logs em memory
- 2026-03-05: Bugfix build frontend - corrigidos 4 erros TypeScript e build validado
- 2026-03-05: Bugfix pagamento de licenÃ¯Â¿Â½a - pagamento unitÃ¯Â¿Â½rio nÃ¯Â¿Â½o reancora datas das demais parcelas
- 2026-03-05: Bugfix vencimento de parcelas - pagamento em atraso nao desloca vencimentos futuros
- 2026-03-05: Bugfix bloqueio x vigencia - inadimplencia priorizada sobre dias restantes
- 2026-03-05: Pacote multi-modulo - adiantamento de parcelas na licenca, recÃ¯Â¿Â½lculo de vigÃ¯Â¿Â½ncia por parcelas pagas, trava de criaÃ¯Â¿Â½Ã¯Â¿Â½o por limite de usuÃ¯Â¿Â½rios, correÃ¯Â¿Â½Ã¯Â¿Â½o de exclusÃ¯Â¿Â½o (fallback token/id) e labels CÃ¯Â¿Â½digo/DescriÃ¯Â¿Â½Ã¯Â¿Â½o em acerto CP/CR
- 2026-03-05: Hotfix UTF-8 no modal de licenÃ¯Â¿Â½a em /adm/empresa/lista + ajuste de strings em GenericTypeModuleForm
- 2026-03-05: Reativacao de governanca ROVIS na sessao (PM-first aprovado, uso de .cursor e registros em memory)
- 2026-03-05: Bugfix cadastro usuario - bloquear criacao ao atingir limite de usuarios da empresa e retornar mensagem de erro
- 2026-03-05: Ajuste regra de limite - cadastro com perfil Mind/Administrador ignora validacao por empresa
- 2026-03-05: Ajuste de labels nas 5 telas (acerto, tipo de cobranÃ¯Â¿Â½a, tipo de documento, classificaÃ¯Â¿Â½Ã¯Â¿Â½o contas a pagar e contas a receber) para Nome/DescriÃ¯Â¿Â½Ã¯Â¿Â½o
- 2026-03-05: Bugfix exclusao em acerto/generic type - usar id no delete em vez de token de modulo
- 2026-03-05: Bugfix exclusao generic type - separar campo da linha (id) e nome do query param (token)
- 2026-03-05: Front pagamento em lote de parcelas de licenca na tela de empresas com chamadas individuais e retorno consolidado
- 2026-03-05: Governanca anti-UTF8 drift no orquestrador + padronizacao de encoding no repositorio
- 2026-03-05: Bugfix UI parcelas - coluna de selecao por linha visivel no pagamento em lote

## Bloqueados
- ...
- 2026-03-05: Hotfix licenca - bloqueado cancelamento de parcelas e recalculo de vigencia pelo proximo vencimento em aberto
- 2026-03-05: Regra de atraso imediato quando dia de vencimento do periodo atual ja passou (sem empurrar para proximo periodo)
## Atualizacao 2026-03-09
- Planejando: Ativacao do modo ROVIS na sessao atual com PM-first e memoria obrigatoria.
- Concluido: Governanca de processo ativada (uso de .cursor + registros em memory).

## Atualizacao 2026-03-09
- Planejando: Bugfix limite de usuarios apos aumento de licenca (novo cadastro nao cria apos 2->3).

## Atualizacao 2026-03-09
- Concluido: Bugfix limite de usuarios apos aumento de licenca (CreateAgileCommonUser agora define EnterpriseSelected e evita falha por listas nulas).

## Atualizacao 2026-03-13
- Concluido: Auditoria ROVIS-BE da sprint backend (contratos de produto adicionados, correcao de CS0103, padronizacao sem var, reforco de autenticacao/summary no ProductGenericsController).
- 2026-03-13: Revisao completa de services para garantir try/catch em todos os metodos conforme padrao ROVIS-BE.
## Atualizacao 2026-03-13
- Contrato criado e pronto para backend: product-services-trycatch-hardening.contract.json
## Atualizacao 2026-03-13
- Concluido: revisao de services de produto para conformidade de try/catch (ProductService e ProductGenericsService).
- 2026-03-13: Simplificacao de ProductGenerics para endpoint unico Save com TypeId (remover saves tipados redundantes).

## Atualizacao 2026-03-13
- Concluido: ProductGenerics consolidado para endpoint unico Save(typeId), com remocao dos endpoints Save tipados no controller e contrato atualizado.

## Atualizacao 2026-03-13
- Concluido: Segregacao de catalogo fiscal de produto em entidade propria (ProductFiscalCatalog), removendo NCM/CEST/CST/ANP do fluxo GenericType.

## Atualizacao 2026-03-13
- Concluido: Estruturacao de controllers por modulo: Product (CRUD + FormOptions), ProductGenerics (catalogos gerais), ProductFiscal (catalogo fiscal + product taxes).

## Atualizacao 2026-03-13
- Concluido: Correcao de FK enterprise no Save de Product (validacao previa de EnterpriseId) + refactor para persistencia via ProductRepository com uso de AutoMapper.

## Atualizacao 2026-03-16
- Planejando: ProductComplementary backend (novas tabelas relacionadas ao produto para ICMS/Embalagem-NCM/CST PIS-COFINS/ANP, nova controller ProductComplementary com SO/Save/Update e migracao da busca NCM BrasilAPI).
- 2026-03-16: Contrato criado e pronto para backend: product-complementary.contract.json
## Atualizacao 2026-03-16
- Em execucao: Implementacao backend ProductComplementary conforme contrato (tabelas Product*Complementary, service/controller e migracao da busca NCM).
- Concluido: ProductComplementary backend entregue (SO/Save/Update por dominio, NCM BrasilAPI em ProductComplementary, NcmController removida).

## Atualizacao 2026-03-17
- Planejando: Refactor backend de ProductComplementary e Product(FormOptions) para aderencia total ao padrao do projeto (try/catch consistente por camada, uso de _mapper conforme referencias, simplificacao/normalizacao de controllers e servicos, e ajuste de contratos/retornos de FormOptions).
- Contrato criado e pronto para backend: product-form-options-extended.contract.json
- Contrato criado e pronto para backend: product-complementary-formoptions-unified.contract.json
- Em execucao: Refactor backend de ProductComplementary e Product(FormOptions) para padronizacao completa e validacao por contrato.

## Atualizacao 2026-03-17
- Concluido: Refactor backend ProductComplementary + Product FormOptions com padronizacao arquitetural, contratos de FormOptions atualizados e validacao de build (sem erros de codigo).

## Atualizacao 2026-03-18
- Contrato criado e pronto para backend: product-save-package-reference-fk-fix.contract.json
- Em execucao: Bugfix Product Save FK package_reference_id (resolver referencia via ProductPackageReferenceComplementaries e eliminar violacao de FK no save/update).
## Atualizacao 2026-03-18
- Concluido: Bugfix save/update de produto para `package_reference_id` com validacao em `ProductPackageReferenceComplementaries` e troca do relacionamento FK (Product -> ProductPackageReferenceComplementaries).
- Em handoff: migration `20260318113000_UseComplementaryPackageReferenceFk` criada para aplicar no banco e remover dependencia de `ProductPackageReferences`.

## Atualizacao 2026-03-19
- Planejando: Refactor backend de Product Fiscal/FormOptions para normalizar labels de CFOP no SO (evitar duplicidade codigo - codigo - descricao) e consolidar aderencia ao padrao arquitetural do projeto nas implementacoes recentes de produto.
## Atualizacao 2026-03-19
- Contrato criado e pronto para backend: product-fiscal-catalog.contract.json (v1.1) com endpoints CFOP (GetCfopSO/GetCfopListFront) e regra de normalizacao de label.
- Em execucao: Refactor backend Product Fiscal/FormOptions conforme contrato atualizado (try/catch e padrao de mapeamento).
## Atualizacao 2026-03-19
- Concluido: Refactor backend Product Fiscal/FormOptions conforme contrato product-fiscal-catalog.contract.json v1.1, com normalizacao de label CFOP no SO e inclusao de CFOP no FormOptions de Produto.
- Em handoff: contratos e endpoints de CFOP prontos para consumo do frontend (sem execucao de front-end).
## Atualizacao 2026-03-19
- Concluido: Novo endpoint geral sem parametros para estoque+lote em ListFrontVO (Product/PrepareStockLotAll), mantendo campos de lote com Visible.False via ProductStockLotPrepareVO.

## Atualizacao 2026-03-19
- Concluido: Endpoint Product/GetListFront criado com retorno ListFrontVO para grid de produtos (Descricao, Codigo, Unidade, Preco, Estoque) e campos extras ocultos para resumo do produto.

## Atualizacao 2026-03-19
- Planejando: Produtos - exportar PDF/CSV, importar CSV para cadastro, prepare completo para edicao e unificacao Save como upsert por Id (removendo endpoint Update).

## Atualizacao 2026-03-19
- Contrato criado e pronto para backend: product-import-export-upsert.contract.json (export PDF/CSV, import CSV, PrepareSave completo e Save upsert por Id com remocao de Update no controller).
- Em execucao: Implementacao backend Product conforme contrato product-import-export-upsert.contract.json.

## Atualizacao 2026-03-19
- Concluido: Product com exportacao PDF/CSV, importacao CSV, PrepareSave completo e Save upsert por Id (endpoint Update removido do ProductController).
- Em handoff: contrato product-import-export-upsert.contract.json pronto para consumo do front.

## Atualizacao 2026-03-19
- Planejando: Product Save/PrepareSave completo para cobrir todos os campos faltantes do formulario (base, caracteristicas, fornecedores, variacoes, estoque inicial, tributacao detalhada, formacao de preco e historicos de compra/venda), com persistencia em tabelas correspondentes e retorno para edicao.
## Atualizacao 2026-03-19
- Contrato criado e pronto para backend: product-save-prepare-complete.contract.json (varredura de duplicidades e modelagem final sem redundancia de tabelas).
- Em execucao: Product Save/PrepareSave com suporte a multiplas imagens, fornecedores multiplos e variacoes, mantendo compatibilidade com payload legado.
## Atualizacao 2026-03-19
- Concluido: Product Save/PrepareSave ampliado com persistencia estruturada para imagens (ProductImages), variacoes (ProductVariations/ProductVariationOptions) e retorno completo de listas no PrepareSave.
- Em handoff: migration nao gerada (sera criada manualmente) para novas tabelas e relacionamentos.
## Atualizacao 2026-03-19
- Em execucao: fechamento do round-trip completo dos campos restantes do formulario de produto via ProductSaveVO/ProductTaxSaveVO + ExtraPayloadJson tipado no PrepareSave/Save.
## Atualizacao 2026-03-19
- Concluido: todos os campos informados pelo usuario passaram a ser persistidos e reidratados no backend, usando colunas/tabelas existentes quando ha estrutura dedicada e ExtraPayloadJson para os demais campos sem coluna propria.
## Atualizacao 2026-03-19
- Planejando: Refactor arquitetural de ProductService para reduzir metodos complementares, reforcar try/catch na camada de servico e migrar mapeamentos manuais para _mapper/Profiles conforme padrao do projeto.
- [2026-03-19 ROVIS-BE][BACK] ProductService aderente ao padrÃ¯Â¿Â½o do projeto: payload JSON extraÃ¯Â¿Â½do para helper dedicado, mapeamentos centrais movidos para ProductProfile e PrepareSave/BuildProductReturn simplificados com _mapper.

- 2026-03-20: Product cadastro/edicao - confrontar destrinchamento FE x backend atual (Save/Prepare/FormOptions), listar gaps de contrato, naming e payload sem alterar codigo. [Planejando]

- 2026-03-20: Ajuste de escopo Product - aliquotas e variacoes migradas para cadastros/tabelas proprias com vinculo por id no produto; fornecedores mantem fluxo hibrido. [Planejando]
## Atualizacao 2026-03-20
- Contrato criado e pronto para backend: product-save-prepare-structured-relations.contract.json
- Em execucao: alinhamento arquitetural de Product para subrecursos de aliquota e variacao com nomenclatura oficial do front.
- [x] BACK 2026-03-20 18: Implementado backend de produto com subrecursos ProductAliquot e ProductVariation, ajuste de PrepareSave/GetFormOptions/Save com nomenclatura oficial do front e enterpriseId vindo do payload. Validado em Core e Infrastructure; API bloqueada apenas por DLLs em uso no IIS Express/Visual Studio.

- [x] BACK 2026-03-20 19: Ajustado contrato publico de Product para expor os nomes pedidos pelo front sem substituir campos legados; incluidos heavyProduct, productValidityDays, reightFree, 	axReplacementCons, 	axReplacementContr, exemptPisCofins, itemTypePisCofins e endpoint GetUfSO para SO de UFs. Build validado em Core e Infrastructure.

- [x] BACK 2026-03-20 20: Product Save/PrepareSave/FormOptions alinhados para fluxo sem variacoes inline no save principal; incluidos wrappers ListFrontVO para fornecedores/aliquotas/variacoes no PrepareSave, SO de UF mantido no formOptions de produto e tipos de variacao expostos como tipos oficiais do dominio. Campos novos preparados para migration manual: heavy_product, product_validity_days, reight_free, 	ax_replacement_contr, 	ax_replacement_cons, exempt_pis_cofins, item_type_pis_cofins.

## Atualizacao 2026-03-23
- Planejando: ativacao da governanca ROVIS na sessao atual com uso obrigatorio de .cursor, gate PM-first e registro continuo em memory.
- Concluido: governanca ROVIS ativada na sessao atual (2026-03-23) com orientacao de sempre passar pelo Product Manager antes de qualquer execucao tecnica.

## Atualizacao 2026-03-23
- Planejando: Bugfix frontend no fluxo de cancelar em produtos (criar/editar) para evitar erro ao retornar para listagem.
- Aguardando aprovacao: ajustar navegacao de cancelamento e alinhar rota de listagem de produtos para nao cair em ErrorPage.

## Atualizacao 2026-03-23
- Em execucao: bugfix de navegacao do Cancelar em criar/editar produto para evitar erro ao retornar para listagem.
- Concluido: fluxo de cancelamento ajustado (add -> /adm/produto) e rota alias /estoque/produtos criada para compatibilidade.

## Atualizacao 2026-03-23
- Planejando: bugfix visual na tela de editar produto (barra de abas com quebra/sobreposicao de textos longos).
- Aguardando aprovacao: ajustar layout das abas para leitura limpa e responsiva.

## Atualizacao 2026-03-23
- Planejando: bugfix no editar produto para restaurar funcionamento dos botoes Voltar e Avancar entre abas.
- Aguardando aprovacao: conectar callbacks onBack/onNext das etapas ao controle real de ctiveTab.

## Atualizacao 2026-03-23
- Em execucao: bugfix dos botoes Voltar/Avancar no editar produto com navegacao por ordem de abas.
- Concluido: callbacks de etapas conectados ao ctiveTab; Voltar/Avancar agora trocam de aba corretamente.

## Atualizacao 2026-03-23
- Planejando: fluxo de adicionar produto com reaproveitamento opcional do item selecionado na listagem (modal Sim/Nao).
- Aguardando aprovacao: abrir modal ao clicar em adicionar com item selecionado, carregar PrepareSave do produto selecionado e iniciar cadastro pre-preenchido quando confirmado.

## Atualizacao 2026-03-23
- Em execucao: feature de adicionar produto com modal Sim/Nao para reutilizar item selecionado na listagem.
- Concluido: modal implementado; opcao Sim carrega template via PrepareSave e abre cadastro pre-preenchido; opcao Nao abre cadastro normal.

## 2026-03-23 - Prefill completo do cadastrar por PrepareSave
- Melhorar fluxo de clonagem no "Novo produto" para preencher o maximo de campos possiveis com base no produto selecionado da lista.
- Incluir mapeamento ampliado de aliases (codeId->sku, barcode->ean, unitMeasure->unit, productType->productType/type etc.), tributacao (productTax), listas (ufRates, lots, suppliers, variacoes) e historico.
- Garantir que etapa de imagens suporte dados ja existentes vindos do template (base64/url) alem de arquivos locais.
## Atualizacao 2026-03-23
- Concluido: refino estrutural de ProductService para reduzir codigo manual, reaproveitar AutoMapper/StaticMethods e alinhar Prepare/PrepareSave/Save/Update no mesmo round-trip completo de payload extra e fornecedor principal.
- Validado: build de Core, Infrastructure e API sem erros de codigo apos o refactor; warnings legados do repositorio permanecem fora deste escopo.
- Concluido: `Lots` removido do fluxo efetivo de Save/Update principal; o backend passa a ignorar qualquer lote no payload e manter apenas a vinculacao automatica.
- Em execucao: fechamento 100% do round-trip de Product no retorno final, expandindo ProductReturnVO para expor os mesmos campos extras aceitos no save e ja persistidos em ExtraPayloadJson.
- Concluido: otimizaÃ¯Â¿Â½Ã¯Â¿Â½o do tempo de save de Product com reducÃ¯Â¿Â½o de round-trips no backend, consolidando persistÃ¯Â¿Â½ncia complementar em um Ã¯Â¿Â½nico SaveChanges e removendo consultas por item em fornecedores e lote automÃ¯Â¿Â½tico.
- 2026-03-23: Product GetFormOptions passou a expor `freightTypes` e `fuelPercentageOptions`, cobrindo `freightType`, `glpPetroleumPerc`, `naturalGasPerc` e `glpImportedPerc` sem options inline no front. [Concluido]

## 2026-03-23 - Corrigir payload de save (criar e editar produto)
- Problema: save estava perdendo campos no service e quebrando consistencia entre editar/criar.
- Necessidade: enviar payload completo (root + productTax + colecoes) preservando campos do Prepare/formulario com aliases corretos.

## Atualizacao 2026-03-23
- Concluido: bugfix complementar no save de produto (criar/editar) para nao perder campos alterados no formulario.
- Concluido: editar agora mescla corretamente campos tributarios em raiz para productTax e preserva colecoes no payload final (ufRates, lots, productSuppliers, variations).

## Atualizacao 2026-03-23
- Concluido: regra de nome do produto ajustada no editar para priorizar description (nome oficial) em vez de 
ame no payload de save.
- 2026-03-23: ProductGenerics com superficie publica traduzida para o front, ajustando labels de colunas e nomes de grupos/tabelas para portugues sem alterar tokens, rotas e propriedades internas. [Concluido]
- 2026-03-23: ProductGenerics com grade do front padronizada para priorizar `Id`, `Name` e `Description`, ocultando `typeId`, `genericToken` e colunas tecnicas nas listas consumidas pelo front. [Concluido]

## Atualizacao 2026-03-23
- Planejando: Product edit/save - auditar campos enviados pelo front que nao persistem no backend e ajustar validacao fiscal para permitir edicao mesmo com observacao de origem/tipo item/CSTs obrigatorios.

## Atualizacao 2026-03-23
- Em execucao: Product edit/save com foco em persistencia completa das propriedades recebidas do front e desbloqueio da edicao fiscal sem regressao no create.
- Concluido: payload de edicao passou a aceitar e preservar listas do front (`Lots`, `ProductSuppliers`, `ProductAliquots`, `ProductVariations`) no contrato de request.
- Concluido: validacao fiscal obrigatoria (origem/tipo item/CSTs) ficou restrita ao create; na edicao o fluxo permite salvar sem bloquear por `ErrorTaxDataInvalid`.
- Concluido: normalizacao de save deixou de sobrescrever lotes recebidos (`model.Lots ??=`), eliminando perda silenciosa de dados.
- Concluido: correcao complementar de duplicidade falsa em barcode/codeId mantida no repositorio (catch nao retorna mais duplicidade).

## Atualizacao 2026-03-23
- Concluido: adicionado endpoint backend para retorno de produtos em formato SelectObject (`GET /Product/GetProductsSO`) com filtro por permissao do usuario.
- Validado: fluxo de save e filtro de barcode permanecem conforme ajuste anterior (sem falso positivo por excecao tecnica no repositorio).

## Atualizacao 2026-03-23
- Em execucao: correcao de persistencia campo-a-campo no Product/Save apos divergencia entre payload enviado e retorno salvo (descricao, grupo/categoria e espelhos de payload).
- Concluido: prioridade de persistencia ajustada para campos principais (`description`, `group`, `barcode`) evitando sobrescrita por espelhos (`descriptionLong`, `category`, `gtin`).
- Concluido: campos espelho de cadastro (`descriptionLong`, `category`, `gtin`, `manageStock`, `currentStock`, `minimumStock`, `minStock`, `termSalePrice`) passaram a ser persistidos e reaplicados via ExtraPayloadJson no round-trip.

## Atualizacao 2026-03-23
- Concluido: pipeline de save endurecido para persistencia por propriedade homonima, sem sobrescrita cruzada entre campos espelho (descriptionLong/category/gtin) e campos principais (description/group/barcode).

## Atualizacao 2026-03-23
- Concluido: ListFrontVO de produtos ajustado para exibir `SKU` no lugar de `Codigo` no cabecalho da coluna de identificador comercial.
- [x] 2026-03-23 14:32 - Product ListFrontVO: coluna 'Codigo' alterada para 'SKU' (sem alteraÃ¯Â¿Â½Ã¯Â¿Â½o de payload/propriedade).
- [x] 2026-03-23 15:02 - Produto: criado endpoint GET /Product/GetDashboardCards para cards da listagem (total, estoque baixo, zerados, pendentes=0).
- [x] 2026-03-23 15:18 - Varredura ListFrontVO (produto): normalizada acentuaÃƒÂ§ÃƒÂ£o dos headers (DescriÃƒÂ§ÃƒÂ£o, PreÃƒÂ§o, CÃƒÂ³digo, FabricaÃƒÂ§ÃƒÂ£o, MÃƒÂ­nima/MÃƒÂ¡xima, ReferÃƒÂªncia).
- [x] 2026-03-23 15:47 - Produto: criado SetActive (ativa/desativa via is_active) e aplicado filtro global para nÃƒÂ£o retornar produtos inativos (is_active=false).
## Atualizacao 2026-03-23
- Concluido: ajuste no Save de produto para normalizar `ImageData` (remove prefixo `data:image/...;base64,`) antes da persistencia, reduzindo falhas quando o front envia imagem em data URL.
## Atualizacao 2026-03-23
- Concluido: save de imagens do produto corrigido para respeitar `isPrimary` enviado pelo front (sem auto-marcar primeira), garantir no maximo uma imagem primaria e evitar regravar/desabilitar imagens quando o conjunto recebido for identico ao ja salvo.

## Atualizacao 2026-03-24
- Planejando: Product cadastro simples backend - criar novos metodos `PrepareSave` e `Save` para fluxo simplificado de produto, salvando apenas propriedades do escopo informado (independente dos nomes/agrupamentos do front), com campos obrigatorios fora do escopo aceitos como nullable para reduzir friccao no cadastro inicial.
- Aguardando aprovacao: seguir para ARCH gerar contrato dedicado (endpoint, request/response e regras de validacao) antes da implementacao backend.
## Atualizacao 2026-03-24
- Contrato criado e pronto para backend: product-simple-save-prepare.contract.json
- Em execucao: implementacao backend do fluxo simples de produto (service/controler/VO dedicados), sem iniciar frontend.
## Atualizacao 2026-03-24
- Em handoff: contrato `product-simple-save-prepare.contract.json` e endpoints backend `ProductSimple/PrepareSave` + `ProductSimple/Save` prontos para consumo do front (sem iniciar frontend).
- Concluido: implementacao backend do fluxo simples de produto com service/controller/VO dedicados e DI registrada, mantendo fluxo legado de `Product` inalterado.
## Atualizacao 2026-03-24
- Planejando: ProductSimple FormOptions backend - adicionar endpoint de opcoes para cadastro simples de produto com os selects solicitados (unidade, tipo produto, tipo producao, categoria, secao, marca, IAT, frete gratis, deposito, produto pesado, grupo ICMS, CFOP, CSOSN, NCM, CST entradas e CST saidas).
- Aguardando aprovacao: seguir para ARCH gerar contrato de `ProductSimple/GetFormOptions` antes da implementacao backend.
## Atualizacao 2026-03-24
- Concluido: ProductSimple recebeu endpoint `GET /ProductSimple/FormOptions` com payload enxuto para cadastro simples (unidade, tipo produto, tipo producao, categoria, secao, marca, IAT, frete gratis, deposito, produto pesado, grupo ICMS, CFOP, CSOSN, NCM, CST entradas e CST saidas).
- Concluido: contrato dedicado criado em `.cursor/contracts/product-simple-form-options.contract.json`.
## Atualizacao 2026-03-24
- Concluido: ProductSimple atualizado para novo escopo de cadastro (incluindo `createdAt/updatedAt` no retorno, `freightType`, suporte a dois codigos de barras via `barcode` + `gtinTax`, mantendo `gtin`), sem migration de banco.
- Concluido: novo endpoint `GET /ProductSimple/SearchByBarcode` com busca cruzada entre base local e API externa `api-produtos.seunegocionanuvem.com.br`.
- Concluido: `GET /ProductSimple/FormOptions` ficou sem parametros e retorna todas as opcoes necessarias para criacao no fluxo simples.
## Atualizacao 2026-03-24
- Concluido: ProductSimple/Save passou a usar o mesmo fluxo de persistencia de imagens do Product normal (normalizacao de base64, garantia de imagem primaria unica e comparacao de conjunto para evitar regravacao desnecessaria).
## Atualizacao 2026-03-24
- Concluido: ProductSimple Save/FormOptions mapeados para bloco de Status e controle (Ativo, Controla Estoque, Fundo Combate a Pobreza, Usa Lote).
## Atualizacao 2026-03-24
- Concluido: ProductSimple persistencia revisada para reduzir extra_payload_json: maximumStock agora salvo no estoque e 	ermSalePrice salvo em coluna de preco do produto.

## Atualizacao 2026-03-24
- Em execucao: retirada definitiva de dependencia de `extra_payload_json` para os fluxos `Product` e `ProductSimple`, com persistencia via colunas proprias e nova estrutura de caracteristicas por chave (`ProductCharacteristics`).
- Concluido: servicos `ProductService` e `ProductSimpleService` estabilizados para salvar/ler payload expandido sem usar JSON livre em `products`/`product_taxes`.
- Concluido: validacao de build da solucao `PrisBackEnd.sln` sem erros de compilacao (warnings legados permanecem fora do escopo desta entrega).
- Em handoff: pronto para migration manual de schema e publicacao.

## Atualizacao 2026-03-24
- Aprovado e executado: remocao das tabelas `ProductSimilarLinks` e `ProductCommercialHistories` do mapeamento EF (sem alterar contratos de `Product` e `ProductSimple`).
- Concluido: entidades/configuracoes removidas e `ApplicationDbContext` ajustado para nao mapear mais essas tabelas.
- Validado: build da solucao sem erros de compilacao.
- Em handoff: migration manual liberada para dropar as duas tabelas no banco.

## Atualizacao 2026-03-24
- Concluido: validacao dos endpoints de produto (`Product/Save`, `Product/PrepareSave`, `ProductSimple/Save`, `ProductSimple/PrepareSave`) apos migration local; build da solucao sem erros.
- Concluido: novo requisito de classificacao em 3 niveis adicionado aos contratos e payload de produto: `mainType`, `specializedType`, `realType`.
- Concluido: mapeamento aplicado para `Product` e `ProductSimple` em save/prepare/return usando o mesmo fluxo de payload/caracteristicas.

## Atualizacao 2026-03-24
- Concluido: tipos `mainType/specializedType/realType` removidos do fluxo de persistencia e contrato de `Product` normal.
- Concluido: no `ProductSimple`, os 3 niveis agora sao carregados somente em `FormOptions` via template JSON em `API/Content/Template`.
- Concluido: criado template de classificacao em `Content/Template/ProductSimpleClassificationTemplate.json` para escolha pelo usuario (sem cadastro desses tipos pelo save).
- Validado: build da solucao sem erros.

## Atualizacao 2026-03-24
- Concluido: template de classificacao 3 niveis do ProductSimple expandido com estrutura ampla (multiplas categorias principais, especializadas e tipos reais).
- Concluido: mantido comportamento de retorno em `ProductSimple/FormOptions` sem persistencia no save e sem impacto no fluxo do `Product` normal.

## Atualizacao 2026-03-25
- Contrato criado e pronto para backend: product-simple-classification-hierarchy.contract.json
- Concluido: classificacao 3 niveis do ProductSimple migrada para persistencia em banco (tabelas dedicadas + controller/service para save/update/formoptions/hierarchy).
- Concluido: ProductSimple Save/PrepareSave/FormOptions integrados com typeMainId/typeSpecializedId/typeRealId.
- Concluido: Product/GetListFront passou a retornar propriedades de imagem (imagePreview) e imageId oculto para grid.
- Em handoff: migration manual liberada para criar ProductSimpleClassifications e ProductSimpleProductClassifications.

- 2026-03-25: ProductSimple/Save ajustado para aceitar typeMain/typeSpecialized/typeReal e criar automaticamente os 3 niveis por nome (hierarquia 1->2->3), preenchendo ids internamente.
- 2026-03-25: Reversao aplicada no ProductSimple/Save; hierarquia por nome movida para ProductSimpleClassification/Save e metodo BindProduct adicionado por id de classificacao.
## Atualizacao 2026-03-25
- Concluido: ProductSimple alinhado com campos fiscais da tela para evitar erro de cadastro no backend (`cstPisEntry`, `cstPisExit`, `cstCofinsEntry`, `cstCofinsExit`, `exemptPisCofins`, `itemTypePisCofins`, `irPerc`, `socialContribPerc`, `otherOutExpensesPerc`, `importRate`, `benefitCode`) em save/prepare.
- Concluido: ProductSimple/FormOptions expandido com opcoes especificas de PIS/COFINS (`taxListTypeOptions`, `exemptPisCofinsOptions`, `cstPisEntryOptions`, `cstPisExitOptions`, `cstCofinsEntryOptions`, `cstCofinsExitOptions`).
- Concluido: bug de listagem corrigido removendo imagem do `ProductListFrontVO` e do mapeamento de `ProductService/GetListFrontAsync`.
- Validado: build de Communication/Core/Infrastructure sem erros (API com lock de DLL por IIS Express no ambiente).
## Atualizacao 2026-03-25
- Concluido: ProductSimple/FormOptions corrigido para evitar arrays vazios em `cestOptions` com fallback de busca via `ProductService.GetFormOptions` (enterprise selecionada e fallback sem enterprise).
- Concluido: `productClassifications` e `productClassificationTemplate` agora nao filtram apenas `isActive=true`; retornam classificacoes nao desabilitadas para refletir os dados cadastrados/migrados.
## Atualizacao 2026-03-25
- Concluido: `ProductListFrontVO` recebeu coluna `Status` visivel no grid de produtos.
- Concluido: regra de status aplicada no backend da listagem: `Zerado` quando estoque <= 0, `Baixo` quando estoque <= minimo e minimo > 0, `Em estoque` nos demais casos.
- Concluido: exportacao CSV da listagem de produtos passou a incluir a coluna `Status`.
## Atualizacao 2026-03-25
- Concluido: regra de busca do ProductSimple restaurada conforme definido: `IsActive = true` e `DisabledAt == null` no `PrepareSave` e na busca de escrita.
- Validado: `PrepareSave` continua validando permissao por empresa apos encontrar produto; quando nao encontra mesmo ativo, principal causa passa a ser falta de acesso da empresa no contexto do usuario.
## Atualizacao 2026-03-25
- Concluido: removida regra de permissao por empresa no ProductSimple (sem bloqueio por EnterpriseSelected/EnterpriseIds).
- Concluido: PrepareSave/Save/SearchByBarcode do ProductSimple nao restringem mais por empresa do usuario.
## Atualizacao 2026-03-25
- Concluido: regra de permissao por empresa restaurada no ProductSimple.
- Concluido: adicionado diagnostico de indisponibilidade no PrepareSave/Save de ProductSimple para diferenciar produto inativo/desabilitado de nao encontrado.
## Atualizacao 2026-03-25
- Concluido: ProductSimple/PrepareSave agora retorna detalhe tecnico da excecao junto da mensagem de preparo para diagnostico rapido.
- Concluido: MapToPrepareAsync blindado para nao quebrar quando consulta de classificacao simples falhar; segue retornando produto sem bloquear o fluxo.
## Atualizacao 2026-03-25
- Concluido: corrigida falha de AutoMapper no PrepareSave do ProductSimple (membro Tax) removendo mapeamento Product->ProductSimplePrepareVO nesse fluxo.
- Concluido: datas CreatedAt/UpdatedAt no prepare agora sao preenchidas manualmente via StaticMethods (`ToDateHourFormat`).
## Atualizacao 2026-03-25
- Concluido: removido retorno detalhado de excecao em ProductSimple/PrepareSave; mensagem voltou ao padrao curto de projeto.
## Atualizacao 2026-03-26
- Concluido: `ProductSimpleService.SaveAsync` refatorado para fluxo linear no padrao do `ProductService` (sem `ExecutionStrategy + BeginTransactionAsync` explicitos), eliminando ponto de falha no retorno final do save.
- Concluido: removido uso de `var` em `ProductSimpleService` e `ProductSimpleClassificationService`.
- Concluido: `ProductSimpleClassificationService` alinhado com padrao de mapeamento via AutoMapper (`Profile` dedicado + `_mapper`) e blindagem de metodos privados com `try/catch`.
- Em validacao funcional: reteste de `ProductSimple/Save` com payload de atualizacao para confirmar fim do erro generico de save.
- 2026-03-26: ProductSimple/Save classificacao desacoplada de query direta na service; validacao e vinculo de classificacao migrados para repositorio dedicado, mantendo fluxo de save.

- [x] ProductSimple: mover fluxo de classificaï¿½ï¿½o para repositï¿½rio e corrigir falha no replace do vï¿½nculo ativo em duas etapas (disable -> save -> insert -> save).

- [x] ProductSimpleService: remover queries diretas de classificacao simples (ProductSimpleClassifications/ProductSimpleProductClassifications) e usar repository dedicado.

- [~] ProductSimpleService repository-only: fase 1 concluida (save do produto, autorizacao, productType, produto por id). Pendentes: estoques/lotes/tax/supplier/imagens/characteristics/list/search.

## Atualizacao 2026-03-27
- Planejando: ProductSimple Save/Prepare/ListFrontVO - incluir DIFAL (nullable) com estrutura origin/destination/interstateTaxRate/internalTaxRate, incluir CBS/IBS em ProductTax, garantir retorno com SalePrice/CostPrice/WholesalePrice/MinimumWholesaleQuantity/Commission e ocultar ProductStock no ListFrontVO com Visible.False.
- Aguardando aprovacao: seguir para ARCH gerar contrato antes da implementacao backend e migration.

## Atualizacao 2026-03-27
- Ajuste solicitado: incluir campo `aplicacao` no escopo do produto (save/prepare/return) junto com DIFAL + CBS/IBS.
- Migration sera gerada pelo usuario; backend deve entregar codigo e mapeamento prontos.

## Atualizacao 2026-03-27
- Ajuste solicitado: incluir endpoint backend na controller para calcular DIFAL (request/response dedicados) sem depender do save.

## Atualizacao 2026-03-27
- Ajuste solicitado: definir local dos campos DIFAL e persistir tambem o valor calculado em coluna dedicada no banco (alem dos campos de entrada da DIFAL).

## Atualizacao 2026-03-27
- Contrato criado e pronto para backend: `product-simple-save-prepare.contract.json` v1.1.0 (DIFAL com valor calculado em coluna propria, CBS/IBS, aplicacao, endpoint ProductSimple/CalculateDifal, ListFrontVO com campos de stock ocultos).
- Em execucao: implementacao backend conforme contrato v1.1.0 (sem iniciar frontend).

## Atualizacao 2026-03-27
- Concluido: ProductSimple e Product alinhados ao contrato v1.1.0 com persistencia dedicada para `application`, `minimum_wholesale_quantity`, `cbs`, `ibs` e DIFAL (`difal_origin`, `difal_destination`, `difal_interstate_tax_rate`, `difal_internal_tax_rate`, `difal_calculated_value`).
- Concluido: endpoint `POST /ProductSimple/CalculateDifal` implementado para simulacao/calculo de DIFAL na controller.
- Concluido: `Product/GetListFront` passou a retornar campos de ProductStock ocultos (`Visible.False`) no `ProductListFrontVO`.
- Em handoff: migration ficara a cargo do usuario, conforme combinado.

## Atualizacao 2026-03-27
- Planejando: refactor backend de produto para mover queries de services para repositories, ampliar uso de AutoMapper/Profile e padronizar datas de retorno em PT-BR via StaticMethods.
- Planejando: auditoria de tabelas do dominio de produto para identificar mapeamentos potencialmente sem uso efetivo.

## Atualizacao 2026-03-27
- Ajuste solicitado: validar campos de preco em tabelas existentes; somente criar ProductPrice se nao houver cobertura atual; preencher historico em ProductPriceHistories no backend; mover 100% das queries das services para repositories; reforcar try/catch em metodos e evitar proliferacao de metodos private complementares.
- Aguardando aprovacao: seguir para ARCH com plano revisado passo a passo e validacao incremental por etapa.

## Atualizacao 2026-03-27
- Ajuste solicitado (escopo final): criar tabela nova ProductPrice para centralizar campos de preco, manter auto preenchimento de historicos (ProductPriceHistories e ProductStockMovements) no fluxo de produto, e adicionar campo de origem propria no produto (distinta da origem do DIFAL).
- Aguardando aprovacao: seguir para ARCH com contrato atualizado e plano de implementacao incremental.

## Atualizacao 2026-03-27
- Ajuste solicitado: no escopo de ProductSimple, a origem do produto deve usar padrao fixo (0 Nacional, 1 Estrangeira importacao direta, 2 Estrangeira mercado interno) e ser exposta em FormOptions de ProductSimple junto das demais opcoes.

## Atualizacao 2026-03-27
- Contrato criado e pronto para backend: product-simple-save-prepare.contract.json v1.2.0 (origin do produto 0/1/2 + originOptions em FormOptions + ProductPrice + historicos automaticos ProductPriceHistories/ProductStockMovements + regra repository-only no ProductSimple).
- Em execucao: implementacao backend ProductSimple conforme contrato v1.2.0.

## Atualizacao 2026-03-27
- Concluido: ProductSimple refatorado para repository-only (sem query direta em ProductSimpleService), com try/catch preservado e ajuste de origem de produto (0/1/2) separada de origem DIFAL.
- Concluido: ProductSimple/FormOptions passou a retornar originOptions (Nacional, Estrangeira importacao direta, Estrangeira mercado interno).
- Concluido: estrutura de preco dedicada ProductPrice adicionada (entidade/config/contexto/relacao 1:1 com Product).
- Concluido: historicos automaticos no fluxo ProductSimple: ProductPriceHistories no Save e ProductStockMovements no Save/StockSaveLot.
- Em handoff: migration manual de banco necessaria para tabela product_prices e coluna origin em products (conforme combinado).
## Atualizacao 2026-03-27
- Concluido: ProductSimple/Tax alinhado com nomenclatura solicitada para taxas CST no payload publico (`cstPisEntryTaxRate`, `cstPisExitTaxRate`, `cstCofinsEntryTaxRate`, `cstCofinsExitTaxRate`) sem criar colunas duplicadas.
- Concluido: mapeamento backend mantido para colunas existentes de ProductTax (`pis_entry_rate`, `pis_exit_rate`, `cofins_entry_rate`, `cofins_exit_rate`), com round-trip em Save/Prepare.
- Concluido: validacao de build executada em Infrastructure e API com 0 erros.
## Atualizacao 2026-03-27
- Em execucao: hardening final de ProductSimple para coluna estrita e eficiencia de persistencia (repository batch/no-autosave).
- Concluido: campos de coluna propria do ProductSimple agora sem fallback em payload no retorno (application/origin/minimumWholesaleQuantity e precos/taxas dedicadas).
- Concluido: guard-rail automatizado adicionado via teste de arquitetura para impedir regressao de `_db`/`ApplicationDbContext` no ProductSimpleService.
- Validado: ProductSimpleService continua repository-only e sem query direta na service.
## Atualizacao 2026-03-27
- Concluido: ProductSimple migrado para persistencia 100% coluna/tabela fisica no fluxo simples (sem ProductCharacteristics/ProductPayloadJsonHelper), com `ProductSimpleData` para campos antes legados em payload.
- Concluido: Save/Prepare/Return/Barcode ajustados para ler e gravar via `Product`, `ProductPrice`, `ProductTax` e `ProductSimpleData`.
- Concluido: `ProductRepository` atualizado com `GetSimpleDataByProductIdAsync`, `UpsertSimpleDataAsync`, `SearchByBarcodeCandidatesWithSimpleDataAsync`, include de `SimpleData` e update completo de `ProductTax` (incluindo `group_icms_contr`, `cfop_contr`, `cbs`, `ibs`, `difal_*`).
- Concluido: guard-rail arquitetural ampliado para bloquear regressao de payload/characteristics no `ProductSimpleService`.

## Atualizacao 2026-03-27
- Concluido (ProductSimple/Estoque): implementado modelo de deposito com tabela dedicada `ProductWarehouses` (nome unico por empresa), associacao de estoque por `warehouse_id` + `location` + `lot_id` e propagacao de deposito em movimentacoes.
- Concluido (Contrato): `ProductSimpleSaveVO` e `ProductSimpleStockLotSaveVO` agora suportam `warehouseId` e `productLocationStock`; retornos de estoque/prepare incluem `warehouseId`, `warehouseName` e `productLocationStock`.
- Concluido (API): novo endpoint `POST /ProductSimple/CreateWarehouse` para cadastro de deposito por empresa logada.
- Concluido (Regras): no Save/SaveStockLot, deposito/localizacao sao resolvidos automaticamente (`DEPOSITO_GERAL`/`PADRAO`) quando nao informados; reuso de lote por combinacao produto+deposito+localizacao+validade.
- Concluido (Repository-only): fluxo ProductSimple mantido sem acesso direto a `_db` na service; consultas concentradas no repositorio.
- Pendente usuario: gerar/aplicar migration manual para novas estruturas/colunas.
## Atualizacao 2026-03-30
- Planejando: ProductSimple PrepareSave/Save hardening completo para round-trip total campo a campo (sem front-end), com mapeamento blindado de propriedades, revisao de tabelas/colunas ativas, validacao de nulidade e retorno completo para consumo do front.
- Aguardando aprovacao: seguir para ARCH gerar contrato incremental antes da implementacao backend.
## Atualizacao 2026-03-30
- Contrato criado e pronto para backend: product-simple-save-prepare.contract.json v1.3.0 (matriz campo->tabela/coluna, fallback estruturado e regra de round-trip estrito no PrepareSave/SaveReturn).
- Em execucao: implementacao backend de hardening ProductSimple conforme contrato v1.3.0 (sem iniciar frontend).
## Atualizacao 2026-03-30
- Concluido: hardening backend de ProductSimple/PrepareSave e ProductSimple/Save (retorno) com fallback estruturado por tabela/coluna, cobrindo Product, ProductPrice, ProductSimpleData, ProductTax, ProductStock, ProductSupplySourceLink e ProductImage.
- Concluido: normalizacao de shape de resposta para garantir objetos/listas obrigatorios (	ax, 	ax.difal, images, productVariationIds) e campos de classificacao/tipo sem omissao silenciosa.
- Em handoff: contrato product-simple-save-prepare.contract.json v1.3.0 pronto para consumo do frontend (sem iniciar frontend).



## Atualizacao 2026-03-30
- Contrato criado e pronto para backend: `product-simple-save-prepare.contract.json` v1.3.1 (concordancia estrita Save->persistencia fisica e Prepare->mesma origem, incluindo deposito interno/externo).
- Em execucao: ajuste de consistencia final do ProductSimple para garantir continuidade de dados entre Save/Prepare/StockSaveLot/CreateWarehouse.
- Concluido: ProductSimple com hardening de concordancia Save/Prepare em tabelas fisicas, incluindo normalizacao de deposito/localizacao no save e limpeza consistente de vinculos de fornecedor/classificacao quando nao enviados.
- Validado: build de Core e Infrastructure com 0 erros; API validada por `dotnet build /t:Compile` com 0 erros (build completo bloqueado localmente por lock de DLL em IIS Express/Visual Studio).
- Em handoff: pronto para reteste funcional de round-trip campo a campo no cadastro simples de produto (sem iniciar frontend).

## Atualizacao 2026-03-30
- Planejando: Bugfix backend ProductSimple/PrepareSave orientado por payload real do usuario; validar lacunas de mapeamento em ProductCharacteristics e corrigir round-trip dos campos ausentes/nulos no retorno.
- Aguardando aprovacao: seguir para ARCH gerar contrato incremental antes da implementacao backend.

## Atualizacao 2026-03-30
- Contrato criado e pronto para backend: `product-simple-save-prepare.contract.json` v1.3.2.
- Escopo ARCH desta iteracao: compatibilidade legada no `PrepareSave` com fallback de leitura em `ProductCharacteristics` (scope `product`/`tax`) quando colunas dedicadas vierem nulas.
- Em execucao: implementacao backend para eliminar lacunas de mapeamento apontadas no objeto real de `ProductSimple/PrepareSave`.

## Atualizacao 2026-03-30
- Em execucao: ProductSimple/PrepareSave com fallback legado de `ProductCharacteristics` para campos ausentes em colunas dedicadas (escopo `product`/`tax`), conforme contrato v1.3.2.
- Concluido: mapeamento de retorno reforcado para preencher campos nulos indevidos no objeto de produto simples usando leitura de caracteristicas legadas quando necessario.
- Validado: build de `PrisBackEnd.Infrastructure` e compilacao da `PrisBackEnd.API` (target `Compile`) sem erros de codigo.

## Atualizacao 2026-03-31
- Planejando: ativacao do modo ROVIS-BE na sessao atual com foco backend, sem iniciar frontend, e suporte de contrato para envio de objeto de save de Fabricante (`POST /ProductGenerics/Save`).
- Aguardando aprovacao: seguir para ARCH somente se houver solicitacao de alteracao de contrato; caso contrario, manter suporte de consumo do contrato vigente.

## Atualizacao 2026-03-31
- Planejando: bugfix backend no ListFrontVO de Fabricante para manter fidelidade do cadastro, exibindo colunas `codigo` e `nome` (substituindo a exibicao atual baseada em `descricao`), sem iniciar frontend.
- Aguardando aprovacao: seguir para ARCH gerar contrato incremental e depois BACK implementar/validar.

## Atualizacao 2026-03-31
- Ajuste solicitado: colunas da aba Fabricante devem seguir gramatica pt-BR com acentuacao correta, usando exatamente `Cï¿½digo` e `Nome`.
- Aguardando aprovacao: seguir para ARCH com contrato incremental incluindo labels publicas acentuadas.

## Atualizacao 2026-03-31
- Contrato criado e pronto para backend: `product-generics.contract.json` v1.2.
- Escopo ARCH desta iteracao: aba Fabricante (`GET /ProductGenerics/GetManufacturerListFront`) com colunas publicas `Cï¿½digo` e `Nome`, priorizando fidelidade ao campo `name` salvo.
- Em execucao: implementacao backend para isolar ajuste no token `PRODUTO_FABRICANTE` sem regressao nas demais abas.

## Atualizacao 2026-03-31
- Em execucao: ajuste backend da aba Fabricante para colunas publicas `Cï¿½digo` e `Nome` no ListFrontVO, isolado por token `PRODUTO_FABRICANTE`.
- Concluido: `ProductGenericsService` atualizado para exibir apenas `id/name` em Fabricante, com relabel de `id` para `Cï¿½digo` e preservacao de `name` como `Nome`.
- Validado: build de `PrisBackEnd.Infrastructure` com 0 erros; build de `PrisBackEnd.API` bloqueado por lock de DLL no ambiente (IIS Express/Visual Studio), sem erro funcional de compilacao do ajuste.
- Em handoff: contrato `product-generics.contract.json` v1.2 pronto para consumo do front (sem iniciar frontend).

## Atualizacao 2026-03-31
- Em execucao: hotfix backend no `GetManufacturerListFront` para quando nao houver linhas de fabricante retornar colunas padrao em vez de `columns: []`.
- Concluido: fallback de lista vazia da aba Fabricante passou a montar `ListFrontVO` com colunas normalizadas `Cï¿½digo` e `Nome`, eliminando retorno vazio de colunas.
- Validado: build de Infrastructure com 0 erros; build da API segue bloqueado por lock de DLL no ambiente (IIS Express/Visual Studio).

## Atualizacao 2026-03-31
- Em execucao: ajuste complementar no backend de Fabricante para impedir fallback de `Descriï¿½ï¿½o` quando o endpoint retorna `rows` vazio com `columns` vazio.
- Concluido: `GetListByTabAsync` agora sempre normaliza colunas por aba antes de retornar; para Fabricante, quando nao houver colunas no payload, injeta colunas padrao `Cï¿½digo` e `Nome`.
- Validado: build de `PrisBackEnd.Infrastructure` com 0 erros apos hotfix.
- Em handoff: pronto para reteste do endpoint `GetManufacturerListFront` com lista vazia e lista com registros.

## Atualizacao 2026-03-31
- Planejando: aplicar na aba Marca o mesmo padrao de Fabricante para ListFrontVO, exibindo somente `Cï¿½digo` (id) e `Nome`, inclusive quando a lista estiver vazia.
- Concluido: regra backend de colunas por aba expandida para `PRODUTO_MARCA` com fallback de colunas explicitas no estado vazio.
- Concluido: contrato `product-generics.contract.json` atualizado para v1.3 com especificacao de Marca (`GetBrandListFront`).
- Em handoff: pronto para reteste de Marca com e sem registros.

## Atualizacao 2026-03-31
- Planejando: ajuste da aba Grupo ICMS para exibir layout dedicado com `Cï¿½digo`, `Nome`, `ICMS/SERVIï¿½O`, `Tipo`, `Alï¿½quota (%)`, `CST` (cï¿½digo + label do select) e `Grupo Usado no ECF`.
- Concluido: implementado no backend o layout dedicado da aba `PRODUCT_ICMS_GROUP_COMPLEMENTARIES`, com fallback de colunas tambï¿½m no estado vazio.
- Concluido: regra de `CST` normalizada para retorno no formato cï¿½digo + label equivalente do select quando disponï¿½vel.
- Contrato atualizado para v1.4 contemplando `GetIcmsGroupListFront`.

## Atualizacao 2026-03-31
- Refinamento solicitado no Grupo ICMS: padronizacao dos dados em caixa alta, `Grupo Usado no ECF` textual (`SIM`/`Nï¿½O`), `ICMS/SERVIï¿½O` com descricao completa e `Tipo` com descricao (sem ID).
- Concluido: backend ajustado para transformar valores textuais do retorno da aba Grupo ICMS para maiusculas e mapear `ICMS/SERVIï¿½O`/`Tipo` por label de select.
- Concluido: campo exibido em `Grupo Usado no ECF` passou para valor textual via coluna dedicada (`descriptionTwo`) com `SIM`/`Nï¿½O`.
- Contrato atualizado para v1.5.

## Atualizacao 2026-03-31
- Validado: nao havia metodo de delecao/inativacao para Grupo ICMS no modulo `ProductComplementary` (existiam apenas Save/Update/GetSO).
- Concluido: criado endpoint backend `POST /ProductComplementary/DisableIcmsGroup` com soft delete (`DisabledAt`) por `id`.
- Concluido: contrato `product-complementary.contract.json` atualizado para v1.1 com novo endpoint `DisableIcmsGroup`.

## Atualizacao 2026-03-31
- Ajuste de padronizacao solicitado: coluna de Grupo ICMS renomeada para `Icms / Serviï¿½o` (substituindo `ICMS/SERVIï¿½O`) mantendo o mesmo campo `icmsOrService`.
- Concluido: label atualizado no backend e no fallback de lista vazia para manter consistencia visual.

## Atualizacao 2026-03-31
- Planejando: padronizacao da aba Unidade de Medida (LVO) para expor `Cï¿½digo`, `Nome` e `Sigla` em substituicao ao comportamento atual com `Descriï¿½ï¿½o`.
- Concluido: regra dedicada de colunas no backend para `PRODUTO_UNIDADE_MEDIDA`, com fallback explicito no estado vazio e labels pt-BR (`Cï¿½digo`, `Nome`, `Sigla`).
- Concluido: contrato `product-generics.contract.json` atualizado para v1.6 com endpoint `GetUnitMeasureListFront` e mapeamento de campos (`id`, `name`, `description`).

## Atualizacao 2026-03-31
- Planejando: ajuste da aba Embalagens/Referencias (LVO) para padrao completo de colunas e dados (`Cï¿½digo`, `Nome`, `Fornecedor`, `Produto`, `Cï¿½digo de barras`, `Quantidade`, `Sigla`) inclusive em lista vazia.
- Concluido: retorno da aba `GetPackageReferenceListFront` passou a usar fonte matriz unica (`ProductPackageReferenceComplementaries`) para eliminar quadruplicacao por mistura de origens.
- Concluido: criado fluxo de inativacao de embalagem/referencia (`DisablePackageReference`) e adicionada protecao anti-duplicidade no save/update da tabela complementar.
- Concluido: contratos atualizados (`product-generics` v1.7 e `product-complementary` v1.2).

## Atualizacao 2026-03-31
- Correcao solicitada: Unidade de Medida estava retornando itens acima do banco por merge indevido com opcoes complementares (incluindo referencias de produto).
- Concluido: aba Unidade de Medida voltou a usar fonte unica `ProductTypes` (token `PRODUTO_UNIDADE_MEDIDA`), sem merge de complementares.
- Contrato atualizado para v1.8 com regra explicita de single source para Unidade de Medida.

## Atualizacao 2026-03-31
- Ajuste solicitado: lista de CEST deve substituir `Id` por `Cï¿½digo` e incluir colunas `Nome`, `Descriï¿½ï¿½o`, `CEST` e `NCM`.
- Concluido: criada regra dedicada para aba CEST no `ProductGenericsService`, com fallback explicito das 5 colunas no estado vazio.
- Contrato `product-generics.contract.json` atualizado para v1.9 com especificacao de `GetCestListFront`.

## Atualizacao 2026-03-31
- Planejando: separar NCM externo (BrasilAPI) de NCM manual no `ProductComplementary`, com novos endpoints `NCMManualyListFrontVO`, `NCMManualyPrepare` e `NCMManualyDelete`.
- Concluido: `SearchNcmBrasilApi` passou a retornar `ListFrontVO` com colunas `Cï¿½digo`, `Nome`, `Tipo do Ato`, `Nï¿½mero do Ato`, `Ano do Ato` e `Descriï¿½ï¿½o`, alimentado somente pela BrasilAPI.
- Concluido: `NCMManualyListFrontVO` implementado com retorno manual nas colunas `Cï¿½digo`, `Nome`, `CST PIS/COFINS`, `Natureza da Receita`, `Alï¿½quota PIS`, `Alï¿½quota COFINS`, `IBPT Nacional`, `IBPT Importado`.
- Concluido: adicionados `NCMManualyPrepare` e `NCMManualyDelete` (soft delete) com filtro exclusivo para registros manuais (`ProductId == null`).
- Contrato atualizado para `product-complementary.contract.json` v1.3.

## Atualizacao 2026-03-31
- Ajuste solicitado: nos dois ListFrontVO de NCM, renomear coluna `Cï¿½digo` para `Cï¿½digo NCM`.
- Concluido: labels atualizados em `NcmBrasilApiListFrontItemVO` e `NcmManualyListFrontItemVO`.
- Contrato alinhado com a nova nomenclatura de coluna.

## Atualizacao 2026-03-31
- Planejando: padronizar todos os retornos de NCM (formOptions, produto simples e produto comum) para o formato ${codigoNCM} - .
- Concluido: GetNcmComplementarySOAsync, SearchNcmBrasilApiSOAsync e fallback NCM de ProductFiscalCatalogService alinhados no mesmo formato de label.
- Validado: build de PrisBackEnd.Infrastructure com 0 erros.

## Atualizacao 2026-03-31
- Planejando: ajustar GetCstPisCofinsListFront para retornar colunas Cï¿½digo CST, Nome e Cï¿½digo Tipo de Crï¿½dito.
- Concluido: aba PRODUCT_CST_PIS_COFINS_COMPLEMENTARIES com colunas dedicadas e fallback de lista vazia no novo padrao.
- Concluido: criado delete (soft delete) de CST PIS/COFINS complementar via DisableCstPisCofins.
- Validado: build de Infrastructure e compile da API com 0 erros.

## Atualizacao 2026-03-31
- Planejando: padronizar GetAnpListFront para Cï¿½digo ANP, Nome e Grupo.
- Concluido: aba ANP (COMPLEMENTAR_GRUPOS_ANP_COMBUSTIVEIS) com colunas dedicadas e fallback de lista vazia no novo padrao.
- Concluido: criado delete (soft delete) para ANP via DisableAnpCode.
- Validado: build de Infrastructure com 0 erros; compile da API bloqueado por lock de DLL (PrisBackEnd.Communication.dll, processo VBCSCompiler).

## Atualizacao 2026-03-31
- Planejando: criar endpoint GetSectionListFront no ProductGenericsController e padronizar retorno da aba Seï¿½ï¿½o para Cï¿½digo, Nome e Comissï¿½o.
- Concluido: endpoint GetSectionListFront implementado e apontando para o token PRODUTO_SECAO.
- Concluido: normalizacao de colunas da aba Seï¿½ï¿½o no backend para id, 
ame, alue com labels Cï¿½digo, Nome, Comissï¿½o (inclusive lista vazia).
- Validado: build de Infrastructure e compile da API com 0 erros.
## Atualizacao 2026-03-31
- Concluido: Lista de Depositos (`ProductSimple/WarehouseListFront`) padronizada para retornar somente `Cï¿½digo` (ID) e `Nome`, com coluna controlada por VO dedicado de ListFront.
## Atualizacao 2026-03-31
- Concluido: Tipo de Produto (ListFrontVO) ajustado para exibir `Cï¿½digo` no lugar de `Id`, sem alterar as demais colunas.
## Atualizacao 2026-03-31
- Concluido: `/Supplier/GetAll` sem coluna `Status` no ListFront (coluna `statusDescription` removida do retorno).
## Atualizacao 2026-03-31
- Planejando: criar modulo de CST ICMS seguindo padrao dos complementares (tabela propria + Save/Update/Prepare/Delete + SO + ListFrontVO).
- Concluido: criada entidade `ProductCstIcmsComplementary` com configuracao EF e relacionamento no `ApplicationDbContext`/`Product`.
- Concluido: implementados metodos de repositorio, service e controller para `GetCstIcmsSO`, `PrepareCstIcms`, `SaveCstIcms`, `UpdateCstIcms`, `DisableCstIcms`.
- Concluido: criado ListFront dedicado `GetCstIcmsListFront` com colunas `Cï¿½digo CST` e `Nome` (incluindo fallback em lista vazia).
- Observacao: migration nao foi executada por solicitaï¿½ï¿½o; somente estrutura pronta no codigo para voce rodar migration localmente.
## Atualizacao 2026-03-31
- Concluido: ListFrontVO de Produtos alterado de `SKU` para `Cï¿½digo de barras`.
- Concluido: a coluna continua no campo tecnico `codeId`, mas agora recebe o valor de `barcode` no backend para refletir corretamente o pedido.
## Atualizacao 2026-03-31
- Planejando: padronizar deletes (disable) com mensagem correta e bloqueio por vinculo em produto.
- Concluido: deletes de generics/complementares/fornecedor agora validam vinculo com produto antes de desabilitar.
- Concluido: mensagens de sucesso de delete padronizadas (sem texto de atualizado) e erro descritivo com produto vinculado.
- Concluido: UNIDADES_MEDIDA em SO/formOptions foi padronizado para origem unica em ProductTypes (token PRODUTO_UNIDADE_MEDIDA).
- Concluido: ProductSimple/GetFormOptions passou a usar UnitMeasures da fonte principal e priorizar CstIcmsCombinado em CstEntry/CstExit.
## Atualizacao 2026-03-31
- Concluido: removidas ocorrencias de "generico/genï¿½rica/generic" em mensagens de retorno ao front para cadastros de produto e tipos de cadastro.
- Concluido: nomenclaturas substituidas por termos naturais (ex.: "cadastro", "tipo de cadastro").
## Atualizacao 2026-03-31
- Concluido: no ListFrontVO de NCM manual, coluna `Cï¿½digo NCM` agora retorna `NcmCode` (codigo ncm), sem uso de ID.
## Atualizacao 2026-03-31
- Concluido: ListFrontVO de CEST corrigido para mapear CEST/NCM na ordem correta.
- Concluido: coluna NCM agora retorna no padrao `{codigo} - {nome}` quando houver descricao cadastrada para o codigo NCM.

## Atualizacao 2026-03-31
- Planejando: migrar `CST_SIMPLES_NACIONAL`, `CST_TIPO` e `TIPOS_OPERACAO_FISCAL` de `ProductComplementaryJsonDatas` para tabelas fisicas, mantendo contrato de retorno para o front.
- Concluido: criadas entidades/tabelas fisicas dedicadas para os 3 tokens (sem vinculo com produto) e troca completa do consumo no `ProductComplementaryService` para repositorio fisico.
- Concluido: `SaveFormOptionsJson`/`CreateFormOptionsJson` passaram a persistir esses 3 tokens nas novas tabelas por upsert de `value+label` (com soft disable dos removidos), evitando duplicidade e contaminacao por uso em produto.
- Concluido: fallback de `GetAllDropdownSO`/`FormOptionsByToken` preservado para o front com mesmo payload de SelectObjectVO.
- Concluido: `/Supplier/GetAll` ajustado para coluna unica `CPF / CNPJ` no ListFrontVO (mantendo dados internos de CPF/CNPJ para prepare).
- Validado: `dotnet build PRISERP-BACK/PrisBackEnd.sln` com 0 erros de compilacao.
## Atualizacao 2026-03-31
- Concluido: mapeamento dos 3 tokens fisicos alinhado para persistencia no banco como `label=id` e `value=descricao`, mantendo retorno para front em `label=descricao` e `value=id` (sem quebrar contrato).
- Concluido: Product FormOptions ajustado para usar `CstSimplesNacional` em `CsosnOptions` e `TiposOperacaoFiscal` em `ListTypeOptions`.
- Concluido: `PackageReferences` em FormOptions passou a fonte unica da tabela complementar (sem fallback por token de types); `UnitMeasures` mantido em fonte unica de UnitMeasure.
- Validado: build de Infrastructure com 0 erros.
## Atualizacao 2026-03-31
- Concluido: criado `ClassificationListFront` em `ProductSimpleController` com origem exclusiva em `ProductSimpleProductClassifications` (categoria com 3 niveis), exibindo `Tipo principal`, `Tipo especializado` e `Tipo real`.
- Concluido: `id` do vinculo passou a ser retornado no row com visualizacao bloqueada (`Visible.Blocked`) no novo `ProductSimpleClassificationListFrontItemVO`.
- Concluido: criado `ClassificationDelete` (disable por `id`) com soft delete direto na tabela de vinculo `ProductSimpleProductClassifications`.
- Concluido: retornos de `TIPOS_OPERACAO_FISCAL`, `CST_SIMPLES_NACIONAL` e `CST_TIPO` no `ProductComplementaryService` agora padronizam label em maiusculo sem quebrar mapeamento `front(label=descricao,value=id)`.
- Validado: `dotnet build PRISERP-BACK/PrisBackEnd.API/PrisBackEnd.API.csproj --no-restore` com 0 erros.
## Atualizacao 2026-03-31
- Concluido: `PrepareSave` reforcado para retornar `Tax.Ncm` e `Tax.Cest` com fallback de payload fiscal (`tax` scope) e normalizacao de codigo.
- Concluido: `Save` de produto simples agora valida campos selecionaveis contra opcoes do backend (impostos, NCM, CEST, CFOP, CSOSN, categoria/classificacao, unidade, marca, secao, fornecedor, etc.).
- Concluido: normalizacao no save para persistir NCM/CEST somente como codigo (quando entrada vier em `{codigo} - {nome}`).
- Concluido: `POST /ProductSimple/ClassificationDelete` alterado para receber `token` (int) no payload, seguindo convensao solicitada.
- Concluido: ListFront de classificacao atualizado para metadado oculto como `Cï¿½digo` (nao `Id`).
- Validado: mapeamentos dos tokens antes-json (`TIPOS_OPERACAO_FISCAL`, `CST_SIMPLES_NACIONAL`, `CST_TIPO`) permanecem consumindo tabelas fisicas (sem `_jsonRepo`).
- Validado: `dotnet build PRISERP-BACK/PrisBackEnd.API/PrisBackEnd.API.csproj --no-restore` com 0 erros.
## Atualizacao 2026-03-31
- Concluido: nas tabelas fisicas de impostos migradas do json (`ProductOperationTypeComplementaries`, `ProductCstSimpleNationalComplementaries`, `ProductCstTypeComplementaries`), o modelo EF foi alterado de `label/value` para `codigo/descricao`.
- Concluido: repositorio e service ajustados para manter o contrato do front intacto (`label=descricao`, `value=codigo`).
- Validado: build API com 0 erros.
## Atualizacao 2026-03-31
- Concluido: SOs de `TIPOS_OPERACAO_FISCAL`, `CST_SIMPLES_NACIONAL` e `CST_TIPO` padronizados para retornar `label` no formato `{CODIGO} - {DESCRICAO}` em todos os pontos que consomem `GetCreatedOptionsByTokenAsync` (incluindo FormOptions e metodos por token).
- Concluido: mantido contrato do front sem quebra (`value` continua sendo o codigo).
- Validado: `dotnet build PRISERP-BACK/PrisBackEnd.API/PrisBackEnd.API.csproj --no-restore` com 0 erros.
## Atualizacao 2026-03-31
- Concluido: padrao de SO/FormOptions ajustado por tipo de imposto.
- Concluido: `CST_TIPO` e `TIPOS_OPERACAO_FISCAL` agora retornam somente `DESCRICAO` (sem `{codigo} - {descricao}` no `label`).
- Concluido: `{CODIGO} - {DESCRICAO}` mantido apenas para `CST_ICMS`, `CST_PIS_COFINS`, `CST_SIMPLES_NACIONAL` e `NCM` (manual e API).
- Concluido: normalizacao para maiusculo reforcada em SO/FormOptions e nas listagens internas de complementares para NCM/CST ICMS/CST PIS-COFINS.
- Concluido: save/update de `CST ICMS` e `CST PIS/COFINS` passaram a persistir em maiusculo.
- Validado: saves dos 3 tokens migrados de JSON seguem apenas tabelas fisicas (`ProductOperationTypeComplementaries`, `ProductCstSimpleNationalComplementaries`, `ProductCstTypeComplementaries`) sem dupla persistencia.
## Atualizacao 2026-03-31
- Concluido: `ListFrontVO` de Product Generics padronizado para retornar valores textuais em maiusculo no `GetListByTab` (incluindo CST PIS/COFINS e demais abas desse fluxo).
## Atualizacao 2026-03-31
- Concluido: ListFront de NCM (API) reforcado para ler campos de ato com fallback de chaves e evitar retorno vazio (`-` quando nao informado pela origem).
- Concluido: CEST deixou de mapear NCM no retorno da listagem; agora retorna exatamente o valor salvo/enviado pelo front no campo NCM.
## Atualizacao 2026-03-31
- Concluido: ANP no formOptions de produto agora vem somente de `ProductAnpCodeComplementaries` (removido fallback de `ProductFiscalCatalogs`).
- Validado: save/update/delete de cadastro ANP continuam no fluxo exclusivo de `ProductAnpCodeComplementaries`.
## Atualizacao 2026-03-31
- Concluido: Categoria (`ProductSimple`) ajustada para update/delete por `id` no payload (sem uso de `token`).
- Concluido: limpeza de fallback em SO/FormOptions para tabelas fisicas de produto (ANP, NCM, CEST, CST ICMS, CST PIS/COFINS, CST SIMPLES NACIONAL, TIPOS OPERACAO FISCAL) usando fonte unica da tabela dedicada.
- Concluido: removida composicao de opcoes fiscais via `ProductIcmsGroupComplementaries` para tokens que possuem tabela propria.

## Atualizacao 2026-03-31
- Em execucao: consolidacao final do fluxo de produto sem fallback em SO/FormOptions quando houver tabela fisica, incluindo categoria (update/delete por id) e limpeza de fontes alternativas.
- Concluido: categoria de produto simples ajustada para update/delete por id do vinculo; FormOptions/SO de produto limpos para priorizar exclusivamente fontes fisicas nos pontos ajustados (sem fallback estatico para armazem, unidade basica e setor local).
## Atualizacao 2026-04-02
- Planejando: adicionar `taxSituationCode` no Save/Prepare de Produto (campo tributario CBS/IBS) sem impacto de front-end visual e validar status das FKs em `ProductTaxes`.
- Em execucao: implementacao backend em VO + ProductSimpleService com persistencia em `extra_payload_json`.
- Concluido: `taxSituationCode` incluido no contrato de Save/Prepare (`ProductSimpleTaxSaveVO`) e mapeado no fluxo de gravacao/leitura.
- Validado: IDs fiscais em `ProductTaxes` existem como colunas, mas sem relacionamentos FK explicitos no `ProductTaxConfiguration`/snapshot para navegacao direta.
## Atualizacao 2026-04-02
- Concluido: `taxSituationCode` migrou para coluna fisica em `ProductTaxes` (`tax_situation_code`) com persistencia direta no save e retorno no prepare sem alterar contrato do front.
- Concluido: leitura de `taxSituationCode` no prepare com fallback legado para `extra_payload_json` apenas para compatibilidade de dados antigos.
- Concluido: `ProductTaxes` recebeu mapeamento FK explicito (EF) para ids fiscais (`GroupIcmsContrId`, `IcmsCstId`, `Pis/Cofins/Cst*`, `AnpCodeId`, `CsosnContrId`, `ItemTypePisCofinsId`).
- Concluido: update de `ProductTax` no repositorio passou a copiar `TaxSituationCode`.
- Validado: `dotnet build PRISERP-BACK/PrisBackEnd.API/PrisBackEnd.API.csproj --no-restore` com 0 erros.
## Atualizacao 2026-04-02
- Concluido: validacao de NCM SO unificado; nao existia endpoint unico para manual + BrasilAPI.
- Concluido: criado endpoint `GET /ProductComplementary/GetNcmUnifiedSO` unificando NCM cadastrado + NCM BrasilAPI com deduplicacao por codigo.
- Regra: em falha da BrasilAPI, retorna ao menos os NCM manuais quando disponiveis (fallback seguro).
- Validado: build API com 0 erros.
## Atualizacao 2026-04-02
- Concluido: padronizacao de referencia por ID para `Brand`, `Section` e `StorageSectorId` no fluxo de produto (save/update), normalizando selecoes pelo `Value` das opcoes de backend.
- Concluido: `PrepareSave` de produto passou a resolver `Brand` e `Section` para ID de `ProductTypes` com fallback legado (quando dado antigo estiver salvo em nome).
- Concluido: rotinas de busca/limpeza de vinculo generico no repositorio agora reconhecem tanto legado por nome quanto novo padrao por ID (`Brand`/`Section`/`ProductType`).
- Validado: `dotnet build PRISERP-BACK/PrisBackEnd.Infrastructure/PrisBackEnd.Infrastructure.csproj --no-restore` com 0 erros.
## Atualizacao 2026-04-02
- Concluido: mapeamento de persistencia por ID com FKs fisicas para campos de referencia de produto simples.
- Concluido: `Brand` agora persiste em `products.brand_id` (FK para `ProductTypes`).
- Concluido: `Section` agora persiste em `product_simple_data.section_id` (FK para `ProductTypes`).
- Concluido: `StorageSectorId` agora persiste em `product_simple_data.storage_sector_id` como inteiro (FK para `ProductScaleSectors`).
- Concluido: `FormOptions` de `storageSectorId` passou a vir da tabela de setores (`ProductScaleSectors`) com IDs.
- Concluido: `PrepareSave` mantï¿½m retorno compativel para front (IDs em string), com fallback legado quando necessario.
## Atualizacao 2026-04-02
- Concluido: mapeamento de `ProductSimpleData` padronizado para tabela `ProductSimpleDatas` (removida referencia hardcoded a `product_simple_data`).
- 2026-04-02: [BACK][ProductSimple/FormOptions] payload ampliado para retorno completo de seletores necessarios (formatos, condicoes, tipos basicos, CST PIS/COFINS combinado, ANP, usados, percentual combustivel, UFs e taxSituationCodeOptions), mantendo compatibilidade com contratos atuais.
- 2026-04-02: [BACK][ProductSimple] corrigido update de `SectionId` e `TermSalePrice` no upsert de `ProductSimpleData`; corrigida validacao de `CST IPI` para aceitar codigo (`00`, `49`, etc.) no save/update.
- 2026-04-02: [BACK][ProductSimple] regra de status ajustada: `isActive=false` no Save/SetStatus nao marca mais `DisabledAt`; produto permanece editavel. Validacao de CST PIS/COFINS entrada/saida movida para tabela fisica (`ProductCstPisCofinsComplementaries`) por codigo/id.
- 2026-04-02: [BACK][ProductSimple] separado CFOP entrada/saida no cadastro simples: mantido `cfopContr` como entrada e criado `cfopCons` para saida, com retorno no PrepareSave e validacao no Save.
- 2026-04-02: [BACK][ProductSimple] renomeado CFOP de saida para `cfopContrExit` (mantendo `cfopContr` para entrada), com fallback de leitura de payload legado `cfopCons` no PrepareSave.

## [2026-04-02 15:52:24] BACKLOG - Corrigir duplicidade de mensagens no Save de Produto
- Tipo: BUG
- Escopo: PRISERP-FRONT/src/components/ui/Form/Form/Form.tsx e PRISERP-FRONT/src/features/product/hooks/useProductAdd.ts.
- Critï¿½rio: impedir toast de erro quando o fluxo final de save foi concluï¿½do com sucesso.
- Observaï¿½ï¿½o: manter contrato atual do back e comportamento de negï¿½cio.

## [2026-04-02 16:21:24] BUG - Save de produto com lote automï¿½tico falhando no SaveChanges
- Sintoma: falha em EnsureAutomaticLotStockByExpirationAsync ao persistir estoque/lote automï¿½tico.
- Causa provï¿½vel validada: uso de lot.Id antes de confirmaï¿½ï¿½o de persistï¿½ncia do lote (PK real).
- Status: corrigido no backend com persistï¿½ncia antecipada do lote e validaï¿½ï¿½o de id > 0.

## [2026-04-02 16:27:31] INVESTIGAï¿½ï¿½O - Save produto com erro sem detalhe (lote automï¿½tico)
- Objetivo: expor motivo tï¿½cnico real de falha no backend (SaveChanges/lote automï¿½tico).
- Aï¿½ï¿½o: melhorar propagaï¿½ï¿½o de erro interno e logging contextual no mï¿½todo de lote automï¿½tico.

## Atualizacao 2026-04-02
- Planejando: Bugfix backend de save de produto com erro paralelo de menu e ajuste de horario persistido no banco.
- Contrato criado e pronto para backend: product-simple-save-menu-permission-datetime-fix.contract.json
- Concluido: MenuController corrigido para validar Result.IsFailed antes de acessar Value em GetMenuPermissionsByUser/GetMenusByUserAsync.
- Concluido: GetMenuPermissionsByUser passou a retornar permissao padrao quando rota nao estiver cadastrada (sem falha/excecao no fluxo).
- Concluido: ProductSimpleService ajustado para persistir timestamps do fluxo de produto em horario de Sao Paulo.

## Atualizacao 2026-04-02
- Planejando: corrigir erro de save de produto para CST IPI (FK indevida em ProductTaxes para cst_ipi_entry_id/cst_ipi_exit_id).
- Concluido: removido vinculo FK de CstIpiEntryId/CstIpiExitId com ProductCstIcmsComplementaries no mapeamento EF.
- Concluido: ajuste de regra de uso em ProductRepository para ICMS CST considerar apenas IcmsCstId (sem CstIpiEntryId/CstIpiExitId).
## Atualizacao 2026-04-02
- Planejando: corrigir erro de save de produto para CST IPI (FK indevida em ProductTaxes para cst_ipi_entry_id/cst_ipi_exit_id).
- Concluido: removido vinculo FK de CstIpiEntryId/CstIpiExitId com ProductCstIcmsComplementaries no mapeamento EF.
- Concluido: ajuste de regra de uso em ProductRepository para ICMS CST considerar apenas IcmsCstId (sem CstIpiEntryId/CstIpiExitId).

## [2026-04-02 17:13:59] BACKLOG - Save Produto (productType + CST IPI)
- Tipo: BUG
- Escopo: PRISERP-BACK/PrisBackEnd.Infrastructure/ServicesImpl/API/ProductSimpleService.cs.
- Critï¿½rio 1: update deve priorizar e persistir productType enviado pelo front (sem manter valor antigo por itemType).
- Critï¿½rio 2: CST IPI deve aceitar codigo (ex.: 00/50), persistir e retornar no PrepareSave.
- Critï¿½rio 3: manter contrato atual com o front sem quebra.

## [2026-04-02 17:26:51] BACKLOG - CST IPI (000/0) no Save e Prepare
- Tipo: BUG
- Escopo: ProductSimpleService (validacao, resolucao de IDs e retorno de prepare).
- Critï¿½rio 1: aceitar entrada  00/  para CST IPI e persistir em cst_ipi_entry_id/cst_ipi_exit_id.
- Critï¿½rio 2: no PrepareSave, resolver ID salvo contra token CST_IPI e devolver codigo ao front.
- Critï¿½rio 3: manter compatibilidade sem alterar contrato do front.

## [2026-04-02 17:34:48] BACKLOG - Fluxo ID-only em complementares fiscais
- Tipo: Refatoracao
- Escopo: remover fallbacks por texto nos bloqueios de delete (ICMS CST, CST PIS/COFINS, ANP), mantendo verificacao somente por IDs de ProductTaxes.
- Critï¿½rio: sem mudanca de contrato para o front; somente logica interna de consistencia.

## [2026-04-02 20:15:00] BACKLOG - Migration final de limpeza de colunas legadas fiscais
- Tipo: Refatoracao de persistencia
- Objetivo: remover colunas texto legadas de ProductTaxes jï¿½ substituï¿½das por *_id, sem alterar contrato do front.
- Critï¿½rio 1: VO/API inalterados.
- Critï¿½rio 2: persistï¿½ncia e validaï¿½ï¿½es por ID mantidas.
- Critï¿½rio 3: build do backend verde apï¿½s limpeza.

- 2026-04-06: Sessao ROVIS-FE reativada neste atendimento; classificacao da tarefa atual como FRONT_LOGIC (orquestracao operacional), com gate obrigatorio lido (04-frontend, front-end/*, 00-context), sem inicio de backend e sem alteracao de contratos.

- 2026-04-06: FRONT_LOGIC - /adm/produto/editar com validacao obrigatoria pre-save para descricao, grupo, barcode, manageStock, estoques (>=0), termSalePrice (>=0) e campos fiscais obrigatorios/taxas nao negativas em productTax; campos visuais marcados como required.

- 2026-04-06: FRONT_LOGIC - ajuste complementar /adm/produto/editar: required adicional em Tributacao (Grupo ICMS, CFOP entrada/saida e CSTs/CSOSN), required adicional em Dados basicos (GTIN tributado, barras caixa, SKU) e remocao de required em Controla estoque.

- 2026-04-06: FRONT_LOGIC - ajuste visual no /adm/produto/editar para destacar Nome do produto como obrigatorio com asterisco no label (campo ja validado como required no submit).

- 2026-04-06: VISUAL_ONLY - /adm/produto/editar aba Tributacao: label atualizado de CFOP de entrada para CFOP de saida fora de estado.

- 2026-04-06: FRONT_LOGIC - reforco de required na tributacao com indicador visual (*) em todos os campos solicitados: Grupo ICMS, CFOP de saida fora de estado, CFOP de saida, CSOSN, CST PIS Entrada/Saida, CST COFINS Entrada/Saida e CST IPI Entrada/Saida.

- 2026-04-06: VISUAL_ONLY - indicador visual (*) adicionado nos labels de Codigo de barras (GTIN/EAN), Codigo de barras (GTIN/EAN Tributado) e Codigo agrup./barras caixa em /adm/produto/editar.

- 2026-04-06: FRONT_LOGIC - /adm/produto/editar: removida obrigatoriedade de group no pre-save (campo interno), eliminando erro indevido Grupo e obrigatorio.

- 2026-04-06: FRONT_LOGIC - endurecimento do pre-save em /adm/produto/editar: validacao agora usa somente estado atual do formulario (sem fallback de prepare), barrando save para todos os required e regras de nao-negativo antes da persistencia.

- 2026-04-06: FRONT_LOGIC - /adm/produto/editar: removida duplicidade de toast na validacao pre-save (agora apenas uma), removida obrigatoriedade de itemType e mantido retorno de erro via fluxo do Form antes do save.

- 2026-04-06: FRONT_LOGIC - correï¿½ï¿½o de bypass dos required em /adm/produto/editar: validacao de Nome, EAN, GTIN Tributado, barras caixa e SKU agora estrita no campo da UI (sem fallback por aliases internos).

- 2026-04-06: ROVIS-BE - Save de produto simples sem obrigatoriedade de WarehouseName/WarehouseId. Regra: quando nao vier deposito valido, usar deposito ativo existente da empresa; se nao existir, criar automaticamente (fallback DEPOSITO_GERAL).
- 2026-04-07: CONTRACT_CONSUMPTION - /adm/grupoicms (adicionar/editar): removido campo tipo e adotado csosnId no payload; CSOSN carregado de GET /ProductSimple/FormOptions (csosnOptions); modal reorganizado para linhas [Grupo Usado no ECF + ICMS/SERVICO], [Nome do grupo ICMS + Aliquota], [CST + CSOSN].
- 2026-04-07: FRONT_LOGIC + CONTRACT_CONSUMPTION - /adm/produto/editar (aba Tributacao): modal de Grupo ICMS alinhado ao novo objeto (remocao de tipo + inclusao de csosnId via ProductSimple/FormOptions.csosnOptions), remocao do campo CSOSN fora do modal e retirada da obrigatoriedade de CSOSN no pre-save; grid da linha ajustado para exibir somente CEST e NCM.
- 2026-04-07: FRONT_LOGIC - /adm/produto/adicionar (aba Tributacao) alinhada ao editar: removido CSOSN fora do modal de Grupo ICMS, CSOSN retirado da validacao de obrigatorios da etapa e grid da segunda linha ajustado para conter somente CEST e NCM.
- 2026-04-07: VISUAL_ONLY - ListPage/DataTable com nova prop de tipografia condicional (useAlternateListTypography): quando habilitada, headers das colunas em 14px negrito e textos das rows em 12px com fonte mais fina; ativado em /adm/produto para visualizacao.
- 2026-04-07: VISUAL_ONLY - tipografia de listas agora com default global da prop useAlternateListTypography=true no DataTable; reversao futura simples por tela com useAlternateListTypography={false}.

- 2026-04-06: ROVIS-BE - ListFrontVO de Produto ajustado para exibir o label 'Nome do produto' no campo Description.

- 2026-04-06: ROVIS-BE/FE - Grupo ICMS ajustado para usar CSOSN por ID (sem migration), substituindo o campo Tipo na lista e no modal.

- 2026-04-07: ROVIS-BE - Cadastro de Tipo de Empresa (BUSINESS_TYPE) com endpoints dedicados no EnterpriseController: SaveBusinessType (upsert), GetAllBusinessTypes (ListFrontVO) e GetBusinessTypeSelect (SelectObjectVO). Token e descricao travados no backend (BUSINESS_TYPE / Tipo de Empresa), front envia apenas id/name.

- 2026-04-07: ROVIS-BE - Enterprise: adicionar businessTypeId (FK GenericTypes token BUSINESS_TYPE) e isMei no cadastro completo (save/update/prepare/getall/form options), incluindo migration de banco.

## [2026-04-07] PM - SaveEnterpriseMEI (sem obrigatoriedade fiscal)
- Tipo: FEATURE
- Escopo: novo endpoint POST /Enterprise/SaveEnterpriseMEI para cadastro MEI sem exigir bloco fiscal no payload, mantendo businessTypeId/isMei.
- Regras: stateRegistration sempre 'ISENTO'; municipalRegistration sempre vazio para MEI; nao iniciar front-end.
- Status: planejando/aguardando aprovacao.

- 2026-04-07: PM ajuste solicitado pelo usuario para SaveEnterpriseMEI: validar obrigatoriedade de Taxes e viabilidade de zerar; manter Save atual intacto; criar VO dedicada para MEI.

- 2026-04-07: PM ajuste confirmado pelo usuario para SaveEnterpriseMEI: priorizar TaxesId fixo 640 (predefinido MEI) e usar GenericTypeId 732 como fallback para campos obrigatorios de Taxes quando necessario.

- 2026-04-07: ARCH - contrato criado .cursor/contracts/enterprise-save-mei.contract.json (endpoint dedicado sem expor taxesId/GenericTypeId no body), pronto para backend.

- 2026-04-07: BACK - SaveEnterpriseMEI implementado conforme contrato, com VO dedicada e sem expor taxesId/genericTypeId no body. Validacao de build concluida.

- 2026-04-07: ajuste incremental SaveEnterpriseMEI: removidos do body os campos de substituto tributario; persistencia interna fixada (stateRegistrationOfTheTaxSubstitute='ISENTO', federalUnitOfTheTaxSubstituteId=null).

## [2026-04-07 12:17:51] PM - Produto simples sem obrigatoriedade fiscal para empresa MEI
- Tipo: FEATURE
- Escopo: PRISERP-BACK/PrisBackEnd.Infrastructure/ServicesImpl/API/ProductSimpleService.cs
- Regra: no create de produto simples, quando a empresa for MEI, remover obrigatoriedade dos campos fiscais (tax) e respectivas validacoes de selecao fiscal.
- Restricoes: nao alterar banco e nao alterar comportamento para empresas nao-MEI.

## [2026-04-07 14:16:10] PM - Tabela de Tipos Genéricos Farmacêuticos (estilo GenericTypes)
- Tipo: FEATURE
- Escopo: backend com tabela própria, CRUD básico e endpoints de listagem/select para futura aba farmacêutica de produto.
- Regras aprovadas: sem front-end; estrutura similar a GenericTypes; campo `value` como string.
- Fluxo: PM aprovado -> ARCH contrato -> BACK implementar e validar.
- 2026-04-07: [BACK][Farmaceutico/FormOptions] endpoint GET /PharmaceuticalGenericType/GetFormOptions adicionado. Primeiro bloco: Portaria 344 (token PORTARIA344) retornando SO com label=description e value=id da ProductPharmaceuticalGenericTypes.
- 2026-04-07: [BACK][Farmaceutico/FormOptions] adicionado TarjaOptions no GET /PharmaceuticalGenericType/GetFormOptions usando token TARJA (label=name, value=id).
- 2026-04-07: [BACK][Produto Simples] removida obrigatoriedade de tax.csosnContr no create para todos os cenários.
- 2026-04-07: ROVIS-BE - Produto simples: tax.csosnContr deixou de ser obrigatório para todos os cenários (create/update), inclusive na validação de seleção de opções.
- 2026-04-10: Sessao ROVIS ativada neste atendimento; usar obrigatoriamente arquivos de .cursor, passar por [PM] antes de qualquer execucao tecnica e registrar planejamento/historico em .cursor/memory.
- 2026-04-10: AI-TESTING acoplado ao modo ROVIS nesta sessao; engine fica reservado para disparo automatico em implementacoes concluidas ou pedidos explicitos de teste.

## 2026-04-10 - Governanca ROVIS v2
Data: 2026-04-10
Agente: ROVIS
Status: concluido
Resumo:
- Governanca consolidada com bootstrap unico, init roteador, estados canonicos, contrato de memoria e scripts oficiais de automacao/lint.
- Pasta .cursor/memory migrada para UTF-8 valido.

## 2026-04-10 - Memoria ROVIS v3
Data: 2026-04-10
Agente: ROVIS
Status: concluido
Resumo:
- Modelo hot/cold implementado com index, session summary, active workset e snapshots em archive.
- Leitura inicial do ROVIS agora prioriza memoria quente.

## 2026-04-11 - Ativacao ROVIS da sessao
Data: 2026-04-11
Agente: ROVIS
Estado: DONE
Modo: ROVIS
Origem: pedido explicito do usuario para ativar governanca ROVIS com bootstrap como fonte principal, state-machine para precedencia e memory-contract para politica de escrita.
Proxima acao: receber a proxima demanda iniciando obrigatoriamente por [PM] e exigir 'aprovado' antes de qualquer implementacao tecnica.

## 2026-04-11 - Automacao de ativacao curta por modo
Data: 2026-04-11
Agente: ROVIS
Estado: DONE
Tipo: governance
Escopo: permitir que o usuario informe apenas o modo desejado e deixar a injecao das fontes obrigatorias automatica no ponto de entrada da sessao.
Arquivos alvo:
- .cursor/init.md
- .cursor/bootstrap.md
Proxima acao: usar comandos curtos como 'modo ROVIS-FE' sem repetir o prompt completo.

## 2026-04-11 - ROVIS Core vNext - manifesto e roteador
Data: 2026-04-11
Agente: ROVIS
Estado: DONE
Tipo: governance
Escopo: consolidar modos, roteamento de entrada e validacao mais rigida do nucleo operacional do ROVIS.
Arquivos alvo:
- .cursor/governance/mode-manifest.json
- .cursor/governance/intent-router.md
- .cursor/scripts/Get-RovisRouting.ps1
- .cursor/scripts/Test-RovisGovernance.ps1
- .cursor/scripts/Compress-RovisMemory.ps1
Proxima acao: usar o manifesto e o roteador como base canonica para proximas evolucoes.

## 2026-04-11 - ROVIS Capability Matrix - capacidades por agente
Data: 2026-04-11
Agente: ROVIS
Estado: DONE
Tipo: governance
Escopo: consolidar capacidades, bloqueios, leituras obrigatorias e gates por agente/modo.
Arquivos alvo:
- .cursor/governance/agent-capabilities.json
- .cursor/agents/01-orchestrator.md
- .cursor/agents/08-rovis-fe.md
- .cursor/agents/09-rovis-be.md
- .cursor/agents/11-ai-testing.md
- .cursor/scripts/Test-RovisGovernance.ps1
Proxima acao: usar a matriz para ampliar delegacao segura, handoff e bloqueios de drift.

## 2026-04-11 - ROVIS Handoff Engine - contrato e validacao
Data: 2026-04-11
Agente: ROVIS
Estado: DONE
Tipo: governance
Escopo: transformar handoff e scorecard em contrato canonico com validacao executavel.
Arquivos alvo:
- .cursor/governance/handoff-contract.json
- .cursor/scripts/Check-RovisHandoff.ps1
- .cursor/agents/10-agent-scorecard.md
- .cursor/scripts/Test-RovisGovernance.ps1
Proxima acao: usar o Handoff Engine como base para bloquear encerramentos incompletos e futuras automacoes de scorecard.

## 2026-04-11 - ROVIS Stage Score Engine - scorecard por etapa
Data: 2026-04-11
Agente: ROVIS
Estado: DONE
Tipo: governance
Escopo: transformar scorecard em contrato executavel por estado com validacao automatica.
Arquivos alvo:
- .cursor/governance/stage-score-rules.json
- .cursor/scripts/Check-RovisStageScore.ps1
- .cursor/agents/10-agent-scorecard.md
- .cursor/scripts/Test-RovisGovernance.ps1
Proxima acao: usar o motor por etapa para evoluir bloqueios de encerramento e scorecards mais automaticos.

## 2026-04-11 - ROVIS Closeout Guard + QA Real Targets
Data: 2026-04-11
Agente: ROVIS
Estado: DONE
Tipo: governance
Escopo: bloquear encerramento incoerente e conectar AI-TESTING a targets/features reais canonicamente resolvidos.
Arquivos alvo:
- .cursor/governance/closeout-contract.json
- .cursor/governance/qa-targets-contract.json
- .cursor/scripts/Check-RovisCloseout.ps1
- .cursor/scripts/Resolve-RovisQATargets.ps1
- .cursor/testing-module/scripts/Run-AIEngine.ps1
- .cursor/testing-module/ai-engine/src/generators/aiTestGenerator.ts
Proxima acao: usar o guard para fechamento e o resolver para futuras baterias reais de QA.

## 2026-04-13 - ROVIS Runtime Executor - sistema nervoso operacional
Data: 2026-04-13
Agente: ROVIS
Estado: DONE
Tipo: governance
Escopo: introduzir resolvedor de proxima acao e executor de etapa guiados por estado, com smoke tests no validator oficial.
Arquivos alvo:
- .cursor/governance/runtime-executor.json
- .cursor/scripts/Resolve-RovisNextAction.ps1
- .cursor/scripts/Run-RovisStage.ps1
- .cursor/scripts/Test-RovisGovernance.ps1
Proxima acao: usar o runtime executor como base para automacoes reais de transicao e bloqueio operacional.

## 2026-04-30 - WriteOff Save com VehicleIds
Data: 2026-04-30
Agente: PM
Status: AWAITING_APPROVAL
Demanda: alterar Save de WriteOff para usar WriteOffSaveVO, validar VehicleIds por AssociateId e gravar WriteOffId nos AssociateRegistrationDraftVehicle apos insert.

## 2026-04-30 - WriteOff ReasonId
Data: 2026-04-30
Agente: PM
Status: AWAITING_APPROVAL
Demanda: remover dependencias remanescentes de Reason em WriteOff e ajustar validacao para ReasonId/WriteOffReason.
Build atual: 4 erros CS1061 em WriteOffService.cs por uso de model.Reason.

## 2026-04-30 - CRUD WriteOffReason
Data: 2026-04-30
Agente: PM
Status: AWAITING_APPROVAL
Demanda: criar CRUD completo para WriteOffReason com interfaces, repository, service, controller, VOs, profile, DI e contratos.
Regra: no Save da service, ManagementAssociationId deve vir do usuario logado/ManagementSelectedId.

## 2026-04-30 - Regra sem var
Data: 2026-04-30
Agente: ROVIS
Estado: Concluido
Ultima acao: Variaveis tipadas explicitamente nos arquivos tocados e regra registrada em .cursor/rules.md e .cursor/rules/backend.mdc.
Arquivos: ProRataService.cs; .cursor/rules.md; .cursor/rules/backend.mdc; .cursor/memory/05-decisions.md
Responsavel: ROVIS

## 2026-04-30 - Frontend ProRata na Intencao de Baixa
Data: 2026-04-30
Agente: ROVIS_FRONT
Estado: Concluido
Ultima acao: Card de calculo por veiculo implementado na etapa Dados da baixa e integrado ao endpoint ProRata/GetWriteOff.
Arquivos: ABPAC-FrontEnd/src/pages/localizar/detalhes/index.tsx; ABPAC-FrontEnd/src/config/apiRoutes/proRata.ts
Responsavel: FRONTEND

## 2026-04-30 - Historia 3 - Coberturas anteriores
Data: 2026-04-30
Agente: ROVIS_FRONT
Estado: Concluido
Ultima acao: Coberturas anteriores permanecem destacadas, mas nao entram marcadas automaticamente no TDO.
Arquivos: ABPAC-FrontEnd/src/pages/localizar/detalhes/index.tsx
Responsavel: FRONTEND

## 2026-05-16 - Ativacao do modo ROVIS na sessao atual
Data: 2026-05-16
Agente: ROVIS
Estado: Concluido
Ultima acao: Modo ROVIS ativado na pasta .cursor com health check oficial sem criticos e loop nao detectado.
Arquivos alvo:
- .cursor/bootstrap.md
- .cursor/governance/state-machine.md
- .cursor/governance/memory-contract.md
- .cursor/governance/mode-manifest.json
- .cursor/agents/01-orchestrator.md
- .cursor/memory/11-session-summary.md
- .cursor/memory/12-active-workset.md
Responsavel: ROVIS
