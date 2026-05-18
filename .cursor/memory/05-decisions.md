# Decisões Técnicas

## Template
Data:
Decisão:
Motivo:
Alternativas:
Impactos:
## 2026-04-30 - Proibir uso de var
Data: 2026-04-30
Decisao: Nao usar `var` em hipotese alguma no codigo novo ou alterado; declarar tipos explicitos em variaveis locais.
Motivo: Padrao solicitado pelo usuario para melhorar legibilidade, revisao e consistencia do projeto.
Alternativas: Permitir inferencia com `var` em casos obvios, mas foi descartado pela regra explicita do usuario.
Impactos: Revisoes futuras devem verificar `var` antes de finalizar; limpezas em codigo legado devem ser tratadas como refatoracao separada quando houver aprovacao.
