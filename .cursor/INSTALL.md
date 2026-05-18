# ROVIS - Guia de Instalacao e Reset

> **Onde voce esta agora**: `D:\RovisMark5` e o **master** do ROVIS. Cada projeto recebe uma copia independente.

---

## 1. Pre-requisito (so na primeira vez na maquina)

Abre **PowerShell** (nao Git Bash) e roda **uma unica vez**:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Confirma com `S`. Isso libera scripts `.ps1` so pro seu usuario. Nunca mais voce esbarra no erro de seguranca.

Verificar se ja esta liberado:
```powershell
Get-ExecutionPolicy -Scope CurrentUser
```
(Se aparecer `RemoteSigned` ou `Unrestricted`, ja esta ok)

---

## 2. Instalar ROVIS num projeto novo

### Comando padrao
```powershell
cd D:\RovisMark5
.\.cursor\scripts\Initialize-Rovis.ps1 -Project "C:\caminho\do\projeto"
```

### Se a pasta do projeto nao existe ainda
```powershell
.\.cursor\scripts\Initialize-Rovis.ps1 -Project "C:\projeto-novo" -Force
```

### So pra ver o que faria, sem escrever nada
```powershell
.\.cursor\scripts\Initialize-Rovis.ps1 -Project "C:\projeto" -DryRun
```

### Se ja tem `.cursor` no projeto e voce quer sobrescrever
```powershell
.\.cursor\scripts\Initialize-Rovis.ps1 -Project "C:\projeto" -Force
```
> Isso so sobrescreve **CORE** (scripts/agentes/governance). Memoria do projeto e contratos sao preservados.

### Pular profile/health pos-install (mais rapido)
```powershell
.\.cursor\scripts\Initialize-Rovis.ps1 -Project "C:\projeto" -SkipProfile -SkipHealth
```

---

## 3. Depois de instalar

```powershell
cd C:\caminho\do\projeto
```

Abre o Cursor nessa pasta e digita no chat:

```
modo ROVIS
```

ROVIS ja vai:
- Detectar a stack do projeto (npm/dotnet/python/etc)
- Rodar health check
- Estar pronto pra trabalhar

---

## 4. Resetar memoria do projeto

> Sempre **dentro da pasta do projeto**. Sempre faz snapshot antes em `.cursor/memory/archive/<timestamp>-<scope>/`.

### Limpar logs e metricas (mantem backlog/done)
```powershell
.\.cursor\scripts\Reset-RovisMemory.ps1 -Scope memory
```

### Limpar so a sessao atual (checkpoint, workset, planning ativo)
```powershell
.\.cursor\scripts\Reset-RovisMemory.ps1 -Scope state
```

### Reset completo (exige -Force pra confirmar)
```powershell
.\.cursor\scripts\Reset-RovisMemory.ps1 -Scope all -Force
```

---

## 5. Erros comuns

### "Initialize-Rovis.ps1 nao pode ser carregado porque a execucao de scripts foi desabilitada"
Voce pulou a Secao 1. Roda:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### "command not found" ou prompt comeca com `$` MINGW64
Voce esta no **Git Bash**, nao no PowerShell. Abre PowerShell de verdade (Win+R -> `powershell`).

### ".cursor ja existe em C:\..."
Use `-Force`:
```powershell
.\.cursor\scripts\Initialize-Rovis.ps1 -Project "C:\projeto" -Force
```

### "Projeto nao existe"
Use `-Force` (cria a pasta):
```powershell
.\.cursor\scripts\Initialize-Rovis.ps1 -Project "C:\projeto-novo" -Force
```

---

## 6. Levar pra outra maquina

ROVIS nao tem instalador online. Pra usar em outro PC:

1. Copia a pasta `D:\RovisMark5` inteira (pendrive / drive / git clone)
2. Na nova maquina, faz a Secao 1 (Set-ExecutionPolicy) uma vez
3. Roda os comandos da Secao 2 normalmente

---

## 7. Cheat sheet (cole no seu OneNote / Sticky Notes)

```powershell
# liberar scripts (1 vez por maquina)
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# instalar em projeto novo
cd D:\RovisMark5
.\.cursor\scripts\Initialize-Rovis.ps1 -Project "C:\meu-projeto" -Force

# usar
cd C:\meu-projeto
# (no Cursor): modo ROVIS

# resetar
.\.cursor\scripts\Reset-RovisMemory.ps1 -Scope memory
.\.cursor\scripts\Reset-RovisMemory.ps1 -Scope state
.\.cursor\scripts\Reset-RovisMemory.ps1 -Scope all -Force
```

---

## 8. O que e copiado

| Categoria | Quantos | O que e |
|---|---|---|
| **CORE** | ~90 arquivos | scripts, agentes, governance, rules |
| **TEMPLATE** | ~75 arquivos | testing-module (engine de QA) |
| **SEEDS** | 13 arquivos | memoria vazia |
| **TOTAL** | ~178 arquivos | tudo que ROVIS precisa |

**Nao copia**: node_modules, dist, build, .git, .next, coverage, relatorios antigos.

Detalhes em `.cursor/governance/portable-manifest.json`.
