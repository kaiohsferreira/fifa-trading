# Workflow Feature com contrato

0) ROVIS confirma estado correto, agente correto e anuncia troca de agente
1) PM cria plano e pede aprovacao
2) Usuario aprova e planning-log vira aprovado
3) ARCH gera contratos
4) ROVIS entra em CONTRACT_READY
5) Backend implementa baseado no contrato
6) Backend valida contrato
7) Frontend le contrato (gate de leitura do contexto ok)
8) Frontend implementa
9) QA valida
10) Reviewer fecha
11) Atualizar backlog e implementation-log ao final de cada etapa
