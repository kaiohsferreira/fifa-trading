## Orquestrador do sistema
Nome: ROVIS
Descrição: sistema de orquestração de desenvolvimento assistido por IA.

# Contexto do Projeto

## Stack
- Backend: .NET 8, EF Core, ASP.NET Identity, JWT
- Frontend: React 19, TypeScript, Vite, TailwindCSS, MUI/PrimeReact, Tauri
- Banco: PostgreSQL (principal), MongoDB (uso pontual)
- Infra: AWS S3, RabbitMQ, Azure DevOps (CI/CD)

## Padrões atuais
- Arquitetura: Clean Architecture + DDD
- Estrutura de pastas: projetos por camada no backend; feature-based no frontend
- Padrão de erro: resultados/fluxos com FluentResults
- Padrão de logs: NLog

## Convenções
- Nomeação: seguir padrões da stack (C# PascalCase; frontend camelCase)
- Rotas: definidas em `src/routes`
- Testes: a confirmar (não identificado no levantamento inicial)

<!-- PROJECT_PROFILE_START -->
## [PROJECT PROFILE] (auto)
Atualizado: 2026-05-04 12:10

- Backend:  .NET (csproj), .NET solution
- Frontend: (nao detectado)
- DB:       EF Core
- Infra:    (nao detectado)

Endpoints detectados: 200 | Paginas: 0 | Scripts npm: 0
Detalhes: `.cursor/memory/cold/project-profile.json`
<!-- PROJECT_PROFILE_END -->
