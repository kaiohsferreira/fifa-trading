# Done

(vazio)


## 2026-04-30 - WriteOff Save com veiculos concluido
Data: 2026-04-30
Agente: ROVIS_BE
Entrega: Save de WriteOff passou a aceitar WriteOffSaveVO, validar VehicleIds e vincular WriteOffId nos AssociateRegistrationDraftVehicle apos insert.
Validacao: build OK.

## 2026-04-30 - WriteOff ReasonId concluido
Data: 2026-04-30
Agente: ROVIS_BE
Entrega: WriteOff passou a usar ReasonId no fluxo de Save, validando WriteOffReason por associacao selecionada e removendo referencias remanescentes a Reason string no service.
Validacao: build OK; AI-TESTING bloqueado por falha interna do runner.

## 2026-04-30 - CRUD WriteOffReason concluido
Data: 2026-04-30
Agente: ROVIS_BE
CRUD de WriteOffReason concluido e compilando. Endpoints adicionados: GetAllSelect, GetAll, Prepare, Save e Delete. Contratos adicionados em .cursor/contracts para os fluxos do CRUD.

## 2026-04-30 - Cancelamento de WriteOff concluido
Data: 2026-04-30
Agente: ROVIS_BE
Cancelamento de WriteOff concluido. Contrato write-off-cancel.contract.json criado e API exposta em POST /WriteOff/Cancel?id={id}.

## 2026-04-30 - GetRenderedDocument WriteOff concluido
Data: 2026-04-30
Agente: ROVIS_BE
GetRenderedDocument de WriteOff concluido com contrato write-off-get-rendered-document.contract.json, VO, interface, controller, service e builder privado BuildRenderedDocumentHtmlAsync.

## 2026-05-04 - Historia 3 TDO faltantes concluidos
Data: 2026-05-04
Agente: ROVIS
Entrega: completado retorno real de metadados TDO no endpoint de placas, consumo frontend desses metadados e transferencia de protecoes com equipamento para o veiculo copiado na finalizacao, mantendo desativacao do original.

## 2026-05-05 - WriteOff GetAllPendingPaged entregue
Data: 2026-05-05
Agente: ROVIS_BE
Estado: DONE
Entrega: metodo/endpoint backend GetAllPendingPaged criado para WriteOff Pending por ManagementSelectedId.
Validacao: build isolado OK com 0 errors; AI-TESTING tentou validar, mas ficou bloqueado por ambiente (codex CLI ausente e API local indisponivel).
Commit sugerido: feat(write-off): add pending paged listing endpoint.
