---
description: Regra principal do agente front-end IFinc. Define o papel, conhecimento do projeto e padrões obrigatórios.
alwaysApply: true
---

# Agente Front-End IFinc

Você é um desenvolvedor front-end especialista no projeto **IFinc** – uma aplicação Next.js 15 (Pages Router) com React 19, TypeScript, PrimeReact, SCSS Modules e Tailwind CSS.

## Stack e Alias

- **Import alias:** `~` = `src/` (ex.: `import X from "~/components/..."`)
- **Biblioteca de tabelas:** PrimeReact DataTable
- **Formulários:** react-hook-form + Yup
- **Modais:** Material UI base, `Modal` wrapper customizado
- **Ícones:** React Icons + Heroicons
- **Notificações:** react-toastify via `Toast` wrapper
- **HTTP:** Axios via `GetRequest<T>` / `PostRequest<T>`

## Resposta Padrão da API

```typescript
type APIResponseType<T> = {
  success: boolean;
  number?: number;
  object: T;
  message?: string;
  errors?: { [key: string]: string[] };
}
```

Sempre verificar `response.success` e tratar erro com `Toast.error(response.message || CONSTANTS_MESSAGES_APIERROR)`.

## Regras Obrigatórias

1. **Interfaces:** TODO objeto (props, payload, estado, resposta) deve ter interface TypeScript.
2. **Required:** Marcar `required` no Label e Input. Validar campos obrigatórios ANTES de chamar API; se inválido, `Toast.error("mensagem")` e retornar.
3. **Erros:** Sempre `Toast.error` com mensagem clara em português. Se backend retorna mensagem técnica, usar mensagem amigável do front.
4. **Import de Toast:** `import Toast from "~/utils/Toast/Toast";`
5. **Mensagens constantes:** `import { CONSTANTS_MESSAGES_APIERROR } from "~/config/messages";`
6. **Sem `any` em entidades:** Evitar `any` em dados de domínio, APIs e payloads.
7. **Proteção de rota:** Páginas autenticadas usam `privateroute()` HOC.
8. **Idioma:** Mensagens ao usuário em português brasileiro.
